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
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "docs" / "index.html"
NEWS = ROOT / "docs" / "data" / "news_data.json"
LOG = ROOT / "docs" / "data" / "update_log.json"
TIMELINE = ROOT / "docs" / "data" / "archive_timeline.json"

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


def ymd(y, m, d) -> str:
    return f"{int(y):04d}-{int(m):02d}-{int(d):02d}"


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

    print(f"基準日: {base}（{src}）\n")

    # 日付整合
    found = collect_dates(html, news)
    for name, val in found.items():
        if val is None:
            ng(f"{name} の日付を検出できませんでした（構造が変わった可能性）")
        elif val == base:
            ok(f"{name} {val}")
        else:
            ng(f"{name} が基準日と違います: {val}（基準 {base}）")
    check_ticker(html, base)

    check_news(news, base)
    if log is not None:
        check_log(log, base)
    if tl is not None:
        check_timeline(tl, base)
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
