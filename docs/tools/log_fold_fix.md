# log_fold_fix.md — 更新履歴 常時表示3件制限 修正指示

> **Claude Code への指示：** 以下の手順を順番に実行してください。
> 変更箇所以外は絶対に触らないこと。
> 作業後に `git commit`（メッセージ: `fix: 更新履歴 常時表示3件制限 + 下閉じるボタン確認`）してください。
> **push は確認後に指示します。**

---

## 背景・目的

`<!--出典・更新ログ-->` セクションの「常時表示」エリアに
5/30・5/29・5/28 以外の多数のエントリーが入り込んでいる。
これを修正し：
- **デフォルト表示**：最新3件（5/30・5/29・5/28）のみ
- **「過去の履歴を見る」押下時**：4件目以降（5/27以前）が全展開
- **閉じるボタン**：上（log-toggle-top）と下（log-toggle-bottom）の2か所

---

## Step 1: 現状の行番号を把握する

以下のコマンドを実行して、更新ログセクションの構造を確認する。

```bash
grep -n "更新</div>\|log-toggle-top\|log-toggle-bottom\|log-collapse\|cbd5e1.*line-height\|94a3b8.*line-height\|折り畳みボタン" docs/index.html | head -30
```

**確認すべき行番号：**
- 常時表示div の開始行（`color:#cbd5e1`）
- `log-toggle-top` の行
- `log-collapse` div の行
- `log-toggle-bottom` の行

---

## Step 2: 常時表示エリアの全エントリーを確認する

Step 1 で特定した「常時表示div開始行」から「log-toggle-top行-3」まで `view_range` で確認する。

```
view docs/index.html [常時表示div開始行, log-toggle-top行-3]
```

**確認すべき情報：**
- 何件のエントリーが常時表示に入っているか
- 5/28 エントリーの本文（div）が閉じる行番号
- 5/28 の次のエントリー（4件目）の開始行番号

---

## Step 3: 移動するブロック（4件目以降）を抽出する

**4件目エントリーの開始行** から **常時表示div の閉じタグ（`</div>`）の行** まで
`view_range` で内容を確認し、このブロックの HTML をコピーしておく。

> ⚠️ この「移動するブロック」は Step 4 で log-collapse 先頭に挿入する。

---

## Step 4: str_replace を2回実行する

### 【4-A】 常時表示から4件目以降を削除する

`str_replace` を使い、以下を置換する：

- **old_str**：Step 3 で確認した「4件目エントリーの開始 div」から
  常時表示 div の閉じタグ `      </div>` まで（log-toggle-top の直前行まで）
- **new_str**：`      </div>` のみ（常時表示 div を正しく閉じる1行だけ）

> ⚠️ 常時表示エリア内の閉じタグを1個だけ残すこと。
> `<!-- 折り畳みボタン（上） -->` の前の `</div>` が正しく残るように確認すること。

---

### 【4-B】 log-collapse の先頭に4件目以降を挿入する

`str_replace` を使い、以下を置換する：

**old_str**（log-collapse の開始部分 — 以下は確認済みの固定テキスト）：
```html
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年5月4日 11:13 JST</strong> 更新</div>
```

**new_str**：上記の `log-collapse` 開始部分 **＋** Step 3 で抽出したブロック **＋** 5/4 エントリー行

```html
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          [Step 3 で抽出した4件目以降のエントリー HTML をここに貼り付ける]
          <div>📅 <strong>2026年5月4日 11:13 JST</strong> 更新</div>
```

> ⚠️ 色スタイルについて：
> 常時表示エリアのエントリーは `color:#cbd5e1`（明るい）、
> log-collapse内のdivは `color:#94a3b8`（暗い）で色が異なるが、
> エントリー個別の `<div>` 内の `<span style="color:#f87171;">` 等のインラインスタイルは
> そのまま引き継がれるため、**変更は不要**。
> 親divの色だけが `#94a3b8` になり、日付見出し行の文字色が少し暗くなる（これが正しい動作）。

---

## Step 5: log-toggle-bottom の動作を確認する

以下のコマンドで `log-toggle-bottom` の存在と配置を確認する。

```bash
grep -n "log-toggle-bottom\|▲ 閉じる" docs/index.html
```

**確認すべき内容：**

1. `log-toggle-bottom` が `log-collapse` の内側（`</div>` 閉じタグの直前）に存在するか
2. `display:none` の初期スタイルがあるか
3. onclick で `c.style.display='none'; b.style.display='none'; t.querySelector('button').textContent='📂 過去の履歴を見る'` が実行されるか

**現在の log-toggle-bottom の正しい形（確認用）：**

```html
        <div id="log-toggle-bottom" style="text-align:center;margin:8px 0 4px;display:none;">
          <button
            onclick="(function(){var c=document.getElementById('log-collapse');var t=document.getElementById('log-toggle-top');var b=document.getElementById('log-toggle-bottom');c.style.display='none';b.style.display='none';t.querySelector('button').textContent='📂 過去の履歴を見る';var btn=t.querySelector('button');var rect=btn.getBoundingClientRect();window.scrollBy({top:rect.top-80,behavior:'smooth'});})()"
            style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);color:#94a3b8;font-size:0.78rem;padding:6px 18px;border-radius:20px;cursor:pointer;transition:all 0.2s;"
            onmouseover="this.style.background='rgba(255,255,255,0.10)'"
            onmouseout="this.style.background='rgba(255,255,255,0.06)'">
            ▲ 閉じる
          </button>
        </div>
```

**上記と異なる場合は `str_replace` で修正する。**

---

## Step 6: 全体構造の確認（最終）

```bash
grep -n "log-toggle-top\|log-toggle-bottom\|log-collapse\|cbd5e1.*line-height\|94a3b8.*line-height\|折り畳みボタン" docs/index.html
```

**期待される構造：**

```
常時表示 div (color:#cbd5e1)
  ├── 5/30 エントリー（日付div + 内容div）
  ├── 5/29 エントリー（日付div + 内容div）
  └── 5/28 エントリー（日付div + 内容div）
log-toggle-top div  ← 「📂 過去の履歴を見る」ボタン
log-collapse div (display:none)
  └── (color:#94a3b8 div)
       ├── 5/27 エントリー ... 最古エントリー まで（全て）
       ├── 出典リンク ①〜⑧
       └── log-toggle-bottom div (display:none)  ← 「▲ 閉じる」ボタン
```

---

## Step 7: ブラウザ動作確認チェックリスト

- [ ] デフォルト: 5/30・5/29・5/28 の3件のみ表示
- [ ] 「📂 過去の履歴を見る」クリック → 4件目以降が全て展開される
- [ ] 展開後、上のボタンが「📂 閉じる」に変わる
- [ ] 展開後、`log-collapse` 末尾に「▲ 閉じる」ボタンが表示される
- [ ] 上の「📂 閉じる」クリック → 折り畳まれる
- [ ] 下の「▲ 閉じる」クリック → 折り畳まれてボタン位置付近にスクロール

---

## 注意事項

- `html { font-size: 18px }` は絶対に変更しないこと
- `log-toggle-bottom` の `onclick` と `style` は変更しないこと
- 出典リンク ①〜⑧ は `log-collapse` 内に残ること（削除不可）
- エントリーの内容・文章は一切変更しないこと
- 作業後 `git commit` してから push 確認を待つこと
