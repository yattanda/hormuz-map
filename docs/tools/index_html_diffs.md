# index_html_diffs.md — 2026年8月1日 10:51 JST 更新分

> Claude Code への指示：以下の差分を index.html および news_data.json に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## ⚠️ 冒頭確認事項（Claude Code への申し送り）

- **封鎖日カウンターの起算日について**：Memory登録では「Day 0 = 2026-04-13」とされていますが、現在ライブ公開中の index.html（badge-alert / TICKER / COUNTDOWN / 更新ログ）は実際には「2/28開戦を起点とする日数」（GEF等の外部集計と一致）で運用されており、4/13起算とは一致していません（例：7/14時点の表示は「封鎖137日目」＝2/28起算と整合、4/13起算なら約92日目のはず）。本diffsでは**既存表示との連続性を優先し、7/30の「153日目」から2日進めて「155日目」としています**。起算日をどちらに統一するかはユーザー確認・決定が必要です（本diffsでは修正していません）。

---

## Step 0 セルフチェック（本文執筆前の事前確認）

project_knowledge_search にて「index_html_diffs.md 最新 更新 JST」「更新ログ 出典 JST 更新」を実行し、直近更新が2026年7月30日 10:08 JSTであることを確認。また `raw.githubusercontent.com` からindex.html・news_data.jsonの最新版を取得し、old_str抽出の正確性を担保。

C01タンカー確認：日本語3クエリ（「日本関係船舶 ホルムズ海峡 通過 足止め」「外務省 ホルムズ海峡 日本関係船舶」「金子国土交通大臣 記者会見 ホルムズ海峡」）＋英語1クエリ（「Japanese ships Strait of Hormuz stranded detained August 2026」）全て実施。金子国交相・外務省ともに7/10発表（残り4隻）以降の新規発表なしを確認。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米・イランの攻撃休止は3日で終了——IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃、米・サウジはイラク国内の親イラン民兵拠点を合同空爆／トランプ氏が対イラン報復攻撃を予告し7/29夜（米時間）に新たな空爆を開始と判明／イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持／原油はブレント90.66ドルまで急騰（+7%）／封鎖153日目）</span>
    <span class="badge-item badge-date">📅2026年7月30日 10:08 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（戦線がエジプト・ダミエッタ港とカザフスタンCPC黒海ターミナルへ拡大——ダミエッタではLNG貯蔵船へのドローン攻撃で今次紛争初のエジプト領内被弾／イランはホルムズ海峡を「米軍護衛下」で出域しようとしたタンカー2隻を拿捕・4隻を引き返させたと主張（西側未確認）／オマーンとの海峡共同管理協議はイラン高官が「成功の見込みなし」と拒否／原油はブレント90ドル台へ上昇・7月月間+23%の見通し／封鎖155日目）</span>
    <span class="badge-item badge-date">📅2026年8月1日 10:51 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月30日 10:08 JST） -->
      🔥【停戦崩壊】米・イラン攻撃休止は3日で終了——IRGC、米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM、7/28夜 JST）｜⚔️ 米・サウジ合同でイラク国内の親イラン民兵拠点を空爆——直近72時間で30件超の攻撃への対応（CENTCOM、7/29）｜🇺🇸 トランプ氏、対イラン報復攻撃を予告——7/29夜（米時間）に新たな対イラン空爆を開始と判明（CBS、7/30 JST）｜🇴🇲 イラン、オマーンの海峡共同管理（50-50）案を拒否——入航路・出航路一部の単独管理の立場を維持（Trading Economics、7/28）｜🇯🇵 茂木外相、アラグチ外相と電話会談——覚書に沿った対米協議継続を確認・拘束邦人1名の早期解決を要請（外務省、7/28）｜🛢️ 原油急騰——ブレント90.66ドル（前日比+7%、7/29 14:30ET）｜⚓ フーシ派、サウジ船のインド洋方面航行を標的にすると宣言——海運各社はスエズ運河迂回を模索｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残17日｜封鎖153日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月1日 10:51 JST） -->
      🚨【戦線拡大】エジプト・ダミエッタ港でLNG貯蔵船「エナゴス・ウィンター」がドローン攻撃を受け出火、隣接のLNG船「ガスログ・セーラム」にも延焼——今次紛争で初のエジプト領内攻撃（Reuters/CNBC、7/29現地）｜🇮🇷 イラン、「米軍護衛下」でホルムズ海峡を出域しようとしたタンカー2隻を拿捕・別の4隻を引き返させたと主張——西側監視機関は未確認（Reuters、7/31）｜🛢️ カザフスタンのCPCノヴォロシースク積出ターミナルが再び操業停止——タンカー「ニソス・シフノス」等への攻撃で7月中8隻超が被弾｜🇴🇲 イラン高官、オマーンの海峡共同管理案を「成功の見込みなし」と拒否——入航路線全域・出航路線一部の単独管理に固執（WSJ経由/Reuters、7/29）｜🇺🇸 米・イラン、7/30夜〜31未明は新たな空爆の報告なし——トランプ氏「勝ち続けるしかない、いずれ何かが起きる」（Fox News、7/31）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認）｜🛢️ 原油急伸——ブレント90.12ドル・WTI84.67ドル（ともに前日比+1%超、7/31 NY終値）・7月月間ではブレント+23%の見通し｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残15日｜封鎖155日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/30 10:08 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/1 10:51 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### トグルボタン内の見出し（strong）

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米・イラン停戦崩壊——IRGC米軍拠点へ奇襲も全弾迎撃／米・サウジがイラク民兵拠点を空爆／イランはオマーン海峡共同管理案を拒否</strong>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">戦線がエジプト・黒海へ拡大——ダミエッタ港LNG船が被弾／イランはタンカー拿捕を主張／オマーン海峡共同管理協議は決裂</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### 折りたたみ本体の要約（strong）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/30 10:08 速報】米中央軍（CENTCOM）は7/28夜、イラン革命防衛隊（IRGC）が中東の米軍拠点へ弾道ミサイルによる奇襲攻撃を試みたが全弾を迎撃したと発表——7/25未明から続いていた攻撃休止は3日で終了｜米・サウジ両軍は合同で、直近72時間に30件超の攻撃を行っていた親イラン系民兵拠点をイラク国内で空爆（CENTCOM）｜トランプ大統領は報復攻撃を予告し、7/29夜（米東部時間）に対イランへの新たな空爆を開始したと報じられた（CBS）｜イランはオマーンによるホルムズ海峡共同管理（50-50）案を拒否し、入航路線・出航路線の一部について単独管理の立場を維持（Trading Economics）｜茂木外相は7/28夜、アラグチ外相と電話会談し、覚書に沿った対米協議継続を求めるとともに、イランで拘束後保釈された邦人1名の問題の早期解決を改めて要請（外務省）｜フーシ派はサウジ船のインド洋方面航行を標的にすると宣言し、海運各社はスエズ運河迂回ルートの検討を進めている｜原油はブレントが7/29 14:30ET時点で90.66ドル（前日比+7%）まで急騰｜日本関係船は残り4隻で変化なし｜封鎖153日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/1 10:51 速報】エジプト・ダミエッタ港で7/29（現地）、LNG貯蔵船「エナゴス・ウィンター」がドローン攻撃を受け出火、隣接のLNG船「ガスログ・セーラム」にも延焼——今次紛争で初めてエジプト領内が攻撃対象となった（Reuters/CNBC/エジプト内閣府）｜イランは、ホルムズ海峡を「米軍護衛下」で出域しようとしたタンカー2隻を拿捕、別の4隻を引き返させたと主張——西側の海事監視機関は未確認（Reuters、7/31）｜カザフスタンのCPCノヴォロシースク積出ターミナルが、タンカー「ニソス・シフノス」等への攻撃を受け再び操業停止——7月中に被弾したタンカーは8隻超に達した｜イラン高官は、オマーンが提示した海峡共同管理案を「成功の見込みなし」と拒否し、入航路線全域・出航路線一部の単独管理に固執する姿勢を改めて示した（WSJ経由/Reuters）｜米・イラン間の直接空爆は7/30夜〜31未明にかけ新たな報告なし——トランプ氏は「勝ち続けるしかない、いずれ何かが起きる」と述べるにとどめた（Fox News）｜原油はブレントが90.12ドル、WTIが84.67ドルまで上昇（ともに前日比+1%超、7/31 NY終値）——ブレントは7月月間で+23%の見通し｜日本関係船は残り4隻で変化なし｜封鎖155日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に4件を追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/28 JST夜</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🔥 7/29 JST（現地）</span>
  <span style="color:#e2e8f0;"> エジプト北部・ダミエッタ港で、米企業所有のLNG貯蔵再ガス化船（FSRU）「エナゴス・ウィンター」がドローン攻撃を受け船体右舷が被弾、出火した炎は隣接するLNGタンカー「ガスログ・セーラム」にも延焼。乗組員は避難し負傷者なし。エジプト内閣府は8/30（現地7/30）、ドローン攻撃であることを確認。犯行声明は出ていない。イラン国営テレビが2日前にダミエッタを「ウクライナ関連権益」への報復候補地として名指ししていたことが報じられている。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇮🇷 7/31 JST</span>
  <span style="color:#e2e8f0;"> イランは、「米軍護衛下」でホルムズ海峡を出域しようとしたタンカー2隻を拿捕したと発表、別の4隻についてもイラン部隊の介入を受けて引き返したと主張した。ロイターによれば、これらの発表内容は独立した第三者機関による確認が取れていない。同日、原油積載の大型タンカー2隻が海峡を通過したことは確認されている。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#94a3b8;font-weight:700;">⚫ 7/30 JST</span>
  <span style="color:#e2e8f0;"> カザフスタンの原油輸出を担うカスピ海パイプラインコンソーシアム（CPC）は、黒海ノヴォロシースク近郊で発生したタンカー「ニソス・シフノス」（積み込み中に被弾・火災）と「マラティ」（接近中に攻撃）への攻撃を受け、積み出しを再び停止した。7/27の再開からわずか3日での再停止で、7月中にCPC関連で攻撃を受けたタンカーは少なくとも8隻に達した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🇴🇲 7/29 JST</span>
  <span style="color:#e2e8f0;"> イランの高官はホルムズ海峡共同管理を巡るオマーンの提案について「成功の見込みはない」と述べ、イラン・オマーン両国のみで、それぞれの領海比率に基づき海峡を管理すべきとの立場を改めて表明。50-50の折半案には応じない考えを示し、オマーンが自国案を受け入れなければ次段階の協議には進まないとも述べた。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/28 JST夜</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] SITUATION CARDS（3枚）

