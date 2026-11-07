# セッション引き継ぎの保存先（詳細）

> 2026-11-07 にルートの `CLAUDE.md` から原文のまま移した（設計書 `tools/claude-md-slim-design.md`）。
> ルートには要点だけを残している。食い違ったら**この文書が正**。

## セッション引き継ぎの保存先

- **引き継ぎノートは private リポジトリ `yattanda/hormuz-ops` の `handovers/` に置く。**
  ローカルでは `~/Documents/GitHub/hormuz-ops/handovers/` に相当する
- `/handover` を実行する場合も保存先はここ。**この指定はグローバルの
  `~/.claude/commands/handover.md` の既定（`.claude/handovers/`）より優先する**
- `hormuz-map/.claude/handovers/` は **2026-09-04 に削除済み**。
  過去14ファイルは `hormuz-ops/handovers/` へ移設した。ここに再び作らない
- ファイル名は `YYYY-MM-DD_HHmm.md`。追加したら `handovers/INDEX.md` に1行足す

### なぜ別リポジトリなのか

`hormuz-map` と `hormuz-data-` はどちらも **public** で、引き継ぎには
上流の戦略・法務判断・第三者とのやり取り・運用上の弱点が入り込む。
一方、ローカルにしか無いとクラウドセッション（Claude Code on the Web）から
読めず、PC が手元に無いときに作業を継続できない。
「どこからでも読める」と「公開しない」を両立させるための構成。

### クラウドセッションからの参照

セッションの対象リポジトリが `hormuz-map` でも読める。
**2026-09-04 にクラウドセッションから実測で確認済み。**

手順は次のとおり。**`gh` CLI はクラウド環境に入っていない**ので使えない。

1. 既定ではセッションのリポジトリスコープが対象リポジトリのみのため、
   `hormuz-ops` へのアクセスは拒否される
2. `add_repo` で `yattanda/hormuz-ops` を **read 権限で**セッションに追加する
3. GitHub MCP のファイル取得ツール（`get_file_contents`）で
   `handovers/INDEX.md` を読む

クラウドセッションにはこう頼めばよい。

```
private リポジトリ yattanda/hormuz-ops を read で追加して、
handovers/INDEX.md を読んで現状を把握して。変更・コミットはしないこと。
```

`add_repo` はそのセッションのスコープに `hormuz-ops` を追加する。
読み取り専用で追加すること。

### クラウドセッションから書き込むとき

- **`hormuz-ops` を write 権限で `add_repo` してから書く。**read で追加した場合は書けない
- 書き込みは GitHub MCP の `create_or_update_file` で `hormuz-ops` の main へ直接行う
  （このリポジトリは運用メモ専用で公開物が無いため、PR を経由しなくてよい）
- **書き込めなかった場合、`hormuz-map` や `hormuz-data-` に代わりにコミットしてはならない。**
  この2つは public であり、引き継ぎを置くと分離した意味が消える。
  書けないときは**引き継ぎの全文をチャットに出力し**、ユーザーが手元で保存できるようにする
- 長い作業では、最後にまとめて書こうとせず**途中で一度書き込んで経路を確かめる**

### 書くときのルール

- **API キー・トークンの実値は書かない。**private であっても書かない。
  Secret 名（`GEMINI_API_KEY` 等）までは可
- 複数リポジトリにまたがる作業では、どのリポジトリの話かを冒頭に明記する
- それ単体で読めるように書く。他のノートを読まないと意味が通らない書き方をしない
