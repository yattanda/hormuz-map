# ② 本体 設計書：セクション統合（S03・S04→S09・S08.5→ルート表）＋#6＋#14

- 作成：2026-09-24（ゲート B 成立済み・ブランチ `redesign/phase2-sections`）
- 正本：`tools/redesign-plan.md` §3（A案・統合対象）・§4「10/2 以降に回したもの」（#14）・§7（#6）、
  作業順案（chokepointlab-notes `10月以降の作業順_案.md` §3-1：② 本体＝セクション統合＋S03・S08.5＋#6。#1・#2(a)・#3・#5 は ②'）
- 状態：**v4**（2026-10-01：PR4b を 4b-1・4b-2 に分割＝E9）。v3（2026-09-29：PR4 を 4a・4b に分割＝E8）。v2（2026-09-27：U2 決定、#14 の区域外を PR4 に分離）。§6 の未決は各 PR の着手時に詰める

---

## 0. 決定事項（2026-09-24 運営者判断）

| # | 論点 | 決定 |
|---|---|---|
| E1 | 速報インシデントの古い項目（212件・4月分まで） | **直近30日だけ残す**。外した項目は `docs/data/incident_archive.json` へ退避（ページからはリンクしない・URL は増やさない）。以後の退避は日次ではなく**月1回まとめて**行う |
| E2 | 情勢カード（実数8枚）の吸収形 | **30秒カラムに「主な動き」を見出し＋出典で3件**。本文は速報インシデントに一本化し重複をなくす |
| E3 | ルート表「現況詳細」セルに溜まった経緯 | **`<details>` で折りたたむ**（内容は削除しない） |
| E4 | 進め方 | ブランチ `redesign/phase2-sections`・**PR 3本**（§3）。各 PR はその日の日次更新の後にマージ |
| E5 | 30日より古いインシデントの本文 | JSON へ退避（E1）。git の履歴だけに頼る案は不採用 |
| E6 | ルート表の脚注の古い数値（2026-09-27） | **PR3 で整理**。「各列：5月22日更新」は実態と違うので削り、5月の概況（充足率65〜70%を含む）は `<details>`「5月22日時点の概況」へ移す（消さない）。貿易統計ベースの推計とは算出方法・時点が違うことを注記。推計の%は月次で変わるので数値は書かない |
| E7 | #14 の区域外の残り（2026-09-27） | **PR4 に分ける**。PR3 はルート表・S08.5・#6 と表の中のインライン style まで |
| E8 | PR4 の分け方（2026-09-29） | **PR4a と PR4b に分ける**。PR4a＝日次が書き込む区域（シナリオ S06〜S08・更新履歴）をスキルの型・validate と一緒にクラス化し、翌朝の日次で型を確かめる。PR4b＝日次が触らない残り（OSINT・その他の検討中ルート・STATS・モーダルほか）と属性セレクタ・`#jf-td-*` の重複の撤去 |
| E9 | PR4b の分け方（2026-10-01） | **PR4b-1 と PR4b-2 に分ける**（残り220か所・style の種類141通りで、1本では見た目の比較を確実にできないため）。PR4b-1＝本文の区域（その他の検討中ルート・主要指標・特別解説コラムのカード・第3層の外枠・数値の注記）。PR4b-2＝部品（トランプ声明のモーダルと比較ブロック・製油所モーダル・TradingView・動画導線・インフォグラフィック・ヘッダー周り）と、属性セレクタ・`#jf-td-*` の重複の撤去。ブランチは `redesign/phase2-pr4b1`・`redesign/phase2-pr4b2` |

---

## 1. 前提の訂正：日次更新の本流は「直接編集」

2026-09-23 の引き継ぎは「日次差分の `old_str`（`apply_diffs.py` の完全一致）が外れるのでクラスを足せない」を制約としていたが、
**日次更新は 2026-09-03 以降、クラウドの Claude Code が `docs/index.html` を直接編集している**
（`.claude/skills/daily-site-update/SKILL.md`「毎日の定常更新フロー」・Memory.md「移行後の定着状況」）。
`tools/index_html_diffs.md`＋`apply_diffs.py`＋`mobile-update.yml` は**手動実行のバックアップ経路**で、差分ファイルは 9/2 版のまま。

したがって構造変更の制約は次の3つ（確度：高）。

