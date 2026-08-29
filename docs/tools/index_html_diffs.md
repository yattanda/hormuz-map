# index_html_diffs.md — 2026年8月29日 10:05 JST 更新分
> Claude Code への指示：以下の差分を docs/index.html / docs/data/news_data.json / docs/data/archive_timeline.json に適用してください。
> 変更箇所以外は絶対に触らないこと。push は確認後に指示します。
> 適用前に `git pull --rebase` を実行してください。

---

## ✅ セルフチェック原文（本文執筆前の先貼り・空欄）

本日のセルフチェック項目数：14件

```
[ ] S01 ヘッダー ― 2026年8月29日 10:05 JST・警戒レベル最高の要約更新
[ ] S02 TICKER ― 本日の主要トピックで刷新（S01と重複しない切り口＝JMIC通航データ・ホワイトハウス発言中心）
[ ] S03 速報インシデント ― トグル日付・見出し・本文・リスト2件追加（AL SALAM II被弾の詳細に特化）
[ ] S04 情勢カード3枚 ― 3枚それぞれ異なる切り口（カタール外交／米軍「開通」主張と実態／タンカー・市場・日本船）
[ ] S05 COUNTDOWN ― Phase29・封鎖183日目・新フェーズラベルに更新
[ ] S06 シナリオ確率補足バナー ― 8/29 10:05 JST日付更新（3箇所）・A↑B→C↓D↓
[ ] S07 シナリオ4本 ― A/B/C/D本文をS06と異なる切り口で更新
[ ] S08 シナリオフッター ― 次の焦点5点をS05のdl-noteと重複しない視点で更新
[ ] S08.5 全ルート現況サマリー ― 8/29 10:05 JST更新・航路別の切り口で記述
[ ] S09 30秒カラム ― 3行サマリー＋バッジ5枚を最後に更新
[ ] S10 news_data.json ― latest 4件追加（既存6件中の最古4件をarchiveへ移動）・osint 1件追加・updated日付
[ ] S11 更新ログ ― 3ブロック構成（常時表示3件固定＋log-collapse先頭挿入＋総件数超過対応で重複エントリー1件削除）
[ ] C01 SHIP_CONFIG dateConfirmed ― 8/29 10:05 JST・変化なし（4クエリ再確認）
[ ] JSON-LD dateModified ― 2026-08-29T10:05:00+09:00
```

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（イランのアラグチー外相とオマーンのアルブサイディ外相は25日、テヘランで会談し、ホルムズ海峡に「共同の暫定航行回廊」を設置し機雷除去を共同実施する枠組みで合意したと発表——恒久的な航路と海峡の将来管理については今後30〜60日間、技術協議を継続するとしている／トランプ大統領は同日、米海軍がホルムズ海峡国際水域の機雷を全て除去・爆破したとSNSに投稿し、新たな敷設船は即時破壊すると警告したが、米政府・軍による裏付け発表はない／イランのガリババディ副外相は26日、暫定合意後も海峡は開放されていないとしてトランプ氏の主張を否定し、南側回廊（オマーン領海経由・国連承認航路）は新枠組みの下で閉鎖される見通しと説明した／トランプ氏は今月17日にも「オマーンが邪魔なら地獄まで爆撃する」と威嚇しており、米国を関与させない二国間合意に米側がどう反応するかは不透明／24日夜にはオマーン東岸沖でタンカー1隻が正体不明の飛翔体を受け機関が損傷、UKMTOが確認（乗員無事）／原油はブレントが一時87ドルを割り込み週間約8%安、WTIも81ドル近辺まで下落／中国外務省は対中制裁計画に「中国・イラン協力は妨害を受けるべきでない」と改めて反発／日本関係船は残り4隻で変化なし／封鎖181日目）</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🚨 警戒レベル：最高（カタールのシェイク・モハンマド首相兼外相は27日、開戦後初めてテヘランを訪問し、アラグチー外相・ペゼシュキアン大統領・ガリバフ国会議長・最高国家安全保障会議のレザイー事務局長と相次いで会談、国際法に基づく航行の自由と近隣国の主権尊重の重要性を強調した／同氏の働きかけを受け、レザイー事務局長は通常の船舶通航を回復するための「条件リスト」を策定中だと表明——イラン・オマーンは一部オマーン領海・一部イラン領海を通る中央航路で合意しており、米国が条件を満たせば同航路が使用可能になるとした／米中央軍のクーパー司令官はSNS動画で、数カ月前にIRGCが敷設した機雷は除去済みとした上で「今日、国際航路は開通し勢いを増している」と主張、最近数カ月で商船約1,500隻・原油約7億5,000万バレル分の通過を支援したと述べたが、船舶追跡データでは通航量は依然戦前比5〜15％にとどまる／トランプ大統領は26日、「MISSION ACCOMPLISHED 2026」とSNS投稿し戦争の事実上の勝利宣言を行ったが、その直後の25日17時30分（UTC）、ホルムズ海峡を東行中のタンカー「AL SALAM II」が飛翔体を受け被弾したとJMICが確認（乗員無事・消火済み）／ホワイトハウスのレビット報道官は27日、米イラン間の交渉は現時点で行われていないと明言／原油はブレントが4営業日続落ののち87ドル台後半で下げ止まり（28日時点87.58ドル）／イラン軍は損傷した兵器体系をすべて「再建済み」と発表／日本関係船は残り4隻で変化なし／封鎖183日目）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-date">📅2026年8月27日 10:00 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-date">📅2026年8月29日 10:05 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年8月27日 10:00 JST） -->` コメント直後のテキスト
**切り口：** S01の外交サマリーとは重複させず、通航データ・米政府発言・軍事情勢の数値面を中心に構成

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年8月27日 10:00 JST） -->
      🕊️【暫定合意】イラン・オマーン、ホルムズ海峡に「共同暫定航行回廊」設置＋機雷除去で合意——恒久ルートは30〜60日以内に協議へ（テヘラン、8/25）｜💣 トランプ氏「機雷は全て除去・爆破」とSNS投稿、新規敷設船は即時破壊と警告——米政府の公式裏付けなし（8/25）｜🇮🇷 イラン副外相ガリババディ氏「海峡は開放されていない」とトランプ氏主張を否定、南側回廊は新枠組みで閉鎖の見通し（8/26）｜⚓ オマーン東岸沖でタンカー1隻が飛翔体で被弾・機関停止、UKMTO確認（乗員無事・8/24夜）｜🛢️ ブレント原油が一時87ドル割れ・週間下落率約8%——通航協議進展を好感（8/25）｜🇨🇳 中国外務省、対中制裁計画に「中国・イラン協力は妨害されるべきでない」と改めて反発｜🇯🇵 日本関係船は残り4隻で変化なし｜封鎖181日目
    </span>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年8月29日 10:05 JST） -->
      🇶🇦【カタール仲介】シェイク・モハンマド首相が開戦後初のテヘラン訪問——イランは通航再開の「条件リスト」策定に合意（8/27）｜🎖️ 米中央軍クーパー司令官「国際航路は開通・勢いを増す」——直近で商船1,500隻・原油7.5億バレル分の通過を支援と主張（8/27）｜📊 JMIC：8/25〜26のホルムズ通航は米軍支援下37隻にとどまる——2025年平均は1日約138隻｜🏛️ ホワイトハウスのレビット報道官「米イラン交渉は現時点で行われていない」（8/27）｜⚓ タンカー「AL SALAM II」が25日17:30 UTC被弾——トランプ氏の「Mission Accomplished」投稿直後にJMICが確認｜🛢️ ブレント原油は4営業日続落後、87ドル台後半で下げ止まり（8/28時点87.58ドル）｜🇯🇵 日本関係船は残り4隻で変化なし｜封鎖183日目
    </span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

**対象：** `<!-- 速報インシデント トグルボタン -->` 内
**切り口：** AL SALAM II被弾の詳細（JMICによる特定情報）に特化し、S01・S02の外交面とは重複させない

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/27 10:00 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 8/29 10:05 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### トグル見出し

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">イラン・オマーンがホルムズ海峡暫定回廊で合意——トランプ氏「機雷全除去」主張にイランは海峡開放を否定</strong>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">タンカー「AL SALAM II」がホルムズ海峡で被弾——JMICが確認、カタール仲介でイランは条件リスト策定へ</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の `<strong>` タグを置き換え）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/27 10:00 速報】イランのアラグチー外相とオマーンのアルブサイディ外相は25日、テヘランで会談し、ホルムズ海峡に「共同の暫定航行回廊」を設置し機雷除去の共同事業を実施する枠組みで合意したと共同声明で発表した（Al Jazeera/Reuters、8/25）｜イラン副外相ガリババディ氏は26日、国営テレビに対し、湾内向け航路は全面的にイラン領海を通過し、湾外向け航路はイラン・オマーン両領海を通過する形になると説明——両国は今後30〜60日間、恒久的で持続可能な新ルートについて協議を続けるとした（AP）｜同氏はまた、南側回廊（オマーン領海経由・国連承認TSS）は新枠組みの下で閉鎖される見通しだと述べたが、オマーン側の声明にこの閉鎖への言及はなく、整合性は未確認｜トランプ大統領は25日、SNS投稿で「米海軍からホルムズ海峡国際水域内の機雷を全て除去・爆破したとの報告を受けた」とし、新たに機雷を敷設する船舶・ボートは即時かつ組織的に破壊すると警告——米宇宙軍による監視継続も強調したが、米政府・軍からこれを裏付ける公式発表はない（CNN/BBC、8/25）｜イラン側はこの主張を「虚偽」として全面否定（読売新聞、8/26）｜Al Jazeeraの分析記事は、機雷除去が主要航路で信頼できる可能性はあるとしつつ、監視外の「漂流機雷」が残る可能性やイランが新たに機雷を敷設する能力自体は保持している点を指摘し、機雷除去だけでは商業航行の「安全」を意味しないと論じた（8/26）｜トランプ氏は今月17日にも今回の枠組み交渉を主導するオマーンに対し「邪魔をするなら地獄まで爆撃する」と2度目の軍事威嚇を行っており、米国を関与させない形での二国間合意に米側がどう反応するかが今後の焦点となる｜24日夜（協定世界時）にはオマーン東岸沖でタンカー1隻が正体不明の飛翔体を受け機関が停止、英UKMTOが被害を確認したが乗員は全員無事、犯行声明はない（AP、8/25）｜中国外務省の林剣副報道官は、米財務省が計画する対中制裁拡大について「中国とイランの協力は妨害・干渉を受けるべきではない」と改めて反発（AP、8/25）｜日本関係船は残り4隻で変化なし｜封鎖181日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【8/29 10:05 速報】英海事機関JMICは、25日17時30分（協定世界時）にホルムズ海峡を東行中だったタンカー「AL SALAM II」が飛翔体を受け喫水線上に小さな穴と火災が発生したと特定——火は乗組員により消火され乗員は全員無事、環境影響の報告もなく、ジャジラト・タワックル北西約0.8海里で錨泊し曳船支援を待つ状態（gCaptain、8/28）｜この被弾は、トランプ大統領が「MISSION ACCOMPLISHED 2026」とSNS投稿し事実上の勝利宣言を行った直後に判明したもので、機雷除去主張と現場のリスクとの落差を改めて示した｜JMICによれば、8/25〜26の2日間で米軍支援下の通航はわずか37隻にとどまり、2025年の平均日量約138隻を大きく下回る水準が続く｜米中央軍のクーパー司令官はSNS動画で「国際航路は開通し勢いを増している」と主張し、直近数カ月で商船約1,500隻・原油約7億5,000万バレル分の通過を支援したと述べたが、船舶追跡データでは実際の通航量は依然戦前比5〜15％にとどまる｜カタールのシェイク・モハンマド首相兼外相は27日、開戦後初めてテヘランを訪問し、アラグチー外相・ペゼシュキアン大統領・最高国家安全保障会議のレザイー事務局長らと会談——航行の自由の尊重を強く求めた｜これを受けレザイー事務局長は、通常航行の再開に向けた条件リストを策定中だと表明し、米国が条件を満たせば一部オマーン領海・一部イラン領海を通る中央航路が使用可能になるとした（Reuters、8/27）｜ホワイトハウスのレビット報道官は27日、米イラン間の交渉は現時点で行われていないと明言｜IMOによれば開戦以来の事案は累計70件・船員死者19人に達した｜日本関係船は残り4隻で変化なし｜封鎖183日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に2件追加）

**既存リストの `<ul id="incident-list" ...>` の直後（1件目の `<li>` の直前）に以下を挿入：**

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇮🇷🇴🇲 8/25〜26 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">⚓ 8/25 17:30 UTC</span>
  <span style="color:#e2e8f0;"> 英海事機関JMICは、ホルムズ海峡を東行中だったタンカー「AL SALAM II」が飛翔体を受け被弾したと特定。喫水線上に小さな穴が開き火災が発生したが乗組員が消火し、乗員は全員無事。ジャジラト・タワックル北西約0.8海里に錨泊し曳船支援を待っている（gCaptain、8/28）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#fbbf24;font-weight:700;">🇶🇦 8/27 JST</span>
  <span style="color:#e2e8f0;"> カタールのシェイク・モハンマド首相兼外相が開戦後初めてテヘランを訪問し、アラグチー外相・ペゼシュキアン大統領・ガリバフ国会議長・最高国家安全保障会議のレザイー事務局長と相次いで会談。同首相の働きかけを受け、レザイー事務局長は通常の船舶通航を回復するための条件リストを策定中だと表明した（Reuters、8/27）。</span>
</li>
<li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.07);">
  <span style="color:#f87171;font-weight:700;">🇮🇷🇴🇲 8/25〜26 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

**対象：** `<!-- SITUATION CARDS -->` 直後の `sit-grid`

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- カード① 外交・暫定合意 -->
  <div class="sit-card danger">
    <div class="s-icon">🇮🇷🇴🇲</div>
        <div class="s-title">🇮🇷🇴🇲 イラン・オマーン、ホルムズ海峡暫定回廊で合意——恒久ルートは30〜60日以内に協議へ</div>
        <div class="s-body">イランのアラグチー外相とオマーンのアルブサイディ外相は25日、テヘランで会談し、ホルムズ海峡に「共同の暫定航行回廊」を設置し機雷除去を共同で行う枠組みで合意したと共同声明で発表した。イラン副外相ガリババディ氏は国営テレビに対し、湾内向け航路は全面的にイラン領海を、湾外向け航路はイラン・オマーン両領海を通過する構成になると説明し、南側回廊（オマーン領海経由の国連承認TSS）は新枠組みの下で閉鎖される見通しだと述べた。両国は恒久的な新ルートと海峡の将来管理について、今後30〜60日間の技術協議を継続するとしている。米国はこの協議に関与しておらず、トランプ大統領は今月、交渉を仲介するオマーンに「邪魔をするなら爆撃する」と警告しており、米国抜きの二国間合意を米側が受け入れるかは不透明。</div>
        <div class="s-src">出典: Al Jazeera / Reuters / AP（8/25〜26 JST 更新）</div>
  </div>

  <!-- カード② 機雷除去論争 -->
  <div class="sit-card warning">
    <div class="s-icon">💣</div>
        <div class="s-title">💣 トランプ氏「機雷は全て除去」——イランは否定、専門家は「安全な航行の回復とは別問題」</div>
        <div class="s-body">トランプ大統領は25日、米海軍がホルムズ海峡国際水域内の機雷を全て除去・爆破したとSNS投稿し、新たな機雷敷設船は即時破壊すると警告した。米国防当局からこれを裏付ける公式発表はない。イラン副外相ガリババディ氏は26日、イラン・オマーンの暫定合意にもかかわらず海峡は開放されていないとし、トランプ氏の除去主張も事実上否定した。Al Jazeeraの分析記事は、米側の主要航路における機雷除去の評価自体は信頼できる可能性があるとしつつ、監視網の外にある「漂流機雷」が残存する可能性や、イランが新たな機雷を敷設する能力を保持し続けている点を指摘し、機雷除去だけでは商業船舶が戦前水準の航行を安全に再開できることを意味しないと論じた。</div>
        <div class="s-src">出典: CNN / BBC / Al Jazeera（8/25〜26 JST 更新）</div>
  </div>

  <!-- カード③ 海上輸送・市場・日本関係船 -->
  <div class="sit-card info">
    <div class="s-icon">🚢</div>
        <div class="s-title">🚢 オマーン沖でタンカー被弾・原油急落——南側航路の緊張続く中、日本関係船は4隻で変化なし</div>
        <div class="s-body">英海運当局UKMTOは、24日夜（協定世界時）にオマーン東岸沖でタンカー1隻が正体不明の飛翔体を受け機関が停止したと発表した。乗員は全員無事で環境影響の報告もないが、犯行声明はなく、南側航路を含む海峡周辺の危険性が依然として続いていることを示す事案となった。原油市場では、イラン・オマーンの通航協議進展を好感し、ブレント原油が25日に一時1バレル＝87ドルを割り込み週間で約8%下落、米国産WTIも81ドル近辺まで下げた。日本関係船については、外務省・国土交通省への日英4クエリ調査で新規発表がないことを再確認し、ペルシャ湾内に残る隻数は引き続き4隻のまま変化はない。</div>
        <div class="s-src">出典: UKMTO / Bloomberg / 外務省・国土交通省（8/24〜26 JST 更新）</div>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
<!-- カード① カタール外交・条件リスト -->
  <div class="sit-card danger">
    <div class="s-icon">🇶🇦</div>
        <div class="s-title">🇶🇦 カタール首相、開戦後初のテヘラン訪問——イランは通航再開の「条件リスト」策定へ</div>
        <div class="s-body">カタールのシェイク・モハンマド首相兼外相は27日、開戦以来初めてテヘランを訪問し、アラグチー外相・ペゼシュキアン大統領・ガリバフ国会議長・最高国家安全保障会議のレザイー事務局長と相次いで会談した。同首相はX（旧Twitter）で、国際法に基づく航行の自由と近隣国の主権を尊重することの重要性を強調したと明らかにした。これを受けレザイー事務局長は、通常の船舶通航を回復するための条件リストを策定中だと表明。イラン・オマーンは一部オマーン領海・一部イラン領海を通る中央航路で合意しており、米国が条件を満たせば同航路が使用可能になると説明したが、従来の6条件（封鎖解除・賠償・制裁解除等）を修正する意向かは依然不明。</div>
        <div class="s-src">出典: Reuters / Qatar News Agency（8/27〜28 JST 更新）</div>
  </div>

  <!-- カード② 米軍「開通」主張と実態のギャップ -->
  <div class="sit-card warning">
    <div class="s-icon">🎖️</div>
        <div class="s-title">🎖️ 米中央軍「国際航路は開通・勢いを増す」——実際の通航データは戦前比5〜15％にとどまる</div>
        <div class="s-body">米中央軍のブラッド・クーパー司令官はSNS動画メッセージで、数カ月前にIRGCが敷設した機雷は既に除去済みとした上で「今日、国際航路は開通しており、勢いが増している」と述べ、直近数カ月で商船約1,500隻・原油約7億5,000万バレル分の通過を米軍が支援したと発表した。トランプ大統領も26日、「MISSION ACCOMPLISHED 2026」とSNSに投稿し事実上の勝利を宣言した。一方、JMICのデータでは8/25〜26の米軍支援下の通航はわずか37隻にとどまり、2025年の1日平均約138隻を大きく下回る。ホワイトハウスのレビット報道官は27日、米イラン間の交渉は現時点で行われていないと明言しており、「開通」の発表と現場の実態には依然として乖離が残る。</div>
        <div class="s-src">出典: 米中央軍（CENTCOM）/ ホワイトハウス（8/26〜27 JST 更新）</div>
  </div>

  <!-- カード③ タンカー被弾・市場・日本関係船 -->
  <div class="sit-card info">
    <div class="s-icon">⚓</div>
        <div class="s-title">⚓ タンカー「AL SALAM II」被弾をJMICが確認——原油は下げ止まり、日本関係船は4隻で変化なし</div>
        <div class="s-body">英海事機関JMICは、25日17時30分（協定世界時）にホルムズ海峡を東行中だったタンカー「AL SALAM II」が飛翔体を受け被弾したと特定した。喫水線上に小さな穴が開き火災が発生したが乗組員により消火され、乗員は全員無事。ジャジラト・タワックル北西約0.8海里に錨泊し曳船支援を待つ状態にある。原油市場では、ブレント原油が4営業日続落したのち28日時点で87ドル台後半（87.58ドル、前日比-1.08%）で下げ止まった。イラン軍は国営テレビで、損傷した兵器体系をすべて「再建済み」と発表している。日本関係船については、外務省・国土交通省への日英4クエリ調査で引き続き新規発表がないことを確認し、ペルシャ湾内に残る隻数は4隻のまま変化はない。</div>
        <div class="s-src">出典: JMIC（gCaptain）/ CNBC / 外務省・国土交通省（8/28〜29 JST 更新）</div>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

**対象：** `<!-- COUNTDOWN -->` 内の `.dl-label` と `.dl-note`

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 28「イラン・オマーンがホルムズ海峡暫定回廊で合意——トランプ氏『機雷全除去』主張にイランは海峡開放を否定」——封鎖181日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 29「カタール仲介でイランが通航条件リスト策定へ——米中央軍『開通宣言』の裏でタンカー被弾」——封鎖183日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="dl-note">
        🌐 <strong>イラン・オマーンの暫定航行回廊合意は、開戦後初めて「海峡管理の具体的な枠組み」が両沿岸国間で言語化された点で外交的な一歩である一方、米国を関与させない二国間の取り決めであるため、トランプ政権がこれを追認するかどうかという新たな不確実性を生んでいる——トランプ氏の「機雷全除去」発言とイランの真っ向からの否定は、同じ事象について当事者間で全く異なる現実認識が併存していることを改めて示した／原油市場は協議進展を好感して下落したが、南側航路でのタンカー被弾は海峡周辺のリスクが消えていないことを裏付けている／日本関係船は残り4隻で変化なし——封鎖181日目</strong>
        <br><span style="color:#fde68a;">⚡ 次の24〜48時間の焦点：①米国がイラン・オマーンの二国間合意をどう評価し対応するか ②南側回廊（国連承認TSS）の閉鎖が実際に実行に移されるか ③機雷除去の実態について第三者（IMO・保険業界等）の独立確認が得られるか ④オマーン沖タンカー被弾の犯行主体特定と再発の有無 ⑤30〜60日間の技術協議の進捗と恒久ルート合意の実現可能性</span>
        <br><span style="color:#fca5a5;">⏳ 外交的前進と現場のリスク残存が併存する局面——「合意はしたが海峡は開いていない」という当事者双方の発言の落差が今後の焦点</span>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="dl-note">
        🌐 <strong>カタール首相のテヘラン訪問を経て、イランが通航再開の「条件リスト」策定に動いたことは、これまでの硬直した六条件からの一歩前進とも読める一方、米中央軍が「国際航路は開通・勢いを増している」と発表した同じ時間軸でタンカー「AL SALAM II」が被弾したことは、公式発表と現場のリスクの間に依然として大きな溝があることを示している——ホワイトハウスが「交渉は行われていない」と明言する中、仲介外交と軍の楽観的発表、そして現場の被弾事案が三者三様に異なる現実を語っている構図は、これまでの膠着とは質の異なる「言葉と実態の乖離」の局面と言える／日本関係船は残り4隻で変化なし——封鎖183日目</strong>
        <br><span style="color:#fde68a;">⚡ 次の24〜48時間の焦点：①イランが策定中の条件リストの具体的内容と提示時期 ②米中央軍の「1,500隻・7.5億バレル」という支援実績の第三者検証可能性 ③AL SALAM II被弾の実行主体特定と類似事案の再発有無 ④ホワイトハウスの「交渉なし」表明とカタール・パキスタンの並行仲介の整合性 ⑤中央航路（イラン・オマーン合意ベース）の座標・発効時期の公表有無</span>
        <br><span style="color:#fca5a5;">⏳ 外交的な糸口と軍の楽観的発表、現場のリスクが同時進行する局面——どの発表を基準に情勢を評価すべきか、情報の信頼性そのものが焦点になりつつある</span>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

**対象：** `<!-- シナリオ確率更新補足 -->` ブロック（日付3箇所）

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月27日 10:00 JST 更新</span><br>
  📊 <strong>イラン・オマーンがホルムズ海峡に共同暫定回廊を設置し機雷除去を共同実施する枠組みで合意した一方、トランプ大統領の「機雷全除去」主張をイランが否定し、海峡が実際に開放されたわけではないと強調——外交的な前進と、当事者間の現実認識の乖離が同時に表面化している：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#4ade80;">↑</span> — 米国が関与しない形とはいえ、イラン・オマーン間で初めて具体的な航路管理の枠組みが文書化されたことは、既存のMOU路線とは別に交渉の糸口が生まれたことを意味する<br>
  🅑 膠着継続 <span style="color:#94a3b8;">→</span> — 暫定合意はまだ「海峡開放」を意味せず、南側回廊の閉鎖観測もあり、実際の通航量が大きく変わる保証はない<br>
  🅒 MOU形骸化・機能不全 <span style="color:#4ade80;">↓</span> — イラン・オマーン間の合意進展は、既存の米・イラン枠組みが完全に機能停止する事態をやや遠ざけている<br>
  🅓 全面対決・無期限封鎖 <span style="color:#4ade80;">↓</span> — 機雷除去や技術協議の進展は軍事エスカレーションの当面のリスクを幾分和らげているが、米国排除の合意にトランプ政権がどう反応するかは読み切れない<br>
  <strong style="color:#f87171;">米国を関与させない形での二国間合意という新しい変数が加わったことで、今後はトランプ政権の反応と南側回廊閉鎖の実行有無が最大の分岐点となる（A↑ B→ C↓ D↓）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月27日 10:00 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#f87171;">📊 2026年8月29日 10:05 JST 更新</span><br>
  📊 <strong>カタールの仲介でイランが通航再開の条件リスト策定に合意した一方、米中央軍の「開通・勢いを増す」発表の直後にタンカーが被弾——外交チャネルの多層化と、発表と現場実態の乖離が同時進行している：</strong><br>
  🅐 段階的MOU履行成功 <span style="color:#4ade80;">↑</span> — カタールという新たな仲介者が条件リスト策定という具体的な行動をイランから引き出したことは、外交プロセスに新たな推進力を与えうる<br>
  🅑 膠着継続 <span style="color:#94a3b8;">→</span> — 条件リストの中身が従来の六条件と実質同じであれば、米国が受け入れる可能性は低く、膠着が続く公算が大きい<br>
  🅒 MOU形骸化・機能不全 <span style="color:#4ade80;">↓</span> — カタール・パキスタンの並行仲介と中央航路の座標合意は、外交チャネルが完全に途絶える事態をやや遠ざけている<br>
  🅓 全面対決・無期限封鎖 <span style="color:#4ade80;">↓</span> — 米中央軍の「開通」発表と機雷除去の継続は軍事的緊張の当面の高まりを抑制する材料だが、タンカー被弾はリスクの残存も示す<br>
  <strong style="color:#f87171;">カタール仲介による条件リスト策定という新たな変数と、米軍発表と現場実態の乖離という二つの軸が今後の分岐点となる（A↑ B→ C↓ D↓）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年8月29日 10:05 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本

**対象：** `.sc-card` 内の `.sc-body`（S06とは異なる切り口＝各シナリオの具体的な波及分析）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>イラン・オマーンが暫定航行回廊と機雷除去の枠組みで合意したことは、既存の米・イラン間MOU路線とは別の経路で「海峡管理の具体化」が進み始めたことを示す。ただし米国が交渉に加わっていない以上、これが正式なMOU履行の再開に直結するかは不透明で、トランプ政権の出方次第で評価は大きく変わりうる。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>カタール首相が開戦後初めてテヘランを直接訪問し、イラン最高国家安全保障会議のレザイー事務局長から条件リスト策定という具体的な言質を引き出したことは、パキスタンに続き複数の仲介チャネルが同時に機能し始めていることを意味する。条件リストの内容次第では、米国側の反応も含めMOU路線再建への糸口となり得る。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>トランプ氏が「機雷全除去」を主張する一方でイランが海峡開放を否定するという、事実認識そのものが対立したまま推移する構図は、これまでの膠着とは異なる新しい形の停滞と言える。実際の通航量に大きな変化がない限り、外交上の言葉の応酬が続く「膠着継続」の枠組みは維持されやすい。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>米中央軍が商船1,500隻・原油7.5億バレル分の支援実績を発表する一方、JMICのデータでは直近2日間の通航がわずか37隻にとどまるという数字上の落差は、公式発表と現場実態のどちらを基準に情勢を評価すべきかという新たな不透明要因を生んでいる。ホワイトハウスが交渉不在を明言している以上、この「発表と実態の乖離」を抱えたままの膠着が続きやすい。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>南側回廊（国連承認TSS）が新枠組みの下で閉鎖されるとの観測は、イラン・オマーン主導の航路管理が既存の国際的な通航ルールに取って代わる可能性を示唆する。もっとも、この閉鎖はオマーン側の声明では確認されておらず、実際に制度化が進むかは今後の技術協議の帰結次第である。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>イラン・オマーンが合意した中央航路（一部オマーン領海・一部イラン領海）は、既存の国連承認TSSに代わる新たな管理体制の萌芽とも解釈できる。ただし利用開始には米国側が条件リストを受け入れる必要があり、イラン軍が兵器体系の「再建済み」を強調していることも踏まえると、制度化の実現は依然として交渉の帰結次第である。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="sc-body">
        <p>軍事的な緊張そのものは、機雷除去や技術協議の進展によって当面は和らいでいるように見える。ただしオマーン沖でのタンカー被弾は攻撃リスクが消えていないことを示しており、米国を排除した合意にトランプ政権が反発すれば、状況が再び悪化する可能性は残る。</p>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="sc-body">
        <p>米中央軍による機雷除去の継続と「開通」発表は軍事エスカレーションの当面のリスクを抑える材料である一方、AL SALAM II被弾が示すように攻撃そのものは止んでいない。イラン軍の「兵器再建済み」発表と合わせ、条件リストが米国に拒否された場合には緊張が再燃する可能性が残る。</p>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオ フッター（次の焦点5つ）

**対象：** `<!-- シナリオ フッター -->`（S05のdl-noteとは異なる視点＝仲介の収斂・検証可能性を中心に構成）

<!-- APPLY:START -->
<!-- OLD:START -->
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米国がイラン・オマーンの二国間合意にどう対応するか——追認か、対抗措置か</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">南側回廊（国連承認TSS）閉鎖が実際に発効し、通航実務にどう影響するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">機雷除去の第三者検証——IMO・保険業界・船社が独自に安全宣言を出すか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">30〜60日間の技術協議で恒久ルート合意に至るか、それとも再び停滞するか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">オマーン沖タンカー被弾の再発防止——UKMTO・JMICの警戒水準に変化はあるか</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月27日 10:00 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">イランが策定中の「条件リスト」の具体的内容と提示時期——従来の六条件から実質的に変化があるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">ホワイトハウスの「交渉なし」表明が、カタール・パキスタンの並行仲介を経てどう転じるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">米中央軍が発表した「商船1,500隻・原油7.5億バレル」の実績を第三者が検証できるか</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">AL SALAM II被弾の実行主体特定——南側・新設回廊双方での再発有無</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">中央航路（イラン・オマーン合意ベース）の座標・発効時期の正式公表があるか</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年8月29日 10:05 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

**対象：** `sec-title`（航路別の切り口で記述、S01〜S04・S07とは重複しない構成）

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月27日 10:00 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">イラン・オマーンの暫定回廊合意により、今後の航路構成に変化が見込まれる。【新設回廊（イラン・オマーン合意ベース）】湾内向け航路は全面的にイラン領海、湾外向け航路はイラン・オマーン両領海を通過する構成となる見通し（イラン副外相ガリババディ氏、8/26）——ただし発効時期・具体的座標は未公表。【南側回廊（オマーン沿岸・国連承認TSS）】新枠組みの下で閉鎖される可能性がイラン側から示唆されているが、オマーン側の声明には言及がなく整合性は未確認。前週まで米軍護衛下で1日15〜20隻規模の通航が報告されていた主要ルート。【北側航路（イラン指定）】通航料徴収の制度化は依然実現せず、利用は低調。【市場】ブレント原油は25日に一時87ドルを割り込み週間約8%安——通航協議進展を好感。【インシデント】24日夜、オマーン東岸沖でタンカー1隻が飛翔体被弾・機関停止（UKMTO確認・乗員無事）。【UKMTO 警戒水準】Substantial（継続）。【ダーク・トラフィック】クウェート・サウジ・UAEはVLCCチャーターとシップ・トゥ・シップ移送でトランスポンダーオフの「不可視」輸送を継続。🇯🇵 日本関係船舶：残り4隻で変化なし（8/27 10:00 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年8月29日 10:05 JST 更新）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">【中央航路（イラン・オマーン合意ベース）】一部オマーン領海・一部イラン領海を通過する構成でイラン・オマーン間の合意が確認された（レザイー最高国家安全保障会議事務局長、8/27）——米国が条件を満たせば利用可能になるとされるが、発効時期・具体的座標は依然未公表。【南側航路（オマーン沿岸・国連承認TSS）】米中央軍は機雷除去済み・「開通」と主張し商船1,500隻分の支援実績を発表したが、8/25にはこのルート付近でタンカー「AL SALAM II」が被弾しておりリスクは残存。【北側航路（イラン指定）】通航料徴収の制度化は依然実現せず、利用は低調のまま。【通航データ】JMICによれば8/25〜26の米軍支援下通航はわずか37隻——2025年平均の1日約138隻を大幅に下回る水準が続く。【市場】ブレント原油は4営業日続落ののち87ドル台後半で下げ止まり（8/28時点87.58ドル）。【UKMTO 警戒水準】Substantial（継続）。【ダーク・トラフィック】クウェート・サウジ・UAEはVLCCチャーターとシップ・トゥ・シップ移送でトランスポンダーオフの「不可視」輸送を継続。🇯🇵 日本関係船舶：残り4隻で変化なし（8/29 10:05 JST再確認・外務省/国交省へ日英4クエリで新規発表なしを確認）。</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ5枚）

**対象：** `<!-- 3行サマリー -->` と直後のステータスバッジ（他の全セクションの総括として最後に作成・重複最小化）

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇮🇷🇴🇲 イラン・オマーンがホルムズ海峡の暫定通航回廊で合意——機雷除去も共同実施へ。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
💣 トランプ氏「機雷全除去」を主張するもイランは海峡開放を否定、オマーン沖でタンカー1隻が被弾。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🛢️ 原油は週間8%安に反落——米国が二国間合意にどう対応するかが焦点、封鎖181日目。
</span>
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🇶🇦 カタール首相が開戦後初のテヘラン訪問——イランは通航再開の「条件リスト」策定に合意。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🎖️ 米中央軍「国際航路は開通・勢いを増す」と主張するも、その直後にタンカーAL SALAM IIが被弾。
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🏛️ ホワイトハウス「交渉は行われていない」と明言——発表と実態の乖離が焦点、封鎖183日目。
</span>
  </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ5枚

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇮🇷🇴🇲暫定航行回廊で合意</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💣機雷「全除去」主張にイラン反論</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚓オマーン沖でタンカー被弾</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🛢️原油週間8%安</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇶🇦カタール首相テヘラン訪問</span>
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#fca5a5;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📋イラン条件リスト策定へ</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚓AL SALAM II被弾・JMIC確認</span>
<span style="display:inline-block;background:rgba(148,163,184,0.15);border:1px solid rgba(148,163,184,0.3);color:#cbd5e1;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🎖️米軍「開通」主張と実態乖離</span>
<span style="display:inline-block;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵日本関係船残り4隻(変化なし)</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新メモ

**方法：** `docs/data/news_data.json` の `latest` 配列の先頭に以下4件を追加し、既存6件のうち最も古い4件を `archive` の先頭バッチへ移動してください（結果として latest は新4件＋直近2件の計6件）。追加後、最新1件のみ `isLatest: true`、他はすべて `false` に設定してください。`osint` 配列には以下1件を先頭に追加し（append-only・既存配列は保持）、既存の先頭項目の `isLatest` を `false` に変更してください。`updated` フィールドを更新し、`staleNotice` は空文字のままとしてください。

### `latest` 新規4件（新しい順）

```json
{
  "id": "latest-qatar-pm-tehran-visit-0827",
  "title": "カタール首相がテヘラン訪問——開戦後初の高官級訪問、航行の自由の尊重を要求",
  "body": "カタールのシェイク・モハンマド首相兼外相が27日、開戦後初めてテヘランを訪問し、アラグチー外相・ペゼシュキアン大統領・ガリバフ国会議長・最高国家安全保障会議のレザイー事務局長と相次いで会談した。同首相は国際法に基づく航行の自由と近隣国の主権尊重の重要性を強調し、対話継続を呼びかけた。",
  "sourceLabel": "Reuters（Arab News）",
  "date": "2026年8月27日（現地）/ 2026年8月28日 JST",
  "label": "🇶🇦 外交",
  "url": "https://www.arabnews.jp/article/middle-east/article_185141/",
  "isLatest": true
},
{
  "id": "latest-iran-conditions-list-0827",
  "title": "イラン、通航再開に向けた「条件リスト」の策定に合意——カタールの働きかけ受け",
  "body": "カタール高官の要請を受け、イラン最高国家安全保障会議のレザイー事務局長は、通常の船舶通航を回復するための条件リストを準備中だと表明。イラン・オマーンは一部オマーン領海・一部イラン領海を通る中央航路で合意しており、米国が条件を満たせば同航路が使用可能になるとした。従来の6条件を修正する意向かは不明。",
  "sourceLabel": "Reuters（Arab News）",
  "date": "2026年8月27日（現地）/ 2026年8月28日 JST",
  "label": "🇮🇷 外交",
  "url": "https://www.arabnews.jp/article/middle-east/article_185141/",
  "isLatest": false
},
{
  "id": "latest-al-salam-ii-attack-0825",
  "title": "タンカー「AL SALAM II」被弾をJMICが確認——トランプ氏「Mission Accomplished」投稿の直後",
  "body": "JMICは25日17時30分（UTC）、ホルムズ海峡を東行中のタンカー「AL SALAM II」が飛翔体を受け喫水線上に小孔と火災が発生したと発表。火は乗組員により消火され乗員は全員無事。ジャジラト・タワックル北西で錨泊し曳船支援を待つ。同日、トランプ大統領は「MISSION ACCOMPLISHED 2026」とSNS投稿していた。",
  "sourceLabel": "gCaptain",
  "date": "2026年8月25日（現地）/ 2026年8月28日 JST",
  "label": "⚓ インシデント",
  "url": "https://gcaptain.com/tanker-hit-in-strait-of-hormuz-as-trump-declares-mission-accomplished-in-iran/",
  "isLatest": false
},
{
  "id": "latest-centcom-cooper-open-route-0827",
  "title": "米中央軍司令官「国際航路は開通・勢いを増している」——実際の通航は依然低水準",
  "body": "米中央軍のクーパー司令官はSNS動画で、数カ月前にIRGCが敷設した機雷を除去済みとした上で「今日、国際航路は開通し勢いを増している」と主張、最近数カ月で約1,500隻・原油約7億5,000万バレル分の商船通過を支援したと述べた。船舶追跡データでは通航量は依然戦前比5〜15％にとどまり、IMOによれば開戦以来70件の事案・船員19人死亡が発生している。",
  "sourceLabel": "Arab News（Reuters）",
  "date": "2026年8月27日 / 2026年8月28日 JST",
  "label": "🎖️ 米軍発表",
  "url": "https://www.arabnews.jp/article/middle-east/article_185130/",
  "isLatest": false
}
```

### `osint` 新規1件（先頭に追加）

```json
{
  "id": "osint-iran-qatar-hormuz-talks-0827",
  "titleJa": "【Al Jazeera】イラン・カタール、ホルムズ海峡巡り協議——対話再開への国際的期待",
  "titleEn": "Iran, Qatar hold Hormuz talks amid intl hopes dialogue with US will resume",
  "title": "【Al Jazeera】イラン・カタール、ホルムズ海峡巡り協議——対話再開への国際的期待",
  "country": "カタール/イラン",
  "media": "Al Jazeera",
  "source": "Al Jazeera",
  "date": "2026年8月27日（現地）/ 2026年8月27日 JST",
  "summary": "Al Jazeeraは、カタール首相のテヘラン訪問と、暫定海上回廊・機雷除去共同事業を含む枠組みを巡る協議を詳報。イラン最高国家安全保障会議のレザイー事務局長は、米国が条件を満たせば指定の中央航路を利用可能になると説明した一方、対米対話再開の時期は不透明だと分析。",
  "cardBg": "rgba(56,189,248,0.05)",
  "cardBorder": "rgba(56,189,248,0.25)",
  "badgeColor": "#38bdf8",
  "borderColor": "rgba(56,189,248,0.4)",
  "textColor": "#7dd3fc",
  "url": "https://www.aljazeera.com/news/2026/8/27/iran-qatar-hold-hormuz-talks-amid-intl-hopes-dialogue-with-us-will-resume",
  "isLatest": true
}
```

**`updated` フィールド更新：**
```
"updated": "2026年8月29日 10:05 日本時間JST"
```

---

## [S11] 更新ログ追記（3ブロック構成）

**対象：** `<!--出典・更新ログ-->` セクション

### ブロック1：常時表示エリアの更新（本日分＋旧2件、旧3件目は除外）

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月27日 10:00 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/27 10:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランのアラグチー外相とオマーンのアルブサイディ外相がテヘランで会談し、ホルムズ海峡に共同暫定航行回廊を設置・機雷除去を共同実施する枠組みで合意（8/25）・イラン副外相ガリババディ氏は恒久ルートを30〜60日以内に協議するとしつつ暫定合意後も海峡は開放されていないと表明、南側回廊（国連承認TSS）は閉鎖の見通しと説明（8/26）・トランプ大統領は米海軍がホルムズ海峡国際水域の機雷を全て除去・爆破したとSNS投稿し新規敷設船は即時破壊と警告するも米政府の公式裏付けなし、イラン側は「虚偽」と全面否定（8/25〜26）・24日夜オマーン東岸沖でタンカー1隻が正体不明の飛翔体で被弾・機関停止、UKMTO確認（乗員無事・犯行声明なし）・原油はブレントが一時87ドル割れ・週間約8%安（8/25）・中国外務省は対中制裁計画に「中国・イラン協力は妨害されるべきでない」と改めて反発・日本関係船は残り4隻で変化なし・封鎖181日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月25日 12:11 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/25 12:11</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官が対イラン新制裁「経済的Dデイ」（Operation Economic Outcast）を発表——デジタル資産・先端技術・金・航空・海運の5分野に対象拡大、船舶・企業等ほぼ60件を新規制裁指定・中国の名指しは避けつつ「対象外はない」と圧力（8/24）・イラン通貨リアルは非公式市場で過去最安値199万2000リアル/ドルを記録、対アジア原油出荷はほぼ途絶（8/24）・中国外務省「正当な権益を守る」と対抗警告（8/24）・イラン安保高官レザイー氏「経済戦争加担国は敵」と再警告（8/22）・原油はブレント92.17ドルへ反落（-2.35%、8/24）・米メディア報道：南側航路で護衛下タンカーが1日15〜20隻通過、石油輸送量は開戦前の半分・日量約1000万バレルに到達（8/22）・日本関係船は残り4隻で変化なし・封鎖179日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月23日 09:03 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/23 09:03</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領がサウスカロライナ州の集会で「今はホルムズ海峡を米国領土だと考えている」と初めて現在形で領有を主張——「イランをもう少し爆撃しないといけないのか」とも言及（8/21）・イラン外務省バガイ報道官は月曜(24日)発表予定の新制裁を「単一国への経済戦争にとどまらない、国連加盟国全体への治外法権的主権の主張」であり「全ての国家への宣戦布告」と猛反発、二次制裁は国際法上根拠がないと主張（8/22）・アラグチー外相も新制裁は「失敗する運命」とXで皮肉・ガリバフ国会議長「独立した自国発の秩序のみが真の平和をもたらす」とX投稿・ベッセント財務長官は24日会見で「史上最も強力な制裁」詳細を発表へ、中国に協力要請・21日、オマーン・イラン両外相が電話会談し海峡開放へ向けた調整を協議も打開は不透明・ペゼシュキアン大統領「今日こそ戦争を終わらせるべき時」と表明・18日被弾船舶の乗組員1名は死亡確認（当初は負傷と発表）・ブレント原油は94ドル前後で約1か月ぶり高値圏・日本関係船は残り4隻で変化なし・封鎖177日目・ニュース3件更新・osint更新</div>
      </div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
        <div>📅 <strong>2026年8月29日 10:05 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/08/29 10:05</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>カタールのシェイク・モハンマド首相兼外相が開戦後初のテヘラン訪問——アラグチー外相・ペゼシュキアン大統領・レザイー最高国家安全保障会議事務局長と会談（8/27）・レザイー氏は通航再開の条件リストを策定中と表明、中央航路（一部オマーン領海・一部イラン領海）で合意済みと説明・米中央軍クーパー司令官はSNS動画で「国際航路は開通・勢いを増す」と主張し商船1,500隻・原油7.5億バレル分の支援実績を発表（8/27）・トランプ大統領は「MISSION ACCOMPLISHED 2026」とSNS投稿し勝利宣言（8/26）も、その直後の25日17:30UTCにタンカー「AL SALAM II」被弾をJMICが確認・ホワイトハウス報道官は米イラン交渉が現時点でないと明言（8/27）・JMICデータでは8/25〜26の通航はわずか37隻（2025年平均は日量約138隻）・ブレント原油は4営業日続落後87ドル台後半で下げ止まり（8/28時点87.58ドル）・イラン軍は損傷兵器を「再建済み」と発表・日本関係船は残り4隻で変化なし・封鎖183日目・ニュース4件更新・osint更新</div>
        <div>📅 <strong>2026年8月27日 10:00 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/27 10:00</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>イランのアラグチー外相とオマーンのアルブサイディ外相がテヘランで会談し、ホルムズ海峡に共同暫定航行回廊を設置・機雷除去を共同実施する枠組みで合意（8/25）・イラン副外相ガリババディ氏は恒久ルートを30〜60日以内に協議するとしつつ暫定合意後も海峡は開放されていないと表明、南側回廊（国連承認TSS）は閉鎖の見通しと説明（8/26）・トランプ大統領は米海軍がホルムズ海峡国際水域の機雷を全て除去・爆破したとSNS投稿し新規敷設船は即時破壊と警告するも米政府の公式裏付けなし、イラン側は「虚偽」と全面否定（8/25〜26）・24日夜オマーン東岸沖でタンカー1隻が正体不明の飛翔体で被弾・機関停止、UKMTO確認（乗員無事・犯行声明なし）・原油はブレントが一時87ドル割れ・週間約8%安（8/25）・中国外務省は対中制裁計画に「中国・イラン協力は妨害されるべきでない」と改めて反発・日本関係船は残り4隻で変化なし・封鎖181日目・ニュース3件更新・osint更新</div>
        <div>📅 <strong>2026年8月25日 12:11 JST</strong> 更新</div>
        <div><span style="color:#cbd5e1;">2026/08/25 12:11</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>ベッセント財務長官が対イラン新制裁「経済的Dデイ」（Operation Economic Outcast）を発表——デジタル資産・先端技術・金・航空・海運の5分野に対象拡大、船舶・企業等ほぼ60件を新規制裁指定・中国の名指しは避けつつ「対象外はない」と圧力（8/24）・イラン通貨リアルは非公式市場で過去最安値199万2000リアル/ドルを記録、対アジア原油出荷はほぼ途絶（8/24）・中国外務省「正当な権益を守る」と対抗警告（8/24）・イラン安保高官レザイー氏「経済戦争加担国は敵」と再警告（8/22）・原油はブレント92.17ドルへ反落（-2.35%、8/24）・米メディア報道：南側航路で護衛下タンカーが1日15〜20隻通過、石油輸送量は開戦前の半分・日量約1000万バレルに到達（8/22）・日本関係船は残り4隻で変化なし・封鎖179日目・ニュース3件更新・osint更新</div>
      </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse先頭への旧3件目（8/23分）の挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月21日 09:09 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年8月23日 09:03 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/23 09:03</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>トランプ大統領がサウスカロライナ州の集会で「今はホルムズ海峡を米国領土だと考えている」と初めて現在形で領有を主張——「イランをもう少し爆撃しないといけないのか」とも言及（8/21）・イラン外務省バガイ報道官は月曜(24日)発表予定の新制裁を「単一国への経済戦争にとどまらない、国連加盟国全体への治外法権的主権の主張」であり「全ての国家への宣戦布告」と猛反発、二次制裁は国際法上根拠がないと主張（8/22）・アラグチー外相も新制裁は「失敗する運命」とXで皮肉・ガリバフ国会議長「独立した自国発の秩序のみが真の平和をもたらす」とX投稿・ベッセント財務長官は24日会見で「史上最も強力な制裁」詳細を発表へ、中国に協力要請・21日、オマーン・イラン両外相が電話会談し海峡開放へ向けた調整を協議も打開は不透明・ペゼシュキアン大統領「今日こそ戦争を終わらせるべき時」と表明・18日被弾船舶の乗組員1名は死亡確認（当初は負傷と発表）・ブレント原油は94ドル前後で約1か月ぶり高値圏・日本関係船は残り4隻で変化なし・封鎖177日目・ニュース3件更新・osint更新</div>
          <div>📅 <strong>2026年8月21日 09:09 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック3：総件数超過対応（重複エントリーの削除）

**理由：** ブロック1・2適用後、常時表示3件＋log-collapse内9件（8/23〜8/09の重複含む）で合計12件となり上限10件を超過するため、log-collapse内で完全に重複している8/09エントリーの2件目（出典リンク直前）を削除する。

<!-- APPLY:START -->
<!-- OLD:START -->
          <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
          <div><span style="color:#94a3b8;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div>📅 <strong>2026年8月9日 10:06 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/08/09 10:06</span> — <strong style="color:#fca5a5;">【超重大更新】</strong>UAE外務省、8日未明のADNOC関連タンカーへのイランのミサイル攻撃を「敵対的行為」「海賊行為」と非難、負傷者なし（Reuters）・ADNOCは紛争開始以来15隻が被弾、今週だけで3隻・死者1名負傷20名と発表（Bloomberg/Gulf News、8/7）・米当局者は無制限の商用航行再開合意が発表され次第、対イラン港湾封鎖を解除する方針をロイターに表明——イラン交渉団は最高国家安全保障会議の承認待ちとの報道（Shafaq News）・イラン議会の排除・通行料法案はなお文言調整中で可決未了・サウジ・パキスタン・トルコがメッカでNATO第5条型の相互防衛協定に署名——フーシ派の対サウジ攻撃激化に対応（CNN、8/7）・フーシ派は木曜に政府軍30名超を殺害、金曜も攻撃継続——マリブで民間人2名死亡14名負傷・NYダウ54,036.93ドル(+0.28%)・S&P500は7,757.64ドルで最高値更新、原油はブレント83.55ドル(+1.29%)・日本関係船は残り4隻で変化なし・封鎖163日目・ニュース4件更新・osint更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S12] archive_timeline.json 追記

**対象：** `entries` 配列の末尾（最新エントリーとして追加）

```json
{
  "date": "2026-08-29",
  "dateLabel": "2026/08/29 10:05",
  "blockadeDay": 183,
  "sourceType": "realtime",
  "summary": "カタールのシェイク・モハンマド首相兼外相が開戦後初のテヘラン訪問——アラグチー外相・ペゼシュキアン大統領・レザイー最高国家安全保障会議事務局長と会談（8/27）・レザイー氏は通航再開の条件リストを策定中と表明、中央航路（一部オマーン領海・一部イラン領海）で合意済みと説明・米中央軍クーパー司令官はSNS動画で「国際航路は開通・勢いを増す」と主張し商船1,500隻・原油7.5億バレル分の支援実績を発表（8/27）・トランプ大統領は「MISSION ACCOMPLISHED 2026」とSNS投稿し勝利宣言（8/26）も、その直後の25日17:30UTCにタンカー「AL SALAM II」被弾をJMICが確認・ホワイトハウス報道官は米イラン交渉が現時点でないと明言（8/27）・JMICデータでは8/25〜26の通航はわずか37隻（2025年平均は日量約138隻）・ブレント原油は4営業日続落後87ドル台後半で下げ止まり（8/28時点87.58ドル）・日本関係船は残り4隻で変化なし",
  "relatedNews": [
    {
      "sourceLabel": "Reuters（Arab News）",
      "title": "カタール首相がテヘラン訪問——イランが通航再開の条件リスト策定に合意",
      "url": "https://www.arabnews.jp/article/middle-east/article_185141/"
    },
    {
      "sourceLabel": "gCaptain",
      "title": "タンカー「AL SALAM II」被弾——トランプ氏「Mission Accomplished」投稿の直後",
      "url": "https://gcaptain.com/tanker-hit-in-strait-of-hormuz-as-trump-declares-mission-accomplished-in-iran/"
    },
    {
      "sourceLabel": "CNBC",
      "title": "ブレント原油、4営業日続落後に87ドル台後半で下げ止まり",
      "url": "https://sundayguardianlive.com/world/brent-crude-price-today-oil-falls-108-to-8758-as-us-says-hormuz-shipping-lanes-are-free-of-iranian-sea-mines-iran-sets-reopening-conditions-272036/"
    }
  ]
}
```

---

## [C01] SHIP_CONFIG（日本関係船舶）

**確認内容（4クエリ実施・すべて再確認）：**
1. 「日本関係船舶 ホルムズ海峡 通過 足止め」→ 直近の新規発表なし
2. 「外務省 ホルムズ海峡 日本関係船舶」→ 直近の新規プレスリリースなし（外務省サイト最新は5月時点のまま）
3. 「金子国土交通大臣 会見 ホルムズ海峡」→ 直近の会見要旨に新規言及なし。直近の確定発言は7/10会見の「残り4隻」のまま
4. 英語："Japanese ships Strait of Hormuz stranded detained August 2026" → 新規報道なし

→ 結論：4クエリいずれも新規発表なし、**残り4隻のまま変化なし**と再確認。カタール・パキスタンの並行仲介が活発化する中でも、日本政府からの新規動きは確認されていない。

<!-- APPLY:START -->
<!-- OLD:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年8月27日 10:00 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近確定発言は7/10会見の「残り4隻」）'
};
<!-- OLD:END -->
<!-- NEW:START -->
const SHIP_CONFIG = {
  totalShips:    4,
  passableShips: 0,
  date:          '2026年7月10日',
  dateConfirmed: '2026年8月29日 10:05 JST 確認・変化なし（4隻のまま。外務省・国交省へ日英4クエリで新規発表なしを確認。金子国交相の直近確定発言は7/10会見の「残り4隻」）'
};
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [JSON-LD] dateModified

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-08-27T10:00:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-08-29T10:05:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
[✓] S01 ヘッダー ― 2026年8月29日 10:05 JST・警戒レベル最高の要約更新
[✓] S02 TICKER ― JMIC通航データ・ホワイトハウス発言中心でS01と重複回避
[✓] S03 速報インシデント ― トグル日付・見出し・本文・リスト2件追加（AL SALAM II特化）
[✓] S04 情勢カード3枚 ― カタール外交／米軍主張と実態／タンカー・市場・日本船の3切り口
[✓] S05 COUNTDOWN ― Phase29・封鎖183日目
[✓] S06 シナリオ確率補足バナー ― 8/29 10:05 JST日付更新（3箇所）・A↑B→C↓D↓
[✓] S07 シナリオ4本 ― A/B/C/D本文をS06と異なる切り口で更新
[✓] S08 シナリオフッター ― 次の焦点5点をS05のdl-noteと重複しない視点で更新
[✓] S08.5 全ルート現況サマリー ― 8/29 10:05 JST更新・航路別の切り口で記述
[✓] S09 30秒カラム ― 3行サマリー＋バッジ5枚を最後に更新
[✓] S10 news_data.json ― latest 4件追加（既存6件中の最古4件をarchiveへ）・osint 1件追加・updated日付
[✓] S11 更新ログ ― 3ブロック構成（常時表示3件固定＋log-collapse先頭挿入＋重複エントリー削除で総件数調整）
[✓] C01 SHIP_CONFIG dateConfirmed ― 8/29 10:05 JST・変化なし（4クエリ再確認）
[✓] JSON-LD dateModified ― 2026-08-29T10:05:00+09:00

二重封鎖表記チェック：本日分での「二重封鎖」表記なし（該当箇所なし）✓
TICKER内JST表記チェック：全日付にJST付き ✓
人名表記チェック：習近平への言及なし（該当箇所なし）／トランプ・アラグチー等は全て日本語カタカナ表記 ✓
禁止ソースチェック：毎日新聞・Wikipedia・TBS・朝日新聞・NHK・東京新聞・テレビ朝日は使用なし／Al Jazeeraはosint配列のみに使用 ✓
URL捏造チェック：全URL web検索で実在確認済み ✓
セクション重複チェック：S01(総括)→S02(数値データ)→S03(被弾詳細)→S04(3視点)→S05(乖離テーマ)→S06/S07(シナリオ別分析)→S08(検証可能性)→S08.5(航路別)→S09(総括)で、同一文言の使い回しを避け表現を分散 ✓
```
