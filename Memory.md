# Memory.md — ホルムズ海峡危機マップ 技術・実装の索引

最終更新: 2026-11-07（索引型に改めた。経緯は原文のまま `tools/history/` へ移した。設計書 `tools/claude-md-slim-design.md`）

- **この文書に書くもの**：サイトの仕組み（どの機能がどのファイル・データで動くか）、触るときの技術上の注意、経緯の記録の在りか
- **書かないもの**：いまの位置・次の作業・優先順位（正本は private の `chokepointlab-notes/STATUS.md`）、運用ルール（`CLAUDE.md`）、手順（各 Project Skill）
- 1つの仕組みは1〜3行で書き、詳しくは設計書（`tools/*.md`）へリンクする

---

## プロジェクト概要

- **サイト**: https://chokepointlab.com/
- **構成**: `docs/hormuz/index.html`（ホルムズ海峡危機マップ本体・HTML/CSS/JS全集約）+ `docs/index.html`（媒体トップ＝ハブ）+ `docs/data/news_data.json`
- **更新頻度**: 日次更新が基本（毎日）。情勢が膠着している時期などは更新しない日もある
- **目標**: 継続可能な媒体化（信頼性の確立 → 独自ドメイン移行 → 収益化）。※媒体名・ドメイン・法務・収益化などの上流の方針、および三媒体連携の構想はリポジトリ外の戦略文書が正本。この Memory.md は技術・実装の現状に限定する

---

## 仕組みの索引

| 仕組み | 実装・データ | 設計書・記録 |
|---|---|---|
| 配信 | GitHub Pages・独自ドメイン `chokepointlab.com`（2026-09-18 移行。旧 URL は 301 転送）。ダッシュボード `hormuz-data-` は `yattanda.github.io/hormuz-data-/` のまま＝**別オリジン** | `tools/migration-runbook.md`・`tools/migration-baseline-2026-09-13.md` |
| ハブと本体 | `/` はハブ（`docs/index.html`）、本体は `/hormuz/`。`/?focus=<キー>` と `/#map` はハブの JS が `/hormuz/` へ送る | `tools/s11-10-design.md` |
| ニュース表示 | `docs/data/news_data.json`（`latest`・`osint`・`archive`）を JS が描く | `/daily-site-update` |
| 更新履歴 | `docs/data/update_log.json`（`index.html` は最新10件のみ） | — |
| シナリオ確率 | `syncScenarioFromDashboard()` が `hormuz-data-/data/manual-update.json` を読む。時点は `updated_at` を `#sc-sync-at` に入れる | `tools/display-unify-design.md` §3-2-R |
| 日本向け原油フロー | `loadRouteTableFlow()` が `hormuz-data-/data/oil-flow.json` を読む（`hormuz-map` 側に同名ファイルは無い） | `tools/oil-flow-redesign.md` |
| ダッシュボード iframe の高さ | 子が `postMessage({type:'iframeHeight'})` で送り、親が受ける（別オリジンのため）。固定値はフォールバック専用 | `tools/history/memory-issues-2026-05-09.md` |
| 今後の予定日 | `docs/data/upcoming.json`。30秒カラムの「次の焦点」直下に JS が出す（過ぎたら出ない・0件なら行ごと出ない） | `tools/display-unify-design.md` |
| 最終更新からの経過 | ヘッダーの日時の文字を JS が読み、36時間超で「（N時間前）」、72時間超で注意書き | 同上 |
| 値と状態の表示 | JS が入れる場所の初期値は「読み込み中…」、失敗時は「取得できず」。日次はここを触らない（`check_state_labels()`） | 同上 §3-3-R |
| 推定のラベル | `.label-estimate`（統計からの試算）・`.label-ai`（生成 AI の値）。日次はピル直後のラベルを消さない（`check_estimate_labels()`） | 同上 §3-4-R |
| 用語集・ツールチップ | 正本 `docs/data/glossary.json`、ページは `tools/build_glossary.py --write`、部品は `docs/assets/glossary.js` | `tools/glossary-search-design.md` |
| 地図 | Leaflet 1.9.4 を自サイトから配信（`docs/assets/vendor/leaflet-1.9.4/`）。横方向エンドレス（「1-B. WORLD WRAP」） | `tools/map-wraparound-design.md` |
| フォント | Noto Sans JP を自サイトから配信（`docs/assets/fonts/noto-sans-jp/`） | `tools/external-deps-design.md` |
| `?focus=<キー>` | 地図を指定の印へ寄せてポップアップを開く。キーは `docs/hormuz/index.html` の `FOCUS_TARGETS`（5-C） | `tools/history/memory-future-structure-2026-09-21.md` |
| アクセス解析 | GA4 を `docs/` 配下の全ページに設置（2026-09-22）。`hormuz-data-` は未設置 | 同上 |
| 危機N日目 | 2026-02-28 を1日目とし、日付から計算する（`docs/archive/index.html` の `calcBlockadeDay()`） | `tools/blockade-term-policy.md`・`tools/history/memory-blockade-day-2026-08-07.md` |
| AIS 通航船舶数 | 実測は見送り（2026-09-05）。AI 推計のみ、出自を明示。`update_ais.yml` は `if: false` のまま | `hormuz-data-/tools/README.md`・`tools/history/memory-ais-2026-09.md` |
| 日次更新の検証 | `tools/validate_daily.py`（読み取り専用・終了コードで判定。`--check-urls` で URL を叩く） | `tools/history/memory-daily-ops-migration-2026-09.md` |
| UKMTO の警報 | `tools/fetch_ukmto.py`（公式の一覧ページが読む公開 API） | `/daily-site-update` |
| 指示ファイルの検証 | `tools/check_instructions.py`（`CLAUDE.md`・`.claude/rules/`・`Memory.md` の分割を点検） | `tools/claude-md-slim-design.md` |

