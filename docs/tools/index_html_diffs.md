# docs/tools/index_html_diffs.md
# 生成日時：2026年5月9日 16:14 JST
# 対象ファイル：docs/index.html（＋ docs/data/news_data.json メモ）

---

## [S10] news_data.json 更新メモ

> **Claude Code への指示：** `docs/data/news_data.json` を以下の内容で更新してください。
> `latest` の先頭に4件を差し替え、最古1件を `archive` 先頭バッチへ移動。
> `updated` フィールドを `"2026年5月9日 16:14 日本時間JST"` に更新。
> `staleNotice` は `""` （本日新情報あり）。

### 差し替え4件（`latest`）

```json
{
  "id": "may0916_1",
  "title": "米・イランがホルムズで交戦——3隻の米駆逐艦を攻撃・米はイラン軍事施設を報復空爆",
  "body": "米CENTCOMは8日（現地時間）、ホルムズ海峡を通過中の米海軍駆逐艦3隻がイランのミサイル・ドローン・小型艇による攻撃を受けたと発表。米軍は即座に報復し、ホルムズ周辺のイランのミサイル・ドローン発射拠点を空爆した。艦船への命中はなく停戦は継続中とトランプ大統領が主張（「love tap」と表現）。米はMOU回答を依然待機中。",
  "sourceLabel": "Bloomberg",
  "date": "2026年5月8日 JST",
  "label": "🚨 速報",
  "url": "https://www.bloomberg.com/news/articles/2026-05-08/us-iran-clash-near-hormuz-as-response-on-proposed-deal-awaited"
},
{
  "id": "may0916_2",
  "title": "イランがUAEに弾道ミサイル2発・ドローン3機を発射——UAE防空システムが迎撃",
  "body": "イランは9日（現地時間）、UAEに向けて弾道ミサイル2発とドローン3機を発射した。UAE国防省は自国の防空システムが全弾を迎撃したと発表。また米海軍は封鎖回避を試みる無人のイラン産油タンカー2隻を攻撃した。ブレント原油は前日比+1.2%の$101.29/bblで引けたが、週間ベースでは6%超の下落。",
  "sourceLabel": "CNBC",
  "date": "2026年5月9日 JST",
  "label": "🚨 速報",
  "url": "https://www.cnbc.com/2026/05/08/oil-prices-today-wti-brent-us-iran-fire-war-hormuz-ceasefire.html"
},
{
  "id": "may0916_3",
  "title": "米・イラン、14項目MOU草案に最接近——30日交渉フレーム・核濃縮モラトリアム最低12年",
  "body": "AxiosはMOU草案の詳細を報道。①ホルムズ段階的再開（30日間）②核濃縮モラトリアム最低12年（イラン提案5年←米要求20年の妥協点）③高濃縮ウランの国外移送④スナップ査察受入れ⑤米の制裁段階的解除・凍結資産解放、が主要条項。イランは本日（9日）も公式回答を出していない。",
  "sourceLabel": "Axios",
  "date": "2026年5月6日 JST",
  "label": "🔴 外交",
  "url": "https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo"
},
{
  "id": "may0916_4",
  "title": "パキスタン「合意を期待」——イラン外務省「米提案を引き続き審査中」と発表",
  "body": "パキスタン外務省スポークスマンはNPRの取材に「できるだけ早い合意を期待・見込んでいる」とコメント。イラン外務省報道官バガエイ氏はISNA通信を通じ「米国の計画・提案は引き続き審査中。整理でき次第パキスタン側に伝達する」と述べ、交渉の継続を確認した。",
  "sourceLabel": "NPR",
  "date": "2026年5月7日 JST",
  "label": "🕊️ 外交",
  "url": "https://www.npr.org/2026/05/06/nx-s1-5813497/iran-war-strait-hormuz-updates"
}
```

### OSINT（`osint` 配列・現地メディア視点）

