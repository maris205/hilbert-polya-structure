'use strict';
// Documentary only: fixed data inputs, filesystem keys, byte comparisons.
// No scientific implementation/import, network, process launch, or file write.
const fs=require('fs'), path=require('path'), crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics';
const fresh='docs/papers211_215_sequence/scouting/finite_residual_fresh18';
const add='docs/papers211_215_sequence/scouting/finite_residual_fresh18_addendum01';
const own='docs/papers211_215_sequence/scouting/root_reception/fresh18_independent_intake01';
const freshNames=['CHECK_ARTIFACTS.cjs','CHECK_NATIVE.json','FINAL_READ_NATIVE.json','HANDOFF.md','INPUT_PINS.json','MANIFEST.json','PLAN.md','PROOF_AND_DISPOSITION.md','SCOPE.json','SOURCE_NATIVE.json','SOURCE_READS.md','WEB_NATIVE.json'];
const addNames=['CLOSURE_FAILURE_NATIVE.json','HANDOFF.md','SEAL_PREPARATION_NATIVE.json','SHA256SUMS'];
const ownNames=['AUTHOR_REPLAY_NATIVE.json','CHECK_INTAKE.cjs','FINDINGS.json','PROOF_AUDIT.md','READS_NATIVE.json','SOURCE_SCOPE.md'];
const selected=[{"archive_index":0,"path":".agents/skills/symbolic-dynamics-research/SKILL.md","from":1,"to":3000,"role":"required skill/workflow"},{"archive_index":1,"path":"docs/research_state/WORKFLOW.md","from":1,"to":3000,"role":"required skill/workflow"},{"archive_index":2,"path":"/root/autodl-tmp/.codex/skills/idea-creator/SKILL.md","from":1,"to":3000,"role":"required skill/workflow"},{"archive_index":3,"path":"/root/autodl-tmp/.codex/skills/research-lit/SKILL.md","from":1,"to":3000,"role":"required skill/workflow"},{"archive_index":6,"path":"docs/papers211_215_sequence/PROBLEM_ANCHOR.md","from":1,"to":3000,"role":"current anchor"},{"archive_index":7,"path":"docs/papers197_201_sequence/PROBLEM_ANCHOR.md","from":1,"to":3000,"role":"prior admission criteria"},{"archive_index":9,"path":"docs/papers204_208_sequence/ARTIFACT_CONTRACT.md","from":1,"to":3000,"role":"inherited artifact contract"},{"archive_index":13,"path":"docs/papers211_215_sequence/scouting/finite_ordered_interaction_fresh_desk/REPORT.md","from":1,"to":3000,"role":"ordered interaction source boundary"},{"archive_index":17,"path":"docs/papers142_146_sequence/scouting/algebraic/SCOUT.md","from":1,"to":130,"role":"old numerical semigroup map"},{"archive_index":18,"path":"docs/papers122_126_sequence/scouting/root/SCOUT.md","from":20,"to":44,"role":"old numerical blowup entry"},{"archive_index":19,"path":"docs/papers122_126_sequence/scouting/replacement/SCOUT.md","from":20,"to":43,"role":"exact old Moore definition"},{"archive_index":20,"path":"docs/papers204_208_sequence/scouting/finite_systems_eighteenth/PROOF_AND_ADAPTERS.md","from":1,"to":128,"role":"old Moore and Brzozowski proof"},{"archive_index":21,"path":"docs/papers211_215_sequence/scouting/word_automata_residual04/SOURCE_SUBTRACTION.md","from":1,"to":105,"role":"current automata subtraction"},{"archive_index":22,"path":"docs/papers211_215_sequence/scouting/fresh_residual_algebra_order01/SOURCES_AND_SUBTRACTION.md","from":1,"to":160,"role":"nearby self-distributive subtraction"},{"archive_index":23,"path":"/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md","from":1,"to":3000,"role":"proof-writer skill"}];
const allowed=new Set([...freshNames.map(n=>fresh+'/'+n),...addNames.map(n=>add+'/'+n),...ownNames.map(n=>own+'/'+n),...selected.map(e=>e.path)]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;
function ensure(x,m){checks++;if(!x)throw Error(m);}
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const cache=new Map();
function read(p){
 ensure(allowed.has(p),'fixed allowlist '+p);
 if(cache.has(p))return cache.get(p);
 const full=path.resolve(root,p),before=fs.lstatSync(full,{bigint:true});
 ensure(before.isFile()&&!before.isSymbolicLink(),'regular leaf '+p);
 const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  const a=fs.fstatSync(fd,{bigint:true}),data=fs.readFileSync(fd),b=fs.fstatSync(fd,{bigint:true}),after=fs.lstatSync(full,{bigint:true});
  ensure(BigInt(data.length)===a.size,'full EOF '+p);
  ensure(same(meta(before),meta(a))&&same(meta(a),meta(b))&&same(meta(b),meta(after)),'stable ten fields '+p);
  const key={path:p,resolved_path:full,sha256:sha(data),metadata:meta(a)};
  const item={data,key};cache.set(p,item);return item;
 }finally{fs.closeSync(fd);}
}
const json=p=>JSON.parse(read(p).data.toString('utf8'));
function utf8(b,p){ensure(Buffer.from(b.toString('utf8'),'utf8').equals(b),'UTF8 round trip '+p);}
function sliceLines(b,from,to){
 const parts=[];let start=0,line=1;
 while(start<b.length){
  const lf=b.indexOf(10,start),end=lf<0?b.length:lf+1;
  if(line>=from&&line<=to)parts.push(b.subarray(start,end));
  if(line>=to)break;
  start=end;line++;
 }
 return Buffer.concat(parts);
}
const manifest=json(fresh+'/MANIFEST.json');
ensure(read(fresh+'/MANIFEST.json').key.sha256==='ad679d4d641f466b98070caff403b0e735eeaca2e085076a96c727cd77df3088','frozen original seal');
ensure(same(fs.readdirSync(path.resolve(root,fresh)).sort(),freshNames),'exact original 12-file census');
ensure(manifest.excluded_self==='MANIFEST.json'&&manifest.payload_count===11&&manifest.payload_bytes===479832,'nonself original manifest scope');
ensure(same(manifest.entries.map(e=>e.path).sort(),freshNames.filter(n=>n!=='MANIFEST.json')),'complete original payload census');
let payloadBytes=0;
for(const e of manifest.entries){
 const r=read(fresh+'/'+e.path);
 ensure(r.key.resolved_path===e.resolved_path&&r.key.sha256===e.sha256&&same(r.key.metadata,e.metadata),'whole frozen input '+e.path);
 payloadBytes+=r.data.length;
}
ensure(payloadBytes===479832&&read(fresh+'/MANIFEST.json').data.length===6666,'original byte census');

