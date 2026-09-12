# Mobile UI Rules

このドキュメントは、スマホ表示を改善・レビューする際の判断基準を定義する。  
スマホUI修正時は必ずこのルールを参照する。

---

## 1. 最重要方針

スマホ表示では以下を最優先する。

1. 読みやすい
2. 余白が過剰でない
3. 重要情報に早く到達できる
4. 横はみ出しがない
5. 表やカードが無理なく読める
6. タップしやすい
7. PC表示を壊さない

---

## 2. 確認viewport

以下の幅を基準にする。

| viewport | 用途 |
|---:|---|
| 360px | 小型スマホ確認 |
| 375px | 最重要確認幅 |
| 390px | iPhone標準幅 |
| 430px | 大きめスマホ |
| 768px | タブレット |
| 1024px以上 | PC副作用確認 |

Claudeがレビューする場合、特に **375px表示** を基準に判断する。

---

## 3. ファーストビュー

### チェック項目

- H1が大きすぎないか
- 上部余白が広すぎないか
- 最初の画面でページの目的が分かるか
- CTAまたは次の行動が見えるか
- 画像や装飾が大きすぎないか
- ファーストビューで情報が少なすぎないか

### 判断基準

悪い例:

- 画面の半分以上が余白
- H1だけで画面が埋まる
- CTAがかなり下までスクロールしないと見えない
- 装飾画像が主役になっている

良い例:

- H1、説明文、CTAの一部が自然に見える
- 余白はあるが間延びしていない
- ページの目的がすぐ分かる

---

## 4. 余白

### 左右padding

スマホでは基本的に以下を目安にする。

```css
padding-inline: 1rem;
```

または、

```css
width: min(100% - 2rem, 1120px);
```

### section上下余白

スマホでは以下を目安にする。

```css
padding-block: 2rem;
```

可変にする場合:

```css
padding-block: clamp(2rem, 6vw, 4rem);
```

### 注意

- スマホで `padding: 80px 40px;` のような指定は広すぎる可能性が高い
- marginとpaddingの重複に注意する
- card内paddingとsection paddingが重なって情報密度が下がらないようにする

---

## 5. 文字サイズ

### 本文

```css
font-size: 1rem;
line-height: 1.7;
```

本文は16px前後を基本とする。

### 補足文

```css
font-size: 0.875rem;
line-height: 1.6;
```

14px未満を多用しない。

### H1

```css
font-size: clamp(1.6rem, 6vw, 2.8rem);
line-height: 1.2;
```

### H2

```css
font-size: clamp(1.35rem, 4.5vw, 2.2rem);
line-height: 1.3;
```

### 注意

- スマホでH1が大きすぎる場合、まず `font-size` と `line-height` を確認する
- `letter-spacing` が広すぎると読みにくい
- `line-height` が広すぎると間延びする

---

## 6. 行間

| 要素 | 目安 |
|---|---|
| 本文 | 1.6〜1.8 |
| 見出し | 1.2〜1.35 |
| 補足文 | 1.5〜1.7 |
| ボタン | 1.1〜1.3 |

注意:

- 見出しに本文並みの `line-height` を使うと間延びする
- 本文の `line-height` が2.0以上だと、スマホでは縦に長くなりすぎる場合がある

---

## 7. カード

### チェック項目

- カード内paddingが広すぎないか
- カード間gapが広すぎないか
- 1カードが縦に長くなりすぎていないか
- カード内の見出し・本文・ボタンの間隔が適切か

### 推奨CSS

```css
.card {
  padding: clamp(1rem, 3vw, 1.5rem);
  border-radius: 1rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: clamp(1rem, 3vw, 1.5rem);
}
```

---

## 8. グリッド・flex

### grid

スマホで自然に1列になるようにする。

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: 1rem;
}
```

### flex

折り返しが必要な場合は `flex-wrap` を使う。

```css
.flex-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
```

### 注意

- `display: flex` のまま横並び固定になっていないか確認する
- `min-width` が原因で横はみ出ししていないか確認する
- `gap` が広すぎて情報密度が下がっていないか確認する

---

## 9. 表・テーブル

スマホ表示で最も崩れやすい要素として扱う。

### 原則

表はスマホ画面に無理やり全列を収めない。

### 選択肢

#### A. 横スクロール型

比較表、料金表、数値表に向いている。

```html
<div class="table-scroll">
  <table>
    ...
  </table>
