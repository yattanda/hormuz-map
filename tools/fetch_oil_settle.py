#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ブレント・WTI の限月ごとの終値（清算値）を、市場データから読む。読み取り専用。

日次更新の原油の終値の裏取り（.claude/skills/daily-site-update/SKILL.md「二次情報の裏取り」・
tools/daily-verify-prompts.md の V2）で、報道とは独立した2つ目の出典として使う。

取得元は Yahoo Finance のチャート用 JSON（取引所 NYMEX のデータ）。
  - WTI：NYMEX の WTI 先物（CL）
  - ブレント：NYMEX の Brent Last Day Financial（BZ）。ICE ブレントの清算値で決済される金融先物で、
    日々の終値は ICE ブレントの清算値と同じ値になる
  2026-10-27 に、2出典で確定済みの 10/21・10/22・10/23 の終値（ブレント12月物 108.82・113.17・116.72、
  WTI12月物 97.15・99.47・103.27）と全件一致することを確かめた。

注意（実測で分かったこと）：
  - 取引中の日（米国時間）の足は、清算後も夜間の取引で値が動く。確定するのは Yahoo の取引日が
    切り替わる米国東部 0時（日本時間 13時・夏時間／14時・冬時間）以降。**朝の日次では、前日（米国時間）の終値は
    多くの場合「未確定」と出る。**その日の終値は報道2出典で確かめ、このスクリプトは
    それより前の日の終値（前回の更新で据え置いた終値の裏取り）に使う
  - 期近をつなげた銘柄（CL=F・BZ=F）は限月が途中で切り替わる（10/26 に BZ=F は既に1月物だった）。
    サイトの限月と合わせるため、必ず限月を指定した銘柄（BZZ26.NYM など）で読む
  - 満期を過ぎた限月は Yahoo から消える（404）。その限月の過去の終値は取れないので、終了コード 2 になる
  - CME の公式サイトは自動取得を利用規約で禁じ、403 を返す。ICE は Cloudflare で拒否される。どちらも使わない
  - 日足の時刻は米国東部の 0時（夏時間は UTC 04:00、冬時間は UTC 05:00）。Yahoo の gmtoffset は**いまの**時差
    だけなので、全部の足に当てると夏時間の終わり（11月第1日曜）の後に、それより前の足が1日前の日付になる
    （2026-11-03 実測：10/30 の 113.43 が「10/29」と出た）。足ごとに米国東部の時差を決める（us_eastern_offset）

使い方：
    python tools/fetch_oil_settle.py                     # 期近とその次の限月、直近7取引日
    python tools/fetch_oil_settle.py --date 2026-10-26   # その取引日の終値だけ
    python tools/fetch_oil_settle.py --month 2026-12     # 限月を指定（ブレント・WTI とも）
    python tools/fetch_oil_settle.py --json

