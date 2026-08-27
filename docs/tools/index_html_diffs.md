# index_html_diffs.md — 2026年8月27日 10:00 JST 更新分
> Claude Code への指示：以下の差分を index.html / news_data.json に適用してください。
> 変更箇所以外は絶対に触らないこと。push は確認後に指示します。

---

## ✅ セルフチェック原文（本文執筆前の先貼り・空欄）

本日のセルフチェック項目数：14件

```
[ ] S01 ヘッダー ― 2026年8月27日 10:00 JST・警戒レベル最高の要約更新
[ ] S02 TICKER ― 本日の主要トピックで刷新（S01と重複しない切り口）
[ ] S03 速報インシデント ― トグル日付・見出し・本文・リスト2件追加
[ ] S04 情勢カード3枚 ― 3枚それぞれ異なる切り口（外交/機雷除去論争・海運市場)
[ ] S05 COUNTDOWN ― Phase28・封鎖181日目・新フェーズラベルに更新
[ ] S06 シナリオ確率補足バナー ― 8/27 10:00 JST日付更新（2箇所）・A↑B→C↓D↓
[ ] S07 シナリオ4本 ― A/B/C/D本文をS06と異なる切り口で更新
[ ] S08 シナリオフッター ― 次の焦点5点をS05のdl-noteと重複しない視点で更新
[ ] S08.5 全ルート現況サマリー ― 8/27 10:00 JST更新・航路別の切り口で記述
[ ] S09 30秒カラム ― 3行サマリー＋バッジ5枚を最後に更新
[ ] S10 news_data.json ― latest 3件追加（旧3件をarchiveへ移動）・osint 1件追加・updated日付
[ ] S11 更新ログ ― 2ブロック構成（常時表示3件固定＋log-collapse先頭挿入）＋総件数超過対応（最古1件削除）
[ ] C01 SHIP_CONFIG dateConfirmed ― 8/27 10:00 JST・変化なし（4クエリ再確認）
[ ] JSON-LD dateModified ― 2026-08-27T10:00:00+09:00
```

（本文執筆後、下記「出力前セルフチェック」で全項目を ✓ で埋めます）

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（ベッセント財務長官は24日、対イラン新制裁「経済的Dデイ」（作戦名"Operation Economic Outcast"）を発表——デジタル資産・先端技術・金・航空・海運の5分野を二次制裁対象に追加し、密輸・サイバー・核関連調達に関与した船舶・企業・個人ほぼ60件を新規制裁指定、対象には中国・UAE・香港・シンガポール・スイス関連の船舶が含まれる／同氏は「中国」を名指しは避けつつ「いかなる者も米制裁の対象外ではない」と述べ対中金融機関への圧力も辞さない姿勢を示唆／イラン通貨リアルは24日、非公式市場で1ドル＝199万2000リアルの過去最安値を記録——トランプ大統領が先週「史上最も壊滅的な経済作戦」を予告して以降4.5%下落、中国向け原油出荷は制裁発表を前に既にほぼ途絶とブルームバーグが報道／中国外務省の林剣副報道局長は24日、対中制裁が発動されれば「正当な権益を守るため必要な措置を講じる」と米側をけん制／イラン最高国家安全保障会議のレザイー事務局長は22日、経済戦争に加担する近隣諸国を「敵」とみなし関連の石油施設等を標的にすると警告／原油はブレントが前日比2.35%安の92.17ドルへ反落——制裁発表も市場の反応は限定的／米メディア（Axios）は、米軍護衛下のタンカーが1日15〜20隻のペースでホルムズ海峡南側航路を通過し、石油輸送量が開戦前の半分・日量約1000万バレルに達したと報道——米軍のレーダー攻撃でイラン側監視能力が低下したことが要因と分析／日本関係船は残り4隻で変化なし／封鎖179日目）</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イランのアラグチー外相とオマーンのアルブサイディ外相は25日、テヘランで会談し、ホルムズ海峡に「共同の暫定航行回廊」を設置し機雷除去を共同実施する枠組みで合意したと発表——恒久的な航路と海峡の将来管理については今後30〜60日間、技術協議を継続するとしている／トランプ大統領は同日、米海軍がホルムズ海峡国際水域の機雷を全て除去・爆破したとSNSに投稿し、新たな敷設船は即時破壊すると警告したが、米政府・軍による裏付け発表はない／イランのガリババディ副外相は26日、暫定合意後も海峡は開放されていないとしてトランプ氏の主張を否定し、南側回廊（オマーン領海経由・国連承認航路）は新枠組みの下で閉鎖される見通しと説明した／トランプ氏は今月17日にも「オマーンが邪魔なら地獄まで爆撃する」と威嚇しており、米国を関与させない二国間合意に米側がどう反応するかは不透明／24日夜にはオマーン東岸沖でタンカー1隻が正体不明の飛翔体を受け機関が損傷、UKMTOが確認（乗員無事）／原油はブレントが一時87ドルを割り込み週間約8%安、WTIも81ドル近辺まで下落／中国外務省は対中制裁計画に「中国・イラン協力は妨害を受けるべきでない」と改めて反発／日本関係船は残り4隻で変化なし／封鎖181日目）</span>
<!-- NEW:END -->
<!-- APPLY:END -->
<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-date">📅2026年8月25日 12:11 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-date">📅2026年8月27日 10:00 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の日付コメント直後の `.ticker-text` 内テキスト全体

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月25日 12:11 JST） -->
      💰【経済Dデイ発動】ベッセント財務長官、対イラン二次制裁「Operation Economic Outcast」を正式発表——デジタル資産・先端技術・金・航空・海運の5分野に対象拡大、船舶・企業等ほぼ60件を新規制裁指定（8/24）｜📉 イランリアルが過去最安値199万2000リアル/ドルに下落——制裁予告後4.5%下落、中国向け原油出荷はほぼ途絶（Bloomberg、8/24）｜🇨🇳 中国外務省・林剣副報道官「対中制裁なら正当な権益守るため必要な措置」と米をけん制（8/24）｜⚔️ イラン安保高官レザイー氏「経済戦争加担国は敵」と改めて警告（8/22）｜🛢️ ブレント原油92.17ドルへ反落（-2.35%）——制裁発表も反応限定的（8/24）｜🚢 米メディア報道：南側航路で護衛下タンカーが1日15〜20隻通過、石油輸送量は開戦前の半分・日量約1000万バレルに到達｜🇯🇵 日本関係船は残り4隻で変化なし｜封鎖179日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月27日 10:00 JST） -->
      🕊️【暫定合意】イラン・オマーン、ホルムズ海峡に「共同暫定航行回廊」設置＋機雷除去で合意——恒久ルートは30〜60日以内に協議へ（テヘラン、8/25）｜💣 トランプ氏「機雷は全て除去・爆破」とSNS投稿、新規敷設船は即時破壊と警告——米政府の公式裏付けなし（8/25）｜🇮🇷 イラン副外相ガリババディ氏「海峡は開放されていない」とトランプ氏主張を否定、南側回廊は新枠組みで閉鎖の見通し（8/26）｜⚓ オマーン東岸沖でタンカー1隻が飛翔体で被弾・機関停止、UKMTO確認（乗員無事・8/24夜）｜🛢️ ブレント原油が一時87ドル割れ・週間下落率約8%——通航協議進展を好感（8/25）｜🇨🇳 中国外務省、対中制裁計画に「中国・イラン協力は妨害されるべきでない」と改めて反発｜🇯🇵 日本関係船は残り4隻で変化なし｜封鎖181日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

**対象：** `<!-- 速報インシデント　トグルボタン -->` 内、および折りたたみ本体の先頭

