# index_html_diffs.md — タンカー1隻の価値 サムネイル追加

## 前提作業（Claude Code が最初に実施すること）

```bash
# ① 画像をリポジトリの images/ にコピー
cp /path/to/タンカー1隻の価値.png docs/images/tanker-value.png
```
> ※ ユーザーが Windows の Downloads などに `タンカー1隻の価値.png` を置いた場合は
>   `docs/images/tanker-value.png` として git add すること。

---

## [P01] CSS追加 — タンカー価値サムネイルボタン

**挿入位置：** `/* タンカー足止めオーバーレイ */` ブロックの直前（`#map { position: relative; }` の手前）

**変更前（この行の直前に挿入）：**
```css
/* ================================================
   タンカー足止めオーバーレイ
================================================ */
```

**挿入するCSS：**
```css
/* ================================================
   タンカー1隻の価値 サムネイルボタン
================================================ */
#tanker-value-thumb {
  position: absolute;
  bottom: 30px;
  right: 278px;      /* tanker-overlay(260px) + gap(8px) + right(10px) */
  z-index: 1000;
  width: 80px;
  cursor: pointer;
  background: rgba(10, 20, 50, 0.85);
  border: 1px solid rgba(251, 191, 36, 0.5);
  border-radius: 8px;
  padding: 5px;
  backdrop-filter: blur(4px);
  box-shadow: 0 4px 20px rgba(0,0,0,0.55);
  transition: border-color 0.2s, transform 0.15s;
  text-align: center;
  user-select: none;
}
#tanker-value-thumb:hover {
  border-color: rgba(251, 191, 36, 0.9);
  transform: scale(1.04);
}
#tanker-value-thumb img {
  width: 100%;
  border-radius: 5px;
  display: block;
  pointer-events: none;
}
#tanker-value-thumb .tv-label {
  font-size: 8px;
  color: #fbbf24;
  margin-top: 4px;
  line-height: 1.3;
  font-weight: bold;
  letter-spacing: 0.03em;
}
@media (max-width: 600px) {
  #tanker-value-thumb {
    width: 60px;
    right: 210px;   /* スマホ時はオーバーレイが折り畳まれるため詰める */
    bottom: 24px;
  }
  #tanker-value-thumb .tv-label { font-size: 7px; }
}

```

---

## [P02] HTML追加 — サムネイルボタン要素

**挿入位置：** `<div id="tanker-overlay">` の直前（同じ `<div id="map">` 内）

**変更前（この行の直前に挿入）：**
```html
  <div id="tanker-overlay">
```

**挿入するHTML：**
```html
  <!-- タンカー1隻の価値 サムネイルボタン -->
  <div id="tanker-value-thumb" onclick="toggleTankerValuePopup()" title="タンカー1隻の価値をポップアップ表示">
    <img src="images/tanker-value.png" alt="タンカー1隻の価値">
    <div class="tv-label">📊 タンカー<br>1隻の価値</div>
  </div>

```

---

## [P03] JavaScript追加 — ポップアップトグル関数

**挿入位置：** `// ============================================================` で始まる
`// 日本関連タンカー足止め可視化 v2.1` ブロックの **直前**

**挿入するJS：**
```javascript
// ============================================================
// タンカー1隻の価値 ポップアップ
// ============================================================
function toggleTankerValuePopup() {
  const overlay = document.getElementById('lightbox-overlay');
  if (!overlay) return;
  if (overlay.classList.contains('active')) {
    closeLightbox();
  } else {
    openLightbox('images/tanker-value.png');
  }
}

```

---

## 変更サマリー

| 変更 | 内容 |
|------|------|
| CSS追加 | `#tanker-value-thumb` のスタイル（PC・スマホ両対応） |
| HTML追加 | `#tanker-overlay` 左隣に浮動サムネイルボタン |
| JS追加 | `toggleTankerValuePopup()` — 既存 `openLightbox` / `closeLightbox` を流用 |
| 画像配置 | `docs/images/tanker-value.png` に配置（git add 必須） |

## 注意事項

- 既存の `#lightbox-overlay` / `openLightbox()` / `closeLightbox()` は**変更しない**
- `right: 278px` はPC時の値。`#tanker-overlay` の幅(260px) + margin(8px) + right(10px)
- スマホ時は `#tanker-overlay` が折り畳まれるため `right: 210px` に調整済み
- 画像ファイル名はASCIIにする（`tanker-value.png`）。日本語ファイル名はURLエンコード問題が出る場合がある

## commit メッセージ（案）

```
feat: タンカー1隻の価値 サムネイルポップアップ追加（MAP左隣）
```
