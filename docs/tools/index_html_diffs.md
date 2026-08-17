# index_html_diffs.md — 2026年8月17日 09:04 JST 更新分

> Claude Code への指示：以下の差分を docs/index.html および docs/data/news_data.json に適用してください。
> 変更箇所以外は絶対に触らないこと。
> docs/data/archive_timeline.json への追記は [ARCHIVE] セクションに個別記載（apply_diffs.pyの対象外のため、str_replaceで手動適用してください）。

---

## Step 0 セルフチェック（本文執筆前の事前確認）

project_knowledge_search にて「index_html_diffs.md 最新 更新 JST」「更新ログ 出典 JST 更新」を実行し、直近の確定更新が2026年8月15日 06:37 JST（封鎖169日目）であることを確認。raw.githubusercontent.com から docs/index.html・docs/data/news_data.json・docs/data/archive_timeline.json を直接取得し、8/15 06:37 JST時点の内容と完全一致することを確認した（ADNOCタンカー再被弾・トランプ「米国領化」発言・イラン「戦略的敗北」応酬・封鎖169日目）。

C01タンカー確認：日本語3クエリ（「日本関係船舶 ホルムズ海峡 通過 足止め 8月」「外務省 ホルムズ海峡 日本関係船舶 8月17日」「金子国土交通大臣 会見 ホルムズ海峡 8月」）＋英語1クエリ（「Japanese ships Strait of Hormuz stranded detained August 2026」）全て実施。外務省・国交省ともに8/4会見（熊本地震対応が主題でホルムズ言及なし）以降の新規発表なしを確認。変化なし・残り4隻のまま。

封鎖日数：Day1=2026年2月28日起算で2026年8月17日はDay171（8/15のDay169から+2）。

**本日の最重要事案：** 6月17日署名のイスラマバード覚書が定める60日間の交渉・最終合意期限が8月16日（月）に到来し、米・イラン双方とも延長に言及しないまま事実上形骸化した（共同通信・時事通信・Al Jazeera確認）。アラグチー外相は「対話再開はまだ決定していない」と表明する一方、オマーンとの新航路協議は「政治的解決が前提」としつつ継続。トランプ大統領は「ホルムズ海峡米国領化」路線を維持し、ベッセント財務長官も「前例のない」対イラン措置を予告。イラン副外相は「海峡はイランのものであり続ける」と応酬した。米シンクタンク・スティムソン・センターは、米側の迎撃ミサイル・戦略石油備蓄がいずれも逼迫していると指摘し「対イラン圧力手段は乏しい」と分析している。

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表——紛争開始来15隻目の被弾・負傷者なし／トランプ大統領はロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と表明／イラン副外相ガリババディ氏は「米が『戦略的敗北』を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開を「未決定」としイスラマバード覚書は「戦争終結」を意味し60日休戦の延長は不要と主張／米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を拡大、カナダは対イラン制裁5名を追加／ブレント原油は87ドル台で下げ止まり、IEAは石油備蓄急減に警鐘／日本関係船は残り4隻で変化なし／MOU機雷除去期限（7/17）を徒過・最終期限まで残1日（8/16）／封鎖169日目）</span>
    <span class="badge-item badge-date">📅2026年8月15日 06:37 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米・イラン間の60日間停戦・最終合意期限「イスラマバード覚書」が8月16日に到来し、双方とも延長に言及しないまま事実上形骸化——共同通信・時事通信は「不安定な膠着状態」の長期化を報道／イラン・アラグチー外相は15日「米国との対話再開はまだ決定していない」と表明する一方、オマーンとの新航路協議は「政治的解決が前提」としつつ継続の姿勢／トランプ大統領は「ホルムズ海峡米国領化」路線を崩さず、ベッセント財務長官も「前例のない」対イラン措置を予告／イラン副外相は「海峡はイランのものであり、イランのものであり続ける」と応酬／米シンクタンク専門家は迎撃ミサイル備蓄・戦略石油備蓄の逼迫を指摘し「トランプ政権に残る圧力手段は乏しい」と分析／ブレント原油は88ドル台後半へ上昇（週初比+1%超）／日本関係船は残り4隻で変化なし／封鎖171日目）</span>
    <span class="badge-item badge-date">📅2026年8月17日 09:04 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年8月15日 06:37 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月15日 06:37 JST） -->
      🇦🇪【ADNOCタンカー再被弾】UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にドローン攻撃受けたと発表——負傷者なし・紛争開始来15隻目の被弾、UKMTOも軽微損傷を確認（14日）｜🇺🇸 トランプ大統領「イラン敗北後、ホルムズ海峡を米国領に宣言する」——ロングアイランドの集会で表明、法的根拠には言及せず（14日）｜🇮🇷 イラン副外相ガリババディ氏「米が『戦略的敗北』を認めるまで封鎖継続」——アラグチー外相は対話再開「未決定」、イスラマバード覚書は「戦争終結」であり60日休戦の延長は不要と主張（14日）｜🌍 米、仲介国を拡大——ルビオ国務長官がオーストリア外相と会談・ギリシャ外相と電話協議、カナダは対イラン制裁5名追加（11〜14日）｜🛢️ ブレント原油は87ドル台で下げ止まり（週央89.53ドルから反落）・IEAは石油備蓄急減に警鐘｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英4クエリで再確認・金子国交相8/4会見はホルムズ言及なし）｜⏳ MOU機雷除去期限（7/17）徒過・最終期限まで残1日（8/16）｜封鎖169日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月17日 09:04 JST） -->
      ⏳【MOU期限徒過】米・イラン間の60日間停戦・最終合意期限（イスラマバード覚書）が8/16到来も延長合意なし——双方とも延長に言及せず事実上形骸化（共同通信・時事通信）｜🇮🇷 アラグチー外相「米との対話再開はまだ決定していない」（8/15 Telegram投稿）——オマーンとの新航路協議は継続も「政治的解決が前提」｜🇺🇸 トランプ氏はホルムズ海峡「米国領化」路線を維持、ベッセント財務長官は「前例のない」対イラン措置を予告｜🇮🇷 イラン副外相「海峡はイランのものであり、イランのものであり続ける」と応酬｜📊 米シンクタンク分析：迎撃ミサイル備蓄・戦略石油備蓄とも逼迫し対イラン圧力手段は限定的と指摘｜🛢️ ブレント原油は88ドル台後半へ上昇（週初比+1%超）｜🇯🇵 日本関係船は残り4隻で変化なし｜封鎖171日目
<!-- NEW:END -->
<!-- APPLY:END -->

## [S03] 速報インシデント ⚠️（トグルボタン見出し）

**対象：** `<!-- 速報インシデント　トグルボタン -->` 内の見出し・日付バッジ

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">トランプ氏「ホルムズ海峡を米国領に宣言する」発言、イランは「戦略的敗北まで封鎖継続」で応酬——ADNOCタンカー2隻が再被弾</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/15 06:37 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米イラン覚書60日期限が延長合意なく徒過——アラグチー外相「対話再開は未決定」、トランプ氏は「米国領化」路線を維持</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/17 09:04 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S03] 速報インシデント（要約 strong タグ）

