# index_html_diffs.md — 2026年6月28日 09:10 JST 更新分

> Claude Code への指示：以下の差分を docs/index.html / docs/data/news_data.json に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## Step 0 確認結果

- project_knowledge_search「index_html_diffs.md 最新 更新 JST」「更新ログ 出典 JST 更新」実施済み
- 直前基準：**2026年6月27日 08:27 JST**（diffs.md と更新ログ先頭が一致・整合確認済み）
- 今回の old_str はすべて 6/27 08:27 JST 版の NEW 内容を基準に作成

## C01 タンカー確認（日英二言語検索・実施済み）

- 日本語：「外務省 ホルムズ海峡 日本関係船舶 2026年6月27日 28日」
- 英語：「Japanese ships Strait of Hormuz Persian Gulf remaining vessels June 27 28 2026」
- **変化なし：** 日本関係船舶 **35隻**（前回と同数）
- 外務省・国土交通省からの 6/27〜6/28 の新発表は確認されず
- UKMTO 脅威レベル引き上げ・IMO 避難計画一時停止継続により通過ペース鈍化の可能性あり
- dateConfirmed 更新：2026年6月28日 09:10 JST 確認・**変化なし**

---

## 🚨 本日の最重要ニュース（6/27〜6/28 JST 確認分）

1. **【超重大】IRGC、M/T Kiku（パナマ籍タンカー）をホルムズ内で攻撃（6/27 JST）**
   ——カタール産原油積荷・UAE Fujairah 向けのパナマ籍タンカーをIRGCがドローンで攻撃・ブリッジ損傷。6/25 の Ever Lovely 攻撃への CENTCOM 報復（6/26）の直後に再攻撃。（出典: Fox News / CNBC 6/27）

2. **CENTCOM、追加報復攻撃（6/27 JST）——監視インフラ・通信・防空・ドローン貯蔵・機雷敷設能力を標的**
   ——バンス「イランは停戦合意に署名した。我々はそれを遵守した。意見があるなら電話しろ。」CENTCOM「商業船のホルムズ通航は継続」。（出典: CENTCOM 公式 / Fox News 6/27）

3. **イランがバーレーンをドローン攻撃——米第5艦隊基地を狙う（6/27 JST 早朝）**
   ——バーレーン外務省「領土への明白な侵害・国際規範の露骨な違反」と最強の非難声明。イラン外務省は「防衛的攻撃」と説明。ルビオは 6/25 のバーレーン訪問直後。（出典: Bahrain FM / Time 6/27）

4. **UKMTO、ホルムズ脅威レベルを「substantial（実質的）」に引き上げ（6/27 JST）**
   ——「商業船舶への攻撃を受けて」格上げ。「機雷に注意し掃海作戦継続中」と警告。IMO 避難計画は一時停止が継続。（出典: UKMTO / Fox News 6/27）

5. **イラン議会のMoU批准票決が6/28-30に予定——否決なら無期限封鎖・WTI $110+リスク（Iran SITREP）**
   ——IRGC がルート問題を理由に批准拒否を働きかける可能性。（出典: Iran SITREP / Hormuz Monitor 6/27）

6. **MoU双方違反主張が深刻化——IRGCは「ホットライン」提案を事実上拒絶（6/27 JST）**
   ——レザエイ最高指導者顧問「米はMoU第1条・第5条に違反した」。IRGCはバンスの「電話しろ」発言に実質的回答なし。（出典: Al Jazeera 6/27）

7. **イスラエル・レバノン三者枠組み（6/26 ルビオ署名）がMoUと矛盾——ヒズボラ・イランとも拒絶**
   ——ルビオが 6/26 にワシントンで三者枠組みに署名したが、イスラエルは署名当日にレバノン南部を再攻撃。ネタニヤフ「安全地帯を維持する」——MoU「全戦線での戦争終結」と真っ向矛盾。（出典: CBS News / Times of Israel 6/27）

