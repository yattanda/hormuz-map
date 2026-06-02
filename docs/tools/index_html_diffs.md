# index_html_diffs.md — 2026年6月3日 08:30 JST 更新分

> Claude Code への指示：以下の差分を docs/index.html に適用してください。
> 変更箇所以外は絶対に触らないこと。
> 作業後に `git commit`（メッセージ: `docs: 2026年6月3日 08:30 JST 更新 — 交渉膠着継続・MOU署名延期・バンス「not there yet」`）してください。
> **push は確認後に指示します。**

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
        <span class="badge-item badge-date">📅2026年6月2日 09:29 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
        <span class="badge-item badge-date">📅2026年6月3日 08:30 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の主要ニュース項目全体

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 新ティッカー（2026年6月2日 09:29 JST） -->
      🚨【Trump「本日最終決定」】MOU署名99%確度・White House leak確認（Hegseth「very close」・Trump「odds up」）｜Lebanon ceasefire合意（Netanyahu・Hezbollah双方停止・6/1発表）｜IRGC「6/2湾岸基地報復」実施・Araghchi「dialogue ongoing」発言｜油価 Brent $92-96・月間-15%・deal観測継続｜｜交渉延期・バンス「TBD」｜外交膠着継続・封鎖101日目
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 新ティッカー（2026年6月3日 08:30 JST） -->
      🚨【MOU署名延期】6/2未署名・Trump「時間が必要」・バンス「not there yet」発言（CBS News 6/2）｜交渉は「急速ペース」で継続中（Trump Truth Social 6/2）｜イラン「矛盾する米国の立場」を理由に停止（6/1状態）・Araghchi「対話継続」｜ブレント $96.65/bbl（6/2）・deal観測維持も署名延期で上値制限｜全ルート依然閉鎖・通航0隻・デフォルト状態継続・封鎖102日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

**対象：** `<!-- 速報インシデント トグルボタン -->` 内のトグルボタン日付バッジと本文

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
📅 6/2 09:29 更新
<!-- OLD:END -->
<!-- NEW:START -->
📅 6/3 08:30 更新
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（強調タイトル）

<!-- APPLY:START -->
<!-- OLD:START -->
  <strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/2 09:29 速報】Trump「本日最終決定」・MOU署名99%確度・White House leak確認（Hegseth「very close」・Trump「odds up」）｜Lebanon ceasefire合意（Netanyahu・Hezbollah停止・6/1発表）｜IRGC「6/2湾岸基地報復」実施・Araghchi「dialogue ongoing」｜油価Brent $92-96・月間-15%・deal観測継続｜外交膠着・バンス「TBD」・封鎖101日目
  </strong>
<!-- OLD:END -->
<!-- NEW:START -->
  <strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/3 08:30 速報】MOU署名延期・Trump「時間が必要」（6/2 Truth Social）・バンス「very close but not there yet」（CBS News 6/2）｜交渉は「急速ペース」で継続・イラン「米国の矛盾」を理由に一時停止（6/1状態）・Araghchi「dialogue ongoing」｜ブレント $96.65/bbl（6/2）・deal観測維持も署名延期で上値制限｜全ルート依然閉鎖・通航0隻・デフォルト状態・封鎖102日目
  </strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト（先頭に新規インシデント追加）

<!-- APPLY:START -->
<!-- OLD:START -->
        <li style="margin-bottom:8px;font-size:0.75rem;color:#e2e8f0;line-height:1.4;">
          <strong style="color:#fca5a5;">【6/2 21:00 JST】Trump：「それは時間の問題だ」MOU署名延期明言</strong> — 予定されていた6/2署名は未実現。バンス「very close but not there yet」（CBS News）・Trump「Time will tell」。イラン「米国の矛盾した立場」を理由に対話一時停止表明（イラン国営テレビ 6/1）後、Trump「継続中」と反論。交渉は「急速ペース」で進行中（Truth Social）。
        </li>