**対象：** 折りたたみ本体先頭の要約 `<strong>` タグ

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/15 06:37 速報】UAE外務省は14日、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表し「海賊行為」と非難——負傷者なし、英UKMTOも2隻の軽微損傷を確認、紛争開始来ADNOC関連では15隻目の被弾（AP/Al Jazeera）｜トランプ大統領はロングアイランドの集会で「イランを完全に打ち負かした後、近くホルムズ海峡を米国領と宣言する」と発言——法的根拠・手続きへの言及はなし（Epoch Times）｜イラン副外相ガリババディ氏は「ホルムズ海峡はイランのものであり、米が『戦略的敗北』を受け入れるまで封鎖を継続する」と表明、アラグチー外相も対話再開について「決定はしていない」とし、イスラマバード覚書は「戦争終結」を意味し60日休戦の延長は不要との立場を示した（Iran International/ISNA）｜米はルビオ国務長官がオーストリア外相と会談・ギリシャ外相と電話協議し仲介国を拡大——オーストリアは会談地提供を申し出、カナダは対イラン制裁対象者5名を追加（AP）｜市場ではブレント原油が週央89.53ドルから87ドル台へ反落・IEAは供給不足の拡大に警鐘（Bloomberg）｜日本関係船は残り4隻で変化なし｜封鎖169日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/17 09:04 速報】6月17日署名のイスラマバード覚書が定める60日間の交渉期限が8月16日（月）に到来したが、米・イラン双方とも延長に言及せず事実上形骸化した状態が続いている（共同通信・時事通信）｜イラン・アラグチー外相は15日、Telegramで「米国との対話再開についてはまだ決定していない」と述べる一方、オマーンとの間でホルムズ海峡の新航路策定協議は継続しているとし「政治的解決に至って初めて可能になる」と条件を付けた（Al Jazeera）｜トランプ大統領は「ホルムズ海峡米国領化」路線を崩しておらず、ベッセント財務長官も「イランに対しこれまでにない措置を講じる」と表明（Al Jazeera）｜イラン副外相は「海峡はイランのものであり、イランのものであり、イランのものであり続ける」と応酬（The National）｜米シンクタンク・スティムソン・センターのスラビン氏は、米の迎撃ミサイル備蓄・戦略石油備蓄がいずれも逼迫し空母の長期洋上展開も限界に近いと指摘し「トランプ政権に残る圧力手段は乏しい」と分析（Al Jazeera）｜イラン国会議長ガリバフ氏は15日「軍事的にも政治的にも真に勝利した」と自賛（Al Jazeera）｜ブレント原油は88ドル台後半へ上昇｜日本関係船は残り4隻で変化なし｜封鎖171日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S03] 速報インシデント（新規2件をリスト先頭に追加）

**対象：** `<ul id="incident-list">` 直後（既存リストの先頭）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇦🇪 8/13夜〜14 JST</span>
  <span style="color:#e2e8f0;"> UAE外務省は、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表し「敵対的な攻撃」「海賊行為」と非難する声明を出した。ADNOCは負傷者なし・状況は制御下にあると説明。英UKMTOも2隻が軽微な損傷を負ったと確認したが、ADNOC発表とは別に船名は特定していない。紛争開始（2/28）以降、ADNOC関連船の被弾は今回で15隻目となり、直近1週間だけで3隻目という高頻度が続いている（AP/Al Jazeera）。</span>
</li>
<!-- OLD:END -->
<!-- NEW:START -->
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⏳ 8/16 JST</span>
  <span style="color:#e2e8f0;"> 6月17日にトランプ大統領とペゼシュキアン大統領が署名したイスラマバード覚書が定める60日間の最終合意期限が到来した。共同通信・時事通信によれば、期限は延長可能だが米・イラン双方とも延長に言及しておらず、覚書は事実上形骸化した状態にある。ホルムズ海峡の開放に向けてイランとオマーンが協議を続けるものの正常化には至らず、戦闘でも平和でもない「不安定な膠着状態」が長期化するとの見方が強まっている。トランプ大統領は「米国がホルムズ海峡を完全に支配している」と主張し、イランは「海峡はイランの管理下にある」と反発した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🇮🇷🇴🇲 8/15 JST</span>
  <span style="color:#e2e8f0;"> イラン・アラグチー外相はTelegramへの投稿で「米国との対話再開についてはまだ決定していない」と表明。一方でオマーンとの間でホルムズ海峡の新たな航行ルート策定に向けた協議は継続しているとし、実現には「政治的解決に至ることが前提」と条件を付けた。同日、イラン国会議長ガリバフ氏は「我々は軍事的にも政治的にもこの戦争に真に勝利した」と述べ、覚書で得た譲歩を「誇りと勝利の証」と自賛した（Al Jazeera）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇦🇪 8/13夜〜14 JST</span>
  <span style="color:#e2e8f0;"> UAE外務省は、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表し「敵対的な攻撃」「海賊行為」と非難する声明を出した。ADNOCは負傷者なし・状況は制御下にあると説明。英UKMTOも2隻が軽微な損傷を負ったと確認したが、ADNOC発表とは別に船名は特定していない。紛争開始（2/28）以降、ADNOC関連船の被弾は今回で15隻目となり、直近1週間だけで3隻目という高頻度が続いている（AP/Al Jazeera）。</span>
</li>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S04] 情勢カード① 外交・体制

**対象：** `<!-- カード① 外交・体制 -->` 内の `.s-title` / `.s-body` / `.s-src`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <div class="s-title">🇺🇸 トランプ氏「イラン敗北後、ホルムズ海峡を米国領に宣言する」——イランは「戦略的敗北まで封鎖継続」で応酬</div>
        <div class="s-body">トランプ大統領は14日、ニューヨーク州ロングアイランドでの集会で「イランを完全に打ち負かした後——現に大敗北を喫しつつあるが——近くホルムズ海峡を米国の領土と宣言する」と発言した。米国がどのように海峡の主権を主張するのか、正式な政府提案であるかについては説明しなかったが、国際法上重大な疑問を招く発言となった。同日、イラン副外相カゼム・ガリババディ氏は「ホルムズ海峡はイランのものであり、イランの命令の下でのみ開閉される」と述べ、米国が「戦略的敗北」を受け入れるまで封鎖を継続すると表明。アラグチー外相も、対話再開について「決定はしていない」とし、6月のイスラマバード覚書はあくまで「戦争終結」を意味するものであり60日間の休戦延長は不要との立場を改めて示した。並行してカナダが対イラン制裁対象者を5名追加し、欧州9カ国もEUの人権侵害を理由とした対イラン制裁（6名）に同調するなど、経済的圧力も強まっている。</div>
        <div class="s-src">出典: Epoch Times / Iran International / AP（8/14 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">⏳ 米イラン覚書60日期限、延長合意なく徒過——「戦争終結」か「ただの停戦」か、解釈の相違が浮き彫りに</div>
        <div class="s-body">6月17日にパキスタン仲介でトランプ大統領とペゼシュキアン大統領が署名したイスラマバード覚書は、60日以内の「最終合意」到達を目指す枠組みだったが、その期限が8月16日（月）に到来した。米・イラン双方とも公式には延長を要請しておらず、事実上の形骸化状態にある。覚書は当初、米側がイラン港湾封鎖を30日以内に解除し核合意後にイランへ最低3000億ドル規模の復興支援を行うとした一方、イラン側は機雷除去とホルムズ海峡の60日間無償通航を約束していたが、いずれも履行されていない。イラン側は覚書を「戦争終結」の合意と位置付け60日間の「停戦」延長という概念自体を否定する一方、米側は覚書がイランの度重なる違反により7月7日時点で「終わった」との立場を崩していない。テヘラン応用科学大学のホシュチェシュム教授はAl Jazeeraに対し「米が覚書の条件を履行しなかった時点で停戦は形骸化した」と述べた。</div>
        <div class="s-src">出典: Al Jazeera / 共同通信 / 時事通信（8/16〜17 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S04] 情勢カード② 地域安保・軍事

