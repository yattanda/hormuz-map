# index_html_diffs.md — 2026年8月19日 08:51 JST 更新分

> Claude Code への指示：以下の差分を docs/index.html および docs/data/news_data.json に適用してください。
> 変更箇所以外は絶対に触らないこと。
> docs/data/archive_timeline.json への追記は [ARCHIVE] セクションに個別記載（apply_diffs.pyの対象外のため、str_replaceで手動適用してください）。
> ⚠️ [S07] シナリオDタグ の項目のみ old_str 未検証のため、適用前に `grep -n "sc-tag-D"` で現況を確認してから str_replace してください（詳細は該当セクション参照）。
> ⚠️ [S11] ブロック3（総件数調整）も、log-collapse内の現況確認が必要なため `view` で件数を数えたうえで適用してください。

---

## Step 0 セルフチェック（本文執筆前の事前確認）

project_knowledge_search にて「index_html_diffs.md 最新 更新 JST」「更新ログ 出典 JST 更新」を実行し、直近の確定更新が2026年8月17日 09:04 JST（封鎖171日目）であることを確認。raw.githubusercontent.com から docs/tools/index_html_diffs.md を直接取得し、8/17 09:04 JST時点の内容（覚書60日期限が延長合意なく徒過・アラグチー「対話再開は未決定」・トランプ「米国領化」路線維持）と完全一致することを確認した。

C01タンカー確認：日本語3クエリ（「日本関係船舶 ホルムズ海峡 通過 足止め 8月」「外務省 ホルムズ海峡 日本関係船舶 8月19日」「金子国土交通大臣 会見 ホルムズ海峡 8月」）＋英語1クエリ（「Japanese ships Strait of Hormuz stranded detained August 2026」）全て実施。外務省・国交省ともに8/4会見（熊本地震対応が主題でホルムズ言及なし）以降の新規発表なしを確認。変化なし・残り4隻のまま。

封鎖日数：Day1=2026年2月28日起算で2026年8月19日はDay173（8/17のDay171から+2）。

**本日の最重要事案：** トランプ大統領は17日、Fox Newsのトレイ・イングスト記者との電話取材で、イランとオマーンが進めるホルムズ海峡の航路管理協議について「オマーンが邪魔をするなら、地獄まで爆撃してやる（bomb the s--- out of them）」と発言し、5月の「痛い目に遭わせる」発言に続き2度目となるオマーンへの軍事威嚇を行った（Washington Post・NBC News・CNN）。同日トランプ氏は、クルディスタン地域政府のバルザニ議長を仲介役としてイラン革命防衛隊（IRGC）と直接の裏チャンネルを持っていることも認めたが（Axios・Fox News）、IRGC報道官モヘッビ准将は「完全な虚偽」と全面否定した（Tasnim通信）。米上院ではケイン議員（民主）が、大統領によるオマーンへの武力行使を禁じる決議案の提出を表明。一方、ホルムズ海峡では18日未明（UTC 01:35）、オマーン方面へ出航中の船舶が「未確認の飛翔体」により機関室を損傷し乗組員1名が負傷する事案が発生（UKMTO・Reuters・Al Jazeera）。イラン国会議長ガリバフ氏は18日、米国が覚書上の義務（資産凍結解除・制裁解除・海上封鎖解除）を履行するまで封鎖は解除しないと改めて表明した。

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米・イラン間の60日間停戦・最終合意期限「イスラマバード覚書」が8月16日に到来し、双方とも延長に言及しないまま事実上形骸化——共同通信・時事通信は「不安定な膠着状態」の長期化を報道／イラン・アラグチー外相は15日「米国との対話再開はまだ決定していない」と表明する一方、オマーンとの新航路協議は「政治的解決が前提」としつつ継続の姿勢／トランプ大統領は「ホルムズ海峡米国領化」路線を崩さず、ベッセント財務長官も「前例のない」対イラン措置を予告／イラン副外相は「海峡はイランのものであり、イランのものであり続ける」と応酬／米シンクタンク専門家は迎撃ミサイル備蓄・戦略石油備蓄の逼迫を指摘し「トランプ政権に残る圧力手段は乏しい」と分析／ブレント原油は88ドル台後半へ上昇（週初比+1%超）／日本関係船は残り4隻で変化なし／封鎖171日目）</span>
    <span class="badge-item badge-date">📅2026年8月17日 09:04 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（トランプ大統領がイラン・オマーンのホルムズ海峡航路協議を巡り「オマーンが邪魔をするなら地獄まで爆撃する」と2度目の軍事威嚇——米上院ケイン議員は大統領の対オマーン武力行使を禁じる決議案提出を表明／トランプ氏はクルディスタン地域政府バルザニ議長を介したIRGCとの直接裏チャンネルの存在を認めたが、IRGC報道官は「完全な虚偽」と全面否定／18日未明、オマーン方面へ出航中の船舶が未確認の飛翔体で機関室を損傷し乗組員1名負傷——UKMTOが調査中／イラン国会議長ガリバフ氏は資産凍結解除・制裁解除・海上封鎖解除という覚書上の米側義務履行まで封鎖解除せずと改めて表明／イラン・オマーンは新航路の地図について「了解」に達したとイラン外務省報道官バガイ氏が発表も、包括合意・共同声明は依然調整中／ブレント原油は90ドル台後半へ上昇（8/18時点90.97ドル）／サウジ・アラムコはUAEフジャイラ沖でのシップ・トゥ・シップ移送により原油出荷を再開／日本関係船は残り4隻で変化なし／封鎖173日目）</span>
    <span class="badge-item badge-date">📅2026年8月19日 08:51 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年8月17日 09:04 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月17日 09:04 JST） -->
      ⏳【MOU期限徒過】米・イラン間の60日間停戦・最終合意期限（イスラマバード覚書）が8/16到来も延長合意なし——双方とも延長に言及せず事実上形骸化（共同通信・時事通信）｜🇮🇷 アラグチー外相「米との対話再開はまだ決定していない」（8/15 Telegram投稿）——オマーンとの新航路協議は継続も「政治的解決が前提」｜🇺🇸 トランプ氏はホルムズ海峡「米国領化」路線を維持、ベッセント財務長官は「前例のない」対イラン措置を予告｜🇮🇷 イラン副外相「海峡はイランのものであり、イランのものであり続ける」と応酬｜📊 米シンクタンク分析：迎撃ミサイル備蓄・戦略石油備蓄とも逼迫し対イラン圧力手段は限定的と指摘｜🛢️ ブレント原油は88ドル台後半へ上昇（週初比+1%超）｜🇯🇵 日本関係船は残り4隻で変化なし｜封鎖171日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月19日 08:51 JST） -->
      💣【オマーン再威嚇】トランプ氏「オマーンが邪魔なら地獄まで爆撃する」——ホルムズ航路協議を巡り2度目の軍事威嚇、米上院ケイン議員は武力行使禁止決議案の提出を表明｜🤝 トランプ氏、クルディスタン地域政府バルザニ議長経由のIRGC直接裏チャンネルの存在を認める——IRGC報道官は「完全な虚偽」と全面否定｜🚢 18日未明、オマーン方面へ出航中の船舶が未確認飛翔体で被弾——機関室損傷・乗組員1名負傷、UKMTO調査中｜🇮🇷 ガリバフ国会議長「米国が覚書義務（資産凍結解除・制裁解除・海上封鎖解除）を履行するまで封鎖継続」｜🇮🇷🇴🇲 イラン・オマーン、新航路地図に「了解」——包括合意・共同声明は調整中（イラン外務省バガイ報道官）｜🛢️ ブレント原油90ドル台後半へ上昇（8/18時点90.97ドル）・サウジアラムコはフジャイラ沖STS移送で出荷再開｜🇯🇵 日本関係船は残り4隻で変化なし｜封鎖173日目
