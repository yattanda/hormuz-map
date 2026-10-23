#!/usr/bin/env python3
"""
validate_daily.py — 日次更新の機械検証

docs/ 配下の更新結果を読み取り専用で検査する。ファイルは一切変更しない。

使い方:
    python tools/validate_daily.py                 # 基準日は news_data.json の updated
    python tools/validate_daily.py --date 2026-09-12
    python tools/validate_daily.py --check-urls    # latest の URL 死活も確認（ネットワーク必要）

終了コード:
    0 … エラーなし（警告のみは 0）
    1 … エラーあり

設計方針:
    - 過去データ（osint 85件・archive 259件）は旧スキーマが混在しているため、
      スキーマ検査は「当日更新される範囲」に限定する。過去分を責めない
    - 判定できない状態は黙って通さず、必ず NG か WARN として出す
    - ファイル間の整合だけでなく、基準日そのものを実測日と照合する。
      揃ったまま間違った日付で書かれていると内部整合では気づけないため
    - 全ルート現況サマリーは見出しの日付更新だけで本文が古いまま、という事故が
      2026-09-15 に実際に発生した。見出しの日付一致（NG）とは別に、各行の「最新」
      （p.route-latest の <time datetime>。② PR3 以降の型）の鮮度を WARN として見る。
      型で書かれていない行は、本文中の M/D 日付表記で推定する（本文の内容自体は機械判定できないため）
    - hormuz-data- の経緯（data/context.json の timeline）は手動追記で、日次手順に
      入っていなかったため 9/3 で止まり、ダッシュボードに ⚠ が出た（2026-09-19 に発覚）。
      最新日が実測の今日から 5日を超えたら WARN を出す（別リポジトリのため NG にはしない）。
      ローカルの ../hormuz-data- を優先し、無ければ公開 URL を取得する。どちらも失敗したら WARN
    - /hormuz/ には石油備蓄日数が3か所（地図の「日本の受入拠点」ポップアップ・精製所表の注記・主要指標の備蓄カード）ある。
      当初はどちらも特別解説コラムの月次更新の対象外で、8/17時点の値が 9/28 まで残っていた。
      クラウドの日次では速報 PDF を取れない（403 / 202）ため、2026-10-01 から毎月4日の PC タスクで更新する。
      「◯時点」の日付が実測の今日から 40日を超えたら WARN、値・日付が食い違ったら WARN を出す。
      2026-10-01 に主要指標の備蓄カード（8/17時点・204日分のまま残っていた）を3か所目として加えた。
      2026-10 の構造再編でハブ（docs/index.html）の主要な数字を4か所目として加えた
    - 日数の呼び名は 2026-10-02 に「封鎖N日目」から「危機N日目」へ改めた（数えているのは開戦 2/28 からの日数で、
      特定の封鎖の日数ではない）。当日に書いた update_log / archive_timeline の本文に「封鎖N日目」や
      主語のない「二重封鎖」があれば WARN を出す。過去分は書き換えない方針なので見ない
    - 本体ヘッダーの「危機N日目」は JS が計算するが、HTML に置いた静的な数字（JS が動かないときの予備）が
      217 のまま残っていた（2026-10-04 に発見）。日次更新が毎回書き換え、基準日から計算した日数と違えば WARN を出す
    - 特別解説コラムのピルの「NEW」「◯月更新」の札は、ピルの data-published / data-updated から決まる。
      記事ページ（datePublished / dateModified）と揃っていなければ WARN を出す
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

JST = timezone(timedelta(hours=9))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "docs" / "hormuz" / "index.html"   # ホルムズ海峡危機マップ本体（日次更新の対象）
HUB = ROOT / "docs" / "index.html"               # 媒体トップ（ハブ）。日次では触らない
NEWS = ROOT / "docs" / "data" / "news_data.json"
LOG = ROOT / "docs" / "data" / "update_log.json"
TIMELINE = ROOT / "docs" / "data" / "archive_timeline.json"
SITEMAP = ROOT / "docs" / "sitemap.xml"
UPCOMING = ROOT / "docs" / "data" / "upcoming.json"   # 今後の予定日（/hormuz/ の30秒カラムに JS が出す）
MILITARY = ROOT / "docs" / "data" / "military.json"   # 地図の艦隊・港・海域の説明（日次で毎回見直す）
MILITARY_REL = "docs/data/military.json"
MILITARY_DETAIL_MAX = 330                              # ポップアップに出す説明の長さの目安（字）

# latest の必須フィールド（daily-site-update スキル準拠）
LATEST_REQUIRED = ["title", "body", "sourceLabel", "date", "label", "url"]
# 旧スキーマのフィールド名。新規追加分に出てはいけない
LATEST_FORBIDDEN = ["headline", "summary", "source", "date_local", "date_jst", "tags"]

errors: list[str] = []
warns: list[str] = []
oks: list[str] = []


def ok(msg: str) -> None:
    oks.append(msg)


def ng(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warns.append(msg)


def load_json(path: Path):
    """JSON を読む。壊れていれば None を返す（呼び出し側で握る）。"""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        ng(f"{path.relative_to(ROOT)} が見つかりません")
    except json.JSONDecodeError as e:
        ng(f"{path.relative_to(ROOT)} が JSON として壊れています: {e}")
    return None


# ── 日付の抽出 ──────────────────────────────────────────────
# index.html 側。いずれも日次更新の対象
PAT_DATEMODIFIED = re.compile(r'"dateModified":\s*"(\d{4})-(\d{2})-(\d{2})T(\d{2}:\d{2})')
# 日付の頭の 📅・📊 は D3 PR 5b（2026-10-20）で外した。古い書き方でも拾えるよう、絵文字は有っても無くてもよい
PAT_HEADER = re.compile(r'badge-date">\s*(?:📅\s*)?(\d{4})年(\d{1,2})月(\d{1,2})日\s+(\d{1,2}:\d{2})\s*JST')
PAT_TICKER = re.compile(r'incident-badge">\s*(?:📅\s*)?(\d{1,2})/(\d{1,2})\s+(\d{1,2}:\d{2})\s*更新')
# ハブ（docs/index.html）の「危機マップの最終更新」の静的な予備。年を持たないので月日だけ照合する
PAT_HUB_UPDATED = re.compile(r'id="hub-updated">(\d{1,2})/(\d{1,2})\s+(\d{1,2}:\d{2})<')
# 本体ヘッダーの「危機N日目」の静的な予備（表示は JS が計算して上書きする）
PAT_CRISIS_DAY = re.compile(r'id="blockade-days">危機(\d+)日目')
CRISIS_START = date(2026, 2, 28)   # 開戦日＝1日目
# 今後の予定日の必須項目と、30秒カラム「次の焦点」の本文
UPCOMING_REQUIRED = ["kind", "title", "date", "source", "url", "added"]
PAT_GLANCE_NEXT = re.compile(r'glance-label--next">次の焦点</span>\s*<span class="glance-text">(.*?)</span>', re.S)
PAT_TICKER_COMMENT = re.compile(r'<!--\s*新ティッカー（(\d{4})年(\d{1,2})月(\d{1,2})日\s+(\d{1,2}:\d{2})\s*JST）\s*-->')
PAT_ROUTES = re.compile(
    r'sec-h2-sub">\s*(\d{4})年(\d{1,2})月(\d{1,2})日\s+(\d{1,2}:\d{2})\s*JST\s*(?:更新|再確認済)'
)
# news_data.json の updated
PAT_UPDATED = re.compile(r'(\d{4})年(\d{1,2})月(\d{1,2})日\s+(\d{1,2}:\d{2})\s*日本時間JST')

# 全ルート現況サマリーの表と、行ごとの本文中の日付表記（鮮度チェック用）
PAT_ROUTE_TABLE = re.compile(r'<table class="rtable">.*?</table>', re.S)
PAT_ROUTE_ROW = re.compile(r'<tr\b[^>]*>.*?</tr>', re.S)
PAT_ROUTE_ROW_ID = re.compile(r'id="jf-td-(\w+)"')
PAT_ROUTE_ROW_MD = re.compile(r'(\d{1,2})/(\d{1,2})')
PAT_ROUTE_LATEST = re.compile(r'<p class="route-latest">.*?<time datetime="(\d{4}-\d{2}-\d{2})', re.S)
STALE_ROUTE_DAYS = 10  # この日数より新しい日付表記が本文中に無ければ WARN

# sitemap.xml の lastmod（ホスト名は問わない。パスで特定する）
PAT_SITEMAP_HUB = re.compile(r'<loc>https?://[^/<]+/</loc>\s*<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>')
PAT_SITEMAP_TOP = re.compile(r'<loc>https?://[^/<]+/hormuz/</loc>\s*<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>')
PAT_SITEMAP_ARCHIVE = re.compile(r'<loc>https?://[^/<]+/archive/</loc>\s*<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>')

# hormuz-data- の経緯（Gemini に渡す確定した事実）。ローカルはリポジトリの親ディレクトリ基準
DATA_CONTEXT_LOCAL = ROOT.parent / "hormuz-data-" / "data" / "context.json"
DATA_CONTEXT_URL = "https://yattanda.github.io/hormuz-data-/data/context.json"
# ダッシュボードの ⚠（context.json の timeline_stale_after_days = 7）より手前で気づくための閾値
DATA_TIMELINE_WARN_DAYS = 5
# 日本向け調達フロー（ルート表の「日本向け」列）の元データ。hormuz-data- が毎日確認して、新しい月が出た日だけ書き換える
OIL_FLOW_LOCAL = ROOT.parent / "hormuz-data-" / "data" / "oil-flow.json"
OIL_FLOW_URL = "https://yattanda.github.io/hormuz-data-/data/oil-flow.json"
# 国別の数量が e-Stat に入るのは対象月の翌月下旬〜翌々月上旬。この日を過ぎても2か月前の月が出ていなければ遅れとみなす
OIL_FLOW_GRACE_DAY = 15

# /hormuz/ の石油備蓄日数3か所（毎月4日の PC タスクがコラムとあわせて更新する）
PAT_STOCKPILE_POPUP = re.compile(r'石油備蓄：</strong>(\d+)日分（[^）]*?(\d{1,2})/(\d{1,2})時点）')
PAT_STOCKPILE_NOTE = re.compile(r'合計は約(\d+)日分（(\d{4})年(\d{1,2})月(\d{1,2})日時点）')
# 主要指標の備蓄カード（時点の行 → 見出し → 合計の数字）。インライン style・クラスのどちらの書き方でも拾う
PAT_STOCKPILE_CARD = re.compile(
    r'>(\d{4})年(\d{1,2})月(\d{1,2})日時点（速報）</div>\s*<div[^>]*>(?:📊\s*)?日本の石油備蓄</div>\s*'
    r'<div class="stat-num[^"]*"[^>]*>(\d+)<span')
# ハブ（docs/index.html）の「主要な数字」。4か所目（2026-10 の構造再編で追加・設計書 s11-10-design.md D6-補）
PAT_STOCKPILE_HUB = re.compile(
    r'id="hub-stockpile">(\d+)<span[^>]*>日分</span></div>\s*'
    r'<div class="hub-stat-note">(\d{4})年(\d{1,2})月(\d{1,2})日時点（速報）')
STOCKPILE_WARN_DAYS = 40  # 月1回の更新で最長 約34日。PC が止まった数日分の余裕を足す

# <body> に残してよいインライン style（JS が style.display / style.width を状態として読み書きする要素の初期値）
STYLE_ALLOWED = {
    ('other-routes-body', 'display:none;'),      # その他の検討中ルート（onclick）
    ('bw-timeline-detail', 'display:none;'),     # toggleTimeline()
    ('bw-detail-body', 'display:none;'),         # toggleBwDetail()
    ('news-archive-container', 'display:none;'), # toggleArchive()
    ('log-collapse', 'display:none;'),           # 更新履歴の開閉
    ('log-toggle-bottom', 'display:none;'),      # 更新履歴の開閉
    ('refinery-modal', 'display:none;'),         # 製油所モーダル（none / flex）
    ('tanker-progress-bar', 'width:100%'),       # 足止め船の割合（JS が style.width を書く）
}

# 特別解説コラムのピル（「NEW」「◯月更新」の札の元になる日付）と記事ページの構造化データ
PAT_COLUMN_PILL = re.compile(
    r'<a href="articles/([\w-]+)/" class="jump-pill[^"]*"'
    r' data-published="(\d{4}-\d{2}-\d{2})" data-updated="(\d{4}-\d{2}-\d{2})"')
PAT_COLUMN_PILL_ANY = re.compile(r'<a href="articles/([\w-]+)/"[^>]*class="jump-pill')
PAT_ARTICLE_PUBLISHED = re.compile(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"')
PAT_ARTICLE_MODIFIED = re.compile(r'"dateModified":\s*"(\d{4}-\d{2}-\d{2})"')
# 記事ページの見える日付（「最終更新：」）と、コラムのカード・記事一覧の日付
# （「公開 YYYY/MM/DD」。公開のあとに加筆した記事は「公開 YYYY/MM/DD・更新 YYYY/MM/DD」）
PAT_ARTICLE_VISIBLE = re.compile(r'最終更新：<strong>(\d{4})/(\d{2})/(\d{2})</strong>')
PAT_COL_CARD_DATE = re.compile(r'<span class="col-card-date">([^<]*)</span>')
PAT_IDX_CARD = re.compile(
    r'<a class="article-index-card" href="/hormuz/articles/([\w-]+)/">(?:(?!</a>).)*?'
    r'<span class="idx-date">([^<]*)</span>', re.S)


def ymd(y, m, d) -> str:
    return f"{int(y):04d}-{int(m):02d}-{int(d):02d}"


def today_jst() -> str:
    """実測の今日（JST）。UTC 基準で計算するのでクラウド（UTC）でも PC でも同じ値になる。"""
    return datetime.now(JST).strftime("%Y-%m-%d")


def check_base_date(base: str) -> None:
    """基準日そのものが正しいかを実測日と照合する。

    ファイル間で日付が揃っていても、揃ったまま間違った日付で書かれていれば
    内部整合だけでは気づけない。日をまたぐ作業と日付の取り違えは実際に起きている
    （2026-08-31→09-01 の誤り、2026-09-13 の 9/14 との取り違え）。
    """
    today = today_jst()
    try:
        delta = (date.fromisoformat(base) - date.fromisoformat(today)).days
    except ValueError:
        ng(f"基準日 {base} を日付として解釈できません")
        return

    if delta > 0:
        ng(f"基準日 {base} が実測の今日（{today} JST）より {delta}日 未来です。"
           "未来日付のまま公開しないこと")
    elif delta == 0:
        ok(f"基準日が実測の今日と一致（{today} JST）")
    elif delta == -1:
        warn(f"基準日 {base} は実測の今日（{today} JST）の前日です。"
             "日付をまたいで作業した場合は正常。意図したものか確認すること")
    else:
        ng(f"基準日 {base} が実測の今日（{today} JST）より {-delta}日 前です。"
           "更新対象の日付を取り違えていないか確認すること")


def collect_dates(html: str, news: dict) -> dict[str, str | None]:
    """日次更新で揃っているべき日付を、箇所ごとに YYYY-MM-DD で集める。"""
    found: dict[str, str | None] = {}

    m = PAT_DATEMODIFIED.search(html)
    found["index.html / JSON-LD dateModified"] = ymd(*m.groups()[:3]) if m else None

    m = PAT_HEADER.search(html)
    found["index.html / ヘッダー日時"] = ymd(*m.groups()[:3]) if m else None

    m = PAT_ROUTES.search(html)
    found["index.html / 全ルート現況サマリー"] = ymd(*m.groups()[:3]) if m else None

    upd = news.get("updated", "") if news else ""
    m = PAT_UPDATED.search(upd)
    found["news_data.json / updated"] = ymd(*m.groups()[:3]) if m else None

    return found


def check_ticker(html: str, base: str) -> None:
    """速報バナーの「M/D HH:MM 更新」。年を持たないので月日だけ照合する。"""
    hits = PAT_TICKER.findall(html)
    if not hits:
        warn("index.html の速報インシデントの日付バッジ「M/D HH:MM 更新」を検出できませんでした（構造が変わった可能性）")
        return
    want = (int(base[5:7]), int(base[8:10]))
    bad = [f"{mm}/{dd}" for mm, dd, _ in hits if (int(mm), int(dd)) != want]
    if bad:
        ng(f"index.html の速報バナーの日付が基準日と違います: {', '.join(bad)}（基準 {want[0]}/{want[1]}）")
    else:
        ok(f"速報バナーの日付 {want[0]}/{want[1]}（{len(hits)}箇所）")


def check_ticker_comment(html: str, base: str) -> None:
    """速報ティッカー（上端を流れる帯）の書き換え漏れを、直前のコメントの日時で見る。

    ティッカーの本文は日付の決まった形を持たないので、check_ticker() では拾えない。
    日次更新のたびに本文と一緒に書き換える `<!-- 新ティッカー（YYYY年M月D日 HH:MM JST） -->` を
    基準日・ヘッダーの時刻と照合する（2026-10-03 の日次でティッカーだけ書き換えが漏れ、
    前日の内容と「封鎖217日目」が残ったまま OK 39 / WARN 0 で通った）。
    """
    hits = PAT_TICKER_COMMENT.findall(html)
    if not hits:
        ng("index.html のコメント「<!-- 新ティッカー（YYYY年M月D日 HH:MM JST） -->」を検出できませんでした"
           "（ティッカーの書き換え漏れを検査できない）")
        return
    if len(hits) > 1:
        warn(f"「新ティッカー」のコメントが {len(hits)} 箇所あります。先頭の1つで検査します")
    y, mo, d, hm = hits[0]
    got = ymd(y, mo, d)
    if got != base:
        ng(f"速報ティッカーのコメントの日付が基準日と違います: {got}（基準 {base}）。"
           "ティッカーの本文を今日の内容に書き換えたか確認すること")
        return
    m = PAT_HEADER.search(html)
    if m and m.group(4) != hm:
        warn(f"速報ティッカーのコメントの時刻 {hm} がヘッダーの時刻 {m.group(4)} と違います")
    else:
        ok(f"速報ティッカーのコメントの日時 {got} {hm}")


def check_hub_updated(html: str, base: str) -> None:
    """ハブ（docs/index.html）の「危機マップの最終更新」が、本体のヘッダー日時と同じか。

    ハブの表示は JS が news_data.json の updated で上書きするが、HTML に置いた静的な値は
    日次更新が書き換える（JS が動かない環境・検索エンジン向けの予備）。書き換え漏れを NG にする。
    """
    try:
        hub = HUB.read_text(encoding="utf-8")
    except FileNotFoundError:
        ng("docs/index.html（ハブ）が見つかりません")
        return
    m = PAT_HUB_UPDATED.search(hub)
    if not m:
        ng("ハブ（docs/index.html）の「危機マップの最終更新」（id=\"hub-updated\" の M/D HH:MM）を検出できませんでした")
        return
    mo, d, hm = int(m.group(1)), int(m.group(2)), m.group(3)
    want = (int(base[5:7]), int(base[8:10]))
    if (mo, d) != want:
        ng(f"ハブの「危機マップの最終更新」の日付が基準日と違います: {mo}/{d}（基準 {want[0]}/{want[1]}）")
        return
    h = PAT_HEADER.search(html)
    if h and h.group(4) != hm:
        warn(f"ハブの「危機マップの最終更新」の時刻 {hm} が本体のヘッダーの時刻 {h.group(4)} と違います")
    else:
        ok(f"ハブの「危機マップの最終更新」 {mo}/{d} {hm}")


def check_route_freshness(html: str, base: str) -> None:
    """全ルート現況サマリーの各行本文が、見出しの日付更新だけで放置されていないかを見る。

    見出し（sec-h2-sub）の日付は collect_dates() で当日一致を確認できるが、
    見出しだけ更新して本文（現況詳細セル）が古いまま、という事故は日付整合では検出できない
    （2026-09-15 にルートB＝サウジ東西PLで実際に発生：見出しは当日日付なのに本文は4/12時点のままだった）。
    そこで各行の本文中に出てくる M/D 形式の日付表記を拾い、最新のものが基準日から
    どれだけ離れているかを見る。あくまで見出し語による推定なので、NG ではなく WARN に留める。
    """
    table_m = PAT_ROUTE_TABLE.search(html)
    if not table_m:
        warn("全ルート現況サマリーの表を検出できませんでした（構造が変わった可能性）")
        return

    try:
        base_date = date.fromisoformat(base)
    except ValueError:
        return  # 基準日自体の異常は check_base_date 側で NG 済み

    rows = PAT_ROUTE_ROW.findall(table_m.group(0))
    seen_any_row = False
    for row_html in rows:
        id_m = PAT_ROUTE_ROW_ID.search(row_html)
        if not id_m:
            continue  # ヘッダー行など、ルート行以外
        seen_any_row = True
        route = id_m.group(1)
        text = re.sub(r"<[^>]+>", " ", row_html)  # href 等はタグごと除去されるので誤検出しない

        newest_md: date | None = None
        for mm, dd in PAT_ROUTE_ROW_MD.findall(text):
            try:
                d = date(base_date.year, int(mm), int(dd))
            except ValueError:
                continue
            if d > base_date + timedelta(days=1):
                continue  # 表記ゆれ等で未来日になったものは日付として扱わない
            if newest_md is None or d > newest_md:
                newest_md = d

        # ② PR3 の型：「最新」は p.route-latest の <time datetime> を正とする
        latest = PAT_ROUTE_LATEST.findall(row_html)
        if len(latest) == 1:
            newest = date.fromisoformat(latest[0])
            if newest_md and newest_md > newest:
                warn(
                    f"全ルート現況サマリー / ルート{route} 行に「最新」（{newest.isoformat()}）より新しい日付表記 "
                    f"{newest_md.isoformat()} があります。新しい情報は「最新」に書き、前の「最新」は経緯へ移す"
                    "（daily-site-update「ルート表の型」）"
                )
        else:
            warn(
                f"全ルート現況サマリー / ルート{route} 行の「最新」（p.route-latest＋<time datetime>）が "
                f"{len(latest)}件です（型は1件。daily-site-update「ルート表の型」）。本文中の日付表記で鮮度を推定します"
            )
            newest = newest_md

        if newest is None:
            warn(f"全ルート現況サマリー / ルート{route} 行に本文中の日付表記が見つかりません（鮮度確認不可）")
            continue

        age = (base_date - newest).days
        if age > STALE_ROUTE_DAYS:
            warn(
                f"全ルート現況サマリー / ルート{route} 行の本文中で最も新しい日付表記が "
                f"{newest.isoformat()}（基準日から{age}日前）。見出しの日付だけ更新して"
                "本文が古いままになっていないか確認すること"
            )
        else:
            ok(f"全ルート現況サマリー / ルート{route} 行の鮮度（最新 {newest.isoformat()}、{age}日前）")

    if not seen_any_row:
        warn("全ルート現況サマリーの表からルート行（jf-td-* を含む行）を検出できませんでした（構造が変わった可能性）")


# ── 個別チェック ────────────────────────────────────────────
def check_news(news: dict, base: str) -> None:
    latest = news.get("latest")
    if not isinstance(latest, list):
        ng("news_data.json の latest が配列ではありません")
        return

    if len(latest) == 4:
        ok("news_data.json / latest 4件")
    else:
        ng(f"news_data.json / latest が {len(latest)}件です（ルールは4件）")

    for i, item in enumerate(latest, 1):
        miss = [k for k in LATEST_REQUIRED if k not in item or item[k] in ("", None)]
        if miss:
            ng(f"latest[{i}] に必須フィールドがありません: {', '.join(miss)}")
        hit = [k for k in LATEST_FORBIDDEN if k in item]
        if hit:
            ng(f"latest[{i}] に旧スキーマのフィールドが混じっています: {', '.join(hit)}")
    if not any("に必須フィールド" in e or "旧スキーマ" in e for e in errors):
        ok("latest の必須フィールド・禁止フィールド")

    n = sum(1 for x in latest if x.get("isLatest"))
    if n == 1:
        ok("latest の isLatest: true が1件")
    else:
        ng(f"latest の isLatest: true が {n}件です（1件のみ）")

    osint = news.get("osint")
    if isinstance(osint, list):
        n = sum(1 for x in osint if x.get("isLatest"))
        if n == 1:
            ok("osint の isLatest: true が1件")
        else:
            ng(f"osint の isLatest: true が {n}件です（1件のみ）")
    else:
        ng("news_data.json の osint が配列ではありません")

    # staleNotice は「新情報がある日は空文字」。日付付き文言なら基準日と一致させる
    stale = news.get("staleNotice", "")
    if stale:
        m = re.search(r"(\d{1,2})/(\d{1,2})", stale)
        if m and (int(m.group(1)), int(m.group(2))) != (int(base[5:7]), int(base[8:10])):
            ng(f"news_data.json の staleNotice の日付が基準日と違います: {stale[:40]}")


def check_log(log, base: str) -> None:
    if not isinstance(log, list) or not log:
        ng("update_log.json が空か、配列ではありません")
        return
    head = log[0].get("date", "")
    m = re.match(r"(\d{4})/(\d{1,2})/(\d{1,2})", head)
    if not m:
        ng(f"update_log.json の先頭の date を解釈できません: {head!r}")
    elif ymd(*m.groups()) == base:
        ok(f"update_log.json の先頭が基準日（{head}）")
        check_blockade_wording("update_log.json の当日分", log[0].get("text", ""))
    else:
        ng(f"update_log.json の先頭が基準日ではありません: {head}（基準 {base}）")


# 日数の呼び名は「危機N日目」（2026-10-02〜）。「封鎖」は主語を付けて書く。
# 過去の本文は書き換えない方針なので、当日に書いた分だけを見る（tools/blockade-term-policy.md）
PAT_BLOCKADE_DAY = re.compile(r'封鎖\s*\d+\s*日目')
PAT_DUAL_BLOCKADE_BARE = re.compile(r'(?<!による)(?<!紅海の)二重封鎖')


def check_blockade_wording(label: str, text: str) -> None:
    found = PAT_BLOCKADE_DAY.findall(text or "")
    if found:
        warn(f"{label} に「{found[0]}」があります。日数は「危機N日目」と書く（開戦 2/28 からの日数）")
    if PAT_DUAL_BLOCKADE_BARE.search(text or ""):
        warn(f"{label} に主語のない「二重封鎖」があります。「イラン・米国による二重封鎖」"
             "「ホルムズ・紅海の二重封鎖」のどちらかで書く")


def check_military(base: str) -> None:
    """地図の軍事レイヤー（military.json）が日次で見直されているか、形が壊れていないか。

    2026-04-18 から 10-11 まで半年のあいだ誰も見直さず、4月の発動直後の説明が地図に残っていた。
    - checked（見直した日）が基準日か（WARN）。本文を変えた日は updated も基準日にする
    - 必須項目・日付の形（NG）
    - 座標・印の増減・id・type・色が直前のコミットから変わっていないか（WARN。日次では変えない決まり）
    - 「封鎖」の書き方・説明の長さ・出典の有無（WARN）
    """
    try:
        data = json.loads(MILITARY.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        ng(f"military.json を読めません（{type(e).__name__}）。地図の艦隊・港・海域が出なくなります")
        return
    upd, chk = str(data.get("updated", "")), str(data.get("checked", ""))
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", upd) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", chk):
        ng(f"military.json の updated「{upd}」・checked「{chk}」が YYYY-MM-DD ではありません")
        return
    if upd > chk:
        ng(f"military.json の updated {upd} が checked {chk} より後です（本文を変えた日は checked も同じ日にする）")
    items = []
    for key in ("fleets", "ports", "blockadeZones"):
        for it in data.get(key) or []:
            items.append((key, it))
            need = ["id", "name", "detail", "source", "type"] + (["coords", "color"] if key == "blockadeZones" else ["lat", "lng", "status", "emoji"])
            lack = [k for k in need if it.get(k) in (None, "", [])]
            if lack:
                ng(f"military.json {key} / {it.get('id', '?')} に必須項目がありません: {', '.join(lack)}")
    if not items:
        ng("military.json に艦隊・港・海域が1件もありません")
        return
    if chk != base:
        warn(f"military.json の checked が {chk} です（基準 {base}）。地図の艦隊・港・海域の説明を今日の情報で見直し、"
             "checked を基準日にする（本文を変えたら updated も）。daily-site-update「地図の軍事レイヤー」")
    else:
        ok(f"military.json 見直し済み（checked {chk}・本文の更新 {upd}・{len(items)}件）")
    for key, it in items:
        label = f"military.json {it.get('id')}"
        text = " ".join(str(it.get(k, "")) for k in ("name", "status", "detail"))
        check_blockade_wording(label, text)
        if re.search(r"封鎖対象|封鎖中|封鎖任務|米封鎖|封鎖強度", text):
            warn(f"{label} に主語のない「封鎖」があります。「米軍の対イラン海上封鎖」のように誰が・どこをを書く")
        if len(str(it.get("detail", ""))) > MILITARY_DETAIL_MAX:
            warn(f"{label} の説明が {len(str(it.get('detail', '')))}字です（目安 {MILITARY_DETAIL_MAX}字）。"
                 "古い数字は新しい数字で置き換える（積み増さない）")
        if not re.search(r"\d{1,2}/\d{1,2}", str(it.get("source", ""))):
            warn(f"{label} の出典に日付（M/D）がありません: {it.get('source')}")

    # 直前のコミットと比べる：日次では座標・印の増減・id・type・色を変えない
    import subprocess
    try:
        head = subprocess.run(["git", "show", f"HEAD:{MILITARY_REL}"], cwd=ROOT, capture_output=True, timeout=20)
        prev = json.loads(head.stdout.decode("utf-8")) if head.returncode == 0 else None
    except Exception:  # git が無い・壊れた JSON など。比べられないだけで止めない
        prev = None
    if prev is None:
        return
    def shape(dat):
        out = {}
        for key in ("fleets", "ports", "blockadeZones"):
            for it in dat.get(key) or []:
                out[(key, it.get("id"))] = (it.get("type"), it.get("emoji"), it.get("lat"), it.get("lng"),
                                            json.dumps(it.get("coords")), it.get("color"), it.get("opacity"))
        return out
    a, b = shape(prev), shape(data)
    if a != b:
        diff = sorted({f"{k[0]}/{k[1]}" for k in set(a) ^ set(b)} | {f"{k[0]}/{k[1]}" for k in set(a) & set(b) if a[k] != b[k]})
        warn(f"military.json の印・座標・種別が直前のコミットから変わっています: {', '.join(diff)}。"
             "日次では説明（name・status・detail・source）だけを書き換える。印の追加・削除や座標の変更が要るときは報告に書く")


def check_timeline(tl, base: str) -> None:
    entries = (tl or {}).get("entries")
    if not isinstance(entries, list) or not entries:
        ng("archive_timeline.json の entries が空か、配列ではありません")
        return
    last = entries[-1].get("date", "")
    if last == base:
        ok(f"archive_timeline.json の末尾が基準日（{last}）")
        check_blockade_wording("archive_timeline.json の当日分", entries[-1].get("summary", ""))
    else:
        # 速報を出さなかった日は追記しないルールなので、これは警告に留める
        warn(f"archive_timeline.json の末尾が基準日ではありません: {last}（基準 {base}）"
             "／速報を出さなかった日なら正常")

    dates = [e.get("date") for e in entries]
    dup = {d for d in dates if dates.count(d) > 1}
    if dup:
        ng(f"archive_timeline.json に日付の重複があります: {', '.join(sorted(dup))}")


def check_sitemap(tl, base: str) -> None:
    """sitemap.xml の lastmod が実態に追従しているか。

    Google は lastmod が一貫して正確な場合にのみ利用する。トップが日次更新されているのに
    lastmod が 2026-05-20 のまま放置されていた（2026-09-19 に発覚）ための追加。
    - `/hormuz/` と `/`（ハブ。「危機マップの最終更新」を書き換える）は日次更新のたびに変わるので基準日と一致すること（NG）
    - `/archive/` は archive_timeline に追記した日だけ変わるので、末尾の日付より古くないこと（NG）
    """
    try:
        xml = SITEMAP.read_text(encoding="utf-8")
    except FileNotFoundError:
        ng("docs/sitemap.xml が見つかりません")
        return

    m = PAT_SITEMAP_TOP.search(xml)
    if not m:
        ng("sitemap.xml の /hormuz/ の lastmod を検出できませんでした（構造が変わった可能性）")
    elif m.group(1) == base:
        ok(f"sitemap.xml /hormuz/ の lastmod {m.group(1)}")
    else:
        ng(f"sitemap.xml /hormuz/ の lastmod が基準日と違います: {m.group(1)}（基準 {base}）")

    m = PAT_SITEMAP_HUB.search(xml)
    if not m:
        ng("sitemap.xml の /（ハブ）の lastmod を検出できませんでした（構造が変わった可能性）")
    elif m.group(1) == base:
        ok(f"sitemap.xml /（ハブ）の lastmod {m.group(1)}")
    else:
        ng(f"sitemap.xml /（ハブ）の lastmod が基準日と違います: {m.group(1)}（基準 {base}）")

    entries = (tl or {}).get("entries")
    last = entries[-1].get("date", "") if isinstance(entries, list) and entries else ""
    m = PAT_SITEMAP_ARCHIVE.search(xml)
    if not m:
        ng("sitemap.xml の /archive/ の lastmod を検出できませんでした（構造が変わった可能性）")
    elif not last:
        warn("archive_timeline.json の末尾日付が取れないため、/archive/ の lastmod を照合できません")
    elif m.group(1) < last:
        ng(f"sitemap.xml /archive/ の lastmod が archive_timeline 末尾より古いです: "
           f"{m.group(1)}（末尾 {last}）")
    else:
        ok(f"sitemap.xml /archive/ の lastmod {m.group(1)}（archive_timeline 末尾 {last}）")


def load_data_context() -> tuple[dict | None, str]:
    """hormuz-data- の context.json を読む。ローカル → 公開 URL の順。

    戻り値は (内容, 取得元または失敗理由)。どちらも失敗したら内容は None。
    """
    import urllib.request

    reasons: list[str] = []
    if DATA_CONTEXT_LOCAL.is_file():
        try:
            return json.loads(DATA_CONTEXT_LOCAL.read_text(encoding="utf-8")), "ローカル ../hormuz-data-"
        except (OSError, ValueError) as e:
            reasons.append(f"ローカル読み込み失敗（{type(e).__name__}）")
    else:
        reasons.append("ローカルの ../hormuz-data- なし")

    req = urllib.request.Request(DATA_CONTEXT_URL, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return json.loads(res.read().decode("utf-8")), "公開 URL"
    except Exception as e:  # ネットワーク到達不能・HTTP エラー・タイムアウト・JSON 破損等
        reasons.append(f"公開 URL 取得失敗（{type(e).__name__}）")
    return None, "／".join(reasons)


def check_data_timeline() -> None:
    """hormuz-data- の経緯（context.json の timeline）の最新日が古すぎないか。

    WARN のみ。別リポジトリの状態で hormuz-map の commit を止めないため NG にはしない。
    基準日ではなく実測の今日（JST）から数える（ダッシュボードの判定と同じ）。
    """
    ctx, src = load_data_context()
    if ctx is None:
        warn(f"hormuz-data- の経緯（context.json の timeline）の最新日は未確認: {src}")
        return

    items = ctx.get("timeline") if isinstance(ctx, dict) else None
    dates: list[date] = []
    for item in items if isinstance(items, list) else []:
        try:
            dates.append(date.fromisoformat(str(item.get("date", ""))))
        except (AttributeError, ValueError):
            continue
    if not dates:
        warn(f"hormuz-data- の経緯（context.json の timeline）の最新日は未確認: 日付を読み取れません（{src}）")
        return

    latest = max(dates)
    today = today_jst()
    age = (date.fromisoformat(today) - latest).days
    if age > DATA_TIMELINE_WARN_DAYS:
        warn(f"hormuz-data- の経緯（context.json の timeline）の最新日が {latest.isoformat()}"
             f"（実測の今日 {today} から{age}日前、{src}）。確定した事実を追記すること"
             f"（{DATA_TIMELINE_WARN_DAYS}日超で WARN／7日超でダッシュボードに ⚠）")
    else:
        ok(f"hormuz-data- の経緯の最新日 {latest.isoformat()}（{age}日前、{src}）")


def check_oil_flow() -> None:
    """日本向け調達フロー（oil-flow.json）の対象月が、公表済みのはずの月より古くないか。

    WARN のみ。国別の数量は対象月の翌月下旬〜翌々月上旬に e-Stat に入る。
    そのため実測の今日が15日以降なら2か月前の月、14日までなら3か月前の月が出ているはず。
    hormuz-data- のワークフローが毎日確認しているので、WARN は取得が止まった印
    （2026-10-11 まで：月1回の実行が公表の前に当たり、7月分のまま3週間残った）。
    読むのは公開 URL → ローカルの順（ページが読むのは公開 URL。ローカルは pull 前だと古い）。
    """
    import urllib.request

    data, src = None, ""
    req = urllib.request.Request(OIL_FLOW_URL, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            data, src = json.loads(res.read().decode("utf-8")), "公開 URL"
    except Exception as e:  # ネットワーク到達不能・HTTP エラー・タイムアウト・JSON 破損等
        src = f"公開 URL 取得失敗（{type(e).__name__}）"
        if OIL_FLOW_LOCAL.is_file():
            try:
                data = json.loads(OIL_FLOW_LOCAL.read_text(encoding="utf-8"))
                src = "ローカル ../hormuz-data-"
            except (OSError, ValueError):
                pass
    period = ""
    if isinstance(data, dict) and isinstance(data.get("source"), dict):
        period = str(data["source"].get("period", ""))
    m = re.fullmatch(r"(\d{4})-(\d{2})", period)
    if not m:
        warn(f"日本向け調達フロー（oil-flow.json）の対象月は未確認: {src or '対象月を読み取れません'}")
        return

    today = date.fromisoformat(today_jst())
    lag = 2 if today.day >= OIL_FLOW_GRACE_DAY else 3
    want = today.year * 12 + (today.month - 1) - lag          # 出ているはずの月（年×12＋月−1）
    got = int(m.group(1)) * 12 + (int(m.group(2)) - 1)
    label = f"{int(m.group(1))}年{int(m.group(2))}月分"
    if got < want:
        warn(f"日本向け調達フロー（oil-flow.json）の対象月が {label} のままです"
             f"（実測の今日 {today.isoformat()} なら {want // 12}年{want % 12 + 1}月分が出ているはず、{src}）。"
             "hormuz-data- の毎日の取得（update_oil_flow.yml）が止まっている印。"
             "日次では直さず、報告の「確認してほしい点」に書く")
    else:
        ok(f"日本向け調達フローの対象月 {label}（{src}）")


def check_stockpile(html: str) -> None:
    """石油備蓄日数4か所（/hormuz/ の3か所とハブの1か所）が古すぎないか、互いに食い違っていないか。

    WARN のみ。値の正しさ（資源エネルギー庁の速報との一致）は機械では確かめられない。
    基準日ではなく実測の今日（JST）から数える。
    """
    today = date.fromisoformat(today_jst())
    found: dict[str, tuple[int, date]] = {}

    m = PAT_STOCKPILE_POPUP.search(html)
    if m:
        total, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        asof = date(today.year, mo, d)
        if asof > today:  # 年をまたいだ直後（1月に 12/28時点 など）
            asof = date(today.year - 1, mo, d)
        found["地図ポップアップ"] = (total, asof)
    else:
        warn("石油備蓄日数（地図の「日本の受入拠点」ポップアップ）を検出できません（書式が変わった可能性）")

    m = PAT_STOCKPILE_NOTE.search(html)
    if m:
        found["精製所表の注記"] = (int(m.group(1)), date(*map(int, m.group(2, 3, 4))))
    else:
        warn("石油備蓄日数（精製所表の注記）を検出できません（書式が変わった可能性）")

    m = PAT_STOCKPILE_CARD.search(html)
    if m:
        found["主要指標の備蓄カード"] = (int(m.group(4)), date(*map(int, m.group(1, 2, 3))))
    else:
        warn("石油備蓄日数（主要指標の備蓄カード）を検出できません（書式が変わった可能性）")

    try:
        m = PAT_STOCKPILE_HUB.search(HUB.read_text(encoding="utf-8"))
    except FileNotFoundError:
        m = None
    if m:
        found["ハブの主要な数字"] = (int(m.group(1)), date(*map(int, m.group(2, 3, 4))))
    else:
        warn("石油備蓄日数（ハブ docs/index.html の主要な数字）を検出できません（書式が変わった可能性）")

    for name, (total, asof) in found.items():
        age = (today - asof).days
        if age > STOCKPILE_WARN_DAYS:
            warn(f"石油備蓄日数（{name}）が {asof.isoformat()}時点のまま（{age}日前）。"
                 f"毎月4日の PC タスクが止まっている可能性。日次では書き換えず、報告に書くこと"
                 f"（PC 側で tools/oil-stockpile-monthly-update.md の手順で4か所とも更新する）")
        else:
            ok(f"石油備蓄日数（{name}）{total}日分・{asof.isoformat()}時点（{age}日前）")

    if len(found) >= 2 and len(set(found.values())) != 1:
        detail = "／".join(f"{k} {t}日分・{a.isoformat()}" for k, (t, a) in found.items())
        warn(f"石油備蓄日数の{len(found)}か所が食い違っています: {detail}")


def check_column_pills(html: str) -> None:
    """特別解説コラムのピルの data-published / data-updated が記事ページと揃っているか。

    札（NEW／◯月更新）はこの日付から表示を決めるので、記事だけ更新してピルを忘れると札が出ない。
    WARN のみ。
    """
    pills = PAT_COLUMN_PILL.findall(html)
    if not pills:
        warn("特別解説コラムのピル（data-published / data-updated 付き）を検出できません（書式が変わった可能性）")
        return
    # 属性の付け忘れ・順番違いのピルは上の正規表現に掛からず黙って漏れるので、総数と突き合わせる
    all_pills = PAT_COLUMN_PILL_ANY.findall(html)
    missing = sorted(set(all_pills) - {p[0] for p in pills})
    if missing:
        warn(f"特別解説コラムのピルのうち、日付を読み取れないものがあります: "
             f"{', '.join('articles/' + f for f in missing)}。"
             f"data-published / data-updated を href・class の後にこの順で付けること（札が出ません）")
    try:
        idx_text = (ROOT / "docs" / "hormuz" / "articles" / "index.html").read_text(encoding="utf-8")
    except OSError:
        idx_text = ""
    for fname, pub, upd in pills:
        path = ROOT / "docs" / "hormuz" / "articles" / fname / "index.html"
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            warn(f"コラムのピルのリンク先が読めません: articles/{fname}")
            continue
        mp, mm = PAT_ARTICLE_PUBLISHED.search(text), PAT_ARTICLE_MODIFIED.search(text)
        a_pub, a_mod = (mp.group(1) if mp else None), (mm.group(1) if mm else None)
        # 同じ記事の日付は、ほかに3か所ある：記事の見える「最終更新」（＝更新日）、
        # 本体のコラムのカードと記事一覧（「公開 …」。加筆した記事は「公開 …・更新 …」）。
        # 記事の JSON-LD と同じ日付か（F7・2026-10-11）
        def label(p_, m_):
            if not p_ or not m_:
                return None
            text_ = "公開 " + p_.replace("-", "/")
            return text_ if m_ == p_ else text_ + "・更新 " + m_.replace("-", "/")
        want = label(a_pub, a_mod)
        others = []
        mv = PAT_ARTICLE_VISIBLE.search(text)
        others.append(("記事の「最終更新」", "-".join(mv.groups()) if mv else None, a_mod))
        card = None
        for seg in re.split(r'(?=<div class="col-card[ "])', html):
            if f'href="articles/{fname}/" class="col-card-link"' in seg:
                mc = PAT_COL_CARD_DATE.search(seg)
                card = mc.group(1) if mc else None
                break
        others.append(("本体のコラムのカード", card, want))
        idx = {m.group(1): m.group(2) for m in PAT_IDX_CARD.finditer(idx_text)}
        others.append(("記事一覧 hormuz/articles/index.html", idx.get(fname), want))
        diff = [f"{name}「{got or '検出できず'}」（正しくは「{exp}」）" for name, got, exp in others if got != exp]
        if diff:
            warn(f"コラム articles/{fname} の日付が食い違っています: {'／'.join(diff)}。"
                 f"カードと記事一覧は「公開 YYYY/MM/DD」（加筆した記事は「・更新 YYYY/MM/DD」を足す）、"
                 f"記事の「最終更新」は dateModified に揃えること")
        if (pub, upd) == (a_pub, a_mod):
            ok(f"コラムのピル articles/{fname}（公開 {pub}・更新 {upd}）" + ("" if diff else "・カード・一覧・記事の表示も一致"))
        else:
            warn(f"コラムのピル articles/{fname} の日付が記事と違います: "
                 f"ピル 公開 {pub}・更新 {upd}／記事 datePublished {a_pub}・dateModified {a_mod}。"
                 f"ピルの data-published / data-updated を記事に揃えること")


def check_urls(news: dict) -> None:
    """latest の URL が生きているか。捏造URL禁止ルールの機械的な担保。"""
    import urllib.error
    import urllib.request

    for i, item in enumerate(news.get("latest", []), 1):
        url = item.get("url", "")
        if not url.startswith("http"):
            ng(f"latest[{i}] の url が URL の形になっていません: {url!r}")
            continue
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=15) as res:
                code = res.status
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception as e:  # ネットワーク到達不能・SSL・タイムアウト等
            warn(f"latest[{i}] の url を確認できませんでした（{type(e).__name__}）: {url}")
            continue
        if code == 404 or code == 410:
            ng(f"latest[{i}] の url が {code} を返しました（URL の捏造・誤記を疑う）: {url}")
        elif code >= 400:
            warn(f"latest[{i}] の url が {code} を返しました（Bot 遮断の可能性）: {url}")
        else:
            ok(f"latest[{i}] の url {code}")


PAT_GLANCE = re.compile(r'<div class="glance">.*?<!-- /30秒カラム ラッパー -->', re.S)
PAT_KEY_MOVE = re.compile(r'<li class="key-move key-move--(\w+)">.*?<time class="key-move-date" datetime="(\d{4}-\d{2}-\d{2})">', re.S)
PAT_INCIDENT_LIST = re.compile(r'<ul id="incident-list"[^>]*>.*?</ul>', re.S)


def check_types(html: str, base: str) -> None:
    """② で決めた型（クラス＋モディファイア・インライン style なし）で書かれているか。
    30秒カラム（主な動き3件を含む）・速報インシデントの一覧・ルート表・シナリオ・更新履歴が対象。見た目は壊れないので WARN にとどめる。"""
    g = PAT_GLANCE.search(html)
    if not g:
        warn("30秒カラム（<div class=\"glance\">）を検出できませんでした（構造が変わった可能性）")
    else:
        body = g.group(0)
        n_style = body.count('style="')
        if n_style:
            warn(f"30秒カラムにインライン style が {n_style}箇所あります（型はクラス。daily-site-update「30秒カラムの型」）")
        else:
            ok("30秒カラムにインライン style なし")
        moves = PAT_KEY_MOVE.findall(body)
        if len(moves) != 3:
            warn(f"30秒カラム / 主な動きが {len(moves)}件です（ルールは3件）")
        else:
            dates = [d for _, d in moves]
            age = (date.fromisoformat(base) - date.fromisoformat(dates[0])).days
            if dates != sorted(dates, reverse=True):
                warn(f"30秒カラム / 主な動きが新しい順になっていません: {', '.join(dates)}")
            elif age > 7:
                warn(f"30秒カラム / 主な動きの最新が {dates[0]}（{age}日前）です。速報インシデントの先頭と揃っているか確認")
            else:
                ok(f"30秒カラム / 主な動き 3件（最新 {dates[0]}）")
    a = re.search(r'<span class="badge-item badge-alert">(.*?)</span>', html, re.S)
    if a and (len(a.group(1)) > 12 or "（" in a.group(1)):
        warn(f"ヘッダーの警戒レベルに要約が書かれています（{len(a.group(1))}字）。「警戒レベル：最高」の一語だけにする")
    elif a:
        ok(f"ヘッダーの警戒レベル「{a.group(1)}」")
    t = PAT_ROUTE_TABLE.search(html)
    if t:
        # <col> の幅だけは style のまま残す（html-safe-edit「colgroup を触らない」）
        n_style = len(re.findall(r'<(?!col\b)\w+[^>]*\sstyle="', t.group(0)))
        if n_style:
            warn(f"ルート表にインライン style が {n_style}箇所あります（型はクラス。daily-site-update「ルート表の型」）")
        else:
            ok("ルート表にインライン style なし（<col> を除く）")
    if 'class="sec-lead"' in html[html.find('全ルート現況サマリー'):html.find('<!-- ROUTE TABLE -->')]:
        warn("全ルート現況サマリーの見出しの下にリード文（p.sec-lead）があります。② PR3 で廃止した。各行の「最新」に書く")
    m = PAT_INCIDENT_LIST.search(html)
    if m:
        n_style = m.group(0).count('style="')
        if n_style:
            warn(f"速報インシデントの一覧にインライン style が {n_style}箇所あります（型は li.incident-item＋モディファイア）")
        else:
            ok("速報インシデントの一覧にインライン style なし")
    # ② PR4a：シナリオ（S06〜S08）と更新履歴
    # 終わりは <!-- /SCENARIOS（2026-10-21。主要指標を速報インシデントの上へ移し、<!-- STATS --> がシナリオの前に来たため）
    i = html.find("<!-- SCENARIOS -->")
    j = html.find("<!-- /SCENARIOS", i)
    if i < 0 or j < i:
        warn("シナリオ（<!-- SCENARIOS -->〜<!-- /SCENARIOS -->）を検出できませんでした（構造が変わった可能性）")
    else:
        n_style = html[i:j].count('style="')
        if n_style:
            warn(f"シナリオにインライン style が {n_style}箇所あります（型はクラス。daily-site-update「シナリオの型」）")
        else:
            ok("シナリオにインライン style なし")
    m = re.search(r'<section class="update-log".*?</section>', html, re.S)
    if not m:
        warn("更新履歴（section.update-log）を検出できませんでした（構造が変わった可能性）")
    else:
        log = m.group(0)
        # 開閉の状態を JS が読む #log-collapse・#log-toggle-bottom の display:none だけは残す
        n_style = log.count('style="') - log.count('style="display:none;"')
        if n_style:
            warn(f"更新履歴にインライン style が {n_style}箇所あります（型はクラス。daily-site-update「更新履歴の型」）")
        else:
            ok("更新履歴にインライン style なし（開閉の display:none を除く）")
        k = log.find('id="log-collapse"')
        recent = log[:k].count('class="log-date"') if k >= 0 else -1
        total = log.count('class="log-date"')
        if recent != 3 or total > 10:
            warn(f"更新履歴の件数：常時表示 {recent}件・合計 {total}件（ルールは常時表示3件・合計10件まで）")
        else:
            ok(f"更新履歴の件数：常時表示 3件・合計 {total}件")

    # ページ全体（② PR4b・2026-10-01 で <body> のインライン style は JS が状態として読む8か所だけになった）
    bi = html.find('<body')
    page = re.sub(r'<script\b[^>]*>.*?</script\b[^>]*>', '', html[bi:], flags=re.S | re.I) if bi >= 0 else ''
    extra = []
    for m in re.finditer(r'<(\w+)\b([^>]*?)\sstyle="([^"]*)"', page):
        tag, attrs, val = m.group(1), m.group(2), m.group(3)
        idm = re.search(r'\bid="([^"]+)"', attrs + m.group(0))
        if tag == 'col' or (idm and (idm.group(1), val.strip()) in STYLE_ALLOWED):
            continue
        extra.append(f"<{tag}{' #' + idm.group(1) if idm else ''}> {val.strip()[:40]}")
    if extra:
        warn(f"ページにインライン style が {len(extra)}箇所あります（JS が読む開閉の状態を除く。型はクラス）: " + "／".join(extra[:5]))
    else:
        ok("ページ全体にインライン style なし（JS が読む開閉の状態・<col> を除く）")

    # JS が組み立てる HTML（②' PR E・2026-10-12 でクラスにした）。
    # 残してよいのは、計算やデータで決まる値（${…} を含む）と、JS が読む開閉の display:none だけ
    scripts = "".join(re.findall(r'<script\b[^>]*>(.*?)</script\b[^>]*>', html[bi:], flags=re.S | re.I)) if bi >= 0 else ''
    # 引用符は二重・単一の両方を見る。属性のほか、JS からまとめて書き込む形（cssText・setAttribute('style', …)）も拾う
    fixed = [v.strip()[:40] for _, v in re.findall(r'''\sstyle=(["'])(.*?)\1''', scripts, flags=re.S)
             if '${' not in v and v.strip() != 'display:none;']
    fixed += [m.strip()[:40] for m in re.findall(r'''\.style\.cssText\s*\+?=[^;\n]*|setAttribute\(\s*["']style["'][^)\n]*\)''', scripts)
              if '${' not in m]
    if fixed:
        warn(f"JS のテンプレートに固定値のインライン style が {len(fixed)}箇所あります（型はクラス。html-safe-edit「JS が組み立てる HTML」）: " + "／".join(fixed[:5]))
    else:
        ok("JS のテンプレートに固定値のインライン style なし（計算・データで決まる値と開閉の display:none を除く）")


# ── main ────────────────────────────────────────────────────
def check_log_wording(html: str, base: str) -> None:
    """基準日の更新履歴の本文に「OSINT」「osint」が出ていないか。

    「OSINT」は開発の経緯で残った内部の呼び名で、読者に見える名前は「現地メディア視点」（2026-10-05 決定）。
    過去の行は書き換えない方針なので、見るのは基準日の行だけ。
    """
    y, m, d = base.split("-")
    lines = [l for l in html.splitlines() if f'log-date">{y}/{m}/{d}' in l]
    if not lines:
        return  # 行の有無は更新履歴の検査（check_types）が見る
    if any(re.search(r"osint", l, re.I) for l in lines):
        warn(f"基準日 {base} の更新履歴の本文に「OSINT／osint」があります。「現地メディア視点を更新」と書きます")
    else:
        ok(f"基準日 {base} の更新履歴の本文に「OSINT／osint」なし")


UNRESOLVED_WORDS = ("終値かは未確認", "終値未確認", "食い違", "未解消")
OFFICIAL_UNREAD_WORDS = ("公式の本文は未確認", "公式の本文は読めていない")
PAT_TICKER_TEXT = re.compile(r'<span class="ticker-text">(.*?)</span>', re.S)
PAT_SC_UPDATE = re.compile(r'<div class="sc-update">.*?<div class="sc-sync-note">', re.S)
PAT_SC_UPDATE_DATE = re.compile(r'sc-update-date">\s*(?:📊\s*)?(\d{4})年(\d{1,2})月(\d{1,2})日\s+(\d{1,2}:\d{2})\s*JST')
PAT_LOG_FIRST = re.compile(r'<span class="log-date">(\d{4})/(\d{2})/(\d{2})\s+(\d{1,2}:\d{2})</span>')
PAT_SC_SYNC_NOTE = re.compile(r'<div class="sc-sync-note">(.*?)</div>', re.S)
PAT_SC_FOOTER_LABEL = re.compile(r'<h3 class="sc-focus-h">[^<]*<span class="label-scenario[^"]*">(.*?)</span>\s*</h3>', re.S)


def check_unresolved(html: str) -> None:
    """読者が最初に見る要約部に、裏取りで解消すべき表記が残っていないか（2026-10-06 追加）。

    10/6 07:33 の更新で「食い違い（未解消）」「終値かは未確認」のまま公開し、のちに訂正した。
    対象は 30秒カラム（主な動き・バッジを含む）・TICKER・シナリオの確率補足バナー。
    速報インシデントとルート表の経緯は過去の記録を含むので見ない。
    """
    blocks = []
    for label, pat, grp in (("30秒カラム", PAT_GLANCE, 0), ("TICKER", PAT_TICKER_TEXT, 1),
                            ("シナリオの確率補足", PAT_SC_UPDATE, 0)):
        m = pat.search(html)
        if not m:
            warn(f"{label}を検出できず、未解消の表記を確認できません（構造が変わった可能性）")
            continue
        blocks.append((label, m.group(grp)))
    for label, text in blocks:
        hits = [w for w in UNRESOLVED_WORDS if w in text]
        if hits:
            warn(f"{label}に未解消の表記があります：{'・'.join(hits)}。"
                 "裏取り（daily-site-update「2.5 裏取り」）で解消して書き直すか、記述を外す")
        else:
            ok(f"{label}に未解消の表記なし")

    # 速報インシデントの先頭3件に「公式の本文は未確認」が残っていないか（2026-10-10 追加）。
    # UKMTO の警報の本文は tools/fetch_ukmto.py で読める。10/10 07:06 の更新は読めないまま運営者に確認を回した。
    m = PAT_INCIDENT_LIST.search(html)
    if not m:
        warn("速報インシデントの一覧を検出できず、公式の本文の未確認を確認できません（構造が変わった可能性）")
    else:
        items = re.findall(r'<li class="incident-item.*?</li>', m.group(0), re.S)[:3]
        hits = [w for w in OFFICIAL_UNREAD_WORDS if any(w in it for it in items)]
        if hits:
            warn(f"速報インシデントの先頭3件に公式の本文の未確認があります：{'・'.join(hits)}。"
                 "python tools/fetch_ukmto.py で読んで直す（スクリプトが終了コード 2 のときだけ残してよい）")
        else:
            ok("速報インシデントの先頭3件に公式の本文の未確認なし")


# 文字数の目安（2026-10-11 追加）。厳密な上限ではなく、超えたら WARN で知らせる。
# 10/11 の 30秒カラム（いま何が 766字・海峡の今 661字）がスマホで読む気がしない長さだったため、
# 運営者の指示で約4割減を目安にした。シナリオの補足も 🅒 が 610字あった
TEXT_LIMITS_GLANCE = (("now", "いま何が", 450), ("strait", "海峡の今", 400), ("next", "次の焦点", 250))
TEXT_LIMIT_SC_SUMMARY = 150   # シナリオの補足の冒頭（📊 今日の動きの要約）
TEXT_LIMIT_SC_LINE = 170      # 🅐〜🅓 の各行
TEXT_LIMIT_SC_CAVEAT = 150    # 但し書き（sc-update-caveat）


def plain_len(fragment: str) -> int:
    return len(re.sub(r"\s+", "", re.sub(r"<[^>]+>", "", fragment)))


def check_text_lengths(html: str) -> None:
    """30秒カラムの3行とシナリオの補足が、文字数の目安を超えていないか（WARN のみ）。"""
    for key, label, limit in TEXT_LIMITS_GLANCE:
        m = re.search(r'glance-label--' + key + r'">[^<]*</span>\s*<span class="glance-text">(.*?)</span>', html, re.S)
        if not m:
            warn(f"30秒カラム「{label}」を検出できず、文字数を確認できません（構造が変わった可能性）")
            continue
        n = plain_len(m.group(1))
        if n > limit:
            warn(f"30秒カラム「{label}」が {n}字（目安 {limit}字）。要点を絞り、細部は速報インシデントへ")
        else:
            ok(f"30秒カラム「{label}」{n}字（目安 {limit}字）")
    m = PAT_SC_UPDATE.search(html)
    if not m:
        warn("シナリオの補足（div.sc-update）を検出できず、文字数を確認できません")
        return
    body = m.group(0)
    PAT_KEY = re.compile(r'sc-key">([A-D])<|([🅐🅑🅒🅓])')   # 各行の頭は 🅐〜🅓（見やすさを優先した例外・2026-10-20）
    seen_summary = False
    for part in body.split("<br>"):
        mm = PAT_KEY.search(part)
        if "sc-update-caveat" in part:
            label, limit = "但し書き", TEXT_LIMIT_SC_CAVEAT
        elif mm:
            label, limit = (mm.group(1) or "ABCD"["🅐🅑🅒🅓".index(mm.group(2))]) + " の行", TEXT_LIMIT_SC_LINE
        elif "<strong>" in part and not seen_summary:   # 冒頭の要約（旧 📊 の行）
            label, limit = "冒頭の要約", TEXT_LIMIT_SC_SUMMARY
            seen_summary = True
        else:
            continue
        n = plain_len(part.split('<div class="sc-sync-note">')[0])
        if n > limit:
            warn(f"シナリオの補足「{label}」が {n}字（目安 {limit}字）。根拠は1〜2点に絞る")
        else:
            ok(f"シナリオの補足「{label}」{n}字（目安 {limit}字）")


def check_scenario_dates(html: str, base: str) -> None:
    """シナリオ区域と更新履歴の日時（②' PR B「日時の一元化」・2026-10-07 追加）。

    ページをいつ更新したかの正本はヘッダー。シナリオの補足バナーと更新履歴の先頭は、
    区域の更新時刻として残したので、ヘッダーと同じ日時かを見る。
    シナリオの注記（sc-sync-note）とフッターのラベルには日付を書かない
    （確率の時点は JS が同期元の updated_at から出す）。書いてあれば NG。
    """
    h = PAT_HEADER.search(html)
    head_time = h.group(4).zfill(5) if h else None
    for label, pat in (("シナリオの補足バナーの日時", PAT_SC_UPDATE_DATE), ("更新履歴の先頭の日時", PAT_LOG_FIRST)):
        m = pat.search(html)
        if not m:
            ng(f"{label}を検出できませんでした（構造が変わった可能性）")
            continue
        got, tm = ymd(*m.groups()[:3]), m.group(4).zfill(5)
        if got != base:
            ng(f"{label}が基準日と違います: {got}（基準 {base}）")
        elif head_time and tm != head_time:
            warn(f"{label}の時刻 {tm} がヘッダーの {head_time} と違います（同じ更新なら揃える）")
        else:
            ok(f"{label} {got} {tm}")
    m = PAT_SC_SYNC_NOTE.search(html)
    if not m:
        ng("シナリオの注記（div.sc-sync-note）を検出できませんでした（構造が変わった可能性）")
    elif re.search(r"\d{4}年\d{1,2}月\d{1,2}日", m.group(1)):
        ng("シナリオの注記（sc-sync-note）に日付が書かれています。日付は書かない（JS が同期元の updated_at から出す）")
    elif 'id="sc-sync-at"' not in m.group(1):
        ng("シナリオの注記（sc-sync-note）に <span id=\"sc-sync-at\"></span> がありません（JS が確率の時点を入れる場所）")
    else:
        ok("シナリオの注記に日付の手書きなし（時点は JS が入れる）")
    m = PAT_SC_FOOTER_LABEL.search(html)
    if not m:
        warn("シナリオのフッターのラベル（h3.sc-focus-h の中の .label-scenario）を検出できませんでした")
    elif re.search(r"\d", m.group(1)):
        ng(f"シナリオのフッターのラベルに日付が書かれています（「{m.group(1).strip()[:30]}」）。「分析」の一語だけにする")
    else:
        ok("シナリオのフッターのラベルに日付なし")


def check_state_labels(html: str) -> None:
    """読み込み中・取得失敗・未公表の表示の型（②' PR C「値と状態の表示」・2026-10-08 追加）。

    JS が値を入れる場所の HTML の初期値は「読み込み中…」（シナリオ確率は見出しの中なので「…」）。
    AI 推定の確率と日本向けフローの数値は HTML に書かない（K4）。日次更新が数値を書き込んだら NG。
    「内訳確認中」「読み込み中...」（ピリオド3つ）は PR C で外した表記で、戻っていたら NG。
    """
    bad = []
    for k in "ABCD":
        m = re.search(rf'<span id="sc-pct-{k}">(.*?)</span>', html)
        if not m:
            bad.append(f"sc-pct-{k}（検出できず）")
        elif m.group(1) != "…":
            bad.append(f"sc-pct-{k}「{m.group(1)[:12]}」")
    if bad:
        ng(f"シナリオ確率の初期値が「…」ではありません: {'・'.join(bad)}。確率の数値は HTML に書かない（JS が同期元から入れる）")
    else:
        ok("シナリオ確率の初期値は「…」（数値の手書きなし）")
    bad = []
    for k in ("old", "A", "B", "C_US", "C_GL", "D"):
        m = re.search(rf'<strong id="jf-{k}-bpd">(.*?)</strong>', html)
        if not m:
            bad.append(f"jf-{k}-bpd（検出できず）")
        elif m.group(1) != "読み込み中…":
            bad.append(f"jf-{k}-bpd「{m.group(1)[:12]}」")
    if bad:
        ng(f"日本向けフローの初期値が「読み込み中…」ではありません: {'・'.join(bad)}。数値は HTML に書かない（JS が oil-flow.json から入れる）")
    else:
        ok("日本向けフローの初期値は「読み込み中…」（数値の手書きなし）")
    # 同じ PR で型にした、ほかの初期値（JS が入れる場所。日次は触らない）
    bad = []
    for label, pat in (("t-stuck", r'<span id="t-stuck">(.*?)</span>'),
                       ("t-total", r'<span id="t-total">(.*?)</span>'),
                       ("t-breakdown", r'<span class="stat-row-val" id="t-breakdown">(.*?)</span>'),
                       ("jf-basis-date", r'<span id="jf-basis-date">(.*?)</span>')):
        m = re.search(pat, html)
        if not m:
            bad.append(f"{label}（検出できず）")
        elif m.group(1) != "読み込み中…":
            bad.append(f"{label}「{m.group(1)[:12]}」")
    units = re.findall(r'<span class="jf-unit"([^>]*)>', html)
    if len(units) != 4 or any("hidden" not in u for u in units):
        bad.append(f"jf-unit（4個とも hidden つきのはず。検出 {len(units)}個）")
    if bad:
        ng(f"日本関係船・フローの対象月・単位の初期値が型と違います: {'・'.join(bad)}")
    else:
        ok("日本関係船・フローの対象月の初期値は「読み込み中…」、単位は hidden")
    # 外した表記は、表示に出る場所（タグの中身・JS の文字列）だけを見る。
    # 更新履歴や本文がこの語に触れただけでは NG にしない
    hits = [w for w in ("内訳確認中", "読み込み中...", "データ読み込みエラー")
            if re.search(r"[>'\"`]\s*" + re.escape(w), html)]
    if hits:
        ng(f"外した表記が残っています：{'・'.join(hits)}。"
           "「読み込み中…」「取得できませんでした」「内訳は未公表（時点）」の型で書く")
    else:
        ok("状態の表示に古い表記なし（内訳確認中・読み込み中...）")


CATS = {"sea": "海上", "attack": "攻撃", "mil": "軍事", "oil": "原油・市場", "dip": "外交", "other": "その他"}
PAT_EMOJI_HEAD = re.compile(r"\s*(?:[\U0001F1E6-\U0001F1FF]|[\U0001F300-\U0001FAFF☀-➿⬀-⯿⌀-⏿])")


def check_categories(html: str, news: dict | None) -> None:
    """分類の札と絵文字（課題46 D3 PR 5b・2026-10-20 追加。設計書 §2-2）。

    日次が書く所の頭に絵文字を書かない（分類は札の語で書く）。札はクラスと語の組が6通りのどれか。
    news_data.json の latest の先頭（その日に足した1件）の label は6つの語のどれか。
    2件目以降は前の日までに書いたもので、古い書き方が残っていても書き換えない（表示のときに読み替える）。
    """
    bad = []
    places = (("速報インシデント", r'<span class="incident-tag">(?:<span class="cat [^"]+">[^<]*</span>)?(.*?)</span>'),
              ("主な動き", r'<span class="key-move-title">(.*?)</span>'),
              ("ステータスバッジ", r'<span class="status-badge[^"]*">(.*?)</span>'),
              ("ルート表の route-tag", r'<strong class="route-tag[^"]*">(.*?)</strong>'),
              ("30秒カラム", r'<span class="glance-text">(.*?)</span>'))
    for label, pat in places:
        hits = [x[:20].strip() for x in re.findall(pat, html, re.S) if PAT_EMOJI_HEAD.match(x)]
        if hits:
            bad.append(f"{label} {len(hits)}件（{hits[0]}…）")
    m = re.search(r'<span class="ticker-text">(.*?)</span>', html, re.S)
    if m:
        body = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S)
        hits = [x for x in body.split("｜") if PAT_EMOJI_HEAD.match(x)]
        if hits:
            bad.append(f"ティッカー {len(hits)}件（{hits[0].strip()[:20]}…）")
    if bad:
        ng(f"頭に絵文字があります: {'・'.join(bad)}。分類は札（<span class=\"cat cat-sea\">海上</span> など）の語で書き、絵文字は書かない")
    else:
        ok("日次が書く所の頭に絵文字なし（速報・主な動き・バッジ・route-tag・30秒カラム・ティッカー）")
    # 速報インシデントのタグは、どれも頭に札が要る（無いもの・タグが1つも無いのも NG）
    tags = re.findall(r'<span class="incident-tag">(.{0,40})', html)
    missing = [re.sub(r"<[^>]+>", "", x)[:20] for x in tags if not x.startswith('<span class="cat cat-')]
    if not tags:
        ng("速報インシデントのタグを検出できません（構造が変わった可能性）")
    elif missing:
        ng(f"速報インシデントのタグの頭に分類の札がありません: {len(missing)}件（{missing[0]}…）。"
           "<span class=\"cat cat-sea\">海上</span> などを先頭に書く")
    else:
        ok(f"速報インシデントのタグ {len(tags)}件すべての頭に分類の札")
    pairs = re.findall(r'<span class="cat cat-(\w+)">([^<]*)</span>', html)
    wrong = [f"cat-{c}「{w}」" for c, w in pairs if CATS.get(c) != w]
    if wrong:
        ng(f"分類の札のクラスと語が合っていません: {'・'.join(wrong[:5])}。組は {'・'.join(f'cat-{k}＝{v}' for k, v in CATS.items())}")
    else:
        ok(f"分類の札 {len(pairs)}個のクラスと語が一致")
    if news:
        first = (news.get("latest") or [{}])[0]
        if first.get("label") not in set(CATS.values()):
            warn(f"news_data.json の latest の先頭の label が分類の語ではありません: {str(first.get('label'))[:20]}。"
                 f"{'・'.join(CATS.values())} のどれかを書く（2件目以降と archive の古い label は書き換えない）")
        else:
            ok(f"news_data.json の latest の先頭の label は分類の語（{first.get('label')}）")


# ── 見た目の決まり（課題46 D3 PR 7b・2026-10-22 追加。設計書 §6・スキル site-design）──────────
# 絵文字：頭だけでなく文の中も見る。矢印（←→↑↓ など）と ▶◀◈▲▼◆ のような図形の記号は絵文字に数えない
PAT_EMOJI_ANY = re.compile(r"[\U0001F000-\U0001FAFF☀-➿⌚⌛⏩-⏺⭐⭕⬛⬜]")
# 絵文字でも残してよい記号（どのページでも）。🅐〜🅓＝シナリオ（PR 5b-1）・✕＝閉じるボタン・
# ★＝日本の受入拠点の説明・✦＝トランプ声明の枠（PR 7 の Q6。▶◀◈ と同じく記号として残す）
EMOJI_ALLOWED = set("🅐🅑🅒🅓✕★✦")
# ページごとの例外。/corrections/ は過去の表示をそのまま引用した訂正の記録（直すと訂正の中身が変わる）
EMOJI_ALLOWED_PAGE = {"corrections/index.html": set("🇺🇸🌍🚢")}
# 直書きの色（16進・rgb()・hsl()・色名）。トークン（tokens.css）を使う
PAT_COLOR = re.compile(r"#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3,4}\b|\b(?:rgba?|hsla?)\([^)]*\)")
PAT_COLOR_NAME = re.compile(r"\b(?:white|black|red|blue|green|yellow|orange|gray|grey|navy|silver|purple|pink)\b", re.I)
PAT_JS_COLOR = re.compile(r"""["'`][^"'`\n]*?(#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3,4}\b|(?:rgba?|hsla?)\([^)]*\))""")
# JS の色名は、色を渡す所（style の値・setProperty・Leaflet の color / fillColor・テンプレートの中の CSS）だけを見る
# （文の中の英単語 Red Sea などを拾わないため）
PAT_JS_COLOR_NAME = re.compile(
    r"""(?:\.style\.\w+\s*=\s*|setProperty\(\s*['"][\w-]+['"]\s*,\s*|"""
    r"""\b(?:color|fillColor|background(?:-color|Color)?|fill|stroke|border(?:-\w+|Color)?|outline(?:-color|Color)?)\s*:\s*)"""
    r"""['"`]?\s*((?:white|black|red|blue|green|yellow|orange|gray|grey|navy|silver|purple|pink)\b)""", re.I)
# 地図の色（設計書 §4 の10色の外）：CSS の規則の選択子で名指しする
# hub.css のハブの地図の陸と海岸（PR 2）・hormuz.css の CARTO に戻したときだけ出る海と国の名前（J1 で戻す道を残す）
CSS_COLOR_ALLOWED = {("hub.css", ".hub-map-land"), ("hormuz.css", ".map-label"),
                     ("hormuz.css", ".map-label--country"), ("hormuz.css", ".map-label--sea")}
# /hormuz/ の JS で、地図を CARTO に戻したとき（BASEMAP === 'carto'）だけ使う国の面・海岸・川の色
JS_MAP_CARTO_COLORS = {"#2a4a6a", "#1e3a7a", "#1e3d28", "#2e5a3a", "#3b82f6", "#0a1b33", "#60a5fa"}


def _emoji_hits(text: str, allowed: set[str]) -> list[str]:
    return [c for c in PAT_EMOJI_ANY.findall(text) if c not in allowed]


def check_emoji(news: dict | None, log) -> None:
    """表示される文の中の絵文字（頭以外も）と、その日に足したデータの絵文字（WARN）。

    頭の絵文字は check_categories() が NG で止める。ここは文の中・固定の部分・ほかのページまで広く見る。
    - docs/ の全ページの、表示される文（<script>・<style>・コメントを除く）と title・alt・aria-label
    - news_data.json（latest・osint）と update_log.json のうち、origin/main との分かれ目（merge-base）に無い項目
      （commit の後に流しても拾える。origin/main が無いときは直前のコミットと、git で比べられないときは
      latest・osint の先頭と update_log の先頭）
    過去のデータの絵文字は書き換えず、表示のときに読み替える決まり（設計書 §6）なので、古い項目は見ない。
    /hormuz/ の JS にある絵文字は、その読み替えの表なので見ない。
    """
    pages = []
    for path in sorted((ROOT / "docs").rglob("*.html")):
        rel = path.relative_to(ROOT / "docs").as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            warn(f"docs/{rel} を読めません（絵文字の検査）")
            continue
        bi = text.find("<body")
        head, body = (text[:bi], text[bi:]) if bi >= 0 else ("", text)
        body = re.sub(r"<script\b[^>]*>.*?</script\b[^>]*>|<style\b[^>]*>.*?</style\b[^>]*>|<!--.*?-->", "", body, flags=re.S | re.I)
        shown = re.sub(r"<[^>]+>", " ", body) + " ".join(re.findall(r'\s(?:title|alt|aria-label)="([^"]*)"', body))
        shown += " ".join(re.findall(r"<title>(.*?)</title>", head, re.S))
        hits = _emoji_hits(shown, EMOJI_ALLOWED | EMOJI_ALLOWED_PAGE.get(rel, set()))
        if hits:
            pages.append(f"{rel} {len(hits)}個（{''.join(sorted(set(hits))[:6])}）")
    if pages:
        warn(f"表示される文に絵文字があります: {'・'.join(pages[:5])}。語か、アイコン（docs/assets/icons/icons.svg）で書く。"
             "残してよいのは 🅐〜🅓・✕・★・✦ と矢印・▶◀◈ だけ（スキル site-design「アイコン」）")
    else:
        ok("全ページの表示される文に絵文字なし（🅐〜🅓・✕・★・✦・矢印・/corrections/ の引用を除く）")

    # その日に足したデータ。origin/main との分かれ目に無い項目を新しい項目とみなす
    # （直前のコミットと比べると、commit の後に流したとき新しい項目が 0件になる）
    import subprocess
    try:
        r = subprocess.run(["git", "merge-base", "HEAD", "origin/main"], cwd=ROOT, capture_output=True, timeout=20)
        base = r.stdout.decode("utf-8").strip() if r.returncode == 0 else ""
    except Exception:  # git が無いなど
        base = ""
    base = base or "HEAD"
    def at_head(rel: str):
        try:
            r = subprocess.run(["git", "show", f"{base}:{rel}"], cwd=ROOT, capture_output=True, timeout=20)
            return json.loads(r.stdout.decode("utf-8")) if r.returncode == 0 else None
        except Exception:  # git が無い・壊れた JSON など
            return None
    new = []
    if isinstance(news, dict):
        prev = at_head("docs/data/news_data.json")
        for key in ("latest", "osint"):
            items = [x for x in news.get(key) or [] if isinstance(x, dict)]
            if isinstance(prev, dict):
                seen = {x.get("id") for x in prev.get(key) or [] if isinstance(x, dict)}
                items = [x for x in items if x.get("id") not in seen]
            else:
                items = items[:1]
            new += [(f"news_data.json {key} / {x.get('id', '?')}", x) for x in items]
    if isinstance(log, list):
        prev = at_head("docs/data/update_log.json")
        items = [x for x in log if isinstance(x, dict)]
        if isinstance(prev, list):
            seen = {json.dumps(x, ensure_ascii=False, sort_keys=True) for x in prev}
            items = [x for x in items if json.dumps(x, ensure_ascii=False, sort_keys=True) not in seen]
        else:
            items = items[:1]
        new += [(f"update_log.json {x.get('date', '?')}", x) for x in items]
    bad = []
    for label, item in new:
        text = " ".join(v for k, v in item.items() if k not in ("id", "url") and isinstance(v, str))
        hits = _emoji_hits(text, EMOJI_ALLOWED)
        if hits:
            bad.append(f"{label}（{''.join(sorted(set(hits))[:6])}）")
    if bad:
        warn(f"その日に足したデータに絵文字があります: {'・'.join(bad[:5])}。分類は label の語で、国は国名で書く"
             "（daily-site-update「分類の札」）")
    else:
        ok(f"その日に足したデータに絵文字なし（news_data.json・update_log.json の新しい項目 {len(new)}件・比べた相手 {base[:7]}）")


def check_colors() -> None:
    """トークン外の色の直書き（WARN）。色は docs/assets/css/tokens.css の変数だけを使う（スキル site-design「色」）。

    - docs/assets/css/*.css（tokens.css を除く）。地図の色は CSS_COLOR_ALLOWED で規則ごとに名指し
    - docs/ の全ページの <style>・style=""・fill・stroke などの属性（<meta name="theme-color"> は CSS 変数を使えないので見ない）
    - docs/ の全ページの JS と docs/assets/js/*.js の文字列の中の色。/hormuz/ の CARTO 用の色（JS_MAP_CARTO_COLORS）は除く
    Leaflet 本体（docs/assets/vendor/）は見ない。日次は CSS に触らないが、修正の PR で古い色が戻るのを止める。
    """
    def css_hits(css: str) -> list[tuple[str, str]]:
        """(選択子, 色) の組を返す。値の側だけを見る（.t-blue のようなクラス名は色に数えない）"""
        out = []
        css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
        for sel, decls in re.findall(r"([^{}]*)\{([^{}]*)\}", css):  # @media の中も、内側の規則だけ拾える
            for val in re.findall(r":([^;{}]*)", decls):
                val = re.sub(r"var\([^)]*\)|url\([^)]*\)", "", val)
                out += [(sel.strip(), c) for c in PAT_COLOR.findall(val) + PAT_COLOR_NAME.findall(val)]
        return out

    bad = []
    n_css = 0
    for path in sorted((ROOT / "docs" / "assets" / "css").glob("*.css")):
        if path.name == "tokens.css":
            continue
        n_css += 1
        for sel, c in css_hits(path.read_text(encoding="utf-8")):
            if any((path.name, s.strip()) in CSS_COLOR_ALLOWED for s in sel.split(",")):
                continue
            bad.append(f"{path.name} {sel[-30:]} {c}")
    n_pages = 0
    for path in sorted((ROOT / "docs").rglob("*.html")):
        rel = path.relative_to(ROOT / "docs").as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue  # 読めないことは check_emoji() が知らせる
        n_pages += 1
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        for st in re.findall(r"<style\b[^>]*>(.*?)</style\b[^>]*>", text, flags=re.S | re.I):
            bad += [f"{rel} <style> {sel[-30:]} {c}" for sel, c in css_hits(st)]
        markup = re.sub(r"<script\b[^>]*>.*?</script\b[^>]*>", "", text, flags=re.S | re.I)
        for name, val in re.findall(r'\s(style|fill|stroke|color|stop-color|bgcolor)="([^"]*)"', markup):
            found = [c for _, c in css_hits("x{" + val + "}")] if name == "style" else PAT_COLOR.findall(val) + PAT_COLOR_NAME.findall(val)
            bad += [f"{rel} {name}=\"{c}\"" for c in found]
        js = "".join(re.findall(r"<script\b[^>]*>(.*?)</script\b[^>]*>", text, flags=re.S | re.I))
        allowed = JS_MAP_CARTO_COLORS if rel == "hormuz/index.html" else set()
        bad += [f"{rel} JS {c}" for c in PAT_JS_COLOR.findall(js) if c.lower() not in allowed]
        bad += [f"{rel} JS {c}" for c in PAT_JS_COLOR_NAME.findall(js)]
    for path in sorted((ROOT / "docs" / "assets" / "js").glob("*.js")):
        js = path.read_text(encoding="utf-8")
        bad += [f"assets/js/{path.name} {c}" for c in PAT_JS_COLOR.findall(js) + PAT_JS_COLOR_NAME.findall(js)]
    if bad:
        warn(f"トークン外の色の直書きが {len(bad)}か所あります: {'／'.join(bad[:5])}。"
             "色は tokens.css の変数（var(--c-*)・地図は var(--map-*)）で書く（スキル site-design「色」）")
    else:
        ok(f"トークン外の色の直書きなし（CSS {n_css}ファイル・{n_pages}ページの <style>・属性・JS。地図の色の例外を除く）")


def check_estimate_labels(html: str) -> None:
    """推定のラベル（②' PR D・2026-10-09 追加）。日次更新で消えていないかを見る。

    「AI推定」＝生成 AI が出した値（.label-ai）、「推定」＝統計などからの試算（.label-estimate）。
    シナリオの見出しは日次が名称と矢印を書き換える場所なので、直後のラベルが落ちやすい。
    """
    bad = []
    for k in "ABCD":
        if not re.search(rf'<span class="sc-tag" id="sc-tag-{k}">.*?</span></span>'
                         r'<span class="label-ai sc-pct-label">AI推定</span>', html):
            bad.append(f"シナリオ{k} の確率の横の「AI推定」")
    if not re.search(r'データ監視ダッシュボード<span class="label-ai sc-h2-label">AI推定を含む</span></h2>', html):
        bad.append("ダッシュボードの見出しの「AI推定を含む」")
    # 個数ではなく場所ごとに見る（ほかの場所に「推定」を足した日に NG にしない）
    if not re.search(r'<span class="jf-th-sub">[^\n]*?<span class="label-estimate">推定</span></span>', html):
        bad.append("日本向けフローの列見出しの「推定」")
    if not re.search(r'<div class="jf-col jf-note">\s*<span class="label-estimate">推定</span>', html):
        bad.append("日本向けフローの注記の「推定」")
    if bad:
        ng(f"推定のラベルが型と違います: {'・'.join(bad)}")
    else:
        ok("推定のラベルあり（確率4枚・ダッシュボードの見出し・日本向けフロー2か所）")


def check_crisis_day(html: str, base: str) -> None:
    """本体ヘッダーの「危機N日目」の静的な数字が、基準日から計算した日数と同じか。

    表示は JS が毎回計算して上書きするので通常は正しく見えるが、HTML に置いた数字は
    JS が動かないときの予備として残る。2026-10-04 に 217 のまま（実際は 219）残っているのが
    見つかったため、日次更新が毎回書き換える。表示に出るのは JS が動かないときだけなので WARN にとどめる。
    """
    m = PAT_CRISIS_DAY.search(html)
    if not m:
        warn("本体ヘッダーの「危機N日目」（id=\"blockade-days\"）を検出できませんでした")
        return
    got = int(m.group(1))
    want = (date.fromisoformat(base) - CRISIS_START).days + 1
    if got != want:
        warn(f"本体ヘッダーの「危機N日目」の静的な数字が {got} です。基準日 {base} は {want}日目（2/28 を1日目として計算）")
    else:
        ok(f"本体ヘッダーの「危機N日目」の静的な数字 {got}（基準日 {base}）")


def check_selfhosted_assets(html: str) -> None:
    """自サイトから配信している資産（①' 外部依存の自前化・2026-10-09 追加）。

    Leaflet を unpkg.com から読む形に戻っていないか。戻ると、/privacy/ 第5章に無い
    外部送信先へ接続することになる（方針ページと実態の食い違い）。
    """
    vendor = "/assets/vendor/leaflet-1.9.4/"
    bad = []
    if re.search(r"unpkg\.com", html):  # ページ内の文字列の有無を見る（URL の検証ではない）
        bad.append("unpkg.com への参照があります")
    for name in ("leaflet.css", "leaflet.js"):
        if f'"{vendor}{name}"' not in html:
            bad.append(f"<head> に {vendor}{name} がありません")
        if not (ROOT / "docs" / "assets" / "vendor" / "leaflet-1.9.4" / name).is_file():
            bad.append(f"docs{vendor}{name} がありません")
    if bad:
        ng(f"Leaflet の読み込み元が型と違います: {'・'.join(bad)}。自サイト（{vendor}）から読む")
    else:
        ok("Leaflet は自サイトから読み込み（unpkg.com への参照なし）")

    # フォント（2026-10-10 追加）。Google Fonts へ戻ると、/privacy/ 第5章に無い送信先へ接続することになる。
    # /hormuz/ のほか、記事（docs/hormuz/articles/ の下の index.html）と記事の雛形も見る（日次は触らないが、新しい記事が古い雛形から作られると戻る）。
    # 2026-10-20：課題46 D3 PR 3・PR 4 で Noto Sans JP から BIZ UDPゴシックに替えたので、見る CSS を替えた（tools/site-redesign-design.md §5-2）
    fonts_dir = ROOT / "docs" / "assets" / "fonts" / "biz-udpgothic"
    fonts_css = "/assets/fonts/biz-udpgothic/biz-udpgothic.css"
    pat_gfonts = re.compile(r"fonts\.(?:googleapis|gstatic)\.com")  # 文字列の有無を見る（URL の検証ではない）
    bad = []
    pages = [("hormuz/index.html", html)]
    for path in sorted((ROOT / "docs" / "hormuz" / "articles").glob("**/index.html")) + [ROOT / "tools" / "article-template.html"]:
        try:
            pages.append((path.relative_to(ROOT).as_posix(), path.read_text(encoding="utf-8")))
        except (OSError, UnicodeDecodeError):
            bad.append(f"{path.relative_to(ROOT).as_posix()} を読めません")
    for name, text in pages:
        if pat_gfonts.search(text):
            bad.append(f"{name} に Google Fonts への参照があります")
        if f'href="{fonts_css}"' not in text:
            bad.append(f"{name} の <head> に {fonts_css} がありません")
    if not (fonts_dir / "biz-udpgothic.css").is_file():
        bad.append(f"docs{fonts_css} がありません")
    else:
        css = (fonts_dir / "biz-udpgothic.css").read_text(encoding="utf-8")
        missing = [f for f in set(re.findall(r"url\(([^)]+\.woff2)\)", css)) if not (fonts_dir / f).is_file()]
        if missing:
            bad.append(f"CSS が指す woff2 が {len(missing)} 個ありません（例：{sorted(missing)[0]}）")
    if bad:
        ng(f"フォントの読み込み元が型と違います: {'・'.join(bad[:6])}。自サイト（{fonts_css}）から読む")
    else:
        ok(f"フォントは自サイトから読み込み（{len(pages)} ファイル・Google Fonts への参照なし）")


def check_upcoming(html: str) -> None:
    """今後の予定日（docs/data/upcoming.json）。/hormuz/ の30秒カラム「次の焦点」の直下に JS が出す。

    2026-10-01 に休止した COUNTDOWN は、期限を JS に直書きし、切れた後の扱いも検査も無かったために
    古い表示が4か月残った。予定日はデータで持ち、ここで形と出典を確かめる（tools/display-unify-design.md §3-1）。
    過ぎた項目は画面に出ないので、残っていても WARN にとどめる。
    """
    data = load_json(UPCOMING)
    if data is None:
        return
    items = data.get("items") if isinstance(data, dict) else None
    if not isinstance(items, list):
        ng("upcoming.json に items（配列）がありません")
        return
    today = date.fromisoformat(today_jst())
    bad = 0
    active = 0
    for i, it in enumerate(items):
        label = f"upcoming.json items[{i}]"
        if not isinstance(it, dict):
            ng(f"{label} がオブジェクトではありません")
            bad += 1
            continue
        label += f"「{it.get('title', '')}」"
        missing = [k for k in UPCOMING_REQUIRED if not str(it.get(k, "")).strip()]
        if missing:
            ng(f"{label} に必須項目がありません: {', '.join(missing)}")
            bad += 1
        if it.get("kind") not in ("schedule", "deadline"):
            ng(f"{label} の kind は schedule か deadline にしてください: {it.get('kind')!r}")
            bad += 1
        if str(it.get("url", "")).strip() and not str(it["url"]).startswith("https://"):
            ng(f"{label} の url が https:// で始まっていません（画面でリンクになりません）")
            bad += 1
        try:
            d = date.fromisoformat(str(it.get("date", "")))
        except ValueError:
            ng(f"{label} の date を YYYY-MM-DD として読めません: {it.get('date')!r}")
            bad += 1
            continue
        if d >= today:
            active += 1
        elif (today - d).days >= 7:
            warn(f"{label} は {d} に過ぎています（画面には出ていません）。upcoming.json から消してください")
    if not bad:
        ok(f"今後の予定日 {len(items)}件（うち今日以降 {active}件）")

    # 「次の焦点」に未来の日付（M/D）が書いてあるのに予定日が0件なら、載せ忘れかもしれない
    m = PAT_GLANCE_NEXT.search(html)
    if not m:
        warn("30秒カラムの「次の焦点」を検出できませんでした（予定日の載せ忘れの確認を省きました）")
        return
    future = []
    for mo, dd in re.findall(r"(?<![\d/])(\d{1,2})/(\d{1,2})(?![\d/])", m.group(1)):
        try:
            d = date(today.year, int(mo), int(dd))
        except ValueError:
            continue
        # 年末に翌年の日付（12月に書いた「1/10」など）を過去と読まないよう、過ぎた月日は翌年でも見る
        # （120日以内に来るものだけ。前日・先週の日付を翌年の予定と読まないため）
        if d <= today:
            try:
                d2 = date(today.year + 1, int(mo), int(dd))
            except ValueError:
                continue
            if (d2 - today).days > 120:
                continue
        future.append(f"{int(mo)}/{int(dd)}")
    if future and not active:
        warn("「次の焦点」に先の日付（" + "・".join(future) + "）がありますが、今後の予定日（upcoming.json）は0件です。"
             "出典つきで日付が確定した予定なら1件足す（載せない判断ならそのままでよい）")


def check_glossary() -> None:
    """用語集ページ（docs/glossary/index.html）が docs/data/glossary.json と一致しているか。

    ページは tools/build_glossary.py が JSON から書き出す。JSON だけ直して書き出しを忘れると、
    ツールチップ（JSON を読む）と用語集ページ（HTML）で説明が食い違う。日次更新は用語集を触らないので
    普段は通るだけの検査。
    """
    import os
    import subprocess

    script = ROOT / "tools" / "build_glossary.py"
    if not script.is_file():
        warn("tools/build_glossary.py が見つからないため、用語集の検査を省きました")
        return
    res = subprocess.run([sys.executable, str(script), "--check"],
                         capture_output=True, text=True, encoding="utf-8", errors="replace",
                         env={**os.environ, "PYTHONIOENCODING": "utf-8"})  # Windows の既定（cp932）で出力させない
    lines = [l.strip() for l in (res.stdout or "").splitlines() if l.strip()]
    if res.returncode == 0:
        ok(lines[-1].replace("OK", "", 1).strip() if lines else "用語集ページは glossary.json と一致")
    else:
        for l in lines or ["用語集の検査が失敗しました（出力なし）"]:
            ng("用語集：" + l.replace("NG", "", 1).strip())


def main() -> int:
    ap = argparse.ArgumentParser(description="日次更新の機械検証（読み取り専用）")
    ap.add_argument("--date", help="基準日 YYYY-MM-DD。省略時は news_data.json の updated")
    ap.add_argument("--check-urls", action="store_true", help="latest の URL 死活も確認する")
    args = ap.parse_args()

    news = load_json(NEWS)
    log = load_json(LOG)
    tl = load_json(TIMELINE)
    try:
        html = HTML.read_text(encoding="utf-8")
    except FileNotFoundError:
        ng("docs/hormuz/index.html が見つかりません")
        html = ""

    if news is None or not html:
        report()
        return 1
    ok("JSON 3ファイルの読み込み")

    # 基準日を決める
    if args.date:
        base = args.date
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", base):
            print("--date は YYYY-MM-DD で指定してください", file=sys.stderr)
            return 1
        src = "--date 指定"
    else:
        m = PAT_UPDATED.search(news.get("updated", ""))
        if not m:
            ng(f"news_data.json の updated を解釈できません: {news.get('updated')!r}")
            report()
            return 1
        base = ymd(*m.groups()[:3])
        src = "news_data.json の updated"

    print(f"基準日: {base}（{src}）／実測の今日: {today_jst()} JST\n")

    # 基準日そのものの妥当性 → そのうえでファイル間の整合
    check_base_date(base)
    found = collect_dates(html, news)
    for name, val in found.items():
        if val is None:
            ng(f"{name} の日付を検出できませんでした（構造が変わった可能性）")
        elif val == base:
            ok(f"{name} {val}")
        else:
            ng(f"{name} が基準日と違います: {val}（基準 {base}）")
    check_ticker(html, base)
    check_ticker_comment(html, base)
    check_hub_updated(html, base)
    check_crisis_day(html, base)
    check_scenario_dates(html, base)
    check_state_labels(html)
    check_estimate_labels(html)
    check_selfhosted_assets(html)
    check_upcoming(html)
    check_log_wording(html, base)
    check_route_freshness(html, base)
    check_types(html, base)
    check_unresolved(html)
    check_text_lengths(html)

    check_news(news, base)
    check_categories(html, news)
    check_emoji(news, log)
    check_colors()
    if log is not None:
        check_log(log, base)
    if tl is not None:
        check_timeline(tl, base)
    check_sitemap(tl, base)
    check_data_timeline()
    check_military(base)
    check_oil_flow()
    check_stockpile(html)
    check_column_pills(html)
    check_glossary()
    if args.check_urls:
        print("URL を確認しています…\n")
        check_urls(news)

    report()
    return 1 if errors else 0


def report() -> None:
    for m in oks:
        print(f"  OK   {m}")
    for m in warns:
        print(f"  WARN {m}")
    for m in errors:
        print(f"  NG   {m}")
    print()
    print(f"OK {len(oks)} / WARN {len(warns)} / NG {len(errors)}")
    if errors:
        print("\n公開前に NG を解消すること。")
    elif warns:
        print("\nWARN は内容を確認したうえで判断すること。")
    else:
        print("\n問題なし。")


if __name__ == "__main__":
    sys.exit(main())
