# index_html_diffs.md — 2026年7月19日 10:17 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> news_data.json の変更は `<!-- FILE:docs/data/news_data.json -->` 指定ブロックを対象ファイルとして適用してください。
> 作業完了後に commit してください。push は確認後に指示します。

---

## ⚠️ セルフチェック（本文執筆前の事前貼付・2026/7/9ルール）

本日のセルフチェック項目数：19件（+ 全体系チェック3件 = 計22項目）

```
[✓] S01 ヘッダー ― 2026年7月19日 10:17 JST・封鎖142日目に更新
[✓] S02 TICKER ― MOU事実上崩壊・ヨルダン米兵死亡・クウェート石油施設被弾・Brent88ドル台・封鎖142日目
[✓] S03 速報インシデント ― 7/19 10:17付け・3件新規追加（ヨルダン米兵死亡／クウェート被弾／MOU危機段階発言）
[✓] S04 情勢カード3枚 ― 外交・軍事・船舶市場を7/19版に更新
[✓] S05 COUNTDOWN ― 封鎖142日目・機雷除去期限(7/17)徒過を明記・MOU最終期限残28日
[✓] S06 シナリオ確率補足バナー ― 7/19 10:17 JST日付更新・矢印をA↓B↓C↑D↑に更新
[✓] S07 シナリオ4本 ― A/B/C/D本文をMOU崩壊・ヨルダン死者・クウェート被弾反映で更新
[✓] S08 シナリオフッター ― 次の焦点5点を7/19版に更新
[✓] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成）
[✓] S10 news_data.json更新メモ ― latest 3件新規・osint 1件・updated日付
[✓] S11 更新ログ ― 2ブロック構成で先頭に7/19 10:17行追記・旧3件目をlog-collapseへ移動
[✓] SHIP_CONFIG ― C01検証実施・変化なし・dateConfirmedを7/19に更新
[✓] JSON-LD dateModified ― 2026-07-19に更新
[✓] C01タンカー確認 ― 日本語3クエリ＋英語1クエリを個別実行・変化なし確認
[✓] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[✓] 全体 ― ニュースURLにAI捏造・推測URLが混入していないか（web検索確認済みURLのみ使用）
[✓] 全体 ― 📰関連最新ニュースにAl Jazeeraが混入していないか（osintのみに配置）
[✓] 全体 ― 人名が日本語表記になっているか（トランプ・アラグチー・バゲイー等）
[✓] 全体 ― diffs.md本文執筆の前にproject_knowledge_searchでセルフチェック原文を取得したか

二重封鎖表記チェック：「イラン・米国による二重封鎖」表記のまま維持 ✓（変更不要）
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：S04カード③内で7/19 10:17 JST再確認済を明示 ✓
```

---

## C01 タンカー確認（必須・毎回実施）

- 日本語クエリ①「日本関係船舶 ホルムズ海峡 通過 足止め」／②「外務省 ホルムズ海峡 日本関係船舶」／③「金子国交相 会見 ホルムズ海峡 7月」を個別実行
- 英語クエリ「Japanese ships Strait of Hormuz stranded detained July 2026」を実行
- 結果：金子国交相の新規会見・外務省新規発表は確認されず。直近の確定情報は7/10会見の「残り4隻」のまま変化なし
- 判定：**変化なし** → SHIP_CONFIG の totalShips・passableShips は据え置き、dateConfirmed のみ本日日時＋「変化なし」で更新

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換する方針に変更／対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を破壊／新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・2隻を進路変更／IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明／トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も／封鎖139日目）</span>
    <span class="badge-item badge-date">📅2026年7月16日 10:52 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（米イラン停戦覚書は事実上崩壊——イラン外務省報道官「MOUは危機段階に入った」と表明／米軍は7夜連続で対イラン空爆を継続しバンダルハミールの橋梁・チャバハール港監視塔を破壊／イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃——ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の戦死者）／クウェート石油公社施設が甚大な被害を受け負傷者発生／原油はブレント7/17終値88.09ドルまで急伸／封鎖142日目）</span>
    <span class="badge-item badge-date">📅2026年7月19日 10:17 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月16日 10:52 JST） -->
      🚨【トランプ、20%通航料を撤回】ガルフ諸国との貿易投資取引に転換すると表明——「石油はかつてないほど流れている」（7/14夜JST）｜⚔️ CENTCOM、5夜連続で対イラン空爆——Greater Tunb島の巡航ミサイル拠点等を破壊・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・2隻を進路変更（7/15 JST）｜🗣️ IRGC海軍幹部「海峡閉鎖の方針を維持し、侵略者に最も過酷な打撃を加える」と表明（7/15）｜⚠️ トランプ「来週はもっと悪くなる——発電所と橋を破壊する」と警告・カーグ島制圧検討との報道も（7/15）｜🇺🇸 米、IRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放（7/15）｜🛢️ 原油続伸——ブレント7/15終値84.95ドル・WTIは7/16アジア時間も80ドル台で4日続伸｜🇯🇵 日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明（7/15）｜封鎖139日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月19日 10:17 JST） -->
      🚨【MOU事実上崩壊】イラン外務省報道官「停戦覚書は危機段階に入った」——米は7夜連続で対イラン空爆、バンダルハミール橋梁・チャバハール港監視塔を破壊（7/17〜18 JST）｜⚔️ イラン、ヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃——ヨルダン米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者・7/17）｜🛢️ クウェート石油公社施設が「甚大な物的損害」と発表・負傷者発生（7/18）｜💥 イラン側発表：直近の米空爆で46名死亡・400名超負傷（橋梁攻撃での8名死亡含む・7/18時点）｜🚢 ホルムズ通航量、7/16(木)は8隻のみで3週間ぶり最低水準——MarineTraffic分析｜🛢️ 原油続伸——ブレント7/17終値88.09ドル（週間+14%超）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認・金子国交相の新規会見なし）｜⚠️ MOU機雷除去期限（7/17）を未着手のまま徒過・最終期限（8/16）まで残28日｜封鎖142日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

