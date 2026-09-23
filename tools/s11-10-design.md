# ③ §11-10 設計書：媒体トップ（ハブ）新設と `/hormuz/` への移設

- 作成：2026-09-23（ゲート A・設計のみ。サイトは変えない）
- 実施：**ゲート C 成立後**（9/30 頃の Search Console 2回目の点検で判定。目安10月第2週。未成立なら1週ずつ延期）
- 正本：案C と実施条件1〜5 は `Memory.md`「§11-10 の実施条件」と上流の PROJECT_CONTEXT §4-6。本書はそれを実装に落とすもの
- 状態：**骨子（v1）**。§2 の「1興行」、§4 の相対パスの一覧、§8 の日次経路の修正内容は実施前に詰める

---

## 0. この設計書で決まったこと（2026-09-23 運営者判断）

| # | 論点 | 決定 | 理由 |
|---|---|---|---|
| D1 | ③ の PR で動かす URL | **トップだけ `/hormuz/` へ移す。** `/articles/`・`/infographic/`・`/archive/` は URL を変えない。記事のディレクトリ化（#7）は**別 PR** | 正本（実施条件3）どおり。ゲート C の判定対象 `/infographic/` を登録直後に動かさない。記事4本を2段転送（旧ドメインの 301 ＋スタブ）にしない。→ 作業順案 §126 の「#7 を ③ に含める」は正本と食い違っていたので、作業順案の方を直す |
| D2 | ハブの主要数値の更新方法 | **JS で既存の JSON から読む。** HTML には基準日付きの静的な値を予備として置く | 日次更新が書き換える場所を増やさない（日次差分・`apply_diffs.py`・スキルの修正が小さくて済む） |
| D3 | 「1興行」の単位 | **動画1本＝1興行** | 動画ごとに入口・見せ場・終点を決められ、GA4 の UTM キャンペーン名とも1対1で対応する |
| D4 | ハブの `<title>` | **当面は「ホルムズ」を残す** | ルートの検索評価は現在「ホルムズ海峡危機マップ」で得ている。中身が入れ替わっても検索語との対応を保つ |

---

## 1. URL の対応表

| 旧 | 新 | 転送 | 備考 |
|---|---|---|---|
| `/`（ホルムズ海峡危機マップ本体） | `/hormuz/` | **なし**（ルートはハブとして残る） | 本体は `git mv docs/index.html docs/hormuz/index.html` で履歴を残す |
| `/?focus=<キー>` | `/hormuz/?focus=<キー>` | ハブの `<head>` 冒頭の JS で転送（実施条件5） | §3 |
| `/#<id>`（旧トップ内のアンカー） | `/hormuz/#<id>` | **転送しない**（外部参照は0件・2026-09-23 棚卸し） | §3 の問い参照 |
| `/articles/`・`/articles/*.html` | 変更なし | — | #7 は別 PR |
| `/infographic/` | 変更なし | — | §6 の最終形（`/hormuz/infographic/`）は #7 と同じ回に検討 |
| `/archive/` | 変更なし | — | 同上（`/hormuz/updates/`） |
| 法務6枚 | 変更なし | — | `../`（ハブ）を指すリンクはそのまま。`/corrections/` だけ直す（§7） |

**リスク（受け入れる）**：ルートからの転送は設定しないため、`/hormuz/` は内部リンクと sitemap だけで評価を得る。
「評価の受け皿の中身が入れ替わる」懸念はゲート C を待っても消えない。D4（title にホルムズを残す）とハブから
`/hormuz/` への目立つ入口で緩和する（確度：中）。

---

## 2. ハブ（ルート `/`）の設計

### 2-1. 構成（案C）

1. 媒体の紹介（2〜3行）
2. **主要数値 3〜5個**（D2。JS で読む・予備の静的値に基準日）
3. 4海峡の地図（静的な画像か軽い SVG。Leaflet は読まない＝ハブを軽く保つ）
4. **`/hormuz/` への入口**（最も目立つ位置）
5. **「YouTube から来た方へ」枠**（§2-3）
6. 最新の解説・更新（`news_data.json` の `latest` から JS で数件）

### 2-2. 主要数値の候補（出典の JSON は実在を確認済み）

| 候補 | 出典 | 注意 |
|---|---|---|
| ホルムズ通航量（mb/d）・平常比 | `hormuz-data-/data/manual-update.json` の `hormuz_daily_flow_mbpd`・`flow_disruption_pct` | AI 推定。**「AI推定」ラベルと算出元を併記**（編集方針） |
| 通航隻数の推定 | 同 `ais_estimated_vessels` | 同上・`ais_confidence` を併記 |
| 最終更新 | `docs/data/news_data.json` の `updated` | — |
| 日本向け原油の代替ルート比率 | `hormuz-data-/data/oil-flow.json` | `updated` を基準日として表示 |