<!-- NEW:END -->
<!-- APPLY:END -->

## [S03] 速報インシデント ⚠️（トグルボタン見出し）

**対象：** `<!-- 速報インシデント　トグルボタン -->` 内の見出し・日付バッジ

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米イラン覚書60日期限が延長合意なく徒過——アラグチー外相「対話再開は未決定」、トランプ氏は「米国領化」路線を維持</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/17 09:04 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">トランプ氏「オマーンが邪魔なら爆撃する」と2度目の威嚇——船舶が未確認飛翔体で被弾、乗組員1名負傷</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/19 08:51 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S03] 速報インシデント（要約 strong タグ）

**対象：** 折りたたみ本体先頭の要約 `<strong>` タグ

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/17 09:04 速報】6月17日署名のイスラマバード覚書が定める60日間の交渉期限が8月16日（月）に到来したが、米・イラン双方とも延長に言及せず事実上形骸化した状態が続いている（共同通信・時事通信）｜イラン・アラグチー外相は15日、Telegramで「米国との対話再開についてはまだ決定していない」と述べる一方、オマーンとの間でホルムズ海峡の新航路策定協議は継続しているとし「政治的解決に至って初めて可能になる」と条件を付けた（Al Jazeera）｜トランプ大統領は「ホルムズ海峡米国領化」路線を崩しておらず、ベッセント財務長官も「イランに対しこれまでにない措置を講じる」と表明（Al Jazeera）｜イラン副外相は「海峡はイランのものであり、イランのものであり、イランのものであり続ける」と応酬（The National）｜米シンクタンク・スティムソン・センターのスラビン氏は、米の迎撃ミサイル備蓄・戦略石油備蓄がいずれも逼迫し空母の長期洋上展開も限界に近いと指摘し「トランプ政権に残る圧力手段は乏しい」と分析（Al Jazeera）｜イラン国会議長ガリバフ氏は15日「軍事的にも政治的にも真に勝利した」と自賛（Al Jazeera）｜ブレント原油は88ドル台後半へ上昇｜日本関係船は残り4隻で変化なし｜封鎖171日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/19 08:51 速報】トランプ大統領は17日、Fox Newsのトレイ・イングスト記者との電話取材で、イラン・オマーン間のホルムズ海峡航路管理協議を巡り「オマーンが邪魔をするなら地獄まで爆撃してやる」と発言——5月の「痛い目に遭わせる」発言に続き2度目のオマーンへの軍事威嚇となった（Washington Post/NBC News）｜同日トランプ氏は、クルディスタン地域政府バルザニ議長を仲介役とするIRGCとの直接裏チャンネルの存在を認めたが（Axios）、IRGC報道官モヘッビ准将は「完全な虚偽」であり米側との対話は一切行われていないと全面否定（Tasnim通信）｜米上院ではケイン議員（民主）が、議会承認なきオマーンへの武力行使を禁じる決議案を上院再開後に提出する方針を表明｜18日未明（UTC 01:35）、オマーン方面へ出航中の船舶が未確認の飛翔体により機関室を損傷し乗組員1名が負傷——残る乗組員はオマーン沿岸警備隊が支援、UKMTOが調査中で環境影響の報告はなし（Reuters/Al Jazeera）｜イラン国会議長ガリバフ氏は18日、資産凍結解除・石油ガス制裁解除・海上封鎖解除という覚書上の米側義務が履行されるまで封鎖は解除しないと改めて表明｜イラン外務省バガイ報道官は、オマーンとの新航路地図について「了解」に達したとしつつ、包括合意・共同声明の取りまとめにはなお時間を要すると説明｜ブレント原油は90ドル台後半へ上昇（8/18時点90.97ドル）、サウジアラムコはUAEフジャイラ沖でのシップ・トゥ・シップ移送により重質原油の出荷を再開｜日本関係船は残り4隻で変化なし｜封鎖173日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S03] 速報インシデント（新規2件をリスト先頭に追加）

**対象：** `<ul id="incident-list">` 直後（既存リストの先頭）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⏳ 8/16 JST</span>
  <span style="color:#e2e8f0;"> 6月17日にトランプ大統領とペゼシュキアン大統領が署名したイスラマバード覚書が定める60日間の最終合意期限が到来した。共同通信・時事通信によれば、期限は延長可能だが米・イラン双方とも延長に言及しておらず、覚書は事実上形骸化した状態にある。ホルムズ海峡の開放に向けてイランとオマーンが協議を続けるものの正常化には至らず、戦闘でも平和でもない「不安定な膠着状態」が長期化するとの見方が強まっている。トランプ大統領は「米国がホルムズ海峡を完全に支配している」と主張し、イランは「海峡はイランの管理下にある」と反発した。</span>
</li>
<!-- OLD:END -->
<!-- NEW:START -->
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">💣 8/17 JST</span>
  <span style="color:#e2e8f0;"> トランプ大統領はFox Newsのトレイ・イングスト記者との電話取材で、イランとオマーンが進めるホルムズ海峡の航路管理協議について「オマーンが邪魔をするなら、地獄まで爆撃してやる」と発言した。5月の閣議で「オマーンは他国同様に振る舞うべきだ、さもなくば吹き飛ばすことになる」と述べて以来、2度目となるオマーンへの軍事威嚇。米上院のティム・ケイン議員（民主・バージニア州）は同日、議会再開後にオマーンへの武力行使を禁じる決議案を提出する方針を表明した。同日トランプ氏はFox Newsに対し、クルディスタン地域政府のネチルヴァン・バルザニ議長を仲介役としてイラン革命防衛隊（IRGC）と直接の裏チャンネルを持っていると認めたが、IRGC報道官モヘッビ准将はタスニム通信に対し「完全な虚偽であり、米側とのいかなる対話も行われていない」と全面否定した（Axios/Fox News/Washington Post）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🚢 8/18 JST</span>
  <span style="color:#e2e8f0;"> 英海運当局UKMTOは18日未明（協定世界時1時35分）、オマーン方面へ出航中の船舶が未確認の飛翔体により被弾したとの報告を受けたと発表した。機関室に損傷が生じ乗組員1名が負傷、残る乗組員はオマーン沿岸警備隊の支援を受けているという。環境影響の報告はなく、当局が調査を進めている。ホルムズ海峡の1日あたり通航隻数は開戦前の130隻超から1桁台まで落ち込んだ状態が続いており、今回の事案は米・イラン交渉が停滞するなかでの発生となった（Reuters/Al Jazeera）。</span>
