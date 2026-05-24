# index_html_diffs.md — 2026年5月24日 08:40 日本時間JST

> **Claude Code への指示：以下の変更を `docs/index.html` に適用してください。**
> **変更箇所以外は絶対に触らないこと。**
> **作業後に `git commit`（メッセージ: `update: 2026-05-24 情勢更新`）してください。pushは確認後に指示します。**

---

## [S10] news_data.json 更新メモ

`docs/data/news_data.json` を以下の内容でマージしてください。

### latest（最古の1件を archive 先頭バッチへ移動し、新規2件を先頭に追加）

**新規追加（先頭に追加する2件）:**

```json
{
  "title": "トランプ「合意はほぼ妥結」——ホルムズ再開を含む米・イラン和平、「まもなく発表」と投稿",
  "body": "トランプ大統領は5月23日、米国・イラン・関係各国の間で「合意がほぼ妥結された。最終詳細を協議中であり、まもなく発表する」とSNSに投稿した。ホルムズ海峡の再開が合意内容に含まれるとされる。イラン外務省はこれを「枠組み合意」と位置づけ、30〜60日間の詳細交渉を経て最終合意に至るとの認識を示した。",
  "sourceLabel": "NPR",
  "date": "2026年5月23日",
  "label": "🕊️ 外交",
  "url": "https://www.npr.org/2026/05/23/g-s1-124145/trump-iran-deal-strait-of-hormuz"
},
{
  "title": "イランFM「核問題は交渉テーブルに乗せない」——米の最重要条件と真っ向対立、枠組み協議に重大障壁",
  "body": "イランのアラグチ外相は5月23日、今回の枠組み合意の交渉対象に「核プログラムは含まれない」と明言した。米国のルビオ国務長官がホルムズ再開の条件として「核兵器取得の阻止・濃縮ウランの引き渡し」を掲げているのと真っ向から対立。合意の「詳細化」フェーズに向けて根本的な隔たりが残ることが改めて浮き彫りとなった。",
  "sourceLabel": "CNBC",
  "date": "2026年5月23日",
  "label": "⚠️ 交渉難航",
  "url": "https://www.cnbc.com/amp/2026/05/23/us-iran-war-talks.html"
}
```

**archive へ移動（現 latest 最古の1件）:** 既存 latest の最古記事を archive 先頭バッチへ移動してください。

### osint（先頭に追加、既存は isLatest: false に変更）

```json
{
  "titleJa": "「合意はほぼ妥結」——トランプ発表にイラン「枠組み合意」で応答、核問題は交渉テーブルに乗せないと拒否",
  "titleEn": "Trump says Iran 'agreement has been largely negotiated'; Tehran calls it framework deal, rejects nuclear talks",
  "country": "カタール",
  "media": "Al Jazeera",
  "cardBg": "rgba(20,83,45,0.25)",
  "cardBorder": "rgba(34,197,94,0.3)",
  "badgeColor": "#22c55e",
  "borderColor": "rgba(34,197,94,0.4)",
  "textColor": "#86efac",
  "url": "https://www.aljazeera.com/news/liveblog/2026/5/23/iran-war-live-tehran-says-diplomacy-continues-but-no-deal-yet-with-us",
  "date": "2026年5月24日",
  "isLatest": true
}
```

> ⚠️ osint 配列ごとの置き換えは禁止。既存の isLatest: true だった記事（ムニル訪問件）を `"isLatest": false` に変更し、上記を配列先頭に追加すること。

### updated フィールド

```
"updated": "2026年5月24日 08:40 日本時間JST"
```

### staleNotice

```
"staleNotice": ""
```

（本日は重大進展あり——空文字）

---

## [S03] 速報インシデント

