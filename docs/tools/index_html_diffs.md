# index_html_diffs.md — 2026年8月7日 09:45 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## 出力前セルフチェック（先貼り・作業前に空欄で貼付）

```
[ ] S01 ヘッダー日時・警戒レベル
[ ] S02 TICKER
[ ] S03 速報インシデント（トグルボタン＋strong＋リスト先頭に新規追加）
[ ] S04 情勢カード3枚
[ ] S05 COUNTDOWN（phase-label＋dl-note）
[ ] S06 シナリオ確率補足バナー（①sec-title直下の日付見出し／②確率バナー末尾の「時点」表記の両方）
[ ] S07 シナリオ4本（タイトル・本文）
[ ] S08 シナリオフッター（次の焦点5つ）
[ ] S08.5 全ルート現況サマリー
[ ] S09 30秒カラム（3行サマリー＋ステータスバッジ）※最後に執筆
[ ] S10 news_data.json（latest4件追加・archive移動・osint2件追記）
[ ] S11 更新ログ（2ブロック構成）
[ ] JSON-LD dateModified
[ ] C01 タンカー確認（日英4クエリ）
[ ] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[ ] 全体 ― ニュースURLにAI捏造・推測URLが混入していないか（web検索確認済みURLのみ使用）
[ ] 全体 ― 📰関連最新ニュースにAl Jazeeraが混入していないか（osintのみ使用可）
[ ] 全体 ― 禁止ソース（毎日新聞・Wikipedia・TBS/TBS NEWS DIG・朝日・NHK・東京新聞・テレビ朝日）混入なし
[ ] 全体 ― 人名が日本語表記になっているか（「Xi」「Trump」のみの表記なし）
[ ] シナリオC・D本文が近似文言でなく差別化されているか
```

**本日のセルフチェック項目数：18件**

```
[x] S01 ― 更新済み
[x] S02 ― 更新済み
[x] S03 ― 更新済み（トグル・strong・リスト先頭2件追加）
[x] S04 ― 更新済み（3枚とも更新）
[x] S05 ― 更新済み
[x] S06 ― 更新済み（①②両方の日付を2026年8月7日 09:45 JSTに統一）
[x] S07 ― 更新済み（4本とも本文差し替え）
[x] S08 ― 更新済み
[x] S08.5 ― 更新済み（S08完了後・S09直前に配置）
[x] S09 ― 更新済み（最後に執筆）
[x] S10 ― 更新済み（latest4件追加・archiveへ4件移動・osint2件追記）
[x] S11 ― 更新済み（2ブロック構成）
[x] JSON-LD dateModified ― 2026-08-07に更新済み
[x] C01 ― 日本語3クエリ＋英語1クエリを個別実行。外務省・国交省とも新規発表なし確認。金子国交相8/4会見は熊本地震対応が主題でホルムズ言及なし。→ 残り4隻・変化なしを維持
[x] 日付表記 ― 全箇所「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一
[x] ニュースURL ― 全てweb検索で実在確認済み（NPR/Reuters/CNBC/Bloomberg/Euronews/CNN等）、AI捏造URLなし
[x] Al Jazeera ― 📰関連最新ニュース（latest/archive）には不使用。🌐現地メディア視点（osint）のみに使用
[x] 禁止ソース ― 毎日新聞・Wikipedia・TBS/TBS NEWS DIG・朝日・NHK・東京新聞・テレビ朝日、いずれも混入なし（NHK記事は確認のみに使用し出典・URLとしては不使用）
[x] 人名表記 ― 該当箇所なし（Trump/Xiの英字単独表記なし）
[x] シナリオC・D ― Cはイラン議会の一方的な通行料・排除法案（制度化リスク）、Dはフーシ派の紅海攻撃継続＋レザイー将軍警告の残存（軍事リスク）で異なる材料に基づき差別化
```

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保／イランは米との直接交渉を否定し「イラン主導の1〜3ヶ月暫定管理」案を提示／イラン高官は代替航路を強制する米艦船への攻撃も辞さないと警告／オマーン沖でリベリア籍バルカーが飛翔体を受け乗員1名行方不明／NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75ドル台へ続落／封鎖159日目）</span>
    <span class="badge-item badge-date">📅2026年8月5日 10:24 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イラン・オマーンがホルムズ海峡の安全航路の座標に合意、共同声明は最終調整段階／米メディアはオマーンが「入域イラン管理・出域オマーン管理」の暫定枠組みに合意したと報道／一方でイラン議会委員会は米・イスラエル船排除と他国船への最大7%通行料課税、違反時は貨物価値20%罰金の法案を審議、米政府は即座に拒否／フーシ派はサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目／NYダウは3日連続最高値も6日は反落、原油は乱高下／封鎖161日目）</span>
    <span class="badge-item badge-date">📅2026年8月7日 09:45 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月5日 10:24 JST） -->
      🤝【合意「今日か明日」】ベッセント財務長官、ホルムズ海峡「自由航行」再開の合意が本日〜明日にも成立の可能性と表明（CNBC、8/4）｜🇺🇸 ルビオ国務長官、オマーン・イラン協議の進展を確認——「イランの非核化が最終目標」としつつ最終合意は未成立と留保（8/4）｜📝 浮上する合意案は入域＝イラン管理ルート・出域＝オマーン管理ルートの二経路方式、米の対イラン封鎖解除が前提条件（AP/Washington Times）｜🇮🇷 イラン、米との直接交渉を否定——交渉委員アジョルル氏「イラン主導で1〜3ヶ月の暫定管理」が基本方針と表明（IRIB、8/4）｜⚠️ レザイー最高指導者上級顧問「イラン指定と異なる航路を強制する米艦船は攻撃対象」と警告（8/3）｜🚢 UKMTO：リベリア籍バルカー「ミノアン・パイオニア」がオマーン・アルハサブ沖で飛翔体被弾——機関室損傷・乗員1名行方不明（8/3 22:00UTC）｜📈 NYダウ907ドル高の54,085.88ドルで連日最高値・S&P500は2ヶ月ぶり高値——ホルムズ合意期待で大幅続伸（8/4）｜🛢️ 原油続落——NY原油（WTI）は75.77ドル（前日比-4.57ドル）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英クエリで再確認）｜封鎖159日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月7日 09:45 JST） -->
      🇮🇷🇴🇲【航路座標に合意】イラン外務省、ホルムズ海峡の安全航路の地理的座標についてオマーンと合意したと発表——共同声明は最終調整・起草段階（IRNA、8/5）｜🚢 米メディア（MS NOW）：オマーンは入域＝イラン管理ルート・出域＝オマーン管理ルートとする暫定枠組みに合意したと報道（8/6）｜⚠️【イラン議会が対抗法案】議会委員会が米・イスラエル船の永久排除、他国船に貨物価値最大7%の通行料、違反時20%の罰金を課す法案を審議（Fars通信、8/6）｜🇺🇸 米政府はこの案を即座に拒否——「承認・許可・通行料一切なしの自由航行」を要求（CNBC、8/6）｜🐹 フーシ派、サウジタンカー「Wafa」をヤンブー沖で攻撃と主張——7/22の紅海封鎖開始以降8隻目、29隻が引き返し（Reuters、8/5）｜📈 NYダウは263ドル高の54,349.12ドルで3日連続最高値（8/5）も6日はハイテク株主導で反落｜🛢️ 原油は乱高下——イラン議会案への懸念でブレントは一時81ドル台へ反発、WTIは75ドル前後で推移（8/6）｜🇯🇵 日本関係船は残り4隻で変化なし（外務省・国交省へ日英4クエリで再確認・金子国交相8/4会見は熊本地震対応が主題）｜封鎖161日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️（漏れ多発セクション）

