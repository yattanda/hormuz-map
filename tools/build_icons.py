"""分類の札のアイコン（CSS の mask）を docs/assets/icons/icons.svg から書き出す（課題46 D3 PR 5b）。

アイコンの正本は icons.svg の <symbol> だけ。札の ::before は <use> を使えないので、
A の簡略版（a-*・1色）を data URI にして hormuz.css の印の間に書き込む。手で書き換えない。

  python tools/build_icons.py          # 書き込む
  python tools/build_icons.py --check  # 書き込まずに、いまの CSS と同じかを見る（違えば終了コード 1）
"""
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPRITE = ROOT / "docs/assets/icons/icons.svg"
CSS = ROOT / "docs/assets/css/hormuz.css"
BEGIN = "/* cat-icons:begin（tools/build_icons.py が書き出す。手で書き換えない） */"
END = "/* cat-icons:end */"

# 分類の札（設計書 §2-2）：クラス → A の記号。外交は文字だけ
CATS = [
    ("cat-sea", "a-tanker"),     # 海上
    ("cat-attack", "a-hit"),     # 攻撃
    ("cat-mil", "a-warship"),    # 軍事
    ("cat-oil", "a-barrel"),     # 原油・市場
    ("cat-other", "a-general"),  # その他
]


def symbol_svg(sprite: str, sym_id: str) -> str:
    m = re.search(r'<symbol id="' + re.escape(sym_id) + r'" viewBox="([^"]+)">(.*?)</symbol>', sprite, re.S)
    if not m:
        sys.exit(f"{SPRITE.name} に {sym_id} がありません")
    body = re.sub(r"\s*\n\s*", "", m.group(2)).replace("var(--a)", "#000")
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{m.group(1)}">{body}</svg>'


def data_uri(svg: str) -> str:
    return "data:image/svg+xml," + urllib.parse.quote(svg.replace('"', "'"), safe=" ='/:,.")


def build() -> str:
    sprite = SPRITE.read_text(encoding="utf-8")
    lines = [BEGIN]
    for cls, sym in CATS:
        lines.append(f'.{cls} {{ --cat-icon:url("{data_uri(symbol_svg(sprite, sym))}"); }}')
    lines.append(END)
    return "\n".join(lines)


def main() -> None:
    # 外から <use href="icons.svg#…"> で読むので、ブラウザが XML として読めること（コメントの「--」など）を確かめる
    import xml.dom.minidom
    try:
        xml.dom.minidom.parse(str(SPRITE))
    except Exception as e:  # noqa: BLE001
        sys.exit(f"{SPRITE.name} が XML として読めません（{e}）。<use> で参照すると絵が出ない")
    css = CSS.read_text(encoding="utf-8")
    pat = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
    if not pat.search(css):
        sys.exit(f"{CSS.name} に書き出しの印（cat-icons:begin／end）がありません")
    new = pat.sub(lambda _: build(), css)
    if "--check" in sys.argv:
        if new != css:
            print("hormuz.css の分類の札のアイコンが icons.svg と食い違っています。python tools/build_icons.py を実行してください")
            sys.exit(1)
        print("OK")
        return
    CSS.write_text(new, encoding="utf-8")
    print(f"{CSS.relative_to(ROOT)} に {len(CATS)} 個を書き出しました")


if __name__ == "__main__":
    main()
