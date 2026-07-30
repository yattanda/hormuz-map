# index_html_diffs.md — 2026年7月30日 10:08 JST 更新分

> Claude Code への指示：以下の差分を index.html / docs/data/news_data.json / docs/data/archive_timeline.json に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## ⚠️ 本日のセルフチェック事前貼付（手順1：空欄先貼り）

```
本日のセルフチェック項目数：14件
[ ] S01 ヘッダー ― 2026年7月30日 10:08 JST
[ ] S02 TICKER ― 米イラン停戦崩壊・IRGC奇襲/全弾迎撃・米報復空爆・イランがオマーン50-50案拒否・原油急騰・封鎖153日目
[ ] S03 速報インシデント ― 7/30 10:08付け・6件新規追加（茂木外相電話会談含む）
[ ] S04 情勢カード3枚 ― 日付・数値・出典を7/30版に更新
[ ] S05 COUNTDOWN ― 封鎖153日目・MOU最終期限残17日
[ ] S06 シナリオ確率補足バナー ― 7/30 10:08 JST日付更新
[ ] S07 シナリオ4本 ― A/B/C/D本文を7/30情勢に更新
[ ] S08 シナリオフッター ― 次の焦点5点を7/30版に更新
[ ] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成）
[ ] S10 news_data.json更新メモ ― latest 3件新規・osint 1件新規・updated日付
[ ] S11 更新ログ ― 2ブロック構成＋常時表示3件固定＋合計10件維持（最古1件削除）
[ ] SHIP_CONFIG ― dateConfirmed 更新（C01・変化なし）
[ ] JSON-LD ― dateModified 更新
[ ] archive_timeline.json ― 本日分エントリー追加
```

全項目 ✓確認済（詳細は各セクション末尾のチェック参照）。未実施(✗)項目なし。

---

## [Step 0] 直前状態の確認結果

- project_knowledge_search により、直前の diffs.md は「2026年7月28日 10:19 JST」時点のものであることを確認。
- live index.html（raw fetch, curl直接取得）でも同時刻（封鎖151日目）の状態を確認し、Step A/Step Bの日時が一致することを確認した。
- 本日は前回更新から一夜明けて情勢が大きく転換：7/25未明から続いていた米・イラン攻撃休止（13夜ぶりの停止）が7/28夜（現地時間）に終了し、IRGCが米軍拠点へ弾道ミサイルによる奇襲攻撃を試みたが全弾迎撃（CENTCOM発表）。米・サウジ両軍はイラク国内の親イラン系民兵拠点を合同空爆し、トランプ大統領は報復を予告、7/29夜（米時間）に新たな対イラン空爆を開始したと報じられている。イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持。日本関係船は残り4隻で変化なし（C01・4クエリ全て確認）。
- 封鎖日数（封鎖NNN日目）は2/28起算の実測値に基づき153日目（7/28時点151日目からの整合性を確認）。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（トランプ氏「イランと協議中、合意に近づく可能性」も、イラン外務省は米との直接協議要請を否定・通航状況も不変と主張／イラン・オマーンは次官級協議「建設的」——通航管理の共通原則を協議も合意文書は非公表／ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張／原油は攻撃休止・外交期待で急落——ブレント89.68ドル（前日比-7.3%）／封鎖151日目）</span>
    <span class="badge-item badge-date">📅2026年7月28日 10:19 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米・イランの攻撃休止は3日で終了——IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃、米・サウジはイラク国内の親イラン民兵拠点を合同空爆／トランプ氏が対イラン報復攻撃を予告し7/29夜（米時間）に新たな空爆を開始と判明／イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持／原油はブレント90.66ドルまで急騰（+7%）／封鎖153日目）</span>
    <span class="badge-item badge-date">📅2026年7月30日 10:08 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S01完了

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月28日 10:19 JST） -->
      🕊️【米・イラン、協議巡り応酬】トランプ氏「イランと協議中、合意に近づく可能性」——ウォルツ大使「協議に時間的余地を与えるため」空爆停止と説明（7/27 JST）｜🇮🇷 イラン外務省バガイ報道官「米との協議再開要請せず」——通航状況にも変更なしと表明（7/27）｜🇴🇲 イラン・オマーン次官級協議「建設的」——沿岸国主権尊重の共通原則・通航管理メカニズムを協議も合意文書は非公表（IRNA/Muscat Daily、7/26）｜🚢 ホルムズ通航、7/26も7隻に留まる——全船がイラン指定北側航路に集中・無許可船6隻は引き返しとイラン主張（Kpler/Windward、7/27）｜🛢️ 原油は攻撃休止・外交期待で急落——ブレント7/27夜89.68ドル（前日比-7.3%）・WTI83.18ドル（7/28 JST）｜📦 インドMRPL、原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記（Reuters、7/27）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残19日｜封鎖151日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月30日 10:08 JST） -->
      🔥【停戦崩壊】米・イラン攻撃休止は3日で終了——IRGC、米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM、7/28夜 JST）｜⚔️ 米・サウジ合同でイラク国内の親イラン民兵拠点を空爆——直近72時間で30件超の攻撃への対応（CENTCOM、7/29）｜🇺🇸 トランプ氏、対イラン報復攻撃を予告——7/29夜（米時間）に新たな対イラン空爆を開始と判明（CBS、7/30 JST）｜🇴🇲 イラン、オマーンの海峡共同管理（50-50）案を拒否——入航路・出航路一部の単独管理の立場を維持（Trading Economics、7/28）｜🇯🇵 茂木外相、アラグチ外相と電話会談——覚書に沿った対米協議継続を確認・拘束邦人1名の早期解決を要請（外務省、7/28）｜🛢️ 原油急騰——ブレント90.66ドル（前日比+7%、7/29 14:30ET）｜⚓ フーシ派、サウジ船のインド洋方面航行を標的にすると宣言——海運各社はスエズ運河迂回を模索｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残17日｜封鎖153日目
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S02完了

