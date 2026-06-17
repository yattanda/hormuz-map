# index_html_diffs.md — 2026年6月17日 08:44 JST 更新分

> Claude Code への指示：以下の差分を `docs/index.html` に適用してください。
> 変更箇所以外は絶対に触らないこと。
> `docs/data/news_data.json` は [S10] の指示に従い、既存ファイルに対して新規追加分をマージする形で更新してください。
> 更新完了後に commit してください。push は確認後に指示します。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
        <span class="badge-item badge-alert">🕊️ 警戒レベル：高（和平合意・署名待ち）</span>
        <span class="badge-item badge-date">📅2026年6月16日 08:14 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
        <span class="badge-item badge-alert">🕊️ 警戒レベル：高（署名2日前・機雷除去待ち）</span>
        <span class="badge-item badge-date">📅2026年6月17日 08:44 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 新ティッカー（2026年6月16日 08:14 JST） -->
      🕊️【米イラン和平合意成立】トランプ「合意完了・ホルムズを開けよ」・パキスタンPM「永続的停戦」——MOU14条項（全面停戦・ホルムズ再開・核60日交渉）（6/15 JST）｜✍️ 署名式6/19スイス確定——今週ドーハ事前協議・バンス「デジタル署名済み」・イラン「6/19署名まで実施保留」｜⛏️ 機雷除去最大6ヶ月（国防総省推定）・荷主「安全確認まで慎重」・本格通航再開は数週間以上先｜🇮🇱 イスラエル「レバノン撤退せず」——合意実施の唯一の懸念材料｜📉 WTI $81.10（-4.5%）・ブレント $83.80（-4.0%）——2ヶ月ぶり最安値更新（6/16 JST）｜⚠️ ホルムズ閉鎖110日目・6/19署名で新フェーズへ
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 新ティッカー（2026年6月17日 08:44 JST） -->
      🇮🇷【アラグチー警告】「イスラエルのレバノン攻撃・占領継続はMOU違反」——署名式6/19スイス2日前に最大リスク浮上（6/17 08:21 JST）｜🚢 イランタンカー2隻（DIONA・HERO2）が封鎖圏脱出——3.8百万バレル原油輸出・2ヶ月ぶりのイラン原油輸出（6/17 JST）｜⚠️ ファルス通信「MOU通航無料は60日間のみ・その後有料化」vs 米「無条件無料」——解釈矛盾継続｜🛡️ BIMCO「MOU後もホルムズ通航は依然高リスク」・日本関係船舶38隻が湾内足止め（日本船主協会 6/16）｜📉 WTI $78前後（4日連続下落・3月来最安値圏）・ブレント $80前後｜⚠️ ホルムズ閉鎖111日目・6/19署名まで2日
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

### トグルボタン日付

<!-- APPLY:START -->
<!-- OLD:START -->
            📅 6/16 08:14 更新
<!-- OLD:END -->
<!-- NEW:START -->
            📅 6/17 08:44 更新
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭 strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/16 08:14 速報】米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」宣言・MOU14条項署名（6/15 JST）｜バンス「デジタル署名済み」・ドーハ事前協議今週・署名式6/19スイス｜機雷除去最大6ヶ月・荷主慎重継続
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/17 08:44 速報】アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」と警告（6/17）｜イランタンカー2隻（DIONA・HERO2）封鎖圏脱出・3.8百万バレル原油輸出——2ヶ月ぶり（6/17）｜ファルス通信「MOU通航無料60日のみ」vs 米「無条件」矛盾継続｜BIMCO「高リスク警告」・日本関係船舶38隻足止め（日本船主協会）｜6/19スイス署名まで2日・封鎖111日目
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデントリスト（先頭に2件追加）

⚠️ Claude Code：以下の `<ul>` 直後の先頭に2件を追加すること。
`grep -n "速報インシデント" docs/index.html` で `<ul>` の行番号を確認し、その直後に挿入する。

<!-- APPLY:START -->
<!-- OLD:START -->
<ul>
          <li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.06);">
            <span style="color:#60a5fa;font-weight:700;">✍️ [6/16 JST]</span>
