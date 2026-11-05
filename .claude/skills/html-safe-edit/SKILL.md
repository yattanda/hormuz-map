---
name: html-safe-edit
description: Safe HTML/CSS/JS editing constraints for hormuz-map / HTML・CSS・JS編集時の安全ルールと既知制約
---

# HTML 安全編集スキル

このスキルは `docs/hormuz/index.html`（ホルムズ海峡危機マップ本体。CSS は `docs/assets/css/hormuz.css` と `tokens.css`）と `docs/index.html`（媒体トップ＝ハブ。CSS は `docs/assets/css/hub.css`）の HTML 構造・CSS・JavaScript・折り畳み表示を編集する際に使用する。

---

## ルートテーブル構造（全ルート現況サマリー）

- **2026-11-02（二段表示 PR-B1）から `<table>` ではない。**各ルートは `<details class="route-row" data-item="…">`（6本）。`<summary>` に 色の帯（`route-strip`）・ルート・日本向け・輸送能力1行・要点（`span.route-lead`）＋札・状態の札、開いた中（`div.route-detail`）に 最新・要点・経緯（`route-detail-main`）と 主なリスク・輸送能力の補足（`route-detail-side`）
- 列の見た目は `hormuz.css` の grid（601px 以上。見出しの行 `div.rtable-head` と同じ `grid-template-columns`）。600px 以下はカード。列を足すときは `.rtable-head` の span・各行の `route-cell`・`grid-template-columns`（601〜1023px と 1024px 以上の2か所）を同時に直す。`<colgroup>`・`nth-child` の幅は無くなった
- `<summary>` の中は phrasing content だけ（`span`・`strong`・`small`・`br`）。`div`・`p` を入れない
- **インライン style を書かない**（例外は無くなった）。「最新」の書き方は 最新（`p.route-latest`）→ 要点（`p.route-summary`）→ 経緯（`details.route-history`）の型、色は `.t-*`（daily-site-update「ルート表の型」）
- 「日本向け」はどの幅でも出す（2026-11-02 に 768px 以下で隠す `.jf-col{display:none}` を外した）。欄の見出し `span.route-cell-h` は 601px 以上で見た目だけ隠す（読み上げ用に残す）
- `loadRouteTableFlow()` が `oil-flow.json` から `#jf-*-bpd` / `#jf-*-tanker` 要素に値を注入（手動編集不要。単位 `.jf-unit` は `#jf-*-bpd` と同じ親〈`span.jf-td`〉の中に置く）。対象は旧ルート（`old`）・A・B・C_US・C_GL・D の6行。`old`・`D` は 0 のとき「停止中」と出す（2026-09-27・#6）
- Route C は `C_US`（米国）と `C_GL`（南半球）の2行に分割済み
- 日本原油調達フロー説明カードへのアンカー `<div id="japan-flow">` が iframe wrapper 直前に設置済み

---

## 折り畳み表示ルール（3件表示統一）

- **速報インシデント**：最新3件常時表示、4件目以降は「過去のインシデントを見る」で折り畳み（`applyIncidentFold()`）。各件は件名だけを見せ、押すと本文（読み込み時に `wrapIncidentDetails()` が `<details class="incident-more">` に包む。日次は `<details>` を書かない。2026-11-01）。項目は `li.incident-item` の型で書く（daily-site-update スキル「速報インシデントの型」）。ページには直近30日分だけを置き、古い項目は `docs/data/incident_archive.json`
  - 上ボタン（3件目直後）：その場で折りたたむ（scrollBy 補正でジャンプ抑制）
  - 下ボタン（展開末尾）：押すと上ボタン位置にスムーズスクロール
- **更新履歴**：最新3件（`div.log-recent`）常時表示、4〜10件目は「📂 過去の履歴を見る」で折り畳み（`#log-collapse`）。項目は daily-site-update「更新履歴の型」で書く。`#log-collapse`・`#log-toggle-bottom` の `style="display:none;"` は開閉ボタンの JS が読むので消さない（② PR4a）
- **関連最新ニュース**：最新3件常時表示、4件目以降は「さらに見る」で折り畳み（scrollBy 補正）
- **現地メディア視点**：LIMIT=3（3件表示）
- 折り畳み/展開時にページが飛ぶ場合は必ず scrollBy 補正を入れること

