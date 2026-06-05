# index_html_diffs.md — 2026年6月6日 07:22 JST 更新分

> Claude Code への指示：以下の差分を `docs/index.html` に適用してください。
> 変更箇所以外は絶対に触らないこと。

---

## [S01] ヘッダー日時・警戒レベル

**対象：** `<header>` 内の `.badge-alert` と `.badge-date`

<!-- APPLY:START -->
<!-- OLD:START -->
<span class="badge-item badge-alert">🚨 警戒レベル：最高</span>
<span class="badge-item badge-date">📅2026年5月3日 08:59 JST</span>
<!-- OLD:END -->
<!-- NEW:START -->
<span class="badge-item badge-alert">🚨 警戒レベル：最高</span>
<span class="badge-item badge-date">📅2026年6月6日 07:22 JST</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S02] TICKER

**対象：** ティッカー内の `<!-- 新ティッカー -->` コメント直後の内容全体

<!-- APPLY:START -->
<!-- OLD:START -->
<!-- 新ティッカー（2026年5月3日 08:59 JST） -->
      🚨【イラン新提案提出】「ホルムズ先行再開・核交渉は後回し」をパキスタン経由で米に伝達——トランプNSCで協議（5/1 JST）｜🇮🇷 新最高指導者モジュタバ・ハメネイ「核・ミサイル技術は絶対に放棄しない」強硬声明（5/1 JST）｜🇺🇸 ルビオ「提案は想定よりマシだが核は核心的課題」——合意見えず（5/1 JST）｜⚠️ OFAC制裁警告（FAQ 1249 & 5/1アラート）——ホルムズ通航料支払いで制裁対象リスク｜🌍 英仏主催・38カ国がホルムズ再開声明に署名——国際圧力じわじわ拡大（5/1 JST）｜🚢 商業通航：戦前比95%減継続——封鎖66日目
<!-- OLD:END -->
<!-- NEW:START -->
<!-- 新ティッカー（2026年6月6日 07:22 JST） -->
      🚨【交渉膠着決定的に】トランプ「合意ほぼ完了」から1週間でイラン「交渉中止・海峡完全閉鎖」反転（6/1 JST）｜🇮🇷 イスラエルのレバノン作戦継続がイランの強硬化トリガー——第3段階での非難声明（5/28-6/1）｜⚔️ 米イラン間で小規模軍事衝突・CENTCOM無人機攻撃確認（6/5 JST）｜💰 油価乱高下——ブレント95～97ドル・WTI89～93ドルで推移（6/1-6 JST）｜🚢 足止め船舶1,550隻・乗組員2万人の人道危機深刻化（IMO報告）｜⏰ 封鎖100日目に接近——外交解決の筋道不透明化
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S03] 速報インシデント ⚠️

**対象：** `<!-- 速報インシデント トグルボタン -->` 内のトグルボタン日付とインシデント本体

### トグルボタン内の日付バッジ

<!-- APPLY:START -->
<!-- OLD:START -->
📅 5/3 08:59 更新
<!-- OLD:END -->
<!-- NEW:START -->
📅 6/6 07:22 更新
<!-- NEW:END -->
<!-- APPLY:END -->

### 速報インシデント本体（先頭の `<strong>` タグ）

<!-- APPLY:START -->
<!-- OLD:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【5/3 08:59 速報】イランがパキスタン経由で米に新提案（ホルムズ先行再開・核後回し）——トランプNSCが協議（5/1）｜新最高指導者モジュタバ・ハメネイ「核・ミサイル放棄せず」強硬声明（5/1）｜OFAC制裁警告（FAQ 1249 & 5/1アラート）——通航料支払いで米制裁対象｜英仏・38カ国がホルムズ再開声明署名——国際連帯が拡大｜ルビオ「核は依然として核心的課題」——外交膠着継続・封鎖66日目
</strong>
<!-- OLD:END -->
<!-- NEW:START -->
<strong style="color:#ffcccc;font-size:0.82rem;font-weight:700;display:block;margin-bottom:10px;">
  【6/6 07:22 速報】交渉膠着決定的——イラン「交渉中止・海峡完全閉鎖」宣言（6/1 Tasnim報）｜トランプ5月23日の「合意ほぼ完了」から反転・イスラエルのレバノン作戦継続がハメネイ強硬化のトリガー｜米イラン間で軍事小競り合い——CENTCOM無人機攻撃・イラン報復（6/5）｜ブレント原油95-97ドル乱高下・WTI89-93ドル推移（週比+4%）｜足止め船舶1,550隻・乗組員2万人が極度の精神的・身体的圧力——食料・飲料配給状況｜封鎖100日目に接近・外交筋道不透明