1. **スキルの型**：クラウドの日次更新は既存の HTML をまねて書き足す。スキルに新しい型（クラス付きの HTML）を書かないと、翌日から古いインライン style が戻る
2. **`tools/validate_daily.py`**：`PAT_TICKER`（実体は S03 の日付バッジ `📅 M/D HH:MM 更新`）、`PAT_ROUTES`（最初に一致する日付付き `sec-h2-sub`＝S08.5 見出し）、ルート表の `jf-td-*` 行の鮮度チェック
3. **CSS**：インライン style の文字列に一致させている属性セレクタ（`[style*="font-size:0.95rem"]`・`div[style*="font-size:0.7"]`・`[style*="display:flex;flex-wrap:wrap;gap:8px;"]`）と `#incident > strong`

バックアップ経路の `tools/diffs-generation-rules.md` も、構造を変えた PR で同時に直す（使う日に壊れていないように）。

---

## 2. 現状（2026-09-24 実測）

| 区域 | 行数 | インライン font-size | 要点 |
|---|---|---|---|
| S09 30秒カラム | 148 | 32 | `href="#situation"`（空アンカー）へのリンクあり |
| S03 速報インシデント | 1,062 | 91 | `#incident-list` に項目212（`<li>` の style が8種類以上混在）。`applyIncidentFold()` が先頭3件を残して `#incident-extra` へ移す。先頭の `<strong>` 要約5本は一覧と重複 |
| S04 情勢カード | 69 | 0 | 文書は「3枚」だが実数8枚。本文は速報インシデントとほぼ同文。`#situation` は空の `div` |
| S05 COUNTDOWN | 41 | 2 | 地図スクリプト（`updateCountdown()` の即時実行）より上に置く必要あり |
| S08.5＋ルート表 | 302 | 34 | サマリーは【外交】【船舶インシデント】【中央航路】【南側航路】【代替輸送路】【市場】の6分類で、表の行（旧・B・A・C🇺🇸・C🌍・D）と1対1に対応しない。日次更新はすでに行のセルにも「M/D JST追記」を足している |
| シナリオ S06〜S08 | 78 | 22 | ② では構造を変えず、クラス化のみ |

- `docs/index.html` の `<body>` 内のインライン font-size：**309か所・35種類**
- 30日より古い項目149件のうち、`archive_timeline.json` に同じ日付の項目があるのは109件。ただし archive は日次の要約（平均約240字）で、**インシデント本文そのものは残らない**（→ E1・E5 で JSON へ退避）
- 食い違っている記述：S03 の目印コメント（HTML は全角空白 `速報インシデント　トグルボタン`、文書は半角）、`<!-- ROUTE TABLE -->` が `#incident` の直上にある、「情勢カード3枚」、html-safe-edit スキルのルート表の説明

---

## 3. PR の分割

各 PR に次を**必ず同梱**する：担当区域の HTML・CSS・JS、`validate_daily.py`、`daily-site-update` スキル（型の例）、
`diffs-generation-rules.md`（バックアップ経路）、`publish-checklist`・`html-safe-edit` スキルの該当記述。
マージは**その日の日次更新のコミットが main に入った後**。翌朝の日次更新が新しい型で通ったことを確認してから次の PR をマージする。

### PR1：S03 速報インシデントの作り直し

- 先頭の `<strong>` 要約5本を廃止（一覧の先頭と重複）。トグル見出し部（見出し・最新の件名・日付バッジ）は残す
- 項目の型を1つにする：
  ```html
  <li class="incident-item incident-item--danger">
    <span class="incident-tag">⚓ 9/21 現地・攻撃主体不明</span>
    <span class="incident-body">本文……</span>
  </li>
  ```
  色の種類（`#f87171`・`#fbbf24`・`#4ade80` など）はモディファイアクラスにする。既存の `div.incident-item` と li の混在も解消
- 直近30日（2026-08-25 以降）だけ残す（E1）。外した項目は `docs/data/incident_archive.json`（日付・タグ・本文・出典）へ退避。
  日付が `M/D` で書かれていない24件は、すべて「2026年5月30日」形式の4〜5月の項目（実測）
- `applyIncidentFold()` は `#incident-list` の子要素を数えるだけなので**変更不要**（実装時に確認）
- `validate_daily.py` の `PAT_TICKER` はバッジの文字（`📅 M/D HH:MM 更新`）だけを見るので**変更不要**。バッジの文字の形は変えない。`#incident > strong` の CSS は撤去
- 目印コメントの全角空白を文書側と揃える。`<!-- ROUTE TABLE -->` を正しい位置へ

### PR2：情勢カード（S04）を30秒カラム（S09）へ吸収

- `<!-- SITUATION CARDS -->` の見出しと `.sit-grid` を廃止し、30秒カラムの3行サマリーの下に「主な動き」を置く（E2）：
  見出し＋日付＋出典の3件（新しい順）。各行は `#incident` の該当項目へのリンク（項目に id を付けるかは §6 U3）
