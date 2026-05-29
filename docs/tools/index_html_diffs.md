# index_html_diffs.md — 2026年5月29日 09:42 JST 更新分

> Claude Code への指示：以下の差分を `docs/index.html`（および `docs/data/news_data.json`）に適用してください。
> 変更箇所以外は絶対に触らないこと。
> 作業後に `git commit`（メッセージ: `update: 2026-05-29 09:42 JST`）してください。push は確認後に指示します。

---

## ⚠️ Claude Code 向け特別指示（S09について）

**S09（「海峡の今」「次の焦点」バッジ5枚）は4日間のスマホ更新で未適用のまま残っている。**
以下の手順で対応すること：

1. `view_range` で `docs/index.html` の `<!-- 30秒で全体像を把握 -->` セクション全体を確認
2. 「海峡の今」「次の焦点」バッジ5枚の現在テキストを把握
3. 本ファイル末尾の「[S09] Claude Code 適用内容」に従って `str_replace` を実施
4. APPLY ブロック失敗 (#エラー) がある場合も Claude Code が補完すること

---

## [S10] news_data.json 更新

> ⚠️ news_data.json は Claude Code が既存ファイルにマージすること（上書き禁止）。
> run.bat は news_data.json を push しない。

### `updated` フィールド更新

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "updated": "2026年5月28日 10:59 日本時間JST",
<!-- OLD:END -->
<!-- NEW:START -->
  "updated": "2026年5月29日 09:42 日本時間JST",
<!-- NEW:END -->
<!-- APPLY:END -->

### `staleNotice` フィールド

```
"staleNotice": ""
```
（本日は超重要進展あり → 空文字）

### `latest` 配列に2件を先頭追加

<!-- APPLY:START -->
<!-- FILE:docs/data/news_data.json -->
<!-- OLD:START -->
  "latest": [
<!-- OLD:END -->
<!-- NEW:START -->
  "latest": [
    {
      "title": "米・イランが60日MOU草案で暫定合意——ホルムズ機雷除去30日・「無制限」通航・核交渉開始・トランプ最終署名待ち",
      "body": "米・イランの交渉担当者が60日間の停戦延長MOU草案に合意（Axios独占スクープ→CBS・CNBC・CNN・Euronews等が確認）。ホルムズ海峡の機雷を30日以内に除去し「無制限」通航を回復、並行して核交渉・制裁緩和・資産凍結解除を協議する枠組み。ただしトランプは「まだ満足していない」として最終署名を保留、イランも公式には合意を確認していない。ベッセント財務長官「ウラン引渡しと海峡無制限開放が前提条件」と強調。ルビオとパキスタン外相イスハク・ダールが5/29ワシントンで会談し推進図る。",
      "sourceLabel": "Axios",
      "date": "2026年5月29日",
      "label": "🕊️ 外交",
      "url": "https://www.axios.com/2026/05/28/iran-peace-deal-trump-approval"
    },
    {
      "title": "IRGCがクウェートへ弾道ミサイル発射・米空軍基地を攻撃——CENTCOM「重大な停戦違反」・新型防空「Arash-e Kamangir」でReaper撃墜",
      "body": "IRGCが5/28（GMT）にクウェートへ弾道ミサイルを発射、クウェート軍が迎撃。同日にIRGCが米空軍基地（場所非公開）を攻撃——米軍のバンダルアッバース付近への新たな空爆への報復と主張。CENTCOMは「重大な停戦違反」と非難。イランは国産新型防空システム「Arash-e Kamangir」で米MQ-9 Reaperをケシュム島付近で撃墜したとも発表（初の戦闘使用）。原油はこれらの攻撃報告でWTI $91前後・ブレント $97前後に反発。",
      "sourceLabel": "Washington Times",
      "date": "2026年5月29日",
      "label": "💥 衝突",
      "url": "https://www.washingtontimes.com/news/2026/may/28/us-military-confirms-iran-launched-attacks-kuwait-test-ceasefire/"
    },
<!-- NEW:END -->
<!-- APPLY:END -->

### `osint`（現地メディア視点）: 先頭に1件追加・既存を `isLatest: false` に変更

```
osint：配列先頭に以下の新記事を追加し、既存記事は isLatest: false に変更してそのまま残すこと。配列ごとの置き換えは禁止。

新規追加（isLatest: true）:
{
  "id": "osint-2026-0528",
  "titleJa": "【Al Jazeera】ライブブログ：米・イランが60日MOU草案で暫定合意——ホルムズ機雷除去30日・無制限通航・核交渉開始（トランプ署名待ち）・イランが「Arash-e Kamangir」でReaper撃墜・クウェートへ弾道ミサイル",
  "titleEn": "US and Iran reach MoU on 60-day truce, Trump's approval still pending — Iran uses new Arash-e Kamangir to down MQ-9, fires ballistic missile at Kuwait",
  "country": "カタール",
  "media": "Al Jazeera",
  "cardBg": "rgba(0,168,132,0.08)",
  "cardBorder": "rgba(0,168,132,0.4)",
  "badgeColor": "#00a884",
  "borderColor": "#00a884",
  "textColor": "#6ee7d0",
  "url": "https://www.aljazeera.com/news/liveblog/2026/5/28/iran-war-live-israel-orders-mass-forced-displacement-for-all-south-lebanon",
  "date": "2026/05/28",
  "isLatest": true
}
```

---

## [S02] TICKER

### コメント行

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年5月28日 10:59 JST） -->
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年5月29日 09:42 JST） -->
<!-- NEW:END -->
<!-- APPLY:END -->

### ティッカー本文（末尾の封鎖日数を含む一意フレーズで置換）

<!-- APPLY:START -->
<!-- OLD:START -->
⚠️ 停戦継続中も通航量は戦前比95%減——封鎖90日目（3ヶ月目突入）
<!-- OLD:END -->
<!-- NEW:START -->
⚠️ 停戦91日目——60日MOU草案合意・トランプ最終署名で「史上最大の外交突破口」か「崩壊」かの正念場（5/29 09:42 JST）
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
🚨【米軍「自衛攻撃」・IRGCドローン4機撃墜】
<!-- OLD:END -->
<!-- NEW:START -->
🚨【歴史的局面・60日MOU草案で暫定合意】米・イランの交渉担当者が60日間の停戦延長MOU草案に合意——ホルムズ機雷除去（30日以内）・「無制限」通航・核交渉開始の枠組み（Axios独占 5/28 GMT確認）。トランプ最終署名待ち・イラン未確認（5/29 09:42 JST）｜💥 IRGCがクウェートへ弾道ミサイル発射（迎撃済）・米空軍基地を攻撃——CENTCOM「重大な停戦違反」（5/28 JST）｜🛩️ イラン「Arash-e Kamangir」新型防空システムで米MQ-9 Reaperをケシュム島付近で撃墜（初の戦闘使用 5/28 JST）｜🤝 ルビオ・パキスタン外相イスハク・ダール本日ワシントンD.C.で会談——MOU推進の鍵｜🇪🇺 EUが対イラン制裁拡大——「ホルムズ封鎖は国際法違反」と決定（5/28 JST）｜
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️（漏れ多発セクション）

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
📅 5/28 10:59 更新
<!-- OLD:END -->
<!-- NEW:START -->
📅 5/29 09:42 更新
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の `<strong>` タグを置き換え）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【5/28 10:59 速報】
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【5/29 09:42 速報】米・イランが60日MOU草案で暫定合意（トランプ最終署名待ち・イラン未確認）——ホルムズ機雷除去30日・無制限通航・核交渉開始の枠組み（Axios 5/28 GMT）｜IRGCがクウェートへ弾道ミサイル発射（迎撃済）・米空軍基地攻撃——CENTCOM「重大な停戦違反」（5/28 JST）｜イランが「Arash-e Kamangir」新型防空システムで米MQ-9 Reaperをケシュム島付近で撃墜——初の戦闘使用（5/28 JST）｜停戦91日目・署名か崩壊かの正念場
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に2件追加）

> ⚠️ `<ul>` の直後に以下の2件を追記すること（既存リストは変更しない）。

```html
<li style="margin-bottom:8px;padding:8px 10px;background:rgba(239,68,68,0.07);border-left:3px solid #ef4444;border-radius:4px;">
  <strong style="color:#fca5a5;">🕊️ 【米・イランが60日MOU草案で暫定合意・トランプ最終署名待ち】（2026年5月28日 GMT / 5月29日 JST）：</strong>
  Axiosが独占報道し各紙確認。米・イランの交渉担当者が60日間のMOU草案に合意——ホルムズ機雷除去（30日以内）・「無制限」通航回復・核交渉・制裁緩和協議を包括した枠組み。トランプは「まだ満足していない」として最終署名保留。ベッセント財務長官「ウラン引渡し・海峡無制限開放が前提」。ルビオとパキスタン外相ダールが5/29ワシントンで会談。
  <span style="font-size:0.75rem;color:#64748b;display:block;margin-top:6px;">📡 Axios・CNBC・CBS News・Washington Times・Euronews（2026年5月29日 09:42 日本時間JST）</span>
</li>
<li style="margin-bottom:8px;padding:8px 10px;background:rgba(239,68,68,0.07);border-left:3px solid #ef4444;border-radius:4px;">
  <strong style="color:#fca5a5;">💥 【IRGCがクウェートへ弾道ミサイル発射・米空軍基地を攻撃・新型防空「Arash-e Kamangir」でReaper撃墜】（2026年5月28日 JST）：</strong>
  IRGCが5/28（GMT）にクウェートへ弾道ミサイルを発射（クウェート軍が迎撃）・米空軍基地（場所非公開）を攻撃——米軍の南イラン空爆への報復。CENTCOMが「重大な停戦違反」と非難。イランは新型防空システム「Arash-e Kamangir」でケシュム島付近の米MQ-9 Reaperを撃墜と発表（初の戦闘使用）。
  <span style="font-size:0.75rem;color:#64748b;display:block;margin-top:6px;">📡 Washington Times・CENTCOM・Al Jazeera（2026年5月29日 09:42 日本時間JST）</span>
</li>
```

---

## [S04] 情勢カード3枚

### カード① 停戦・封鎖状況

<!-- APPLY:START -->
<!-- OLD:START -->
<strong>封鎖90日目（3ヶ月目突入）</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong>封鎖91日目——60日MOU草案で暫定合意</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
2026年5月28日 10:59 JST 更新
<!-- OLD:END -->
<!-- NEW:START -->
2026年5月29日 09:42 JST 更新
<!-- NEW:END -->
<!-- APPLY:END -->

### カード② 原油・経済影響

<!-- APPLY:START -->
<!-- OLD:START -->
<strong>ブレント $95〜96/bbl</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong>WTI $91/bbl前後・ブレント $97/bbl前後</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
合意期待で下落継続（週次2連続）。EIA STEO「2Q26在庫日量850万bbl減・Brent $106/bbl予測（5〜6月）」。IRGCが25隻以上の通過を許可・管理。🇯🇵 日本籍タンカーが戦争後初のホルムズ通過・日本着を確認（CNN 5/26）。出典：TradingEconomics・CNN・EIA STEO（5/28 JST確認）
<!-- OLD:END -->
<!-- NEW:START -->
60日MOU草案合意報道で大幅下落後、IRGC→クウェートミサイル・米基地攻撃で反発。WTI 5/28終値$88.90→5/29朝$91前後、ブレント $93.71→$97前後。MOU署名確定なら$75〜80急落シナリオ。IRGC「Arash-e Kamangir」新型防空使用で不確実性残存。出典：TradingEconomics・CNBC（5/29 09:42 JST確認）
<!-- NEW:END -->
<!-- APPLY:END -->

### カード③ 海峡・通航状況

<!-- APPLY:START -->
<!-- OLD:START -->
<strong>封鎖90日目（3ヶ月目突入）</strong>——通航量は戦前比95%減継続。
<!-- OLD:END -->
<!-- NEW:START -->
<strong>封鎖91日目——MOU草案でホルムズ機雷除去30日条項合意</strong>——通航量は戦前比95%減継続（MOU署名確定まで）。
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
出典：CENTCOM・CNN・Al Jazeera（5/28 10:59 JST更新）
<!-- OLD:END -->
<!-- NEW:START -->
出典：Axios・CENTCOM・CNN・Washington Times（5/29 09:42 JST更新）
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

### フェーズラベル

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="color:#fbbf24;">⚠️ MOU最終調整中——核条項・IRGC批准の壁が残る（5/28 10:59 JST 更新）</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="color:#4ade80;">🕊️ 60日MOU草案で暫定合意——トランプ最終署名の判断待ち（5/29 09:42 JST 更新）</span>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
🕊️ <strong>外交交渉フェーズ（MOU最終調整）——「数日内署名」目標・核条項・IRGC批准の壁 ／ 停戦90日目</strong>
<!-- OLD:END -->
<!-- NEW:START -->
🕊️ <strong>外交交渉フェーズ（60日MOU草案暫定合意）——ホルムズ機雷除去30日・無制限通航・核交渉開始の枠組み ／ トランプ署名が唯一の関門 ／ 停戦91日目</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

<!-- APPLY:START -->
<!-- OLD:START -->
<span style="font-weight:800;color:#f87171;">📊 2026年5月28日 10:59 JST 更新</span><br>
<!-- OLD:END -->
<!-- NEW:START -->
<span style="font-weight:800;color:#4ade80;">📊 2026年5月29日 09:42 JST 更新</span><br>
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
🅐 外交解決 <span style="color:#4ade80;">↑</span> — 米CENTCOM 攻撃下でもカタール協議は継続。MOU「大枠合意」は維持されているが、米軍攻撃がイランSNSC・最高指導者の批准判断を遅延させるリスク（5/27 09:17 JST）<br>
  🅑 部分封鎖 <span style="color:#fbbf24;">→</span> — IRGCの「管制海域」制度が既成事実化。交渉失敗時の最有力帰着点。変化なし<br>
  🅒 完全封鎖 <span style="color:#fbbf24;">→</span> — 米CENTCOM 攻撃でIRGC報復リスクが再上昇。前回の↓から→に修正——機雷追加敷設・封鎖強化シナリオが現実味<br>
  🅓 軍事拡大 <span style="color:#f87171;">↑</span> — IRGCがMQ-9 Reaper撃墜・「報復権を保有」と宣言。直接軍事衝突へのエスカレーションリスクが上昇（
<!-- OLD:END -->
<!-- NEW:START -->
🅐 外交解決 <span style="color:#4ade80;">↑↑</span> — 60日MOU草案で米・イラン交渉担当者が暫定合意——ホルムズ機雷除去30日・無制限通航・核交渉開始の枠組み確立。トランプとモジュタバ・ハメネイの最終署名が唯一の関門（5/29 09:42 JST）<br>
  🅑 部分封鎖 <span style="color:#4ade80;">↓</span> — MOU草案合意でシナリオAへの移行確率が上昇。ただしトランプ「まだ満足していない」・イラン未確認・核条項が最大の地雷として残存<br>
  🅒 完全封鎖 <span style="color:#4ade80;">↓</span> — MOU枠組みが前進し全面封鎖リスクは後退。ただしIRGCのクウェートミサイル・「Arash-e Kamangir」投入で軍事行動継続——合意崩壊→機雷再敷設シナリオの火種残存<br>
  🅓 軍事拡大 <span style="color:#4ade80;">↓</span> — MOU草案合意でエスカレーション直接リスクは後退。ただしIRGCのクウェート弾道ミサイル攻撃・新型防空システム戦闘使用は軍事衝突の火種——合意崩壊時に急浮上する（
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（タイトル・本文）

### シナリオA タイトル

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-title" id="sc-tag-A">🅐 シナリオA：外交解決——MOU署名・段階的ホルムズ再開
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-title" id="sc-tag-A">🅐 シナリオA：外交解決——60日MOU草案合意・トランプ署名で歴史的突破口
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオA 本文

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-body"><p>停戦から3ヶ月が過ぎ、カタール・ドーハ会談でのMOU最終調整が続く。米・イランの交渉担当者は「大枠で合意」しているが、IRGCのSNSC批准と最高指導者モジュタバ・ハメネイの最終決裁が最後の関門。「単語1つの対立」が解消されれば、60日間の停戦延長・段階的ホルムズ再開・核交渉開始が実現する。トランプが「急がない——時間は味方」に転じたことが交渉長期化リスク。WTI見通し：署名確定なら$75〜80急落・日本の精製コスト改善。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-body"><p>米・イランの交渉担当者が60日間のMOU草案で暫定合意（Axios独占スクープ→各紙確認）——ホルムズ機雷除去（30日以内）・「無制限」通航回復・核交渉・制裁緩和協議を包括。トランプとモジュタバ・ハメネイの最終署名が唯一の関門。トランプは「まだ満足していない」と保留中——ベッセント財務長官「ウラン引渡し・海峡無制限開放が前提」と条件を強調。ルビオとパキスタン外相ダールが5/29ワシントンで会談し推進図る。WTI見通し：署名確定なら$75〜80急落（合意期待を上回る下落）・日本の供給は30〜60日以内の正常化へ。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB タイトル

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-title" id="sc-tag-B">🅑 シナリオB：部分封鎖継続——PGSA管制通航・交渉膠着
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-title" id="sc-tag-B">🅑 シナリオB：MOU崩壊・部分封鎖継続——PGSA管制通航の既成事実化
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB 本文

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-body"><p>カタール協議でMOU「大枠合意」が続く中、IRGCの「管制通航」制度（PGSA）が既成事実化しつつある。トランプが「急がない」に転じたことで交渉が長期化し、管制通航が「常態」になるリスク。イランが実質的な海峡コントロールを維持しながら、停戦と封鎖を並立させる「新常態」への移行シナリオ。日本は喜望峰回り・代替ルートを継続するが長期化により備蓄圧迫が深刻化。WTI：$95〜100/bbl。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-body"><p>60日MOU草案は合意担当者レベルで成立したが、トランプが署名を拒否するか条件を再追加してMOUが破談するシナリオ。IRGCの「管制通航」制度（PGSA）が既成事実化し、イランが実質的な海峡コントロールを維持しながら停戦と部分封鎖を並立させる「新常態」への移行。クウェートへの弾道ミサイル発射・「Arash-e Kamangir」投入でIRGCが軍事的優位を誇示——管制継続の既成事実化を後押し。日本は喜望峰回り・代替ルートを継続するが長期化により精製コスト高止まり。WTI：$95〜100/bbl。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC タイトル

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-title" id="sc-tag-C">🅒 シナリオC：完全封鎖——合意崩壊・機雷再敷設・全面封鎖
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-title" id="sc-tag-C">🅒 シナリオC：MOU完全崩壊——機雷再敷設・「Arash-e Kamangir」防衛体制・全面封鎖
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC 本文

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-body"><p>MOU交渉が完全に崩壊し、イラン強硬派（IRGC主導）が主導権を取り戻すシナリオ。核棚上げ拒否・制裁解除要求を巡りトランプが最終的に拒絶、イランが「交渉拒絶」を宣言し封鎖強化へ転換。IRGCが追加機雷を敷設し通航量が戦前比ゼロに近づく。EUの制裁追加・日本の代替調達が限界に達する。WTI：$110〜125/bbl超（エネルギー危機第2波）。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-body"><p>60日MOU草案が最終的に崩壊し、イラン強硬派（IRGC主導）が完全に主導権を取り戻すシナリオ。トランプが核条件（ウラン引渡し・核放棄）で折り合わず署名拒否→イランが「交渉拒絶・防衛強化」を宣言。イランが国産新型防空システム「Arash-e Kamangir」（MQ-9 Reaper撃墜実績）でホルムズ上空を制圧し、追加機雷敷設で通航ゼロに接近。EUの制裁追加・日本の代替調達が限界に達する。WTI：$115〜130/bbl（エネルギー危機第2波）。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD タイトル

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-title" id="sc-tag-D">🅓 シナリオD：軍事エスカレーション——停戦崩壊・全面軍事衝突
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-title" id="sc-tag-D">🅓 シナリオD：軍事エスカレーション——IRGCクウェート弾道ミサイル→連鎖拡大・全面衝突
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD 本文

<!-- APPLY:START -->
<!-- OLD:START -->
<div class="sc-body"><p>IRGCによるMQ-9 Reaper撃墜・F-35・RQ-4への発砲、そして「停戦違反への報復権を保有」宣言が示す通り、軍事エスカレーションの火種が残存する。MOU交渉が最終的に崩壊し、IRGCが核施設防衛を名目に弾道ミサイルを多数発射するシナリオ。米軍が大規模報復作戦に移行、イスラエルが再参戦。クウェート・バーレーン・UAE等湾岸同盟国への攻撃が拡大し地域戦争に発展。WTI：$130超（2022年水準突破）・世界的スタグフレーション。</p></div>
<!-- OLD:END -->
<!-- NEW:START -->
<div class="sc-body"><p>IRGCがクウェートへの弾道ミサイル発射・米空軍基地攻撃・「Arash-e Kamangir」による米無人機撃墜を実施——停戦の枠内でありながら同盟国へのミサイル攻撃がエスカレーションの引き金となる。60日MOU草案が崩壊し米軍が大規模報復作戦に移行、IRGCが弾道ミサイルを多数発射するシナリオ。イスラエルの再参戦・湾岸同盟国（クウェート・バーレーン・UAE等）への攻撃拡大で地域戦争に発展。核施設への直接攻撃が視野に入る。WTI：$140超（史上最高水準更新）・世界的スタグフレーション。</p></div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター（次の焦点5点）

<!-- APPLY:START -->
<!-- OLD:START -->
①MOU署名可否 ／ IRGC・SNSC批准 ／ 核棚上げ60日合意 ／ ブレント$70急落 vs $120急騰——「署名か崩壊か」の二択
<!-- OLD:END -->
<!-- NEW:START -->
①トランプのMOU最終署名——「数日以内」か「条件再交渉」か——イスハク・ダール（パキスタン外相）との本日会談が鍵
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
②IRGC・SNSCの批准——IRGCがMOU「停戦違反への報復権を保有」と宣言したまま署名できるか
<!-- OLD:END -->
<!-- NEW:START -->
②イランSNSC・モジュタバ・ハメネイの批准——「Arash-e Kamangir」誇示でIRGC内強硬派の影響力が署名を阻むリスク
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
③ホルムズ機雷除去の技術的実施——30日以内という期限の現実性
<!-- OLD:END -->
<!-- NEW:START -->
③ホルムズ機雷除去の実施体制——MOU草案「30日以内」の技術的現実性・IRGC協力の条件と米軍監視体制
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
④核交渉の枠組み——ウラン引渡し先（国外移転 vs 国内保管）・完全廃棄要求とイランの抵抗
<!-- OLD:END -->
<!-- NEW:START -->
④核交渉の枠組み——ウラン引渡し先をめぐりトランプ「ロシア・中国への移転反対」と新条件追加。完全廃棄 vs 制限的保有でイランと根本対立
<!-- NEW:END -->
<!-- APPLY:END -->

<!-- APPLY:START -->
<!-- OLD:START -->
⑤月曜市場の反応——合意確定なら週明けWTI $10〜20急落・不成立なら$100回帰。市場が「早期合意」を先取りして動く可能性
<!-- OLD:END -->
<!-- NEW:START -->
⑤原油市場の反応——MOU署名確定なら機雷除去完了前でもWTI $15〜20急落へ。IRGC軍事行動（クウェートミサイル・Reaper撃墜）が合意リスクプレミアムを下支え。「署名なし」と判明した場合の急反発シナリオも注視
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオフッターの分析日付

<!-- APPLY:START -->
<!-- OLD:START -->
2026年5月28日 10:59 JST 情勢分析
<!-- OLD:END -->
<!-- NEW:START -->
2026年5月29日 09:42 JST 情勢分析
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

<!-- APPLY:START -->
<!-- OLD:START -->
2026年5月28日 10:59 JST 再確認済
<!-- OLD:END -->
<!-- NEW:START -->
2026年5月29日 09:42 JST 再確認済
<!-- NEW:END -->
<!-- APPLY:END -->

> ルート状況に新たな変化なし。60日MOU草案合意にホルムズ機雷除去30日条項が含まれるが、署名確定・IRGC協力まで物理的状況は現状維持。通航量95%減・喜望峰回り継続。

---

## [S09] 30秒カラム — Claude Code 適用内容

> ⚠️ **APPLY ブロックを使わず Claude Code が直接対応すること。**
> 1. `view docs/index.html` の `<!-- 30秒で全体像を把握 -->` セクションを view_range で確認
> 2. 現在のテキストを把握してから str_replace を実施
> 3. 「いま何が」「海峡の今」「次の焦点」3行と バッジ5枚を全て更新

### 【いま何が起きているか】（5/29 09:42 JST）

```
🚨【60日MOU草案で暫定合意】米・イランの交渉担当者が60日間の停戦延長MOU草案に合意——ホルムズ機雷除去（30日以内）・「無制限」通航・核交渉開始の枠組み確立（Axios 5/28 GMT）。しかしトランプは「まだ満足していない」と署名保留、イランも公式確認なし。IRGCはクウェートへ弾道ミサイル・米基地攻撃・新型防空システム「Arash-e Kamangir」でReaper撃墜と軍事示威を継続。停戦91日目——歴史的突破口か最終崩壊かの正念場。
```

### 【海峡の今】

```
通航量：戦前比約95%減継続（MOU草案：機雷除去30日以内・無制限通航回復の条項あり）
WTI：$91前後／ブレント：$97前後（合意期待で週次大幅↓・IRGC攻撃で反発）
IRGC：クウェートへ弾道ミサイル発射・「Arash-e Kamangir」でReaper撃墜（5/28 JST）
```

### 【次の焦点】

```
トランプMOU最終署名 ／ イランSNSC・モジュタバ・ハメネイ批准 ／ ホルムズ機雷除去30日の実施体制 ／ 核交渉枠組み（ウラン引渡し先・ロシア中国移転拒否） ／ ルビオ・ダール（パキスタン外相）本日会談の結果
```

### バッジ5枚（全て更新）

```
🔴 外交：60日MOU草案合意・トランプ署名待ち
🔴 海峡：通航95%減・封鎖91日目
📉 原油：WTI $91（合意期待で週次大幅↓）
⚠️ 核問題：ウラン引渡し・核放棄が署名条件——最大の壁
🇯🇵 日本：備蓄維持・MOU署名→30〜60日以内の供給正常化へ
```

---

## [S01] ヘッダー日時・警戒レベル

<!-- APPLY:START -->
<!-- OLD:START -->
<span class="badge-item badge-date">📅2026年5月28日 10:59 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span class="badge-item badge-date">📅2026年5月29日 09:42 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

> 警戒レベルは **🚨 最高** を維持（MOU未署名・IRGC軍事行動継続・核条件未解決のため）

---

## [S11] 更新ログ追記

### JSON-LD dateModified の更新（必須）

<!-- APPLY:START -->
<!-- OLD:START -->
"dateModified": "2026-05-28T00:00:00+09:00",
<!-- OLD:END -->
<!-- NEW:START -->
"dateModified": "2026-05-29T00:00:00+09:00",
<!-- NEW:END -->
<!-- APPLY:END -->

### 更新ログ先頭への追記

<!-- APPLY:START -->
<!-- OLD:START -->
<div>📅 <strong>2026年5月28日 10:59 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div>📅 <strong>2026年5月29日 09:42 JST</strong> 更新</div>
        <div><span style="color:#4ade80;">2026/05/29 09:42</span> — <strong style="color:#86efac;">【超重大更新（91日目）】</strong>米・イランが60日MOU草案で暫定合意（トランプ最終署名待ち・イラン未確認）——ホルムズ機雷除去30日・無制限通航・核交渉開始の枠組み確立（Axios独占）。IRGCがクウェートへ弾道ミサイル発射（迎撃済）・米空軍基地攻撃——CENTCOM「重大な停戦違反」。イランが「Arash-e Kamangir」新型防空システムでMQ-9 Reaper撃墜（初の戦闘使用）。EUが対イラン制裁拡大。WTI $91・ブレント $97（5/29 JST）。ルビオ・パキスタン外相ダール本日ワシントン会談。ニュース2件更新・OSINT更新。出典：Axios・Washington Times・CNBC・CNN・Al Jazeera・CBS News。</div>
        <div>📅 <strong>2026年5月28日 10:59 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

> `<!--出典・更新ログ-->` セクションに表示する更新ログが11件を超えた場合は最古の1件を削除してください。

---

## ✅ 出力前セルフチェック

```
[x] S01 ヘッダー ― 2026年5月29日 09:42 JST ✓
[x] S02 TICKER ― 60日MOU暫定合意・IRGC→クウェートミサイル・Arash-e Kamangir・ルビオ・ダール・EU制裁・封鎖91日目 ✓
[x] S03 速報インシデント ― 5/29 09:42付け・2件新規追加（60日MOU合意・IRGC→クウェートミサイル）✓
[x] S04 情勢カード3枚 ― 3枚とも日付・数値・出典が5/29版に更新 ✓
[x] S05 COUNTDOWN ― 「60日MOU草案暫定合意フェーズ」・91日目 ✓
[x] S06 シナリオ確率補足バナー ― 5/29 09:42日付・根拠文更新（A↑↑・B↓・C↓・D↓）✓
[x] S07 シナリオ4本 ― タイトル・本文が60日MOU暫定合意情勢を反映 ✓
[x] S07 シナリオC・D ― 内容近似なし（C：Arash-e Kamangir防衛・機雷再敷設 / D：クウェートミサイル→連鎖拡大）✓
[x] S07 シナリオC・D ― WTI価格レンジ差別化済み（C: $115〜130、D: $140超）✓
[x] S08 シナリオフッター ― 次の焦点5点を5/29版に更新（①トランプ署名②イラン批准③機雷除去④核枠組み⑤市場反応）✓
[x] S08.5 全ルート現況サマリー ― 2026年5月29日 09:42 JST 再確認済 ✓
[x] S09 30秒カラム ― 3行+バッジ5枚の新しい内容を記載（Claude Code view_range後に適用）✓
[x] S10 news_data.jsonメモ ― アーカイブ注意事項記載 ✓
[x] S10 osint ― Al Jazeera 5/28ライブブログを検索・URL確認済み ✓
[x] S10 osint ― 配列ごと置き換えになっていないか → 先頭追加・既存isLatest:false変更形式で記載 ✓
[x] S11 更新ログ ― 先頭に5/29 09:42行追記 ✓
[x] S11 JSON-LD ― "dateModified": "2026-05-29T00:00:00+09:00" に更新 ✓
[x] 全体 ― 日付表記「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一 ✓
[x] 全体 ― URLはweb検索確認済みのみ使用（Axios・WashingtonTimes・Al Jazeera）✓
[x] 全体 ― 📰関連最新ニュースにAl Jazeera混入なし（osintのみ）✓
[x] 全体 ― 人名日本語表記：トランプ・ルビオ・モジュタバ・ハメネイ・イスハク・ダール ✓
[x] S07 シナリオC・D ― WTI B($95-100) < C($115-130) < D($140超) 差別化確認 ✓
[x] S10 latest ― 各記事のtitle/bodyとurlが同一記事を指しているか確認 ✓
```

---

## 📣 X投稿案（2ポスト構成）

### 【第1投稿】本文（約130字・URL なし）

```
🚨【速報・ホルムズ91日目】米・イラン交渉担当者が60日MOU草案で暫定合意——ホルムズ機雷除去30日・無制限通航・核交渉開始の枠組み確立（Axios独占）。しかしトランプは「まだ満足していない」と署名保留。IRGCはクウェートへ弾道ミサイル・新型防空で米Reaper撃墜と強硬姿勢継続。WTI $91。

#ホルムズ海峡 #イラン #原油価格
```

### 【第2投稿】リンク＋補足

```
詳細・全情勢マップはこちら↓
https://yattanda.github.io/hormuz-map/

60日MOU：機雷除去30日以内・無制限通航・核交渉開始——署名確定ならWTI $15〜20急落の可能性。ルビオ・パキスタン外相本日会談が最後の鍵。

@hormuz_map_jp
```
