---
name: daily-site-update
description: Daily update workflow for hormuz-map site / ホルムズマップの日次定常更新手順
---

# 日次定常更新スキル

このスキルはホルムズマップの毎日の定常更新作業に使用する。

---

## 毎日の定常更新フロー

1. Claude.ai で最新情報収集・`index_html_diffs.md` を生成（news_data.json は生成しない）
2. `index_html_diffs.md` をダウンロード
3. `run.bat` をダブルクリック（index_html_diffs.md のみ push）
   └ 「完了: 1/1 ファイル push成功」を確認してウィンドウを閉じる
4. Claude Code に以下の定型文を送る：
   「docs/tools/index_html_diffs.md に従って docs/index.html を更新してください。
    docs/data/news_data.json は [S10] の指示に従い、既存ファイルに対して
    新規追加分をマージする形で更新してください。
    更新完了後に commit してください。push は確認後に指示します。」
5. 内容確認後、push を指示

---

## 毎日更新の作業順序（厳守）

抜け漏れ防止のため、以下の順番で作業する。順番を変えない。

1. 最新情報収集（Web 検索・複数ソース確認）
2. `docs/data/news_data.json` 更新（latest 4件・osint）
3. 速報インシデント 更新
4. 速報ティッカー（TICKER）決定
5. 情勢カード（SITUATION CARDS）更新
6. COUNTDOWN 更新
7. 4つのシナリオ内容決定（1〜6を踏まえて初めて書く）
8. シナリオフッター 更新
8.5. **全ルート現況サマリー 更新**（S08完了後・30秒カラムの直前）
9. **30秒カラム（3行サマリー＋ステータスバッジ）― 必ず最後に書く**
   └ 全セクションの総括のため、他が確定してから書くこと
10. ヘッダー（日時・警戒レベル）更新
11. 更新ログ 追記

---

## セクション構成と更新頻度

| セクション識別子 | 更新頻度 | 備考 |
|---|---|---|
| `/* TICKER */` | 毎日 | |
| `<!-- 30秒で全体像を把握 -->` | 毎日 | 末尾にインフォグラフィックブロックあり |
| `<!-- SITUATION CARDS -->` | 毎日 | |
| `<!-- COUNTDOWN -->` | 適宜 | |
| `<!-- 💰 リアルタイム市場ダッシュボード -->` | 通常変更なし | |
| `<!-- MAP -->` | 適宜 | タンカー可視化オーバーレイを毎回確認 |
| `<!-- STATS -->` | 週1 | |
| `<!-- 速報インシデント トグルボタン -->` | 毎日 | |
| `<!-- SCENARIOS -->` | 毎日 | sc-tag-A/B/C/D の確率は自動同期 |
| `<!-- シナリオ フッター -->` | 毎日 | |
| `<!-- 特別解説コラム -->` | 手動指示時のみ | |
| `<!-- NEWS COLUMN -->` | 毎日 | |
| `<!--🌐 現地メディア視点-->` | 毎日 | |
| `<!--出典・更新ログ-->` | 毎日 | |
| `<!-- 数値注記 -->` | 適宜 | |

### セクション補足

- **インフォグラフィック画像**：`docs/images/` に配置。追加時は `openLightbox('images/xxx.png')` を参照（引数は `index.html` からの相対パス）
- **MAPタンカー可視化**：毎日、作業前に「日本関係船舶 ホルムズ海峡 通過 足止め」等を web 検索し、足止め数・通過数の変化を調査すること（省略禁止）。変化あり時は SHIP_CONFIG（totalShips・passableShips・date・dateConfirmed）を全て更新。変化なし時も dateConfirmed に調査日時（JST）と「変更なし」を記録すること。
- **シナリオ確率**：ページ読み込み時に `syncScenarioFromDashboard()` が hormuz-data- から自動上書きするため手動更新不要。ただし矢印（↑↓）や補足テキストは手動で情勢に合わせて更新する
- **sc-tag の確率表示**：styled な HTML スパン（`innerHTML`）で構成されている。`textContent` で上書きすると装飾が消えるため **必ず `innerHTML` を使うこと**

---

## COUNTDOWN セクションのルール

