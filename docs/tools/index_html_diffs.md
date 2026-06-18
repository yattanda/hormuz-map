# index_html_diffs.md — 2026年6月18日 09:51 JST 更新分

> Claude Code への指示：以下の差分を `docs/index.html` に適用してください。
> 変更箇所以外は絶対に触らないこと。
> `docs/data/news_data.json` は [S10] の指示に従い、既存ファイルに対して新規追加分をマージする形で更新してください。
> 更新完了後に commit してください。push は確認後に指示します。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
        <span class="badge-item badge-alert">🕊️ 警戒レベル：高（署名2日前・機雷除去待ち）</span>
        <span class="badge-item badge-date">📅2026年6月17日 08:44 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
        <span class="badge-item badge-alert">🕊️ 警戒レベル：高（MOU発効・機雷除去30日フェーズ）</span>
        <span class="badge-item badge-date">📅2026年6月18日 09:51 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 新ティッカー（2026年6月17日 08:44 JST） -->
      🇮🇷【アラグチー警告】「イスラエルのレバノン攻撃・占領継続はMOU違反」——署名式6/19スイス2日前に最大リスク浮上（6/17 08:21 JST）｜🚢 イランタンカー2隻（DIONA・HERO2）が封鎖圏脱出——3.8百万バレル原油輸出・2ヶ月ぶりのイラン原油輸出（6/17 JST）｜⚠️ ファルス通信「MOU通航無料は60日間のみ・その後有料化」vs 米「無条件無料」——解釈矛盾継続｜🛡️ BIMCO「MOU後もホルムズ通航は依然高リスク」・日本関係船舶38隻が湾内足止め（日本船主協会 6/16）｜📉 WTI $78前後（4日連続下落・3月来最安値圏）・ブレント $80前後｜⚠️ ホルムズ閉鎖111日目・6/19署名まで2日
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 新ティッカー（2026年6月18日 09:51 JST） -->
      🕊️【MOU全文公開・電子署名確認】米政府がイスラマバードMOU14条項全文公開——5条項：60日無料通航・30日以内機雷除去・米国$3000億復興計画（6/18 09:51 JST）｜🗓️ 6/19ジュネーブ署名式キャンセル——電子署名発効済み・第2電子署名を6/18中に実施の観測（バガエイ外務省報道官）｜📉 WTI $75前後・ブレント $79前後（5日連続下落・3月来最安値）——Goldman Sachs「Brent Q4目標$80」に下方修正｜⚠️ ガリバフ議長「ホルムズは旧来条件に戻らない・サービス料徴収する」——米「永久無料」と解釈矛盾継続｜🚢 通航実態2%（1隻/日）・機雷除去30日以内（MOU5条項）・日本関係38隻湾内足止め継続｜⚠️ ホルムズ閉鎖112日目・MOU発効→実施フェーズ移行
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

### トグルボタン日付

<!-- APPLY:START -->
<!-- OLD:START -->
            📅 6/17 08:44 更新
<!-- OLD:END -->
<!-- NEW:START -->
            📅 6/18 09:51 更新
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭 strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/17 08:44 速報】アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」——署名式6/19前日に最大リスク（6/17 JST）｜イランタンカー2隻（DIONA・HERO2）封鎖圏脱出・3.8百万バレル原油輸出｜ファルス通信「MOU通航無料60日のみ・有料化」vs 米「無条件無料」矛盾継続
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/18 09:51 速報】MOU14条項全文公開（6/18）——5条項：60日無料通航・30日以内機雷除去・イラン-オマーン将来管理協議・米$3000億復興計画｜6/19ジュネーブ署名式キャンセル——電子署名発効確認済（バガエイ外務省報道官）・第2電子署名6/18中の観測｜Goldman Sachs「Brent Q4目標$80」下方修正——IEA 2027年供給過剰警告（需要+2百万b/d vs 供給+8百万b/d）｜WTI $75前後（5日連続下落・3月来最安値）
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ Claude Code: 上記 old_str の先頭 strong タグは `grep -n "6/17 08:44 速報" docs/index.html` で位置確認後に適用すること。

