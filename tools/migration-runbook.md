# ドメイン移行 当日手順書（§11-13）

作成：2026-09-13。予定日：**2026-09-18（木）頃**。
移行先：`https://yattanda.github.io/hormuz-map/` → **`https://chokepointlab.com/`**

この手順書は `PROJECT_CONTEXT.md` §6「ドメイン移行手順（確定）」を、
2026-09-13 までに判明した事実で具体化したもの。**順序を入れ替えないこと。**
突き合わせに使う基準値は `tools/migration-baseline-2026-09-13.md`。

---

## 0. 前日までに済んでいること（2026-09-13 時点）

| 項目 | 状態 | 確認方法 |
|---|---|---|
| Cloudflare DNS：apex に A×4、`www` に CNAME | ✅ 9/13 設定 | 公開 DNS（8.8.8.8 / 1.1.1.1）で実測済み |
| Cloudflare のプロキシ | ✅ **DNS only（灰色）** | GitHub の IP（185.199.x）がそのまま返ることで確認 |
| GitHub アカウントでのドメイン所有権確認 | ✅ 9/13 Verified | TXT `_github-pages-challenge-yattanda` |
| Search Console 新ドメイン（Domain 型） | ✅ 9/13 | **専用アカウント**。TXT `google-site-verification`（Cloudflare 連携で自動追加） |
| Search Console 旧 URL（URL プレフィックス型） | ✅ 9/13 | **専用アカウント**。GA4 方式で確認 |
| 移行スクリプトの除外設定 | ✅ `b028d54` | 基準値ファイルと CLAUDE.md を置換対象外に |
| 基準値の採取 | ✅ `64e4133` / `c740024` | `tools/migration-baseline-2026-09-13.md` |
| `@chokepointlab` の本運用開始 | **移行の前提から外した**（2026-09-13） | 期限を撤回し「準備でき次第」に変更。移行当日には行わない（手順8） |

### GitHub Pages の現在設定（2026-09-13 `gh api` で実測）

- 公開元：`main` ブランチの `/docs`（ブランチ公開方式・legacy ビルド）
- `cname`：なし／`https_enforced`：true
- **`yattanda.github.io` というユーザーサイトのリポジトリは存在しない**
  → `hormuz-map` にカスタムドメインを設定しても、**`hormuz-data-` と
  `hormuz-crisis-report` は `yattanda.github.io` のまま動かない**
  （ダッシュボードの iframe と特別レポートへのリンクは切れない）

---

## 1. 当日の直前確認

**日次更新と時間をずらす。** 日次更新は `docs/index.html` を書き換えるため、
移行コミットと重なると競合する。**その日の日次更新が push された後**に始める。

```bash
cd ~/Documents/GitHub/hormuz-map
git pull
git status            # clean であること
```

- 凍結期間（9/15〜9/17）が破られていないか、`tools/redesign-plan.md`
  「凍結期間の定義 → 凍結を破る場合」の記録を確認する
- 公開 DNS で apex の A×4 と `www` が引けることを確認する（Cloudflare 側で誰かが変えていないか）

### 1-2. 移行直前の検索データの控え（2026-09-14 決定）

**手順3（Custom domain）より前に行う。** 301 転送が始まると、旧 URL の実績に移行後のデータが混ざり始めるため。

- Search Console（**専用アカウント**）で旧 URL プロパティ `https://yattanda.github.io/hormuz-map/` を開き、次をエクスポートする
  - 検索パフォーマンス（期間：過去16か月）
  - ページのインデックス登録
  - リンク
  - サイトマップ画面はスクリーンショットを撮る
- 保存先は**非公開の `chokepointlab-notes`** の `2026_9_18_検索データの控え/`（日付は当日に合わせる）。
  **検索データはこのリポジトリ（公開）に置かない**
- 前回（9/14）の控え `chokepointlab-notes/2026_9_14_検索データの控え/SUMMARY.md` と見比べ、差分を記録する

## 2. 移行スクリプトの dry-run（本番はまだ変えない）

```bash
bash tools/migrate-domain.sh --new-site chokepointlab.com
```

