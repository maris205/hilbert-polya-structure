'use strict';
// Fixed local documentary reads only. Never import the DATA consumer/observer.
const fs=require('node:fs'),crypto=require('node:crypto');
const BASE='/root/autodl-tmp/symbolic_dynamics/';
const QA='docs/papers211_215_sequence/qa/',P=QA+'p212_minimal_contract01_file_observation_';
const R=P+'execution_root01/',M=P+'materialization_root01/',S=P+'source_root01/';
const A=P+'preparation01/',E=P+'enabled01/',B=P+'binding01/',RAW=P+'raw01/';
const OWN=QA+'p212_eight_file_data_context_preparation01/';
const V=QA+'p212_eight_file_data_receiver_source01/';
const F='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' ');
const SF=['lstat_before','fd_before','fd_after','lstat_after'];
const EXEC_NAMES=['ACTUAL_NATIVE.json','CLOSING_NATIVE.json','CONSUMPTION.json','CREATION_NATIVE.json','GRANT.json','HANDOFF.md','PREFLIGHT.cjs','PREFLIGHT_NATIVE.json','RAW_INPUTS.sha256','RAW_RECEIVE.cjs','RAW_RECEIVE_NATIVE.json'];
const MAT_NAMES=['CHECK_NATIVE.json','RECEPTION.md','REPLAY_NATIVE.json','SCOPE.md'];
const FIXED=[...EXEC_NAMES.map(n=>R+n),R+'SHA256SUMS',...MAT_NAMES.map(n=>M+n),M+'SHA256SUMS',S+'RECEPTION.md',S+'SHA256SUMS',
 A+'file_keys.proposed.mjs.txt',A+'collect_files.proposed.mjs.txt',A+'FILE_REQUEST.proposed.json',A+'ENTRY_REQUEST.proposed.json',A+'capture.proposed.sh.txt',
 E+'file_keys.mjs',E+'collect_files.mjs',B+'FILE_REQUEST.json',RAW+'stdout.canonical.json',RAW+'stderr.raw',
 QA+'p213_initial_science_enabled_root01/READ_FIXED.cjs',V+'receive_data.v2.proposed.mjs.txt',V+'CONTRACT.md',QA+'p212_eight_file_data_receiver_source_root01/RECEPTION.md'];
