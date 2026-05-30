# rules_patch_s11.md — diffs-generation-rules.md への S11 折り畳み維持ルール追加

> **Claude Code への指示：** 以下の str_replace を `docs/tools/diffs-generation-rules.md` に適用してください。
> `docs/index.html` は触らないこと。
> 作業後に `git commit`（メッセージ: `docs: S11 折り畳み維持ルールを diffs-generation-rules.md に追加`）してください。
> **push は確認後に指示します。**

---

## 変更 1: S11 セルフチェック項目の拡充

**old_str**（現在のセルフチェック内 S11 2行）:
```
[ ] S11 更新ログ ― 先頭行に本日分が追記されているか
[ ] S11 JSON-LD ― `"dateModified": "YYYY-MM-DD"` が本日の日付に更新されているか ← Google評価に直結
```

**new_str**（S11 チェック項目を 5行に拡充）:
```
[ ] S11 更新ログ ― 先頭行に本日分が追記されているか
[ ] S11 常時表示3件 ― APPLY ブロック1で常時表示が正確に3件になっているか（4件以上は NG）
[ ] S11 折り畳み移動 ― APPLY ブロック2で旧3件目が log-collapse 先頭に挿入されているか
[ ] S11 総件数 ― 常時表示3 + log-collapse内エントリー数の合計が10以下か（超過時は最古を削除）
[ ] S11 JSON-LD ― `"dateModified": "YYYY-MM-DD"` が本日の日付に更新されているか ← Google評価に直結
```

---

## 変更 2: [S11] 詳細ルールセクションを新規追加

以下の old_str で一意のアンカーを特定し、その直後に new_str を挿入する。

**old_str**（diffs-generation-rules.md 内の既存の S11 注記行）:
```
> `<!--出典・更新ログ-->` セクションに表示する更新ログが11件を超えた場合は最古の1件を削除してください。
```