- 置換は `yattanda.github.io/hormuz-map` → `chokepointlab.com` のリテラル置換。
  `https://yattanda.github.io/hormuz-map/about/` が `https://chokepointlab.com/about/` になる
- 対象は **22ファイル前後・82箇所前後**（9/13 計測。日次更新で増減していれば実数を控える）
- 差分を目で見て、`//` の二重スラッシュや `chokepointlab.com/hormuz-map` のような
  **パスの取り残しが無いこと**を確認する
- 置換対象外が正しく外れていること：`CLAUDE.md`・`tools/migration-baseline-*.md`・
  `yattanda.github.io/hormuz-data-`（`SITE_CONFIG`）・`yattanda.github.io/hormuz-crisis-report`

> 注：2026-09-13 に Claude Code のセッションからこのスクリプトを実行しようとしたところ、
> 自動許可の判定で実行が止められた。当日は実行の許可を明示するか、ターミナルで自分で実行する。

## 3. GitHub でカスタムドメインを設定する（ここから本番が変わる）

1. `https://github.com/yattanda/hormuz-map` → **Settings** → 左メニュー **Pages**
2. **Custom domain** に `chokepointlab.com` → **Save**
3. 「DNS check successful」の表示を待つ

この操作で起きること：

- **GitHub が `docs/CNAME` を `main` に自動コミットする**（手で作らない・編集しない）
- **旧 URL から新ドメインへの 301 転送が即座に始まる**
- この時点では canonical・OGP・sitemap はまだ旧ドメインを指している。
  **手順5の push までを、なるべく間を空けずに進める**

## 4. HTTPS 証明書の発行を待つ

- Pages の設定画面で証明書の発行が進む。通常は数分〜1時間程度、長いと24時間程度かかることがある（確度：中）
- 発行が終わると **Enforce HTTPS** のチェックが入れられるようになるので、チェックする
- 発行前は `https://chokepointlab.com` が証明書エラーになることがある。異常ではない
- **Cloudflare のプロキシは DNS only（灰色）のまま。** オレンジにすると証明書が発行されない

## 5. ホスト名を置換してコミットする

```bash
git pull                                   # 手順3で GitHub が作った CNAME のコミットを取り込む
bash tools/migrate-domain.sh --new-site chokepointlab.com --apply
```

- 終了コード 0 と「旧文字列の残存はありません」を確認する
- `git diff` を確認し、**ホスト名置換だけの単独コミット**にする
  （CLAUDE.md「パス変更とホスト名置換を同一コミットに混ぜない」）
- push する

## 6. 本番検証（基準値と突き合わせる）

`tools/migration-baseline-2026-09-13.md` の各節と同じ項目を新ドメインで測る。

| 基準値の節 | 確認すること |
|---|---|
| §1 | 新ドメインで18件すべて 200 |
| §1 | **旧 URL → 新 URL の 301**：トップ・`/about/`・記事1本・`/sitemap.xml` を `curl -I` で |
| — | `http://` → `https://`、`www.` → apex の転送 |
| §2 | 内部ファイル6件と `/tools/` が 404 のまま |
| §3 | コンソールエラー 0、横スクロールなし（1280px / 375px） |
| §3 | **ダッシュボード iframe の高さ同期**。移行で別オリジンになり、`postMessage` 経由に切り替わる（初めての動作）。iframe の高さが暫定値（1110 / 2200 / 2110px）で固定されず、実寸に追随していること |
| §4 | `<body>` 直下 41要素、Leaflet のマーカー描画 |
| §5 | 全15ページの canonical / og:url が `https://chokepointlab.com/...` |
| §6 | `sitemap.xml` 15 URL が新ドメイン、`robots.txt` の Sitemap 行が新ドメイン |

## 7. 外部サービスの設定

- **Search Console**（専用アカウント）
  - 新ドメインのプロパティで `https://chokepointlab.com/sitemap.xml` を送信する
  - 旧 URL のプロパティは**削除しない**（旧 URL が検索結果から抜けていく推移を見る）
  - 「アドレス変更ツール」は、旧サイトがパス付き（`/hormuz-map/`）のため使えない見込み（確度：中）。301 転送で足りる
