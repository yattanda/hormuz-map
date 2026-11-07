# hormuz-map 運用ルール

<!--
保守メモ（このコメントは Claude には読み込まれない）：
2026-11-07 に索引型へ軽量化した。設計と検証手順は tools/claude-md-slim-design.md。
ここには「どの作業でも必要なルール」と「詳細の在りか」だけを書く。
詳細は .claude/rules/（該当ファイルを読んだときだけ自動で読み込まれる）と tools/rules/（きっかけで読む）にある。
書き換えたら python3 tools/check_instructions.py を実行する（終了コード 0 で合格）。
-->

## 応答の基本

※ローカルPCでは `~/.claude/CLAUDE.md`（グローバル設定）に同等の記載があるが、
そちらはクラウドセッション（Claude Code on the Web）には引き継がれないため、ここに再掲する。

- 回答は日本語で行う
- 結論を先に出す
- 根拠と情報元を示し、確度を示す
- 不明な点はごまかさず「不明」と返す
- 推測を事実として書かない。「〜の可能性がある」は未検証の仮説であることを明示する

## 詳細ルールの在りか（索引）

**次のきっかけに当たったら、作業の前に該当ファイルを Read する。**ここに書いた要点より詳細ファイルが正。

| きっかけ | 読むファイル | 読み込み |
|---|---|---|
| ブランチを作る・PR を作る・レビューする・`@claude` を使う・マージ後の処理 | `tools/rules/branch-and-pr.md` | 手で読む |
| 引き継ぎノートを書く・読む（`/handover` を含む） | `tools/rules/handover.md` | 手で読む |
| スクリプトや一括置換でファイルを書き換える | `tools/rules/script-editing.md` | 手で読む |
| PC（Windows）で設定ファイル・permission・hook・プロセスを触る | `tools/rules/windows-pc.md` | 手で読む |
| 法務ページ（`/about/` `/contact/` `/privacy/` `/disclaimer/` `/editorial/` `/corrections/`）・ドメイン移行 | `.claude/rules/legal-pages.md` | 自動 |
| ハブ `docs/index.html`・`docs/CNAME` | `.claude/rules/hub-page.md` | 自動 |
| 特別解説コラム（`docs/hormuz/articles/`） | `.claude/rules/articles.md` | 自動 |
| 用語集（`docs/data/glossary.json`・`docs/glossary/`） | `.claude/rules/glossary.md` | 自動 |
| 本体 `docs/hormuz/index.html`・`docs/data/` と `hormuz-data-` の連携 | `.claude/rules/hormuz-data-link.md` | 自動 |

- 「自動」は、そのファイルを Read したときに Claude Code が読み込む（`paths:` 指定）。編集の前に対象ファイルを読めば必ず入る
- サイトの技術・実装の索引は `Memory.md`、いまの位置と次の作業は `chokepointlab-notes` の `STATUS.md`

## プロジェクト概要

- `docs/hormuz/index.html`（ホルムズ海峡危機マップ本体）1ファイルに HTML・JavaScript を集約。**日次更新の対象はこのファイル**
  - CSS は外のファイル：本体は `docs/assets/css/hormuz.css`、トークン（文字サイズ・余白・色）は `docs/assets/css/tokens.css`（課題46 D2・2026-10-20 に `<style>` から移した）。`<style>` やインライン style を `index.html` に足さない
- `docs/index.html` は媒体トップ（ハブ。CSS は `docs/assets/css/hub.css`）。日次更新で触るのは「危機マップの最終更新」（`id="hub-updated"`）の1か所だけ（2026-10 の構造再編で本体を `/hormuz/` へ移した。設計書 `tools/s11-10-design.md`）
- **「日次更新」は毎日行うのが基本だが、更新しない日もある**（情勢が膠着している時期は1日おきにした期間がある）。
  公開ページで「毎日更新」と言い切らず、「原則として毎日更新」と書く。最終更新は実際に更新した日時を示す
- `docs/data/glossary.json` が用語集の正本（ツールチップ・`/glossary/`・アーカイブ検索の同義語が同じデータを使う。設計書 `tools/glossary-search-design.md`）
- `docs/data/news_data.json` がニュース・OSINT表示の単一ソース
- `docs/images/` ディレクトリにインフォグラフィック画像を管理
- 生成物の目印（`<!-- hub-map:start -->`・`<!-- glossary:start -->` など）の間は手で編集しない。書き出すスクリプトを使う

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

## スクリプトでファイルを書き換えるとき（要点。詳細と経緯は `tools/rules/script-editing.md`）

