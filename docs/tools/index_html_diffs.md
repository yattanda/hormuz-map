# index_html_diffs.md — 2026年8月15日 06:37 JST 更新分

> Claude Code への指示：以下の差分を docs/index.html および docs/data/news_data.json に適用してください。
> 変更箇所以外は絶対に触らないこと。
> docs/data/archive_timeline.json への追記は [ARCHIVE] セクションに個別記載（apply_diffs.pyの対象外のため、str_replaceで手動適用してください）。

---

## Step 0 セルフチェック（本文執筆前の事前確認）

project_knowledge_search にて「index_html_diffs.md 最新 更新 JST」「更新ログ 出典 JST 更新」を実行し、直近の確定更新が2026年8月13日 10:37 JST（封鎖167日目）であることを確認。raw.githubusercontent.com から docs/index.html・docs/data/news_data.json・docs/data/archive_timeline.json を直接取得し、8/13 10:37 JST時点の内容と完全一致することを確認した（IRGC上級顧問ナグディ氏の長期化発言・フーシ派モカ/ティハマ死者・米軍ヘリ発砲・封鎖167日目）。

C01タンカー確認：日本語3クエリ（「日本関係船舶 ホルムズ海峡 通過 足止め」「外務省 ホルムズ海峡 日本関係船舶 8月」「金子国土交通大臣 会見 ホルムズ海峡 8月」）＋英語1クエリ（「Japanese ships Strait of Hormuz stranded detained August 2026」）全て実施。外務省・国交省ともに8/4会見（熊本地震対応が主題でホルムズ言及なし）以降の新規発表なしを確認。変化なし・残り4隻のまま。

封鎖日数：Day1=2026年2月28日起算で2026年8月15日はDay169（8/13のDay167から+2）。

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イランIRGC上級顧問ナグディ氏がPBSに対し「トランプ政権終了（2029年）まで戦争を長期化させ消耗戦で対米抑止力を確立する選択肢がある」と発言／トランプ大統領は「米国はホルムズ海峡を完全支配している」とTruth Social投稿も、通航量は8/11に週間最低の8隻へ低下／フーシ派が紅海バブエルマンデブ海峡でエジプト所有貨物船「ティハマ」を二重攻撃、乗組員4名・救助隊員2名の計6名死亡10名負傷——今次紛争で初のフーシ派関連死者／米軍ヘリがパナマ籍貨物船「ヴェラ・ノヴァ」に対イラン港湾封鎖破り阻止でヘルファイア2発発射（3週間で3件目の摘発）／ブレント原油は87.92ドルへ反落（6営業日続伸後）、EIA原油在庫は2023年来最大の増加／日本関係船は残り4隻で変化なし／封鎖167日目）</span>
    <span class="badge-item badge-date">📅2026年8月13日 10:37 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表——紛争開始来15隻目の被弾・負傷者なし／トランプ大統領はロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と表明／イラン副外相ガリババディ氏は「米が『戦略的敗北』を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開を「未決定」としイスラマバード覚書は「戦争終結」を意味し60日休戦の延長は不要と主張／米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を拡大、カナダは対イラン制裁5名を追加／ブレント原油は87ドル台で下げ止まり、IEAは石油備蓄急減に警鐘／日本関係船は残り4隻で変化なし／MOU機雷除去期限（7/17）を徒過・最終期限まで残1日（8/16）／封鎖169日目）</span>
    <span class="badge-item badge-date">📅2026年8月15日 06:37 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年8月13日 10:37 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月13日 10:37 JST） -->
      🇮🇷【長期化発言】IRGC上級顧問ナグディ氏がPBSに「トランプ政権終了まで戦争を長期化させ消耗戦に持ち込む選択肢がある」と表明——テヘランの戦略計算を異例に開示（12日）｜🇵🇰 パキスタン外務省報道官アンドラビ氏「両者を交渉の席に戻す努力を継続」——副首相・副外相が10日にイラン・サウジ・クウェートと協議、内相もテヘラン訪問中｜🛰️ Windward衛星監視：8/11のホルムズ通航は正規5隻＋不明船2隻のみ、Larak/East両錨地に係留船51隻——8/4被弾のバルカー船は9日経過後も推進喪失状態が継続｜⚓ 米軍ヘリがオマーン湾でパナマ籍「ヴェラ・ノヴァ」にヘルファイア2発発射・出火（7/15 BELMA、7/24 M/T LAVINEに続く3週間で3件目の摘発）｜🛢️ ブレント87.92ドルへ反落（前日比-1.19%、6営業日続伸後）・EIA原油在庫は2023年来最大の週間増加(+1740万バレル)｜📉 NYダウ53,770ドル（-21.58、3日続落）・CME日経平均先物は+850円高｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英4クエリで再確認・金子国交相8/4会見はホルムズ言及なし）｜封鎖167日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月15日 06:37 JST） -->
      🇦🇪【ADNOCタンカー再被弾】UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にドローン攻撃受けたと発表——負傷者なし・紛争開始来15隻目の被弾、UKMTOも軽微損傷を確認（14日）｜🇺🇸 トランプ大統領「イラン敗北後、ホルムズ海峡を米国領に宣言する」——ロングアイランドの集会で表明、法的根拠には言及せず（14日）｜🇮🇷 イラン副外相ガリババディ氏「米が『戦略的敗北』を認めるまで封鎖継続」——アラグチー外相は対話再開「未決定」、イスラマバード覚書は「戦争終結」であり60日休戦の延長は不要と主張（14日）｜🌍 米、仲介国を拡大——ルビオ国務長官がオーストリア外相と会談・ギリシャ外相と電話協議、カナダは対イラン制裁5名追加（11〜14日）｜🛢️ ブレント原油は87ドル台で下げ止まり（週央89.53ドルから反落）・IEAは石油備蓄急減に警鐘｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英4クエリで再確認・金子国交相8/4会見はホルムズ言及なし）｜⏳ MOU機雷除去期限（7/17）徒過・最終期限まで残1日（8/16）｜封鎖169日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

