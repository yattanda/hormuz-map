---
name: daily-site-update
description: Daily update workflow for hormuz-map site / ホルムズマップの日次定常更新手順
---

# 日次定常更新スキル

このスキルはホルムズマップの毎日の定常更新作業に使用する。

---

## 作業開始時に必ず実行（省略禁止）

日付を1文字でも書き込む前に、以下を実行して当日の JST を実測する。

```bash
date -u -d '+9 hours' '+%Y-%m-%d %H:%M JST'
```

- 素の `date` は使わない。クラウド環境（Claude Code on the Web）は UTC のため JST と9時間ずれる
- プロンプトに `[現在日時 JST]` が注入されている場合はその値を使ってよい
- セッション開始時に取得した日付を後半で使い回さない（日をまたぐため）

---

## 情報収集（省略禁止）

以下の観測点を**毎回すべて**確認する。
「変化がなさそうだから省略する」をしない。変化がないこと自体が記載事項になるため。

### 毎日必ず叩く検索クエリ

| # | クエリ | 反映先 |
|---|---|---|
| 1 | `ホルムズ海峡 タンカー 通過 足止め 日本` | MAP の SHIP_CONFIG・30秒カラム |
| 2 | `Strait of Hormuz tanker traffic latest` | 同上（英語ソースでの裏取り） |
| 3 | `原油価格 WTI ブレント 最新` | 30秒カラム「海峡の今」 |
| 4 | `イラン 米国 攻撃 最新` | TICKER・速報インシデント・情勢カード |
| 5 | `ホルムズ海峡 封鎖 日本 影響` | シナリオ・日本フロー |
| 6 | `Iran Israel US military latest`（英語） | 情勢カード・シナリオ |
| 7 | 現地メディア（Al Jazeera / Tehran Times 等）の当日記事 | 🌐 現地メディア視点 |

- 検索結果は**必ず日付を確認**する。数か月前の記事が上位に来ることがある
- 1〜2で数値（足止め隻数・通過隻数）に変化がなくても、`dateConfirmed` に調査日時と「変更なし」を記録する

### URL の扱い（絶対ルール）

- **記事URLは検索結果に実際に出たものだけを使う。推測・生成による URL は禁止**
- URL を確認する場合は WebFetch を使う

### WebSearch / WebFetch が失敗するときの確認先

クラウド環境（Claude Code on the Web）のネットワークアクセスは、既定の **Trusted**
（パッケージレジストリ・GitHub のみ）では報道各社のサイトに WebFetch できない。
**2026-09-02 に Full へ変更済み**のため通常は問題ないが、接続エラーが出たらここを最初に疑う。

確認場所：claude.ai/code の新規タスク画面 → 入力欄の上の環境セレクタ（雲アイコン）
→ 「クラウド」にホバー → `Default` の歯車 → **ネットワークアクセス**

同じダイアログの **環境変数**には `TZ=Asia/Tokyo` を設定済み（2026-09-04〜06 に適用）。
これがないとクラウドのシステム時刻が UTC になり、git のコミット時刻が9時間ずれる。

---

## 毎日の定常更新フロー

**このスキルを起動したら、Claude Code がそのまま最後まで実行する。**
差分ファイル（`tools/index_html_diffs.md`）は経由しない。PC・スマホとも手順は同じ。

### 1. 日付を実測する

冒頭の「作業開始時に必ず実行」のとおり。ここで得た JST を以後すべての日付表記に使う。

### 2. 情報収集

上記「情報収集（省略禁止）」の検索クエリ7点をすべて実行する。

### 3. ファイルを直接編集する

後述の「毎日更新の作業順序（厳守）」の番号順に進める。触るのは次の4ファイル。

| ファイル | 内容 |
|---|---|
| `docs/data/news_data.json` | ニュース・OSINT（`latest` 4件・`osint`・`updated`） |
| `docs/index.html` | TICKER・30秒カラム・情勢カード・シナリオ・ヘッダー日時・`dateModified` ほか |
| `docs/data/update_log.json` | 更新ログ（先頭に追記し、index.html 側は最新10件を維持） |
| `docs/data/archive_timeline.json` | 当日分のエントリーを1件追記（速報を出した日のみ） |

- `docs/index.html` を触る前に `/html-safe-edit` の制約を確認する
- 文章表記・メディア選定は `/content-style-guide` に従う