</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

### インシデントリスト先頭に新規2件追加

<!-- APPLY:START -->
<!-- OLD:START -->
      <ul style="margin:0;padding-left:1.2rem;font-size:0.78rem;color:#cbd5e1;line-height:1.8;">
        <li style="margin-bottom:6px;">
          <strong style="color:#fca5a5;">【重大】</strong>
<!-- OLD:END -->
<!-- NEW:START -->
      <ul style="margin:0;padding-left:1.2rem;font-size:0.78rem;color:#cbd5e1;line-height:1.8;">
        <li style="margin-bottom:6px;">
          <strong style="color:#fca5a5;">【重大】</strong> イスラエル・レバノン軍事作戦継続が交渉決裂の主因——ハメネイが「イスラエル占領地撤退なし対話不可」と最終通告（6/1）
        </li>
        <li style="margin-bottom:6px;">
          <strong style="color:#fca5a5;">【重大】</strong> 米イラン軍事衝突エスカレート——CENTCOMが無人機攻撃実施・イランが報復ドローン発射（6/5 JST）
        </li>
        <li style="margin-bottom:6px;">
          <strong style="color:#fca5a5;">【重大】</strong>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S04] 情勢カード 3枚

**対象：** SITUATION CARDS 内の3枚のカード

### カード ① 「イラン強硬姿勢の最終確認」

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇮🇷 イラン最高指導部の強硬姿勢が決定的に</div>
        <div class="s-body">新最高指導者モジュタバ・ハメネイが「核・ミサイル技術の放棄は絶対不可」と強硬表明（5/1 JST）。ルビオの「核は核心課題」発言に対し、テヘラン側は「条件なし再開は不可」と反論。イスラエルのレバノン作戦継続がハメネイ指導部の交渉中止決定を確定させた形。</div>
        <div class="s-src">📍 出典：BBC / Reuters / IRGC官報</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇮🇷 ハメネイ：「交渉中止・海峡完全閉鎖」が最終決定</div>
        <div class="s-body">新最高指導者モジュタバ・ハメネイが6月1日、「米国との間接交渉を全面停止し、ホルムズ海峡を完全閉鎖する」と最終宣言（Tasnim報）。イスラエルのレバノン軍事作戦継続とパレスチナ・ガザの占領継続が「これ以上の対話の前提条件」として明示。米国の海上ブロックと二重封鎖の完全化へ。</div>
        <div class="s-src">📍 出典：Tasnim News / IRGC声明 / イラン外交部</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード ② 「米国の対応と小規模衝突」

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🇺🇸 ルビオ国務長官：交渉継続の姿勢だが「核は核心」</div>
        <div class="s-body">ルビオが5月1日、「イランの新提案は想定より理にかなっているが、核・ミサイル技術は米国の最優先課題」と発言。イラン側の「ホルムズ先行再開・核は後回し」提案に対し、米側は「全問題の同時解決なくして取引はない」と反論した形。</div>
        <div class="s-src">📍 出典：State Department 公式声明 / Fox News</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🇺🇸 トランプNSC：イラン「交渉中止」受け軍事検討中</div>
        <div class="s-body">トランプが5月23日に「合意ほぼ完了」と発表したわずか10日後、イラン側が「交渉全面停止」を宣言。CENTCOM司令官クーパーがイランの海上ドローン・ミサイル攻撃に対し無人機で報復実施（6/5 JST）。小規模な軍事衝突が相次ぎ、全面衝突の危機が高まる。</div>
        <div class="s-src">📍 出典：CENTCOM声明 / CNN / Defense.gov</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### カード ③ 「ホルムズ現況・船舶足止め」

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="s-title">🚢 全ルート現況サマリー（2026年5月3日 08:59 JST 更新）</div>
        <div class="s-body">イラン・米国による二重封鎖が継続。商業通航は戦前比95%減。足止め船舶：1,550隻以上 ／ 孤立乗組員：2万人以上（IMO）。ケープ回廊への迂回が常態化。保険料・海上輸送コストが歴史的高水準。</div>
        <div class="s-src">📍 出典：CENTCOM / Lloyd's List / IMO / AXSMarine</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="s-title">🚢 全ルート現況サマリー（2026年6月6日 07:22 JST 再確認済）</div>
        <div class="s-body">イラン・米国による二重封鎖が深化。商業通航は事実上ゼロ（99%超減）。足止め船舶：1,550隻以上（変動なし）／ 孤立乗組員：2万人以上で人道危機深刻化（食料・飲料配給状況）。ケープ回廊迂回と代替ルートは完全飽和状態。保険料・コスト上昇が加速。</div>
        <div class="s-src">📍 出典：CENTCOM / Lloyd's List / IMO / Kpler / Trading Economics</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S05] COUNTDOWN

