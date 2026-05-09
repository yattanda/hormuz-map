---
name: resolve-news-data-conflict
description: Step-by-step procedure to resolve news_data.json rebase conflicts / news_data.json の git rebase conflict を解決する手順書
disable-model-invocation: true
---

# news_data.json conflict 解決手順

このスキルは `git pull --rebase` 中に `docs/data/news_data.json` で conflict が発生したときのみ使用する。

---

## 発生パターン

`auto_push.py` がリモートに新しい JSON を push 済みの状態で、Claude Code がローカルに JSON の旧版 commit を持っている場合に `git pull --rebase` で conflict が起きる。

---

## ⚠️ 重要：--ours / --theirs は直感と逆になる

rebase 文脈での `--ours` / `--theirs` の意味は通常の merge と**逆**になるため、以下の手順を厳守する。

```sh
# NG（やってはいけない）
git checkout --theirs docs/data/news_data.json
# → rebase文脈では「ローカルの旧commit側」になるため、古い版で上書きしてしまう

# OK（正しい手順）
git checkout origin/main -- docs/data/news_data.json
# → リモートの最新版を明示的に取得する
```

---

## 正しい解決手順

```sh
# 1. conflict が発生していることを確認
git status

# 2. リモートの最新版を明示的に取得
git checkout origin/main -- docs/data/news_data.json

# 3. 正しい構造であることを確認（"title" フィールドが存在するか）
head -10 docs/data/news_data.json

# 4. ステージに追加して rebase を続行
git add docs/data/news_data.json
git rebase --continue
```

---

## 根拠

`auto_push.py` は GitHub API 経由でリモートに直接 push するため、リモート版が常に最新の正しい構造を持つ。ローカルの旧 commit を優先すると古い内容で上書きされる。
