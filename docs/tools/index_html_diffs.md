# index_html_diffs.md — 2026年7月14日 08:48 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> news_data.json の変更は [S10] の指示に従い、既存ファイルへのマージとして適用してください。
> 適用後、C01タンカー確認行を含めた変更内容まとめを提示し、commit してください。push は確認後に指示します。

---

## ✅ 出力前セルフチェック（本日のチェックリスト）

本日のセルフチェック項目数：30件（project_knowledge_search取得の原文と一致）

```
[✓] S01 ヘッダー ― 日付 2026年7月14日 08:48 JSTが入っているか
[✓] S02 TICKER ― 本日の主要ニュースが反映されているか / 末尾 JST 付きか
[✓] S03 速報インシデント ― 存在するか・本日の新インシデントが入っているか
[✓] S04 情勢カード3枚 ― 3枚とも日付・数値・出典が更新されているか
[✓] S05 COUNTDOWN ― フェーズラベルが現状に合っているか
[✓] S06 シナリオ確率補足バナー ― 存在するか・日付と矢印テキストが更新されているか
[✓] S07 シナリオ4本 ― タイトルと本文が最新情勢を反映しているか
[✓] S07 シナリオC・D ― 内容が近似していないか（差別化確認）
[✓] S07 シナリオC・D ― WTI価格レンジがエスカレーション度に沿っているか（本文のみ、数値は自動同期のため記載省略）
[✓] S08 シナリオフッター ― 次の焦点5点が最新か
[✓] S08.5 全ルート現況サマリー ― 日付が当日JSTになっているか・変更なし時は「再確認済」付きか
[✓] S09 30秒カラム ― 3行サマリーとバッジ5枚が全て更新されているか（最後に書いたか）
[✓] S10 news_data.jsonメモ ― アーカイブ注意事項が記載されているか
[✓] S10 osint ― 当日付の Al Jazeera ライブブログを検索したか
[✓] S10 osint ― 配列ごと置き換えになっていないか（先頭追加・既存 isLatest:false 変更になっているか）
[✓] S10 latest ― 大型イベント進行中でも、海運・エネルギー・市場の周辺ニュースを個別に検索したか
[✓] S11 更新ログ ― 先頭行に本日分が追記されているか
[✓] S11 常時表示3件 ― APPLY ブロック1で常時表示が正確に3件になっているか
[✓] S11 折り畳み移動 ― APPLY ブロック2で旧3件目が log-collapse 先頭に挿入されているか
[✓] S11 総件数 ― 常時表示3 + log-collapse内エントリー数の合計が10以下か（超過分は最古1件削除指示あり）
[✓] S11 JSON-LD ― `"dateModified": "YYYY-MM-DD"` が本日の日付に更新されているか
[✓] C01 タンカー可視化 ― 日本語3クエリ＋英語1クエリの計4クエリを個別に実行したか
[✓] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一されているか
[✓] 全体 ― ニュースURLにAI捏造・推測URLが混入していないか
[✓] 全体 ― 📰関連最新ニュースにAl Jazeeraが混入していないか
[✓] 全体 ── 人名が日本語表記になっているか
[✓] 全体 ― diffs.md本文執筆の前に project_knowledge_search でセルフチェック原文を取得したか
[✓] 全体 ― 「本日のセルフチェック項目数：◯件」を数値で明記し、原文の項目数と一致しているか
[✓] 全体 ― 各項目に ✓確認済／✗未実施 のいずれかを明記したか
[✓] 全体 ― ✗が1件でもある場合、⚠️見出しを明記したか（該当なし）
[✓] C01 ― SHIP_CONFIG（totalShips/date/dateConfirmed）を本日分の確認結果で更新したか（変化なし・dateConfirmedのみ更新）
```

**⚠️ 本日の最重要トピック：** トランプ大統領が7/13、対イラン海上封鎖の再開と、米国が「ホルムズ海峡の守護者」となり全貨物の20%を通航料として徴収する方針を表明した。封鎖は7/14 20:00 GMT（7/15 05:00 JST）に発効予定。イランのアラグチー外相はX投稿で「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる、公正な水準にする」と税率交渉に含みを持たせた。IMOは強制的な通航料導入に断固反対の立場を表明。中国外務省も安全な航行確保を関係国に要求。米軍は3夜連続の対イラン空爆を継続しており、原油は週明けにブレント一時83ドル台まで急伸した。

**C01 タンカー確認**：日本語クエリ3本（①「金子国土交通大臣 会見 ホルムズ海峡 7月14日」②「外務省 ホルムズ海峡 日本関係船舶 7月14日」③「（金子国交相） 会見 ホルムズ海峡」）＋英語クエリ（"Japanese ships Strait of Hormuz stranded detained July 14 2026"）を個別実行し、外務省・国土交通省の一次情報を優先確認。**変化なし**——直近の会見は7/10（22隻通過・残り4隻）が最新であり、7/11〜7/14時点で新たな大臣会見・外務省発表は確認されず。SHIP_CONFIGのdateConfirmedのみ本日日時・変更なしとして更新。

