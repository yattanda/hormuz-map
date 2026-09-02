# hormuz-map 運用ルール

## プロジェクト概要

- `docs/index.html` 1ファイルにHTML・CSS・JavaScript全て集約
- `docs/data/news_data.json` がニュース・OSINT表示の単一ソース
- `docs/images/` ディレクトリにインフォグラフィック画像を管理
- ※目標・URL・運用状況は `Memory.md` を参照

## 絶対ルール

- コメントアウトタイトル `<!-- xxxx -->` は変更しない
- ニュースのURLはAI生成・推測による捏造禁止（web検索で確認済みのURLは使用可）
- 更新対象セクション以外は触らない
- タイムスタンプの日付は必ずユーザーが明示したものを使用する。未明示の場合は作業前に確認する
- **日付を書き込む前に、その都度コマンドで現在日時を実測する。**
  セッション開始時に取得した日付を使い回さない
  （`.claude/settings.json` の UserPromptSubmit フックが毎ターン `[現在日時 JST]` を注入する。
   注入値が無い場合は以下を実行する。**素の `date` は使わない**——
   クラウド環境（Claude Code on the Web）はシステム時刻が UTC のため JST と9時間ずれる）

  ```bash
  date -u -d '+9 hours' '+%Y-%m-%d %H:%M JST'
  ```
- 長時間のセッションでは日付をまたいでいる可能性を常に疑う。
  夜間に開始して翌日に再開するケースで実際に誤りが発生している（2026-08-31→09-01）
- 「最終更新」は作業日ではなく**内容を変更した日**を書く。
  レイアウトのみの変更や、表示に影響しない修正では更新しない

## スクリプトでファイルを書き換えるときのルール

- **原本を直接 `open(path, "w")` しない。**一時ファイルに書いてから `os.replace()` で差し替える
  - 理由：`"w"` は開いた時点でファイルを空にするため、書き込み中に例外が出ると**原本が失われる**。
    2026-09-01 に `docs/index.html`（5,015行）を実際に全消ししている
    （直前のコミットが push 済みだったため `git checkout` で復旧）
- 書き込み前に `s.encode("utf-8")` を単体で実行し、エンコードできることを確かめてからファイルに触る
- **絵文字をサロゲートペアのエスケープ（`\ud83c\uddef` 形式）で書かない。**
  Python では単独サロゲート扱いになり UTF-8 に変換できず例外になる。
  `\U0001F1EF` 形式を使うか、置換文字列に絵文字を含めない
- 大きな書き換えの前には、直前の状態をコミットして復旧点を作っておく

## Git操作ルール

- commit後のpushは必ずユーザーの指示を待ってから実行する
- 自動pushは行わない
- **コミットメッセージに GitHub API ドキュメントのサンプル文言を使わない。**
  `Change 'Hello World' to 'Goodbye World'` / `Update print statement from 'Hello' to 'Goodbye'` は
  Contents API のドキュメント例であり、実際に 2026-08-29・08-31・09-02 の3回、
  スマホから `docs/tools/index_html_diffs.md` を更新した際にそのまま記録されている
- スマホ（Claude Code on the Web）から GitHub API 経由でファイルを上書きする場合、
  コミットメッセージは次の形式にする
  ```
  mobile: update <ファイル名> (M/D HH:MM JST)
  ```
  例：`mobile: update index_html_diffs.md (9/2 10:45 JST)`
- 日次更新の commit は、何を更新したかが後から履歴だけで分かる文言にする

## ブランチルール

### PC（ローカル・VS Code拡張）

- 作業は必ず main ブランチで直接行う
- 新しいブランチ（claude/〇〇〇 等）を自動作成しない
- 作業開始前に必ず `git branch` で main にいることを確認する
- main 以外のブランチにいた場合は `git checkout main` してから作業を開始する
- commit 後・push 前に `git branch && git log --oneline -3` を実行し、main ブランチにコミットされていることを確認してからユーザーに報告する

### スマホ（Claude Code on the Web）