- `href="#situation"` のボタンを「主な動き」または `#incident` へ付け替え。空の `div#situation` は削除
- S05 COUNTDOWN は現位置のまま（地図スクリプトより上）。クラス化のみ
- 日次の作業順序：旧「5. 情勢カード」は「9. 30秒カラム」に統合（S04 を欠番にする）
- 30秒カラムの属性セレクタ（`[style*="font-size:0.95rem"]` 等）をクラスへ置換

### PR3：S08.5 をルート表へ分解＋#6

- 見出し `🚢 全ルート現況サマリー` と `sec-h2-sub` の日付は**表の基準日として残す**（`PAT_ROUTES` が参照）
- 長文の `<p class="sec-lead">` を廃止。6分類の行き先：
  - 【中央航路】【南側航路】【代替輸送路】→ 該当する表の行の「現況詳細」先頭の「最新（M/D）」1行（対応表は §6 U2）
  - 【外交】【船舶インシデント】【市場】→ 表には入れない（30秒カラム・速報インシデントが担う）
- 各行の「現況詳細」は「最新」行＋直近の要点を見せ、それ以前の経緯は `<details><summary>経緯を見る</summary>…</details>`（E3）
- #6：旧ルート・ルート D のセルに `id="jf-old-bpd"`・`jf-old-tanker`・`jf-D-bpd`・`jf-D-tanker` を付け、
  `loadRouteTableFlow()` の `MAP` に `old`・`D` を追加（`oil-flow.json` 側は現状どおり手入力0。redesign-plan §7）
- 表の脚注の古い数値（「充足率65〜70%」と統計ベースの110%が並ぶ件・oil-flow-redesign.md）は、この PR で整理するか ②' へ回すかを着手時に判断

### #14（インライン font-size のクラス化）の割り振り

- 各 PR で担当区域を置換する（S03→PR1、S09・S04・S05→PR2、ルート表・シナリオ→PR3）
- 区域外の残り（`div[style*="font-size:0.7"]` 54か所など）・シナリオ S06〜S08 のクラス化・属性セレクタの撤去は **PR4**（E7）。PR4a・PR4b に分け（E8）、PR4b はさらに 4b-1・4b-2 に分ける（E9）
- 値の集約（2026-09-23 決定どおり数%の変化を許容）。rem 値だけを対象とし、`em`（絵文字の相対指定）と `px`（地図オーバーレイ）は対象外：

| トークン | 集約する値 |
|---|---|
| `--fs-2xs` 0.65rem | 0.62・0.65・0.66 |
| `--fs-xs` 0.72rem | 0.68・0.7・0.72・0.73・0.74 |
| `--fs-sm` 0.78rem | 0.75・0.77・0.78・0.8 |
| `--fs-base` 0.85rem | 0.82・0.85・0.88 |
| `--fs-md` 0.95rem | 0.9・0.95・1 |
| `--fs-lg` 1.1rem | 1.05・1.1・1.2 |
| `--fs-xl` 1.35rem | 1.35・1.4 |

- クラス名は `.fs-2xs`〜`.fs-2xl`（ユーティリティ）。要素に既に意味のあるクラスを付ける場合は、そのクラスの CSS に `font-size: var(--fs-*)` を書き、ユーティリティは使わない

---

## 4. 検証（各 PR 共通）

1. タグを除いたテキストの差分が、意図した変更（削除した項目・移した文）だけであること
2. 対応する開始タグの無い閉じタグが0件
3. `python tools/validate_daily.py` が通る（新しい正規表現で）
4. ローカルのプレビュー（`.claude/launch.json`・8765番）で 375・390・430・768・1280px。コンソールエラー0、`applyIncidentFold()`・`loadRouteTableFlow()`・カウントダウンが動く
5. マージ後に本番で同じ確認
6. **翌朝の日次更新のコミットを読み、新しい型で書かれていること・validate が通ったことを確認**

---

## 5. 範囲外（②' 以降）

- #1 基準日の統一・最終更新の一元表示、#2(a) 主要数値の静的化、#3 未ラベルの推定値のラベル（候補4）、#5「確認中」「-」表示、#4 候補5
- #15 の残り（スマホの `h1`・見出し色 `#94a3b8`）＝②' のタイポグラフィ再設計
- ただし PR3 の「最新（M/D）」行は #1 の基準日の統一で扱いやすいよう、日付を `<time>` か決まったクラスで包む

---

## 6. 未決