### トグルボタン本文・バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米、5夜連続の対イラン空爆——カーグ島向けタンカーを無力化／トランプは20%通航料を撤回しガルフ投資取引に転換／IRGC「海峡閉鎖を維持」</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/16 10:52 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米イラン停戦覚書、事実上崩壊——ヨルダンで米兵2名戦死・1名不明／イランがヨルダン・クウェート・バーレーン・カタール・イラクを攻撃／クウェート石油施設に甚大被害</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/19 10:17 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/16 10:52 速報】トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明——「石油はかつてないほど流れている」と主張｜CENTCOM、対イラン空爆を5夜連続実施——Greater Tunb島の巡航ミサイル拠点等を破壊・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・2隻を進路変更｜IRGC海軍幹部「海峡閉鎖の方針を維持し、侵略者に最も過酷な打撃を加える」と表明｜トランプ「来週はもっと悪くなる——発電所と橋を破壊する」と警告・カーグ島制圧検討との報道も｜米、IRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放｜日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明｜封鎖139日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/19 10:17 速報】イラン外務省報道官バゲイー氏「米イラン停戦覚書は危機段階に入った」と表明——米は7夜連続で対イラン空爆継続・バンダルハミールの橋梁とチャバハール港監視塔を破壊｜イラン、ヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃——ヨルダンのムワッファク・サルティ空軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者・負傷4名は退院済み）｜クウェート石油公社、石油部門施設が「甚大な物的損害」を受け負傷者発生と発表｜イラン側発表：直近の米空爆により46名死亡・400名超負傷（橋梁攻撃での8名死亡含む）｜ホルムズ通航量は7/16(木)8隻のみで3週間ぶり最低水準——原油はブレント7/17終値88.09ドルまで急伸（週間+14%超）｜日本関係船は残り4隻で変化なし｜封鎖142日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に3件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#86efac;font-weight:700;">💰 7/14 JST夜</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇺🇸 7/17 JST</span>
  <span style="color:#e2e8f0;"> ヨルダンのムワッファク・サルティ空軍基地（米軍・戦闘機駐留）がイランの弾道ミサイル・ドローン攻撃を受け、CENTCOMは米兵2名が交戦中に戦死したと発表。1名が行方不明となっているほか、4名がヨルダン国内の病院に搬送されたが既に退院した。米軍の戦闘死者は3月以来初めてで、CENTCOMは戦死者の氏名を近親者への通知から24時間経過後に公表するとしている。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fca5a5;font-weight:700;">🛢️ 7/18 JST</span>
  <span style="color:#e2e8f0;"> クウェート石油公社は、石油部門の重要施設が「度重なる過酷なイランの攻撃」を受け「甚大な物的損害」と負傷者が発生したと発表。カタール外務省はヨルダン・バーレーン・クウェートへの攻撃を「主権と領土保全への重大な違反、国際法違反」だとして最も強い言葉で非難した。ヨルダン軍は7/19未明にもイランのミサイル10発を迎撃したと発表。バーレーンでは空襲警報が発令された。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fde68a;font-weight:700;">🗣️ 7/13〜18 JST</span>
  <span style="color:#e2e8f0;"> イラン外務省報道官エスマイル・バゲイー氏は7/13の会見で米イラン間のMOU（覚書）が「危機段階に入った」と述べ、イランが履行していない点があるとすれば米側の「義務違反」が直接の原因だと主張。週末のオマーンでの協議は核問題ではなくホルムズ海峡の安全通航に限定した協議だったとし、「米国のオマーンへの公然・非公然の圧力」により合意に至らなかったと説明した。トランプ大統領は「（イランとの合意を）もう終わったと思っている」と述べ事実上のMOU破棄に言及。CENTCOMは7夜連続の空爆で、バンダルハミールの高速道路・鉄道橋（バンダルアッバス港と内陸部を結ぶ要衝）とチャバハール港（対アフガニスタン貿易の要衝）の監視塔を破壊したと発表した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#86efac;font-weight:700;">💰 7/14 JST夜</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

