# hormuz-map 運用ルール

## プロジェクト概要
- index.html 1ファイルにHTML・CSS・JavaScript全て集約
- `data/news_data.json` がニュース・OSINT表示の単一ソース
- `images/` ディレクトリにインフォグラフィック画像を管理
- GitHub Pages で公開済み
- 更新頻度：毎日〜数日に1回

## 絶対ルール
- コメントアウトタイトル <!-- xxxx --> は変更しない
- 日付は必ず JST 表示、フォーマットは `YYYY年MM月DD日 HH:MM 日本時間JST` で統一する（例：2026年4月19日 12:00 日本時間JST）
- 利用可メディア：AP通信・ロイター・ブルームバーグ・AFP・アルジャジーラ・産経・テレビ東京・フジテレビ
- 利用不可メディア：朝日・NHK・東京新聞・テレビ朝日・TBS（日本メディアのみ対象）
- 利用可否不明の海外メディアは利用可として扱う
- ニュースのURLは必ずユーザー提供のもののみ使用（AI捏造禁止）
- シナリオは最大4つまで（確度最低のものを削除）
- スマホ最適化を常に意識
- 更新対象セクション以外は触らない

## セクション構成（順番固定）
- /* TICKER */　← 毎日更新
- <!-- 30秒で全体像を把握 --> ← 毎日更新
  - 末尾に「📊 解説インフォグラフィック」サムネイルブロックあり（クリックでライトボックス拡大）
  - 画像ファイルは `images/` に配置。追加時は `openLightbox('images/xxx.png')` を参照
- <!-- SITUATION CARDS --> ← 毎日更新
- <!-- COUNTDOWN --> ← 適宜更新
- <!-- 💰 リアルタイム市場ダッシュボード --> ← 通常変更なし
- <!-- MAP --> ← 適宜更新
  - MAP内の `// 日本関連タンカー足止め可視化` オーバーレイを毎回更新する：
    - 日本船の足止め数・通過数を最新情報に更新
    - 変更がない場合もチェックした日時（JST）を必ず記載する
- <!-- STATS --> ← 週1更新
- <!-- 速報インシデント トグルボタン --> ← 毎日更新
- <!-- SCENARIOS --> ← 毎日更新
  - 各sc-tagには `id="sc-tag-A"` / `id="sc-tag-B"` / `id="sc-tag-C"` / `id="sc-tag-D"` が付与済み
  - シナリオはA（外交妥結）・B（停戦膠着）・C（全面衝突）・D（軍事エスカレーション）の4種
  - ページ読み込み時に `syncScenarioFromDashboard()` が hormuz-data- から確率を自動上書きする
  - **確率補足バナー・sc-tagの確率数値は手動更新不要**（自動同期が優先）。ただし文面の矢印（↑↓）や補足テキストは手動で情勢に合わせて更新する
- <!-- シナリオ フッター --> ← 毎日更新
- <!-- 特別解説コラム --> ← 手動指示時のみ
- <!-- NEWS COLUMN --> ← 毎日更新
- <!--🌐 現地メディア視点--> ← 毎日更新
- <!--出典・更新ログ--> ← 毎日更新
- <!-- 数値注記 --> ← 適宜更新

## COUNTDOWNセクションのルール
- カウントダウンの期限時刻は日本時間（JST）を基準とする
- 表示には必ず「日本時間JST」と明記する
- 米国時間（ET）も併記する場合は「日本時間JST」を先に・主として表示する

## Git操作ルール
- commit後のpushは必ずユーザーの指示を待ってから実行する
- 自動pushは行わない

## メディア掲載ルール
- 「📰 関連最新ニュース」カラムに現地中東系メディアは使用不可
- 現地中東系メディア＝（例）PressTV（イラン国営）、Al Arabiya（サウジ系）、The National（UAE系）、Al Jazeera（カタール系）等
- これらの現地中東系メディアは「🌐 現地メディア視点」カラムにのみ掲載可

## 運用方針
- Claude.ai Project：戦略・設計・相談担当
- Claude Code：コード実装・git push 担当
- GitHub 公式連携：完全自動化フェーズで実施予定
- マネタイズ：現状は X 投稿によるインプレッション収益
- GenSpark：参照用アーカイブのみ（更新しない）

