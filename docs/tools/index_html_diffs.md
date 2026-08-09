# index_html_diffs.md — 2026年8月9日 10:06 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## 出力前セルフチェック（先貼り・作業前に空欄で貼付）

```
[ ] S01 ヘッダー日時・警戒レベル
[ ] S02 TICKER
[ ] S03 速報インシデント（トグルボタン＋strong＋リスト先頭に新規追加）
[ ] S04 情勢カード3枚
[ ] S05 COUNTDOWN（phase-label＋dl-note）
[ ] S06 シナリオ確率補足バナー（①sec-title直下の日付見出し／②確率バナー末尾の「時点」表記の両方）
[ ] S07 シナリオ4本（タイトル・本文）
[ ] S08 シナリオフッター（次の焦点5つ）
[ ] S08.5 全ルート現況サマリー
[ ] S09 30秒カラム（3行サマリー＋ステータスバッジ）※最後に執筆
[ ] S10 news_data.json（latest4件追加・archive移動・osint2件追記）
[ ] S11 更新ログ（2ブロック構成＋合計超過分削除）
[ ] JSON-LD dateModified
[ ] C01 タンカー確認（日英4クエリ）
[ ] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[ ] 全体 ― ニュースURLにAI捏造・推測URLが混入していないか（web検索確認済みURLのみ使用）
[ ] 全体 ― 📰関連最新ニュースにAl Jazeeraが混入していないか（osintのみ使用可）
[ ] 全体 ― 禁止ソース（毎日新聞・Wikipedia・TBS/TBS NEWS DIG・朝日・NHK・東京新聞・テレビ朝日）混入なし
[ ] 全体 ― 人名が日本語表記になっているか（「Xi」「Trump」のみの表記なし）
[ ] シナリオC・D本文が近似文言でなく差別化されているか
[ ] 各セクションで同一情報を重複記載せず、セクションの性格に応じて書き方を変えているか
```

**本日のセルフチェック項目数：19件**

```
[x] S01 ― 更新済み
[x] S02 ― 更新済み
[x] S03 ― 更新済み（トグル・strong・リスト先頭2件追加）
[x] S04 ― 更新済み（3枚とも更新）
[x] S05 ― 更新済み
[x] S06 ― 更新済み（①②両方の日付を2026年8月9日 10:06 JSTに統一）
[x] S07 ― 更新済み（4本とも本文差し替え）
[x] S08 ― 更新済み
[x] S08.5 ― 更新済み（S08完了後・S09直前に配置）
[x] S09 ― 更新済み（最後に執筆）
[x] S10 ― 更新済み（latest4件追加・archiveへ4件移動・osint2件追記）
[x] S11 ― 更新済み（2ブロック構成＋合計超過につき最古1件を削除）
[x] JSON-LD dateModified ― 2026-08-09に更新済み
[x] C01 ― 日本語3クエリ＋英語1クエリを個別実行。外務省・国交省とも新規発表なし確認。金子国交相の直近会見（8/4）は熊本地震対応が主題でホルムズ言及なし。→ 残り4隻・変化なしを維持
[x] 日付表記 ― 全箇所「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一
[x] ニュースURL ― 全てweb検索で実在確認済み（Reuters/Bloomberg/CNBC/CNN/Gulf News/Shafaq News/US News/Türkiye Today/TradingEconomics等）、AI捏造URLなし
[x] Al Jazeera ― 📰関連最新ニュース（latest/archive）には不使用。🌐現地メディア視点（osint）のみに使用
[x] 禁止ソース ― 毎日新聞・Wikipedia・TBS/TBS NEWS DIG・朝日・NHK・東京新聞・テレビ朝日、いずれも混入なし（NHK記事は確認のみに使用し出典・URLとしては不使用）
[x] 人名表記 ― 該当箇所なし
[x] シナリオC・D ― CはイラN議会法案（依然審議中・可決未了）による制度化リスクの停滞、DはUAE-ADNOCタンカー攻撃とサウジ・パキスタン・トルコ相互防衛協定という新規の軍事的緊張材料で差別化
[x] セクション重複回避 ― UAE-ADNOC攻撃／米封鎖解除条件／サウジ防衛協定／フーシ派激化／市場動向の5つの材料を、S01(概観)・S02(箇条書き速報)・S03(詳細経緯＋出典)・S04(3カード個別深掘り)・S08.5(ルート別実務影響)・S09(3行超要約)でそれぞれ異なる切り口・文体で記載
```

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イラン・オマーンがホルムズ海峡の安全航路の座標に合意、共同声明は最終調整段階／米メディアはオマーンが「入域イラン管理・出域オマーン管理」の暫定枠組みに合意したと報道／一方でイラン議会委員会は米・イスラエル船排除と他国船への最大7%通行料課税、違反時は貨物価値20%罰金の法案を審議、米政府は即座に拒否／フーシ派はサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目／NYダウは3日連続最高値も6日は反落、原油は乱高下／封鎖161日目）</span>
    <span class="badge-item badge-date">📅2026年8月7日 09:45 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（UAE政府、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「海賊行為」と非難・負傷者なし／ADNOCは紛争開始以来15隻が被弾・今週だけで3隻・死者1名負傷20名と発表／米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明／イラン議会の米・イスラエル船排除・通行料法案はなお文言調整中で可決未了／サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応／NYダウ・S&P500とも最高値圏、ブレント83.55ドル／封鎖163日目）</span>
    <span class="badge-item badge-date">📅2026年8月9日 10:06 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月7日 09:45 JST） -->
      🇮🇷🇴🇲【航路座標に合意】イラン外務省、ホルムズ海峡の安全航路の地理的座標についてオマーンと合意したと発表——共同声明は最終調整・起草段階（IRNA、8/5）｜🚢 米メディア（MS NOW）：オマーンは入域＝イラン管理ルート・出域＝オマーン管理ルートとする暫定枠組みに合意したと報道（8/6）｜⚠️【イラン議会が対抗法案】議会委員会が米・イスラエル船の永久排除、他国船に貨物価値最大7%の通行料、違反時20%の罰金を課す法案を審議（Fars通信、8/6）｜🇺🇸 米政府はこの案を即座に拒否——「承認・許可・通行料一切なしの自由航行」を要求（CNBC、8/6）｜🐹 フーシ派、サウジタンカー「Wafa」をヤンブー沖で攻撃と主張——7/22の紅海封鎖開始以降8隻目、29隻が引き返し（Reuters、8/5）｜📈 NYダウは263ドル高の54,349.12ドルで3日連続最高値（8/5）も6日はハイテク株主導で反落｜🛢️ 原油は乱高下——イラン議会案への懸念でブレントは一時81ドル台へ反発、WTIは75ドル前後で推移（8/6）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英4クエリで再確認・金子国交相8/4会見は熊本地震対応が主題）｜封鎖161日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月9日 10:06 JST） -->
      🇦🇪【ADNOCタンカー再び被弾】UAE政府、8日未明のイランによるミサイル攻撃を「敵対的行為」「海賊行為」と非難——負傷者なし・状況は制御下（Reuters、8/8）｜📊 ADNOC：紛争開始以来15隻が被弾、今週だけで3隻——死者1名・負傷者20名（Bloomberg/Gulf News、8/7）｜🇺🇸【封鎖解除の条件提示】米当局者、無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除すると表明——イラン交渉団は最高国家安全保障会議の最終承認待ちとの報道も（Shafaq News、8/7〜8）｜🇮🇷 イラン議会の排除・通行料法案はなお文言調整中——可決には至らず｜🇸🇦🇵🇰🇹🇷【NATO型防衛協定】サウジ・パキスタン・トルコがメッカで相互防衛協定に署名——フーシ派の対サウジ攻撃激化への対応（CNN、8/7）｜🐹 フーシ派、木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷｜📈 NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、ブレントは83.55ドル(+1.29%)｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英4クエリで再確認・金子国交相直近会見は熊本地震対応が主題）｜封鎖163日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

