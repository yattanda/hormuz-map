# index_html_diffs — 速報インシデント 下ボタンジャンプ修正 2026-05-06

> Claude Code への指示：以下の1箇所を docs/index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> 適用後は commit してください。push はユーザーの確認後に実施。

---

## [A] JS: applyIncidentFold の bottomBtn.onclick を修正

対象: function applyIncidentFold() 内の bottomBtn.onclick 部分のみ

変更前:
  bottomBtn.onclick = function() {
    collapse();
    // 折りたたんだ後、上ボタンが見える位置までスクロール
    topBtn.scrollIntoView({ behavior: 'smooth', block: 'center' });
  };

変更後:
  bottomBtn.onclick = function() {
    // collapse()のscrollBy補正は使わず、直接非表示にしてtopBtnへスクロール
    setExpanded(false);
    topBtn.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

---

## 確認ポイント（適用後）

- [ ] 下の「▲ 折りたたむ」を押したとき、上ボタンの位置にスムーズにスクロールするか
- [ ] 別の関係ない場所にジャンプしないか
- [ ] 上の「▲ 折りたたむ」は引き続きその場でジャンプなく動作するか
