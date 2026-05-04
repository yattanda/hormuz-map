# index_html_diffs.md — 凡例 PC折りたたみ対応

## [P01] CSS変更 — legend-toggle-btn を PC でも表示

**変更前：**
```css
.legend-toggle-btn {
  display:none; 
  background:rgba(239,68,68,0.15);
  border:1px solid #ef4444;
  color:#fca5a5;
  font-size:0.7rem;
  font-weight:700;
  padding:2px 8px;
  border-radius:12px;
  cursor:pointer;
}
```

**変更後：**
```css
.legend-toggle-btn {
  display:inline-block;
  background:rgba(239,68,68,0.15);
  border:1px solid #ef4444;
  color:#fca5a5;
  font-size:0.7rem;
  font-weight:700;
  padding:2px 8px;
  border-radius:12px;
  cursor:pointer;
}
```

---

## [P02] CSS追加 — legend-body の折りたたみをグローバルに適用

**挿入位置：** `.leg-note { ... }` ブロックの直後（`/* STATS */` より前）

**変更前（この行の直前に挿入）：**
```css
/* STATS */
```

**挿入するCSS：**
```css
/* 凡例ボディ折りたたみ（PC・スマホ共通） */
.legend-body {
  display: none;
}
.map-legend.open .legend-body {
  display: block;
}

```

---

## 変更サマリー

| 変更 | 内容 |
|------|------|
| CSS変更 | `.legend-toggle-btn` の `display:none` → `display:inline-block` |
| CSS追加 | `.legend-body` の hide/show をグローバルルールとして追加 |

## 動作確認ポイント

- **PC**：ページ読み込み時は「開く」状態（`initLegendState()` が `.open` を付与済み）
- **PC**：ボタンクリックで本文が折りたたまれ、タイトル行（🗺️ 凡 例 ＋ボタン）だけ残る
- **スマホ**：既存動作（幅も縮まる）は維持される
- 既存の `toggleLegend()` / `initLegendState()` JS は**変更不要**

## commit メッセージ（案）

```
feat: 凡例折りたたみをPC表示にも対応
```
