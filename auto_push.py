"""
auto_push.py  ― hormuz-map 自動push スクリプト
改訂: 2026-04-30
変更点:
  - ファイル名を完全固定（完全一致のみ・正規表現リモート無効化オプション追加）
  - ファイルサイズ上限チェック（MAX_FILE_SIZE_KB）
  - 空ファイル拒否
  - GITHUB_TOKEN / github_pat_ / ghp_ を含むファイルはpush拒否
  - push前に対象ファイル名・サイズを表示
  - 前回と同一ファイル（差分なし）の場合は警告を表示
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

# push先リポジトリ内パス → ローカルの「完全固定」ファイル名
FILE_MAP = {
    "data/news_data.json":  "news_data.json",
    "index_html_diffs.md":  "index_html_diffs.md",
}

DOWNLOADS_DIR = Path(r"C:\Users\yutay\Downloads")

# ─── レート設定 ──────────────────────────────────────────────
# [2] ファイルサイズ上限（KB）。これを超えるファイルはpush拒否
MAX_FILE_SIZE_KB = 512  # 512KB = 十分な上限（JSON/MDとして異常に大きい場合を弾く）

# トークン漏洩ガード用キーワード
# [4] これらの文字列がファイル内容に含まれる場合はpush拒否
TOKEN_PATTERNS = [
    "GITHUB_TOKEN",
    "github_pat_",
    "ghp_",
]
# ─────────────────────────────────────────────────────────────


def find_exact_file(exact_name: str) -> Path | None:
    """
    [1] ファイル名を完全固定：Downloadsから exact_name に完全一致するファイルのみ返す。
    「news_data (1).json」のような類似ファイルは一切拾わない。
    """
    target = DOWNLOADS_DIR / exact_name
    if target.exists() and target.is_file():
        return target
    return None


def check_file_safety(local_path: Path) -> tuple[bool, str]:
    """
    [2][3][4] ファイルの安全チェック。
    戻り値: (OK: bool, エラーメッセージ: str)
    """
    # [3] 空ファイル拒否
    size_bytes = local_path.stat().st_size
    if size_bytes == 0:
        return False, "空ファイルのため push を中断します。"

    # [2] ファイルサイズ上限チェック
    size_kb = size_bytes / 1024
    if size_kb > MAX_FILE_SIZE_KB:
        return False, (
            f"ファイルサイズ {size_kb:.1f} KB が上限 {MAX_FILE_SIZE_KB} KB を超えています。"
            " 誤ったファイルを指定している可能性があります。"
        )

    # [4] トークン漏洩チェック
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
    """
    [6] ローカルファイルとGitHub上のファイルが同一かどうかをハッシュで比較。
    """
    if remote_bytes is None:
        return False  # リモートに存在しない = 新規ファイル → 差分あり扱い
    local_bytes = local_path.read_bytes()
    return hashlib.sha256(local_bytes).digest() == hashlib.sha256(remote_bytes).digest()


def push_file(local_path: Path, repo_path: str, sha: str | None) -> bool:
    """ファイルをGitHub APIでpushする。成功時True。"""
    url     = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{repo_path}"
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
    for repo_path, exact_name in FILE_MAP.items():

        print(f"{'━'*50}")
        print(f"🔍 [{exact_name}] を検索中...")

        # [1] 完全一致のみ
        local_file = find_exact_file(exact_name)

        if local_file is None:
            print(f"  ⚠   ファイルが見つかりません: {exact_name}  → スキップ\n")
            results[repo_path] = False
            continue

        # [5] push前にファイル名・サイズを表示
        size_kb = local_file.stat().st_size / 1024
        print(f"  📄 対象ファイル : {local_file.name}")
        print(f"     フルパス     : {local_file}")
        print(f"     ファイルサイズ: {size_kb:.1f} KB")

        # [2][3][4] 安全チェック
        ok, err_msg = check_file_safety(local_file)
        if not ok:
            print(f"  ❌ {err_msg}")
            results[repo_path] = False
            print()
            continue

        # リモート情報取得（SHA + コンテンツ）
        sha, remote_bytes = get_remote_sha_and_content(repo_path)

        # [6] 差分チェック
        if files_are_identical(local_file, remote_bytes):
            print()
            print("  ⚠️  前回と同一ファイルです（空撃ちでトークン無駄遣いにならないよう確認してください）")
            print()
            results[repo_path] = False
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
