# index_html_diffs.md — 2026年5月11日 18:22 JST 更新分（部分更新）

> Claude Code への指示：以下の差分を index.html に適用してください。
> **今回の更新範囲：S01（ヘッダー）・S02（TICKER）・S03（速報インシデント）・S09（30秒カラム）・S11（更新ログ）のみ。**
> S04〜S08（情勢カード・COUNTDOWN・シナリオ等）は今回更新しない。
> 変更箇所以外は絶対に触らないこと。

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-date`

**変更前：**
```html
<span class="badge-item badge-date">📅2026年5月9日 16:14 JST</span>
```

**変更後：**
```html
<span class="badge-item badge-date">📅2026年5月11日 18:22 JST</span>
```

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー（2026年5月9日 16:14 JST） -->` コメント直後の `<span class="ticker-text">` 内テキスト全体

**変更前（コメント行含む）：**
```
<!-- 新ティッカー（2026年5月9日 16:14 JST） -->
```

**変更後（コメント行のみ置き換え）：**
```
<!-- 新ティッカー（2026年5月11日 18:22 JST） -->
```

**続けてティッカー本文を置き換え：**

**現在のティッカーテキスト（`<span class="ticker-text">` 内）old_str：**

> ⚠️ Claude Code 作業注意：`view_range` で現在の ticker-text を確認してから以下の new_str に str_replace すること。

```
🚨【イランがUAEを攻撃】ミサイル2発・ドローン3機——UAE防空が全弾迎撃（5/9 JST）｜⚔️ 5/8 米・イランがホルムズで軍事衝突——3駆逐艦攻撃・米が報復空爆（5/8 JST）｜MOU回答待機中——停戦辛うじて継続（5/9 JST）｜🛢️ ブレント$101.29・週間▲6%超（5/9 JST）｜⚠️ 停戦綱渡り継続——封鎖72日目
```

**変更後：**
```
🚨【交渉決裂】イランが「ホルムズ主権認定・戦争賠償」要求の対案提出——トランプ「TOTALLY UNACCEPTABLE」と即座に拒否（5/11 JST）｜🇮🇷 イランの対案に核問題の記載なし——意図的除外か（5/11 JST）｜🛢️ ブレント原油$104.50（+3.2%）——交渉決裂懸念で急上昇（5/10 JST）｜✈️ UAE・クウェート・カタール沖でドローン攻撃が同日多発（5/10 JST）｜🚢 開戦以来初のカタールLNGタンカーがホルムズを通過——信頼醸成・象徴的のみ（5/11 JST）｜⚠️ 停戦は名目上継続——封鎖74日目
```

---

## [S03] 速報インシデント ⚠️（漏れ多発セクション）

**対象：** `<!-- 速報インシデント トグルボタン -->` 内

### トグルボタン内の日付バッジ

**変更前：**
```html
📅 5/9 16:14 更新
```

**変更後：**
```html
📅 5/11 18:22 更新
```

---

### 速報インシデント本体（先頭の `<strong>` タグを置き換え）

**変更前（先頭の strong タグ）：**
```html
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【5/9 16:14 速報】イランがUAEにミサイル2発・ドローン3機発射——全弾迎撃｜5/8 米・イランがホルムズ内で軍事衝突（3米駆逐艦攻撃→報復空爆）｜MOU回答なし・停戦は辛うじて継続｜ブレント$101.29・週間-6%超
</strong>
```

**変更後：**
```html
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【5/11 18:22 速報】イランが「ホルムズ主権認定・戦争賠償・制裁解除」要求の対案提出→トランプ「TOTALLY UNACCEPTABLE」即座に拒否（5/10-11）｜UAE・クウェート・カタール沖でドローン攻撃が同日多発（5/10）｜カタールLNGタンカー、開戦以来初のホルムズ通過（信頼醸成・象徴的）｜ブレント$104.50急騰・交渉行き詰まり・封鎖74日目
</strong>
```

---

### インシデントリスト（先頭に2件追加）

**既存リストの先頭（`<ul id="incident-list">` の直後）に以下の2件を追記：**