### トグルボタン（見出し・日付バッジ）

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:1.1rem;">🚨</span>
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">ベッセント財務長官「経済的Dデイ」発動——イランリアル過去最安値・南側航路の実効支配崩壊が同時進行</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/25 12:11 更新</span>
    </span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:1.1rem;">🚨</span>
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">イラン・オマーンがホルムズ海峡暫定回廊で合意——トランプ氏「機雷全除去」主張にイランは海峡開放を否定</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/27 10:00 更新</span>
    </span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の `<strong>` タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/25 12:11 速報】ベッセント財務長官は24日、対イラン新制裁「経済的Dデイ」を発表し、作戦名「Operation Economic Outcast」の下、デジタル資産・先端技術・金・航空・海運の5分野を二次制裁対象に加え、密輸・サイバー・核関連調達に関与した船舶・企業・個人ほぼ60件を新規制裁指定した（Axios/NPR/PBS/Al Jazeera）｜対象国には猶予期間が設けられるが具体的期限は非公表、ベッセント氏は中国を名指しは避けつつ「いかなる者も米制裁の対象外ではない」と述べ、対中金融機関への圧力も辞さない姿勢を示唆した｜イラン通貨リアルは24日、非公式市場で1ドル＝199万2000リアルの過去最安値を記録——トランプ大統領が先週「史上最も壊滅的な経済作戦」を予告して以降4.5%下落、イランの対アジア原油出荷は制裁発表を前に既にほぼ途絶したとブルームバーグが報道｜中国外務省の林剣副報道局長は24日、対中制裁が発動された場合「正当な権益を守るため必要な措置を講じる」と表明——「制裁や圧力は緊張を激化させるだけ」と対話解決を呼びかけ｜イラン最高国家安全保障会議のレザイー事務局長は22日、国営テレビで「近隣諸国が米国の経済戦争に加担すれば敵と見なし標的にする」と警告し、米国が態度を改めない限りホルムズ海峡は開放しないと改めて表明｜一方、米メディア（Axios）は政府関係者の情報として、米軍の保護を受けたタンカーが1日15〜20隻のペースでホルムズ海峡南側航路を通過し、石油輸送量が開戦前の半分・日量約1000万バレルに達していると報道——米軍によるレーダー等への攻撃でイラン側の監視能力が低下したことが要因と分析｜原油はブレントが前日比2.35%安の92.17ドルへ反落——制裁発表も市場の反応は限定的｜日本関係船は残り4隻で変化なし｜封鎖179日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/27 10:00 速報】イランのアラグチー外相とオマーンのアルブサイディ外相は25日、テヘランで会談し、ホルムズ海峡に「共同の暫定航行回廊」を設置し機雷除去の共同事業を実施する枠組みで合意したと共同声明で発表した（Al Jazeera/Reuters、8/25）｜イラン副外相ガリババディ氏は26日、国営テレビに対し、湾内向け航路は全面的にイラン領海を通過し、湾外向け航路はイラン・オマーン両領海を通過する形になると説明——両国は今後30〜60日間、恒久的で持続可能な新ルートについて協議を続けるとした（AP）｜同氏はまた、南側回廊（オマーン領海経由・国連承認TSS）は新枠組みの下で閉鎖される見通しだと述べたが、オマーン側の声明にこの閉鎖への言及はなく、整合性は未確認｜トランプ大統領は25日、SNS投稿で「米海軍からホルムズ海峡国際水域内の機雷を全て除去・爆破したとの報告を受けた」とし、新たに機雷を敷設する船舶・ボートは即時かつ組織的に破壊すると警告——米宇宙軍による監視継続も強調したが、米政府・軍からこれを裏付ける公式発表はない（CNN/BBC、8/25）｜イラン側はこの主張を「虚偽」として全面否定（読売新聞、8/26）｜Al Jazeeraの分析記事は、機雷除去が主要航路で信頼できる可能性はあるとしつつ、監視外の「漂流機雷」が残る可能性やイランが新たに機雷を敷設する能力自体は保持している点を指摘し、機雷除去だけでは商業航行の「安全」を意味しないと論じた（8/26）｜トランプ氏は今月17日にも今回の枠組み交渉を主導するオマーンに対し「邪魔をするなら地獄まで爆撃する」と2度目の軍事威嚇を行っており、米国を関与させない形での二国間合意に米側がどう反応するかが今後の焦点となる｜24日夜（協定世界時）にはオマーン東岸沖でタンカー1隻が正体不明の飛翔体を受け機関が停止、英UKMTOが被害を確認したが乗員は全員無事、犯行声明はない（AP、8/25）｜中国外務省の林剣副報道官は、米財務省が計画する対中制裁拡大について「中国とイランの協力は妨害・干渉を受けるべきではない」と改めて反発（AP、8/25）｜日本関係船は残り4隻で変化なし｜封鎖181日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に2件追加）

**既存リストの先頭（`<ul>` の直後）に以下の2件を追記：**

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇮🇷🇴🇲 8/25〜26 JST</span>
  <span style="color:#e2e8f0;"> イランのアラグチー外相とオマーンのアルブサイディ外相は25日、テヘランで会談し、ホルムズ海峡における「共同の暫定航行回廊」の設置と機雷除去の共同事業実施について合意したと共同声明を発表した。イラン副外相ガリババディ氏は26日、湾内向け航路が全面的にイラン領海を、湾外向け航路がイラン・オマーン両領海を通過する形になると説明し、両国は今後30〜60日間、恒久的な新ルートについて技術協議を継続するとした。同氏は暫定合意後も海峡は開放されていないとし、トランプ大統領の「機雷全除去」発言も事実上否定した（Al Jazeera/AP、8/25〜26）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">💣 8/25 JST</span>
  <span style="color:#e2e8f0;"> トランプ大統領はSNS投稿で、米海軍がホルムズ海峡の国際水域内にある機雷を全て除去または爆破したと発表し、新たに機雷を敷設しようとする船舶・ボートは即座に破壊すると警告した。米政府・軍からはこの主張を裏付ける公式発表はなく、Al Jazeeraは主要航路での機雷除去は信頼できる可能性があるとしつつ、監視外の漂流機雷やイランの再敷設能力が残る限り「商業航行が安全になったとは言えない」と分析した（CNN/BBC/Al Jazeera、8/25〜26）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 最新情勢カード3枚

**対象：** `<!-- SITUATION CARDS -->` 内の3カード

### カード①（外交）

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sit-card danger">
    <div class="s-icon">💰</div>
        <div class="s-title">💰 ベッセント財務長官「経済的Dデイ」発動——5分野に二次制裁拡大、対中名指しは回避</div>
        <div class="s-body">ベッセント財務長官は24日の記者会見で、対イラン新制裁「経済的Dデイ」を正式発表した。作戦名「Operation Economic Outcast」の下、デジタル資産・先端技術・金・航空・海運の5分野を新たに二次制裁の対象領域に加え、密輸・サイバー活動・核ミサイル関連調達等に関与したとする船舶・企業・個人ほぼ60件を新規制裁指定した。対象国には是正の猶予期間が設けられるが具体的な期限は非公表。ベッセント氏は「世界中でこの専制体制を支える経済的な生命線を、テヘランが孤立するまで断ち切る」と述べる一方、記者から中国系銀行が標的になり得るか問われると「いかなる者も米制裁の対象外ではない」と述べるにとどめ、中国の名指しは避けた。米国はイラン原油輸入の9割を占めるとされる中国への対応を軸に、同盟国への協力要請を優先する構えを見せている。</div>
        <div class="s-src">出典: Axios / NPR / PBS / Al Jazeera（8/24 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- カード① 外交・暫定合意 -->
  <div class="sit-card danger">
    <div class="s-icon">🇮🇷🇴🇲</div>
        <div class="s-title">🇮🇷🇴🇲 イラン・オマーン、ホルムズ海峡暫定回廊で合意——恒久ルートは30〜60日以内に協議へ</div>
        <div class="s-body">イランのアラグチー外相とオマーンのアルブサイディ外相は25日、テヘランで会談し、ホルムズ海峡に「共同の暫定航行回廊」を設置し機雷除去を共同で行う枠組みで合意したと共同声明で発表した。イラン副外相ガリババディ氏は国営テレビに対し、湾内向け航路は全面的にイラン領海を、湾外向け航路はイラン・オマーン両領海を通過する構成になると説明し、南側回廊（オマーン領海経由の国連承認TSS）は新枠組みの下で閉鎖される見通しだと述べた。両国は恒久的な新ルートと海峡の将来管理について、今後30〜60日間の技術協議を継続するとしている。米国はこの協議に関与しておらず、トランプ大統領は今月、交渉を仲介するオマーンに「邪魔をするなら爆撃する」と警告しており、米国抜きの二国間合意を米側が受け入れるかは不透明。</div>
        <div class="s-src">出典: Al Jazeera / Reuters / AP（8/25〜26 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード②（機雷除去論争）

