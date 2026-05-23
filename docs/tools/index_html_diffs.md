# index_html_diffs.md — 2026年5月23日 08:56 日本時間JST

> **Claude Code への指示：以下の変更を `docs/index.html` に適用してください。**
> **変更箇所以外は絶対に触らないこと。**
> **作業後に `git commit`（メッセージ: `update: 2026-05-23 情勢更新`）してください。pushは確認後に指示します。**

-----

## [S01] ヘッダー日時・警戒レベル

**対象:** `<header>` 内の警戒レベル表示と更新日時

**変更内容:** 日時を本日 JST に更新。警戒レベルは 🚨 最高 を維持。

**old_str（日時行のみ — 前回の日付を含む行）:**

```
📅 2026年5月22日
```

**new_str:**

```
📅 2026年5月23日 08:56 JST
```

-----

## [S02] TICKER

**対象:** `/* TICKER */` セクション

**変更内容:** 本日の主要ニュース5件に更新。進展があるため「膠着継続」行は追加しない。

**old_str（TICKER 内容ブロックの特定行 — 前回の先頭ニュース行）:**

```
🔴 5/22
```

※ TICKER 内のテキスト全体を以下の new_str に置き換えてください。
TICKER コメント `/* TICKER */` の開始〜終了タグ内のテキスト部分のみ置換します。

**new_str（TICKER テキスト）:**

```
🔴 5/23 08:56 JST 米下院GOP、対イラン戦争権限決議の採決を土壇場で回避——民主党「賛成票は確保済み」と激怒、6月3日再提起へ ｜ 🔴 5/22 JST ルビオ国務長官「ホルムズ通行料は完全に違法」——PGSAへの制裁検討を財務省に促す ｜ 🔴 5/22 JST イラン最高指導者・モジュタバ・ハメネイ師「60%濃縮ウランを国外移送しない」指令——米国の核要求に重大な障壁 ｜ 🟡 5/22 JST カタール・パキスタン軍参謀長ムニルがテヘランに向け集中仲介——「いくらかの前進」ルビオが認める ｜ 🟡 5/22 JST イラン国営メディア「過去24時間で35隻がIRGC調整下でホルムズを通過」——PGSA通行料最大200万ドル ｜ 📈 WTI $96〜98/bbl（週間小幅下落、ウラン指令報道で週末に反発）
```

-----

## [S03] 速報インシデント

**対象:** `<!-- 速報インシデント トグルボタン -->` セクション内の最新インシデントカード

**変更内容:** 本日の最重要インシデントを先頭に追加。前回の先頭カードは2番目に押し下げる。

**追加する新規インシデントカード（先頭に挿入）:**

```html
<!-- 速報インシデント #1: 2026-05-21 -->
<div class="incident-card" style="border-left:4px solid #f59e0b;background:rgba(245,158,11,0.08);padding:12px 14px;border-radius:6px;margin-bottom:10px;">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
    <span style="font-size:0.75rem;font-weight:700;color:#f59e0b;letter-spacing:0.05em;">🏛️ 議会動向</span>
    <span style="font-size:0.72rem;color:#94a3b8;">2026年5月21日 JST</span>
  </div>
  <p style="font-size:0.88rem;color:#e2e8f0;line-height:1.6;margin:0;">
    <strong>米下院GOP、対イラン戦争権限決議の採決を土壇場で回避。</strong>
    民主党が共和党議員を取り込み可決確実の情勢となったため、GOP指導部が採決自体を6月3日以降に延期。
    前回（5月14日）は212-212の同数で辛くじて否決。上院でも共和党4名が賛成票を投じており、トランプ政権の対イラン戦争遂行権限をめぐる議会との対立が深刻化。
  </p>
  <p style="font-size:0.78rem;color:#94a3b8;margin:6px 0 0;">📰 出典: NPR / CBS News（2026年5月22日）</p>
</div>
```

-----

## [S04] 情勢カード3枚

**対象:** `<!-- SITUATION CARDS -->` セクション内の各カード

### カード1: 封鎖継続日数

**old_str（日数表示部分）:**

