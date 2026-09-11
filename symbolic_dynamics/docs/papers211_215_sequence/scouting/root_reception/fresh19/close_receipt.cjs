'use strict';
// Root fixed-workspace DOCUMENT reception. Never import/evaluate any submitted
// source or query its embedded operational/host/private/future path strings.
const fs=require('node:fs'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',D="docs/papers211_215_sequence/scouting/finite_residual_fresh19/",A="docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/",OWN="docs/papers211_215_sequence/scouting/root_reception/fresh19/";
const EXTERNAL=["docs/papers211_215_sequence/scouting/finite_residual_fresh19/PLAN.md","docs/papers211_215_sequence/scouting/finite_residual_fresh19/SOURCE_READS.md","docs/papers211_215_sequence/scouting/finite_residual_fresh19/PROOF_AND_DISPOSITION.md","docs/papers211_215_sequence/scouting/finite_residual_fresh19/HANDOFF.md","docs/papers211_215_sequence/scouting/finite_residual_fresh19/SOURCE_TOOL_RETURNS.json","docs/papers211_215_sequence/scouting/finite_residual_fresh19/LOCAL_TOOL_RETURNS.json","docs/papers211_215_sequence/scouting/finite_residual_fresh19/INPUT_PINS.json","docs/papers211_215_sequence/scouting/finite_residual_fresh19/ARTIFACT_CHECK.json","docs/papers211_215_sequence/scouting/finite_residual_fresh19/manifest_sha256.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/ORIGIN_AND_SCOPE.md","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/REVIEW.md","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/FINDINGS.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/INPUT_PINS.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/PRIMARY_RETURNS.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/LOCAL_READ_RETURNS.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/check_artifacts.mjs","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/ARTIFACT_CHECK.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/ARTIFACT_CHECK_NATIVE.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/close_check.mjs","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/CLOSING_CHECK.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/CLOSING_NATIVE.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/MANIFEST.sha256","docs/papers211_215_sequence/scouting/finite_metric_reconstruction_scout01/PROOF_PACKAGE.md","docs/papers211_215_sequence/scouting/finite_metric_reconstruction_scout01/SOURCE_READS.md","docs/papers122_126_sequence/scouting/combinatorial/SCOUT.md","docs/papers117_121_sequence/scouting/ALGEBRAIC_PHASE2B_SCOUT.md","docs/papers204_208_sequence/scouting/algebra/PROOF_NOTES.md","papers/106-synchronous-mis-polarity-dynamics/main.tex","docs/papers211_215_sequence/scouting/set_code_lane/PROOF_PACKAGE.md","docs/papers204_208_sequence/scouting/finite_systems_eighteenth/PROOF_AND_ADAPTERS.md","docs/papers211_215_sequence/scouting/finite_residual_fresh18/PROOF_AND_DISPOSITION.md","docs/papers211_215_sequence/scouting/finite_residual_fresh17/PROOF_PACKAGE.md"];
const OWN_INPUTS=["CHECK_NATIVE.json","FAILED_CHECK01.cjs","FAILED_NATIVE01.json","RECEPTION.md","REPLAY_NATIVE.json","RESULT.json","ROOT_READS_NATIVE.json","ROOT_WEB_NATIVE.json","check_receipt.cjs","close_receipt.cjs"];
const allowed=new Set([...EXTERNAL,...OWN_INPUTS.map(n=>OWN+n)]);
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
let checks=0;const need=(v,m)=>{checks++;if(!v)throw new Error(m);};
const same=(a,b,m)=>need(JSON.stringify(a)===JSON.stringify(b),m);
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const pin=b=>({bytes:b.length,sha256:hash(b)});
const raw=new Map(),keys=new Map(),pairs=[];
const fields=s=>Object.fromEntries(F.map(k=>{need(typeof s[k]==='bigint','actual exact documentary integer');return[k,s[k].toString()];}));
function read(p){
 need(allowed.has(p),'literal documentary whitelist: '+p);if(raw.has(p))return raw.get(p);
 const full=ROOT+'/'+p,l=fs.lstatSync(full,{bigint:true}),L=fields(l);need(l.isFile()&&!l.isSymbolicLink(),'regular physical document');
 const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let bytes,row;
 try{const b=fs.fstatSync(fd,{bigint:true}),B=fields(b);need(b.isFile(),'regular descriptor');same(L,B,'same fd before content');
 const pieces=[],buf=Buffer.alloc(65536);let n,total=0,calls=0;do{n=fs.readSync(fd,buf,0,buf.length,null);calls++;need(n>=0&&n<=65536,'actual read count');if(n){total+=n;need(total<=8388608,'8MiB per-document bound');pieces.push(Buffer.from(buf.subarray(0,n)));}}while(n!==0);
 bytes=Buffer.concat(pieces);const Z=fields(fs.fstatSync(fd,{bigint:true})),E=fields(fs.lstatSync(full,{bigint:true}));same(B,Z,'same fd after zero-return EOF');same(L,E,'stable lexical endpoint');need(bytes.length===total&&BigInt(total)===b.size,'whole count');
 need(Buffer.from(bytes.toString('utf8'),'utf8').equals(bytes),'whole UTF8 roundtrip for any text comparison');
 row={path:p,...pin(bytes),lstat_before:L,fstat_before:B,fstat_after:Z,lstat_after:E,fd,read_calls:calls,last_read_return:n,eof:true,close_succeeded:false};
 }finally{fs.closeSync(fd);}row.close_succeeded=true;raw.set(p,bytes);keys.set(p,row);return bytes;
}
const json=p=>{const b=read(p),v=JSON.parse(b.toString());need(Buffer.from(JSON.stringify(v,null,2)+'\n').equals(b),'canonical whole JSON data '+p);return v;};
function pair(label,a,b){need(a.equals(b),'entire RAW equality '+label);pairs.push({label,...pin(a)});}
function manifest(dir,n,sealPin){
 const b=read(dir+'SHA256SUMS');same(pin(b),sealPin,'received commissioned seal');
 need(b.toString().endsWith('\n'),'seal final LF');const entries=b.toString().slice(0,-1).split('\n').map(l=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);need(m,'strict flat nonself seal row');return {sha256:m[1],name:m[2]};});
 need(entries.length===n&&new Set(entries.map(e=>e.name)).size===n,'complete distinct nonself rows');
 same(fs.readdirSync(ROOT+'/'+dir).sort(),[...entries.map(e=>e.name),'SHA256SUMS'].sort(),'exact frozen physical layout');
 let size=b.length;for(const e of entries){need(e.name!=='SHA256SUMS','no seal self member');const x=read(dir+e.name);need(hash(x)===e.sha256,'whole payload hash');size+=x.length;}return {directory:dir,payloads:n,files:n+1,physical_bytes:size,seal:pin(b)};
}