---

## [S04] 情勢カード3枚

> ⚠️ Claude Code: 以下の old_str は各カードの日付・数値部分を中心に記載。`grep -n "6月17日\|アラグチー警告\|タンカー.*脱出\|WTI.*78" docs/index.html` で現在の実態を確認し、完全一致させてから適用すること。

### カード①（外交）— MOU発効・署名式キャンセル

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🕊️ 外交フェーズ：MOU電子署名確認・ドーハ事前協議</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🕊️ 外交フェーズ：MOU全文公開・6/19署名式キャンセル確定</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-body">米イラン和平合意（MOU14条項）成立。トランプ大統領・バンス副大統領・ガリバフ議長が電子署名。6/19スイス・ジュネーブにて正式署名式予定。アラグチー外相「イスラエルのレバノン攻撃継続はMOU違反」と警告——署名式前日に最大リスク要因浮上。ファルス通信「通航無料は60日のみ・その後有料化」vs 米「無条件無料」の解釈矛盾継続。<span class="s-src">出典：NBC News / Al Jazeera / Reuters (6/17 JST)</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-body">米政府がMOU14条項全文を公開（6/18 JST）——4条項:米国30日以内に海上封鎖完全解除・5条項:イラン60日無料通航保証・30日以内機雷除去・米国$3000億復興計画。バガエイ外務省報道官「電子署名済み・発効中・ジュネーブ署名式は不要」と確認。6/19式キャンセル確定。第2電子署名を6/18中に実施の観測あり。ガリバフ議長「ホルムズは旧来条件に戻らない・サービス料徴収する」と強硬姿勢継続。<span class="s-src">出典：NBC News / Korea Times / Times of Israel (6/18 JST)</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード②（軍事/海運）— 通航実態・機雷除去

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🚢 海運フェーズ：タンカー2隻脱出・BIMCO高リスク警告継続</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🚢 海運フェーズ：MOU発効・通航2%・機雷除去30日フェーズ開始</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-body">イランタンカー2隻（DIONA・HERO2）が封鎖圏を脱出——3.8百万バレル原油輸出・2ヶ月ぶりのイラン原油輸出確認（6/17 JST）。ただし商業通航は依然ほぼ閉鎖（通常比約2%）。BIMCO「MOU後もホルムズ通航は依然高リスク」と警告継続。日本船主協会：日本関係船舶38隻が湾内に足止め（6/16）。機雷除去完了まで荷主・保険会社は慎重姿勢を維持。<span class="s-src">出典：Marine Link / Japan Shipowners' Association / BIMCO (6/16-17 JST)</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-body">MOU5条項により機雷除去は署名から30日以内が義務となった。通航実態は依然2%（1隻/日）——Iran SITREP「7日移動平均3%・世界最大タンカー運航会社が「急いで通航するな」と公式警告」。日本関係船舶38隻が引き続き湾内足止め（日本船主協会 6/16確認）。BIMCO警告継続。保険会社・荷主は「安全確認まで待機」姿勢。IEA「ホルムズ再開後100隻以上の滞留タンカーが一斉放出で供給過剰」と警告。<span class="s-src">出典：BIMCO / Iran SITREP / Japan Shipowners' Association (6/16-18 JST)</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③（エネルギー）— 油価急落・Goldman Sachs

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">📉 市場フェーズ：WTI $78前後・4日連続下落</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">📉 市場フェーズ：WTI $75前後・5日連続下落・3月来最安値</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-body">WTI $78前後・ブレント $80前後——4日連続下落・3月来最安値圏。MOU合意期待で原油は紛争ピーク比約40%下落。Goldman Sachs：ブレントQ4目標を$90→$80に下方修正（湾岸輸出が7月末前に戦前水準へ回復との予測に基づく）。IEA警告：2027年供給過剰シナリオ（需要増+2百万b/d vs 供給増+8百万b/d）。米国内ガソリン小売価格が4ドル/ガロンを下回る。<span class="s-src">出典：Trading Economics / Goldman Sachs via Barchart / IEA (6/17-18 JST)</span></div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-body">WTI $75前後・ブレント $79前後——5日連続下落・3月来最安値。Goldman Sachs「Brent Q4目標を$90→$80に下方修正・湾岸輸出は7月末前に戦前水準回復予測」。IEA「2027年供給過剰：需要増+2百万b/d vs 供給増+8百万b/d・需要ショック悪化で余剰拡大」と警告。US原油在庫は先週830万バレル減（強い需要）でも油価は下落——MOU合意期待が上回る。紛争ピーク比40%超の下落。<span class="s-src">出典：Trading Economics / Goldman Sachs (via Barchart) / IEA (6/18 JST)</span></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

