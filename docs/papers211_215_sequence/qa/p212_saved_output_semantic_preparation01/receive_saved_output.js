'use strict';

/*
 * SOURCE_ONLY preparation; not parsed as JavaScript, imported or executed.
 * Future use requires separately approved, pinned runtime/binding reception.
 * New closed author-side implementation of the complete P212 output contract.
 * Mathematical/source familiarity and author reuse are disclosed; this is
 * neither an independent manuscript review nor an all-parameter theorem test.
 * Reads only one explicit binding and its three explicit pinned files.
 * No submitted-code import, process spawning, network, environment read,
 * canonical access, filesystem write, or producer invocation exists here.
 */
const fs = require('node:fs');
const crypto = require('node:crypto');
const path = require('node:path');

const PARAMETERS = {
  schema: 'p212-parameters-v1', carrier_sizes: [1, 2, 3, 4], label_base: 1,
  carrier: '[n]^2 x [n]^[n]',
  state_order: 'lexicographic (u,v,f(1),...,f(n))',
  update: 'R(u,v,f)=(v,f(v),f[v:=u]); simultaneous old-state RHS',
  edge_identity: 'none; undirected multiplicities only', loop_degree: 2,
  series_max_core_size: 4,
  fixed_iterates: 'all integers 1 through the predicted maximum period in each carrier',
  expected_state_counts: [1, 16, 243, 4096], expected_total_states: 4356,
  unobserved_core_first_sizes: [5, 6, 5], output_schema: 'p212-full-output-v1'
};
const PARAMETER_SHA256 = '0870d9de8a1e2dde2c568656ea69b39511ae3a8ebf992f787c6e5ae060ca4550';
const FAMILIES = ['figure_eight', 'barbell', 'theta'];
const ROWS = [
  'figure_eight_double_loop', 'figure_eight_short_nontrivial', 'figure_eight_long',
  'barbell_short', 'barbell_long', 'theta_triple_direct', 'theta_other'
];
const ROW_FIRST = [1, 2, 3, 2, 4, 2, 3];
const LIMITS = [
  ['figure_eight_both_cycles_long', 5],
  ['barbell_both_cycles_long', 6],
  ['theta_all_paths_nondirect', 5]
];
const NAMES = [
  'carrier_size', 'successor_in_carrier', 'inverse_in_carrier',
  'inverse_after_forward', 'forward_after_inverse', 'unit_fibre',
  'invariant_matrix', 'active_component_bicyclic', 'registers_in_core',
  'core_bicyclic', 'core_minimum_degree', 'core_stored_arrows_internal',
  'frozen_complement', 'core_key_invariant', 'pruned_arrows_toward_core',
  'orbit_closure', 'orbit_no_preperiod', 'orbit_partition',
  'orbit_exact_period', 'orbit_group_constant', 'orbit_anchor_nonempty',
  'group_catalogue_complete', 'group_anchor_states', 'group_decoration_classes',
  'group_orbit_decoration_bijection', 'group_orbit_count', 'group_periods',
  'core_catalogue_graph_count', 'core_catalogue_orbit_census',
  'core_series_family', 'core_series_total', 'core_series_hand_control',
  'univariate_rational_identity', 'univariate_closed_coefficient',
  'period_weighted_core_identity', 'carrier_period_polynomial',
  'carrier_hand_control', 'carrier_orbit_total', 'carrier_weighted_total',
  'carrier_period_set', 'carrier_maximum_period', 'carrier_fixed_states',
  'fixed_iterate_count', 'seven_row_coverage', 'finite_coverage_limits',
  'total_carrier_states'
];
const EXCLUDED = [
  'No finite computation proves the all-n theorem.',
  'No finite observation of the three first-size 5/6/5 families is claimed.',
  'No independent manuscript review, global novelty, priority, or publication acceptance is claimed.',
  'Known kernel, inverse, zero preperiod, unit fibres, invariant, and standard counting are not new axes.'
];
const CORE_CONTROL_ROWS = [
  [[1, 1, 1]],
  [[2, 1, 2], [3, 1, 1], [4, 1, 2]],
  [[4, 1, 2], [5, 1, 1], [6, 1, 2], [8, 1, 1]],
  [[6, 1, 2], [7, 1, 1], [8, 1, 2], [10, 2, 1], [12, 1, 2]]
];
const CARRIER_CONTROL_ROWS = [
  [[1, 1]],
  [[1, 4], [2, 1], [3, 2], [4, 1]],
  [[1, 27], [2, 9], [3, 18], [4, 12], [5, 6], [6, 3], [8, 6]],
  [[1, 256], [2, 96], [3, 192], [4, 144], [5, 96], [6, 60],
   [7, 24], [8, 108], [10, 48], [12, 12]]
];
let checks = 0;
function need(ok, label) {
  checks += 1;
  if (!ok) throw new Error(label);
}
function asciiString(s) {
  return JSON.stringify(s).replace(/[\u007f-\uffff]/g,
    c => '\\u' + c.charCodeAt(0).toString(16).padStart(4, '0'));
}
function canon(v) {
  if (Array.isArray(v)) return '[' + v.map(canon).join(',') + ']';
  if (v !== null && typeof v === 'object')
    return '{' + Object.keys(v).sort().map(k => asciiString(k) + ':' + canon(v[k])).join(',') + '}';
  if (typeof v === 'string') return asciiString(v);
  if (typeof v === 'boolean') return v ? 'true' : 'false';
  if (typeof v === 'number' && Number.isSafeInteger(v) && !Object.is(v, -0)) return String(v);
  throw new Error('noncontract value reached canonical serializer');
}
function deep(a, b, where) {
  need(typeof a === typeof b && Array.isArray(a) === Array.isArray(b), where + ': type');
  if (Array.isArray(b)) {
    need(a.length === b.length, where + ': array length');
    for (let i = 0; i < b.length; i += 1) deep(a[i], b[i], where + '/' + i);
  } else if (b !== null && typeof b === 'object') {
    need(a !== null, where + ': nonnull object');
    const ak = Object.keys(a).sort(), bk = Object.keys(b).sort();
    need(ak.length === bk.length && ak.every((k, i) => k === bk[i]), where + ': exact keys');
    for (const k of bk) deep(a[k], b[k], where + '/' + k);
  } else {
    need(a === b && !(typeof a === 'number' && Object.is(a, -0)), where + ': value');
  }
}
function shape(v, keys, where) {
  need(v !== null && typeof v === 'object' && !Array.isArray(v), where + ': object');
  const actual = Object.keys(v).sort(), wanted = keys.slice().sort();
  need(actual.length === wanted.length && actual.every((k, i) => k === wanted[i]),
    where + ': exact keys');
}