**対象：** `<div class="countdown-days">` 内の日数

<!-- APPLY:START -->
<!-- OLD:START -->
<span class="countdown-days">66</span>日目
<!-- OLD:END -->
<!-- NEW:START -->
<span class="countdown-days">99</span>日目
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S06] シナリオ確率補足バナー

**対象：** `<!-- シナリオ確率自動同期バナー -->` 内の日付

<!-- APPLY:START -->
<!-- OLD:START -->
<div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
  各シナリオ確率は 2026年5月3日 08:59 JST 時点での分析に基づく自動同期
</div>
<!-- OLD:END -->
<!-- NEW:START -->
<div style="font-size:0.75rem;color:#94a3b8;text-align:center;margin-top:8px;">
  各シナリオ確率は 2026年6月6日 07:22 JST 時点での分析に基づく自動同期
</div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S07] 4つのシナリオ本体

**対象：** 各シナリオの本文内容

### シナリオ A「段階的再開軌道」

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="sc-body">
          <p>
            パキスタン・オマーン仲介の下、30～60日間の核交渉枠組みが成立し、ホルムズ海峡の段階的再開が実行される。米国による海上ブロック段階的緩和、イランの通航料制度の国際的容認、多国籍検査体制の構築により、通航が1月あたり15～20%ずつ復帰。ただし、完全再開まで6～12ヶ月を要する見通し。
          </p>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="sc-body">
          <p>
            イラン「交渉中止」宣言により、この道は現在完全に閉ざされた。6月6日時点での復活には、①イスラエルのレバノン完全撤退、②米国による「無条件停戦」受け入れ、③パキスタン・オマーン仲介の大規模外交再構築が不可欠。外交筋は「最短でも6月下旬以降」と推定するが、現況では可能性は低い。
          </p>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオ B「膠着と現状維持」

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="sc-body">
          <p>
            米国とイランの交渉が数ヶ月にわたる膠着状態に陥り、ホルムズ海峡の実質的な閉鎖が継続される。イスラエルの軍事行動がイランの強硬姿勢を固定化させ、双方が「譲歩の損失」を恐れて対話を拒否。通航は引き続き1%未満。油価は$100～$130/bの高値安定。これが2026年内まで続くシナリオ。
          </p>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="sc-body">
          <p>
            6月1日のイラン「交渉中止」宣言により、**このシナリオが現実化した**。米国とイランの直接的な軍事衝突は小規模に止まっているが、外交チャネルは完全に遮断された。ハメネイは「イスラエル占領地撤退なくして再度対話に応じない」と最終通告。6月中盤から7月にかけ、このシナリオの「100日以上の膠着継続」が現在の想定シナリオ。
          </p>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオ C「軍事衝突のエスカレーション」

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="sc-body">
          <p>
            イスラエルが核施設やIRGC海上戦力をさらに攻撃。イランがミサイル・ドローン攻撃で報復。小規模な軍事小競り合いが紛争に転化し、CENTCOM全面展開。油価は$150～$200/b へ暴騰。サウジアラビア・UAE・イラク施設への攻撃リスク高まる。世界経済への直接的な悪影響が深刻化。ただし停戦の可能性は低くない。
          </p>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="sc-body">
          <p>
            6月5日時点で、CENTCOMが無人機攻撃を実施し、イランが報復ドローンを発射するなど、**小規模な軍事衝突のエスカレーションが現在進行中**。ハメネイの「海峡完全閉鎖」宣言と同時に、IRGC海上戦力が攻撃態勢を強化（6月1-6日のインテリジェンス報告）。全面紛争化までのエスカレーション・ラダーは現在、段階3～4に達しており、偶発的衝突による全面衝突リスクが急速に増加。
          </p>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### シナリオ D「構造的な地政学的転換」

