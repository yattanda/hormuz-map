"""Cloudflare のプロキシ（オレンジ／灰色）を chokepointlab.com の apex と www で切り替える（2026-11-01 追加）。

対象は apex の A 4件と www の CNAME だけ。メール（MX・DKIM・SPF）や確認用の TXT は触らない。
既定は「何をするかを表示するだけ」。--yes を付けたときだけ書き換える。

使い方：
  python tools/cf_proxy.py status                # 今の状態を表示（読み取りだけ）
  python tools/cf_proxy.py on  [--yes]           # プロキシ有り（オレンジ）に
  python tools/cf_proxy.py off [--yes]           # プロキシ無し（灰色）に。先に delivery_check で直接の経路を確かめる

API トークン：環境変数 CLOUDFLARE_API_TOKEN（運営者が Cloudflare で作る。権限は「ゾーン → DNS → 編集」、
対象のゾーンは chokepointlab.com だけ）。トークンの値をファイルやコミットに書かない。
トークンが無いときは、画面での切り替え（スキル delivery-check「画面での切り替え」）で行う。
設計 hormuz-ops/drafts/design/cloudflare-proxy-plan.md
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ZONE = "chokepointlab.com"
TARGETS = (("A", ZONE), ("CNAME", "www." + ZONE))   # この2種類の名前のレコードだけを切り替える
API = "https://api.cloudflare.com/client/v4"


def call(method: str, path: str, token: str, body: dict | None = None) -> dict:
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        d = json.loads(e.read().decode() or "{}")
    if not d.get("success"):
        msg = "；".join(f'{x.get("code")} {x.get("message")}' for x in d.get("errors", [])) or "不明なエラー"
        sys.exit(f"Cloudflare API のエラー：{method} {path}：{msg}")
    return d


def records(token: str) -> tuple[str, list[dict]]:
    zone = call("GET", f"/zones?name={ZONE}", token)["result"]
    if not zone:
        sys.exit(f"ゾーン {ZONE} が見つかりません（トークンの対象のゾーンを確かめる）")
    zid = zone[0]["id"]
    out = []
    for typ, name in TARGETS:
        out += call("GET", f"/zones/{zid}/dns_records?type={typ}&name={name}&per_page=100", token)["result"]
    return zid, out


def show(recs: list[dict]) -> None:
    for r in recs:
        print(f'  {r["type"]:<5} {r["name"]:<22} {r["content"]:<20} {"オレンジ（プロキシ有り）" if r["proxied"] else "灰色（DNS only）"}')
    a = [r for r in recs if r["type"] == "A"]
    if len(a) != 4 or len(recs) != 5:
        print(f"  ※ 想定は A 4件＋CNAME 1件。見つかったのは A {len(a)}件・合計 {len(recs)}件（DNS の画面で確かめる）")


def main() -> int:
    ap = argparse.ArgumentParser(description="Cloudflare のプロキシの切り替え（apex と www だけ）")
    ap.add_argument("action", choices=("status", "on", "off"))
    ap.add_argument("--yes", action="store_true", help="実際に書き換える（無いときは表示だけ）")
    ap.add_argument("--skip-check", action="store_true", help="off の前の delivery_check を省く")
    ap.add_argument("--force", action="store_true", help="delivery_check が「戻してよい」でなくても off にする")
    args = ap.parse_args()

    token = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
    if not token:
        sys.exit("環境変数 CLOUDFLARE_API_TOKEN がありません。画面で切り替える手順はスキル delivery-check の「画面での切り替え」")
    zid, recs = records(token)
    print(f"{ZONE} の apex と www（今）")
    show(recs)
    if args.action == "status":
        return 0

    want = args.action == "on"
    todo = [r for r in recs if r["proxied"] != want]
    if not todo:
        print(f"\nすでに{'オレンジ' if want else '灰色'}です。何もしません")
        return 0

    if not want and not args.skip_check:
        print("\nプロキシ無しに戻す前に、GitHub Pages から直接取ったときの状態を確かめます（delivery_check.py）")
        rc = subprocess.run([sys.executable, str(Path(__file__).with_name("delivery_check.py"))]).returncode
        if rc != 0 and not args.force:
            print("\n直接の経路が「戻してよい」ではないので、灰色に戻しません（どうしても戻すなら --force）")
            return 1

    print(f"\n{len(todo)}件を{'オレンジ（プロキシ有り）' if want else '灰色（DNS only）'}にします")
    if not args.yes:
        print("（表示だけ。書き換えるには --yes を付けて実行）")
        return 0
    for r in todo:
        call("PATCH", f'/zones/{zid}/dns_records/{r["id"]}', token, {"proxied": want})
    print("書き換えました。今の状態：")
    show(records(token)[1])
    print("\n5〜10分ほどで行き渡ります。そのあと python tools/delivery_check.py で今の経路を確かめる")
    if want:
        print("（プロキシ有りにしたら、応答の server が cloudflare になり、2回目から cf-cache-status: HIT になるはず）")
    return 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")   # Windows の既定（cp932）で文字化けさせない
    sys.exit(main())
