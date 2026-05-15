# 戦争リスク保険料率 修正 Diffs — 2026-05-15

## 修正根拠
- 7.00%はGemini推定値。一次ソース（S&P Global・Caixin）では確認されず
- 実際のピーク値：約2.5%（2026年3月上旬 / S&P Global）
- 現状推定（2026年5月）：1〜2%前後（Global SCM・5/7報告）
- 修正値として「2.0%」を採用（5月現状の実態中央値・説明しやすい値）

---

## ① hormuz-data- / data/manual-update.json

### 変更箇所 (str_replace)

**old_str:**
```
  "war_risk_premium_pct": 7.0,
  "war_risk_premium_source": "推定値（Gemini自動分析）",
```

**new_str:**
```
  "war_risk_premium_pct": 2.0,
  "war_risk_premium_source": "S&P Global・Caixin報告（2026/03）｜危機ピーク2.5% → 現在1〜2%前後",
```

---

## ② hormuz-data- / scripts/fetch_manual.py

### 変更箇所 (str_replace) — Geminiプロンプトの数値範囲修正

**old_str:**
```
  "war_risk_premium_pct": <戦争リスク保険料率 小数点1桁 現在は1.0〜7.5%の範囲>,
```

**new_str:**
```
  "war_risk_premium_pct": <戦争リスク保険料率 小数点1桁 現在は0.8〜2.5%の範囲（S&P Global・Caixin実績値。ピーク2.5%、現在1〜2%前後）>,
```

### 変更箇所 (str_replace) — 背景知識の保険料率記述修正

**old_str:**
```
- 戦争リスク保険料率は封鎖前の1%から大幅上昇中
```

**new_str:**
```
- 戦争リスク保険料率：平時0.025〜0.125% → 危機ピーク（3月上旬）約2.5% → 現在1〜2%前後（S&P Global・Caixin実績）
- Gemini推定は必ずこの実績レンジ内（0.8〜2.5%）に収めること
```

---

## ③ hormuz-map / index.html

### 変更箇所 (str_replace) — Card 4 card-sub に但し書き追加

**old_str:**
```
    <div class="card-sub" style="margin-top:8px;">
      通常時: 0.025〜0.05% ／ 現在: <span id="ins-val2" style="color:var(--yellow);font-weight:700;">—%</span><br/>
      タンカー1隻あたり +約 <span id="ins-cost">—</span> 万USD/航海<br/>
      <span style="font-size:0.63rem;">出典: <span id="ins-source">—</span></span>
    </div>
```

**new_str:**
```
    <div class="card-sub" style="margin-top:8px;">
      通常時: 0.025〜0.125% ／ 現在: <span id="ins-val2" style="color:var(--yellow);font-weight:700;">—%</span><br/>
      タンカー1隻あたり +約 <span id="ins-cost">—</span> 万USD/航海<br/>
      <span style="font-size:0.63rem;">出典: <span id="ins-source">—</span></span><br/>
      <span style="font-size:0.60rem;color:#94a3b8;line-height:1.5;">
        ※危機ピーク（2026年3月上旬）は約2.5%<br/>
        ※船籍・積荷・旗国・航路により大幅に変動<br/>
        ※3月初旬は保険自体の引受停止が相次いだ局面あり<br/>
        ※出典: S&amp;P Global / Caixin Global (2026/03)
      </span>
    </div>
```

---

## commit メッセージ（Claude Codeに伝える）

```
fix: 戦争リスク保険料率を実績値に修正・但し書き追加 2026-05-15

- manual-update.json: war_risk_premium_pct 7.0→2.0（現状推定値）
- fetch_manual.py: Geminiプロンプト上限を7.5→2.5に修正（S&P Global実績ベース）
- index.html: Card4に但し書き追加（ピーク値・条件・出典）
```