- **GA4**（専用アカウント）
  - 管理 → データストリーム → `hormuz-map` → 鉛筆アイコン → ストリーム URL を `https://chokepointlab.com` に変更
  - 測定 ID `G-T0KCXP29E5` は変わらないので、データは同じプロパティに届き続ける
- **X（任意・急がない）**
  - `@hormuz_map_jp` のプロフィールのウェブサイト欄を `https://chokepointlab.com` に変える。
    旧 URL のままでも 301 転送で新ドメインに届くので、当日でなくてよい
  - `@chokepointlab` への切り替え自体は**当日行わない**（手順8）

## 8. X（旧Twitter）の切り替え（§11-12(C)）— **移行当日には行わない**

**【2026-09-13 変更】期限を撤回した。** 2026-09-06 の決定（案ア）では「ドメイン移行と同時に
`@chokepointlab` へ切り替える」としていたが、`@chokepointlab` をすぐ運用するマンパワーが無く、
旧アカウントも手放しがたいため、**`@chokepointlab` の準備ができた時点で切り替える**ことにした。
9/18 の期限は「引っ越しと切り替えを一度に済ませれば説明が1回で済む」という好みの問題で、
技術的に必要なものではなかった（2026-09-06 の深刻度評価で確認済み）。

**切り替えるまでの状態**

- サイトの可視リンク：`@hormuz_map_jp` のまま（読者が空のアカウントに着地する経路は無い）
- メタ情報（`twitter:site` 15ページ・JSON-LD `sameAs`）：`@chokepointlab` のまま。**戻さない**
  （9/6 に「案イ」として不要と結論済み。戻すと同じ箇所を3回触り、凍結の定義にも反する）
- 記事の雛形の `twitter:site`：`@chokepointlab`（公開中のページに揃えた）
- **`@chokepointlab` に定期的にログインする。** 長期未使用で X に削除されると、
  メタ情報が存在しないアカウントを指す（残るリスクはこれだけ）

以下は、**切り替えを行う日**の手順。移行とは別日に行う。

### 前提：本運用開始の最低条件

「本運用開始」は記録上定義が無かったため、2026-09-13 に次を最低条件と定めた。
X 上の作業でサイトには触れないので、凍結期間中でも行ってよい（サイトのリンク差し替え 8-2 は凍結中は不可）。

| 条件 | 理由 |
|---|---|
| 表示名「チョークポイント・ラボ」、自己紹介文、アイコンが入っている | リンクから来た読者が媒体のアカウントだと分かるように |
| 2段階認証が有効 | 記録上の方針（作成直後に有効化） |
| **実投稿が数件ある** | 空のアカウントに読者を送らないため。9/6 にリンク差し替えを見送った理由そのもの |
| ウェブサイト欄は**まだ新ドメインにしない** | 移行前の `chokepointlab.com` は「Site not found」になる |

**条件を満たすまでは 8-1・8-2 を行わない。** メタ情報は既に `@chokepointlab` を指しているので、
待っても不整合は増えない。

### 8-1. `@chokepointlab` のウェブサイト欄

- ドメイン移行（手順6の本番検証と HTTPS 証明書の発行）が**済んでいること**を確認してから、
  ウェブサイト欄を `https://chokepointlab.com` にする
- 証明書の発行前に入れると、プロフィールから来た人が証明書エラーを見ることになる

### 8-2. サイトのリンク差し替え（独立コミット）

- 対象：`docs/index.html` の**ページ上部、30秒カードの上に右寄せで並ぶ**
  「𝕏 このマップの更新情報はXで発信中」のリンク
  - 記録（`PROJECT_CONTEXT.md` ほか）では「フッターの X リンク」と呼ばれているが、**実際はフッターではない**
  - 行番号は日次更新などでずれる（9/6 時点 1411行目 → 9/13 時点 1448行目）。当日は次で探す

```bash
grep -n 'x.com/hormuz_map_jp' docs/index.html
```

