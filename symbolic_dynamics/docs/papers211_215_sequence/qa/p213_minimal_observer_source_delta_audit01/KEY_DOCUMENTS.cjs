// Fixed workspace documentary baseline only. Embedded candidate paths are NEVER dereferenced.
'use strict';
const fs=require('node:fs'),crypto=require('node:crypto');
const root='docs/papers211_215_sequence/qa/';
const specs=[
 {dir:root+'p213_minimal_observer_source_delta01/',seal:'98ed7e008e16eef37dfb37dcbb00060cef97479957ef25f4df939b6e3314ee34',payloads:24},
 {dir:root+'p213_minimal_observer_binding_preparation01/',seal:'98f27ead29fa8862591d3b5a4cc6813eea1f09814f5d03a5edce0571ab278d96',payloads:21}
];
const extra=[root+'p213_runtime_design_root01/RECEPTION.md',root+'p213_runtime_preparation01/DESIGN.md',root+'p213_runtime_design_audit01/REPORT.md',root+'p213_runtime_design_audit01/FINDINGS.json',root+'p213_minimal_observer_source_root01/RECEPTION.md'];
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
let checks=0;const keys=new Map(),bytes=new Map();
function ok(v,m){checks++;if(!v)throw Error(m);}
function sha(b){return crypto.createHash('sha256').update(b).digest('hex');}
function meta(s){return Object.fromEntries(fields.map(n=>{ok(typeof s[n]==='bigint','integer');return[n,String(s[n])];}));}
function read(p){
 ok(p.startsWith(root+'p213_')||p===root+'root_replays/p211_author_pair_01/child01/RUNTIME_BEFORE.json','document selection');
 const a=fs.lstatSync(p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink()&&a.size<=10000000n,'bounded regular document');
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 let before,after,b;try{const s=fs.fstatSync(fd,{bigint:true});ok(s.isFile(),'regular fd');before=meta(s);ok(JSON.stringify(before)===JSON.stringify(meta(a)),'path/fd');b=fs.readFileSync(fd);after=meta(fs.fstatSync(fd,{bigint:true}));}finally{fs.closeSync(fd);}
 ok(JSON.stringify(before)===JSON.stringify(after)&&JSON.stringify(before)===JSON.stringify(meta(fs.lstatSync(p,{bigint:true}))),'endpoints');
 ok(BigInt(b.length)===BigInt(before.size),'whole read');
 const k={path:p,bytes:b.length,sha256:sha(b),metadata:before};if(keys.has(p))ok(JSON.stringify(k)===JSON.stringify(keys.get(p)),'unchanged document');
 keys.set(p,k);bytes.set(p,b);return b;
}
function parse(b,local){
 const s=b.toString('utf8');ok(s.endsWith('\n')&&!s.endsWith('\n\n'),'strict seal LF');
 const seen=new Set();return s.slice(0,-1).split('\n').map(l=>{
 const m=/^([0-9a-f]{64})  ([A-Za-z0-9_./-]+)$/.exec(l);ok(m&&!m[2].startsWith('/')&&!m[2].split('/').includes('..'),'strict pin');
 if(local)ok(!m[2].includes('/')&&m[2]!=='SHA256SUMS','nonself basename');
 ok(!seen.has(m[2]),'unique pin');seen.add(m[2]);return{sha256:m[1],path:m[2]};});
}
const inventories=[],inputs=[];
for(const spec of specs){
 const seal=read(spec.dir+'SHA256SUMS');ok(sha(seal)===spec.seal,'fixed sealed source/proposal');
 const rows=parse(seal,true);ok(rows.length===spec.payloads,'payload count');
 const names=fs.readdirSync(spec.dir).sort();ok(JSON.stringify(names)===JSON.stringify([...rows.map(x=>x.path),'SHA256SUMS'].sort()),'physical inventory');
 for(const x of rows)ok(sha(read(spec.dir+x.path))===x.sha256,'sealed payload');
 const pins=parse(bytes.get(spec.dir+'INPUTS.sha256'),false);inputs.push({path:spec.dir+'INPUTS.sha256',pins});
 for(const x of pins)ok(sha(read(x.path))===x.sha256,'original input pin');
 inventories.push({dir:spec.dir,payloads:rows.length,files:names.length,bytes:names.reduce((n,p)=>n+bytes.get(spec.dir+p).length,0),seal_sha256:spec.seal});
}
for(const p of extra)read(p);
const before=[...keys.values()];for(const k of before)read(k.path);
process.stdout.write(JSON.stringify({status:'DOCUMENTARY_BASELINE_ONLY',checks,host_candidate_paths_read:false,reviewed_programs_executed:false,source_acceptance:false,inventories,inputs,keys:[...keys.values()]},null,2)+'\n');
