"""OpenStreetMap の海岸線（Overpass の out geom・複数タイル）から、範囲ごとの陸地の面を作る。
使い方: python -I osm_build2.py <タイルのフォルダ> <ne_10m_admin_0_countries.geojson> <出力フォルダ> [範囲名 ...]
海岸線の向きは「進行方向の左が陸」。範囲の縁は反時計回りにたどって閉じる。"""
import json, io, sys, os, math, glob
tiles, nec, out = sys.argv[1], sys.argv[2], sys.argv[3]
only = sys.argv[4:]
os.makedirs(out, exist_ok=True)
# 範囲（西, 南, 東, 北）。取得したタイルより 0.1度 内側に置く
REGIONS = {
    'gulf':    (47.4, 21.8, 61.5, 30.8),
    'red':     (32.1, 11.1, 45.5, 31.7),
    'panama':  (-81.0, 7.0, -77.0, 10.0),
    'malacca': (96.5, 0.5, 104.8, 7.0),
    'tsugaru': (139.3, 40.3, 141.9, 42.2),
}
TOL = 0.0008              # およそ 80〜90m より細かい凹凸を省く
MINA = 0.002 ** 2         # およそ 200m 四方より小さい島を省く

def dp(pts, tol):
    if len(pts) < 3: return pts
    keep = [False] * len(pts); keep[0] = keep[-1] = True; st = [(0, len(pts) - 1)]
    while st:
        i, j = st.pop(); ax, ay = pts[i]; bx, by = pts[j]; dx, dy = bx - ax, by - ay; L = dx * dx + dy * dy
        m = -1; md = tol * tol
        for k in range(i + 1, j):
            px, py = pts[k]
            if L == 0: d = (px - ax) ** 2 + (py - ay) ** 2
            else:
                t = ((px - ax) * dx + (py - ay) * dy) / L; t = 0 if t < 0 else 1 if t > 1 else t
                d = (px - ax - t * dx) ** 2 + (py - ay - t * dy) ** 2
            if d > md: md = d; m = k
        if m >= 0: keep[m] = True; st.append((i, m)); st.append((m, j))
    return [p for p, k in zip(pts, keep) if k]
def area(r): return abs(sum(r[i][0] * r[i + 1][1] - r[i + 1][0] * r[i][1] for i in range(len(r) - 1))) / 2
def km(a, b): return math.hypot((b[0] - a[0]) * math.cos(math.radians((a[1] + b[1]) / 2)) * 111.32, (b[1] - a[1]) * 110.57)

ne = json.load(io.open(nec, encoding='utf-8'))

# 島（範囲の中で閉じた輪）ごとに国を決める。Natural Earth の国の面の中ならその国、外なら いちばん近い国。
# 試作ページは「粗い国の形から 2.5km 以内」を国の色に塗るので、それより沖の島は国の色にならない（2026-10-16 に確認）。島は自分の国の色で塗る
def pip(x, y, r):
    c = False
    for i in range(len(r) - 1):
        (x1, y1), (x2, y2) = r[i][:2], r[i + 1][:2]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: c = not c
    return c