### カード① 戦線拡大（軍事・地理的拡大）

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="s-title">⚔️ 停戦崩壊：IRGC、米軍拠点へ弾道ミサイル奇襲も全弾迎撃——米・サウジはイラク民兵拠点を合同空爆</div>
        <div class="s-body">米中央軍（CENTCOM）は7/28夜、IRGCが中東の米軍拠点へ弾道ミサイルによる奇襲攻撃を試みたが全弾を迎撃したと発表。7/25未明から続いていた攻撃休止は3日で終了した。米・サウジ両軍は合同でイラク国内の親イラン系民兵拠点を空爆——直近72時間に30件超の攻撃への対応とした。トランプ大統領は報復を予告し、7/29夜（米時間）に新たな対イラン空爆を開始したと報じられている。イラク国家安全保障会議は主権侵害対処の安全保障計画策定を決定した。</div>
        <div class="s-src">出典: CENTCOM / Reuters / CBS News（7/29 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="s-title">🔥 戦線拡大：エジプト・ダミエッタ港のLNG船が被弾、カザフスタンCPCも再停止</div>
        <div class="s-body">エジプト北部ダミエッタ港で7/29（現地）、米企業所有のLNG貯蔵船「エナゴス・ウィンター」がドローン攻撃を受け出火、隣接LNGタンカー「ガスログ・セーラム」にも延焼した。エジプト内閣府は7/30、ドローン攻撃と確認——今次紛争で初のエジプト領内攻撃であり、ホルムズ・紅海双方が悪化する中で最後の安全ルートとされてきたスエズ運河・スメド・パイプライン回廊に直接波及した形となる。同時期、カザフスタンのCPCノヴォロシースク積出ターミナルもタンカー2隻への攻撃を受け、7/27の再開からわずか3日で再び操業停止した。</div>
        <div class="s-src">出典: Reuters / CNBC / Egypt Cabinet（7/30〜31 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 外交・海峡管理（イラン主張と対オマーン協議）

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="s-title">🇴🇲 イラン、オマーンの海峡共同管理（50-50）案を拒否——単独管理の立場を維持／茂木外相はアラグチ外相と会談</div>
        <div class="s-body">イランは、オマーンが提示していたホルムズ海峡の共同管理（入航路線・出航路線を折半する50-50案）を拒否し、単独での完全管理の立場を維持したと報じられた。前日までの「次官級協議は建設的」との評価とは裏腹に、通航管理の主権を巡る溝は埋まっていない。茂木外相は7/28夜にアラグチ外相と電話会談し、覚書に沿った対米協議継続を要請するとともに、拘束後保釈された邦人1名の早期解決を改めて求めた。フーシ派はサウジ船のインド洋方面航行を標的にすると宣言し、海運各社はスエズ運河迂回を検討している。</div>
        <div class="s-src">出典: Trading Economics / 外務省 / CNN（7/28〜29 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="s-title">🇮🇷 イラン、タンカー2隻拿捕を主張——オマーン海峡共同管理案は「成功の見込みなし」と拒否</div>
        <div class="s-body">イランは、「米軍護衛下」でホルムズ海峡を出域しようとしたタンカー2隻を拿捕、別の4隻を引き返させたと発表したが、ロイターによれば西側の独立した海事監視機関はこの主張を確認できていない。同日、大型タンカー2隻の通航自体は確認された。外交面では、イラン高官がオマーン提案の50-50共同管理案を「成功の見込みはない」と改めて拒否——入航路線全域・出航路線一部の単独管理に固執し、オマーンが受け入れなければ協議は次段階に進まないとの姿勢を示した。</div>
        <div class="s-src">出典: Reuters / WSJ経由（7/29〜31 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ 船舶・市場（日本関係船・原油）

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/30再確認）——原油はブレント90ドル台まで急騰</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/30 10:08 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。原油はイランの奇襲攻撃・米の報復空爆を受け急騰し、ブレントは7/29 14:30ET時点で90.66ドル（前日比+7%）まで上昇。米API統計では原油在庫が前週比330万バレル減少し供給逼迫が継続。QatarEnergyのLNG不可抗力は9月中旬（一部10月）まで延長中。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残17日に迫っている。</div>
        <div class="s-src">出典: CNN / Reuters / Trading Economics（7/29 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（8/1再確認）——原油は7月月間+23%の見通し</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（8/1 10:51 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。原油はダミエッタ港攻撃・CPC再停止・イランのタンカー拿捕主張を受け続伸し、ブレントは7/31 NY終値で90.12ドル、WTIは84.67ドル（ともに前日比+1%超）——ブレントは7月月間で+23%上昇の見通しとロイター調査のアナリストは市場のさらなる上昇を予想する。QatarEnergyのLNG不可抗力は9月中旬（一部10月）まで延長中。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残15日に迫っている。</div>
        <div class="s-src">出典: Reuters / CNBC（7/31 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN Phaseラベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 15「米・イラン停戦崩壊——IRGC奇襲・米報復空爆・イランはオマーン海峡共同管理案を拒否」——封鎖153日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 16「戦線がエジプト・黒海へ拡大——ダミエッタ港LNG船被弾・CPC再停止・イランはタンカー拿捕を主張」——封鎖155日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率更新補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
    各シナリオ確率は 2026年7月30日 10:08 JST 時点での分析に基づく自動同期
