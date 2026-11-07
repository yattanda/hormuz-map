# CLAUDE.md・Memory.md の索引型軽量化 — 設計と実施記録

- 作成：2026-11-07（クラウドセッション）
- 対象リポジトリ：`hormuz-map`（`hormuz-data-` は対象外）
- 基準コミット（分割前の原文）：`6175938`
- 状態：実施済み・**main 未マージ**（ブランチ `claude/intelligent-thompson-8v1rfn`）

## 1. 目的

- 毎セッション読み込まれる `CLAUDE.md` を、「どの作業でも要るルール」と「詳細の在りか（索引）」だけに絞る
- `Memory.md` を「サイトの技術・実装の索引」に改め、`STATUS.md` と重なっていた「現状・課題」を外す
- **ルールを1つも失わない**ことを機械で確かめられるようにする（§6）

## 2. 根拠（公式ドキュメント `https://code.claude.com/docs/en/memory`・2026-11-07 確認）

| 仕様 | 本設計での使い方 |
|---|---|
| 「target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence」 | ルートの上限を 200 行とした |
| `@path` で取り込んだファイルは起動時に一緒に読み込まれる | `@` は使わない（軽くならない） |
| `.claude/rules/*.md` に `paths:` を書くと、該当ファイルを扱うときだけ読み込まれる | ファイルで判定できるルールはここへ |
| ブロック単位の HTML コメントは読み込み時に取り除かれる | 保守メモはコメントで書く |
| `InstructionsLoaded` フック（load reason：`session_start`・`path_glob_match` など） | 実測の検証に使う（§6-2） |

確度：高（一次資料。`paths:` の動作は §7 で実測した）

## 3. 方針

1. **原文は消さずに移す。**ルートには要約を新たに書き、原文は詳細ファイルに置く。詳細ファイルが正
2. 振り分けの基準は「**いつ必要になるか**」

| 必要になる場面 | 置き場所 | 読み込み |
|---|---|---|
| すべての作業 | ルート `CLAUDE.md` | 起動時（毎回） |
| 特定のファイルを触るとき | `.claude/rules/*.md`（`paths:` 付き） | 該当ファイルを Read したとき（自動） |
| 特定の作業をするとき（ファイルでは判定できない） | `tools/rules/*.md` | ルートの索引の「きっかけ」で Claude が Read する |
| 経緯（判断には要らない） | `tools/history/*.md` | 必要なときだけ |

3. **ファイルをまたいで効くルールは、パス指定にしない。**例：「外部スクリプトを足したら `/privacy/` を見直す」は `/privacy/` 以外を編集するときに要るため、ルートに残した
4. 公開範囲：`tools/` は配信範囲外（GitHub Pages は `docs/` のみ）。移した内容は、もともと public の `CLAUDE.md`・`Memory.md` にあったもので、公開範囲は変わらない

## 4. 振り分け（CLAUDE.md）

| 原文の節 | 行き先 | ルートに残した要点 |
|---|---|---|
| 応答の基本・絶対ルール・触ってはいけないファイル・記録の置き場所・上位の方針文書・専門エージェント・font-size・Project Skills | ルート（原文のまま） | — |
| プロジェクト概要 | ルート。用語集の詳細5行は `.claude/rules/glossary.md`、ハブの地図の1行は `.claude/rules/hub-page.md` | 生成物の目印を手で編集しない（1行に集約） |
| スクリプトでファイルを書き換えるときのルール | `tools/rules/script-editing.md` | 5項目（経緯を外した） |
| Git操作ルール | ルート（2項目を短縮）。原文は `tools/rules/branch-and-pr.md` 付録 | — |
| ブランチルール（PC・スマホ） | `tools/rules/branch-and-pr.md` | 表・自動作成しない・マージは指示待ち・仮想ブランチ・Stop フック |
| Windows環境・Claude Code設定ルール | `tools/rules/windows-pc.md` | taskkill・deny を使わない・forward slash |
| 特別解説コラムの個別ページ化 | `.claude/rules/articles.md` | — |
| 法務ページ・ドメイン移行（実装を変えたら見直す を含む） | `.claude/rules/legal-pages.md` | 単独コミット・`/privacy/` 見直しのきっかけ |
| 所有権確認のために消してはいけないもの | `.claude/rules/hub-page.md` | GA4 タグ・`docs/CNAME` |
| セッション引き継ぎの保存先 | `tools/rules/handover.md` | 保存先・public に置かない・実値を書かない |
| hormuz-data- 連携ルール | `.claude/rules/hormuz-data-link.md` | — |
| Memory.mdとの役割分担 | ルート（書き直し） | — |

### `.claude/rules/` の `paths:`

| ファイル | paths |
|---|---|
| `legal-pages.md` | `docs/{about,contact,privacy,disclaimer,editorial,corrections}/**`・`tools/migrate-domain.sh`・`tools/migration-*.md` |
| `hub-page.md` | `docs/index.html`・`docs/CNAME`・`docs/assets/css/hub.css`・`tools/build_hub_map.py` |
| `articles.md` | `docs/hormuz/articles/**`・`docs/articles/**`・`tools/new-article-checklist.md`・`tools/article-template.html` |
| `glossary.md` | `docs/data/glossary.json`・`docs/glossary/**`・`docs/assets/glossary.js`・`tools/build_glossary.py`・`tools/glossary-search-design.md` |
| `hormuz-data-link.md` | `docs/hormuz/index.html`・`docs/data/**` |

