---
name: html-safe-edit
description: Safe HTML/CSS/JS editing constraints for hormuz-map / HTML・CSS・JS編集時の安全ルールと既知制約
---

# HTML 安全編集スキル

このスキルは `docs/hormuz/index.html`（ホルムズ海峡危機マップ本体）と `docs/index.html`（媒体トップ＝ハブ）の HTML 構造・CSS・JavaScript・折り畳み表示を編集する際に使用する。

---

## ルートテーブル構造（STATS セクション内）

- **7列構成**：アイコン / ルート / 輸送能力 / 🇯🇵日本向け（`.jf-col`）/ 現況詳細 / 主なリスク / 状態（2026-09-27 実測で記述を直した）
- `<colgroup>` は必ず7列（`<col>` 7個）に保つこと。列追加時は colgroup・nth-child CSS・JS の3箇所を同時更新する。脚注行の `colspan` も7
- **インライン style を書かない**（`<col>` の幅を除く）。「現況詳細」セルは 最新（`p.route-latest`）→ 要点（`p.route-summary`）→ 経緯（`details.route-history`）の型、色は `.t-*`（daily-site-update「ルート表の型」・② PR3）
- `.jf-col` クラスの列はスマホ（768px以下）で `display:none` により自動非表示（2026-09-18 フェーズ2で 860px 以下 → 768px 以下に変更。タブレットは横スクロールで表示）
- `loadRouteTableFlow()` が `oil-flow.json` から `#jf-*-bpd` / `#jf-*-tanker` 要素に値を注入（手動編集不要）。対象は旧ルート（`old`）・A・B・C_US・C_GL・D の6行。`old`・`D` は 0 のとき「停止中」と出す（2026-09-27・#6）
- Route C は `C_US`（米国）と `C_GL`（南半球）の2行に分割済み
- 日本原油調達フロー説明カードへのアンカー `<div id="japan-flow">` が iframe wrapper 直前に設置済み

---

## 折り畳み表示ルール（3件表示統一）

- **速報インシデント**：最新3件常時表示、4件目以降は「過去のインシデントを見る」で折り畳み（`applyIncidentFold()`）。項目は `li.incident-item` の型で書く（daily-site-update スキル「速報インシデントの型」）。ページには直近30日分だけを置き、古い項目は `docs/data/incident_archive.json`
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
- **キーワードの自動の色付け**：`markKeywords()`（同じ script）が、30秒カラムの3行・シナリオの補足・次の焦点の文から、日付・単位つきの数値・被害の語・回復の語・但し書きを正規表現で見つけ、`span.kw-*` で囲む。
  色は控えめにする（クラスは `.kw-num` `.kw-date` `.kw-alert` `.kw-ease` `.kw-hedge`）。対象の区域や語を増やすときは `ZONES` と正規表現を直す。本文に手で印を書かない
- **文章に使う黄色は淡くする**：1文を超える長さの文には `--c-warn-soft`（`#efe2b6`）を使う（例：`.sc-focus-list strong`・`.sc-update-caveat`・`.sc-ctx-note`・ルート表の `.t-warning-soft`）。
  見出し・ラベル・短い印（ルート表の「⚓ 10/9 追記：」やシナリオBの見出し）は `--c-warn`（`#fbbf24`）のまま

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
