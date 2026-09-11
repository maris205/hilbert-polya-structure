'use strict';
// Finite read-only copy-receipt closure. Never invoke ADOPT or science.
const fs=require('node:fs'),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const Q='docs/papers211_215_sequence/qa/',R=Q+'p213_author_canonical_adoption_root01/',D=Q+'p213_initial_science_data_root01/';
const source=Q+'p213_initial_science_run01/stdout.bin',target='papers/213-receiver-limited-cyclic-transfer/canonical_stdout.txt';
const PRE=['ADOPT.cjs','GRANT.json','CONSUMPTION.json','ROOT_READS_NATIVE.json','ADOPT_NATIVE.json','ADOPT_RESULT.json','RECEIVE_NATIVE.json','RECEIVE_RESULT.json','RECEIPT.md','CLOSE.cjs'];
const final=process.argv.length===3&&process.argv[2]==='--sealed',payload=final?[...PRE,'CLOSING_NATIVE.json','CLOSING_RESULT.json']:PRE;
const prior=['CHECK_NATIVE.json','CHECK_ROOT.cjs','CLOSE.cjs','CLOSING_NATIVE.json','CLOSING_RESULT.json','INPUT_SPEC.json','RECEPTION.md','REPLAY_NATIVE.json','RESULT.json','ROOT_READS_NATIVE.json','SHA256SUMS'];
const names=[...payload,...(final?['SHA256SUMS']:[])];
const paths=[...prior.map(n=>D+n),...names.map(n=>R+n),Q+'p213_initial_science_enabled_root01/READ_FIXED.cjs',source,target];
const r=make(new Set(paths)),{need,read,equal,sha,keys}=r;let old=0,pairs=0;
need(process.argv.length===2||final,'EXACT_CLOSURE_MODE');
need(process.cwd()==='/root/autodl-tmp/symbolic_dynamics','EXACT_CWD');
paths.forEach(read);
need(equal(fs.readdirSync(R).sort(),names.slice().sort()),'EXACT_NONSELF_PHASE_LAYOUT');
function key(k){need(keys.has(k.path)&&equal(keys.get(k.path),k),'ENTIRE_PRIOR_KEY');old++;}
for(const [nn,rn,cmd,status,id]of [
 ['ADOPT_NATIVE.json','ADOPT_RESULT.json','--adopt','PASS_EXACT_CANONICAL_RAW_COPY','f05161'],
 ['RECEIVE_NATIVE.json','RECEIVE_RESULT.json','--receive','PASS_READ_ONLY_EXACT_CANONICAL_ADOPTION_RECEPTION','f348d3']]){
 const n=JSON.parse(read(R+nn)),v=JSON.parse(read(R+rn));
 need(n.result.chunk_id===id&&n.result.exit_code===0&&!n.result.session_id&&n.request.cmd==='node '+R+'ADOPT.cjs '+cmd,'ACTUAL_FIXED_NATIVE');
 need(Buffer.from(n.result.output).equals(read(R+rn)),'WHOLE_NATIVE_RESULT_RAW');pairs++;
 need(v.status===status&&v.failure===null,'ACTUAL_PASS_SCOPE');
 v.keys.forEach(key);key(v.source_key);key(v.canonical_key);
}
need(read(source).equals(read(target)),'WHOLE_PHYSICAL_CANONICAL_RAW');pairs++;
need(sha(read(D+'SHA256SUMS'))==='59337ecab14eb2c7e0155b48b460b6452f1ec4fb37396d3b1ca6beceb8642308','UNCHANGED_INITIAL_DATA_SEAL');
need(sha(read(Q+'p213_initial_science_enabled_root01/READ_FIXED.cjs'))==='f3faa0a29e91dd56ace36b3e7d1dd54f11e97064122c1a9b2c77b20edc6667c7','PINNED_TRUSTED_READER');
if(final){
 const n=JSON.parse(read(R+'CLOSING_NATIVE.json')),v=JSON.parse(read(R+'CLOSING_RESULT.json'));
 need(n.result.exit_code===0&&!n.result.session_id&&n.request.cmd==='node '+R+'CLOSE.cjs','ACTUAL_PRESEAL_NATIVE');
 need(Buffer.from(n.result.output).equals(read(R+'CLOSING_RESULT.json'))&&v.phase==='PRESEAL_TEN_PAYLOADS'&&v.status==='PASS_CANONICAL_DOCUMENTARY_CLOSURE','WHOLE_PRESEAL_RAW');pairs++;
 v.keys.forEach(key);
 need(Buffer.from(payload.slice().sort().map(n=>sha(read(R+n))+'  '+n+'\n').join('')).equals(read(R+'SHA256SUMS')),'WHOLE_TWELVE_PAYLOAD_NONSELF_MANIFEST');
}
const payloads=payload.slice().sort().map(n=>({name:n,bytes:read(R+n).length,sha256:sha(read(R+n))}));
process.stdout.write(JSON.stringify({status:'PASS_CANONICAL_DOCUMENTARY_CLOSURE',phase:final?'FINAL_TWELVE_PAYLOADS':'PRESEAL_TEN_PAYLOADS',checks:r.checks,key_count:keys.size,total_read_bytes:r.total,entire_prior_keys:old,complete_raw_pairs:pairs,payloads,payload_bytes:payloads.reduce((s,p)=>s+p.bytes,0),science_execution:false,new_copy:false,new_grant:false,keys:[...keys.values()]},null,2)+'\n');