same(fs.readdirSync(ROOT+'/'+OWN).sort(),OWN_INPUTS,'exact ten root preclosing payloads');
for(const p of EXTERNAL)read(p);for(const n of OWN_INPUTS)read(OWN+n);
const r=json(OWN+'RESULT.json'),n=json(OWN+'CHECK_NATIVE.json');
need(n.actual_return.chunk_id==='b81043'&&n.actual_return.exit_code===0,'actual root successful receipt native');
pair('actual root whole stdout',Buffer.from(n.actual_return.output),read(OWN+'RESULT.json'));
need(r.checks===2294&&r.keys_count===38&&r.raw_pairs.length===35&&r.raw_pair_bytes===255754&&r.count_delta===0,'exact root zero-entry receipt');
for(const k of r.keys){same(pin(read(k.path)),{bytes:k.bytes,sha256:k.sha256},'every original reception byte key unchanged');same(keys.get(k.path).lstat_before,k.lstat_before,'all original root ten-field metadata unchanged');}
same(pin(read(D+'manifest_sha256.json')),{bytes:1447,sha256:'6e2f1f2508b46072b07b68d1023d5a0813739a1855003524eca649b3282883f6'},'unchanged author seal');
same(pin(read(A+'MANIFEST.sha256')),{bytes:1019,sha256:'67734126376f76b95a607b6f5dce97f745d44ffcb6d5b2ed15e0470ce12ca32d'},'unchanged independent seal');
const failed=json(OWN+'FAILED_NATIVE01.json');need(failed.actual_return.chunk_id==='de4f97'&&failed.actual_return.exit_code===1&&failed.actual_return.output.includes('selected full native read range'),'actual first checker failure unchanged');
const doc=read(OWN+'RECEPTION.md').toString();need(doc.includes('ZERO_COUNT_DELTA')&&doc.includes('HOLD_EXTERNAL')&&doc.includes('missing initial command request'),'scope and failure limits retained');
const path=require('node:path');let links=0;for(const m of doc.matchAll(/\]\(([^)]+)\)/g)){if(/^https:\/\//.test(m[1]))continue;const p=path.posix.normalize(OWN+m[1]);need(allowed.has(p),'local receipt link within fixed documents');read(p);links++;}
console.log(JSON.stringify({schema:'fresh19-root-documentary-closing-v1',status:'PASS_PRESEAL_DOCUMENTARY_CLOSURE',checks,keys_count:keys.size,received_keys:38,preclosing_payloads:10,local_links:links,count_delta:0,raw_pairs:pairs,payloads:OWN_INPUTS.map(n=>({path:n,...pin(read(OWN+n))})),keys:[...keys.values()]},null,2));
