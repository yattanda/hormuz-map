---
name: site-design
description: Visual design rules for the chokepoint-lab site (color tokens, fonts, the three icon types, dividers, what not to use) / サイトの見た目の決まり（色のトークン・書体・アイコン3種類の使い分け・区切り方・使わないもの）。HTML・CSS・JS の見た目に触る前に読む
---

# サイトの見た目の決まり（課題46）

このスキルは、ページの HTML・CSS・JS の見た目（色・書体・アイコン・区切り・地図の印）を作る・直すときに使用する。
決定と経緯の正本は設計書 `tools/site-redesign-design.md`（§1 画面の作法・§2 アイコン・§3 なくすもの・§4 色・§4-1 書体・§4-2 地図）。ここには、手を動かすときに守ることだけを書く。
決まった色や書体を変えたいときは、変える前に案として運営者に出す（勝手に値を替えない）。

## 考え方

題材は艦艇の識別表と航路標識。区切り方と状態の示し方をそこから借りる。飾りは足さない。
迷ったら「識別表にこれはあるか」で決める。

## 色

- 色は `docs/assets/css/tokens.css` の変数だけを使う。16進・`rgb()`・色名を CSS・`style=""`・JS のテンプレートに直に書かない（`validate_daily.py` の `check_colors()` が WARN を出す）
- 地 `--c-bg`・面 `--c-surface`（帯と札の下地だけ）・本文 `--c-text`・補助の文字（日付・出典）`--c-text-mute`・細い罫 `--c-rule`
- 差し色 `--c-accent` はアイコンと小見出しだけ。面の上では文字に使わない。差し色の面（ボタン）の文字は `--c-on-accent`
- 大きな数字は `--c-figure`（主要な数字だけ）
- リンクは `--c-text`＋下線（青いリンク色は無い）。本文の強調は `--c-text` の太字
- 状態の4色は**状態を示すときだけ**、必ず面（札）にして、状態を文でも書く。札の文字は `--c-on-*`
  - 危険（停止・攻撃）＝赤 `--c-danger`／警戒（制限下）＝橙 `--c-alert`／注記（復旧途上・未確認）＝黄 `--c-warn`／平常（回復・増加）＝緑 `--c-ok`／判断なし＝枠だけ
  - シナリオは A 緑・B 黄・C 橙・D 赤（`sc-tag-A`〜`D` の id で CSS が塗る）
  - 赤・緑を文字の色にしない。飾りのために4色を使わない。黄色の文（以前の `--c-warn-soft`）も使わない
- 地図の色は `--map-*`（§4 の10色の外・地図だけ）。ルートの線は `--map-route-*` で、状態の4色と取り違えない色で組んである
- 直書きが許されている例外は、地図を CARTO に戻したときの色（`hormuz.css` の `.map-label*`・`/hormuz/` の JS の `BASEMAP === 'carto'` の側）、ハブの地図の陸（`hub.css` の `.hub-map-land`）、`<meta name="theme-color">`、Leaflet 本体（`docs/assets/vendor/`）だけ。増やすときは `validate_daily.py` の `CSS_COLOR_ALLOWED`・`JS_MAP_CARTO_COLORS` にも足し、理由をコメントに書く
- トークンの名前を変える・外すときは、各ページが `tokens.css` に付けている `?v=` を進める（古い `tokens.css` がブラウザに最大 600 秒残り、新しい HTML と組むと色が戻るため・D3 PR 7a）

## 書体

- 本文は BIZ UDPゴシック（400・700）＝`--f-body`。大きな数字と段の見出しの英字は IBM Plex Sans Condensed（500・600）＝`--f-figure`。文中の数字は本文の書体のまま
- 書体は自サイトから配る（`/assets/fonts/biz-udpgothic/biz-udpgothic.css`）。Google Fonts へつながない（`validate_daily.py` が NG にする）
- 数字は `font-variant-numeric: tabular-nums` で桁をそろえる

