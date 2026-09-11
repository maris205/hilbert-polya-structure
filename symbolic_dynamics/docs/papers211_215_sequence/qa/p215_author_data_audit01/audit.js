'use strict';
// SOURCE ONLY. Root must read this whole stable file and separately grant DATA.
// Archived DATA reconstruction: no producer import, subprocess, host read or write.
const fs = require('node:fs');
const crypto = require('node:crypto');
const W = '/root/autodl-tmp/symbolic_dynamics';
const Q = 'docs/papers211_215_sequence/qa';
const OWN = Q + '/p215_author_data_audit01';
const P = 'papers/215-prefix-drawdown-clock';
const PREP = Q + '/p215_runtime_preparation01';
const ROOT = Q + '/p215_runtime_root01';
const SR = Q + '/p215_source_root01';
const RUN = Q + '/p215_author_runs/initial01';
const BASE = Q + '/p212_a_source_root01/RUNTIME_INPUTS.json';
const META = ['dev', 'ino', 'mode', 'size', 'mtimeNs', 'ctimeNs'];
const NS = [0, 1, 2, 3, 4, 5], QS = [0, 1, 2, 3];
const RAW_BYTES = 2724478;
const RAW_SHA = 'd8a654f53890a94736bb03c1aceaee3975cd53580fa5d212b3482f035a5df405';
const SOURCE_HASH = 'd516bb381f01c38047c29d4b4b2f8d4c4f4ef8d19791feb1d645d681dfe43eda';
const STATIC = [
  [PREP + '/SOURCE_INPUTS.sha256', '7b73a767da3dac14aeb06f32a38f8c88b9589332d6d47c81431dffaeaf06b748'],
  [PREP + '/BASELINE_INPUTS.sha256', '4b2dd204ae71177aa3ba78dd98447fcfe5afda9587cec3a76111a8d37030fc4a'],
  [P + '/SOURCE_PREPARED.sha256', 'f0c78f9629e59e3332324f0533d615deb938b39fdd784164a8099fa2081cd123'],
  [BASE, 'fd64f171325548a01dc076ceda92685aad6577485334e7622d7a84ee4bc9e22b']
];
const CAPTURE_DOCS = ['REQUEST.json', 'PRE.json', 'EXIT.json', 'POST.json', 'RECEIPT.json'];
const SOURCE_PAYLOADS = ['audit.js', 'INPUTS.sha256', 'SOURCE_COVERAGE.md', 'EXECUTION_REQUEST.proposed.json'];
const inputs = new Map(), ledger = [], boxesReport = [];
const assertionCounts = Object.create(null), comparisonCounts = Object.create(null);
let assertions = 0, producerComparisons = 0, producerFailures = 0;
let completeStates = 0, completeTargets = 0, recurrenceRows = 0, subtractionTerms = 0;