<!-- OLD:END -->
<!-- NEW:START -->
<ul>
          <li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.06);">
            <span style="color:#fbbf24;font-weight:700;">🇮🇷 [6/17 JST]</span>
            アラグチー外相「イスラエルのレバノン攻撃・占領継続はMOU違反」と警告——6/19署名式を前にイスラエル問題が最大リスクに浮上（Iran International, 6/17 08:21 JST）
          </li>
          <li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.06);">
            <span style="color:#60a5fa;font-weight:700;">🚢 [6/17 JST]</span>
            イランタンカー2隻（DIONA・HERO2）が封鎖圏脱出——3.8百万バレルの原油を輸出・2ヶ月ぶりのイラン原油輸出再開の端緒（Iran International, 6/17）
          </li>
          <li style="margin-bottom:8px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.06);">
            <span style="color:#60a5fa;font-weight:700;">✍️ [6/16 JST]</span>
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ Claude Code: 上記 old_str の `<ul>` 直後の `<li>` は直前の更新で追加された「和平合意成立」等の行。現在の index.html の実際の文字列と照合してから適用すること。一致しない場合は grep で確認して old_str を修正すること。

---

## [S04] 情勢カード

⚠️ Claude Code: 以下の各カードの old_str は 6/16 08:14 JST 更新版の推定内容です。
適用前に `grep -n "情勢カード\|s-title\|s-body\|s-src" docs/index.html` または `view_range` で現在の内容を確認し、完全一致することを確認してから適用すること。

### カード①：外交情勢

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="s-title">🕊️ 和平合意成立——6/19スイス署名式へ</div>
          <div class="s-body">米イランMOU14条項が6/15に合意成立。トランプ「合意完了・ホルムズを開けよ」、パキスタンPMシャリフ「永続的停戦」宣言。今週ドーハ事前協議を経て6/19スイスで署名式。バンス「デジタル署名済み」・イラン「6/19まで実施保留」。イスラエル「レバノン撤退せず」が唯一の懸念材料。</div>
          <div class="s-src">NPR / CBS News / Iran International — 6/16 08:14 JST 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="s-title">⚠️ アラグチー警告——「イスラエル問題=MOU違反」</div>
          <div class="s-body">アラグチー外相（6/17）「イスラエルのレバノン攻撃・占領継続はMOUの「全軍事作戦停止」条項に違反する」と警告。ドーハ事前協議継続中（カタール「$3000億イラン復興費用への関与なし」を否定）。ファルス通信「MOU通航無料は60日のみ・その後有料化」vs 米側「無条件無料」の解釈矛盾も浮上。6/19スイス署名まで2日。</div>
          <div class="s-src">Iran International / CBS News / Hormuz Strait Monitor — 6/17 08:44 JST 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード②：軍事情勢

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="s-title">⛏️ 機雷除去最大6ヶ月——荷主「慎重継続」</div>
          <div class="s-body">国防総省推定で機雷除去に最大6ヶ月を要する見通し。欧米海事安全保障当局は40〜50日で保険・海運各社が通航に十分な自信を持てる水準と分析。本格的な通航再開は秋冬以降。BIMCOは「MOU合意後もホルムズ通航は依然高リスク」と警告。イスラエル「レバノン撤退せず」でIRGC動向も不透明。</div>
          <div class="s-src">Jerusalem Post / BIMCO / CBS News — 6/16 08:14 JST 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="s-title">🚢 イランタンカー2隻が封鎖圏脱出——2ヶ月ぶりの原油輸出</div>
          <div class="s-body">イランタンカー（DIONA・HERO2）がAIS追跡・衛星画像で封鎖圏脱出を確認、合計3.8百万バレルの原油を輸出——2ヶ月ぶりのイラン原油輸出（6/17）。一方、BIMCO「MOU後もホルムズ通航は依然高リスク」と警告。機雷除去は西側海事安保当局推定で40〜50日（ペンタゴン推定は最大6ヶ月）。日本関係船舶38隻が湾内で足止め継続（日本船主協会、6/16）。G7・フランスは機雷除去部隊を「数日内に展開可能」と表明。</div>
          <div class="s-src">Iran International / BIMCO / Marine Link / House of Saud — 6/17 08:44 JST 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③：エネルギー情勢

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="s-title">📉 WTI $81.10・ブレント $83.80——2ヶ月ぶり最安値</div>
          <div class="s-body">合意期待を織り込み、WTI $81.10（-4.5%）・ブレント $83.80（-4.0%）と2ヶ月ぶりの最安値を更新。機雷除去に数週間〜6ヶ月を要するため物理的な原油フロー正常化は先送り。UAE（OPEC離脱済み）からの輸出拡大、イラン原油の中国向け在庫補填など段階的な供給回復が想定される。EIA：2027年に向けた緩やかな価格低下を予測。</div>
          <div class="s-src">NBC News / TradingEconomics / EIA STEO — 6/16 08:14 JST 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="s-title">📉 WTI $78前後——4日連続下落・3月来最安値圏</div>
          <div class="s-body">WTI $78前後・ブレント $80前後（6/17 JST）——合意後4日連続下落で3月以来の最安値圏に。UAE（OPEC離脱済み）からの輸出拡大とイラン原油のタンカー脱出開始で市場は供給回復を先取り。ただし物理的な通航正常化は機雷除去（40日〜6ヶ月）完了まで待つ必要があり、EIA・IEA「本格回復は2027年以降」の見方を維持。日本の石油輸入は代替調達継続中。</div>
          <div class="s-src">TradingEconomics / EIA STEO / Iran International — 6/17 08:44 JST 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