| # | 論点 | 案 | 決める時期 |
|---|---|---|---|
| U2 | 【中央航路】【南側航路】【代替輸送路】と表の行の対応 | **決定（2026-09-27）：ラベルではなく中身で振り分ける**。海峡内の航行（中央・南側航路とも）→旧ルート、東西PL・ヤンブー・紅海・バブエルマンデブ→B、ADCOP・フジャイラ→A、通航料→D。9/27 のリード文では【南側航路】の下にサウジ東西PL の話が入っており、ラベルと中身がずれていた。対応表は daily-site-update「ルート表の型」 | 済 |
| U3 | 「主な動き」から速報インシデントの各項目へのリンク | **決定（2026-09-25）：`#incident` だけ**。主な動き3件＝速報インシデントの先頭3件（折りたたまれず見えている）なので id は不要。日次の手間と、月1回の退避で id が消えるリスクを避ける | 済 |

---

## 7. 実施記録

### PR1（2026-09-24・ブランチ `redesign/phase2-sections`）

- `docs/index.html`：要約段落を削除、見出し部を `.incident-headline`・`.incident-badge` に、残した35件（8/25〜9/21）を `li.incident-item`＋色のモディファイア4種に。
  `<!-- ROUTE TABLE -->` をルート表の直前へ移し、S03 の目印コメントの全角空白を半角に
- `docs/data/incident_archive.json`（新設）：186件（8/24 以前。元の HTML と本文）。ブラウザで数えた項目数（221＝35＋186）と一致、本文の全文一致を確認
- 検証：タグを除いたテキストの差分は「退避した186件」と「要約段落5本」だけ／対応の無い閉じタグ0／`validate_daily.py` OK 22・WARN 0・NG 0／
  1280px・375px で項目の文字・色・余白・幅が変更前と一致、件名だけ 17.6→17px（1280px）・15.84→15.3px（375px）＝トークン集約による想定内の変化／
  `#incident` の高さ 2,932→858px（1280px）／折りたたみの開閉が動く・コンソールエラー0
- スキル（daily-site-update「速報インシデントの型」・月1回の退避）、`diffs-generation-rules.md`（S03 の新しい型の APPLY 例）、html-safe-edit を更新

### PR2（2026-09-25・ブランチ `redesign/phase2-sections`）

- 前提：9/25 07:16 の日次更新（`4ddc0db`）が PR1 の型で通った（新規2件は `li.incident-item`＋モディファイア・インライン style なし・要約段落なし・validate OK 22）
- 決定：U3 は `#incident` だけ。ステータスバッジは残してクラス化のみ（主な動きとの重複整理は ②'）
- `docs/index.html`
  - S04：見出し・空の `div#situation`・`.sit-grid`（カード8枚）を削除。撤去したカードの出来事8件はすべて速報インシデントに残っていることを確認
  - S09：30秒カラムの全要素をクラス化（`.glance*`・`.key-move*`・`.status-badge--*`・`.jump-pill--*`・`.report-banner*`、インライン style 47→0、`onmouseover` は `:hover` へ）。
    3行サマリーの下に「主な動き」3件（`<ol class="key-moves-list">`・`<time datetime>`・行ごと `#incident` へのリンク）。
    `href="#situation"` の「🌐 情勢カード」ボタンは「🚨 速報インシデント」（`#incident`）に付け替え、ジャンプ行の重複リンクを外した。「🇯🇵 日本向け調達フロー」だけ形が違っていたのをほかのピルに揃えた
  - S05：`dl-box` の min-width・`dl-num` の文字サイズ・`dl-note` の焦点行をクラス化（`.dl-box--timer`・`.dl-num--text`・`.dl-focus`）
  - CSS：`.sit-*` 一式、S09 専用だった属性セレクタ `[style*="display:flex;flex-wrap:wrap;gap:8px;"]`・`[style*="font-size:0.95rem"]`、
    一致する要素が無かった `[style*="font-size:1.2rem;font-weight:800;letter-spacing:0.06em"]`、未使用の `.summary-row` を削除。
    属性セレクタのスマホ時の効果（0.88rem・0.8rem）は `.glance-text` などのクラスで引き継いだ。`div[style*="font-size:0.7"]` は区域外に54か所残るので PR3