### 3-1. トグルボタン内の見出し・日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <span style="font-size:1.1rem;">🚨</span>
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">フーシ派が紅海で今次紛争初の死者を出す攻撃、IRGC顧問は「トランプ政権終了まで長期化」発言——米軍はパナマ籍船に発砲</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/13 10:37 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span style="font-size:1.1rem;">🚨</span>
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">トランプ氏「ホルムズ海峡を米国領に宣言する」発言、イランは「戦略的敗北まで封鎖継続」で応酬——ADNOCタンカー2隻が再被弾</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/15 06:37 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 3-2. 固定サマリー（ffcccc強調ブロック）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/11 09:26 速報】イラン最高国家安全保障会議は9日、書記をモフセン・レザイー氏（革命防衛隊元司令官・対米強硬派）に交代——前書記ゾルガドル氏はハメネイ師の政治顧問に転じた。米シンクタンクISWは、レザイー氏がホルムズ海峡の管理権を含む最大限の要求実現を志向する一方、譲歩には消極的とみる（NBC）｜イラン外務省報道官バガイ氏は10日、ゾルガドル氏が8日に示した6条件（脅迫停止・戦争終結・海上封鎖解除と米軍撤収・戦争賠償・制裁解除・資産凍結解除）を改めて確認した（Time）｜トランプ大統領は10日、イランの賠償要求を一蹴し「同様に賠償を求める」と表明——2000年のUSSコール事件やイラン国内デモ弾圧の犠牲者への補償も対象に含める考えを示した（Euronews）｜高市首相は10日、オマーンのハイサム国王と約20分間電話会談——「追加的費用のない形での自由で安全な航行の一刻も早い回復」を要請し、海峡利用国を含む国際社会との協議をハイサム国王から確約された｜フーシ派は9日夜・10日と紅海の要衝モカを2日連続攻撃——政府軍関係者4人・民間人3人の計7人が死亡、30人が負傷、タイズ近郊でも衝突が続く（AP）｜市場ではブレント原油が87.72ドルへ4日続伸する一方、NYダウは53,975.98ドル（-0.11%）・S&P500は7,753.11ドル（-0.06%）と最高値圏から小反落——米戦略石油備蓄は1983年以来の低水準に落ち込んだ（Reuters）｜日本関係船は残り4隻で変化なし｜封鎖165日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/15 06:37 速報】UAE外務省は14日、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表し「海賊行為」と非難——負傷者なし、英UKMTOも2隻の軽微損傷を確認、紛争開始来ADNOC関連では15隻目の被弾（AP/Al Jazeera）｜トランプ大統領はロングアイランドの集会で「イランを完全に打ち負かした後、近くホルムズ海峡を米国領と宣言する」と発言——法的根拠・手続きへの言及はなし（Epoch Times）｜イラン副外相ガリババディ氏は「ホルムズ海峡はイランのものであり、米が『戦略的敗北』を受け入れるまで封鎖を継続する」と表明、アラグチー外相も対話再開について「決定はしていない」とし、イスラマバード覚書は「戦争終結」を意味し60日休戦の延長は不要との立場を示した（Iran International/ISNA）｜米はルビオ国務長官がオーストリア外相と会談・ギリシャ外相と電話協議し仲介国を拡大——オーストリアは会談地提供を申し出、カナダは対イラン制裁対象者5名を追加（AP）｜市場ではブレント原油が週央89.53ドルから87ドル台へ反落・IEAは供給不足の拡大に警鐘（Bloomberg）｜日本関係船は残り4隻で変化なし｜封鎖169日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### 3-3. インシデントリスト先頭に新規2件を追加

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li>🐹 8/11 JST（現地）イエメン政府によれば、フーシ派が紅海バブエルマンデブ海峡でエジプト所有・タンザニア籍の貨物船「ティハマ」（食料輸送中）に弾道ミサイル3発を発射する「二重攻撃」を実施。
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇦🇪 8/13夜〜14 JST</span>
  <span style="color:#e2e8f0;"> UAE外務省は、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表し「敵対的な攻撃」「海賊行為」と非難する声明を出した。ADNOCは負傷者なし・状況は制御下にあると説明。英UKMTOも2隻が軽微な損傷を負ったと確認したが、ADNOC発表とは別に船名は特定していない。紛争開始（2/28）以降、ADNOC関連船の被弾は今回で15隻目となり、直近1週間だけで3隻目という高頻度が続いている（AP/Al Jazeera）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🇺🇸🇮🇷 8/14 JST</span>
  <span style="color:#e2e8f0;"> トランプ大統領はニューヨーク州ロングアイランドでの集会で「イランを完全に打ち負かした後、近くホルムズ海峡を米国領と宣言する」と発言し、具体的な法的根拠・手続きには言及しなかった。同日、イラン副外相カゼム・ガリババディ氏は「ホルムズ海峡はイランのものであり、イランの命令の下でのみ開閉される」と述べ、米国が「戦略的敗北」を受け入れるまで封鎖を継続すると表明。アラグチー外相も対話再開について「決定はしていない」とし、6月のイスラマバード覚書は「戦争終結」を意味するものであり60日間の休戦延長は不要との立場を示した（Iran International/ISNA/Epoch Times）。</span>
</li>
<li>🐹 8/11 JST（現地）イエメン政府によれば、フーシ派が紅海バブエルマンデブ海峡でエジプト所有・タンザニア籍の貨物船「ティハマ」（食料輸送中）に弾道ミサイル3発を発射する「二重攻撃」を実施。
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 最新情勢カード（3枚）