**対象:** `<!-- 速報インシデント トグルボタン -->` 内のトグルボタン日付バッジと先頭インシデントカード

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
📅 5/23 09:58 更新
<!-- OLD:END -->
<!-- NEW:START -->
📅 5/24 08:40 更新
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント先頭カード（新規追加 — 既存の先頭カードの直前に挿入）

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="incident-card" style="border-left:4px solid #f59e0b;background:rgba(245,158,11,0.08);padding:12px 14px;border-radius:6px;margin-bottom:10px;">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
    <span style="font-size:0.75rem;font-weight:700;color:#f59e0b;letter-spacing:0.05em;">🏛️ 議会動向</span>
    <span style="font-size:0.72rem;color:#94a3b8;">2026年5月21日 日本時間JST</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="incident-card" style="border-left:4px solid #ef4444;background:rgba(239,68,68,0.08);padding:12px 14px;border-radius:6px;margin-bottom:10px;">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
    <span style="font-size:0.75rem;font-weight:700;color:#f87171;letter-spacing:0.05em;">🕊️ 最重要外交</span>
    <span style="font-size:0.72rem;color:#94a3b8;">2026年5月23日 日本時間JST</span>
  </div>
  <p style="font-size:0.88rem;color:#e2e8f0;line-height:1.6;margin:0;">
    <strong>トランプ「米・イラン合意はほぼ妥結」と発表——ホルムズ再開を含む和平、「まもなく発表」。</strong>
    5月23日夜（日本時間）、トランプ大統領がSNSに「合意がほぼ妥結された」と投稿。イラン外務省は「枠組み合意」として30〜60日の詳細交渉を主張。ただし、イランのアラグチ外相は「核プログラムは交渉対象に含まれない」と明言しており、米国のルビオ国務長官が設定した3条件（核兵器阻止・通行料なし・濃縮ウラン引き渡し）との間に根本的な隔たりが残る。枠組みと最終合意の間には依然として長い距離がある。
  </p>
  <p style="font-size:0.78rem;color:#94a3b8;margin:6px 0 0;">📰 出典：NPR・CNBC・Al Jazeera（2026年5月23日）</p>
</div>
<div class="incident-card" style="border-left:4px solid #f59e0b;background:rgba(245,158,11,0.08);padding:12px 14px;border-radius:6px;margin-bottom:10px;">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
    <span style="font-size:0.75rem;font-weight:700;color:#f59e0b;letter-spacing:0.05em;">🏛️ 議会動向</span>
    <span style="font-size:0.72rem;color:#94a3b8;">2026年5月21日 日本時間JST</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象:** `/* TICKER */` セクション内の ticker-text

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年5月23日 09:58 JST） -->
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年5月24日 08:40 JST） -->
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
🔴 5/23 09:58 JST パキスタン軍参謀長ムニルがテヘランへ——仲介外交が新局面、イラン「合意にはほど遠い」と牽制（Al Jazeera）
<!-- OLD:END -->
<!-- NEW:START -->
🔴 5/24 08:40 JST トランプ「合意はほぼ妥結」——ホルムズ再開含む米・イラン和平「まもなく発表」（NPR/CNBC）｜🔴 5/23 JST イランFM「核問題は交渉テーブルに乗せない」——ルビオの3条件と根本対立・枠組みと最終合意の間に大きな溝（CNBC）｜🟡 5/23 JST 過去24時間で35隻がホルムズ通過——イランが「調整」と発表、選別通航が継続（イラン国家メディア）｜🟡 5/23 JST EUがホルムズ封鎖でイランへの追加制裁を検討中｜🟡 5/22 JST WTI $96〜98——停戦期待で週間4%超下落、トランプ発表で月曜市場はさらに反応見込み｜⚠️ 停戦継続中・海峡通航量は依然戦前比95%減——封鎖86日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

**対象:** `<!-- SITUATION CARDS -->` セクション

### カード①：封鎖継続日数

<!-- APPLY:START -->
<!-- OLD:START -->
85<span
<!-- OLD:END -->
<!-- NEW:START -->
86<span
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
2026年5月23日 09:58 JST
<!-- OLD:END -->
<!-- NEW:START -->
2026年5月24日 08:40 JST
<!-- NEW:END -->
<!-- APPLY:END -->

### カード②：WTI原油価格

（WTI価格レンジは変更なし。トランプ発表を受けた月曜の市場動向を注視中。日付・出典のみ更新）

