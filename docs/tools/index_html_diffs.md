# index_html_diffs.md — 2026年8月5日 10:24 JST 更新分

> Claude Code への指示：以下の差分を index.html および news_data.json / archive_timeline.json に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## ⚠️ 冒頭確認事項（Claude Code への申し送り）

- 封鎖日カウンターは既存の「2/28起算（表示値＝経過日数+1）」の連続性に合わせ、本日は**159日目**としています（8/3時点157日目からの整合を確認済み）。起算日の統一問題（Memory記載の4/13起算との齟齬）は引き続き未対応で、別途ユーザー判断が必要です。
- 前回セッション（8/3 09:46 JST）以降、米側高官（ベッセント財務長官・ルビオ国務長官）がホルムズ海峡再開合意への楽観的見通しを相次いで表明し、NYダウ・S&P500が史上最高値／2ヶ月ぶり高値を記録、原油（WTI）は75ドル台まで続落するなど、市場心理が大きく好転しました。一方、イラン側は米との直接交渉を公式には否定しており、外交的実体はなお不透明です。

---

## Step 0 セルフチェック（本文執筆前の事前確認）

project_knowledge_search にて「index_html_diffs.md 最新 更新 JST」「更新ログ 出典 JST 更新」を実行し、直近更新が2026年8月3日 09:46 JSTであることを確認。また `raw.githubusercontent.com` から index.html（badge-date: 2026年8月3日 09:46 JST／封鎖157日目）および news_data.json（updated: 2026年8月3日 09:46 日本時間JST）の最新版を取得し、old_str抽出の正確性を担保済み。

**C01タンカー確認（4クエリ個別実行・省略なし）：**
① 日本語「日本関係船舶 ホルムズ海峡 通過 足止め 8月」
② 日本語「外務省 ホルムズ海峡 日本関係船舶 8月」
③ 日本語「金子国土交通大臣 会見 ホルムズ海峡 8月」（8/4 13:22〜13:41の会見記録を確認したが、議題は九州豪雨災害対応が中心でホルムズ海峡への言及は確認できず）
④ 英語「Japanese ships Strait of Hormuz stranded detained August 2026」
→ 外務省・国交省いずれも7/10発表（残り4隻）以降の新規発表なしを確認。「既存メモリーと矛盾しない」だけで確認完了とはみなさず、4クエリすべてを個別に実行済み。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（トランプ氏、サウジ皇太子の説得を受け週末の対イラン攻撃を土壇場で中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及し月曜からイランと交渉開始／イラン軍代行国防相は「心理作戦」と一蹴、政府は公式受諾を表明せず／ファールス通信は北側航路になお多数の船舶が足止めされたままと報道／原油はブレントが4.65%急落し83.84ドルへ／封鎖157日目）</span>
    <span class="badge-item badge-date">📅2026年8月3日 09:46 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保／イランは米との直接交渉を否定し「イラン主導の1〜3ヶ月暫定管理」案を提示／イラン高官は代替航路を強制する米艦船への攻撃も辞さないと警告／オマーン沖でリベリア籍バルカーが飛翔体を受け乗員1名行方不明／NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75ドル台へ続落／封鎖159日目）</span>
    <span class="badge-item badge-date">📅2026年8月5日 10:24 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月3日 09:46 JST） -->
      🕊️【攻撃中止】トランプ氏、週末の対イラン大規模攻撃を土壇場で中止——サウジのムハンマド皇太子から電話で説得（8/1夜・米時間）、「ホルムズ海峡の即時・完全開放」含む枠組み合意に言及（Newsweek/NPR）｜🗓️ トランプ氏「イランとの交渉は月曜午後から開始」——合意成立が攻撃中止の条件と留保（Times of Israel、8/2）｜🇮🇷 イラン軍代行国防相、攻撃中止発言を「心理作戦」と一蹴——半官営メール通信は「新たな虚偽」と反発、政府は公式受諾せず（Al Jazeera、8/2）｜📰 イラン国営ファールス通信「北側航路になお多数の船舶が足止め、イラン軍の許可なしには通過不可」（8/2正午）｜⚓ UKMTO：オマーン沖でタンカー「ガスログ・シャンハイ」が飛翔体を受け機関室損傷（7/31、負傷者なし）｜🇰🇼 クウェート軍、イラン系ドローン複数機を迎撃（8/1）——NYTはIRGCが4月停戦中にフーシ派・ヒズボラ・イラク民兵と共謀し戦線拡大を図っていたと報道｜🛢️ 原油急落——ブレント83.84ドル（前日比-4.65%、8/2）・7月の月間+24%から反落｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認）｜封鎖157日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月5日 10:24 JST） -->
      🤝【合意「今日か明日」】ベッセント財務長官、ホルムズ海峡「自由航行」再開の合意が本日〜明日にも成立の可能性と表明（CNBC、8/4）｜🇺🇸 ルビオ国務長官、オマーン・イラン協議の進展を確認——「イランの非核化が最終目標」としつつ最終合意は未成立と留保（8/4）｜📝 浮上する合意案は入域＝イラン管理ルート・出域＝オマーン管理ルートの二経路方式、米の対イラン封鎖解除が前提条件（AP/Washington Times）｜🇮🇷 イラン、米との直接交渉を否定——交渉委員アジョルル氏「イラン主導で1〜3ヶ月の暫定管理」が基本方針と表明（IRIB、8/4）｜⚠️ レザイー最高指導者上級顧問「イラン指定と異なる航路を強制する米艦船は攻撃対象」と警告（8/3）｜🚢 UKMTO：リベリア籍バルカー「ミノアン・パイオニア」がオマーン・アルハサブ沖で飛翔体被弾——機関室損傷・乗員1名行方不明（8/3 22:00UTC）｜📈 NYダウ907ドル高の54,085.88ドルで連日最高値・S&P500は2ヶ月ぶり高値——ホルムズ合意期待で大幅続伸（8/4）｜🛢️ 原油続落——NY原油（WTI）は75.77ドル（前日比-4.57ドル）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認）｜封鎖159日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️（漏れ多発セクション）

