# index_html_diffs.md — 2026年7月12日 09:19 JST 更新分

> Claude Code への指示：以下の差分を index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> news_data.json の変更は [S10] の指示に従い、既存ファイルへのマージとして適用してください。
> 適用後、C01タンカー確認行を含めた変更内容まとめを提示し、commit してください。push は確認後に指示します。

---

## ✅ 出力前セルフチェック（本日のチェックリスト）

本日のセルフチェック項目数：14件

```
[✓] S01 ヘッダー ― 2026年7月12日 09:19 JST に更新
[✓] S02 TICKER ― ホルムズ海峡「閉鎖」宣言／米3度目の空爆／オマーン無料二経路案／日本関係船変化なし／封鎖135日目、全てJST表記あり
[✓] S03 速報インシデント ― 7/12 09:19付け・新規2件を先頭に追加
[✓] S04 情勢カード3枚 ― 外交／軍事／市場・船舶を本日情勢に更新
[✓] S05 COUNTDOWN ― 封鎖135日目・機雷除去期限残5日・MOU最終期限残35日
[✓] S06 シナリオ確率補足バナー ― 7/12 09:19 JST日付・矢印（A↓ B→ C↑ D↑）更新
[✓] S07 シナリオ4本 ― A/B/C/D本文を本日情勢（海峡閉鎖宣言・3度目空爆・オマーン提案）に更新
[✓] S08 シナリオフッター ― 次の焦点5点を本日版に更新
[✓] S08.5 全ルート現況サマリー ― 7/12 09:19 JST更新・海峡閉鎖宣言を反映
[✓] S09 30秒カラム ― 3行サマリー＋バッジ5枚更新（最後に作成）
[✓] SHIP_CONFIG ― totalShips 4（変化なし）・dateConfirmed 7/12 09:19 JSTに更新
[✓] JSON-LD dateModified ― 2026-07-12T09:19:00+09:00 に更新
[✓] S10 news_data.json更新メモ ― latest 3件新規・archive移動指示・osint 1件・updated日付
[✓] S11 更新ログ ― ブロック1（常時表示3件）＋ブロック2（log-collapse先頭挿入）＋11件超過分の削除指示
```

**C01 タンカー確認**：日本語クエリ3本（①「金子国土交通大臣 会見 ホルムズ海峡 7月12日」②「金子国土交通大臣 会見 ホルムズ海峡 7月11日」③「外務省 ホルムズ海峡 日本関係船舶 7月12日」）＋英語クエリ（"Japanese ships Strait of Hormuz stranded detained July 2026"）を個別実行し、外務省・国土交通省の一次情報を優先確認。**変化なし**——直近の会見は7/10（22隻通過・残り4隻）が最新であり、7/11・7/12時点で新たな会見・発表は確認されず。SHIP_CONFIGのdateConfirmedのみ本日日時・変更なしとして更新。

二重封鎖表記チェック：「イラン・米国による二重封鎖」の単独表記は変更していません（dl-boxは今回対象外）。
TICKER内JST表記チェック：全日付にJST付き ✓
ルート現況サマリー日付：S08.5内で7/12 09:19 JST更新を明示 ✓
人名表記チェック：「Xi」「Trump」単独表記なし（該当箇所なし、トランプ大統領と表記） ✓
Al Jazeera混入チェック：📰関連最新ニュース欄（news_data.json latest）には使用せず、🌐現地メディア視点（osint）にのみ使用 ✓
毎日新聞・Wikipedia混入チェック：使用なし ✓
URL捏造チェック：全URL web検索で実在確認済み（CENTCOM経由報道・CNN・Times of Israel・Al Jazeera）✓

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（金子国交相、日本関係船22隻の新規通過を発表——残り4隻に大幅減／米は対イランに攻撃停止の公式声明を要求、アラグチー外相は本日オマーンで海峡管理を協議・封鎖134日目）</span>
    <span class="badge-item badge-date">📅2026年7月11日 08:38 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イラン、コンテナ船GFS Galaxyを攻撃しホルムズ海峡「閉鎖」を宣言——米が今週3度目の対イラン空爆を実施し停戦は事実上崩壊／オマーンは通航料なしの南北二経路案を提示・イランは持ち帰り検討中／封鎖135日目）</span>
    <span class="badge-item badge-date">📅2026年7月12日 09:19 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年7月11日 08:38 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年7月11日 08:38 JST） -->
      🚨【日本関係船、残り4隻に大幅減】金子国交相、7〜9日にホルムズ海峡を通過した日本関係船舶22隻（日本向け大型原油タンカー6隻・原油約180万キロリットル含む）を発表——開戦時45隻から残り4隻に（7/10会見）｜🇺🇸 米当局者、イランに「攻撃停止・全通航路開放」を公式に表明するよう要求——通航料も認めない方針（Reuters 7/10）｜🇮🇷 イラン、米側に攻撃は「制度の一部が暴走した結果」と釈明——対話継続を希望（米当局者）｜🕊️ アラグチー外相、本日（7/11）オマーンでブーサイーディー外相とホルムズ海峡管理を協議——トルコ外相フィダン氏「今週末にも解決の可能性」と楽観視｜⚠️ イラン国連大使イラワニ氏「海峡の管理は専らイランに属する」と対立姿勢を崩さず｜🛢️ ブレント原油$76台で高止まり（週間+5〜6%）・南ルート（オマーン沿岸）は7/7以降10,000dwt超の大型船AIS通航ゼロ——事実上の通航停止（Lloyd's List）｜🎣 バンダルアッバスの漁船30隻超が米空爆で損壊（1隻あたり約1.1万ドル相当）｜⚠️ 機雷除去期限まで残6日・封鎖134日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年7月12日 09:19 JST） -->
      🚨【停戦事実上崩壊】イラン革命防衛隊、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃（「認可外ルート航行」を理由）——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）｜🇺🇸 CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」（7/12 JST）｜🕊️ オマーン、通航料なしの南北二経路案を提示——南ルートは戦前同様に自由航行、北ルート（イラン領海）は事前承認制だが無料（CNN 7/11）｜🇮🇷 アラグチー外相・ブーサイーディー外相会談は具体的合意なく終了、イランは提案を持ち帰り検討中｜🇯🇵 日本関係船、残り4隻で変化なし（7/12 09:19 JST再確認）｜🛢️ ブレント原油、週間+5〜6%で$76台高止まり（7/10終値時点）｜⚠️ 機雷除去期限まで残5日・封鎖135日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

