"""
Generate a self-contained HTML dashboard from data.json.
"""
import json
from datetime import datetime
from pathlib import Path


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Semiconductor Universe — Performance Tracker</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Manrope:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --bg:        #0a0d12;
  --bg-2:      #11151c;
  --bg-3:      #161b24;
  --panel:     #0f1319;
  --line:      #1f2630;
  --line-2:    #2a3340;
  --text:      #e8ecf2;
  --text-2:    #98a2b3;
  --text-3:    #667085;
  --accent:    #f5e6c8;
  --accent-2:  #d4af6a;
  --up:        #4ade80;
  --up-bg:     rgba(74,222,128,0.10);
  --down:      #f87171;
  --down-bg:   rgba(248,113,113,0.10);
  --neutral:   #64748b;
}
*  { box-sizing: border-box; }
html, body { margin:0; padding:0; background:var(--bg); color:var(--text); font-family:'Manrope', sans-serif; -webkit-font-smoothing:antialiased; }
body { min-height:100vh; }

/* ---------- Header ---------- */
.head {
  border-bottom: 1px solid var(--line);
  background: linear-gradient(180deg, #0d1117 0%, #0a0d12 100%);
  padding: 28px 32px 22px;
  position: sticky; top: 0; z-index: 50;
  backdrop-filter: blur(12px);
}
.head-row { display:flex; justify-content:space-between; align-items:flex-end; gap:24px; flex-wrap:wrap; }
.brand h1 {
  font-family:'Fraunces', serif; font-weight:400; font-style:italic;
  font-size: clamp(28px, 4vw, 44px); line-height:1; margin:0; letter-spacing:-0.02em;
  color: var(--accent);
}
.brand .sub { font-size:12px; color:var(--text-3); letter-spacing:0.18em; text-transform:uppercase; margin-top:10px; font-weight:500; }
.meta { font-family:'JetBrains Mono', monospace; font-size:11px; color:var(--text-3); text-align:right; line-height:1.6; }
.meta b { color:var(--text-2); font-weight:500; }
.meta .stat { color:var(--text); font-weight:600; }

/* ---------- Top movers strip ---------- */
.movers {
  display:grid; grid-template-columns: repeat(4, 1fr);
  gap:1px; background:var(--line); border-bottom:1px solid var(--line);
}
.mover { background:var(--bg); padding:14px 20px; }
.mover .lbl { font-size:10px; color:var(--text-3); text-transform:uppercase; letter-spacing:0.15em; font-weight:600; margin-bottom:6px; }
.mover .val { display:flex; align-items:baseline; gap:8px; font-family:'JetBrains Mono', monospace; }
.mover .tkr { font-size:14px; font-weight:700; color:var(--text); }
.mover .pct { font-size:14px; font-weight:600; }
.mover .nm { font-size:11px; color:var(--text-3); margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }

/* ---------- Controls ---------- */
.controls {
  display:flex; gap:12px; padding:18px 32px; background:var(--bg-2);
  border-bottom:1px solid var(--line); align-items:center; flex-wrap:wrap;
}
.controls input, .controls select {
  background:var(--bg-3); border:1px solid var(--line-2); color:var(--text);
  font-family:'Manrope',sans-serif; font-size:13px; padding:8px 12px; border-radius:6px;
  outline:none; transition: border-color .15s;
}
.controls input { width: 280px; }
.controls input:focus, .controls select:focus { border-color: var(--accent-2); }
.controls input::placeholder { color: var(--text-3); }
.controls select { cursor:pointer; }
.controls label { font-size:11px; color:var(--text-3); letter-spacing:0.1em; text-transform:uppercase; font-weight:600; margin-right:-4px; }
.spacer { flex:1; }
.count { font-family:'JetBrains Mono', monospace; font-size:12px; color:var(--text-2); }

/* ---------- Table ---------- */
.table-wrap { padding: 0 32px 64px; }
.cat-block { margin-top: 36px; scroll-margin-top: 140px; }
.cat-block:first-child { margin-top: 24px; }
.cat-block.highlight .cat-title { color: var(--accent); }
.cat-block.highlight .cat-title::before { background: var(--accent); width: 6px; }
.cat-title {
  display:flex; align-items:baseline; gap:14px;
  font-family:'Fraunces', serif; font-style:italic; font-weight:400;
  font-size: 22px; color: var(--text); margin: 0 0 12px 0; letter-spacing:-0.01em;
}
.cat-title .cat-count {
  font-family:'JetBrains Mono', monospace; font-style:normal; font-size:11px;
  color:var(--text-3); font-weight:500; letter-spacing:0.1em;
}
.cat-title::before {
  content:''; display:inline-block; width:3px; height:18px; background:var(--accent-2); border-radius:2px;
}

table { width:100%; border-collapse:collapse; font-size:13px; }
thead { position:sticky; top:0; }
thead th {
  background: var(--bg-2);
  color: var(--text-3); font-weight:600;
  text-transform:uppercase; font-size:10px; letter-spacing:0.12em;
  text-align:right; padding:10px 12px; border-bottom: 1px solid var(--line-2);
  cursor:pointer; user-select:none; white-space:nowrap;
}
thead th.left { text-align:left; }
thead th:hover { color: var(--accent); }
thead th .arrow { display:inline-block; width:10px; opacity:.6; }
tbody td {
  padding: 8px 12px; border-bottom: 1px solid var(--line);
  font-family:'JetBrains Mono', monospace; text-align:right; white-space:nowrap;
}
tbody td.left { text-align:left; font-family:'Manrope', sans-serif; }
tbody tr:hover td { background: var(--bg-2); }
.tkr { font-weight:700; color: var(--text); font-family:'JetBrains Mono', monospace; }
.nm  { color: var(--text-2); }
.ctry { font-size:10px; color: var(--text-3); padding: 2px 6px; border:1px solid var(--line-2); border-radius:3px; }
.px { color: var(--text); font-weight:500; }
.cur { font-size:10px; color:var(--text-3); margin-left:4px; }
.ret { font-weight:600; padding: 4px 8px; border-radius:4px; min-width:64px; display:inline-block; text-align:right; }
.ret.na { color: var(--text-3); font-weight:400; background: transparent; }

/* ---------- Sector heatmap ---------- */
.heatmap-wrap { padding: 32px 32px 0; }
.heatmap-head {
  display:flex; align-items:baseline; justify-content:space-between; flex-wrap:wrap; gap:12px;
  margin-bottom: 14px;
}
.heatmap-title {
  font-family:'Fraunces', serif; font-style:italic; font-weight:400;
  font-size: 26px; color: var(--text); margin:0; letter-spacing:-0.01em;
  display:flex; align-items:baseline; gap:14px;
}
.heatmap-title::before {
  content:''; display:inline-block; width:3px; height:22px; background:var(--accent); border-radius:2px;
  align-self:center;
}
.heatmap-toggle {
  display:flex; gap:0; border:1px solid var(--line-2); border-radius:6px; overflow:hidden;
  font-family:'JetBrains Mono', monospace;
}
.heatmap-toggle button {
  background:var(--bg-3); color:var(--text-2); border:none; cursor:pointer;
  font-family:inherit; font-size:11px; padding:7px 14px; letter-spacing:0.08em; text-transform:uppercase; font-weight:600;
  transition: all .15s;
}
.heatmap-toggle button + button { border-left:1px solid var(--line-2); }
.heatmap-toggle button:hover { color: var(--text); }
.heatmap-toggle button.active { background: var(--accent-2); color: var(--bg); }

.heatmap {
  width:100%; border-collapse:separate; border-spacing:0;
  background: var(--panel); border:1px solid var(--line); border-radius:8px; overflow:hidden;
}
.heatmap th, .heatmap td {
  padding: 10px 14px; font-size: 12px; text-align: right; border-bottom: 1px solid var(--line);
}
.heatmap th {
  background: var(--bg-2); color: var(--text-3); font-weight:600;
  text-transform:uppercase; font-size:10px; letter-spacing:0.12em;
  cursor:pointer; user-select:none;
}
.heatmap th:hover { color: var(--accent); }
.heatmap th.left, .heatmap td.left { text-align:left; }
.heatmap tbody tr {
  cursor: pointer;
  transition: background 0.12s;
}
.heatmap tbody tr:hover td { background: var(--bg-2); }
.heatmap tbody tr:hover td.left { background: var(--bg-3); }
.heatmap tbody tr:hover .cat-name { color: var(--accent); }
.heatmap tbody tr:last-child td { border-bottom: none; }
.heatmap .cat-name {
  font-family:'Manrope', sans-serif; font-weight:500; color: var(--text); font-size:13px;
}
.heatmap .cat-n { font-family:'JetBrains Mono', monospace; font-size:10px; color: var(--text-3); margin-left: 6px; }
.heatmap .hm-cell {
  font-family:'JetBrains Mono', monospace; font-weight:600; font-size:12px;
}

/* ---------- Footer ---------- */
.foot { padding: 32px; text-align:center; color: var(--text-3); font-size:12px; border-top:1px solid var(--line); margin-top:48px; }
.foot a { color: var(--accent-2); text-decoration:none; }

@media (max-width: 900px) {
  .head { padding: 20px 16px 16px; }
  .table-wrap { padding: 0 12px 32px; }
  .movers { grid-template-columns: repeat(2,1fr); }
  .controls { padding: 14px 16px; }
  .controls input { width: 100%; flex: 1 1 200px; }
  thead th, tbody td { padding: 8px 6px; font-size:11px; }
  .nm { display:none; }
}
</style>
</head>
<body>

<header class="head">
  <div class="head-row">
    <div class="brand">
      <h1>Semiconductor Universe</h1>
      <div class="sub">Multi-Timeframe Performance Tracker</div>
    </div>
    <div class="meta">
      <div>As of <b>__ASOF__</b></div>
      <div>Universe: <span class="stat">__N__ tickers</span> · <span class="stat">__CATS__ categories</span></div>
      <div>Generated <b>__GEN__</b></div>
    </div>
  </div>
</header>

<div class="movers" id="movers"></div>

<div class="heatmap-wrap">
  <div class="heatmap-head">
    <h2 class="heatmap-title">Sector Heatmap <span style="font-style:normal; font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--text-3); font-weight:500; letter-spacing:0.1em;">PERFORMANCE BY CATEGORY</span></h2>
    <div class="heatmap-toggle">
      <button data-agg="median" class="active">Median</button>
      <button data-agg="mean">Mean</button>
    </div>
  </div>
  <table class="heatmap" id="heatmap"></table>
</div>

<div class="controls">
  <input id="search" placeholder="Search ticker or name…" autocomplete="off">
  <label>Category</label>
  <select id="catFilter"><option value="">All categories</option></select>
  <label>Region</label>
  <select id="regionFilter">
    <option value="">All</option>
    <option value="US">US</option>
    <option value="TW">Taiwan</option>
    <option value="JP">Japan</option>
    <option value="KR">Korea</option>
    <option value="CN">China</option>
    <option value="DE">Germany</option>
    <option value="NL">Netherlands</option>
    <option value="FR">France</option>
    <option value="GB">UK</option>
    <option value="IL">Israel</option>
    <option value="CH">Switzerland</option>
    <option value="AT">Austria</option>
    <option value="CA">Canada</option>
    <option value="HK">Hong Kong</option>
  </select>
  <div class="spacer"></div>
  <span class="count" id="count"></span>
</div>

<div class="table-wrap" id="tableWrap"></div>

<footer class="foot">
  Data: Yahoo Finance via yfinance · Returns calculated from adjusted close (splits/dividends adjusted) · Re-run <code>python3 fetch_data.py &amp;&amp; python3 build_dashboard.py</code> for refresh
</footer>

<script>
const DATA = __DATA__;
const COLS = [
  {key:'ticker',   label:'Ticker',   left:true},
  {key:'name',     label:'Name',     left:true},
  {key:'country',  label:'Reg',      left:true},
  {key:'price',    label:'Price',    fmt:'price'},
  {key:'d1',       label:'1D',       fmt:'pct'},
  {key:'d7',       label:'1W',       fmt:'pct'},
  {key:'d14',      label:'2W',       fmt:'pct'},
  {key:'m1',       label:'1M',       fmt:'pct'},
  {key:'m3',       label:'3M',       fmt:'pct'},
  {key:'ytd',      label:'YTD',      fmt:'pct'},
  {key:'y1',       label:'1Y',       fmt:'pct'},
  {key:'y2',       label:'2Y',       fmt:'pct'},
];

let state = { sortKey: 'd1', sortDir: -1, search: '', cat: '', region: '' };
let hmState = { agg: 'median', sortKey: 'd1', sortDir: -1 };

const TF_COLS = [
  {key:'d1', label:'1D'},
  {key:'d7', label:'1W'},
  {key:'d14', label:'2W'},
  {key:'m1', label:'1M'},
  {key:'m3', label:'3M'},
  {key:'ytd', label:'YTD'},
  {key:'y1', label:'1Y'},
  {key:'y2', label:'2Y'},
];

function median(arr) {
  if (arr.length === 0) return null;
  const s = [...arr].sort((a,b) => a-b);
  const m = Math.floor(s.length / 2);
  return s.length % 2 === 0 ? (s[m-1] + s[m]) / 2 : s[m];
}
function mean(arr) {
  if (arr.length === 0) return null;
  return arr.reduce((a,b) => a+b, 0) / arr.length;
}

function aggregateByCategory(agg) {
  const cats = {};
  DATA.rows.forEach(r => {
    if (!cats[r.category]) cats[r.category] = { name: r.category, n: 0 };
    cats[r.category].n += 1;
    TF_COLS.forEach(c => {
      if (r[c.key] != null && !isNaN(r[c.key])) {
        (cats[r.category][c.key] = cats[r.category][c.key] || []).push(r[c.key]);
      }
    });
  });
  // Compute aggregate
  const fn = agg === 'mean' ? mean : median;
  return Object.values(cats).map(c => {
    const out = { name: c.name, n: c.n };
    TF_COLS.forEach(col => { out[col.key] = c[col.key] ? fn(c[col.key]) : null; });
    return out;
  });
}

function catId(cat) {
  return 'cat-' + cat.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function scrollToCategory(cat) {
  const id = catId(cat);
  const target = document.getElementById(id);
  if (!target) return;
  // Clear any prior highlights, add new one
  document.querySelectorAll('.cat-block.highlight').forEach(el => el.classList.remove('highlight'));
  target.classList.add('highlight');
  target.scrollIntoView({behavior: 'smooth', block: 'start'});
  // Auto-remove highlight after 2s
  setTimeout(() => target.classList.remove('highlight'), 2400);
}

function renderHeatmap() {
  const data = aggregateByCategory(hmState.agg);
  // Sort
  const k = hmState.sortKey, d = hmState.sortDir;
  data.sort((a,b) => {
    let va = a[k], vb = b[k];
    if (va == null && vb == null) return 0;
    if (va == null) return 1;
    if (vb == null) return -1;
    if (typeof va === 'string') return d * va.localeCompare(vb);
    return d * (vb - va);
  });

  const el = document.getElementById('heatmap');
  const arrow = (key) => hmState.sortKey === key ? (hmState.sortDir === -1 ? ' ▼' : ' ▲') : '';
  let html = '<thead><tr>';
  html += `<th class="left" data-k="name">Category${arrow('name')}</th>`;
  html += `<th data-k="n">N${arrow('n')}</th>`;
  TF_COLS.forEach(c => { html += `<th data-k="${c.key}">${c.label}${arrow(c.key)}</th>`; });
  html += '</tr></thead><tbody>';
  data.forEach(row => {
    html += '<tr>';
    html += `<td class="left"><span class="cat-name">${row.name}</span></td>`;
    html += `<td style="color:var(--text-3); font-family:'JetBrains Mono',monospace; font-size:11px;">${row.n}</td>`;
    TF_COLS.forEach(c => {
      const v = row[c.key];
      if (v == null) {
        html += `<td class="hm-cell" style="color:var(--text-3);">—</td>`;
      } else {
        const sign = v > 0 ? '+' : '';
        html += `<td class="hm-cell" style="${colorize(v)}">${sign}${v.toFixed(1)}%</td>`;
      }
    });
    html += '</tr>';
  });
  html += '</tbody>';
  el.innerHTML = html;

  // Wire row clicks - jump to category in per-ticker table
  el.querySelectorAll('tbody tr').forEach((tr, i) => {
    const cat = data[i].name;
    tr.addEventListener('click', () => scrollToCategory(cat));
  });

  // Wire sort headers
  el.querySelectorAll('th[data-k]').forEach(th => {
    th.onclick = (e) => {
      e.stopPropagation();
      const k = th.dataset.k;
      if (hmState.sortKey === k) hmState.sortDir = -hmState.sortDir;
      else { hmState.sortKey = k; hmState.sortDir = (k === 'name') ? 1 : -1; }
      renderHeatmap();
    };
  });
}

function fmtPrice(v, cur) {
  if (v == null) return '—';
  const s = v >= 1000 ? v.toLocaleString(undefined,{maximumFractionDigits:0})
          : v.toLocaleString(undefined,{minimumFractionDigits:2, maximumFractionDigits:2});
  return s + '<span class="cur">' + (cur || '') + '</span>';
}

function colorize(v) {
  // Heatmap: caps at ±20% for the strongest tint
  if (v == null || isNaN(v)) return '';
  const cap = 20;
  const t = Math.max(-1, Math.min(1, v / cap));
  if (t > 0) {
    const a = 0.06 + 0.32 * t;
    return `background: rgba(74,222,128,${a.toFixed(3)}); color: var(--up);`;
  } else if (t < 0) {
    const a = 0.06 + 0.32 * (-t);
    return `background: rgba(248,113,113,${a.toFixed(3)}); color: var(--down);`;
  }
  return 'color: var(--text-3);';
}

function fmtPct(v) {
  if (v == null || isNaN(v)) return '<span class="ret na">—</span>';
  const sign = v > 0 ? '+' : '';
  return `<span class="ret" style="${colorize(v)}">${sign}${v.toFixed(1)}%</span>`;
}

function topMovers() {
  const rows = DATA.rows.filter(r => r.d1 != null);
  if (rows.length === 0) return;
  const by = (k, dir) => [...rows].sort((a,b) => (dir*(b[k]-a[k])))[0];
  const best1d = by('d1', 1);
  const worst1d = by('d1', -1);
  const bestYTD = by('ytd', 1);
  const bestY1 = by('y1', 1);
  const slots = [
    {lbl:'Top 1D', r:best1d, key:'d1'},
    {lbl:'Worst 1D', r:worst1d, key:'d1'},
    {lbl:'Top YTD', r:bestYTD, key:'ytd'},
    {lbl:'Top 1Y', r:bestY1, key:'y1'},
  ];
  const html = slots.map(s => {
    const v = s.r[s.key];
    const pct = (v >= 0 ? '+' : '') + v.toFixed(1) + '%';
    const c = v >= 0 ? 'var(--up)' : 'var(--down)';
    return `<div class="mover">
      <div class="lbl">${s.lbl}</div>
      <div class="val"><span class="tkr">${s.r.ticker}</span><span class="pct" style="color:${c}">${pct}</span></div>
      <div class="nm">${s.r.name}</div>
    </div>`;
  }).join('');
  document.getElementById('movers').innerHTML = html;
}

function populateCats() {
  const cats = [...new Set(DATA.rows.map(r => r.category))];
  const sel = document.getElementById('catFilter');
  cats.forEach(c => {
    const o = document.createElement('option'); o.value = c; o.textContent = c; sel.appendChild(o);
  });
}

function filterRows() {
  const s = state.search.toLowerCase();
  return DATA.rows.filter(r => {
    if (state.cat && r.category !== state.cat) return false;
    if (state.region && r.country !== state.region) return false;
    if (s) {
      if (!(r.ticker.toLowerCase().includes(s) || r.name.toLowerCase().includes(s))) return false;
    }
    return true;
  });
}

function sortGroup(rows) {
  const k = state.sortKey, d = state.sortDir;
  return [...rows].sort((a,b) => {
    let va = a[k], vb = b[k];
    if (va == null && vb == null) return 0;
    if (va == null) return 1;
    if (vb == null) return -1;
    if (typeof va === 'string') return d * va.localeCompare(vb);
    return d * (va - vb) * -1;  // sortDir -1 = descending for numbers
  });
}

function render() {
  const filtered = filterRows();
  document.getElementById('count').textContent = `${filtered.length} of ${DATA.rows.length} tickers`;

  // Group by category
  const groups = {};
  filtered.forEach(r => { (groups[r.category] = groups[r.category] || []).push(r); });
  const catOrder = [...new Set(DATA.rows.map(r => r.category))]; // preserve original order
  const wrap = document.getElementById('tableWrap');
  wrap.innerHTML = '';

  catOrder.forEach(cat => {
    const rows = groups[cat];
    if (!rows || rows.length === 0) return;
    const block = document.createElement('div');
    block.className = 'cat-block';
    block.id = catId(cat);
    block.innerHTML = `<h2 class="cat-title">${cat} <span class="cat-count">${rows.length}</span></h2>`;

    const table = document.createElement('table');
    const thead = document.createElement('thead');
    const tr = document.createElement('tr');
    COLS.forEach(c => {
      const th = document.createElement('th');
      th.className = c.left ? 'left' : '';
      const arrow = state.sortKey === c.key ? (state.sortDir === -1 ? '▼' : '▲') : '';
      th.innerHTML = c.label + ' <span class="arrow">' + arrow + '</span>';
      th.onclick = () => {
        if (state.sortKey === c.key) state.sortDir = -state.sortDir;
        else { state.sortKey = c.key; state.sortDir = -1; }
        render();
      };
      tr.appendChild(th);
    });
    thead.appendChild(tr); table.appendChild(thead);

    const tbody = document.createElement('tbody');
    sortGroup(rows).forEach(r => {
      const trow = document.createElement('tr');
      COLS.forEach(c => {
        const td = document.createElement('td');
        if (c.left) td.className = 'left';
        let v = r[c.key];
        if (c.key === 'ticker')      td.innerHTML = `<span class="tkr">${v}</span>`;
        else if (c.key === 'name')   td.innerHTML = `<span class="nm">${v}</span>`;
        else if (c.key === 'country')td.innerHTML = `<span class="ctry">${v}</span>`;
        else if (c.fmt === 'price')  td.innerHTML = `<span class="px">${fmtPrice(v, r.currency)}</span>`;
        else if (c.fmt === 'pct')    td.innerHTML = fmtPct(v);
        else td.textContent = v ?? '—';
        trow.appendChild(td);
      });
      tbody.appendChild(trow);
    });
    table.appendChild(tbody);
    block.appendChild(table);
    wrap.appendChild(block);
  });
}

// --- wire up ---
document.getElementById('search').addEventListener('input', e => { state.search = e.target.value; render(); });
document.getElementById('catFilter').addEventListener('change', e => { state.cat = e.target.value; render(); });
document.getElementById('regionFilter').addEventListener('change', e => { state.region = e.target.value; render(); });

// Heatmap toggle (median / mean)
document.querySelectorAll('.heatmap-toggle button').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.heatmap-toggle button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    hmState.agg = btn.dataset.agg;
    renderHeatmap();
  });
});

populateCats();
topMovers();
renderHeatmap();
render();
</script>
</body>
</html>
"""


def main():
    with open("data.json") as f:
        data = json.load(f)

    rows = data["rows"]
    gen = data["generated_at"]
    asof = max((r.get("as_of") for r in rows if r.get("as_of")), default="—")
    cats = len({r["category"] for r in rows})

    # Pretty-print generated time
    try:
        dt = datetime.fromisoformat(gen.replace("Z", "+00:00"))
        gen_pretty = dt.strftime("%Y-%m-%d %H:%M UTC")
    except Exception:
        gen_pretty = gen

    html = (HTML_TEMPLATE
            .replace("__DATA__", json.dumps(data))
            .replace("__ASOF__", asof)
            .replace("__N__", str(len(rows)))
            .replace("__CATS__", str(cats))
            .replace("__GEN__", gen_pretty))

    out = Path("semiconductor_tracker.html")
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size//1024} KB)")


if __name__ == "__main__":
    main()
