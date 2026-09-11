'use strict';
// Root-owned finite documentary closing only; no submitted program is loaded.
const fs=require('node:fs'),path=require('node:path');
const make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const R='docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_root01/';
const spec=JSON.parse(fs.readFileSync(R+'INPUT_SPEC.json','utf8'));
const PRE=['INPUT_SPEC.json','ROOT_READS_NATIVE.json','ROOT_WEB_NATIVE.json','REPLAY_NATIVE.json','CHECK_ROOT.cjs','CHECK_NATIVE.json','RESULT.json','RECEPTION.md','CLOSE.cjs'];
const FINAL=[...PRE,'CLOSING_NATIVE.json','CLOSING_RESULT.json'];
const final=process.argv.length===3&&process.argv[2]==='--sealed';
const names=final?[...FINAL,'SHA256SUMS']:PRE;
const allowed=new Set([...spec.external.map(p=>p.path),...spec.extra_docs,...names.map(n=>R+n)]);
const r=make(allowed),read=p=>r.read(p),json=p=>{const b=read(p),v=JSON.parse(b.toString('utf8'));r.need(Buffer.from(JSON.stringify(v,null,2)+'\n').equals(b),'ENTIRE_CANONICAL_JSON');return v;};
r.need(process.argv.length===2||final,'EXACT_CLOSING_MODE');
for(const p of allowed)read(p);
r.need(r.equal(json(R+'INPUT_SPEC.json'),spec),'WHOLE_BOOTSTRAP_SPEC');
for(const p of spec.external)r.need(read(p.path).length===p.bytes&&r.sha(read(p.path))===p.sha256,'UNCHANGED_EXTERNAL_WHOLE_PIN');
r.need(r.equal(fs.readdirSync(R).sort(),names.slice().sort()),'EXACT_PHASE_NONSELF_INVENTORY');
const n=json(R+'CHECK_NATIVE.json'),v=json(R+'RESULT.json');
r.need(n.tool==='exec_command'&&n.result.chunk_id==='a7674a'&&n.result.exit_code===0&&!('session_id'in n.result),'ACTUAL_ROOT_CHECK_NATIVE');
r.need(r.equal(n.request,{cmd:'node '+R+'CHECK_ROOT.cjs',workdir:'/root/autodl-tmp/symbolic_dynamics',max_output_tokens:100000}),'WHOLE_ROOT_REQUEST');
r.need(Buffer.from(n.result.output).equals(read(R+'RESULT.json')),'ENTIRE_ROOT_STDOUT_CANONICAL_RAW_EQUAL');
r.need(v.checks===19903&&v.key_count===67&&v.historical_key_occurrences===333&&v.raw_pairs.length===32&&v.root_read_coverage.length===21&&v.excluded_reads.length===2,'EXACT_CURRENT_ROOT_RECEPTION_SCOPE');
function oldKeys(keys){for(const k of keys){const current=r.keys.get(k.path);r.need(!!current&&r.equal(k,current),'ALL_COMPLETE_PREVIOUS_DOCUMENT_KEY_FIELDS');}}
oldKeys(v.keys);
const links=[];
for(const m of read(R+'RECEPTION.md').toString('utf8').matchAll(/\]\(([^)]+)\)/g)){
 const target=m[1];if(/^https?:\/\//.test(target))continue;
 const resolved=path.posix.normalize(R+target);r.need(allowed.has(resolved),'LOCAL_RECEIPT_LINK_FIXED_SCOPE');read(resolved);links.push({target,resolved});
}
r.need(read(R+'RECEPTION.md').includes(Buffer.from('HOLD_OPERATIONAL / HOLD_EXTERNAL')),'SOURCE_ONLY_HOLDS_REMAIN');
if(final){
 const cn=json(R+'CLOSING_NATIVE.json'),cv=json(R+'CLOSING_RESULT.json');
 r.need(cn.result.exit_code===0&&!('session_id'in cn.result)&&cn.request.cmd==='node '+R+'CLOSE.cjs','ACTUAL_PRIOR_PRESEAL_NATIVE');
 r.need(Buffer.from(cn.result.output).equals(read(R+'CLOSING_RESULT.json'))&&cv.phase==='PRESEAL_NINE_PAYLOADS'&&cv.status==='PASS_ROOT_SOURCE_DOCUMENTARY_CLOSURE_ONLY','ENTIRE_PRESEAL_STDOUT_RAW');
 oldKeys(cv.keys);
 const lines=read(R+'SHA256SUMS').toString('utf8').split('\n');r.need(lines.pop()==='','FINAL_SEAL_LF');
 const rows=lines.map(l=>{const m=l.match(/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/);r.need(!!m,'STRICT_FINAL_ROW');return{sha256:m[1],name:m[2]};});
 r.need(r.equal(rows.map(x=>x.name),FINAL.slice().sort()),'EXACT_ELEVEN_FINAL_NONSELF_PAYLOADS');
 for(const p of rows)r.need(r.sha(read(R+p.name))===p.sha256,'WHOLE_FINAL_NONSELF_PAYLOAD_HASH');
}
const payloads=(final?FINAL:PRE).slice().sort().map(n=>({path:R+n,bytes:read(R+n).length,sha256:r.sha(read(R+n))}));
process.stdout.write(JSON.stringify({status:'PASS_ROOT_SOURCE_DOCUMENTARY_CLOSURE_ONLY',phase:final?'FINAL_ELEVEN_PAYLOADS':'PRESEAL_NINE_PAYLOADS',checks:r.checks,key_count:r.keys.size,total_read_bytes:r.total,unchanged_root_keys:v.keys.length,links,payloads,payload_bytes:payloads.reduce((s,p)=>s+p.bytes,0),host_or_future_path_observation:false,source_execution:false,operation_grant:false,keys:[...r.keys.values()]},null,2)+'\n');