ensure(same(fs.readdirSync(path.resolve(root,add)).sort(),addNames),'exact addendum four-file census');
const seal=read(add+'/SHA256SUMS');
ensure(seal.key.sha256==='64a3ffa4c286f9938ecaac83798015f1a2fd01fff5715f51404871607dcefad8','pinned addendum nonself seal');
const raw=seal.data.toString('utf8');utf8(seal.data,'addendum seal');
ensure(raw.endsWith('\n'),'addendum terminal LF');
const rows=raw.slice(0,-1).split('\n').map(row=>{
 const m=/^([a-f0-9]{64})  ([A-Z_]+[.](?:md|json))$/.exec(row);
 ensure(!!m,'strict addendum row');return {sha256:m[1],path:m[2]};
});
ensure(same(rows.map(e=>e.path).sort(),addNames.filter(n=>n!=='SHA256SUMS')),'complete addendum nonself rows');
let addBytes=0;
for(const e of rows){const r=read(add+'/'+e.path);ensure(r.key.sha256===e.sha256,'addendum payload '+e.path);addBytes+=r.data.length;}

const pins=json(fresh+'/INPUT_PINS.json'),source=json(fresh+'/SOURCE_NATIVE.json'),web=json(fresh+'/WEB_NATIVE.json');
ensure(pins.scope==='POST_READ_BASELINE_NOT_RETROACTIVE_BRACKET','honest baseline timing');
ensure(pins.inputs.length===15&&pins.baseline.native.exit_code===0,'fifteen baseline keys');
ensure(same(JSON.parse(pins.baseline.native.output).inputs,pins.inputs),'actual baseline stdout');
ensure(source.initial_calls.length===24&&web.calls.length===8,'native call census');
ensure(web.calls.reduce((n,c)=>n+(c.request.search_query||[]).length,0)===6,'six search queries');
ensure(source.initial_calls.every(c=>typeof c.native.output==='string'&&!/^Warning: truncated output/m.test(c.native.output)),'native source outputs retained');
ensure(web.calls.every(c=>typeof c.result==='string'&&c.result.length>0),'full archived provider strings');
const failures=source.initial_calls.flatMap((r,i)=>r.native.exit_code===0?[]:[{index:i,exit_code:r.native.exit_code}]);
ensure(same(failures,[{index:8,exit_code:2},{index:15,exit_code:1},{index:16,exit_code:1}]),'three initial failures retained');
ensure(source.late_lookup.native.chunk_id==='5e6a9f'&&source.late_lookup.native.exit_code===2,'late failure retained');
let slicePairs=0,sliceBytes=0;
for(const item of selected){
 const p=pins.inputs.find(e=>e.path===item.path);
 ensure(!!p,'selected pin exists');
 ensure(['archive_index','from','to','role'].every(f=>p[f]===item[f]),'exact fixed selected premise');
 const r=read(item.path);
 ensure(r.key.resolved_path===p.resolved_path&&r.key.sha256===p.sha256&&same(r.key.metadata,p.metadata),'current external complete key');
 utf8(r.data,item.path);
 const c=source.initial_calls[item.archive_index];
 ensure(c.request.cmd==="sed -n '"+item.from+","+item.to+"p' "+item.path&&c.native.exit_code===0,'exact original selected request/exit');
 const actual=sliceLines(r.data,item.from,item.to),expected=Buffer.from(c.native.output,'utf8');
 ensure(actual.equals(expected),'true byte-slice/original-stdout equality');
 slicePairs++;sliceBytes+=actual.length;
}
ensure(slicePairs===15&&sliceBytes===94397,'selected raw pair census');