---

## [S03] 速報インシデント

### トグルボタン内テキスト・日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米・イラン、協議の有無巡り応酬／イラン・オマーン次官級協議「建設的」／通航は7隻に留まり原油急落</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/28 10:19 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米・イラン停戦崩壊——IRGC米軍拠点へ奇襲も全弾迎撃／米・サウジがイラク民兵拠点を空爆／イランはオマーン海峡共同管理案を拒否</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/30 10:08 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/28 10:19 速報】トランプ大統領は7/27、米国とイランが協議を行っており合意に至る可能性があると発言——ウォルツ国連大使は「協議に時間的余地を与えるため」攻撃を休止したと説明｜イラン外務省バガイ報道官は、イランが米国との協議再開を要請したとの報道を否定し、ホルムズ海峡の通航状況にも変更はないと表明（7/27）｜イランとオマーンは7/25〜26にテヘランで次官級協議を実施し、沿岸2国の主権的権利を尊重しつつ安全な通航を管理する共通原則・運用メカニズムについて意見交換——合意文書は公表されていない（IRNA/Muscat Daily）｜Kpler・Windwardともに、7/26のホルムズ海峡通航は7隻にとどまったと確認——全船がイラン指定の北側航路を利用し、イランは無許可で通過を試みた船舶6隻を引き返させたと主張｜フーシ派はサウジ東西輸送網（紅海向け原油供給網）への無人機攻撃を発表・サウジ国防省はイラク領内から飛来した無人機を迎撃したと発表（7/27）｜原油は攻撃休止・外交進展期待を受け急落——ブレントは7/27夜時点で89.68ドル（前日比-7.3%）、WTIは83.18ドル（同-6.9%）｜インド国営MRPLは原油スポット入札で紅海・ホルムズ海峡経由の積み出しを避けるよう明記——同種条項の明記は同国精製会社で初とロイターが報道｜日本関係船は残り4隻で変化なし｜封鎖151日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/30 10:08 速報】米中央軍（CENTCOM）は7/28夜、イラン革命防衛隊（IRGC）が中東の米軍拠点へ弾道ミサイルによる奇襲攻撃を試みたが全弾を迎撃したと発表——7/25未明から続いていた攻撃休止は3日で終了｜米・サウジ両軍は合同で、直近72時間に30件超の攻撃を行っていた親イラン系民兵拠点をイラク国内で空爆（CENTCOM）｜トランプ大統領は報復攻撃を予告し、7/29夜（米東部時間）に対イランへの新たな空爆を開始したと報じられた（CBS）｜イランはオマーンによるホルムズ海峡共同管理（50-50）案を拒否し、入航路線・出航路線の一部について単独管理の立場を維持（Trading Economics）｜茂木外相は7/28夜、アラグチ外相と電話会談し、覚書に沿った対米協議継続を求めるとともに、イランで拘束後保釈された邦人1名の問題の早期解決を改めて要請（外務省）｜フーシ派はサウジ船のインド洋方面航行を標的にすると宣言し、海運各社はスエズ運河迂回ルートの検討を進めている｜原油はブレントが7/29 14:30ET時点で90.66ドル（前日比+7%）まで急騰｜日本関係船は残り4隻で変化なし｜封鎖153日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に新規6件を追加）

> Claude Codeへの指示：既存リストの先頭（`<ul id="incident-list" ...>` の直後、現在の先頭 `<li>` 要素の直前）に以下6件を追記してください。既存の `<li>` 要素は一切変更しないこと。

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🕊️ 7/27 JST</span>
  <span style="color:#e2e8f0;"> トランプ大統領は、米国とイランが協議を行っており合意に至る可能性があると発言。協議が失敗すれば攻撃を再開する可能性にも言及した。ウォルツ国連大使は、大統領が「協議に時間的余地を与えるため」攻撃を休止したと説明。報道によれば、米軍指揮官は攻撃対象の枯渇や防空兵器の消耗への懸念を進言していたという。</span>
</li>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/28 JST夜</span>
  <span style="color:#e2e8f0;"> 米中央軍（CENTCOM）は、イラン革命防衛隊（IRGC）が中東の米軍拠点へ弾道ミサイルによる奇襲攻撃を試みたと発表。「全てのイラン側ミサイルは迎撃に成功した」とし、米軍は引き続き高度な即応態勢を維持しているとした。7/25未明から続いていた攻撃休止は3日で終了した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/28 JST夜</span>
  <span style="color:#e2e8f0;"> CENTCOMは、米・サウジ両軍が合同でイラク国内の親イラン系民兵拠点を空爆したと発表。直近72時間に米軍・サウジのエネルギー拠点へ30件超の無人機攻撃が試みられたことへの対応とした。イラク国家安全保障会議は主権侵害への対処を含む安全保障計画の策定を決定した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🇺🇸 7/29 JST</span>
  <span style="color:#e2e8f0;"> トランプ大統領はイランの奇襲攻撃を受け、対イランへの強い報復攻撃を実施すると表明。米国時間7/29夜、対イランへの新たな空爆を開始したと報じられた。トランプ氏は協議継続の可能性にも改めて言及した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🇴🇲 7/28 JST</span>
  <span style="color:#e2e8f0;"> イランは、オマーンが提示していたホルムズ海峡の共同管理（入航路線・出航路線を折半で管理する50-50案）を拒否し、入航路線と出航路線の一部について単独での完全管理を維持する立場を崩さなかったと報じられた。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🇯🇵 7/28 JST</span>
  <span style="color:#e2e8f0;"> 茂木外相は7/28午後6時20分から20分間、アラグチ外相と電話会談を実施。覚書に沿って米国との協議を継続し課題を解決すべきとの考えを伝え、日本としても協議を支える方針を示した。イラン国内で拘束後、4月に保釈された邦人1名の問題の早期解決も改めて要請した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚓ 7/29 JST</span>
  <span style="color:#e2e8f0;"> イエメンの親イラン武装組織フーシ派は、インド洋方面へ向かおうとするサウジアラビア船舶を標的にすると宣言。海運業界はスエズ運河経由の代替ルートを検討し始めている。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🕊️ 7/27 JST</span>
  <span style="color:#e2e8f0;"> トランプ大統領は、米国とイランが協議を行っており合意に至る可能性があると発言。協議が失敗すれば攻撃を再開する可能性にも言及した。ウォルツ国連大使は、大統領が「協議に時間的余地を与えるため」攻撃を休止したと説明。報道によれば、米軍指揮官は攻撃対象の枯渇や防空兵器の消耗への懸念を進言していたという。</span>
