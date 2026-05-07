# Design System

このドキュメントは、HTMLサイト全体のデザイン基準を定義する。  
Claude CodeがHTML/CSSを修正する際は、この基準を優先する。

---

## 1. デザイン方針

このサイトのデザインでは、以下を重視する。

1. スマホで読みやすい
2. 情報が探しやすい
3. 余白を使いすぎない
4. 信頼感がある
5. 装飾より内容を優先する
6. PCとスマホで印象が大きく変わらない
7. ページごとのデザイン差を小さくする

---

## 2. レスポンシブ基準

主要な確認viewportは以下。

| 種別 | 幅 |
|---|---:|
| 小型スマホ | 360px |
| 標準スマホ | 375px |
| iPhone標準 | 390px |
| 大きめスマホ | 430px |
| タブレット | 768px |
| PC | 1024px以上 |

最重要基準は **375px** とする。

---

## 3. CSS設計方針

### 基本方針

- モバイルファーストで書く
- PC向けの調整は `@media (min-width: ...)` を使う
- 固定幅を避ける
- `clamp()`, `min()`, `max()` を活用する
- 余白・文字サイズ・色はなるべく変数化する
- ページ固有CSSを増やしすぎない
- 共通コンポーネントを優先する

---

## 4. デザイントークン

### spacing

```css
:root {
  --space-2xs: 0.25rem;
  --space-xs: 0.5rem;
  --space-sm: 0.75rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  --space-3xl: 4rem;
}
```

使用目安:

| 用途 | 値 |
|---|---|
| 小さな要素間 | `--space-xs` |
| 本文内の間隔 | `--space-sm` / `--space-md` |
| カード内padding | `--space-md` / `--space-lg` |
| セクション内gap | `--space-lg` / `--space-xl` |
| セクション上下余白 | `--space-xl` / `--space-2xl` |

スマホで `--space-3xl` を多用しない。

---

## 5. layout

### container

基本のコンテナ幅。

```css
.container {
  width: min(100% - 2rem, 1120px);
  margin-inline: auto;
}
```

スマホでは左右16px程度の余白を基本とする。

### section

```css
.section {
  padding-block: clamp(2rem, 6vw, 4rem);
}
```

スマホでセクション間が広すぎる場合、まず `padding-block` を確認する。

---

## 6. typography

### 基本文字サイズ

```css
html {
  font-size: 100%;
}

body {
  font-size: 1rem;
  line-height: 1.7;
}
```

### 見出し

```css
h1,
.h1 {
  font-size: clamp(1.6rem, 6vw, 2.8rem);
  line-height: 1.2;
  letter-spacing: -0.02em;
}

h2,
.h2 {
  font-size: clamp(1.35rem, 4.5vw, 2.2rem);
  line-height: 1.3;
}

h3,
.h3 {
  font-size: clamp(1.15rem, 3.5vw, 1.6rem);
  line-height: 1.35;
}
```

### 本文

```css
p {
  font-size: 1rem;
  line-height: 1.7;
}
```

### 補足文

```css
.small-text {
  font-size: 0.875rem;
  line-height: 1.6;
}
```

補足文でもスマホでは極端に小さくしない。

---

## 7. color

現在のサイトカラーに合わせて調整すること。

```css
:root {
  --color-bg: #ffffff;
  --color-surface: #f8fafc;
  --color-text: #1f2937;
  --color-muted: #6b7280;
  --color-border: #e5e7eb;
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-accent: #f97316;
}
```

### 色の方針

- 本文は十分なコントラストを確保する
- 薄いグレー文字を多用しない
- CTAは他のリンクより目立たせる
- 背景色を増やしすぎない

---

## 8. buttons

### 基本ボタン

```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0.75rem 1rem;
  border-radius: 999px;
  font-weight: 700;
  line-height: 1.2;
  text-decoration: none;
}
```

### スマホでの注意

- タップ領域は最低44px程度を確保する
- 横幅いっぱいにする場合は `width: 100%` を検討する
- ボタン同士の間隔を詰めすぎない
- CTAがファーストビューから遠くなりすぎないようにする

---

## 9. cards

### 基本カード

```css
.card {
  padding: clamp(1rem, 3vw, 1.5rem);
  border: 1px solid var(--color-border);
  border-radius: 1rem;
  background: var(--color-bg);
}
```

### カードグリッド

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: clamp(1rem, 3vw, 1.5rem);
}
```

### スマホでの注意

- カード内paddingが広すぎないようにする
- カードが縦に長くなりすぎないようにする
- 1画面に何も情報が入らない状態を避ける

---

## 10. tables

### 基本方針

スマホでは表を無理に画面幅へ圧縮しない。

優先順位:

1. 横スクロール
2. カード型表示
3. 重要列だけ表示
4. 表を分割する

### 横スクロール型

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

### セル

```css
th,
td {
  padding: 0.75rem;
  vertical-align: top;
}
```

### 注意

- `white-space: nowrap` を安易に使わない
- すべての列をスマホ画面内に押し込まない
- 列幅を固定しすぎない
- 読みやすさを優先する

---

## 11. images

```css
img {
  max-width: 100%;
  height: auto;
}
```

画像の注意:

- スマホで横はみ出ししない
- 不要に大きな画像余白を作らない
- ファーストビューの画像が大きすぎる場合は調整する

---

## 12. breakpoint

基本breakpoint:

```css
@media (min-width: 600px) {
  /* 大きめスマホ・小型タブレット */
}

@media (min-width: 768px) {
  /* タブレット */
}

@media (min-width: 1024px) {
  /* PC */
}
```

原則として `max-width` より `min-width` を優先し、モバイルファーストにする。

---

## 13. 禁止・注意事項

- 固定幅pxを多用しない
- スマホで左右paddingを広くしすぎない
- セクション上下余白を広くしすぎない
- PC用のデザインをそのままスマホへ縮小しない
- `!important` を安易に使わない
- ページごとに似たCSSを重複させない
- テーブルを無理にスマホ画面内へ押し込まない
