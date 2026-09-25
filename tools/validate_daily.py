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
      2026-09-15 に実際に発生した。見出しの日付一致（NG）とは別に、各行本文中の
      M/D 日付表記の鮮度を WARN として見る（本文の内容自体は機械判定できないため）
    - hormuz-data- の経緯（data/context.json の timeline）は手動追記で、日次手順に
      入っていなかったため 9/3 で止まり、ダッシュボードに ⚠ が出た（2026-09-19 に発覚）。
      最新日が実測の今日から 5日を超えたら WARN を出す（別リポジトリのため NG にはしない）。
      ローカルの ../hormuz-data- を優先し、無ければ公開 URL を取得する。どちらも失敗したら WARN
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
HTML = ROOT / "docs" / "index.html"
NEWS = ROOT / "docs" / "data" / "news_data.json"
LOG = ROOT / "docs" / "data" / "update_log.json"
TIMELINE = ROOT / "docs" / "data" / "archive_timeline.json"
SITEMAP = ROOT / "docs" / "sitemap.xml"

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
PAT_HEADER = re.compile(r'badge-date">\s*📅\s*(\d{4})年(\d{1,2})月(\d{1,2})日\s+(\d{1,2}:\d{2})\s*JST')
PAT_TICKER = re.compile(r'📅\s*(\d{1,2})/(\d{1,2})\s+(\d{1,2}:\d{2})\s*更新')
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
STALE_ROUTE_DAYS = 10  # この日数より新しい日付表記が本文中に無ければ WARN

# sitemap.xml の lastmod（ホスト名は問わない。パスで特定する）
PAT_SITEMAP_TOP = re.compile(r'<loc>https?://[^/<]+/</loc>\s*<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>')
PAT_SITEMAP_ARCHIVE = re.compile(r'<loc>https?://[^/<]+/archive/</loc>\s*<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>')

# hormuz-data- の経緯（Gemini に渡す確定した事実）。ローカルはリポジトリの親ディレクトリ基準
DATA_CONTEXT_LOCAL = ROOT.parent / "hormuz-data-" / "data" / "context.json"
DATA_CONTEXT_URL = "https://yattanda.github.io/hormuz-data-/data/context.json"
# ダッシュボードの ⚠（context.json の timeline_stale_after_days = 7）より手前で気づくための閾値
DATA_TIMELINE_WARN_DAYS = 5


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
        warn("index.html の速報バナー「📅 M/D HH:MM 更新」を検出できませんでした（構造が変わった可能性）")
        return
    want = (int(base[5:7]), int(base[8:10]))
    bad = [f"{mm}/{dd}" for mm, dd, _ in hits if (int(mm), int(dd)) != want]
    if bad:
        ng(f"index.html の速報バナーの日付が基準日と違います: {', '.join(bad)}（基準 {want[0]}/{want[1]}）")
    else:
        ok(f"速報バナーの日付 {want[0]}/{want[1]}（{len(hits)}箇所）")


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

        newest: date | None = None
        for mm, dd in PAT_ROUTE_ROW_MD.findall(text):
            try:
                d = date(base_date.year, int(mm), int(dd))
            except ValueError:
                continue
            if d > base_date + timedelta(days=1):
                continue  # 表記ゆれ等で未来日になったものは日付として扱わない
            if newest is None or d > newest:
                newest = d

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
            ok(f"全ルート現況サマリー / ルート{route} 行の鮮度（本文中の最新日付表記 {newest.isoformat()}、{age}日前）")

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
    else:
        ng(f"update_log.json の先頭が基準日ではありません: {head}（基準 {base}）")


def check_timeline(tl, base: str) -> None:
    entries = (tl or {}).get("entries")
    if not isinstance(entries, list) or not entries:
        ng("archive_timeline.json の entries が空か、配列ではありません")
        return
    last = entries[-1].get("date", "")
    if last == base:
        ok(f"archive_timeline.json の末尾が基準日（{last}）")
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
    - `/` は日次更新のたびに変わるので基準日と一致すること（NG）
    - `/archive/` は archive_timeline に追記した日だけ変わるので、末尾の日付より古くないこと（NG）
    """
    try:
        xml = SITEMAP.read_text(encoding="utf-8")
    except FileNotFoundError:
        ng("docs/sitemap.xml が見つかりません")
        return

    m = PAT_SITEMAP_TOP.search(xml)
    if not m:
        ng("sitemap.xml の / の lastmod を検出できませんでした（構造が変わった可能性）")
    elif m.group(1) == base:
        ok(f"sitemap.xml / の lastmod {m.group(1)}")
    else:
        ng(f"sitemap.xml / の lastmod が基準日と違います: {m.group(1)}（基準 {base}）")

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
    30秒カラム（主な動き3件を含む）と速報インシデントの一覧が対象。見た目は壊れないので WARN にとどめる。"""
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
    m = PAT_INCIDENT_LIST.search(html)
    if m:
        n_style = m.group(0).count('style="')
        if n_style:
            warn(f"速報インシデントの一覧にインライン style が {n_style}箇所あります（型は li.incident-item＋モディファイア）")
        else:
            ok("速報インシデントの一覧にインライン style なし")


# ── main ────────────────────────────────────────────────────
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
        ng("docs/index.html が見つかりません")
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
    check_route_freshness(html, base)
    check_types(html, base)

    check_news(news, base)
    if log is not None:
        check_log(log, base)
    if tl is not None:
        check_timeline(tl, base)
    check_sitemap(tl, base)
    check_data_timeline()
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