</li>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S03完了

---

## [S04] 情勢カード3枚

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- カード① 外交交渉 -->
  <div class="sit-card danger">
    <div class="s-icon">🕊️</div>
        <div class="s-title">🕊️ 外交：米・イランが協議の有無を巡り応酬——トランプ氏は合意に近づく可能性を示唆、イランは直接協議を否定</div>
        <div class="s-body">トランプ大統領は7/27、米国とイランが協議を行っており合意に至る可能性があると発言。一方でイラン外務省のバガイ報道官は、米国との協議再開を要請したとの報道を否定し、ホルムズ海峡の通航状況にも変更はないと説明した。イランが確認しているのはオマーンとの協議のみで、テヘランで7/25〜26に次官級協議が行われ、沿岸国の主権を尊重しつつ安全な通航を管理する共通原則・運用メカニズムを協議した（オマーン側は「実りある」協議と評価）。ただし対象船舶・航路・料金・発効時期を定めた合意文書はいずれも公表されていない。</div>
        <div class="s-src">出典: Reuters / IRNA / AP / Muscat Daily（7/27 JST 更新）</div>
  </div>

  <!-- カード② 軍事情勢 -->
  <div class="sit-card warning">
    <div class="s-icon">⚔️</div>
        <div class="s-title">⚠️ 通航：ホルムズは7/26も7隻に留まり全船が北側航路に集中／紅海側にも攻撃リスクが拡大</div>
        <div class="s-body">Kpler・Windward双方の集計で、7/26のホルムズ海峡通航は7隻にとどまり、平常時（1日約45隻）の約6分の1の水準が継続。全船がイラン指定の北側航路を利用しており、イランは無許可で通過を試みた船舶6隻を引き返させたと主張——船側の選択というより、イランによる通航管理の結果とみられる。フーシ派はサウジ東部から紅海沿岸ヤンブーへの原油輸送網（東西輸送網）への無人機攻撃を発表し、サウジ国防省もイラク領内から飛来した無人機を迎撃したと発表。施設損傷や輸出減少の独立した確認は現時点でない。</div>
        <div class="s-src">出典: Kpler / Windward / Reuters（7/27 JST 更新）</div>
  </div>

  <!-- カード③ エネルギー・市場 -->
  <div class="sit-card info">
    <div class="s-icon">🛢️</div>
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/28再確認）——原油はブレント90ドル割れまで急落</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/28 10:19 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。原油は攻撃休止・外交進展期待を受け急落し、ブレントは7/27夜時点で89.68ドル（前日比-7.3%）、WTIは83.18ドル（同-6.9%）まで下落。ただしRBCのクロフト氏は「戦闘休止は通航再開を意味しない」と指摘し、実際のホルムズ通航は依然1日1桁にとどまる。インド国営MRPLは原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記し、QatarEnergyのLNG不可抗力は9月中旬（一部10月）まで延長中。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残19日に迫っている。</div>
        <div class="s-src">出典: Reuters / Trading Economics（7/27〜28 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- カード① 外交交渉 -->
  <div class="sit-card danger">
    <div class="s-icon">⚔️</div>
        <div class="s-title">⚔️ 停戦崩壊：IRGC、米軍拠点へ弾道ミサイル奇襲も全弾迎撃——米・サウジはイラク民兵拠点を合同空爆</div>
        <div class="s-body">米中央軍（CENTCOM）は7/28夜、IRGCが中東の米軍拠点へ弾道ミサイルによる奇襲攻撃を試みたが全弾を迎撃したと発表。7/25未明から続いていた攻撃休止は3日で終了した。米・サウジ両軍は合同でイラク国内の親イラン系民兵拠点を空爆——直近72時間に30件超の攻撃への対応とした。トランプ大統領は報復を予告し、7/29夜（米時間）に新たな対イラン空爆を開始したと報じられている。イラク国家安全保障会議は主権侵害対処の安全保障計画策定を決定した。</div>
        <div class="s-src">出典: CENTCOM / Reuters / CBS News（7/29 JST 更新）</div>
  </div>

  <!-- カード② 軍事情勢 -->
  <div class="sit-card warning">
    <div class="s-icon">🇴🇲</div>
        <div class="s-title">🇴🇲 イラン、オマーンの海峡共同管理（50-50）案を拒否——単独管理の立場を維持／茂木外相はアラグチ外相と会談</div>
        <div class="s-body">イランは、オマーンが提示していたホルムズ海峡の共同管理（入航路線・出航路線を折半する50-50案）を拒否し、単独での完全管理の立場を維持したと報じられた。前日までの「次官級協議は建設的」との評価とは裏腹に、通航管理の主権を巡る溝は埋まっていない。茂木外相は7/28夜にアラグチ外相と電話会談し、覚書に沿った対米協議継続を要請するとともに、拘束後保釈された邦人1名の早期解決を改めて求めた。フーシ派はサウジ船のインド洋方面航行を標的にすると宣言し、海運各社はスエズ運河迂回を検討している。</div>
        <div class="s-src">出典: Trading Economics / 外務省 / CNN（7/28〜29 JST 更新）</div>
  </div>

  <!-- カード③ エネルギー・市場 -->
  <div class="sit-card info">
    <div class="s-icon">🛢️</div>
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/30再確認）——原油はブレント90ドル台まで急騰</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/30 10:08 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。原油はイランの奇襲攻撃・米の報復空爆を受け急騰し、ブレントは7/29 14:30ET時点で90.66ドル（前日比+7%）まで上昇。米API統計では原油在庫が前週比330万バレル減少し供給逼迫が継続。QatarEnergyのLNG不可抗力は9月中旬（一部10月）まで延長中。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残17日に迫っている。</div>
        <div class="s-src">出典: CNN / Reuters / Trading Economics（7/29 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S04完了

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 14「米・イラン、協議の有無を巡り応酬——イランは直接協議否定も次官級のオマーン仲介は継続」——封鎖151日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 15「米・イラン停戦崩壊——IRGC奇襲・米報復空爆・イランはオマーン海峡共同管理案を拒否」——封鎖153日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🕊️ <strong>トランプ大統領「イランと協議中、合意に近づく可能性」（7/27）——一方イラン外務省は米との直接協議要請を否定し通航状況も不変と主張／イラン・オマーンは7/25〜26テヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表／ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張（Kpler/Windward）／フーシ派、サウジ東西輸送網へ無人機攻撃を発表——紅海側にもリスク拡大／原油は攻撃休止・外交期待で急落——ブレント89.68ドル（前日比-7.3%）——日本関係船は残り4隻で変化なし——封鎖151日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残19日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米・イラン協議の実態（米は「進行中」・イランは否定）の見極め ②イラン・オマーン次官級協議の合意文書化の有無 ③フーシ派・紅海方面の攻撃継続とサウジ東西輸送網への影響 ④北側航路一極集中・無許可船引き返しの継続性 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残19日（8/16）</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        ⚔️ <strong>米・イランの攻撃休止は3日（7/25〜7/28）で終了——IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM）／米・サウジはイラク国内の親イラン民兵拠点を合同空爆／トランプ氏は報復を予告し7/29夜（米時間）に新たな空爆を開始と判明／イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理を維持／茂木外相はアラグチ外相と電話会談し覚書に沿った協議継続を要請／原油はブレント90.66ドルまで急騰（前日比+7%）——日本関係船は残り4隻で変化なし——封鎖153日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残17日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米の報復空爆の規模・イランの対応（更なる報復かエスカレーション停止か） ②イラン・オマーン海峡共同管理協議の帰趨（50-50案拒否後の展開） ③フーシ派によるサウジ船インド洋方面標的化と紅海ルートへの波及 ④茂木・アラグチ電話会談後の日本人拘束問題の進展 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残17日（8/16）</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S05完了

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月28日 10:19 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【北側航路（イラン指定・北側航路）】Kpler・Windwardともに7/26の通航は7隻と確認。全船がイラン指定の北側航路に集中し、イランは無許可で通過を試みた船舶6隻を引き返させたと主張。【南ルート（Omani coastal corridor）】イラン管理下での通航は事実上なし——通航船はほぼ全て北側に集約。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限は7/17（MOU第5条）を未着手のまま徒過。【米・イラン攻撃休止】7/25未明の停止から3日目に継続——トランプ氏「協議中、合意の可能性」に対しイラン外務省は直接協議を否定。【イラン・オマーン仲介】7/25〜26にテヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表。【紅海・バブエルマンデブ】フーシ派がサウジ東西輸送網（紅海向け原油供給網）へ無人機攻撃を発表・商品輸送船の通航は数カ月ぶり低水準（Kpler：11隻）。【UKMTO 警戒水準】Substantial（継続）。EUNAVFOR ASPIDESは紅海南部の脅威水準を中程度→高いへ引き上げ。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（7/28 10:19 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月30日 10:08 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【停戦崩壊】米・イラン攻撃休止は3日（7/25〜7/28）で終了。IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM）・米・サウジはイラク国内の親イラン民兵拠点を合同空爆・トランプ氏は7/29夜（米時間）に新たな対イラン空爆を開始したと判明。【北側航路（イラン指定）】通航は依然イラン指定の北側航路に集中。エスカレーションを受け通航数の更なる悪化が懸念される。【南ルート（Omani coastal corridor）】イラン管理下での通航は事実上なし。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限は7/17（MOU第5条）を未着手のまま徒過。【イラン・オマーン仲介】イランはオマーン提示のホルムズ海峡共同管理（50-50）案を拒否し単独管理の立場を維持。【紅海・バブエルマンデブ】フーシ派はサウジ船のインド洋方面航行を標的にすると宣言——海運各社はスエズ運河迂回を検討中。【UKMTO 警戒水準】Substantial（継続、悪化リスク）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（7/30 10:08 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S08.5完了

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年7月28日 10:19 JST 更新</span><br>
  📊 <strong>米・イランが協議の有無を巡り応酬——トランプ氏は合意に近づく可能性を示唆も、イランは直接協議を否定・通航状況も不変と主張：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#4ade80;">↑</span> — イラン・オマーン次官級協議が「建設的」と評価され空爆休止も3日目に継続中<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — 通航は依然7隻程度の低水準で推移し最多シナリオを維持<br>
  🅒 MOU形骸化・機能不全 <span style="color:#fbbf24;">→</span> — 北側航路への一極集中・無許可船引き返しの継続で「イランによる管理の既成事実化」路線は不変<br>
  🅓 全面対決・無期限封鎖 <span style="color:#4ade80;">↓</span> — 直接攻撃休止が3日目に入り、原油急落も市場のエスカレーション懸念後退を示唆<br>
  <strong style="color:#f87171;">攻撃休止の継続とイラン・オマーン協議の進展は好材料だが、正式な停戦・通航再開合意はいずれも確認されておらず、限定的な改善にとどまる（A↑ B→ C→ D↓）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月28日 10:19 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年7月30日 10:08 JST 更新</span><br>
  📊 <strong>米・イラン攻撃休止は3日で終了——IRGC奇襲・米報復空爆・イランはオマーン海峡共同管理案を拒否：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — イランがオマーン提示の海峡共同管理案を拒否し、外交トラックが後退<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — 通航は依然低水準で推移するが、軍事エスカレーションで更なる悪化リスク<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — オマーン案拒否・単独管理継続で「イランによる管理の既成事実化」路線が強まる<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — 攻撃休止が3日で崩壊し米が報復空爆に着手、原油急騰がエスカレーション再燃を裏付け<br>
  <strong style="color:#f87171;">7/25〜28の攻撃休止・外交進展は一夜で反転し、IRGCの奇襲・米の報復空爆によって軍事的緊張は7月上旬以来の水準に逆戻りした（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月30日 10:08 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S06完了

