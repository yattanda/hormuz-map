# ドメイン移行 基準値（2026-09-13 実測）

`tools/redesign-plan.md` §1「凍結期間の定義 → 凍結中に取る基準値」に基づく実測記録。
**移行後（9/18頃）に同じ項目を測り、この値と突き合わせる。**
差が出た項目だけを調べれば、移行が壊したものを切り分けられる。

計測時点：`a8e6ae5`（フェーズ1b・§11-18 反映後、日次更新 `4df149f` 反映後）
**2026-09-13 追記**：計測後に移行前の是正3件（`b028d54` / `6a81ecf` / `d2432ce`）を入れたため、
影響を受けた §5・§6 の値を更新した。§1〜§4・§7 は計測時のまま。
計測方法：`curl` によるステータス取得と、ブラウザ実機での DOM 計測。

---

## 1. HTTP ステータス（旧ドメイン `https://yattanda.github.io/hormuz-map`）

| パス | 状態 |
|---|---|
| `/` | 200 |
| `/archive/` | 200 |
| `/infographic/` | 200 |
| `/articles/` | 200 |
| `/articles/mine-clearance.html` | 200 |
| `/articles/saudi-pipeline-attack.html` | 200 |
| `/articles/route-c-alaska-oil.html` | 200 |
| `/articles/oil-diversification-africa-brazil.html` | 200 |
| `/articles/oil-stockpile-monthly-trend.html` | 200 |
| `/about/` | 200 |
| `/editorial/` | 200 |
| `/disclaimer/` | 200 |
| `/contact/` | 200 |
| `/privacy/` | 200 |
| `/corrections/` | 200 |
| `/sitemap.xml` | 200 |
| `/robots.txt` | 200 |
| `/ogp.jpg` | 200 |

**移行後の確認**：新ドメインで同じ18件が 200 であること。あわせて
**旧 URL が新 URL へ 301 されること**（GitHub Pages がカスタムドメイン設定時に自動で行う）。

## 2. 404 のままであるべきパス（内部ファイル・§11-8 / §11-18 の結果）

`/tools/`・`/design-system.md`・`/mobile-ui-rules.md`・`/infographic/README.md`・
`/infographic/layer-test.html`・`/infographic/assets/final/README.txt`
→ 2026-09-12 時点で全件 404。**移行後も 404 であること。**

## 3. コンソールエラーと横スクロール

| ページ | 幅 | `scrollWidth` | コンソールエラー |
|---|---|---|---|
| `/` | 1280px | 1265 | 0件 |
| `/` | 375px | 375 | 0件 |
| `/about/` | 375px | 375 | 0件 |
| `/corrections/` | 375px | 375 | 0件 |
| `/articles/mine-clearance.html` | 375px | 375 | 0件 |
| `/archive/` | 375px | 375 | 0件 |
| `/infographic/` | 375px | 375 | 0件 |

`scrollWidth` が viewport 幅と等しい＝横スクロールなし。
トップの 1280px だけ 1265 なのは縦スクロールバー分（viewport 1280 − 15）。

**移行後に特に見るもの**：トップの埋め込みダッシュボード。移行すると
`chokepointlab.com` → `yattanda.github.io/hormuz-data-` が**別オリジンになる**ため、
`iframe.contentDocument` による高さ実測が例外になり、`postMessage`（`iframeHeight`）
経由へ切り替わる。両側に実装済み（`docs/index.html` の `fallbackHeight()` と
`hormuz-data-/index.html:1053`）だが、**実際に切り替わるのは移行が初めて**。

## 4. トップページの構造（フェーズ1b 後）

`<body>` 直下 **41要素**（38＋層ラベル3）。並びは
`tools/diffs-generation-rules.md`「HTML 上のセクション並び」を参照。
Leaflet はマーカー80個を描画。`#situation` / `#scenario` / `#japan-flow` は**空が正常**。

## 5. canonical / og:url の現在値（移行スクリプトの置換対象）

全15ページとも `https://yattanda.github.io/hormuz-map/<path>` の絶対URL。
~~`docs/archive/index.html` のみ `og:url` を持たない~~
→ **2026-09-13 に解消**（`d2432ce`）。OGP が丸ごと無かったため about と同じ7項目を追加した。

`tools/migrate-domain.sh` が置換するリテラルは `yattanda.github.io/hormuz-map`。
**22ファイル・82箇所**（2026-09-13 の B1〜B3 反映後。`git grep -c` で計測）。
除外により対象外：`CLAUDE.md`（説明文）と本ファイル（実測記録）。内訳の上位：
`docs/sitemap.xml` 14／`docs/index.html` 8／`tools/article-template.html` 5／
記事5枚 各5／`docs/infographic/index.html` 4／`docs/articles/index.html` 4。

置換されない自ドメイン外リンク（別リポジトリのため）：
`yattanda.github.io/hormuz-crisis-report` 3件（§11-11 で統合予定）、
`yattanda.github.io/hormuz-data-` 1件（`SITE_CONFIG.DASHBOARD_BASE`・§11-14 で `data.` へ）。

## 6. sitemap.xml / robots.txt

`sitemap.xml` は **15 URL**。`robots.txt` は `User-agent: * / Allow: /` と
`Sitemap: https://yattanda.github.io/hormuz-map/sitemap.xml` の1行。

~~既知の欠落：`/archive/` が sitemap に載っていない~~
→ **2026-09-13 に解消**（`6a81ecf`・14→15 URL）。

## 7. DNS（2026-09-13 実測・**未設定**）

- ネームサーバー：`zainab.ns.cloudflare.com` / `rajeev.ns.cloudflare.com`（Cloudflare 管理下）
- apex `chokepointlab.com` の **A レコードなし**
- `www.chokepointlab.com` は **NXDOMAIN**
- `https://chokepointlab.com` へ **接続不可**
- リポジトリに `docs/CNAME` は**存在しない**（手動作成しない方針どおり）

→ 移行手順（§6）のステップ1がまだ着手されていない状態。
