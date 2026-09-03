# index_html_diffs.md — 2026年9月2日 10:30 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> news_data.json は本ファイル内の [FILE:docs/data/news_data.json] 指定ブロックをapply_diffs.py非対象として直接str_replaceしてください。
> archive_timeline.json は apply_diffs.py の対象外のため、末尾の [S12] セクションの指示に従い直接 str_replace で追記してください。

---

## Step 0 / C01 実施記録（本文執筆前に完了）

- Step 0: project_knowledge_search 2件（"index_html_diffs.md 最新 更新 JST" / "更新ログ 出典 JST 更新"）を実施し、直前セッションの基準時刻が2026年8月31日09:49 JST（封鎖185日目）であることを確認。さらに old_str はメモリではなく `raw.githubusercontent.com` から直接 curl 取得した実ファイルから抽出（diffs-generation-rules.md の鉄則どおり）。
- C01タンカー確認（4クエリ個別実行、結論：変化なし）：
  1. 日本語「日本関係船舶 ホルムズ海峡 通過 足止め 9月」→ 新規発表なし
  2. 日本語「外務省 ホルムズ海峡 日本関係船舶 9月2日」→ 新規発表なし
  3. 日本語「金子国土交通大臣 会見 ホルムズ海峡 日本関係船舶 9月」→ 直近の確定発言は引き続き7/10会見の「残り4隻」
  4. 英語「Japanese ships Strait of Hormuz stranded detained September 2026」→ 新規報道なし
  → 結論：日本関係船は残り4隻のまま変化なし。dateConfirmedを本日時刻で更新。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米中央軍のホーキンス報道官によれば、イラン革命防衛隊(IRGC)が30日、ホルムズ海峡ララク島から機雷搭載ロケット弾を発射する準備をしていたため、米軍がロケットランチャー2基を攻撃——先週の機雷除去完了発表からわずか1週間足らずでの対イラン軍事行動再開となった／IRGCはこの攻撃で「犠牲者」が出たと発表し、報復として31日、ヨルダン駐留の米軍基地2カ所（キング・フセイン空軍基地、アルアズラク空軍基地）に弾道ミサイル攻撃を実施、ヨルダン軍は同国領空に侵入した8発を迎撃したと発表、双方とも目立った被害は確認されていない／米中央軍は30日時点で対イラン港湾封鎖に伴い商船83隻を迂回・3隻を航行不能化・2隻を臨検したと発表／IRGC海軍は海峡の実効支配を「完全に決定的」と主張し米側の「開通」発表を「明白な嘘」と非難、米中央軍は「イランは海峡を支配していない」と反論／モジュタバ・ハメネイ最高指導者はインフレ・失業など「経済的・生活上の課題」への対応が必要と初めて公に認め、ペゼシュキアン大統領はイランの輸出が制裁・封鎖で約35％減少したと発表／米財務省はUAEのバンク・ミスル支店を対米コルレス銀行取引から遮断する手続きを開始（イラン向けシャドーバンキング103社・18億ドル相当に関与と認定）／原油はブレントが90ドル台、WTIも86ドル近辺まで反発／日本関係船は残り4隻で変化なし／封鎖185日目）</span>
    <span class="badge-item badge-date">📅2026年8月31日 09:49 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米中央軍は9月1日正午（米東部時間）、バンダレアッバース近郊・ケシュム島・シリク・南部ケルマーン州ジロフト空港周辺などのレーダー網・防空システム・対艦巡航ミサイル発射拠点を含む数十カ所へ対イラン攻撃を拡大——トランプ大統領は機雷再敷設の失敗した試みとヨルダン基地攻撃への報復だと説明し、海峡に機雷は存在しないと強調、イランが再報復すれば「これまでで最大級」を含むさらに厳しい攻撃を行うと最大級の警告を発した／イラン国営タスニム通信は同日「決断作戦」の開始を発表し報復に着手、ヨルダンへ13発の弾道ミサイルを発射しヨルダン軍は10発を迎撃・3発が無人地帯に着弾したと発表（8/31の8発から規模拡大）、クウェート・バーレーンでもイラン発ドローンに対し防空システムが作動／イラン当局者は南部ホルモズガン州の結婚式会場が米攻撃を受け2人死亡と発表／イスラエル報道によれば米側はイランがタンカーを攻撃するたびイラン国営タンカーを攻撃する「タンカー・フォー・タンカー」政策を新たに導入したと関係者証言／ベッセント財務長官は「イランの経済破綻は加速局面」と述べ、8/31だけで原油1700万バレルが海峡を通過したと指摘／ペゼシュキアン大統領はSCO首脳会議（ビシュケク）で米がイスラマバード覚書の履行に戻れば即応じると表明したが、トランプ氏は「合意は紙切れ同然」と一蹴／原油はブレントが96ドル台へ3営業日続伸し直近6週間で最高値／日本関係船は残り4隻で変化なし／封鎖187日目）</span>
    <span class="badge-item badge-date">📅2026年9月2日 10:30 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月31日 09:49 JST） -->
      ⚔️【対イラン軍事行動再開】米軍がホルムズ海峡ララク島でイランのロケットランチャー2基を攻撃——機雷搭載ロケット弾の発射準備を阻止、約1カ月ぶりの軍事行動（8/30）｜🇯🇴 IRGC、報復としてヨルダンの米軍基地2カ所へ弾道ミサイル攻撃、ヨルダン軍は侵入した8発を迎撃と発表（8/31 JST）｜⚔️ IRGC海軍「海峡支配は完全に決定的」——米中央軍の「開通」主張を「明白な嘘」と一蹴、CENTCOMは「イランは海峡を支配していない」と反論｜💰 米財務省、UAEのバンク・ミスル支店を対米コルレス銀行取引から遮断へ——イラン向けシャドーバンキング103社・18億ドル相当を関与認定｜📉 モジュタバ・ハメネイ最高指導者「インフレ・失業など経済課題への対応が必要」と初めて公に認める——ペゼシュキアン大統領は輸出35％減と発表｜🛢️ 原油はブレントが90ドル台、WTIも86ドル近辺まで反発（8/30）｜🇯🇵 日本関係船は残り4隻で変化なし｜封鎖185日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年9月2日 10:30 JST） -->
      ⚔️【対イラン攻撃さらに拡大】米軍が9/1、バンダレアッバース・ケシュム島・シリク・ジロフト空港などレーダー・防空網を含む数十カ所を攻撃——トランプ氏「再報復なら過去最大級の攻撃も」と最大級の警告（9/1）｜🇯🇴 イラン、「決断作戦」で報復——ヨルダンへ13発発射・10発迎撃（9/1）｜🇰🇼🇧🇭 クウェート・バーレーンでもイラン発ドローンに防空発動、被害報告なし｜🛢️ 米、イランのタンカー攻撃への対抗策として「タンカー・フォー・タンカー」政策導入と関係者証言｜💬 ペゼシュキアン氏、SCO首脳会議で米のMOU履行復帰なら即応と表明——トランプ氏「合意は紙切れ」と一蹴｜🛢️ ブレント原油96ドル台——直近6週間で最高値（9/2）｜🇯🇵 日本関係船は残り4隻で変化なし｜封鎖187日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米軍がホルムズ海峡ララク島のイラン軍施設を攻撃、イランはヨルダンの米軍基地2カ所へ報復——ヨルダン軍が8発迎撃</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/31 09:49 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米、対イラン攻撃を数十カ所へ拡大——イランは「決断作戦」でヨルダンに13発発射、クウェート・バーレーンも防空発動</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 9/2 10:30 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/31 09:49 速報】米中央軍のティム・ホーキンス報道官によれば、イラン革命防衛隊(IRGC)の部隊が30日、ホルムズ海峡のイラン領ララク島から機雷を搭載したロケット弾を海峡へ向け発射する準備をしているのが確認されたため、米軍がロケットランチャー2基を攻撃した——対イラン軍事行動は約1カ月ぶりで、米軍は先週、同海峡国際航路の機雷除去作業を完了したばかりだった（AP、NBC News）｜イラン国営系メディアはララク島付近で複数の爆発音を確認したと報道｜IRGCはこの攻撃により「犠牲者」が出たと主張し、正確な人数は示さないまま即時報復を表明した（Reuters）｜報復として、IRGCは31日、ヨルダンに駐留する米軍が運用するキング・フセイン空軍基地およびアルアズラク空軍基地の技術インフラ・整備施設・戦闘機駐機位置を弾道ミサイルで標的にし「甚大な被害」を与えたと国営テレビ・IRIBを通じ発表（AFP、時事通信）｜ヨルダン軍広報官は31日未明、同国領空に侵入した8発のミサイルを防空システムが交戦規則に基づき迎撃したと発表、市民・施設への被害はなかったと強調｜米側も、着弾したミサイルのほぼ全てを迎撃し目立った被害はないと説明（Fox News）｜米中央軍は30日時点で、対イラン港湾封鎖の一環として商船83隻を迂回、3隻を航行不能化、2隻を臨検したと発表——前回確認時点（39隻）から大幅に増加｜TankerTrackers社の分析では、直近1週間で米の封鎖ラインを越えて輸送された原油は日量平均670万バレルに達した｜原油市場はこの軍事衝突再燃を受け上昇、ブレント原油は90ドル台へ、WTIも86ドル近辺まで反発｜今回の軍事応酬は、トランプ政権が「軍事行動より経済圧力を優先する」と表明した直後のタイミングで発生した点が注目されている｜UKMTOは29日20時53分（UTC）、オマーン・ハサブ北方約12海里の地点でホルムズ海峡へ向け内航中のタンカーが正体不明の飛翔体で被弾したとの遅延報告（Warning 122-26）を30日付で公表——負傷者・環境影響の報告はなく当局が調査中。JMICのUpdate 091（8/30 15:00 UTC時点）はアラビア湾＝Moderate、ホルムズ海峡＝Severe、オマーン湾＝Moderateと評価｜日本関係船は残り4隻で変化なし｜封鎖185日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【9/2 10:30 速報】米中央軍は9月1日正午（米東部時間）、イラン革命防衛隊(IRGC)の対艦巡航ミサイル発射拠点・レーダー施設・防空システムなど数十カ所を対象に対イラン攻撃を拡大した——バンダレアッバース近郊、ケシュム島、シリク、南部ケルマーン州ジロフト空港周辺などで爆発が相次いだとイラン国営テレビが報道（CENTCOM、CNBC）｜トランプ大統領はTruth Socialで、イランによる機雷再敷設の失敗した試みとヨルダン基地攻撃への報復だと説明し、海峡に機雷は存在しないと強調——イランが再度報復すれば「これまでで最大級」を含むさらに厳しい対応を取ると警告した（The Times of Israel）｜イラン国営タスニム通信は同日「決断作戦」の開始を発表、地域の米軍基地・権益をミサイル・ドローンで狙うとした｜ヨルダン軍は自国領空に侵入した13発の弾道ミサイルのうち10発を迎撃、3発は無人地帯に着弾し死傷者はなかったと発表——前回（8/31）の8発から規模が拡大した（AFP）｜クウェート・バーレーンも自国上空でイラン発ドローンに対し防空システムを作動させたと発表、被害報告はなし｜イラン・ホルモズガン州副知事は南部の結婚式会場が米攻撃を受け2人死亡・複数負傷と発表（AFP）｜イスラエルメディアによれば、米は今回からイランがホルムズ海峡でタンカーを攻撃するたびイラン国営タンカーを攻撃する「タンカー・フォー・タンカー」政策を導入したと関係者が証言｜ベッセント財務長官はG20財務相会合で「イランの経済破綻は加速局面にある」と述べ、8/31だけで原油1700万バレルが海峡を通過したとしてイランが海峡を実効支配していない証拠だと指摘（CBS News）｜原油はブレントが96ドル台へ3営業日続伸、直近6週間で最高値｜日本関係船は外務省・国土交通省への日英4クエリ確認で新規発表なし・残り4隻のまま｜封鎖187日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に新規3件を追記）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 8/30 米東部時間</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 9/1 12:00 米東部時間</span>
  <span style="color:#e2e8f0;"> CENTCOMは、IRGCによるホルムズ海峡での商船攻撃未遂・米軍要員への攻撃を受けIRGC標的への攻撃を開始したと発表。イラン国営メディアはバンダレアッバース近郊・ケシュム島・シリク・ジロフト空港周辺での爆発を報告し、対象はレーダー・防空システム・対艦巡航ミサイル発射拠点など数十カ所に及んだ。トランプ大統領は「再敷設の失敗した機雷とヨルダン攻撃への報復」と説明し、更なる報復には「これまでで最大級」の攻撃で応じると警告した（CENTCOM、CNBC）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇯🇴🇰🇼🇧🇭 9/1 JST</span>
  <span style="color:#e2e8f0;"> イラン国営タスニム通信は「決断作戦」開始を発表し即時報復。ヨルダン軍は自国領空に侵入した13発の弾道ミサイルのうち10発を迎撃、3発は無人地帯へ着弾し死傷者なしと発表——8/31の8発から規模拡大。クウェート・バーレーンも自国上空でイラン発ドローンへ防空システムを作動させたが被害報告はない（The Times of Israel、AFP）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">💒 9/1 JST</span>
  <span style="color:#e2e8f0;"> イラン・ホルモズガン州のナフィシ副知事は、州内の結婚式会場が米攻撃を受け2人が死亡、複数が負傷したと国営テレビで発表。真偽は独立検証できていない（AFP）。同日、イスラエルメディアは米側が今回からイランのタンカー攻撃に対しイラン国営タンカーを攻撃する「タンカー・フォー・タンカー」政策を導入したと関係者証言を報じた。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 8/30 米東部時間</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 最新情勢カード（3枚とも刷新・角度を分離）

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- カード① カタール外交・条件リスト -->
  <div class="sit-card danger">
    <div class="s-icon">🇶🇦</div>
        <div class="s-title">⚔️ 米軍、ホルムズ海峡ララク島のイラン軍施設を攻撃——対イラン軍事行動が約1カ月ぶりに再開</div>
        <div class="s-body">米中央軍は30日、イラン革命防衛隊(IRGC)の部隊がホルムズ海峡のイラン領ララク島から機雷を搭載したロケット弾を海峡へ発射する準備をしていたことを受け、ロケットランチャー2基を攻撃したと発表した。米軍が同海峡の国際航路における機雷除去作業を完了したと表明してからわずか1週間足らずでの軍事行動再開であり、トランプ政権が数日前に「軍事行動より経済圧力を優先する」方針を示した直後のタイミングでもある。IRGCはこの攻撃で「犠牲者」が出たと主張し、正確な人数を示さないまま即座に報復を表明した。</div>
        <div class="s-src">出典: AP通信 / NBC News（8/30 現地時間）</div>
  </div>

  <!-- カード② 米軍「開通」主張と実態のギャップ -->
  <div class="sit-card warning">
    <div class="s-icon">🇯🇴</div>
        <div class="s-title">🇯🇴 イラン、ヨルダンの米軍基地2カ所へ報復ミサイル攻撃——ヨルダン軍が8発迎撃・双方に目立った被害なし</div>
        <div class="s-body">IRGCは報復として31日、ヨルダンに駐留する米軍が運用するキング・フセイン空軍基地とアルアズラク空軍基地の技術インフラ・整備施設・戦闘機駐機位置を弾道ミサイルで標的にし「甚大な被害」を与えたと国営テレビ・IRIBを通じ発表した。これに対しヨルダン軍広報官は31日未明、同国領空に侵入した8発のミサイルを防空システムが交戦規則に基づき迎撃したとし、市民や施設への被害はなかったと強調。米側報道でも、着弾したミサイルのほぼ全てを迎撃し目立った被害はないとされ、双方の発表を突き合わせる限り、軍事衝突再燃の割に実害は限定的にとどまっている。</div>
        <div class="s-src">出典: AFP通信 / 時事通信 / ヨルダン軍公式発表（8/31 JST）</div>
  </div>

  <!-- カード③ タンカー被弾・市場・日本関係船 -->
  <div class="sit-card info">
    <div class="s-icon">🗣️</div>
        <div class="s-title">🗣️ IRGC海軍「海峡支配は完全に決定的」、米中央軍は反論——原油は90ドル台へ反発、日本関係船は4隻で変化なし</div>
        <div class="s-body">IRGC海軍は「海峡を巡る戦士たちの支配は完全に決定的」であり、米側の「開通」発表は「原油価格を操作し自らの失敗を覆い隠すための明白な嘘」だと非難した。これに対し米中央軍のホーキンス報道官は「イランは海峡を支配していない」と反論し、発表合戦が続いている。並行して、モジュタバ・ハメネイ最高指導者はインフレ・失業など「経済的・生活上の課題」への対応が必要だと初めて公に認め、ペゼシュキアン大統領はイランの輸出が制裁・封鎖により約35％減少したと発表した。原油市場はララク島攻撃を受けブレントが90ドル台、WTIも86ドル近辺まで反発。日本関係船については外務省・国土交通省への日英4クエリ調査で引き続き新規発表がないことを確認し、残り4隻のまま変化はない。</div>
        <div class="s-src">出典: Tasnim通信 / Fox News Digital / 外務省・国土交通省（8/30〜31 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- カード① 軍事エスカレーション拡大 -->
  <div class="sit-card danger">
    <div class="s-icon">⚔️</div>
        <div class="s-title">⚔️ 米、対イラン攻撃を数十カ所へ拡大——トランプ氏「再報復なら過去最大級の攻撃も」と最大級の警告</div>
        <div class="s-body">CENTCOMは9月1日正午（米東部時間）、IRGCによる商船攻撃未遂・米軍要員への攻撃を受け、レーダー網・防空システム・対艦巡航ミサイル発射拠点を含む数十カ所への攻撃を開始したと発表した。イラン国営メディアはバンダレアッバース近郊・ケシュム島・シリク・南部ケルマーン州ジロフト空港周辺での爆発を報告。トランプ大統領はTruth Socialで、イランによる機雷再敷設の失敗した試みとヨルダン基地攻撃への報復だと説明し、海峡に機雷は存在しないと強調したうえで、イランが再報復すれば「これまでで最大級」を含むさらに厳しい攻撃で応じると警告した。8/30〜31の攻撃からわずか1〜2日での再拡大となる。</div>
        <div class="s-src">出典: CENTCOM / CNBC / The Times of Israel（9/1）</div>
  </div>

  <!-- カード② ヨルダン・湾岸諸国への報復拡散 -->
  <div class="sit-card warning">
    <div class="s-icon">🇯🇴</div>
        <div class="s-title">🇯🇴 イラン「決断作戦」で報復拡大——ヨルダンに13発発射・10発迎撃、クウェート・バーレーンも防空発動</div>
        <div class="s-body">イラン国営タスニム通信は9月1日、「決断作戦」の開始を発表し即座に報復に着手。ヨルダン軍は自国領空に侵入した13発の弾道ミサイルのうち10発を迎撃、3発は無人地帯へ着弾し死傷者はなかったと発表した——8/31の8発から規模が拡大している。同日、クウェート・バーレーンでも自国上空でイラン発ドローンに対し防空システムが作動したが、いずれも被害報告はない。イラン当局者は南部ホルモズガン州の結婚式会場が米攻撃を受け2人死亡・複数負傷と発表しており、報復の応酬が周辺の湾岸諸国全体を巻き込む形で広がっている。</div>
        <div class="s-src">出典: The Times of Israel / AFP（9/1 JST）</div>
  </div>

  <!-- カード③ 市場・タンカー政策・外交・日本関係船 -->
  <div class="sit-card info">
    <div class="s-icon">🛢️</div>
        <div class="s-title">🛢️ 米「タンカー・フォー・タンカー」政策導入、原油は96ドル台へ——ペゼシュキアン氏のMOU復帰提案をトランプ氏は一蹴</div>
        <div class="s-body">イスラエルメディアによれば、米側は今回からイランがホルムズ海峡でタンカーを攻撃するたびイラン国営タンカーを攻撃する「タンカー・フォー・タンカー」政策を新たに導入したと関係者が証言している。ベッセント財務長官はG20財務相会合で「イランの経済破綻は加速局面にある」と述べ、8/31だけで原油1700万バレルが海峡を通過したとしてイランが海峡を実効支配していない証拠だと指摘した。並行してペゼシュキアン大統領はSCO首脳会議（ビシュケク）で、米がイスラマバード覚書の履行に戻れば即座に応じると表明したが、トランプ氏は「合意は紙切れ同然」と一蹴。原油はブレントが96ドル台へ3営業日続伸し直近6週間で最高値を付けた。日本関係船は外務省・国土交通省への日英4クエリ調査で新規発表がないことを確認し、残り4隻のまま変化はない。</div>
        <div class="s-src">出典: CBS News / RFE/RL / Trading Economics（9/1〜9/2）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN（Phaseラベル＋展望ノート）

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 30「対イラン軍事行動が再開——ララク島攻撃とヨルダン報復の応酬で停戦の脆さ露呈」——封鎖185日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 31「対イラン攻撃が数十カ所へ拡大——イラン『決断作戦』でヨルダン・湾岸諸国を巻き込む報復合戦に」——封鎖187日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🌐 <strong>米軍が機雷除去完了の発表からわずか1週間足らずで対イラン軍事行動に踏み切ったことは、トランプ政権が数日前に表明したばかりの「軍事より経済圧力優先」路線の実効性に早くも疑問符を投げかけている——イランが即座にヨルダンの米軍基地を狙った報復に踏み切ったことは、6カ月におよぶ緊張状態が依然として一触即発の均衡の上に成り立っていたことを浮き彫りにした。イラン・オマーンの通航管理枠組みや「条件リスト」策定といった外交的な地ならしが同時並行で進んでいた矢先の軍事衝突再燃は、外交チャンネルの脆さも示している——ヨルダン軍が迎撃に成功し双方に目立った被害がなかったことは全面戦争再燃を回避する余地が残っていることを示す一方、IRGC海軍と米中央軍が海峡の実効支配を巡り真っ向から対立する発表を続けている状況は、今後の情勢判断を一層難しくしている／日本関係船は残り4隻で変化なし——封鎖185日目</strong>
        <br><span style="color:#fde68a;">⚡ 次の24〜48時間の焦点：①イランのヨルダン攻撃を受けた米側の追加対応の有無 ②IRGCが主張する「犠牲者」の具体的な人数・状況の裏付け ③オマーン・イラン間の通航管理枠組みが今回の衝突で頓挫するか ④米中央軍とIRGC海軍の海峡支配を巡る発表合戦の帰結 ⑤原油相場のさらなる上振れリスク</span>
        <br><span style="color:#fca5a5;">⏳ 「経済圧力優先」を掲げた直後の軍事行動再開という矛盾したメッセージが、今後の米政権の対イラン戦略の一貫性そのものを問う局面になりつつある</span>
