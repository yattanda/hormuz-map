---
name: feature-extension-plan
description: Planning guide for new features, mobile UI, responsive improvements / 新機能・スマホUI・レスポンシブ改善・構造変更の前に参照するガイド
---

# 機能拡張・UI 改善計画スキル

このスキルは新機能追加・スマホ UI 改善・レスポンシブ対応・構造変更を行う前に使用する。

---

## 参照必須ドキュメント

スマホ表示や CSS レイアウトを修正する場合は、必ず以下を参照する。

- [@docs/design-system.md](docs/design-system.md)
- [@docs/mobile-ui-rules.md](docs/mobile-ui-rules.md)

---

## 専門エージェントの使い分け

### mobile-ui-reviewer

スマホ表示の問題発見・レビューに使う。原則としてコード編集は行わない。

**使用タイミング：**

- スマホ表示がしっくりこないとき
- 余白が広すぎると感じるとき
- 文字サイズが不自然なとき
- 表やカードが読みにくいとき
- ファーストビューの情報密度を確認したいとき

### responsive-css-specialist

CSS 修正・レスポンシブ実装に使う。

**使用タイミング：**

- mobile-ui-reviewer のレビュー後
- CSS の具体修正が必要なとき
- table / grid / flex / clamp / media query を調整するとき

---

## スマホ表示修正の必須手順

1. まず `mobile-ui-reviewer` で問題点を整理する
2. いきなり編集しない
3. 原因となっている CSS/HTML を特定する
4. `responsive-css-specialist` で修正案を作る
5. 共通 CSS・デザイントークンで直せるものを優先する
6. ページ固有 CSS は最後の手段とする
7. 375px、390px、430px、768px で確認する前提で調整する
8. PC 表示への副作用を必ず説明する

---

## 新機能・構造変更の前確認事項

1. 変更対象セクションの HTML 識別子を明示する
2. 変更箇所以外に影響が波及しないか確認する
3. JavaScript との連携がある場合は JS 側の変更箇所も一覧化する
4. モバイル（375px）とPC（1024px以上）の両方で動作を確認する
5. `hormuz-data-` リポジトリとの fetch 連携に影響しないか確認する
