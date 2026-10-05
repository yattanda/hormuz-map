#!/usr/bin/env python3
"""ハブ（docs/index.html）の「4つの海の要衝」の地図を、同梱の国境データから静的な SVG に書き出す。

設計：tools/s11-10-design.md D7。実行時の JS・Leaflet・外部読み込みを使わず、
docs/data/countries.geojson（Natural Earth・ODC-PDDL）を正距円筒図法で簡略化して
インライン SVG にする。地名は <text> なので検索・読み上げの対象になる。

使い方：
    python tools/build_hub_map.py            # SVG を標準出力へ（dry-run。ファイルは変えない）
    python tools/build_hub_map.py --write    # docs/index.html の目印の間を書き換える

目印：<!-- hub-map:start --> と <!-- hub-map:end -->
地点を足すときは POINTS に1行足して --write で書き直す。
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEOJSON = ROOT / "docs" / "data" / "countries.geojson"
HUB = ROOT / "docs" / "index.html"
START, END = "<!-- hub-map:start -->", "<!-- hub-map:end -->"

# 描く範囲（経度・緯度）と縮尺（1度あたりの px）
LON0, LON1 = -125.0, 150.0
LAT0, LAT1 = -38.0, 62.0
SCALE = 3.0
W, H = (LON1 - LON0) * SCALE, (LAT1 - LAT0) * SCALE

TOLERANCE = 0.45   # 簡略化の許容差（度）
MIN_AREA = 1.2     # これより小さい多角形（平方度）は描かない

# name, 経度, 緯度, ラベルの位置（dx, dy, text-anchor）, リンク先（無ければ None）
POINTS = [
    ("パナマ運河", -79.7, 9.1, (0, -16, "middle"), None),
    ("スエズ運河", 32.3, 30.6, (-12, -14, "end"), None),
    ("ホルムズ海峡", 56.3, 26.6, (16, -16, "start"), "hormuz/"),
    ("マラッカ海峡", 101.0, 2.5, (0, 34, "middle"), None),
]


def project(lon: float, lat: float) -> tuple[float, float]:
    return (lon - LON0) * SCALE, (LAT1 - lat) * SCALE


def simplify(pts: list, tol: float) -> list:
    """Douglas-Peucker（再帰を使わない版）。"""
    if len(pts) < 3:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        ax, ay = pts[a]
        bx, by = pts[b]
        dx, dy = bx - ax, by - ay
        norm = (dx * dx + dy * dy) ** 0.5
        far, idx = 0.0, -1
        for i in range(a + 1, b):
            px, py = pts[i]
            if norm == 0:
                d = ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5
            else:
                d = abs(dy * px - dx * py + bx * ay - by * ax) / norm
            if d > far:
                far, idx = d, i
        if far > tol and idx > 0:
            keep[idx] = True
            stack.append((a, idx))
            stack.append((idx, b))
    return [p for p, k in zip(pts, keep) if k]


def area(pts: list) -> float:
    s = 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        s += x1 * y2 - x2 * y1
    return abs(s) / 2


def rings(geom: dict):
    if geom["type"] == "Polygon":
        yield geom["coordinates"][0]
    elif geom["type"] == "MultiPolygon":
        for poly in geom["coordinates"]:
            yield poly[0]


def land_path() -> str:
    data = json.loads(GEOJSON.read_text(encoding="utf-8"))
    parts = []
    for feat in data["features"]:
        for ring in rings(feat["geometry"]):
            pts = [(float(p[0]), float(p[1])) for p in ring]
            lons = [p[0] for p in pts]
            lats = [p[1] for p in pts]
            if max(lons) < LON0 or min(lons) > LON1 or max(lats) < LAT0 or min(lats) > LAT1:
                continue
            if area(pts) < MIN_AREA:
                continue
            pts = simplify(pts, TOLERANCE)
            if len(pts) < 4:
                continue
            xy = [project(*p) for p in pts]
            parts.append("M" + "L".join(f"{x:.0f},{y:.0f}" for x, y in xy) + "Z")
    return "".join(parts)


def build_svg() -> str:
    out = [
        START,
        f'<svg class="hub-map-svg" viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-labelledby="hub-map-title hub-map-desc" xmlns="http://www.w3.org/2000/svg">',
        '  <title id="hub-map-title">4つの海の要衝の位置</title>',
        '  <desc id="hub-map-desc">世界地図の上に、パナマ運河・スエズ運河・ホルムズ海峡・マラッカ海峡の位置を示す。ホルムズ海峡はホルムズ海峡危機マップへのリンク。</desc>',
        f'  <rect class="hub-map-sea" width="{W:.0f}" height="{H:.0f}"/>',
        f'  <path class="hub-map-land" d="{land_path()}"/>',
    ]
    for name, lon, lat, (dx, dy, anchor), href in POINTS:
        x, y = project(lon, lat)
        cls = "hub-map-point hub-map-point--live" if href else "hub-map-point"
        body = [
            f'<circle class="hub-map-ring" cx="{x:.0f}" cy="{y:.0f}" r="14"/>' if href else "",
            f'<circle class="hub-map-dot" cx="{x:.0f}" cy="{y:.0f}" r="7"/>',
            f'<text class="hub-map-label" x="{x + dx:.0f}" y="{y + dy:.0f}" text-anchor="{anchor}">{name}</text>',
        ]
        inner = "".join(b for b in body if b)
        if href:
            out.append(f'  <a href="{href}" class="{cls}" aria-label="{name}——ホルムズ海峡危機マップを開く">{inner}</a>')
        else:
            out.append(f'  <g class="{cls}">{inner}</g>')
    out += ["</svg>", END]
    return "\n".join(out)


def main() -> int:
    svg = build_svg()
    if "--write" not in sys.argv:
        sys.stdout.reconfigure(encoding="utf-8")
        print(svg)
        print(f"\n(dry-run) {len(svg.encode('utf-8'))} bytes。書き込むには --write", file=sys.stderr)
        return 0
    raw = HUB.read_bytes()
    nl = b"\r\n" if b"\r\n" in raw else b"\n"
    s, e = raw.find(START.encode()), raw.find(END.encode())
    if s < 0 or e < 0 or e < s:
        print(f"NG: {HUB} に目印 {START} … {END} がありません", file=sys.stderr)
        return 1
    new = raw[:s] + svg.encode("utf-8").replace(b"\n", nl) + raw[e + len(END):]
    new.decode("utf-8")
    tmp = HUB.with_suffix(".html.tmp")
    tmp.write_bytes(new)
    os.replace(tmp, HUB)
    print(f"OK: {HUB.relative_to(ROOT)} の地図を書き換えました（{len(svg.encode('utf-8'))} bytes）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