**対象：** `<!-- 速報インシデント　トグルボタン -->` 内

### トグルボタン内タイトル・日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">日本関係船22隻通過・残り4隻／米、イランに攻撃停止の公式声明を要求・本日オマーンで協議</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/11 08:38 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">イラン、ホルムズ海峡「閉鎖」を宣言・米艦船攻撃で停戦事実上崩壊——米が3度目の空爆／オマーンが無料二経路案提示</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 7/12 09:19 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の `<strong>` タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/11 08:38 速報】金子国交相、日本関係船22隻がホルムズ海峡を通過したと発表（うち日本向け大型原油タンカー6隻）——残り4隻に大幅減（7/10会見）｜米当局者、イランに「攻撃停止・全通航路開放」の公式声明を要求——通航料も不可（Reuters）｜イラン、攻撃は「制度の一部が暴走した結果」と釈明・対話継続を希望｜アラグチー外相、本日オマーンでブーサイーディー外相とホルムズ海峡管理を協議｜イラン国連大使は「海峡管理は専らイランに属する」と対立姿勢を維持｜ブレント原油$76台で高止まり・南ルートは大型船AIS通航事実上ゼロ｜バンダルアッバスの漁船30隻超が空爆で損壊｜封鎖134日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【7/12 09:19 速報】イラン革命防衛隊、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）｜CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」｜停戦は事実上崩壊｜オマーン、通航料なしの南北二経路案を提示（南＝自由航行、北＝イラン事前承認制だが無料）｜アラグチー外相・ブーサイーディー外相会談は具体的合意なく終了、イランは提案を持ち帰り検討中｜日本関係船は残り4隻で変化なし｜原油はブレント週間+5〜6%で$76台高止まり｜封鎖135日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に新規2件を追加）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#86efac;font-weight:700;">🇯🇵 7/10 JST</span>
  <span style="color:#e2e8f0;"> 金子恭之国土交通相は10日の閣議後会見で、ペルシャ湾内に留め置かれていた日本関係船舶のうち新たに22隻（7〜9日の間）がホルムズ海峡を通過したと発表。うち6隻は日本向けの大型原油タンカーで、積載量は合計約180万キロリットル、20日程度かけて今月末に日本へ到着する見通し。乗組員の健康状態・船体に異常はなし。これにより湾内に留め置かれている日本関係船舶は、開戦時45隻から過去最少の残り4隻となった。</span>
</li>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚔️ 7/12 JST</span>
  <span style="color:#e2e8f0;"> イラン革命防衛隊（IRGC）海軍は、キプロス籍コンテナ船GFS Galaxyが「認可外ルート」を航行しようとしたとして警告射撃を実施し、船体後部に着火・機関室に大きな損傷を与えた（乗組員1名が行方不明）。IRGCはこれを受けホルムズ海峡を「次官通達があるまで閉鎖する」と宣言。CENTCOMはこれに対し今週3度目となる対イラン空爆を米東部時間7/11午後7時15分に開始したと発表し、「イランはMOU（覚書）遵守の機会を再び与えられたが、また失敗した」と非難した。ヘグセス国防長官はX投稿で「イランは間違った選択をした。今、代償を払う」と表明。イラン国営メディアはバンダルアッバス・ゲシュム島・ブシェール・アサルイェ・チャバハール・シリク等の沿岸各地で複数の爆発を報じた。トランプ大統領は「（自身が標的にされれば）即応態勢にある」と発言した。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🕊️ 7/11 JST</span>
  <span style="color:#e2e8f0;"> オマーンは、ホルムズ海峡の通航を南北2つの経路に分けて管理する案を提示したとCNNが関係筋の話として報道。南ルート（オマーン領海）は戦前同様に自由航行が可能、北ルート（イラン領海）は事前にイランの承認が必要だが通航料は課さない内容。イランのアラグチー外相とオマーンのブーサイーディー外相はマスカットで会談し、技術・政治レベルでの協議継続に合意したが、米政権が求める「海峡が全面的に開放され船舶の安全が確保されている」旨の公式声明表明には至らなかった。アラグチー外相の代表団は同案を承認せずテヘランに持ち帰り検討中とみられ、イラン側筋は「海峡に関する決定はイランとオマーンのみが行う」と強調している。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#86efac;font-weight:700;">🇯🇵 7/10 JST</span>
  <span style="color:#e2e8f0;"> 金子恭之国土交通相は10日の閣議後会見で、ペルシャ湾内に留め置かれていた日本関係船舶のうち新たに22隻（7〜9日の間）がホルムズ海峡を通過したと発表。うち6隻は日本向けの大型原油タンカーで、積載量は合計約180万キロリットル、20日程度かけて今月末に日本へ到着する見通し。乗組員の健康状態・船体に異常はなし。これにより湾内に留め置かれている日本関係船舶は、開戦時45隻から過去最少の残り4隻となった。</span>