**対象：** `<!-- カード② 地域安保 -->` 内の `.s-title` / `.s-body` / `.s-src`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <div class="s-title">🇦🇪 ADNOC関連タンカー2隻が再び被弾——紛争開始来15隻目、直近1週間で3隻目の高頻度</div>
        <div class="s-body">UAE外務省は14日、アブダビ国営石油会社（ADNOC）関連のタンカー2隻が13日夜、ホルムズ海峡を通航中にイランのドローン攻撃を受けたと発表し「敵対的なイランの攻撃」「海賊行為」と強く非難した。ADNOCは負傷者がいないこと、状況は制御下にあることを確認。英海軍系のUKMTO（英国海運貿易オペレーション）も2隻が軽微な損傷を負ったとの報告を確認したが、ADNOC発表とは別に船名までは特定していない。UAE外務省は、商船への攻撃や海峡の経済的威圧の手段としての利用は国連安保理決議2817の重大な違反であり、海賊行為に相当すると強調した。ADNOCによれば紛争開始（2/28）以降の被弾は今回で通算15隻目となり、直近1週間だけでも3隻目という高い頻度が続いている。</div>
        <div class="s-src">出典: Al Jazeera / AP / UKMTO（8/14 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">📉 米シンクタンク分析「トランプ政権に残る圧力手段は乏しい」——迎撃ミサイル・戦略石油備蓄とも逼迫</div>
        <div class="s-body">米シンクタンク・スティムソン・センターのバーバラ・スラビン上級研究員はAl Jazeeraの取材に対し、米国が対イラン圧力を追加で強める上での軍事的な選択肢は限られていると分析した。米軍の迎撃ミサイル在庫は開戦以来の消耗で枯渇が進み、戦略石油備蓄も取り崩しが続いており、空母をはじめとする主要艦艇も想定を大幅に超える長期の洋上展開を強いられている。一方でイラン側は、ホルムズ海峡の通航を妨害することで自ら経済的打撃を与える能力を保持し続けており、スラビン氏は「イランはこの局面で強気に出ており、世界経済とトランプ氏を焦らせている」と指摘。今回の紛争は「中間選挙後、投票への影響が小さくなった段階での取引を通じて決着する可能性が高い」との見通しを示した。イラン最高国家安全保障会議トップに就任したレザイー元IRGC司令官の人事も、イランが「優位に立っていると認識している証左」との見方が専門家の間で強まっている。</div>
        <div class="s-src">出典: Al Jazeera（スティムソン・センター分析）（8/16 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S04] 情勢カード③ 日本外交・市場

**対象：** `<!-- カード③ 日本外交・市場 -->` 内の `.s-title` / `.s-body` / `.s-src`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <div class="s-title">🌍 米、仲介国を欧州へ拡大——オーストリア・ギリシャに接触、ブレントは87ドル台で下げ止まり</div>
        <div class="s-body">AP通信によれば、対話が停滞する中、米国務省は伝統的な仲介国（オマーン・パキスタン・トルコ・カタール）に加え、欧州諸国への働きかけを静かに拡大している。ルビオ国務長官は11日、ワシントンでオーストリアのマインライトナー外相と直接会談し、12日にはギリシャのゲラペトリティス外相と電話協議を行った。オーストリア外務省は今後の対イラン協議の会場提供を申し出、「軍事的解決策はあり得ない、外交的解決策こそが優先事項」と強調。ギリシャ外務省も「航行の自由と海洋の安全保障の重要性」を訴えた。一方イラン外務省は、アラグチー外相と欧州各国外相との通話について「ホルムズ海峡の将来的な管理メカニズム」を協議したものと説明しており、双方の受け止め方には差がある。市場では、ブレント原油が週央（12日）に一時89.53ドルまで上昇した後、87ドル台まで反落して推移しており、IEAは2026年の世界的な供給不足幅が過去5年で最大になるとの見通しを示している。</div>
        <div class="s-src">出典: AP / Bloomberg / 外務省・国土交通省（8/11〜14 JST 更新、日本関係船情報は8/15 06:37 JST再確認）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇴🇲 イラン・オマーン、新航路協議は「政治的解決が前提」で継続——原油は膠着観測で88ドル台後半へ</div>
        <div class="s-body">イラン外務省のアラグチー外相は15日、オマーンとの間で進めてきたホルムズ海峡の新たな航行ルート策定協議について「引き続き技術的な議論を続けている」としつつ、実際の運用開始には「まず政治的な解決に至る必要がある」と改めて条件を付けた。8月上旬に地理的座標について暫定合意したとされる南北回廊案は、米・イラン間の政治対立が続く限り実装に至らない見通しである。市場では、米イラン覚書の期限徒過を受けて海峡再開の見通しが一段と後退したとの受け止めから、ブレント原油先物は週明け88ドル台後半（Investing.com時点88.85ドル前後）まで上昇し、WTIも82ドル台へ上げ幅を広げた。IEAは2026年の世界的な供給不足幅が過去5年で最大になるとの見通しを既に示している。日本関係船については、外務省・国土交通省への日英4クエリで新規発表がないことを改めて確認し、残り4隻のまま変化はない。</div>
        <div class="s-src">出典: Al Jazeera / Investing.com / 外務省・国土交通省（8/15〜17 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S05] COUNTDOWN フェーズラベル

**対象：** `#cd-phase-label`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 22「トランプ氏がホルムズ海峡の米国領化を宣言、イランは『戦略的敗北まで封鎖継続』で応酬——ADNOCタンカー2隻が再被弾」——封鎖169日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 23「米イラン覚書60日期限が延長合意なく徒過——アラグチー外相『対話再開は未決定』、トランプ氏は『米国領化』路線を維持」——封鎖171日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S05] COUNTDOWN dl-note（要約・次の焦点・MOU期限注記）

