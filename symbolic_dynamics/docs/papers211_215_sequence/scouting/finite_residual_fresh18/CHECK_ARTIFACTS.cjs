'use strict';
// Documentary only. No scientific imports, network, child process, or writes.

const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics';
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
let checks=0;function ensure(x,m){checks++;if(!x)throw Error(m);}
function key(p){const full=path.resolve(root,p),before=fs.lstatSync(full,{bigint:true});ensure(before.isFile()&&!before.isSymbolicLink(),'regular input '+p);const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);try{const a=fs.fstatSync(fd,{bigint:true});const data=fs.readFileSync(fd);const b=fs.fstatSync(fd,{bigint:true}),after=fs.lstatSync(full,{bigint:true});ensure(BigInt(data.length)===a.size,'EOF '+p);ensure(JSON.stringify(meta(before))===JSON.stringify(meta(a))&&JSON.stringify(meta(a))===JSON.stringify(meta(b))&&JSON.stringify(meta(b))===JSON.stringify(meta(after)),'stable metadata '+p);return {path:p,resolved_path:full,sha256:crypto.createHash('sha256').update(data).digest('hex'),metadata:meta(a)};}finally{fs.closeSync(fd);}}


const base='docs/papers211_215_sequence/scouting/finite_residual_fresh18';
const own=["PLAN.md","PROOF_AND_DISPOSITION.md","SOURCE_READS.md","SCOPE.json","HANDOFF.md","SOURCE_NATIVE.json","WEB_NATIVE.json","INPUT_PINS.json","CHECK_ARTIFACTS.cjs"];
const selected=[{"archive_index":0,"path":".agents/skills/symbolic-dynamics-research/SKILL.md","from":1,"to":3000,"role":"required skill/workflow"},{"archive_index":1,"path":"docs/research_state/WORKFLOW.md","from":1,"to":3000,"role":"required skill/workflow"},{"archive_index":2,"path":"/root/autodl-tmp/.codex/skills/idea-creator/SKILL.md","from":1,"to":3000,"role":"required skill/workflow"},{"archive_index":3,"path":"/root/autodl-tmp/.codex/skills/research-lit/SKILL.md","from":1,"to":3000,"role":"required skill/workflow"},{"archive_index":6,"path":"docs/papers211_215_sequence/PROBLEM_ANCHOR.md","from":1,"to":3000,"role":"current anchor"},{"archive_index":7,"path":"docs/papers197_201_sequence/PROBLEM_ANCHOR.md","from":1,"to":3000,"role":"prior admission criteria"},{"archive_index":9,"path":"docs/papers204_208_sequence/ARTIFACT_CONTRACT.md","from":1,"to":3000,"role":"inherited artifact contract"},{"archive_index":13,"path":"docs/papers211_215_sequence/scouting/finite_ordered_interaction_fresh_desk/REPORT.md","from":1,"to":3000,"role":"ordered interaction source boundary"},{"archive_index":17,"path":"docs/papers142_146_sequence/scouting/algebraic/SCOUT.md","from":1,"to":130,"role":"old numerical semigroup map"},{"archive_index":18,"path":"docs/papers122_126_sequence/scouting/root/SCOUT.md","from":20,"to":44,"role":"old numerical blowup entry"},{"archive_index":19,"path":"docs/papers122_126_sequence/scouting/replacement/SCOUT.md","from":20,"to":43,"role":"exact old Moore definition"},{"archive_index":20,"path":"docs/papers204_208_sequence/scouting/finite_systems_eighteenth/PROOF_AND_ADAPTERS.md","from":1,"to":128,"role":"old Moore and Brzozowski proof"},{"archive_index":21,"path":"docs/papers211_215_sequence/scouting/word_automata_residual04/SOURCE_SUBTRACTION.md","from":1,"to":105,"role":"current automata subtraction"},{"archive_index":22,"path":"docs/papers211_215_sequence/scouting/fresh_residual_algebra_order01/SOURCES_AND_SUBTRACTION.md","from":1,"to":160,"role":"nearby self-distributive subtraction"},{"archive_index":23,"path":"/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md","from":1,"to":3000,"role":"proof-writer skill"}];
function readOwn(name){ensure(own.includes(name),'fixed own file');const p=base+'/'+name,k=key(p),data=fs.readFileSync(path.resolve(root,p));ensure(crypto.createHash('sha256').update(data).digest('hex')===k.sha256,'read same bytes '+name);return {k,data};}
const cache=Object.fromEntries(own.map(n=>[n,readOwn(n)]));
function json(name){return JSON.parse(cache[name].data.toString('utf8'));}
const source=json('SOURCE_NATIVE.json'),web=json('WEB_NATIVE.json'),pins=json('INPUT_PINS.json'),scope=json('SCOPE.json');
ensure(source.initial_calls.length===24,'24 original source calls');
ensure(web.calls.length===8,'8 original web calls');
const failures=source.initial_calls.map((x,i)=>x.native.exit_code===0?null:{index:i,exit_code:x.native.exit_code}).filter(Boolean);
ensure(JSON.stringify(failures)===JSON.stringify([{index:8,exit_code:2},{index:15,exit_code:1},{index:16,exit_code:1}]),'original failures preserved');
ensure(source.late_lookup.native.exit_code===2&&source.late_lookup.native.chunk_id==='5e6a9f','late lookup failure preserved');
ensure(source.initial_calls.every(x=>typeof x.native.output==='string'&&typeof x.request.cmd==='string'),'actual native records present');
ensure(source.initial_calls.every(x=>!/^Warning: truncated output/m.test(x.native.output)),'no source-native intrinsic truncation');
ensure(web.calls.every(x=>typeof x.result==='string'&&x.result.length>0),'full returned web strings');
ensure(web.calls.reduce((n,x)=>n+(x.request.search_query||[]).length,0)===6,'six source queries');
ensure(pins.inputs.length===15&&pins.baseline.native.exit_code===0,'15 input keys and actual baseline');
ensure(JSON.stringify(JSON.parse(pins.baseline.native.output).inputs)===JSON.stringify(pins.inputs),'baseline stdout key equality');
ensure(pins.scope==='POST_READ_BASELINE_NOT_RETROACTIVE_BRACKET','baseline timing limitation');
ensure(scope.substantive_directions===3&&scope.root_reception==='PENDING','author status');
for(const field of ['new_literals','closed_attempt_delta_recommended','controls','pilots','scientific_executions','nominations','reserves','paper_ids','independent_reviews','central_state_writes'])ensure(scope[field]===0,'zero '+field);
ensure(scope.external_status==='HOLD_EXTERNAL','external hold');
let pairs=0,pairBytes=0;const inputKeys=[];
for(const item of selected){
 const pinned=pins.inputs.find(x=>x.path===item.path);
 ensure(!!pinned,'fixed input present');
 for(const f of ['archive_index','from','to','role'])ensure(pinned[f]===item[f],'fixed slice '+item.path);
 const current=key(item.path);
 ensure(current.resolved_path===pinned.resolved_path&&current.sha256===pinned.sha256&&JSON.stringify(current.metadata)===JSON.stringify(pinned.metadata),'input full key unchanged '+item.path);
 const data=fs.readFileSync(current.resolved_path);
 ensure(crypto.createHash('sha256').update(data).digest('hex')===current.sha256,'slice input hash');
 const lines=data.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];
 const actual=Buffer.from(lines.slice(item.from-1,item.to).join(''),'utf8');
 const archived=source.initial_calls[item.archive_index];
 ensure(archived.request.cmd==="sed -n '"+item.from+","+item.to+"p' "+item.path,'exact original command');
 ensure(archived.native.exit_code===0,'selected original exit');
 ensure(actual.equals(Buffer.from(archived.native.output,'utf8')),'raw selected stdout bytes '+item.path);
 pairs++;pairBytes+=actual.length;inputKeys.push(current);
}
for(const name of ['PROOF_AND_DISPOSITION.md','HANDOFF.md']){
 const s=cache[name].data.toString('utf8');
 ensure(s.includes('ZERO_NEW_LITERAL')&&s.includes('HOLD_EXTERNAL'),'explicit scope '+name);
}
ensure(cache['PROOF_AND_DISPOSITION.md'].data.toString('utf8').includes('g=3'),'source caveat retained');
const ownKeys=own.map(name=>cache[name].k);
console.log(JSON.stringify({status:'DOCUMENTARY_ONLY_PASS_NOT_SCIENTIFIC_ACCEPTANCE',checks,source_native_calls:24,late_failed_lookups:1,web_calls:8,queries:6,original_native_failures:failures,selected_raw_pairs:pairs,selected_raw_bytes:pairBytes,post_read_input_keys:inputKeys,own_payload_keys:ownKeys},null,2));