<!-- OLD:END -->
<!-- NEW:START -->
        🌐 <strong>8/30〜31の応酬からわずか1〜2日で米が攻撃対象を数十カ所へ拡大し、イランも「決断作戦」でヨルダンへの発射数を8発から13発へ引き上げたことは、双方が段階的に威嚇の規模を引き上げる「エスカレーション・ラダー」に入ったことを示している——攻撃がクウェート・バーレーンにも及んだことで、当事国以外の湾岸諸国が巻き込まれるリスクが現実化した。トランプ氏がペゼシュキアン氏のMOU復帰提案を「紙切れ同然」と一蹴したことは、外交チャンネルを通じた沈静化がこの時点では選択肢に入っていないことを意味する。一方でヨルダン軍が13発中10発の迎撃に成功し死傷者が出なかったことは、防空能力面での抑止が機能している証左でもあり、全面戦争への転化を防ぐ緩衝材として働いている。</strong>
        <br><span style="color:#fde68a;">⚡ 次の24〜48時間の焦点：①イランが「決断作戦」の第2弾に踏み切るか、それとも攻撃規模を維持するか ②「タンカー・フォー・タンカー」政策の初回発動事例が出るか ③クウェート・バーレーンへの攻撃が両国の対米協力姿勢にどう影響するか ④SCO首脳会議でのロシア・中国の対イラン支持表明の有無 ⑤ホルモズガン州の民間人死傷の独立検証状況</span>
        <br><span style="color:#fca5a5;">⏳ トランプ氏がMOU復帰提案を明確に拒否したことで、少なくとも短期的には交渉より軍事的圧力の応酬が優先される局面が続くとみられる</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年8月31日 09:49 JST 更新</span><br>
  📊 <strong>米軍が対イラン軍事行動を約1カ月ぶりに再開し、イランが即座にヨルダン駐留米軍基地への報復に踏み切ったことで、直前まで進んでいたカタール仲介の外交モメンタムに冷や水が浴びせられた形となった：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — 軍事衝突が再燃したタイミングは、カタール仲介による条件リスト策定という外交的前進の勢いを削ぐ材料となる<br>
  🅑 膠着継続 <span style="color:#94a3b8;">→</span> — ヨルダン軍の迎撃成功で双方に目立った被害が出なかったことは、事態が即座に全面衝突へ転じることを回避し、従来型の膠着へ回帰する余地を残す<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 「経済圧力優先」を表明した直後の軍事行動という矛盾は、外交プロセスそのものへの信頼を損ないかねない<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — IRGCが「犠牲者」を理由に即座に報復した事実は、双方の抑制が依然として脆弱であることを示している<br>
  <strong style="color:#f87171;">約1カ月ぶりの軍事行動再開とその即時報復という新たな変数が、経済圧力路線と軍事衝突リスクという二つの軸を再び前面に押し出した（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月31日 09:49 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年9月2日 10:30 JST 更新</span><br>
  📊 <strong>米が攻撃対象を数十カ所へ拡大し、イランが「決断作戦」でヨルダン・クウェート・バーレーンを巻き込む報復に踏み切ったことで、トランプ氏がペゼシュキアン氏のMOU復帰提案を明確に拒絶する事態にまで発展した：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — トランプ氏が復帰提案を「紙切れ同然」と一蹴したことで、短期的な外交再開の芽は大きく後退した<br>
  🅑 膠着継続 <span style="color:#94a3b8;">→</span> — ヨルダンが13発中10発の迎撃に成功し死傷者が出なかった点は、応酬拡大の中でも全面戦争への即時転化を防ぐ緩衝材として機能している<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 「タンカー・フォー・タンカー」政策の新設は、当面の攻撃応酬が制度化・恒常化する方向を示唆する<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — 攻撃対象国がヨルダンからクウェート・バーレーンへ拡散したことは、地域紛争化のリスクが一段階進んだことを意味する<br>
  <strong style="color:#f87171;">米の攻撃拡大とイランの多方面報復、そしてトランプ氏の復帰提案拒否という3つの新変数が重なり、外交収束シナリオの確率をさらに押し下げている（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年9月2日 10:30 JST 時点での分析に基づく自動同期
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオA〜D 本文

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>米軍がホルムズ海峡ララク島でIRGCの機雷搭載ロケット準備を阻止した一方、この軍事行動自体が「経済圧力優先」への転換直後に発生した点は皮肉である。カタールの仲介による条件リスト策定という外交的地ならしが継続する限り、軍事衝突と交渉の並走という不安定な均衡の中でも段階的な合意形成の芽は残る。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>ペゼシュキアン大統領はSCO首脳会議の場で、米がイスラマバード覚書の履行に戻れば即座に応じる用意があると明言しており、外交チャンネル自体が完全に閉ざされたわけではないことを示している。しかしトランプ氏がこの提案をその場で「紙切れ同然」と切り捨てたことで、少なくとも米側の政治的意思としては段階的合意への回帰が当面見込みにくい状況にある。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>ヨルダン軍が侵入した8発のミサイルを全て迎撃し、双方に目立った被害が出なかったことは、当面の全面戦争回避という点では安定材料である。しかし米中央軍とIRGC海軍が海峡の実効支配を巡り真っ向から対立する発表を続ける状況が変わらない限り、発表と実態のどちらを基準に評価すべきかという不透明感を抱えたままの膠着が続きやすい。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>ヨルダン軍が13発中10発の迎撃に成功し死傷者が出なかったことは、攻撃規模が拡大する中でも防空能力による抑止が一定程度機能していることを示す。「タンカー・フォー・タンカー」政策のような新たな応酬の枠組みが導入されても、双方が決定打を欠いたまま被害を限定的に抑え合う構図が続けば、拡大と沈静化を繰り返す膠着状態が長期化する可能性がある。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>イラン・オマーンの通航管理枠組みは「イスラマバード覚書」の米側履行が前提とされているが、今回のような軍事応酬が起きるたびにその実現は遠のく。ハメネイ最高指導者が経済的苦境を公に認めた事実は、イランが交渉の必要性を内心で感じている可能性を示す一方、報復の即応性はイラン側が依然として軍事的選択肢を放棄していないことも示している。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>米が「タンカー・フォー・タンカー」政策という制度化された報復の枠組みを導入したことは、単発の応酬ではなく恒常的な攻撃応酬パターンへ移行するリスクを示している。ベッセント財務長官が「イランの経済破綻は加速局面」と明言する一方でイラン側が攻撃対象を拡大し続けている状況は、経済的疲弊が必ずしも軍事的抑制につながっていないことを裏付けている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>米軍による機雷除去完了発表からわずか1週間足らずでの軍事行動再開は、機雷除去や「開通」宣言が必ずしも安定した平時への移行を意味しないことを裏付けた。IRGCが即座にヨルダンの米軍基地を狙う報復に踏み切ったことは、双方の抑制メカニズムが依然として脆弱であり、次の一手次第で全面対決へ転じるリスクが残っていることを示している。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イランの報復対象がヨルダンからクウェート・バーレーンへと拡散したことは、これまで比較的抑制されてきた地域紛争化のリスクが一段階進んだことを示す。トランプ氏が「これまでで最大級」の攻撃を予告し、イラン側も「決断作戦」という継続性を示唆する呼称を用いていることから、双方とも次の一手として更なるエスカレーションを選択肢から排除していない点が懸念材料である。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5つ）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">「経済圧力優先」路線から一夜で軍事応酬に転じた米政権の対イラン戦略の一貫性</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン・オマーンの通航管理枠組みが今回の衝突を経てなお有効とみなされるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">Operation Economic Outcastによる金融包囲網（バンク・ミスル等）がイラン経済にどこまで実効的な打撃を与えるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">ハメネイ最高指導者が公に認めた経済的苦境が、イランの対米姿勢の軟化につながるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">UKMTOが「深刻」水準の警戒を維持する中、商船の北側（イラン指定）航路へのシフトが更に進むか</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月31日 09:49 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">イランが「決断作戦」の追加攻撃に踏み切るか、それとも今回で一区切りとするか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">「タンカー・フォー・タンカー」政策が実際に発動される初の事例が出るか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">クウェート・バーレーンへの攻撃拡散が両国の対米基地提供姿勢に変化を及ぼすか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">トランプ氏がMOU復帰提案を拒否したことで、SCO参加国（露・中）がイラン支持を強めるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">原油96ドル台からさらなる上振れが続くか、G20での追加制裁協議の行方</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年9月2日 10:30 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月31日 09:49 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【中央航路（イラン・オマーン合意ベース）】イランのガリババディ副外相は、オマーンとの間で協定の理解は一致したとしつつ、6月の「イスラマバード覚書」を米側が履行するまで発効しないと説明——「海峡は依然として閉鎖されており、通航は全てイランとの調整下でのみ可能」と強調。【南側航路（オマーン沿岸・国連承認TSS）】30日、このルート付近のイラン領ララク島でIRGCの機雷搭載ロケット準備を米軍が攻撃で阻止。同ルート沿いのオマーン・ハサブ北方約12海里でも29日20:53UTC、内航中のタンカーが正体不明の飛翔体で被弾したとUKMTOが遅延報告（Warning 122-26）——8/25の「AL SALAM II」被弾と同一海域での別事案。IRGC海軍は海峡の実効支配を「完全に決定的」と主張し米側の「開通」発表を否定、米中央軍は「イランは海峡を支配していない」と反論。【北側航路（イラン指定）】UKMTOによれば、攻撃・臨検の強化を背景に商船が北側ルートへシフトする傾向が続いている。【通航データ】米中央軍は30日時点で商船83隻を迂回、3隻を航行不能化、2隻を臨検したと発表。【市場】原油はララク島攻撃を受けブレントが90ドル台、WTIも86ドル近辺まで反発。TankerTrackersによれば直近1週間の封鎖ライン越え原油輸送は日量平均670万バレル。【JMIC/UKMTO 警戒水準】Update 091（8/30 15:00 UTC時点）によればアラビア湾：Moderate、ホルムズ海峡：Severe（深刻）、オマーン湾：Moderate。🇯🇵 日本関係船舶：残り4隻で変化なし（8/31 09:49 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年9月2日 10:30 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【中央航路（イラン・オマーン合意ベース）】9/1のSCO首脳会議で、ペゼシュキアン大統領は米がイスラマバード覚書の履行に戻れば即応じると改めて表明したが、トランプ氏はこの提案を拒否しており、当面この航路の正式発効に向けた進展は見込みにくい。【南側航路（オマーン沿岸・国連承認TSS）】9/1、米軍がバンダレアッバース近郊・ケシュム島・シリク周辺のレーダー・防空システムを攻撃したことで、南側航路の安全性を左右する監視・防空体制そのものが打撃を受けた可能性がある。イスラエルメディアによれば米は新たに「タンカー・フォー・タンカー」政策を導入し、イランのタンカー攻撃に報復する方針とされ、南側航路の商船とイラン国営タンカー双方のリスクが連動して高まる構図になっている。【北側航路（イラン指定）】クウェート・バーレーンへの攻撃拡散を受け、地域全体の緊張が北側ルートの通航判断にも波及するとみられる。【通航データ】ベッセント財務長官はG20会合で、8/31だけで原油1700万バレルが海峡を通過したと述べ、イランが海峡を実効支配していないことの証左だと指摘した。【市場】原油はブレントが96ドル台へ3営業日続伸し直近6週間で最高値、WTIも92ドル近辺まで上昇。【地域波及】ヨルダンはイランから13発の弾道ミサイル攻撃を受け10発を迎撃、クウェート・バーレーンもイラン発ドローンに対し防空システムを作動させた。🇯🇵 日本関係船舶：残り4隻で変化なし（9/2 10:30 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒で全体像を把握（3行サマリー＋ステータスバッジ5枚）※最後に作成

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⚔️ 米軍がホルムズ海峡ララク島でイランのロケット施設を攻撃、イランは即座にヨルダンの米軍基地へ報復。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷🇺🇸 IRGC海軍「海峡支配は完全に決定的」と米軍の「開通」主張を否定——発表合戦が続く中、原油は90ドル台へ反発。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
💰 ハメネイ最高指導者が経済的苦境を初めて公に認める中、軍事衝突再燃が外交モメンタムに影を落とす——封鎖185日目。
</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⚔️ 米が対イラン攻撃を数十カ所へ拡大、イランは「決断作戦」でヨルダン・クウェート・バーレーンへ報復拡散。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🛢️ 米が「タンカー・フォー・タンカー」政策を導入と関係者証言——原油はブレント96ドル台へ6週間ぶり高値。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
💬 トランプ氏、ペゼシュキアン氏のMOU復帰提案を「紙切れ同然」と拒否——外交収束の糸口は当面見えず・封鎖187日目。
</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️ララク島 米軍攻撃</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇴イラン ヨルダン基地へ報復</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🗣️IRGC海軍「支配は決定的」</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油90ドル台へ反発</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️米、攻撃を数十カ所へ拡大</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇴イラン「決断作戦」で13発発射</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇰🇼🇧🇭クウェート・バーレーンも防空発動</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油96ドル台・6週間ぶり高値</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [C01] SHIP_CONFIG dateConfirmed