```
83<span
```

（※ 前回の日数。前回が83日だった場合）

**new_str:**

```
84<span
```

**カード内日付表示も更新:**

**old_str:**

```
2026年5月22日
```

（カード1内の日付行のみ）

**new_str:**

```
2026年5月23日 08:56 JST
```

### カード2: ホルムズ通航状況

**変更内容:** イラン国営メディア「過去24時間で35隻通過（PGSA管理下）」を反映。

**old_str（カード2の主要数値行 — 前回の数値）:**

```
PGSA管理下の通過船舶
```

対象のカード2テキスト本体を以下の内容に更新してください：

**new_str:**

```html
<p style="font-size:0.85rem;color:#e2e8f0;line-height:1.6;margin:4px 0;">
  イラン国営メディア：PGSA管理下で<strong style="color:#fbbf24;">過去24時間に35隻が通過</strong>。
  ただし通過料は最大200万ドル（ビットコイン/人民元）。
  米国はOFAC制裁に抵触するとして支払いを全面禁止。
  欧州・日本船社は通過を事実上断念している。
</p>
<p style="font-size:0.78rem;color:#94a3b8;margin:4px 0 0;">📅 2026年5月23日 08:56 JST 確認</p>
```

### カード3: 原油価格

**old_str（WTI価格表示行）:**

```
$9
```

（カード3内の価格数値。前回の値を含む行を特定して置換）

※ カード3の価格帯テキストを以下に更新してください：

**new_str（カード3テキスト本体）:**

```html
<p style="font-size:0.85rem;color:#e2e8f0;line-height:1.6;margin:4px 0;">
  WTI原油：<strong style="color:#f87171;">$96〜98/bbl</strong>（5月22日終値 $98超）。
  週間では小幅下落するも、イラン最高指導者のウラン国外移送禁止指令を受けて週末に反発。
  IEAは「7月までに世界在庫が危機的水準に達する」と警告。
  米国は戦略石油備蓄(SPR)から先週1000万バレル放出（過去最大）。
</p>
<p style="font-size:0.78rem;color:#94a3b8;margin:4px 0 0;">📅 2026年5月23日 08:56 JST</p>
```

-----

## [S05] COUNTDOWN

**対象:** `<!-- COUNTDOWN -->` セクション

**変更内容:** フェーズラベルを現状に合わせて維持・日付更新のみ。

**フェーズ:** 「停戦・集中交渉フェーズ（84日目）」

**old_str（カウントダウン内の日数またはフェーズ表記行）:**

```
停戦・集中交渉フェーズ（83日目）
```

**new_str:**

```
停戦・集中交渉フェーズ（84日目）
```

-----

## [S06] シナリオ確率補足バナー

**対象:** `<!-- SCENARIOS -->` 内の補足バナー（矢印＋根拠文のみ。数値は記載しない）

**変更内容:** 本日の情勢を反映した根拠文と矢印を更新。

**old_str（バナー内の日付行）:**

```
2026年5月22日
```

（バナー内の日付のみ。補足バナーのdiv内を対象）

**new_str（補足バナー全体を以下に置換）:**

```html
<!-- SCENARIOS 確率補足バナー -->
<div style="background:rgba(99,102,241,0.08);border:1px solid rgba(99,102,241,0.25);border-radius:8px;padding:12px 16px;margin:0 0 16px;font-size:0.82rem;color:#c7d2fe;line-height:1.65;">
  <strong style="color:#a5b4fc;">📊 シナリオ確率の根拠（2026年5月23日 08:56 JST 更新）</strong><br>
  <span style="color:#86efac;">A 外交解決 ↑</span>　パキスタン・カタール集中仲介で「若干の前進」。ただしモジュタバ・ハメネイ師のウラン国内保有指令が核交渉に深刻な障壁。外交解決の確率は微増も道のりは険しい。<br>
  <span style="color:#fbbf24;">B 部分封鎖継続 →</span>　PGSA管理下で一部船舶が通航（24時間で35隻）。米国の制裁対象ゆえ欧米・日本は事実上断念。現状の「制限的通航」が膠着継続の最有力シナリオ。<br>
  <span style="color:#fb923c;">C 制度的封鎖定着 ↑</span>　イラン・オマーンがPGSA恒久化を協議。米国の「違法」宣言にもかかわらずPGSAが国際的認知を拡大しつつあり、事実上の恒久制限リスクが上昇。<br>
  <span style="color:#f87171;">D 軍事エスカレーション →</span>　議会の戦争権限決議が6月再提起見込みで政治的圧力は増大。CENTCOMの「短期打撃計画」報道あるも、外交継続中のため即時リスクは低位維持。ウラン指令でイスラエルの攻撃再開圧力は高い。
</div>
```

