# index_html_diffs.md — 2026年7月22日 09:15 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> news_data.json の変更は `<!-- FILE:docs/data/news_data.json -->` 指定ブロックを対象ファイルとして適用してください。
> archive_timeline.json の変更は `<!-- FILE:docs/data/archive_timeline.json -->` 指定ブロックを対象ファイルとして適用してください（entries配列末尾に追加・既存エントリーは変更しないこと）。
> 作業完了後に commit してください。push は確認後に指示します。

---

## ⚠️ セルフチェック（本文執筆前の事前貼付・2026/7/9ルール）

本日のセルフチェック項目数：19件（+ 全体系チェック3件 = 計22項目）

```
[✓] S01 ヘッダー ― 2026年7月22日 09:15 JST・封鎖145日目に更新
[✓] S02 TICKER ― タンカー2隻炎上・米10夜連続空爆・10日間停戦案・フーシ派サウジ海上封鎖宣言・原油91ドル台・封鎖145日目
[✓] S03 速報インシデント ― 7/22 09:15付け・4件新規追加（タンカー炎上／10日間停戦案／フーシ派封鎖宣言／戦費375億ドル）
[✓] S04 情勢カード3枚 ― 外交・軍事・船舶市場を7/22版に更新
[✓] S05 COUNTDOWN ― 封鎖145日目・機雷除去期限(7/17)徒過を明記・MOU最終期限残25日
[✓] S06 シナリオ確率補足バナー ― 7/22 09:15 JST日付更新・矢印をA↓B→C↑D↑に更新
[✓] S07 シナリオ4本 ― A/B/C/D本文をタンカー炎上・10日間停戦案・フーシ派封鎖で更新
[✓] S08 シナリオフッター ― 次の焦点5点を7/22版に更新
[✓] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成）
[✓] S10 news_data.json更新メモ ― latest 3件新規・osint 1件・updated日付
[✓] S11 更新ログ ― 3ブロック構成で先頭に7/22 09:15行追記・旧3件目をlog-collapseへ移動・合計10件超過分を削除
[✓] SHIP_CONFIG ― C01検証実施・変化なし・dateConfirmedを7/22に更新
[✓] JSON-LD dateModified ― 2026-07-22T09:15:00+09:00に更新
[✓] C01タンカー確認 ― 日本語3クエリ＋英語1クエリを個別実行・変化なし確認
[✓] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[✓] 全体 ― ニュースURLにAI捏造・推測URLが混入していないか（web検索確認済みURLのみ使用）
[✓] 全体 ― 📰関連最新ニュースにAl Jazeeraが混入していないか（osintのみに配置）
[✓] 全体 ― 人名が日本語表記になっているか（トランプ・ヘグセス・イラン外務省等）
[✓] 全体 ― diffs.md本文執筆の前にproject_knowledge_searchでセルフチェック原文を取得したか

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記のまま維持 ✓（変更不要）
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：S04カード③内で7/22 09:15 JST再確認済を明示 ✓
```

---

## C01 タンカー確認（必須・毎回実施）

