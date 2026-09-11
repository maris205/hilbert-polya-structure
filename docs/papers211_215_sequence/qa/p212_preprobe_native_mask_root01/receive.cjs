'use strict';
// Finite workspace-only documentary reception. No archived command execution.
const fs=require('fs'),crypto=require('crypto'),path=require('path'),assert=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const A='docs/papers211_215_sequence/qa/p212_preprobe_native_mask_analysis01/';
const R='docs/papers211_215_sequence/qa/p212_preprobe_native_mask_root01/';
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const need=(x,m)=>{assert.ok(x,m);checks++;};
const eq=(a,b,m)=>{assert.deepEqual(a,b,m);checks++;};
const cache=new Map(),keys=new Map();
function read(p){
 need(p.startsWith('docs/')&&!p.split('/').some(x=>!x||x==='.'||x==='..'),'workspace document only');
 const full=ROOT+p,st=fs.lstatSync(full,{bigint:true});
 need(st.isFile()&&!st.isSymbolicLink()&&st.size<4000000n,'bounded physical document');
 const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 let b;try{eq(meta(fs.fstatSync(fd,{bigint:true})),meta(st),'opened key');b=fs.readFileSync(fd);
  eq(meta(fs.fstatSync(fd,{bigint:true})),meta(st),'same-fd end key');
 }finally{fs.closeSync(fd);}
 eq(meta(fs.lstatSync(full,{bigint:true})),meta(st),'lexical end key');eq(BigInt(b.length),st.size,'whole length');
 const key={path:p,bytes:b.length,sha256:hash(b),metadata:meta(st)};
 if(keys.has(p))eq(key,keys.get(p),'repeat full key');
 keys.set(p,key);cache.set(p,b);return b;
}
function object(p){return JSON.parse(read(p));}
const seal=read(A+'SHA256SUMS');
eq(hash(seal),'cbfaf50d24cf97dcb1c6e91357316b12b3a85cdb774b7e75dc01075657914ab0','exact frozen analysis seal');
need(seal.toString().endsWith('\n')&&!seal.toString().endsWith('\n\n'),'strict final LF');
const members=[];
for(const line of seal.toString().slice(0,-1).split('\n')){
 const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);need(m&&m[2]!=='SHA256SUMS','nonself member');
 need(!members.includes(m[2]),'unique member');members.push(m[2]);eq(hash(read(A+m[2])),m[1],'whole payload');
}
eq(members.length,8,'eight original payloads');
eq(fs.readdirSync(ROOT+A).sort(),[...members,'SHA256SUMS'].sort(),'complete physical packet membership');
const pins=cache.get(A+'INPUT_SHA256SUMS').toString('utf8');
// Existing author parser used trimEnd: disclose, do not claim native strict syntax.
need(pins.endsWith('\n\n')&&!pins.endsWith('\n\n\n'),'exact preserved extra input-pin LF');
const pinRows=[];
for(const line of pins.slice(0,-2).split('\n')){
 const m=/^([a-f0-9]{64})  (docs\/[A-Za-z0-9_./-]+)$/.exec(line);need(m,'exact input pin');
 need(!pinRows.includes(m[2]),'unique input');pinRows.push(m[2]);eq(hash(read(m[2])),m[1],'complete pinned input');
}
eq(pinRows.length,23,'twenty-three source/data inputs');
const archived=object(A+'CHECK_NATIVE.json'),fresh=object(R+'ROOT_CHECKER_REPLAY_NATIVE.json');
eq(archived.result.exit_code,0,'actual author document check exit');eq(fresh.response.exit_code,0,'actual root document replay exit');
need(Buffer.from(archived.result.output).equals(Buffer.from(fresh.response.output)),'actual complete raw checker pair');
const checked=JSON.parse(archived.result.output);
eq(checked.checks,3181,'actual checker count');eq(checked.input_count,23,'actual checker input count');
eq(checked.inputs_before,checked.inputs_after,'complete author byte-key endpoints');
for(const key of checked.keys){const b=read(key.path);eq(b.length,key.bytes,'recorded whole bytes');eq(hash(b),key.sha256,'recorded whole hash');eq(keys.get(key.path).metadata,key.endpoint,'recorded ten-field key');}
const native=[];
function collect(x,where){
 if(!x||typeof x!=='object')return;
 const res=x.result||x.response;
 if(x.request&&res&&typeof res.output==='string'&&res.chunk_id){native.push({where,request:x.request,result:res});return;}
 if(typeof x.output==='string'&&x.chunk_id){native.push({where,request:null,result:x});return;}
 for(const [k,v]of Object.entries(x))collect(v,where+'/'+k);
}
for(const name of ['READS_NATIVE.json','CHECK_NATIVE.json','FIRST_DOCUMENT_CHECK_NATIVE.json','CLOSING_NATIVE.json'])collect(object(A+name),name);
const compared=[],unclaimed=[];
for(const row of native){
 const out=Buffer.from(row.result.output),req=row.request;
 const item={where:row.where,chunk_id:row.result.chunk_id,exit_code:row.result.exit_code,bytes:out.length,sha256:hash(out),request_present:!!req};
 const m=req&&/^sed -n '(\d+),(\d+)p' (docs\/[A-Za-z0-9_./-]+)$/.exec(req.cmd);
 if(m&&cache.has(m[3])&&row.result.exit_code===0){
  const lines=cache.get(m[3]).toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];
  const expected=Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join(''));
  if(out.equals(expected)){compared.push({...item,path:m[3],first:Number(m[1]),last:Number(m[2])});continue;}
  item.reason='preserved earlier draft or capped return; not exact current source read';
 }else item.reason=!req?'raw native only, no full request supplied':'not a successful single pinned sed; no command replay claimed';
 unclaimed.push(item);
}
const rawSummary=object('docs/papers211_215_sequence/qa/p212_preprobe_observation_root01/INITIAL_RAW_INTAKE_NATIVE.json');
need(JSON.stringify(rawSummary).includes('375140'),'prior summary whole original bound, not a new private read');
const finalKeys=[...keys.values()].sort((a,b)=>a.path.localeCompare(b.path));
for(const key of finalKeys){read(key.path);eq(keys.get(key.path),key,'final whole key');}
process.stdout.write(JSON.stringify({status:'MASK_ANALYSIS_DOCUMENTARY_RECEPTION_PASS_NOT_SOURCE_OR_RUNTIME_GRANT',checks,
 original_payloads:8,input_pins:23,distinct_whole_keys:keys.size,keys:finalKeys,raw_checker_bytes:Buffer.byteLength(archived.result.output),
 archived_native_count:native.length,verified_raw_sed_count:compared.length,verified_raw_sed:compared,other_native_scope:unclaimed,
 input_pin_format:'one preserved extra trailing empty line; exact scoped removal for parsing only; no original edit or strict-native input-pin PASS',
 no_private_host_reads:true,no_submitted_source_execution:true,no_new_observation:true},null,2)+'\n');