### カード① 外交交渉

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">💰 外交：トランプ大統領、20%通航料を撤回——ガルフ諸国との貿易投資取引に転換／IRGCは「海峡閉鎖の方針維持」を表明</div>
        <div class="s-body">トランプ大統領は表明からわずか1日で20%通航料案を撤回し、「ガルフ諸国が米国に対して行う貿易・投資取引」に置き換えると発表した。同氏は「石油はかつてないほど流れている」と成果を強調したが、対イラン海上封鎖自体は継続する方針を維持している。IRGC海軍幹部は「海峡閉鎖の方針を維持し、侵略者に最も過酷な打撃を加える」と改めて対決姿勢を示した。トランプ氏は「来週はもっと悪くなる——発電所と橋を破壊する」と警告し、CNNはカーグ島制圧を含む作戦拡大の検討をトランプ氏が協議していると報道。ネタニヤフ首相は今週末に訪米しトランプ氏との会談を模索していると伝えられる。</div>
        <div class="s-src">出典: CNBC / Foreign Policy / CNN（7/14〜15 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">💰 外交：MOU「危機段階」入り——トランプ「停戦は終わった」／イラン外務省は米側の義務違反を主張</div>
        <div class="s-body">イラン外務省報道官バゲイー氏は「米イラン間のMOUは危機段階に入った」と述べ、イランが履行していない点があるとすれば米側の義務違反が原因だと主張した。週末のオマーンでの協議はホルムズ海峡の安全通航に限定した内容で、「米国のオマーンへの圧力」により合意に至らなかったとした。トランプ大統領は「（イランとの合意を）もう終わったと思っている」と述べ、事実上MOUの形骸化を認めた形。国連人権高等弁務官テュルク氏は「数百万人が依存する生命線」への打撃に懸念を表明し、双方に即時攻撃停止と停戦復帰を要請した。</div>
        <div class="s-src">出典: ABC News / CNN / 国連人権高等弁務官事務所（7/13〜18 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 軍事情勢

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">⚔️ 軍事：対イラン海上封鎖が発効・5夜連続空爆——カーグ島向けタンカーを新封鎖下で初めて無力化</div>
        <div class="s-body">対イラン海上封鎖は米東部時間7/14午後4時（7/14 20:00 GMT）に正式発効し、CENTCOMは封鎖再開後17時間で商船2隻を進路変更させ、カーグ島へ向かおうとしていた無許可タンカー1隻を無力化したと発表した（新封鎖下で初）。CENTCOMは7/15朝にグレーター・タンブ島の巡航ミサイル拠点等を90分間攻撃、同日午後にも追加攻撃を実施し、対イラン攻撃は5夜連続となった。Kplerによれば7/14の通航実績は21隻とやや持ち直したものの、オマーン沖での攻撃確認件数は累計56件に達したという。</div>
        <div class="s-src">出典: CENTCOM / CNN / Marine Log（7/15 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">⚔️ 軍事：米、7夜連続空爆——ヨルダンで米兵2名戦死・1名不明／イランはクウェート石油施設等を攻撃</div>
        <div class="s-body">CENTCOMは7夜連続で対イラン空爆を実施し「監視施設・軍事兵站インフラ・地下武器庫・海上能力」を標的にしたと発表。バンダルハミールの高速道路・鉄道橋、チャバハール港の監視塔（IRGCが商船追跡に使用）を破壊した。イランはヨルダン・クウェート・バーレーン・カタール・イラク（クルド人自治区）へ報復攻撃を実施し、ヨルダンのムワッファク・サルティ空軍基地への弾道ミサイル・ドローン攻撃で米兵2名が交戦中に戦死・1名が行方不明——3月以来初の米軍戦死者となった。クウェート石油公社は石油部門施設への攻撃で「甚大な物的損害」と負傷者発生を発表。イラン側は直近の米空爆で46名死亡・400名超負傷と発表している。</div>
        <div class="s-src">出典: CENTCOM / NPR / Bloomberg / Air Force Times（7/17〜18 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ 船舶・市場

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし——日本経済界トップ「ホルムズ海峡は当面使えない」／原油は4日続伸</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/16 10:52 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認）。日本貿易会・岡藤正広会長（伊藤忠商事会長）は7/15の定例会見で「ホルムズ海峡はしばらく使えない」と述べ、石油連盟・木藤俊一会長（出光興産会長）も同日「現時点で当てにできない、当てにしない」と表明した。原油はブレント先物が7/15終値で84.95ドル（3日続伸）を付け、WTIは7/16アジア時間も80ドル台で4日続伸。機雷除去は依然未着手のまま7/17の除去期限まで残1日、8/16のMOU最終期限まで残31日に迫っている。</div>
        <div class="s-src">出典: 日本経済新聞 / Trading Economics / OilPrice.com（7/15〜16 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし（7/19再確認）——ホルムズ通航量は3週間ぶり最低水準／原油急伸</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/19 10:17 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。ホルムズ海峡の通航量はMarineTraffic分析によれば7/16(木)にわずか8隻まで落ち込み、3週間ぶりの最低水準を記録した。原油はブレント先物が7/17終値で88.09ドル（一時88.38ドルまで上昇・週間+14%超）を付け、今月の高値圏に迫っている。機雷除去は依然未着手のまま7/17の除去期限を徒過し、8/16のMOU最終期限まで残28日に迫っている。</div>
        <div class="s-src">出典: NPR / TradingEconomics / Investing.com（7/17〜18 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（対イラン海上封鎖発効・5夜連続空爆——トランプは20%通航料を撤回しガルフ投資取引に転換）」——封鎖139日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU事実上崩壊——7夜連続空爆・ヨルダン米兵死亡・クウェート石油施設被弾」——封鎖142日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🚨 <strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換／対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島を攻撃／新封鎖下で初めてカーグ島向けタンカーを無力化・商船2隻を進路変更／IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明／トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も／日本関係船は残り4隻で変化なし——封鎖139日目・MOU機雷除去期限残1日（7/17）・MOU最終期限残31日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①トランプ「来週」発言の実行有無・攻撃対象拡大（発電所・橋梁） ②カーグ島制圧検討の具体化有無 ③IRGCの反撃・海峡閉鎖継続の実効性 ④残る日本関係船4隻の安全確保 ⑤機雷除去着手の有無（期限まで残1日）</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残1日（7/17）</span>