<!-- APPLY:START -->
<!-- OLD:START -->
  <!-- カード② イラン反発・通貨市場 -->
  <div class="sit-card warning">
    <div class="s-icon">📉</div>
        <div class="s-title">📉 イランリアル過去最安値——中国は「正当な権益守る」と対抗警告、レザイー氏は近隣諸国を「敵」と威嚇</div>
        <div class="s-body">イラン通貨リアルは24日、非公式市場で1ドル＝199万2000リアルの過去最安値を記録した。トランプ大統領が先週「史上最も壊滅的な経済作戦」の実施を予告して以降、下落率は4.5%に達している。ブルームバーグによれば、イランのアジア向け原油出荷は制裁発表を前に既にほぼ途絶しており、イラン産原油のアジア向け価格は数年ぶりの高水準となっている。中国外務省の林剣副報道局長は24日の記者会見で、対中制裁が発動された場合「正当な権益を守るため必要な措置を講じる」と米側をけん制し、「制裁や圧力は緊張を激化させるだけ」と対話による解決を呼びかけた。イラン最高国家安全保障会議のレザイー事務局長は22日、国営テレビで「近隣諸国が米国の経済戦争に加担すれば敵と見なし標的にする」と警告し、米国が態度を改めない限りホルムズ海峡は開放しないとの立場を改めて示した。</div>
        <div class="s-src">出典: Bloomberg / 共同通信 / AFP（8/22〜24 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <!-- カード② 機雷除去論争 -->
  <div class="sit-card warning">
    <div class="s-icon">💣</div>
        <div class="s-title">💣 トランプ氏「機雷は全て除去」——イランは否定、専門家は「安全な航行の回復とは別問題」</div>
        <div class="s-body">トランプ大統領は25日、米海軍がホルムズ海峡国際水域内の機雷を全て除去・爆破したとSNS投稿し、新たな機雷敷設船は即時破壊すると警告した。米国防当局からこれを裏付ける公式発表はない。イラン副外相ガリババディ氏は26日、イラン・オマーンの暫定合意にもかかわらず海峡は開放されていないとし、トランプ氏の除去主張も事実上否定した。Al Jazeeraの分析記事は、米側の主要航路における機雷除去の評価自体は信頼できる可能性があるとしつつ、監視網の外にある「漂流機雷」が残存する可能性や、イランが新たな機雷を敷設する能力を保持し続けている点を指摘し、機雷除去だけでは商業船舶が戦前水準の航行を安全に再開できることを意味しないと論じた。</div>
        <div class="s-src">出典: CNN / BBC / Al Jazeera（8/25〜26 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③（海上輸送・市場・日本関係船）

<!-- APPLY:START -->
<!-- OLD:START -->
  <!-- カード③ 海上輸送・日本関係船 -->
  <div class="sit-card info">
    <div class="s-icon">🚢</div>
        <div class="s-title">🚢 南側航路の実効通過量が開戦前の半分に到達——米軍護衛下15〜20隻/日、日本関係船は4隻で変化なし</div>
        <div class="s-body">米ニュースサイトAxiosは政府関係者の情報として、米軍の保護を受けたタンカーが1日あたり15〜20隻のペースでホルムズ海峡の南側航路を通過していると報じた。石油の輸送量は戦闘開始前の半分にあたる日量約1000万バレルに達しており、米軍によるレーダー等への攻撃でイラン側の船舶監視能力が低下したことが要因とみられる。トランプ大統領は海峡が「開放されている」と主張する一方、イラン側は「覚書が実行されない限り開放されない」と応酬しており、実務上の通航量と両国の政治的主張の間には依然として乖離がある。原油市場では、ブレントが24日に前日比2.35%安の92.17ドルへ反落し、新制裁発表も市場の反応は限定的だった。日本関係船については外務省・国土交通省への日英4クエリ調査で新規発表がないことを再確認し、残り4隻のまま変化はない。</div>
        <div class="s-src">出典: Axios（KSB瀬戸内海放送 8/22 経由）/ ロイター / 外務省・国土交通省（8/22〜24 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <!-- カード③ 海上輸送・市場・日本関係船 -->
  <div class="sit-card info">
    <div class="s-icon">🚢</div>
        <div class="s-title">🚢 オマーン沖でタンカー被弾・原油急落——南側航路の緊張続く中、日本関係船は4隻で変化なし</div>
        <div class="s-body">英海運当局UKMTOは、24日夜（協定世界時）にオマーン東岸沖でタンカー1隻が正体不明の飛翔体を受け機関が停止したと発表した。乗員は全員無事で環境影響の報告もないが、犯行声明はなく、南側航路を含む海峡周辺の危険性が依然として続いていることを示す事案となった。原油市場では、イラン・オマーンの通航協議進展を好感し、ブレント原油が25日に一時1バレル＝87ドルを割り込み週間で約8%下落、米国産WTIも81ドル近辺まで下げた。日本関係船については、外務省・国土交通省への日英4クエリ調査で新規発表がないことを再確認し、ペルシャ湾内に残る隻数は引き続き4隻のまま変化はない。</div>
        <div class="s-src">出典: UKMTO / Bloomberg / 外務省・国土交通省（8/24〜26 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN フェーズラベル・補足ノート

### フェーズラベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 27「ベッセント財務長官が対イラン『経済的Dデイ』を発動——リアル過去最安値・南側航路の実効支配崩壊が同時進行」——封鎖179日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 28「イラン・オマーンがホルムズ海峡暫定回廊で合意——トランプ氏『機雷全除去』主張にイランは海峡開放を否定」——封鎖181日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### 補足ノート（dl-note）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🌐 <strong>ベッセント財務長官が対イラン制裁を「経済的Dデイ」と位置づけ発動したことで、対立の重心は言説・法的な主権闘争から具体的な経済的締め付けの段階へと移行した——中国の名指しは回避しつつ「いかなる者も対象外ではない」と圧力を残す慎重な手法をとっている／イラン通貨リアルは過去最安値を更新し、経済的な打撃は実体経済の水準にまで及び始めている／その一方で、米軍護衛下のホルムズ海峡南側航路では通航量が実質的に開戦前の半分規模まで回復しており、「制裁による締め付け」と「現場での実効支配の緩み」という相反する動きが同時進行している／日本関係船は残り4隻で変化なし——封鎖179日目</strong>
        <br><span style="color:#fde68a;">⚡ 次の24〜48時間の焦点：①対中制裁の実際の発動有無とタイミング ②イランリアルのさらなる下落と国内経済への波及 ③レザイー事務局長が警告した近隣諸国への「報復」が現実の行動に移るか ④南側航路の通航量増加がイラン側の反応（監視強化・攻撃再開）を招くか ⑤中国以外の主要貿易国（トルコ・インド・UAE）の対応</span>
        <br><span style="color:#fca5a5;">⏳ 制裁と現場の実効支配緩みが同時進行するねじれ構造——経済戦線と海上輸送の実態が乖離したまま推移している</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🌐 <strong>イラン・オマーンの暫定航行回廊合意は、開戦後初めて「海峡管理の具体的な枠組み」が両沿岸国間で言語化された点で外交的な一歩である一方、米国を関与させない二国間の取り決めであるため、トランプ政権がこれを追認するかどうかという新たな不確実性を生んでいる——トランプ氏の「機雷全除去」発言とイランの真っ向からの否定は、同じ事象について当事者間で全く異なる現実認識が併存していることを改めて示した／原油市場は協議進展を好感して下落したが、南側航路でのタンカー被弾は海峡周辺のリスクが消えていないことを裏付けている／日本関係船は残り4隻で変化なし——封鎖181日目</strong>
        <br><span style="color:#fde68a;">⚡ 次の24〜48時間の焦点：①米国がイラン・オマーンの二国間合意をどう評価し対応するか ②南側回廊（国連承認TSS）の閉鎖が実際に実行に移されるか ③機雷除去の実態について第三者（IMO・保険業界等）の独立確認が得られるか ④オマーン沖タンカー被弾の犯行主体特定と再発の有無 ⑤30〜60日間の技術協議の進捗と恒久ルート合意の実現可能性</span>
        <br><span style="color:#fca5a5;">⏳ 外交的前進と現場のリスク残存が併存する局面——「合意はしたが海峡は開いていない」という当事者双方の発言の落差が今後の焦点</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月25日 12:11 JST 更新</span><br>
  📊 <strong>ベッセント財務長官が対イラン制裁を「経済的Dデイ」として発動する一方、ホルムズ海峡南側航路では米軍護衛下の通航量が開戦前の半分規模まで回復——「制裁強化」と「現場の実効支配緩み」が同時進行し、シナリオの重心が経済戦線と海上実務の二正面に分岐しつつある：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — 経済制裁による対立の先鋭化は交渉のテーブル自体を遠ざけており、公式な履行合意への道筋はさらに狭まっている<br>
  🅑 膠着継続 <span style="color:#94a3b8;">→</span> — 外交チャンネルでの具体的な進展は見られないが、南側航路での実務的な通航拡大が「事実上の部分正常化」として並行して進んでいる<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 制裁と通貨危機によりイラン経済への圧力が実体化し、既存枠組みの形骸化がさらに進む可能性が高まっている<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — レザイー氏の近隣諸国への威嚇と、南側航路拡大に対するイラン側の反発次第では、監視・攻撃の再強化という軍事的な巻き戻しリスクも残る<br>
  <strong style="color:#f87171;">経済的圧力の強化と海上での実効支配の緩みという相反する動きが同時に進む中、対中制裁の発動有無とイランの実際の反撃行動が今後のシナリオを左右する分岐点となる（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月25日 12:11 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月27日 10:00 JST 更新</span><br>
  📊 <strong>イラン・オマーンがホルムズ海峡に共同暫定回廊を設置し機雷除去を共同実施する枠組みで合意した一方、トランプ大統領の「機雷全除去」主張をイランが否定し、海峡が実際に開放されたわけではないと強調——外交的な前進と、当事者間の現実認識の乖離が同時に表面化している：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#4ade80;">↑</span> — 米国が関与しない形とはいえ、イラン・オマーン間で初めて具体的な航路管理の枠組みが文書化されたことは、既存のMOU路線とは別に交渉の糸口が生まれたことを意味する<br>
  🅑 膠着継続 <span style="color:#94a3b8;">→</span> — 暫定合意はまだ「海峡開放」を意味せず、南側回廊の閉鎖観測もあり、実際の通航量が大きく変わる保証はない<br>
  🅒 MOU形骸化・機能不全 <span style="color:#4ade80;">↓</span> — イラン・オマーン間の合意進展は、既存の米・イラン枠組みが完全に機能停止する事態をやや遠ざけている<br>
  🅓 全面対決・無期限封鎖 <span style="color:#4ade80;">↓</span> — 機雷除去や技術協議の進展は軍事エスカレーションの当面のリスクを幾分和らげているが、米国排除の合意にトランプ政権がどう反応するかは読み切れない<br>
  <strong style="color:#f87171;">米国を関与させない形での二国間合意という新しい変数が加わったことで、今後はトランプ政権の反応と南側回廊閉鎖の実行有無が最大の分岐点となる（A↑ B→ C↓ D↓）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月27日 10:00 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ本文 A/B/C/D（確率矢印＋本文更新）

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="sc-card sc-best">
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>ベッセント財務長官が対イラン制裁を「経済的Dデイ」と位置づけて発動したことで、米国は交渉より圧力の継続を選んだ姿勢を鮮明にした。イラン通貨の急落という実体経済への打撃が加わったことで、体制側が公式な譲歩に動く可能性はむしろ後退したとみられる。</p>
      </div>
    </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="sc-card sc-best">
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> <span style="color:#4ade80;">↑</span></span>
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>イラン・オマーンが暫定航行回廊と機雷除去の枠組みで合意したことは、既存の米・イラン間MOU路線とは別の経路で「海峡管理の具体化」が進み始めたことを示す。ただし米国が交渉に加わっていない以上、これが正式なMOU履行の再開に直結するかは不透明で、トランプ政権の出方次第で評価は大きく変わりうる。</p>
      </div>
    </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
    <!-- シナリオ B：部分的封鎖継続（膠着） -->
    <div class="sc-card sc-mid">
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>外交チャンネルでの具体的な進展は乏しい一方、米軍護衛下の南側航路では1日15〜20隻・日量約1000万バレルという開戦前の半分規模の通航が実現しつつある。政治的な対立と現場での部分的な正常化が並行するという、これまでにない膠着の形が定着しつつある。</p>
      </div>
    </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <!-- シナリオ B：部分的封鎖継続（膠着） -->
    <div class="sc-card sc-mid">
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>トランプ氏が「機雷全除去」を主張する一方でイランが海峡開放を否定するという、事実認識そのものが対立したまま推移する構図は、これまでの膠着とは異なる新しい形の停滞と言える。実際の通航量に大きな変化がない限り、外交上の言葉の応酬が続く「膠着継続」の枠組みは維持されやすい。</p>
      </div>
    </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
    <!-- シナリオ C：完全封鎖の制度化・経済疲弊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>イランリアルの過去最安値更新と対アジア原油出荷の事実上の停止は、制裁による経済疲弊が加速局面に入ったことを示す。中国が「正当な権益を守る」と対抗姿勢を示す一方で実際の行動には慎重な構えを見せており、制裁の実効性を巡る綱引きが長期化の一因となりうる。</p>
      </div>
    </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <!-- シナリオ C：完全封鎖の制度化・経済疲弊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> <span style="color:#4ade80;">↓</span></span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>南側回廊（国連承認TSS）が新枠組みの下で閉鎖されるとの観測は、イラン・オマーン主導の航路管理が既存の国際的な通航ルールに取って代わる可能性を示唆する。もっとも、この閉鎖はオマーン側の声明では確認されておらず、実際に制度化が進むかは今後の技術協議の帰結次第である。</p>
      </div>
    </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
    <!-- シナリオ D：軍事エスカレーション・停戦崩壊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> <span style="color:#f87171;">↑</span></span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>レザイー事務局長が近隣諸国に対し「経済戦争への加担は敵対行為」と明言し関連石油施設への攻撃を示唆したことは、経済制裁が軍事的対抗措置の引き金になりうることを示している。南側航路での通航拡大にイランが強く反発すれば、監視・攻撃能力の再強化という形でのエスカレーションも排除できない。</p>
      </div>
    </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <!-- シナリオ D：軍事エスカレーション・停戦崩壊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> <span style="color:#4ade80;">↓</span></span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>軍事的な緊張そのものは、機雷除去や技術協議の進展によって当面は和らいでいるように見える。ただしオマーン沖でのタンカー被弾は攻撃リスクが消えていないことを示しており、米国を排除した合意にトランプ政権が反発すれば、状況が再び悪化する可能性は残る。</p>
      </div>
    </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオ フッター（次の焦点5つ）

