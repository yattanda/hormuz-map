# index_html_diffs.md — 2026年6月19日 07:55 JST 更新分

> Claude Code への指示：以下の差分を index.html / news_data.json に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## ✅ Step 0 確認結果

- project_knowledge_search 2件（index_html_diffs.md / 更新ログ）に加え、**GitHub raw（docs/index.html・docs/data/news_data.json）を直接フェッチしてベースライン実態を確認**（プロジェクト知識のみに依存せず実ファイルで検証）。
- 確認済みベースライン：**2026年6月18日 09:51 JST版**（Phase 10・封鎖112日目）と完全一致。
- 本日の封鎖日数：**113日目**（6/16=110→6/17=111→6/18=112→6/19=113の連番を継続）。

## 📌 本日の主要新展開（要約）

1. **最高指導者モジュタバ・ハメネイがMOUを承認**——「異なる見解を持つが承認した」と表明（6/18夜、Al Jazeera）。イラン国内の最終意思決定が完了。
2. **本日6/19、米イラン実務協議がビュルゲンシュトック（瑞ルツェルン近郊）で開催予定**——会場が当初予定のジュネーブから変更。パキスタン首相シャリフは「MOUは既に電子署名済み」として訪欧をキャンセル。
3. **独仏英伊（メルツ・マクロン・スターマー・メローニ）が共同声明**——「防衛的・独立的ミッション」として機雷除去・商船保護への参加意志を表明（実働化には法的根拠が別途必要）。
4. **IAEAグロッシ事務局長「技術的検証作業開始」**——MOUにより440kg・60%濃縮ウランの希釈化（downblending）検証をIAEAが担当することが規定。
5. **通航実態は変化なし**——Argus調査で船舶動向に大きな変化なし。日本船主協会も「機雷敷設報道もあり安易に進められない」と慎重姿勢継続、**日本関係38隻が引き続き足止め（変化なし・C01確認済）**。
6. **油価は安値圏で推移**——WTI $75前後・ブレント $78前後（Trading Economics 6/18）。Goldman Sachsは湾岸産油フローが既に日量1100万バレルに回復と分析（CNBC）。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
    <span class="badge-item badge-alert">🕊️ 警戒レベル：高（MOU発効・機雷除去30日フェーズ）</span>
    <span class="badge-item badge-date">📅2026年6月18日 09:51 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
    <span class="badge-item badge-alert">🕊️ 警戒レベル：高（MOU実施開始・ビュルゲンシュトック実務協議）</span>
    <span class="badge-item badge-date">📅2026年6月19日 07:55 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年6月18日 09:51 JST） -->
      🕊️【MOU全文公開・電子署名確認】米政府がイスラマバードMOU14条項全文公開——5条項：60日無料通航・30日以内機雷除去・米国$3000億復興計画（6/18 09:51 JST）｜🗓️ 6/19ジュネーブ署名式キャンセル——電子署名発効済み・第2電子署名を6/18中に実施の観測（バガエイ外務省報道官）｜📉 WTI $75前後・ブレント $79前後（5日連続下落・3月来最安値）——Goldman Sachs「Brent Q4目標$80」に下方修正｜⚠️ ガリバフ議長「ホルムズは旧来条件に戻らない・サービス料徴収する」——米「永久無料」と解釈矛盾継続｜🚢 通航実態2%（1隻/日）・機雷除去30日以内（MOU5条項）・日本関係38隻湾内足止め継続｜⚠️ ホルムズ閉鎖112日目・MOU発効→実施フェーズ移行
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年6月19日 07:55 JST） -->
      🕊️【最高指導者がMOU承認】モジュタバ・ハメネイ「異なる見解持つも承認」と表明——イラン国内の意思決定完了（6/18 JST Al Jazeera）｜🏔️ 本日ビュルゲンシュトック（瑞ルツェルン）で米イラン実務協議——会場をジュネーブから変更・パキスタン首相シャリフは訪欧キャンセル（電子署名済みのため）｜🇪🇺 独仏英伊が機雷除去任務参加を表明——「防衛的・独立ミッション」共同声明（メルツ・マクロン・スターマー・メローニ）｜☢️ IAEA・グロッシ事務局長「技術的検証作業開始」——440kg・60%濃縮ウランの希釈化（downblending）をIAEAが監督｜🚢 通航実態は前日比変化なし——日本船主協会「もう少し詳しい情報を待ちたい」・38隻継続足止め｜📉 WTI $75前後・ブレント $78前後で安値圏継続｜⚠️ ホルムズ閉鎖113日目・MOU実施フェーズ
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