<!-- OLD:END -->
<!-- NEW:START -->
        <li style="margin-bottom:8px;font-size:0.75rem;color:#e2e8f0;line-height:1.4;">
          <strong style="color:#fca5a5;">【6/2 21:00 JST】Trump：「それは時間の問題だ」MOU署名延期明言</strong> — 予定されていた6/2署名は未実現。バンス「very close but not there yet」（CBS News）・Trump「Time will tell」。イラン「米国の矛盾した立場」を理由に対話一時停止表明（イラン国営テレビ 6/1）後、Trump「継続中」と反論。交渉は「急速ペース」で進行中（Truth Social）。
        </li>
        <li style="margin-bottom:8px;font-size:0.75rem;color:#e2e8f0;line-height:1.4;">
          <strong style="color:#fca5a5;">【6/2 05:00 JST】米軍、ホルムズ付近の防空陣地を再度攻撃</strong> — Strait of Hormuz coast + island targets（Defense Department発表 6/1夜GMT）。イランの「6/2湾岸基地報復」宣言に対する先制攻撃。停戦継続状況下でも防空体制への限定攻撃は継続。
        </li>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード3枚

**対象：** `<!-- SITUATION CARDS -->` セクション内の各カード

### カード1：Blockade Status

<!-- APPLY:START -->
<!-- OLD:START -->
          <span style="font-size:0.85rem;color:#94a3b8;font-weight:500;">🚢 通航状況</span>
          <div style="font-size:1.1rem;font-weight:700;color:#ffcccc;margin:8px 0;">0隻/日（デフォルト）</div>
          <span style="font-size:0.75rem;color:#cbd5e1;">ルート全閉鎖・ホルムズ完全停止継続</span>
          <div style="font-size:0.72rem;color:#64748b;margin-top:8px;">📅 最終確認：6/2 09:29 JST — 変更なし</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <span style="font-size:0.85rem;color:#94a3b8;font-weight:500;">🚢 通航状況</span>
          <div style="font-size:1.1rem;font-weight:700;color:#ffcccc;margin:8px 0;">0隻/日（デフォルト）</div>
          <span style="font-size:0.75rem;color:#cbd5e1;">ルート全閉鎖・ホルムズ完全停止継続</span>
          <div style="font-size:0.72rem;color:#64748b;margin-top:8px;">📅 最終確認：6/3 08:30 JST — 変更なし（MOU延期で署名後解除へ）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード2：Oil Price（動向）

<!-- APPLY:START -->
<!-- OLD:START -->
          <span style="font-size:0.85rem;color:#94a3b8;font-weight:500;">⛽ 原油価格</span>
          <div style="font-size:1.1rem;font-weight:700;color:#fbbf24;margin:8px 0;">Brent $96.42 / WTI $91</div>
          <span style="font-size:0.75rem;color:#cbd5e1;">month-on-month: -15% (deal観測) | year-on-year: +45%</span>
          <div style="font-size:0.72rem;color:#64748b;margin-top:8px;">📅 更新：6/2 08:30 ET — deal観測継続</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <span style="font-size:0.85rem;color:#94a3b8;font-weight:500;">⛽ 原油価格</span>
          <div style="font-size:1.1rem;font-weight:700;color:#fbbf24;margin:8px 0;">Brent $96.65 / WTI $91-92</div>
          <span style="font-size:0.75rem;color:#cbd5e1;">month-on-month: -15% (deal観測維持) | year-on-year: +46%</span>
          <div style="font-size:0.72rem;color:#64748b;margin-top:8px;">📅 更新：6/2 08:20 ET — deal観測維持も署名延期で上値制限</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード3：Supply Chain Risk

<!-- APPLY:START -->
<!-- OLD:START -->
          <span style="font-size:0.85rem;color:#94a3b8;font-weight:500;">🌍 サプライチェーン影響</span>
          <div style="font-size:1.1rem;font-weight:700;color:#ff7f7f;margin:8px 0;">🚨 最高</div>
          <span style="font-size:0.75rem;color:#cbd5e1;">全航路迂回・輸送期間+14日・保険料+30%・日本LNG調達再編協議中</span>
          <div style="font-size:0.72rem;color:#64748b;margin-top:8px;">📅 最終確認：6/2 — 変更なし（MOU未署名で継続）</div>
<!-- OLD:END -->
<!-- NEW:START -->
          <span style="font-size:0.85rem;color:#94a3b8;font-weight:500;">🌍 サプライチェーン影響</span>
          <div style="font-size:1.1rem;font-weight:700;color:#ff7f7f;margin:8px 0;">🚨 最高</div>
          <span style="font-size:0.75rem;color:#cbd5e1;">全航路迂回・輸送期間+14日・保険料+30%・日本LNG調達再編協議中</span>
          <div style="font-size:0.72rem;color:#64748b;margin-top:8px;">📅 最終確認：6/3 08:30 JST — 変更なし（MOP署名延期で継続）</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN フェーズラベル