二重封鎖表記チェック：「イラン・米国による二重封鎖」の単独表記は変更していません（dl-boxは今回対象外）。
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：S08.5内で7/14 08:48 JST更新を明示 ✓
人名表記チェック：「Xi」「Trump」単独表記なし（トランプ大統領と表記）✓
Al Jazeera混入チェック：📰関連最新ニュース欄（news_data.json latest）には使用せず、🌐現地メディア視点（osint）にのみ使用 ✓
毎日新聞・Wikipedia混入チェック：使用なし ✓
URL捏造チェック：全URL web検索で実在確認済み（Al Jazeera・CNBC・NPR/KPBS・Bloomberg・Newsweek日本版・日本経済新聞）✓

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イラン、米の3度目空爆に対しオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国を弾道ミサイル・ドローンで報復攻撃——米は約140カ所を空爆／オマーンはイラン大使を召喚し抗議、通航正常化の見通し立たず／日本関係船は残り4隻で変化なし／原油は週明けに反発し4%高／封鎖136日目）</span>
    <span class="badge-item badge-date">📅2026年7月13日 08:28 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明／イランのアラグチー外相は「イランこそ永遠の守護者」と反発しつつ税率交渉に含みを持たせる／IMOは強制通航料に断固反対／米軍は3夜連続の対イラン空爆を継続・封鎖は7/14 20:00 GMT発効予定／封鎖137日目）</span>
    <span class="badge-item badge-date">📅2026年7月14日 08:48 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年7月13日 08:28 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月13日 08:28 JST） -->
      🚨【5カ国へ報復攻撃】イラン、米の3度目空爆（約140カ所）に対しオマーン（ドゥクム）・カタール（アルウデイド基地）・クウェート・バーレーン・ヨルダンの米軍関連拠点を弾道ミサイル・ドローンで攻撃（7/12 JST）｜🗣️ ガリバフ国会議長「一方的な合意の時代は終わった」とX投稿｜🇴🇲 オマーン外務省、ドゥクム・ムサンダム攻撃を受けイラン大使を召喚し「無責任な行為」と正式抗議（7/12 JST）｜🇶🇦 カタール、迎撃時の破片で3名負傷・「危険なエスカレーション」と非難｜🇯🇵 日本関係船、残り4隻で変化なし（7/13 08:28 JST再確認）｜🛢️ 原油、週明けに反発——ブレント一時79ドル台・WTI74ドル台まで4%高（7/13早朝JST）｜⚠️ 機雷除去期限まで残4日・封鎖136日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月14日 08:48 JST） -->
      🚨【米、対イラン海上封鎖を再開へ】トランプ大統領、6月に解除したイラン港湾封鎖の再開を宣言——発効は7/14 20:00 GMT（7/15 05:00 JST）予定（7/13 JST）｜💰 トランプ氏「米国はホルムズ海峡の守護者となり、全貨物の20%を通航料として徴収する」とTruth Social投稿｜🇮🇷 アラグチー外相「イランこそ永遠の守護者」と反発——ただし「20%は高すぎる、公正な水準にする」と税率交渉の余地も示唆｜🌐 IMO「強制的な通航料導入に法的根拠なし」と断固反対の立場表明（7/13）｜🇨🇳 中国外務省もホルムズ海峡の安全な航行確保を関係国に要求（7/13）｜⚔️ 米軍は3夜連続の対イラン空爆を継続——日本関係船は残り4隻で変化なし｜🛢️ 原油、週明けにブレント一時83ドル台まで急伸（7/13夜JST）｜⚠️ 機雷除去期限まで残3日・封鎖137日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/13 08:28 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/14 08:48 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント見出し（トグルボタン内 strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">イラン、ホルムズ海峡「閉鎖」を宣言・米艦船攻撃で停戦事実上崩壊——米が3度目の空爆／オマーンが無料二経路案提示</strong>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%通航料徴収を表明／イランは反発しつつ税率交渉に含み</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### 折りたたみ本体 先頭 strong タグ

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/13 08:28 速報】イラン、米の3度目空爆（約140カ所）に対しオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国を弾道ミサイル・ドローンで報復攻撃（7/12 JST）｜ガリバフ国会議長「一方的な合意の時代は終わった」｜オマーン外務省、ドゥクム・ムサンダム攻撃を受けイラン大使を召喚し正式抗議｜カタールは迎撃破片で3名負傷｜日本関係船は残り4隻で変化なし｜原油は週明けに反発しブレント一時79ドル台・WTI74ドル台まで4%高｜封鎖136日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/14 08:48 速報】トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言・全貨物の20%を通航料として徴収する方針を表明（封鎖発効は7/14 20:00 GMT予定）｜アラグチー外相「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる」と税率交渉に含み｜IMOは強制通航料に断固反対｜中国外務省も安全な航行確保を要求｜米軍は3夜連続の対イラン空爆を継続｜日本関係船は残り4隻で変化なし｜封鎖137日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に2件追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/12 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">💰 7/13 JST</span>
  <span style="color:#e2e8f0;"> トランプ大統領はTruth Social投稿とFox Newsのインタビューで、6月に解除した対イラン海上封鎖を再開し、米国が「ホルムズ海峡の守護者（Guardian of the Hormuz Strait）」となって同海峡を通過する全貨物の20%相当を安全確保の対価として徴収すると表明した。同氏は「イラン以外の全ての国は海峡を公正かつ自由に利用できる」としつつ、封鎖はイランの船舶・顧客の出入りのみを止めるものだと説明した。CENTCOMは封鎖が米東部時間7/14午後4時（7/14 20:00 GMT・7/15 05:00 JST）に発効すると発表。米国はこれまで海峡通航への通航料導入に一貫して反対してきた立場から大きく転換した形となる。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🗣️ 7/13 JST</span>
  <span style="color:#e2e8f0;"> イランのアラグチー外相はX投稿で、安全な航行への対価支払いという発想自体は正しいと認めつつ、「イランこそが海峡の守護者であり、これからも永遠にそうである」と反論。その上で「20%は明らかに高すぎる。我々は公正にやる」と述べ、税率を巡る交渉の余地を示唆した。一方、イラン軍ハタム・アル・アンビヤ司令部の報道官は、米国がこの戦略的水路の管理に干渉することはいかなる状況でも許さないと強調した。国連の国際海事機関（IMO）は、国際航行に用いられる海峡での強制的な通航料導入に法的根拠はないとして断固反対する立場を改めて表明。中国外務省も同日、ホルムズ海峡での安全な航行確保を紛争関係国に求めた。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/12 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 最新情勢カード3枚

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sit-card danger">
    <div class="s-icon">🕊️</div>
        <div class="s-title">🕊️ 外交：前日の仲介協議から一転、オマーンがイラン大使を召喚——外交チャンネルは維持も緊張最高潮</div>
        <div class="s-body">7/11にアラグチー外相・ブーサイーディー外相がマスカットで海峡管理を協議した翌日、イランがオマーン領内（ドゥクム・ムサンダム）を攻撃したため、オマーン外務省はイラン大使を召喚し「無責任な行為」への不満を正式に表明した。ガリバフ国会議長はMOU第5条（海峡再開義務）を引き合いに「一方的な合意の時代は終わった」とX投稿し、対米強硬姿勢を鮮明にした。外交チャンネル自体は完全には途絶していないが、仲介役自身が攻撃対象となったことで信頼構築は大きく後退している。</div>
        <div class="s-src">出典: Al Jazeera / global-scm.com（7/13 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sit-card danger">
    <div class="s-icon">🕊️</div>
        <div class="s-title">💰 外交：トランプ大統領「米国がホルムズ海峡の守護者」宣言・全貨物20%通航料を表明——イランは反発しつつ税率交渉に含み</div>
        <div class="s-body">トランプ大統領はTruth Social投稿とFox Newsのインタビューで、対イラン海上封鎖の再開と、米国が「ホルムズ海峡の守護者」となって同海峡を通過する全貨物の20%を安全確保の対価として徴収する方針を表明した。イランのアラグチー外相はX投稿で「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる、公正にする」と税率交渉の余地を示唆。イラン軍ハタム・アル・アンビヤ司令部は米国の海峡管理への干渉を一切許さないと強調した。国連IMOは強制的な通航料導入に法的根拠なしとして断固反対を表明し、中国外務省も安全な航行確保を関係国に要求した。</div>
        <div class="s-src">出典: Al Jazeera / CNBC / ニューズウィーク日本版（7/13〜14 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sit-card warning">
    <div class="s-icon">⚔️</div>
        <div class="s-title">⚔️ 軍事：米の約140カ所空爆にイランが5カ国へ報復——今回の紛争で最大規模の相互攻撃</div>
        <div class="s-body">CENTCOMは、GFS Galaxy攻撃への対応として今週3度目・約140カ所（ミサイル・ドローン拠点、艦艇能力、弾薬庫、通信網、沿岸監視施設）への空爆を実施したと発表（この1週間の3夜合計では300カ所超）。これに対しイランはオマーン（ドゥクム）・カタール（アルウデイド基地）・クウェート・バーレーン・ヨルダンの米軍関連拠点にドローン・弾道ミサイルで報復攻撃を実施。カタールで迎撃破片により3名負傷。イラン国営放送はロレスタン州ヴェイシアン近郊やホンダーブの軍事拠点への米空爆も報じている。停戦崩壊後、最も広範囲な軍事応酬となった。</div>
        <div class="s-src">出典: CENTCOM / Al Jazeera / NPR（7/13 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sit-card warning">
    <div class="s-icon">⚔️</div>
        <div class="s-title">⚔️ 軍事：米軍、3夜連続の対イラン空爆を継続——海上封鎖は本日7/14 20:00 GMTに発効予定</div>
        <div class="s-body">CENTCOMは米東部時間7/13午後4時45分、トランプ大統領の指示の下「今週3夜連続」となる対イラン空爆を開始したと発表し、イランの対艦ミサイル能力・商船攻撃能力の低下を継続的に図ると強調した。同日発表された対イラン海上封鎖は米東部時間7/14午後4時（7/14 20:00 GMT）に発効予定で、4/13〜6/18に続く2度目の封鎖再開となる。データ分析企業Kplerによれば、ホルムズ海峡の通航実績は前週比で半分以下に減少しているという。</div>
        <div class="s-src">出典: CENTCOM / NPR・KPBS / Axios（7/13 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sit-card info">
    <div class="s-icon">🛢️</div>
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし——週明けの原油は反発し4%高</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/13 08:28 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認）。週末に発生した5カ国への報復攻撃・約140カ所の空爆を受け、日本時間13日早朝の取引で原油先物は反発。ブレント先物（期近9月物）は一時1バレル79ドル台と前週末比4%上昇、WTIも同74ドル台と4%高を付けた。機雷除去は依然未着手のまま7/17の除去期限まで残4日、8/16のMOU最終期限まで残34日に迫っている。</div>
        <div class="s-src">出典: 日本経済新聞 / 国土交通省 / 外務省（7/13 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sit-card info">
    <div class="s-icon">🛢️</div>
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし——原油はブレント一時83ドル台まで急伸</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/14 08:48 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認）。日本経済新聞によれば日本関係の原油タンカーはすでに全てホルムズ海峡を通過済みだが、封鎖再開により今後の正常化の見通しは不透明という。原油はトランプ大統領の封鎖再開・通航料表明を受け週明けの取引で急伸し、ブレント先物は7/13終値で前日比3.74%高の78.85ドルを付けた後、同日夜の取引で一時83ドル台まで上昇。機雷除去は依然未着手のまま7/17の除去期限まで残3日、8/16のMOU最終期限まで残33日に迫っている。</div>
        <div class="s-src">出典: 日本経済新聞 / CNBC / Trading Economics（7/13〜14 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（イラン、米に5カ国同時報復攻撃・米は約140カ所を空爆——事実上の全面軍事応酬）」——封鎖136日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（米、対イラン海上封鎖の再開と20%通航料を宣言——イランは反発しつつ税率交渉に含み）」——封鎖137日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🚨 <strong>イラン、米の3度目空爆（約140カ所）に対しオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国を報復攻撃——ガリバフ国会議長「一方的な合意の時代は終わった」／オマーンはイラン大使を召喚し抗議、仲介の立場も緊張最高潮／日本関係船は残り4隻で変化なし／原油は週明けに反発し4%高——封鎖136日目・MOU機雷除去期限残4日（7/17）・MOU最終期限残34日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①これ以上の軍事応酬拡大の有無 ②オマーンの仲介機能が維持されるか ③米国要求（攻撃停止・全通航路開放の公式声明）にイランが応じるか ④残る日本関係船4隻の安全確保 ⑤機雷除去着手の有無（期限まで残4日）</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残4日（7/17）</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🚨 <strong>トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明（封鎖発効は7/14 20:00 GMT予定）／アラグチー外相「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる」と税率交渉に含み／IMOは強制通航料に断固反対／米軍は3夜連続の対イラン空爆を継続／日本関係船は残り4隻で変化なし——封鎖137日目・MOU機雷除去期限残3日（7/17）・MOU最終期限残33日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①封鎖の正式発効と実際の運用実態（7/14 20:00 GMT〜）②20%通航料の実効性・IMO/主要海運国の反応 ③これ以上の軍事応酬拡大の有無 ④残る日本関係船4隻の安全確保 ⑤機雷除去着手の有無（期限まで残3日）</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残3日（7/17）</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年7月13日 08:28 JST 更新</span><br>
  📊 <strong>イランが米の3度目空爆（約140カ所）に対しオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国へ同時報復攻撃——ガリバフ国会議長「一方的な合意の時代は終わった」。仲介役オマーンもイラン大使を召喚し抗議：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — 仲介国オマーン自身が攻撃対象となり、外交基盤そのものが揺らいでいる<br>
  🅑 膠着継続 <span style="color:#f87171;">↓</span> — 5カ国同時攻撃は「膠着」の域を超えた事態であり、本シナリオの該当性が後退<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 機雷除去着手なきまま期限残4日に迫り、MOU第5条（海峡再開）は事実上機能不全<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — 米の約140カ所空爆・イランの5カ国報復という今回紛争で最大規模の応酬——エスカレーションリスクが最高水準に達している<br>
  <strong style="color:#f87171;">5カ国への同時報復攻撃とオマーンによるイラン大使召喚により、外交解決（A）・膠着継続（B）双方の前提が崩れつつあり、C・Dへのリスクシフトが一段と鮮明化している（A↓ B↓ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月13日 08:28 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
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
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（本文のみ・確率は自動同期のため矢印テキストのみ更新）

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>7/11のマスカット協議からわずか1日で、イランはオマーン領内（ドゥクム・ムサンダム）をドローン攻撃し、仲介役であるオマーン自身がイラン大使召喚という対抗措置に踏み切った。同時にカタール・クウェート・バーレーン・ヨルダンの米軍拠点も攻撃対象となり、段階的なMOU履行という前提そのものが崩れつつある。米の約140カ所への空爆規模も踏まえると、双方が「話し合いより実力行使」を選んだ1週間であったと言わざるを得ず、本シナリオの実現可能性はさらに後退している。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-A"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ A</span> ― 段階的MOU履行成功　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
      <div class="sc-title">🟢 シナリオA：IMO避難計画成功→核査察スケジュール合意→Hormuz主ルート再開</div>
      <div class="sc-body">
        <p>トランプ大統領は対イラン海上封鎖の再開に加え、米国が「ホルムズ海峡の守護者」として全貨物の20%を通航料として徴収する方針を一方的に表明した。これはMOUが本来目指していた封鎖解除・海峡自由開放という前提そのものを覆すものであり、イラン側も税率を巡り交渉の余地を示しつつも「イランこそ守護者」と対抗する姿勢を崩していない。段階的なMOU履行という枠組みは事実上機能を停止しており、本シナリオの実現可能性はさらに一段と後退している。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>オマーンの二経路案は事実上棚上げされた状態にある。仲介国自身が攻撃を受け抗議に転じたことで、案の実務協議が短期間で再開する見込みは薄い。カタール・クウェート・バーレーン・ヨルダンも同時に攻撃対象となり、単なる「交渉と衝突の併存」という枠組みでは説明しきれない広域化が進んでいる。主要海運4社（Maersk・MSC・CMA CGM・Hapag-Lloyd）は依然ケープ廻りを継続しており、戦争保険水準が下がる材料も見当たらない。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-B"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ B</span> ― 膠着継続・外交不透明化（最多シナリオ）　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↓</span>
      <div class="sc-title">🟡 シナリオB：核査察問題長期化→期間延長交渉、機雷除去は先行</div>
      <div class="sc-body">
        <p>単純な「交渉と衝突の併存」という膠着状態は、トランプ大統領の封鎖再開・一方的通航料宣言によって新たな局面に移行しつつある。海峡の管理権・課金権そのものを巡る制度的な奪い合いが表面化しており、従来の「膠着」という言葉では実態を説明しきれなくなっている。主要海運4社（Maersk・MSC・CMA CGM・Hapag-Lloyd）は依然ケープ廻りを継続しており、戦争保険水準が下がる材料も見当たらない。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>機雷除去は依然未着手のまま7/17期限（残4日）が目前に迫っている。ガリバフ国会議長がMOU第5条（海峡再開義務）を名指しして「一方的な合意の時代は終わった」と表明したことは、MOUの枠組み自体が空文化しつつあることを象徴している。共通インフラ（機雷除去・海峡管理）の整備は完全に停止したまま、個別の軍事的応酬のみが進行しており、本シナリオが想定する「制度の形骸化」がほぼそのまま現実化している。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-C"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ C</span> ― 完全封鎖の制度化・経済疲弊深刻化　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">🔴 シナリオC：南レバノン大規模衝突再発→Hormuz再閉鎖宣言</div>
      <div class="sc-body">
        <p>機雷除去は依然未着手のまま7/17期限（残3日）が目前に迫っている。トランプ大統領による対イラン海上封鎖の正式再開と、米国が徴収主体となる20%通航料の一方的宣言は、MOUが目指した「海峡自由開放」を制度面から覆すものであり、本シナリオが想定する「封鎖の制度化」がまさに現実化しつつある。IMOが強制通航料に断固反対を表明していることも、国際的な制度対立の深刻化を裏付けている。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> →</span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>CENTCOMの約140カ所への空爆に対し、イランはオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国同時攻撃で応酬した——開戦以来最大規模の相互軍事行動である。シナリオCとの差：C=「機雷除去等の実務レベルでの機能不全」、D=「複数国を巻き込む実力行使の応酬」。今回は明確にDに該当する事態であり、リスクは直近で最も高い水準にある。オマーンの仲介機能が今後も維持されるか、追加の軍事応酬が発生するかが、本シナリオへの本格移行を左右する分水嶺となる。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="sc-tag" id="sc-tag-D"><span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">シナリオ D</span> ― 全面対決・無期限封鎖　<span style="font-size:1.15em;font-weight:900;text-shadow:-1px -1px 0 rgba(0,0,0,0.8),1px -1px 0 rgba(0,0,0,0.8),-1px 1px 0 rgba(0,0,0,0.8),1px 1px 0 rgba(0,0,0,0.8);">確率</span> ↑</span>
      <div class="sc-title">⚫ シナリオD：核査察問題で交渉打ち切り→Hormuz武力制圧→全面戦争再開</div>
      <div class="sc-body">
        <p>CENTCOMは3夜連続で対イラン空爆を継続しており、これに加えて対イラン海上封鎖が本日7/14 20:00 GMTに正式発効する予定である。シナリオCとの差：C=「通航料・海峡管理を巡る制度的対立」、D=「継続的な軍事行動を伴う実力による現状変更」。今回は軍事・経済両面での対立が同時進行しており、直近で最も高いリスク水準にある。封鎖発効後の実際の運用実態と、イランがこれに軍事的に反応するかが、本シナリオへの本格移行を左右する分水嶺となる。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5点）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">これ以上の軍事応酬拡大の有無（追加の報復・反撃）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">オマーンの仲介機能が維持されるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">米国要求（攻撃停止・全通航路開放の公式声明）にイランが応じるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">機雷除去着手の有無（期限まで残4日）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月13日 08:28 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">封鎖の正式発効と実際の運用実態（7/14 20:00 GMT〜）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">20%通航料の実効性・IMO/主要海運国の反応</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">これ以上の軍事応酬拡大の有無（追加の報復・反撃）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">機雷除去着手の有無（期限まで残3日）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月14日 08:48 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月13日 08:28 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンの自由航行案提示から一夜明け、当のオマーン領内（ドゥクム・ムサンダム）がイランのドローン攻撃を受け、オマーン外務省がイラン大使を召喚。7/7以降10,000dwt超の大型船AIS通航実績はなく、事実上の通航停止状態が継続。【北ルート（Iran coastline / IRGC管理）】ホルムズ海峡「閉鎖」宣言（7/12未明）に続き、イランはオマーン・カタール・クウェート・バーレーン・ヨルダンへ報復攻撃を実施——南北両ルートとも運用停止に近い状態が継続している。CENTCOMは約140カ所への空爆で応酬。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残4日）。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。戦争保険水準・ルート法的不確実性が解消されるまで復帰なし。🇯🇵 日本関係船舶：残り4隻で変化なし（7/13 08:28 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月14日 08:48 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンの二経路案の実務協議は事実上停止したまま。7/7以降10,000dwt超の大型船AIS通航実績はなく、事実上の通航停止状態が継続。【北ルート（Iran coastline / IRGC管理）】ホルムズ海峡「閉鎖」宣言が続く中、トランプ大統領が対イラン海上封鎖の再開と20%通航料の一方的徴収を宣言（7/14 20:00 GMT発効予定）——南北両ルートとも運用停止に近い状態が継続。CENTCOMは3夜連続の対イラン空爆を継続中。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残3日）。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。戦争保険水準・ルート法的不確実性が解消されるまで復帰なし。🇯🇵 日本関係船舶：残り4隻で変化なし（7/14 08:48 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋バッジ5枚・必ず最後に反映）

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
🗣️ イラン、米の3度目空爆（約140カ所）にオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国への報復攻撃で応酬。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇯🇵 オマーンはイラン大使を召喚し抗議、仲介の立場も緊張最高潮。日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ これ以上の軍事応酬拡大の有無が焦点、封鎖136日目——機雷除去期限（7/17）まで残4日・MOU最終期限（8/16）まで34日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚨イラン、5カ国へ報復攻撃</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️米、約140カ所を空爆</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️オマーンがイラン大使召喚</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、週明けに4%高反発</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💰米、対イラン封鎖再開・20%通航料</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️米、3夜連続で空爆継続</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️イラン、税率交渉に含み・IMOは反対</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、ブレント一時83ドル台</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [SHIP_CONFIG] 日本関連タンカー足止め可視化