### カード① 外交・体制

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇮🇷 IRGC上級顧問「トランプ政権終了まで戦争長期化も辞さず」——テヘランの戦略計算を異例に開示</div>
        <div class="s-body">革命防衛隊（IRGC）司令官の上級顧問モハンマド・レザ・ナグディ将軍（2019〜25年にIRGC調整担当副司令官）は12日、米PBSとの異例のインタビューで、イランが対米戦争をトランプ大統領の任期終了（2029年）まで意図的に長期化させる選択肢を検討していると明らかにした。「我々は敵が二度と攻撃を仕掛けようとは思わないだけの抑止力を確立しなければならない。一つの方法は、この戦争を次期大統領の任期まで引き延ばし消耗戦に持ち込むことだ。そうすればイランを再び攻撃しようとする者は代償を払うと理解するだろう」と述べた。同氏はまた、米国が2〜3日ごとに目標を変えており一貫した戦略を欠いていると批判し、米軍の実力は当初想定より劣ると学んだとも主張した。これらの発言は独立検証されたものではないが、イラン側が紛争をどう捉えているかを示す数少ない公的な手掛かりとなっている。</div>
        <div class="s-src">出典: PBS / Iran International / Israel National News（8/12 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇺🇸 トランプ氏「イラン敗北後、ホルムズ海峡を米国領に宣言する」——イランは「戦略的敗北まで封鎖継続」で応酬</div>
        <div class="s-body">トランプ大統領は14日、ニューヨーク州ロングアイランドでの集会で「イランを完全に打ち負かした後——現に大敗北を喫しつつあるが——近くホルムズ海峡を米国の領土と宣言する」と発言した。米国がどのように海峡の主権を主張するのか、正式な政府提案であるかについては説明しなかったが、国際法上重大な疑問を招く発言となった。同日、イラン副外相カゼム・ガリババディ氏は「ホルムズ海峡はイランのものであり、イランの命令の下でのみ開閉される」と述べ、米国が「戦略的敗北」を受け入れるまで封鎖を継続すると表明。アラグチー外相も、対話再開について「決定はしていない」とし、6月のイスラマバード覚書はあくまで「戦争終結」を意味するものであり60日間の休戦延長は不要との立場を改めて示した。並行してカナダが対イラン制裁対象者を5名追加し、欧州9カ国もEUの人権侵害を理由とした対イラン制裁（6名）に同調するなど、経済的圧力も強まっている。</div>
        <div class="s-src">出典: Epoch Times / Iran International / AP（8/14 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 地域安保

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🐹 フーシ派の紅海攻撃で今次紛争初の死者——エジプト所有船「ティハマ」二重攻撃で6人死亡</div>
        <div class="s-body">イエメン政府（国際的に承認されたアデン拠点政府）によれば、フーシ派は11日、紅海バブエルマンデブ海峡で食料を輸送中だったエジプト所有・タンザニア籍の貨物船「ティハマ」に弾道ミサイル3発を発射する「二重攻撃（double-tap）」を実施した。1回目の着弾で火災が発生し乗組員4名（パキスタン人3名・インドネシア人1名）が死亡、その後の救助活動中に再度ミサイルが撃ち込まれ、対応にあたっていた政府系「国家抵抗軍」隊員2名も死亡——計6名死亡・10名負傷となった。フーシ派系メディア（サバ通信）は軍事物資を積んだサウジ船を狙ったと別の主張をしており、対象船舶の特定を巡り説明が対立している。2/28の紛争開始以降、フーシ派関連の攻撃による初の確認死者で、専門家はホルムズ海峡と紅海の「2つの紛争が収斂しつつある」と分析する。</div>
        <div class="s-src">出典: Al Jazeera / AP / CNBC（8/11〜12 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇦🇪 ADNOC関連タンカー2隻が再び被弾——紛争開始来15隻目、直近1週間で3隻目の高頻度</div>
        <div class="s-body">UAE外務省は14日、アブダビ国営石油会社（ADNOC）関連のタンカー2隻が13日夜、ホルムズ海峡を通航中にイランのドローン攻撃を受けたと発表し「敵対的なイランの攻撃」「海賊行為」と強く非難した。ADNOCは負傷者がいないこと、状況は制御下にあることを確認。英海軍系のUKMTO（英国海運貿易オペレーション）も2隻が軽微な損傷を負ったとの報告を確認したが、ADNOC発表とは別に船名までは特定していない。UAE外務省は、商船への攻撃や海峡の経済的威圧の手段としての利用は国連安保理決議2817の重大な違反であり、海賊行為に相当すると強調した。ADNOCによれば紛争開始（2/28）以降の被弾は今回で通算15隻目となり、直近1週間だけでも3隻目という高い頻度が続いている。</div>
        <div class="s-src">出典: Al Jazeera / AP / UKMTO（8/14 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ 日本外交・市場

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇯🇵 通航量は週間最低の8隻に——トランプ氏「完全支配」主張も実態は乖離、原油は反落</div>
        <div class="s-body">ロイターによれば、11日のホルムズ海峡通航はわずか8隻にとどまり、Kplerデータの直近10日平均（約12隻）をさらに下回る一週間ぶりの低水準となった（戦前は1日130〜140隻）。トランプ大統領は12日、Truth Socialで「米国はホルムズ海峡を完全に支配している。我々はそれを維持するつもりだ」と改めて主張したが、専門家からは「イランは依然として海峡の海上交通を妨害する十分な能力を保持している」との反論が出ている。米エネルギー長官クリス・ライト氏が示した「直近7日平均で日量900万バレル近くが海峡を出ている」との説明にも、独立系分析（Obsidian Risk Advisors）から根拠を疑問視する声が上がった。市場では、EIA統計で米原油在庫が前週比1,740万バレル増（2023年来最大の週間増）となったことも重なり、ブレント原油は6営業日続伸で89ドル台に迫った後、13日は87.92ドル（前日比-1.19%）へ反落した。</div>
        <div class="s-src">出典: Reuters / Al Jazeera / TradingEconomics（8/12〜13 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🌍 米、仲介国を欧州へ拡大——オーストリア・ギリシャに接触、ブレントは87ドル台で下げ止まり</div>
        <div class="s-body">AP通信によれば、対話が停滞する中、米国務省は伝統的な仲介国（オマーン・パキスタン・トルコ・カタール）に加え、欧州諸国への働きかけを静かに拡大している。ルビオ国務長官は11日、ワシントンでオーストリアのマインライトナー外相と直接会談し、12日にはギリシャのゲラペトリティス外相と電話協議を行った。オーストリア外務省は今後の対イラン協議の会場提供を申し出、「軍事的解決策はあり得ない、外交的解決策こそが優先事項」と強調。ギリシャ外務省も「航行の自由と海洋の安全保障の重要性」を訴えた。一方イラン外務省は、アラグチー外相と欧州各国外相との通話について「ホルムズ海峡の将来的な管理メカニズム」を協議したものと説明しており、双方の受け止め方には差がある。市場では、ブレント原油が週央（12日）に一時89.53ドルまで上昇した後、87ドル台まで反落して推移しており、IEAは2026年の世界的な供給不足幅が過去5年で最大になるとの見通しを示している。</div>
        <div class="s-src">出典: AP / Bloomberg / 外務省・国土交通省（8/11〜14 JST 更新、日本関係船情報は8/15 06:37 JST再確認）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 21「フーシ派の紅海攻撃で今次紛争初の死者、IRGC顧問は『トランプ政権終了まで長期化』発言——米軍はパナマ籍船に発砲」——封鎖167日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 22「トランプ氏がホルムズ海峡の米国領化を宣言、イランは『戦略的敗北まで封鎖継続』で応酬——ADNOCタンカー2隻が再被弾」——封鎖169日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🤝 <strong>IRGC上級顧問ナグディ氏がPBSで「トランプ政権終了まで戦争長期化も選択肢」と発言し消耗戦戦略を異例に開示（8/12）／フーシ派が紅海で今次紛争初の死者を出す攻撃を実施——エジプト所有船「ティハマ」への二重攻撃で6人死亡（8/11）／米軍ヘリがパナマ籍船「ヴェラ・ノヴァ」に対封鎖破り阻止でヘルファイア発射（8/11）／トランプ氏「米国はホルムズを完全支配」と主張も通航量は週間最低の8隻に低下（8/11〜12）／パキスタンが仲介継続、内相がテヘラン訪問中／日本関係船は残り4隻で変化なし——封鎖167日目・MOU機雷除去期限（7/17）を未着手のまま徒過</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①レザイー新体制下でイランの対米姿勢はどう変化するか ②トランプの逆賠償要求がイラン側の態度をさらに硬化させるか ③イラン・オマーンの「最終段階」協議がいつ正式合意に至るか ④フーシ派のモカ攻撃を含むイエメン内戦がどこまで拡大するか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残3日（8/16）</span>