**対象：** `<!-- COUNTDOWN -->` セクション内のフェーズラベル

<!-- APPLY:START -->
<!-- OLD:START -->
      <div style="font-size:0.9rem;color:#cbd5e1;font-weight:600;letter-spacing:0.05em;text-transform:uppercase;">Phase 5 — 「最後の24時間：MOU署名直前」</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <div style="font-size:0.9rem;color:#cbd5e1;font-weight:600;letter-spacing:0.05em;text-transform:uppercase;">Phase 5 — 「膠着局面：署名タイムライン未定」</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

**対象：** `<!-- SCENARIOS -->` セクション内のバナーテキスト

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="background:rgba(248,113,113,0.08);border-left:3px solid #f87171;padding:12px 14px;margin-bottom:16px;font-size:0.8rem;color:#fca5a5;line-height:1.5;">
          <strong>⚡ 補足：</strong>「24時間が決定づける：本日のMOU署名が確率を大きく左右する。署名なし＝膠着継続・シナリオB確度向上」
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="background:rgba(248,113,113,0.08);border-left:3px solid #f87171;padding:12px 14px;margin-bottom:16px;font-size:0.8rem;color:#fca5a5;line-height:1.5;">
          <strong>⚡ 補足：</strong>「署名延期で不確実性拡大：MOU未署名でバンス『not there yet』発言。6月上旬の決定まで膠着が深刻化。シナリオBが依然として最有力（70%）」
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] シナリオ4本（タイトル・本文）

**対象：** `<!-- SCENARIOS -->` セクション内の各シナリオカード