</li>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S04] 情勢カード① 外交・体制

**対象：** `<!-- カード① 外交・体制 -->` 内の `.s-title` / `.s-body` / `.s-src`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <div class="s-title">⏳ 米イラン覚書60日期限、延長合意なく徒過——「戦争終結」か「ただの停戦」か、解釈の相違が浮き彫りに</div>
        <div class="s-body">6月17日にパキスタン仲介でトランプ大統領とペゼシュキアン大統領が署名したイスラマバード覚書は、60日以内の「最終合意」到達を目指す枠組みだったが、その期限が8月16日（月）に到来した。米・イラン双方とも公式には延長を要請しておらず、事実上の形骸化状態にある。覚書は当初、米側がイラン港湾封鎖を30日以内に解除し核合意後にイランへ最低3000億ドル規模の復興支援を行うとした一方、イラン側は機雷除去とホルムズ海峡の60日間無償通航を約束していたが、いずれも履行されていない。イラン側は覚書を「戦争終結」の合意と位置付け60日間の「停戦」延長という概念自体を否定する一方、米側は覚書がイランの度重なる違反により7月7日時点で「終わった」との立場を崩していない。テヘラン応用科学大学のホシュチェシュム教授はAl Jazeeraに対し「米が覚書の条件を履行しなかった時点で停戦は形骸化した」と述べた。</div>
        <div class="s-src">出典: Al Jazeera / 共同通信 / 時事通信（8/16〜17 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">💣 トランプ氏、オマーンへ2度目の軍事威嚇——IRGCとの「裏チャンネル」表明は本人発表・イラン側は即座に全面否定</div>
        <div class="s-body">トランプ大統領は17日、Fox Newsの電話取材で、イラン・オマーン間のホルムズ海峡航路協議について「オマーンが邪魔をするなら地獄まで爆撃してやる」と発言した。オマーンへの軍事威嚇は5月の閣議での「吹き飛ばす」発言に続き2度目であり、米国の同盟国に対する異例の恫喝として波紋を広げている。米上院のティム・ケイン議員（民主）はこれを受け、大統領による対オマーン武力行使を議会承認なしに禁じる決議案の提出を表明し、「暴走する権力に酔った大統領を止める」と述べた。同じ取材でトランプ氏は、クルディスタン地域政府のバルザニ議長を介してIRGC幹部と直接連絡を取っていると認め「彼らはポーカーは上手いが死にかけている」と述べたが、IRGC報道官モヘッビ准将は「純然たる虚偽」と即座に否定し、外交はイラン外務省の所管であって軍が独自に対米対話を行うことはないと強調した。この情報戦の応酬自体が、米・イラン双方とも公式な対話ルートを持たないまま6か月目に入った交渉の実態を映し出している。</div>
        <div class="s-src">出典: Washington Post / Axios / Fox News / NBC News（8/17〜18 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S04] 情勢カード② 地域安保・軍事

**対象：** `<!-- カード② 地域安保 -->` 内の `.s-title` / `.s-body` / `.s-src`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <div class="s-title">📉 米シンクタンク分析「トランプ政権に残る圧力手段は乏しい」——迎撃ミサイル・戦略石油備蓄とも逼迫</div>
        <div class="s-body">米シンクタンク・スティムソン・センターのバーバラ・スラビン上級研究員はAl Jazeeraの取材に対し、米国が対イラン圧力を追加で強める上での軍事的な選択肢は限られていると分析した。米軍の迎撃ミサイル在庫は開戦以来の消耗で枯渇が進み、戦略石油備蓄も取り崩しが続いており、空母をはじめとする主要艦艇も想定を大幅に超える長期の洋上展開を強いられている。一方でイラン側は、ホルムズ海峡の通航を妨害することで自ら経済的打撃を与える能力を保持し続けており、スラビン氏は「イランはこの局面で強気に出ており、世界経済とトランプ氏を焦らせている」と指摘。今回の紛争は「中間選挙後、投票への影響が小さくなった段階での取引を通じて決着する可能性が高い」との見通しを示した。イラン最高国家安全保障会議トップに就任したレザイー元IRGC司令官の人事も、イランが「優位に立っていると認識している証左」との見方が専門家の間で強まっている。</div>
        <div class="s-src">出典: Al Jazeera（スティムソン・センター分析）（8/16 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🚢 船舶が未確認飛翔体で被弾、乗組員1名負傷——通航隻数は依然1桁台、フーシ派はサウジ製油所への攻撃継続</div>
        <div class="s-body">英海運当局UKMTOは18日未明（協定世界時1時35分）、オマーン方面へ出航中の船舶が未確認の飛翔体により被弾したとの報告を受けたと発表した。機関室が損傷し乗組員1名が負傷、残る乗組員はオマーン沿岸警備隊の支援を受けている。環境影響の報告はなく、犯行主体を含め当局が調査を進めている。ホルムズ海峡の1日あたり通航隻数は開戦前の130隻超から1桁台まで落ち込んだ状態が続いており、月曜（17日）時点でも週末からわずかに持ち直したのみの低水準にとどまる。並行して紅海方面では、イエメンのフーシ派が18日、サウジアラビア国営石油会社アラムコのジザン製油所をドローンで攻撃したとフーシ派系メディア・サバ通信が報じた。フーシ派は7月以降、サウジの石油インフラや船舶への攻撃を継続的に行っており、ホルムズ海峡とは別の第二の紛争前線として緊張が高止まりしている。</div>
        <div class="s-src">出典: UKMTO / Reuters / Al Jazeera（8/18 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S04] 情勢カード③ 日本外交・市場

