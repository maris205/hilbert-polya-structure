'use strict';
// Workspace bytes/metadata only. Never load, compile or execute proposed Python.
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const assert = require('assert').strict;
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = ROOT + '/docs/papers211_215_sequence/qa';
const BASE = QA + '/p212_author_pair_controller_preparation01';
const ADOPTION = QA + '/p212_canonical_adoption_preparation01';
let checks = 0;
function eq(a, b) { checks++; assert.deepEqual(a, b); }
function need(a) { checks++; assert(a); }
function sha(data) { return crypto.createHash('sha256').update(data).digest('hex'); }
function safe(p) {
  need(path.isAbsolute(p) && path.normalize(p) === p && p.startsWith(ROOT + '/'));
  for (let cursor = p; cursor.startsWith(ROOT); cursor = path.dirname(cursor)) {
    need(!fs.lstatSync(cursor).isSymbolicLink());
    if (cursor === ROOT) break;
  }
  eq(fs.realpathSync(p), p);
}
function read(p) { safe(p); need(fs.statSync(p).isFile()); return fs.readFileSync(p); }
function pin(p) { const d = read(p); return {bytes: d.length, sha256: sha(d), resolved: p, symlink: null}; }
function json(p) { return JSON.parse(read(p)); }
function absent(p) {
  need(p.startsWith(ROOT + '/'));
  try { fs.lstatSync(p); throw Error('unexpected existing output'); }
  catch (error) { eq(error.code, 'ENOENT'); }
}
function tree(base) {
  safe(base);
  const files = {}, directories = [];
  function visit(dir) {
    for (const n of fs.readdirSync(dir).sort()) {
      const p = dir + '/' + n, r = path.relative(base, p);
      need(!fs.lstatSync(p).isSymbolicLink());
      if (fs.statSync(p).isDirectory()) { directories.push(r); visit(p); }
      else files[r] = pin(p);
    }
  }
  visit(base); return {files, directories: directories.sort()};
}
const inventoryPath = ADOPTION + '/WORKSPACE_INPUTS.json';
eq(pin(inventoryPath), {bytes:148177, sha256:'9ed644f2f5b6dea4be8af585c9657121914968e1b44cedb76340991b28b32cb1', resolved:inventoryPath, symlink:null});
const inventory = json(inventoryPath);
eq(inventory.schema, 'p212-adoption-workspace-inputs-v1');
eq(inventory.host_paths_dereferenced, 0);
let fileCount = 0, originalBytes = 0;
for (const [base, expected] of Object.entries(inventory.trees)) {
  eq(tree(base), expected);
  fileCount += Object.keys(expected.files).length;
  originalBytes += Object.values(expected.files).reduce((s, p) => s + p.bytes, 0);
}
for (const [p, expected] of Object.entries(inventory.files)) { eq(pin(p), expected); fileCount++; originalBytes += expected.bytes; }
eq(fileCount, 416); eq(Object.keys(inventory.trees).length, 11); eq(originalBytes, 20149659);
for (const p of inventory.absent) absent(p);
const adoptionTree = tree(ADOPTION), manifest = read(ADOPTION + '/SHA256SUMS');
eq({bytes:manifest.length, sha256:sha(manifest)}, {bytes:1286, sha256:'3fcc2ed22fe40a6d25a634bc6fd9fdb8b7d6ad654ca75dcc2880d7683a531ebd'});
const manifestRows = {};
need(manifest.toString().endsWith('\n'));
for (const line of manifest.toString().slice(0, -1).split('\n')) {
  const m = /^([a-f0-9]{64})  ([A-Za-z0-9_.]+)$/.exec(line);
  need(m && !(m[2] in manifestRows) && m[2] !== 'SHA256SUMS');
  manifestRows[m[2]] = m[1];
  eq(adoptionTree.files[m[2]].sha256, m[1]);
}
eq(Object.keys(manifestRows).length, 15);
eq(Object.keys(adoptionTree.files).sort(), Object.keys(manifestRows).concat(['SHA256SUMS']).sort());
eq(adoptionTree.directories, []);
const original = QA + '/p212_author_initial_binding01/run.py';
const originalBytesRaw = read(original), proposedBytes = read(BASE + '/run.py');
eq(sha(originalBytesRaw), '69d92dcead9cfd2bd9a5b0ee8da0ddb3d86ee43b18501b470bea5c710c0ee007');
const deltas = json(BASE + '/LITERAL_DELTAS.json').ordered_unique_replacements;
eq(deltas.length, 13);
let transformed = originalBytesRaw.toString();
for (const row of deltas) { eq(transformed.split(row.before).length, 2); transformed = transformed.replace(row.before, row.after); }
eq(Buffer.from(transformed), proposedBytes);
const oldPair = read(QA + '/p212_runtime_preparation01/PAIR.pending.json');
eq(read(BASE + '/PAIR.pending.json'), oldPair);
const pair = JSON.parse(oldPair), controller = json(BASE + '/CONTROLLER.disabled.json');
eq(pair.approved, false); eq(pair.mode, 'pair'); eq(pair.attempt, null);
eq(pair.runtime_lock, {path:null, sha256:null, bytes:null});
eq(pair.canonical.sha256, null); eq(pair.canonical.bytes, null);
eq(Object.values(pair.timeouts), [null, null, null]); eq(pair.provenance_inputs, []);
eq(controller.approved, false); eq(controller.independent_review, false);
for (const key of ['operational_controller_pin', 'authority', 'canonical', 'runtime_lock']) eq(controller[key], null);
eq(controller.provenance_inputs, []); eq(controller.expected_canonical_after_root_adoption.observed_canonical, false);
absent(QA + '/p212_author_pair_binding01'); absent(QA + '/root_replays/p212_author_pair_01');
const diff = json(BASE + '/SOURCE_DIFF.native.json');
eq(diff[0].result.exit_code, 1); eq(diff[0].result.output, read(BASE + '/SOURCE_DIFF.patch').toString());
eq(diff[1].result.exit_code, 0); eq(diff[1].result.output, '');
const reads = json(BASE + '/ORIGINAL_READS_NATIVE.json').reads;
const selected_original_pins = {};
for (const row of reads) {
  const p = ROOT + '/' + row.path;
  eq(row.result.exit_code, 0); eq(Buffer.from(row.result.output), read(p));
  selected_original_pins[p] = pin(p);
}
const prepared_files = {};
for (const n of ['run.py','PAIR.pending.json','CONTROLLER.disabled.json','LITERAL_DELTAS.json','PLAN.md','SOURCE_DIFF.patch','SOURCE_DIFF.native.json','ORIGINAL_READS_NATIVE.json','inspect_preparation.js']) prepared_files[n] = pin(BASE + '/' + n);
process.stdout.write(JSON.stringify({status:'PASS_SOURCE_ONLY_P212_PAIR_CONTROLLER_PREPARATION', checks, original_workspace_inventory:{path:inventoryPath, ...pin(inventoryPath)}, preserved_original_file_count:fileCount, preserved_original_bytes:originalBytes, preserved_exact_tree_roots:Object.keys(inventory.trees), selected_original_pins, adoption_preparation_exact_tree:adoptionTree, prepared_files, literal_deltas:deltas.length, actual_diff_exit:1, actual_template_cmp_exit:0, canonical_absent:true, alias_absent:true, proposed_binding_and_attempt_absent:true, helper_executions:0, host_paths_dereferenced:0, scientific_producer_invocations:0, authority_created:false, independent_review:false}, null, 2) + '\n');
