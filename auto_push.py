#!/usr/bin/env python3
"""
auto_push.py
ダウンロードフォルダの2ファイルをGitHub APIで直接pushするスクリプト
使い方: python auto_push.py
"""

import os
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

# ===== 設定 =====
DOWNLOADS = Path.home() / "Downloads"
REPO      = "yattanda/hormuz-map"
BRANCH    = "main"
FILES = [
    ("news_data.json",       "data/news_data.json"),
    ("index_html_diffs.md",  "index_html_diffs.md"),
]
# ================

def load_token():
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        raise FileNotFoundError(".envファイルが見つかりません")
    for line in env_path.read_text().splitlines():
        if line.startswith("GITHUB_TOKEN="):
            return line.split("=", 1)[1].strip()
    raise ValueError(".envにGITHUB_TOKENが見つかりません")

def github_api(method, path, token, body=None):
    url = f"https://api.github.com/repos/{REPO}/{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"GitHub API エラー {e.code}: {e.read().decode()}")

def push_file(token, local_path, repo_path):
    content = base64.b64encode(local_path.read_bytes()).decode()
    # 既存ファイルのSHAを取得
    sha = None
    try:
        res = github_api("GET", f"contents/{repo_path}", token)
        sha = res.get("sha")
    except RuntimeError:
        pass  # 新規ファイルの場合はSHA不要

    body = {
        "message": f"update: {repo_path}",
        "content": content,
        "branch": BRANCH,
    }
    if sha:
        body["sha"] = sha

    github_api("PUT", f"contents/{repo_path}", token, body)
    print(f"  ✅ {repo_path} → pushed")

def main():
    print("=" * 40)
    print("  ホルムズマップ 自動push")
    print("=" * 40)

    try:
        token = load_token()
    except Exception as e:
        print(f"❌ トークン読み込み失敗: {e}")
        input("Enterで終了...")
        return

    errors = []
    for local_name, repo_path in FILES:
        local_path = DOWNLOADS / local_name
        if not local_path.exists():
            print(f"  ⚠️  スキップ: {local_name} がDownloadsに見つかりません")
            errors.append(local_name)
            continue
        try:
            push_file(token, local_path, repo_path)
        except Exception as e:
            print(f"  ❌ {repo_path} の push 失敗: {e}")
            errors.append(local_name)

    print("-" * 40)
    if errors:
        print(f"⚠️  {len(errors)}件をスキップまたは失敗しました")
    else:
        print("🎉 全ファイルのpushが完了しました！")
        print("   GitHub Pages に反映されるまで1〜2分かかります")
    print("=" * 40)
    input("Enterで終了...")

if __name__ == "__main__":
    main()