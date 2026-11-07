#!/usr/bin/env python3
"""指示ファイル（CLAUDE.md・.claude/rules/・tools/rules/・Memory.md）の分割を点検する。

設計書：tools/claude-md-slim-design.md §6。設定：tools/instructions-check.json。
読み取り専用（--live でも作業ツリーは書き換えない）。

  python3 tools/check_instructions.py            # 静的な点検（数秒）
  python3 tools/check_instructions.py --live     # 加えて Claude Code を起動し、ルールが実際に読み込まれるか確かめる
  python3 tools/check_instructions.py --base <commit>   # 原文の基準コミットを変える

終了コード：0 合格／1 NG あり／2 実行できない（git が無い・--live で claude が無い など）
"""
import argparse
import fnmatch
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, 'tools', 'instructions-check.json')

ng = []
warn = []


def read(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return f.read()


def git(*args):
    r = subprocess.run(['git', '-C', ROOT, *args], capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        print(f'ERROR: git {" ".join(args)}: {r.stderr.strip()}')
        sys.exit(2)
    return r.stdout


def strip_comments(s):
    """Claude Code はブロック単位の HTML コメントを取り除いて読み込む（コードブロック内は除く）。"""
    out, in_code, in_cmt = [], False, False
    for line in s.split('\n'):
        t = line.strip()
        if t.startswith('```'):
            in_code = not in_code
        if not in_code and not in_cmt and t.startswith('<!--'):
            in_cmt = '-->' not in t
            continue
        if in_cmt:
            if '-->' in t:
                in_cmt = False
            continue
        out.append(line)
    return '\n'.join(out)


def expand(patterns):
    files = []
    for p in patterns:
        files += sorted(glob.glob(os.path.join(ROOT, p)))
    return [os.path.relpath(f, ROOT) for f in files]


def check_root_size(cfg):
    s = strip_comments(read('CLAUDE.md'))
    lines, chars = s.count('\n'), len(s)
    lim = cfg['root_limits']
    print(f'[size] CLAUDE.md（コメント除く）: {lines}行 / {chars}字（上限 {lim["max_lines"]}行 / {lim["max_chars"]}字）')
    if lines > lim['max_lines']:
        ng.append(f'size: CLAUDE.md が {lines} 行（上限 {lim["max_lines"]}）')
    if chars > lim['max_chars']:
        ng.append(f'size: CLAUDE.md が {chars} 字（上限 {lim["max_chars"]}）')


def check_lossless(cfg, base):
    """基準コミットの原文の各行が、移した先のどこかに残っているか（意図して削った行は設定に理由つきで載せる）。"""
    for item in cfg['lossless']:
        old = git('show', f'{base}:{item["old"]}').split('\n')
        pool = set()
        for f in expand(item['pool']):
            pool.update(l.strip() for l in read(f).split('\n'))
        dropped = item.get('dropped', {})
        missing = [l.strip() for l in old if l.strip() and l.strip() not in pool and l.strip() not in dropped]
        unused = [k for k in dropped if k in pool]
        print(f'[lossless] {item["old"]}（{base}）: {len([l for l in old if l.strip()])}行中 抜け {len(missing)}・意図して削った {len(dropped)}')
        for l in missing:
            ng.append(f'lossless: {item["old"]} の行が見当たらない: {l[:80]}')
        for k in unused:
            warn.append(f'lossless: dropped に載っているが実際は残っている（設定から外せる）: {k[:60]}')


def check_required(cfg):
    s = strip_comments(read('CLAUDE.md'))
    miss = [r for r in cfg['required_in_root'] if r not in s]
    print(f'[required] ルートに必須の文言: {len(cfg["required_in_root"]) - len(miss)}/{len(cfg["required_in_root"])}')
    for r in miss:
        ng.append(f'required: CLAUDE.md に無い: {r}')
    # 書き出し時にエスケープが絵文字へ化ける事故（2026-11-07 に実際に発生）を検出する
    if re.search('[\U0001F1E6-\U0001F1FF]', s):
        ng.append('required: CLAUDE.md に国旗の絵文字（地域指示子）がある。エスケープの例文が化けていないか確認')


def parse_paths(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not m:
        return None
    return re.findall(r'^\s*-\s*"([^"]+)"\s*$', m.group(1), re.M)


def glob_match(pattern, files):
    # ** を含むパターン：fnmatch の * は / もまたぐので、** を * に縮めて判定すれば十分
    pat = pattern.replace('**/', '*').replace('**', '*')
    return [f for f in files if fnmatch.fnmatch(f, pat)]


def check_rules():
    tracked = git('ls-files').split('\n')
    rules = expand(['.claude/rules/*.md'])
    print(f'[rules] .claude/rules/: {len(rules)}ファイル')
    for r in rules:
        paths = parse_paths(read(r))
        if not paths:
            ng.append(f'rules: {r} に paths: が無い（起動時に毎回読み込まれてしまう）')
            continue
        for p in paths:
            if not glob_match(p, tracked):
                ng.append(f'rules: {r} の paths "{p}" に当たる追跡ファイルが無い（綴りの誤りか、ファイルが移った）')


def check_index():
    s = strip_comments(read('CLAUDE.md'))
    refs = set(re.findall(r'`((?:\.claude/rules|tools/rules)/[\w.-]+\.md)`', s))
    have = set(expand(['.claude/rules/*.md', 'tools/rules/*.md']))
    print(f'[index] 索引からの参照: {len(refs)}・実在: {len(have)}')
    for r in sorted(refs - have):
        ng.append(f'index: CLAUDE.md が参照しているが存在しない: {r}')
    for r in sorted(have - refs):
        ng.append(f'index: CLAUDE.md の索引から参照されていない（読まれないルール）: {r}')


def check_memory_links(cfg):
    ignore = cfg.get('link_ignore', {})
    files = ['Memory.md'] + expand(['tools/rules/*.md', '.claude/rules/*.md'])
    bad = 0
    for f in files:
        for ref in set(re.findall(r'`((?:tools|docs|\.claude|\.github)/[\w./-]+\.(?:md|py|json|html|css|js|yml|sh))`', read(f))):
            if '*' in ref or '<' in ref or ref in ignore:
                continue
            if not os.path.exists(os.path.join(ROOT, ref)):
                bad += 1
                (ng if f == 'Memory.md' else warn).append(f'link: {f} が参照するファイルが無い: {ref}')
    print(f'[link] Memory.md と詳細ルールが参照するファイル: 欠け {bad}')


def check_live(cfg, model):
    """実際に Claude Code を起動し、対象ファイルを Read させて InstructionsLoaded の記録を見る。"""
    exe = shutil.which('claude')
    if not exe:
        print('ERROR: --live には claude（Claude Code CLI）が必要')
        sys.exit(2)
    for t in cfg['live_tests']:
        with tempfile.TemporaryDirectory() as d:
            log = os.path.join(d, 'loaded.jsonl')
            hook = f'cat >> "{log}"; echo >> "{log}"'
            settings = {'hooks': {'InstructionsLoaded': [{'hooks': [{'type': 'command', 'command': hook}]}]}}
            prompt = f'Read ツールで {t["read"]} の先頭5行だけを読み、「ok」とだけ答えてください。ほかの操作はしないこと。'
            r = subprocess.run([exe, '-p', prompt, '--model', model, '--max-turns', '3',
                                '--allowedTools', 'Read', '--settings', json.dumps(settings)],
                               cwd=ROOT, capture_output=True, text=True, encoding='utf-8', timeout=300)
            text = open(log, encoding='utf-8').read() if os.path.exists(log) else ''
        events = [json.loads(l) for l in text.split('\n') if l.strip().startswith('{')]
        if t['rule'] is None:
            stray = sorted({m for e in events for m in re.findall(r'\.claude/rules/[\w.-]+\.md', json.dumps(e, ensure_ascii=False))})
            print(f'[live] {t["read"]} → ルールなしの想定: 読み込まれたルール {stray or "なし"}（exit={r.returncode}）')
            if stray:
                ng.append(f'live: {t["read"]} を読んだだけで {stray} が読み込まれた（paths: が広すぎる）')
            if not events:
                warn.append('live: InstructionsLoaded の記録が1件も無い（フックが動いていない可能性）')
            continue
        hit = [e for e in events if t['rule'] in json.dumps(e, ensure_ascii=False)]
        early = [e for e in hit if 'session_start' in json.dumps(e)]
        ok = bool(hit) and not early
        reasons = sorted({str(e.get('load_reason', '?')) for e in hit})
        print(f'[live] {t["read"]} → {t["rule"]}: {"読み込まれた" if hit else "読み込まれず"}（load_reason={reasons}・exit={r.returncode}）')
        if not hit:
            ng.append(f'live: {t["read"]} を読んでも {t["rule"]} が読み込まれなかった')
        if early:
            ng.append(f'live: {t["rule"]} が起動時に読み込まれている（paths: が効いていない）')
        if not events:
            warn.append('live: InstructionsLoaded の記録が1件も無い（フックが動いていない可能性）')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', help='原文の基準コミット（既定は設定の baseline_commit）')
    ap.add_argument('--live', action='store_true', help='Claude Code を起動して読み込みを実測する（利用枠を少し使う）')
    ap.add_argument('--model', default='haiku', help='--live で使うモデル（既定 haiku）')
    a = ap.parse_args()
    with open(CONFIG, encoding='utf-8') as f:
        cfg = json.load(f)
    base = a.base or cfg['baseline_commit']
    check_root_size(cfg)
    check_lossless(cfg, base)
    check_required(cfg)
    check_rules()
    check_index()
    check_memory_links(cfg)
    if a.live:
        check_live(cfg, a.model)
    for w in warn:
        print('WARN', w)
    for n in ng:
        print('NG  ', n)
    print('結果:', 'NG' if ng else 'OK', f'(NG {len(ng)} / WARN {len(warn)})')
    sys.exit(1 if ng else 0)


if __name__ == '__main__':
    main()