**C01タンカー確認：** 日本語「日本関係船舶 ホルムズ海峡 通過 足止め 9月」「外務省 ホルムズ海峡 日本関係船舶 9月2日」「金子国土交通大臣 会見 ホルムズ海峡 日本関係船舶 9月」＋英語「Japanese ships Strait of Hormuz stranded detained September 2026」の計4クエリを個別実行。結論：4クエリいずれも新規発表なし、残り4隻のまま変化なしを再確認。

<!-- APPLY:START -->
<!-- OLD:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年8月31日 09:49 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近確定発言は7/10会見の「残り4隻」）'
};
<!-- OLD:END -->
<!-- NEW:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年9月2日 10:30 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近確定発言は7/10会見の「残り4隻」）'
};
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
dateModified": "2026-08-31T09:49:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
dateModified": "2026-09-02T10:30:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S11] 更新ログ追記（2ブロック構成）

### ブロック1：常時表示エリアの更新（本日分＋旧2件、旧3件目は除外）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月31日 09:49 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/31 09:49</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米中央軍が30日、ホルムズ海峡ララク島でIRGCの機雷搭載ロケット弾発射準備を確認しロケットランチャー2基を攻撃——対イラン軍事行動は約1カ月ぶり・米軍は先週機雷除去完了を発表したばかり（AP）・IRGCは「犠牲者」が出たと主張し即座に報復、31日にヨルダン駐留のキング・フセイン空軍基地とアルアズラク空軍基地を弾道ミサイルで攻撃したと発表（IRIB/AFP）・ヨルダン軍は同国領空侵入の8発を迎撃、市民・施設への被害なしと発表・米中央軍は30日時点で商船83隻を迂回・3隻航行不能化・2隻臨検したと発表・IRGC海軍「海峡支配は完全に決定的」と米の「開通」主張を否定、米中央軍は反論・ハメネイ最高指導者が経済的苦境を初めて公に認める、ペゼシュキアン大統領は輸出35％減と発表・米財務省がUAEのバンク・ミスル支店を対米コルレス取引から遮断へ（103社・18億ドル関与認定）・原油はブレント90ドル台・WTI86ドル近辺まで反発・日本関係船は残り4隻で変化なし・封鎖185日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月29日 10:05 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/29 10:05</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>カタールのシェイク・モハンマド首相兼外相が開戦後初のテヘラン訪問——アラグチー外相・ペゼシュキアン大統領・レザイー最高国家安全保障会議事務局長と会談（8/27）・レザイー氏は通航再開の条件リストを策定中と表明、中央航路（一部オマーン領海・一部イラン領海）で合意済みと説明・米中央軍クーパー司令官はSNS動画で「国際航路は開通・勢いを増す」と主張し商船1,500隻・原油7.5億バレル分の支援実績を発表（8/27）・トランプ大統領は「MISSION ACCOMPLISHED 2026」とSNS投稿し勝利宣言（8/26）も、その直後の25日17:30UTCにタンカー「AL SALAM II」被弾をJMICが確認・ホワイトハウス報道官は米イラン交渉が現時点でないと明言（8/27）・JMICデータでは8/25〜26の通航はわずか37隻（2025年平均は日量約138隻）・ブレント原油は4営業日続落後87ドル台後半で下げ止まり（8/28時点87.58ドル）・イラン軍は損傷兵器を「再建済み」と発表・日本関係船は残り4隻で変化なし・封鎖183日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月27日 10:00 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/27 10:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランのアラグチー外相とオマーンのアルブサイディ外相がテヘランで会談し、ホルムズ海峡に共同暫定航行回廊を設置・機雷除去を共同実施する枠組みで合意（8/25）・イラン副外相ガリババディ氏は恒久ルートを30〜60日以内に協議するとしつつ暫定合意後も海峡は開放されていないと表明、南側回廊（国連承認TSS）は閉鎖の見通しと説明（8/26）・トランプ大統領は米海軍がホルムズ海峡国際水域の機雷を全て除去・爆破したとSNS投稿し新規敷設船は即時破壊と警告するも米政府の公式裏付けなし、イラン側は「虚偽」と全面否定（8/25〜26）・24日夜オマーン東岸沖でタンカー1隻が正体不明の飛翔体で被弾・機関停止、UKMTO確認（乗員無事・犯行声明なし）・原油はブレントが一時87ドル割れ・週間約8%安（8/25）・中国外務省は対中制裁計画に「中国・イラン協力は妨害されるべきでない」と改めて反発・日本関係船は残り4隻で変化なし・封鎖181日目・ニュース3件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年9月2日 10:30 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/09/02 10:30</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米中央軍が9月1日正午（米東部時間）、バンダレアッバース近郊・ケシュム島・シリク・ジロフト空港周辺のレーダー・防空システム・対艦巡航ミサイル発射拠点など数十カ所を攻撃——トランプ氏は機雷再敷設の失敗した試みとヨルダン基地攻撃への報復と説明、再報復なら「これまでで最大級」の攻撃で応じると警告（CENTCOM/CNBC）・イランは同日「決断作戦」で報復、ヨルダンへ13発発射しヨルダン軍は10発迎撃・3発は無人地帯に着弾（8/31の8発から拡大）・クウェート・バーレーンもイラン発ドローンに防空発動（The Times of Israel/AFP）・イラン当局者は南部ホルモズガン州の結婚式会場が米攻撃を受け2人死亡と発表・米は「タンカー・フォー・タンカー」政策を新設と関係者証言・ベッセント財務長官「イランの経済破綻は加速局面」、8/31だけで原油1700万バレルが海峡通過と指摘（CBS News）・ペゼシュキアン氏はSCO首脳会議でMOU復帰なら即応と表明もトランプ氏は「紙切れ同然」と拒否（RFE/RL）・原油はブレント96ドル台へ3営業日続伸・6週間ぶり高値・日本関係船は残り4隻で変化なし・封鎖187日目・ニュース2件更新・osint更新</div>
        <div>📅 <strong>2026年8月31日 09:49 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/31 09:49</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米中央軍が30日、ホルムズ海峡ララク島でIRGCの機雷搭載ロケット弾発射準備を確認しロケットランチャー2基を攻撃——対イラン軍事行動は約1カ月ぶり・米軍は先週機雷除去完了を発表したばかり（AP）・IRGCは「犠牲者」が出たと主張し即座に報復、31日にヨルダン駐留のキング・フセイン空軍基地とアルアズラク空軍基地を弾道ミサイルで攻撃したと発表（IRIB/AFP）・ヨルダン軍は同国領空侵入の8発を迎撃、市民・施設への被害なしと発表・米中央軍は30日時点で商船83隻を迂回・3隻航行不能化・2隻臨検したと発表・IRGC海軍「海峡支配は完全に決定的」と米の「開通」主張を否定、米中央軍は反論・ハメネイ最高指導者が経済的苦境を初めて公に認める、ペゼシュキアン大統領は輸出35％減と発表・米財務省がUAEのバンク・ミスル支店を対米コルレス取引から遮断へ（103社・18億ドル関与認定）・原油はブレント90ドル台・WTI86ドル近辺まで反発・日本関係船は残り4隻で変化なし・封鎖185日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月29日 10:05 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/29 10:05</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>カタールのシェイク・モハンマド首相兼外相が開戦後初のテヘラン訪問——アラグチー外相・ペゼシュキアン大統領・レザイー最高国家安全保障会議事務局長と会談（8/27）・レザイー氏は通航再開の条件リストを策定中と表明、中央航路（一部オマーン領海・一部イラン領海）で合意済みと説明・米中央軍クーパー司令官はSNS動画で「国際航路は開通・勢いを増す」と主張し商船1,500隻・原油7.5億バレル分の支援実績を発表（8/27）・トランプ大統領は「MISSION ACCOMPLISHED 2026」とSNS投稿し勝利宣言（8/26）も、その直後の25日17:30UTCにタンカー「AL SALAM II」被弾をJMICが確認・ホワイトハウス報道官は米イラン交渉が現時点でないと明言（8/27）・JMICデータでは8/25〜26の通航はわずか37隻（2025年平均は日量約138隻）・ブレント原油は4営業日続落後87ドル台後半で下げ止まり（8/28時点87.58ドル）・イラン軍は損傷兵器を「再建済み」と発表・日本関係船は残り4隻で変化なし・封鎖183日目・ニュース4件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse への旧3件目（8/27分）の挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月25日 12:11 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月27日 10:00 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/27 10:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランのアラグチー外相とオマーンのアルブサイディ外相がテヘランで会談し、ホルムズ海峡に共同暫定航行回廊を設置・機雷除去を共同実施する枠組みで合意（8/25）・イラン副外相ガリババディ氏は恒久ルートを30〜60日以内に協議するとしつつ暫定合意後も海峡は開放されていないと表明、南側回廊（国連承認TSS）は閉鎖の見通しと説明（8/26）・トランプ大統領は米海軍がホルムズ海峡国際水域の機雷を全て除去・爆破したとSNS投稿し新規敷設船は即時破壊と警告するも米政府の公式裏付けなし、イラン側は「虚偽」と全面否定（8/25〜26）・24日夜オマーン東岸沖でタンカー1隻が正体不明の飛翔体で被弾・機関停止、UKMTO確認（乗員無事・犯行声明なし）・原油はブレントが一時87ドル割れ・週間約8%安（8/25）・中国外務省は対中制裁計画に「中国・イラン協力は妨害されるべきでない」と改めて反発・日本関係船は残り4隻で変化なし・封鎖181日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年8月25日 12:11 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：collapse最古エントリー（8/9分）の削除（総件数調整）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新（Claude Codeが直接編集・apply_diffs.py非対象）

### updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年8月31日 09:49 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年9月2日 10:30 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列：先頭に新規2件を追加し、isLatestを付け替え

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-us-strikes-larak-island-0830",
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "id": "latest-us-strikes-expanded-0901",
      "title": "米軍、対イラン攻撃を数十カ所へ拡大——バンダレアッバース近郊やレーダー網など攻撃、トランプ氏が最大級の警告",
      "body": "CENTCOMは9月1日正午（米東部時間）、IRGCによる商船攻撃未遂・米軍要員への攻撃を受け、レーダー・防空システム・対艦巡航ミサイル発射拠点など数十カ所への攻撃を開始したと発表した。イラン国営メディアはバンダレアッバース近郊・ケシュム島・シリク・南部ケルマーン州ジロフト空港周辺での爆発を報告。トランプ大統領はイランによる機雷再敷設の失敗した試みとヨルダン基地攻撃への報復だと説明し、再報復なら「これまでで最大級」の攻撃で応じると警告した。",
      "sourceLabel": "CENTCOM / CNBC / The Times of Israel（9/1）",
      "date": "2026年9月1日（現地）/ 2026年9月2日 JST",
      "label": "⚔️ 軍事行動拡大",
      "url": "https://www.cnbc.com/2026/09/01/us-strikes-iran-after-new-hormuz-strait-shipping-attacks-centcom.html",
      "isLatest": true
    },
    {
      "id": "latest-iran-decisive-operation-jordan-0901",
      "title": "イラン『決断作戦』で報復拡大——ヨルダンに13発発射・10発迎撃、クウェート・バーレーンも防空発動",
      "body": "イラン国営タスニム通信は「決断作戦」の開始を発表し即座に報復に着手した。ヨルダン軍は自国領空に侵入した13発の弾道ミサイルのうち10発を迎撃、3発は無人地帯へ着弾し死傷者はなかったと発表——8/31の8発から規模が拡大した。同日、クウェート・バーレーンでも自国上空でイラン発ドローンに対し防空システムが作動、被害報告はない。イラン当局者は南部ホルモズガン州の結婚式会場が米攻撃を受け2人死亡・複数負傷と発表した。",
      "sourceLabel": "The Times of Israel / AFP（9/1）",
      "date": "2026年9月1日（現地）/ 2026年9月2日 JST",
      "label": "🇯🇴 報復拡大",
      "url": "https://www.timesofisrael.com/liveblog-september-1-2026/",
      "isLatest": false
    },
    {
      "id": "latest-us-strikes-larak-island-0830",
<!-- NEW:END -->
<!-- APPLY:END -->

### 旧isLatest:trueアイテムをfalseへ

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "id": "latest-tanker-khasab-projectile-0829",
<!-- OLD:END -->
<!-- NEW:START -->
      "id": "latest-tanker-khasab-projectile-0829-archived-flag-off",
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️上記は目印置換です。Claude Codeは実際のisLatestフィールド（"latest-tanker-khasab-projectile-0829"を含むオブジェクト内の"isLatest": true）をfalseに書き換えたうえで、idは元の"latest-tanker-khasab-projectile-0829"に戻してください（idの変更は不要、isLatestのみ変更）。

### latest配列末尾2件（qatar-pm-tehran-visit-0827 / iran-conditions-list-0827）をarchiveへ移動

Claude Codeは、latest配列に現在含まれる `latest-qatar-pm-tehran-visit-0827` と `latest-iran-conditions-list-0827` の2件（本追加によりlatest配列が8件になるため、cap 6件を超過する最古2件）をlatest配列から削除し、archive配列の先頭に新規batchLabel（例："2026年8月27日〜29日"）付きバッチとして移動してください。

### osint 配列：先頭に新規1件を追加（Al Jazeera・osint専用）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "id": "osint-irgc-strait-control-claim-0829",
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "id": "osint-aljazeera-us-new-strikes-0901",
      "titleJa": "【Al Jazeera】米軍、対イラン攻撃を再開・拡大——ホルムズ海峡での攻撃未遂への対応と説明",
      "titleEn": "US launches new strikes against Iran as war escalates",
      "title": "【Al Jazeera】米軍、対イラン攻撃を再開・拡大——ホルムズ海峡での攻撃未遂への対応と説明",
      "country": "イラン/米国",
      "media": "Al Jazeera",
      "source": "Al Jazeera",
      "date": "2026年9月1日（現地）/ 2026年9月2日 JST",
      "summary": "Al Jazeeraは、CENTCOMがホルムズ海峡での商船攻撃未遂と米軍要員への攻撃を理由にIRGC標的への攻撃を再開・拡大したと報道。過去にも同様の米攻撃の後にイランが報復してきた経緯を踏まえ、今回の攻撃再開が新たな戦闘サイクルを引き起こすリスクがあると分析し、地域の軍事的緊張が再び高まっている構図を詳報している。",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/2026/9/1/us-military-says-launching-new-attacks-on-iran",
      "isLatest": true
    },
    {
      "id": "osint-irgc-strait-control-claim-0829",
<!-- NEW:END -->
<!-- APPLY:END -->

### 旧osint isLatest:trueを付け替え

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "url": "https://www.aljazeera.com/news/liveblog/2026/8/29/iran-war-live-irgc-asserts-strait-control-us-enforces-blockade",
      "isLatest": true
    },
    {
      "id": "osint-iran-qatar-hormuz-talks-0827",
<!-- OLD:END -->
<!-- NEW:START -->
      "url": "https://www.aljazeera.com/news/liveblog/2026/8/29/iran-war-live-irgc-asserts-strait-control-us-enforces-blockade",
      "isLatest": false
    },
    {
      "id": "osint-iran-qatar-hormuz-talks-0827",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S12] archive_timeline.json 追記（apply_diffs.py非対象・Claude Codeが直接str_replace）