// This parser rejects duplicate keys before assigning, all decimal/exponent
// tokens, null/nonfinite values, unsafe integers, malformed UTF-8 and -0.
// It is used for binding, parameter and output documents, not submitted code.
function parseStrict(bytes, label, requireWire = false) {
  const text = bytes.toString('utf8');
  need(Buffer.from(text, 'utf8').equals(bytes), label + ': exact UTF-8 decoding');
  if (requireWire) need(bytes.every(x => x < 128), label + ': ASCII bytes only');
  let i = 0;
  const skip = () => { while (i < text.length && /[ \t\r\n]/.test(text[i])) i += 1; };
  function string() {
    need(text[i] === '"', label + ': string start');
    const start = i++;
    let closed = false;
    while (i < text.length) {
      const c = text[i++];
      if (c === '\\') { need(i < text.length, label + ': string escape'); i += 1; }
      else if (c === '"') { closed = true; break; }
    }
    need(closed, label + ': terminated string');
    const value = JSON.parse(text.slice(start, i));
    need(typeof value === 'string', label + ': parsed string');
    return value;
  }
  function value(depth) {
    need(depth <= 128, label + ': bounded structural depth');
    skip();
    const c = text[i];
    if (c === '"') return string();
    if (c === '{') {
      i += 1; skip();
      const obj = Object.create(null), seen = new Set();
      if (text[i] === '}') { i += 1; return obj; }
      while (true) {
        skip(); const key = string();
        need(!seen.has(key), label + ': duplicate object key ' + key); seen.add(key);
        skip(); need(text[i++] === ':', label + ': object colon');
        obj[key] = value(depth + 1); skip();
        const separator = text[i++];
        if (separator === '}') return obj;
        need(separator === ',', label + ': object separator');
      }
    }
    if (c === '[') {
      i += 1; skip(); const out = [];
      if (text[i] === ']') { i += 1; return out; }
      while (true) {
        out.push(value(depth + 1)); skip();
        const separator = text[i++];
        if (separator === ']') return out;
        need(separator === ',', label + ': array separator');
      }
    }
    if (text.slice(i, i + 4) === 'true') { i += 4; return true; }
    if (text.slice(i, i + 5) === 'false') { i += 5; return false; }
    const match = /^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?/.exec(text.slice(i));
    need(match !== null, label + ': integer/Boolean/array/object/string token required');
    const token = match[0];
    need(!/[.eE]/.test(token) && token !== '-0', label + ': integer token only');
    const number = Number(token);
    need(Number.isSafeInteger(number), label + ': safe finite integer');
    i += token.length; return number;
  }
  const out = value(0); skip(); need(i === text.length, label + ': no trailing bytes');
  if (requireWire) need(Buffer.from(canon(out) + '\n', 'ascii').equals(bytes),
    label + ': complete sorted compact ASCII JSON plus exactly one LF');
  return out;
}
function compare(a, b) {
  if (Array.isArray(a) && Array.isArray(b)) {
    for (let i = 0; i < Math.min(a.length, b.length); i += 1) {
      const c = compare(a[i], b[i]); if (c) return c;
    }
    return a.length - b.length;
  }
  return a < b ? -1 : a > b ? 1 : 0;
}
const sorted = xs => xs.slice().sort(compare);
const unique = xs => sorted([...new Map(xs.map(x => [canon(x), x])).values()]);
const range = (start, stop) => Array.from({length: Math.max(0, stop - start)}, (_, i) => start + i);
const sum = xs => xs.reduce((a, b) => a + b, 0);
const factorial = n => range(1, n + 1).reduce((a, b) => a * b, 1);
function* tuples(values, count, prefix = []) {
  if (count === 0) { yield prefix; return; }
  for (const v of values) yield* tuples(values, count - 1, prefix.concat([v]));
}
function* subsets(values, count, start = 0, prefix = []) {
  if (count === 0) { yield prefix; return; }
  for (let i = start; i <= values.length - count; i += 1)
    yield* subsets(values, count - 1, i + 1, prefix.concat([values[i]]));
}
function* allocations(total, slots, prefix = []) {
  if (slots === 1) { yield prefix.concat([total]); return; }
  for (let x = 0; x <= total; x += 1)
    yield* allocations(total - x, slots - 1, prefix.concat([x]));
}
function* permutations(xs) {
  if (!xs.length) { yield []; return; }
  for (let i = 0; i < xs.length; i += 1)
    for (const tail of permutations(xs.filter((_, j) => j !== i))) yield [xs[i], ...tail];
}

// Exact reduced rationals use BigInt internally and safe integer pairs on wire.
const abs = x => x < 0n ? -x : x;
function gcd(a, b) { a = abs(a); b = abs(b); while (b) { const r = a % b; a = b; b = r; } return a; }
function rat(a, b = 1) {
  a = BigInt(a); b = BigInt(b); need(b !== 0n, 'nonzero rational denominator');
  if (b < 0n) { a = -a; b = -b; }
  const g = gcd(a, b); return [a / g, b / g];
}
const radd = (a, b) => rat(a[0] * b[1] + b[0] * a[1], a[1] * b[1]);
const rmul = (a, b) => rat(a[0] * b[0], a[1] * b[1]);
const rsum = xs => xs.reduce(radd, rat(0));
function safeBig(x) {
  const n = Number(x); need(Number.isSafeInteger(n) && BigInt(n) === x, 'exact safe rational wire integer');
  return n;
}
const rwire = r => [safeBig(r[0]), safeBig(r[1])];
function integer(r) { need(r[1] === 1n, 'integral reconstructed count'); return safeBig(r[0]); }
function put(map, key, value) {
  const v = radd(map.get(key) || rat(0), value);
  if (v[0]) map.set(key, v); else map.delete(key);
}
const polyWire = p => [...p].sort((a, b) => a[0] - b[0]).filter(x => x[1][0]).map(([k, v]) => [k, ...rwire(v)]);
const fromPolyRows = rows => new Map(rows.map(([p, a, b = 1]) => [p, rat(a, b)]));
const polyScale = (p, k) => new Map([...p].map(([p0, v]) => [p0, rmul(v, rat(k))]));
function polySum(...ps) { const out = new Map(); for (const p of ps) for (const [k, v] of p) put(out, k, v); return out; }
function periodCounts(periods) { const out = new Map(); for (const p of periods) put(out, p, rat(1)); return out; }
function monomial(s, p, a = 1, b = 1) {
  return s <= 4 && a !== 0 ? new Map([[s + ',' + p, rat(a, b)]]) : new Map();
}
function seriesAdd(...ps) { const out = new Map(); for (const p of ps) for (const [k, v] of p) put(out, k, v); return out; }
function seriesScale(p, a, b = 1) { return new Map([...p].map(([k, v]) => [k, rmul(v, rat(a, b))]).filter(x => x[1][0])); }
function seriesMultiply(a, b) {
  const out = new Map();
  for (const [ka, va] of a) for (const [kb, vb] of b) {
    const [sa, pa] = ka.split(',').map(Number), [sb, pb] = kb.split(',').map(Number);
    if (sa + sb <= 4) put(out, (sa + sb) + ',' + (pa + pb), rmul(va, vb));
  }
  return out;
}
function seriesPower(p, n) {
  let out = monomial(0, 0);
  for (let i = 0; i < n; i += 1) out = seriesMultiply(out, p);
  return out;
}
const geometric = step => new Map(range(0, 5).map(s => [s + ',' + (step * s), rat(1)]));
const bySize = (series, s) => new Map([...series].filter(([k]) => Number(k.split(',')[0]) === s)
  .map(([k, v]) => [Number(k.split(',')[1]), v]));
