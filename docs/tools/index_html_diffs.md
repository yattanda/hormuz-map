# index_html_diffs — 凡例ボタン修正 + テーブル右余白解消 2026-05-06

> Claude Code への指示：以下の2箇所を docs/index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> 適用後は commit してください。push はユーザーの確認後に実施。

---

## [CSS-1] 凡例ボタン修正（タップできない問題）

対象： @media(max-width:860px) ブロック内の .map-legend 関連CSS

変更前：
  .map-legend {
    min-width: 80px !important;
    max-width: 80px !important;
    padding: 8px 10px !important;
    transition: max-width 0.3s ease, min-width 0.3s ease, padding 0.3s ease;
    overflow: hidden;
    cursor: pointer;
    -webkit-tap-highlight-color: rgba(56,189,248,0.2);
    touch-action: manipulation;
  }
  .map-legend.open {
    min-width: 230px !important;
    max-width: 260px !important;
    padding: 12px 14px !important;
  }
  .map-legend h4 {
    font-size:0.75rem;
    white-space:nowrap;
    cursor: pointer;
    user-select: none;
    -webkit-user-select: none;
  }
  .legend-toggle-btn {
    display: inline-block;
    pointer-events: auto;
  }

変更後：
  .map-legend {
    min-width: 80px !important;
    max-width: 80px !important;
    padding: 8px 10px !important;
    transition: max-width 0.3s ease, min-width 0.3s ease, padding 0.3s ease;
    overflow: hidden;
    cursor: pointer;
    -webkit-tap-highlight-color: rgba(56,189,248,0.2);
    touch-action: manipulation;
  }
  .map-legend.open {
    min-width: 250px !important;
    max-width: 290px !important;
    padding: 12px 14px !important;
  }
  .map-legend h4 {
    font-size: 13px !important;
    white-space: nowrap;
    cursor: pointer;
    user-select: none;
    -webkit-user-select: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
  }
  .legend-toggle-btn {
    display: inline-block;
    pointer-events: auto;
    flex-shrink: 0;
    font-size: 11px !important;
    padding: 3px 8px !important;
    min-width: 44px;
    text-align: center;
  }

---

## [CSS-2] テーブル右余白解消（containerのpaddingを削減）

対象： /* ===== スマホ最適化 ===== */ @media (max-width: 600px) ブロック内の
      .container の padding指定

変更前：
  .container,
  [style*="max-width:960px"],
  [style*="max-width: 960px"] {
    padding-left: 6px !important;
    padding-right: 6px !important;
  }

変更後：
  .container,
  [style*="max-width:960px"],
  [style*="max-width: 960px"] {
    padding-left: 4px !important;
    padding-right: 4px !important;
  }

  /* ルートテーブルは端まで広げる */
  .rtable-wrap {
    margin-left: -4px !important;
    margin-right: -4px !important;
    width: calc(100% + 8px) !important;
    overflow-x: auto;
  }

---

## 確認ポイント（適用後）

- [ ] 地図凡例の「閉じる」ボタンがタップできるか
- [ ] テーブルの右余白が減り、表が広くなっているか
- [ ] 6列すべて表示・横スクロールなしで「状態」まで見えるか
- [ ] 他のセクション（ニュース・カード等）の余白が極端に狭くなっていないか
- [ ] PC表示（768px超）が崩れていないか