**対象：** `.dl-note`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <div class="dl-note">
        🤝 <strong>トランプ大統領がロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言（8/14）／イラン副外相ガリババディ氏は「米が戦略的敗北を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開を「未決定」とし60日休戦の延長は不要と主張（8/14）／UAE、ADNOC関連タンカー2隻が13日夜の通航中にイランのドローン攻撃で被弾したと発表——紛争開始来15隻目、負傷者なし（8/14）／米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を欧州へ拡大、カナダは対イラン制裁5名を追加（8/11〜14）／ブレント原油は週央89.53ドルから87ドル台へ反落、IEAは供給不足拡大に警鐘／日本関係船は残り4隻で変化なし——封鎖169日目・MOU機雷除去期限（7/17）を未着手のまま徒過</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①トランプ氏の「米国領化」発言が交渉に与える影響 ②イランの「戦略的敗北」要求水準が対話再開の障害となるか ③欧州仲介国拡大（オーストリア・ギリシャ）が突破口となるか ④ADNOCタンカーへの攻撃頻発が主要船社の航行判断にどう影響するか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残1日（8/16）</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🤝 <strong>6月17日署名のイスラマバード覚書が定める60日間の交渉期限が8月16日に到来したが、米・イラン双方とも延長に言及せず事実上形骸化した状態が続いている／アラグチー外相は「米との対話再開はまだ決定していない」と表明する一方、オマーンとの新航路協議は「政治的解決が前提」としつつ継続／トランプ大統領は「ホルムズ海峡米国領化」路線を維持、ベッセント財務長官も「前例のない」対イラン措置を予告／イラン副外相は「海峡はイランのものであり、イランのものであり続ける」と応酬／米シンクタンク・スティムソン・センターは米の迎撃ミサイル・戦略石油備蓄逼迫を指摘し「対イラン圧力手段は乏しい」と分析／ブレント原油は88ドル台後半へ上昇／日本関係船は残り4隻で変化なし——封鎖171日目</strong>
        <br><span style="color:#fde68a;">⚡ 次の24〜48時間の焦点：①米・イランが覚書失効を公式にどう扱うか（新たな枠組み提示の有無） ②イラン・オマーン新航路協議が政治的解決なしに実務合意へ進展するか ③ベッセント財務長官が予告した「前例のない」対イラン措置の内容と時期 ④ブレント原油88ドル台後半からの続伸有無 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU最終期限（8/16）を延長合意なく徒過——事実上の交渉空白期に</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
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
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月17日 09:04 JST 更新</span><br>
  📊 <strong>米イラン覚書60日期限が延長合意なく徒過——アラグチー外相「対話再開は未決定」、トランプ氏は「米国領化」路線を維持：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — 覚書の60日期限が延長合意なく徒過したことで、既存枠組みに基づく履行という選択肢自体が事実上消滅した<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — アラグチー外相の「対話再開は未決定」発言とオマーン新航路協議の継続は、期限徒過後も膠着状態がそのまま持続する構図を裏付ける<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 覚書が定めた最終合意期限そのものが延長合意なく到来・徒過したことは、枠組みの形骸化が制度的に確定した段階に入ったことを意味する<br>
  🅓 全面対決・無期限封鎖 <span style="color:#94a3b8;">→</span> — 米シンクタンクが指摘する米側の圧力手段の乏しさは軍事的な即時エスカレーションの動機を弱める一方、リスクの高止まり自体は変わらない<br>
  <strong style="color:#f87171;">覚書の60日期限が延長合意なく徒過したことで、外交トラックは制度的な後ろ盾を失った状態に入った。イラン側は「対話再開は未決定」としつつオマーンとの実務協議は継続しており、完全な断絶ではないが、膠着の長期化がより確度の高いシナリオとなっている（A↓ B→ C↑ D→）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月17日 09:04 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S07] シナリオA タグ（確率矢印: → から ↓ へ変更）

**対象：** `#sc-tag-A`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S07] シナリオA 本文

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <p>トランプ大統領の「ホルムズ海峡米国領化」発言は、テヘランにとって交渉のインセンティブそのものを損ないかねない発言であり、段階的MOU履行シナリオへの逆風となった。一方で米国が欧州（オーストリア・ギリシャ）への仲介拡大に動いていることは、従来にない新しいチャネルの模索でもある。ただしイラン側が「戦略的敗北」承認を対話再開の前提に据えている以上、両者の隔たりを埋める兆しは乏しい。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>覚書が定めた60日間の交渉期限が延長合意なく8月16日に到来・徒過したことで、既存のイスラマバード覚書に基づく段階的履行という道筋そのものが制度的な後ろ盾を失った。唯一の細い糸は、アラグチー外相が継続を明言したオマーンとの新航路協議だが、本人が「政治的解決が前提」と条件を付けている通り、政治対立が続く限り実務合意には進まない見通しである。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S07] シナリオB 本文

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <p>米国務省がオマーン・パキスタン・トルコ・カタールに加え、オーストリア・ギリシャといった欧州諸国へも接触を広げていることは、伝統的な仲介チャネルが行き詰まっている証左でもある。イラン外務省は欧州各国との通話を「海峡の将来管理メカニズムの協議」と説明する一方、米イラン間の直接対話再開についてアラグチー外相は「未決定」と留保しており、膠着状態が最も蓋然性の高い展開であり続けている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>米シンクタンク・スティムソン・センターの分析が示す通り、米側は迎撃ミサイル・戦略石油備蓄の逼迫により追加の軍事的圧力手段を欠く一方、イラン側も覚書失効後すぐに態度を硬化させる動きは見せておらず、双方が明確な次の一手を欠いたまま様子見を続ける構図が強まっている。アラグチー外相の「対話再開は未決定」という留保付きの発言も、完全な断絶ではなく膠着の持続を示唆する。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S07] シナリオC 本文

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <p>アラグチー外相が6月のイスラマバード覚書を「戦争終結（の合意）」であり「60日間の休戦」ではないと位置付け直したことは、MOU解釈をめぐる米イラン間の食い違いを一段と鮮明にした。トランプ大統領のホルムズ海峡米国領化発言も、既存の国際枠組みを迂回する形での事実上の管理を志向するものであり、両者ともにMOUという公式枠組みの形骸化を後押ししている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イラン国会議長ガリバフ氏が覚書での譲歩獲得を「軍事的にも政治的にも真の勝利」と自賛したことは、テヘランが現状の海峡管理体制を既成事実として固定化させる方向に自信を深めていることを示す。最高国家安全保障会議トップに対米強硬派レザイー元IRGC司令官が就いた人事とも符合し、覚書失効を機にイラン主導の統治枠組みが一段と制度化に向かうリスクが高まっている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S07] シナリオD 本文

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <p>ADNOC関連タンカーへの攻撃が紛争開始来15隻目に達し、直近1週間だけで3隻目という高頻度が続いていることは、海峡の軍事的緊張が沈静化していない実態を示す。トランプ氏の「米国領化」発言とイラン側の「戦略的敗北」要求という、互いに譲歩の余地を残さない強硬なレトリックの応酬が、偶発的エスカレーションのリスクを高めている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>スティムソン・センターのスラビン氏が指摘する通り、米側の軍事的な追加圧力手段は乏しく、直ちに大規模な軍事エスカレーションへ向かう可能性は当面後退している。ただしトランプ氏の「米国領化」路線とベッセント財務長官が予告する「前例のない」対イラン措置の具体的な内容次第では、偶発的な緊張再燃のリスクが依然として残る。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S08] シナリオフッター（次の焦点5点）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">トランプ氏の「米国領化」発言に国際法上・外交上どう反応が広がるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イランの「戦略的敗北」要求が対話再開の前提として維持され続けるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">欧州仲介国拡大（オーストリア・ギリシャ）が新たなチャネルとして機能するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">ADNOCタンカーへの攻撃頻発が主要船社の航行判断にどう影響するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月15日 06:37 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">覚書失効を受け、米・イラン双方が新たな交渉の枠組みを提示するか、それとも無枠組み状態が長期化するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン・オマーン新航路協議が「政治的解決」なしに実務レベルで前進する余地があるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">ベッセント財務長官が予告した「前例のない」対イラン措置の中身と発動時期</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">イラン最高国家安全保障会議（レザイー体制）が覚書失効後にどのような対米方針を打ち出すか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月17日 09:04 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月15日 06:37 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">外交トラックは米が仲介国をオーストリア・ギリシャへ拡大する動きを見せる一方、イラン側はアラグチー外相が対話再開を「未決定」と明言するなど目立った進展がなく、トランプ大統領の「ホルムズ海峡米国領化」発言が緊張を一段と高めている。【北側航路（イラン指定）】直近の公開監視データに大きな更新の報告はなく、高止まりの膠着状態が続いているとみられる。【南ルート（Omani coastal corridor）】8月上旬の航路案合意以降、目立った追加進展の報告はなく、米・イラン間の3者協議は事実上停止したまま。【米の交渉姿勢】トランプ大統領は「イラン敗北後にホルムズ海峡を米国領に宣言する」と発言し、封鎖の既成事実化路線を一段と鮮明にした。【紅海・バブエルマンデブ】直近の大規模攻撃の続報はないが、8/11のフーシ派攻撃による死者発生を受け警戒水準は高いまま。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/15 06:37 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月17日 09:04 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">外交トラックは覚書60日期限が延長合意なく徒過したことで制度的な後ろ盾を失い、イラン側はアラグチー外相が対話再開を「未決定」としつつオマーンとの新航路協議のみ継続と説明している。【北側航路（イラン指定）】直近の公開監視データに大きな更新の報告はなく、高止まりの膠着状態が続いているとみられる。【南ルート（Omani coastal corridor）】新航路の地理的座標は合意済みとされるが、アラグチー外相は運用開始に「政治的解決」を前提条件として付しており、実装は停止したまま。【米の交渉姿勢】トランプ大統領は「ホルムズ海峡米国領化」路線を維持し、ベッセント財務長官も「前例のない」対イラン措置を予告——具体的な発動時期は不明。【紅海・バブエルマンデブ】直近の大規模攻撃の続報はないが、8/11のフーシ派攻撃による死者発生を受け警戒水準は高いまま。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/17 09:04 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S09] 30秒カラム 3行サマリー