**対象：** `<!-- カード③ 日本外交・市場 -->` 内の `.s-title` / `.s-body` / `.s-src`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <div class="s-title">🇴🇲 イラン・オマーン、新航路協議は「政治的解決が前提」で継続——原油は膠着観測で88ドル台後半へ</div>
        <div class="s-body">イラン外務省のアラグチー外相は15日、オマーンとの間で進めてきたホルムズ海峡の新たな航行ルート策定協議について「引き続き技術的な議論を続けている」としつつ、実際の運用開始には「まず政治的な解決に至る必要がある」と改めて条件を付けた。8月上旬に地理的座標について暫定合意したとされる南北回廊案は、米・イラン間の政治対立が続く限り実装に至らない見通しである。市場では、米イラン覚書の期限徒過を受けて海峡再開の見通しが一段と後退したとの受け止めから、ブレント原油先物は週明け88ドル台後半（Investing.com時点88.85ドル前後）まで上昇し、WTIも82ドル台へ上げ幅を広げた。IEAは2026年の世界的な供給不足幅が過去5年で最大になるとの見通しを既に示している。日本関係船については、外務省・国土交通省への日英4クエリで新規発表がないことを改めて確認し、残り4隻のまま変化はない。</div>
        <div class="s-src">出典: Al Jazeera / Investing.com / 外務省・国土交通省（8/15〜17 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🗺️ イラン・オマーン、新航路「地図」に了解——ガリバフ議長は資産凍結解除等の履行を封鎖解除の条件に再提示</div>
        <div class="s-body">イラン外務省のバガイ報道官は18日、オマーンとの間で協議してきたホルムズ海峡の新たな航行ルートの「地図」について了解に達したと明らかにした。両国は今後、包括的な合意としてロードマップと共同声明の取りまとめを目指して交渉を継続する方針だが、案件の複雑さと複数の関係者の利害が絡むため長期化しているという。一方、イラン国会議長で対米交渉の中心人物でもあるガリバフ氏は18日、海外で凍結されているイラン資産の解放、石油・ガス取引への制裁解除、イラン港湾への米海軍封鎖の解除という覚書上の米側義務が履行されるまでホルムズ海峡の封鎖を解除しないと国営テレビの演説で改めて表明した。市場ではこうした膠着の長期化観測を背景に、ブレント原油は8/18時点で1バレル90.97ドルへ上昇（前日比+0.11%）。サウジアラムコはUAEフジャイラ沖でのシップ・トゥ・シップ移送により重質原油の出荷を先週再開したと報じられており、湾岸産油国が海峡経由以外の輸送手段を模索する動きも並行して進んでいる。日本関係船については、外務省・国土交通省への日英4クエリで新規発表がないことを改めて確認し、残り4隻のまま変化はない。</div>
        <div class="s-src">出典: Trading Economics / CBS News / 外務省・国土交通省（8/18〜19 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S05] COUNTDOWN フェーズラベル

**対象：** `#cd-phase-label`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 23「米イラン覚書60日期限が延長合意なく徒過——アラグチー外相『対話再開は未決定』、トランプ氏は『米国領化』路線を維持」——封鎖171日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 24「トランプ氏がオマーンへ2度目の爆撃威嚇——船舶が未確認飛翔体で被弾、ガリバフ議長は米側義務履行を封鎖解除の条件に再提示」——封鎖173日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S05] COUNTDOWN dl-note（要約・次の焦点・MOU期限注記）

**対象：** `.dl-note`

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <div class="dl-note">
        🤝 <strong>6月17日署名のイスラマバード覚書が定める60日間の交渉期限が8月16日に到来したが、米・イラン双方とも延長に言及せず事実上形骸化した状態が続いている／アラグチー外相は「米との対話再開はまだ決定していない」と表明する一方、オマーンとの新航路協議は「政治的解決が前提」としつつ継続／トランプ大統領は「ホルムズ海峡米国領化」路線を維持、ベッセント財務長官も「前例のない」対イラン措置を予告／イラン副外相は「海峡はイランのものであり、イランのものであり続ける」と応酬／米シンクタンク・スティムソン・センターは米の迎撃ミサイル・戦略石油備蓄逼迫を指摘し「対イラン圧力手段は乏しい」と分析／ブレント原油は88ドル台後半へ上昇／日本関係船は残り4隻で変化なし——封鎖171日目</strong>
        <br><span style="color:#fde68a;">⚡ 次の24〜48時間の焦点：①米・イランが覚書失効を公式にどう扱うか（新たな枠組み提示の有無） ②イラン・オマーン新航路協議が政治的解決なしに実務合意へ進展するか ③ベッセント財務長官が予告した「前例のない」対イラン措置の内容と時期 ④ブレント原油88ドル台後半からの続伸有無 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU最終期限（8/16）を延長合意なく徒過——事実上の交渉空白期に</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🤝 <strong>トランプ大統領はイラン・オマーンのホルムズ航路協議を巡り「オマーンが邪魔なら地獄まで爆撃する」と2度目の軍事威嚇——米上院ケイン議員は対オマーン武力行使禁止決議案の提出を表明／トランプ氏はクルディスタン地域政府バルザニ議長経由のIRGC直接裏チャンネルの存在を認めたが、IRGC報道官は「完全な虚偽」と全面否定／18日未明、オマーン方面へ出航中の船舶が未確認飛翔体で被弾し乗組員1名負傷、UKMTOが調査中／イラン国会議長ガリバフ氏は資産凍結解除・制裁解除・海上封鎖解除という米側義務履行まで封鎖継続と再表明／イラン・オマーンは新航路地図に「了解」も包括合意・共同声明は調整中／ブレント原油は90ドル台後半へ上昇（8/18時点90.97ドル）／日本関係船は残り4隻で変化なし——封鎖173日目</strong>
        <br><span style="color:#fde68a;">⚡ 次の24〜48時間の焦点：①ケイン議員の対オマーン武力行使禁止決議案が上院に正式提出されるか ②IRGC裏チャンネル報道の真偽を巡る双方の応酬がどう推移するか ③未確認飛翔体による船舶被弾の実行主体特定とUKMTO調査の進展 ④イラン・オマーン新航路の包括合意・共同声明がいつまとまるか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU最終期限（8/16）徒過後も後継の公式枠組みは提示されず——非公式チャンネルと威嚇の応酬が続く</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
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
<!-- OLD:END -->
<!-- NEW:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月19日 08:51 JST 更新</span><br>
  📊 <strong>トランプ氏がオマーンへ2度目の爆撃威嚇——船舶が未確認飛翔体で被弾、IRGC裏チャンネル報道は当事者間で真っ向対立：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#94a3b8;">→</span> — 公式なMOU枠組みは死んだままだが、イラン・オマーン間の新航路「地図了解」という非公式トラックが技術レベルでは細く前進しており、完全な停止とまでは言えない<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — トランプ氏のIRGC裏チャンネル発言をIRGCが即座に否定したことは、公式・非公式いずれの対話ルートも確証を欠いたまま様子見が続く構図を裏付ける<br>
  🅒 MOU形骸化・機能不全 <span style="color:#fbbf24;">→</span> — ガリバフ議長が覚書上の米側義務履行を改めて封鎖解除の条件に掲げたことは、前回確定した形骸化状態が高止まりのまま推移していることを示す<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — トランプ氏が同盟国オマーンへ2度目の爆撃威嚇を行ったことは威嚇対象を交渉当事者以外にも広げる新たなエスカレーション経路であり、船舶への飛翔体被弾も重なって軍事的リスクの高まりを示す<br>
  <strong style="color:#f87171;">米国の圧力対象が交渉当事者のイランから仲介国オマーンにまで広がったことは、対話の枠組みそのものが不安定化していることを意味する。IRGC裏チャンネルの存否を巡る食い違いも、誰が実際に交渉の当事者なのかという根本的な不透明さを一段と際立たせている（A→ B→ C→ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月19日 08:51 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S07] シナリオDタグ（確率矢印: → から ↑ へ変更・要事前確認）

