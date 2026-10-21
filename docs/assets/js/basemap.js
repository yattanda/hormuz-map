/* 地図の背景（課題46 D3 PR 6a・2026-10-21）。CARTO のタイルをやめ、同梱のデータだけで陸・海・川・湖・地名を描く。
   設計：tools/site-redesign-design.md §4-2。データの作り方：tools/map/README.md。
   色は tokens.css の --map-*（案2「海図」・湾岸の9か国を少し暗く。運営者・10/21）。
   使い方：HormuzBasemap.init(map)。/hormuz/ の BASEMAP を 'carto' にすると、これは呼ばれず、前の CARTO の地図に戻る。

   層（下から）：
     bmBase(200)  Natural Earth の陸地。細かい海岸線の範囲は、その上を海の色の四角で塗りつぶす
     bmPatch(210) OpenStreetMap 由来の細かい陸地と、その上にだけ重ねる国の色（canvas の source-atop）
     bmWater(220) 湖・川・細かい海岸線・国境
     bmLabel(595) 地名（ルートの線 400・パナマの湖 580・運河 590 より上、印 600 より下）
   どの層も自分で経度 ±360° の3つの世界に描く。地図の複製の仕組み（1-B. WORLD WRAP）には乗せない（options.bmOwn） */
(function () {
  var HI = ['IR', 'SA', 'AE', 'YE', 'IQ', 'OM', 'BH', 'QA', 'KW'];   // 湾岸の9か国（明るい陸）
  var REG = ['gulf', 'red', 'panama', 'malacca', 'tsugaru'];          // 細かい海岸線の範囲
  var REG_ZOOM = 6;        // この拡大より手前では細かい海岸線を読まない（世界の全体では差が見えない）
  var WORLDS = [-360, 0, 360];
  var BASE = '/data/map/';

  // データに無い港（位置はおおよそ）。拡大 7 から
  var OWN = [[56.25, 26.18, 'ハサブ'], [51.55, 25.91, 'ラスラファン'], [57.77, 25.64, 'ジャスク'], [50.31, 29.24, 'カーグ島'], [56.27, 26.96, 'ゲシュム'],
    [54.88, 26.56, 'バンダルレンゲ'], [50.16, 26.64, 'ラスタヌラ'], [57.70, 19.66, 'ドゥクム']];
  // 海の名前 [経度, 緯度, 名前, 出す拡大]。ペルシャ湾は拡大 5 でマナマを消さないよう、試作の 26.9 から北へ寄せた
  var SEAS = [[51.8, 27.2, 'ペルシャ湾', 4], [58.8, 24.6, 'オマーン湾', 5], [38.4, 20.5, '紅海', 4], [63, 16, 'アラビア海', 3], [56.45, 26.62, 'ホルムズ海峡', 8],
    [43.35, 12.55, 'バベルマンデブ海峡', 8], [33.1, 28.7, 'スエズ湾', 7.5], [34.75, 28.6, 'アカバ湾', 8], [100.4, 3.6, 'マラッカ海峡', 6], [140.6, 41.47, '津軽海峡', 8],
    [-79.3, 8.3, 'パナマ湾', 8], [48, 12.5, 'アデン湾', 5]];
  // 国名。前の地図の一覧（23か国）に、範囲に陸がある8か国を足した。置く場所は、見えている範囲のその国の陸の上で空いている所
  var CN = { IR: 'イラン', SA: 'サウジアラビア', AE: 'UAE', OM: 'オマーン', YE: 'イエメン', IQ: 'イラク', KW: 'クウェート', BH: 'バーレーン', QA: 'カタール', PK: 'パキスタン', IN: 'インド',
    EG: 'エジプト', DJ: 'ジブチ', SO: 'ソマリア', JP: '日本', CN: '中国', MY: 'マレーシア', US: 'アメリカ', RU: 'ロシア', ZA: '南アフリカ', BR: 'ブラジル', IL: 'イスラエル', TR: 'トルコ',
    SD: 'スーダン', ER: 'エリトリア', ET: 'エチオピア', JO: 'ヨルダン', PA: 'パナマ', CO: 'コロンビア', ID: 'インドネシア', TH: 'タイ' };
  // サイトの本文に出てくる地名（2026-10-16 に数えたもの）と主な港。首都や国名より先に置く
  var KEY = {};
  ['ドバイ', 'アブダビ', 'マスカット', 'バスラ', 'ドーハ', 'マナマ', 'ソハール', 'ケルマーン', 'ブシェール', 'チャーバハール', 'ダーラン', 'フジャイラ', 'ジェッダ', 'アバダン', 'アフマディ', 'シャルジャ', 'バンダルアッバース', 'ジュベル・アリ',
    'メッカ', 'サヌア', 'アデン', 'タイズ', 'マディーナ', 'スエズ', 'ポートサイド', 'サアダ', 'アブハ', 'ジザン', 'アカバ', 'ヤンブー', 'ハッジャ', 'リダ', 'イスマイリア', 'シンガポール', 'パナマ市', 'コロン', 'バルボア'
  ].forEach(function (k) { KEY[k] = 1; });
  var RIVS = [[45.9, 32.6, 'チグリス川', 6.5], [44.9, 31.2, 'ユーフラテス川', 6.5], [48.3, 30.2, 'シャットゥルアラブ川', 8], [31.2, 26.5, 'ナイル川', 5.5], [68.6, 27.6, 'インダス川', 5.5]];

  function count(c) { return typeof c[0] === 'number' ? 1 : c.reduce(function (n, x) { return n + count(x); }, 0); }
  function bbox(g) {
    var b = [999, 999, -999, -999];
    (function w(c) { if (typeof c[0] === 'number') { if (c[0] < b[0]) b[0] = c[0]; if (c[1] < b[1]) b[1] = c[1]; if (c[0] > b[2]) b[2] = c[0]; if (c[1] > b[3]) b[3] = c[1]; } else c.forEach(w); })(g.coordinates);
    return b;
  }
  function hit(a, b) { return !(a[2] < b[0] || a[0] > b[2] || a[3] < b[1] || a[1] > b[3]); }
  function shift(dx) { return function (c) { return L.latLng(c[1], c[0] + dx); }; }
  function inRing(x, y, r) {
    var c = false;
    for (var i = 0, j = r.length - 1; i < r.length; j = i++) { if ((r[i][1] > y) !== (r[j][1] > y) && x < (r[j][0] - r[i][0]) * (y - r[i][1]) / (r[j][1] - r[i][1]) + r[i][0]) c = !c; }
    return c;
  }
  // 国名は、その国のいちばん大きい陸の上にだけ置く（試作では「イラン」がゲシュム島の上に出ることがあった）
  function mainPoly(f) {
    if (f._main) return f._main;
    var ps = f.geometry.type === 'Polygon' ? [f.geometry.coordinates] : f.geometry.coordinates, best = null, ba = -1;
    ps.forEach(function (p) { var b = bbox({ coordinates: p }), a = (b[2] - b[0]) * (b[3] - b[1]); if (a > ba) { ba = a; best = { ring: p[0], bb: b }; } });
    return (f._main = best);
  }

  function init(map) {
    var css = getComputedStyle(document.documentElement);
    var C = {}; ['sea', 'land', 'land-hi', 'coast', 'coast-hi', 'river'].forEach(function (k) { C[k] = css.getPropertyValue('--map-' + k).trim(); });
    [['bmBase', 200], ['bmPatch', 210], ['bmWater', 220], ['bmLabel', 595]].forEach(function (p) {
      if (!map.getPane(p[0])) { map.createPane(p[0]).style.zIndex = p[1]; }
    });
    map.getPane('bmLabel').style.pointerEvents = 'none';
    // 細かい陸地の層：先に塗った陸地の上にだけ、国の色を重ねる（source-atop）
    var Comp = L.Canvas.extend({
      _fillStroke: function (ctx, layer) {
        ctx.globalCompositeOperation = layer.options.gco || 'source-over';
        L.Canvas.prototype._fillStroke.call(this, ctx, layer);
        ctx.globalCompositeOperation = 'source-over';
      }
    });
    var rA = L.canvas({ pane: 'bmBase', padding: .3 }), rB = new Comp({ pane: 'bmPatch', padding: .3 }), rC = L.canvas({ pane: 'bmWater', padding: .3 });
    var D = { osm: {} }, G = {}, loading = {}, hiLayers = [];
    var OPT = { interactive: false, bmOwn: true };
    function o(x) { return L.extend({}, OPT, x); }
    function each(fc, st, g) { WORLDS.forEach(function (dx) { L.geoJSON(fc, o({ style: st, coordsToLatLng: shift(dx) })).addTo(g); }); }
    function haloW() {   // 国の色を粗い国の形の外へ 2.5km 広げる線の太さ（画素）
      var c = map.getCenter(), mpp = 40075016 * Math.cos(c.lat * Math.PI / 180) / (256 * Math.pow(2, map.getZoom()));
      return Math.max(1, 2 * 2500 / mpp);
    }
    function get(name) { return fetch(BASE + name).then(function (r) { if (!r.ok) throw new Error(name + ' ' + r.status); return r.json(); }); }

    function buildLand() {
      var fc = { type: 'FeatureCollection', features: D.land.features.concat(D.isl.features.map(function (f) { return { type: 'Feature', properties: { i: '' }, geometry: f.geometry }; })) };
      var g = L.layerGroup();
      each(fc, function (f) {
        var hi = HI.indexOf(f.properties.i) >= 0;
        return { renderer: rA, color: hi ? C['coast-hi'] : C.coast, weight: hi ? 1.1 : .7, fillColor: hi ? C['land-hi'] : C.land, fillOpacity: 1, opacity: 1 };
      }, g);
      G.land = g.addTo(map);
    }
    // 細かい海岸線の範囲（読み終えたものだけ）。範囲を読むたびに全部を描き直す（source-atop の重ね順を崩さないため）
    function buildOsm() {
      ['sea', 'patch', 'lines'].forEach(function (k) { if (G[k]) { map.removeLayer(G[k]); G[k] = null; } });
      hiLayers = [];
      var sea = L.layerGroup(), patch = L.layerGroup(), lines = L.layerGroup(), boxes = [], w = haloW();
      var regs = REG.filter(function (r) { return D.osm[r]; });
      if (!regs.length) return;
      regs.forEach(function (r) {
        var d = D.osm[r], b = d.box; boxes.push(b);
        WORLDS.forEach(function (dx) {
          // 範囲の縁の細い線を消すため、海の四角は 0.002度 内側に置く
          L.rectangle([[b[1] + .002, b[0] + dx + .002], [b[3] - .002, b[2] + dx - .002]], o({ renderer: rA, stroke: false, fillColor: C.sea, fillOpacity: 1 })).addTo(sea);
          L.geoJSON(d.land, o({ coordsToLatLng: shift(dx), style: function () { return { renderer: rB, stroke: false, fillColor: C.land, fillOpacity: 1 }; } })).addTo(patch);
          L.geoJSON(d.line, o({ coordsToLatLng: shift(dx), style: function () { return { renderer: rC, color: C['coast-hi'], weight: .9, opacity: 1 }; } })).addTo(lines);
          L.geoJSON(d.borders, o({ coordsToLatLng: shift(dx), style: function () { return { renderer: rC, color: C['coast-hi'], weight: 1.1, opacity: 1 }; } })).addTo(lines);
        });
      });
      // 湾岸の9か国は、粗い国の形の外へ 2.5km 分だけ色を広げてから、隣の国を塗り直す
      var inBox = D.land.features.filter(function (f) { var bb = f._bb || (f._bb = bbox(f.geometry)); return boxes.some(function (b) { return hit(bb, b); }); });
      var hi = { type: 'FeatureCollection', features: inBox.filter(function (f) { return HI.indexOf(f.properties.i) >= 0; }) };
      var lo = { type: 'FeatureCollection', features: inBox.filter(function (f) { return HI.indexOf(f.properties.i) < 0; }) };
      WORLDS.forEach(function (dx) {
        hiLayers.push(L.geoJSON(hi, o({ coordsToLatLng: shift(dx), style: function () {
          return { renderer: rB, gco: 'source-atop', color: C['land-hi'], weight: w, opacity: 1, lineJoin: 'round', fillColor: C['land-hi'], fillOpacity: 1 }; } })).addTo(patch));
        L.geoJSON(lo, o({ coordsToLatLng: shift(dx), style: function () { return { renderer: rB, gco: 'source-atop', stroke: false, fillColor: C.land, fillOpacity: 1 }; } })).addTo(patch);
        // 島は組み立てのときに決めた国（properties.i）の色で塗り直す（粗い国の形から 2.5km より沖の島のため）
        regs.forEach(function (r) {
          L.geoJSON(D.osm[r].land, o({ filter: function (f) { return f.properties.i != null; }, coordsToLatLng: shift(dx), style: function (f) {
            return { renderer: rB, stroke: false, fillColor: HI.indexOf(f.properties.i) >= 0 ? C['land-hi'] : C.land, fillOpacity: 1 }; } })).addTo(patch);
        });
      });
      G.sea = sea.addTo(map); G.patch = patch.addTo(map); G.lines = lines.addTo(map);
    }
    // 範囲の縁を除いた海岸線（縁に沿う辺は線にしない）
    function addLine(d) {
      var b = d.box, e = 1e-6, lines = [];
      function edge(p) { return Math.abs(p[0] - b[0]) < e || Math.abs(p[0] - b[2]) < e || Math.abs(p[1] - b[1]) < e || Math.abs(p[1] - b[3]) < e; }
      d.land.features.forEach(function (f) {
        f.geometry.coordinates.forEach(function (r) {
          var cur = [];
          for (var i = 0; i < r.length - 1; i++) {
            if (edge(r[i]) && edge(r[i + 1])) { if (cur.length > 1) lines.push(cur); cur = []; }
            else { if (!cur.length) cur.push(r[i]); cur.push(r[i + 1]); }
          }
          if (cur.length > 1) lines.push(cur);
        });
      });
      d.line = { type: 'Feature', properties: {}, geometry: { type: 'MultiLineString', coordinates: lines } };
    }
    function buildWater() {
      var g = L.layerGroup();
      each(D.lakes, function () { return { renderer: rC, color: C.river, weight: .6, fillColor: C.sea, fillOpacity: 1 }; }, g);
      each(D.rivers, function (f) { return { renderer: rC, color: C.river, weight: f.properties.s <= 3 ? 1.8 : f.properties.s <= 6 ? 1.2 : .8, opacity: 1 }; }, g);
      G.water = g.addTo(map);
    }
    // 細かい海岸線：範囲が画面に入り、拡大が REG_ZOOM 以上になったときに読む（設計書 R2）
    function loadRegions() {
      if (map.getZoom() < REG_ZOOM) return;
      var vb = map.getBounds(), c = map.getCenter().lng, off = 360 * Math.round(c / 360);
      var view = [vb.getWest() - off, vb.getSouth(), vb.getEast() - off, vb.getNorth()];
      REG.forEach(function (r) {
        if (D.osm[r] || loading[r] || !D.boxes[r] || !hit(D.boxes[r], view)) return;
        loading[r] = true;
        get('osm-' + r + '.json').then(function (d) { addLine(d); D.osm[r] = d; buildOsm(); })
          .catch(function (e) { loading[r] = false; console.warn('細かい海岸線の読み込みに失敗:', e); });
      });
    }

    // 地名
    var lbl = L.layerGroup().addTo(map);
    function icon(cls, txt, w, centered) {
      return L.divIcon({ className: 'bm-label', iconSize: [w, 16], iconAnchor: centered ? [w / 2, 8] : [3, 8], html: '<div class="bm-lb ' + cls + '" style="width:' + w + 'px">' + txt + '</div>' });
    }
    function labels() {
      lbl.clearLayers();
      var z = map.getZoom(), b = map.getBounds().pad(.05), c = map.getCenter().lng, boxes = [], n = 0;
      function near(x) { return x + 360 * Math.round((c - x) / 360); }
      // 重なったら後から置くほうを省く
      function tryAdd(x, y, txt, cls, centered) {
        var X = near(x); if (!b.contains([y, X])) return false;
        var p = map.latLngToContainerPoint([y, X]), w = txt.length * (cls === 'sea' ? 17 : cls === 'cty' ? 19 : 13) + 14;
        var bx = centered ? [p.x - w / 2, p.y - 9, p.x + w / 2, p.y + 9] : [p.x - 4, p.y - 9, p.x + w, p.y + 9];
        for (var i = 0; i < boxes.length; i++) { var q = boxes[i]; if (bx[0] < q[2] + 4 && bx[2] > q[0] - 4 && bx[1] < q[3] + 2 && bx[3] > q[1] - 2) return false; }
        boxes.push(bx); n++;
        L.marker([y, X], o({ icon: icon(cls, txt, w, centered), keyboard: false, pane: 'bmLabel' })).addTo(lbl);
        return true;
      }
      // 国名：見えている範囲とその国のいちばん大きい陸の重なりに 7×7 の候補を取り、真ん中に近い順に、陸の上でぶつからない最初の所に置く
      function placeCountries() {
        var ib = map.getBounds().pad(-.06), W = ib.getWest(), E = ib.getEast(), S = ib.getSouth(), N = ib.getNorth();
        Object.keys(CN).forEach(function (iso) {
          var f = D.byIso[iso]; if (!f) return; var m = mainPoly(f), bb = m.bb;
          var off = 360 * Math.round((c - (bb[0] + bb[2]) / 2) / 360), x0 = Math.max(W, bb[0] + off), x1 = Math.min(E, bb[2] + off), y0 = Math.max(S, bb[1]), y1 = Math.min(N, bb[3]);
          if (x0 >= x1 || y0 >= y1) return;
          var cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, ps = [];
          for (var i = 0; i < 7; i++) for (var j = 0; j < 7; j++) ps.push([x0 + (x1 - x0) * (i + .5) / 7, y0 + (y1 - y0) * (j + .5) / 7]);
          ps.sort(function (p, q) { return (p[0] - cx) * (p[0] - cx) + (p[1] - cy) * (p[1] - cy) - ((q[0] - cx) * (q[0] - cx) + (q[1] - cy) * (q[1] - cy)); });
          for (var k = 0; k < ps.length; k++) { if (!inRing(ps[k][0] - off, ps[k][1], m.ring)) continue; if (tryAdd(ps[k][0], ps[k][1], CN[iso], 'cty', true)) return; }
        });
      }
      // 置く順：海の名前 → 自前の港 → 本文に出てくる地名 → 首都と州都（国の首都が先） → 国名 → ほかの都市 → 川
      SEAS.forEach(function (s) { if (z >= s[3]) tryAdd(s[0], s[1], s[2], 'sea', true); });
      var lim = z + 0.6, byRank = function (a, b) { return (b[6] - a[6]) || (a[4] - b[4]) || (b[5] - a[5]); };
      if (z >= 7) OWN.forEach(function (p) { tryAdd(p[0], p[1], p[2], 'own', false); });
      D.places.filter(function (r) { return KEY[r[2]] && r[3] <= lim; }).sort(byRank).forEach(function (r) { tryAdd(r[0], r[1], r[2], r[6] ? 'cap' : '', false); });
      D.places.filter(function (r) { return !KEY[r[2]] && r[6] > 0 && r[3] <= lim; }).sort(byRank).forEach(function (r) { if (n < 70) tryAdd(r[0], r[1], r[2], 'cap', false); });
      placeCountries();
      var cand = D.places.filter(function (r) { return r[3] <= lim && r[6] === 0 && !KEY[r[2]]; }).sort(byRank);
      for (var i = 0; i < cand.length && n < 90; i++) tryAdd(cand[i][0], cand[i][1], cand[i][2], '', false);
      RIVS.forEach(function (s) { if (z >= s[3]) tryAdd(s[0], s[1], s[2], 'riv', true); });
    }

    return Promise.all([get('land.json'), get('islands.json'), get('places.json'), get('rivers.json'), get('lakes.json'), get('regions.json')]).then(function (a) {
      D.land = a[0]; D.isl = a[1]; D.places = a[2]; D.rivers = a[3]; D.lakes = a[4]; D.boxes = a[5];
      D.byIso = {}; D.land.features.forEach(function (f) { D.byIso[f.properties.i] = f; });
      buildLand(); buildWater(); labels();
      map.on('moveend', labels);
      map.on('moveend', loadRegions); loadRegions();
      map.on('zoomend', function () { var w = haloW(); hiLayers.forEach(function (h) { h.setStyle({ weight: w }); }); });
    });
  }

  window.HormuzBasemap = { init: init };
})();