> ⚠️ Claude Code: `grep -n "countdown-days\|Phase\|署名" docs/index.html | head -10` で現在の実態を確認後に適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="countdown-days">111</span>日目
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="countdown-days">112</span>日目
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="countdown-phase">Phase 9：6/19スイス署名式まであと2日</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="countdown-phase">Phase 10：MOU発効・機雷除去フェーズ（30日以内 = 7月上旬目途）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー ⚠️（漏れ多発セクション）

> ⚠️ **数値記載禁止** — 矢印・根拠文のみ。確率数値は自動同期。
> ⚠️ Claude Code: `grep -n "補足バナー\|6月17日.*08:44\|矢印" docs/index.html | head -5` で現在の実態を確認後に適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="scenario-banner-date">2026年6月17日 08:44 JST 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="scenario-banner-date">2026年6月18日 09:51 JST 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="scenario-banner-text">A↑↑↑↑↑↑ — MOU電子署名確認・6/19スイス式確定で和平合意シナリオ確度がさらに上昇。ただしアラグチー「イスラエル攻撃継続=MOU違反」警告が唯一のダウンサイドリスク。</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="scenario-banner-text">A↑↑↑↑↑↑ — MOU全文公開・電子署名発効確認・6/19式キャンセル（署名既完了）で和平合意シナリオ確度が最高水準へ。実施フェーズ移行により機雷除去30日が次の焦点。</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（タイトル・本文）

> ⚠️ Claude Code: `grep -n "sc-title\|sc-body\|sc-tag" docs/index.html | head -20` で現在の実態を確認後に適用すること。