- 日本語クエリ①「日本関係船舶 ホルムズ海峡 通過 足止め 7月」／②「日本関係船舶 ホルムズ海峡 外務省」／③「金子国土交通大臣 会見 ホルムズ海峡 7月21日」「金子国土交通大臣 記者会見 ホルムズ海峡 日本関係船舶 隻」を個別実行
- 英語クエリ「Japanese ships Strait of Hormuz stranded detained July 2026」を実行
- 結果：金子国交相の新規会見・外務省新規発表は確認されず。直近の確定情報は7/10会見の「残り4隻」のまま変化なし（7/19確認時点から変化なし）
- 判定：**変化なし** → SHIP_CONFIG の totalShips・passableShips は据え置き、dateConfirmed のみ本日日時＋「変化なし」で更新

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米イラン停戦覚書は事実上崩壊——イラン外務省報道官「MOUは危機段階に入った」と表明／米軍は7夜連続で対イラン空爆を継続しバンダルハミールの橋梁・チャバハール港監視塔を破壊／イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃——ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の戦死者）／クウェート石油公社施設が甚大な被害を受け負傷者発生／原油はブレント7/17終値88.09ドルまで急伸／封鎖142日目）</span>
    <span class="badge-item badge-date">📅2026年7月19日 10:17 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（ホルムズ海峡でタンカー2隻が爆発・炎上——IRGCは南側迂回ルート航行中と発表・UKMTOも別途正体不明飛翔体によるタンカー損傷を報告／米軍は対イラン10夜連続空爆を継続／トランプ大統領、仲介国提示の「10日間停戦」受け入れか大規模軍事作戦かの二択に直面——数日内に方針決定へ（Axios報道）／フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線／原油はブレント7/21終値91.10ドルまで急伸（前日比+2.11%）／封鎖145日目）</span>
    <span class="badge-item badge-date">📅2026年7月22日 09:15 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月19日 10:17 JST） -->
      🚨【MOU事実上崩壊】イラン外務省報道官「停戦覚書は危機段階に入った」——米は7夜連続で対イラン空爆、バンダルハミール橋梁・チャバハール港監視塔を破壊（7/17〜18 JST）｜⚔️ イラン、ヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃——ヨルダン米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者・7/17）｜🛢️ クウェート石油公社施設が「甚大な物的損害」と発表・負傷者発生（7/18）｜💥 イラン側発表：直近の米空爆で46名死亡・400名超負傷（橋梁攻撃での8名死亡含む・7/18時点）｜🚢 ホルムズ通航量、7/16(木)は8隻のみで3週間ぶり最低水準——MarineTraffic分析｜🛢️ 原油続伸——ブレント7/17終値88.09ドル（週間+14%超）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を未着手のまま徒過・最終期限（8/16）まで残28日｜封鎖142日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月22日 09:15 JST） -->
      🚨【ホルムズでタンカー2隻炎上】IRGC発表：南側迂回ルート航行中のタンカー2隻が爆発・炎上——UKMTOも別途正体不明飛翔体による損傷を報告（7/21未明 JST）｜💥 米軍、対イラン10夜連続空爆——ゲシュム島・バンダルアッバース等で爆発（7/21 JST）｜🕊️ トランプ氏、仲介国（カタール・パキスタン等）提示の「10日間停戦」受け入れか大規模軍事作戦かの二択に直面——数日内に方針決定へ（Axios・7/21）｜⚓ フーシ派、サウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新たな脅威（7/20）｜🛢️ 原油急伸——ブレント7/21終値91.10ドル（前日比+2.11%）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を徒過のまま・最終期限（8/16）まで残25日｜封鎖145日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

