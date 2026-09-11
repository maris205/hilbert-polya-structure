'use strict';
// Independent audit-package closure only. Fixed workspace DATA, not submitted
// source execution. The sealed mode validates the final nonself layout.
const fs=require('node:fs'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA='docs/papers211_215_sequence/qa/';
const D=QA+'p212_minimal_contract01_source_preparation01/',OWN=QA+'p212_minimal_contract01_source_audit01/';
const PRE=['DATA_NATIVE.json','FINDINGS.json','INPUT_PINS.sha256','ORIGIN.md','PRIMARY_NATIVE.json','REPORT.md','RESULT.json','SELECTED_READ_NATIVE.json','check_data.cjs','close_data.cjs'];
const SUBMITTED=['ARCHIVAL_DISPOSITIONS.json','BINDING.disabled.json','CLOSING_KEYS.json','CLOSING_NATIVE.json','CONTRACT.md','DEPENDENCY_GATE.md','DIRECTORY_REQUEST.disabled.json','DOCUMENTARY_CHECK01.json','DOCUMENTARY_NATIVE.json','FILE_REQUEST.disabled.json','HANDOFF.md','INPUTS.sha256','OBLIGATION_DELTA.md','PRIMARY_SOURCE_EVIDENCE.json','REQUEST.disabled.json','SHA256SUMS','SOURCE_ORIGIN.md','capture.js','file_keys.mjs','receive.mjs'];
const ORIGINALS=['.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md','docs/papers211_215_sequence/PROBLEM_ANCHOR.md','docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md','docs/papers204_208_sequence/ARTIFACT_CONTRACT.md',
 ...['REPORT.md','INPUTS.sha256'].map(n=>QA+'p212_runtime_obligation_diagnosis01/'+n),QA+'p212_s0_source_commission_root01/DECISION.md',
 ...['SOURCE_CONTRACT.md','RUNTIME_PREPARATION.md','FRONTIER_REASONING.md','product_capture.js','driver.js','outer_contract.py','node_preload.js','companions/CAPTURE_CONTRACT.json'].map(n=>QA+'p212_keyed_stdin_source_delta01/'+n),
 ...['FRONTIER.json','CONTRACT.md'].map(n=>QA+'p212_keyed_stdin_cuda_alias_source_delta01/'+n),QA+'p212_dependency_query_driver_preparation01/STAGED_CAPTURE_AND_CLOSURE.md',QA+'p212_dependency_source_root01/RECEPTION.md',
 ...['PLAN.md','SELECTOR_OBLIGATIONS.json'].map(n=>QA+'p212_build_dependency_source_preparation01/'+n),QA+'p212_initial_build_preparation01/PLAN.md',QA+'p213_minimal_observer_source_delta01/CONTRACT.md',
 ...['RECEPTION.md','DECISION.json'].map(n=>QA+'p212_trusted_product_boundary_root01/'+n),QA+'p212_keyed_stdin_source_root01/RECEPTION.md',QA+'p212_author_pair_runtime_reception01/RECEPTION.md'];
const EXTERNAL=[...SUBMITTED.map(n=>D+n),...ORIGINALS];
const sealed=process.argv[2]==='--sealed';
if(process.argv.length!==(sealed?3:2))throw new Error('exact no-argument preseal or --sealed mode');
const FINAL=[...PRE,'CLOSING_RESULT.json','CLOSING_NATIVE.json'].sort();
const ALLOW=new Set([...EXTERNAL,...[...FINAL,'SHA256SUMS'].map(n=>OWN+n)]);
let checks=0;const need=(v,m)=>{checks++;if(!v)throw new Error(m);};
const same=(a,b,m)=>need(JSON.stringify(a)===JSON.stringify(b),m);
const hash=b=>crypto.createHash('sha256').update(b).digest('hex'),pin=b=>({bytes:b.length,sha256:hash(b)});
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const fields=s=>Object.fromEntries(F.map(k=>{need(typeof s[k]==='bigint','real documentary integer');return[k,s[k].toString()];}));
const bytes=new Map(),keys=new Map();
function read(p){need(ALLOW.has(p),'fixed documentary file only');if(bytes.has(p))return bytes.get(p);
 const full=ROOT+'/'+p,a=fs.lstatSync(full,{bigint:true}),A=fields(a);need(a.isFile()&&!a.isSymbolicLink(),'physical document leaf');
 const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let raw,row;
 try{const b=fs.fstatSync(fd,{bigint:true}),B=fields(b);need(b.isFile(),'physical document handle');same(A,B,'expected same-fd before content');
 const chunks=[],buffer=Buffer.alloc(65536);let count,calls=0,total=0;do{count=fs.readSync(fd,buffer,0,buffer.length,null);calls++;need(count>=0&&count<=65536,'actual read count');if(count){total+=count;need(total<=8388608,'8 MiB document bound');chunks.push(Buffer.from(buffer.subarray(0,count)));}}while(count!==0);
 raw=Buffer.concat(chunks);const Z=fields(fs.fstatSync(fd,{bigint:true})),L=fields(fs.lstatSync(full,{bigint:true}));same(A,L,'stable lexical after');same(B,Z,'stable same-fd after');need(BigInt(total)===b.size&&raw.length===total,'whole EOF count');
 row={path:p,...pin(raw),lstat_before:A,fstat_before:B,fstat_after:Z,lstat_after:L,fd,read_calls:calls,last_read_return:count,eof:true,close_succeeded:false};}finally{fs.closeSync(fd);}row.close_succeeded=true;bytes.set(p,raw);keys.set(p,row);return raw;}
const json=p=>{const b=read(p),v=JSON.parse(b.toString());need(Buffer.from(JSON.stringify(v,null,2)+'\n').equals(b),'whole canonical JSON data');return v;};
same(fs.readdirSync(ROOT+'/'+OWN).sort(),(sealed?[...FINAL,'SHA256SUMS']:PRE).sort(),'exact current audit layout');
for(const n of PRE)read(OWN+n);
const result=json(OWN+'RESULT.json'),native=json(OWN+'DATA_NATIVE.json');
need(native.actual_return.chunk_id==='cdfd40'&&native.actual_return.exit_code===0,'actual successful independent documentary native');
need(Buffer.from(native.actual_return.output).equals(read(OWN+'RESULT.json')),'complete actual independent stdout/result raw equality');
need(result.status==='PASS_FIXED_DOCUMENTARY_DATA_ONLY_NOT_OPERATIONAL'&&result.checks===8093&&result.whole_file_keys===50,'exact independent original census');
same(result.keys.map(k=>k.path).sort(),[...EXTERNAL,OWN+'check_data.cjs',OWN+'ORIGIN.md'].sort(),'all fifty expected original key paths');
for(const old of result.keys){same(pin(read(old.path)),{bytes:old.bytes,sha256:old.sha256},'whole original file unchanged');same(keys.get(old.path).lstat_before,old.lstat_before,'all ten actual original documentary fields unchanged');}
const pins=read(OWN+'INPUT_PINS.sha256').toString().trimEnd().split('\n').map(l=>{const m=/^([a-f0-9]{64})  (.+)$/.exec(l);need(m,'strict independent pin row');return{sha256:m[1],path:m[2]};});
same(pins.map(r=>r.path).sort(),EXTERNAL.slice().sort(),'all forty-eight external inputs, no own circular pin');for(const r of pins)need(hash(read(r.path))===r.sha256,'every independent external pin');
const submittedSeal=read(D+'SHA256SUMS');same(pin(submittedSeal),{bytes:1630,sha256:'523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40'},'immutable submitted seal');
same(fs.readdirSync(ROOT+'/'+D).sort(),SUBMITTED,'unchanged entire submitted twenty-file layout');
for(const line of submittedSeal.toString().trimEnd().split('\n')){const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);need(m&&SUBMITTED.includes(m[2])&&m[2]!=='SHA256SUMS','strict submitted manifest row');need(hash(read(D+m[2]))===m[1],'entire submitted payload still sealed');}
const findings=json(OWN+'FINDINGS.json');same(findings.census,{critical:0,major:0,minor:0,open:0},'exact accepted source census');need(findings.findings.length===0&&findings.operational_grant===false,'no finding deletion or grant');
need(findings.verdict==='ACCEPT_EXACT_DISABLED_S0_SOURCE_POLICY_BOUNDARY','exact source-only verdict');
let payloadBytes=null,seal=null;
if(sealed){const old=json(OWN+'CLOSING_RESULT.json'),n=json(OWN+'CLOSING_NATIVE.json');need(n.actual_return.exit_code===0,'actual successful preseal completion');need(Buffer.from(n.actual_return.output).equals(read(OWN+'CLOSING_RESULT.json')),'complete original closing stdout raw equality');
 need(old.mode==='PRESEAL'&&old.preclosing_payloads===10,'original preseal scope');for(const k of old.keys){need(ALLOW.has(k.path),'old closing whitelist');same(pin(read(k.path)),{bytes:k.bytes,sha256:k.sha256},'all original closing content unchanged');same(keys.get(k.path).lstat_before,k.lstat_before,'all closing ten-field keys unchanged');}
 const raw=read(OWN+'SHA256SUMS');seal=pin(raw);const rows=raw.toString().trimEnd().split('\n').map(l=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);need(m,'strict nonself audit seal row');return{sha256:m[1],path:m[2]};});same(rows.map(r=>r.path),FINAL,'every final payload, never manifest itself');payloadBytes=0;for(const r of rows){const b=read(OWN+r.path);payloadBytes+=b.length;need(hash(b)===r.sha256,'all complete audit payloads');}}
console.log(JSON.stringify({schema:'p212-independent-s0-audit-document-closure-v1',status:'PASS_DOCUMENTARY_CLOSURE_ONLY',mode:sealed?'SEALED':'PRESEAL',checks,preclosing_payloads:10,final_payloads:sealed?12:null,whole_file_keys:keys.size,external_inputs:48,source_census:findings.census,submitted_source_executed:false,host_private_raw_future_paths_queried:false,operational_grant:false,payload_bytes:payloadBytes,seal,keys:[...keys.values()],limits:'Independent same-fd explicit-EOF ten-field workspace documentary checks only; old native outputs compared as whole bytes. No operational or runtime acceptance. This result and its original native are distinct later nonself manifest members in preseal mode.'},null,2));
