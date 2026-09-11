'use strict';
// Root data-only reception. Never follow operational strings in the documents.
const fs=require('fs'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const QA='docs/papers211_215_sequence/qa/';
const P=QA+'p213_minimal_observer_enabled_preparation01/';
const A=QA+'p213_minimal_observer_enabled_preparation_audit01/';
const R=QA+'p213_minimal_observer_enabled_root01/';
const OWN=['CHECK_ROOT.cjs','ROOT_READS_NATIVE.json','ROOT_REPLAYS_NATIVE.json','DISPLAY_LIMITS_NATIVE.json'];
let checks=0;const keys=new Map(),buffers=new Map(),pairs=[];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function ok(x,m){checks++;if(!x)throw Error(m);}
const priorNative=JSON.parse(fs.readFileSync(ROOT+A+'CLOSING_NATIVE.json','utf8'));
ok(priorNative.result.exit_code===0,'independent closing exit');
const prior=JSON.parse(priorNative.result.output);
ok(prior.keys.length===75&&prior.checks===1848,'fixed independent closing census');
const allowed=new Set([...prior.keys.map(k=>k.path),A+'CLOSING_NATIVE.json',A+'SHA256SUMS',...OWN.map(n=>R+n)]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs'];
const meta=s=>Object.fromEntries(fields.map(f=>[f,s[f].toString()]));
function acquire(p){
  ok(allowed.has(p),'fixed documentary allowlist '+p);
  ok(!p.includes('/p213_minimal_observer_enabled01/')&&!p.includes('/p213_minimal_observer_probe01/'),'no future operand');
  const a=fs.lstatSync(ROOT+p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'regular no-link '+p);
  const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);let b,k;
  try{
    const f=fs.fstatSync(fd,{bigint:true});b=fs.readFileSync(fd);
    const g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(ROOT+p,{bigint:true});
    for(const s of [f,g,z])ok(JSON.stringify(meta(a))===JSON.stringify(meta(s)),'same-fd/full-endpoint '+p);
    ok(BigInt(b.length)===a.size,'whole EOF length');
    k={path:p,type:'regular',...meta(a),bytes:b.length,sha256:sha(b)};
  }finally{fs.closeSync(fd);}
  if(keys.has(p))ok(JSON.stringify(k)===JSON.stringify(keys.get(p)),'whole repeated key');
  keys.set(p,k);buffers.set(p,b);return b;
}
const get=p=>buffers.has(p)?buffers.get(p):acquire(p);
const js=p=>JSON.parse(get(p).toString('utf8'));
const raw=(a,b,label)=>{a=Buffer.isBuffer(a)?a:Buffer.from(a);b=Buffer.isBuffer(b)?b:Buffer.from(b);ok(a.equals(b),'raw '+label);pairs.push({label,bytes:a.length,sha256:sha(a)});};
for(const k of prior.keys){acquire(k.path);ok(JSON.stringify(k)===JSON.stringify(keys.get(k.path)),'every 75-field-key record unchanged');}
for(const n of OWN)acquire(R+n);
const sealed=[];
for(const [prefix,digest,count,size]of [[P,'daa0bc55ab3e1f8f2e9cc97ff846508434b0ac6f65e6ed84e9559f5fad9f049d',32,1177073],[A,'2f720e6f52f37d730b3c9165d374151accb635242946f79159f589da7b425354',23,667554]]){
  const b=get(prefix+'SHA256SUMS');ok(sha(b)===digest,'external full seal '+prefix);
  const s=b.toString('utf8');ok(s.endsWith('\n'),'strict seal LF');const rows=s.slice(0,-1).split('\n').map(l=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);ok(!!m,'strict flat nonself grammar');return {name:m[2],sha256:m[1]};});
  ok(rows.length===count&&new Set(rows.map(x=>x.name)).size===count,'exact unique payload count');
  ok(!rows.some(x=>x.name==='SHA256SUMS'),'nonself seal');
  ok(JSON.stringify(fs.readdirSync(ROOT+prefix).sort())===JSON.stringify([...rows.map(x=>x.name),'SHA256SUMS'].sort()),'complete physical inventory');
  let bytes=b.length;for(const e of rows){const v=get(prefix+e.name);ok(sha(v)===e.sha256,'every sealed file');bytes+=v.length;}
  ok(bytes===size,'whole physical packet bytes');sealed.push({path:prefix,payloads:count,files:count+1,bytes,sha256sums:digest});
}
ok(sha(get(A+'HANDOFF.md'))==='fbe2ac5da02cb4b7dc961aa14074388c67c38c5a90e1cc3d4ec1ecb840b5fda4','independent exact handoff');
ok(sha(get(A+'ACCEPTANCE.json'))==='6a2846a47b89eb468ac2d03188850ff1802b9577acc11793e14197d79edeac89','independent exact acceptance');
const oldCheck=js(A+'CHECK_NATIVE.json'),newReplays=js(R+'ROOT_REPLAYS_NATIVE.json');
ok(newReplays.records.length===2,'two actual root documentary replays');
for(const [i,r]of newReplays.records.entries()){
  const old=i?priorNative:oldCheck;ok(r.result.exit_code===0&&r.result.chunk_id&& !r.result.session_id,'actual completed root replay');
  const expected='node '+A+(i?'CLOSE.cjs':'CHECK.cjs');ok(r.request.cmd===expected,'exact source read-only replay cmd');
  raw(r.result.output,old.result.output,'whole root replay stdout '+expected);
}
const checkData=JSON.parse(oldCheck.result.output);
ok(checkData.checks===55218&&checkData.fullKeys.length===66&&checkData.rawPairCount===49&&checkData.rawPairedBytes===1011615,'source/derivative original census');
ok(checkData.originalNativeCount===46&&JSON.stringify(checkData.originalNativeExits)===JSON.stringify({zero:39,difference:6,missingDocument:1}),'original failed native census retained');
ok(checkData.bindingChanges.length===12&&checkData.collectorSuffixBytes===32620,'exact structural transformation census');
const findings=js(A+'FINDINGS.json'),accept=js(A+'ACCEPTANCE.json');
ok(findings.verdict==='ACCEPT_EXACT_PROSPECTIVE_SOURCE_LITERAL_CAPTURE_REQUEST'&&Object.values(findings.current_census).every(x=>x===0),'independent exact zero-current source census');
ok(findings.operation_or_probe_authorized===false&&accept.operation_or_allocation_grant===false,'source acceptance not runtime grant');
for(const e of accept.reviewed_prospective_artifacts){const b=get(P+e.existing_documentary_carrier);ok(sha(b)===e.sha256&&b.length===e.bytes,'exact externally accepted future bytes');ok(e.actual_destination_metadata_presence_and_hash===null,'no future key');}
for(const [n,h]of Object.entries(accept.exact_contracts))ok(sha(get(P+n))===h,'every exact accepted contract');
const readPacket=js(R+'ROOT_READS_NATIVE.json');ok(readPacket.absence.result.exit_code===0,'own new-only packet absence');
const sourceParts=readPacket.records.filter(x=>x.role.startsWith('prospective_source_part_'));
ok(sourceParts.length===6,'six complete root source ranges');
const rootReadCensus=[];
for(const r of readPacket.records){
  ok(r.request&&r.result&&r.result.exit_code===0&&typeof r.result.chunk_id==='string'&&!r.result.session_id,'actual root data-read envelope');
  const m=/^sed -n '(\d+),(\d+)p' (.+)$/.exec(r.request.cmd);
  if(m){
    const b=get(m[3]),lines=b.toString('utf8').split(/(?<=\n)/);
    raw(r.result.output,lines.slice(Number(m[1])-1,Number(m[2])).join(''),'root exact document slice '+r.role);
  }
  rootReadCensus.push({role:r.role,request:r.request,chunk_id:r.result.chunk_id,exit:r.result.exit_code,bytes:Buffer.byteLength(r.result.output),sha256:sha(r.result.output)});
}
raw(sourceParts.map(x=>x.result.output).join(''),get(P+'observe.proposed.py.txt'),'complete root 2845-line source concatenation');
const checkerParts=readPacket.records.filter(x=>x.role==='checkera'||x.role==='checkerb');
raw(checkerParts.map(x=>x.result.output).join(''),get(A+'CHECK.cjs'),'whole independent checker source before root replay');
const diff=js(P+'SOURCE_DIFF_NATIVE.json').diffs;const shown=readPacket.records.find(x=>x.role==='other_diffs');
raw(shown.result.output,diff.filter(x=>x.role!=='source_observer').map(x=>x.result.output).join(''),'complete five nonaddition diff raw display');
const whole=checkData.diffs;ok(whole.length===6&&whole.reduce((s,x)=>s+x.hunks,0)===13,'all six full diff reconstruction obligations preserved');
const src=get(P+'observe.proposed.py.txt').toString('utf8'),prev=get(QA+'p213_minimal_observer_source_delta01/observe.py').toString('utf8');
raw(src.slice(src.indexOf('if BINDING is None:\n')),prev.slice(prev.indexOf('if BINDING is None:\n')),'whole prior accepted collector reused unchanged');
const scope=js(P+'CONSUMPTION_MAP.json'),binding=js(P+'BINDING.prepared.json'),projection=js(P+'BINDING.runtime_literal.json');
for(const n of scope.consumed_top_level_fields)ok(JSON.stringify(binding[n])===JSON.stringify(projection[n]),'every whole projected field '+n);
ok(scope.consumed_top_level_fields.length===13&&binding.enabled===false&&binding.operation_authorized===false,'literal and authority remain distinct');
ok(js(P+'CAPTURE_REQUEST.disabled.json').request.cmd===null&&js(P+'PROPOSED_REQUEST.json').operation_authorized===false,'current command disabled');
for(const p of [...keys.keys()])acquire(p);
console.log(JSON.stringify({scope:'ROOT_EXACT_PROSPECTIVE_SOURCE_LITERAL_CAPTURE_REQUEST_RECEPTION_NOT_OPERATION',checks,keys:[...keys.values()],keyCount:keys.size,sealedPackets:sealed,independentOriginalKeysPreserved:75,rootReplayCount:2,sourceReconstructedDiffs:whole,rootReadCensus,rawPairs:pairs,rawPairCount:pairs.length,rawPairedBytes:pairs.reduce((s,x)=>s+x.bytes,0),currentSourceCensus:findings.current_census,futurePathsUsedAsOperands:false,observerOrPythonExecuted:false,operationGranted:false,scientificOrManuscriptAcceptance:false}));
