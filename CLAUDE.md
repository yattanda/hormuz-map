# hormuz-map 運用ルール

## プロジェクト概要

- `docs/index.html` 1ファイルにHTML・CSS・JavaScript全て集約
- `docs/data/news_data.json` がニュース・OSINT表示の単一ソース
- `docs/images/` ディレクトリにインフォグラフィック画像を管理
- ※目標・URL・運用状況は `Memory.md` を参照

## 絶対ルール

- コメントアウトタイトル `<!-- xxxx -->` は変更しない
- ニュースのURLは必ずユーザー提供のもののみ使用（AI捏造禁止）
- 更新対象セクション以外は触らない
- タイムスタンプの日付は必ずユーザーが明示したものを使用する。未明示の場合は作業前に確認する

## Git操作ルール

- commit後のpushは必ずユーザーの指示を待ってから実行する
- 自動pushは行わない

## 運用ツール

- Claude Code：`docs/index.html` 更新・commit担当（pushはユーザー確認後）
- `auto_push.py` / `run.bat`：`news_data.json` と `index_html_diffs.md` を Downloads フォルダから GitHub API で直接 push
- GenSpark：参照用アーカイブのみ（更新しない）

## hormuz-data- 連携ルール

- `hormuz-data-` リポジトリはダッシュボード・自動データの別リポジトリ
- `data/manual-update.json` の `scenario` フィールド（A/B/C/D確率）がシナリオ確率の正として自動同期される
- `syncScenarioFromDashboard()` がページ読み込み時にfetchして `sc-tag-A/B/C/D` を上書き（手動更新不要）
- fetch URL：`https://yattanda.github.io/hormuz-data-/data/manual-update.json`
- `docs/data/oil-flow.json` が日本原油調達フローの単一ソース（`loadRouteTableFlow()` がfetchして値を注入）
- **LiveServer では iframe 内容は更新が反映されない**（GitHub Pages URL から読み込むため）。hormuz-data- の変更は push して GitHub Pages 経由で確認すること

## 専門エージェント

- `mobile-ui-reviewer`：スマホ表示の問題発見・レビュー（コード編集なし）
- `responsive-css-specialist`：CSS修正・レスポンシブ実装

## スマホ font-size（変更禁止）

`@media (max-width: 768px) { html { font-size: 18px } }` は削除・変更しない。

## Memory.mdとの役割分担

- `CLAUDE.md`（このファイル）：Claude Code向け **運用ルール・技術制約のみ**
- `Memory.md`：Claude.ai向け **引き継ぎ・現状・課題・完了履歴**
- CLAUDE.md には「何をすべきか（ルール）」のみ記載し、「現状・経緯」は書かない

## Project Skills の使い分け

以下の作業に該当する場合は、該当する Project Skill を優先して使用する。

| スキル | 使うタイミング |
|---|---|
| `/daily-site-update` | 毎日の定常更新作業 |
| `/html-safe-edit` | HTML/CSS/JSの構造・テーブル・折り畳み表示を触るとき |
| `/content-style-guide` | ニュース記事・メディア選定・文章表記の確認 |
| `/publish-checklist` | 更新完了前・commit前・push前の最終チェック |
| `/feature-extension-plan` | 新機能・スマホUI・レスポンシブ改善・構造変更の前 |
| `/resolve-news-data-conflict` | git rebase中にconflictが発生したとき |

`/publish-checklist` と `/resolve-news-data-conflict` は、原則としてユーザーが明示的に呼び出した場合のみ使用する。