const archived=json(fresh+'/CHECK_NATIVE.json'),actual=json(own+'/AUTHOR_REPLAY_NATIVE.json');
ensure(archived.native.chunk_id==='21bea2'&&archived.native.exit_code===0,'actual original checker receipt');
ensure(actual.result.chunk_id==='f4c1b9'&&actual.result.exit_code===0,'actual independent documentary replay');
ensure(archived.request.cmd===actual.request.cmd&&actual.request.cmd==='node '+fresh+'/CHECK_ARTIFACTS.cjs','same inspected documentary command');
ensure(Buffer.from(archived.native.output,'utf8').equals(Buffer.from(actual.result.output,'utf8')),'entire replay stdout bytes equal');
const checked=JSON.parse(archived.native.output);
ensure(checked.checks===266&&checked.selected_raw_pairs===15&&checked.selected_raw_bytes===94397,'actual archived 266-result census');
ensure(checked.post_read_input_keys.length===15&&checked.own_payload_keys.length===9,'actual 24-key census');
for(const p of [...checked.post_read_input_keys,...checked.own_payload_keys])ensure(same(read(p.path).key,p),'archived full key remains unchanged');

const finalReads=json(fresh+'/FINAL_READ_NATIVE.json').calls;
ensure(finalReads.length===6,'six archived final reads');
let finalPairs=0,finalBytes=0;
for(const c of finalReads){
 const m=/^sed -n '1,3000p' (.+)$/.exec(c.request.cmd);
 ensure(!!m&&m[1].startsWith(fresh+'/')&&c.native.exit_code===0,'actual owned full read');
 const r=read(m[1]);utf8(r.data,m[1]);
 ensure(r.data.equals(Buffer.from(c.native.output,'utf8')),'original final full-read byte equality');
 finalPairs++;finalBytes+=r.data.length;
}
ensure(finalPairs===6&&finalBytes===29417,'actual final-read byte census');

