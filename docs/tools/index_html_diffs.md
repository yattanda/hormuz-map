# index_html_diffs.md — 2026年7月28日 10:19 JST 更新分

> Claude Code への指示：以下の差分を index.html / docs/data/news_data.json に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## ⚠️ 本日のセルフチェック事前貼付（手順1：空欄先貼り）

```
本日のセルフチェック項目数：14件
[ ] S01 ヘッダー ― 2026年7月28日 10:19 JST
[ ] S02 TICKER ― 米イラン協議応酬・イランオマーン次官級協議・通航7隻・原油急落・MRPL航路除外・封鎖151日目
[ ] S03 速報インシデント ― 7/28 10:19付け・6件新規追加
[ ] S04 情勢カード3枚 ― 日付・数値・出典を7/28版に更新
[ ] S05 COUNTDOWN ― 封鎖151日目・MOU最終期限残19日
[ ] S06 シナリオ確率補足バナー ― 7/28 10:19 JST日付更新（前回7/24付けのまま放置されていたため今回復旧）
[ ] S07 シナリオ4本 ― A/B/C/D本文を7/28情勢に更新
[ ] S08 シナリオフッター ― 次の焦点5点を7/28版に更新
[ ] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成）
[ ] S10 news_data.json更新メモ ― latest 3件新規・osint 1件新規・updated日付
[ ] S11 更新ログ ― 2ブロック構成＋常時表示4→3件への是正＋合計10件維持
[ ] SHIP_CONFIG ― dateConfirmed 更新（C01・変化なし）
[ ] JSON-LD ― dateModified 更新
[ ] archive_timeline.json ― 本日分エントリー追加
```

全項目 ✓確認済（詳細は各セクション末尾のチェック参照）。未実施(✗)項目なし。

---

## [Step 0] 直前状態の確認結果

- project_knowledge_search により、直前の diffs.md は「2026年5月3日」時点のものであることを確認（push漏れのため古い状態）。
- 一方、live index.html（raw fetch）および project_knowledge 内 SHIP_CONFIG/JSON-LD 記載から、実際の最新状態は **2026年7月26日 10:30 JST**（封鎖149日目）であることを確認。
- ルール「Step AとStep Bの日時が食い違う場合はStep B（更新ログ）を正とする」に基づき、**live index.html を正**として old_str を全て抽出した（curlで直接取得・完全一致を確認済み）。
- なお、シナリオ確率補足バナー（S06）のみ 7/24 09:23 JST のまま7/26更新時に取り残されていたことを確認。今回のdiffsで是正する。
- 常時表示ログ（S11）も本来「3件固定」のところ実態は4件（7/26・7/24・7/22・7/19）になっており、7/19が折り畳み側とも重複していた。今回のdiffsで3件へ是正し、重複を解消する。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米軍が13夜ぶりに対イラン空爆を停止——一時的な小康状態／オマーン・イラン、ホルムズ海峡再開・領海管理を巡る協議で進展／IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表／フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明／原油はブレント7/24終値98.38ドルまで反落も週間+10%超維持／封鎖149日目）</span>
    <span class="badge-item badge-date">📅2026年7月26日 10:30 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（トランプ氏「イランと協議中、合意に近づく可能性」も、イラン外務省は米との直接協議要請を否定・通航状況も不変と主張／イラン・オマーンは次官級協議「建設的」——通航管理の共通原則を協議も合意文書は非公表／ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張／原油は攻撃休止・外交期待で急落——ブレント89.68ドル（前日比-7.3%）／封鎖151日目）</span>
    <span class="badge-item badge-date">📅2026年7月28日 10:19 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月26日 10:30 JST） -->
      🕊️【米、13夜ぶり空爆停止】対イラン空爆が7/25未明、開戦後初めて途絶——一時的な小康状態（7/25 JST）｜🇴🇲 オマーン・イラン、ホルムズ海峡再開・両国領海管理を巡る協議で進展——オマーン外交団が7/24テヘラン訪問（CBS/IRNA、7/25）｜⚠️ IRGC、南側迂回ルートの不正通航船4隻に警告射撃——進路変更させたと発表（7/25）｜⚓ フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明（7/25）｜🛢️ 原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%）——週間では依然+10%超（7/24〜25 JST）｜⛽ 米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇（7/25）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残21日｜📋 7/26 10:30 JST確認済——軍事面は小康状態も外交・海上情勢は流動的｜封鎖149日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月28日 10:19 JST） -->
      🕊️【米・イラン、協議巡り応酬】トランプ氏「イランと協議中、合意に近づく可能性」——ウォルツ大使「協議に時間的余地を与えるため」空爆停止と説明（7/27 JST）｜🇮🇷 イラン外務省バガイ報道官「米との協議再開要請せず」——通航状況にも変更なしと表明（7/27）｜🇴🇲 イラン・オマーン次官級協議「建設的」——沿岸国主権尊重の共通原則・通航管理メカニズムを協議も合意文書は非公表（IRNA/Muscat Daily、7/26）｜🚢 ホルムズ通航、7/26も7隻に留まる——全船がイラン指定北側航路に集中・無許可船6隻は引き返しとイラン主張（Kpler/Windward、7/27）｜🛢️ 原油は攻撃休止・外交期待で急落——ブレント7/27夜89.68ドル（前日比-7.3%）・WTI83.18ドル（7/28 JST）｜📦 インドMRPL、原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記（Reuters、7/27）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残19日｜封鎖151日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

