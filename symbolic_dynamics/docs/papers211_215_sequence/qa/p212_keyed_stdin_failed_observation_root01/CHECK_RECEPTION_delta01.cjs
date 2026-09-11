'use strict';
// Root documentary receiver: only the named immutable packets, explicit
// observation documents and the same TWO existing private raw originals.
// No recorded command/observer/import/parser/host target is executed.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics/',QA=ROOT+'docs/papers211_215_sequence/qa/';
const A=QA+'p212_keyed_stdin_observation_failure_audit01/';
const R=QA+'p212_keyed_stdin_observation_root01/';
const D=QA+'p212_keyed_stdin_failed_observation_root01/';
const PRIVATE='/root/symbolic-dynamics-p212-keyed-stdin-observation-20260910-01';
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(F.map(f=>[f,String(s[f])]));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const eq=(a,b,m)=>{checks++;assert.deepEqual(a,b,m);},ok=(a,m)=>{checks++;assert(a,m);};
const selected=new Set([
 ...['GRANT.md','REQUEST.json','ARGV.json','AUTHORIZATION.json','RELOCATED_TRUST_DECISION.json',
 'REQUEST_RECEPTION_NATIVE.json','CAPTURE_PREPARATION_NATIVE.json','ACTUAL_OBSERVER_NATIVE.json',
 'INITIAL_RAW_INTAKE_NATIVE.json','FAILURE_SHAPE_NATIVE.json','CAPTURE_PREPARATION_DECISION.md',
 'PROPOSAL_RECEPTION.md','PROPOSAL_CHECK_NATIVE.json','PROPOSAL_SHAPE_NATIVE.json',
 'PROPOSAL_REPLAY_NATIVE.json','PROPOSAL_READS_NATIVE.json'].map(n=>R+n),
 ...['observe.py','FRONTIER.json'].map(n=>QA+'p212_keyed_stdin_source_delta01/'+n),
 ...['RECEPTION.md','DECISION.json'].map(n=>QA+'p212_trusted_product_boundary_root01/'+n),
 ...['AGENTS.md','.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md'].map(n=>ROOT+n),
 ...['ROOT_READS_NATIVE.json','ROOT_REPLAY_NATIVE.json','ROOT_OTHER_NATIVE.json','CHECK_RECEPTION.cjs','CHECK_RECEPTION_delta01.cjs','FIRST_RECEIVER_FAILURE_NATIVE.json'].map(n=>D+n),
 PRIVATE+'/stdout.raw',PRIVATE+'/stderr.raw'
]);
const bodies=new Map(),keys=new Map();
function read(p){
 ok(selected.has(p),'finite read selection');
 const a=fs.lstatSync(p,{bigint:true});
 ok(a.isFile()&&!a.isSymbolicLink()&&a.size<=134217728n,'physical bounded original');
 if(p.startsWith(PRIVATE+'/')){eq(a.uid,0n);eq(a.mode&0o777n,0o600n);}
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 let b;
 try{eq(meta(fs.fstatSync(fd,{bigint:true})),meta(a));b=fs.readFileSync(fd);eq(meta(fs.fstatSync(fd,{bigint:true})),meta(a));}
 finally{fs.closeSync(fd);}
 eq(meta(fs.lstatSync(p,{bigint:true})),meta(a));eq(b.length,Number(a.size));
 const k={path:p,bytes:b.length,sha256:sha(b),metadata:meta(a)};
 if(keys.has(p))eq(k,keys.get(p),'whole repeated key');
 keys.set(p,k);bodies.set(p,b);return b;
}
const packets=[];
for(const [name,count,digest] of [
 ['p212_keyed_stdin_source_root01',16,'0f65f815ca28d4153bc968b0d8dd041f3571287ebe639c942abce6064bb32380'],
 ['p212_keyed_stdin_nonlineage_audit01',24,'ff622be9502a7bd931820cf1c22b5e858bc09243ef3e0488fe7d65cfbea71887'],
 ['p212_keyed_stdin_input_preparation_root01',5,'aa3d3cf04d02766b6efe6c9184c81876bac019472ca915cecc5d17239b7b9bca'],
 ['p212_keyed_stdin_observation_failure_audit01',13,'75ee5bb631eaf447ae4f7516dd564c6969202f77c8c109f4fd274fec5f289ac2']
]){
 const base=QA+name+'/',manifest=base+'SHA256SUMS';selected.add(manifest);
 const raw=read(manifest),text=raw.toString('ascii');
 eq(sha(raw),digest);ok(text.endsWith('\n')&&!text.endsWith('\n\n'));
 const rows=text.slice(0,-1).split('\n').map(l=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);ok(m!==null&&m[2]!=='SHA256SUMS');return{digest:m[1],name:m[2]};});
 eq(rows.length,count);eq(new Set(rows.map(r=>r.name)).size,count);
 eq(fs.readdirSync(base).sort(),rows.map(r=>r.name).concat('SHA256SUMS').sort());
 let bytes=0;for(const r of rows){selected.add(base+r.name);const b=read(base+r.name);eq(sha(b),r.digest);bytes+=b.length;}
 packets.push({directory:base,payloads:count,files:count+1,payload_bytes:bytes,seal_sha256:digest});
}
for(const p of selected)if(!bodies.has(p))read(p);
const json=p=>JSON.parse(bodies.get(p));
const original=json(A+'RESULT.json'),originalNative=json(A+'CHECK_NATIVE.json'),replay=json(D+'ROOT_REPLAY_NATIVE.json');
eq(originalNative.result.chunk_id,'3aaa58');eq(originalNative.result.exit_code,0);
eq(replay.return.chunk_id,'b8a56d');eq(replay.return.exit_code,0);
eq(replay.request.cmd,'node docs/papers211_215_sequence/qa/p212_keyed_stdin_observation_failure_audit01/CHECK.cjs');
eq(bodies.get(A+'RESULT.json'),Buffer.from(originalNative.result.output),'full original raw stdout');
eq(bodies.get(A+'RESULT.json'),Buffer.from(replay.return.output),'full actual root replay raw stdout');
eq(original.checks,72772);eq(original.document_and_private_keys.length,73);
eq(original.verdict,'ACCEPT_FAILED_RAW_ORIGINALS_ONLY');
for(const k of original.document_and_private_keys){ok(keys.has(k.path));eq(keys.get(k.path),k,'all 73 original complete keys');}
const artifact=json(A+'ARTIFACT_NATIVE.json');eq(artifact.result.chunk_id,'471d83');eq(artifact.result.exit_code,0);
const closing=JSON.parse(artifact.result.output);eq(closing.checks,804);eq(closing.keys.length,85);
eq(closing.own_preclosure_payloads,12);eq(closing.full_runtime_acceptance,false);
for(const k of closing.keys){ok(keys.has(k.path),'historical preclosure finite selection');eq(keys.get(k.path),k,'all 85 actual historical closing keys');}
eq(closing.result_stdout_raw_bytes,bodies.get(A+'RESULT.json').length);
eq(closing.result_stdout_sha256,sha(bodies.get(A+'RESULT.json')));
const incomplete=json(A+'CHECK_TRUNCATED_NATIVE.json');eq(incomplete.result.chunk_id,'5d854e');eq(incomplete.result.exit_code,0);
ok(incomplete.result.output.startsWith('Warning: truncated output'),'preserved incomplete tool transport');
const census=json(A+'FINDINGS.json');eq(census.current_artifact_findings,{Blocker:0,Major:0,Minor:0});
eq(census.retained_operational_failure.closed_by_artifact_acceptance,false);eq(census.retained_operational_failure.new_invocation_authorized,false);
const raw=bodies.get(PRIVATE+'/stdout.raw'),err=bodies.get(PRIVATE+'/stderr.raw');
eq(raw.length,7802105);eq(sha(raw),'4c430a238251197d811a03b3f43e148ceed9ca34d4381ecaa0da284cf59e2f50');eq(err.length,0);
const privateDir=fs.lstatSync(PRIVATE,{bigint:true});ok(privateDir.isDirectory()&&!privateDir.isSymbolicLink());eq(privateDir.uid,0n);eq(privateDir.mode&0o777n,0o700n);
eq(meta(privateDir),original.private_directory_key);eq(meta(privateDir),closing.private_directory_key);
const viewed=[];
function slice(p,first,last,numbered){
 ok(bodies.has(p),'source rendering refers only to selected pinned document');
 const b=bodies.get(p),s=b.toString('utf8');eq(Buffer.from(s),b,'lossless source decoding');
 const lines=s.match(/[^\n]*\n|[^\n]+$/g)||[];
 return Buffer.from(lines.slice(first-1,last).map((l,i)=>numbered?String(first+i).padStart(6,' ')+'\t'+l:l).join(''));
}
let ownBytes=0;
for(const r of json(D+'ROOT_READS_NATIVE.json')){
 eq(r.return.exit_code,0);ok(!/^Warning: truncated output/.test(r.return.output),'tool truncation header, not a substring in source');
 const m=/^sed -n '(\d+),(\d+)p' (docs\/[A-Za-z0-9_./-]+)$/.exec(r.request.cmd);ok(m!==null);
 const p=ROOT+m[3],expected=slice(p,Number(m[1]),Number(m[2]),false);
 eq(Buffer.from(r.return.output),expected,'root entire exact source/prose slice');
 ownBytes+=expected.length;viewed.push({key:r.key,path:p,bytes:expected.length,sha256:sha(expected)});
}
eq(viewed.length,8);
let numbered=0,numberedBytes=0,document=0,documentBytes=0;
for(const r of [...json(A+'READS_NATIVE.json'),...json(A+'READS_MORE_NATIVE.json')]){
 eq(r.result.exit_code,0);const cmd=r.request.cmd;
 const n=/^nl -ba (docs\/[A-Za-z0-9_./-]+) \| sed -n '(\d+),(\d+)p'$/.exec(cmd);
 const m=/^sed -n '(\d+),(\d+)p' (docs\/[A-Za-z0-9_./-]+)$/.exec(cmd);
 if(n){const expected=slice(ROOT+n[1],Number(n[2]),Number(n[3]),true);eq(Buffer.from(r.result.output),expected);numbered++;numberedBytes+=expected.length;}
 else if(m){const expected=slice(ROOT+m[3],Number(m[1]),Number(m[2]),false);eq(Buffer.from(r.result.output),expected);document++;documentBytes+=expected.length;}
}
eq(numbered,closing.source_renderings);eq(numberedBytes,closing.source_rendered_bytes);
eq(document,closing.native_document_renderings);eq(documentBytes,closing.native_document_rendered_bytes);
const before=[...keys.values()];for(const k of before){read(k.path);eq(keys.get(k.path),k);}
eq(meta(fs.lstatSync(PRIVATE,{bigint:true})),meta(privateDir),'private directory closing only');
process.stdout.write(JSON.stringify({
 status:'ROOT_FAILED_ORIGINALS_RECEIVED_NO_RUNTIME_PASS_OR_RETRY',checks,packets,
 full_keys:[...keys.values()],all_73_original_keys_unchanged:true,all_85_historical_closing_keys_unchanged:true,
 root_documentary_replay:{chunk_id:replay.return.chunk_id,checks:72772,raw_bytes:67003,sha256:sha(bodies.get(A+'RESULT.json')),equals_independent_original_raw:true},
 root_raw_reads:viewed,root_raw_read_bytes:ownBytes,
 independent_raw_reads:{numbered,numbered_bytes:numberedBytes,document,document_bytes:documentBytes},
 actual_observer_invocations:1,new_observer_invocations_here:0,
 actual_observer_exit:78,full_runtime_acceptance:false,retry_granted:false,
 private_raw_body_exported:false,private_directory_key:meta(privateDir)
},null,2)+'\n');