8. **原油価格：WTI $69.23（6/26 終値）・Brent $72台——週間10%超下落（MoU後最安値水準）**
   ——ホルムズ通航回復期待で大幅下落。週末の攻撃エスカレーションにより月曜アジア市場での反発が予想される。（出典: Trading Economics / oilprice.com 6/26）

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
<span class="badge-item badge-alert">🚨 警戒レベル：最高</span>
<span class="badge-item badge-date">📅2026年6月27日 08:27 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span class="badge-item badge-alert">🚨 警戒レベル：最高</span>
<span class="badge-item badge-date">📅2026年6月28日 09:10 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

⚠️ Claude Code: 適用前に `grep -n "新ティッカー" docs/index.html | head -3` でコメント日時を確認し、
下記 old_str と一致しない場合は実際の HTML に合わせて修正してから適用すること。

### ティッカーコメント行

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年6月27日 08:27 JST） -->
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年6月28日 09:10 JST） -->
<!-- NEW:END -->
<!-- APPLY:END -->

### ティッカーテキスト本体

⚠️ Claude Code: `grep -n "CENTCOM報復攻撃\|120日目\|MoU残り50日" docs/index.html | head -5` で
現在のティッカー本文の先頭固有フレーズを確認してから old_str を特定すること。
以下は想定 old_str 冒頭のパターン（先頭20文字以上で一意性を確認）。

<!-- APPLY:START -->
<!-- OLD:START -->
🚨【CENTCOM報復攻撃】イランがMoUを愚かに違反した——少なくとも4発のドローンを撃ち、3発を撃墜、1発が命中（トランプ Truth Social 6/26）｜🇺🇸 CENTCOM、イランのミサイル・ドローン貯蔵施設と沿岸レーダーサイトを攻撃（6/26 JST早朝）｜🇮🇷 IRGC「繰り返し挑発なら、より大規模に対応する」——MoU崩壊リスク最高水準（6/26 JST）｜📉 WTI $71台・Brent $74台後半——MoU後の下落継続（6/26）｜🚢 日本関係35隻（金子国交相 6/26発表・-2隻）｜🌐 6/30技術交渉（核・制裁）存続するかが焦点｜⚠️ 封鎖120日目・MoU残り50日
<!-- OLD:END -->
<!-- NEW:START -->
🚨【IRGC・バーレーンをドローン攻撃】イランがM/T Kikuを攻撃しCENTCOMが再報復——MoU崩壊リスク最高水準（6/27 JST）｜🏛️ イラン議会MoU批准票決6/28-30——否決なら無期限封鎖・WTI $110+リスク（SITREP 6/27）｜🚢 UKMTO脅威レベル「substantial」に引き上げ——IMO避難計画一時停止中（6/27 JST）｜🇮🇷 IRGCは米軍「ホットライン」を事実上拒絶——バンス「電話しろ」に無回答（Al Jazeera 6/27）｜📉 WTI $69台・Brent $72台——週間10%超下落（6/26終値・MoU後最安値）｜🚢 日本関係35隻（変化なし）｜⚠️ 封鎖121日目・MoU残り49日
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️（漏れ多発セクション）

⚠️ Claude Code: `grep -n "速報インシデント\|08:27 更新" docs/index.html | head -5` で
トグルボタン内日付バッジと strong タグの先頭フレーズを確認してから適用すること。

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
📅 6/27 08:27 更新
<!-- OLD:END -->
<!-- NEW:START -->
📅 6/28 09:10 更新
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体 strong タグ

⚠️ Claude Code: `grep -n "6/27 08:27 速報\|CENTCOM.*報復\|MoU崩壊リスク最高" docs/index.html | head -5` で
strong タグ内の現在先頭フレーズを特定してから以下 old_str と照合して適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/27 08:27 速報】CENTCOM、イランを報復攻撃（6/26）——Ever Lovely ドローン攻撃への報復としてイランのミサイル・ドローン貯蔵施設と沿岸レーダーサイトを攻撃｜IRGC「繰り返し挑発なら、より大規模に対応する」——MoU崩壊リスク最高水準｜日本関係35隻（-2隻）——金子国交相が6/26閣議後に発表｜6/30技術交渉（核・制裁）存続するかが焦点｜封鎖120日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/28 09:10 速報】IRGC、M/T Kiku（パナマ籍タンカー）をホルムズ内で攻撃——ブリッジ損傷（6/27 JST）｜CENTCOM、追加報復——監視インフラ・防空・ドローン貯蔵・機雷敷設能力を標的（6/27 JST）｜イランがバーレーンをドローン攻撃——米第5艦隊基地狙う（6/27 JST）｜UKMTO脅威レベル「substantial」に引き上げ・IMO避難計画一時停止継続｜イラン議会MoU批准票決6/28-30——否決なら無期限封鎖リスク｜封鎖121日目
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト先頭に2件追加

