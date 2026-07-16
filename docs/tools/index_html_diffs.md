# index_html_diffs.md — 2026年7月16日 10:52 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。news_data.json は [S10] の指示に従いマージしてください。

---

## ✅ 出力前セルフチェック（本日分・原文貼付）

```
[ ] S01 ヘッダー ― 2026年7月16日 10:52 JST に更新したか
[ ] S02 TICKER ― 20%通航料撤回・封鎖発効/5夜連続空爆・タンカー無力化・IRGC発言・トランプ次週警告・封鎖139日目を反映したか
[ ] S03 速報インシデント ― トグル日付・strongタグ・リスト先頭への新規追加を行ったか
[ ] S04 情勢カード3枚 ― 外交/軍事/船舶市場をそれぞれ最新情報に更新したか
[ ] S05 COUNTDOWN ― phase-label・dl-note・次の焦点・機雷除去残日数（残り1日）を更新したか
[ ] S06 シナリオ確率補足バナー ― 日付・矢印・説明文を更新したか
[ ] S07 シナリオ4本 ― A/B/C/D本文を本日情勢に更新したか
[ ] S08 シナリオフッター ― 次の焦点5点を更新したか
[ ] S08.5 全ルート現況サマリー ― 日付・内容を更新したか
[ ] S09 30秒カラム ― 3行サマリー＋ステータスバッジ（最後に作成）を更新したか
[ ] S10 news_data.json ― updated・latest新規3件・アーカイブ移動指示・osint更新を記載したか
[ ] S11 更新ログ ― 2ブロック構成（常時表示3件固定＋log-collapse先頭挿入）で追記したか
[ ] SHIP_CONFIG ― C01確認結果（変化なし）を反映しdateConfirmedを更新したか
[ ] JSON-LD dateModified ― 本日日付に更新したか
[ ] C01 タンカー確認 ― 日本語3クエリ＋英語1クエリを実施したか
[ ] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[ ] 全体 ― ニュースURLにAI捏造・推測URLが混入していないか（web検索確認済みURLのみ使用）
[ ] 全体 ― 📰関連最新ニュースにAl Jazeeraが混入していないか（osint専用）
[ ] 全体 ― 人名が日本語表記になっているか（「Xi」「Trump」単独表記なし）

本日のセルフチェック項目数：19件（すべて✓確認済・下記本文に反映）
```

**C01 タンカー確認（必須・完了）**：日本語クエリ「日本関係船舶 ホルムズ海峡 通過 足止め」「外務省 ホルムズ海峡 日本関係船舶」「金子国交相 ホルムズ海峡 会見」＋英語クエリ「Japanese ships Strait of Hormuz stranded detained July 2026」を実施。→ **変化なし**：ペルシャ湾内の日本関係船舶は引き続き残り4隻（原油タンカー以外）。金子国交相の新規会見・外務省新規発表なし。日本貿易会・岡藤会長（伊藤忠会長）、石油連盟・木藤会長（出光会長）とも7/15の定例会見で「ホルムズ海峡は当面使えない／当てにしない」との認識を表明（news_data.json新規項目に反映）。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明／イランのアラグチー外相は「イランこそ永遠の守護者」と反発しつつ税率交渉に含みを持たせる／IMOは強制通航料に断固反対／米軍は3夜連続の対イラン空爆を継続・封鎖は7/14 20:00 GMT発効予定／封鎖137日目）</span>
    <span class="badge-item badge-date">📅2026年7月14日 18:00 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換する方針に変更／対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を破壊／新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・2隻を進路変更／IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明／トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も／封鎖139日目）</span>
    <span class="badge-item badge-date">📅2026年7月16日 10:52 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月14日 18:00 JST） -->
      🚨【UAE船2隻がイラン巡航ミサイル攻撃・死者】ホルムズ海峡南部・オマーン領海内でUAE国防省の石油タンカー「モンバサ」「アルバヒヤ」が被弾——モンバサの乗組員インド人1人死亡・8人負傷（4人重傷／インド6人・ウクライナ2人）、火災は鎮圧（7/14 JST）｜⚠️ UKMTOは別に、オマーン沖のタンカー1隻が正体不明の飛翔体で機関室に着弾したと発表——UAE発表と同一事案か未確認｜🇦🇪 UAE「あからさまな攻撃」と非難・事態悪化への対応権を留保｜🇺🇸 トランプ大統領、対イラン戦闘が7/7に再開したと米議会へ正式通知｜⚔️ IRGCがバーレーンの米軍レーダー関連施設を破壊・ヨルダンの米軍拠点も攻撃と伝えられる｜🇯🇵 日本関係の原油タンカーは全て通過済み・残る4隻（非タンカー）は変化なし｜💰 対イラン海上封鎖・20%通航料は本日20:00 GMT発効予定｜封鎖137日目
    </span>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月16日 10:52 JST） -->
      🚨【トランプ、20%通航料を撤回】ガルフ諸国との貿易投資取引に転換すると表明——「石油はかつてないほど流れている」（7/14夜JST）｜⚔️ CENTCOM、5夜連続で対イラン空爆——Greater Tunb島の巡航ミサイル拠点等を破壊・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・2隻を進路変更（7/15 JST）｜🗣️ IRGC海軍幹部「海峡閉鎖の方針を維持し、侵略者に最も過酷な打撃を加える」と表明（7/15）｜⚠️ トランプ「来週はもっと悪くなる——発電所と橋を破壊する」と警告・カーグ島制圧検討との報道も（7/15）｜🇺🇸 米、IRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放（7/15）｜🛢️ 原油続伸——ブレント7/15終値84.95ドル・WTIは7/16アジア時間も80ドル台で4日続伸｜🇯🇵 日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明（7/15）｜封鎖139日目
    </span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

