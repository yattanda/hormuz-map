"""
auto_push.py  ― hormuz-map / hormuz-data- 自動push スクリプト
改訂: 2026-05-04 (rev2)
変更点:
  - FILE_MAP を複数リポジトリ対応に拡張（リストオブジェクト形式へ変更）
  - hormuz-data- の data/oil-flow.json を FILE_MAP に追加
  - push成功後に各ローカルリポジトリへ git pull --rebase を自動実行
  - git pull の対象をpush成否に関わらずファイル発見時点で追加（スキップ時も pull する）
"""

import os
import re
import hashlib
import base64
import subprocess
import requests
from pathlib import Path
from dotenv import load_dotenv

# ─── 設定 ──────────────────────────────────────────────────
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER   = os.getenv("REPO_OWNER", "yattanda")

# push先の定義（複数リポジトリ対応）
# - repo       : GitHubリポジトリ名
# - repo_path  : リポジトリ内のファイルパス
# - local_name : Downloadsフォルダ内の基準ファイル名
# - local_repo : ローカルのgitリポジトリパス（git pull対象）
FILE_MAP = [
    {
        "repo":       "hormuz-map",
        "repo_path":  "docs/data/news_data.json",
        "local_name": "news_data.json",
        "local_repo": r"C:\Users\yutay\Documents\GitHub\hormuz-map",
    },
    {
        "repo":       "hormuz-map",
        "repo_path":  "docs/tools/index_html_diffs.md",
        "local_name": "index_html_diffs.md",
        "local_repo": r"C:\Users\yutay\Documents\GitHub\hormuz-map",
    },
    {
        "repo":       "hormuz-data-",
        "repo_path":  "data/oil-flow.json",
        "local_name": "oil-flow.json",
        "local_repo": r"C:\Users\yutay\Documents\GitHub\hormuz-data-",
    },
]

DOWNLOADS_DIR = Path(r"C:\Users\yutay\Downloads")

# ─── ガード設定 ────────────────────────────────────────────
MAX_FILE_SIZE_KB = 512

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

    candidates.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    newest = candidates[0]

    for old in candidates[1:]:
        try:
            old.unlink()
            print(f"  🗑  削除: {old.name}  (古い重複)")
        except Exception as e:
            print(f"  ⚠  削除失敗: {old.name} ({e})")

    return newest


def check_file_safety(local_path: Path) -> tuple[bool, str]:
    """ファイルの安全チェック（空・サイズ・トークン漏洩）。"""
    size_bytes = local_path.stat().st_size

    if size_bytes == 0:
        return False, "空ファイルのため push を中止します。"

    size_kb = size_bytes / 1024
    if size_kb > MAX_FILE_SIZE_KB:
        return False, (
            f"ファイルサイズ {size_kb:.1f} KB が上限 {MAX_FILE_SIZE_KB} KB を超えています。"
            " 誤ったファイルの可能性があります。"
        )

    try:
        content_text = local_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return False, f"ファイル読み込みエラー: {e}"

    for pattern in TOKEN_PATTERNS:
        if pattern in content_text:
            return False, (
                f"⛔ 危険: ファイル内に '{pattern}' が含まれています！"
                " 機密情報の混入を防ぐため push を中止します。"
            )

    return True, ""


def get_remote_sha_and_content(repo: str, repo_path: str) -> tuple[str | None, bytes | None]:
    """GitHub上の既存ファイルのSHAとコンテンツを取得。"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{repo}/contents/{repo_path}"
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
        return False
    local_bytes = local_path.read_bytes()
    return hashlib.sha256(local_bytes).digest() == hashlib.sha256(remote_bytes).digest()


def push_file(local_path: Path, repo: str, repo_path: str, sha: str | None) -> bool:
    """ファイルをGitHub APIでpushする。成功時True。"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{repo}/contents/{repo_path}"
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
        print(f"  ✅ push成功: {repo}/{repo_path}")
        return True
    else:
        print(f"  ❌ push失敗: {repo}/{repo_path}  [{resp.status_code}] {resp.text[:200]}")
        return False


def git_pull_local(local_repo: str) -> None:
    """push成功後にローカルリポジトリを git pull --rebase で同期。"""
    print(f"  🔄 git pull --rebase: {local_repo}")
    try:
        result = subprocess.run(
            ["git", "pull", "--rebase", "origin", "main"],
            cwd=local_repo,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"  ✅ git pull成功: {Path(local_repo).name}")
        else:
            print(f"  ⚠️  git pull失敗（手動でpullしてください）:")
            print(f"     {result.stderr.strip()}")
    except Exception as e:
        print(f"  ⚠️  git pull実行エラー: {e}")


def main():
    if not GITHUB_TOKEN:
        raise SystemExit("❌ .env に GITHUB_TOKEN が設定されていません。")

    print(f"\n📂 Downloadsフォルダ: {DOWNLOADS_DIR}\n")

    results = {}
    pull_target_repos = set()  # ファイル発見時点でpull対象に追加（push成否は問わない）

    for entry in FILE_MAP:
        repo       = entry["repo"]
        repo_path  = entry["repo_path"]
        local_name = entry["local_name"]
        local_repo = entry["local_repo"]

        print(f"{'─' * 50}")
        print(f"🔍 {local_name} を検索中...  [{repo}]")

        local_file = find_latest_file(local_name)

        if local_file is None:
            print(f"  ⚠  ファイルが見つかりません: {local_name}  → スキップ")
            results[repo_path] = False
            print()
            continue

        # ファイルが見つかった時点でpull対象に追加（push成否は問わない）
        pull_target_repos.add(local_repo)

        size_kb = local_file.stat().st_size / 1024
        print(f"  📄 対象ファイル : {local_file.name}")
        print(f"     フルパス     : {local_file}")
        print(f"     ファイルサイズ: {size_kb:.1f} KB")

        ok, err_msg = check_file_safety(local_file)
        if not ok:
            print(f"  ❌ {err_msg}")
            results[repo_path] = False
            print()
            continue

        sha, remote_bytes = get_remote_sha_and_content(repo, repo_path)

        if files_are_identical(local_file, remote_bytes):
            print()
            print("  ⚠️  前回と同一ファイルです！空打ちでトークン無駄遣いにならないように、確認してください！")
            results[repo_path] = False
            print()
            continue

        ok = push_file(local_file, repo, repo_path, sha)
        results[repo_path] = ok
        print()

    # ─── git pull（ファイル発見済みリポジトリ全て）──────────
    if pull_target_repos:
        print(f"{'─' * 50}")
        print("🔄 ローカルリポジトリを同期中...")
        for local_repo in pull_target_repos:
            git_pull_local(local_repo)
        print()

    # ─── サマリー ───────────────────────────────────────────
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