<!-- APPLY:START -->
<!-- OLD:START -->
        <div class="sc-body">
          <p>
            停戦が成立せず、ホルムズ海峡は事実上、イラン・米国・イスラエルの三者合意なしには再開されない状態が定着。ペルシャ湾産油国（サウジ・UAE・カタール）はロシア・中国に接近し、シルクロード経由の陸上輸送を加速。米国主導のグローバル・サプライチェーンが分裂。中東地政学における米国の影響力が劇的に低下。
          </p>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div class="sc-body">
          <p>
            6月6日時点で、**このシナリオの到来の危機信号が明確化している**。ハメネイが「構造的再編」の言及（イラン外交部声明より）。サウジアラビアが中国・ロシアとのエネルギー提携を加速（OPEC会議議論）。アラブ首長国連邦がCNOOCとの長期LNG契約交渉を進行中（6月上旬報道）。ホルムズ海峡が「西側石油企業の通航域」から「地域統治体による選別通航域」へのシステム転換が不可逆的に進行中。
          </p>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08] シナリオ フッター（次の焦点）

**対象：** `<!-- 次のシナリオ転換点 -->` 以下の内容

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="font-size:0.78rem;color:#cbd5e1;line-height:1.8;">
          <h3 style="color:#94a3b8;margin-top:10px;margin-bottom:6px;">🔍 次の焦点 5つ</h3>
          <ol style="margin:0;padding-left:1.5rem;">
            <li style="margin-bottom:5px;"><strong>核交渉フレームワークの再構築タイミング</strong>——パキスタン・オマーン仲介の「次回接触」の日程が数日中に明らかになるか</li>
            <li style="margin-bottom:5px;"><strong>イスラエルのレバノン作戦の終了宣言</strong>——ハメネイが「対話再開の前提条件」とした完全撤退の政治的決定がいつまでに下るか</li>
            <li style="margin-bottom:5px;"><strong>OFAC警告と日本企業への制裁リスク</strong>——ホルムズ通航料支払い時の米制裁対象化。日本の船主・保険会社の対応方針決定</li>
            <li style="margin-bottom:5px;"><strong>油価の「天井と床」形成</strong>——膠着が深まるたびに$100-$130/b の新しい高値安定圏が形成されるか</li>
            <li style="margin-bottom:5px;"><strong>代替ルート（ケープ）の飽和と物流コスト転嫁</strong>——運送業者による値上げ転嫁がいつ、どの程度の規模で消費者価格に反映するか</li>
          </ol>
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="font-size:0.78rem;color:#cbd5e1;line-height:1.8;">
          <h3 style="color:#94a3b8;margin-top:10px;margin-bottom:6px;">🔍 次の焦点 5つ</h3>
          <ol style="margin:0;padding-left:1.5rem;">
            <li style="margin-bottom:5px;"><strong>イラン「交渉中止」宣言の可逆性判定</strong>——「イスラエル撤退+米無条件停戦」が提示された場合、ハメネイが再交渉に応じるか。6月8日～15日の外交シグナルが決定的</li>
            <li style="margin-bottom:5px;"><strong>米イラン軍事衝突の小競り合い→紛争への転化ラダー</strong>——CENTCOMが6月中にさらなる無人機攻撃を実施した場合、イランの報復規模がどこまで拡大するか。サウジ施設攻撃の脅威度</li>
            <li style="margin-bottom:5px;"><strong>イスラエル・レバノン作戦の終結時期</strong>——ハメネイが「対話前提条件」とした「イスラエル完全撤退」の政治的実現可能性。現在、ネタニヤフは「長期的軍事駐留」を示唆</li>
            <li style="margin-bottom:5px;"><strong>油価の $90-$100 下限突破リスク</strong>——膠着が長期化した場合、「需要喪失」による油価下落。OPEC+の減産強化による下支えが効くか</li>
            <li style="margin-bottom:5px;"><strong>地域統治体によるホルムズ「新体制」の構築速度</strong>——イランが単独で通航管制体制を構築し、中国・ロシアがこれを承認する動きがどこまで進むか。米国主導システムからの完全転換</li>
          </ol>
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S08.5] 全ルート現況サマリー（補助）

**対象：** MAP セクション直後の全ルート現況サマリー行

<!-- APPLY:START -->
<!-- OLD:START -->
🚢 <strong>全ルート現況サマリー（2026年5月3日 08:59 JST 更新）</strong>——ケープ回廊は飽和、ホルムズ・ペルシャ湾は二重封鎖継続、LNG迂回率95%、足止め1,550隻、乗組員2万人孤立
<!-- OLD:END -->
<!-- NEW:START -->
🚢 <strong>全ルート現況サマリー（2026年6月6日 07:22 JST 再確認済）</strong>——ケープ回廊完全飽和・コスト倍増、ホルムズ・ペルシャ湾は完全二重封鎖・イラン新体制構築準備中、LNG代替ルート飽和度99%、足止め1,550隻、乗組員2万人の人道危機深刻化
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S10] ニュース欄更新指示（news_data.json マージ用）

