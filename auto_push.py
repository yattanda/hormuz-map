"""
auto_push.py  ― hormuz-map 自動push スクリプト
改訂: 2026-04-30
変更点:
  - 旧来の「最新ファイル自動選択・古い重複削除」ロジックを維持
  - ファイルサイズ上限チェック（MAX_FILE_SIZE_KB）追加
  - 空ファイル拒否 追加
  - GITHUB_TOKEN / github_pat_ / ghp_ を含むファイルはpush拒否 追加
  - push前に対象ファイル名・サイズを表示 追加
  - 前回と同一ファイル（差分なし）の場合は警告を表示 追加
"""

import os
import re
import hashlib
import base64
import requests
from pathlib import Path
from dotenv import load_dotenv

# ─── 設定 ──────────────────────────────────────────────────
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER   = os.getenv("REPO_OWNER", "yattanda")
REPO_NAME    = os.getenv("REPO_NAME",  "hormuz-map")

# push先リポジトリ内パス → ローカルの「基準ファイル名（拡張子あり）」
FILE_MAP = {
    "data/news_data.json":  "news_data.json",
    "index_html_diffs.md":  "index_html_diffs.md",
}

DOWNLOADS_DIR = Path(r"C:\Users\yutay\Downloads")

# ─── レート設定 ──────────────────────────────────────────────
# ファイルサイズ上限（KB）。これを超えるファイルはpush拒否
MAX_FILE_SIZE_KB = 512

# トークン漏洩ガード用キーワード
TOKEN_PATTERNS = [
    "GITHUB_TOKEN",
    "github_pat_",
    "ghp_",
]
# ─────────────────────────────────────────────────────────────


def find_latest_file(base_name: str) -> Path | None:
    """
    Downloadsフォルダから base_name に対応する最新ファイルを返す。
    「news_data (1).json」などの重複は自動で最新選択・古いものを削除。

    マッチパターン（例: base_name = "news_data.json"）
      news_data.json
      news_data (1).json
      news_data (2).json
      news_data(1).json  ← スペースなし variant
    """
    stem, suffix = os.path.splitext(base_name)

    all_files = list(DOWNLOADS_DIR.iterdir())
    pattern = re.compile(
        r"^" + re.escape(stem) + r"(\s*\(\d+\))?" + re.escape(suffix) + r"$",
        re.IGNORECASE,
    )
    candidates = [f for f in all_files if f.is_file() and pattern.match(f.name)]

    if not candidates:
        return None

    # 最終更新時刻が最も新しいものを選ぶ
    candidates.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    newest = candidates[0]

    # 古い重複ファイルを削除（最新1件だけ残す）
    for old in candidates[1:]:
        try:
            old.unlink()
            print(f"  🗑  削除: {old.name}  (古い重複)")
        except Exception as e:
            print(f"  ⚠  削除失敗: {old.name} ({e})")

    return newest


def check_file_safety(local_path: Path) -> tuple[bool, str]:
    """
    ファイルの安全チェック（空・サイズ上限・トークン漏洩）。
    戻り値: (OK: bool, エラーメッセージ: str)
    """
    size_bytes = local_path.stat().st_size

    # 空ファイル拒否
    if size_bytes == 0:
        return False, "空ファイルのため push を中断します。"

    # ファイルサイズ上限
    size_kb = size_bytes / 1024
    if size_kb > MAX_FILE_SIZE_KB:
        return False, (
            f"ファイルサイズ {size_kb:.1f} KB が上限 {MAX_FILE_SIZE_KB} KB を超えています。"
            " 誤ったファイルの可能性があります。"
        )

    # トークン漏洩チェック
    try:
        content_text = local_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return False, f"ファイル読み込みエラー: {e}"

    for pattern in TOKEN_PATTERNS:
        if pattern in content_text:
            return False, (
                f"⚠ 危険: ファイル内に '{pattern}' が含まれています！"
                " 機密情報の混入を防ぐため push を中断します。"
            )

    return True, ""


def get_remote_sha_and_content(repo_path: str) -> tuple[str | None, bytes | None]:
    """GitHub上の既存ファイルのSHAとコンテンツを取得。"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{repo_path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.get(url, headers=headers, timeout=15)
    if resp.status_code == 200:
        data = resp.json()
        sha = data.get("sha")
        content_b64 = data.get("content", "").replace("\n", "")
        try:
            remote_bytes = base64.b64decode(content_b64)
        except Exception:
            remote_bytes = None
        return sha, remote_bytes
    return None, None


def files_are_identical(local_path: Path, remote_bytes: bytes | None) -> bool:
    """ローカルとリモートが同一内容かSHA256で比較。"""
    if remote_bytes is None:
        return False  # リモート未存在 = 新規 → 差分あり扱い
    local_bytes = local_path.read_bytes()
    return hashlib.sha256(local_bytes).digest() == hashlib.sha256(remote_bytes).digest()


def push_file(local_path: Path, repo_path: str, sha: str | None) -> bool:
    """ファイルをGitHub APIでpushする。成功時True。"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{repo_path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type":  "application/json",
    }
    content_b64 = base64.b64encode(local_path.read_bytes()).decode()
    payload = {
        "message": f"auto: update {repo_path}",
        "content": content_b64,
    }
    if sha:
        payload["sha"] = sha

    resp = requests.put(url, headers=headers, json=payload, timeout=30)
    if resp.status_code in (200, 201):
        print(f"  ✅ push成功: {repo_path}")
        return True
    else:
        print(f"  ❌ push失敗: {repo_path}  [{resp.status_code}] {resp.text[:200]}")
        return False


def main():
    if not GITHUB_TOKEN:
        raise SystemExit("❌ .env に GITHUB_TOKEN が設定されていません。")

    print(f"\n📂 Downloadsフォルダ: {DOWNLOADS_DIR}\n")

    results = {}
    for repo_path, base_name in FILE_MAP.items():

        print(f"{'━' * 50}")
        print(f"🔍 {base_name} を検索中...")

        # 最新ファイルを自動選択（重複は古いものを自動削除）
        local_file = find_latest_file(base_name)

        if local_file is None:
            print(f"  ⚠   ファイルが見つかりません: {base_name}  → スキップ")
            results[repo_path] = False
            print()
            continue

        # push前にファイル名・サイズを表示
        size_kb = local_file.stat().st_size / 1024
        print(f"  📄 対象ファイル : {local_file.name}")
        print(f"     フルパス     : {local_file}")
        print(f"     ファイルサイズ: {size_kb:.1f} KB")

        # 安全チェック（空・サイズ上限・トークン漏洩）
        ok, err_msg = check_file_safety(local_file)
        if not ok:
            print(f"  ❌ {err_msg}")
            results[repo_path] = False
            print()
            continue

        # リモート情報取得（SHA + コンテンツ）
        sha, remote_bytes = get_remote_sha_and_content(repo_path)

        # 差分チェック
        if files_are_identical(local_file, remote_bytes):
            print()
            print("  ⚠️  前回と同一ファイルです（空撃ちでトークン無駄遣いにならないよう確認してください）")
            results[repo_path] = False
            print()
            continue

        # push実行
        ok = push_file(local_file, repo_path, sha)
        results[repo_path] = ok
        print()

    # ─── サマリー ────────────────────────────────────────────
    print("=" * 50)
    success = sum(v for v in results.values())
    total   = len(results)
    print(f"完了: {success}/{total} ファイル push成功")
    if success < total:
        failed = [k for k, v in results.items() if not v]
        print("スキップ/失敗:", ", ".join(failed))
    print("=" * 50)


if __name__ == "__main__":
    main()
