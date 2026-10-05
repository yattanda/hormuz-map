/* 用語集のツールチップ（共通部品）
 *
 * 本文中の用語に点線の下線を付け、乗せる・タップする・Tab で短い説明を出す。
 * 用語と説明の正本は /data/glossary.json（tools/build_glossary.py が同じデータから /glossary/ を書き出す）。
 * 設計：tools/glossary-search-design.md §3・§11
 *
 * 使い方：
 *   <script defer src="/assets/glossary.js" data-zones=".article-body"></script>
 *   data-zones … 印を付ける区域のセレクタ。当たった要素1つが1区域で、各用語は区域ごとに最初の1回だけ印を付ける
 *   JS が後から描く区域は、描いた側が Glossary.annotate(要素または要素の並び) を呼ぶ
 *   Glossary.data は glossary.json の中身で解決する Promise（読めなければ null）
 *
 * 外部送信・Cookie・ストレージは使わない。glossary.json を読めなければ何もしない（本文はそのまま読める）。
 */
(function(){
  'use strict';

  var DATA_URL = '/data/glossary.json';
  var PAGE_URL = '/glossary/';
  // 印を付けない場所
  var SKIP = 'a,button,h1,h2,h3,h4,code,pre,script,style,textarea,input,select,.article-section-title,[data-glossary-skip]';

  var script = document.currentScript;
  var ZONES = (script && script.getAttribute('data-zones')) || '';

  var ready = false;      // glossary.json を読み終えたか
  var failed = false;
  var queue = [];         // 読み終える前に annotate() された要素
  var byMatch = {};       // 表記 → 用語
  var byId = {};
  var matcher = null;     // 全表記をまとめた正規表現（長い表記が先）

  function isAlnum(ch){ return !!ch && /[A-Za-z0-9]/.test(ch); }

  function build(data){
    var words = [];
    (data.terms || []).forEach(function(t){
      byId[t.id] = t;
      if(t.tooltip === false) return;
      (t.match || []).forEach(function(w){
        if(!w || byMatch[w]) return;
        byMatch[w] = t;
        words.push(w);
      });
    });
    if(!words.length) return;
    words.sort(function(a, b){ return b.length - a.length; });
    matcher = new RegExp(words.map(function(w){
      return w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }).join('|'), 'g');
  }

  // 英数字で始まる・終わる表記は、前後が英数字でないときだけ当てる（IAEA の中の IEA などを避ける）。
  // 後読み (?<!…) は古い iOS Safari で構文エラーになるため使わない
  function accept(text, index, word, term){
    if(isAlnum(word.charAt(0)) && isAlnum(text.charAt(index - 1))) return false;
    if(isAlnum(word.charAt(word.length - 1)) && isAlnum(text.charAt(index + word.length))) return false;
    var ex = term.except || [];
    for(var i = 0; i < ex.length; i++){
      if(text.substr(index, ex[i].length) === ex[i]) return false;
    }
    return true;
  }

  function annotateZone(zone){
    if(!matcher || !zone || zone.nodeType !== 1) return;
    var seen = {};
    // 既に印が付いている用語は数えておく（同じ区域を2回処理しても増えない）
    var done = zone.querySelectorAll('a.gl-term');
    for(var d = 0; d < done.length; d++) seen[done[d].getAttribute('data-term')] = true;

    var walker = document.createTreeWalker(zone, NodeFilter.SHOW_TEXT, null);
    var nodes = [], n;
    while((n = walker.nextNode())){
      if(!n.nodeValue || !n.nodeValue.trim()) continue;
      if(n.parentElement && n.parentElement.closest(SKIP)) continue;
      nodes.push(n);
    }
    nodes.forEach(function(node){
      var text = node.nodeValue, hits = [], m;
      matcher.lastIndex = 0;
      while((m = matcher.exec(text))){
        var term = byMatch[m[0]];
        if(!term || seen[term.id] || !accept(text, m.index, m[0], term)) continue;
        seen[term.id] = true;
        hits.push({index: m.index, word: m[0], term: term});
      }
      if(!hits.length) return;
      var frag = document.createDocumentFragment(), last = 0;
      hits.forEach(function(h){
        if(h.index > last) frag.appendChild(document.createTextNode(text.slice(last, h.index)));
        var a = document.createElement('a');
        a.className = 'gl-term';
        a.href = PAGE_URL + '#term-' + h.term.id;
        a.setAttribute('data-term', h.term.id);
        a.textContent = h.word;
        frag.appendChild(a);
        last = h.index + h.word.length;
      });
      if(last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
      node.parentNode.replaceChild(frag, node);
    });
  }

  function annotate(target){
    if(failed || !target) return;
    if(!ready){ queue.push(target); return; }
    if(target.nodeType === 1){ annotateZone(target); return; }
    for(var i = 0; i < target.length; i++) annotateZone(target[i]);
  }

  // ------------------------------------------------------------
  // ポップアップ（画面に1個だけ作って使い回す）
  // ------------------------------------------------------------
  var pop = null, popTerm = null, popShort = null, popMore = null;
  var current = null;     // いま説明を出している用語の要素
  var hideTimer = null;
  var lastPointer = 'mouse';

  var CSS =
    'a.gl-term{color:inherit;text-decoration:underline dotted;text-decoration-thickness:1px;text-underline-offset:3px;cursor:help;}' +
    'a.gl-term:focus-visible{outline:2px solid #d9a441;outline-offset:2px;border-radius:2px;}' +
    '.gl-pop{--gl-bg:#1c2128;--gl-fg:#e6e9ee;--gl-muted:#aab2bd;--gl-line:#3a424d;--gl-link:#e8b85a;' +
      'position:absolute;z-index:9999;box-sizing:border-box;width:min(320px,calc(100vw - 24px));' +
      'background:var(--gl-bg);color:var(--gl-fg);border:1px solid var(--gl-line);border-radius:8px;' +
      'padding:10px 12px 8px;font-size:14px;line-height:1.6;text-align:left;font-weight:400;letter-spacing:0;' +
      'box-shadow:0 6px 24px rgba(0,0,0,.35);}' +
    '.gl-pop[hidden]{display:none;}' +
    '.gl-pop-term{display:block;font-weight:700;font-size:14px;margin:0 0 2px;}' +
    '.gl-pop-short{margin:0 0 6px;color:var(--gl-fg);}' +
    '.gl-pop-more{display:inline-block;padding:6px 0;font-size:13px;color:var(--gl-link);text-decoration:none;}' +
    '.gl-pop-more:hover{text-decoration:underline;}';

  function ensurePop(){
    if(pop) return;
    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    pop = document.createElement('div');
    pop.className = 'gl-pop';
    pop.id = 'gl-pop';
    pop.setAttribute('role', 'tooltip');
    pop.hidden = true;
    popTerm = document.createElement('strong');
    popTerm.className = 'gl-pop-term';
    popShort = document.createElement('p');
    popShort.className = 'gl-pop-short';
    popMore = document.createElement('a');
    popMore.className = 'gl-pop-more';
    popMore.textContent = '用語集で読む →';
    pop.appendChild(popTerm);
    pop.appendChild(popShort);
    pop.appendChild(popMore);
    document.body.appendChild(pop);

    pop.addEventListener('pointerenter', function(){ clearTimeout(hideTimer); });
    pop.addEventListener('pointerleave', function(ev){ if(ev.pointerType === 'mouse') scheduleHide(); });
  }

  function show(el){
    var term = byId[el.getAttribute('data-term')];
    if(!term) return;
    ensurePop();
    clearTimeout(hideTimer);
    if(current && current !== el) current.removeAttribute('aria-describedby');
    current = el;
    popTerm.textContent = term.term;
    popShort.textContent = term.short;
    popMore.href = el.href;
    el.setAttribute('aria-describedby', 'gl-pop');
    pop.hidden = false;

    // 用語の上に出す。収まらなければ下。左右は画面内に収める
    var r = el.getBoundingClientRect();
    var vw = document.documentElement.clientWidth;
    var pw = pop.offsetWidth, ph = pop.offsetHeight;
    var left = Math.max(12, Math.min(r.left + r.width / 2 - pw / 2, vw - pw - 12));
    var top = (r.top - ph - 8 >= 0) ? r.top - ph - 8 : r.bottom + 8;
    pop.style.left = (left + window.pageXOffset) + 'px';
    pop.style.top = (top + window.pageYOffset) + 'px';
  }

  function hide(){
    clearTimeout(hideTimer);
    if(current) current.removeAttribute('aria-describedby');
    current = null;
    if(pop) pop.hidden = true;
  }

  function scheduleHide(){
    clearTimeout(hideTimer);
    hideTimer = setTimeout(hide, 150);   // ポップアップの中へ移る間の猶予
  }

  function termOf(node){
    return (node && node.closest) ? node.closest('a.gl-term') : null;
  }

  function setupEvents(){
    document.addEventListener('pointerdown', function(ev){ lastPointer = ev.pointerType || 'mouse'; }, true);
    document.addEventListener('pointerover', function(ev){
      if(ev.pointerType !== 'mouse') return;
      var el = termOf(ev.target);
      if(el) show(el);
    });
    document.addEventListener('pointerout', function(ev){
      if(ev.pointerType !== 'mouse') return;
      if(termOf(ev.target)) scheduleHide();
    });
    document.addEventListener('focusin', function(ev){
      var el = termOf(ev.target);
      if(el) show(el);
    });
    document.addEventListener('focusout', function(ev){
      if(termOf(ev.target)) scheduleHide();
    });
    document.addEventListener('click', function(ev){
      var el = termOf(ev.target);
      if(el){
        // タッチ：1回目のタップは移動せず説明を出す。説明の中の「用語集で読む」で移動する
        if(lastPointer !== 'mouse' && (current !== el || pop.hidden)){
          ev.preventDefault();
          show(el);
        }
        return;
      }
      if(pop && !pop.hidden && !pop.contains(ev.target)) hide();
    });
    document.addEventListener('keydown', function(ev){
      if(ev.key === 'Escape' && pop && !pop.hidden) hide();
    });
  }

  // ------------------------------------------------------------
  // 読み込み
  // ------------------------------------------------------------
  function start(){
    fetch(DATA_URL)
      .then(function(r){ if(!r.ok) throw new Error(String(r.status)); return r.json(); })
      .then(function(data){
        build(data);
        ready = true;
        resolveData(data);
        if(!matcher) return;
        ensurePop();
        setupEvents();
        if(ZONES) annotate(document.querySelectorAll(ZONES));
        queue.forEach(annotate);
        queue = [];
      })
      .catch(function(){ failed = true; queue = []; resolveData(null); });
  }

  // data … glossary.json の中身で解決する Promise（読めなければ null）。
  // 同じデータを使うページ（/archive/ の検索の同義語）が、もう一度読み込まずに済むようにする
  var resolveData;
  var dataPromise = new Promise(function(resolve){ resolveData = resolve; });

  window.Glossary = { annotate: annotate, data: dataPromise };

  function idle(fn){
    if('requestIdleCallback' in window) window.requestIdleCallback(fn, {timeout: 2000});
    else setTimeout(fn, 200);
  }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function(){ idle(start); });
  else idle(start);
})();