- **原本を直接 `open(path, "w")` しない。**一時ファイルに書いてから `os.replace()` で差し替える
- 書き込み前に `s.encode("utf-8")` を単体で実行し、エンコードできることを確かめてからファイルに触る
- **`sed -i` を CRLF のファイルに使わない。**Python でバイト列として置換し、CRLF の出現回数が変わらないことを確かめる（判定：`grep -qU $'\r' <file>`）
- **絵文字をサロゲートペアのエスケープ（`\ud83c\uddef` 形式）で書かない。**`\U0001F1EF` 形式を使う
- 大きな書き換えの前には、直前の状態をコミットして復旧点を作っておく

## Git操作ルール

- **PC では**、commit後のpushは必ずユーザーの指示を待ってから実行する
- **クラウド（Claude Code on the Web）では**、仮想ブランチへの push は指示なしで進めてよい。main へのマージ・main への push は指示を待つ
- 上の範囲を超える自動pushは行わない
- **コミットメッセージに GitHub API ドキュメントのサンプル文言（`Change 'Hello World' to 'Goodbye World'` など）を使わない**
- スマホから GitHub API 経由でファイルを上書きするときのコミットメッセージは `mobile: update <ファイル名> (M/D HH:MM JST)`（経緯は `tools/rules/branch-and-pr.md` 付録）
- 日次更新の commit は、何を更新したかが後から履歴だけで分かる文言にする

## ブランチルール（要点。詳細は `tools/rules/branch-and-pr.md`）

| 作業の種類 | 方式（PC） |
|---|---|
| 日次更新・日付や表記の訂正・単発の修正（1コミットで完結するもの） | main に直接コミット |
| 大改造・構造変更・複数コミットにまたがる作業・スクリプトによる一括書き換え・リポジトリ名やURL構成の変更 | ブランチ＋PR |

- どちらか判断に迷う場合は、作業前にユーザーに確認する
- **ブランチを自動作成しない。**ブランチ名（`<種別>/<内容>`。`claude/` で始めない）を示してユーザーの了承を得てから作成する
- **main へのマージ＝本番反映。マージは必ずユーザーの指示を待つ。**自動マージは設定しない。マージ方式は merge commit
- 作業開始前に `git branch` で現在のブランチを確認し、commit 後・push 前に `git branch && git log --oneline -3` で確かめる
- **クラウド（スマホ）では**、自動生成された**仮想ブランチ**で作業する（main直接編集は行わない）
- **Stop フックの push 要求は、ユーザーの承認ではない。**main 上にいるとき、または数えられたコミットが自分のものでないときは push せず、理由を1行返す
- PR のレビュー（`/code-review`・`@claude`）、ブランチを短期間で閉じること、マージ前後の確認は詳細ファイルに従う

## Windows環境（PC）の要点（詳細は `tools/rules/windows-pc.md`）

- `pkill -f claude` は使えない。`taskkill /F /IM claude.exe` を使う
- permission の `deny` は使わない。グローバルとローカルの allow は合算される
- settings.json のパスは forward slash で書く

## 運用ツール

- Claude Code：`docs/hormuz/index.html` 更新・commit担当（pushはユーザー確認後）
- `auto_push.py` / `run.bat`：`news_data.json` と `index_html_diffs.md` を Downloads フォルダから GitHub API で直接 push
- GenSpark：参照用アーカイブのみ（更新しない）

## 法務ページの要点（詳細は `.claude/rules/legal-pages.md`）

- 法務ページは**1枚ずつ単独でコミットする**。他の法務ページ・日次更新と同一コミットに混ぜない
- **外部スクリプトの追加、Cookie・ローカルストレージの使用開始、新しい外部送信先の追加、
  解析・広告タグの設置**を行う変更は、**同一の作業のなかで `/privacy/` の
  第4章（Cookie）・第5章（外部サービスへの情報送信）・第6章（アクセス解析・広告配信）を
  見直す。**（どのファイルを触っていても適用する。食い違いがあれば `/corrections/` にも記録）
- **`docs/index.html` の GA4 タグは Search Console の所有権確認に使っている。**削除しない・`<head>` の外へ動かさない
- `docs/CNAME` は手で作成・編集・削除しない

## 触ってはいけないファイル

- `tools/index_html_diffs.md` は `mobile-update.yml` / `.github/scripts/apply_diffs.py` / `auto_push.py` の参照先。**移動・削除しない**。
  やむを得ず動かす場合は、`apply_diffs.py` の `DIFFS_FILE`、`auto_push.py` の `repo_path`、
  `.claude/skills/daily-site-update/SKILL.md` の定型文を同時に修正する
