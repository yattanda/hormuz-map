#!/usr/bin/env bash
# tools/migrate-domain.sh
# ドメイン / hormuz-data- リポジトリ名 移行スクリプト（置換＋残存検証）
#
# 使い方:
#   tools/migrate-domain.sh --new-site <new-host/path> [--new-data <new-host/path>] [--apply]
#
# 例（独自ドメイン移行）:
#   tools/migrate-domain.sh --new-site hormuz-map.example.com --apply
#
# 例（hormuz-data- のリポジトリ名変更も同時に行う場合）:
#   tools/migrate-domain.sh --new-site hormuz-map.example.com \
#     --new-data hormuz-data.example.com --apply
#
# --apply を付けない場合は dry-run（差分プレビューのみ、ファイルは書き換えない）。
# 対象ファイルは `git grep` で検出した git 管理下のテキストファイルのみ（.git内部・バイナリは対象外）。
#
# CRLF(Windows改行)を含むファイル（README.md等）でも改行コードを壊さないよう、
# 実際の置換処理は Python (newline='' でバイナリセーフに読み書き) で行う。
# sed等のUnixツールはGit Bash上でCRLFをLFに正規化してしまう場合があるため使用しない。

set -euo pipefail

OLD_SITE="yattanda.github.io/hormuz-map"
NEW_SITE=""
OLD_DATA="yattanda.github.io/hormuz-data-"
NEW_DATA=""
APPLY=0

usage() {
  echo "使い方: $0 --new-site <new-host/path> [--old-site <old-host/path>] [--new-data <new-host/path>] [--old-data <old-host/path>] [--apply]" >&2
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --old-site) OLD_SITE="$2"; shift 2;;
    --new-site) NEW_SITE="$2"; shift 2;;
    --old-data) OLD_DATA="$2"; shift 2;;
    --new-data) NEW_DATA="$2"; shift 2;;
    --apply) APPLY=1; shift;;
    -h|--help) usage;;
    *) echo "不明なオプション: $1" >&2; usage;;
  esac
done

[[ -z "$NEW_SITE" ]] && usage

PY="$(command -v python || command -v python3 || true)"
if [[ -z "$PY" ]]; then
  echo "エラー: python (または python3) が見つかりません。CRLFセーフな置換に必要です。" >&2
  exit 1
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "エラー: gitリポジトリ内で実行してください。" >&2
  exit 1
fi

# 除外パターン: 画像・バイナリ、このスクリプト自身
EXCLUDES=(':!*.png' ':!*.jpg' ':!*.jpeg' ':!*.ico' ':!*.gif' ':!*.woff' ':!*.woff2' ':!tools/migrate-domain.sh')

collect_targets() {
  local pattern="$1"
  git grep -l -F "$pattern" -- . "${EXCLUDES[@]}" 2>/dev/null || true
}

TARGET_FILES="$(collect_targets "$OLD_SITE")"
if [[ -n "$NEW_DATA" ]]; then
  TARGET_FILES="$TARGET_FILES
$(collect_targets "$OLD_DATA")"
fi
TARGET_FILES="$(printf '%s\n' "$TARGET_FILES" | grep -v '^$' | sort -u || true)"

if [[ -z "$TARGET_FILES" ]]; then
  echo "対象文字列（$OLD_SITE）を含むファイルは見つかりませんでした。"
  exit 0
fi

echo "=== 対象ファイル ($(printf '%s\n' "$TARGET_FILES" | wc -l)件) ==="
printf '%s\n' "$TARGET_FILES"
echo ""

echo "=== 置換内容 ==="
echo "  $OLD_SITE  →  $NEW_SITE"
[[ -n "$NEW_DATA" ]] && echo "  $OLD_DATA  →  $NEW_DATA"
echo ""

# --- Python置換ヘルパー ---
# 引数: mode(check|apply) old_site new_site old_data new_data files...
run_python_replace() {
  local mode="$1"; shift
  "$PY" - "$mode" "$OLD_SITE" "$NEW_SITE" "$OLD_DATA" "$NEW_DATA" "$@" <<'PYEOF'
import sys, io, difflib

# Windowsコンソールのcp932ではなくUTF-8で出力する（日本語文字化け・絵文字クラッシュ対策）
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

mode, old_site, new_site, old_data, new_data = sys.argv[1:6]
files = sys.argv[6:]

changed_any = False
for path in files:
    with io.open(path, "r", encoding="utf-8", newline="") as f:
        original = f.read()

    updated = original.replace(old_site, new_site)
    if new_data:
        updated = updated.replace(old_data, new_data)

    if updated == original:
        continue

    changed_any = True
    if mode == "check":
        diff = difflib.unified_diff(
            original.splitlines(keepends=True),
            updated.splitlines(keepends=True),
            fromfile=f"a/{path}",
            tofile=f"b/{path}",
        )
        sys.stdout.writelines(diff)
        print()
    else:
        with io.open(path, "w", encoding="utf-8", newline="") as f:
            f.write(updated)
        print(f"  更新: {path}")

sys.exit(0 if changed_any or mode == "apply" else 0)
PYEOF
}

if [[ "$APPLY" -eq 0 ]]; then
  echo "[dry-run] --apply が指定されていないため、ファイルは変更していません。"
  echo "--- 差分プレビュー ---"
  run_python_replace check $TARGET_FILES
  echo ""
  echo "内容を確認し、問題なければ --apply を付けて再実行してください。"
  exit 0
fi

echo "=== 置換実行 ==="
run_python_replace apply $TARGET_FILES

echo ""
echo "=== 残存検証 ==="
REMAINING="$(collect_targets "$OLD_SITE")"
if [[ -n "$NEW_DATA" ]]; then
  REMAINING="$REMAINING
$(collect_targets "$OLD_DATA")"
fi
REMAINING="$(printf '%s\n' "$REMAINING" | grep -v '^$' || true)"

if [[ -z "$REMAINING" ]]; then
  echo "✅ 旧文字列（$OLD_SITE$( [[ -n "$NEW_DATA" ]] && echo ", $OLD_DATA")）の残存はありません。"
  echo ""
  echo "完了。'git diff' で変更内容を確認し、問題なければ commit してください。"
  exit 0
fi

echo "❌ 以下のファイルに旧文字列が残っています（要修正）:"
printf '%s\n' "$REMAINING" | while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  echo "  - $f"
  git grep -n -F "$OLD_SITE" -- "$f" 2>/dev/null | sed 's/^/      /' || true
  if [[ -n "$NEW_DATA" ]]; then
    git grep -n -F "$OLD_DATA" -- "$f" 2>/dev/null | sed 's/^/      /' || true
  fi
done

echo ""
echo "失敗: 旧文字列が残存しています。上記を確認し、手動で修正してください。"
exit 1
