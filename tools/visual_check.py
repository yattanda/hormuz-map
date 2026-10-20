"""画面写真の撮影と比較（課題46 D2・D3 で使った手順を道具にしたもの。設計書 tools/site-redesign-design.md §5-1・§5-2）

使い方（Python 3 と Playwright。ブラウザは手元の Chrome を使う）:
  python -X utf8 tools/visual_check.py shoot <docs_dir> <out_dir> [ページ ...]
  python -X utf8 tools/visual_check.py diff  <before_dir> <after_dir>
  python -X utf8 tools/visual_check.py sheet <before_dir> <after_dir> <out.html> [ページ ...]

- shoot：各ページを幅 1280・390 で全体を撮る。ページを省くと全19ページ
  - ファイルはブラウザの中で直接返す（簡易サーバーは同時の読み込みで取りこぼす）
  - 外への通信はすべて止める（解析・外部のデータ・画像）。外のデータを読むページは、その部分が空のまま写る
  - 時計は --now（既定 2026-10-20T12:00:00+09:00）から進める。/hormuz/ の地図の印のように時刻で変わるものをそろえるため
  - 下までスクロールしてから、書体の読み込みと用語集の下線（requestIdleCallback・最大 2 秒）を待つ。/hormuz/ は地図の zoomend を出して印の大きさをそろえる
- diff：同じ名前の写真を1画素単位で比べ、差のある画素の数を出す。差がなければ終了コード 0
- sheet：前と後を左右に並べた HTML を作る（写真は相対パスで参照する。見た目が変わる PR で目で確かめる用）

Git Bash では /hormuz/ のような引数が書き換えられるので、MSYS_NO_PATHCONV=1 を付ける。
そのときは保存先も C:/Users/... の形で渡す（/c/Users/... のままだと C ドライブ直下の c/Users/... に書かれる）。
"""
import argparse, html, json, mimetypes, os, pathlib, sys
from urllib.parse import urlparse

PAGES = ['/', '/hormuz/', '/hormuz/articles/',
         '/hormuz/articles/mine-clearance/', '/hormuz/articles/oil-diversification-africa-brazil/',
         '/hormuz/articles/oil-stockpile-monthly-trend/', '/hormuz/articles/route-c-alaska-oil/',
         '/hormuz/articles/saudi-pipeline-attack/',
         '/archive/', '/infographic/', '/glossary/',
         '/about/', '/contact/', '/corrections/', '/disclaimer/', '/editorial/', '/privacy/', '/terms/',
         '/404.html']
WIDTHS = [1280, 390]
HOST = 'chokepointlab.com'

# Date だけを --now から進める（タイマーやアニメーションの時間は本物のまま）
CLOCK = """
(() => {
  const base = %d, start = Date.now(), R = Date;
  function D(...a) { return a.length ? new R(...a) : new R(base + (R.now() - start)); }
  D.prototype = R.prototype; D.now = () => base + (R.now() - start);
  D.UTC = R.UTC; D.parse = R.parse;
  window.Date = D;
})();
"""


def name_of(page, width):
    s = page.strip('/').replace('/', '_') or 'hub'
    return f'{s}@{width}.png'


