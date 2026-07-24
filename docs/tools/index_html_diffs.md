# index_html_diffs.md — 2026年7月24日 09:23 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> news_data.json の変更は `<!-- FILE:docs/data/news_data.json -->` 指定ブロックを対象ファイルとして適用してください。
> archive_timeline.json の変更は `<!-- FILE:docs/data/archive_timeline.json -->` 指定ブロックを対象ファイルとして適用してください（entries配列末尾に追加・既存エントリーは変更しないこと）。
> 作業完了後に commit してください。push は確認後に指示します。

---

## ⚠️ 未実施項目あり（申告）

- **全ルート現況サマリー（S04カード③下部セクション）が前回7/22更新時に据え置かれ、実際には7/19 10:17 JST時点の内容のまま最新化されていなかったことが判明しました。**（7/22のセルフチェックでは「✓ S04カード③内で7/22 09:15 JST再確認済を明示」と記載されていましたが、live index.htmlを確認したところ該当セクションの日付は「2026年7月19日 10:17 JST 更新」のままでした。）
- 本日分の差分でこのセクションを7/24版に更新し是正します。過去のセルフチェックの記載と実際のファイル状態に乖離があった旨、申告します。このまま本日分の是正を含めて進めてよろしいでしょうか（ユーザー確認を推奨。異論なければそのまま適用してください）。

---

## ⚠️ セルフチェック（本文執筆前の事前貼付・2026/7/9ルール）

本日のセルフチェック項目数：19件（+ 全体系チェック3件 = 計22項目）

```
[✓] S01 ヘッダー ― 2026年7月24日 09:23 JST・封鎖147日目に更新
[✓] S02 TICKER ― 原油100ドル突破・フーシ派サウジタンカー攻撃・トランプ氏大規模攻撃警告・カザフスタンCPC停止・封鎖147日目
[✓] S03 速報インシデント ― 7/24 09:23付け・4件新規追加（原油急騰／フーシ派タンカー攻撃・トランプ警告／カザフスタンCPC停止／ルビオ護衛連合発言）
[✓] S04 情勢カード3枚 ― 外交・軍事・船舶市場を7/24版に更新
[✓] S05 COUNTDOWN ― 封鎖147日目・機雷除去期限(7/17)徒過継続・MOU最終期限残23日
[✓] S06 シナリオ確率補足バナー ― 7/24 09:23 JST日付更新・矢印をA↓B→C↑D↑で維持
[✓] S07 シナリオ4本 ― A/B/C/D本文をフーシ派参戦拡大・原油100ドル突破・トランプ大規模攻撃警告で更新
[✓] S08 シナリオフッター ― 次の焦点5点を7/24版に更新
[✓] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成）
[✓] S10 news_data.json更新メモ ― latest 3件新規・osint 1件・updated日付
[✓] S11 更新ログ ― 2ブロック構成で先頭に7/24 09:23行追記・旧3件目をlog-collapseへ移動・合計11件超過分（7/10エントリー）を削除
[✓] SHIP_CONFIG ― C01検証実施・変化なし・dateConfirmedを7/24に更新
[✓] JSON-LD dateModified ― 2026-07-24T09:23:00+09:00に更新
[✓] C01タンカー確認 ― 日本語3クエリ＋英語1クエリを個別実行・変化なし確認
[✓] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[✓] 全体 ― ニュースURLにAI捏造・推測URLが混入していないか（web検索確認済みURLのみ使用）
[✓] 全体 ― 📰関連最新ニュースにAl Jazeeraが混入していないか（osintのみに配置）
[✓] 全体 ― 人名が日本語表記になっているか（トランプ・ヘグセス・ルビオ・イラン外務省等）
[✓] 全体 ― diffs.md本文執筆の前にproject_knowledge_searchでセルフチェック原文を取得したか

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記のまま維持 ✓（変更不要）
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：上記「未実施項目あり」参照——本日分で7/24 09:23 JSTに是正 ✓
```

---

## C01 タンカー確認（必須・毎回実施）

- 日本語クエリ①「日本関係船舶 ホルムズ海峡 通過 足止め 7月24日」／②「外務省 ホルムズ海峡 日本関係船舶 7月23日 発表」／③「金子国土交通大臣 記者会見 ホルムズ海峡 日本関係船舶 隻 7月」を個別実行
- 英語クエリ「Japanese ships Strait of Hormuz stranded detained July 2026」を実行
- 結果：金子国交相の新規会見・外務省新規発表は確認されず。直近の確定情報は7/10会見の「残り4隻」のまま変化なし（7/22確認時点から変化なし）
- 判定：**変化なし** → SHIP_CONFIG の totalShips・passableShips は据え置き、dateConfirmed のみ本日日時＋「変化なし」で更新

---

## 本日の主要トピック（背景メモ）