<!-- APPLY:START -->
<!-- OLD:START -->
2026年5月23日｜Trading Economics
<!-- OLD:END -->
<!-- NEW:START -->
2026年5月24日｜Trading Economics（月曜市場動向注視中）
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③：通航量

<!-- APPLY:START -->
<!-- OLD:START -->
2026年5月23日 09:58 JST 再確認済
<!-- OLD:END -->
<!-- NEW:START -->
2026年5月24日 08:40 JST 再確認済
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

**対象:** `<!-- COUNTDOWN -->` セクション

<!-- APPLY:START -->
<!-- OLD:START -->
封鎖85日目
<!-- OLD:END -->
<!-- NEW:START -->
封鎖86日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

**対象:** `<!-- SCENARIOS -->` 内の確率補足バナー（数値は変更しない・矢印と根拠文のみ更新）

<!-- APPLY:START -->
<!-- OLD:START -->
2026年5月23日 09:58 JST
<!-- OLD:END -->
<!-- NEW:START -->
2026年5月24日 08:40 JST
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
ルビオ「わずかな前進」認めるも核ウラン移送でイラン最高指導者が拒否指令——交渉継続中、合意の道筋は依然不透明（Bloomberg 5/22）
<!-- OLD:END -->
<!-- NEW:START -->
トランプ「合意はほぼ妥結」と発表（5/23 NPR/CNBC）↑ ——ただしイランFMが「核問題は交渉対象外」と明言し米3条件と根本対立。「枠組み」と「最終合意」の間に依然大きな溝（Al Jazeera 5/23）
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本

**対象:** `<!-- SCENARIOS -->` 内の各 sc-card

### シナリオA（外交解決シナリオ）

<!-- APPLY:START -->
<!-- OLD:START -->
シナリオA：外交解決——仲介加速も核障壁が最大の壁
<!-- OLD:END -->
<!-- NEW:START -->
シナリオA：外交解決——「ほぼ妥結」も核問題が最終合意の最大障壁
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
パキスタン軍参謀長ムニルのテヘラン訪問など仲介外交が加速。ルビオ国務長官も「わずかな前進」を認めた。しかし最高指導者モジュタバ・ハメネイが「60%濃縮ウランの国外移送は認めない」と指令しており、米国が最重要条件とする核問題で根本的な隔たりが残る。停戦が「合意まで延長」されている間に外交妥結を図る動きは続くが、イラン側は「合意にはほど遠い」と公式には牽制。議会での戦争権限論争もトランプ政権の足かせになりつつある。WTI：$60〜75/bbl（完全再開時）。
<!-- OLD:END -->
<!-- NEW:START -->
トランプ大統領が「合意はほぼ妥結」と発表し外交解決への期待が一気に高まった。イランも「枠組み合意」として30〜60日の詳細交渉フェーズに入ることを認めており、停戦から合意へのロードマップが初めて形を見せた。ただし、イランのアラグチ外相が「核プログラムは交渉対象に含まれない」と明言しており、ルビオが掲げる3条件（核兵器阻止・通行料なし・濃縮ウラン引き渡し）と根本的に対立している。枠組みが最終合意に到達するかは核問題の扱い次第。WTI：$60〜75/bbl（完全再開・正常化時）。
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB（部分的封鎖継続）

<!-- APPLY:START -->
<!-- OLD:START -->
現時点で最も現実的なシナリオ。IRGCによる通行料徴収が既成事実化し、中国・カタール・パキスタン向けの個別通航許可が散発的に続く。米国の港湾封鎖とイランの海峡管理による「二重封鎖」構造が固定化しつつあり、停戦は継続しても通航量は戦前比95%減が続く。ルビオが「わずかな前進」と認めた交渉は継続するが、核問題での隔たりが大きく短期解決は困難。日本の原油調達は代替ルート（喜望峰回り・パイプライン）でかろうじて維持。WTI：$90〜105/bbl。
<!-- OLD:END -->
<!-- NEW:START -->
トランプの「ほぼ妥結」発表後も依然として最も現実的なシナリオ。「枠組み合意」から「最終合意」までの30〜60日間の交渉フェーズ中、IRGCによる海峡の選別管理は継続する。核問題という根本的な隔たりが交渉を長期化させ、その間も通航量は戦前比95%減が続く見込み。イランは1日35隻前後の「調整通航」を認めているが、これは危機前の正常値（1日100隻超）の3割以下。日本の原油調達は喜望峰回り・パイプライン経由で綱渡りが継続。WTI：$85〜105/bbl（合意進展度で変動）。
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC（完全封鎖固定化）