### シナリオA（和平合意・段階的再開）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-title">🕊️ シナリオA：MOU署名→機雷除去→段階的再開</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-title">🕊️ シナリオA：MOU発効→機雷除去（30日）→段階的再開→60日核交渉</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-body"><p>MOU電子署名確認済み。6/19スイス・ジュネーブ正式署名式後にホルムズ通航再開が本格化。機雷除去（西側推定40〜50日・MOU上30日以内）→60日核交渉開始の流れ。日本関係38隻の段階的解放、原油・LNG輸出再開、WTI $65〜75への収束が見込まれる。イスラエル・レバノン問題が唯一の不確定要素。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-body"><p>MOU全文公開（6/18）・電子署名発効確認済み。6/19署名式キャンセルで既に合意発効中。次の焦点は機雷除去（MOU5条項：30日以内義務）。機雷除去完了後に商業通航本格化・日本関係38隻段階的解放・60日核交渉開始へ。WTI $65〜75、ブレント $70〜80への収束が見込まれる。Goldman Sachs「湾岸輸出7月末前に戦前水準」予測と整合。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB（機雷遅延・荷主慎重継続）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-title">⏳ シナリオB：機雷除去遅延・BIMCO警告・保険慎重継続</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-title">⏳ シナリオB：機雷除去遅延・荷主慎重・通航回復2〜3ヶ月遅れ</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-body"><p>MOU合意成立も実施面での摩擦が通航回復を遅らせるシナリオ。BIMCO「MOU後もホルムズは依然高リスク」警告継続。機雷除去に実際には3ヶ月以上かかる可能性（米国防総省推定最大6ヶ月）。保険会社・荷主が安全確認まで待機。ファルス通信の「有料化」発言が荷主の不確実性を高める。WTI $80〜90の高止まり継続。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-body"><p>合意発効も機雷除去・保険・荷主の三重ボトルネックで通航回復が2〜3ヶ月遅れるシナリオ。MOU5条項「30日以内」は義務だが実施能力・意志が不透明。BIMCO「依然高リスク」警告継続。世界最大タンカー運航会社「急いで通航するな」と公式声明。ガリバフ「サービス料徴収」発言が将来的な通航コスト上昇リスクを示唆。WTI $80〜90に再上昇の可能性。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC（イスラエル問題→合意崩壊）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-title">⚠️ シナリオC：アラグチー「MOU違反」発動→署名前外交崩壊</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-title">⚠️ シナリオC：60日核交渉失敗→イスラエル問題で合意崩壊</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-body"><p>アラグチー「イスラエルのレバノン攻撃継続=MOU違反」警告が現実化するシナリオ。イスラエルがレバノン撤退せず攻撃継続→イランがMOU実施を一方的に停止。WTI $100〜120に急騰、封鎖再強化の可能性。ネタニヤフ「トランプとは必ずしも同意見でない」発言が示すイスラエルの独自行動リスク。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-body"><p>電子署名発効も60日核交渉中にイスラエル問題が顕在化するシナリオ。ヒズボラ「イスラエル撤退なき停戦は拒否」の姿勢継続。アラグチー「レバノン攻撃継続はMOU違反」発言が伏線として残存。60日交渉中にイスラエルがレバノン攻撃を拡大→イランがMOU実施を停止宣言→通航再封鎖。WTI $100〜120。Stimson Center「イスラエル=最大の不安定要因」と分析。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD（核交渉失敗→再封鎖）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-title">💣 シナリオD：署名後破棄→軍事再開・再封鎖</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-title">💣 シナリオD：60日核交渉決裂→イラン一方的停止→再封鎖</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-body"><p>MOU発効後も60日核交渉が不成立に終わり、イランが合意を一方的に破棄するシナリオ。核・ミサイル問題で根本的合意が得られず、米国が再制裁→イランがホルムズ再封鎖。「MOU前よりも危険な核状況」が顕在化。WTI $130以上への急騰。ただし電子署名発効・MOU全文公開により実施段階に入っており、この段階でのシナリオD確率は最低水準。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-body"><p>MOU発効・機雷除去後も60日核交渉で根本的合意が得られず、イランが一方的に協議を打ち切るシナリオ。MOU8条項「核兵器調達・開発しない」の検証機構が「相互合意」に委ねられており未確定。米国が再制裁→イランが「MOU破棄」宣言→再封鎖・再機雷散布。WTI $130以上。Iran SITREP「核軟化に対するイラン国内コスト上昇中・強硬派の抵抗」を指摘。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター

> ⚠️ Claude Code: `grep -n "scenario-footer\|次の焦点\|6月17日" docs/index.html | head -10` で現在の実態を確認後に適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="scenario-footer"><p><strong>次の5焦点（2026年6月17日 08:44 JST）：</strong>①MOU全文公開待ち（米側24〜48時間以内予告）②アラグチー「イスラエル攻撃=MOU違反」警告の現実化リスク③機雷除去タイムライン（MOU上30日以内・ペンタゴン推定最大6ヶ月）④日本関係38隻の解放タイミング⑤ファルス通信「有料化」vs 米「無条件無料」矛盾の決着</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="scenario-footer"><p><strong>次の5焦点（2026年6月18日 09:51 JST）：</strong>①機雷除去（MOU5条項：30日以内義務——実際のタイムラインと能力の確認）②ガリバフ「サービス料徴収」vs 米「永久無料」の決着（60日交渉の核心議題のひとつ）③60日核交渉開始（核兵器放棄確認・濃縮ウラン処理・検証機構の相互合意）④日本関係38隻の段階的解放と保険・BIMCO問題の解消⑤イスラエル・レバノン問題の帰趨（ヒズボラ撤退合意が60日交渉の前提条件になりうる）</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

