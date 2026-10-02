---
name: publish-checklist
description: Pre-commit and pre-push checklist for daily updates / commit・push前の更新完了確認チェックリスト
disable-model-invocation: true
---

# 更新完了チェックリスト

commit 前に、①機械検証 → ②目視確認 の順で行う。

---

## ① 機械検証（先に通す）

```bash
python tools/validate_daily.py
```

- `NG 0` になるまで直す。**終了コードが 1 のまま commit しない**
- `WARN` は自動では落とさない。内容を読んで判断する
- ニュース URL の死活も確認する場合は `--check-urls` を付ける

ここで確認されるのは次のとおり。**以下は目視しなくてよい。**

- **基準日が実測の今日（JST）と一致するか**（未来日・2日以上前は NG／前日は WARN）
- 日付整合：`dateModified` / ヘッダー日時 / 速報バナー / 全ルート現況サマリー /
  `news_data.updated` / `update_log` 先頭 / `archive_timeline` 末尾
- `news_data.json` の `latest` 4件・必須フィールド・旧スキーマの混入
- `latest` と `osint` の `isLatest: true` が各1件
- `archive_timeline.json` の日付重複
- `sitemap.xml` の `/` の `lastmod` が基準日と一致／`/archive/` の `lastmod` が `archive_timeline` 末尾より古くない
- hormuz-data- の経緯（`data/context.json` の `timeline`）の最新日が実測の今日から5日超なら WARN（NG にはしない。読めなければ WARN「未確認」）
- ルート表の型（WARN）：インライン style（`<col>` を除く）・各行の「最新」（`p.route-latest`）が1件か・「最新」より新しい日付が行の中にないか・リード文 `sec-lead` の復活。
  各行の鮮度は「最新」の `<time datetime>` で判定
- シナリオ・更新履歴の型（WARN）：シナリオ（`<!-- SCENARIOS -->`〜`<!-- STATS -->`）のインライン style・更新履歴のインライン style（開閉の `display:none` を除く）・更新履歴の件数（常時表示3件・合計10件まで）（② PR4a）

---

## ② 目視確認（機械では判定できないもの）

内容の妥当性・整合・重複は人が読むしかない。

- [ ] TICKER ― 本日の主要ニュースを反映しているか
- [ ] 30秒カラム「いま何が」― 最新の事実か
- [ ] 30秒カラム「海峡の今」― 最新の通過数・価格か
- [ ] 30秒カラム「主な動き」― 3件が速報インシデントの先頭3件と同じ出来事・新しい順か
- [ ] ステータスバッジ ― 本日の事実を反映しているか
- [ ] COUNTDOWN ― 休止中（2026-10-01〜）。`<!-- COUNTDOWN -->` の下に表示用の HTML を足していないか
- [ ] 速報インシデント ― 本日分が追加されているか
- [ ] シナリオ確率補足バナー ― 矢印・根拠テキストが最新か
- [ ] シナリオ4本 ― 内容が相互に矛盾していないか
- [ ] シナリオフッター ― 次の焦点が最新か
- [ ] **各カラム間で同じ文章を繰り返していないか**（機械では検出できない）
- [ ] ニュースの内容と出典の対応が正しいか（URL の生死は機械が見る）

---

全項目の確認後に `git commit` を実行する。
push・main へのマージはユーザーの指示を待ってから行う。