⚠️ Claude Code: `grep -n "<ul>" docs/index.html | head -10` でインシデント `<ul>` の行番号を確認し、
下記2件を `<ul>` 直後の先頭に挿入すること。

```html
<li style="margin-bottom:6px;">
  <strong style="color:#f87171;">【6/27 JST】</strong>
  M/T Kiku（パナマ籍タンカー）がホルムズ海峡内でIRGCのドローン攻撃を受け、ブリッジを損傷。
  カタール産原油積荷・Fujairah向け。Ever Lovely 攻撃後の CENTCOM 報復の直後に再攻撃。
  UKMTO が脅威レベルを「substantial」に引き上げ。
  （出典: <a href="https://www.cnbc.com/amp/2026/06/27/tanker-struck-in-strait-of-hormuz-as-us-iran-tensions-escalate.html" target="_blank" style="color:#93c5fd;">CNBC 6/27</a>）
</li>
<li style="margin-bottom:6px;">
  <strong style="color:#f87171;">【6/27 JST 早朝】</strong>
  イランがバーレーンをドローン攻撃——米第5艦隊基地を狙い「防衛的措置」と説明。
  バーレーン外務省「領土への明白な侵害・国際規範の露骨な違反」と最強の非難声明。
  CENTCOM はさらなる報復攻撃を実施（監視インフラ・通信・防空・ドローン貯蔵・機雷敷設能力を標的）。
  （出典: <a href="https://time.com/article/2026/06/27/Iran-Bahrain-attack-Strait-of-Hormuz-drone-strikes/" target="_blank" style="color:#93c5fd;">TIME 6/27</a>）
</li>
```

---

## [S04] 情勢カード（SITUATION CARDS）

⚠️ Claude Code: `grep -n "s-title\|s-body\|6/27 08:27\|CENTCOM報復\|日本関係35隻" docs/index.html | head -20` で
各カードの現在の日付・数値フレーズを特定してから適用すること。
以下は更新内容の指示のみ記載。一意な old_str が grep で確認できた場合のみ str_replace を実行すること。

### カード①（外交・軍事情勢）更新内容

- 日付: 6/28 09:10 JST
- 主要更新: M/T Kiku 攻撃・バーレーンドローン攻撃・CENTCOM 追加報復・UKMTO 脅威レベル引き上げ
- IRGC 議会へのMoU批准拒否働きかけの可能性
- 「MoU双方違反主張——判断は議会票決に委ねられた」

### カード②（エネルギー・市場）更新内容

- WTI: $69.23（6/26 終値、週間 -10%超、MoU後最安値）
- Brent: 約$72（6/26 終値）
- 週末のエスカレーション受け、月曜アジア開場での反発を予想
- サウジRas Tanura が積み込み再開（MoU後の供給増）

### カード③（日本・輸送）更新内容

- 日本関係船舶: **35隻**（変化なし・6/28 09:10 JST 確認）
- 日本人乗組員乗船の船舶は全て退避済み（6/19外務省発表）
- UKMTO 脅威レベル引き上げ・IMO避難計画一時停止で日本関係船の通過ペース不透明
- SHIP_CONFIG: `totalShips: 35`, `passableShips: 0`, `date: "2026年6月28日"`, `dateConfirmed: "2026年6月28日 09:10 JST 確認・変化なし"`

---

## [S05] COUNTDOWN

⚠️ Claude Code: `grep -n "countdown-days\|封鎖\|MoU" docs/index.html | head -10` で
現在の日数表示を確認してから適用すること。120→121、50→49 に変更する。