function need(ok, label, detail = '') {
  assertions++;
  assertionCounts[label] = (assertionCounts[label] || 0) + 1;
  if (!ok) throw new Error(label + (detail ? ': ' + detail : ''));
}
function sha(raw) { return crypto.createHash('sha256').update(raw).digest('hex'); }
function plainObject(x) { return x !== null && typeof x === 'object' && Object.getPrototypeOf(x) === Object.prototype; }
function identical(a, b) {
  if (typeof a !== typeof b) return false;
  if (a === null || b === null || typeof a !== 'object') return Object.is(a, b);
  if (Array.isArray(a) || Array.isArray(b))
    return Array.isArray(a) && Array.isArray(b) && a.length === b.length && a.every((v, i) => identical(v, b[i]));
  const ak = Object.keys(a).sort(), bk = Object.keys(b).sort();
  return identical(ak, bk) && ak.every(k => identical(a[k], b[k]));
}
function exact(a, b, path) {
  need(typeof a === typeof b, 'typed_kind', path);
  if (a === null || b === null || typeof a !== 'object') {
    need(Object.is(a, b), 'typed_primitive', path); return;
  }
  if (Array.isArray(a) || Array.isArray(b)) {
    need(Array.isArray(a) && Array.isArray(b), 'typed_array', path);
    need(a.length === b.length, 'exact_array_length', path);
    for (let j = 0; j < a.length; j++) exact(a[j], b[j], path + '/' + j);
    return;
  }
  need(plainObject(a) && plainObject(b), 'plain_object', path);
  const ak = Object.keys(a).sort(), bk = Object.keys(b).sort();
  need(identical(ak, bk), 'exact_object_keys', path);
  for (const k of ak) exact(a[k], b[k], path + '/' + k);
}
function wire(x) {
  if (x === null) return 'null';
  if (typeof x === 'boolean') return x ? 'true' : 'false';
  if (typeof x === 'number') {
    need(Number.isSafeInteger(x) && !Object.is(x, -0), 'scientific_exact_integer');
    return String(x);
  }
  if (typeof x === 'string') {
    need([...x].every(c => c.charCodeAt(0) >= 32 && c.charCodeAt(0) <= 126), 'scientific_printable_string');
    return JSON.stringify(x);
  }
  if (Array.isArray(x)) return '[' + x.map(wire).join(',') + ']';
  need(plainObject(x), 'scientific_json_value');
  return '{' + Object.keys(x).sort().map(k => wire(k) + ':' + wire(x[k])).join(',') + '}';
}
function relative(p) {
  need(typeof p === 'string' && /^[A-Za-z0-9_./-]+$/.test(p) && !p.startsWith('/') &&
    p.split('/').every(s => s !== '' && s !== '.' && s !== '..'), 'workspace_only_path', String(p));
  return W + '/' + p;
}
function metadata(s) { return Object.fromEntries(META.map(k => [k, String(s[k])])); }
function file(p) {
  const full = relative(p), fd = fs.openSync(full, 'r');
  try {
    const before = fs.fstatSync(fd, {bigint: true});
    need(before.isFile(), 'regular_workspace_file', p);
    const raw = fs.readFileSync(fd), after = fs.fstatSync(fd, {bigint: true});
    exact(metadata(before), metadata(after), 'read-stability/' + p);
    exact(metadata(after), metadata(fs.statSync(full, {bigint: true})), 'path-stability/' + p);
    need(BigInt(raw.length) === after.size, 'complete_workspace_read', p);
    return {raw, key: {path: p, kind: 'regular-file', bytes: raw.length, sha256: sha(raw), metadata: metadata(after)}};
  } finally { fs.closeSync(fd); }
}
function read(p) {
  if (!inputs.has(p)) inputs.set(p, file(p));
  return inputs.get(p).raw;
}
function json(p) { return JSON.parse(read(p).toString('utf8')); }
function pinRows(p, count, base = '') {
  const raw = read(p);
  need(raw.length > 0 && raw[raw.length - 1] === 10, 'pin_final_lf', p);
  need(raw.every(b => b === 10 || (b >= 32 && b <= 126)), 'pin_ascii_bytes', p);
  const rows = raw.toString('ascii').slice(0, -1).split('\n').map(line => {
    need(/^[0-9a-f]{64}  [A-Za-z0-9_./-]+$/.test(line), 'strict_pin_row', p);
    const suffix = line.slice(66); relative(suffix);
    return [base ? base + '/' + suffix : suffix, line.slice(0, 64)];
  });
  need(rows.length === count && new Set(rows.map(r => r[0])).size === count, 'exact_pin_census', p);
  return rows;
}
function receivePins(p, count, base = '') {
  const rows = pinRows(p, count, base);
  for (const [path, hash] of rows) exact(sha(read(path)), hash, 'pin/' + path);
  return rows;
}
function regularKey(k, path) {
  need(plainObject(k), 'key_object', path);
  exact(Object.keys(k).sort(), ['path', 'kind', 'bytes', 'sha256', 'metadata'].sort(), 'key-fields/' + path);
  need(k.path === path && k.kind === 'regular-file', 'key_identity', path);
  need(Number.isSafeInteger(k.bytes) && k.bytes >= 0 && typeof k.sha256 === 'string' && /^[0-9a-f]{64}$/.test(k.sha256), 'key_bytes_hash', path);
  exact(Object.keys(k.metadata).sort(), META.slice().sort(), 'metadata-fields/' + path);
  for (const name of META) need(typeof k.metadata[name] === 'string' && /^(0|[1-9][0-9]*)$/.test(k.metadata[name]), 'metadata_decimal', path + '/' + name);
  exact(k.metadata.size, String(k.bytes), 'metadata-size/' + path);
}