### トグルボタン本体

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:1.1rem;">🚨</span>
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">米高官が相次ぎ合意近しと表明——オマーン・イラン協議は前進も最終合意は未成立／イランは直接交渉を否定し独自案を提示</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/5 10:24 更新</span>
    </span>
  </div>

  <!-- 折りたたみ本体（デフォルト非表示） -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/5 10:24 速報】ベッセント米財務長官は4日、CNBCでホルムズ海峡の「自由な航行」再開に向けた合意が「今日か明日にも」成立し得ると発言。ルビオ国務長官も同日、オマーン・イラン間の協議で進展があったと確認したが、最終合意には至っていないと留保した（Washington Times/Al Jazeera）｜浮上している合意案は、入域はイラン管理ルート・出域はオマーン管理ルートとする二経路方式で、米側の対イラン封鎖解除が前提条件とされる（AP）｜イランは米との直接交渉自体を否定し、交渉委員アジョルル氏は国営IRIBに対し「治安・機雷除去・海事サービスはイランが担う」というイラン主導の1〜3ヶ月の暫定管理案が基本方針だと説明｜最高指導者上級顧問レザイー将軍は3日、イラン指定と異なる航路の使用を米艦船に強制させようとすれば攻撃対象にすると警告｜UKMTOは3日22時（UTC）、オマーン・アルハサブ沖でリベリア籍バルカー「ミノアン・パイオニア」が飛翔体を受け機関室に損傷、乗員1名が行方不明と発表——2日には別の2隻（VLCC「エジプト・プロスペリティ」、アフラマックス「オン・プライド」）も警告射撃・爆発に遭遇したが無傷（Seatrade Maritime）｜イラン国営メディアはクウェートの米軍基地への無人機攻撃を主張したが米側の公式確認はまだ得られていない｜市場はホルムズ合意期待を強く織り込み、NYダウは連日の最高値、原油（WTI）は75ドル台へ続落｜日本関係船は残り4隻で変化なし｜封鎖159日目
</strong>
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🇺🇸 8/4 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:1.1rem;">🚨</span>
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">イラン・オマーンが航路座標に合意——一方でイラン議会は米・イスラエル船排除と通行料の法案を審議、米は即座に拒否</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/7 09:45 更新</span>
    </span>
  </div>

  <!-- 折りたたみ本体（デフォルト非表示） -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/7 09:45 速報】イラン外務省報道官バガイ氏は5日、ホルムズ海峡の安全航路についてオマーンと地理的座標で合意したと発表。両国の共同声明は最終調整・起草段階にあるとした（CNN/Bloomberg/Euronews）｜米メディアMS NOWは6日、オマーンが入域＝イラン管理ルート・出域＝オマーン管理ルートとする暫定枠組みに合意したと関係者の話として報道。イラン副外相ガリババディ氏はこの合意が海峡の自動的な全面再開を意味しないと釘を刺した（IRNA）｜一方、イラン議会の委員会は6日、米・イスラエル関連船を恒久的に排除し、その他の「敵対国」船には貨物価値最大7%の通行料を、違反船には20%の罰金を課す法案を審議していると国営ファールス通信が報道（Reuters/NPR）｜米政府高官はこの案を即座に拒否し、「承認・許可・通行料を一切伴わない自由な航行」を要求すると表明（CNBC）｜フーシ派は5日、サウジのヤンブー沖でタンカー「Wafa」に複数のミサイルを撃ち込んだと主張——7/22の紅海封鎖宣言以降、被弾したサウジタンカーは8隻目、引き返した船舶は29隻に達したとした（Reuters/AFP）｜市場では5日にNYダウが263ドル高の54,349.12ドルで3日連続最高値を更新したが、6日はハイテク株主導で反落。原油はイラン議会案への懸念からブレントが一時81ドル台へ反発する場面もあり、乱高下が続いている｜日本関係船は残り4隻で変化なし｜封鎖161日目
