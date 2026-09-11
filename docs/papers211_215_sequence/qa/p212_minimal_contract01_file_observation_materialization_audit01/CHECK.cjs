'use strict';
// Fixed documentary/copy reception only. Never import any received program.
// Runtime-directory records are DATA from the explicitly permitted live calls.
const fs=require('node:fs'),{createHash}=require('node:crypto');
const P='docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_';
const SOURCE=P+'materialization01/',OWN=P+'materialization_audit01/',AUTHOR=P+'preparation01/';
const ENABLED=P+'enabled01',RAW=P+'raw01';
const FIELDS=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const META=['lstat_before','fstat_before','fstat_after','lstat_after'];
const FIXED=[
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/file_keys.proposed.mjs.txt",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/collect_files.proposed.mjs.txt",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/capture.proposed.sh.txt",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/FILE_REQUEST.proposed.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/ENTRY_REQUEST.proposed.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_audit01/REPORT.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_audit01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_root01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_enabled01/file_keys.mjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_enabled01/collect_files.mjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/CHECK.cjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/CLOSE.cjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/CLOSING_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/CLOSING_RESULT.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/HANDOFF.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/MATERIALIZE_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/MATERIALIZE_RESULT.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/ORIGIN.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/PREFLIGHT_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/PREFLIGHT_RESULT.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/READ_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_materialization01/SHA256SUMS"
];
const OWN_INPUTS=['INPUT_PINS.json','READ_NATIVE.json','PREFLIGHT_REPLAY_NATIVE.json','SEALED_REPLAY_NATIVE.json','FINDINGS.json','ORIGIN.md','REVIEW.md','CHECK.cjs'];
const BASE=['CHECK.cjs','HANDOFF.md','MATERIALIZE_NATIVE.json','MATERIALIZE_RESULT.json','ORIGIN.md','PREFLIGHT_NATIVE.json','PREFLIGHT_RESULT.json','READ_NATIVE.json','CLOSE.cjs'].sort();
const SOURCE_PAYLOAD=[...BASE,'CLOSING_NATIVE.json','CLOSING_RESULT.json'].sort();
const allowed=new Set([...FIXED,...OWN_INPUTS.map(x=>OWN+x)]);
const files=new Map(),current=new Map(),report={schema:'p212-materialization-independent-fixed-reception-v1',status:'FAILED_PARTIAL_PRESERVED',checks:0,keys:[],named_checks:{},raw_comparisons:[],rich_key_occurrences:[],directory_occurrences:[],json_trees:[],numeric_tokens:0,json_nodes:0,failure:null,source_execution:false,candidate_observation:false,binding_materialized:false,observation_grant:false,operation_permission:false,direct_runtime_directory_queries:0,old_two_grants:'consumed',trust:'Ordinary Node/fs/crypto/root bootstrap and unscanned ancestors adopted; ten fields only, no native14 or directory-handle identity.'};
const need=(v,s)=>{report.checks++;if(!v)throw Error(s);};
const equal=(a,b,s)=>need(JSON.stringify(a)===JSON.stringify(b),s);
const mark=(k,v=true)=>{need(!Object.hasOwn(report.named_checks,k),'unique named check');report.named_checks[k]=v;};
const pin=b=>({bytes:b.length,sha256:createHash('sha256').update(b).digest('hex')});
const err=e=>({name:String(e?.name??'Error'),code:typeof e?.code==='string'?e.code:null,message:String(e?.message??e)});
function fields(s){return Object.fromEntries(FIELDS.map(k=>{need(typeof s[k]==='bigint','actual bigint '+k);return[k,s[k].toString()];}));}
function read(path){
 need(allowed.has(path),'fixed documentary/copy path only');
 const row={path,lstat_before:null,fstat_before:null,fstat_after:null,lstat_after:null,fd:null,reads:[],bytes_read:0,eof:false,content:null,close_succeeded:null,error:null,close_error:null};
 report.keys.push(row);let fd=null;const chunks=[];
 try{
  const l=fs.lstatSync(path,{bigint:true});row.lstat_before=fields(l);
  need(l.isFile()&&!l.isSymbolicLink()&&l.size>=0n&&l.size<=8388608n,'bounded physical regular leaf');
  fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);row.fd=fd;
  const s=fs.fstatSync(fd,{bigint:true});row.fstat_before=fields(s);need(s.isFile(),'opened regular file');equal(row.lstat_before,row.fstat_before,'same opened descriptor before');
  const block=Buffer.alloc(65536);
  for(;;){const requested=Math.min(block.length,8388609-row.bytes_read);need(requested>0,'positive request');
   const returned=fs.readSync(fd,block,0,requested,null);row.reads.push({requested,returned});
   if(returned===0){row.eof=true;break;}chunks.push(Buffer.from(block.subarray(0,returned)));row.bytes_read+=returned;need(row.bytes_read<=8388608,'bounded complete read');}
  const bytes=Buffer.concat(chunks);row.content=pin(bytes);need(BigInt(bytes.length)===s.size,'actual EOF entire size');
  row.fstat_after=fields(fs.fstatSync(fd,{bigint:true}));row.lstat_after=fields(fs.lstatSync(path,{bigint:true}));
  equal(row.fstat_before,row.fstat_after,'same opened descriptor after');equal(row.lstat_before,row.lstat_after,'same lexical leaf after');
  need(Buffer.from(bytes.toString('utf8'),'utf8').equals(bytes),'UTF8 reversible');
  files.set(path,bytes);current.set(path,row);
 }catch(e){row.error=err(e);throw e;}
 finally{if(fd!==null){try{fs.closeSync(fd);row.close_succeeded=true;}catch(e){row.close_succeeded=false;row.close_error=err(e);throw e;}}}
 need(row.eof&&row.close_succeeded===true,'actual closed EOF');return row;
}
function tree(a,b,label){
 report.json_nodes++;need(typeof a===typeof b&&Array.isArray(a)===Array.isArray(b),'JSON type '+label);
 if(a===null||b===null||typeof a!=='object'){need(Object.is(a,b),'JSON scalar '+label);return;}
 equal(Object.keys(a),Object.keys(b),'complete JSON keys '+label);
 for(const k of Object.keys(a))tree(a[k],b[k],label+'/'+k);
}
function parse(raw,label){
 const text=Buffer.isBuffer(raw)?raw.toString('utf8'):raw;
 const re=/-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?/y;
 for(let i=0;i<text.length;){
  if(text[i]==='"'){i++;while(i<text.length){if(text[i]==='\\'){i+=2;continue;}if(text[i++]==='"')break;}continue;}
  if(text[i]==='-'||/[0-9]/.test(text[i])){re.lastIndex=i;const m=re.exec(text);need(!!m,'JSON number token');
   const n=Number(m[0]);need(Number.isFinite(n)&&(!Number.isInteger(n)||Number.isSafeInteger(n)),'safe numeric token');
   if(!/[.eE]/.test(m[0]))need(BigInt(m[0])===BigInt(n),'exact integral token');
   report.numeric_tokens++;i=re.lastIndex;continue;}i++;
 }
 const v=JSON.parse(text);tree(v,JSON.parse(JSON.stringify(v)),label);report.json_trees.push({label,...pin(Buffer.from(text,'utf8'))});return v;
}
const json=p=>parse(files.get(p),p);
function raw(a,b,label){a=Buffer.isBuffer(a)?a:Buffer.from(a,'utf8');b=Buffer.isBuffer(b)?b:Buffer.from(b,'utf8');need(a.equals(b),'whole RAW '+label);report.raw_comparisons.push({label,...pin(a),raw_equal:true});}
function native(n,label,expectedCommand){
 need(n.tool==='exec_command'&&n.request&&n.result,'whole native shape '+label);
 equal(Object.keys(n.result).sort(),['chunk_id','wall_time_seconds','exit_code','original_token_count','output'].sort(),'complete native result fields '+label);
 need(typeof n.request.cmd==='string'&&typeof n.result.chunk_id==='string'&&Number.isInteger(n.result.exit_code)&&Number.isInteger(n.result.original_token_count)&&typeof n.result.wall_time_seconds==='number'&&typeof n.result.output==='string','complete native field types '+label);
 if(expectedCommand!==undefined){need(n.request.cmd===expectedCommand&&n.request.workdir==='/root/autodl-tmp/symbolic_dynamics','exact native request '+label);need(n.result.exit_code===0,'settled passing native '+label);}
}
function decimalRecord(x,label){equal(Object.keys(x),FIELDS,'exact ten-field set/order '+label);for(const k of FIELDS)need(typeof x[k]==='string'&&/^-?(0|[1-9][0-9]*)$/.test(x[k])&&x[k]!=='-0','exact decimal field '+label+'/'+k);}
function rich(x,label){
 const now=current.get(x.path);need(!!now,'historical/current fixed key present '+label);
 const wanted=['path',...(Object.hasOwn(x,'phase')?['phase']:[]),...META,'fd','reads','bytes_read','eof','content','close_succeeded','error','close_error'];
 equal(Object.keys(x),wanted,'all complete key fields '+label);
 for(const k of META){decimalRecord(x[k],label+'/'+k);equal(x[k],now[k],'whole metadata '+label+'/'+k);}
 for(const k of ['content','bytes_read','eof','close_succeeded','error','close_error'])equal(x[k],now[k],'whole key endpoint '+label+'/'+k);
 need(Number.isSafeInteger(x.fd)&&x.fd>=0&&x.reads.length>0,'retained actual descriptor/read list');
 let total=0;x.reads.forEach((q,i)=>{equal(Object.keys(q),['requested','returned'],'complete read-call fields');need(Number.isSafeInteger(q.requested)&&q.requested>0&&Number.isSafeInteger(q.returned)&&q.returned>=0&&q.returned<=q.requested,'actual read-call integers');need(i===x.reads.length-1?q.returned===0:q.returned>0,'sole terminal actual zero');total+=q.returned;});
 need(total===x.bytes_read&&x.eof&&x.close_succeeded&&x.error===null&&x.close_error===null,'whole closed-key totals');
 report.rich_key_occurrences.push({label,path:x.path,phase:x.phase??null,fd:x.fd,reads:x.reads,bytes_read:x.bytes_read});
}
function collectRich(v,label){if(v&&typeof v==='object'){if(META.every(k=>Object.hasOwn(v,k))&&Object.hasOwn(v,'reads'))rich(v,label);for(const[k,x]of Object.entries(v))collectRich(x,label+'/'+k);}}
function directory(d,label,expectedNames){
 const wanted=['path',...(Object.hasOwn(d,'phase')?['phase']:[]),'before','after','names','eof','close_succeeded','error','close_error'];
 equal(Object.keys(d),wanted,'complete directory record fields');
 need([SOURCE.slice(0,-1),ENABLED,RAW].includes(d.path),'only archived assigned directory paths');
 decimalRecord(d.before,label+'/before');decimalRecord(d.after,label+'/after');equal(d.before,d.after,'whole lexical endpoints');
 need((BigInt(d.before.mode)&0o170000n)===0o040000n,'recorded directory type');
 if(d.path!==SOURCE.slice(0,-1))need((BigInt(d.before.mode)&0o7777n)===0o700n&&d.before.uid==='0'&&d.before.gid==='0','recorded exact runtime0700 ownership');
 equal(d.names,[...expectedNames].sort(),'entire expected directory member set');
 need(d.eof===true&&d.close_succeeded===true&&d.error===null&&d.close_error===null,'actual directory EOF/close');
 report.directory_occurrences.push({label,record:d});
}
function seal(path,count,selected){
 const s=files.get(path).toString('utf8');need(s.endsWith('\n'),'seal LF');
 const m=new Map();for(const l of s.slice(0,-1).split('\n')){const q=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);need(q&&!m.has(q[2])&&q[2]!=='SHA256SUMS','strict leaf nonself seal');m.set(q[2],q[1]);}
 need(m.size===count,'declared complete seal line count');
 for(const p of selected)need(m.get(p.split('/').at(-1))===current.get(p).content.sha256,'selected member seal binding');return m;
}
try{
 need(process.argv.length===2&&process.cwd()==='/root/autodl-tmp/symbolic_dynamics','exact fixed read-only invocation');
 need(process.getuid()===0&&process.getgid()===0,'adopted root-key tool owner');
 [...FIXED,...OWN_INPUTS.map(x=>OWN+x)].forEach(read);
 const inputs=json(OWN+'INPUT_PINS.json');equal(inputs.files.map(x=>x.path),FIXED,'all fixed input identities');
 for(const x of inputs.files)equal(current.get(x.path).content,{bytes:x.bytes,sha256:x.sha256},'all pinned file bytes');
 mark('fixed_original_document_and_copy_files',24);mark('current_full_key_count',report.keys.length);
 const sourceBytes=SOURCE_PAYLOAD.reduce((s,n)=>s+files.get(SOURCE+n).length,0)+files.get(SOURCE+'SHA256SUMS').length;
 need(sourceBytes===555691,'whole source physical byte count');
 mark('source_packet_physical_bytes',sourceBytes);
 need(current.get(SOURCE+'SHA256SUMS').content.sha256==='fd642d1a48ad1612ecbae9a3df3ce7b3d2d7242fab3d8659eb342b6f37b71e17','assigned source seal hash');
 raw(files.get(SOURCE+'SHA256SUMS'),SOURCE_PAYLOAD.map(n=>current.get(SOURCE+n).content.sha256+'  '+n+'\n').join(''),'whole source eleven-payload nonself seal');
 mark('source_nonself_payloads_and_files',[11,12]);
 const sourceJSON=new Map();
 for(const n of SOURCE_PAYLOAD.filter(n=>n.endsWith('.json')))sourceJSON.set(n,json(SOURCE+n));
 const oldReads=sourceJSON.get('READ_NATIVE.json');
 equal(Object.keys(oldReads),['schema','native','documentary_creation','scope'],'complete original read packet');
 need(oldReads.native.length===4,'four original preparation natives');
 oldReads.native.forEach((n,i)=>{native(n,'original preparation '+i);need(n.result.exit_code===0&&!n.result.output.startsWith('Warning: truncated output'),'original preparatory return success/untruncated');});
 const reports=[];
 for(const[n,r,cmd,status]of [
  ['MATERIALIZE_NATIVE.json','MATERIALIZE_RESULT.json','CHECK.cjs --materialize','MATERIALIZED_ROOT_RECEPTION_PENDING'],
  ['PREFLIGHT_NATIVE.json','PREFLIGHT_RESULT.json','CHECK.cjs --preflight','PASS_READ_ONLY_PREFLIGHT_ROOT_RECEPTION_PENDING'],
  ['CLOSING_NATIVE.json','CLOSING_RESULT.json','CLOSE.cjs --preseal','PASS_PRESEAL_NONSELF_DOCUMENTARY_CLOSURE'],
 ]){
  const nr=sourceJSON.get(n),v=sourceJSON.get(r);native(nr,n,'node '+SOURCE+cmd);
  raw(nr.result.output,files.get(SOURCE+r),n+' vs whole result');
  tree(v,parse(nr.result.output,n+' decoded stdout'),n+' all stdout/result nodes');
  need(v.status===status&&v.failure===null,'original status scope');
  reports.push([r,v]);
 }
 const material=reports[0][1],pref=reports[1][1],oldClose=reports[2][1];
 const livePrefNative=json(OWN+'PREFLIGHT_REPLAY_NATIVE.json'),liveCloseNative=json(OWN+'SEALED_REPLAY_NATIVE.json');
 native(livePrefNative,'actual independent preflight','node '+SOURCE+'CHECK.cjs --preflight');
 native(liveCloseNative,'actual independent sealed','node '+SOURCE+'CLOSE.cjs --sealed');
 const livePref=parse(livePrefNative.result.output,'actual preflight stdout'),liveClose=parse(liveCloseNative.result.output,'actual sealed stdout');
 raw(livePrefNative.result.output,files.get(SOURCE+'PREFLIGHT_RESULT.json'),'whole new preflight vs original canonical');
 raw(liveCloseNative.result.output,JSON.stringify(liveClose,null,2)+'\n','whole actual sealed canonical serialization');
 need(livePref.status==='PASS_READ_ONLY_PREFLIGHT_ROOT_RECEPTION_PENDING'&&liveClose.status==='PASS_FINAL_NONSELF_DOCUMENTARY_CLOSURE'&&livePref.failure===null&&liveClose.failure===null,'current read-only passes');
 reports.push(['actual_preflight',livePref],['actual_sealed',liveClose]);
 mark('actual_preflight_complete_raw_equal',{chunk_id:livePrefNative.result.chunk_id,...pin(Buffer.from(livePrefNative.result.output)),checks:livePref.checks,key_count:livePref.key_count});
 mark('actual_sealed_complete_native_received',{chunk_id:liveCloseNative.result.chunk_id,...pin(Buffer.from(liveCloseNative.result.output)),checks:liveClose.checks,key_count:liveClose.key_count});
 const reportFacts=[[2143,30,406310],[2241,30,547383],[4936,21,549194],[2241,30,547383],[6395,24,643954]];
 const keySetMain=['schema','mode','status','checks','current_uid','current_gid','keys','directories','absence','actions','comparisons','input_pins','failure','source_execution','candidate_observation','binding_materialized','observation_grant','operation_permission','installed_closure','external_status','directory_handle_identity_attested','unscanned_ancestors_trusted','disposition','key_count','total_read_bytes'];
 const keySetClose=['schema','mode','status','checks','keys','directories','raw_comparisons','historical_keys_compared','payloads','seal','failure','source_execution','operation_permission','observation_grant','binding_materialized','payload_bytes','key_count','total_read_bytes'];
 reports.forEach(([name,v],i)=>{
  equal(Object.keys(v),i===2||i===4?keySetClose:keySetMain,'whole report fields '+name);
  equal([v.checks,v.key_count,v.total_read_bytes],reportFacts[i],'declared actual report counts '+name);
  need(v.keys.length===v.key_count&&v.keys.reduce((s,x)=>s+x.bytes_read,0)===v.total_read_bytes,'all key totals '+name);
  for(const k of ['source_execution','operation_permission','observation_grant','binding_materialized'])need(v[k]===false,'scope false '+name+'/'+k);
  collectRich(v,name);
 });
 mark('all_complete_rich_key_occurrences_compared',report.rich_key_occurrences.length);
 mark('all_five_report_whole_key_sets_received',reports.map(([name,v])=>({name,keys:Object.keys(v)})));
 const docIDs=['reader','entry','capture','file_request','entry_request','author_seal','audit_report','audit_seal','root_receipt','root_seal','materializer','scope','read_native'];
 const docPaths=[...FIXED.slice(0,10),SOURCE+'CHECK.cjs',SOURCE+'ORIGIN.md',SOURCE+'READ_NATIVE.json'];
 const expectedPins=docIDs.map((id,i)=>({id,path:docPaths[i],...current.get(docPaths[i]).content}));
 for(const v of [material,pref,livePref])equal(v.input_pins,expectedPins,'complete thirteen input pins');
 mark('all_thirteen_input_pins_current_and_historical');
 const copies=[ENABLED+'/file_keys.mjs',ENABLED+'/collect_files.mjs'];
 copies.forEach((p,i)=>{
  raw(files.get(docPaths[i]),files.get(p),'complete source/physical copy '+i);
  const a=current.get(docPaths[i]).lstat_before,b=current.get(p).lstat_before;
  need(a.dev!==b.dev||a.ino!==b.ino,'distinct physical copy inode');
  need((BigInt(b.mode)&0o7777n)===0o644n&&b.uid==='0'&&b.gid==='0'&&b.nlink==='1','exact copy mode0644/root/single link');
 });
 mark('two_exact_distinct_physical_source_copies');
 const request=json(AUTHOR+'FILE_REQUEST.proposed.json'),entry=json(AUTHOR+'ENTRY_REQUEST.proposed.json');
 need(request.enabled===false&&request.permission_receipt===null&&request.settlement_receipt===null,'request remains unbound');
 equal(entry.exact_eight_candidates,request.entries,'whole ordered documentary candidate rows only DATA');
 for(const k of ['operation_authorized','operation_permission','observation_accepted','installed_closure_accepted','new_observation_grant_consumed','directory_guard_enabled','help_version_capture_enabled','old_receiver_enabled'])need(entry[k]===false,'unchanged operational hold '+k);
 for(const k of ['request_cmd','operation_request','root_grant','actual_native_request','actual_native_result','actual_session_id','actual_bound_request','actual_bound_request_key','materialization_receipt','new_observation_grant'])need(entry[k]===null,'unchanged documentary null '+k);
 need(entry.old_two_observation_grants==='remain consumed; neither is a new grant','old grants not renewed');
 raw(entry.proposed_native_request.arguments.cmd,files.get(AUTHOR+'capture.proposed.sh.txt'),'complete prospective native command/capture DATA');
 entry.prospective_sources.slice(0,2).forEach((s,i)=>{equal(s.documentary_carrier,{path:docPaths[i],...current.get(docPaths[i]).content,lines:i===0?189:304},'entire documentary source pin');need(s.future_path==='/root/autodl-tmp/symbolic_dynamics/'+copies[i]&&s.actual_future_key===null,'unchanged source mapping metadata');});
 mark('unbound_request_and_both_consumed_grants_preserved');
 seal(AUTHOR+'SHA256SUMS',19,docPaths.slice(0,5));seal(P+'source_audit01/SHA256SUMS',13,[P+'source_audit01/REPORT.md']);seal(P+'source_root01/SHA256SUMS',11,[P+'source_root01/RECEPTION.md']);
 mark('selected_upstream_members_bound_to_19_13_11_seals');
 // Complete original data patch, never executed as a patch or as code.
 const creation=oldReads.documentary_creation;need(creation.tool==='apply_patch'&&creation.request&&typeof creation.request.patch==='string','whole original documentary patch');
 equal(Object.keys(creation.result),[],'actual empty patch result retained');
 const patchLines=creation.request.patch.split('\n');if(patchLines.at(-1)==='')patchLines.pop();
 need(patchLines.shift()==='*** Begin Patch'&&patchLines.pop()==='*** End Patch','full original patch delimiters');
 const rebuilt=new Map();let target=null,payload=[];
 function flush(){if(target!==null){need(!rebuilt.has(target),'unique original patch target');rebuilt.set(target,payload.join('\n')+'\n');}}
 for(const l of patchLines){if(l.startsWith('*** Add File: ')){flush();target=l.slice(14);need([SOURCE+'ORIGIN.md',SOURCE+'CHECK.cjs'].includes(target),'two permitted historical patch targets');payload=[];}else{need(target!==null&&l.startsWith('+'),'only full historical added lines');payload.push(l.slice(1));}}flush();
 need(rebuilt.size===2,'both original creation bodies');for(const[p,b]of rebuilt)raw(b,files.get(p),'entire original apply_patch body '+p);
 mark('original_documentary_creation_received_not_reapplied');
 const originalGroups=[[P+'source_root01/RECEPTION.md',P+'source_root01/SHA256SUMS',AUTHOR+'FILE_REQUEST.proposed.json',AUTHOR+'ENTRY_REQUEST.proposed.json'],[AUTHOR+'file_keys.proposed.mjs.txt',AUTHOR+'collect_files.proposed.mjs.txt',AUTHOR+'capture.proposed.sh.txt']];
 originalGroups.forEach((g,i)=>{need(oldReads.native[i+1].request.cmd==='cat '+g.join(' '),'complete original source-read command');raw(oldReads.native[i+1].result.output,Buffer.concat(g.map(p=>files.get(p))),'complete original source/request read '+i);});
 const initialAbsence=parse(oldReads.native[3].result.output,'initial absence stdout');
 equal(initialAbsence.rows.map(x=>[x.path,x.state,x.error.code]),[[SOURCE.slice(0,-1),'ABSENT','ENOENT'],[ENABLED,'ABSENT','ENOENT'],[RAW,'ABSENT','ENOENT']],'three original absence records');
 equal(material.absence.map(x=>[x.path,x.state,x.error.code]),[[ENABLED,'ABSENT','ENOENT'],[RAW,'ABSENT','ENOENT']],'two mutation-time absence records');
 const expectedActions=[
 {operation:'mkdirSync',path:ENABLED,requested_mode:'0700',recursive:false,success:true,error:null},
 {operation:'mkdirSync',path:RAW,requested_mode:'0700',recursive:false,success:true,error:null},
 ...copies.map((destination,i)=>({operation:'copyFileSync',source:docPaths[i],destination,flags:'COPYFILE_EXCL',success:true,error:null})),
 ];
 equal(material.actions,expectedActions,'every exact original action field');
 for(const v of [pref,livePref]){equal(v.actions,[],'no replay mutation');equal(v.absence,[],'no replay absence query');}
 mark('five_original_ENOENT_and_four_exclusive_actions_DATA_only');
 // Every main-report raw comparison is reconstructed in full.
 const cap={label:'complete proposed native command vs capture carrier',bytes:638,raw_equal:true};
 const whole=(label,path,left,right)=>({label,left:{path,phase:left},right:{path,phase:right},bytes:current.get(path).content.bytes,raw_equal:true});
 for(const v of [material,pref,livePref]){
  const comps=[cap];
  if(v.mode==='--materialize')for(let i=0;i<2;i++)comps.push(whole(docIDs[i]+' immediately before copy',docPaths[i],'before','before_copy_'+docIDs[i]));
  else comps.push({label:'complete materialization native stdout vs full result',bytes:files.get(SOURCE+'MATERIALIZE_RESULT.json').length,raw_equal:true});
  copies.forEach((destination,i)=>comps.push({label:docIDs[i]+' full source/copy RAW comparison',source:docPaths[i],destination,bytes:current.get(destination).content.bytes,raw_equal:true}));
  comps.push(cap);docPaths.forEach((p,i)=>comps.push(whole(docIDs[i]+' entire input before/after',p,'before','after')));
  equal(v.comparisons,comps,'all complete historical/current main raw comparison fields');
 }
 const closeComps=[
 {label:'MATERIALIZE_NATIVE.json whole native stdout/raw result',bytes:78431,raw_equal:true},
 {label:'PREFLIGHT_NATIVE.json whole native stdout/raw result',bytes:74131,raw_equal:true},
 {label:'complete original receipt/request/source/capture read 0',bytes:23939,raw_equal:true},
 {label:'complete original receipt/request/source/capture read 1',bytes:27838,raw_equal:true},
 {label:'whole prospective native command/capture',bytes:638,raw_equal:true},
 {label:'whole original source/physical copy 0',bytes:13660,raw_equal:true},
 {label:'whole original source/physical copy 1',bytes:13540,raw_equal:true},
 ];
 equal(oldClose.raw_comparisons,closeComps,'all seven original closure raw pairs');
 equal(liveClose.raw_comparisons,[...closeComps,{label:'CLOSING_NATIVE.json whole native stdout/raw result',bytes:43469,raw_equal:true},{label:'entire exact eleven-payload nonself manifest',bytes:916,raw_equal:true}],'all nine actual sealed raw pairs');
 mark('all_71_complete_comparison_records_received',material.comparisons.length+pref.comparisons.length+livePref.comparisons.length+oldClose.raw_comparisons.length+liveClose.raw_comparisons.length);
 // Directory observations are received from the two permitted live modes only.
 const memberNames=['collect_files.mjs','file_keys.mjs'];
 reports.forEach(([label,v],i)=>{
  const count=i===0?4:i===1||i===3?2:3;need(v.directories.length===count,'complete directory census '+label);
  v.directories.forEach((d,j)=>{
   const names=d.path===SOURCE.slice(0,-1)?(i===2?BASE:[...SOURCE_PAYLOAD,'SHA256SUMS']):d.phase==='fresh_created'||d.path===RAW?[]:memberNames;
   directory(d,label+'/directories/'+j,names);
  });
  if(v.disposition){
   equal(Object.keys(v.disposition),['enabled_directory','raw_directory','copies','raw_members','binding_path_queried','raw_leaves_queried'],'complete disposition fields');
   for(const[path,k]of [[ENABLED,'enabled_directory'],[RAW,'raw_directory']]){
    const d=v.directories.find(x=>x.path===path&&x.phase==='final_preflight');tree(v.disposition[k],d,'whole duplicate directory disposition');
    directory(v.disposition[k],label+'/disposition/'+k,path===RAW?[]:memberNames);
   }
   equal(v.disposition.raw_members,[],'empty raw disposition');
   need(v.disposition.binding_path_queried===false&&v.disposition.raw_leaves_queried===false,'no future leaves queried');
   equal(v.disposition.copies.map(x=>[x.id,x.path]),copies.map((p,i)=>[docIDs[i],p]),'complete copy disposition identities');
   v.disposition.copies.forEach(x=>tree(x.key,v.keys.find(k=>k.path===x.path&&k.phase==='copy_final'),'complete duplicate copy disposition'));
  }
 });
 const matFinal=path=>material.directories.find(d=>d.path===path&&d.phase==='final_preflight');
 for(const path of [ENABLED,RAW]){
  const final=matFinal(path),fresh=material.directories.find(d=>d.path===path&&d.phase==='fresh_created');
  for(const f of FIELDS.filter(f=>!['size','mtimeNs','ctimeNs'].includes(f)))equal(fresh.before[f],final.before[f],'complete stable created identity '+f);
  if(path===RAW)equal(fresh.before,final.before,'entire raw directory unchanged since creation');
  for(const[,v]of reports.slice(1)){const d=v.directories.find(d=>d.path===path);equal(d.before,final.before,'all current/historical final runtime fields');equal(d.after,final.after,'all current/historical final endpoints');equal(d.names,final.names,'all current/historical final memberships');}
 }
 mark('complete_runtime_directory_records_received_no_new_query');
 mark('runtime_directory_0700_final_records',[matFinal(ENABLED),matFinal(RAW)]);
 equal(oldClose.payloads,BASE.map(name=>({name,...current.get(SOURCE+name).content})),'whole historical nine-payload phase');
 equal(liveClose.payloads,SOURCE_PAYLOAD.map(name=>({name,...current.get(SOURCE+name).content})),'whole current eleven-payload phase');
 need(oldClose.seal===null&&oldClose.historical_keys_compared===60&&liveClose.historical_keys_compared===81,'historical versus final closure scope');
 equal(liveClose.seal,{path:SOURCE+'SHA256SUMS',...current.get(SOURCE+'SHA256SUMS').content},'whole final source seal pin');
 mark('historical_preseal_census_received_not_rerun');
 const reads=json(OWN+'READ_NATIVE.json');need(reads.native.length===11,'all eleven own initial natives');
 for(const n of reads.native)native(n,n.name);
 const readMap=new Map(reads.native.map(x=>[x.name,x]));
 raw(readMap.get('read_handoff').result.output,Buffer.concat([SOURCE+'HANDOFF.md',SOURCE+'ORIGIN.md',P+'source_root01/RECEPTION.md'].map(p=>files.get(p))),'whole independent handoff/origin/root-source read');
 const lineCount=p=>files.get(p).toString('utf8').split('\n').length-1;
 const wc=[SOURCE+'CHECK.cjs',SOURCE+'CLOSE.cjs'].map(p=>String(lineCount(p)).padStart(5,' ')+' '+p+'\n').join('')+String(lineCount(SOURCE+'CHECK.cjs')+lineCount(SOURCE+'CLOSE.cjs')).padStart(5,' ')+' total\n';
 raw(readMap.get('check_source').result.output,wc+files.get(SOURCE+'CHECK.cjs').toString('utf8'),'whole independent materializer source read');
 raw(readMap.get('close_source').result.output,Buffer.concat([files.get(SOURCE+'CLOSE.cjs'),files.get(SOURCE+'SHA256SUMS')]),'whole independent closer and seal read');
 raw(readMap.get('requests_and_source_report').result.output,Buffer.concat([P+'source_audit01/REPORT.md',AUTHOR+'FILE_REQUEST.proposed.json',AUTHOR+'ENTRY_REQUEST.proposed.json'].map(p=>files.get(p))),'whole independent prior report and request read');
 need(readMap.get('archive_semantics').result.chunk_id==='fda1b7'&&readMap.get('archive_semantics').result.output.startsWith('Warning: truncated output (original token count: 14236)'),'actual truncated diagnostic retained');
 need(readMap.get('bounded_semantics').result.chunk_id==='8d12e0'&&!readMap.get('bounded_semantics').result.output.startsWith('Warning: truncated output'),'separate bounded diagnostic not substituted');
 mark('own_diagnostic_truncation_and_missing_bytes_preserved');
 const finding=json(OWN+'FINDINGS.json');need(finding.verdict==='ACCEPT_MATERIALIZATION_ONLY_ROOT_RECEPTION_PENDING'&&finding.open_findings===0,'bounded finding census');
 for(const k of ['critical','major','minor'])equal(finding[k],[],'zero substantive finding');
 for(const k of ['operation_permission','observation_grant','source_execution','binding_materialized','candidate_observation'])need(finding[k]===false,'no expanded authority');
 mark('materialization_only_no_observation_permission');
 mark('original_final_native_not_invented_and_own_actual_sealed_saved');
 report.status='PASS_MATERIALIZATION_ONLY_FIXED_DOCUMENT_COPY_RECEPTION';
}catch(e){report.failure=err(e);process.exitCode=78;}
report.key_count=report.keys.length;report.total_read_bytes=report.keys.reduce((s,x)=>s+x.bytes_read,0);
report.named_check_count=Object.keys(report.named_checks).length;
report.raw_pair_count=report.raw_comparisons.length;report.raw_pair_bytes=report.raw_comparisons.reduce((s,x)=>s+x.bytes,0);
process.stdout.write(JSON.stringify(report,null,2)+'\n');