const seriesWire = series => [...series].map(([k, v]) => [...k.split(',').map(Number), ...rwire(v)])
  .filter(r => r[2] !== 0).sort((a, b) => compare(a.slice(0, 2), b.slice(0, 2)));
function formulaSeries() {
  const x = monomial(1, 2), one = monomial(0, 0), g = geometric(2);
  const q = seriesMultiply(x, g);
  const d = seriesAdd(seriesPower(g, 2), seriesScale(seriesPower(seriesAdd(one, x), 2), -1));
  const figure = seriesAdd(monomial(1, 1), monomial(2, 3), monomial(3, 4, 1, 2),
    seriesScale(seriesMultiply(monomial(1, 4), d), 1, 4));
  const barbell = seriesAdd(
    seriesScale(seriesMultiply(seriesMultiply(monomial(2, 4),
      seriesPower(seriesAdd(one, monomial(1, 1)), 2)), g), 1, 2),
    seriesScale(seriesMultiply(seriesMultiply(monomial(2, 8), d), geometric(4)), 1, 4));
  const theta = seriesAdd(monomial(2, 2, 1, 2),
    seriesScale(seriesMultiply(monomial(2, 6),
      seriesAdd(q, seriesPower(q, 2), seriesScale(seriesPower(q, 3), 1, 3))), 1, 2));
  return {pieces: [figure, barbell, theta], total: seriesAdd(figure, barbell, theta)};
}

const blank = n => range(0, n).map(() => Array(n).fill(0));
function edge(m, a, b, delta) { m[a - 1][b - 1] += delta; if (a !== b) m[b - 1][a - 1] += delta; }
const degree = (m, a, vertices) => sum(vertices.map(b => m[a - 1][b - 1])) + m[a - 1][a - 1];
const upper = (m, vs) => vs.flatMap(a => vs.filter(b => b >= a).map(b => m[a - 1][b - 1]));
const restricted = (m, vs) => vs.map(a => vs.map(b => m[a - 1][b - 1]));
function component(m, seed, vs) {
  const reached = new Set([seed]), queue = [seed];
  for (const a of queue) for (const b of vs)
    if (m[a - 1][b - 1] && !reached.has(b)) { reached.add(b); queue.push(b); }
  return sorted([...reached]);
}
function forward(state) {
  const [u, v] = state, f = state.slice(2), target = f[v - 1];
  f[v - 1] = u; return [v, target, ...f];
}
function inverse(state) {
  const [a, b] = state, f = state.slice(2), predecessor = f[a - 1];
  f[a - 1] = b; return [predecessor, a, ...f];
}
const stateObject = s => ({u: s[0], v: s[1], f: s.slice(2)});
function stateId(state, n) {
  need(state.length === n + 2 && state.every(x => Number.isInteger(x) && x >= 1 && x <= n),
    'reconstructed state lies in complete carrier');
  return state.reduce((id, x) => id * n + x - 1, 0);
}
function structural(state) {
  const n = state.length - 2, vs = range(1, n + 1), m = blank(n);
  for (const a of vs) edge(m, a, state[a + 1], 1);
  edge(m, state[0], state[1], 1);
  const active = component(m, state[0], vs), alive = new Set(active), pruning = [];
  while (true) {
    const current = sorted([...alive]), leaf = current.find(a => degree(m, a, current) === 1);
    if (leaf === undefined) break;
    const neighbors = current.filter(b => m[leaf - 1][b - 1] > 0);
    need(neighbors.length === 1, 'pruning has unique remaining neighbor');
    pruning.push([leaf, neighbors[0]]); alive.delete(leaf);
  }
  const core = sorted([...alive]), outside = vs.filter(a => !alive.has(a));
  return {
    matrix: m, active_vertices: active, inactive_vertices: vs.filter(a => !active.includes(a)),
    pruning, core_vertices: core, core_matrix: restricted(m, core),
    core_degrees: core.map(a => degree(m, a, core)),
    frozen_complement: outside.map(a => [a, state[a + 1]]),
    key: [core, upper(m, core), outside.map(a => state[a + 1])]
  };
}

