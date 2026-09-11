'use strict';
// Finite current documentary and actual closed raw closure; no producer/host path actions.
const fs=require('node:fs'),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const R='docs/papers211_215_sequence/qa/p213_author_strict_pair_execution_root01/';
const spec=JSON.parse(fs.readFileSync(R+'INPUT_SPEC.json','utf8'));
const PRE=['PREFLIGHT.cjs','GRANT.replay01.json','GRANT.replay02.json','PREFLIGHT.replay01.NATIVE.json','PREFLIGHT.replay02.NATIVE.json','CONSUMPTION.replay01.json','CONSUMPTION.replay02.json','ACTUAL.replay01.NATIVE.json','ACTUAL.replay02.NATIVE.json','RAW_RECEIVE.cjs','PARSER_READ_NATIVE.json','RAW.replay01.NATIVE.json','RAW.replay02.NATIVE.json','CMP_NATIVE.json','RAW_INPUTS.sha256','INPUT_SPEC.json','HANDOFF.md','CLOSE.cjs'];
const final=process.argv.length===3&&process.argv[2]==='--sealed',payload=final?[...PRE,'CLOSING_NATIVE.json','CLOSING_RESULT.json']:PRE,names=[...payload,...(final?['SHA256SUMS']:[])];
const r=make(new Set([...spec.external.map(k=>k.path),...names.map(n=>R+n)])),{need,read,equal,sha,keys}=r;let old=0,pairs=0;
need(process.argv.length===2||final,'EXACT_READ_ONLY_PHASE');need(process.cwd()==='/root/autodl-tmp/symbolic_dynamics','EXACT_CWD');
for(const p of r.keys.keys())throw Error('UNEXPECTED_BOOTSTRAP_KEY');
for(const k of spec.external)read(k.path);for(const n of names)read(R+n);
need(equal(JSON.parse(read(R+'INPUT_SPEC.json')),spec),'ENTIRE_TRUSTED_BOOTSTRAP_SPEC_RAW_READ');
need(equal(fs.readdirSync(R).sort(),names.slice().sort()),'EXACT_NONSELF_PHASE_INVENTORY');
function key(k){need(keys.has(k.path)&&equal(keys.get(k.path),k),'ENTIRE_OLD_CURRENT_KEY');old++;}
spec.external.forEach(key);
for(const [stage,scienceId,preId,rawId]of [['replay01','2aa611','2a4e1c','a0a5dc'],['replay02','384c57','a1cd2a','d64a46']]){
 const json=n=>JSON.parse(read(R+n)),g=json('GRANT.'+stage+'.json'),c=json('CONSUMPTION.'+stage+'.json'),a=json('ACTUAL.'+stage+'.NATIVE.json');
 need(a.result.chunk_id===scienceId&&a.result.exit_code===0&&!a.result.session_id&&a.continuations.length===0,'EXACT_ACTUAL_NEW_SCIENCE_NATIVE');
 need(equal(a.request,g.native_request.arguments)&&equal(c.exact_native_request,g.native_request)&&c.grant_id===g.id&&c.remaining_submissions===0,'ENTIRE_CONSUMED_DISTINCT_GRANT_BINDING');
 need(Buffer.from(a.result.output).equals(Buffer.from('P213_SCIENCE_NATIVE_EXIT=0\n')),'WHOLE_ACTUAL_NATIVE_STATUS_RAW');
 for(const [name,id,command,status]of [
 ['PREFLIGHT.'+stage+'.NATIVE.json',preId,'PREFLIGHT.cjs '+stage,'PASS_CURRENT_PREFLIGHT_FOR_NEW_DISTINCT_STRICT_RUN'],
 ['RAW.'+stage+'.NATIVE.json',rawId,'RAW_RECEIVE.cjs '+stage,'PASS_COMPLETE_STRICT_RAW_BYTES_PENDING_INDEPENDENT_CONTROL_AND_PAIR_RECEPTION']]){
  const n=json(name);need(n.result.chunk_id===id&&n.result.exit_code===0&&!n.result.session_id&&n.request.cmd==='node '+R+command,'EXACT_PRIOR_NATIVE');
  const v=JSON.parse(n.result.output);need(v.status===status&&v.stage===stage,'ENTIRE_PRIOR_RAW_RESULT_DATA');v.keys.forEach(key);
  if(name.startsWith('RAW.'))v.raw_keys.forEach(key);
 }
}
const Q='docs/papers211_215_sequence/qa/',can='papers/213-receiver-limited-cyclic-transfer/canonical_stdout.txt',one=Q+'p213_author_strict_pair_run01/stdout.bin',two=Q+'p213_author_strict_pair_run02/stdout.bin';
const expected=[[one,can],[two,can],[one,two]],cmp=JSON.parse(read(R+'CMP_NATIVE.json'));
need(cmp.native.length===3,'ALL_THREE_ACTUAL_NATIVE_RAW_COMPARISONS');
expected.forEach(([a,b],i)=>{const n=cmp.native[i];need(n.request.cmd==='cmp -- '+a+' '+b&&n.result.exit_code===0&&!n.result.session_id&&n.result.output==='','EXACT_ACTUAL_RAW_CMP_NATIVE');need(read(a).equals(read(b)),'WHOLE_RAW_COMPARISON_REPERFORMED');pairs++;});
const raw=spec.external.filter(k=>/^docs\/papers211_215_sequence\/qa\/p213_author_strict_pair_run0[12]\/(?:stdout|stderr|runtime_control)\.bin$/.test(k.path)).sort((a,b)=>a.path.localeCompare(b.path));
need(raw.length===6&&Buffer.from(raw.map(k=>sha(read(k.path))+'  '+k.path+'\n').join('')).equals(read(R+'RAW_INPUTS.sha256')),'ENTIRE_SIX_RAW_WORKSPACE_RELATIVE_SEAL');
if(final){
 const n=JSON.parse(read(R+'CLOSING_NATIVE.json')),v=JSON.parse(read(R+'CLOSING_RESULT.json'));
 need(n.result.exit_code===0&&!n.result.session_id&&n.request.cmd==='node '+R+'CLOSE.cjs','ACTUAL_PRESEAL_NATIVE');
 need(Buffer.from(n.result.output).equals(read(R+'CLOSING_RESULT.json'))&&v.status==='PASS_STRICT_EXECUTION_RAW_DOCUMENTARY_CLOSURE'&&v.phase==='PRESEAL_EIGHTEEN_PAYLOADS','ENTIRE_PRESEAL_NATIVE_RESULT_RAW');pairs++;v.keys.forEach(key);
 need(Buffer.from(payload.slice().sort().map(n=>sha(read(R+n))+'  '+n+'\n').join('')).equals(read(R+'SHA256SUMS')),'ENTIRE_TWENTY_PAYLOAD_NONSELF_SEAL');
}
const payloads=payload.slice().sort().map(n=>({name:n,bytes:read(R+n).length,sha256:sha(read(R+n))}));
process.stdout.write(JSON.stringify({status:'PASS_STRICT_EXECUTION_RAW_DOCUMENTARY_CLOSURE',phase:final?'FINAL_TWENTY_PAYLOADS':'PRESEAL_EIGHTEEN_PAYLOADS',checks:r.checks,key_count:keys.size,total_read_bytes:r.total,entire_prior_keys:old,complete_raw_pairs:pairs,payloads,payload_bytes:payloads.reduce((s,p)=>s+p.bytes,0),scientific_execution:false,new_grant:false,full_control_semantics_accepted:false,pair_accepted:false,keys:[...keys.values()]},null,2)+'\n');