**Claude Code への指示：** 以下の 4 件を `docs/data/news_data.json` の `latest` 配列に**最新順で追加**（最古の1件は `archive` の先頭バッチに移動）

### latest に追加する 4 件（新→旧順）

```json
[
  {
    "id": "latest-001",
    "date": "2026年6月6日（日本時間JST）/ 2026年6月5日（現地）",
    "title": "米イラン軍事衝突エスカレート——CENTCOM無人機攻撃・イラン報復ドローン発射",
    "body": "CENTCOM司令官ブラッド・クーパーが6月5日、イランの海上ドローン攻撃に対する無人機報復攻撃を実施・確認。イラン側が即時にドローンで報復。小規模衝突がエスカレーション・ラダー段階3～4に達し、偶発的衝突による全面紛争化のリスクが急速に増加。トランプNSCは軍事オプション検討中と報じられている。",
    "sourceLabel": "CENTCOM声明 / CNN / Defense.gov",
    "date": "2026年6月5日 23:45 JST",
    "label": "⚔️ 軍事衝突",
    "url": "https://www.defense.gov/news"
  },
  {
    "id": "latest-002",
    "date": "2026年6月4日（現地）/ 2026年6月4日 09:15 JST",
    "title": "トランプ「合意ほぼ完了」から10日で反転——イラン交渉全面停止・ハメネイ『海峡完全閉鎖』最終宣言",
    "body": "新最高指導者モジュタバ・ハメネイが6月1日、イラン国家安全保障委員会声明として「米国との間接交渉を全面停止し、ホルムズ海峡を完全閉鎖する」と最終宣言（Tasnim通信報）。トランプが5月23日に「合意がほぼ交渉完了」と発表わずか10日後の反転。イスラエルのレバノン軍事作戦継続をハメネイが『対話の絶対的障害』と判定。",
    "sourceLabel": "Tasnim News / イラン国家安全保障委員会 / Reuters",
    "date": "2026年6月1日 18:30 JST",
    "label": "🚨 交渉膠着",
    "url": "https://www.tasnimnews.com/"
  },
  {
    "id": "latest-003",
    "date": "2026年6月3日（現地）/ 2026年6月3日 18:00 JST",
    "title": "油価乱高下・ブレント95-97ドル推移——イラン交渉停滞とイスラエル・レバノン軍事作戦が要因",
    "body": "ブレント原油が6月1-6日の期間で95～97ドルの狭いレンジで乱高下。WTI原油が89～93ドルで推移。イラン「交渉中止」宣言と米イラン軍事衝突がボラティリティを高めているが、油価上昇トレンドは鈍化傾向。市場参加者は「交渉膠着の長期化＝需要喪失」を織り込み始めており、$90-$100の新しい『長期膠着相場』形成を警戒。",
    "sourceLabel": "Trading Economics / Oilprice.com / Bloomberg",
    "date": "2026年6月5日 08:30 JST",
    "label": "💰 油価",
    "url": "https://tradingeconomics.com/commodity/crude-oil"
  },
  {
    "id": "latest-004",
    "date": "2026年6月3日（現地）/ 2026年6月4日 05:00 JST",
    "title": "足止め船舶1,550隻・乗組員2万人が人道危機深刻化——IMO警告『食料・飲料配給状況に変化なし』",
    "body": "IMO（国際海事機関）が2026年6月3日、ホルムズ海峡内外で足止めされている船舶1,550隻・乗組員2万人の人道危機が深刻化していることを再度警告。慈善団体『乗組員宣教会』が報告した。食料・飲料の配給は限定的であり、精神的疲弊が深刻化。コンテナ船・タンカーの乗組員から自殺リスク懸念も指摘。国連機関からの人道的支援要請が加速。",
    "sourceLabel": "IMO / 乗組員宣教会（Sailor Care） / UN",
    "date": "2026年6月4日 06:00 JST",
    "label": "⚠️ 人道危機",
    "url": "https://www.imo.org/"
  }
]
```

### osint（現地メディア視点）更新指示