### トグルボタン内テキスト・日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米イラン停戦覚書、事実上崩壊——ヨルダンで米兵2名戦死・1名不明／イランがヨルダン・クウェート・バーレーン・カタール・イラクを攻撃／クウェート石油施設に甚大被害</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/19 10:17 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">ホルムズ海峡でタンカー2隻炎上／米、10夜連続空爆／トランプ氏「10日間停戦か大規模作戦か」の二択に直面／フーシ派、サウジへ海上封鎖宣言</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/22 09:15 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグを置き換え）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/19 10:17 速報】イラン外務省報道官バゲイー氏「米イラン停戦覚書は危機段階に入った」と表明——米は7夜連続で対イラン空爆継続・バンダルハミールの橋梁とチャバハール港監視塔を破壊｜イラン、ヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃——ヨルダンのムワッファク・サルティ空軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者・負傷4名は退院済み）｜クウェート石油公社、石油部門施設が「甚大な物的損害」を受け負傷者発生と発表｜イラン側発表：直近の米空爆により46名死亡・400名超負傷（橋梁攻撃での8名死亡含む）｜ホルムズ通航量は7/16(木)8隻のみで3週間ぶり最低水準——原油はブレント7/17終値88.09ドルまで急伸（週間+14%超）｜日本関係船は残り4隻で変化なし｜封鎖142日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/22 09:15 速報】イラン革命防衛隊（IRGC）、南側迂回ルートを航行中のタンカー2隻が爆発・炎上したと発表——「米軍の誤誘導」と主張。UKMTOは別途、オマーン沖でタンカー1隻が正体不明の飛翔体により損傷し乗員が退避したと報告（同一事案か未確認）｜米軍は7/21未明に対イラン10夜連続空爆を実施——ゲシュム島・バンダルアッバース・バンダルレンゲ等で爆発｜Axios報道：トランプ大統領は仲介国（カタール・パキスタン等）提示の「10日間停戦」受け入れか、イスラエルと共同での大規模軍事作戦かの二択に直面——数日内に方針決定の見通し｜イラン高官はロイターに10日間停戦案の受領を認め、外務省も複数提案受領を確認｜フーシ派がサウジアラビアへ海上封鎖を宣言（7/20）——バブ・エル・マンデブ海峡経由の迂回ルートにも新戦線、サウジは「断固たる対抗措置」を表明｜ヘグセス国防長官、対イラン戦費を約375億ドルと試算（7/21議会証言）｜原油はブレント7/21終値91.10ドルまで急伸（前日比+2.11%）｜日本関係船は残り4隻で変化なし｜封鎖145日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に4件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇺🇸 7/17 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🚢 7/21 JST</span>
  <span style="color:#e2e8f0;"> イラン革命防衛隊（IRGC）は、南側迂回ルート（オマーン指定ルート）を航行しようとしたタンカー2隻が爆発・炎上し航行不能になったと発表。「米軍の誤誘導」によるものと主張し、捜索救難部隊が乗員を退避中とした。英国海事貿易機関（UKMTO）は同日、オマーン沖リマ岬東方8海里で別のタンカー1隻が正体不明の飛翔体により損傷し、乗員が救命艇で退避したと報告——IRGC発表と同一事案かは未確認。環境汚染の報告は現時点でなし。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🕊️ 7/20〜21 JST</span>
  <span style="color:#e2e8f0;"> ロイター通信によれば、イラン政府高官が仲介国（カタール・パキスタン等）から10日間の停戦提案を受領したことを認めた。案は6/17署名のMOU（覚書）の立て直しとホルムズ海峡開放への道筋回復を狙うもの。イラン外務省も複数の提案受領を確認したが条件は非公表。Axiosは米・イスラエル当局者の話として、トランプ大統領がこの10日間停戦の実施か、イスラエルと共同での大規模軍事作戦の実施かという二択に直面していると報道——数日内に方針が決まる見通しとした。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">⚓ 7/20 JST</span>
  <span style="color:#e2e8f0;"> イエメンの親イラン武装組織フーシ派は報道官談話で、サウジアラビアが「約12年にわたり不当な包囲を続け港湾・空港を封鎖している」と非難した上で、「目には目を」の原則に基づきサウジアラビアへの即時海上封鎖実施を宣言。バブ・エル・マンデブ海峡経由のサウジ船舶封鎖が懸念される。サウジ主導のアラブ連合軍報道官は「商船を守るためあらゆる断固たる措置を講じる」と反発。ホルムズ海峡が封鎖状態にある中、サウジの紅海迂回ルートにも新たな不確実性が生じている。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fde68a;font-weight:700;">💰 7/21 JST</span>
  <span style="color:#e2e8f0;"> ヘグセス国防長官は議会証言で、対イラン軍事作戦の戦費がこれまでに約375億ドルに達したとの試算を示し、追加予算要求への理解を求めた。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇺🇸 7/17 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">💰 外交：MOU「危機段階」入り——トランプ「停戦は終わった」／イラン外務省は米側の義務違反を主張</div>
        <div class="s-body">イラン外務省報道官バゲイー氏は「米イラン間のMOUは危機段階に入った」と述べ、イランが履行していない点があるとすれば米側の義務違反が原因だと主張した。週末のオマーンでの協議はホルムズ海峡の安全通航に限定した内容で、「米国のオマーンへの圧力」により合意に至らなかったとした。トランプ大統領は「（イランとの合意を）もう終わったと思っている」と述べ、事実上MOUの形骸化を認めた形。国連人権高等弁務官テュルク氏は「数百万人が依存する生命線」への打撃に懸念を表明し、双方に即時攻撃停止と停戦復帰を要請した。</div>
        <div class="s-src">出典: ABC News / CNN / 国連人権高等弁務官事務所（7/13〜18 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">💰 外交：仲介国「10日間停戦」提案——トランプ氏、受諾か大規模軍事作戦かの二択に直面</div>
        <div class="s-body">Axiosによれば、米・イスラエル当局者はトランプ大統領がホルムズ海峡再開を目指す仲介国（カタール・パキスタン等）提示の10日間停戦の実施か、イスラエルと共同での大規模軍事作戦の実施かという二択に直面していると報道。イラン政府高官はロイターに停戦案受領を認め、外務省も複数提案受領を確認したが条件は非公表。ヨルダン基地攻撃での米兵死亡への報復として、米国はまず数日間攻撃を継続した後に停戦案を検討するとの見方も一部で示されている。現時点で最終決定はなされていない。</div>
        <div class="s-src">出典: Axios（テレビ朝日系ANN報道）/ ロイター（産経新聞・ブルームバーグ経由）（7/20〜21 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">⚔️ 軍事：米、7夜連続空爆——ヨルダンで米兵2名戦死・1名不明／イランはクウェート石油施設等を攻撃</div>
        <div class="s-body">CENTCOMは7夜連続で対イラン空爆を実施し「監視施設・軍事兵站インフラ・地下武器庫・海上能力」を標的にしたと発表。バンダルハミールの高速道路・鉄道橋、チャバハール港の監視塔（IRGCが商船追跡に使用）を破壊した。イランはヨルダン・クウェート・バーレーン・カタール・イラク（クルド人自治区）へ報復攻撃を実施し、ヨルダンのムワッファク・サルティ空軍基地への弾道ミサイル・ドローン攻撃で米兵2名が交戦中に戦死・1名が行方不明——3月以来初の米軍戦死者となった。クウェート石油公社は石油部門施設への攻撃で「甚大な物的損害」と負傷者発生を発表。イラン側は直近の米空爆で46名死亡・400名超負傷と発表している。</div>
        <div class="s-src">出典: CENTCOM / NPR / Bloomberg / Air Force Times（7/17〜18 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">⚔️ 軍事：米、対イラン10夜連続空爆——ホルムズ海峡でタンカー2隻炎上／フーシ派がサウジへ海上封鎖宣言</div>
        <div class="s-body">CENTCOMは7/21未明、対イラン10夜連続となる空爆を実施し、ゲシュム島・バンダルアッバース・バンダルレンゲ等で爆発が確認された。イラン革命防衛隊（IRGC）は同日、南側迂回ルートを航行しようとしたタンカー2隻が爆発・炎上し航行不能になったと発表——「米軍の誤誘導」と主張。UKMTOも別途、オマーン沖で正体不明の飛翔体によるタンカー損傷・乗員退避を報告した（同一事案か未確認）。並行して、イエメンの親イラン武装組織フーシ派がサウジアラビアへの海上封鎖を宣言し、バブ・エル・マンデブ海峡経由の迂回ルートにも新たな脅威が生じている。ヘグセス国防長官は対イラン戦費を約375億ドルと試算した。</div>
        <div class="s-src">出典: CENTCOM / Al Jazeera / AFPBB News / ロイター（7/20〜21 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/19再確認）——ホルムズ通航量は3週間ぶり最低水準／原油急伸</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/19 10:17 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。ホルムズ海峡の通航量はMarineTraffic分析によれば7/16(木)にわずか8隻まで落ち込み、3週間ぶりの最低水準を記録した。原油はブレント先物が7/17終値で88.09ドル（一時88.38ドルまで上昇・週間+14%超）を付け、今月の高値圏に迫っている。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残28日に迫っている。</div>
        <div class="s-src">出典: NPR / TradingEconomics / Investing.com（7/17〜18 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/22再確認）——ホルムズ通航量は週次66%減／原油91ドル台</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/22 09:15 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。Lloyd's List Intelligenceによれば、7/20までの週のホルムズ海峡通航量は53隻で前週比66%減。CNBCはさらに、7/17〜19の3日間ではわずか40隻（1日平均13隻）にとどまったと報じた。原油はブレント先物が7/21終値で91.10ドル（前日比+2.11%・一時91.57ドル）に達し、フーシ派のサウジ海上封鎖宣言も価格を押し上げている。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残25日に迫っている。</div>
        <div class="s-src">出典: CNBC / Lloyd's List / TradingEconomics（7/21 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU事実上崩壊——7夜連続空爆・ヨルダン米兵死亡・クウェート石油施設被弾」——封鎖142日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 11「ホルムズでタンカー2隻炎上・フーシ派サウジ海上封鎖宣言——トランプ氏10日間停戦か大規模作戦かの二択に直面」——封鎖145日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🚨 <strong>イラン外務省「MOUは危機段階」と表明・トランプ「停戦は終わった」／米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊／イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃——ヨルダン米軍基地攻撃で米兵2名戦死・1名不明（3月以来初）／クウェート石油公社施設に甚大被害／日本関係船は残り4隻で変化なし——封鎖142日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残28日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米軍戦死者の氏名公表とその後の対応 ②イランの追加報復の範囲拡大有無 ③クウェート石油供給への実害の規模 ④MOU正式破棄・全面戦争再開の有無 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残28日（8/16）</span>
