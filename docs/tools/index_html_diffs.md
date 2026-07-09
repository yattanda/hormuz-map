# index_html_diffs.md — 2026年7月10日 07:40 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## 本日の情勢サマリー

7/8のトランプ氏「停戦は終わった」発言後、米イラン軍事衝突が本格化。CENTCOMは7/8夜（イラン時間）に南部イラン各地（ブシェール、チャバハール、バンダルアッバス、ジャスク等）で追加空爆を実施（防空・レーダー・小型艇能力等、計約80カ所規模）。これに対しIRGCは7/9、クウェート（Ali Al Salem基地・パトリオット迎撃システム）、バーレーン（第5艦隊拠点Port Salman・燃料タンク）、カタール（早期警戒システム）の米軍関連拠点にドローン・ミサイルで報復攻撃を実施——停戦後初めてカタールが標的となった。クウェート国防省は弾道ミサイル3発・巡航ミサイル1発・ドローン10機を迎撃したが、迎撃に伴う被害で1名負傷（容体安定）と発表。バーレーン・クウェート・UAE・ヨルダンが強く非難。イラン国会議長ガリバフ氏（対米交渉責任者）はXで「攻撃すれば、反撃を受ける」と警告し、ホルムズ海峡の航行は「イランの取り決めの下でのみ」可能と主張。アラグチー外相はトランプ氏の発言を「下品な物言い」と批判しつつ「決然として恐れず」対応すると表明。ブシェール州で7/9に原因不明の爆発も複数報告。原油は一時ブレント$79台まで急騰後、$77前後に落ち着く動き。日本関係船舶は18隻で変化なし（本日確認済み）。封鎖133日目。

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（トランプ氏「停戦は終わった」表明・原油急騰（ブレント一時$75台）／一方で商船三井関係8隻が追加通過し日本関係船は残り18隻に・封鎖132日目）</span>
    <span class="badge-item badge-date">📅2026年7月9日 06:59 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米イラン軍事衝突が本格化——CENTCOM追加空爆にイランがクウェート・バーレーン・カタールの米軍拠点をドローン・ミサイルで報復／日本関係船18隻で変化なし・封鎖133日目）</span>
    <span class="badge-item badge-date">📅2026年7月10日 07:40 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年7月9日 06:59 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月9日 06:59 JST） -->
      🚨【トランプ氏「停戦終わった」】NATO首脳会議（アンカラ）で記者団に「もう終わったと思っている」「時間の無駄」と発言・イラン指導部を「cuckoo」等と罵倒（7/8 CBS）｜🇮🇷 アラグチー外相、X投稿で反論——「下品さには下品さでなく行動で応える」（7/8）｜💬 イラン外務省バガーイ報道官「MOUはホルムズ管理権をイランに戻すもの」——米側はこの解釈を否定｜🛢️ 原油急騰——ブレント原油+4.4%・一時$75.18（前日終値$71.99）／WTI+5.3%・一時$74.26——ホルムズ攻撃再燃でリスクプレミアム再評価（7/8）｜🇯🇵 商船三井関係8隻が追加でイランルート経由通過——金子国交相発表の26隻（7/7会見）から残り18隻に減少・通航料支払いなし（7/7判明・時事通信）｜🏛️ 木原官房長官「日本船舶に被害なし」——ホルムズ攻撃への外交努力継続を強調（7/8）｜🌍 IMO「ペルシャ湾内に船員約6,000人が依然取り残されている」（7/8）｜⚱️ 故ハメネイ師、本日マシュハドで埋葬予定｜⚠️ 機雷除去「イランのみ権利」継続——除去期限まで残8日・封鎖132日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月10日 07:40 JST） -->
      🚨【米イラン軍事衝突が本格化】CENTCOM、南部イラン各地（ブシェール・チャバハール・バンダルアッバス・ジャスク等）で追加空爆——防空・レーダー・小型艇能力等を標的（7/8夜・RFE/RL）｜🇮🇷 IRGC、クウェート（Ali Al Salem基地）・バーレーン（第5艦隊拠点）・カタール（早期警戒システム）の米軍拠点をドローン・ミサイルで報復攻撃——停戦後初のカタール標的化（7/9）｜🛡️ クウェート国防省「弾道ミサイル3発・巡航ミサイル1発・ドローン10機を迎撃」——迎撃被害で1名負傷（容体安定）｜🗣️ ガリバフ国会議長（対米交渉責任者）「攻撃すれば反撃を受ける」——ホルムズはイランの取り決めの下でのみ航行可能と主張（X投稿）｜🇮🇷 アラグチー外相、トランプ氏発言を「下品な物言い」と批判——「決然として恐れず」対応表明・パキスタン等に電話で情勢共有｜🌍 バーレーン・クウェート・UAE・ヨルダンがイランの攻撃を強く非難｜💥 ブシェール州で原因不明の爆発複数報告（7/9・詳細調査中）｜🛢️ 原油、一時ブレント$79台まで急騰後$77前後に落ち着く（Trading Economics）｜🇯🇵 日本関係船18隻で変化なし（本日確認済み）｜⚠️ 機雷除去期限まで残7日・封鎖133日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

