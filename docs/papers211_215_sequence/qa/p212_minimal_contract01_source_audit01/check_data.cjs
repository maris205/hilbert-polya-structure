'use strict';
// Independent fixed-workspace DATA checker. No submitted code is loaded,
// parsed as code, evaluated, executed or used to discover a file pathname.
const fs = require('node:fs');
const crypto = require('node:crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = 'docs/papers211_215_sequence/qa/';
const D = QA + 'p212_minimal_contract01_source_preparation01/';
const OWN = QA + 'p212_minimal_contract01_source_audit01/';
const PAYLOADS = ['ARCHIVAL_DISPOSITIONS.json','BINDING.disabled.json','CLOSING_KEYS.json','CLOSING_NATIVE.json','CONTRACT.md','DEPENDENCY_GATE.md','DIRECTORY_REQUEST.disabled.json','DOCUMENTARY_CHECK01.json','DOCUMENTARY_NATIVE.json','FILE_REQUEST.disabled.json','HANDOFF.md','INPUTS.sha256','OBLIGATION_DELTA.md','PRIMARY_SOURCE_EVIDENCE.json','REQUEST.disabled.json','SOURCE_ORIGIN.md','capture.js','file_keys.mjs','receive.mjs'];
const INPUTS = [
  '.agents/skills/symbolic-dynamics-research/SKILL.md',
  'docs/research_state/WORKFLOW.md','docs/papers211_215_sequence/PROBLEM_ANCHOR.md',
  'docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md',
  'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md',
  QA+'p212_runtime_obligation_diagnosis01/REPORT.md',
  QA+'p212_runtime_obligation_diagnosis01/INPUTS.sha256',
  QA+'p212_s0_source_commission_root01/DECISION.md',
  ...['SOURCE_CONTRACT.md','RUNTIME_PREPARATION.md','FRONTIER_REASONING.md','product_capture.js','driver.js','outer_contract.py','node_preload.js','companions/CAPTURE_CONTRACT.json'].map(n=>QA+'p212_keyed_stdin_source_delta01/'+n),
  QA+'p212_keyed_stdin_cuda_alias_source_delta01/FRONTIER.json',
  QA+'p212_keyed_stdin_cuda_alias_source_delta01/CONTRACT.md',
  QA+'p212_dependency_query_driver_preparation01/STAGED_CAPTURE_AND_CLOSURE.md',
  QA+'p212_dependency_source_root01/RECEPTION.md',
  QA+'p212_build_dependency_source_preparation01/PLAN.md',
  QA+'p212_build_dependency_source_preparation01/SELECTOR_OBLIGATIONS.json',
  QA+'p212_initial_build_preparation01/PLAN.md',
  QA+'p213_minimal_observer_source_delta01/CONTRACT.md',
  QA+'p212_trusted_product_boundary_root01/RECEPTION.md',
  QA+'p212_keyed_stdin_source_root01/RECEPTION.md',
  QA+'p212_author_pair_runtime_reception01/RECEPTION.md'
];
const EXTRA = [QA+'p212_trusted_product_boundary_root01/DECISION.json',OWN+'check_data.cjs',OWN+'ORIGIN.md'];
const F = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
let checks=0;
const need=(v,m)=>{checks++;if(!v)throw new Error(m);};
const same=(a,b,m)=>need(JSON.stringify(a)===JSON.stringify(b),m);
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const pin=b=>({bytes:b.length,sha256:hash(b)});
const rawMap=new Map(), keyMap=new Map();
const allowed=new Set([...INPUTS,...PAYLOADS.map(n=>D+n),D+'SHA256SUMS',...EXTRA]);
const fields=s=>Object.fromEntries(F.map(k=>{need(typeof s[k]==='bigint','native documentary integer '+k);return[k,s[k].toString()];}));
function read(p) {
  need(allowed.has(p),'fixed documentary whitelist only: '+p);
  if(rawMap.has(p))return rawMap.get(p);
  const full=ROOT+'/'+p, a=fs.lstatSync(full,{bigint:true});
  need(a.isFile()&&!a.isSymbolicLink(),'document physical regular leaf');
  const A=fields(a),fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let row,bytes;
  try {
    const b=fs.fstatSync(fd,{bigint:true}),B=fields(b);need(b.isFile(),'regular same-fd document');same(B,A,'lstat/fstat BEFORE any byte');
    const chunks=[],buffer=Buffer.alloc(65536);let total=0,count,readCalls=0;
    do {count=fs.readSync(fd,buffer,0,buffer.length,null);readCalls++;need(count>=0&&count<=buffer.length,'actual bounded read count');
      if(count){total+=count;need(total<=8388608,'fixed 8 MiB documentary ceiling');chunks.push(Buffer.from(buffer.subarray(0,count)));}
    } while(count!==0);
    bytes=Buffer.concat(chunks);const Z=fields(fs.fstatSync(fd,{bigint:true})),L=fields(fs.lstatSync(full,{bigint:true}));
    same(Z,B,'same fd after true zero-return EOF');same(L,A,'lexical endpoint after complete EOF');
    need(BigInt(total)===b.size&&bytes.length===total,'entire raw count equals original descriptor size');
    row={path:p,...pin(bytes),lstat_before:A,fstat_before:B,fstat_after:Z,lstat_after:L,fd,read_calls:readCalls,last_read_return:count,eof:count===0,close_succeeded:false};
  } finally {fs.closeSync(fd);}
  row.close_succeeded=true;rawMap.set(p,bytes);keyMap.set(p,row);return bytes;
}
const json=p=>{const b=read(p),s=b.toString('utf8'),v=JSON.parse(s);need(Buffer.from(s).equals(b)&&Buffer.from(JSON.stringify(v,null,2)+'\n').equals(b),'canonical complete JSON DATA '+p);return v;};
const j=n=>json(D+n), doc=n=>read(D+n);
const manifest=doc('SHA256SUMS');same(pin(manifest),{bytes:1630,sha256:'523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40'},'exact commissioned package seal');
need(manifest.toString().endsWith('\n'),'manifest final LF');
const entries=manifest.toString().slice(0,-1).split('\n').map(line=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);need(m,'strict flat manifest row');return {sha256:m[1],name:m[2]};});
same(entries.map(r=>r.name),PAYLOADS,'all nineteen exact sorted payload roles');
same(fs.readdirSync(ROOT+'/'+D).sort(),[...PAYLOADS,'SHA256SUMS'].sort(),'exact twenty physical entries, no omissions');
let physical=manifest.length;for(const e of entries){const b=doc(e.name);need(hash(b)===e.sha256,'entire payload pin '+e.name);physical+=b.length;}
need(physical===1322853,'exact commissioned physical bytes');
need(hash(doc('CLOSING_NATIVE.json'))==='2a28cb9ce721c2ce496d06dc0f4e2f0b6181e0c1becbf0be04e985c45fa96853','exact closing native pin');
need(hash(doc('CLOSING_KEYS.json'))==='ec12e41a690ee44b4a5a1dcae3d3a59ba630e3dc2b09d2fb04cace2f93c71a95','exact closing key pin');
const inputLines=doc('INPUTS.sha256').toString().trimEnd().split('\n'),inputRows=inputLines.map(l=>{const m=/^([a-f0-9]{64})  (.+)$/.exec(l);need(m,'strict input pin row');return{sha256:m[1],path:m[2]};});
same(inputRows.map(r=>r.path),INPUTS,'all twenty-seven whole input paths independently enumerated');
for(const r of inputRows)need(hash(read(r.path))===r.sha256,'unchanged complete original '+r.path);
for(const p of EXTRA)read(p);
const diagnosis=read(QA+'p212_runtime_obligation_diagnosis01/INPUTS.sha256').toString().trimEnd().split('\n').map(l=>{const m=/^([a-f0-9]{64})  (.+)$/.exec(l);need(m,'diagnosis pin line is DATA');return{sha256:m[1],path:m[2]};});
const shared=diagnosis.filter(r=>INPUTS.includes(r.path));need(shared.length===19,'nineteen shared documentary inputs');for(const r of shared)need(hash(read(r.path))===r.sha256,'shared unchanged hash');
const archive=j('ARCHIVAL_DISPOSITIONS.json'),frontier=json(QA+'p212_keyed_stdin_cuda_alias_source_delta01/FRONTIER.json');
same(archive.frontier,{path:QA+'p212_keyed_stdin_cuda_alias_source_delta01/FRONTIER.json',...pin(read(QA+'p212_keyed_stdin_cuda_alias_source_delta01/FRONTIER.json'))},'whole archival frontier pin');
same(archive.original_counts,{targets:164,components:207,memberships:5,membership_names:292,closure_gaps:8},'complete original census');
need(frontier.targets.length===164&&frontier.allowed_components.length===207&&frontier.closure_gaps.length===8,'whole target/component/gap census');
const memberships=frontier.targets.filter(r=>r.mode==='membership');need(memberships.length===5&&memberships.reduce((n,r)=>n+r.expected_names.length,0)===292,'all unchanged membership names');
need(archive.classes.length===11&&archive.rows.length===164,'exact disposition classes and rows');
const classified=new Map();for(const c of archive.classes){need(typeof c.reason==='string'&&c.reason.length>80&&typeof c.gate==='string','nonempty actual class rationale and gate');for(const id of c.rows){need(Number.isInteger(id)&&id>=1&&id<=164&&!classified.has(id),'exactly-once class membership');classified.set(id,c.id);}}
need(classified.size===164,'complete class partition');
archive.rows.forEach((r,i)=>{same(Object.keys(r).sort(),['class','id','original_complete_row_value','path'],'exact disposition row fields');need(r.id===i+1&&r.path===frontier.targets[i].path&&r.class===classified.get(i+1),'row id/path/class against original');same(r.original_complete_row_value,pin(Buffer.from(JSON.stringify(frontier.targets[i]))),'entire original row value pin');});
for(const id of [24,25,156,157,158,159])need(archive.classes.find(c=>c.id===classified.get(id)).gate.includes('B2'),'CUDA candidate retains loader blocker');
const binding=j('BINDING.disabled.json'),request=j('REQUEST.disabled.json'),files=j('FILE_REQUEST.disabled.json'),dirs=j('DIRECTORY_REQUEST.disabled.json');
for(const x of [binding,request,files,dirs])need(x.enabled===false&&x.status.startsWith('HOLD_SOURCE_ONLY'),'all exact disabled records');
need(request.source_enabled===false&&request.automatic_next_call===false&&request.lookup_body_build_science_permission===false,'no source/next-phase activation');
for(const k of ['input_permissions','directory_identity','owned_uid','option_acceptance'])need(binding[k]===null,'actual future input role remains null');
same(binding.receipts,{source:null,policy:null,tool_closure:null},'no invented semantic receipt');
const env={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'};
same(binding.environment,env,'exact eight child variables');same(binding.provenance,request.provenance,'matching narrower provenance');
same(binding.later_authority,{lookup:false,bodies:false,build:false,science:false,review:false,external:'HOLD_EXTERNAL'},'later gates all held');
const absQA=ROOT+'/'+QA.slice(0,-1),cwd=absQA+'/p212_build_dependency_query01/query_cwd',raw=absQA+'/p212_minimal_contract01_raw01',stdin=absQA+'/p212_keyed_stdin_input01/empty.stdin';
const quote=s=>"'"+s+"'";const vectors=[['/usr/bin/kpsewhich','--help'],['/usr/bin/kpsewhich','--version']];same(binding.tool_argv,vectors,'only original S0 vectors');
for(const [i,call] of ['help','version'].entries()){
  const cmd='umask 077 || exit 78\nset -o noclobber || exit 78\nexec < '+quote(stdin)+' > '+quote(raw+'/'+call+'01/stdout.raw')+' 2> '+quote(raw+'/'+call+'01/stderr.raw')+' || exit 78\nexec '+['/usr/bin/env','-i',...Object.entries(env).map(([k,v])=>k+'='+v),...vectors[i]].map(quote).join(' ');
  const expected={cmd,workdir:cwd,shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:4000};
  same(binding.prepared_requests[i],expected,'entire binding request reconstructed independently');same(request.prepared_calls[i].request,expected,'entire request template matches');need(request.prepared_calls[i].call===call,'ordered help then version');
  for(const [k,v] of Object.entries(request.prepared_calls[i]))if(!['call','request'].includes(k))need(v===null,'no fabricated future evidence '+k);
}
same(dirs.paths,[cwd,raw,raw+'/help01',raw+'/version01'],'exact directory spellings as DATA only');need(dirs.permission_receipt===null,'no directory permission');
same(files.entries.map(r=>[r.id,r.path,r.role,r.optional,r.max_bytes]),[
 ['BASH','/bin/bash','executable',false,16777216],['ENV','/usr/bin/env','executable',false,16777216],['KPSEWHICH','/usr/bin/kpsewhich','executable',false,16777216],
 ['LOADER_CANDIDATE','/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2','loader',false,16777216],['LIBC_CANDIDATE','/usr/lib/x86_64-linux-gnu/libc.so.6','loader',false,16777216],['TINFO_CANDIDATE','/usr/lib/x86_64-linux-gnu/libtinfo.so.6.3','loader',false,16777216],['LOADER_CACHE','/etc/ld.so.cache','configuration',true,1048576],['SYSTEM_PRELOAD','/etc/ld.so.preload','configuration',true,1048576]],'eight exact bounded initial candidate roles');
need(files.entries.every(r=>r.expected===null&&r.capture_hex===true)&&files.total_byte_limit===102760448&&files.permission_receipt===null&&files.settlement_receipt===null,'no candidate runtime key or grant');
const sourceRoles={capture:'capture.js',file_keys:'file_keys.mjs',receiver:'receive.mjs'},sourceLines={capture:117,file_keys:189,receiver:271},sourcePins={capture:'c0369d9c6d0b623f59620884ef7b6252c9d99c98ff38a73168d0eba9733b8063',file_keys:'448b7a0c17ddc708fd14a9adb15beef5b5eb8b5081fd7480045b00c80973b896',receiver:'adc0570ff23bece682812c77e69a2e8e7e9e1bcc64cba87c970e97f390202421'};
let lines=0,sourceBytes=0;for(const [role,name] of Object.entries(sourceRoles)){const b=doc(name),n=b.toString().split('\n').length-1;need(n===sourceLines[role]&&hash(b)===sourcePins[role],'entire submitted source line/hash identity');same(binding.sources[role],{path:ROOT+'/'+D+name,pin:pin(b)},'only actual disabled source pins filled');need((b.toString().match(/const SOURCE_ENABLED = false;/g)||[]).length===(role==='file_keys'?2:1),'four unconditional source guards as TEXT only');lines+=n;sourceBytes+=b.length;}
need(lines===577&&sourceBytes===48570,'whole new source census');
const gate=doc('DEPENDENCY_GATE.md').toString();for(const s of ['32 distinct ELF image nodes','96\n   named file states','64 initialization/finalization entries','B1','B2','B3','B4','B5','B6'])need(gate.includes(s),'finite gate anchor '+s);
const first=j('DOCUMENTARY_CHECK01.json'),closing=j('CLOSING_KEYS.json'),native=j('DOCUMENTARY_NATIVE.json'),closeNative=j('CLOSING_NATIVE.json');
need(first.checks===2417&&first.rows.length===39&&closing.checks===2192&&closing.keys.length===44,'author original documentary censuses');
need(native.cutoff_sequence===59&&native.records.length===59,'selected actual native cutoff');native.records.forEach((r,i)=>{need(r.seq===i+1,'unbroken selected native record sequence');need(['exec_command','apply_patch'].includes(r.tool)&&r.request!==undefined&&r.result!==undefined,'actual named native record roles');});
const actualFirst=native.records.filter(r=>r.result?.chunk_id==='b5bb72');need(actualFirst.length===1&&actualFirst[0].result.exit_code===0,'actual first documentary native completion');
const rawPairs=[];function rawPair(label,a,b){need(a.equals(b),'whole actual original stdout equals separately retained result '+label);rawPairs.push({label,...pin(a)});}
rawPair('author_first_native_stdout',Buffer.from(actualFirst[0].result.output),doc('DOCUMENTARY_CHECK01.json'));
need(closeNative.actual_return.chunk_id==='1be80e'&&closeNative.actual_return.exit_code===0,'actual author closing native completion');rawPair('author_closing_native_stdout',Buffer.from(closeNative.actual_return.output),doc('CLOSING_KEYS.json'));
let historicalKeys=0;const normalize=p=>p.startsWith(ROOT+'/')?p.slice(ROOT.length+1):p;
for(const [kind,rows] of [['first',first.rows],['closing',closing.keys]])for(const r of rows){const p=normalize(r.path);need(allowed.has(p),'historical key path already in independent whitelist');
  for(const name of ['lstat_before','fstat_before','fstat_after','lstat_after']){same(Object.keys(r[name]),F,'every old ten-field key');for(const value of Object.values(r[name]))need(typeof value==='string'&&/^-?(0|[1-9][0-9]*)$/.test(value)&&value!=='-0','every historical exact integer');same(r[name],r.lstat_before,'historical same-fd/lexical agreement');}
  need(r.close_succeeded===true&&Number.isSafeInteger(r.fd)&&r.fd>=0,'historical complete close/fd');
  if(kind==='closing')need(r.eof===true&&r.last_read_return===0&&Number.isSafeInteger(r.read_calls)&&r.read_calls>=2,'closing true zero-return EOF');else need(r.whole_eof===true,'first API whole-file claim preserved, not invented read-return');
  if(kind==='first'&&p===D+'BINDING.disabled.json'){
    const old=JSON.parse(JSON.stringify(binding));for(const v of Object.values(old.sources))v.pin=null;const original=Buffer.from(JSON.stringify(old,null,2)+'\n');same(pin(original),{bytes:r.bytes,sha256:r.sha256},'only declared three source pins changed since initial check');need(String(original.length)===r.lstat_before.size,'historical original binding size');
  }else{same(pin(read(p)),{bytes:r.bytes,sha256:r.sha256},'complete historical bytes remain unchanged');same(keyMap.get(p).lstat_before,r.lstat_before,'entire historical ten-field key unchanged');}
  historicalKeys++;
}
need(historicalKeys===83,'all 39 plus 44 historical full keys');
const primary=j('PRIMARY_SOURCE_EVIDENCE.json');need(primary.requests.length===3,'all three author primary-source original requests');for(const r of primary.requests)need(r.request&&typeof r.actual_return==='string'&&r.actual_return.length>0,'retain original source returns including failures');
const stage=json(QA+'p212_build_dependency_source_preparation01/SELECTOR_OBLIGATIONS.json');same(stage.stages.map(r=>r.id),['S0_QUERY_RUNTIME_AND_OPTIONS','S1_DIRECT_BODIES','S2_CLASS_AND_ORDERED_PACKAGE_GRAPH','S3_T1_AND_MATH_FONT_GRAPH','S4_FORMAT_AND_CONFIG_GRAPH','S5_NATIVE_AND_RENDER_TOOL_GRAPH','S6_FRESH_LOCK_AND_ACTUAL_BUILD_CWD'],'all unchanged later stage roles');
console.log(JSON.stringify({schema:'p212-independent-s0-source-documentary-audit-v1',status:'PASS_FIXED_DOCUMENTARY_DATA_ONLY_NOT_OPERATIONAL',checks,package_payloads:19,package_files:20,package_physical_bytes:physical,package_seal:pin(manifest),input_pins:27,extra_documentary_inputs:3,whole_file_keys:keyMap.size,historical_key_occurrences:historicalKeys,shared_diagnosis_pins:shared.length,source_files:3,source_lines:lines,source_bytes:sourceBytes,archival_rows:164,archival_classes:archive.classes.map(c=>({id:c.id,rows:c.rows.length,gate:c.gate})),raw_pairs:rawPairs,actual_submitted_source_execution:false,embedded_host_path_reads:false,operational_grant:false,keys:[...keyMap.values()],limits:'Independent current same-fd explicit-EOF ten-field DOCUMENT checks under ordinary trusted Node. No submitted sources imported/evaluated/syntax/AST tested. Historical first whole_eof is an API-read claim, not a retained zero-return event. Original stdout byte equality is checked, not author checker execution. Semantic source verdict is a separate human-readable REPORT.'},null,2));