<!-- OLD:END -->
<!-- NEW:START -->
    各シナリオ確率は 2026年8月1日 10:51 JST 時点での分析に基づく自動同期
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] 4つのシナリオ本文

### シナリオA（外交解決）

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>7/25未明から3日間続いた攻撃休止は7/28夜のIRGCによる米軍拠点への奇襲攻撃で崩壊した。さらにイランは、オマーンが提示していたホルムズ海峡の共同管理（50-50）案を拒否し、単独管理の立場を維持した。次官級協議の「建設的」評価は一夜で覆り、段階的なMOU履行という外交シナリオの実現可能性は明確に後退した。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イラン高官がオマーン提案を「成功の見込みなし」と明確に拒否し、入航路線全域の単独管理という当初来の要求を崩さなかったことで、外交トラックはさらに後退した。加えて、タンカー拿捕やダミエッタ港・CPCへの攻撃拡大は、対話環境そのものを損なう方向に作用しており、A シナリオの実現可能性は一段と低下したと評価する。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB（膠着継続）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>米・イラン間の直接空爆は7/30夜〜31未明にかけ新たな報告がなく、短期的な小康状態が続いている。一方でホルムズ海峡そのものではなく周辺海域（エジプト・黒海）で新たな攻撃が続いており、「海峡内は膠着、周辺は拡大」という複線的な構図が定着しつつある点が今週の特徴である。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC（完全封鎖の制度化）

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>イランがオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持したことは、通航管理権限を制度的に固定化する路線がむしろ強化されたことを示す。フーシ派によるサウジ船インド洋方面標的化の宣言も、紅海側での「管理の制度化」圧力を新たに加えるものだ。米イラン間の攻撃休止崩壊・報復応酬により、シナリオCの水準はやや上昇したと評価する。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イラン高官が改めて「50-50案は成功の見込みなし」と明言し、オマーンが受諾しない限り次段階協議には進まないとの姿勢を示したことは、イラン主導の管理体制を既成事実化しようとする意図の表れと読める。同時に、タンカー拿捕の主張という新たな実力行使的手段も加わり、通航管理を巡るイランの主導権固定化シナリオの蓋然性はさらに高まったと評価する。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD（軍事エスカレーション）

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>7/25〜28の3日間の攻撃休止はIRGCによる米軍拠点への奇襲攻撃で崩壊し、米・サウジはイラク国内の親イラン民兵拠点を合同空爆、トランプ大統領は7/29夜（米時間）に対イラン報復空爆を開始したと報じられた。原油先物の急騰（ブレント+7%）は市場が軍事エスカレーションの再燃を織り込み始めたことを示す。フーシ派によるサウジ船インド洋方面標的化という新たなリスク要因も加わり、シナリオDの水準は明確に上昇したと評価する。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>米・イラン間の直接空爆自体は7/30夜〜31未明に報告がなく一時的に落ち着いたが、代わって戦域そのものが地中海（ダミエッタ港）・黒海（CPC）へと地理的に拡大しており、局地的エスカレーションのリスクが新たな地域へ波及している。イランによるタンカー拿捕の主張が事実であれば、米軍護衛下の船舶に対する直接的な実力行使という新段階に踏み込むことになり、Dシナリオの警戒水準は引き続き高い状態を維持していると評価する。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5つ）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米の報復空爆の規模とイランの対応（更なる報復かエスカレーション停止か）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン・オマーン海峡共同管理協議の帰趨（50-50案拒否後の展開）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">フーシ派のサウジ船インド洋方面標的化と紅海ルートへの波及</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">茂木・アラグチ電話会談後の拘束邦人問題の進展</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月30日 10:08 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">ダミエッタ港・CPCへの攻撃拡大が他地域へさらに波及するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン主張のタンカー拿捕・引き返し情報の第三者機関による裏付け有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">イラン・オマーン協議の次の展開（イラン対案の行方）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">米・イラン間の空爆休止が継続するか、再開の引き金の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保（変わらず最重要）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月1日 10:51 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒で全体像を把握（3行サマリー＋バッジ）― 必ず最後に確認

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
⚔️ 米・イランの攻撃休止は3日で終了——IRGCが米軍拠点へ奇襲も全弾迎撃、米・サウジはイラク民兵拠点を合同空爆。トランプ氏は報復空爆を開始。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇴🇲 イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理を維持——原油はブレント90.66ドルまで急騰・日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 米の報復空爆の規模とイランの対応が焦点、封鎖153日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残17日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
🌍 戦線がエジプト・ダミエッタ港とカザフスタンCPCターミナルへ拡大——ホルムズ本体は空爆こそ小康状態だが、周辺海域で新たな攻撃が相次ぐ。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷 イランは「米軍護衛下」のタンカー2隻を拿捕したと主張（西側未確認）——オマーンとの共同管理協議は「成功の見込みなし」と決裂。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 空爆休止が続くか、戦線拡大の裏付け情報が焦点、封鎖155日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残15日。
</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ（5枚）

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️IRGC奇襲・全弾迎撃</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸米、報復空爆を開始</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇴🇲イラン、50-50共同管理案を拒否</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油急騰・ブレント90.66ドル(+7%)</span>
        </div>

        </div>
      </div>

      <!-- ジャンプ＋クリッカブルバッジ -->
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🔥ダミエッタ港LNG船が被弾</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️CPCノヴォロシースク再停止</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷イラン、タンカー拿捕を主張(未確認)</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油続伸・ブレント90.12ドル</span>
        </div>

        </div>
      </div>

      <!-- ジャンプ＋クリッカブルバッジ -->
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S09完了