<!-- APPLY:START -->
<!-- OLD:START -->
  <div style="margin-top:10px;padding:10px 14px;border-radius:8px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);font-size:0.7rem;color:#64748b;display:flex;flex-wrap:wrap;gap:10px;align-items:center;">
    <h3 style="font-size:0.9rem;font-weight:700;color:#94a3b8;margin:0 0 10px;letter-spacing:0.05em;">🔍 次の焦点 5つ</h3>
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">対中制裁が実際に発動されるか——中国が原油輸入を続けた場合の米側の次の一手</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イランリアルの下落が体制の統治能力・国内世論にどこまで波及するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">南側航路の通航拡大にイランがどう反応するか——黙認か、監視・攻撃の再強化か</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">レザイー事務局長が警告した「関連石油施設への攻撃」が現実の行動に移るか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">中国以外の主要貿易国（トルコ・インド・UAE）が米制裁圧力にどう対応するか</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月25日 12:11 JST情勢分析</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div style="margin-top:10px;padding:10px 14px;border-radius:8px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);font-size:0.7rem;color:#64748b;display:flex;flex-wrap:wrap;gap:10px;align-items:center;">
    <h3 style="font-size:0.9rem;font-weight:700;color:#94a3b8;margin:0 0 10px;letter-spacing:0.05em;">🔍 次の焦点 5つ</h3>
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米国がイラン・オマーンの二国間合意にどう対応するか——追認か、対抗措置か</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">南側回廊（国連承認TSS）閉鎖が実際に発効し、通航実務にどう影響するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">機雷除去の第三者検証——IMO・保険業界・船社が独自に安全宣言を出すか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">30〜60日間の技術協議で恒久ルート合意に至るか、それとも再び停滞するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">オマーン沖タンカー被弾の再発防止——UKMTO・JMICの警戒水準に変化はあるか</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月27日 10:00 JST情勢分析</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月25日 12:11 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">米メディア（Axios）報道によれば、南側航路（オマーン沿岸回廊）の実務上の通航規模が拡大し、政治的対立の激化とは裏腹に「事実上の部分正常化」が進んでいる可能性が浮上した。【南ルート（Omani coastal corridor）】米軍護衛下のタンカーが1日15〜20隻のペースで通過し、石油輸送量は開戦前の半分・日量約1000万バレルに到達——米軍のレーダー等への攻撃でイラン側の監視能力が低下したことが要因と分析されている。【北側航路（イラン指定）】通航料徴収の制度化は依然実現しておらず、利用は低調なまま。【市場との連動】ブレント原油は24日に前日比2.35%安の92.17ドルへ反落——南側航路の実質拡大が供給不安の緩和材料として意識された可能性がある。【外交・制裁】ベッセント財務長官が24日、対イラン新制裁「経済的Dデイ」を発動し海運・航空分野も対象に加えたが、現時点で南側航路の通航実績への直接的な影響は確認されていない。【UKMTO 警戒水準】Substantial（継続）。【ダーク・トラフィック】クウェート・サウジ・UAEはVLCCチャーターとシップ・トゥ・シップ移送でトランスポンダーオフの「不可視」輸送を継続。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/25 12:11 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月27日 10:00 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">イラン・オマーンの暫定回廊合意により、今後の航路構成に変化が見込まれる。【新設回廊（イラン・オマーン合意ベース）】湾内向け航路は全面的にイラン領海、湾外向け航路はイラン・オマーン両領海を通過する構成となる見通し（イラン副外相ガリババディ氏、8/26）——ただし発効時期・具体的座標は未公表。【南側回廊（オマーン沿岸・国連承認TSS）】新枠組みの下で閉鎖される可能性がイラン側から示唆されているが、オマーン側の声明には言及がなく整合性は未確認。前週まで米軍護衛下で1日15〜20隻規模の通航が報告されていた主要ルート。【北側航路（イラン指定）】通航料徴収の制度化は依然実現せず、利用は低調。【市場】ブレント原油は25日に一時87ドルを割り込み週間約8%安——通航協議進展を好感。【インシデント】24日夜、オマーン東岸沖でタンカー1隻が飛翔体被弾・機関停止（UKMTO確認・乗員無事）。【UKMTO 警戒水準】Substantial（継続）。【ダーク・トラフィック】クウェート・サウジ・UAEはVLCCチャーターとシップ・トゥ・シップ移送でトランスポンダーオフの「不可視」輸送を継続。🇯🇵 日本関係船舶：残り4隻で変化なし（8/27 10:00 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ5枚）※最後に作成

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 3行サマリー -->
<div style="display:flex;flex-direction:column;gap:6px;margin-bottom:10px;border:1.5px solid rgba(56,189,248,0.3);border-radius:14px;padding:8px 10px;background:rgba(15,23,42,0.6);">
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.4);color:#fca5a5;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">いま何が</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
💰 ベッセント財務長官が対イラン新制裁「経済的Dデイ」を発動——5分野に二次制裁拡大、中国名指しは回避。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📉 イランリアルは過去最安値199万2000リアル/ドルに下落。南側航路は開戦前の半分規模まで通航拡大。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇨🇳 対中制裁の発動有無とイランの反撃行動が焦点——封鎖179日目。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 3行サマリー -->
<div style="display:flex;flex-direction:column;gap:6px;margin-bottom:10px;border:1.5px solid rgba(56,189,248,0.3);border-radius:14px;padding:8px 10px;background:rgba(15,23,42,0.6);">
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.4);color:#fca5a5;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">いま何が</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷🇴🇲 イラン・オマーンがホルムズ海峡の暫定通航回廊で合意——機雷除去も共同実施へ。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
💣 トランプ氏「機雷全除去」を主張するもイランは海峡開放を否定、オマーン沖でタンカー1隻が被弾。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🛢️ 原油は週間8%安に反落——米国が二国間合意にどう対応するかが焦点、封鎖181日目。
</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ5枚

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💰経済的Dデイ発動・60件制裁指定</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📉イランリアル過去最安値</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇨🇳中国「正当な権益守る」と警告</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚢南側航路15〜20隻/日・半分規模回復</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷🇴🇲暫定航行回廊で合意</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💣機雷「全除去」主張にイラン反論</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚓オマーン沖でタンカー被弾</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油週間8%安</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新メモ

**更新方法：** `docs/data/news_data.json` の `latest` 配列の先頭に以下3件を追加し、既存の最古3件（`latest-trump-hormuz-american-territory-0821`／`latest-iran-declaration-of-war-sanctions-0822`／`latest-oman-iran-fm-call-hormuz-0821`）を `archive` 配列の先頭バッチ（`batchLabel: "2026年8月27日"`）へ移動すること。

`isLatest` は新規追加分の最新1件（`latest-iran-oman-temporary-corridor-0825`）のみ `true` とし、他は全て `false` に変更すること。

`updated` フィールドを `"2026年8月27日 10:00 日本時間JST"` に更新すること。

`osint` 配列の先頭に以下1件を追加し、既存の先頭記事（`osint-us-sanctions-ripple-global-markets-0824`）の `isLatest` を `false` に変更すること（配列全体の置き換えは禁止）。

### 追加する `latest` 3件（JSON）

```json
[
  {
    "id": "latest-iran-oman-temporary-corridor-0825",
    "title": "イラン・オマーン、ホルムズ海峡の暫定通航回廊で合意——機雷除去も共同実施へ",
    "body": "イランのアラグチー外相とオマーンのアルブサイディ外相は25日、テヘランで会談し、ホルムズ海峡に「共同の暫定航行回廊」を設置し機雷除去を共同で行う枠組みで合意したと共同声明で発表した。恒久的な航路と海峡の将来管理については今後30〜60日間、技術協議を継続するとしている。",
    "sourceLabel": "Al Jazeera / Reuters",
    "date": "2026年8月25日（現地）/ 2026年8月26日 JST",
    "label": "🇮🇷🇴🇲 外交",
    "url": "https://www.aljazeera.com/news/2026/8/26/iran-oman-agree-on-temporary-hormuz-route-what-we-know",
    "isLatest": true
  },
  {
    "id": "latest-trump-mines-cleared-iran-denies-0826",
    "title": "トランプ氏「ホルムズ海峡の機雷は全て除去」と主張——イラン副外相は海峡開放を否定",
    "body": "トランプ米大統領は25日、米海軍がホルムズ海峡国際水域の機雷を全て除去・爆破したとSNSに投稿し、新たな敷設船は即時破壊すると警告した。米政府・軍から裏付ける公式発表はない。イランのガリババディ副外相は26日、オマーンとの暫定合意後も海峡は開放されていないとして、トランプ氏の主張を否定した。",
    "sourceLabel": "CNN / BBC",
    "date": "2026年8月25日（現地）/ 2026年8月26日 JST",
    "label": "💣 軍事",
    "url": "https://news.yahoo.co.jp/articles/7fc5c824919766b70ad5829b2e3b00e35a795e2c",
    "isLatest": false
  },
  {
    "id": "latest-brent-crude-drop-hormuz-talks-0826",
    "title": "ブレント原油、一時87ドル割れ——イラン・オマーンの通航協議進展を好感し週間8%安",
    "body": "イランとオマーンがホルムズ海峡の暫定通航回廊で協議を進めたことを受け、原油価格は3営業日続落した。北海ブレントは25日に一時1バレル＝87ドルを割り込み、週間の下落率は約8%に達した。米国産WTIも81ドル近辺まで下げた。",
    "sourceLabel": "Bloomberg",
    "date": "2026年8月25日（現地）/ 2026年8月26日 JST",
    "label": "🛢️ 市場",
    "url": "https://news.yahoo.co.jp/articles/da55639f462a19c3d962294f0a1c65e3ecefd8a4",
    "isLatest": false
  }
]
```

### 追加する `osint` 1件（JSON）