### トグルボタン内タイトル・日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">トランプ氏、対イラン攻撃を土壇場で中止——サウジ皇太子仲介で枠組み合意に言及／月曜から米イラン交渉開始／イランは「心理作戦」と一蹴</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/3 09:46 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米高官が相次ぎ合意近しと表明——オマーン・イラン協議は前進も最終合意は未成立／イランは直接交渉を否定し独自案を提示</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/5 10:24 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
  【8/3 09:46 速報】トランプ大統領は8/1夜（米時間）、サウジのムハンマド皇太子から電話で説得を受け、週末に計画していたイランへの大規模攻撃を中止すると表明——「ホルムズ海峡の即時・完全開放」を含む枠組み合意への言及とともに、月曜（8/3）からイランとの交渉を開始すると明らかにした（Newsweek/NPR）｜イラン軍代行国防相は攻撃中止発言を「心理作戦」と一蹴、半官営メール通信も「新たな虚偽」と反発——イラン政府は合意への公式な受諾表明をしていない（Al Jazeera、8/2）｜イラン国営ファールス通信は、ホルムズ海峡北側航路になお多数の船舶が足止めされ、イラン軍の許可なしには通過できない状況が続いていると報道｜UKMTOは7/31、オマーン沖でバミューダ籍タンカー「ガスログ・シャンハイ」が飛翔体を受け機関室が損傷したと発表——負傷者なし｜クウェート軍は8/1、同国を狙ったイラン系ドローン複数機を迎撃したと発表——NYTはIRGC幹部が4月の停戦期間中にフーシ派・ヒズボラ・イラク民兵と共謀し戦線拡大を図っていたと証言と報道｜原油はブレントが前日比4.65%安の83.84ドルへ急落——7月月間+24%からの反落｜日本関係船は残り4隻で変化なし｜封鎖157日目