- フーシ派がサウジアラビアの原油タンカー2隻を紅海で攻撃（新たな封鎖宣言の実行）。トランプ大統領はイランに「紅海での責任」を警告し、「大規模攻撃を検討中」と発言（7/23）
- カザフスタンがドローン攻撃を受け、CPC（カスピ海パイプラインコンソーシアム）ターミナル経由の原油輸出を停止（7/23）——ホルムズ以外の供給網にも波及
- 原油急騰：ブレント7/23終値100.65ドル（前日比+7.00%）——5月22日以来の高値。WTIも90ドル台に上昇
- クウェート国境沿いAl-Abdaliでイラン攻撃による火災（鎮火）、バーレーンも再び攻撃を受ける（Al Jazeera 7/23）
- ルビオ国務長官：複数国がホルムズ海峡での商船護衛参加に関心を示すも法的・政治的障壁で正式合意には未達（7/22）
- Windward海事インテリジェンス：南側迂回ルート（クムザール・リマ沖）でタンカー3隻が被弾、通航はほぼ北側ルートに集中（直近24時間）
- 日本関係船舶：C01実施の結果、変化なし（残り4隻を維持）

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（ホルムズ海峡でタンカー2隻が爆発・炎上——IRGCは南側迂回ルート航行中と発表・UKMTOも別途正体不明飛翔体によるタンカー損傷を報告／米軍は対イラン10夜連続空爆を継続／トランプ大統領、仲介国提示の「10日間停戦」受け入れか大規模軍事作戦かの二択に直面——数日内に方針決定へ（Axios報道）／フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線／原油はブレント7/21終値91.10ドルまで急伸（前日比+2.11%）／封鎖145日目）</span>
    <span class="badge-item badge-date">📅2026年7月22日 09:15 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——トランプ大統領はイランへの「大規模攻撃」検討を警告／カザフスタンがドローン攻撃を受けCPCターミナル経由の原油輸出を停止／クウェート国境沿いで火災・バーレーンも再攻撃を受ける／原油はブレント7/23終値100.65ドルまで急伸（前日比+7.00%・5月22日以来の高値）／ルビオ国務長官「複数国がホルムズ護衛参加に関心」も法的障壁で未実現／封鎖147日目）</span>
    <span class="badge-item badge-date">📅2026年7月24日 09:23 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月22日 09:15 JST） -->
      🚨【ホルムズでタンカー2隻炎上】IRGC発表：南側迂回ルート航行中のタンカー2隻が爆発・炎上——UKMTOも別途正体不明飛翔体による損傷を報告（7/21未明 JST）｜💥 米軍、対イラン10夜連続空爆——ゲシュム島・バンダルアッバース等で爆発（7/21 JST）｜🕊️ トランプ氏、仲介国（カタール・パキスタン等）提示の「10日間停戦」受け入れか大規模軍事作戦かの二択に直面——数日内に方針決定へ（Axios・7/21）｜⚓ フーシ派、サウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新たな脅威（7/20）｜🛢️ 原油急伸——ブレント7/21終値91.10ドル（前日比+2.11%）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残25日｜封鎖145日目
    </span>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月24日 09:23 JST） -->
      🚨【原油100ドル突破】ブレント7/23終値100.65ドル（前日比+7.00%）——5月22日以来の高値（7/24 JST）｜⚓ フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——トランプ氏「大規模攻撃を検討中」とイランへ責任転嫁を警告（7/23）｜🛢️ カザフスタン、ドローン攻撃を受けCPCターミナル経由の原油輸出を停止（7/23）｜🔥 クウェート国境Al-Abdali沿いで火災発生・バーレーンも再攻撃を受ける（7/23）｜🕊️ ルビオ国務長官「複数国がホルムズ護衛参加に関心」——法的・政治的障壁で正式化せず（7/22）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残23日｜封鎖147日目
    </span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