**対象：** `<!-- 速報インシデント　トグルボタン -->` 内

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/9 06:59 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/10 07:40 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグを置き換え）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/9 06:59 速報】トランプ氏「停戦は終わった」——NATO首脳会議で表明・イラン指導部を罵倒（7/8）｜アラグチー外相、Xで反論「行動で応える」（7/8）｜イラン外務省「MOUはホルムズ管理権をイランに戻す」——米は否定｜原油急騰——ブレント一時$75.18（+4.4%）・WTI一時$74.26（+5.3%）｜商船三井関係8隻が追加通過——日本関係船は残り18隻に減少｜IMO「船員約6,000人が依然取り残され」・封鎖132日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/10 07:40 速報】米イラン軍事衝突が本格化——CENTCOM、南部イラン各地で追加空爆（7/8夜）｜IRGC、クウェート・バーレーン・カタールの米軍拠点をドローン・ミサイルで報復——停戦後初のカタール標的化（7/9）｜クウェート国防省「迎撃したが被害で1名負傷」｜ガリバフ国会議長「攻撃すれば反撃を受ける」——ホルムズはイランの取り決めの下でのみ航行可能と主張｜アラグチー外相、トランプ氏発言を「下品な物言い」と批判｜バーレーン・クウェート・UAE・ヨルダンがイランの攻撃を非難｜原油、一時ブレント$79台まで急騰後$77前後に落ち着く｜日本関係船18隻で変化なし・封鎖133日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に2件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🗣️ 7/8 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/9 JST</span>
  <span style="color:#e2e8f0;"> IRGC、クウェート（Ali Al Salem基地・パトリオット迎撃システムを標的）・バーレーン（第5艦隊拠点Port Salman・燃料タンクを標的）・カタール（早期警戒システムを標的）の米軍関連拠点に、多数の特攻型ドローン・弾道ミサイル・巡航ミサイルで報復攻撃を実施。停戦後初めてカタールが標的となった。クウェート国防省は弾道ミサイル3発・巡航ミサイル1発・ドローン10機を迎撃したと発表したが、迎撃に伴う被害で少なくとも1名が負傷（容体は安定）。バーレーン・クウェート・UAE・ヨルダンが揃って「主権への明白な侵害」と強く非難し、カタールも近隣国への攻撃を非難した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🗣️ 7/9 JST</span>
  <span style="color:#e2e8f0;"> イラン国会議長で対米交渉責任者のガリバフ氏がX投稿で「米国はいじめや約束違反がもはや罰せられないままでは済まされないと理解していない」「攻撃すれば、反撃を受ける」と警告し、ホルムズ海峡の航行は「イランの取り決めの下でのみ」可能と改めて主張。アラグチー外相もトランプ氏の対イラン発言を「下品な物言い」と批判しつつ「イランの対応は決然として恐れず、全力である」と表明。同外相はパキスタン・オマーン・トルコの外相らと電話会談し、ホルムズ海峡の情勢を協議した。ブシェール州では7/9、原因不明の爆発が複数報告されている。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🗣️ 7/8 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