> ⚠️ Claude Code: `grep -n "全ルート現況サマリー\|6月17日" docs/index.html | head -5` で現在の実態を確認後に適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
🚢 全ルート現況サマリー（2026年6月17日 08:44 JST 再確認済）
<!-- OLD:END -->
<!-- NEW:START -->
🚢 全ルート現況サマリー（2026年6月18日 09:51 JST 再確認済）
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行＋バッジ） ⚠️ 必ず最後に書く

> ⚠️ Claude Code: `grep -n "30秒で全体像\|quick-summary\|status-badge" docs/index.html | head -10` で現在の実態を確認後に適用すること。

### 3行サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
        <li>🕊️ <strong>MOU電子署名確認・6/19スイス署名式</strong>——トランプ・バンス・ガリバフが署名、バガエイ「発効済み」と確認（6/17 JST）</li>
        <li>🚢 <strong>イランタンカー2隻脱出・BIMCO高リスク警告</strong>——DIONA・HERO2が封鎖圏を脱出（3.8百万バレル）も通航実態は2%、保険・荷主は慎重維持</li>
        <li>📉 <strong>WTI $78前後（4日連続下落）</strong>——紛争ピーク比約40%下落、Goldman Sachs「Brent Q4目標$80」下方修正</li>
<!-- OLD:END -->
<!-- NEW:START -->
        <li>🕊️ <strong>MOU全文公開・6/19署名式キャンセル確定</strong>——14条項テキスト公開（5条項：60日無料・30日機雷除去・$3000億復興）、バガエイ「電子署名発効済み・式典不要」（6/18 JST）</li>
        <li>📉 <strong>WTI $75前後・5日連続下落・3月来最安値</strong>——Goldman Sachs「Brent Q4目標$80」下方修正・IEA 2027年供給過剰警告・紛争ピーク比40%超下落</li>
        <li>🚢 <strong>通航2%・機雷除去30日フェーズ・38隻足止め</strong>——BIMCO「依然高リスク」・世界最大タンカー運航会社「急いで通航するな」・日本関係38隻湾内継続</li>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ

<!-- APPLY:START -->
<!-- OLD:START -->
        <span class="status-badge badge-days">⏱️ 封鎖111日目</span>
<!-- OLD:END -->
<!-- NEW:START -->
        <span class="status-badge badge-days">⏱️ 封鎖112日目</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
        <span class="status-badge badge-phase">📋 Phase 9：6/19署名式</span>
<!-- OLD:END -->
<!-- NEW:START -->
        <span class="status-badge badge-phase">📋 Phase 10：MOU発効・機雷除去30日</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

### updated フィールド

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年6月17日 08:44 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年6月18日 09:51 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

### staleNotice（新情報あり → 空文字）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### latest 配列への先頭追加（2件）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "title": "MOU14条項全文公開——60日無料通航・30日機雷除去・米$3000億復興計画",
      "body": "米政府がイスラマバードMOUの全14条項テキストを公開（6/18 JST）。4条項：米国が署名後即座に封鎖解除開始・30日以内完全解除。5条項：イランが60日間のみ無料通航保証・30日以内に機雷除去。また米国はイランの石油輸出に対する制裁免除を即座に発効し、イラン凍結資産を利用可能にすると約束。$3000億以上の復興・開発計画も明記。ガリバフ議長「ホルムズは旧来条件に戻らない・サービス料徴収」と改めて強調。",
      "sourceLabel": "NBC News",
      "date": "2026年6月18日",
      "label": "🕊️ 外交",
      "url": "https://www.nbcnews.com/politics/national-security/text-iran-us-memorandum-understanding-rcna350582"
    },
    {
      "title": "Goldman Sachs「Brent Q4目標$80」下方修正——WTI $75・5日連続下落・IEA供給過剰警告",
      "body": "Goldman SachsがBrentクルードのQ4 2026目標価格を$90から$80に下方修正。「湾岸輸出は7月末前に戦前水準に回復する」との予測を根拠とする。WTI $75前後・Brent $79前後（5日連続下落・3月来最安値）。IEAは2027年に向けて供給過剰シナリオを警告——需要増+2百万b/d に対し供給増+8百万b/d の見通し。紛争ピーク比40%超の油価下落。",
      "sourceLabel": "Trading Economics",
      "date": "2026年6月18日",
      "label": "📉 市場",
      "url": "https://tradingeconomics.com/commodity/crude-oil"
    },