</strong>
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🇮🇷🇴🇲 8/5 JST</span>
  <span style="color:#e2e8f0;"> イラン外務省報道官エスマイル・バガイ氏は、対岸のオマーンと進めてきたホルムズ海峡の航行ルート協議について、両国提案ルートの地理的座標について合意に達したと発表。「特定の第三者が妨害しない限り」共同声明は最終レビュー・起草段階にあるとし、両国は過去2ヶ月にわたり技術・法的・安全保障・環境面の協議を重ねてきたと説明した。イラン・ラーラク島付近の暫定ルートとオマーン領海経由ルートは閉鎖される見通し。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇮🇷 8/6 JST</span>
  <span style="color:#e2e8f0;"> イラン議会の委員会が審議する法案は、米・イスラエル関連船舶をいかなる時も海峡通過から排除し、その他の「敵対国」船には戦争被害への補償として貨物価値最大7%の通行料を、条件違反時には20%の罰金を課す内容。法案はなお専門家審査中で、議会は確定前に専門家の意見提出を招請しているという。米政府高官はCNBCに対し「暫定ルートは承認・許可・通行料を一切伴わない自由な航行でなければならない」と述べ、この案を拒否する姿勢を示した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#6ee7b7;font-weight:700;">🇺🇸 8/4 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

### カード① 外交交渉

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🤝 米高官「合意は今日か明日にも」——浮上する二経路方式、封鎖解除が焦点</div>
        <div class="s-body">ベッセント財務長官は4日、CNBCでホルムズ海峡の「自由な航行」再開に向けた合意が「今日か明日にも」まとまり得ると発言。ルビオ国務長官も同日、米国が関与するオマーン・イラン協議で進展があったことを確認したが、最終合意には未到達と留保した。関係者によれば浮上している合意案は、湾内への入域はイラン管理ルート・湾外への出域はオマーン管理ルートとする二経路方式で、米側が対イラン封鎖を解除することが前提条件とされる。カタール政府は、両者の直接協議はないものの合意草案が「回覧されている」段階だと説明した。</div>
        <div class="s-src">出典: Washington Times / AP / Al Jazeera（8/4 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇮🇷🇴🇲 イラン・オマーンが航路座標に合意——共同声明は最終調整段階</div>
        <div class="s-body">イラン外務省報道官バガイ氏は5日、対岸のオマーンとホルムズ海峡の安全航路について地理的座標で合意したと発表。両国の共同声明は最終レビュー・起草段階にあるとした。米メディアMS NOWは6日、オマーンが入域＝イラン管理ルート・出域＝オマーン管理ルートとする暫定枠組みに合意したと関係者の話として報道。イラン副外相ガリババディ氏は、この合意自体が海峡の自動的な全面再開を意味するわけではないと強調しており、実現しても米の対イラン封鎖解除が前提条件である点は変わらない。</div>
        <div class="s-src">出典: CNN / Bloomberg / Euronews（8/5〜6 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 軍事情勢

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇮🇷 イラン、直接交渉を否定——「イラン主導の暫定管理」提示と米艦船への攻撃警告</div>
        <div class="s-body">イラン交渉委員のサイード・アジョルル氏は国営IRIBに対し、米国との直接交渉を否定した上で、交渉の狙いは「治安・機雷除去・海事サービスをイランが担う」1〜3ヶ月の暫定的な取り決めの確立にあると説明した。最高指導者モジュタバ・ハメネイ師の上級顧問モフセン・レザイー将軍も3日、イラン指定と異なる航路の使用を強制しようとする米艦船はいかなる艦船であっても攻撃対象になると警告し、米が海上封鎖を継続すれば米艦船・基地への攻撃も辞さない構えを示した。イラン国営メディアはクウェートの米軍基地へのドローン攻撃も主張しているが、米側の公式確認はまだない。</div>
        <div class="s-src">出典: IRIB / Jerusalem Post / AP（8/3〜4 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇮🇷 イラン議会、米・イスラエル船排除と通行料の法案を審議——米は即座に拒否</div>
        <div class="s-body">イラン議会の委員会は6日、米・イスラエル関連船舶を恒久的に海峡通過から排除し、その他の「敵対国」船には戦争被害への補償として貨物価値最大7%の通行料を、条件違反時には20%の罰金を課す法案を審議していると国営ファールス通信が報じた。法案はなお専門家審査中とされる。これに対し米政府高官はCNBCに対し「暫定ルートは承認・許可・通行料を一切伴わない自由な航行でなければならない」と述べ、案を拒否する姿勢を示した。イラン・オマーン間の技術合意と、イラン議会が目指す一方的な統制強化との間には温度差が浮き彫りになっている。</div>
        <div class="s-src">出典: Fars通信 / Reuters / NPR / CNBC（8/6 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ エネルギー・市場

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">📈 NYダウが連日最高値、原油はWTI75ドル台へ続落——合意期待が市場を牽引</div>
        <div class="s-body">4日のNY株式市場では、ホルムズ海峡合意への期待を背景にNYダウが前日比907.47ドル高の54,085.88ドルと連日で史上最高値を更新、S&P500も1.8%高の7,736.52と6月2日以来2ヶ月ぶりの高値をつけた。一方、原油（WTI）は前日比4.57ドル安の75.77ドルまで続落し、開戦前水準に接近。カザフスタンはCPCノヴォロシースク積出ターミナルからの原油積み出しを再開し、トルコ・イラクは石油パイプライン協定を1年延長した。UKMTOはオマーン海域でリベリア籍バルカー「ミノアン・パイオニア」の被弾（乗員1名行方不明）を発表しており、市場の楽観と現場の緊張とのギャップが続く。日本関係船は残り4隻から変化なし（8/5 10:24 JST再確認）。</div>
        <div class="s-src">出典: 日本経済新聞 / TradingEconomics / Seatrade Maritime（8/4〜5 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">📈 NYダウ3日連続最高値も6日反落、原油は乱高下——フーシ派はサウジタンカーを攻撃</div>
        <div class="s-body">5日のNY株式市場でNYダウは前日比263.24ドル高の54,349.12ドルと3日連続で史上最高値を更新したが、6日はハイテク株の利益確定売りに押され反落。エネルギー株は原油高を受け上昇した。原油はイラン議会の対米船排除・通行料法案への懸念からブレントが3営業日続落後に一時81ドル台まで反発、WTIは75ドル前後で推移するなど乱高下が続いている。フーシ派は5日、紅海のサウジ港湾都市ヤンブー沖でサウジタンカー「Wafa」に複数のミサイルを撃ち込んだと主張。7/22の封鎖宣言以降、被弾したサウジタンカーは8隻目、引き返した船舶は29隻に達したとしている。日本関係船は残り4隻から変化なし（8/7 09:45 JST再確認）。</div>
        <div class="s-src">出典: TheStreet / TradingEconomics / Reuters（8/5〜6 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 18「米高官が相次ぎ合意近しと表明——オマーン・イラン協議は前進、イランは独自の暫定管理案を提示」——封鎖159日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 19「イラン・オマーンが航路座標に合意も、イラン議会は米船排除・通行料の法案を審議——米は即座に拒否」——封鎖161日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🤝 <strong>ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）／浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提／イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示、レザイー将軍は代替航路を強制する米艦船への攻撃も辞さないと警告（8/3〜4）——日本関係船は残り4隻で変化なし——封鎖159日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残11日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①米側の楽観論どおり数日内に最終合意へ至るか ②入域イラン管理・出域オマーン管理の二経路案の実務詳細が固まるか ③イランの「1〜3ヶ月暫定管理」提案を米側が受け入れるか ④レザイー将軍の攻撃警告が現実化しないか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残11日（8/16）</span>