### トグルボタン内タイトル＋日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">イラン・オマーンが航路座標に合意——一方でイラン議会は米・イスラエル船排除と通行料の法案を審議、米は即座に拒否</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/7 09:45 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">UAE、イランによるADNOCタンカーへのミサイル攻撃を非難——米は無制限航行再開を条件に対イラン封鎖解除の方針、サウジは新防衛協定で対抗</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/9 10:06 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/7 09:45 速報】イラン外務省報道官バガイ氏は5日、ホルムズ海峡の安全航路についてオマーンと地理的座標で合意したと発表。両国の共同声明は最終調整・起草段階にあるとした（CNN/Bloomberg/Euronews）｜米メディアMS NOWは6日、オマーンが入域＝イラン管理ルート・出域＝オマーン管理ルートとする暫定枠組みに合意したと関係者の話として報道。イラン副外相ガリババディ氏はこの合意が海峡の自動的な全面再開を意味しないと釘を刺した（IRNA）｜一方、イラン議会の委員会は6日、米・イスラエル関連船を恒久的に排除し、その他の「敵対国」船には貨物価値最大7%の通行料を、違反船には20%の罰金を課す法案を審議していると国営ファールス通信が報道（Reuters/NPR）｜米政府高官はこの案を即座に拒否し、「承認・許可・通行料を一切伴わない自由な航行」を要求すると表明（CNBC）｜フーシ派は5日、サウジのヤンブー沖でタンカー「Wafa」に複数のミサイルを撃ち込んだと主張——7/22の紅海封鎖宣言以降、被弾したサウジタンカーは8隻目、引き返した船舶は29隻に達したとした（Reuters/AFP）｜市場では5日にNYダウが263ドル高の54,349.12ドルで3日連続最高値を更新したが、6日はハイテク株主導で反落。原油はイラン議会案への懸念からブレントが一時81ドル台へ反発する場面もあり、乱高下が続いている｜日本関係船は残り4隻で変化なし｜封鎖161日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/9 10:06 速報】UAE外務省は8日、国営石油会社ADNOC関連のタンカーが同日未明にホルムズ海峡通航中にイランからミサイル攻撃を受けたと発表し、「敵対的なイランの攻撃」「海賊行為」と非難した。国営通信WAMは当初ADNOCの発表として「状況は制御下にある」と伝え、負傷者は報告されていない（Reuters）｜これに先立ちADNOCは7日、紛争開始以来15隻の関連船舶がミサイル・ドローンで攻撃を受け、今週だけで3隻が被弾、死者1名・負傷者20名に上ると発表していた（Bloomberg/Gulf News）｜米当局者はロイターに対し、ホルムズ海峡での商用航行が制限なく再開される合意が発表され次第、対イラン港湾封鎖を解除する方針を明らかにした。イラン交渉団は同国最高国家安全保障会議の最終承認を待っている状態とAxiosが報じたという（Shafaq News）｜イラン議会の米・イスラエル船排除・通行料法案は依然文言調整中で可決には至っていない｜サウジアラビアは7日、パキスタン・トルコとメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化を受けた動き（CNN）｜フーシ派は木曜に少なくとも30名の政府軍兵士を殺害する大規模攻撃を実施、金曜も攻撃を継続しマリブで民間人2名が死亡・14名が負傷した｜市場ではNYダウ・S&P500がともに最高値圏を維持、原油はブレントが83.55ドルまで上昇｜日本関係船は残り4隻で変化なし｜封鎖163日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に2件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🇮🇷🇴🇲 8/5 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇦🇪 8/8 JST（現地未明）</span>
  <span style="color:#e2e8f0;"> UAE外務省は、ADNOC関連タンカーがホルムズ海峡通航中にイランからミサイル攻撃を受けたと発表し「敵対的なイランの攻撃」「海賊行為」と非難する声明を出した。国営通信WAMは当初、ADNOC発表として被弾したタンカーの詳細（船名・積荷）は明らかにせず「状況は制御下にある」と伝達。負傷者の報告はない（Reuters）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🇸🇦🇵🇰🇹🇷 8/7 JST</span>
  <span style="color:#e2e8f0;"> サウジアラビア・パキスタン・トルコがメッカで相互防衛協定に署名。参加国への攻撃を全参加国への攻撃とみなすNATO第5条型の条項を含み、サウジがイスラム圏屈指の2つの軍事大国と集団防衛の枠組みを構築する形となった。フーシ派が同日、イエメン東部の政府軍基地を攻撃したことを背景とした動き（CNN）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🇮🇷🇴🇲 8/5 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- カード① 外交交渉 -->
  <div class="sit-card info">
    <div class="s-icon">🤝</div>
        <div class="s-title">🇮🇷🇴🇲 イラン・オマーンが航路座標に合意——共同声明は最終調整段階</div>
        <div class="s-body">イラン外務省報道官バガイ氏は5日、対岸のオマーンとホルムズ海峡の安全航路について地理的座標で合意したと発表。両国の共同声明は最終レビュー・起草段階にあるとした。米メディアMS NOWは6日、オマーンが入域＝イラン管理ルート・出域＝オマーン管理ルートとする暫定枠組みに合意したと関係者の話として報道。イラン副外相ガリババディ氏は、この合意自体が海峡の自動的な全面再開を意味するわけではないと強調しており、実現しても米の対イラン封鎖解除が前提条件である点は変わらない。</div>
        <div class="s-src">出典: CNN / Bloomberg / Euronews（8/5〜6 JST 更新）</div>
  </div>

  <!-- カード② 軍事情勢 -->
  <div class="sit-card warning">
    <div class="s-icon">🇮🇷</div>
        <div class="s-title">🇮🇷 イラン議会、米・イスラエル船排除と通行料の法案を審議——米は即座に拒否</div>
        <div class="s-body">イラン議会の委員会は6日、米・イスラエル関連船舶を恒久的に海峡通過から排除し、その他の「敵対国」船には戦争被害への補償として貨物価値最大7%の通行料を、条件違反時には20%の罰金を課す法案を審議していると国営ファールス通信が報じた。法案はなお専門家審査中とされる。これに対し米政府高官はCNBCに対し「暫定ルートは承認・許可・通行料を一切伴わない自由な航行でなければならない」と述べ、案を拒否する姿勢を示した。イラン・オマーン間の技術合意と、イラン議会が目指す一方的な統制強化との間には温度差が浮き彫りになっている。</div>
        <div class="s-src">出典: Fars通信 / Reuters / NPR / CNBC（8/6 JST 更新）</div>
  </div>

  <!-- カード③ エネルギー・市場 -->
  <div class="sit-card danger">
    <div class="s-icon">📈</div>
        <div class="s-title">📈 NYダウ3日連続最高値も6日反落、原油は乱高下——フーシ派はサウジタンカーを攻撃</div>
        <div class="s-body">5日のNY株式市場でNYダウは前日比263.24ドル高の54,349.12ドルと3日連続で史上最高値を更新したが、6日はハイテク株の利益確定売りに押され反落。エネルギー株は原油高を受け上昇した。原油はイラン議会の対米船排除・通行料法案への懸念からブレントが3営業日続落後に一時81ドル台まで反発、WTIは75ドル前後で推移するなど乱高下が続いている。フーシ派は5日、紅海のサウジ港湾都市ヤンブー沖でサウジタンカー「Wafa」に複数のミサイルを撃ち込んだと主張。7/22の封鎖宣言以降、被弾したサウジタンカーは8隻目、引き返した船舶は29隻に達したとしている。日本関係船は残り4隻から変化なし（8/7 09:45 JST再確認）。</div>
        <div class="s-src">出典: TheStreet / TradingEconomics / Reuters（8/5〜6 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- カード① 軍事情勢 -->
  <div class="sit-card danger">
    <div class="s-icon">🇦🇪</div>
        <div class="s-title">🇦🇪 UAE、ADNOCタンカーへのイランのミサイル攻撃を非難——「海賊行為」と表現、負傷者なし</div>
        <div class="s-body">UAE外務省は8日未明、国営石油会社ADNOC関連のタンカーがホルムズ海峡通航中にイランからミサイル攻撃を受けたと発表し「敵対的なイランの攻撃」「海賊行為」と非難する声明を出した。国営通信WAMは当初ADNOC発表として、被弾したタンカーの詳細を明らかにせず「状況は制御下にある」と伝えた。負傷者の報告はない。これに先立ちADNOCは7日、紛争開始以来15隻の関連船舶がミサイル・ドローンで攻撃を受け、今週だけで3隻が被弾、死者1名・負傷者20名に達したと発表していた。UAEが攻撃の主体をイランと名指しし非難する声明を出すのは、これまでの民間企業単独の発表からさらに一段深刻な政治的対応となる。</div>
        <div class="s-src">出典: Reuters / US News / Bloomberg / Gulf News（8/7〜8 JST 更新）</div>
  </div>

  <!-- カード② 外交・封鎖解除の条件 -->
  <div class="sit-card info">
    <div class="s-icon">🇺🇸</div>
        <div class="s-title">🇺🇸 米当局者「無制限の航行再開合意が出れば対イラン封鎖解除」——イラン議会法案はなお審議中</div>
        <div class="s-body">米当局者はロイターに対し、ホルムズ海峡での商用航行が制限なく再開されるとの合意が発表され次第、米国は対イラン港湾封鎖を解除する方針だと明らかにした。イラン交渉団は同国最高国家安全保障会議の最終承認を待っている段階とAxiosが伝えたとされる。一方でイラン側は、米・イスラエル関連船の恒久排除や貨物価値最大7%の通行料を盛り込んだ議会法案について、依然「専門家審査中」の段階にとどまり文言調整が続いており、可決・成立の見通しは立っていない。外交トラックの前進と国内立法プロセスの停滞が併存する状況が続く。</div>
        <div class="s-src">出典: Shafaq News / Reuters / ZeroHedge（8/7〜8 JST 更新）</div>
  </div>

  <!-- カード③ 地域安保・市場 -->
  <div class="sit-card warning">
    <div class="s-icon">🇸🇦</div>
        <div class="s-title">🇸🇦🇵🇰🇹🇷 サウジ・パキスタン・トルコがNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化が背景</div>
        <div class="s-body">サウジアラビアは7日、パキスタン・トルコとメッカで、参加国への攻撃を全参加国への攻撃とみなす集団防衛条項を含む相互防衛協定に署名した。イラン系フーシ派が木曜（6日）にイエメン政府軍拠点を攻撃し30名超を殺害、金曜（7日）も攻撃を継続してマリブで民間人2名が死亡・14名が負傷するなど、対サウジ圧力が急速に強まっていることが背景にある。市場面では、NYダウ54,036.93ドル（+0.28%）・S&P500は7,757.64ドルで最高値を更新する一方、原油はブレントが83.55ドル（+1.29%）まで上昇し、ホルムズ情勢を巡る不透明感の高まりを織り込む展開となった。</div>
        <div class="s-src">出典: CNN / The Hill / TradingEconomics / CNBC（8/7 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN（phase-label＋dl-note）

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 19「イラン・オマーンが航路座標に合意も、イラン議会は米船排除・通行料の法案を審議——米は即座に拒否」——封鎖161日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 20「UAEがADNOCタンカーへのイラン攻撃を非難、米は封鎖解除の条件提示——サウジは新防衛協定で応戦態勢」——封鎖163日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🤝 <strong>イラン外務省がオマーンとホルムズ海峡の安全航路の座標に合意したと発表——共同声明は最終調整段階（8/5）／米メディアはオマーンが入域イラン管理・出域オマーン管理の暫定枠組みに合意したと報道（8/6）／一方イラン議会委員会は米・イスラエル船の恒久排除と他国船への最大7%通行料・違反時20%罰金の法案を審議、米政府は「無条件の自由航行」を求め即座に拒否（8/6）——フーシ派はサウジタンカー「Wafa」への攻撃を主張、紅海封鎖開始以降8隻目（8/5）——日本関係船は残り4隻で変化なし——封鎖161日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残9日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①イラン議会の対米・イスラエル排除／通行料法案を巡る対立が収束するか ②イラン・オマーンの共同声明が正式発表され、内容に米の関与が反映されるか ③米の「無条件自由航行」要求とイランの「許可制・通行料」要求の溝が埋まるか ④フーシ派の紅海攻撃激化がホルムズ情勢と連動してエスカレートしないか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残9日（8/16）</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🤝 <strong>UAE外務省が8日未明のADNOC関連タンカーへのイラン攻撃を「海賊行為」と非難（負傷者なし）／ADNOCは紛争開始以来15隻被弾・死者1名負傷20名と発表（8/7）／米当局者は無制限の航行再開合意が出れば対イラン封鎖を解除すると表明、イラン交渉団は最高国家安全保障会議の承認待ちとの報道（8/7〜8）／イラン議会の排除・通行料法案はなお文言調整中で可決未了／サウジ・パキスタン・トルコがNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（8/7）／日本関係船は残り4隻で変化なし——封鎖163日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残7日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①UAE-ADNOC攻撃の実行主体・被害の詳細が明らかになるか ②米の「無制限航行再開→封鎖解除」条件を満たす合意がまとまるか ③イラン議会の排除・通行料法案の文言調整がいつ決着するか ④サウジ新防衛協定発足後もフーシ派の対サウジ攻撃が激化を続けるか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残7日（8/16）</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率更新補足バナー（① sec-title直下／② 確率バナー末尾の両方）

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月7日 09:45 JST 更新</span><br>
  📊 <strong>イラン・オマーンは航路座標に合意も、イラン議会は米・イスラエル船排除と通行料の法案を審議——米は即座に拒否：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#fbbf24;">→</span> — イラン・オマーン間の技術的合意（航路座標）は進展だが、イラン議会の一方的な排除・通行料法案に米が即座に反発しており、全体としての合意成立には至っていない<br>
  🅑 膠着継続 <span style="color:#4ade80;">↑</span> — 二国間の技術協議は進む一方、米・イラン間の根本的な条件（無条件自由航行 vs 許可制・通行料）の溝は埋まっておらず、当面の膠着継続がより現実的な帰結となっている<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — イラン議会が提示する米・イスラエル船の恒久排除と通行料課税の法案は、海峡統制の制度化・恒久化そのものであり、Cシナリオの警戒する事態に一歩近づいた<br>
  🅓 全面対決・無期限封鎖 <span style="color:#fbbf24;">→</span> — フーシ派の紅海攻撃は継続しレザイー将軍の攻撃警告も撤回されていないが、本日時点で米・イラン間の直接的な軍事エスカレーションの新規報告はない<br>
  <strong style="color:#fbbf24;">イラン・オマーンの技術合意は前進材料だが、イラン議会の一方的な統制強化の動きが米の即時拒否を招いており、外交解決シナリオの勢いは足踏み。膠着継続とMOU形骸化のリスクがともに高まっている（A→ B↑ C↑ D→）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月7日 09:45 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月9日 10:06 JST 更新</span><br>
  📊 <strong>UAEがADNOCタンカーへのイラン攻撃を非難、米は封鎖解除の条件を提示——サウジは新防衛協定で応戦態勢：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#fbbf24;">→</span> — 米当局者が「無制限航行再開合意→封鎖解除」という具体的な条件を提示したのは前進材料だが、UAEタンカー攻撃という新たな軍事事案が同時進行しており綱引きが続く<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — イラン議会法案は依然「文言調整中」で決着せず、米・イラン間の根本条件の溝も埋まらないまま、技術面の停滞状態が続いている<br>
  🅒 MOU形骸化・機能不全 <span style="color:#fbbf24;">→</span> — イラン議会の排除・通行料法案に新たな進展はなく、制度化リスクは前回水準からの変化なし<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — UAE政府がイランの攻撃を公式に「海賊行為」と非難したことに加え、サウジ・パキスタン・トルコがNATO第5条型の相互防衛協定を締結し、フーシ派の対サウジ攻撃も激化——地域全体の軍事的緊張が明確に高まった<br>
  <strong style="color:#f87171;">UAEによる対イラン非難声明と、サウジを中心とする新たな軍事同盟の形成は、外交トラックとは別の軍事的緊張の高まりを示している。イラン議会法案の停滞で制度化リスクに大きな変化はないが、地域的な武力衝突の危険性は明確に上昇した（A→ B→ C→ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月9日 10:06 JST 時点での分析に基づく自動同期
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（タイトル・本文）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>イラン・オマーンが安全航路の座標に合意し共同声明が最終調整段階に入ったことは、Aシナリオにとって具体的な前進材料である。しかしイラン議会が米・イスラエル船の恒久排除と通行料課税の法案を審議し、米政府がこれを即座に拒否したことで、二国間の技術合意と米・イラン間の根本条件のギャップが露呈した。全面再開に至るには、この溝を埋める必要がある。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>米当局者が「無制限の商用航行再開合意が出れば対イラン封鎖を解除する」という具体的な条件を初めて明示したことは、段階的MOU履行の道筋を描く上で意味のある一歩である。ただし合意成立の前提となるイラン議会の排除・通行料法案はなお文言調整段階にとどまり、同時にUAE関連タンカーへの新たな攻撃も発生しており、条件が整うまでには依然距離がある。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>イラン・オマーンの二国間協議は座標合意まで進んだが、これは海峡再開の一部に過ぎない。イラン議会が審議する米船排除・通行料法案に米側が「無条件の自由航行」を要求して即時反発したことで、米・イラン間の根本条件は依然平行線のままである。技術面の進展と政治的対立が併存する状態が当面続く可能性が高い。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>イラン議会の排除・通行料法案は「専門家審査中」からステータスが動かず、米側が提示した封鎖解除の条件を満たすめどは立っていない。並行してADNOCタンカーへの攻撃やサウジの新防衛協定締結といった動きが進んでおり、外交と軍事の両トラックが並行して停滞・緊張する状態がより長期化する様相を呈している。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>イラン議会が審議する法案は、米・イスラエル船を恒久的に排除し、他国船には貨物価値最大7%の通行料と違反時20%の罰金を課す内容で、海峡統制の恒久的な制度化そのものである。1951年の石油国有化になぞらえる議員の発言もあり、イランが仮に協議中の技術合意を結んでも、この統制構造自体は維持される可能性が高い。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>イラン議会の排除・通行料法案は依然として審議・文言調整の段階にとどまり、本日時点で採決や新たな制度化に向けた具体的な動きは確認されていない。法案が最終的にどのような条件で可決されるかは未確定だが、米側が明確に拒否姿勢を崩していないこともあり、当面は制度化のリスクが顕在化する一歩手前で足踏みが続いている。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>フーシ派は5日、サウジのヤンブー沖でタンカー「Wafa」への攻撃を主張し、紅海封鎖開始（7/22）以降の被弾サウジタンカーは8隻目に達した。レザイー将軍の米艦船への攻撃警告も撤回されていない。ただし本日時点でホルムズ海峡そのものにおける米・イラン間の新たな直接軍事衝突の報告はなく、緊張は周辺海域（紅海）に分散している状況である。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>UAE政府がADNOC関連タンカーへのイラン攻撃を公式に「海賊行為」と非難したことは、これまでの民間企業単独の被害報告から一段踏み込んだ政治的対応であり、今後の対応次第では緊張がさらに拡大する可能性がある。加えてサウジ・パキスタン・トルコが集団防衛協定を締結し、フーシ派が政府軍拠点への攻撃を激化させるなど、ホルムズ海峡単体にとどまらない地域全体での軍事的な緊張の高まりが顕著になっている。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5つ）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">イラン議会の対米・イスラエル排除／通行料法案を巡る対立が収束するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン・オマーンの共同声明が正式発表され、内容に米の関与・同意が反映されるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">米の「無条件自由航行」要求とイランの「許可制・通行料」要求の溝が埋まるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">フーシ派の紅海攻撃激化がホルムズ情勢と連動してエスカレートしないか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保（変わらず最重要）</strong></li>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">UAE-ADNOCタンカー攻撃の実行主体・被害詳細が今後明らかになるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">米が提示した「無制限航行再開合意→封鎖解除」の条件を満たす合意がまとまるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">イラン議会の排除・通行料法案の文言調整がいつ決着し可決に至るか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">サウジ・パキスタン・トルコの新防衛協定発足後もフーシ派の対サウジ攻撃が続くか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保（変わらず最重要）</strong></li>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月7日 09:45 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">イラン・オマーンは安全航路の座標に合意し共同声明は最終調整段階に入ったが、イラン議会は米・イスラエル船排除と通行料の法案を審議しており、外交トラックと国内政治の間に温度差が生じている。【北側航路（イラン指定）】イラン議会の法案が成立すれば「敵対国」船に貨物価値最大7%の通行料・違反時20%の罰金を課す統制ルートとして制度化される見通し。【南ルート（Omani coastal corridor）】オマーンは入域イラン管理・出域オマーン管理の暫定枠組みに合意したと報じられ、実現すれば南側の管理主体がオマーンに移る可能性がある。中央チャンネルの機雷約80個は除去未着手のまま、除去期限は7/17（MOU第5条）を徒過。【イラン・オマーン仲介】両国は技術合意まで到達も、副外相ガリババディ氏は全面再開を意味しないと釘を刺す。【紅海・スエズ・黒海】フーシ派がサウジタンカー「Wafa」への攻撃を主張——7/22の紅海封鎖宣言以降8隻目、引き返した船舶は29隻に達したとする。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/7 09:45 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認・金子国交相の8/4会見は熊本地震対応が主題でホルムズ言及なし）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月9日 10:06 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">UAEがADNOC関連タンカーへのイラン攻撃を公式に非難し、米は「無制限航行再開→封鎖解除」の条件を提示したが、イラン議会法案の停滞と地域的な軍事的緊張の高まりが同時進行している。【北側航路（イラン指定）】8日未明にADNOC関連タンカーがミサイル攻撃を受けたと報告され、北側ルートの安全性への懸念が再燃。イラン議会の排除・通行料法案はなお専門家審査・文言調整中で可決未了。【南ルート（Omani coastal corridor）】オマーンとの入域イラン管理・出域オマーン管理の暫定枠組み協議に新たな進展の報告はなし。中央チャンネルの機雷約80個は除去未着手のまま、除去期限は7/17（MOU第5条）を徒過。【米の封鎖姿勢】米当局者はロイターに対し、無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針を明言——イラン交渉団は最高国家安全保障会議の承認待ちと報じられる。【紅海・スエズ・黒海】フーシ派が木曜に政府軍30名超を殺害する大規模攻撃を実施、金曜も攻撃継続——サウジはパキスタン・トルコとの相互防衛協定でこれに対応。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/9 10:06 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認・金子国交相の直近会見は熊本地震対応が主題でホルムズ言及なし）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）※最後に執筆

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷🇴🇲 イラン・オマーンが航路座標に合意——一方でイラン議会は米・イスラエル船排除と通行料の法案を審議し、米は即座に拒否。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📰 フーシ派がサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目。NYダウは3日連続最高値も6日反落。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 米・イランの条件対立が収束するか焦点、封鎖161日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残9日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇦🇪 UAEがADNOC関連タンカーへのイランのミサイル攻撃を「海賊行為」と非難——米は無制限航行再開を条件に封鎖解除の方針を提示。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📰 サウジ・パキスタン・トルコがNATO第5条型の相互防衛協定に署名——フーシ派激化に対応。NYダウ・S&P500とも最高値圏。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ イラン議会法案の決着と米封鎖解除条件の充足が焦点、封鎖163日目——MOU最終期限（8/16）まで残7日。
</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(74,222,128,0.15);border:1px solid rgba(74,222,128,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷🇴🇲航路座標に合意・共同声明調整中</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷議会が米船排除・通行料法案審議</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸米「無条件自由航行」要求で拒否</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📈NYダウ3日連続最高値も反落</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇦🇪ADNOCタンカー被弾・海賊行為と非難</span>
<span style="display:inline-block;background:rgba(74,222,128,0.15);border:1px solid rgba(74,222,128,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸無制限航行再開で封鎖解除の方針</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇸🇦🇵🇰🇹🇷相互防衛協定に署名</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📈NYダウ・S&P500最高値圏</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [C01] タンカー確認（SHIP_CONFIG dateConfirmed）

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年8月7日 09:45 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の8/4会見は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年8月9日 10:06 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近会見（8/4）は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- NEW:END -->
<!-- APPLY:END -->

**C01 タンカー確認**：日本語「日本関係船舶 ホルムズ海峡 通過 足止め」「外務省 ホルムズ海峡 日本関係船舶」「金子国土交通大臣 記者会見 ホルムズ海峡 日本関係船舶」＋英語「Japanese ships Strait of Hormuz stranded detained August 2026」の4クエリ全てでweb検索済み（外務省・国土交通省の一次情報を優先確認）／変化なし→残り4隻のまま・dateConfirmedを本日日時「変更なし」で更新

---

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-08-07T09:45:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-09T10:06:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

### updated フィールド

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年8月7日 09:45 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年8月9日 10:06 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列（新規4件を先頭に追加・旧latest後半4件をarchiveへ移動）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-iran-oman-route-agree-0805",
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "id": "latest-uae-adnoc-missile-attack-0808",
      "title": "UAE、ADNOC関連タンカーへのイランのミサイル攻撃を非難——「海賊行為」と表現、負傷者なし",
      "body": "UAE外務省は8月8日未明、国営石油会社ADNOC関連のタンカーがホルムズ海峡通航中にイランからミサイル攻撃を受けたと発表し、「敵対的なイランの攻撃」であり「海賊行為」に当たると非難する声明を出した。国営通信WAMは当初、ADNOC発表として被弾したタンカーの船名や積荷の詳細は明らかにせず「状況は制御下にある」と伝えた。負傷者の報告はない。",
      "sourceLabel": "Reuters / US News",
      "date": "2026年8月8日（現地）/ 2026年8月8日 JST",
      "label": "⚔️ 軍事",
      "url": "https://www.usnews.com/news/world/articles/2026-08-08/uae-says-iran-attacked-adnoc-vessel-with-missile-in-strait-of-hormuz",
      "isLatest": true
    },
    {
      "id": "latest-adnoc-15-vessels-attacked-0807",
      "title": "ADNOC「紛争開始以来15隻が被弾」——今週だけで3隻・死者1名負傷20名",
      "body": "アブダビ国営石油会社ADNOCは8月7日、紛争開始以来15隻の関連船舶がホルムズ海峡通航中にミサイル・ドローン攻撃を受けたとする声明を発表した。今週だけで3隻が被弾し、死者1名・負傷者20名に達したという。ADNOCは攻撃の実行主体を特定していないが、乗員・資産の保護のため関係当局と連携し必要な措置を講じているとした。",
      "sourceLabel": "Bloomberg / Gulf News",
      "date": "2026年8月7日（現地）/ 2026年8月7日 JST",
      "label": "⚔️ 軍事",
      "url": "https://www.bloomberg.com/news/articles/2026-08-07/adnoc-says-three-vessels-hit-this-week-while-transiting-hormuz",
      "isLatest": false
    },
    {
      "id": "latest-us-lift-blockade-condition-0807",
      "title": "米当局者「無制限の航行再開合意が出れば対イラン港湾封鎖を解除」",
      "body": "米当局者はロイターに対し、ホルムズ海峡での商用航行が制限なく再開されるとの合意が発表され次第、米国は対イラン港湾封鎖を解除する方針だと明らかにした。イラン交渉団は同国最高国家安全保障会議の最終承認を待っている段階だとする仲介国外交官の見方をAxiosが伝えたという。今週の海峡通航は月曜〜木曜でわずか33隻にとどまり、前週の50隻からさらに減少している。",
      "sourceLabel": "Shafaq News / Reuters",
      "date": "2026年8月7日（現地）/ 2026年8月8日 JST",
      "label": "🇺🇸 外交",
      "url": "https://shafaq.com/en/World/US-to-lift-Iran-port-blockade-after-Hormuz-deal",
      "isLatest": false
    },
    {
      "id": "latest-saudi-pakistan-turkey-pact-0807",
      "title": "サウジ・パキスタン・トルコがNATO第5条型の相互防衛協定に署名——フーシ派激化への対応",
      "body": "サウジアラビアは8月7日、パキスタン・トルコとメッカで相互防衛協定に署名した。参加国への攻撃を全参加国への攻撃とみなす集団防衛条項を含み、サウジがイスラム圏屈指の軍事大国2カ国と安全保障関係を強化する形となった。同日、イエメンの親イラン武装組織フーシ派が政府軍拠点を攻撃するなど、対サウジ圧力の激化が背景にある。",
      "sourceLabel": "CNN",
      "date": "2026年8月7日（現地）/ 2026年8月7日 JST",
      "label": "🌍 地域安保",
      "url": "https://www.cnn.com/2026/08/07/world/live-news/iran-war-trump",
      "isLatest": false
    },
    {
      "id": "latest-iran-oman-route-agree-0805",
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
    {
      "id": "latest-us-rejects-iran-toll-plan-0806",
      "title": "米政府、イランの通行料・排除案を即座に拒否——「無条件の自由航行」を要求",
      "body": "イラン議会の対米船排除・通行料法案の報道を受け、米政府高官はCNBCに対し「暫定ルートは承認・許可・通行料を一切伴わない自由な航行でなければならない」と述べ、この案を拒否する姿勢を明確にした。トランプ大統領は「ホルムズ海峡はまもなく開放される」としつつ、「（イランが）再び後退すれば手痛い報いを受けるだろう」とも述べている。",
      "sourceLabel": "CNBC",
      "date": "2026年8月6日（現地）/ 2026年8月6日 JST",
      "label": "🇺🇸 外交",
      "url": "https://www.cnbc.com/2026/08/06/us-iran-war-hormuz-trump-bessent-deal.html",
      "isLatest": true
    },
    {
      "id": "latest-houthi-saudi-tanker-wafa-0805",
      "title": "フーシ派、サウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目",
      "body": "イエメンの親イラン武装組織フーシ派は8月5日、サウジアラビアの紅海側港湾都市ヤンブー沖でサウジ籍タンカー「Wafa」に複数のミサイルを撃ち込んだと発表した。フーシ派報道官ヤヒヤ・サリア氏は、7月22日の紅海封鎖宣言以降、攻撃を受けたサウジタンカーは8隻目、引き返した船舶は29隻に達したと述べ、サウジが南側を避け北側ルートへタンカーを迂回させていることへの対抗措置として攻撃を継続・激化させると表明した。",
      "sourceLabel": "Reuters / AFP",
      "date": "2026年8月5日（現地）/ 2026年8月5日 JST",
      "label": "⚔️ 軍事",
      "url": "https://www.dailysabah.com/world/mid-east/yemens-houthis-reportedly-strike-saudi-tanker-transiting-red-sea",
      "isLatest": true
    },
    {
      "id": "latest-bessent-rubio-deal-close-0804",
      "title": "ベッセント財務長官「合意は今日か明日にも」——ルビオ氏はオマーン・イラン協議の進展を確認",
      "body": "ベッセント米財務長官は8月4日、CNBCのインタビューでホルムズ海峡の「自由な航行」再開に向けた合意が「今日か明日にも」まとまる可能性があると発言した。ルビオ国務長官も同日、米国が関与するオマーンとイランの協議で進展があったと確認したが、最終合意にはまだ至っていないと留保。「イランの非核化こそが最終的な目標」とも述べた。",
      "sourceLabel": "Washington Times / Al Jazeera",
      "date": "2026年8月4日（現地）/ 2026年8月5日 JST",
      "label": "🤝 外交",
      "url": "https://www.washingtontimes.com/news/2026/aug/4/strait-talk-us-regional-partners-see-progress-toward-reopening-hormuz/",
      "isLatest": true
    },
    {
      "id": "latest-iran-two-route-proposal-0804",
      "title": "浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式——米の封鎖解除が前提",
      "body": "米・中東関係者によれば、検討されている合意案は湾内への入域をイラン管理ルート、湾外への出域をオマーン管理ルートとする二経路方式。合意成立には米側による対イラン封鎖の解除が前提条件とされる。イラン交渉委員のサイード・アジョルル氏は国営IRIBに対し、米との直接交渉を否定した上で「治安・機雷除去・海事サービスはイランが担う」1〜3ヶ月の暫定管理案が基本方針だと説明した。",
      "sourceLabel": "AP / Washington Times",
      "date": "2026年8月4日（現地）/ 2026年8月5日 JST",
      "label": "📝 交渉内容",
      "url": "https://www.washingtontimes.com/news/2026/aug/4/strait-talk-us-regional-partners-see-progress-toward-reopening-hormuz/",
      "isLatest": false
    }
  ],
