# 課題7 記事のディレクトリ化 — 設計書

2026-10-12 起票。2026-10-19 にこの PR で `tools/` へ移した（それまではリポジトリ外の下書き）。
順番と位置の決定（2026-10-06）は、リポジトリ外の運用メモにある。
本番の HTML は、③ の観測明け（目安 10/19 頃）まで触らないことにしていた。

## 0. 何をするか

特別解説コラム5本と一覧を、いまの `/articles/<slug>.html` から、ディレクトリ形式の URL に移す。旧 URL には転送用のスタブを残す。

理由（リポジトリ外の運用メモ・課題7）：
- 同じ内容に複数の URL で届く（`/articles/mine-clearance.html` と、拡張子なしの `/articles/mine-clearance`。GitHub Pages が両方に同じファイルを返す。301 は使えない）
- ⑤ 特別レポート統合と ⑤' RSS は、記事の URL の形に依存する
- YouTube などから記事へ直リンクできるのは、URL が固まってから（§11-10 実施条件1）

## 1. 現状（2026-10-12 実測・`hormuz-map` `ab4d5bb`）

| もの | いま |
|---|---|
| 記事 | `docs/articles/<slug>.html` × 5（`mine-clearance`・`saudi-pipeline-attack`・`route-c-alaska-oil`・`oil-diversification-africa-brazil`・`oil-stockpile-monthly-trend`） |
| 一覧 | `docs/articles/index.html`（`/articles/`） |
| 共通の CSS | `docs/articles/_article.css`（記事から文書相対 `_article.css` で読む） |
| canonical・`og:url`・JSON-LD の `mainEntityOfPage` | どれも `https://chokepointlab.com/articles/<slug>.html` |
| sitemap | `/articles/` と記事5本（`.html` つき）の6行 |

書き換えが要る参照：

| 場所 | 数 | 形 |
|---|---|---|
| `docs/hormuz/index.html` | 10 | コラムのピル5（2031〜2035行）・カードの「全文を読む」5（4976行ほか）。`../articles/<slug>.html` |
| 記事どうし | 各3 | 「あわせて読む」。`<slug>.html` |
| 記事 → ほかのページ | 各3 | `../`（ホーム）・`../hormuz/#special-commentary` × 2 |
| `docs/index.html`（ハブ） | 1 | `articles/` |
| `docs/glossary/index.html` | 1 | `../articles/` |
| `docs/404.html` | 1 | `/articles/` |
| `docs/sitemap.xml` | 6 | |
| `tools/validate_daily.py` | 4か所 | 174・176行の正規表現（`\.\./articles/([\w-]+\.html)`）、801行（カードのリンク）、807行（一覧の読み込み）、1232行付近（記事と雛形を見る検査） |
| `tools/article-template.html` | 3 | canonical・`og:url`・`mainEntityOfPage` |
| `tools/new-article-checklist.md` | 多数 | 手順そのもの（コピー先・リンクの書き方・sitemap の行） |
| `tools/oil-stockpile-monthly-update.md` | 2 | 月次タスクの対象ファイルのパス |
| `CLAUDE.md` | 2 | 25行・189行 |
| **PC の月次タスクの定義（リポジトリ外）** | 1 | `oil-stockpile-monthly-column`。`docs/articles/oil-stockpile-monthly-trend.html` を書き換える。**次回は 11/4** |

参照がないと確かめたもの：`hormuz-data-`・`hormuz-crisis-report`・`docs/archive/`・`docs/infographic/`・`docs/assets/glossary.js`・`.github/workflows`・`apply_diffs.py`・`auto_push.py`（`docs/data/*.json` の `articles/` は外部の報道の URL）。
YouTube の概要欄など外部からの直リンクは、リンクの台帳（リポジトリ外）に記事あての行がない（実施条件1で、外部にはルート＋UTM だけを貼ってきたため）。

## 2. 決めること（運営者）

