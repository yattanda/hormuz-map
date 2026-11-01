"""delivery_check.py が貯めた結果（delivery-*.json）から、証拠の1ページ（report.html）を作る（2026-11-01 追加）。

「このドメインだけ遅い・ほかの GitHub Pages のサイトや同じ中身の raw は速い」を、1枚で見せるためのページ。
GitHub Support への問い合わせや、プロキシを入れる・切るの判断に添える。外部のファイルは読まない（1ファイルで開ける）。

使い方：
  python tools/delivery_report.py <フォルダ>            # <フォルダ>/report.html を作る
  python tools/delivery_check.py --history <フォルダ>    # 測って貯め、そのまま作り直す（ふつうはこちら）

手で測った値（curl など・delivery_check.py より前）も、同じ形の JSON に "source" を書いて置けば並ぶ。
"""
from __future__ import annotations

import json
import statistics
import sys
from datetime import datetime
from pathlib import Path


def load(d: Path) -> list[dict]:
    runs = []
    for p in sorted(d.glob("delivery-*.json")):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        r["_file"] = p.name
        runs.append(r)
    runs.sort(key=lambda r: r.get("at_iso", ""))
    return runs


def median_speed(rows: list[dict]) -> int | None:
    """大きいファイル（10KB 以上か打ち切り）の速さの中央値。
    取れなかった行（接続のエラー・200 以外の応答）は大きさに関わらず 0 として数える（503 の本文を速さに数えない）"""
    failed = lambda r: bool(r.get("error")) or r.get("status") != 200
    v = [0 if failed(r) else r.get("speed", 0) for r in rows
         if failed(r) or r.get("bytes", 0) >= 10_000 or not r.get("complete")]
    return int(statistics.median(v)) if v else None


def summarize(run: dict) -> dict:
    return {"at": run.get("at_iso", ""), "label": run.get("at", ""), "source": run.get("source", "delivery_check.py"),
            "mode": run.get("mode", ""), "verdict": run.get("verdict", ""),
            "current": median_speed(run.get("current", [])),
            "direct": median_speed(run.get("direct", [])),
            "control": median_speed(run.get("control", []))}


TEMPLATE = r"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>配信の確認</title>
<style>
:root {
  color-scheme: light;
  --surface-0: #f3f2ee; --surface-1: #fcfcfb; --rule: #dcdad3;
  --text-primary: #0b0b0b; --text-secondary: #52514e; --text-muted: #6f6e69;
  --series-1: #2a78d6; --series-2: #eb6834; --series-3: #1baf7a;
  --good: #0ca30c; --warning: #fab219; --critical: #d03b3b;
  --on-status: #0b0b0b;
}
@media (prefers-color-scheme: dark) {
  :root:where(:not([data-theme="light"])) {
    color-scheme: dark;
    --surface-0: #121211; --surface-1: #1a1a19; --rule: #33332f;
    --text-primary: #f0efec; --text-secondary: #c3c2b7; --text-muted: #a3a298;
    --series-1: #3987e5; --series-2: #d95926; --series-3: #199e70;
  }
}
:root[data-theme="dark"] {
  color-scheme: dark;
  --surface-0: #121211; --surface-1: #1a1a19; --rule: #33332f;
  --text-primary: #f0efec; --text-secondary: #c3c2b7; --text-muted: #a3a298;
  --series-1: #3987e5; --series-2: #d95926; --series-3: #199e70;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--surface-0); color: var(--text-primary);
  font-family: 'BIZ UDPGothic', 'Hiragino Sans', 'Yu Gothic UI', system-ui, sans-serif; font-size: 15px; line-height: 1.6; }
