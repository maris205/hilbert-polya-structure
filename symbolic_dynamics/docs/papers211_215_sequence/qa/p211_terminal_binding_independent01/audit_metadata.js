// Independent data-only audit; no submitted source execution or lock output.
'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const util = require('node:util');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = 'docs/papers211_215_sequence/qa/';
const BASE = QA + 'p211_terminal_binding_preparation01';
const PRIOR = QA + 'p211_round2_preparation01';
const PAPER = 'papers/211-kernel-image-projection-feedback';
const R2 = PAPER + '/frozen_round2';
const REFRESH = QA + 'p211_round2_binding_root01/refresh02';
const reads = {}, snapshots = {}, labels = [], nativeRows = [];
function need(ok, label) { if (!ok) throw Error(label); labels.push(label); }
function equal(a, b, label) { need(util.isDeepStrictEqual(a, b), label); }
function pin(raw) { return {bytes:raw.length, sha256:crypto.createHash('sha256').update(raw).digest('hex')}; }
function relative(s) {
  need(typeof s === 'string' && s.length > 0 && !/[\\\x00\r\n\t]/.test(s)
    && !s.startsWith('/') && s.split('/').every(x => x && x !== '.' && x !== '..'), 'literal:' + s);
  return s;
}
function local(s) {
  if (s.startsWith(ROOT + '/')) return relative(s.slice(ROOT.length + 1));
  return relative(s);
}
function stat(name, type) {
  name = relative(name);
  let p = ROOT, result;
  for (const [i, n] of name.split('/').entries()) {
    p += '/' + n; result = fs.lstatSync(p, {bigint:true});
    need(!result.isSymbolicLink(), 'no-alias:' + p);
    if (i < name.split('/').length - 1) need(result.isDirectory(), 'ordinary-parent:' + p);
  }
  need(type === 'dir' ? result.isDirectory() : result.isFile(), 'ordinary-' + type + ':' + name);
  return result;
}
function stable(s) {
  return ['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'].map(k => String(s[k]));
}
function read(name, expected) {
  name = local(name); const before = stat(name, 'file');
  const raw = fs.readFileSync(ROOT + '/' + name); const after = stat(name, 'file');
  equal(stable(before), stable(after), 'stable-read:' + name);
  const p = pin(raw); need(BigInt(raw.length) === after.size, 'read-size:' + name);
  if (expected) equal(p, expected, 'expected-pin:' + name);
  if (reads[name]) { equal(p, reads[name], 'unchanged-pin:' + name); equal(stable(after), snapshots[name], 'unchanged-stat:' + name); }
  reads[name] = p; snapshots[name] = stable(after); return raw;
}
function parse(raw) {
  const s = Buffer.isBuffer(raw) ? raw.toString('utf8') : raw; let i = 0;
  function white() { while (/[\t\r\n ]/.test(s[i] || 'x')) i++; }
  function string() {
    const start = i++; while (i < s.length) {
      if (s[i] === '\\') { i += 2; continue; }
      if (s[i++] === '"') return JSON.parse(s.slice(start, i));
    } throw Error('unterminated JSON string');
  }
  function value() {
    white(); const c = s[i];
    if (c === '"') { string(); return; }
    if (c === '{') {
      i++; white(); const keys = new Set(); if (s[i] === '}') { i++; return; }
      while (true) {
        white(); if (s[i] !== '"') throw Error('JSON key'); const k = string();
        if (keys.has(k)) throw Error('duplicate JSON key:' + k); keys.add(k);
        white(); if (s[i++] !== ':') throw Error('JSON colon'); value(); white();
        const d = s[i++]; if (d === '}') return; if (d !== ',') throw Error('JSON object delimiter');
      }
    }
    if (c === '[') {
      i++; white(); if (s[i] === ']') { i++; return; }
      while (true) { value(); white(); const d = s[i++]; if (d === ']') return; if (d !== ',') throw Error('JSON array delimiter'); }
    }
    const m = /^(?:true|false|null|-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?)/.exec(s.slice(i));
    if (!m) throw Error('JSON primitive'); i += m[0].length;
  }
  value(); white(); if (i !== s.length) throw Error('JSON trailing bytes'); return JSON.parse(s);
}
function obj(name, expected) { return parse(read(name, expected)); }
function tree(base) {
  stat(base, 'dir'); const files = [], dirs = ['.'];
  function walk(rel) {
    const here = rel ? base + '/' + rel : base;
    for (const n of fs.readdirSync(ROOT + '/' + here).sort()) {
      const r = rel ? rel + '/' + n : n, full = base + '/' + r;
      relative(full); const s = fs.lstatSync(ROOT + '/' + full);
      need(!s.isSymbolicLink(), 'tree-no-alias:' + full);
      if (s.isDirectory()) { dirs.push(r); walk(r); }
      else { need(s.isFile(), 'tree-regular:' + full); files.push(r); }
    }
  }
  walk(''); return {files:files.sort(), dirs:dirs.sort()};
}
function seal(base) {
  const t = tree(base), raw = read(base + '/SHA256SUMS'), text = raw.toString('utf8');
  need(text.endsWith('\n'), 'manifest-newline:' + base);
  const names = [], pins = {};
  for (const line of text.slice(0,-1).split('\n')) {
    const m = /^([0-9a-f]{64})  (.+)$/.exec(line); need(!!m, 'manifest-line:' + base);
    const n = relative(m[2]); need(n !== 'SHA256SUMS' && !names.includes(n), 'nonself-unique:' + n);
    const p = pin(read(base + '/' + n)); equal(p.sha256,m[1],'manifest-hash:' + n); names.push(n); pins[n]=p;
  }
  equal(names, names.slice().sort(), 'canonical-manifest-order:' + base);
  equal(t.files, [...names,'SHA256SUMS'].sort(), 'complete-manifest-files:' + base);
  const wanted = new Set(['.']); for (const n of names) { const a=n.split('/'); a.pop(); while(a.length) {wanted.add(a.join('/'));a.pop();} }
  equal(t.dirs, [...wanted].sort(), 'complete-manifest-dirs:' + base);
  return {payloads:names.length,payload_bytes:Object.values(pins).reduce((s,p)=>s+p.bytes,0),pins,dirs:t.dirs,seal:pin(raw)};
}
function record(r, label, exit=0) {
  need(r && typeof r.request.cmd === 'string' && r.result, 'native-record:' + label);
  need(r.result.exit_code === exit && !r.result.session_id, 'native-completion:' + label);
  need(typeof r.result.output === 'string' && typeof r.result.chunk_id === 'string', 'native-output:' + label);
  need(!r.result.output.startsWith('Warning: truncated output'), 'native-untruncated:' + label);
  nativeRows.push({label,request:r.request,chunk_id:r.result.chunk_id,exit_code:r.result.exit_code,output_pin:pin(Buffer.from(r.result.output))});
}
function sedBinding(r,label) {
  record(r,label); const m = /^sed -n '(\d+),(\d+)p' ([^\s]+)$/.exec(r.request.cmd);
  need(!!m,'literal-sed:' + label); const raw = read(m[3]);
  const lines = raw.toString('utf8').match(/[^\n]*\n|[^\n]+$/g) || [];
  equal(Buffer.from(r.result.output), Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join('')), 'raw-sed-output:' + label);
}
function packets(o,label) {
  need(o && o.request && typeof o.request.cmd === 'string' && Array.isArray(o.polls), 'saved-packet-container:' + label);
  const pp = [o.result,...o.polls.map(x=>x.result||x)];
  for(let i=0;i<pp.length;i++) {
    need(typeof pp[i].output === 'string' && !pp[i].output.startsWith('Warning: truncated output'),'saved-complete-stream:' + label + ':' + i);
    if(i < pp.length-1) {
      need(Number.isInteger(pp[i].session_id) && pp[i].exit_code === undefined,'saved-running-session:' + label);
      equal(o.polls[i].request.session_id,pp[i].session_id,'saved-poll-session:' + label);
    }
  }
  need(pp.at(-1).exit_code === 0 && !pp.at(-1).session_id,'saved-final-completion:' + label);
  return pp;
}
const submitted = seal(BASE), originalSource = seal(PRIOR);
need(submitted.payloads === 11 && originalSource.payloads === 22,'exact-submitted-and-original-source-count');
const plan = obj(BASE+'/INPUT_PLAN.json'), recipe=obj(BASE+'/LOCK_DERIVATION_PLAN.json'), all=obj(BASE+'/ROUND2_ALL_FILE_PINS.json');
need(Object.keys(plan.input_pins).length === 166,'exact-166-plan-pins');
for(const [n,p] of Object.entries(plan.input_pins)) read(n,p);
const outer = seal(R2), aSeal=seal(R2+'/review_a'), bSeal=seal(R2+'/review_b');
equal(all,{...outer.pins,SHA256SUMS:outer.seal},'all-124-round2-pins');
need(Object.keys(all).length === 124 && outer.payloads === 123 && outer.payload_bytes === 10518152,'round2-exact-count-bytes');
equal(outer.dirs,plan.round2_directories,'round2-13-directories');
const old=obj(plan.original_lock.path,plan.original_lock.pin), initial=obj(plan.original_initial_binding.path,plan.original_initial_binding.pin);
const fields=Object.fromEntries(Object.entries(old).map(([k,v])=>[k,{type:Array.isArray(v)?'array':v===null?'null':typeof v,items:v && typeof v==='object'?Object.keys(v).length:null,semantic_serialization_pin:pin(Buffer.from(JSON.stringify(v)))}]));
equal(fields,recipe.original_top_level_fields,'all-15-original-field-semantic-fingerprints');
equal(Object.keys(old),plan.old_lock_fields,'exact-old-field-list'); need(Object.keys(old).length===15,'old-field-count');
const changed=['schema','status','code_observations','terminal_derivation'];
equal(recipe.changed_fields,changed,'recipe-four-fields'); equal(plan.allowed_lock_field_changes,changed,'plan-four-fields');
equal(recipe.retained_fields,Object.keys(old).filter(k=>!changed.includes(k)),'exact-twelve-retained-field-names');
equal(Object.keys(recipe.new_field_values),changed,'new-values-exact-field-list');
equal(recipe.new_field_values,{schema:'p211-terminal-bounded-dependency-lock-v1',status:'ROOT_BOUND_EXACT_INHERITED_HOST_KEY_NEW_ADAPTER_ONLY',code_observations:plan.new_adapter_pins,terminal_derivation:{original_lock:plan.original_lock,allowed_changes:changed,host_candidate_extension:false}},'exact-four-new-values');
// This is a transient object comparison, not serialization/writing of a derived lock.
const conceptual = {...old,...recipe.new_field_values};
equal(Object.keys(conceptual).filter(k=>!util.isDeepStrictEqual(old[k],conceptual[k])).sort(),changed.slice().sort(),'conceptual-exact-change-set');
for(const k of recipe.retained_fields) equal(conceptual[k],old[k],'retained-deep-equality:' + k);
equal(old.environment,plan.fixed_environment,'stored-environment-equality');
equal(plan.fixed_environment,{PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'},'literal-ENV8-only');
for(const [name,count] of [['entries',840],['selector_specs',840],['selection_reasons',840],['queries',16],['query_commands',16],['ldd_elf_inputs',33],['cwd_relative_absence_roles',3],['source_observations',9],['environment',8]]) need(Object.keys(old[name]).length===count,'complete-old-count:'+name);
equal(initial.adapter_pins,plan.original_adapter_pins,'initial-old-adapters'); equal(old.code_observations,plan.original_adapter_pins,'old-lock-adapters');
equal(initial.dependency_lock,plan.original_lock,'initial-full-old-lock-reference');
for(const [root,pins] of [[plan.new_adapter_root,plan.new_adapter_pins],[plan.original_adapter_root,plan.original_adapter_pins]]) {
  need(Object.keys(pins).length===5,'five-adapter-files:'+root); for(const [n,p] of Object.entries(pins)) read(root+'/'+n,p);
}
equal(plan.source_pins,initial.source_pins,'nine-initial-source-pins'); equal(plan.source_pins,old.source_observations,'nine-old-source-pins');
for(const [n,p] of Object.entries(plan.source_pins)) {read(PAPER+'/'+n,p);equal(all[n],p,'nine-frozen-source:'+n);}
need(Object.values(plan.source_pins).reduce((s,p)=>s+p.bytes,0)===20508,'nine-source-total-bytes');
const bindings=[];
for(const i of [1,2]) {
  const b=obj(BASE+'/BINDING_'+i+'.disabled.json'), o=obj(plan.disabled_original_templates[i]); bindings.push(b);
  equal(Object.keys(b),Object.keys(o),'binding-original-field-set:'+i);
  equal(Object.keys(o).filter(k=>!util.isDeepStrictEqual(o[k],b[k])).sort(),['status','adapter_pins','round2_package','_note'].sort(),'binding-only-four-preparation-edits:'+i);
  equal(b.round2_package,{...o.round2_package,all_file_pins:all},'binding-full-round2:'+i);
  need(b.enabled===false && b.dependency_lock===null && b.cwd_relative_configuration===null,'disabled-lock-and-cwd-null:'+i);
  equal(b.status,'SOURCE_ONLY_PHYSICAL_ROUND2_PINNED_PENDING_ACCEPTANCE_AND_SEPARATE_ROOT_BINDING','disabled-status:'+i);
  equal(b.root_authorization,{issuer:null,decision:null,build_number:i,record:null},'null-rootauthority:'+i);
  for(const r of plan.pending_root_receipts) equal(b.receipt_references[r],null,'pending-receipt:'+i+':'+r);
  for(const r of Object.values(b.receipt_references)) if(r!==null) read(r.path,r.pin);
  equal(b.adapter_pins,plan.new_adapter_pins,'binding-new-adapters:'+i); equal(b.original_adapter_pins,plan.original_adapter_pins,'binding-old-adapters:'+i);
  equal(b.environment,plan.fixed_environment,'binding-environment:'+i); equal(b.source_pins,plan.source_pins,'binding-sources:'+i);
  equal(b.build_number,i,'binding-number:'+i); equal(b.output,ROOT+'/'+PAPER+'/qa_final/cold_build_'+i,'distinct-literal-output:'+i);
  need(b.scientific_execution===false && b.manuscript_review===false && b.terminal_acceptance===false,'non-science-and-nonacceptance:'+i);
  for(const [role,entry] of Object.entries(plan.future_cwd_relative_roles[i])) {
    equal(entry.actual_observation,null,'future-absence-not-observed:'+i+':'+role);
    equal(entry.future_absolute,b.output+'/inner/source_only/'+entry.relative,'future-role-spelling:'+i+':'+role);
    equal(entry.relative,old.cwd_relative_absence_roles[role].relative,'inherited-relative-role:'+i+':'+role);
  }
}
equal(Object.keys(bindings[0]).filter(k=>!util.isDeepStrictEqual(bindings[0][k],bindings[1][k])),['build_number','output','root_authorization'],'binding-only-three-pair-differences');
const native=obj(BASE+'/NATIVE_PREPARATION_READS.json'); need(native.records.length===23,'all-23-preparation-records');
for(let i=0;i<23;i++) {
  const r=native.records[i];
  if(i===0 || i===1 || i===2 || i===3 || i===5 || i>=21) record(r,'preparation:'+i,i===3?1:0);
  else sedBinding(r,'preparation:'+i);
}
need(native.records[3].result.output.includes('No such file or directory'),'historical-absence-failure-preserved');
const wc=native.records[5].result.output.trim().split('\n'); need(wc.length===6,'wc-six-output-rows');
let totalLines=0,totalBytes=0;for(const line of wc.slice(0,-1)) {
  const m=/^\s*(\d+)\s+(\d+)\s+(.+)$/.exec(line); need(!!m,'wc-row-syntax'); const raw=read(m[3]);
  const lines=raw.filter(x=>x===10).length; equal([Number(m[1]),Number(m[2])],[lines,raw.length],'wc-exact-source-count:'+m[3]);totalLines+=lines;totalBytes+=raw.length;
}
equal([totalLines,totalBytes],[987,53793],'wc-total-987-53793');
need(/987\s+53793\s+total$/.test(wc.at(-1)),'wc-raw-total-row');
const saved21=parse(native.records[21].result.output);
const refresh={}, refreshCorrespondence=[];
for(const phase of ['precopy','postcopy']) {
  const base=REFRESH+'/'+phase+'01', r=obj(base+'/RESULT.json'), ins=obj(base+'/READ_INPUTS.json'), ll=obj(base+'/CHECK_LABELS.json');
  const n=obj(REFRESH+'/'+phase.toUpperCase()+'_NATIVE01.json'), b=obj(REFRESH+'/BUILD_'+phase.toUpperCase()+'_NATIVE01.json');
  const pp=packets(n,phase), bp=packets(b,'build-'+phase), stream=pp.map(x=>x.output).join('');
  equal(parse(stream),r,'full-saved-native-to-RESULT:'+phase);
  equal(parse(bp.map(x=>x.output).join('')),parse(saved21.refresh[phase].build_output),'full-saved-build-output:'+phase);
  refresh[phase]={result:r,input_rows:Object.keys(ins).length,labels_count:ll.length,labels_type:typeof ll,native_keys:Object.keys(n),native_result_keys:Object.keys(n.result),build_native_keys:Object.keys(b),build_exit:b.result.exit_code,build_output:b.result.output};
  if(n.result.exit_code!==undefined) refresh[phase].native_exit=n.result.exit_code;
  need(r.checks===24347 && r.read_paths===3359 && r.r1_all_original_rows_full_stat_checked_twice===2255,'saved-refresh-counts:'+phase);
  need(r.accepted_key_entries===1785 && r.outside_workspace_entries===801 && r.runtime_files===122 && r.runtime_configuration_paths===69 && r.runtime_memberships===5 && r.runtime_loader_directory_states===9,'saved-refresh-key-counts:'+phase);
  const br=parse(bp.map(x=>x.output).join(''));need(br.checks===5974 && br.prior_read_key_entries_checked_twice===1299 && br.configuration_entries_checked_twice===843,'saved-build-check-counts:'+phase);
  refreshCorrespondence.push({phase,final_exit:0,complete_output_bytes:Buffer.byteLength(stream),saved_result_equal:true,host_paths_dereferenced_here:0});
}
const nine=obj(PRIOR+'/NINE_BUILD_SOURCES.json');
equal(saved21,{status:'DATA_ONLY_ORIGINAL_METADATA_NO_DERIVED_LOCK',inputs:plan.input_pins,old_lock_top_level_fields:fields,old_lock_schema:old.schema,old_lock_status:old.status,old_lock_environment:old.environment,old_lock_relative_roles:old.cwd_relative_absence_roles,old_lock_selector_count:840,old_lock_entry_count:840,old_lock_code_observations:old.code_observations,initial_binding:initial,adapters:plan.new_adapter_pins,old_adapters:plan.original_adapter_pins,round2_all_file_pins:all,round2_directory_names:outer.dirs,round2_payload_bytes:outer.payload_bytes,refresh,source_pins:nine.sources,template_delta:['build_number','output','root_authorization'],no_host_dereferences:true,no_ambient_environment_collection:true,no_submitted_source_execution:true},'whole-saved-74261-byte-metadata-object-correspondence');
const saved22=parse(native.records[22].result.output);
need(saved22.rows.length===4,'all-four-native-projections');
for(const row of saved22.rows) {
  const o=obj(row.path,row.pin), pp=packets(o,row.path);
  equal(row.request,o.request,'exact-saved-request:'+row.path);
  equal(row.packets,pp.map(x=>Object.fromEntries(Object.entries({chunk_id:x.chunk_id,exit_code:x.exit_code,session_id:x.session_id,output_bytes:Buffer.byteLength(x.output),truncated:x.output.startsWith('Warning:')}).filter(([,v])=>v!==undefined))),'exact-saved-packet-projection:'+row.path);
}
const metaNative=obj(BASE+'/METADATA_CHECK_NATIVE.json'); record(metaNative,'author-metadata'); const meta=parse(metaNative.result.output);
for(const [n,p] of Object.entries(meta.payload)) read(BASE+'/'+n,p);
need(Object.keys(meta.payload).length===8 && meta.original_input_pins===166 && meta.complete_workspace_read_paths===174 && meta.round2_files===124 && meta.old_field_fingerprints_checked===15 && meta.retained_fields===12 && meta.code_source_lines===272,'saved-author-metadata-counts');
equal(meta.refresh_saved_native_result_correspondence,refreshCorrespondence,'saved-author-refresh-correspondence');
const final=obj(BASE+'/FINAL_SOURCE_READS.json');need(final.records.length===5,'five-final-source-reads');
for(let i=0;i<final.records.length;i++) { const r=final.records[i];sedBinding(r,'final:'+i);equal(Buffer.from(r.result.output),read(r.path),'final-full-raw-file:'+i); }
const pre=obj(BASE+'/PRESEAL_NATIVE.json');record(pre.metadata_preseal,'author-preseal');record(pre.original_preparation_seal_check,'author-prior-seal');
const pres=parse(pre.metadata_preseal.result.output);for(const [n,p] of Object.entries(pres.payload)) read(BASE+'/'+n,p);
need(pres.payloads===10 && Object.keys(pres.payload).length===10 && pres.payload_bytes===503477 && pres.original_workspace_input_pins_checked_twice===166 && pres.full_final_native_text_bindings===5,'saved-preseal-counts');
equal(Object.values(pres.payload).reduce((s,p)=>s+p.bytes,0),pres.payload_bytes,'saved-preseal-byte-arithmetic');
equal(pre.original_preparation_seal_check.request.cmd,'sha256sum -c SHA256SUMS','original-seal-command');
equal(pre.original_preparation_seal_check.request.workdir,ROOT+'/'+PRIOR,'original-seal-cwd');
equal(pre.original_preparation_seal_check.result.output,Object.keys(originalSource.pins).map(n=>n+': OK\n').join(''),'all-22-original-seal-native-lines');
for(const n of Object.keys(reads)) read(n,reads[n]);
// No fs writes, subprocess, imports of submitted code, ambient settings reads,
// host-key dereferences or operational output existence probes occur above.
process.stdout.write(JSON.stringify({status:'INDEPENDENT_SOURCE_METADATA_CHECKS_COMPLETED_NOT_OPERATIONAL_ACCEPTANCE',checks:labels.length,unique_workspace_files:Object.keys(reads).length,submitted:{payloads:submitted.payloads,payload_bytes:submitted.payload_bytes,total_bytes:submitted.payload_bytes+submitted.seal.bytes,seal:submitted.seal},original_source_payloads:originalSource.payloads,plan_pins:166,round2:{files:124,payloads:123,payload_bytes:outer.payload_bytes,directories:outer.dirs,seals:[outer.seal,aSeal.seal,bSeal.seal]},original_lock:plan.original_lock,original_fields:15,retained_fields:12,changed_fields:changed,disabled_bindings:2,fresh_adapter_lines:987,fresh_adapter_bytes:53793,native_records:nativeRows,refresh_saved_correspondence:refreshCorrespondence,read_pins:reads,read_stat_schema:['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'],read_stats:snapshots,checks_labels_pin:pin(Buffer.from(JSON.stringify(labels))),limits:{submitted_code_executions:0,submitted_import_AST_compile:0,derived_lock_files:0,host_paths_dereferenced:0,ambient_environment_read:false,operational_output_absence_probes:0,builds:0,science:0,page_views:0,round2_accepted:false,root_authority:false,historical_navigation_and_rg_not_asserted_current:true,historical_absence_outputs_not_asserted_current:true}},null,2)+'\n');