- カウントダウンの期限時刻は日本時間（JST）を基準とする
- 表示には必ず「日本時間JST」と明記する
- 米国時間（ET）も併記する場合は「日本時間JST」を先に・主として表示する

---

## ヘッダーの毎回更新項目

毎回の更新時に `<header>` 内の以下を必ず更新する：

- 警戒レベル表示（例：🚨 警戒レベル：最高）← 情勢に応じて変更
- 更新日時表示（例：📅 2026年4月17日 11:12 JST）← 当日の JST 時刻に更新

---

## 表記ルール（日次作業用）

### ルール1：全ルート現況サマリーの日付

- `🚢 全ルート現況サマリー（...）` の日付は毎回当日の日時（JST）に更新する
- ルート情報に変更がない週も日付を更新し末尾に「再確認済」を付ける
- 形式：変更あり → `YYYY年MM月DD日 HH:MM JST 更新` ／ 変更なし → `YYYY年MM月DD日 HH:MM JST 再確認済`

### ルール2：TICKER 内の日付

- TICKER 内の日付には必ず「JST」を付ける
- 例：`4/30 09:51 JST` ← OK　`4/30` のみ ← NG

### ルール3：膠着日の表記

情勢に大きな変化がない日は、TICKER の末尾に以下を追記する：
「｜📋 MM/DD HH:MM JST 確認済——新たな進展なし（膠着継続）」
進展があった日はこの行は不要（追加しない）。

---

## news_data.json 運用ルール

- `docs/data/news_data.json` がニュース・OSINT 表示の単一ソース（NEWS COLUMN・現地メディア視点は JS で動的レンダリング）
- 毎日の更新は `docs/data/news_data.json` のみを編集する（`docs/index.html` の NEWS COLUMN セクションは触らない）
- `latest` に最新4件を掲載。追加時は最古の1件を `archive` の先頭バッチへ移動する
- `archive` は更新バッチ単位（`batchLabel` 付き）で管理。1バッチ10件前後が目安
- `osint` は各メディア1件ずつ。`isLatest: true` は最新記事1件のみに付与（複数不可）
- `updated` フィールドは `YYYY年MM月DD日 HH:MM 日本時間JST` 形式で必ず更新
- Claude.ai は news_data.json を単体ファイルとして生成しない
- 新規追加分は index_html_diffs.md の [S10] に記載し、Claude Code がマージする
- run.bat（auto_push.py）は news_data.json を push しない

### 必須フィールド

`latest` / `archive.items` の各アイテムは以下の6フィールドが必須：
`title`・`body`・`sourceLabel`・`date`・`label`・`url`

旧フィールド名（`headline`・`summary`・`source`・`date_local`・`date_jst`・`tags`）は使用禁止。
`archive` のバッチキーは `batchLabel`（旧 `label` は使用禁止）。

### osint アイテムの必須フィールド

`titleJa`・`titleEn`・`country`・`media`・`cardBg`・`cardBorder`・`badgeColor`・`borderColor`・`textColor`・`url`・`date`

### staleNotice フィールド

- 新情報がない日：`"MM/DD HH:MM JST 確認済——最新ニュースなし（膠着継続中）"`
- 新情報がある日：`"staleNotice": ""` （空文字）

---

## update_log.json 運用ルール

- `docs/data/update_log.json` が更新ログの完全アーカイブ
- 形式：`[{"date":"YYYY/MM/DD HH:MM","text":"..."},...]`（新しい順）
- `index.html` の `<!--出典・更新ログ-->` セクションは**常に最新10件のみ**掲載する
  - 常時表示：最新3件 ／ 折り畳み（`log-collapse`）：4〜10件目
  - 出典リンク①〜⑧は折り畳み末尾に固定（削除しない）
- 毎日の更新時に新エントリを1件追加したら、`index.html` から11件目を削除し、その内容を `update_log.json` の先頭に追加する
- `update_log.json` の編集は `index.html` の更新と同じ commit に含める

## JSON-LD dateModified の更新（毎回必須）

docs/index.html 内の以下の行を本日のJST日付（YYYY-MM-DD）に更新すること：

  "dateModified": "YYYY-MM-DD",

例：
  "dateModified": "2026-05-21",

※ この行を更新し忘れると、Googleに「更新なし」と判断される。