function describe(matrix, vertices) {
  const branches = vertices.filter(a => degree(matrix, a, vertices) > 2);
  const remaining = matrix.map(row => row.slice()), chains = [];
  for (const start of branches) while (true) {
    let next = vertices.find(b => remaining[start - 1][b - 1] > 0);
    if (next === undefined) break;
    edge(remaining, start, next, -1);
    const chain = [start, next];
    while (!branches.includes(next)) {
      const candidates = vertices.filter(b => remaining[next - 1][b - 1] > 0);
      need(candidates.length === 1, 'core chain has one unused neighbor');
      const following = candidates[0];
      edge(remaining, next, following, -1); chain.push(following); next = following;
    }
    chains.push(sorted([chain, chain.slice().reverse()])[0]);
  }
  need(vertices.every(a => vertices.every(b => remaining[a - 1][b - 1] === 0)),
    'all unlabeled core multiplicities consumed');
  chains.sort(compare);
  let family, row, paths, period, count;
  if (branches.length === 1 && degree(matrix, branches[0], vertices) === 4) {
    need(chains.length === 2 && chains.every(p => p[0] === p[p.length - 1]), 'figure-eight chains');
    family = FAMILIES[0]; paths = chains;
    const [a, b] = paths.map(p => p.length - 1);
    row = a === 1 && b === 1 ? ROWS[0] : Math.max(a, b) <= 2 ? ROWS[1] : ROWS[2];
    period = row === ROWS[0] ? 1 : row === ROWS[1] ? a + b : 2 * (a + b);
    count = Math.min(a, b) >= 3 ? 2 : 1;
  } else {
    need(branches.length === 2 && branches.every(a => degree(matrix, a, vertices) === 3),
      'two degree-three branches');
    const closed = chains.filter(p => p[0] === p[p.length - 1]);
    const open = chains.filter(p => p[0] !== p[p.length - 1]);
    if (closed.length === 2 && open.length === 1) {
      family = FAMILIES[1];
      paths = [closed.find(p => p[0] === branches[0]), closed.find(p => p[0] === branches[1]), open[0]];
      need(paths.every(p => p !== undefined), 'barbell roots both represented');
      const [a, b, c] = paths.map(p => p.length - 1);
      row = Math.max(a, b) <= 2 ? ROWS[3] : ROWS[4];
      period = (a + b + 2 * c) * (row === ROWS[3] ? 1 : 2);
      count = Math.min(a, b) >= 3 ? 2 : 1;
    } else {
      need(closed.length === 0 && open.length === 3, 'theta chains');
      family = FAMILIES[2]; paths = sorted(open);
      const lengths = paths.map(p => p.length - 1), direct = lengths.filter(x => x === 1).length;
      row = direct === 3 ? ROWS[5] : ROWS[6];
      period = direct === 3 ? 2 : 2 * sum(lengths);
      count = direct >= 2 ? 1 : 2;
    }
  }
  return {family, row, branches, paths, lengths: paths.map(p => p.length - 1),
    predicted_period: period, predicted_orbit_count: count};
}
const rotations = triple => sorted(range(0, 3).map(i => triple.slice(i).concat(triple.slice(0, i))))[0];
const cycleClass = (bits, lengths) => sorted([bits,
  bits.map((b, i) => lengths[i] >= 3 ? 1 - b : 0)])[0];
