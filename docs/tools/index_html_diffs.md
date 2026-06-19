# index_html_diffs.md — 2026年6月20日 08:18 JST 更新分

> Claude Code への指示：以下の差分を index.html / news_data.json に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## ✅ Step 0 確認結果

- project_knowledge_search 2件（index_html_diffs.md / 更新ログ）に加え、**GitHub raw（docs/index.html・docs/data/news_data.json）を直接フェッチしてベースライン実態を確認**。
- 確認済みベースライン：**2026年6月19日 07:55 JST版**（Phase 10・封鎖113日目）と完全一致。
- 本日の封鎖日数：**114日目**（6/18=112→6/19=113→6/20=114の連番を継続）。
- C01（日本関係船舶）確認：web検索実施済み・**重要進展あり**。茂木外相が6/19会見で、日本人3名搭乗の船舶1隻がホルムズ海峡を通過しペルシャ湾外へ退避したと発表——これにより**日本人乗組員が乗船する日本関係船舶は全てペルシャ湾外への退避が完了**。残る日本関係船舶は**37隻**（日本人乗船なし・38隻から1隻減）。出典：外務省（茂木外務大臣会見記録, 6/19）。

## 📌 本日の主要新展開（要約）

1. **米イラン実務協議（ビュルゲンシュトック・瑞）が延期**——レバノン南部でのイスラエル攻撃激化を理由にイラン代表団が渡航を延期し、バンス副大統領のスイス訪問もキャンセル。新日程は未定（NBC News, CBS News 6/19）。
2. **イスラエル・ヒズボラが停戦に合意**——トランプ大統領がネタニヤフ首相に要請し米仲介で実現したと米当局者が説明。ただしIDFは合意発表後も一部攻撃を継続したと報じられている（The Hill, NBC News 6/19）。
3. **イラン新設「ペルシャ湾海峡庁（PGSA）」がホルムズ通航に義務的保険・指定航路・48時間前申請を導入**——MOUの「60日間無料通航」期間中は無償としつつ、期間終了後の課金権を留保。英国主導で同盟国がこれに反発（Lloyd's List, Middle East Eye 6/19）。
4. **通航量に改善の兆し**——AXSMarine集計で6/18に検証済み商船25隻が通航（4/18以来最多・6月上旬平均の5倍）。CENTCOMは「一晩で20隻超が通過」と発表、紛争開始後初のサウジ所有タンカーの通過も確認（CBS News 6/19）。
5. **日本人乗組員が乗船する日本関係船舶は全てペルシャ湾外への退避が完了**——茂木外相が6/19会見で発表。日本人3名搭乗の船舶1隻がホルムズ海峡を通過し退去、これで日本人乗船船は全て退避完了。残る日本関係船舶は37隻（38隻から1隻減・日本人乗船なし）（外務省 6/19）。
6. イラン側は、レバノン情勢が改善しなければMOU実施を停止し、イスラエルへの無警告反撃も辞さない構えだと米側に伝達したとの報道あり（Drop Site News 6/19）。
7. モジュタバ・ハメネイのMOU承認声明の詳細判明——「個人的には異なる意見」としつつ大統領・SNSCの責任保証を条件に許可。IRGCは「山のように堅固」に政府を支持しつつ、米の違反があれば「より大きな歴史的敗北」を与える用意があると警告。
8. 油価：WTI $76前後・ブレント $79前後（Trading Economics, Investing.com 6/19-20）——週間で約8〜10%下落。

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🕊️ 警戒レベル：高（MOU実施開始・ビュルゲンシュトック実務協議）</span>
    <span class="badge-item badge-date">📅2026年6月19日 07:55 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🕊️ 警戒レベル：高（MOU実施に動揺・ビュルゲンシュトック協議延期）</span>
    <span class="badge-item badge-date">📅2026年6月20日 08:18 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年6月19日 07:55 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年6月19日 07:55 JST） -->
      🕊️【最高指導者がMOU承認】モジュタバ・ハメネイ「異なる見解持つも承認」と表明——イラン国内の意思決定完了（6/18 JST Al Jazeera）｜🏔️ 本日ビュルゲンシュトック（瑞ルツェルン）で米イラン実務協議——会場をジュネーブから変更・パキスタン首相シャリフは訪欧キャンセル（電子署名済みのため）｜🇪🇺 独仏英伊が機雷除去任務参加を表明——「防衛的・独立ミッション」共同声明（メルツ・マクロン・スターマー・メローニ）｜☢️ IAEA・グロッシ事務局長「技術的検証作業開始」——440kg・60%濃縮ウランの希釈化（downblending）をIAEAが監督｜🚢 通航実態は前日比変化なし——日本船主協会「もう少し詳しい情報を待ちたい」・38隻継続足止め｜📉 WTI $75前後・ブレント $78前後で安値圏継続｜⚠️ ホルムズ閉鎖113日目・MOU実施フェーズ
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年6月20日 08:18 JST） -->
      🚨【米イラン実務協議が延期】レバノンでのイスラエル攻撃激化を理由にイラン代表団が渡航延期・バンス副大統領のスイス訪問もキャンセル——新日程は未定（6/19 JST）｜🇯🇵 日本人乗船の日本関係船舶が全てペルシャ湾外へ退避完了——茂木外相会見（6/19）・残る日本関係船舶は37隻に｜🇱🇧 イスラエル・ヒズボラが停戦に合意——トランプの要請で実現も、IDFは停戦後も一部攻撃継続と報道（6/19 JST）｜⚓ イラン、ホルムズ海峡通航に「義務的保険」導入——新設PGSAが指定航路・48時間前申請を義務化、60日間は無料だが将来課金の可能性を留保——英国主導で同盟国が反発（Lloyd's List/MEE 6/19）｜🚢 通航量に改善の兆し——6/18に検証済み商船25隻が通航（4/18以来最多・6月上旬平均の5倍）・CENTCOM「一晩で20隻超が通過」（CBS News 6/19）｜📉 WTI $76前後・ブレント $79前後——週間で約8〜10%下落・ホルムズ閉鎖114日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 6/19 07:55 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 6/20 08:18 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の `<strong>` タグを置き換え）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/19 07:55 速報】最高指導者モジュタバ・ハメネイがMOU承認（「異なる見解持つも承認」・Al Jazeera 6/18）｜本日ビュルゲンシュトック（瑞ルツェルン）で米イラン実務協議——会場をジュネーブから変更・パキスタン首相シャリフは訪欧キャンセル｜独仏英伊が機雷除去任務参加を共同声明で表明（メルツ・マクロン・スターマー・メローニ）｜IAEA・グロッシ事務局長「技術的検証作業開始」——440kg・60%濃縮ウラン希釈化(downblending)をIAEA監督｜通航実態は変化なし・日本船主協会38隻継続足止め｜WTI $75前後・ブレント $78前後で安値圏継続｜封鎖113日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/20 08:18 速報】米イラン実務協議（ビュルゲンシュトック）が延期——レバノンでのイスラエル攻撃激化が理由・バンス副大統領のスイス訪問もキャンセル・新日程未定（6/19）｜日本人乗船の日本関係船舶が全てペルシャ湾外へ退避完了——茂木外相発表・残る日本関係船舶37隻に（外務省 6/19）｜イスラエル・ヒズボラが停戦合意——トランプの要請で実現も完全履行は未確認｜イラン新設PGSAがホルムズ通航に義務的保険・指定航路を導入——60日間無料も将来課金の可能性を留保・英国主導で同盟国反発｜通航量に改善兆し——6/18に25隻通航（4/18以来最多）・CENTCOM「一晩で20隻超通過」｜WTI $76前後・ブレント $79前後・封鎖114日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に1件追加：旧見出しを保存・漏れ防止）