// The local JSON Schema is pinned DATA. No resolver, package or network is used.
function schemaMatches(v, s, root) {
  if (s.$ref !== undefined) {
    if (!/^#\/\$defs\/[A-Za-z_]+$/.test(s.$ref)) return false;
    return schemaMatches(v, root.$defs[s.$ref.slice(8)], root);
  }
  if (s.oneOf && s.oneOf.filter(t => schemaMatches(v, t, root)).length !== 1) return false;
  if (s.type !== undefined) {
    const names = Array.isArray(s.type) ? s.type : [s.type];
    const yes = names.some(t => t === 'null' ? v === null : t === 'array' ? Array.isArray(v) :
      t === 'object' ? plainObject(v) : t === 'integer' ? Number.isSafeInteger(v) : typeof v === t);
    if (!yes) return false;
  }
  if (Object.hasOwn(s, 'const') && !identical(v, s.const)) return false;
  if (typeof v === 'number' && ((s.minimum !== undefined && v < s.minimum) || (s.maximum !== undefined && v > s.maximum))) return false;
  if (typeof v === 'string' && s.pattern !== undefined && !new RegExp(s.pattern).test(v)) return false;
  if (Array.isArray(v)) {
    if ((s.minItems !== undefined && v.length < s.minItems) || (s.maxItems !== undefined && v.length > s.maxItems)) return false;
    if (s.items && !v.every(x => schemaMatches(x, s.items, root))) return false;
  }
  if (plainObject(v)) {
    if (s.required && !s.required.every(k => Object.hasOwn(v, k))) return false;
    const props = s.properties || {};
    if (s.additionalProperties === false && Object.keys(v).some(k => !Object.hasOwn(props, k))) return false;
    for (const [k, t] of Object.entries(props)) if (Object.hasOwn(v, k) && !schemaMatches(v[k], t, root)) return false;
  }
  return true;
}
function schemaVocabulary(s) {
  const allowed = ['$schema', 'title', '$defs', '$ref', 'oneOf', 'type', 'const', 'minimum', 'maximum',
    'pattern', 'minItems', 'maxItems', 'items', 'required', 'properties', 'additionalProperties'];
  need(plainObject(s) && Object.keys(s).every(k => allowed.includes(k)), 'supported_schema_vocabulary');
  if (s.$defs) for (const t of Object.values(s.$defs)) schemaVocabulary(t);
  if (s.properties) for (const t of Object.values(s.properties)) schemaVocabulary(t);
  if (s.items) schemaVocabulary(s.items);
  if (s.oneOf) s.oneOf.forEach(schemaVocabulary);
}

function provenance() {
  const own = receivePins(OWN + '/SOURCE.sha256', 4);
  exact(own.map(r => r[0]).sort(), SOURCE_PAYLOADS.map(s => OWN + '/' + s).sort(), 'own-exact-source-members');
  const declaredRows = receivePins(OWN + '/INPUTS.sha256', 55);
  const declared = new Map(declaredRows);
  for (const [p, h] of STATIC) exact(sha(read(p)), h, 'capture-static/' + p);
  const command = {executable: '/usr/bin/python3.10', args: ['-I', '-S', '-B', W + '/' + P + '/verify.py'],
    cwd: W, env: {LANG: 'C', LC_ALL: 'C'}, stdin: '/dev/null', timeout_ms: 600000};
  const grantPath = ROOT + '/GRANT.initial01.json', grant = json(grantPath);
  const grantBindings = [
    ['guard_sha256', PREP + '/guard.js'], ['preparation_manifest_sha256', PREP + '/PREPARATION_INPUTS.sha256'],
    ['source_manifest_sha256', PREP + '/SOURCE_INPUTS.sha256'], ['source_reception_sha256', SR + '/SOURCE_RECEPTION.md'],
    ['runtime_manifest_sha256', ROOT + '/RUNTIME_INPUTS.json'], ['runtime_policy_sha256', ROOT + '/ORDINARY_RUNTIME_POLICY.md'],
    ['guard_source_reception_sha256', ROOT + '/GUARD_SOURCE_RECEPTION.md']
  ];
  exact(grant, {schema: 'P215_AUTHOR_ONE_RUN_GRANT_V1', authority: 'root', action: 'execute_once',
    run_id: 'initial01', run_directory: W + '/' + RUN,
    ...Object.fromEntries(grantBindings.map(([field, path]) => [field, sha(read(path))])), command}, 'complete-13-field-grant');
  const expected = new Map();
  function add(p, h) {
    need(!expected.has(p) || expected.get(p) === h, 'capture_pin_no_conflict', p); expected.set(p, h);
  }
  for (const [field, path] of grantBindings.slice(3)) add(path, grant[field]);
  STATIC.forEach(([p, h]) => add(p, h));
  add(PREP + '/PREPARATION_INPUTS.sha256', grant.preparation_manifest_sha256);
  add(grantPath, sha(read(grantPath)));
  for (const [p, n] of [[PREP + '/SOURCE_INPUTS.sha256', 25], [PREP + '/BASELINE_INPUTS.sha256', 8],
    [PREP + '/PREPARATION_INPUTS.sha256', 6]]) for (const [name, hash] of receivePins(p, n)) add(name, hash);
  need(expected.size === 46, 'complete_46_workspace_capture_keys');
  const sourceRows = receivePins(P + '/SOURCE_PREPARED.sha256', 25, P);
  exact(sourceRows, pinRows(PREP + '/SOURCE_INPUTS.sha256', 25), 'same_25_source_projection');
  const prepSeal = receivePins(PREP + '/SHA256SUMS', 7, PREP);
  exact(prepSeal.map(r => r[0]).sort(), [PREP + '/PREPARATION_INPUTS.sha256',
    ...pinRows(PREP + '/PREPARATION_INPUTS.sha256', 6).map(r => r[0])].sort(), 'exact_preparation_seal_members');
  const extra = [...CAPTURE_DOCS.map(n => RUN + '/' + n), ROOT + '/INITIAL_NATIVE.json',
    PREP + '/SHA256SUMS', 'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md', 'docs/research_state/WORKFLOW.md'];
  exact([...declared.keys()].sort(), [...expected.keys(), ...extra].sort(), 'exact_55_pinned_input_members');
  for (const [p, h] of expected) exact(declared.get(p), h, 'all-capture-keys-pinned/' + p);
  exact(sha(read(P + '/verify.py')), SOURCE_HASH, 'accepted_complete_author_source_hash');
  exact(read(P + '/verify.py').toString('utf8').split('\n').length - 1, 310, 'accepted_author_source_lines');

  const runtime = json(ROOT + '/RUNTIME_INPUTS.json'), baseline = json(BASE);
  exact(Object.keys(runtime).sort(), ['status', 'ordinary_trust_only', 'origin', 'roles', 'historical_metadata_changes'].sort(), 'runtime-document-fields');
  exact([runtime.status, runtime.ordinary_trust_only, runtime.origin, runtime.historical_metadata_changes],
    ['CURRENT_SELECTED_RUNTIME_PREFLIGHT_PASS', true, BASE, []], 'runtime-document-boundary');
  need(runtime.roles.length === 19 && new Set(runtime.roles.map(r => r.path)).size === 19, 'runtime_19_distinct_archived_roles');
  const projection = r => r.kind === 'required-absence' ? {path: r.path, kind: r.kind, errno: r.errno} :
    {path: r.path, kind: r.kind, bytes: r.bytes, sha256: r.sha256};
  exact(runtime.roles.map(projection), baseline.roles.map(projection), 'fixed_19_role_content_projection');
  exact(runtime.roles, baseline.roles, 'zero_historical_metadata_drift_full_roles');
  let regulars = 0, absences = 0;
  for (const role of runtime.roles) {
    need(typeof role.path === 'string' && role.path.startsWith('/'), 'archived_absolute_host_label_only');
    if (role.kind === 'required-absence') {
      exact(role, {path: '/usr/lib/python310.zip', kind: 'required-absence', errno: 'ENOENT'}, 'archived_zip_absence'); absences++;
    } else { regularKey(role, role.path); regulars++; }
  }
  exact([regulars, absences], [18, 1], 'archived_runtime_kind_census');
  const preRaw = read(RUN + '/PRE.json'), postRaw = read(RUN + '/POST.json');
  need(preRaw.equals(postRaw), 'complete_pre_post_raw_identity');
  const pre = JSON.parse(preRaw.toString('utf8'));
  const localPaths = [...expected.keys()].sort((a, b) => a.localeCompare(b, 'en'));
  const localKeys = localPaths.map(p => { read(p); return inputs.get(p).key; });
  exact(pre, {schema: 'P215_AUTHOR_KEYS_V1', keys: [...localKeys, ...runtime.roles], errors: [],
    runtime_baseline_metadata_changes: []}, 'complete_typed_65_pre_post_keys');
  for (const k of localKeys) regularKey(k, k.path);
  const request = json(RUN + '/REQUEST.json');
  exact(request, {grant_path: grantPath, grant_key: inputs.get(grantPath).key, grant, command,
    run_id: 'initial01', run_directory: W + '/' + RUN, guard_key: inputs.get(PREP + '/guard.js').key,
    preparation_manifest_key: inputs.get(PREP + '/PREPARATION_INPUTS.sha256').key}, 'complete_capture_request');
  const exit = json(RUN + '/EXIT.json');
  exact(exit, {status: 0, signal: null, error: null, pid: 146288, science_submitted: true}, 'complete_actual_exit');
  const receipt = json(RUN + '/RECEIPT.json');
  regularKey(receipt.stdout, W + '/' + RUN + '/stdout.raw');
  regularKey(receipt.stderr, W + '/' + RUN + '/stderr.raw');
  exact(receipt, {schema: 'P215_AUTHOR_CAPTURE_V1', run_id: 'initial01', ordinary_runtime_only: true,
    pre_post_equal: true, exit, stdout: receipt.stdout, stderr: receipt.stderr, execution_completed_zero: true,
    semantic_reception: 'NOT_PERFORMED', canonical_adoption: 'NOT_AUTHORIZED'}, 'complete_capture_receipt');
  const nativeSummary = {status: 'CAPTURED_ZERO_EXIT_NOT_SEMANTIC_PASS', run_directory: W + '/' + RUN,
    stdout_sha256: RAW_SHA, stdout_bytes: RAW_BYTES};
  exact(json(ROOT + '/INITIAL_NATIVE.json'), {
    arguments: {cmd: 'node ' + PREP + '/guard.js initial01', workdir: W, shell: '/bin/bash',
      login: false, tty: false, yield_time_ms: 1000, max_output_tokens: 2000},
    result: {chunk_id: '2bc032', wall_time_seconds: 0.778686962, exit_code: 0, original_token_count: 67,
      output: JSON.stringify(nativeSummary) + '\n'}}, 'entire_native_request_result_no_session');
  exact(fs.readdirSync(relative(RUN)).sort(), [...CAPTURE_DOCS, 'stdout.raw', 'stderr.raw'].sort(), 'exact_complete_capture_inventory');

  // These are the first scientific stream reads. They occur only in a granted DATA run.
  const out = read(RUN + '/stdout.raw'), err = read(RUN + '/stderr.raw');
  for (const name of ['stdout', 'stderr']) {
    const key = inputs.get(RUN + '/' + name + '.raw').key;
    exact({...key, path: W + '/' + key.path}, receipt[name], 'whole_stream_bytes_and_six_metadata/' + name);
  }
  exact([out.length, sha(out), err.length], [RAW_BYTES, RAW_SHA, 0], 'fixed_actual_whole_stream_identity');
  need(out.length > 0 && out[out.length - 1] === 10 && out.subarray(0, -1).every(b => b >= 32 && b <= 126), 'one_ascii_document_exact_final_lf');
  const actual = JSON.parse(out.toString('ascii'));
  need(Buffer.from(wire(actual) + '\n', 'ascii').equals(out), 'entire_sorted_compact_wire_identity');
  const schema = json(P + '/OUTPUT_SCHEMA.json'); schemaVocabulary(schema);
  exact(schema.$schema, 'https://json-schema.org/draft/2020-12/schema', 'schema_dialect_documentary_only');
  need(schemaMatches(actual, schema, schema), 'complete_structural_schema');
  const parameters = json(P + '/PARAMETERS.json');
  exact(parameters, {paper: 215, phase: 'AUTHOR_SOURCE_ONLY', n: NS, q: QS,
    order: 'n_outer_q_inner_ascending', carrier: 'all_words_over_0_through_q_of_length_n', state_order: 'lexicographic',
    expected_boxes: 24, expected_states_by_n: [4, 10, 30, 100, 354, 1300], expected_total_states: 1798,
    expected_counts_status: 'source_derived_not_executed', duplicate_singleton_boxes: 'retained_separately',
    cli_parameter_overrides: false, execution_authorized_by_this_file: false}, 'complete_fixed_parameters');
  return {actual, raw: out, binding: {native_chunk: '2bc032', native_session: null, science_pid: exit.pid,
    run_directory: RUN, stdout_bytes: out.length, stdout_sha256: sha(out), workspace_keys: 46, runtime_keys: 19,
    runtime_scope: 'archived role DATA only; no present host observation', canonical_adopted_by_checker: false}};
}

// Independent finite DATA representation: base codes, direct prefix maxima and Floyd cycles.
function decode(id, n, q) {
  const a = Array(n).fill(0), base = q + 1;
  for (let j = n - 1; j >= 0; j--) { a[j] = id % base; id = Math.floor(id / base); }
  need(id === 0, 'complete_base_decode'); return a;
}
function encode(a, q) { return a.reduce((code, x) => code * (q + 1) + x, 0); }
function drawdown(a) { return a.map((x, j) => Math.max(...a.slice(0, j + 1)) - x); }
function floyd(next, start) {
  let slow = next[start], fast = next[next[start]], steps = 0;
  while (slow !== fast) {
    slow = next[slow]; fast = next[next[fast]]; steps++;
    need(steps <= next.length, 'finite_floyd_meeting_bound');
  }
  let mu = 0; slow = start;
  while (slow !== fast) { slow = next[slow]; fast = next[fast]; mu++; need(mu < next.length, 'finite_floyd_entry_bound'); }
  let period = 1; fast = next[slow];
  while (slow !== fast) { fast = next[fast]; period++; need(period <= next.length, 'finite_floyd_period_bound'); }
  const ids = [start];
  for (let j = 0; j < mu + period; j++) ids.push(next[ids[ids.length - 1]]);
  need(ids[ids.length - 1] === ids[mu] && new Set(ids.slice(0, -1)).size === ids.length - 1, 'complete_first_repeat_trajectory');
  return {mu, period, ids, cycle: ids.slice(mu, -1)};
}
function signData(a) {
  const differences = a.map((v, j) => v - (j === 0 ? 0 : a[j - 1]));
  const signs = differences.filter(v => v !== 0).map(Math.sign);
  return {differences, signs, runs: signs.filter((s, j) => j === 0 || signs[j - 1] !== s)};
}
function binomial(u, l) {
  need(Number.isSafeInteger(u) && Number.isSafeInteger(l) && u >= 0 && l >= 0, 'binomial_nonnegative_indices');
  if (l > u) return 0;
  let row = [1];
  for (let i = 1; i <= u; i++) row = Array.from({length: i + 1}, (_, j) => (row[j - 1] || 0) + (row[j] || 0));
  return row[l];
}
function monotone(length, low, high) {
  const result = [];
  function visit(prefix, lower) {
    if (prefix.length === length) { result.push(prefix); return; }
    for (let v = lower; v <= high; v++) visit([...prefix, v], v);
  }
  visit([], low); return result;
}
function formulaFor(y, q) {
  if (y.length === 0) return {zeros: [], b: [], B: [], c: [], A: [1], recurrence_terms: [],
    height_sequences: [[]], constructed_sources: [[]], count: 1};
  if (y[0] !== 0) return {zeros: [], b: [], B: [], c: [], A: [], recurrence_terms: [],
    height_sequences: [], constructed_sources: [], count: 0};
  const zeros = y.map((v, i) => v === 0 ? i + 1 : 0).filter(v => v !== 0), k = zeros.length;
  const ends = [...zeros.slice(1).map(z => z - 1), y.length];
  const b = zeros.map((z, j) => Math.max(...y.slice(z - 1, ends[j])));
  const B = b.map((unused, j) => Math.max(...b.slice(0, j + 1)));
  const c = B.slice().reverse().map(v => q - v), heights = [];
  function grow(prefix) {
    const j = prefix.length;
    if (j === k) { heights.push(prefix); return; }
    const lower = Math.max(B[j], j ? prefix[j - 1] : 0);
    for (let v = lower; v <= q; v++) grow([...prefix, v]);
  }
  grow([]);
  const sources = heights.map(h => y.map((v, i) => {
    const j = zeros.filter(z => z <= i + 1).length - 1;
    return h[j] - v;
  }));
  sources.forEach((source, j) => {
    need(source.length === y.length && source.every(v => Number.isSafeInteger(v) && v >= 0 && v <= q), 'each_constructed_source_in_carrier');
    exact(drawdown(source), y, 'each_constructed_source_literal_image');
    exact(zeros.map(z => Math.max(...source.slice(0, z))), heights[j], 'each_height_recovered_from_source');
  });
  const A = [1], terms = [];
  for (let m = 1; m <= k; m++) {
    const candidates = monotone(m, 0, c[m - 1]), firstBad = Array(m).fill(0);
    let valid = 0;
    for (const candidate of candidates) {
      const first = candidate.findIndex((a, j) => a > c[j]);
      if (first === -1) valid++; else firstBad[first]++;
    }
    const base = binomial(c[m - 1] + m, m), subs = [];
    exact(base, candidates.length, 'recurrence-combinatorial-base');
    exact(firstBad[m - 1], 0, 'last-ceiling-cannot-first-fail');
    for (let i = 1; i < m; i++) {
      const upper = c[m - 1] - c[i - 1] + m - i, lower = m - i + 1;
      const coefficient = binomial(upper, lower), product = A[i - 1] * coefficient;
      exact(coefficient, monotone(lower, c[i - 1] + 1, c[m - 1]).length, 'every-suffix-binomial-enumeration');
      exact(product, firstBad[i - 1], 'every-first-violation-class');
      subs.push({i, prefix_count: A[i - 1], upper, lower, binomial: coefficient, product}); subtractionTerms++;
    }
    const value = base - subs.reduce((s, t) => s + t.product, 0);
    exact(value, valid, 'every-recurrence-valid-prefix-count');
    A.push(valid);
    terms.push({m, base_upper: c[m - 1] + m, base_lower: m, base, subtractions: subs, value}); recurrenceRows++;
  }
  exact(A[k], heights.length, 'independent-ceiling-and-height-count');
  return {zeros, b, B, c, A, recurrence_terms: terms, height_sequences: heights, constructed_sources: sources, count: A[k]};
}
function cmpWord(a, b) {
  for (let j = 0; j < Math.min(a.length, b.length); j++) if (a[j] !== b[j]) return a[j] - b[j];
  return a.length - b.length;
}
function comparison(name, actual, expected) {
  const pass = identical(actual, expected);
  producerComparisons++; comparisonCounts[name] = (comparisonCounts[name] || 0) + 1;
  if (!pass) producerFailures++;
  return {name, actual, expected, pass};
}
function take(kind, path, actual, expected, n = null, q = null, index = null) {
  const begin = assertions; exact(actual, expected, path);
  const raw = Buffer.from(wire(actual), 'ascii');
  ledger.push({kind, json_pointer: path, n, q, index, canonical_subtree_bytes: raw.length,
    canonical_subtree_sha256: sha(raw), typed_assertions: assertions - begin,
    comparison_names: actual.comparisons.map(c => c.name)});
}
function receiveBox(actual, n, q, boxIndex) {
  const size = (q + 1) ** n, states = Array.from({length: size}, (_, id) => decode(id, n, q));
  const outputs = states.map(drawdown), next = outputs.map(a => encode(a, q));
  outputs.forEach(a => need(a.length === n && a.every(x => Number.isSafeInteger(x) && x >= 0 && x <= q), 'literal_carrier_closure'));
  states.forEach((a, id) => exact(encode(a, q), id, 'independent-base-bijection'));
  const pre = Array.from({length: size}, () => []);
  next.forEach((target, source) => pre[target].push(source));
  const zero = Array(n).fill(0), recurrent = new Set(), depths = [], stateRows = [], expectedDeepest = [];
  const clockCensus = Array(size + 1).fill(0), fibreCensus = Array(size + 1).fill(0);
  const bp = '/boxes/' + boxIndex;
  need(plainObject(actual) && Array.isArray(actual.states) && Array.isArray(actual.targets), 'box_records_present', bp);
  exact(actual.states.length, size, bp + '/states-length'); exact(actual.targets.length, size, bp + '/targets-length');
  for (let id = 0; id < size; id++) {
    const x = states[id], fx = outputs[id], walk = floyd(next, id), a = signData(x), b = signData(fx);
    const cycle = walk.cycle.map(i => states[i]); walk.cycle.forEach(i => recurrent.add(i));
    depths.push(walk.mu); clockCensus[walk.mu]++;
    const alternating = a.differences.every(v => v !== 0) && a.differences.slice(1).every((v, j) => v * a.differences[j] < 0);
    const maximal = n > 0 && q > 0 ? alternating : identical(x, zero);
    if (maximal) expectedDeepest.push(x);
    const comparisons = [
      comparison('exact_clock', walk.mu, a.runs.length), comparison('cycle_is_zero', cycle, [zero]),
      comparison('output_runs', b.runs, a.runs.slice(1).map(s => -s)),
      comparison('run_drop', b.runs.length, Math.max(0, a.runs.length - 1)),
      comparison('deepest_predicate', walk.mu === (n > 0 && q > 0 ? n : 0), maximal)
    ];
    const expected = {x, Fx: fx, orbit: walk.ids.map(i => states[i]), repeat_index: walk.mu, period: walk.period,
      cycle, clock: walk.mu, differences: a.differences, nonzero_signs: a.signs, runs: a.runs,
      output_differences: b.differences, output_nonzero_signs: b.signs, output_runs: b.runs,
      alternating_nonzero: alternating, maximal_predicate: maximal, comparisons};
    take('state', bp + '/states/' + id, actual.states[id], expected, n, q, id); stateRows.push(expected); completeStates++;
  }
  const targets = [], image = [], expectedImage = [], counts = pre.map(a => a.length);
  for (let id = 0; id < size; id++) {
    const y = states[id], bucket = pre[id].map(i => states[i]), formula = formulaFor(y, q), source = formula.constructed_sources;
    const predicate = n === 0 || y[0] === 0;
    if (bucket.length) image.push(y); if (predicate) expectedImage.push(y); fibreCensus[bucket.length]++;
    const comparisons = [
      comparison('complete_fibre', bucket, source.slice().sort(cmpWord)),
      comparison('construction_injective', source.length, new Set(source.map(a => encode(a, q))).size),
      comparison('height_source_lengths', formula.height_sequences.length, source.length),
      comparison('recurrence_actual', formula.count, bucket.length),
      comparison('recurrence_construction', formula.count, source.length),
      comparison('image_predicate', bucket.length > 0, predicate)
    ];
    const expected = {y, actual_predecessors: bucket, actual_count: bucket.length, image_predicate: predicate, formula, comparisons};
    take('target', bp + '/targets/' + id, actual.targets[id], expected, n, q, id); targets.push(expected); completeTargets++;
  }
  const height = Math.max(...depths), deepest = states.filter((unused, id) => depths[id] === height);
  const maximum = Math.max(...counts), maximumTargets = states.filter((unused, id) => counts[id] === maximum);
  const recurrentStates = [...recurrent].sort((a, b) => a - b).map(i => states[i]);
  const comparisons = [
    comparison('carrier_size', states.length, (q + 1) ** n), comparison('unique_recurrent', recurrentStates, [zero]),
    comparison('sharp_height', height, n > 0 && q > 0 ? n : 0), comparison('complete_deepest_set', deepest, expectedDeepest),
    comparison('complete_image', image, expectedImage), comparison('image_size', image.length, n ? (q + 1) ** (n - 1) : 1),
    comparison('maximum_fibre', maximum, binomial(q + n, n)), comparison('maximum_fibre_targets', maximumTargets, [zero]),
    comparison('clock_census_total', clockCensus.reduce((s, v) => s + v, 0), size),
    comparison('target_census_total', fibreCensus.reduce((s, v) => s + v, 0), size),
    comparison('fibre_mass', fibreCensus.reduce((s, v, i) => s + i * v, 0), size)
  ];
  const expected = {n, q, carrier_size: size, states: stateRows, targets, recurrent_states: recurrentStates, height,
    deepest_states: deepest, expected_deepest_states: expectedDeepest, image, expected_image: expectedImage,
    maximum_fibre: maximum, maximum_fibre_targets: maximumTargets, clock_census: clockCensus, fibre_census: fibreCensus, comparisons};
  take('box', bp, actual, expected, n, q, boxIndex);
  boxesReport.push({n, q, states: size, targets: size, height, image_size: image.length, maximum_fibre: maximum,
    all_states_targets_and_zero_census_bins_received: true});
  return expected;
}

try {
  need(process.argv.length === 2, 'no_checker_arguments');
  need(process.cwd() === W, 'fixed_workspace_cwd');
  const received = provenance(), actual = received.actual;
  exact(actual.boxes.length, NS.length * QS.length, 'all_24_boxes');
  const expectedBoxes = [];
  for (const n of NS) for (const q of QS) expectedBoxes.push(receiveBox(actual.boxes[expectedBoxes.length], n, q, expectedBoxes.length));
  const total = expectedBoxes.reduce((s, b) => s + b.carrier_size, 0);
  const comparisons = [comparison('box_count', expectedBoxes.length, 24), comparison('state_count', total, 1798)];
  const expected = {kind: 'p215_author_verification', schema_version: 1, parameters: {n: NS, q: QS}, boxes: expectedBoxes,
    comparisons, checks: producerComparisons, failures: producerFailures, pass: producerFailures === 0};
  take('document', '', actual, expected);
  need(Buffer.from(wire(expected) + '\n', 'ascii').equals(received.raw), 'complete_independently_reconstructed_raw_wire');
  exact([completeStates, completeTargets, producerComparisons, producerFailures], [1798, 1798, 20044, 0], 'independent_complete_totals');
  exact(Object.values(comparisonCounts).reduce((s, n) => s + n, 0), producerComparisons, 'complete_comparison_registry_mass');
  exact(ledger.length, completeStates + completeTargets + expectedBoxes.length + 1, 'complete_subtree_ledger_census');
  // Full closing rereads are workspace DATA only. No host role path reaches file().
  for (const [p, original] of inputs) {
    const closing = file(p);
    need(original.raw.equals(closing.raw), 'closing_full_raw_stability', p);
    exact(original.key, closing.key, 'closing-six-metadata/' + p);
  }
  process.stdout.write(JSON.stringify({status: 'P215_INITIAL_ARCHIVED_DATA_SEMANTICS_PASS',
    scope: 'complete fixed-box archived DATA only; no producer run, canonical adoption, new proof, A/B review or build',
    binding: received.binding, assertions, assertion_counts: assertionCounts, complete_boxes: expectedBoxes.length,
    complete_states: completeStates, complete_targets: completeTargets, producer_comparisons: producerComparisons,
    producer_failures: producerFailures, complete_comparison_counts: comparisonCounts,
    recurrence_rows: recurrenceRows, first_violation_subtractions: subtractionTerms, boxes: boxesReport,
    complete_input_keys: [...inputs.values()].map(v => v.key), complete_compared_subtree_ledger: ledger}, null, 2) + '\n');
} catch (error) {
  process.stderr.write((error.stack || String(error)) + '\n');
  process.stdout.write(JSON.stringify({status: 'P215_INITIAL_ARCHIVED_DATA_SEMANTICS_FAIL', error: error.message,
    assertions, assertion_counts: assertionCounts, complete_states: completeStates, complete_targets: completeTargets,
    producer_comparisons: producerComparisons, producer_failures: producerFailures,
    complete_comparison_counts: comparisonCounts, recurrence_rows: recurrenceRows, first_violation_subtractions: subtractionTerms,
    completed_boxes: boxesReport, completed_subtree_ledger: ledger}, null, 2) + '\n');
  process.exitCode = 1;
}