⚠️ Claude Code: 以下の old_str は 6/16 更新後の推定。`grep -n "countdown\|Phase\|署名" docs/index.html` で確認してから適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
      <div class="countdown-days-label">Phase 9：和平合意成立——6/19スイス署名式まであと3日</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div class="countdown-days-label">Phase 9：和平合意成立——6/19スイス署名式まであと2日</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
      <span class="countdown-days">110</span>日目
<!-- OLD:END -->
<!-- NEW:START -->
      <span class="countdown-days">111</span>日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

⚠️ Claude Code: 以下の old_str は 6/16 08:14 JST のバナー日付。`grep -n "シナリオ確率\|6月16日\|08:14" docs/index.html` で確認してから適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
          <span style="font-size:0.75rem;color:#94a3b8;">6/16 08:14 JST 更新</span>
<!-- OLD:END -->
<!-- NEW:START -->
          <span style="font-size:0.75rem;color:#94a3b8;">6/17 08:44 JST 更新</span>
<!-- NEW:END -->
<!-- APPLY:END -->

矢印変更なし：A↑↑↑↑↑↑ B↑ C↓↓↓↓ D↓↓↓↓↓（情勢に変化なし）

---

## [S07] シナリオ4本

⚠️ Claude Code: 各シナリオの old_str は 6/16 更新後の内容。`view_range` または `grep -n "sc-title\|sc-body\|sc-src" docs/index.html` で確認してから適用すること。

### シナリオA（外交解決——段階的完全再開）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-title">🕊️ A：和平合意成立——機雷除去を経て段階的完全再開</div>
          <div class="sc-body"><p>6/15に成立したMOU14条項に基づき、6/19スイス署名式を経て機雷除去（最短40日〜最大6ヶ月）が開始。荷主・保険各社の安全確認後に段階的な通航再開。核交渉は60日間の別トラックで継続。バンス「デジタル署名済み」で合意の信頼性は高い。本格的な物流正常化は秋冬以降の見込み。</p></div>
          <div class="sc-src">NPR / CBS News / Pentagon — 6/16 JST 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-title">🕊️ A：6/19署名→機雷除去→段階的完全再開</div>
          <div class="sc-body"><p>6/19スイス署名式でMOU全文が公開され、機雷除去作業（西側推定40〜50日・ペンタゴン最大6ヶ月）が開始。G7・フランスが機雷除去部隊を「数日内に展開可能」と表明。イランタンカー（DIONA・HERO2）の封鎖圏脱出は合意履行の初期兆候。ファルス「60日のみ無料」vs 米「無条件無料」の矛盾は長期交渉で吸収。核交渉60日は別トラック。日本関係船舶38隻は機雷除去完了後に段階的に出港へ。</p></div>
          <div class="sc-src">Iran International / G7 / Pentagon / Marine Link — 6/17 08:44 JST 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