- スマホから操作する場合は、クラウドセッションが自動生成する**仮想ブランチ**で作業する（main直接編集は行わない）
- これはクラウドセッション側の隔離設計によるデフォルト動作であり、明示的な指示がなくても仮想ブランチを使ってよい
- 仮想ブランチへの commit・push（diffのレビュー用push）は通常通り進めてよい
- **mainへのマージは必ずユーザーの指示を待ってから行う**（PR作成後、ユーザーがレビュー・マージ操作を行う、またはマージ指示を出すまで待機）
- 自動マージは行わない

## Windows環境・Claude Code設定ルール

### プロセス終了コマンド（Windows専用）
- `pkill -f claude` はWindows非対応。必ず以下を使うこと：
  ```
  taskkill /F /IM claude.exe
  ```

### permission設定の構造（重要）
- グローバル設定：`%USERPROFILE%\.claude\settings.json`
- ローカル設定：`.claude/settings.local.json`（プロジェクト内・gitignore済）
- **両ファイルのallowリストは合算される**（ローカルだけ修正しても不十分）
- `deny` = 完全ブロック（pushすら不可になる）→ **denyは使わない**
- allowに未登録 = 確認ダイアログ表示（git pushに推奨）
- git pushを確認ダイアログにするには**両ファイルからallowを削除**する
- `Bash(*)` より明示的ホワイトリストのほうが信頼性が高い（v2.1.123確認済）

### settings.json内のWindowsパス記述
- バックスラッシュ（`\`）はPython書換えやbash経由でエスケープが剥がれる事故あり
- hookやコマンドパスは**forward slash推奨**：
  ```json
  "command": "node C:/Users/yutay/.claude/hooks/session-summary.js"
  ```
- Node.jsはWindows上でもforward slashに対応している

## 運用ツール

- Claude Code：`docs/index.html` 更新・commit担当（pushはユーザー確認後）
- `auto_push.py` / `run.bat`：`news_data.json` と `index_html_diffs.md` を Downloads フォルダから GitHub API で直接 push
- GenSpark：参照用アーカイブのみ（更新しない）

## 特別解説コラムの個別ページ化

- 「特別解説コラム」の各コラムは `docs/articles/{slug}.html` として個別ページ化されている（一覧：`docs/articles/index.html`）
- `docs/index.html` 側の各カードは要約＋「全文を読む」リンクのみを表示し、本文全文は個別ページ側が正とする
- 新規コラムを追加する場合は `docs/tools/new-article-checklist.md` の手順に従うこと

## 法務ページ・ドメイン移行フェーズのルール

- 法務ページ（`/about/` `/contact/` `/privacy/` `/disclaimer/` `/editorial/` `/corrections/`）は、正規ディレクトリ形式 `docs/<name>/index.html` で作成する
- 法務ページは**1枚ずつ単独でコミットする**。他の法務ページ・日次更新（`index.html` / `news_data.json` 等）・archive 整理と同一コミットに混ぜない
- 作業ツリーに未コミットの変更（`.gitignore` 変更・未追跡の archive 系ファイル等）が残っている場合は、単独コミットを守るため stash で退避してから作業し、push 後に戻す
- 改行コードは既存 `docs/index.html` に合わせ **CRLF・BOMなし**で統一する
- **URL の書き方は2通りだけ。`{{base_url}}` などのプレースホルダは使わない**
  - ページ間のリンク（`<a href>`）は**文書相対パス**（`../about/`、トップは `../`）。ホスト名を含まないため移行時の書き換えが不要
  - `canonical` / `og:url` は仕様上絶対URLが必須なので**絶対URLを直接書く**。`tools/migrate-domain.sh` がリテラル文字列 `yattanda.github.io/hormuz-map` を検出して置換するため、移行時に自動追従する
  - （経緯）従来は「`{{base_url}}` のまま残し、一括展開は移行スクリプトが担う」としていたが、**展開機構は実装されていなかった**（`migrate-domain.sh` はリテラルのホスト名しか置換しない）。その結果法務ページ6枚のリンクが本番で全滅していた。commit 47ef650 で解消済み
- 未完成ページへのリンクは **`TODO(§11-6):` という文字列マーカー**で残す。これは戦略側の完了判定に対応する予約語であり、別の書式に変えない
- **パス変更とホスト名（ドメイン）置換を同一コミットに混ぜない**（残存検証の判定が濁るため）
- 破壊的操作を含むスクリプトは dry-run を既定とし、成否は警告ではなく**終了コードで判定できる**形にする

## 触ってはいけないファイル

- `docs/tools/index_html_diffs.md` は `mobile-update.yml` / `.github/scripts/apply_diffs.py` の参照先。**移動・削除しない**。やむを得ず動かす場合は `apply_diffs.py` のパスも同時に修正する
- `.env`（`GITHUB_TOKEN` を格納）は追跡対象外を維持する

## 上位の方針文書について

- サイトの**技術・実装の現状**は `Memory.md` を参照する（従来どおり）
- 媒体名・ドメイン・法務・収益化などの**上流の戦略・意思決定**は、リポジトリ外で管理されており Claude Code の直接の参照対象ではない
- 法務・ドメイン・媒体方針に関わる論点では、**文面案・比較案・選択肢の提示は積極的に行ってよい**（長所短所や前例・リスクを添えると良い）
- ただし、複数の妥当な選択肢がある繊細な判断（準拠法・免責範囲・収益化手法・実名や住所の公開可否など）を**独断で確定してコミット・push しない**。案を出したうえで確定はユーザーに委ねる

## hormuz-data- 連携ルール

- `hormuz-data-` リポジトリはダッシュボード・自動データの別リポジトリ
- `data/manual-update.json` の `scenario` フィールド（A/B/C/D確率）がシナリオ確率の正として自動同期される
- `syncScenarioFromDashboard()` がページ読み込み時にfetchして `sc-tag-A/B/C/D` を上書き（手動更新不要）
- fetch URL：`https://yattanda.github.io/hormuz-data-/data/manual-update.json`
- **`hormuz-data-` の `data/oil-flow.json`** が日本原油調達フローの単一ソース（`loadRouteTableFlow()` が `SITE_CONFIG.DASHBOARD_BASE + '/data/oil-flow.json'` をfetchして値を注入）
  - `hormuz-map` 側に `docs/data/oil-flow.json` は**存在しない**。従来の記述は誤りで、実測により訂正した
  - 同ファイルの `updated` はルートテーブルの**基準日表示に直結**する（`jf-basis-date` に注入）。値を更新するときは `updated` も必ず更新する
