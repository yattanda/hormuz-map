# index_html_diffs.md — 2026年7月26日 10:30 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> news_data.json の変更は `<!-- FILE:docs/data/news_data.json -->` 指定ブロックを対象ファイルとして適用してください。
> archive_timeline.json の変更は `<!-- FILE:docs/data/archive_timeline.json -->` 指定ブロックを対象ファイルとして適用してください（entries配列末尾に追加・既存エントリーは変更しないこと）。
> update_log.json は、S11で折り畳みから削除される最古エントリー（2026/07/11 08:38）を配列先頭に追加してください（このファイルはrun.batでpushされないため、Claude Codeが直接編集・commitしてください）。
> 作業完了後に commit してください。push は確認後に指示します。

---

## ⚠️ セルフチェック（本文執筆前の事前貼付・2026/7/9ルール）

本日のセルフチェック項目数：19件（+ 全体系チェック3件 = 計22項目）

```
[✓] S01 ヘッダー ― 2026年7月26日 10:30 JST・封鎖149日目に更新
[✓] S02 TICKER ― 米、13夜ぶりに対イラン空爆停止／オマーン・イラン、ホルムズ再開協議で進展／フーシ派サウジアラムコ拠点攻撃／原油反落／封鎖149日目
[✓] S03 速報インシデント ― 7/26 10:30付け・4件新規追加（対イラン空爆停止／オマーン仲介進展／IRGC警告射撃で船舶4隻進路変更／フーシ派アラムコ攻撃）
[✓] S04 情勢カード3枚 ― 外交・軍事・船舶市場を7/26版に更新
[✓] S05 COUNTDOWN ― 封鎖149日目・機雷除去期限(7/17)徒過継続・MOU最終期限残21日
[✓] S06 シナリオ確率補足バナー ― 7/26 10:30 JST日付更新・矢印をA→B→C→D↓に変更（空爆停止・オマーン仲介進展を反映）
[✓] S07 シナリオ4本 ― A/B/C/D本文を空爆停止・オマーン仲介進展・フーシ派紅海攻撃継続で更新
[✓] S08 シナリオフッター ― 次の焦点5点を7/26版に更新
[✓] S09 30秒カラム ― 3行サマリー＋バッジ更新（最後に作成）
[✓] S10 news_data.json更新メモ ― latest 3件新規・osint 1件・updated日付
[✓] S11 更新ログ ― 2ブロック構成で先頭に7/26 10:30行追記・旧3件目（7/19）をlog-collapseへ移動・合計11件超過分（7/11 08:38エントリー）を削除
[✓] SHIP_CONFIG ― C01検証実施・変化なし・dateConfirmedを7/26に更新
[✓] JSON-LD dateModified ― 2026-07-26T10:30:00+09:00に更新
[✓] C01タンカー確認 ― 日本語3クエリ＋英語1クエリを個別実行・変化なし確認
[✓] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[✓] 全体 ― ニュースURLにAI捏造・推測URLが混入していないか（web検索確認済みURLのみ使用）
[✓] 全体 ― 📰関連最新ニュースにAl Jazeeraが混入していないか（osintのみに配置）
[✓] 全体 ― 人名が日本語表記になっているか（トランプ・ルビオ・ゼレンスキー等）
[✓] 全体 ― diffs.md本文執筆の前にproject_knowledge_searchでセルフチェック原文を取得したか

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記のまま維持 ✓（変更不要）
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：本日分で7/26 10:30 JST「更新」に是正（IRGC警告射撃・オマーン仲介進展という新情報のため「更新」表記・再確認済ではない）✓
```

---

## C01 タンカー確認（必須・毎回実施）

- 日本語クエリ①「日本関係船舶 ホルムズ海峡 通過 足止め 7月」／②「外務省 ホルムズ海峡 日本関係船舶 7月24日 発表」／③「金子国土交通大臣 記者会見 ホルムズ海峡 日本関係船舶 隻数」を個別実行
- 英語クエリ「Japanese ships Strait of Hormuz stranded detained July 2026」を実行
- 結果：金子国交相の新規会見・外務省の新規発表は確認されず。直近の確定情報は7/10会見の「残り4隻」のまま（7/24確認時点から変化なし）
- 判定：**変化なし** → SHIP_CONFIG の totalShips・passableShips は据え置き、dateConfirmed のみ本日日時＋「変化なし」で更新

---

## 本日の主要トピック（背景メモ）

