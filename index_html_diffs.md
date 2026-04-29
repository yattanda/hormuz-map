# index_html_diffs.md
# 更新日時: 2026年4月29日 JST
# 目的: 出光丸通過反映 / 42→41隻 / 船種別アイコン表示 / 通過済み行削除

---

## [C01] MAP・タンカー可視化 更新

### 変更1: SHIP_CONFIG の数値・日付更新

**検索文字列（完全一致）:**
```
const SHIP_CONFIG = {
  totalShips:    42,
  passableShips: 0,
  date:          '2026年4月8日',
  dateConfirmed: '2026年4月20日 7:31 JST確認：Touska拿捕・報復宣言により解消の見通しなし。推定40隻超が継続停留'
};
```

**置換後:**
```
const SHIP_CONFIG = {
  totalShips:    41,
  passableShips: 0,
  date:          '2026年4月29日',
  dateConfirmed: '2026年4月29日 JST確認：出光丸（出光タンカー運航・サウジ産原油200万bbl積載）が4月28日夜にホルムズ海峡を通過。41隻が引き続き湾内停留中。'
};
```

---

### 変更2: ship-grid のアイコン描画ロジックを船種別に変更

**検索文字列（完全一致）:**
```
    const grid = document.getElementById('ship-grid');
    grid.innerHTML = '';

    for (let i = 0; i < totalShips; i++) {
      const el        = document.createElement('span');
      const isPass    = (i < passableShips);
      el.className    = 'ship-icon' + (isPass ? ' passable' : '');
      el.textContent  = '🚢';
      el.title        = isPass
                          ? `#${i + 1}　通過済み ✅`
                          : `#${i + 1}　足止め中 🔴`;
      grid.appendChild(el);
    }
```

**置換後:**
```
    const grid = document.getElementById('ship-grid');
    grid.innerHTML = '';

    const SHIP_TYPES = [
      { icon: '🛢', count: 23, label: '石油系タンカー', color: 'rgba(251,191,36,0.9)'  },
      { icon: '🧊', count: 5,  label: 'LNG',           color: 'rgba(56,189,248,0.9)'   },
      { icon: '🚢', count: 13, label: 'その他',         color: 'rgba(248,113,113,0.8)'  },
    ];

    let idx = 0;
    SHIP_TYPES.forEach(function(type) {
      for (let i = 0; i < type.count; i++) {
        idx++;
        const el       = document.createElement('span');
        el.className   = 'ship-icon';
        el.textContent = type.icon;
        el.title       = `#${idx}　${type.label}　足止め中 🔴`;
        el.style.filter = `drop-shadow(0 0 3px ${type.color})`;
        grid.appendChild(el);
      }
    });
```

---

### 変更3: t-pass の更新処理を安全化（null チェック追加）

**検索文字列（完全一致）:**
```
    document.getElementById('t-stuck').textContent = stuck        + '隻';
    document.getElementById('t-pass' ).textContent = passableShips + '隻';
    document.getElementById('t-total').textContent = totalShips    + '隻';
```

**置換後:**
```
    document.getElementById('t-stuck').textContent = stuck     + '隻';
    document.getElementById('t-total').textContent = totalShips + '隻';
```

---

### 変更4: tanker-stats から「通過済み」行を削除し、船種別内訳を追加

**検索文字列（完全一致）:**
```
    <div class="stat-row">
      <span>足止め中</span>
      <span id="t-stuck">-</span>
    </div>
    <div class="stat-row pass">
      <span>通過済み</span>
      <span id="t-pass">-</span>
    </div>
    <div class="stat-row">
      <span>合計</span>
      <span id="t-total">-</span>
    </div>
```

**置換後:**
```
    <div class="stat-row">
      <span>足止め中</span>
      <span id="t-stuck">-</span>
    </div>
    <div class="stat-row" style="font-size:9px; color:#94a3b8; padding-left:8px; margin-top:4px; border-top:1px solid rgba(148,163,184,0.2); padding-top:5px;">
      <span>🛢 石油系タンカー</span>
      <span style="color:#fbbf24; font-weight:bold;">23隻</span>
    </div>
    <div class="stat-row" style="font-size:8px; color:#64748b; padding-left:16px;">
      <span>原油 11隻 ／ 製品 12隻</span>
      <span></span>
    </div>
    <div class="stat-row" style="font-size:9px; color:#94a3b8; padding-left:8px;">
      <span>🧊 LNG</span>
      <span style="color:#38bdf8; font-weight:bold;">5隻</span>
    </div>
    <div class="stat-row" style="font-size:9px; color:#94a3b8; padding-left:8px;">
      <span>⛽ LPG</span>
      <span style="color:#4ade80; font-weight:bold;">0隻</span>
    </div>
    <div class="stat-row" style="font-size:9px; color:#94a3b8; padding-left:8px; border-bottom:1px solid rgba(148,163,184,0.2); padding-bottom:5px; margin-bottom:2px;">
      <span>🚢 その他</span>
      <span style="color:#94a3b8; font-weight:bold;">13隻</span>
    </div>
    <div class="stat-row">
      <span>合計</span>
      <span id="t-total">-</span>
    </div>
```

---

### 変更5: ルートテーブル内「42隻」テキストを「41隻」に更新

**検索文字列（完全一致）:**
```
タンカー足止め42隻は解放待ち
```

**置換後:**
```
タンカー足止め41隻は解放待ち（4/28夜 出光丸通過・1隻減）
```

---

## 更新ログ追記

**`<!--出典・更新ログ-->` セクション内の既存最新ログエントリの直前に以下を追加:**

```html
<li><strong>2026年4月29日 JST</strong>：出光丸（出光タンカー）がホルムズ海峡を通過（4/28夜）。国交省発表42隻→41隻に更新。タンカーオーバーレイを船種別アイコン表示に刷新（🛢石油系23隻・🧊LNG5隻・🚢その他13隻）、通過済み表示を削除。出典：ロイター・国交省金子大臣会見（4/28）</li>
```
