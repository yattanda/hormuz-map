# Design System

このドキュメントは、HTMLサイト全体のレイアウトの基準（レスポンシブ・余白・表・画像）を定義する。
Claude CodeがHTML/CSSを修正する際は、この基準を優先する。

**見た目の決まり（色・書体・アイコン・区切り方・ボタン・カード）の正本は設計書 `tools/site-redesign-design.md`（§1〜§4-2）と、スキル `.claude/skills/site-design/SKILL.md`。**
このファイルには、それと重ならない今も有効な所だけを残した（2026-10-22・課題46 D3 PR 7b。以前は明るい地の `--color-*` の色・角丸のボタンとカードの例を載せていたが、いまのサイトと合わないので外した）。

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

画面の作法（段は太い罫・箱や角丸や影で区切らない・状態は色面の札）は設計書 §1 とスキル `site-design`。

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

最重要基準は **375px** とする。タブレット（768px 前後）も毎回確かめる。

### breakpoint

`docs/assets/css/tokens.css` の末尾の覚書が正本（2026-09-18 に3つへ整理）。境界の値は「以下（max-width）」側に含める。

| 幅 | 役割 | 書き方 |
|---|---|---|
| 600px | スマホ縦の詰め（余白・小物） | `max-width:600px` / `min-width:601px` |
| 768px | 文字サイズ（スマホは `html { font-size:18px }`・変更禁止） | `max-width:768px` / `min-width:769px` |
| 1023px | 表・地図凡例の狭幅対応、PC との境 | `max-width:1023px` / `min-width:1024px` |
| 1199px | **`/hormuz/` のヘッダーだけ**：バッジの列を次の行へ送る（〜1199px）か、列の中で折り返す（1200px〜）か | `max-width:1199px` / `min-width:1200px` |

カラム数は 〜600px 1列／601〜1023px 2列／1024px〜 3列。新しい境界の値を足さない。1199px は 2026-11-02 に、書体の差し替えでヘッダーが伸び縮みする CLS を直すために足した例外（運営者の決定・`hormuz-map` PR #151）。ヘッダーのほかでは使わない。

---

## 3. CSS設計方針

- 固定幅を避ける。`clamp()`, `min()`, `max()` を活用する
- 余白・文字サイズ・色は `tokens.css` の変数を使う（色は変数だけ。直書きは `tools/validate_daily.py` が WARN を出す）
- ページ固有CSSを増やしすぎない。共通の部品を優先する（CSS の置き場所は `docs/assets/css/`。ページ内の `<style>` に足さない）
- `!important` を安易に使わない

---

## 4. 余白

`tokens.css` の `--space-*` を使う。

| 用途 | 値 |
|---|---|
| 小さな要素間 | `--space-xs` |
| 本文内の間隔 | `--space-sm` / `--space-md` |
| 段の中の区切りの前後 | `--space-md` / `--space-lg` |
| 段の中の gap | `--space-lg` / `--space-xl` |
| 段の上下 | `--space-xl` / `--space-2xl` |

- スマホでは左右16px程度の余白を基本とする。左右 padding を広くしすぎない
- スマホで `--space-3xl` を多用しない。段の間が広すぎるときは、まず段の上下の padding を確かめる
- 1画面に何も情報が入らない状態を避ける

---

## 5. 文字の大きさ

- 大きさは `tokens.css` の `--fs-*`、行間は `--lh-body`（1.7）、行長は `--measure`（70ch）
- 補足文でもスマホでは極端に小さくしない
- 書体（BIZ UDPゴシック＋IBM Plex Sans Condensed）は設計書 §4-1 とスキル `site-design`

---

## 6. 押せる所

- タップ領域は最低44px程度を確保する
- 押せる所どうしの間隔を詰めすぎない
- 形と色（差し色の面・`--c-on-accent` の文字）はスキル `site-design`

---

## 7. tables

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
- 列幅を固定しすぎない（`/hormuz/` のルート表の `<colgroup>` は `html-safe-edit` の決まりどおり触らない）
- 読みやすさを優先する
- 罫は `--c-rule`（設計書 §1）

---

## 8. images

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
- アイコンは画像ではなく `docs/assets/icons/icons.svg` の `<symbol>`（スキル `site-design`）

---

## 9. 禁止・注意事項

- 固定幅pxを多用しない
- PC用のデザインをそのままスマホへ縮小しない
- ページごとに似たCSSを重複させない
- テーブルを無理にスマホ画面内へ押し込まない
- 色・絵文字・グラデーション・影・角丸のカードなど、見た目で使わないものは設計書 §3 とスキル `site-design`