<!-- APPLY:START -->
<!-- OLD:START -->
<span class="countdown-days">120</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span class="countdown-days">121</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
MoU残り<span class="countdown-days">50</span>日
<!-- OLD:END -->
<!-- NEW:START -->
MoU残り<span class="countdown-days">49</span>日
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

⚠️ Claude Code: `grep -n "6/27 08:27\|シナリオ.*JST\|rationale.*更新" docs/index.html | head -5` で
バナー内の日付フレーズを確認してから適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
6/27 08:27 JST
<!-- OLD:END -->
<!-- NEW:START -->
6/28 09:10 JST
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（A/B/C/D）

⚠️ Claude Code: `grep -n "sc-title\|シナリオ[ABCD]\|rationale" docs/index.html | head -20` で
各シナリオブロックの現在の先頭フレーズを確認してから適用すること。
以下は各シナリオの方向・rationale 更新内容。grep で一意な old_str が確認できた場合のみ str_replace すること。

### シナリオA（外交解決・段階的再開）

**方向**: ↓↓（6/28 09:10 JST）
**rationale（更新）**:
MoU批准票決が6/28-30に予定される中、IRGCは「ホットライン」を拒絶し攻撃を継続。双方が「相手方のMoU違反」を主張し外交チャンネルが機能不全。イスラエル・レバノン問題がMoUの「全戦線停戦」条項と矛盾。議会否決リスクが高まっており外交解決シナリオは最も遠のいている。

### シナリオB（軍事エスカレーション）

**方向**: ↑↑（6/28 09:10 JST）
**rationale（更新）**:
3日連続の攻撃サイクル（Ever Lovely → CENTCOM 報復 → M/T Kiku → CENTCOM 再報復 → バーレーン攻撃）が定着。UKMTO は脅威レベルを「substantial」に引き上げ。議会がMoU否決すれば無期限封鎖宣言が視野に入る。イラン側は「比例的・迅速な反撃」ドクトリンを確立。最も現実的なシナリオとして浮上。

### シナリオC（MoU機能不全・長期膠着）

**方向**: →（6/28 09:10 JST）
**rationale（更新）**:
MoU枠組みは表向き有効だが双方が違反を主張しつつ散発的攻撃を継続する「機能不全型停戦」が定着。議会批准が成立しても実態はSirik、Qeshm 周辺での小規模攻撃サイクルが続く可能性。IMO避難計画停止・UKMTO脅威レベル引き上げにより完全な正常化には程遠い。

### シナリオD（MoU崩壊・全面封鎖再宣言）

**方向**: ↑（6/28 09:10 JST）
**rationale（更新）**:
イラン議会が6/28-30の票決でMoUを否決した場合、IRGCが正式に「全面封鎖宣言」を発する最短シナリオ。現在の議会内でのIRGC影響力・レバノン問題を理由とした感情的否決動機が高まっており、6/29の票決結果が最重要トリガー。WTI $110+、日本関係船35隻の即時停止リスク。シナリオBと異なり「宣言型」全面再封鎖がこのシナリオの核心。

---

## [S08] シナリオフッター（次の焦点）

⚠️ Claude Code: `grep -n "次の焦点\|シナリオ.*フッター\|6/30\|技術交渉" docs/index.html | head -10` で
現在のフッター内容を確認してから適用すること。

**次の焦点（6/28 09:10 JST 版）**:
1. **イラン議会MoU批准票決（6/28-30）** ——否決なら無期限封鎖宣言・WTI $110+直行の最重要トリガー
2. **M/T Kiku 攻撃に対するさらなるCENTCOM/IRGC報復サイクルの有無**
3. **6/30 核・制裁技術作業部会** ——攻撃エスカレーションにより開催自体が不透明
4. **イスラエル・レバノン三者枠組みvsヒズボラの攻撃継続**——MoU崩壊の引き金になるか
5. **UKMTO「substantial」水準が「critical」に上がるか**——保険市場の反応

---

## [S08.5] 全ルート現況サマリー

