---
paths:
  - "docs/data/glossary.json"
  - "docs/glossary/**"
  - "docs/assets/glossary.js"
  - "tools/build_glossary.py"
  - "tools/glossary-search-design.md"
---

# 用語集のルール

> 2026-11-07 にルートの `CLAUDE.md` から原文のまま移した（設計書 `tools/claude-md-slim-design.md`）。
> ルートには要点だけを残している。食い違ったら**この文書が正**。

- `docs/data/glossary.json` が用語集の正本（ツールチップ・`/glossary/`・アーカイブ検索の同義語が同じデータを使う。設計書 `tools/glossary-search-design.md`）
  - 載せるのは運営者が確認した定義文だけ。確認前の原稿は private リポジトリ `hormuz-ops` の `drafts/` に置く
  - 用語集ページ `docs/glossary/index.html` は `tools/build_glossary.py --write` が書き出す。目印 `<!-- glossary:start -->`〜`<!-- glossary:end -->`・`<!-- glossary-jsonld:start -->`〜`<!-- glossary-jsonld:end -->` の間を手で編集しない。JSON を直したら同じコミットでページも書き出す
- 本文に用語のタグを手で書かないこと・`/hormuz/` の中のリンクの書き方は、本体や記事にも効くためルートの `CLAUDE.md` に置いている
- `docs/data/news_data.json` がニュース・OSINT表示の単一ソース