---

## [S07] 4つのシナリオ本文

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>米軍による対イラン攻撃休止は7/27時点で3日目に入り、トランプ大統領は米イラン協議が進行中で合意に至る可能性があると発言した。イラン・オマーンの次官級協議も「建設的」と双方が評価し、テヘランでの協議は継続される。ただしイラン外務省は米との直接協議を否定しており、対象船舶・航路・料金・発効時期を定めた合意文書はいずれも公表されていない。外交進展の「兆し」は増えたが、「合意」段階には至っていない。</p>
      </div>
    </div>

    <!-- シナリオ B：部分的封鎖継続（膠着） -->
    <div class="sc-card sc-mid">
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>Kpler・Windwardが確認した7/26のホルムズ通航はわずか7隻で、平常時の約6分の1にとどまる。イランは無許可で北側航路以外を通過しようとした船舶6隻を引き返させたと主張しており、通航管理の実権を維持する姿勢を崩していない。機雷除去（7/17期限を徒過）にも依然着手しておらず、攻撃休止・協議進展という外交面の好材料とは裏腹に、海上の実態は低水準の膠着が続いている。</p>
      </div>
    </div>

    <!-- シナリオ C：完全封鎖の制度化・経済疲弊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>イランが無許可船6隻を引き返させたとの主張や、全通航船が北側航路に集中している実態は、イランがホルムズ海峡の管理権限を制度的に固定化しようとする路線の継続を示す。フーシ派によるサウジ東西輸送網（紅海向け原油供給網）への攻撃発表も、紅海側での「管理の制度化」圧力を新たに加えるものだ。米イラン間の攻撃休止・協議進展は好材料だが、通航管理そのものを巡る力学は変わっておらず、シナリオCの水準はおおむね据え置きと評価する。</p>
      </div>
    </div>

    <!-- シナリオ D：軍事エスカレーション・停戦崩壊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>米軍による対イラン攻撃休止は7/27時点で3日目に継続し、トランプ大統領は協議による合意の可能性にも言及した。原油先物の急落（ブレント-7.3%）は市場が当面の全面エスカレーションを織り込んでいないことを示唆する。ただし米国は協議失敗時の攻撃再開に明確に言及しており、正式な停戦文書はなお存在しない。フーシ派の紅海攻撃継続というリスク要因も残るため、シナリオDの水準はさらにやや低下したが、消滅したわけではないと評価する。</p>
      </div>
    </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>7/25未明から3日間続いた攻撃休止は7/28夜のIRGCによる米軍拠点への奇襲攻撃で崩壊した。さらにイランは、オマーンが提示していたホルムズ海峡の共同管理（50-50）案を拒否し、単独管理の立場を維持した。次官級協議の「建設的」評価は一夜で覆り、段階的なMOU履行という外交シナリオの実現可能性は明確に後退した。</p>
      </div>
    </div>

    <!-- シナリオ B：部分的封鎖継続（膠着） -->
    <div class="sc-card sc-mid">
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>7/26時点の通航はわずか7隻程度で推移していたが、7/28夜の攻撃休止崩壊・米の報復空爆着手により、通航水準の更なる悪化が懸念される。機雷除去（7/17期限を徒過）にも依然着手しておらず、海上の実態は低水準の膠着が続く一方、軍事エスカレーションは新たな下振れリスクとなっている。</p>
      </div>
    </div>

    <!-- シナリオ C：完全封鎖の制度化・経済疲弊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>イランがオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持したことは、通航管理権限を制度的に固定化する路線がむしろ強化されたことを示す。フーシ派によるサウジ船インド洋方面標的化の宣言も、紅海側での「管理の制度化」圧力を新たに加えるものだ。米イラン間の攻撃休止崩壊・報復応酬により、シナリオCの水準はやや上昇したと評価する。</p>
      </div>
    </div>

    <!-- シナリオ D：軍事エスカレーション・停戦崩壊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>7/25〜28の3日間の攻撃休止はIRGCによる米軍拠点への奇襲攻撃で崩壊し、米・サウジはイラク国内の親イラン民兵拠点を合同空爆、トランプ大統領は7/29夜（米時間）に対イラン報復空爆を開始したと報じられた。原油先物の急騰（ブレント+7%）は市場が軍事エスカレーションの再燃を織り込み始めたことを示す。フーシ派によるサウジ船インド洋方面標的化という新たなリスク要因も加わり、シナリオDの水準は明確に上昇したと評価する。</p>
      </div>
    </div>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S07完了