**対象：** `#sc-tag-D`

⚠️ この要素の現況（old_str）は今回未検証です。Claude Code は適用前に `grep -n 'sc-tag-D' docs/index.html` で現在のHTML（矢印記号を含む）を確認し、末尾の矢印スパンを `<span style="color:#f87171;">↑</span>` に置き換えてください（他の文言・スタイルは変更しないこと）。S06本文の「D↑」という記述と整合させるための措置です。

## [S07] シナリオA 本文

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <p>覚書が定めた60日間の交渉期限が延長合意なく8月16日に到来・徒過したことで、既存のイスラマバード覚書に基づく段階的履行という道筋そのものが制度的な後ろ盾を失った。唯一の細い糸は、アラグチー外相が継続を明言したオマーンとの新航路協議だが、本人が「政治的解決が前提」と条件を付けている通り、政治対立が続く限り実務合意には進まない見通しである。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イラン・オマーン間で新航路の「地図」について了解に達したとの発表は、公式MOUの外側で細々と続く実務協議の存在を示すものではある。しかし包括合意・共同声明の取りまとめは依然調整中であり、トランプ氏がオマーンへ爆撃を威嚇したことで、この非公式トラックの仲介役自体が米国の圧力対象となりかねない構図が生まれている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S07] シナリオB 本文

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <p>米シンクタンク・スティムソン・センターの分析が示す通り、米側は迎撃ミサイル・戦略石油備蓄の逼迫により追加の軍事的圧力手段を欠く一方、イラン側も覚書失効後すぐに態度を硬化させる動きは見せておらず、双方が明確な次の一手を欠いたまま様子見を続ける構図が強まっている。アラグチー外相の「対話再開は未決定」という留保付きの発言も、完全な断絶ではなく膠着の持続を示唆する。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>トランプ氏が認めたIRGCとの裏チャンネルをIRGC自身が即座に否定したことは、双方がどの相手と交渉すべきか合意できていないという根本的な機能不全を露呈させた。ガリバフ議長が資産凍結解除等の履行を改めて条件として掲げたことも、要求水準に変化がないまま従来の主張を繰り返す膠着継続シナリオの持続を裏付けている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S07] シナリオC 本文

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <p>イラン国会議長ガリバフ氏が覚書での譲歩獲得を「軍事的にも政治的にも真の勝利」と自賛したことは、テヘランが現状の海峡管理体制を既成事実として固定化させる方向に自信を深めていることを示す。最高国家安全保障会議トップに対米強硬派レザイー元IRGC司令官が就いた人事とも符合し、覚書失効を機にイラン主導の統治枠組みが一段と制度化に向かうリスクが高まっている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>ガリバフ議長が18日、資産凍結解除・制裁解除・海上封鎖解除という米側義務の履行を封鎖解除の前提条件として改めて明示したことは、MOUが公式には機能していない現状をイラン側自身が追認し、独自の条件闘争へと切り替えていることを示す。イラン・オマーンの新航路協議も、米国を交渉から排除した形での既成事実化という側面を帯びつつある。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S07] シナリオD 本文

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
        <p>スティムソン・センターのスラビン氏が指摘する通り、米側の軍事的な追加圧力手段は乏しく、直ちに大規模な軍事エスカレーションへ向かう可能性は当面後退している。ただしトランプ氏の「米国領化」路線とベッセント財務長官が予告する「前例のない」対イラン措置の具体的な内容次第では、偶発的な緊張再燃のリスクが依然として残る。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>トランプ氏がイランのみならず同盟国オマーンにまで爆撃を威嚇した事実は、圧力の矛先が拡散し始めていることを意味し、米上院で武力行使禁止決議案が検討される事態にまで発展した。船舶が未確認飛翔体で被弾し乗組員が負傷した事案も重なり、実行主体が特定されないまま緊張が高止まりする状況が続いている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S08] シナリオフッター（次の焦点5点）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">覚書失効を受け、米・イラン双方が新たな交渉の枠組みを提示するか、それとも無枠組み状態が長期化するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン・オマーン新航路協議が「政治的解決」なしに実務レベルで前進する余地があるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">ベッセント財務長官が予告した「前例のない」対イラン措置の中身と発動時期</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">イラン最高国家安全保障会議（レザイー体制）が覚書失効後にどのような対米方針を打ち出すか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月17日 09:04 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米上院のオマーン武力行使禁止決議案が実際に提出・審議されるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">IRGC裏チャンネルの実在性を巡る米・イラン双方の主張がどちらに軍配が上がるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">未確認飛翔体による船舶被弾事案の実行主体特定とUKMTO調査結果</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">イラン・オマーン新航路の包括合意・共同声明がまとまる時期と内容</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月19日 08:51 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月17日 09:04 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">外交トラックは覚書60日期限が延長合意なく徒過したことで制度的な後ろ盾を失い、イラン側はアラグチー外相が対話再開を「未決定」としつつオマーンとの新航路協議のみ継続と説明している。【北側航路（イラン指定）】直近の公開監視データに大きな更新の報告はなく、高止まりの膠着状態が続いているとみられる。【南ルート（Omani coastal corridor）】新航路の地理的座標は合意済みとされるが、アラグチー外相は運用開始に「政治的解決」を前提条件として付しており、実装は停止したまま。【米の交渉姿勢】トランプ大統領は「ホルムズ海峡米国領化」路線を維持し、ベッセント財務長官も「前例のない」対イラン措置を予告——具体的な発動時期は不明。【紅海・バブエルマンデブ】直近の大規模攻撃の続報はないが、8/11のフーシ派攻撃による死者発生を受け警戒水準は高いまま。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/17 09:04 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月19日 08:51 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">米側の圧力対象がイランに加え仲介国オマーンにも及んだことで、外交トラックは公式・非公式いずれのルートも不安定さを増している。【北側航路（イラン指定）】直近の公開監視データに大きな更新の報告はなく、高止まりの膠着状態が続いているとみられる。【南ルート（Omani coastal corridor）】イラン・オマーン間で新航路の地図に「了解」が成立したと発表されたが、包括合意・共同声明は調整中で実装には至っていない。トランプ氏の対オマーン爆撃威嚇が、この協議の先行きに新たな不確実性を加えている。【米の交渉姿勢】トランプ氏はオマーンへの軍事威嚇に加え、IRGCとの直接裏チャンネルの存在を主張——イラン側は全面否定しており交渉主体自体が不透明。【紅海・バブエルマンデブ】18日、フーシ派がサウジ・アラムコのジザン製油所をドローン攻撃したと表明——第二の紛争前線として警戒継続。【UKMTO 警戒水準】Substantial（継続）、18日未明には船舶が未確認飛翔体で被弾し乗組員1名負傷。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/19 08:51 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S09] 30秒カラム 3行サマリー