### 4. 自己チェック

`/publish-checklist` の項目を1件ずつ確認する。特に次は毎回外せない。

- 4ファイルすべての日付が**同じ JST 日時**で揃っているか
- `news_data.json` の `latest` が4件・`osint` の `isLatest: true` が1件だけか
- `dateModified` を当日に更新したか

### 5. commit

何を更新したかが履歴だけで分かる文言にする。

```
daily: YYYY年M月D日 HH:MM JST更新——（主な変更点を簡潔に）
```

### 6. push / マージはユーザーの指示を待つ

- **PC（main で作業）**：commit まで。push はユーザーの指示を待つ
- **クラウド（仮想ブランチ）**：仮想ブランチへの push まで。**main へのマージは必ずユーザーの指示を待つ**

---

## 旧フロー（凍結中・2026-09-03 以降未使用）

Claude.ai で `tools/index_html_diffs.md` を生成し、`run.bat` またはスマホの GitHub Web UI で
リポジトリへ反映し、Claude Code が適用する方式。**通常は使わない。**

関連ファイル：`tools/index_html_diffs.md` / `tools/diffs-generation-rules.md` / `tools/run.bat` /
`auto_push.py` / `.github/scripts/apply_diffs.py` / `.github/workflows/mobile-update.yml`

- 上記一式は削除予定。削除の判断がつくまでは残してあるだけで、**新規に使わない**
- やむを得ず使う場合、スマホからの手編集のコミットメッセージは
  `mobile: update index_html_diffs.md (M/D HH:MM JST)` の形式にする
  （GitHub が自動提案する `Change 'Hello World' to 'Goodbye World'` 等をそのまま使わない）

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
12. `archive_timeline.json` への当日分追記（速報を出した日のみ）

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

- `🚢 全ルート現況サマリー` の日付は毎回当日の日時（JST）に更新する
- **日付の場所は見出し内の `<span class="sec-h2-sub">`**。本文は隣の `<p class="sec-lead">`
  （2026-09-05 のフェーズ1a-2 で `div.sec-title` 1要素から2要素に分離した）
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
- **既存ファイルを全面的に書き直さない。**新規追加分をマージする形で編集する
  （`archive` に過去の全バッチが入っており、書き直すと履歴が失われる）
- 新記事を `latest` の先頭へ追加する前に、既存の `isLatest: true` を `false` に戻す

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

## archive_timeline.json 運用ルール

- `docs/archive/index.html`（全記録アーカイブ）は `docs/data/archive_timeline.json` を読み込んで表示する
- 日次更新のたびに、`entries` 配列の**末尾に1日1エントリを追記**する
- **追記のみ。既存エントリーの本文は変更しない**（過去に公開した速報の改変にあたるため）

### エントリーのスキーマ

```json
{
  "date": "YYYY-MM-DD",
  "dateLabel": "YYYY/MM/DD HH:MM",
  "blockadeDay": 143,   // ⚠️ 任意項目・表示には未使用（2026-08-07以降）
  "summary": "（更新ログ本文と同一）",
  "relatedNews": [
    {"title": "...", "url": "...", "sourceLabel": "..."}
  ]
}
```

- `summary` は同日の更新ログ本文と同一の内容にする
- **`blockadeDay` は表示に使用されない（2026-08-07以降）**
  → `docs/archive/index.html` の `calcBlockadeDay()` が `date` から動的に算出するため、
    このフィールドの値はアーカイブページのスタンプ・統計欄のいずれにも反映されない。
  → 既存エントリーとの構造的な整合のため記入は継続してよいが、**値の正確性は問われない**。
  → 記入する場合の正しい値は「2026-02-28 を1日目とした通算日数」
    （例：2026-08-05 → 159）。
- `relatedNews` は本日 `news_data.json` の `latest` に追加した新規記事から転記する（最大5件・タイトル/URL/出典のみ）
- 速報を出さなかった日はエントリーを作成しない（スキップしてよい——アーカイブ側は自動的に「◯日分の速報なし」と表示する）

---

## JSON-LD dateModified の更新（毎回必須）

docs/index.html 内の以下の行を本日のJST日付（YYYY-MM-DD）に更新すること：

  "dateModified": "YYYY-MM-DD",

例：
  "dateModified": "2026-05-21",

※ この行を更新し忘れると、Googleに「更新なし」と判断される。
