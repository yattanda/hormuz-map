# index_html_diffs.md — 凡例ボタン 二重発火バグ修正

## 原因
ボタン `onclick="toggleLegend()"` → イベントが親div `#map-legend-ctrl` に伝播
→ divの `click` リスナーでもう1回 `toggleLegend()` 発火
→ 計2回トグル = 元に戻る = ノーリアクションに見える

---

## [P01] HTML修正 — ボタンに event を渡す

**変更前：**
```html
<button class="legend-toggle-btn" onclick="toggleLegend()" id="legend-btn">開く</button>
```

**変更後：**
```html
<button class="legend-toggle-btn" onclick="toggleLegend(event)" id="legend-btn">閉じる</button>
```
> ※ PCはデフォルト「開く」状態なのでボタン初期テキストは「閉じる」に変更

---

## [P02] CSS修正 — スマホのボタン pointer-events を有効化

**変更前（`@media(max-width:860px)` 内）：**
```css
  .legend-toggle-btn {
    display: inline-block;
    pointer-events: none;
  }
```

**変更後：**
```css
  .legend-toggle-btn {
    display: inline-block;
    pointer-events: auto;
  }
```

---

## [P03] JS修正 — div・h4 への click/touchstart リスナーを削除

**変更前：**
```javascript
  setTimeout(() => {
    const legend = document.getElementById('map-legend-ctrl');
    if (!legend) return;
    ['click','touchstart'].forEach(evtType => {
      legend.addEventListener(evtType, function(e) {
        e.stopPropagation();
        e.preventDefault();
        toggleLegend();
      }, { passive: false });
    });

    setTimeout(() => {
      const h4 = document.querySelector('#map-legend-ctrl h4');
      if (!h4) return;
      ['click','touchstart'].forEach(evtType => {
        h4.addEventListener(evtType, function(e) {
          e.stopPropagation();
          e.preventDefault();
          toggleLegend();
        }, { passive: false });
      });
    }, 1200);
  }, 1000);
```

**変更後（ブロックごと削除、凡例の初期状態設定だけ残す）：**
```javascript
  // 凡例はボタンのみでトグル（div全体クリックは廃止）
```

---

## 変更サマリー

| # | 変更 | 内容 |
|---|------|------|
| P01 | HTML | `toggleLegend()` → `toggleLegend(event)` でイベント伝播を停止 |
| P02 | CSS | スマホの `pointer-events:none` → `auto`（スマホでもボタンが押せる）|
| P03 | JS | div・h4 への click リスナーを削除（ボタン一本化）|

## 動作確認ポイント

- **PC**：「閉じる」ボタン押下 → 凡例が折りたたまれボタンが「開く」に変わる ✓
- **PC**：パネル本体クリック → 何も起きない（意図通り）✓
- **スマホ**：ボタン押下で開閉できる ✓

## commit メッセージ（案）

```
fix: 凡例ボタンの二重発火バグを修正・ボタン操作に一本化
```