```html
<li style="background:rgba(239,68,68,0.15);border-left:3px solid #ef4444;padding:10px 12px;border-radius:6px;">
  <strong style="color:#fca5a5;">🔴【交渉決裂 5/11 18:22 JST】イランが「ホルムズ主権認定・戦争賠償・制裁解除・核問題除外」の対案を米に提出——トランプ「TOTALLY UNACCEPTABLE」と即座に拒否</strong><br>
  イランはパキスタン経由で対案を米国に送付。内容は①ホルムズへの主権認定②戦争賠償③凍結資産解放④制裁解除⑤全戦線停戦⑥米海軍封鎖終了を要求。核問題は対案に一切記載なし（意図的に除外）。トランプはTruth Socialで「TOTALLY UNACCEPTABLE」と投稿。ウォルツ米国連大使「米国はレッドラインを明確に示した」。停戦延長後の最大の交渉決裂。
  <span style="font-size:0.75rem;color:#64748b;display:block;margin-top:6px;">📡 CNBC（5/11 JST）</span>
</li>

<li style="background:rgba(251,191,36,0.08);border-left:3px solid #f59e0b;padding:10px 12px;border-radius:6px;">
  <strong style="color:#fcd34d;">✈️【多発ドローン攻撃 5/10 JST】UAE・クウェート・カタール沖で同日多発——停戦が再度テスト</strong><br>
  5/10（現地時間）、UAE：イランからの弾道ミサイル2発とドローンへの対処で3人負傷（一部迎撃不確認）。クウェート：敵対ドローンが領空侵入し防空が対処。カタール沖：カーゴ船にドローンが着弾し小火災、死傷者なし。IRGCは「米軍基地への報復攻撃」を再度警告。トランプ政権は「停戦維持中」と主張するも実態は停戦崩壊寸前。パキスタン首相はカタール首脳と平和努力継続を確認。
  <span style="font-size:0.75rem;color:#64748b;display:block;margin-top:6px;">📡 Fortune・CNN（5/10 JST）</span>
</li>
```

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ5枚）

> ⚠️ Claude Code 作業注意：`view_range` で `<!-- 30秒で全体像を把握 -->` セクションの現在の内容を確認してから str_replace すること。

### ステータスバッジ5枚（全置き換え）

**変更前（バッジ5枚 — 現在の内容）：**
```html
<span style="background:rgba(239,68,68,0.06);border:1px dashed rgba(239,68,68,0.4);color:#f87171;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">🔒 封鎖72日目</span>
          <span style="background:rgba(251,191,36,0.06);border:1px dashed rgba(251,191,36,0.4);color:#fbbf24;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">🛢️ ブレント $101.29/bbl</span>
          <span style="background:rgba(251,191,36,0.06);border:1px dashed rgba(251,191,36,0.4);color:#fbbf24;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">🚢 通航 約5%</span>
          <span style="background:rgba(56,189,248,0.06);border:1px dashed rgba(56,189,248,0.4);color:#38bdf8;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">📜 MOU回答 待機中</span>
          <span style="background:rgba(16,185,129,0.06);border:1px dashed rgba(16,185,129,0.4);color:#6ee7b7;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">⚠️ 停戦 綱渡り継続</span>
```

**変更後：**
```html
<span style="background:rgba(239,68,68,0.06);border:1px dashed rgba(239,68,68,0.4);color:#f87171;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">🔒 封鎖74日目：停戦継続中</span>
          <span style="background:rgba(239,68,68,0.06);border:1px dashed rgba(239,68,68,0.4);color:#f87171;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">🛢️ ブレント $104.50/bbl（+3.2%）</span>
          <span style="background:rgba(251,191,36,0.06);border:1px dashed rgba(251,191,36,0.4);color:#fbbf24;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">🚢 通航 約5%</span>
          <span style="background:rgba(239,68,68,0.06);border:1px dashed rgba(239,68,68,0.4);color:#f87171;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">🔴 対案：トランプ即座に拒否</span>
          <span style="background:rgba(251,191,36,0.06);border:1px dashed rgba(251,191,36,0.4);color:#fbbf24;font-size:0.78rem;font-weight:600;padding:4px 12px;border-radius:6px;cursor:default;">⚠️ 停戦 綱渡り継続</span>
```

---

### 3行サマリー（「いま何が」「海峡の今」「次の焦点」）

> ⚠️ Claude Code：view で現在の 3行サマリーテキストを確認後、以下の内容に str_replace すること。  
> 対象：`<!-- 30秒で全体像を把握 -->` セクション内の「いま何が起きているか」「海峡の今」「次の焦点」の各ブロック。

**「いま何が起きているか」ブロック本文 — 変更後：**
```
【いま何が起きているか（5/11 18:22 JST）】
イランが「ホルムズ主権認定・戦争賠償・核問題除外」の対案を米国に提出。トランプは即座に「TOTALLY UNACCEPTABLE」と拒否し交渉は再び完全決裂。
UAE・クウェート・カタール沖で5/10にドローン攻撃が同日多発——停戦は名目上継続も実態は崩壊寸前。
開戦以来初のカタールLNGタンカーがホルムズを通過（信頼醸成・象徴的）するも、交渉決裂でブレント$104.50急騰——封鎖74日目。
```