- どれを採るかは実装時に決める。**シナリオ確率はハブに出さない**（AI 推定で振れが大きく、ハブの顔にするには弱い）
- fetch 先は既存どおり `SITE_CONFIG.DASHBOARD_BASE`（`hormuz-data-`）。新しい外部送信先は増えない＝`/privacy/` の改訂は不要の見込み（実施時に再確認）

### 2-3. 「1興行」（D3：動画1本＝1興行）

1本ごとに次の4つを決め、UTM 台帳（chokepointlab-notes）に1行で記録する。

| 項目 | 内容 | 例（南鳥島 `RqGfMLI0KgA`） |
|---|---|---|
| 入口 | ハブの「YouTube から来た方へ」枠の1行 | 「南鳥島レアアース、回収の次は？」 |
| 見せ場 | `/hormuz/?focus=<キー>`（地図の印） | `minamitori` |
| 回遊先 | 関連する記事・図解（無ければ省略） | — |
| 計測 | GA4 の UTM キャンペーン名 | `20260922-rareearth` |

- 枠は**常に表示**し、新しい順に**最大3本**。4本目以降は外す（古い動画の導線は動画側のリンクで足りる）
- 枠のリンクは `<a href="/hormuz/?focus=<キー>">`。**`onclick="focusOn()"` は使わない**（ハブに地図が無いため）。UTM は付けない（流入元は着地時の UTM で記録済み）
- Shorts の概要欄は押せない（2026-09-23 確定）ので、実際の入口はチャンネルのリンク欄（ルート＋UTM）→ ハブの枠

### 2-4. `<title>`・メタ（§11-12(B)・D4）

| | ハブ `/` | `/hormuz/` |
|---|---|---|
| title | 例「チョークポイント・ラボ｜ホルムズ海峡など海の要衝の危機を追う」（**文言は実装前に運営者が確定**） | 現行「ホルムズ海峡危機マップ｜通航状況・代替ルート・市場波及」を引き継ぐ |
| canonical・og:url | `https://chokepointlab.com/` | `https://chokepointlab.com/hormuz/` |
| JSON-LD | `WebSite`＋`Organization` | 現行の `NewsArticle` の `url` を `/hormuz/` に。`BreadcrumbList` を追加 |
| GA4 タグ | **残す**（Search Console 旧プロパティの所有権確認に使用中・CLAUDE.md） | 入れる |
| `google-site-verification` | 残す（CLAUDE.md） | 入れない |

---

## 3. ハブの転送 JS（実施条件5）

```html
<head>
<meta charset="UTF-8">
<script>
  // ?focus=<キー> 付きのアクセスは、クエリとアンカーごと /hormuz/ へ送る（§11-10 実施条件5）
  if (new URLSearchParams(location.search).has('focus')) {
    location.replace('/hormuz/' + location.search + location.hash);
  }
</script>
<!-- この後に GA4 タグ -->
```

- **GA4 タグより前に置く**。転送されるアクセスでハブの page_view を計上しないため（二重計上の防止）
- 転送すると referrer（youtube.com）は失われる見込み（確度：中）。UTM が付いていれば流入元は GA4 に残る
- 問い（実施前に決める）：`#<旧トップの id>` 付きのアクセスも送るか。外部参照は0件なので**送らない**を推奨

---

## 4. `/hormuz/` 本体

- `git mv docs/index.html docs/hormuz/index.html`（履歴を残す）。ハブは新規の `docs/index.html`
- **相対パスの書き換え**（2026-09-23 実測・実施時に数え直す）
  - `href`/`src` の相対指定 21件：`articles/` 5・`images/` 4・`./`（`./infographic/` 等）3・`archive/` 2・`editorial/` 2・法務 5
  - `fetch()` の相対指定：`data/military.json`・`data/rio-indio.geojson`・`data/news_data.json` ほか変数経由のもの（gatun・alajuela 等）。`/data/countries.geojson` は既にルート相対
  - `openLightbox('images/…')` 2件
- **書き方の方針**：
  - ページ間のリンク（`<a href>`）は CLAUDE.md どおり**文書相対**（`../articles/…`）
  - 画像・データ（`src`・`fetch`・`openLightbox`）は**ルート相対**（`/images/…`・`/data/…`）。
    データと画像はハブと共有し `docs/data/`・`docs/images/` に置いたままにするため、階層に依存しない書き方にする
- `?focus=` の処理（`focusOn()`・4749行付近）と「YouTube から来た方へ」枠はそのまま動く（同じページ内）。
  枠は `/hormuz/` 側にも残すか、ハブだけにするかは実装時に決める

---

## 5. スタブ

D1 によりパスが消えるページは無いので、**③ ではスタブは作らない**。
（テンプレート：`location.replace`＋0秒 meta refresh＋canonical＋リンク1行・noindex なし。#7 の PR で使う）