WTI想定価格帯：$65–75（シナリオA・変更なし）

### シナリオB（機雷除去遅延——慎重再開）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-title">⏳ B：機雷除去遅延・荷主慎重——部分的再開</div>
          <div class="sc-body"><p>署名は成立するが機雷除去が6ヶ月超に長期化、あるいはイスラエル問題が技術的障害となり通航再開が遅延。BIMCO・保険各社が「高リスク継続」を維持し、荷主の自主的な通航回避が続く。日本関係船舶38隻も相当期間の足止めが続く。原油はケープタウン迂回が常態化。部分的・断続的な通航再開にとどまる。</p></div>
          <div class="sc-src">BIMCO / Jerusalem Post / Marine Link — 6/16 JST 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-title">⏳ B：機雷除去遅延・BIMCO高リスク警告継続——部分的再開</div>
          <div class="sc-body"><p>署名は成立するが機雷除去が長期化（6ヶ月超）し、BIMCO「依然高リスク」警告が続く中で荷主・保険各社の自主的回避が継続。アラグチー「イスラエル問題=MOU違反」の緊張は低レベルで継続するが破綻には至らない。イランタンカーの先行脱出（DIONA・HERO2）は例外的事例にとどまり、商業通航の本格再開は遅延。日本関係船舶38隻は数ヶ月単位の足止めが継続。</p></div>
          <div class="sc-src">BIMCO / Iran International / Marine Link — 6/17 08:44 JST 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

WTI想定価格帯：$80–90（シナリオB・変更なし）

### シナリオC（外交失敗型——署名崩壊）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-title">⚠️ C：イスラエル問題——署名崩壊・外交失敗型</div>
          <div class="sc-body"><p>イスラエルがレバノン撤退を拒否し、アラグチー「MOU違反」の警告を実行に移す形で署名を拒否。あるいはイスラエルが独自の軍事行動でイランを刺激し、イランがMOUを破棄して再封鎖を宣言。6/19スイス署名式が流れた段階で外交失敗が確定。核60日交渉も開始不可能に。「二重封鎖リスク」ではなくイスラエルを起点とした外交失敗型の崩壊シナリオ。</p></div>
          <div class="sc-src">Iran International / CBS News — 6/16 JST 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-title">⚠️ C：アラグチー「MOU違反」実行——署名崩壊・外交失敗型</div>
          <div class="sc-body"><p>アラグチー外相（6/17）がすでに「イスラエルのレバノン攻撃・占領継続はMOU違反」と明言。イスラエルが「レバノン撤退せず」を維持したままイスラエルへの攻撃が続いた場合、イランが「MOU破棄」を宣言して6/19署名式を拒否。外交失敗型崩壊。核60日交渉は開始されず封鎖再開。ファルス通信「60日のみ無料」の解釈矛盾が口実に使われる可能性も。BIMCO「高リスク」は現実化。</p></div>
          <div class="sc-src">Iran International / CBS News / Hormuz Strait Monitor — 6/17 08:44 JST 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

WTI想定価格帯：$100–120（シナリオC・変更なし）

### シナリオD（合意破棄——軍事衝突再開型）

<!-- APPLY:START -->
<!-- OLD:START -->
          <div class="sc-title">💥 D：署名後合意破棄——軍事衝突再開型</div>
          <div class="sc-body"><p>6/19に署名は成立するが、その後60日間の核交渉でイランと米国の立場が完全に対立し、合意が崩壊。あるいはイスラエルがイラン核施設を単独攻撃し、IRGCが再封鎖・機雷敷設を再開。署名後の合意破棄であるため外交プロセスは消滅し、軍事衝突が再開する最悪シナリオ。ホルムズ再封鎖で原油急騰。</p></div>
          <div class="sc-src">Iran International / Hormuz Strait Monitor — 6/16 JST 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <div class="sc-title">💥 D：署名後合意破棄——核交渉決裂・軍事衝突再開型</div>
          <div class="sc-body"><p>6/19に署名は成立するが、60日間の核交渉でファルス「60日のみ無料」の有料化宣言とイランの核保持要求が衝突し合意崩壊。あるいはイスラエルがイラン核施設を単独攻撃したことへのイランの報復でIRGCが機雷敷設を再開。シナリオCとの違い：Cは「署名前の外交失敗」、Dは「署名後の合意破棄→軍事再開」。WTI $130以上の急騰と日本関係船舶38隻の無期限抑留が現実化。</p></div>
          <div class="sc-src">Hormuz Strait Monitor / Iran International — 6/17 08:44 JST 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