```json
{
  "id": "osint-hormuz-high-risk-despite-mine-clearing-0826",
  "titleJa": "【Al Jazeera】機雷除去主張でも海峡は依然高リスク——専門家「安全な通航の回復とは別問題」",
  "titleEn": "Why Hormuz remains high risk for ships despite US claims of mine-clearing",
  "title": "【Al Jazeera】機雷除去主張でも海峡は依然高リスク——専門家「安全な通航の回復とは別問題」",
  "summary": "Al Jazeeraは、トランプ大統領が主張する機雷の全除去について、主要航路での評価自体は信頼できる可能性があるとしつつ、監視網の外にある「漂流機雷」の残存やイランが新たな機雷を敷設する能力を保持し続けている点を専門家が指摘していると報道。機雷除去だけでは商業船舶が戦前水準の航行を安全に再開できることを意味しないと論じている。",
  "source": "Al Jazeera",
  "country": "カタール",
  "media": "Al Jazeera",
  "cardBg": "rgba(56,189,248,0.05)",
  "cardBorder": "rgba(56,189,248,0.25)",
  "badgeColor": "#38bdf8",
  "borderColor": "rgba(56,189,248,0.4)",
  "textColor": "#7dd3fc",
  "date": "2026年8月26日（現地）/ 2026年8月26日 JST",
  "url": "https://www.aljazeera.com/news/2026/8/26/why-hormuz-remains-high-risk-for-ships-despite-us-claims-of-mine-clearing",
  "isLatest": true
}
```

`staleNotice` は新情報があるため `""`（空文字）のまま維持すること。


---

## [S11] 更新ログ — 2ブロック構成（常時表示3件固定＋log-collapse先頭挿入）＋総件数超過対応

### ブロック1：常時表示3件の更新（本日分を先頭に追加、旧3件目は落とす）

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 常時表示: 最新3件 -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月25日 12:11 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/25 12:11</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官が対イラン新制裁「経済的Dデイ」（Operation Economic Outcast）を発表——デジタル資産・先端技術・金・航空・海運の5分野に対象拡大、船舶・企業等ほぼ60件を新規制裁指定・中国の名指しは避けつつ「対象外はない」と圧力（8/24）・イラン通貨リアルは非公式市場で過去最安値199万2000リアル/ドルを記録、対アジア原油出荷はほぼ途絶（8/24）・中国外務省「正当な権益を守る」と対抗警告（8/24）・イラン安保高官レザイー氏「経済戦争加担国は敵」と再警告（8/22）・原油はブレント92.17ドルへ反落（-2.35%、8/24）・米メディア報道：南側航路で護衛下タンカーが1日15〜20隻通過、石油輸送量は開戦前の半分・日量約1000万バレルに到達（8/22）・日本関係船は残り4隻で変化なし・封鎖179日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月23日 09:03 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/23 09:03</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領がサウスカロライナ州の集会で「今はホルムズ海峡を米国領土だと考えている」と初めて現在形で領有を主張——「イランをもう少し爆撃しないといけないのか」とも言及（8/21）・イラン外務省バガイ報道官は月曜(24日)発表予定の新制裁を「単一国への経済戦争にとどまらない、国連加盟国全体への治外法権的主権の主張」であり「全ての国家への宣戦布告」と猛反発、二次制裁は国際法上根拠がないと主張（8/22）・アラグチー外相も新制裁は「失敗する運命」とXで皮肉・ガリバフ国会議長「独立した自国発の秩序のみが真の平和をもたらす」とX投稿・ベッセント財務長官は24日会見で「史上最も強力な制裁」詳細を発表へ、中国に協力要請・21日、オマーン・イラン両外相が電話会談し海峡開放へ向けた調整を協議も打開は不透明・ペゼシュキアン大統領「今日こそ戦争を終わらせるべき時」と表明・18日被弾船舶の乗組員1名は死亡確認（当初は負傷と発表）・ブレント原油は94ドル前後で約1か月ぶり高値圏・日本関係船は残り4隻で変化なし・封鎖177日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月21日 09:09 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/21 09:09</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE国防省が18日探知した弾道ミサイル2発を受け、UAE外務省は19日、イランとの全ての貿易・商業交流・金融取引を追って通知があるまで停止すると発表——イラン外務省は「根拠がない」「偽旗作戦」の可能性と全面否定（Bloomberg/Reuters）・同日トランプ大統領はSNSで「史上最も壊滅的な経済作戦」の実施を予告——石油密輸・スワップライン・ダミー企業等を通じたイラン支援国への経済的報いを警告（詳細非公表）・トランプ氏「現時点では状況は非常に良好」とホルムズ海峡の「完全支配」を改めて主張（CNN）・20日、バンス副大統領は経済圧力を「最も効果的な手段」としつつ「慎重な舵取りが必要」と発言・同日、イラン軍参謀総長アブドラヒ氏は湾岸諸国に「米軍支援は軍事作戦への加担とみなす」と警告——空母ジョージ・ワシントン中東再配備の中での発言（メヘル通信）・米国防総省データでは開戦以来の米兵死者18人・負傷757人に増加（8/19更新）・トランプ政権はヒズボラをイラン代理勢力として再指定し追加制裁（20日）・CNN/ケプラー分析によれば直近2週間の通航船の8割超がオマーン側ルートを採用——イランは実効支配の大部分喪失との見方・ブレント原油は91ドル台後半へ上昇し約1か月ぶり高値圏（8/20時点91.6〜92.2ドル）・日本関係船は残り4隻で変化なし・封鎖175日目・ニュース3件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 常時表示: 最新3件 -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月27日 10:00 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/27 10:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランのアラグチー外相とオマーンのアルブサイディ外相がテヘランで会談し、ホルムズ海峡に共同暫定航行回廊を設置・機雷除去を共同実施する枠組みで合意（8/25）・イラン副外相ガリババディ氏は恒久ルートを30〜60日以内に協議するとしつつ暫定合意後も海峡は開放されていないと表明、南側回廊（国連承認TSS）は閉鎖の見通しと説明（8/26）・トランプ大統領は米海軍がホルムズ海峡国際水域の機雷を全て除去・爆破したとSNS投稿し新規敷設船は即時破壊と警告するも米政府の公式裏付けなし、イラン側は「虚偽」と全面否定（8/25〜26）・24日夜オマーン東岸沖でタンカー1隻が正体不明の飛翔体で被弾・機関停止、UKMTO確認（乗員無事・犯行声明なし）・原油はブレントが一時87ドル割れ・週間約8%安（8/25）・中国外務省は対中制裁計画に「中国・イラン協力は妨害されるべきでない」と改めて反発・日本関係船は残り4隻で変化なし・封鎖181日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月25日 12:11 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/25 12:11</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官が対イラン新制裁「経済的Dデイ」（Operation Economic Outcast）を発表——デジタル資産・先端技術・金・航空・海運の5分野に対象拡大、船舶・企業等ほぼ60件を新規制裁指定・中国の名指しは避けつつ「対象外はない」と圧力（8/24）・イラン通貨リアルは非公式市場で過去最安値199万2000リアル/ドルを記録、対アジア原油出荷はほぼ途絶（8/24）・中国外務省「正当な権益を守る」と対抗警告（8/24）・イラン安保高官レザイー氏「経済戦争加担国は敵」と再警告（8/22）・原油はブレント92.17ドルへ反落（-2.35%、8/24）・米メディア報道：南側航路で護衛下タンカーが1日15〜20隻通過、石油輸送量は開戦前の半分・日量約1000万バレルに到達（8/22）・日本関係船は残り4隻で変化なし・封鎖179日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月23日 09:03 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/23 09:03</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領がサウスカロライナ州の集会で「今はホルムズ海峡を米国領土だと考えている」と初めて現在形で領有を主張——「イランをもう少し爆撃しないといけないのか」とも言及（8/21）・イラン外務省バガイ報道官は月曜(24日)発表予定の新制裁を「単一国への経済戦争にとどまらない、国連加盟国全体への治外法権的主権の主張」であり「全ての国家への宣戦布告」と猛反発、二次制裁は国際法上根拠がないと主張（8/22）・アラグチー外相も新制裁は「失敗する運命」とXで皮肉・ガリバフ国会議長「独立した自国発の秩序のみが真の平和をもたらす」とX投稿・ベッセント財務長官は24日会見で「史上最も強力な制裁」詳細を発表へ、中国に協力要請・21日、オマーン・イラン両外相が電話会談し海峡開放へ向けた調整を協議も打開は不透明・ペゼシュキアン大統領「今日こそ戦争を終わらせるべき時」と表明・18日被弾船舶の乗組員1名は死亡確認（当初は負傷と発表）・ブレント原油は94ドル前後で約1か月ぶり高値圏・日本関係船は残り4隻で変化なし・封鎖177日目・ニュース3件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ 旧エントリー「2026年8月21日 09:09 JST」は new_str に含めない（ブロック1では常時表示3件を厳守）。ブロック2で log-collapse 先頭に挿入する。