**対象：** 「海峡の今」「次の焦点」スパン（「いま何が」直後から）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
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
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
💣 トランプ氏「オマーンが邪魔なら爆撃する」と2度目の威嚇——船舶が未確認飛翔体で被弾し乗組員1名負傷。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷🇴🇲 イラン・オマーンは新航路地図に「了解」も共同声明は調整中。ブレント原油は90ドル台後半へ上昇。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🏛️ 米上院ケイン議員が対オマーン武力行使禁止決議案の提出を表明——封鎖173日目。
</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S09] 30秒カラム ステータスバッジ5枚

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⏳MOU60日期限、延長なく徒過</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷アラグチー「対話再開は未決定」</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸トランプ「米国領化」路線維持</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📊ブレント88ドル台後半へ上昇</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💣トランプ「オマーン爆撃」再威嚇</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚢船舶被弾・乗組員1名負傷</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🤝IRGC裏チャンネル説をIRGCが否定</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📊ブレント90ドル台後半へ上昇</span>
<!-- NEW:END -->
<!-- APPLY:END -->

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
  "dateModified": "2026-08-17T09:04:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-19T08:51:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

## [C01] SHIP_CONFIG dateConfirmed（日本関係船再確認・変化なし）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
  dateConfirmed: '2026年8月17日 09:04 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近会見（8/4）は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年8月19日 08:51 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近会見（8/4）は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- NEW:END -->
<!-- APPLY:END -->

## [S11] 更新ログ ブロック1（常時表示3件：本日分を追加、旧3件目を除外）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月17日 09:04 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/17 09:04</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米イラン間の60日間停戦・最終合意期限「イスラマバード覚書」が8月16日に到来し延長合意なく事実上形骸化（共同通信・時事通信）・アラグチー外相「米との対話再開はまだ決定していない」（8/15 Telegram）——オマーンとの新航路協議は継続も「政治的解決が前提」・トランプ大統領は「ホルムズ海峡米国領化」路線を維持、ベッセント財務長官は「前例のない」対イラン措置を予告・イラン副外相「海峡はイランのものであり、イランのものであり続ける」と応酬・米シンクタンク（スティムソン・センター）は米の迎撃ミサイル・戦略石油備蓄逼迫を指摘し「対イラン圧力手段は乏しい」と分析・イラン国会議長ガリバフ氏「軍事的にも政治的にも真に勝利した」（8/15）・ブレント原油88ドル台後半へ上昇・日本関係船は残り4隻で変化なし・封鎖171日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月15日 06:37 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/15 06:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表——紛争開始来15隻目の被弾・負傷者なし（8/14）・トランプ大統領はロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言（8/14）・イラン副外相ガリババディ氏は「米が戦略的敗北を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開「未決定」とし60日休戦の延長は不要と主張（8/14）・米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を欧州へ拡大、カナダは対イラン制裁5名追加（8/11〜14）・ブレント原油は週央89.53ドルから87ドル台へ反落、IEAは供給不足拡大に警鐘・日本関係船は残り4隻で変化なし・封鎖169日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月13日 10:37 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/13 10:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランIRGC上級顧問ナグディ氏がPBSに「トランプ政権終了（2029年）まで戦争を長期化させ消耗戦に持ち込む選択肢がある」と発言（8/12）・フーシ派が紅海バブエルマンデブ海峡でエジプト所有船「ティハマ」を二重攻撃し乗組員4名・救助隊員2名の計6名死亡10名負傷——今次紛争開始後初のフーシ派関連死者（8/11）・米軍ヘリがパナマ籍船「ヴェラ・ノヴァ」に対封鎖破り阻止でヘルファイア2発発射（3週間で3件目の摘発、8/11）・トランプ氏「米国はホルムズを完全支配」と主張も通航量は8/11に週間最低の8隻へ低下・パキスタンが仲介継続——内相がテヘラン訪問中（8/10）・ブレント原油は87.92ドルへ反落（6営業日続伸後、-1.19%）、EIA原油在庫は2023年来最大の週間増（+1740万バレル）・NYダウ53,770ドル(-21.58、3日続落)・日本関係船は残り4隻で変化なし・封鎖167日目・ニュース4件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月19日 08:51 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/19 08:51</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領がイラン・オマーンのホルムズ航路協議を巡り「オマーンが邪魔なら地獄まで爆撃する」と2度目の軍事威嚇（8/17）・米上院ケイン議員は対オマーン武力行使禁止決議案の提出を表明・トランプ氏はクルディスタン地域政府バルザニ議長経由のIRGC直接裏チャンネルの存在を認めるも、IRGC報道官は「完全な虚偽」と全面否定（8/17）・18日未明、オマーン方面へ出航中の船舶が未確認飛翔体で被弾し乗組員1名負傷、UKMTOが調査中・イラン国会議長ガリバフ氏「米国が資産凍結解除・制裁解除・海上封鎖解除を履行するまで封鎖継続」（8/18）・イラン・オマーンは新航路地図に「了解」も包括合意・共同声明は調整中（イラン外務省バガイ報道官、8/18）・フーシ派はサウジ・アラムコのジザン製油所をドローン攻撃（8/18）・ブレント原油90ドル台後半へ上昇（8/18時点90.97ドル）・サウジアラムコはフジャイラ沖STS移送で出荷再開・日本関係船は残り4隻で変化なし・封鎖173日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月17日 09:04 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/17 09:04</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米イラン間の60日間停戦・最終合意期限「イスラマバード覚書」が8月16日に到来し延長合意なく事実上形骸化（共同通信・時事通信）・アラグチー外相「米との対話再開はまだ決定していない」（8/15 Telegram）——オマーンとの新航路協議は継続も「政治的解決が前提」・トランプ大統領は「ホルムズ海峡米国領化」路線を維持、ベッセント財務長官は「前例のない」対イラン措置を予告・イラン副外相「海峡はイランのものであり、イランのものであり続ける」と応酬・米シンクタンク（スティムソン・センター）は米の迎撃ミサイル・戦略石油備蓄逼迫を指摘し「対イラン圧力手段は乏しい」と分析・イラン国会議長ガリバフ氏「軍事的にも政治的にも真に勝利した」（8/15）・ブレント原油88ドル台後半へ上昇・日本関係船は残り4隻で変化なし・封鎖171日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月15日 06:37 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/15 06:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE、ADNOC関連タンカー2隻が13日夜ホルムズ海峡通航中にイランのドローン攻撃を受けたと発表——紛争開始来15隻目の被弾・負傷者なし（8/14）・トランプ大統領はロングアイランドの集会で「イラン敗北後、ホルムズ海峡を米国領に宣言する」と発言（8/14）・イラン副外相ガリババディ氏は「米が戦略的敗北を認めるまで封鎖継続」と応酬、アラグチー外相は対話再開「未決定」とし60日休戦の延長は不要と主張（8/14）・米はルビオ国務長官がオーストリア・ギリシャ両外相と接触し仲介国を欧州へ拡大、カナダは対イラン制裁5名追加（8/11〜14）・ブレント原油は週央89.53ドルから87ドル台へ反落、IEAは供給不足拡大に警鐘・日本関係船は残り4隻で変化なし・封鎖169日目・ニュース4件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S11] 更新ログ ブロック2（log-collapse 先頭に旧3件目＝8/13分を挿入）

