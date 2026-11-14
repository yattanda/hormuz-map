#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""30秒カラム「海峡の今」の通航の札を、IMF PortWatch の7日平均から作る。

札の出典は 2026-11-14 に報道（Kpler・MarineTraffic などの週の集計）から PortWatch に替えた（運営者）。
ダッシュボードのカード1と同じ値（hormuz-data- の data/portwatch-hormuz.json の window）を出すため、
ページの上と下で通航数が食い違わない。PortWatch は AIS で捕捉した通航だけを数えるので下限であり、
報道の数字より小さい（11/14 時点で 3.9隻/日、報道の週141回＝約20回/日）。報道の数字は全文に出典つきで書く。

使い方：
    python tools/glance_transit.py           # 札の HTML を表示するだけ
    python tools/glance_transit.py --write   # docs/hormuz/index.html の通航の札（3枚目）を置き換える

読むのは公開 URL → ローカルの ../hormuz-data- の順（ページが読むのは公開 URL。ローカルは pull 前だと古い）。
終了コード：0＝札を作れた／2＝データを読めなかった（札は前の値のまま）
"""
import argparse
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "docs" / "hormuz" / "index.html"
PORTWATCH_URL = "https://yattanda.github.io/hormuz-data-/data/portwatch-hormuz.json"
PORTWATCH_LOCAL = ROOT.parent / "hormuz-data-" / "data" / "portwatch-hormuz.json"

LABEL = "通航（AIS）"
UNIT = "隻/日"
SOURCE = "PortWatch"

PAT_FIGS = re.compile(r'(<dl class="glance-figs"[^>]*>)(.*?)(</dl>)', re.S)
PAT_FIG = re.compile(r'<div class="glance-fig">.*?</div>', re.S)


def load_portwatch() -> tuple[dict | None, str]:
    """(内容, 取得元または失敗理由)。どちらも失敗したら内容は None。"""
    reasons = []
    req = urllib.request.Request(PORTWATCH_URL, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return json.loads(res.read().decode("utf-8")), "公開 URL"
    except Exception as e:  # ネットワーク到達不能・HTTP エラー・タイムアウト・JSON 破損など
        reasons.append(f"公開 URL 取得失敗（{type(e).__name__}）")
    try:
        return json.loads(PORTWATCH_LOCAL.read_text(encoding="utf-8")), "ローカル ../hormuz-data-"
    except (OSError, ValueError) as e:
        reasons.append(f"ローカル読み込み失敗（{type(e).__name__}）")
    return None, "・".join(reasons)


def expected(pw: dict) -> tuple[str, str, date]:
    """(数字, 補足, 期間の終わりの日)。window は 7日の平均（隻/日）と期間 'YYYY-MM-DD/YYYY-MM-DD'。"""
    w = pw["window"]
    start, end = (date.fromisoformat(x) for x in w["period"].split("/"))
    num = f"{float(w['total']):.1f}"
    sub = f"{start.month}/{start.day}〜{end.month}/{end.day}・{SOURCE}"
    return num, sub, end


def fig_html(num: str, sub: str) -> str:
    return (f'<div class="glance-fig"><dt class="glance-fig-label">{LABEL}</dt>'
            f'<dd class="glance-fig-val"><span class="glance-fig-num">{num}</span>'
            f'<span class="glance-fig-unit">{UNIT}</span></dd>'
            f'<dd class="glance-fig-sub">{sub}</dd></div>')


def replace_fig(html: str, new_fig: str) -> str:
    """数字の札の3枚目（通航）を置き換える。札が4枚でなければ ValueError。"""
    m = PAT_FIGS.search(html)
    if not m:
        raise ValueError('<dl class="glance-figs"> が見つかりません')
    figs = list(PAT_FIG.finditer(m.group(2)))
    if len(figs) != 4:
        raise ValueError(f"数字の札が {len(figs)}枚です（4枚の前提）")
    f = figs[2]
    body = m.group(2)[:f.start()] + new_fig + m.group(2)[f.end():]
    return html[:m.start(2)] + body + html[m.end(2):]


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--write", action="store_true", help="docs/hormuz/index.html の通航の札を置き換える")
    args = p.parse_args(argv)

    pw, src = load_portwatch()
    if pw is None:
        print(f"PortWatch のデータを読めませんでした: {src}。札は前の値のままにする", file=sys.stderr)
        return 2
    num, sub, end = expected(pw)
    new_fig = fig_html(num, sub)
    print(f"PortWatch（{src}）: {num} {UNIT}・{sub}（最新日 {pw.get('latest_date')}）")
    print(new_fig)
    if args.write:
        # 改行コードをそのまま保つ（newline="" で読み書きする）
        with open(HTML, encoding="utf-8", newline="") as f:
            html = f.read()
        out = replace_fig(html, new_fig)
        if out == html:
            print("変更なし（札はすでにこの値）")
        else:
            with open(HTML, "w", encoding="utf-8", newline="") as f:
                f.write(out)
            print(f"{HTML.relative_to(ROOT)} の通航の札を書き換えました")
    return 0


if __name__ == "__main__":
    sys.exit(main())