**「海峡の今」ブロック本文 — 変更後：**
```
【海峡の今】
通航量：戦前比約95%減（月3,000隻→150隻前後）
ブレント原油：$104.50/bbl（+3.2%・交渉決裂で急騰）
交渉状況：イランの対案をトランプが「TOTALLY UNACCEPTABLE」と拒否——次の動き未定
```

**「次の焦点」ブロック本文 — 変更後：**
```
【次の焦点】
トランプの次の外交・軍事オプション ／ イランの対案撤回または修正交渉 ／ ブレント$110超えによる市場パニックの閾値
```

---

## [S10] news_data.json 更新メモ

**今回の更新方針：**
- `docs/data/news_data.json` を `str_replace` で更新すること（`run.bat` / `auto_push.py` 経由での全ファイル置き換えは不要）
- `archive` セクションは触らずそのまま維持すること（別ファイル `news_data.json` が提供されているが archive は部分的なため `str_replace` 方式を推奨）

**① `"updated"` フィールドの更新**

```
old_str: "updated": "2026年5月10日 更新（ルート情報特集）"
new_str: "updated": "2026年5月11日 18:22 日本時間JST"
```

**② `"staleNotice"` は `""` のまま変更なし**

**③ `"latest"` 配列を以下の4件に全置き換え**

old_str: `"latest": [` から始まり `],` で終わる配列全体（先頭から `"osint"` の手前まで）  
new_str:

```json
"latest": [
    {
      "id": "news-2026-05-11-iran-counter-proposal-rejected",
      "date": "2026/05/11",
      "label": "🔴 交渉",
      "url": "https://www.cnbc.com/2026/05/11/iran-war-trump-negotiation-hormuz-nuclear-talks.html",
      "title": "イランが「ホルムズ主権認定・戦争賠償・制裁解除」要求の対案提出——トランプ「TOTALLY UNACCEPTABLE」と即座に拒否",
      "body": "イランはパキスタン経由で対案を米国に送付。要求内容：①ホルムズへの主権認定②戦争賠償③凍結資産解放④制裁解除⑤全戦線停戦⑥米封鎖終了。核問題は対案に一切記載なし（意図的に除外）。トランプはTruth Socialで「I have just read the response from Iran's so-called 'Representatives.' I don't like it — TOTALLY UNACCEPTABLE!」と投稿。Saxo Bankは「再エスカレーション方向への傾き」と分析。ウォルツ米国連大使「米国はレッドラインを明確に示した」。ブレント$104.50（+3.2%）急騰。",
      "sourceLabel": "CNBC（2026/05/11）"
    },
    {
      "id": "news-2026-05-10-drone-attacks-gcc",
      "date": "2026/05/10",
      "label": "⚔️ 軍事",
      "url": "https://fortune.com/2026/05/10/iran-war-ceasefire-drone-cargo-ship-qatar-kuwait-uae-attacks/",
      "title": "UAE・クウェート・カタール沖でドローン攻撃が同日多発——停戦が再度テスト（5/10）",
      "body": "5/10（現地時間）、停戦が再度試される攻撃が同日多発した。UAE：イランからの弾道ミサイル2発とドローンへの対処で3人負傷。クウェート：敵対ドローンが領空侵入し防空が対処。カタール沖：カーゴ船にドローンが着弾し小火災発生、死傷者なし。IRGCは「米軍基地への報復攻撃」を再度警告。トランプ政権は「停戦維持中」と主張するも実態は綱渡り。パキスタン首相はカタール首脳と平和努力の継続を確認。",
      "sourceLabel": "Fortune（2026/05/10）"
    },
    {
      "id": "news-2026-05-11-qatar-lng-hormuz-passage",
      "date": "2026/05/11",
      "label": "🚢 通航",
      "url": "https://www.cnbc.com/2026/05/11/iran-war-trump-negotiation-hormuz-nuclear-talks.html",
      "title": "開戦以来初・カタールLNGタンカーがホルムズを通過——イランがカタール・パキスタンへの信頼醸成として承認",
      "body": "開戦以来初めてカタール産LNGを積んだタンカーがホルムズ海峡を通過した。イランがカタール・パキスタンとの関係維持のため通過を特例承認したとされる。ただし同日にカタール沖でカーゴ船へのドローン攻撃が発生しており、象徴的な通過が実質的な開通にはほど遠い現実が浮き彫りに。「この通過は市場の懸念解消には至らなかった」（OCBC銀行）。",
      "sourceLabel": "CNBC（2026/05/11）"
    },
    {
      "id": "news-2026-05-08-us-iran-military-clash-update",
      "date": "2026/05/08",
      "label": "⚔️ 軍事",
      "url": "https://www.npr.org/2026/05/08/g-s1-121061/iran-war-updates",
      "title": "米がイラン産油タンカー2隻を攻撃——UAE「3人負傷」・CMA CGM被弾・Kharg島沖油流出（5/8更新）",
      "body": "米軍は米海軍封鎖突破を試みるイラン産油タンカー2隻を攻撃し無力化した。UAE国防省はイラン発射の弾道ミサイル・ドローンで3人が負傷したと発表（一部迎撃不確認）。アラグチー外相は「外交テーブルにある度に米国は無謀な軍事行動を選ぶ」とXに投稿。カタール沖ではCMA CGMサンアントニオが巡航ミサイルに被弾し乗組員8名が負傷（5/5）。Kharg島沖の油流出が欧州宇宙機関の衛星画像で確認され拡大中。",
      "sourceLabel": "NPR（2026/05/08）"
    }
  ],
```

