'use strict';
// Own documentary closure only. No source evaluation or operational paths.
const fs=require('fs'), crypto=require('crypto'), assert=require('assert');
const own='docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/';
const src='docs/papers211_215_sequence/qa/p213_initial_science_preparation01/';
const files=['PLAN.md','CHECK_SOURCE.cjs','CHECK_SOURCE_FAILURE01.cjs.txt',
 'CHECK_FAILURE01_NATIVE.json','AUDIT.md','FINDINGS.json','HANDOFF.md',
 'READ_NATIVE.json','CHECK_NATIVE.json','INPUTS.sha256','CLOSE_DOCUMENTS.cjs'];
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p,'utf8');
const json=p=>JSON.parse(read(p));
const checks=[];
const ok=(id,value)=>checks.push({id,pass:Boolean(value)});
const native=json(own+'CHECK_NATIVE.json'), result=JSON.parse(native.native.output);
const failure=json(own+'CHECK_FAILURE01_NATIVE.json');
const reads=json(own+'READ_NATIVE.json').records;
ok('current_exact_11_preseal_payloads',JSON.stringify(fs.readdirSync(own).sort())===JSON.stringify([...files].sort()));
ok('original_successful_check_a0f17d',native.native.chunk_id==='a0f17d'&&native.native.exit_code===0&&result.checks_count===133&&result.checks.length===133&&result.failed.length===0&&result.checks.every(c=>c.pass));
ok('original_failed_check_cbbb40_preserved',failure.native.chunk_id==='cbbb40'&&failure.native.exit_code===1&&JSON.parse(failure.native.output).failed.length===1);
ok('failure_exact_boundary_diagnostic_preserved',failure.diagnosis.native.chunk_id==='07ed99'&&failure.diagnosis.native.exit_code===0&&JSON.parse(failure.diagnosis.native.output).first_difference===28800&&JSON.parse(failure.diagnosis.native.output).exact_equal_after_removing_only_boundary_trailing_whitespace===true);
const census=json(own+'FINDINGS.json').current_census;
ok('zero_current_source_findings',Object.values(census).every(n=>n===0)&&json(own+'FINDINGS.json').source_findings.length===0);
ok('full_50_original_read_records',reads.length===50&&reads.every(r=>typeof r.native.output==='string'&&typeof r.request.cmd==='string'));
ok('truncated_original_read_preserved',reads[47].native.chunk_id==='041b83'&&reads[47].native.output.startsWith('Warning: truncated output'));
const pins=read(own+'INPUTS.sha256').trimEnd().split('\n');
ok('exact_34_input_pins',pins.length===34&&result.keys.length===34&&pins.every((line,i)=>line===result.keys[i].sha256+'  '+result.keys[i].path));
const current=new Map();
for(const k of result.keys) {
 // Only this reviewed fixed set is admitted: a known source package member or
 // one of the selected existing external source/document paths (never raw).
 const allowed=k.path.startsWith(src)||[
  'papers/213-receiver-limited-cyclic-transfer/verify.py',
  'papers/213-receiver-limited-cyclic-transfer/VERIFICATION_PARAMETERS.json',
  'papers/213-receiver-limited-cyclic-transfer/OUTPUT_SCHEMA.md',
  'papers/213-receiver-limited-cyclic-transfer/SCIENTIFIC_DEPENDENCIES.md',
  'papers/213-receiver-limited-cyclic-transfer/RUNTIME_PLAN.md',
  'papers/213-receiver-limited-cyclic-transfer/REVIEW_INTERFACES.md',
  'docs/papers211_215_sequence/P213_THEOREM_CONTRACT.md',
  'docs/papers211_215_sequence/qa/p213_source_parameter_root01/RECEPTION.md',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/CONTRACT.md',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/BINDING_FORMAT.md',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/BINDING.runtime_literal.json',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/observe.proposed.py.txt',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/capture.proposed.sh.txt',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_root01/RECEPTION.md',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_probe_reception_root01/RECEPTION.md',
  'docs/papers211_215_sequence/qa/p213_minimal_observer_probe_reception_root01/SHA256SUMS'
 ].includes(k.path);
 assert(allowed&&!k.path.includes('..')&&fs.lstatSync(k.path).isFile());
 const b=fs.readFileSync(k.path); current.set(k.path,b.toString('utf8'));
 ok('current_input_pin:'+k.path,k.complete&&k.closed&&k.eof&&b.length===k.byte_count&&hash(b)===k.sha256);
}
for(const r of reads) {
 const m=/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_./-]+)$/.exec(r.request.cmd);
 if(m&&current.has(m[3])&&!r.native.output.startsWith('Warning: truncated output')) {
  const t=current.get(m[3]).split(/(?<=\n)/).slice(Number(m[1])-1,Number(m[2])).join('');
  ok('recorded_read_matches_frozen_input:'+r.native.chunk_id,r.native.exit_code===0&&r.native.output===t);
 }
}
ok('all_3083_wrapper_lines_reconstructed',reads.slice(16,21).map(r=>r.native.output).join('')===current.get(src+'run_science.disabled.py'));
ok('whole_new_binding_reconstructed',reads.slice(21,24).map(r=>r.native.output).join('')===current.get(src+'BINDING.proposed.json'));
ok('whole_old_binding_reconstructed',reads.slice(44,47).map(r=>r.native.output).join('')===current.get('docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/BINDING.runtime_literal.json'));
ok('no_authority_in_findings',json(own+'FINDINGS.json').operational_authority===false&&json(own+'FINDINGS.json').external_status==='HOLD_EXTERNAL');
const payloads=files.map(name=>{const b=fs.readFileSync(own+name);return{name,bytes:b.length,sha256:hash(b)};});
const output={schema:'P213_SOURCE_AUDIT_PRESEAL_CLOSURE_V1',checks_count:checks.length,checks,failed:checks.filter(c=>!c.pass),preseal_payloads:payloads,preseal_payload_bytes:payloads.reduce((n,p)=>n+p.bytes,0),next:'Archive this original native result as CLOSURE_NATIVE.json, then seal the exact 12 payloads with the sole nonself SHA256SUMS.',scientific_execution:false,source_mutation:false,operational_authority:false};
console.log(JSON.stringify(output,null,2));
process.exitCode=output.failed.length?1:0;