const signatureObject = sig => ({
  kind: sig[0] === 'cycles' ? 'cycle_orientation_class' : 'theta_cyclic_order',
  value: sig[1]
});
function constructAnchors(n, d, frozen) {
  const anchors = new Map(), paths = d.paths;
  const base = () => { const f = Array(n + 1); for (const [a, b] of frozen) f[a] = b; return f; };
  function interior(f, p) {
    for (let i = 1; i < p.length - 1; i += 1) f[p[i]] = p[i + 1];
  }
  function finish(f, u, v, raw, sig) {
    need(range(1, n + 1).every(a => Number.isInteger(f[a]) && f[a] >= 1 && f[a] <= n),
      'every expected anchor pointer independently specified');
    const state = [u, v, ...f.slice(1)], key = canon(state), row = {state, raw, sig};
    if (anchors.has(key)) deep(row, anchors.get(key), 'duplicate direct-token anchor identity');
    anchors.set(key, row);
  }
  if (d.family !== 'theta') {
    const lengths = d.lengths.slice(0, 2);
    for (const b0 of range(0, lengths[0] >= 3 ? 2 : 1))
      for (const b1 of range(0, lengths[1] >= 3 ? 2 : 1)) {
        const bits = [b0, b1], oriented = paths.slice(0, 2).map((p, i) => bits[i] ? p.slice().reverse() : p);
        const f = base(), a = d.branches[0]; for (const p of oriented) interior(f, p);
        let v;
        if (d.family === 'figure_eight') { f[a] = oriented[1][1]; v = oriented[0][1]; }
        else {
          const b = d.branches[1];
          f[a] = oriented[0][1]; f[b] = oriented[1][1]; interior(f, paths[2]); v = paths[2][1];
        }
        finish(f, a, v, bits, ['cycles', cycleClass(bits, lengths)]);
      }
  } else {
    const [a, b] = d.branches, tokens = paths.map(p => p.slice(1, -1));
    const tokenPaths = new Map(paths.map(p => [canon(p.slice(1, -1)), p]));
    for (const roles of unique([...permutations(tokens)])) {
      const [extra, stored, incoming] = roles.map(t => tokenPaths.get(canon(t))), f = base();
      interior(f, extra); interior(f, stored); interior(f, incoming.slice().reverse());
      f[a] = stored[1]; f[b] = incoming[incoming.length - 2];
      finish(f, a, extra[1], roles, ['theta', rotations(roles)]);
    }
  }
  return [...anchors.values()].sort((a, b) => compare(a.state, b.state));
}
function decodeAnchor(state, d) {
  const [u, v] = state, a = d.branches[0], paths = d.paths;
  if (u !== a) return null;
  if (d.family === 'theta') {
    const remaining = paths.map(p => p.slice(1, -1)), roles = [];
    for (const destination of [v, state[a + 1]]) {
      const choices = unique(paths.filter(p => p[1] === destination &&
        remaining.some(t => canon(t) === canon(p.slice(1, -1)))).map(p => p.slice(1, -1)));
      need(choices.length === 1, 'theta role uniquely observable without edge identity');
      const token = choices[0], pos = remaining.findIndex(t => canon(t) === canon(token));
      need(pos >= 0, 'theta token available in multiset'); remaining.splice(pos, 1); roles.push(token);
    }
    need(remaining.length === 1, 'theta incoming token determined');
    roles.push(remaining[0]); return {raw: roles, sig: ['theta', rotations(roles)]};
  }
  let starts;
  if (d.family === 'figure_eight') {
    if (![paths[0][1], paths[0][paths[0].length - 2]].includes(v)) return null;
    starts = [v, state[a + 1]];
  } else {
    if (v !== paths[2][1]) return null;
    starts = d.branches.map(b => state[b + 1]);
  }
  const bits = starts.map((start, i) => {
    const p = paths[i];
    if (start === p[1]) return 0;
    need(p.length - 1 >= 3 && start === p[p.length - 2], 'cycle departure identifies orientation');
    return 1;
  });
  return {raw: bits, sig: ['cycles', cycleClass(bits, d.lengths.slice(0, 2))]};
}
function makeCatalogues() {
  return range(1, 5).map(s => {
    const vs = range(1, s + 1), pairs = vs.flatMap(a => vs.filter(b => b >= a).map(b => [a, b]));
    const entries = [];
    for (const weights of allocations(s + 1, pairs.length)) {
      const m = blank(s);
      pairs.forEach(([a, b], i) => edge(m, a, b, weights[i]));
      if (!vs.every(a => degree(m, a, vs) >= 2) || component(m, 1, vs).length !== s) continue;
      entries.push({catalogue_id: entries.length, s, matrix: m, upper: weights, description: describe(m, vs)});
    }
    return {s, entries};
  });
}
function makeGroups(n, catalogues) {
  const groups = [], labels = range(1, n + 1);
  for (let s = 1; s <= n; s += 1) for (const vertices of subsets(labels, s)) {
    const outside = labels.filter(a => !vertices.includes(a));
    for (const entry of catalogues[s - 1].entries) {
      const original = entry.description;
      const d = {...original, branches: original.branches.map(a => vertices[a - 1]),
        paths: original.paths.map(p => p.map(a => vertices[a - 1]))};
      for (const targets of tuples(labels, n - s)) {
        const frozen = outside.map((a, i) => [a, targets[i]]);
        groups.push({id: groups.length, s, catalogue_id: entry.catalogue_id,
          core_vertices: vertices, core_matrix: entry.matrix, description: d,
          frozen_complement: frozen, key: [vertices, entry.upper, targets],
          anchor_map: constructAnchors(n, d, frozen)});
      }
    }
  }
  return groups;
}
function predicateReceiver(out) {
  need(Array.isArray(out.predicates), 'complete predicate array');
  const counts = new Map(NAMES.map(name => [name, {checks: 0, failures: 0}]));
  let position = 0; const failures = [];
  return {
    check(name, scope, observed, expected) {
      need(counts.has(name), 'declared predicate: ' + name);
      const passed = canon(observed) === canon(expected);
      deep(out.predicates[position], {id: position, name, scope, observed, expected, passed},
        'predicates/' + position);
      const count = counts.get(name); count.checks += 1;
      if (!passed) { count.failures += 1; failures.push(position); }
      position += 1;
    },
    finish() {
      need(position === out.predicates.length, 'no extra, missing or reordered predicates');
      const census = NAMES.map(name => ({name, ...counts.get(name)}));
      deep(out.predicate_census, census, 'predicate_census');
      return {position, failures, census};
    }
  };
}
function periodSet(n) {
  const out = n === 1 ? [1] : range(1, 2 * n + 1);
  if (n > 1) for (let p = 2 * n + 2; p <= 4 * n - 4; p += 2) out.push(p);
  return out;
}
function receiveCarrier(n, saved, catalogues, series, ledger) {
  const scope = 'n=' + n, labels = range(1, n + 1);
  // Lexicographic complete carrier, never taken from saved row IDs.
  const states = [...tuples(labels, n + 2)], count = states.length;
  const next = states.map(s => stateId(forward(s), n)), previous = states.map(s => stateId(inverse(s), n));
  const structures = states.map(structural), groups = makeGroups(n, catalogues);
  const byKey = new Map(groups.map(g => [canon(g.key), g]));
  need(byKey.size === groups.length, scope + ': unique expected group keys');
  ledger.check('carrier_size', scope, count, n ** (n + 2));
  ledger.check('group_catalogue_complete', scope, unique(structures.map(s => s.key)),
    unique(groups.map(g => g.key)));
  need(structures.every(s => byKey.has(canon(s.key))), scope + ': all actual groups identified');
  const fibres = states.map(() => []); next.forEach((target, source) => fibres[target].push(source));
  const orbitFor = Array(count).fill(-1), orbits = [];
  for (let seed = 0; seed < count; seed += 1) {
    if (orbitFor[seed] !== -1) continue;
    const local = new Map(), cycle = []; let current = seed;
    while (!local.has(current) && orbitFor[current] === -1) {
      local.set(current, cycle.length); cycle.push(current); current = next[current];
    }
    need(local.has(current), scope + ': traversal closes locally');
    const id = orbits.length, oscope = scope + '/orbit=' + id;
    ledger.check('orbit_closure', oscope, current, seed);
    ledger.check('orbit_no_preperiod', oscope, local.get(current), 0);
    need(current === seed, scope + ': no preperiod or previously seen orbit');
    for (const sid of cycle) orbitFor[sid] = id;
    const group = byKey.get(canon(structures[seed].key)), d = group.description;
    ledger.check('orbit_exact_period', oscope, cycle.length, d.predicted_period);
    ledger.check('orbit_group_constant', oscope, unique(cycle.map(i => structures[i].key)), [group.key]);
    const anchors = [];
    cycle.forEach((sid, phase) => {
      const a = decodeAnchor(states[sid], d);
      if (a !== null) anchors.push({phase, state_id: sid, raw_decoration: a.raw, class: signatureObject(a.sig)});
    });
    ledger.check('orbit_anchor_nonempty', oscope, anchors.length > 0, true);
    orbits.push({id, representative_state_id: seed, state_ids_in_time_order: cycle,
      preperiod: 0, period: cycle.length, group_id: group.id, anchors});
  }
  ledger.check('orbit_partition', scope, sorted(orbits.flatMap(o => o.state_ids_in_time_order)), range(0, count));
  const grouped = groups.map(() => []), stateRows = [];
  states.forEach((state, id) => {
    const sscope = scope + '/state=' + id, a = structures[id], b = structures[next[id]];
    const groupId = byKey.get(canon(a.key)).id; grouped[groupId].push(id);
    ledger.check('successor_in_carrier', sscope, next[id] >= 0 && next[id] < count, true);
    ledger.check('inverse_in_carrier', sscope, previous[id] >= 0 && previous[id] < count, true);
    ledger.check('inverse_after_forward', sscope, inverse(forward(state)), state);
    ledger.check('forward_after_inverse', sscope, forward(inverse(state)), state);
    ledger.check('unit_fibre', sscope, fibres[id], [previous[id]]);
    ledger.check('invariant_matrix', sscope, b.matrix, a.matrix);
    ledger.check('active_component_bicyclic', sscope, sum(upper(a.matrix, a.active_vertices)), a.active_vertices.length + 1);
    ledger.check('registers_in_core', sscope, state.slice(0, 2).map(v => a.core_vertices.includes(v)), [true, true]);
    ledger.check('core_bicyclic', sscope, sum(upper(a.matrix, a.core_vertices)), a.core_vertices.length + 1);
    ledger.check('core_minimum_degree', sscope, Math.min(...a.core_degrees) >= 2, true);
    ledger.check('core_stored_arrows_internal', sscope,
      a.core_vertices.map(v => a.core_vertices.includes(state[v + 1])), a.core_vertices.map(() => true));
    ledger.check('frozen_complement', sscope, b.frozen_complement, a.frozen_complement);
    ledger.check('core_key_invariant', sscope, b.key, a.key);
    ledger.check('pruned_arrows_toward_core', sscope, a.pruning.map(([v]) => [v, state[v + 1]]), a.pruning);
    const {key, ...invariant} = a;
    stateRows.push({id, state: stateObject(state), successor_id: next[id], inverse_id: previous[id],
      inverse_state: stateObject(inverse(state)), preimage_ids: fibres[id],
      orbit_id: orbitFor[id], group_id: groupId, invariant});
  });
  const groupRows = groups.map(g => {
    const gscope = scope + '/group=' + g.id, stateIds = grouped[g.id], orbitIds = unique(stateIds.map(i => orbitFor[i]));
    const actualAnchors = [], classOrbits = new Map();
    for (const sid of stateIds) {
      const decoded = decodeAnchor(states[sid], g.description);
      if (decoded === null) continue;
      actualAnchors.push({state: states[sid], ...decoded});
      const key = canon(decoded.sig);
      if (!classOrbits.has(key)) classOrbits.set(key, {sig: decoded.sig, ids: new Set()});
      classOrbits.get(key).ids.add(orbitFor[sid]);
    }
    actualAnchors.sort((a, b) => compare(a.state, b.state));
    const expected = g.anchor_map, actualClasses = [...classOrbits.values()].sort((a, b) => compare(a.sig, b.sig));
    const expectedClasses = unique(expected.map(a => a.sig));
    const anchorTriple = a => [a.state, a.raw, signatureObject(a.sig)];
    ledger.check('group_anchor_states', gscope, actualAnchors.map(anchorTriple), expected.map(anchorTriple));
    ledger.check('group_decoration_classes', gscope,
      actualClasses.map(a => signatureObject(a.sig)), expectedClasses.map(signatureObject));
    ledger.check('group_orbit_decoration_bijection', gscope,
      sorted(actualClasses.map(a => sorted([...a.ids]))), orbitIds.map(i => [i]));
    ledger.check('group_orbit_count', gscope, orbitIds.length, g.description.predicted_orbit_count);
    ledger.check('group_periods', gscope, orbitIds.map(i => orbits[i].period),
      orbitIds.map(() => g.description.predicted_period));
    return {id: g.id, s: g.s, catalogue_id: g.catalogue_id, core_vertices: g.core_vertices,
      core_matrix: g.core_matrix, description: g.description, frozen_complement: g.frozen_complement,
      state_ids: stateIds, orbit_ids: orbitIds,
      expected_anchors: expected.map(a => ({state: stateObject(a.state), state_id: stateId(a.state, n),
        raw_decoration: a.raw, class: signatureObject(a.sig)})),
      observed_anchor_state_ids: actualAnchors.map(a => stateId(a.state, n)),
      expected_classes: expectedClasses.map(signatureObject),
      observed_classes: actualClasses.map(a => ({class: signatureObject(a.sig), orbit_ids: sorted([...a.ids])}))};
  });
  const observed = periodCounts(orbits.map(o => o.period)), expected = new Map(), contributions = [];
  for (let s = 1; s <= n; s += 1) {
    const falling = factorial(n) / factorial(n - s), complement = n ** (n - s), multiplier = falling * complement;
    need(Number.isSafeInteger(falling), 'integral falling factorial');
    const core = bySize(series, s), contribution = polyScale(core, multiplier);
    for (const [p, v] of contribution) put(expected, p, v);
    contributions.push({s, falling_factorial: falling, complement_map_count: complement, multiplier,
      core_coefficients: polyWire(core), contribution: polyWire(contribution)});
  }
  const hand = fromPolyRows(CARRIER_CONTROL_ROWS[n - 1]);
  ledger.check('carrier_period_polynomial', scope, polyWire(observed), polyWire(expected));
  ledger.check('carrier_hand_control', scope, polyWire(observed), polyWire(hand));
  ledger.check('carrier_orbit_total', scope, orbits.length, integer(rsum([...hand.values()])));
  ledger.check('carrier_weighted_total', scope, integer(rsum([...observed].map(([p, v]) => rmul(rat(p), v)))), count);
  ledger.check('carrier_period_set', scope, sorted([...observed.keys()]), periodSet(n));
  ledger.check('carrier_maximum_period', scope, Math.max(...observed.keys()), n === 1 ? 1 : 4 * n - 4);
  const fixed = range(0, count).filter(i => next[i] === i);
  ledger.check('carrier_fixed_states', scope, fixed.length, n ** n);
  const fixedIterates = []; let targets = range(0, count);
  for (let k = 1; k <= Math.max(...periodSet(n)); k += 1) {
    targets = targets.map(i => next[i]);
    const ids = range(0, count).filter(i => targets[i] === i);
    const wanted = rsum([...expected].filter(([p]) => k % p === 0).map(([p, v]) => rmul(rat(p), v)));
    ledger.check('fixed_iterate_count', scope + '/k=' + k, rwire(rat(ids.length)), rwire(wanted));
    fixedIterates.push({k, fixed_state_ids: ids, observed_count: ids.length, expected_count: rwire(wanted)});
  }
  const coverage = ROWS.map((row, i) => {
    const matching = groupRows.filter(g => g.description.row === row), present = matching.length > 0;
    ledger.check('seven_row_coverage', scope + '/row=' + row, present, n >= ROW_FIRST[i]);
    return {row, group_ids: matching.map(g => g.id), first_core_size: ROW_FIRST[i],
      observed_present: present, expected_present: n >= ROW_FIRST[i], group_count: matching.length,
      orbit_count: sum(matching.map(g => g.orbit_ids.length)), state_count: sum(matching.map(g => g.state_ids.length))};
  });
  ledger.check('seven_row_coverage', scope, sum(coverage.map(r => r.state_count)), count);
  const reconstructed = {n, state_count: count, states: stateRows, orbits, groups: groupRows,
    row_coverage: coverage, period_polynomial_observed: polyWire(observed),
    period_polynomial_expected: polyWire(expected), extension_contributions: contributions,
    orbit_count: orbits.length, period_set: sorted([...observed.keys()]),
    maximum_period: Math.max(...observed.keys()), fixed_state_ids: fixed, fixed_iterates: fixedIterates};
  deep(saved, reconstructed, 'carriers/' + (n - 1));
  return reconstructed;
}