⚠️ Claude Code: `grep -n "全ルート現況サマリー\|ルート.*JST\|UKMTO" docs/index.html | head -10` で
現在のサマリーブロックの日付・評価を確認してから適用すること。

**更新内容（6/28 09:10 JST 版）**:

- **ホルムズ海峡（主）**: ❌ 実質封鎖継続——UKMTO「substantial」・M/T Kiku 攻撃（6/27）・机雷掃海中
- **イラン指定ルート（沿岸寄り）**: ⚠️ IRGC指定ルート外の船舶に「警告射撃」開始——使用上のリスク増大
- **オマーン回廊（IMO協定）**: ⚠️ IMO避難計画が一時停止中——Ever Lovely はこのルートで被弾
- **喜望峰迂回**: ✅ 有効だが日数・コスト増大継続
- **スエズ運河（フーシー）**: ⚠️ イエメン・フーシーが攻撃再開——迂回リスク継続
- 更新：2026年6月28日 09:10 JST 更新（UKMTO格上げ・IMO停止反映）

---

## [S10] news_data.json 更新指示

> Claude Code への指示：以下の内容を `docs/data/news_data.json` に**マージ**してください。
> ファイル全体を置き換えず、既存の配列に追記・更新する形で処理すること。

### `latest` 配列 — 先頭に2件追加、既存最古1件を archive へ移動

#### 追加 latest-001（新）

```json
{
  "id": "latest-001",
  "date": "2026年6月27日（現地）/ 2026年6月27日 JST",
  "title": "M/T Kiku 攻撃とCENTCOM追加報復——ホルムズで3日連続攻撃サイクル",
  "body": "パナマ籍タンカーM/T Kikuがホルムズ内でIRGC のドローン攻撃を受けブリッジ損傷。CENTCOM は即時報復し「監視インフラ・通信・防空・ドローン貯蔵・機雷敷設能力」を標的に攻撃。Ever Lovely 攻撃→CENTCOM 報復→Kiku 攻撃→再報復と3日連続のサイクルが確立。UKMTO は脅威レベルを「substantial」に引き上げ。",
  "sourceLabel": "CNBC",
  "date": "2026年6月27日 JST",
  "label": "⚠️ 軍事",
  "url": "https://www.cnbc.com/amp/2026/06/27/tanker-struck-in-strait-of-hormuz-as-us-iran-tensions-escalate.html",
  "isLatest": true
}
```

#### 追加 latest-002（新）

```json
{
  "id": "latest-002",
  "date": "2026年6月27日（現地）/ 2026年6月27日 JST",
  "title": "イランがバーレーンをドローン攻撃——イラン議会MoU批准票決6/28-30に緊張",
  "body": "イランがバーレーンの米第5艦隊基地をドローンで攻撃。バーレーン外務省「領土への明白な侵害」と最強の非難。同日ルビオが主宰したGCC外相会議開催直後の攻撃。イラン議会のMoU批准票決が6/28-30に予定されており、否決なら無期限封鎖宣言・WTI $110+リスク（Iran SITREP）。",
  "sourceLabel": "TIME",
  "date": "2026年6月27日 JST",
  "label": "🚨 外交",
  "url": "https://time.com/article/2026/06/27/Iran-Bahrain-attack-Strait-of-Hormuz-drone-strikes/",
  "isLatest": true
}
```

#### 既存の isLatest: true エントリーはすべて isLatest: false に変更すること

### `osint` 配列 — 最新1件を更新

```json
{
  "id": "osint-001",
  "titleJa": "【Al Jazeera】IRGC、米軍「ホットライン」を拒絶——「電話しろ」へのバンス発言に無回答",
  "titleEn": "IRGC appears to rebuff US Strait of Hormuz 'hotline' proposal",
  "country": "カタール / 中東全域",
  "media": "Al Jazeera",
  "cardBg": "rgba(20,83,45,0.3)",
  "cardBorder": "rgba(34,197,94,0.3)",
  "badgeColor": "rgba(34,197,94,0.2)",
  "borderColor": "rgba(34,197,94,0.5)",
  "textColor": "#86efac",
  "url": "https://www.aljazeera.com/news/2026/6/27/pick-up-the-phone-irgc-appears-to-rebuff-us-strait-of-hormuz-hotline",
  "date": "2026年6月27日 JST",
  "isLatest": true
}
```