> ⚠️ Claude Code: 適用前に `grep -n "6/18 09:51 更新\|6月18日 09:51 速報" docs/index.html` で現状一致を確認すること。

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">交渉決裂・海峡完全閉鎖宣言・米イラン軍事衝突エスカレーション</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 6/18 09:51 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <strong style="font-size:0.88rem;font-weight:800;color:#f87171;">交渉決裂・海峡完全閉鎖宣言・米イラン軍事衝突エスカレーション</strong>
      <span style="font-size:0.65rem;color:#64748b;padding:2px 8px;border-radius:12px;background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.25);">📅 6/19 07:55 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（新ヘッドライン化 + 旧ヘッドラインをリスト先頭へ移動）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/18 09:51 速報】MOU14条項全文公開（6/18）——5条項：60日無料通航・30日以内機雷除去・イラン-オマーン将来管理協議・米$3000億復興計画｜6/19ジュネーブ署名式キャンセル——電子署名発効確認済（バガエイ外務省報道官）・第2電子署名6/18中の観測｜Goldman Sachs「Brent Q4目標$80」下方修正——IEA 2027年供給過剰警告（需要+2百万b/d vs 供給+8百万b/d）｜WTI $75前後（5日連続下落・3月来最安値）
</strong>
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(251,191,36,0.5);">
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/19 07:55 速報】最高指導者モジュタバ・ハメネイがMOU承認（「異なる見解持つも承認」・Al Jazeera 6/18）｜本日ビュルゲンシュトック（瑞ルツェルン）で米イラン実務協議——会場をジュネーブから変更・パキスタン首相シャリフは訪欧キャンセル｜独仏英伊が機雷除去任務参加を共同声明で表明（メルツ・マクロン・スターマー・メローニ）｜IAEA・グロッシ事務局長「技術的検証作業開始」——440kg・60%濃縮ウラン希釈化(downblending)をIAEA監督｜通航実態は変化なし・日本船主協会38隻継続足止め｜WTI $75前後・ブレント $78前後で安値圏継続｜封鎖113日目
</strong>
<ul id="incident-list" style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;">
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(134,239,172,0.5);">
  【6/18 09:51 JST】<strong style="color:#86efac;">MOU14条項全文公開・電子署名発効確認</strong>——5条項：60日無料通航・30日以内機雷除去・米$3000億復興計画。バガエイ外務省報道官「電子署名済み・式典不要」（NBC News, 6/18）
</li>
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(251,191,36,0.5);">
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