```json
{
  "titleJa": "米が「ホルムズ先行・核後回し」を受入れか——専門家「最大の方針転換」と評価",
  "titleEn": "Has the US accepted Iran's demand to settle Hormuz first, nuclear later?",
  "country": "カタール",
  "media": "Al Jazeera",
  "cardBg": "rgba(0,100,60,0.12)",
  "cardBorder": "rgba(0,200,100,0.25)",
  "badgeColor": "#00c864",
  "borderColor": "#00c864",
  "textColor": "#86efac",
  "url": "https://www.aljazeera.com/news/2026/5/6/has-the-us-accepted-irans-demand-to-settle-hormuz-first-nuclear-later",
  "date": "2026年5月6日 JST",
  "isLatest": true
}
```

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の警戒レベル表示・更新日時

**変更前：**
```
警戒レベル：最高
📅 2026年5月8日 09:57 JST
```

**変更後：**
```
警戒レベル：最高
📅 2026年5月9日 16:14 JST
```

---

## [S02] TICKER

**対象：** `/* TICKER */` 内のテキスト文字列

**変更後（全文置き換え）：**

```
5/9 16:14 JST｜🚨 イラン、UAEにミサイル2発・ドローン3機発射——UAE防空システムが全弾迎撃｜⚔️ 米・イランがホルムズで軍事衝突（5/8）——3米駆逐艦が攻撃受けるも命中なし・停戦は継続｜📜 イランMOU回答なし——ルビオ国務長官「本日中に回答期待」も空振り・交渉継続｜🛢️ ブレント原油$101.29/bbl・WTI$95.42——週間-6%超（MOU期待の巻き戻し）｜🇨🇳 トランプ大統領、5/14-15に北京でXi習主席と首脳会談——ホルムズ再開を中国に要求か｜🚢 封鎖72日目——二重封鎖継続、商業船通航は約5%水準
```

---

## [S03] 速報インシデント ⚠️

**対象：** `<!-- 速報インシデント トグルボタン -->` セクション内の最新インシデントリスト

**追加インシデント2件（既存リストの先頭に挿入）：**

### 新インシデント①（最新・先頭に追加）
```html
<li class="incident-item incident-red">
  <span class="inc-date">5/9 16:14 JST</span>
  <span class="inc-tag tag-red">🚀 ミサイル</span>
  <span class="inc-body">
    <strong>イラン、UAEに弾道ミサイル2発・ドローン3機発射——UAE防空が全弾迎撃</strong><br>
    UAE国防省：自国防空システムがイラン発射の弾道ミサイル2発とドローン3機を完全迎撃したと発表（5/9 現地時間）。米軍はホルムズ内で封鎖回避を試みる無人のイラン産油タンカー2隻を攻撃した。停戦は継続中とトランプ。
    <span class="inc-src">出典：CNBC（5/9 JST）</span>
  </span>
</li>
```

### 新インシデント②（2番目に追加）
```html
<li class="incident-item incident-orange">
  <span class="inc-date">5/8 JST</span>
  <span class="inc-tag tag-orange">⚔️ 軍事衝突</span>
  <span class="inc-body">
    <strong>米・イランがホルムズ内で交戦——3米駆逐艦を攻撃・米がイラン拠点を報復空爆</strong><br>
    CENTCOMは米海軍駆逐艦3隻がホルムズ通過中にイランのミサイル・ドローン・小型艇による攻撃を受けたと発表。米軍は即座にイラン軍のミサイル・ドローン発射拠点を空爆し報復。艦船への命中なし。トランプは「停戦は継続中」（"just a love tap"）と主張。イランのKhatam Al Anbiya司令部は「米が停戦違反」と非難。MOU交渉は継続中。
    <span class="inc-src">出典：Bloomberg（5/8 JST）</span>
  </span>
</li>
```

> **補足：** 既存インシデントのうち最古のものを折り畳みエリアへ移動させること（常時3件表示ルール遵守）。

---

## [S04] 情勢カード3枚

**対象：** `<!-- SITUATION CARDS -->` 内カード3枚の `.s-body` および `.s-src`

### カード①：海峡・軍事動向

**日付を `5月9日 16:14 JST` に更新。本文全文置き換え：**