**対象：** 「海峡の今」「次の焦点」スパン（「いま何が」直後から）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇺🇸 トランプ氏「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言——イランは「戦略的敗北まで封鎖継続」で応酬。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇦🇪 ADNOC関連タンカー2隻が再びドローン攻撃で被弾（紛争開始来15隻目）。ブレント原油は87ドル台で下げ止まり。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 米が仲介国をオーストリア・ギリシャへ拡大するも対話再開の道筋は立たず、封鎖169日目。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 米イラン覚書60日期限が延長合意なく徒過——アラグチー外相「対話再開は未決定」、トランプ氏は「米国領化」路線を維持。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇴🇲 イラン・オマーン新航路協議は「政治的解決が前提」で継続。ブレント原油は88ドル台後半へ上昇。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📉 米シンクタンクは「米側の対イラン圧力手段は乏しい」と分析——封鎖171日目。
</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S09] 30秒カラム ステータスバッジ5枚

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸トランプ「ホルムズ米国領化」発言</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇦🇪ADNOCタンカー再被弾(15隻目)</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷イラン「戦略的敗北まで封鎖」</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📊ブレント87ドル台で下げ止まり</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⏳MOU60日期限、延長なく徒過</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷アラグチー「対話再開は未決定」</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸トランプ「米国領化」路線維持</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📊ブレント88ドル台後半へ上昇</span>
<!-- NEW:END -->
<!-- APPLY:END -->

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
  "dateModified": "2026-08-15T06:37:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-17T09:04:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

## [C01] SHIP_CONFIG dateConfirmed（日本関係船再確認・変化なし）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
  dateConfirmed: '2026年8月15日 06:37 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近会見（8/4）は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年8月17日 09:04 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近会見（8/4）は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- NEW:END -->
<!-- APPLY:END -->