| # | 判断 | 推奨 | 理由 |
|---|---|---|---|
| N1 | URL の形 | **`/hormuz/articles/<slug>/`**、一覧は `/hormuz/articles/` | 上流の正規 URL 形式（リポジトリ外の運用メモ・「移行時に凍結」）どおり。5本ともホルムズ海峡危機の記事。もう1つの案 `/articles/<slug>/` は、テーマが増えたときに記事の置き場がテーマと合わなくなる |
| N2 | slug | 変えない | 変える理由がない。変えると転送の対応表が要る |
| N3 | 旧 URL のスタブ | 旧ファイル6つ（記事5＋一覧）を同じ場所にスタブとして残す。期限は設けない | GitHub Pages は 301 を出せない。スタブは `.html` つきと拡張子なしの両方の旧 URL に効く |
| N4 | 共通の CSS の置き場 | `/assets/css/article.css`（ルート相対） | 課題46 D2（共通 CSS 化）で `/assets/` にまとめる予定。ここで先にルート相対にしておけば、D2 でもう一度動かさずに済む |
| N5 | マージの日 | **11/4 の月次タスクが済んでから**（11/5 以降）、または 11/4 より十分前にマージして、PC の月次タスクの定義のパスを同じ日に直す | 月次タスクは記事のファイルを直接書き換える。パスが食い違ったまま 11/4 を迎えると、タスクが旧ファイル（スタブ）を書き換えるか、何もせずに終わる |
| N6 | 課題46（デザイン刷新）との順 | 課題7 を先にマージし、その観測期間に D2・D3 | 位置の決定（2026-10-06・10-12）どおり。記事の新しい見た目は D3 で入る |

N5 について：③ の観測明け（10/19 頃）からすぐ実装すれば、10/20 台の前半にマージできる。その場合は月次タスクの定義を同じ日に直す（運営者の PC での作業が1つ要る）。観測は約2週間なので、明けは 11月上旬になる。

**決定（運営者・2026-10-12）：N1〜N6 とも推奨どおり。**N5 は「10/20 台の前半にマージし、同じ日に PC の月次タスクの定義のパスを直す」。

## 2-1. 実装の状態（2026-10-12）

`hormuz-map` のローカルのブランチ `restructure/articles-directory` に実装した（`main` の `ab4d5bb` から3コミット。**push していない・PR も作っていない**）。PC の `hormuz-map` は `main` に戻してある。

| コミット | 内容 |
|---|---|
| `0a5b8a4` | 記事5本と一覧を `docs/hormuz/articles/` へ、CSS を `/assets/css/article.css` へ移し、参照を書き換え（`validate_daily.py` を含む） |
| `7fa6af5` | 旧 URL 6つにスタブ |
| `517165d` | 雛形・追加の手順・月次の手順・`CLAUDE.md` |

ローカルで確かめたこと（`python -m http.server` で `docs/` を配信）：
- 新 URL 6つと CSS が 200。記事と一覧の中のリンク・CSS・スクリプトに切れなし。canonical は6つとも新 URL
- 旧 URL `…/articles/mine-clearance.html?utm_source=test&utm_medium=x#section-y` が、クエリとアンカーを保ったまま新 URL へ移る
- `/hormuz/` の記事へのリンクは5種類とも新 URL で 200
- 375px 幅で横スクロールなし（一覧・記事2本）。コンソールエラーなし
- `validate_daily.py` は OK 74 / WARN 0 / NG 0（移す前と同じ）

確かめていないこと：
- 拡張子なしの旧 URL（`/articles/mine-clearance`）。ローカルのサーバーは GitHub Pages と違って拡張子を補わない。本番で確かめる
- JavaScript を切ったときの `meta refresh`

rebase と確認のやり直し（2026-10-19）：
- 10/19 の日次（PR #82・`43f85cc`）のあとに `main` へ rebase。衝突なし（分岐点の `ab4d5bb` 以降、日次は `docs/articles/` を触っていない）
- `validate_daily.py` は OK 74 / WARN 0 / NG 0
- ローカルで、新 URL 6つが 200・canonical は新 URL・記事の中のリンクと CSS に切れなし・`/hormuz/` のピルとカード5つが新 URL・sitemap は新 URL の6行だけ・旧 URL（クエリと #アンカーつき）が新 URL へ移る・375px 幅で横スクロールなし
- コンソールの2件（グラフの `<svg height="auto">`・`/favicon.ico` の 404）は、移す前からあるもの

マージまでにやること（観測明け・10/19 頃〜）：
1. その日の日次が `main` に入ったあと、ブランチを `main` に rebase する（日次は `docs/hormuz/index.html` を書き換えるが、ピルとカードの行は触らない。衝突したらその行だけ直す）
2. `validate_daily.py` とローカルの確認をやり直す
3. 運営者の指示で push → PR → マージ
4. 同じ日に：PC の月次タスクの定義のパスを `docs/hormuz/articles/oil-stockpile-monthly-trend/index.html` に（運営者）／Search Console で新 URL 6つの URL 検査と sitemap の送り直し／本番で §4 の確認
5. この設計書を `hormuz-map/tools/` へ移す（同じ PR に入れる）

