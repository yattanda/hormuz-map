# 将来の構成方針・§11-10 の実施条件・新テーマの土台

> 2026-11-07 に `Memory.md` から原文のまま移した経緯の記録（設計書 `tools/claude-md-slim-design.md`）。
> **書かれている「現状」「次にやること」は当時のもの。**いまの位置は `chokepointlab-notes` の `STATUS.md`、仕組みの現状は `Memory.md` を見る。
> 追記はしない（新しい経緯は設計書・`tools/*.md` の実施記録に書く）。

## 将来の構成方針 — 複数チョークポイント化とリポジトリ名（2026-09-21 記録）

### 決定事項（運営者の方針）

- 新しいリポジトリは作らず、**1ドメイン＝1サイトリポジトリ**に集約する
- チョークポイントは**サブディレクトリ**で分ける（例：`docs/taiwan/` → `chokepointlab.com/taiwan/`）
- 別のチョークポイントをメインに昇格させる時点で、リポジトリ名を `chokepointlab` 等へ変更する
- 既存ページの URL は極力変えない。移動する場合は旧 URL に meta refresh＋canonical の転送ページを置く
  （GitHub Pages では 301 を出せないため。Google は即時の meta refresh を恒久的な転送として扱う）
- 大改造・構造変更・リポジトリ名の変更は**ブランチ＋PR** で行う（CLAUDE.md「ブランチルール」、`d508a87`）

### ルートと `/hormuz/` の関係 — 2026-09-19 に確定済み（案C）

- **ルート `/` は媒体トップ（ハブ）にし、現在のトップの中身は `/hormuz/` へ移す。**
  ホルムズ以外は当面、地図内の付随情報にとどめ、テーマページは中身を継続して更新できるまで作らない
- 実施は §11-10（~~10/2 以降~~ → 2026-09-23 から**ゲート C 成立後**・設計はいまから並行。順序は GA4 全ページ展開〔済〕 → フェーズ2 HTML の残り → フェーズ1b の残り〔本体〕 → §11-10 → 表示の統一）。
  判断の理由・比較した案・受け入れたリスクは上流の戦略文書（§4-6）が正本
- 【訂正】2026-09-21 の初版（`6614451`）ではこの点を「未決・案A推奨」と書いていたが、
  9/19 の決定を確認しないまま書いた誤り。同日中に訂正した

### §11-10 の実施条件（2026-09-21 追加。案C は据え置き）

**設計書：`tools/s11-10-design.md`（2026-09-23 v1）。** D1 トップだけ移す（#7 は別 PR）／D2 ハブの数値は JS で既存 JSON から／D3 動画1本＝1興行／D4 ハブの title にホルムズを残す

1. **§11-10 が済むまで、YouTube 等の外部に貼るリンクはルート（`https://chokepointlab.com/`）＋UTM のみ。**
   ルートは移設後もハブとして同じ URL で残る。記事・`#アンカー` への直リンクは URL が固まってから
   - 理由：meta refresh の転送先は固定 URL のため、**クエリ（UTM）と `#アンカー` が落ちる**（確度：高）
2. **旧パスのスタブはクエリとアンカーを引き継ぐ形にする。**
   `location.replace(新URL + location.search + location.hash)` を基本に、0秒 meta refresh と canonical を併記
3. **PR の切り方**：ルートの `/hormuz/` への移設・ハブ新設・スタブ設置・日次更新経路の修正は**1つの PR にまとめる**
   （分けると途中でトップが空になるか日次更新が壊れる）。`docs/index.html` を名指ししている箇所は
   14ファイル（2026-09-21 実測：スキル・`apply_diffs.py`・`mobile-update.yml`・`validate_daily.py` 等）。
   マージはその日の日次更新の後。記事のディレクトリ化は別 PR。リポジトリ名（ホスト）の変更とは混ぜない