<!-- OLD:END -->
<!-- NEW:START -->
        🤝 <strong>イラン外務省がオマーンとホルムズ海峡の安全航路の座標に合意したと発表——共同声明は最終調整段階（8/5）／米メディアはオマーンが入域イラン管理・出域オマーン管理の暫定枠組みに合意したと報道（8/6）／一方イラン議会委員会は米・イスラエル船の恒久排除と他国船への最大7%通行料・違反時20%罰金の法案を審議、米政府は「無条件の自由航行」を求め即座に拒否（8/6）——フーシ派はサウジタンカー「Wafa」への攻撃を主張、紅海封鎖開始以降8隻目（8/5）——日本関係船は残り4隻で変化なし——封鎖161日目・MOU機雷除去期限（7/17）を未着手のまま徒過・MOU最終期限残9日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①イラン議会の対米・イスラエル排除／通行料法案を巡る対立が収束するか ②イラン・オマーンの共同声明が正式発表され、内容に米の関与が反映されるか ③米の「無条件自由航行」要求とイランの「許可制・通行料」要求の溝が埋まるか ④フーシ派の紅海攻撃激化がホルムズ情勢と連動してエスカレートしないか ⑤残る日本関係船4隻の安全確保</span>
        <br><span style="color:#fca5a5;">⏳ MOU機雷除去期限（7/17）を徒過・最終期限まで残9日（8/16）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー ⚠️（日付表記2箇所を両方確認）

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sec-title">📊 4つのシナリオ（2/28 開戦後・今後の展開）<span class="label-scenario" style="margin-left:8px;font-size:0.7rem;">シナリオ分析</span></div>
  <!-- シナリオ確率更新補足 -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
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
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sec-title">📊 4つのシナリオ（2/28 開戦後・今後の展開）<span class="label-scenario" style="margin-left:8px;font-size:0.7rem;">シナリオ分析</span></div>
  <!-- シナリオ確率更新補足 -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月7日 09:45 JST 更新</span><br>
  📊 <strong>イラン・オマーンは航路座標に合意も、イラン議会は米・イスラエル船排除と通行料の法案を審議——米は即座に拒否：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#fbbf24;">→</span> — イラン・オマーン間の技術的合意（航路座標）は進展だが、イラン議会の一方的な排除・通行料法案に米が即座に反発しており、全体としての合意成立には至っていない<br>
  🅑 膠着継続 <span style="color:#4ade80;">↑</span> — 二国間の技術協議は進む一方、米・イラン間の根本的な条件（無条件自由航行 vs 許可制・通行料）の溝は埋まっておらず、当面の膠着継続がより現実的な帰結となっている<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — イラン議会が提示する米・イスラエル船の恒久排除と通行料課税の法案は、海峡統制の制度化・恒久化そのものであり、Cシナリオの警戒する事態に一歩近づいた<br>
  🅓 全面対決・無期限封鎖 <span style="color:#fbbf24;">→</span> — フーシ派の紅海攻撃は継続しレザイー将軍の攻撃警告も撤回されていないが、本日時点で米・イラン間の直接的な軍事エスカレーションの新規報告はない<br>
  <strong style="color:#fbbf24;">イラン・オマーンの技術合意は前進材料だが、イラン議会の一方的な統制強化の動きが米の即時拒否を招いており、外交解決シナリオの勢いは足踏み。膠着継続とMOU形骸化のリスクがともに高まっている（A→ B↑ C↑ D→）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月7日 09:45 JST 時点での分析に基づく自動同期
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（タイトル・本文）

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>ベッセント財務長官の「今日か明日にも合意」発言とルビオ国務長官によるオマーン・イラン協議進展の確認は、Aシナリオにとって初めて具体的な合意の輪郭（入域イラン管理・出域オマーン管理の二経路方式）が語られた点で意義が大きい。ただし米の封鎖解除が前提とされており、実務面での詰めが今後の焦点となる。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>イラン・オマーンが安全航路の座標に合意し共同声明が最終調整段階に入ったことは、Aシナリオにとって具体的な前進材料である。しかしイラン議会が米・イスラエル船の恒久排除と通行料課税の法案を審議し、米政府がこれを即座に拒否したことで、二国間の技術合意と米・イラン間の根本条件のギャップが露呈した。全面再開に至るには、この溝を埋める必要がある。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>米高官の楽観的発言が相次ぐ一方、イラン交渉委員アジョルル氏は「治安・機雷除去・海事サービスはイランが担う」1〜3ヶ月の暫定管理案を基本方針として提示しており、これは実質的にイラン統制の期間限定的な既成事実化とも読める。従来の完全な膠着からは一歩進んだが、米側がこの提案をどこまで受け入れるかは未確定である。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>イラン・オマーンの二国間協議は座標合意まで進んだが、これは海峡再開の一部に過ぎない。イラン議会が審議する米船排除・通行料法案に米側が「無条件の自由航行」を要求して即時反発したことで、米・イラン間の根本条件は依然平行線のままである。技術面の進展と政治的対立が併存する状態が当面続く可能性が高い。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>イランが提示する「イラン主導1〜3ヶ月の暫定管理」案は、機雷除去・海事サービス・治安をイランが一手に担う内容であり、Cシナリオが警戒する封鎖の制度化・既成事実化そのものの構図に近い。米側がこの枠組みを合意として受け入れれば、短期的な航行再開と引き換えにイランの統制が事実上追認される可能性がある。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>イラン議会が審議する法案は、米・イスラエル船を恒久的に排除し、他国船には貨物価値最大7%の通行料と違反時20%の罰金を課す内容で、海峡統制の恒久的な制度化そのものである。1951年の石油国有化になぞらえる議員の発言もあり、イランが仮に協議中の技術合意を結んでも、この統制構造自体は維持される可能性が高い。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>市場は合意期待を強く織り込みNYダウが連日最高値を更新しているが、イラン最高指導者上級顧問レザイー将軍は3日、イラン指定と異なる航路の使用を強制する米艦船を攻撃対象にすると明言した。楽観的な外交報道の裏で軍事的な威嚇レトリックが同時進行しており、交渉が不調に終わった場合の再エスカレーションリスクは払拭されていない。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>フーシ派は5日、サウジのヤンブー沖でタンカー「Wafa」への攻撃を主張し、紅海封鎖開始（7/22）以降の被弾サウジタンカーは8隻目に達した。レザイー将軍の米艦船への攻撃警告も撤回されていない。ただし本日時点でホルムズ海峡そのものにおける米・イラン間の新たな直接軍事衝突の報告はなく、緊張は周辺海域（紅海）に分散している状況である。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5つ）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">ベッセント氏の言う「今日か明日」の期限内に最終合意へ至るか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">入域イラン管理・出域オマーン管理の二経路案の実務詳細（封鎖解除の具体的手順を含む）が固まるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">イランの「1〜3ヶ月・イラン主導」暫定管理提案を米側がどこまで受け入れるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">レザイー将軍の米艦船への攻撃警告が現実化しないか、クウェート基地攻撃の真偽が確認されるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保（変わらず最重要）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月5日 10:24 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">イラン議会の対米・イスラエル排除／通行料法案を巡る対立が収束するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イラン・オマーンの共同声明が正式発表され、内容に米の関与・同意が反映されるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">米の「無条件自由航行」要求とイランの「許可制・通行料」要求の溝が埋まるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">フーシ派の紅海攻撃激化がホルムズ情勢と連動してエスカレートしないか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保（変わらず最重要）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月7日 09:45 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー ⚠️（S08完了後・S09直前・忘れやすい）

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月5日 10:24 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">米高官が合意近しと相次いで発言する一方、イランは米との直接交渉を否定し独自の暫定管理案を提示——外交トラックは進展したが現場統制は依然イラン側にある。【北側航路（イラン指定）】イランは「治安・機雷除去・海事サービスをイランが担う」1〜3ヶ月の暫定管理案を提示しており、当面は同ルートでの統制継続が既定路線とみられる。【南ルート（Omani coastal corridor）】浮上する合意案では出域をオマーン管理ルートとする案が検討されており、実現すればイランと分担する形に変わる可能性がある。中央チャンネルの機雷約80個は除去未着手のまま、除去期限は7/17（MOU第5条）を徒過。【イラン・オマーン仲介】ルビオ国務長官が米国の関与と協議進展を確認——最終合意には未到達。【紅海・スエズ・黒海】カザフスタンはCPCノヴォロシースク積出ターミナルからの原油積み出しを再開、トルコ・イラクは石油パイプライン協定を1年延長するなど周辺ルートは部分的に平常化。【UKMTO 警戒水準】Substantial（継続）。オマーン・アルハサブ沖でリベリア籍バルカー「ミノアン・パイオニア」が3日22時（UTC）に飛翔体を受け機関室損傷・乗員1名行方不明、2日にも別の2隻が爆発・警告射撃に遭遇（無傷）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/5 10:24 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認・金子国交相の8/4会見でも言及なし）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月7日 09:45 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">イラン・オマーンは安全航路の座標に合意し共同声明は最終調整段階に入ったが、イラン議会は米・イスラエル船排除と通行料の法案を審議しており、外交トラックと国内政治の間に温度差が生じている。【北側航路（イラン指定）】イラン議会の法案が成立すれば「敵対国」船に貨物価値最大7%の通行料・違反時20%の罰金を課す統制ルートとして制度化される見通し。【南ルート（Omani coastal corridor）】オマーンは入域イラン管理・出域オマーン管理の暫定枠組みに合意したと報じられ、実現すれば南側の管理主体がオマーンに移る可能性がある。中央チャンネルの機雷約80個は除去未着手のまま、除去期限は7/17（MOU第5条）を徒過。【イラン・オマーン仲介】両国は技術合意まで到達も、副外相ガリババディ氏は全面再開を意味しないと釘を刺す。【紅海・スエズ・黒海】フーシ派がサウジタンカー「Wafa」への攻撃を主張——7/22の紅海封鎖宣言以降8隻目、引き返した船舶は29隻に達したとする。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。🇯🇵 日本関係船舶：残り4隻で変化なし（8/7 09:45 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認・金子国交相の8/4会見は熊本地震対応が主題でホルムズ言及なし）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）※最後に執筆

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
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
<!-- OLD:END -->
<!-- NEW:START -->
🇮🇷🇴🇲 イラン・オマーンが航路座標に合意——一方でイラン議会は米・イスラエル船排除と通行料の法案を審議し、米は即座に拒否。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📰 フーシ派がサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目。NYダウは3日連続最高値も6日反落。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ 米・イランの条件対立が収束するか焦点、封鎖161日目——機雷除去期限（7/17）を徒過・MOU最終期限（8/16）まで残9日。
</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(74,222,128,0.15);border:1px solid rgba(74,222,128,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🤝ベッセント氏「合意は今日か明日」</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚢入域イラン管理・出域オマーン管理案</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷イラン、直接交渉を否定</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📈NYダウ最高値・WTI75ドル台</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(74,222,128,0.15);border:1px solid rgba(74,222,128,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷🇴🇲航路座標に合意・共同声明調整中</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷議会が米船排除・通行料法案審議</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸米「無条件自由航行」要求で拒否</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📈NYダウ3日連続最高値も反落</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [C01] タンカー確認（SHIP_CONFIG dateConfirmed）

<!-- APPLY:START -->
<!-- OLD:START -->
  dateConfirmed: '2026年8月3日 09:46 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認。トランプ氏はサウジ皇太子の説得で対イラン攻撃を中止し月曜から交渉開始、イランは公式受諾せず現場の通航実態は不変）'
<!-- OLD:END -->
<!-- NEW:START -->
  dateConfirmed: '2026年8月7日 09:45 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の8/4会見は令和8年熊本地震の被災地対応が主題でホルムズ言及なし）'
<!-- NEW:END -->
<!-- APPLY:END -->

---

## JSON-LD dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-08-05T10:24:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-07T09:45:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新（latest 4件追加・archive移動・osint 2件追記）

<!-- FILE:docs/data/news_data.json -->

### 手順

1. `latest` 配列の**先頭に以下4件を追加**（新しい順）：

```json
[
  {
    "id": "latest-iran-oman-route-agree-0805",
    "title": "イラン・オマーンがホルムズ海峡の安全航路座標に合意——共同声明は最終調整段階",
    "body": "イラン外務省報道官エスマイル・バガイ氏は8月5日、対岸のオマーンと進めてきたホルムズ海峡の航行ルート協議について、両国提案ルートの地理的座標について合意に達したと発表した。共同声明は「特定の第三者が妨害しない限り」最終レビュー・起草段階にあるとした。イラン副外相ガリババディ氏は、この合意が海峡の自動的な全面再開を意味するわけではないと述べている。",
    "sourceLabel": "CNN / Bloomberg / Euronews",
    "date": "2026年8月5日（現地）/ 2026年8月6日 JST",
    "label": "🤝 外交",
    "url": "https://www.cnn.com/2026/08/05/world/live-news/iran-war-trump",
    "isLatest": true
  },
  {
    "id": "latest-iran-parliament-ban-toll-0806",
    "title": "イラン議会、米・イスラエル船の排除と他国船への通行料課税の法案を審議",
    "body": "イラン議会の委員会は8月6日、米・イスラエル関連船舶を恒久的にホルムズ海峡通過から排除し、その他の「敵対国」船には貨物価値最大7%の通行料を、条件違反時には20%の罰金を課す法案を審議していると国営ファールス通信が報じた。法案はなお専門家審査中で、議会は確定前に専門家の意見提出を招請しているという。",
    "sourceLabel": "Reuters / NPR",
    "date": "2026年8月6日（現地）/ 2026年8月6日 JST",
    "label": "🇮🇷 政治",
    "url": "https://www.npr.org/2026/08/06/nx-s1-5923623/iran-strait-hormuz-us-israel-ban",
    "isLatest": true
  },
  {
    "id": "latest-us-rejects-iran-toll-plan-0806",
    "title": "米政府、イランの通行料・排除案を即座に拒否——「無条件の自由航行」を要求",
    "body": "イラン議会の対米船排除・通行料法案の報道を受け、米政府高官はCNBCに対し「暫定ルートは承認・許可・通行料を一切伴わない自由な航行でなければならない」と述べ、この案を拒否する姿勢を明確にした。トランプ大統領は「ホルムズ海峡はまもなく開放される」としつつ、「（イランが）再び後退すれば手痛い報いを受けるだろう」とも述べている。",
    "sourceLabel": "CNBC",
    "date": "2026年8月6日（現地）/ 2026年8月6日 JST",
    "label": "🇺🇸 外交",
    "url": "https://www.cnbc.com/2026/08/06/us-iran-war-hormuz-trump-bessent-deal.html",
    "isLatest": true
  },
  {
    "id": "latest-houthi-saudi-tanker-wafa-0805",
    "title": "フーシ派、サウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目",
    "body": "イエメンの親イラン武装組織フーシ派は8月5日、サウジアラビアの紅海側港湾都市ヤンブー沖でサウジ籍タンカー「Wafa」に複数のミサイルを撃ち込んだと発表した。フーシ派報道官ヤヒヤ・サリア氏は、7月22日の紅海封鎖宣言以降、攻撃を受けたサウジタンカーは8隻目、引き返した船舶は29隻に達したと述べ、サウジが南側を避け北側ルートへタンカーを迂回させていることへの対抗措置として攻撃を継続・激化させると表明した。",
    "sourceLabel": "Reuters / AFP",
    "date": "2026年8月5日（現地）/ 2026年8月5日 JST",
    "label": "⚔️ 軍事",
    "url": "https://www.dailysabah.com/world/mid-east/yemens-houthis-reportedly-strike-saudi-tanker-transiting-red-sea",
    "isLatest": true
  }
]
```

2. 現在 `latest` にある最古の4件（`id`: `latest-minoan-pioneer-hit-0803` ／ `latest-trump-halts-strikes-saudi-mbs-0801` ／ `latest-trump-talks-monday-iran-0802` ／ `latest-dow-record-oil-drop-0804`）を `archive` の**新規バッチ**（`batchLabel: "2026年8月1日〜4日"`）として移動。
3. `updated` フィールドを `"2026年8月7日 09:45 日本時間JST"` に更新。
4. `staleNotice` は空文字のままとする（新情報あり）。

### osint 配列への追記（先頭に2件、既存の isLatest:true は false に変更）

既存の先頭要素（`titleJa: "【Al Jazeera】米、ホルムズ再開合意近しと発言..."`）の `isLatest` を `true` → `false` に変更した上で、以下2件を配列先頭に追加：

```json
[
  {
    "titleJa": "【NPR】イラン、米・イスラエル船のホルムズ海峡締め出しと通行料徴収を狙う",
    "titleEn": "Iran aims to ban U.S. and Israeli ships from Strait of Hormuz and charge others a toll",
    "country": "アメリカ",
    "media": "NPR",
    "cardBg": "rgba(56,189,248,0.05)",
    "cardBorder": "rgba(56,189,248,0.25)",
    "badgeColor": "#38bdf8",
    "borderColor": "rgba(56,189,248,0.4)",
    "textColor": "#7dd3fc",
    "url": "https://www.npr.org/2026/08/06/nx-s1-5923623/iran-strait-hormuz-us-israel-ban",
    "date": "2026年8月6日（現地）/ 2026年8月6日 JST",
    "isLatest": true
  },
  {
    "titleJa": "【Euronews】イラン・オマーン、ホルムズ海峡の航路で合意——米は関与せずとイラン主張",
    "titleEn": "Iran and Oman agree route for ships in Strait of Hormuz, Tehran says",
    "country": "イラン",
    "media": "Euronews",
    "cardBg": "rgba(56,189,248,0.05)",
    "cardBorder": "rgba(56,189,248,0.25)",
    "badgeColor": "#38bdf8",
    "borderColor": "rgba(56,189,248,0.4)",
    "textColor": "#7dd3fc",
    "url": "https://www.euronews.com/2026/08/05/iran-and-oman-agree-route-for-ships-in-strait-of-hormuz-tehran-says",
    "date": "2026年8月5日（現地）/ 2026年8月6日 JST",
    "isLatest": false
  }
]
```

---

## [S11] 更新ログ — 2ブロック構成

### ブロック1：常時表示エリア（3件固定を維持）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月5日 10:24 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/05 10:24</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）・浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提（AP/Washington Times）・イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示（IRIB）・レザイー最高指導者上級顧問は代替航路を強制する米艦船への攻撃も辞さないと警告・UKMTOはオマーン沖でリベリア籍バルカー「ミノアン・パイオニア」の被弾を発表（乗員1名行方不明）・イラン国営メディアはクウェート米軍基地への攻撃を主張したが米側未確認・NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75.77ドルへ続落・日本関係船は残り4隻で変化なし・封鎖159日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月3日 09:46 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/03 09:46</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ氏、サウジのムハンマド皇太子から電話で説得を受け週末の対イラン大規模攻撃を土壇場で中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及し月曜からイランと交渉開始へ（Newsweek/NPR）・イラン軍代行国防相は「心理作戦」と一蹴、半官営メール通信は「新たな虚偽」と反発——イラン政府は公式受諾を表明せず（Al Jazeera）・イラン国営ファールス通信は北側航路になお多数の船舶が足止めされたままと報道・UKMTOはオマーン沖でタンカー「ガスログ・シャンハイ」の被弾を発表（7/31・機関室損傷）・クウェート軍はイラン系ドローンを迎撃（8/1）——NYTはIRGCが4月停戦中にフーシ派・ヒズボラ・イラク民兵と共謀し戦線拡大を図っていたと報道・原油はブレントが前日比4.65%安の83.84ドルへ急落（8/2）・日本関係船は残り4隻で変化なし・封鎖157日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月1日 10:51 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/01 10:51</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>戦線が中東域外へ拡大——エジプト・ダミエッタ港でLNG貯蔵船「エナゴス・ウィンター」がドローン攻撃を受け出火、隣接LNG船「ガスログ・セーラム」にも延焼（今次紛争で初のエジプト領内攻撃・Reuters/CNBC）・カザフスタンのCPCノヴォロシースク積出ターミナルもタンカー攻撃を受け3日で再停止（7月中8隻超が被弾）・イランは「米軍護衛下」で海峡を出域しようとしたタンカー2隻を拿捕・4隻を引き返させたと主張したが西側は未確認（Reuters）・オマーンとの海峡共同管理協議はイラン高官が「成功の見込みなし」と改めて拒否・米・イラン間の直接空爆は7/30夜〜31未明は報告なし・原油はブレント90.12ドル・WTI84.67ドル（ともに前日比+1%超・7月月間+23%見通し）・日本関係船は残り4隻で変化なし・封鎖155日目・ニュース4件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月7日 09:45 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/07 09:45</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン外務省、ホルムズ海峡の安全航路座標についてオマーンと合意したと発表——共同声明は最終調整段階（IRNA、8/5）・米メディアはオマーンが入域イラン管理・出域オマーン管理の暫定枠組みに合意と報道（MS NOW、8/6）・一方イラン議会委員会は米・イスラエル船の恒久排除と他国船への最大7%通行料・違反時20%罰金の法案を審議（Fars通信）・米政府はこの案を即座に拒否し無条件の自由航行を要求（CNBC）・フーシ派はサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目、29隻が引き返し（Reuters）・NYダウは263ドル高の54,349.12ドルで3日連続最高値も6日は反落・原油は乱高下しブレントが一時81ドル台へ反発・日本関係船は残り4隻で変化なし・封鎖161日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月5日 10:24 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/05 10:24</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官「合意は今日か明日にも」・ルビオ国務長官はオマーン・イラン協議の進展を確認するも最終合意は未成立と留保（8/4）・浮上する合意案は入域イラン管理・出域オマーン管理の二経路方式で米の封鎖解除が前提（AP/Washington Times）・イランは直接交渉を否定し「イラン主導1〜3ヶ月の暫定管理」案を提示（IRIB）・レザイー最高指導者上級顧問は代替航路を強制する米艦船への攻撃も辞さないと警告・UKMTOはオマーン沖でリベリア籍バルカー「ミノアン・パイオニア」の被弾を発表（乗員1名行方不明）・イラン国営メディアはクウェート米軍基地への攻撃を主張したが米側未確認・NYダウは907ドル高の54,085ドルで連日最高値、原油はWTIが75.77ドルへ続落・日本関係船は残り4隻で変化なし・封鎖159日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月3日 09:46 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/03 09:46</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ氏、サウジのムハンマド皇太子から電話で説得を受け週末の対イラン大規模攻撃を土壇場で中止——「ホルムズ海峡の即時・完全開放」を含む枠組み合意に言及し月曜からイランと交渉開始へ（Newsweek/NPR）・イラン軍代行国防相は「心理作戦」と一蹴、半官営メール通信は「新たな虚偽」と反発——イラン政府は公式受諾を表明せず（Al Jazeera）・イラン国営ファールス通信は北側航路になお多数の船舶が足止めされたままと報道・UKMTOはオマーン沖でタンカー「ガスログ・シャンハイ」の被弾を発表（7/31・機関室損傷）・クウェート軍はイラン系ドローンを迎撃（8/1）——NYTはIRGCが4月停戦中にフーシ派・ヒズボラ・イラク民兵と共謀し戦線拡大を図っていたと報道・原油はブレントが前日比4.65%安の83.84ドルへ急落（8/2）・日本関係船は残り4隻で変化なし・封鎖157日目・ニュース4件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse 先頭への旧3件目挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月30日 10:08 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月1日 10:51 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/01 10:51</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>戦線が中東域外へ拡大——エジプト・ダミエッタ港でLNG貯蔵船「エナゴス・ウィンター」がドローン攻撃を受け出火、隣接LNG船「ガスログ・セーラム」にも延焼（今次紛争で初のエジプト領内攻撃・Reuters/CNBC）・カザフスタンのCPCノヴォロシースク積出ターミナルもタンカー攻撃を受け3日で再停止（7月中8隻超が被弾）・イランは「米軍護衛下」で海峡を出域しようとしたタンカー2隻を拿捕・4隻を引き返させたと主張したが西側は未確認（Reuters）・オマーンとの海峡共同管理協議はイラン高官が「成功の見込みなし」と改めて拒否・米・イラン間の直接空爆は7/30夜〜31未明は報告なし・原油はブレント90.12ドル・WTI84.67ドル（ともに前日比+1%超・7月月間+23%見通し）・日本関係船は残り4隻で変化なし・封鎖155日目・ニュース4件更新・osint更新</div>
          <div>📅 <strong>2026年7月30日 10:08 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ 合計エントリー数（常時表示3 + log-collapse内）は現時点で11件以下のため、最古エントリーの削除は不要。

---

## [S12] archive_timeline.json への追記（既存エントリーは変更しない）

<!-- FILE:docs/data/archive_timeline.json -->

`entries` 配列の末尾に、以下のエントリーを追加してください（既存エントリーは変更しないこと）。
`blockadeDay` フィールドは表示には使用されません（2026-08-07の `calcBlockadeDay()` 導入により動的計算化済み）が、データの一貫性のため記入します。

```json
{
  "date": "2026-08-07",
  "dateLabel": "2026/08/07 09:45",
  "blockadeDay": 161,
  "summary": "イラン外務省、ホルムズ海峡の安全航路座標についてオマーンと合意したと発表——共同声明は最終調整段階（IRNA、8/5）・米メディアはオマーンが入域イラン管理・出域オマーン管理の暫定枠組みに合意と報道（MS NOW、8/6）・一方イラン議会委員会は米・イスラエル船の恒久排除と他国船への最大7%通行料・違反時20%罰金の法案を審議（Fars通信）・米政府はこの案を即座に拒否し無条件の自由航行を要求（CNBC）・フーシ派はサウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目、29隻が引き返し（Reuters）・NYダウは263ドル高の54,349.12ドルで3日連続最高値も6日は反落・原油は乱高下しブレントが一時81ドル台へ反発・日本関係船は残り4隻で変化なし・封鎖161日目・ニュース4件更新・osint更新",
  "relatedNews": [
    {"title": "イラン・オマーンがホルムズ海峡の安全航路座標に合意——共同声明は最終調整段階", "url": "https://www.cnn.com/2026/08/05/world/live-news/iran-war-trump", "sourceLabel": "CNN / Bloomberg / Euronews"},
    {"title": "イラン議会、米・イスラエル船の排除と他国船への通行料課税の法案を審議", "url": "https://www.npr.org/2026/08/06/nx-s1-5923623/iran-strait-hormuz-us-israel-ban", "sourceLabel": "Reuters / NPR"},
    {"title": "米政府、イランの通行料・排除案を即座に拒否——「無条件の自由航行」を要求", "url": "https://www.cnbc.com/2026/08/06/us-iran-war-hormuz-trump-bessent-deal.html", "sourceLabel": "CNBC"},
    {"title": "フーシ派、サウジタンカー「Wafa」への攻撃を主張——紅海封鎖開始以降8隻目", "url": "https://www.dailysabah.com/world/mid-east/yemens-houthis-reportedly-strike-saudi-tanker-transiting-red-sea", "sourceLabel": "Reuters / AFP"}
  ]
}
```

---

## Claude Code への引き継ぎ指示（必須手順）

```
1. git pull --rebase
2. 本ファイル（docs/tools/index_html_diffs.md）のAPPLYブロックを docs/index.html に順次適用
   （S01〜S09・C01・JSON-LD・S11の全APPLYブロック）
3. [S10] の指示に従い、docs/data/news_data.json を直接編集
   （latestへ4件追加・archiveへ4件移動・osintへ2件追記・updated更新）
4. [S12] の指示に従い、docs/data/archive_timeline.json の entries 配列末尾に新規エントリーを追加
   （既存エントリーは一切変更しない）
5. 全OLD blockが index.html 内で「完全に1回だけ」マッチすることをPythonで検証（count==1）
6. commit（コミットメッセージ例: "update: 2026-08-07 09:45 JST — イラン・オマーンが航路座標に合意、イラン議会は米船排除・通行料法案審議、封鎖161日目"）
7. push は必ずユーザー確認後に実施
```
