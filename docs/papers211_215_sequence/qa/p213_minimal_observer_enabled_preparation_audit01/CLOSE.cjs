'use strict';
// Independent final document closing only; future operational paths remain data.
const fs=require('node:fs'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const A='docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation_audit01/';
const P='docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/';
const OWN=['ACCEPTANCE.json','ARTIFACT_SHAPES_NATIVE.json','AUTHOR_REPLAYS_NATIVE.json','BASELINE_NATIVE.json','CHECK.cjs','CHECKER_READS_NATIVE.json','CHECK_NATIVE.json','CLOSE.cjs','CONTRACT_READS_NATIVE.json','DIFF_READS_NATIVE.json','EVIDENCE.md','FINAL_READS_NATIVE.json','FINDINGS.json','HANDOFF.md','KEY_DOCUMENTS.cjs','ORIENTATION_NATIVE.json','PLAN.md','POLICY_READS_NATIVE.json','PREDECESSOR_READS_NATIVE.json','PROGRAM_READS_NATIVE.json','READ_SCOPE.md','REPORT.md'].sort();
let checks=0;function ok(v,m){checks++;if(!v)throw new Error(m);}
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const rawCheck=JSON.parse(fs.readFileSync(ROOT+A+'CHECK_NATIVE.json','utf8'));ok(rawCheck.result.exit_code===0,'actual independent data check exit');
const old=JSON.parse(rawCheck.result.output);ok(old.checks===55218&&old.fullKeys.length===66,'original check counts');
const allowed=new Set([...old.fullKeys.map(x=>x.path),...OWN.map(n=>A+n)]);
const ff=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs'];
const meta=s=>Object.fromEntries(ff.map(k=>[k,s[k].toString()]));
const keys=new Map(),bufs=new Map();
function read(p){
  ok(allowed.has(p),'finite documentary operand');ok(!p.includes('/p213_minimal_observer_enabled01/')&&!p.includes('/p213_minimal_observer_probe01/'),'no future path operand');
  const a=fs.lstatSync(ROOT+p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'regular no leaf link');const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);let b,k;
  try{const f=fs.fstatSync(fd,{bigint:true});b=fs.readFileSync(fd);const g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(ROOT+p,{bigint:true});for(const s of [f,g,z])ok(JSON.stringify(meta(a))===JSON.stringify(meta(s)),'whole same-fd/end-path key');ok(BigInt(b.length)===a.size,'whole EOF byte count');k={path:p,type:'regular',...meta(a),bytes:b.length,sha256:sha(b)};}finally{fs.closeSync(fd);}
  if(keys.has(p))ok(JSON.stringify(keys.get(p))===JSON.stringify(k),'whole repeated key');else keys.set(p,k);bufs.set(p,b);return b;
}
const json=n=>JSON.parse(read(A+n).toString('utf8'));
ok(JSON.stringify(fs.readdirSync(ROOT+A).filter(n=>n!=='CLOSING_NATIVE.json'&&n!=='SHA256SUMS').sort())===JSON.stringify(OWN),'complete audit preclosing inventory');
for(const k of old.fullKeys){read(k.path);ok(JSON.stringify(keys.get(k.path))===JSON.stringify(k),'every original independent whole key unchanged');}
for(const n of OWN)read(A+n);
let jsonCount=0;for(const n of OWN.filter(x=>x.endsWith('.json'))){JSON.parse(bufs.get(A+n).toString('utf8'));jsonCount++;}
const f=json('FINDINGS.json'),accept=json('ACCEPTANCE.json');
ok(f.verdict==='ACCEPT_EXACT_PROSPECTIVE_SOURCE_LITERAL_CAPTURE_REQUEST'&&Object.values(f.current_census).every(x=>x===0),'exact zero-current-finding verdict');
ok(f.operation_or_probe_authorized===false&&f.physical_enabled_materialization_observed===false&&f.future_path_presence_absence_metadata_observed===false&&f.observer_capture_python_executed_parsed_imported_or_compiled===false&&f.runtime_observed_or_accepted===false,'source review not operational claim');
ok(accept.verdict===f.verdict&&accept.root_reception_pending===true&&accept.operation_or_allocation_grant===false&&accept.future_destination_used_as_filesystem_operand===false,'exact prospective acceptance boundary');
for(const x of accept.reviewed_prospective_artifacts){const p=P+x.existing_documentary_carrier;const b=read(p);ok(b.length===x.bytes&&sha(b)===x.sha256,'both exact external prospective commitments');ok(x.actual_destination_metadata_presence_and_hash===null,'no prospective metadata fabrication');}
for(const [name,digest] of Object.entries(accept.exact_contracts))ok(sha(read(P+name))===digest,'every accepted exact contract hash');
ok(sha(read(P+'SHA256SUMS'))===accept.author_sha256sums,'author whole seal unchanged');
const s=read(P+'SHA256SUMS').toString('utf8');const manifest=s.trimEnd().split('\n').map(line=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);ok(!!m,'strict current manifest line');return {sha256:m[1],name:m[2]};});
ok(manifest.length===32,'all current 32 author payloads');
ok(JSON.stringify(fs.readdirSync(ROOT+P).sort())===JSON.stringify([...manifest.map(x=>x.name),'SHA256SUMS'].sort()),'complete current physical author inventory');
for(const r of manifest)ok(sha(read(P+r.name))===r.sha256,'every author payload unchanged');
const readbacks=json('FINAL_READS_NATIVE.json').records;ok(readbacks.length===6,'six complete own-document readbacks');const pairs=[];
for(const r of readbacks){ok(r.result.exit_code===0&&!r.result.output.startsWith('Warning: truncated output'),'complete actual final read');const m=/^sed -n '\d+,\d+p' (.+)$/.exec(r.request.cmd);ok(!!m&&OWN.includes(m[1].slice(A.length))&&m[1].startsWith(A),'exact final documentary read target');const b=read(m[1]);ok(b.equals(Buffer.from(r.result.output)),'whole final native raw readback');pairs.push({path:m[1],bytes:b.length,sha256:sha(b)});}
let links=0;for(const n of OWN.filter(x=>x.endsWith('.md'))){const s=read(A+n).toString('utf8');for(const m of s.matchAll(/\]\(([^)]+)\)/g)){ok(!m[1].includes('://')&&!m[1].startsWith('/')&&!m[1].includes('..'),'audit local link scope');ok(OWN.includes(m[1]),'all local documentary links exist');links++;}}
const ownKeys=OWN.map(n=>keys.get(A+n));const closingKeys=[...keys.values()];for(const k of closingKeys)read(k.path);
console.log(JSON.stringify({scope:'INDEPENDENT_FINAL_DOCUMENTARY_CLOSING_PASS_NOT_OPERATION',checks,fullKeyCount:keys.size,keys:[...keys.values()],originalWholeKeysCompared:66,baselineKeysPreserved:53,authorPayloads:32,auditPayloadsBeforeClosingReceipt:OWN.length,auditPayloadBytesBeforeClosingReceipt:ownKeys.reduce((s,k)=>s+k.bytes,0),jsonFilesParsed:jsonCount,localMarkdownLinks:links,rawFinalReadbacks:pairs,rawFinalReadbackBytes:pairs.reduce((s,x)=>s+x.bytes,0),currentCensus:f.current_census,reviewedProspectiveArtifacts:accept.reviewed_prospective_artifacts,nonselfRule:'CLOSING_NATIVE.json is written after this read-only command, then SHA256SUMS includes every other physical file; only the seal itself is excluded.'}));