### カード① 外交

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🕊️ 外交：トランプ氏「停戦は終わった」表明——枠組み合意（MOU）の存続に最大の不透明感</div>
        <div class="s-body">トランプ大統領は7/8、NATO首脳会議（アンカラ）でルッテ事務総長と並び記者団に対し、イランとの暫定停戦は「もう終わったと思っている」「時間の無駄にすぎない」と発言。イラン指導部を「cuckoo」「evil, sick people」等と表現した。アラグチー外相はX投稿で「イラン人は品格・文化・強い道徳観で知られている。下品さには下品さでなく、行動で応える」と反論。イラン外務省のバガーイ報道官はMOUがホルムズ海峡の管理権をイランに戻すものだと主張しているが、米側はこの解釈を否定している。故ハメネイ師はマシュハドで本日埋葬予定。</div>
        <div class="s-src">出典: CBS News / Britannica / AP（7/9 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🕊️ 外交：ガリバフ議長・アラグチー外相が対米強硬姿勢——湾岸諸国はイランの報復攻撃を一斉非難</div>
        <div class="s-body">イラン国会議長で対米交渉責任者のガリバフ氏は7/9、X投稿で「攻撃すれば、反撃を受ける」と警告し、ホルムズ海峡の航行は「イランの取り決めの下でのみ」可能と改めて主張。アラグチー外相もトランプ大統領の発言を「下品な物言い」と批判し、「決然として恐れず」対応すると表明した。同外相はパキスタン・オマーン・トルコの外相らと電話協議し、ホルムズ情勢を共有。一方バーレーン・クウェート・UAE・ヨルダンは、イランによるクウェート・バーレーン・カタールへの報復攻撃を「主権への明白な侵害」として強く非難した。トランプ大統領はイランが「取引に値するか分からない」と述べ、NATO首脳会議からの帰路は通信・防衛体制上の懸念から予備の大統領専用機で帰国したと報じられている。</div>
        <div class="s-src">出典: RFE/RL / CNN / Middle East Eye（7/10 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 船舶・エネルギー

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🚢 船舶・エネルギー：商船三井関係8隻が追加通過し日本関係船は残り18隻に——原油は急騰しブレント一時$75台</div>
        <div class="s-body">金子国交相発表の5隻（7/7会見・計26隻）に続き、ペルシャ湾にとどまっていた商船三井（MOL）関係の船舶8隻が7/7、ホルムズ海峡を通過したことが同社取材で判明。日本関係船は開戦時45隻から18隻に減少した（通航料の支払いはなし）。一方、7/7未明の3隻被弾・米イラン軍事衝突再燃を受け、原油は7/8に急騰。ブレント原油は前日終値$71.99から一時$75.18（+4.4%）、WTIは$70.44から一時$74.26（+5.3%）まで上昇した。木原官房長官は「日本船舶に被害なし」と説明している。</div>
        <div class="s-src">出典: 時事通信（7/7） / Bloomberg / Investing.com（7/8 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🚢 船舶・エネルギー：日本関係船18隻で変化なし——原油は一時$79台へ急騰後、$77前後に落ち着く</div>
        <div class="s-body">日本関係船舶は7/7判明の18隻から本日（7/10）確認まで変化なし（外務省・国土交通省の新規会見発表なし）。一方、CENTCOMの追加空爆とIRGCによるクウェート・バーレーン・カタールへの報復攻撃を受け、原油市場は再び荒い値動きとなった。ブレント原油は7/9に一時$79台まで急騰（6月23日以来の高値）した後、伸び悩み$77前後まで反落（Trading Economics：$76.97・前日比-1.35%）。WTIも$73台前半で推移している。トレーダーは「次の一手が緊張緩和に向かうかどうか」を見極めている段階との指摘がある。</div>
        <div class="s-src">出典: Trading Economics / Kitco・Reuters / Bloomberg（7/10 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ 安全保障

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">⚠️ 安全保障：機雷除去は依然未着手——MOU存続への疑義と個別船団通過の併存が続く</div>
        <div class="s-body">トランプ氏の「停戦は終わった」発言は、シナリオC（実務レベルでの機能不全）〜D（全面対決）双方のリスクを高める一方、商船三井関係8隻が無事にイラン指定ルート経由で通過を完了したことは、イランが個別交渉・自国管理ルートでの通航自体は容認し続けていることを示す。IMOは船員約6,000人が依然ペルシャ湾内に取り残されていると発表。7/17の機雷除去期限まで残8日、8/16のMOU最終期限まで残38日。</div>
        <div class="s-src">出典: gCaptain / IMO / Britannica（7/9 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">⚠️ 安全保障：CENTCOM追加空爆にイランが4カ国規模で応酬——機雷除去は依然未着手のまま期限迫る</div>
        <div class="s-body">CENTCOMは7/8夜、南部イラン各地（ブシェール・チャバハール・バンダルアッバス・ジャスク等）で追加空爆を実施。これに対しIRGCは7/9、クウェート・バーレーン・カタールの米軍拠点にドローン・ミサイルで報復し、停戦後初めてカタールが標的となった。クウェート国防省は弾道ミサイル3発・巡航ミサイル1発・ドローン10機を迎撃したが、迎撃被害で1名が負傷したと発表。ブシェール州では原因不明の爆発も複数報告されている。機雷除去は依然未着手のまま7/17の除去期限まで残7日、8/16のMOU最終期限まで残37日に迫っている。</div>
        <div class="s-src">出典: RFE/RL / CNN / IranWire（7/10 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（トランプ氏「停戦終わった」表明／日本関係船団は通過完了・18隻に）」——封鎖132日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（米イラン軍事衝突が本格化——クウェート・バーレーン・カタールへの報復攻撃）」——封鎖133日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🚨 <strong>トランプ氏「停戦は終わった」表明（7/8 NATO首脳会議）——イラン外務省はMOUがホルムズ管理権をイランに戻すと主張／原油急騰（ブレント一時$75台・WTI一時$74台）／一方で商船三井関係8隻が追加通過し日本関係船は残り18隻に——封鎖132日目・MOU機雷除去期限残8日（7/17）・MOU最終期限残38日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①トランプ発言後のMOU（枠組み合意）存続の可否 ②MOUのホルムズ管理権解釈を巡る米イラン対立の行方 ③原油急騰の高止まりリスク（$75台定着か反落か） ④残る日本関係船18隻の通過見通し・日本人乗組員の有無 ⑤故ハメネイ師マシュハド埋葬（7/9）後の国内情勢</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残8日（7/17）</span>
