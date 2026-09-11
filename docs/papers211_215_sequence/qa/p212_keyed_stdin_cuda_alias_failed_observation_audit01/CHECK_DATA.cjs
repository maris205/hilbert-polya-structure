'use strict';
// Independent documentary intake. Filesystem operations use only this fixed
// selection and the specifically granted capture directory/two raw files.
// Embedded shell commands, source text, host targets and captured paths are data.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict');
const {parseCanonical}=require('./JSON_LOSSLESS.cjs'),auditTrace=require('./AUDIT_TRACE.cjs');
const ROOT='/root/autodl-tmp/symbolic_dynamics',Q='docs/papers211_215_sequence/qa/';
const A=Q+'p212_keyed_stdin_cuda_alias_failed_observation_audit01/';
const O=Q+'p212_keyed_stdin_cuda_alias_observation_root01/';
const P=Q+'p212_keyed_stdin_cuda_alias_capture_preparation01/';
const R=Q+'p212_keyed_stdin_cuda_alias_request_root01/';
const S=Q+'p212_keyed_stdin_cuda_alias_source_delta01/';
const T=Q+'p212_keyed_stdin_cuda_alias_request_preparation01/';
const sourceReceipt=Q+'p212_keyed_stdin_cuda_alias_source_root01/RECEPTION.md';
const sourceSeal=Q+'p212_keyed_stdin_cuda_alias_source_root01/SHA256SUMS';
const trustReceipt=Q+'p212_trusted_product_boundary_root01/RECEPTION.md';
const C='/root/symbolic-dynamics-p212-cuda-alias-observation-20260910-01';
const groups=[
 {base:O,names:['ARGV.json','ATTEMPT_COMMITTED.json','AUTHORIZATION.json','CLOSING_NATIVE.json','GRANT.json','HANDOFF.md','OBSERVATION_NATIVE.json','PREFLIGHT_NATIVE.json','RAW_INITIAL_NATIVE.json','RAW_INPUTS.sha256','READ_RAW.cjs','REQUEST.json'],seal:'3d3969afc775eec209b0cb99ca94b5bb0369f7fa23092024d3fb590f4814586c'},
 {base:P,names:['BYTE_MATCH_NATIVE.json','CLOSING_NATIVE.json','DECISION.json','PREPARATION_NATIVE.json','RECEIPT.md'],seal:'d81766e628ec983dbb18fa835f035ad1eb9da2cc848922ea5d9e02509d372c67'},
 {base:R,names:['CHECK_NATIVE.json','CHECK_RESULT.json','CHECK_ROOT.cjs','CLOSING_NATIVE.json','RECEPTION.md','REPLAYS_NATIVE.json','ROOT_READS_NATIVE.json','WRAPPER_FAILURE.md'],seal:'bc5d2d512b2c81c444e28c609c1a39f0cf8eea5d3ef0f229b3c7ca09a73cdffc'}
];
const extra=[sourceReceipt,sourceSeal,S+'observe.py',S+'FRONTIER.json',trustReceipt,...['AUTHORIZATION','ARGV','REQUEST'].map(n=>T+n+'.prospective.json')];
const own=['AUDIT_TRACE.cjs','CHECK_DATA.cjs','INITIAL_RAW_NATIVE.json','INITIAL_RAW_RESULT.json','JSON_LOSSLESS.cjs','READ_RAW_LOSSLESS.cjs','READS_NATIVE_01.json','READS_NATIVE_02.json','READS_NATIVE_03.json','SCOPE.md','WRAPPER_FAILURE.md'];
const external=[...groups.flatMap(g=>[...g.names,'SHA256SUMS'].map(n=>g.base+n)),...extra];
const selected=[...external,...own.map(n=>A+n),C+'/stdout.raw',C+'/stderr.raw'];
const allowed=new Set(selected),bodies=new Map(),keys=new Map(),pairs=[],nativeReceipts=[];
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const OLD=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs','birthtimeNs'];
let checks=0,oldKeys=0;
const eq=(a,b,m)=>{checks++;assert.deepStrictEqual(a,b,m);},ok=(a,m)=>{checks++;assert(a,m);};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const meta=s=>Object.fromEntries(F.map(f=>[f,String(s[f])]));
const stable=(a,b)=>eq(Object.fromEntries(F.filter(f=>f!=='atimeNs').map(f=>[f,a[f]])),Object.fromEntries(F.filter(f=>f!=='atimeNs').map(f=>[f,b[f]])),'physical stable fields (atime recorded, not required invariant)');
function read(path) {
  ok(allowed.has(path),'explicit fixed file selection');
  const s=fs.lstatSync(path,{bigint:true});
  ok(s.isFile()&&s.nlink===1n&&s.uid===0n&&s.size>=0n&&s.size<=134217728n);
  if(path.startsWith(C+'/'))eq(s.mode&4095n,384n);
  const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let raw,start,end;
  try {start=meta(fs.fstatSync(fd,{bigint:true}));stable(meta(s),start);raw=fs.readFileSync(fd);end=meta(fs.fstatSync(fd,{bigint:true}));stable(start,end);}
  finally {fs.closeSync(fd);}
  const finish=meta(fs.lstatSync(path,{bigint:true}));stable(end,finish);eq(BigInt(raw.length),s.size);
  return{raw,key:{path,bytes:raw.length,sha256:sha(raw),fields:meta(s),fd_before:start,fd_end:end,path_end:finish,full_eof:true,leaf_links:1}};
}
function body(p){ok(allowed.has(p));return bodies.get(p);}
function json(p){const b=body(p),j=JSON.parse(b.toString('utf8'));eq(b,Buffer.from(JSON.stringify(j,null,2)+'\n','utf8'),'whole canonical documentary JSON');return j;}
function pair(label,a,b){eq(a,b,label);pairs.push({label,bytes:b.length,sha256:sha(b)});}
function normalize(p){return p.startsWith(ROOT+'/')?p.slice(ROOT.length+1):p;}
function oldKey(k) {
  ok(k&&typeof k==='object');eq(Object.keys(k).sort(),['bytes','fields','path','sha256']);
  eq(Object.keys(k.fields),OLD,'actual old ten-field schema, no rdev');
  const p=normalize(k.path);ok(allowed.has(p),'old pin resolves only into explicit selection');
  const current=keys.get(p);eq([current.bytes,current.sha256],[k.bytes,k.sha256]);
  eq(Object.fromEntries(OLD.map(f=>[f,current.fields[f]])),k.fields,'all old metadata fields unchanged');oldKeys++;
}
function settled(record,id,exit=0) {
  ok(record&&record.request&&record.result);eq(record.result.chunk_id,id);eq(record.result.exit_code,exit);
  ok(!record.result.session_id&&typeof record.result.output==='string');ok(!record.result.output.startsWith('Warning: truncated output'));
  nativeReceipts.push({native:id,exit,request:record.request,output_bytes:Buffer.byteLength(record.result.output),
    output_sha256:sha(Buffer.from(record.result.output,'utf8'))});
}
function output(record,id){settled(record,id);return JSON.parse(record.result.output);}
function numbered(raw){const s=raw.toString('utf8');ok(s.endsWith('\n'));return Buffer.from(s.slice(0,-1).split('\n').map((l,i)=>String(i+1).padStart(6,' ')+'\t'+l+'\n').join(''),'utf8');}
const directoryBefore=meta(fs.lstatSync(C,{bigint:true}));
eq(directoryBefore.mode,'16832');eq([directoryBefore.uid,directoryBefore.gid],['0','0']);
const dfd=fs.openSync(C,fs.constants.O_RDONLY|fs.constants.O_DIRECTORY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
let directoryFdStart,directoryFdEnd,directoryEnd;
try {
  directoryFdStart=meta(fs.fstatSync(dfd,{bigint:true}));stable(directoryBefore,directoryFdStart);
  eq(fs.readdirSync(C).sort(),['stderr.raw','stdout.raw']);
  for(const p of selected){const r=read(p);bodies.set(p,r.raw);keys.set(p,r.key);}
  const packages=[];
  for(const g of groups) {
    eq(fs.readdirSync(g.base).sort(),[...g.names,'SHA256SUMS'].sort(),'complete nonself package inventory');
    const manifest=Buffer.from(g.names.map(n=>keys.get(g.base+n).sha256+'  '+n).join('\n')+'\n','ascii');
    pair('entire exact nonself manifest '+g.base,body(g.base+'SHA256SUMS'),manifest);
    eq(sha(manifest),g.seal);
    packages.push({path:g.base,payloads:g.names.length,physical_files:g.names.length+1,
      payload_bytes:g.names.reduce((n,p)=>n+keys.get(g.base+p).bytes,0),seal:g.seal});
  }
  eq([keys.get(S+'observe.py').bytes,keys.get(S+'observe.py').sha256],[22128,'cbacb868df156a422a619531720f0488ea0b1944972b188f2e6246e2cfc62408']);
  eq(keys.get(sourceSeal).sha256,'4c302b5c5eb67892ed846b4cfc33c9aa3d70478bd78fe457a3cea88357ca5def');
  eq(keys.get(O+'GRANT.json').sha256,'131d513b3439fb054a814b7add408f3b34cd849f46bb247453741e38c68070a9');
  eq(keys.get(O+'HANDOFF.md').sha256,'9f163b7c9b6d116ec8ba425f3d520f52f52a6941f8850aeb731d3c1671350984');
  for(const p of selected.filter(p=>p.endsWith('.json')))json(p);
  const auth=json(O+'AUTHORIZATION.json'),argv=json(O+'ARGV.json'),request=json(O+'REQUEST.json'),grant=json(O+'GRANT.json'),commit=json(O+'ATTEMPT_COMMITTED.json');
  for(const n of ['AUTHORIZATION','ARGV','REQUEST'])pair('whole prospective/copy '+n,body(T+n+'.prospective.json'),body(O+n+'.json'));
  eq(Object.keys(auth),['schema','enabled','status','provenance','source_receipt','trust_receipt','frontier']);
  eq([auth.schema,auth.enabled,auth.status],['p212-independent-preprobe-observer-authorization-v1',true,'ROOT_BOUND_FINITE_OBSERVATION_ONLY']);
  eq(argv,['/usr/bin/env','-i','PATH=/usr/bin:/bin','LANG=C.UTF-8','LC_ALL=C.UTF-8','TZ=UTC','SOURCE_DATE_EPOCH=1788825600',
    'FORCE_SOURCE_DATE=1','openin_any=p','openout_any=p','/usr/bin/python3.10','-I','-S','-B',ROOT+'/'+S+'observe.py',body(O+'AUTHORIZATION.json').toString('ascii')]);
  ok(argv.every(s=>!s.includes("'")));
  const expectedCmd="umask 077\nset -C\nexec "+argv.map(s=>"'"+s+"'").join(' ')+" < '"+ROOT+'/'+Q+"p212_keyed_stdin_input01/empty.stdin' > '"+C+"/stdout.raw' 2> '"+C+"/stderr.raw'\n";
  eq(request,{cmd:expectedCmd,workdir:ROOT,shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:2000});
  eq([grant.owner,grant.maximum_invocations,grant.automatic_retries,grant.old_ad435d_grant],['/root',1,0,'CONSUMED_NOT_REUSED']);
  eq(grant.request,{path:O+'REQUEST.json',bytes:2137,sha256:keys.get(O+'REQUEST.json').sha256});
  eq(grant.root_request_reception,{path:R+'RECEPTION.md',bytes:keys.get(R+'RECEPTION.md').bytes,sha256:keys.get(R+'RECEPTION.md').sha256,seal:groups[2].seal});
  eq(grant.separate_preparation.path,P+'RECEIPT.md');eq(grant.separate_preparation.sha256,keys.get(P+'RECEIPT.md').sha256);eq(grant.separate_preparation.seal,groups[1].seal);
  eq(grant.capture.directory,C);eq(grant.capture.stdout,C+'/stdout.raw');eq(grant.capture.stderr,C+'/stderr.raw');
  eq([grant.future_runtime_or_science_accepted,grant.science_build_author_or_refusal_probe,grant.HOLD_EXTERNAL],[false,false,true]);
  eq([commit.status,commit.invocation_budget_consumed,commit.maximum_invocations,commit.prior_new_invocations,commit.automatic_retries,commit.old_grant_reused],
    ['COMMITTED_BEFORE_SINGLE_ACTUAL_SUBMISSION',true,1,0,0,false]);
  eq(commit.exact_request_sha256,keys.get(O+'REQUEST.json').sha256);eq(commit.preflight,{native_chunk:'953486',exit_code:0,checks:247});
  const observation=json(O+'OBSERVATION_NATIVE.json');settled(observation,'a8a5b3',78);eq(observation.request,request);eq(observation.result.output,'');
  const prep=output(json(P+'PREPARATION_NATIVE.json'),'1d7a42'),decision=json(P+'DECISION.json');
  eq([prep.checks,prep.observer_invoked,prep.stdin_or_target_observed,prep.raw_files_created,prep.grant],[13,false,false,false,false]);
  eq(prep.parents.map(p=>p.path),decision.allowed_parents);eq(prep.absent.map(p=>p.path),decision.exact_new_directories);eq(prep.created.map(p=>p.path),decision.exact_new_directories);
  for(const p of prep.parents){eq(BigInt(p.available_bytes),BigInt(p.statfs.bavail)*BigInt(p.statfs.bsize));ok(BigInt(p.available_bytes)>=536870912n);eq(p.fields.uid,'0');ok((BigInt(p.fields.mode)&18n)===0n);}
  for(const p of prep.absent)eq(p.error,{code:'ENOENT',syscall:'lstat',path:p.path});
  for(const p of prep.created){eq(p.inventory,[]);eq(p.fields.mode,'16832');eq(p.fields.uid,'0');}
  const createdCapture=prep.created.find(p=>p.path===C);
  for(const f of ['dev','ino','mode','uid','gid','birthtimeNs'])eq(directoryBefore[f],createdCapture.fields[f],'prepared capture identity retained; contents/times changed by redirections');
  const matching=json(P+'BYTE_MATCH_NATIVE.json'),readCopy=output(matching.source_read,'305b51'),matched=output(matching.byte_match,'780270');
  eq(readCopy.length,3);
  for(const d of readCopy){ok(['AUTHORIZATION','ARGV','REQUEST'].includes(d.name));eq(d.source,T+d.name+'.prospective.json');pair('complete original exact-copy source return '+d.name,Buffer.from(d.body,'utf8'),body(d.source));}
  eq([matched.checks,matched.keys.length,matched.pairs.length,matched.source_or_frontier_modified,matched.observer_invoked,matched.operational_grant],[40,6,3,false,false,false]);
  for(const k of matched.keys)oldKey(k);
  for(const p of matched.pairs){ok(allowed.has(p.source)&&allowed.has(normalize(p.destination)));eq([p.bytes,p.sha256],[keys.get(p.source).bytes,keys.get(p.source).sha256]);pair('historical exact-copy pair '+p.source,body(p.source),body(normalize(p.destination)));}
  const prepClosing=output(json(P+'CLOSING_NATIVE.json'),'2defdf');eq([prepClosing.checks,prepClosing.keys.length,prepClosing.preclosing_payloads,prepClosing.grant],[72,10,4,false]);
  for(const k of prepClosing.keys)oldKey(k);
  pair('preparation historical four-payload manifest',Buffer.from(prepClosing.manifest_before_closing,'ascii'),Buffer.from(groups[1].names.filter(n=>n!=='CLOSING_NATIVE.json').map(n=>keys.get(P+n).sha256+'  '+n).join('\n')+'\n','ascii'));
  const preflight=output(json(O+'PREFLIGHT_NATIVE.json'),'953486');eq([preflight.checks,preflight.keys.length,preflight.observer_invoked,preflight.stdin_separately_observed,preflight.grant_consumed],[247,16,false,false,false]);
  for(const k of preflight.keys)oldKey(k);
  eq(preflight.capture.path,C);eq(preflight.capture.inventory,[]);ok(BigInt(preflight.capture.available_bytes)>=536870912n);eq(preflight.capture.fields,createdCapture.fields);
  const stdout=body(C+'/stdout.raw'),stderr=body(C+'/stderr.raw');
  eq([stdout.length,sha(stdout),stderr.length,sha(stderr)],[7868291,'7b57c2f186676b8bfa7b7473a38a0140b1f1013f93e652c5dc22015602675da3',0,'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855']);
  const parsed=parseCanonical(stdout),v=parsed.value;
  const controlBodies={source_receipt:body(sourceReceipt),trust_receipt:body(trustReceipt),frontier:body(S+'FRONTIER.json')};
  for(const[role,p]of [['source_receipt',sourceReceipt],['trust_receipt',trustReceipt],['frontier',S+'FRONTIER.json']]) {
    eq(auth[role],{path:ROOT+'/'+p,pin:{bytes:keys.get(p).bytes,sha256:keys.get(p).sha256}});
  }
  const trace=auditTrace(v,auth,controlBodies);
  const initialRoot=output(json(O+'RAW_INITIAL_NATIVE.json'),'387087');
  eq(initialRoot.checks,416607);eq(initialRoot.parse,{integers:parsed.counts.integers,unsafe_integer_tokens:parsed.counts.unsafe_integers,objects:parsed.counts.objects,complete_input:true,float_tokens_permitted:false});
  eq(initialRoot.top_level_fields,Object.keys(v));for(const k of initialRoot.keys)oldKey(k);
  eq(initialRoot.capture.path,C);eq(initialRoot.capture.fields,Object.fromEntries(OLD.map(f=>[f,directoryBefore[f]])));
  eq([initialRoot.status,initialRoot.controls,initialRoot.closing_controls,initialRoot.native_events,initialRoot.path_events,initialRoot.actual_read_bytes,initialRoot.actual_captured_bytes],
    [v.status,3,0,trace.native_events,trace.path_events,String(trace.actual_read_bytes),String(trace.actual_captured_bytes)]);
  // Root initial reader renders every numeric token that came from raw JSON as
  // a decimal string; array lengths and its parser counters remain numbers.
  const numericStrings=x=>Array.isArray(x)?x.map(numericStrings):x&&typeof x==='object'?Object.fromEntries(Object.entries(x).map(([k,y])=>[k,numericStrings(y)])):typeof x==='number'?String(x):x;
  eq(initialRoot.errors,numericStrings(v.errors));eq(initialRoot.closure_gaps,v.closure_gaps);eq(initialRoot.independent_runtime_acceptance,false);
  const closing=output(json(O+'CLOSING_NATIVE.json'),'a4f83a');eq([closing.checks,closing.keys.length,closing.preflight_keys,closing.raw_keys,closing.preclosing_payloads,closing.observation_exit,closing.grant_consumed,closing.no_retry,closing.independent_runtime_acceptance],[428,28,16,2,11,78,true,true,false]);
  for(const k of closing.keys)oldKey(k);
  settled(closing.handoff_readback,'fc21cd');pair('whole producer handoff raw readback',Buffer.from(closing.handoff_readback.result.output,'utf8'),body(O+'HANDOFF.md'));
  pair('producer historical eleven-payload manifest',Buffer.from(closing.preclosing_manifest,'ascii'),Buffer.from(groups[0].names.filter(n=>n!=='CLOSING_NATIVE.json').map(n=>keys.get(O+n).sha256+'  '+n).join('\n')+'\n','ascii'));
  pair('whole original raw input digest list',body(O+'RAW_INPUTS.sha256'),Buffer.from(initialRoot.keys.map(k=>k.sha256+'  '+k.path+'\n').join(''),'ascii'));
  const ownInitial=json(A+'INITIAL_RAW_NATIVE.json').record;settled(ownInitial,'03c29e');
  pair('whole independent raw-reader stdout',Buffer.from(ownInitial.result.output,'utf8'),body(A+'INITIAL_RAW_RESULT.json'));
  const ownSummary=json(A+'INITIAL_RAW_RESULT.json');eq(ownSummary.parse_counts,parsed.counts);eq(ownSummary.status,v.status);
  for(const k of ownSummary.raw_keys){const current=keys.get(k.path);eq([current.bytes,current.sha256],[k.bytes,k.sha256]);stable(current.fields,k.path_end);eq(k.full_eof,true);eq(k.leaf_links,1);}
  const reads=[...json(A+'READS_NATIVE_01.json').records,...json(A+'READS_NATIVE_02.json').records,...json(A+'READS_NATIVE_03.json').records];
  eq(reads.map(r=>r.seq),Array.from({length:29},(_,i)=>i+1));
  const readMap=new Map(reads.map(r=>[r.seq,r]));
  for(const seq of [...Array.from({length:12},(_,i)=>i+6),19,20,23,24,25]) {
    const record=readMap.get(seq);eq(record.result.exit_code,0);ok(!record.result.output.startsWith('Warning: truncated output'));
    ok(record.request.cmd.startsWith('nl -ba '));const p=record.request.cmd.slice(7);ok(allowed.has(p));
    pair('whole numbered receiver read '+seq,Buffer.from(record.result.output,'utf8'),numbered(body(p)));
  }
  eq(readMap.get(21).result.chunk_id,'b34432');eq(readMap.get(21).result.exit_code,0);ok(readMap.get(21).result.output.startsWith('Warning: truncated output'));
  eq(readMap.get(22),ownInitial);
  eq(readMap.get(27).result.chunk_id,'a3933f');eq(readMap.get(27).result.exit_code,0);ok(readMap.get(27).result.output.startsWith('Warning: truncated output'));
  eq(readMap.get(28).result.chunk_id,'62dddf');eq(readMap.get(28).result.exit_code,1);ok(readMap.get(28).result.output.includes('TypeError: out.keys.map is not a function'));
  eq(readMap.get(29).result.chunk_id,'37893a');eq(readMap.get(29).result.exit_code,0);
  ok(body(R+'WRAPPER_FAILURE.md').toString('utf8').includes('unavailable, not reconstructed'));
  for(const p of selected){const r=read(p),k=keys.get(p);eq([r.key.bytes,r.key.sha256],[k.bytes,k.sha256]);stable(r.key.fields,k.fields);eq(r.raw,bodies.get(p));}
  directoryFdEnd=meta(fs.fstatSync(dfd,{bigint:true}));directoryEnd=meta(fs.lstatSync(C,{bigint:true}));stable(directoryBefore,directoryFdEnd);stable(directoryFdEnd,directoryEnd);
  eq(fs.readdirSync(C).sort(),['stderr.raw','stdout.raw']);
  const inputs=external.map(p=>keys.get(p).sha256+'  '+p).join('\n')+'\n';
  process.stdout.write(JSON.stringify({
    scope:'PERSONAL_NONCONTRIBUTOR_DATA_ONLY_REVIEW_WITH_SOURCE_AUTHOR_PARENT_DISCLOSED',
    documentary_checks:checks,trace_checks:trace.checks,total_checks:checks+trace.checks,document_keys:keys.size,
    packages,old_complete_keys_received:oldKeys,parse_counts:parsed.counts,canonical_raw_equality:true,
    raw_pairs:pairs.length,raw_paired_bytes:pairs.reduce((n,p)=>n+p.bytes,0),pairs,
    keys:[...keys.values()],directory:{path:C,path_before:directoryBefore,fd_before:directoryFdStart,fd_end:directoryFdEnd,path_end:directoryEnd,members:['stderr.raw','stdout.raw']},
    original_native_receipts:nativeReceipts,trace,external_inputs:external.length,external_digest_list:inputs,
    producer_failed_exit:78,once_grant_consumed:true,source_or_manuscript_acceptance:false,runtime_accepted:false,operational_authorization:false
  },null,2)+'\n');
} finally {fs.closeSync(dfd);}