<!-- APPLY:START -->
<!-- OLD:START -->
イランがオマーンとの通行料永続制度の枠組み協議を進めており、ホルムズ海峡の「イラン主権的管理」が既成事実として固定化するリスク。トランプが通行料を「完全に違法」と拒否してもIRGCの実効支配は日々深まっている。最高指導者の核ウラン移送拒否指令が米イラン交渉を行き詰まらせ、長期的な封鎖状態が続く。機雷除去作業に6ヶ月超を要し、保険・物流の正常化にはさらに時間がかかる。日本企業の事業継続計画（BCP）の根本的見直しが不可避。WTI：$105〜120/bbl。
<!-- OLD:END -->
<!-- NEW:START -->
「枠組み合意」が核問題の隔たりを越えられず30〜60日の交渉フェーズで破綻するシナリオ。イランはオマーンとの通行料永続制度協議を継続しており、交渉決裂後にこの制度が既成事実化するリスクが残る。イランFMが「核問題は交渉対象外」と明言したことは、このシナリオの現実性を示すシグナルでもある。トランプ「ほぼ妥結」発表後に市場が楽観を先取りした分、破綻時の原油価格反発は大きい。機雷除去・保険正常化に6ヶ月超を要し、日本企業のBCP根本見直しが不可避。WTI：$108〜122/bbl。
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD（軍事エスカレーション）

<!-- APPLY:START -->
<!-- OLD:START -->
米下院での戦争権限決議論争が示すように、議会内でのトランプ政権への圧力が高まっている。一方でトランプは依然として「最後通告」的な強硬発言を維持しており、パキスタン・カタールの仲介が最終的に失敗した場合には米軍の直接行動再開シナリオが残る。イランの核ウラン移送拒否という強硬姿勢が米国の「レッドライン」に抵触する可能性もある。中東全域に波及する大規模エスカレーションとなれば、日本のエネルギー安全保障は根底から揺らぐ。WTI：$110〜130/bbl（急騰）。
<!-- OLD:END -->
<!-- NEW:START -->
「ほぼ妥結」発表後も、イランの「核問題は交渉対象外」という強硬姿勢が米国の本質的な要求と一致しない場合、30〜60日の詳細交渉フェーズで合意が崩壊し軍事的解決に回帰するシナリオ。ルビオは「外交でも軍事でもこの問題は解決される」と明言しており、外交失敗時の軍事再開オプションは依然として排除されていない。議会での戦争権限論争（6月3日再提起）の行方も変数となる。枠組み合意への楽観が高まるほど、破綻時のエスカレーション速度も速くなるリスクがある。WTI：$115〜135/bbl（急騰）。
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター

**対象:** `<!-- シナリオ フッター -->` セクション

<!-- APPLY:START -->
<!-- OLD:START -->
<h3 style="font-size:0.9rem;font-weight:700;color:#94a3b8;margin:0 0 10px;letter-spacing:0.05em;">📌 次の焦点</h3>
<ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
  <li style="font-size:0.85rem;color:#cbd5e1;">① パキスタン仲介の結果——ムニル陸軍元帥テヘラン訪問の成否（5/23〜24）</li>
  <li style="font-size:0.85rem;color:#cbd5e1;">② 核ウラン移送問題——モジュタバ指令を米国がどう受け止めるか（次回交渉の鍵）</li>
  <li style="font-size:0.85rem;color:#cbd5e1;">③ 米下院での戦争権限決議——6月3日の採決再提起とトランプ政権の対応</li>
  <li style="font-size:0.85rem;color:#cbd5e1;">④ ホルムズ通行料制度——イラン・オマーン協議の行方とトランプの制裁対抗措置</li>
  <li style="font-size:0.85rem;color:#cbd5e1;">⑤ 原油価格動向——停戦期待と核交渉の難航でWTI $90〜105のボックス相場が続くか</li>
