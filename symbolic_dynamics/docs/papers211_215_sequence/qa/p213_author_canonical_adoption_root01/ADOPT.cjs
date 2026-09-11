'use strict';
// Separate exact copy grant. No producer/source/host execution or target discovery.
const fs=require('node:fs'),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const Q='docs/papers211_215_sequence/qa/',R=Q+'p213_author_canonical_adoption_root01/',D=Q+'p213_initial_science_data_root01/';
const source=Q+'p213_initial_science_run01/stdout.bin',target='papers/213-receiver-limited-cyclic-transfer/canonical_stdout.txt';
const priorNames=['CHECK_NATIVE.json','CHECK_ROOT.cjs','CLOSE.cjs','CLOSING_NATIVE.json','CLOSING_RESULT.json','INPUT_SPEC.json','RECEPTION.md','REPLAY_NATIVE.json','RESULT.json','ROOT_READS_NATIVE.json'];
const own=['ADOPT.cjs','GRANT.json','CONSUMPTION.json','ROOT_READS_NATIVE.json'];
const mode=process.argv[2],receive=mode==='--receive';
const allowed=new Set([...priorNames.map(n=>D+n),D+'SHA256SUMS',...own.map(n=>R+n),Q+'p213_initial_science_enabled_root01/READ_FIXED.cjs',source,...(receive?[target,R+'ADOPT_NATIVE.json',R+'ADOPT_RESULT.json']:[])]);
const r=make(allowed),{need,read,sha,equal,keys}=r;
const report={status:'RUNNING',mode,actions:[],science_execution:false,strict_pair_grant:false,source_normalized:false,failure:null};
try{
 need(process.argv.length===3&&['--adopt','--receive'].includes(mode)&&process.cwd()==='/root/autodl-tmp/symbolic_dynamics','EXACT_SCOPED_MODE_CWD');
 for(const p of allowed)read(p);
 const g=JSON.parse(read(R+'GRANT.json')),c=JSON.parse(read(R+'CONSUMPTION.json'));
 need(g.id==='P213_AUTHOR_CANONICAL_EXACT_COPY_01'&&g.permitted_copy_submissions===1&&g.source.path===source&&g.target===target,'EXACT_NEW_COPY_GRANT');
 need(c.grant_id===g.id&&c.status==='CONSUMED_BEFORE_NATIVE_SUBMISSION'&&c.remaining_submissions===0,'DISTINCT_GRANT_ALREADY_CONSUMED_FOR_ONE_SUBMISSION');
 need(sha(read(D+'SHA256SUMS'))===g.initial_data_receipt.seal&&sha(read(D+'RECEPTION.md'))===g.initial_data_receipt.sha256,'EXACT_ACCEPTED_INITIAL_DATA_RECEIPT');
 need(sha(read(Q+'p213_initial_science_enabled_root01/READ_FIXED.cjs'))==='f3faa0a29e91dd56ace36b3e7d1dd54f11e97064122c1a9b2c77b20edc6667c7','EXACT_ORDINARY_READER');
 const manifest=priorNames.slice().sort().map(n=>sha(read(D+n))+'  '+n+'\n').join('');
 need(Buffer.from(manifest).equals(read(D+'SHA256SUMS')),'WHOLE_TEN_PAYLOAD_NONSELF_SEAL');
 need(equal(fs.readdirSync(D).sort(),[...priorNames,'SHA256SUMS'].sort()),'ENTIRE_FIXED_PRIOR_LAYOUT');
 const n=JSON.parse(read(D+'CHECK_NATIVE.json')),v=JSON.parse(read(D+'RESULT.json'));
 need(n.result.exit_code===0&&n.result.chunk_id==='c05de0'&&!n.result.session_id,'ACTUAL_ACCEPTED_INITIAL_DATA_ROOT_NATIVE');
 need(Buffer.from(n.result.output).equals(read(D+'RESULT.json'))&&v.status==='PASS_ROOT_ORIGINAL_INITIAL_CONTROL_AND_BOUNDED_SCIENCE_DATA','WHOLE_ROOT_RESULT_RAW');
 const old=v.keys.find(k=>k.path===source);need(!!old&&equal(old,keys.get(source)),'ENTIRE_ACCEPTED_CURRENT_RAW_SOURCE_KEY');
 need(read(source).length===g.source.bytes&&sha(read(source))===g.source.sha256,'ENTIRE_ACCEPTED_ORIGINAL_SCIENTIFIC_STDOUT');
 const rawkey=keys.get(source);
 need(rawkey.lstat_before.nlink==='1'&&rawkey.lstat_before.mode==='33152'&&rawkey.lstat_before.uid==='0','PHYSICAL_PRIVATE_RAW_SOURCE');
 if(!receive){
   try{fs.lstatSync(target);throw Error('CANONICAL_EXISTS_REFUSE_WITHOUT_OVERWRITE');}
   catch(e){if(e.code!=='ENOENT')throw e;report.target_before={path:target,lstat_errno:'ENOENT'};}
   const action={operation:'copyFileSync',source,target,flags:'COPYFILE_EXCL',attempted:true,success:false};report.actions.push(action);
   fs.copyFileSync(source,target,fs.constants.COPYFILE_EXCL);action.success=true;
 }
 const after=make(new Set([source,target])),afterSource=after.read(source),adopted=after.read(target);
 need(equal(keys.get(source),after.keys.get(source)),'ALL_SOURCE_KEY_FIELDS_UNCHANGED_ACROSS_COPY_OR_RECEIPT');
 need(read(source).equals(afterSource)&&afterSource.equals(adopted),'ENTIRE_ORIGINAL_SOURCE_AND_TARGET_RAW_EQUAL');
 const a=after.keys.get(source).lstat_before,b=after.keys.get(target).lstat_before;
 need(a.dev!==b.dev||a.ino!==b.ino,'DISTINCT_PHYSICAL_CANONICAL_COPY');
 need(b.nlink==='1'&&b.mode==='33152'&&b.uid==='0','PHYSICAL_PRIVATE_SINGLE_LINK_CANONICAL');
 report.source_key=after.keys.get(source);report.canonical_key=after.keys.get(target);
 report.raw_comparison={source,target,bytes:adopted.length,sha256:after.sha(adopted),raw_equal:true};
 report.after_read_checks=after.checks;report.after_read_bytes=after.total;
 if(receive){
   const an=JSON.parse(read(R+'ADOPT_NATIVE.json')),av=JSON.parse(read(R+'ADOPT_RESULT.json'));
   need(an.result.exit_code===0&&!an.result.session_id&&equal(an.request,g.request),'EXACT_ACTUAL_SINGLE_COPY_NATIVE');
   need(Buffer.from(an.result.output).equals(read(R+'ADOPT_RESULT.json')),'ENTIRE_ACTUAL_ADOPTION_STDOUT_RAW');
   need(av.status==='PASS_EXACT_CANONICAL_RAW_COPY'&&av.actions.length===1&&av.actions[0].success===true&&av.target_before.lstat_errno==='ENOENT','ACTUAL_EXCLUSIVE_COPY_SUCCESS');
   need(equal(av.source_key,report.source_key)&&equal(av.canonical_key,report.canonical_key),'ENTIRE_ACTUAL_COPY_CURRENT_SOURCE_TARGET_KEYS');
   for(const k of av.keys)need(keys.has(k.path)&&equal(k,keys.get(k.path)),'ALL_ADOPTION_PRIOR_DOCUMENT_KEYS');
 }
 report.status=receive?'PASS_READ_ONLY_EXACT_CANONICAL_ADOPTION_RECEPTION':'PASS_EXACT_CANONICAL_RAW_COPY';
}catch(e){report.status='FAIL_COPY_OR_RECEIPT_PRESERVE_HOLD';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=r.checks;report.key_count=keys.size;report.total_read_bytes=r.total;report.keys=[...keys.values()];
process.stdout.write(JSON.stringify(report,null,2)+'\n');