<!-- APPLY:START -->
<!-- FILE:docs/index.html -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月11日 09:26 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月13日 10:37 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/13 10:37</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランIRGC上級顧問ナグディ氏がPBSに「トランプ政権終了（2029年）まで戦争を長期化させ消耗戦に持ち込む選択肢がある」と発言（8/12）・フーシ派が紅海バブエルマンデブ海峡でエジプト所有船「ティハマ」を二重攻撃し乗組員4名・救助隊員2名の計6名死亡10名負傷——今次紛争開始後初のフーシ派関連死者（8/11）・米軍ヘリがパナマ籍船「ヴェラ・ノヴァ」に対封鎖破り阻止でヘルファイア2発発射（3週間で3件目の摘発、8/11）・トランプ氏「米国はホルムズを完全支配」と主張も通航量は8/11に週間最低の8隻へ低下・パキスタンが仲介継続——内相がテヘラン訪問中（8/10）・ブレント原油は87.92ドルへ反落（6営業日続伸後、-1.19%）、EIA原油在庫は2023年来最大の週間増（+1740万バレル）・NYダウ53,770ドル(-21.58、3日続落)・日本関係船は残り4隻で変化なし・封鎖167日目・ニュース4件更新・osint更新</div>
          <div>📅 <strong>2026年8月11日 09:26 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

## [S11] 更新ログ ブロック3（総件数調整・要事前確認）

⚠️ 常時表示3件＋log-collapse内エントリー数の合計が11件を超えていないか、Claude Code は `view` で `docs/index.html` の `#log-collapse` 内エントリー数を数えて確認してください。今回ブロック2でlog-collapse先頭に8/13分を1件追加したため、超過している場合はlog-collapse内の最古エントリー（出典リンク①の直前）を1件削除し、その本文を `docs/data/update_log.json` の配列先頭に追加してください（このAPPLYブロックは提供しません。件数超過が確認された場合のみ、str_replaceで個別対応してください）。

---

## [S10] news_data.json — updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
"updated": "2026年8月17日 09:04 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
"updated": "2026年8月19日 08:51 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

## [S10] news_data.json — latest 配列（新規3件を先頭に追加、最古3件を archive へ移動）

**方針：** `isLatest: true` は新しい先頭1件のみ。旧6件目までのうち古い3件（adnoc-tankers-drone-attack / trump-hormuz-us-territory / iran-strategic-defeat-araghchi）は次のAPPLYブロックで新規archiveバッチへ移動する。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
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
  <!-- OLD:END -->