- `tools/validate_daily.py`：`check_types()` を追加（30秒カラムのインライン style・主な動きの件数/並び/最新日、速報インシデント一覧のインライン style。いずれも WARN）
- スキル・文書：daily-site-update（作業順序5を欠番、「30秒カラムの型」、COUNTDOWN の `dl-focus`）、publish-checklist、content-style-guide、`diffs-generation-rules.md`（[S04] 欠番・[S09] の APPLY 例）
- 検証：タグを除いたテキストの差分は「情勢カード8枚」「主な動き3件」「ボタンの付け替え」だけ／対応の無い閉じタグ0／validate OK 25・WARN 0・NG 0／
  1280px・375px で30秒カラムの各要素の色・余白・角丸が変更前と一致、文字サイズはトークン集約分だけ変化（例：ラベル 0.75→0.78rem、ボタン 0.82→0.85rem、地図リンク 0.9→0.95rem）／
  横はみ出し0／ページの高さ（375px）35,765→32,346px／速報インシデントの折りたたみ（3＋34件）・カウントダウンが動く・コンソールエラー0

### PR3（2026-09-27・ブランチ `redesign/phase2-sections`）

- 前提：9/27 07:35 の日次更新（`e321102`・#26）が PR2 の型で通った（validate OK 26・WARN 0）。ただしリード文は 9/25 の内容のまま残っており（【外交】が 60日ロードマップ、「9月25日朝時点」）、見出しの日付だけが更新されていた
- 決定：U2（中身で振り分け）、E6（脚注は PR3 で整理）、E7（#14 の区域外は PR4）
- `docs/index.html`
  - リード文 `p.sec-lead` を削除。【中央航路】（GCC 協議の延期）→旧ルートの要点、【代替輸送路】（フーシ派・ペリム島）→ルートB の要点へ移した。
    【南側航路】（東西PL 9/22 再開）はルートB の 9/25 追記と同じ内容のため移さない。【外交】【船舶インシデント】【市場】【日本関係船舶】は速報インシデント・更新ログに同じ事実があることを確認して削除
  - 「現況詳細」6行を 最新（`p.route-latest`＋`<time datetime>`）→ 要点（`p.route-summary`）→ 経緯（`details.route-history`）に。本文は並べ替えとラベル（「最新」）以外は変えていない
  - 表の中のインライン style 83→0（`<col>` 7か所は html-safe-edit に従い残す）。色は `.t-*`、分析の箱は `.route-priority`、注記は `.jf-note`・`.route-note`
  - 脚注（E6）。`colspan="6"` を 7 に直した（表は7列）
  - #6：`jf-old-*`・`jf-D-*` を付け、`loadRouteTableFlow()` の `MAP` に `old`・`D`（0 のとき「停止中」）
- `tools/validate_daily.py`：行ごとの鮮度を `route-latest` の `<time datetime>` で判定（型で書かれていない行は M/D 表記で推定し WARN）。
  `check_types()` にルート表のインライン style・`sec-lead` の復活・「最新」より新しい日付の検出を追加。変更前の HTML で WARN 8件が出ることを確認
- スキル・文書：daily-site-update（「ルート表の型」・U2 の対応表・鮮度 WARN の手順・作業順序 8.5・ルール1）、html-safe-edit（列の記述の誤りを直した）、publish-checklist、`diffs-generation-rules.md`（[S08.5]）
- 検証：タグを除いたテキストの差分はリード文の削除・並べ替え・「最新」ラベル・脚注だけ／対応の無い閉じタグ0／validate OK 27・WARN 0・NG 0／
  1280px で色・余白・背景が変更前と一致、文字サイズはトークン集約分だけ変化（見出し 13.6→14.4px、脚注 13.6→14.4px）。表の高さ 5,085→4,016px（1280px）・8,512→6,571px（375px）／
  375px・800px で横はみ出し0／「経緯を見る」の開閉が動く／旧ルート・D は「停止中」、A は「69 万BPD・🚢×2 隻/週」／コンソールエラー0
- マージ：2026-09-28（`04cb8fb`・#27）。9/28 の日次（#28）を取り込んで競合1か所（見出しの日付）を解消してから。本番で 1280px・375px・「停止中」・コンソールエラー0 を確認。
  9/29 の日次（`4ee9e12`・#32）で旧ルートの行が新しい型（`route-latest` 1件・前の「最新」は `route-entry` として経緯の先頭へ）で書かれたことを確認（validate OK 34・WARN 0）

### PR4a（2026-09-29・ブランチ `redesign/phase2-pr4a`）