**④ `"osint"` 配列を以下の1件に置き換え（既存全件を新1件に差し替え）**

```json
"osint": [
    {
      "country": "🇮🇷",
      "media": "Al Jazeera",
      "date": "2026/05/06",
      "url": "https://www.aljazeera.com/news/2026/5/6/french-container-ship-struck-in-latest-escalation-at-strait-of-hormuz",
      "titleJa": "IRGC「新手順でホルムズ通航を保証する」——米作戦一時停止後に声明・CMA CGMサンアントニオが最新被弾事例",
      "titleEn": "Iran's IRGC says Hormuz safe transit will be 'ensured' under new procedures as US pauses operation",
      "cardBg": "rgba(30,10,10,0.7)",
      "cardBorder": "rgba(239,68,68,0.2)",
      "badgeColor": "rgba(239,68,68,0.15)",
      "borderColor": "rgba(239,68,68,0.3)",
      "textColor": "#f87171",
      "isLatest": true
    }
  ],
```

**⑤ `"archive"` 先頭に以下のバッチを追加**（既存バッチの上に挿入）

```json
    {
      "batchLabel": "2026/05/10 ルート情報特集（アーカイブ）",
      "items": [
        {
          "id": "news-2026-05-08-fujairah-limited-recovery",
          "date": "2026/05/08",
          "label": "🔴 ルートA",
          "url": "https://energynow.com/2026/03/port-of-fujairah-resumes-oil-loadings-after-attack-and-why-it-matters-globally/",
          "title": "フジャイラ港・一部復旧も実態は不透明——衛星画像でタンカー2隻・VLCC1隻のみ確認（通常比58%激減継続）",
          "body": "5/4のVTTIターミナルへのドローン攻撃後、衛星画像（5/7）では港内タンカー2隻・VLCC1隻のみ。UAE産原油輸出は日量135万バレルに落ち込み（通常比58%減）。100隻超が錨泊滞留中。",
          "sourceLabel": "EnergyNow・Windward（5/4〜5/8）"
        },
        {
          "id": "news-2026-05-08-yanbu-surge-330pct",
          "date": "2026/05/08",
          "label": "🟢 ルートB",
          "url": "https://oilprice.com/Latest-Energy-News/World-News/East-West-Pipeline-Key-to-Saudi-Arabias-New-Oil-Export-Strategy.html",
          "title": "サウジ・ヤンブー輸出が戦前比330%増——VLCC27隻が向航中、ただしバベルマンデブ「二重チョークポイント」リスクが浮上",
          "body": "サウジアラビアはヤンブーへの振り向けを全開にし、輸出量が日量247万BPDと戦前比330%増に達した。Windwardは27隻のVLCCがヤンブーへ向航中と報告。ただしアジア向けはバベルマンデブ海峡を通過必須で「ホルムズを避けたが別のチョークポイントに依存する」構造が鮮明に。",
          "sourceLabel": "OilPrice・Windward・HornReview（5/8）"
        },
        {
          "id": "news-2026-05-06-nigeria-dangote-full-capacity",
          "date": "2026/05/06",
          "label": "🌍 西アフリカ",
          "url": "https://oilprice.com/Latest-Energy-News/World-News/Dangote-Refinery-Crude-Supply-Doubles-But-High-Import-Costs-Squeeze-Margins.html",
          "title": "ダンゴテ製油所がフル稼働（65万BPD）・欧州向け輸出開始——日本もナイジェリア・アンゴラからの輸入を本格拡大",
          "body": "アフリカ最大のダンゴテ製油所が日量65万BPDのフル稼働を達成。日本はホルムズ危機を受けナイジェリア・アンゴラ・ブラジルからの原油輸入を急拡大中。西アフリカ産はホルムズ・バベルマンデブ・スエズの3大チョークポイントを完全回避できる。日本向けは喜望峰経由で約35〜40日。",
          "sourceLabel": "OilPrice・Pravda Nigeria・African Energy Week（4/8〜5/6）"
        },
        {
          "id": "news-2026-05-04-hormuz-alternative-routes-overview",
          "date": "2026/04/23",
          "label": "分析",
          "url": "https://www.cnbc.com/2026/04/23/strait-hormuz-closure-alternative-routes-middle-east-oil-gas-pipelines.html",
          "title": "ホルムズ代替ルートの現実——IEA「既存の全バイパスを合わせても封鎖分の半分しか補えない」",
          "body": "CNBCが代替ルートを総括。既存の全パイプライン・迂回ルートの合計容量は最大約900〜1,000万BPD（ホルムズ通常流量2,000万BPDの半分以下）。メキシコ産は2026年7月に日本向け初便（100万バレル）が予定されている。",
          "sourceLabel": "CNBC・IEA・RSIS（4/23〜5/1）"
        }
      ]
    },
```