## hormuz-data- 連携ルール
- `hormuz-data-` リポジトリ（`https://yattanda.github.io/hormuz-data-/`）はダッシュボード・自動データの別リポジトリ
- `data/manual-update.json` の `scenario` フィールド（A/B/C/D確率）がシナリオ確率の正として自動同期される
- hormuz-map/index.html の `syncScenarioFromDashboard()` がページ読み込み時にfetchして `sc-tag-A/B/C/D` を上書き
- hormuz-data- の fetch URL：`https://yattanda.github.io/hormuz-data-/data/manual-update.json`
- hormuz-data- を直接編集する場合は別途 git push が必要（hormuz-map とは独立）

## news_data.json 運用ルール
- `data/news_data.json` がニュース・OSINT表示の単一ソース（index.htmlのNEWS COLUMN・現地メディア視点はJSで動的レンダリング）
- 毎日の更新は `data/news_data.json` のみを編集する（index.htmlのNEWS COLUMNセクションは触らない）
- `latest` に最新4件を掲載。追加時は最古の1件を `archive` の先頭バッチへ移動する
- `archive` は更新バッチ単位（`label` 付き）で管理。1バッチ10件前後が目安
- `osint` は各メディア1件ずつ。`isLatest: true` は最新記事1件のみに付与（複数不可）
- `updated` フィールドは `YYYY年MM月DD日 HH:MM 日本時間JST` 形式で必ず更新

## 作業方針
- 変更前に対象セクションを明示する
- 変更箇所以外は絶対に触らない
- 編集後に差分を簡潔に要約する
- URLを伴うニュースはユーザー入力のURLのみ採用
- 毎回の更新時に `<header>` 内の以下を必ず更新する：
  - 警戒レベル表示（例：🚨 警戒レベル：最高）← 情勢に応じて変更
  - 更新日時表示（例：📅 2026年4月17日 11:12 JST）← 当日のJST時刻に更新
- タイムスタンプの日付は必ずユーザーがプロンプトで明示したものを使用する
- Claudeが自動推測した日付は使わない
- 日付が明示されていない場合は作業前にユーザーに確認する
- 関連最新ニュースおよび現地メディア視点の記事日付は、現地時間とJST（日本標準時）の両方を記載する

## 毎日更新の作業順序（厳守）
1. `data/news_data.json` を更新（latest差し替え・旧latestをarchiveへ・osint更新・updatedフィールド更新）
2. `index.html` — ヘッダー日時・警戒レベル更新
3. `index.html` — TICKERテキスト更新
4. `index.html` — 「30秒で全体像を把握」セクション（いま何が・海峡の今・バッジ5枚）更新
5. `index.html` — SITUATION CARDS 3枚（本文・出典）更新
6. `index.html` — COUNTDOWN ラベル更新（HTMLとJS両方）
7. `index.html` — 速報インシデント更新
8. `index.html` — シナリオ確率補足バナー（矢印・説明文・タイムスタンプ）更新
9. `index.html` — シナリオ本文（必要な場合のみ）更新
10. `index.html` — シナリオ フッター タイムスタンプ更新
11. `index.html` — 更新ログ先頭にエントリ追加
12. JSONバリデーション（`python -m json.tool data/news_data.json`）
13. `git commit`（メッセージに日時・主な変更を記載）
14. ユーザーの push 指示を待つ

## 更新完了チェックリスト
- [ ] `news_data.json` — `updated` フィールドを今回のJST日時に更新した
- [ ] `news_data.json` — `latest` 4件を差し替え、旧latestを archive 先頭バッチに移動した
- [ ] `news_data.json` — `osint` の `isLatest:true` は最新1件のみである
- [ ] `index.html` — ヘッダー badge-date を今回のJST日時に更新した
- [ ] `index.html` — TICKERコメント行の日時を更新した
- [ ] `index.html` — 「いま何が」「海峡の今」・バッジ5枚を更新した
- [ ] `index.html` — SITUATION CARDS 3枚の本文・出典を更新した
- [ ] `index.html` — COUNTDOWN ラベルを HTML・JS 両方更新した
- [ ] `index.html` — 速報インシデントを更新した
- [ ] `index.html` — シナリオ確率バナーのタイムスタンプ・矢印・説明文を更新した
- [ ] `index.html` — シナリオ フッターのタイムスタンプを更新した
- [ ] `index.html` — 更新ログ先頭に新エントリを追加した
- [ ] JSONバリデーションがエラーなし
- [ ] `git commit` 済み（push はユーザー指示待ち）