def shoot(docs, out, pages, now_ms):
    from playwright.sync_api import sync_playwright
    docs = pathlib.Path(docs)
    out = pathlib.Path(out)
    out.mkdir(parents=True, exist_ok=True)

    def route(r):
        u = urlparse(r.request.url)
        if u.hostname in ('localhost', HOST):
            fp = docs / u.path.lstrip('/')
            if u.path.endswith('/'):
                fp = fp / 'index.html'
            if fp.is_file():
                ct = mimetypes.guess_type(fp.name)[0] or 'application/octet-stream'
                if fp.suffix == '.woff2':
                    ct = 'font/woff2'
                return r.fulfill(body=fp.read_bytes(), content_type=ct)
            return r.fulfill(status=404, body='')
        return r.abort()

    with sync_playwright() as p:
        br = p.chromium.launch(channel='chrome')
        for page in pages:
            for w in WIDTHS:
                ctx = br.new_context(viewport={'width': w, 'height': 900}, device_scale_factor=1,
                                     locale='ja-JP', timezone_id='Asia/Tokyo')
                ctx.add_init_script(CLOCK % now_ms)
                ctx.route('**/*', route)
                pg = ctx.new_page()
                errors = []
                pg.on('pageerror', lambda e: errors.append(str(e)))
                pg.on('console', lambda m: m.type == 'error' and errors.append(m.text))
                pg.goto('http://localhost' + page, wait_until='networkidle')
                pg.evaluate('async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}scrollTo(0,0);}')
                pg.evaluate('document.fonts.ready.then(()=>true)')
                pg.wait_for_timeout(2500)
                pg.evaluate("typeof map!=='undefined' && map.fire && map.fire('zoomend')")
                pg.wait_for_timeout(300)
                pg.evaluate('document.fonts.ready.then(()=>true)')
                fn = name_of(page, w)
                pg.screenshot(path=str(out / fn), full_page=True, animations='disabled', caret='hide')
                # 外への通信を止めているので、その失敗は数えない
                errors = [e for e in errors if 'net::ERR_FAILED' not in e]
                print(json.dumps({'shot': fn, 'errors': errors}, ensure_ascii=False), flush=True)
                ctx.close()
        br.close()


def diff(a, b):
    from PIL import Image, ImageChops
    a, b = pathlib.Path(a), pathlib.Path(b)
    names = sorted({p.name for p in a.glob('*.png')} | {p.name for p in b.glob('*.png')})
    bad = 0
    for n in names:
        if not (a / n).exists() or not (b / n).exists():
            print(f'{n}\t片方だけ'); bad += 1; continue
        ia, ib = Image.open(a / n).convert('RGB'), Image.open(b / n).convert('RGB')
        if ia.size != ib.size:
            print(f'{n}\t大きさが違う {ia.size} → {ib.size}'); bad += 1; continue
        d = ImageChops.difference(ia, ib).convert('L').point(lambda v: 255 if v else 0)
        cnt = d.histogram()[255]
        print(f'{n}\t{cnt}')
        bad += cnt > 0
    print(f'差のある写真：{bad} / {len(names)}')
    return bad


def sheet(a, b, out, pages):
    a, b, out = pathlib.Path(a), pathlib.Path(b), pathlib.Path(out)
    rel = lambda p: os.path.relpath(p, out.parent).replace(os.sep, '/')
    rows = []
    for page in pages:
        for w in WIDTHS:
            n = name_of(page, w)
            if not (a / n).exists() and not (b / n).exists():
                continue
            rows.append(f'<h2>{html.escape(page)}・幅 {w}</h2><div class="pair">'
                        f'<figure><figcaption>前</figcaption><img loading="lazy" src="{rel(a / n)}"></figure>'
                        f'<figure><figcaption>後</figcaption><img loading="lazy" src="{rel(b / n)}"></figure></div>')
    out.write_text('<!doctype html><meta charset="utf-8"><title>前と後</title>'
                   '<style>body{font-family:sans-serif;margin:16px;background:#777}h2{font-size:15px;margin:28px 0 8px}'
                   '.pair{display:grid;grid-template-columns:1fr 1fr;gap:12px;align-items:start}'
                   'figure{margin:0}figcaption{font-size:13px;margin-bottom:4px}img{width:100%;border:1px solid #333}</style>'
                   + ''.join(rows), encoding='utf-8')
    print(out)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('shoot'); s.add_argument('docs'); s.add_argument('out'); s.add_argument('pages', nargs='*')
    s.add_argument('--now', default='2026-10-20T12:00:00+09:00')
    d = sub.add_parser('diff'); d.add_argument('a'); d.add_argument('b')
    h = sub.add_parser('sheet'); h.add_argument('a'); h.add_argument('b'); h.add_argument('out'); h.add_argument('pages', nargs='*')
    o = ap.parse_args()
    if o.cmd == 'shoot':
        from datetime import datetime
        shoot(o.docs, o.out, o.pages or PAGES, int(datetime.fromisoformat(o.now).timestamp() * 1000))
    elif o.cmd == 'diff':
        sys.exit(1 if diff(o.a, o.b) else 0)
    else:
        sheet(o.a, o.b, o.out, o.pages or PAGES)


if __name__ == '__main__':
    main()
