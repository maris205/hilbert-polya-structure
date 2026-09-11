'use strict';
// Documentary metadata only. Never require submitted code or follow host keys.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const assert = require('assert').strict;
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = ROOT + '/docs/papers211_215_sequence/qa';
const PAPER = ROOT + '/papers/212-closed-pointer-orbits';
const PREP = QA + '/p212_canonical_adoption_preparation01';
const names = ['p212_saved_output_root_reception01', 'p212_author_initial_runtime_reception01', 'root_replays/p212_author_initial_01', 'p212_author_initial_binding01', 'p212_runtime_preparation01', 'p212_runtime_discovery01', 'p212_runtime_source_root_reception01', 'p212_runtime_discovery_root_reception01', 'p212_saved_output_semantic_preparation01', 'p212_author_source_reception'];
let count = 0;
function check(value, label) { count++; assert(value, label); }
function inside(p) { check(path.isAbsolute(p) && path.normalize(p) === p && p.startsWith(ROOT + '/'), 'workspace path'); }
function sha(data) { return crypto.createHash('sha256').update(data).digest('hex'); }
function safe(p) {
  inside(p);
  for (let cursor = p; cursor.startsWith(ROOT); cursor = path.dirname(cursor)) {
    check(!fs.lstatSync(cursor).isSymbolicLink(), 'no workspace symlink');
    if (cursor === ROOT) break;
  }
  check(fs.realpathSync(p) === p, 'no resolved alias');
}
function pin(p) { safe(p); check(fs.statSync(p).isFile(), 'regular input'); const data = fs.readFileSync(p); return {bytes: data.length, sha256: sha(data), resolved: p, symlink: null}; }
function tree(base) {
  safe(base);
  const files = {}, directories = [];
  function visit(dir) {
    for (const name of fs.readdirSync(dir).sort()) {
      const p = dir + '/' + name, relative = path.relative(base, p);
      check(!fs.lstatSync(p).isSymbolicLink(), 'tree no symlink');
      if (fs.statSync(p).isDirectory()) { directories.push(relative); visit(p); }
      else files[relative] = pin(p);
    }
  }
  visit(base); return {files, directories: directories.sort()};
}
const trees = Object.fromEntries([...names.map(n => QA + '/' + n), PAPER].map(p => [p, tree(p)]));
const files = {[QA + '/p211_b_initial_binding/adopt_initial_output.py']: pin(QA + '/p211_b_initial_binding/adopt_initial_output.py')};
const absent = [PAPER + '/CANONICAL.json', PAPER + '/canonical.stdout.json'];
for (const p of absent) { inside(p); check(!fs.existsSync(p), 'canonical absent'); try { fs.lstatSync(p); throw Error('lexists'); } catch (error) { check(error.code === 'ENOENT', 'canonical absent not symlink'); } }
function seal(base, sealName, expectedCount) {
  const inventory = tree(base).files;
  const raw = fs.readFileSync(base + '/' + sealName, 'utf8');
  check(raw.endsWith('\n'), 'seal newline');
  const records = {};
  for (const line of raw.slice(0, -1).split('\n')) {
    const match = /^([0-9a-f]{64})  (.+)$/.exec(line); check(Boolean(match), 'seal line');
    const relative = match[2];
    check(!path.isAbsolute(relative) && path.normalize(relative) === relative && !relative.startsWith('../') && relative !== sealName && !(relative in records), 'seal normalized nonself unique');
    records[relative] = match[1];
    check(inventory[relative] && inventory[relative].sha256 === match[1], 'seal full payload bytes');
  }
  check(Object.keys(records).length === expectedCount, 'expected payload count');
  assert.deepEqual(Object.keys(records).sort(), Object.keys(inventory).filter(n => n !== sealName).sort()); count++;
  return expectedCount;
}
const sealed_payloads = {
  semantic: seal(QA + '/p212_saved_output_root_reception01', 'SHA256SUMS', 92),
  runtime: seal(QA + '/p212_author_initial_runtime_reception01', 'SHA256SUMS', 14),
  production: seal(QA + '/root_replays/p212_author_initial_01', 'SHA256SUMS', 77),
  initial_controller: seal(QA + '/p212_author_initial_binding01/entry01', 'SHA256SUMS', 9),
  semantic_failed_attempt: seal(QA + '/p212_saved_output_root_reception01/initial01', 'SHA256SUMS', 21),
  semantic_actual_attempt: seal(QA + '/p212_saved_output_root_reception01/initial02', 'SHA256SUMS', 21),
  runtime_preparation: seal(QA + '/p212_runtime_preparation01', 'SHA256SUMS', 15),
  discovery: seal(QA + '/p212_runtime_discovery01', 'SHA256SUMS', 58),
  semantic_preparation: seal(QA + '/p212_saved_output_semantic_preparation01', 'MANIFEST.sha256', 5)
};
function json(p) { inside(p); return JSON.parse(fs.readFileSync(p, 'utf8')); }
function received(p) {
  const r = json(p), parts = [r.result];
  for (const item of r.polls || []) { check(item.request.session_id === parts.at(-1).session_id, 'actual poll chain'); parts.push(item.result); }
  check(parts.at(-1).exit_code === 0 && !parts.at(-1).session_id, 'actual native terminal zero');
  for (const r of parts.slice(0, -1)) check(r.exit_code === undefined && r.session_id, 'actual running state');
  return JSON.parse(parts.map(r => r.output).join(''));
}
const semantic = json(QA + '/p212_saved_output_root_reception01/EXECUTION_RECEPTION_RESULT.json');
const runtime = json(QA + '/p212_author_initial_runtime_reception01/RESULT.json');
assert.deepEqual(semantic, received(QA + '/p212_saved_output_root_reception01/EXECUTION_RECEPTION_NATIVE.json')); count++;
assert.deepEqual(runtime, received(QA + '/p212_author_initial_runtime_reception01/ROOT_NATIVE02.json')); count++;
const scientific = semantic.saved_scientific_stdout;
assert.deepEqual(runtime.raw_stdout, [scientific]); count++;
check(scientific.bytes === 12501943 && scientific.sha256 === '1a32be6bb36dd8b4b27b9891a42876fe235bf2555a3dd9f4e36195a6ad72676c', 'actual raw identity');
check(pin(scientific.path).sha256 === scientific.sha256, 'actual raw bytes');
const initial = json(QA + '/p212_author_initial_binding01/BINDING.json');
const semanticBinding = json(QA + '/p212_saved_output_root_reception01/BINDING.json');
assert.deepEqual(semanticBinding.saved_stdout, scientific); count++;
check(initial.approved === true && initial.mode === 'initial' && runtime.actual_author_invocations_received === 1, 'accepted sole initial');
check(semantic.status === 'PASS_ROOT_COMPLETE_P212_INITIAL_SAVED_OUTPUT_SEMANTICS' && semantic.canonical_adopted === false, 'semantic acceptance boundary');
const inventory = {schema: 'p212-adoption-workspace-inputs-v1', scope: 'Whole selected workspace trees and old adoption source; host lock paths are data only, not current host verification.', host_paths_dereferenced: 0, trees, files, absent, checks: {assertions: count, sealed_payloads, whole_semantic_native_equals_result: true, whole_runtime_native_equals_result: true, scientific_stdout: scientific, helper_not_executed: true, submitted_code_not_imported: true}};
process.stdout.write(JSON.stringify(inventory, null, 2) + '\n');