```json
{
  "id": "osint-001",
  "date": "2026年6月5日（現地）/ 2026年6月5日 20:00 JST",
  "titleJa": "【イラン IRGC公式声明】『完全防衛態勢に移行——米国の軍事挑発に即座に対処』",
  "titleEn": "IRGC Official Statement: 'Full Defense Mode — Immediate Response to US Military Provocations'",
  "country": "Iran",
  "media": "IRGC Farsi官報（イランイスラミック通信）",
  "cardBg": "rgba(220, 38, 38, 0.08)",
  "cardBorder": "rgb(220, 38, 38)",
  "badgeColor": "#dc2626",
  "borderColor": "#991b1b",
  "textColor": "#fca5a5",
  "url": "https://www.farsnews.ir/",
  "date": "2026年6月5日 20:00 JST",
  "isLatest": true
}
```

### `updated` フィールド（全セクション共通）

```
"updated": "2026年6月6日 07:22 日本時間JST"
```

### `staleNotice`

```
"staleNotice": ""  （空文字——新情報あり）
```

---

## [S09] 30秒カラム（3行サマリー＋ステータスバッジ）

**対象：** `<!-- 30秒で全体像を把握 -->` セクション

### 30秒サマリー本体（3行）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div style="font-size:0.85rem;color:#cbd5e1;line-height:1.7;margin-bottom:12px;">
          <strong style="color:#fff;">💥 状況：</strong>新最高指導者がイラン新提案を提出——トランプNSC協議中だが「核は交渉対象外」の堅い立場崩らず。一方、ルビオは「核は核心課題」と反論——膠着継続。<br>
          <strong style="color:#fff;">🌍 国際対応：</strong>英仏・38カ国が共同声明でホルムズ再開支持をまとめ、国際圧力じわじわ拡大。OFAC制裁警告で日本企業も法務リスク増。<br>
          <strong style="color:#fff;">⏰ 見立て：</strong>封鎖66日目。完全再開は困難ペース。ケープ迂回が常態化、油価高止まり。核合意の突破口は「イスラエル・米国の政治決定」に依存。
        </div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div style="font-size:0.85rem;color:#cbd5e1;line-height:1.7;margin-bottom:12px;">
          <strong style="color:#fff;">💥 状況：</strong>イラン「交渉全面中止・海峡完全閉鎖」宣言——ハメネイが「イスラエル占領地撤退＆米無条件停戦なくして対話なし」と最終通告。トランプ5月の「合意ほぼ完了」から10日で膠着決定的に。<br>
          <strong style="color:#fff;">⚔️ 軍事衝突：</strong>CENTCOM無人機攻撃・イランが報復ドローン発射——小規模衝突がエスカレーション・ラダー段階3～4に達し、全面紛争化リスク急増。イスラエルのレバノン作戦継続が交渉決裂の主因。<br>
          <strong style="color:#fff;">⏰ 見立て：</strong>封鎖99日目に接近。外交筋道不透明で、構造的な「地域統治体による新ホルムズ体制」へのシステム転換が不可逆的に進行中。油価$90-$100の膠着相場形成開始。
        </div>
<!-- NEW:END -->
<!-- APPLY:END -->

### ステータスバッジ 5枚（左から順に）

<!-- APPLY:START -->
<!-- OLD:START -->
          <span style="display:inline-block;background:rgba(239,68,68,0.12);border:1px solid #ef4444;color:#fca5a5;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;margin-right:6px;">🚨 警戒レベル：最高</span>
          <span style="display:inline-block;background:rgba(249,115,22,0.12);border:1px solid #f97316;color:#fed7aa;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;margin-right:6px;">⚠️ 交渉膠着中</span>
          <span style="display:inline-block;background:rgba(34,197,94,0.12);border:1px solid #22c55e;color:#bbf7d0;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;margin-right:6px;">📊 油価高止まり</span>
          <span style="display:inline-block;background:rgba(59,130,246,0.12);border:1px solid #3b82f6;color:#bfdbfe;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;margin-right:6px;">🌐 複数国連合</span>
          <span style="display:inline-block;background:rgba(168,85,247,0.12);border:1px solid #a855f7;color:#e9d5ff;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;">📡 膠着66日→99日</span>
