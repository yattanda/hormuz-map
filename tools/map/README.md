# 地図の背景のデータを作る道具

`/hormuz/` の地図の背景（課題46 D3 PR 6a・2026-10-21）は、CARTO のタイルを使わず、`docs/data/map/` のデータだけで描く。
描くのは `docs/assets/js/basemap.js`、色は `docs/assets/css/tokens.css` の `--map-*`。設計と経緯は `tools/site-redesign-design.md` §4-2。

ここの道具は、2026-10-12〜10-16 の試作で使ったものを移した（もとは private の下書き `hormuz-ops/drafts/design/tools/`）。中身は変えていない。

## できるファイル（`docs/data/map/`）

| ファイル | 中身 | 作る道具 |
|---|---|---|
| `land.json` | 国の面。湾岸・紅海まわりの18か国は Natural Earth 10m の無加工、ほかは `docs/data/countries.geojson` のまま。`properties.i` が国の2文字 | `ne_build.py` |
| `islands.json` | 小さな島（範囲の中だけ） | `ne_build.py` |
| `places.json` | 都市（全世界）。`[経度, 緯度, 日本語名, min_zoom, scalerank, 人口, 首都か（2＝国の首都・1＝州都など・0）]`。名前は本文の表記に読み替える（設計書 §4-2「都市名の読み替えの表」。`ne_build.py` の `RENAME`） | `ne_build.py` |
| `rivers.json`・`lakes.json` | 川と湖。全世界は大きなものだけ、範囲の中は全部 | `ne_build.py` |
| `osm-<範囲>.json` | 細かい海岸線（OpenStreetMap）の陸地の面・国境・範囲の枠。範囲は `gulf`・`red`・`panama`・`malacca`・`tsugaru` | `osmd_extract.py` → `osm_build2.py` |
| `regions.json` | 細かい海岸線の範囲の枠だけ（`basemap.js` が、どの範囲を読むかを決めるのに使う） | 下の手順 4 |

## 作り直す手順

作業用のフォルダはリポジトリの外に置く（元のデータは合わせて約 1 GB）。Python は `-I` を付けて、道具のあるフォルダから実行しない。

1. Natural Earth 10m（パブリックドメイン。`https://github.com/nvkelso/natural-earth-vector` の `geojson/`）から5つを取る：
   `ne_10m_admin_0_countries.geojson`・`ne_10m_minor_islands.geojson`・`ne_10m_populated_places.geojson`・`ne_10m_rivers_lake_centerlines.geojson`・`ne_10m_lakes.geojson`
2. 国の面・島・都市・川・湖：
   `python -I tools/map/ne_build.py <Natural Earth のフォルダ> docs/data/countries.geojson <出力フォルダ>`
3. 細かい海岸線：
   1. osmdata.openstreetmap.de の海岸線一式 `coastlines-split-4326.zip`（約 925 MB・ODbL）を取る
   2. `python -I tools/map/osmd_extract.py <zip> <作業フォルダ>` で範囲ごとに切り出す（zip は展開しない。線の向きを OSM と同じに直す）
   3. `python -I tools/map/osm_build2.py <作業フォルダ> <Natural Earth のフォルダ>/ne_10m_admin_0_countries.geojson <出力フォルダ>` で陸地の面にする（間引き 0.0008度・約200 m 四方より小さい島は省く・島ごとに国を決める）
   - `fetch_osm.sh` は、最初に試した Overpass API から取る道具。10/12・10/16 とも 504・500 が続いて取り切れなかったので、いまは使っていない
4. 出力を `docs/data/map/` へ置き、`regions.json` を作り直す（`osm-*.json` の `box` を並べただけのもの）
5. `/hormuz/` を開き、「地点へ移動」の各地点とズーム 3〜10 で見る。コンソールのエラーがないこと

## 範囲を足すとき

`osmd_extract.py` の `BOXES`・`osm_build2.py` の `REGIONS`・`ne_build.py` の `BOXES`（川・湖・島を全部残す範囲）・`basemap.js` の `REG` の4か所を同じにする。

## クレジット

地図の右下に「Natural Earth・© OpenStreetMap contributors」（`docs/hormuz/index.html` の `addAttribution`）。OpenStreetMap 由来のデータ（細かい海岸線・パナマの湖と川）がある間は外さない。
