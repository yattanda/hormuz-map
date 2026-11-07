---
paths:
  - "docs/index.html"
  - "docs/CNAME"
  - "docs/assets/css/hub.css"
  - "tools/build_hub_map.py"
---

# ハブ（`docs/index.html`）を触るときのルール

> 2026-11-07 にルートの `CLAUDE.md` から原文のまま移した（設計書 `tools/claude-md-slim-design.md`）。
> ルートには要点だけを残している。食い違ったら**この文書が正**。

## ハブの地図

- ハブの4海峡の地図は `tools/build_hub_map.py --write` が書き出す。目印 `<!-- hub-map:start -->`〜`<!-- hub-map:end -->` の間を手で編集しない

### 所有権確認のために消してはいけないもの（2026-09-13 追加）

- **`docs/index.html`（ハブ＝ルートのページ）の GA4 タグ（`gtag.js?id=G-T0KCXP29E5` の読み込みと `gtag('config', ...)`）は、
  Search Console の旧 URL プロパティの所有権確認に使っている。**削除しない・`<head>` の外へ動かさない。
  外すと確認が外れる（2026-09-13 に GA4 方式で確認したため）。`<head>` 冒頭の `?focus=` 転送 JS は GA4 タグより前に置いたままにする
- `docs/index.html`（ハブ）の `google-site-verification` メタは 2026-05-02 に**専用アカウント以外**で
  発行されたもので、現在の確認には使っていない。ただし発行元アカウントが不明なので当面は残す
- `docs/CNAME` はドメイン移行時に GitHub が自動でコミットする。**手で作成・編集・削除しない**
- ドメイン移行の当日手順は `tools/migration-runbook.md`、突き合わせる基準値は
  `tools/migration-baseline-2026-09-13.md`
