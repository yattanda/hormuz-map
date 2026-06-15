# index_html_diffs.md — 2026年6月16日 08:14 JST 更新分

> Claude Code への指示：以下の差分を `docs/index.html` に適用してください。
> 変更箇所以外は絶対に触らないこと。
> `docs/data/news_data.json` は [S10] の指示に従い、既存ファイルに対して新規追加分をマージする形で更新してください。
> 更新完了後に commit してください。push は確認後に指示します。

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
        <span class="badge-item badge-alert">🚨 警戒レベル：最高</span>
        <span class="badge-item badge-date">📅2026年6月15日 07:09 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
        <span class="badge-item badge-alert">🕊️ 警戒レベル：高（和平合意・署名待ち）</span>
        <span class="badge-item badge-date">📅2026年6月16日 08:14 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 新ティッカー（2026年6月15日 07:09 JST） -->
      🕊️【パキスタンPM「停戦は今すぐ発効」】署名式は6月19日スイスへ延期——G7エヴィアン（6/15-17）初日・トランプ「合意は完了・石油を流せ」宣言（6/14-15 JST）｜🇮🇱 イスラエルがベイルートを空爆（6/14）——トランプ「あるべきではなかった」と異例の批判・合意プロセスに打撃｜🇶🇦 カタール調停団がテヘランへ（6/14朝）——イラン「最終決定まだ」と署名延期（ファルス通信 6/14）｜🇮🇷 アラグチー「ホルムズ通航に『サービス料』徴収・ホルムズの剣は永遠に」——MOU後もイラン主権継続主張（6/14 JST）｜📉 WTI $84.88・ブレント $87.33——合意期待で2ヶ月ぶり最安値継続｜⚠️ ホルムズ閉鎖109日目・署名式6/19スイス確定
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 新ティッカー（2026年6月16日 08:14 JST） -->
      🕊️【米イラン和平合意成立】トランプ「合意完了・ホルムズを開けよ」・パキスタンPM「永続的停戦」——MOU14条項（全面停戦・ホルムズ再開・核60日交渉）（6/15 JST）｜✍️ 署名式6/19スイス確定——今週ドーハ事前協議・バンス「デジタル署名済み」・イラン「6/19署名まで実施保留」｜⛏️ 機雷除去最大6ヶ月（国防総省推定）・荷主「安全確認まで慎重」・本格通航再開は数週間以上先｜🇮🇱 イスラエル「レバノン撤退せず」——合意実施の唯一の懸念材料｜📉 WTI $81.10（-4.5%）・ブレント $83.80（-4.0%）——2ヶ月ぶり最安値更新（6/16 JST）｜⚠️ ホルムズ閉鎖110日目・6/19署名で新フェーズへ
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント

### トグルボタン日付

<!-- APPLY:START -->
<!-- OLD:START -->
            📅 6/15 07:09 更新
<!-- OLD:END -->
<!-- NEW:START -->
            📅 6/16 08:14 更新
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭 strong タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/15 07:09 速報】パキスタンPM「停戦は今すぐ発効」・署名式6/19スイス確定・G7エヴィアン（6/15-17）開幕・イスラエルのベイルート空爆（6/14）で複雑化・カタール調停団テヘランへ・アラグチー「サービス料・ホルムズの剣は永遠」・WTI $84.88・ブレント $87.33・109日目
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/16 08:14 速報】米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」宣言・MOU14条項署名（6/15 JST）｜バンス「デジタル署名済み」・ドーハ事前協議今週・署名式6/19スイス｜機雷除去最大6ヶ月・荷主慎重継続・WTI $81.10・ブレント $83.80急落・110日目
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデントリスト先頭2件追加

<!-- APPLY:START -->
<!-- OLD:START -->
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(239,68,68,0.4);">
  【6/15 JST】パキスタンPM「停戦は今すぐ発効」
<!-- OLD:END -->
<!-- NEW:START -->
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(74,222,128,0.5);">
  【6/15 JST】<strong style="color:#86efac;">米イラン和平合意成立</strong>——トランプ「合意完了・ホルムズを開けよ」、パキスタンPM「全戦線における即時かつ恒久的な軍事作戦終結」宣言。MOU14条項：全面停戦・ホルムズ再開・核60日後交渉・$300億湾岸国再建基金
