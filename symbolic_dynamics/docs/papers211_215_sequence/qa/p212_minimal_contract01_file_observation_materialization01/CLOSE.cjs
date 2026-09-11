'use strict';
// Read-only fixed-document closure; no imported materializer or copied code.
const fs=require('node:fs'),{createHash}=require('node:crypto');
const P='docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_';
const OWN=P+'materialization01',AUTHOR=P+'preparation01',ENABLED=P+'enabled01',RAW=P+'raw01';
const BASE=['CHECK.cjs','HANDOFF.md','MATERIALIZE_NATIVE.json','MATERIALIZE_RESULT.json','ORIGIN.md','PREFLIGHT_NATIVE.json','PREFLIGHT_RESULT.json','READ_NATIVE.json','CLOSE.cjs'].sort();
const ADDED=['CLOSING_NATIVE.json','CLOSING_RESULT.json'];
const DOCS=[...['file_keys.proposed.mjs.txt','collect_files.proposed.mjs.txt','capture.proposed.sh.txt','FILE_REQUEST.proposed.json','ENTRY_REQUEST.proposed.json','SHA256SUMS'].map(x=>AUTHOR+'/'+x),P+'source_audit01/REPORT.md',P+'source_audit01/SHA256SUMS',P+'source_root01/RECEPTION.md',P+'source_root01/SHA256SUMS'];
const COPIES=[ENABLED+'/file_keys.mjs',ENABLED+'/collect_files.mjs'];
const FIELDS=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const META=['lstat_before','fstat_before','fstat_after','lstat_after'];
const report={schema:'p212-materialization-documentary-closure-v1',mode:null,status:'FAILED_PARTIAL_PRESERVED',checks:0,keys:[],directories:[],raw_comparisons:[],historical_keys_compared:0,payloads:[],seal:null,failure:null,source_execution:false,operation_permission:false,observation_grant:false,binding_materialized:false};
const data=new Map(),rows=new Map();
const need=(v,m)=>{report.checks++;if(!v)throw Error(m);};
const same=(a,b,m)=>need(JSON.stringify(a)===JSON.stringify(b),m);
const pin=b=>({bytes:b.length,sha256:createHash('sha256').update(b).digest('hex')});
const err=e=>({name:String(e?.name??'Error'),code:typeof e?.code==='string'?e.code:null,message:String(e?.message??e)});
const fields=s=>Object.fromEntries(FIELDS.map(k=>{need(typeof s[k]==='bigint','actual bigint '+k);return[k,s[k].toString()];}));
let allowed;
function read(path){
 need(allowed.has(path),'fixed document/copy whitelist');
 const row={path,lstat_before:null,fstat_before:null,fstat_after:null,lstat_after:null,fd:null,reads:[],bytes_read:0,eof:false,content:null,close_succeeded:null,error:null,close_error:null};
 report.keys.push(row);let fd=null;const chunks=[];
 try{const s=fs.lstatSync(path,{bigint:true});row.lstat_before=fields(s);need(s.isFile()&&!s.isSymbolicLink(),'regular physical document/copy');need(s.size>=0n&&s.size<=8388608n,'bounded documentary size');
  fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);row.fd=fd;
  const t=fs.fstatSync(fd,{bigint:true});row.fstat_before=fields(t);need(t.isFile(),'regular opened leaf');same(row.lstat_before,row.fstat_before,'same-fd before bytes');
  const b=Buffer.alloc(65536);for(;;){const requested=Math.min(b.length,8388609-row.bytes_read);need(requested>0,'positive read request');const n=fs.readSync(fd,b,0,requested,null);row.reads.push({requested,returned:n});if(n===0){row.eof=true;break;}chunks.push(Buffer.from(b.subarray(0,n)));row.bytes_read+=n;need(row.bytes_read<=8388608,'full document bound');}
  const raw=Buffer.concat(chunks);row.content=pin(raw);need(BigInt(raw.length)===t.size,'full actual zero EOF size');row.fstat_after=fields(fs.fstatSync(fd,{bigint:true}));row.lstat_after=fields(fs.lstatSync(path,{bigint:true}));same(row.fstat_before,row.fstat_after,'same opened endpoint');same(row.lstat_before,row.lstat_after,'same lexical endpoint');need(Buffer.from(raw.toString('utf8'),'utf8').equals(raw),'UTF8 reversible');data.set(path,raw);rows.set(path,row);
 }catch(e){row.error=err(e);throw e;}finally{if(fd!==null){try{fs.closeSync(fd);row.close_succeeded=true;}catch(e){row.close_succeeded=false;row.close_error=err(e);throw e;}}}
 need(row.eof&&row.close_succeeded===true,'complete closed key');return row;
}
function directory(path,names){
 need([OWN,ENABLED,RAW].includes(path),'three explicit owned evidence/runtime directories only');
 const row={path,before:null,after:null,names:[],eof:false,close_succeeded:null,error:null,close_error:null};report.directories.push(row);let d=null;
 try{const s=fs.lstatSync(path,{bigint:true});row.before=fields(s);need(s.isDirectory()&&!s.isSymbolicLink(),'physical directory');
  if(path!==OWN){need((s.mode&0o7777n)===0o700n&&s.uid===0n&&s.gid===0n,'root owned exact0700 runtime directory');}
  d=fs.opendirSync(path);for(;;){const e=d.readSync();if(e===null){row.eof=true;break;}row.names.push(e.name);need(row.names.length<=names.length+1,'unexpected member retained then refuse');}
  row.names.sort();same(row.names,[...names].sort(),'exact non-discovery directory membership through EOF');row.after=fields(fs.lstatSync(path,{bigint:true}));same(row.before,row.after,'whole directory endpoint stability');
 }catch(e){row.error=err(e);throw e;}finally{if(d!==null){try{d.closeSync();row.close_succeeded=true;}catch(e){row.close_succeeded=false;row.close_error=err(e);throw e;}}}
 need(row.eof&&row.close_succeeded===true,'directory EOF and close');return row;
}
const json=path=>JSON.parse(data.get(path).toString('utf8'));
function rawEqual(a,b,label){need(a.equals(b),label);report.raw_comparisons.push({label,bytes:a.length,raw_equal:true});}
function wholeKey(now,old,label){need(!!now&&!!old,label+' present');
 for(const k of META){same(Object.keys(old[k]),FIELDS,label+' exact ten-field order');for(const f of FIELDS)need(typeof old[k][f]==='string'&&/^-?(0|[1-9][0-9]*)$/.test(old[k][f])&&old[k][f]!=='-0',label+' complete decimal '+f);same(now[k],old[k],label+' '+k);}
 for(const k of ['content','bytes_read','eof','close_succeeded','error','close_error'])same(now[k],old[k],label+' '+k);
 need(old.eof===true&&old.close_succeeded===true&&Array.isArray(old.reads)&&old.reads.length>0,'historical actual EOF and close');
 let total=0;old.reads.forEach((r,i)=>{need(Number.isSafeInteger(r.requested)&&r.requested>0&&Number.isSafeInteger(r.returned)&&r.returned>=0&&r.returned<=r.requested,'actual read counts');need(i===old.reads.length-1?r.returned===0:r.returned>0,'exact final zero EOF call');total+=r.returned;});need(total===old.bytes_read,'all actual read counts sum');
 report.historical_keys_compared++;
}
function nativePair(nativeName,resultName,cmd,status){
 const n=json(OWN+'/'+nativeName),raw=data.get(OWN+'/'+resultName),r=JSON.parse(raw);
 need(n.tool==='exec_command'&&n.request.cmd===cmd&&n.request.workdir==='/root/autodl-tmp/symbolic_dynamics','exact native original request');
 need(n.result.exit_code===0&&!n.result.session_id&&typeof n.result.output==='string','actual settled zero native original');
 rawEqual(Buffer.from(n.result.output,'utf8'),raw,nativeName+' whole native stdout/raw result');
 need(r.status===status&&r.failure===null,'actual documentary result status');
 for(const old of r.keys)wholeKey(rows.get(old.path),old,nativeName+' '+old.path);
 return r;
}
try{
 need(process.argv.length===3&&['--preseal','--sealed'].includes(process.argv[2]),'explicit read-only closure mode');report.mode=process.argv[2];
 need(process.cwd()==='/root/autodl-tmp/symbolic_dynamics'&&process.getuid()===0&&process.getgid()===0,'adopted ordinary root-key bootstrap');
 const names=[...BASE,...(report.mode==='--sealed'?ADDED:[])].sort();
 const paths=[...new Set([...DOCS,...COPIES,...names.map(x=>OWN+'/'+x),...(report.mode==='--sealed'?[OWN+'/SHA256SUMS']:[])])];
 allowed=new Set(paths);directory(OWN,[...names,...(report.mode==='--sealed'?['SHA256SUMS']:[])]);
 paths.forEach(read);
 const material=nativePair('MATERIALIZE_NATIVE.json','MATERIALIZE_RESULT.json','node '+OWN+'/CHECK.cjs --materialize','MATERIALIZED_ROOT_RECEPTION_PENDING');
 const preflight=nativePair('PREFLIGHT_NATIVE.json','PREFLIGHT_RESULT.json','node '+OWN+'/CHECK.cjs --preflight','PASS_READ_ONLY_PREFLIGHT_ROOT_RECEPTION_PENDING');
 same(material.absence.map(x=>[x.path,x.state,x.error.code]),[[ENABLED,'ABSENT','ENOENT'],[RAW,'ABSENT','ENOENT']],'two actual original exclusive-creation absences');
 same(material.actions.map(x=>[x.operation,x.path??x.destination,x.success,x.error]),[['mkdirSync',ENABLED,true,null],['mkdirSync',RAW,true,null],['copyFileSync',COPIES[0],true,null],['copyFileSync',COPIES[1],true,null]],'exact four actual successful mutations');
 for(const a of material.actions)need(a.operation==='mkdirSync'?(a.requested_mode==='0700'&&a.recursive===false):a.flags==='COPYFILE_EXCL','exclusive exact mutation parameters');
 const initial=json(OWN+'/READ_NATIVE.json');need(initial.native.length===4,'all four original initial native calls');
 for(const n of initial.native)need(n.tool==='exec_command'&&n.result.exit_code===0&&!n.result.session_id&&typeof n.result.output==='string','entire actual preparatory native originals');
 const expectedRequests=[
 'cat docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_root01/RECEPTION.md docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_root01/SHA256SUMS docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/FILE_REQUEST.proposed.json docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/ENTRY_REQUEST.proposed.json',
 'cat docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/file_keys.proposed.mjs.txt docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/collect_files.proposed.mjs.txt docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/capture.proposed.sh.txt'];
 const groups=[[P+'source_root01/RECEPTION.md',P+'source_root01/SHA256SUMS',AUTHOR+'/FILE_REQUEST.proposed.json',AUTHOR+'/ENTRY_REQUEST.proposed.json'],[AUTHOR+'/file_keys.proposed.mjs.txt',AUTHOR+'/collect_files.proposed.mjs.txt',AUTHOR+'/capture.proposed.sh.txt']];
 groups.forEach((g,i)=>{need(initial.native[i+1].request.cmd===expectedRequests[i],'exact entire original cat request');rawEqual(Buffer.from(initial.native[i+1].result.output,'utf8'),Buffer.concat(g.map(x=>data.get(x))),'complete original receipt/request/source/capture read '+i);});
 const a=JSON.parse(initial.native[3].result.output);same(a.rows.map(x=>[x.path,x.state,x.error.code]),[[OWN,'ABSENT','ENOENT'],[ENABLED,'ABSENT','ENOENT'],[RAW,'ABSENT','ENOENT']],'original three-directory absence evidence remains historical DATA');
 const entry=json(AUTHOR+'/ENTRY_REQUEST.proposed.json');rawEqual(Buffer.from(entry.proposed_native_request.arguments.cmd,'utf8'),data.get(AUTHOR+'/capture.proposed.sh.txt'),'whole prospective native command/capture');
 COPIES.forEach((dst,i)=>{const src=AUTHOR+'/'+['file_keys.proposed.mjs.txt','collect_files.proposed.mjs.txt'][i];rawEqual(data.get(src),data.get(dst),'whole original source/physical copy '+i);const x=rows.get(src).lstat_before,y=rows.get(dst).lstat_before;need(x.dev!==y.dev||x.ino!==y.ino,'distinct physical copy inode');need(y.nlink==='1'&&y.uid==='0'&&y.gid==='0','root single-link copy');});
 for(const[path,members]of [[ENABLED,['collect_files.mjs','file_keys.mjs']],[RAW,[]]]){const now=directory(path,members);for(const old of [material,preflight]){const d=old.directories.find(x=>x.path===path&&x.phase==='final_preflight');need(!!d,'original directory disposition');same(now.before,d.before,'whole actual original/current directory key');same(now.after,d.after,'whole original/current final directory key');same(now.names,d.names,'whole original/current directory membership');need(d.eof&&d.close_succeeded===true&&d.error===null&&d.close_error===null,'actual original directory EOF and close');}}
 if(report.mode==='--sealed'){
  const closure=nativePair('CLOSING_NATIVE.json','CLOSING_RESULT.json','node '+OWN+'/CLOSE.cjs --preseal','PASS_PRESEAL_NONSELF_DOCUMENTARY_CLOSURE');
  need(closure.mode==='--preseal'&&closure.payloads.length===BASE.length,'actual nine-payload preseal original');
  const expected=names.map(name=>rows.get(OWN+'/'+name).content.sha256+'  '+name+'\n').join('');
  rawEqual(data.get(OWN+'/SHA256SUMS'),Buffer.from(expected,'utf8'),'entire exact eleven-payload nonself manifest');
  report.seal={path:OWN+'/SHA256SUMS',...rows.get(OWN+'/SHA256SUMS').content};
 }
 report.payloads=names.map(name=>({name,...rows.get(OWN+'/'+name).content}));report.payload_bytes=report.payloads.reduce((n,x)=>n+x.bytes,0);
 report.status=report.mode==='--sealed'?'PASS_FINAL_NONSELF_DOCUMENTARY_CLOSURE':'PASS_PRESEAL_NONSELF_DOCUMENTARY_CLOSURE';
}catch(e){report.failure=err(e);process.exitCode=78;}
report.key_count=report.keys.length;report.total_read_bytes=report.keys.reduce((n,x)=>n+x.bytes_read,0);
process.stdout.write(JSON.stringify(report,null,2)+'\n');