### トグルボタン内タイトル・日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">ホルムズ海峡でタンカー2隻炎上／米、10夜連続空爆／トランプ氏「10日間停戦か大規模作戦か」の二択に直面／フーシ派、サウジへ海上封鎖宣言</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/22 09:15 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">原油100ドル突破／フーシ派、サウジタンカー攻撃——トランプ氏「大規模攻撃」検討／カザフスタンCPC原油輸出停止</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/24 09:23 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/22 09:15 速報】イラン革命防衛隊（IRGC）、南側迂回ルートを航行中のタンカー2隻が爆発・炎上したと発表——「米軍の誤誘導」と主張。UKMTOは別途、オマーン沖でタンカー1隻が正体不明の飛翔体により損傷し乗員が退避したと報告（同一事案か未確認）｜米軍は7/21未明に対イラン10夜連続空爆を実施——ゲシュム島・バンダルアッバース・バンダルレンゲ等で爆発｜Axios報道：トランプ大統領は仲介国（カタール・パキスタン等）提示の「10日間停戦」受け入れか、イスラエルと共同での大規模軍事作戦かの二択に直面——数日内に方針決定の見通し｜イラン高官はロイターに10日間停戦案の受領を認め、外務省も複数提案受領を確認｜フーシ派がサウジアラビアへ海上封鎖を宣言（7/20）——バブ・エル・マンデブ海峡経由の迂回ルートにも新戦線、サウジは「断固たる対抗措置」を表明｜ヘグセス国防長官、対イラン戦費を約375億ドルと試算（7/21議会証言）｜原油はブレント7/21終値91.10ドルまで急伸（前日比+2.11%）｜日本関係船は残り4隻で変化なし｜封鎖145日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/24 09:23 速報】イエメンの親イラン武装組織フーシ派が、サウジアラビアの原油タンカー2隻を紅海で攻撃（7/23）——先に宣言していたサウジ海上封鎖の実行と見られる｜トランプ大統領は、イランを紅海での攻撃の責任者とみなすと警告し、「大規模攻撃を検討中」と発言｜カザフスタンがドローン攻撃を受け、CPC（カスピ海パイプラインコンソーシアム）ターミナル経由の原油輸出を停止（7/23）——ホルムズ以外の供給網にも混乱が波及｜クウェート国境沿いAl-Abdaliでイラン攻撃による火災が発生し鎮圧、バーレーンも再び攻撃を受けたとAl Jazeeraが報告｜ルビオ国務長官は、複数国がホルムズ海峡での商船護衛参加に関心を示していると明らかにしたが、法的・政治的障壁で正式合意には至っていないと説明（7/22）｜Windward海事インテリジェンスによれば、直近24時間で南側迂回ルート（クムザール・リマ沖）のタンカー3隻が被弾し、通航はほぼ北側ルートに集中｜原油はブレント7/23終値100.65ドルまで急伸（前日比+7.00%・5月22日以来の高値）｜日本関係船は残り4隻で変化なし｜封鎖147日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に4件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🚢 7/21 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fca5a5;font-weight:700;">⚓ 7/23 JST</span>
  <span style="color:#e2e8f0;"> イエメンの親イラン武装組織フーシ派は、サウジアラビアの原油タンカー2隻を紅海で攻撃したと表明——7/20に宣言していたサウジへの海上封鎖の実行と見られる。米国側は、イランがこの攻撃に責任を負うとみなす立場を示し、トランプ大統領は「大規模攻撃を検討中」と発言した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🛢️ 7/23 JST</span>
  <span style="color:#e2e8f0;"> カザフスタンは、ドローン攻撃を受けCPC（カスピ海パイプラインコンソーシアム）ターミナル経由の原油輸出を停止したと発表。ホルムズ海峡以外の輸出ルートにも供給不安が波及し、原油価格の押し上げ要因となった。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🔥 7/23 JST</span>
  <span style="color:#e2e8f0;"> クウェート国境沿いAl-Abdali付近でイランの攻撃による火災が発生し、クウェート当局が鎮圧したと発表。バーレーンも同日、再び攻撃を受けたとAl Jazeeraが報告した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🕊️ 7/22 JST</span>
  <span style="color:#e2e8f0;"> ルビオ国務長官は記者団に対し、複数国がホルムズ海峡での商船護衛への参加に関心を示していると明らかにした一方、法的・政治的な障壁により正式な合意には至っていないと説明した。同長官は、ホルムズ海峡は国際水域であり全船舶の自由な通航が確保されるべきだと改めて強調した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🚢 7/21 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