- 前提：9/29 の日次が PR3 の型で通った（上記）。決定：E8（PR4 を 4a・4b に分割）
- 事前の調査：`<body>` のインライン style（スクリプト・`<col>` を除く）301か所。`git blame` で、日次が書き込むのはシナリオと更新履歴だけと確認
- `docs/index.html`
  - シナリオ：確率補足バナー `.sc-update`（`.sc-update-date`・`.sc-trend`・`.sc-update-caveat`・`.sc-sync-note`）、AI 注記 `.sc-ai-note`・`.sc-ai-meta`・`.sc-ai-variance`・`.sc-ctx-note`、
    見出しの強調 `.sc-tag-em`、フッター `.sc-footer`・`.sc-focus-h`・`.sc-focus-list`。インライン style 43→0。
    `.sc-grid` のインライン（2列）を外し、CSS の `!important` も外した。B の矢印だけ span が無かったので `.sc-trend` で揃えた（色が黄→灰）
  - 更新履歴：`.update-log`・`.update-log-head`・`.log-recent`・`.log-older`・`.log-date`・`.log-tag`・`.log-sources-start`・`.log-toggle`・`.log-toggle-btn`（`onmouseover`/`onmouseout` は `:hover` へ）。
    インライン style 38→0（開閉の状態として JS が読む `#log-collapse`・`#log-toggle-bottom` の `display:none` は残す）。
    日時の色は日次ごとにばらついていた（折りたたみの中に赤など）ので、位置で決める CSS にした（常時表示の先頭＝赤、2・3件目＝明るい灰、折りたたみ＝灰）
  - 全ルート現況サマリーの見出しも `.sec-h2--sky`（日次が毎日書き換える行のため）
  - スマホで `div[style*="font-size:0.7"]` が当てていた 0.8rem は、クラスのメディアクエリで引き継いだ。属性セレクタ自体は区域外に37か所残るので PR4b で撤去
  - `<body>` のインライン style 301→220
- `tools/validate_daily.py`：`check_types()` にシナリオ・更新履歴のインライン style、更新履歴の件数（常時表示3件・合計10件まで）を追加（WARN）。変更前の HTML で WARN 3件
- スキル・文書：daily-site-update（「シナリオの型」「更新履歴の型」・作業順序 7・8・11・sc-tag の古い記述「innerHTML を使う」を実装に合わせて直した）、publish-checklist、html-safe-edit、`diffs-generation-rules.md`（[S06]〜[S08]・[S11]）
- 検証：タグを除いたテキストの差分0／対応の無い閉じタグ0／validate OK 37・WARN 0・NG 0／
  同一オリジンの iframe で変更前後の計算済みスタイルを要素ごとに比較（1280px・375px）：色・背景・枠線・余白は一致、違いはトークン集約分の文字サイズ（0.7→0.72・0.73/0.74→0.72・0.75→0.78・0.9→0.95rem）と、更新履歴の日時の色4か所（上記の統一）だけ／
  375px で横はみ出し0／更新履歴の開閉（上・下のボタン）・確率の同期・2列の配置が動く／コンソールエラー0
- マージ：2026-09-30（`acbf971`・#33）。9/30 の日次（#34）を取り込み、競合7か所は本文を main（9/30）から採ってマークアップを PR4a の型に直した（`ea0410c`）。本番で更新履歴 3件＋7件・開閉・日時の色・コンソールエラー0 を確認。
  10/1 の日次（`d6ed150`・#35）でシナリオ・更新履歴が新しい型で書かれたこと（validate の型の検査 OK・更新履歴 3件・10件）と、初回の月1回退避（8/24〜8/31 の7件・`incident_archive.json` 186→193件）を確認

### PR4b-1（2026-10-01・ブランチ `redesign/phase2-pr4b1`）

- 前提：10/1 の日次が PR4a の型で通った（上記）。決定：E9（PR4b を 4b-1・4b-2 に分割）
- `docs/index.html`（CSS は「本文の残り（② PR4b-1）」にまとめた）
  - その他の検討中ルート：`.or-wrap`・`.or-toggle`（onclick が書き戻す HTML の span も `.or-toggle-em`）・`.or-panel`・`.or-list`・`.or-card--{br,mx,iq,ca}`（色は CSS 変数）・`.or-head`・`.or-flag`・`.or-title`・`.or-badge`・`.or-text`（`.or-ok`・`.or-alert`）・`.or-note`。
    開閉の状態は onclick が `style.display` で読むので `#other-routes-body` の `display:none` はインラインに残した
  - 主要指標：`.stat-asof`・`.stat-head`・`.stat-num--stock`・`.stat-num--wti`・`.stat-unit`（`--sm`）・`.stat-label--stock`・`.stat-sub`・`.stat-card--wti`
  - 特別解説コラムのカード6枚：`.col-card--{red,amber,sky,green,orange,violet}`（色は `--cc`・`--cc-accent`）・`.col-card-head`・`-icon`・`-titles`・`-title`・`-sub`・`-date`・`-lead`・`-link`（`--inrow`）・`-thumbrow`・`-thumb`
  - 第3層の外枠：`.sec-block`（`--left`・`--news`）、見出し `.sec-h2--red`・`.sec-h2--violet`・`.sec-h2--spaced`、読み込み中 `.loading-note`、数値の注記 `.data-note`、日次アーカイブへのリンク `.archive-link-wrap`・`.archive-link`。
    `toggleArchive()` が `style.display` で読む `#news-archive-container` の `display:none` は残した
  - 文字サイズは #14 の対応表どおりトークンへ（0.68・0.7→xs、0.75・0.8→sm、0.9・1→md、1.2→lg、1.4→xl）。スマホで `div[style*="font-size:0.7"]` が当てていた 0.8rem はクラスのメディアクエリで引き継ぎ、
    コラムの要約（`p`・0.8→0.78rem）もスマホでは 2-a の本文の下限 0.8rem を保つ
  - `<body>` のインライン style（スクリプト・`<col>` を除く）220→100
  - `SOURCE & UPDATE LOG` の外枠（`max-width:960px`・属性セレクタが当たる）とトランプ声明の比較ブロック（`bw-*`・開閉の状態をインラインで持つ）は PR4b-2