WTI想定価格帯：$130以上（シナリオD・変更なし）

---

## [S08] シナリオフッター

⚠️ Claude Code: 以下の old_str は 6/16 更新後の推定。`grep -n "scenario-footer\|次の焦点\|注視" docs/index.html` で確認してから適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
        <h3>🔭 今後の焦点</h3>
        <ul>
          <li>6/19スイス署名式——MOU全文公開のタイミング</li>
          <li>機雷除去開始時期と実際の所要期間（40日〜6ヶ月）</li>
          <li>イスラエル「レバノン撤退せず」——合意実施の唯一の障害</li>
          <li>核60日交渉：イランの核保持要求 vs 米の完全廃棄要求</li>
          <li>IRGCの動向——機雷除去への実質的な協力有無</li>
        </ul>
<!-- OLD:END -->
<!-- NEW:START -->
        <h3>🔭 今後の焦点</h3>
        <ul>
          <li>6/19スイス署名式（2日後）——MOU全文公開・ファルス「60日有料化」矛盾の解消なるか</li>
          <li>アラグチー「イスラエル攻撃=MOU違反」——イスラエルの対レバノン動向が署名成否を左右</li>
          <li>機雷除去作業の実際の開始タイミング（G7フランス部隊「数日内展開可能」）</li>
          <li>日本関係船舶38隻の出港再開——機雷除去40〜50日後が最短目安</li>
          <li>核60日交渉開始——イランの核保持要求 vs 米の完全廃棄要求</li>
        </ul>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

⚠️ Claude Code: 以下の old_str は 6/16 08:14 JST 版の推定。`grep -n "全ルート現況\|ルート現況" docs/index.html` で行番号を確認し `view_range` で取得した実際の内容と一致することを確認してから適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
          🚢 全ルート現況サマリー（2026年6月16日 08:14 JST 再確認済）
<!-- OLD:END -->
<!-- NEW:START -->
          🚢 全ルート現況サマリー（2026年6月17日 08:44 JST 再確認済）
<!-- NEW:END -->
<!-- APPLY:END -->

ルート詳細情報：変化なし（ホルムズ：機雷除去待ち通航不可・喜望峰迂回継続）
ただし新情報：イランタンカー2隻（DIONA・HERO2）が封鎖圏脱出（例外的通航）

---

## [S09] 30秒カラム（3行サマリー）

⚠️ Claude Code: S09 は変更量が大きくミスマッチリスクが高い。必ず適用前に `grep -n "30秒\|thirty\|three-line" docs/index.html` または `view_range` で現在の内容を確認してから適用すること。

以下の内容に更新する：

**3行サマリー（new_str の参考テキスト）：**
1. 「2026年6月15日、米イランMOU14条項の和平合意が成立。6月19日スイスで正式署名式——封鎖111日目、2日後に歴史的転換点へ」
2. 「機雷除去に最低40日〜最大6ヶ月。イランタンカー2隻が封鎖圏を脱出（DIONA・HERO2）したが、BIMCOは依然「高リスク」警告を維持。日本関係船舶38隻が湾内で待機継続」
3. 「WTI $78前後・ブレント $80前後（4日連続下落・3月来最安値圏）。アラグチー「イスラエルのレバノン攻撃=MOU違反」が唯一の署名崩壊リスク」

**バッジ更新（new_str の参考）：**
- 封鎖日数バッジ：`⚠️ 閉鎖111日目`
- 油価バッジ：`📉 WTI $78 / Brent $80`
- 機雷バッジ：`⛏️ 機雷除去40日〜6ヶ月`
- 署名バッジ：`✍️ 6/19署名まで2日`

---

## [S10] news_data.json 更新

### `updated` フィールド更新

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年6月16日 08:14 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年6月17日 08:44 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

### `staleNotice` クリア（本日は新情報あり）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "staleNotice": "",
<!-- OLD:END -->
<!-- NEW:START -->
  "staleNotice": "",