<!-- NEW:END -->
<!-- APPLY:END -->

### osint 配列への先頭追加（Al Jazeera 最新 1件）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
<!-- OLD:END -->
<!-- NEW:START -->
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
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ Claude Code: 旧 osint 先頭アイテム（isLatest: true）を `isLatest: false` に変更すること。
> ⚠️ Claude Code: `latest` 配列の現在の3件目・4件目を `archive` の先頭バッチへ移動すること（配列サイズを4件に維持）。

---

## [S11] 更新ログ追記 ＋ 折り畳み維持

### ブロック1: 常時表示エリアの更新（3件固定維持）

> ⚠️ Claude Code: `grep -n "2026年6月17日 08:44 JST\|2026年6月16日 08:14 JST\|2026年6月15日 07:09 JST" docs/index.html | head -10` で現在の常時表示3件の行番号を確認してから適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年6月17日 08:44 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/17 08:44</span> — <strong style="color:#fca5a5;">【重大更新】</strong>アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」——署名式6/19スイス2日前に最大リスク浮上（6/17 JST）｜イランタンカー2隻（DIONA・HERO2）封鎖圏脱出——3.8百万バレル原油・2ヶ月ぶりのイラン原油輸出（6/17 JST）｜ファルス通信「MOU通航無料は60日間のみ・有料化」vs 米「無条件無料」矛盾浮上｜BIMCO高リスク警告継続・日本関係船舶38隻足止め（日本船主協会）｜WTI $78前後（4日連続下落）｜6/19署名まで2日・封鎖111日目・ニュース2件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月16日 08:14 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/16 08:14</span> — <strong style="color:#fca5a5;">【重大更新】</strong>米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」宣言・MOU14条項（全面停戦・ホルムズ再開・核60日交渉）・バンス「デジタル署名済み」・ドーハ事前協議・署名式6/19スイス・機雷除去最大6ヶ月・WTI $81.10（-4.5%）・警戒レベル最高→高・封鎖110日目・ニュース3件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月15日 07:09 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/15 07:09</span> — <strong style="color:#fca5a5;">【重大更新】</strong>パキスタンPM「停戦は今すぐ発効」・G7エヴィアン（6/15-17）開幕・署名式6/19スイス確定・イスラエル空爆（6/14）で複雑化・カタール調停団テヘランへ・アラグチー「サービス料・ホルムズの剣は永遠」・WTI $84.88・封鎖109日目</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年6月18日 09:51 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/18 09:51</span> — <strong style="color:#fca5a5;">【重大更新】</strong>MOU14条項全文公開（60日無料通航・30日機雷除去・$3000億復興計画）・6/19ジュネーブ署名式キャンセル確定（電子署名発効確認済：バガエイ外務省報道官）・Goldman Sachs Brent Q4$80下方修正・IEA供給過剰警告・WTI $75前後（5日連続下落・3月来最安値）・日本関係38隻足止め継続・封鎖112日目・ニュース2件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月17日 08:44 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/17 08:44</span> — <strong style="color:#fca5a5;">【重大更新】</strong>アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」——署名式6/19スイス2日前に最大リスク浮上（6/17 JST）｜イランタンカー2隻（DIONA・HERO2）封鎖圏脱出——3.8百万バレル原油・2ヶ月ぶりのイラン原油輸出（6/17 JST）｜ファルス通信「MOU通航無料は60日間のみ・有料化」vs 米「無条件無料」矛盾浮上｜BIMCO高リスク警告継続・日本関係船舶38隻足止め（日本船主協会）｜WTI $78前後（4日連続下落）｜6/19署名まで2日・封鎖111日目・ニュース2件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月16日 08:14 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/16 08:14</span> — <strong style="color:#fca5a5;">【重大更新】</strong>米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」宣言・MOU14条項（全面停戦・ホルムズ再開・核60日交渉）・バンス「デジタル署名済み」・ドーハ事前協議・署名式6/19スイス・機雷除去最大6ヶ月・WTI $81.10（-4.5%）・警戒レベル最高→高・封鎖110日目・ニュース3件更新・OSINT更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2: log-collapse への旧3件目（6/15 07:09）の挿入