function receiveSeries(saved, catalogues, carriers, formula, ledger) {
  // Degree-five numerator term is discarded only by the specified degree-four
  // series truncation; no state/core cutoff five is enumerated.
  const numerator = seriesAdd(monomial(1, 0), monomial(2, 0, -1),
    monomial(4, 0, 1, 2), monomial(5, 0, -1, 12));
  const univariate = seriesMultiply(numerator, seriesPower(geometric(0), 3)), records = [];
  for (let s = 1; s <= 4; s += 1) {
    const scope = 'core_size=' + s, carrier = carriers[s - 1];
    const pure = carrier.groups.filter(g => g.s === s), entries = catalogues[s - 1].entries;
    ledger.check('core_catalogue_graph_count', scope, pure.length, entries.length);
    const familyRecords = [], totalObserved = new Map();
    FAMILIES.forEach((family, fi) => {
      const observed = new Map();
      for (const group of pure.filter(g => g.description.family === family))
        for (const id of group.orbit_ids) put(observed, carrier.orbits[id].period, rat(1, factorial(s)));
      const expected = bySize(formula.pieces[fi], s);
      ledger.check('core_series_family', scope + '/' + family, polyWire(observed), polyWire(expected));
      for (const [p, v] of observed) put(totalObserved, p, v);
      familyRecords.push({family, observed_coefficients: polyWire(observed), expected_coefficients: polyWire(expected)});
    });
    need(pure.length === entries.length, scope + ': full canonical pure-group correspondence');
    entries.forEach((entry, i) => {
      deep([pure[i].catalogue_id, pure[i].core_vertices, pure[i].core_matrix],
        [entry.catalogue_id, range(1, s + 1), entry.matrix], scope + '/pure_group=' + i);
      ledger.check('core_catalogue_orbit_census', scope + '/catalogue=' + entry.catalogue_id,
        pure[i].orbit_ids.length, entry.description.predicted_orbit_count);
    });
    const expected = bySize(formula.total, s), hand = fromPolyRows(CORE_CONTROL_ROWS[s - 1]);
    ledger.check('core_series_total', scope, polyWire(totalObserved), polyWire(expected));
    ledger.check('core_series_hand_control', scope, polyWire(expected), polyWire(hand));
    const coefficient = rsum([...expected.values()]);
    const closed = s === 1 ? rat(1) : s === 2 ? rat(2) : rat(5 * s * s + s + 24, 24);
    const weighted = rsum([...expected].map(([p, v]) => rmul(rat(p), v)));
    ledger.check('univariate_rational_identity', scope, rwire(coefficient), rwire(univariate.get(s + ',0') || rat(0)));
    ledger.check('univariate_closed_coefficient', scope, rwire(coefficient), rwire(closed));
    ledger.check('period_weighted_core_identity', scope, rwire(weighted), rwire(rat(s * s * (s + 1), 2)));
    records.push({s, families: familyRecords, observed_coefficients: polyWire(totalObserved),
      expected_coefficients: polyWire(expected), hand_control: polyWire(hand),
      univariate_coefficient: rwire(coefficient), closed_coefficient: rwire(closed),
      period_weighted_coefficient: rwire(weighted),
      labelled_orbit_counts: polyWire(polyScale(totalObserved, factorial(s)))});
  }
  const reconstructed = {max_core_size: 4,
    pieces: FAMILIES.map((family, i) => ({family, terms: seriesWire(formula.pieces[i])})),
    total_terms: seriesWire(formula.total), coefficient_checks: records,
    control_provenance: 'Deductive rational expansions in the admitted MATHEMATICAL_AUDIT.md; not prior executed results.'};
  deep(saved, reconstructed, 'series');
  return reconstructed;
}
function receiveLimits(saved, carriers, ledger) {
  const rows = LIMITS.map(([family, first_core_size], i) => {
    const witnesses = [];
    for (const c of carriers) for (const g of c.groups) {
      const d = g.description;
      const match = (i === 0 && d.family === 'figure_eight' && Math.min(...d.lengths) >= 3) ||
        (i === 1 && d.family === 'barbell' && Math.min(...d.lengths.slice(0, 2)) >= 3) ||
        (i === 2 && d.family === 'theta' && Math.min(...d.lengths) >= 2);
      if (match) witnesses.push([c.n, g.id]);
    }
    ledger.check('finite_coverage_limits', family, witnesses, []);
    return {family, first_core_size, observed_group_references: witnesses,
      finite_status: 'not_exercised_in_n_1_2_3_4',
      theorem_status: 'deductively_covered_by_all_parameter_anchor_argument'};
  });
  deep(saved, rows, 'coverage_limits');
}
function receiveSemantics(out) {
  shape(out, ['schema', 'parameters', 'role', 'method', 'excluded_claims',
    'core_catalogues', 'carriers', 'series', 'coverage_limits', 'predicates',
    'predicate_census', 'summary'], 'top-level twelve keys');
  deep(out.schema, 'p212-full-output-v1', 'schema');
  deep(out.parameters, PARAMETERS, 'parameters');
  deep(out.role, 'author_verifier_not_independent_review', 'role');
  deep(out.method, 'literal_state_graph_vs_multiplicity_catalogue_observable_anchors_and_Fraction_series', 'method');
  deep(out.excluded_claims, EXCLUDED, 'excluded_claims');
  need(NAMES.length === 46 && new Set(NAMES).size === 46, 'exact distinct 46 declared predicate names');
  need(Array.isArray(out.carriers) && out.carriers.length === 4, 'four complete carriers');
  const catalogues = makeCatalogues();
  deep(out.core_catalogues, catalogues, 'core_catalogues');
  const formula = formulaSeries(), ledger = predicateReceiver(out), carriers = [];
  for (let n = 1; n <= 4; n += 1)
    carriers.push(receiveCarrier(n, out.carriers[n - 1], catalogues, formula.total, ledger));
  receiveSeries(out.series, catalogues, carriers, formula, ledger);
  receiveLimits(out.coverage_limits, carriers, ledger);
  const total = sum(carriers.map(c => c.state_count));
  ledger.check('total_carrier_states', 'all_carriers', total, 4356);
  const received = ledger.finish();
  deep(out.summary, {carrier_sizes: [1, 2, 3, 4], state_count: total,
    orbit_counts: carriers.map(c => c.orbit_count), predicate_count: received.position,
    failure_ids: received.failures, passed: received.failures.length === 0}, 'summary');
  need(received.failures.length === 0, 'all reconstructed finite author predicates must hold for adoption');
  return {carriers: carriers.map(c => ({n: c.n, states: c.state_count, groups: c.groups.length,
    orbits: c.orbit_count, periods: c.period_set})), predicate_count: received.position,
    predicate_census: received.census, total_states: total};
}