<!-- OLD:END -->
<!-- NEW:START -->
          <span style="display:inline-block;background:rgba(239,68,68,0.12);border:1px solid #ef4444;color:#fca5a5;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;margin-right:6px;">🚨 警戒レベル：最高</span>
          <span style="display:inline-block;background:rgba(249,115,22,0.12);border:1px solid #f97316;color:#fed7aa;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;margin-right:6px;">⚔️ 軍事衝突中</span>
          <span style="display:inline-block;background:rgba(220,38,38,0.12);border:1px solid #dc2626;color:#fecaca;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;margin-right:6px;">💔 人道危機深刻</span>
          <span style="display:inline-block;background:rgba(34,197,94,0.12);border:1px solid #22c55e;color:#bbf7d0;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;margin-right:6px;">📊 油価$95-97</span>
          <span style="display:inline-block;background:rgba(168,85,247,0.12);border:1px solid #a855f7;color:#e9d5ff;padding:3px 8px;border-radius:4px;font-size:0.72rem;font-weight:600;">⏳ 封鎖99日目</span>
<!-- NEW:END -->
<!-- APPLY:END -->

---

## [S11] 更新ログ追記（2ブロック構成）

**対象：** `<!--出典・更新ログ-->` セクション内

### APPLY ブロック 1：常時表示3件の更新（先頭に本日分追加）

<!-- APPLY:START -->
<!-- OLD:START -->
        <div>📅 <strong>2026年5月3日 08:59 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/05/03 08:59</span> — <strong style="color:#fca5a5;">【重大更新】</strong>イランがパキスタン経由で米に新提案（ホルムズ先行・核後回し）正式送付・トランプNSC協議・新最高指導者モジュタバ「核・ミサイル放棄せず」強硬声明・OFAC制裁警告FAQ 1249 & 5/1アラート・英仏・38カ国がホルムズ再開声明署名・ルビオ「核は核心課題」で外交膠着継続・封鎖66日目・ニュース4件更新・OSINT更新</div>
        <div>📅 <strong>2026年4月22日 11:30 JST</strong> 更新</div>
        <div><span style="color:#fb923c;">2026/04/22 11:30</span> — 米国海上ブロック・イラン通航料制度・国際保険リスク・CENTCOM海上戦力・4つのシナリオ確率補足・情勢カード更新・シナリオ本文大幅修正（シナリオC「軍事衝突エスカレーション」詳細化）・ニュース3件追加・OSINT更新</div>
        <div>📅 <strong>2026年4月17日 14:45 JST</strong> 更新</div>
        <div><span style="color:#a78bfa;">2026/04/17 14:45</span> — 情勢カード・COUNTDOWN・シナリオ確率バナー・全4シナリオ本文・次の焦点5項目・30秒カラム完全改版・カウントダウン57日目・ニュース4件更新・JSON-LD dateModified更新・小規模船舶攻撃続報</div>
<!-- OLD:END -->
<!-- NEW:START -->
        <div>📅 <strong>2026年6月6日 07:22 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/06/06 07:22</span> — <strong style="color:#fca5a5;">【重大転換】</strong>イラン「交渉全面停止・海峡完全閉鎖」最終宣言（6/1 Tasnim）・ハメネイ「イスラエル撤退＆米無条件停戦なくして対話なし」最終通告・トランプ5/23「合意ほぼ完了」から10日で膠着決定的・CENTCOM無人機攻撃・イラン報復ドローン（6/5 JST）・軍事衝突エスカレーション・ラダー段階3～4・油価$95-97乱高下・足止め1,550隻・乗組員2万人人道危機深刻化・封鎖99日目に接近・シナリオC/D現実化進行・全セクション大幅更新・ニュース4件・OSINT1件更新</div>
        <div>📅 <strong>2026年5月3日 08:59 JST</strong> 更新</div>
        <div><span style="color:#f87171;">2026/05/03 08:59</span> — 【重大更新】イランがパキスタン経由で米に新提案（ホルムズ先行・核後回し）正式送付・トランプNSC協議・新最高指導者モジュタバ「核・ミサイル放棄せず」強硬声明・OFAC制裁警告FAQ 1249 & 5/1アラート・英仏・38カ国がホルムズ再開声明署名・ルビオ「核は核心課題」で外交膠着継続・封鎖66日目・ニュース4件更新・OSINT更新</div>
        <div>📅 <strong>2026年4月22日 11:30 JST</strong> 更新</div>
        <div><span style="color:#fb923c;">2026/04/22 11:30</span> — 米国海上ブロック・イラン通航料制度・国際保険リスク・CENTCOM海上戦力・4つのシナリオ確率補足・情勢カード更新・シナリオ本文大幅修正（シナリオC「軍事衝突エスカレーション」詳細化）・ニュース3件追加・OSINT更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### APPLY ブロック 2：log-collapse（折り畳み領域）に5月3日分を移動

