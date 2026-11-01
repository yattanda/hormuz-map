"""chokepointlab.com の配信の速さと、GitHub Pages から直接取ったときの状態を測る（2026-11-01 追加）。

11/1 にマージ後の本番が日本から極端に遅くなった（GitHub Pages がこのサイトだけ遅い）。
Cloudflare のプロキシを前に挟んだあとも、「プロキシ無し（DNS only）に戻してよいか」を
いつでも事前に確かめられるように、次の3つを同じ条件で測る：

  1. 今の経路     … ふつうに名前解決した chokepointlab.com（プロキシ有りなら Cloudflare 経由）
  2. 直接（Pages） … GitHub Pages の IP（185.199.108〜111.153）へ直接つなぐ。プロキシ無しにしたときの姿
  3. 比べる相手   … 同じ中身の raw.githubusercontent.com と、別の GitHub Pages のサイト（こちらの回線の確認）

直接の経路は、GitHub の証明書（chokepointlab.com 用）の有効性と残り日数も見る。
プロキシの下では GitHub の証明書の更新が失敗することがあり、切れたまま戻すとサイトが開かなくなる。

使い方：
  python tools/delivery_check.py            # 全部測って「戻してよいか」を出す（1〜2分）
  python tools/delivery_check.py --quick    # /hormuz/ だけ・IP 1つ（約30秒）
  python tools/delivery_check.py --json out.json
  python tools/delivery_check.py --history <フォルダ>   # 結果をフォルダに貯め、証拠の1ページ（report.html）を作り直す

終了コード：0＝直接の経路は良好（戻してよい）／1＝不良（戻さない）／2＝保留（こちらの回線も遅い・測れない）
読み取りだけで、サイトにも DNS にも何も書き込まない。設計 hormuz-ops/drafts/design/cloudflare-proxy-plan.md
"""
from __future__ import annotations

import argparse
import http.client
import json
import socket
import ssl
import sys
import time
from datetime import datetime, timezone, timedelta

HOST = "chokepointlab.com"
PAGES_IPS = ["185.199.108.153", "185.199.109.153", "185.199.110.153", "185.199.111.153"]
FILES = ["/hormuz/", "/data/news_data.json", "/assets/vendor/leaflet-1.9.4/leaflet.js", "/"]
RAW = ("raw.githubusercontent.com", "/yattanda/hormuz-map/main/docs/hormuz/index.html")
OTHER_PAGES = ("google.github.io", "/styleguide/cppguide.html")   # 別の GitHub Pages のサイト（約430KB）

TIMEOUT = 30           # 1ファイルの打ち切り（秒）
GOOD_SPEED = 200_000   # B/秒。大きいファイル（10KB 以上）がこれ以上なら良好
BAD_SPEED = 50_000     # B/秒。これ未満か、打ち切りなら不良
CERT_MIN_DAYS = 14     # 直接の経路の証明書の残り日数がこれ未満なら、戻すと危ない
JST = timezone(timedelta(hours=9))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36 chokepointlab-delivery-check/1"
CF_NOT_CACHED = ("DYNAMIC", "BYPASS")   # Cloudflare がキャッシュの対象にしていない印（キャッシュルールが効いていない）


def fetch(host: str, path: str, ip: str | None = None, timeout: float = TIMEOUT) -> dict:
    """host の path を取る。ip を渡すと名前解決をせず、その IP へ SNI＝host でつなぐ。圧縮なしで本文を全部読む"""
    res = {"host": host, "path": path, "ip": ip, "status": None, "bytes": 0, "secs": None,
           "speed": 0, "complete": False, "error": None, "headers": {}}
    ctx = ssl.create_default_context()
    t0 = time.monotonic()
    try:
        raw = socket.create_connection((ip or host, 443), timeout=10)
        sock = ctx.wrap_socket(raw, server_hostname=host)
        cert = sock.getpeercert()
        exp = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
        res["cert_days"] = (exp - datetime.now(timezone.utc)).days
        res["cert_issuer"] = dict(x[0] for x in cert.get("issuer", ())).get("organizationName", "")
        res["peer_ip"] = sock.getpeername()[0]
        conn = http.client.HTTPSConnection(host, timeout=10)
        conn.sock = sock
        # 読者のブラウザと同じ条件で取る：キャッシュを飛ばす指示（Cache-Control: no-cache）は付けない
        # （付けると Cloudflare がキャッシュを使わず、読者より遅く出ることがある）。
        # 名乗りはブラウザに近い形＋道具の名前（Cloudflare の Browser Integrity Check に止められにくく）
        conn.request("GET", path, headers={"User-Agent": UA, "Accept-Encoding": "identity", "Accept": "*/*"})
        r = conn.getresponse()
        res["status"] = r.status
        res["headers"] = {k.lower(): v for k, v in r.getheaders()
                          if k.lower() in ("server", "cf-cache-status", "x-cache", "x-served-by", "age",
                                           "content-length", "location")}
        want = int(res["headers"].get("content-length") or 0)
        deadline = t0 + timeout
        while time.monotonic() < deadline:
            sock.settimeout(max(0.5, deadline - time.monotonic()))
            try:
                chunk = r.read(65536)
            except (socket.timeout, TimeoutError):
                break
            if not chunk:
                res["complete"] = (not want) or res["bytes"] >= want
                break
            res["bytes"] += len(chunk)
        conn.close()
    except ssl.SSLCertVerificationError as e:
        res["error"] = f"証明書のエラー：{e.verify_message}"
        res["cert_error"] = True
    except Exception as e:   # noqa: BLE001  測るだけなので、どの失敗も結果に書いて続ける
        res["error"] = f"{type(e).__name__}: {e}"
    res["secs"] = round(time.monotonic() - t0, 2)
    res["speed"] = int(res["bytes"] / res["secs"]) if res["secs"] else 0
    return res