<!-- OLD:END -->
<!-- NEW:START -->
        🚨 <strong>ホルムズ海峡でタンカー2隻炎上・UKMTOも別途タンカー損傷を報告／米軍は対イラン10夜連続空爆継続／トランプ氏、仲介国提示の「10日間停戦」受け入れか大規模軍事作戦かの二択に直面——数日内に方針決定へ／フーシ派がサウジアラビアへ海上封鎖を宣言——紅海迂回ルートにも新戦線／日本関係船は残り4隻で変化なし——封鎖145日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残25日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米国の最終方針決定（10日間停戦受諾か大規模軍事作戦か） ②タンカー炎上・UKMTO損傷事案の被害詳細確認 ③フーシ派海上封鎖の実効性・紅海迂回ルートへの影響 ④MOU正式破棄・全面戦争再開の有無 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残25日（8/16）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年7月19日 10:17 JST 更新</span><br>
  📊 <strong>MOUは「危機段階」入り・トランプ「停戦は終わった」——米は7夜連続空爆・イランはヨルダン等5方面へ報復、ヨルダンで米兵2名が3月以来初の戦死：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — 双方が公然と相手の義務違反を非難し合い、履行の枠組み自体が形骸化<br>
  🅑 膠着継続 <span style="color:#f87171;">↓</span> — 米兵戦死・5カ国への報復攻撃は「膠着」の域を明確に超え、全面戦争再燃の様相<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 機雷除去期限徒過・クウェート石油施設被弾等、封鎖の実害が制度化しつつある<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — 米軍の戦闘死者発生・5カ国同時攻撃により、本シナリオへの移行リスクが最も顕著に高まっている<br>
  <strong style="color:#f87171;">米兵の戦闘死は3月以来初めてであり、事態は「膠着」段階を超え全面戦争再燃に近づいている（A↓ B↓ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月19日 10:17 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（A/B/C/D本文）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>イラン外務省報道官は米イラン間のMOUが「危機段階に入った」と公言し、トランプ大統領も「（合意を）もう終わったと思っている」と述べるなど、双方が事実上の履行放棄を認め合う状況にある。米軍は7夜連続で空爆を継続し、イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃を行い、ヨルダンでは米兵2名が3月以来初めて戦闘で死亡した。段階的なMOU履行という枠組み自体がほぼ機能を失っており、本シナリオの実現可能性は極めて低い水準にとどまる。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>仲介国（カタール・パキスタン等）が「10日間停戦」を提示し、イラン高官・外務省双方がこれを認めるなど、初めて具体的な収拾ルートが外交テーブルに乗った。ただしAxiosによれば米・イスラエル当局者はトランプ大統領がこの停戦案受諾かイスラエルと共同での大規模軍事作戦かの「二択」に直面していると認めており、最終決定は依然として不透明。同時にホルムズ海峡ではタンカー2隻が炎上するなど軍事的実害も継続しており、段階的なMOU履行という枠組みの再構築にはなお高いハードルが残る。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>イランはヨルダン・クウェート・バーレーン・カタール・イラクの5カ国へ同時に報復攻撃を行い、クウェートでは石油公社の施設が「甚大な物的損害」を受けるなど、単純な「膠着」では説明できない規模の実力行使が現実化している。ヨルダンでの米兵戦死は3月以来初めてであり、米軍の直接的な人的損耗が発生した点で従来の膠着状態から質的に変化している。主要海運各社は依然ケープ廻りを継続しており、ホルムズ通航量は7/16に8隻まで落ち込むなど、事態沈静化の材料は見当たらない。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>10日間停戦案が実際に発効すれば、当面は「戦闘一時停止・海峡通航は限定的」という膠着状態が再現される可能性がある。一方でイランはヨルダン・クウェート等5カ国への報復攻撃を続け、フーシ派も新たにサウジアラビアへの海上封鎖を宣言するなど、単純な現状維持を超えた多方面での緊張激化が同時進行している。停戦案の受諾如何が今後数日のシナリオ分岐を左右する。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>機雷除去はMOU上の7/17期限を未着手のまま徒過し、期限そのものが形骸化した。クウェート石油公社施設への攻撃、チャバハール港監視塔・バンダルハミール橋梁の破壊など、封鎖・攻撃の常態化が着実に進行している。イラン外務省報道官が「MOUは危機段階」と明言したことで、南北両ルートの正常化はさらに遠のいており、通航量の低迷（7/16に8隻のみ）が続く前提での「制度化」がより現実味を帯びている。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>ホルムズ海峡ではタンカー2隻が炎上・航行不能となり、UKMTOも別途タンカー損傷を報告するなど、南側迂回ルートを含めた事実上の航行不能状態が続いている。フーシ派によるサウジ海上封鎖宣言は、ホルムズの代替輸出ルートである紅海側にも新たな制約をもたらし、「完全封鎖の制度化」がホルムズ単独ではなく地域全体に広がりつつある構図を強めている。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>CENTCOMは7夜連続で対イラン空爆を継続し、バンダルハミールの橋梁・チャバハール港監視塔を破壊するなど攻撃対象を段階的に拡大している。イランはヨルダン・クウェート・バーレーン・カタール・イラクへの同時報復攻撃に踏み切り、ヨルダンでは米兵2名が交戦で戦死・1名が行方不明となった——3月以来初めての米軍戦闘死者である。シナリオCとの差：C=「封鎖・通航管理を巡る制度的対立」、D=「米軍の人的損耗を伴う実力による現状変更・攻撃対象の多国間拡大」。米兵戦死という一線を越えたことで、本シナリオへの本格移行リスクは今回の更新で最も顕著に高まっている。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>米軍は対イラン10夜連続空爆を継続し、フーシ派の参戦（サウジ海上封鎖宣言）により戦線がイエメン・紅海方面へも拡大した。ヘグセス国防長官は戦費が約375億ドルに達したと議会証言し、長期化する軍事作戦の規模が改めて可視化された。シナリオCとの差：C=「封鎖・通航管理を巡る制度的対立」、D=「多国間・多正面にわたる実力による現状変更」。トランプ大統領が大規模軍事作戦を選択した場合、イスラエルとの共同作戦を含む本格的なエスカレーションへ移行するリスクが最も高い局面にある。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5点）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">戦死した米兵の氏名公表とその後の米側対応</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イランの追加報復の範囲拡大有無（湾岸諸国以外への波及）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">クウェート石油供給への実害の規模と回復状況</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">MOU正式破棄・全面戦争再開の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月19日 10:17 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米国の最終方針決定（10日間停戦受諾か大規模軍事作戦か）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">タンカー炎上・UKMTO損傷事案の被害詳細確認</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">フーシ派海上封鎖の実効性・紅海迂回ルートへの影響</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">MOU正式破棄・全面戦争再開の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月22日 09:15 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## SHIP_CONFIG（変化なし・dateConfirmedのみ更新）

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年7月19日 10:17 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。米イラン停戦覚書は事実上崩壊し軍事衝突が拡大中）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年7月22日 09:15 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。ホルムズ海峡でタンカー2隻炎上・フーシ派がサウジへ海上封鎖宣言する中、トランプ氏は10日間停戦か大規模軍事作戦かの二択に直面）'
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）※最後に作成

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🗣️ イラン外務省「MOUは危機段階」と表明・トランプ「停戦は終わった」——米軍は7夜連続で対イラン空爆継続。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷 イランがヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃——ヨルダンで米兵2名戦死・1名不明（3月以来初）。日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 戦死した米兵の氏名公表・イランの追加報復の行方が焦点、封鎖142日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残28日。
</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
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
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💥MOU「危機段階」入り・トランプ「停戦は終わった」</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸ヨルダンで米兵2名戦死・1名不明</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️クウェート石油施設に甚大被害</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント88ドル台・週間+14%超</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💥タンカー2隻炎上・米10夜連続空爆</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️トランプ氏「10日間停戦か大規模作戦か」の二択</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚓フーシ派、サウジへ海上封鎖宣言</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント91ドル台・+2.11%</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## JSON-LD dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-19T10:17:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-22T09:15:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新（latest 3件新規追加・4件をarchiveへ移動・osint 1件追加）