- **LiveServer では iframe 内容は更新が反映されない**（GitHub Pages URL から読み込むため）。hormuz-data- の変更は push して GitHub Pages 経由で確認すること

## 専門エージェント

- `mobile-ui-reviewer`：スマホ表示の問題発見・レビュー（コード編集なし）
- `responsive-css-specialist`：CSS修正・レスポンシブ実装

## スマホ font-size（変更禁止）

`@media (max-width: 768px) { html { font-size: 18px } }` は削除・変更しない。

## Memory.mdとの役割分担

- `CLAUDE.md`（このファイル）：Claude Code向け **運用ルール・技術制約のみ**
- `Memory.md`：Claude.ai向け **引き継ぎ・現状・課題・完了履歴**
- CLAUDE.md には「何をすべきか（ルール）」のみ記載し、「現状・経緯」は書かない

## Project Skills の使い分け

以下の作業に該当する場合は、該当する Project Skill を優先して使用する。

| スキル | 使うタイミング |
|---|---|
| `/daily-site-update` | 毎日の定常更新作業 |
| `/html-safe-edit` | HTML/CSS/JSの構造・テーブル・折り畳み表示を触るとき |
| `/content-style-guide` | ニュース記事・メディア選定・文章表記の確認 |
| `/publish-checklist` | 更新完了前・commit前・push前の最終チェック |
| `/feature-extension-plan` | 新機能・スマホUI・レスポンシブ改善・構造変更の前 |
| `/resolve-news-data-conflict` | git rebase中にconflictが発生したとき |

`/publish-checklist` と `/resolve-news-data-conflict` は、原則としてユーザーが明示的に呼び出した場合のみ使用する。