<!-- OLD:END -->
<!-- NEW:START -->
        🤝 <strong>トランプ大統領がロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言（8/14）／イラン副外相ガリババディ氏は「米が戦略的敗北を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開を「未決定」とし60日休戦の延長は不要と主張（8/14）／UAE、ADNOC関連タンカー2隻が13日夜の通航中にイランのドローン攻撃で被弾したと発表——紛争開始来15隻目、負傷者なし（8/14）／米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を欧州へ拡大、カナダは対イラン制裁5名を追加（8/11〜14）／ブレント原油は週央89.53ドルから87ドル台へ反落、IEAは供給不足拡大に警鐘／日本関係船は残り4隻で変化なし——封鎖169日目・MOU機雷除去期限（7/17）を未着手のまま徒過</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①トランプ氏の「米国領化」発言が交渉に与える影響 ②イランの「戦略的敗北」要求水準が対話再開の障害となるか ③欧州仲介国拡大（オーストリア・ギリシャ）が突破口となるか ④ADNOCタンカーへの攻撃頻発が主要船社の航行判断にどう影響するか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残1日（8/16）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年8月13日 10:37 JST 更新</span><br>
  📊 <strong>IRGC上級顧問「トランプ政権終了まで長期化も選択肢」と発言——フーシ派の紅海攻撃で今次紛争初の死者：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — IRGC上級顧問が消耗戦による長期化戦略を公言したことで、短期妥結を前提とする本シナリオの現実味はさらに後退した<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — 通航量は週間最低の8隻に沈み、パキスタンの仲介努力も対話再開には至らず、高止まりの膠着状態が変わらず最多シナリオであり続けている<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 米軍によるパナマ籍船への発砲が3週間で3件目となり、対イラン港湾封鎖の一方的な既成事実化が一段と進んだ<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — フーシ派の紅海攻撃で今次紛争初の死者が出たことに加え、IRGC顧問の長期化発言が地域紛争の構造的な長期化リスクを裏付けている<br>
  <strong style="color:#f87171;">イラン側の一部勢力が短期妥結よりも消耗戦による抑止力確立を志向する姿勢を公式に示したことで、外交トラックの停滞が一段と長期化する様相が強まった。フーシ派の紅海攻撃による死者発生と米軍の実力行使拡大が重なり、ホルムズ単体にとどまらない地域全体の軍事的緊張が高止まりしている（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月13日 10:37 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年8月15日 06:37 JST 更新</span><br>
  📊 <strong>トランプ氏「ホルムズを米国領に」発言——イランは「戦略的敗北まで封鎖継続」で応酬、ADNOCタンカー再被弾：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — トランプ氏の「米国領化」発言とイランの「戦略的敗北」要求は双方の立場を一段と硬直化させ、短期妥結の見通しをさらに後退させた<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — 米が仲介国を欧州（オーストリア・ギリシャ）へ拡大する動きはあるが、当事者間の実質協議は依然として再開されておらず、最多シナリオの座は変わらない<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — アラグチー外相がイスラマバード覚書を「戦争終結」であり60日休戦の延長は不要と位置付けたことは、MOU枠組みそのものの形骸化を一段と裏付ける<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — ADNOCタンカーへの攻撃が紛争開始来15隻目に達し、トランプ氏の「米国領化」宣言もイラン側の態度硬化を招きかねず、軍事的緊張の高止まりが続いている<br>
  <strong style="color:#f87171;">トランプ大統領がホルムズ海峡の米国領化に言及したことで、既に硬直化していた外交トラックはさらに動きにくくなった。イラン側も「戦略的敗北」を対話再開の前提に据えたことで、双方の要求水準の乖離が一段と鮮明になっている（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月15日 06:37 JST 時点での分析に基づく自動同期
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本の本文

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>IRGC上級顧問が「トランプ政権終了まで戦争を長期化させる」戦略を公にPBSで語ったことは、段階的MOU履行シナリオにとって明確な逆風である。テヘラン側の一部勢力が短期妥結よりも消耗戦による抑止力確立を志向していることが公式に示された形で、パキスタンなど仲介国が交渉再開を模索する一方、当事者間の時間軸に対する認識のずれが一段と際立った。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>トランプ大統領の「ホルムズ海峡米国領化」発言は、テヘランにとって交渉のインセンティブそのものを損ないかねない発言であり、段階的MOU履行シナリオへの逆風となった。一方で米国が欧州（オーストリア・ギリシャ）への仲介拡大に動いていることは、従来にない新しいチャネルの模索でもある。ただしイラン側が「戦略的敗北」承認を対話再開の前提に据えている以上、両者の隔たりを埋める兆しは乏しい。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>トランプ氏の「完全支配」発言とは裏腹に、実際の通航量は8/11に週間最低の8隻まで落ち込み、Windwardの衛星監視でも係留船51隻・正規通航わずか5隻という膠着状態が確認された。パキスタンは10日にイラン・サウジ・クウェートと協議し内相をテヘランへ派遣するなど仲介努力を継続しているが、当事者間の対話再開には至っておらず、低空飛行の膠着が最も蓋然性の高い展開であり続けている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>米国務省がオマーン・パキスタン・トルコ・カタールに加え、オーストリア・ギリシャといった欧州諸国へも接触を広げていることは、伝統的な仲介チャネルが行き詰まっている証左でもある。イラン外務省は欧州各国との通話を「海峡の将来管理メカニズムの協議」と説明する一方、米イラン間の直接対話再開についてアラグチー外相は「未決定」と留保しており、膠着状態が最も蓋然性の高い展開であり続けている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>米軍によるパナマ籍船「ヴェラ・ノヴァ」への発砲は、対イラン港湾封鎖の摘発が7/15・7/24に続き3週間で3件目となったことを意味し、米側の一方的な「管理の既成事実化」が続いている実態を示す。イラン議会の通行料法案の審議に目立った進展はないが、米側の実力行使が常態化していること自体が機能不全の一形態として定着しつつある。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>アラグチー外相が6月のイスラマバード覚書を「戦争終結（の合意）」であり「60日間の休戦」ではないと位置付け直したことは、MOU解釈をめぐる米イラン間の食い違いを一段と鮮明にした。トランプ大統領のホルムズ海峡米国領化発言も、既存の国際枠組みを迂回する形での事実上の管理を志向するものであり、両者ともにMOUという公式枠組みの形骸化を後押ししている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>フーシ派の紅海攻撃で今次紛争初の死者が出たことは、イエメン内戦とイラン・米対立という「2つの紛争の収斂」（専門家評）を明確に裏付けた。加えてIRGC上級顧問が2029年までの長期化戦略に公然と言及したことで、短期的な軍事的緊張だけでなく、紛争そのものの構造的な長期化リスクが従来以上に現実味を帯びている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>ADNOC関連タンカーへの攻撃が紛争開始来15隻目に達し、直近1週間だけで3隻目という高頻度が続いていることは、海峡の軍事的緊張が沈静化していない実態を示す。トランプ氏の「米国領化」発言とイラン側の「戦略的敗北」要求という、互いに譲歩の余地を残さない強硬なレトリックの応酬が、偶発的エスカレーションのリスクを高めている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5つ・分析日時）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">IRGC顧問の「長期化発言」がイラン指導部内でどこまで共有された方針か</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">フーシ派の紅海攻撃激化がイエメン内戦の全面再燃に至るか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">米軍による封鎖破り船舶への実力行使（発砲）が今後どこまで拡大するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">パキスタン仲介による米イラン対話再開のめどが立つか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月11日 09:26 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">トランプ氏の「米国領化」発言に国際法上・外交上どう反応が広がるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イランの「戦略的敗北」要求が対話再開の前提として維持され続けるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">欧州仲介国拡大（オーストリア・ギリシャ）が新たなチャネルとして機能するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">ADNOCタンカーへの攻撃頻発が主要船社の航行判断にどう影響するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月15日 06:37 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月13日 10:37 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">外交トラックはパキスタンの仲介努力（イラン・サウジ・クウェートとの協議、内相のテヘラン訪問）を除き目立った進展がなく、IRGC上級顧問による「長期化発言」が示す通りイラン側の時間軸認識も長期戦を前提としつつある。【北側航路（イラン指定）】Windward衛星監視によれば8/11の正規通航はわずか5隻・不明船2隻で、Larak/East両錨地に係留船51隻——8/4被弾のバルカー船は9日経過後も推進喪失状態が継続。【南ルート（Omani coastal corridor）】8月上旬の航路案合意以降、目立った追加進展の報告はなく、米・イラン間の3者協議は事実上停止したまま。【米の交渉姿勢】トランプ大統領は「米国はホルムズを完全支配」と主張する一方、米軍はパナマ籍船「ヴェラ・ノヴァ」に発砲するなど封鎖破り船舶への実力行使を継続（3週間で3件目）。【紅海・バブエルマンデブ】フーシ派の攻撃でエジプト所有船「ティハマ」の乗組員・救助隊員計6名が死亡——今次紛争開始後初のフーシ派関連死者。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/13 10:37 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月15日 06:37 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">外交トラックは米が仲介国をオーストリア・ギリシャへ拡大する動きを見せる一方、イラン側はアラグチー外相が対話再開を「未決定」と明言するなど目立った進展がなく、トランプ大統領の「ホルムズ海峡米国領化」発言が緊張を一段と高めている。【北側航路（イラン指定）】直近の公開監視データに大きな更新の報告はなく、高止まりの膠着状態が続いているとみられる。【南ルート（Omani coastal corridor）】8月上旬の航路案合意以降、目立った追加進展の報告はなく、米・イラン間の3者協議は事実上停止したまま。【米の交渉姿勢】トランプ大統領は「イラン敗北後にホルムズ海峡を米国領に宣言する」と発言し、封鎖の既成事実化路線を一段と鮮明にした。【紅海・バブエルマンデブ】直近の大規模攻撃の続報はないが、8/11のフーシ派攻撃による死者発生を受け警戒水準は高いまま。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/15 06:37 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）― 最後に作成