終了コード：0＝取得できた（「未確定」を含む）／2＝取得できなかった（報道の2出典で確かめる）
"""
import argparse
import datetime
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

API_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?{span}&interval=1d"
PAGE_URL = "https://finance.yahoo.com/quote/{symbol}/history/"
USER_AGENT = "Mozilla/5.0 (compatible; chokepointlab-daily/1.0; +https://chokepointlab.com/contact/)"
MONTH_CODES = "FGHJKMNQUVXZ"
PRODUCTS = (("ブレント", "BZ"), ("WTI", "CL"))


def us_eastern_offset(utc_dt):
    """その時刻（UTC）の米国東部の時差。夏時間は3月第2日曜 2時〜11月第1日曜 2時（2007年からの規則）。
    Windows の Python は tzdata が無いと zoneinfo で America/New_York を読めないので、規則を直に書く。"""
    def sunday(year, month, nth):
        day = datetime.date(year, month, 1)
        day += datetime.timedelta(days=(6 - day.weekday()) % 7)
        return day + datetime.timedelta(weeks=nth - 1)
    y = utc_dt.year
    # 切り替わりの時刻（UTC）：3月は 2時 EST＝7時 UTC、11月は 2時 EDT＝6時 UTC
    start = datetime.datetime.combine(sunday(y, 3, 2), datetime.time(7), datetime.timezone.utc)
    end = datetime.datetime.combine(sunday(y, 11, 1), datetime.time(6), datetime.timezone.utc)
    return datetime.timedelta(hours=-4 if start <= utc_dt < end else -5)


def to_eastern_date(ts):
    """Yahoo のタイムスタンプ（秒）を、米国東部の日付にする。"""
    utc_dt = datetime.datetime.fromtimestamp(ts, datetime.timezone.utc)
    return (utc_dt + us_eastern_offset(utc_dt)).date()


def business_days_back(day, n):
    """day から n 営業日（土日のみ除く。祝日は考慮しない）さかのぼった日。"""
    while n > 0:
        day -= datetime.timedelta(days=1)
        if day.weekday() < 5:
            n -= 1
    return day


def last_trade_day(product, year, month):
    """限月の取引最終日の目安（祝日は考慮しない）。

    ブレント：受渡月の2か月前の月の最終営業日（12月物なら10月末）
    WTI：受渡月の前月25日の3営業日前（25日が休日なら、その前の営業日から3営業日前）
    """
    if product == "BZ":
        y, m = (year, month - 2) if month > 2 else (year - 1, month + 10)
        day = datetime.date(y + (m == 12), m % 12 + 1, 1) - datetime.timedelta(days=1)
        while day.weekday() >= 5:
            day -= datetime.timedelta(days=1)
        return day
    y, m = (year, month - 1) if month > 1 else (year - 1, 12)
    day = datetime.date(y, m, 25)
    while day.weekday() >= 5:
        day -= datetime.timedelta(days=1)
    return business_days_back(day, 3)


def front_months(product, on_date, count=2):
    """on_date に取引されている限月を、期近から count 本。"""
    y, m = on_date.year, on_date.month
    out = []
    while len(out) < count:
        if last_trade_day(product, y, m) >= on_date:
            out.append((y, m))
        y, m = (y, m + 1) if m < 12 else (y + 1, 1)
    return out


def symbol_of(product, year, month):
    return "{}{}{:02d}.NYM".format(product, MONTH_CODES[month - 1], year % 100)


def fetch(symbol, days, on_date=None):
    if on_date:
        # 指定日の前後だけを取る（前日比のため、前に休日をまたいでも足りる幅を取る）
        start = datetime.datetime.combine(on_date - datetime.timedelta(days=10), datetime.time(), datetime.timezone.utc)
        end = datetime.datetime.combine(on_date + datetime.timedelta(days=2), datetime.time(), datetime.timezone.utc)
        span = "period1={}&period2={}".format(int(start.timestamp()), int(end.timestamp()))
    else:
        span = "range=" + ("1mo" if days <= 15 else "3mo")
    req = urllib.request.Request(API_URL.format(symbol=symbol, span=span),
                                 headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as res:
        data = json.loads(res.read().decode("utf-8"))
    result = (data.get("chart") or {}).get("result") or []
    if not result:
        raise ValueError("データなし：{}".format((data.get("chart") or {}).get("error")))
    r = result[0]
    meta = r["meta"]
    period = (meta.get("currentTradingPeriod") or {}).get("regular") or {}
    if not period.get("start"):
        # 取引中の日が分からないと、動いている値を「終値」と出してしまう。取得失敗として扱う
        raise ValueError("取引中の日（currentTradingPeriod）が返らず、終値と未確定を区別できない")
    current = to_eastern_date(period["start"])
    closes = (r.get("indicators", {}).get("quote") or [{}])[0].get("close") or []
    rows, prev = [], None
    for ts, close in zip(r.get("timestamp") or [], closes):
        if close is None:
            continue
        day = to_eastern_date(ts)
        value = round(close, 2)
        if rows and rows[-1]["date"] == day.isoformat():
            # 取引中の日の足が2本返ることがある（2026-10-27 実測）。同じ日は後の1本だけ残す
            rows.pop()
            prev = rows[-1]["close"] if rows else None
        rows.append({
            "date": day.isoformat(),
            "close": value,
            "change": None if prev is None else round(value - prev, 2),
            "final": day < current,
        })
        prev = value
    return {"name": meta.get("longName") or meta.get("shortName"), "rows": rows,
            "current_session": current.isoformat()}


# ---- 報道から当日の終値を拾う（2026-11-12 追加） ----------------------------------------------
# Yahoo の日足は米国東部 0時（日本時間 13〜14時）まで確定しない。朝の日次の時点（米国東部 17〜18時）の値は
# 清算値ではなく、休場直前の最終取引値（2026-11-12 実測：WTI 12月物は清算 86.53 に対し Yahoo 86.42、
# ブレント1月物は清算 92.76 に対し Yahoo 92.63）。そこで、清算の後に配信された報道を Google ニュースの RSS で探し
# （WebSearch の索引は数時間遅れるので使わない）、本文から清算値を読んで系統ごとに並べる。

WIRE_QUERIES = ["oil settle", "Brent settled", "\"Settles at\" WTI", "oil prices Brent WTI", "crude oil futures",
                "Rigzone oil", "Reuters oil prices"]
# 本文が読めて、系統が分かる媒体を先に開く（WSJ・Barron's・MarketWatch は 401 で開けない。2026-11-12 実測）
PREFERRED = re.compile(r"rigzone|yahoo|reuters|bloomberg|associated press|\bap\b|cnbc|investinglive|nasdaq|"
                       r"morningstar|kyodo|xinhua|the star|bernama|newsquawk", re.I)
PAYWALL = re.compile(r"\bwsj\b|wall street journal|barron|marketwatch|financial times|\bft\b", re.I)
PRICE_WORDS = re.compile(r"settle|oil (?:price|rise|rose|fall|fell|gain|climb|slip|drop|jump|edge|rebound)|crude (?:price|rise|fall)", re.I)
OIL_WORDS = re.compile(r"\boil\b|crude|brent|wti", re.I)
# MT Newswires の清算速報の見出し（MarketScreener に配信。2026-11-13 に記事の署名で MT Newswires と確認。
# 11/12 までは Dow Jones と誤って名付けていた。Dow Jones・Bloomberg・Reuters とは別の系統）
MTN_TITLE = re.compile(r"(\w+) WTI Crude Oil Contract Closes (Up|Down) \$([\d.]+).{0,40}?Settles at \$(\d{2,3}\.\d{2})", re.I)
# 取引中・時間外の値の語。この語をはさむ価格は終値として拾わない（Codex の指摘・PR #172）
LIVE = r"trad|after-hours|post-settlement|post settlement|last seen|intraday|was at|were at"
NOT_WTI = r"(?:(?!WTI|West Texas|U\.?S\.? crude|" + LIVE + r").)"
NOT_BRENT = r"(?:(?!Brent|" + LIVE + r").)"
BRENT_RE = [re.compile(r"Brent\b" + NOT_WTI + r"{0,160}?settl\w*" + NOT_WTI + r"{0,90}?\b(?:at|to) \$(\d{2,3}\.\d{2})", re.I),
            re.compile(r"Brent\b" + NOT_WTI + r"{0,60}?\bsettled (?:at )?\$(\d{2,3}\.\d{2})", re.I)]
# WTI は「settle」の語を WTI の価格に結びつけて探す
WTI_RE = [re.compile(r"(?:WTI|West Texas Intermediate|U\.?S\.? crude)\b" + NOT_BRENT + r"{0,160}?settl\w*" + NOT_BRENT + r"{0,90}?\b(?:at|to) \$(\d{2,3}\.\d{2})", re.I)]
# Reuters は「Brent futures settled … at $X, while US WTI crude gained 49 cents … to $Y」と書く（WTI の側に settle が無い）。
# この形だけは、ブレントの清算の文の直後（250字まで）に、値動きの動詞＋「to $」で続く WTI を拾う
WTI_AFTER_BRENT = re.compile(
    r"^" + NOT_BRENT + r"{0,60}?(?:WTI|West Texas Intermediate)\b" + NOT_BRENT + r"{0,100}?"
    r"\b(?:rose|gained|added|climbed|rallied|advanced|jumped|fell|lost|dropped|declined|slipped|eased|shed|slid)\b"
    + NOT_BRENT + r"{0,60}?\bto \$(\d{2,3}\.\d{2})", re.I)


def eastern(day, hour, minute=0):
    """米国東部のその日時を UTC にする。"""
    naive = datetime.datetime.combine(day, datetime.time(hour, minute), datetime.timezone.utc)
    return naive - us_eastern_offset(naive + datetime.timedelta(hours=5))


def page_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as res:
        raw = res.read().decode("utf-8", "replace")
    raw = re.sub(r"<script\b.*?</script\b[^>]*>|<style\b.*?</style\b[^>]*>", " ", raw, flags=re.S | re.I)
    text = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    return re.sub(r"\s+", " ", text)


def on_domain(host, *domains):
    """host がそのドメインか、そのサブドメインか（文字列の部分一致にしない）。"""
    return any(host == d or host.endswith("." + d) for d in domains)


def family_of(source, url, text):
    """通信社の系統（同じ系統どうしは1出典と数える。スキル「二次情報の裏取り」）。"""
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    head = text[:6000]
    if on_domain(host, "reuters.com") or "(Reuters)" in head or "Reuters" in (source or ""):
        return "Reuters 系"
    if on_domain(host, "bloomberg.com") or "Bloomberg" in head:
        return "Bloomberg 系"
    if "Associated Press" in head or "(AP)" in head or on_domain(host, "apnews.com"):
        return "AP 系"
    if "MT Newswires" in head:
        return "MT Newswires 系"
    if "Dow Jones" in head or on_domain(host, "marketwatch.com", "wsj.com"):
        return "Dow Jones 系"
    if on_domain(host, "investinglive.com"):
        return "investingLive"
    if on_domain(host, "newsquawk.com"):
        return "Newsquawk"
    if on_domain(host, "cnbc.com"):
        return "CNBC"
    return "{}（系統は本文で確かめる）".format(source or host)


def first_match(patterns, text, lo, hi):
    """(値, 原文の前後, 一致の終わりの位置)。"""
    for pat in patterns:
        for m in pat.finditer(text):
            v = float(m.group(1))
            if lo <= v <= hi:
                return v, text[max(0, m.start() - 20):m.end() + 20], m.end()
    return None, None, None


def extract_closes(text, prev):
    """本文から {"ブレント": 値, "WTI": 値} と原文の前後を読む。"""
    vals, snips = {}, {}
    bounds = {}
    for label in ("ブレント", "WTI"):
        base = prev.get(label)
        bounds[label] = (base * 0.85, base * 1.15) if base else (20, 300)
    vals["ブレント"], snips["ブレント"], b_end = first_match(BRENT_RE, text, *bounds["ブレント"])
    vals["WTI"], snips["WTI"], _ = first_match(WTI_RE, text, *bounds["WTI"])
    if vals["WTI"] is None and b_end is not None:
        m = WTI_AFTER_BRENT.search(text[b_end:b_end + 250])
        if m and bounds["WTI"][0] <= float(m.group(1)) <= bounds["WTI"][1]:
            vals["WTI"] = float(m.group(1))
            snips["WTI"] = text[max(0, b_end - 60):b_end + m.end() + 20]
    return vals, snips


def wire_closes(day, prev, max_fetch=14):
    """day（米国時間の取引日）の清算後に配信された報道から、ブレント・WTI の終値の候補を集める。
    prev：{"ブレント": 前の取引日の終値, "WTI": …}（値の範囲の目安に使う）。"""
    import fetch_news_feeds as nf  # 同じ tools/ にある

    start, end = eastern(day, 14, 30), eastern(day + datetime.timedelta(days=1), 14, 0)
    seen, cands, errors = set(), [], []
    for q in WIRE_QUERIES:
        try:
            for it in nf.google_news(q, "en", "2d"):
                if not (start <= it["published"] < end) or not OIL_WORDS.search(it["title"]):
                    continue
                key = nf.norm_title(it["title"])
                if key not in seen:
                    seen.add(key)
                    cands.append(it)
        except (urllib.error.URLError, OSError, ValueError) as e:
            errors.append("Google ニュース「{}」：{}".format(q, e))

    found = []
    # MT Newswires の清算速報の見出し（MarketScreener に配信）は、見出しだけで WTI の清算値が分かる
    for it in cands:
        m = MTN_TITLE.search(it["title"])
        if m:
            found.append({"family": "MT Newswires 系", "source": it["source"], "title": it["title"], "link": it["link"],
                          "published": it["published"], "WTI": float(m.group(4)), "ブレント": None,
                          "snippet": {"WTI": it["title"]}, "from_title": True})
    fetched = 0
    def priority(it):
        src = it.get("source") or ""
        return (0 if PREFERRED.search(src) else 1, 0 if PRICE_WORDS.search(it["title"]) else 1, it["published"])

    for it in sorted(cands, key=priority):
        if PAYWALL.search(it.get("source") or ""):
            continue
        if fetched >= max_fetch or MTN_TITLE.search(it["title"]):
            continue
        fetched += 1
        try:
            url = nf.resolve_google(it["link"])
            text = page_text(url)
        except (urllib.error.URLError, OSError, ValueError, KeyError, IndexError, json.JSONDecodeError) as e:
            errors.append("{}：{}".format(it["title"][:60], e))
            continue
        if not re.search(r"settl", text, re.I):
            continue
        row = {"family": family_of(it["source"], url, text), "source": it["source"], "title": it["title"],
               "link": url, "published": it["published"], "snippet": {}}
        vals, snips = extract_closes(text, prev)
        row.update(vals)
        row["snippet"] = snips
        if row["ブレント"] or row["WTI"]:
            found.append(row)
    for row in found:
        if row.get("from_title"):
            try:
                row["link"] = nf.resolve_google(row["link"])
            except (urllib.error.URLError, OSError, ValueError, KeyError, IndexError, json.JSONDecodeError):
                pass
    return found, errors


def judge(found, label):
    """値ごとに系統を数え、2系統以上で一致した値を返す（無ければ None）。"""
    by_value = {}
    for row in found:
        v = row.get(label)
        if v is not None:
            fam = row["family"]
            if "系統は本文で確かめる" in fam:
                fam = "その他：" + fam
            by_value.setdefault(v, set()).add(fam)
    named = {v: {f for f in fams if not f.startswith("その他：")} for v, fams in by_value.items()}
    agreed = [v for v, fams in named.items() if len(fams) >= 2]
    return (agreed[0] if len(agreed) == 1 else None), by_value


def main():
    ap = argparse.ArgumentParser(description="ブレント・WTI の限月ごとの終値を市場データから読む（読み取り専用）")
    ap.add_argument("--days", type=int, default=7, help="直近◯取引日を出す（既定 7）")
    ap.add_argument("--date", help="取引日（米国時間）を YYYY-MM-DD で指定。その日の終値だけ出す")
    ap.add_argument("--month", help="限月を YYYY-MM で指定（既定：その日の期近と次の限月）")
    ap.add_argument("--json", action="store_true", help="JSON で出す")
    ap.add_argument("--no-wire", action="store_true",
                    help="「未確定」の取引日があっても、報道から終値を探さない")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    on_date = datetime.date.fromisoformat(args.date) if args.date else datetime.date.today()
    out, failed = [], []
    for label, product in PRODUCTS:
        if args.month:
            y, m = (int(x) for x in args.month.split("-"))
            months = [(y, m)]
        else:
            months = front_months(product, on_date)
        for i, (y, m) in enumerate(months):
            symbol = symbol_of(product, y, m)
            item = {"product": label, "contract": "{}年{}月物".format(y, m), "symbol": symbol,
                    "front": not args.month and i == 0,
                    "last_trade_day": last_trade_day(product, y, m).isoformat(),
                    "url": PAGE_URL.format(symbol=symbol)}
            try:
                got = fetch(symbol, args.days, on_date if args.date else None)
            except (urllib.error.URLError, ValueError, KeyError, json.JSONDecodeError, OSError) as e:
                failed.append("{}（{}）：{}".format(symbol, label, e))
                continue
            rows = got["rows"]
            rows = [r for r in rows if r["date"] == args.date] if args.date else rows[-args.days:]
            item.update(name=got["name"], current_session=got["current_session"], rows=rows)
            out.append(item)

    if args.json:
        print(json.dumps({"items": out, "errors": failed}, ensure_ascii=False, indent=2))
    else:
        print("出典：Yahoo Finance（NYMEX のデータ）。終値は清算値。「未確定」は取引中の日で、夜間の取引で動いている値")
        for it in out:
            mark = "（期近）" if it["front"] else ""
            print("\n■ {} {}{} {}  取引最終日の目安 {}".format(it["product"], it["contract"], mark, it["symbol"], it["last_trade_day"]))
            print("  {}".format(it["url"]))
            if not it["rows"]:
                print("  該当する取引日なし")
            for r in it["rows"]:
                chg = "" if r["change"] is None else "（{:+.2f}）".format(r["change"])
                state = "終値" if r["final"] else "未確定（取引中の日。終値に使わない）"
                print("  {}  {:.2f}{}  {}".format(r["date"], r["close"], chg, state))
        for f in failed:
            print("\n取得できなかった：" + f, file=sys.stderr)

    # 最新の取引日が「未確定」なら、報道から清算値を探す（朝の日次はほぼ毎回これになる）
    if not args.no_wire and not args.month and not args.json:
        fronts = [it for it in out if it["front"] and it["rows"]]
        pending = sorted({r["date"] for it in fronts for r in it["rows"] if not r["final"]})
        now = datetime.datetime.now(datetime.timezone.utc)
        for d in pending:
            day = datetime.date.fromisoformat(d)
            if now < eastern(day, 15, 0):
                print("\n{} はまだ清算前（米国東部 14:30）。報道を探さない".format(d))
                continue
            prev = {}
            for it in fronts:
                finals = [r for r in it["rows"] if r["final"] and r["date"] < d]
                if finals:
                    prev[it["product"]] = finals[-1]["close"]
            found, errs = wire_closes(day, prev)
            print("\n■■ {}（米国時間）の終値を報道から探した結果（Google ニュースの RSS・清算後の配信だけ）".format(d))
            print("   Yahoo の同じ日の値は「未確定」なので使わない。下の値は本文の文で確かめてから使う")
            for row in found:
                t = row["published"].astimezone(datetime.timezone(datetime.timedelta(hours=9))).strftime("%m/%d %H:%M JST")
                vals = "　".join("{} {}".format(k, "{:.2f}".format(row[k]) if row[k] else "—") for k in ("ブレント", "WTI"))
                print("  ・{}｜{}｜{}｜{}".format(t, row["family"], row["source"], vals))
                print("    {}".format(row["link"]))
                for k, sn in row["snippet"].items():
                    if sn:
                        print("    原文（{}）：…{}…".format(k, sn))
            if not found:
                print("  候補なし（清算後の配信が RSS にまだ無い）")
            for label in ("ブレント", "WTI"):
                fronts_l = [it for it in fronts if it["product"] == label]
                contract = fronts_l[0]["contract"] if fronts_l else "限月不明"
                value, by_value = judge(found, label)
                detail = "、".join("{:.2f}＝{}".format(v, "・".join(sorted(f))) for v, f in sorted(by_value.items()))
                base = prev.get(label)
                chg = "" if (value is None or base is None) else "（前日比 {:+.2f}。前の終値 {:.2f} は Yahoo で確定済み）".format(value - base, base)
                if value is not None:
                    print("  【判定】{} {}：{:.2f}{}　2系統以上で一致 → 終値として使える（{}）".format(label, contract, value, chg, detail))
                else:
                    print("  【判定】{} {}：確定できず（{}）→ 据え置き。WebSearch で数値を引用符で囲んで2出典目を探す".format(
                        label, contract, detail or "候補なし"))
                print("          限月は報道の本文（「January」「December」など）と照らし合わせる")
            for e in errs:
                print("  取得できなかった：" + e, file=sys.stderr)

    return 2 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