-----

## [S07] シナリオ4本（タイトル・本文）

**対象:** `<!-- SCENARIOS -->` 内の各 `sc-card`（A・B・C・D）

> ⚠️ 数値（%）は記載しない。syncScenarioFromDashboard() が自動更新する。

### シナリオA：外交解決

**変更内容:** バナーと整合させた本文に更新。

**old_str（シナリオAカード内のsc-titleまたはsc-body冒頭）:**

```
sc-card-a
```

（sc-card-a クラスを持つdiv内の sc-body テキストを置換）

**sc-title:**

```
🕊️ シナリオA：外交解決・ホルムズ正常化
```

**sc-body（置換）:**

```html
<p>パキスタンとカタールの集中仲介のもと、米国・イラン間の提案・反提案のやり取りが継続。ルビオ国務長官は5月22日、「若干の前進」と認めつつも、PGSA通行料制度を「世界のどの国も受け入れるべきでない」と明確に拒否した。</p>
<p>最大の障壁は核問題。モジュタバ・ハメネイ最高指導者は60%濃縮ウランの国外移送を禁止する指令を発し、「ウランをイランから取り出す」というトランプ大統領がイスラエルに約束した条件と真っ向から対立する。</p>
<p>外交解決が実現した場合、WTI原油は$65〜$80/bblへの急落が想定される。日本船社のペルシャ湾ルート復帰も3〜6週間内に実現する見通し。</p>
```

**sc-src（出典）:**

```
出典：Irish Times・Fox News・Algemeiner（2026年5月22〜23日）
```

-----

### シナリオB：部分封鎖継続（PGSA管理下の制限通航）

**sc-title:**

```
⚠️ シナリオB：PGSA制限通航の長期膠着
```

**sc-body（置換）:**

```html
<p>現在の最有力シナリオ。イランはPGSA管理下で「35隻/24時間」の通航を認め、通過料（最大200万ドル、ビットコインまたは人民元）を徴収。中国・韓国など一部国は事実上の支払いを行い通過している模様。</p>
<p>米国はOFAC制裁を根拠に通行料支払いを全面禁止、欧州・日本の海運会社は通過を断念。「制限的通航」という曖昧な状態が外交交渉中は継続する公算大。</p>
<p>このシナリオが継続した場合、WTI原油は$90〜$105/bblの高止まりが続く。米国のSPR放出（先週1000万バレル、過去最大）も価格抑制効果は限定的。</p>
```

**sc-src（出典）:**

```
出典：CBS News・Maritime Executive・Trading Economics（2026年5月22〜23日）
```

-----

### シナリオC：PGSA制度定着・事実上の恒久封鎖

**sc-title:**

```
🚫 シナリオC：PGSA恒久制度化・国際的封鎖固定化
```

**sc-body（置換）:**

```html
<p>交渉が長期化する中、イランとオマーンがPGSAを恒久的な「ホルムズ管理機関」として制度化する協議を進めている（Bloomberg報道）。イラン大使は「透明性ある料金体制」を強調し、通過料の国際的認知獲得を目指している。</p>
<p>米国は「違法」と宣言し制裁を検討するが、中国・ロシアが事実上容認し国連での制裁決議も不可能な構造。PGSAが国際的既成事実となれば、ホルムズは「公海」から「イラン管理水域」へと実質転換する。</p>
<p>このシナリオでは、日本・韓国・インドの原油調達ルートは恒久的な多様化を余儀なくされ、ケープ・オブ・グッド・ホープ経由が標準化。WTI原油は$100〜$115/bblの高水準を維持。</p>
```