### 9-1. 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
🇮🇷 IRGC上級顧問が「トランプ政権終了まで戦争長期化も辞さず」と発言——消耗戦戦略を異例に開示。
<!-- OLD:END -->
<!-- NEW:START -->
🇺🇸 トランプ氏「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言——イランは「戦略的敗北まで封鎖継続」で応酬。
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
🐹 フーシ派の紅海攻撃で今次紛争初の死者、米軍はパナマ籍船に発砲。通航量は週間最低の8隻。
<!-- OLD:END -->
<!-- NEW:START -->
🇦🇪 ADNOC関連タンカー2隻が再びドローン攻撃で被弾（紛争開始来15隻目）。ブレント原油は87ドル台で下げ止まり。
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
⏳ パキスタン仲介で米イラン対話が再開するか、封鎖167日目——通航正常化のめどは依然立たず。
<!-- OLD:END -->
<!-- NEW:START -->
⏳ 米が仲介国をオーストリア・ギリシャへ拡大するも対話再開の道筋は立たず、封鎖169日目。
<!-- NEW:END -->
<!-- APPLY:END -->

### 9-2. ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷IRGC顧問「長期化も辞さず」</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🐹紅海攻撃で初の死者(6名)</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚓米軍が封鎖破り船に発砲</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📉ブレント87.92ドルへ反落</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸トランプ「ホルムズ米国領化」発言</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇦🇪ADNOCタンカー再被弾(15隻目)</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷イラン「戦略的敗北まで封鎖」</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📊ブレント87ドル台で下げ止まり</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新（Claude Codeでマージ）

