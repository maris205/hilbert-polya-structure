// Independent documentary metadata audit only. Does not load Python or run children.
// Reads exact scoped files and emits JSON to stdout; never writes an input/output file.
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = '/root/autodl-tmp/symbolic_dynamics';
const prep = 'docs/papers211_215_sequence/qa/p211_round2_preparation01';
const owned = 'docs/papers211_215_sequence/qa/p211_round2_source_audit01';
const paper = 'papers/211-kernel-image-projection-feedback';
const bReview = 'docs/papers211_215_sequence/reviews/p211_b';
const pins = {};
const checks = [];
function abs(p) { return path.isAbsolute(p) ? p : path.join(root, p); }
function canonical(v) {
  if (Array.isArray(v)) return v.map(canonical);
  if (v && typeof v === 'object') return Object.fromEntries(Object.keys(v).sort().map(k => [k, canonical(v[k])]));
  return v;
}
function equal(a,b) { return JSON.stringify(canonical(a)) === JSON.stringify(canonical(b)); }
function check(name, actual, expected) {
  const ok = equal(actual, expected);
  checks.push({name, ok, actual, expected});
  if (!ok) throw Error('Documentary check failed: ' + name);
}
function read(p) {
  const full = abs(p), stat = fs.lstatSync(full);
  if (!stat.isFile() || stat.isSymbolicLink()) throw Error('Nonordinary scoped file: '+p);
  const data = fs.readFileSync(full);
  const pin = {bytes:data.length,sha256:crypto.createHash('sha256').update(data).digest('hex')};
  const key = full.startsWith(root+'/') ? full.slice(root.length+1) : full;
  if (pins[key] && !equal(pins[key], pin)) throw Error('Changed scoped input: '+p);
  pins[key] = pin;
  return data;
}
function json(p) { return JSON.parse(read(p).toString('utf8')); }
function pin(p) { read(p); return pins[abs(p).slice(root.length+1)]; }
function walk(p) {
  const files = [], directories = [];
  function visit(rel) {
    for (const ent of fs.readdirSync(abs(rel), {withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))) {
      const q = rel+'/'+ent.name;
      if (ent.isSymbolicLink()) throw Error('Symlink in scoped physical tree: '+q);
      if (ent.isDirectory()) { directories.push(q.slice(p.length+1)); visit(q); }
      else if (ent.isFile()) files.push(q.slice(p.length+1));
      else throw Error('Special entry: '+q);
    }
  }
  visit(p);
  return {files:files.sort(),directories:directories.sort()};
}
function manifest(p) {
  const result = {};
  for (const line of read(p).toString('utf8').trimEnd().split('\n')) {
    const m = /^([0-9a-f]{64})  (.+)$/.exec(line);
    if (!m || result[m[2]]) throw Error('Malformed/duplicate manifest line: '+p);
    result[m[2]] = m[1];
  }
  return result;
}
try {
  check('preparation seal bytes/hash', pin(prep+'/SHA256SUMS'), {bytes:1998,sha256:'41a9e4a8203acee181b91e21e6985e521d43a1c303f7a697bfdb5d9306a60d21'});
  const prepSeal = manifest(prep+'/SHA256SUMS');
  const prepTree = walk(prep);
  check('preparation complete physical file inventory', prepTree.files, [...Object.keys(prepSeal),'SHA256SUMS'].sort());
  check('preparation physical subdirectories', prepTree.directories, ['terminal_build']);
  check('preparation payload count', Object.keys(prepSeal).length, 22);
  for (const [p,h] of Object.entries(prepSeal)) check('sealed preparation '+p, pin(prep+'/'+p).sha256, h);
  const inputScope = json(prep+'/INPUT_SCOPE.json');
  const stable = inputScope.original_stable_file_pins;
  check('stable input count', Object.keys(stable).length, 164);
  check('declared stable count', inputScope.pinned_file_count, 164);
  const inputManifest = manifest(prep+'/INPUT_PINS.sha256');
  check('input manifest complete keys', Object.keys(inputManifest).sort(), Object.keys(stable).sort());
  for (const [p,v] of Object.entries(stable)) {
    check('original stable bytes/hash '+p, pin(p), v);
    check('original stable manifest '+p, inputManifest[p], v.sha256);
  }
  const inv = json(prep+'/INTENDED_INVENTORY.json');
  const r1Seal = manifest(paper+'/frozen_round1/SHA256SUMS');
  const bSeal = manifest(bReview+'/SHA256SUMS');
  check('physical Round1 inventory', walk(paper+'/frozen_round1').files, [...Object.keys(r1Seal),'SHA256SUMS'].sort());
  check('physical whole final-B inventory', walk(bReview).files, [...Object.keys(bSeal),'SHA256SUMS'].sort());
  const expectedNames = [...Object.keys(r1Seal),...Object.keys(bSeal).map(x=>'review_b/'+x),'review_b/SHA256SUMS'].sort();
  check('intended destinations exact complete union', inv.rows.map(x=>x.destination).sort(), expectedNames);
  check('unique intended destination count', new Set(inv.rows.map(x=>x.destination)).size, 123);
  check('declared intended payload count', inv.payload_count, 123);
  check('declared total after outer seal', inv.total_file_count_with_future_outer_manifest, 124);
  const selection = json('docs/papers211_215_sequence/qa/p211_round1_execution01/SOURCE_SELECTION.json');
  const groups = {};
  for (const row of inv.rows) {
    const isB = row.destination.startsWith('review_b/');
    const expectedSource = isB ? bReview+'/'+row.destination.slice(9) : paper+'/frozen_round1/'+row.destination;
    check('intended physical source '+row.destination, row.source, expectedSource);
    check('intended actual byte pin '+row.destination, pin(row.source), row.pin);
    check('intended historical origin '+row.destination, row.original_document, isB ? row.source : selection[row.destination].original_document);
    check('intended source seal '+row.destination, row.pin.sha256, isB ? (row.destination==='review_b/SHA256SUMS'?pin(bReview+'/SHA256SUMS').sha256:bSeal[row.destination.slice(9)]) : r1Seal[row.destination]);
    if (!groups[row.role]) groups[row.role] = {files:0,bytes:0};
    groups[row.role].files++; groups[row.role].bytes += row.pin.bytes;
  }
  check('Round1 unchanged count and bytes', groups.UNCHANGED_ROUND1_PAYLOAD, {files:83,bytes:4438548});
  const bGroups = Object.entries(groups).filter(([k])=>k!=='UNCHANGED_ROUND1_PAYLOAD').map(([,v])=>v);
  check('whole B count and bytes', bGroups.reduce((a,v)=>({files:a.files+v.files,bytes:a.bytes+v.bytes}),{files:0,bytes:0}), {files:40,bytes:6079604});
  check('actual payload bytes', inv.rows.reduce((n,r)=>n+r.pin.bytes,0), 10518152);
  check('declared payload bytes', inv.payload_bytes, 10518152);
  const nine = json(prep+'/NINE_BUILD_SOURCES.json');
  const binding0 = json('docs/papers211_215_sequence/qa/p211_initial_build_binding01/BINDING.json');
  const lock = json('docs/papers211_215_sequence/qa/p211_initial_build_binding01/ROOT_DERIVED_SOURCE_LOCK.json');
  const freeze = json(prep+'/BINDING.pending.json');
  const b1 = json(prep+'/terminal_build/BINDING_1.pending.json');
  const b2 = json(prep+'/terminal_build/BINDING_2.pending.json');
  check('exact nine selected sources', Object.keys(nine.sources).length, 9);
  check('nine total bytes', Object.values(nine.sources).reduce((n,v)=>n+v.bytes,0), 20508);
  for (const [p,v] of Object.entries(nine.sources)) {
    check('nine live bytes '+p, pin(paper+'/'+p), v);
    check('nine Round1 bytes '+p, pin(paper+'/frozen_round1/'+p), v);
  }
  check('nine accepted initial binding pins', binding0.source_pins, nine.sources);
  check('nine prior lock source observations', lock.source_observations, nine.sources);
  check('build1 nine pins', b1.source_pins, nine.sources);
  check('build2 nine pins', b2.source_pins, nine.sources);
  check('all pending templates disabled', [freeze.enabled,b1.enabled,b2.enabled], [false,false,false]);
  check('all pending issuer/decision fields null', [freeze,b1,b2].map(x=>[x.root_authorization.issuer,x.root_authorization.decision]), [[null,null],[null,null],[null,null]]);
  const normalizedB2 = structuredClone(b2);
  normalizedB2.build_number=1;
  normalizedB2.output=b1.output;
  normalizedB2.root_authorization.build_number=1;
  check('two terminal templates differ only number/output/authorization number', normalizedB2, b1);
  const lineage = json(prep+'/INFRASTRUCTURE_LINEAGE.json');
  for (const key of ['original_freeze','original_freeze_reception','original_build_binding','original_build_lock','current_final_b_reception']) check('lineage '+key, pin(lineage[key].path), lineage[key].pin);
  for (const [p,v] of Object.entries(lineage.original_build_sources)) check('lineage original code '+p, pin(p), v);
  check('old lock exact bytes/hash', pin(lineage.original_build_lock.path), {bytes:570037,sha256:'1a879caa4d7bb68fd841e381f37d5ec3e31236ccd6c7b677dbd95492a92bbf87'});
  const census = {};
  for (const [role,entry] of Object.entries(freeze.inherited_input_keys)) {
    check('original full inherited key pin '+role, pin(entry.reference.path), entry.reference.pin);
    const rows = json(entry.reference.path);
    const v = {entries:0,workspace:0,host:0};
    for (const [key,row] of Object.entries(rows)) {
      const p = entry.entry_layout==='WRAPPED_EXTERNAL_PIN' ? row.pin : row;
      if (!Number.isInteger(p.bytes) || p.bytes<0 || !/^[0-9a-f]{64}$/.test(p.sha256)) throw Error('Malformed inherited pin '+key);
      const resolved = path.isAbsolute(key)?key:path.join(root,key);
      v.entries++; if (resolved.startsWith(root+'/')) v.workspace++; else v.host++;
    }
    census[role] = {...v,entry_layout:entry.entry_layout,scope:'ENTIRE_KEY_SCHEMA_ONLY; no host dereference or accepted-current-resolution claim'};
  }
  const closing = json(prep+'/NATIVE_CLOSING_METADATA.json');
  check('six original closing source records', closing.full_actual_final_source_reads.length, 6);
  const sourceComparisons=[];
  for (const rec of closing.full_actual_final_source_reads) {
    const m = /^sed -n '1,2000p' '([^']+)'$/.exec(rec.request.cmd);
    if (!m) throw Error('Unexpected native source read request');
    check('original source stdout exact current bytes '+m[1], Buffer.from(rec.result.output).equals(read(m[1])), true);
    sourceComparisons.push({path:m[1],bytes:Buffer.byteLength(rec.result.output),exit_code:rec.result.exit_code});
  }
  const originals=json(prep+'/NATIVE_SOURCE_DIFFS.json');
  const ours=json(owned+'/NATIVE_DIFFS.json');
  check('six retained exact full diffs', originals.records.length,6);
  check('six independent exact full diffs', ours.complete_records.length,6);
  for(let i=0;i<6;i++) {
    check('independent vs preparation complete diff stdout '+i, ours.complete_records[i].result.output, originals.records[i].result.output);
    check('independent native diff expected exit1 '+i, ours.complete_records[i].result.exit_code,1);
  }
  const absence = {};
  for(const p of [paper+'/frozen_round2',paper+'/qa_final','docs/papers211_215_sequence/qa/p211_round2_execution01']) {
    try { fs.lstatSync(abs(p)); absence[p]='PRESENT'; } catch(e) { if(e.code!=='ENOENT')throw e; absence[p]='ABSENT'; }
    check('future output remains absent '+p, absence[p], 'ABSENT');
  }
  const compactChecks=checks.map(({name,ok,actual})=>({name,ok,...(name.startsWith('independent vs preparation complete diff')?{comparison:'EXACT_FULL_STDOUT_BYTES'}:(typeof actual!=='object'||actual===null?{actual}:{}))}));
  console.log(JSON.stringify({schema:'p211-round2-independent-documentary-check-v1',status:'METADATA_CHECKS_PASS_NOT_OPERATIONAL_AUTHORIZATION',checks:compactChecks,check_count:checks.length,groups,inherited_complete_key_schema_census:census,sourceComparisons,absence,actual_scoped_input_pins:pins,operational_programs_invoked:0,host_entries_dereferenced:0,scientific_contents_interpreted:false},null,2));
} catch(e) {
  console.log(JSON.stringify({schema:'p211-round2-independent-documentary-check-v1',status:'DOCUMENTARY_CHECK_FAILED',error:e.message,checks,actual_scoped_input_pins:pins,operational_programs_invoked:0},null,2));
  process.exitCode=1;
}