### シナリオA（確度10%）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="sc-card" style="background:linear-gradient(135deg,rgba(226,232,240,0.08) 0%,rgba(148,163,184,0.04) 100%);border:1px solid rgba(226,232,240,0.15);border-radius:8px;padding:16px;margin-bottom:12px;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
            <h4 style="color:#cbd5e1;font-size:0.85rem;font-weight:700;margin:0;text-transform:uppercase;letter-spacing:0.08em;">A. 即時再開（確度：10%）</h4>
            <span style="background:#10b981;color:#fff;font-size:0.7rem;padding:4px 8px;border-radius:4px;font-weight:600;">10%</span>
          </div>
          <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.6;">
            Trump「本日署名」が成立。MOU内容の90%が既に合意状態。ホルムズが数時間内に再開。油価急落・ドル高・株価上昇。ただし実現確率は低い（イラン側の最後の抵抗・手段論で膠着の可能性高）。
          </div>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="sc-card" style="background:linear-gradient(135deg,rgba(226,232,240,0.08) 0%,rgba(148,163,184,0.04) 100%);border:1px solid rgba(226,232,240,0.15);border-radius:8px;padding:16px;margin-bottom:12px;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
            <h4 style="color:#cbd5e1;font-size:0.85rem;font-weight:700;margin:0;text-transform:uppercase;letter-spacing:0.08em;">A. 即時再開（確度：10%）</h4>
            <span style="background:#10b981;color:#fff;font-size:0.7rem;padding:4px 8px;border-radius:4px;font-weight:600;">10%</span>
          </div>
          <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.6;">
            6月上旬中にMOU署名が急速に成立。バンス「not there yet」発言から一転、Trump強力な圧力で両陣営を妥協させる。ホルムズが数日内に再開。油価急落・ドル高・株価上昇。ただし交渉膠着の深刻化が実現確率を低下させている。
          </div>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオB（確度70%）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="sc-card" style="background:linear-gradient(135deg,rgba(245,158,11,0.08) 0%,rgba(217,119,6,0.04) 100%);border:1px solid rgba(245,158,11,0.15);border-radius:8px;padding:16px;margin-bottom:12px;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
            <h4 style="color:#fbbf24;font-size:0.85rem;font-weight:700;margin:0;text-transform:uppercase;letter-spacing:0.08em;">B. 段階的開放（確度：70%）</h4>
            <span style="background:#f59e0b;color:#000;font-size:0.7rem;padding:4px 8px;border-radius:4px;font-weight:600;">70%</span>
          </div>
          <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.6;">
            6月中旬までにMOU署名。60日フェーズが開始される。ホルムズは制限付き・PGSA型の有償通航制度で部分的再開（イラン独自管理）。日本タンカーは限定再開。油価は$85～88 range維持。UAE沖での混在ルート増設。「膠着の段階的解消」が現実的シナリオ。
          </div>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="sc-card" style="background:linear-gradient(135deg,rgba(245,158,11,0.08) 0%,rgba(217,119,6,0.04) 100%);border:1px solid rgba(245,158,11,0.15);border-radius:8px;padding:16px;margin-bottom:12px;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
            <h4 style="color:#fbbf24;font-size:0.85rem;font-weight:700;margin:0;text-transform:uppercase;letter-spacing:0.08em;">B. 段階的開放（確度：70%）</h4>
            <span style="background:#f59e0b;color:#000;font-size:0.7rem;padding:4px 8px;border-radius:4px;font-weight:600;">70%</span>
          </div>
          <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.6;">
            6月中旬～下旬にMOU署名成立。60日フェーズ開始。ホルムズは制限付き・PGSA型有償通航制度で部分的再開（イラン独自管理）。日本タンカーは限定再開。油価は$85～90 range維持。UAE沖混在ルート増設。バンスの「not there yet」発言が反映される段階的解消シナリオ。
          </div>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオC（確度15%）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="sc-card" style="background:linear-gradient(135deg,rgba(244,63,94,0.08) 0%,rgba(225,29,72,0.04) 100%);border:1px solid rgba(244,63,94,0.15);border-radius:8px;padding:16px;margin-bottom:12px;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
            <h4 style="color:#f87171;font-size:0.85rem;font-weight:700;margin:0;text-transform:uppercase;letter-spacing:0.08em;">C. 完全閉鎖＆機雷除去延期（確度：15%）</h4>
            <span style="background:#ef4444;color:#fff;font-size:0.7rem;padding:4px 8px;border-radius:4px;font-weight:600;">15%</span>
          </div>
          <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.6;">
            イランが「米国の矛盾・イスラエルの攻撃」を理由に交渉を一時中断。ホルムズ完全閉鎖の継続宣言。機雷除去の「条件前払い」をイランが拒否。油価$110~115へ上昇。日本への影響：LNG調達不可・海運保険料50%超上昇・消費者物価大幅上昇。
          </div>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="sc-card" style="background:linear-gradient(135deg,rgba(244,63,94,0.08) 0%,rgba(225,29,72,0.04) 100%);border:1px solid rgba(244,63,94,0.15);border-radius:8px;padding:16px;margin-bottom:12px;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
            <h4 style="color:#f87171;font-size:0.85rem;font-weight:700;margin:0;text-transform:uppercase;letter-spacing:0.08em;">C. 完全閉鎖＆機雷除去延期（確度：15%）</h4>
            <span style="background:#ef4444;color:#fff;font-size:0.7rem;padding:4px 8px;border-radius:4px;font-weight:600;">15%</span>
          </div>
          <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.6;">
            イランが「米国の矛盾した要求・イスラエルの Lebanon 攻撃」を理由に交渉を段階的に放棄。ホルムズ完全閉鎖の継続宣言強化。機雷除去の「条件前払い」をイランが拒否。油価$110～115へ上昇。日本への影響：LNG調達不可・海運保険料50%超上昇・消費者物価大幅上昇。6月下旬～7月の膠着深刻化ケース。
          </div>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオD（確度5%）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="sc-card" style="background:linear-gradient(135deg,rgba(139,0,0,0.12) 0%,rgba(255,0,0,0.04) 100%);border:1px solid rgba(255,50,50,0.2);border-radius:8px;padding:16px;margin-bottom:12px;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
            <h4 style="color:#fca5a5;font-size:0.85rem;font-weight:700;margin:0;text-transform:uppercase;letter-spacing:0.08em;">D. 軍事再開＆Escalation（確度：5%）</h4>
            <span style="background:#dc2626;color:#fff;font-size:0.7rem;padding:4px 8px;border-radius:4px;font-weight:600;">5%</span>
          </div>
          <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.6;">
            イラン「米国・イスラエルの攻撃」を理由に外交を完全放棄。イスラエル Lebanon侵攻 + IRGC報復ミサイル発射。米軍による制裁下での物資輸送制限が発動。石油施設への大規模攻撃の懸念。油価$130以上。全面紛争状態。ただし現在のバイデン仲介・Pakistan mediation により実現確率は最小限。
          </div>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="sc-card" style="background:linear-gradient(135deg,rgba(139,0,0,0.12) 0%,rgba(255,0,0,0.04) 100%);border:1px solid rgba(255,50,50,0.2);border-radius:8px;padding:16px;margin-bottom:12px;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
            <h4 style="color:#fca5a5;font-size:0.85rem;font-weight:700;margin:0;text-transform:uppercase;letter-spacing:0.08em;">D. 軍事再開＆Escalation（確度：5%）</h4>
            <span style="background:#dc2626;color:#fff;font-size:0.7rem;padding:4px 8px;border-radius:4px;font-weight:600;">5%</span>
          </div>
          <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.6;">
            イラン外交放棄宣言・Trump無視表明。イスラエル Lebanon侵攻激化 + IRGC報復ミサイル・ドローン大規模発射。米軍による制裁下での物資輸送制限発動。ホルムズ付近での再度の軍事衝突。石油施設への大規模攻撃懸念。油価$130以上。全面紛争状態。Trump mediation 失敗・Pakistan仲介破綻のシナリオ。
          </div>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオフッター

**対象：** `<!-- シナリオ フッター -->` セクション

<!-- APPLY:START -->
<!-- OLD:START -->
    <div style="text-align:center;font-size:0.8rem;color:#94a3b8;margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.08);">
      ⚡ <strong>24時間が全てを決める：本日 6/2 のMOU署名が確率を左右。署名なし＝シナリオB~C継続。</strong>
    </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div style="text-align:center;font-size:0.8rem;color:#94a3b8;margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.08);">
      ⚠️ <strong>署名延期・膠着局面：MOU未署名で6月上旬の決定まで不確実性が拡大。バンス「not there yet」発言が反映される。シナリオB（70%）が継続有力。イラン「矛盾する米国要求」を理由に対話一時停止状態での膠着深刻化。</strong>
    </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー

**対象：** `🚢 全ルート現況サマリー` セクション

<!-- APPLY:START -->
<!-- OLD:START -->
    <div style="font-size:0.8rem;color:#cbd5e1;margin:20px 0;line-height:1.8;">
      <span style="font-weight:600;">🚢 全ルート現況サマリー（2026年6月2日 09:29 JST 更新）</span>
      <div style="margin-top:8px;color:#94a3b8;font-size:0.75rem;">
        ホルムズ海峡完全閉鎖・PGSA通航料制度実質化・101日目突入。UAE沖迂回ルート(+14日)が全便の95%。スエズ経由(+10日)は5%。日本タンカー0隻通過継続。通航料金は有償制へ移行（公式発表なし・非公式通達のみ）。<strong>MOU署名99%確度（6/2署名予定）→署名実現で同日中にホルムズ部分再開予定。</strong>
      </div>
    </div>
<!-- OLD:END -->
<!-- NEW:START -->
    <div style="font-size:0.8rem;color:#cbd5e1;margin:20px 0;line-height:1.8;">
      <span style="font-weight:600;">🚢 全ルート現況サマリー（2026年6月3日 08:30 JST 再確認済）</span>
      <div style="margin-top:8px;color:#94a3b8;font-size:0.75rem;">
        ホルムズ海峡完全閉鎖継続・102日目。PGSA通航料制度実質化・デフォルト化。UAE沖迂回ルート(+14日)が全便の95%。スエズ経由(+10日)は5%。日本タンカー0隻通過継続。<strong>MOU署名は6/2に未実現（予定延期）。バンス「not there yet」発言で6月上旬まで署名延期の可能性高。署名後のホルムズ部分再開日程は未定。</strong>膠着深刻化により、6月中旬～下旬での段階的再開がシナリオB有力。
      </div>
    </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S09] 30秒カラム（3行+バッジ5枚）

**対象：** `<!-- 30秒で全体像を把握 -->` セクション

**ステータス：全セクション確定後に最後に作成（本diffs.md では記載）**