> Claude Code への指示：以下は `docs/data/news_data.json` に対する変更です。既存の `latest` 配列先頭に新規3件を追加し、既存の `isLatest:true` エントリー（id: `latest-mou-crisis-stage-0719`）は `isLatest:false` に変更。`latest` の末尾4件（id: `latest-kharg-tanker-0715` 相当の7/15カーグ島タンカー無力化・7/14の20%通航料撤回・7/15日本貿易会発言・7/14原油タンカー全通過の4件）は `archive` 配列の先頭に新規バッチ「2026年7月21日 更新分（アーカイブ）」として移動してください（該当4件のidは現状ファイルを参照し、正確に一致させてください）。

<!-- FILE:docs/data/news_data.json -->

### updated / staleNotice フィールド

```json
"updated": "2026年7月22日 09:15 日本時間JST",
"staleNotice": ""
```

### latest 配列 先頭に追加する新規3件

```json
{
  "id": "latest-hormuz-tankers-fire-0721",
  "title": "ホルムズ海峡でタンカー2隻炎上——IRGC発表、UKMTOも別途損傷を報告",
  "body": "イラン革命防衛隊（IRGC）は、南側迂回ルートを航行しようとしたタンカー2隻が爆発・炎上し航行不能になったと発表し、「米軍の誤誘導」によるものと主張した。英国海事貿易機関（UKMTO）は同日、オマーン沖で別のタンカー1隻が正体不明の飛翔体により損傷し、乗員が救命艇で退避したと報告——IRGC発表と同一事案かは未確認。米軍は同日、対イラン10夜連続空爆を実施した。",
  "sourceLabel": "Al Jazeera",
  "date": "2026年7月21日（現地）/ 2026年7月22日 JST",
  "label": "⚔️ 軍事",
  "url": "https://www.aljazeera.com/news/2026/7/21/hormuz-tankers-on-fire-as-us-iran-continue-attacks-whats-the-latest",
  "isLatest": true
},
{
  "id": "latest-10day-ceasefire-proposal-0721",
  "title": "仲介国「10日間停戦」提案——トランプ氏、受諾か大規模軍事作戦かの二択に直面",
  "body": "イラン政府高官はロイター通信に対し、仲介国（カタール・パキスタン等）から10日間の停戦提案を受領したことを認めた。案は6月17日署名のMOU（覚書）の立て直しとホルムズ海峡開放への道筋回復を狙う。Axiosは米・イスラエル当局者の話として、トランプ大統領がこの停戦案受諾かイスラエルと共同での大規模軍事作戦かという二択に直面していると報道。数日内に方針が決まる見通し。",
  "sourceLabel": "産経新聞（Yahoo!ニュース）/ Axios",
  "date": "2026年7月20日（現地）/ 2026年7月21日 JST",
  "label": "🕊️ 外交",
  "url": "https://news.yahoo.co.jp/articles/a756ce18793f140cb21858ea5545aee428925e86",
  "isLatest": false
},
{
  "id": "latest-houthi-saudi-blockade-0720",
  "title": "フーシ派がサウジアラビアへ海上封鎖を宣言——紅海迂回ルートにも新戦線",
  "body": "イエメンの親イラン武装組織フーシ派は、サウジアラビアが「約12年にわたり不当な包囲を続けている」と非難した上で、「目には目を」の原則に基づきサウジアラビアへの即時海上封鎖実施を宣言した。バブ・エル・マンデブ海峡経由のサウジ船舶封鎖が懸念され、サウジ主導のアラブ連合軍は「断固たる対抗措置を講じる」と反発。ホルムズ海峡封鎖に加え、サウジの紅海迂回ルートにも新たな不確実性が生じている。",
  "sourceLabel": "AFPBB News",
  "date": "2026年7月20日（現地）/ 2026年7月21日 JST",
  "label": "⚓ 海上輸送",
  "url": "https://www.afpbb.com/articles/-/3644879",
  "isLatest": false
}
```

