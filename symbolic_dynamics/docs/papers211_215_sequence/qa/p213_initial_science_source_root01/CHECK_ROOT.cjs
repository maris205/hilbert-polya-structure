'use strict';
// Root source/documentary reception. Never execute operational paths or Python.
const fs=require('fs'),crypto=require('crypto'),path=require('path');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const Q='docs/papers211_215_sequence/qa/';
const P=Q+'p213_initial_science_preparation01/';
const A=Q+'p213_initial_science_source_audit01/';
const R=Q+'p213_initial_science_source_root01/';
const OLD_PATHS=["docs/papers211_215_sequence/qa/p213_initial_science_preparation01/BINDING.proposed.json","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/CHECK_NATIVE.json","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/COLLECTOR_REUSE_CHECK.json","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/CREATION_NATIVE.json","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/DEPENDENCY_CONTRACT.md","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/EXECUTION_SEQUENCE.md","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/HANDOFF.md","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/PREPARATION.md","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/REQUEST.disabled.json","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SOURCE_DELTA.md","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SOURCE_INPUTS.sha256","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SOURCE_TEXT_READS_NATIVE.json","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/WORKSPACE_READS_NATIVE.json","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.initial.disabled.sh","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.replay01.disabled.sh","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.replay02.disabled.sh","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/run_science.disabled.py","docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SHA256SUMS","papers/213-receiver-limited-cyclic-transfer/verify.py","papers/213-receiver-limited-cyclic-transfer/VERIFICATION_PARAMETERS.json","papers/213-receiver-limited-cyclic-transfer/OUTPUT_SCHEMA.md","papers/213-receiver-limited-cyclic-transfer/SCIENTIFIC_DEPENDENCIES.md","papers/213-receiver-limited-cyclic-transfer/RUNTIME_PLAN.md","papers/213-receiver-limited-cyclic-transfer/REVIEW_INTERFACES.md","docs/papers211_215_sequence/P213_THEOREM_CONTRACT.md","docs/papers211_215_sequence/qa/p213_source_parameter_root01/RECEPTION.md","docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/CONTRACT.md","docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/BINDING_FORMAT.md","docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/BINDING.runtime_literal.json","docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/observe.proposed.py.txt","docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/capture.proposed.sh.txt","docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_root01/RECEPTION.md","docs/papers211_215_sequence/qa/p213_minimal_observer_probe_reception_root01/RECEPTION.md","docs/papers211_215_sequence/qa/p213_minimal_observer_probe_reception_root01/SHA256SUMS"];
const AUDIT_NAMES=['SHA256SUMS','CLOSURE_NATIVE.json','CLOSE_DOCUMENTS.cjs','INPUTS.sha256','CHECK_NATIVE.json','READ_NATIVE.json','HANDOFF.md','FINDINGS.json','AUDIT.md','CHECK_FAILURE01_NATIVE.json','CHECK_SOURCE_FAILURE01.cjs.txt','CHECK_SOURCE.cjs','PLAN.md'];
const OWN=['ROOT_READS_NATIVE.json','ROOT_AUDIT_READS_NATIVE.json','ROOT_REPLAY_NATIVE.json','CHECK_ROOT.cjs'];
const extra=[Q+'p213_minimal_observer_enabled_root01/CHECK_ROOT.cjs',Q+'p213_minimal_observer_enabled_root01/CLOSE.cjs'];
const allowed=new Set([...OLD_PATHS,...AUDIT_NAMES.map(n=>A+n),...OWN.map(n=>R+n),...extra]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(f=>[f,s[f].toString()]));
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const keys=new Map(),buffers=new Map(),pairs=[];
function ok(v,m){checks++;if(!v)throw Error(m);}
function read(p){
 ok(allowed.has(p),'fixed documentary allowlist '+p);
 const a=fs.lstatSync(ROOT+p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'regular no-link document');
 const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 let b,k;try{const f=fs.fstatSync(fd,{bigint:true});b=fs.readFileSync(fd);
 const g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(ROOT+p,{bigint:true});
 for(const s of[f,g,z])ok(same(meta(a),meta(s)),'same-fd/full-endpoint metadata');
 ok(BigInt(b.length)===a.size,'whole EOF');
 k={path:p,metadata:meta(a),bytes:b.length,sha256:sha(b)};
 }finally{fs.closeSync(fd);}
 if(keys.has(p))ok(same(k,keys.get(p)),'unchanged repeated complete key');
 keys.set(p,k);buffers.set(p,b);return b;
}
const get=p=>buffers.has(p)?buffers.get(p):read(p);
const js=p=>JSON.parse(get(p).toString('utf8'));
function raw(a,b,label){a=Buffer.isBuffer(a)?a:Buffer.from(a,'utf8');b=Buffer.isBuffer(b)?b:Buffer.from(b,'utf8');ok(a.equals(b),'raw '+label);pairs.push({label,bytes:a.length,sha256:sha(a)});}
function nativeKey(k,label){
 const b=get(k.path),actual=keys.get(k.path);
 ok(k.complete===true&&k.eof===true&&k.closed===true,'actual full EOF/close '+label);
 ok(b.length===k.byte_count&&sha(b)===k.sha256,'actual whole byte pin '+label);
 for(const name of ['begin','fd_before','fd_after','after_read'])ok(same(k[name],actual.metadata),'all old ten fields '+label+' '+name);
}
for(const p of allowed)read(p);
const packets=[];
for(const[prefix,digest,count,bytes]of[
 [P,'ef1e95d740634c6531706aaa3b4fda0f0f99fbb14f604c80bc24f3d3235a7cdf',17,868945],
 [A,'27890badfbebbac1db8ddb4046d98c847555c7cc62995253b1ebf23064c10dcf',12,954662]]){
 const seal=get(prefix+'SHA256SUMS');ok(sha(seal)===digest,'external nonself seal');
 const text=seal.toString('utf8');ok(text.endsWith('\n'),'seal LF');
 const rows=text.slice(0,-1).split('\n').map(line=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);ok(!!m,'strict nonself row');return{sha256:m[1],name:m[2]};});
 ok(rows.length===count&&new Set(rows.map(r=>r.name)).size===count&&!rows.some(r=>r.name==='SHA256SUMS'),'exact nonself count');
 ok(same(fs.readdirSync(ROOT+prefix).sort(),[...rows.map(r=>r.name),'SHA256SUMS'].sort()),'complete physical inventory');
 let total=seal.length;for(const r of rows){const b=get(prefix+r.name);ok(sha(b)===r.sha256,'all sealed payloads');total+=b.length;}
 ok(total===bytes,'complete physical bytes');packets.push({prefix,payloads:count,files:count+1,bytes:total,seal:digest});
}
const old=js(A+'CHECK_NATIVE.json'),od=JSON.parse(old.native.output);
ok(old.native.exit_code===0&&old.native.chunk_id==='a0f17d'&&od.checks_count===133&&od.failed.length===0&&od.checks.every(c=>c.pass===true),'actual independent source check');
ok(same(od.keys.map(k=>k.path),OLD_PATHS),'exact 34 original input order');
for(const k of od.keys)nativeKey(k,k.path);
const pins=get(A+'INPUTS.sha256').toString('utf8');
raw(pins,od.keys.map(k=>k.sha256+'  '+k.path+'\n').join(''),'all 34 independent input pins');
const replay=js(R+'ROOT_REPLAY_NATIVE.json'),rd=JSON.parse(replay.result.output);
ok(replay.request.cmd==='node '+A+'CHECK_SOURCE.cjs'&&replay.result.exit_code===0&&replay.result.chunk_id==='b16558'&&!replay.result.session_id,'actual root source checker replay');
raw(replay.result.output,old.native.output,'complete 133-check root replay stdout');
ok(rd.checks_count===133&&rd.failed.length===0&&rd.keys.length===34,'entire root replay result');
for(const k of rd.keys)nativeKey(k,'root replay '+k.path);
const close=js(A+'CLOSURE_NATIVE.json'),cd=JSON.parse(close.native.output);
ok(close.native.chunk_id==='dbc5da'&&close.native.exit_code===0&&cd.checks_count===84&&cd.failed.length===0&&cd.checks.every(c=>c.pass===true),'actual preseal 84 result received AS DATA');
ok(cd.preseal_payloads.length===11,'original preseal 11-payload stage not current replay');
for(const e of cd.preseal_payloads){const b=get(A+e.name);ok(b.length===e.bytes&&sha(b)===e.sha256,'complete historical preseal payload retained');}
const fail=js(A+'CHECK_FAILURE01_NATIVE.json'),fd=JSON.parse(fail.native.output);
ok(fail.native.chunk_id==='cbbb40'&&fail.native.exit_code===1&&fd.failed.length===1,'original failed checker preserved');
for(const k of fd.keys)nativeKey(k,'original failed documentary key');
const diagnosis=JSON.parse(fail.diagnosis.native.output);
ok(fail.diagnosis.native.chunk_id==='07ed99'&&fail.diagnosis.native.exit_code===0&&diagnosis.first_difference===28800,'original boundary diagnostic');
const findings=js(A+'FINDINGS.json');
ok(findings.disposition==='SOURCE_ONLY_PASS_FOR_ROOT_RECEPTION'&&Object.values(findings.current_census).every(v=>v===0)&&findings.source_findings.length===0,'zero actual source finding census');
ok(findings.source_authorship_by_reviewer===false&&findings.prior_familiarity_disclosed===true&&findings.enabled_source_acceptance===false&&findings.operational_authority===false,'nonauthor disclosed exact restricted scope');
ok(sha(get(A+'HANDOFF.md'))==='2fb72a401702047ec1a71be139da66808fb292ddaabcf84c42c58be5770e4e4c','exact independent handoff');
ok(sha(get(A+'AUDIT.md'))==='7d5c2ba9f62a312aeae3f424ba0e0f67df5d1310c602a63bc87a09a9c89a727d','exact independent semantic audit');
const requests=js(P+'REQUEST.disabled.json');
ok(requests.request_cmd===null&&requests.root_grant===null&&requests.operation_authorized===false,'old preparation still disabled');
ok(requests.stages.every(s=>s.request_cmd===null&&s.root_grant===null&&s.accepted===false),'all three actual stage grants remain absent');
const readPackets=[js(R+'ROOT_READS_NATIVE.json'),js(R+'ROOT_AUDIT_READS_NATIVE.json')];
const rootRecords=readPackets.flatMap(p=>p.records),rootExceptions=[],sourceParts=[];
let rootReadPairs=0;
for(const r of rootRecords){
 ok(r.result&&typeof r.result.output==='string'&&typeof r.command==='string','actual root read record');
 if(r.result.exit_code!==0||r.result.output.startsWith('Warning: truncated output')){rootExceptions.push({command:r.command,chunk:r.result.chunk_id,exit:r.result.exit_code,truncated:r.result.output.startsWith('Warning: truncated output')});continue;}
 const m=/^sed -n '(\d+),(\d+)p' (.+)$/.exec(r.command);
 if(!m)continue;
 ok(allowed.has(m[3]),'root fixed read premise');
 const b=get(m[3]),lines=b.toString('utf8').split(/(?<=\n)/);
 raw(r.result.output,lines.slice(Number(m[1])-1,Number(m[2])).join(''),'complete root read '+r.result.chunk_id);rootReadPairs++;
 if(m[3]===P+'run_science.disabled.py')sourceParts.push({from:Number(m[1]),to:Number(m[2]),output:r.result.output});
}
sourceParts.sort((a,b)=>a.from-b.from);
ok(sourceParts.length===10&&sourceParts[0].from===1&&sourceParts.at(-1).to===3083,'ten complete root wrapper ranges');
for(let i=1;i<sourceParts.length;i++)ok(sourceParts[i].from===sourceParts[i-1].to+1,'contiguous source ranges');
raw(sourceParts.map(p=>p.output).join(''),get(P+'run_science.disabled.py'),'entire root 3083-line source reception');
ok(rootExceptions.length===2&&rootExceptions.some(e=>e.chunk==='f45f2a'&&e.exit===2)&&rootExceptions.some(e=>e.chunk==='340ac0'&&e.truncated),'own failed basename/truncated archive read kept without false full-read claim');
const rootScience=rootRecords.filter(r=>/^sed -n '\d+,\d+p' papers\/213-receiver-limited-cyclic-transfer\/verify.py$/.test(r.command));
raw(rootScience.map(r=>r.result.output).join(''),get('papers/213-receiver-limited-cyclic-transfer/verify.py'),'whole unchanged 451-line verifier root read');
const ar=js(A+'READ_NATIVE.json').records;
ok(ar.length===50,'50 independent actual archived reads');
let independentReadPairs=0;
for(const r of ar){const m=/^sed -n '(\d+),(\d+)p' (.+)$/.exec(r.request.cmd);
 if(!m||!allowed.has(m[3])||r.native.exit_code!==0||r.native.output.startsWith('Warning: truncated output'))continue;
 const t=get(m[3]).toString('utf8').split(/(?<=\n)/).slice(Number(m[1])-1,Number(m[2])).join('');
 raw(r.native.output,t,'independent original full read '+r.native.chunk_id);independentReadPairs++;
}
for(const p of [...keys.keys()])read(p);
console.log(JSON.stringify({scope:'ROOT_P213_EXACT_DISABLED_COMPILE_WRAPPER_SOURCE_POLICY_RECEPTION_NOT_OPERATION',checks,keys:[...keys.values()],keyCount:keys.size,sealedPackets:packets,oldFullKeyOccurrencesReceived:102,rootReplayChecks:133,historicalPresealChecksReceived:84,historicalPresealRerun:false,rawPairs:pairs,rawPairCount:pairs.length,rawPairedBytes:pairs.reduce((s,p)=>s+p.bytes,0),rootReadPairs,independentReadPairs,rootExceptions,currentSourceCensus:findings.current_census,completeWrapperLines:3083,scienceBytes:17539,scienceParametersUnchanged:{carriers:30,states:461},futureOperandsUsed:false,enabledSourceAccepted:false,operationGranted:false,runtimeOrScienceAccepted:false,externalStatus:'HOLD_EXTERNAL'}));

