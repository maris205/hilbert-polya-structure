'use strict';
// SOURCE PREPARATION ONLY. Execute only after root full-source reception and DATA grant.
// Archived DATA receiver: no Python, producer import, subprocess, network or file writes.
const fs = require('node:fs');
const crypto = require('node:crypto');
const W = '/root/autodl-tmp/symbolic_dynamics';
const Q = 'docs/papers211_215_sequence/qa';
const OWN = Q + '/p214_author_data_audit01';
const P = 'papers/214-nilpotent-bilinear-clock';
const RUN = Q + '/p214_author_runs/initial01';
const ROOT = Q + '/p214_runtime_root01';
const PREP = Q + '/p214_runtime_preparation01';
const SR = Q + '/p214_source_root01';
const VERSION = 'p214-author-jsonl-v1';
const BOX = [2, 3, 4].flatMap(q => [2, 3, 4].map(m => [q, m]));
const META = ['dev', 'ino', 'mode', 'size', 'mtimeNs', 'ctimeNs'];
const inputs = new Map(), assertionCounts = {}, recordCounts = {}, checkCounts = {};
const ledger = [], carriers = [];
let assertions = 0, sourceComparisons = 0, cursor = 0, lines, schema;
function wire(v) {
  if (v === null || typeof v === 'boolean' || typeof v === 'string') return JSON.stringify(v);
  if (typeof v === 'number' && Number.isSafeInteger(v)) return String(v);
  if (Array.isArray(v)) return '[' + v.map(wire).join(',') + ']';
  if (v && Object.getPrototypeOf(v) === Object.prototype)
    return '{' + Object.keys(v).sort().map(k => JSON.stringify(k) + ':' + wire(v[k])).join(',') + '}';
  throw new Error('unsupported exact data value');
}
function equal(a, b) { return wire(a) === wire(b); }
function need(ok, name) {
  assertions++;
  assertionCounts[name] = (assertionCounts[name] || 0) + 1;
  if (!ok) throw new Error(name + ' at next record ' + (cursor + 1));
}
function eq(a, b, name) { need(equal(a, b), name); }
function sha(b) { return crypto.createHash('sha256').update(b).digest('hex'); }
function pathOf(p) {
  need(typeof p === 'string' && /^[A-Za-z0-9_./-]+$/.test(p) &&
       !p.startsWith('/') && !p.split('/').some(x => x === '..' || x === '.' || !x), 'safe_workspace_path');
  return W + '/' + p;
}
function file(p) {
  const full = pathOf(p), fd = fs.openSync(full, 'r');
  try {
    const before = fs.fstatSync(fd, {bigint: true});
    need(before.isFile(), 'regular_workspace_input');
    const raw = fs.readFileSync(fd), after = fs.fstatSync(fd, {bigint: true});
    const meta = s => Object.fromEntries(META.map(k => [k, String(s[k])]));
    eq(meta(before), meta(after), 'read_metadata_stable');
    eq(meta(after), meta(fs.statSync(full, {bigint: true})), 'read_path_stable');
    need(BigInt(raw.length) === after.size, 'complete_input_bytes');
    return {raw, key: {path: p, kind: 'regular-file', bytes: raw.length,
                      sha256: sha(raw), metadata: meta(after)}};
  } finally { fs.closeSync(fd); }
}
function read(p) {
  if (!inputs.has(p)) inputs.set(p, file(p));
  return inputs.get(p).raw;
}
function json(p) { return JSON.parse(read(p).toString('utf8')); }
function pins(p, count = null) {
  const txt = read(p).toString('utf8');
  need(txt.endsWith('\n'), 'pin_newline');
  const rows = txt.slice(0, -1).split('\n').map(s => {
    need(/^[a-f0-9]{64}  [A-Za-z0-9_./-]+$/.test(s), 'pin_syntax');
    pathOf(s.slice(66));
    return [s.slice(66), s.slice(0, 64)];
  });
  need(new Set(rows.map(r => r[0])).size === rows.length, 'unique_pin_paths');
  if (count !== null) eq(rows.length, count, 'pin_cardinality');
  for (const [path, hash] of rows) eq(sha(read(path)), hash, 'complete_pinned_input');
  return rows;
}
function check(name, actual, expected, bag) {
  eq(actual, expected, 'independent_' + name);
  sourceComparisons++;
  checkCounts[name] = (checkCounts[name] || 0) + 1;
  bag[name] = true;
}
// Exact evaluator of all assertion keywords used by the pinned line schema.
// It does not fetch $schema, compile external schemas, or accept unknown keywords.
const KEYWORDS = new Set(['$schema', 'title', 'description', '$defs', '$ref', 'oneOf', 'anyOf',
  'allOf', 'type', 'minimum', 'minItems', 'minProperties', 'required', 'properties',
  'additionalProperties', 'unevaluatedProperties', 'items', 'const', 'enum']);