**対象：** トグルボタンの日付バッジ＋見出し `<strong>`＋インシデントリスト先頭

### トグルボタン内 見出し＋日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">UAE船2隻がイランのミサイル攻撃を受け船員1人死亡——ホルムズ海峡で緊張最高潮／トランプは対イラン戦闘再開を議会に正式通知</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/14 18:00 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米、5夜連続の対イラン空爆——カーグ島向けタンカーを無力化／トランプは20%通航料を撤回しガルフ投資取引に転換／IRGC「海峡閉鎖を維持」</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/16 10:52 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の `<strong>` タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/14 18:00 速報】UAE国防省：ホルムズ海峡南部でタンカー「モンバサ」「アルバヒヤ」がイラン巡航ミサイル攻撃を受け、モンバサの乗組員インド人1人死亡・8人負傷（火災は鎮圧）｜UKMTOは別のタンカーへの飛翔体着弾も報告（同一事案か未確認）｜トランプ大統領、対イラン戦闘は7/7に再開と議会へ正式通知｜IRGCがバーレーン米軍レーダー施設破壊・ヨルダン拠点も攻撃と報道｜日本関係の原油タンカーは全て通過済み・残る4隻（非タンカー）は変化なし｜封鎖137日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/16 10:52 速報】トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明——「石油はかつてないほど流れている」と主張｜CENTCOM、対イラン空爆を5夜連続実施——Greater Tunb島の巡航ミサイル拠点等を破壊・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・2隻を進路変更｜IRGC海軍幹部「海峡閉鎖の方針を維持し、侵略者に最も過酷な打撃を加える」と表明｜トランプ「来週はもっと悪くなる——発電所と橋を破壊する」と警告・カーグ島制圧検討との報道も｜米、IRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放｜日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明｜封鎖139日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に新規5件を追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#86efac;font-weight:700;">💰 7/14 JST夜</span>
  <span style="color:#e2e8f0;"> トランプ大統領はTruth Social投稿で、前日表明した20%通航料を撤回し「ガルフ諸国が米国に対して行う貿易・投資取引」に置き換えると表明した。「（通航料で得られたはずの収入は）将来の投資でそれ以上に相殺される」とし、投資の具体的な内容には言及しなかった。同氏は「石油はかつてないほど流れている」と述べ、ヘグセス国防長官・ケイン統合参謀本部議長・CENTCOMクーパー司令官の功績を称えた。対イラン海上封鎖自体は継続する方針に変わりはない。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/15 JST</span>
  <span style="color:#e2e8f0;"> 対イラン海上封鎖は米東部時間7/14午後4時（7/14 20:00 GMT）に正式発効。CENTCOMは米東部時間7/15午前6時から90分間、ホルムズ海峡西側入口付近のグレーター・タンブ島で沿岸防衛システム・巡航ミサイル貯蔵/発射拠点を攻撃したと発表し、対艦攻撃能力の低下を継続的に図った。同日午後にはバンダルアッバス等を含む複数拠点への追加攻撃を実施し、対イラン攻撃は5夜連続となった。CENTCOMはまた、封鎖再開後17時間で無許可通航を試みた商船2隻を進路変更させたと発表し、カーグ島（イラン最大の原油輸出拠点）へ向かおうとしていた無人（乗員退避済み）の石油タンカー1隻を無力化したと明らかにした——新封鎖下で初の無力化措置となる。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🗣️ 7/15 JST</span>
  <span style="color:#e2e8f0;"> IRGC海軍幹部アリ・オズマイ氏はX投稿で「（最高指導者の指示に応え）ホルムズ海峡閉鎖の方針を維持しつつ、侵略者たる敵に最も過酷な打撃を加える」と表明し、対米強硬姿勢を改めて示した。IRGCは同日、クウェートの米衛星通信センター・パトリオット防空システム・HIMARSミサイル発射拠点等を標的に新たな攻撃を実施したと発表（CENTCOMは成否未確認）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fca5a5;font-weight:700;">⚠️ 7/15 JST</span>
  <span style="color:#e2e8f0;"> トランプ大統領はFox Newsのインタビューで「今夜も、明日の夜も強く攻撃する。そして来週はもっと悪くなる——発電所を破壊し、橋を破壊する」と述べ、イランが交渉のテーブルに戻らない限り攻撃を段階的に拡大すると警告した。CNNは複数の関係者の話として、トランプ氏が軍事作戦の拡大選択肢を検討しており、イラン最大の原油輸出拠点であるカーグ島の制圧も協議対象に含まれていると報じた。米政権はカーグ島作戦の実施を正式発表しておらず、トランプ氏自身の発言も計画の確認には至っていない。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🇺🇸 7/15 JST</span>
  <span style="color:#e2e8f0;"> 米国務省は、IRGCの兵器調達を支援したとして個人4名・団体3法人に新規制裁を科したと発表。米財務省も別途イラン中央銀行に関連する暗号資産ウォレットを制裁し1億3000万ドル超を凍結したほか、石油密輸に関与したとされる海運業者関連50の個人・団体・船舶を追加制裁した。一方でトランプ大統領は、2024年12月からイランに拘束されていた米国籍女性デナ・カラリ氏（Children of Mehr Foundation創設者）が解放されたと発表し「善意の表れに感謝する」と投稿した。</span>
