#!/usr/bin/env python3
"""
apply_diffs.py
docs/tools/index_html_diffs.md の <!-- APPLY --> ブロックを解析して
docs/index.html に str_replace を適用する。

ブロック形式:
  <!-- APPLY:START -->
  <!-- OLD:START -->
  （置き換え前の文字列・完全一致）
  <!-- OLD:END -->
  <!-- NEW:START -->
  （置き換え後の文字列）
  <!-- NEW:END -->
  <!-- APPLY:END -->
"""
import re
import sys
from pathlib import Path

DIFFS_FILE = Path("docs/tools/index_html_diffs.md")
HTML_FILE  = Path("docs/index.html")

# ブロックを抽出する正規表現
BLOCK_RE = re.compile(
    r'<!-- APPLY:START -->[ \t]*\n'
    r'<!-- OLD:START -->[ \t]*\n'
    r'(.*?)'               # グループ1: old_str
    r'\n?<!-- OLD:END -->[ \t]*\n'
    r'<!-- NEW:START -->[ \t]*\n'
    r'(.*?)'               # グループ2: new_str
    r'\n?<!-- NEW:END -->[ \t]*\n'
    r'<!-- APPLY:END -->',
    re.DOTALL
)


def main() -> None:
    # ── ファイル確認 ───────────────────────────────────────
    if not DIFFS_FILE.exists():
        print(f"❌ diffs ファイルが見つかりません: {DIFFS_FILE}")
        sys.exit(1)
    if not HTML_FILE.exists():
        print(f"❌ index.html が見つかりません: {HTML_FILE}")
        sys.exit(1)

    diffs_text = DIFFS_FILE.read_text(encoding="utf-8")
    html_text  = HTML_FILE.read_text(encoding="utf-8")

    # ── ブロック抽出 ───────────────────────────────────────
    pairs = [(m.group(1), m.group(2)) for m in BLOCK_RE.finditer(diffs_text)]
    print(f"📦 APPLY ブロック検出数: {len(pairs)}")
    print()

    if not pairs:
        print("⚠️  適用ブロックなし。")
        print("   diffs.md に <!-- APPLY:START/END --> ブロックが含まれているか確認してください。")
        sys.exit(0)

    # ── 適用 ───────────────────────────────────────────────
    errors: list[str] = []
    applied = 0

    for i, (old, new) in enumerate(pairs, 1):
        count = html_text.count(old)
        if count == 0:
            errors.append(
                f"#{i}: old_str が index.html に見つかりません\n"
                f"       先頭70文字: {old[:70]!r}"
            )
        elif count > 1:
            errors.append(
                f"#{i}: old_str が {count} 箇所にマッチ（曖昧のためスキップ）\n"
                f"       先頭70文字: {old[:70]!r}"
            )
        else:
            html_text = html_text.replace(old, new, 1)
            print(f"✅ #{i}: 適用完了")
            applied += 1

    print()

    # ── エラー報告 ─────────────────────────────────────────
    if errors:
        print(f"{'─' * 50}")
        print(f"❌ {len(errors)} 件のエラー:")
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        print()
        # 一部適用できていれば書き込んでから失敗終了
        if applied > 0:
            HTML_FILE.write_text(html_text, encoding="utf-8")
            print(f"⚠️  {applied} 件は適用済み・{len(errors)} 件はスキップ")
        sys.exit(1)

    # ── 書き込み ───────────────────────────────────────────
    HTML_FILE.write_text(html_text, encoding="utf-8")
    print(f"✅ 全 {applied} 件の変更を docs/index.html に適用しました")


if __name__ == "__main__":
    main()