def seg_km(p, a, b):
    k = math.cos(math.radians(p[1])); dx, dy = (b[0] - a[0]) * k, b[1] - a[1]
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, ((p[0] - a[0]) * k * dx + (p[1] - a[1]) * dy) / L))
    return km(p, (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
def interior(r):
    ys = sorted(q[1] for q in r); y = (ys[0] + ys[-1]) / 2; xs = []
    for i in range(len(r) - 1):
        (x1, y1), (x2, y2) = r[i], r[i + 1]
        if (y1 > y) != (y2 > y): xs.append((x2 - x1) * (y - y1) / (y2 - y1) + x1)
    xs.sort()
    return max(((xs[i + 1] - xs[i], ((xs[i] + xs[i + 1]) / 2, y)) for i in range(0, len(xs) - 1, 2)), default=(0, r[0]))[1]
def island_country(rings, box, margin=1.5):
    W, S_, E, N = box; cs = []
    for f in ne['features']:
        iso = f['properties'].get('ISO_A2_EH')
        for poly in ([f['geometry']['coordinates']] if f['geometry']['type'] == 'Polygon' else f['geometry']['coordinates']):
            xs = [q[0] for q in poly[0]]; ys = [q[1] for q in poly[0]]
            if max(xs) < W - margin or min(xs) > E + margin or max(ys) < S_ - margin or min(ys) > N + margin: continue
            cs.append((iso, poly, (min(xs), min(ys), max(xs), max(ys))))
    res = []
    for r in rings:
        p = interior(r); c = None
        for iso, poly, bb in cs:
            if bb[0] <= p[0] <= bb[2] and bb[1] <= p[1] <= bb[3] and pip(p[0], p[1], poly[0]) and not any(pip(p[0], p[1], h) for h in poly[1:]):
                c = iso; break
        if c is None:
            best = 1e9
            for iso, poly, bb in cs:
                if p[0] < bb[0] - margin or p[0] > bb[2] + margin or p[1] < bb[1] - margin or p[1] > bb[3] + margin: continue
                for q in poly:
                    for i in range(len(q) - 1):
                        a, b = q[i], q[i + 1]
                        if abs(a[0] - p[0]) > margin and abs(b[0] - p[0]) > margin: continue
                        if abs(a[1] - p[1]) > margin and abs(b[1] - p[1]) > margin: continue
                        d = seg_km(p, a, b)
                        if d < best: best = d; c = iso
        res.append(c or '')
    return res

def build(name, box):
    W, S_, E, N = box
    els = {}
    for f in sorted(glob.glob(os.path.join(tiles, name + '_*.json'))):
        for e in json.load(io.open(f, encoding='utf-8'))['elements']:
            if e['type'] == 'way' and len(e.get('nodes', [])) > 1: els[e['id']] = e
    els = list(els.values())
    if not els: print(name, 'NO DATA'); return
    print('==', name, 'ways', len(els), 'points', sum(len(e['nodes']) for e in els))
    first = {}
    for i, e in enumerate(els): first.setdefault(e['nodes'][0], i)
    lasts = {e['nodes'][-1] for e in els}
    used = [False] * len(els); chains = []
    def follow(i):
        pts = []; closed = False; start = els[i]['nodes'][0]
        while i is not None and not used[i]:
            used[i] = True; e = els[i]
            g = [(p['lon'], p['lat']) for p in e['geometry']]
            pts.extend(g if not pts else g[1:])
            if e['nodes'][-1] == start: closed = True; break
            i = first.get(e['nodes'][-1])
        return pts, closed
    for i, e in enumerate(els):
        if not used[i] and e['nodes'][0] not in lasts: chains.append(follow(i))
    for i in range(len(els)):
        if not used[i]: chains.append(follow(i))
    def inside(p): return W <= p[0] <= E and S_ <= p[1] <= N
    def cross(a, b):
        best = None; dx, dy = b[0] - a[0], b[1] - a[1]
        for (axis, val) in ((0, W), (0, E), (1, S_), (1, N)):
            d = dx if axis == 0 else dy
            if d == 0: continue
            t = (val - a[axis]) / d
            if 0 <= t <= 1:
                x, y = a[0] + dx * t, a[1] + dy * t
                if W - 1e-9 <= x <= E + 1e-9 and S_ - 1e-9 <= y <= N + 1e-9:
                    if best is None or t < best[0]: best = (t, (min(max(x, W), E), min(max(y, S_), N)))
        return best[1] if best else None
    pieces = []; rings = []; warn = 0
    for pts, closed in chains:
        if closed and all(inside(p) for p in pts): rings.append(pts); continue
        if closed:
            k = next((i for i, p in enumerate(pts) if not inside(p)), 0)
            pts = pts[k:-1] + pts[:k + 1]
        cur = None
        if inside(pts[0]): warn += 1; print('  warn: chain starts inside box at', pts[0])
        for i in range(len(pts) - 1):
            a, b = pts[i], pts[i + 1]; ia, ib = inside(a), inside(b)
            if not ia and ib:
                c = cross(a, b); cur = [c, b] if c else None
            elif ia and ib:
                if cur is not None: cur.append(b)
            elif ia and not ib:
                c = cross(b, a)
                if cur is not None and c: cur.append(c); pieces.append(cur)
                cur = None
        if cur is not None: warn += 1; print('  warn: chain ends inside box at', cur[-1])
    raw_pts = sum(len(p) for p in pieces) + sum(len(r) for r in rings)
    pieces = [dp(p, TOL) for p in pieces]
    r2 = []
    for r in rings:
        if area(r) < MINA: continue
        h = len(r) // 2; s = dp(r[:h + 1], TOL) + dp(r[h:], TOL)[1:]
        if len(s) >= 4: r2.append(s)
    Wd, Hd = E - W, N - S_; PER = 2 * (Wd + Hd)
    def tpar(p):
        x, y = p; e = 1e-7
        if abs(y - S_) < e: return x - W
        if abs(x - E) < e: return Wd + (y - S_)
        if abs(y - N) < e: return Wd + Hd + (E - x)
        if abs(x - W) < e: return 2 * Wd + Hd + (N - y)
        return None
    CORN = [(Wd, (E, S_)), (Wd + Hd, (E, N)), (2 * Wd + Hd, (W, N)), (PER, (W, S_))]
    ok = [p for p in pieces if len(p) > 1 and tpar(p[0]) is not None and tpar(p[-1]) is not None]
    ts = [tpar(p[0]) for p in ok]
    polys = []; done = [False] * len(ok)
    for i0 in range(len(ok)):
        if done[i0]: continue
        ring = []; i = i0
        while True:
            done[i] = True; ring.extend(ok[i]); cur = tpar(ok[i][-1])
            j = min(range(len(ok)), key=lambda k: ((ts[k] - cur) % PER) or PER)
            gap = ((ts[j] - cur) % PER) or PER
            ring.extend(cp for _, cp in sorted(((ct - cur) % PER, cp) for ct, cp in CORN if 0 < (ct - cur) % PER < gap))
            if j == i0: break
            if done[j]: warn += 1; print('  warn: ring closed on used piece'); break
            i = j
        ring.append(ring[0]); polys.append(ring)
    rd = lambda r: [[round(x, 4), round(y, 4)] for x, y in r]
    isl = island_country(r2, box)
    feats = [{'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Polygon', 'coordinates': [rd(p)]}} for p in polys] + \
            [{'type': 'Feature', 'properties': {'i': c}, 'geometry': {'type': 'Polygon', 'coordinates': [rd(p)]}} for p, c in zip(r2, isl)]
    kept = sum(len(p) for p in polys) + sum(len(r) for r in r2)
    seg = sorted(km(p[i], p[i + 1]) for p in pieces for i in range(len(p) - 1))
    # 国境（Natural Earth の国の面で、2か国が共有する辺）
    edges = {}
    for f in ne['features']:
        iso = f['properties'].get('ISO_A2_EH')
        for poly in ([f['geometry']['coordinates']] if f['geometry']['type'] == 'Polygon' else f['geometry']['coordinates']):
            for r in poly:
                for i in range(len(r) - 1):
                    a, b = (round(r[i][0], 4), round(r[i][1], 4)), (round(r[i + 1][0], 4), round(r[i + 1][1], 4))
                    if not (inside(a) and inside(b)): continue
                    edges.setdefault((a, b) if a < b else (b, a), set()).add(iso)
    bl = [[list(a), list(b)] for (a, b), s in edges.items() if len(s) >= 2]
    obj = {'box': [W, S_, E, N], 'land': {'type': 'FeatureCollection', 'features': feats},
           'borders': {'type': 'Feature', 'properties': {}, 'geometry': {'type': 'MultiLineString', 'coordinates': bl}}}
    p = os.path.join(out, 'osm-%s.json' % name)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(obj, ensure_ascii=False, separators=(',', ':')))
    print('  chains', len(chains), 'pieces', len(ok), 'mainland', len(polys), 'islands', len(r2), 'of', len(rings),
          '| points', raw_pts, '->', kept, '| median km %.3f' % (seg[len(seg) // 2] if seg else 0), '| borders', len(bl), '| bytes', os.path.getsize(p), '| warnings', warn)
    print('  island countries', {c: isl.count(c) for c in sorted(set(isl))})

ov = os.environ.get('OSM_BOX')          # 試験用：'gulf:53.6,24.1,58.4,27.5' のように範囲を上書き
if ov:
    k, vals = ov.split(':'); REGIONS[k] = tuple(float(x) for x in vals.split(','))
for name, box in REGIONS.items():
    if only and name not in only: continue
    build(name, box)