def grade(r: dict) -> str:
    """1ファイルの結果を 良好／注意／不良 に分ける"""
    if r["error"] or r["status"] != 200:
        return "不良"
    if not r["complete"]:
        return "不良"
    if r["bytes"] < 10_000:          # 小さいファイルは速さより時間で見る
        return "良好" if r["secs"] < 2 else "注意" if r["secs"] < 5 else "不良"
    return "良好" if r["speed"] >= GOOD_SPEED else "注意" if r["speed"] >= BAD_SPEED else "不良"


def line(label: str, r: dict) -> str:
    h = r["headers"]
    via = h.get("server", "")
    cache = h.get("cf-cache-status") or h.get("x-cache") or ""
    if r["error"]:
        body = r["error"]
    else:
        body = (f'{r["status"]} {r["bytes"]:>8,}B {r["secs"]:>6.2f}s {r["speed"]:>10,}B/秒'
                f'{"" if r["complete"] else "（打ち切り）"}  {via} {cache}')
    return f"  [{grade(r)}] {label:<34} {body}"


def current_mode() -> tuple[str, list[str]]:
    """ふつうの名前解決で chokepointlab.com がどこを向いているか"""
    try:
        ips = sorted({ai[4][0] for ai in socket.getaddrinfo(HOST, 443, proto=socket.IPPROTO_TCP)})
    except OSError as e:
        return f"名前解決に失敗（{e}）", []
    v4 = [ip for ip in ips if ":" not in ip]
    if v4 and all(ip in PAGES_IPS for ip in v4):
        return "プロキシ無し（DNS only・GitHub Pages を直接向いている）", ips
    return "プロキシ有り（Cloudflare を向いている）の見込み", ips


