# index_patch.md — ルート情報更新・構造変更
# 生成日時: 2026-05-10
# 作業者: Claude Code
# 対象ファイル: docs/index.html
# 重要: 各str_replaceの前に必ずview_rangeで該当箇所を確認してから実施すること

---

## 事前確認

作業開始前に以下を実行してください：

```
view docs/index.html
```

行数を確認し、以下の各セクションの位置をview_rangeで把握してから作業に入ること。

---

## PATCH-01: ルートA現況テキスト更新（ルートテーブル内）

### 目的
5/4攻撃後の最新状況（58%激減・限定復旧）を反映

### 検索キーワード
`5/4 VTTIターミナル直撃・積み出し停止中` を含む `<td>` セル

### str_replace

**old_str（ルートA説明セル・現在の内容）:**
```
            ADCOPパイプライン→フジャイラ→ムンバイ沖積み替え→日本。<br>
            <strong style="color:#f87171;">🔴 5/4 VTTIターミナル直撃・積み出し停止中。</strong>
            イランのドローン1機がUAEの防空網を突破しVTTI施設（Vitol・IFM・ADNOC共同所有）を直撃、火災発生。
            UAEは弾道ミサイル3発・ドローン多数を迎撃したが終端施設への攻撃は防げず。
            イランは関与を否定。革命防衛隊海軍はフジャイラを「イラン管理域」に追加宣言。
            積み出し再開時期不明。ADCOPパイプラインとホルムズの「二択同時崩壊」が確定。<br>
            <small style="color:#64748b">出典：Bloomberg・Reuters・Al Jazeera・EurasianTimes（5/4〜5/5）</small>
```

**new_str:**
```
            ADCOPパイプライン→フジャイラ→ムンバイ沖積み替え→日本。<br>
            <strong style="color:#f87171;">🔴 5/4 VTTIターミナル直撃・限定復旧も実態は不透明。</strong>
            イランのドローン1機がUAEの防空網を突破しVTTI施設（Vitol・IFM・ADNOC共同所有）を直撃。
            同時にADNOCスーパータンカー「バラカ」もドローン2機で攻撃を受け複合打撃。
            UAE産原油輸出量は通常比<strong style="color:#f87171;">58%減（日量135万BPD）</strong>に急落、100隻超が錨泊滞留。
            一部バースは再開報告あるが、衛星画像では港内タンカー2隻・VLCC1隻のみ確認（5/7）。
            革命防衛隊海軍がフジャイラを「イラン管理域」に宣言、ADCOPとホルムズの「二択同時崩壊」が確定。<br>
            <small style="color:#64748b">出典：Bloomberg・Reuters・Windward・Kanoo Shipping・衛星画像分析（5/4〜5/8）</small>
```

---

## PATCH-02: ルートA ステータスpillの更新

### str_replace

**old_str:**
```
          <td><span class="pill pill-r">🔴 機能不全（5/4攻撃）</span></td>
```

**new_str:**
```
          <td><span class="pill pill-r">🔴 機能不全（58%激減・限定復旧）</span></td>
```

---

## PATCH-03: ルートB説明セル更新（SUMED迂回・330%増追記）

### 目的
東西PL経由輸出330%増・バベルマンデブ二重チョークポイント・SUMED迂回オプションを追記

### str_replace

**old_str（ルートB説明セル）:**
```
            東西PL→ヤンブー→バベルマンデブ→日本。
            <strong style="color:#4ade80">4/12 パイプライン全面復旧（700万BPD）✅</strong>（サウジエネルギー省公式・Reuters確認）。
            Manifa油田（▲30万BPD）も復旧済み✅。
            <strong style="color:#fbbf24">⚠️ Khurais油田（▲30万BPD）は5/8時点でも復旧作業継続中・未完了。</strong>
            サウジの実際の生産能力は30万BPD規模の低下が継続。太陽石油（愛媛）3/28到着済み。ルートA機能不全後の最重要代替ルート。<br>
            <small style="color:#64748b">出典：Reuters・Bloomberg・サウジエネルギー省（4/12）・The National（4/12）</small>
```

