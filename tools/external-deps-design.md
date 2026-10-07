# ①' 外部依存の自前化 設計書 v1（2026-10-07）

対象：Google Fonts（Noto Sans JP）と Leaflet（unpkg.com）の読み込みを自サイトからの配信に替え、`/privacy/` 第5章を合わせて改訂する。
状態：**現状の調査と設計まで。実装はしていない。**運営者の判断事項 L1〜L5（§4）が決まってから着手する。

上流の決定（変えない）

- 設計ルール「外部サービスに依存する資産（画像・JS・フォント）は自前ホストへ寄せる」（`PROJECT_CONTEXT.md` §6）
- J5（2026-09-23）：Leaflet はいまは SRI のみ。自前ホストは ①'（フォントの自前化・③ の後）と同じ回
- 自前ホストの資産はルート相対パス（`/assets/...`）で置く（`10月以降の作業順_案.md`）
- `/privacy/` の改訂は外部送信先が変わるたびに必要。①' でまとめて1回で済ませる
- ②' の PR と並行させない（`STATUS.md`）

---

## 1. 現状（2026-10-07 調査）

### 1-1. 外部から読み込んでいるもの

| 読み込み先 | 何を | どのページ | ①' の対象か |
|---|---|---|---|
| `fonts.googleapis.com`・`fonts.gstatic.com` | Noto Sans JP（400・700・800） | `/hormuz/` と `/articles/` の6ファイル（索引を含む）の計7ファイル | **対象** |
| `unpkg.com` | Leaflet 1.9.4 の `leaflet.js`・`leaflet.css`（SRI つき） | `/hormuz/` だけ | **対象** |
| `googletagmanager.com` | GA4 | 全ページ | 対象外（解析そのもの。ハブのタグは Search Console の所有権確認に使用中） |
| `s3.tradingview.com` | 市場のウィジェット | `/hormuz/` | 対象外（外部サービスの埋め込み） |
| `basemaps.cartocdn.com` | 地図の背景タイル | `/hormuz/` | 対象外（J1 で別に判断） |
| `yattanda.github.io/hormuz-data-` | ダッシュボードの iframe と JSON | `/hormuz/` | 対象外（④ `data.` で扱う） |

- ハブ・法務ページ・用語集・アーカイブは Google Fonts を読み込んでいない（システムのフォントで表示）
- `countries.geojson`・`rio-indio.geojson` は自サイト（`/data/`）から読んでいる（自前化済み）

### 1-2. フォントの使われ方（本番で実測）

- `/hormuz/` は `* { font-family: 'Noto Sans JP', 'Hiragino Sans', 'Yu Gothic UI', sans-serif; }` で、ページのほぼ全体が Noto Sans JP
- 読み込まれたフォントの面：`/hormuz/` で 225（400・700・800 の3ウェイト）。記事 `mine-clearance.html` では `fonts.gstatic.com` などへのリクエストが 76件
- Google Fonts の CSS は `@font-face` が 372（1ウェイトあたり約124 の文字の区画 × 3）。ブラウザは、ページに出てくる文字を含む区画だけを取りに行く
- 2026-09-20 の計測では、トップで 80ファイル・2.26 MB（`tools/redesign-plan.md`）
- CSS には `font-weight` の 600・900 の指定もあるが、読み込んでいるのは 400・700・800 だけ（600 は 700、900 は 800 で描かれる）

### 1-3. Leaflet の使われ方

- `<head>` で `leaflet.css`・`leaflet.js` を unpkg.com から読む。SRI（`integrity`）つき
- 印は自前の HTML（`divIcon`）で、Leaflet 同梱の画像（`marker-icon.png` など）を使う指定は見つからなかった。
  ただし `leaflet.css` が `images/layers.png` などを相対パスで参照するので、自前に置くときは `images/` も一緒に置く

### 1-4. `/privacy/` 第5章の現在の記載（最終更新 2026-09-28）

外部サービスとして、Google Fonts・Google アナリティクス・TradingView・CARTO および OpenStreetMap・unpkg.com（Leaflet）・GitHub・Google フォームを挙げている。
①' のあとは、**Google Fonts と unpkg.com の2行が事実と合わなくなる。**

---

## 2. 設計

### 2-1. フォント（判断 L1）

| 案 | 中身 | 見た目 | 第三者への送信 | 手間・重さ |
|---|---|---|---|---|
| **(a) 区画に分かれたファイルをそのまま自前に置く** | Google Fonts と同じ分け方の woff2 を `/assets/fonts/noto-sans-jp/` に置き、`@font-face` を自前の CSS に書く | 変わらない | なくなる | ファイルが約370個・合計は数 MB の見込み（**未計測**）。取得元は SIL OFL 1.1 のフォントの配布物（例：npm の `@fontsource/noto-sans-jp`） |
| (b) ウェブフォントをやめ、システムのフォントで出す | `'Noto Sans JP'` の読み込みを外し、ハブと同じフォントの並びにする | **変わる**（iPhone はヒラギノ、Android は端末の Noto、Windows は游ゴシック） | なくなる | 最小。転送量が 2 MB ほど減る。ハブ・法務ページとは揃う |
| (c) (a) のうえでウェイトを減らす（800 → 700） | 3ウェイト → 2ウェイト | 見出しの太さが少し変わる | なくなる | ファイルが約250個に減る |

- **推奨は (a)。**理由：②' で表示を揃えた直後で、見た目を変える判断を同じ時期に重ねない。(b) は軽いが、見た目が端末ごとに変わる
- (b) の判断材料になる「閲覧者の端末の内訳」（GA4）は、このセッションでは見ていない（不明）
- 文字の区画を自分で作り直す方法（よく使う漢字だけを1ファイルにまとめる）は採らない。日次更新で新しい漢字が毎日出るため、欠けた文字だけ別のフォントで出るおそれがある