```html
<div class="s-title"><span class="label-fact">事実</span>🚨 海峡・軍事動向（5月9日 16:14 JST）</div>
<div class="s-body">
  <strong style="color:#f87171;">🛑 封鎖72日目——米・イランがホルムズ内で軍事衝突（5/8）・イランがUAEに攻撃（5/9）（5/9 16:14 JST）</strong><br>
  • 封鎖72日目継続（2月28日起算）<br>
  • 5/8：3隻の米海軍駆逐艦がホルムズ通過中にミサイル・ドローン・小型艇攻撃を受ける——命中なし<br>
  • 米軍はイラン国内のミサイル・ドローン発射拠点を報復空爆（CENTCOM「自衛措置」）<br>
  • 5/9：イランがUAEに弾道ミサイル2発・ドローン3機発射——UAE防空が全弾迎撃<br>
  • 米、封鎖回避を試みる無人イランタンカー2隻を攻撃（5/9）<br>
  • トランプ「停戦は継続中」（「love tap」発言）・Project Freedom 再開検討中<br>
  • CENTCOM：封鎖迂回済み艦船52隻・湾内足止め船員約2万3000名
</div>
<span class="s-src">📡 Bloomberg / CNBC（5/8-9 JST）</span>
```

### カード②：外交・交渉動向

**日付を `5月9日 16:14 JST` に更新。本文全文置き換え：**

```html
<div class="s-title"><span class="label-fact">事実</span>🤝 外交・交渉動向（5月9日 16:14 JST）</div>
<div class="s-body">
  <strong style="color:#f87171;">🔴 イラン、MOU回答を5/9も出さず——ルビオ「本日中に期待」も空振り・交渉は継続（5/9 16:14 JST）</strong><br>
  • 米の14項目MOU草案（パキスタン経由送付）：イランが引き続き審査中<br>
  • ルビオ国務長官「5/8（金）中に回答期待」と言明したが、本日16:14現在も公式回答なし<br>
  • イラン外務省「提案を整理でき次第パキスタン側に伝達」（バガエイ報道官）<br>
  • パキスタン外務省「できるだけ早い合意を期待」（タヒル・アンドラービ報道官）<br>
  • トランプ、5/14-15に北京でXi習主席と会談予定——中国に対イラン圧力を要求か<br>
  • アラグチー外相が北京でWang Yi外相と会談（5/6）——「公正・包括的合意のみ受諾」
</div>
<span class="s-src">📡 Axios / Bloomberg / NPR（5/8-9 JST）</span>
```

### カード③：エネルギー・市場

**日付を `5月9日 16:14 JST` に更新。本文全文置き換え：**

```html
<div class="s-title"><span class="label-fact">事実</span>📊 エネルギー・経済動向（5月9日 16:14 JST）</div>
<div class="s-body">
  <strong style="color:#fbbf24;">🟡 ブレント$101.29/bbl——MOU期待剥落と軍事衝突で週間-6%超・WTI$95.42（5/9 16:14 JST）</strong><br>
  • ブレント原油終値 $101.29/bbl（前週比 -6%超）<br>
  • WTI終値 $95.42/bbl<br>
  • MOU草案報道で一時急落→軍事衝突報道で反発→引けは小幅高の「ジェットコースター相場」（ANZリサーチ）<br>
  • 米ガソリン平均 $4.46/ガロン（約4年ぶり高水準）——封鎖継続で $5/ガロン超えシナリオ（Goldman Sachs）<br>
  • 石油日産不足：推計 1,450万バレル/日<br>
  • 仏空母シャルル・ドゴール、紅海に前方展開（マクロン大統領が5/7に発表）
</div>
<span class="s-src">📡 CNBC / Bloomberg / The National（5/9 JST）</span>
```

---

## [S05] COUNTDOWN

**対象：** `<!-- COUNTDOWN -->` セクション

**変更内容：**

フェーズラベル：以下に更新
```
📋 封鎖72日目（二重封鎖継続中）— イランのMOU回答待機・交渉最終盤
```