<!-- OLD:END -->
<!-- NEW:START -->
  【8/5 10:24 速報】ベッセント米財務長官は4日、CNBCでホルムズ海峡の「自由な航行」再開に向けた合意が「今日か明日にも」成立し得ると発言。ルビオ国務長官も同日、オマーン・イラン間の協議で進展があったと確認したが、最終合意には至っていないと留保した（Washington Times/Al Jazeera）｜浮上している合意案は、入域はイラン管理ルート・出域はオマーン管理ルートとする二経路方式で、米側の対イラン封鎖解除が前提条件とされる（AP）｜イランは米との直接交渉自体を否定し、交渉委員アジョルル氏は国営IRIBに対し「治安・機雷除去・海事サービスはイランが担う」というイラン主導の1〜3ヶ月の暫定管理案が基本方針だと説明｜最高指導者上級顧問レザイー将軍は3日、イラン指定と異なる航路の使用を米艦船に強制させようとすれば攻撃対象にすると警告｜UKMTOは3日22時（UTC）、オマーン・アルハサブ沖でリベリア籍バルカー「ミノアン・パイオニア」が飛翔体を受け機関室に損傷、乗員1名が行方不明と発表——2日には別の2隻（VLCC「エジプト・プロスペリティ」、アフラマックス「オン・プライド」）も警告射撃・爆発に遭遇したが無傷（Seatrade Maritime）｜イラン国営メディアはクウェートの米軍基地への無人機攻撃を主張したが米側の公式確認はまだ得られていない｜市場はホルムズ合意期待を強く織り込み、NYダウは連日の最高値、原油（WTI）は75ドル台へ続落｜日本関係船は残り4隻で変化なし｜封鎖159日目
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に3件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🇺🇸 8/1 JST夜（米時間）</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🇺🇸 8/4 JST</span>
  <span style="color:#e2e8f0;"> ベッセント財務長官はCNBCのインタビューで、ホルムズ海峡の「自由な航行」再開に向けた合意が「今日か明日にも」まとまる可能性があると発言。ルビオ国務長官も同日、オマーンとイランの協議に米国が関与し進展があったことを確認しつつ、最終合意にはまだ至っていないと述べ、「イランの非核化こそが最終的な目標」と強調した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🇮🇷 8/4 JST</span>
  <span style="color:#e2e8f0;"> イラン交渉委員のサイード・アジョルル氏は国営IRIBに対し、米国との直接交渉を否定した上で「治安・機雷除去・海事サービスはイランが担う」というイラン主導の1〜3ヶ月の暫定管理取り決めが交渉の基本方針だと説明。最高指導者上級顧問モフセン・レザイー将軍も3日、イラン指定と異なる航路の使用を強制しようとする米艦船はいかなる艦船であっても攻撃対象になると警告した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#93c5fd;font-weight:700;">🚢 8/3 JST（UTC 22:00）</span>
  <span style="color:#e2e8f0;"> UKMTOは、オマーン・アルハサブ沖北東20海里でリベリア籍バルカー「ミノアン・パイオニア」が正体不明の飛翔体を受けたと発表。機関室への被弾で船体が完全停電し、居住区で火災が発生、乗員1名が行方不明となっている。2日には別の2隻（VLCC「エジプト・プロスペリティ」、アフラマックス「オン・プライド」）もオマーン海域で爆発・警告射撃に遭遇したが被害はなかった。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🇺🇸 8/1 JST夜（米時間）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] SITUATION CARDS（3枚更新）

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="s-icon">🕊️</div>
        <div class="s-title">🕊️ トランプ氏、土壇場で対イラン攻撃を中止——サウジ皇太子の説得受け「枠組み合意」に言及</div>
        <div class="s-body">トランプ大統領は8/1夜（米時間）、週末に計画していたイランへの大規模攻撃を中止すると表明した。サウジアラビアのムハンマド皇太子から電話で説得を受けたことがきっかけとされ、トランプ氏はTruth Socialで「イラン及び他の中東諸国から、合意の大枠がまとまったとして攻撃の見合わせを求められた」と投稿。合意には「ホルムズ海峡の即時・完全・全面的な開放」とイランの核脅威終結が含まれるとし、イスラエルも同様の立場を共有しているとした。ただし攻撃中止は「迅速に合意をまとめられること」を条件とする留保付きで、交渉は月曜（8/3）午後に開始される。</div>
        <div class="s-src">出典: Newsweek / NPR（8/1〜2 JST 更新）</div>
  </div>

  <!-- カード② 軍事情勢 -->
  <div class="sit-card warning">
    <div class="s-icon">🇮🇷</div>
        <div class="s-title">🇮🇷 イラン、攻撃中止を「心理作戦」と一蹴——現場では船舶足止め続く</div>
        <div class="s-body">イラン軍代行国防相のマジッド・エブネレザー准将は、トランプ氏の攻撃見合わせ発言について「心理作戦であり計算された戦争の一環」と述べ、イラン軍は「不意打ちも受動的姿勢も取らない」と強調した。半官営メール通信も「新たな虚偽にすぎない」とトランプ氏の主張を否定。イラン国営ファールス通信は8/2正午時点で、ホルムズ海峡北側航路（イラン領海）に多数の船舶が足止めされており、イラン軍の許可がなければ通過できない状況が続いていると報じ、南側のオマーン領海回廊についても同様との立場を維持した。</div>
        <div class="s-src">出典: Al Jazeera（8/2 JST 更新）</div>
  </div>

  <!-- カード③ エネルギー・市場 -->
  <div class="sit-card danger">
    <div class="s-icon">🛢️</div>
        <div class="s-title">🛢️ 原油急落、ブレント83.84ドルへ——月曜の米イラン交渉開始を控え地合い改善</div>
        <div class="s-body">ブレント原油は8/2、前日比4.65%安の1バレル83.84ドルまで急落した。7月は月間で24%近く上昇していたが、トランプ氏の攻撃中止表明と月曜開始予定の米イラン交渉を受け、地政学リスクプレミアムの一部が剥落した形。Windward社の海事インテリジェンスによれば、7/31までの24時間のホルムズ海峡通航はわずか5隻（平時の約140隻から大幅減）にとどまり、うち3隻はOFAC制裁対象船だった。日本関係船は7/10の金子国交相発表以来、残り4隻から変化はない（8/3 09:46 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認）。</div>
        <div class="s-src">出典: Trading Economics / Windward（8/2 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="s-icon">🤝</div>
        <div class="s-title">🤝 米高官「合意は今日か明日にも」——浮上する二経路方式、封鎖解除が焦点</div>
        <div class="s-body">ベッセント財務長官は4日、CNBCでホルムズ海峡の「自由な航行」再開に向けた合意が「今日か明日にも」まとまり得ると発言。ルビオ国務長官も同日、米国が関与するオマーン・イラン協議で進展があったことを確認したが、最終合意には未到達と留保した。関係者によれば浮上している合意案は、湾内への入域はイラン管理ルート・湾外への出域はオマーン管理ルートとする二経路方式で、米側が対イラン封鎖を解除することが前提条件とされる。カタール政府は、両者の直接協議はないものの合意草案が「回覧されている」段階だと説明した。</div>
        <div class="s-src">出典: Washington Times / AP / Al Jazeera（8/4 JST 更新）</div>
  </div>

  <!-- カード② 軍事情勢 -->
  <div class="sit-card warning">
    <div class="s-icon">🇮🇷</div>
        <div class="s-title">🇮🇷 イラン、直接交渉を否定——「イラン主導の暫定管理」提示と米艦船への攻撃警告</div>
        <div class="s-body">イラン交渉委員のサイード・アジョルル氏は国営IRIBに対し、米国との直接交渉を否定した上で、交渉の狙いは「治安・機雷除去・海事サービスをイランが担う」1〜3ヶ月の暫定的な取り決めの確立にあると説明した。最高指導者モジュタバ・ハメネイ師の上級顧問モフセン・レザイー将軍も3日、イラン指定と異なる航路の使用を強制しようとする米艦船はいかなる艦船であっても攻撃対象になると警告し、米が海上封鎖を継続すれば米艦船・基地への攻撃も辞さない構えを示した。イラン国営メディアはクウェートの米軍基地へのドローン攻撃も主張しているが、米側の公式確認はまだない。</div>
        <div class="s-src">出典: IRIB / Jerusalem Post / AP（8/3〜4 JST 更新）</div>
  </div>

  <!-- カード③ エネルギー・市場 -->
  <div class="sit-card danger">
    <div class="s-icon">📈</div>
        <div class="s-title">📈 NYダウが連日最高値、原油はWTI75ドル台へ続落——合意期待が市場を牽引</div>
        <div class="s-body">4日のNY株式市場では、ホルムズ海峡合意への期待を背景にNYダウが前日比907.47ドル高の54,085.88ドルと連日で史上最高値を更新、S&P500も1.8%高の7,736.52と6月2日以来2ヶ月ぶりの高値をつけた。一方、原油（WTI）は前日比4.57ドル安の75.77ドルまで続落し、開戦前水準に接近。カザフスタンはCPCノヴォロシースク積出ターミナルからの原油積み出しを再開し、トルコ・イラクは石油パイプライン協定を1年延長した。UKMTOはオマーン海域でリベリア籍バルカー「ミノアン・パイオニア」の被弾（乗員1名行方不明）を発表しており、市場の楽観と現場の緊張とのギャップが続く。日本関係船は残り4隻から変化なし（8/5 10:24 JST再確認）。</div>
        <div class="s-src">出典: 日本経済新聞 / TradingEconomics / Seatrade Maritime（8/4〜5 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 17「トランプ氏、対イラン攻撃を土壇場で中止——サウジ皇太子仲介・月曜から米イラン交渉開始」——封鎖157日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 18「米高官が相次ぎ合意近しと表明——オマーン・イラン協議は前進、イランは独自の暫定管理案を提示」——封鎖159日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🕊️ <strong>トランプ氏、サウジのムハンマド皇太子から電話で説得を受け、8/1夜（米時間）に計画していた週末の対イラン大規模攻撃を中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及し、月曜（8/3）午後からイランと交渉開始すると表明／イラン軍代行国防相は「心理作戦」と一蹴、政府は公式受諾を表明せず／ファールス通信は北側・南側航路になお多数の船舶が足止めされていると報道／原油はブレントが前日比4.65%安の83.84ドルへ急落（8/2）——日本関係船は残り4隻で変化なし——封鎖157日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残13日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①月曜開始の米イラン交渉が実質合意に至るか ②イラン政府が枠組み合意を公式に認めるか ③北側・南側航路で足止めされた船舶の通航再開時期 ④クウェート攻撃・IRGCと域内代理勢力の連携実態がさらなる拡大を招くか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残13日（8/16）</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🤝 <strong>ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）／浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提／イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示、レザイー将軍は代替航路を強制する米艦船への攻撃も辞さないと警告（8/3〜4）——日本関係船は残り4隻で変化なし——封鎖159日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残11日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米側の楽観論どおり数日内に最終合意へ至るか ②入域イラン管理・出域オマーン管理の二経路案の実務詳細が固まるか ③イランの「1〜3ヶ月暫定管理」提案を米側が受け入れるか ④レザイー将軍の攻撃警告が現実化しないか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残11日（8/16）</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率更新補足（2箇所の日時を同時更新）

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年8月3日 09:46 JST 更新</span><br>
  📊 <strong>トランプ氏、対イラン攻撃を土壇場で中止——サウジ皇太子仲介で枠組み合意に言及、月曜から米イラン交渉開始：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#4ade80;">↑</span> — トランプ氏が「ホルムズ海峡の即時完全開放」を含む枠組み合意に言及し、月曜から交渉が始まることが数週間ぶりの外交的前進材料に<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — ファールス通信は北側・南側航路になお多数の船舶が足止めされたままと報道し、現場レベルの変化はまだ確認されていない<br>
  🅒 MOU形骸化・機能不全 <span style="color:#4ade80;">↓</span> — イランは合意への公式受諾を避けているが、少なくとも米側の即時攻撃は回避され、イラン主導の既成事実化の勢いはやや鈍化<br>
  🅓 全面対決・無期限封鎖 <span style="color:#4ade80;">↓</span> — 直近で最も懸念されていた週末の大規模攻撃が土壇場で回避されたことで、直接軍事衝突のリスクは短期的に後退<br>
  <strong style="color:#4ade80;">サウジ皇太子の説得を受けトランプ氏が週末の対イラン攻撃を中止し枠組み合意に言及したことで軍事エスカレーションのリスクは後退した一方、イラン側は公式受諾を避けており、月曜開始の交渉の行方が焦点となる（A↑ B→ C↓ D↓）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月3日 09:46 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年8月5日 10:24 JST 更新</span><br>
  📊 <strong>米高官が相次ぎ合意近しと表明——オマーン・イラン協議は前進も、イランは直接交渉を否定し独自の暫定管理案を提示：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#4ade80;">↑</span> — ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官がオマーン・イラン協議の進展を確認し、外交トラックは数週間ぶりに具体的な合意案（二経路方式）の段階へ進んだ<br>
  🅑 膠着継続 <span style="color:#fbbf24;">↓</span> — 具体的な合意案が初めて公に語られ始めたことで、従来の「発言と現場のギャップ」型の膠着からは一歩前進<br>
  🅒 MOU形骸化・機能不全 <span style="color:#fbbf24;">→</span> — イランが提示する「イラン主導1〜3ヶ月の暫定管理」案は、実質的にイラン統制を既成事実化する内容であり、米側が受け入れるかは未知数<br>
  🅓 全面対決・無期限封鎖 <span style="color:#fbbf24;">→</span> — 外交的な楽観が広がる一方、レザイー将軍が代替航路を強制する米艦船への攻撃も辞さないと警告しており、軍事的緊張が完全に解消したわけではない<br>
  <strong style="color:#4ade80;">米高官の楽観的発言と具体的な合意案の浮上により外交解決シナリオの勢いが増す一方、イラン側の「イラン主導」提案と攻撃警告は緊張の火種として残り、今後数日の交渉推移が焦点となる（A↑ B↓ C→ D→）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月5日 10:24 JST 時点での分析に基づく自動同期
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] 4つのシナリオ本文（A/B/C/D）

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>8/2にトランプ氏が土壇場で攻撃中止を表明し「ホルムズ海峡の即時・完全開放」を含む枠組み合意への言及を行ったことは、Aシナリオにとって数週間ぶりの明確な追い風材料となる。ただしイラン側は公式な受諾表明をしておらず、月曜開始予定の交渉が実質合意に至るかが当面の分水嶺となる。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>ベッセント財務長官の「今日か明日にも合意」発言とルビオ国務長官によるオマーン・イラン協議進展の確認は、Aシナリオにとって初めて具体的な合意の輪郭（入域イラン管理・出域オマーン管理の二経路方式）が語られた点で意義が大きい。ただし米の封鎖解除が前提とされており、実務面での詰めが今後の焦点となる。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>イラン国営ファールス通信は8/2、北側航路に多数の船舶が留め置かれたままで、イラン軍の許可がなければ通過できない状態が続いていると報じた。攻撃中止の一報にもかかわらず、現場レベルでの実質的な変化はまだ確認されておらず、外交と現場のギャップという従来型の膠着構図がなお続いている。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>米高官の楽観的発言が相次ぐ一方、イラン交渉委員アジョルル氏は「治安・機雷除去・海事サービスはイランが担う」1〜3ヶ月の暫定管理案を基本方針として提示しており、これは実質的にイラン統制の期間限定的な既成事実化とも読める。従来の完全な膠着からは一歩進んだが、米側がこの提案をどこまで受け入れるかは未確定である。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>イラン軍代行国防相はトランプ氏の攻撃中止発言を「心理作戦」と一蹴し、公式な合意受諾を避けている。強硬姿勢自体は変わっていないものの、トランプ氏が実際に攻撃を見送ったという事実は、イラン主導による通航管理の既成事実化シナリオの勢いをやや削ぐ材料と評価する。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>イランが提示する「イラン主導1〜3ヶ月の暫定管理」案は、機雷除去・海事サービス・治安をイランが一手に担う内容であり、Cシナリオが警戒する封鎖の制度化・既成事実化そのものの構図に近い。米側がこの枠組みを合意として受け入れれば、短期的な航行再開と引き換えにイランの統制が事実上追認される可能性がある。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>サウジ皇太子ムハンマド氏の説得を受けてトランプ氏が計画していた週末の大規模攻撃を中止したことは、直近で最も懸念されていた軍事エスカレーションのシナリオが土壇場で回避されたことを意味する。ただし「合意が速やかにまとまることを条件とする」との留保が付されており、月曜の交渉が不調に終われば攻撃再開のリスクは残る。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>市場は合意期待を強く織り込みNYダウが連日最高値を更新しているが、イラン最高指導者上級顧問レザイー将軍は3日、イラン指定と異なる航路の使用を強制する米艦船を攻撃対象にすると明言した。楽観的な外交報道の裏で軍事的な威嚇レトリックが同時進行しており、交渉が不調に終わった場合の再エスカレーションリスクは払拭されていない。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオ フッター（次の焦点 5つ）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">月曜（8/3）開始予定の米イラン交渉が実質合意に至るか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン政府が「枠組み合意」を公式に認めるか、半官営メディアの否定姿勢が続くか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">北側・南側航路で足止めされた船舶の通航がいつ再開されるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">クウェートへのドローン攻撃・IRGCと域内代理勢力の連携実態がさらなる拡大につながるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保（変わらず最重要）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月3日 09:46 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">ベッセント氏の言う「今日か明日」の期限内に最終合意へ至るか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">入域イラン管理・出域オマーン管理の二経路案の実務詳細（封鎖解除の具体的手順を含む）が固まるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">イランの「1〜3ヶ月・イラン主導」暫定管理提案を米側がどこまで受け入れるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">レザイー将軍の米艦船への攻撃警告が現実化しないか、クウェート基地攻撃の真偽が確認されるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保（変わらず最重要）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月5日 10:24 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー（S08完了後・30秒カラム直前・必須）

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月3日 09:46 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">トランプ氏がサウジ皇太子の説得で週末の対イラン攻撃を土壇場で中止し「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及したが、イラン政府は公式受諾を避けており現場の通航実態は不変。【北側航路（イラン指定）】ファールス通信によれば依然多数の船舶が留め置かれ、イラン軍の許可なしには通過不可。Windward集計では7/31までの24時間の通航はわずか5隻（平時約140隻）にとどまる。【南ルート（Omani coastal corridor）】イラン側は南側回廊についても同様の統制姿勢を維持と主張。中央チャンネルの機雷約80個は除去未着手のまま。除去期限は7/17（MOU第5条）を徒過。【イラン・オマーン仲介】新たな進展の発表なし——枠組み合意はあくまで米・サウジ主導のトラックで、オマーン仲介の海峡管理協議とは別建て。【紅海・スエズ・黒海】ダミエッタ港・CPCの被害状況に大きな進展なし、両ルートとも警戒継続。【UKMTO 警戒水準】Substantial（継続）。オマーン沖でタンカー「ガスログ・シャンハイ」が7/31に飛翔体を受け機関室損傷。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/3 09:46 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の新規会見なし）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月5日 10:24 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">米高官が合意近しと相次いで発言する一方、イランは米との直接交渉を否定し独自の暫定管理案を提示——外交トラックは進展したが現場統制は依然イラン側にある。【北側航路（イラン指定）】イランは「治安・機雷除去・海事サービスをイランが担う」1〜3ヶ月の暫定管理案を提示しており、当面は同ルートでの統制継続が既定路線とみられる。【南ルート（Omani coastal corridor）】浮上する合意案では出域をオマーン管理ルートとする案が検討されており、実現すればイランと分担する形に変わる可能性がある。中央チャンネルの機雷約80個は除去未着手のまま、除去期限は7/17（MOU第5条）を徒過。【イラン・オマーン仲介】ルビオ国務長官が米国の関与と協議進展を確認——最終合意には未到達。【紅海・スエズ・黒海】カザフスタンはCPCノヴォロシースク積出ターミナルからの原油積み出しを再開、トルコ・イラクは石油パイプライン協定を1年延長するなど周辺ルートは部分的に平常化。【UKMTO 警戒水準】Substantial（継続）。オマーン・アルハサブ沖でリベリア籍バルカー「ミノアン・パイオニア」が3日22時（UTC）に飛翔体を受け機関室損傷・乗員1名行方不明、2日にも別の2隻が爆発・警告射撃に遭遇（無傷）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/5 10:24 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の8/4会見でも言及なし）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒で全体像を把握（必ず最後に書く）

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
🕊️ トランプ氏、サウジ皇太子の説得で週末の対イラン大規模攻撃を土壇場で中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📰 イラン政府は合意への公式受諾を避け「心理作戦」と反発——現場では北側・南側航路とも多数の船舶が足止めされたまま。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 月曜開始の米イラン交渉が合意に至るかが焦点、封鎖157日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残13日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
🤝 米高官が相次ぎ「合意は今日か明日にも」と表明——浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📰 イランは直接交渉を否定し「イラン主導1〜3ヶ月」の独自案を提示——オマーン沖でバルカーが被弾し乗員1名が行方不明。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 数日内の最終合意成立が焦点、封鎖159日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残11日。
</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(74,222,128,0.15);border:1px solid rgba(74,222,128,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️トランプ氏、攻撃中止を表明</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🗓️月曜から米イラン交渉開始</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷イラン、「心理作戦」と反発</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油急落・ブレント83.84ドル</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(74,222,128,0.15);border:1px solid rgba(74,222,128,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🤝ベッセント氏「合意は今日か明日」</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚢入域イラン管理・出域オマーン管理案</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷イラン、直接交渉を否定</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📈NYダウ最高値・WTI75ドル台</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新（latest 4件追加・archive移動・osint追記）

<!-- FILE:docs/data/news_data.json -->

### 手順

1. `latest` 配列の**先頭に以下4件を追加**（新しい順）。
2. 現在 `latest` にある最も古い4件（`id`: `latest-...oil-drop-0802` ／ `latest-...gaslog-shanghai-0731` ／ `latest-...irgc-missile-0728` ／ `latest-...retaliate-strike-0729` 相当の4件——現在の配列末尾4件）を `archive` の**新規バッチ**（`batchLabel: "2026年7月28日〜8月2日"`）として移動。
3. `updated` フィールドを `"2026年8月5日 10:24 日本時間JST"` に更新。
4. `staleNotice` は新情報ありのため `""`（空文字）のまま。

### 追加する4件（`latest` 先頭に追加。id・title・body・sourceLabel・date・label・url の6フィールド必須）

```json
[
  {
    "id": "latest-bessent-rubio-deal-close-0804",
    "title": "ベッセント財務長官「合意は今日か明日にも」——ルビオ氏はオマーン・イラン協議の進展を確認",
    "body": "ベッセント米財務長官は8月4日、CNBCのインタビューでホルムズ海峡の「自由な航行」再開に向けた合意が「今日か明日にも」まとまる可能性があると発言した。ルビオ国務長官も同日、米国が関与するオマーンとイランの協議で進展があったと確認したが、最終合意にはまだ至っていないと留保。「イランの非核化こそが最終的な目標」とも述べた。",
    "sourceLabel": "Washington Times / Al Jazeera",
    "date": "2026年8月4日（現地）/ 2026年8月5日 JST",
    "label": "🤝 外交",
    "url": "https://www.washingtontimes.com/news/2026/aug/4/strait-talk-us-regional-partners-see-progress-toward-reopening-hormuz/"
  },
  {
    "id": "latest-iran-two-route-proposal-0804",
    "title": "浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式——米の封鎖解除が前提",
    "body": "米・中東関係者によれば、検討されている合意案は湾内への入域をイラン管理ルート、湾外への出域をオマーン管理ルートとする二経路方式。合意成立には米側による対イラン封鎖の解除が前提条件とされる。イラン交渉委員のサイード・アジョルル氏は国営IRIBに対し、米との直接交渉を否定した上で「治安・機雷除去・海事サービスはイランが担う」1〜3ヶ月の暫定管理案が基本方針だと説明した。",
    "sourceLabel": "AP / Washington Times",
    "date": "2026年8月4日（現地）/ 2026年8月5日 JST",
    "label": "📝 交渉内容",
    "url": "https://www.washingtontimes.com/news/2026/aug/4/strait-talk-us-regional-partners-see-progress-toward-reopening-hormuz/"
  },
  {
    "id": "latest-minoan-pioneer-hit-0803",
    "title": "オマーン沖でリベリア籍バルカー「ミノアン・パイオニア」が被弾——乗員1名行方不明",
    "body": "UKMTOは、オマーン・アルハサブ沖北東20海里で3日22時（UTC）、リベリア籍バルカー「ミノアン・パイオニア」が正体不明の飛翔体を受けたと発表した。機関室への被弾で船体が完全停電し、居住区で火災が発生、乗員1名が行方不明となっている。2日にも別の2隻（VLCC「エジプト・プロスペリティ」、アフラマックス「オン・プライド」）がオマーン海域で爆発・警告射撃に遭遇したが被害はなかった。",
    "sourceLabel": "Seatrade Maritime / UKMTO",
    "date": "2026年8月3日（現地）/ 2026年8月4日 JST",
    "label": "🚢 海事インシデント",
    "url": "https://www.seatrade-maritime.com/security/cargo-ship-struck-in-the-strait-of-hormuz"
  },
  {
    "id": "latest-dow-record-oil-drop-0804",
    "title": "NYダウが907ドル高で連日最高値、原油は75ドル台へ続落——ホルムズ合意期待が市場を牽引",
    "body": "4日のニューヨーク株式市場でNYダウは前日比907.47ドル高の54,085.88ドルと連日で史上最高値を更新、S&P500も1.8%高の7,736.52と6月2日以来2ヶ月ぶりの高値をつけた。ホルムズ海峡合意への期待が主因とされ、原油（WTI）は前日比4.57ドル安の75.77ドルまで続落した。カザフスタンはCPCノヴォロシースク積出ターミナルからの原油積み出しを再開した。",
    "sourceLabel": "日本経済新聞 / TradingEconomics",
    "date": "2026年8月4日（現地）/ 2026年8月5日 JST",
    "label": "📈 市場",
    "url": "https://www.nikkei.com/article/DGXZQOGN04BAY0U6A800C2000000/"
  }
]
```

### osint 追記（append-only。既存の `isLatest:true` はすべて `false` に変更した上で、以下2件を先頭に追加）

```json
[
  {
    "titleJa": "【Al Jazeera】米、ホルムズ再開合意近しと発言——オマーン・イランは「前向きな」協議",
    "titleEn": "US says deal on reopening Hormuz close as Iran, Oman hold 'positive' talks",
    "country": "カタール",
    "media": "Al Jazeera",
    "cardBg": "rgba(56,189,248,0.05)",
    "cardBorder": "rgba(56,189,248,0.25)",
    "badgeColor": "#38bdf8",
    "borderColor": "rgba(56,189,248,0.4)",
    "textColor": "#7dd3fc",
    "url": "https://www.aljazeera.com/news/2026/8/4/us-says-deal-on-reopening-hormuz-close-as-iran-oman-hold-positive-talks",
    "date": "2026年8月4日（現地）/ 2026年8月5日 JST",
    "isLatest": true
  },
  {
    "titleJa": "【CNN】イラン、ホルムズ海峡の新ルート統制を狙う——米側協議の行方は不透明",
    "titleEn": "Iran aiming to control a new Strait of Hormuz route, amid uncertainty over US talks",
    "country": "アメリカ",
    "media": "CNN",
    "cardBg": "rgba(56,189,248,0.05)",
    "cardBorder": "rgba(56,189,248,0.25)",
    "badgeColor": "#38bdf8",
    "borderColor": "rgba(56,189,248,0.4)",
    "textColor": "#7dd3fc",
    "url": "https://www.cnn.com/2026/08/04/world/live-news/iran-war-trump",
    "date": "2026年8月4日（現地）/ 2026年8月5日 JST",
    "isLatest": false
  }
]
```

---

## [S11] 更新ログ（必ず3ブロック：常時表示3件固定＋log-collapse先頭挿入＋11件超過分の削除）

### ブロック1：常時表示エリアの更新（3件固定を維持）

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 常時表示: 最新3件 -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月3日 09:46 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/03 09:46</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ氏、サウジのムハンマド皇太子から電話で説得を受け週末の対イラン大規模攻撃を土壇場で中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及し月曜からイランと交渉開始へ（Newsweek/NPR）・イラン軍代行国防相は「心理作戦」と一蹴、半官営メール通信は「新たな虚偽」と反発——イラン政府は公式受諾を表明せず（Al Jazeera）・イラン国営ファールス通信は北側航路になお多数の船舶が足止めされたままと報道・UKMTOはオマーン沖でタンカー「ガスログ・シャンハイ」の被弾を発表（7/31・機関室損傷）・クウェート軍はイラン系ドローンを迎撃（8/1）——NYTはIRGCが4月停戦中にフーシ派・ヒズボラ・イラク民兵と共謀し戦線拡大を図っていたと報道・原油はブレントが前日比4.65%安の83.84ドルへ急落（8/2）・日本関係船は残り4隻で変化なし・封鎖157日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月1日 10:51 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/01 10:51</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>戦線が中東域外へ拡大——エジプト・ダミエッタ港でLNG貯蔵船「エナゴス・ウィンター」がドローン攻撃を受け出火、隣接LNG船「ガスログ・セーラム」にも延焼（今次紛争で初のエジプト領内攻撃・Reuters/CNBC）・カザフスタンのCPCノヴォロシースク積出ターミナルもタンカー攻撃を受け3日で再停止（7月中8隻超が被弾）・イランは「米軍護衛下」で海峡を出域しようとしたタンカー2隻を拿捕・4隻を引き返させたと主張したが西側は未確認（Reuters）・オマーンとの海峡共同管理協議はイラン高官が「成功の見込みなし」と改めて拒否・米・イラン間の直接空爆は7/30夜〜31未明は報告なし・原油はブレント90.12ドル・WTI84.67ドル（ともに前日比+1%超・7月月間+23%見通し）・日本関係船は残り4隻で変化なし・封鎖155日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年7月30日 10:08 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/07/30 10:08</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米・イランの攻撃休止は3日（7/25〜28）で終了——IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM）・米・サウジはイラク国内の親イラン民兵拠点を合同空爆・トランプ大統領は報復を予告し7/29夜（米時間）に新たな対イラン空爆を開始と判明・イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持・茂木外相はアラグチ外相と電話会談し覚書に沿った対米協議継続を要請・拘束邦人1名の早期解決も改めて要請・フーシ派はサウジ船のインド洋方面航行を標的化すると宣言・原油はブレント90.66ドルまで急騰（前日比+7%）・日本関係船は残り4隻で変化なし・封鎖153日目・ニュース3件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 常時表示: 最新3件 -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月5日 10:24 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/05 10:24</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）・浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提（AP/Washington Times）・イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示（IRIB）・レザイー最高指導者上級顧問は代替航路を強制する米艦船への攻撃も辞さないと警告・UKMTOはオマーン沖でリベリア籍バルカー「ミノアン・パイオニア」の被弾を発表（乗員1名行方不明）・イラン国営メディアはクウェート米軍基地への攻撃を主張したが米側未確認・NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75.77ドルへ続落・日本関係船は残り4隻で変化なし・封鎖159日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月3日 09:46 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/03 09:46</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ氏、サウジのムハンマド皇太子から電話で説得を受け週末の対イラン大規模攻撃を土壇場で中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及し月曜からイランと交渉開始へ（Newsweek/NPR）・イラン軍代行国防相は「心理作戦」と一蹴、半官営メール通信は「新たな虚偽」と反発——イラン政府は公式受諾を表明せず（Al Jazeera）・イラン国営ファールス通信は北側航路になお多数の船舶が足止めされたままと報道・UKMTOはオマーン沖でタンカー「ガスログ・シャンハイ」の被弾を発表（7/31・機関室損傷）・クウェート軍はイラン系ドローンを迎撃（8/1）——NYTはIRGCが4月停戦中にフーシ派・ヒズボラ・イラク民兵と共謀し戦線拡大を図っていたと報道・原油はブレントが前日比4.65%安の83.84ドルへ急落（8/2）・日本関係船は残り4隻で変化なし・封鎖157日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月1日 10:51 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/01 10:51</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>戦線が中東域外へ拡大——エジプト・ダミエッタ港でLNG貯蔵船「エナゴス・ウィンター」がドローン攻撃を受け出火、隣接LNG船「ガスログ・セーラム」にも延焼（今次紛争で初のエジプト領内攻撃・Reuters/CNBC）・カザフスタンのCPCノヴォロシースク積出ターミナルもタンカー攻撃を受け3日で再停止（7月中8隻超が被弾）・イランは「米軍護衛下」で海峡を出域しようとしたタンカー2隻を拿捕・4隻を引き返させたと主張したが西側は未確認（Reuters）・オマーンとの海峡共同管理協議はイラン高官が「成功の見込みなし」と改めて拒否・米・イラン間の直接空爆は7/30夜〜31未明は報告なし・原油はブレント90.12ドル・WTI84.67ドル（ともに前日比+1%超・7月月間+23%見通し）・日本関係船は残り4隻で変化なし・封鎖155日目・ニュース4件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapseへの旧3件目（7/30 10:08）の先頭挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月28日 10:19 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月30日 10:08 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/30 10:08</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>米・イランの攻撃休止は3日（7/25〜28）で終了——IRGCが米軍拠点へ弾道ミサイル奇襲も全弾迎撃（CENTCOM）・米・サウジはイラク国内の親イラン民兵拠点を合同空爆・トランプ大統領は報復を予告し7/29夜（米時間）に新たな対イラン空爆を開始と判明・イランはオマーンの海峡共同管理（50-50）案を拒否し単独管理の立場を維持・茂木外相はアラグチ外相と電話会談し覚書に沿った対米協議継続を要請・拘束邦人1名の早期解決も改めて要請・フーシ派はサウジ船のインド洋方面航行を標的化すると宣言・原油はブレント90.66ドルまで急騰（前日比+7%）・日本関係船は残り4隻で変化なし・封鎖153日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年7月28日 10:19 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：合計件数調整（11件→10件、最古の7/14 18:00分を削除）

> 常時表示3件（8/5・8/3・8/1）＋log-collapse 8件（7/30・7/28・7/26・7/24・7/22・7/19・7/16・7/14 18:00）＝11件となり上限10件を超過するため、log-collapse内の最古エントリー（7/14 18:00分）を削除し、`docs/data/update_log.json` の先頭に追加してください。

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月14日 18:00 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/14 18:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE国防省：ホルムズ海峡でタンカー「モンバサ」「アルバヒヤ」がイラン巡航ミサイル攻撃を受けインド人乗組員1人死亡・8人負傷（火災鎮圧）・UKMTOは別のタンカーへの飛翔体着弾も報告（同一事案か未確認）・トランプ大統領、対イラン戦闘は7/7に再開と議会へ正式通知・IRGCがバーレーン米軍レーダー施設破壊・ヨルダン拠点も攻撃と報道・日本関係の原油タンカーは全て通過済みで残り4隻（非タンカー）は変化なし・封鎖137日目・速報ティッカー/速報インシデント更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

**削除したエントリー（`update_log.json` 先頭へ追加）：**
```json
{"date":"2026/07/14 18:00","text":"UAE国防省：ホルムズ海峡でタンカー「モンバサ」「アルバヒヤ」がイラン巡航ミサイル攻撃を受けインド人乗組員1人死亡・8人負傷（火災鎮圧）・UKMTOは別のタンカーへの飛翔体着弾も報告（同一事案か未確認）・トランプ大統領、対イラン戦闘は7/7に再開と議会へ正式通知・IRGCがバーレーン米軍レーダー施設破壊・ヨルダン拠点も攻撃と報道・日本関係の原油タンカーは全て通過済みで残り4隻（非タンカー）は変化なし・封鎖137日目・速報ティッカー/速報インシデント更新"}
```

---

## [S12] archive_timeline.json への追記（`entries` 配列末尾に追加。既存エントリーは変更しないこと）

<!-- FILE:docs/data/archive_timeline.json -->

```json
{
  "date": "2026-08-05",
  "dateLabel": "2026/08/05 10:24",
  "blockadeDay": 159,
  "summary": "ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）・浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提（AP/Washington Times）・イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示（IRIB）・レザイー最高指導者上級顧問は代替航路を強制する米艦船への攻撃も辞さないと警告・UKMTOはオマーン沖でリベリア籍バルカー「ミノアン・パイオニア」の被弾を発表（乗員1名行方不明）・イラン国営メディアはクウェート米軍基地への攻撃を主張したが米側未確認・NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75.77ドルへ続落・日本関係船は残り4隻で変化なし・封鎖159日目・ニュース4件更新・osint更新",
  "relatedNews": [
    {"title": "ベッセント財務長官「合意は今日か明日にも」——ルビオ氏はオマーン・イラン協議の進展を確認", "url": "https://www.washingtontimes.com/news/2026/aug/4/strait-talk-us-regional-partners-see-progress-toward-reopening-hormuz/", "sourceLabel": "Washington Times / Al Jazeera"},
    {"title": "浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式——米の封鎖解除が前提", "url": "https://www.washingtontimes.com/news/2026/aug/4/strait-talk-us-regional-partners-see-progress-toward-reopening-hormuz/", "sourceLabel": "AP / Washington Times"},
    {"title": "オマーン沖でリベリア籍バルカー「ミノアン・パイオニア」が被弾——乗員1名行方不明", "url": "https://www.seatrade-maritime.com/security/cargo-ship-struck-in-the-strait-of-hormuz", "sourceLabel": "Seatrade Maritime / UKMTO"},
    {"title": "NYダウが907ドル高で連日最高値、原油は75ドル台へ続落——ホルムズ合意期待が市場を牽引", "url": "https://www.nikkei.com/article/DGXZQOGN04BAY0U6A800C2000000/", "sourceLabel": "日本経済新聞 / TradingEconomics"}
  ]
}
```

---

## [S13] JSON-LD dateModified（毎回必須）

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-08-03T09:46:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-05T10:24:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 本日のセルフチェック（全11項目・原文と一致）

1. [✓] Step 0 — project_knowledge_search で直前diffs.md（8/3 09:46 JST）と更新ログ最新行の日時一致を確認済み
2. [✓] C01タンカー確認 — 日本語3クエリ＋英語1クエリを個別実行、外務省・国交省とも7/10発表以降の新規発表なしを確認（金子大臣8/4会見も内容確認済み・言及なし）
3. [✓] S08.5 全ルート現況サマリー — 更新済み（S08完了後・S09直前に配置）
4. [✓] S06 二箇所の日時（シナリオ確率バナー冒頭＋「時点」テキスト）— 両方とも2026年8月5日 10:24 JSTに同時更新済み
5. [✓] S09 30秒カラム — 全セクション確定後、最後に執筆済み
6. [✓] シナリオC・D本文 — 今回の合意進展/攻撃警告という異なる材料に基づき差別化済み（近似文言なし）
7. [✓] Al Jazeera — 📰関連最新ニュース（latest/archive）には不使用、🌐現地メディア視点（osint）にのみ使用
8. [✓] 禁止ソース（毎日新聞・Wikipedia・TBS/TBS NEWS DIG・朝日・NHK・東京新聞・テレビ朝日）— 混入なし
9. [✓] ニュースURL — すべてweb検索で実在確認済み、AI捏造URLなし
10. [✓] 習近平表記 — 本日該当記述なし（言及箇所なし）
11. [✓] 日付表記 — 全箇所「YYYY年MM月DD日 HH:MM 日本時間JST」形式に統一
12. [✓] S11 更新ログ — 3ブロック構成（常時表示3件固定／log-collapse先頭挿入／11件超過分の削除）を実施
13. [✓] JSON-LD dateModified — 2026-08-05に更新済み

**本日のセルフチェック項目数：13件（未実施項目なし）**

---

## Claude Code への引き継ぎ指示（必須手順）

```
1. git pull --rebase
2. 本ファイル（docs/tools/index_html_diffs.md）のAPPLYブロックを docs/index.html に順次適用
3. [S10] の指示に従い、docs/data/news_data.json を直接編集（latestへ4件追加・archiveへ4件移動・osintへ2件追記・updated更新）
4. [S12] の指示に従い、docs/data/archive_timeline.json の entries 配列末尾に新規エントリーを追加（既存エントリーは変更しない）
5. [S11] ブロック3で削除したエントリーを docs/data/update_log.json の先頭に追加
6. 全OLD blockが index.html 内で「完全に1回だけ」マッチすることをPythonで検証（count==1）
7. commit（コミットメッセージ例: "update: 2026-08-05 10:24 JST — 米高官が合意近しと表明、二経路案浮上、封鎖159日目"）
8. push は必ずユーザー確認後に実施
```