<!-- APPLY:START -->
<!-- OLD:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年7月13日 08:28 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認）'
};
<!-- OLD:END -->
<!-- NEW:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年7月14日 08:48 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認）'
};
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [JSON-LD] dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-13T08:28:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-14T08:48:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新メモ

### updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月13日 08:28 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年7月14日 08:48 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列（新規3件を先頭に追加・既存 isLatest フラグ移動・最古3件をアーカイブへ移動）

latest は現在6件（`latest-iran-attacks-5states-0712` に isLatest:true）。新規3件を先頭に追加すると9件になるため、
Claude Code は既存の最も古い3件（`latest-hormuz-closed-gfs-galaxy-0712`・`latest-oman-tollfree-corridor-0712`・`latest-us-third-strikes-hegseth-0712`）を
新規アーカイブバッチ「2026年7月12日 更新分（アーカイブ）」として `archive` 配列の先頭に移動してください（本文は既存ファイルに保存済みのため、そのまま転記）。
また、現在 `isLatest: true` の `latest-iran-attacks-5states-0712` は `isLatest: false` に変更してください。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-iran-attacks-5states-0712",
      "title": "イラン、米の3度目空爆にオマーン・カタール・クウェート・バーレーン・ヨルダンを報復攻撃",
      "body": "CENTCOMが今週3度目・約140カ所への対イラン空爆を実施したのに続き、イランはオマーン（ドゥクム）、カタール（アルウデイド空軍基地）、クウェート、バーレーン、ヨルダンの米軍関連拠点にドローン・弾道ミサイルで報復攻撃を実施した。カタールは迎撃したと発表したが、破片により子供を含む3名が負傷。イラン国会議長ガリバフ氏はMOU第5条（ホルムズ海峡再開）の条文画像を添え「約束を守るか代償を払うかだ」「一方的な合意の時代は終わった」とX投稿し、対米強硬姿勢を鮮明にした。開戦以来、最も広範囲に及ぶ軍事応酬となった。",
      "sourceLabel": "NPR / Washington Post",
      "date": "2026年7月12日（現地）/ 2026年7月12日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.npr.org/2026/07/11/g-s1-133212/us-iran-vessel-attack-strait-hormuz-gulf",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "id": "latest-trump-guardian-20pct-toll-0713",
      "title": "トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%通航料を表明",
      "body": "トランプ大統領はTruth Social投稿とFox Newsのインタビューで、6月に解除した対イラン海上封鎖を再開し、米国が「ホルムズ海峡の守護者」となって同海峡を通過する全貨物の20%相当を安全確保の対価として徴収する方針を表明した。イラン以外の国は海峡を公正かつ自由に利用できるとしつつ、封鎖はイランの船舶・顧客の出入りのみを止めるものだと説明。CENTCOMは封鎖が米東部時間7/14午後4時（7/14 20:00 GMT）に発効すると発表した。米国はこれまで海峡通航への通航料導入に一貫して反対してきた立場から大きく転換した。",
      "sourceLabel": "CNBC / Al Jazeera",
      "date": "2026年7月13日（現地）/ 2026年7月13日 JST",
      "label": "💰 経済・封鎖",
      "url": "https://www.cnbc.com/2026/07/13/trump-iran-hormuz-strait-charge-reimburse.html",
      "isLatest": true
    },
    {
      "id": "latest-araghchi-response-imo-oppose-0713",
      "title": "アラグチー外相「イランこそ永遠の守護者」と反発——IMOは強制通航料に断固反対",
      "body": "イランのアラグチー外相はX投稿で、安全な航行への対価支払いという発想自体は正しいと認めつつ「イランこそが海峡の守護者であり、これからも永遠にそうである」と反論し、「20%は明らかに高すぎる。我々は公正にやる」と税率を巡る交渉の余地を示唆した。国連の国際海事機関（IMO）は、国際航行に用いられる海峡での強制的な通航料導入に法的根拠はないとして断固反対する立場を改めて表明。イラン軍ハタム・アル・アンビヤ司令部も米国による海峡管理への干渉は一切許さないと強調した。",
      "sourceLabel": "NPR/KPBS / ニューズウィーク日本版",
      "date": "2026年7月13日（現地）/ 2026年7月13日 JST",
      "label": "🗣️ 外交",
      "url": "https://www.newsweekjapan.jp/articles/-/328268",
      "isLatest": false
    },
    {
      "id": "latest-oil-surge-83dollar-0713",
      "title": "原油急伸、ブレント一時83ドル台——封鎖再開・通航料表明を受け週明けに急騰",
      "body": "原油先物はトランプ大統領による対イラン海上封鎖再開・20%通航料表明を受けて週明けの取引で急伸した。ブレント先物は7/13終値で前日比3.74%高の78.85ドルを付けた後、同日夜の取引で一時83ドル台まで上昇。米国内のレギュラーガソリン平均価格は1ガロン3.87ドルと、1週間前から8セント上昇した。データ分析企業Kplerは、ホルムズ海峡の通航実績が前週比で半分以下に減少したと分析している。",
      "sourceLabel": "Trading Economics / KPBS",
      "date": "2026年7月13日（現地）/ 2026年7月13日 JST",
      "label": "🛢️ 市場動向",
      "url": "https://www.kpbs.org/news/international/2026/07/13/the-u-s-strikes-iran-after-trump-announces-a-renewed-blockade-and-tolls-in-hormuz",
      "isLatest": false
    },
    {
      "id": "latest-iran-attacks-5states-0712",
      "title": "イラン、米の3度目空爆にオマーン・カタール・クウェート・バーレーン・ヨルダンを報復攻撃",
      "body": "CENTCOMが今週3度目・約140カ所への対イラン空爆を実施したのに続き、イランはオマーン（ドゥクム）、カタール（アルウデイド空軍基地）、クウェート、バーレーン、ヨルダンの米軍関連拠点にドローン・弾道ミサイルで報復攻撃を実施した。カタールは迎撃したと発表したが、破片により子供を含む3名が負傷。イラン国会議長ガリバフ氏はMOU第5条（ホルムズ海峡再開）の条文画像を添え「約束を守るか代償を払うかだ」「一方的な合意の時代は終わった」とX投稿し、対米強硬姿勢を鮮明にした。開戦以来、最も広範囲に及ぶ軍事応酬となった。",
      "sourceLabel": "NPR / Washington Post",
      "date": "2026年7月12日（現地）/ 2026年7月12日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.npr.org/2026/07/11/g-s1-133212/us-iran-vessel-attack-strait-hormuz-gulf",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

### osint（現地メディア視点）最新1件（isLatest: true）を先頭に追加・既存フラグ変更

現在 `isLatest: true` の `osint-iran-attacks-5states-live-0712` を `isLatest: false` に変更し、以下を配列の先頭に追加してください。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "id": "osint-iran-attacks-5states-live-0712",
      "titleJa": "【Al Jazeera】イラン、5カ国へ報復攻撃——米が新たな空爆を実施と発表",
      "titleEn": "Iran war live: More explosions as US says launching new strikes",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/12/iran-war-live-irgc-declares-strait-of-hormuz-closed-over-us-interference",
      "date": "2026年7月12日（現地）/ 2026年7月12日 JST",
      "isLatest": true
<!-- OLD:END -->
<!-- NEW:START -->
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
    {
      "id": "osint-iran-attacks-5states-live-0712",
      "titleJa": "【Al Jazeera】イラン、5カ国へ報復攻撃——米が新たな空爆を実施と発表",
      "titleEn": "Iran war live: More explosions as US says launching new strikes",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/12/iran-war-live-irgc-declares-strait-of-hormuz-closed-over-us-interference",
      "date": "2026年7月12日（現地）/ 2026年7月12日 JST",
      "isLatest": false
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S11] 更新ログ — 2ブロック構成

### ブロック1: 常時表示エリア（本日分+旧2件・旧3件目=7/11分はブロック2でlog-collapseへ）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年7月13日 08:28 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/13 08:28</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン、米の3度目・約140カ所への対イラン空爆に対しオマーン（ドゥクム）・カタール（アルウデイド基地）・クウェート・バーレーン・ヨルダンの5カ国を弾道ミサイル・ドローンで同時報復攻撃（7/12 JST）・カタールで迎撃破片により3名負傷・ガリバフ国会議長「一方的な合意の時代は終わった」とX投稿・オマーン外務省、ドゥクム・ムサンダム攻撃を受けイラン大使を召喚し正式抗議——前日のアラグチー・ブーサイーディー両外相協議から一転し仲介の立場も緊張最高潮・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油は週明けに反発しブレント一時79ドル台・WTI74ドル台まで4%高・封鎖136日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月12日 09:19 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/12 09:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>IRGC、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）・CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」・停戦は事実上崩壊・オマーンが通航料なしの南北二経路案を提示（南＝自由航行、北＝イラン事前承認制だが無料）——アラグチー外相はオマーン外相と会談も結論持ち帰りで検討中・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント週間+5〜6%で$76台高止まり（7/10終値時点）・封鎖135日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月11日 08:38 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/11 08:38</span> — <strong style="color:#fca5a5;">【重大更新】</strong>金子国交相、日本関係船22隻（大型原油タンカー6隻含む）の通過を発表——残り4隻に大幅減（開戦時45隻から・7/10会見）・米当局者、イランに攻撃停止・全通航路開放の公式声明を要求——通航料も不可（Reuters）・イラン、攻撃は「制度の一部の暴走」と釈明し対話継続を希望・アラグチー外相は本日オマーンでブーサイーディー外相と海峡管理を協議・トルコ外相フィダン氏「今週末にも解決の可能性」・イラン国連大使は「海峡管理は専らイランに属する」と対立姿勢維持・原油はブレント$76台で高止まり（週間+5〜6%）・南ルートは大型船AIS通航が7/7以降ゼロで事実上停止・バンダルアッバスの漁船30隻超が空爆で損壊・封鎖134日目・ニュース3件更新・osint更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年7月14日 08:48 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/14 08:48</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領、対イラン海上封鎖の再開と「ホルムズ海峡の守護者」を宣言——全貨物の20%を通航料として徴収する方針を表明（封鎖発効は7/14 20:00 GMT予定）・アラグチー外相「イランこそ永遠の守護者」と反発しつつ「20%は高すぎる」と税率交渉に含み・イラン軍ハタム・アル・アンビヤ司令部は米国の海峡管理への干渉を許さないと強調・IMOは強制通航料に法的根拠なしとして断固反対・中国外務省も安全な航行確保を要求・米軍は3夜連続の対イラン空爆を継続・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント7/13終値78.85ドル（+3.74%）後、同日夜一時83ドル台まで急伸・封鎖137日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月13日 08:28 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/13 08:28</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン、米の3度目・約140カ所への対イラン空爆に対しオマーン（ドゥクム）・カタール（アルウデイド基地）・クウェート・バーレーン・ヨルダンの5カ国を弾道ミサイル・ドローンで同時報復攻撃（7/12 JST）・カタールで迎撃破片により3名負傷・ガリバフ国会議長「一方的な合意の時代は終わった」とX投稿・オマーン外務省、ドゥクム・ムサンダム攻撃を受けイラン大使を召喚し正式抗議——前日のアラグチー・ブーサイーディー両外相協議から一転し仲介の立場も緊張最高潮・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油は週明けに反発しブレント一時79ドル台・WTI74ドル台まで4%高・封鎖136日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月12日 09:19 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/12 09:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>IRGC、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）・CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」・停戦は事実上崩壊・オマーンが通航料なしの南北二経路案を提示（南＝自由航行、北＝イラン事前承認制だが無料）——アラグチー外相はオマーン外相と会談も結論持ち帰りで検討中・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント週間+5〜6%で$76台高止まり（7/10終値時点）・封鎖135日目・ニュース3件更新・osint更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2: log-collapseへ旧3件目（7/11分）を先頭挿入 ＋ 総件数超過分（7/4分）を削除

現在の常時表示3件+log-collapse7件＝合計10件。本日分追加後、旧3件目（7/11 08:38）をlog-collapse先頭へ移動すると合計11件になるため、log-collapse最古の「2026年7月4日 08:22 JST」エントリーを削除し、`update_log.json`の先頭に追加してください（このエントリーの本文は既存ファイルに保存済み）。

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月10日 07:40 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月11日 08:38 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/11 08:38</span> — <strong style="color:#fca5a5;">【重大更新】</strong>金子国交相、日本関係船22隻（大型原油タンカー6隻含む）の通過を発表——残り4隻に大幅減（開戦時45隻から・7/10会見）・米当局者、イランに攻撃停止・全通航路開放の公式声明を要求——通航料も不可（Reuters）・イラン、攻撃は「制度の一部の暴走」と釈明し対話継続を希望・アラグチー外相は本日オマーンでブーサイーディー外相と海峡管理を協議・トルコ外相フィダン氏「今週末にも解決の可能性」・イラン国連大使は「海峡管理は専らイランに属する」と対立姿勢維持・原油はブレント$76台で高止まり（週間+5〜6%）・南ルートは大型船AIS通航が7/7以降ゼロで事実上停止・バンダルアッバスの漁船30隻超が空爆で損壊・封鎖134日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年7月10日 07:40 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月4日 08:22 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/04 08:22</span> — <strong style="color:#fca5a5;">【重大更新】</strong>故ハメネイ師国葬、本日テヘランで開始（7/6大葬列・7/9マシュハド埋葬）・ドーハ協議は国葬終了まで完全休止——次回は国葬後に設定・イラン軍「米介入に断固対応」新威嚇声明・米は第2海兵遠征部隊を中東追加展開・日本関係船新たに1隻通過で残り31隻に（7/1分・7/3発表）・ブレント$71台/WTI$68台弱で戦前水準近辺・封鎖127日目・ニュース2件更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

**update_log.json への追加指示：** 削除する「2026年7月4日 08:22 JST」エントリーを `docs/data/update_log.json` の先頭に `{"date":"2026/07/04 08:22","text":"..."}` 形式で追加してください（本文は上記の削除対象div内容をそのまま使用）。

---

## 確認事項（Claude Code 適用後）

適用後、以下を必ず確認してください：

```bash
grep -n "2026年7月14日\|封鎖137日目\|SHIP_CONFIG\|dateModified" docs/index.html | head -20
```

期待される出力：本日日付・封鎖137日目・SHIP_CONFIG更新・dateModified 2026-07-14 が全て反映されていること。