- 文書：`tools/new-article-checklist.md` §4 のコラムカードの例をクラスの型に（インライン style を書かない・色は `col-card--{色}`）
- 検証：タグを除いたテキストの差分は開閉ボタンの onclick 属性の中身だけ（画面に出る本文は同じ）／対応の無い閉じタグは変更前と同数／validate OK 37・WARN 0・NG 0／
  同一オリジンの iframe で計算済みスタイルを要素ごとに比較（1280px・800px・375px、その他の検討中ルートは開閉の両方）：色・背景・枠線・余白は一致、違いはトークン集約分の文字サイズと、それに比例する幅・高さ・`letter-spacing`（em 指定）・`margin-left:auto` の計算値だけ／
  375px で横はみ出し0／開閉ボタンの黄色の強調が開閉後も同じ／コンソールエラー0
- 見つけたこと（PR の範囲外）：主要指標の備蓄カードが「2026年8月17日時点（速報）・204日分」のまま。validate の備蓄日数の検査（地図ポップアップ・精製所表の注記の2か所）の対象外だった → 2026-10-01 に main で 9/27 時点（198日分）へ直し、validate と毎月4日のタスクの対象に加えた（`777e05e`）
- マージ：2026-10-02（`a61cfed`・#36）。10/1 午後の main の変更（COUNTDOWN 休止・フッター・トランプ声明バナーの移動）と 10/2 の日次（#39）を取り込み、競合なし（`ed23260`）。
  main の `09ca39d` で特別解説コラムの格子に足されたトランプ声明カードがインライン style だったので、7枚目として `.col-card--slate` の型にした（`253dabe`。枠線の濃さ 0.25 は `--slate` で保ち、全文ボタンは `<button>` なので `button.col-card-link` に `cursor`・`font-family` を足した。文字サイズはほかのカードと同じ対応表でトークンへ）。
  main との比較で本文の差分0、カードの色・背景・枠線は一致。CI 3件 pass。本番で カード7枚・声明モーダルの開閉・コンソールエラー0 を確認

### PR4b-2（2026-10-01・ブランチ `redesign/phase2-pr4b2`。PR4b-1 の上に積む）

- `docs/index.html`（CSS は「部品の残り（② PR4b-2）」にまとめた。既存のクラスより前に置くので、上書きは複合セレクタで書いた）
  - ヘッダー：`.h1-title`・`.h1-sub`（スマホの `header h1 span:first/last-of-type` の `!important` は不要になったのでクラスの指定に置き換え）、
    `.infographic-cta-row`・`.infographic-thumb-link`（`onmouseover`/`onmouseout` は `:hover` へ）・`.reload-btn`（同）
  - 層の帯：`.layer-band--1`〜`--3`（`--layer-accent` を CSS へ）
  - X・YouTube のリンク `.social-link`（`--yt`）、YouTube から来た方へ `.yt-visitors`・`-label`・`-btn`
  - 解説インフォグラフィック `.infographic-block`、速報インシデントの枠 `.incident-box`・`.incident-head`・`.sec-h2--incident`、トランプ声明バナーの外枠
  - 地図のタンカー欄：`#tanker-stats .stat-row--breakdown`・`.stat-row-val`、`#t-total`、`#tanker-note`（地図に重ねる表示なので px のまま）
  - データ監視 `.dash-frame`・`#hormuz-dashboard`、リアルタイム市場 `.sec-h2--green`・`.market-widget`・`.market-grid--main/--sub`・`.market-cell`・`.market-note`
  - トランプ声明モーダル：`.modal-trans`・`.modal-interp-lead`・`.i-text--a/--b`・`.modal-ling`（灰色の節の見出しのインライン色は `.modal-section.gray .modal-section-title` と同じなので削除）
  - 比較ブロック：`.bw-flag--end`・`.bw-toggle`・`.bw-em`・`.bw-sec--spaced`
  - 出典・更新履歴の外枠 `.source-wrap`・`.source-inner`、製油所モーダル `.ref-modal`・`.ref-modal-*`・`.ref-area*`・`.ref-base-grid`
  - `<body>` のインライン style 100→8。残りは JS が状態として読み書きするもの：`display:none` 7か所（`#other-routes-body`・`#bw-timeline-detail`・`#bw-detail-body`・`#news-archive-container`・`#log-collapse`・`#log-toggle-bottom`・`#refinery-modal`）と `#tanker-progress-bar` の `width:100%`