</ul>
<!-- OLD:END -->
<!-- NEW:START -->
<h3 style="font-size:0.9rem;font-weight:700;color:#94a3b8;margin:0 0 10px;letter-spacing:0.05em;">📌 次の焦点</h3>
<ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
  <li style="font-size:0.85rem;color:#cbd5e1;">① 「枠組み合意」の詳細交渉入り——30〜60日の協議で核問題の溝を埋められるか（最重要）</li>
  <li style="font-size:0.85rem;color:#cbd5e1;">② 市場の反応——月曜（5/25）の原油市場がトランプ発表をどう織り込むか（WTI方向感）</li>
  <li style="font-size:0.85rem;color:#cbd5e1;">③ ホルムズ段階的再開の条件——枠組み合意とホルムズ通航正常化のタイムライン</li>
  <li style="font-size:0.85rem;color:#cbd5e1;">④ イランFMの核問題発言——米国がこれを「ディールブレーカー」と判断するか否か</li>
  <li style="font-size:0.85rem;color:#cbd5e1;">⑤ 米下院戦争権限決議——6月3日の再提起でトランプ政権の交渉余地がさらに制約されるか</li>
</ul>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

**対象:** `🚢 全ルート現況サマリー` セクションの日付

<!-- APPLY:START -->
<!-- OLD:START -->
2026年5月23日 09:58 JST 再確認済
<!-- OLD:END -->
<!-- NEW:START -->
2026年5月24日 08:40 JST 再確認済
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（必ず最後に記載）

**対象:** `<!-- 30秒で全体像を把握 -->` セクション

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
① 仲介加速も「合意遠い」——パキスタン軍参謀長がテヘランへ、ルビオ「わずかな前進」認めるも最高指導者が核ウラン国外移送を拒否
② ホルムズ通行料の制度化が進行——IRGCが実効支配を継続、85日目も通航量は戦前比95%減
③ 議会でも亀裂——米下院GOP、戦争権限決議を土壇場で延期。6月3日再提起で与野党対立が深刻化
<!-- OLD:END -->
<!-- NEW:START -->
① トランプ「合意はほぼ妥結」——ホルムズ再開含む米・イラン枠組み合意が浮上、だがイランFMは「核問題は交渉対象外」と明言し根本的矛盾が残る
② 86日目も通航量は戦前比95%減——IRGCの選別管理継続、月曜市場はトランプ発表への反応が焦点
③ 枠組みと最終合意の間に30〜60日——詳細交渉フェーズで核・ホルムズ・制裁の3問題すべてを解決できるか不透明
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ5枚

<!-- APPLY:START -->
<!-- OLD:START -->
85日目
<!-- OLD:END -->
<!-- NEW:START -->
86日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S01] ヘッダー日時・警戒レベル

**対象:** `<header>` 内の badge-date

<!-- APPLY:START -->
<!-- OLD:START -->
<span class="badge-item badge-date">📅2026年5月23日 09:58 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span class="badge-item badge-date">📅2026年5月24日 08:40 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

※ 警戒レベルは 🚨 最高 を維持。

---

## [S11] 更新ログ追記

**対象:** `<!--出典・更新ログ-->` セクション

### JSON-LD dateModified の更新（必須）

<!-- APPLY:START -->
<!-- OLD:START -->
"dateModified": "2026-05-23",
<!-- OLD:END -->
<!-- NEW:START -->
"dateModified": "2026-05-24",
<!-- NEW:END -->
<!-- APPLY:END -->

### 更新ログ先頭への追記