</li>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 最新情勢カード（3枚）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🕊️ 外交：米、イランに攻撃停止の公式声明を要求——アラグチー外相は本日オマーンで海峡管理を協議</div>
        <div class="s-body">米当局者は7/10、イランに対しホルムズ海峡の全通航路が開放され船舶への攻撃をやめる旨を公式に表明するよう要求していると明らかにした。通航料の徴収も認めない方針。イラン側は非公式に、今回の攻撃は「制度の一部が暴走した結果」であり対話継続を望んでいると伝えたという。アラグチー外相は7/11（現地時間）にオマーンを訪問し、ブーサイーディー外相とホルムズ海峡の管理問題を協議する予定で、トルコのフィダン外相は「今週末にも解決の可能性がある」と楽観的な見方を示した。一方でイランの国連大使イラワニ氏は、海峡の開放・機雷除去を含む運用は「専らイランに属する」と述べ、対立姿勢を崩していない。パキスタンのシャリフ首相もペゼシュキアン大統領と電話協議し、自制と対話の継続を呼びかけた。</div>
        <div class="s-src">出典: Reuters / AP / Al Jazeera（7/11 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🕊️ 外交：オマーンが無料の南北二経路案を提示——イランは持ち帰り検討、米要求の公式声明は不発</div>
        <div class="s-body">オマーンは通航料を課さない南北二経路案を提示したとCNNが報じた。南ルート（オマーン領海）は戦前同様に自由航行、北ルート（イラン領海）は事前承認制だが無料。アラグチー外相・ブーサイーディー外相は7/11マスカットで会談し技術・政治協議の継続で合意したが、米政権が求める「海峡は全面開放され安全」との公式声明表明には至らず、イラン側は提案をテヘランに持ち帰り検討中。イラン側筋は「海峡に関する決定はイランとオマーンのみが行う」と強調しており、対立点は未解消のまま。</div>
        <div class="s-src">出典: CNN / Israel National News（7/12 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇯🇵 船舶・エネルギー：日本関係船、残り4隻に大幅減——原油は$76台で高止まり</div>
        <div class="s-body">金子恭之国土交通相は7/10の閣議後会見で、7〜9日にホルムズ海峡を通過した日本関係船舶22隻（過去最大規模）を発表した。うち6隻は日本向け大型原油タンカーで、積載する原油量は合計約180万キロリットル、今月末には日本に到着する見通し。乗組員の健康状態・船体に異常はなし。これにより湾内に留め置かれている日本関係船舶は、開戦時45隻から残り4隻となった。一方、原油市場はブレント原油が$76台で高止まりし、週間では約5〜6％の上昇（Trading Economics：$76.58前後）。南ルート（オマーン沿岸）では7/7以降、10,000dwt超の大型船がAISを作動させて通航した実績がなく、Lloyd's Listは「事実上の通航停止」状態と指摘している。</div>
        <div class="s-src">出典: 国土交通省 / 時事通信 / NHK / Trading Economics / Al Jazeera（7/11 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">⚔️ 軍事：イラン、コンテナ船GFS Galaxyを攻撃しホルムズ海峡「閉鎖」宣言——米が3度目の空爆</div>
        <div class="s-body">IRGC海軍は「認可外ルート」を航行したとしてキプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃を実施（乗組員1名行方不明・機関室損傷）し、ホルムズ海峡を「次官通達まで閉鎖」と宣言した。CENTCOMは即座に今週3度目となる対イラン空爆を実施し、「イランはMOU遵守の機会を再び与えられたが、また失敗した」と非難。ヘグセス国防長官は「イランは間違った選択をした。今、代償を払う」とX投稿。イラン国営メディアはバンダルアッバス・ゲシュム島・ブシェール等各地での爆発を報道し、停戦は事実上崩壊した状態にある。</div>
        <div class="s-src">出典: CENTCOM / Times of Israel / Haaretz（7/12 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">⚠️ 安全保障：軍事衝突は小康状態も機雷除去は未着手のまま期限迫る——漁船被害も判明</div>
        <div class="s-body">7/9のクウェート・バーレーン・カタールへの報復攻撃以降、目立った新規攻撃の報告はなく、軍事的には小康状態にある。もっとも、バンダルアッバスのパンジュ・ペレ漁港では、7/8〜9の米空爆により漁船30隻超が損壊し、1隻あたり約1.1万ドル相当の損失が生じたと地元漁業協同組合関係者が明らかにした。機雷除去は依然未着手のまま7/17の除去期限まで残6日、8/16のMOU最終期限まで残36日に迫っている。イラン国連大使は海峡の管理・機雷除去は「専らイランに属する」と述べ、第三者の関与を強く牽制した。</div>
        <div class="s-src">出典: IRNA / RFE/RL / Reuters（7/11 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇯🇵 船舶・市場：日本関係船は残り4隻で変化なし——原油は週間+5〜6%で$76台高止まり</div>
        <div class="s-body">日本関係船舶は7/10会見の残り4隻から変化なし（7/12 09:19 JST再確認・外務省・国土交通省への日英クエリで新規発表なしを確認）。原油市場はブレント原油が7/10終値時点で$76台にとどまり、週間では約5〜6％の上昇。市場は週末（土日）の閉場中に発生した本件（IRGCによるGFS Galaxy攻撃・米の3度目の空爆・海峡閉鎖宣言）を織り込んでおらず、週明けの反応が焦点となる。機雷除去は依然未着手のまま7/17の除去期限まで残5日、8/16のMOU最終期限まで残35日に迫っている。</div>
        <div class="s-src">出典: Trading Economics / 国土交通省 / 外務省（7/12 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（日本関係船22隻通過で残り4隻に・米はイランに攻撃停止の公式声明を要求）」——封鎖134日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU実装・60日交渉フェーズ（イラン、ホルムズ海峡「閉鎖」宣言・米が3度目の空爆で停戦事実上崩壊）」——封鎖135日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🚨 <strong>金子国交相、日本関係船22隻の通過を発表——残り4隻に大幅減（うち大型原油タンカー6隻）／米、イランに攻撃停止・全通航路開放の公式声明を要求／アラグチー外相は本日オマーンで海峡管理を協議／原油は$76台で高止まり——封鎖134日目・MOU機雷除去期限残6日（7/17）・MOU最終期限残36日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①アラグチー外相・オマーン外相会談の結果 ②イランが米要求（攻撃停止の公式声明）に応じるか ③残る日本関係船4隻の通過見通し ④機雷除去着手の有無（期限まで残6日） ⑤バンダルアッバス漁船被害への補償・反発の広がり</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残6日（7/17）</span>
