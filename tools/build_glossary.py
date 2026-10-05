#!/usr/bin/env python3
"""用語集ページ（docs/glossary/index.html）を docs/data/glossary.json から書き出す。

  python tools/build_glossary.py            何も書かない（検査して、変わる行数だけ出す）
  python tools/build_glossary.py --write    書く
  python tools/build_glossary.py --check    ページが JSON と一致していなければ終了コード 1

書き換えるのは目印の間だけ：
  <!-- glossary:start --> 〜 <!-- glossary:end -->                 本文（最終更新・目次・用語）
  <!-- glossary-jsonld:start --> 〜 <!-- glossary-jsonld:end -->   構造化データ
目印の間を手で編集しない。<head>・ヘッダー・フッターは手で書いた HTML をそのまま残す。

検査に1つでも掛かれば終了コード 1 で、ファイルには触らない。
設計：tools/glossary-search-design.md §11
"""
import html
import json
import os
import re
import sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "docs", "data", "glossary.json")
PAGE = os.path.join(ROOT, "docs", "glossary", "index.html")
BASE_URL = "https://chokepointlab.com/glossary/"

CATEGORIES = [
    ("org", "組織"),
    ("place", "地名・施設"),
    ("market", "原油・市場"),
    ("ship", "船舶・海運"),
    ("military", "軍事・外交"),
    ("site", "このサイトの用語"),
]
DRAFT_MARKS = ("【要確認】", "【未確認】", "【検索】", "【取得】")
SHORT_MAX = 80
SITE_BADGE = "このサイト独自の用語"      # docs/assets/glossary.js のポップアップにも同じ文言がある
SITE_NOTE_LABEL = "このサイトでは"

BODY_START, BODY_END = "<!-- glossary:start -->", "<!-- glossary:end -->"
LD_START, LD_END = "<!-- glossary-jsonld:start -->", "<!-- glossary-jsonld:end -->"


def validate(data):
    """検査。問題の一覧（文字列）を返す。空なら合格。"""
    errs = []
    terms = data.get("terms")
    if not isinstance(terms, list):
        return ["terms が配列ではない"]
    cats = {c for c, _ in CATEGORIES}
    ids, words = set(), {}
    for i, t in enumerate(terms):
        tid = t.get("id", "")
        where = f"{i + 1}番目（{tid or '?'}）"
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", tid):
            errs.append(f"{where}：id は英小文字・数字・ハイフンだけにする")
        if tid in ids:
            errs.append(f"{where}：id が重複している")
        ids.add(tid)
        for key in ("term", "reading", "short", "updated"):
            if not isinstance(t.get(key), str) or not t[key].strip():
                errs.append(f"{where}：{key} が空")
        if t.get("updated") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", t["updated"]):
            errs.append(f"{where}：updated は YYYY-MM-DD で書く")
        if t.get("category") not in cats:
            errs.append(f"{where}：category が不明（{t.get('category')}）")
        body = t.get("body")
        if not isinstance(body, list) or not body or not all(isinstance(p, str) and p.strip() for p in body):
            errs.append(f"{where}：body は空でない段落の配列にする")
        note = t.get("site_note", [])
        if not isinstance(note, list) or not all(isinstance(p, str) and p.strip() for p in note):
            errs.append(f"{where}：site_note は空でない段落の配列にする")
        if len(t.get("short", "")) > SHORT_MAX:
            errs.append(f"{where}：short が{SHORT_MAX}字を超えている（{len(t['short'])}字）")
        for w in list(t.get("match", [])) + list(t.get("aliases", [])):
            if not isinstance(w, str) or not w.strip():
                errs.append(f"{where}：match／aliases に空の表記がある")
            elif w in words and words[w] != tid:
                errs.append(f"{where}：表記「{w}」が {words[w]} と重複している")
            else:
                words[w] = tid
        sources = t.get("sources", [])
        if not sources and t.get("category") != "site":
            errs.append(f"{where}：出典が無い（出典なしで載せられるのは「このサイトの用語」だけ）")
        for s in sources:
            if not str(s.get("label", "")).strip():
                errs.append(f"{where}：出典の表示名が空")
            if not re.match(r"https?://", str(s.get("url", ""))):
                errs.append(f"{where}：出典の URL が http(s):// で始まらない")
        text = json.dumps([t.get("term"), t.get("short"), body, note, sources], ensure_ascii=False)
        for mark in DRAFT_MARKS:
            if mark in text:
                errs.append(f"{where}：原稿の印 {mark} が残っている")
    for t in terms:
        for r in t.get("related", []):
            if r not in ids:
                errs.append(f"{t.get('id')}：related の {r} が存在しない")
    return errs


def esc(s):
    return html.escape(str(s), quote=True)


def jp_date(iso):
    y, m, d = iso.split("-")
    return f"{int(y)}年{int(m)}月{int(d)}日"