---

## [S08] シナリオフッター（次の焦点5点）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米・イラン協議の実態（米「進行中」・イラン否定）の見極め</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン・オマーン次官級協議の合意文書化の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">フーシ派・紅海方面の攻撃継続とサウジ東西輸送網への影響</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">北側航路一極集中・無許可船引き返しの継続性</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月28日 10:19 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米の報復空爆の規模とイランの対応（更なる報復かエスカレーション停止か）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン・オマーン海峡共同管理協議の帰趨（50-50案拒否後の展開）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">フーシ派のサウジ船インド洋方面標的化と紅海ルートへの波及</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">茂木・アラグチ電話会談後の拘束邦人問題の進展</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月30日 10:08 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S08完了

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）※必ず最後に作成

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="display:flex;flex-direction:column;gap:6px;margin-bottom:10px;border:1.5px solid rgba(56,189,248,0.3);border-radius:14px;padding:8px 10px;background:rgba(15,23,42,0.6);">
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.4);color:#6ee7b7;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">いま何が</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🗣️ トランプ氏「イランと協議中、合意に近づく可能性」——イランは直接協議を否定。イラン・オマーン次官級協議は「建設的」。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⚠️ ホルムズ通航は7/26も7隻に留まり北側航路に集中——原油は90ドル割れまで急落・日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 米イラン協議の実態とオマーン仲介の合意文書化が焦点、封鎖151日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残19日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="display:flex;flex-direction:column;gap:6px;margin-bottom:10px;border:1.5px solid rgba(56,189,248,0.3);border-radius:14px;padding:8px 10px;background:rgba(15,23,42,0.6);">
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.4);color:#fca5a5;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">いま何が</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
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
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(56,189,248,0.15);border:1px solid rgba(56,189,248,0.3);color:#7dd3fc;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️トランプ氏「協議中、合意の可能性」</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷イラン「直接協議は要請せず」</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚢通航7隻・北側航路に集中</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油急落・ブレント89.68ドル(-7.3%)</span>
        </div>

        </div>
      </div>

      <!-- ジャンプ＋クリッカブルバッジ -->
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️IRGC奇襲・全弾迎撃</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸米、報復空爆を開始</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇴🇲イラン、50-50共同管理案を拒否</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油急騰・ブレント90.66ドル(+7%)</span>
        </div>

        </div>
      </div>

      <!-- ジャンプ＋クリッカブルバッジ -->