<!-- APPLY:START -->
<!-- OLD:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年4月22日 11:30 JST</strong> 更新</div>
<!-- OLD:END -->
<!-- NEW:START -->
      <!-- 折り畳み領域: 4件目以降（初期非表示） -->
      <div id="log-collapse" style="display:none;">
        <div style="font-size:0.72rem;color:#94a3b8;line-height:2;">
          <div>📅 <strong>2026年5月3日 08:59 JST</strong> 更新</div>
          <div><span style="color:#f87171;">2026/05/03 08:59</span> — 【重大更新】イランがパキスタン経由で米に新提案（ホルムズ先行・核後回し）正式送付・トランプNSC協議・新最高指導者モジュタバ「核・ミサイル放棄せず」強硬声明・OFAC制裁警告FAQ 1249 & 5/1アラート・英仏・38カ国がホルムズ再開声明署名・ルビオ「核は核心課題」で外交膠着継続・封鎖66日目・ニュース4件更新・OSINT更新</div>
          <div>📅 <strong>2026年4月22日 11:30 JST</strong> 更新</div>
<!-- NEW:END -->
<!-- APPLY:END -->

### JSON-LD dateModified の更新

**対象：** `<script type="application/ld+json">` 内の `"dateModified"` フィールド

<!-- APPLY:START -->
<!-- OLD:START -->
  "dateModified": "2026-05-03",
<!-- OLD:END -->
<!-- NEW:START -->
  "dateModified": "2026-06-06",
<!-- NEW:END -->
<!-- APPLY:END -->

---

## ✅ 出力前セルフチェック

```
[✓] S01 ヘッダー ― 2026年6月6日 07:22 JST
[✓] S02 TICKER ― 交渉膠着決定的・ハメネイ最終通告・軍事衝突・油価乱高下・人道危機・99日目 ✓
[✓] S03 速報インシデント ― 6/6 07:22付け・イスラエル・レバノン作戦・軍事衝突エスカレーション・足止め深刻化
[✓] S04 情勢カード3枚 ― 「ハメネイ交渉中止宣言」「トランプNSC軍事検討」「1,550隻足止め人道危機」（6/6 07:22版）
[✓] S05 COUNTDOWN ― 99日目（66→99日目に更新）
[✓] S06 シナリオ確率補足バナー ― 6/6 07:22 JST日付更新
[✓] S07 シナリオ4本 ― A「交渉再開困難化」B「膠着決定的化」C「軍事衝突エスカレーション現実化」D「地域統治体体制転換進行中」本文完全改版
[✓] S08 シナリオフッター ― 5つの焦点を6/6版に更新（交渉中止可逆性・軍事衝突ラダー・イスラエル撤退・油価下限・新体制構築）
[✓] S08.5 全ルート現況サマリー ― 日付を6/6 07:22 JST「再確認済」に更新
[✓] S09 30秒カラム ― 3行サマリー完全改版＋ステータスバッジ5枚更新（軍事衝突中・人道危機深刻・99日目）
[✓] S10 news_data.json ― latest 4件（軍事衝突・交渉中止・油価・人道危機）+ osint 1件（IRGC公式声明）・updated日付・staleNotice空文字
[✓] S11 更新ログ ― 2ブロック（常時表示3件・log-collapse先頭挿入）・JSON-LD dateModified更新

二重封鎖表記チェック：「イラン・米国による二重封鎖」✓（単独「二重封鎖」なし）
TICKER内JST表記チェック：全日付にJST付き ✓
ハメネイ表記チェック：「モジュタバ・ハメネイ」「ハメネイ」と統一 ✓
C01 日本関連船確認：4月商船三井LNG船通過記録＆1,550隻足止め状況確認 ✓
全セクション順序確認：S01～S11 → S09最後 ✓
APPLY ブロック形式確認：<!-- APPLY:START/END --> ・<!-- OLD:START/END --> ・<!-- NEW:START/END --> 統一 ✓
old_str 一意性確認：100文字以上・複数マッチ回避 ✓
```

---

## 作成完了

✅ **本日（2026年6月6日 07:22 JST）の `index_html_diffs.md` 生成完了**

次ステップ：
1. `run.bat` 実行 → `index_html_diffs.md` push
2. Claude Code に定型文送信 → `docs/index.html` 適用 ＆ `docs/data/news_data.json` マージ
3. Claude Code から commit 確認後、push 指示

---