</li>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 最新情勢カード（3枚）

### カード① 外交

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">💰 外交：トランプ大統領「米国がホルムズ海峡の守護者」宣言・全貨物20%通航料を表明——イランは反発しつつ税率交渉に含み</div>
        <div class="s-body">トランプ大統領はTruth Social投稿とFox Newsのインタビューで、対イラン海上封鎖の再開と、米国が「ホルムズ海峡の守護者」となって同海峡を通過する全貨物の20%を安全確保の対価として徴収する方針を表明した。イランのアラグチー外相はX投稿で「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる、公正にする」と税率交渉の余地を示唆。イラン軍ハタム・アル・アンビヤ司令部は米国の海峡管理への干渉を一切許さないと強調した。国連IMOは強制的な通航料導入に法的根拠なしとして断固反対を表明し、中国外務省も安全な航行確保を関係国に要求した。</div>
        <div class="s-src">出典: Al Jazeera / CNBC / ニューズウィーク日本版（7/13〜14 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">💰 外交：トランプ大統領、20%通航料を撤回——ガルフ諸国との貿易投資取引に転換／IRGCは「海峡閉鎖の方針維持」を表明</div>
        <div class="s-body">トランプ大統領は表明からわずか1日で20%通航料案を撤回し、「ガルフ諸国が米国に対して行う貿易・投資取引」に置き換えると発表した。同氏は「石油はかつてないほど流れている」と成果を強調したが、対イラン海上封鎖自体は継続する方針を維持している。IRGC海軍幹部は「海峡閉鎖の方針を維持し、侵略者に最も過酷な打撃を加える」と改めて対決姿勢を示した。トランプ氏は「来週はもっと悪くなる——発電所と橋を破壊する」と警告し、CNNはカーグ島制圧を含む作戦拡大の検討をトランプ氏が協議していると報道。ネタニヤフ首相は今週末に訪米しトランプ氏との会談を模索していると伝えられる。</div>
        <div class="s-src">出典: CNBC / Foreign Policy / CNN（7/14〜15 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 軍事情勢

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">⚔️ 軍事：米軍、3夜連続の対イラン空爆を継続——海上封鎖は本日7/14 20:00 GMTに発効予定</div>
        <div class="s-body">CENTCOMは米東部時間7/13午後4時45分、トランプ大統領の指示の下「今週3夜連続」となる対イラン空爆を開始したと発表し、イランの対艦ミサイル能力・商船攻撃能力の低下を継続的に図ると強調した。同日発表された対イラン海上封鎖は米東部時間7/14午後4時（7/14 20:00 GMT）に発効予定で、4/13〜6/18に続く2度目の封鎖再開となる。データ分析企業Kplerによれば、ホルムズ海峡の通航実績は前週比で半分以下に減少しているという。</div>
        <div class="s-src">出典: CENTCOM / NPR・KPBS / Axios（7/13 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">⚔️ 軍事：対イラン海上封鎖が発効・5夜連続空爆——カーグ島向けタンカーを新封鎖下で初めて無力化</div>
        <div class="s-body">対イラン海上封鎖は米東部時間7/14午後4時（7/14 20:00 GMT）に正式発効し、CENTCOMは封鎖再開後17時間で商船2隻を進路変更させ、カーグ島へ向かおうとしていた無許可タンカー1隻を無力化したと発表した（新封鎖下で初）。CENTCOMは7/15朝にグレーター・タンブ島の巡航ミサイル拠点等を90分間攻撃、同日午後にも追加攻撃を実施し、対イラン攻撃は5夜連続となった。Kplerによれば7/14の通航実績は21隻とやや持ち直したものの、オマーン沖での攻撃確認件数は累計56件に達したという。</div>
        <div class="s-src">出典: CENTCOM / CNN / Marine Log（7/15 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ エネルギー・市場

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし——原油はブレント一時83ドル台まで急伸</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/14 08:48 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認）。日本経済新聞によれば日本関係の原油タンカーはすでに全てホルムズ海峡を通過済みだが、封鎖再開により今後の正常化の見通しは不透明という。原油はトランプ大統領の封鎖再開・通航料表明を受け週明けの取引で急伸し、ブレント先物は7/13終値で前日比3.74%高の78.85ドルを付けた後、同日夜の取引で一時83ドル台まで上昇。機雷除去は依然未着手のまま7/17の除去期限まで残3日、8/16のMOU最終期限まで残33日に迫っている。</div>
        <div class="s-src">出典: 日本経済新聞 / CNBC / Trading Economics（7/13〜14 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし——日本経済界トップ「ホルムズ海峡は当面使えない」／原油は4日続伸</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/16 10:52 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認）。日本貿易会・岡藤正広会長（伊藤忠商事会長）は7/15の定例会見で「ホルムズ海峡はしばらく使えない」と述べ、石油連盟・木藤俊一会長（出光興産会長）も同日「現時点で当てにできない、当てにしない」と表明した。原油はブレント先物が7/15終値で84.95ドル（3日続伸）を付け、WTIは7/16アジア時間も80ドル台で4日続伸。機雷除去は依然未着手のまま7/17の除去期限まで残1日、8/16のMOU最終期限まで残31日に迫っている。</div>
        <div class="s-src">出典: 日本経済新聞 / Trading Economics / OilPrice.com（7/15〜16 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（米、対イラン海上封鎖の再開と20%通航料を宣言——イランは反発しつつ税率交渉に含み）」——封鎖137日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（対イラン海上封鎖発効・5夜連続空爆——トランプは20%通航料を撤回しガルフ投資取引に転換）」——封鎖139日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🚨 <strong>トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明（封鎖発効は7/14 20:00 GMT予定）／アラグチー外相「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる」と税率交渉に含み／IMOは強制通航料に断固反対／米軍は3夜連続の対イラン空爆を継続／日本関係船は残り4隻で変化なし——封鎖137日目・MOU機雷除去期限残3日（7/17）・MOU最終期限残33日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①封鎖の正式発効と実際の運用実態（7/14 20:00 GMT〜）②20%通航料の実効性・IMO/主要海運国の反応 ③これ以上の軍事応酬拡大の有無 ④残る日本関係船4隻の安全確保 ⑤機雷除去着手の有無（期限まで残3日）</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残3日（7/17）</span>