</li>
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(74,222,128,0.4);">
  【6/15-16 JST】バンス副大統領「MOUは日曜にデジタル署名済み」・ドーハで事前協議今週開催——イラン副外相ガリバブ「6/19正式署名まで実施保留」・機雷除去最大6ヶ月（国防総省推定）・荷主は安全確認まで慎重姿勢継続
</li>
<li style="margin-bottom:6px;padding-left:10px;border-left:2px solid rgba(239,68,68,0.4);">
  【6/15 JST】パキスタンPM「停戦は今すぐ発効」
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

### カード①外交

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="s-title">🕊️ 外交：停戦発効・署名6/19スイス</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="s-title">🕊️ 外交：和平合意成立・6/19スイス署名へ</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="s-body">パキスタンPM「停戦は今すぐ発効」・署名式6/19スイスへ延期確定。G7エヴィアン（6/15-17）開幕——トランプが主要議題に。カタール調停団17時間交渉——イラン「最終決定まだ」。イスラエルのベイルート空爆が複雑化要因。アラグチー「サービス料・ホルムズの剣は永遠」。</div>
<div class="s-src">出典: CBS News / ファルス通信 / NPR（6/14-15）</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="s-body">トランプ「合意完了」・パキスタンPM「永続的停戦」——MOU14条項に合意（6/15 JST）。署名式は6/19スイスで確定、今週ドーハで事前協議。バンス「デジタル署名済み」。イラン「6/19署名まで実施保留」。イスラエルの「レバノン撤退拒否」が唯一の懸念材料として残存。</div>
<div class="s-src">出典: NBC News / CNN / NPR（6/15-16）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード②軍事

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="s-title">⚔️ 軍事：ベイルート空爆・IRGC強硬化</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="s-title">⛏️ 軍事：機雷除去開始準備・イスラエル問題</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="s-body">イスラエルがベイルート南郊を空爆（6/14）——トランプ「あるべきではなかった」と異例の批判。IRGCがタンカー1隻阻止継続（6/13）。CENTCOM自爆ドローン複数撃墜。合意プロセスへの打撃が懸念される。</div>
<div class="s-src">出典: Times of Israel / CENTCOM（6/13-14）</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="s-body">国防総省「機雷除去に最大6ヶ月」——除去艦3隻が既に展開中。イスラエル国防相「レバノン撤退せず」——合意がイスラエルに全前線停戦を義務付けており懸念材料。CENTCOM機雷除去準備作業開始。IRGC強硬派の動向に引き続き注視。</div>
<div class="s-src">出典: TechTimes / NPR / CNN（6/15-16）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③エネルギー

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="s-title">💰 エネルギー：WTI $84.88・ブレント $87.33</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="s-title">📉 エネルギー：WTI $81.10・ブレント $83.80（急落）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="s-body">WTI $84.88（-3.2%）・ブレント $87.33（-3.4%）——合意期待で週間マイナス6%・2ヶ月ぶり最安値継続。商業通航は戦前比95%減継続。</div>
<div class="s-src">出典: Trading Economics / Investing.com（6/14）</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="s-body">WTI $81.10（-4.5%）・ブレント $83.80（-4.0%）——和平合意発表で急落、2ヶ月ぶり最安値更新。荷主は「安全確認まで慎重」——本格通航再開まで数週間以上。正常化後はWTI $65-75へ下落見通し（各社分析）。</div>
<div class="s-src">出典: Yahoo Finance / Trading Economics / Globe and Mail（6/16）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

<!-- APPLY:START -->
<!-- OLD:START -->
<span class="countdown-days">109</span>日目
<!-- OLD:END -->
<!-- NEW:START -->
<span class="countdown-days">110</span>日目
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="countdown-label">Phase 9「スイス署名式（6/19）」停戦発効</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="countdown-label">Phase 9「和平合意成立——6/19スイス署名式まであと3日」</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="font-size:0.72rem;color:#94a3b8;text-align:right;margin-top:4px;">6/15 07:09 JST 確率更新 ／ A↑↑↑↑↑ B↑ C↓↓↓ D↓↓↓↓</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="font-size:0.72rem;color:#94a3b8;text-align:right;margin-top:4px;">6/16 08:14 JST 確率更新 ／ A↑↑↑↑↑↑ B↑ C↓↓↓↓ D↓↓↓↓↓</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本