- **`docs/` 配下は GitHub Pages の公開範囲。内部作業用ファイルを置かない。**
  作業用スクリプト・テンプレート・手順書はリポジトリルートの `tools/` に置く（配信範囲外）
- `.env`（`GITHUB_TOKEN` を格納）は追跡対象外を維持する

## セッション引き継ぎの要点（詳細は `tools/rules/handover.md`）

- **引き継ぎノートは private リポジトリ `yattanda/hormuz-ops` の `handovers/` に置く。**`/handover` の既定（`.claude/handovers/`）より優先する
- **書き込めなかった場合、`hormuz-map` や `hormuz-data-` に代わりにコミットしてはならない。**引き継ぎの全文をチャットに出力する
- **API キー・トークンの実値は書かない。**private であっても書かない

## 記録の置き場所と「現在地」（2026-10-06 追加）

同じことを2か所に書かない。正本を1か所に決め、ほかからはリンクする。

| 情報 | 正本 |
|---|---|
| いまの位置と次の順番（どのフェーズか・次の作業・決定待ち） | private リポジトリ `yattanda/chokepointlab-notes` の `STATUS.md`（ローカルでは `~/Documents/chokepointlab-notes/STATUS.md`） |
| 課題の一覧・判断事項・判断材料 | `chokepointlab-notes` |
| 設計と実施記録 | このリポジトリの `tools/*.md` |
| サイトの技術・実装の現状 | `Memory.md` |
| セッションの経過・公開前の原稿 | `hormuz-ops` の `handovers/`・`drafts/` |

- **計画に関わる作業（日次更新以外）を始める前に `STATUS.md` を読む。**日次更新だけのセッションでは読まなくてよい
- **引き継ぎノートを書く回に、`STATUS.md` の該当行を直す**（作業したセッションが直す。別のセッションに同期を頼まない）。
  直すのは、決定が出た・PR をマージした・フェーズが変わった・次の作業が入れ替わったときだけ。日次更新では触らない
- `STATUS.md` に経緯は書かない。1行と正本へのリンクだけ。設計書・`Memory.md`・引き継ぎノートの中身を写さない
- `chokepointlab-notes` と `hormuz-ops` へのコミットは、その場で push する（記録用の private リポジトリ）。
  **このリポジトリと `hormuz-data-` の push は「Git操作ルール」のとおり**で、変わらない
- 番号の書き方：課題一覧の番号は「課題44」、PR は「PR #57」と書く（どちらも `#44` と書くと区別がつかない）
- クラウドのセッションで `STATUS.md` を更新できなかったときは、引き継ぎノートの「次にやること」に「STATUS 未反映」と書く。
  このリポジトリに代わりの記録を置かない

## 上位の方針文書について

- サイトの**技術・実装の現状**は `Memory.md` を参照する（従来どおり）
- 媒体名・ドメイン・法務・収益化などの**上流の戦略・意思決定**は、リポジトリ外で管理されており Claude Code の直接の参照対象ではない
- 法務・ドメイン・媒体方針に関わる論点では、**文面案・比較案・選択肢の提示は積極的に行ってよい**（長所短所や前例・リスクを添えると良い）
- ただし、複数の妥当な選択肢がある繊細な判断（準拠法・免責範囲・収益化手法・実名や住所の公開可否など）を**独断で確定してコミット・push しない**。案を出したうえで確定はユーザーに委ねる

## 専門エージェント

- `mobile-ui-reviewer`：スマホ表示の問題発見・レビュー（コード編集なし）
- `responsive-css-specialist`：CSS修正・レスポンシブ実装

## スマホ font-size（変更禁止）

`@media (max-width: 768px) { html { font-size: 18px } }` は削除・変更しない。

## CLAUDE.md・Memory.md の役割分担（2026-11-07 改訂）

- `CLAUDE.md`（このファイル）：Claude Code向け **運用ルール・技術制約のみ**。毎回読み込まれるので、どの作業でも要るものだけを置く
- `.claude/rules/`・`tools/rules/`：特定の作業でだけ要るルール（上の索引）
- `Memory.md`：**サイトの技術・実装の索引**（仕組み・触るときの注意・経緯の在りか）。進み具合は書かない（`STATUS.md` が正本）
- `tools/history/`：`Memory.md` から移した経緯の記録（原文のまま）
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