<!-- OLD:END -->
<!-- NEW:START -->
        🚨 <strong>CENTCOM追加空爆にイランが報復——クウェート・バーレーン・カタールの米軍拠点をドローン・ミサイルで攻撃（7/9）／迎撃被害で1名負傷／ガリバフ国会議長「攻撃すれば反撃を受ける」／原油は一時$79台へ急騰後$77前後に落ち着く／日本関係船18隻で変化なし——封鎖133日目・MOU機雷除去期限残7日（7/17）・MOU最終期限残37日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①イランの報復攻撃に対する米側の対応・追加報復の有無 ②ガリバフ・アラグチー発言を受けたMOU存続の可否 ③原油急騰の高止まりリスク（$77台定着か反落か） ④ブシェール州での爆発の原因究明 ⑤残る日本関係船18隻の通過見通し</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残7日（7/17）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#4ade80;">📊 2026年7月8日 08:14 JST 更新</span><br>
  📊 <strong>米イラン軍事衝突再燃——タンカー攻撃・原油輸出許可取消で緊張が急速に悪化する一方、日本関係船団は無事通過を完了：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#fbbf24;">→</span> — ドーハ協議再開のめどは一段と後退<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — 国葬継続中に加え軍事衝突再燃で外交停止が長期化する様相<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — タンカー3隻被弾・原油輸出許可取消で実務レベルの機能不全が現実味<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — 駆逐艦への攻撃と米の反撃で軍事エスカレーションリスクが上昇（ただし日本関係船団の無事通過はイランが個別ルート通航自体は継続容認していることを示す）<br>
  <strong style="color:#fbbf24;">軍事衝突再燃を受けC・D双方のリスクが上昇する一方、イラン指定ルートでの個別通航自体は機能している（A→ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月8日 08:14 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <span style="font-weight:800;color:#4ade80;">📊 2026年7月10日 07:40 JST 更新</span><br>
  📊 <strong>CENTCOM追加空爆にイランがクウェート・バーレーン・カタールへ報復——軍事衝突が4カ国規模に拡大する一方、日本関係船は無事通過を維持：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#fbbf24;">↓</span> — ガリバフ・アラグチー両氏の強硬発言でドーハ協議再開のめどはさらに後退<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — 軍事衝突拡大で外交停止が一段と長期化する様相<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 双方の攻撃応酬で実務レベルの機能不全がさらに現実味を増す<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — 米軍拠点への直接攻撃が3カ国に拡大し軍事エスカレーションリスクが一段と上昇（ただし日本関係船18隻は変化なく個別ルート通航自体は継続）<br>
  <strong style="color:#fbbf24;">軍事衝突が湾岸諸国へ拡大しC・D双方のリスクがさらに上昇する一方、個別通航は機能を維持している（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月10日 07:40 JST 時点での分析に基づく自動同期
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>7/7、CENTCOM駆逐艦3隻がホルムズ海峡通過中にイランの攻撃を受け反撃するという新たな軍事衝突が発生し、外交進展の兆しは大きく後退した。アラグチー外相は「脅威が続く限り最終合意交渉には応じない」と明言しており、ドーハ協議再開の前提条件自体が崩れつつある。一方で、日本関係船10隻超が7/6〜7、イラン沿岸寄りルートを通じて無事にホルムズ海峡を通過し、残る日本関係船舶は26隻まで減少した。これはイランが個別調整・自国管理ルートでの商船通航自体は継続して認めていることを示しており、通航の「部分的な機能」と軍事衝突が併存する複雑な状況にある。故ハメネイ師の国葬は本日7/8ナジャフ・カルバラでの追悼式典を経て7/9マシュハド埋葬まで継続する。段階的MOU履行という楽観シナリオの実現には、まず今回の軍事衝突の収束と再発防止が前提となる。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>CENTCOMによる7/8夜の追加空爆と、これに対するIRGCのクウェート・バーレーン・カタールへの報復攻撃（7/9）により、軍事衝突は当初の駆逐艦への攻撃・反撃という限定的な応酬から、複数の湾岸諸国を巻き込む規模へと拡大した。ガリバフ国会議長は「攻撃すれば反撃を受ける」と改めて警告し、アラグチー外相もトランプ氏の発言を「下品な物言い」と批判するなど、対米交渉の前提条件はさらに崩れつつある。一方で日本関係船18隻は本日確認まで変化がなく、イランが個別調整・自国管理ルートでの商船通航自体は継続して認めていることを示している。段階的MOU履行という楽観シナリオの実現には、まず今回の4カ国規模の軍事衝突の収束と再発防止が前提となるが、現時点でその兆しは乏しい。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>ドーハ協議は依然として再開のめどが立っておらず、今回の軍事衝突とアラグチー外相の強硬発言により、膠着状態がさらに固定化する様相を見せている。一方、日本関係船10隻超がイラン沿岸寄りルート経由で無事通過を完了し残り26隻となったことは、イランが「自国管理下での個別通航」という形での部分的な正常化路線を維持していることを示す——これは通航料徴収を含む恒久的な管理体制への布石とも解釈できる。故ハメネイ師の国葬は本日7/8ナジャフ・カルバラでの追悼式典へ進行中で、外交停止が事実上長期化している。主要海運4社（Maersk・MSC・CMA CGM・Hapag-Lloyd）は戦争保険水準が下がるまで復帰しない方針を維持しており、機雷約80個が除去されない限り完全正常化は遠い。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>ドーハ協議は依然として再開のめどが立っておらず、軍事衝突が湾岸3カ国へ拡大したことで、膠着状態がさらに固定化する様相を見せている。一方、日本関係船18隻は本日確認まで変化がなく、イランが「自国管理下での個別通航」という形での部分的な正常化路線を維持していることを示す——これは通航料徴収を含む恒久的な管理体制への布石とも解釈できる。ガリバフ議長の「イランの取り決めの下でのみ航行可能」との発言は、この路線の固定化をさらに印象づける。主要海運4社（Maersk・MSC・CMA CGM・Hapag-Lloyd）は戦争保険水準が下がるまで復帰しない方針を維持しており、機雷約80個が除去されない限り完全正常化は遠い。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>7/7のタンカー3隻被弾・原油輸出許可取消は、まさに本シナリオが想定する「実務レベルでの機能不全」が現実化しつつあることを示している。機雷除去はINTERTANKOによれば依然未着手のまま7/17期限（残9日）が迫っており、イランは「機雷除去はイランのみの権利」との立場を崩していない。一方で日本関係船団はイラン指定ルート経由で無事通過を完了しており、これは「機雷除去等の共通インフラは機能不全のまま、個別調整による通航のみが機能する」という本シナリオの状態そのものを体現している。原油輸出許可の取消は、イランにとって収入源の喪失であり、通航への嫌がらせ（タンカー攻撃）という形での報復インセンティブを高める要因になり得る。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>CENTCOM追加空爆とIRGCによる湾岸3カ国への報復攻撃は、まさに本シナリオが想定する「実務レベルでの機能不全」が現実化しつつあることを示している。機雷除去は依然未着手のまま7/17期限（残7日）が迫っており、イランは「機雷除去はイランのみの権利」との立場を崩していない。一方で日本関係船18隻はイラン指定ルート経由の通航自体は維持されており、これは「機雷除去等の共通インフラは機能不全のまま、個別調整による通航のみが機能する」という本シナリオの状態そのものを体現している。ブシェール州での原因不明の爆発も、実務レベルの機能不全がインフラ面にまで及びつつある兆候として注視が必要である。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>7/7、CENTCOM駆逐艦3隻がイランの攻撃を受け反撃するという、standdown合意（6/28）後で最も深刻な軍事衝突が発生した。CENTCOMは「エスカレーションは求めない」と明言し、反撃を発射拠点・指揮統制・偵察拠点に限定するなど自制姿勢を維持している点、また同時期に日本関係船団がイラン指定ルートを無事通過していることは、本シナリオへの急速な移行を今のところ食い止めている材料といえる。ただしイラン側はタンカー3隻への攻撃と米の原油輸出許可取消という応酬が続いており、双方の自制が今後も維持されるかは不透明。シナリオCとの差：C=「機雷除去等の実務レベルでの機能不全」、D=「IRGCが完全封鎖を実力行使・CENTCOM大規模報復・戦争再開」。今回の衝突がCENTCOMの限定反撃にとどまるか、より大規模な報復の連鎖に発展するかが焦点。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>CENTCOMの7/8夜の追加空爆と、これに対するIRGCのクウェート・バーレーン・カタール3カ国への同時報復攻撃（7/9）は、standdown合意（6/28）後で最も規模の大きい軍事衝突となった。クウェート国防省は迎撃に伴う負傷者1名を報告しており、実際の人的被害が生じた点は従来の応酬から一段階深刻化したことを示す。バーレーン・クウェート・UAE・ヨルダンが一斉に非難する一方、日本関係船18隻は変化なく個別通航自体は維持されており、本シナリオへの急速な移行を今のところ食い止めている材料といえる。シナリオCとの差：C=「機雷除去等の実務レベルでの機能不全」、D=「IRGCが複数国規模で実力行使・CENTCOM大規模報復・戦争再開」。今回の3カ国同時報復がさらなる応酬の連鎖に発展するか、ここで収束するかが焦点。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオ フッター（次の焦点5点）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">タンカー攻撃を受けた通航の安全性再評価</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">アラグチー発言を受けたドーハ協議再開の可否</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">本日7/8ナジャフ・カルバラ、7/9マシュハド埋葬の国葬日程への影響有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">原油輸出許可取消の実務的影響（7/17清算期限）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船26隻の今後の通過見通し</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月8日 08:14 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">イランの報復攻撃に対する米側の追加対応の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">ガリバフ・アラグチー両氏の強硬発言を受けたMOU存続の可否</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">ブシェール州での原因不明の爆発の実態解明</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">原油急騰の高止まりリスク（$77台定着か反落か）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船18隻の今後の通過見通し</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月10日 07:40 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月9日 06:59 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】JMIC（米海軍主導）が推奨する機雷除去済みルートとして商業船が実際に通航するが、7/7未明の3隻被弾事案以降、安全性への懸念が継続。中央のTSS（通航分離帯）は危険なため回避勧告が継続。【北ルート（Iran coastline / IRGC管理）】イランのPGSA（ペルシャ湾海峡局・米OFAC制裁対象）が事前登録制で管理。7/7、金子国交相発表の5隻（計26隻）に続き、商船三井関係8隻（超大型タンカー5隻・ケミカルタンカー2隻・自動車船1隻）が追加でこの北ルート経由で通過したことが判明し、ペルシャ湾内残存の日本関係船舶は開戦時45隻から18隻に減少（時事通信7/7報道・通航料支払いなし）。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残8日）。7/8にはトランプ大統領が「停戦は終わった」と発言し、枠組み合意の存続に不透明感が強まる一方、イラン外務省はMOUがホルムズ管理権をイランに戻すと主張（米は否定）。IMOは船員約6,000人が依然ペルシャ湾内に取り残されていると発表。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。戦争保険8倍水準・ルート法的不確実性が解消されるまで復帰なし。🇯🇵 日本関係船舶：残り18隻（7/7に商船三井関係8隻が追加通過・7/9 06:59 JST再確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月10日 07:40 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】JMIC（米海軍主導）が推奨する機雷除去済みルートとして商業船が実際に通航するが、7/7未明の3隻被弾事案以降、安全性への懸念が継続。中央のTSS（通航分離帯）は危険なため回避勧告が継続。【北ルート（Iran coastline / IRGC管理）】イランのPGSA（ペルシャ湾海峡局・米OFAC制裁対象）が事前登録制で管理。日本関係船舶は7/7判明の18隻から本日（7/10）確認まで変化なし（外務省・国土交通省の新規会見発表なし）。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残7日）。CENTCOMは7/8夜、南部イラン各地で追加空爆を実施。これに対しIRGCは7/9、クウェート（Ali Al Salem基地）・バーレーン（第5艦隊拠点）・カタール（早期警戒システム）の米軍拠点をドローン・ミサイルで報復し、クウェート国防省は迎撃被害で1名負傷したと発表。バーレーン・クウェート・UAE・ヨルダンがイランの攻撃を強く非難した。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。戦争保険8倍水準・ルート法的不確実性が解消されるまで復帰なし。🇯🇵 日本関係船舶：残り18隻（変化なし・7/10 07:40 JST再確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）— 最後に作成