### カード① 外交交渉

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">💰 外交：仲介国「10日間停戦」提案——トランプ氏、受諾か大規模軍事作戦かの二択に直面</div>
        <div class="s-body">Axiosによれば、米・イスラエル当局者はトランプ大統領がホルムズ海峡再開を目指す仲介国（カタール・パキスタン等）提示の10日間停戦の実施か、イスラエルと共同での大規模軍事作戦の実施かという二択に直面していると報道。イラン政府高官はロイターに停戦案受領を認め、外務省も複数提案受領を確認したが条件は非公表。ヨルダン基地攻撃での米兵死亡への報復として、米国はまず数日間攻撃を継続した後に停戦案を検討するとの見方も一部で示されている。現時点で最終決定はなされていない。</div>
        <div class="s-src">出典: Axios（テレビ朝日系ANN報道）/ ロイター（産経新聞・ブルームバーグ経由）（7/20〜21 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">💰 外交：フーシ派参戦でトランプ氏「大規模攻撃」検討——ルビオ氏「護衛連合に複数国関心」も未実現</div>
        <div class="s-body">フーシ派がサウジアラビアの原油タンカー2隻を紅海で攻撃したことを受け、トランプ大統領はイランに責任があるとの立場を示し、「大規模攻撃を検討中」と発言。10日間停戦案の受諾か大規模軍事作戦かという二択は、フーシ派参戦によりさらに緊迫化した。一方、ルビオ国務長官は複数国がホルムズ海峡での商船護衛への参加に関心を示していると明らかにしたが、法的・政治的障壁により正式な合意・実施には至っていない。外交的収拾と軍事エスカレーションの綱引きが続く。</div>
        <div class="s-src">出典: Al Jazeera / Trading Economics / Barchart（7/22〜23 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 軍事情勢

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">⚔️ 軍事：米、対イラン10夜連続空爆——ホルムズ海峡でタンカー2隻炎上／フーシ派がサウジへ海上封鎖宣言</div>
        <div class="s-body">CENTCOMは7/21未明、対イラン10夜連続となる空爆を実施し、ゲシュム島・バンダルアッバース・バンダルレンゲ等で爆発が確認された。イラン革命防衛隊（IRGC）は同日、南側迂回ルートを航行しようとしたタンカー2隻が爆発・炎上し航行不能になったと発表——「米軍の誤誘導」と主張。UKMTOも別途、オマーン沖で正体不明の飛翔体によるタンカー損傷・乗員退避を報告した（同一事案か未確認）。並行して、イエメンの親イラン武装組織フーシ派がサウジアラビアへの海上封鎖を宣言し、バブ・エル・マンデブ海峡経由の迂回ルートにも新たな脅威が生じている。ヘグセス国防長官は対イラン戦費を約375億ドルと試算した。</div>
        <div class="s-src">出典: CENTCOM / Al Jazeera / AFPBB News / ロイター（7/20〜21 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">⚔️ 軍事：フーシ派がサウジタンカー2隻を攻撃・戦線が紅海へ拡大／クウェート・バーレーンも再攻撃</div>
        <div class="s-body">イエメンの親イラン武装組織フーシ派は7/23、サウジアラビアの原油タンカー2隻を紅海で攻撃したと発表——7/20宣言のサウジ海上封鎖の実行とみられる。クウェート国境沿いAl-Abdali付近ではイラン攻撃による火災が発生（鎮圧済み）、バーレーンも再び攻撃を受けたとAl Jazeeraが報告。Windward海事インテリジェンスによれば、直近24時間でホルムズ海峡南側迂回ルート（クムザール・リマ沖）のタンカー3隻が被弾し、通航はほぼ北側ルートに集中している。一方、Bloombergによれば商船三井系を含むVLCC3隻がリスクを冒してホルムズ海峡経由でペルシャ湾を脱出した。</div>
        <div class="s-src">出典: Al Jazeera / Windward / Bloomberg（7/23 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ エネルギー・市場

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/22再確認）——ホルムズ通航量は週次66%減／原油91ドル台</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/22 09:15 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。Lloyd's List Intelligenceによれば、7/20までの週のホルムズ海峡通航量は53隻で前週比66%減。CNBCはさらに、7/17〜19の3日間ではわずか40隻（1日平均13隻）にとどまったと報じた。原油はブレント先物が7/21終値で91.10ドル（前日比+2.11%・一時91.57ドル）に達し、フーシ派のサウジ海上封鎖宣言も価格を押し上げている。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残25日に迫っている。</div>
        <div class="s-src">出典: CNBC / Lloyd's List / TradingEconomics（7/21 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/24再確認）——原油はブレント100ドル突破／カザフスタンCPC停止</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/24 09:23 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。原油はブレント先物が7/23終値で100.65ドル（前日比+7.00%・一時101ドル超）に達し、5月22日以来の高値を記録。フーシ派のサウジタンカー攻撃に加え、カザフスタンがドローン攻撃を受けCPC（カスピ海パイプラインコンソーシアム）ターミナル経由の原油輸出を停止したことも供給不安を増幅させた。WTIも90ドル台に上昇。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残23日に迫っている。</div>
        <div class="s-src">出典: Trading Economics / Barchart / Forbes Advisor（7/23 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 11「ホルムズでタンカー2隻炎上・フーシ派サウジ海上封鎖宣言——トランプ氏10日間停戦か大規模作戦かの二択に直面」——封鎖145日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 12「フーシ派、サウジタンカー攻撃を実行——トランプ氏『大規模攻撃』検討・原油100ドル突破」——封鎖147日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🚨 <strong>ホルムズ海峡でタンカー2隻炎上・UKMTOも別途タンカー損傷を報告／米軍は対イラン10夜連続空爆継続／トランプ氏、仲介国提示の「10日間停戦」受け入れか大規模軍事作戦かの二択に直面——数日内に方針決定へ／フーシ派がサウジアラビアへ海上封鎖を宣言——紅海迂回ルートにも新戦線／日本関係船は残り4隻で変化なし——封鎖145日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残25日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米国の最終方針決定（10日間停戦受諾か大規模軍事作戦か） ②タンカー炎上・UKMTO損傷事案の被害詳細確認 ③フーシ派海上封鎖の実効性・紅海迂回ルートへの影響 ④MOU正式破棄・全面戦争再開の有無 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残25日（8/16）</span>
<!-- OLD:END -->
<!-- NEW:START -->
        🚨 <strong>フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行／トランプ大統領、イランへの「大規模攻撃」検討を警告／カザフスタンがドローン攻撃受けCPCターミナル経由原油輸出を停止／クウェート国境で火災・バーレーンも再攻撃／原油はブレント100ドル突破（7/23終値100.65ドル・+7.00%）——日本関係船は残り4隻で変化なし——封鎖147日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残23日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①トランプ氏の「大規模攻撃」実施判断 ②フーシ派参戦の紅海・バブエルマンデブ海峡への影響拡大 ③ホルムズ南側迂回ルートのタンカー被弾続発（Windward報告） ④ルビオ氏言及の護衛連合構想の実現可否 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残23日（8/16）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## 全ルート現況サマリー（是正・S04直後）

