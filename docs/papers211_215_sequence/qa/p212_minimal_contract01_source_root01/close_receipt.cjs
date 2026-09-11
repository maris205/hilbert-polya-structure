'use strict';
// Root fixed-workspace DOCUMENT reception. Never import/evaluate any submitted
// source or query its embedded operational/host/private/future path strings.
const fs=require('node:fs'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',D="docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/",A="docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/",OWN="docs/papers211_215_sequence/qa/p212_minimal_contract01_source_root01/";
const EXTERNAL=[
  ".agents/skills/symbolic-dynamics-research/SKILL.md",
  "docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md",
  "docs/papers204_208_sequence/ARTIFACT_CONTRACT.md",
  "docs/papers211_215_sequence/PROBLEM_ANCHOR.md",
  "docs/papers211_215_sequence/qa/p212_author_pair_runtime_reception01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_build_dependency_source_preparation01/PLAN.md",
  "docs/papers211_215_sequence/qa/p212_build_dependency_source_preparation01/SELECTOR_OBLIGATIONS.json",
  "docs/papers211_215_sequence/qa/p212_dependency_query_driver_preparation01/STAGED_CAPTURE_AND_CLOSURE.md",
  "docs/papers211_215_sequence/qa/p212_dependency_source_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_initial_build_preparation01/PLAN.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/CONTRACT.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/FRONTIER.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/FRONTIER_REASONING.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/RUNTIME_PREPARATION.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/SOURCE_CONTRACT.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/companions/CAPTURE_CONTRACT.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/driver.js",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/node_preload.js",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/outer_contract.py",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/product_capture.js",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/CLOSING_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/CLOSING_RESULT.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/DATA_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/FINDINGS.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/INPUT_PINS.sha256",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/ORIGIN.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/PRIMARY_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/REPORT.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/RESULT.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/SELECTED_READ_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/check_data.cjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_audit01/close_data.cjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/ARCHIVAL_DISPOSITIONS.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/BINDING.disabled.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/CLOSING_KEYS.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/CLOSING_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/CONTRACT.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DEPENDENCY_GATE.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DIRECTORY_REQUEST.disabled.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DOCUMENTARY_CHECK01.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DOCUMENTARY_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/FILE_REQUEST.disabled.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/HANDOFF.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/INPUTS.sha256",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/OBLIGATION_DELTA.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/PRIMARY_SOURCE_EVIDENCE.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/REQUEST.disabled.json",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/SOURCE_ORIGIN.md",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/capture.js",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/file_keys.mjs",
  "docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/receive.mjs",
  "docs/papers211_215_sequence/qa/p212_runtime_obligation_diagnosis01/INPUTS.sha256",
  "docs/papers211_215_sequence/qa/p212_runtime_obligation_diagnosis01/REPORT.md",
  "docs/papers211_215_sequence/qa/p212_s0_source_commission_root01/DECISION.md",
  "docs/papers211_215_sequence/qa/p212_trusted_product_boundary_root01/DECISION.json",
  "docs/papers211_215_sequence/qa/p212_trusted_product_boundary_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/CONTRACT.md",
  "docs/research_state/WORKFLOW.md"
];
const OWN_INPUTS=["CHECK_NATIVE.json","RECEPTION.md","REPLAY_NATIVE.json","RESULT.json","ROOT_READS_NATIVE.json","ROOT_WEB_NATIVE.json","check_receipt.cjs","close_receipt.cjs"];
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

same(fs.readdirSync(ROOT+'/'+OWN).sort(),OWN_INPUTS,'exact eight-member preclosing root layout');
for(const p of EXTERNAL)read(p);for(const n of OWN_INPUTS)read(OWN+n);
const r=json(OWN+'RESULT.json'),native=json(OWN+'CHECK_NATIVE.json');
need(native.actual_return.chunk_id==='0a0857'&&native.actual_return.exit_code===0,'actual root original reception success');
pair('whole root reception stdout',Buffer.from(native.actual_return.output),read(OWN+'RESULT.json'));
need(r.checks===20155&&r.keys_count===65&&r.historical_key_occurrences===302&&r.raw_pairs.length===27&&r.raw_pair_bytes===556759,'unchanged received actual root census');
for(const k of r.keys){same(pin(read(k.path)),{bytes:k.bytes,sha256:k.sha256},'whole first root input unchanged');same(keys.get(k.path).lstat_before,k.lstat_before,'all ten first-root fields unchanged');}
for(const [p,n,sha]of [[D,19,'523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40'],[A,12,'be307853b648f2fba9f532e072f19f6cc64e51760e9b38759c59d060d54a6819']]){
 const b=read(p+'SHA256SUMS');manifest(p,n,{bytes:b.length,sha256:sha});
}
const path=require('node:path');let links=0;const text=read(OWN+'RECEPTION.md').toString();
for(const m of text.matchAll(/\]\(([^)]+)\)/g)){
 if(/^https:\/\//.test(m[1]))continue;
 const p=path.posix.normalize(OWN+m[1]);need(allowed.has(p),'receipt link resolves only to received fixed input');read(p);links++;
}
need(text.includes('ACCEPT_EXACT_DISABLED_SOURCE_AND_NEW_S0_POLICY')&&text.includes('HOLD_OPERATIONAL / HOLD_EXTERNAL')&&text.includes('No operation grant is issued'),'actual explicit root policy with no operational grant');
console.log(JSON.stringify({schema:'p212-root-source-reception-closing-v1',status:'PASS_PRESEAL_DOCUMENTARY_CLOSURE',checks,preclosing_payloads:8,received_keys:65,keys_count:keys.size,links,raw_pairs:pairs,actual_submitted_source_execution:false,host_private_raw_future_path_queries:false,operational_grant:false,payloads:OWN_INPUTS.map(n=>({path:n,...pin(read(OWN+n))})),keys:[...keys.values()]},null,2));