> ⚠️ Claude Code: `grep -n "log-collapse\|6月15日 07:09\|6月16日 08:14" docs/index.html | head -10` で現在の log-collapse 先頭エントリーを確認すること。
> 6/15 07:09 が log-collapse の先頭に既に存在する場合はこのブロックは **スキップ**（二重挿入禁止）。
> 存在しない場合のみ以下を適用すること。

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
          <div><span style="color:#94a3b8;">2026/06/16 08:14</span> — 米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」宣言・MOU14条項（全面停戦・ホルムズ再開・核60日交渉）・バンス「デジタル署名済み」・ドーハ事前協議・署名式6/19スイス・機雷除去最大6ヶ月・WTI $81.10（-4.5%）・警戒レベル最高→高・封鎖110日目</div>
          <div>📅 <strong>2026年6月15日 07:09 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### JSON-LD dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-06-17T00:00:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-06-18T00:00:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
[✓] Step 0 — old_str 基準：6月17日 08:44 JST版（プロジェクト知識＋更新ログ照合確認済み・一致）
[✓] C01 タンカー確認 — web検索実施済み・日本関係船舶38隻が湾内足止め（日本船主協会・6/16確認）・6/18現時点で変化なし（最新報告見つからず前回値維持）
[✓] S01 ヘッダー — 6月17日 08:44 JST → 6月18日 09:51 JST・警戒レベル「高（MOU発効・機雷除去30日フェーズ）」
[✓] S02 TICKER — MOU全文公開・6/19署名式キャンセル・Goldman Sachs Brent $80・ガリバフ矛盾・通航2%・112日目
[✓] S03 速報インシデント — 6/18 09:51付け・MOU全文公開・署名式キャンセル・Goldman Sachs下方修正
[✓] S04 情勢カード3枚 — 外交（MOU全文公開・式キャンセル・ガリバフ）・軍事/海運（通航2%・機雷30日・BIMCO・38隻）・エネルギー（WTI $75・Goldman $80・IEA過剰）
[✓] S05 COUNTDOWN — 112日目・Phase 10「MOU発効・機雷除去フェーズ（30日以内 = 7月上旬）」
[✓] S06 シナリオ確率補足バナー — 6/18 09:51 JST・A↑↑↑↑↑↑（MOU発効確認・最高水準）・矢印変更なし
[✓] S07 シナリオ4本 — A（MOU発効→機雷30日→段階再開→60日核交渉）・B（機雷遅延・BIMCO・サービス料）・C（60日交渉中イスラエル問題顕在化）・D（核交渉決裂→一方的停止）
[✓] S07 C/D差別化 — C（イスラエル問題→MOU実施停止型）vs D（60日核交渉決裂→一方的破棄型）✓
[✓] S07 WTI差別化 — A: $65-75 / B: $80-90 / C: $100-120 / D: $130+ ✓
[✓] S08 シナリオフッター — 5焦点（機雷除去30日・サービス料決着・60日核交渉・38隻/BIMCO・イスラエル・レバノン）
[✓] S08.5 全ルート現況サマリー — 6/18 09:51 JST 再確認済
[✓] S09 30秒カラム — 3行サマリー（MOU全文公開・WTI $75・通航2%/38隻）＋バッジ更新（112日目・Phase 10）
[✓] S10 news_data.json — latest 2件新規（MOU全文公開・Goldman Sachs下方修正）・旧2件archive移動・osint AJ 6/17
[✓] S10 URL確認済 — NBC News ✓ Trading Economics ✓ Al Jazeera ✓（osintのみ）
[✓] S10 osint — 配列先頭追加・既存 isLatest:true → false 変更 ✓
[✓] S11 更新ログ — 2ブロック構成（常時表示3件固定・log-collapse先頭に6/16版挿入）
[✓] S11 ブロック1 — grep確認注記済み。6/16 08:14の内容は上記に記載済み ✓
[✓] S11 ブロック2 — 6/15 07:09が log-collapse に既存の場合はスキップ注記済み ✓
[✓] S11 JSON-LD — 2026-06-18T00:00:00+09:00（ISO 8601 JST形式）✓
[✓] 全体 — 📰関連最新ニュースにAl Jazeera混入なし ✓（AJはosintのみ）
[✓] 全体 — 習近平 記載なし ✓
[✓] 全体 — Wikipedia/毎日新聞 URL 不使用 ✓
[✓] 全体 — シナリオ確率数値 記載なし（自動同期） ✓
[✓] 全体 — TICKER内JST表記あり ✓
[✓] 全体 — 「二重封鎖」使用なし ✓
[✓] 全体 — Iran International は latest 使用不可（今回は NBC News・Trading Economics使用） ✓
```

---

## 🔑 本日の重要事項まとめ（Claude Code 参照用）

| 項目 | 内容 |
|---|---|
| **最重要①** | **MOU14条項全文公開（6/18 JST）——NBC News** |
| **最重要②** | **6/19ジュネーブ署名式キャンセル確定——バガエイ外務省報道官「電子署名済み・式は不要」** |
| 新展開① | Goldman Sachs Brent Q4目標$80（$90→$80）下方修正 |
| 新展開② | IEA 2027年供給過剰警告（供給+8百万b/d vs 需要+2百万b/d） |
| 新展開③ | WTI $75前後・Brent $79前後（5日連続下落・3月来最安値） |
| 機雷除去 | MOU5条項「30日以内」義務——7月上旬目途 |
| 日本関係船舶 | **38隻**が湾内足止め継続（日本船主協会・Reuters 6/16、6/18変化なし） |
| 通航実態 | 2%（1隻/日）——世界最大タンカー運航会社「急いで通航するな」 |
| ガリバフ矛盾 | 「ホルムズは旧来条件に戻らない・サービス料徴収」継続 |
| 封鎖日数 | **112日目** |

---

## 次ステップ

1. `run.bat` 実行 → `index_html_diffs.md` push
2. Claude Code 定型文送信：
   「git pull --rebase してから、docs/tools/index_html_diffs.md に従って docs/index.html を更新してください。また docs/data/news_data.json も最新版がpush済みです。更新完了後に commit してください。push は確認後に指示します。」
3. ⚠️ S03 速報インシデントの先頭 strong タグ old_str は `grep -n "6/17 08:44 速報" docs/index.html` で確認すること
4. ⚠️ S04・S05・S06・S07・S08・S08.5・S09 の old_str は view_range/grep で確認すること
5. ⚠️ S11 ブロック2：log-collapse先頭に 6/15 07:09 が既存かどうか `grep -n "6月15日 07:09" docs/index.html` で確認し、あれば **ブロック2はスキップ**（二重挿入防止）
6. commit 確認（`git branch && git log --oneline -3`）→ push 指示
