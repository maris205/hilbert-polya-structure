// SOURCE-ONLY entry proposal. Not imported/executed/materialized now.
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {collectThreeLeaves} from './three_leaves.mjs';
const REQUEST='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_os_release_terminal_binding01/REQUEST.json';
const F='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' '),IDENTITY=F.slice(0,7);
const MAX_REQUEST=65536,MAX_STDOUT=268435456,MAX_STDERR=8388608;
const need=(b,s)=>{if(!b)throw Error(s);};
const fields=s=>Object.fromEntries(F.map(k=>{need(typeof s[k]==='bigint','ACTUAL_BIGINT_FIELD');return[k,s[k].toString()];}));
const same=(a,b,s)=>need(JSON.stringify(a)===JSON.stringify(b),s);
const pin=b=>({bytes:b.length,sha256:createHash('sha256').update(b).digest('hex')});
const errorData=e=>({name:String(e?.name??'Error'),code:typeof e?.code==='string'?e.code:null,message:String(e?.message??e)});
function loadRequest(r){
 Object.assign(r,{path:REQUEST,byte_limit:MAX_REQUEST,lstat_before:null,fstat_before:null,fstat_after:null,lstat_after:null,bytes_read:0,reads:[],eof:false,close_succeeded:null,raw_hex:'',content:null,complete:false,error:null,close_error:null});
 let fd=null;const chunks=[];
 try{const first=fs.lstatSync(REQUEST,{bigint:true});r.lstat_before=fields(first);need(first.isFile()&&!first.isSymbolicLink()&&first.nlink===1n&&first.uid===0n&&first.size>=0n&&first.size<=BigInt(MAX_REQUEST),'FIXED_PHYSICAL_BOUNDED_ROOT_REQUEST');
  fd=fs.openSync(REQUEST,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);r.fstat_before=fields(fs.fstatSync(fd,{bigint:true}));same(r.fstat_before,r.lstat_before,'ALL_TEN_REQUEST_BEFORE');
  const block=Buffer.alloc(65536);for(;;){const remaining=MAX_REQUEST-r.bytes_read;need(remaining>=0,'REQUEST_REMAINING');const requested=Math.min(block.length,remaining+1),n=fs.readSync(fd,block,0,requested,null);r.reads.push({requested,returned:n});need(Number.isSafeInteger(n)&&n>=0&&n<=requested,'ACTUAL_REQUEST_READ_COUNT');if(n===0){r.eof=true;break;}chunks.push(Buffer.from(block.subarray(0,n)));r.bytes_read+=n;need(n<=remaining,'REQUEST_OVERFLOW_SENTINEL_PRESERVED');}
  r.fstat_after=fields(fs.fstatSync(fd,{bigint:true}));r.lstat_after=fields(fs.lstatSync(REQUEST,{bigint:true}));same(r.fstat_before,r.fstat_after,'REQUEST_FD_STABLE');same(r.lstat_before,r.lstat_after,'REQUEST_LEAF_STABLE');need(BigInt(r.bytes_read)===first.size,'REQUEST_WHOLE_SIZE_EOF');
 }catch(e){r.error=errorData(e);throw e;}
 finally{let closeFailure=null;if(fd!==null){try{fs.closeSync(fd);r.close_succeeded=true;}catch(e){r.close_succeeded=false;r.close_error=errorData(e);closeFailure=e;}}const raw=Buffer.concat(chunks);r.raw_hex=raw.toString('hex');r.content=pin(raw);if(closeFailure!==null)throw closeFailure;}
 r.complete=r.eof&&r.close_succeeded===true&&r.error===null&&r.close_error===null;need(r.complete,'COMPLETE_CLOSED_REQUEST');const b=Buffer.concat(chunks),s=b.toString('utf8');need(Buffer.from(s,'utf8').equals(b),'REQUEST_UTF8_REVERSIBLE');return JSON.parse(s);
}
let phase='capture_descriptors',ready=false,outInitial=null,errInitial=null,outBytes=0,errBytes=0,called=false,readerResult=null,exitCode=79;const input={};
function writeAll(fd,b){let at=0;while(at<b.length){const n=fs.writeSync(fd,b,at,b.length-at,null);need(Number.isSafeInteger(n)&&n>0&&n<=b.length-at,'POSITIVE_CAPTURE_WRITE');at+=n;if(fd===1)outBytes+=n;else errBytes+=n;}}
function checkOutput(fd,initial,written){const now=fields(fs.fstatSync(fd,{bigint:true}));need(IDENTITY.every(k=>initial[k]===now[k]),'CAPTURE_SAME_DESCRIPTOR');need(BigInt(now.size)===BigInt(written),'CAPTURE_ACTUAL_SIZE');}
function emit(value){const text=JSON.stringify(value);need(typeof text==='string','JSON_DOCUMENT');const b=Buffer.from(text+'\n','utf8');need(b.length<=MAX_STDOUT&&outBytes===0,'ONE_COMPLETE_BOUNDED_DOCUMENT');writeAll(1,b);checkOutput(1,outInitial,outBytes);}
function diagnostic(label,error){if(!ready)return;try{const b=Buffer.from(JSON.stringify({schema:'p212-three-leaf-entry-diagnostic-v1',status:'FAILED_PARTIAL_PRESERVED',phase,label,error:errorData(error),stdout_bytes_written:outBytes,reader_called:called,reader_returned:readerResult!==null,complete_result_not_guaranteed:true,operation_permission:false})+'\n','utf8');need(errBytes+b.length<=MAX_STDERR,'DIAGNOSTIC_TOTAL_BOUND');writeAll(2,b);checkOutput(2,errInitial,errBytes);}catch(_){/* Preserve all existing partial stdout/stderr. */}}
function envelope(status,entryFailure){return {schema:'p212-three-leaf-captured-result-v1',status,request_input:input,reader_called:called,reader_returned:readerResult!==null,reader_result:readerResult,entry_failure:entryFailure,operation_permission:false,installed_closure:false,referents_followed:false,package_queries:false};}
try{
 const out=fs.fstatSync(1,{bigint:true}),err=fs.fstatSync(2,{bigint:true});
 for(const s of [out,err])need(s.isFile()&&s.nlink===1n&&s.uid===0n&&s.gid===0n&&(s.mode&0o7777n)===0o600n&&s.size===0n,'FRESH_ROOT_PRIVATE_CAPTURE_DESCRIPTOR');
 need(out.dev!==err.dev||out.ino!==err.ino,'DISTINCT_CAPTURE_FILES');outInitial=fields(out);errInitial=fields(err);ready=true;
 need(process.argv.length===2,'EXACT_NO_ARGUMENT_ENTRY');phase='load_fixed_request';const request=loadRequest(input);
 phase='single_three_leaf_call';called=true;readerResult=collectThreeLeaves(request);
 need(readerResult&&readerResult.schema==='p212-three-lexical-leaves-v1'&&['FAILED_PARTIAL_PRESERVED','THREE_LEXICAL_LEAVES_ROOT_RECEPTION_PENDING'].includes(readerResult.status),'EXACT_READER_RETURN');
 phase='complete_json_capture';emit(envelope(readerResult.status,null));same(fields(fs.fstatSync(2,{bigint:true})),errInitial,'STDERR_UNCHANGED_ON_NORMAL_RETURN');exitCode=readerResult.status==='FAILED_PARTIAL_PRESERVED'?78:0;
}catch(e){exitCode=79;if(ready&&outBytes===0){try{emit(envelope('FAILED_ENTRY_OR_UNRETURNED_READER',{phase,error:errorData(e)}));}catch(secondary){diagnostic('failure_envelope_unavailable',secondary);}}else diagnostic('entry_or_partial_stdout_failure',e);}
finally{try{fs.closeSync(1);}catch(e){exitCode=79;diagnostic('stdout_close_failure',e);}}
process.exitCode=exitCode;