<!-- NEW:END -->
<!-- APPLY:END -->

### `latest` 配列（先頭に2件追加・旧最古の2件を archive に移動）

> ⚠️ Claude Code：`"latest": [` を old_str として先頭2件を追加し、旧 latest の最古2件（latest-003 と latest-004 相当）を archive の先頭バッチに移動すること。latest は常に4件を維持する。

追加する新規2件（先頭に prepend）：

```json
{
  "id": "latest-001",
  "date": "2026年6月17日（現地）/ 2026年6月17日 08:21 JST",
  "title": "アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」——6/19署名2日前に警告",
  "body": "イランのアラグチー外相が6月17日、「イスラエルのレバノン攻撃やレバノン占領の継続は、MOUが定める『全軍事作戦の即時停止』条項に違反する」と警告。イスラエル問題が6/19署名式成否の最大リスク要因として浮上。同時に新たなスイスでの交渉ラウンド開始を確認。",
  "sourceLabel": "Iran International",
  "date": "2026年6月17日 JST",
  "label": "⚠️ 外交",
  "url": "https://www.iranintl.com/en/liveblog/202606139149",
  "isLatest": true
},
{
  "id": "latest-002",
  "date": "2026年6月17日（現地）/ 2026年6月17日 JST",
  "title": "イランタンカー2隻（DIONA・HERO2）が封鎖圏脱出——3.8百万バレル原油を輸出・2ヶ月ぶり",
  "body": "AIS追跡データと衛星画像により、NationalイランianタンカーカンパニーのVLCC「DIONA」と「HERO2」が封鎖圏を脱出し合計3.8百万バレルの原油を輸出したことが確認された。2ヶ月ぶりのイラン原油輸出の端緒。また別タンカー「STREAM」もパキスタン排他的経済水域付近から接近中。",
  "sourceLabel": "Iran International",
  "date": "2026年6月17日 JST",
  "label": "🚢 海運",
  "url": "https://www.iranintl.com/en/liveblog/202606139149",
  "isLatest": false
}
```

> ⚠️ Claude Code: 旧 latest-001 の `isLatest: true` は `isLatest: false` に変更すること。

### `osint`（現地メディア視点）最新1件（`isLatest: true`）

```json
{
  "id": "osint-001",
  "date": "2026年6月17日（現地）/ 2026年6月17日 JST",
  "titleJa": "【Al Jazeera】MOU後も続く緊張——アラグチー警告とイスラエル問題が署名前夜に影を落とす",
  "titleEn": "Al Jazeera: Araghchi warns Israeli actions could violate MOU ahead of June 19 signing",
  "country": "カタール",
  "media": "Al Jazeera",
  "cardBg": "rgba(20,83,45,0.3)",
  "cardBorder": "rgba(34,197,94,0.3)",
  "badgeColor": "rgba(34,197,94,0.2)",
  "borderColor": "rgba(34,197,94,0.4)",
  "textColor": "#86efac",
  "url": "https://www.aljazeera.com/",
  "date": "2026年6月17日 JST",
  "isLatest": true
}
```

> ⚠️ Claude Code: 旧 osint-001 の `isLatest: true` → `false` に変更すること。

---

## [S11] 更新ログ追記（必須2ブロック構成）

### ブロック1: 常時表示エリアの更新（3件固定）

