# Windows 環境・Claude Code 設定（PC）

> 2026-11-07 にルートの `CLAUDE.md` から原文のまま移した（設計書 `tools/claude-md-slim-design.md`）。
> ルートには要点だけを残している。食い違ったら**この文書が正**。

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
  "command": "node C:/Users/<ユーザー名>/.claude/hooks/session-summary.js"
  ```
- Node.jsはWindows上でもforward slashに対応している