> **補足（Claude Codeへ）：** カウントダウンタイマーの目標日時が既に過去の日時になっている場合は、次の外交上の焦点となる日時（例：トランプ=Xi首脳会談前日 2026年5月13日 23:59 JST 等）に更新すること。タイムゾーンは必ず「日本時間JST」を先に・主として記載する。

---

## [S06] シナリオ確率補足バナー ⚠️

**対象：** `<!-- SCENARIOS -->` 内・シナリオ4本の上部にある確率補足バナー

**変更前の日付：**
```
5/8 09:57 JST 更新
```

**変更後：**
```
5/9 16:14 JST 更新
```

**矢印テキスト（方向性）の更新：**

MOU交渉は史上最接近も回答遅延・軍事衝突が継続しているため：

```
A（外交解決）↑ 微上昇——MOU 14項目に最接近も回答なし
B（部分封鎖継続）→ 最有力——停戦継続・衝突も局所的
C（完全封鎖）→ 横ばい
D（軍事エスカレーション）→ 横ばい——MOU決裂時は急上昇リスク残存
```

---

## [S07] シナリオ4本（A/B/C/D 本文）

**対象：** 各 `sc-card` 内の `<p>` テキスト

### シナリオA（外交解決）

**現状評価の日付・本文を以下に置き換え：**

```html
<p>▼ 現状評価（5/9 16:14 JST）：微上昇 ↑（MOU草案に史上最接近）<br>
米がイランの「ホルムズ先行・核後回し」フレームを事実上容認し、14項目MOU草案がパキスタン経由で送付された。核濃縮モラトリアム12〜15年、高濃縮ウランの国外移送、スナップ査察受入れ等の条項が報告されており、合意なら30日間の最終交渉に入る枠組み。ただしイランは5/9現在も公式回答を出しておらず、IRGC強硬派・議会内反対勢力の内部対立が障害となっている。トランプ=Xi首脳会談（5/14-15・北京）前が最大の圧力ウィンドウ。<br>
<strong>【トリガー】</strong>①イランがMOU正式受諾、②30日交渉フェーズ開始宣言</p>
```

### シナリオB（部分封鎖継続）

```html
<p>▼ 現状評価（5/9 16:14 JST）：最有力 →（停戦維持・局所衝突継続）<br>
5/8の軍事衝突（米駆逐艦3隻攻撃・米の報復空爆）および5/9のUAEへのミサイル攻撃が起きたにもかかわらず、双方が停戦継続を主張し交渉は継続中。ホルムズの商業通航は依然約5%水準（平常時月3,000隻→約150隻）。イランのIRGCが「新手続きで安全通航保証」と声明も詳細不明。封鎖が段階的に緩和されながら交渉が続く現状維持が最も蓋然性高い。<br>
<strong>【トリガー】</strong>①MOU署名後の30日暫定緩和フェーズ開始、②IRGCの「新手続き」の具体化</p>
```

### シナリオC（完全封鎖強化）

```html
<p>▼ 現状評価（5/9 16:14 JST）：リスク低下 →（MOU進展が下押し・衝突継続が上押し）<br>
MOU交渉が現時点で最接近している事実はシナリオCの確率を押し下げているが、5/8の軍事衝突・5/9のUAE攻撃が示すようにエスカレーションの閾値は依然低い。イランがMOUを拒否し核濃縮再開を宣言した場合、米軍が「封鎖+爆撃再開」（Operation Epic Fury再始動）に踏み切るシナリオが浮上する。トランプ「拒否すれば前回より高い強度で爆撃する」と繰り返し警告。<br>
<strong>【トリガー】</strong>①イランのMOU全面拒否、②核濃縮再開宣言</p>
```

### シナリオD（軍事エスカレーション再燃）