4. **他リポジトリ側の追従**：`hormuz-data-/index.html` の戻りリンク（2か所）を `https://chokepointlab.com/hormuz/` へ。
   `/corrections/` の `href="../"` は `../hormuz/` へ（注記済み）。他の法務ページ6枚の `../` はハブを指すのが正しいので据え置き
5. **（2026-09-22 追加）ハブは `?focus=` 付きのアクセスをクエリごと `/hormuz/` へ送る。**
   `location.replace('/hormuz/' + location.search + location.hash)` 相当。これが無いと、それまでに YouTube に貼った
   `https://chokepointlab.com/?focus=…` が地図に届かなくなる。トップの「YouTube から来た方へ」枠もハブへ引き継ぐ

### 実施時の注意（2026-09-21 実測）

- `docs/index.html` の GA4 タグは Search Console の所有権確認に使用中。**ルートに置くページの `<head>` に残す**（CLAUDE.md）
- `docs/CNAME` は公開元の `docs/` 直下に置いたまま動かさない
- リポジトリ名の変更で追従が要る箇所：
  - `auto_push.py:39`（`"repo": "hormuz-map"`）、`.env` の `GITHUB_REPO`
  - **`hormuz-data-/index.html` の189行目と421行目**：メインサイトへの戻りリンクが旧 URL `yattanda.github.io/hormuz-map/` のまま。
    今は 301 転送で届いているが、名前を変えると届かなくなる見込み（確度：中）。**名前の変更とは別に、先に `https://chokepointlab.com/` へ直しておくのが安全**
  - ローカルの接続先：`git remote set-url origin https://github.com/yattanda/<新名>.git`
  - ローカルのフォルダ名も変える場合、Claude Code のメモリと設定の保存先（フォルダのパスで決まる）が切り替わり、引き継がれない
- 名前の変更後の見込み：独自ドメインでの配信は継続（確度：中〜高）。旧 URL `yattanda.github.io/hormuz-map/` は転送されなくなる可能性（確度：中）。
  変更後に本番と旧 URL の両方を実測する。Search Console の旧 URL プロパティへの影響も確認する

### 新テーマの土台（先行して整備する）

- **GA4 は 2026-09-22 に `docs/` 配下の全15ページへ展開済み**（`b146be4`〜`f75f484`）。`hormuz-data-` は未設置（④ で判断）
  - `/privacy/` 第6章の設置範囲・最終更新日も同じ作業で改訂した（`b146be4`）
  - 確認期間中だが、`<head>` へのタグ追加は構造・パス・タイトルを変えないため実施した
  - **新しいページを作るときは、`<head>` の viewport の直後に同じ GA4 タグを入れる**（入れないと `/privacy/` の「すべてのページに設置」と食い違う）。
    記事は `tools/article-template.html` に入れてあるので、テンプレートからコピーすれば入る
- **UTM**：YouTube のスマホアプリからの流入は参照元が落ちて direct に紛れやすい（確度：中〜高）。
  概要欄のリンクには UTM を付ける。**命名規則は 2026-09-22 に決定**：
  `?utm_source=youtube&utm_medium=video&utm_campaign=<公開日YYYYMMDD>-<短い英語>&utm_content=<description|pinned_comment|community|channel_links>`
  （すべて小文字。サイト内リンクには付けない。台帳は上流の非公開ノート側）
- **`?focus=<キー>`（2026-09-22 実装、`ca84606`）**：トップの地図を指定の印へ寄せてポップアップを開く。UTM ではなく表示を決めるパラメータ。
  書く順は `?focus=<キー>&utm_…`。キーは小文字英字で、`docs/hormuz/index.html` の `FOCUS_TARGETS`（5-C）に定義する。ルートに `?focus=` 付きで来たアクセスはハブの JS が `/hormuz/` へ送る。
  現在のキー：`minamitori`（南鳥島）・`tsugaru`（津軽海峡）・`malacca`（マラッカ海峡）。キーを足したら、ハブの「YouTube から来た方へ」枠（`docs/index.html` の `#yt-visitors`）と台帳にも足す。
  `/hormuz/` 側の枠は 2026-10-24 に外した（K9・`tools/display-unify-design.md` §4。10/6〜10/23 の GA4 で、YouTube から `focus` なしで `/hormuz/` に着いたのは1件だけ）
  `#アンカー` を使わないのは、§11-10 実施条件1に反し、GA4 の page_location にも残らないため