<!-- NEW:START -->
"latest": [
    {
      "id": "latest-trump-bomb-oman-threat-0817",
      "title": "トランプ氏、オマーンへ2度目の爆撃威嚇——「邪魔をするなら地獄まで爆撃する」",
      "body": "トランプ大統領は17日、Fox Newsの電話取材でイラン・オマーンのホルムズ海峡航路協議を巡り「オマーンが邪魔をするなら地獄まで爆撃してやる」と発言。5月の「吹き飛ばす」発言に続き2度目の対オマーン軍事威嚇となった。米上院ケイン議員は対オマーン武力行使を禁じる決議案の提出を表明した。",
      "sourceLabel": "Washington Post",
      "date": "2026年8月17日（現地）/ 2026年8月18日 JST",
      "label": "💣 外交",
      "url": "https://www.washingtonpost.com/world/2026/08/17/trump-threatens-bomb-oman-if-it-gets-way/",
      "isLatest": true
    },
    {
      "id": "latest-irgc-backchannel-denial-0817",
      "title": "トランプ氏「IRGCと直接裏チャンネル」と表明——IRGC報道官は「完全な虚偽」と全面否定",
      "body": "トランプ氏はクルディスタン地域政府バルザニ議長を仲介役としたIRGCとの直接裏チャンネルの存在を認めたが、IRGC報道官モヘッビ准将はタスニム通信に対し「純然たる虚偽」であり米側との対話は一切行われていないと否定した。双方の主張が真っ向から対立している。",
      "sourceLabel": "Axios",
      "date": "2026年8月17日（現地）/ 2026年8月18日 JST",
      "label": "🤝 外交",
      "url": "https://www.axios.com/2026/08/16/iran-backchannel-trump-gabbard-barzani-war",
      "isLatest": false
    },
    {
      "id": "latest-vessel-unknown-projectile-0818",
      "title": "船舶が未確認飛翔体で被弾——機関室損傷、乗組員1名負傷",
      "body": "英海運当局UKMTOは18日未明、オマーン方面へ出航中の船舶が未確認の飛翔体により被弾したとの報告を受けたと発表。機関室が損傷し乗組員1名が負傷、残る乗組員はオマーン沿岸警備隊が支援している。環境影響の報告はなく当局が調査中。",
      "sourceLabel": "Arab News（Reuters）",
      "date": "2026年8月18日（現地）/ 2026年8月18日 JST",
      "label": "🚢 軍事",
      "url": "https://www.arabnews.com/node/2655036/middle-east",
      "isLatest": false
    },
    {
      "id": "latest-mou-deadline-expires-stalemate-0816",
      "title": "米イラン覚書60日期限、延長合意なく到来——「不安定な膠着」長期化の観測強まる",
      "body": "米国とイランは16日、戦闘終結に向けた最終合意の交渉期限とされたイスラマバード覚書の60日期限を迎えた。期限は延長可能だが双方とも延長に言及せず、覚書は事実上形骸化。ホルムズ海峡の開放に向けてイランとオマーンが協議を続けるが正常化には至らず、戦闘でも平和でもない「不安定な膠着状態」の長期化が懸念されている。",
      "sourceLabel": "共同通信",
      "date": "2026年8月16日（現地）/ 2026年8月16日 JST",
      "label": "⏳ 外交",
      "url": "https://news.yahoo.co.jp/articles/c180d898d2b9321ba1560f65adc67dd5b988c589",
      "isLatest": false
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
      "batchLabel": "2026年8月中旬（8/11〜8/12）",<!-- OLD:END -->
<!-- NEW:START -->
"archive": [
    {
      "batchLabel": "2026年8月中旬（8/13〜8/14）",
      "items": [
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
      ]
    },
    {
      "batchLabel": "2026年8月中旬（8/11〜8/12）",<!-- NEW:END -->
<!-- APPLY:END -->

## [S10] news_data.json — osint 配列（新規1件を先頭に追加、既存記事は isLatest: false へ）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
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
    },<!-- OLD:END -->
<!-- NEW:START -->
"osint": [
    {
      "id": "osint-trump-bomb-oman-second-time-0818",
      "date": "2026年8月18日（現地）/ 2026年8月18日 JST",
      "titleJa": "なぜトランプ氏は2度目のオマーン爆撃威嚇に踏み切ったのか",
      "titleEn": "Why has Trump threatened to bomb Oman – for a second time?",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/2026/8/18/why-has-trump-threatened-to-bomb-oman-for-a-second-time",
      "isLatest": true
    },
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
      "isLatest": false
    },<!-- NEW:END -->
<!-- APPLY:END -->

---

## [ARCHIVE] docs/data/archive_timeline.json への追記（Claude Code手動str_replace対象）

`docs/data/archive_timeline.json` の `entries` 配列末尾に、以下のエントリーを追加してください（既存エントリーは変更しないこと）。

```json
{
  "date": "2026-08-19",
  "dateLabel": "2026/08/19 08:51",
  "blockadeDay": 173,
  "summary": "トランプ大統領がイラン・オマーンのホルムズ航路協議を巡り「オマーンが邪魔なら地獄まで爆撃する」と2度目の軍事威嚇（8/17）・米上院ケイン議員は対オマーン武力行使禁止決議案の提出を表明・トランプ氏はクルディスタン地域政府バルザニ議長経由のIRGC直接裏チャンネルの存在を認めるも、IRGC報道官は「完全な虚偽」と全面否定（8/17）・18日未明、オマーン方面へ出航中の船舶が未確認飛翔体で被弾し乗組員1名負傷、UKMTOが調査中・イラン国会議長ガリバフ氏「米国が資産凍結解除・制裁解除・海上封鎖解除を履行するまで封鎖継続」（8/18）・イラン・オマーンは新航路地図に「了解」も包括合意・共同声明は調整中（イラン外務省バガイ報道官、8/18）・フーシ派はサウジ・アラムコのジザン製油所をドローン攻撃（8/18）・ブレント原油90ドル台後半へ上昇（8/18時点90.97ドル）・サウジアラムコはフジャイラ沖STS移送で出荷再開・日本関係船は残り4隻で変化なし・封鎖173日目・ニュース3件更新・osint更新",
  "relatedNews": [
    {
      "title": "トランプ氏、オマーンへ2度目の爆撃威嚇——ホルムズ海峡巡る対立エスカレート",
      "url": "https://www.washingtonpost.com/world/2026/08/17/trump-threatens-bomb-oman-if-it-gets-way/",
      "sourceLabel": "Washington Post"
    },
    {
      "title": "トランプ氏のIRGC裏チャンネル舞台裏——クルディスタン議長バルザニ氏の役割",
      "url": "https://www.axios.com/2026/08/16/iran-backchannel-trump-gabbard-barzani-war",
      "sourceLabel": "Axios"
    },
    {
      "title": "船舶が未確認飛翔体で被弾——ホルムズ海峡、乗組員1名負傷",
      "url": "https://www.arabnews.com/node/2655036/middle-east",
      "sourceLabel": "Arab News（Reuters）"
    }
  ]
}
```

---

## ✅ 出力前セルフチェック（本日のセルフチェック項目数：19件）

```
[✓] Step 0 project_knowledge_search 2クエリ実施・baseline確認（8/17 09:04 JST・封鎖171日目）
[✓] C01タンカー確認：日本語3クエリ＋英語1クエリ全実施・変化なし・残り4隻
[✓] S01 ヘッダー ― 2026年8月19日 08:51 JST・封鎖173日目 ✓
[✓] S02 TICKER ― オマーン爆撃威嚇・IRGC裏チャンネル否定・船舶被弾・ガリバフ条件再提示・封鎖173日目 ✓
[✓] S03 速報インシデント ― 8/19 08:51付け・トグル見出し／ffcccc要約／li2件（8/17爆撃威嚇, 8/18船舶被弾）を新規追加 ✓
[✓] S04 情勢カード3枚 ― 全カードを本日情勢に更新（重複表現を避け各カードで異なる切り口：①外交・威嚇/裏チャンネル ②軍事・被弾/フーシ派 ③航路合意/市場）✓
[✓] S05 COUNTDOWN ― Phase24・封鎖173日目・「後継枠組みなき威嚇と非公式チャンネルの応酬」に更新 ✓
[✓] S06 シナリオ確率補足バナー ― 8/19 08:51 JST日付更新・A→ B→ C→ D↑（矢印はダッシュボード自動同期のため数値は非記載）✓
[✓] S07 シナリオ4本 ― A/B/C/D本文を本日情勢に更新（S06と異なる切り口で記述）・sc-tag-Dの矢印更新は要事前grep確認と明記 ✓
[✓] S08 シナリオフッター ― 次の焦点5点を本日版に更新（S05のdl-noteと重複しない中長期視点で記述）✓
[✓] S08.5 全ルート現況サマリー ― 8/19 08:51 JST更新・S08.5固有の切り口（航路別）で記述 ✓
[✓] S09 30秒カラム ― 3行サマリー＋バッジ5枚を最後に更新 ✓
[✓] S10 news_data.json ― latest 3件追加（3件をarchiveへ新規バッチ移動）・osint 1件追加・updated日付 ✓
[✓] S11 更新ログ ― 2ブロック構成（常時表示3件固定＋log-collapse先頭挿入）・ブロック3は総件数要目視確認と明記 ✓
[✓] C01 SHIP_CONFIG dateConfirmed ― 8/19 08:51 JST・変化なし ✓
[✓] JSON-LD dateModified ― 2026-08-19T08:51:00+09:00 ✓
[✓] archive_timeline.json ― 2026-08-19エントリー追加（Claude Code手動str_replace対象）✓
[✓] Python OLD-block一意性検証 ― sc-tag-D関連を除く全APPLYブロックでcount==1を目視確認済み（sc-tag-Dのみ現地grep要）✓
[✓] 各セクションの文章重複チェック ― S01(総合要約)/S02(箇条書き)/S03(時系列+背景)/S04①(外交・威嚇分析)②(軍事・被弾詳細)③(航路合意・市場)/S05(直近48h焦点)/S06(シナリオ別影響)/S07(シナリオ別深掘り)/S08(中長期焦点)/S08.5(航路別)/S09(最圧縮3行+バッジ)で表現・切り口をそれぞれ変えて記述 ✓

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記は変更なし（S05 dl-box内の枠組みは不変）✓
TICKER内JST表記チェック：全日付にJST付き ✓
Al Jazeera使用箇所チェック：📰関連最新ニュース(latest)には不使用、osintのみ使用（新規追加のオマーン威嚇解説記事もosintに配置）✓
人名表記チェック：習近平の言及なし（該当なし）／トランプ・アラグチー・ガリバフ・ガリババディ・バルザニ・モヘッビ・ケイン等は日本語カタカナ表記で統一 ✓
URL捏造チェック：全URLはweb_search結果から取得した実在URLのみ使用（Washington Post・Axios・Arab News・Al Jazeeraいずれも確認済み）✓
禁止ソースチェック：毎日新聞・Wikipedia・TBS・朝日新聞・NHK・東京新聞・テレビ朝日は不使用 ✓
```