---

## 触るときの技術上の注意

- **地図に印・線・面を足すときに、手で複製を書かない。**`map.on('layeradd')` が経度 ±360° に自動で複製する。地図を飛ばす処理は `map.flyTo` ではなく `flyToNearest` を使う。`setPopupContent()` で書き換える印はコピー（`_wrapCopies`）にも反映する
- **`L`・`HormuzBasemap` を使うコードは、地図のスクリプト（MILITARY LAYER）の直前の `<script src>` より下か、`DOMContentLoaded` の後に書く**（`<head>` では preload だけ）
- **用語集の区域（`data-zones`）は日次スキルの型の class を使う。**型の class を変えるときは `data-zones` も直す。JS が後から描く区域は描いた直後に `Glossary.annotate()` を呼ぶ
- **新しいページは `<head>` の viewport の直後に GA4 タグを入れる。**記事は `tools/article-template.html` から作る（Google Fonts の `<link>` が戻ると `validate_daily.py` が NG）
- **`?focus=` のキーを足したら、ハブの「YouTube から来た方へ」枠（`docs/index.html` の `#yt-visitors`）と台帳にも足す**
- **`news_data.json` の過去分はスキーマが不揃い**（`osint`・`archive` は旧フィールド名を含む）。一括変換しない。`validate_daily.py` のスキーマ検査は `latest` に限る
- **クラウド環境はシステム時刻が UTC。**日付は `date -u -d '+9 hours'` で取る。コミット時刻はクラウド環境変数 `TZ=Asia/Tokyo` で `+0900` になる
- **旧経路ファイル**（`tools/index_html_diffs.md`・`tools/diffs-generation-rules.md`・`tools/run.bat`・`auto_push.py`・`.github/scripts/apply_diffs.py`・`.github/workflows/mobile-update.yml`）は、Claude Code を使わずに差分を適用できるバックアップとして残す（2026-09-14 決定・期限なし）
- **リポジトリ名を変えるときに追従が要る箇所**は `tools/history/memory-future-structure-2026-09-21.md`「実施時の注意」

---

## 未解決の技術課題（経緯は `tools/history/memory-issues-2026-05-09.md`）

- ルートテーブルのスマホ右余白：`<colgroup>` を変更すると表が崩れる。colgroup を触らない別の方法で検討
- インフォグラフィック導線：タイトルの視認性（30秒カラム末尾）
- スマホ UI の継続改善：`mobile-ui-reviewer` → `responsive-css-specialist` の順。ルールは `tools/design-system.md`・`tools/mobile-ui-rules.md`
- ※優先順位と着手の判断は `STATUS.md` 側

---

## 経緯の記録（原文のまま `tools/history/` に移した。2026-11-07）

| 旧 `Memory.md` の節 | 移した先 |
|---|---|
| 現在の状態（2026-09-18〜10-10 の日付ログ） | `tools/history/memory-state-log-2026-09-10.md` |
| 現在進行中の課題・保留中の課題・今後の最重要課題 | `tools/history/memory-issues-2026-05-09.md` |
| 将来の構成方針（複数チョークポイント化・リポジトリ名）・§11-10 の実施条件・新テーマの土台 | `tools/history/memory-future-structure-2026-09-21.md` |
| AIS 通航船舶数 — 実測と推計の分離・VesselAPI 移行 | `tools/history/memory-ais-2026-09.md` |
| 日次更新の運用移行 — Claude Code 主体化（移行後の定着状況・旧経路ファイル・実測で判明した技術事実を含む） | `tools/history/memory-daily-ops-migration-2026-09.md` |
| 封鎖日数カウンター（blockadeDay）の起算日問題 | `tools/history/memory-blockade-day-2026-08-07.md` |
| 完了済み主要作業 | `tools/history/memory-completed-work.md` |

- 他の文書が「`Memory.md` の◯◯の節」と書いている場合は、上の表で移した先を引く

---

## 環境メモ

- **OS**: Windows 11（Macなし）
- **ffmpeg パス**: `C:\ffmpeg\bin\ffmpeg.exe`（PATH未設定環境対応）
- **Python**: venv 使用 → `venv\Scripts\python`
- **Claude.ai**: 戦略・特別解説コラム・週次レビュー（2026-09-02 の決定により日次からは外す方針。移行完了までは従来どおり差分ファイル生成も担う）
- **Claude Code（PC）**: index.html更新・commit（pushはユーザー確認後）
- **Claude Code（クラウド／スマホ）**: 移行先。ネットワークは Full 設定済み。
  ブラウザ操作・コンピューター使用は PC と隔離のため利用不可
- **auto_push.py / run.bat**: DownloadsフォルダからGitHub API直接push（旧経路・~~凍結予定~~ → 2026-09-14 に**バックアップとして保持**に変更。期限なし）

---

## セッション再開コマンド

```
前回のセッションを再開して
```