### osint 配列 先頭に追加する新規1件（既存の isLatest:true は false に変更）

```json
{
  "id": "osint-us-10th-night-strikes-kuwait-0721",
  "titleJa": "【Al Jazeera】米、10夜連続の対イラン空爆——ホルムズでタンカー炎上・クウェートも攻撃",
  "titleEn": "US launches 10th night of strikes, Tehran attacks Kuwait",
  "country": "カタール",
  "media": "Al Jazeera",
  "cardBg": "rgba(56,189,248,0.05)",
  "cardBorder": "rgba(56,189,248,0.25)",
  "badgeColor": "#38bdf8",
  "borderColor": "rgba(56,189,248,0.4)",
  "textColor": "#7dd3fc",
  "url": "https://www.aljazeera.com/news/liveblog/2026/7/21/iran-war-live-us-launches-10th-night-of-strikes-tehran-attacks-kuwait",
  "date": "2026年7月21日（現地）/ 2026年7月22日 JST",
  "isLatest": true
}
```

---

## [S11] 更新ログ追記（3ブロック構成・常時表示3件固定 + log-collapse先頭挿入 + 超過分削除）

### ブロック1：常時表示3件の更新

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/19 10:17</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省「米イラン停戦覚書は危機段階に入った」と表明・トランプ「停戦は終わった」と言及・米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊・イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃・ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者）・クウェート石油公社施設に甚大な被害・イラン側発表で直近の米空爆により46名死亡400名超負傷・ホルムズ通航量は7/16に8隻のみで3週間ぶり最低水準・原油はブレント7/17終値88.09ドル（週間+14%超）・日本関係船は残り4隻で変化なし・封鎖142日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/16 10:52</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明・対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を攻撃・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更・IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明・トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も・米はIRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放・日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明・原油はブレント7/15終値84.95ドル・封鎖139日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月14日 18:00 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/14 18:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE国防省：ホルムズ海峡でタンカー「モンバサ」「アルバヒヤ」がイラン巡航ミサイル攻撃を受けインド人乗組員1人死亡・8人負傷（火災鎮圧）・UKMTOは別のタンカーへの飛翔体着弾も報告（同一事案か未確認）・トランプ大統領、対イラン戦闘は7/7に再開と議会へ正式通知・IRGCがバーレーン米軍レーダー施設破壊・ヨルダン拠点も攻撃と報道・日本関係の原油タンカーは全て通過済みで残り4隻（非タンカー）は変化なし・封鎖137日目・速報ティッカー/速報インシデント更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年7月22日 09:15 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/22 09:15</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン革命防衛隊、ホルムズ海峡南側迂回ルートでタンカー2隻が爆発・炎上したと発表・UKMTOも別のタンカー損傷を報告——米軍は対イラン10夜連続空爆を継続・Axios報道：トランプ大統領は仲介国提示の「10日間停戦」受諾か大規模軍事作戦かの二択に直面——数日内に方針決定へ・イラン高官はロイターに停戦案受領を認める・フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線・ヘグセス国防長官、戦費を約375億ドルと試算・原油はブレント7/21終値91.10ドル（前日比+2.11%）・日本関係船は残り4隻で変化なし・封鎖145日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/19 10:17</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省「米イラン停戦覚書は危機段階に入った」と表明・トランプ「停戦は終わった」と言及・米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊・イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃・ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者）・クウェート石油公社施設に甚大な被害・イラン側発表で直近の米空爆により46名死亡400名超負傷・ホルムズ通航量は7/16に8隻のみで3週間ぶり最低水準・原油はブレント7/17終値88.09ドル（週間+14%超）・日本関係船は残り4隻で変化なし・封鎖142日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/16 10:52</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明・対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を攻撃・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更・IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明・トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も・米はIRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放・日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明・原油はブレント7/15終値84.95ドル・封鎖139日目・ニュース3件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：旧3件目（7/14 18:00）を log-collapse 先頭に挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月14日 16:16 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月14日 18:00 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/14 18:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE国防省：ホルムズ海峡でタンカー「モンバサ」「アルバヒヤ」がイラン巡航ミサイル攻撃を受けインド人乗組員1人死亡・8人負傷（火災鎮圧）・UKMTOは別のタンカーへの飛翔体着弾も報告（同一事案か未確認）・トランプ大統領、対イラン戦闘は7/7に再開と議会へ正式通知・IRGCがバーレーン米軍レーダー施設破壊・ヨルダン拠点も攻撃と報道・日本関係の原油タンカーは全て通過済みで残り4隻（非タンカー）は変化なし・封鎖137日目・速報ティッカー/速報インシデント更新</div>
          <div>📅 <strong>2026年7月14日 16:16 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：合計10件超過分（最古2件）を削除

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月9日 06:59 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/09 06:59</span> — <strong style="color:#fca5a5;">【重大更新】</strong>トランプ大統領、NATO首脳会議（アンカラ）でイランとの停戦は「もう終わったと思っている」と表明・イラン指導部を罵倒（7/8）・アラグチー外相はXで反論・イラン外務省「MOUはホルムズ管理権をイランに戻す」——米は否定（7/8）・原油急騰（ブレント一時$75.18・+4.4%／WTI一時$74.26・+5.3%）・商船三井関係8隻が追加通過し日本関係船は残り18隻に（7/7判明・時事通信）・IMO「船員約6,000人取り残され」・封鎖132日目・ニュース3件更新</div>
          <div>📅 <strong>2026年7月8日 08:14 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/08 08:14</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>CENTCOM、ホルムズ海峡通過中の駆逐艦3隻（トラクスタン・ペラルタ・メイソン）への攻撃に反撃——米イラン軍事衝突が再燃（7/7）・タンカー3隻新たに被弾（カタール籍Al Rekayyat・サウジ籍Wedyan含む）・米財務省がイラン産原油売却許可を取消（7/17清算期限）・アラグチー外相「脅威継続なら交渉再開せず」・一方で日本関係船10隻超がイランルート経由で通過し残り26隻に（7/6〜7・金子国交相発表）・故ハメネイ師、本日ナジャフ・カルバラで追悼式典（7/9マシュハド埋葬）・封鎖131日目・ニュース3件更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

