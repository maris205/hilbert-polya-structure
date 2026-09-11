'use strict';
// Documentary equality checks only; never run, import, AST-parse, or test Python.
const fs=require('fs'), crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics/';
const own='docs/papers211_215_sequence/qa/private_checkpoint_d01_source_audit01/';
const prep='docs/papers211_215_sequence/qa/private_checkpoint_d01_preparation01/';
let checks=0;
const need=(x,m)=>{checks++;if(!x)throw Error(m);};
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,s[k].toString()]));
const json=p=>JSON.parse(fs.readFileSync(root+p,'utf8'));
const a=json(own+'INPUT_BEFORE_NATIVE.json'),z=json(own+'INPUT_AFTER_NATIVE.json');
need(a.response.exit_code===0&&z.response.exit_code===0,'Inventory native exits');
const before=JSON.parse(a.response.output),after=JSON.parse(z.response.output);
need(JSON.stringify(before)===JSON.stringify(after),'Recorded complete input endpoints differ');
const keys=[...before.input_package,...before.author_referenced_inputs,...before.context_inputs];
const known=new Map();
for(const key of keys){if(known.has(key.path))need(JSON.stringify(known.get(key.path))===JSON.stringify(key),'Duplicate conflicting input');known.set(key.path,key);}
const cached=new Map();
for(const [p,key] of known){
  need(p.startsWith('docs/')&&!p.split('/').some(x=>x==='..'||x==='.'),'Documentary whitelist path');
  const s=fs.lstatSync(root+p,{bigint:true});
  need(s.isFile()&&!s.isSymbolicLink()&&JSON.stringify(meta(s))===JSON.stringify(key.metadata),'Pre-read metadata '+p);
  const fd=fs.openSync(root+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try{
    need(JSON.stringify(meta(fs.fstatSync(fd,{bigint:true})))===JSON.stringify(key.metadata),'Opened metadata '+p);
    const b=fs.readFileSync(fd);
    need(b.length===key.bytes&&hash(b)===key.sha256,'Whole input bytes '+p);
    need(JSON.stringify(meta(fs.fstatSync(fd,{bigint:true})))===JSON.stringify(key.metadata)
      &&JSON.stringify(meta(fs.lstatSync(root+p,{bigint:true})))===JSON.stringify(key.metadata),'Post-read metadata '+p);
    need(Buffer.from(b.toString('utf8'),'utf8').equals(b),'Lossless textual input '+p);
    cached.set(p,b.toString('utf8'));
  }finally{fs.closeSync(fd);}
}
const verified=[],unclaimed=[];
function checkRecord(label,r){
  const req=r.request,res=r.result||r.response;
  need(req&&res&&typeof req.cmd==='string'&&typeof res.output==='string','Actual record format '+label);
  const m=/^sed -n '(\d+),(\d+)p' (docs\/[A-Za-z0-9_./-]+)$/.exec(req.cmd);
  if(!m||!known.has(m[3])){unclaimed.push({label,request:req,reason:'Not a single whitelisted sed; not re-executed or claimed as slice equality'});return;}
  const lines=cached.get(m[3]).match(/[^\n]*\n|[^\n]+$/g)||[];
  const expected=lines.slice(Number(m[1])-1,Number(m[2])).join('');
  need(res.exit_code===0&&res.output===expected,'Exact original sed stdout '+label);
  verified.push({label,path:m[3],first:Number(m[1]),last:Number(m[2]),stdout_bytes:Buffer.byteLength(res.output),sha256:hash(Buffer.from(res.output))});
}
for(const file of ['SOURCE_READS_NATIVE.json','DOCUMENT_READS_NATIVE.json','CLOSING_NATIVE.json']){
  const x=JSON.parse(cached.get(prep+file));
  need(Array.isArray(x.records),'Author native records '+file);
  x.records.forEach((r,i)=>checkRecord('author/'+file+'/'+i,r));
}
const ownReads=json(own+'DOCUMENTARY_NATIVE.json');
ownReads.records.forEach((r,i)=>checkRecord('reviewer/'+i,r));
checkRecord('reviewer/source_native_reread',json(own+'SOURCE_NATIVE_REREAD.json'));
const docs=JSON.parse(cached.get(prep+'DOCUMENT_READS_NATIVE.json'));
for(const [index,start,end] of [[19,0,3],[20,3,6],[21,6,10]]){
  const r=ownReads.records[index],x=JSON.parse(r.response.output);
  need(r.response.exit_code===0&&x.whole_sha256===known.get(prep+'DOCUMENT_READS_NATIVE.json').sha256
    &&x.selected_records_start_inclusive===start&&x.selected_records_end_exclusive===end
    &&JSON.stringify(x.records)===JSON.stringify(docs.records.slice(start,end)),
    'Complete archival record slice '+index);
}
process.stdout.write(JSON.stringify({status:'DOCUMENTARY_EQUALITIES_PASS_NOT_SOURCE_ACCEPTANCE',
 checks,distinct_complete_inputs:known.size,recorded_input_endpoints_identical:true,
 input_keys_rechecked_now:true,verified_sed_slice_count:verified.length,
 verified_sed_slices:verified,non_slice_records_unclaimed:unclaimed,
 submitted_sources_executed:false,commands_from_archives_executed:false,
 runtime_or_host_observation:false},null,2)+'\n');