<!-- OLD:END -->
<!-- NEW:START -->
        🚨 <strong>イラン、コンテナ船GFS Galaxyを攻撃しホルムズ海峡「閉鎖」を宣言——米が今週3度目の対イラン空爆を実施し停戦は事実上崩壊／オマーンは通航料なしの南北二経路案を提示・イランは持ち帰り検討中／日本関係船は残り4隻で変化なし／原油は週間+5〜6%で$76台高止まり——封鎖135日目・MOU機雷除去期限残5日（7/17）・MOU最終期限残35日（8/16）</strong>
        <br><span style="color:#fde68a;">⚡ 次の焦点：①イランがオマーンの無料二経路案を受諾するか ②米国要求（攻撃停止・全通航路開放の公式声明）にイランが応じるか ③新たな軍事衝突がさらに拡大するか ④残る日本関係船4隻の安全確保 ⑤機雷除去着手の有無（期限まで残5日）</span>
        <br><span style="color:#fca5a5;">⏳ 機雷除去期限まで残5日（7/17）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#4ade80;">📊 2026年7月11日 08:38 JST 更新</span><br>
  📊 <strong>日本関係船22隻が通過し残り4隻に大幅減する一方、米はイランに攻撃停止の公式声明を要求——アラグチー外相は本日オマーンで海峡管理を協議：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#4ade80;">↑</span> — イランが攻撃を「制度の一部の暴走」と釈明し対話継続を希望・オマーン協議に前向きな兆し<br>
  🅑 膠着継続 <span style="color:#fbbf24;">→</span> — イラン国連大使は「海峡管理は専らイランに属する」との立場を崩さず対立点は残存<br>
  🅒 MOU形骸化・機能不全 <span style="color:#fbbf24;">→</span> — 軍事衝突は小康状態だが機雷除去は未着手のまま期限が迫る<br>
  🅓 全面対決・無期限封鎖 <span style="color:#4ade80;">↓</span> — 新規攻撃は報告されず、日本関係船の大量通過も緊張緩和の兆候として作用<br>
  <strong style="color:#4ade80;">日本関係船の大量通過と米イラン双方の対話継続姿勢によりA・Dの改善方向が優勢だが、海峡管理を巡る対立は未解消（A↑ B→ C→ D↓）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年7月11日 08:38 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] 4つのシナリオ本文（A/B/C/D）

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>7/10、金子国交相は日本関係船舶22隻（大型原油タンカー6隻を含む）がホルムズ海峡を通過したと発表し、湾内残存は開戦時45隻からわずか4隻にまで減少した。同時に米当局者は、イラン側が今回の攻撃を「制度の一部の暴走」と釈明し対話継続を希望していると明らかにし、イランに攻撃停止・全通航路開放の公式声明を要求している。アラグチー外相は7/11、オマーンのブーサイーディー外相と海峡管理を協議する予定で、トルコのフィダン外相も「今週末にも解決の可能性」と楽観的な見方を示した。日本関係船のほぼ全船通過という実務面での大きな前進と、米イラン双方の対話継続姿勢が重なり、段階的MOU履行への期待がやや高まっている。ただしイラン国連大使は海峡管理は「専らイランに属する」と述べており、最終的な制度設計を巡る対立は解消していない。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>7/11、イラン革命防衛隊はキプロス籍コンテナ船GFS Galaxyを「認可外ルート」航行を理由に攻撃し、ホルムズ海峡を「次官通達まで閉鎖」と宣言した。これを受け米は今週3度目となる対イラン空爆を実施し、前日まで期待されていた段階的なMOU履行の流れは大きく後退した。一方でオマーンは通航料なしの南北二経路案（南＝自由航行、北＝イラン事前承認制だが無料）を提示しており、アラグチー・ブーサイーディー両外相も技術・政治協議の継続に合意している。イラン側が同案を検討していること自体は交渉ルートが完全に閉ざされたわけではないことを示すが、海峡閉鎖宣言と武力行使が先行した状況では、本シナリオの実現確率は明確に後退したと評価せざるを得ない。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>日本関係船22隻の大量通過は前進材料である一方、南ルート（オマーン沿岸）では7/7以降、10,000dwt超の大型船がAISを作動させて通航した実績がなく、Lloyd's Listは「事実上の通航停止」と指摘している。つまり通航そのものはイラン管理ルート経由に事実上集約されつつあり、通航料徴収を含む恒久的な管理体制へ既成事実化が進んでいる可能性がある。イラン国連大使が海峡の運用は「専らイランに属する」と明言したことも、この路線を印象づける。主要海運4社（Maersk・MSC・CMA CGM・Hapag-Lloyd）は戦争保険水準が下がるまで復帰しない方針を維持しており、機雷約80個が除去されない限り完全正常化は遠い。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>オマーンが提示した通航料なしの南北二経路案は、南ルート（オマーン領海）での自由航行と北ルート（イラン領海）での事前承認制無料航行を組み合わせるもので、イラン・米双方にとって受け入れ余地のある妥協案となり得る。しかしイランの代表団は同案を即座に承認せずテヘランへ持ち帰っており、承認の可否・時期は不透明なままだ。GFS Galaxy攻撃とホルムズ海峡閉鎖宣言が既に発生している以上、仮に案が承認されても実務適用までには一定のタイムラグが生じる見込みで、当面は交渉と衝突が併存する膠着状態が続く可能性が高い。主要海運4社（Maersk・MSC・CMA CGM・Hapag-Lloyd）は戦争保険水準が下がるまで復帰しない方針を維持している。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>機雷除去は依然未着手のまま7/17期限（残6日）が迫っており、イラン国連大使は海峡の運用・機雷除去は「専らイランに属する」と改めて明言し、第三者関与を強く牽制した。日本関係船22隻の大量通過はイラン指定ルート経由での個別調整通航が機能していることを示す一方、共通インフラである機雷除去には依然着手の兆しがない——これは「共通インフラは機能不全のまま、個別調整による通航のみが機能する」という本シナリオの状態を体現している。加えてバンダルアッバスの漁船30隻超が空爆で損壊するなど、地元経済への実害も蓄積しつつある。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>機雷除去は依然未着手のまま7/17期限（残5日）が目前に迫っている。今回、イランが自ら海峡を「次官通達まで閉鎖」と宣言したことは、除去着手どころか通航そのものの安定運用すら実現していない現実を象徴している。オマーンの二経路案が実務レベルの通航ルールを提示している一方、機雷除去・海峡管理という共通インフラの整備は棚上げされたままであり、「共通インフラは機能不全のまま、個別交渉による部分的な通航のみが試みられる」という本シナリオの様相が一段と強まっている。バンダルアッバスの漁船被害等、地元経済への実害も引き続き蓄積している。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>7/9のクウェート・バーレーン・カタールへの報復攻撃以降、新たな大規模攻撃の応酬は報告されておらず、軍事的には小康状態にある。むしろ日本関係船22隻の大量通過や、米イラン双方が対話継続の意向を示していること（イラン側の「制度の一部が暴走した」との釈明、アラグチー外相のオマーン訪問）は、本シナリオへの急速な移行リスクを後退させる材料である。シナリオCとの差：C=「機雷除去等の実務レベルでの機能不全」、D=「IRGCが複数国規模で実力行使・CENTCOM大規模報復・戦争再開」。今回の3カ国同時報復から2日以上新たな衝突が報告されていない点は、当面の収束方向を示唆するが、機雷除去やイランの海峡管理権を巡る対立が再燃すれば、再び本シナリオのリスクが高まる。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>7/11未明（JST）、IRGCがコンテナ船GFS Galaxyを攻撃しホルムズ海峡の「閉鎖」を一方的に宣言、これに対しCENTCOMが今週3度目となる対イラン空爆を実施した——7/9の3カ国同時報復以来、最大の軍事エスカレーションである。シナリオCとの差：C=「機雷除去等の実務レベルでの機能不全」、D=「IRGCによる艦船・インフラへの直接的な実力行使とCENTCOMの大規模報復の応酬」。今回はまさにDの定義に該当する事態が発生しており、リスクは直近で最も高い水準にある。他方でオマーンの仲介案・アラグチー外相のオマーン訪問は交渉ルートが完全に断たれていないことを示しており、今後数日の推移（イランのオマーン案への回答、追加の軍事応酬の有無）が本シナリオへの本格移行を左右する。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5点）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">アラグチー外相・オマーン外相会談（7/11）の結果</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イランが米要求（攻撃停止の公式声明）に応じるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">残る日本関係船4隻の通過見通し</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">機雷除去着手の有無（期限まで残6日）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">バンダルアッバス漁船被害への補償・反発の広がり</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月11日 08:38 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">イランがオマーンの無料二経路案を受諾するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">米国要求（攻撃停止・全通航路開放の公式声明）にイランが応じるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">新たな軍事衝突がさらに拡大するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">残る日本関係船4隻の安全確保</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">機雷除去着手の有無（期限まで残5日）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年7月12日 09:19 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月11日 08:38 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】JMIC（米海軍主導）が推奨する機雷除去済みルートだが、7/7以降10,000dwt超の大型船がAISを作動させて通航した実績はなく（Lloyd's List）、事実上の通航停止状態が継続。【北ルート（Iran coastline / IRGC管理）】イランのPGSA（ペルシャ湾海峡局・米OFAC制裁対象）が事前登録制で管理。金子国交相は7/10、7〜9日に日本関係船舶22隻（大型原油タンカー6隻含む）がホルムズ海峡を通過したと発表——湾内残存は開戦時45隻から残り4隻に大幅減。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残6日）。7/9のクウェート・バーレーン・カタールへの報復攻撃以降、新たな大規模攻撃は報告されていないが、バンダルアッバスの漁船30隻超が7/8〜9の空爆で損壊したと判明。米当局者はイランに攻撃停止・全通航路開放の公式声明を要求し、アラグチー外相は7/11オマーンでブーサイーディー外相と海峡管理を協議予定。【UKMTO 警戒水準】Substantial（継続）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。戦争保険8倍水準・ルート法的不確実性が解消されるまで復帰なし。🇯🇵 日本関係船舶：残り4隻（22隻通過・7/11 08:38 JST確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年7月12日 09:19 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【南ルート（Omani coastal corridor）】オマーンが通航料なしの自由航行案を提示（7/11・CNN）が、7/7以降10,000dwt超の大型船AIS通航実績はなく、事実上の通航停止状態が継続。【北ルート（Iran coastline / IRGC管理）】イランのPGSAが事前登録制で管理していたが、7/12未明（JST）、IRGCがキプロス籍コンテナ船GFS Galaxyへの警告射撃・着火攻撃を実施し、ホルムズ海峡を「次官通達まで閉鎖」と宣言——南北両ルートとも運用停止に近い状態に陥っている。これに対しCENTCOMは今週3度目の対イラン空爆を実施。オマーンは南北二経路案（北ルートは事前承認制だが無料）を提示しアラグチー・ブーサイーディー両外相が協議したが、イランは持ち帰り検討中で承認は未定。中央チャンネルの機雷約80個は除去完了まで通行不可。除去期限：7/17（MOU第5条・残5日）。【UKMTO 警戒水準】Substantial（継続、更なる引き上げの可能性）。【主要船社動向】Maersk・MSC・CMA CGM・Hapag-Lloyd：依然ケープ廻り。戦争保険水準・ルート法的不確実性が解消されるまで復帰なし。🇯🇵 日本関係船舶：残り4隻で変化なし（7/12 09:19 JST再確認・外務省/国交省へ日英クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ・最後に作成）

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇯🇵 日本関係船は残り4隻（開戦時45隻から）——アラグチー外相は本日オマーンで海峡管理を協議、原油は$76台で高止まり。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ アラグチー外相・オマーン外相会談の結果とイランが米要求に応じるかが焦点、封鎖134日目——機雷除去期限（7/17）まで残6日・MOU最終期限（8/16）まで36日。
</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇯🇵 イランがコンテナ船GFS Galaxyを攻撃しホルムズ海峡「閉鎖」を宣言——米が3度目の空爆を実施し停戦は事実上崩壊。日本関係船は残り4隻で変化なし。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
⏳ イランがオマーンの無料二経路案を受諾するかが焦点、封鎖135日目——機雷除去期限（7/17）まで残5日・MOU最終期限（8/16）まで35日。
</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇺🇸攻撃停止の声明要求</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️本日オマーンで協議</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油$76台高止まり</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🎣漁船30隻超が損壊</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🚨海峡「閉鎖」宣言</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚔️米が3度目の空爆</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️オマーン無料二経路案</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油$76台高止まり</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [SHIP_CONFIG] タンカー可視化パネル

