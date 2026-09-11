'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const R='docs/papers211_215_sequence/scouting/root_reception/fresh18/';
const n=JSON.parse(fs.readFileSync(path.join(ROOT,R+'CHECK_NATIVE.json'),'utf8'));
const prior=JSON.parse(n.result.output);
const own=['ROOT_READS_NATIVE.json','ROOT_WEB_NATIVE.json','ROOT_REPLAY_NATIVE.json','ROOT_AUDIT_READS_NATIVE.json','ROOT_AUDIT_REPLAY_NATIVE.json','CHECK_ROOT.cjs','CHECK_NATIVE.json','RECEPTION.md','CLOSE.cjs'];
const allowed=new Set([...prior.keys.map(k=>k.path),...own.map(p=>R+p)]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
let checks=0;const keys=new Map();function ok(v,m){checks++;if(!v)throw Error(m);}
function read(p){
 ok(allowed.has(p),'fixed documentary path');const full=path.resolve(ROOT,p);
 const a=fs.lstatSync(full,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'regular');
 const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);let b,k;
 try{const f=fs.fstatSync(fd,{bigint:true});b=fs.readFileSync(fd);
  const g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(full,{bigint:true});
  for(const s of[f,g,z])ok(same(meta(a),meta(s)),'same fd and full metadata');
  ok(BigInt(b.length)===a.size,'whole EOF');
  k={path:p,resolved_path:full,sha256:sha(b),metadata:meta(a)};
 }finally{fs.closeSync(fd);}
 if(keys.has(p))ok(same(keys.get(p),k),'whole repeated key');keys.set(p,k);return b;
}
ok(n.result.exit_code===0&&prior.checks===766&&prior.keyCount===47,'actual root original reception');
for(const k of prior.keys){read(k.path);ok(same(k,keys.get(k.path)),'all 47 earlier complete keys unchanged');}
for(const p of own)read(R+p);
ok(same(fs.readdirSync(path.join(ROOT,R)).filter(x=>!['CLOSING_NATIVE.json','SHA256SUMS'].includes(x)).sort(),own.slice().sort()),'complete preclosing inventory');
let links=0;
for(const m of read(R+'RECEPTION.md').toString('utf8').matchAll(/\]\(([^)]+)\)/g)){ok(own.includes(m[1]),'finite local receipt link');read(R+m[1]);links++;}
for(const p of [...keys.keys()])read(p);
console.log(JSON.stringify({scope:'ROOT_FRESH18_DOCUMENTARY_RECEPTION_CLOSING_ONLY',checks,keys:[...keys.values()],keyCount:keys.size,priorKeysPreserved:47,links,receipt:keys.get(R+'RECEPTION.md'),closedAttemptDelta:0,scientificExecution:false,operationPermission:false}));

