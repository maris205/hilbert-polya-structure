'use strict';
// Bounded read-only physical-freeze DATA reception, not manuscript review.
const fs=require('node:fs'),crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics/';
const P=W+'papers/213-receiver-limited-cyclic-transfer/',Q=W+'docs/papers211_215_sequence/';
const read=p=>fs.readFileSync(p),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;function ok(v,m){checks++;if(!v)throw Error(m);}
function manifest(dir,name){const raw=read(dir+name),rows=raw.toString('ascii').trimEnd().split('\n').map(l=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.\/-]+)$/.exec(l);ok(m&&!m[2].startsWith('/')&&!m[2].split('/').includes('..'),'manifest syntax');ok(sha(read(dir+m[2]))===m[1],'payload hash');return {name:m[2],sha256:m[1]};});ok(new Set(rows.map(x=>x.name)).size===rows.length,'unique entries');return{sha256:sha(raw),rows};}
const r1=manifest(P+'frozen_round1/','SHA256SUMS'),r2=manifest(P+'frozen_round2/','SHA256SUMS');
ok(r1.rows.length===25&&r2.rows.length===25,'both25payloads');
const files=[];function walk(dir,prefix=''){for(const e of fs.readdirSync(dir,{withFileTypes:true})){ok(!e.isSymbolicLink(),'no symlink');if(e.isDirectory())walk(dir+e.name+'/',prefix+e.name+'/');else{ok(e.isFile(),'regular');files.push(prefix+e.name);}}}
walk(P+'frozen_round2/');ok(JSON.stringify(files.sort())===JSON.stringify([...r2.rows.map(x=>x.name),'SHA256SUMS'].sort()),'complete physical inventory');
const copy=JSON.parse(read(Q+'qa/p213_round2_terminal_root01/ROUND2_COPY_NATIVE.json'));
ok(copy.chunk_id==='e56a10'&&copy.exit_code===0,'actual materialization');const data=JSON.parse(copy.output);ok(data.pairs.length===24&&data.source_unchanged===true,'copy receipt');
const pairs=[];for(const row of r2.rows){if(row.name==='FREEZE_SCOPE.md')continue;const a=read(P+'frozen_round1/'+row.name),b=read(P+'frozen_round2/'+row.name);ok(a.equals(b),'whole counterpart equality');const prior=data.pairs.find(x=>x.name===row.name);ok(prior&&prior.bytes===b.length&&prior.sha256===sha(b),'copy original record');pairs.push({name:row.name,bytes:b.length,sha256:sha(b)});}
ok(pairs.length===24,'complete24pairs');
const note=read(P+'frozen_round2/FREEZE_SCOPE.md');ok(sha(note)==='da9afbe7d6adbbb4a1f602cd4b547bbdd72478316cca42e6a7f305432b11d646','exact accepted scope');ok(note.equals(read(Q+'qa/p213_round2_terminal_preparation01/FREEZE_SCOPE.accepted.proposed.md')),'whole accepted scope equality');
const accept=read(Q+'qa/p213_b_source_root01/FINAL_B_ACCEPTANCE.md');ok(sha(accept)==='8fe38cd9739958f243d16b2f1bdb6f39c2f72ba547b85294b321d93cf6165d27','root final B acceptance pin');
const bfinal=manifest(Q+'reviews/p213_b/','FINAL_PACKAGE_SHA256SUMS');ok(bfinal.rows.length===28&&bfinal.sha256==='6b34cac7ab45c930eb79c25eec96916523d289bcf920f4b5368c9ae535e2f52c','explicit B final28role');
ok(bfinal.rows.some(x=>x.name==='SHA256SUMS'),'old source seal is subordinate historical payload');
console.log(JSON.stringify({status:'ACCEPT_PHYSICAL_ROUND2_DATA_ONLY',checks,physical_files:files.length,round1_manifest:r1.sha256,round2_manifest:r2.sha256,scope_sha256:sha(note),root_B_acceptance_sha256:sha(accept),B_final_manifest:bfinal.sha256,pairs},null,2));
