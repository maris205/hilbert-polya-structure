'use strict';
// Fixed current local source/document/canonical keys; one exact future absence and capacity.
const fs=require('node:fs'),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const Q='docs/papers211_215_sequence/qa/',R=Q+'p213_author_strict_pair_execution_root01/',P=Q+'p213_initial_science_enabled_preparation01/',E=Q+'p213_initial_science_enabled_root01/',M=Q+'p213_initial_science_materialization_root01/',D=Q+'p213_initial_science_data_root01/',C=Q+'p213_author_canonical_adoption_root01/',I=Q+'p213_initial_science_execution_root01/',S='papers/213-receiver-limited-cyclic-transfer/';
const stage=process.argv[2],num=stage==='replay01'?'01':stage==='replay02'?'02':null;
if(process.argv.length!==3||!num)throw Error('EXACT_DISTINCT_STAGE');
const wrapper=Q+'p213_initial_science_enabled01/run_science.py',output=Q+'p213_author_strict_pair_run'+num,canonical=S+'canonical_stdout.txt',initial=Q+'p213_initial_science_run01/stdout.bin';
const scienceNames=['verify.py','VERIFICATION_PARAMETERS.json','OUTPUT_SCHEMA.md','SCIENTIFIC_DEPENDENCIES.md','RUNTIME_PLAN.md','REVIEW_INTERFACES.md'];
const docs=[R+'PREFLIGHT.cjs',R+'GRANT.'+stage+'.json',E+'READ_FIXED.cjs',E+'RECEPTION.md',E+'SHA256SUMS',E+'CHECK_NATIVE.json',M+'RECEIPT.md',M+'SHA256SUMS',M+'CHECK_NATIVE.json',D+'RECEPTION.md',D+'SHA256SUMS',C+'RECEIPT.md',C+'SHA256SUMS',C+'RECEIVE_NATIVE.json',C+'RECEIVE_RESULT.json',I+'PREFLIGHT_NATIVE.json',P+'REQUEST.'+stage+'.proposed.json',P+'capture.'+stage+'.proposed.sh.txt',wrapper,canonical,initial,...scienceNames.map(n=>S+n)];
const r=make(new Set(docs)),{need,read,sha,equal,keys}=r;
const report={scope:'EXACT_NEW_DISTINCT_AUTHOR_STRICT_RUN_PREFLIGHT',stage,status:'RUNNING',science_executed:false,host_runtime_inputs_queried:false};
try{
 need(process.cwd()==='/root/autodl-tmp/symbolic_dynamics','FIXED_CONTEXT');
 docs.forEach(read);
 const grant=JSON.parse(read(R+'GRANT.'+stage+'.json'));
 need(grant.id==='P213_AUTHOR_STRICT_PAIR_NEW_RUN_'+num&&grant.stage===stage&&grant.permitted_native_submissions===1&&grant.consumed===false,'NEW_STAGE_SPECIFIC_SINGLE_USE_GRANT');
 for(const [g,p,n]of [[grant.source_acceptance,E,'RECEPTION.md'],[grant.materialization,M,'RECEIPT.md'],[grant.initial_data,D,'RECEPTION.md'],[grant.canonical_adoption,C,'RECEIPT.md']])
  need(sha(read(p+n))===g.sha256&&sha(read(p+'SHA256SUMS'))===g.seal,'EXACT_ACCEPTED_PREREQUISITE_RECEIPT_SEAL');
 need(sha(read(E+'READ_FIXED.cjs'))==='f3faa0a29e91dd56ace36b3e7d1dd54f11e97064122c1a9b2c77b20edc6667c7','PINNED_ORDINARY_READER');
 const previous=JSON.parse(JSON.parse(read(E+'CHECK_NATIVE.json')).result.output),material=JSON.parse(JSON.parse(read(M+'CHECK_NATIVE.json')).result.output),initialPre=JSON.parse(JSON.parse(read(I+'PREFLIGHT_NATIVE.json')).result.output);
 need(equal(keys.get(wrapper),material.materialized_source_key)&&equal(keys.get(wrapper),initialPre.accepted_actual_wrapper_key),'ENTIRE_CURRENT_WRAPPER_KEY');
 for(const name of scienceNames){const p=S+name;need(equal(keys.get(p),previous.keys.find(k=>k.path===p))&&equal(keys.get(p),initialPre.keys.find(k=>k.path===p)),'ALL_CURRENT_SCIENTIFIC_DOCUMENT_KEYS');}
 for(const p of [P+'REQUEST.'+stage+'.proposed.json',P+'capture.'+stage+'.proposed.sh.txt'])need(equal(keys.get(p),previous.keys.find(k=>k.path===p)),'COMPLETE_PRIOR_ACCEPTED_STRICT_REQUEST_CAPTURE_KEY');
 const request=JSON.parse(read(P+'REQUEST.'+stage+'.proposed.json'));
 need(equal(grant.native_request,request.proposed_native_request)&&equal(grant.continuation,request.proposed_continuation),'ENTIRE_ACCEPTED_INLINE_REQUEST_AND_CONTINUATION');
 need(Buffer.from(grant.native_request.arguments.cmd).equals(read(P+'capture.'+stage+'.proposed.sh.txt')),'ENTIRE_CAPTURE_CMD_RAW_EQUALS_ACCEPTED_CARRIER');
 need(request.proposed_output_directory==='/root/autodl-tmp/symbolic_dynamics/'+output&&grant.preflight.output_directory===output,'EXACT_DISTINCT_NEW_RUN_PATH');
 const cn=JSON.parse(read(C+'RECEIVE_NATIVE.json')),cv=JSON.parse(read(C+'RECEIVE_RESULT.json'));
 need(cn.result.exit_code===0&&!cn.result.session_id&&Buffer.from(cn.result.output).equals(read(C+'RECEIVE_RESULT.json')),'COMPLETE_ACTUAL_CANONICAL_RECEPTION_NATIVE_RAW');
 need(equal(grant.canonical_pin,cv.canonical_key)&&equal(keys.get(canonical),cv.canonical_key)&&equal(keys.get(initial),cv.source_key),'ENTIRE_CURRENT_CANONICAL_AND_INITIAL_KEYS');
 need(read(canonical).equals(read(initial)),'ENTIRE_SCIENTIFIC_CANONICAL_RAW_UNCHANGED');
 try{fs.lstatSync(output);throw Error('EXISTING_STRICT_RUN_DIRECTORY_REFUSE');}catch(e){if(e.code!=='ENOENT')throw e;}
 const parent=fs.lstatSync(Q,{bigint:true});need(parent.isDirectory()&&!parent.isSymbolicLink(),'EXACT_CAPTURE_PARENT');
 const s=fs.statfsSync('.',{bigint:true}),available=s.bavail*s.bsize;need(available>=134217728n,'CURRENT_CAPTURE_CAPACITY_NOT_RESERVED');
 report.output_directory={path:output,actual_lstat_errno:'ENOENT',parent:Q};
 report.capacity={available_bytes:available.toString(),minimum_bytes:'134217728',bavail:s.bavail.toString(),bsize:s.bsize.toString(),reservation:false};
 report.accepted_actual_wrapper_key=keys.get(wrapper);report.canonical_key=keys.get(canonical);report.exact_native_request=grant.native_request;
 report.status='PASS_CURRENT_PREFLIGHT_FOR_NEW_DISTINCT_STRICT_RUN';
}catch(e){report.status='FAIL_PREFLIGHT_NO_STRICT_SCIENCE_SUBMITTED';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=r.checks;report.key_count=keys.size;report.total_read_bytes=r.total;report.keys=[...keys.values()];
process.stdout.write(JSON.stringify(report,null,2)+'\n');