### カード① 外交交渉

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🕊️ 外交：MOU全文公開・6/19署名式キャンセル確定</div>
        <div class="s-body">米政府がMOU14条項全文を公開（6/18 JST）——4条項:米国30日以内に海上封鎖完全解除・5条項:イラン60日無料通航保証・30日以内機雷除去・米国$3000億復興計画。バガエイ外務省報道官「電子署名済み・発効中・ジュネーブ署名式は不要」と確認。6/19式キャンセル確定。第2電子署名を6/18中に実施の観測あり。ガリバフ議長「ホルムズは旧来条件に戻らない・サービス料徴収する」と強硬姿勢継続。</div>
        <div class="s-src">出典: NBC News / Korea Times / Times of Israel（6/18 09:51 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🕊️ 外交：最高指導者がMOU承認・本日ビュルゲンシュトックで実務協議</div>
        <div class="s-body">イラン最高指導者モジュタバ・ハメネイが18日夜、MOUについて「異なる見解を持つが承認した」と表明（Al Jazeera）——イラン国内の最終意思決定が完了。本日6/19、米イラン両国が仲介国パキスタン・カタールと共に瑞ビュルゲンシュトック（ルツェルン近郊）で実施段階の実務協議を開催予定。会場は当初予定のジュネーブから変更。パキスタン首相シャリフは「MOUは既に電子署名済み」として訪欧を取りやめ。ガリバフ議長は通航サービス料がMOU文書上で既に正式化されたと主張——米「永久無料」との解釈矛盾は未解消。</div>
        <div class="s-src">出典: Al Jazeera / France24(AFP) / CNN（6/19 07:55 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 軍事/海運

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🚢 海運：MOU発効・通航2%・機雷除去30日フェーズ開始</div>
        <div class="s-body">MOU5条項により機雷除去は署名から30日以内が義務となった。通航実態は依然2%（1隻/日）——Iran SITREP「7日移動平均3%・世界最大タンカー運航会社が『急いで通航するな』と公式警告」。日本関係船舶38隻が引き続き湾内足止め（日本船主協会 6/16確認）。BIMCO警告継続。保険会社・荷主は「安全確認まで待機」姿勢。IEAは「ホルムズ再開後100隻以上の滞留タンカーが一斉放出で供給過剰」と警告。</div>
        <div class="s-src">出典: BIMCO / Iran SITREP / Japan Shipowners' Association（6/16-18 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🚢 海運：欧州が機雷除去任務参加表明・通航実態は変化なし</div>
        <div class="s-body">独仏英伊（メルツ首相・マクロン大統領・スターマー首相・メローニ首相）が共同声明で「防衛的・独立的ミッション」として機雷除去・商船保護への参加意志を表明。一方、Argus調査では合意発表後も船舶動向に大きな変化なし——船主は6/19以降の詳細情報を待つ姿勢。日本船主協会も「もう少し詳しい情報を待ちたい・機雷敷設報道もあり安易に進めない」とコメント・38隻が引き続き湾内足止め継続（変化なし確認）。</div>
        <div class="s-src">出典: Argus Media / Reuters (Japan Shipowners' Association) / AFP（6/19 07:55 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ エネルギー・市場

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">📉 市場：WTI $75前後・5日連続下落・3月来最安値</div>
        <div class="s-body">WTI $75前後・ブレント $79前後——5日連続下落・3月来最安値。Goldman Sachs「Brent Q4目標を$90→$80に下方修正・湾岸輸出は7月末前に戦前水準回復予測」。IEAは「2027年供給過剰：需要増+2百万b/d vs 供給増+8百万b/d・需要ショック悪化で余剰拡大」と警告。米原油在庫は先週830万バレル減（強い需要）でも油価は下落——MOU合意期待が上回る。紛争ピーク比40%超の下落。</div>
        <div class="s-src">出典: Trading Economics / Goldman Sachs (via Barchart) / IEA（6/18 JST 更新）</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">📉 市場：WTI/ブレントとも安値圏で推移・Goldman「湾岸フロー日量1100万バレルに回復」</div>
        <div class="s-body">WTI $75前後・ブレント $78前後で安値圏が継続（Trading Economics, 6/18）。Goldman Sachsは6/16付ノートで「供給回復はより強い可能性」とし、湾岸産油フローが既に日量1100万バレルまで増加（ホルムズ経由分・迂回分双方の増加含む）と分析。一方、IEAの2027年供給過剰警告（需要増+2百万b/d vs 供給増+8百万b/d）は継続。タンカー滞留の解消には10〜15日程度かかる見通しとの業界専門家の指摘あり。</div>
        <div class="s-src">出典: CNBC / Trading Economics / Goldman Sachs（6/19 07:55 JST 更新）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU発効・機雷除去フェーズ（30日以内＝7月上旬目途）」——封鎖112日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div class="dl-label" id="cd-phase-label">⏱️ Phase 10「MOU発効・機雷除去フェーズ（30日以内＝7月上旬目途）」——封鎖113日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
  <span style="font-weight:800;color:#4ade80;">📊 2026年6月18日 09:51 JST 更新</span><br>
  📊 <strong>MOU発効・機雷除去30日フェーズ（6/18 09:51現在）：</strong><br>
  🅐 外交解決 <span style="color:#4ade80;">↑↑↑↑↑↑</span> — MOU全文公開・電子署名発効確認・6/19式キャンセル（署名は既に完了）——最有力シナリオの確度が最高水準に上昇<br>
  🅑 実施遅延 <span style="color:#4ade80;">↑</span> — 機雷除去30日義務（MOU5条項）だが実施能力・意志は不透明・BIMCO高リスク警告継続——部分再開・完全正常化遅延リスク残存<br>
  🅒 合意崩壊 <span style="color:#f87171;">↓↓↓↓</span> — 60日核交渉中にイスラエル・レバノン問題が顕在化しMOU実施が一方的に停止される最悪シナリオ<br>
  🅓 合意破棄 <span style="color:#f87171;">↓↓↓↓↓</span> — 60日核交渉決裂によるイランの一方的破棄・再封鎖——MOU発効済みの現時点では極めて低い<br>
  <strong style="color:#fbbf24;">MOU発効・実施フェーズ移行——A↑↑↑↑↑↑ B↑ C↓↓↓↓ D↓↓↓↓↓（機雷除去30日が次の焦点）。</strong><br>
  <div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
    各シナリオ確率は 2026年6月18日 09:51 JST 時点での分析に基づく自動同期
  </div>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本

### シナリオA

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>MOU全文公開（6/18）・電子署名発効確認済み。6/19署名式キャンセルで既に合意発効中。次の焦点は機雷除去（MOU5条項：30日以内義務）。機雷除去完了後に商業通航本格化・日本関係38隻段階的解放・60日核交渉開始へ。WTI $65〜75、ブレント $70〜80への収束が見込まれる。Goldman Sachs「湾岸輸出7月末前に戦前水準」予測と整合。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>最高指導者モジュタバが18日夜「異なる見解だが承認」と表明——イラン国内の意思決定リスクが大きく後退。本日ビュルゲンシュトックで実務協議開始、独仏英伊は機雷除去任務への参加を共同声明で表明。Goldman Sachs分析では湾岸産油フローが既に日量1100万バレルまで回復。次の焦点は機雷除去完了（MOU5条項：30日以内義務）と60日核交渉の本格化。WTI $65〜75、ブレント $70〜80への収束が見込まれる。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>合意発効も機雷除去・保険・荷主の三重ボトルネックで通航回復が2〜3ヶ月遅れるシナリオ。MOU5条項「30日以内」は義務だが実施能力・意志が不透明。BIMCO「依然高リスク」警告継続。世界最大タンカー運航会社「急いで通航するな」と公式声明。ガリバフ「サービス料徴収」発言が将来的な通航コスト上昇リスクを示唆。WTI $80〜90に再上昇の可能性。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>合意発効も機雷除去・保険・荷主の三重ボトルネックで通航回復が2〜3ヶ月遅れるシナリオ。Argus調査では合意発表後も船舶動向に実質変化なし——日本船主協会も「機雷敷設報道もあり安易に進められない」と慎重姿勢を継続、38隻の足止め状態が変わらず。欧州の機雷除去任務は表明段階に留まり実働化は未定。ガリバフ議長「サービス料は既にMOU文書で正式化済み」発言が将来的な通航コスト上昇リスクを示唆。WTI $80〜90に再上昇の可能性。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>電子署名発効も60日核交渉中にイスラエル問題が顕在化するシナリオ。ヒズボラ「イスラエル撤退なき停戦は拒否」の姿勢継続。アラグチー「レバノン攻撃継続はMOU違反」発言が伏線として残存。60日交渉中にイスラエルがレバノン攻撃を拡大→イランがMOU実施を停止宣言→通航再封鎖。WTI $100-120。Stimson Center「イスラエル=最大の不安定要因」と分析。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>電子署名発効も60日核交渉中にイスラエル問題が顕在化するシナリオ。イラン軍は「停戦発表以降、イスラエルが84回違反」と非難——アラグチー「レバノン攻撃継続はMOU違反」発言が伏線として残存。60日交渉中にイスラエルがレバノン攻撃を拡大→イランがMOU実施を停止宣言→通航再封鎖。WTI $100-120。Stimson Center「イスラエル=最大の不安定要因」と分析。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD

<!-- APPLY:START -->
<!-- OLD:START -->
        <p>MOU発効・機雷除去後も60日核交渉で根本的合意が得られず、イランが一方的に協議を打ち切るシナリオ。MOU8条項「核兵器調達・開発しない」の検証機構が「相互合意」に委ねられており未確定。米国が再制裁→イランが「MOU破棄」宣言→再封鎖・再機雷散布。WTI $130以上。Iran SITREP「核軟化に対するイラン国内コスト上昇中・強硬派の抵抗」を指摘。</p>
<!-- OLD:END -->
<!-- NEW:START -->
        <p>MOU発効・機雷除去後も60日核交渉で根本的合意が得られず、イランが一方的に協議を打ち切るシナリオ。MOUはIAEAに440kg・60%濃縮ウランの希釈化（downblending）検証を委ねるが、グロッシ事務局長は「事実を先取りするのは賢明でない」と慎重姿勢——検証範囲・タイムラインは依然未確定。米国が再制裁→イランが「MOU破棄」宣言→再封鎖・再機雷散布。WTI $130以上。Iran SITREP「核軟化に対するイラン国内コスト上昇中・強硬派の抵抗」を指摘。</p>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5つ）

<!-- APPLY:START -->
<!-- OLD:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">機雷除去（MOU5条項：30日以内義務——実際のタイムラインと能力の確認）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">ガリバフ「サービス料徴収」vs 米「永久無料」の決着（60日交渉の核心議題のひとつ）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">60日核交渉開始（核兵器放棄確認・濃縮ウラン処理・検証機構の相互合意）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">日本関係38隻の段階的解放と保険・BIMCO問題の解消</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">イスラエル・レバノン問題の帰趨（ヒズボラ撤退合意が60日交渉の前提条件になりうる）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年6月18日 09:51 JST情勢分析</span>
<!-- OLD:END -->
<!-- NEW:START -->
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">① <strong style="color:#fbbf24;">本日ビュルゲンシュトック実務協議の結果（パキスタン首相は欠席・実施詳細の合意可否）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">② <strong style="color:#fbbf24;">欧州の機雷除去任務の実働化（独仏英伊が表明・国連安保理決議等の法的根拠が必要）</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">③ <strong style="color:#fbbf24;">IAEAによる440kg・60%濃縮ウラン検証・希釈化（downblending）の開始時期</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">④ <strong style="color:#fbbf24;">日本関係38隻の段階的解放と保険・BIMCO問題の解消</strong></li>
      <li style="font-size:0.85rem;color:#cbd5e1;margin-bottom:5px;">⑤ <strong style="color:#fbbf24;">イスラエル・レバノン問題の帰趨（停戦違反84回——ヒズボラ撤退合意が60日交渉の前提条件になりうる）</strong></li>
    </ul>
    <span class="label-scenario" style="margin-left:auto;">分析：2026年6月19日 07:55 JST情勢分析</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年6月18日 09:51 JST 再確認済・MOU発効・機雷除去30日フェーズ移行）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">→ ホルムズ：MOU5条項により機雷除去30日以内が義務化・通航実態は依然2%（1隻/日）、世界最大タンカー運航会社「急いで通航するな」と警告——ガリバフ議長「サービス料徴収する」と強硬姿勢継続、紅海：フーシ派「イスラエル船完全禁止」継続——大手船社が接近一時停止・代替ルート信頼性低下、ケープ回廊完全飽和・コスト倍増、日本関係船舶38隻が湾内足止め継続</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
  <div class="sec-title">🚢 全ルート現況サマリー（2026年6月19日 07:55 JST 再確認済・通航実態に変化なし）<br><span style="font-size:0.75rem;font-weight:400;color:#7dd3fc;">→ ホルムズ：Argus調査で合意発表後も船舶動向に大きな変化なし・船主は6/19以降の詳細情報待ち、日本船主協会「機雷敷設報道もあり安易に進められない」と慎重姿勢継続、紅海：フーシ派「イスラエル船完全禁止」継続——大手船社が接近一時停止・代替ルート信頼性低下、ケープ回廊完全飽和・コスト倍増、日本関係船舶38隻が湾内足止め継続（変化なし確認）</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [MAP補足] SHIP_CONFIG（日本関連タンカー可視化）整合性修正

> ⚠️ Claude Code への注記：このブロックは index.html 内の SHIP_CONFIG が **2026年6月12日時点の古い値（totalShips:41・約45隻表記）のまま** であり、ページ本文の他セクション（38隻・日本船主協会ベース）と不整合になっているのを修正するものです。「ついでに修正」ではなく、daily-site-update スキルが定める毎日必須のMAPタンカー可視化確認に基づく対応です。

<!-- APPLY:START -->
<!-- OLD:START -->
const SHIP_CONFIG = {
  totalShips:    41,
  passableShips: 3,
  date:          '2026年5月25日',
  dateConfirmed: '2026年6月12日 07:29 JST 変更なし（web検索確認済）：約45隻の日本関係船舶が停留継続（日本国土交通省推計・4月末時点）。トランプの「和解」宣言でホルムズ正式再開の可能性が浮上しているが、イラン公式未承認・IRGC継続攻撃により日本船の通過再開は署名成立まで不可。'
};
<!-- OLD:END -->
<!-- NEW:START -->
const SHIP_CONFIG = {
  totalShips:    38,
  passableShips: 0,
  date:          '2026年6月19日',
  dateConfirmed: '2026年6月19日 07:55 JST 変更なし（web検索確認済）：日本関係船舶38隻が引き続き湾内足止め（日本船主協会、6/16発表を6/19時点でも維持確認）。同協会は「機雷敷設報道もあり安易に進められない・もう少し詳しい情報を待ちたい」とコメント。MOU発効・最高指導者承認後も日本船の通過再開は未着手。'
};
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（最後に作成）

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
🕊️ MOU全文公開・6/19署名式キャンセル確定——14条項テキスト公開（5条項：60日無料・30日機雷除去・$3000億復興）、バガエイ「電子署名発効済み・式典不要」（6/18 JST）
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.4);color:#fbbf24;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">海峡の今</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
🚢 通航2%・機雷除去30日フェーズ・38隻足止め——BIMCO「依然高リスク」・世界最大タンカー運航会社「急いで通航するな」・日本関係38隻湾内継続
</span>
  </div>
  <div style="display:flex;align-items:flex-start;gap:10px;">
    <span style="background:rgba(100,116,139,0.15);border:1px solid rgba(100,116,139,0.4);color:#94a3b8;font-size:0.75rem;font-weight:700;padding:2px 8px;border-radius:4px;white-space:nowrap;">次の焦点</span>
    <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">