<!-- APPLY:START -->
<!-- OLD:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年7月11日 08:38 JST 確認・22隻通過（うち大型原油タンカー6隻）で残り4隻に大幅減（金子国交相7/10発表、開戦時45隻から）'
};
<!-- OLD:END -->
<!-- NEW:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年7月12日 09:19 JST 確認・変化なし（4隻のまま。金子国交相の新規会見なし・外務省/国交省へ日英クエリで確認）'
};
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [JSON-LD] dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-07-11T08:38:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-07-12T09:19:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新メモ

### updated / staleNotice

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年7月11日 08:38 日本時間JST",
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年7月12日 09:19 日本時間JST",
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列（新規3件を先頭に追加・既存の isLatest フラグ移動）

latest は現在6件（`latest-japan-ships-22-passed-0711` に isLatest:true）。新規3件を先頭に追加すると9件になるため、
Claude Code は既存の最も古い3件（`latest-irgc-kuwait-bahrain-qatar-0710`・`latest-ghalibaf-araghchi-warning-0710`・`latest-oil-volatile-0710`）を
新規アーカイブバッチ「2026年7月10日 更新分（アーカイブ）」として `archive` 配列の先頭に移動してください（本文は既存ファイルに保存済みのため、そのまま転記）。
また、現在 `isLatest: true` の `latest-japan-ships-22-passed-0711` は `isLatest: false` に変更してください。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "id": "latest-japan-ships-22-passed-0711",
<!-- OLD:END -->
<!-- NEW:START -->
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
    {
      "id": "latest-oman-tollfree-corridor-0712",
      "title": "オマーン、通航料なしの南北二経路案を提示——イランは持ち帰り検討",
      "body": "オマーンはホルムズ海峡の通航を南北2つの経路に分けて管理する案を提示したとCNNが関係筋の話として報じた。南ルート（オマーン領海）は戦前同様に自由航行が可能、北ルート（イラン領海）は事前にイランの承認が必要だが通航料は課さない内容。イランのアラグチー外相とオマーンのブーサイーディー外相は7月11日マスカットで会談し、技術・政治レベルでの協議継続に合意したが、米政権が求める公式声明表明には至らず、イラン側は同案を承認せずテヘランに持ち帰り検討中とみられる。",
      "sourceLabel": "CNN",
      "date": "2026年7月11日（現地）/ 2026年7月12日 JST",
      "label": "🕊️ 外交",
      "url": "https://www.cnn.com/2026/07/11/world/live-news/iran-war-trump",
      "isLatest": false
    },
    {
      "id": "latest-us-third-strikes-hegseth-0712",
      "title": "米、今週3度目の対イラン空爆——ヘグセス長官「代償を払う」",
      "body": "米中央軍（CENTCOM）は7月11日、GFS Galaxy攻撃への対応として今週3度目となる対イラン空爆を実施したと発表した。ヘグセス国防長官はX投稿で「イランは間違った選択をした。今、代償を払う」と表明。イラン国営メディアはバンダルアッバス・ゲシュム島・ブシェール・アサルイェ・チャバハール・シリク等の沿岸各地で複数の爆発を報じた。トランプ大統領は自身が標的にされた場合は即応する用意があると述べた。",
      "sourceLabel": "Times of Israel / Haaretz",
      "date": "2026年7月11日（現地）/ 2026年7月12日 JST",
      "label": "⚔️ 軍事衝突",
      "url": "https://www.haaretz.com/israel-news/israel-security/2026-07-11/ty-article-live/aoc-calls-to-release-gaza-hospital-director-hussam-abu-safiya/0000019f-4de2-d38b-afbf-5ff684110004",
      "isLatest": false
    },
    {
      "id": "latest-japan-ships-22-passed-0711",
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
      "url": "https://www.nippon.com/en/news/yjj2026071000499/",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
      "url": "https://www.nippon.com/en/news/yjj2026071000499/",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

### archive への移動（latest の末尾3件を新規バッチとして先頭に追加）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "archive": [
    {
      "batchLabel": "2026年7月9日 更新分（アーカイブ）",
<!-- OLD:END -->
<!-- NEW:START -->
  "archive": [
    {
      "batchLabel": "2026年7月10日 更新分（アーカイブ）",
      "items": [
        {
          "id": "latest-irgc-kuwait-bahrain-qatar-0710",
          "title": "IRGC、クウェート・バーレーン・カタールの米軍拠点に報復攻撃——1名負傷",
          "body": "イラン革命防衛隊（IRGC）は7月9日、CENTCOMによる前夜の追加空爆への報復として、クウェート（Ali Al Salem基地）、バーレーン（第5艦隊拠点）、カタール（早期警戒システム）の米軍関連拠点にドローン・ミサイルによる攻撃を実施したと発表した。停戦後、カタールが標的となったのは初めて。クウェート国防省は弾道ミサイル3発・巡航ミサイル1発・ドローン10機を迎撃したとしたが、迎撃に伴う被害で少なくとも1名が負傷（容体は安定）したと明らかにした。バーレーン・クウェート・UAE・ヨルダンはイランの攻撃を「主権への明白な侵害」として一斉に非難した。",
          "sourceLabel": "RFE/RL",
          "date": "2026年7月9日（現地）/ 2026年7月9日 JST",
          "label": "⚔️ 軍事衝突",
          "url": "https://www.rferl.org/a/iran-war-us-hormuz-oil-blockade-gulf-israel/33640284.html",
          "isLatest": false
        },
        {
          "id": "latest-ghalibaf-araghchi-warning-0710",
          "title": "ガリバフ国会議長「攻撃すれば反撃を受ける」——アラグチー外相も対米強硬姿勢",
          "body": "イラン国会議長で対米交渉責任者のモハマド・バゲル・ガリバフ氏は7月9日、X投稿で米国は「いじめや約束違反がもはや罰せられないままでは済まされない」と警告し、「攻撃すれば、反撃を受ける」と述べた。ホルムズ海峡の航行は「イランの取り決めの下でのみ」可能と改めて主張。アラグチー外相もトランプ大統領の対イラン発言を「下品な物言い」と批判し、イランの対応は「決然として恐れず、全力」であると表明した。",
          "sourceLabel": "CNN",
          "date": "2026年7月9日（現地）/ 2026年7月9日 JST",
          "label": "🕊️ 外交",
          "url": "https://www.cnn.com/2026/07/09/middleeast/iran-us-ceasefire-attacks-resume-intl-hnk",
          "isLatest": false
        },
        {
          "id": "latest-oil-volatile-0710",
          "title": "原油、一時ブレント$79台へ急騰後$77前後に落ち着く",
          "body": "軍事衝突拡大を受け、ブレント原油は7月9日に一時1バレル=79ドル台まで急騰し、6月23日以来の高値を付けた。その後は伸び悩み、Trading Economicsによれば同日終値は76.97ドル（前日比-1.35%）。WTIも73ドル台前半で推移している。トレーダーは軍事衝突がさらなる報復につながるか、収束に向かうかを見極めている段階だとの指摘が出ている。",
          "sourceLabel": "Trading Economics / Kitco・Reuters",
          "date": "2026年7月9日（現地）/ 2026年7月10日 JST",
          "label": "🛢️ 原油市場",
          "url": "https://www.kitco.com/news/off-the-wire/2026-07-09/oil-prices-fall-markets-weigh-impact-us-strikes-iran",
          "isLatest": false
        }
      ]
    },
    {
      "batchLabel": "2026年7月9日 更新分（アーカイブ）",
<!-- NEW:END -->
<!-- APPLY:END -->

### osint（現地メディア視点）最新1件の更新

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "id": "osint-hormuz-traffic-halt-0711",
      "titleJa": "【Al Jazeera】ホルムズ海峡の通航、事実上停止——大型船のAIS通航は7/7以降ゼロ",
      "titleEn": "Strait of Hormuz traffic plunges as US, Iran resume fighting",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/economy/2026/7/10/strait-of-hormuz-shipping-grinds-to-halt-as-us-iran-resume-fighting",
      "date": "2026年7月10日（現地）/ 2026年7月10日 JST",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "id": "osint-hormuz-closed-live-0712",
      "titleJa": "【Al Jazeera】イラン、ホルムズ海峡「閉鎖」を宣言——米、公式声明を要求も応酬続く",
      "titleEn": "Iran war updates: IRGC navy declares Strait of Hormuz closed",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/news/liveblog/2026/7/11/iran-war-live-us-demands-iran-publicly-state-strait-of-hormuz-open-for-all",
      "date": "2026年7月11日（現地）/ 2026年7月12日 JST",
      "isLatest": true
    },
    {
      "id": "osint-hormuz-traffic-halt-0711",
      "titleJa": "【Al Jazeera】ホルムズ海峡の通航、事実上停止——大型船のAIS通航は7/7以降ゼロ",
      "titleEn": "Strait of Hormuz traffic plunges as US, Iran resume fighting",
      "country": "カタール",
      "media": "Al Jazeera",
      "cardBg": "rgba(56,189,248,0.05)",
      "cardBorder": "rgba(56,189,248,0.25)",
      "badgeColor": "#38bdf8",
      "borderColor": "rgba(56,189,248,0.4)",
      "textColor": "#7dd3fc",
      "url": "https://www.aljazeera.com/economy/2026/7/10/strait-of-hormuz-shipping-grinds-to-halt-as-us-iran-resume-fighting",
      "date": "2026年7月10日（現地）/ 2026年7月10日 JST",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S11] 更新ログ（2ブロック構成＋超過分削除）

### ブロック1：常時表示3件の更新（本日分を追加し、旧3件目を押し出す）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年7月11日 08:38 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/11 08:38</span> — <strong style="color:#fca5a5;">【重大更新】</strong>金子国交相、日本関係船22隻（大型原油タンカー6隻含む）の通過を発表——残り4隻に大幅減（開戦時45隻から・7/10会見）・米当局者、イランに攻撃停止・全通航路開放の公式声明を要求——通航料も不可（Reuters）・イラン、攻撃は「制度の一部の暴走」と釈明し対話継続を希望・アラグチー外相は本日オマーンでブーサイーディー外相と海峡管理を協議・トルコ外相フィダン氏「今週末にも解決の可能性」・イラン国連大使は「海峡管理は専らイランに属する」と対立姿勢維持・原油はブレント$76台で高止まり（週間+5〜6%）・南ルートは大型船AIS通航が7/7以降ゼロで事実上停止・バンダルアッバスの漁船30隻超が空爆で損壊・封鎖134日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月10日 07:40 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/10 07:40</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>CENTCOM、南部イラン各地（ブシェール・チャバハール・バンダルアッバス・ジャスク等）で追加空爆（7/8夜）・IRGCがクウェート・バーレーン・カタールの米軍拠点にドローン・ミサイルで報復——停戦後初のカタール標的化（7/9）・クウェート国防省「迎撃したが被害で1名負傷」・ガリバフ国会議長「攻撃すれば反撃を受ける」・バーレーン・クウェート・UAE・ヨルダンが非難・ブシェール州で原因不明の爆発複数・原油一時$79台へ急騰後$77前後に落ち着く・日本関係船18隻で変化なし・封鎖133日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月9日 06:59 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/09 06:59</span> — <strong style="color:#fca5a5;">【重大更新】</strong>トランプ大統領、NATO首脳会議（アンカラ）でイランとの停戦は「もう終わったと思っている」と表明・イラン指導部を罵倒（7/8）・アラグチー外相はXで反論・イラン外務省「MOUはホルムズ管理権をイランに戻す」——米は否定（7/8）・原油急騰（ブレント一時$75.18・+4.4%／WTI一時$74.26・+5.3%）・商船三井関係8隻が追加通過し日本関係船は残り18隻に（7/7判明・時事通信）・IMO「船員約6,000人取り残され」・封鎖132日目・ニュース3件更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年7月12日 09:19 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/12 09:19</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>IRGC、キプロス籍コンテナ船GFS Galaxyに警告射撃・着火攻撃——ホルムズ海峡を「次官通達まで閉鎖」と宣言（7/12未明JST）・CENTCOM、今週3度目の対イラン空爆を実施——ヘグセス国防長官「イランは間違った選択をした。今、代償を払う」・停戦は事実上崩壊・オマーンが通航料なしの南北二経路案を提示（南＝自由航行、北＝イラン事前承認制だが無料）——アラグチー外相はオマーン外相と会談も結論持ち帰りで検討中・日本関係船は残り4隻で変化なし（外務省/国交省へ日英クエリで再確認）・原油はブレント週間+5〜6%で$76台高止まり（7/10終値時点）・封鎖135日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月11日 08:38 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/11 08:38</span> — <strong style="color:#fca5a5;">【重大更新】</strong>金子国交相、日本関係船22隻（大型原油タンカー6隻含む）の通過を発表——残り4隻に大幅減（開戦時45隻から・7/10会見）・米当局者、イランに攻撃停止・全通航路開放の公式声明を要求——通航料も不可（Reuters）・イラン、攻撃は「制度の一部の暴走」と釈明し対話継続を希望・アラグチー外相は本日オマーンでブーサイーディー外相と海峡管理を協議・トルコ外相フィダン氏「今週末にも解決の可能性」・イラン国連大使は「海峡管理は専らイランに属する」と対立姿勢維持・原油はブレント$76台で高止まり（週間+5〜6%）・南ルートは大型船AIS通航が7/7以降ゼロで事実上停止・バンダルアッバスの漁船30隻超が空爆で損壊・封鎖134日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年7月10日 07:40 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/07/10 07:40</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>CENTCOM、南部イラン各地（ブシェール・チャバハール・バンダルアッバス・ジャスク等）で追加空爆（7/8夜）・IRGCがクウェート・バーレーン・カタールの米軍拠点にドローン・ミサイルで報復——停戦後初のカタール標的化（7/9）・クウェート国防省「迎撃したが被害で1名負傷」・ガリバフ国会議長「攻撃すれば反撃を受ける」・バーレーン・クウェート・UAE・ヨルダンが非難・ブシェール州で原因不明の爆発複数・原油一時$79台へ急騰後$77前後に落ち着く・日本関係船18隻で変化なし・封鎖133日目・ニュース3件更新・osint更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse への旧3件目（7/9 06:59分）の挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月8日 08:14 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年7月9日 06:59 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/07/09 06:59</span> — <strong style="color:#fca5a5;">【重大更新】</strong>トランプ大統領、NATO首脳会議（アンカラ）でイランとの停戦は「もう終わったと思っている」と表明・イラン指導部を罵倒（7/8）・アラグチー外相はXで反論・イラン外務省「MOUはホルムズ管理権をイランに戻す」——米は否定（7/8）・原油急騰（ブレント一時$75.18・+4.4%／WTI一時$74.26・+5.3%）・商船三井関係8隻が追加通過し日本関係船は残り18隻に（7/7判明・時事通信）・IMO「船員約6,000人取り残され」・封鎖132日目・ニュース3件更新</div>
          <div>📅 <strong>2026年7月8日 08:14 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

> **合計件数チェック**：常時表示3件（7/12・7/11・7/10）＋ log-collapse内（7/9・7/8・7/7・7/6・7/5・7/4・7/3・7/2）＝ 常時3件＋collapse8件 ＝ 合計11件で超過するため、
> Claude Code は log-collapse 最古エントリー（**2026年7月2日 08:23 JST分**・出典リンク①の直前）を削除し、`docs/data/update_log.json` の先頭に追加してください。
> 削除対象の old_str アンカーは以下の通りです（`grep -n "2026年7月2日 08:23"` で行番号を確認のうえ、当該 `<div>` 2行〔日付見出し＋内容〕をまるごと削除）：
> ```html
>           <div>📅 <strong>2026年7月2日 08:23 JST</strong> 更新</div>
>           <div><span style="color:#f87171;">2026/07/02 08:23</span> — <strong style="color:#fca5a5;">【重大更新】</strong>米イラン、ドーハで技術協議を正式実施・バンス副大統領確認（6/30の否定から一転）・イランが海峡管轄権と通行料徴収の国際承認を要求・WTI一時$69割れで2/27以来安値・日本関係船舶は新規発表なく残り約32隻のまま・機雷除去は依然未着手（INTERTANKO）で南北二重ルート継続・封鎖125日目・ニュース2件更新</div>
> ```

---

## 補足：週末オフライン期間中の主要動向（背景メモ・Claude Code適用不要）

- 7/8〜7/9：ハメネイ師国葬関連の動きに続き、CENTCOM追加空爆・IRGCによるクウェート/バーレーン/カタール報復（既存反映済み）
- 7/10：金子国交相会見で日本関係船22隻通過・残り4隻に大幅減（既存反映済み）
- 7/11：オマーンが無料の南北二経路案を提示、アラグチー・ブーサイーディー会談（具体的合意なし）
- 7/11深夜〜7/12未明（JST）：IRGCがGFS Galaxyを攻撃しホルムズ海峡「閉鎖」を宣言、CENTCOMが今週3度目の空爆を実施——**今回の最重要更新点**
- 市場：週末（土日）のため取引は停止中。7/10終値時点でブレントは$76台・週間+5〜6%。週明け（7/13月または7/14火扱い）の市場反応は次回更新で要確認