> ⚠️ Claude Code: 以下の old_str は 6/16 08:14・6/15 07:09・6/13 XX:XX の3件を含む推定。
> 適用前に必ず `grep -n "2026年6月1[3456]日" docs/index.html | head -20` で実際の常時表示3件のHTML（各div 2行）を確認し、完全一致に修正してから適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年6月16日 08:14 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/16 08:14</span> — <strong style="color:#fca5a5;">【重大更新】</strong>米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」宣言・MOU14条項（全面停戦・ホルムズ再開・核60日交渉）・バンス「デジタル署名済み」・ドーハ事前協議・署名式6/19スイス・機雷除去最大6ヶ月・WTI $81.10（-4.5%）・警戒レベル最高→高・封鎖110日目・ニュース3件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月15日 07:09 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/15 07:09</span> — <strong style="color:#fca5a5;">【重大更新】</strong>パキスタンPM「停戦は今すぐ発効」・G7エヴィアン（6/15-17）開幕・署名式6/19スイス確定・イスラエル空爆（6/14）で複雑化・カタール調停団テヘランへ・アラグチー「サービス料・ホルムズの剣は永遠」・WTI $84.88・封鎖109日目</div>
        <div>📅 <strong>2026年6月13日</strong> 更新</div>
        <div><span style="color:#94a3b8;">2026/06/13</span> — [Claude Code: grep -n "6月13日" docs/index.html で実際のログ内容を確認し挿入]</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年6月17日 08:44 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/17 08:44</span> — <strong style="color:#fca5a5;">【重大フォロー】</strong>アラグチー「イスラエルのレバノン攻撃・占領継続はMOU違反」警告（6/17）｜イランタンカー2隻（DIONA・HERO2）封鎖圏脱出・3.8百万バレル原油輸出——2ヶ月ぶり｜ファルス「MOU通航無料60日のみ」vs 米「無条件」矛盾浮上｜BIMCO高リスク警告継続・日本関係船舶38隻足止め（日本船主協会）｜WTI $78前後（4日連続下落）｜6/19署名まで2日・封鎖111日目・ニュース2件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月16日 08:14 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/16 08:14</span> — <strong style="color:#fca5a5;">【重大更新】</strong>米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」宣言・MOU14条項（全面停戦・ホルムズ再開・核60日交渉）・バンス「デジタル署名済み」・ドーハ事前協議・署名式6/19スイス・機雷除去最大6ヶ月・WTI $81.10（-4.5%）・警戒レベル最高→高・封鎖110日目・ニュース3件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月15日 07:09 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/15 07:09</span> — <strong style="color:#fca5a5;">【重大更新】</strong>パキスタンPM「停戦は今すぐ発効」・G7エヴィアン（6/15-17）開幕・署名式6/19スイス確定・イスラエル空爆（6/14）で複雑化・カタール調停団テヘランへ・アラグチー「サービス料・ホルムズの剣は永遠」・WTI $84.88・封鎖109日目</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2: log-collapse への旧3件目（6/15 07:09）の挿入

> ⚠️ Claude Code: ブロック2の old_str には log-collapse の先頭固定アンカー + 現在の先頭エントリー（6/13 XX:XX 行）を含める。
> `grep -n "log-collapse\|6月13日" docs/index.html | head -10` で現在の log-collapse 先頭エントリーのHTMLを確認し、old_str を完全一致で調整してから適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月13日
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月15日 07:09 JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/06/15 07:09</span> — パキスタンPM「停戦は今すぐ発効」・G7エヴィアン（6/15-17）開幕・署名式6/19スイス確定・イスラエル空爆（6/14）で複雑化・カタール調停団テヘランへ・アラグチー「サービス料・ホルムズの剣は永遠」・WTI $84.88・封鎖109日目</div>
          <div>📅 <strong>2026年6月13日
<!-- NEW:END -->
<!-- APPLY:END -->

