---
name: html-safe-edit
description: Safe HTML/CSS/JS editing constraints for hormuz-map / HTML・CSS・JS編集時の安全ルールと既知制約
---

# HTML 安全編集スキル

このスキルは `docs/index.html` の HTML 構造・CSS・JavaScript・折り畳み表示を編集する際に使用する。

---

## ルートテーブル構造（STATS セクション内）

- **7列構成**：状態 / ルート名 / BPD / タンカー/週 / 備考 / 日本フロー実績 / 同前週比
- `<colgroup>` は必ず7列（`<col>` 7個）に保つこと。列追加時は colgroup・nth-child CSS・JS の3箇所を同時更新する
- `.jf-col` クラスの列はモバイル（600px以下）で `display:none` により自動非表示
- `loadRouteTableFlow()` が `oil-flow.json` から `.jf-*-bpd` / `.jf-*-tanker` 要素に値を注入（手動編集不要）
- Route C は `C_US`（米国）と `C_GL`（南半球）の2行に分割済み
- 日本原油調達フロー説明カードへのアンカー `<div id="japan-flow">` が iframe wrapper 直前に設置済み

---

## 折り畳み表示ルール（3件表示統一）

- **速報インシデント**：最新3件常時表示、4件目以降は「過去のインシデントを見る」で折り畳み
  - 上ボタン（3件目直後）：その場で折りたたむ（scrollBy 補正でジャンプ抑制）
  - 下ボタン（展開末尾）：押すと上ボタン位置にスムーズスクロール
- **関連最新ニュース**：最新3件常時表示、4件目以降は「さらに見る」で折り畳み（scrollBy 補正）
- **現地メディア視点**：LIMIT=3（3件表示）
- 折り畳み/展開時にページが飛ぶ場合は必ず scrollBy 補正を入れること

---

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