**sc-src（出典）:**

```
出典：gCaptain・Bloomberg・Windward AI（2026年5月22〜23日）
```

-----

### シナリオD：軍事エスカレーション再開

**sc-title:**

```
💥 シナリオD：停戦崩壊・軍事衝突再開
```

**sc-body（置換）:**

```html
<p>議会圧力が増大。5月21日に米下院で可決寸前だった対イラン戦争権限決議はGOP指導部が採決を回避したが、6月3日に再提起予定。上院でも共和党4名が賛成。議会からの制約が現実化すれば、逆にトランプ政権が「決着」を急ぐインセンティブが生じる可能性がある。</p>
<p>イラン側ではモジュタバ・ハメネイ最高指導者のウラン国内保有指令がイスラエルを強く刺激。ネタニヤフ首相は「ウラン国外移送なしに戦争は終わらない」と明言しており、イスラエルによる単独先制攻撃の可能性が残る。CENTCOMも「短期集中打撃計画」を策定済みと報道されている。</p>
<p>軍事衝突が再開した場合、WTI原油は$115〜$135/bblへ急騰。日本のLNG・原油調達が再び深刻な危機に陥り、内閣の緊急備蓄対応が不可避となる。</p>
```

**sc-src（出典）:**

```
出典：NPR・Britannica・Algemeiner・The Defense News（2026年5月21〜23日）
```

-----

## [S08] シナリオフッター

**対象:** `<!-- シナリオ フッター -->` セクション内の「次の焦点5点」

**変更内容:** 本日の情勢に合わせて焦点を更新。

**new_str（次の焦点5点）:**

```html
<ol style="margin:8px 0 0;padding-left:20px;font-size:0.85rem;color:#c8d5e4;line-height:1.7;">
  <li><strong>6月3日：米下院の対イラン戦争権限決議再採決</strong>——可決すれば初の議会制約。</li>
  <li><strong>パキスタン軍参謀長ムニルのテヘラン訪問成果</strong>——次の提案・反提案サイクルの内容。</li>
  <li><strong>イランの60%濃縮ウラン問題</strong>——ハメネイ師指令と米国・イスラエルの要求の隔たりを埋める打開策があるか。</li>
  <li><strong>PGSAへの制裁発動</strong>——コットン上院議員が財務省に要求。通行料支払国への二次制裁の行方。</li>
  <li><strong>IEA「7月危機」警告への各国対応</strong>——日本・韓国・欧州の備蓄追加放出・代替ルート確保の進捗。</li>
</ol>
```

-----

## [S08.5] 全ルート現況サマリー

**対象:** `🚢 全ルート現況サマリー` セクション

**変更内容:** 日付を本日に更新。ルート状況に実質的変化なし（PGSA管理下の制限通航が継続）。「再確認済」を付記。

**old_str（サマリー内の日付行）:**

```
2026年5月22日
```

（全ルート現況サマリーセクション内の日付行を対象）

**new_str:**

```
2026年5月23日 08:56 JST 再確認済
```

**ルート状況補足（変更があった場合のみ — 今回は追記）:**

- ホルムズ海峡：PGSA管理下で35隻/24時間の制限通航（欧米・日本船社は事実上断念）
- スエズ運河：通常運航
- ケープ・オブ・グッド・ホープ：日本・欧州向け代替ルートとして需要増、混雑継続
- バブ・エル・マンデブ（紅海）：フーシ派攻撃リスク継続

-----

## [S09] 30秒カラム（3行サマリー＋バッジ5枚）

> ⚠️ **必ず全セクション確定後に最後に書く。**

**対象:** `<!-- 30秒で全体像を把握 -->` セクション

### 3行サマリー（置換）:

```html
<p style="font-size:0.92rem;color:#e2e8f0;line-height:1.75;margin:0 0 12px;">
  ① ホルムズ危機は<strong>停戦84日目</strong>。PGSA（ペルシャ湾海峡当局）が正式稼働し、
  通過料最大200万ドルで35隻/日の「有料通航」が続く。米国は「違法」と宣言し制裁を検討中。
</p>
<p style="font-size:0.92rem;color:#e2e8f0;line-height:1.75;margin:0 0 12px;">
  ② 外交は<strong>「若干の前進」</strong>（ルビオ）。パキスタン・カタールが仲介を集中化させる一方、
  最高指導者モジュタバ・ハメネイ師が「60%濃縮ウランを国外移送しない」指令を発し核交渉が複雑化。
</p>
<p style="font-size:0.92rem;color:#e2e8f0;line-height:1.75;margin:0 0 12px;">
  ③ 米議会では<strong>戦争権限決議が6月3日に再提起予定</strong>。WTI原油は$96〜98/bblで高止まり。
  IEAは「7月に世界在庫が危機的水準」と警告。日本の代替調達・備蓄対応が急務。
</p>
```

### バッジ5枚（置換）:

```html
<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:12px;">
  <span style="background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.4);color:#fca5a5;padding:4px 10px;border-radius:20px;font-size:0.78rem;font-weight:600;">🚨 停戦84日目</span>
  <span style="background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.4);color:#fcd34d;padding:4px 10px;border-radius:20px;font-size:0.78rem;font-weight:600;">⚓ PGSA通行料 最大$200万</span>
  <span style="background:rgba(99,102,241,0.15);border:1px solid rgba(99,102,241,0.4);color:#a5b4fc;padding:4px 10px;border-radius:20px;font-size:0.78rem;font-weight:600;">🕊️ 若干の前進（ルビオ）</span>
  <span style="background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.4);color:#fca5a5;padding:4px 10px;border-radius:20px;font-size:0.78rem;font-weight:600;">☢️ 濃縮ウラン国内保有指令</span>
  <span style="background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.4);color:#6ee7b7;padding:4px 10px;border-radius:20px;font-size:0.78rem;font-weight:600;">📈 WTI $96〜98/bbl</span>
</div>
```

-----

## [S10] news_data.json 更新メモ

> ⚠️ Claude.ai は news_data.json を単体ファイルとして生成しない。
> 以下の内容を Claude Code が `docs/data/news_data.json` に手動でマージすること。
> run.bat（auto_push.py）は news_data.json を push しない。

### `latest` 配列の更新

**操作:** 既存の最古の1件を `archive` 先頭バッチへ移動し、以下3件を `latest` の先頭に追加する。

```json
{
  "title": "米下院GOP、対イラン戦争権限決議の採決を土壇場で回避——6月3日に再提起へ",
  "body": "5月21日、米下院で対イラン戦争権限決議の採決が予定されていたが、民主党側が共和党議員を取り込み可決確実とみたGOP指導部が採決を6月3日以降に延期。前回（5月14日）は212-212の同数でかろうじて否決。上院でも共和党4名が賛成票を投じており、議会のトランプ政権への対イラン戦争遂行権限制約が現実味を増している。",
  "sourceLabel": "NPR",
  "date": "2026/05/22",
  "label": "🏛️ 米議会",
  "url": "https://www.npr.org/2026/05/22/g-s1-123592/republicans-call-off-vote-on-iran-war-resolution"
},
{
  "title": "ルビオ国務長官「ホルムズ通行料は完全に違法」——PGSA制裁を財務省に促す",
  "body": "米国務長官マルコ・ルビオは5月22日、イランが設立したPGSA（ペルシャ湾海峡当局）のホルムズ通行料制度について「完全に違法」と断じ、通行料支払い企業・国家への制裁発動を財務省に促した。コットン上院議員（共和党）も財務省宛て書簡でPGSA支払者への二次制裁を要求。ルビオは同日、パキスタン・カタールとの仲介交渉で「若干の前進」があったとも述べた。",
  "sourceLabel": "Fox News",
  "date": "2026/05/22",
  "label": "🗣️ 米外交",
  "url": "https://www.foxnews.com/live-news/iran-war-trump-news-strait-hormuz-blockade-ceasefire-tensions-may-22"
},
{
  "title": "イラン最高指導者「60%濃縮ウランを国外移送しない」——核交渉に深刻な障壁",
  "body": "最高指導者モジュタバ・ハメネイ師が、60%純度の濃縮ウランを国外に移送しない指令を発したと複数のイラン当局者がロイターに証言。米国が和平の条件として「ウランの国外移送」を求め、トランプ大統領がイスラエルにも約束していたため、核交渉の最大の障壁となった。ハメネイ師側近は「国外移送は将来の攻撃に対してイランをより脆弱にする」と説明。",
  "sourceLabel": "Reuters / Algemeiner",
  "date": "2026/05/21",
  "label": "☢️ 核問題",
  "url": "https://www.algemeiner.com/2026/05/21/supreme-leader-says-enriched-uranium-must-stay-iran-iranian-sources-say/"
}
```

