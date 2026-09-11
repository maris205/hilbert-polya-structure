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
const OWN_INPUTS=['ROOT_READS_NATIVE.json','ROOT_WEB_NATIVE.json','REPLAY_NATIVE.json','check_receipt.cjs'];
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
const packages=[manifest(D,19,{bytes:1630,sha256:'523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40'}),manifest(A,12,{bytes:989,sha256:'be307853b648f2fba9f532e072f19f6cc64e51760e9b38759c59d060d54a6819'})];
same(packages.map(p=>p.physical_bytes),[1322853,553906],'both entire physical packages');
for(const p of EXTERNAL)read(p);for(const n of OWN_INPUTS)read(OWN+n);
for(const p of [D+'INPUTS.sha256',A+'INPUT_PINS.sha256']){
 const rows=read(p).toString().trimEnd().split('\n').map(l=>{const m=/^([a-f0-9]{64})  (.+)$/.exec(l);need(m,'strict original pin syntax');return{sha256:m[1],path:m[2]};});
 need(rows.length===(p.startsWith(D)?27:48),'complete original pin census');for(const r of rows)need(hash(read(r.path))===r.sha256,'whole original input pin');
}
const first=json(D+'DOCUMENTARY_CHECK01.json'),closing=json(D+'CLOSING_KEYS.json'),native=json(D+'DOCUMENTARY_NATIVE.json'),nclose=json(D+'CLOSING_NATIVE.json');
const independent=json(A+'RESULT.json'),inative=json(A+'DATA_NATIVE.json'),iclose=json(A+'CLOSING_RESULT.json'),inc=json(A+'CLOSING_NATIVE.json');
const replays=json(OWN+'REPLAY_NATIVE.json');need(replays.records.length===2,'exact two actual documentary invocations');
const [rr,rc]=replays.records;need(rr.actual_return.chunk_id==='e0e8c0'&&rr.actual_return.exit_code===0&&!Object.hasOwn(rr.actual_return,'session_id'),'actual complete root 8093 replay');
need(rc.actual_return.chunk_id==='8e9996'&&rc.actual_return.exit_code===0&&!Object.hasOwn(rc.actual_return,'session_id'),'actual complete root sealed closure');
need(rr.request.cmd==='node '+A+'check_data.cjs'&&rc.request.cmd==='node '+A+'close_data.cjs --sealed','exact scoped documentary commands');
const rvalue=JSON.parse(rr.actual_return.output),cvalue=JSON.parse(rc.actual_return.output);
need(rvalue.checks===8093&&rvalue.whole_file_keys===50&&cvalue.checks===3692&&cvalue.whole_file_keys===61&&cvalue.mode==='SEALED','actual root scopes');
const fn=native.records.filter(r=>r.result?.chunk_id==='b5bb72');need(fn.length===1&&fn[0].result.exit_code===0,'real author first native');
pair('author first original stdout',Buffer.from(fn[0].result.output),read(D+'DOCUMENTARY_CHECK01.json'));
need(nclose.actual_return.chunk_id==='1be80e'&&nclose.actual_return.exit_code===0,'real author closing native');
pair('author closing original stdout',Buffer.from(nclose.actual_return.output),read(D+'CLOSING_KEYS.json'));
need(inative.actual_return.chunk_id==='cdfd40'&&inative.actual_return.exit_code===0,'real independent data native');
pair('independent original whole stdout',Buffer.from(inative.actual_return.output),read(A+'RESULT.json'));
pair('root 8093 replay whole stdout',Buffer.from(rr.actual_return.output),read(A+'RESULT.json'));
need(inc.actual_return.chunk_id==='219a11'&&inc.actual_return.exit_code===0&&iclose.mode==='PRESEAL'&&iclose.checks===3263,'real historical preseal DATA only');
pair('independent historical preseal stdout',Buffer.from(inc.actual_return.output),read(A+'CLOSING_RESULT.json'));
let historical=0;const normalize=p=>p.startsWith(ROOT+'/')?p.slice(ROOT.length+1):p;
for(const [role,list] of [['author_first',first.rows],['author_closing',closing.keys],['independent',independent.keys],['independent_preseal',iclose.keys],['root_replay',rvalue.keys],['root_sealed',cvalue.keys]]){
 for(const k of list){const p=normalize(k.path);need(allowed.has(p),'historical key is fixed DATA');
 for(const n of ['lstat_before','fstat_before','fstat_after','lstat_after']){same(Object.keys(k[n]),F,'all original ten fields');same(k[n],k.lstat_before,'all original structures agree');for(const v of Object.values(k[n]))need(typeof v==='string'&&/^-?(0|[1-9][0-9]*)$/.test(v)&&v!=='-0','exact original decimal');}
 need(Number.isSafeInteger(k.fd)&&k.fd>=0&&k.close_succeeded===true,'original actual fd/close');
 if(role==='author_first')need(k.whole_eof===true,'historical API whole-read only');else need(k.eof===true&&k.last_read_return===0,'original explicit zero-return EOF');
 if(role==='author_first'&&p===D+'BINDING.disabled.json'){const v=json(p),old=JSON.parse(JSON.stringify(v));for(const r of Object.values(old.sources))r.pin=null;const b=Buffer.from(JSON.stringify(old,null,2)+'\n');same(pin(b),{bytes:k.bytes,sha256:k.sha256},'one declared pre-source-pin binding original');need(String(b.length)===k.lstat_before.size,'old binding size preserved');}
 else{same(pin(read(p)),{bytes:k.bytes,sha256:k.sha256},'entire original byte key unchanged');same(keys.get(p).lstat_before,k.lstat_before,'all actual original ten fields unchanged');}historical++;
 }
}
need(historical===302,'83 author plus108 independent plus111 root full-key occurrences');
const findings=json(A+'FINDINGS.json');same(findings.census,{critical:0,major:0,minor:0,open:0},'exact source-only census');need(findings.findings.length===0&&findings.operational_grant===false&&findings.verdict==='ACCEPT_EXACT_DISABLED_S0_SOURCE_POLICY_BOUNDARY','independent no-operation verdict');
const reads=json(OWN+'ROOT_READS_NATIVE.json');let comparedReads=0;for(const r of [...reads.prior_records,...reads.current_records]){
 const cmd=r.command||r.request?.cmd,m=/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_./-]+)$/.exec(cmd||'');
 if(!m||!allowed.has(m[3])||r.result.exit_code!==0)continue;
 need(!r.result.output.includes('Warning: truncated output'),'selected semantic source read is complete');
 const b=read(m[3]),lines=b.toString().split(/(?<=\n)/),part=Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join(''));
 pair('root selected exact lines '+r.result.chunk_id,Buffer.from(r.result.output),part);comparedReads++;
}
need(comparedReads===22,'all full new source/contracts and current audit/source ranges bound');
console.log(JSON.stringify({schema:'p212-root-source-reception-data-v1',status:'PASS_DOCUMENTARY_ORIGINALS_ONLY_SOURCE_POLICY_IN_RECEPTION',checks,packages,keys_count:keys.size,historical_key_occurrences:historical,raw_pairs:pairs,raw_pair_bytes:pairs.reduce((n,p)=>n+p.bytes,0),root_selected_raw_read_pairs:comparedReads,source_census:findings.census,actual_submitted_source_execution:false,host_private_raw_future_path_queries:false,operational_grant:false,keys:[...keys.values()]},null,2));
