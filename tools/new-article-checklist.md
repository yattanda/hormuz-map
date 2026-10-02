# 特別解説コラム 新規個別ページ追加手順

「特別解説コラム」に新しいコラムを追加し、同時に個別ページ（`docs/articles/`）としても
公開するときの手順。これに従えば毎回ゼロから構成を考える必要がない。

対象は「機雷除去とは」「代替ルート比較」等、危機終了後も検索され続ける
普遍テーマのコラムのみ。速報的なニュース（`news_data.json`側）は対象外。

## 0. スラッグを決める

- 英語・ハイフン区切り・内容を表す名詞句にする
- 例：`mine-clearance`、`saudi-pipeline-attack`、`route-c-alaska-oil`
- トグルID（`xxx-detail`）や日付を含めない

## 1. テンプレートをコピーする

```
tools/article-template.html を docs/articles/{slug}.html としてコピー
```

## 2. プレースホルダーを埋める

`{{ }}` で囲まれた箇所をすべて置換する。

| プレースホルダー | 内容 |
|---|---|
| `{{記事タイトル}}` | ページタイトル・OGP・構造化データで共通使用 |
| `{{140字程度の要約}}` | meta description / OGP description |
| `{{slug}}` | 手順0で決めたスラッグ |
| `{{YYYY-MM-DD（初出日）}}` | コラムを最初に書いた日 |
| `{{YYYY-MM-DD（最終更新日）}}` | 加筆・修正した日。加筆のたびに更新する |
| 本文セクション | 既存コラム本文をそのまま移設。書き換え・拡充は行わない |
| 関連コラムリンク | 既存の他コラムから2〜3件、関連性の高いものを選ぶ |

### 時事情報の扱い

コラム本文には「いつ・何が起きたか」という時系列的な事実が含まれることが多い。
個別ページ化後も内容を古びさせないため、時系列的な事実には
`<span class="at-the-time">（{{当時の日付}}時点の情報）</span>` のような注記を添える。
普遍的な解説部分（仕組み・構造の説明）には注記は不要。

本文そのものの書き換え・要約作成はユーザー側で行う場合がある。
Claude Codeが作業する場合も、内容の追加・脚色は行わず「移設＋時事注記の付与」に留める。

## 3. 記事一覧ページに追加する

`docs/articles/index.html` の一覧に新しいカードを追加する。

## 4. index.html側にリンクを追加する

`docs/index.html` の「特別解説コラム」セクション（`#special-commentary`）内、
該当カードに以下を追加する。

- カードは `<div class="commentary-grid">` の**直下**に、他のカードと同じ階層で置く
  （`</div><!-- /.commentary-grid -->` の前。別のカードの `</div>` の内側に入れない）。
  先頭の1枚が全幅、2枚目以降が格子（PC 3列・タブレット 2列・スマホ 1列）になる

- カード本文は要約（3〜5行程度、新しい主張やデータを加えない）
- カード末尾に「全文を読む」ボタンを設置し `articles/{slug}.html` へリンク
- **インライン style を書かない**（② PR4b-1・2026-10-01 からクラスで書く）。
  色は `col-card--{色}` で選ぶ：`red`・`amber`・`sky`・`green`・`orange`・`violet`。
  新しい色が要るときは `docs/index.html` の CSS「特別解説コラムのカード」に `--cc`（RGB）と `--cc-accent` の組を足す

```html
<!-- ○○コラムカード -->
<div class="col-card col-card--red">

  <!-- タイトル行 -->
  <div class="col-card-head">
    <span class="col-card-icon">💣</span>
    <div class="col-card-titles">
      <h3 class="col-card-title">記事タイトル</h3>
      <div class="col-card-sub">サブタイトル</div>
    </div>
    <span class="col-card-date">2026/04/12</span>
  </div>

  <!-- 要約 -->
  <p class="col-card-lead">
    要約（3〜5行）
  </p>

  <!-- 全文リンク -->
  <a href="articles/{slug}.html" class="col-card-link">
    📄 全文を読む
  </a>
</div><!-- /○○コラムカード -->
```

（色は既存カードの配色に合わせる）

### 4-2. 「30秒で全体像」内の特別解説ピルを追加する

`<div class="glance-special-links">` にピルを1つ足す。リンク先は記事ページ、日付は記事の
構造化データ（`datePublished` / `dateModified`）と同じ値にする。

```html
<a href="articles/{slug}.html" class="jump-pill jump-pill--{色}" data-published="YYYY-MM-DD" data-updated="YYYY-MM-DD">📄 短い見出し</a>
```

- 公開から30日間は「NEW」、それ以降は更新から30日間「◯月更新」の札が自動で付く（`applyColumnBadges()`）
- **既存コラムに加筆したときも**、記事の `dateModified` と一緒にピルの `data-updated` を書き換える。
  忘れると札が出ない（`tools/validate_daily.py` が食い違いを WARN で出す）
- 属性の順番（`href` → `class` → `data-published` → `data-updated`）は変えない。検証スクリプトがこの書式で検出している

## 5. sitemap.xmlに追加する

`docs/sitemap.xml` に以下のURLを追加する。

```xml
<url>
  <loc>https://chokepointlab.com/articles/{slug}.html</loc>
  <lastmod>{{YYYY-MM-DD}}</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.6</priority>
</url>
```

## 6. 公開前チェック

- [ ] `{{ }}` プレースホルダーの置換漏れがないか
- [ ] canonical URL・OGP URL・構造化データのURLが一致しているか
- [ ] パンくずのリンク先が正しいか
- [ ] `docs/articles/index.html` にカードを追加したか
- [ ] `docs/index.html` の該当カードに「全文を読む」リンクを追加したか
- [ ] `docs/sitemap.xml` に追加したか
- [ ] `/publish-checklist` の対象範囲であれば併せて実行する