> ⚠️ 前回（7/22）更新時に据え置かれていたことが判明したため、本日分で7/19時点の内容から7/24版へ更新します。

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月19日 10:17 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンとの実務協議は「危機段階」入りが公式に表明され事実上停止。10,000dwt超の大型船AIS通航実績は依然乏しい。【北ルート（Iran coastline / IRGC管理）】対イラン海上封鎖は継続中。CENTCOMは7夜連続で対イラン空爆を実施しバンダルハミール橋梁・チャバハール港監視塔を破壊——南北両ルートとも運用停止に近い状態が継続。ホルムズ通航量は7/16(木)に8隻まで落ち込み3週間ぶり最低水準（MarineTraffic）。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限は7/17（MOU第5条）を未着手のまま徒過。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃を実施し、クウェート石油公社施設が甚大な被害を受けた。🇯🇵 日本関係船舶：残り4隻で変化なし（7/19 10:17 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月24日 09:23 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】Windward海事インテリジェンスによれば、直近24時間で南側迂回ルート（クムザール・リマ沖）のタンカー3隻が被弾し、以降の通航12件のうち南ルート使用は2件のみと事実上機能不全。【北ルート（Iran coastline / IRGC管理）】対イラン海上封鎖は継続中。通航はほぼ北側ルートに集中しているが、依然として低水準。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限は7/17（MOU第5条）を未着手のまま徒過。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。フーシ派がサウジアラビアの原油タンカー2隻を紅海で攻撃し、バブ・エル・マンデブ海峡経由の迂回ルートにも新たな脅威。Bloombergによれば直近24時間でVLCC3隻がリスクを冒してホルムズ海峡を脱出。🇯🇵 日本関係船舶：残り4隻で変化なし（7/24 09:23 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年7月22日 09:15 JST 更新</span><br>
  📊 <strong>ホルムズ海峡でタンカー2隻炎上・フーシ派がサウジへ海上封鎖宣言——一方でトランプ氏は仲介国提示の「10日間停戦」受諾か大規模軍事作戦かの二択に直面：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — 軍事的実害は継続も、初めて具体的な10日間停戦案が外交テーブルに乗った<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — 停戦案が実現すれば一時的な膠着再現の可能性がある一方、フーシ派参戦で不確実性も増大<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — タンカー炎上・フーシ派のサウジ海上封鎖宣言で、封鎖の実害が地域全体に拡散<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — フーシ派の参戦により戦線がイエメン・紅海方面へも拡大、戦費は約375億ドルに達した<br>
  <strong style="color:#f87171;">「10日間停戦か大規模軍事作戦か」という具体的な分岐点が初めて明示された一方、タンカー炎上・フーシ派参戦など軍事的実害は同時進行しており、二択の帰趨次第で急速にC/Dへ振れるリスクも残る（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月22日 09:15 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
  <div class="sc-grid" style="grid-template-columns:repeat(2,1fr);">

    <!-- シナリオ A：外交解決 -->
    <div class="sc-card sc-best">
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>仲介国（カタール・パキスタン等）が「10日間停戦」を提示し、イラン高官・外務省双方がこれを認めるなど、初めて具体的な収拾ルートが外交テーブルに乗った。ただしAxiosによれば米・イスラエル当局者はトランプ大統領がこの停戦案受諾かイスラエルと共同での大規模軍事作戦かの「二択」に直面していると認めており、最終決定は依然として不透明。同時にホルムズ海峡ではタンカー2隻が炎上するなど軍事的実害も継続しており、段階的なMOU履行という枠組みの再構築にはなお高いハードルが残る。</p>
      </div>
    </div>

    <!-- シナリオ B：部分的封鎖継続（膠着） -->
    <div class="sc-card sc-mid">
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>10日間停戦案が実際に発効すれば、当面は「戦闘一時停止・海峡通航は限定的」という膠着状態が再現される可能性がある。一方でイランはヨルダン・クウェート等5カ国への報復攻撃を続け、フーシ派も新たにサウジアラビアへの海上封鎖を宣言するなど、単純な現状維持を超えた多方面での緊張激化が同時進行している。停戦案の受諾如何が今後数日のシナリオ分岐を左右する。</p>
      </div>
    </div>

    <!-- シナリオ C：完全封鎖の制度化・経済疲弊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>ホルムズ海峡ではタンカー2隻が炎上・航行不能となり、UKMTOも別途タンカー損傷を報告するなど、南側迂回ルートを含めた事実上の航行不能状態が続いている。フーシ派によるサウジ海上封鎖宣言は、ホルムズの代替輸出ルートである紅海側にも新たな制約をもたらし、「完全封鎖の制度化」がホルムズ単独ではなく地域全体に広がりつつある構図を強めている。</p>
      </div>
    </div>

    <!-- シナリオ D：軍事エスカレーション・停戦崩壊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>米軍は対イラン10夜連続空爆を継続し、フーシ派の参戦（サウジ海上封鎖宣言）により戦線がイエメン・紅海方面へも拡大した。ヘグセス国防長官は戦費が約375億ドルに達したと議会証言し、長期化する軍事作戦の規模が改めて可視化された。シナリオCとの差：C=「封鎖・通航管理を巡る制度的対立」、D=「多国間・多正面にわたる実力による現状変更」。トランプ大統領が大規模軍事作戦を選択した場合、イスラエルとの共同作戦を含む本格的なエスカレーションへ移行するリスクが最も高い局面にある。</p>
      </div>
    </div>

  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
  <div class="sc-grid" style="grid-template-columns:repeat(2,1fr);">

    <!-- シナリオ A：外交解決 -->
    <div class="sc-card sc-best">
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>ルビオ国務長官は複数国がホルムズ海峡での商船護衛への参加に関心を示していると明らかにしたが、法的・政治的障壁により正式な合意には至っていない。フーシ派がサウジタンカー攻撃を実行に移し、トランプ大統領が「大規模攻撃」検討を表明するなど、外交解決に向けた機運は7/22時点よりもさらに後退している。10日間停戦案は依然テーブルには残るが、実現の見通しは不透明さを増している。</p>
      </div>
    </div>

    <!-- シナリオ B：部分的封鎖継続（膠着） -->
    <div class="sc-card sc-mid">
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>カザフスタンのCPCターミナル停止は、供給混乱がホルムズ以外にも広がっていることを示しており、単純な現状維持を前提としたシナリオBの想定を超えつつある。クウェート・バーレーンへの攻撃も継続しており、地域全体の緊張が「膠着」という言葉では表現しきれない段階に入っている。</p>
      </div>
    </div>

    <!-- シナリオ C：完全封鎖の制度化・経済疲弊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>Windward海事インテリジェンスによれば、南側迂回ルート（クムザール・リマ沖）でタンカー3隻が被弾し、通航はほぼ北側ルートに集中している。フーシ派によるサウジタンカー攻撃の実行は、ホルムズの代替輸出ルートである紅海側の封鎖をさらに現実のものとし、「完全封鎖の制度化」がホルムズ単独ではなく地域全体に及ぶ構図を一段と強めている。</p>
      </div>
    </div>

    <!-- シナリオ D：軍事エスカレーション・停戦崩壊 -->
    <div class="sc-card sc-worst">
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>トランプ大統領は、フーシ派のサウジタンカー攻撃を受けイランに責任があるとの立場を示し、「大規模攻撃を検討中」と発言した。フーシ派の参戦（サウジタンカー攻撃実行）により戦線はイエメン・紅海方面へすでに拡大しており、シナリオCとの差はさらに縮小している。シナリオCとの差：C=「封鎖・通航管理を巡る制度的対立」、D=「多国間・多正面にわたる実力による現状変更」。トランプ氏が「大規模攻撃」を実行に移した場合、イスラエルとの共同作戦を含む本格的なエスカレーションへ移行するリスクが最も高い局面にある。</p>
      </div>
    </div>

  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター

<!-- APPLY:START -->
<!-- OLD:START -->
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米国の最終方針決定（10日間停戦受諾か大規模軍事作戦か）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">タンカー炎上・UKMTO損傷事案の被害詳細確認</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">フーシ派海上封鎖の実効性・紅海迂回ルートへの影響</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">MOU正式破棄・全面戦争再開の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月22日 09:15 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">トランプ氏の「大規模攻撃」実施判断の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">フーシ派参戦の紅海・バブエルマンデブ海峡への影響拡大</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">ホルムズ南側迂回ルートのタンカー被弾続発（Windward報告）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">ルビオ氏言及の護衛連合構想の実現可否</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月24日 09:23 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（最後に作成）

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
🗣️ ホルムズ海峡でタンカー2隻炎上・トランプ氏「10日間停戦か大規模作戦か」の二択に直面——数日内に決定へ。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷 フーシ派がサウジアラビアへ海上封鎖を宣言し紅海側にも新戦線——日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 米国の最終方針決定・タンカー炎上の被害確認が焦点、封鎖145日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残25日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ5枚

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💥タンカー2隻炎上・米10夜連続空爆</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️トランプ氏「10日間停戦か大規模作戦か」の二択</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚓フーシ派、サウジへ海上封鎖宣言</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント91ドル台・+2.11%</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚓フーシ派、サウジタンカー攻撃を実行</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️トランプ氏「大規模攻撃」検討を警告</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️カザフスタンCPC原油輸出停止</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント100ドル突破・+7.00%</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## SHIP_CONFIG（C01検証済み・変化なし）

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年7月22日 09:15 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。ホルムズ海峡でタンカー2隻炎上・フーシ派がサウジへ海上封鎖宣言する中、トランプ氏は10日間停戦か大規模軍事作戦かの二択に直面）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年7月24日 09:23 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。フーシ派がサウジアラビアの原油タンカー2隻を紅海で攻撃し海上封鎖宣言を実行、トランプ大統領はイランへの「大規模攻撃」検討を警告）'
<!-- NEW:END -->
<!-- APPLY:END -->

---

## JSON-LD dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-22T09:15:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-24T09:23:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S11] 更新ログ（2ブロック構成・必須）

