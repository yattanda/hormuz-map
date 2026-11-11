#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ニュースの RSS から、直近◯時間の記事の見出し・媒体・配信時刻・元記事の URL を集める。読み取り専用。

日次更新の情報収集（.claude/skills/daily-site-update/SKILL.md「情報収集」）で、WebSearch と並べて使う。

なぜ要るか（2026-11-12 追加）：
  WebSearch の索引は数時間〜1日遅れることがあり、朝の日次で前日〜当日（日本時間）の記事がほとんど
  出ない日がある（2026-11-12 の日次で 11/11〜12 の記事がほぼ出なかった）。RSS は媒体やニュース集約の
  配信そのものなので、配信から数分で載る。

取得元（どれも公開の RSS。ログインや API キーは要らない）：
  - Google ニュースの検索 RSS（英語・日本語。`when:2d` で直近に絞る）。リンクは Google の転送用 URL なので、
    --resolve（既定）で元記事の URL に戻す
  - Bing ニュースの検索 RSS（リンクの url= に元記事の URL が入っている）
  - 媒体の RSS（Al Jazeera・gCaptain・BBC 中東・Arab News・The National・Splash247・Maritime Executive）。
    語で絞り込む（ホルムズ・イラン・タンカーなど）
  Tehran Times・IRNA・Press TV は直接つながらない（2026-11-12 実測）。Google ニュース経由で拾える

使い方：
    python tools/fetch_news_feeds.py                 # 既定のクエリ（スキルの毎日の検索）・直近36時間
    python tools/fetch_news_feeds.py --hours 24
    python tools/fetch_news_feeds.py --query "Didamar island"   # クエリを足す（複数可）
    python tools/fetch_news_feeds.py --only-query "UKMTO"       # 足したクエリだけ（媒体の RSS も読まない）
    python tools/fetch_news_feeds.py --no-resolve    # Google の転送用 URL のまま（速い）
    python tools/fetch_news_feeds.py --resolve-url "https://news.google.com/rss/articles/…"  # 1件だけ元記事の URL に戻す
    python tools/fetch_news_feeds.py --json

注意：
  - 出るのは見出しと URL だけ。**本文に使う前に、その URL を WebFetch で開いて原文を読む**（スキルの「URL の扱い」）
  - 見出しは媒体の言い方で、事実の確認ではない。UKMTO・原油の終値の裏取りの決まりは変わらない
  - 配信時刻は RSS の pubDate。記事が更新されると新しい時刻になる媒体がある