def main() -> int:
    ap = argparse.ArgumentParser(description="配信の速さと、プロキシ無しに戻してよいかの確認（読み取りだけ）")
    ap.add_argument("--quick", action="store_true", help="/hormuz/ だけ・直接の IP は1つ")
    ap.add_argument("--json", help="結果を JSON で保存するパス")
    ap.add_argument("--history", help="結果を貯めるフォルダ。delivery-YYYYMMDD-HHMM.json を足し、同じフォルダの report.html を作り直す")
    args = ap.parse_args()

    started = datetime.now(JST)
    now = started.strftime("%Y-%m-%d %H:%M JST")
    mode, ips = current_mode()
    print(f"配信の確認 {now}\n今の向き先：{mode}（{', '.join(ips)}）\n")
    files = FILES[:1] if args.quick else FILES
    out = {"at": now, "at_iso": started.isoformat(timespec="seconds"), "tool": "delivery_check.py",
           "quick": args.quick, "mode": mode, "ips": ips, "current": [], "direct": [], "control": []}

    print("1. 今の経路（読者が実際に通る道）")
    for p in files:
        r = fetch(HOST, p)
        # プロキシ有りで Cloudflare の手元に無かった（MISS・EXPIRED）ときは、GitHub へ取りに行った分だけ遅い。
        # 10分に1回の読者だけがこれに当たるので、もう1回取って、ふつうの読者の速さ（2回目）を記録する
        if (r["headers"].get("cf-cache-status") or "").upper() in ("MISS", "EXPIRED") and not r["error"]:
            first = {k: r[k] for k in ("secs", "speed", "bytes", "complete")}
            first["cache"] = r["headers"].get("cf-cache-status")
            print(line(p + "（1回目）", r))
            r = fetch(HOST, p)
            r["first"] = first
            p = p + "（2回目）"
        out["current"].append(r)
        print(line(p, r))
    if mode.startswith("プロキシ有り"):
        cg = [grade(r) for r in out["current"]]
        not_cached = [r["path"] for r in out["current"]
                      if (r["headers"].get("cf-cache-status") or "").upper() in CF_NOT_CACHED]
        note = f"読者の経路（Cloudflare）：良好 {cg.count('良好')}／{len(cg)}"
        if not_cached:
            note += f"。キャッシュされていないもの：{'・'.join(not_cached)}（キャッシュルールを確かめる）"
        out["current_note"] = note
        print(f"  → {note}")

    print("\n2. 直接 GitHub Pages（プロキシ無しにしたときの姿）")
    direct_ips = PAGES_IPS[:1] if args.quick else PAGES_IPS
    for p in files:
        for ip in (direct_ips if p == "/hormuz/" else PAGES_IPS[:1]):
            r = fetch(HOST, p, ip=ip)
            out["direct"].append(r)
            print(line(f"{p} @{ip}", r))
    cert_days = [r.get("cert_days") for r in out["direct"] if r.get("cert_days") is not None]
    cert_err = any(r.get("cert_error") for r in out["direct"])

    print("\n3. 比べる相手（こちらの回線の確認）")
    for label, (h, p) in (("raw（同じ HTML）", RAW), ("別の GitHub Pages のサイト", OTHER_PAGES)):
        r = fetch(h, p)
        out["control"].append(r)
        print(line(label, r))

    # 判定
    print("\n判定：プロキシ無し（DNS only）に戻してよいか")
    direct_grades = [grade(r) for r in out["direct"]]
    control_ok = all(grade(r) == "良好" for r in out["control"])
    reasons = []
    if cert_err:
        reasons.append("直接の経路で GitHub の証明書が通らない（戻すとサイトが開かない）")
    elif cert_days and min(cert_days) < CERT_MIN_DAYS:
        reasons.append(f"GitHub の証明書の残りが {min(cert_days)}日（{CERT_MIN_DAYS}日未満）")
    elif cert_days:
        print(f"  証明書：GitHub の証明書は有効・残り {min(cert_days)}日")
    if not control_ok:
        verdict, code = "保留", 2
        reasons.append("比べる相手も遅い・取れない。こちらの回線の問題の疑い。時間をおいて測り直す")
    elif cert_err or (cert_days and min(cert_days) < CERT_MIN_DAYS) or "不良" in direct_grades:
        verdict, code = "戻さない", 1
        if "不良" in direct_grades:
            reasons.append(f"直接の経路が遅い・取れない（不良 {direct_grades.count('不良')}／{len(direct_grades)}）")
    elif "注意" in direct_grades:
        verdict, code = "戻さない（様子見）", 1
        reasons.append(f"直接の経路がやや遅い（注意 {direct_grades.count('注意')}／{len(direct_grades)}）。時間をおいて2回以上良好なら戻す")
    else:
        verdict, code = "戻してよい", 0
        reasons.append("直接の経路はすべて良好")
    print(f"  → {verdict}")
    for x in reasons:
        print(f"    ・{x}")
    if mode.startswith("プロキシ無し"):
        print("    ・（今はプロキシ無し。「戻さない」が続くときは、プロキシを入れるかの判断材料にする）")
    elif out.get("current_note"):
        print(f"    ・（今はプロキシ有り。{out['current_note']}）")
    out["verdict"], out["reasons"] = verdict, reasons
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        print(f"\n保存：{args.json}")
    if args.history:
        from pathlib import Path
        d = Path(args.history)
        d.mkdir(parents=True, exist_ok=True)
        # 秒まで入れ、それでも同じ名前があれば -2・-3 … を付ける（同じ分に2回測っても前の回を上書きしない）
        stem = f"delivery-{started.strftime('%Y%m%d-%H%M%S')}"
        for n in range(1, 100):
            path = d / (f"{stem}.json" if n == 1 else f"{stem}-{n}.json")
            try:
                with open(path, "x", encoding="utf-8") as f:
                    json.dump(out, f, ensure_ascii=False, indent=1)
                break
            except FileExistsError:
                continue
        print(f"\n貯めた：{path}")
        import delivery_report   # 同じ tools/ にある
        print(f"証拠の1ページ：{delivery_report.build(d)}")
    return code


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")   # Windows の既定（cp932）で文字化けさせない
    sys.exit(main())