- **米軍、13夜連続の対イラン空爆後、7/25未明（現地時間）は初めて空爆なし**——イラン保健省報道官は「平穏な夜だった」とX投稿。CENTCOMは即時のコメントなし（Washington Post, 7/25）
- **オマーン・イラン、ホルムズ海峡再開と両国領海管理を巡る協議で「進展」**——地域筋2名がCBS Newsに証言（7/25）。オマーン外交団は7/24（金）テヘランを訪問し、イラン国営IRNA通信によれば「海峡での船舶交通を管理する適切なメカニズムの構築」を協議したと7/25伝達
- **イラン革命防衛隊（IRGC）、南側（オマーン沿岸）迂回ルートを通じて不正・危険な経路での通航を試みた船舶4隻に対し、過去24時間で警告射撃を実施し進路変更させたと発表**——イラン国営テレビが伝達（CBS News, 7/25）。イランは南ルート通航船に対しても自国の許可・通航料を求める姿勢を強めている
- **フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明**（7/25・土曜）——紅海方面での攻撃を継続する姿勢を改めて示した
- **原油は反落基調**——ブレントは7/23終値100.65ドルから7/24終値98.38ドル（前日比-2.29%）まで反落。週間では依然+10%超の水準。7/25朝時点（米東部時間）ではさらに97ドル前後まで下落したとの報道もあり、7/24の2ヶ月ぶり高値（一時102ドル）からの反落が続く
- **米国内ガソリン価格は上昇継続**——7/25時点で全米平均1ガロン4.11ドル（週間+11セント・開戦来+38%）
- **カザフスタンCPC（カスピ海パイプラインコンソーシアム）ターミナルは依然停止継続**——新規情報なし、前回確認時点の状態を維持
- **日本関係船は残り4隻で変化なし**（7/26 10:30 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——トランプ大統領はイランへの「大規模攻撃」検討を警告／カザフスタンがドローン攻撃を受けCPCターミナル経由の原油輸出を停止／クウェート国境沿いで火災・バーレーンも再攻撃を受ける／原油はブレント7/23終値100.65ドルまで急伸（前日比+7.00%・5月22日以来の高値）／ルビオ国務長官「複数国がホルムズ護衛参加に関心」も法的障壁で未実現／封鎖147日目）</span>
    <span class="badge-item badge-date">📅2026年7月24日 09:23 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米軍が13夜ぶりに対イラン空爆を停止——一時的な小康状態／オマーン・イラン、ホルムズ海峡再開・領海管理を巡る協議で進展／IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表／フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明／原油はブレント7/24終値98.38ドルまで反落も週間+10%超維持／封鎖149日目）</span>
    <span class="badge-item badge-date">📅2026年7月26日 10:30 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年7月24日 09:23 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月24日 09:23 JST） -->
      🚨【原油100ドル突破】ブレント7/23終値100.65ドル（前日比+7.00%）——5月22日以来の高値（7/24 JST）｜⚓ フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——トランプ氏「大規模攻撃を検討中」とイランへ責任転嫁を警告（7/23）｜🛢️ カザフスタン、ドローン攻撃を受けCPCターミナル経由の原油輸出を停止（7/23）｜🔥 クウェート国境Al-Abdali沿いで火災発生・バーレーンも再攻撃を受ける（7/23）｜🕊️ ルビオ国務長官「複数国がホルムズ護衛参加に関心」——法的・政治的障壁で正式化せず（7/22）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残23日｜封鎖147日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月26日 10:30 JST） -->
      🕊️【米、13夜ぶり空爆停止】対イラン空爆が7/25未明、開戦後初めて途絶——一時的な小康状態（7/25 JST）｜🇴🇲 オマーン・イラン、ホルムズ海峡再開・両国領海管理を巡る協議で進展——オマーン外交団が7/24テヘラン訪問（CBS/IRNA、7/25）｜⚠️ IRGC、南側迂回ルートの不正通航船4隻に警告射撃——進路変更させたと発表（7/25）｜⚓ フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明（7/25）｜🛢️ 原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%）——週間では依然+10%超（7/24〜25 JST）｜⛽ 米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇（7/25）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残21日｜📋 7/26 10:30 JST確認済——軍事面は小康状態も外交・海上情勢は流動的｜封鎖149日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

**対象：** `<!-- 速報インシデント　トグルボタン -->` 内

