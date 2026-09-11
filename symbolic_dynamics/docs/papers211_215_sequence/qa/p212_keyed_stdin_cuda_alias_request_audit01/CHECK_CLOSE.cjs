'use strict';
// Finite documentary closure only. Never execute embedded requests or source.
const fs=require('fs'), crypto=require('crypto'), assert=require('assert/strict');
const Q='docs/papers211_215_sequence/qa/';
const A=Q+'p212_keyed_stdin_cuda_alias_request_audit01/';
const B=Q+'p212_keyed_stdin_cuda_alias_request_preparation01/';
const S=Q+'p212_keyed_stdin_cuda_alias_source_delta01/';
const SR=Q+'p212_keyed_stdin_cuda_alias_source_root01/';
const SA=Q+'p212_keyed_stdin_cuda_alias_source_audit01/';
const TR=Q+'p212_trusted_product_boundary_root01/';
const OLD=Q+'p212_keyed_stdin_observation_root01/';
const FAIL=Q+'p212_keyed_stdin_failed_observation_root01/';
const ext=[SR+'RECEPTION.md',SR+'SHA256SUMS',S+'observe.py',S+'FRONTIER.json',S+'AUTHORIZATION.disabled.json',S+'SHA256SUMS',SA+'REPORT.md',SA+'FINDINGS.json',SA+'SHA256SUMS',TR+'DECISION.json',TR+'RECEPTION.md',OLD+'RELOCATED_TRUST_DECISION.json',OLD+'REQUEST.json',FAIL+'RECEPTION.md',FAIL+'SHA256SUMS'];
const proposal=['ARGV.prospective.json','AUTHORIZATION.disabled.json','AUTHORIZATION.prospective.json','CHECK_DOCUMENTS.cjs','CHECK_NATIVE.json','CHECK_RESULT.json','CLOSING_NATIVE.json','CONTRACT.md','HANDOFF.md','INPUT_KEYS_NATIVE.json','PREFIX.proposed.json','PROSPECTIVE_BYTES.json','PROSPECTIVE_PINS_NATIVE.json','READBACK_NATIVE.json','REQUEST.disabled.json','REQUEST.prospective.json','TRANSFORMATION.json','SHA256SUMS'];
const own=['AUTHOR_REPLAY_NATIVE.json','CHECK_CLOSE.cjs','CHECK_NATIVE.json','CHECK_REQUEST.cjs','CHECK_RESULT.json','FINDINGS.json','HANDOFF.md','INPUTS.sha256','READBACK_NATIVE.json','READS_NATIVE_01.json','READS_NATIVE_02.json','READS_NATIVE_03.json','REPORT.md','SCOPE.md'];
const external=[...ext,...proposal.map(n=>B+n)];
const selected=[...external,...own.map(n=>A+n)], allowed=new Set(selected);
const fields=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs','birthtimeNs'];
const bodies=new Map(), keys=new Map(), pairs=[];
let checks=0;
function ok(v,m){checks++;assert(v,m);}
function eq(x,y,m){checks++;assert.deepStrictEqual(x,y,m);}
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const field=s=>Object.fromEntries(fields.map(n=>[n,String(s[n])]));
function physical(path){
  ok(allowed.has(path),'fixed selected existing documentary operand');
  const first=fs.lstatSync(path,{bigint:true});
  ok(first.isFile()&&first.nlink===1n&&first.size>=0n&&first.size<=5000000n,'bounded physical file');
  const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let raw;
  try{eq(field(fs.fstatSync(fd,{bigint:true})),field(first));raw=fs.readFileSync(fd);eq(field(fs.fstatSync(fd,{bigint:true})),field(first));}finally{fs.closeSync(fd);}
  eq(field(fs.lstatSync(path,{bigint:true})),field(first));eq(BigInt(raw.length),first.size);
  return{raw,key:{path,bytes:raw.length,sha256:sha(raw),fields:field(first)}};
}
for(const path of selected){const r=physical(path);bodies.set(path,r.raw);keys.set(path,r.key);}
const body=p=>{ok(allowed.has(p),'selected cached body');return bodies.get(p);};
const json=p=>JSON.parse(body(p).toString('utf8'));
function settled(r){eq(r.exit_code,0);ok(!r.session_id&&typeof r.output==='string','complete native response');ok(!r.output.startsWith('Warning: truncated output'),'no truncation header');}
function pair(label,x,y){eq(x,y,label);pairs.push({label,bytes:y.length,sha256:sha(y)});}
function numbered(raw){const s=raw.toString('utf8');ok(s.endsWith('\n'));return Buffer.from(s.slice(0,-1).split('\n').map((l,i)=>String(i+1).padStart(6,' ')+'\t'+l+'\n').join(''),'utf8');}
const main=json(A+'CHECK_RESULT.json'), native=json(A+'CHECK_NATIVE.json').record;
settled(native.result);eq(native.result.chunk_id,'aedcac');eq(native.request.cmd,'node '+A+'CHECK_REQUEST.cjs');
pair('original independent result stdout',Buffer.from(native.result.output,'utf8'),body(A+'CHECK_RESULT.json'));
eq([main.checks,main.document_keys,main.keys.length,main.raw_comparisons,main.raw_comparison_bytes],[1277,38,38,50,472543]);
eq(main.proposal,{payloads:17,physical_files:18,payload_bytes:157525,seal_sha256:'c7a4349d3ff0021d52ef2d88fb8d695b09a1e108b2c4db45f104c877b311edba'});
eq(main.keys.filter(k=>external.includes(k.path)).map(k=>k.path),external,'all 33 external keys exactly once');
for(const k of main.keys){ok(allowed.has(k.path),'original key is explicitly selected');eq(keys.get(k.path),k,'whole original ten-field key unchanged');}
pair('exact external input digest manifest',body(A+'INPUTS.sha256'),Buffer.from(external.map(p=>keys.get(p).sha256+'  '+p).join('\n')+'\n','ascii'));
const oldReads=[...json(A+'READS_NATIVE_01.json').records,...json(A+'READS_NATIVE_02.json').records];
const newReads=json(A+'READS_NATIVE_03.json').records;
eq([...oldReads,...newReads].map(r=>r.seq),Array.from({length:38},(_,i)=>i+1));
for(const r of newReads)settled(r.result);
eq(newReads[2],native,'original execution preserved in both native records');
eq(newReads[1].request.cmd,'nl -ba '+A+'CHECK_REQUEST.cjs');
pair('full final checker pre-execution numbered read',Buffer.from(newReads[1].result.output,'utf8'),numbered(body(A+'CHECK_REQUEST.cjs')));
eq(newReads[0].request.cmd,newReads[1].request.cmd,'earlier unrun draft read retained separately');
ok(newReads[0].result.output!==newReads[1].result.output,'unrun draft is not relabelled as final source read');
const replay=json(A+'AUTHOR_REPLAY_NATIVE.json').record;settled(replay.result);eq(replay.result.chunk_id,'26a7c0');
eq(oldReads[34],replay,'actual author replay preserved in both native records');
pair('fresh author replay original stdout',Buffer.from(replay.result.output,'utf8'),body(B+'CHECK_RESULT.json'));
const readbacks=json(A+'READBACK_NATIVE.json').records;
const readbackNames=['REPORT.md','FINDINGS.json','HANDOFF.md','SCOPE.md','INPUTS.sha256','CHECK_CLOSE.cjs'];
eq(readbacks.length,6);eq(readbacks.map(x=>x.seq),[39,40,41,42,43,44]);
for(let i=0;i<readbacks.length;i++){
  const r=readbacks[i],path=A+readbackNames[i];settled(r.result);eq(r.request.cmd,'nl -ba '+path);
  pair('full final substantive numbered read '+readbackNames[i],Buffer.from(r.result.output,'utf8'),numbered(body(path)));
}
const findings=json(A+'FINDINGS.json');eq(findings.census,{Blocker:0,Major:0,Minor:0});eq(findings.findings,[]);
eq(findings.reviewer_status,main.scope);eq(findings.verdict,'ACCEPT_EXACT_PROSPECTIVE_REQUEST_PREFIX_ONLY_UNDER_ORDINARY_TRUST');
eq(findings.independent_check,{chunk_id:'aedcac',exit_code:0,checks:1277,document_keys:38,raw_comparisons:50,raw_comparison_bytes:472543});
eq(findings.prospective,main.prospective);eq(findings.operational_authorization,false);eq(findings.source_manuscript_or_runtime_acceptance,false);
eq(findings.observations_or_allocations,[]);eq(findings.modified_existing_external_files,[]);
const report=body(A+'REPORT.md').toString('utf8'),handoff=body(A+'HANDOFF.md').toString('utf8');
for(const s of[main.scope,findings.verdict,'HOLD_EXTERNAL']){ok(report.includes(s));ok(handoff.includes(s));}
for(const p of main.prospective)ok(report.includes(p.sha256),'complete exact-copy digest retained');
const preclosingManifest=own.map(n=>keys.get(A+n).sha256+'  '+n).join('\n')+'\n';
const selectedPayloadBytes=own.reduce((n,p)=>n+body(A+p).length,0);
for(const[path,key]of keys){const final=physical(path);eq(final.key,key,'closing full key');eq(final.raw,bodies.get(path),'closing full whole bytes');}
process.stdout.write(JSON.stringify({scope:main.scope,checks,selected_external_documents:33,selected_audit_payloads:14,selected_audit_payload_bytes:selectedPayloadBytes,document_keys:keys.size,raw_comparisons:pairs.length,raw_comparison_bytes:pairs.reduce((n,p)=>n+p.bytes,0),pairs,keys:[...keys.values()],preclosing_manifest:preclosingManifest,preclosing_manifest_sha256:sha(Buffer.from(preclosingManifest,'ascii')),final_seal_not_self_attested:true,operational_authorization:false,host_private_stdin_future_paths_observed:false},null,2)+'\n');