### シナリオA（正式合意・段階的完全再開）

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-title">🟢 シナリオA：6/19署名・30日以内再開</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-title">🟢 シナリオA：和平合意成立・機雷除去→段階的完全再開</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-body"><p>6/19スイス署名式が成立し、ホルムズ海峡の機雷除去が開始される。30日以内に商業船舶の段階的通航が再開し、秋〜冬にかけて完全正常化が達成される。60日間核交渉でイラン制裁解除・凍結資産返還が実現。WTI $70-80水準への正常化が進む。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-body"><p>【現在進行中】米イラン和平合意（MOU14条項）が成立（6/15）。6/19スイス署名式→機雷除去開始（国防総省推定最大6ヶ月）→商業船舶の段階的再開へ。60日間核交渉でイラン制裁解除・凍結資産返還・$300億湾岸国再建基金実現。WTI $65-75まで段階的下落見通し。機雷除去完了後の完全正常化は2026年末〜2027年初を見込む。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB（機雷問題・慎重再開）

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-title">🟡 シナリオB：サービス料問題・部分的再開</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-title">🟡 シナリオB：機雷除去遅延・荷主慎重で部分再開にとどまる</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-body"><p>アラグチーが示した「サービス料徴収」が通航条件として残存。船主・保険業者が合意後も慎重姿勢を維持し、完全正常化が遅れる。WTI $85-95のレンジで推移が継続。イランが事実上の通航管理権を保持し、交渉カードとして活用し続ける。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-body"><p>機雷除去の遅れ（最大6ヶ月）・保険適用問題で荷主が安全確認まで慎重姿勢を継続。イランが事実上の通航管理権を保持（「どんな合意内容であれイランがホルムズを支配する」—A.ホッホスタイン）。商業通航の完全正常化は2027年以降にずれ込み、WTI $80-90のレンジ継続。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC（署名崩壊・再炎上）

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-title">🔴 シナリオC：ベイルート連鎖・署名失敗</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-title">🔴 シナリオC：イスラエル問題拡大・署名崩壊・再炎上</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-body"><p>イスラエルのベイルート攻撃が拡大し、イランが「全戦線停戦」条項を盾に署名を拒否。IRGCの強硬派が合意を覆し、ホルムズ封鎖が再強化される。ベイルート〜テヘラン連鎖で全面衝突リスクが再浮上。WTI $100-120への逆戻り。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-body"><p>イスラエル「レバノン撤退せず」——合意はイスラエルに全前線停戦を義務付けており、イランが「全戦線停戦」条項を盾に6/19署名を拒否するリスク。IRGCの強硬派がMOU実施を妨害し、ホルムズ封鎖が再強化される可能性。合意不履行→外交崩壊→再炎上シナリオ。WTI $100-120への逆戻り。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD（合意破棄・全面崩壊）

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-title">⚫ シナリオD：全面戦争再開</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-title">⚫ シナリオD：署名後合意破棄・軍事衝突再開</div>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-body"><p>イスラエルとイランが軍事衝突を再開し、米軍が全面的に介入。ホルムズが再封鎖され、レバノン・シリア・イエメンへ連鎖拡大。WTI $130-150超まで急騰。グローバル経済への甚大ダメージが避けられない最悪シナリオ。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-body"><p>合意成立後に米国またはイランがMOUを一方的に破棄——イスラエルの大規模攻撃を契機にイランが「合意無効」宣言、米軍が全面介入するシナリオ。ホルムズ再封鎖・レバノン・シリア・イエメンへ連鎖拡大。WTI $130+超まで急騰。和平合意成立後の現時点では確率は極めて低いが、監視継続が必要。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="scenario-footer"><p><strong>📍 次の焦点：</strong>①6/19スイス署名式（3日後）——正式発効のカウントダウン ②機雷除去プロセス開始——最大6ヶ月、ホルムズ安全航行確保 ③イスラエルのレバノン問題——「撤退しない」で合意への懸念残存 ④イラン国内批准——IRGC強硬派とモジュタバ・ハメネイの動向 ⑤60日間核交渉開始——制裁解除・凍結資産・$300億再建基金</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="scenario-footer"><p><strong>📍 次の焦点（6/16時点）：</strong>①6/19スイス署名式——正式発効まであと3日 ②機雷除去開始——国防総省推定最大6ヶ月・本格通航は秋冬以降 ③イスラエルのレバノン撤退問題——「撤退せず」が唯一の懸念材料 ④60日間核交渉——制裁解除・凍結資産・湾岸国$300億再建基金の行方 ⑤イラン国内——IRGC強硬派がMOU実施を妨害するリスク</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
🚢 全ルート現況サマリー（2026年6月15日 07:09 JST 再確認済
<!-- OLD:END -->
<!-- NEW:START -->
🚢 全ルート現況サマリー（2026年6月16日 08:14 JST 再確認済・和平合意成立で近日段階的再開見込み
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行サマリー＋バッジ）