### 2-2. Leaflet（判断 L2）

- `leaflet.js`・`leaflet.css`・`images/`・ライセンス（BSD 2-Clause）を `/assets/vendor/leaflet-1.9.4/` に置く
- 取得した `leaflet.js`・`leaflet.css` のハッシュが、いま HTML に書いてある SRI の値と一致することを確かめてから置く（一致＝いま配信されているものと同じ中身）
- 自サイトから配信するので `integrity`・`crossorigin` は外す
- バージョンを上げるときは、ディレクトリ名ごと替える（キャッシュの取り違えを防ぐ）

### 2-3. 置き場所と書き方

- `/assets/fonts/noto-sans-jp/`（woff2 と `noto-sans-jp.css`）、`/assets/vendor/leaflet-1.9.4/`
- HTML からはルート相対（`/assets/...`）で読む。`<link rel="preconnect">` の2行（`fonts.googleapis.com`・`fonts.gstatic.com`）は外す
- `font-display: swap` はいまと同じにする
- フォントのライセンス（OFL.txt）を同じディレクトリに置く

### 2-4. `/privacy/` 第5章の改訂（判断 L4）

- 一覧から「Google LLC（Google Fonts）」と「unpkg.com（Leaflet）」の2行を外し、最終更新日を改訂日にする
- **順序：実装を本番に出してから、同じ日のうちに改訂する。**先に改訂すると、まだ接続しているのに「接続しない」と書くことになる
- 法務ページなので単独コミット。文面は案を出し、運営者が確定する
- `/corrections/` への記録は不要と考える（公開していた記述が誤っていたのではなく、実装を変えたため）。記録するかは L4 で確認する

### 2-5. PR の分け方（判断 L5）

| 順 | 中身 | 触るファイル | ブランチ名の案（作成前に了承を得る） |
|---|---|---|---|
| 1 | Leaflet の自前化 | `docs/hormuz/index.html` の `<head>` 2行・`docs/assets/vendor/` | `infra/selfhost-leaflet` |
| 2 | フォントの自前化 | `/hormuz/` と記事6ファイルの `<head>`・`docs/assets/fonts/` | `infra/selfhost-fonts` |
| 3 | `/privacy/` 第5章の改訂 | `docs/privacy/index.html` だけ | main に直接（単独コミット） |

- 1 と 2 を分けるのは、問題が出たときにどちらが原因かを分けるため（地図が出ない／文字が変わる、は別の症状）
- 記事ページの `<head>` は、新しい記事の雛形（`tools/new-article-checklist.md` が指すテンプレート）も同じ回に直す

---

## 3. 検証

1. 本番で、`fonts.googleapis.com`・`fonts.gstatic.com`・`unpkg.com` へのリクエストが 0 件（`/hormuz/` と記事1本）
2. 地図が出る・印を押すとポップアップが開く・凡例・地点ジャンプ・横方向のエンドレス（`tools/map-wraparound-design.md`）
3. 見た目：変更の前後でヘッダー・30秒カラム・ルート表・シナリオの画面写真を比べる（PC・スマホ幅）
4. 読み込まれたフォントのウェイトが 400・700・800 のまま
5. `validate_daily.py` が NG 0
6. PSI を取り直す（PC のターミナルで。環境変数 `PSI_API_KEY`）
7. コンソールエラー 0

---

## 4. 運営者に決めていただくこと

| # | 判断 | 選択肢 | 推奨 | 確度 |
|---|---|---|---|---|
| L1 | フォントをどうするか | (a) そのまま自前に置く／(b) ウェブフォントをやめる／(c) (a) のうえで 800 を 700 に寄せる | **(a)** | 中（(b) の材料になる端末の内訳を見ていない） |
| L2 | Leaflet を自前に置くか | (a) 置く／(b) SRI のまま据え置く | **(a)**（上流の設計ルールと J5 のとおり） | 高 |
| L3 | フォントのファイルを外部から取得してリポジトリに入れてよいか | (a) よい（取得元・ファイル数・合計の大きさを示してから取得する）／(b) 運営者が取得して渡す | **(a)** | 高 |
| L4 | `/privacy/` 第5章の文面と、`/corrections/` に記録するか | 文面は実装の PR のときに案を出す。記録は (a) しない／(b) する | **(a)** | 中 |
| L5 | PR を2本に分けるか | (a) 分ける（Leaflet → フォント）／(b) 1本にまとめる | **(a)** | 高 |

---

## 5. この設計で扱わないもの

- 地図タイル（CARTO）の切り替え（J1）
- TradingView のウィジェット、GA4
- `hormuz-data-` の読み込み先（④ `data.`）
- `font-weight` の 600・900 の指定の整理（見た目に関わるため、L1 が (c) になったときに一緒に見る）

## 6. 情報元

- 実測：このリポジトリの `docs/`（2026-10-07 時点の main）、本番 `https://chokepointlab.com/hormuz/`・`/articles/mine-clearance.html`（アプリ内ブラウザ）
- Google Fonts の CSS（`@font-face` の数）：`fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;800&display=swap` を取得して数えた
- 過去の計測：`tools/redesign-plan.md`（2026-09-20・09-23）
- 上流の決定：`chokepointlab-notes/10月以降の作業順_案.md`（J5 ほか）、`PROJECT_CONTEXT.md` §6
- 未確認：自前に置いたときのファイルの合計の大きさ、閲覧者の端末の内訳、記事の雛形の場所