### トグルボタン内タイトル・日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">原油100ドル突破／フーシ派、サウジタンカー攻撃——トランプ氏「大規模攻撃」検討／カザフスタンCPC原油輸出停止</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/24 09:23 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米、13夜ぶり空爆停止／オマーン・イラン、ホルムズ再開協議で進展／フーシ派サウジアラムコ拠点攻撃</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/26 10:30 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/24 09:23 速報】イエメンの親イラン武装組織フーシ派が、サウジアラビアの原油タンカー2隻を紅海で攻撃（7/23）——先に宣言していたサウジ海上封鎖の実行と見られる｜トランプ大統領は、イランを紅海での攻撃の責任者とみなすと警告し、「大規模攻撃を検討中」と発言｜カザフスタンがドローン攻撃を受け、CPC（カスピ海パイプラインコンソーシアム）ターミナル経由の原油輸出を停止（7/23）——ホルムズ以外の供給網にも混乱が波及｜クウェート国境沿いAl-Abdaliでイラン攻撃による火災が発生し鎮圧、バーレーンも再び攻撃を受けたとAl Jazeeraが報告｜ルビオ国務長官は、複数国がホルムズ海峡での商船護衛参加に関心を示していると明らかにしたが、法的・政治的障壁で正式合意には至っていないと説明（7/22）｜Windward海事インテリジェンスによれば、直近24時間で南側迂回ルート（クムザール・リマ沖）のタンカー3隻が被弾し、通航はほぼ北側ルートに集中｜原油はブレント7/23終値100.65ドルまで急伸（前日比+7.00%・5月22日以来の高値）｜日本関係船は残り4隻で変化なし｜封鎖147日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/26 10:30 速報】米軍による対イラン空爆が7/25未明（現地時間）、13夜連続の後初めて途絶——イラン保健省報道官は「平穏な夜だった」とX投稿、CENTCOMは即時コメントなし｜オマーンとイランは、ホルムズ海峡再開と両国領海の管理を巡る協議で進展があったと地域筋2名がCBS Newsに証言（7/25）——オマーン外交団は7/24にテヘランを訪問し「船舶交通を管理する適切なメカニズム」を協議したとイラン国営IRNAが伝達｜イラン革命防衛隊（IRGC）は、南側（オマーン沿岸）迂回ルートを通じ不正・危険な経路での通航を試みた船舶4隻に対し、直近24時間で警告射撃を実施し進路変更させたと発表｜フーシ派は、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明（7/25）——紅海方面での攻撃継続姿勢を改めて示す｜原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%）も週間では依然+10%超｜米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇｜日本関係船は残り4隻で変化なし｜封鎖149日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に4件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fca5a5;font-weight:700;">⚓ 7/23 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🕊️ 7/25 JST</span>
  <span style="color:#e2e8f0;"> 米軍による対イランへの空爆が、7/25未明（現地時間）に13夜連続の後、開戦後初めて途絶した。イラン保健省報道官は「平穏な夜だった」とX（旧Twitter）に投稿。米中央軍（CENTCOM）は即座のコメントを避けている。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🇴🇲 7/25 JST</span>
  <span style="color:#e2e8f0;"> オマーンとイランの間で、ホルムズ海峡の再開と両国領海の管理を巡る協議に進展があったと、地域筋2名がCBS Newsに証言。オマーン外交団は7/24にテヘランを訪問し、イラン国営IRNA通信によれば「海峡での船舶交通を管理する適切なメカニズムの構築」について協議したという。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">⚠️ 7/25 JST</span>
  <span style="color:#e2e8f0;"> イラン革命防衛隊（IRGC）は、南側（オマーン沿岸）迂回ルートを通じ不正・危険な経路での通航を試みた船舶4隻に対し、直近24時間で警告射撃を実施し進路変更させたと発表。イラン国営テレビが伝達した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚓ 7/25 JST</span>
  <span style="color:#e2e8f0;"> イエメンの親イラン武装組織フーシ派は、サウジアラムコのジザン・ヤンブー両拠点への攻撃を表明した。紅海方面での攻撃を継続する姿勢を改めて示すもの。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fca5a5;font-weight:700;">⚓ 7/23 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

### カード① 外交交渉

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">💰 外交：フーシ派参戦でトランプ氏「大規模攻撃」検討——ルビオ氏「護衛連合に複数国関心」も未実現</div>
        <div class="s-body">フーシ派がサウジアラビアの原油タンカー2隻を紅海で攻撃したことを受け、トランプ大統領はイランに責任があるとの立場を示し、「大規模攻撃を検討中」と発言。10日間停戦案の受諾か大規模軍事作戦かという二択は、フーシ派参戦によりさらに緊迫化した。一方、ルビオ国務長官は複数国がホルムズ海峡での商船護衛への参加に関心を示していると明らかにしたが、法的・政治的障壁により正式な合意・実施には至っていない。外交的収拾と軍事エスカレーションの綱引きが続く。</div>
        <div class="s-src">出典: Al Jazeera / Trading Economics / Barchart（7/22〜23 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🕊️ 外交：米が13夜ぶりに空爆停止——オマーン・イラン、ホルムズ再開協議で進展</div>
        <div class="s-body">米軍による対イランへの空爆は、7/25未明（現地時間）に13夜連続の後、開戦後初めて途絶した。並行して、オマーンとイランの間でホルムズ海峡再開と両国領海の管理を巡る協議に進展があったと地域筋2名がCBS Newsに証言。オマーン外交団は7/24にテヘランを訪問し「船舶交通を管理する適切なメカニズム」を協議したとイラン国営IRNAが伝達した。ただし、これが恒久的な沈静化を意味するかは不透明で、10日間停戦案やトランプ大統領の「大規模攻撃」検討はいずれも撤回されていない。</div>
        <div class="s-src">出典: Washington Post / CBS News / IRNA（7/25 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 軍事情勢

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">⚔️ 軍事：フーシ派がサウジタンカー2隻を攻撃・戦線が紅海へ拡大／クウェート・バーレーンも再攻撃</div>
        <div class="s-body">イエメンの親イラン武装組織フーシ派は7/23、サウジアラビアの原油タンカー2隻を紅海で攻撃したと発表——7/20宣言のサウジ海上封鎖の実行とみられる。クウェート国境沿いAl-Abdali付近ではイラン攻撃による火災が発生（鎮圧済み）、バーレーンも再び攻撃を受けたとAl Jazeeraが報告。Windward海事インテリジェンスによれば、直近24時間でホルムズ海峡南側迂回ルート（クムザール・リマ沖）のタンカー3隻が被弾し、通航はほぼ北側ルートに集中している。一方、Bloombergによれば商船三井系を含むVLCC3隻がリスクを冒してホルムズ海峡経由でペルシャ湾を脱出した。</div>
        <div class="s-src">出典: Al Jazeera / Windward / Bloomberg（7/23 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">⚠️ 軍事：IRGCが南側迂回ルートの不正通航船4隻に警告射撃／フーシ派はサウジアラムコ拠点を攻撃と表明</div>
        <div class="s-body">米軍の対イラン空爆は7/25未明に13夜ぶりで途絶した一方、イラン革命防衛隊（IRGC）は、南側（オマーン沿岸）迂回ルートを通じ不正・危険な経路での通航を試みた船舶4隻に対し、直近24時間で警告射撃を実施し進路変更させたと発表——イランは南ルート通航船にも自国の許可・通航料を求める姿勢を強めている。イエメンの親イラン武装組織フーシ派は、サウジアラムコのジザン・ヤンブー両拠点への攻撃を表明し、紅海方面での攻撃継続姿勢を改めて示した。</div>
        <div class="s-src">出典: CBS News（IRGC・イラン国営テレビ引用）（7/25 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ エネルギー・市場・船舶

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/24再確認）——原油はブレント100ドル突破／カザフスタンCPC停止</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/24 09:23 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。原油はブレント先物が7/23終値で100.65ドル（前日比+7.00%・一時101ドル超）に達し、5月22日以来の高値を記録。フーシ派のサウジタンカー攻撃に加え、カザフスタンがドローン攻撃を受けCPC（カスピ海パイプラインコンソーシアム）ターミナル経由の原油輸出を停止したことも供給不安を増幅させた。WTIも90ドル台に上昇。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残23日に迫っている。</div>
        <div class="s-src">出典: Trading Economics / Barchart / Forbes Advisor（7/23 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/26再確認）——原油はブレント98ドル台へ反落／ガソリンは上昇継続</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/26 10:30 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。原油はブレント先物が7/23終値100.65ドルから7/24終値98.38ドル（前日比-2.29%）まで反落したが、週間では依然+10%超の水準を維持。カザフスタンCPCターミナルの原油輸出停止は新規情報なく継続中とみられる。一方、米国内ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇（開戦来+38%）。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残21日に迫っている。</div>
        <div class="s-src">出典: Trading Economics / CNN（7/25 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