def render_body(data):
    terms = data["terms"]
    if not terms:
        return "<p>用語集は準備中です。</p>"
    by_id = {t["id"]: t for t in terms}
    updated = max(t["updated"] for t in terms)
    out = [f'<p class="updated">最終更新：{jp_date(updated)}　／　{len(terms)}語</p>']

    groups = []
    for key, name in CATEGORIES:
        items = sorted((t for t in terms if t["category"] == key), key=lambda t: t["reading"])
        if items:
            groups.append((key, name, items))

    out.append('<nav class="gl-toc" aria-label="用語の目次">')
    for key, name, items in groups:
        links = "".join(f'<a href="#term-{esc(t["id"])}">{esc(t["term"])}</a>' for t in items)
        out.append(f'<p><a class="gl-toc-cat" href="#cat-{key}">{esc(name)}</a>{links}</p>')
    out.append("</nav>")

    for key, name, items in groups:
        out.append("")
        out.append(f'<h2 id="cat-{key}">{esc(name)}</h2>')
        out.append("<dl>")
        for t in items:
            # このサイト独自の用語は、見出しの横に札を付けて一般の用語と区別する
            badge = f' <span class="gl-badge">{SITE_BADGE}</span>' if t["category"] == "site" else ""
            out.append(f'<dt id="term-{esc(t["id"])}">{esc(t["term"])}{badge}</dt>')
            out.append("<dd>")
            out.append(f'<p class="gl-short">{esc(t["short"])}</p>')
            for p in t["body"]:
                out.append(f"<p>{esc(p)}</p>")
            # 一般の説明と、このサイトでの使い方を分けて見せる
            if t.get("site_note"):
                out.append('<div class="gl-site">')
                out.append(f'<p class="gl-site-label">{SITE_NOTE_LABEL}</p>')
                for p in t["site_note"]:
                    out.append(f"<p>{esc(p)}</p>")
                out.append("</div>")
            if t.get("sources"):
                out.append('<ul class="gl-src">')
                for s in t["sources"]:
                    out.append(f'<li><a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s["label"])}</a></li>')
                out.append("</ul>")
            related = [by_id[r] for r in t.get("related", []) if r in by_id]
            if related:
                links = "、".join(f'<a href="#term-{esc(r["id"])}">{esc(r["term"])}</a>' for r in related)
                out.append(f'<p class="gl-rel">関連する用語：{links}</p>')
            if t.get("match") and t.get("synonyms") is False and len(t["match"]) > 1:
                # 表記どうしが同義語でない語は、検索が別表記へ広がらない。表記ごとにリンクを出す
                links = "・".join(f'<a href="../archive/#q={quote(w, safe="")}">「{esc(w)}」</a>' for w in t["match"])
                out.append(f'<p class="gl-arch">日次記録を見る：{links}</p>')
            elif t.get("match"):
                q = quote(t["match"][0], safe="")
                out.append(f'<p class="gl-arch"><a href="../archive/#q={q}">この用語を含む日次記録を見る →</a></p>')
            out.append("</dd>")
        out.append("</dl>")
    return "\n".join(out)


def render_jsonld(data):
    ld = {
        "@context": "https://schema.org",
        "@type": "DefinedTermSet",
        "@id": BASE_URL,
        "name": "用語集｜チョークポイント・ラボ",
        "url": BASE_URL,
        "inLanguage": "ja",
        "hasDefinedTerm": [
            {"@type": "DefinedTerm", "name": t["term"], "description": t["short"],
             "url": f"{BASE_URL}#term-{t['id']}", "inDefinedTermSet": BASE_URL}
            for t in data["terms"]
        ],
    }
    text = json.dumps(ld, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{text}\n</script>'


def replace_between(page, start, end, inner):
    if page.count(start) != 1 or page.count(end) != 1:
        raise ValueError(f"目印が1組ではない：{start}")
    a = page.index(start) + len(start)
    b = page.index(end)
    if a > b:
        raise ValueError(f"目印の順番が逆：{start}")
    return page[:a] + "\n" + inner + "\n" + page[b:]


def main(argv):
    write = "--write" in argv
    check = "--check" in argv
    try:
        data = json.loads(open(DATA, "rb").read().decode("utf-8"))
    except (OSError, ValueError) as e:
        print(f"NG  glossary.json を読めない：{e}")
        return 1
    errs = validate(data)
    if errs:
        for e in errs:
            print("NG ", e)
        return 1

    try:
        old = open(PAGE, "rb").read().decode("utf-8")
        page = old.replace("\r\n", "\n")
        page = replace_between(page, BODY_START, BODY_END, render_body(data))
        page = replace_between(page, LD_START, LD_END, render_jsonld(data))
    except (OSError, ValueError) as e:
        print(f"NG  {e}")
        return 1
    # 改行は既存のファイルに合わせる。PC の作業ツリーは CRLF、クラウド（Linux）の checkout は LF で、
    # 常に CRLF にすると LF の環境で --check が必ず不一致になる
    new = page.replace("\n", "\r\n") if "\r\n" in old else page
    new_bytes = new.encode("utf-8")         # 先にエンコードできることを確かめる

    count = len(data["terms"])
    if new == old:
        print(f"OK  用語集ページは glossary.json と一致（{count}語）")
        return 0
    changed = sum(1 for a, b in zip(old.splitlines(), new.splitlines()) if a != b) \
        + abs(len(old.splitlines()) - len(new.splitlines()))
    if check:
        print(f"NG  用語集ページが glossary.json と食い違っている（{changed}行）。"
              "python tools/build_glossary.py --write で書き出す")
        return 1
    if not write:
        print(f"dry-run：{count}語・{changed}行が変わる（--write で書く）")
        return 0
    tmp = PAGE + ".tmp"
    with open(tmp, "wb") as f:
        f.write(new_bytes)
    os.replace(tmp, PAGE)
    print(f"OK  docs/glossary/index.html を書き出した（{count}語・{changed}行）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