### ブロック2：旧3件目（8/21）を log-collapse 先頭に挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月19日 08:51 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/19 08:51</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領がイラン・オマーンのホルムズ航路協議を巡り「オマーンが邪魔なら地獄まで爆撃する」と2度目の軍事威嚇（8/17）・米上院ケイン議員は対オマーン武力行使禁止決議案の提出を表明・トランプ氏はクルディスタン地域政府バルザニ議長経由のIRGC直接裏チャンネルの存在を認めるも、IRGC報道官は「完全な虚偽」と全面否定（8/17）・18日未明、オマーン方面へ出航中の船舶が未確認飛翔体で被弾し乗組員1名負傷、UKMTOが調査中・イラン国会議長ガリバフ氏「米国が資産凍結解除・制裁解除・海上封鎖解除を履行するまで封鎖継続」（8/18）・イラン・オマーンは新航路地図に「了解」も包括合意・共同声明は調整中（イラン外務省バガイ報道官、8/18）・フーシ派はサウジ・アラムコのジザン製油所をドローン攻撃（8/18）・ブレント原油90ドル台後半へ上昇（8/18時点90.97ドル）・サウジアラムコはフジャイラ沖STS移送で出荷再開・日本関係船は残り4隻で変化なし・封鎖173日目・ニュース3件更新・osint更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月21日 09:09 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/21 09:09</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE国防省が18日探知した弾道ミサイル2発を受け、UAE外務省は19日、イランとの全ての貿易・商業交流・金融取引を追って通知があるまで停止すると発表——イラン外務省は「根拠がない」「偽旗作戦」の可能性と全面否定（Bloomberg/Reuters）・同日トランプ大統領はSNSで「史上最も壊滅的な経済作戦」の実施を予告——石油密輸・スワップライン・ダミー企業等を通じたイラン支援国への経済的報いを警告（詳細非公表）・トランプ氏「現時点では状況は非常に良好」とホルムズ海峡の「完全支配」を改めて主張（CNN）・20日、バンス副大統領は経済圧力を「最も効果的な手段」としつつ「慎重な舵取りが必要」と発言・同日、イラン軍参謀総長アブドラヒ氏は湾岸諸国に「米軍支援は軍事作戦への加担とみなす」と警告——空母ジョージ・ワシントン中東再配備の中での発言（メヘル通信）・米国防総省データでは開戦以来の米兵死者18人・負傷757人に増加（8/19更新）・トランプ政権はヒズボラをイラン代理勢力として再指定し追加制裁（20日）・CNN/ケプラー分析によれば直近2週間の通航船の8割超がオマーン側ルートを採用——イランは実効支配の大部分喪失との見方・ブレント原油は91ドル台後半へ上昇し約1か月ぶり高値圏（8/20時点91.6〜92.2ドル）・日本関係船は残り4隻で変化なし・封鎖175日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年8月19日 08:51 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/19 08:51</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領がイラン・オマーンのホルムズ航路協議を巡り「オマーンが邪魔なら地獄まで爆撃する」と2度目の軍事威嚇（8/17）・米上院ケイン議員は対オマーン武力行使禁止決議案の提出を表明・トランプ氏はクルディスタン地域政府バルザニ議長経由のIRGC直接裏チャンネルの存在を認めるも、IRGC報道官は「完全な虚偽」と全面否定（8/17）・18日未明、オマーン方面へ出航中の船舶が未確認飛翔体で被弾し乗組員1名負傷、UKMTOが調査中・イラン国会議長ガリバフ氏「米国が資産凍結解除・制裁解除・海上封鎖解除を履行するまで封鎖継続」（8/18）・イラン・オマーンは新航路地図に「了解」も包括合意・共同声明は調整中（イラン外務省バガイ報道官、8/18）・フーシ派はサウジ・アラムコのジザン製油所をドローン攻撃（8/18）・ブレント原油90ドル台後半へ上昇（8/18時点90.97ドル）・サウジアラムコはフジャイラ沖STS移送で出荷再開・日本関係船は残り4隻で変化なし・封鎖173日目・ニュース3件更新・osint更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：総件数超過対応（常時表示3＋collapse内エントリー数の合計が10を超えるため、collapse最古の「8/7」エントリーを削除）

> 上記ブロック1・2の適用後、常時表示3件＋log-collapse内エントリー（8/21,8/19,8/17,8/15,8/13,8/11,8/09,8/07の8件）で合計11件となり上限10件を超過するため、collapse内最古の「2026年8月7日」エントリーを削除する。

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年8月7日 09:45 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/07 09:45</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省、ホルムズ海峡の安全航路座標についてオマーンと合意したと発表——共同声明は最終調整段階（IRNA、8/5）・米メディアはオマーンが入域イラン管理・出域オマーン管理の暫定枠組みに合意と報道（MS NOW、8/6）・一方イラン議会委員会は米・イスラエル船の恒久排除と他国船への最大7%通行料・違反時20%罰金の法案を審議（Fars通信）・米政府はこの案を即座に拒否し無条件の自由航行を要求（CNBC）・フーシ派はサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目、29隻が引き返し（Reuters）・NYダウは263ドル高の54,349.12ドルで3日連続最高値も6日は反落・原油は乱高下しブレントが一時81ドル台へ反発・日本関係船は残り4隻で変化なし・封鎖161日目・ニュース4件更新・osint更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [C01] SHIP_CONFIG dateConfirmed（4クエリ再確認・変化なし）

**4クエリ実施結果：**
1. 「日本関係船舶 ホルムズ海峡 通過 足止め」→ 直近の隻数変化に関する新規発表なし（外務省サイトの最新プレスは5月時点のものが最上位、8月の新規発表は確認できず）
2. 「外務省 ホルムズ海峡 日本関係船舶」→ 直近の新規プレスリリースなし
3. 「金子国土交通大臣 会見 ホルムズ海峡」→ 直近の会見要旨に新規言及なし（直近の確定発言は7/10会見の「残り4隻」）
4. 英語："Japanese ships Strait of Hormuz stranded detained August 2026" → 新規報道なし

→ 結論：4クエリいずれも新規発表なし、**残り4隻のまま変化なし**と再確認。

<!-- APPLY:START -->
<!-- OLD:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年8月25日 12:11 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近確定発言は7/10会見の「残り4隻」）'
};
<!-- OLD:END -->
<!-- NEW:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年8月27日 10:00 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近確定発言は7/10会見の「残り4隻」）'
};
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-08-25T12:11:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-27T10:00:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
[✓] S01 ヘッダー ― 2026年8月27日 10:00 JST・警戒レベル最高の要約更新
[✓] S02 TICKER ― 本日の主要トピックで刷新（S01と重複しない切り口）
[✓] S03 速報インシデント ― トグル日付・見出し・本文・リスト2件追加
[✓] S04 情勢カード3枚 ― 3枚それぞれ異なる切り口（外交/機雷除去論争・海運市場）
[✓] S05 COUNTDOWN ― Phase28・封鎖181日目・新フェーズラベルに更新
[✓] S06 シナリオ確率補足バナー ― 8/27 10:00 JST日付更新（2箇所）・A↑B→C↓D↓
[✓] S07 シナリオ4本 ― A/B/C/D本文をS06と異なる切り口で更新
[✓] S08 シナリオフッター ― 次の焦点5点をS05のdl-noteと重複しない視点で更新
[✓] S08.5 全ルート現況サマリー ― 8/27 10:00 JST更新・航路別の切り口で記述
[✓] S09 30秒カラム ― 3行サマリー＋バッジ5枚を最後に更新
[✓] S10 news_data.json ― latest 3件追加（旧3件をarchiveへ移動）・osint 1件追加・updated日付
[✓] S11 更新ログ ― 3ブロック構成（常時表示3件固定＋log-collapse先頭挿入＋総件数超過対応で最古1件削除）
[✓] C01 SHIP_CONFIG dateConfirmed ― 8/27 10:00 JST・変化なし（4クエリ再確認）
[✓] JSON-LD dateModified ― 2026-08-27T10:00:00+09:00