**new_str:**
```
            東西PL→ヤンブー→バベルマンデブ→日本。
            <strong style="color:#4ade80">4/12 パイプライン全面復旧（700万BPD）✅</strong>（サウジエネルギー省公式・Reuters確認）。
            <strong style="color:#4ade80">⬆ ヤンブー輸出量：戦前比330%増（日量247万BPD）・VLCC27隻がヤンブーへ向航中。</strong><br>
            Manifa油田（▲30万BPD）復旧済み✅。
            <strong style="color:#fbbf24">⚠️ Khurais油田（▲30万BPD）は5/8時点でも復旧作業継続中・未完了。</strong><br>
            ⚠️ <strong style="color:#fbbf24">二重チョークポイント問題：</strong>ヤンブー発アジア向けはバベルマンデブ海峡（フーシ派リスク）を通過必須。
            ただし日量200〜250万BPD分はエジプト・アイン・スフナ経由のSUMEDパイプラインでバベルマンデブを迂回可能（欧州向け限定）。
            太陽石油（愛媛）3/28到着済み ✅。ルートA崩壊後の最重要代替ルート。<br>
            <small style="color:#64748b">出典：Reuters・Bloomberg・Windward・OilPrice・サウジエネルギー省（4/12〜5/8）</small>
```

---

## PATCH-04: ルートテーブルの行順を並び替え（B→A→C→西アフリカ→D）

### 目的
日本への影響度（輸入シェア）順に並び替え

### 手順
1. まず `view docs/index.html` で各 `<tr class="ra">` `<tr class="rb">` の行番号を確認
2. テーブル内の行順を以下の通りに並び替える：
   - ルートB行（`<tr class="rb">`）を先頭へ
   - ルートA行（`<tr class="ra">`）を2番目へ  
   - ルートC🇺🇸行（`<tr class="rc">`）を3番目へ
   - 西アフリカ行（ナイジェリア・アンゴラ、`<tr class="rng">`等）を4番目へ
   - ルートD行を末尾へ

### str_replace（テーブルヘッダー直後の行）

**※重要: view_rangeで `<thead>` ～最初の `<tr class=` までを確認してから実施**

テーブルの `<tbody>` 開始直後を探し、`<tr class="ra">` で始まる場合は以下を適用：

**old_str（tbody開始の識別子 ― 正確な文字列はview後に確認）:**
```
        <tr class="ra">
```

**new_str（ルートBをBODY先頭に移動するため、実際の作業はCUT＆PASTEで対応）:**

※ 行の移動はstr_replaceの組み合わせで実施する。具体的には：
1. ルートBの `<tr class="rb">〜</tr>` ブロック全体をコピーし、ルートAの `<tr class="ra">` の直前に `str_replace` で挿入
2. 元のルートBブロックを空str_replaceで削除

実際の作業例：

**Step A - ルートB行を先頭に複製（ルートA行の直前に挿入）:**
```
# old_str の先頭部分（ルートA行の開始）:
        <tr class="ra">
          <td>🔴</td>
          <td>
            <strong style="color:#f87171">ルートA</strong>

# new_str（ルートBをコピーして先に配置 + ルートA継続）:
        <tr class="rb">
          ← ここにルートBの全内容を view で確認して貼り付け →
        </tr>

        <tr class="ra">
          <td>🔴</td>
          <td>
            <strong style="color:#f87171">ルートA</strong>
```

**Step B - 元のルートB行を削除:**
```
# old_str（元の位置のルートB行 ― viewで確認した完全なブロック）:
        <tr class="rb">
          ← ルートBの全内容 →
        </tr>

# new_str: （空文字 = 削除）
```

---

## PATCH-05: ルートCにメキシコ産原油を追記

### 目的
2026年7月予定の日本向けメキシコ産原油1百万バレルを新情報として追記

### 対象
ルートC🇺🇸の説明セル内、アラスカの説明の後に追加

### str_replace

**ルートC説明セル内、アラスカ関連テキストの末尾を探す。以下の文字列の直後に追記：**

**old_str（ルートC 説明セル末尾付近）:**
```
            <small style="color:#64748b">出典：Reuters・Bloomberg・日米首脳会談資料（3月）・UPI（3/19）</small>
```
※ 上記が見つからない場合は view でルートC説明セルの最終 `<small>` タグを確認してから適用

**new_str:**
```
            <strong style="color:#c084fc">🆕 メキシコ産原油（2026年7月・初便予定）：</strong>日量換算は小規模だが太平洋ルート約30〜35日で到着。3大チョークポイントを完全回避。<br>
            <small style="color:#64748b">出典：Reuters・Bloomberg・日米首脳会談資料（3月）・UPI（3/19）・DiscoveryAlert（4/26）</small>
```

---

## PATCH-06: 西アフリカ（ナイジェリア・アンゴラ）コラムカード本文の更新

