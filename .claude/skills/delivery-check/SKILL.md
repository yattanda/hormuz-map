---
name: delivery-check
description: Check how fast chokepointlab.com is delivered, whether GitHub Pages is healthy when reached directly (speed and certificate), and switch the Cloudflare proxy on or off / 本番の配信の速さと、GitHub Pages を直接取ったときの状態（速さ・証明書）を確かめ、Cloudflare のプロキシを入れる・切る。「サイトが重い」「プロキシ無しに戻してよいか」「プロキシを入れる・切る」のときに使う
---

# 配信の確認と Cloudflare のプロキシの切り替え（2026-11-01〜）

このスキルは、本番 `chokepointlab.com` の表示が重いとき、Cloudflare のプロキシを入れるか切るかを決めるとき、
切り替えたあとに確かめるときに使う。設計と経緯は `hormuz-ops/drafts/design/cloudflare-proxy-plan.md`（private）、
11/1 の測定は `chokepointlab-notes/2026_11_01_二段表示PR-Aの計測/SUMMARY.md` §5。

## 1. 配信の確認（いつでも・読み取りだけ）

```bash
python tools/delivery_check.py
```

- `--quick` で /hormuz/ だけ（約30秒）。`--json 保存先.json` で結果を残す
- 測るのは3つ：
  1. **今の経路**：読者が実際に通る道（プロキシ有りなら Cloudflare 経由）
  2. **直接 GitHub Pages**：GitHub Pages の IP（185.199.108〜111.153）へ直接つなぐ。**プロキシ無しにしたときの姿**。プロキシ有りのあいだも、いつでも測れる。GitHub の証明書が有効か・残り日数も見る
  3. **比べる相手**：同じ HTML の raw.githubusercontent.com と、別の GitHub Pages のサイト。こちらの回線が遅くないかの確認
- 1ファイルの評価：良好（10KB 以上で 200,000B/秒以上・小さいファイルは2秒未満）／注意／不良（50,000B/秒未満・30秒で打ち切り・エラー）
- 判定（終了コード）：
  - **戻してよい（0）**：直接の経路がすべて良好・証明書が有効で残り14日以上・比べる相手も良好
  - **戻さない（1）**：直接の経路に不良か注意がある・証明書が通らない・残り14日未満
  - **保留（2）**：比べる相手も遅い（こちらの回線の問題の疑い）。時間をおいて測り直す
- 「戻してよい」は**時間をおいて2回以上**続いてから戻す（1回だけでは一時的なことがある）

### 1-1. 結果を貯めて、証拠の1ページを作る

```bash
python tools/delivery_check.py --history "C:/Users/yutay/Documents/chokepointlab-notes/配信の確認"
```

- 測った結果を `delivery-YYYYMMDD-HHMM.json` としてフォルダに足し、同じフォルダの **`report.html`**（1ファイル・外部の読み込みなし）を作り直す。ふつうはこちらで測る
- ページの中身：最新の回の結論（直接 GitHub Pages と比べる相手の速さ・「約N分の1」・判定）／3つの数字（今の経路・直接・比べる相手の中央値）／同じ大きさのページを取るのにかかった時間の横棒（30秒で打ち切り）／**測った回ごとの速さの推移**（対数の目盛り）／最新の回の内訳と回の一覧の表／測り方
- ページだけ作り直すとき：`python tools/delivery_report.py <フォルダ>`
- 貯める先は private の `chokepointlab-notes/配信の確認/`（測った回の JSON と `report.html` をそのままコミット・push する）。GitHub Support への問い合わせには `report.html` を添えるか、画面写真を貼る
- curl などで手で測った値も、同じ形の JSON に `"source"` を書いて置けば並ぶ（11/1 15:21〜16:11 の3回はこの形で入れてある）

## 2. プロキシの切り替え

### 2-1. 道具で（API トークンがあるとき）

```bash
python tools/cf_proxy.py status
```

```bash
python tools/cf_proxy.py off
```

```bash
python tools/cf_proxy.py off --yes
```

- `status`：apex の A 4件と www の CNAME が、オレンジ（プロキシ有り）か灰色（DNS only）か
- `on`／`off`：`--yes` が無いときは何をするかを表示するだけ。`off` は先に `delivery_check.py` を動かし、「戻してよい」でなければ止まる（`--force` で押し切れるが、使うのは運営者が決めたときだけ）
- 触るのは apex の A 4件と www の CNAME だけ。メール（MX・DKIM・SPF）・確認用の TXT・ほかのレコードは触らない
- トークンは環境変数 `CLOUDFLARE_API_TOKEN`。運営者が Cloudflare の「API トークン」で作る（権限は「ゾーン → DNS → 編集」、対象のゾーンは chokepointlab.com だけ）。**値をファイル・コミット・会話に書かない**。Claude はトークンを作らない・入力しない

### 2-2. 画面での切り替え（トークンが無いとき・運営者）

1. Cloudflare の画面 → chokepointlab.com → DNS → レコード
2. 名前が `chokepointlab.com` の A 4件と、`www` の CNAME の「プロキシ ステータス」を切り替える（オレンジ＝プロキシ有り／灰色＝DNS only）。5件とも同じにそろえる
3. 保存。5〜10分ほどで行き渡る
4. `python tools/delivery_check.py` で今の経路を確かめる

### 2-3. 初めてプロキシを入れるときだけの準備（運営者・画面）

オレンジにする前に、この順で（設計書 §3-1。2回目からは済んでいる）：

1. SSL/TLS → 暗号化モードを「フル」（「フレキシブル」は無限の転送になる。「フル（厳密）」は GitHub の証明書の更新が失敗したときに開かなくなる）
2. SSL/TLS → エッジ証明書：ユニバーサル証明書が有効か。「常に HTTPS を使用」をオン
3. Scrape Shield の「メールアドレスの難読化」をオフ。Rocket Loader はオフ。Bot Fight Mode はオフ
4. キャッシュルール：ホスト名が `chokepointlab.com` → キャッシュの対象にする・エッジとブラウザの TTL はオリジン（GitHub の `max-age=600`＝10分）に従う
5. `hormuz-map` の下書き PR（`?t=` を10分刻みに・`/privacy/` 第5章に Cloudflare）を、オレンジにする日にマージする

## 3. 切り替えたあとに見ること

- **オレンジにしたあと**：`delivery_check.py` の「今の経路」の server が `cloudflare`、2回目から `cf-cache-status: HIT`。良好になったか。`http://`・`www.`・旧 URL の転送、主要ページの 200（`python tools/validate_daily.py --check-urls`）
- **灰色に戻したあと**：「今の経路」が GitHub.com になり、良好のままか
- **プロキシ有りのあいだ**：週に1回と12月上旬に `delivery_check.py` で直接の経路の証明書の残り日数を見る（GitHub の証明書は 2026-12-17 まで。プロキシの下では更新が失敗することがある。残りが減り続けるなら、灰色に戻して更新させるかを運営者に相談する）
- 結果は STATUS の該当の行と、計測の控えに書く