## [S11] 更新ログ ブロック1（常時表示3件：本日分を追加、旧3件目を除外）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月15日 06:37 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/15 06:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表——紛争開始来15隻目の被弾・負傷者なし（8/14）・トランプ大統領はロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言（8/14）・イラン副外相ガリババディ氏は「米が戦略的敗北を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開「未決定」とし60日休戦の延長は不要と主張（8/14）・米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を欧州へ拡大、カナダは対イラン制裁5名追加（8/11〜14）・ブレント原油は週央89.53ドルから87ドル台へ反落、IEAは供給不足拡大に警鐘・日本関係船は残り4隻で変化なし・封鎖169日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月13日 10:37 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/13 10:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランIRGC上級顧問ナグディ氏がPBSに「トランプ政権終了（2029年）まで戦争を長期化させ消耗戦に持ち込む選択肢がある」と発言（8/12）・フーシ派が紅海バブエルマンデブ海峡でエジプト所有船「ティハマ」を二重攻撃し乗組員4名・救助隊員2名の計6名死亡10名負傷——今次紛争開始後初のフーシ派関連死者（8/11）・米軍ヘリがパナマ籍船「ヴェラ・ノヴァ」に対封鎖破り阻止でヘルファイア2発発射（3週間で3件目の摘発、8/11）・トランプ氏「米国はホルムズを完全支配」と主張も通航量は8/11に週間最低の8隻へ低下・パキスタンが仲介継続——内相がテヘラン訪問中（8/10）・ブレント原油は87.92ドルへ反落（6営業日続伸後、-1.19%）、EIA原油在庫は2023年来最大の週間増（+1740万バレル）・NYダウ53,770ドル(-21.58、3日続落)・日本関係船は残り4隻で変化なし・封鎖167日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月11日 09:26 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/11 09:26</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン最高国家安全保障会議、書記をゾルガドル氏から対米強硬派モフセン・レザイー氏（革命防衛隊元司令官）に交代——ゾルガドル氏はハメネイ師政治顧問に転身（NBC、8/9）・前書記の6条件（脅迫停止・戦争終結・封鎖解除と米軍撤収・戦争賠償・制裁解除・資産凍結解除）は継承・トランプ大統領はイランの賠償要求に「同様の賠償を求める」と反発、USSコール事件等も対象に（Euronews、8/10）・高市首相はオマーンのハイサム国王と電話会談し追加費用のない自由航行の回復を要請（8/10）・フーシ派は紅海の要衝モカを2日連続攻撃し7人死亡・イエメン内戦拡大の懸念（AP）・ブレント原油87.72ドルへ4日続伸(+4.95%)、NYダウ53,975.98ドル(-0.11%)・S&P500は7,753.11ドル(-0.06%)と小反落・日本関係船は残り4隻で変化なし・封鎖165日目・ニュース4件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月17日 09:04 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/17 09:04</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米イラン間の60日間停戦・最終合意期限「イスラマバード覚書」が8月16日に到来し延長合意なく事実上形骸化（共同通信・時事通信）・アラグチー外相「米との対話再開はまだ決定していない」（8/15 Telegram）——オマーンとの新航路協議は継続も「政治的解決が前提」・トランプ大統領は「ホルムズ海峡米国領化」路線を維持、ベッセント財務長官は「前例のない」対イラン措置を予告・イラン副外相「海峡はイランのものであり、イランのものであり続ける」と応酬・米シンクタンク（スティムソン・センター）は米の迎撃ミサイル・戦略石油備蓄逼迫を指摘し「対イラン圧力手段は乏しい」と分析・イラン国会議長ガリバフ氏「軍事的にも政治的にも真に勝利した」（8/15）・ブレント原油88ドル台後半へ上昇・日本関係船は残り4隻で変化なし・封鎖171日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月15日 06:37 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/15 06:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表——紛争開始来15隻目の被弾・負傷者なし（8/14）・トランプ大統領はロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言（8/14）・イラン副外相ガリババディ氏は「米が戦略的敗北を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開「未決定」とし60日休戦の延長は不要と主張（8/14）・米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を欧州へ拡大、カナダは対イラン制裁5名追加（8/11〜14）・ブレント原油は週央89.53ドルから87ドル台へ反落、IEAは供給不足拡大に警鐘・日本関係船は残り4隻で変化なし・封鎖169日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月13日 10:37 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/13 10:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランIRGC上級顧問ナグディ氏がPBSに「トランプ政権終了（2029年）まで戦争を長期化させ消耗戦に持ち込む選択肢がある」と発言（8/12）・フーシ派が紅海バブエルマンデブ海峡でエジプト所有船「ティハマ」を二重攻撃し乗組員4名・救助隊員2名の計6名死亡10名負傷——今次紛争開始後初のフーシ派関連死者（8/11）・米軍ヘリがパナマ籍船「ヴェラ・ノヴァ」に対封鎖破り阻止でヘルファイア2発発射（3週間で3件目の摘発、8/11）・トランプ氏「米国はホルムズを完全支配」と主張も通航量は8/11に週間最低の8隻へ低下・パキスタンが仲介継続——内相がテヘラン訪問中（8/10）・ブレント原油は87.92ドルへ反落（6営業日続伸後、-1.19%）、EIA原油在庫は2023年来最大の週間増（+1740万バレル）・NYダウ53,770ドル(-21.58、3日続落)・日本関係船は残り4隻で変化なし・封鎖167日目・ニュース4件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S11] 更新ログ ブロック2（log-collapse 先頭に旧3件目を挿入）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月11日 09:26 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/11 09:26</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン最高国家安全保障会議、書記をゾルガドル氏から対米強硬派モフセン・レザイー氏（革命防衛隊元司令官）に交代——ゾルガドル氏はハメネイ師政治顧問に転身（NBC、8/9）・前書記の6条件（脅迫停止・戦争終結・封鎖解除と米軍撤収・戦争賠償・制裁解除・資産凍結解除）は継承・トランプ大統領はイランの賠償要求に「同様の賠償を求める」と反発、USSコール事件等も対象に（Euronews、8/10）・高市首相はオマーンのハイサム国王と電話会談し追加費用のない自由航行の回復を要請（8/10）・フーシ派は紅海の要衝モカを2日連続攻撃し7人死亡・イエメン内戦拡大の懸念（AP）・ブレント原油87.72ドルへ4日続伸(+4.95%)、NYダウ53,975.98ドル(-0.11%)・S&P500は7,753.11ドル(-0.06%)と小反落・日本関係船は残り4隻で変化なし・封鎖165日目・ニュース4件更新・osint更新</div>
          <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S11] 更新ログ ブロック3（総件数調整：log-collapse最古の7/26エントリーを削除）

常時表示3件＋log-collapse 9件で合計12件となり上限（11件）を超えるため、最古の7/26エントリーを削除する。削除する本文は下記の通り、`update_log.json` の先頭に追加すること。

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月26日 10:30 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/26 10:30</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態・オマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展（オマーン外交団7/24テヘラン訪問）・IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表・フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明・原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）・米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇・日本関係船は残り4隻で変化なし・封鎖149日目・ニュース3件更新・osint更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- NEW:END -->
<!-- APPLY:END -->

## [S10] news_data.json — updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
"updated": "2026年8月15日 06:37 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
"updated": "2026年8月17日 09:04 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

## [S10] news_data.json — latest 配列（新規3件を先頭に追加、最古3件を archive へ移動）

**方針：** `isLatest: true` は新しい先頭1件のみ。旧6件目までのうち古い3件（irgc-naqdi / houthi-tihamah / us-helicopter）は次のAPPLYブロックで新規archiveバッチへ移動する。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
"latest": [
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
    },
    {
      "id": "latest-irgc-naqdi-prolong-war-0812",
      "title": "IRGC上級顧問「トランプ政権終了まで戦争長期化も選択肢」——テヘランの戦略計算を異例に開示",
      "body": "革命防衛隊（IRGC）司令官の上級顧問モハンマド・レザ・ナグディ将軍は12日、米PBSとのインタビューで、イランが対米戦争をトランプ大統領の任期終了（2029年）まで意図的に長期化させ消耗戦に持ち込む選択肢を検討していると明らかにした。米国の戦略が一貫性を欠くとも批判した。発言は独立検証されたものではないが、イラン側の時間軸認識を示す数少ない公的な手掛かりとなっている。",
      "sourceLabel": "Iran International",
      "date": "2026年8月12日（現地）/ 2026年8月12日 JST",
      "label": "🇮🇷 軍事",
      "url": "https://www.iranintl.com/en/202608124129",
      "isLatest": false
    },
    {
      "id": "latest-houthi-tihamah-doubletap-0811",
      "title": "フーシ派、紅海で今次紛争初の死者——エジプト所有船「ティハマ」二重攻撃で6人死亡",
      "body": "イエメン政府によれば、フーシ派は11日、バブエルマンデブ海峡で食料輸送中のエジプト所有・タンザニア籍貨物船「ティハマ」に弾道ミサイル3発を発射する二重攻撃を実施。乗組員4名（パキスタン人3名・インドネシア人1名）と救助中の国家抵抗軍隊員2名の計6名が死亡、10名が負傷した。2/28の紛争開始以降、フーシ派関連の攻撃による初の確認死者。",
      "sourceLabel": "PBS News",
      "date": "2026年8月11日（現地）/ 2026年8月11日 JST",
      "label": "🐹 軍事",
      "url": "https://www.pbs.org/newshour/amp/world/iranian-backed-houthis-kill-6-in-attack-on-vessel-and-other-developments-in-the-mideast",
      "isLatest": false
    },
    {
      "id": "latest-us-helicopter-velanova-strike-0811",
      "title": "米軍ヘリ、封鎖破り試みたパナマ籍船「ヴェラ・ノヴァ」にヘルファイア発射——3週間で3件目の摘発",
      "body": "米中央軍は、対イラン港湾封鎖の突破を試みたとするパナマ籍コンテナ船「ヴェラ・ノヴァ」（オマーン湾）に海軍ヘリコプターがヘルファイア・ミサイル2発を発射したと発表。船体火災は鎮火し乗組員17名全員の無事を確認。7/15のBELMA号・7/24のM/T LAVINE号に続き、3週間で3件目の摘発となった。",
      "sourceLabel": "Fox News",
      "date": "2026年8月11日（現地）/ 2026年8月12日 JST",
      "label": "⚓ 軍事",
      "url": "https://www.foxnews.com/live-news/iran-war-news-trump-israel-hormuz-august-12",
      "isLatest": false
    }
  ],
  <!-- OLD:END -->