### タイトル行

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="font-size:0.9rem;font-weight:700;color:#e2e8f0;margin-bottom:8px;">🚨 30秒で全体像を把握</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="font-size:0.9rem;font-weight:700;color:#e2e8f0;margin-bottom:8px;">🚨 30秒で全体像を把握</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### 本文3行

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.8;margin-bottom:14px;">
          <div>1️⃣ <strong>MOU署名直前</strong>：Trump「本日最終決定」・90%確度・白宮leak確認。イラン・米国がほぼ合意。</div>
          <div>2️⃣ <strong>油価安定</strong>：Brent $96 range（month -15%）。deal観測で下値支持・上値制限。</div>
          <div>3️⃣ <strong>日本への影響</strong>：MOU署名後「数時間内」にホルムズ部分再開予定→日本タンカー限定再開→LNG調達安定化へ。</div>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="font-size:0.8rem;color:#cbd5e1;line-height:1.8;margin-bottom:14px;">
          <div>1️⃣ <strong>MOU署名延期</strong>：予定された6/2署名は未実現。バンス「very close but not there yet」。6月上旬中の決定を見込む。</div>
          <div>2️⃣ <strong>油価安定化</strong>：Brent $96.65 range（month -15%）。deal観測維持も署名延期で上値制限。膠着深刻化で $100突破リスク。</div>
          <div>3️⃣ <strong>日本への影響</strong>：MOU署名延期で解除日程未定。6月中旬～下旬での段階的再開がシナリオB有力→LNG調達安定化は遅延。</div>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### バッジ5枚

#### バッジ① - Status

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="display:inline-block;background:#f87171;color:#000;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;margin-right:8px;margin-bottom:6px;">
          ⏳ 待機中（24h以内署名予定）
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="display:inline-block;background:#f87171;color:#000;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;margin-right:8px;margin-bottom:6px;">
          ⏳ 膠着継続（署名延期）
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

#### バッジ② - Risk Level

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="display:inline-block;background:#fbbf24;color:#000;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;margin-right:8px;margin-bottom:6px;">
          🚨 最高（署名直前）
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="display:inline-block;background:#f87171;color:#000;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;margin-right:8px;margin-bottom:6px;">
          🚨 最高（膠着深刻化）
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

#### バッジ③ - Oil Market

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="display:inline-block;background:#4ade80;color:#000;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;margin-right:8px;margin-bottom:6px;">
          ✓ 安定（deal観測）
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="display:inline-block;background:#fbbf24;color:#000;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;margin-right:8px;margin-bottom:6px;">
          ⚠️ 上下動（署名延期で不確実）
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

#### バッジ④ - Japan LNG

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="display:inline-block;background:#f87171;color:#fff;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;margin-right:8px;margin-bottom:6px;">
          🇯🇵 LNG調達: 危機継続
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="display:inline-block;background:#f87171;color:#fff;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;margin-right:8px;margin-bottom:6px;">
          🇯🇵 LNG調達: 危機継続（解除日未定）
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

#### バッジ⑤ - Scenario Best Fit

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="display:inline-block;background:#cbd5e1;color:#000;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;text-align:right;display:block;">
          📊 有力：シナリオA（署名直前） | バックアップ：B
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="display:inline-block;background:#cbd5e1;color:#000;padding:5px 10px;border-radius:4px;font-size:0.7rem;font-weight:600;text-align:right;display:block;">
          📊 有力：シナリオB（段階的開放・70%） | 注視：C（膠着15%）
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] news_data.json 更新メモ

### 新規ニュース追加（latest配列へ）

**新規追加予定：**

1. **CBS News**: Trump Iran deal talks - "not there yet" Vance statement（6/2 15:00 JST）  
   https://www.cbsnews.com/live-updates/iran-war-us-trump-vance-ceasefire-strait-of-hormuz-deal-close/

2. **Fox News**: Trump Iran ceasefire deal continues at rapid pace（6/2 06:00 JST）  
   https://www.foxnews.com/live-news/trump-iran-war-israel-lebanon-hormuz-june-2

3. **Time Magazine**: Trump says it's time "one way or another" for Iran to make a deal（6/2 22:00 JST）  
   https://time.com/article/2026/06/02/trump-netanyahu-crazy-lebanon-hezbollah-ceasefire-iran-us-peace-deal/

### news_data.json 更新ルール

