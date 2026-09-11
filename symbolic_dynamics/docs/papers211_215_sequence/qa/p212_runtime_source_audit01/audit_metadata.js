'use strict';
// Independent documentary inspection only. No submitted imports, AST,
// interpreter invocation, graph calculation, or file mutation.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const assert = require('assert/strict');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const PREP = ROOT + '/docs/papers211_215_sequence/qa/p212_runtime_preparation01';
const OWN = ROOT + '/docs/papers211_215_sequence/qa/p212_runtime_source_audit01';
const checks = [], inputKeys = {}, bindings = [], limitations = [];
function need(ok, label, detail = null) {
  checks.push({label, passed: Boolean(ok), detail});
  assert.ok(ok, label + ': ' + JSON.stringify(detail));
}
function sha(bytes) { return crypto.createHash('sha256').update(bytes).digest('hex'); }
function read(p) { return fs.readFileSync(p); }
function meta(p) {
  const bytes = read(p), st = fs.lstatSync(p, {bigint: true});
  return {bytes: bytes.length, sha256: sha(bytes), resolved: fs.realpathSync(p),
    regular: st.isFile(), symlink: st.isSymbolicLink(), nlink: Number(st.nlink),
    mode: Number(st.mode), size: Number(st.size), mtime_ns: st.mtimeNs.toString()};
}
function json(p) { return JSON.parse(read(p)); }
function same(a, b) { try { assert.deepStrictEqual(a, b); return true; } catch (_) { return false; } }
function rows(p) {
  const bytes = read(p), text = bytes.toString('utf8');
  need(text.endsWith('\n') && Buffer.from(text).equals(bytes), 'manifest UTF8 and final LF', p);
  const out = {};
  for (const line of text.slice(0, -1).split('\n')) {
    const m = /^([0-9a-f]{64})  (.+)$/.exec(line);
    need(m && !(m[2] in out), 'unique complete hash row', {p, line});
    out[m[2]] = m[1];
  }
  return out;
}
function digestBinding(label, output, expected) {
  const actual = {bytes: Buffer.byteLength(output), sha256: sha(Buffer.from(output))};
  need(actual.bytes === expected.bytes && actual.sha256 === expected.sha256,
    'complete archived output byte binding', {label, actual, expected});
  bindings.push({label, ...actual});
}
function reconstructDiff(oldPath, newPath, diff) {
  const original = read(oldPath).toString('utf8').split('\n');
  const wanted = read(newPath).toString('utf8').split('\n');
  need(original.pop() === '' && wanted.pop() === '', 'source final LF for documentary patch', newPath);
  const lines = diff.split('\n');
  need(lines.pop() === '' && lines[0].startsWith('--- ') && lines[1].startsWith('+++ '),
    'complete native unified headers', newPath);
  let cursor = 0, i = 2, built = [], hunks = 0;
  while (i < lines.length) {
    const h = /^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@.*$/.exec(lines[i++]);
    need(h !== null, 'actual unified hunk syntax', {newPath, i});
    const a = Number(h[1]), an = h[2] === undefined ? 1 : Number(h[2]);
    const b = Number(h[3]), bn = h[4] === undefined ? 1 : Number(h[4]);
    const start = an ? a - 1 : a;
    need(start >= cursor && start <= original.length, 'ordered hunk old position', newPath);
    built.push(...original.slice(cursor, start)); cursor = start;
    need(built.length === (bn ? b - 1 : b), 'hunk new position', newPath);
    let usedOld = 0, usedNew = 0;
    while (i < lines.length && !lines[i].startsWith('@@ ')) {
      const line = lines[i++], prefix = line[0], body = line.slice(1);
      need([' ', '-', '+'].includes(prefix), 'hunk body prefix', {newPath, i});
      if (prefix !== '+') {
        need(original[cursor++] === body, 'exact old source hunk body', {newPath, i}); usedOld++;
      }
      if (prefix !== '-') { built.push(body); usedNew++; }
    }
    need(usedOld === an && usedNew === bn, 'whole hunk counts', {newPath, usedOld, an, usedNew, bn});
    hunks++;
  }
  built.push(...original.slice(cursor));
  need(same(built, wanted), 'full old-to-new native patch reconstructs exact new source', newPath);
  return {oldPath, newPath, hunks, old_lines: original.length, new_lines: wanted.length};
}
const sealRows = rows(PREP + '/SHA256SUMS');
const members = fs.readdirSync(PREP).sort();
need(members.length === 16 && Object.keys(sealRows).length === 15, 'exact 15 payload / 16 file preparation');
need(same(members, [...Object.keys(sealRows), 'SHA256SUMS'].sort()), 'complete nonself membership');
for (const name of members) {
  need(path.basename(name) === name && name !== '.' && name !== '..', 'flat safe preparation name', name);
  const p = PREP + '/' + name, key = meta(p);
  need(key.regular && !key.symlink && key.nlink === 1 && key.resolved === p, 'physical single-link preparation input', name);
  if (name !== 'SHA256SUMS') need(key.sha256 === sealRows[name], 'sealed payload bytes', name);
  inputKeys[p] = key;
}
const selected = rows(PREP + '/INPUT_PINS.sha256');
need(Object.keys(selected).length === 19, 'nineteen selected input roles');
need(Object.keys(selected).filter(p => path.isAbsolute(p)).length === 2, 'exactly two absolute host-source roles');
for (const [name, digest] of Object.entries(selected)) {
  need(path.isAbsolute(name) ? ['/usr/lib/python3.10/fractions.py', '/usr/lib/python3.10/decimal.py'].includes(name) : !name.split('/').includes('..'),
    'preserve mixed manifest base', name);
  const p = path.isAbsolute(name) ? name : ROOT + '/' + name, key = meta(p);
  need(key.sha256 === digest, 'whole selected metadata pin', name); inputKeys[p] = key;
}
inputKeys[ROOT + '/docs/papers211_215_sequence/PROBLEM_ANCHOR.md'] = meta(ROOT + '/docs/papers211_215_sequence/PROBLEM_ANCHOR.md');
const original = json(PREP + '/ORIGINAL_NATIVE_READS.json');
const closing = json(PREP + '/CLOSING_NATIVE.json');
need(original.records.length === 54 && closing.records.length === 18, 'actual 54 plus 18 record count');
const recordCensus = [];
for (const [group, records] of [['original', original.records], ['closing', closing.records]]) {
  const seen = new Set();
  for (const [i, r] of records.entries()) {
    need(same(Object.keys(r).sort(), ['request', 'result']), 'native request/result role', {group, i});
    need(typeof r.request.cmd === 'string' && r.request.workdir.startsWith(ROOT) && Number.isInteger(r.request.max_output_tokens),
      'actual native request shape', {group, i});
    need(typeof r.result.output === 'string' && typeof r.result.chunk_id === 'string' && Number.isInteger(r.result.exit_code) &&
      Number.isFinite(r.result.wall_time_seconds) && !r.result.session_id && !seen.has(r.result.chunk_id),
      'completed native result shape', {group, i});
    seen.add(r.result.chunk_id);
    recordCensus.push({group, index: i, request: r.request, chunk_id: r.result.chunk_id,
      exit_code: r.result.exit_code, output_bytes: Buffer.byteLength(r.result.output), output_sha256: sha(Buffer.from(r.result.output))});
  }
}
const byId = new Map([...original.records, ...closing.records].map(r => [r.result.chunk_id, r]));
const fullGroups = [
  ['new core', ['7f2b14'], PREP + '/runtime_core.py'],
  ['new adapter', ['957b55', 'b3282f'], PREP + '/p212_runtime.py'],
  ['new preparer first', ['e1b915'], PREP + '/prepare_runtime.py'],
  ['new preparer repeated', ['47f87f'], PREP + '/prepare_runtime.py'],
  ['old core', ['acd1ca'], ROOT + '/docs/papers211_215_sequence/qa/p211_runtime_preparation/runtime_core.py'],
  ['old adapter', ['188d74', '33f50f'], ROOT + '/docs/papers211_215_sequence/qa/p211_runtime_preparation/p211_runtime.py'],
  ['old preparer', ['a53760'], ROOT + '/docs/papers211_215_sequence/qa/p211_runtime_preparation/prepare_runtime.py'],
  // Hash binding only: never display, parse, execute or review scientific bodies.
  ['scientific source archived three slices HASH ONLY', ['1c05fa', 'ad048f', '9de099'], ROOT + '/papers/212-closed-pointer-orbits/verify.py'],
  ['schema archived two slices HASH ONLY', ['005912', '48545f'], ROOT + '/papers/212-closed-pointer-orbits/OUTPUT_SCHEMA.md'],
  ['output plan HASH ONLY', ['6ec634'], ROOT + '/papers/212-closed-pointer-orbits/OUTPUT_PLAN.md'],
  ['output plan repeated HASH ONLY', ['594069'], ROOT + '/papers/212-closed-pointer-orbits/OUTPUT_PLAN.md']
];
for (const [label, ids, p] of fullGroups) digestBinding(label, ids.map(id => byId.get(id).result.output).join(''), inputKeys[p]);
const consumed = new Set(fullGroups.flatMap(x => x[1]));
for (const r of [...original.records, ...closing.records]) {
  const id = r.result.chunk_id;
  if (consumed.has(id) || r.result.exit_code !== 0 || id === 'bad337') continue;
  const m = /^sed -n '(\d+),(\d+)p' '?([^']+?)'?$/.exec(r.request.cmd);
  if (!m) continue;
  const p = path.isAbsolute(m[3]) ? m[3] : ROOT + '/' + m[3];
  if (!(p in inputKeys)) { limitations.push({chunk_id: id, reason: 'mutable navigation or unselected source; archived shape only'}); continue; }
  // Only source-range binding, not semantic interpretation. Pin was checked above.
  const bytes = read(p), lines = bytes.toString('utf8').match(/[^\n]*\n|[^\n]+$/g) || [];
  const slice = lines.slice(Number(m[1]) - 1, Number(m[2])).join('');
  digestBinding(id, r.result.output, {bytes: Buffer.byteLength(slice), sha256: sha(Buffer.from(slice))});
}
const diffs = json(OWN + '/NATIVE_DIFFS.json');
inputKeys[OWN + '/NATIVE_DIFFS.json'] = meta(OWN + '/NATIVE_DIFFS.json');
const diffIds = ['d9586b', '95e6b4', 'f40175'];
const patchResults = [];
for (let i = 0; i < 3; i++) {
  const old = byId.get(diffIds[i]), fresh = diffs.records[i];
  need(fresh.result.exit_code === 1 && fresh.result.output === old.result.output && fresh.request.cmd === old.request.cmd,
    'fresh complete actual diff equals archived whole native diff', diffIds[i]);
  const m = /^diff -u -- (\S+) (\S+)$/.exec(old.request.cmd);
  patchResults.push(reconstructDiff(ROOT + '/' + m[1], ROOT + '/' + m[2], fresh.result.output));
}
const oldCore = read(ROOT + '/docs/papers211_215_sequence/qa/p211_runtime_preparation/runtime_core.py').toString('utf8').split('\n');
const newCore = read(PREP + '/runtime_core.py').toString('utf8').split('\n');
need(oldCore[0] === newCore[0] && oldCore.slice(6).join('\n').replaceAll('P211_OWNED_NATIVE_RUNNING', 'P212_OWNED_NATIVE_RUNNING') === newCore.slice(6).join('\n'),
  'whole core outside truthful header and heartbeat is text-identical');