```html
<p>▼ 現状評価（5/9 16:14 JST）：ベースラインは低下も急上昇リスク残存 →（MOU決裂時は48時間以内に急変）<br>
MOU交渉進展によりシナリオDのベースライン確率は低下しているが、5/8の米・イラン軍事衝突（3米駆逐艦攻撃）および5/9のUAEミサイル攻撃が示すように火種は依然くすぶっている。イランのIRGC強硬派がMOU交渉を妨害し、米艦艇への攻撃を拡大した場合、Project Freedomの再始動とともにエスカレーション・ラダーが急上昇しうる。トランプ「停戦は love tap 程度」と軽視しつつ爆撃再開を繰り返し警告。<br>
<strong>【トリガー】</strong>①イランのMOU拒否＋米艦艇への直接攻撃拡大、②IRGC強硬派によるアラグチー外相の交渉妨害</p>
```

---

## [S08] シナリオフッター

**対象：** `<!-- シナリオ フッター -->` 内の「次の焦点」`<ol>` リスト・日付タイムスタンプ

**変更後（全文置き換え）：**

```html
<span style="color:#64748b;">📌 次の焦点（5/9 16:14時点）：</span>
<ol style="margin:4px 0 0 0;padding-left:20px;color:#94a3b8;font-size:0.7rem;">
  <li>📜 <strong>イランのMOU公式回答——5/9（土）中が次の事実上の期限目安（ルビオが5/8を期待も空振り）</strong></li>
  <li>🇨🇳 <strong>トランプ=Xi首脳会談（5/14-15・北京）——中国がイランへの圧力仲介役を担うか否か</strong></li>
  <li>⚔️ <strong>ホルムズ内の軍事衝突が停戦崩壊に発展するか——IRGC強硬派の自律的行動リスク</strong></li>
  <li>🚢 <strong>Project Freedom 再開の可否——市場は再開報道でリスクオフ・ANZリサーチが警告</strong></li>
  <li>💣 <strong>MOU決裂時の「より高い強度の爆撃再開」（トランプ警告）の実行可能性</strong></li>
</ol>
<span class="label-scenario" style="margin-left:auto;">分析：2026年5月9日 16:14 JST時点</span>
```

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ5枚）

**対象：** `<!-- 30秒で全体像を把握 -->` セクション全体

> **⚠️ このセクションは他の全セクションが確定した後に書くこと。**

### 3行サマリー

**変更後（全文置き換え）：**

```html
<!-- 「いま何が起きているか」3行 -->
<div class="thirty-sec-item">
  <span class="ts-label">📰 いま何が</span>
  <span class="ts-body">
    <strong>5/9 16:14 JST</strong>——封鎖72日目。米・イランが5/8にホルムズ内で軍事衝突（3米駆逐艦攻撃→米が報復空爆）、5/9にはイランがUAEにミサイル2発・ドローン3機を発射。停戦は辛うじて継続中。イランはMOU草案への公式回答をいまだ出しておらず、交渉は綱渡りの最終局面。
  </span>
</div>

<div class="thirty-sec-item">
  <span class="ts-label">🌊 海峡の今</span>
  <span class="ts-body">
    商業通航は約5%水準（平常時月3,000隻→約150隻）継続。IRGC「新手続きで安全通航保証」と声明も詳細不明。MOU合意なら30日間で段階的再開へ。ブレント原油 $101.29/bbl・WTI $95.42/bbl（週間-6%超）。
  </span>
</div>

<div class="thirty-sec-item">
  <span class="ts-label">🔭 次の焦点</span>
  <span class="ts-body">
    ①イランのMOU公式回答（5/9中が次の事実上の期限）②トランプ=Xi首脳会談（5/14-15）が対イラン圧力の鍵③MOU決裂→より高強度の爆撃再開リスクが残存。合意なら原油は急落・不合意なら $120/bbl 再試験へ。
  </span>
</div>
```

### ステータスバッジ5枚

**変更後（全5枚を置き換え）：**