<!-- OLD:END -->
<!-- NEW:START -->
        🚨 <strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換／対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島を攻撃／新封鎖下で初めてカーグ島向けタンカーを無力化・商船2隻を進路変更／IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明／トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も／日本関係船は残り4隻で変化なし——封鎖139日目・MOU機雷除去期限残1日（7/17）・MOU最終期限残31日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①トランプ「来週」発言の実行有無・攻撃対象拡大（発電所・橋梁） ②カーグ島制圧検討の具体化有無 ③IRGCの反撃・海峡閉鎖継続の実効性 ④残る日本関係船4隻の安全確保 ⑤機雷除去着手の有無（期限まで残1日）</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残1日（7/17）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年7月14日 08:48 JST 更新</span><br>
  📊 <strong>トランプ大統領が対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言、全貨物の20%通航料徴収を表明——イランは反発しつつ税率交渉に含みを持たせ、IMOは強制通航料に断固反対：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — 封鎖再開・一方的通航料宣言はMOUの核心規定（封鎖解除・海峡開放）を正面から覆すもの<br>
  🅑 膠着継続 <span style="color:#f87171;">↓</span> — 「膠着」を超え、双方が海峡の管理権・課金権を巡り制度そのものを奪い合う新局面に移行<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 封鎖の正式再開・一方的通航料宣言により、MOUの海峡開放条項は事実上完全に空文化<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — 3夜連続の対イラン空爆継続下での封鎖再開発効（7/14 20:00 GMT予定）——軍事・経済両面での対立が同時進行<br>
  <strong style="color:#f87171;">封鎖の正式再開と一方的通航料宣言により、外交解決（A）・膠着継続（B）双方の前提がさらに崩れ、C・Dへのリスクシフトが継続している（A↓ B↓ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月14日 08:48 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ本文（A〜D）

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>トランプ大統領は対イラン海上封鎖の再開に加え、米国が「ホルムズ海峡の守護者」として全貨物の20%を通航料として徴収する方針を一方的に表明した。これはMOUが本来目指していた封鎖解除・海峡自由開放という前提そのものを覆すものであり、イラン側も税率を巡り交渉の余地を示しつつも「イランこそ守護者」と対抗する姿勢を崩していない。段階的なMOU履行という枠組みは事実上機能を停止しており、本シナリオの実現可能性はさらに一段と後退している。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>トランプ大統領は20%通航料こそ撤回したが、対イラン海上封鎖・空爆は継続し、新封鎖下で初めてカーグ島向けタンカーを無力化するなど実力行使を強めている。IRGC側も「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と明言しており、双方とも段階的なMOU履行という枠組みからますます乖離している。トランプ氏の「来週はもっと悪くなる」という発言も交渉復帰への圧力である以上に軍事エスカレーションの予告と受け止められており、本シナリオの実現可能性は引き続き低い水準にとどまる。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>単純な「交渉と衝突の併存」という膠着状態は、トランプ大統領の封鎖再開・一方的通航料宣言によって新たな局面に移行しつつある。海峡の管理権・課金権そのものを巡る制度的な奪い合いが表面化しており、従来の「膠着」という言葉では実態を説明しきれなくなっている。主要海運4社（Maersk・MSC・CMA CGM・Hapag-Lloyd）は依然ケープ廻りを継続しており、戦争保険水準が下がる材料も見当たらない。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>通航料撤回・貿易投資取引への転換は経済面での一定の軟化シグナルだが、軍事面では5夜連続の空爆・新封鎖下でのタンカー無力化・カーグ島制圧検討報道と、単純な「膠着」では説明しきれない実力行使が積み重なっている。イラン国内では拘束中の米国籍女性の解放という融和的動きも見られるが、IRGCは海峡閉鎖の維持を明言しており、外交と軍事が同時並行するねじれた膠着が続いている。主要海運4社は依然ケープ廻りを継続しており、戦争保険水準が下がる材料は見当たらない。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>機雷除去は依然未着手のまま7/17期限（残3日）が目前に迫っている。トランプ大統領による対イラン海上封鎖の正式再開と、米国が徴収主体となる20%通航料の一方的宣言は、MOUが目指した「海峡自由開放」を制度面から覆すものであり、本シナリオが想定する「封鎖の制度化」がまさに現実化しつつある。IMOが強制通航料に断固反対を表明していることも、国際的な制度対立の深刻化を裏付けている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>機雷除去は依然未着手のまま7/17期限（残1日）が目前に迫っている。20%通航料自体は撤回されたが、対イラン海上封鎖は制度として発効・運用が既に始まっており、新封鎖下でのタンカー無力化・商船の進路変更措置は「封鎖の制度化」がまさに現実化していることを示す。IRGC海軍幹部の「海峡閉鎖維持」発言と合わせ、南北両ルートとも実務的な正常化にはほど遠い状態が続いている。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>CENTCOMは3夜連続で対イラン空爆を継続しており、これに加えて対イラン海上封鎖が本日7/14 20:00 GMTに正式発効する予定である。シナリオCとの差：C=「通航料・海峡管理を巡る制度的対立」、D=「継続的な軍事行動を伴う実力による現状変更」。今回は軍事・経済両面での対立が同時進行しており、直近で最も高いリスク水準にある。封鎖発効後の実際の運用実態と、イランがこれに軍事的に反応するかが、本シナリオへの本格移行を左右する分水嶺となる。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>CENTCOMは5夜連続で対イラン空爆を継続し、Greater Tunb島への攻撃・新封鎖下でのタンカー無力化と、実力による現状変更が着実に積み上がっている。トランプ大統領は「来週はもっと悪くなる——発電所と橋を破壊する」と攻撃対象の拡大を予告し、カーグ島制圧の検討も報じられている。シナリオCとの差：C=「封鎖・通航管理を巡る制度的対立」、D=「継続的な軍事行動を伴う実力による現状変更・攻撃対象の段階的拡大」。IRGCが「最も過酷な打撃」を予告する中、トランプ氏の警告が実行に移されるかが、本シナリオへの本格移行を左右する分水嶺となる。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター「次の焦点5つ」

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">封鎖の正式発効と実際の運用実態（7/14 20:00 GMT〜）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">20%通航料の実効性・IMO/主要海運国の反応</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">これ以上の軍事応酬拡大の有無（追加の報復・反撃）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">機雷除去着手の有無（期限まで残3日）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月14日 08:48 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">トランプ「来週はもっと悪くなる」発言の実行有無（発電所・橋梁攻撃）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">カーグ島制圧検討の具体化有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">IRGCの反撃・「海峡閉鎖維持」の実効性</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">機雷除去着手の有無（期限まで残1日）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月16日 10:52 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月14日 08:48 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンの二経路案の実務協議は事実上停止したまま。7/7以降10,000dwt超の大型船AIS通航実績はなく、事実上の通航停止状態が継続。【北ルート（Iran coastline / IRGC管理）】ホルムズ海峡「閉鎖」宣言が続く中、トランプ大統領が対イラン海上封鎖の再開と20%通航料の一方的徴収を宣言（7/14 20:00 GMT発効予定）——南北両ルートとも運用停止に近い状態が継続。CENTCOMは3夜連続の対イラン空爆を継続中。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残3日）。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。戦争保険水準・ルート法的不確実性が解消されるまで復帰なし。🇯🇵 日本関係船舶：残り4隻で変化なし（7/14 08:48 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月16日 10:52 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンの二経路案の実務協議は事実上停止したまま。10,000dwt超の大型船AIS通航実績は依然乏しく、事実上の通航停止状態が継続。【北ルート（Iran coastline / IRGC管理）】対イラン海上封鎖が7/14夕に正式発効し、CENTCOMは新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更させたと発表。IRGC海軍幹部は「海峡閉鎖の方針を維持する」と表明——南北両ルートとも運用停止に近い状態が継続。CENTCOMは5夜連続の対イラン空爆を継続中（Greater Tunb島等）。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残1日）。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。日本貿易会・岡藤会長、石油連盟・木藤会長ら日本経済界トップも7/15「ホルムズ海峡は当面使えない」との認識を表明。🇯🇵 日本関係船舶：残り4隻で変化なし（7/16 10:52 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒で全体像を把握（3行サマリー＋ステータスバッジ）― 最後に作成

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🗣️ トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷 アラグチー外相「イランこそ永遠の守護者」と反発しつつ税率交渉に含み。日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 封鎖の正式発効（7/14 20:00 GMT）と20%通航料の実効性が焦点、封鎖137日目——機雷除去期限（7/17）まで残3日・MOU最終期限（8/16）まで33日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
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
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💰米、対イラン封鎖再開・20%通航料</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️米、3夜連続で空爆継続</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️イラン、税率交渉に含み・IMOは反対</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント一時83ドル台</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💰米、20%通航料撤回・ガルフ投資取引へ</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️米、5夜連続空爆・タンカー無力化</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️IRGC「海峡閉鎖維持」・来週更に悪化警告</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント84ドル台・4日続伸</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [SHIP_CONFIG] 日本関連タンカー足止め可視化（C01再確認・変化なし）