### 10-1. `latest` 配列：新規3件を先頭に追加し、末尾3件（latest-trump-total-control-transit-drop-0812／latest-snsc-rezaei-secretary-0809／latest-trump-counter-compensation-0810）を `archive` の新規バッチへ移動

新規追加分（先頭3件・`isLatest`は最新のみ true）：

```json
{
  "id": "latest-adnoc-tankers-drone-attack-0813",
  "title": "ADNOC関連タンカー2隻が再び被弾——ホルムズ海峡通航中にイランのドローン攻撃、紛争開始来15隻目",
  "body": "UAE外務省は14日、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表し「海賊行為」と非難した。負傷者はなく状況は制御下にあるという。英UKMTOも2隻が軽微な損傷を受けたと確認。ADNOC関連船が被弾するのは紛争開始来15隻目となる。",
  "sourceLabel": "AP",
  "date": "2026年8月13日（現地）/ 2026年8月14日 JST",
  "label": "🇦🇪 軍事",
  "url": "https://www.usnews.com/news/world/articles/2026-08-14/2-uae-tankers-attacked-while-transiting-strait-of-hormuz-and-other-news-from-the-middle-east",
  "isLatest": true
},
{
  "id": "latest-trump-hormuz-us-territory-0814",
  "title": "トランプ氏「イラン敗北後、ホルムズ海峡を米国領に宣言する」——国際法上の疑問符",
  "body": "トランプ大統領は14日、ニューヨーク州ロングアイランドでの集会で「イランを完全に打ち負かした後、近くホルムズ海峡を米国領と宣言する」と発言した。具体的な法的根拠や手続きには言及しておらず、国際法上の重大な疑問を招く発言となった。",
  "sourceLabel": "Epoch Times",
  "date": "2026年8月14日（現地）/ 2026年8月14日 JST",
  "label": "🇺🇸 外交",
  "url": "https://www.theepochtimes.com/us/trump-says-hell-declare-the-hormuz-strait-a-us-territory-pretty-soon-6075391",
  "isLatest": false
},
{
  "id": "latest-iran-strategic-defeat-araghchi-0814",
  "title": "イラン副外相「米が戦略的敗北認めるまで封鎖継続」——アラグチー外相は対話再開「未決定」",
  "body": "イラン副外相カゼム・ガリババディ氏は14日、「ホルムズ海峡はイランのものであり、イランの命令の下でのみ開閉される」と述べ、米国が「戦略的敗北」を受け入れるまで封鎖を継続すると表明した。アラグチー外相も同日、対話再開について「決定はしていない」と述べ、6月のイスラマバード覚書は「戦争終結」を意味し60日休戦の延長は不要との立場を示した。",
  "sourceLabel": "Iran International",
  "date": "2026年8月14日（現地）/ 2026年8月14日 JST",
  "label": "🇮🇷 外交",
  "url": "https://www.iranintl.com/en/liveblog/202608084952",
  "isLatest": false
}
```

既存の先頭3件（`latest-irgc-naqdi-prolong-war-0812`／`latest-houthi-tihamah-doubletap-0811`／`latest-us-helicopter-velanova-strike-0811`）は上記3件の直後に残し、`isLatest` は全て false に統一（新規1件目のみ true）。

移動対象（末尾の既存3件 → `archive` 新規バッチへ、`batchLabel`: "2026年8月中旬（8/9〜8/12）"）：
`latest-trump-total-control-transit-drop-0812`／`latest-snsc-rezaei-secretary-0809`／`latest-trump-counter-compensation-0810`

### 10-2. `osint` 配列：新規1件を先頭に追加（`isLatest: true`）、既存の `osint-hormuz-transit-drop-trump-control-0812` は `isLatest: false` に変更

```json
{
  "id": "osint-uae-adnoc-attack-piracy-0814",
  "date": "2026年8月14日（現地）/ 2026年8月14日 JST",
  "titleJa": "UAE、ADNOC関連タンカー2隻へのイラン攻撃を非難——紛争開始来15隻目の被弾",
  "titleEn": "UAE accuses Iran of attacks on two ADNOC vessels in Strait of Hormuz",
  "country": "カタール",
  "media": "Al Jazeera",
  "cardBg": "rgba(56,189,248,0.05)",
  "cardBorder": "rgba(56,189,248,0.25)",
  "badgeColor": "#38bdf8",
  "borderColor": "rgba(56,189,248,0.4)",
  "textColor": "#7dd3fc",
  "url": "https://www.aljazeera.com/news/2026/8/14/uae-accuses-iran-of-attacks-on-two-adnoc-vessels-in-strait-of-hormuz",
  "isLatest": true
}
```