### Phase ラベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 12「フーシ派、サウジタンカー攻撃を実行——トランプ氏『大規模攻撃』検討・原油100ドル突破」——封鎖147日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 13「米、13夜ぶりに空爆停止——オマーン・イラン仲介進展も、フーシ派は紅海攻撃継続」——封鎖149日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### dl-note（速報要約・次の焦点・機雷除去期限）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🚨 <strong>フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行／トランプ大統領、イランへの「大規模攻撃」検討を警告／カザフスタンがドローン攻撃受けCPCターミナル経由原油輸出を停止／クウェート国境で火災・バーレーンも再攻撃／原油はブレント100ドル突破（7/23終値100.65ドル・+7.00%）——日本関係船は残り4隻で変化なし——封鎖147日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残23日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①トランプ氏の「大規模攻撃」実施判断の有無 ②フーシ派参戦の紅海・バブエルマンデブ海峡への影響拡大 ③ホルムズ南側迂回ルートのタンカー被弾続発（Windward報告） ④ルビオ氏言及の護衛連合構想の実現可否 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残23日（8/16）</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🕊️ <strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態／オマーン・イラン、ホルムズ海峡再開・領海管理協議で進展（オマーン外交団7/24テヘラン訪問）／IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更／フーシ派、サウジアラムコのジザン・ヤンブー拠点攻撃を表明——原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）——日本関係船は残り4隻で変化なし——封鎖149日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残21日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米の空爆停止が一時的か継続的かの見極め ②オマーン・イラン仲介協議の進捗と正式合意の可否 ③フーシ派・紅海方面の攻撃継続とバブエルマンデブ海峡への影響 ④IRGCによる南ルート取り締まり強化の航行への影響 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残21日（8/16）</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー（矢印更新）

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
<!-- NEW:END -->
<!-- APPLY:END -->

> 備考：B（→）・C（→、従来の↑から据え置きに変更なし——実際は前回同様「↑」を維持。下記参照）は今回変更しない。

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
<!-- NEW:END -->
<!-- APPLY:END -->

（Claude Codeへの補足：本日の矢印は A：↓→↑／B：→（変更なし）／C：↑→→／D：↑→↓ の3件変更です。上記3ブロックを適用してください。）

---