### トグルボタン（見出し＋日付バッジ）

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:1.1rem;">🚨</span>
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米、13夜ぶり空爆停止／オマーン・イラン、ホルムズ再開協議で進展／フーシ派サウジアラムコ拠点攻撃</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/26 10:30 更新</span>
    </span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:1.1rem;">🚨</span>
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米・イラン、協議の有無巡り応酬／イラン・オマーン次官級協議「建設的」／通航は7隻に留まり原油急落</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/28 10:19 更新</span>
    </span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/26 10:30 速報】米軍による対イラン空爆が7/25未明（現地時間）、13夜連続の後初めて途絶——イラン保健省報道官は「平穏な夜だった」とX投稿、CENTCOMは即時コメントなし｜オマーンとイランは、ホルムズ海峡再開と両国領海の管理を巡る協議で進展があったと地域筋2名がCBS Newsに証言（7/25）——オマーン外交団は7/24にテヘランを訪問し「船舶交通を管理する適切なメカニズム」を協議したとイラン国営IRNAが伝達｜イラン革命防衛隊（IRGC）は、南側（オマーン沿岸）迂回ルートを通じ不正・危険な経路での通航を試みた船舶4隻に対し、直近24時間で警告射撃を実施し進路変更させたと発表｜フーシ派は、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明（7/25）——紅海方面での攻撃継続姿勢を改めて示す｜原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%）も週間では依然+10%超｜米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇｜日本関係船は残り4隻で変化なし｜封鎖149日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/28 10:19 速報】トランプ大統領は7/27、米国とイランが協議を行っており合意に至る可能性があると発言——ウォルツ国連大使は「協議に時間的余地を与えるため」攻撃を休止したと説明｜イラン外務省バガイ報道官は、イランが米国との協議再開を要請したとの報道を否定し、ホルムズ海峡の通航状況にも変更はないと表明（7/27）｜イランとオマーンは7/25〜26にテヘランで次官級協議を実施し、沿岸2国の主権的権利を尊重しつつ安全な通航を管理する共通原則・運用メカニズムについて意見交換——合意文書は公表されていない（IRNA/Muscat Daily）｜Kpler・Windwardともに、7/26のホルムズ海峡通航は7隻にとどまったと確認——全船がイラン指定の北側航路を利用し、イランは無許可で通過を試みた船舶6隻を引き返させたと主張｜フーシ派はサウジ東西輸送網（紅海向け原油供給網）への無人機攻撃を発表・サウジ国防省はイラク領内から飛来した無人機を迎撃したと発表（7/27）｜原油は攻撃休止・外交進展期待を受け急落——ブレントは7/27夜時点で89.68ドル（前日比-7.3%）、WTIは83.18ドル（同-6.9%）｜インド国営MRPLは原油スポット入札で紅海・ホルムズ海峡経由の積み出しを避けるよう明記——同種条項の明記は同国精製会社で初とロイターが報道｜日本関係船は残り4隻で変化なし｜封鎖151日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に6件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🕊️ 7/25 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🕊️ 7/27 JST</span>
  <span style="color:#e2e8f0;"> トランプ大統領は、米国とイランが協議を行っており合意に至る可能性があると発言。協議が失敗すれば攻撃を再開する可能性にも言及した。ウォルツ国連大使は、大統領が「協議に時間的余地を与えるため」攻撃を休止したと説明。報道によれば、米軍指揮官は攻撃対象の枯渇や防空兵器の消耗への懸念を進言していたという。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇮🇷 7/27 JST</span>
  <span style="color:#e2e8f0;"> イラン外務省のバガイ報道官は、イランが米国との協議再開を要請したとの報道を否定。ホルムズ海峡の通航状況にも変更はないと説明した。イラン側が確認しているのはオマーンとの協議のみとしている。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🇴🇲 7/26 JST</span>
  <span style="color:#e2e8f0;"> イランとオマーンは7/25〜26、テヘランで次官級協議を実施し、沿岸2国の主権的権利を尊重しつつホルムズ海峡の安全な通航を管理する共通原則・運用メカニズムについて意見交換。オマーン代表団は26日午後に帰国し、協議は継続される。合意文書は公表されていない。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🚢 7/27 JST</span>
  <span style="color:#e2e8f0;"> Kpler・Windward双方の集計で、7/26のホルムズ海峡通航は7隻にとどまったことが判明。全船がイラン側に近い北側航路を利用し、イランは無許可で通過を試みた船舶6隻を引き返させたと主張。平常時（1日約45隻）の約6分の1の水準が続く。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚓ 7/26〜27 JST</span>
  <span style="color:#e2e8f0;"> フーシ派は、サウジアラビア東部から紅海沿岸ヤンブーへ原油を輸送する東西輸送網への無人機攻撃を発表。サウジ国防省は同日、イラク領内から飛来した無人機を迎撃・破壊したと発表した。施設損傷や輸出減少の独立した確認は現時点でない。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🛢️ 7/27〜28 JST</span>
  <span style="color:#e2e8f0;"> 原油先物は攻撃休止・外交進展期待を受け急落。ブレントは7/27夜時点で89.68ドル（前日比-7.3%）、WTIは83.18ドル（同-6.9%）。RBCキャピタル・マーケッツのクロフト氏は「戦闘の休止は双方向の船舶通航再開を意味しない」と指摘。インド国営MRPLは原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🕊️ 7/25 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sit-card danger">
    <div class="s-icon">🕊️</div>
        <div class="s-title">🕊️ 外交：米が13夜ぶりに空爆停止——オマーン・イラン、ホルムズ再開協議で進展</div>
        <div class="s-body">米軍による対イランへの空爆は、7/25未明（現地時間）に13夜連続の後、開戦後初めて途絶した。並行して、オマーンとイランの間でホルムズ海峡再開と両国領海の管理を巡る協議に進展があったと地域筋2名がCBS Newsに証言。オマーン外交団は7/24にテヘランを訪問し「船舶交通を管理する適切なメカニズム」を協議したとイラン国営IRNAが伝達した。ただし、これが恒久的な沈静化を意味するかは不透明で、10日間停戦案やトランプ大統領の「大規模攻撃」検討はいずれも撤回されていない。</div>
        <div class="s-src">出典: Washington Post / CBS News / IRNA（7/25 JST 更新）</div>
  </div>

  <!-- カード② 軍事情勢 -->
  <div class="sit-card warning">
    <div class="s-icon">⚔️</div>
        <div class="s-title">⚠️ 軍事：IRGCが南側迂回ルートの不正通航船4隻に警告射撃／フーシ派はサウジアラムコ拠点を攻撃と表明</div>
        <div class="s-body">米軍の対イラン空爆は7/25未明に13夜ぶりで途絶した一方、イラン革命防衛隊（IRGC）は、南側（オマーン沿岸）迂回ルートを通じ不正・危険な経路での通航を試みた船舶4隻に対し、直近24時間で警告射撃を実施し進路変更させたと発表——イランは南ルート通航船にも自国の許可・通航料を求める姿勢を強めている。イエメンの親イラン武装組織フーシ派は、サウジアラムコのジザン・ヤンブー両拠点への攻撃を表明し、紅海方面での攻撃継続姿勢を改めて示した。</div>
        <div class="s-src">出典: CBS News（IRGC・イラン国営テレビ引用）（7/25 JST 更新）</div>
  </div>

  <!-- カード③ エネルギー・市場 -->
  <div class="sit-card info">
    <div class="s-icon">🛢️</div>
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/26再確認）——原油はブレント98ドル台へ反落／ガソリンは上昇継続</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/26 10:30 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。原油はブレント先物が7/23終値100.65ドルから7/24終値98.38ドル（前日比-2.29%）まで反落したが、週間では依然+10%超の水準を維持。カザフスタンCPCターミナルの原油輸出停止は新規情報なく継続中とみられる。一方、米国内ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇（開戦来+38%）。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残21日に迫っている。</div>
        <div class="s-src">出典: Trading Economics / CNN（7/25 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 13「米、13夜ぶりに空爆停止——オマーン・イラン仲介進展も、フーシ派は紅海攻撃継続」——封鎖149日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 14「米・イラン、協議の有無を巡り応酬——イランは直接協議否定も次官級のオマーン仲介は継続」——封鎖151日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🕊️ <strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態／オマーン・イラン、ホルムズ海峡再開・領海管理協議で進展（オマーン外交団7/24テヘラン訪問）／IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更／フーシ派、サウジアラムコのジザン・ヤンブー拠点攻撃を表明——原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）——日本関係船は残り4隻で変化なし——封鎖149日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残21日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米の空爆停止が一時的か継続的かの見極め ②オマーン・イラン仲介協議の進捗と正式合意の可否 ③フーシ派・紅海方面の攻撃継続とバブエルマンデブ海峡への影響 ④IRGCによる南ルート取り締まり強化の航行への影響 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残21日（8/16）</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🕊️ <strong>トランプ大統領「イランと協議中、合意に近づく可能性」（7/27）——一方イラン外務省は米との直接協議要請を否定し通航状況も不変と主張／イラン・オマーンは7/25〜26テヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表／ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張（Kpler/Windward）／フーシ派、サウジ東西輸送網へ無人機攻撃を発表——紅海側にもリスク拡大／原油は攻撃休止・外交期待で急落——ブレント89.68ドル（前日比-7.3%）——日本関係船は残り4隻で変化なし——封鎖151日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残19日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米・イラン協議の実態（米は「進行中」・イランは否定）の見極め ②イラン・オマーン次官級協議の合意文書化の有無 ③フーシ派・紅海方面の攻撃継続とサウジ東西輸送網への影響 ④北側航路一極集中・無許可船引き返しの継続性 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残19日（8/16）</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー（7/24付けのまま放置されていたため是正）

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年7月24日 09:23 JST 更新</span><br>
  📊 <strong>フーシ派がサウジタンカー2隻を紅海で攻撃し海上封鎖宣言を実行——トランプ氏はイランへの「大規模攻撃」検討を警告、原油はブレント100ドルを突破：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — フーシ派参戦・原油急騰で外交テーブルの機運はさらに後退<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — カザフスタンCPC停止等ホルムズ以外にも供給混乱が波及し単純な現状維持シナリオは後退<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — サウジタンカー攻撃の実行・クウェート/バーレーンへの攻撃継続で、封鎖の実害が地域全体にさらに拡散<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — トランプ氏の「大規模攻撃」検討発言により、軍事エスカレーションの現実味が増大<br>
  <strong style="color:#f87171;">フーシ派参戦が「宣言」から「実行」段階に移行し、トランプ氏の「大規模攻撃」検討発言と合わせて、軍事エスカレーションのリスクが一段と高まっている（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月24日 09:23 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（A/B/C/D 本文）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>米軍による対イラン空爆が7/25未明、13夜連続の後に開戦後初めて途絶した。並行してオマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展を見せており、オマーン外交団の7/24テヘラン訪問も伝えられている。これらは外交解決へ向けた小さな好材料だが、10日間停戦案の正式受諾やトランプ大統領の「大規模攻撃」検討撤回は確認されておらず、一時的な小康状態にとどまる可能性も残る。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>米軍による対イラン攻撃休止は7/27時点で3日目に入り、トランプ大統領は米イラン協議が進行中で合意に至る可能性があると発言した。イラン・オマーンの次官級協議も「建設的」と双方が評価し、テヘランでの協議は継続される。ただしイラン外務省は米との直接協議を否定しており、対象船舶・航路・料金・発効時期を定めた合意文書はいずれも公表されていない。外交進展の「兆し」は増えたが、「合意」段階には至っていない。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>空爆停止とオマーン・イラン仲介協議の進展は、事態がすぐさま核査察問題の実務交渉に戻ることを意味しない。IRGCが南ルートの不正通航船に警告射撃を行うなど、イランは自国の管理権を維持する姿勢を崩しておらず、機雷除去（7/17期限を徒過）にも依然着手していない。膠着継続の中で、軍事面のみが一時的に沈静化している段階と評価できる。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>Kpler・Windwardが確認した7/26のホルムズ通航はわずか7隻で、平常時の約6分の1にとどまる。イランは無許可で北側航路以外を通過しようとした船舶6隻を引き返させたと主張しており、通航管理の実権を維持する姿勢を崩していない。機雷除去（7/17期限を徒過）にも依然着手しておらず、攻撃休止・協議進展という外交面の好材料とは裏腹に、海上の実態は低水準の膠着が続いている。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>IRGCによる南ルート不正通航船への警告射撃は、イランがホルムズ海峡の管理権限を制度的に固定化しようとする動きの一環と解釈できる。フーシ派によるサウジアラムコ拠点攻撃の表明も、紅海側の緊張を継続させている。米イラン間の空爆停止・仲介協議進展は好材料だが、海峡・紅海双方での「管理の制度化」路線自体は後退しておらず、シナリオCの水準は前回からおおむね据え置きと評価する。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>イランが無許可船6隻を引き返させたとの主張や、全通航船が北側航路に集中している実態は、イランがホルムズ海峡の管理権限を制度的に固定化しようとする路線の継続を示す。フーシ派によるサウジ東西輸送網（紅海向け原油供給網）への攻撃発表も、紅海側での「管理の制度化」圧力を新たに加えるものだ。米イラン間の攻撃休止・協議進展は好材料だが、通航管理そのものを巡る力学は変わっておらず、シナリオCの水準はおおむね据え置きと評価する。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>米軍は7/25未明、13夜連続の対イラン空爆を初めて見送った。トランプ大統領が予告していた「大規模攻撃」は、少なくとも本日時点では実行に移されておらず、シナリオD（多国間・多正面にわたる実力による現状変更）が想定する即時の全面エスカレーションからは距離を置く形となっている。フーシ派の紅海攻撃継続というリスク要因は残るが、シナリオCとの差（C=制度的対立の継続、D=実力による現状変更の実行）は、本日時点ではやや開いたと評価する。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>米軍による対イラン攻撃休止は7/27時点で3日目に継続し、トランプ大統領は協議による合意の可能性にも言及した。原油先物の急落（ブレント-7.3%）は市場が当面の全面エスカレーションを織り込んでいないことを示唆する。ただし米国は協議失敗時の攻撃再開に明確に言及しており、正式な停戦文書はなお存在しない。フーシ派の紅海攻撃継続というリスク要因も残るため、シナリオDの水準はさらにやや低下したが、消滅したわけではないと評価する。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオ フッター（次の焦点5つ＋分析日時）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米の空爆停止が一時的か継続的かの見極め</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">オマーン・イラン仲介協議の進捗と正式合意の可否</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">フーシ派・紅海方面の攻撃継続とバブエルマンデブ海峡への影響</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">IRGCによる南ルート取り締まり強化の航行への影響</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月26日 10:30 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米・イラン協議の実態（米「進行中」・イラン否定）の見極め</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン・オマーン次官級協議の合意文書化の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">フーシ派・紅海方面の攻撃継続とサウジ東西輸送網への影響</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">北側航路一極集中・無許可船引き返しの継続性</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月28日 10:19 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月26日 10:30 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】イラン革命防衛隊（IRGC）は、直近24時間で南ルートを通じた不正・危険な経路での通航を試みた船舶4隻に警告射撃を実施し進路変更させたと発表——イランは南ルート通航船にも自国の許可・通航料を求める姿勢を強めている。【北ルート（Iran coastline / IRGC管理）】対イラン海上封鎖は継続中も、米軍による対イラン空爆は7/25未明に13夜ぶりで停止。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限は7/17（MOU第5条）を未着手のまま徒過。【オマーン・イラン仲介】ホルムズ海峡再開・両国領海管理を巡る協議に進展——オマーン外交団が7/24テヘランを訪問。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。フーシ派はサウジアラムコのジザン・ヤンブー拠点への攻撃を表明し、バブ・エル・マンデブ海峡経由の迂回ルートにも脅威継続。🇯🇵 日本関係船舶：残り4隻で変化なし（7/26 10:30 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月28日 10:19 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【北側航路（イラン指定・北側航路）】Kpler・Windwardともに7/26の通航は7隻と確認。全船がイラン指定の北側航路に集中し、イランは無許可で通過を試みた船舶6隻を引き返させたと主張。【南ルート（Omani coastal corridor）】イラン管理下での通航は事実上なし——通航船はほぼ全て北側に集約。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限は7/17（MOU第5条）を未着手のまま徒過。【米・イラン攻撃休止】7/25未明の停止から3日目に継続——トランプ氏「協議中、合意の可能性」に対しイラン外務省は直接協議を否定。【イラン・オマーン仲介】7/25〜26にテヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表。【紅海・バブエルマンデブ】フーシ派がサウジ東西輸送網（紅海向け原油供給網）へ無人機攻撃を発表・商品輸送船の通航は数カ月ぶり低水準（Kpler：11隻）。【UKMTO 警戒水準】Substantial（継続）。EUNAVFOR ASPIDESは紅海南部の脅威水準を中程度→高いへ引き上げ。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（7/28 10:19 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）― 最後に作成

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🗣️ 米、13夜ぶりに対イラン空爆停止——オマーン・イラン、ホルムズ再開協議で進展。フーシ派は紅海攻撃継続を表明。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⚠️ IRGCが南ルート不正通航船4隻に警告射撃——原油は98ドル台へ反落・日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 空爆停止の継続性とオマーン仲介協議の行方が焦点、封鎖149日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残21日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ5枚

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚓フーシ派、サウジタンカー攻撃を実行</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️トランプ氏「大規模攻撃」検討を警告</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️カザフスタンCPC原油輸出停止</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント100ドル突破・+7.00%</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(56,189,248,0.15);border:1px solid rgba(56,189,248,0.3);color:#7dd3fc;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️トランプ氏「協議中、合意の可能性」</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷イラン「直接協議は要請せず」</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚢通航7隻・北側航路に集中</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油急落・ブレント89.68ドル(-7.3%)</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

### updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月26日 10:30 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年7月28日 10:19 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest：新規3件を先頭に追加（既存6件のうち最古3件はClaude Codeがarchiveへ移動）

> Claude Codeへの指示：`latest` 配列は最大6件のため、以下の新規3件を先頭に追加した後、
> 現在の配列末尾3件（id: `latest-houthi-saudi-tanker-attack-0723`／`latest-brent-100-kazakhstan-cpc-0723`／`latest-rubio-escort-coalition-0722`）を
> `archive` の先頭バッチ（`batchLabel`: "2026年7月23日〜24日"）へ移動してください。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-us-strikes-pause-0725",
<!-- OLD:END -->
<!-- NEW:START -->
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
    },
    {
      "id": "latest-us-strikes-pause-0725",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest：末尾3件のフラグ整理（isLatest は新規追加分のみtrueとする）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "id": "latest-us-strikes-pause-0725",
      "title": "米、13夜連続の対イラン空爆を停止——開戦後初めての小康状態",
      "body": "米軍による対イランへの空爆は、7月25日未明（現地時間）、13夜連続の攻撃の後、開戦後初めて途絶した。イラン保健省報道官はX（旧Twitter）に「イランは平穏な夜を過ごした」と投稿。米中央軍（CENTCOM）は取材への即時のコメントを行っていない。",
      "sourceLabel": "Washington Post",
      "date": "2026年7月25日（現地）/ 2026年7月26日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.washingtonpost.com/world/2026/07/25/iran-us-hormuz-strait-war-25-july-2026/db469ab4-880e-11f1-9cec-0fb26676f07e_story.html",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
      "id": "latest-us-strikes-pause-0725",
      "title": "米、13夜連続の対イラン空爆を停止——開戦後初めての小康状態",
      "body": "米軍による対イランへの空爆は、7月25日未明（現地時間）、13夜連続の攻撃の後、開戦後初めて途絶した。イラン保健省報道官はX（旧Twitter）に「イランは平穏な夜を過ごした」と投稿。米中央軍（CENTCOM）は取材への即時のコメントを行っていない。",
      "sourceLabel": "Washington Post",
      "date": "2026年7月25日（現地）/ 2026年7月26日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.washingtonpost.com/world/2026/07/25/iran-us-hormuz-strait-war-25-july-2026/db469ab4-880e-11f1-9cec-0fb26676f07e_story.html",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

### osint：現在の isLatest:true を false に変更

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "url": "https://www.aljazeera.com/",
      "date": "2026年7月25日（現地）/ 2026年7月26日 JST",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
      "url": "https://www.aljazeera.com/",
      "date": "2026年7月25日（現地）/ 2026年7月26日 JST",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

### osint：新規1件を先頭に追加

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "titleJa": "【Al Jazeera】米、13夜ぶりに対イラン空爆停止——オマーン仲介進展もフーシ派は紅海攻撃継続",
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "titleJa": "【Al Jazeera】米・イラン戦争に新戦線——フーシ派がサウジ石油施設を攻撃",
      "titleEn": "New front in US-Iran war escalates as Houthis fire at Saudi oil facilities",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/2026/7/26/new-front-in-us-iran-war-escalates-as-houthis-fire-at-saudi-oil-facilities",
      "date": "2026年7月26日（現地）/ 2026年7月27日 JST",
      "isLatest": true
    },
    {
      "titleJa": "【Al Jazeera】米、13夜ぶりに対イラン空爆停止——オマーン仲介進展もフーシ派は紅海攻撃継続",
<!-- NEW:END -->
<!-- APPLY:END -->

**セルフチェック（S10）**
```
[x] latest 新規3件（トランプ発言・イラン否定＆オマーン協議・通航7隻＆原油急落）を追加
[x] latest 既存6件のうち末尾3件をarchiveへ移動する指示をClaude Codeへ明記
[x] osint 新規1件（Al Jazeera・紅海新戦線）を追加、旧isLatestをfalseに変更
[x] updated フィールドを2026年7月28日 10:19 日本時間JSTに更新
[x] Al Jazeeraはosintのみに使用・latestには混入なし
[x] 全URLはweb検索で実在確認済み（Reuters/IRNA/Kpler/Windward/Al Jazeera）
```

---

## [S11] 更新ログ — 常時表示3件への是正＋新規追加（2ブロック構成）

> ⚠️ 現在の常時表示は本来の3件ではなく4件（7/26・7/24・7/22・7/19）になっており、
> かつ7/19は折り畳み側（log-collapse）にも重複して存在していました。
> 本diffsで「常時表示3件固定」に是正し、重複も解消します。

### ブロック1：常時表示エリア（4件→本日分+2件＝3件に是正）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年7月26日 10:30 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/26 10:30</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態・オマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展（オマーン外交団7/24テヘラン訪問）・IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表・フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明・原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）・米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇・日本関係船は残り4隻で変化なし・封鎖149日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月24日 09:23 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/24 09:23</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行・トランプ大統領はイランへの「大規模攻撃」検討を警告・カザフスタンがドローン攻撃を受けCPCターミナル経由原油輸出を停止・クウェート国境で火災発生（鎮圧）・バーレーンも再攻撃・ルビオ国務長官「複数国がホルムズ護衛に関心」も法的障壁で未実現・Windward報告：南側迂回ルートでタンカー3隻被弾・通航は北側ルートに集中・原油はブレント7/23終値100.65ドル（前日比+7.00%・5月22日以来の高値）・日本関係船は残り4隻で変化なし・封鎖147日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月22日 09:15 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/22 09:15</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン革命防衛隊、ホルムズ海峡南側迂回ルートでタンカー2隻が爆発・炎上したと発表・UKMTOも別のタンカー損傷を報告——米軍は対イラン10夜連続空爆を継続・Axios報道：トランプ大統領は仲介国提示の「10日間停戦」受諾か大規模軍事作戦かの二択に直面——数日内に方針決定へ・イラン高官はロイターに停戦案受領を認める・フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線・ヘグセス国防長官、戦費を約375億ドルと試算・原油はブレント7/21終値91.10ドル（前日比+2.11%）・日本関係船は残り4隻で変化なし・封鎖145日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/19 10:17</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省「米イラン停戦覚書は危機段階に入った」と表明・トランプ「停戦は終わった」と言及・米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊・イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃・ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者）・クウェート石油公社施設に甚大な被害・イラン側発表で直近の米空爆により46名死亡400名超負傷・ホルムズ通航量は7/16に8隻のみで3週間ぶり最低水準・原油はブレント7/17終値88.09ドル（週間+14%超）・日本関係船は残り4隻で変化なし・封鎖142日目・ニュース3件更新・osint更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年7月28日 10:19 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/28 10:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領「イランと協議中、合意に近づく可能性」（7/27）——一方イラン外務省バガイ報道官は米との直接協議要請を否定し通航状況も不変と主張・イラン・オマーンは7/25〜26テヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表・ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張（Kpler/Windward）・フーシ派、サウジ東西輸送網へ無人機攻撃を発表——紅海側にもリスク拡大・原油は攻撃休止・外交期待で急落しブレント89.68ドル（前日比-7.3%）・インドMRPLが原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記・日本関係船は残り4隻で変化なし・封鎖151日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月26日 10:30 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/26 10:30</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態・オマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展（オマーン外交団7/24テヘラン訪問）・IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表・フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明・原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）・米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇・日本関係船は残り4隻で変化なし・封鎖149日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月24日 09:23 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/24 09:23</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行・トランプ大統領はイランへの「大規模攻撃」検討を警告・カザフスタンがドローン攻撃を受けCPCターミナル経由原油輸出を停止・クウェート国境で火災発生（鎮圧）・バーレーンも再攻撃・ルビオ国務長官「複数国がホルムズ護衛に関心」も法的障壁で未実現・Windward報告：南側迂回ルートでタンカー3隻被弾・通航は北側ルートに集中・原油はブレント7/23終値100.65ドル（前日比+7.00%・5月22日以来の高値）・日本関係船は残り4隻で変化なし・封鎖147日目・ニュース3件更新・osint更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse 先頭に旧3・4件目（7/22・7/19）を挿入し、最古（7/12）を削除

> log-collapse の現在の先頭は「2026年7月19日 10:17 JST」ですが、これはブロック1で常時表示から外れる7/19分と同一エントリーです。
> 重複させないため、ブロック1で外れる7/22分のみをここに新規挿入し、7/19分はcollapse側の既存エントリーをそのまま維持してください。
> また、追加後の合計件数（常時表示3＋collapse内）が10件を超えるため、collapse最古の「2026年7月12日 09:19 JST」エントリーを削除し、update_log.jsonへ追記してください。

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月22日 09:15 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/22 09:15</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン革命防衛隊、ホルムズ海峡南側迂回ルートでタンカー2隻が爆発・炎上したと発表・UKMTOも別のタンカー損傷を報告——米軍は対イラン10夜連続空爆を継続・Axios報道：トランプ大統領は仲介国提示の「10日間停戦」受諾か大規模軍事作戦かの二択に直面——数日内に方針決定へ・イラン高官はロイターに停戦案受領を認める・フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線・ヘグセス国防長官、戦費を約375億ドルと試算・原油はブレント7/21終値91.10ドル（前日比+2.11%）・日本関係船は残り4隻で変化なし・封鎖145日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：合計10件超過分（最古の7/12 09:19エントリー）を削除

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月12日 09:19 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/12 09:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>IRGC、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）・CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」・停戦は事実上崩壊・オマーンが通航料なしの南北二経路案を提示（南＝自由航行、北＝イラン事前承認制だが無料）——アラグチー外相はオマーン外相と会談も結論持ち帰りで検討中・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント週間+5〜6%で$76台高止まり（7/10終値時点）・封鎖135日目・ニュース3件更新・osint更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

**update_log.json への追加（配列先頭）：**

```json
{"date":"2026/07/28 10:19","text":"【超重大更新】トランプ大統領「イランと協議中、合意に近づく可能性」（7/27）——一方イラン外務省バガイ報道官は米との直接協議要請を否定し通航状況も不変と主張・イラン・オマーンは7/25〜26テヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表・ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張（Kpler/Windward）・フーシ派、サウジ東西輸送網へ無人機攻撃を発表——紅海側にもリスク拡大・原油は攻撃休止・外交期待で急落しブレント89.68ドル（前日比-7.3%）・インドMRPLが原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記・日本関係船は残り4隻で変化なし・封鎖151日目・ニュース3件更新・osint更新"}
{"date":"2026/07/12 09:19","text":"【超重大更新】IRGC、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）・CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」・停戦は事実上崩壊・オマーンが通航料なしの南北二経路案を提示（南＝自由航行、北＝イラン事前承認制だが無料）——アラグチー外相はオマーン外相と会談も結論持ち帰りで検討中・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント週間+5〜6%で$76台高止まり（7/10終値時点）・封鎖135日目・ニュース3件更新・osint更新"}
```

> ※ 上記2件のうち、1件目（本日分）は先頭に追加、2件目（7/12分・collapseから削除されたもの）は既存アーカイブ内の適切な時系列位置（7/13分と7/11分の間）に挿入してください。

**セルフチェック（S11）**
```
[x] 常時表示 ― 4件→3件（本日分＋7/26＋7/24）に是正
[x] 折り畳み移動 ― 旧3件目（7/22）をlog-collapse先頭に新規挿入・旧7/19分との重複は解消
[x] 総件数 ― 常時表示3＋collapse内7＝10件（cap内に収まる）
[x] 最古超過分（7/12）をcollapseから削除しupdate_log.jsonへ追記
[x] 出典リンク①〜⑧の位置・内容は変更していない
```

---

## [SHIP_CONFIG] dateConfirmed 更新（C01・変化なし）

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年7月26日 10:30 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。米軍は13夜ぶりに対イラン空爆を停止し、オマーン・イランはホルムズ海峡再開協議で進展を見せる一方、IRGCは南ルート不正通航船に警告射撃を実施）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年7月28日 10:19 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。米・イランの直接攻撃休止は3日目に継続——トランプ氏「協議中、合意の可能性」／イラン外務省は直接協議を否定し通航状況も不変と主張。イラン・オマーンは次官級で通航管理協議を継続中）'
<!-- NEW:END -->
<!-- APPLY:END -->

**C01 タンカー確認（必須記載）**

| セクション | 変更内容 |
|---|---|
| C01 タンカー確認 | 日本語クエリ①「日本関係船舶 ホルムズ海峡 通過 足止め 7月」②「外務省 ホルムズ海峡 日本関係船舶 7月28日」③「金子国交相 記者会見 ホルムズ海峡 日本関係船舶」＋英語クエリ「Japanese ships Strait of Hormuz stranded detained July 2026」の計4クエリを個別実行済み。外務省サイトの最新発表は6/19付（全邦人乗船船退避完了）、国交省会見は7/10付（金子国交相・残り4隻）から更新なしを確認。**変化なし**→ dateConfirmed を「2026年7月28日 10:19 JST 確認・変化なし」で更新。 |

---

## [JSON-LD] dateModified 更新（毎回必須）

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-26T10:30:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-28T10:19:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [archive_timeline.json] 本日分エントリー追加

> Claude Codeへの指示：`docs/data/archive_timeline.json` の `entries` 配列の最後の要素（date: "2026-07-26"）を確認し、
> その閉じ `}` の直後にカンマを追加して、以下のJSONオブジェクトを配列の新しい最後の要素として挿入してください（既存エントリーは変更しないこと）。

```json
{
  "date": "2026-07-28",
  "dateLabel": "2026/07/28 10:19",
  "blockadeDay": 151,
  "summary": "トランプ大統領「イランと協議中、合意に近づく可能性」（7/27）——一方イラン外務省バガイ報道官は米との直接協議要請を否定し通航状況も不変と主張・イラン・オマーンは7/25〜26テヘランで次官級協議「建設的」——共通原則・運用メカニズムを協議も合意文書は非公表・ホルムズ通航は7/26も7隻に留まり全船が北側航路に集中——イランは無許可船6隻を引き返させたと主張（Kpler/Windward）・フーシ派、サウジ東西輸送網へ無人機攻撃を発表——紅海側にもリスク拡大・原油は攻撃休止・外交期待で急落しブレント89.68ドル（前日比-7.3%）・インドMRPLが原油スポット入札で紅海・ホルムズ経由の除外条項を初めて明記・日本関係船は残り4隻で変化なし・封鎖151日目・ニュース3件更新・osint更新",
  "relatedNews": [
    {"title": "トランプ氏「イランと協議中、合意に近づく可能性」——ウォルツ大使は空爆停止の理由を説明", "url": "https://www.reuters.com/world/middle-east/iran-says-it-still-controls-strait-not-seeking-talks-after-trump-halts-bombing-2026-07-27/", "sourceLabel": "Reuters"},
    {"title": "イラン、米との協議否定も「オマーンとの通航協議は建設的」——次官級でテヘラン協議", "url": "https://www.reuters.com/world/middle-east/iran-has-not-asked-resumption-talks-with-us-iranian-spokesperson-says-2026-07-27/", "sourceLabel": "Reuters / IRNA"},
    {"title": "ホルムズ通航、7/26も7隻に留まる——原油は攻撃休止・外交期待で急落", "url": "https://www.reuters.com/business/energy/oil-slips-more-than-5-after-us-pauses-strikes-iran-2026-07-26/", "sourceLabel": "Kpler / Windward / Reuters"}
  ]
}
```

---

## ✅ 出力前セルフチェック（全項目）

```
[x] S01 ヘッダー ― 2026年7月28日 10:19 JST ✓
[x] S02 TICKER ― 米イラン協議応酬・イランオマーン次官級協議・通航7隻・原油急落・MRPL航路除外・封鎖151日目 ✓
[x] S03 速報インシデント ― 7/28 10:19付け・6件新規追加 ✓
[x] S04 情勢カード3枚 ― 日付・数値・出典を7/28版に更新 ✓
[x] S04.5 全ルート現況サマリー ― 7/28 10:19 JST更新に統一 ✓
[x] S05 COUNTDOWN ― 封鎖151日目・MOU最終期限残19日 ✓
[x] S06 シナリオ確率補足バナー ― 7/24付け放置分を7/28 10:19 JSTへ是正・矢印更新（A↑ B→ C→ D↓） ✓
[x] S07 シナリオ4本 ― A/B/C/D本文を7/28情勢に更新 ✓
[x] S08 シナリオフッター ― 次の焦点5点を7/28版に更新 ✓
[x] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成）✓
[x] S10 news_data.json更新メモ ― latest新規3件・osint新規1件・updated日付 ✓
[x] S11 更新ログ ― 常時表示4→3件へ是正・重複解消・ブロック2件＋削除1件・合計10件維持 ✓
[x] SHIP_CONFIG ― dateConfirmed更新・C01 4クエリ実施済み・変化なし ✓
[x] JSON-LD ― dateModified更新 ✓
[x] archive_timeline.json ― 本日分（2026-07-28・封鎖151日目）エントリー追加 ✓

二重封鎖表記チェック：本日分では「イラン・米国による二重封鎖」の単独表記なし（該当箇所なし）✓
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：S04.5で7/28 10:19 JST更新を明示 ✓
人名表記チェック：習近平表記への言及なし・「Trump」単独表記なし（トランプ/トランプ大統領で統一）✓
ニュースURL：全てweb検索で実在確認済み（Reuters/IRNA/Kpler/Windward/Al Jazeera/Muscat Daily）✓
Al Jazeera混入チェック：latestには不使用・osintのみに使用 ✓
禁止媒体チェック：朝日新聞・NHK・東京新聞・テレビ朝日・TBS/TBS NEWS DIG・毎日新聞・Wikipedia使用なし ✓
```

---

## 📎 参考出典（本日の主要ソース）

- Reuters: Iran says it still controls strait, not seeking talks, after Trump halts bombing（7/27）
- Reuters: Iran has not asked for resumption of talks with US（7/27）
- IRNA: Iran says Strait of Hormuz talks with Oman constructive, unrelated to US（7/26）
- AP: Mediators see progress in efforts to halt Iran war（7/27）
- Muscat Daily: Oman, Iran hold talks on Strait of Hormuz shipping safety（7/26）
- Kpler: Strait of Hormuz crossings drop 70% as tanker traffic shifts almost entirely to the Iranian route
- Windward: The Red Sea Reopens as a Second Front While Saudi Crude Routes Around the Blockade
- Reuters: Red Sea shipping slows after Houthi attack on Saudi Arabia, data shows（7/27）
- Reuters: Houthis say they targeted Saudi east-west oil transport（7/27）
- Reuters: Saudi Arabia says it destroyed drones launched by Iran-backed groups in Iraq（7/27）
- Reuters: India's MRPL seeks crude via tender avoiding Red Sea and Hormuz（7/27）
- Reuters: Oil slips more than 5% after US pauses strikes on Iran（7/26〜27）
- Reuters: QatarEnergy extends LNG force majeure, charters out tankers into October（7/23）
- Al Jazeera: New front in US-Iran war escalates as Houthis fire at Saudi oil facilities（7/26）
- 参考分析：global-scm.com「ホルムズ海峡危機：情勢と今後の見通し（2026年7月28日更新）」
- C01確認：外務省報道発表（直近6/19付）・国土交通省 金子国交相会見（直近7/10付）― いずれも新規発表なしを日英クエリで確認