- `latest` に上記3件を先頭から追加
- 既存の最古1件を `archive` バッチ（6月2日分）の先頭へ移動
- `updated` フィールドを `"2026年6月3日 08:30 日本時間JST"` に更新
- `staleNotice` を空文字 `""` に更新（新情報あり）

---

## [S11] 更新ログ追記 + 折り畳み維持（2ブロック構成）

### ブロック1：常時表示3件の更新（3件固定を維持）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
          <div>📅 <strong>2026年6月2日 09:29 JST</strong> 更新</div>
          <div><span style="color:#f87171;">2026/06/02 09:29</span> — Trump「本日最終決定」日程・MOU署名99%確度（White House leak確認・Hegseth「very close」・Trump「odds up」）・Lebanon ceasefire合意（Netanyahu・Hezbollah双方停止・6/1発表）・IRGC「6/2湾岸基地報復」実施・Araghchi「dialogue ongoing」発言・油価 Brent $92-96・月間-15%・deal観測継続・S01時刻更新・S02 TICKER更新・S03速報2件更新・S04カード3枚・S05フェーズラベル・S06補足バナー・S07シナリオ4本（A→10%・B→70%・C→15%・D→5%）・S08フッター・S08.5全ルート再確認・S10 news2件+osint・dateModified 6/2。出典：CBS News・Al Jazeera・TradingEconomics・Defense Department（2026/6/1-2）</div>
          <div>📅 <strong>2026年6月1日 09:00 JST</strong> 更新</div>
          <div><span style="color:#4ade80;">2026/06/01 09:00</span> — Trump「Lebanon Netanyahu・Hezbollah停止合意」発表・MOU暫定合意White House確認・Hegseth「blockade very much still in place」Singapore防衛会議で発言・oil markets deal観測で Brent下落-15%月間・News2件・OSINT更新</div>
          <div>📅 <strong>2026年5月29日 09:42 JST</strong> 更新</div>
          <div><span style="color:#f87171;">2026/05/29 09:42</span> — 米・イランが60日MOU草案で暫定合意（トランプ最終署名待ち）・機雷除去30日・無制限通航・核交渉開始・IRGC missile launch・MQ-9撃墜・EU制裁拡大・ニュース2件・OSINT更新</div>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="font-size:0.72rem;color:#cbd5e1;line-height:2;">
          <div>📅 <strong>2026年6月3日 08:30 JST</strong> 更新</div>
          <div><span style="color:#f87171;">2026/06/03 08:30</span> — MOU署名延期・6/2未署名・Trump「時間が必要」・バンス「very close but not there yet」（CBS News 6/2）・交渉は「急速ペース」で継続（Truth Social 6/2）・イラン「米国の矛盾した立場」を理由に一時停止（6/1状態）・Araghchi「対話継続」・米軍ホルムズ付近防空陣地再度攻撃（6/1夜GMT）・ブレント $96.65/bbl（6/2）・deal観測維持も署名延期で上値制限・全ルート依然閉鎖・通航0隻・デフォルト継続・S01時刻更新・S02 TICKER更新・S03速報3件（署名延期+防空攻撃）・S04カード3枚更新・S05フェーズラベル・S06補足バナー・S07シナリオ4本確度再評価（A→10%・B→70%・C→15%・D→5%）・S08フッター・S08.5全ルート再確認・S09全更新・S10 news3件・S11更新ログ追記・dateModified 6/3。出典：CBS News・Time Magazine・Fox News・TradingEconomics・Defense Department（2026/6/2-3）</div>
          <div>📅 <strong>2026年6月2日 09:29 JST</strong> 更新</div>
          <div><span style="color:#f87171;">2026/06/02 09:29</span> — Trump「本日最終決定」日程・MOU署名99%確度（White House leak確認・Hegseth「very close」・Trump「odds up」）・Lebanon ceasefire合意（Netanyahu・Hezbollah双方停止・6/1発表）・IRGC「6/2湾岸基地報復」実施・Araghchi「dialogue ongoing」発言・油価 Brent $92-96・月間-15%・deal観測継続・S01時刻更新・S02 TICKER更新・S03速報2件更新・S04カード3枚・S05フェーズラベル・S06補足バナー・S07シナリオ4本（A→10%・B→70%・C→15%・D→5%）・S08フッター・S08.5全ルート再確認・S10 news2件+osint・dateModified 6/2。出典：CBS News・Al Jazeera・TradingEconomics・Defense Department（2026/6/1-2）</div>
          <div>📅 <strong>2026年6月1日 09:00 JST</strong> 更新</div>
          <div><span style="color:#4ade80;">2026/06/01 09:00</span> — Trump「Lebanon Netanyahu・Hezbollah停止合意」発表・MOU暫定合意White House確認・Hegseth「blockade very much still in place」Singapore防衛会議で発言・oil markets deal観測で Brent下落-15%月間・News2件・OSINT更新</div>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ブロック2：log-collapse への旧4番目エントリー挿入

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年5月31日 09:00 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年5月29日 09:42 JST</strong> 更新</div>
          <div><span style="color:#f87171;">2026/05/29 09:42</span> — 米・イランが60日MOU草案で暫定合意（トランプ最終署名待ち）・機雷除去30日・無制限通航・核交渉開始・IRGC missile launch・MQ-9撃墜・EU制裁拡大・ニュース2件・OSINT更新</div>
          <div>📅 <strong>2026年5月31日 09:00 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [C01] MAP・タンカー可視化（ステータス確認）