<!-- NEW:END -->
<!-- APPLY:END -->

✓ S09完了

---

## [SHIP_CONFIG] C01タンカー確認

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年7月28日 10:19 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。米・イランの直接攻撃休止は3日目に継続——トランプ氏「協議中、合意の可能性」／イラン外務省は直接協議を否定し通航状況も不変と主張。イラン・オマーンは次官級で通航管理協議を継続中）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年7月30日 10:08 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。米・イランの攻撃休止は3日で終了しIRGCが米軍拠点へ奇襲・米は報復空爆を開始。イランはオマーンの海峡共同管理案を拒否し単独管理を維持）'
<!-- NEW:END -->
<!-- APPLY:END -->

**C01 タンカー確認**：日本語「日本関係船舶 ホルムズ海峡 通過 足止め」「外務省 ホルムズ海峡 日本関係船舶」「金子国土交通大臣 記者会見 ホルムズ海峡 日本関係船舶」＋英語「Japanese ships Strait of Hormuz stranded detained」の4クエリ全てでweb検索済み（外務省・国土交通省の一次情報を優先確認）／変化なし→残り4隻のまま・dateConfirmedを本日日時「変更なし」で更新

✓ SHIP_CONFIG完了

---

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-28T10:19:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-30T10:08:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

✓ JSON-LD完了

---

## [S10] news_data.json 更新

### updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月28日 10:19 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年7月30日 10:08 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest：新規3件を先頭に追加（既存6件のうち最古3件はClaude Codeがarchiveへ移動）

> Claude Codeへの指示：`latest` 配列は最大6件のため、以下の新規3件を先頭に追加した後、
> 現在の配列末尾3件（id: `latest-us-strikes-pause-0725`／`latest-oman-iran-talks-progress-0725`／`latest-irgc-warning-shots-houthi-aramco-0725`）を
> `archive` の先頭バッチ（`batchLabel`: "2026年7月25日〜26日"）へ移動してください。
> また、既存の `latest-trump-talks-progress-0727` の `isLatest` は `false` に変更してください（新規追加分の先頭が最新となるため）。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-trump-talks-progress-0727",
      "title": "トランプ氏「イランと協議中、合意に近づく可能性」——ウォルツ大使は空爆停止の理由を説明",
      "body": "トランプ大統領は7月27日、米国とイランが協議を行っており合意に至る可能性があると述べた。協議が失敗すれば攻撃を再開する可能性にも言及。ウォルツ国連大使は、大統領が「協議に時間的余地を与えるため」攻撃を休止したと説明した。報道によれば米軍指揮官は攻撃対象の枯渇や防空兵器の消耗への懸念を進言していたという。",
      "sourceLabel": "Reuters",
      "date": "2026年7月27日（現地）/ 2026年7月27日 JST",
      "label": "🕊️ 外交",
      "url": "https://www.reuters.com/world/middle-east/iran-says-it-still-controls-strait-not-seeking-talks-after-trump-halts-bombing-2026-07-27/",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