function statKey(s) {
  need(typeof s.mtimeNs === 'bigint' && typeof s.ctimeNs === 'bigint',
    'runtime supplies exact nanosecond BigInt file timestamps');
  return {device: String(s.dev), inode: String(s.ino), mode: String(s.mode),
    size_bytes: String(s.size), link_count: String(s.nlink),
    mtime_ns: String(s.mtimeNs), ctime_ns: String(s.ctimeNs)};
}
const digest = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
function readStable(name, label) {
  need(typeof name === 'string' && path.isAbsolute(name) && path.resolve(name) === name,
    label + ': explicit normalized absolute path');
  const initial = fs.lstatSync(name, {bigint: true});
  need(initial.isFile() && !initial.isSymbolicLink(), label + ': regular nonsymlink file');
  const fd = fs.openSync(name, fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW);
  let raw, before;
  try {
    const opened = fs.fstatSync(fd, {bigint: true});
    need(opened.isFile(), label + ': opened regular file');
    before = statKey(opened); deep(statKey(initial), before, label + ': lstat/fstat identity');
    raw = fs.readFileSync(fd);
    deep(statKey(fs.fstatSync(fd, {bigint: true})), before, label + ': unchanged opened file');
  } finally { fs.closeSync(fd); }
  const after = fs.lstatSync(name, {bigint: true});
  need(after.isFile() && !after.isSymbolicLink(), label + ': path remains regular');
  deep(statKey(after), before, label + ': path remains same file');
  need(String(raw.length) === before.size_bytes, label + ': complete file length');
  return {raw, key: {path: name, bytes: raw.length, sha256: digest(raw), ...before}};
}
function pinned(spec, label) {
  shape(spec, ['path', 'bytes', 'sha256'], label + ': pin');
  need(Number.isSafeInteger(spec.bytes) && spec.bytes > 0, label + ': positive integer bytes');
  need(typeof spec.sha256 === 'string' && /^[0-9a-f]{64}$/.test(spec.sha256), label + ': lowercase SHA-256');
  const read = readStable(spec.path, label);
  need(read.raw.length === spec.bytes && read.key.sha256 === spec.sha256, label + ': exact pinned raw bytes');
  return read;
}
function main() {
  need(process.argv.length === 4 && process.argv[2] === '--binding',
    'exact interface: node receive_saved_output.js --binding ABSOLUTE_BINDING_JSON');
  const bindingRead = readStable(process.argv[3], 'binding');
  const binding = parseStrict(bindingRead.raw, 'binding');
  shape(binding, ['schema', 'approved', 'role', 'saved_stdout', 'parameters', 'receiver'], 'binding');
  deep(binding.schema, 'p212-saved-output-semantic-binding-v1', 'binding/schema');
  deep(binding.approved, true, 'binding/approved');
  deep(binding.role, 'author', 'binding/role');
  shape(binding.receiver, ['path', 'bytes', 'sha256'], 'binding/receiver');
  need(binding.receiver.path === path.resolve(__filename), 'binding pins this exact receiver path');
  const receiverRead = pinned(binding.receiver, 'receiver');
  const parameterRead = pinned(binding.parameters, 'parameters');
  need(parameterRead.key.sha256 === PARAMETER_SHA256 && parameterRead.raw.length === 609,
    'unchanged exact source-accepted parameter bytes');
  deep(parseStrict(parameterRead.raw, 'parameters'), PARAMETERS, 'fixed parameter contract');
  const outputRead = pinned(binding.saved_stdout, 'saved_stdout');
  need(new Set([bindingRead.key.path, receiverRead.key.path, parameterRead.key.path, outputRead.key.path]).size === 4,
    'four distinct explicit input paths');
  const out = parseStrict(outputRead.raw, 'saved_stdout', true);
  const semantics = receiveSemantics(out);
  const before = [bindingRead, receiverRead, parameterRead, outputRead];
  const after = before.map((old, i) => {
    const current = readStable(old.key.path, 'post_input_' + i);
    need(old.raw.equals(current.raw), 'full before/after raw equality for input ' + i);
    deep(current.key, old.key, 'full before/after rich key for input ' + i);
    return current.key;
  });
  // A receipt is emitted only after all fields, all comparisons, all pins,
  // and both complete raw input reads have actually succeeded.
  const receipt = {
    schema: 'p212-saved-output-semantic-receipt-v1',
    status: 'COMPLETE_SAVED_OUTPUT_SEMANTICS_CHECKED',
    role: 'author_side_receiver_not_independent_review',
    binding_sha256: bindingRead.key.sha256,
    source_parameter_sha256: PARAMETER_SHA256,
    saved_stdout_sha256: outputRead.key.sha256, saved_stdout_bytes: outputRead.raw.length,
    receiver_sha256: receiverRead.key.sha256,
    semantic_checks: checks, semantics,
    inputs_before: before.map(r => r.key), inputs_after: after,
    scientific_producer_invocations: 0, submitted_code_imports: 0,
    canonical_accesses: 0, filesystem_writes: 0,
    scope: 'All twelve output fields, complete labelled catalogues/states/arrows/matrices/orbits/anchors/classes/groups, exact BigInt rational series, all 46 named predicate values and evaluation order, census and coverage; finite saved-output reception only.'
  };
  process.stdout.write(canon(receipt) + '\n');
}
try { main(); }
catch (error) {
  process.stderr.write('P212 saved-output semantic receiver failure: ' + error.name + ': ' + error.message + '\n');
  process.exitCode = 1;
}