---

## [S11] 更新ログ追記

**対象：** `<!--出典・更新ログ-->` セクション内の更新グリッド先頭

**直近更新行（view で確認して先頭に以下を追加）：**

```html
<div>📅 <strong>2026年5月11日 18:22 JST</strong> 更新</div>
<div><span style="color:#f87171;">2026/05/11 18:22</span> — <strong style="color:#fca5a5;">【速報更新】</strong>イランが「ホルムズ主権認定・戦争賠償・制裁解除・核除外」の対案提出→トランプ「TOTALLY UNACCEPTABLE」即座に拒否・UAE・クウェート・カタール沖でドローン攻撃多発（5/10）・カタールLNGタンカー初通過（象徴的）・ブレント$104.50急騰・封鎖74日目・ニュース4件更新・OSINT更新</div>
```

---

## ✅ 出力前セルフチェック（部分更新版）

```
[x] S01 ヘッダー ― 2026年5月11日 18:22 JST ✓
[x] S02 TICKER ― イラン対案拒否・ドローン多発・カタールLNG・$104.50・封鎖74日目 ✓
[x] S03 速報インシデント ― 5/11 18:22付け・2件新規追加 ✓
[ ] S04〜S08 ― 今回は更新しない（省略）
[x] S09 30秒カラム ― バッジ5枚更新・3行サマリー更新（最後に作成）✓
[x] S10 news_data.json ― str_replace 5項目の指示を記載 ✓
[x] S11 更新ログ ― 先頭に5/11 18:22行追記 ✓

TICKER内JST表記チェック：全日付にJST付き ✓
📰 関連最新ニュースのAl Jazeera混入チェック：Al Jazeeraはosintのみ ✓
AI推測URL混入チェック：全URLは検索結果から取得済み ✓
日付表記フォーマット統一チェック：YYYY年MM月DD日 HH:MM JST ✓
封鎖日数チェック：5/3=66日目 → 5/11=74日目（+8日）✓
```

---

## ⚠️ シナリオ変更について（ユーザーへの確認依頼）

今回の情報はシナリオ確率に顕著な影響を与えます。
次回の通常更新時（または今回の追加指示時）にシナリオ更新もご検討ください。

| シナリオ | 現在 | 要検討 | 変更理由 |
|---|---|---|---|
| A（外交解決） | ~15% | **↓ 5〜10%** | トランプ「TOTALLY UNACCEPTABLE」で短期合意が極めて困難に |
| B（現状維持） | ~35% | 35%前後維持 | 依然として最大確率だが不安定要素増大 |
| C（完全封鎖強化） | ~15% | 15〜20%↑ | 対案決裂後の強硬行動リスク上昇 |
| D（軍事エスカレーション） | ~20% | **↑ 25〜30%** | ドローン攻撃継続・停戦崩壊寸前・IRGC警告強化 |
