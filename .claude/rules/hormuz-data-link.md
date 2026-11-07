---
paths:
  - "docs/hormuz/index.html"
  - "docs/data/**"
---

# hormuz-data- 連携ルール

> 2026-11-07 にルートの `CLAUDE.md` から原文のまま移した（設計書 `tools/claude-md-slim-design.md`）。
> ルートには要点だけを残している。食い違ったら**この文書が正**。

## hormuz-data- 連携ルール

- `hormuz-data-` リポジトリはダッシュボード・自動データの別リポジトリ
- `data/manual-update.json` の `scenario` フィールド（A/B/C/D確率）がシナリオ確率の正として自動同期される
- `syncScenarioFromDashboard()` がページ読み込み時にfetchして確率（`sc-pct-A`〜`D`）・バー・推定の幅・判定日を入れる（手動更新不要）
- fetch URL：`https://yattanda.github.io/hormuz-data-/data/manual-update.json`
- **`hormuz-data-` の `data/oil-flow.json`** が日本原油調達フローの単一ソース（`loadRouteTableFlow()` が `SITE_CONFIG.DASHBOARD_BASE + '/data/oil-flow.json'` をfetchして値を注入）
  - `hormuz-map` 側に `docs/data/oil-flow.json` は**存在しない**。従来の記述は誤りで、実測により訂正した
  - 同ファイルの `updated` はルートテーブルの**基準日表示に直結**する（`jf-basis-date` に注入）。値を更新するときは `updated` も必ず更新する
- **LiveServer では iframe 内容は更新が反映されない**（GitHub Pages URL から読み込むため）。hormuz-data- の変更は push して GitHub Pages 経由で確認すること