### 10-3. `updated` / `staleNotice`

```json
"updated": "2026年8月15日 06:37 日本時間JST",
"staleNotice": ""
```

---

## [S11] 更新ログ（2ブロック構成）

### ブロック1：常時表示エリア（3件固定）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月13日 10:37 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/13 10:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランIRGC上級顧問ナグディ氏がPBSに「トランプ政権終了（2029年）まで戦争を長期化させ消耗戦に持ち込む選択肢がある」と発言（8/12）・フーシ派が紅海バブエルマンデブ海峡でエジプト所有船「ティハマ」を二重攻撃し乗組員4名・救助隊員2名の計6名死亡10名負傷——今次紛争開始後初のフーシ派関連死者（8/11）・米軍ヘリがパナマ籍船「ヴェラ・ノヴァ」に対封鎖破り阻止でヘルファイア2発発射（3週間で3件目の摘発、8/11）・トランプ氏「米国はホルムズを完全支配」と主張も通航量は8/11に週間最低の8隻へ低下・パキスタンが仲介継続——内相がテヘラン訪問中（8/10）・ブレント原油は87.92ドルへ反落（6営業日続伸後、-1.19%）、EIA原油在庫は2023年来最大の週間増（+1740万バレル）・NYダウ53,770ドル(-21.58、3日続落)・日本関係船は残り4隻で変化なし・封鎖167日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月11日 09:26 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/11 09:26</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン最高国家安全保障会議、書記をゾルガドル氏から対米強硬派モフセン・レザイー氏（革命防衛隊元司令官）に交代——ゾルガドル氏はハメネイ師政治顧問に転身（NBC、8/9）・前書記の6条件（脅迫停止・戦争終結・封鎖解除と米軍撤収・戦争賠償・制裁解除・資産凍結解除）は継承・トランプ大統領はイランの賠償要求に「同様の賠償を求める」と反発、USSコール事件等も対象に（Euronews、8/10）・高市首相はオマーンのハイサム国王と電話会談し追加費用のない自由航行の回復を要請（8/10）・フーシ派は紅海の要衝モカを2日連続攻撃し7人死亡・イエメン内戦拡大の懸念（AP）・ブレント原油87.72ドルへ4日続伸(+4.95%)、NYダウ53,975.98ドル(-0.11%)・S&P500は7,753.11ドル(-0.06%)と小反落・日本関係船は残り4隻で変化なし・封鎖165日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月15日 06:37 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/15 06:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表——紛争開始来15隻目の被弾・負傷者なし（8/14）・トランプ大統領はロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言（8/14）・イラン副外相ガリババディ氏は「米が戦略的敗北を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開「未決定」とし60日休戦の延長は不要と主張（8/14）・米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を欧州へ拡大、カナダは対イラン制裁5名追加（8/11〜14）・ブレント原油は週央89.53ドルから87ドル台へ反落、IEAは供給不足拡大に警鐘・日本関係船は残り4隻で変化なし・封鎖169日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月13日 10:37 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/13 10:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランIRGC上級顧問ナグディ氏がPBSに「トランプ政権終了（2029年）まで戦争を長期化させ消耗戦に持ち込む選択肢がある」と発言（8/12）・フーシ派が紅海バブエルマンデブ海峡でエジプト所有船「ティハマ」を二重攻撃し乗組員4名・救助隊員2名の計6名死亡10名負傷——今次紛争開始後初のフーシ派関連死者（8/11）・米軍ヘリがパナマ籍船「ヴェラ・ノヴァ」に対封鎖破り阻止でヘルファイア2発発射（3週間で3件目の摘発、8/11）・トランプ氏「米国はホルムズを完全支配」と主張も通航量は8/11に週間最低の8隻へ低下・パキスタンが仲介継続——内相がテヘラン訪問中（8/10）・ブレント原油は87.92ドルへ反落（6営業日続伸後、-1.19%）、EIA原油在庫は2023年来最大の週間増（+1740万バレル）・NYダウ53,770ドル(-21.58、3日続落)・日本関係船は残り4隻で変化なし・封鎖167日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月11日 09:26 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/11 09:26</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン最高国家安全保障会議、書記をゾルガドル氏から対米強硬派モフセン・レザイー氏（革命防衛隊元司令官）に交代——ゾルガドル氏はハメネイ師政治顧問に転身（NBC、8/9）・前書記の6条件（脅迫停止・戦争終結・封鎖解除と米軍撤収・戦争賠償・制裁解除・資産凍結解除）は継承・トランプ大統領はイランの賠償要求に「同様の賠償を求める」と反発、USSコール事件等も対象に（Euronews、8/10）・高市首相はオマーンのハイサム国王と電話会談し追加費用のない自由航行の回復を要請（8/10）・フーシ派は紅海の要衝モカを2日連続攻撃し7人死亡・イエメン内戦拡大の懸念（AP）・ブレント原油87.72ドルへ4日続伸(+4.95%)、NYダウ53,975.98ドル(-0.11%)・S&P500は7,753.11ドル(-0.06%)と小反落・日本関係船は残り4隻で変化なし・封鎖165日目・ニュース4件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse 先頭に旧3件目（8/9 10:06分）を挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月7日 09:45 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
          <div>📅 <strong>2026年8月7日 09:45 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ 合計エントリー数（常時表示3 + log-collapse内）は現在11件（8/7〜7/26既存分含む）で上限10件を1件超過。次回更新時にlog-collapse最古（出典リンク直前）の削除を検討してください。

---

## [C01] タンカー確認（SHIP_CONFIG dateConfirmed）

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年8月13日 10:37 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近会見（8/4）は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年8月15日 06:37 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近会見（8/4）は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- NEW:END -->
<!-- APPLY:END -->

**C01 タンカー確認**：日本語「日本関係船舶 ホルムズ海峡 通過 足止め」「外務省 ホルムズ海峡 日本関係船舶 8月」「金子国土交通大臣 会見 ホルムズ海峡 8月」＋英語「Japanese ships Strait of Hormuz stranded detained August 2026」の4クエリ全てでweb検索済み（外務省・国土交通省の一次情報を優先確認）／変化なし→残り4隻のまま・dateConfirmedを本日日時「変更なし」で更新