<!-- OLD:END -->
<!-- NEW:START -->
        🚨 <strong>イラン外務省「MOUは危機段階」と表明・トランプ「停戦は終わった」／米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊／イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃——ヨルダン米軍基地攻撃で米兵2名戦死・1名不明（3月以来初）／クウェート石油公社施設に甚大被害／日本関係船は残り4隻で変化なし——封鎖142日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残28日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米軍戦死者の氏名公表とその後の対応 ②イランの追加報復の範囲拡大有無 ③クウェート石油供給への実害の規模 ④MOU正式破棄・全面戦争再開の有無 ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残28日（8/16）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年7月16日 10:52 JST 更新</span><br>
  📊 <strong>対イラン海上封鎖が発効し米軍は5夜連続で空爆継続・新封鎖下で初のタンカー無力化——トランプは20%通航料を撤回しガルフ投資取引に転換する一方、IRGCは海峡閉鎖の維持と「最も過酷な打撃」を表明：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — 封鎖の実運用化・タンカー無力化はMOU核心規定（封鎖解除・海峡開放）とさらに乖離<br>
  🅑 膠着継続 <span style="color:#f87171;">↓</span> — トランプ「来週はもっと悪くなる」発言・カーグ島制圧検討報道により単純な「膠着」の枠を超えつつある<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 通航料は撤回されたが海上封鎖・タンカー無力化は継続——海峡開放条項の空文化がさらに進行<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — 5夜連続空爆・カーグ島制圧検討・「来週さらに悪化」警告により本シナリオへのリスクが最も顕著に高まっている<br>
  <strong style="color:#f87171;">通航料の撤回は経済的な緊張緩和材料だが、軍事的エスカレーション（無力化措置・攻撃対象拡大の警告）は継続しており、C・Dへのリスクシフトは変わらず継続している（A↓ B↓ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月16日 10:52 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>トランプ大統領は20%通航料こそ撤回したが、対イラン海上封鎖・空爆は継続し、新封鎖下で初めてカーグ島向けタンカーを無力化するなど実力行使を強めている。IRGC側も「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と明言しており、双方とも段階的なMOU履行という枠組みからますます乖離している。トランプ氏の「来週はもっと悪くなる」という発言も交渉復帰への圧力である以上に軍事エスカレーションの予告と受け止められており、本シナリオの実現可能性は引き続き低い水準にとどまる。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イラン外務省報道官は米イラン間のMOUが「危機段階に入った」と公言し、トランプ大統領も「（合意を）もう終わったと思っている」と述べるなど、双方が事実上の履行放棄を認め合う状況にある。米軍は7夜連続で空爆を継続し、イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃を行い、ヨルダンでは米兵2名が3月以来初めて戦闘で死亡した。段階的なMOU履行という枠組み自体がほぼ機能を失っており、本シナリオの実現可能性は極めて低い水準にとどまる。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>通航料撤回・貿易投資取引への転換は経済面での一定の軟化シグナルだが、軍事面では5夜連続の空爆・新封鎖下でのタンカー無力化・カーグ島制圧検討報道と、単純な「膠着」では説明しきれない実力行使が積み重なっている。イラン国内では拘束中の米国籍女性の解放という融和的動きも見られるが、IRGCは海峡閉鎖の維持を明言しており、外交と軍事が同時並行するねじれた膠着が続いている。主要海運4社は依然ケープ廻りを継続しており、戦争保険水準が下がる材料は見当たらない。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イランはヨルダン・クウェート・バーレーン・カタール・イラクの5カ国へ同時に報復攻撃を行い、クウェートでは石油公社の施設が「甚大な物的損害」を受けるなど、単純な「膠着」では説明できない規模の実力行使が現実化している。ヨルダンでの米兵戦死は3月以来初めてであり、米軍の直接的な人的損耗が発生した点で従来の膠着状態から質的に変化している。主要海運各社は依然ケープ廻りを継続しており、ホルムズ通航量は7/16に8隻まで落ち込むなど、事態沈静化の材料は見当たらない。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>機雷除去は依然未着手のまま7/17期限（残1日）が目前に迫っている。20%通航料自体は撤回されたが、対イラン海上封鎖は制度として発効・運用が既に始まっており、新封鎖下でのタンカー無力化・商船の進路変更措置は「封鎖の制度化」がまさに現実化していることを示す。IRGC海軍幹部の「海峡閉鎖維持」発言と合わせ、南北両ルートとも実務的な正常化にはほど遠い状態が続いている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>機雷除去はMOU上の7/17期限を未着手のまま徒過し、期限そのものが形骸化した。クウェート石油公社施設への攻撃、チャバハール港監視塔・バンダルハミール橋梁の破壊など、封鎖・攻撃の常態化が着実に進行している。イラン外務省報道官が「MOUは危機段階」と明言したことで、南北両ルートの正常化はさらに遠のいており、通航量の低迷（7/16に8隻のみ）が続く前提での「制度化」がより現実味を帯びている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>CENTCOMは5夜連続で対イラン空爆を継続し、Greater Tunb島への攻撃・新封鎖下でのタンカー無力化と、実力による現状変更が着実に積み上がっている。トランプ大統領は「来週はもっと悪くなる——発電所と橋を破壊する」と攻撃対象の拡大を予告し、カーグ島制圧の検討も報じられている。シナリオCとの差：C=「封鎖・通航管理を巡る制度的対立」、D=「継続的な軍事行動を伴う実力による現状変更・攻撃対象の段階的拡大」。IRGCが「最も過酷な打撃」を予告する中、トランプ氏の警告が実行に移されるかが、本シナリオへの本格移行を左右する分水嶺となる。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>CENTCOMは7夜連続で対イラン空爆を継続し、バンダルハミールの橋梁・チャバハール港監視塔を破壊するなど攻撃対象を段階的に拡大している。イランはヨルダン・クウェート・バーレーン・カタール・イラクへの同時報復攻撃に踏み切り、ヨルダンでは米兵2名が交戦で戦死・1名が行方不明となった——3月以来初めての米軍戦闘死者である。シナリオCとの差：C=「封鎖・通航管理を巡る制度的対立」、D=「米軍の人的損耗を伴う実力による現状変更・攻撃対象の多国間拡大」。米兵戦死という一線を越えたことで、本シナリオへの本格移行リスクは今回の更新で最も顕著に高まっている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5点）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">トランプ「来週はもっと悪くなる」発言の実行有無（発電所・橋梁攻撃）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">カーグ島制圧検討の具体化有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">IRGCの反撃・「海峡閉鎖維持」の実効性</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">機雷除去着手の有無（期限まで残1日）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月16日 10:52 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">戦死した米兵の氏名公表とその後の米側対応</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イランの追加報復の範囲拡大有無（湾岸諸国以外への波及）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">クウェート石油供給への実害の規模と回復状況</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">MOU正式破棄・全面戦争再開の有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月19日 10:17 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## 全ルート現況サマリー（S08完了後）

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月16日 10:52 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンの二経路案の実務協議は事実上停止したまま。10,000dwt超の大型船AIS通航実績は依然乏しく、事実上の通航停止状態が継続。【北ルート（Iran coastline / IRGC管理）】対イラン海上封鎖が7/14夕に正式発効し、CENTCOMは新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更させたと発表。IRGC海軍幹部は「海峡閉鎖の方針を維持する」と表明——南北両ルートとも運用停止に近い状態が継続。CENTCOMは5夜連続の対イラン空爆を継続中（Greater Tunb島等）。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残1日）。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。日本貿易会・岡藤会長、石油連盟・木藤会長ら日本経済界トップも7/15「ホルムズ海峡は当面使えない」との認識を表明。🇯🇵 日本関係船舶：残り4隻で変化なし（7/16 10:52 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月19日 10:17 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンとの実務協議は「危機段階」入りが公式に表明され事実上停止。10,000dwt超の大型船AIS通航実績は依然乏しい。【北ルート（Iran coastline / IRGC管理）】対イラン海上封鎖は継続中。CENTCOMは7夜連続で対イラン空爆を実施しバンダルハミール橋梁・チャバハール港監視塔を破壊——南北両ルートとも運用停止に近い状態が継続。ホルムズ通航量は7/16(木)に8隻まで落ち込み3週間ぶり最低水準（MarineTraffic）。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限は7/17（MOU第5条）を未着手のまま徒過。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃を実施し、クウェート石油公社施設が甚大な被害を受けた。🇯🇵 日本関係船舶：残り4隻で変化なし（7/19 10:17 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（最後に作成）

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
🗣️ トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換——対イラン海上封鎖・空爆は5夜連続で継続。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷 新封鎖下で初めてカーグ島向けタンカーを無力化・IRGC「海峡閉鎖の方針を維持」。日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ トランプ「来週はもっと悪くなる」発言の実行有無・カーグ島制圧検討の行方が焦点、封鎖139日目——機雷除去期限（7/17）まで残1日・MOU最終期限（8/16）まで31日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💰米、20%通航料撤回・ガルフ投資取引へ</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️米、5夜連続空爆・タンカー無力化</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️IRGC「海峡閉鎖維持」・来週更に悪化警告</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント84ドル台・4日続伸</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💥MOU「危機段階」入り・トランプ「停戦は終わった」</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸ヨルダンで米兵2名戦死・1名不明</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️クウェート石油施設に甚大被害</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント88ドル台・週間+14%超</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## SHIP_CONFIG（C01検証済み・変化なし）

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年7月16日 10:52 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。日本貿易会/石油連盟トップは7/15「ホルムズ海峡は当面使えない」と表明）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年7月19日 10:17 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。米イラン停戦覚書は事実上崩壊し軍事衝突が拡大中）'
<!-- NEW:END -->
<!-- APPLY:END -->