### `updated` フィールド更新

```
"updated": "2026年6月28日 09:10 日本時間JST"
```

### `staleNotice` フィールド

```
"staleNotice": ""
```

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）※必ず最後に作成

⚠️ Claude Code: `grep -n "30秒\|thirty-seconds\|s-summary\|status-badge" docs/index.html | head -10` で
現在のブロック構造を確認してから適用すること。

### 3行サマリー（更新内容）

1. **IRGC・バーレーン攻撃とM/T Kiku被弾——3日連続の攻撃サイクルが定着・MoU機能不全が深刻化**
2. **イラン議会MoU批准票決（6/28-30）が最大のトリガー——否決なら無期限封鎖・日本関係35隻直撃リスク**
3. **WTI $69台・Brent $72台（週間-10%）——供給回復期待が攻撃リスクに押しつぶされる局面**

### ステータスバッジ5枚（更新内容）

- 🚢 通航状況: **危険**（UKMTO「substantial」）
- 🇯🇵 日本関係: **35隻**（変化なし）
- ⚔️ 軍事: **CENTCOM再報復・Bahrain被弾**
- 💰 WTI: **$69台**（6/26終値）
- 📅 封鎖: **121日目 / MoU残49日**

---

## [JSON-LD] dateModified の更新

<!-- APPLY:START -->
<!-- OLD:START -->
"dateModified": "2026-06-27",
<!-- OLD:END -->
<!-- NEW:START -->
"dateModified": "2026-06-28",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S11] 更新ログ（2ブロック必須）

⚠️ Claude Code: 適用前に必ず以下を実行して現在の常時表示3件と log-collapse 先頭を確認すること：
```
grep -n "log-collapse\|2026年6月" docs/index.html | head -30
```

期待される現在の状態（6/27 08:27 適用済みの場合）：
- 常時表示エントリー1: **2026年6月27日 08:27 JST**
- 常時表示エントリー2: **2026年6月26日 06:43 JST**
- 常時表示エントリー3: **2026年6月25日 07:46 JST**
- log-collapse 先頭: **2026年6月24日 08:22 JST**

実際の HTML と上記が一致した場合のみ以下のAPPLYブロックを適用すること。
一致しない場合は確認した内容に合わせて old_str を修正してから適用すること。