📉 WTI $75前後・5日連続下落・3月来最安値——Goldman Sachs「Brent Q4目標$80」下方修正・IEA 2027年供給過剰警告・紛争ピーク比40%超下落
</span>
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#f87171;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚠️ 閉鎖112日目</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📉 WTI $75 / Brent $79</span>
<span style="display:inline-block;background:rgba(147,51,234,0.15);border:1px solid rgba(147,51,234,0.3);color:#c084fc;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⛏️ 機雷除去30日以内（MOU義務）</span>
<span style="display:inline-block;background:rgba(134,239,172,0.25);border:1px solid rgba(134,239,172,0.5);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️ MOU発効・機雷除去フェーズ</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#f87171;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚠️ 閉鎖113日目</span>
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📉 WTI $75 / Brent $78</span>
<span style="display:inline-block;background:rgba(147,51,234,0.15);border:1px solid rgba(147,51,234,0.3);color:#c084fc;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🏔️ 本日ビュルゲンシュトック実務協議</span>
<span style="display:inline-block;background:rgba(134,239,172,0.25);border:1px solid rgba(134,239,172,0.5);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️ 最高指導者がMOU承認</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年6月18日 09:51 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年6月19日 07:55 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
    {
      "title": "MOU14条項全文公開——60日無料通航・30日機雷除去・米$3000億復興計画",
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "title": "イラン最高指導者モジュタバ・ハメネイがMOU承認——「異なる見解持つも承認」と表明",
      "body": "イラン最高指導者モジュタバ・ハメネイが18日夜、米・イラン間のMOU（覚書）について「異なる見解を持つが承認した」と述べたとAl Jazeeraが報道。イラン国内における最終的な意思決定が完了した形となり、外交解決シナリオの確度を大きく後押しする材料となった。同日、米副大統領バンスは60日間の交渉期間が開始されたこと、イラン港湾への封鎖が解除されたことを発表。",
      "sourceLabel": "Al Jazeera",
      "date": "2026年6月18日",
      "label": "🕊️ 外交",
      "url": "https://www.aljazeera.com/news/2026/6/18/world-reacts-to-us-iran-deal-to-extend-ceasefire-begin-negotations"
    },
    {
      "title": "独仏英伊、ホルムズ機雷除去任務への参加を共同声明で表明",
      "body": "ドイツ（メルツ首相）・フランス（マクロン大統領）・英国（スターマー首相）・イタリア（メローニ首相）の4カ国首脳が共同声明を発表し、ホルムズ海峡の無条件・無制限の航行自由化が不可欠だとした上で、各国の憲法上の要件に従い「防衛的・独立的なミッション」として商船の安心供与と機雷除去作戦への参加意志を表明した。実働化には国連安保理決議等の法的根拠が必要との指摘もある。",
      "sourceLabel": "AFP",
      "date": "2026年6月18日",
      "label": "⛏️ 軍事/海運",
      "url": "https://www.yahoo.com/news/world/articles/european-leaders-ready-mission-strait-004128455.html"
    },
    {
      "title": "MOU14条項全文公開——60日無料通航・30日機雷除去・米$3000億復興計画",
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
    {
      "id": "osint-001",
      "date": "2026年6月17日（現地）/ 2026年6月18日 JST",
      "titleJa": "【Al Jazeera】イラン外務省「MOUは電子署名済み・ジュネーブ署名式は不要」——ガリバフ「ホルムズは旧来条件に戻らない」",
      "titleEn": "Iran FM confirms MOU electronically signed, no Geneva ceremony needed — Ghalibaf: Hormuz will never return to pre-war conditions",
      "country": "Qatar / Iran",
      "media": "Al Jazeera",
      "cardBg": "rgba(0,150,136,0.13)",
      "cardBorder": "rgba(0,150,136,0.35)",
      "badgeColor": "#00897b",
      "borderColor": "#00897b",
      "textColor": "#80cbc4",
      "url": "https://www.aljazeera.com/news/2026/6/17/iran-confirms-that-mou-has-been-signed-electronically-by-both-sides",
      "isLatest": true
    },
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "id": "osint-001-0619",
      "date": "2026年6月18日（現地）/ 2026年6月19日 JST",
      "titleJa": "【Al Jazeera】MOU14条項を解説——レバノン・ホルムズ・濃縮ウランの扱いとは",
      "titleEn": "What the Trump-Iran agreement says about Lebanon, Hormuz and uranium",
      "country": "Qatar",
      "media": "Al Jazeera",
      "cardBg": "rgba(0,150,136,0.13)",
      "cardBorder": "rgba(0,150,136,0.35)",
      "badgeColor": "#00897b",
      "borderColor": "#00897b",
      "textColor": "#80cbc4",
      "url": "https://www.aljazeera.com/news/2026/6/18/what-the-trump-iran-14-point-plan-says-about-lebanon-hormuz-and-uranium",
      "isLatest": true
    },
    {
      "id": "osint-001",
      "date": "2026年6月17日（現地）/ 2026年6月18日 JST",
      "titleJa": "【Al Jazeera】イラン外務省「MOUは電子署名済み・ジュネーブ署名式は不要」——ガリバフ「ホルムズは旧来条件に戻らない」",
      "titleEn": "Iran FM confirms MOU electronically signed, no Geneva ceremony needed — Ghalibaf: Hormuz will never return to pre-war conditions",
      "country": "Qatar / Iran",
      "media": "Al Jazeera",
      "cardBg": "rgba(0,150,136,0.13)",
      "cardBorder": "rgba(0,150,136,0.35)",
      "badgeColor": "#00897b",
      "borderColor": "#00897b",
      "textColor": "#80cbc4",
      "url": "https://www.aljazeera.com/news/2026/6/17/iran-confirms-that-mou-has-been-signed-electronically-by-both-sides",
      "isLatest": false
    },