### 目的
ダンゴテ製油所フル稼働・拡張計画・欧州輸出開始の最新情報を追加

### 対象
`原油輸入多様化の現実：ナイジェリア・アンゴラ・ブラジル調達の全貌` カードを探す

### str_replace

**old_str（カードのサブタイトル行）:**
```
      <div style="font-size:0.72rem;color:#94a3b8;margin-top:2px;">日本はホルムズ依存95%からの脱却を急ぐ ― 各国の状況・ボリューム・見通しを徹底解説</div>
```

**new_str:**
```
      <div style="font-size:0.72rem;color:#94a3b8;margin-top:2px;">日本はホルムズ依存95%からの脱却を急ぐ ― 各国の最新状況・ボリューム・ダンゴテ急拡大の全貌</div>
```

---
**ナイジェリア最新情報を追記（カード本文内のナイジェリア説明部分を探して更新）:**

`<strong style="color:#fbbf24;">🇳🇬 ナイジェリア` を含むブロック内に以下を追記。
viewで確認後、ナイジェリアの説明末尾に以下を挿入：

**追記内容（ナイジェリアの説明セクション末尾に追加）:**
```html
            <div style="background:rgba(251,191,36,0.08);border-left:3px solid #fbbf24;padding:8px 12px;margin-top:8px;border-radius:0 6px 6px 0;font-size:0.78rem;">
              <strong style="color:#fbbf24;">🆕 2026年5月 最新情報</strong><br>
              ダンゴテ製油所（アフリカ最大・日量65万BPD）がフル稼働達成。欧州・アフリカ向け燃料輸出を開始。
              2025年10月に1.4百万BPD（世界最大）への拡張計画を発表。
              南アフリカ・ガーナ・ケニア各政府が12ヶ月長期供給契約の交渉に入った。
              日本はスポット調達で輸入実績あり ✅。ホルムズ・バベルマンデブ・スエズの3大チョークポイントを完全回避。
              <small style="color:#64748b">出典：OilPrice・Wikipedia・Pravda Nigeria（5/6）・African Energy Week（4/8）</small>
            </div>
```

---

## PATCH-07: 「その他のルート」折り畳みセクションを追加

### 目的
ブラジル・メキシコ・イラク-チェイハン・カナダを影響度高い順で折り畳みに収容

### 挿入位置
西アフリカ・コラムカードの閉じタグ `</div><!-- /ナイジェリアコラムカード -->` の直後
（見つからない場合は `<!-- ルートC・アラスカ原油コラムカード -->` の前）

### new_str（追加ブロック全体）:

