"""
auto_push.py  ― hormuz-map 自動push スクリプト
改訂: 2026-04-28
変更点: Downloads内に同名ファイルが複数存在する場合（例: news_data (1).json）、
        最終更新時刻が最新のものを自動選択し、古いものを削除する。
"""

import os
import re
import glob
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
    "data/news_data.json":     "news_data.json",
    "index_html_diffs.md":     "index_html_diffs.md",
}

DOWNLOADS_DIR = Path(r"C:\Users\yutay\Downloads")
# ─────────────────────────────────────────────────────────────


def find_latest_file(base_name: str) -> Path | None:
    """
    Downloadsフォルダから base_name に対応する最新ファイルを返す。

    マッチパターン（例: base_name = "news_data.json"）
      news_data.json
      news_data (1).json
      news_data (2).json
      news_data(1).json      ← スペースなし variant
    """
    stem, suffix = os.path.splitext(base_name)   # "news_data", ".json"

    # glob で候補を収集（大小文字区別なし対応のため lower 比較）
    all_files = list(DOWNLOADS_DIR.iterdir())
    pattern   = re.compile(
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
    old_files = candidates[1:]
    for old in old_files:
        try:
            old.unlink()
            print(f"  🗑  削除: {old.name}  (古い重複)")
        except Exception as e:
            print(f"  ⚠  削除失敗: {old.name} ({e})")

    return newest


def get_sha(repo_path: str) -> str | None:
    """GitHub上の既存ファイルSHAを取得（更新時に必要）。"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{repo_path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.get(url, headers=headers, timeout=15)
    if resp.status_code == 200:
        return resp.json().get("sha")
    return None


def push_file(local_path: Path, repo_path: str) -> bool:
    """ファイルをGitHub APIでpushする。成功時True。"""
    url     = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{repo_path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type":  "application/json",
    }
    content_b64 = base64.b64encode(local_path.read_bytes()).decode()
    sha = get_sha(repo_path)

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
        print(f"🔍 {base_name} を検索中...")
        local_file = find_latest_file(base_name)

        if local_file is None:
            print(f"  ⚠  ファイルが見つかりません: {base_name}  → スキップ\n")
            results[repo_path] = False
            continue

        print(f"  📄 使用するファイル: {local_file.name}")
        print(f"     更新時刻: {local_file.stat().st_mtime:.0f}")
        ok = push_file(local_file, repo_path)
        results[repo_path] = ok
        print()

    # サマリー
    print("─" * 40)
    success = sum(v for v in results.values())
    total   = len(results)
    print(f"完了: {success}/{total} ファイル push成功")
    if success < total:
        failed = [k for k, v in results.items() if not v]
        print("失敗:", ", ".join(failed))
    print("─" * 40)


if __name__ == "__main__":
    main()
