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
    切り替わる米国東部 0時（日本時間 13時・夏時間）以降。**朝の日次では、前日（米国時間）の終値は
    多くの場合「未確定」と出る。**その日の終値は報道2出典で確かめ、このスクリプトは
    それより前の日の終値（前回の更新で据え置いた終値の裏取り）に使う
  - 期近をつなげた銘柄（CL=F・BZ=F）は限月が途中で切り替わる（10/26 に BZ=F は既に1月物だった）。
    サイトの限月と合わせるため、必ず限月を指定した銘柄（BZZ26.NYM など）で読む
  - 満期を過ぎた限月は Yahoo から消える（404）。その限月の過去の終値は取れないので、終了コード 2 になる
  - CME の公式サイトは自動取得を利用規約で禁じ、403 を返す。ICE は Cloudflare で拒否される。どちらも使わない

使い方：
    python tools/fetch_oil_settle.py                     # 期近とその次の限月、直近7取引日
    python tools/fetch_oil_settle.py --date 2026-10-26   # その取引日の終値だけ
    python tools/fetch_oil_settle.py --month 2026-12     # 限月を指定（ブレント・WTI とも）
    python tools/fetch_oil_settle.py --json

終了コード：0＝取得できた（「未確定」を含む）／2＝取得できなかった（報道の2出典で確かめる）
"""
import argparse
import datetime
import json
import sys
import urllib.error
import urllib.request

API_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?{span}&interval=1d"
PAGE_URL = "https://finance.yahoo.com/quote/{symbol}/history/"
USER_AGENT = "Mozilla/5.0 (compatible; chokepointlab-daily/1.0; +https://chokepointlab.com/contact/)"
MONTH_CODES = "FGHJKMNQUVXZ"
PRODUCTS = (("ブレント", "BZ"), ("WTI", "CL"))


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
    offset = datetime.timedelta(seconds=meta.get("gmtoffset", 0))
    period = (meta.get("currentTradingPeriod") or {}).get("regular") or {}
    if not period.get("start"):
        # 取引中の日が分からないと、動いている値を「終値」と出してしまう。取得失敗として扱う
        raise ValueError("取引中の日（currentTradingPeriod）が返らず、終値と未確定を区別できない")
    current = (datetime.datetime.fromtimestamp(period["start"], datetime.timezone.utc) + offset).date()
    closes = (r.get("indicators", {}).get("quote") or [{}])[0].get("close") or []
    rows, prev = [], None
    for ts, close in zip(r.get("timestamp") or [], closes):
        if close is None:
            continue
        day = (datetime.datetime.fromtimestamp(ts, datetime.timezone.utc) + offset).date()
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


def main():
    ap = argparse.ArgumentParser(description="ブレント・WTI の限月ごとの終値を市場データから読む（読み取り専用）")
    ap.add_argument("--days", type=int, default=7, help="直近◯取引日を出す（既定 7）")
    ap.add_argument("--date", help="取引日（米国時間）を YYYY-MM-DD で指定。その日の終値だけ出す")
    ap.add_argument("--month", help="限月を YYYY-MM で指定（既定：その日の期近と次の限月）")
    ap.add_argument("--json", action="store_true", help="JSON で出す")
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

    return 2 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