終了コード：0＝1件以上取れた／2＝どの取得元からも取れなかった
"""
import argparse
import datetime
import email.utils
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "Mozilla/5.0 (compatible; chokepointlab-daily/1.0; +https://chokepointlab.com/contact/)"
BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
JST = datetime.timezone(datetime.timedelta(hours=9))

GOOGLE_RSS = {
    "en": "https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en",
    "ja": "https://news.google.com/rss/search?q={q}&hl=ja&gl=JP&ceid=JP:ja",
}
BING_RSS = "https://www.bing.com/news/search?q={q}&format=rss"

# スキルの「毎日必ず叩く検索クエリ」に合わせる（RSS の検索向けに語を絞った）
DEFAULT_QUERIES = [
    ("ja", "ホルムズ海峡 タンカー"),
    ("ja", "ホルムズ 日本 船舶"),
    ("ja", "原油 WTI ブレント"),
    ("ja", "イラン 米国 攻撃"),
    ("en", "Strait of Hormuz tanker"),
    ("en", "Iran US military"),
    ("en", "Iran Israel strike"),
    ("en", "UKMTO"),
    ("en", "CENTCOM blockade Iran"),
    ("en", "aircraft carrier Iran"),
    ("en", "Houthi Red Sea ship"),
    ("en", "oil prices Brent"),
]
BING_QUERIES = ["Strait of Hormuz", "Iran tanker"]

OUTLET_FEEDS = [
    ("Al Jazeera", "https://www.aljazeera.com/xml/rss/all.xml"),
    ("gCaptain", "https://gcaptain.com/feed/"),
    ("BBC（中東）", "https://feeds.bbci.co.uk/news/world/middle_east/rss.xml"),
    ("Arab News", "https://www.arabnews.com/rss.xml"),
    ("The National", "https://www.thenationalnews.com/arc/outboundfeeds/rss/?outputType=xml"),
    ("Splash247", "https://splash247.com/feed/"),
    ("Maritime Executive", "https://maritime-executive.com/articles.rss"),
]
OUTLET_KEYWORDS = re.compile(
    r"hormuz|iran|tanker|ukmto|centcom|houthi|red sea|gulf of oman|persian gulf|fujairah|"
    r"bab el-mandeb|crude|brent|opec|strait|blockade|irgc|tehran|ホルムズ|イラン",
    re.I)


def http_get(url, data=None, headers=None, timeout=20):
    h = {"User-Agent": USER_AGENT}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as res:
        return res.read().decode("utf-8", "replace")


def _tag(block, name):
    m = re.search(r"<{0}[^>]*>(.*?)</{0}>".format(name), block, re.S)
    if not m:
        return ""
    text = m.group(1).strip()
    if text.startswith("<![CDATA["):
        text = text[9:-3]
    return html.unescape(text).strip()


def parse_rss(xml):
    """RSS 2.0 の item を (title, link, pubDate(UTC), source) にする。"""
    items = []
    for block in re.findall(r"<item>(.*?)</item>", xml, re.S):
        title, link, pub = _tag(block, "title"), _tag(block, "link"), _tag(block, "pubDate")
        if not pub:
            pub = _tag(block, "dc:date")
        try:
            dt = email.utils.parsedate_to_datetime(pub)
        except (TypeError, ValueError):
            try:
                dt = datetime.datetime.fromisoformat(pub.replace("Z", "+00:00"))
            except ValueError:
                continue
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=datetime.timezone.utc)
        items.append({"title": title, "link": link, "published": dt.astimezone(datetime.timezone.utc),
                      "source": _tag(block, "source")})
    return items


def google_news(query, lang="en", window="2d"):
    q = urllib.parse.quote_plus("{} when:{}".format(query, window))
    items = parse_rss(http_get(GOOGLE_RSS[lang].format(q=q)))
    for it in items:
        # Google の見出しは「見出し - 媒体名」。媒体名を外す
        if it["source"] and it["title"].endswith(" - " + it["source"]):
            it["title"] = it["title"][: -len(it["source"]) - 3]
        it["via"] = "Google ニュース"
    return items


def bing_news(query):
    items = parse_rss(http_get(BING_RSS.format(q=urllib.parse.quote_plus(query))))
    for it in items:
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(it["link"]).query)
        if qs.get("url"):
            it["link"] = qs["url"][0]
            it["resolved"] = True
        it["source"] = it["source"] or urllib.parse.urlparse(it["link"]).netloc.replace("www.", "")
        it["via"] = "Bing ニュース"
    return items


def outlet_feed(name, url):
    # Arab News はブラウザ風の長い UA だと 403、短い UA なら通る（2026-11-12 実測）
    items = [it for it in parse_rss(http_get(url, headers={"User-Agent": "Mozilla/5.0"}))
             if OUTLET_KEYWORDS.search(it["title"])]
    for it in items:
        it["source"], it["via"], it["resolved"] = name, "媒体の RSS", True
    return items


def resolve_google(link, lang="en"):
    """Google ニュースの転送用 URL（news.google.com/rss/articles/…）を元記事の URL に戻す。
    記事ページの data-n-a-sg・data-n-a-ts を、Google ニュースのページ自身が使う batchexecute に渡す。"""
    page = http_get(link, headers={"User-Agent": BROWSER_UA})
    gid = re.search(r'data-n-a-id="([^"]+)"', page)
    ts = re.search(r'data-n-a-ts="([^"]+)"', page)
    sg = re.search(r'data-n-a-sg="([^"]+)"', page)
    if not (gid and ts and sg):
        raise ValueError("転送ページに記事の識別子が無い")
    locale = "US:en" if lang == "en" else "JP:ja"
    inner = ["garturlreq", [["X", "X", ["X", "X"], None, None, 1, 1, locale, None, 1, None, None, None, None, None, 0, 1],
                            "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0],
             gid.group(1), int(ts.group(1)), sg.group(1)]
    body = "f.req=" + urllib.parse.quote(json.dumps([[["Fbv4je", json.dumps(inner), None, "generic"]]]))
    res = http_get("https://news.google.com/_/DotsSplashUi/data/batchexecute", data=body.encode(),
                   headers={"User-Agent": BROWSER_UA,
                            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"})
    payload = json.loads(res.split("\n", 2)[2])
    return json.loads(payload[0][2])[1]


def norm_title(title):
    return re.sub(r"\W+", "", title.lower())[:80]


def collect(queries, hours, use_bing=True, use_outlets=True, resolve=True, max_resolve=60, errors=None, limit=None):
    """クエリと取得元を回して、直近 hours 時間の記事を新しい順に返す（見出しで重複を除く）。"""
    errors = errors if errors is not None else []
    since = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=hours)
    window = "{}d".format(max(1, -(-hours // 24)))
    found = []
    for lang, q in queries:
        try:
            for it in google_news(q, lang, window):
                it.update(query=q, lang=lang)
                found.append(it)
        except (urllib.error.URLError, OSError, ValueError) as e:
            errors.append("Google ニュース「{}」：{}".format(q, e))
    if use_bing:
        for q in BING_QUERIES:
            try:
                for it in bing_news(q):
                    it.update(query=q, lang="en")
                    found.append(it)
            except (urllib.error.URLError, OSError, ValueError) as e:
                errors.append("Bing ニュース「{}」：{}".format(q, e))
    if use_outlets:
        for name, url in OUTLET_FEEDS:
            try:
                for it in outlet_feed(name, url):
                    it.update(query="（媒体の RSS）", lang="en")
                    found.append(it)
            except (urllib.error.URLError, OSError, ValueError) as e:
                errors.append("{} の RSS：{}".format(name, e))

    seen, out = set(), []
    for it in sorted(found, key=lambda x: x["published"], reverse=True):
        if it["published"] < since:
            continue
        key = norm_title(it["title"])
        if key in seen:
            continue
        seen.add(key)
        out.append(it)
    if limit:
        out = out[:limit]

    if resolve:
        done = 0
        for it in out:
            if it.get("resolved") or "news.google.com" not in it["link"]:
                continue
            if done >= max_resolve:
                break
            try:
                it["link"] = resolve_google(it["link"], it.get("lang", "en"))
                it["resolved"] = True
            except (urllib.error.URLError, OSError, ValueError, KeyError, IndexError, json.JSONDecodeError) as e:
                it["resolve_error"] = str(e)
            done += 1
            time.sleep(0.3)
    return out


def main():
    ap = argparse.ArgumentParser(description="ニュースの RSS から直近の記事を集める（読み取り専用）")
    ap.add_argument("--hours", type=int, default=36, help="直近◯時間（既定 36）")
    ap.add_argument("--query", action="append", default=[], help="Google ニュースのクエリを足す（英語）。複数可")
    ap.add_argument("--query-ja", action="append", default=[], help="日本語のクエリを足す。複数可")
    ap.add_argument("--only-query", action="append", default=[],
                    help="このクエリだけで探す（既定のクエリ・Bing・媒体の RSS を読まない）。複数可")
    ap.add_argument("--no-resolve", action="store_true", help="Google の転送用 URL を元記事に戻さない")
    ap.add_argument("--max-resolve", type=int, default=150, help="元記事に戻す件数の上限（既定 150）")
    ap.add_argument("--limit", type=int, default=150, help="出す件数の上限（新しい順。既定 150）")
    ap.add_argument("--resolve-url", help="Google の転送用 URL を1件だけ元記事の URL に戻して出す")
    ap.add_argument("--json", action="store_true", help="JSON で出す")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    if args.resolve_url:
        try:
            print(resolve_google(args.resolve_url))
            return 0
        except (urllib.error.URLError, OSError, ValueError, KeyError, IndexError, json.JSONDecodeError) as e:
            print("元記事の URL に戻せなかった：{}".format(e), file=sys.stderr)
            return 2

    if args.only_query:
        queries = [("en", q) for q in args.only_query]
        use_bing = use_outlets = False
    else:
        queries = DEFAULT_QUERIES + [("en", q) for q in args.query] + [("ja", q) for q in args.query_ja]
        use_bing = use_outlets = True

    errors = []
    items = collect(queries, args.hours, use_bing, use_outlets, not args.no_resolve, args.max_resolve, errors,
                    limit=args.limit)

    if args.json:
        print(json.dumps({"items": [dict(it, published=it["published"].astimezone(JST).isoformat()) for it in items],
                          "errors": errors}, ensure_ascii=False, indent=2))
    else:
        now = datetime.datetime.now(JST).strftime("%Y-%m-%d %H:%M JST")
        print("取得：{}　直近{}時間　{}件（見出しで重複を除いた数）".format(now, args.hours, len(items)))
        print("本文に使う前に、URL を WebFetch で開いて原文を読む。見出しは媒体の言い方で、事実の確認ではない\n")
        for it in items:
            t = it["published"].astimezone(JST).strftime("%m/%d %H:%M")
            mark = "" if it.get("resolved") or "news.google.com" not in it["link"] else "（Google の転送用 URL）"
            print("{} JST｜{}｜{}".format(t, it["source"] or "媒体名なし", it["title"]))
            print("    {}{}　［{}：{}］".format(it["link"], mark, it["via"], it["query"]))
        for e in errors:
            print("取得できなかった：" + e, file=sys.stderr)
    return 0 if items else 2


if __name__ == "__main__":
    sys.exit(main())
