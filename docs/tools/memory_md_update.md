# Memory.md 更新指示 — 2026-05-08（iframeスマホ空白 調査記録）

## 概要
`Memory.md` の「hormuz-data- フッター余白・スマホ空白」セクションを更新する。
作業後 `git commit`（メッセージ: `docs: Memory.md 更新 2026-05-08 iframe空白調査記録`）。
**pushは確認後に指示します。**

---

## 【変更1】最終更新日付を更新

### str_replace

old_str:
```
最終更新: 2026-05-07（本日作業反映済み）
```

new_str:
```
最終更新: 2026-05-08（本日作業反映済み）
```

---

## 【変更2】「hormuz-data- フッター余白・スマホ空白」セクションを丸ごと置換

### str_replace

old_str:
```
#### 2. hormuz-data- フッター余白・スマホ空白（未解決・対応保留）
- **現状**:
  - デスクトップ: `min-height:100vh` 削除後にfooterが半行分クリップされる
  - スマホ: フッター付近に約10行分の空白が残る（`min-height` 削除前から存在）
- **診断状況**: コードのみでは原因特定できず。実機確認が必要
  - footer CSSには `padding:16px 20px; margin-top:10px; line-height:1.8` が設定済み
  - スマホ空白の原因候補: grid/card-footerのパディング累積、JS生成ルート行の高さ、iOSセーフエリア等
- **次回の対応案**:
  - デスクトップ: `footer` に `padding-bottom:24px` または `body` に `padding-bottom:8px` を追加
  - スマホ: ブラウザのDevToolsで実測してから対応。`@media(max-width:768px)` に `footer { padding-bottom:8px; margin-top:4px; }` を試す
```

new_str:
```
#### 2. hormuz-data- iframe 空白問題（⏸️ 保留中・根本解決待ち）

**症状**:
- PC: iframeコンテンツ終端〜USOILウィジェットの間に大きな黒い空白
- スマホ: さらに深刻で、実機ではF12シミュレーションの約2倍の空白が発生

**根本原因**:
- `adjustIframeHeight()` がスマホで `2200px` 固定を設定しているが、
  実際のiframeコンテンツ高さが環境・DPRにより可変のため、常にずれが生じる
- 固定値で合わせようとすると「大きすぎて空白」か「小さすぎてコンテンツが切れる」の繰り返しになる

**2026-05-08 試行記録**（固定値アプローチ・失敗）:

| バージョン | スマホ(≤480px) | PC | 結果 |
|---|---|---|---|
| 元の値 | 2200px | 1000px | 空白が巨大 |
| v1 | 1200px | 800px | コンテンツが切れた |
| v2 | 1500px | 800px | まだ切れた |
| v3 | 1700px | 950px | PCほぼ完成、スマホまだ切れた |
| v4 | 1900px | 950px | もう少し切れていた |
| v5 | 2110px | 1110px | pullで元の値に戻り失敗 ← ここで保留 |

**失敗の構造**:
- pullにより `adjustIframeHeight()` の値がリポジトリの元の値（2200px/1000px）に戻る
- 固定値の手動チューニングは恒久解決にならない

**次回の対応方針（保留中）**:
- **アプローチA（推奨・低リスク）**: `hormuz-data-` 側の `body/html` の `min-height` を確認・削除し、
  実コンテンツ高さを小さくする → その上でフォールバック値を設定
- **アプローチB（根本解決・中リスク）**: postMessageによる動的サイジング
  - 過去に試みたが真っ黒になりリバート済み
  - 次回は `hormuz-data-` 側の `body/html min-height` 削除を先に行ってから再挑戦
- **前提確認事項**: `hormuz-data-` の `index.html` で `body { min-height: 100vh; }` 等の設定がないか確認すること

**現在のリポジトリ値**（元に戻っている状態）:
```javascript
if (window.innerWidth <= 480) {
  iframe.style.height = '2200px';   // ← 空白が大きい
} else if (window.innerWidth <= 768) {
  iframe.style.height = '2300px';
} else {
  iframe.style.height = '1000px';   // ← クリップが発生
}
```
```

---

## 完了確認

変更適用後、以下を確認してからcommitしてください：
- [ ] 最終更新日付が `2026-05-08` になっているか
- [ ] 「2. hormuz-data- フッター余白・スマホ空白」セクションが新しい内容に置き換わっているか
- [ ] 試行記録テーブル・失敗の構造・次回方針が含まれているか