**new_str**（上記行を以下で置き換える）:
```
> `<!--出典・更新ログ-->` セクションに表示する更新ログが11件を超えた場合は最古の1件を削除してください。

---

## [S11] 更新ログ — 折り畳み維持ルール（詳細）

### 構造要件（常時維持すること）

```
常時表示エリア (color:#cbd5e1)
  ├── エントリー1 (本日更新分 = 最新)
  ├── エントリー2 (前回更新分)
  └── エントリー3 (前々回更新分)
log-toggle-top  ← 「📂 過去の履歴を見る」ボタン
log-collapse (display:none)
  └── (color:#94a3b8 div)
       ├── エントリー4 以降（旧3件目から順に蓄積）
       ├── 出典リンク ①〜⑧（削除不可）
       └── log-toggle-bottom (display:none)  ← 「▲ 閉じる」ボタン
```

- **常時表示は必ず3件固定**
- **log-collapse は 4件目〜10件目を保持**（最大7件 + 出典リンク）
- 合計11件を超えたら log-collapse の最古エントリー（出典リンク直前）を削除し
  `update_log.json` の先頭に追加する

---

### [S11] APPLY ブロック 必須構成（毎回 2ブロック）

毎回の更新で S11 は **必ず 2 つの APPLY ブロック**を生成する。

#### ブロック1: 常時表示エリアの更新（3件固定を維持）

```
APPLY ブロック1
  old_str = 旧エントリー1 + 旧エントリー2 + 旧エントリー3（3エントリー分のHTML全体）
  new_str = 新エントリー（本日分）+ 旧エントリー1 + 旧エントリー2（合計3件）
```

> ⚠️ **旧エントリー3 は new_str に含めない。**
> 旧エントリー3 はブロック2で log-collapse に追加する。
> ブロック1の new_str に4件以上含めることは禁止。

**フォーマット例（ブロック1）:**

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年XX月YY日 HH:MM JST</strong> 更新</div>
        <div><span style="color:#...;">2026/XX/YY HH:MM</span> — [旧1件目内容]</div>
        <div>📅 <strong>2026年XX月ZZ日 HH:MM JST</strong> 更新</div>
        <div><span style="color:#...;">2026/XX/ZZ HH:MM</span> — [旧2件目内容]</div>
        <div>📅 <strong>2026年XX月WW日 HH:MM JST</strong> 更新</div>
        <div><span style="color:#...;">2026/XX/WW HH:MM</span> — [旧3件目内容]</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年MM月DD日 HH:MM JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/MM/DD HH:MM</span> — [本日分内容]</div>
        <div>📅 <strong>2026年XX月YY日 HH:MM JST</strong> 更新</div>
        <div><span style="color:#...;">2026/XX/YY HH:MM</span> — [旧1件目内容]</div>
        <div>📅 <strong>2026年XX月ZZ日 HH:MM JST</strong> 更新</div>
        <div><span style="color:#...;">2026/XX/ZZ HH:MM</span> — [旧2件目内容]</div>
<!-- NEW:END -->
<!-- APPLY:END -->

#### ブロック2: log-collapse への旧3件目の挿入

```
APPLY ブロック2
  old_str = log-collapse の先頭固定アンカー（コメント + div 2行 + 現在の先頭エントリー1行目）
  new_str = 同じアンカー + 旧エントリー3（2行）を先頭に挿入
```

> ⚠️ ブロック2の old_str は「現在の log-collapse 先頭エントリー」を含む必要がある。
> 毎回変化するため、project_knowledge_search で現在の log-collapse 先頭行を確認してから書くこと。

**フォーマット例（ブロック2）:**

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>[現在のlog-collapse先頭エントリーの日付]</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年XX月WW日 HH:MM JST</strong> 更新</div>
          <div><span style="color:#...;">2026/XX/WW HH:MM</span> — [旧3件目内容]</div>
          <div>📅 <strong>[現在のlog-collapse先頭エントリーの日付]</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

### S11 生成フロー（毎回の手順）

1. project_knowledge_search で「更新ログ 常時表示 log-collapse」を検索
2. 現在の **常時表示3件**（旧1・旧2・旧3）を確認する
3. 現在の **log-collapse 先頭エントリー**の日付行を確認する
4. **ブロック1** を生成:
   - old_str: 現在の常時表示3件（全HTML）
   - new_str: 本日分 + 旧1 + 旧2（3件のみ）
5. **ブロック2** を生成:
   - old_str: log-collapse 固定アンカー + 現在の先頭エントリー1行目
   - new_str: 同 + 旧3（2行）を先頭に挿入
6. 合計エントリー数（常時3 + collapse内）が10を超えるなら
   collapse の最古エントリー（出典リンク `<div>①` の直前）を削除するブロックを追加

---

### よくある失敗パターン（禁止）

❌ **NG**: ブロック1の new_str に旧3件目を含める（4件以上になる）
❌ **NG**: ブロック2を省略して、旧3件目を log-collapse に移動しない
❌ **NG**: ブロック2の old_str に log-collapse 先頭エントリーを含めず、アンカーが曖昧になる
❌ **NG**: log-toggle-bottom や出典リンク①〜⑧の位置を変更する
```

---

## 変更 3: セクション対応表の S11 備考を更新

**old_str**（セクション対応表内 S11 行）:
```
| [S11] | ステップ11 | 更新ログ追記 | `<!--出典・更新ログ-->` | |
```

**new_str**:
```
| [S11] | ステップ11 | 更新ログ追記 + 折り畳み維持 | `<!--出典・更新ログ-->` | ⚠️ 必ず2ブロック構成（常時表示3件固定 + log-collapse先頭挿入）|
```

---

## 確認

上記3箇所を str_replace で適用後、以下を確認してください：

```bash
grep -n "S11\|折り畳み維持\|ブロック1\|ブロック2\|log-collapse先頭" docs/tools/diffs-generation-rules.md | head -20
```

期待される出力：S11 関連の新規行が複数ヒットすること。