### `staleNotice` フィールドの更新

本日は進展あり（戦争権限決議・PGSA・ウラン指令）のため：

```json
"staleNotice": ""
```

（空文字に設定）

### `updated` フィールドの更新

```json
"updated": "2026年5月23日 08:56 日本時間JST"
```

### `osint` 配列の更新

**操作:** 新規記事を配列先頭に追加。既存の `isLatest: true` 記事を `isLatest: false` に変更してそのまま残す。

```json
{
  "isLatest": true,
  "date": "2026/05/22",
  "titleJa": "Al Jazeera ライブブログ：「和平合意に向けた前進の兆し」——米イラン交渉",
  "titleEn": "Iran war live: Signs of progress amid efforts to reach US-Iran peace deal",
  "country": "カタール（アル・ジャジーラ）",
  "media": "Al Jazeera",
  "cardBg": "rgba(20,83,45,0.15)",
  "cardBorder": "rgba(34,197,94,0.3)",
  "badgeColor": "#4ade80",
  "borderColor": "rgba(34,197,94,0.5)",
  "textColor": "#86efac",
  "url": "https://www.aljazeera.com/news/liveblog/2026/5/22/iran-war-live-signs-of-progress-amid-efforts-to-reach-us-iran-peace-deal",
  "body": "パキスタン当局者が「集中的な仲介活動」中と報告。イラン当局者の一人は「合意は近い」と述べる一方、別の当局者は「最終合意に達するかは時期尚早」とコメント。イランのISNAは「双方がメッセージと草案テキストを交換し、正式な合意枠組みの構築に努力している」と報道。米国で対イラン戦争に反対する世論が60%に達したとの世論調査も。"
}
```

既存の直前の `isLatest: true` 記事（前回追加分）を `"isLatest": false` に変更すること。

-----

## [S11] 更新ログ追記

**対象:** `<!--出典・更新ログ-->` セクション内の更新履歴

**操作:** 先頭行に本日分を追記し、11件目を `update_log.json` の先頭に移動して削除。

**追記する先頭行:**

```html
<div style="padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.05);font-size:0.80rem;color:#94a3b8;">
  <span style="color:#60a5fa;font-weight:600;">2026/05/23 08:56</span>
  　米下院戦争権限決議採決回避・ルビオ「PGSA違法」発言・最高指導者ウラン国内保有指令・カタール・パキスタン集中仲介を反映。WTI $96〜98/bbl。
</div>
```

-----

## JSON-LD dateModified の更新（毎回必須）

**対象:** `docs/index.html` 内の JSON-LD `dateModified` フィールド

**old_str:**

```
"dateModified": "2026-05-22",
```

**new_str:**

```
"dateModified": "2026-05-23",
```

-----

## ✅ 出力前セルフチェック

