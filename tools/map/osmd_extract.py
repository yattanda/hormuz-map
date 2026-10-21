"""osmdata.openstreetmap.de の海岸線一式（coastlines-split-4326.zip）から、範囲ごとの海岸線を切り出し、
Overpass の out geom と同じ形（way・nodes・geometry）で書き出す。osm_build2.py がそのまま読める。
使い方: python -I osmd_extract.py <coastlines-split-4326.zip> <出力フォルダ> [範囲名 ...]
- Overpass が混んで取れなかったための別の経路（2026-10-16）。zip は展開せずに読む
- 線の向きは逆にして、OSM と同じ（進行方向の左が陸）にそろえる。線の端は隣の線の端と同じ座標なので、座標から点の番号を作ってつなぐ
- 出力は <範囲名>_osmd.json。Overpass の区画（<範囲名>_1.json など）と同じフォルダに置かない（番号の付け方が違う）"""
import io, json, os, struct, sys, zipfile
src, out = sys.argv[1], sys.argv[2]
only = sys.argv[3:]
os.makedirs(out, exist_ok=True)
# 取得する範囲（西, 南, 東, 北）。osm_build2.py の範囲より 0.1度 外側（fetch_osm.sh の区画の外枠と同じ）
BOXES = {
    'gulf':    (47.3, 21.7, 62.1, 30.9),
    'red':     (32.0, 11.0, 45.6, 31.8),
    'panama':  (-81.1, 6.9, -76.9, 10.1),
    'malacca': (96.4, 0.4, 104.9, 7.1),
    'tsugaru': (139.2, 40.2, 142.0, 42.3),
}
BOXES = {k: v for k, v in BOXES.items() if not only or k in only}

z = zipfile.ZipFile(src)
shp = next(n for n in z.namelist() if n.endswith('.shp'))
ways = {k: [] for k in BOXES}
nid = {}
def node(x, y):
    k = (round(x, 7), round(y, 7))
    if k not in nid: nid[k] = len(nid) + 1
    return nid[k]
n = 0
with z.open(shp) as f:
    f.read(100)                                   # ファイルの見出し
    while True:
        h = f.read(8)
        if len(h) < 8: break
        rec, words = struct.unpack('>ii', h)
        body = f.read(words * 2); n += 1
        st = struct.unpack('<i', body[:4])[0]
        if st != 3: continue                       # 3 = 折れ線
        x0, y0, x1, y1 = struct.unpack('<4d', body[4:36])
        hit = [k for k, (W, S, E, N) in BOXES.items() if x1 >= W and x0 <= E and y1 >= S and y0 <= N]
        if not hit: continue
        np_, npt = struct.unpack('<ii', body[36:44])
        parts = list(struct.unpack('<%di' % np_, body[44:44 + 4 * np_])) + [npt]
        pts = struct.unpack('<%dd' % (2 * npt), body[44 + 4 * np_:44 + 4 * np_ + 16 * npt])
        for a, b in zip(parts[:-1], parts[1:]):
            # この一式の線は OSM と逆向き（陸が右）。島の輪が右回りになっていた（2026-10-16 に Overpass の区画と比べて確認）ので、逆にする
            xy = [(pts[2 * i], pts[2 * i + 1]) for i in range(b - 1, a - 1, -1)]
            if len(xy) < 2: continue
            w = {'type': 'way', 'id': rec * 100 + len(ways[hit[0]]) % 100,
                 'nodes': [node(x, y) for x, y in xy],
                 'geometry': [{'lat': round(y, 7), 'lon': round(x, 7)} for x, y in xy]}
            for k in hit: ways[k].append(w)
print('records', n)
for k, els in ways.items():
    for i, w in enumerate(els): w['id'] = i + 1          # 範囲の中で番号を振り直す（重複を避ける）
    p = os.path.join(out, k + '_osmd.json')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(
        {'version': 0.6, 'generator': 'osmd_extract.py (' + os.path.basename(src) + ')', 'elements': els},
        separators=(',', ':')))
    print(k, 'ways', len(els), 'points', sum(len(w['nodes']) for w in els), 'bytes', os.path.getsize(p))
