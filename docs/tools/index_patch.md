# index_patch.md — スマホ文字改善 & 出典・更新ログ折り畳み

> Claude Code への指示：以下の変更を `docs/index.html` に適用してください。
> **変更箇所以外は絶対に触らないこと。**
> 作業後に `git commit`（メッセージ: `ui: スマホ文字改善・出典ログ折り畳み`）してください。pushは確認後に指示します。

---

## [UI-A] スマホ文字サイズ・色 改善 — CSS追加

**対象：** `@media (max-width: 768px)` ブロックの閉じ括弧 `}` の直前

**old_str（最後の2行のみ — 一意マッチに使用）:**
```css
  .scenario-bar-bg { min-width: 15px; }
}
```

**new_str:**
```css
  .scenario-bar-bg { min-width: 15px; }

  /* ===== スマホ文字改善 2026-05-07 ===== */
  :root { --muted: #b8c5d6 !important; }

  .s-title {
    font-size: 0.95rem !important;
    line-height: 1.5 !important;
  }
  .s-body {
    font-size: 0.88rem !important;
    line-height: 1.65 !important;
    color: #c8d5e4 !important;
  }
  .s-src {
    font-size: 0.80rem !important;
    color: #9ab0c8 !important;
  }

  .sc-title {
    font-size: 0.93rem !important;
    line-height: 1.45 !important;
  }
  .sc-body,
  .sc-body p {
    font-size: 0.86rem !important;
    line-height: 1.65 !important;
    color: #c8d5e4 !important;
  }
  .sc-tag {
    font-size: 0.80rem !important;
  }

  .scenario-footer,
  .scenario-footer p,
  .scenario-footer li,
  .scenario-footer div {
    font-size: 0.86rem !important;
    line-height: 1.65 !important;
    color: #c8d5e4 !important;
  }
  .scenario-footer h3,
  .scenario-footer strong {
    font-size: 0.90rem !important;
  }
  /* ===== /スマホ文字改善 ===== */
}
```

---

## [UI-B] 出典・更新ログ → 統合 & 4件目以降折り畳み

### 手順 1: セクション構造を確認

`<!--出典・更新ログ-->` コメント以降の HTML を `view` コマンドで確認する。
以下の2ブロックを特定する:
- `🕐 最終更新＆主要出典` ブロック
- `📝 変更履歴` ブロック

### 手順 2: 統合ラッパー + 折り畳み実装

2ブロックを1つに統合し、最新3件を常時表示、4件目以降を折り畳みにする。
置換後の構造骨格：

```html
<!--出典・更新ログ-->
<section style="margin:20px 16px 10px;padding:14px 16px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:10px;">

  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;gap:8px;flex-wrap:wrap;">
    <h3 style="font-size:0.82rem;font-weight:700;color:#94a3b8;letter-spacing:0.06em;text-transform:uppercase;margin:0;">
      🕐 更新履歴 &amp; 主要出典
    </h3>
  </div>

  <!-- 常時表示: 最新3件 -->
  [最新3件のHTMLをここに配置]

  <!-- 折り畳みボタン（上） -->
  <div id="log-toggle-top" style="text-align:center;margin:8px 0 4px;">
    <button
      onclick="(function(){
        var c=document.getElementById('log-collapse');
        var t=document.getElementById('log-toggle-top');
        var b=document.getElementById('log-toggle-bottom');
        var isOpen=(c.style.display!=='none');
        if(isOpen){
          c.style.display='none';
          t.querySelector('button').textContent='📂 過去の履歴を見る';
          b.style.display='none';
        } else {
          c.style.display='block';
          t.querySelector('button').textContent='📂 閉じる';
          b.style.display='block';
          window.scrollBy({top:0,behavior:'smooth'});
        }
      })()"
      style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);
             color:#94a3b8;font-size:0.78rem;padding:6px 18px;border-radius:20px;
             cursor:pointer;transition:all 0.2s;"
      onmouseover="this.style.background='rgba(255,255,255,0.10)'"
      onmouseout="this.style.background='rgba(255,255,255,0.06)'">
      📂 過去の履歴を見る
    </button>
  </div>

  <!-- 折り畳み領域: 4件目以降（初期非表示） -->
  <div id="log-collapse" style="display:none;">

    [4件目以降のHTMLをここに配置]

    <div id="log-toggle-bottom" style="text-align:center;margin:8px 0 4px;display:none;">
      <button
        onclick="(function(){
          var c=document.getElementById('log-collapse');
          var t=document.getElementById('log-toggle-top');
          var b=document.getElementById('log-toggle-bottom');
          c.style.display='none';
          b.style.display='none';
          t.querySelector('button').textContent='📂 過去の履歴を見る';
          var btn=t.querySelector('button');
          var rect=btn.getBoundingClientRect();
          window.scrollBy({top:rect.top - 80, behavior:'smooth'});
        })()"
        style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);
               color:#94a3b8;font-size:0.78rem;padding:6px 18px;border-radius:20px;
               cursor:pointer;transition:all 0.2s;"
        onmouseover="this.style.background='rgba(255,255,255,0.10)'"
        onmouseout="this.style.background='rgba(255,255,255,0.06)'">
        ▲ 閉じる
      </button>
    </div>

  </div>

</section>
```

### 手順 3: 注意点

1. 「🕐 最終更新＆主要出典」と「📝 変更履歴」の2ブロックを1セクションに統合
2. セクションタイトルは「🕐 更新履歴 & 主要出典」に統一、「📝 変更履歴」見出しは削除
3. 日付が新しい順に並べ、先頭3件を常時表示、4件目以降を折り畳み領域に
4. 各エントリの内容・順番は変更しないこと
5. html { font-size: 18px } は絶対に変更しないこと

### 手順 4: 確認

- [ ] 最新3件が常時表示されているか
- [ ] 4件目以降が初期非表示か
- [ ] ボタンの展開・折り畳みが動作するか
- [ ] [UI-A] CSSが追加されているか