`docs/data/archive_timeline.json` の配列末尾（2026-08-31エントリーの直後）に、以下のオブジェクトを新規追加してください（`blockadeDay`フィールドは表示に使用されないため形式的な記録のみ）。

```json
    ,
    {
      "date": "2026-09-01",
      "dateLabel": "2026/09/02 10:30",
      "blockadeDay": 187,
      "sourceType": "realtime",
      "summary": "米中央軍は9月1日正午（米東部時間）、バンダレアッバース近郊・ケシュム島・シリク・ジロフト空港周辺のレーダー・防空システム・対艦巡航ミサイル発射拠点など数十カ所を攻撃した。トランプ大統領は機雷再敷設の失敗した試みとヨルダン基地攻撃への報復と説明し、再報復なら『これまでで最大級』の攻撃で応じると警告。イランは同日『決断作戦』を発動し、ヨルダンへ13発の弾道ミサイルを発射（10発迎撃・3発は無人地帯着弾）、クウェート・バーレーンでもイラン発ドローンへの防空発動が確認された。イラン当局者は南部ホルモズガン州の結婚式会場が米攻撃を受け2人死亡と発表。米側は『タンカー・フォー・タンカー』政策を新設したと関係者証言があり、ベッセント財務長官は8/31だけで原油1700万バレルが海峡を通過したと指摘した。ペゼシュキアン大統領はSCO首脳会議でMOU復帰なら即応と表明したが、トランプ氏は拒否。原油はブレントが96ドル台へ上昇し6週間ぶり高値。日本関係船は残り4隻で変化なし。",
      "relatedNews": [
        {
          "sourceLabel": "CENTCOM / CNBC",
          "title": "米、対イラン攻撃を数十カ所へ拡大——トランプ氏「再報復ならこれまでで最大級」",
          "url": "https://www.cnbc.com/2026/09/01/us-strikes-iran-after-new-hormuz-strait-shipping-attacks-centcom.html"
        },
        {
          "sourceLabel": "The Times of Israel",
          "title": "イラン『決断作戦』でヨルダンに13発発射・10発迎撃——クウェート・バーレーンも防空発動",
          "url": "https://www.timesofisrael.com/liveblog-september-1-2026/"
        },
        {
          "sourceLabel": "Trading Economics",
          "title": "ブレント原油、96ドル台へ3営業日続伸——直近6週間で最高値",
          "url": "https://tradingeconomics.com/commodity/brent-crude-oil"
        }
      ]
    }
```

