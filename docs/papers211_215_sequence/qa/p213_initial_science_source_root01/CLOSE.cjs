'use strict';
const fs=require('fs'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const R='docs/papers211_215_sequence/qa/p213_initial_science_source_root01/';
const old=JSON.parse(fs.readFileSync(ROOT+R+'CHECK_NATIVE.json','utf8'));
const prior=JSON.parse(old.result.output);
const own=['ROOT_READS_NATIVE.json','ROOT_AUDIT_READS_NATIVE.json','ROOT_REPLAY_NATIVE.json','CHECK_ROOT.cjs','CHECK_NATIVE.json','RECEPTION.md','CLOSE.cjs'];
const allowed=new Set([...prior.keys.map(k=>k.path),...own.map(n=>R+n)]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(f=>[f,s[f].toString()]));
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const keys=new Map();function ok(v,m){checks++;if(!v)throw Error(m);}
function read(p){
 ok(allowed.has(p),'fixed documentary permission');
 const a=fs.lstatSync(ROOT+p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'regular leaf');
 const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);let b,k;
 try{const f=fs.fstatSync(fd,{bigint:true});b=fs.readFileSync(fd);const g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(ROOT+p,{bigint:true});
 for(const s of[f,g,z])ok(same(meta(a),meta(s)),'same-fd/full-endpoint complete ten fields');
 ok(BigInt(b.length)===a.size,'whole EOF');ok(Buffer.from(b.toString('utf8'),'utf8').equals(b),'complete byte-exact UTF8 reversibility');
 k={path:p,metadata:meta(a),bytes:b.length,sha256:sha(b)};
 }finally{fs.closeSync(fd);}
 if(keys.has(p))ok(same(k,keys.get(p)),'whole repeated key');keys.set(p,k);return b;
}
ok(old.result.exit_code===0&&prior.checks===1556&&prior.keyCount===53,'actual root reception');
for(const k of prior.keys){read(k.path);ok(same(k,keys.get(k.path)),'all 53 root keys unchanged');}
for(const n of own)read(R+n);
ok(same(fs.readdirSync(ROOT+R).filter(n=>!['CLOSING_NATIVE.json','SHA256SUMS'].includes(n)).sort(),own.slice().sort()),'complete own preclosing layout');
let links=0;
for(const m of read(R+'RECEPTION.md').toString('utf8').matchAll(/\]\(([^)]+)\)/g)){ok(own.includes(m[1]),'finite local receipt link');read(R+m[1]);links++;}
for(const p of [...keys.keys()])read(p);
console.log(JSON.stringify({scope:'ROOT_P213_DISABLED_SOURCE_RECEPTION_CLOSING',checks,keys:[...keys.values()],keyCount:keys.size,priorFullKeysPreserved:53,wholeUTF8Reversibility:true,links,receipt:keys.get(R+'RECEPTION.md'),operationPermission:false,enabledCopyAcceptance:false}));

