'use strict';
// Independent documentary reader. Never imports, parses as code or invokes submitted sources.
// Finite input names come only from the two fixed source manifests and author nonself seal.
// Embedded JSON host/runtime paths remain opaque.
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const PREP='docs/papers211_215_sequence/qa/private_checkpoint_executor_preparation03';
const AUDIT='docs/papers211_215_sequence/qa/private_checkpoint_executor_source_audit03';
const must=(c,m)=>{if(!c)throw Error(m)};
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const statkey=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
const inputs=new Map();
function obtain(rel) {
  must(typeof rel==='string'&&/^[A-Za-z0-9_.\/-]+$/.test(rel)&&!rel.startsWith('/')&&rel.split('/').every(p=>p!==''&&p!=='.'&&p!=='..'),'unsafe finite name');
  const abs=path.join(ROOT,rel); must(fs.realpathSync.native(abs)===abs,'physical alias '+rel);
  const a=fs.lstatSync(abs,{bigint:true});must(a.isFile()&&!a.isSymbolicLink(),'nonregular '+rel);
  const fd=fs.openSync(abs,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let b,c,data;
  try {b=fs.fstatSync(fd,{bigint:true});data=fs.readFileSync(fd);c=fs.fstatSync(fd,{bigint:true});}
  finally{fs.closeSync(fd);}
  const d=fs.lstatSync(abs,{bigint:true});
  const keys=[a,b,c,d].map(statkey);
  must(keys.every(x=>JSON.stringify(x)===JSON.stringify(keys[0])),'unstable key '+rel);
  must(data.length===Number(a.size),'short read '+rel);
  const result={path:rel,bytes:data.length,sha256:digest(data),stat:keys[0],four_keys_equal:true,physical:true};
  const prior=inputs.get(rel); if(prior) must(JSON.stringify(prior)===JSON.stringify(result),'repeat drift '+rel);
  inputs.set(rel,result);return data;
}
function manifest(rel,local=false) {
 const raw=obtain(rel).toString('utf8');must(raw.endsWith('\n'),'unterminated manifest');
 const rows=raw.slice(0,-1).split('\n').map(line=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.\/-]+)$/.exec(line);must(m,'bad manifest row');return{sha256:m[1],path:local?path.posix.join(PREP,m[2]):m[2]};});
 must(new Set(rows.map(x=>x.path)).size===rows.length,'duplicate manifest path');
 for(const row of rows)must(digest(obtain(row.path))===row.sha256,'manifest hash mismatch '+row.path);
 return rows;
}
const seal=manifest(PREP+'/SHA256SUMS',true);
const review=manifest(PREP+'/REVIEW_INPUTS.sha256');
const source=manifest(PREP+'/SOURCE_INPUTS.sha256');
must(seal.length===19&&review.length===12&&source.length===15,'manifest count');
function namesUnder(rel){const names=[];for(const d of fs.readdirSync(path.join(ROOT,rel),{withFileTypes:true})){const n=rel+'/'+d.name;must(!d.isSymbolicLink(),'package alias');if(d.isDirectory())names.push(...namesUnder(n));else{must(d.isFile(),'package nonregular');names.push(n);}}return names.sort();}
must(JSON.stringify(namesUnder(PREP))===JSON.stringify([...seal.map(x=>x.path),PREP+'/SHA256SUMS'].sort()),'nonself author seal incomplete');
for(const rel of [
 'docs/papers211_215_sequence/qa/control_before_residual46_accepted01/STATE.before.md',
 'docs/papers211_215_sequence/qa/control_before_residual46_accepted01/PIPELINE.before.md',
 AUDIT+'/PLAN.md',AUDIT+'/input_reader.cjs'
])obtain(rel);
const chosen=JSON.parse(obtain('docs/papers211_215_sequence/qa/private_checkpoint03_scope_root01/CHOSEN_SCOPE.json'));
const core=JSON.parse(obtain('docs/papers211_215_sequence/qa/private_checkpoint03_scope_preparation01/FINAL_CANDIDATE_INVENTORY.json'));
const bridge=JSON.parse(obtain('docs/papers211_215_sequence/qa/private_checkpoint03_scope_preparation01/OPTIONAL_OLD_SCOUT_BRIDGE_INVENTORY.json'));
const shape=v=>Object.fromEntries(Object.entries(v).map(([k,x])=>[k,Array.isArray(x)?{type:'array',length:x.length,first:x[0]}:x&&typeof x==='object'?{type:'object',keys:Object.keys(x),first:Object.entries(x)[0]}:x]));
console.log(JSON.stringify({schema:'independent-executor03-documentary-inputs-v1',read_mode:'whole-byte named workspace reads only; no submitted-source import, AST, execution, hostpath follow, Git or checkpoint operation',author_seal:{payload:seal.length,complete:true},review_inputs:review.length,source_inputs:source.length,inputs:[...inputs.values()].sort((a,b)=>a.path.localeCompare(b.path)),metadata_shapes:{chosen:shape(chosen),core:shape(core),bridge:shape(bridge)}},null,2));

