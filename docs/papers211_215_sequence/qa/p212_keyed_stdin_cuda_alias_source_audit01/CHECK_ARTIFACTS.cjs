'use strict';
// Audit artifact/data-only closure. No reviewed source or embedded path runs.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',BASE='docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_audit01';
const INPUTS=[
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_decision01/DECISION.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_decision01/FRONTIER_DOCUMENT_SELECTION_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_decision01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/AUTHORIZATION.disabled.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/CHECK_DOCUMENTS.cjs",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/CHECK_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/CHECK_RESULT.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/CLOSING_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/CONTRACT.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/DELTA.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/DIFF_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/EVIDENCE.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/FRONTIER.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/HANDOFF.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/INPUTS.sha256",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/INPUT_KEYS_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/ORIGINAL_READS_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/OWN_READS_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/PREPARATION_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/REQUEST.disabled.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/diffs/AUTHORIZATION.disabled.json.diff",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/diffs/FRONTIER.json.diff",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/diffs/observe.py.diff",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/observe.py",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_failed_observation_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_failed_observation_root01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_linecount_erratum01/ERRATUM.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_linecount_erratum01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_nonlineage_audit01/FINDINGS.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_nonlineage_audit01/HANDOFF.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_nonlineage_audit01/READ_SCOPE.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_nonlineage_audit01/REPORT.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_nonlineage_audit01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/AUTHORIZATION.disabled.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/FRONTIER.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/FRONTIER_REASONING.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/HANDOFF.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/SOURCE_CONTRACT.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/driver.js",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/node_preload.js",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/node_runtime_probe.js",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/observe.py",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/outer_contract.py",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/product_capture.js",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/python_runtime_probe.py",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_root01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_trusted_product_boundary_root01/DECISION.json",
  "docs/papers211_215_sequence/qa/p212_trusted_product_boundary_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_trusted_product_boundary_root01/SHA256SUMS"
];
const PRE=['AUTHOR_REPLAY_NATIVE.json','AUTHOR_REPLAY_RESULT.json','CHECK_ARTIFACTS.cjs','CHECK_NATIVE.json','CHECK_RESULT.json','CHECK_SOURCE_DELTA.cjs','EXTRA_READS_NATIVE.json','FINAL_READS_NATIVE.json','FINDINGS.json','HANDOFF.md','INPUTS.sha256','PREPARATION_NATIVE.json','READS_NATIVE.json','READ_SCOPE.md','REPORT.md'];
const mode=process.argv[2]??'preseal';
assert(['preseal','sealed'].includes(mode)&&process.argv.length<=3,'one documentary layout choice');
const names=mode==='preseal'?PRE:[...PRE,'CLOSING_NATIVE.json','SHA256SUMS'].sort();
const permitted=new Set([...INPUTS,...names.map(n=>BASE+'/'+n)]);
const FIELDS=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs','birthtimeNs'];
let checks=0;const files=new Map();
function ok(v,m){checks++;assert(v,m);}
function eq(a,b,m){checks++;assert.deepStrictEqual(a,b,m);}
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const shape=s=>Object.fromEntries(FIELDS.map(k=>[k,String(s[k])]));
function whole(p){
 ok(permitted.has(p),'exact documentary selection before filesystem operation');
 const l=fs.lstatSync(ROOT+'/'+p,{bigint:true});ok(l.isFile()&&!l.isSymbolicLink()&&l.nlink===1n,'physical regular single-link file');
 const fd=fs.openSync(ROOT+'/'+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{const s=fs.fstatSync(fd,{bigint:true});eq(shape(s),shape(l),'actual same selected fd');
 const raw=fs.readFileSync(fd);eq(shape(fs.fstatSync(fd,{bigint:true})),shape(s),'unchanged fd after whole read');
 eq(shape(fs.lstatSync(ROOT+'/'+p,{bigint:true})),shape(s),'unchanged lexical endpoint');eq(BigInt(raw.length),s.size,'whole byte length');
 return {raw,key:{path:p,bytes:raw.length,sha256:hash(raw),lf_lines:raw.reduce((n,b)=>n+(b===10),0),fields:shape(s)}};
 }finally{fs.closeSync(fd);}
}
function inventory(){const s=fs.lstatSync(ROOT+'/'+BASE);ok(s.isDirectory()&&!s.isSymbolicLink(),'one owned physical audit directory');
 eq(fs.readdirSync(ROOT+'/'+BASE).sort(),[...names].sort(),'complete exact physical audit layout');}
inventory();
for(const p of [...permitted].sort())files.set(p,whole(p));
const get=p=>{ok(files.has(p),'already selected whole document');return files.get(p).raw;};
const own=n=>get(BASE+'/'+n),parse=n=>JSON.parse(own(n));
const result=parse('CHECK_RESULT.json'),native=parse('CHECK_NATIVE.json');
eq(native.run.result.exit_code,0,'actual independent documentary check exit');
eq(native.run.result.chunk_id,'1b2bf6','actual original independent source-check identity');
eq(native.run.request.cmd,'node '+BASE+'/CHECK_SOURCE_DELTA.cjs','exact actual source-check request');
eq(Buffer.from(native.run.result.output),own('CHECK_RESULT.json'),'whole raw own check attachment');
eq(native.checker_read.result.exit_code,0,'own checker full read settled');
eq(Buffer.from(native.checker_read.result.output),own('CHECK_SOURCE_DELTA.cjs'),'whole actual own checker read');
eq(result.checks,16959,'actual assertions');eq(result.keys.length,58,'all original own keys');
for(const k of result.keys){ok(files.has(k.path),'original key explicitly selected');eq(files.get(k.path).key,k,'entire original key remains unchanged');}
const nonself=result.keys.filter(k=>!k.path.startsWith(BASE+'/'));
eq(nonself.map(k=>k.path),INPUTS,'all 52 exact selected non-own documents');
eq(own('INPUTS.sha256'),Buffer.from(nonself.map(k=>k.sha256+'  '+k.path).join('\n')+'\n'),'whole exact input pin list');
const reads=parse('FINAL_READS_NATIVE.json');
eq(reads.result.exit_code,0,'actual final report read settled');
const renderNames=['FINDINGS.json','REPORT.md','READ_SCOPE.md','HANDOFF.md'];
eq(reads.request.cmd,'cat '+renderNames.map(n=>BASE+'/'+n).join(' '),'exact complete final prose read request');
eq(Buffer.from(reads.result.output),Buffer.concat(renderNames.map(own)),'whole final report/read-scope/census/handoff raw correspondence');
const census=parse('FINDINGS.json');
eq(census.census,{Blocker:0,Major:0,Minor:0},'actual current scoped findings');
eq(census.findings,[],'no concealed scoped finding rows');
eq(census.auditor,'/root/p212_cuda_delta_audit','actual independent auditor');
eq(census.operational_authorization,false,'no grant');
eq(census.independence.manuscript_review,false,'not manuscript review');
for(const name of ['REPORT.md','HANDOFF.md']){
 const s=own(name).toString('utf8');
 ok(s.includes(census.verdict),'exact scoped source verdict carried');
 ok(s.includes(census.accepted_source_packet.seal_sha256),'exact author source combination carried');
 ok(s.includes('16,959')&&s.includes('58'),'actual independent result carried');
 ok(s.includes('17,454')&&s.includes('26,935'),'actual documentary replay carried');
}
const replay=parse('AUTHOR_REPLAY_NATIVE.json');
eq(replay.result.exit_code,0,'actual author-checker replay success');
eq(own('AUTHOR_REPLAY_RESULT.json'),Buffer.from(replay.result.output),'actual whole replay stdout attachment');
const extra=parse('EXTRA_READS_NATIVE.json');eq(extra.reads.length,1,'one full documentary original closing command inspection');
const e=extra.reads[0];eq(e.result.exit_code,0,'actual data inspector settled');
const inspection=JSON.parse(e.result.output),authorClosing=JSON.parse(get('docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/CLOSING_NATIVE.json'));
eq(inspection.keys,Object.keys(authorClosing),'whole original closing envelope keys');
eq(inspection.closing_request,authorClosing.request,'full original embedded closing command is read unchanged as data');
eq(inspection.result_keys,Object.keys(authorClosing.result),'actual closing result shape');
const preparation=parse('PREPARATION_NATIVE.json');eq(preparation.destination_check.result.exit_code,0,'exclusive new audit destination actual check');
eq(preparation.role.auditor,census.auditor,'own disclosed role');
if(mode==='sealed'){
 const closing=parse('CLOSING_NATIVE.json');
 eq(closing.run.result.exit_code,0,'actual preseal audit closure settled');
 eq(closing.run.request.cmd,'node '+BASE+'/CHECK_ARTIFACTS.cjs','exact actual documentary closure request');
 eq(closing.checker_read.result.exit_code,0,'full artifact checker read settled');
 eq(Buffer.from(closing.checker_read.result.output),own('CHECK_ARTIFACTS.cjs'),'entire actual artifact checker source read');
 const before=JSON.parse(closing.run.result.output);eq(before.mode,'preseal','historical preseal mode');
 eq(before.own_payloads,15,'historical complete preseal inventory');
 eq(before.keys.length,67,'historical entire source plus own key set');
 for(const k of before.keys){ok(files.has(k.path),'all historical closure keys explicit');eq(files.get(k.path).key,k,'all whole closing keys remain unchanged');}
 const rows=own('SHA256SUMS').toString('utf8').split('\n');eq(rows.pop(),'','exact final seal LF');eq(rows.length,16,'complete final nonself seal');
 const named=[];
 for(const row of rows){const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.]+)$/.exec(row);ok(m,'strict flat nonself seal grammar');
  ok(m[2]!=='SHA256SUMS'&&!named.includes(m[2]),'nonself unique seal path');named.push(m[2]);eq(hash(own(m[2])),m[1],'whole final sealed payload');}
 eq(named,[...PRE,'CLOSING_NATIVE.json'].sort(),'all final payloads and only them');
}
for(const [p,{key}] of files)eq(whole(p).key,key,'final unchanged whole document endpoint');
inventory();
const ownBytes=names.filter(n=>n!=='SHA256SUMS').reduce((n,p)=>n+own(p).length,0);
console.log(JSON.stringify({scope:'AUDIT_DOCUMENTARY_ARTIFACT_CLOSURE_ONLY',mode,checks,own_payloads:mode==='preseal'?15:16,physical_files:names.length,
 own_payload_bytes:ownBytes,
 whole_document_keys:files.size,original_source_check_keys:58,nonself_input_pins:52,final_prose_read_bytes:Buffer.byteLength(reads.result.output),
 keys:[...files.values()].map(x=>x.key),observer_run:false,host_or_private_or_input_probe:false,root_acceptance:false,grant:false},null,2));