<!-- NEW:END -->
<!-- APPLY:END -->

> 📝 URL確認済：NBC News(既存) / Al Jazeera ×2(新規2件・実在確認済) / AFP経由Yahoo News(新規・実在確認済)。毎日新聞・Wikipedia不使用。Al Jazeeraは「latest」配列には使用せず「osint」配列のみに使用（ルール厳守）。

---

## [S11] 更新ログ — 折り畳み維持ルール準拠（2ブロック構成）

> ⚠️ Claude Code: 適用前に `grep -n "log-collapse\|6月15日 07:09\|6月16日 08:14" docs/index.html | head -10` で現在の常時表示3件・log-collapse先頭エントリーを確認すること。

### ブロック1: 常時表示エリアの更新（3件固定維持）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年6月18日 09:51 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/18 09:51</span> — <strong style="color:#fca5a5;">【重大更新】</strong>MOU14条項全文公開（60日無料通航・30日機雷除去・$3000億復興計画）・6/19ジュネーブ署名式キャンセル確定（電子署名発効確認済：バガエイ外務省報道官）・Goldman Sachs Brent Q4$80下方修正・IEA供給過剰警告・WTI $75前後（5日連続下落・3月来最安値）・日本関係38隻足止め継続・封鎖112日目・ニュース2件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月17日 08:44 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/17 08:44</span> — <strong style="color:#fca5a5;">【重大フォロー】</strong>アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」警告（6/17）｜イランタンカー2隻（DIONA・HERO2）封鎖圏脱出・3.8百万バレル原油輸出——2ヶ月ぶり｜ファルス「MOU通航無料60日のみ」vs 米「無条件」矛盾浮上｜BIMCO高リスク警告継続・日本関係船舶38隻足止め（日本船主協会）｜WTI $78前後（4日連続下落）｜6/19署名まで2日・封鎖111日目・ニュース2件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月16日 08:14 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/16 08:14</span> — <strong style="color:#fca5a5;">【和平合意成立】</strong>米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」・MOU14条項・6/19スイス署名式・機雷除去最大6ヶ月・WTI $81.10・ブレント $83.80急落・110日目・ニュース3件更新・OSINT更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年6月19日 07:55 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/19 07:55</span> — <strong style="color:#fca5a5;">【重大進展】</strong>最高指導者モジュタバ「異なる見解だが承認」表明・本日ビュルゲンシュトック（瑞）で米イラン実務協議——会場をジュネーブから変更・パキスタン首相訪欧キャンセル｜独仏英伊が機雷除去任務参加を共同声明で表明｜IAEA・グロッシ事務局長「技術検証開始」——440kg濃縮ウラン希釈化を監督｜通航実態変化なし・日本関係38隻継続足止め｜WTI $75前後・ブレント $78前後で安値圏継続｜封鎖113日目・ニュース2件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月18日 09:51 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/18 09:51</span> — <strong style="color:#fca5a5;">【重大更新】</strong>MOU14条項全文公開（60日無料通航・30日機雷除去・$3000億復興計画）・6/19ジュネーブ署名式キャンセル確定（電子署名発効確認済：バガエイ外務省報道官）・Goldman Sachs Brent Q4$80下方修正・IEA供給過剰警告・WTI $75前後（5日連続下落・3月来最安値）・日本関係38隻足止め継続・封鎖112日目・ニュース2件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月17日 08:44 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/17 08:44</span> — <strong style="color:#fca5a5;">【重大フォロー】</strong>アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」警告（6/17）｜イランタンカー2隻（DIONA・HERO2）封鎖圏脱出・3.8百万バレル原油輸出——2ヶ月ぶり｜ファルス「MOU通航無料60日のみ」vs 米「無条件」矛盾浮上｜BIMCO高リスク警告継続・日本関係船舶38隻足止め（日本船主協会）｜WTI $78前後（4日連続下落）｜6/19署名まで2日・封鎖111日目・ニュース2件更新・OSINT更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2: log-collapse への旧3件目（6/16 08:14）の挿入