---

## [S10] news_data.json 更新

### updated フィールド

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月30日 10:08 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年8月1日 10:51 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列（新規4件を先頭に追加、旧latest後半4件をarchiveへ移動）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-irgc-surprise-attack-us-bases-0728",
      "title": "IRGC、米軍拠点へ弾道ミサイル奇襲——全弾迎撃、攻撃休止は3日で終了",
      "body": "米中央軍（CENTCOM）は7月28日夜、イラン革命防衛隊（IRGC）が中東の米軍拠点へ弾道ミサイルによる奇襲攻撃を試みたが、全弾を迎撃したと発表した。7月25日未明から続いていた攻撃休止は3日で終了した。米・サウジ両軍は合同で、直近72時間に30件超の攻撃を行っていた親イラン系民兵拠点をイラク国内で空爆した。",
      "sourceLabel": "Reuters / CENTCOM",
      "date": "2026年7月28日（現地）/ 2026年7月29日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.pressdemocrat.com/2026/07/28/iran-us-troops-missile-attack/",
      "isLatest": true
    },
    {
      "id": "latest-trump-retaliation-strikes-0729",
      "title": "トランプ氏「対イラン報復攻撃を実施」——7/29夜（米時間）に新たな空爆開始",
      "body": "トランプ大統領はイランの奇襲攻撃を受け、対イランへの強い報復攻撃を実施すると警告し、7月29日夜（米東部時間）に新たな対イラン空爆を開始したと報じられた。CENTCOMは同日、米・サウジ両軍によるイラク国内の親イラン系民兵拠点への攻撃も発表している。",
      "sourceLabel": "CBS News",
      "date": "2026年7月29日（現地）/ 2026年7月30日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.cbsnews.com/live-updates/us-iran-war-trump-saudi-arabia-strait-of-hormuz/",
      "isLatest": false
    },
    {
      "id": "latest-iran-rejects-oman-5050-proposal-0728",
      "title": "イラン、オマーンの海峡共同管理（50-50）案を拒否——単独管理の立場を維持",
      "body": "イランは、ホルムズ海峡の管理をオマーンと折半する共同管理案を拒否し、入航路線・出航路線の一部について単独での完全管理を維持する立場を崩さなかったと報じられた。米国のAPIデータでは原油在庫が前週比330万バレル減少し、供給逼迫の継続も示された。",
      "sourceLabel": "Trading Economics",
      "date": "2026年7月28日（現地）/ 2026年7月29日 JST",
      "label": "🕊️ 外交",
      "url": "https://tradingeconomics.com/commodity/brent-crude-oil",
      "isLatest": false
    },
    {
      "id": "latest-trump-talks-progress-0727",
      "title": "トランプ氏「イランと協議中、合意に近づく可能性」——ウォルツ大使は空爆停止の理由を説明",
      "body": "トランプ大統領は7月27日、米国とイランが協議を行っており合意に至る可能性があると述べた。協議が失敗すれば攻撃を再開する可能性にも言及。ウォルツ国連大使は、大統領が「協議に時間的余地を与えるため」攻撃を休止したと説明した。報道によれば米軍指揮官は攻撃対象の枯渇や防空兵器の消耗への懸念を進言していたという。",
      "sourceLabel": "Reuters",
      "date": "2026年7月27日（現地）/ 2026年7月27日 JST",
      "label": "🕊️ 外交",
      "url": "https://www.reuters.com/world/middle-east/iran-says-it-still-controls-strait-not-seeking-talks-after-trump-halts-bombing-2026-07-27/",
      "isLatest": false
    },
    {
      "id": "latest-iran-oman-talks-constructive-0726",
      "title": "イラン、米との協議否定も「オマーンとの通航協議は建設的」——次官級でテヘラン協議",
      "body": "イラン外務省のバガイ報道官は、米国との協議再開を要請したとの報道を否定し、ホルムズ海峡の通航状況にも変更はないと説明した。一方、イランとオマーンは7月25〜26日にテヘランで次官級協議を実施し、沿岸国の主権を尊重しつつ安全な通航を管理する共通原則・運用メカニズムについて意見交換した。対象船舶・航路・料金・発効時期を定めた合意文書は公表されていない。",
      "sourceLabel": "Reuters / IRNA",
      "date": "2026年7月26日〜27日（現地）/ 2026年7月27日 JST",
      "label": "🕊️ 外交",
      "url": "https://www.reuters.com/world/middle-east/iran-has-not-asked-resumption-talks-with-us-iranian-spokesperson-says-2026-07-27/",
      "isLatest": false
    },
    {
      "id": "latest-hormuz-7ships-oil-slump-0727",
      "title": "ホルムズ通航、7/26も7隻に留まる——原油は攻撃休止・外交期待で急落",
      "body": "Kpler・Windward双方の集計で、7月26日のホルムズ海峡通航は7隻にとどまったことが判明。全船がイラン指定の北側航路を利用し、イランは無許可で通過を試みた船舶6隻を引き返させたと主張。原油先物は攻撃休止と外交進展期待を受け急落し、ブレントは7月27日夜時点で89.68ドル（前日比-7.3%）、WTIは83.18ドル（同-6.9%）。インド国営MRPLは原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記した。",
      "sourceLabel": "Kpler / Windward / Reuters",
      "date": "2026年7月26日〜27日（現地）/ 2026年7月28日 JST",
      "label": "⚓ 海上輸送",
      "url": "https://www.reuters.com/business/energy/oil-slips-more-than-5-after-us-pauses-strikes-iran-2026-07-26/",
      "isLatest": false
    }
  ],
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "id": "latest-damietta-drone-attack-lng-0729",
      "title": "エジプト・ダミエッタ港でLNG貯蔵船2隻がドローン攻撃——今次紛争で初のエジプト領内攻撃",
      "body": "エジプト北部ダミエッタ港で7月29日（現地）、米企業所有のLNG貯蔵再ガス化船「エナゴス・ウィンター」がドローン攻撃を受け出火し、隣接するLNGタンカー「ガスログ・セーラム」にも延焼した。エジプト内閣府は7月30日、ドローン攻撃であったことを確認。乗組員は避難し負傷者はいない。犯行声明は出ていないが、イラン国営テレビが2日前にダミエッタを対ウクライナ報復の候補地として名指ししていたと報じられている。",
      "sourceLabel": "Reuters / CNBC",
      "date": "2026年7月29日（現地）/ 2026年7月30日 JST",
      "label": "🔥 施設攻撃",
      "url": "https://www.cnbc.com/2026/07/30/egypt-drone-gas-ship-damietta-port-iran-war.html",
      "isLatest": true
    },
    {
      "id": "latest-iran-claims-tanker-seizure-0731",
      "title": "イラン、ホルムズ海峡でタンカー2隻を拿捕・4隻を引き返させたと主張——西側は未確認",
      "body": "イランは、「米軍護衛下」でホルムズ海峡を出域しようとしたタンカー2隻を拿捕し、別の4隻についてもイラン部隊の介入を受けて引き返したと発表した。ロイターによれば、これらの主張は独立した第三者機関による確認が取れていない。同日、大型タンカー2隻の通航自体は確認されており、原油価格は1%超上昇した。",
      "sourceLabel": "Reuters",
      "date": "2026年7月31日（現地）/ 2026年7月31日 JST",
      "label": "⚓ 海上輸送",
      "url": "https://www.investing.com/news/commodities-news/oil-price-rises-after-iran-says-it-stops-ships-in-hormuz-4828985",
      "isLatest": false
    },
    {
      "id": "latest-cpc-novorossiysk-suspended-again-0730",
      "title": "カザフスタンCPCターミナル、タンカー攻撃受け3日で再停止——7月中8隻超が被弾",
      "body": "カザフスタンの主要原油輸出ルートであるカスピ海パイプラインコンソーシアム（CPC）は、黒海ノヴォロシースク近郊でタンカー「ニソス・シフノス」（積み込み中に被弾・火災）と「マラティ」（接近中に攻撃）が攻撃を受けたことを受け、積み出しを再び停止した。7月27日の再開からわずか3日での再停止で、7月中にCPC関連で攻撃を受けたタンカーは少なくとも8隻に達した。",
      "sourceLabel": "The Times of Central Asia",
      "date": "2026年7月30日（現地）/ 2026年7月30日 JST",
      "label": "🛢️ エネルギー",
      "url": "https://timesca.com/breaking-cpc-halts-oil-loadings-again-after-two-more-tankers-attacked-near-novorossiysk/",
      "isLatest": false
    },
    {
      "id": "latest-oil-surge-brent-90-july-0731",
      "title": "原油続伸、ブレント90ドル台——7月月間ではブレント+23%の見通し",
      "body": "原油価格は7月31日、イランのタンカー拿捕主張とダミエッタ港攻撃を受けて上昇し、ブレントは90.12ドル、WTIは84.67ドルで終値を付けた（ともに前日比+1%超）。ベンチマークのブレント原油先物は7月の月間上昇率で+23%となる見通しで、ロイターが調査したエコノミスト・アナリストは今後さらなる価格上昇を予想している。",
      "sourceLabel": "CNBC / Reuters",
      "date": "2026年7月31日（現地）/ 2026年7月31日 JST",
      "label": "🛢️ エネルギー",
      "url": "https://www.cnbc.com/2026/07/31/oil-prices-today-brent-wti-hormuz-trump-iran-.html",
      "isLatest": false
    },
    {
      "id": "latest-irgc-surprise-attack-us-bases-0728",
      "title": "IRGC、米軍拠点へ弾道ミサイル奇襲——全弾迎撃、攻撃休止は3日で終了",
      "body": "米中央軍（CENTCOM）は7月28日夜、イラン革命防衛隊（IRGC）が中東の米軍拠点へ弾道ミサイルによる奇襲攻撃を試みたが、全弾を迎撃したと発表した。7月25日未明から続いていた攻撃休止は3日で終了した。米・サウジ両軍は合同で、直近72時間に30件超の攻撃を行っていた親イラン系民兵拠点をイラク国内で空爆した。",
      "sourceLabel": "Reuters / CENTCOM",
      "date": "2026年7月28日（現地）/ 2026年7月29日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.pressdemocrat.com/2026/07/28/iran-us-troops-missile-attack/",
      "isLatest": false
    },
    {
      "id": "latest-trump-retaliation-strikes-0729",
      "title": "トランプ氏「対イラン報復攻撃を実施」——7/29夜（米時間）に新たな空爆開始",
      "body": "トランプ大統領はイランの奇襲攻撃を受け、対イランへの強い報復攻撃を実施すると警告し、7月29日夜（米東部時間）に新たな対イラン空爆を開始したと報じられた。CENTCOMは同日、米・サウジ両軍によるイラク国内の親イラン系民兵拠点への攻撃も発表している。",
      "sourceLabel": "CBS News",
      "date": "2026年7月29日（現地）/ 2026年7月30日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.cbsnews.com/live-updates/us-iran-war-trump-saudi-arabia-strait-of-hormuz/",
      "isLatest": false
    }
  ],