<!-- APPLY:START -->
<!-- OLD:START -->
<p style="margin:0 0 8px;font-size:0.88rem;line-height:1.7;color:#e2e8f0;">① <strong>和平合意目前</strong>——パキスタンPM「停戦は今すぐ発効」・署名式6/19スイス確定・G7エヴィアンで合意が最重要議題</p>
<p style="margin:0 0 8px;font-size:0.88rem;line-height:1.7;color:#e2e8f0;">② <strong>イスラエルが複雑化</strong>——ベイルート空爆（6/14）・トランプが異例の批判・カタール調停団17時間交渉でイラン「最終決定まだ」</p>
<p style="margin:0 0 8px;font-size:0.88rem;line-height:1.7;color:#e2e8f0;">③ <strong>アラグチー強硬</strong>——「サービス料徴収・ホルムズの剣は永遠」・WTI $84.88・ブレント $87.33——封鎖109日目</p>
<!-- OLD:END -->
<!-- NEW:START -->
<p style="margin:0 0 8px;font-size:0.88rem;line-height:1.7;color:#e2e8f0;">① <strong>米イラン和平合意成立</strong>——トランプ「合意完了」・パキスタンPM「永続的停戦」宣言・MOU14条項（全面停戦・ホルムズ再開・核60日交渉）・6/19スイス署名式（6/15-16 JST）</p>
<p style="margin:0 0 8px;font-size:0.88rem;line-height:1.7;color:#e2e8f0;">② <strong>機雷除去が最大の課題</strong>——国防総省「最大6ヶ月」・荷主は安全確認まで慎重・バンス「デジタル署名済み」・ドーハ事前協議今週開催</p>
<p style="margin:0 0 8px;font-size:0.88rem;line-height:1.7;color:#e2e8f0;">③ <strong>イスラエルが唯一の懸念</strong>——「レバノン撤退せず」・WTI $81.10・ブレント $83.80急落——封鎖110日目・6/19署名で新フェーズへ</p>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ更新

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(134,239,172,0.15);border:1px solid rgba(134,239,172,0.3);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📅 署名6/19スイス</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(134,239,172,0.25);border:1px solid rgba(134,239,172,0.5);color:#86efac;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">🕊️ 和平合意成立・6/19署名</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">💰 WTI $84.88 / Brent $87.33</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">📉 WTI $81.10 / Brent $83.80</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#f87171;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚠️ 閉鎖109日目</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#f87171;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⚠️ 閉鎖110日目</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="display:inline-block;background:rgba(147,51,234,0.15);border:1px solid rgba(147,51,234,0.3);color:#c084fc;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⛏️ 署名待ち・機雷除去準備中</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="display:inline-block;background:rgba(147,51,234,0.15);border:1px solid rgba(147,51,234,0.3);color:#c084fc;font-size:0.72rem;padding:3px 10px;border-radius:12px;margin:3px;">⛏️ 機雷除去最大6ヶ月</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新

