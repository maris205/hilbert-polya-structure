'use strict';
// Own frozen documentary packet only; never evaluates reviewed or other-auditor source.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict');
const own='docs/papers211_215_sequence/qa/p212_keyed_stdin_nonlineage_audit01/';
const names=['BOOTSTRAP_NATIVE.json','CLOSING_NATIVE.json','DELTA_RESULT.json','FINDINGS.json','HANDOFF.md','INCIDENTS.json','INPUTS_AFTER.json','INPUTS_BEFORE.json','NATIVE01.json','NATIVE02.json','READ_SCOPE.md','RECEIPT_RESULT.json','REPORT.md','check_artifacts.cjs','check_delta.cjs','check_inputs.cjs','check_inputs_delta01.cjs','check_inputs_delta02.cjs','check_receipts.cjs'];
let checks=0;const eq=(a,b,m)=>{checks++;assert.deepEqual(a,b,m);};const ok=(a,m)=>{checks++;assert(a,m);};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const mode=process.argv[2]||'prepare';
function read(name){ok(names.includes(name)||['ARTIFACT_NATIVE.json','SHA256SUMS'].includes(name),'exact owned name');const s=fs.lstatSync(own+name);ok(s.isFile()&&!s.isSymbolicLink(),'physical owned file');return fs.readFileSync(own+name);}
const keys=names.map(name=>{const b=read(name);return{name,bytes:b.length,sha256:sha(b)};});
const before=JSON.parse(read('INPUTS_BEFORE.json')),after=JSON.parse(read('INPUTS_AFTER.json'));
eq(after.inputs,before.inputs,'all 130 before-after keys');eq(after.inputs.length,130);eq(after.checks,1224);
const closing=JSON.parse(read('CLOSING_NATIVE.json'));const c=closing.calls.find(x=>x.return?.chunk_id==='a5d6a7');ok(c,'actual closing native');eq(c.return.exit_code,0);eq(Buffer.from(c.return.output),read('INPUTS_AFTER.json'),'whole closing stdout attachment');
const initial=JSON.parse(read('BOOTSTRAP_NATIVE.json'));
for(const [i,p]of [[1,'.agents/skills/symbolic-dynamics-research/SKILL.md'],[2,'docs/research_state/WORKFLOW.md']]){
 const b=Buffer.from(initial.calls[i].return.output),pin=before.inputs.find(x=>x.path===p);ok(pin,'pinned instruction');
 eq(b.length,pin.bytes,'transcribed initial instruction bytes');eq(sha(b),pin.sha256,'transcribed initial output whole hash');
}
const native1=JSON.parse(read('NATIVE01.json')),native2=JSON.parse(read('NATIVE02.json'));
const nr=native2.calls.find(x=>x.return?.chunk_id==='9c7519');ok(nr,'receipt native');eq(read('RECEIPT_RESULT.json'),Buffer.from(nr.return.output),'receipt raw output attachment');
eq(JSON.parse(read('RECEIPT_RESULT.json')).checks,803);
for(const n of ['check_inputs.cjs','check_inputs_delta01.cjs']){
 const r=native1.calls.find(x=>x.request?.cmd==='node '+own+n);ok(r,'failed original native retained '+n);eq(r.return.exit_code,1);
}
const delta=JSON.parse(read('DELTA_RESULT.json'));eq(delta.checks,7082);eq(delta.pairs.length,19);
const f=JSON.parse(read('FINDINGS.json'));eq(f.current_source_census,{Blocker:0,Major:0,Minor:0});eq(f.received_finding.independent_actual_lines,2679);
ok(!f.limited_prior_review_is_independent_full_acceptance,'no inherited reviewer misclassification');
const allowed=names.concat(mode==='seal'?['ARTIFACT_NATIVE.json','SHA256SUMS']:[]).sort();
eq(fs.readdirSync(own).sort(),allowed,'complete exact owned physical membership');
if(mode==='seal'){
 const record=JSON.parse(read('ARTIFACT_NATIVE.json'));eq(record.return.exit_code,0);
 const check=JSON.parse(record.return.output);eq(check.keys,keys,'all earlier owned payload keys unchanged');eq(check.mode,'prepare');
 const b=read('SHA256SUMS'),s=b.toString();ok(s.endsWith('\n')&&!s.endsWith('\n\n')&&!s.includes('\r'),'one final LF');
 const rows=s.slice(0,-1).split('\n').map(line=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);ok(m,'strict bare-relative manifest');ok(m[2]!=='SHA256SUMS','nonself');return{sha256:m[1],name:m[2]};});
 eq(rows.map(x=>x.name),names.concat('ARTIFACT_NATIVE.json').sort(),'all payloads once, sorted');
 for(const r of rows)eq(sha(read(r.name)),r.sha256,'actual payload bytes '+r.name);
 process.stdout.write(JSON.stringify({kind:'INDEPENDENT_AUDIT_FINAL_SEAL_CHECK',mode,checks,payloads:rows.length,files:allowed.length,manifest_bytes:b.length,manifest_sha256:sha(b)},null,2)+'\n');
}else process.stdout.write(JSON.stringify({kind:'INDEPENDENT_AUDIT_ARTIFACT_PRESEAL_CHECK',mode,checks,keys,no_reviewed_program_execution:true,no_host_or_runtime_observation:true},null,2)+'\n');

