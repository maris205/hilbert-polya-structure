'use strict';
// The sole executable in this preparation: workspace source/document metadata.
// Never require/compile/execute either proposed receiver or follow host records.
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const assert = require('assert').strict;
const ROOT = '/root/autodl-tmp/symbolic_dynamics', QA = ROOT + '/docs/papers211_215_sequence/qa';
const BASE = QA + '/p212_author_pair_receiver_preparation01';
const PAPER = ROOT + '/papers/212-closed-pointer-orbits';
const ADOPT = QA + '/p212_canonical_adoption_preparation01';
const CONTROLLER = QA + '/p212_author_pair_controller_preparation01';
const ACTUAL_ADOPTION = QA + '/p212_canonical_adoption_root01/adoption01';
let checks = 0;
function eq(x, y) { checks++; assert.deepEqual(x, y); }
function need(x) { checks++; assert(x); }
function sha(b) { return crypto.createHash('sha256').update(b).digest('hex'); }
function safe(p) {
  need(path.isAbsolute(p) && path.normalize(p) === p && p.startsWith(ROOT + '/'));
  for (let q = p; q.startsWith(ROOT); q = path.dirname(q)) { need(!fs.lstatSync(q).isSymbolicLink()); if (q === ROOT) break; }
  eq(fs.realpathSync(p), p);
}
function read(p) { safe(p); need(fs.statSync(p).isFile()); return fs.readFileSync(p); }
function pin(p) { const b = read(p); return {bytes:b.length, sha256:sha(b), resolved:p, symlink:null}; }
const obj = p => JSON.parse(read(p));
function tree(base) {
  safe(base);
  const files = {}, directories = [];
  function walk(p) {
    for (const n of fs.readdirSync(p).sort()) {
      const q = p + '/' + n, r = path.relative(base, q);
      need(!fs.lstatSync(q).isSymbolicLink());
      if (fs.statSync(q).isDirectory()) { directories.push(r); walk(q); }
      else files[r] = pin(q);
    }
  }
  walk(base); return {files, directories:directories.sort()};
}
const priorInventory = ADOPT + '/WORKSPACE_INPUTS.json';
const priorPin = pin(priorInventory);
eq(priorPin.bytes,148177); eq(priorPin.sha256,'9ed644f2f5b6dea4be8af585c9657121914968e1b44cedb76340991b28b32cb1');
const prior = obj(priorInventory);
const canonical = pin(PAPER + '/CANONICAL.json');
eq({bytes:canonical.bytes,sha256:canonical.sha256},{bytes:12501943,sha256:'1a32be6bb36dd8b4b27b9891a42876fe235bf2555a3dd9f4e36195a6ad72676c'});
let preservedFiles = 0, preservedBytes = 0;
for (const [base, expected] of Object.entries(prior.trees)) {
  const current = tree(base);
  if (base === PAPER) { eq(current.files['CANONICAL.json'],canonical); delete current.files['CANONICAL.json']; }
  eq(current, expected);
  preservedFiles += Object.keys(expected.files).length;
  preservedBytes += Object.values(expected.files).reduce((n,p) => n+p.bytes,0);
}
for (const [p,k] of Object.entries(prior.files)) { eq(pin(p),k); preservedFiles++; preservedBytes+=k.bytes; }
eq(preservedFiles,416); eq(preservedBytes,20149659); eq(Object.keys(prior.trees).length,11);
// Deliberately never execute or replay the old canonical-absence predicates.
try { fs.lstatSync(PAPER + '/canonical.stdout.json'); throw Error('unexpected alias'); } catch (e) { eq(e.code,'ENOENT'); }
function sealed(base, payloads, expectedSeal) {
  const t = tree(base), b = read(base + '/SHA256SUMS');
  if (expectedSeal) eq(sha(b),expectedSeal);
  need(b.toString().endsWith('\n'));
  const names = [];
  for (const line of b.toString().slice(0,-1).split('\n')) {
    const m = /^([a-f0-9]{64})  ([A-Za-z0-9_.]+)$/.exec(line);
    need(m && !names.includes(m[2]) && m[2] !== 'SHA256SUMS'); names.push(m[2]);
    eq(t.files[m[2]].sha256,m[1]);
  }
  eq(names.length,payloads); eq(Object.keys(t.files).sort(),names.concat(['SHA256SUMS']).sort()); eq(t.directories,[]);
  return t;
}
const sealedOriginals = {
  [ADOPT]:sealed(ADOPT,15,'3fcc2ed22fe40a6d25a634bc6fd9fdb8b7d6ad654ca75dcc2880d7683a531ebd'),
  [CONTROLLER]:sealed(CONTROLLER,13,'5287daf8dfad0ccbd9b5e3f9708cbd43b0fda72ca0a09aad6f5c758d1a9dfd95'),
  [ACTUAL_ADOPTION]:sealed(ACTUAL_ADOPTION,7,null)
};
const adoption = obj(ACTUAL_ADOPTION + '/RESULT.json'), cmp = obj(ACTUAL_ADOPTION + '/CMP_RECEIPT.json');
eq(adoption.target,PAPER + '/CANONICAL.json');eq(adoption.source,prior.checks.scientific_stdout.path);
eq(adoption.bytes,canonical.bytes);eq(adoption.sha256,canonical.sha256);
eq(adoption.producer_invocations,0);eq(adoption.strict_pair_completed,false);
eq(cmp.argv,['/usr/bin/cmp','--',adoption.source,adoption.target]);eq(cmp.exit_code,0);
eq(read(ACTUAL_ADOPTION+'/cmp.stdout.raw').length,0);eq(read(ACTUAL_ADOPTION+'/cmp.stderr.raw').length,0);
eq(read(adoption.source),read(adoption.target));
const originals = obj(BASE + '/ORIGINAL_READS_NATIVE.json'), selectedOriginalPins = {};
for (const r of [...originals.receiver_originals,...originals.runtime_interface_originals]) {
  const p = ROOT + '/' + r.path;eq(r.result.exit_code,0);eq(Buffer.from(r.result.output),read(p));selectedOriginalPins[p]=pin(p);
}
const deltas = obj(BASE + '/LITERAL_DELTAS.json');
eq(deltas.python.ordered_replacements.length,17);eq(deltas.javascript.ordered_replacements.length,19);
for (const record of [deltas.python,deltas.javascript]) {
  let transformed = read(ROOT + '/' + record.source).toString();
  for (const d of record.ordered_replacements) { eq(transformed.split(d.before).length-1,d.count||1);transformed=transformed.split(d.before).join(d.after); }
  eq(Buffer.from(transformed),read(BASE + '/' + record.target));
}
const diffs = obj(BASE + '/DIFF_NATIVE.json');
for (let i=0;i<2;i++) { eq(diffs[i].result.exit_code,1);eq(diffs[i].result.output,read(BASE + '/' + ['inspect_production.patch','supplement.patch'][i]).toString()); }
const disabled = obj(BASE + '/EXECUTION.disabled.json');
eq(disabled.approved,false);eq(disabled.authority,null);eq(disabled.independent_review,false);eq(disabled.canonical_semantic_reuse_accepted,false);
for (const k of ['future_receiver_result','future_receiver_inputs','future_binding_result','future_binding_inputs','root_runtime_authority']) eq(disabled[k],null);
eq(disabled.proposed_deployment.python_pin,null);eq(disabled.proposed_deployment.javascript_pin,null);
for (const k of ['future_binding','future_product_capture','future_receiver_capture']) eq(disabled[k].pin,null);
eq(disabled.future_attempt.manifest_pin,null);
eq(disabled.source_contract,{mode:'pair',stages:['outer','launcher','recorder','child01','child02'],recorder_commands:9,adapter_native_commands:11,scientific_producer_records:2,scientific_raw_cmp_records:3,separate_root_capture_commands:1});
const savedMetadata = {};
for (const p of [QA+'/p212_author_initial_runtime_reception01/INPUTS_CURRENT.json',QA+'/p212_author_initial_runtime_reception01/SUPPLEMENT_INPUTS.json',QA+'/p212_runtime_discovery01/RUNTIME_LOCK.json']) savedMetadata[p]=pin(p);
const prepared = {};
for (const n of ['inspect_production.py','supplement.js','LITERAL_DELTAS.json','ORIGINAL_READS_NATIVE.json','DIFF_NATIVE.json','inspect_production.patch','supplement.patch','PLAN.md','EXECUTION.disabled.json','inspect_source_metadata.js']) prepared[n]=pin(BASE+'/'+n);
const result = {status:'SOURCE_ONLY_PAIR_RECEIVER_METADATA_VALID',checks,historical_inventory:{path:priorInventory,...priorPin},preserved_historical_files:preservedFiles,preserved_historical_bytes:preservedBytes,historical_trees:11,current_paper_tree_delta:['CANONICAL.json'],canonical_document:{path:PAPER+'/CANONICAL.json',...canonical},sealed_original_trees:sealedOriginals,selected_original_pins:selectedOriginalPins,saved_host_metadata_as_documents:savedMetadata,prepared_sources:prepared,python_literal_rules:17,javascript_literal_rules:19,native_diff_exit_codes:[1,1],future_pair_outputs_read:0,operational_source_executions:0,host_paths_dereferenced:0,mathematical_reevaluations:0,authority_created:false,independent_review:false};
process.stdout.write(JSON.stringify(result,null,2)+'\n');