## [S07] シナリオ4本

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>ルビオ国務長官は複数国がホルムズ海峡での商船護衛への参加に関心を示していると明らかにしたが、法的・政治的障壁により正式な合意には至っていない。フーシ派がサウジタンカー攻撃を実行に移し、トランプ大統領が「大規模攻撃」検討を表明するなど、外交解決に向けた機運は7/22時点よりもさらに後退している。10日間停戦案は依然テーブルには残るが、実現の見通しは不透明さを増している。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>米軍による対イラン空爆が7/25未明、13夜連続の後に開戦後初めて途絶した。並行してオマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展を見せており、オマーン外交団の7/24テヘラン訪問も伝えられている。これらは外交解決へ向けた小さな好材料だが、10日間停戦案の正式受諾やトランプ大統領の「大規模攻撃」検討撤回は確認されておらず、一時的な小康状態にとどまる可能性も残る。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>カザフスタンのCPCターミナル停止は、供給混乱がホルムズ以外にも広がっていることを示しており、単純な現状維持を前提としたシナリオBの想定を超えつつある。クウェート・バーレーンへの攻撃も継続しており、地域全体の緊張が「膠着」という言葉では表現しきれない段階に入っている。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>空爆停止とオマーン・イラン仲介協議の進展は、事態がすぐさま核査察問題の実務交渉に戻ることを意味しない。IRGCが南ルートの不正通航船に警告射撃を行うなど、イランは自国の管理権を維持する姿勢を崩しておらず、機雷除去（7/17期限を徒過）にも依然着手していない。膠着継続の中で、軍事面のみが一時的に沈静化している段階と評価できる。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>Windward海事インテリジェンスによれば、南側迂回ルート（クムザール・リマ沖）でタンカー3隻が被弾し、通航はほぼ北側ルートに集中している。フーシ派によるサウジタンカー攻撃の実行は、ホルムズの代替輸出ルートである紅海側の封鎖をさらに現実のものとし、「完全封鎖の制度化」がホルムズ単独ではなく地域全体に及ぶ構図を一段と強めている。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>IRGCによる南ルート不正通航船への警告射撃は、イランがホルムズ海峡の管理権限を制度的に固定化しようとする動きの一環と解釈できる。フーシ派によるサウジアラムコ拠点攻撃の表明も、紅海側の緊張を継続させている。米イラン間の空爆停止・仲介協議進展は好材料だが、海峡・紅海双方での「管理の制度化」路線自体は後退しておらず、シナリオCの水準は前回からおおむね据え置きと評価する。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>トランプ大統領は、フーシ派のサウジタンカー攻撃を受けイランに責任があるとの立場を示し、「大規模攻撃を検討中」と発言した。フーシ派の参戦（サウジタンカー攻撃実行）により戦線はイエメン・紅海方面へすでに拡大しており、シナリオCとの差はさらに縮小している。シナリオCとの差：C=「封鎖・通航管理を巡る制度的対立」、D=「多国間・多正面にわたる実力による現状変更」。トランプ氏が「大規模攻撃」を実行に移した場合、イスラエルとの共同作戦を含む本格的なエスカレーションへ移行するリスクが最も高い局面にある。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>米軍は7/25未明、13夜連続の対イラン空爆を初めて見送った。トランプ大統領が予告していた「大規模攻撃」は、少なくとも本日時点では実行に移されておらず、シナリオD（多国間・多正面にわたる実力による現状変更）が想定する即時の全面エスカレーションからは距離を置く形となっている。フーシ派の紅海攻撃継続というリスク要因は残るが、シナリオCとの差（C=制度的対立の継続、D=実力による現状変更の実行）は、本日時点ではやや開いたと評価する。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター

<!-- APPLY:START -->
<!-- OLD:START -->
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">トランプ氏の「大規模攻撃」実施判断の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">フーシ派参戦の紅海・バブエルマンデブ海峡への影響拡大</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">ホルムズ南側迂回ルートのタンカー被弾続発（Windward報告）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">ルビオ氏言及の護衛連合構想の実現可否</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月24日 09:23 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米の空爆停止が一時的か継続的かの見極め</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">オマーン・イラン仲介協議の進捗と正式合意の可否</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">フーシ派・紅海方面の攻撃継続とバブエルマンデブ海峡への影響</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">IRGCによる南ルート取り締まり強化の航行への影響</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月26日 10:30 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04-補足] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月24日 09:23 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】Windward海事インテリジェンスによれば、直近24時間で南側迂回ルート（クムザール・リマ沖）のタンカー3隻が被弾し、以降の通航12件のうち南ルート使用は2件のみと事実上機能不全。【北ルート（Iran coastline / IRGC管理）】対イラン海上封鎖は継続中。通航はほぼ北側ルートに集中しているが、依然として低水準。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限は7/17（MOU第5条）を未着手のまま徒過。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。フーシ派がサウジアラビアの原油タンカー2隻を紅海で攻撃し、バブ・エル・マンデブ海峡経由の迂回ルートにも新たな脅威。Bloombergによれば直近24時間でVLCC3隻がリスクを冒してホルムズ海峡を脱出。🇯🇵 日本関係船舶：残り4隻で変化なし（7/24 09:23 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月26日 10:30 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】イラン革命防衛隊（IRGC）は、直近24時間で南ルートを通じた不正・危険な経路での通航を試みた船舶4隻に警告射撃を実施し進路変更させたと発表——イランは南ルート通航船にも自国の許可・通航料を求める姿勢を強めている。【北ルート（Iran coastline / IRGC管理）】対イラン海上封鎖は継続中も、米軍による対イラン空爆は7/25未明に13夜ぶりで停止。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限は7/17（MOU第5条）を未着手のまま徒過。【オマーン・イラン仲介】ホルムズ海峡再開・両国領海管理を巡る協議に進展——オマーン外交団が7/24テヘランを訪問。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。フーシ派はサウジアラムコのジザン・ヤンブー拠点への攻撃を表明し、バブ・エル・マンデブ海峡経由の迂回ルートにも脅威継続。🇯🇵 日本関係船舶：残り4隻で変化なし（7/26 10:30 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー）― 最後に作成

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🗣️ フーシ派、サウジタンカー2隻を紅海で攻撃——トランプ氏「大規模攻撃を検討中」と警告。原油は100ドル突破。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷 カザフスタンCPC停止・クウェート/バーレーンへの攻撃継続——日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ トランプ氏の攻撃実施判断とフーシ派参戦の拡大が焦点、封鎖147日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残23日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

### updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月24日 09:23 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年7月26日 10:30 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列：新規3件を先頭追加

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-houthi-saudi-tanker-attack-0723",
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "id": "latest-us-strikes-pause-0725",
      "title": "米、13夜連続の対イラン空爆を停止——開戦後初めての小康状態",
      "body": "米軍による対イランへの空爆は、7月25日未明（現地時間）、13夜連続の攻撃の後、開戦後初めて途絶した。イラン保健省報道官はX（旧Twitter）に「イランは平穏な夜を過ごした」と投稿。米中央軍（CENTCOM）は取材への即時のコメントを行っていない。",
      "sourceLabel": "Washington Post",
      "date": "2026年7月25日（現地）/ 2026年7月26日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.washingtonpost.com/world/2026/07/25/iran-us-hormuz-strait-war-25-july-2026/db469ab4-880e-11f1-9cec-0fb26676f07e_story.html",
      "isLatest": true
    },
    {
      "id": "latest-oman-iran-talks-progress-0725",
      "title": "オマーン・イラン、ホルムズ海峡再開・領海管理を巡る協議で進展",
      "body": "オマーンとイランの間で、ホルムズ海峡の再開及び両国領海の管理を巡る協議に進展があったと、地域筋2名がCBS Newsに証言した。イラン国営通信IRNAによれば、オマーン外交団は7月24日にテヘランを訪問し、海峡での船舶交通を管理する「適切なメカニズム」の構築について協議したという。",
      "sourceLabel": "CBS News",
      "date": "2026年7月25日（現地）/ 2026年7月26日 JST",
      "label": "🕊️ 外交",
      "url": "https://www.cbsnews.com/live-updates/iran-war-us-trump-strait-hormuz-middle-east/",
      "isLatest": false
    },
    {
      "id": "latest-irgc-warning-shots-houthi-aramco-0725",
      "title": "IRGC、南ルート不正通航船4隻に警告射撃／フーシ派はサウジアラムコ拠点攻撃を表明",
      "body": "イラン革命防衛隊（IRGC）は、南側（オマーン沿岸）迂回ルートを通じ不正・危険な経路での通航を試みた船舶4隻に対し、直近24時間で警告射撃を実施し進路変更させたと発表した。一方、イエメンの親イラン武装組織フーシ派は、サウジアラムコのジザン・ヤンブー両拠点への攻撃を表明し、紅海方面での攻撃継続姿勢を改めて示した。",
      "sourceLabel": "CBS News",
      "date": "2026年7月25日（現地）/ 2026年7月26日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.cbsnews.com/live-updates/iran-war-us-trump-strait-hormuz-middle-east/",
      "isLatest": false
    },
    {
      "id": "latest-houthi-saudi-tanker-attack-0723",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列内 isLatest フラグの付け替え（旧最新記事を false に）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "url": "https://www.barchart.com/futures/quotes/CBN26",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
      "url": "https://www.barchart.com/futures/quotes/CBN26",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列：最古3件（7/21〜7/20分）を archive へ移動

> Claude Codeへの指示：latest配列は現在9件（新規3件＋既存6件）になっているため、最古の3件（id: `latest-hormuz-tankers-fire-0721`・`latest-10day-ceasefire-proposal-0721`・`latest-houthi-saudi-blockade-0720`）をlatest配列から削除し、archive配列の先頭に新規バッチ（batchLabel: "2026年7月20日〜21日 更新分（アーカイブ）"）として、この3件の内容をそのまま移動してください。各アイテムの isLatest は false のまま維持してください。

### osint 配列：新規1件を先頭追加＋旧isLatestをfalseへ

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "titleJa": "【Al Jazeera】トランプ氏「大規模攻撃」を警告——クウェート国境で火災・バーレーンも再攻撃",
      "titleEn": "Iran war updates: Trump warns of unprecedented 'massive attack' on Iran",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/23/iran-war-live-us-launches-new-attacks-houthis-attack-2-saudi-oil-tankers",
      "date": "2026年7月23日（現地）/ 2026年7月24日 JST",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "titleJa": "【Al Jazeera】米、13夜ぶりに対イラン空爆停止——オマーン仲介進展もフーシ派は紅海攻撃継続",
      "titleEn": "Iran war live: US pauses strikes after 13 nights as Oman mediation advances, Houthis continue Red Sea attacks",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/",
      "date": "2026年7月25日（現地）/ 2026年7月26日 JST",
      "isLatest": true
    },
    {
      "titleJa": "【Al Jazeera】トランプ氏「大規模攻撃」を警告——クウェート国境で火災・バーレーンも再攻撃",
      "titleEn": "Iran war updates: Trump warns of unprecedented 'massive attack' on Iran",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/23/iran-war-live-us-launches-new-attacks-houthis-attack-2-saudi-oil-tankers",
      "date": "2026年7月23日（現地）/ 2026年7月24日 JST",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

> 備考：この1ブロックで「新規osintオブジェクトの先頭追加」と「旧最新エントリ（7/24付）のisLatestをfalseへ変更」の両方を同時に行っています。既存オブジェクトのフィールド構成（cardBg等）をそのまま複製して新規オブジェクトを作成しています。

---

## [S11] 更新ログ（2ブロック構成・必須）

### ブロック1：常時表示3件（本日分を先頭に追加、旧3件目は次ブロックで移動）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年7月24日 09:23 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/24 09:23</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行・トランプ大統領はイランへの「大規模攻撃」検討を警告・カザフスタンがドローン攻撃を受けCPCターミナル経由原油輸出を停止・クウェート国境で火災発生（鎮圧）・バーレーンも再攻撃・ルビオ国務長官「複数国がホルムズ護衛に関心」も法的障壁で未実現・Windward報告：南側迂回ルートでタンカー3隻被弾・通航は北側ルートに集中・原油はブレント7/23終値100.65ドル（前日比+7.00%・5月22日以来の高値）・日本関係船は残り4隻で変化なし・封鎖147日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月22日 09:15 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/22 09:15</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン革命防衛隊、ホルムズ海峡南側迂回ルートでタンカー2隻が爆発・炎上したと発表・UKMTOも別のタンカー損傷を報告——米軍は対イラン10夜連続空爆を継続・Axios報道：トランプ大統領は仲介国提示の「10日間停戦」受諾か大規模軍事作戦かの二択に直面——数日内に方針決定へ・イラン高官はロイターに停戦案受領を認める・フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線・ヘグセス国防長官、戦費を約375億ドルと試算・原油はブレント7/21終値91.10ドル（前日比+2.11%）・日本関係船は残り4隻で変化なし・封鎖145日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/19 10:17</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省「米イラン停戦覚書は危機段階に入った」と表明・トランプ「停戦は終わった」と言及・米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊・イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃・ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者）・クウェート石油公社施設に甚大な被害・イラン側発表で直近の米空爆により46名死亡400名超負傷・ホルムズ通航量は7/16に8隻のみで3週間ぶり最低水準・原油はブレント7/17終値88.09ドル（週間+14%超）・日本関係船は残り4隻で変化なし・封鎖142日目・ニュース3件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年7月26日 10:30 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/26 10:30</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態・オマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展（オマーン外交団7/24テヘラン訪問）・IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表・フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明・原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）・米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇・日本関係船は残り4隻で変化なし・封鎖149日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月24日 09:23 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/24 09:23</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行・トランプ大統領はイランへの「大規模攻撃」検討を警告・カザフスタンがドローン攻撃を受けCPCターミナル経由原油輸出を停止・クウェート国境で火災発生（鎮圧）・バーレーンも再攻撃・ルビオ国務長官「複数国がホルムズ護衛に関心」も法的障壁で未実現・Windward報告：南側迂回ルートでタンカー3隻被弾・通航は北側ルートに集中・原油はブレント7/23終値100.65ドル（前日比+7.00%・5月22日以来の高値）・日本関係船は残り4隻で変化なし・封鎖147日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月22日 09:15 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/22 09:15</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン革命防衛隊、ホルムズ海峡南側迂回ルートでタンカー2隻が爆発・炎上したと発表・UKMTOも別のタンカー損傷を報告——米軍は対イラン10夜連続空爆を継続・Axios報道：トランプ大統領は仲介国提示の「10日間停戦」受諾か大規模軍事作戦かの二択に直面——数日内に方針決定へ・イラン高官はロイターに停戦案受領を認める・フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線・ヘグセス国防長官、戦費を約375億ドルと試算・原油はブレント7/21終値91.10ドル（前日比+2.11%）・日本関係船は残り4隻で変化なし・封鎖145日目・ニュース3件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse 先頭に旧3件目（7/19）を挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/19 10:17</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省「米イラン停戦覚書は危機段階に入った」と表明・トランプ「停戦は終わった」と言及・米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊・イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃・ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者）・クウェート石油公社施設に甚大な被害・イラン側発表で直近の米空爆により46名死亡400名超負傷・ホルムズ通航量は7/16に8隻のみで3週間ぶり最低水準・原油はブレント7/17終値88.09ドル（週間+14%超）・日本関係船は残り4隻で変化なし・封鎖142日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：合計11件超過分（最古の7/11 08:38エントリー）を削除

> 現在の常時表示3件＋log-collapse内エントリーの合計は、本日分追加後11件になるため、log-collapse内の最古エントリー（2026/07/11 08:38）を削除し、`docs/data/update_log.json` の先頭に追加してください。

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月11日 08:38 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/11 08:38</span> — <strong style="color:#fca5a5;">【重大更新】</strong>金子国交相、日本関係船22隻（大型原油タンカー6隻含む）の通過を発表——残り4隻に大幅減（開戦時45隻から・7/10会見）・米当局者、イランに攻撃停止・全通航路開放の公式声明を要求——通航料も不可（Reuters）・イラン、攻撃は「制度の一部の暴走」と釈明し対話継続を希望・アラグチー外相は本日オマーンでブーサイーディー外相と海峡管理を協議・トルコ外相フィダン氏「今週末にも解決の可能性」・イラン国連大使は「海峡管理は専らイランに属する」と対立姿勢維持・原油はブレント$76台で高止まり（週間+5〜6%）・南ルートは大型船AIS通航が7/7以降ゼロで事実上停止・バンダルアッバスの漁船30隻超が空爆で損壊・封鎖134日目・ニュース3件更新・osint更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

**update_log.json への追加（配列先頭）：**

```json
{"date":"2026/07/11 08:38","text":"【重大更新】金子国交相、日本関係船22隻（大型原油タンカー6隻含む）の通過を発表——残り4隻に大幅減（開戦時45隻から・7/10会見）・米当局者、イランに攻撃停止・全通航路開放の公式声明を要求——通航料も不可（Reuters）・イラン、攻撃は「制度の一部の暴走」と釈明し対話継続を希望・アラグチー外相は本日オマーンでブーサイーディー外相と海峡管理を協議・トルコ外相フィダン氏「今週末にも解決の可能性」・イラン国連大使は「海峡管理は専らイランに属する」と対立姿勢維持・原油はブレント$76台で高止まり（週間+5〜6%）・南ルートは大型船AIS通航が7/7以降ゼロで事実上停止・バンダルアッバスの漁船30隻超が空爆で損壊・封鎖134日目・ニュース3件更新・osint更新"}
```

---

## [SHIP_CONFIG] dateConfirmed 更新（変化なし）

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年7月24日 09:23 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。フーシ派がサウジアラビアの原油タンカー2隻を紅海で攻撃し海上封鎖宣言を実行、トランプ大統領はイランへの「大規模攻撃」検討を警告）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年7月26日 10:30 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。米軍は13夜ぶりに対イラン空爆を停止し、オマーン・イランはホルムズ海峡再開協議で進展を見せる一方、IRGCは南ルート不正通航船に警告射撃を実施）'
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [JSON-LD] dateModified 更新（毎回必須）

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-24T09:23:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-26T10:30:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [archive_timeline.json] 本日分エントリー追加

> Claude Codeへの指示：`docs/data/archive_timeline.json` はAPPLYブロック形式を使わず、以下の手順で直接編集してください。
> 1. `entries` 配列の最後の要素（date: "2026-07-24" のオブジェクト）を確認する。
> 2. その要素の閉じ `}` の直後にカンマを追加し、続けて下記のJSONオブジェクトを配列の新しい最後の要素として挿入する。
> 3. 既存のエントリーは一切変更しないこと。

**追加するエントリー：**

```json
{
  "date": "2026-07-26",
  "dateLabel": "2026/07/26 10:30",
  "blockadeDay": 149,
  "summary": "米軍、13夜連続の対イラン空爆後7/25未明に初めて停止——一時的な小康状態・オマーンとイランがホルムズ海峡再開・両国領海管理を巡る協議で進展（オマーン外交団7/24テヘラン訪問）・IRGC、南側迂回ルートの不正通航船4隻に警告射撃し進路変更させたと発表・フーシ派、サウジアラムコのジザン・ヤンブー拠点への攻撃を表明・原油はブレント7/24終値98.38ドルまで反落（前日比-2.29%・週間+10%超維持）・米ガソリン価格は週間+11セントの1ガロン4.11ドルへ上昇・日本関係船は残り4隻で変化なし・封鎖149日目・ニュース3件更新・osint更新",
  "relatedNews": [
    {"title": "米、13夜連続の対イラン空爆を停止——開戦後初めての小康状態", "url": "https://www.washingtonpost.com/world/2026/07/25/iran-us-hormuz-strait-war-25-july-2026/db469ab4-880e-11f1-9cec-0fb26676f07e_story.html", "sourceLabel": "Washington Post"},
    {"title": "オマーン・イラン、ホルムズ海峡再開・領海管理を巡る協議で進展", "url": "https://www.cbsnews.com/live-updates/iran-war-us-trump-strait-hormuz-middle-east/", "sourceLabel": "CBS News"},
    {"title": "IRGC、南ルート不正通航船4隻に警告射撃／フーシ派はサウジアラムコ拠点攻撃を表明", "url": "https://www.cbsnews.com/live-updates/iran-war-us-trump-strait-hormuz-middle-east/", "sourceLabel": "CBS News"}
  ]
}
```

---

## ✅ 出力後セルフチェック（再掲・実施結果）

```
[x] S01 ヘッダー ― 2026年7月26日 10:30 JST・封鎖149日目 ✓
[x] S02 TICKER ― 空爆停止・オマーン仲介進展・IRGC警告射撃・フーシ派アラムコ攻撃・原油反落・封鎖149日目 ✓
[x] S03 速報インシデント ― 7/26 10:30付け・4件新規追加 ✓
[x] S04 情勢カード3枚 ― 外交・軍事・船舶市場を7/26版に更新 ✓
[x] S05 COUNTDOWN ― 封鎖149日目・MOU最終期限残21日 ✓
[x] S06 シナリオ確率補足バナー ― A↑・C→・D↓に変更（B→は据え置き）✓
[x] S07 シナリオ4本 ― A/B/C/D本文を空爆停止・オマーン仲介進展・フーシ派紅海攻撃継続で更新 ✓
[x] S08 シナリオフッター ― 次の焦点5点を7/26版に更新 ✓
[x] S09 30秒カラム ― 3行サマリー更新（最後に作成）✓
[x] S10 news_data.json更新メモ ― latest 3件新規・osint 1件・updated日付 ✓
[x] S11 更新ログ ― 2ブロック構成で先頭に7/26 10:30行追記・旧3件目（7/19）をlog-collapseへ移動・7/11 08:38エントリーを削除しupdate_log.jsonへ ✓
[x] SHIP_CONFIG ― C01検証実施・変化なし・dateConfirmedを7/26に更新 ✓
[x] JSON-LD dateModified ― 2026-07-26T10:30:00+09:00に更新 ✓
[x] C01タンカー確認 ― 日本語3クエリ＋英語1クエリを個別実行・変化なし確認 ✓

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記のまま維持 ✓
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：7/26 10:30 JST「更新」に是正（新情報のため）✓
```