---

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-08-13T10:37:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-15T06:37:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [ARCHIVE] archive_timeline.json への追記（Claude Codeで手動str_replace適用・apply_diffs.py対象外）

**対象ファイル：** `docs/data/archive_timeline.json`
**対象箇所：** `entries` 配列の末尾（2026-08-07エントリーの直後、配列を閉じる `]` の直前）

<!-- APPLY:START -->
<!-- OLD:START -->
        {
          "title": "フーシ派、サウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目",
          "url": "https://www.dailysabah.com/world/mid-east/yemens-houthis-reportedly-strike-saudi-tanker-transiting-red-sea",
          "sourceLabel": "Reuters / AFP"
        }
      ]
    }
  ]
}
<!-- OLD:END -->
<!-- NEW:START -->
        {
          "title": "フーシ派、サウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目",
          "url": "https://www.dailysabah.com/world/mid-east/yemens-houthis-reportedly-strike-saudi-tanker-transiting-red-sea",
          "sourceLabel": "Reuters / AFP"
        }
      ]
    },
    {
      "date": "2026-08-15",
      "dateLabel": "2026/08/15 06:37",
      "blockadeDay": 169,
      "summary": "UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表——紛争開始来15隻目の被弾・負傷者なし（8/14）・トランプ大統領はロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言（8/14）・イラン副外相ガリババディ氏は「米が戦略的敗北を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開「未決定」とし60日休戦の延長は不要と主張（8/14）・米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を欧州へ拡大、カナダは対イラン制裁5名追加（8/11〜14）・ブレント原油は週央89.53ドルから87ドル台へ反落、IEAは供給不足拡大に警鐘・日本関係船は残り4隻で変化なし・封鎖169日目・ニュース4件更新・osint更新",
      "relatedNews": [
        {
          "title": "ADNOC関連タンカー2隻が再び被弾——ホルムズ海峡通航中にイランのドローン攻撃、紛争開始来15隻目",
          "url": "https://www.usnews.com/news/world/articles/2026-08-14/2-uae-tankers-attacked-while-transiting-strait-of-hormuz-and-other-news-from-the-middle-east",
          "sourceLabel": "AP"
        },
        {
          "title": "トランプ氏「イラン敗北後、ホルムズ海峡を米国領に宣言する」——国際法上の疑問符",
          "url": "https://www.theepochtimes.com/us/trump-says-hell-declare-the-hormuz-strait-a-us-territory-pretty-soon-6075391",
          "sourceLabel": "Epoch Times"
        },
        {
          "title": "イラン副外相「米が戦略的敗北認めるまで封鎖継続」——アラグチー外相は対話再開「未決定」",
          "url": "https://www.iranintl.com/en/liveblog/202608084952",
          "sourceLabel": "Iran International"
        },
        {
          "title": "米、仲介国を欧州へ拡大——ルビオ氏がオーストリア・ギリシャ外相と接触",
          "url": "https://lasvegassun.com/news/2026/aug/14/with-us-iran-talks-stalled-diplomatic-efforts-expa/",
          "sourceLabel": "AP"
        }
      ]
    }
  ]
}
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック（本日のセルフチェック項目数：12件）

```
[✓] Step 0 project_knowledge_search 2クエリ実施・baseline確認（8/13 10:37 JST・封鎖167日目）
[✓] C01タンカー確認：日本語3クエリ＋英語1クエリ全実施・変化なし・残り4隻
[✓] S01 ヘッダー ― 2026年8月15日 06:37 JST・封鎖169日目 ✓
[✓] S02 TICKER ― ADNOC再被弾・トランプ米国領化発言・イラン戦略的敗北・欧州仲介拡大・封鎖169日目 ✓
[✓] S03 速報インシデント ― 8/15 06:37付け・トグル見出し／ffcccc要約／li2件を更新 ✓
[✓] S04 情勢カード3枚 ― 全カードを本日情勢に更新（重複表現を避け各カードで異なる切り口）✓
[✓] S05 COUNTDOWN ― Phase22・封鎖169日目・MOU期限残1日 ✓
[✓] S06 シナリオ確率補足バナー ― 8/15 06:37 JST日付更新・A↓B→C↑D↑（矢印はダッシュボード自動同期のため数値は非記載）✓
[✓] S07 シナリオ4本 ― A/B/C/D本文を本日情勢に更新（S06と異なる切り口で記述）✓
[✓] S08 シナリオフッター ― 次の焦点5点を本日版に更新（S05のdl-noteと重複しない表現）✓
[✓] S08.5 全ルート現況サマリー ― 8/15 06:37 JST更新・S08.5固有の切り口（航路別）で記述 ✓
[✓] S09 30秒カラム ― 3行サマリー＋バッジ5枚を最後に更新 ✓
[✓] S10 news_data.json ― latest 3件追加（3件をarchiveへ移動）・osint 1件追加・updated日付 ✓
[✓] S11 更新ログ ― 2ブロック構成（常時表示3件固定＋log-collapse先頭挿入）✓
[✓] C01 SHIP_CONFIG dateConfirmed ― 8/15 06:37 JST・変化なし ✓
[✓] JSON-LD dateModified ― 2026-08-15T06:37:00+09:00 ✓
[✓] archive_timeline.json ― 2026-08-15エントリー追加（Claude Code手動str_replace対象）✓

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記は変更なし（S04カード③の枠組みのみ差し替え）✓
TICKER内JST表記チェック：全日付にJST付き ✓
Al Jazeera使用箇所チェック：📰関連最新ニュース(latest)には不使用、osintのみ使用 ✓
人名表記チェック：習近平の言及なし（該当なし）／トランプ・アラグチー・ガリババディ等は日本語カタカナ表記で統一 ✓
URL捏造チェック：全URLはweb_search結果から取得した実在URLのみ使用 ✓
禁止ソースチェック：毎日新聞・Wikipedia・TBS・朝日新聞・NHK・東京新聞・テレビ朝日は不使用 ✓
```