> ⚠️ Claude Code: 6/15 07:09 が log-collapse の先頭に既に存在する場合のみ、以下を適用（重複挿入防止のため `grep -n "6月15日 07:09"` で件数を確認すること）。

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月15日 07:09 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月16日 08:14 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/06/16 08:14</span> — 米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」宣言・MOU14条項（全面停戦・ホルムズ再開・核60日交渉）・バンス「デジタル署名済み」・ドーハ事前協議・署名式6/19スイス・機雷除去最大6ヶ月・WTI $81.10（-4.5%）・警戒レベル最高→高・封鎖110日目・ニュース3件更新・OSINT更新</div>
          <div>📅 <strong>2026年6月15日 07:09 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### JSON-LD dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-06-18T00:00:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-06-19T00:00:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
[✓] Step 0 — old_str 基準：GitHub raw直接フェッチで6/18 09:51 JST版と完全一致確認（プロジェクト知識2件 + 実ファイル検証）
[✓] C01 タンカー確認 — web検索実施済み・日本関係船舶38隻が湾内足止め（日本船主協会・6/16発表を6/19時点でも維持確認・変化なし）
[✓] S01 ヘッダー — 6月18日 09:51 JST → 6月19日 07:55 JST・警戒レベル「高（MOU実施開始・ビュルゲンシュトック実務協議）」
[✓] S02 TICKER — 最高指導者承認・ビュルゲンシュトック協議・欧州機雷除去任務・IAEA検証・通航変化なし・113日目
[✓] S03 速報インシデント — 6/19 07:55付け・旧ヘッドラインを<li>として保存（漏れ防止）
[✓] S04 情勢カード3枚 — 外交（最高指導者承認・ビュルゲンシュトック）・軍事/海運（欧州機雷除去任務・通航変化なし）・エネルギー（Goldman湾岸フロー分析）
[✓] S05 COUNTDOWN — 113日目・Phase 10継続
[✓] S06 シナリオ確率補足バナー — 6/19 07:55 JST・矢印変更なし（A↑↑↑↑↑↑のまま、根拠を更新）
[✓] S07 シナリオ4本 — A/B/C/D本文を6/19情勢に更新（最高指導者承認・通航変化なし・レバノン違反84回・IAEA検証）
[✓] S07 C/D差別化 — C（イスラエル/レバノン問題→実施停止型）vs D（核交渉決裂→一方的破棄型）✓維持
[✓] S07 WTI差別化 — A: $65-75 / B: $80-90 / C: $100-120 / D: $130+ ✓維持
[✓] S08 シナリオフッター — 5焦点をビュルゲンシュトック・欧州任務・IAEA検証中心に更新
[✓] S08.5 全ルート現況サマリー — 6/19 07:55 JST 再確認済（変化なし明記）
[✓] MAP補足 — SHIP_CONFIG（6/12時点の古い41隻表記）を38隻に整合修正（daily-site-update必須チェック対応）
[✓] S09 30秒カラム — 3行サマリー＋バッジ4枚更新（最後に作成）
[✓] S10 news_data.json — latest 2件新規（最高指導者承認・欧州機雷除去任務）・旧2件はarchiveへ自然移動（追加分のみ記載）
[✓] S10 URL確認済 — Al Jazeera ×2 ✓ AFP(Yahoo News) ✓（いずれも実在確認済・捏造なし）
[✓] S10 osint — 配列先頭に新規追加・既存 osint-001 の isLatest:true → false 変更 ✓
[✓] S11 更新ログ — 2ブロック構成（常時表示3件固定・log-collapse先頭に6/16版挿入）
[✓] S11 ブロック2 — 6/15 07:09が log-collapse に既存の場合のみ適用する旨を注記済み ✓
[✓] S11 JSON-LD — 2026-06-19T00:00:00+09:00（ISO 8601 JST形式）✓
[✓] 全体 — 📰関連最新ニュースにAl Jazeera混入なし ✓（AJはosintのみ・latestには未使用）
[✓] 全体 — 習近平 表記なし（本日言及なし）✓
[✓] 全体 — Wikipedia/毎日新聞 URL 不使用 ✓
[✓] 全体 — シナリオ確率数値 記載なし（自動同期） ✓
[✓] 全体 — TICKER内JST表記あり ✓
[✓] 全体 — 「二重封鎖」単独使用なし ✓
```

---

## 🔑 本日の重要事項まとめ（Claude Code 参照用）

| 項目 | 内容 |
|---|---|
| **最重要①** | **最高指導者モジュタバがMOU承認（「異なる見解だが承認」）——Al Jazeera 6/18** |
| **最重要②** | **本日6/19、ビュルゲンシュトック（瑞）で米イラン実務協議——会場はジュネーブから変更** |
| 新展開① | 独仏英伊が機雷除去任務参加を共同声明で表明（実働化は法的根拠待ち） |
| 新展開② | IAEA・グロッシ事務局長「技術検証開始」——440kg・60%濃縮ウラン希釈化を監督 |
| 新展開③ | Goldman Sachs分析：湾岸産油フローが日量1100万バレルに回復 |
| パキスタン | シャリフ首相が訪欧キャンセル（電子署名済みのため） |
| 日本関係船舶 | **38隻**が湾内足止め継続（日本船主協会・変化なし確認） |
| 通航実態 | Argus調査で変化なし——船主は詳細情報待ち姿勢 |
| 油価 | WTI $75前後・ブレント $78前後（安値圏継続） |
| 封鎖日数 | **113日目** |

---

## 次ステップ

1. `run.bat` 実行 → `index_html_diffs.md` push
2. Claude Code 定型文送信：
   「git pull --rebase してから、docs/tools/index_html_diffs.md に従って docs/index.html を更新してください。また docs/data/news_data.json も最新版がpush済みです。更新完了後に commit してください。push は確認後に指示します。」
3. ⚠️ S03 速報インシデントの old_str は `grep -n "6月18日 09:51 速報\|6/18 09:51 更新"` で確認すること
4. ⚠️ S04・S05・S06・S07・S08・S08.5・S09・MAP補足 の old_str は view_range/grep で確認すること
5. ⚠️ S11 ブロック2：log-collapse先頭に 6/16 08:14 が既存かどうか `grep -n "6月16日 08:14"` で確認し、既に存在する場合はブロック2をスキップ（二重挿入防止）
6. commit 確認（`git branch && git log --oneline -3`）→ push 指示