### `updated` フィールド更新

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年6月15日 07:09 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年6月16日 08:14 日本時間JST",
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

### `latest` 配列（先頭に3件追加・旧2〜4番目を archive に移動）

#### 旧2〜4番目を archive に移動するため、最古の3件を削除して3件追加

> ⚠️ Claude Code：以下の APPLY ブロックは `"latest": [` を old_str として先頭に3件を prepend する。
> 同時に旧 latest-002・003・004 を archive の先頭バッチに移動すること。

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "id": "latest-001",
      "date": "2026年6月15日（現地）/ 2026年6月16日 JST",
      "title": "【速報】米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」・MOU14条項署名",
      "body": "トランプ大統領がTruth Socialで「イランとの合意が完了した」と宣言。パキスタンPMシャリフが米・イラン双方の「全戦線における即時かつ恒久的な軍事作戦終結」を発表。MOU14条項はホルムズ完全再開・米封鎖解除・核交渉60日後開始・$300億湾岸国再建基金を含む。署名式は6月19日スイスで開催予定。",
      "sourceLabel": "NBC News",
      "label": "🕊️ 和平合意",
      "url": "https://www.nbcnews.com/news/us-news/deal-reached-united-states-iran-war-rcna350039"
    },
    {
      "id": "latest-002",
      "date": "2026年6月15日（現地）/ 2026年6月16日 JST",
      "title": "バンス「MOUデジタル署名済み」・ドーハ事前協議今週——イラン「6/19正式署名まで実施保留」",
      "body": "バンス副大統領がABCニュースで「MOUは日曜日にデジタル署名済み」と確認。米・イラン代表が今週ドーハで事前協議、6/19スイス署名式に備える。一方イラン副外相ガリバブ「6/19正式署名まで実施保留」と慎重姿勢。トランプは「船舶はホルムズから動き出している」とTruth Social投稿。",
      "sourceLabel": "CNN",
      "label": "✍️ 署名準備",
      "url": "https://edition.cnn.com/2026/06/14/world/live-news/iran-war-trump-israel"
    },
    {
      "id": "latest-003",
      "date": "2026年6月15日（現地）/ 2026年6月16日 JST",
      "title": "機雷除去最大6ヶ月・荷主「安全確認まで慎重」——本格通航再開は秋冬以降",
      "body": "米国防総省はホルムズ海峡の機雷除去に最大6ヶ月かかるとの内部見積もり。除去艦3隻が既に展開中。船主・用船者は「市場は正常化を織り込んでいるが、実際に船舶が安定通航するまで慎重」（センタサ・シップ・ブローカーズ）。WTI $81.10（-4.5%）・ブレント $83.80（-4.0%）。正常化後は$65-75見通し。",
      "sourceLabel": "The Globe and Mail",
      "label": "⛏️ 機雷除去",
      "url": "https://www.theglobeandmail.com/business/article-ships-oil-strait-hormuz-us-iran-peace-deal/"
    },
<!-- NEW:END -->
<!-- APPLY:END -->