const allowed=new Set(FIXED),buffers=new Map(),current=new Map(),adapters=[];
let checks=0,total=0;
const need=(b,s)=>{checks++;if(!b)throw Error(s);};
const stable=x=>JSON.stringify(x,(_,v)=>v&&typeof v==='object'&&!Array.isArray(v)?Object.fromEntries(Object.keys(v).sort().map(k=>[k,v[k]])):v);
const eq=(a,b,label)=>need(stable(a)===stable(b),label);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pin=b=>({bytes:b.length,sha256:sha(b)});
const stat=s=>Object.fromEntries(F.map(k=>[k,s[k].toString()]));
const exact=(o,n,label)=>{need(o!==null&&typeof o==='object'&&!Array.isArray(o),label);eq(Object.keys(o).sort(),[...n].sort(),label+' fields');};
function read(path){
 need(allowed.has(path),'FINITE_COMPILED_DOCUMENT_ALLOWLIST');if(buffers.has(path))return buffers.get(path);
 const max=path===RAW+'stdout.canonical.json'?268435456:path===RAW+'stderr.raw'?8388608:16777216;
 const k={path,lstat_before:null,fd_before:null,fd_after:null,lstat_after:null,reads:[],byte_count:0,eof:false,closed:false,complete:false,sha256:null};
 current.set(path,k);let fd=null;const chunks=[];
 try{
  const s=fs.lstatSync(BASE+path,{bigint:true});k.lstat_before=stat(s);need(s.isFile()&&!s.isSymbolicLink()&&s.size>=0n&&s.size<=BigInt(max),'PHYSICAL_BOUNDED_FIXED_DOCUMENT');
  fd=fs.openSync(BASE+path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);k.fd_before=stat(fs.fstatSync(fd,{bigint:true}));eq(k.fd_before,k.lstat_before,'FULL_BEFORE_KEY');
  const h=crypto.createHash('sha256'),block=Buffer.alloc(65536);
  for(;;){const requested=Math.min(65536,max-k.byte_count+1);need(requested>0,'positive bounded read');const n=fs.readSync(fd,block,0,requested,null);k.reads.push({requested,returned:n});need(Number.isSafeInteger(n)&&n>=0&&n<=requested,'ACTUAL_READ_RETURN');
   if(n===0){k.eof=true;break;}k.byte_count+=n;total+=n;const piece=Buffer.from(block.subarray(0,n));chunks.push(piece);h.update(piece);need(k.byte_count<=max&&total<=536870912,'READ_CAP');}
  k.fd_after=stat(fs.fstatSync(fd,{bigint:true}));k.lstat_after=stat(fs.lstatSync(BASE+path,{bigint:true}));eq(k.fd_before,k.fd_after,'FULL_FD_AFTER');eq(k.lstat_before,k.lstat_after,'FULL_ENDPOINT_AFTER');need(BigInt(k.byte_count)===s.size,'WHOLE_SIZE_EOF');
  k.sha256=h.digest('hex');fs.closeSync(fd);fd=null;k.closed=true;k.complete=true;const b=Buffer.concat(chunks);buffers.set(path,b);return b;
 }catch(e){k.failure={name:e.name,code:e.code??null,message:e.message};k.partial_hex=Buffer.concat(chunks).toString('hex');throw e;}
 finally{if(fd!==null){try{fs.closeSync(fd);k.closed=true;}catch(e){k.close_failure={name:e.name,code:e.code??null,message:e.message};}}}
}
function json(path){need(path!==RAW+'stdout.canonical.json'&&path!==RAW+'stderr.raw','NO_CAPTURE_PARSE');const b=read(path),s=b.toString('utf8');need(Buffer.from(s,'utf8').equals(b),'DOC_UTF8');return JSON.parse(s);}
function key(k,path,kind){
 // Preserve originals separately. This is the COMPLETE named field adapter,
 // not a claim that historical reads/descriptors equal this loader's reads.
 const names=['path',...SF,'byte_count','eof','closed','sha256'];
 if(kind==='doc')names.push('complete','eof_zero_return');else if(kind==='raw')names.push('reads');else names.push('reads','complete');
 exact(k,names,'complete '+kind+' key');need(k.path===path,'EXACT_LITERAL_OLD_KEY');
 for(const f of SF){exact(k[f],F,'ten fields');for(const v of Object.values(k[f]))need(typeof v==='string'&&/^-?(0|[1-9][0-9]*)$/.test(v)&&v!=='-0','DECIMAL_STAT');eq(k[f],k.lstat_before,'ALL_FOUR_OLD_STATS');}
 need((BigInt(k.lstat_before.mode)&0o170000n)===0o100000n&&BigInt(k.lstat_before.size)===BigInt(k.byte_count),'OLD_REGULAR_SIZE');
 need(Number.isSafeInteger(k.byte_count)&&k.byte_count>=0&&k.eof===true&&k.closed===true,'OLD_WHOLE_FLAGS');
 if(kind==='doc')need(k.complete===true&&k.eof_zero_return===0,'OLD_EXPLICIT_ZERO');
 else{need(Array.isArray(k.reads)&&k.reads.length>0,'ACTUAL_READ_LIST');let sum=0;k.reads.forEach((r,i)=>{exact(r,['requested','returned'],'read row');need(Number.isSafeInteger(r.requested)&&r.requested>0&&Number.isSafeInteger(r.returned)&&r.returned>=0&&r.returned<=r.requested,'READ_COUNTS');need(i===k.reads.length-1?r.returned===0:r.returned>0,'FINAL_ONLY_ZERO');sum+=r.returned;});need(sum===k.byte_count,'READ_LIST_SUM');if(kind==='current')need(k.complete===true,'CURRENT_COMPLETE');}
 const b=read(path);need(b.length===k.byte_count&&typeof k.sha256==='string'&&sha(b)===k.sha256,'OLD_BODY_PIN_RECOMPUTED');
 return {path:BASE+path,lstat_before:k.lstat_before,fstat_before:k.fd_before,fstat_after:k.fd_after,lstat_after:k.lstat_after,bytes_read:k.byte_count,eof:k.eof,close_succeeded:k.closed,content:{bytes:k.byte_count,sha256:k.sha256}};
}
function oldKey(list,path,kind,label){need(Array.isArray(list),'OLD_KEY_ARRAY');const hits=list.filter(k=>k.path===path);need(hits.length===1,'ONE_OLD_LITERAL_KEY '+label);const mapped=key(hits[0],path,kind);eq(mapped,key(current.get(path),path,'current'),'FULL_CURRENT_VS_OLD '+label);adapters.push({origin:label,path,kind,original:hits[0],mapped});return mapped;}
function native(path,chunk){const n=json(path);need(n.result.exit_code===0&&n.result.chunk_id===chunk&&!Object.hasOwn(n.result,'session_id'),'ACTUAL_FINAL_NATIVE '+path);return n;}
function generated(name,value){const b=Buffer.from(JSON.stringify(value,null,2)+'\n');fs.writeFileSync(BASE+OWN+name,b,{flag:'wx',mode:0o600});return pin(b);}
const report={schema:'p212-eight-file-context-preparation-v1',status:'RUNNING',consumer_invoked:false,capture_parsed:false,host_query:false,operation_permission:false,external_status:'HOLD_EXTERNAL'};
try{
 need(process.argv.length===2&&process.cwd()===BASE.slice(0,-1),'EXACT_NO_ARGUMENT_CONTEXT');FIXED.forEach(read);
 const seal=(dir,names)=>{const expected=Buffer.from(names.slice().sort().map(n=>sha(read(dir+n))+'  '+n+'\n').join(''));need(expected.equals(read(dir+'SHA256SUMS')),'COMPLETE_FIXED_SEAL '+dir);};
 seal(R,EXEC_NAMES);seal(M,MAT_NAMES);
 const g=json(R+'GRANT.json'),c=json(R+'CONSUMPTION.json'),binding=json(B+'FILE_REQUEST.json'),template=json(A+'FILE_REQUEST.proposed.json'),entry=json(A+'ENTRY_REQUEST.proposed.json');
 need(sha(read(S+'RECEPTION.md'))===g.source_acceptance.sha256&&sha(read(S+'SHA256SUMS'))===g.source_acceptance.seal,'GRANTED_SOURCE_RECEIPT_SEAL');
 need(sha(read(M+'RECEPTION.md'))===g.materialization_acceptance.sha256&&sha(read(M+'SHA256SUMS'))===g.materialization_acceptance.seal,'GRANTED_MATERIAL_RECEIPT_SEAL');
 need(sha(read(V+'receive_data.v2.proposed.mjs.txt'))==='fc1ece786bb81cf1046e766ec9223272db576ebc284eab0ad45f9d42198ab253','ACCEPTED_V2_BYTES_ONLY');
 const pn=native(R+'PREFLIGHT_NATIVE.json','00bf7a'),rn=native(R+'RAW_RECEIVE_NATIVE.json','fce894'),mn=native(M+'CHECK_NATIVE.json','20a7fd');
 const pv=JSON.parse(pn.result.output),rv=JSON.parse(rn.result.output),mv=JSON.parse(mn.result.output);
 need(pv.status==='PASS_EXACT_BOUND_EIGHT_FILE_OBSERVATION_PREFLIGHT'&&rv.status==='PASS_COMPLETE_CLOSED_RAW_BYTES_ONLY_DATA_SOURCE_AND_SEMANTIC_RECEPTION_PENDING'&&mv.status==='PASS_ROOT_MATERIALIZATION_ORIGINAL_AND_CURRENT_RECEPTION','EXACT_RECEIVED_STATUS');
 need(pv.keys.length===17&&rv.keys.length===21&&rv.raw_keys.length===2,'EXACT_KEY_CENSUS');
 for(const old of pv.keys){need(allowed.has(old.path),'PREFLIGHT_PATH_IN_COMPILED_SCOPE');oldKey(pv.keys,old.path,'doc','preflight');}
 for(const old of rv.keys){need(allowed.has(old.path),'POST_PATH_IN_COMPILED_SCOPE');oldKey(rv.keys,old.path,'doc','post-observation');}
 const an=native(R+'ACTUAL_NATIVE.json','e08313');exact(an,['tool','request','result','continuations'],'complete actual native wrapper');
 need(read(R+'ACTUAL_NATIVE.json').equals(Buffer.from(JSON.stringify(an,null,2)+'\n')),'WHOLE_NATIVE_ORIGINAL_RAW_REENCODING');
 need(an.tool==='exec_command'&&an.result.output===''&&Array.isArray(an.continuations)&&an.continuations.length===0,'ONE_ACTUAL_NATIVE_FINAL');
 const frame={request:{tool:an.tool,arguments:an.request},result:an.result};eq(frame.request,g.native_request,'ENTIRE_NATIVE_GRANT');eq(frame.request,c.exact_native_request,'ENTIRE_CONSUMED_REQUEST');eq(frame.request,entry.proposed_native_request,'ENTIRE_ACCEPTED_REQUEST');
 need(Buffer.from(an.request.cmd).equals(read(A+'capture.proposed.sh.txt')),'ENTIRE_CMD_RAW');
 need(g.id==='P212_EIGHT_FILE_OBSERVATION_NEW_SINGLE_01'&&g.permitted_native_submissions===1&&g.old_two_grants_reused===false&&c.grant_id===g.id&&c.status==='CONSUMED_BEFORE_NATIVE_SUBMISSION'&&c.remaining_submissions===0&&c.old_two_grants_reused===false&&c.automatic_retry===false&&c.preflight_actual_chunk_id==='00bf7a','DISTINCT_CONSUMED_GRANT');
 // Cross-file chronology is the execution root's received act record, NOT an
 // inference from metadata times, current booleans or this context's assertion.
 need(read(R+'HANDOFF.md').includes(Buffer.from('CONSUMPTION was written before submission')),'RECEIVED_CHRONOLOGY_STATEMENT');
 const grantRef={path:BASE+R+'GRANT.json',pin:pin(read(R+'GRANT.json'))};eq(binding.permission_receipt,grantRef,'FULL_BINDING_GRANT');
 need(binding.enabled===true&&binding.status==='ROOT_BOUND_FINITE_FILES_ONLY','BOUND_ACTIVATION');eq({...binding,enabled:false,status:template.status,permission_receipt:null},template,'ONLY_THREE_FIELD_DELTA');eq(g.ordered_eight_candidates,template.entries,'ALL_EIGHT_GRANT_ROWS');need(g.total_byte_limit===template.total_byte_limit,'TOTAL_LIMIT');
 const sourceRows=[['reader','file_keys.proposed.mjs.txt','file_keys.mjs','957111a4a680f61cc94e89eb220b8c7c10d779e04eabd4734948690ef11b41f8'],['entry','collect_files.proposed.mjs.txt','collect_files.mjs','bd9baeb57f2387860a400f4b27e8acf9897da3843482cf856378f9807a2b2b87']];
 const sources=sourceRows.map(([role,src,dst,digest])=>{need(read(A+src).equals(read(E+dst))&&sha(read(A+src))===digest,'EXACT_SOURCE_COPY_BODY');const destination_key=oldKey(pv.keys,E+dst,'doc','source-preflight');oldKey(mv.keys,E+dst,'doc','materialized-source');return {role,source:BASE+A+src,destination:BASE+E+dst,raw_hex:read(A+src).toString('hex'),source_key:key(current.get(A+src),A+src,'current'),destination_key};});
 const before_key=oldKey(pv.keys,B+'FILE_REQUEST.json','doc','binding-before'),after_key=oldKey(rv.keys,B+'FILE_REQUEST.json','doc','binding-after');eq(before_key,after_key,'COMPLETE_BINDING_PRE_POST');
 const rawRows={};for(const [role,name] of [['stdout','stdout.canonical.json'],['stderr','stderr.raw']]){const path=RAW+name,closed_key=oldKey(rv.raw_keys,path,'raw','closed-'+role);rawRows[role]={role,source:BASE+path,destination:BASE+path,closed_key};}
 need(read(R+'RAW_INPUTS.sha256').equals(Buffer.from(['stdout.canonical.json','stderr.raw'].map(n=>sha(read(RAW+n))+'  '+RAW+n+'\n').join(''))),'COMPLETE_RAW_INPUT_MANIFEST');
 // Exact embedded request/result byte ranges of the FULL original wrapper.
 const nativeRaw=read(R+'ACTUAL_NATIVE.json');const nativeText=nativeRaw.toString('utf8');
 function sliceMember(name){const marker='\n  "'+name+'": ',at=nativeText.indexOf(marker);need(at>=0&&nativeText.indexOf(marker,at+1)===-1,'UNIQUE_TOP_MEMBER');const start=at+marker.length;const embedded=JSON.stringify(an[name],null,2).split('\n').map((l,i)=>i?'  '+l:l).join('\n');const b=nativeRaw.subarray(Buffer.byteLength(nativeText.slice(0,start)),Buffer.byteLength(nativeText.slice(0,start+embedded.length)));need(b.equals(Buffer.from(embedded)),'EXACT_NATIVE_MEMBER_RAW_SLICE');eq(JSON.parse(b),an[name],'ENTIRE_ORIGINAL_TO_PROJECTION');return {buffer:b,start:Buffer.byteLength(nativeText.slice(0,start)),bytes:b.length};}
 const req=sliceMember('request'),res=sliceMember('result');
 const context={schema:'p212-eight-file-authenticated-data-context-v1',root_original_projection_reception:null,sources,binding:{role:'binding',source:BASE+B+'FILE_REQUEST.json',destination:BASE+B+'FILE_REQUEST.json',raw_hex:read(B+'FILE_REQUEST.json').toString('hex'),before_key,after_key},
  grant:{reference:grantRef,raw_hex:read(R+'GRANT.json').toString('hex'),key:oldKey(pv.keys,R+'GRANT.json','doc','grant-preflight'),consumed_before_submission:true,remaining_uses:0,fresh_distinct_from_two_consumed_grants:true},...rawRows,
  native:{frames:[frame],originals:[{request_hex:req.buffer.toString('hex'),request_pin:pin(req.buffer),result_hex:res.buffer.toString('hex'),result_pin:pin(res.buffer)}],final_exit_code:an.result.exit_code,settled:true,continuations:0,initial_session_id:null}};
 report.context_pin=generated('CONTEXT.prospective.json',context);
 report.evidence_pin=generated('EVIDENCE.json',{schema:'p212-fixed-document-context-evidence-v1',documents:FIXED.map(path=>({path,key:current.get(path),raw_hex:path.startsWith(RAW)?null:read(path).toString('hex'),raw_omission:path.startsWith(RAW)?'entire existing literal raw is retained in place and keyed; no raw parsing':null})),adapters,
  native_projection:{original_path:R+'ACTUAL_NATIVE.json',original_pin:pin(nativeRaw),request_range:{start:req.start,bytes:req.bytes},result_range:{start:res.start,bytes:res.bytes},tool_source:'entire original top-level tool member',frame},
  root_authentication_pending:true,allowed_context_delta:['root_original_projection_reception'],chronology_source:R+'HANDOFF.md plus original CONSUMPTION.json and ACTUAL_NATIVE.json; root actual issuance/consumption/submission record'});
 report.status='CONTEXT_PREPARED_ROOT_AUTHENTICATION_PENDING';report.fixed_count=FIXED.length;report.adapter_count=adapters.length;
}catch(e){report.status='FAILED_PRESERVED_NO_CONSUMER_INVOCATION';report.failure={name:e.name,code:e.code??null,message:e.message};process.exitCode=1;report.partial_keys=[...current.values()];}
report.checks=checks;report.total_bytes=total;process.stdout.write(JSON.stringify(report,null,2)+'\n');
