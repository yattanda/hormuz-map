import json, io, sys, os
ne, cur, out = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True)
def load(p): return json.load(io.open(p, encoding='utf-8'))
def dump(name, obj):
    p = os.path.join(out, name)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(obj, ensure_ascii=False, separators=(',', ':')))
    print(name, os.path.getsize(p))
def P(f, k):
    pr = f['properties']
    return pr.get(k, pr.get(k.upper(), pr.get(k.lower())))
def rnd(c, n):
    if not c: return c
    if isinstance(c[0], (int, float)): return [round(c[0], n), round(c[1], n)]
    r = [rnd(x, n) for x in c]
    if r and r[0] and isinstance(r[0][0], (int, float)):
        o = [r[0]]
        for q in r[1:]:
            if q != o[-1]: o.append(q)
        return o
    return r
def bbox(g):
    xs = []; ys = []
    def walk(c):
        if not c: return
        if isinstance(c[0], (int, float)): xs.append(c[0]); ys.append(c[1])
        else:
            for x in c: walk(x)
    walk(g['coordinates'])
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None
def hit(b, box): return b is not None and not (b[2] < box[0] or b[0] > box[2] or b[3] < box[1] or b[1] > box[3])
def npts(c): return 0 if not c else (1 if isinstance(c[0], (int, float)) else sum(npts(x) for x in c))

REGION = (30, 8, 70, 35)
# 川・湖・小さな島を全部残す範囲（細かい海岸線に差し替える所のまわり）
BOXES = [REGION, (-82, 6, -76, 11), (95, -1, 106, 8), (138, 39, 143, 43)]
def inreg(b): return any(hit(b, x) for x in BOXES)
DETAIL = set('IR IQ KW SA BH QA AE OM YE EG SD ER DJ SO JO IL PS PK'.split())

# 1) 国の面：湾岸・紅海まわりの国だけ Natural Earth 10m の無加工、ほかは今のファイルのまま
raw = load(os.path.join(ne, 'ne_10m_admin_0_countries.geojson'))
now = load(cur)
rawby = {}
for f in raw['features']:
    iso = P(f, 'ISO_A2_EH')
    if iso in (None, '-99'): iso = P(f, 'ISO_A2')
    rawby.setdefault(iso, f)
feats = []; det_pts = 0; used = 0
for f in now['features']:
    iso = f['properties'].get('ISO3166-1-Alpha-2')
    g = f['geometry']; d = 0
    if iso in DETAIL and iso in rawby:
        g = {'type': rawby[iso]['geometry']['type'], 'coordinates': rnd(rawby[iso]['geometry']['coordinates'], 3)}
        d = 1; used += 1; det_pts += npts(g['coordinates'])
    feats.append({'type': 'Feature', 'properties': {'i': iso, 'd': d}, 'geometry': g})
print('detail countries', used, 'points', det_pts, 'total points', sum(npts(f['geometry']['coordinates']) for f in feats))
dump('land.json', {'type': 'FeatureCollection', 'features': feats})

# 2) 小さな島（範囲内だけ）
mi = load(os.path.join(ne, 'ne_10m_minor_islands.geojson'))
isl = [{'type': 'Feature', 'properties': {}, 'geometry': {'type': f['geometry']['type'], 'coordinates': rnd(f['geometry']['coordinates'], 3)}}
       for f in mi['features'] if inreg(bbox(f['geometry']))]
print('islands in region', len(isl))
dump('islands.json', {'type': 'FeatureCollection', 'features': isl})

# 3) 都市：全世界。 [経度, 緯度, 日本語名, min_zoom, scalerank, 人口, 首都か（2＝国の首都・1＝州都など・0）]
# 名前はサイトの本文の表記に合わせて読み替える（設計書 §4-2「都市名の読み替えの表」・2026-10-16）
RENAME = {'フジャイラ市': 'フジャイラ', 'マナーマ': 'マナマ', 'ジッダ': 'ジェッダ', 'アーバーダーン': 'アバダン', 'アハマディ': 'アフマディ',
          'シャールジャ': 'シャルジャ', 'バンダレ・アッバース': 'バンダルアッバース', 'ブーシェフル': 'ブシェール'}
pl = load(os.path.join(ne, 'ne_10m_populated_places.geojson'))
rows = []
for f in pl['features']:
    x, y = f['geometry']['coordinates'][:2]
    cla = (P(f, 'featurecla') or '').lower()
    name = P(f, 'name_ja') or P(f, 'name')
    rows.append([round(x, 3), round(y, 3), RENAME.get(name, name), round(P(f, 'min_zoom') or 9, 1), P(f, 'scalerank'), int(P(f, 'pop_max') or 0),
                 2 if cla.startswith('admin-0 capital') else 1 if 'capital' in cla else 0])
dump('places.json', rows)

# 4) 川：全世界は大きな川だけ、範囲内は全部
rv = load(os.path.join(ne, 'ne_10m_rivers_lake_centerlines.geojson'))
rf = []
for f in rv['features']:
    if not f['geometry']: continue
    inr = inreg(bbox(f['geometry'])); sr = P(f, 'scalerank') or 0
    if inr or sr <= 5:
        rf.append({'type': 'Feature', 'properties': {'s': sr, 'n': P(f, 'name') or ''},
                   'geometry': {'type': f['geometry']['type'], 'coordinates': rnd(f['geometry']['coordinates'], 3 if inr else 2)}})
print('rivers kept', len(rf), 'points', sum(npts(f['geometry']['coordinates']) for f in rf))
dump('rivers.json', {'type': 'FeatureCollection', 'features': rf})

# 5) 湖：全世界は大きな湖だけ、範囲内は全部
lk = load(os.path.join(ne, 'ne_10m_lakes.geojson'))
lf = []
for f in lk['features']:
    if not f['geometry']: continue
    inr = inreg(bbox(f['geometry'])); sr = P(f, 'scalerank') or 0
    if inr or sr <= 4:
        lf.append({'type': 'Feature', 'properties': {'s': sr, 'n': P(f, 'name_ja') or P(f, 'name') or ''},
                   'geometry': {'type': f['geometry']['type'], 'coordinates': rnd(f['geometry']['coordinates'], 3 if inr else 2)}})
print('lakes kept', len(lf), 'points', sum(npts(f['geometry']['coordinates']) for f in lf))
dump('lakes.json', {'type': 'FeatureCollection', 'features': lf})
print('river names in region:', sorted({f['properties']['n'] for f in rf if f['properties']['n'] and hit(bbox(f['geometry']), (40, 20, 62, 38))})[:40])
