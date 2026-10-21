#!/usr/bin/env bash
# OpenStreetMap の海岸線（natural=coastline）を、範囲ごとのタイルで取得する。
# 使い方: fetch_osm.sh <出力フォルダ>
out="$1"; mkdir -p "$out"; cd "$out" || exit 1
MIRRORS=("https://overpass-api.de/api/interpreter" "https://overpass.private.coffee/api/interpreter" "https://overpass.kumi.systems/api/interpreter")
UA="chokepointlab-map-prototype/0.1 (https://chokepointlab.com)"
TILES=(
 "gulf_1 21.7,47.3,26.3,54.7" "gulf_2 26.3,47.3,30.9,54.7" "gulf_3 21.7,54.7,26.3,62.1" "gulf_4 26.3,54.7,30.9,62.1"
 "red_1 11.0,32.0,16.2,38.8" "red_2 11.0,38.8,16.2,45.6" "red_3 16.2,32.0,21.4,38.8" "red_4 16.2,38.8,21.4,45.6"
 "red_5 21.4,32.0,26.6,38.8" "red_6 21.4,38.8,26.6,45.6" "red_7 26.6,32.0,31.8,38.8" "red_8 26.6,38.8,31.8,45.6"
 "panama_1 6.9,-81.1,10.1,-76.9"
 "malacca_1 0.4,96.4,3.8,104.9" "malacca_2 3.8,96.4,7.1,104.9"
 "tsugaru_1 40.2,139.2,42.3,142.0"
)
# SPLIT=n を付けると、取れていない区画を n×n に分けて <区画>_<行><列>.json で取る。
# 大きい区画は取得元で時間切れ（504・500）になりやすく、1度四方なら数秒〜数十秒で通った（2026-10-16）
SPLIT="${SPLIT:-1}"; JOBS=()
for t in "${TILES[@]}"; do
  name="${t%% *}"; bb="${t#* }"
  if [ -s "$name.json" ] && head -c 200 "$name.json" | grep -q '"version"'; then echo "$name skip (have)"; continue; fi
  if [ "$SPLIT" = 1 ]; then JOBS+=("$name $bb"); continue; fi
  IFS=, read -r s w n e <<<"$bb"
  for i in $(seq 0 $((SPLIT-1))); do for j in $(seq 0 $((SPLIT-1))); do
    JOBS+=("${name}_${i}${j} $(awk -v s="$s" -v w="$w" -v n="$n" -v e="$e" -v i="$i" -v j="$j" -v k="$SPLIT" \
      'BEGIN{dy=(n-s)/k; dx=(e-w)/k; printf "%.4f,%.4f,%.4f,%.4f", s+i*dy, w+j*dx, s+(i+1)*dy, w+(j+1)*dx}')")
  done; done
done
for t in "${JOBS[@]}"; do
  name="${t%% *}"; bb="${t#* }"; f="$name.json"
  if [ -s "$f" ] && head -c 200 "$f" | grep -q '"version"'; then echo "$name skip (have)"; continue; fi
  ok=0
  for try in 1 2 3 4 5 6; do
    m="${MIRRORS[$(( (try-1) % ${#MIRRORS[@]} ))]}"
    code=$(curl -sS -m 420 -A "$UA" -H "Accept: application/json" -o "$f.part" -w "%{http_code}" \
      --data-urlencode "data=[out:json][timeout:360][maxsize:1073741824];way[\"natural\"=\"coastline\"]($bb);out geom qt;" "$m" 2>/dev/null)
    if [ "$code" = "200" ] && head -c 200 "$f.part" | grep -q '"version"' && tail -c 50 "$f.part" | grep -q '}'; then
      mv "$f.part" "$f"; echo "$name ok $(stat -c %s "$f") bytes via $m (try $try)"; ok=1; break
    fi
    echo "$name fail http $code via $m (try $try)"; rm -f "$f.part"; sleep 25
  done
  [ "$ok" = 1 ] || echo "$name GAVE UP"
  [ "$SPLIT" = 1 ] && sleep 10 || sleep 3
done
echo DONE