<!-- APPLY:START -->
<!-- OLD:START -->
🗣️ トランプ氏「停戦は終わった」とNATO首脳会議で表明——イラン外相はXで反論、原油は一時ブレント$75台へ急騰。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇯🇵 商船三井関係8隻が追加通過し日本関係船は残り18隻に（7/7）——一方でトランプ氏「停戦は終わった」と表明・原油は一時ブレント$75台へ急騰。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ MOUのホルムズ管理権解釈を巡る米イラン対立の行方が焦点、封鎖132日目——機雷除去期限（7/17）まで残8日・MOU最終期限（8/16）まで38日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
🗣️ CENTCOM追加空爆にイランがクウェート・バーレーン・カタールの米軍拠点へドローン・ミサイルで報復——迎撃被害で1名負傷、湾岸諸国が一斉に非難。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇯🇵 日本関係船18隻で変化なし——一方で米イラン軍事衝突が湾岸3カ国規模に拡大・原油は一時ブレント$79台へ急騰後$77前後に落ち着く。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ イランの報復攻撃を受けた米側の対応と追加エスカレーションの有無が焦点、封鎖133日目——機雷除去期限（7/17）まで残7日・MOU最終期限（8/16）まで37日。
</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🗣️停戦「終わった」</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油急騰$75台</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💬MOU解釈対立</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船18隻に</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚱️マシュハド埋葬</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️湾岸3カ国へ報復</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油一時$79台</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🗣️ガリバフ「反撃警告」</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船18隻変化なし</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🤕クウェートで負傷者</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新メモ

