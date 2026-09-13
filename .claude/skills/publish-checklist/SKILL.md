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

---

## ② 目視確認（機械では判定できないもの）

内容の妥当性・整合・重複は人が読むしかない。

- [ ] TICKER ― 本日の主要ニュースを反映しているか
- [ ] 30秒カラム「いま何が」― 最新の事実か
- [ ] 30秒カラム「海峡の今」― 最新の通過数・価格か
- [ ] ステータスバッジ ― 5枚が本日の事実を反映しているか
- [ ] 情勢カード3枚 ― 数値・出典が最新か
- [ ] COUNTDOWN ― フェーズラベルが現状と合っているか
- [ ] 速報インシデント ― 本日分が追加されているか
- [ ] シナリオ確率補足バナー ― 矢印・根拠テキストが最新か
- [ ] シナリオ4本 ― 内容が相互に矛盾していないか
- [ ] シナリオフッター ― 次の焦点が最新か
- [ ] **各カラム間で同じ文章を繰り返していないか**（機械では検出できない）
- [ ] ニュースの内容と出典の対応が正しいか（URL の生死は機械が見る）

---

全項目の確認後に `git commit` を実行する。
push・main へのマージはユーザーの指示を待ってから行う。