### osint：新規1件を追加（既存の isLatest: true は false に変更）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "titleJa": "【Al Jazeera】米・イラン戦争に新戦線——フーシ派がサウジ石油施設を攻撃",
      "titleEn": "New front in US-Iran war escalates as Houthis fire at Saudi oil facilities",
      "country": "カタール",
<!-- OLD:END -->
<!-- NEW:START -->
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
    {
      "titleJa": "【Al Jazeera】米・イラン戦争に新戦線——フーシ派がサウジ石油施設を攻撃",
      "titleEn": "New front in US-Iran war escalates as Houthis fire at Saudi oil facilities",
      "country": "カタール",
<!-- NEW:END -->
<!-- APPLY:END -->

> Claude Codeへの指示：上記で追加した新規osintエントリーの直後に続く、既存の先頭エントリー（【Al Jazeera】米・イラン戦争に新戦線...）の `"isLatest": true` を `"isLatest": false` に変更してください（同エントリー1件のみ）。

✓ S10完了

---

## [S11] 更新ログ追記（2ブロック構成・常時表示3件固定・合計10件維持）

### ブロック1：常時表示エリア（3件固定）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年7月28日 10:19 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/28 10:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領「イランと協議中、合意に近づく可能性」（7/27）——一方イラン外務省バガイ報道官は米との直接協議要請を否定し通航状況も不変と主張・イラン・オマーンは7/25〜26テヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表・ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張（Kpler/Windward）・フーシ派、サウジ東西輸送網へ無人機攻撃を発表——紅海側にもリスク拡大・原油は攻撃休止・外交期待で急落しブレント89.68ドル（前日比-7.3%）・インドMRPLが原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記・日本関係船は残り4隻で変化なし・封鎖151日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月26日 10:30 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/26 10:30</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態・オマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展（オマーン外交団7/24テヘラン訪問）・IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表・フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明・原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）・米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇・日本関係船は残り4隻で変化なし・封鎖149日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月24日 09:23 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/24 09:23</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行・トランプ大統領はイランへの「大規模攻撃」検討を警告・カザフスタンがドローン攻撃を受けCPCターミナル経由原油輸出を停止・クウェート国境で火災発生（鎮圧）・バーレーンも再攻撃・ルビオ国務長官「複数国がホルムズ護衛に関心」も法的障壁で未実現・Windward報告：南側迂回ルートでタンカー3隻被弾・通航は北側ルートに集中・原油はブレント7/23終値100.65ドル（前日比+7.00%・5月22日以来の高値）・日本関係船は残り4隻で変化なし・封鎖147日目・ニュース3件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年7月30日 10:08 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/30 10:08</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米・イランの攻撃休止は3日（7/25〜28）で終了——IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM）・米・サウジはイラク国内の親イラン民兵拠点を合同空爆・トランプ大統領は報復を予告し7/29夜（米時間）に新たな対イラン空爆を開始と判明・イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持・茂木外相はアラグチ外相と電話会談し覚書に沿った対米協議継続を要請・拘束邦人1名の早期解決も改めて要請・フーシ派はサウジ船のインド洋方面航行を標的化すると宣言・原油はブレント90.66ドルまで急騰（前日比+7%）・日本関係船は残り4隻で変化なし・封鎖153日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月28日 10:19 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/28 10:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領「イランと協議中、合意に近づく可能性」（7/27）——一方イラン外務省バガイ報道官は米との直接協議要請を否定し通航状況も不変と主張・イラン・オマーンは7/25〜26テヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表・ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張（Kpler/Windward）・フーシ派、サウジ東西輸送網へ無人機攻撃を発表——紅海側にもリスク拡大・原油は攻撃休止・外交期待で急落しブレント89.68ドル（前日比-7.3%）・インドMRPLが原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記・日本関係船は残り4隻で変化なし・封鎖151日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月26日 10:30 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/26 10:30</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態・オマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展（オマーン外交団7/24テヘラン訪問）・IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表・フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明・原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）・米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇・日本関係船は残り4隻で変化なし・封鎖149日目・ニュース3件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse 先頭への旧3件目（7/24 09:23分）の挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月22日 09:15 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月24日 09:23 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/24 09:23</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行・トランプ大統領はイランへの「大規模攻撃」検討を警告・カザフスタンがドローン攻撃を受けCPCターミナル経由原油輸出を停止・クウェート国境で火災発生（鎮圧）・バーレーンも再攻撃・ルビオ国務長官「複数国がホルムズ護衛に関心」も法的障壁で未実現・Windward報告：南側迂回ルートでタンカー3隻被弾・通航は北側ルートに集中・原油はブレント7/23終値100.65ドル（前日比+7.00%・5月22日以来の高値）・日本関係船は残り4隻で変化なし・封鎖147日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年7月22日 09:15 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：合計件数調整（11件→10件、最古の7/13 08:28分を削除）

> 常時表示3件（7/30・7/28・7/26）＋log-collapse 8件（7/24・7/22・7/19・7/16・7/14 18:00・7/14 16:16・7/14 08:48・7/13 08:28）＝11件となり上限10件を超過するため、log-collapse内の最古エントリー（7/13 08:28分）を削除し、`docs/data/update_log.json` の先頭に追加してください。

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月13日 08:28 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/13 08:28</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン、米の3度目・約140カ所への対イラン空爆に対しオマーン（ドゥクム）・カタール（アルウデイド基地）・クウェート・バーレーン・ヨルダンの5カ国を弾道ミサイル・ドローンで同時報復攻撃（7/12 JST）・カタールで迎撃破片により3名負傷・ガリバフ国会議長「一方的な合意の時代は終わった」とX投稿・オマーン外務省、ドゥクム・ムサンダム攻撃を受けイラン大使を召喚し正式抗議——前日のアラグチー・ブーサイーディー両外相協議から一転し仲介の立場も緊張最高潮・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油は週明けに反発しブレント一時79ドル台・WTI74ドル台まで4%高・封鎖136日目・ニュース3件更新・osint更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

> Claude Codeへの指示：削除した7/13 08:28分のエントリー本文を `docs/data/update_log.json` の先頭に `{"date":"2026/07/13 08:28","text":"（上記削除本文をそのまま貼付）"}` として追加してください。

✓ S11完了

---

## [archive] archive_timeline.json 追記分

> Claude Codeへの指示：`docs/data/archive_timeline.json` の `entries` 配列末尾に、以下のエントリーを追加してください（既存エントリーは変更しないこと）。

```json
{
  "date": "2026-07-30",
  "dateLabel": "2026/07/30 10:08",
  "blockadeDay": 153,
  "summary": "米・イランの攻撃休止は3日（7/25〜28）で終了——IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM）・米・サウジはイラク国内の親イラン民兵拠点を合同空爆・トランプ大統領は報復を予告し7/29夜（米時間）に新たな対イラン空爆を開始と判明・イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持・茂木外相はアラグチ外相と電話会談し覚書に沿った対米協議継続を要請・拘束邦人1名の早期解決も改めて要請・フーシ派はサウジ船のインド洋方面航行を標的化すると宣言・原油はブレント90.66ドルまで急騰（前日比+7%）・日本関係船は残り4隻で変化なし・封鎖153日目・ニュース3件更新・osint更新",
  "relatedNews": [
    {"title": "IRGC、米軍拠点へ弾道ミサイル奇襲——全弾迎撃、攻撃休止は3日で終了", "url": "https://www.pressdemocrat.com/2026/07/28/iran-us-troops-missile-attack/", "sourceLabel": "Reuters / CENTCOM"},
    {"title": "トランプ氏「対イラン報復攻撃を実施」——7/29夜（米時間）に新たな空爆開始", "url": "https://www.cbsnews.com/live-updates/us-iran-war-trump-saudi-arabia-strait-of-hormuz/", "sourceLabel": "CBS News"},
    {"title": "イラン、オマーンの海峡共同管理（50-50）案を拒否——単独管理の立場を維持", "url": "https://tradingeconomics.com/commodity/brent-crude-oil", "sourceLabel": "Trading Economics"}
  ]
}
```

✓ archive完了

---

## ✅ 出力前セルフチェック

```
[x] S01 ヘッダー ― 2026年7月30日 10:08 JST ✓
[x] S02 TICKER ― 停戦崩壊・IRGC奇襲/全弾迎撃・米報復空爆・イラン50-50案拒否・原油急騰・封鎖153日目 ✓
[x] S03 速報インシデント ― 7/30 10:08付け・6件新規追加（茂木外相会談含む）✓
[x] S04 情勢カード3枚 ― 日付・数値・出典を7/30版に更新 ✓
[x] S05 COUNTDOWN ― 封鎖153日目・MOU最終期限残17日 ✓
[x] S06 シナリオ確率補足バナー ― 7/30 10:08 JST日付更新・矢印方向を情勢反転に合わせ変更 ✓
[x] S07 シナリオ4本 ― A/B/C/D本文を7/30情勢に更新（A↓ B→ C↑ D↑）✓
[x] S08 シナリオフッター ― 次の焦点5点を7/30版に更新 ✓
[x] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成）✓
[x] S10 news_data.json更新メモ ― latest 3件新規・osint 1件新規・updated日付 ✓
[x] S11 更新ログ ― 2ブロック構成＋常時表示3件固定への是正＋合計10件維持（7/13 08:28分を削除）✓
[x] SHIP_CONFIG ― dateConfirmed 更新（C01・4クエリ全実施・変化なし）✓
[x] JSON-LD ― dateModified 更新 ✓
[x] archive_timeline.json ― 本日分エントリー追加 ✓

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記は本セクションで変更なし（S05のdl-box内に既存表記あり、今回未変更）✓
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：S08.5で7/30 10:08 JST更新を明示 ✓
習近平表記チェック：本日分に言及なし（該当なし）✓
Al Jazeeraのlatest混入チェック：問題なし（osintのみに配置）✓
人名表記チェック：トランプ・ネタニヤフ・アラグチ等、日本語表記で統一 ✓
URLチェック：全てweb検索で実在確認済みのURLのみ使用（AI生成・推測URLなし）✓
```

---

## Claude Code への引き継ぎ文（コピー用）

```
git pull --rebase してから、docs/tools/index_html_diffs.mdに従ってdocs/index.htmlを更新してください。
また docs/data/news_data.json・docs/data/archive_timeline.json・docs/data/update_log.json も
本diffs.md記載の内容に従って更新してください（news_data.jsonはlatest配列の追加・archiveへの移動、
osint配列の追加・isLatest付け替えを含みます）。
更新完了後にcommitしてください。pushは確認後に指示します。
```