全体チェック：
[✓] 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[✓] ニュースURLにAI捏造・推測URLが混入していないか（全てweb検索で実在確認済み：Al Jazeera / Reuters / AP / CNN / BBC / Bloomberg / Yahoo経由記事）
[✓] 📰関連最新ニュースにAl Jazeeraが混入していないか（Al Jazeeraはosintのみに配置）
[✓] 人名が日本語表記になっているか（該当する主要人物名はアラグチー・アルブサイディ・ガリババディ・トランプ・林剣で全て日本語表記、"Xi"表記なし）
[✓] 禁止媒体（毎日新聞・Wikipedia・TBS・朝日新聞・NHK・東京新聞・テレビ朝日）が出典・URLに含まれていないか（該当なし。テレビ朝日系ANN記事は意図的に不使用）
[✓] 各カラム・項目間で同一事実の重複記述を避け、性格に応じた切り口の違いを持たせたか
      （S01=全体見出し／S02=圧縮ティッカー／S03=時系列詳細+引用／S04①=外交詳細②=機雷除去論争③=海運市場／
       S05=24-48h焦点／S06=シナリオ確率変化の理由／S07=シナリオ別個別分析／S08=中期5焦点／
       S08.5=航路別現況／S09=最大圧縮3行／S11=アーカイブ用ダイジェスト）
```

---

## 📌 補足：本日のポイント整理（Claude Code 適用時の参考）

- **最重要ニュース**：イラン・オマーンがホルムズ海峡に「共同暫定航行回廊」設置＋機雷除去の共同実施で合意（8/25、テヘラン）。恒久ルートは今後30〜60日間協議。
- **対立する主張**：トランプ大統領は「機雷は全て除去・爆破」と主張（米政府の公式裏付けなし）。イラン副外相ガリババディ氏はこれを否定し「海峡は開放されていない」と明言（8/26）。
- **インシデント**：24日夜、オマーン東岸沖でタンカー1隻が正体不明の飛翔体で被弾・機関停止（UKMTO確認、乗員無事）。
- **市場**：ブレント原油が一時87ドル割れ・週間約8%安。
- **日本関係船**：4隻で変化なし（4クエリ確認済み）。
- **封鎖日数**：181日目（Day1=2026年2月28日起算）。
- **フェーズ更新**：Phase 27 → Phase 28。

---

## [ARCHIVE] docs/data/archive_timeline.json 追記（8/25・8/27の2日分、速報日のため追記）

**注記：** 前回セッション終了時点で `archive_timeline.json` への8/25分の追記が漏れていたことが判明したため、8/25・8/27の2エントリーをまとめて追記します。本ファイルは `apply_diffs.py` の対象外のため、Claude Codeによる手動 `str_replace` 適用が必要です。

### エントリー追加（entries配列の末尾に2件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
        {
          "title": "オマーン・イラン両外相が電話会談——海峡開放へ調整継続も打開は不透明",
          "url": "https://www.hokkaido-np.co.jp/article/1356995/",
          "sourceLabel": "共同通信"
        }
      ]
    }
  ]
}
<!-- OLD:END -->
<!-- NEW:START -->
        {
          "title": "オマーン・イラン両外相が電話会談——海峡開放へ調整継続も打開は不透明",
          "url": "https://www.hokkaido-np.co.jp/article/1356995/",
          "sourceLabel": "共同通信"
        }
      ]
    },
    {
      "date": "2026-08-25",
      "dateLabel": "2026/08/25 12:11",
      "blockadeDay": 179,
      "sourceType": "realtime",
      "summary": "ベッセント財務長官が対イラン新制裁「経済的Dデイ」（Operation Economic Outcast）を発表——デジタル資産・先端技術・金・航空・海運の5分野に対象拡大、船舶・企業等ほぼ60件を新規制裁指定・中国の名指しは避けつつ「対象外はない」と圧力（8/24）・イラン通貨リアルは非公式市場で過去最安値199万2000リアル/ドルを記録、対アジア原油出荷はほぼ途絶（8/24）・中国外務省「正当な権益を守る」と対抗警告（8/24）・イラン安保高官レザイー氏「経済戦争加担国は敵」と再警告（8/22）・原油はブレント92.17ドルへ反落（-2.35%、8/24）・米メディア報道：南側航路で護衛下タンカーが1日15〜20隻通過、石油輸送量は開戦前の半分・日量約1000万バレルに到達（8/22）・日本関係船は残り4隻で変化なし",
      "relatedNews": [
        {
          "title": "米国が対イランで二次制裁拡大、デジタル資産など5分野「例外ない」",
          "url": "https://www.nikkei.com/article/DGXZQOGN24AA70U6A820C2000000/",
          "sourceLabel": "日本経済新聞"
        },
        {
          "title": "イランリアル過去最安値199万2000リアル/ドルに——中国は対中制裁なら「正当な権益守る」と警告",
          "url": "https://news.yahoo.co.jp/articles/88caa19f3a4d8e99d250195aca51f4ba00b3a2f4",
          "sourceLabel": "Yahoo!ニュース"
        },
        {
          "title": "中国、対イラン米制裁をけん制——違法な一方的制裁と反発",
          "url": "https://news.yahoo.co.jp/articles/d46f27a4fd3a264cd6a0e84dfde316d639b1459b",
          "sourceLabel": "FNNプライムオンライン"
        }
      ]
    },
    {
      "date": "2026-08-27",
      "dateLabel": "2026/08/27 10:00",
      "blockadeDay": 181,
      "sourceType": "realtime",
      "summary": "イランのアラグチー外相とオマーンのアルブサイディ外相がテヘランで会談し、ホルムズ海峡に共同暫定航行回廊を設置・機雷除去を共同実施する枠組みで合意（8/25）・イラン副外相ガリババディ氏は恒久ルートを30〜60日以内に協議するとしつつ暫定合意後も海峡は開放されていないと表明、南側回廊（国連承認TSS）は閉鎖の見通しと説明（8/26）・トランプ大統領は米海軍がホルムズ海峡国際水域の機雷を全て除去・爆破したとSNS投稿し新規敷設船は即時破壊と警告するも米政府の公式裏付けなし、イラン側は「虚偽」と全面否定（8/25〜26）・24日夜オマーン東岸沖でタンカー1隻が正体不明の飛翔体で被弾・機関停止、UKMTO確認（乗員無事・犯行声明なし）・原油はブレントが一時87ドル割れ・週間約8%安（8/25）・中国外務省は対中制裁計画に「中国・イラン協力は妨害されるべきでない」と改めて反発・日本関係船は残り4隻で変化なし",
      "relatedNews": [
        {
          "title": "イラン・オマーン、ホルムズ海峡の暫定通航回廊で合意——恒久ルートは30〜60日以内に協議へ",
          "url": "https://www.aljazeera.com/news/2026/8/26/iran-oman-agree-on-temporary-hormuz-route-what-we-know",
          "sourceLabel": "Al Jazeera"
        },
        {
          "title": "トランプ氏、ホルムズ海峡で機雷を全て除去と投稿",
          "url": "https://news.yahoo.co.jp/articles/7fc5c824919766b70ad5829b2e3b00e35a795e2c",
          "sourceLabel": "BBC News（Yahoo!ニュース）"
        },
        {
          "title": "ブレント原油87ドル割れ、イランとオマーンがホルムズ通航再開へ協議",
          "url": "https://news.yahoo.co.jp/articles/da55639f462a19c3d962294f0a1c65e3ecefd8a4",
          "sourceLabel": "Bloomberg（Yahoo!ニュース）"
        }
      ]
    }
  ]
}
<!-- NEW:END -->
<!-- APPLY:END -->

### meta.rangeEnd の更新（本日日付に合わせて更新）

<!-- APPLY:START -->
<!-- OLD:START -->
"rangeEnd": "2026-07-19"
<!-- OLD:END -->
<!-- NEW:START -->
"rangeEnd": "2026-08-27"
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ Claude Codeでの適用手順：
> 1. `docs/data/archive_timeline.json` を `view` で開く
> 2. 上記の str_replace を entries配列末尾／meta.rangeEnd の2箇所に適用
> 3. `python3 -c "import json; json.load(open('docs/data/archive_timeline.json'))"` でJSON構文を検証
> 4. commit（push は確認後に指示）
