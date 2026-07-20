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
docs/tools/article-template.html を docs/articles/{slug}.html としてコピー
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

- カード本文は要約（3〜5行程度、新しい主張やデータを加えない）
- カード末尾に「全文を読む」ボタンを設置し `articles/{slug}.html` へリンク

```html
<a href="articles/{slug}.html"
  style="display:block;margin-top:12px;width:100%;text-align:center;
  background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);
  border-radius:6px;color:#f87171;font-size:0.78rem;font-weight:700;
  padding:9px 0;text-decoration:none;letter-spacing:0.03em;">
  📄 全文を読む
</a>
```

（色は既存カードの配色に合わせる）

## 5. sitemap.xmlに追加する

`docs/sitemap.xml` に以下のURLを追加する。

```xml
<url>
  <loc>https://yattanda.github.io/hormuz-map/articles/{slug}.html</loc>
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