- **地図の横方向エンドレス化（2026-10-06 公開・PR #55・merge commit `a815220`）**：地図に足した印（`L.marker`）・線（`L.polyline`）・面（`L.polygon`・GeoJSON）は、`map.on('layeradd')` のフックが経度 ±360° に自動で複製する（`docs/hormuz/index.html` の「1-B. WORLD WRAP」）。**印を足すときに手で複製を書かない。**
  中心経度は常に −180〜180° に戻る（ドラッグ中は Leaflet の `worldCopyJump`、それ以外は `moveend` の補正）。点の経度は −180〜180° で書き、180° 線をまたぐ線は連続した値（…170, 180, 190…）で書く。
  `moveend` と `zoomend` はドラッグ中・地図の置き直し時にも出るので、この2つに処理を足すときは何度呼ばれても結果が同じになるように書く。
  あとから `setPopupContent()` で文面を書き換える印を作るときは、コピー（`印._wrapCopies`）にも反映する。設計と検証は `tools/map-wraparound-design.md`（実施記録は §15）。
  開いているポップアップは、地図が動くたびに中心に近い側の印（元かコピー）の上へ置き直している（`keepPopupNear`）。座標が空の線・面は複製しない。
  PR 2（2026-10-06 公開・PR #56・merge commit `bb21bbc`。これで作業順の #45 は完了）：「地点へ移動」と「全体表示に戻す」は近い側へ飛ぶ（`flyToNearest`。地図を飛ばす処理を足すときは `map.flyTo` ではなくこれを使う）。
  最小ズームは地図の幅に合わせる（`fitMinZoom`。幅 1024px 以下は 2、PC の幅 1223px で 2.26。世界1周が地図の幅を下回らないので、同じ印が左右に2回見えない）
- **地図のスクリプトの位置（2026-10-22）**：`leaflet.js`・`basemap.js` は `<head>` では `<link rel="preload">` で取り寄せだけ始め、実行は本文の地図のスクリプト（MILITARY LAYER）の直前の `<script src>`。
  `<head>` で実行すると、上の欄（30秒カラム＝mobile の LCP）の表示がこの2つを待つ。**`L`・`HormuzBasemap` を使うコードは、この位置より下か `DOMContentLoaded` の後に書く**。
  `defer` にしなかったのは、地図のスクリプト（約1,800行）のトップレベルの関数を HTML の `onclick` が呼んでいて、包み直すと壊れるため
- **用語集のツールチップ（`/hormuz/`・2026-10-24）**：`</body>` の手前の「用語集」の `<script>` が、`load` の後に `/assets/glossary.js` を `data-lazy` 付きで読み込む
  （区域が画面の上下 300px 以内に入ったときに1回だけ印を付ける。まとめて付けると、ページ全体の配置の計算がやり直しになり mobile の TBT が増えるため）。
  区域は `data-zones` の6つ（`.glance-summary`・`.incident-item .incident-body`・`td.route-detail`・`.sc-body`・`.sc-update`・`.news-body`）で、日次スキルの型にある class だけを使う。
  **型の class を変えるときは `data-zones` も直す**。JS が後から描く区域（ニュース・30秒カラムの「今後の予定」）は、描いた直後に `Glossary.annotate()` を呼ぶ。日次スキル・`validate_daily.py` は変えていない
- **直リンク化**：リンク先となるアンカー（`id`）の棚卸しが必要