<!-- APPLY:START -->
<!-- OLD:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年7月14日 16:16 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認）'
};
<!-- OLD:END -->
<!-- NEW:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年7月16日 10:52 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。日本貿易会/石油連盟トップは7/15「ホルムズ海峡は当面使えない」と表明）'
};
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [JSON-LD] dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-14T18:00:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-16T10:52:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

### updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月14日 16:16 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年7月16日 10:52 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列（新規3件を先頭に追加・isLatestフラグ移動・最古3件をアーカイブへ移動）

latest は現在6件（`latest-japan-tankers-all-transited-0714` に isLatest:true）。新規3件を先頭に追加すると9件になるため、
Claude Code は既存の最も古い3件（`latest-oil-surge-83dollar-0713`・`latest-iran-attacks-5states-0712`・`latest-oman-summons-iran-ambassador-0712`）を
新規アーカイブバッチ「2026年7月14日 更新分（アーカイブ）」として `archive` 配列の先頭に移動してください（本文は既存ファイルのまま転記）。
また、現在 `isLatest: true` の `latest-japan-tankers-all-transited-0714` は `isLatest: false` に変更してください。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-japan-tankers-all-transited-0714",
      "title": "日本関係の原油タンカー、全てホルムズ海峡を通過——残る4隻は非タンカー船",
      "body": "関係者への取材で14日、日本関係船舶のうち原油タンカーは全てホルムズ海峡を通過し、ペルシャ湾外へ退避したことが判明した。船舶位置情報の追跡データによると、商船三井系のタンカーなどが14日までに通過したとみられ、日本へ向かっている船もあるとみられる。現在ペルシャ湾内に残る日本関係船舶は原油タンカー以外の4隻で、金子国土交通相が10日の会見で発表した隻数からの変化はない。トランプ大統領がホルムズ海峡通航貨物の20%相当を安全確保の対価として徴収する方針を表明するなど、情勢の混乱は続いている。",
      "sourceLabel": "共同通信 / 日本海新聞",
      "date": "2026年7月14日 JST",
      "label": "🇯🇵 邦人・船舶",
      "url": "https://news.yahoo.co.jp/articles/b43aa6b7fa6a8027bec7ecb1fb1bfed60e62beb4",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "id": "latest-blockade-tanker-disabled-0715",
      "title": "米、新封鎖下で初めてカーグ島向けタンカーを無力化——CENTCOMは5夜連続で対イラン空爆",
      "body": "対イラン海上封鎖は米東部時間7/14午後4時（7/14 20:00 GMT）に正式発効し、CENTCOMは発効から17時間で無許可通航を試みた商船2隻を進路変更させ、イラン最大の原油輸出拠点カーグ島へ向かおうとしていた無人（乗員退避済み）の石油タンカー1隻を無力化したと発表した。新封鎖下での無力化措置は初めて。CENTCOMは7/15朝にはホルムズ海峡西側入口付近のグレーター・タンブ島で沿岸防衛システム・巡航ミサイル拠点を90分間攻撃し、対イラン攻撃は5夜連続となった。IRGC海軍幹部は「海峡閉鎖の方針を維持し、侵略者に最も過酷な打撃を加える」とX投稿で表明した。",
      "sourceLabel": "CENTCOM / CNN / Marine Log",
      "date": "2026年7月15日（現地）/ 2026年7月15日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.cnn.com/2026/07/15/world/live-news/iran-war-trump",
      "isLatest": true
    },
    {
      "id": "latest-trump-toll-reversal-0714",
      "title": "トランプ大統領、20%通航料を撤回——ガルフ諸国との貿易投資取引に転換",
      "body": "トランプ大統領は表明からわずか1日で、ホルムズ海峡通過貨物への20%通航料案を撤回し「ガルフ諸国が米国に対して行う貿易・投資取引」に置き換えると発表した。「投資は莫大なものになるが、彼らにとっても極めて良い話だ」とし、具体的な投資内容には言及しなかった。同氏は「石油はかつてないほど流れている」と成果を強調し、ヘグセス国防長官・ケイン統合参謀本部議長・CENTCOMクーパー司令官の功績を称えた。対イラン海上封鎖自体は継続する方針に変わりはない。",
      "sourceLabel": "CNBC / Foreign Policy",
      "date": "2026年7月14日（現地）/ 2026年7月14日 JST",
      "label": "💰 経済・封鎖",
      "url": "https://www.cnbc.com/2026/07/15/cnbc-daily-open-trump-hormuz-fees-us-stocks-tech-fed.html",
      "isLatest": false
    },
    {
      "id": "latest-japan-business-hormuz-offlimits-0715",
      "title": "日本貿易会・石油連盟トップ「ホルムズ海峡は当面使えない」——日本経済界が長期化を前提とした見方を表明",
      "body": "日本貿易会の岡藤正広会長（伊藤忠商事会長）は7/15の定例会見で、中東情勢に関して「ホルムズ海峡はしばらく使えない」と述べ、中長期的な視点でのサプライチェーン再構築の必要性を訴えた。石油連盟の木藤俊一会長（出光興産会長）も同日の定例会見で、海峡経由の原油調達再開について「現時点で当てにできない、当てにしない」との認識を示した。両会長とも、米イラン戦争が終結しない限り根本的な解決には至らないとの見方を共有している。",
      "sourceLabel": "日本経済新聞",
      "date": "2026年7月15日 JST",
      "label": "🇯🇵 邦人・船舶",
      "url": "https://www.nikkei.com/article/DGXZQOUC14B4Z0U6A710C2000000/",
      "isLatest": false
    },
    {
      "id": "latest-japan-tankers-all-transited-0714",
      "title": "日本関係の原油タンカー、全てホルムズ海峡を通過——残る4隻は非タンカー船",
      "body": "関係者への取材で14日、日本関係船舶のうち原油タンカーは全てホルムズ海峡を通過し、ペルシャ湾外へ退避したことが判明した。船舶位置情報の追跡データによると、商船三井系のタンカーなどが14日までに通過したとみられ、日本へ向かっている船もあるとみられる。現在ペルシャ湾内に残る日本関係船舶は原油タンカー以外の4隻で、金子国土交通相が10日の会見で発表した隻数からの変化はない。トランプ大統領がホルムズ海峡通航貨物の20%相当を安全確保の対価として徴収する方針を表明するなど、情勢の混乱は続いている。",
      "sourceLabel": "共同通信 / 日本海新聞",
      "date": "2026年7月14日 JST",
      "label": "🇯🇵 邦人・船舶",
      "url": "https://news.yahoo.co.jp/articles/b43aa6b7fa6a8027bec7ecb1fb1bfed60e62beb4",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

### osint（現地メディア視点）最新1件を追加・既存isLatestをfalseへ

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "id": "osint-trump-guardian-toll-live-0713",
      "titleJa": "【Al Jazeera】トランプ大統領、対イラン封鎖再開と「ホルムズ海峡の守護者」宣言を受け米が新たな空爆を実施",
      "titleEn": "Iran war live: US carrying out new attacks on Iran after Trump's threats",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/13/iran-war-live-us-bombs-iranian-cities-again-as-hormuz-standoff-intensifies",
      "date": "2026年7月13日（現地）/ 2026年7月13日 JST",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "id": "osint-us-attacks-irgc-strikes-live-0715",
      "titleJa": "【Al Jazeera】米、対イラン攻撃継続——IRGCは湾岸の米軍拠点への攻撃を主張",
      "titleEn": "US attacks Iran as IRGC claims strikes on US military sites in Gulf",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/2026/7/15/us-attacks-iran-as-irgc-claims-strikes-on-us-military-sites-in-gulf",
      "date": "2026年7月15日（現地）/ 2026年7月15日 JST",
      "isLatest": true
    },
    {
      "id": "osint-trump-guardian-toll-live-0713",
      "titleJa": "【Al Jazeera】トランプ大統領、対イラン封鎖再開と「ホルムズ海峡の守護者」宣言を受け米が新たな空爆を実施",
      "titleEn": "Iran war live: US carrying out new attacks on Iran after Trump's threats",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/13/iran-war-live-us-bombs-iranian-cities-again-as-hormuz-standoff-intensifies",
      "date": "2026年7月13日（現地）/ 2026年7月13日 JST",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S11] 更新ログ追記（2ブロック構成・必須）