const discovery = json(PREP + '/DISCOVERY.pending.json'), initial = json(PREP + '/INITIAL.pending.json');
const pair = json(PREP + '/PAIR.pending.json'), iface = json(PREP + '/INTERFACE.json');
need([discovery, initial, pair].every(x => x.approved === false && x.provenance_inputs.length === 0), 'all three templates disabled without authority');
need(discovery.reviewed_all_preparation_sources === false && discovery.native_timeout_seconds === null, 'discovery remains pending');
const imports = ['itertools', 'json', 'math', 'sys', 'fractions'];
need([discovery, initial, pair, iface].every(x => same(x.declared_imports, imports)), 'same exact declared five imports');
need(same(discovery.source_inputs, iface.source_files) && same(discovery.lineage_inputs, iface.original_infrastructure_inputs), 'template/interface source and lineage identity');
for (const key of ['source_inputs', 'lineage_inputs']) for (const [p, pin] of Object.entries(discovery[key])) {
  need(same(pin, {bytes: inputKeys[p].bytes, sha256: inputKeys[p].sha256}), 'actual entire proposed source pin', p);
}
need(Object.keys(discovery.source_inputs).length === 3 && Object.keys(discovery.lineage_inputs).length === 3, 'exact 3 source plus 3 lineage roles');
need(same(initial.schema, pair.schema) && initial.mode === 'initial' && pair.mode === 'pair', 'distinct mode same entire schema');
const parameters = json(ROOT + '/papers/212-closed-pointer-orbits/PARAMETERS.json');
need(Object.keys(parameters).length === 14 && same(parameters, initial.schema.equalities.find(x => same(x.path, ['parameters'])).value), 'entire received parameter object only');
need(same(parameters.carrier_sizes, [1,2,3,4]) && same(parameters.unobserved_core_first_sizes, [5,6,5]), 'fixed interface coverage metadata');
for (const x of [initial, pair]) {
  need(x.attempt === null && Object.values(x.timeouts).every(v => v === null) && Object.values(x.runtime_lock).every(v => v === null), 'runtime role keys unresolved');
  need(x.reviewed_static_source_import_closure === false && x.reviewed_schema_and_parameters === false && x.reviewed_compile_exec_interface === false && x.complete_semantic_reception_is_separate === true,
    'no science authority; separate semantic reception');
  need(same(x.capsule_files, iface.scientific_input_interface) && same(x.argv_template, ['$ENTRY','--parameters','$PARAMETERS']) && x.parameters === 'PARAMETERS.json', 'exact capsule/interface argv metadata');
  need(same(x.schema.top_keys, iface.required_top_keys) && x.schema.top_keys.length === 12, 'twelve output role keys');
  need(x.canonical.path === iface.canonical_role && x.canonical.sha256 === null && x.canonical.bytes === null, 'canonical pending role');
}
const priorInterface = JSON.parse(byId.get('bad337').result.output);
priorInterface.proposed_scientific_entry = priorInterface.actual_scientific_entry; delete priorInterface.actual_scientific_entry;
priorInterface.fresh_runtime_program_invocations = priorInterface.fresh_native_execution_count; delete priorInterface.fresh_native_execution_count;
need(same(priorInterface, iface), 'exact two declared unsealed interface key renames only');
const expectedHashList = read(PREP + '/INPUT_PINS.sha256').toString('utf8');
need(byId.get('b360c1').result.output === expectedHashList, 'actual original hash stdout equals complete mixed input list');
const okList = Object.keys(selected).map(p => p + ': OK\n').join('');
need(['5f1fc1','7b1bce'].every(id => byId.get(id).result.output === okList && byId.get(id).result.exit_code === 0), 'both archived nineteen-pin native check outputs complete');
const sourceHashList = Object.keys(discovery.source_inputs).map(p => discovery.source_inputs[p].sha256 + '  ' + p + '\n').join('');
need(byId.get('37e7c7').result.output === sourceHashList, 'closing actual source-hash native output bound');
const links = [];
for (const name of ['PLAN.md','INFRASTRUCTURE_LINEAGE.md','BINDING_CONTRACT.md','READ_SCOPE.md','HANDOFF.md']) {
  for (const m of read(PREP + '/' + name).toString('utf8').matchAll(/\[[^\]]+\]\(([^)]+)\)/g)) {
    need(!/^https?:/.test(m[1]), 'local documentary link scope', m[1]);
    const resolved = path.resolve(PREP, m[1]);
    need(fs.existsSync(resolved), 'local link exists metadata only', resolved);
    links.push({document: name, literal: m[1], resolved});
  }
}
need(same(links, closing.local_markdown_links), 'all actual ordered preparation link metadata');
const absent = [discovery.output, iface.canonical_role, iface.historical_name_must_stay_absent, PREP + '/RUNTIME_LOCK.json'];
for (const p of absent) { let missing = false; try { fs.lstatSync(p); } catch (e) { if (e.code === 'ENOENT') missing = true; else throw e; } need(missing, 'prospective output still absent', p); }
for (const [p, key] of Object.entries(inputKeys)) need(same(meta(p), key), 'entire selected documentary input key unchanged', p);
process.stdout.write(JSON.stringify({format:'p212-independent-runtime-source-documentary-check-v1',status:'PASS_DOCUMENTARY_METADATA_ONLY',
  checks:checks.length, preparation_payloads:15, preparation_total_files:16,
  preparation_total_bytes:members.reduce((n,k)=>n+inputKeys[PREP+'/'+k].bytes,0),
  selected_input_roles:19,selected_host_source_roles:2, input_key_count:Object.keys(inputKeys).length,
  original_native_records:54,closing_native_records:18,complete_archived_output_bindings:bindings,
  native_diff_reconstructions:patchResults,ordered_local_links:links.length,record_census:recordCensus,
  input_keys:inputKeys,limitations,
  scope:'Source/document/parameter and hash metadata only. Scientific source/schema/output plan archived bodies receive only opaque complete digest binding; no scientific interpretation or submitted execution. Mutable navigation and exploratory inventories are archived record shapes, not live-byte claims. Not runtime, syntax, science, manuscript or operational acceptance.'},null,2)+'\n');