**対象：** MAP セクション内の日本籍タンカー足止め日数表示

**変更なし・再確認済：**

- 日本籍タンカー足止め数：12隻（最後の更新：6/2）
- 最終確認日時：2026年6月3日 08:30 JST — 変更なし（MOU未署名で継続）

---

## 出力前セルフチェック

```
[x] S01 ヘッダー ― 日付 2026年6月3日 08:30 JST が入っているか ✓
[x] S02 TICKER ― 署名延期・バンス「not there yet」・膠着継続が反映されているか ✓
[x] S03 速報インシデント ― 3件記載（署名延期・防空攻撃+既存情報） ✓
[x] S04 情勢カード3枚 ― Blockade・Oil price・Supply chain 全て本日更新 ✓
[x] S05 COUNTDOWN ― フェーズラベル「膠着局面：署名タイムライン未定」に更新 ✓
[x] S06 シナリオ確率補足バナー ― 「署名延期で不確実性拡大」テキスト入力 ✓
[x] S07 シナリオ4本 ― A(10%)・B(70%)・C(15%)・D(5%) 確度維持＋内容更新 ✓
[x] S07 C・D ― 内容差別化確認（C=完全閉鎖継続、D=外交放棄＆軍事再開） ✓
[x] S08 フッター ― 「膠着深刻化・シナリオB継続有力」に更新 ✓
[x] S08.5 全ルート現況サマリー ― 日付 2026年6月3日 08:30 JST・「MOU署名延期」記載 ✓
[x] S09 30秒カラム ― 署名延期・バンス「not there yet」・膠着継続が反映・全セクション確定後に最後に作成 ✓
[x] S10 news_data.json ― URL確認済（CBS News・Time・Fox News）・append-only ルール確認 ✓
[x] S11 更新ログ ― ブロック1で3件固定（6/3・6/2・6/1）✓ ブロック2で旧3番目（5/29）を先頭挿入 ✓
[x] S11 常時表示3件 ― 6/3・6/2・6/1 正確に3件 ✓
[x] S11 JSON-LD ― "dateModified": "2026-06-03" に更新指示 ✓
[x] C01 タンカー可視化 ― dateConfirmed：「6月3日 08:30 JST 変更なし」確認 ✓
[x] 全体 ― 日付表記が「YYYY年MM月DD日 HH:MM 日本時間JST」形式で統一 ✓
```

---

## JSON-LD dateModified 更新指示

docs/index.html 内の JSON-LD セクションで以下を更新してください：

```json
"dateModified": "2026-06-03",
```

（Claude Code が通常の str_replace 対象外として自動処理）

---

## 📥 ダウンロード準備完了

本 diffs.md は **11セクション全て対応**し、全出力前セルフチェックを満たしています。

**生成完了日時:** 2026年6月3日 08:30 日本時間JST  
**対応セクション:** S01～S09・S10・S11・C01  
**ファイルサイズ:** ~28KB（APPLY ブロック形式）  
**総項目数:** S11 更新ログ新規1件追加 + S10 news 3件追加 + S11 折り畳み移動

---

**✅ このファイルは Claude Code の `git pull --rebase` 後に `docs/index.html` に適用可能です。**
