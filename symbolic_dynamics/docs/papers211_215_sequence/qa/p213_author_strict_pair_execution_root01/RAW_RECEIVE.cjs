'use strict';
// Complete already-created raw DATA only. No producer/science/host-path execution.
const fs=require('node:fs'),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const Q='docs/papers211_215_sequence/qa/',R=Q+'p213_author_strict_pair_execution_root01/',P=Q+'p213_initial_science_enabled_preparation01/',E=Q+'p213_initial_science_enabled_root01/',M=Q+'p213_initial_science_materialization_root01/',D=Q+'p213_initial_science_data_root01/',C=Q+'p213_author_canonical_adoption_root01/',I=Q+'p213_initial_science_execution_root01/',S='papers/213-receiver-limited-cyclic-transfer/';
const stage=process.argv[2],num=stage==='replay01'?'01':stage==='replay02'?'02':null;
if(process.argv.length!==3||!num)throw Error('EXACT_DISTINCT_RAW_STAGE');
const raw=Q+'p213_author_strict_pair_run'+num+'/',wrapper=Q+'p213_initial_science_enabled01/run_science.py',canonical=S+'canonical_stdout.txt',initial=Q+'p213_initial_science_run01/stdout.bin',parser=Q+'p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs';
const scienceNames=['verify.py','VERIFICATION_PARAMETERS.json','OUTPUT_SCHEMA.md','SCIENTIFIC_DEPENDENCIES.md','RUNTIME_PLAN.md','REVIEW_INTERFACES.md'];
const docs=[R+'PREFLIGHT.cjs',R+'GRANT.'+stage+'.json',E+'READ_FIXED.cjs',E+'RECEPTION.md',E+'SHA256SUMS',E+'CHECK_NATIVE.json',M+'RECEIPT.md',M+'SHA256SUMS',M+'CHECK_NATIVE.json',D+'RECEPTION.md',D+'SHA256SUMS',C+'RECEIPT.md',C+'SHA256SUMS',C+'RECEIVE_NATIVE.json',C+'RECEIVE_RESULT.json',I+'PREFLIGHT_NATIVE.json',P+'REQUEST.'+stage+'.proposed.json',P+'capture.'+stage+'.proposed.sh.txt',wrapper,canonical,initial,...scienceNames.map(n=>S+n),R+'PREFLIGHT.'+stage+'.NATIVE.json',R+'CONSUMPTION.'+stage+'.json',R+'ACTUAL.'+stage+'.NATIVE.json',R+'RAW_RECEIVE.cjs',R+'PARSER_READ_NATIVE.json',parser,...['stdout.bin','stderr.bin','runtime_control.bin'].map(n=>raw+n)];
const r=make(new Set(docs)),{need,read,equal,sha,keys}=r;
const report={scope:'COMPLETE_ACTUAL_STRICT_RAW_BYTES_AND_CURRENT_SOURCE_KEYS_ONLY_FULL_CONTROL_AUDIT_PENDING',stage,status:'RUNNING',science_rerun:false,control_semantics_accepted:false,strict_pair_accepted:false};
try{
 need(process.cwd()==='/root/autodl-tmp/symbolic_dynamics','FIXED_CONTEXT');docs.forEach(read);
 need(sha(read(E+'READ_FIXED.cjs'))==='f3faa0a29e91dd56ace36b3e7d1dd54f11e97064122c1a9b2c77b20edc6667c7','CURRENT_TRUSTED_DOCUMENT_READER');
 need(sha(read(parser))==='9d6e081b7c8940f6730cc41c62bfc67862738eb49ded8f4021b6875583120471','EXACT_FULLY_READ_PURE_LOSSLESS_PARSER');
 const {parseIntegerJSON,canonicalIntegerJSON}=require('../p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs');
 const g=JSON.parse(read(R+'GRANT.'+stage+'.json')),c=JSON.parse(read(R+'CONSUMPTION.'+stage+'.json')),n=JSON.parse(read(R+'ACTUAL.'+stage+'.NATIVE.json'));
 need(g.id==='P213_AUTHOR_STRICT_PAIR_NEW_RUN_'+num&&g.stage===stage&&c.grant_id===g.id&&c.remaining_submissions===0&&c.status==='CONSUMED_BEFORE_NATIVE_SUBMISSION','DISTINCT_CONSUMED_SINGLE_USE_GRANT');
 need(equal(n.request,g.native_request.arguments)&&equal(c.exact_native_request,g.native_request),'ENTIRE_BOUND_ACTUAL_NATIVE_REQUEST');
 need(n.tool==='exec_command'&&n.result.exit_code===0&&!n.result.session_id&&Array.isArray(n.continuations)&&n.continuations.length===0,'ACTUAL_SETTLED_ZERO_NO_SESSION_SUBMISSION');
 need(Buffer.from(n.result.output).equals(Buffer.from('P213_SCIENCE_NATIVE_EXIT=0\n')),'ENTIRE_ACTUAL_NATIVE_STATUS_STDOUT');
 const pn=JSON.parse(read(R+'PREFLIGHT.'+stage+'.NATIVE.json')),pv=JSON.parse(pn.result.output);
 need(pn.result.exit_code===0&&!pn.result.session_id&&pn.result.chunk_id===c.preflight_actual_chunk_id&&pv.stage===stage&&pv.status==='PASS_CURRENT_PREFLIGHT_FOR_NEW_DISTINCT_STRICT_RUN','ACTUAL_PRIOR_CURRENT_PREFLIGHT');
 need(equal(pv.exact_native_request,g.native_request)&&pv.output_directory.actual_lstat_errno==='ENOENT','COMPLETE_PREFLIGHT_REQUEST_AND_ABSENCE');
 for(const k of pv.keys)need(keys.has(k.path)&&equal(k,keys.get(k.path)),'ALL_ENTIRE_PREFLIGHT_KEYS_UNCHANGED_AFTER_SCIENCE');
 need(equal(keys.get(canonical),g.canonical_pin)&&read(canonical).equals(read(initial)),'COMPLETE_CANONICAL_KEY_AND_ORIGINAL_RAW_STILL_EQUAL');
 const dir=fs.lstatSync(raw,{bigint:true});need(dir.isDirectory()&&!dir.isSymbolicLink()&&(dir.mode&0o7777n)===0o700n&&dir.uid===0n,'EXACT_CREATED_PRIVATE_CAPTURE_DIRECTORY');
 const members=fs.readdirSync(raw).sort();need(equal(members,['runtime_control.bin','stderr.bin','stdout.bin']),'EXACT_THREE_CREATED_RAW_MEMBERS');
 for(const name of ['stdout.bin','stderr.bin','runtime_control.bin']){
  const k=keys.get(raw+name),m=k.lstat_before;need(m.mode==='33152'&&m.nlink==='1'&&m.uid==='0'&&m.gid==='0','PHYSICAL_PRIVATE_SINGLE_LINK_COMPLETE_RAW_KEY');
 }
 const out=read(raw+'stdout.bin'),err=read(raw+'stderr.bin'),control=read(raw+'runtime_control.bin');
 need(out.equals(read(canonical))&&out.equals(read(initial)),'ENTIRE_STRICT_SCIENCE_RAW_EQUALS_CANONICAL_AND_INITIAL');
 need(err.length===0,'EMPTY_ACTUAL_STDERR');
 need(out.every(c=>c<128)&&out.at(-1)===10&&control.every(c=>c<128)&&control.at(-1)===10,'COMPLETE_ASCII_RAW_FRAMING');
 const parsed=parseIntegerJSON(control.toString('ascii')),reencoded=Buffer.from(canonicalIntegerJSON(parsed.data)+'\n','ascii');
 need(reencoded.equals(control),'ENTIRE_CONTROL_LOSSLESS_INTEGER_RAW_ROUNDTRIP');
 const after=fs.lstatSync(raw,{bigint:true});need(equal(r.stat(dir),r.stat(after)),'WHOLE_CAPTURE_DIRECTORY_POINT_KEYS_UNCHANGED');
 report.actual_scientific_native_chunk_id=n.result.chunk_id;report.prior_entire_key_count=pv.keys.length;
 report.raw_keys=['stdout.bin','stderr.bin','runtime_control.bin'].map(n=>keys.get(raw+n));
 report.canonical_raw_comparison={bytes:out.length,sha256:sha(out),raw_equal:true,normalization:false};
 report.control_integer_counts=parsed.counts;report.control_reported_status=parsed.data.status;report.control_top_fields=Object.keys(parsed.data);
 report.reported_before_file_count=Object.keys(parsed.data.before_keys||{}).length;report.reported_after_file_count=Object.keys(parsed.data.after_keys||{}).length;
 report.stdout_line_count=out.reduce((n,c)=>n+(c===10),0);
 report.capture_directory={path:raw,before:r.stat(dir),after:r.stat(after),members};
 report.status='PASS_COMPLETE_STRICT_RAW_BYTES_PENDING_INDEPENDENT_CONTROL_AND_PAIR_RECEPTION';
}catch(e){report.status='FAIL_STRICT_RAW_RECEPTION_PRESERVE_HOLD';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=r.checks;report.key_count=keys.size;report.total_read_bytes=r.total;report.keys=[...keys.values()];
process.stdout.write(JSON.stringify(report,null,2)+'\n');