> 注：削除した2件（2026/07/09 06:59・2026/07/08 08:14）は `docs/data/update_log.json` の先頭に追加してください（`update_log.json` は既に7/8・7/9分を含む可能性があるため、重複がないかご確認の上で追加してください）。

---

## [S12] archive_timeline.json 追記（entries配列末尾に1件追加）

<!-- FILE:docs/data/archive_timeline.json -->

```json
{
  "date": "2026-07-22",
  "dateLabel": "2026/07/22 09:15",
  "blockadeDay": 145,
  "summary": "イラン革命防衛隊、ホルムズ海峡南側迂回ルートでタンカー2隻が爆発・炎上したと発表・UKMTOも別のタンカー損傷を報告——米軍は対イラン10夜連続空爆を継続・Axios報道：トランプ大統領は仲介国提示の「10日間停戦」受諾か大規模軍事作戦かの二択に直面——数日内に方針決定へ・イラン高官はロイターに停戦案受領を認める・フーシ派がサウジアラビアへ海上封鎖を宣言——バブ・エル・マンデブ海峡の迂回ルートにも新戦線・ヘグセス国防長官、戦費を約375億ドルと試算・原油はブレント7/21終値91.10ドル（前日比+2.11%）・日本関係船は残り4隻で変化なし・封鎖145日目・ニュース3件更新・osint更新",
  "relatedNews": [
    {
      "title": "ホルムズ海峡でタンカー2隻炎上——IRGC発表、UKMTOも別途損傷を報告",
      "url": "https://www.aljazeera.com/news/2026/7/21/hormuz-tankers-on-fire-as-us-iran-continue-attacks-whats-the-latest",
      "sourceLabel": "Al Jazeera"
    },
    {
      "title": "仲介国「10日間停戦」提案——トランプ氏、受諾か大規模軍事作戦かの二択に直面",
      "url": "https://news.yahoo.co.jp/articles/a756ce18793f140cb21858ea5545aee428925e86",
      "sourceLabel": "産経新聞（Yahoo!ニュース）"
    },
    {
      "title": "フーシ派がサウジアラビアへ海上封鎖を宣言——紅海迂回ルートにも新戦線",
      "url": "https://www.afpbb.com/articles/-/3644879",
      "sourceLabel": "AFPBB News"
    }
  ]
}
```

---

## 適用後の確認コマンド

```bash
grep -n "封鎖145日目\|2026年7月22日 09:15\|dateModified.*2026-07-22" docs/index.html | head -20
```