```html
<!-- ▼ その他の検討中ルート（折り畳み） -->
<div style="margin-top:24px;margin-bottom:32px;">

  <button onclick="
    var body = document.getElementById('other-routes-body');
    var isOpen = body.style.display !== 'none';
    body.style.display = isOpen ? 'none' : 'block';
    this.innerHTML = isOpen
      ? '▼ その他の検討中ルート（実績少・計画段階）― <span style=&quot;color:#fbbf24&quot;>影響度高い順</span>に表示'
      : '▲ その他の検討中ルートを閉じる';
  "
    style="width:100%;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.12);
           border-radius:8px;color:#94a3b8;font-size:0.8rem;font-weight:700;
           padding:12px 18px;cursor:pointer;text-align:left;letter-spacing:0.03em;
           transition:background 0.2s;">
    ▼ その他の検討中ルート（実績少・計画段階）― <span style="color:#fbbf24">影響度高い順</span>に表示
  </button>

  <div id="other-routes-body" style="display:none;margin-top:14px;">
    <div style="display:flex;flex-direction:column;gap:14px;">

      <!-- ① ブラジル（影響度1位 / 実績少） -->
      <div style="background:rgba(192,132,252,0.05);border:1px solid rgba(192,132,252,0.2);border-radius:10px;padding:14px 18px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;flex-wrap:wrap;">
          <span style="font-size:1rem;">🇧🇷</span>
          <strong style="color:#c084fc;font-size:0.85rem;">ブラジル→喜望峰→インド洋→日本</strong>
          <span style="font-size:0.72rem;background:rgba(192,132,252,0.15);border:1px solid rgba(192,132,252,0.3);color:#c084fc;padding:2px 8px;border-radius:4px;margin-left:auto;">約40〜45日</span>
        </div>
        <div style="font-size:0.78rem;color:#94a3b8;line-height:1.75;">
          チュピ・ブジオス油田からの良質原油（Tupi Blend）。
          ホルムズ・バベルマンデブ・スエズ3大チョークポイント完全回避。
          <strong style="color:#e2e8f0;">課題：</strong>日本向け到着は2026年後半以降の見込み。中国との競合激化・長距離コスト。精製時の品質調整が必要。
        </div>
        <div style="font-size:0.72rem;color:#64748b;margin-top:6px;">📌 実績：確認なし（計画・スポット交渉段階）</div>
      </div>

      <!-- ② メキシコ（影響度2位 / 7月予定のみ） -->
      <div style="background:rgba(52,211,153,0.04);border:1px solid rgba(52,211,153,0.15);border-radius:10px;padding:14px 18px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;flex-wrap:wrap;">
          <span style="font-size:1rem;">🇲🇽</span>
          <strong style="color:#34d399;font-size:0.85rem;">メキシコ→太平洋→日本</strong>
          <span style="font-size:0.72rem;background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.25);color:#34d399;padding:2px 8px;border-radius:4px;margin-left:auto;">約30〜35日</span>
        </div>
        <div style="font-size:0.78rem;color:#94a3b8;line-height:1.75;">
          <strong style="color:#fbbf24;">🆕 2026年7月初便予定：</strong>日本向け約100万バレルの輸送が計画中。
          太平洋直行ルートで3大チョークポイントを完全回避。往復所要日数は中東比で半分以下。
          輸送コスト：1バレルあたり2〜4ドル（中東比で競争力あり）。
          <strong style="color:#e2e8f0;">課題：</strong>総生産量の輸出余力は日量40〜50万BPDのみ（国内消費優先）。前例なし。
        </div>
        <div style="font-size:0.72rem;color:#64748b;margin-top:6px;">📌 実績：なし（2026年7月着予定・100万バレル）</div>
      </div>

      <!-- ③ イラク・キルクーク→トルコ・チェイハン（影響度3位） -->
      <div style="background:rgba(251,191,36,0.04);border:1px solid rgba(251,191,36,0.15);border-radius:10px;padding:14px 18px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;flex-wrap:wrap;">
          <span style="font-size:1rem;">🇮🇶</span>
          <strong style="color:#fbbf24;font-size:0.85rem;">イラク・キルクーク→🇹🇷トルコ・チェイハン（地中海）</strong>
          <span style="font-size:0.72rem;background:rgba(251,191,36,0.12);border:1px solid rgba(251,191,36,0.25);color:#fbbf24;padding:2px 8px;border-radius:4px;margin-left:auto;">🆕 3月再開</span>
        </div>
        <div style="font-size:0.78rem;color:#94a3b8;line-height:1.75;">
          <strong style="color:#4ade80;">✅ 2026年3月再開：</strong>10年以上の閉鎖から復活。初期輸送能力 日量25万BPD（最大容量1.6百万BPD）。
          バグダッド連邦政府とクルド自治区政府（KRG）が合意。地中海へ直結しホルムズを完全回避。
          IEAはバスラ〜チェイハン新規パイプライン建設も提言中。
          <strong style="color:#e2e8f0;">課題：</strong>ISIS・PKKによる攻撃リスク（過去に繰り返し閉鎖）。
          <strong style="color:#f87171;">⚠️ 2026年7月27日：</strong>イラク・トルコ1973年条約が期限切れ→交渉再開リスク。
          欧州向け主体で日本への直接供給実績はなし。
        </div>
        <div style="font-size:0.72rem;color:#64748b;margin-top:6px;">📌 実績：欧州向けのみ。日本向けは確認なし。</div>
      </div>

      <!-- ④ カナダ西岸（影響度4位） -->
      <div style="background:rgba(56,189,248,0.04);border:1px solid rgba(56,189,248,0.12);border-radius:10px;padding:14px 18px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;flex-wrap:wrap;">
          <span style="font-size:1rem;">🇨🇦</span>
          <strong style="color:#7dd3fc;font-size:0.85rem;">カナダ西岸（Trans Mountain）→太平洋直行→日本</strong>
          <span style="font-size:0.72rem;background:rgba(56,189,248,0.1);border:1px solid rgba(56,189,248,0.2);color:#7dd3fc;padding:2px 8px;border-radius:4px;margin-left:auto;">約14〜16日</span>
        </div>
        <div style="font-size:0.78rem;color:#94a3b8;line-height:1.75;">
          Trans Mountain拡張パイプライン（2024年完成）でアルバータ州の産油がバンクーバー港へ。
          太平洋最短ルートで地政学的リスクはほぼゼロ。3大チョークポイント完全回避。
          <strong style="color:#e2e8f0;">課題：</strong>日本向け長期契約の締結実績が未確認。
          重質油主体でカナダ産は日本の製油所設備との適合性要確認。
        </div>
        <div style="font-size:0.72rem;color:#64748b;margin-top:6px;">📌 実績：日本向け契約なし（可能性段階）</div>
      </div>

    </div><!-- /flex -->
  </div><!-- /#other-routes-body -->

</div><!-- /その他ルート折り畳み -->
```