## 3. 設計

### 3-1. ファイルの動かし方

```
docs/articles/<slug>.html        →  docs/hormuz/articles/<slug>/index.html   （git mv）
docs/articles/index.html         →  docs/hormuz/articles/index.html          （git mv）
docs/articles/_article.css       →  docs/assets/css/article.css              （git mv）
docs/articles/<slug>.html        ←  スタブを新しく置く（5つ）
docs/articles/index.html         ←  スタブを新しく置く
```

`git mv` で履歴を引き継ぎ、スタブは同じ PR の別コミットで足す。

### 3-2. スタブ（§11-10 実施条件2 と `s11-10-design.md` §5 のテンプレートどおり）

- `<head>` の冒頭で `location.replace(新URL + location.search + location.hash)`（クエリと `#アンカー` を引き継ぐ）
- 0秒の `meta refresh`（JavaScript が切られているとき用）
- 新 URL への `rel="canonical"`
- 本文に移転先へのリンク1行
- `noindex` は付けない
- GA4 のタグは入れない（転送だけのページを数えない）

### 3-3. 記事の中の書き換え

- canonical・`og:url`・JSON-LD（`mainEntityOfPage`、あれば `BreadcrumbList`）を新 URL に
- 文書相対のリンクは階層が変わるので、ルート相対に統一する：`/`（ホーム）・`/hormuz/#special-commentary`・`/hormuz/articles/<slug>/`
- CSS は `/assets/css/article.css`
- フォント・`glossary.js` はすでにルート相対（変更なし）

### 3-4. 記事への入口

- `/hormuz/` のピルとカード：`../articles/<slug>.html` → `articles/<slug>/`（`/hormuz/` からの文書相対。`CLAUDE.md` の「`/hormuz/` の中ではページ間のリンクは文書相対」に合わせる）
- ハブ・用語集・404：`/hormuz/articles/` へ
- sitemap：6行を新 URL に。旧 URL の行は消す（スタブは載せない）

### 3-5. 日次・月次の経路

- `validate_daily.py`：正規表現を `articles/([\w-]+)/` の形に。記事のファイルを開く所は `docs/hormuz/articles/<slug>/index.html` に。検査の件数（いま OK 74）が変わらないことを確かめる
- `article-template.html`・`new-article-checklist.md`・`oil-stockpile-monthly-update.md`・`CLAUDE.md`：新しいパスと URL に
- 日次スキル（`daily-site-update`）は記事のパスを名指ししていない（確認済み）。ピルとカードの `data-updated` の書き方は変わらない
- PC の月次タスクの定義：対象ファイルのパスを直す（運営者・N5）

### 3-6. PR の切り方

1つの PR にまとめる（途中の状態を本番に出さない）。コミットは、(1) `git mv` とパスの書き換え (2) スタブ (3) 検査と手順書、の順。
マージはその日の日次更新のあと。`hormuz-map` の push は運営者の指示で。

## 4. 確かめること

マージ前（ローカル）：
- 新 URL 6つが 200 で開き、CSS・フォント・用語集のツールチップが効く
- 旧 URL 12通り（`.html` つき6＋拡張子なし6）が新 URL へ移る。`?utm_source=x#y` を付けても、クエリとアンカーが残る
- 記事の中のリンク（ホーム・本編へ戻る・あわせて読む）が切れていない
- `/hormuz/` のピル5つとカード5つが新 URL を指す
- `validate_daily.py` が OK のまま（件数が変わらない）。記事の日付の突き合わせ（ピル・カード・一覧・記事）が通る
- 375px 幅で横スクロールが出ない

マージ後（本番）：
- 上と同じものを本番で
- Search Console：新 URL 6つを URL 検査にかけ、sitemap を送り直す
- 翌朝の日次が通る
- 約2週間の観測：旧 URL の表示が減り、新 URL が登録されるか（③ のときと同じ4項目。リポジトリ外の運用メモ）

## 5. 戻し方

PR を revert すれば元に戻る（スタブが消え、旧 URL に記事が戻る）。ただし新 URL が検索に登録されたあとで戻すと、新 URL が 404 になる。戻すなら観測の早い段階で。

## 6. 持ち越し（この PR ではやらない）

- 記事の見た目の刷新（課題46 D3）
- RSS（⑤'）
- `/infographic/`・`/archive/` を `/hormuz/` の下へ移すか（上流の形では `/<theme>/infographic/`・`/<theme>/updates/`）。URL の変更を重ねないため、別の回に判断する