### `osint` 配列更新（先頭に追加・既存 isLatest:true → false）

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "osint": [
<!-- OLD:END -->
<!-- NEW:START -->
  "osint": [
    {
      "id": "osint-001",
      "titleJa": "【Al Jazeera】米「船舶はホルムズから移動開始」——イランはデジタル署名を未確認・実施は6/19署名後",
      "titleEn": "US says Iran signed deal to end war, ships moving through Strait of Hormuz",
      "country": "Qatar",
      "media": "Al Jazeera",
      "cardBg": "rgba(139,90,43,0.15)",
      "cardBorder": "rgba(217,119,6,0.4)",
      "badgeColor": "rgba(217,119,6,0.25)",
      "borderColor": "rgba(217,119,6,0.5)",
      "textColor": "#fcd34d",
      "url": "https://www.aljazeera.com/news/2026/6/15/trump-says-ships-starting-to-move-through-strait-of-hormuz",
      "date": "2026年6月15日",
      "isLatest": true
    },
<!-- NEW:END -->
<!-- APPLY:END -->

> ⚠️ Claude Code：上記追加後、旧 `"isLatest": true` のエントリー（6/14分）を `"isLatest": false` に変更すること。

---

## [S11] 更新ログ

⚠️ **Claude Code：S11 適用前に以下を実行して確認すること**
```bash
grep -n "6月15日\|6月14日\|6月13日\|6月12日" docs/index.html | head -20
```

### ブロック1: 常時表示エリア（3件固定維持）

> ⚠️ 以下の old_str は「6/15 エントリーの2行」を使って一意性を確保している。
> str_replace 適用後、常時表示が「6/16 + 6/15 + 6/14 の3件」になっているか grep で確認すること。
> 6/13 の行が常時表示に残っている場合は下記ブロック2（逆順）で追加対応すること。

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年6月15日 07:09 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/15 07:09</span> — <strong style="color:#86efac;">【停戦発効】</strong>パキスタンPM「停戦は今すぐ発効」・署名式6/19スイス確定・G7エヴィアン（6/15-17）開幕・イスラエルのベイルート空爆（6/14）で複雑化・カタール調停団テヘランへ・アラグチー「サービス料・ホルムズの剣は永遠」・WTI $84.88・ブレント $87.33・109日目・ニュース4件更新・OSINT更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年6月16日 08:14 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/16 08:14</span> — <strong style="color:#86efac;">【和平合意成立】</strong>米イラン和平合意成立——トランプ「合意完了」・パキスタンPM「永続的停戦」・MOU14条項・6/19スイス署名式・機雷除去最大6ヶ月・WTI $81.10・ブレント $83.80急落・110日目・ニュース3件更新・OSINT更新</div>
        <div>📅 <strong>2026年6月15日 07:09 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/15 07:09</span> — <strong style="color:#86efac;">【停戦発効】</strong>パキスタンPM「停戦は今すぐ発効」・署名式6/19スイス確定・G7エヴィアン（6/15-17）開幕・イスラエルのベイルート空爆（6/14）で複雑化・カタール調停団テヘランへ・アラグチー「サービス料・ホルムズの剣は永遠」・WTI $84.88・ブレント $87.33・109日目・ニュース4件更新・OSINT更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2: log-collapse への 6/13 エントリー挿入

> ⚠️ **Claude Code**: 以下の old_str 内の `[6月13日の日付行]` は
> `grep -n "6月13日" docs/index.html` で確認した実際の HTML に置き換えること。
> log-collapse の先頭（現在: 6/12 XX:XX）の前に 6/13 エントリーを挿入する。

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月12日
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月13日 [Claude Code: grep で時刻を確認して補完] JST</strong> 更新</div>
          <div><span style="color:#94a3b8;">2026/06/13 [時刻]</span> — [Claude Code: grep -n "6月13日" docs/index.html で実際のログ内容を確認し挿入]</div>
          <div>📅 <strong>2026年6月12日
<!-- NEW:END -->
<!-- APPLY:END -->

### JSON-LD dateModified 更新

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-06-15T00:00:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-06-16T00:00:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
[✓] Step 0 — old_str 基準：6月15日 07:09 JST版（プロジェクト知識＋更新ログ照合確認済み・一致）
[✓] C01 タンカー確認 — web検索実施済み・変化なし（6/16 JST 日本船舶新規通過・足止め特段情報なし）
[✓] S01 ヘッダー — 6月15日 07:09 JST → 6月16日 08:14 JST・警戒レベル 最高→高（和平合意・署名待ち）
[✓] S02 TICKER — 米イラン和平合意成立・MOU14条項・6/19署名・機雷除去6ヶ月・WTI$81.10・110日目
[✓] S03 速報インシデント — 6/16 08:14付け・2件新規追加（和平合意成立・デジタル署名＋機雷除去）
[✓] S04 情勢カード3枚 — 外交（和平合意・ドーハ協議）・軍事（機雷除去6ヶ月・イスラエル問題）・エネルギー（WTI$81.10・Brent$83.80）
[✓] S05 COUNTDOWN — 110日目・Phase 9「和平合意成立——6/19スイス署名式まであと3日」
[✓] S06 シナリオ確率補足バナー — 6/16 08:14 JST・A↑↑↑↑↑↑ B↑ C↓↓↓↓ D↓↓↓↓↓
[✓] S07 シナリオ4本 — A（合意成立・機雷除去→段階的完全再開）・B（機雷遅延・慎重再開）・C（イスラエル問題・署名崩壊）・D（合意破棄・軍事再開）
[✓] S07 C/D差別化 — C（イスラエル問題→外交失敗型・署名崩壊）vs D（署名後合意破棄→軍事衝突型）✓
[✓] S07 WTI差別化 — A: $65-75 / B: $80-90 / C: $100-120 / D: $130+ ✓
[✓] S08 シナリオフッター — 6/19署名・機雷除去・イスラエル問題・60日核交渉・IRGC動向
[✓] S08.5 全ルート現況サマリー — 6/16 08:14 JST 再確認済・和平合意成立で近日段階的再開見込み
[✓] S09 30秒カラム — 3行サマリー（和平合意成立・機雷除去6ヶ月・WTI急落）＋バッジ4枚更新
[✓] S10 news_data.json — latest 3件新規（和平合意・デジタル署名・機雷除去）+ 旧1件維持・osint AJ 6/15
[✓] S10 URL確認済 — NBC News ✓ CNN ✓ Globe and Mail ✓ Al Jazeera 6/15 ✓
[✓] S10 osint — 配列先頭追加・既存 isLatest:true → false 変更 ✓
[✓] S11 更新ログ — 2ブロック構成（常時表示3件固定・log-collapse先頭に6/13版挿入）✓
[✓] S11 ブロック2 — 6/13のXX:XXはgrep確認後にClaude Codeが補完するよう注記済み ✓
[✓] S11 JSON-LD — 2026-06-16T00:00:00+09:00（ISO 8601 JST形式）✓
[✓] 全体 — 📰関連最新ニュースにAl Jazeera混入なし ✓（AJはosintのみ）
[✓] 全体 — 習近平 記載なし ✓
[✓] 全体 — Wikipedia/毎日新聞 URL 不使用 ✓
[✓] 全体 — シナリオ確率数値 記載なし（自動同期） ✓
[✓] 全体 — TICKER内JST表記あり ✓
[✓] 全体 — 人名日本語表記：トランプ・バンス・パキスタンPMシャリフ・ガリバブ・イスラエル国防相 ✓
[✓] 全体 — 「二重封鎖」使用なし ✓
[✓] 全体 — 警戒レベル変更（最高→高）理由明記 ✓
```

---

## 🔑 本日の重要事項まとめ（Claude Code 参照用）

| 項目 | 内容 |
|---|---|
| **最重要** | **米イラン和平合意成立（6/15 JST）——MOU14条項署名** |
| 合意内容 | 全面停戦・ホルムズ再開・核60日交渉・$300億再建基金 |
| 署名式 | 6/19スイス・今週ドーハで事前協議 |
| デジタル署名 | バンス「署名済み」・イラン「6/19まで実施保留」 |
| 機雷除去 | 国防総省推定最大6ヶ月・本格通航は秋冬以降 |
| 懸念材料 | イスラエル「レバノン撤退せず」 |
| 油価 | WTI $81.10（-4.5%）・ブレント $83.80（-4.0%） |
| 封鎖日数 | **110日目** |
| C01 | 日本関係船舶：変化なし（6/16 08:14 JST 確認） |

---

## 次ステップ

1. `run.bat` 実行 → `index_html_diffs.md` push
2. Claude Code 定型文送信：
   「git pull --rebase してから、docs/tools/index_html_diffs.md に従って docs/index.html を更新してください。また docs/data/news_data.json も [S10] の指示に従い、既存ファイルに対して新規追加分をマージする形で更新してください。更新完了後に commit してください。push は確認後に指示します。」
3. ⚠️ S11 ブロック2 の `6月13日 XX:XX` は `grep -n "6月13日" docs/index.html` で確認後に補完すること
4. ⚠️ news_data.json の旧 latest-002〜004 を archive に移動すること（3件）
5. commit 確認（`git branch && git log --oneline -3`）→ push 指示
