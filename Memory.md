# Memory.md — ホルムズ海峡危機マップ 引き継ぎドキュメント

最終更新: 2026-05-07（本日作業反映済み）

---

## プロジェクト概要

- **サイト**: https://yattanda.github.io/hormuz-map/
- **構成**: `docs/index.html`（HTML/CSS/JS全集約）+ `docs/data/news_data.json`
- **更新頻度**: 毎日〜数日に1回
- **目標**: マネタイズ（Xインプレッション収益 → YouTube+AI連携へ拡張）

---

## 現在の状態

- **最終更新完了**: 2026年5月5日分 ✅（pull済）
- **公開中**: GitHub Pages で稼働中

---

## 現在進行中の課題（優先順位順）

### 🟡 重要（順次対応）

#### 1. ~~出典・更新ログの整理~~ ✅ 完了（2026-05-07）
- 2カラム統合・最新3件常時表示・4件目以降折り畳み実装済み
- 全27件を `docs/data/update_log.json` に切り出し、index.htmlは最新10件のみ保持

#### 2. hormuz-data- フッター余白・スマホ空白（未解決・対応保留）
- **現状**:
  - デスクトップ: `min-height:100vh` 削除後にfooterが半行分クリップされる
  - スマホ: フッター付近に約10行分の空白が残る（`min-height` 削除前から存在）
- **診断状況**: コードのみでは原因特定できず。実機確認が必要
  - footer CSSには `padding:16px 20px; margin-top:10px; line-height:1.8` が設定済み
  - スマホ空白の原因候補: grid/card-footerのパディング累積、JS生成ルート行の高さ、iOSセーフエリア等
- **次回の対応案**:
  - デスクトップ: `footer` に `padding-bottom:24px` または `body` に `padding-bottom:8px` を追加
  - スマホ: ブラウザのDevToolsで実測してから対応。`@media(max-width:768px)` に `footer { padding-bottom:8px; margin-top:4px; }` を試す

#### 3. スマホUI改善（継続課題）

**現状の問題点**:
- スマホ表示で余白が広すぎる箇所がある（`margin-bottom` / `gap` / `padding` の過剰）
- 見出しサイズが画面幅に対して大きすぎる場合がある
- セクション間の間延びがある
- 表の列幅がスマホで最適化されにくい
- Claudeの修正が試行錯誤になりやすかった（→ 専用エージェント・ルールで解決済み）

**採用する改善方針**:
- 375pxを最重要基準として確認する
- モバイルファーストでCSSを整理する
- 見出し・余白には `clamp()` を優先する
- 表は横スクロールまたはカード型を基本にする
- 共通CSSで直せるものを優先し、ページ固有の場当たり的CSSを増やさない
- 修正時は `mobile-ui-reviewer` → `responsive-css-specialist` の順で進める
- 詳細ルールは `docs/design-system.md` / `docs/mobile-ui-rules.md` を参照

#### 4. インフォグラフィック導線改善
- **対象**: 30秒カラム末尾の「📊 解説インフォグラフィック」→「ホルムズ海峡危機を6枚の図解で俯瞰する」
- **問題**: タイトルの色が地味、大タイトルからの導線が不明瞭
- **方針**: タイトル色を青系（`#38bdf8` or `#43d9ff`）に変更、ボタン/バナーとして視認性強化

---

### 🟢 機能追加（余裕があれば）

#### 4. キーワードツールチップ
- **概要**: 重要キーワード上にカーソルオン（スマホはタップ）で簡潔な解説ポップアップ
- **対象語例**: ホルムズ海峡、OPEC、Kpler、CENTCOM、OFAC、BPD 等
- **実装方針**: CSS `position:relative` + `::after` または `<span data-tooltip="...">` + JSで制御
- **スマホ対応**: タップで表示・もう一度タップで非表示

---

## 保留中の課題

### ⏸️ ルートテーブル スマホ右余白
- `<colgroup>` を変更するとテーブルが崩壊することを確認済み
- 複数回試みたが未解決 → 次回は colgroup を触らない別アプローチで検討

---

## 今後の最重要課題（次フェーズ）

- **更新作業の自動化**（現在は手動）
  - news_data.json の自動生成
  - index_html_diffs.md の自動生成
  - Claude Code への自動適用
- **Xへの投稿自動化**（別スレッドで対応中）

---

## 完了済み主要作業

- ✅ サブエージェント作成（mobile-ui-reviewer / responsive-css-specialist）（2026-05-07）
- ✅ デザイン基準書・スマホUIルール作成（docs/design-system.md / docs/mobile-ui-rules.md）（2026-05-07）
- ✅ CLAUDE.mdにスマホUI改善ルール・専門エージェント使い分けを追記（2026-05-07）
- ✅ Memory.md 新規作成・Claude.aiプロジェクト知識連携（2026-05-06）
- ✅ スマホフォントサイズ底上げ（`@media (max-width:768px) { html { font-size:18px } }`）（2026-05-06）
- ✅ 速報インシデント・関連最新ニュース・現地メディア視点 折り畳み整備（各3件表示統一）（2026-05-06）
- ✅ 現地メディア視点 LIMIT 4→3 に変更（2026-05-06）
- ✅ ホルムズ海峡危機マップ 公開・毎日更新運用中
- ✅ news_data.json による動的ニュースレンダリング実装
- ✅ auto_push.py / run.bat による半自動push体制構築
- ✅ syncScenarioFromDashboard() によるシナリオ確率自動同期
- ✅ インフォグラフィック6枚 公開
- ✅ MAP凡例折り畳み（スマホ対応）
- ✅ ルートテーブル7列構成 + 日本フロー列
- ✅ 2026年5月5日分まで更新完了

---

## 環境メモ

- **OS**: Windows 11（Macなし）
- **ffmpeg パス**: `C:\ffmpeg\bin\ffmpeg.exe`（PATH未設定環境対応）
- **Python**: venv 使用 → `venv\Scripts\python`
- **Claude.ai**: 戦略・情報収集・差分ファイル生成
- **Claude Code**: index.html更新・commit（pushはユーザー確認後）
- **auto_push.py**: DownloadsフォルダからGitHub API直接push

---

## セッション再開コマンド

```
前回のセッションを再開して
```