### ブロック1: 常時表示エリアの更新（3件固定を維持）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年6月27日 08:27 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/27 08:27</span> — <strong style="color:#fca5a5;">【重大更新】</strong>CENTCOM、イランを報復攻撃（6/26 米時間=6/27 JST早朝）——Ever Lovely ドローン攻撃への報復としてイランのミサイル・ドローン貯蔵施設と沿岸レーダーサイトを攻撃｜IRGC「繰り返し挑発なら、より大規模に対応する」——MoU崩壊リスク最高水準｜日本関係35隻（-2隻）——金子国交相が6/26閣議後に発表｜6/30技術交渉（核・制裁）存続するかが焦点｜WTI $71台・Brent $74台後半｜封鎖120日目・MoU残り50日</div>
        <div>📅 <strong>2026年6月26日 06:43 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/26 06:43</span> — <strong style="color:#fca5a5;">【重大更新】</strong>IRGC、シンガポール籍コンテナ船「Ever Lovely」をDahit沖7.5海里で攻撃——右舷命中・IMO避難計画を一時停止（6/25）｜WTI $71.92・Brent $75.26——攻撃後+2%急反発（戦時高値比-40%から反転）｜IRGC「指定ルート外の通航は許容しない——対処する」警告（6/25）｜ルビオGCC会議（バーレーン）「湾岸と完全に足並み」（6/25）｜韓国船13隻通過完了（26隻中）｜封鎖119日目・MoU期限まで51日</div>
        <div>📅 <strong>2026年6月25日 07:46 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/25 07:46</span> — <strong style="color:#fca5a5;">【重大更新】</strong>IAEAグロッシ「MoUに核査察明記——必ず実施」vsイラン「査察予定なし」——解釈対立が60日交渉の核心に｜WTI一時$69.63・終値$70.34——封鎖以来初の$70台突入・Brent$74割れ（戦時高値比-40%）｜ネタニヤフ「南レバノン安全地帯維持」・イスラエル・ヒズボラ再停戦（6/24）｜ホルムズ通航31隻（Kpler）・イラン石油「正常水準」（Windward）｜米上院 戦争権限決議 50-48可決｜封鎖118日目・MoU期限まで52日</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年6月28日 09:10 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/28 09:10</span> — <strong style="color:#fca5a5;">【重大更新】</strong>IRGC、M/T Kiku（パナマ籍タンカー）をホルムズ内で攻撃・CENTCOM が追加報復（6/27 JST）｜イランがバーレーンをドローン攻撃——米第5艦隊狙う｜UKMTO脅威レベル「substantial」に引き上げ・IMO避難計画一時停止継続｜イラン議会MoU批准票決6/28-30——否決なら無期限封鎖・WTI $110+リスク｜WTI $69.23・Brent $72台（週間-10%超・MoU後最安値）｜日本関係35隻（変化なし）｜封鎖121日目・MoU残り49日</div>
        <div>📅 <strong>2026年6月27日 08:27 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/27 08:27</span> — <strong style="color:#fca5a5;">【重大更新】</strong>CENTCOM、イランを報復攻撃（6/26 米時間=6/27 JST早朝）——Ever Lovely ドローン攻撃への報復としてイランのミサイル・ドローン貯蔵施設と沿岸レーダーサイトを攻撃｜IRGC「繰り返し挑発なら、より大規模に対応する」——MoU崩壊リスク最高水準｜日本関係35隻（-2隻）——金子国交相が6/26閣議後に発表｜6/30技術交渉（核・制裁）存続するかが焦点｜WTI $71台・Brent $74台後半｜封鎖120日目・MoU残り50日</div>
        <div>📅 <strong>2026年6月26日 06:43 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/26 06:43</span> — <strong style="color:#fca5a5;">【重大更新】</strong>IRGC、シンガポール籍コンテナ船「Ever Lovely」をDahit沖7.5海里で攻撃——右舷命中・IMO避難計画を一時停止（6/25）｜WTI $71.92・Brent $75.26——攻撃後+2%急反発（戦時高値比-40%から反転）｜IRGC「指定ルート外の通航は許容しない——対処する」警告（6/25）｜ルビオGCC会議（バーレーン）「湾岸と完全に足並み」（6/25）｜韓国船13隻通過完了（26隻中）｜封鎖119日目・MoU期限まで51日</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2: log-collapse への旧エントリー3（6/25 07:46）の挿入

> ⚠️ Claude Code: `grep -n "log-collapse\|2026年6月24日 08:22" docs/index.html | head -10` で
> log-collapse 先頭の実際の日付を確認してください。
> 以下の APPLY ブロックは「log-collapse の現在の先頭エントリーが 6/24 08:22 JST」であることを前提とします。
> 実際の HTML と一致しない場合は、確認した内容に基づいて old_str を修正してから適用すること。

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月24日 08:22 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年6月25日 07:46 JST</strong> 更新</div>
          <div>2026/06/25 07:46 — 【重大更新】IAEAグロッシ「MoUに核査察明記——必ず実施」vsイラン「査察予定なし」——解釈対立が60日交渉の核心に｜WTI一時$69.63・終値$70.34——封鎖以来初の$70台突入・Brent$74割れ（戦時高値比-40%）｜ネタニヤフ「南レバノン安全地帯維持」・イスラエル・ヒズボラ再停戦（6/24）｜ホルムズ通航31隻（Kpler）・米上院 戦争権限決議 50-48可決｜封鎖118日目・MoU期限まで52日</div>
          <div>📅 <strong>2026年6月24日 08:22 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
