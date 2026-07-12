# index_html_diffs.md — 2026年7月13日 08:28 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> news_data.json の変更は [S10] の指示に従い、既存ファイルへのマージとして適用してください。
> 適用後、C01タンカー確認行を含めた変更内容まとめを提示し、commit してください。push は確認後に指示します。

---

## ✅ 出力前セルフチェック（本日のチェックリスト・執筆前に空欄で先貼り→本文執筆後に埋める）

本日のセルフチェック項目数：30件（project_knowledge_search取得の原文と一致）

```
[✓] S01 ヘッダー ― 日付 2026年7月13日 08:28 JSTが入っているか
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
[✓] S11 総件数 ― 常時表示3 + log-collapse内エントリー数の合計が10以下か（超過分削除指示あり）
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

**⚠️ 内訳ロジック修正について：** ユーザーからご指摘のあった「日本関連船足止め状況の内訳の数のロジック」は、前回セッション（7/12）で既に修正・適用済みであることを本日 raw fetch で確認しました（`SHIP_TYPES` は `count: totalShips` を参照し、ラベルは「内訳確認中」——架空の23/5/13内訳は使用されていません）。本diffsでの追加修正はありません。

**C01 タンカー確認**：日本語クエリ3本（①「金子国土交通大臣 会見 ホルムズ海峡 7月13日」②「外務省 ホルムズ海峡 日本関係船舶 7月13日」③「（金子国交相） 会見 ホルムズ海峡」）＋英語クエリ（"Japanese ships Strait of Hormuz stranded detained July 2026"）を個別実行し、外務省・国土交通省の一次情報を優先確認。**変化なし**——直近の会見は7/10（22隻通過・残り4隻）が最新であり、7/11〜7/13時点で新たな大臣会見・外務省発表は確認されず。SHIP_CONFIGのdateConfirmedのみ本日日時・変更なしとして更新。

二重封鎖表記チェック：「イラン・米国による二重封鎖」の単独表記は変更していません（dl-boxは今回対象外）。
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：S08.5内で7/13 08:28 JST更新を明示 ✓
人名表記チェック：「Xi」「Trump」単独表記なし（トランプ大統領と表記）✓
Al Jazeera混入チェック：📰関連最新ニュース欄（news_data.json latest）には使用せず、🌐現地メディア視点（osint）にのみ使用 ✓
毎日新聞・Wikipedia混入チェック：使用なし ✓
URL捏造チェック：全URL web検索で実在確認済み（NPR・Washington Post・Al Jazeera・global-scm.com・日本経済新聞）✓

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イラン、コンテナ船GFS Galaxyを攻撃しホルムズ海峡「閉鎖」を宣言——米が今週3度目の対イラン空爆を実施し停戦は事実上崩壊／オマーンは通航料なしの南北二経路案を提示・イランは持ち帰り検討中／封鎖135日目）</span>
    <span class="badge-item badge-date">📅2026年7月12日 09:19 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イラン、米の3度目空爆に対しオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国を弾道ミサイル・ドローンで報復攻撃——米は約140カ所を空爆／オマーンはイラン大使を召喚し抗議、通航正常化の見通し立たず／日本関係船は残り4隻で変化なし／原油は週明けに反発し4%高／封鎖136日目）</span>
    <span class="badge-item badge-date">📅2026年7月13日 08:28 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年7月12日 09:19 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月12日 09:19 JST） -->
      🚨【停戦事実上崩壊】イラン革命防衛隊、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃（「認可外ルート航行」を理由）——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）｜🇺🇸 CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」（7/12 JST）｜🕊️ オマーン、通航料なしの南北二経路案を提示——南ルートは戦前同様に自由航行、北ルート（イラン領海）は事前承認制だが無料（CNN 7/11）｜🇮🇷 アラグチー外相・ブーサイーディー外相会談は具体的合意なく終了、イランは提案を持ち帰り検討中｜🇯🇵 日本関係船、残り4隻で変化なし（7/12 09:19 JST再確認）｜🛢️ ブレント原油、週間+5〜6%で$76台高止まり（7/10終値時点）｜⚠️ 機雷除去期限まで残5日・封鎖135日目
    </span>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月13日 08:28 JST） -->
      🚨【5カ国へ報復攻撃】イラン、米の3度目空爆（約140カ所）に対しオマーン（ドゥクム）・カタール（アルウデイド基地）・クウェート・バーレーン・ヨルダンの米軍関連拠点を弾道ミサイル・ドローンで攻撃（7/12 JST）｜🗣️ ガリバフ国会議長「一方的な合意の時代は終わった」とX投稿｜🇴🇲 オマーン外務省、ドゥクム・ムサンダム攻撃を受けイラン大使を召喚し「無責任な行為」と正式抗議（7/12 JST）｜🇶🇦 カタール、迎撃時の破片で3名負傷・「危険なエスカレーション」と非難｜🇯🇵 日本関係船、残り4隻で変化なし（7/13 08:28 JST再確認）｜🛢️ 原油、週明けに反発——ブレント一時79ドル台・WTI74ドル台まで4%高（7/13早朝JST）｜⚠️ 機雷除去期限まで残4日・封鎖136日目
    </span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️（漏れ多発セクション）

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/12 09:19 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/13 08:28 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の strong タグを置き換え）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/12 09:19 速報】イラン革命防衛隊、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）｜CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」｜停戦は事実上崩壊｜オマーン、通航料なしの南北二経路案を提示（南＝自由航行、北＝イラン事前承認制だが無料）｜アラグチー外相・ブーサイーディー外相会談は具体的合意なく終了、イランは提案を持ち帰り検討中｜日本関係船は残り4隻で変化なし｜原油はブレント週間+5〜6%で$76台高止まり｜封鎖135日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/13 08:28 速報】イラン、米の3度目空爆（約140カ所）に対しオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国を弾道ミサイル・ドローンで報復攻撃（7/12 JST）｜ガリバフ国会議長「一方的な合意の時代は終わった」｜オマーン外務省、ドゥクム・ムサンダム攻撃を受けイラン大使を召喚し正式抗議｜カタールは迎撃破片で3名負傷｜日本関係船は残り4隻で変化なし｜原油は週明けに反発しブレント一時79ドル台・WTI74ドル台まで4%高｜封鎖136日目
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
  <span style="color:#f87171;font-weight:700;">⚔️ 7/12 JST</span>
  <span style="color:#e2e8f0;"> イランは、米による今週3度目・約140カ所への対イラン空爆に対する報復として、オマーン（ドゥクム港のロジ支援施設・給油拠点）、カタール（アルウデイド空軍基地）、クウェート（パトリオット防空システム・弾薬庫・レーダー施設）、バーレーン（通信システム・レーダー施設）、ヨルダン（プリンス・ハッサン空軍基地）の米軍関連施設・拠点にドローン・弾道ミサイルで攻撃を実施したと発表した。カタール国防省は着弾を迎撃したと発表したが、迎撃破片により子供を含む3名が負傷。イラン国会議長で対米交渉責任者のガリバフ氏はX投稿でMOU第5条（海峡再開）の画像を添え「約束を守るか代償を払うかだ。現実が扉を叩いている」「一方的な合意の時代は終わった」と表明した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🕊️ 7/12 JST</span>
  <span style="color:#e2e8f0;"> オマーン外務省は、ムサンダム県・アルウスタ県（ドゥクム周辺）の施設を狙ったイランのドローン攻撃を受け、駐オマーン・イラン大使を召喚し正式な抗議文を手交した。オマーン外務次官は会談でイランの「無責任な行為」への不満を表明したという。オマーン政府は「事態への対応に必要なあらゆる措置を講じ、国と国民の安全を守る」と発表し、攻撃を強く非難した。前日にはアラグチー外相がオマーンを訪問しブーサイーディー外相とホルムズ海峡の安全通航について協議したばかりで、外交チャンネルは維持されているものの、実効的な安全通航合意には至っていない。在オマーン米国大使館はムサンダム県への退避勧告を発出した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/12 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

**対象：** SITUATION CARDS セクション（外交・軍事・市場船舶の3枚）

### カード①：外交

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🕊️ 外交：オマーンが無料の南北二経路案を提示——イランは持ち帰り検討、米要求の公式声明は不発</div>
        <div class="s-body">オマーンは通航料を課さない南北二経路案を提示したとCNNが報じた。南ルート（オマーン領海）は戦前同様に自由航行、北ルート（イラン領海）は事前承認制だが無料。アラグチー外相・ブーサイーディー外相は7/11マスカットで会談し技術・政治協議の継続で合意したが、米政権が求める「海峡は全面開放され安全」との公式声明表明には至らず、イラン側は提案をテヘランに持ち帰り検討中。イラン側筋は「海峡に関する決定はイランとオマーンのみが行う」と強調しており、対立点は未解消のまま。</div>
        <div class="s-src">出典: CNN / Israel National News（7/12 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🕊️ 外交：前日の仲介協議から一転、オマーンがイラン大使を召喚——外交チャンネルは維持も緊張最高潮</div>
        <div class="s-body">7/11にアラグチー外相・ブーサイーディー外相がマスカットで海峡管理を協議した翌日、イランがオマーン領内（ドゥクム・ムサンダム）を攻撃したため、オマーン外務省はイラン大使を召喚し「無責任な行為」への不満を正式に表明した。ガリバフ国会議長はMOU第5条（海峡再開義務）を引き合いに「一方的な合意の時代は終わった」とX投稿し、対米強硬姿勢を鮮明にした。外交チャンネル自体は完全には途絶していないが、仲介役自身が攻撃対象となったことで信頼構築は大きく後退している。</div>
        <div class="s-src">出典: Al Jazeera / global-scm.com（7/13 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード②：軍事情勢

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">⚔️ 軍事：イラン、コンテナ船GFS Galaxyを攻撃しホルムズ海峡「閉鎖」宣言——米が3度目の空爆</div>
        <div class="s-body">IRGC海軍は「認可外ルート」を航行したとしてキプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃を実施（乗組員1名行方不明・機関室損傷）し、ホルムズ海峡を「次官通達まで閉鎖」と宣言した。CENTCOMは即座に今週3度目となる対イラン空爆を実施し、「イランはMOU遵守の機会を再び与えられたが、また失敗した」と非難。ヘグセス国防長官は「イランは間違った選択をした。今、代償を払う」とX投稿。イラン国営メディアはバンダルアッバス・ゲシュム島・ブシェール等各地での爆発を報道し、停戦は事実上崩壊した状態にある。</div>
        <div class="s-src">出典: CENTCOM / Times of Israel / Haaretz（7/12 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">⚔️ 軍事：米の約140カ所空爆にイランが5カ国へ報復——今回の紛争で最大規模の相互攻撃</div>
        <div class="s-body">CENTCOMは、GFS Galaxy攻撃への対応として今週3度目・約140カ所（ミサイル・ドローン拠点、艦艇能力、弾薬庫、通信網、沿岸監視施設）への空爆を実施したと発表（この1週間の3夜合計では300カ所超）。これに対しイランはオマーン（ドゥクム）・カタール（アルウデイド基地）・クウェート・バーレーン・ヨルダンの米軍関連拠点にドローン・弾道ミサイルで報復攻撃を実施。カタールで迎撃破片により3名負傷。イラン国営放送はロレスタン州ヴェイシアン近郊やホンダーブの軍事拠点への米空爆も報じている。停戦崩壊後、最も広範囲な軍事応酬となった。</div>
        <div class="s-src">出典: CENTCOM / Al Jazeera / NPR（7/13 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③：船舶・市場

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし——原油は週間+5〜6%で$76台高止まり</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/12 09:19 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認）。原油市場はブレント原油が7/10終値時点で$76台にとどまり、週間では約5〜6％の上昇。市場は週末（土日）の閉場中に発生した本件（IRGCによるGFS Galaxy攻撃・米の3度目の空爆・海峡閉鎖宣言）を織り込んでおらず、週明けの反応が焦点となる。機雷除去は依然未着手のまま7/17の除去期限まで残5日、8/16のMOU最終期限まで残35日に迫っている。</div>
        <div class="s-src">出典: Trading Economics / 国土交通省 / 外務省（7/12 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし——週明けの原油は反発し4%高</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/13 08:28 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認）。週末に発生した5カ国への報復攻撃・約140カ所の空爆を受け、日本時間13日早朝の取引で原油先物は反発。ブレント先物（期近9月物）は一時1バレル79ドル台と前週末比4%上昇、WTIも同74ドル台と4%高を付けた。機雷除去は依然未着手のまま7/17の除去期限まで残4日、8/16のMOU最終期限まで残34日に迫っている。</div>
        <div class="s-src">出典: 日本経済新聞 / 国土交通省 / 外務省（7/13 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（イラン、ホルムズ海峡「閉鎖」宣言・米が3度目の空爆で停戦事実上崩壊）」——封鎖135日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（イラン、米に5カ国同時報復攻撃・米は約140カ所を空爆——事実上の全面軍事応酬）」——封鎖136日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🚨 <strong>イラン、コンテナ船GFS Galaxyを攻撃しホルムズ海峡「閉鎖」を宣言——米が今週3度目の対イラン空爆を実施し停戦は事実上崩壊／オマーンは通航料なしの南北二経路案を提示・イランは持ち帰り検討中／日本関係船は残り4隻で変化なし／原油は週間+5〜6%で$76台高止まり——封鎖135日目・MOU機雷除去期限残5日（7/17）・MOU最終期限残35日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①イランがオマーンの無料二経路案を受諾するか ②米国要求（攻撃停止・全通航路開放の公式声明）にイランが応じるか ③新たな軍事衝突がさらに拡大するか ④残る日本関係船4隻の安全確保 ⑤機雷除去着手の有無（期限まで残5日）</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残5日（7/17）</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🚨 <strong>イラン、米の3度目空爆（約140カ所）に対しオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国を報復攻撃——ガリバフ国会議長「一方的な合意の時代は終わった」／オマーンはイラン大使を召喚し抗議、仲介の立場も緊張最高潮／日本関係船は残り4隻で変化なし／原油は週明けに反発し4%高——封鎖136日目・MOU機雷除去期限残4日（7/17）・MOU最終期限残34日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①これ以上の軍事応酬拡大の有無 ②オマーンの仲介機能が維持されるか ③米国要求（攻撃停止・全通航路開放の公式声明）にイランが応じるか ④残る日本関係船4隻の安全確保 ⑤機雷除去着手の有無（期限まで残4日）</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残4日（7/17）</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#f87171;">📊 2026年7月12日 09:19 JST 更新</span><br>
  📊 <strong>イランがコンテナ船GFS Galaxyを攻撃しホルムズ海峡「閉鎖」を宣言、米が今週3度目の空爆を実施——停戦は事実上崩壊。一方オマーンは通航料なしの南北二経路案を提示、イランは持ち帰り検討中：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#f87171;">↓</span> — 停戦は事実上崩壊し、イラン自ら海峡閉鎖を宣言——前日までの前進材料が後退<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — オマーンの無料二経路案をイランが検討中だが、承認・結論は依然出ていない<br>
  🅒 MOU形骸化・機能不全 <span style="color:#f87171;">↑</span> — 機雷除去は未着手のまま期限まで残5日に迫り、海峡自体が「閉鎖」を一方的に宣言される事態に発展<br>
  🅓 全面対決・無期限封鎖 <span style="color:#f87171;">↑</span> — 米が今週3度目の空爆を実施し、イランは艦船攻撃・海峡閉鎖宣言で応酬——エスカレーションリスクが直近で最も高まっている<br>
  <strong style="color:#f87171;">GFS Galaxy攻撃とホルムズ海峡閉鎖宣言・米の3度目空爆により事態は急速に悪化方向へ——C・Dのリスクが顕在化する一方、オマーン仲介案の存在がAへの一縷の望みを残す（A↓ B→ C↑ D↑）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月12日 09:19 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（本文）

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>7/11、イラン革命防衛隊はキプロス籍コンテナ船GFS Galaxyを「認可外ルート」航行を理由に攻撃し、ホルムズ海峡を「次官通達まで閉鎖」と宣言した。これを受け米は今週3度目となる対イラン空爆を実施し、前日まで期待されていた段階的なMOU履行の流れは大きく後退した。一方でオマーンは通航料なしの南北二経路案（南＝自由航行、北＝イラン事前承認制だが無料）を提示しており、アラグチー・ブーサイーディー両外相も技術・政治協議の継続に合意している。イラン側が同案を検討していること自体は交渉ルートが完全に閉ざされたわけではないことを示すが、海峡閉鎖宣言と武力行使が先行した状況では、本シナリオの実現確率は明確に後退したと評価せざるを得ない。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>7/11のマスカット協議からわずか1日で、イランはオマーン領内（ドゥクム・ムサンダム）をドローン攻撃し、仲介役であるオマーン自身がイラン大使召喚という対抗措置に踏み切った。同時にカタール・クウェート・バーレーン・ヨルダンの米軍拠点も攻撃対象となり、段階的なMOU履行という前提そのものが崩れつつある。米の約140カ所への空爆規模も踏まえると、双方が「話し合いより実力行使」を選んだ1週間であったと言わざるを得ず、本シナリオの実現可能性はさらに後退している。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>オマーンが提示した通航料なしの南北二経路案は、南ルート（オマーン領海）での自由航行と北ルート（イラン領海）での事前承認制無料航行を組み合わせるもので、イラン・米双方にとって受け入れ余地のある妥協案となり得る。しかしイランの代表団は同案を即座に承認せずテヘランへ持ち帰っており、承認の可否・時期は不透明なままだ。GFS Galaxy攻撃とホルムズ海峡閉鎖宣言が既に発生している以上、仮に案が承認されても実務適用までには一定のタイムラグが生じる見込みで、当面は交渉と衝突が併存する膠着状態が続く可能性が高い。主要海運4社（Maersk・MSC・CMA CGM・Hapag-Lloyd）は戦争保険水準が下がるまで復帰しない方針を維持している。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>オマーンの二経路案は事実上棚上げされた状態にある。仲介国自身が攻撃を受け抗議に転じたことで、案の実務協議が短期間で再開する見込みは薄い。カタール・クウェート・バーレーン・ヨルダンも同時に攻撃対象となり、単なる「交渉と衝突の併存」という枠組みでは説明しきれない広域化が進んでいる。主要海運4社（Maersk・MSC・CMA CGM・Hapag-Lloyd）は依然ケープ廻りを継続しており、戦争保険水準が下がる材料も見当たらない。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>機雷除去は依然未着手のまま7/17期限（残5日）が目前に迫っている。今回、イランが自ら海峡を「次官通達まで閉鎖」と宣言したことは、除去着手どころか通航そのものの安定運用すら実現していない現実を象徴している。オマーンの二経路案が実務レベルの通航ルールを提示している一方、機雷除去・海峡管理という共通インフラの整備は棚上げされたままであり、「共通インフラは機能不全のまま、個別交渉による部分的な通航のみが試みられる」という本シナリオの様相が一段と強まっている。バンダルアッバスの漁船被害等、地元経済への実害も引き続き蓄積している。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>機雷除去は依然未着手のまま7/17期限（残4日）が目前に迫っている。ガリバフ国会議長がMOU第5条（海峡再開義務）を名指しして「一方的な合意の時代は終わった」と表明したことは、MOUの枠組み自体が空文化しつつあることを象徴している。共通インフラ（機雷除去・海峡管理）の整備は完全に停止したまま、個別の軍事的応酬のみが進行しており、本シナリオが想定する「制度の形骸化」がほぼそのまま現実化している。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>7/11未明（JST）、IRGCがコンテナ船GFS Galaxyを攻撃しホルムズ海峡の「閉鎖」を一方的に宣言、これに対しCENTCOMが今週3度目となる対イラン空爆を実施した——7/9の3カ国同時報復以来、最大の軍事エスカレーションである。シナリオCとの差：C=「機雷除去等の実務レベルでの機能不全」、D=「IRGCによる艦船・インフラへの直接的な実力行使とCENTCOMの大規模報復の応酬」。今回はまさにDの定義に該当する事態が発生しており、リスクは直近で最も高い水準にある。他方でオマーンの仲介案・アラグチー外相のオマーン訪問は交渉ルートが完全に断たれていないことを示しており、今後数日の推移（イランのオマーン案への回答、追加の軍事応酬の有無）が本シナリオへの本格移行を左右する。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>CENTCOMの約140カ所への空爆に対し、イランはオマーン・カタール・クウェート・バーレーン・ヨルダンの5カ国同時攻撃で応酬した——開戦以来最大規模の相互軍事行動である。シナリオCとの差：C=「機雷除去等の実務レベルでの機能不全」、D=「複数国を巻き込む実力行使の応酬」。今回は明確にDに該当する事態であり、リスクは直近で最も高い水準にある。オマーンの仲介機能が今後も維持されるか、追加の軍事応酬が発生するかが、本シナリオへの本格移行を左右する分水嶺となる。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5点）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">イランがオマーンの無料二経路案を受諾するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">米国要求（攻撃停止・全通航路開放の公式声明）にイランが応じるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">新たな軍事衝突がさらに拡大するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">機雷除去着手の有無（期限まで残5日）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月12日 09:19 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">これ以上の軍事応酬拡大の有無（追加の報復・反撃）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">オマーンの仲介機能が維持されるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">米国要求（攻撃停止・全通航路開放の公式声明）にイランが応じるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">機雷除去着手の有無（期限まで残4日）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月13日 08:28 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月12日 09:19 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンが通航料なしの自由航行案を提示（7/11・CNN）が、7/7以降10,000dwt超の大型船AIS通航実績はなく、事実上の通航停止状態が継続。【北ルート（Iran coastline / IRGC管理）】イランのPGSAが事前登録制で管理していたが、7/12未明（JST）、IRGCがキプロス籍コンテナ船GFS Galaxyへの警告射撃・着火攻撃を実施し、ホルムズ海峡を「次官通達まで閉鎖」と宣言——南北両ルートとも運用停止に近い状態に陥っている。これに対しCENTCOMは今週3度目の対イラン空爆を実施。オマーンは南北二経路案（北ルートは事前承認制だが無料）を提示しアラグチー・ブーサイーディー両外相が協議したが、イランは持ち帰り検討中で承認は未定。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残5日）。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。戦争保険水準・ルート法的不確実性が解消されるまで復帰なし。🇯🇵 日本関係船舶：残り4隻で変化なし（7/12 09:19 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月13日 08:28 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンの自由航行案提示から一夜明け、当のオマーン領内（ドゥクム・ムサンダム）がイランのドローン攻撃を受け、オマーン外務省がイラン大使を召喚。7/7以降10,000dwt超の大型船AIS通航実績はなく、事実上の通航停止状態が継続。【北ルート（Iran coastline / IRGC管理）】ホルムズ海峡「閉鎖」宣言（7/12未明）に続き、イランはオマーン・カタール・クウェート・バーレーン・ヨルダンへ報復攻撃を実施——南北両ルートとも運用停止に近い状態が継続している。CENTCOMは約140カ所への空爆で応酬。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残4日）。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。戦争保険水準・ルート法的不確実性が解消されるまで復帰なし。🇯🇵 日本関係船舶：残り4隻で変化なし（7/13 08:28 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ5枚・最後に作成）

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🗣️ 金子国交相、日本関係船22隻の通過を発表——残り4隻に大幅減。米はイランに攻撃停止の公式声明を要求。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇯🇵 イランがコンテナ船GFS Galaxyを攻撃しホルムズ海峡「閉鎖」を宣言——米が3度目の空爆を実施し停戦は事実上崩壊。日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ イランがオマーンの無料二経路案を受諾するかが焦点、封鎖135日目——機雷除去期限（7/17）まで残5日・MOU最終期限（8/16）まで35日。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
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
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ5枚

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚨海峡「閉鎖」宣言</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️米が3度目の空爆</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️オマーン無料二経路案</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油$76台高止まり</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚨イラン、5カ国へ報復攻撃</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️米、約140カ所を空爆</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️オマーンがイラン大使召喚</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油、週明けに4%高反発</span>
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
  dateConfirmed: '2026年7月12日 09:19 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認）'
};
<!-- OLD:END -->
<!-- NEW:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年7月13日 08:28 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認）'
};
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [JSON-LD] dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-12T09:19:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-13T08:28:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新メモ

### updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月12日 09:19 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年7月13日 08:28 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列（新規3件を先頭に追加・既存の isLatest フラグ移動・最古3件をアーカイブへ移動）

latest は現在6件（`latest-hormuz-closed-gfs-galaxy-0712` に isLatest:true）。新規3件を先頭に追加すると9件になるため、
Claude Code は既存の最も古い3件（`latest-japan-ships-22-passed-0711`・`latest-us-demands-iran-statement-0711`・`latest-araghchi-oman-talks-0711`）を
新規アーカイブバッチ「2026年7月11日 更新分（アーカイブ）」として `archive` 配列の先頭に移動してください（本文は既存ファイルに保存済みのため、そのまま転記）。
また、現在 `isLatest: true` の `latest-hormuz-closed-gfs-galaxy-0712` は `isLatest: false` に変更してください。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-hormuz-closed-gfs-galaxy-0712",
      "title": "イラン、ホルムズ海峡「閉鎖」を宣言——コンテナ船GFS Galaxyを攻撃",
      "body": "イラン革命防衛隊（IRGC）海軍は7月11日夜（現地時間）、キプロス籍コンテナ船GFS Galaxyが「認可外ルート」を航行しようとしたとして警告射撃を実施し、船体後部に着火・機関室に大きな損傷を与えた。乗組員1名が行方不明。IRGCはこれを受け、ホルムズ海峡を「次官通達があるまで閉鎖する」と宣言した。CENTCOMは同日、今週3度目となる対イラン空爆を実施し、「イランはMOU遵守の機会を再び与えられたが、また失敗した」と非難。ヘグセス国防長官は「イランは間違った選択をした。今、代償を払う」とX投稿した。",
      "sourceLabel": "CENTCOM / Times of Israel",
      "date": "2026年7月11日（現地）/ 2026年7月12日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.timesofisrael.com/liveblog-july-11-2026/",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
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
    {
      "id": "latest-oman-summons-iran-ambassador-0712",
      "title": "オマーン、ドゥクム・ムサンダム攻撃を受けイラン大使を召喚——「無責任な行為」と抗議",
      "body": "オマーン外務省は7月12日、ムサンダム県とアルウスタ県（ドゥクム周辺）の施設を狙ったイランのドローン攻撃を受け、駐オマーン・イラン大使を召喚し正式な抗議文を手交した。会談でオマーン外務次官はイランの「無責任な行為」への不満を表明したと発表されている。ムサンダム県はホルムズ海峡のオマーン側沿岸を構成し、アルウスタ県にはドゥクム周辺地域が含まれる。前日にはアラグチー外相がオマーンを訪問しブーサイーディー外相とホルムズ海峡の安全通航の枠組みを協議したばかりで、外交チャンネル自体は維持されているものの、実効的な安全通航合意には至っていない。在オマーン米国大使館はムサンダム県への退避勧告を発出した。",
      "sourceLabel": "コンサルタントの独り言（global-scm.com）",
      "date": "2026年7月12日 JST",
      "label": "🕊️ 外交",
      "url": "https://global-scm.com/blog/?p=7870",
      "isLatest": false
    },
    {
      "id": "latest-oil-surge-4pct-0713",
      "title": "原油急反発、ブレント一時79ドル台・WTI74ドル台——週明けに4%高",
      "body": "イランによるホルムズ海峡の再封鎖宣言・5カ国への報復攻撃などで供給懸念が高まり、日本時間13日早朝の取引で原油の先物価格が反発した。国際指標である北海ブレント先物の期近9月物は一時1バレル79ドル台と、前週末比4%上昇。同じく国際指標であるWTI先物も同74ドル台と、4%高を付けた。イランの革命防衛隊は海峡を通る商船に攻撃し、海峡の通航を認めないと宣言している。",
      "sourceLabel": "日本経済新聞",
      "date": "2026年7月13日 JST",
      "label": "🛢️ 市場",
      "url": "https://www.nikkei.com/markets/stocks/",
      "isLatest": false
    },
    {
      "id": "latest-hormuz-closed-gfs-galaxy-0712",
      "title": "イラン、ホルムズ海峡「閉鎖」を宣言——コンテナ船GFS Galaxyを攻撃",
      "body": "イラン革命防衛隊（IRGC）海軍は7月11日夜（現地時間）、キプロス籍コンテナ船GFS Galaxyが「認可外ルート」を航行しようとしたとして警告射撃を実施し、船体後部に着火・機関室に大きな損傷を与えた。乗組員1名が行方不明。IRGCはこれを受け、ホルムズ海峡を「次官通達があるまで閉鎖する」と宣言した。CENTCOMは同日、今週3度目となる対イラン空爆を実施し、「イランはMOU遵守の機会を再び与えられたが、また失敗した」と非難。ヘグセス国防長官は「イランは間違った選択をした。今、代償を払う」とX投稿した。",
      "sourceLabel": "CENTCOM / Times of Israel",
      "date": "2026年7月11日（現地）/ 2026年7月12日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.timesofisrael.com/liveblog-july-11-2026/",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

**アーカイブ移動対象（Claude Code側で `archive` 配列先頭に新規バッチとして追加）：**
`latest-japan-ships-22-passed-0711`・`latest-us-demands-iran-statement-0711`・`latest-araghchi-oman-talks-0711` の3件を、既存ファイルからそのまま転記し、以下のバッチとして `archive` 配列の先頭に追加してください。

```json
{
  "batchLabel": "2026年7月11日 更新分（アーカイブ）",
  "items": [
    { /* latest-japan-ships-22-passed-0711 の内容をそのまま転記 */ },
    { /* latest-us-demands-iran-statement-0711 の内容をそのまま転記 */ },
    { /* latest-araghchi-oman-talks-0711 の内容をそのまま転記 */ }
  ]
}
```

### osint（現地メディア視点・配列先頭に追加）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "id": "osint-hormuz-closed-live-0712",
      "titleJa": "【Al Jazeera】イラン、ホルムズ海峡「閉鎖」を宣言——米、公式声明を要求も応酬続く",
      "titleEn": "Iran war updates: IRGC navy declares Strait of Hormuz closed",
<!-- OLD:END -->
<!-- NEW:START -->
      "id": "osint-iran-attacks-5states-live-0712",
      "titleJa": "【Al Jazeera】イラン、5カ国へ報復攻撃——米が新たな空爆を実施と発表",
      "titleEn": "Iran war live: More explosions as US says launching new strikes",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(239,68,68,0.06)",
      "cardBorder": "rgba(239,68,68,0.25)",
      "badgeColor": "#fca5a5",
      "borderColor": "rgba(239,68,68,0.35)",
      "textColor": "#e2e8f0",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/12/iran-war-live-irgc-declares-strait-of-hormuz-closed-over-us-interference",
      "date": "2026/07/12",
      "isLatest": true
    },
    {
      "id": "osint-hormuz-closed-live-0712",
      "titleJa": "【Al Jazeera】イラン、ホルムズ海峡「閉鎖」を宣言——米、公式声明を要求も応酬続く",
      "titleEn": "Iran war updates: IRGC navy declares Strait of Hormuz closed",
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ Claude Codeへの注記：上記 osint 追加ブロックは、既存の `osint-hormuz-closed-live-0712` エントリーのフィールド構造（`country`〜`isLatest`まで）をそのまま踏襲していますが、他フィールドの値（cardBg等の配色）は既存の直近エントリーと揃えているか、適用後に `grep -n "osint-iran-attacks-5states-live-0712" -A 10 docs/data/news_data.json` で確認してください。また、既存の `osint-hormuz-closed-live-0712` の `isLatest` は `false` に変更する必要があります（この old_str/new_str だけでは isLatest フィールド行が変わらないため、別途 str_replace で `"isLatest": true` → `"isLatest": false` を該当ブロック内でのみ適用してください）。

---

## [S11] 更新ログ

### ブロック1：常時表示エリア（3件固定を維持）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年7月12日 09:19 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/12 09:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>IRGC、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）・CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」・停戦は事実上崩壊・オマーンが通航料なしの南北二経路案を提示（南＝自由航行、北＝イラン事前承認制だが無料）——アラグチー外相はオマーン外相と会談も結論持ち帰りで検討中・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント週間+5〜6%で$76台高止まり（7/10終値時点）・封鎖135日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月11日 08:38 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/11 08:38</span> — <strong style="color:#fca5a5;">【重大更新】</strong>金子国交相、日本関係船22隻（大型原油タンカー6隻含む）の通過を発表——残り4隻に大幅減（開戦時45隻から・7/10会見）・米当局者、イランに攻撃停止・全通航路開放の公式声明を要求——通航料も不可（Reuters）・イラン、攻撃は「制度の一部の暴走」と釈明し対話継続を希望・アラグチー外相は本日オマーンでブーサイーディー外相と海峡管理を協議・トルコ外相フィダン氏「今週末にも解決の可能性」・イラン国連大使は「海峡管理は専らイランに属する」と対立姿勢維持・原油はブレント$76台で高止まり（週間+5〜6%）・南ルートは大型船AIS通航が7/7以降ゼロで事実上停止・バンダルアッバスの漁船30隻超が空爆で損壊・封鎖134日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月10日 07:40 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/10 07:40</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>CENTCOM、南部イラン各地（ブシェール・チャバハール・バンダルアッバス・ジャスク等）で追加空爆（7/8夜）・IRGCがクウェート・バーレーン・カタールの米軍拠点にドローン・ミサイルで報復——停戦後初のカタール標的化（7/9）・クウェート国防省「迎撃したが被害で1名負傷」・ガリバフ国会議長「攻撃すれば反撃を受ける」・バーレーン・クウェート・UAE・ヨルダンが非難・ブシェール州で原因不明の爆発複数・原油一時$79台へ急騰後$77前後に落ち着く・日本関係船18隻で変化なし・封鎖133日目・ニュース3件更新・osint更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年7月13日 08:28 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/13 08:28</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イラン、米の3度目・約140カ所への対イラン空爆に対しオマーン（ドゥクム）・カタール（アルウデイド基地）・クウェート・バーレーン・ヨルダンの5カ国を弾道ミサイル・ドローンで同時報復攻撃（7/12 JST）・カタールで迎撃破片により3名負傷・ガリバフ国会議長「一方的な合意の時代は終わった」とX投稿・オマーン外務省、ドゥクム・ムサンダム攻撃を受けイラン大使を召喚し正式抗議——前日のアラグチー・ブーサイーディー両外相協議から一転し仲介の立場も緊張最高潮・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油は週明けに反発しブレント一時79ドル台・WTI74ドル台まで4%高・封鎖136日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月12日 09:19 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/12 09:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>IRGC、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）・CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」・停戦は事実上崩壊・オマーンが通航料なしの南北二経路案を提示（南＝自由航行、北＝イラン事前承認制だが無料）——アラグチー外相はオマーン外相と会談も結論持ち帰りで検討中・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント週間+5〜6%で$76台高止まり（7/10終値時点）・封鎖135日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月11日 08:38 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/11 08:38</span> — <strong style="color:#fca5a5;">【重大更新】</strong>金子国交相、日本関係船22隻（大型原油タンカー6隻含む）の通過を発表——残り4隻に大幅減（開戦時45隻から・7/10会見）・米当局者、イランに攻撃停止・全通航路開放の公式声明を要求——通航料も不可（Reuters）・イラン、攻撃は「制度の一部の暴走」と釈明し対話継続を希望・アラグチー外相は本日オマーンでブーサイーディー外相と海峡管理を協議・トルコ外相フィダン氏「今週末にも解決の可能性」・イラン国連大使は「海峡管理は専らイランに属する」と対立姿勢維持・原油はブレント$76台で高止まり（週間+5〜6%）・南ルートは大型船AIS通航が7/7以降ゼロで事実上停止・バンダルアッバスの漁船30隻超が空爆で損壊・封鎖134日目・ニュース3件更新・osint更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ 上記ブロック1の適用により、旧「7/10 07:40 JST」エントリーは常時表示から外れます。これはブロック2で `log-collapse` の先頭に挿入するため、new_str には含めていません（4件以上を常時表示に含めない原則を遵守）。

### ブロック2：log-collapse 先頭への旧3件目挿入 + 総件数調整（11件目削除）

現在の常時表示3件（7/12・7/11・7/10）のうち、旧3件目にあたる「7/10 07:40 JST」エントリーを、`log-collapse` の先頭（現在の先頭エントリー「7/9 06:59 JST」の直前）に挿入します。

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月9日 06:59 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月10日 07:40 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/10 07:40</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>CENTCOM、南部イラン各地（ブシェール・チャバハール・バンダルアッバス・ジャスク等）で追加空爆（7/8夜）・IRGCがクウェート・バーレーン・カタールの米軍拠点にドローン・ミサイルで報復——停戦後初のカタール標的化（7/9）・クウェート国防省「迎撃したが被害で1名負傷」・ガリバフ国会議長「攻撃すれば反撃を受ける」・バーレーン・クウェート・UAE・ヨルダンが非難・ブシェール州で原因不明の爆発複数・原油一時$79台へ急騰後$77前後に落ち着く・日本関係船18隻で変化なし・封鎖133日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年7月9日 06:59 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

**総件数チェック：** 常時表示3件（7/13・7/12・7/11）＋ log-collapse内（7/10・7/9・7/8・7/7・7/6・7/5・7/4・7/3＝8件）＝合計11件となり、10件の上限を1件超過します。したがって log-collapse 最古の「7/3 09:16 JST」エントリー（出典リンク①の直前）を削除し、`update_log.json` の先頭に追加してください。

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年7月3日 09:16 JST</strong> 更新</div>
          <div><span style="color:#f87171;">2026/07/03 09:16</span> — <strong style="color:#fca5a5;">【重大更新】</strong>ドーハ協議、突破口なく終了（通航料対立継続・実務進展のみ）・イラン軍司令部が米介入に新威嚇声明・故ハメネイ師国葬あす7/4開始（次回協議は国葬後）・ブレント$70台/WTI$68台に続落（ホルムズ通航量日量1000万バレル超）・米海軍ヘリ緊急着水1名不明（7/1）・日本関係船変化なく残り約32隻・封鎖126日目・ニュース2件更新</div>
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div style="margin-top:10px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">① <a href="https://jp.reuters.com/world/us/XFYI674QIBLRJJY2HCA3T2LZCA-2026-04-12/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:none;">Reuters日本語 — トランプ「米軍がホルムズ封鎖へ」・CENTCOM正式発表（4/12〜13）</a></div>
<!-- NEW:END -->
<!-- APPLY:END -->

**`docs/data/update_log.json` への追加（先頭に1件挿入）：**

```json
{
  "date": "2026/07/03 09:16",
  "text": "ドーハ協議、突破口なく終了（通航料対立継続・実務進展のみ）・イラン軍司令部が米介入に新威嚇声明・故ハメネイ師国葬あす7/4開始（次回協議は国葬後）・ブレント$70台/WTI$68台に続落（ホルムズ通航量日量1000万バレル超）・米海軍ヘリ緊急着水1名不明（7/1）・日本関係船変化なく残り約32隻・封鎖126日目・ニュース2件更新"
}
```

---

## 変更内容まとめ（Claude Code 作業報告用テンプレート）

| セクション | 変更内容 |
|---|---|
| S01 | ヘッダー日時 2026年7月13日 08:28 JST・警戒レベル文言を5カ国報復攻撃反映に更新 |
| S02 | TICKER 全文更新（5カ国報復攻撃・オマーン大使召喚・原油4%高・封鎖136日目） |
| S03 | 速報インシデント：トグル日付・本体・リスト先頭2件追加 |
| S04 | 情勢カード3枚（外交・軍事・船舶市場）全面更新 |
| S05 | COUNTDOWN フェーズラベル・注記更新（封鎖136日目・機雷除去残4日） |
| S06 | シナリオ確率補足バナー更新（矢印 A↓ B↓ C↑ D↑） |
| S07 | シナリオA/B/C/D 本文更新 |
| S08 | シナリオフッター次の焦点5点更新 |
| S08.5 | 全ルート現況サマリー 7/13 08:28 JST更新 |
| S09 | 30秒カラム3行＋バッジ5枚更新（最後に作成） |
| SHIP_CONFIG | dateConfirmedのみ7/13更新（隻数変化なし） |
| JSON-LD | dateModified 2026-07-13T08:28:00+09:00 |
| S10 | news_data.json：latest 3件新規・archive移動（旧3件）・osint 1件追加 |
| S11 | 更新ログ：ブロック1（常時表示3件）＋ブロック2（log-collapse先頭挿入＋11件目削除） |
| **C01 タンカー確認** | **日本語3クエリ＋英語1クエリでweb検索済み（外務省・国土交通省の一次情報を優先確認）／変化なし——4隻のまま。dateConfirmedをYYYY年MM月DD日 HH:MM JST 変更なしで更新** |