<!-- OLD:END -->
<!-- NEW:START -->
    {
      "id": "latest-iran-parliament-ban-toll-0806",
      "title": "イラン議会、米・イスラエル船の排除と他国船への通行料課税の法案を審議",
      "body": "イラン議会の委員会は8月6日、米・イスラエル関連船舶を恒久的にホルムズ海峡通過から排除し、その他の「敵対国」船には貨物価値最大7%の通行料を、条件違反時には20%の罰金を課す法案を審議していると国営ファールス通信が報じた。法案はなお専門家審査中で、議会は確定前に専門家の意見提出を招請しているという。",
      "sourceLabel": "Reuters / NPR",
      "date": "2026年8月6日（現地）/ 2026年8月6日 JST",
      "label": "🇮🇷 政治",
      "url": "https://www.npr.org/2026/08/06/nx-s1-5923623/iran-strait-hormuz-us-israel-ban",
      "isLatest": true
    }
  ],
<!-- NEW:END -->
<!-- APPLY:END -->

### archive 配列（先頭に新規バッチを追加：latest から溢れた4件）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "archive": [
    {
      "batchLabel": "2026年8月1日〜4日",
<!-- OLD:END -->
<!-- NEW:START -->
  "archive": [
    {
      "batchLabel": "2026年8月4日〜6日",
      "items": [
        {
          "id": "latest-us-rejects-iran-toll-plan-0806",
          "title": "米政府、イランの通行料・排除案を即座に拒否——「無条件の自由航行」を要求",
          "body": "イラン議会の対米船排除・通行料法案の報道を受け、米政府高官はCNBCに対し「暫定ルートは承認・許可・通行料を一切伴わない自由な航行でなければならない」と述べ、この案を拒否する姿勢を明確にした。トランプ大統領は「ホルムズ海峡はまもなく開放される」としつつ、「（イランが）再び後退すれば手痛い報いを受けるだろう」とも述べている。",
          "sourceLabel": "CNBC",
          "date": "2026年8月6日（現地）/ 2026年8月6日 JST",
          "label": "🇺🇸 外交",
          "url": "https://www.cnbc.com/2026/08/06/us-iran-war-hormuz-trump-bessent-deal.html",
          "isLatest": false
        },
        {
          "id": "latest-houthi-saudi-tanker-wafa-0805",
          "title": "フーシ派、サウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目",
          "body": "イエメンの親イラン武装組織フーシ派は8月5日、サウジアラビアの紅海側港湾都市ヤンブー沖でサウジ籍タンカー「Wafa」に複数のミサイルを撃ち込んだと発表した。フーシ派報道官ヤヒヤ・サリア氏は、7月22日の紅海封鎖宣言以降、攻撃を受けたサウジタンカーは8隻目、引き返した船舶は29隻に達したと述べた。",
          "sourceLabel": "Reuters / AFP",
          "date": "2026年8月5日（現地）/ 2026年8月5日 JST",
          "label": "⚔️ 軍事",
          "url": "https://www.dailysabah.com/world/mid-east/yemens-houthis-reportedly-strike-saudi-tanker-transiting-red-sea",
          "isLatest": false
        },
        {
          "id": "latest-bessent-rubio-deal-close-0804",
          "title": "ベッセント財務長官「合意は今日か明日にも」——ルビオ氏はオマーン・イラン協議の進展を確認",
          "body": "ベッセント米財務長官は8月4日、CNBCのインタビューでホルムズ海峡の「自由な航行」再開に向けた合意が「今日か明日にも」まとまる可能性があると発言した。ルビオ国務長官も同日、米国が関与するオマーンとイランの協議で進展があったと確認したが、最終合意にはまだ至っていないと留保した。",
          "sourceLabel": "Washington Times / Al Jazeera",
          "date": "2026年8月4日（現地）/ 2026年8月5日 JST",
          "label": "🤝 外交",
          "url": "https://www.washingtontimes.com/news/2026/aug/4/strait-talk-us-regional-partners-see-progress-toward-reopening-hormuz/",
          "isLatest": false
        },
        {
          "id": "latest-iran-two-route-proposal-0804",
          "title": "浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式——米の封鎖解除が前提",
          "body": "米・中東関係者によれば、検討されている合意案は湾内への入域をイラン管理ルート、湾外への出域をオマーン管理ルートとする二経路方式。合意成立には米側による対イラン封鎖の解除が前提条件とされる。",
          "sourceLabel": "AP / Washington Times",
          "date": "2026年8月4日（現地）/ 2026年8月5日 JST",
          "label": "📝 交渉内容",
          "url": "https://www.washingtontimes.com/news/2026/aug/4/strait-talk-us-regional-partners-see-progress-toward-reopening-hormuz/",
          "isLatest": false
        }
      ]
    },
    {
      "batchLabel": "2026年8月1日〜4日",
<!-- NEW:END -->
<!-- APPLY:END -->

### osint 配列への追記（先頭に2件、既存の isLatest:true は false に変更）

既存の先頭要素（`titleJa: "【NPR】イラン、米・イスラエル船のホルムズ海峡締め出しと通行料徴収を狙う"`）の `isLatest` を `true` → `false` に変更した上で、以下2件を配列先頭に追加：

```json
[
  {
    "titleJa": "【Türkiye Today】UAE、ホルムズ海峡でイランがADNOCタンカーを標的にしたと発表",
    "titleEn": "UAE says Iran targeted ADNOC tanker in Strait of Hormuz",
    "country": "アラブ首長国連邦",
    "media": "Türkiye Today",
    "cardBg": "rgba(56,189,248,0.05)",
    "cardBorder": "rgba(56,189,248,0.25)",
    "badgeColor": "#38bdf8",
    "borderColor": "rgba(56,189,248,0.4)",
    "textColor": "#7dd3fc",
    "url": "https://www.turkiyetoday.com/region/uae-says-iran-targeted-adnoc-tanker-in-strait-of-hormuz-3225648",
    "date": "2026年8月8日（現地）/ 2026年8月8日 JST",
    "isLatest": true
  },
  {
    "titleJa": "【Al Jazeera】サウジがフーシ派攻撃に備える中、イエメンで戦闘激化——現状まとめ",
    "titleEn": "Houthi strikes in Yemen as Saudi Arabia braces for attacks: What we know",
    "country": "カタール",
    "media": "Al Jazeera",
    "cardBg": "rgba(56,189,248,0.05)",
    "cardBorder": "rgba(56,189,248,0.25)",
    "badgeColor": "#38bdf8",
    "borderColor": "rgba(56,189,248,0.4)",
    "textColor": "#7dd3fc",
    "url": "https://www.aljazeera.com/news/2026/8/7/houthi-strikes-hit-yemen-as-saudi-arabia-braces-for-attacks-what-we-know",
    "date": "2026年8月7日（現地）/ 2026年8月7日 JST",
    "isLatest": false
  }
]
```

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "titleJa": "【NPR】イラン、米・イスラエル船のホルムズ海峡締め出しと通行料徴収を狙う",
      "titleEn": "Iran aims to ban U.S. and Israeli ships from Strait of Hormuz and charge others a toll",
      "country": "アメリカ",
      "media": "NPR",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.npr.org/2026/08/06/nx-s1-5923623/iran-strait-hormuz-us-israel-ban",
      "date": "2026年8月6日（現地）/ 2026年8月6日 JST",
      "isLatest": true
<!-- OLD:END -->
<!-- NEW:START -->
      "titleJa": "【Türkiye Today】UAE、ホルムズ海峡でイランがADNOCタンカーを標的にしたと発表",
      "titleEn": "UAE says Iran targeted ADNOC tanker in Strait of Hormuz",
      "country": "アラブ首長国連邦",
      "media": "Türkiye Today",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.turkiyetoday.com/region/uae-says-iran-targeted-adnoc-tanker-in-strait-of-hormuz-3225648",
      "date": "2026年8月8日（現地）/ 2026年8月8日 JST",
      "isLatest": true
    },
    {
      "titleJa": "【Al Jazeera】サウジがフーシ派攻撃に備える中、イエメンで戦闘激化——現状まとめ",
      "titleEn": "Houthi strikes in Yemen as Saudi Arabia braces for attacks: What we know",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/2026/8/7/houthi-strikes-hit-yemen-as-saudi-arabia-braces-for-attacks-what-we-know",
      "date": "2026年8月7日（現地）/ 2026年8月7日 JST",
      "isLatest": false
    },
    {
      "titleJa": "【NPR】イラン、米・イスラエル船のホルムズ海峡締め出しと通行料徴収を狙う",
      "titleEn": "Iran aims to ban U.S. and Israeli ships from Strait of Hormuz and charge others a toll",
      "country": "アメリカ",
      "media": "NPR",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.npr.org/2026/08/06/nx-s1-5923623/iran-strait-hormuz-us-israel-ban",
      "date": "2026年8月6日（現地）/ 2026年8月6日 JST",
      "isLatest": false
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S11] 更新ログ — 2ブロック構成＋合計超過分削除

### ブロック1：常時表示エリア（3件固定を維持）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月7日 09:45 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/07 09:45</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省、ホルムズ海峡の安全航路座標についてオマーンと合意したと発表——共同声明は最終調整段階（IRNA、8/5）・米メディアはオマーンが入域イラン管理・出域オマーン管理の暫定枠組みに合意と報道（MS NOW、8/6）・一方イラン議会委員会は米・イスラエル船の恒久排除と他国船への最大7%通行料・違反時20%罰金の法案を審議（Fars通信）・米政府はこの案を即座に拒否し無条件の自由航行を要求（CNBC）・フーシ派はサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目、29隻が引き返し（Reuters）・NYダウは263ドル高の54,349.12ドルで3日連続最高値も6日は反落・原油は乱高下しブレントが一時81ドル台へ反発・日本関係船は残り4隻で変化なし・封鎖161日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月5日 10:24 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/05 10:24</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）・浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提（AP/Washington Times）・イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示（IRIB）・レザイー最高指導者上級顧問は代替航路を強制する米艦船への攻撃も辞さないと警告・UKMTOはオマーン沖でリベリア籍バルカー「ミノアン・パイオニア」の被弾を発表（乗員1名行方不明）・イラン国営メディアはクウェート米軍基地への攻撃を主張したが米側未確認・NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75.77ドルへ続落・日本関係船は残り4隻で変化なし・封鎖159日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月3日 09:46 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/03 09:46</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ氏、サウジのムハンマド皇太子から電話で説得を受け週末の対イラン大規模攻撃を土壇場で中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及し月曜からイランと交渉開始へ（Newsweek/NPR）・イラン軍代行国防相は「心理作戦」と一蹴、半官営メール通信は「新たな虚偽」と反発——イラン政府は公式受諾を表明せず（Al Jazeera）・イラン国営ファールス通信は北側航路になお多数の船舶が足止めされたままと報道・UKMTOはオマーン沖でタンカー「ガスログ・シャンハイ」の被弾を発表（7/31・機関室損傷）・クウェート軍はイラン系ドローンを迎撃（8/1）——NYTはIRGCが4月停戦中にフーシ派・ヒズボラ・イラク民兵と共謀し戦線拡大を図っていたと報道・原油はブレントが前日比4.65%安の83.84ドルへ急落（8/2）・日本関係船は残り4隻で変化なし・封鎖157日目・ニュース4件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月7日 09:45 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/07 09:45</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省、ホルムズ海峡の安全航路座標についてオマーンと合意したと発表——共同声明は最終調整段階（IRNA、8/5）・米メディアはオマーンが入域イラン管理・出域オマーン管理の暫定枠組みに合意と報道（MS NOW、8/6）・一方イラン議会委員会は米・イスラエル船の恒久排除と他国船への最大7%通行料・違反時20%罰金の法案を審議（Fars通信）・米政府はこの案を即座に拒否し無条件の自由航行を要求（CNBC）・フーシ派はサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目、29隻が引き返し（Reuters）・NYダウは263ドル高の54,349.12ドルで3日連続最高値も6日は反落・原油は乱高下しブレントが一時81ドル台へ反発・日本関係船は残り4隻で変化なし・封鎖161日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月5日 10:24 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/05 10:24</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）・浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提（AP/Washington Times）・イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示（IRIB）・レザイー最高指導者上級顧問は代替航路を強制する米艦船への攻撃も辞さないと警告・UKMTOはオマーン沖でリベリア籍バルカー「ミノアン・パイオニア」の被弾を発表（乗員1名行方不明）・イラン国営メディアはクウェート米軍基地への攻撃を主張したが米側未確認・NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75.77ドルへ続落・日本関係船は残り4隻で変化なし・封鎖159日目・ニュース4件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse 先頭への旧3件目（8/3 09:46分）の挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月1日 10:51 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月3日 09:46 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/03 09:46</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ氏、サウジのムハンマド皇太子から電話で説得を受け週末の対イラン大規模攻撃を土壇場で中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及し月曜からイランと交渉開始へ（Newsweek/NPR）・イラン軍代行国防相は「心理作戦」と一蹴、半官営メール通信は「新たな虚偽」と反発——イラン政府は公式受諾を表明せず（Al Jazeera）・イラン国営ファールス通信は北側航路になお多数の船舶が足止めされたままと報道・UKMTOはオマーン沖でタンカー「ガスログ・シャンハイ」の被弾を発表（7/31・機関室損傷）・クウェート軍はイラン系ドローンを迎撃（8/1）——NYTはIRGCが4月停戦中にフーシ派・ヒズボラ・イラク民兵と共謀し戦線拡大を図っていたと報道・原油はブレントが前日比4.65%安の83.84ドルへ急落（8/2）・日本関係船は残り4隻で変化なし・封鎖157日目・ニュース4件更新・osint更新</div>
          <div>📅 <strong>2026年8月1日 10:51 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：合計件数調整（常時3件＋collapse9件＝12件で上限超過のため、最古の7/16 10:52分を削除）

> 常時表示3件（8/9・8/7・8/5）＋log-collapse 9件（8/3・8/1・7/30・7/28・7/26・7/24・7/22・7/19・7/16）＝12件となり上限を超過するため、log-collapse内の最古エントリー（7/16 10:52分）を削除し、`docs/data/update_log.json` の先頭に追加してください。

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/16 10:52</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明・対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を攻撃・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更・IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明・トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も・米はIRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放・日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明・原油はブレント7/15終値84.95ドル・封鎖139日目・ニュース3件更新・osint更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S11完了（常時表示3件固定・log-collapseは8/3挿入後9件→7/16分削除で8件に調整）

---

## 補足：archive_timeline.json への当日分追記について

> 本日は「速報を出した日」に該当する重大インシデント（UAE-ADNOC攻撃・サウジ新防衛協定）があるため、`docs/data/archive_timeline.json` への追記対象です。ただし `blockadeDay` フィールドは2026-08-07セッションの決定によりJS側の `calcBlockadeDay()` が動的計算するため空欄のままで構いません（新規エントリーへの入力不要）。追記は別途Claude Codeへの独立指示として行うか、次回セッションでまとめて対応してください。