---

## 6. サイト内リンクの書き換え

| 場所 | 現状 | ③ 後 |
|---|---|---|
| 記事5本・記事一覧の「本編へ戻る」「パンくず」 `../index.html#special-commentary` | 11件 | `../hormuz/#special-commentary` |
| 記事のパンくず「ホーム」 | `../index.html` 6件 | ハブ（`../`）のまま。文言は「ホーム」で整合 |
| `/archive/` の「トップへ」系 | `../index.html`・絶対 URL 各1 | 文言が「危機マップ」なら `/hormuz/`、「ホーム」ならハブ |
| `/infographic/` の「ホルムズ海峡危機マップに戻る」 | 1件 | `../hormuz/` |
| `docs/404.html` の「トップ（ホルムズ海峡危機マップ）」 | `/` | ハブと `/hormuz/` の2行に分ける |
| sitemap.xml | `/` のみ | `/` と `/hormuz/` の両方。`/hormuz/` の lastmod は日次で更新 |

---

## 7. 他リポジトリ・法務ページ（実施条件4）

- `hormuz-data-/index.html` の戻りリンク2か所（189・421行付近）→ `https://chokepointlab.com/hormuz/`。**同じ日に別コミット**（別リポジトリ）
- `/corrections/` の `href="../"`（ホルムズ海峡ダッシュボード 12か所）→ `../hormuz/`。**法務ページは1枚ずつ単独コミット**（CLAUDE.md）なので、③ の PR 内で独立したコミットにする
- `hormuz-crisis-report` の4か所（旧 `yattanda.github.io/hormuz-map/`）は ⑤ で直す（301 でハブに着くので実害は小さい）

---

## 8. 日次更新経路の修正（実施条件3）

`docs/index.html` を名指ししているファイル（2026-09-23 実測・`docs/` の外）：

- 機能に効くもの：`.github/scripts/apply_diffs.py`・`.github/workflows/mobile-update.yml`・`tools/validate_daily.py`（sitemap の `/` の lastmod 確認を含む）・`tools/updater.html`・`.claude/skills/daily-site-update/SKILL.md`・`.claude/skills/html-safe-edit/SKILL.md`・`tools/.claude/settings*.json`
- 文書：`CLAUDE.md`・`Memory.md`・`tools/index_html_diffs.md`・`tools/new-article-checklist.md`・`tools/migration-*.md`・`tools/oil-flow-redesign.md`・`tools/redesign-plan.md`
- **`tools/index_html_diffs.md` は移動・削除しない**（CLAUDE.md。参照先が3つある）。対象ファイルのパスだけを `docs/hormuz/index.html` に変える
- Claude.ai 側（プロジェクトナレッジ）とスマホ経路の差分生成ルールにも新しいパスを反映する。**ここが漏れると翌朝の日次更新が失敗する**
- 実施条件3：移設・ハブ・日次経路の修正は1つの PR。マージは**その日の日次更新の後**

---

## 9. PR・マージの手順

1. ブランチ `restructure/hub-and-hormuz`（名前は着手時に了承を得る）
2. コミットの単位：`git mv` → 相対パスの書き換え → ハブ新設 → 転送 JS → 日次経路 → サイト内リンク → sitemap → `/corrections/`（単独）→ 文書
3. 着手日に `git merge main`（日次更新が毎日入るため。着手から1〜2日で閉じる）
4. ローカル確認（GitHub Pages はブランチを表示できない）：`python -m http.server --directory docs` で `/`・`/hormuz/`・`/?focus=minamitori`・記事の戻りリンク・404
5. `/code-review <PR> --comment`
6. その日の日次更新の後にマージ（merge commit）
7. 本番確認（§10）→ `hormuz-data-` の戻りリンクを更新

---

## 10. 検証と観測

- 本番確認：`/` がハブ、`/hormuz/` が地図、`/?focus=minamitori&utm_source=youtube&utm_medium=video` が `/hormuz/` に着き UTM が GA4 に残る、記事の戻りリンク、404、sitemap
- 翌朝のスマホ経路の日次更新が `docs/hormuz/index.html` に当たること
- 約2週間の観測：Search Console で `/hormuz/` の登録・ルートの表示回数・「ホルムズ海峡」系の検索語の順位
- 戻し方：merge commit を revert（`/corrections/` と `hormuz-data-` は個別に戻す）

---

## 11. 未決（実施前に決める）

- ハブの title・description の文言（D4 の枠内で）
- 主要数値の最終的な3〜5個（§2-2）
- 4海峡の地図を画像にするか SVG にするか
- 「YouTube から来た方へ」枠を `/hormuz/` 側にも残すか
- `#<旧 id>` 付きアクセスの転送（推奨：しない）