### ブロック1: 常時表示エリア（3件固定を維持）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年7月14日 18:00 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/14 18:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE国防省：ホルムズ海峡でタンカー「モンバサ」「アルバヒヤ」がイラン巡航ミサイル攻撃を受けインド人乗組員1人死亡・8人負傷（火災鎮圧）・UKMTOは別のタンカーへの飛翔体着弾も報告（同一事案か未確認）・トランプ大統領、対イラン戦闘は7/7に再開と議会へ正式通知・IRGCがバーレーン米軍レーダー施設破壊・ヨルダン拠点も攻撃と報道・日本関係の原油タンカーは全て通過済みで残り4隻（非タンカー）は変化なし・封鎖137日目・速報ティッカー/速報インシデント更新</div>
        <div>📅 <strong>2026年7月14日 16:16 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/14 16:16</span> — <strong style="color:#fca5a5;">【重大更新】</strong>共同通信：日本関係の原油タンカーは全てホルムズ海峡を通過しペルシャ湾外へ退避したと判明（関係者取材・7/14）・ペルシャ湾内に残る日本関係船舶は原油タンカー以外の4隻で隻数に変化なし（金子国交相7/10会見の水準を維持）・UAE国防省、ホルムズ海峡南部でタンカー2隻がイランのミサイル攻撃を受けインド国籍乗組員1人死亡と発表・米軍は日本時間14日朝から対イラン3日連続空爆を継続・封鎖137日目・ニュース1件更新</div>
        <div>📅 <strong>2026年7月14日 08:48 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/14 08:48</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明（封鎖発効は7/14 20:00 GMT予定）・アラグチー外相「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる」と税率交渉に含み・イラン軍ハタム・アル・アンビヤ司令部は米国の海峡管理への干渉を許さないと強調・IMOは強制通航料に法的根拠なしとして断固反対・中国外務省も安全な航行確保を要求・米軍は3夜連続の対イラン空爆を継続・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント7/13終値78.85ドル（+3.74%）後、同日夜一時83ドル台まで急伸・封鎖137日目・ニュース3件更新・osint更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年7月16日 10:52 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/16 10:52</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、20%通航料を撤回しガルフ諸国との貿易投資取引に転換すると表明・対イラン海上封鎖は7/14夕発効・米軍は5夜連続の対イラン空爆を継続しGreater Tunb島の巡航ミサイル拠点等を攻撃・新封鎖下で初めてカーグ島向け無許可タンカー1隻を無力化・商船2隻を進路変更・IRGC海軍幹部「海峡閉鎖の方針を維持し最も過酷な打撃を加える」と表明・トランプ「来週はもっと悪くなる」と発電所・橋梁攻撃を警告・カーグ島制圧検討との報道も・米はIRGC武器調達関連に追加制裁・イランは拘束中の米国籍女性を解放・日本関係船は残り4隻で変化なし・日本貿易会/石油連盟トップが「ホルムズ海峡は当面使えない」と表明・原油はブレント7/15終値84.95ドル・封鎖139日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月14日 18:00 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/14 18:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE国防省：ホルムズ海峡でタンカー「モンバサ」「アルバヒヤ」がイラン巡航ミサイル攻撃を受けインド人乗組員1人死亡・8人負傷（火災鎮圧）・UKMTOは別のタンカーへの飛翔体着弾も報告（同一事案か未確認）・トランプ大統領、対イラン戦闘は7/7に再開と議会へ正式通知・IRGCがバーレーン米軍レーダー施設破壊・ヨルダン拠点も攻撃と報道・日本関係の原油タンカーは全て通過済みで残り4隻（非タンカー）は変化なし・封鎖137日目・速報ティッカー/速報インシデント更新</div>
        <div>📅 <strong>2026年7月14日 16:16 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/14 16:16</span> — <strong style="color:#fca5a5;">【重大更新】</strong>共同通信：日本関係の原油タンカーは全てホルムズ海峡を通過しペルシャ湾外へ退避したと判明（関係者取材・7/14）・ペルシャ湾内に残る日本関係船舶は原油タンカー以外の4隻で隻数に変化なし（金子国交相7/10会見の水準を維持）・UAE国防省、ホルムズ海峡南部でタンカー2隻がイランのミサイル攻撃を受けインド国籍乗組員1人死亡と発表・米軍は日本時間14日朝から対イラン3日連続空爆を継続・封鎖137日目・ニュース1件更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2: log-collapse への旧3件目（7/14 08:48）の挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月13日 08:28 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月14日 08:48 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/14 08:48</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明（封鎖発効は7/14 20:00 GMT予定）・アラグチー外相「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる」と税率交渉に含み・イラン軍ハタム・アル・アンビヤ司令部は米国の海峡管理への干渉を許さないと強調・IMOは強制通航料に法的根拠なしとして断固反対・中国外務省も安全な航行確保を要求・米軍は3夜連続の対イラン空爆を継続・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント7/13終値78.85ドル（+3.74%）後、同日夜一時83ドル台まで急伸・封鎖137日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年7月13日 08:28 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ ブロック2適用後、常時表示3件＋log-collapse内エントリー数の合計は11件（3＋8）になる。10件を超えるため、次回更新時に log-collapse 最古エントリー（2026年7月7日 09:05 JST分）を削除し `update_log.json` へ移動する対応を検討してください（今回は許容範囲内のためスキップ可）。

---

## 📌 Claude Code への申し送り事項

- `docs/data/update_log.json` の先頭にも本日分（2026/07/16 10:52）のエントリを追加し、[S11] ブロック1・2 の内容と一致させてください。
- news_data.json のマージ後、`latest` 配列が9件になっていないか（6件+新規3件-アーカイブ移動3件=6件が正しい）を確認してください。
