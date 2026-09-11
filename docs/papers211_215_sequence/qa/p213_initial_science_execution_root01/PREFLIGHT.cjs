'use strict';
// Only exact local source/document pins, one future capture ENOENT and capacity.
const fs=require('node:fs'),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const Q='docs/papers211_215_sequence/qa/',E=Q+'p213_initial_science_enabled_root01/',M=Q+'p213_initial_science_materialization_root01/',P=Q+'p213_initial_science_enabled_preparation01/',R=Q+'p213_initial_science_execution_root01/',S='papers/213-receiver-limited-cyclic-transfer/';
const target=Q+'p213_initial_science_enabled01/run_science.py',capture=Q+'p213_initial_science_run01';
const docs=[E+'READ_FIXED.cjs',E+'RECEPTION.md',E+'SHA256SUMS',E+'CHECK_NATIVE.json',M+'RECEIPT.md',M+'SHA256SUMS',M+'CHECK_NATIVE.json',target,P+'REQUEST.initial.proposed.json',P+'capture.initial.proposed.sh.txt',R+'GRANT.json',R+'PREFLIGHT.cjs',S+'verify.py',S+'VERIFICATION_PARAMETERS.json',S+'OUTPUT_SCHEMA.md',S+'SCIENTIFIC_DEPENDENCIES.md',S+'RUNTIME_PLAN.md',S+'REVIEW_INTERFACES.md'];
const r=make(new Set(docs)),{need,read,sha,equal,keys}=r;
const report={scope:'EXACT_SINGLE_INITIAL_SCIENCE_PREFLIGHT_ONLY',status:'RUNNING',science_executed:false,host_runtime_inputs_queried:false};
try{
 need(process.argv.length===2&&process.cwd()==='/root/autodl-tmp/symbolic_dynamics','FIXED_CONTEXT');
 for(const p of docs)read(p);
 const grant=JSON.parse(read(R+'GRANT.json'));
 need(grant.id==='P213_INITIAL_SCIENCE_SINGLE_RUN_01'&&grant.status==='GRANTED_SUBJECT_TO_EXACT_PREFLIGHT_UNCONSUMED'&&grant.consumed===false&&grant.permitted_native_submissions===1,'NEW_UNCONSUMED_GRANT');
 need(sha(read(E+'RECEPTION.md'))===grant.source_acceptance.sha256&&sha(read(E+'SHA256SUMS'))===grant.source_acceptance.seal,'ROOT_SOURCE_RECEPTION_PIN');
 need(sha(read(M+'RECEIPT.md'))===grant.materialization.sha256&&sha(read(M+'SHA256SUMS'))===grant.materialization.seal,'MATERIALIZATION_ACCEPTED_PINS');
 need(sha(read(E+'READ_FIXED.cjs'))==='f3faa0a29e91dd56ace36b3e7d1dd54f11e97064122c1a9b2c77b20edc6667c7','PINNED_ORDINARY_DOCUMENT_READER');
 const previous=JSON.parse(JSON.parse(read(E+'CHECK_NATIVE.json')).result.output);
 const material=JSON.parse(JSON.parse(read(M+'CHECK_NATIVE.json')).result.output);
 need(equal(keys.get(target),material.materialized_source_key),'WHOLE_CURRENT_WRAPPER_KEY');
 for(const name of ['verify.py','VERIFICATION_PARAMETERS.json','OUTPUT_SCHEMA.md','SCIENTIFIC_DEPENDENCIES.md','RUNTIME_PLAN.md','REVIEW_INTERFACES.md']){
   const p=S+name;need(equal(keys.get(p),previous.keys.find(k=>k.path===p)),'ALL_CURRENT_SCIENTIFIC_DOCUMENT_KEYS');
 }
 const request=JSON.parse(read(P+'REQUEST.initial.proposed.json'));
 need(equal(grant.native_request,request.proposed_native_request),'EXACT_ACCEPTED_COMPLETE_NATIVE_REQUEST');
 need(Buffer.from(grant.native_request.arguments.cmd).equals(read(P+'capture.initial.proposed.sh.txt')),'FULL_CAPTURE_CMD_RAW_EQUAL');
 try{fs.lstatSync(capture);throw Error('UNEXPECTED_EXISTING_CAPTURE_DIRECTORY');}catch(e){if(e.code!=='ENOENT')throw e;}
 const parent=fs.lstatSync(Q,{bigint:true});need(parent.isDirectory()&&!parent.isSymbolicLink(),'EXACT_CAPTURE_PARENT');
 const s=fs.statfsSync('.',{bigint:true}),available=s.bavail*s.bsize;need(available>=134217728n,'CURRENT_MINIMUM_CAPTURE_CAPACITY');
 report.output_directory={path:capture,actual_lstat_errno:'ENOENT',parent:Q};
 report.capacity={available_bytes:available.toString(),minimum_bytes:'134217728',bavail:s.bavail.toString(),bsize:s.bsize.toString(),reservation:false};
 report.accepted_actual_wrapper_key=keys.get(target);report.exact_native_request=grant.native_request;
 report.status='PASS_PREFLIGHT_FOR_DISTINCT_SINGLE_INITIAL_SUBMISSION';
}catch(e){report.status='FAIL_PREFLIGHT_NO_SCIENCE_SUBMITTED';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=r.checks;report.key_count=keys.size;report.total_read_bytes=r.total;report.keys=[...keys.values()];
process.stdout.write(JSON.stringify(report,null,2)+'\n');