function grammar(v, s) {
  if (typeof s === 'boolean') return {ok: s, keys: new Set()};
  for (const k of Object.keys(s)) if (!KEYWORDS.has(k)) throw new Error('unhandled schema keyword ' + k);
  const evaluated = new Set();
  const merge = r => { for (const k of r.keys) evaluated.add(k); return r.ok; };
  if (s.$ref) {
    if (!/^#\/\$defs\/[a-z_]+$/.test(s.$ref)) throw new Error('nonlocal schema reference');
    const target = schema.$defs[s.$ref.slice(8)];
    if (!target || !merge(grammar(v, target))) return {ok: false, keys: evaluated};
  }
  if (s.allOf && !s.allOf.every(t => merge(grammar(v, t)))) return {ok: false, keys: evaluated};
  for (const k of ['anyOf', 'oneOf']) if (s[k]) {
    const valid = s[k].map(t => grammar(v, t)).filter(r => r.ok);
    if (!(k === 'oneOf' ? valid.length === 1 : valid.length > 0)) return {ok: false, keys: evaluated};
    valid.forEach(merge);
  }
  const object = v !== null && typeof v === 'object' && !Array.isArray(v);
  const types = {null: v === null, integer: Number.isSafeInteger(v), array: Array.isArray(v),
                 object, string: typeof v === 'string', boolean: typeof v === 'boolean'};
  if (s.type && !types[s.type]) return {ok: false, keys: evaluated};
  if (Object.hasOwn(s, 'const') && !equal(v, s.const)) return {ok: false, keys: evaluated};
  if (s.enum && !s.enum.some(x => equal(x, v))) return {ok: false, keys: evaluated};
  if (Object.hasOwn(s, 'minimum') && typeof v === 'number' && v < s.minimum) return {ok: false, keys: evaluated};
  if (Array.isArray(v)) {
    if (s.minItems !== undefined && v.length < s.minItems) return {ok: false, keys: evaluated};
    if (s.items && !v.every(x => grammar(x, s.items).ok)) return {ok: false, keys: evaluated};
  }
  if (object) {
    if (s.minProperties !== undefined && Object.keys(v).length < s.minProperties) return {ok: false, keys: evaluated};
    if (s.required && !s.required.every(k => Object.hasOwn(v, k))) return {ok: false, keys: evaluated};
    for (const [k, t] of Object.entries(s.properties || {})) if (Object.hasOwn(v, k)) {
      evaluated.add(k);
      if (!grammar(v[k], t).ok) return {ok: false, keys: evaluated};
    }
    if (Object.hasOwn(s, 'additionalProperties')) for (const k of Object.keys(v))
      if (!Object.hasOwn(s.properties || {}, k)) {
        if (!grammar(v[k], s.additionalProperties).ok) return {ok: false, keys: evaluated};
        evaluated.add(k);
      }
    if (s.unevaluatedProperties === false && Object.keys(v).some(k => !evaluated.has(k)))
      return {ok: false, keys: evaluated};
  }
  return {ok: true, keys: evaluated};
}
function take(kind, payload) {
  need(cursor < lines.length, 'record_available');
  const row = JSON.parse(lines[cursor]);
  const expected = {schema_version: VERSION, kind, ...payload};
  eq(lines[cursor], wire(row), 'exact_sorted_ascii_wire_no_duplicate_keys');
  need(grammar(row, schema).ok, 'full_nested_line_schema');
  eq(row, expected, 'entire_record_exact_fields_and_semantics');
  ledger.push({line: cursor + 1, kind,
    ...(payload.q === undefined ? {} : {q: payload.q}), ...(payload.m === undefined ? {} : {m: payload.m}),
    ...(payload.state_id === undefined ? {} : {state_id: payload.state_id}),
    ...(payload.target_state_id === undefined ? {} : {target_state_id: payload.target_state_id}),
    ...(payload.h === undefined ? {} : {h: payload.h}),
    ...(payload.d === undefined ? {} : {d: payload.d}),
    bytes: Buffer.byteLength(lines[cursor]) + 1, sha256: sha(Buffer.from(lines[cursor] + '\n')),
    exact_payload_schema_and_wire: true, named_checks: Object.keys(payload.checks || {}).sort()});
  cursor++;
  recordCounts[kind] = (recordCounts[kind] || 0) + 1;
}
function field(q) {
  // For GF4, write a=a0+a1*alpha and use alpha^2=alpha+1 directly.
  // This is not the producer's bit-shift reduction loop or arithmetic mod 4.
  const add = (a, b) => q === 4 ? ((a % 2 + b % 2) % 2) + 2 * ((Math.floor(a / 2) + Math.floor(b / 2)) % 2) : (a + b) % q;
  const mul = (a, b) => {
    if (q !== 4) return a * b % q;
    const [a0, a1, b0, b1] = [a % 2, Math.floor(a / 2), b % 2, Math.floor(b / 2)];
    return (a0 * b0 + a1 * b1) % 2 + 2 * ((a0 * b1 + a1 * b0 + a1 * b1) % 2);
  };
  const neg = a => q === 4 ? a : (q - a) % q;
  const inv = a => { for (let b = 1; b < q; b++) if (mul(a, b) === 1) return b; throw new Error('no inverse'); };
  return {q, add, mul, neg, inv};
}
const range = n => Array.from({length: n}, (_, i) => i);
const ascending = a => [...a].sort((x, y) => x - y);
function ring(f, m) {
  const q = f.q, size = q ** m, idealSize = q ** (m - 1), n = idealSize ** 2;
  const codes = range(size), coefficients = codes.map(c => range(m).map(i => Math.floor(c / q ** i) % q));
  const encode = a => a.reduce((v, c, i) => v + c * q ** i, 0);
  const add = (a, b) => encode(coefficients[a].map((v, i) => f.add(v, coefficients[b][i])));
  const neg = a => encode(coefficients[a].map(f.neg));
  const mul = (a, b) => encode(range(m).map(k => range(k + 1).reduce((v, i) => f.add(v, f.mul(coefficients[a][i], coefficients[b][k - i])), 0)));
  const valuation = a => { const i = coefficients[a].findIndex(c => c !== 0); return i < 0 ? m : i; };
  const ideal = codes.filter(a => a % q === 0), idealPower = r => codes.filter(a => valuation(a) >= r);
  const sid = (x, y) => { need(ideal.includes(x) && ideal.includes(y), 'independent_state_coordinate_bounds'); return (x / q) * idealSize + y / q; };
  const state = id => [q * Math.floor(id / idealSize), q * (id % idealSize)];
  const unitCache = new Map();
  const unitInverse = a => {
    if (!unitCache.has(a)) {
      // Independent exhaustive unit equation, not producer coefficient recursion.
      const candidates = codes.filter(b => mul(a, b) === 1);
      eq(candidates.length, 1, 'unique_exhaustive_unit_inverse');
      unitCache.set(a, candidates[0]);
    }
    return unitCache.get(a);
  };
  return {q, m, size, idealSize, n, codes, coefficients, encode, add, neg, mul, valuation,
          ideal, idealPower, sid, state, unitInverse, shift: (a, d) => Math.floor(a / q ** d), t: q};
}
function walk(transitions, start) {
  const seen = new Map(), visited = []; let v = start;
  while (!seen.has(v)) {
    need(Number.isInteger(v) && v >= 0 && v < transitions.length, 'literal_orbit_id_bounds');
    seen.set(v, visited.length); visited.push(v); v = transitions[v];
  }
  const k = seen.get(v);
  return {state_ids: [...visited, v], cycle_start_index: k, cycle_state_ids: visited.slice(k),
          period: visited.length - k, first_zero_index: seen.has(0) ? seen.get(0) : null};
}
function backwards(mapping) {
  const buckets = mapping.map(() => []);
  mapping.forEach((target, source) => { need(Number.isInteger(target) && target >= 0 && target < mapping.length, 'literal_transition_id_bounds'); buckets[target].push(source); });
  return buckets;
}
function receiveField(f) {
  const {q, add, mul, neg, inv} = f, elements = range(q), c = {};
  for (const a of elements) {
    check('field_additive_identity', add(a, 0), a, c);
    check('field_multiplicative_identity', mul(a, 1), a, c);
    check('field_additive_inverse', add(a, neg(a)), 0, c);
    if (a) check('field_multiplicative_inverse', mul(a, inv(a)), 1, c);
    for (const b of elements) {
      check('field_addition_closure', elements.includes(add(a, b)), true, c);
      check('field_multiplication_closure', elements.includes(mul(a, b)), true, c);
      check('field_addition_commutative', add(a, b), add(b, a), c);
      check('field_multiplication_commutative', mul(a, b), mul(b, a), c);
      for (const z of elements) {
        check('field_addition_associative', add(add(a, b), z), add(a, add(b, z)), c);
        check('field_multiplication_associative', mul(mul(a, b), z), mul(a, mul(b, z)), c);
        check('field_distributive', mul(a, add(b, z)), add(mul(a, b), mul(a, z)), c);
      }
    }
  }
  if (q === 4) { check('gf4_alpha_square', mul(2, 2), 3, c); check('gf4_characteristic_two', add(1, 1), 0, c); }
  take('field', {q, characteristic: q === 4 ? 2 : q,
    element_labels: q === 4 ? ['0', '1', 'alpha', '1+alpha'] : elements.map(String),
    modulus_binary: q === 4 ? 7 : null, addition_table: elements.map(a => elements.map(b => add(a, b))),
    multiplication_table: elements.map(a => elements.map(b => mul(a, b))),
    additive_inverses: elements.map(neg), multiplicative_inverses: [null, ...elements.slice(1).map(inv)], checks: c});
}
function receiveCarrier(f, m) {
  const r = ring(f, m), {q, n, t, add, neg, mul, valuation: val, sid, state} = r;
  const ids = range(n), nt = neg(t); let c = {};
  check('carrier_ideal_size', r.ideal.length, q ** (m - 1), c);
  check('carrier_state_count', n, q ** (2 * (m - 1)), c);
  for (const z of r.codes) check('ring_encoding_round_trip', r.encode(r.coefficients[z]), z, c);
  for (let d = 0; d <= m; d++) check('ideal_power_cardinality', r.idealPower(d).length, q ** (m - d), c);
  take('carrier', {q, m, ring_size: r.size, ideal_size: r.idealSize, state_count: n, t_code: t,
    negative_t_code: nt, ideal_codes: r.ideal,
    ring_elements: r.codes.map(code => ({code, coefficients: r.coefficients[code], valuation: val(code)})), checks: c});
  const F = [], L = [], M = [], A = [], AI = [], B = [], BI = [];
  for (const s of ids) {
    const [x, y] = state(s);
    F.push(sid(y, mul(x, add(t, y)))); L.push(sid(y, mul(t, x))); M.push(sid(y, mul(x, y)));
    A.push(sid(x, add(y, t))); AI.push(sid(x, add(y, nt)));
    B.push(sid(add(x, nt), y)); BI.push(sid(add(x, t), y));
  }
  const pre = backwards(F), mpre = backwards(M); c = {};
  for (const [name, a] of [['P', A], ['P_inverse', AI], ['Q', B], ['Q_inverse', BI]]) check('adapter_' + name + '_permutation', ascending(a), ids, c);
  check('adapter_P_inverse', ids.map(s => AI[A[s]]), ids, c);
  check('adapter_Q_inverse', ids.map(s => BI[B[s]]), ids, c);
  check('adapter_Q_is_not_P_inverse_at_zero', B[0] !== AI[0], true, c);
  take('adapter', {q, m, P: A, P_inverse: AI, Q: B, Q_inverse: BI, M_transitions: M,
    nonconjugacy_warning_witness: {state_id: 0, Q_state_id: B[0], P_inverse_state_id: AI[0]}, checks: c});
  const depths = [], ld = [], recurrent = [], fixed = [], lr = [];
  for (const s of ids) {
    const [x, y] = state(s), [sx, sy] = state(F[s]), a = val(x), b = val(y);
    const orbit = walk(F, s), lo = walk(L, s), depth = orbit.first_zero_index;
    const expectedDepth = Math.max(2 * (m - b), 2 * (m - a) - 1); c = {};
    check('state_encoding_round_trip', sid(x, y), s, c);
    check('closure', r.ideal.includes(sx) && r.ideal.includes(sy), true, c);
    check('product_valuation', val(mul(x, y)), Math.min(m, a + b), c);
    check('second_successor_in_t_squared', val(sy) >= 2, true, c);
    check('orbit_repeat_bound', orbit.state_ids.length <= n + 1, true, c);
    check('unique_recurrent_sink_per_orbit', orbit.cycle_state_ids, [0], c);
    check('recurrent_period_one', orbit.period, 1, c);
    check('exact_clock', depth, expectedDepth, c);
    check('maximum_depth_characterization', depth === 2 * m - 2, b === 1, c);
    check('QMP_pointwise', B[M[A[s]]], F[s], c);
    check('linear_unique_recurrent_sink', lo.cycle_state_ids, [0], c);
    check('linear_clock', lo.first_zero_index, expectedDepth, c);
    if (m === 2) { check('m2_linear_boundary', F[s], L[s], c); check('m2_literal_boundary', F[s], sid(y, 0), c); }
    const nonrepeated = orbit.state_ids.slice(0, -1);
    const scalar = [...nonrepeated.map(id => state(id)[0]), state(nonrepeated[nonrepeated.length - 1])[1]];
    scalar.forEach((z, index) => {
      if (index >= 2) { check('later_scalar_in_t_squared', val(z) >= 2, true, c); check('later_multiplier_valuation_one', val(add(t, z)), 1, c); }
      if (b >= 2) check('noncancellation_chain_valuation', val(z), Math.min(m, (index % 2 ? b : a) + Math.floor(index / 2)), c);
      else if (index % 2) check('cancellation_safe_odd_chain', val(z), Math.min(m, 1 + Math.floor(index / 2)), c);
      else check('cancellation_even_chain_lower_bound', val(z) >= Math.min(m, a + Math.floor(index / 2)), true, c);
    });
    depths.push(depth); ld.push(lo.first_zero_index);
    if (orbit.cycle_start_index === 0) recurrent.push(s);
    if (lo.cycle_start_index === 0) lr.push(s);
    if (F[s] === s) fixed.push(s);
    take('state', {q, m, state_id: s, x_code: x, y_code: y, x_valuation: a, y_valuation: b,
      successor_state_id: F[s], linear_successor_state_id: L[s], orbit, linear_orbit: lo,
      actual_depth: depth, expected_depth: expectedDepth, scalar_path_codes: scalar,
      P_state_id: A[s], M_P_state_id: M[A[s]], Q_M_P_state_id: B[M[A[s]]], checks: c});
  }
  const predicted = [], targetD = [];
  for (const target of ids) {
    const [u, w] = state(target), s = add(t, u), vs = val(s), d = Math.min(vs, m - 1);
    const feasible = val(w) >= d + 1, kernel = r.idealPower(m - d);
    let unit = null, inverse = null, shifted = null, x0 = null;
    if (d < m - 1) { unit = r.shift(s, d); inverse = r.unitInverse(unit); }
    if (feasible) {
      if (d === m - 1) x0 = 0;
      else { shifted = r.shift(w, d + 1); x0 = mul(t, mul(inverse, shifted)); }
    }
    const coset = feasible ? ascending(kernel.map(k => sid(add(x0, k), u))) : [];
    const literal = pre[target], mt = BI[target], transported = ascending(mpre[mt].map(z => AI[z]));
    predicted.push(coset); targetD.push(d); c = {};
    check('fibre_feasibility', literal.length > 0, feasible, c);
    check('fibre_kernel_size', kernel.length, q ** d, c);
    check('fibre_size', literal.length, feasible ? q ** d : 0, c);
    check('fibre_coset_equality', literal, coset, c);
    check('fibre_QMP_transport', literal, transported, c);
    check('fibre_first_coordinate_constraint', literal.map(z => state(z)[1]), literal.map(() => u), c);
    check('fibre_kernel_equation', kernel.map(k => mul(s, k)), kernel.map(() => 0), c);
    if (unit !== null) { check('fibre_unit_inverse', mul(unit, inverse), 1, c); check('fibre_shifted_unit', mul(q ** d, unit), s, c); }
    if (feasible) { check('fibre_representative_in_I', r.ideal.includes(x0), true, c); check('fibre_representative_equation', mul(s, x0), w, c); }
    if (d === m - 1) check('saturated_feasibility', feasible, w === 0, c);
    take('target', {q, m, target_state_id: target, u_code: u, w_code: w, multiplier_code: s,
      multiplier_valuation: vs, d, feasible, predecessor_state_ids: literal,
      actual_fibre_size: literal.length, expected_fibre_size: feasible ? q ** d : 0,
      kernel_codes: kernel, unit_code: unit, inverse_unit_code: inverse, shifted_w_code: shifted,
      representative_x_code: x0, coset_predecessor_state_ids: coset, M_target_state_id: mt,
      M_predecessor_state_ids: mpre[mt], transported_predecessor_state_ids: transported, checks: c});
  }
  for (let h = 0; h <= 2 * m - 2; h++) {
    const exact = ids.filter(s => depths[s] === h), cum = ids.filter(s => depths[s] <= h);
    const lex = ids.filter(s => ld[s] === h), lcum = ids.filter(s => ld[s] <= h);
    const tx = m - Math.ceil(h / 2), ty = m - Math.floor(h / 2);
    const rectangle = ids.filter(s => val(state(s)[0]) >= tx && val(state(s)[1]) >= ty);
    const count = h === 0 ? 1 : (q - 1) * q ** (h - 1); c = {};
    check('cumulative_depth_rectangle', cum, rectangle, c); check('cumulative_depth_count', cum.length, q ** h, c);
    check('exact_depth_count', exact.length, count, c); check('linear_exact_depth_census', lex, exact, c);
    check('linear_cumulative_depth_census', lcum, cum, c);
    take('depth_row', {q, m, h, threshold_x: tx, threshold_y: ty, exact_state_ids: exact,
      cumulative_state_ids: cum, rectangle_state_ids: rectangle, linear_exact_state_ids: lex,
      linear_cumulative_state_ids: lcum, actual_exact_count: exact.length, expected_exact_count: count,
      actual_cumulative_count: cum.length, expected_cumulative_count: q ** h, checks: c});
  }
  const image = ids.filter(s => pre[s].length > 0);
  const imageFormula = q + (q - 1) * range(m - 2).reduce((s, j) => s + q ** (2 * (j + 1)), 0);
  for (let d = 0; d < m; d++) {
    const size = d === 0 ? 0 : q ** d, actual = ids.filter(s => pre[s].length === size);
    const expected = ids.filter(s => d === 0 ? predicted[s].length === 0 : targetD[s] === d && predicted[s].length > 0);
    const count = d === 0 ? n - imageFormula : d === m - 1 ? q : (q - 1) * q ** (2 * (m - d - 1)); c = {};
    check('fibre_census_target_set', actual, expected, c); check('fibre_census_count', actual.length, count, c);
    take('fibre_row', {q, m, d, fibre_size: size, target_state_ids: actual,
      expected_target_state_ids: expected, actual_count: actual.length, expected_count: count, checks: c});
  }
  const maxDepth = Math.max(...depths), maxIds = ids.filter(s => depths[s] === maxDepth);
  const expectedMax = ids.filter(s => val(state(s)[1]) === 1), maxFibre = Math.max(...pre.map(x => x.length));
  const maxFibreIds = ids.filter(s => pre[s].length === maxFibre);
  const saturated = ascending(range(q).map(a => sid(add(nt, a * q ** (m - 1)), 0))); c = {};
  check('zero_fixed', F[0], 0, c); check('unique_recurrent_set', recurrent, [0], c); check('unique_fixed_set', fixed, [0], c);
  check('linear_unique_recurrent_set', lr, [0], c); check('maximum_depth_value', maxDepth, 2 * m - 2, c);
  check('maximum_depth_exact_set', maxIds, expectedMax, c); check('maximum_fibre_value', maxFibre, q ** (m - 1), c);
  check('maximum_fibre_exact_set', maxFibreIds, saturated, c); check('saturated_target_count', saturated.length, q, c);
  check('image_size', image.length, imageFormula, c); check('image_exact_set', image, ids.filter(s => predicted[s].length > 0), c);
  check('predecessor_partition', ascending(pre.flat()), ids, c); check('fibre_mass', pre.reduce((s, a) => s + a.length, 0), n, c);
  const seed = sid(t, nt), co = walk(F, seed), ce = [seed];
  for (let i = 1; i < co.state_ids.length; i++) {
    const exponent = Math.floor(i / 2) + 1, power = exponent < m ? q ** exponent : 0;
    ce.push(i % 2 ? sid(neg(power), 0) : sid(0, neg(power)));
  }
  check('cancellation_witness_trajectory', co.state_ids, ce, c); check('cancellation_witness_clock', co.first_zero_index, 2 * m - 2, c);
  let unequal = null, nonlinear = null;
  if (m >= 3) {
    const small = sid(0, 0), large = sid(nt, 0), witness = sid(t, t);
    unequal = {small_target_state_id: small, large_target_state_id: large,
      small_predecessor_state_ids: pre[small], large_predecessor_state_ids: pre[large],
      small_fibre_size: pre[small].length, large_fibre_size: pre[large].length};
    check('unequal_positive_fibre_small', pre[small].length, q, c); check('unequal_positive_fibre_large', pre[large].length, q ** (m - 1), c);
    check('unequal_positive_fibres', pre[small].length > 0 && pre[small].length < pre[large].length, true, c);
    nonlinear = {state_id: witness, F_state_id: F[witness], L_state_id: L[witness]};
    check('m_ge_3_literal_nonlinear_difference', F[witness] !== L[witness], true, c);
  }
  take('carrier_complete', {q, m, state_count: n, target_count: n, recurrent_state_ids: recurrent,
    fixed_state_ids: fixed, linear_recurrent_state_ids: lr, maximum_depth: maxDepth,
    maximum_depth_state_ids: maxIds, expected_maximum_depth_state_ids: expectedMax,
    maximum_fibre_size: maxFibre, maximum_fibre_target_state_ids: maxFibreIds, saturated_target_state_ids: saturated,
    image_target_state_ids: image, actual_image_size: image.length, expected_image_size: imageFormula,
    empty_fibre_count: n - image.length, unequal_positive_fibre_witness: unequal,
    nonlinear_literal_witness: nonlinear, cancellation_witness: {state_id: seed, orbit: co, expected_state_ids: ce}, checks: c});
  carriers.push({q, m, states: n, targets: n, maximum_depth: maxDepth, image_size: image.length,
    maximum_fibre: maxFibre, all_records_received: true});
}
function provenance() {
  pins(OWN + '/SOURCE.sha256', 4);
  const manifest = pins(OWN + '/INPUTS.sha256', 56);
  const declared = new Set(manifest.map(r => r[0]));
  const preRaw = read(RUN + '/PRE.json'), postRaw = read(RUN + '/POST.json');
  need(preRaw.equals(postRaw), 'archived_pre_post_whole_raw_equal');
  const pre = JSON.parse(preRaw.toString('utf8')), request = json(RUN + '/REQUEST.json');
  const grant = json(ROOT + '/GRANT.initial01.json'), receipt = json(RUN + '/RECEIPT.json'), exit = json(RUN + '/EXIT.json');
  const runtime = json(ROOT + '/RUNTIME_INPUTS.json');
  const expectedKeys = new Map();
  const addPin = (p, h) => {
    need(!expectedKeys.has(p) || expectedKeys.get(p) === h, 'capture_key_no_conflict');
    expectedKeys.set(p, h);
  };
  for (const p of [ROOT + '/RUNTIME_INPUTS.json', ROOT + '/ORDINARY_RUNTIME_POLICY.md',
    ROOT + '/GUARD_SOURCE_RECEPTION.md', SR + '/SOURCE_RECEPTION.md', SR + '/ADOPTED_SOURCE_INPUTS.sha256',
    PREP + '/SOURCE_INPUTS.sha256', PREP + '/BASELINE_INPUTS.sha256',
    Q + '/p212_a_source_root01/RUNTIME_INPUTS.json', PREP + '/PREPARATION_INPUTS.sha256',
    ROOT + '/GRANT.initial01.json']) addPin(p, sha(read(p)));
  for (const [p, n] of [[PREP + '/SOURCE_INPUTS.sha256', 5], [SR + '/ADOPTED_SOURCE_INPUTS.sha256', 28],
    [PREP + '/BASELINE_INPUTS.sha256', 8], [PREP + '/PREPARATION_INPUTS.sha256', 6]])
    for (const row of pins(p, n)) addPin(...row);
  eq(pre.schema, 'P214_AUTHOR_KEYS_V1', 'archived_key_schema'); eq(pre.errors, [], 'archived_key_errors_empty');
  eq(pre.runtime_baseline_metadata_changes, [], 'archived_runtime_changes_empty');
  eq(pre.keys.length, 68, 'archived_complete_68_keys');
  eq(new Set(pre.keys.map(k => k.path)).size, 68, 'archived_no_duplicate_keys');
  const local = pre.keys.filter(k => !k.path.startsWith('/')), host = pre.keys.filter(k => k.path.startsWith('/'));
  eq(local.length, 49, 'archived_49_workspace_keys'); eq(host, runtime.roles, 'archived_19_runtime_keys_complete');
  eq(local.map(k => k.path), [...expectedKeys.keys()].sort((a, b) => a.localeCompare(b, 'en')), 'exact_ordered_capture_key_membership');
  for (const key of local) {
    need(declared.has(key.path), 'archived_workspace_key_explicitly_pinned');
    eq(key.sha256, expectedKeys.get(key.path), 'archived_capture_key_expected_hash');
    read(key.path); eq(inputs.get(key.path).key, key, 'current_workspace_key_matches_archived_capture');
  }
  eq(request.grant, grant, 'archived_request_exact_grant'); eq(request.command, grant.command, 'archived_request_exact_command');
  eq(request.run_id, 'initial01', 'archived_run_id'); eq(request.run_directory, W + '/' + RUN, 'archived_run_directory');
  eq(grant.run_directory, W + '/' + RUN, 'grant_run_directory');
  eq(request.grant_path, ROOT + '/GRANT.initial01.json', 'archived_grant_path');
  for (const [key, path] of [[request.grant_key, request.grant_path], [request.guard_key, PREP + '/guard.js'],
    [request.preparation_manifest_key, PREP + '/PREPARATION_INPUTS.sha256']]) {
    read(path); eq(key, inputs.get(path).key, 'archived_request_key_binding');
  }
  const command = {executable: '/usr/bin/python3.10', args: ['-I', '-S', '-B', W + '/' + P + '/verify.py'],
    cwd: W, env: {LANG: 'C', LC_ALL: 'C'}, stdin: '/dev/null', timeout_ms: 600000};
  eq(grant.command, command, 'exact_scientific_command_archival_only');
  eq([grant.schema, grant.authority, grant.action, grant.run_id, grant.consumption],
    ['P214_AUTHOR_ONE_RUN_GRANT_V1', 'root', 'execute_once', 'initial01', 'ISSUED_AND_CONSUMED_BEFORE_SINGLE_SUBMISSION'], 'grant_identity_and_consumption');
  for (const [name, p] of [['guard_sha256', PREP + '/guard.js'], ['preparation_manifest_sha256', PREP + '/PREPARATION_INPUTS.sha256'],
    ['source_manifest_sha256', PREP + '/SOURCE_INPUTS.sha256'], ['runtime_manifest_sha256', ROOT + '/RUNTIME_INPUTS.json'],
    ['runtime_policy_sha256', ROOT + '/ORDINARY_RUNTIME_POLICY.md'], ['guard_source_reception_sha256', ROOT + '/GUARD_SOURCE_RECEPTION.md'],
    ['source_reception_sha256', SR + '/SOURCE_RECEPTION.md'], ['adopted_source_manifest_sha256', SR + '/ADOPTED_SOURCE_INPUTS.sha256']])
    eq(grant[name], sha(read(p)), 'grant_complete_document_hash');
  eq(receipt.schema, 'P214_AUTHOR_CAPTURE_V1', 'capture_schema'); eq(receipt.run_id, 'initial01', 'capture_run');
  eq([receipt.ordinary_runtime_only, receipt.pre_post_equal, receipt.execution_completed_zero], [true, true, true], 'capture_status');
  eq(receipt.exit, exit, 'capture_exit_document');
  eq([exit.status, exit.signal, exit.error, exit.science_submitted], [0, null, null, true], 'successful_archived_exit');
  need(Number.isSafeInteger(exit.pid) && exit.pid > 0, 'archived_positive_pid');
  eq(receipt.semantic_reception, 'NOT_PERFORMED', 'historical_receipt_semantics_not_rewritten');
  eq(receipt.canonical_adoption, 'NOT_AUTHORIZED', 'no_canonical_claim_in_capture');
  const native = json(ROOT + '/INITIAL_ACTUAL_NATIVE.json');
  eq(native.arguments.cmd, 'node ' + PREP + '/guard.js initial01', 'native_exact_guard_submission');
  eq(native.result.chunk_id, '9644b6', 'native_execution_identity'); eq(native.result.exit_code, 0, 'native_zero_exit');
  need(!Object.hasOwn(native.result, 'session_id'), 'native_no_remaining_session');
  const actual = JSON.parse(native.result.output);
  eq(actual, {status: 'CAPTURED_ZERO_EXIT_NOT_SEMANTIC_PASS', run_directory: W + '/' + RUN,
    stdout_sha256: receipt.stdout.sha256, stdout_bytes: receipt.stdout.bytes}, 'native_complete_capture_correspondence');
  const rootReceipt = read(ROOT + '/INITIAL_RECEPTION.md').toString('utf8');
  need(rootReceipt.includes('RAW_ONLY / SEMANTICS_PENDING / NO_CANONICAL') && rootReceipt.includes('Actual9644b6'), 'root_archived_raw_reception');
  const adopted = pins(SR + '/ADOPTED_SOURCE_INPUTS.sha256', 28);
  need(adopted.every(([p, h]) => declared.has(p) && sha(read(p)) === h), 'accepted_28_source_pins');
  eq(sha(read(P + '/verify.py')), 'dc1d9f73263e8330616b641ee89b0c22cfd5ab9dadb588664b50ca57fa67fb8b', 'accepted_577_line_source_hash');
  eq(read(P + '/verify.py').toString('utf8').split('\n').length - 1, 577, 'accepted_source_complete_lines');
  const parameters = json(P + '/PARAMETERS.json');
  eq(parameters.pairs, BOX, 'documented_parameter_box'); eq(parameters.q_values, [2, 3, 4], 'documented_fields');
  eq(parameters.m_values, [2, 3, 4], 'documented_truncations');
  eq(parameters.deductive_state_counts, BOX.map(([q, m]) => q ** (2 * (m - 1))), 'documented_state_counts');
  eq(parameters.deductive_total_states, 5271, 'documented_total');
  const out = file(RUN + '/stdout.raw'), err = file(RUN + '/stderr.raw');
  for (const [value, key] of [[out, receipt.stdout], [err, receipt.stderr]]) {
    eq({...value.key, path: W + '/' + value.key.path}, key, 'full_capture_bytes_and_metadata');
    inputs.set(value.key.path, value);
  }
  eq(out.key.bytes, 10419112, 'fixed_capture_byte_count');
  eq(out.key.sha256, '4ebeac267f855a1f9b03263ed2517d7a34b6dd0b62639b9fa54129c136763c35', 'fixed_capture_hash');
  eq(err.raw.length, 0, 'empty_complete_stderr');
  need(out.raw.every(b => b === 10 || (b >= 32 && b <= 126)), 'complete_ascii_no_controls');
  need(out.raw[out.raw.length - 1] === 10, 'complete_final_newline');
  lines = out.raw.toString('ascii').slice(0, -1).split('\n');
  eq(lines.length, 10646, 'complete_line_count');
  schema = json(P + '/OUTPUT_SCHEMA.json');
  return {native_chunk: '9644b6', run_directory: RUN, stdout_bytes: out.raw.length, stdout_sha256: out.key.sha256,
    archived_workspace_keys: 49, archived_runtime_keys: 19, runtime_scope: 'archived comparison only; no current host observation'};
}
try {
  need(process.argv.length === 2, 'no_checker_arguments');
  need(process.cwd() === W, 'fixed_checker_working_directory');
  const binding = provenance();
  take('run_start', {parameters: BOX, q_values: [2, 3, 4], m_values: [2, 3, 4], program_role: 'author_verifier',
    mathematical_scope: 'fixed_finite_box_only', configuration_policy: 'embedded_constants_no_external_reads'});
  for (const q of [2, 3, 4]) { const f = field(q); receiveField(f); for (const m of [2, 3, 4]) receiveCarrier(f, m); }
  const c = {}, total = carriers.reduce((s, r) => s + r.states, 0);
  check('complete_cartesian_state_total', total, 5271, c); check('complete_cartesian_target_total', recordCounts.target, 5271, c);
  check('complete_cartesian_carriers', recordCounts.carrier_complete, 9, c); check('complete_state_records', recordCounts.state, 5271, c);
  check('complete_record_census', recordCounts, {run_start: 1, field: 3, carrier: 9, adapter: 9, state: 5271,
    target: 5271, depth_row: 45, fibre_row: 27, carrier_complete: 9}, c);
  take('run_complete', {status: 'FINITE_BOX_CHECKS_PASSED', parameters: BOX, state_count: total, target_count: total,
    carrier_count: 9, check_count: sourceComparisons, check_counts: {...checkCounts}, preceding_record_counts: {...recordCounts},
    checks: c, limitation: 'finite checks do not prove all-parameter theorems or establish novelty'});
  eq(cursor, lines.length, 'no_omitted_or_extra_records');
  eq(sourceComparisons, Object.values(checkCounts).reduce((s, n) => s + n, 0), 'full_check_registry_mass');
  // Closing full-byte rereads cover the exact same workspace DATA; no host reinspection.
  for (const [p, original] of inputs) {
    const current = file(p);
    need(original.raw.equals(current.raw), 'closing_full_raw_input_stability');
    eq(original.key, current.key, 'closing_input_metadata_stability');
  }
  process.stdout.write(JSON.stringify({status: 'P214_INITIAL_ARCHIVED_DATA_SEMANTICS_PASS',
    scope: 'complete archived finite-box DATA reception; not science execution, canonical adoption, proof, novelty or manuscript review',
    binding, assertions, assertion_counts: assertionCounts, independently_recomputed_producer_comparisons: sourceComparisons,
    exact_check_counts: checkCounts, record_counts: recordCounts, carriers,
    complete_input_keys: [...inputs.values()].map(v => v.key), complete_record_ledger: ledger}, null, 2) + '\n');
} catch (error) {
  process.stderr.write((error.stack || String(error)) + '\n');
  process.stdout.write(JSON.stringify({status: 'P214_INITIAL_ARCHIVED_DATA_SEMANTICS_FAIL', error: error.message,
    assertions, consumed_records: cursor, record_counts: recordCounts, completed_record_ledger: ledger}, null, 2) + '\n');
  process.exitCode = 1;
}
