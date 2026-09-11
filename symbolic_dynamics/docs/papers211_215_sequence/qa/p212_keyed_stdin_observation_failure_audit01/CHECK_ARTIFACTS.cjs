'use strict';
// Final documentary closure. No recorded command or reviewed source is run.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics/',QA=ROOT+'docs/papers211_215_sequence/qa/';
const D=QA+'p212_keyed_stdin_observation_failure_audit01/';
const PRIVATE='/root/symbolic-dynamics-p212-keyed-stdin-observation-20260910-01';
const names=['CHECK.cjs','CHECK_TRUNCATED_NATIVE.json','CHECK_NATIVE.json','READS_NATIVE.json',
 'RESULT.json','READS_MORE_NATIVE.json','REPORT.md','FINDINGS.json','READ_SCOPE.md','INCIDENTS.json',
 'HANDOFF.md','CHECK_ARTIFACTS.cjs'];
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(F.map(k=>[k,String(s[k])]));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const eq=(a,b,m)=>{checks++;assert.deepEqual(a,b,m);},ok=(a,m)=>{checks++;assert(a,m);};
const selected=new Set(names.map(n=>D+n)),body=new Map(),keys=new Map();
function read(p){
 ok(selected.has(p),'exact documentary/two-original selection');const s=fs.lstatSync(p,{bigint:true});
 ok(s.isFile()&&!s.isSymbolicLink()&&s.size<=134217728n,'bounded physical file');
 if(p.startsWith(PRIVATE+'/')){eq(s.uid,0n);eq(s.mode&0o777n,0o600n);}
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b,m;
 try{m=meta(fs.fstatSync(fd,{bigint:true}));eq(m,meta(s));b=fs.readFileSync(fd);eq(meta(fs.fstatSync(fd,{bigint:true})),m);}finally{fs.closeSync(fd);}
 eq(meta(fs.lstatSync(p,{bigint:true})),m);eq(String(b.length),m.size);
 const k={path:p,bytes:b.length,sha256:sha(b),metadata:m};if(keys.has(p))eq(k,keys.get(p));keys.set(p,k);body.set(p,b);return b;
}
const inventory=fs.readdirSync(D).sort();eq(inventory,names.slice().sort(),'preseal exact own inventory');
for(const n of names)read(D+n);
const j=n=>JSON.parse(body.get(D+n));
const native=j('CHECK_NATIVE.json'),result=j('RESULT.json'),short=j('CHECK_TRUNCATED_NATIVE.json');
eq(native.result.chunk_id,'3aaa58');eq(native.result.exit_code,0);eq(native.request.cmd,'node docs/papers211_215_sequence/qa/p212_keyed_stdin_observation_failure_audit01/CHECK.cjs');
eq(native.request.max_output_tokens,40000);ok(!native.result.output.startsWith('Warning: truncated output'));
eq(body.get(D+'RESULT.json'),Buffer.from(native.result.output),'entire actual checker stdout vs attached raw bytes');
eq(result.checks,72772);eq(result.document_and_private_keys.length,73);
eq(short.result.chunk_id,'5d854e');eq(short.result.exit_code,0);ok(short.result.output.startsWith('Warning: truncated output'),'old incomplete transport remains visibly incomplete');
eq(result.verdict,j('FINDINGS.json').verdict);eq(j('FINDINGS.json').current_artifact_findings,{Blocker:0,Major:0,Minor:0});
const packetNames=new Set(['p212_keyed_stdin_source_root01','p212_keyed_stdin_nonlineage_audit01','p212_keyed_stdin_input_preparation_root01']);
const exactDocs=new Set([
 'AGENTS.md','.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md',
 ...['observe.py','FRONTIER.json'].map(n=>'docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/'+n),
 ...['RECEPTION.md','DECISION.json'].map(n=>'docs/papers211_215_sequence/qa/p212_trusted_product_boundary_root01/'+n),
 ...['GRANT.md','REQUEST.json','ARGV.json','AUTHORIZATION.json','RELOCATED_TRUST_DECISION.json','REQUEST_RECEPTION_NATIVE.json','CAPTURE_PREPARATION_NATIVE.json','ACTUAL_OBSERVER_NATIVE.json','INITIAL_RAW_INTAKE_NATIVE.json','FAILURE_SHAPE_NATIVE.json','CAPTURE_PREPARATION_DECISION.md','PROPOSAL_RECEPTION.md','PROPOSAL_CHECK_NATIVE.json','PROPOSAL_SHAPE_NATIVE.json','PROPOSAL_REPLAY_NATIVE.json','PROPOSAL_READS_NATIVE.json'].map(n=>'docs/papers211_215_sequence/qa/p212_keyed_stdin_observation_root01/'+n)
].map(n=>ROOT+n));
for(const k of result.document_and_private_keys){
 let allowed=exactDocs.has(k.path)||[PRIVATE+'/stdout.raw',PRIVATE+'/stderr.raw'].includes(k.path);
 if(k.path.startsWith(QA)){const rel=k.path.slice(QA.length).split('/');allowed=allowed||(rel.length===2&&packetNames.has(rel[0])&&/^[A-Za-z0-9_.-]+$/.test(rel[1]));}
 ok(allowed,'prior key cannot authorize an arbitrary host path');selected.add(k.path);read(k.path);eq(keys.get(k.path),k,'all 73 closing ten-field keys and whole raw hashes');
}
const ds=fs.lstatSync(PRIVATE,{bigint:true});ok(ds.isDirectory()&&!ds.isSymbolicLink());eq(ds.uid,0n);eq(ds.mode&0o777n,0o700n);eq(meta(ds),result.private_directory_key,'exact private directory final endpoint');
const sourcePath=QA+'p212_keyed_stdin_source_delta01/observe.py';
const source=body.get(sourcePath).toString();const lines=source.split('\n');eq(lines.pop(),'');eq(lines.length,436);
const reads=[...j('READS_NATIVE.json'),...j('READS_MORE_NATIVE.json')];let sourceRenderings=0,sourceRenderedBytes=0,nativeDocumentComparisons=0,nativeDocumentBytes=0;
for(const rec of reads){
 eq(rec.result.exit_code,0,'actual read settlement');
 const cmd=rec.request.cmd;
 const m=/^nl -ba docs\/papers211_215_sequence\/qa\/p212_keyed_stdin_source_delta01\/observe.py \| sed -n '(\d+),(\d+)p'$/.exec(cmd);
 if(m){const first=Number(m[1]),last=Number(m[2]);const expected=lines.slice(first-1,last).map((s,i)=>String(first+i).padStart(6,' ')+'\t'+s+'\n').join('');eq(Buffer.from(rec.result.output),Buffer.from(expected),'complete exact numbered source rendering');sourceRenderings++;sourceRenderedBytes+=Buffer.byteLength(expected);}
 else if(cmd.startsWith('sed -n ')){
  const a=/^sed -n '(\d+),(\d+)p' (docs\/[A-Za-z0-9_./-]+)$/.exec(cmd);ok(a,'finite documentary read command syntax');
  const path=ROOT+a[3];ok(body.has(path),'already pinned read document');const text=body.get(path).toString();const split=text.split('\n');if(split.at(-1)==='')split.pop();
  const expected=split.slice(Number(a[1])-1,Number(a[2])).map(s=>s+'\n').join('');eq(Buffer.from(rec.result.output),Buffer.from(expected),'complete native documentary source rendering');nativeDocumentComparisons++;nativeDocumentBytes+=Buffer.byteLength(expected);
 }
}
eq(sourceRenderings,3);eq(sourceRenderedBytes,source.length+436*7);
for(const p of names.map(n=>D+n))read(p);
const out={schema:'p212-failed-data-artifact-closure-v1',status:'PASS_DOCUMENTARY_ARTIFACT_CLOSURE_ONLY',checks,
 result_stdout_raw_bytes:body.get(D+'RESULT.json').length,result_stdout_sha256:sha(body.get(D+'RESULT.json')),
 source_renderings:sourceRenderings,source_rendered_bytes:sourceRenderedBytes,
 native_document_renderings:nativeDocumentComparisons,native_document_rendered_bytes:nativeDocumentBytes,
 original_keys_unchanged:73,private_raw_originals_unchanged:2,own_preclosure_payloads:names.length,
 keys:[...keys.values()],private_directory_key:meta(ds),extra_observer_invocations:0,host_target_queries:0,
 full_runtime_acceptance:false,root_reception_pending:true};
process.stdout.write(JSON.stringify(out,null,2)+'\n');