### ブロック1：常時表示3件の更新

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年7月22日 09:15 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/22 09:15</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン革命防衛隊、ホルムズ海峡南側迂回ルートでタンカー2隻が爆発・炎上したと発表・UKMTOも別のタンカー損傷を報告——米軍は対イラン10夜連続空爆を継続・Axios報道：トランプ大統領は仲介国提示の「10日間停戦」受諾か大規模軍事作戦かの二択に直面——数日内に方針決定へ・イラン高官はロイターに停戦案受領を認める・フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線・ヘグセス国防長官、戦費を約375億ドルと試算・原油はブレント7/21終値91.10ドル（前日比+2.11%）・日本関係船は残り4隻で変化なし・封鎖145日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/19 10:17</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省「米イラン停戦覚書は危機段階に入った」と表明・トランプ「停戦は終わった」と言及・米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊・イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃・ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者）・クウェート石油公社施設に甚大な被害・イラン側発表で直近の米空爆により46名死亡400名超負傷・ホルムズ通航量は7/16に8隻のみで3週間ぶり最低水準・原油はブレント7/17終値88.09ドル（週間+14%超）・日本関係船は残り4隻で変化なし・封鎖142日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/16 10:52</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明・対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を攻撃・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更・IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明・トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も・米はIRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放・日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明・原油はブレント7/15終値84.95ドル・封鎖139日目・ニュース3件更新・osint更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年7月24日 09:23 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/24 09:23</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行・トランプ大統領はイランへの「大規模攻撃」検討を警告・カザフスタンがドローン攻撃を受けCPCターミナル経由原油輸出を停止・クウェート国境で火災発生（鎮圧）・バーレーンも再攻撃・ルビオ国務長官「複数国がホルムズ護衛に関心」も法的障壁で未実現・Windward報告：南側迂回ルートでタンカー3隻被弾・通航は北側ルートに集中・原油はブレント7/23終値100.65ドル（前日比+7.00%・5月22日以来の高値）・日本関係船は残り4隻で変化なし・封鎖147日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月22日 09:15 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/22 09:15</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン革命防衛隊、ホルムズ海峡南側迂回ルートでタンカー2隻が爆発・炎上したと発表・UKMTOも別のタンカー損傷を報告——米軍は対イラン10夜連続空爆を継続・Axios報道：トランプ大統領は仲介国提示の「10日間停戦」受諾か大規模軍事作戦かの二択に直面——数日内に方針決定へ・イラン高官はロイターに停戦案受領を認める・フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線・ヘグセス国防長官、戦費を約375億ドルと試算・原油はブレント7/21終値91.10ドル（前日比+2.11%）・日本関係船は残り4隻で変化なし・封鎖145日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/19 10:17</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省「米イラン停戦覚書は危機段階に入った」と表明・トランプ「停戦は終わった」と言及・米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊・イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃・ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者）・クウェート石油公社施設に甚大な被害・イラン側発表で直近の米空爆により46名死亡400名超負傷・ホルムズ通航量は7/16に8隻のみで3週間ぶり最低水準・原油はブレント7/17終値88.09ドル（週間+14%超）・日本関係船は残り4隻で変化なし・封鎖142日目・ニュース3件更新・osint更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse先頭への旧3件目（7/16分）挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月14日 18:00 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/16 10:52</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明・対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を攻撃・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更・IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明・トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も・米はIRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放・日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明・原油はブレント7/15終値84.95ドル・封鎖139日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年7月14日 18:00 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：合計11件超過分（7/10エントリー）を削除

> 常時表示3 + log-collapse内は 7/16, 7/14 18:00, 7/14 16:16, 7/14 08:48, 7/13, 7/12, 7/11, 7/10 の8件 → 合計11件で1件超過。最古の7/10エントリーを削除する。

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月10日 07:40 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/10 07:40</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>CENTCOM、南部イラン各地（ブシェール・チャバハール・バンダルアッバス・ジャスク等）で追加空爆（7/8夜）・IRGCがクウェート・バーレーン・カタールの米軍拠点にドローン・ミサイルで報復——停戦後初のカタール標的化（7/9）・クウェート国防省「迎撃したが被害で1名負傷」・ガリバフ国会議長「攻撃すれば反撃を受ける」・バーレーン・クウェート・UAE・ヨルダンが非難・ブシェール州で原因不明の爆発複数・原油一時$79台へ急騰後$77前後に落ち着く・日本関係船18隻で変化なし・封鎖133日目・ニュース3件更新・osint更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

> Claude Code への指示：以下は `docs/data/news_data.json` に対する変更です。既存の `latest` 配列先頭に新規3件を追加し、既存の `isLatest:true` エントリー（id: `latest-hormuz-tankers-fire-0721`）は `isLatest:false` に変更。`latest` の末尾3件（id: `latest-mou-crisis-stage-0719`・`latest-jordan-us-troops-killed-0718`・`latest-kuwait-oil-facility-attack-0718`）は `archive` 配列の先頭に新規バッチ「2026年7月24日 更新分（アーカイブ）」として移動してください。

<!-- FILE:docs/data/news_data.json -->

### updated / staleNotice フィールド

```json
"updated": "2026年7月24日 09:23 日本時間JST",
"staleNotice": ""
```

### latest 配列 先頭に追加する新規3件

```json
{
  "id": "latest-houthi-saudi-tanker-attack-0723",
  "title": "フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——トランプ氏「大規模攻撃」検討を警告",
  "body": "イエメンの親イラン武装組織フーシ派は、サウジアラビアの原油タンカー2隻を紅海で攻撃したと発表した。7月20日に宣言していたサウジへの海上封鎖の実行とみられる。米国側はイランがこの攻撃に責任を負うとの立場を示し、トランプ大統領は「大規模攻撃を検討中」と発言した。ホルムズ海峡に加え紅海側でも輸送リスクが顕在化している。",
  "sourceLabel": "Trading Economics / Barchart",
  "date": "2026年7月23日（現地）/ 2026年7月24日 JST",
  "label": "⚓ 海上輸送",
  "url": "https://www.barchart.com/futures/quotes/CBN26",
  "isLatest": true
},
{
  "id": "latest-brent-100-kazakhstan-cpc-0723",
  "title": "原油ブレント100ドル突破——カザフスタンもドローン攻撃受けCPCターミナル原油輸出停止",
  "body": "ブレント原油先物は7月23日終値で100.65ドル（前日比+7.00%）に達し、5月22日以来の高値を記録した。フーシ派によるサウジタンカー攻撃に加え、カザフスタンがドローン攻撃を受けCPC（カスピ海パイプラインコンソーシアム）ターミナル経由の原油輸出を停止したことも供給不安を増幅させた。WTIも90ドル台に上昇している。",
  "sourceLabel": "Trading Economics",
  "date": "2026年7月23日（現地）/ 2026年7月24日 JST",
  "label": "🛢️ 原油市場",
  "url": "https://tradingeconomics.com/commodity/brent-crude-oil",
  "isLatest": false
},
{
  "id": "latest-rubio-escort-coalition-0722",
  "title": "ルビオ国務長官「複数国がホルムズ護衛参加に関心」——法的障壁で正式化せず",
  "body": "ルビオ国務長官は記者団に対し、複数国がホルムズ海峡での商船護衛への参加に関心を示していると明らかにした一方、法的・政治的な障壁により正式な合意には至っていないと説明した。同長官はホルムズ海峡が国際水域であり、全ての商船に対して通行料や制約のない自由な航行が確保されるべきだと改めて強調した。",
  "sourceLabel": "Fox News Digital",
  "date": "2026年7月22日（現地）/ 2026年7月23日 JST",
  "label": "🕊️ 外交",
  "url": "https://www.foxnews.com/live-news/iran-war-trump-strait-of-hormuz-oil-07-22-26",
  "isLatest": false
}
```