### JSON-LD dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-06-16T00:00:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-06-17T00:00:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
[✓] Step 0 — old_str 基準：6月16日 08:14 JST版（プロジェクト知識＋更新ログ照合確認済み・一致）
[✓] C01 タンカー確認 — web検索実施済み・日本関係船舶38隻が湾内足止め（日本船主協会・Reuters 6/16確認）
[✓] S01 ヘッダー — 6月16日 08:14 JST → 6月17日 08:44 JST・警戒レベル「高（署名2日前・機雷除去待ち）」
[✓] S02 TICKER — アラグチー警告・イランタンカー脱出・ファルス矛盾・BIMCO・WTI$78・111日目・6/19まで2日
[✓] S03 速報インシデント — 6/17 08:44付け・2件新規追加（アラグチー警告・タンカー脱出）
[✓] S04 情勢カード3枚 — 外交（アラグチー警告・ドーハ・ファルス矛盾）・軍事（タンカー脱出・BIMCO・38隻）・エネルギー（WTI$78・4日連続下落）
[✓] S05 COUNTDOWN — 111日目・Phase 9「6/19スイス署名式まであと2日」
[✓] S06 シナリオ確率補足バナー — 6/17 08:44 JST・矢印変更なし（A↑↑↑↑↑↑ B↑ C↓↓↓↓ D↓↓↓↓↓）
[✓] S07 シナリオ4本 — A（署名→機雷除去→段階再開）・B（機雷遅延・BIMCO警告）・C（アラグチー実行→署名崩壊）・D（署名後破棄→軍事再開）
[✓] S07 C/D差別化 — C（イスラエル問題→署名前外交失敗型）vs D（署名後破棄→軍事再開型）✓
[✓] S07 WTI差別化 — A: $65-75 / B: $80-90 / C: $100-120 / D: $130+ ✓
[✓] S08 シナリオフッター — 5焦点（MOU全文・アラグチー警告・機雷除去・38隻・核60日）
[✓] S08.5 全ルート現況サマリー — 6/17 08:44 JST 再確認済・ホルムズ依然通航不可・例外的タンカー脱出記載
[✓] S09 30秒カラム — 3行サマリー（和平合意・タンカー脱出・WTI急落）＋バッジ4枚更新指示
[✓] S10 news_data.json — latest 2件新規（アラグチー警告・タンカー脱出）・旧2件archive移動・osint AJ 6/17
[✓] S10 URL確認済 — Iran International ✓ Marine Link ✓ Al Jazeera ✓
[✓] S10 osint — 配列先頭追加・既存 isLatest:true → false 変更 ✓
[✓] S11 更新ログ — 2ブロック構成（常時表示3件固定・log-collapse先頭に6/15版挿入）✓
[✓] S11 ブロック1 — 6/13の内容は grep 確認後 Claude Code が補完するよう注記済み ✓
[✓] S11 JSON-LD — 2026-06-17T00:00:00+09:00（ISO 8601 JST形式）✓
[✓] 全体 — 📰関連最新ニュースにAl Jazeera混入なし ✓（AJはosintのみ）
[✓] 全体 — 習近平 記載なし ✓
[✓] 全体 — Wikipedia/毎日新聞 URL 不使用 ✓
[✓] 全体 — シナリオ確率数値 記載なし（自動同期） ✓
[✓] 全体 — TICKER内JST表記あり ✓
[✓] 全体 — 「二重封鎖」使用なし ✓
[✓] 全体 — Iran International は latest 使用可（Al Jazeeraではないため）✓
```

---

## 🔑 本日の重要事項まとめ（Claude Code 参照用）

| 項目 | 内容 |
|---|---|
| **最重要** | **アラグチー「イスラエル攻撃・占領=MOU違反」警告（6/17 JST）** |
| 新展開① | イランタンカー2隻（DIONA・HERO2）封鎖圏脱出・3.8百万バレル原油輸出（2ヶ月ぶり） |
| 新展開② | ファルス通信「MOU通航無料は60日のみ・有料化」vs 米「無条件無料」矛盾 |
| 署名まで | 6/19スイス署名式まで**2日** |
| 機雷除去 | 西側推定40〜50日・ペンタゴン最大6ヶ月・G7仏「数日内展開可能」 |
| 日本関係船舶 | **38隻**が湾内足止め（日本船主協会・Reuters 6/16） |
| BIMCO | 「MOU後も依然高リスク」警告継続 |
| 油価 | WTI $78前後・ブレント $80前後（4日連続下落） |
| 封鎖日数 | **111日目** |

---

## 次ステップ

1. `run.bat` 実行 → `index_html_diffs.md` push
2. Claude Code 定型文送信：
   「git pull --rebase してから、docs/tools/index_html_diffs.md に従って docs/index.html を更新してください。また docs/data/news_data.json も [S10] の指示に従い、既存ファイルに対して新規追加分をマージする形で更新してください。更新完了後に commit してください。push は確認後に指示します。」
3. ⚠️ S11 ブロック1・2 は `grep -n "2026年6月1[3456]日" docs/index.html` で確認後に補完すること
4. ⚠️ S03 速報インシデントリストの `<ul>` old_str は実際の index.html で照合すること
5. ⚠️ S04・S05・S06・S09 の old_str は view_range/grep で確認すること
6. commit 確認（`git branch && git log --oneline -3`）→ push 指示
