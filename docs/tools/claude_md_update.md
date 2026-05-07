# CLAUDE.md 更新指示 — 2026-05-06

## 概要
以下の変更を `CLAUDE.md` に適用してください。
作業後に `git commit`（メッセージ: `docs: CLAUDE.md 追記・スリム化 2026-05-06`）してください。
**pushは確認後に指示します。**

---

## 【変更1】プロジェクト概要のスリム化（2行削除）

**old:**
```
## プロジェクト概要
- `docs/index.html` 1ファイルにHTML・CSS・JavaScript全て集約
- `docs/data/news_data.json` がニュース・OSINT表示の単一ソース
- `docs/images/` ディレクトリにインフォグラフィック画像を管理
- GitHub Pages で公開済み
- 更新頻度：毎日〜数日に1回
```

**new:**
```
## プロジェクト概要
- `docs/index.html` 1ファイルにHTML・CSS・JavaScript全て集約
- `docs/data/news_data.json` がニュース・OSINT表示の単一ソース
- `docs/images/` ディレクトリにインフォグラフィック画像を管理
- ※目標・URL・運用状況は `Memory.md` を参照
```

---

## 【変更2】運用方針のスリム化（Claude Code不要行を削除）

**old:**
```
## 運用方針
- Claude.ai Project：戦略・設計・情報収集・差分ファイル生成担当
- Claude Code：index.html更新・commit担当
- auto_push.py：news_data.json と index_html_diffs.md を
  DownloadsフォルダからGitHub APIで直接pushするスクリプト
  （hormuz-map/auto_push.py・hormuz-map/.envにトークン管理）
  ※ Downloads内に同名ファイルが複数存在する場合（例: news_data (1).json）、
     最終更新時刻が最新のものを自動選択し、古いものを自動削除する。
     手動でのファイル整理は不要。
- run.bat：auto_push.py をダブルクリック一発で実行するバッチファイル
  （cd + python auto_push.py + pause を自動実行）
- マネタイズ：現状は X 投稿によるインプレッション収益
- GenSpark：参照用アーカイブのみ（更新しない）
```

**new:**
```
## 運用方針
- Claude Code：index.html更新・commit担当（pushはユーザー確認後）
- auto_push.py：news_data.json と index_html_diffs.md を
  DownloadsフォルダからGitHub APIで直接pushするスクリプト
  （hormuz-map/auto_push.py・hormuz-map/.envにトークン管理）
  ※ Downloads内に同名ファイルが複数存在する場合（例: news_data (1).json）、
     最終更新時刻が最新のものを自動選択し、古いものを自動削除する。
     手動でのファイル整理は不要。
- run.bat：auto_push.py をダブルクリック一発で実行するバッチファイル
  （cd + python auto_push.py + pause を自動実行）
- GenSpark：参照用アーカイブのみ（更新しない）
- ※戦略・マネタイズ方針は `Memory.md` を参照
```

---

## 【変更3】新セクション4つを追記

`## 更新完了チェックリスト（毎回必ず確認）` の**直前**に以下を挿入してください。

**old（挿入位置の目印）:**
```
## 更新完了チェックリスト（毎回必ず確認）
```

**new（新セクション4つ＋元の見出し）:**
```
## Memory.mdとの役割分担
- `CLAUDE.md`（このファイル）：Claude Code向け **運用ルール・技術制約のみ**
- `Memory.md`：Claude.ai向け **引き継ぎ・現状・課題・完了履歴**
- 課題の優先度・進行状況・完了履歴は Memory.md に記載する
- CLAUDE.md には「何をすべきか（ルール）」のみ記載し、「現状・経緯」は書かない

## 折り畳み表示ルール（3件表示統一）
- **速報インシデント**：最新3件常時表示、4件目以降は「過去のインシデントを見る」で折り畳み
  - 上ボタン（3件目直後）：その場で折りたたむ（scrollBy補正でジャンプ抑制）
  - 下ボタン（展開末尾）：押すと上ボタン位置にスムーズスクロール
- **関連最新ニュース**：最新3件常時表示、4件目以降は「さらに見る」で折り畳み（scrollBy補正）
- **現地メディア視点**：LIMIT=3（3件表示）
- 折り畳み/展開時にページが飛ぶ場合は必ずscrollBy補正を入れること

## スマホフォントサイズ（変更禁止）
- `@media (max-width: 768px) { html { font-size: 18px } }` が設定済み
- この設定は削除・変更しない

## 既知の未解決問題（対応保留）
- **ルートテーブル スマホ右余白**：`<colgroup>` を変更するとテーブルが崩壊する
  → colgroup を触らない別アプローチで対応すること（現時点では保留）

## 更新完了チェックリスト（毎回必ず確認）
```

---

## 完了確認

変更適用後、以下を確認してからcommitしてください：
- [ ] `## プロジェクト概要` が3行＋注釈行になっているか
- [ ] `## 運用方針` から「Claude.ai Project」行と「マネタイズ」行が削除されているか
- [ ] 新セクション4つが `## 更新完了チェックリスト` の直前に存在するか