---

## PATCH-08: ルートテーブルのヘッダー行に並び替え注記を追加

### 目的
テーブルが「影響度順」であることを明示

### 対象
ルートテーブルの `<thead>` 内、最初の `<th>` の前

**ルートテーブルのcaptionまたはtableタグ直後を探して追加**

viewで `<table` を含み、`輸送ルート比較` に近い箇所を確認後：

テーブルタイトル行があれば以下を付加：

**old_str（テーブルタイトル部分の例）:**
```
        <div style="font-size:0.8rem;font-weight:800;color:#a78bfa;margin-bottom:8px;">🗺️ 輸送ルート比較（日本向け）</div>
```

**new_str:**
```
        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:8px;">
          <div style="font-size:0.8rem;font-weight:800;color:#a78bfa;">🗺️ 輸送ルート比較（日本向け）</div>
          <span style="font-size:0.68rem;background:rgba(251,191,36,0.15);border:1px solid rgba(251,191,36,0.3);color:#fbbf24;padding:2px 8px;border-radius:4px;">↑ 日本への影響度（輸入シェア）高い順</span>
        </div>
```

---

## PATCH-09: 更新ログへの記載追加

### 対象
`<!--出典・更新ログ-->` セクション内の更新グリッド先頭

**old_str（更新グリッドの先頭行を探す ― `2026年5月8日` または最新の更新行）:**
```
<div>📅 <strong>2026年5月8日
```
※ viewで最新の更新ログ行を確認後、その直前に以下を挿入

**new_str（既存行の前に追加）:**
```html
<div>📅 <strong>2026年5月10日 更新</strong></div>
<div><span style="color:#4ade80;">2026/05/10</span> — <strong style="color:#86efac;">【ルート情報大幅更新】</strong>
  代替ルート情報を日本輸入シェア影響度順に再編成。
  ルートA：VTTI攻撃詳細更新（58%激減・衛星画像確認）。
  ルートB：330%急増・SUMED迂回オプション・二重チョークポイント問題追記。
  ルートC：メキシコ産7月初便予定を追加。
  西アフリカ：ダンゴテ製油所フル稼働・拡張計画（1.4百万BPD）追記。
  新設：折り畳み「その他の検討中ルート」（ブラジル・メキシコ・イラク-チェイハン・カナダ）。
</div>
```

---

## 作業完了チェックリスト

```
[ ] PATCH-01: ルートA説明テキスト更新（58%激減・ADNOCバラカ追記）
[ ] PATCH-02: ルートA ステータスpill更新
[ ] PATCH-03: ルートB説明更新（330%増・SUMED追記・二重チョークポイント）
[ ] PATCH-04: ルートテーブル行順並び替え（B→A→C→西アフリカ→D）
[ ] PATCH-05: ルートCにメキシコ産追記
[ ] PATCH-06: 西アフリカカードのサブタイトル更新・ダンゴテ新情報追加
[ ] PATCH-07: 「その他の検討中ルート」折り畳みセクション追加
[ ] PATCH-08: ルートテーブルヘッダーに「影響度順」注記追加
[ ] PATCH-09: 更新ログ追記
[ ] git add docs/index.html
[ ] git commit -m "feat: ルート情報大幅更新・影響度順再編成・その他ルート折り畳み追加（2026-05-10）"
[ ] git push
```

---

## 注意事項

1. **str_replace前に必ずview_rangeで対象行を確認** すること（プロジェクトナレッジのテキストは空白・改行が実ファイルと異なる場合あり）
2. PATCH-04（行並び替え）は特に慎重に。ビューで各trブロックの完全な内容を確認してから実施
3. PATCH-07の折り畳みHTMLを挿入する位置は、既存のコラムカード最後の `</div>` の直後かつ次のセクションの `<!-- コメント -->` の直前
4. git push後はGitHubのProject Knowledgeで手動「Sync now」を実施すること