<!-- NEW:START -->
"latest": [
    {
      "id": "latest-mou-deadline-expires-stalemate-0816",
      "title": "米イラン覚書60日期限、延長合意なく到来——「不安定な膠着」長期化の観測強まる",
      "body": "米国とイランは16日、戦闘終結に向けた最終合意の交渉期限とされたイスラマバード覚書の60日期限を迎えた。期限は延長可能だが双方とも延長に言及せず、覚書は事実上形骸化。ホルムズ海峡の開放に向けてイランとオマーンが協議を続けるが正常化には至らず、戦闘でも平和でもない「不安定な膠着状態」の長期化が懸念されている。",
      "sourceLabel": "共同通信",
      "date": "2026年8月16日（現地）/ 2026年8月16日 JST",
      "label": "⏳ 外交",
      "url": "https://news.yahoo.co.jp/articles/c180d898d2b9321ba1560f65adc67dd5b988c589",
      "isLatest": true
    },
    {
      "id": "latest-trump-iran-hormuz-territory-rebuttal-0816",
      "title": "トランプ氏「間もなく米国領に」に応酬、イラン副外相「海峡はイランのものであり続ける」",
      "body": "米・イラン覚書の期限失効を受け、トランプ大統領は改めてホルムズ海峡の米国領化路線に言及、イラン副外相は「海峡はイランのものであり、イランのものであり、イランのものであり続ける」と真っ向から反論した。両国が海峡の実効支配を各々主張し、経済的圧力による揺さぶり合いが続いている。",
      "sourceLabel": "The National",
      "date": "2026年8月16日（現地）/ 2026年8月16日 JST",
      "label": "🇺🇸 外交",
      "url": "https://www.thenationalnews.com/news/us/2026/08/16/deadline-for-us-iran-agreement-expires-with-stalemate-set-to-continue/",
      "isLatest": false
    },
    {
      "id": "latest-oil-brent-rally-deadlock-0817",
      "title": "ブレント原油88ドル台後半へ上昇——覚書失効を受け海峡再開観測が一段と後退",
      "body": "米イラン覚書の期限失効を受け、ホルムズ海峡再開の見通しが一段と後退したとの見方から、ブレント原油先物は週明け88ドル台後半まで上昇、WTIも82ドル台へ上げ幅を広げた。IEAは2026年の世界的な供給不足幅が過去5年で最大になるとの見通しを既に示している。",
      "sourceLabel": "Investing.com",
      "date": "2026年8月17日 JST",
      "label": "🛢️ 市場",
      "url": "https://www.investing.com/commodities/brent-oil",
      "isLatest": false
    },
    {
      "id": "latest-adnoc-tankers-drone-attack-0813",
      "title": "ADNOC関連タンカー2隻が再び被弾——ホルムズ海峡通航中にイランのドローン攻撃、紛争開始来15隻目",
      "body": "UAE外務省は14日、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表し「海賊行為」と非難した。負傷者はなく状況は制御下にあるという。英UKMTOも2隻が軽微な損傷を受けたと確認。ADNOC関連船が被弾するのは紛争開始来15隻目となる。",
      "sourceLabel": "AP",
      "date": "2026年8月13日（現地）/ 2026年8月14日 JST",
      "label": "🇦🇪 軍事",
      "url": "https://www.usnews.com/news/world/articles/2026-08-14/2-uae-tankers-attacked-while-transiting-strait-of-hormuz-and-other-news-from-the-middle-east",
      "isLatest": false
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
  ],
  <!-- NEW:END -->
<!-- APPLY:END -->

## [S10] news_data.json — archive 配列（新規バッチ挿入：旧latestの最古3件を格納）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
"archive": [
    {
      "batchLabel": "2026年8月中旬（8/9〜8/12）",<!-- OLD:END -->
<!-- NEW:START -->
"archive": [
    {
      "batchLabel": "2026年8月中旬（8/11〜8/12）",
      "items": [
        {
          "id": "latest-irgc-naqdi-prolong-war-0812",
          "title": "IRGC上級顧問「トランプ政権終了まで戦争長期化も選択肢」——テヘランの戦略計算を異例に開示",
          "body": "革命防衛隊（IRGC）司令官の上級顧問モハンマド・レザ・ナグディ将軍は12日、米PBSとのインタビューで、イランが対米戦争をトランプ大統領の任期終了（2029年）まで意図的に長期化させ消耗戦に持ち込む選択肢を検討していると明らかにした。米国の戦略が一貫性を欠くとも批判した。発言は独立検証されたものではないが、イラン側の時間軸認識を示す数少ない公的な手掛かりとなっている。",
          "sourceLabel": "Iran International",
          "date": "2026年8月12日（現地）/ 2026年8月12日 JST",
          "label": "🇮🇷 軍事",
          "url": "https://www.iranintl.com/en/202608124129",
          "isLatest": false
        },
        {
          "id": "latest-houthi-tihamah-doubletap-0811",
          "title": "フーシ派、紅海で今次紛争初の死者——エジプト所有船「ティハマ」二重攻撃で6人死亡",
          "body": "イエメン政府によれば、フーシ派は11日、バブエルマンデブ海峡で食料輸送中のエジプト所有・タンザニア籍貨物船「ティハマ」に弾道ミサイル3発を発射する二重攻撃を実施。乗組員4名（パキスタン人3名・インドネシア人1名）と救助中の国家抵抗軍隊員2名の計6名が死亡、10名が負傷した。2/28の紛争開始以降、フーシ派関連の攻撃による初の確認死者。",
          "sourceLabel": "PBS News",
          "date": "2026年8月11日（現地）/ 2026年8月11日 JST",
          "label": "🐹 軍事",
          "url": "https://www.pbs.org/newshour/amp/world/iranian-backed-houthis-kill-6-in-attack-on-vessel-and-other-developments-in-the-mideast",
          "isLatest": false
        },
        {
          "id": "latest-us-helicopter-velanova-strike-0811",
          "title": "米軍ヘリ、封鎖破り試みたパナマ籍船「ヴェラ・ノヴァ」にヘルファイア発射——3週間で3件目の摘発",
          "body": "米中央軍は、対イラン港湾封鎖の突破を試みたとするパナマ籍コンテナ船「ヴェラ・ノヴァ」（オマーン湾）に海軍ヘリコプターがヘルファイア・ミサイル2発を発射したと発表。船体火災は鎮火し乗組員17名全員の無事を確認。7/15のBELMA号・7/24のM/T LAVINE号に続き、3週間で3件目の摘発となった。",
          "sourceLabel": "Fox News",
          "date": "2026年8月11日（現地）/ 2026年8月12日 JST",
          "label": "⚓ 軍事",
          "url": "https://www.foxnews.com/live-news/iran-war-news-trump-israel-hormuz-august-12",
          "isLatest": false
        }
      ]
    },
    {
      "batchLabel": "2026年8月中旬（8/9〜8/12）",<!-- NEW:END -->
<!-- APPLY:END -->

## [S10] news_data.json — osint 配列（新規1件を先頭に追加、既存記事は isLatest: false へ）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
"osint": [
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
    },<!-- OLD:END -->
<!-- NEW:START -->
"osint": [
    {
      "id": "osint-mou-expires-what-to-know-0816",
      "date": "2026年8月16日（現地）/ 2026年8月16日 JST",
      "titleJa": "米イラン覚書、期限失効へ——何が起き、何が起きなかったのか",
      "titleEn": "US-Iran MoU is set to expire: What to know",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/2026/8/16/us-iran-mou-is-set-to-expire-what-to-know",
      "isLatest": true
    },
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
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [ARCHIVE] docs/data/archive_timeline.json への追記（Claude Code手動str_replace対象）

`docs/data/archive_timeline.json` の `entries` 配列末尾に、以下のエントリーを追加してください（既存エントリーは変更しないこと）。

```json
{
  "date": "2026-08-17",
  "dateLabel": "2026/08/17 09:04",
  "blockadeDay": 171,
  "summary": "米イラン間の60日間停戦・最終合意期限「イスラマバード覚書」が8月16日に到来し延長合意なく事実上形骸化（共同通信・時事通信）・アラグチー外相「米との対話再開はまだ決定していない」（8/15 Telegram）——オマーンとの新航路協議は継続も「政治的解決が前提」・トランプ大統領は「ホルムズ海峡米国領化」路線を維持、ベッセント財務長官は「前例のない」対イラン措置を予告・イラン副外相「海峡はイランのものであり、イランのものであり続ける」と応酬・米シンクタンク（スティムソン・センター）は米の迎撃ミサイル・戦略石油備蓄逼迫を指摘し「対イラン圧力手段は乏しい」と分析・イラン国会議長ガリバフ氏「軍事的にも政治的にも真に勝利した」（8/15）・ブレント原油88ドル台後半へ上昇・日本関係船は残り4隻で変化なし・封鎖171日目・ニュース3件更新・osint更新",
  "relatedNews": [
    {
      "title": "米イラン「不安定な膠着」 覚書期限、海峡開放見えず",
      "url": "https://news.yahoo.co.jp/articles/c180d898d2b9321ba1560f65adc67dd5b988c589",
      "sourceLabel": "共同通信"
    },
    {
      "title": "米イラン合意期限が失効——「イランのものだ」海峡巡り対立続く",
      "url": "https://www.thenationalnews.com/news/us/2026/08/16/deadline-for-us-iran-agreement-expires-with-stalemate-set-to-continue/",
      "sourceLabel": "The National"
    },
    {
      "title": "ブレント原油88ドル台後半へ上昇——覚書失効を受け海峡再開観測が一段と後退",
      "url": "https://www.investing.com/commodities/brent-oil",
      "sourceLabel": "Investing.com"
    }
  ]
}
```

---

## ✅ 出力前セルフチェック（本日のセルフチェック項目数：19件）

```
[✓] Step 0 project_knowledge_search 2クエリ実施・baseline確認（8/15 06:37 JST・封鎖169日目）
[✓] C01タンカー確認：日本語3クエリ＋英語1クエリ全実施・変化なし・残り4隻
[✓] S01 ヘッダー ― 2026年8月17日 09:04 JST・封鎖171日目 ✓
[✓] S02 TICKER ― MOU期限徒過・アラグチー未決定・トランプ米国領化・イラン副外相応酬・封鎖171日目 ✓
[✓] S03 速報インシデント ― 8/17 09:04付け・トグル見出し／ffcccc要約／li2件（8/16, 8/15）を新規追加 ✓
[✓] S04 情勢カード3枚 ― 全カードを本日情勢に更新（重複表現を避け各カードで異なる切り口：①経緯解説 ②軍事力学分析 ③航路・市場）✓
[✓] S05 COUNTDOWN ― Phase23・封鎖171日目・MOU期限「延長合意なく徒過」に更新 ✓
[✓] S06 シナリオ確率補足バナー ― 8/17 09:04 JST日付更新・A↓ B→ C↑ D→（矢印はダッシュボード自動同期のため数値は非記載）✓
[✓] S07 シナリオ4本 ― A/B/C/D本文を本日情勢に更新（S06と異なる切り口で記述）・sc-tag-Aの矢印を→から↓へ更新 ✓
[✓] S08 シナリオフッター ― 次の焦点5点を本日版に更新（S05のdl-noteと重複しない中長期視点で記述）✓
[✓] S08.5 全ルート現況サマリー ― 8/17 09:04 JST更新・S08.5固有の切り口（航路別）で記述 ✓
[✓] S09 30秒カラム ― 3行サマリー＋バッジ5枚を最後に更新 ✓
[✓] S10 news_data.json ― latest 3件追加（3件をarchiveへ新規バッチ移動）・osint 1件追加・updated日付 ✓
[✓] S11 更新ログ ― 2ブロック構成（常時表示3件固定＋log-collapse先頭挿入）＋総件数調整（7/26最古エントリー削除）✓
[✓] C01 SHIP_CONFIG dateConfirmed ― 8/17 09:04 JST・変化なし ✓
[✓] JSON-LD dateModified ― 2026-08-17T09:04:00+09:00 ✓
[✓] archive_timeline.json ― 2026-08-17エントリー追加（Claude Code手動str_replace対象）✓
[✓] Python OLD-block一意性検証 ― 全29 APPLYブロックでcount==1を確認済み ✓
[✓] 各セクションの文章重複チェック ― S01(総合要約)/S02(箇条書き)/S03(時系列+背景)/S04①(経緯解説)②(軍事分析)③(航路市場)/S05(直近48h焦点)/S06(シナリオ別影響)/S07(シナリオ別深掘り)/S08(中長期焦点)/S08.5(航路別)/S09(最圧縮3行+バッジ)で表現・切り口をそれぞれ変えて記述 ✓

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記は変更なし（S05 dl-box内の枠組みは不変）✓
TICKER内JST表記チェック：全日付にJST付き ✓
Al Jazeera使用箇所チェック：📰関連最新ニュース(latest)には不使用、osintのみ使用（新規追加のMOU期限解説記事もosintに配置）✓
人名表記チェック：習近平の言及なし（該当なし）／トランプ・アラグチー・ガリババディ・ガリバフ・レザイー等は日本語カタカナ表記で統一 ✓
URL捏造チェック：全URLはweb_search／web_fetch結果から取得した実在URLのみ使用（共同通信・The National・Investing.com・Al Jazeeraいずれも確認済み）✓
禁止ソースチェック：毎日新聞・Wikipedia・TBS・朝日新聞・NHK・東京新聞・テレビ朝日は不使用 ✓
```
