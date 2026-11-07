# 「現在の状態」の日付ログ（2026-09-18〜10-10）

> 2026-11-07 に `Memory.md` から原文のまま移した経緯の記録（設計書 `tools/claude-md-slim-design.md`）。
> **書かれている「現状」「次にやること」は当時のもの。**いまの位置は `chokepointlab-notes` の `STATUS.md`、仕組みの現状は `Memory.md` を見る。
> 追記はしない（新しい経緯は設計書・`tools/*.md` の実施記録に書く）。

## 現在の状態

- **公開中**: GitHub Pages で稼働中（独自ドメイン `https://chokepointlab.com/`）。日次更新を継続中
  - 【2026-09-18】独自ドメインへ移行完了（Custom domain 設定 `75bbdac` → ホスト名置換 `60b62a1`、Enforce HTTPS 有効）。
    旧 URL `https://yattanda.github.io/hormuz-map/` は新ドメインへ 301 転送。
    本番検証は基準値どおり（`tools/migration-baseline-2026-09-13.md` §8）
  - ダッシュボード（`hormuz-data-`）は `yattanda.github.io/hormuz-data-/` のまま。**本体とは別オリジンになった**
- **現フェーズ**: ~~基盤整備（法務ページ整備・独自ドメイン移行準備）~~
  → 【2026-09-18〜】**移行後の確認期間**。~~〜10/2頃・HTML の構造・パス・タイトルは変えない~~
  → 【2026-09-23 変更】**日付ではなくゲート A・B・C で区切る**（`tools/redesign-plan.md` §1「確認期間のゲート」）。
  A（9/23〜）パス・タイトル・メタを変えない作業／B（9/25〜26 頃の点検後）フェーズ1b の残り／
  C（9/30 頃の点検で判定）パスを変える再編。日常のコンテンツ更新は継続
  - 例外として、**フェーズ2のうち CSS だけの変更（2-a 文字サイズ・2-b 行の長さ・2-c カラム／ブレークポイント）は
    2026-09-18 に本番反映済み**（確認期間中に前倒し。`<style>` 内のみ。詳細は `tools/redesign-plan.md` §4「実施結果」）
  - ~~10/2 以降~~ → ゲート順：フェーズ2の HTML 側の残り（注記箱へのクラス付与・特別解説コラムの入れ子修正・インライン `font-size` のクラス化）
    → フェーズ1b の残り（セクション統合＋S03・S08.5）→ 再編（§11-10）→ 表示の統一（基準日・主要数値の静的化など）→ フェーズ3
  - 【2026-10-01】**第1層末尾の COUNTDOWN カラムを休止**（表示を外した。期限が 5/22 で切れたまま形骸化していたため）。
    日次更新では書かない。「リアルタイム表示」の再定義は 10/2 以降に設計し、実装は表示の統一と同じ回（`tools/redesign-plan.md` §9）。
    同日、フッターの「データソース」表記を実際の出典に合わせて書き換えた（利用不可メディアを含む初期の固定表記が残っていた）
  - 【2026-10-05】**再編（§11-10）を実施**（PR #48・merge commit `90d5670`）。ルート `/` は媒体トップ（ハブ・`docs/index.html`）、
    ホルムズ海峡危機マップの本体は `/hormuz/`（`docs/hormuz/index.html`）へ移した。**日次更新の対象は `docs/hormuz/index.html`**。
    ハブで日次が触るのは「危機マップの最終更新」（`id="hub-updated"`）の1か所だけ。`/?focus=<キー>` と `/#map` はハブの JS が `/hormuz/` へ送る。
    設計と実施記録は `tools/s11-10-design.md`（§12）。同日、本体ヘッダーの「危機N日目」の予備の数字を日次更新が毎回書き換える手順にした（`validate_daily.py` が WARN）。
  - 【2026-10-05】**用語集を公開**（PR #51・merge commit `78144f3`）。`/glossary/`（47語）、`/archive/` の日別カードと記事5本のツールチップ、
    アーカイブ検索の同義語（「米中央軍」で「CENTCOM」の日も当たる）。正本は `docs/data/glossary.json`、ページは `tools/build_glossary.py --write` が書き出す。
    共通部品は `docs/assets/glossary.js`（本文に用語のタグは書かない・日次の作業は増えない）。確認前の原稿と確認用の一覧は private の `hormuz-ops/drafts/`。
    「このサイト独自の用語」は札、一般の用語の中の「このサイトでは」は囲みで区別して出す。`/hormuz/` 本体へのツールチップは未実施（S4・再編の観測のあと）。
    同日、読者に見える「OSINT」をやめた：更新履歴には「現地メディア視点を更新」と書く（日次の手順・`validate_daily.py` が WARN）。日次アーカイブの過去の本文は書き換えず、
    「収録範囲について」に意味を1文足した。内部の名前（`osint-panel`・`news_data.json` の `osint`）はそのまま。設計と実施記録は `tools/glossary-search-design.md`（§11）。
    `hormuz-data-` の戻りリンク2か所も `/hormuz/` に変更。次は「表示の統一」（「リアルタイム表示」の実装を含む。決定は `tools/redesign-plan.md` §9）
  - 【2026-10-06】**②' 表示の統一に着手**（設計書 `tools/display-unify-design.md`。判断 K1〜K10 は同日決定・WTI のカードは変えない）。
    PR A「リアルタイム表示」を公開（PR #57・merge commit `42bb23f`）：**今後の予定日**は `docs/data/upcoming.json` に持ち、30秒カラムの「次の焦点」の直下に JS が出す
    （出典つきで日付が確定した予定だけ・日単位・過ぎたら出ない・0件なら行ごと出ない）。**最終更新からの経過**はヘッダーの日時の文字を JS が読んで計算し、
    36時間を超えたら日時の横に「（N時間前）」、72時間を超えたら注意書きを出す（ハブは経過だけ）。日次の作業順序 6 は「今後の予定日（該当があるときだけ）」。
    `<!-- COUNTDOWN -->` には何も書かない。残していた CSS（`.deadline`・`.dl-*`・`.cd-*`・`.annot-*`）は削除。残りは PR B（日時の一元化）・C（「—」「確認中」の整理）・D（推定のラベル）
  - 【2026-10-07】**②' PR B「日時の一元化」を公開**（PR #60・merge commit `cce10c3`・本番確認済み）。シナリオの注記（`sc-sync-note`）とフッターのラベルに**日付を書かなくなった**
    （確率の時点は JS が `manual-update.json` の `updated_at` を `#sc-sync-at` に入れる。日次の手数は2か所減）。地図の凡例の「最終更新：2026/04/13」は削除。
    `validate_daily.py` に `check_scenario_dates()`。日付の書式は3つに絞り、正本は `/content-style-guide`。ヘッダーの日時は `<time datetime>` にしていない。
    残りは PR C・D と `/editorial/` の暫定注記。記録は `tools/display-unify-design.md` §3-2-R
  - 【2026-10-08】**②' PR C「値と状態の表示」を公開**（PR #62・merge commit `0232fd2`・本番確認済み）。JS が値を入れる場所の初期値は「読み込み中…」（シナリオ確率は「…」）、
    取得できないときは「取得できず」／「取得できませんでした」（シナリオは注記も差し替える）。「内訳確認中」は JS が `SHIP_CONFIG.date` から「未公表（◯時点）」と出す。
    日本向けフローの「基準日：」は「対象月：」に。**日次はこれらの場所を触らない**（`validate_daily.py` の `check_state_labels()` が NG にする・OK 58）。記録は `tools/display-unify-design.md` §3-3-R
  - 【2026-10-09】**②' PR D「推定のラベル」を公開**（PR #64・merge commit `6a88c96`・本番確認済み）。ラベルに「推定」（`.label-estimate`・統計などからの試算）を1種足した。
    生成 AI が出した値は「AI推定」（`.label-ai`）。シナリオ4枚の確率のピルの直後とダッシュボードの見出しに「AI推定」、日本向けフローの列見出しと注記に「推定」。
    「隻/週」は VLCC 換算の必要隻数と注記。主要指標は「約40カ国」に直し時点と出典（4/2 の外相オンライン会合・AFP）を添えた。
    **日次はピル直後のラベルを消さない**（`check_estimate_labels()` が NG にする・OK 59）。記録は `tools/display-unify-design.md` §3-4-R
  - 【2026-10-09】**`/editorial/` 第3章の暫定注記を書き換え、②' 表示の統一（PR A〜D ＋注記）を終えた**（main `8582c90`・`/corrections/` に1件 `268c876`・本番確認済み）。
    生成 AI の推定値は通過量・通航船舶数・シナリオ確率と明記し、ラベル2種の説明を置いた。残るのは任意の PR E（設計書 §3-6）。記録は同 §3-5-R
  - 【2026-10-10】**①' 1本目：Leaflet 1.9.4 を自サイトから配信**（PR #65・merge commit `5a4f0c4`・本番確認済み）。置き場所は `docs/assets/vendor/leaflet-1.9.4/`、
    `/hormuz/` は `unpkg.com` に接続しなくなった。`validate_daily.py` の `check_selfhosted_assets()` が逆戻りを NG にする。
    `/privacy/` 第5章から unpkg.com の行を外した（`028effa`・最終更新 10/10）。Google Fonts の行はフォントの自前化（2本目）まで残る。記録は `tools/external-deps-design.md` §2-2-R・§2-4-R
  - 【2026-10-10】**①' 2本目：Noto Sans JP を自サイトから配信し、①' 外部依存の自前化を終えた**（PR #67・merge commit `1cc7187`・本番確認済み）。
    置き場所は `docs/assets/fonts/noto-sans-jp/`（woff2 372個・約8.49 MB・`@fontsource/noto-sans-jp` 5.3.0）。`/hormuz/`・記事6ファイル・記事の雛形は Google Fonts に接続しなくなった。
    `/privacy/` 第5章から Google Fonts の行も外した。**新しい記事は `tools/article-template.html` から作る**（Google Fonts の `<link>` が戻ると `validate_daily.py` が NG）。
    読むファイルは 75個 → 約165個に増え、キャッシュは10分（PSI は未取得）。記録は `tools/external-deps-design.md` §2-1-R
  - 【2026-10-10】**日次が運営者に確認を回さない形に改めた**（main `034da5c`）。UKMTO の警報の本文は `tools/fetch_ukmto.py`（公式の一覧ページが読む公開 API）で読む。
    前回の「未確認」「据え置き」は次の日次が最初に拾う（スキル 2.4）。原油終値の2出典目は1出典目の数値で検索する。報告の「確認してほしい点」は運営者にしか決められないことだけ。
    **クラウドからこの API に届くかは未確認**（10/11 朝の日次で分かる。届かなければスクリプトが終了コード 2 を返す）
- **並行して進行中**: ~~日次更新の Claude Code 主体化（2026-09-02 着手・フェーズ0〜2完了。旧経路はバックアップとして保持）~~
  → 移行は実質完了（フェーズ0〜2完了・クラウドセッションが主経路）。旧経路はバックアップとして保持（2026-09-14 決定）