```
[x] S01 ヘッダー ― 2026年5月23日 08:56 JST が入っているか
[x] S02 TICKER ― 本日の主要ニュース5件が反映されているか / JST付きか
[x] S03 速報インシデント ― 米下院戦争権限決議採決回避（5/21）が入っているか ← 最重要確認
[x] S04 情勢カード3枚 ― 封鎖84日目・PGSA35隻・WTI $96〜98 が更新されているか
[x] S05 COUNTDOWN ― 停戦・集中交渉フェーズ（84日目）になっているか
[x] S06 シナリオ確率補足バナー ― 5/23日付・A↑B→C↑D→ が入っているか ← 最重要確認
[x] S07 シナリオ4本 ― タイトルと本文が最新情勢（PGSA・ウラン指令・議会動向）を反映しているか
[x] S07 シナリオC・D ― CはPGSA恒久化、DはCENTCOM計画・議会圧力・イスラエル圧力で差別化 ← 品質チェック
[x] S07 シナリオC・D ― WTI価格レンジ C:$100〜115 vs D:$115〜135 で差別化 ← 数値確認
[x] S08 シナリオフッター ― 次の焦点5点（議会決議6/3・ムニル訪問・ウラン・PGSA制裁・IEA）が最新か
[x] S08.5 全ルート現況サマリー ― 2026年5月23日 08:56 JST 再確認済 になっているか
[x] S09 30秒カラム ― 3行サマリーとバッジ5枚が全て更新されているか（最後に書いたか）
[x] S10 news_data.json メモ ― アーカイブ注意事項（配列先頭追加・isLatest:false 変更）が記載されているか
[x] S10 osint ― 2026/05/22 の Al Jazeera ライブブログ（URL確認済）が追加されているか
[x] S10 osint ― 配列ごと置き換えになっていないか（先頭追加・既存 isLatest:false 変更になっているか）
[x] S11 更新ログ ― 先頭行に 2026/05/23 分が追記されているか
[x] JSON-LD dateModified ― 2026-05-23 に更新されているか
[x] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[x] 全体 ― ニュースURLにAI捏造・推測URLが混入していないか（全URL web検索で確認済み）
[x] 全体 ― 📰関連最新ニュースにAl Jazeeraが混入していないか（osintのみに掲載）
[x] 全体 ― 人名が日本語表記になっているか（モジュタバ・ハメネイ、ルビオ、トランプ、ムニル）
[x] S07 シナリオC・D 内容差別化 ― C=PGSA制度定着・恒久化 vs D=議会圧力・CENTCOM計画・イスラエル先制攻撃リスク
```

-----

## 参考：本日使用した主要ソース（URL確認済み）

|記事内容                     |ソース               |URL                                                                                                                                        |
|-------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
|米下院戦争権限決議採決回避            |NPR               |<https://www.npr.org/2026/05/22/g-s1-123592/republicans-call-off-vote-on-iran-war-resolution>                                              |
|ルビオ「PGSA違法」・若干の前進        |Fox News Live     |<https://www.foxnews.com/live-news/iran-war-trump-news-strait-hormuz-blockade-ceasefire-tensions-may-22>                                   |
|カタール・パキスタン仲介             |Irish Times       |<https://www.irishtimes.com/world/middle-east/2026/05/22/qatar-sends-mediators-to-tehran-as-talks-to-reopen-strait-of-hormuz-reach-climax/>|
|PGSA・ルビオ「違法」発言           |gCaptain/Bloomberg|<https://gcaptain.com/iran-and-oman-discuss-hormuz-toll-regime-as-rubio-warns-it-cant-happen/>                                             |
|イランウラン国内保有指令             |Algemeiner        |<https://www.algemeiner.com/2026/05/21/supreme-leader-says-enriched-uranium-must-stay-iran-iranian-sources-say/>                           |
|Al Jazeera ライブブログ（osint用）|Al Jazeera        |<https://www.aljazeera.com/news/liveblog/2026/5/22/iran-war-live-signs-of-progress-amid-efforts-to-reach-us-iran-peace-deal>               |
|WTI油価動向（5/22）            |Trading Economics |<https://tradingeconomics.com/commodity/crude-oil>                                                                                         |
|PGSA正式稼働・X開設             |Maritime Executive|<https://maritime-executive.com/article/iran-s-persian-gulf-strait-authority-takes-steps-towards-operations>                               |
|米上院・戦争権限決議前進             |CBS News          |<https://www.cbsnews.com/news/house-gop-pulls-iran-war-resolution-vote/>                                                                   