const prep=json(add+'/SEAL_PREPARATION_NATIVE.json'),prepResult=JSON.parse(prep.native.output);
ensure(prep.native.chunk_id==='e04509'&&prep.native.exit_code===0,'original 150 receipt exported');
ensure(prep.request.cmd.startsWith("node <<'NODE'\n")&&prep.request.cmd.includes('exact payload census before seal'),'original pre-manifest command is data only');
ensure(prepResult.scope==='NONSELF_AUTHOR_DESK_SEAL_PREPARATION'&&prepResult.checks===150&&prepResult.final_read_pairs===6&&prepResult.final_read_bytes===29417&&prepResult.prior_unchanged_keys===24,'actual 150 receipt census');
ensure(same(prepResult.manifest,manifest),'original generated manifest content agrees exactly');
const fail=json(add+'/CLOSURE_FAILURE_NATIVE.json');
ensure(fail.native.chunk_id==='3e76f4'&&fail.native.exit_code===1&&fail.native.output.includes('Error: strict manifest row'),'addendum original failed closure retained');

const scope=json(fresh+'/SCOPE.json'),findings=json(own+'/FINDINGS.json');
ensure(scope.substantive_directions===3&&scope.root_reception==='PENDING','original author scope unchanged');
for(const f of ['new_literals','closed_attempt_delta_recommended','controls','pilots','scientific_executions','nominations','reserves','paper_ids','independent_reviews','central_state_writes'])ensure(scope[f]===0,'zero original '+f);
ensure(scope.external_status==='HOLD_EXTERNAL','external hold');
ensure(findings.verdict==='ACCEPT_NEGATIVE_INTAKE_WITH_EXPLICIT_CLAIM_EXCLUSION'&&findings.census.frozen_author_wording_exclusions===1,'explicit singleton exclusion retained');

const reads=json(own+'/READS_NATIVE.json').reads;
ensure(reads.some(r=>r.role==='seal_addendum_manifest'&&r.result.exit_code===2),'receiver wrong-basename failure retained');
let receiverPairs=0,receiverBytes=0;
for(const c of reads){
 const m=/^sed -n '([0-9]+),([0-9]+)p' (.+)$/.exec(c.request.cmd);
 if(!m||c.result.exit_code!==0||!allowed.has(m[3]))continue;
 const r=read(m[3]);utf8(r.data,m[3]);
 const bytes=sliceLines(r.data,Number(m[1]),Number(m[2]));
 ensure(bytes.equals(Buffer.from(c.result.output,'utf8')),'receiver current read agrees with fixed current bytes '+c.role);
 receiverPairs++;receiverBytes+=bytes.length;
}
for(const n of ownNames)read(own+'/'+n);
const inputKeys=[...freshNames.map(n=>read(fresh+'/'+n).key),...addNames.map(n=>read(add+'/'+n).key),...selected.map(e=>read(e.path).key)];
const ownKeys=ownNames.map(n=>read(own+'/'+n).key);
console.log(JSON.stringify({
 status:'INDEPENDENT_DOCUMENTARY_PASS_NOT_SCIENTIFIC_EXECUTION_OR_MANUSCRIPT_REVIEW',
 checks,original_payloads:11,original_files:12,original_payload_bytes:payloadBytes,
 original_packet_bytes:payloadBytes+6666,addendum_payloads:3,addendum_files:4,
 addendum_payload_bytes:addBytes,addendum_packet_bytes:addBytes+seal.data.length,
 external_keys:15,source_raw_pairs:slicePairs,source_raw_bytes:sliceBytes,
 final_full_read_pairs:finalPairs,final_full_read_bytes:finalBytes,
 receiver_fixed_read_pairs:receiverPairs,receiver_fixed_read_bytes:receiverBytes,
 author_documentary_checks:266,author_seal_preparation_checks:150,
 replay_stdout_byte_equal:true,historical_preseal_command_reexecuted:false,
 input_keys:inputKeys,own_preclosure_keys:ownKeys
},null,2));