---

## JSON-LD dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-16T10:52:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-19T10:17:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

### updated フィールド

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月16日 10:52 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年7月19日 10:17 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列：新規3件を先頭追加 + 既存6件目のisLatestをfalseに整理

> 手順：既存の isLatest:true 付き "latest-blockade-tanker-disabled-0715" の isLatest を false へ変更し、
> 新規3件を先頭に追加。latest配列を6件維持するため、既存の末尾2件
> （"latest-trump-guardian-20pct-toll-0713"・"latest-araghchi-response-imo-oppose-0713"）は
> archiveの新規バッチへ移動する（下記参照）。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-blockade-tanker-disabled-0715",
      "title": "米、新封鎖下で初めてカーグ島向けタンカーを無力化——CENTCOMは5夜連続で対イラン空爆",
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "id": "latest-mou-crisis-stage-0719",
      "title": "イラン外務省「米イラン停戦覚書は危機段階に入った」——トランプ大統領も事実上の破棄を示唆",
      "body": "イラン外務省報道官エスマイル・バゲイー氏は会見で、米イラン間のMOU（覚書）が「危機段階に入った」と発言。イランが履行していない点があるとすれば米側の義務違反が直接の原因だと主張した。週末のオマーンでの協議はホルムズ海峡の安全通航に限定した内容だったが合意に至らず、「米国のオマーンへの公然・非公然の圧力」が原因だと説明した。トランプ大統領も「（イランとの合意を）もう終わったと思っている」と述べ、事実上MOUの形骸化を認めた形となっている。",
      "sourceLabel": "ABC News",
      "date": "2026年7月13日〜18日（現地）/ 2026年7月18日 JST",
      "label": "🕊️ 外交",
      "url": "https://abcnews.com/International/live-updates/iran-live-updates-kuwait-reports-attacks-after-latest/?id=134704698",
      "isLatest": true
    },
    {
      "id": "latest-jordan-us-troops-killed-0718",
      "title": "ヨルダンで米兵2名戦死・1名不明——3月以来初の米軍戦闘死者",
      "body": "米中央軍（CENTCOM）は、7月17日にヨルダンのムワッファク・サルティ空軍基地でイランの弾道ミサイル・ドローン攻撃に対応中、米兵2名が交戦中に死亡したと発表した。1名が現在も行方不明となっているほか、4名がヨルダン国内の病院に搬送されたが既に退院している。米軍の戦闘死者は今年3月以来初めてで、CENTCOMは戦死者の氏名を近親者への通知から24時間経過後に公表するとしている。",
      "sourceLabel": "CNN / Bloomberg",
      "date": "2026年7月17日（現地）/ 2026年7月18日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.cnn.com/2026/07/18/politics/iran-war-us-service-members-killed-jordan",
      "isLatest": false
    },
    {
      "id": "latest-kuwait-oil-facility-attack-0718",
      "title": "クウェート石油公社施設が「甚大な物的損害」——イラン、5カ国へ同時報復攻撃",
      "body": "クウェート石油公社は、石油部門の重要施設がイランの度重なる攻撃を受け「甚大な物的損害」と負傷者が発生したと発表した。同日、イランはヨルダン・バーレーン・カタール・イラク（クルド人自治区）へも攻撃を実施。カタール外務省は「主権・領土保全への重大な違反、国際法違反」だとして最も強い言葉で非難し、ヨルダン軍は7/19未明にもイランのミサイル10発を迎撃したと発表した。",
      "sourceLabel": "Fox News / Al Jazeera",
      "date": "2026年7月18日（現地）/ 2026年7月18日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.foxnews.com/live-news/iran-war-trump-israel-hormuz-oil-july-18-2026",
      "isLatest": false
    },
    {
      "id": "latest-blockade-tanker-disabled-0715",
      "title": "米、新封鎖下で初めてカーグ島向けタンカーを無力化——CENTCOMは5夜連続で対イラン空爆",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest配列 末尾2件をisLatest維持のまま削除（archiveへ移動するため）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "id": "latest-trump-guardian-20pct-toll-0713",
      "title": "トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明",
<!-- OLD:END -->
<!-- NEW:START -->
      "id": "latest-trump-guardian-20pct-toll-0713-archived-marker",
      "title": "【削除対象・手順3参照】トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明",
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ Claude Codeへの補足：上記は一意特定のためのマーカー付けです。実際の適用時は
> grep -n "latest-trump-guardian-20pct-toll-0713\|latest-araghchi-response-imo-oppose-0713" docs/data/news_data.json
> で該当2オブジェクト全体を確認のうえ、latest配列から完全に削除し、
> 内容をそのまま下記の新規archiveバッチ（[S10]archive追加ブロック）へ移設してください
> （id・title・body等の内容は変更せず、isLatestはfalseのまま維持）。

### archive：新規バッチ追加（末尾2件を移設）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "archive": [
    {
      "batchLabel": "2026年7月14日 更新分（アーカイブ）",
<!-- OLD:END -->
<!-- NEW:START -->
  "archive": [
    {
      "batchLabel": "2026年7月16日 更新分（アーカイブ）",
      "items": [
        {
          "id": "latest-trump-guardian-20pct-toll-0713",
          "title": "トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明",
          "body": "（原文は7/16版latest配列より移設。本文はClaude Codeが grep で現行latest配列内の同idオブジェクトの body を確認し、そのままコピーして反映してください。）",
          "sourceLabel": "（原文の値をそのまま維持）",
          "date": "2026年7月13日（現地）/ 2026年7月13日 JST",
          "label": "🚨 封鎖",
          "url": "（原文の値をそのまま維持）",
          "isLatest": false
        },
        {
          "id": "latest-araghchi-response-imo-oppose-0713",
          "title": "アラグチー外相「イランこそ永遠の守護者」と反発——IMOは強制通航料に断固反対",
          "body": "（原文は7/16版latest配列より移設。本文はClaude Codeが grep で現行latest配列内の同idオブジェクトの body を確認し、そのままコピーして反映してください。）",
          "sourceLabel": "（原文の値をそのまま維持）",
          "date": "2026年7月13日（現地）/ 2026年7月13日 JST",
          "label": "🕊️ 外交",
          "url": "（原文の値をそのまま維持）",
          "isLatest": false
        }
      ]
    },
    {
      "batchLabel": "2026年7月14日 更新分（アーカイブ）",
<!-- NEW:END -->
<!-- APPLY:END -->

### osint：新規1件追加（先頭）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "id": "osint-us-attacks-irgc-strikes-live-0715",
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "id": "osint-jordan-strikes-us-troops-live-0718",
      "titleJa": "【Al Jazeera】ヨルダンで米兵2名死亡・1名不明——米、対イラン攻撃7夜目に突入",
      "titleEn": "Two US service members killed in Jordan and another missing",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/18/iran-war-live-us-and-iran-exchange-attacks-for-7th-consecutive-night",
      "date": "2026年7月18日（現地）/ 2026年7月18日 JST",
      "isLatest": true
    },
    {
      "id": "osint-us-attacks-irgc-strikes-live-0715",
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ 既存の "osint-us-attacks-irgc-strikes-live-0715" の isLatest は true → false へ手動変更してください
> （grep -n "osint-us-attacks-irgc-strikes-live-0715" docs/data/news_data.json で該当箇所を確認）。

### staleNotice（変更なし・空文字を維持）

staleNotice は本日進展ありのため空文字 `""` のまま維持（変更不要）。

---

## [S11] 更新ログ追記（2ブロック構成・必須）

### ブロック1：常時表示3件の更新（本日分 + 旧1 + 旧2）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/16 10:52</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明・対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を攻撃・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更・IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明・トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も・米はIRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放・日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明・原油はブレント7/15終値84.95ドル・封鎖139日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月14日 18:00 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/14 18:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE国防省：ホルムズ海峡でタンカー「モンバサ」「アルバヒヤ」がイラン巡航ミサイル攻撃を受けインド人乗組員1人死亡・8人負傷（火災鎮圧）・UKMTOは別のタンカーへの飛翔体着弾も報告（同一事案か未確認）・トランプ大統領、対イラン戦闘は7/7に再開と議会へ正式通知・IRGCがバーレーン米軍レーダー施設破壊・ヨルダン拠点も攻撃と報道・日本関係の原油タンカーは全て通過済みで残り4隻（非タンカー）は変化なし・封鎖137日目・速報ティッカー/速報インシデント更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年7月19日 10:17 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/19 10:17</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省「米イラン停戦覚書は危機段階に入った」と表明・トランプ「停戦は終わった」と言及・米軍は7夜連続で対イラン空爆継続——バンダルハミール橋梁・チャバハール港監視塔を破壊・イランはヨルダン・クウェート・バーレーン・カタール・イラクへ報復攻撃・ヨルダンの米軍基地攻撃で米兵2名戦死・1名行方不明（3月以来初の米軍戦死者）・クウェート石油公社施設に甚大な被害・イラン側発表で直近の米空爆により46名死亡400名超負傷・ホルムズ通航量は7/16に8隻のみで3週間ぶり最低水準・原油はブレント7/17終値88.09ドル（週間+14%超）・日本関係船は残り4隻で変化なし・封鎖142日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/16 10:52</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明・対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を攻撃・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更・IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明・トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も・米はIRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放・日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明・原油はブレント7/15終値84.95ドル・封鎖139日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月14日 18:00 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/14 18:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE国防省：ホルムズ海峡でタンカー「モンバサ」「アルバヒヤ」がイラン巡航ミサイル攻撃を受けインド人乗組員1人死亡・8人負傷（火災鎮圧）・UKMTOは別のタンカーへの飛翔体着弾も報告（同一事案か未確認）・トランプ大統領、対イラン戦闘は7/7に再開と議会へ正式通知・IRGCがバーレーン米軍レーダー施設破壊・ヨルダン拠点も攻撃と報道・日本関係の原油タンカーは全て通過済みで残り4隻（非タンカー）は変化なし・封鎖137日目・速報ティッカー/速報インシデント更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：旧3件目（7/14 16:16）をlog-collapseへ移動・最古1件（7/7）を削除

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月14日 08:48 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月14日 16:16 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/14 16:16</span> — <strong style="color:#fca5a5;">【重大更新】</strong>共同通信：日本関係の原油タンカーは全てホルムズ海峡を通過しペルシャ湾外へ退避したと判明（関係者取材・7/14）・ペルシャ湾内に残る日本関係船舶は原油タンカー以外の4隻で隻数に変化なし（金子国交相7/10会見の水準を維持）・UAE国防省、ホルムズ海峡南部でタンカー2隻がイランのミサイル攻撃を受けインド国籍乗組員1人死亡と発表・米軍は日本時間14日朝から対イラン3日連続空爆を継続・封鎖137日目・ニュース1件更新</div>
          <div>📅 <strong>2026年7月14日 08:48 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：最古エントリー（7/7）を削除（合計件数を10以下に維持）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月7日 09:05 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/07 09:05</span> — <strong style="color:#fca5a5;">【定常確認更新】</strong>故ハメネイ師国葬、本日ゴム追悼式（7/9マシュハド埋葬まで継続）・トランプ「いずれにせよ米国が勝つ」発言（7/6）・オマーン南ルートで商船8隻Uターン（うち4隻イランルートへ変針・7/3〜4）・イランが日本企業へ石油販売を打診（Reuters 7/3）・日本関係船舶31隻で変化なし・ブレント$72割れ/WTI$69割れに続落（OPEC+8月増産・サウジ値下げ）・封鎖130日目・ニュース2件更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

> 📌 補足：ブロック3の適用により log-collapse 内エントリーは 7/14 16:16〜7/8 の8件となり、
> 常時表示3件（7/19・7/16・7/14 18:00）と合わせて合計11件。次回更新時にさらに最古の1件
>（7/8分）を削除するよう申し送りしてください。

---

## Claude Code 確認用コマンド（適用前に必ず実行）

```bash
git pull --rebase
grep -n "dateModified\|badge-date\|totalShips\|SHIP_CONFIG" docs/index.html
grep -n "\"updated\"\|latest-blockade-tanker-disabled-0715\|osint-us-attacks-irgc-strikes-live-0715" docs/data/news_data.json
```

## Claude Code への申し送り事項

1. news_data.json の archive 移設作業（[S10]内の2件）は、grep で現行 latest 配列内の該当2オブジェクト（id: `latest-trump-guardian-20pct-toll-0713` および `latest-araghchi-response-imo-oppose-0713`）の **body・sourceLabel・url を実際の値のままコピー**して archive 側に反映してください（diffs.md内では簡略化のためプレースホルダーにしています）。
2. osint配列の既存先頭アイテム（`osint-us-attacks-irgc-strikes-live-0715`）の `isLatest` を `true` → `false` に変更してください。
3. S11ブロック3適用後、log-collapse内エントリー数が8件（常時表示3件と合わせ合計11件）になるため、次回更新時に最古1件（7/8分）をさらに削除する申し送りを次回diffs.mdに含めます。
4. push は確認後に指示します。commit のみ実施してください。