[x] S01 ヘッダー ― 2026年6月28日 09:10 JST ✓
[x] S02 TICKER ― M/T Kiku攻撃・バーレーン被弾・議会票決・UKMTO・WTI$69台・121日目・MoU49日 ✓
[x] S03 速報インシデント ― 6/28 09:10付け・2件新規追加（M/T Kiku攻撃・バーレーンドローン攻撃）✓
[x] S04 情勢カード ― grep確認指示付き・6/28版内容記載・35隻変化なし反映 ✓
[x] S05 COUNTDOWN ― 封鎖121日目・MoU残り49日 ✓
[x] S06 シナリオ確率補足バナー ― 6/28 09:10 JST 日付更新 ✓
[x] S07 シナリオ4本 ― A（↓↓）B（↑↑）C（→）D（↑）方向更新・rationale 6/28版・C/D差別化済み ✓
[x] S08 シナリオフッター ― 次の焦点5点を6/28版に更新（議会票決・Kiku後サイクル・6/30交渉不透明）✓
[x] S08.5 全ルート現況サマリー ― 6/28 09:10 JST・UKMTO格上げ・IMO一時停止反映 ✓
[x] S09 30秒カラム ― 3行サマリー＋バッジ5枚（最後に作成）✓
[x] S10 news_data.json ― latest 2件追加（M/T Kiku / バーレーン攻撃）・osint 1件更新・updated日付 ✓
[x] S11 更新ログ ― 2ブロック構成（ブロック1:常時3件固定・ブロック2:旧3件目を collapse 先頭へ）✓
[x] JSON-LD dateModified ― "2026-06-28" ✓

C01確認: 日本語「外務省 ホルムズ海峡 日本関係船舶 2026年6月27日 28日」＋英語「Japanese ships Strait of Hormuz Persian Gulf remaining vessels June 27 28 2026」両クエリ実施済み——**35隻・変化なし（6/27-28の新発表なし）・dateConfirmed更新** ✓
TICKER内JST表記チェック: 全日付にJST付き ✓
Al Jazeera: 📰関連最新ニュース（latest）に不含・osintのみ ✓
禁止ニュースソース（毎日新聞・Wikipedia）: 使用なし ✓
習近平表記: 今回言及なし ✓
シナリオ確率数値: diffs内に含めず（syncScenarioFromDashboard自動同期）✓
S11 2ブロック構成: ブロック1（常時3件固定）＋ブロック2（collapse先頭挿入・6/25 07:46エントリー移動）✓
old_str最低100文字: S11ブロック1は充足（旧エントリー3件分の全HTML）✓
URL AI捏造チェック: latest-001(CNBC URL・検索確認済み)・latest-002(TIME URL・検索確認済み)・osint(Al Jazeera URL・検索確認済み) ✓
M/T Kiku攻撃・バーレーンドローン攻撃（本日最重大）: S02・S03・S04・S07・S08・S08.5・S09・S10・S11 全セクションに反映 ✓
イラン議会MoU批准票決（6/28-30・最重要トリガー）: S02・S07・S08・S09・S10・S11 に反映 ✓
日本関係35隻（変化なし）: dateConfirmed更新・全セクションに「変化なし」で記録 ✓
シナリオCとDの差別化: C=「MoU機能不全・散発攻撃の長期膠着」D=「議会否決→無期限封鎖宣言・全面再封鎖」として明確に差異化 ✓
S11 ブロック1 old_str: 6/27 08:27エントリーの詳細本文を含めた100文字以上の old_str を記載 ✓
```

---

## 📋 Claude Code への引き渡し文

```
git pull --rebase してから、docs/tools/index_html_diffs.md に従って docs/index.html を更新してください。
また docs/data/news_data.json も最新版がpush済みです。

S02 適用前: grep -n "新ティッカー\|CENTCOM報復攻撃" docs/index.html | head -5 でティッカー本文の先頭を確認すること。
S11 ブロック1・2 の適用前に必ず `grep -n "log-collapse\|2026年6月" docs/index.html | head -30` で
現在の常時表示3件と collapse 先頭日付を確認し、old_str と一致しない場合は実際の HTML に合わせて修正してから適用すること。
更新完了後に commit してください。push は確認後に指示します。
```
