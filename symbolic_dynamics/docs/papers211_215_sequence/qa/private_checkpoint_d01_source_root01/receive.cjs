'use strict';
// D01 documentary root reception only. Never executes either Python launcher.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const B='docs/papers211_215_sequence/qa/';
const P=B+'private_checkpoint_d01_preparation01/';
const A=B+'private_checkpoint_d01_source_audit01/';
const D=B+'private_checkpoint_d01_cancellation_delta01/';
const I=B+'private_checkpoint_d01_cancellation_audit_delta01/';
const R=B+'private_checkpoint_d01_source_root01/';
const specs=[
 [P,13,'bc61e43e136281c0ea4e55809d26d0e34e92a9e88dd6bd4d1a06e1157e5d82ee'],
 [A,13,'709433ceb8102a8bd624f14ecdbbae45e368a72d747855e04f18babc0f224428'],
 [D,9,'dbe83bea29b244561b420624064d2771f114ef8354e17d9a6fa179b057a80fc3'],
 [I,14,'ab76b14b6eb9eff7ec964077437c66e1f0a8dfd276ad8772ef55ea4d3f5a0b7f']];
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const eq=(a,b,m)=>{assert.deepEqual(a,b,m);checks++;};const need=(x,m)=>{assert.ok(x,m);checks++;};
const cache=new Map(),keys=new Map();
function read(p){
 need(p.startsWith('docs/')&&!p.split('/').some(x=>!x||x==='.'||x==='..'),'fixed workspace path');
 const st=fs.lstatSync(ROOT+p,{bigint:true});need(st.isFile()&&!st.isSymbolicLink()&&st.size<4000000n,'bounded physical document');
 const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 let raw;try{eq(meta(fs.fstatSync(fd,{bigint:true})),meta(st),'same fd before');raw=fs.readFileSync(fd);eq(meta(fs.fstatSync(fd,{bigint:true})),meta(st),'same fd after');}finally{fs.closeSync(fd);}
 eq(meta(fs.lstatSync(ROOT+p,{bigint:true})),meta(st),'path endpoint');eq(BigInt(raw.length),st.size,'whole file length');
 const key={path:p,bytes:raw.length,sha256:hash(raw),metadata:meta(st)};
 if(keys.has(p))eq(key,keys.get(p),'unchanged repeated full key');keys.set(p,key);cache.set(p,raw);return raw;
}
const json=p=>JSON.parse(read(p));
const packages=[];
for(const [dir,count,digest]of specs){
 const b=read(dir+'SHA256SUMS');eq(hash(b),digest,'selected seal');
 need(b.toString().endsWith('\n')&&!b.toString().endsWith('\n\n'),'strict seal ending');
 const names=[];let bytes=b.length;
 for(const line of b.toString().slice(0,-1).split('\n')){
  const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);need(m&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'nonself unique strict member');
  names.push(m[2]);const raw=read(dir+m[2]);bytes+=raw.length;eq(hash(raw),m[1],'whole payload');
  if(m[2].endsWith('.json'))JSON.parse(raw);
 }
 eq(names.length,count,'payload count');eq(fs.readdirSync(ROOT+dir).sort(),[...names,'SHA256SUMS'].sort(),'complete package membership');
 packages.push({path:dir,payloads:count,files:count+1,bytes,seal_sha256:digest});
}
function recordedKeys(file,fields){
 const x=json(file);eq(x.response.exit_code,0,'actual inventory exit');const body=JSON.parse(x.response.output);
 return fields.flatMap(k=>{need(Array.isArray(body[k]),'recorded key array');return body[k];});
}
for(const [dir,fspec]of [[A,['input_package','author_referenced_inputs','context_inputs']],[I,['author_inputs','historical_inputs']]]){
 const before=recordedKeys(dir+'INPUT_BEFORE_NATIVE.json',fspec),after=recordedKeys(dir+'INPUT_AFTER_NATIVE.json',fspec);eq(before,after,'recorded endpoint vector');
 for(const key of before){const b=read(key.path);eq(b.length,key.bytes,'complete recorded bytes');eq(hash(b),key.sha256,'complete recorded hash');eq(keys.get(key.path).metadata,key.metadata,'ten recorded fields');}
}
for(const [author,name,census]of [[P,'INPUT_PINS.sha256',14],[D,'INPUT_PINS.sha256',9]]){
 const data=cache.get(author+name).toString();const rows=data.trimEnd().split('\n');eq(rows.length,census,'declared input pins');
 for(const line of rows){const m=/^([a-f0-9]{64})  (docs\/[A-Za-z0-9_./-]+)$/.exec(line);need(m,'input pin syntax');eq(hash(read(m[2])),m[1],'all pinned inputs');}
}
const replays=[];
for(const [archive,actual,expected]of [[A+'VERIFICATION_NATIVE.json',R+'OLD_AUDIT_REPLAY_NATIVE.json',273],[I+'CHECKS_NATIVE.json',R+'DELTA_AUDIT_REPLAY_NATIVE.json',210]]){
 const a=json(archive),b=json(actual);eq(a.response.exit_code,0,'archived check exit');eq(b.response.exit_code,0,'fresh check exit');
 need(Buffer.from(a.response.output).equals(Buffer.from(b.response.output)),'actual complete raw documentary replay equality');
 const value=JSON.parse(b.response.output);eq(value.checks,expected,'documentary checks');replays.push({archive,actual,checks:expected,bytes:Buffer.byteLength(b.response.output),sha256:hash(Buffer.from(b.response.output))});
}
const rd=json(R+'ROOT_DIFF_NATIVE.json'),ind=json(I+'DIFF_NATIVE.json');eq(rd.response.exit_code,1,'actual root diff expected exit');eq(ind.response.exit_code,1,'independent diff expected exit');
const patch=cache.get(D+'EXACT_DELTA.patch');
for(const b of [Buffer.from(rd.response.output),Buffer.from(ind.response.output),read(I+'INDEPENDENT_DELTA.patch')])need(b.equals(patch),'four-way raw delta equality');
eq(patch.length,6356,'whole diff length');
const old=json(A+'FINDINGS.json'),verdict=json(I+'FINDINGS.json');eq(old.findings[0].status,'open','old Major unchanged');
eq(verdict.verdict,'D01_F01_CLOSED_FOR_EXACT_SOURCE','actual exact same-reviewer verdict');eq(verdict.current_open_census,{critical:0,major:0,minor:0},'current exact source census');
eq(verdict.source.sha256,hash(cache.get(D+'launch.py')),'entire accepted source hash');eq(verdict.source.bytes,cache.get(D+'launch.py').length,'whole source bytes');
eq(verdict.findings[0].id,'D01-F01','same finding');eq(verdict.findings[0].status,'closed','new exact closure');
need(verdict.operational_authority===false&&verdict.submitted_source_executed===false,'no authority/test transplant');
const native=[];
function collect(x,label){
 if(!x||typeof x!=='object')return;const r=x.result||x.response;
 if(x.request&&r&&typeof r.output==='string'&&r.chunk_id){native.push({label,request:x.request,response:r});return;}
 if(x.chunk_id&&typeof x.output==='string'){native.push({label,request:null,response:x});return;}
 for(const [k,v]of Object.entries(x))collect(v,label+'/'+k);
}
for(const [dir]of specs)for(const [name,raw]of cache)if(name.startsWith(dir)&&name.endsWith('.json'))collect(JSON.parse(raw),name);
const nativeKeys=native.map(r=>({label:r.label,chunk_id:r.response.chunk_id,exit_code:r.response.exit_code,request_present:!!r.request,bytes:Buffer.byteLength(r.response.output),sha256:hash(Buffer.from(r.response.output))}));
const final=[...keys.values()].sort((a,b)=>a.path.localeCompare(b.path));for(const key of final){read(key.path);eq(keys.get(key.path),key,'closing complete key');}
process.stdout.write(JSON.stringify({status:'D01_EXACT_SOURCE_ORIGINAL_RECEPTION_PASS_NOT_DIAGNOSTIC_GRANT',checks,packages,whole_keys:keys.size,keys:final,replays,
 native_records:nativeKeys,actual_root_diff:{bytes:patch.length,sha256:hash(patch)},accepted_source:verdict.source,
 historical_finding_open:true,current_exact_source_open:verdict.current_open_census,submitted_source_executed:false,SSH_Git_private_host_observed:false},null,2)+'\n');