</div>
```

```css
.table-scroll {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.table-scroll table {
  min-width: 640px;
  border-collapse: collapse;
}
```

#### B. カード型

各行が独立した情報の場合に向いている。

```css
@media (max-width: 600px) {
  .responsive-table thead {
    display: none;
  }

  .responsive-table tr {
    display: block;
    margin-bottom: 1rem;
    border: 1px solid var(--color-border);
    border-radius: 0.75rem;
    padding: 1rem;
  }

  .responsive-table td {
    display: grid;
    grid-template-columns: 7em 1fr;
    gap: 0.75rem;
  }

  .responsive-table td::before {
    content: attr(data-label);
    font-weight: 700;
  }
}
```

この方式を使う場合、HTML側に `data-label` を入れる。

```html
<td data-label="項目">内容</td>
```

#### C. 重要列だけ表示

列が多すぎる表では、スマホ用に重要列だけ表示することを検討する。

### 注意

- `table-layout: fixed;` が適切か確認する
- `white-space: nowrap;` が読みづらさを生んでいないか確認する
- セル内テキストが極端に細く折り返されていないか確認する
- 数字や短いラベルだけ `nowrap` にするのは可
- 長文セルは折り返しを許可する

---

## 10. 横はみ出し

### よくある原因

- 固定幅 `width: 600px`
- 固定 `min-width`
- flex itemの縮小不可
- table
- 長いURL
- 長い英単語
- 画像
- negative margin
- `100vw` 指定

### 対策

```css
img,
video,
iframe {
  max-width: 100%;
}

.long-text {
  overflow-wrap: anywhere;
}

.flex-item {
  min-width: 0;
}
```

`width: 100vw` はスクロールバー分ではみ出す場合があるため注意する。

---

## 11. CTA・ボタン

### 基準

- タップ領域は最低44px程度
- テキストは短く明確にする
- スマホでは横幅いっぱいも検討する
- ボタン上下の余白を広くしすぎない

### CSS例

```css
.button {
  min-height: 44px;
  padding: 0.75rem 1rem;
}
```

---

## 12. 修正時の流れ

スマホ表示を改善するときは、以下の順で進める。

1. `mobile-ui-reviewer` で問題点を整理する
2. 原因CSS/HTMLを特定する
3. `responsive-css-specialist` で修正方針を作る
4. 共通CSSで直せるものを優先する
5. ページ固有CSSは最後にする
6. PC表示への副作用を確認する
7. 変更内容をMemory.mdに記録する

---

## 13. Claudeへの依頼テンプレート

スマホ改善を依頼するときは、以下のように依頼する。

```
このページのスマホ表示を改善したいです。

まず mobile-ui-reviewer として、修正せずに問題点を整理してください。

確認viewport:
- 360px
- 375px
- 390px
- 430px

重点確認:
- 余白
- 文字サイズ
- 見出し
- ファーストビュー
- 表
- カード
- 横はみ出し
- 情報密度

その後、responsive-css-specialist として修正案を出してください。
いきなり編集せず、原因CSSと修正方針を先に説明してください。
```

---

## 14. 合格基準

スマホ表示改善後、以下を満たすこと。

- 375pxで横スクロールが発生しない（ただし、意図したテーブル横スクロールは可）
- 本文が読みやすい
- H1/H2が画面を圧迫しすぎない
- セクション間の余白が過剰でない
- ファーストビューでページの目的が分かる
- CTAが分かりやすい
- 表が読める
- カードが縦に間延びしない
- PC表示が大きく崩れていない

---

## 15. 禁止事項

- 「いい感じに」だけで大幅変更する
- 理由なく余白を増やす
- 固定幅を増やす
- `!important` を多用する
- ページ固有CSSを大量追加する
- PC表示を確認せずスマホだけ直す
- 表を無理に狭い画面へ押し込む

---

## 16. 優先度評価の注意

ユーザーが実際に違和感を感じている箇所は、レビュー上の一般的な優先度より高く扱う。

特に以下はスマホUIで優先度を高める。

- 横スクロール
- 右余白
- 表の列幅
- 段落間の過剰な空白
- ファーストビューの間延び
- 本番とローカルの表示差分
