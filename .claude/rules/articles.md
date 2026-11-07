---
paths:
  - "docs/hormuz/articles/**"
  - "docs/articles/**"
  - "tools/new-article-checklist.md"
  - "tools/article-template.html"
---

# 特別解説コラムのルール

> 2026-11-07 にルートの `CLAUDE.md` から原文のまま移した（設計書 `tools/claude-md-slim-design.md`）。
> ルートには要点だけを残している。食い違ったら**この文書が正**。

## 特別解説コラムの個別ページ化

- 「特別解説コラム」の各コラムは `docs/hormuz/articles/{slug}/index.html` として個別ページ化されている（URL は `/hormuz/articles/{slug}/`。一覧：`docs/hormuz/articles/index.html`）。旧 URL の `docs/articles/*.html` は転送用のスタブで、中身を書き換えない
- `docs/hormuz/index.html` 側の各カードは要約＋「全文を読む」リンクのみを表示し、本文全文は個別ページ側が正とする
- 新規コラムを追加する場合は `tools/new-article-checklist.md` の手順に従うこと