## 区切り

- 段は太い罫（上に3px・`--c-text`）、段の中は細い罫（`--c-rule`）
- 箱・角丸・影・グラデーションで区切らない。左端の色帯だけのカードも作らない
- 見出しと本文は左寄せ
- 数字の下に「いつ時点・どこの発表か」を必ず置く

## アイコン

絵はすべて `docs/assets/icons/icons.svg` の `<symbol>`。`<svg><use href="/assets/icons/icons.svg#…"/></svg>` で使う。

| 種類 | 記号 | 使う場所 | 大きさ |
|---|---|---|---|
| A 識別シルエット（1色・簡略版） | `a-*` | 文の中、一覧の行頭、表の中、分類の札 | 16〜24px |
| B 塗り分け | `i-*` | 見出し、カード、記事の入口（コラムのカード 40px・記事一覧のカード 32px） | 28px 以上 |
| C 徽章 | 台 `i-disc`＋A | 地図の印と凡例、ロゴまわり、favicon、`og:image`、サムネイル | 24px 以上（地図の印は危険 32px・ほか 26px） |

- 題材は12：`tanker`・`warship`・`mine`・`anchor`・`barrel`・`strait`・`hit`・`refinery`・`tank`・`report`・`speaker`・`general`（使い場所は設計書 §2-1）
- 地図の印は `mkBadge(状態, 題材)`（`docs/hormuz/index.html`）で作る。台 `i-disc` だけを置かない（題材を描き忘れた印と区別がつかない）。都市・島・岬・湖には題材を作らない（共通の印＋地名、湖は地名だけ）
- 速報・ニュースの分類は札の語（海上・攻撃・軍事・原油・市場・外交・その他）。型と添える A は `daily-site-update` の「分類の札」
- 新しい絵を勝手に描き足さない（形の揃いが崩れる）。題材が一式にないときは文字だけにして、足りない題材を報告に書く。足すときは B と A の簡略版の2つを作り、16px・20px で形が残るか確かめる（設計書 §2）

## 絵文字と記号

- 絵文字を使わない（見出しの頭・アイコン代わり・状態の色丸 🔴🟠🟡🟢 とも）。国旗の絵文字も使わず、国名の文字で書く
- 過去のデータ（`news_data.json`・`incident_archive.json` など）の絵文字は書き換えず、表示のときに JS が札に読み替える
- 残してよい記号：🅐〜🅓（シナリオの補足の行頭）・✕（閉じるボタン）・★（日本の受入拠点の説明）・✦（トランプ声明の枠）・▶◀◈・矢印。増減は ↑↓（▲▼ は開閉の記号だけ）
- `/corrections/` の 🇺🇸🌍🚢 は過去の表示の引用なので残す
- `validate_daily.py` の `check_emoji()` が、全ページの表示される文とその日に足したデータの絵文字を WARN にする。例外を増やすときは `EMOJI_ALLOWED` に足し、この節も直す

## 使わないもの（設計書 §3）

Tailwind の既定色（`#1e293b`・`#38bdf8`・`#94a3b8`・`#fbbf24` など）／トークンにない色／絵文字／装飾のグラデーション・影・角丸のカード・左端の色帯／中央寄せの見出しと本文。

## 確かめ方

- PC（1280px）・タブレット（768px）・スマホ（375〜390px）で見る。横スクロールが出ないこと
- 文字のコントラスト比は 4.5 以上（値ごとの比は `tokens.css` のコメントと設計書 §4）
- 見た目を変えない直しは、`tools/visual_check.py`（`shoot`・`diff`）で `main` と画素を比べる
- `python tools/validate_daily.py` で、絵文字・トークン外の色・頭の絵文字と分類の札・書体の読み込み元が WARN・NG を出さないこと
- 関連：HTML の構造と JS の制約は `html-safe-edit`、表記は `content-style-guide`、日次の型は `daily-site-update`。レスポンシブの基準と余白は `tools/design-system.md`