<!-- APPLY:START -->
<!-- OLD:START -->
<div>📅 <strong>2026年5月23日 09:58 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div>📅 <strong>2026年5月24日 08:40 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/05/24 08:40</span> — <strong style="color:#fca5a5;">【重大更新（86日目）】</strong>TICKER・速報インシデント・情勢カード3枚・COUNTDOWN・シナリオ確率補足バナー・シナリオ4本・シナリオフッター・全ルート現況サマリー（再確認済）・30秒カラム更新。主要変更：トランプ「合意はほぼ妥結・まもなく発表」（5/23 NPR/CNBC）・イランFM「核問題は交渉対象外」と明言（5/23 CNBC）・イラン「枠組み合意」として30〜60日詳細交渉を主張（5/23 Al Jazeera）・過去24時間で35隻がホルムズ通過（5/23 イラン国家メディア）・WTI $96〜98（月曜市場動向注視中）。出典：NPR・CNBC・Al Jazeera・Bloomberg・Reuters・Trading Economics。</div>
        <div>📅 <strong>2026年5月23日 09:58 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

※ `<!--出典・更新ログ-->` セクションに表示する更新ログが11件を超えた場合は最古の1件を削除してください。

---

## ✅ 出力前セルフチェック

```
[x] S01 ヘッダー ― 2026年5月24日 08:40 JST ✓
[x] S02 TICKER ― トランプ「ほぼ妥結」・イランFM「核問題対象外」・35隻通過・86日目 ✓
[x] S03 速報インシデント ― 5/24 08:40更新・トランプ「ほぼ妥結」速報カードを最先頭に追加 ✓
[x] S04 情勢カード3枚 ― 86日目・WTI $96〜98（月曜注視）・通航95%減 再確認済 ✓
[x] S05 COUNTDOWN ― 封鎖86日目 ✓
[x] S06 シナリオ確率補足バナー ― 5/24日付・根拠文更新（トランプ妥結・イランFM核拒否）✓
[x] S07 シナリオA ― 「ほぼ妥結」も核問題が最大障壁 ✓
[x] S07 シナリオB ― 枠組みから最終合意への移行フェーズ・通航95%減継続 ✓
[x] S07 シナリオC ― 交渉破綻→制度化固定化（B と差別化：交渉フェーズの破綻シナリオ）✓
[x] S07 シナリオD ― 外交破綻→軍事再開（C と差別化：トリガーが破綻の速度・楽観崩壊）✓
[x] S07 シナリオC・D ― WTI価格レンジ差別化済み（C: $108〜122、D: $115〜135）✓
[x] S08 シナリオフッター ― 次の焦点5点を5/24版・枠組み合意詳細交渉中心に更新 ✓
[x] S08.5 全ルート現況サマリー ― 5/24 08:40 JST 再確認済 ✓
[x] S09 30秒カラム ― 3行サマリー「ほぼ妥結」軸・バッジ86日目更新（最後に作成）✓
[x] S10 news_data.json ― latest 2件追加（NPR・CNBC確認済URL）・osint 先頭追加・isLatest更新・updated更新 ✓
[x] S11 更新ログ ― 先頭に5/24 08:40行追記・dateModified 更新 ✓
[x] 全体 ― 日付表記「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一 ✓
[x] 全体 ― URLはweb検索確認済みのみ使用（NPR・CNBC・Al Jazeera URLは検索結果で確認済）✓
[x] 全体 ― 📰関連最新ニュースにAl Jazeera混入なし（latest: NPR・CNBCのみ / osint: Al Jazeera）✓
[x] 全体 ― 人名日本語表記：トランプ・ルビオ・アラグチ・モジュタバ・ハメネイ・ムニル ✓
[x] S10 osint ― Al Jazeera 5/23ライブブログを検索確認済（検索結果 doc64 に出現）✓
[x] S10 osint ― 配列ごと置き換えではなく先頭追加・既存 isLatest:false 変更指示あり ✓
[x] シナリオC・D ― 内容近似なし（C：交渉フェーズ破綻→制度固定化 / D：外交失敗→軍事オプション再浮上）✓