- 属性セレクタ・重複の撤去
  - `[style*="max-width:960px"]`（2か所）→ `.source-wrap`（`.container` と同じ指定）
  - `#news-latest-extra[style*="block"]` → `#news-latest-extra.is-open`（`toggleNewsExtra()` が開閉で `is-open` を付け外し）
  - `#jf-td-*` の `display:none`（`.jf-col` の `!important` と重複）を削除
  - **`div[style*="font-size:0.7"]` は残した**：HTML には当たらなくなったが、JS が組み立てる HTML（地図のポップアップ5か所・関連最新ニュースの項目）にまだ当たる。JS のテンプレートをクラスにするまで残す（コメントに明記）
- `tools/validate_daily.py`：`check_types()` に「ページ全体のインライン style（上の8か所・`<col>` を除く）」を追加（WARN）。PR4b 前の HTML で WARN 214件
- スキル：daily-site-update に「ページ全体」の節（どこにも `style` を書き足さない）
- 検証：タグを除いたテキストの差分0／対応の無い閉じタグは変更前と同数／validate OK 39・WARN 0・NG 0／
  PR4b-1 の HTML と計算済みスタイルを要素ごとに比較（1280px・800px・375px。製油所・トランプ声明の両モーダル、比較ブロックの2つの開閉、ニュースの「さらに見る」を開いた状態も）：
  色・背景・枠線・余白は一致、違いはトークン集約分の文字サイズとそれに比例する値、比べた瞬間が違うアニメーション（`.bw-dot`・バナーの枠の色）だけ。地図のタンカー欄は差分0／
  スマホで旧属性セレクタの 0.8rem を引き継ぎ（`.market-note` は旧インラインが「font-size: 0.75rem」（空白入り）で当たっていなかったので引き継がない）、製油所モーダルの概要文は 2-a の下限 0.8rem を保つ／
  ニュースの「さらに見る」は開く＝`is-open`・grid、閉じる＝none／375px で横はみ出し0／コンソールエラー0
- マージ：2026-10-02（`20d160a`・#37）。#36 のマージ後に基準ブランチを main に変え、PR4b-1（main を含む）を取り込んで競合2か所を解消（`0942e0f`）：
  ヘッダーの日時は 10/2 08:36 の値・再表示ボタンは `.reload-btn` のまま／第1層末尾のトランプ声明バナーは main（`09ca39d`）がコラムのカードへ移したので、バナーと上記の「トランプ声明バナーの外枠」（`.trump-banner-wrap`）を消した。
  CodeQL が validate の `<script>` を除く正規表現を指摘（`py/bad-tag-filter`・high。大文字と `</script >` に当たらない）→ `<script\b[^>]*>.*?</script\b[^>]*>`・`re.I` に直して pass（`3fcf873`）。
  基準を変える前の push では CI が動かなかったので、main を取り込み直して起動した（`17479fa`・内容は変わらず）。
  マージ前に #36 マージ後の main と比較（1280px・390px、開閉とモーダルは開いた状態も）：本文の差分0、色・背景・枠線・余白は一致、違いは文字サイズのトークン化分と `.bw-dot` のアニメーションだけ。validate OK 39・WARN 0・NG 0。
  本番（1280px・375px）：ソースの `<body>` のインライン style 8か所・`onmouseover`/`onmouseout` 0、開閉6か所（その他の検討中ルート・タイムライン・声明の詳細・ニュースのアーカイブ・「さらに見る」・更新履歴）と声明モーダル・製油所モーダルの表示と閉じるボタン、横はみ出し0、コンソールエラー0。
  マージ後にブランチ `redesign/phase2-pr4b1`・`-pr4b2` を削除（運営者の指示）