<!-- APPLY:START -->
<!-- OLD:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(134,239,172,0.5);">
  【6/18 09:51 JST】<strong style="color:#86efac;">MOU14条項全文公開・電子署名発効確認</strong>——5条項：60日無料通航・30日以内機雷除去・米$3000億復興計画。バガエイ外務省報道官「電子署名済み・式典不要」（NBC News, 6/18）
</li>
<!-- OLD:END -->
<!-- NEW:START -->
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(134,239,172,0.5);">
  【6/19 07:55 JST】<strong style="color:#86efac;">最高指導者モジュタバがMOU承認・本日ビュルゲンシュトックで実務協議予定</strong>——「異なる見解だが承認」と表明・独仏英伊が機雷除去任務参加を共同声明で表明・IAEA技術検証開始（Al Jazeera, CNN 6/19）
</li>
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(134,239,172,0.5);">
  【6/18 09:51 JST】<strong style="color:#86efac;">MOU14条項全文公開・電子署名発効確認</strong>——5条項：60日無料通航・30日以内機雷除去・米$3000億復興計画。バガエイ外務省報道官「電子署名済み・式典不要」（NBC News, 6/18）
</li>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

### カード①（外交）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🕊️ 外交：最高指導者がMOU承認・本日ビュルゲンシュトックで実務協議</div>
        <div class="s-body">イラン最高指導者モジュタバ・ハメネイが18日夜、MOUについて「異なる見解を持つが承認した」と表明（Al Jazeera）——イラン国内の最終意思決定が完了。本日6/19、米イラン両国が仲介国パキスタン・カタールと共に瑞ビュルゲンシュトック（ルツェルン近郊）で実施段階の実務協議を開催予定。会場は当初予定のジュネーブから変更。パキスタン首相シャリフは「MOUは既に電子署名済み」として訪欧を取りやめ。ガリバフ議長は通航サービス料がMOU文書上で既に正式化されたと主張——米「永久無料」との解釈矛盾は未解消。</div>
        <div class="s-src">出典: Al Jazeera / France24(AFP) / CNN（6/19 07:55 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🕊️ 外交：ビュルゲンシュトック協議が延期・レバノン情勢が新たな火種に</div>
        <div class="s-body">本日6/19開催予定だった米イラン実務協議（瑞ビュルゲンシュトック）は、レバノン南部でのイスラエル攻撃激化を理由にイラン代表団が渡航を延期し、バンス副大統領のスイス訪問もキャンセル——開催見送りとなった（新日程未定）。イランは仲介国を通じ「イスラエル・ヒズボラ間の停戦保証」を要求。同日午後、米仲介によりイスラエル・ヒズボラが停戦に合意したと米当局者が明らかにしたが、IDFは合意発表後も一部攻撃を継続したと報じられている。レバノン情勢が改善しなければMOU実施を停止し、イスラエルへの無警告反撃も辞さない構えだとイランが米側に伝えたとの報道もある。</div>
        <div class="s-src">出典: Al Jazeera / NBC News / The Hill / Drop Site News（6/20 08:18 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード②（海運/軍事）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🚢 海運：欧州が機雷除去任務参加表明・通航実態は変化なし</div>
        <div class="s-body">独仏英伊（メルツ首相・マクロン大統領・スターマー首相・メローニ首相）が共同声明で「防衛的・独立的ミッション」として機雷除去・商船保護への参加意志を表明。一方、Argus調査では合意発表後も船舶動向に大きな変化なし——船主は6/19以降の詳細情報を待つ姿勢。日本船主協会も「もう少し詳しい情報を待ちたい・機雷敷設報道もあり安易に進めない」とコメント・38隻が引き続き湾内足止め継続（変化なし確認）。</div>
        <div class="s-src">出典: Argus Media / Reuters (Japan Shipowners' Association) / AFP（6/19 07:55 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🚢 海運：イラン新設PGSAが義務的保険・指定航路を導入——日本人乗船船は全退避完了</div>
        <div class="s-body">イランが新設した「ペルシャ湾海峡庁（PGSA）」が、ホルムズ海峡を通航する全船舶に対し同庁承認の保険加入・48時間前の通航申請・ラーク島沿いの指定航路順守を義務化する文書を公開。MOUが定める「60日間無料通航」期間中は無償提供としつつ、期間終了後の課金の可能性を留保しており、英国主導で同盟国が国際海事法違反になりかねないとして容認しない方針。一方、AXSMarine集計では6/18に検証済み商船25隻がホルムズを通航——4/18以来の最多で6月上旬平均の5倍。CENTCOMは「一晩で20隻超が通過した」と発表し、紛争開始後初のサウジ所有タンカーの通過も確認された。日本関連では、茂木外相が6/19会見で日本人3名搭乗の船舶1隻の通過を発表——日本人乗組員が乗船する日本関係船舶は全てペルシャ湾外への退避が完了した。残る日本関係船舶は37隻（日本人乗船なし）。</div>
        <div class="s-src">出典: Lloyd's List / Middle East Eye / CBS News (AXSMarine) / ABC News / 外務省（茂木外務大臣会見, 6/19）（6/20 08:18 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③（市場）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">📉 市場：WTI/ブレントとも安値圏で推移・Goldman「湾岸フロー日量1100万バレルに回復」</div>
        <div class="s-body">WTI $75前後・ブレント $78前後で安値圏が継続（Trading Economics, 6/18）。Goldman Sachsは6/16付ノートで「供給回復はより強い可能性」とし、湾岸産油フローが既に日量1100万バレルまで増加（ホルムズ経由分・迂回分双方の増加含む）と分析。一方、IEAの2027年供給過剰警告（需要増+2百万b/d vs 供給増+8百万b/d）は継続。タンカー滞留の解消には10〜15日程度かかる見通しとの業界専門家の指摘あり。</div>
        <div class="s-src">出典: CNBC / Trading Economics / Goldman Sachs（6/19 07:55 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">📉 市場：WTI/ブレントとも安値圏で推移・週間で大幅下落</div>
        <div class="s-body">WTI原油は$76前後・ブレントは$79前後で推移（Trading Economics・Investing.com, 6/19-20）。実務協議の延期とPGSA保険義務化を巡る不透明感から相場はやや不安定ながらも、週間ベースでは紛争中の上昇分の大半を打ち消す約8〜10%の下落となった。市場は通航再開の持続性を見極める姿勢を継続しており、商船の本格的な復帰にはなお時間を要するとの見方が大勢。</div>
        <div class="s-src">出典: Trading Economics / Investing.com（6/20 08:18 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU発効・機雷除去フェーズ（30日以内＝7月上旬目途）」——封鎖113日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU発効・機雷除去フェーズ（30日以内＝7月上旬目途）」——封鎖114日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        🕊️ <strong>米イラン和平合意成立——MOU14条項署名・6/19スイス署名式まであと3日・封鎖110日目</strong>
<!-- OLD:END -->
<!-- NEW:START -->
        🕊️ <strong>米イラン和平合意成立——MOU14条項署名・ビュルゲンシュトック実務協議は延期（新日程未定）・封鎖114日目</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

⚠️ Claude Code：上記dl-noteのold_strは現在のHTML実態と完全一致するか `grep -n "米イラン和平合意成立"` で確認すること（複数箇所にマッチした場合は前後の固有タグで一意化）。

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#4ade80;">📊 2026年6月19日 07:55 JST 更新</span><br>
  📊 <strong>MOU発効・実施段階移行（6/19 07:55現在）：</strong><br>
  🅐 外交解決 <span style="color:#4ade80;">↑↑↑↑↑↑</span> — 最高指導者モジュタバが「異なる見解だが承認」と表明・本日ビュルゲンシュトック実務協議開始——最有力シナリオの確度は最高水準を維持<br>
  🅑 実施遅延 <span style="color:#4ade80;">↑</span> — 通航実態は変化なし・船主は詳細情報待ち姿勢継続・欧州が機雷除去任務参加を表明したが実働化は未定——部分再開・完全正常化遅延リスク残存<br>
  🅒 合意崩壊 <span style="color:#f87171;">↓↓↓↓</span> — 60日核交渉中にイスラエル・レバノン問題が顕在化しMOU実施が一方的に停止される最悪シナリオ<br>
  🅓 合意破棄 <span style="color:#f87171;">↓↓↓↓↓</span> — 60日核交渉決裂によるイランの一方的破棄・再封鎖——MOU発効済みの現時点では極めて低い<br>
  <strong style="color:#fbbf24;">MOU実施フェーズ継続——A↑↑↑↑↑↑ B↑ C↓↓↓↓ D↓↓↓↓↓（本日のビュルゲンシュトック協議結果が次の焦点）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年6月19日 07:55 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="background:rgba(239,68,68,0.07);border:1px dashed rgba(239,68,68,0.35);border-radius:8px;padding:12px 16px;margin-bottom:16px;font-size:0.78rem;color:#fca5a5;line-height:1.8;">
  <span style="font-weight:800;color:#4ade80;">📊 2026年6月20日 08:18 JST 更新</span><br>
  📊 <strong>MOU実施初日に動揺——協議延期・レバノン情勢が新リスク（6/20 08:18現在）：</strong><br>
  🅐 外交解決 <span style="color:#4ade80;">↑↑↑↑↑</span> — 実務協議は延期されたが、通航量増加（6/18に25隻）・イスラエル/ヒズボラ停戦合意など部分的な前進材料も継続——確度はなお高水準ながら足踏み<br>
  🅑 実施遅延 <span style="color:#4ade80;">↑↑</span> — イランPGSAによる保険・許可制度の導入で通航管理が複雑化・協議延期で実施スケジュールに遅れ——部分再開・完全正常化遅延リスクが拡大<br>
  🅒 合意崩壊 <span style="color:#f87171;">↓↓↓</span> — レバノン情勢を巡るイランの警告（MOU停止の可能性）・保険課金問題を巡る対立が崩壊リスクをやや押し上げ<br>
  🅓 合意破棄 <span style="color:#f87171;">↓↓↓↓</span> — 停戦合意自体は維持・双方とも対話継続の意志を示しており、即時破棄の可能性は依然低い<br>
  <strong style="color:#fbbf24;">MOU実施フェーズで初の試練——A↑↑↑↑↑ B↑↑ C↓↓↓ D↓↓↓↓（協議再開の日程発表が次の焦点）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年6月20日 08:18 JST 時点での分析に基づく自動同期
  </div>
  <span style="font-size:0.7rem;color:#64748b;">※ 確率数値は hormuz-data- の manual-update.json を Gemini AI が自動更新。syncScenarioFromDashboard() がフェッチして sc-tag-A/B/C/D に反映。</span>
</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（本文）

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>最高指導者モジュタバが18日夜「異なる見解だが承認」と表明——イラン国内の意思決定リスクが大きく後退。本日ビュルゲンシュトックで実務協議開始、独仏英伊は機雷除去任務への参加を共同声明で表明。Goldman Sachs分析では湾岸産油フローが既に日量1100万バレルまで回復。次の焦点は機雷除去完了（MOU5条項：30日以内義務）と60日核交渉の本格化。WTI $65〜75、ブレント $70〜80への収束が見込まれる。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>本日予定されていた米イラン実務協議（ビュルゲンシュトック）はレバノンでのイスラエル攻撃激化を理由に延期されたが、同日午後にイスラエル・ヒズボラが停戦に合意。通航面では6/18に25隻が通航——4/18以来の最多を記録し、CENTCOMは一晩で20隻超の通過を確認、紛争開始後初のサウジ所有タンカーも通過した。日本関連でも、茂木外相が6/19、日本人乗組員が乗船する日本関係船舶が全てペルシャ湾外への退避を完了したと発表——前向きな材料が積み上がっている。次の焦点は協議再開の日程確定とイランPGSAの保険・許可制度を巡る調整。WTI $65〜75、ブレント $70〜80への収束シナリオは維持。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>合意発効も機雷除去・保険・荷主の三重ボトルネックで通航回復が2〜3ヶ月遅れるシナリオ。Argus調査では合意発表後も船舶動向に実質変化なし——日本船主協会も「機雷敷設報道もあり安易に進められない」と慎重姿勢を継続、38隻の足止め状態が変わらず。欧州の機雷除去任務は表明段階に留まり実働化は未定。ガリバフ議長「サービス料は既にMOU文書で正式化済み」発言が将来的な通航コスト上昇リスクを示唆。WTI $80〜90に再上昇の可能性。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>実務協議の延期・イラン新設PGSAによる義務的保険・指定航路・48時間前申請の導入により、通航正常化には依然時間を要するとの見方が強まっている。PGSAは60日間は無料としつつ将来の課金権を留保しており、英国主導の同盟国がこれに反発——MOUの「無料通航」原則との矛盾が顕在化。日本関連では日本人乗船船の退避は完了したものの、残る37隻の足止め状態は継続。WTI $80〜90に再上昇する可能性が残る。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>電子署名発効も60日核交渉中にイスラエル問題が顕在化するシナリオ。イラン軍は「停戦発表以降、イスラエルが84回違反」と非難——アラグチー「レバノン攻撃継続はMOU違反」発言が伏線として残存。60日交渉中にイスラエルがレバノン攻撃を拡大→イランがMOU実施を停止宣言→通航再封鎖。WTI $100-120。Stimson Center「イスラエル=最大の不安定要因」と分析。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>レバノン情勢の悪化を受け、イランは「イスラエルの攻撃が止まらなければMOU実施を停止し、無警告でイスラエルに反撃する用意がある」と米側に伝達したと報じられた。同日中にイスラエル・ヒズボラの停戦が成立したことで最悪の事態は当面回避されたが、IDFは停戦後も一部攻撃を継続したとの報道もあり予断を許さない。WTI $100-120。Stimson Center「イスラエル=最大の不安定要因」との分析が改めて裏付けられた形。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>MOU発効・機雷除去後も60日核交渉で根本的合意が得られず、イランが一方的に協議を打ち切るシナリオ。MOUはIAEAに440kg・60%濃縮ウランの希釈化（downblending）検証を委ねるが、グロッシ事務局長は「事実を先取りするのは賢明でない」と慎重姿勢——検証範囲・タイムラインは依然未確定。米国が再制裁→イランが「MOU破棄」宣言→再封鎖・再機雷散布。WTI $130以上。Iran SITREP「核軟化に対するイラン国内コスト上昇中・強硬派の抵抗」を指摘。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>モジュタバ・ハメネイは18日夜の声明でMOU承認の条件として「イラン国民と抵抗の枢軸の権利保護」を明記、IRGCも「敵が違反すればより大きな歴史的敗北を与える用意がある」と警告しており、強硬派の許容範囲は依然限定的。IAEAによる440kg濃縮ウラン検証の具体的な開始時期は未確定のまま。米国の再制裁や核交渉決裂が生じれば、MOU破棄・再封鎖のリスクは即座に再燃しうる。WTI $130以上。Iran SITREP「核軟化に対するイラン国内コスト上昇中・強硬派の抵抗」を指摘。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5つ）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">本日ビュルゲンシュトック実務協議の結果（パキスタン首相は欠席・実施詳細の合意可否）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">欧州の機雷除去任務の実働化（独仏英伊が表明・国連安保理決議等の法的根拠が必要）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">IAEAによる440kg・60%濃縮ウラン検証・希釈化（downblending）の開始時期</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">日本関係38隻の段階的解放と保険・BIMCO問題の解消</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">イスラエル・レバノン問題の帰趨（停戦違反84回——ヒズボラ撤退合意が60日交渉の前提条件になりうる）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年6月19日 07:55 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">米イラン実務協議（ビュルゲンシュトック）の新日程——延期理由となったレバノン情勢の収束が前提条件に</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">イスラエル・ヒズボラ停戦の履行状況（IDFは合意後も一部攻撃継続と報道・完全停止の確認が焦点）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">イラン新設PGSAの保険・許可制度を巡る国際調整（英国主導の同盟国がMOU「無料通航」原則との整合性を問題視）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">IAEAによる440kg・60%濃縮ウラン検証・希釈化（downblending）の開始時期</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">日本関係37隻の段階的解放——日本人乗船船は全退避完了（6/19）・通航量は改善傾向（6/18に25隻）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年6月20日 08:18 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年6月19日 07:55 JST 再確認済・通航実態に変化なし）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">→ ホルムズ：Argus調査で合意発表後も船舶動向に大きな変化なし・船主は6/19以降の詳細情報待ち、日本船主協会「機雷敷設報道もあり安易に進められない」と慎重姿勢継続、紅海：フーシ派「イスラエル船完全禁止」継続——大手船社が接近一時停止・代替ルート信頼性低下、ケープ回廊完全飽和・コスト倍増、日本関係船舶38隻が湾内足止め継続（変化なし確認）</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年6月20日 08:18 JST 更新・日本人乗船船は全退避完了）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">→ ホルムズ：6/18に検証済み商船25隻が通航——4/18以来最多・6月上旬平均の5倍（AXSMarine）、CENTCOM「一晩で20隻超通過」、紛争後初のサウジ所有タンカーも通過確認。一方、イラン新設PGSAが義務的保険・指定航路・48時間前申請を導入——将来課金の可能性を留保し国際的反発を招いている。日本関連では、茂木外相が6/19、日本人乗組員が乗船する日本関係船舶は全てペルシャ湾外への退避が完了したと発表——残る日本関係船舶は37隻（日本人乗船なし）。紅海：フーシ派「イスラエル船完全禁止」継続——大手船社が接近一時停止・代替ルート信頼性低下、ケープ回廊完全飽和・コスト倍増</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## MAP補足：SHIP_CONFIG（毎回必須チェック）

<!-- APPLY:START -->
<!-- OLD:START -->
const SHIP_CONFIG = {
  totalShips:    38,
  passableShips: 0,
  date:          '2026年6月19日',
  dateConfirmed: '2026年6月19日 07:55 JST 変更なし（web検索確認済）：日本関係船舶38隻が引き続き湾内足止め（日本船主協会、6/16発表を6/19時点でも維持確認）。同協会は「機雷敷設報道もあり安易に進められない・もう少し詳しい情報を待ちたい」とコメント。MOU発効・最高指導者承認後も日本船の通過再開は未着手。'
};
<!-- OLD:END -->
<!-- NEW:START -->
const SHIP_CONFIG = {
  totalShips:    37,
  passableShips: 0,
  date:          '2026年6月20日',
  dateConfirmed: '2026年6月20日 08:18 JST 重要進展（外務省・web検索確認済）：茂木外相が6/19会見で、日本人3名搭乗の船舶1隻がホルムズ海峡を通過しペルシャ湾外へ退避したと発表——これにより日本人乗組員が乗船する日本関係船舶は全てペルシャ湾外への退避が完了。残る日本関係船舶は37隻（38隻から1隻減・日本人乗船なし）。茂木外相「本当に良かった」とコメント、政府は残る37隻の早期通過に向け外交努力を継続。'
};
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（最後に作成）

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
🕊️ 最高指導者モジュタバがMOU承認・本日ビュルゲンシュトックで実務協議——独仏英伊が機雷除去任務参加を表明（6/19 07:55 JST）
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🚢 通航実態変化なし・38隻足止め継続——日本船主協会「機雷敷設報道もあり安易に進められない」・IAEAが440kg濃縮ウラン検証担当に
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📉 WTI $75前後・ブレント $78前後で安値圏継続——Goldman Sachs「湾岸フロー日量1100万バレルに回復」分析・IEA供給過剰警告継続
</span>
<!-- OLD:END -->
<!-- NEW:START -->
🚨 ビュルゲンシュトック実務協議が延期——レバノン情勢悪化が理由・同日イスラエル/ヒズボラは停戦合意（6/20 08:18 JST）
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🚢 通航量に改善兆し（6/18に25隻）・日本人乗船の日本関係船は全退避完了——イラン新設PGSAが義務的保険・指定航路を導入、残る37隻は足止め継続
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📉 WTI $76前後・ブレント $79前後——協議再開の日程発表とPGSA保険問題の行方が焦点
</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#f87171;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚠️ 閉鎖113日目</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📉 WTI $75 / Brent $78</span>
<span style="display:inline-block;background:rgba(147,51,234,0.15);border:1px solid rgba(147,51,234,0.3);color:#c084fc;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🏔️ 本日ビュルゲンシュトック実務協議</span>
<span style="display:inline-block;background:rgba(134,239,172,0.25);border:1px solid rgba(134,239,172,0.5);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️ 最高指導者がMOU承認</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#f87171;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚠️ 閉鎖114日目</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📉 WTI $76 / Brent $79</span>
<span style="display:inline-block;background:rgba(147,51,234,0.15);border:1px solid rgba(147,51,234,0.3);color:#c084fc;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🏔️ 実務協議は延期——新日程未定</span>
<span style="display:inline-block;background:rgba(134,239,172,0.25);border:1px solid rgba(134,239,172,0.5);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🇯🇵 日本人乗船船は全退避完了</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

⚠️ Claude Code：以下を `docs/data/news_data.json` にマージしてください（既存データを全置換しないこと）。

### `updated` フィールド

<!-- APPLY:START -->
<!-- OLD:START -->
"updated": "2026年6月19日 07:55 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
"updated": "2026年6月20日 08:18 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

### `latest` 配列の先頭に新規4件を追加

```json
{
  "title": "米イラン実務協議（ビュルゲンシュトック）が延期——レバノン情勢悪化が理由",
  "body": "イラン代表団がレバノン南部でのイスラエル攻撃激化を理由に渡航を延期し、バンス副大統領のスイス訪問もキャンセルされたことで、6月19日にスイス・ビュルゲンシュトックで予定されていた米イラン実務協議は開催見送りとなった。新たな日程は示されていない。",
  "sourceLabel": "NBC News",
  "date": "2026年6月19日 JST",
  "label": "⚠️ 外交",
  "url": "https://www.nbcnews.com/world/iran/us-iran-talks-postponed-vance-cancels-trip-israel-strikes-lebanon-rcna350830"
},
{
  "title": "イラン新設PGSA、ホルムズ通航に義務的保険・指定航路を導入——将来課金の可能性を留保",
  "body": "イランが新設したペルシャ湾海峡庁（PGSA）は、ホルムズ海峡を通航する全船舶に対し同庁承認の保険加入・48時間前の通航申請・指定航路（ラーク島沿い）の順守を義務化する文書を公表した。米イランMOUが定める60日間の無料通航期間中は無償とするが、期間終了後の課金権を留保しており、英国主導で同盟国がこれに反発している。",
  "sourceLabel": "Middle East Eye",
  "date": "2026年6月19日 JST",
  "label": "🚢 海運",
  "url": "https://www.middleeasteye.net/news/iran-plans-charge-insurance-fee-vessels-transiting-hormuz-after-us-deal-expires"
},
{
  "title": "イスラエル・ヒズボラが停戦合意——レバノン情勢の悪化が一時沈静化",
  "body": "トランプ大統領がネタニヤフ首相に要請したことを受け、イスラエルとヒズボラが6月19日に停戦に合意したと米当局者が明らかにした。ただし、合意発表後もイスラエル国防軍（IDF）が一部攻撃を継続したとの報道があり、完全な履行は未確認。",
  "sourceLabel": "The Hill",
  "date": "2026年6月19日 JST",
  "label": "🕊️ 外交",
  "url": "https://thehill.com/homenews/5931781-ceasefire-lebanon-israel-hezbollah/"
},
{
  "title": "ホルムズ海峡の通航量に改善の兆し——6/18に検証済み商船25隻が通航",
  "body": "海事データ企業AXSMarineによれば、6月18日にホルムズ海峡を通航した検証済み商船は25隻——4月18日以来の最多で、6月上旬の平均日量の5倍に達した。米中央軍（CENTCOM）は一晩で20隻超が通過したと発表し、紛争開始後初となるサウジアラビア所有タンカーの通過も確認された。",
  "sourceLabel": "CBS News",
  "date": "2026年6月19日 JST",
  "label": "🚢 海運",
  "url": "https://www.cbsnews.com/live-updates/iran-us-war-talks-suspended-trump-mou-israel-lebanon-hezbollah-fighting/"
}
```

### `osint` 配列の先頭に新規1件を追加（既存先頭は `isLatest:false` へ変更）

```json
{
  "id": "osint-002-0620",
  "date": "2026年6月19日（現地）/ 2026年6月20日 JST",
  "titleJa": "【Al Jazeera】レバノン情勢の悪化で米イラン協議延期——停戦合意の持続性に懸念",
  "titleEn": "Fears for US-Iran deal as talks delayed by Israeli strikes on Lebanon",
  "country": "Qatar",
  "media": "Al Jazeera",
  "cardBg": "rgba(0,150,136,0.13)",
  "cardBorder": "rgba(0,150,136,0.35)",
  "badgeColor": "#00897b",
  "borderColor": "#00897b",
  "textColor": "#80cbc4",
  "url": "https://www.aljazeera.com/news/2026/6/19/us-iran-talks-postponed-as-israel-attacks-lebanon",
  "isLatest": true
}
```

⚠️ Claude Code：既存の `osint-001-0619`（isLatest:true）を `isLatest:false` に変更すること。

### `staleNotice` フィールド

<!-- APPLY:START -->
<!-- OLD:START -->
"staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
"staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

⚠️ Claude Code：staleNoticeは変更なし（新情報ありのため空文字を維持）。上記ブロックはold=newのため適用不要（参考表示のみ）。

---

## [S11] 更新ログ（2ブロック構成・必須）

### ブロック1：常時表示3件の更新

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年6月19日 07:55 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/19 07:55</span> — <strong style="color:#fca5a5;">【重大進展】</strong>最高指導者モジュタバ「異なる見解だが承認」表明・本日ビュルゲンシュトック（瑞）で米イラン実務協議——会場をジュネーブから変更・パキスタン首相訪欧キャンセル｜独仏英伊が機雷除去任務参加を共同声明で表明｜IAEA・グロッシ事務局長「技術検証開始」——440kg濃縮ウラン希釈化を監督｜通航実態変化なし・日本関係38隻継続足止め｜WTI $75前後・ブレント $78前後で安値圏継続｜封鎖113日目・ニュース1件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月18日 09:51 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/18 09:51</span> — <strong style="color:#fca5a5;">【重大更新】</strong>MOU14条項全文公開（60日無料通航・30日機雷除去・$3000億復興計画）・6/19ジュネーブ署名式キャンセル確定（電子署名発効確認済：バガエイ外務省報道官）・Goldman Sachs Brent Q4$80下方修正・IEA供給過剰警告・WTI $75前後（5日連続下落・3月来最安値）・日本関係38隻足止め継続・封鎖112日目・ニュース2件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月17日 08:44 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/17 08:44</span> — <strong style="color:#fca5a5;">【重大フォロー】</strong>アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」警告（6/17）｜イランタンカー2隻（DIONA・HERO2）封鎖圏脱出・3.8百万バレル原油輸出——2ヶ月ぶり｜ファルス「MOU通航無料60日のみ」vs 米「無条件」矛盾浮上｜BIMCO高リスク警告継続・日本関係船舶38隻足止め（日本船主協会）｜WTI $78前後（4日連続下落）｜6/19署名まで2日・封鎖111日目・ニュース2件更新・OSINT更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年6月20日 08:18 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/20 08:18</span> — <strong style="color:#fca5a5;">【重大フォロー】</strong>米イラン実務協議（ビュルゲンシュトック）延期——レバノン情勢悪化が理由・バンス副大統領訪欧キャンセル・新日程未定｜日本人乗船の日本関係船は全てペルシャ湾外へ退避完了（茂木外相 6/19）・残る日本関係船舶37隻に｜イスラエル・ヒズボラ停戦合意——IDFは停戦後も一部攻撃継続と報道｜イラン新設PGSAがホルムズ通航に義務的保険・指定航路を導入——60日無料も将来課金の可能性留保・英国主導で同盟国反発｜通航量改善——6/18に25隻通航（4/18以来最多）・CENTCOM「一晩で20隻超通過」｜WTI $76前後・ブレント $79前後｜封鎖114日目・ニュース4件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月19日 07:55 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/19 07:55</span> — <strong style="color:#fca5a5;">【重大進展】</strong>最高指導者モジュタバ「異なる見解だが承認」表明・本日ビュルゲンシュトック（瑞）で米イラン実務協議——会場をジュネーブから変更・パキスタン首相訪欧キャンセル｜独仏英伊が機雷除去任務参加を共同声明で表明｜IAEA・グロッシ事務局長「技術検証開始」——440kg濃縮ウラン希釈化を監督｜通航実態変化なし・日本関係38隻継続足止め｜WTI $75前後・ブレント $78前後で安値圏継続｜封鎖113日目・ニュース1件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月18日 09:51 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/18 09:51</span> — <strong style="color:#fca5a5;">【重大更新】</strong>MOU14条項全文公開（60日無料通航・30日機雷除去・$3000億復興計画）・6/19ジュネーブ署名式キャンセル確定（電子署名発効確認済：バガエイ外務省報道官）・Goldman Sachs Brent Q4$80下方修正・IEA供給過剰警告・WTI $75前後（5日連続下落・3月来最安値）・日本関係38隻足止め継続・封鎖112日目・ニュース2件更新・OSINT更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ 旧3件目（6/17 08:44）は new_str に含めていません。ブロック2で log-collapse に移動します。

### ブロック2：旧3件目を log-collapse 先頭へ挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月16日 08:14 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月17日 08:44 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/06/17 08:44</span> — アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」警告（6/17）｜イランタンカー2隻（DIONA・HERO2）封鎖圏脱出・3.8百万バレル原油輸出——2ヶ月ぶり｜ファルス「MOU通航無料60日のみ」vs 米「無条件」矛盾浮上｜BIMCO高リスク警告継続・日本関係船舶38隻足止め（日本船主協会）｜WTI $78前後（4日連続下落）｜6/19署名まで2日・封鎖111日目・ニュース2件更新・OSINT更新</div>
          <div>📅 <strong>2026年6月16日 08:14 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### JSON-LD dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-06-19T00:00:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-06-20T08:18:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
[✓] Step 0 — old_str 基準：GitHub raw直接フェッチで6/19 07:55 JST版と完全一致確認（プロジェクト知識2件 + 実ファイル検証）
[✓] C01 タンカー確認 — web検索実施済み・**重要進展**：日本人乗船の日本関係船は全てペルシャ湾外へ退避完了（茂木外相 6/19会見）・残る日本関係船舶37隻（38隻から1隻減）
[✓] S01 ヘッダー — 6月19日 07:55 JST → 6月20日 08:18 JST・警戒レベル「高（MOU実施に動揺・協議延期）」
[✓] S02 TICKER — 協議延期・イスラエル/ヒズボラ停戦・PGSA保険義務化・通航量改善・114日目
[✓] S03 速報インシデント — 6/20 08:18付け・旧ヘッドラインを<li>として保存（漏れ防止）
[✓] S04 情勢カード3枚 — 外交（協議延期・レバノン情勢）・海運（PGSA保険制度・通航量改善）・市場（油価下落基調）
[✓] S05 COUNTDOWN — 114日目・Phase 10継続
[✓] S06 シナリオ確率補足バナー — 6/20 08:18 JST・A↑↑↑↑↑（1段階減）B↑↑（1段階増）C↓↓↓（1段階増）D↓↓↓↓（1段階増）・根拠更新
[✓] S07 シナリオ4本 — A/B/C/D本文を6/20情勢に更新（協議延期・PGSA・レバノン停戦・通航量改善を反映）
[✓] S07 C/D差別化 — C（イスラエル/レバノン問題→実施停止型）vs D（核交渉決裂→一方的破棄型）✓維持
[✓] S07 WTI差別化 — A: $65-75 / B: $80-90 / C: $100-120 / D: $130+ ✓維持
[✓] S08 シナリオフッター — 5焦点を協議再開日程・レバノン停戦履行・PGSA保険問題中心に更新
[✓] S08.5 全ルート現況サマリー — 6/20 08:18 JST 更新（通航量改善の兆しを明記）
[✓] MAP補足 — SHIP_CONFIG totalShips 38→37・dateConfirmedに日本人乗船船全退避完了を反映（6/20時点）
[✓] S09 30秒カラム — 3行サマリー＋バッジ4枚更新（最後に作成）
[✓] S10 news_data.json — latest 4件新規（協議延期・PGSA保険・レバノン停戦・通航量改善）・osint 1件新規
[✓] S10 URL確認済 — NBC News ✓ Middle East Eye ✓ The Hill ✓ CBS News ✓ Al Jazeera（osintのみ）✓（いずれも実在確認済・捏造なし）
[✓] S10 osint — 配列先頭に新規追加・既存 osint-001-0619 の isLatest:true → false 変更 ✓
[✓] S11 更新ログ — 2ブロック構成（常時表示3件固定・log-collapse先頭に6/17版挿入）
[✓] S11 JSON-LD — 2026-06-20T08:18:00+09:00（ISO 8601 JST形式）✓
[✓] 全体 — 📰関連最新ニュースにAl Jazeera混入なし ✓（AJはosintのみ・latestには未使用）
[✓] 全体 — 習近平 表記なし（本日言及なし）✓
[✓] 全体 — Wikipedia/毎日新聞 URL 不使用 ✓
[✓] 全体 — シナリオ確率数値 記載なし（自動同期・矢印のみ） ✓
[✓] 全体 — TICKER内JST表記あり ✓
[✓] 全体 — 「二重封鎖」単独使用なし ✓

【参考・今回スコープ外】S11 log-collapse内の総エントリー数が既に10件超過状態（過去セッションからの蓄積）。本日は2ブロック構成ルールのみ遵守し、件数整理（11件目以降の削除・update_log.json移動）は別タスクとして次回以降に対応を検討。
```

---

## 🔑 本日の重要事項まとめ（Claude Code 参照用）

| 項目 | 内容 |
|---|---|
| **最重要①** | **米イラン実務協議（ビュルゲンシュトック）が延期**——レバノンでのイスラエル攻撃激化が理由・バンス副大統領のスイス訪問もキャンセル・新日程未定 |
| **最重要②** | **イラン新設PGSAがホルムズ通航に義務的保険・指定航路を導入**——60日間無料も将来課金の可能性を留保・英国主導で同盟国反発 |
| **最重要③** | **日本人乗船の日本関係船舶は全てペルシャ湾外への退避が完了**——茂木外相6/19会見。残る日本関係船舶37隻（38隻から1隻減・日本人乗船なし） |
| 新展開① | イスラエル・ヒズボラが停戦合意——トランプの要請で実現も、IDFは停戦後も一部攻撃継続と報道 |
| 新展開② | 通航量に改善の兆し——6/18に検証済み商船25隻通航（4/18以来最多）・CENTCOM「一晩で20隻超通過」・紛争後初のサウジ所有タンカー通過 |
| 新展開③ | イラン、レバノン攻撃停止なければMOU停止・対イスラエル無警告反撃も辞さずと米に警告（Drop Site報道） |
| モジュタバ声明詳細 | 「個人的には異なる意見」としつつ大統領・SNSCの責任保証を条件に承認。IRGCは違反時「より大きな歴史的敗北」を与える用意があると警告 |
| 日本関係船舶 | **37隻**が湾内足止め継続——日本人乗船船は全退避完了（外務省・茂木外相会見 6/19） |
| 油価 | WTI $76前後・ブレント $79前後（週間で約8〜10%下落） |
| 封鎖日数 | **114日目** |

---

## 次ステップ

1. `run.bat` 実行 → `index_html_diffs.md` push
2. Claude Code 定型文送信：
   「git pull --rebase してから、docs/tools/index_html_diffs.md に従って docs/index.html を更新してください。また docs/data/news_data.json も最新版がpush済みです。更新完了後に commit してください。push は確認後に指示します。」
3. ⚠️ S03 速報インシデントの old_str は `grep -n "6月19日 07:55 速報\|6/19 07:55 更新"` で確認すること
4. ⚠️ S04・S05・S06・S07・S08・S08.5・S09・MAP補足 の old_str は view_range/grep で確認すること
5. ⚠️ S11 ブロック2：log-collapse先頭に 6/17 08:44 が既存かどうか `grep -n "6月17日 08:44"` で確認し、既に存在する場合はブロック2をスキップ（二重挿入防止）
6. commit 確認（`git branch && git log --oneline -3`）→ push 指示