<!-- NEW:END -->
<!-- APPLY:END -->

### archive への新規バッチ追加（latestから押し出された旧4件）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "archive": [
    {
      "batchLabel": "2026年7月25日〜26日",
<!-- OLD:END -->
<!-- NEW:START -->
  "archive": [
    {
      "batchLabel": "2026年7月28日〜29日",
      "items": [
        {
          "id": "latest-iran-rejects-oman-5050-proposal-0728",
          "title": "イラン、オマーンの海峡共同管理（50-50）案を拒否——単独管理の立場を維持",
          "body": "イランは、ホルムズ海峡の管理をオマーンと折半する共同管理案を拒否し、入航路線・出航路線の一部について単独での完全管理を維持する立場を崩さなかったと報じられた。米国のAPIデータでは原油在庫が前週比330万バレル減少し、供給逼迫の継続も示された。",
          "sourceLabel": "Trading Economics",
          "date": "2026年7月28日（現地）/ 2026年7月29日 JST",
          "label": "🕊️ 外交",
          "url": "https://tradingeconomics.com/commodity/brent-crude-oil",
          "isLatest": false
        },
        {
          "id": "latest-trump-talks-progress-0727",
          "title": "トランプ氏「イランと協議中、合意に近づく可能性」——ウォルツ大使は空爆停止の理由を説明",
          "body": "トランプ大統領は7月27日、米国とイランが協議を行っており合意に至る可能性があると述べた。協議が失敗すれば攻撃を再開する可能性にも言及。ウォルツ国連大使は、大統領が「協議に時間的余地を与えるため」攻撃を休止したと説明した。報道によれば米軍指揮官は攻撃対象の枯渇や防空兵器の消耗への懸念を進言していたという。",
          "sourceLabel": "Reuters",
          "date": "2026年7月27日（現地）/ 2026年7月27日 JST",
          "label": "🕊️ 外交",
          "url": "https://www.reuters.com/world/middle-east/iran-says-it-still-controls-strait-not-seeking-talks-after-trump-halts-bombing-2026-07-27/",
          "isLatest": false
        },
        {
          "id": "latest-iran-oman-talks-constructive-0726",
          "title": "イラン、米との協議否定も「オマーンとの通航協議は建設的」——次官級でテヘラン協議",
          "body": "イラン外務省のバガイ報道官は、米国との協議再開を要請したとの報道を否定し、ホルムズ海峡の通航状況にも変更はないと説明した。一方、イランとオマーンは7月25〜26日にテヘランで次官級協議を実施し、沿岸国の主権を尊重しつつ安全な通航を管理する共通原則・運用メカニズムについて意見交換した。対象船舶・航路・料金・発効時期を定めた合意文書は公表されていない。",
          "sourceLabel": "Reuters / IRNA",
          "date": "2026年7月26日〜27日（現地）/ 2026年7月27日 JST",
          "label": "🕊️ 外交",
          "url": "https://www.reuters.com/world/middle-east/iran-has-not-asked-resumption-talks-with-us-iranian-spokesperson-says-2026-07-27/",
          "isLatest": false
        },
        {
          "id": "latest-hormuz-7ships-oil-slump-0727",
          "title": "ホルムズ通航、7/26も7隻に留まる——原油は攻撃休止・外交期待で急落",
          "body": "Kpler・Windward双方の集計で、7月26日のホルムズ海峡通航は7隻にとどまったことが判明。全船がイラン指定の北側航路を利用し、イランは無許可で通過を試みた船舶6隻を引き返させたと主張。原油先物は攻撃休止と外交進展期待を受け急落し、ブレントは7月27日夜時点で89.68ドル（前日比-7.3%）、WTIは83.18ドル（同-6.9%）。インド国営MRPLは原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記した。",
          "sourceLabel": "Kpler / Windward / Reuters",
          "date": "2026年7月26日〜27日（現地）/ 2026年7月28日 JST",
          "label": "⚓ 海上輸送",
          "url": "https://www.reuters.com/business/energy/oil-slips-more-than-5-after-us-pauses-strikes-iran-2026-07-26/",
          "isLatest": false
        }
      ]
    },
    {
      "batchLabel": "2026年7月25日〜26日",
<!-- NEW:END -->
<!-- APPLY:END -->

### osint（現地メディア視点）最新1件を追加・旧isLatestをfalseへ

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "titleJa": "【Al Jazeera】イラン、ヨルダンの米軍拠点を攻撃——トランプ氏はネタニヤフ氏と会談中",
      "titleEn": "Iran attacks US forces in Jordan as Trump meets Netanyahu",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/2026/7/29/iran-attacks-us-bases-in-middle-east-as-trump-meets-netanyahu",
      "date": "2026年7月29日（現地）/ 2026年7月29日 JST",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "titleJa": "【Al Jazeera】エジプト、ダミエッタ港の船舶火災はドローン攻撃と確認",
      "titleEn": "Egypt says fire on ships at Damietta port caused by drone",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/2026/7/29/fire-erupts-on-ships-at-egypts-damietta-port",
      "date": "2026年7月30日（現地）/ 2026年7月30日 JST",
      "isLatest": true
    },
    {
      "titleJa": "【Al Jazeera】イラン、ヨルダンの米軍拠点を攻撃——トランプ氏はネタニヤフ氏と会談中",
      "titleEn": "Iran attacks US forces in Jordan as Trump meets Netanyahu",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/2026/7/29/iran-attacks-us-bases-in-middle-east-as-trump-meets-netanyahu",
      "date": "2026年7月29日（現地）/ 2026年7月29日 JST",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S10完了（latest 4件新規追加・archiveへ4件退避・osint 1件追加）

---

## [S11] 更新ログ（2ブロック構成・必須）

### ブロック1：常時表示エリアの更新（3件固定を維持）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年7月30日 10:08 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/30 10:08</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米・イランの攻撃休止は3日（7/25〜28）で終了——IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM）・米・サウジはイラク国内の親イラン民兵拠点を合同空爆・トランプ大統領は報復を予告し7/29夜（米時間）に新たな対イラン空爆を開始と判明・イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持・茂木外相はアラグチ外相と電話会談し覚書に沿った対米協議継続を要請・拘束邦人1名の早期解決も改めて要請・フーシ派はサウジ船のインド洋方面航行を標的化すると宣言・原油はブレント90.66ドルまで急騰（前日比+7%）・日本関係船は残り4隻で変化なし・封鎖153日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月28日 10:19 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/28 10:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領「イランと協議中、合意に近づく可能性」（7/27）——一方イラン外務省バガイ報道官は米との直接協議要請を否定し通航状況も不変と主張・イラン・オマーンは7/25〜26テヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表・ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張（Kpler/Windward）・フーシ派、サウジ東西輸送網へ無人機攻撃を発表——紅海側にもリスク拡大・原油は攻撃休止・外交期待で急落しブレント89.68ドル（前日比-7.3%）・インドMRPLが原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記・日本関係船は残り4隻で変化なし・封鎖151日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月26日 10:30 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/26 10:30</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態・オマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展（オマーン外交団7/24テヘラン訪問）・IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表・フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明・原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）・米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇・日本関係船は残り4隻で変化なし・封鎖149日目・ニュース3件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月1日 10:51 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/01 10:51</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>戦線が中東域外へ拡大——エジプト・ダミエッタ港でLNG貯蔵船「エナゴス・ウィンター」がドローン攻撃を受け出火、隣接LNG船「ガスログ・セーラム」にも延焼（今次紛争で初のエジプト領内攻撃・Reuters/CNBC）・カザフスタンのCPCノヴォロシースク積出ターミナルもタンカー攻撃を受け3日で再停止（7月中8隻超が被弾）・イランは「米軍護衛下」で海峡を出域しようとしたタンカー2隻を拿捕・4隻を引き返させたと主張したが西側は未確認（Reuters）・オマーンとの海峡共同管理協議はイラン高官が「成功の見込みなし」と改めて拒否・米・イラン間の直接空爆は7/30夜〜31未明は報告なし・原油はブレント90.12ドル・WTI84.67ドル（ともに前日比+1%超・7月月間+23%見通し）・日本関係船は残り4隻で変化なし・封鎖155日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年7月30日 10:08 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/30 10:08</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米・イランの攻撃休止は3日（7/25〜28）で終了——IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM）・米・サウジはイラク国内の親イラン民兵拠点を合同空爆・トランプ大統領は報復を予告し7/29夜（米時間）に新たな対イラン空爆を開始と判明・イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持・茂木外相はアラグチ外相と電話会談し覚書に沿った対米協議継続を要請・拘束邦人1名の早期解決も改めて要請・フーシ派はサウジ船のインド洋方面航行を標的化すると宣言・原油はブレント90.66ドルまで急騰（前日比+7%）・日本関係船は残り4隻で変化なし・封鎖153日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月28日 10:19 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/28 10:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領「イランと協議中、合意に近づく可能性」（7/27）——一方イラン外務省バガイ報道官は米との直接協議要請を否定し通航状況も不変と主張・イラン・オマーンは7/25〜26テヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表・ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張（Kpler/Windward）・フーシ派、サウジ東西輸送網へ無人機攻撃を発表——紅海側にもリスク拡大・原油は攻撃休止・外交期待で急落しブレント89.68ドル（前日比-7.3%）・インドMRPLが原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記・日本関係船は残り4隻で変化なし・封鎖151日目・ニュース3件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse 先頭への旧3件目（7/26 10:30分）の挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月24日 09:23 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月26日 10:30 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/26 10:30</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態・オマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展（オマーン外交団7/24テヘラン訪問）・IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表・フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明・原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）・米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇・日本関係船は残り4隻で変化なし・封鎖149日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年7月24日 09:23 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：合計件数調整（11件→10件、最古の7/14 08:48分を削除）

> 常時表示3件（8/1・7/30・7/28）＋log-collapse 8件（7/26・7/24・7/22・7/19・7/16・7/14 18:00・7/14 16:16・7/14 08:48）＝11件となり上限10件を超過するため、log-collapse内の最古エントリー（7/14 08:48分）を削除し、`docs/data/update_log.json` の先頭に追加してください。

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月14日 08:48 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/14 08:48</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明（封鎖発効は7/14 20:00 GMT予定）・アラグチー外相「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる」と税率交渉に含み・イラン軍ハタム・アル・アンビヤ司令部は米国の海峡管理への干渉を許さないと強調・IMOは強制通航料に法的根拠なしとして断固反対・中国外務省も安全な航行確保を要求・米軍は3夜連続の対イラン空爆を継続・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント7/13終値78.85ドル（+3.74%）後、同日夜一時83ドル台まで急伸・封鎖137日目・ニュース3件更新・osint更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S11完了（常時表示3件固定・log-collapse 4件目以降8件→7件に整理）

---

## [SHIP_CONFIG] C01タンカー確認

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年7月30日 10:08 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。米・イランの攻撃休止は3日で終了しIRGCが米軍拠点へ奇襲・米は報復空爆を開始。イランはオマーンの海峡共同管理案を拒否し単独管理を維持）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年8月1日 10:51 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。戦線はエジプト・ダミエッタ港とカザフスタンCPCへ拡大、イランはタンカー拿捕を主張したが西側未確認。オマーンとの海峡共同管理協議は決裂）'
<!-- NEW:END -->
<!-- APPLY:END -->

**C01 タンカー確認**：日本語「日本関係船舶 ホルムズ海峡 通過 足止め」「外務省 ホルムズ海峡 日本関係船舶」「金子国土交通大臣 記者会見 ホルムズ海峡 日本関係船舶」＋英語「Japanese ships Strait of Hormuz stranded detained」の4クエリ全てでweb検索済み（外務省・国土交通省の一次情報を優先確認）／変化なし→残り4隻のまま・dateConfirmedを本日日時「変更なし」で更新

✓ SHIP_CONFIG完了

---

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-30T10:08:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-01T10:51:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

✓ JSON-LD完了

---

## [archive] archive_timeline.json への追記分（新規1エントリ）

> Claude Code への指示：`docs/data/archive_timeline.json` の `entries` 配列末尾に、以下のエントリーを追加してください（既存エントリーは変更しないこと）。

```json
{
  "date": "2026-08-01",
  "dateLabel": "2026/08/01 10:51",
  "blockadeDay": 155,
  "summary": "戦線が中東域外へ拡大——エジプト・ダミエッタ港でLNG貯蔵船「エナゴス・ウィンター」がドローン攻撃を受け出火、隣接LNG船「ガスログ・セーラム」にも延焼（今次紛争で初のエジプト領内攻撃・Reuters/CNBC）・カザフスタンのCPCノヴォロシースク積出ターミナルもタンカー攻撃を受け3日で再停止（7月中8隻超が被弾）・イランは「米軍護衛下」で海峡を出域しようとしたタンカー2隻を拿捕・4隻を引き返させたと主張したが西側は未確認（Reuters）・オマーンとの海峡共同管理協議はイラン高官が「成功の見込みなし」と改めて拒否・米・イラン間の直接空爆は7/30夜〜31未明は報告なし・原油はブレント90.12ドル・WTI84.67ドル（ともに前日比+1%超・7月月間+23%見通し）・日本関係船は残り4隻で変化なし・封鎖155日目・ニュース4件更新・osint更新",
  "relatedNews": [
    {"title": "エジプト・ダミエッタ港でLNG貯蔵船2隻がドローン攻撃——今次紛争で初のエジプト領内攻撃", "url": "https://www.cnbc.com/2026/07/30/egypt-drone-gas-ship-damietta-port-iran-war.html", "sourceLabel": "Reuters / CNBC"},
    {"title": "イラン、ホルムズ海峡でタンカー2隻を拿捕・4隻を引き返させたと主張——西側は未確認", "url": "https://www.investing.com/news/commodities-news/oil-price-rises-after-iran-says-it-stops-ships-in-hormuz-4828985", "sourceLabel": "Reuters"},
    {"title": "カザフスタンCPCターミナル、タンカー攻撃受け3日で再停止——7月中8隻超が被弾", "url": "https://timesca.com/breaking-cpc-halts-oil-loadings-again-after-two-more-tankers-attacked-near-novorossiysk/", "sourceLabel": "The Times of Central Asia"},
    {"title": "原油続伸、ブレント90ドル台——7月月間ではブレント+23%の見通し", "url": "https://www.cnbc.com/2026/07/31/oil-prices-today-brent-wti-hormuz-trump-iran-.html", "sourceLabel": "CNBC / Reuters"}
  ]
}
```

✓ archive完了

---

## ✅ 出力前セルフチェック（本日：15項目）

```
[x] S01 ヘッダー ― 2026年8月1日 10:51 JST ✓
[x] S02 TICKER ― ダミエッタ港攻撃・タンカー拿捕主張・CPC再停止・オマーン案拒否・封鎖155日目 ✓
[x] S03 速報インシデント ― 8/1 10:51付け・4件新規追加（重複なし・各々異なる文体で記述）✓
[x] S04 情勢カード3枚 ― 日付・数値・出典を8/1版に更新（S02/S03と表現を変えて記述）✓
[x] S05 COUNTDOWN ― Phase16・封鎖155日目 ✓
[x] S06 シナリオ確率補足バナー ― 8/1 10:51 JST日付更新 ✓
[x] S07 シナリオ4本 ― A/B/C/D本文を8/1情勢に更新（ダミエッタ・CPC・拿捕主張・空爆休止を反映、各シナリオで異なる切り口）✓
[x] S08 シナリオフッター ― 次の焦点5点を8/1版に更新 ✓
[x] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成・他セクションと表現を変更）✓
[x] S10 news_data.json更新 ― latest 4件新規・archiveへ4件退避・osint 1件追加・updated日付 ✓
[x] S11 更新ログ ― 3ブロック構成で常時表示3件固定・log-collapse整理・11件→10件に調整 ✓
[x] SHIP_CONFIG ― C01確認・4隻のまま変化なし・dateConfirmed更新 ✓
[x] JSON-LD ― dateModified を 2026-08-01 に更新 ✓
[x] archive_timeline.json ― 新規1エントリ追記分を出力 ✓
[x] 全体 ― ニュースURLは全てweb検索で実在確認済み（AI捏造なし）✓

二重封鎖表記チェック：本文中に単独「二重封鎖」表記なし（COUNTDOWN内の既存「イラン・米国による二重封鎖」表記は変更なし）✓
TICKER内JST表記チェック：全日付にJST付き ✓
Al Jazeera混入チェック：latestには使用せず、osintのみに配置 ✓
人名表記チェック：「Xi」等の単独表記なし ✓
S09作成順チェック：S01〜S08確定後に最後に作成 ✓
```

### ⚠️ 未実施・要確認項目

1. **封鎖日カウンターの起算日の不整合**（冒頭に記載の通り）。Memory記載の「4/13起算」と、ライブサイトの実運用「2/28起算（GEF等外部集計と一致）」が食い違っています。次回セッションまでにどちらの基準を正とするか、ユーザーの決定をお願いします。決定後、Memory更新（`memory_user_edits`）またはサイト側の日数遡及修正のいずれかが必要になります。
2. 茂木・アラグチ電話会談や邦人拘束問題について、7/28以降の新規動きはweb検索で確認できませんでした（進展があり次第、次回反映します）。
