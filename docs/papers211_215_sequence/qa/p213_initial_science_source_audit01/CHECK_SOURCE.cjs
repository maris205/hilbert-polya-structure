'use strict';
// Independent finite documentary checker. Reads only the fixed existing source
// inputs below. No Python, AST, compile, eval, child process or embedded-path use.
const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert');
const base = 'docs/papers211_215_sequence/qa/p213_initial_science_preparation01/';
const prior = 'docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/';
const paper = 'papers/213-receiver-limited-cyclic-transfer/';
const names = [
  'BINDING.proposed.json', 'CHECK_NATIVE.json', 'COLLECTOR_REUSE_CHECK.json',
  'CREATION_NATIVE.json', 'DEPENDENCY_CONTRACT.md', 'EXECUTION_SEQUENCE.md',
  'HANDOFF.md', 'PREPARATION.md', 'REQUEST.disabled.json', 'SOURCE_DELTA.md',
  'SOURCE_INPUTS.sha256', 'SOURCE_TEXT_READS_NATIVE.json',
  'WORKSPACE_READS_NATIVE.json', 'capture.initial.disabled.sh',
  'capture.replay01.disabled.sh', 'capture.replay02.disabled.sh',
  'run_science.disabled.py', 'SHA256SUMS'
];
const external = [
  paper+'verify.py', paper+'VERIFICATION_PARAMETERS.json', paper+'OUTPUT_SCHEMA.md',
  paper+'SCIENTIFIC_DEPENDENCIES.md', paper+'RUNTIME_PLAN.md', paper+'REVIEW_INTERFACES.md',
  'docs/papers211_215_sequence/P213_THEOREM_CONTRACT.md',
  'docs/papers211_215_sequence/qa/p213_source_parameter_root01/RECEPTION.md',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/CONTRACT.md',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/BINDING_FORMAT.md',
  prior+'BINDING.runtime_literal.json', prior+'observe.proposed.py.txt',
  prior+'capture.proposed.sh.txt',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_root01/RECEPTION.md',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_probe_reception_root01/RECEPTION.md',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_probe_reception_root01/SHA256SUMS'
];
const paths = [...names.map(n=>base+n), ...external];
const texts = new Map(), keys = [], checks = [];
const digest = b=>crypto.createHash('sha256').update(b).digest('hex');
function ok(id, value, detail) {
  checks.push({id, pass:Boolean(value), ...(detail===undefined ? {} : {detail})});
}
function equal(a,b) { try { assert.deepStrictEqual(a,b); return true; } catch { return false; } }
function stat(s) {
  return Object.fromEntries(['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs']
    .map(k=>[k,s[k].toString()]));
}
for (const path of paths) {
  const k={path, byte_count:0, eof:false, complete:false, closed:false};
  keys.push(k);
  let fd;
  try {
    const first=fs.lstatSync(path,{bigint:true});
    assert(first.isFile() && !first.isSymbolicLink() && first.size<=2097152n);
    k.begin=stat(first);
    fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
    k.fd_before=stat(fs.fstatSync(fd,{bigint:true}));
    assert(equal(k.begin,k.fd_before));
    const chunks=[];
    for (;;) {
      const b=Buffer.alloc(Math.min(65536,2097153-k.byte_count));
      const n=fs.readSync(fd,b,0,b.length,null);
      if (!n) { k.eof=true; break; }
      chunks.push(b.subarray(0,n)); k.byte_count+=n;
      assert(k.byte_count<=2097152);
    }
    k.fd_after=stat(fs.fstatSync(fd,{bigint:true}));
    k.after_read=stat(fs.lstatSync(path,{bigint:true}));
    assert(equal(k.begin,k.fd_before)&&equal(k.fd_before,k.fd_after)&&equal(k.begin,k.after_read));
    assert(k.byte_count===Number(first.size));
    const bytes=Buffer.concat(chunks);
    k.sha256=digest(bytes); texts.set(path,bytes.toString('utf8'));
  } finally { if(fd!==undefined) { fs.closeSync(fd); k.closed=true; } }
  k.complete=k.eof&&k.closed;
}
const read=p=>{ assert(texts.has(p)); return texts.get(p); };
const json=p=>JSON.parse(read(p));
const key=p=>keys.find(k=>k.path===p);
function pins(t) {
  assert(t.endsWith('\n'));
  return t.trimEnd().split('\n').map(line=>{
    const m=/^([a-f0-9]{64})  ([A-Za-z0-9_./-]+)$/.exec(line); assert(m);
    return {sha256:m[1],path:m[2]};
  });
}
ok('34_fixed_documentary_inputs',keys.length===34&&keys.every(k=>k.complete));
ok('source_nonself_manifest_pin',key(base+'SHA256SUMS').sha256==='ef1e95d740634c6531706aaa3b4fda0f0f99fbb14f604c80bc24f3d3235a7cdf');
ok('source_exact_18_file_census',equal(fs.readdirSync(base).sort(),[...names].sort()));
const manifest=pins(read(base+'SHA256SUMS'));
ok('source_manifest_exact_17_nonself_members',equal(manifest.map(p=>p.path).sort(),names.filter(n=>n!=='SHA256SUMS').sort()));
for(const p of manifest)ok('source_manifest:'+p.path,key(base+p.path)?.sha256===p.sha256);
ok('source_package_exact_total',names.reduce((n,p)=>n+key(base+p).byte_count,0)===868945);
const sourcepins=pins(read(base+'SOURCE_INPUTS.sha256'));
ok('external_pin_exact_16_input_scope',equal(sourcepins.map(p=>p.path),external));
for(const p of sourcepins)ok('external_pin:'+p.path,key(p.path)?.sha256===p.sha256);
const b=json(base+'BINDING.proposed.json'), old=json(prior+'BINDING.runtime_literal.json');
const req=json(base+'REQUEST.disabled.json');
const source=read(base+'run_science.disabled.py'), oldsource=read(prior+'observe.proposed.py.txt');
const sci=read(paper+'verify.py');
const firstStatement=s=>s.split('\n').find(x=>x.trim()&&!x.trimStart().startsWith('#'));
ok('wrapper_gate_first',firstStatement(source)==='raise SystemExit("P213_SCIENCE_PREPARATION_DISABLED_NO_AUTHORITY")');
function pythonLiteral(o) {
  // Lexical spelling conversion of JSON DATA only; never parses/evaluates Python.
  return JSON.stringify(o,null,2).replace(/"(?:\\.|[^"\\])*"|\b(?:null|true|false)\b/g,
    t=>t[0]==='"'?t:({null:'None',true:'True',false:'False'})[t]);
}
const literalStart=source.indexOf('BINDING = '), literalEnd=source.indexOf('\n\nif BINDING is None:');
ok('inline_binding_exact_entire_documentary_conversion',literalStart>=0&&literalEnd>literalStart&&source.slice(literalStart+10,literalEnd).trimEnd()===pythonLiteral(b));
const inverse=JSON.parse(JSON.stringify(b));
inverse.id=old.id; inverse.observer=old.observer;
inverse.launch_policy.argv=old.launch_policy.argv;
inverse.launch_policy.orig_argv=old.launch_policy.orig_argv;
inverse.modules.__main__.file=old.modules.__main__.file;
inverse.modules.__main__.file_roles=old.modules.__main__.file_roles;
inverse.files=inverse.files.filter(e=>e.lexical!==b.science.source).map(e=>{
  if(e.lexical===b.observer) { e.lexical=old.observer; e.final=old.observer; } return e;
});
inverse.bounds.files=old.bounds.files; delete inverse.science;
ok('complete_inverse_binding_delta_equals_baseline',equal(inverse,old));
ok('exact_science_entry',equal(b.files.find(e=>e.lexical===b.science.source),{
  lexical:b.science.source,final:b.science.source,links:[],optional:false,absence_required:false,
  earliest_phase:'helper',roles:['scientific_source_exact_bytes'],observed_presence:null,observed_key:null
}));
const rolecount=role=>b.files.filter(e=>e.roles.includes(role)).length;
const mechanisms=Object.values(b.modules).reduce((a,m)=>(a[m.mechanism]=(a[m.mechanism]||0)+1,a),{});
ok('70_candidates_62_modules',b.files.length===70&&Object.keys(b.modules).length===62);
ok('26_builtin_3_frozen_32_filebacked_1_main',mechanisms.builtin===26&&mechanisms.frozen===3&&mechanisms.source_file+mechanisms.extension_file===32&&mechanisms.direct_script===1,mechanisms);
ok('29_matching_29_cache_9_map_6_special',rolecount('source_or_matching_source')===29&&rolecount('eligible_nonoptimized_cache')===29&&rolecount('mapped_file')===9&&b.special_maps.length===6);
ok('23_62_62_phase_permissions',b.module_names.early.length===23&&b.module_names.helper.length===62&&b.module_names.closing.length===62);
ok('all_observation_placeholders_null',b.files.every(e=>e.observed_presence===null&&e.observed_key===null)&&Object.values(b.modules).every(e=>e.observed_row===null)&&b.launch_policy.full_actual_record===null);
const newcodes=['science_key','science_source_pin','science_loaded_key','science_loaded_pin','science_source_ascii','science_source_bytes','science_builtin_binding','science_stream_binding','science_phase_module_change','science_phase_launch_change','science_phase_process_change','science_phase_map_change','stdio_regular','stdio_nlink','stdio_empty','stdio_distinct','stdio_input_collision','stdio_identity','stdio_unchanged','science_stdout_bound','science_not_completed','runtime_key_changed','control_bound','control_short_write','control_unready','control_changed'];
const vocab=s=>s.slice(s.indexOf('FAILURE_CODES = ('),s.indexOf('\nclass ObserverFailure')).trimEnd();
const codes=s=>[...vocab(s).matchAll(/^    "([a-z_]+)",$/gm)].map(m=>m[1]);
ok('99_original_plus_exact_26_failure_codes',codes(oldsource).length===99&&equal(codes(source),[...codes(oldsource),...newcodes]));
const oldfrag=oldsource.slice(oldsource.indexOf('if BINDING is None:'),oldsource.indexOf('RESULT = {'));
const newfrag=source.slice(source.indexOf('if BINDING is None:'),source.indexOf('def output_points():'));
const transformed=oldfrag.replace(vocab(oldsource),vocab(source)).replaceAll('sys.stdout.write(ascii(', 'sys.stderr.write(ascii(');
// Exclude only trailing separator whitespace after the final function body.
// Failure01 preserves the original comparison that included one extra blank line.
ok('entire_collector_fragment_exact_declared_delta',transformed.trimEnd()===newfrag.trimEnd(),{old_body_chars:oldfrag.trimEnd().length,new_body_chars:newfrag.trimEnd().length,old_separator_chars:oldfrag.length-oldfrag.trimEnd().length,new_separator_chars:newfrag.length-newfrag.trimEnd().length,stderr_replacements:(oldfrag.match(/sys[.]stdout[.]write\(ascii\(/g)||[]).length});
const funcs=['need','failure','same_tree','tuple_tree','frozen','attribute','loader_id','module_snapshot','launch_snapshot','path_ok','launch_allowed','binding_entries','module_delta','mapped_paths','missing_or_null','module_roles','raw_maps','map_roles','canonical','full_stat','points','key_file','process_points'];
function deftext(s,n) {
  const start=s.indexOf('def '+n+'('); assert(start>=0);
  const lineEnd=s.indexOf('\n',start), tail=s.slice(lineEnd+1);
  const end=tail.search(/^\S/m); return s.slice(start,end<0?s.length:lineEnd+1+end).trimEnd();
}
for(const n of funcs)ok('unchanged_function:'+n,deftext(source,n)===deftext(oldsource,n));
ok('unchanged_exception_class',source.slice(source.indexOf('class ObserverFailure'),source.indexOf('def need('))===oldsource.slice(oldsource.indexOf('class ObserverFailure'),oldsource.indexOf('def need(')));
ok('science_pinned_exact_ascii_bytes',key(paper+'verify.py').byte_count===17539&&key(paper+'verify.py').sha256==='a01d3d93619cea90adfc2e5be1bdfd8089d7eae6fcaae153b4fb4af398fc1812'&&Buffer.from(sci).every(x=>x<128));
ok('request_binding_science_pins',req.science_source.bytes===17539&&b.science.source_bytes===17539&&req.science_source.sha256===key(paper+'verify.py').sha256&&b.science.source_sha256===key(paper+'verify.py').sha256);
ok('scientific_source_has_no_import_statement',!/^\s*(import |from .+ import )/m.test(sci));
const param=json(paper+'VERIFICATION_PARAMETERS.json');
ok('unchanged_declared_box',equal(param.code_constants,{N_MIN:1,N_MAX:6,MASS_MIN:0,MASS_MAX:4,EXPECTED_CARRIERS:30,EXPECTED_STATES:461}));
for(const [n,v] of Object.entries(param.code_constants))ok('science_constant:'+n,sci.includes('\n'+n+' = '+v+'\n'));
ok('source_sole_name_entry',sci.includes('if __name__ == "__main__":\n    main()'));
ok('exact_compile_and_exec_source',source.includes('science_code = compile(science_bytes, BINDING["science"]["source"], "exec",\n                           flags=0, dont_inherit=True, optimize=0)')&&source.includes('exec(science_code, science_globals, science_globals)'));
ok('no_new_loader_or_argv_module_rewrite',!/^\s*(?:import runpy|import importlib|from runpy|from importlib|sys[.]argv\s*=|sys[.]orig_argv\s*=|sys[.]modules\[.*\]\s*=)/m.test(source));
for(const flag of ['runtime_accepted','science_accepted','canonical_adopted','strict_pair_completed'])ok('wrapper_acceptance_false:'+flag,source.includes('"'+flag+'": False'));
ok('disabled_request_no_authority',req.operation_authorized===false&&req.request_cmd===null&&req.root_grant===null);
ok('enabled_wrapper_unresolved',req.enabled_wrapper.present_observed===null&&req.enabled_wrapper.whole_key===null&&req.enabled_wrapper.source_sha256===null&&req.enabled_wrapper.exact_enabled_source_review===null);
ok('three_distinct_separate_stage_gates',equal(req.stages.map(s=>s.id),['initial','replay01','replay02'])&&new Set(req.stages.map(s=>s.proposed_output_directory)).size===3&&req.stages.every(s=>s.request_cmd===null&&s.root_grant===null&&s.future_path_queried===false&&s.accepted===false));
const captures=req.stages.map(s=>read(base+s.disabled_capture));
for(let i=0;i<3;i++) {
  ok('capture_disabled:'+i,firstStatement(captures[i])==='exit 78');
  ok('capture_finite_fresh_and_descriptor_order:'+i,captures[i].includes('umask 077\nset -o noclobber')&&captures[i].includes('"$P213_CAPTURE_MKDIR" -m 700 -- "$P213_CAPTURE_DIRECTORY" || exit 78')&&captures[i].includes('1>&3 2>&4 3>&5 4>&- 5>&-')&&captures[i].includes('P213_CAPTURE_STATUS=$?'));
  ok('capture_only_directory_variant:'+i,captures[i].replace(req.stages[i].proposed_output_directory,req.stages[0].proposed_output_directory)===captures[0]);
}
ok('canonical_separate_unresolved',req.canonical_adoption.request_cmd===null&&req.canonical_adoption.root_grant===null&&req.canonical_adoption.target_queried===false&&req.canonical_adoption.adopted===false&&req.canonical_adoption.sha256===null&&req.canonical_adoption.may_use_candidate_or_gate_data===false);
ok('pair_two_new_runs_not_initial',req.strict_pair.both_new_runs_required===true&&req.strict_pair.initial_counts_as_replay===false&&req.strict_pair.request_cmd===null&&req.strict_pair.root_grant===null&&req.strict_pair.completed===false&&equal(req.strict_pair.full_raw_comparisons,['replay01 vs canonical','replay02 vs canonical','replay01 vs replay02']));
const srcarchive=json(base+'SOURCE_TEXT_READS_NATIVE.json');
ok('author_original_whole_old_source_receipt',srcarchive.records[0].result.exit_code===0&&srcarchive.records[0].result.output===oldsource);
ok('author_original_whole_new_source_receipt',srcarchive.records[1].result.exit_code===0&&srcarchive.records[1].result.output===source);
const ca=json(base+'CHECK_NATIVE.json');
for(const [i,n] of [[2,'BINDING.proposed.json'],[3,'REQUEST.disabled.json'],[4,'capture.initial.disabled.sh'],[5,'capture.replay01.disabled.sh'],[6,'capture.replay02.disabled.sh']])ok('author_actual_full_read:'+n,ca.records[i].result.exit_code===0&&ca.records[i].result.output===read(base+n));
const wa=json(base+'WORKSPACE_READS_NATIVE.json');
const authorFailures=wa.records.filter(r=>r.result.exit_code!==0||r.result.output.startsWith('Warning: truncated output')).map(r=>({role:r.role,chunk:r.result.chunk_id,exit:r.result.exit_code,truncated:r.result.output.startsWith('Warning: truncated output')}));
ok('author_failed_and_truncated_evidence_preserved',equal(authorFailures,[{role:'binding_runtime_literal',chunk:'532c13',exit:0,truncated:true},{role:'selected_existing_input_hashes',chunk:'655509',exit:1,truncated:false}]));
ok('author_binding_truncation_recovered_exactly',[26,27,28].map(i=>wa.records[i].result.output).join('')===read(prior+'BINDING.runtime_literal.json'));
for(const r of wa.records) {
  const m=/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_./-]+)$/.exec(r.request.cmd);
  if(m&&texts.has(m[3])&&!r.result.output.startsWith('Warning: truncated output')) {
    const expected=read(m[3]).split(/(?<=\n)/).slice(Number(m[1])-1,Number(m[2])).join('');
    ok('author_existing_document_receipt:'+r.role,r.result.exit_code===0&&r.result.output===expected);
  }
}
ok('author_not_independent_or_executed',ca.independent_review===false&&ca.scientific_execution===false&&ca.enabled_copy_materialization===false);
const result={schema:'P213_INDEPENDENT_FIXED_SOURCE_DOCUMENTARY_CHECK_V1',
  scope:'Documentary consistency and existing-workspace input keys only; semantic judgment is separate in AUDIT.md.',
  stat_integer_representation:'Exact decimal strings from native bigint values; mtimeNs/ctimeNs are native nanoseconds.',
  scientific_execution:false, future_operand_lookup:false, operational_authority:false,
  checks,checks_count:checks.length,failed:checks.filter(c=>!c.pass),author_retained_failures:authorFailures,keys};
console.log(JSON.stringify(result,null,2));
process.exitCode=result.failed.length?1:0;