---

## 読みやすさの仕組み（2026-10-11）

- **ティッカーの速さ**：`fitTickerSpeed()`（`</body>` 直前の script）が、文字の長さから一定の速さ（`PX_PER_SEC = 90`）になるよう `animation-duration` を上書きする。
  CSS の `50s` は JS が動かないときの予備。以前は 50 秒固定で、文が長い日ほど速くなり（10/11 は約300px/秒）文字が二重に見えた。速さを変えるときは `PX_PER_SEC` だけを変える
- **キーワードの自動の色付け**：`markKeywords()`（同じ script）が、30秒カラムの4行の全文（`.glance-text`。要点の `.glance-lead` には掛けない）・シナリオの今日の見立てと但し書き・次の焦点の本文から、日付・単位つきの数値・被害の語・回復の語・但し書きを正規表現で見つけ、`span.kw-*` で囲む。
  色は控えめにする（クラスは `.kw-num` `.kw-date` `.kw-alert` `.kw-ease` `.kw-hedge`）。対象の区域や語を増やすときは `ZONES` と正規表現を直す。本文に手で印を書かない
- **用語集のツールチップ**（2026-10-24）：`</body>` の手前の「用語集」の script が `glossary.js` を読み込み、`data-zones` の区域（日次スキルの型の class）に印を付ける。型の class を変えるときは `data-zones` も直す（`validate_daily.py` の `check_glossary_zones()` が WARN）。本文に手で印を書かない
- **色・アイコン・区切り方は、スキル `site-design` の決まり**（2026-10-22・課題46 D3 PR 7b）。黄色を含む状態の色は札（色面）だけに使い、文の色にしない。以前ここにあった「文章に使う黄色は淡く（`--c-warn-soft`）」の決まりは、D3 で状態の色を札だけにしたので外した

## JS が組み立てる HTML（2026-10-12・②' PR E）

- 地図のポップアップ・印・凡例・関連最新ニュース・現地メディア視点は、JS のテンプレートが HTML を組み立てる。**テンプレートにも固定値のインライン style を書かない。**クラスは `docs/assets/css/hormuz.css` の末尾「JS が組み立てる HTML のクラス」にまとめてある（課題46 D2 で `<style>` から移した）
  （軍事レイヤー `.mil-*`／調達先などのポップアップ `.src-pop*`／バッジ `.p-badge--*`／印 `.mk*`／地図上の文字 `.map-label*`／凡例 `.leg-dash--*`／`.news-*`／`.osint-*`）
- style で残してよいのは2種類だけ：計算やデータで決まる値（`${size}`・`${col}`・`news_data.json` が持つ色）と、JS が開閉の状態として読む `display:none;`
- ポップアップを足すときは、見出しに `<div class="p-title">`（色は付けない。文字色の `.tc-*` は D3 PR 7a で外した）、バッジに `<span class="p-badge p-badge--◯">`、小さな注記に `<div class="p-note">` を使う。色はトークンの変数だけで、新しい色は足さない（スキル `site-design`）
- スマホの文字の下限（0.8rem）は、クラスの並び（`.src-pop-body`・`.news-stale-notice` ほか。`.osint-en` は二段表示 PR-C1 で外した）で指定している。以前の属性セレクタ `div[style*="font-size:0.7"]` は外した
- `tools/validate_daily.py` が、テンプレートの固定値のインライン style を WARN で確認する

## スマホ font-size（変更禁止）

`@media (max-width: 768px) { html { font-size: 18px } }` が設定済み。この設定は削除・変更しない。

---

## 既知の未解決問題（対応保留）

- **ルートテーブル スマホ右余白**：`<colgroup>` を変更するとテーブルが崩壊する
  → colgroup を触らない別アプローチで対応すること（現時点では保留）

---

## 禁止事項（スマホ UI 修正）

- 「なんとなく余白を増やす」修正
- 固定幅 px を増やす修正
- PC 表示を壊す修正
- ページごとの場当たり的な CSS 追加
- `!important` の安易な使用
- 表を無理にスマホ幅へ圧縮する修正
