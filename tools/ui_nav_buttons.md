# ui_nav_buttons.md — 30秒カラム ナビゲーションボタン & 枠線強化

> Claude Code への指示：以下の差分を docs/index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## [UI-01] テキストリンク → 目立つナビゲーションボタンに変換

**対象：** `<!-- テキストリンク行 -->` のコメント直後の `<span>` ブロック全体

**変更前：**
```html
      <!-- テキストリンク行 -->
      <span style="color:#e2e8f0;font-size:0.95rem;line-height:1.6;">↓
        <a href="#situation" style="color:#38bdf8;text-decoration:none;border-bottom:1px solid rgba(56,189,248,0.4);">情勢カード</a>で各プレイヤーの最新動向を確認 →
        <a href="#routes" style="color:#38bdf8;text-decoration:none;border-bottom:1px solid rgba(56,189,248,0.4);">ルート表</a>で日本向け代替輸送の現状を把握 →
        <a href="#scenario" style="color:#38bdf8;text-decoration:none;border-bottom:1px solid rgba(56,189,248,0.4);">シナリオ</a>で今後の展開を整理。
      </span>
```

**変更後：**
```html
      <!-- テキストリンク行 -->
      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:6px;">
        <a href="#situation"
           style="display:inline-flex;align-items:center;gap:7px;
                  background:linear-gradient(135deg,rgba(239,68,68,0.22),rgba(239,68,68,0.08));
                  border:1.5px solid rgba(239,68,68,0.65);
                  color:#fca5a5;font-size:0.82rem;font-weight:700;
                  padding:9px 20px;border-radius:8px;text-decoration:none;
                  letter-spacing:0.03em;
                  box-shadow:0 2px 10px rgba(239,68,68,0.25);
                  transition:all 0.2s;"
           onmouseover="this.style.background='linear-gradient(135deg,rgba(239,68,68,0.38),rgba(239,68,68,0.18))';this.style.boxShadow='0 4px 16px rgba(239,68,68,0.4)'"
           onmouseout="this.style.background='linear-gradient(135deg,rgba(239,68,68,0.22),rgba(239,68,68,0.08))';this.style.boxShadow='0 2px 10px rgba(239,68,68,0.25)'">
          🌐 情勢カード
        </a>
        <a href="#routes"
           style="display:inline-flex;align-items:center;gap:7px;
                  background:linear-gradient(135deg,rgba(251,191,36,0.22),rgba(251,191,36,0.08));
                  border:1.5px solid rgba(251,191,36,0.65);
                  color:#fbbf24;font-size:0.82rem;font-weight:700;
                  padding:9px 20px;border-radius:8px;text-decoration:none;
                  letter-spacing:0.03em;
                  box-shadow:0 2px 10px rgba(251,191,36,0.25);
                  transition:all 0.2s;"
           onmouseover="this.style.background='linear-gradient(135deg,rgba(251,191,36,0.38),rgba(251,191,36,0.18))';this.style.boxShadow='0 4px 16px rgba(251,191,36,0.4)'"
           onmouseout="this.style.background='linear-gradient(135deg,rgba(251,191,36,0.22),rgba(251,191,36,0.08))';this.style.boxShadow='0 2px 10px rgba(251,191,36,0.25)'">
          🚢 ルート表
        </a>
        <a href="#scenario"
           style="display:inline-flex;align-items:center;gap:7px;
                  background:linear-gradient(135deg,rgba(56,189,248,0.22),rgba(56,189,248,0.08));
                  border:1.5px solid rgba(56,189,248,0.65);
                  color:#38bdf8;font-size:0.82rem;font-weight:700;
                  padding:9px 20px;border-radius:8px;text-decoration:none;
                  letter-spacing:0.03em;
                  box-shadow:0 2px 10px rgba(56,189,248,0.25);
                  transition:all 0.2s;"
           onmouseover="this.style.background='linear-gradient(135deg,rgba(56,189,248,0.38),rgba(56,189,248,0.18))';this.style.boxShadow='0 4px 16px rgba(56,189,248,0.4)'"
           onmouseout="this.style.background='linear-gradient(135deg,rgba(56,189,248,0.22),rgba(56,189,248,0.08))';this.style.boxShadow='0 2px 10px rgba(56,189,248,0.25)'">
          📊 シナリオ
        </a>
      </div>
```

---

## [UI-02] 30秒カラム 外枠ボーダー強化

**対象：** `<!-- 30秒で全体像を把握 -->` 直後の外側ラッパー div のスタイル

**探し方：** `<!-- 30秒で全体像を把握 -->` コメントの直後にある `<div` を探し、
その `style` 属性内の `border:` プロパティを変更する。

**変更前（borderの値）：**
```
border:1px solid rgba(255,255,255,0.08)
```

**変更後（borderの値）：**
```
border:2px solid rgba(56,189,248,0.45);box-shadow:0 0 18px rgba(56,189,248,0.08),inset 0 0 0 1px rgba(56,189,248,0.06)
```

> ※ border プロパティだけを上記に置き換える。
> 他の style 属性（padding, margin, border-radius など）はそのまま保持すること。

---

## 変更の意図（参考）

| 変更点 | 変更前 | 変更後 |
|---|---|---|
| リンクの見た目 | 下線付きテキスト | グラデーション背景 + ボックスシャドウ付きボタン |
| ボタンの色分け | 全て同色（青） | 情勢=赤・ルート=金・シナリオ=青（3色差別化） |
| ホバー効果 | なし | 背景濃化 + シャドウ強調 |
| 枠線太さ | 1px / opacity 0.08 | 2px / opacity 0.45 + 外周グロー |

