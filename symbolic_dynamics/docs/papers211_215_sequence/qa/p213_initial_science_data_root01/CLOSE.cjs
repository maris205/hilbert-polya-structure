'use strict';
// Root finite documentary closure, no producer/science/host/canonical action.
const fs=require('node:fs'),path=require('node:path');
const make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const R='docs/papers211_215_sequence/qa/p213_initial_science_data_root01/';
const spec=JSON.parse(fs.readFileSync(R+'INPUT_SPEC.json','utf8'));
const PRE=['INPUT_SPEC.json','ROOT_READS_NATIVE.json','REPLAY_NATIVE.json','CHECK_ROOT.cjs','CHECK_NATIVE.json','RESULT.json','RECEPTION.md','CLOSE.cjs'];
const FINAL=[...PRE,'CLOSING_NATIVE.json','CLOSING_RESULT.json'];
const final=process.argv.length===3&&process.argv[2]==='--sealed',names=final?[...FINAL,'SHA256SUMS']:PRE;
const r=make(new Set([...spec.external.map(p=>p.path),...names.map(n=>R+n)])),read=p=>r.read(p),json=p=>JSON.parse(read(p).toString('utf8'));
r.need(process.argv.length===2||final,'EXACT_ROOT_CLOSURE_MODE');
for(const p of [...spec.external.map(p=>p.path),...names.map(n=>R+n)])read(p);
r.need(r.equal(json(R+'INPUT_SPEC.json'),spec),'ENTIRE_BOOTSTRAP_SPEC');
for(const p of spec.external)r.need(read(p.path).length===p.bytes&&r.sha(read(p.path))===p.sha256,'ENTIRE_FIXED_EXTERNAL_PIN');
r.need(r.equal(fs.readdirSync(R).sort(),names.slice().sort()),'EXACT_ROOT_PHASE_LAYOUT');
const n=json(R+'CHECK_NATIVE.json'),v=json(R+'RESULT.json');
r.need(n.result.chunk_id==='c05de0'&&n.result.exit_code===0&&!('session_id'in n.result),'ACTUAL_ROOT_ORIGINAL_RECEPTION');
r.need(r.equal(n.request,{cmd:'node '+R+'CHECK_ROOT.cjs',workdir:'/root/autodl-tmp/symbolic_dynamics',max_output_tokens:100000}),'ENTIRE_ACTUAL_ROOT_REQUEST');
r.need(Buffer.from(n.result.output).equals(read(R+'RESULT.json')),'ENTIRE_ROOT_CANONICAL_STDOUT_RAW_EQUAL');
r.need(v.status==='PASS_ROOT_ORIGINAL_INITIAL_CONTROL_AND_BOUNDED_SCIENCE_DATA'&&v.checks===27459&&v.key_count===81&&v.historical_key_occurrences===376&&v.raw_pairs.length===26&&v.root_read_coverage.length===21,'EXACT_ROOT_ORIGINAL_SCOPE');
let oldKeys=0;function receiveKeys(keys){for(const k of keys){r.need(r.keys.has(k.path)&&r.equal(k,r.keys.get(k.path)),'ENTIRE_PRIOR_CURRENT_KEY');oldKeys++;}}
receiveKeys(v.keys);
const receipt=read(R+'RECEPTION.md').toString('utf8'),links=[];
for(const m of receipt.matchAll(/\]\(([^)]+)\)/g)){if(/^https?:\/\//.test(m[1]))continue;const resolved=path.posix.normalize(R+m[1]);r.need(r.keys.has(resolved),'CURRENT_FIXED_RECEIPT_LINK');read(resolved);links.push({target:m[1],resolved});}
r.need(receipt.includes('HOLD_EXTERNAL')&&receipt.includes('Initial aa582c is neither replay'),'LATER_GATE_BOUNDARIES_RETAINED');
if(final){const cn=json(R+'CLOSING_NATIVE.json'),cv=json(R+'CLOSING_RESULT.json');r.need(cn.request.cmd==='node '+R+'CLOSE.cjs'&&cn.result.exit_code===0&&!('session_id'in cn.result),'ACTUAL_PRESEAL_NATIVE');r.need(Buffer.from(cn.result.output).equals(read(R+'CLOSING_RESULT.json'))&&cv.phase==='PRESEAL_EIGHT_PAYLOADS'&&cv.status==='PASS_ROOT_INITIAL_DATA_DOCUMENTARY_CLOSURE','ENTIRE_PRESEAL_STDOUT_RAW_EQUAL');receiveKeys(cv.keys);
 const lines=read(R+'SHA256SUMS').toString('utf8').split('\n');r.need(lines.pop()==='','SEAL_FINAL_LF');const rows=lines.map(l=>{const m=l.match(/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/);r.need(!!m,'STRICT_NONSELF_ROW');return{name:m[2],sha256:m[1]};});r.need(r.equal(rows.map(p=>p.name),FINAL.slice().sort()),'EXACT_TEN_FINAL_PAYLOADS');for(const p of rows)r.need(r.sha(read(R+p.name))===p.sha256,'COMPLETE_NONSELF_HASH');}
const payloads=(final?FINAL:PRE).slice().sort().map(n=>({path:R+n,bytes:read(R+n).length,sha256:r.sha(read(R+n))}));
process.stdout.write(JSON.stringify({status:'PASS_ROOT_INITIAL_DATA_DOCUMENTARY_CLOSURE',phase:final?'FINAL_TEN_PAYLOADS':'PRESEAL_EIGHT_PAYLOADS',checks:r.checks,key_count:r.keys.size,total_read_bytes:r.total,complete_prior_key_comparisons:oldKeys,links,payloads,payload_bytes:payloads.reduce((s,p)=>s+p.bytes,0),science_execution:false,host_query:false,canonical_adoption:false,operation_grant:false,keys:[...r.keys.values()]},null,2)+'\n');