main { max-width: 1080px; margin: 0 auto; padding: 20px 16px 48px; display: flex; flex-direction: column; gap: 16px; }
h1 { font-size: 1.35rem; margin: 0; line-height: 1.4; }
h2 { font-size: 1.05rem; margin: 0 0 4px; }
.sub { color: var(--text-secondary); font-size: .85rem; margin: 2px 0 0; }
.card { background: var(--surface-1); border: 1px solid var(--rule); border-radius: 8px; padding: 16px; min-width: 0; }
.tiles { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.tile .k { color: var(--text-secondary); font-size: .8rem; }
.tile .v { font-size: 1.9rem; font-weight: 700; font-variant-numeric: tabular-nums; line-height: 1.2; }
.tile .u { font-size: .85rem; font-weight: 400; color: var(--text-secondary); margin-left: 4px; }
.tile .n { color: var(--text-muted); font-size: .78rem; }
.verdict { display: inline-flex; align-items: center; gap: 6px; padding: 2px 10px; border-radius: 4px; font-weight: 700;
  color: var(--on-status); }
.verdict--good { background: var(--good); } .verdict--bad { background: var(--critical); color: #fff; }
.verdict--hold { background: var(--warning); }
.lead { font-size: 1rem; margin: 0; }
.lead strong { font-size: 1.15rem; }
.legend { display: flex; flex-wrap: wrap; gap: 6px 16px; font-size: .82rem; color: var(--text-secondary); margin: 6px 0 4px; }
.legend i { display: inline-block; width: 12px; height: 12px; border-radius: 3px; margin-right: 6px; vertical-align: -1px; }
svg { display: block; width: 100%; height: auto; overflow: visible; }
.chart { overflow-x: auto; }
.chart svg { min-width: 620px; }   /* スマホでは図だけ横に動かして見る（縮めると文字が読めない） */
svg text { fill: var(--text-secondary); font-size: 12px; font-family: inherit; }
svg .val { fill: var(--text-primary); font-weight: 700; }
svg .grid { stroke: var(--rule); stroke-width: 1; }
svg .hit { fill: transparent; cursor: default; }
.note { color: var(--text-muted); font-size: .8rem; margin: 6px 0 0; }
.tip { position: fixed; pointer-events: none; z-index: 10; background: var(--surface-1); color: var(--text-primary);
  border: 1px solid var(--rule); border-radius: 6px; padding: 6px 9px; font-size: .8rem; line-height: 1.5;
  box-shadow: 0 2px 8px rgba(0,0,0,.18); max-width: 300px; display: none; }
table { border-collapse: collapse; width: 100%; font-size: .8rem; font-variant-numeric: tabular-nums; }
th, td { text-align: left; padding: 5px 8px; border-bottom: 1px solid var(--rule); vertical-align: top; }
th { color: var(--text-secondary); font-weight: 700; }
td.r, th.r { text-align: right; white-space: nowrap; }
.lead strong { white-space: nowrap; }
.scroll { overflow-x: auto; }
details summary { cursor: pointer; font-weight: 700; }
code { font-size: .85em; }
@media (max-width: 640px) {
  .tiles { grid-template-columns: 1fr; }
  .tile .v { font-size: 1.6rem; }
}
</style>
</head>
<body>
<main>
<header>
  <h1>chokepointlab.com の配信の確認</h1>
  <p class="sub" id="meta"></p>
</header>

<section class="card">
  <p class="lead" id="lead"></p>
  <p class="note" id="reasons"></p>
</section>

<section class="tiles" id="tiles"></section>

<section class="card">
  <h2>同じ大きさのページを取るのにかかった時間（最新の回）</h2>
  <p class="sub">/hormuz/（約458KB）と、同じくらいの大きさの比べる相手。短いほど速い。30秒で打ち切り</p>
  <div class="legend" id="legend-bars"></div>
  <div class="chart" id="bars"></div>
  <p class="note">「直接」は GitHub Pages の IP へ直接つないだもの（プロキシ無しのときに読者が通る道と同じ）。比べる相手は同じ GitHub の配信の、別のサイトと同じ中身の raw。</p>
</section>

<section class="card">
  <h2>速さの推移（1回ごとの中央値・対数の目盛り）</h2>
  <p class="sub">大きいファイル（10KB 以上）の速さの中央値。取れなかったものは 0 として数える。上ほど速い</p>
  <div class="legend" id="legend-line"></div>
  <div class="chart" id="line"></div>
  <p class="note" id="line-note"></p>
</section>

<section class="card">
  <details open>
    <summary>最新の回の内訳</summary>
    <div class="scroll"><table id="latest"></table></div>
  </details>
</section>

<section class="card">
  <details>
    <summary>測った回の一覧</summary>
    <div class="scroll"><table id="history"></table></div>
  </details>
</section>

<section class="card">
  <h2>測り方</h2>
  <p class="note" style="font-size:.85rem">__METHOD__</p>
</section>
</main>
<div class="tip" id="tip" role="tooltip"></div>
<script id="data" type="application/json">__DATA__</script>
<script>
(function () {
  const D = JSON.parse(document.getElementById('data').textContent);
  const runs = D.runs, sums = D.summaries, latest = runs[runs.length - 1];
  const $ = id => document.getElementById(id);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const kb = b => b == null ? '—' : b >= 1e6 ? (b / 1e6).toFixed(2) + ' MB' : (b / 1e3).toFixed(b >= 1e5 ? 0 : 1) + ' KB';
  const rate = b => b == null ? '—' : b >= 1e6 ? (b / 1e6).toFixed(2) + ' MB/秒' : (b / 1e3).toFixed(b >= 1e4 ? 0 : 1) + ' KB/秒';
  const tip = $('tip');
  function showTip(e, html) { tip.innerHTML = html; tip.style.display = 'block';
    const x = Math.min(e.clientX + 14, innerWidth - tip.offsetWidth - 8), y = Math.min(e.clientY + 14, innerHeight - tip.offsetHeight - 8);
    tip.style.left = x + 'px'; tip.style.top = y + 'px'; }
  function hideTip() { tip.style.display = 'none'; }
  function bindTip(el, html) { el.addEventListener('pointermove', e => showTip(e, html)); el.addEventListener('pointerleave', hideTip); }

  // 見出しの下・結論
  $('meta').textContent = '作成 ' + D.generated + '／測った回 ' + runs.length + '（' + (sums[0] ? sums[0].label : '') + ' 〜 ' + (latest ? latest.at : '') + '）';
  const last = sums[sums.length - 1];
  const v = latest.verdict || '';
  const cls = v.startsWith('戻してよい') ? 'good' : v.startsWith('保留') ? 'hold' : 'bad';
  const ratio = last.control && last.direct != null ? Math.round(last.control / Math.max(last.direct, 1)) : null;
  const modeShort = m => String(m || '').startsWith('プロキシ無し') ? 'プロキシ無し' : String(m || '').startsWith('プロキシ有り') ? 'プロキシ有り' : (m || '');
  $('lead').innerHTML = '最新（' + esc(latest.at) + '・' + esc(modeShort(latest.mode)) + '）：GitHub Pages から直接取ると <strong>' + rate(last.direct) +
    '</strong>、比べる相手は <strong>' + rate(last.control) + '</strong>' + (ratio && ratio > 1 ? '（このドメインは<strong>約' + ratio + '分の1</strong>の速さ）' : '') +
    '。判定 <span class="verdict verdict--' + cls + '">' + (cls === 'good' ? '✓ ' : cls === 'hold' ? '… ' : '✕ ') + esc(v || '—') + '</span>';
  $('reasons').textContent = (latest.reasons || []).join('／');

  const tiles = [
    ['このドメイン・今の経路', last.current, '読者が実際に通る道'],
    ['このドメイン・直接 GitHub Pages', last.direct, 'プロキシ無しのときの姿'],
    ['比べる相手（別の Pages・raw）', last.control, 'こちらの回線の速さの目安']];
  $('tiles').innerHTML = tiles.map(t => '<div class="card tile"><div class="k">' + t[0] + '</div><div class="v">' +
    (t[1] == null ? '—' : (t[1] >= 1e6 ? (t[1] / 1e6).toFixed(2) : (t[1] / 1e3).toFixed(t[1] >= 1e4 ? 0 : 1))) +
    '<span class="u">' + (t[1] != null && t[1] >= 1e6 ? 'MB/秒' : 'KB/秒') + '</span></div><div class="n">' + t[2] + '（中央値）</div></div>').join('');

  // 凡例（色は経路の種類。色だけに頼らず、棒の左に名前を書く）
  const KINDS = [['current', '今の経路', 'var(--series-1)'], ['direct', '直接 GitHub Pages', 'var(--series-2)'], ['control', '比べる相手', 'var(--series-3)']];
  const legend = KINDS.map(k => '<span><i style="background:' + k[2] + '"></i>' + k[1] + '</span>').join('');
  $('legend-bars').innerHTML = legend; $('legend-line').innerHTML = legend;

  // 1. 横棒：/hormuz/ と比べる相手の時間
  const rows = [];
  (latest.current || []).filter(r => r.path === '/hormuz/').forEach(r => rows.push(['current', '今の経路 /hormuz/', r]));
  (latest.direct || []).filter(r => r.path === '/hormuz/').forEach(r => rows.push(['direct', '直接 ' + (r.ip || ''), r]));
  (latest.control || []).forEach(r => rows.push(['control', r.host === 'raw.githubusercontent.com' ? 'raw（同じ HTML）' : '別の Pages のサイト', r]));
  const W = 760, LBL = 190, ROW = 30, TOP = 8, AX = 22, H = TOP + rows.length * ROW + AX;
  const maxT = Math.max(30, ...rows.map(r => r[2].secs || 0));
  const xs = t => LBL + (W - LBL - 130) * Math.min(t, maxT) / maxT;
  let s = '<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="経路ごとの取得時間の横棒グラフ">';
  for (let t = 0; t <= maxT; t += 10) s += '<line class="grid" x1="' + xs(t) + '" x2="' + xs(t) + '" y1="' + TOP + '" y2="' + (H - AX) + '"/>' +
    '<text x="' + xs(t) + '" y="' + (H - 6) + '" text-anchor="middle">' + t + '秒</text>';
  rows.forEach((row, i) => {
    const [kind, label, r] = row, y = TOP + i * ROW, col = KINDS.find(k => k[0] === kind)[2];
    const t = r.error ? maxT : (r.secs || 0), x1 = Math.max(xs(t), LBL + 3);
    const done = !r.error && r.complete;
    const valTxt = r.error ? '取れず（' + esc(r.error).slice(0, 18) + '）' : (r.secs.toFixed(r.secs < 10 ? 2 : 1) + '秒' + (done ? '' : '・打ち切り'));
    s += '<text x="' + (LBL - 8) + '" y="' + (y + 19) + '" text-anchor="end">' + esc(label) + '</text>' +
      '<path d="M' + LBL + ' ' + (y + 6) + ' H' + (x1 - 4) + ' a4 4 0 0 1 4 4 V' + (y + 20) + ' a4 4 0 0 1 -4 4 H' + LBL + ' Z" fill="' + col + '"' + (done ? '' : ' fill-opacity=".45"') + '/>' +
      '<text class="val" x="' + (x1 + 6) + '" y="' + (y + 19) + '">' + valTxt + '</text>' +
      '<rect class="hit" data-i="' + i + '" x="0" y="' + y + '" width="' + W + '" height="' + ROW + '"/>';
  });
  s += '</svg>';
  $('bars').innerHTML = s;
  $('bars').querySelectorAll('.hit').forEach(el => { const [, label, r] = rows[+el.dataset.i];
    bindTip(el, '<b>' + esc(label) + '</b><br>' + (r.error ? esc(r.error) : kb(r.bytes) + ' を ' + r.secs + '秒（' + rate(r.speed) + '）' + (r.complete ? '' : '<br>30秒で打ち切り')) +
      (r.headers && r.headers.server ? '<br>応答：' + esc(r.headers.server) + ' ' + esc(r.headers['cf-cache-status'] || r.headers['x-cache'] || '') : '')); });

  // 2. 推移：対数の目盛り（1KB/秒〜10MB/秒）
  const LW = 760, LH = 260, PL = 92, PR = 16, PT = 10, PB = 34;
  const lo = 3, hi = 7;   // 10^3〜10^7 B/秒
  const ly = b => { const v = Math.log10(Math.max(b || 1000, 1000)); return PT + (LH - PT - PB) * (1 - (v - lo) / (hi - lo)); };
  const tms = sums.map(x => Date.parse(x.at)), t0 = Math.min(...tms), t1 = Math.max(...tms);
  const lx = t => t1 === t0 ? (PL + LW - PR) / 2 : PL + (LW - PL - PR) * (t - t0) / (t1 - t0);
  let g = '<svg viewBox="0 0 ' + LW + ' ' + LH + '" role="img" aria-label="速さの推移の折れ線グラフ">';
  for (let e = lo; e <= hi; e++) g += '<line class="grid" x1="' + PL + '" x2="' + (LW - PR) + '" y1="' + ly(10 ** e) + '" y2="' + ly(10 ** e) + '"/>' +
    '<text x="' + (PL - 8) + '" y="' + (ly(10 ** e) + 4) + '" text-anchor="end">' + rate(10 ** e).replace('.0 ', ' ') + '</text>';
  const fmtT = t => { const d = new Date(t); return (d.getMonth() + 1) + '/' + d.getDate() + ' ' + String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0'); };
  // 時刻の目盛り：近すぎる（90px 未満）ものは飛ばす。最後の回は必ず出す
  let lastX = -1e9;
  tms.forEach((t, i) => { const x = lx(t);
    if (x - lastX < 90 && i !== tms.length - 1) return;
    if (i === tms.length - 1 && x - lastX < 90) g = g.replace(/<text data-tick="last"[^>]*>[^<]*<\/text>$/, '');
    g += '<text data-tick="last" x="' + x + '" y="' + (LH - 10) + '" text-anchor="' + (i === 0 ? 'start' : i === tms.length - 1 ? 'end' : 'middle') + '">' + fmtT(t) + '</text>';
    lastX = x; });
  // 線の名前は右端の点の上に。重なるときは縦にずらす
  const ends = [];
  KINDS.forEach(k => {
    const pts = sums.map((x, i) => [lx(tms[i]), x[k[0]]]).filter(p => p[1] != null);
    if (pts.length > 1) g += '<polyline fill="none" stroke="' + k[2] + '" stroke-width="2" points="' + pts.map(p => p[0] + ',' + ly(p[1])).join(' ') + '"/>';
    pts.forEach(p => g += '<circle cx="' + p[0] + '" cy="' + ly(p[1]) + '" r="4.5" fill="' + k[2] + '" stroke="var(--surface-1)" stroke-width="2"/>');
    const lp = pts[pts.length - 1];
    if (lp) ends.push([lp[0], ly(lp[1]) - 8, k[1]]);
  });
  ends.sort((a, b) => a[1] - b[1]);
  ends.forEach((e, i) => { if (i && e[1] - ends[i - 1][1] < 16) e[1] = ends[i - 1][1] + 16; });
  ends.forEach(e => g += '<text class="val" x="' + Math.min(e[0] - 8, LW - PR - 4) + '" y="' + e[1] + '" text-anchor="end">' + e[2] + '</text>');
  sums.forEach((x, i) => { const xx = lx(tms[i]);
    g += '<rect class="hit" data-i="' + i + '" x="' + (xx - 14) + '" y="' + PT + '" width="28" height="' + (LH - PT - PB) + '"/>'; });
  g += '</svg>';
  $('line').innerHTML = g;
  $('line').querySelectorAll('.hit').forEach(el => { const x = sums[+el.dataset.i];
    bindTip(el, '<b>' + esc(x.label) + '</b>' + (x.source !== 'delivery_check.py' ? '（' + esc(x.source) + '）' : '') +
      '<br>今の経路 ' + rate(x.current) + '<br>直接 ' + rate(x.direct) + '<br>比べる相手 ' + rate(x.control) + (x.verdict ? '<br>判定 ' + esc(x.verdict) : '')); });
  const manual = sums.filter(x => x.source !== 'delivery_check.py').length;
  $('line-note').textContent = manual ? '手で測った値（curl・delivery_check.py より前）を ' + manual + '回含む。プロキシ無しのあいだは「今の経路」と「直接」はほぼ同じ道。' :
    'プロキシ無しのあいだは「今の経路」と「直接」はほぼ同じ道。';

  // 表
  const head = '<tr><th>経路</th><th>ファイル</th><th class="r">取れた量</th><th class="r">時間</th><th class="r">速さ</th><th>評価</th><th>応答</th></tr>';
  const grade = r => r.error || r.status !== 200 || !r.complete ? '不良' : r.bytes < 10000 ? (r.secs < 2 ? '良好' : r.secs < 5 ? '注意' : '不良') : r.speed >= 200000 ? '良好' : r.speed >= 50000 ? '注意' : '不良';
  const tr = (k, r) => '<tr><td>' + k + (r.ip ? ' ' + esc(r.ip) : '') + '</td><td>' + esc((r.host !== 'chokepointlab.com' ? r.host : '') + r.path) + '</td><td class="r">' + kb(r.bytes) +
    (r.complete ? '' : '（打ち切り）') + '</td><td class="r">' + (r.secs == null ? '—' : r.secs + '秒') + '</td><td class="r">' + rate(r.speed) + '</td><td>' + grade(r) + '</td><td>' +
    esc(r.error || ((r.headers && r.headers.server || '') + ' ' + (r.headers && (r.headers['cf-cache-status'] || r.headers['x-cache']) || ''))) + '</td></tr>';
  $('latest').innerHTML = head + (latest.current || []).map(r => tr('今の経路', r)).join('') + (latest.direct || []).map(r => tr('直接', r)).join('') +
    (latest.control || []).map(r => tr('比べる相手', r)).join('');
  $('history').innerHTML = '<tr><th>日時</th><th>測り方</th><th>向き先</th><th class="r">今の経路</th><th class="r">直接</th><th class="r">比べる相手</th><th>判定</th></tr>' +
    sums.slice().reverse().map(x => '<tr><td>' + esc(x.label) + '</td><td>' + esc(x.source) + '</td><td>' + esc(x.mode) + '</td><td class="r">' + rate(x.current) +
      '</td><td class="r">' + rate(x.direct) + '</td><td class="r">' + rate(x.control) + '</td><td>' + esc(x.verdict || '—') + '</td></tr>').join('');
})();
</script>
</body>
</html>
"""

METHOD = (
    "測る道具は <code>python tools/delivery_check.py --history &lt;このフォルダ&gt;</code>（hormuz-map）。"
    "1ファイルずつ圧縮なしで本文を全部取り、時間と量から速さを出す（30秒で打ち切り）。"
    "「今の経路」はふつうに名前解決した chokepointlab.com、「直接」は GitHub Pages の IP（185.199.108〜111.153）へ"
    "名前を chokepointlab.com としてつないだもの、「比べる相手」は同じ中身の raw.githubusercontent.com と、"
    "別の GitHub Pages のサイト（google.github.io の約430KB のページ）。"
    "評価は 10KB 以上で 200KB/秒以上を良好・50KB/秒未満か打ち切りを不良。"
    "プロキシ無しに戻してよいかの判定は、直接の経路がすべて良好・GitHub の証明書の残りが14日以上・比べる相手も良好のとき「戻してよい」。"
)


def build(d: Path) -> Path:
    d = Path(d)
    runs = load(d)
    if not runs:
        raise SystemExit(f"{d} に delivery-*.json がありません")
    data = {"generated": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M"),
            "runs": runs, "summaries": [summarize(r) for r in runs]}
    text = TEMPLATE.replace("__METHOD__", METHOD).replace(
        "__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    out = d / "report.html"
    out.write_text(text, encoding="utf-8")
    return out


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")   # Windows の既定（cp932）で文字化けさせない
    if len(sys.argv) != 2:
        sys.exit("使い方：python tools/delivery_report.py <delivery-*.json のあるフォルダ>")
    print(build(Path(sys.argv[1])))
