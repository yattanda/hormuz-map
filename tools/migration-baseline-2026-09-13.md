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

### 2026-09-13 追記：計測後に DNS と所有権確認を設定した

上の §7 は計測時点の記録として残す。同日中に次を設定し、公開 DNS（8.8.8.8 / 1.1.1.1）で実測した。

| レコード | 値 | 実測 |
|---|---|---|
| A `@` ×4 | `185.199.108.153` / `109` / `110` / `111` | ✅ 両 DNS で4件。GitHub の IP がそのまま返る＝**プロキシは DNS only** |
| CNAME `www` | `yattanda.github.io` | ✅ 別名として解決 |
| TXT `_github-pages-challenge-yattanda` | GitHub の確認値 | ✅ GitHub アカウントで **Verified** |
| TXT `@` `google-site-verification=…` | Search Console の確認値 | ✅ Cloudflare 連携で自動追加。**専用アカウント**で確認済み |
| MX ×3・TXT DKIM・TXT SPF | Email Routing（既存） | ✅ **無傷** |

Cloudflare の DNS レコードは全12件（MX 3・TXT 4・A 4・CNAME 1）。

- `http://chokepointlab.com` → **404「Site not found · GitHub Pages」**。
  DNS は GitHub まで届いており、どのリポジトリで配信するかが未設定という意味で**正常**
- GitHub Pages 設定（`gh api`）：公開元 `main` の `/docs`、`cname` なし、`https_enforced` true。
  **`yattanda.github.io` ユーザーサイトのリポジトリは存在しない**（他のプロジェクトサイトは移行の影響を受けない）
- Search Console（専用アカウント `chokepointlab@gmail.com`）：
  新ドメイン `chokepointlab.com`（Domain 型）と旧 URL `https://yattanda.github.io/hormuz-map/`
  （URL プレフィックス型・GA4 方式）の2件を登録

当日の手順は `tools/migration-runbook.md`。

---

## 8. 移行後の実測（2026-09-18）— 基準値との突き合わせ

移行コミット：Custom domain 設定（GitHub 自動 `75bbdac`）→ ホスト名置換 `60b62a1`（22ファイル・82箇所）。
HTTPS 証明書は Custom domain 設定の直後に発行済み（approved・期限 2026-12-17・`chokepointlab.com` / `www`）。Enforce HTTPS 有効。

| 基準値の節 | 移行後（`https://chokepointlab.com`） | 判定 |
|---|---|---|
| §1 | 18件すべて 200 | ✅ 一致 |
| §1 旧→新 301 | トップ・`/archive/`・`/articles/`・`/infographic/`・`/corrections/`・記事・`/sitemap.xml`・`/robots.txt` は `https://chokepointlab.com/...` へ直接 301 | ✅ |
| — | `http://` → `https://`、`www.` → apex がいずれも 301 | ✅ |
| §2 | 内部ファイル6件すべて 404 | ✅ 一致 |
| §3 横スクロール | `/` 1280px で 1265、375px で6ページとも 375 | ✅ 一致 |
| §3 コンソール | エラー 0件 | ✅ 一致 |
| §3 iframe 高さ同期 | PC 1476px／スマホ 2338px。暫定値（1110 / 2200 / 2110）ではない＝**postMessage 経由の同期が初めて動作** | ✅ |
| §4 | `<body>` 直下 41要素、Leaflet マーカー 80個 | ✅ 一致 |
| §5 | 15ページとも canonical / og:url が `https://chokepointlab.com/<path>` | ✅ |
| §6 | sitemap 15 URL すべて新ドメイン（旧ドメイン 0件）、robots.txt の Sitemap 行も新ドメイン | ✅ |
| 別リポジトリ | `yattanda.github.io/hormuz-data-/`・`/hormuz-crisis-report/` は 200 のまま | ✅ 影響なし |

**差が出た1件**：旧 URL `/hormuz-map/about/` のみ、転送先が `http://chokepointlab.com/about/`（http）。
そこから `https://` へもう一度 301 し、最終的に 200 で表示されるため読者への実害はない。
応答に `X-Cache: HIT` があり、Enforce HTTPS 有効化前の転送が GitHub の CDN キャッシュに残っていると考えられる（確度：中）。
クエリ付き（`?v=1`）でも同じだった。後日に再測する。

Search Console（新ドメインのプロパティ）：`https://chokepointlab.com/sitemap.xml` を送信 → **成功・検出 15**（2026-09-18 当日）。
旧 URL のプロパティでは 4/30 送信のまま「取得できませんでした」だった sitemap が、新ドメインでは初めて読み込まれた。