### `updated` フィールド

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月9日 06:59 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年7月10日 07:40 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

### `latest` 配列 先頭に3件追加（既存の isLatest:true 項目は false に変更）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-trump-ceasefire-over-0709",
      "title": "トランプ氏「イランとの停戦は終わった」——NATO首脳会議で表明",
      "body": "トランプ米大統領は7月8日、トルコ・アンカラで開催されたNATO年次首脳会議で、ルッテ事務総長と並んで記者団に対し、イランとの暫定停戦について「私としては、もう終わったと思っている」「私からすれば、時間の無駄にすぎない」と発言した。イラン指導部を「cuckoo」「evil, sick people」等と表現。米イラン間の軍事衝突再燃（7/7）後、枠組み合意（MOU）の存続に対する最大の不透明要因となっている。",
      "sourceLabel": "CBS News / Bloomberg",
      "date": "2026年7月8日（現地）/ 2026年7月8日 JST",
      "label": "🕊️ 外交",
      "url": "https://www.cbsnews.com/live-updates/us-iran-war-trump-says-ceasefire-over/",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "id": "latest-irgc-kuwait-bahrain-qatar-0710",
      "title": "IRGC、クウェート・バーレーン・カタールの米軍拠点に報復攻撃——1名負傷",
      "body": "イラン革命防衛隊（IRGC）は7月9日、CENTCOMによる前夜の追加空爆への報復として、クウェート（Ali Al Salem基地）、バーレーン（第5艦隊拠点）、カタール（早期警戒システム）の米軍関連拠点にドローン・ミサイルによる攻撃を実施したと発表した。停戦後、カタールが標的となったのは初めて。クウェート国防省は弾道ミサイル3発・巡航ミサイル1発・ドローン10機を迎撃したとしたが、迎撃に伴う被害で少なくとも1名が負傷（容体は安定）したと明らかにした。バーレーン・クウェート・UAE・ヨルダンはイランの攻撃を「主権への明白な侵害」として一斉に非難した。",
      "sourceLabel": "RFE/RL",
      "date": "2026年7月9日（現地）/ 2026年7月9日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.rferl.org/a/iran-war-us-hormuz-oil-blockade-gulf-israel/33640284.html",
      "isLatest": true
    },
    {
      "id": "latest-ghalibaf-araghchi-warning-0710",
      "title": "ガリバフ国会議長「攻撃すれば反撃を受ける」——アラグチー外相も対米強硬姿勢",
      "body": "イラン国会議長で対米交渉責任者のモハマド・バゲル・ガリバフ氏は7月9日、X投稿で米国は「いじめや約束違反がもはや罰せられないままでは済まされない」と警告し、「攻撃すれば、反撃を受ける」と述べた。ホルムズ海峡の航行は「イランの取り決めの下でのみ」可能と改めて主張。アラグチー外相もトランプ大統領の対イラン発言を「下品な物言い」と批判し、イランの対応は「決然として恐れず、全力」であると表明した。",
      "sourceLabel": "CNN",
      "date": "2026年7月9日（現地）/ 2026年7月9日 JST",
      "label": "🕊️ 外交",
      "url": "https://www.cnn.com/2026/07/09/middleeast/iran-us-ceasefire-attacks-resume-intl-hnk",
      "isLatest": false
    },
    {
      "id": "latest-oil-volatile-0710",
      "title": "原油、一時ブレント$79台へ急騰後$77前後に落ち着く",
      "body": "軍事衝突拡大を受け、ブレント原油は7月9日に一時1バレル=79ドル台まで急騰し、6月23日以来の高値を付けた。その後は伸び悩み、Trading Economicsによれば同日終値は76.97ドル（前日比-1.35%）。WTIも73ドル台前半で推移している。トレーダーは軍事衝突がさらなる報復につながるか、収束に向かうかを見極めている段階だとの指摘が出ている。",
      "sourceLabel": "Trading Economics / Kitco・Reuters",
      "date": "2026年7月9日（現地）/ 2026年7月10日 JST",
      "label": "🛢️ 原油市場",
      "url": "https://www.kitco.com/news/off-the-wire/2026-07-09/oil-prices-fall-markets-weigh-impact-us-strikes-iran",
      "isLatest": false
    },
    {
      "id": "latest-trump-ceasefire-over-0709",
      "title": "トランプ氏「イランとの停戦は終わった」——NATO首脳会議で表明",
      "body": "トランプ米大統領は7月8日、トルコ・アンカラで開催されたNATO年次首脳会議で、ルッテ事務総長と並んで記者団に対し、イランとの暫定停戦について「私としては、もう終わったと思っている」「私からすれば、時間の無駄にすぎない」と発言した。イラン指導部を「cuckoo」「evil, sick people」等と表現。米イラン間の軍事衝突再燃（7/7）後、枠組み合意（MOU）の存続に対する最大の不透明要因となっている。",
      "sourceLabel": "CBS News / Bloomberg",
      "date": "2026年7月8日（現地）/ 2026年7月8日 JST",
      "label": "🕊️ 外交",
      "url": "https://www.cbsnews.com/live-updates/us-iran-war-trump-says-ceasefire-over/",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

> 📌 Claude Codeへ：latest配列が7件を超える場合は、最古の1件（latest-mou-hormuz-control-dispute-0709 以降）をarchive配列の先頭に移動してください。

### `osint`（現地メディア視点）先頭に1件追加

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "id": "osint-hormuz-july3-001",
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "id": "osint-bushehr-blasts-0709",
      "titleJa": "【Al Jazeera】南部イラン各地で爆発——テヘランは湾岸諸国へ攻撃",
      "titleEn": "Iran war live: Blasts across southern Iran after Tehran attacks GCC states",
      "country": "カタール / 中東全域",
      "media": "Al Jazeera",
      "cardBg": "rgba(20,83,45,0.3)",
      "cardBorder": "rgba(34,197,94,0.3)",
      "badgeColor": "rgba(34,197,94,0.2)",
      "borderColor": "rgba(34,197,94,0.5)",
      "textColor": "#86efac",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/9/iran-war-live-one-killed-as-us-bombs-bushehr-chabahar-bandar-abbas-jask",
      "date": "2026年7月9日（現地）/ 2026年7月9日 JST",
      "isLatest": true
    },
    {
      "id": "osint-hormuz-july3-001",
<!-- NEW:END -->
<!-- APPLY:END -->

> 📌 既存の `osint-hormuz-july3-001` エントリの `isLatest` を `true` から `false` に変更してください（Claude Codeでの反映時にgrep確認）。

---

## [JSON-LD] dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-09T06:59:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-10T07:40:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S11] 更新ログ追記（2ブロック構成）

### ブロック1：常時表示3件を更新

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年7月9日 06:59 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/09 06:59</span> — <strong style="color:#fca5a5;">【重大更新】</strong>トランプ大統領、NATO首脳会議（アンカラ）でイランとの停戦は「もう終わったと思っている」と表明・イラン指導部を罵倒（7/8）・アラグチー外相はXで反論・イラン外務省「MOUはホルムズ管理権をイランに戻す」——米は否定（7/8）・原油急騰（ブレント一時$75.18・+4.4%／WTI一時$74.26・+5.3%）・商船三井関係8隻が追加通過し日本関係船は残り18隻に（7/7判明・時事通信）・IMO「船員約6,000人取り残され」・封鎖132日目・ニュース3件更新</div>
        <div>📅 <strong>2026年7月8日 08:14 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/08 08:14</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>CENTCOM、ホルムズ海峡通過中の駆逐艦3隻（トラクスタン・ペラルタ・メイソン）への攻撃に反撃——米イラン軍事衝突が再燃（7/7）・タンカー3隻新たに被弾（カタール籍Al Rekayyat・サウジ籍Wedyan含む）・米財務省がイラン産原油売却許可を取消（7/17清算期限）・アラグチー外相「脅威継続なら交渉再開せず」・一方で日本関係船10隻超がイランルート経由で通過し残り26隻に（7/6〜7・金子国交相発表）・故ハメネイ師、本日ナジャフ・カルバラで追悼式典（7/9マシュハド埋葬）・封鎖131日目・ニュース3件更新</div>
        <div>📅 <strong>2026年7月7日 09:05 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/07 09:05</span> — <strong style="color:#fca5a5;">【定常確認更新】</strong>故ハメネイ師国葬、本日ゴム追悼式（7/9マシュハド埋葬まで継続）・トランプ「いずれにせよ米国が勝つ」発言（7/6）・オマーン南ルートで商船8隻Uターン（うち4隻イランルートへ変針・7/3〜4）・イランが日本企業へ石油販売を打診（Reuters 7/3）・日本関係船舶31隻で変化なし・ブレント$72割れ/WTI$69割れに続落（OPEC+8月増産・サウジ値下げ）・封鎖130日目・ニュース2件更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年7月10日 07:40 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/10 07:40</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>CENTCOM、南部イラン各地（ブシェール・チャバハール・バンダルアッバス・ジャスク等）で追加空爆（7/8夜）・IRGCがクウェート・バーレーン・カタールの米軍拠点にドローン・ミサイルで報復——停戦後初のカタール標的化（7/9）・クウェート国防省「迎撃したが被害で1名負傷」・ガリバフ国会議長「攻撃すれば反撃を受ける」・バーレーン・クウェート・UAE・ヨルダンが非難・ブシェール州で原因不明の爆発複数・原油一時$79台へ急騰後$77前後に落ち着く・日本関係船18隻で変化なし・封鎖133日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月9日 06:59 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/09 06:59</span> — <strong style="color:#fca5a5;">【重大更新】</strong>トランプ大統領、NATO首脳会議（アンカラ）でイランとの停戦は「もう終わったと思っている」と表明・イラン指導部を罵倒（7/8）・アラグチー外相はXで反論・イラン外務省「MOUはホルムズ管理権をイランに戻す」——米は否定（7/8）・原油急騰（ブレント一時$75.18・+4.4%／WTI一時$74.26・+5.3%）・商船三井関係8隻が追加通過し日本関係船は残り18隻に（7/7判明・時事通信）・IMO「船員約6,000人取り残され」・封鎖132日目・ニュース3件更新</div>
        <div>📅 <strong>2026年7月8日 08:14 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/08 08:14</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>CENTCOM、ホルムズ海峡通過中の駆逐艦3隻（トラクスタン・ペラルタ・メイソン）への攻撃に反撃——米イラン軍事衝突が再燃（7/7）・タンカー3隻新たに被弾（カタール籍Al Rekayyat・サウジ籍Wedyan含む）・米財務省がイラン産原油売却許可を取消（7/17清算期限）・アラグチー外相「脅威継続なら交渉再開せず」・一方で日本関係船10隻超がイランルート経由で通過し残り26隻に（7/6〜7・金子国交相発表）・故ハメネイ師、本日ナジャフ・カルバラで追悼式典（7/9マシュハド埋葬）・封鎖131日目・ニュース3件更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：旧3件目（7/7分）を log-collapse 先頭に挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月6日 09:04 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月7日 09:05 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/07 09:05</span> — <strong style="color:#fca5a5;">【定常確認更新】</strong>故ハメネイ師国葬、本日ゴム追悼式（7/9マシュハド埋葬まで継続）・トランプ「いずれにせよ米国が勝つ」発言（7/6）・オマーン南ルートで商船8隻Uターン（うち4隻イランルートへ変針・7/3〜4）・イランが日本企業へ石油販売を打診（Reuters 7/3）・日本関係船舶31隻で変化なし・ブレント$72割れ/WTI$69割れに続落（OPEC+8月増産・サウジ値下げ）・封鎖130日目・ニュース2件更新</div>
          <div>📅 <strong>2026年7月6日 09:04 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
本日のセルフチェック項目数：14件

[x] Step 0 ― project_knowledge_search で最新diffs.md（7/9 06:59）と更新ログ先頭行の日時一致を確認 ✓
[x] S01 ヘッダー ― 2026年7月10日 07:40 JST・封鎖133日目 ✓
[x] S02 TICKER ― CENTCOM追加空爆・IRGC報復（クウェート/バーレーン/カタール）・ガリバフ発言・原油動向・日本関係船18隻 ✓
[x] S03 速報インシデント ― 7/10 07:40更新・新規2件追加（IRGC報復攻撃／ガリバフ・アラグチー発言） ✓
[x] S04 情勢カード3枚 ― 外交・船舶エネルギー・安全保障の3枚を7/10版に更新 ✓
[x] S05 COUNTDOWN ― 封鎖133日目・機雷除去残7日・MOU最終期限残37日 ✓
[x] S06 シナリオ確率補足バナー ― 7/10 07:40 JST日付更新・矢印A↓B→C↑D↑ ✓
[x] S07 シナリオ4本 ― A/B/C/D本文を7/10情勢（4カ国規模衝突）に更新、C・Dの差別化維持 ✓
[x] S08 シナリオフッター ― 次の焦点5点を7/10版に更新 ✓
[x] S08.5 全ルート現況サマリー ― 7/10 07:40 JST更新・日本関係船18隻変化なし反映 ✓
[x] S09 30秒カラム（3行＋バッジ5枚） ― 7/10版に更新（最後に作成）✓
[x] S10 news_data.json更新メモ ― latest 3件新規追加・osint 1件追加・updated日付 ✓
[x] S11 更新ログ ― ブロック1（常時3件）＋ブロック2（log-collapse先頭移動）2ブロック構成 ✓
[x] JSON-LD dateModified ― 2026-07-10T07:40:00+09:00 に更新 ✓

C01 タンカー確認（本日実施・4クエリ）：
　日本語①「日本関係船舶 ホルムズ海峡 通過 足止め」②「外務省 ホルムズ海峡 日本関係船舶」③「金子国土交通大臣 会見 ホルムズ海峡」
　英語④「Japanese ships Strait of Hormuz stranded remaining July 2026」
→ 変化なし：7/7判明の18隻から本日まで新規の大臣会見・外務省発表を確認できず、18隻のまま。
　dateConfirmed: 2026年7月10日 07:40 JST「変更なし」として記録。
二重封鎖表記チェック：「イラン・米国による二重封鎖」✓（単独表記なし）
TICKER内JST表記チェック：全日付にJST付き ✓
Al Jazeera使用チェック：📰関連最新ニュースへの混入なし（🌐現地メディア視点osintのみ使用）✓
人名表記チェック：習近平等の言及なし ✓
URL捏造チェック：新規newsアイテムのurlはRFE/RL・CNN・Kitco・Al Jazeeraで実在確認済み ✓
毎日新聞・Wikipedia使用チェック：不使用 ✓
```

---

## ⚠️ Claude Code への申し送り事項

1. news_data.json の `latest` 配列は本日3件を先頭に追加したため、合計が7件を超える場合は最古の1件（`latest-mou-hormuz-control-dispute-0709` 以降）を `archive` 配列の先頭に移動してください。
2. `osint` 配列の既存先頭エントリ（`osint-hormuz-july3-001`）の `isLatest` を `true` → `false` に変更するのを忘れずに（新規追加した `osint-bushehr-blasts-0709` のみ `true`）。
3. S06/S07/S08（シナリオ確率補足バナー・シナリオ4本・シナリオフッター）は、7/9更新時に未反映のまま7/8時点の内容が残っていたため、本diffsのold_strは実際のHTML（7/8時点の内容）を前提としています。適用前に念のため grep で該当箇所が一致するか確認してください。
4. S11ブロック2の old_str は「本日時点のlog-collapse先頭エントリー」を前提としています。他の更新が並行して適用されていた場合は、実際のHTMLと突き合わせてください。
