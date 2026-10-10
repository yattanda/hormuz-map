#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UKMTO の警報（Recent Incidents）の本文を公式の公開 API から読む。読み取り専用。

日次更新の裏取り（.claude/skills/daily-site-update/SKILL.md「2.5 裏取り」）で使う。
ukmto.org の一覧ページは JS があとから本文を入れるため、WebFetch では本文が取れない
（既定の User-Agent には 403 を返す）。一覧ページ自身が読んでいる JSON を、
サイト名と連絡先を名乗る User-Agent で取りに行く（2026-10-10 に PC から実測して 200）。

使い方：
    python tools/fetch_ukmto.py              # 直近3日に発行された警報
    python tools/fetch_ukmto.py --days 7     # 直近7日
    python tools/fetch_ukmto.py --number 160 # 警報番号を指定
    python tools/fetch_ukmto.py --json       # 絞り込んだ結果を JSON で出す

終了コード：0＝取得できた（該当0件を含む）／2＝取得できなかった（本文は「未確認」のまま扱う）
"""
import argparse
import datetime
import json
import sys
import urllib.error
import urllib.request

API_URL = "https://sccd.royalnavy.mod.uk/api/ukmto/all"
PAGE_URL = "https://www.ukmto.org/recent-incidents"
USER_AGENT = "chokepointlab-daily/1.0 (+https://chokepointlab.com/contact/)"
JST = datetime.timezone(datetime.timedelta(hours=9))


def parse_utc(value):
    if not value:
        return None
    return datetime.datetime.strptime(value[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=datetime.timezone.utc)


def fmt(dt):
    if dt is None:
        return "記載なし"
    return "{} UTC（{} JST）".format(dt.strftime("%Y-%m-%d %H:%M"), dt.astimezone(JST).strftime("%m/%d %H:%M"))


def fetch():
    req = urllib.request.Request(API_URL, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.loads(res.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description="UKMTO の警報の本文を公式の公開 API から読む（読み取り専用）")
    ap.add_argument("--days", type=int, default=3, help="発行日が直近◯日のものを出す（既定 3）")
    ap.add_argument("--number", type=int, action="append", help="警報番号（例：160）。複数指定可。指定すると --days は無視")
    ap.add_argument("--json", action="store_true", help="JSON で出す")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    try:
        items = fetch()
    except (urllib.error.URLError, OSError, ValueError) as e:
        print("取得できなかった：{}（{}）".format(e, API_URL), file=sys.stderr)
        print("UKMTO 公式の本文は「未確認」のまま扱う。回避策を探さず、報告に このエラーを書く。", file=sys.stderr)
        return 2
    if not isinstance(items, list):
        print("取得できなかった：想定と違う形の応答（list ではない）", file=sys.stderr)
        return 2

    now = datetime.datetime.now(datetime.timezone.utc)
    if args.number:
        picked = [x for x in items if x.get("incidentNumber") in args.number]
    else:
        since = now - datetime.timedelta(days=args.days)
        picked = [x for x in items if (parse_utc(x.get("utcDateCreated")) or now) >= since]
    picked.sort(key=lambda x: x.get("utcDateCreated") or "", reverse=True)

    if args.json:
        print(json.dumps(picked, ensure_ascii=False, indent=2))
        return 0

    newest = max((x.get("utcDateCreated") or "" for x in items), default="")
    print("UKMTO Recent Incidents（公式の公開 API・取得 {}）".format(fmt(now)))
    print("出典として書く URL：{}".format(PAGE_URL))
    print("全 {} 件・最新の発行 {}・該当 {} 件".format(len(items), fmt(parse_utc(newest)), len(picked)))
    for x in picked:
        print("-" * 60)
        print("警報 #{}（{}）".format(x.get("incidentNumber"), (x.get("incidentTypeName") or "").strip()))
        print("  発行（utcDateCreated）　　 : {}".format(fmt(parse_utc(x.get("utcDateCreated")))))
        print("  日時欄（utcDateOfIncident）: {}".format(fmt(parse_utc(x.get("utcDateOfIncident")))))
        print("  場所の欄：{}／緯度経度：{} {}／船種の欄：{}".format(
            (x.get("place") or "").strip() or "記載なし",
            x.get("locationLatitudeDDDMMSS") or "-", x.get("locationLongitudeDDDMMSS") or "-",
            (x.get("vesselType") or "").strip() or "記載なし"))
        print("  本文（原文）：")
        for line in (x.get("otherDetails") or "").replace("\r\n", "\n").split("\n"):
            print("    " + line)
    if not picked:
        print("該当する警報なし（条件を満たす発行がない。警報が出ていないことの確認として書ける）")
    print("-" * 60)
    print("注：「日時欄」は発生時刻とは限らない（遅れての報告では報告を受けた時刻のことがある）。")
    print("　　発生日時は本文の Incident Date / Time を優先し、本文に無ければ「公式の本文に発生時刻の記載なし」と書く。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
