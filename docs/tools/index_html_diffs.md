# index_html_diffs.md — 2026年8月11日 09:26 JST 更新分

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
[ ] S10 news_data.json（latest4件追加・archive移動・osint1件追記）
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
[x] S01 ― 更新済み（レザイー氏SNSC新書記就任・逆賠償要求・高市=ハイサム電話会談・フーシ派モカ攻撃を要約統合）
[x] S02 ― 更新済み（8項目の速報箇条書き、S01とは異なる短文形式）
[x] S03 ― 更新済み（トグル日付・strong本文・リスト先頭2件を時系列詳細形式で追加）
[x] S04 ― 更新済み（①SNSC体制交代＋逆賠償応酬 ②フーシ派モカ攻撃・イエメン内戦拡大 ③高市=オマーン電話会談＋市場動向、の3カード個別深掘り）
[x] S05 ― 更新済み（Phase21・dl-note運用視点で要約、MOU残5日を明記）
[x] S06 ― 更新済み（①②両方の日付を2026年8月11日 09:26 JSTに統一、方向性を分析的に記述）
[x] S07 ― 更新済み（4本とも本文をSNSC体制交代・逆賠償要求を軸に差し替え）
[x] S08 ― 更新済み（次の焦点5点を本日情勢に刷新）
[x] S08.5 ― 更新済み（ルート実務影響の切り口で記載・S08完了後・S09直前に配置）
[x] S09 ― 更新済み（3行サマリー＋バッジ5枚、最後に作成）
[x] S10 ― 更新済み（latest4件追加・archiveへ4件移動・osint1件追記）
[x] S11 ― 更新済み（2ブロック構成・常時表示3件維持・合計12件のため最古1件削除）
[x] JSON-LD dateModified ― 2026-08-11に更新済み
[x] C01 ― 日本語3クエリ（①日本関係船舶 ホルムズ海峡 通過 足止め ②外務省 ホルムズ海峡 日本関係船舶 ③金子国土交通大臣 記者会見 ホルムズ海峡 日本関係船舶）＋英語1クエリ（Japanese ships Strait of Hormuz stranded detained August 2026）を個別実行。外務省・国交省の新規発表なしを確認。金子国交相の直近会見（8/4）は熊本地震対応が主題でホルムズ言及なし。→ 残り4隻・変化なしを維持
[x] 日付表記 ― 全箇所「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一
[x] ニュースURL ― 全てweb検索で実在確認済み（Reuters/NBC/Time/Euronews/AP/CBS News/日テレNEWS/Al Jazeera(osint限定)等）、AI捏造URLなし
[x] Al Jazeera ― 📰関連最新ニュース（latest/archive）には不使用。🌐現地メディア視点（osint）のみに使用
[x] 禁止ソース ― 毎日新聞・Wikipedia・TBS/TBS NEWS DIG・朝日・NHK・東京新聞・テレビ朝日、いずれも混入なし（毎日新聞記事は確認のみに使用し出典・URLとしては不使用、代わりに日テレNEWS(infoseek)を採用）
[x] 人名表記 ― トランプ（大統領）、高市（早苗首相）、ハイサム（オマーン国王）、モフセン・レザイー、ゾルガドル、アラグチー、いずれも日本語表記で統一・「Xi」「Trump」単独表記なし
[x] シナリオC・D ― CはイラN議会法案（依然審議中・可決未了）の停滞継続、DはSNSC新書記の対米強硬姿勢継続とイエメン内戦拡大という新規の緊張材料で差別化
[x] セクション重複回避 ― ①SNSC体制交代＋6条件継承 ②トランプ逆賠償要求 ③イラン・オマーン協議の位置づけ ④高市=オマーン電話会談 ⑤フーシ派モカ攻撃・イエメン内戦拡大 ⑥市場動向（ブレント続伸・米株小反落）の6つの材料を、S01(概観)・S02(箇条書き速報)・S03(詳細経緯＋出典)・S04(3カード個別深掘り)・S08.5(ルート別実務影響)・S09(3行超要約)でそれぞれ異なる切り口・文体で記載
```

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（UAE政府、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「海賊行為」と非難・負傷者なし／ADNOCは紛争開始以来15隻が被弾・今週だけで3隻・死者1名負傷20名と発表／米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明／イラン議会の米・イスラエル船排除・通行料法案はなお文言調整中で可決未了／サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応／NYダウ・S&P500とも最高値圏、ブレント83.55ドル／封鎖163日目）</span>
    <span class="badge-item badge-date">📅2026年8月9日 10:06 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イラン最高国家安全保障会議の書記がゾルガドル氏からモフセン・レザイー氏（革命防衛隊元司令官・対米強硬派）に交代、前書記が示した6条件（脅迫停止・戦争終結・封鎖解除と米軍撤収・戦争賠償・制裁解除・資産凍結解除）は継承／トランプ大統領はイランの賠償要求に「同様の賠償」を求めると応酬し対話は一段と硬直化／高市首相は10日、オマーンのハイサム国王と電話会談し追加費用のない自由で安全な航行の早期回復を要請／フーシ派は紅海の要衝モカを2日連続攻撃し7人死亡・30人負傷、イエメン内戦拡大の懸念／ブレント原油は87.72ドルへ4日続伸、NYダウ・S&P500は最高値圏から小反落／封鎖165日目）</span>
    <span class="badge-item badge-date">📅2026年8月11日 09:26 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月9日 10:06 JST） -->
      🇦🇪【ADNOCタンカー再び被弾】UAE政府、8日未明のイランによるミサイル攻撃を「敵対的行為」「海賊行為」と非難——負傷者なし・状況は制御下（Reuters、8/8）｜📊 ADNOC：紛争開始以来15隻が被弾、今週だけで3隻——死者1名・負傷者20名（Bloomberg/Gulf News、8/7）｜🇺🇸【封鎖解除の条件提示】米当局者、無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除すると表明——イラン交渉団は最高国家安全保障会議の最終承認待ちとの報道も（Shafaq News、8/7〜8）｜🇮🇷 イラン議会の排除・通行料法案はなお文言調整中——可決には至らず｜🇸🇦🇵🇰🇹🇷【NATO型防衛協定】サウジ・パキスタン・トルコがメッカで相互防衛協定に署名——フーシ派の対サウジ攻撃激化への対応（CNN、8/7）｜🐹 フーシ派、木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷｜📈 NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、ブレントは83.55ドル(+1.29%)｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英4クエリで再確認・金子国交相直近会見は熊本地震対応が主題）｜封鎖163日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月11日 09:26 JST） -->
      🇮🇷【SNSC体制交代】イラン最高国家安全保障会議の書記がゾルガドル氏からレザイー氏（対米強硬派・革命防衛隊元司令官）へ交代——ゾルガドル氏はハメネイ師政治顧問に転身（9日、NBC）｜🚫 IRGC報道官「イランの条件を米が飲めば必ず開放」——海峡再開はオマーン協議とは別問題と明言｜🇺🇸【逆賠償要求】トランプ氏、イランの賠償要求に「同様に賠償を求める」と反発——USSコール事件等も含め対抗要求（10日、Euronews）｜🇴🇲 高市首相、オマーン国王と電話会談——追加費用のない自由で安全な航行の早期回復を要請（10日）｜🐹 フーシ派、紅海の要衝モカを日曜夜・月曜と2日連続攻撃——7人死亡30人負傷、タイズ近郊で衝突継続｜📈 ブレント87.72ドルへ4日続伸(+4.95%)、NYダウ53,975.98ドル・S&P500は7,753.11ドルで小反落｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英4クエリで再確認）｜封鎖165日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

### トグルボタン内の日付バッジ・見出し

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">UAE、イランによるADNOCタンカーへのミサイル攻撃を非難——米は無制限航行再開を条件に対イラン封鎖解除の方針、サウジは新防衛協定で対抗</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/9 10:06 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">イランSNSC書記が対米強硬派レザイー氏に交代、トランプは逆賠償要求で応酬——高市首相はオマーン国王に自由航行の回復要請</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/11 09:26 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/9 10:06 速報】UAE外務省は8日、国営石油会社ADNOC関連のタンカーが同日未明にホルムズ海峡通航中にイランからミサイル攻撃を受けたと発表し、「敵対的なイランの攻撃」「海賊行為」と非難した。国営通信WAMは当初ADNOCの発表として「状況は制御下にある」と伝え、負傷者は報告されていない（Reuters）｜これに先立ちADNOCは7日、紛争開始以来15隻の関連船舶がミサイル・ドローンで攻撃を受け、今週だけで3隻が被弾、死者1名・負傷者20名に上ると発表していた（Bloomberg/Gulf News）｜米当局者はロイターに対し、ホルムズ海峡での商用航行が制限なく再開される合意が発表され次第、対イラン港湾封鎖を解除する方針を明らかにした。イラン交渉団は同国最高国家安全保障会議の最終承認を待っている状態とAxiosが報じたという（Shafaq News）｜イラン議会の米・イスラエル船排除・通行料法案は依然文言調整中で可決には至っていない｜サウジアラビアは7日、パキスタン・トルコとメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化を受けた動き（CNN）｜フーシ派は木曜に少なくとも30名の政府軍兵士を殺害する大規模攻撃を実施、金曜も攻撃を継続しマリブで民間人2名が死亡・14名が負傷した｜市場ではNYダウ・S&P500がともに最高値圏を維持、原油はブレントが83.55ドルまで上昇｜日本関係船は残り4隻で変化なし｜封鎖163日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/11 09:26 速報】イラン最高国家安全保障会議は9日、書記をモフセン・レザイー氏（革命防衛隊元司令官・対米強硬派）に交代——前書記ゾルガドル氏はハメネイ師の政治顧問に転じた。米シンクタンクISWは、レザイー氏がホルムズ海峡の管理権を含む最大限の要求実現を志向する一方、譲歩には消極的とみる（NBC）｜イラン外務省報道官バガイ氏は10日、ゾルガドル氏が8日に示した6条件（脅迫停止・戦争終結・海上封鎖解除と米軍撤収・戦争賠償・制裁解除・資産凍結解除）を改めて確認した（Time）｜トランプ大統領は10日、イランの賠償要求を一蹴し「同様に賠償を求める」と表明——2000年のUSSコール事件やイラン国内デモ弾圧の犠牲者への補償も対象に含める考えを示した（Euronews）｜高市首相は10日、オマーンのハイサム国王と約20分間電話会談——「追加的費用のない形での自由で安全な航行の一刻も早い回復」を要請し、海峡利用国を含む国際社会との協議をハイサム国王から確約された｜フーシ派は9日夜・10日と紅海の要衝モカを2日連続攻撃——政府軍関係者4人・民間人3人の計7人が死亡、30人が負傷、タイズ近郊でも衝突が続く（AP）｜市場ではブレント原油が87.72ドルへ4日続伸する一方、NYダウは53,975.98ドル（-0.11%）・S&P500は7,753.11ドル（-0.06%）と最高値圏から小反落——米戦略石油備蓄は1983年以来の低水準に落ち込んだ（Reuters）｜日本関係船は残り4隻で変化なし｜封鎖165日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に2件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇦🇪 8/8 JST（現地未明）</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇮🇷 8/9〜10 JST</span>
  <span style="color:#e2e8f0;"> イラン最高国家安全保障会議の書記がゾルガドル氏からモフセン・レザイー氏（革命防衛隊元司令官・1981〜97年在任、対米強硬派）に交代したと発表された。ゾルガドル氏はハメネイ師（モジュタバ師）の政治顧問に転じる。米シンクタンクISWはレザイー氏について、ホルムズ海峡の管理権を含むイランの最大限の要求実現を志向する一方、具体的な譲歩案の提示には消極的と分析。トランプ大統領は10日、イランの戦争賠償要求に対し「同様の賠償を求める」とSNSに投稿し、2000年のUSSコール事件やイラン国内デモ弾圧犠牲者への補償も交渉に含めるよう指示したと明らかにした（NBC/Euronews）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🐹 8/9夜〜10 JST</span>
  <span style="color:#e2e8f0;"> イエメンのフーシ派が紅海沿岸の政府軍支配下の港町モカを日曜夜と月曜の2日連続で攻撃し、少なくとも7人（政府軍関係者4人・民間人3人）が死亡、30人が負傷した。フーシ派側は13歳の子どもが砲撃で死亡したと発表。タイズ近郊でも衝突が継続しており、マリブ・ハドラマウト両州での大規模攻撃（8/6〜7）に続くイエメン内戦の再燃・拡大が懸念されている（AP）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇦🇪 8/8 JST（現地未明）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

<!-- APPLY:START -->
<!-- OLD:START -->
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
<!-- OLD:END -->
<!-- NEW:START -->
<!-- カード① 外交・体制 -->
  <div class="sit-card danger">
    <div class="s-icon">🇮🇷</div>
        <div class="s-title">🇮🇷 SNSC書記が対米強硬派レザイー氏に交代——トランプは逆賠償要求で応酬し対話は硬直化</div>
        <div class="s-body">イラン最高国家安全保障会議（SNSC）は9日、書記をゾルガドル氏から革命防衛隊元司令官（1981〜97年在任）のモフセン・レザイー氏に交代させた。ゾルガドル氏は最高指導者モジュタバ・ハメネイ師の政治顧問に転じる。米シンクタンクISWは、レザイー氏がホルムズ海峡の管理権を含むイランの最大限の要求実現を志向する一方、具体的な譲歩には消極的だと分析する。ゾルガドル氏が8日に示した6条件（脅迫停止・戦争終結・海上封鎖解除と米軍撤収・戦争賠償・制裁解除・資産凍結解除）は新体制下でも継承され、外務省報道官バガイ氏も10日、改めてこれを確認した。トランプ大統領は同日、イランの賠償要求に「同様の賠償を求める」と反発し、2000年のUSSコール事件やイラン国内デモ弾圧の犠牲者への補償も対象に含める考えを示した。</div>
        <div class="s-src">出典: NBC News / Time / Euronews（8/9〜10 JST 更新）</div>
  </div>

  <!-- カード② 地域安保 -->
  <div class="sit-card warning">
    <div class="s-icon">🐹</div>
        <div class="s-title">🐹 フーシ派、紅海の要衝モカを2日連続攻撃——イエメン内戦拡大の懸念強まる</div>
        <div class="s-body">イラン系フーシ派は9日夜と10日、紅海沿岸の政府軍支配下の港町モカを2日連続で攻撃し、少なくとも7人（政府軍関係者4人・民間人3人）が死亡、30人が負傷した。フーシ派側は13歳の子どもが砲撃で死亡したと発表している。中部・東部のマリブ・ハドラマウト両州でも6日にフーシ派が政府軍拠点を攻撃し30人超が死亡、政府軍側も8日に複数戦線で反撃を実施しており、タイズ近郊でも衝突が続く。専門家は2022年停戦が事実上失効した状態にあり、全面的なイエメン内戦再燃の「差し迫った可能性」を指摘している。</div>
        <div class="s-src">出典: AP / The National / Al Jazeera（8/6〜10 JST 更新）</div>
  </div>

  <!-- カード③ 日本外交・市場 -->
  <div class="sit-card info">
    <div class="s-icon">🇯🇵</div>
        <div class="s-title">🇯🇵 高市首相、オマーン国王と電話会談——自由航行の早期回復を要請、原油は続伸</div>
        <div class="s-body">高市早苗首相は10日夕、オマーンのハイサム国王と約20分間電話会談し、「追加的費用のない形での自由で安全な航行の一刻も早い回復」の重要性を伝え、海峡利用国を含む国際社会との協議を求めた。ハイサム国王からは、海峡利用国と協議することを確約し各国の意思も尊重する考えが示された。両首脳の電話会談は4月以来2回目。市場では、イランの対米強硬姿勢継続を受けブレント原油が87.72ドル（前日比+4.95%）へ4日続伸し、米戦略石油備蓄は1983年以来の低水準（3億バレル割れ）に落ち込んだ一方、NYダウは53,975.98ドル（-0.11%）・S&P500は7,753.11ドル（-0.06%）と最高値圏からわずかに反落した。</div>
        <div class="s-src">出典: 日テレNEWS（infoseek）/ TradingEconomics / Reuters（8/10 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN（phase-label ＋ dl-note）

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 20「UAEがADNOCタンカーへのイラン攻撃を非難、米は封鎖解除の条件提示——サウジは新防衛協定で応戦態勢」——封鎖163日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 21「イランSNSC書記が対米強硬派レザイー氏に交代、トランプは逆賠償要求で応酬——高市首相はオマーン国王に自由航行回復を要請」——封鎖165日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🤝 <strong>UAE外務省が8日未明のADNOC関連タンカーへのイラン攻撃を「海賊行為」と非難（負傷者なし）／ADNOCは紛争開始以来15隻被弾・死者1名負傷20名と発表（8/7）／米当局者は無制限の航行再開合意が出れば対イラン封鎖を解除すると表明、イラン交渉団は最高国家安全保障会議の承認待ちとの報道（8/7〜8）／イラン議会の排除・通行料法案はなお文言調整中で可決未了／サウジ・パキスタン・トルコがNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（8/7）／日本関係船は残り4隻で変化なし——封鎖163日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残7日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①UAE-ADNOC攻撃の実行主体・被害の詳細が明らかになるか ②米の「無制限航行再開→封鎖解除」条件を満たす合意がまとまるか ③イラン議会の排除・通行料法案の文言調整がいつ決着するか ④サウジ新防衛協定発足後もフーシ派の対サウジ攻撃が激化を続けるか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残7日（8/16）</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🤝 <strong>イラン最高国家安全保障会議の書記がゾルガドル氏から対米強硬派レザイー氏に交代、前書記の6条件は継承（8/9）／トランプ大統領はイランの賠償要求に逆賠償要求で応酬し対話が硬直化（8/10）／イラン外務省報道官は6条件を改めて確認、IRGC報道官は海峡再開をオマーン協議とは別問題と明言／高市首相はオマーン国王に自由で安全な航行の早期回復を要請（8/10）／フーシ派は紅海の要衝モカを2日連続攻撃、7人死亡・イエメン内戦拡大の懸念／日本関係船は残り4隻で変化なし——封鎖165日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残5日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①レザイー新体制下でイランの対米姿勢はどう変化するか ②トランプの逆賠償要求がイラン側の態度をさらに硬化させるか ③イラン・オマーンの「最終段階」協議がいつ正式合意に至るか ④フーシ派のモカ攻撃を含むイエメン内戦がどこまで拡大するか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残5日（8/16）</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー（① sec-title直下／② 確率バナー末尾、両方）

<!-- APPLY:START -->
<!-- OLD:START -->
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
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月11日 09:26 JST 更新</span><br>
  📊 <strong>イランSNSC書記が対米強硬派レザイー氏に交代、トランプは逆賠償要求で応酬——フーシ派はモカを2日連続攻撃：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — SNSC新体制も前書記の6条件を継承しつつ、トランプの逆賠償要求で対話の焦点がさらに拡散——合意への道筋はむしろ後退した<br>
  🅑 膠着継続 <span style="color:#f87171;">↑</span> — イラン・オマーン協議は「最終段階」とされる一方、海峡再開自体は対米条件次第とIRGCが明言し、外交と実務の分離が鮮明化——最多シナリオとしての位置づけが一段と強まった<br>
  🅒 MOU形骸化・機能不全 <span style="color:#fbbf24;">→</span> — イラン議会の排除・通行料法案に新たな進展はなく、制度化リスクは前回水準からの変化なし<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — SNSCの対米強硬派新書記就任と、フーシ派によるモカへの2日連続攻撃・イエメン内戦再燃の懸念が重なり、地域全体の軍事的緊張が引き続き高まっている<br>
  <strong style="color:#f87171;">イランの体制強硬化と米側の対抗姿勢が同時進行し、外交トラックの停滞が長期化する公算が強まった。イラン議会法案の停滞に大きな変化はないが、イエメン情勢の悪化により地域的な武力衝突リスクも高止まりしている（A↓ B↑ C→ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月11日 09:26 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（本文）

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>米当局者が「無制限の商用航行再開合意が出れば対イラン封鎖を解除する」という具体的な条件を初めて明示したことは、段階的MOU履行の道筋を描く上で意味のある一歩である。ただし合意成立の前提となるイラン議会の排除・通行料法案はなお文言調整段階にとどまり、同時にUAE関連タンカーへの新たな攻撃も発生しており、条件が整うまでには依然距離がある。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イラン最高国家安全保障会議の書記が対米強硬派レザイー氏に交代したことは、段階的MOU履行の見通しにとって逆風となった。前書記が示した6条件は新体制下でも継承されており、トランプ大統領がこれに逆賠償要求で応酬したことで、両者の要求リストはむしろ拡大している。イラン・オマーン間の協議自体は「最終段階」とされるが、海峡再開はあくまで対米条件の充足次第とイラン側が明言しており、段階的履行への現実的な道筋は依然見通しにくい。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>イラン議会の排除・通行料法案は「専門家審査中」からステータスが動かず、米側が提示した封鎖解除の条件を満たすめどは立っていない。並行してADNOCタンカーへの攻撃やサウジの新防衛協定締結といった動きが進んでおり、外交と軍事の両トラックが並行して停滞・緊張する状態がより長期化する様相を呈している。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イラン・オマーン間の協議は「最終段階」に近づいているとされる一方、IRGC報道官は海峡再開そのものはオマーン協議とは切り離された対米条件次第だと明言しており、実務的な航路合意と政治的な海峡再開決定が別々のトラックとして並走する構図が一段と鮮明になった。SNSC新書記も具体的な譲歩を示していないため、当面はこの二重トラックの膠着状態が続く可能性が最も高いとみられる。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>イラン議会の排除・通行料法案は依然として審議・文言調整の段階にとどまり、本日時点で採決や新たな制度化に向けた具体的な動きは確認されていない。法案が最終的にどのような条件で可決されるかは未確定だが、米側が明確に拒否姿勢を崩していないこともあり、当面は制度化のリスクが顕在化する一歩手前で足踏みが続いている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イラン議会の排除・通行料法案は本日時点でも審議・文言調整の段階にとどまり、採決や新たな制度化に向けた具体的な動きは確認されていない。SNSC体制交代という政治的な大きな変化はあったものの、法案自体のステータスに直接的な影響は見られず、制度化リスクが顕在化する一歩手前での足踏みが続いている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>UAE政府がADNOC関連タンカーへのイラン攻撃を公式に「海賊行為」と非難したことは、これまでの民間企業単独の被害報告から一段踏み込んだ政治的対応であり、今後の対応次第では緊張がさらに拡大する可能性がある。加えてサウジ・パキスタン・トルコが集団防衛協定を締結し、フーシ派が政府軍拠点への攻撃を激化させるなど、ホルムズ海峡単体にとどまらない地域全体での軍事的な緊張の高まりが顕著になっている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イランSNSCの対米強硬派新書記就任と、フーシ派による紅海要衝モカへの2日連続攻撃は、それぞれ独立した事象でありながら地域全体の軍事的緊張を同時に押し上げている。イエメンでは2022年停戦が事実上失効した状態にあり、専門家は全面的な内戦再燃の「差し迫った可能性」を指摘する。ホルムズ海峡単体の情勢に加え、周辺地域での軍事エスカレーションが連鎖的に広がるリスクが顕著になっている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5つ）

<!-- APPLY:START -->
<!-- OLD:START -->
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">UAE-ADNOCタンカー攻撃の実行主体・被害詳細が今後明らかになるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">米が提示した「無制限航行再開合意→封鎖解除」の条件を満たす合意がまとまるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">イラン議会の排除・通行料法案の文言調整がいつ決着し可決に至るか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">サウジ・パキスタン・トルコの新防衛協定発足後もフーシ派の対サウジ攻撃が続くか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保（変わらず最重要）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月7日 09:45 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">レザイー新体制下でイランの対米姿勢はどう変化するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">トランプの逆賠償要求がイラン側の態度をさらに硬化させるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">イラン・オマーンの「最終段階」協議がいつ正式合意に至るか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">フーシ派のモカ攻撃を含むイエメン内戦がどこまで拡大するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保（MOU最終期限まで残5日）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月11日 09:26 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月9日 10:06 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">UAEがADNOC関連タンカーへのイラン攻撃を公式に非難し、米は「無制限航行再開→封鎖解除」の条件を提示したが、イラン議会法案の停滞と地域的な軍事的緊張の高まりが同時進行している。【北側航路（イラン指定）】8日未明にADNOC関連タンカーがミサイル攻撃を受けたと報告され、北側ルートの安全性への懸念が再燃。イラン議会の排除・通行料法案はなお専門家審査・文言調整中で可決未了。【南ルート（Omani coastal corridor）】オマーンとの入域イラン管理・出域オマーン管理の暫定枠組み協議に新たな進展の報告はなし。中央チャンネルの機雷約80個は除去未着手のまま、除去期限は7/17（MOU第5条）を徒過。【米の封鎖姿勢】米当局者はロイターに対し、無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針を明言——イラン交渉団は最高国家安全保障会議の承認待ちと報じられる。【紅海・スエズ・黒海】フーシ派が木曜に政府軍30名超を殺害する大規模攻撃を実施、金曜も攻撃継続——サウジはパキスタン・トルコとの相互防衛協定でこれに対応。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/9 10:06 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認・金子国交相の直近会見は熊本地震対応が主題でホルムズ言及なし）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月11日 09:26 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">イランSNSCの対米強硬派新書記就任とトランプの逆賠償要求により外交トラックの実務進展は乏しい一方、イラン・オマーンの航路協議自体は「最終段階」に近づいているとされる二重構造が続く。【北側航路（イラン指定）】海峡再開の可否は対米条件の充足次第とIRGCが明言しており、通航条件面での新たな進展の報告はなし。イラン議会の排除・通行料法案はなお文言調整中で可決未了。【南ルート（Omani coastal corridor）】イラン・オマーン間の入域イラン管理・出域オマーン管理の暫定枠組み協議は「最終段階」とアラグチー外相が表明——高市首相も10日にオマーン国王へ追加費用なしの自由航行回復を要請した。中央チャンネルの機雷約80個は除去未着手のまま、除去期限7/17（MOU第5条）を徒過。【米の交渉姿勢】トランプ大統領はイランの賠償要求に逆賠償要求で応酬——具体的な封鎖解除条件の提示には至っていない。【紅海・スエズ・黒海】フーシ派が紅海の要衝モカを2日連続攻撃し7人死亡・イエメン内戦拡大の懸念。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/11 09:26 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）※最後に執筆

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
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
<!-- OLD:END -->
<!-- NEW:START -->
<span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷 イランSNSC書記が対米強硬派レザイー氏に交代——トランプは逆賠償要求で応酬し対話は硬直化。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📰 高市首相がオマーン国王と電話会談、フーシ派は紅海モカを2日連続攻撃。ブレントは4日続伸。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ イラン・オマーン協議の「最終段階」がいつ合意に至るか、封鎖165日目——MOU最終期限（8/16）まで残5日。
</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇦🇪ADNOCタンカー被弾・海賊行為と非難</span>
<span style="display:inline-block;background:rgba(74,222,128,0.15);border:1px solid rgba(74,222,128,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸無制限航行再開で封鎖解除の方針</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇸🇦🇵🇰🇹🇷相互防衛協定に署名</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📈NYダウ・S&P500最高値圏</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷SNSC新書記レザイー氏に交代</span>
<span style="display:inline-block;background:rgba(74,222,128,0.15);border:1px solid rgba(74,222,128,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸トランプが逆賠償要求で応酬</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🐹フーシ派モカ2日連続攻撃</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📈ブレント87ドル台へ続伸</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [C01] タンカー確認（SHIP_CONFIG dateConfirmed）

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年8月9日 10:06 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近会見（8/4）は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年8月11日 09:26 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近会見（8/4）は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- NEW:END -->
<!-- APPLY:END -->

**C01 タンカー確認**：日本語「日本関係船舶 ホルムズ海峡 通過 足止め」「外務省 ホルムズ海峡 日本関係船舶」「金子国土交通大臣 記者会見 ホルムズ海峡 日本関係船舶」＋英語「Japanese ships Strait of Hormuz stranded detained August 2026」の4クエリ全てでweb検索済み（外務省・国土交通省の一次情報を優先確認）／変化なし→残り4隻のまま・dateConfirmedを本日日時「変更なし」で更新

---

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-08-09T10:06:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-11T09:26:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

**対象ファイル：** `docs/data/news_data.json`

### updated フィールド

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年8月9日 10:06 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年8月11日 09:26 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

### staleNotice フィールド（新情報ありのため空文字を維持）

現状 `"staleNotice": ""` のまま変更なし。

### `latest` に追加する新規4件（先頭にprepend。追加後、現在の6件のうち最古4件をarchiveへ移動し、latestは常に最新6件を維持）

```json
[
  {
    "id": "latest-snsc-rezaei-secretary-0809",
    "title": "イラン最高国家安全保障会議、新書記にレザイー氏——対米強硬路線を継続",
    "body": "イラン最高国家安全保障会議は9日、書記をゾルガドル氏から革命防衛隊元司令官のモフセン・レザイー氏に交代させた。ゾルガドル氏は最高指導者モジュタバ・ハメネイ師の政治顧問に転じる。米シンクタンクISWは、レザイー氏がホルムズ海峡の管理権を含む最大限の要求実現を志向する一方、具体的な譲歩には消極的とみている。",
    "sourceLabel": "NBC News",
    "date": "2026年8月9日（現地）/ 2026年8月10日 JST",
    "label": "🇮🇷 外交",
    "url": "https://www.nbcnews.com/world/iran/iran-sets-steep-demands-reopening-hormuz-hopes-oman-deal-break-impasse-rcna591553",
    "isLatest": true
  },
  {
    "id": "latest-trump-counter-compensation-0810",
    "title": "トランプ氏、イランの賠償要求に「同様の賠償」で応酬——対話は一段と硬直化",
    "body": "トランプ大統領は10日、イランが求める戦争賠償要求を一蹴し、米国側も同様にイランへの賠償を求めると表明した。2000年のUSSコール事件や、イラン国内でのデモ弾圧犠牲者への補償も交渉に含めるよう代表団に指示したという。",
    "sourceLabel": "Euronews",
    "date": "2026年8月10日（現地）/ 2026年8月10日 JST",
    "label": "🇺🇸 外交",
    "url": "https://www.euronews.com/2026/08/10/trump-says-will-demand-conflict-compensation-from-iran-as-part-of-peace-talks",
    "isLatest": false
  },
  {
    "id": "latest-takaichi-oman-call-0810",
    "title": "高市首相、オマーン国王と電話会談——追加費用のない自由航行の回復を要請",
    "body": "高市早苗首相は10日夕、オマーンのハイサム国王と約20分間電話会談し、「追加的費用のない形での自由で安全な航行の一刻も早い回復」の重要性を伝え、海峡利用国を含む国際社会との協議を求めた。ハイサム国王からは、海峡利用国と協議することを確約し各国の意思も尊重する考えが示された。",
    "sourceLabel": "日テレNEWS（infoseek）",
    "date": "2026年8月10日（現地）/ 2026年8月10日 JST",
    "label": "🇯🇵 外交",
    "url": "https://news.infoseek.co.jp/article/ntv_2026081008237911/",
    "isLatest": false
  },
  {
    "id": "latest-houthi-mokha-attack-0810",
    "title": "フーシ派、紅海の要衝モカを2日連続攻撃——7人死亡、イエメン内戦拡大の懸念",
    "body": "イエメンのフーシ派は9日夜と10日、紅海沿岸の政府軍支配下の港町モカを2日連続で攻撃し、少なくとも7人（政府軍関係者4人・民間人3人）が死亡、30人が負傷した。マリブ・ハドラマウト両州での大規模攻撃（8/6〜7）に続く動きで、2022年停戦の事実上の失効とイエメン内戦再燃の懸念が強まっている。",
    "sourceLabel": "AP通信",
    "date": "2026年8月9〜10日（現地）/ 2026年8月10日 JST",
    "label": "🇾🇪 軍事",
    "url": "https://www.usnews.com/news/world/articles/2026-08-10/iran-wont-reopen-strait-of-hormuz-without-us-concessions-and-other-mideast-developments",
    "isLatest": false
  }
]
```

### 移動先アーカイブ新規バッチ（現在の latest 最古4件を格納。batchLabel例）

```json
{
  "batchLabel": "2026年8月5日〜8日",
  "items": [ /* 現在のlatest配列インデックス2〜5（米当局者封鎖解除条件・サウジパキスタントルコ防衛協定・イランオマーン安全航路合意・イラン議会法案審議 の4件）をそのまま移動 */ ]
}
```

### `osint`（現地メディア視点）新規1件（`isLatest: true`、既存の Türkiye Today 記事は `isLatest: false` に変更）

```json
{
  "id": "osint-oil-prices-climb-iran-demands",
  "date": "2026年8月10日（現地）/ 2026年8月10日 JST",
  "titleJa": "ブレント原油続伸——イランの新たな要求が海峡見通しに影を落とす",
  "titleEn": "Oil prices climb as Iranian demands cloud outlook for Strait of Hormuz",
  "country": "カタール",
  "media": "Al Jazeera",
  "url": "https://www.aljazeera.com/economy/2026/8/10/oil-prices-climb-as-iranian-demands-cloud-outlook-for-strait-of-hormuz",
  "isLatest": true
}
```

---

## [S11] 更新ログ

### ブロック1: 常時表示エリアの更新（3件固定を維持）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月7日 09:45 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/07 09:45</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省、ホルムズ海峡の安全航路座標についてオマーンと合意したと発表——共同声明は最終調整段階（IRNA、8/5）・米メディアはオマーンが入域イラン管理・出域オマーン管理の暫定枠組みに合意と報道（MS NOW、8/6）・一方イラン議会委員会は米・イスラエル船の恒久排除と他国船への最大7%通行料・違反時20%罰金の法案を審議（Fars通信）・米政府はこの案を即座に拒否し無条件の自由航行を要求（CNBC）・フーシ派はサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目、29隻が引き返し（Reuters）・NYダウは263ドル高の54,349.12ドルで3日連続最高値も6日は反落・原油は乱高下しブレントが一時81ドル台へ反発・日本関係船は残り4隻で変化なし・封鎖161日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月5日 10:24 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/05 10:24</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）・浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提（AP/Washington Times）・イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示（IRIB）・レザイー最高指導者上級顧問は代替航路を強制する米艦船への攻撃も辞さないと警告・UKMTOはオマーン沖でリベリア籍バルカー「ミノアン・パイオニア」の被弾を発表（乗員1名行方不明）・イラン国営メディアはクウェート米軍基地への攻撃を主張したが米側未確認・NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75.77ドルへ続落・日本関係船は残り4隻で変化なし・封鎖159日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月3日 09:46 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/03 09:46</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ氏、サウジのムハンマド皇太子から電話で説得を受け週末の対イラン大規模攻撃を土壇場で中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及し月曜からイランと交渉開始へ（Newsweek/NPR）・イラン軍代行国防相は「心理作戦」と一蹴、半官営メール通信は「新たな虚偽」と反発——イラン政府は公式受諾を表明せず（Al Jazeera）・イラン国営ファールス通信は北側航路になお多数の船舶が足止めされたままと報道・UKMTOはオマーン沖でタンカー「ガスログ・シャンハイ」の被弾を発表（7/31・機関室損傷）・クウェート軍はイラン系ドローンを迎撃（8/1）——NYTはIRGCが4月停戦中にフーシ派・ヒズボラ・イラク民兵と共謀し戦線拡大を図っていたと報道・原油はブレントが前日比4.65%安の83.84ドルへ急落（8/2）・日本関係船は残り4隻で変化なし・封鎖157日目・ニュース4件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月11日 09:26 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/11 09:26</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン最高国家安全保障会議、書記をゾルガドル氏から対米強硬派モフセン・レザイー氏（革命防衛隊元司令官）に交代——ゾルガドル氏はハメネイ師政治顧問に転身（NBC、8/9）・前書記の6条件（脅迫停止・戦争終結・封鎖解除と米軍撤収・戦争賠償・制裁解除・資産凍結解除）は継承・トランプ大統領はイランの賠償要求に「同様の賠償を求める」と反発、USSコール事件等も対象に（Euronews、8/10）・高市首相はオマーンのハイサム国王と電話会談し追加費用のない自由航行の回復を要請（8/10）・フーシ派は紅海の要衝モカを2日連続攻撃し7人死亡・イエメン内戦拡大の懸念（AP）・ブレント原油87.72ドルへ4日続伸(+4.95%)、NYダウ53,975.98ドル(-0.11%)・S&P500は7,753.11ドル(-0.06%)と小反落・日本関係船は残り4隻で変化なし・封鎖165日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月7日 09:45 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/07 09:45</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省、ホルムズ海峡の安全航路座標についてオマーンと合意したと発表——共同声明は最終調整段階（IRNA、8/5）・米メディアはオマーンが入域イラン管理・出域オマーン管理の暫定枠組みに合意と報道（MS NOW、8/6）・一方イラン議会委員会は米・イスラエル船の恒久排除と他国船への最大7%通行料・違反時20%罰金の法案を審議（Fars通信）・米政府はこの案を即座に拒否し無条件の自由航行を要求（CNBC）・フーシ派はサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目、29隻が引き返し（Reuters）・NYダウは263ドル高の54,349.12ドルで3日連続最高値も6日は反落・原油は乱高下しブレントが一時81ドル台へ反発・日本関係船は残り4隻で変化なし・封鎖161日目・ニュース4件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2: log-collapse への旧3件目（8/5 10:24）の挿入 ＋ 合計超過分（7/19）の削除

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月3日 09:46 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月5日 10:24 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/05 10:24</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）・浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提（AP/Washington Times）・イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示（IRIB）・レザイー最高指導者上級顧問は代替航路を強制する米艦船への攻撃も辞さないと警告・UKMTOはオマーン沖でリベリア籍バルカー「ミノアン・パイオニア」の被弾を発表（乗員1名行方不明）・イラン国営メディアはクウェート米軍基地への攻撃を主張したが米側未確認・NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75.77ドルへ続落・日本関係船は残り4隻で変化なし・封鎖159日目・ニュース4件更新・osint更新</div>
          <div>📅 <strong>2026年8月3日 09:46 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/19 10:17</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省「米イラン停戦覚書は危機段階に入った」と表明・トランプ「停戦は終わった」と言及・米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊・イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃・ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者）・クウェート石油公社施設に甚大な被害・イラン側発表で直近の米空爆により46名死亡400名超負傷・ホルムズ通航量は7/16に8隻のみで3週間ぶり最低水準・原油はブレント7/17終値88.09ドル（週間+14%超）・日本関係船は残り4隻で変化なし・封鎖142日目・ニュース3件更新・osint更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ ブロック2で 7/19 のエントリー本文（`<div>📅...</div>` と `<div><span>...</span>...</div>` の2行）を削除し、出典リンク①以降はそのまま維持すること。削除理由：常時表示3件＋log-collapse内エントリーの合計が12件となり10件を超過するため、最古（7/19）を削除。`update_log.json` にも同エントリーを先頭追加すること（追記のみ・削除ではない）。

---

## 補足：`update_log.json` への追記（プロンプト指示・str_replaceでの直接編集不要、Claude Codeが追記）

```json
{"date":"2026/08/11 09:26","text":"イランSNSC書記が対米強硬派レザイー氏に交代・トランプは逆賠償要求で応酬・高市首相がオマーン国王に自由航行回復を要請・フーシ派が紅海モカを2日連続攻撃・ブレント87.72ドルへ続伸・日本関係船残り4隻で変化なし・封鎖165日目"}
```