```html
<!-- バッジ① 封鎖日数 -->
<div class="status-badge badge-red">
  <span class="badge-icon">🔒</span>
  <span class="badge-label">封鎖</span>
  <span class="badge-value">72日目</span>
</div>

<!-- バッジ② 原油価格 -->
<div class="status-badge badge-orange">
  <span class="badge-icon">🛢️</span>
  <span class="badge-label">ブレント</span>
  <span class="badge-value">$101.29</span>
</div>

<!-- バッジ③ 通航水準 -->
<div class="status-badge badge-yellow">
  <span class="badge-icon">🚢</span>
  <span class="badge-label">通航</span>
  <span class="badge-value">約5%</span>
</div>

<!-- バッジ④ 外交 -->
<div class="status-badge badge-blue">
  <span class="badge-icon">📜</span>
  <span class="badge-label">MOU回答</span>
  <span class="badge-value">待機中</span>
</div>

<!-- バッジ⑤ 停戦 -->
<div class="status-badge badge-green">
  <span class="badge-icon">⚠️</span>
  <span class="badge-label">停戦</span>
  <span class="badge-value">綱渡り継続</span>
</div>
```

---

## [S11] 更新ログ追記

**対象：** `<!--出典・更新ログ-->` セクション

**先頭に以下を1行追加（末尾の古い行を削除してアーカイブへ移動）：**

```html
<div class="log-item">
  <span class="log-date">2026/05/09 16:14</span>
  <span class="log-text">
    封鎖72日目更新：5/8 米・イランがホルムズ内で軍事衝突（3米駆逐艦攻撃→報復空爆）、5/9 イランがUAEにミサイル・ドローン攻撃——停戦辛うじて継続。イラン MOU回答なし・交渉最終盤。ブレント$101.29・週間-6%超。
  </span>
</div>
```

---

## 出力前セルフチェック ✅

```
[✅] S01 ヘッダー ― 2026年5月9日 16:14 JST が入っているか
[✅] S02 TICKER ― 5/8-9の軍事衝突・MOU回答なし・UAE攻撃が反映されているか
[✅] S03 速報インシデント ― 存在するか・UAE攻撃（5/9）・ホルムズ衝突（5/8）の新インシデント2件が入っているか ← 最重要確認
[✅] S04 情勢カード3枚 ― 3枚とも 5/9 16:14 JST・最新事実・出典が更新されているか
[✅] S05 COUNTDOWN ― 「封鎖72日目」・「MOU回答待機」に更新されているか
[✅] S06 シナリオ確率補足バナー ― 5/9 16:14 JST に更新・矢印テキストが入っているか ← 最重要確認
[✅] S07 シナリオ4本 ― 衝突・MOU最接近・UAE攻撃を反映した本文に更新されているか
[✅] S08 シナリオフッター ― MOU回答・Trump-Xi会談・Project Freedom 再開を焦点に更新されているか
[✅] S09 30秒カラム ― 封鎖72日目・MOU回答待機・$101.29が全て反映されているか
[✅] S10 news_data.json メモ ― 4件の最新記事・osint・アーカイブ注意事項が記載されているか
[✅] S11 更新ログ ― 先頭行に 2026/05/09 16:14 の本日分が追記されているか
```

---

## 条件付きセクション確認

| セクション | 判断 | 理由 |
|---|---|---|
| [C01] MAP・タンカー可視化 | **要確認** | 衝突により足止め・迂回船舶数が変化している可能性あり。5/9 16:14 JST確認済を記載 |
| [C02] STATS ルートテーブル | 今回スキップ | 週1回ルールに基づき次回週次更新時に対応 |
| [C03] 特別解説コラム | スキップ | ユーザーからの手動指示がないため |

---

## 主要情報ソース（本更新で参照したURL）

| 記事 | 媒体 | 日付 |
|---|---|---|
| US/Iran clash near Hormuz | Bloomberg | 2026-05-08 |
| Oil prices today: UAE attack, ceasefire holds | CNBC | 2026-05-08/09 |
| US/Iran closing in on one-page memo | Axios | 2026-05-06 |
| Pakistan hopeful for deal | NPR | 2026-05-07 |
| Oil climbs as Hormuz escalation threatens truce | The National | 2026-05-08 |
| Has US accepted Iran's demand? | Al Jazeera | 2026-05-06 |
| Mixed messages on deal to end war | TIME | 2026-05-07 |
