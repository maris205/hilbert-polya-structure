'use strict';
const fs=require('fs'),crypto=require('crypto'),path=require('path');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const R='docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_root01/';
const old=JSON.parse(JSON.parse(fs.readFileSync(ROOT+R+'CHECK_NATIVE.json','utf8')).result.output);
const own=['ROOT_READS_NATIVE.json','ROOT_REPLAYS_NATIVE.json','DISPLAY_LIMITS_NATIVE.json','CHECK_ROOT.cjs','CHECK_NATIVE.json','RECEPTION.md','CLOSE.cjs'];
const allowed=new Set([...old.keys.map(k=>k.path),...own.map(n=>R+n)]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs'];
const meta=s=>Object.fromEntries(fields.map(f=>[f,s[f].toString()]));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const keys=new Map();function ok(v,m){checks++;if(!v)throw Error(m);}
function read(p){ok(allowed.has(p),'finite documentation');ok(!p.includes('/p213_minimal_observer_enabled01/')&&!p.includes('/p213_minimal_observer_probe01/'),'no future operands');const a=fs.lstatSync(ROOT+p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'regular document');const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);let b,k;try{const f=fs.fstatSync(fd,{bigint:true});b=fs.readFileSync(fd);const g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(ROOT+p,{bigint:true});for(const s of[f,g,z])ok(JSON.stringify(meta(a))===JSON.stringify(meta(s)),'same-fd/path full identity');ok(BigInt(b.length)===a.size,'whole bytes');k={path:p,type:'regular',...meta(a),bytes:b.length,sha256:sha(b)};}finally{fs.closeSync(fd);}if(keys.has(p))ok(JSON.stringify(keys.get(p))===JSON.stringify(k),'repeated whole key');keys.set(p,k);return b;}
for(const k of old.keys){read(k.path);ok(JSON.stringify(k)===JSON.stringify(keys.get(k.path)),'all original root keys unchanged');}
for(const n of own)read(R+n);
const receipt=read(R+'RECEPTION.md').toString('utf8');let links=0;
for(const m of receipt.matchAll(/\]\(([^)]+)\)/g)){ok(!m[1].includes('/')&&own.includes(m[1]),'local receipt link');read(R+m[1]);links++;}
ok(JSON.stringify(fs.readdirSync(ROOT+R).filter(n=>!['CLOSING_NATIVE.json','SHA256SUMS'].includes(n)).sort())===JSON.stringify(own.slice().sort()),'complete preclosing own inventory');
for(const p of [...keys.keys()])read(p);
console.log(JSON.stringify({scope:'ROOT_EXACT_PROSPECTIVE_RECEPTION_CLOSING_ONLY',checks,keys:[...keys.values()],keyCount:keys.size,originalRootKeysPreserved:old.keys.length,receiptKey:keys.get(R+'RECEPTION.md'),links,operationGranted:false}));
