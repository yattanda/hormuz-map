---
name: publish-checklist
description: Pre-commit and pre-push checklist for daily updates / commit・push前の更新完了確認チェックリスト
disable-model-invocation: true
---

# 更新完了チェックリスト

commit・push 前に以下を1件ずつ目視確認すること。

---

## 必須確認項目

- [ ] TICKER ― 本日の主要ニュースを反映しているか
- [ ] 30秒カラム「いま何が」― 最新日付・最新事実か
- [ ] 30秒カラム「海峡の今」― 最新通過数・価格か
- [ ] ステータスバッジ ― 5枚が本日の事実を反映しているか
- [ ] 情勢カード3枚 ― 日付・数値・出典が最新か
- [ ] COUNTDOWN ― フェーズラベルが現状と合っているか
- [ ] 速報インシデント ― 本日分が追加されているか
- [ ] シナリオ確率補足バナー ― 日付・矢印・根拠テキストが最新か
- [ ] シナリオ4本 ― 内容が相互に矛盾していないか
- [ ] シナリオフッター ― 次の焦点が最新か
- [ ] news_data.json latest ― 4件が最新か
- [ ] news_data.json osint ― isLatest:true が1件のみか
- [ ] ヘッダー日時 ― 本日 JST 時刻になっているか
- [ ] 更新ログ ― 先頭行に本日分が追記されているか

---

全項目確認後に `git commit` を実行する。push はユーザーの指示を待ってから行う。