- `href` を `https://x.com/hormuz_map_jp` → `https://x.com/chokepointlab` に変える
- 文言「このマップの更新情報はXで発信中」と、隣の YouTube リンクは変えない
- **移行コミット（手順5）とも、日次更新とも別の独立コミットにする**
- メタ情報（`twitter:site` 15ページ・JSON-LD の `sameAs`）は 9/6 に `@chokepointlab` へ切り替え済みなので**触らない**
- push 後、本番でリンク先が `@chokepointlab` になっていることを確認する

2026-09-13 時点で、公開サイト（`docs/`）内の `hormuz_map_jp` の参照は**この1箇所だけ**
（`hormuz-data-`・`hormuz-crisis-report` にも参照は無い）。

### 8-3. 旧アカウント `@hormuz_map_jp` の扱い — **未決**（2026-09-13 時点）

フォロワーがいるのはこちら。どちらにするかは運営者が決める。

| 案 | 内容 | 当日の作業 |
|---|---|---|
| 併存 | ホルムズ専用の発信として続ける | 任意：新アカウントと新ドメインを紹介する投稿を1件 |
| 一本化 | 以後は `@chokepointlab` に移る | 移転の告知を投稿して固定表示／プロフィールに `@chokepointlab` と新ドメインを記載／以後の投稿を新アカウントへ |

**どちらの案でも守ること**

- **リネームしない。** 旧ハンドル `@hormuz_map_jp` が即座に第三者に取られる（記録上の方針）
- **削除しない。** 同じくハンドルが開放され、なりすましに使われうる
- **一本化した場合も定期的にログインする。** X は長期未使用のアカウントを削除する方針のため、
  放置すると結果的に削除と同じことになる

**決める期限**：なし。`@chokepointlab` への切り替えを行うときまでに決める。それまでは併存の状態。

**この決定に連動するもの**：`README.md` の `@hormuz_map_jp` 3箇所（4行目のバッジ・44行目・74行目）。
GitHub のリポジトリ紹介ページで、サイトではない。一本化するなら差し替え、併存なら残す。

### 8-4. 記録

- `PROJECT_CONTEXT.md`「X（旧Twitter）アカウント」節と §11-12(C)
- 旧アカウントの扱いを決めた場合は、その決定と理由

## 9. 記録

- `PROJECT_CONTEXT.md`（§11-13 完了、§6、DNS / ホスティング方針）
- 引き継ぎノート（`hormuz-ops/handovers/`）
- 基準値と差が出た項目があれば、その内容と対処

---

## 触ってはいけないもの

| 対象 | 理由 |
|---|---|
| Cloudflare の MX×3・TXT（DKIM `cf2024-1._domainkey`・SPF） | 問い合わせ用メール（Email Routing）が止まる |
| TXT `_github-pages-challenge-yattanda` | GitHub のドメイン所有権確認が外れる |
| apex の TXT `google-site-verification=bewJul…` | Search Console 新ドメインの所有権確認が外れる |
| `docs/index.html` の GA4 タグ（7行目 `gtag.js`・13行目 `config`） | Search Console 旧 URL の所有権確認が外れる（GA4 方式で確認しているため） |
| `docs/CNAME` | GitHub が管理する。手で作成・編集・削除しない |
| ワイルドカード DNS（`*.chokepointlab.com`） | 作らない。サブドメイン乗っ取り防止 |
| Cloudflare のプロキシ（オレンジ） | 証明書発行前は切り替えない |

## 切り戻し（重大な問題が出た場合）

1. 手順5の置換コミットを `git revert` して push（canonical 等を旧ドメインに戻す）
2. Settings → Pages → Custom domain を **Remove**（GitHub が `docs/CNAME` を削除するコミットを作る）→ `git pull`
3. DNS レコードと各所有権確認は**残してよい**（再挑戦時にそのまま使える）

注意：301 転送はブラウザや検索エンジンにキャッシュされるため、
切り戻しても**しばらく新ドメインへ飛ばされる読者が残る**ことがある。
切り戻しは「表示が壊れて読めない」ような重大な場合に限る。