### archive 配列 先頭に追加する新規バッチ

> 以下3件は既存ファイルの現行 `latest-mou-crisis-stage-0719`・`latest-jordan-us-troops-killed-0718`・`latest-kuwait-oil-facility-attack-0718` の内容をそのまま転記してください（本文は変更しないこと・既存ファイルを参照して正確に一致させること）。

```json
{
  "batchLabel": "2026年7月24日 更新分（アーカイブ）",
  "items": [
    { "id": "latest-mou-crisis-stage-0719", "...": "既存ファイルの内容をそのまま転記" },
    { "id": "latest-jordan-us-troops-killed-0718", "...": "既存ファイルの内容をそのまま転記" },
    { "id": "latest-kuwait-oil-facility-attack-0718", "...": "既存ファイルの内容をそのまま転記" }
  ]
}
```

### osint 配列 先頭に追加する新規1件

> 既存の `isLatest:true` エントリー（Al Jazeera「米、10夜連続の対イラン空爆」）は `isLatest:false` に変更してください。

```json
{
  "titleJa": "【Al Jazeera】トランプ氏「大規模攻撃」を警告——クウェート国境で火災・バーレーンも再攻撃",
  "titleEn": "Iran war updates: Trump warns of unprecedented 'massive attack' on Iran",
  "country": "カタール",
  "media": "Al Jazeera",
  "cardBg": "既存osintエントリーのcardBg値を踏襲",
  "cardBorder": "既存osintエントリーのcardBorder値を踏襲",
  "badgeColor": "既存osintエントリーのbadgeColor値を踏襲",
  "borderColor": "既存osintエントリーのborderColor値を踏襲",
  "textColor": "既存osintエントリーのtextColor値を踏襲",
  "url": "https://www.aljazeera.com/news/liveblog/2026/7/23/iran-war-live-us-launches-new-attacks-houthis-attack-2-saudi-oil-tankers",
  "date": "2026年7月23日（現地）/ 2026年7月24日 JST",
  "isLatest": true
}
```

---

## archive_timeline.json 追記（entries配列末尾に追加）

> Claude Code への指示：`docs/data/archive_timeline.json` の `entries` 配列末尾に、以下のエントリーを追加してください（既存エントリーは変更しないこと）。

<!-- FILE:docs/data/archive_timeline.json -->

```json
{
  "date": "2026-07-24",
  "dateLabel": "2026/07/24 09:23",
  "blockadeDay": 147,
  "summary": "フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——サウジ海上封鎖宣言を実行・トランプ大統領はイランへの「大規模攻撃」検討を警告・カザフスタンがドローン攻撃を受けCPCターミナル経由原油輸出を停止・クウェート国境で火災発生（鎮圧）・バーレーンも再攻撃・ルビオ国務長官「複数国がホルムズ護衛に関心」も法的障壁で未実現・Windward報告：南側迂回ルートでタンカー3隻被弾・通航は北側ルートに集中・原油はブレント7/23終値100.65ドル（前日比+7.00%・5月22日以来の高値）・日本関係船は残り4隻で変化なし・封鎖147日目・ニュース3件更新・osint更新",
  "relatedNews": [
    { "title": "フーシ派、サウジアラビアの原油タンカー2隻を紅海で攻撃——トランプ氏「大規模攻撃」検討を警告", "url": "https://www.barchart.com/futures/quotes/CBN26", "sourceLabel": "Trading Economics / Barchart" },
    { "title": "原油ブレント100ドル突破——カザフスタンもドローン攻撃受けCPCターミナル原油輸出停止", "url": "https://tradingeconomics.com/commodity/brent-crude-oil", "sourceLabel": "Trading Economics" },
    { "title": "ルビオ国務長官「複数国がホルムズ護衛参加に関心」——法的障壁で正式化せず", "url": "https://www.foxnews.com/live-news/iran-war-trump-strait-of-hormuz-oil-07-22-26", "sourceLabel": "Fox News Digital" }
  ]
}
```

---

## ✅ 出力前セルフチェック（再掲・全項目確認済み）

```
[✓] S01〜S11・SHIP_CONFIG・JSON-LD・C01・osint・全体系チェック 全19+3項目 ✓確認済
[⚠️] 全ルート現況サマリー ― 前回(7/22)据え置きだった問題を本日分で是正（上記「未実施項目あり」参照）
```