## 5. 振り分け（Memory.md）

| 原文の節 | 行き先 |
|---|---|
| プロジェクト概要・環境メモ・セッション再開コマンド | `Memory.md`（原文のまま） |
| 現在の状態 | `tools/history/memory-state-log-2026-09-10.md`。仕組みは「仕組みの索引」に1行ずつ |
| 現在進行中・保留中・今後の最重要課題 | `tools/history/memory-issues-2026-05-09.md`。未解決の技術課題だけ要約 |
| 将来の構成方針・§11-10 の実施条件・新テーマの土台 | `tools/history/memory-future-structure-2026-09-21.md`。地図・用語集・GA4・focus の注意は「触るときの技術上の注意」へ |
| AIS／日次更新の運用移行／blockadeDay／完了済み主要作業 | `tools/history/memory-*.md` |

- 他の文書（`tools/s11-10-design.md`・`tools/phase2-sections-design.md` など）の「`Memory.md` の◯◯の節」という参照は書き換えていない。`Memory.md`「経緯の記録」の表で移した先を引ける
- `Memory.md`「環境メモ」の Claude.ai の行（「移行完了までは差分ファイル生成も担う」）は古い可能性がある。今回は原文のまま残した（**未確認**）

## 6. 検証のしかた

### 6-1. 静的な点検（毎回・数秒）

```bash
python3 tools/check_instructions.py
```

終了コード 0 で合格、1 で NG あり、2 で実行できない。点検するもの：

| 項目 | 内容 |
|---|---|
| size | ルート `CLAUDE.md`（コメント除く）が 200 行・9,000 字以内 |
| lossless | 基準コミットの `CLAUDE.md`・`Memory.md` の全行が、移した先のどこかに残っている。意図して削った行は `tools/instructions-check.json` の `dropped` に理由つきで載せる |
| required | 必ずルートに置く文言（捏造禁止・日付の実測・push の扱い・`/privacy/` 見直し など 26 項目）がある。エスケープの例文が絵文字に化けていない |
| rules | `.claude/rules/*.md` に `paths:` があり、各パターンに当たる追跡ファイルが1つ以上ある |
| index | ルートの索引が参照するファイルが実在し、索引から参照されないルールファイルが無い |
| link | `Memory.md` が参照するファイルが実在する（詳細ルールの欠けは WARN） |

- ルールを書き足したら、ルートに置くべきものは `required_in_root` にも足す
- 今後 `CLAUDE.md` を直すたびに lossless で `dropped` が増えるのは手間なので、次に大きく直すときに `baseline_commit` を新しいコミットへ進める

### 6-2. 実測（ルールを足した・paths を変えたとき）

```bash
python3 tools/check_instructions.py --live
```

- `claude -p`（既定 haiku）を対象ごとに1回起動し、対象ファイルを Read させる。`InstructionsLoaded` フックの記録で、ルールが `path_glob_match` で読み込まれたこと、起動時（`session_start`）には読み込まれていないことを確かめる
- 関係ないファイル（`README.md`）を読んだときにどのルールも読み込まれないことも確かめる
- 利用枠を少し使う（6回起動）。クラウドでも PC でも動く（`claude` がパスにあること）
- 作業ツリーは書き換えない（`--allowedTools Read` のみ）

### 6-3. 目視（PC で一度）

- PC の Claude Code で `/status`（または `/memory`）を開き、長さの警告が出ないこと、Memory files にルートの `CLAUDE.md` だけが出ることを見る
- 法務ページを開いて「このページのルールを要約して」と頼み、`legal-pages.md` の中身が答えに出ることを見る

## 7. 実施結果（2026-11-07）

| 指標 | 前 | 後 |
|---|---|---|
| ルート `CLAUDE.md`（毎回読み込まれる分） | 15,930字・367行 | **約8,200字・194行（コメント除く）**（約49%減） |
| 起動時に読み込まれるルールファイル | — | 0（`.claude/rules/` 5本はすべて必要時のみ） |
| `Memory.md` | 34,921字・776行 | 6,254字・104行 |

- 静的な点検：size・lossless（抜け 0）・required 26/26・rules・index とも合格
- 実測（`--live`）：5本すべて `path_glob_match` で読み込まれ、`session_start` での読み込みは無かった。`README.md` ではどれも読み込まれなかった
- 作業中に起きたこと：ルート `CLAUDE.md` を書き出したとき、例文のエスケープ（バックスラッシュ＋`ud83c`…）が国旗の絵文字に化けた。気づいて直し、`required` の点検に検出を入れた

## 8. 残る弱点と次の候補

- `tools/rules/` は「Claude が索引を見て自分で Read する」前提のため、読み忘れの可能性がある（`paths:` のような強制力は無い）。気になる項目は要点をルートに残してある。読み忘れが実際に起きたら、その要点をルートへ戻す
- 日次更新では `docs/hormuz/index.html` を読むため、`hormuz-data-link.md` は毎回読み込まれる（約1,000字。許容）
- 候補：`/daily-site-update` などスキル側の重複も同じ方法で点検できる（今回は対象外）
- PC 側のグローバル `~/.claude/CLAUDE.md` との重複（「応答の基本」）は、クラウドに引き継がれないため残している