---

## ✅ 出力前セルフチェック（本日のセルフチェック項目数：15件）

```
[x] Step 0 ― project_knowledge_search 2件実施・直前基準時刻(8/31 09:49 JST)を確認 ✓
[x] C01 タンカー確認 ― 日英4クエリ個別実行・変化なしを確認 ✓
[x] S01 ヘッダー ― 2026年9月2日 10:30 JST・封鎖187日目 ✓
[x] S02 TICKER ― 米攻撃拡大・イラン決断作戦・タンカー政策・原油96ドル台・封鎖187日目、全日付JST付き ✓
[x] S03 速報インシデント ― 9/2 10:30付け・新規3件追加 ✓
[x] S04 情勢カード3枚 ― 3枚とも新規事象・角度を分離して刷新 ✓
[x] S05 COUNTDOWN ― Phase31・封鎖187日目・展望ノートはS01と重複回避 ✓
[x] S06 シナリオ確率補足バナー ― 9/2 10:30 JST日付更新（2箇所：見出しとフッター）✓
[x] S07 シナリオ4本 ― A/B/C/D本文を9/2情勢に更新・各シナリオ独自角度 ✓
[x] S08 シナリオフッター ― 次の焦点5点を9/2版に更新 ✓
[x] S08.5 全ルート現況サマリー ― ルート別に整理・9/2 10:30 JST更新 ✓
[x] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成）✓
[x] S10 news_data.json ― latest2件追加・isLatest付け替え・archive移動指示・osint1件追加 ✓
[x] S11 更新ログ ― 2ブロック構成＋collapse最古1件削除で総件数調整 ✓
[x] S12 archive_timeline.json ― 新規エントリー追記指示（Claude Code直接str_replace）✓
[x] JSON-LD dateModified ― 2026-09-02T10:30:00+09:00に更新 ✓

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記は本日変更対象外のため維持 ✓
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：S08.5内で9/2 10:30 JST更新を明示 ✓
人名表記チェック：「モジュタバ・ハメネイ」「ペゼシュキアン」等すべて日本語カナ表記 ✓
URL捏造チェック：全URLをweb検索で実在確認済み（CENTCOM系はCNBC/Times of Israel経由で確認） ✓
禁止媒体チェック：📰latestにAl Jazeeraは使用せず、osintのみに使用 ✓
```

---

## Claude Code への引き継ぎ指示

```
git pull --rebase してから、tools/index_html_diffs.mdに従ってdocs/index.htmlを更新してください。
また、本ファイル内の[S10]セクションに従ってdocs/data/news_data.jsonを直接str_replaceで更新し、
[S12]セクションに従ってdocs/data/archive_timeline.jsonにも新規エントリーを直接str_replaceで追加してください
（いずれもapply_diffs.pyの対象外です）。
更新完了後にcommitしてください。pushは確認後に指示します。
```
