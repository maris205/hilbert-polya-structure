'use strict';
// Independent documentary audit only. No reviewed program is loaded, parsed as
// language source, imported or run. Native children are three explicit diff calls.
const fs = require('fs'), crypto = require('crypto'), assert = require('assert/strict');
const cp = require('child_process');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = 'docs/papers211_215_sequence/qa';
const OLD = QA + '/p212_keyed_stdin_source_delta01';
const NEW = QA + '/p212_keyed_stdin_cuda_alias_source_delta01';
const SELF = QA + '/p212_keyed_stdin_cuda_alias_source_audit01';
const GROUPS = {
  p212_keyed_stdin_cuda_alias_decision01: ['DECISION.md','FRONTIER_DOCUMENT_SELECTION_NATIVE.json','SHA256SUMS'],
  p212_keyed_stdin_failed_observation_root01: ['RECEPTION.md','SHA256SUMS'],
  p212_keyed_stdin_linecount_erratum01: ['ERRATUM.md','SHA256SUMS'],
  p212_keyed_stdin_nonlineage_audit01: ['FINDINGS.json','HANDOFF.md','REPORT.md','SHA256SUMS'],
  p212_keyed_stdin_source_delta01: ['AUTHORIZATION.disabled.json','FRONTIER.json','FRONTIER_REASONING.md','HANDOFF.md','SHA256SUMS','SOURCE_CONTRACT.md','driver.js','node_preload.js','node_runtime_probe.js','observe.py','outer_contract.py','product_capture.js','python_runtime_probe.py'],
  p212_keyed_stdin_source_root01: ['RECEPTION.md','SHA256SUMS']
};
const INPUTS = Object.entries(GROUPS).flatMap(([d,ns])=>ns.map(n=>QA+'/'+d+'/'+n)).sort();
const NEW_NAMES = ['AUTHORIZATION.disabled.json','CHECK_DOCUMENTS.cjs','CHECK_NATIVE.json','CHECK_RESULT.json','CLOSING_NATIVE.json','CONTRACT.md','DELTA.md','DIFF_NATIVE.json','EVIDENCE.md','FRONTIER.json','HANDOFF.md','INPUTS.sha256','INPUT_KEYS_NATIVE.json','ORIGINAL_READS_NATIVE.json','OWN_READS_NATIVE.json','PREPARATION_NATIVE.json','REQUEST.disabled.json','diffs/AUTHORIZATION.disabled.json.diff','diffs/FRONTIER.json.diff','diffs/observe.py.diff','observe.py'];
const EXTRA = [QA+'/p212_keyed_stdin_nonlineage_audit01/READ_SCOPE.md',
  ...['DECISION.json','RECEPTION.md','SHA256SUMS'].map(n=>QA+'/p212_trusted_product_boundary_root01/'+n)];
const OWN_NAMES = ['AUTHOR_REPLAY_NATIVE.json','AUTHOR_REPLAY_RESULT.json','CHECK_SOURCE_DELTA.cjs','EXTRA_READS_NATIVE.json','PREPARATION_NATIVE.json','READS_NATIVE.json'];
const ALLOWED = new Set([...INPUTS,...NEW_NAMES.map(n=>NEW+'/'+n),NEW+'/SHA256SUMS',...EXTRA,...OWN_NAMES.map(n=>SELF+'/'+n)]);
const FIELDS = ['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs','birthtimeNs'];
let checks=0;
function ok(v,m){checks++;assert(v,m);}
function eq(a,b,m){checks++;assert.deepStrictEqual(a,b,m);}
function wholeValue(a,b,m){
  eq(a===null,b===null,m+' null');eq(typeof a,typeof b,m+' type');
  if(a===null||typeof a!=='object'){eq(a,b,m);return;}
  eq(Array.isArray(a),Array.isArray(b),m+' array');eq(Object.keys(a).sort(),Object.keys(b).sort(),m+' exact keys');
  for(const k of Object.keys(a))wholeValue(a[k],b[k],m+'.'+k);
}
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const pin=b=>({bytes:b.length,sha256:hash(b)});
const fields=s=>Object.fromEntries(FIELDS.map(k=>[k,String(s[k])]));
const cache=new Map();
function whole(p){
  ok(ALLOWED.has(p),'explicit document selection before filesystem access: '+p);
  const l=fs.lstatSync(ROOT+'/'+p,{bigint:true});
  ok(l.isFile()&&!l.isSymbolicLink()&&l.nlink===1n,'physical single-link document');
  const fd=fs.openSync(ROOT+'/'+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try{
    const s=fs.fstatSync(fd,{bigint:true});eq(fields(s),fields(l),'lexical same fd');
    const raw=fs.readFileSync(fd);eq(fields(fs.fstatSync(fd,{bigint:true})),fields(s),'same fd after whole read');
    eq(fields(fs.lstatSync(ROOT+'/'+p,{bigint:true})),fields(s),'lexical unchanged after read');
    eq(BigInt(raw.length),s.size,'whole byte count');
    return {raw,key:{path:p,...pin(raw),lf_lines:raw.reduce((n,b)=>n+(b===10),0),fields:fields(s)}};
  }finally{fs.closeSync(fd);}
}
function read(p){if(!cache.has(p))cache.set(p,whole(p));return cache.get(p).raw;}
function text(p){const b=read(p),s=b.toString('utf8');eq(Buffer.from(s),b,'lossless UTF-8 document');return s;}
function json(p){return JSON.parse(text(p));}
function own(n){return read(SELF+'/'+n);}
function canon(v){return Buffer.from(JSON.stringify(v,null,2)+'\n');}
function canonical(p){const v=json(p);eq(canon(v),read(p),'complete canonical JSON document');return v;}
function inventory(){
  const found=[];
  for(const d of [NEW,NEW+'/diffs']){
    const s=fs.lstatSync(ROOT+'/'+d);ok(s.isDirectory()&&!s.isSymbolicLink(),'two exact physical source directories');
    for(const n of fs.readdirSync(ROOT+'/'+d)){
      if(d===NEW&&n==='diffs')continue;
      found.push((d===NEW?'':'diffs/')+n);
    }
  }
  eq(found.sort(),[...NEW_NAMES,'SHA256SUMS'].sort(),'entire final source packet physical membership');
}
inventory();
for(const p of [...ALLOWED].sort())read(p);
function manifest(p,count,digest){
  const raw=read(p);if(digest)eq(hash(raw),digest,'fixed manifest bytes');
  const rows=text(p).split('\n');eq(rows.pop(),'','exact final LF');eq(rows.length,count,'manifest row count');
  const entries=new Map();
  for(const r of rows){
    const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.\/-]+)$/.exec(r);ok(m,'strict bare-relative manifest grammar');
    ok(!m[2].startsWith('/')&&m[2]!=='SHA256SUMS'&&!m[2].split('/').some(x=>x===''||x==='.'||x==='..'),'nonself finite manifest path');
    ok(!entries.has(m[2]),'manifest unique paths');entries.set(m[2],m[1]);
  }
  return entries;
}
const newSeal='32c3c6da8cc47ef0adf96723a98ec8244ae004990582effdca407a49537aa10d';
const nm=manifest(NEW+'/SHA256SUMS',21,newSeal);
eq([...nm.keys()],[...NEW_NAMES],'complete ordered new payload names');
for(const [n,h] of nm)eq(hash(read(NEW+'/'+n)),h,'all complete new payloads');
const SEALED=[
 ['p212_keyed_stdin_source_delta01',55,'f076522fc7e120c46be0c57b60168784c38c32339e07f65b74e0012694ca1ee8'],
 ['p212_keyed_stdin_source_root01',16,'0f65f815ca28d4153bc968b0d8dd041f3571287ebe639c942abce6064bb32380'],
 ['p212_keyed_stdin_nonlineage_audit01',24,'ff622be9502a7bd931820cf1c22b5e858bc09243ef3e0488fe7d65cfbea71887'],
 ['p212_keyed_stdin_linecount_erratum01',7,'7876c67cf7a4f436e746bf7ac282868dce74aa7c5ef31063725af815371c4007'],
 ['p212_keyed_stdin_failed_observation_root01',10,'0c99b21b1e0401bc771abb0561e5969f8bb6fc7925ddb0ce0d36a32ccf4f16be'],
 ['p212_keyed_stdin_cuda_alias_decision01',2,'c1c05f3714d9b1a803091bd6e76c0676d2657396452da2bf523493bd312eff69']
];
for(const [d,n,h] of SEALED){
  const base=QA+'/'+d, m=manifest(base+'/SHA256SUMS',n,h);
  for(const p of [...INPUTS,...EXTRA].filter(p=>p.startsWith(base+'/')&&!p.endsWith('/SHA256SUMS')))
    eq(hash(read(p)),m.get(p.slice(base.length+1)),'selected historical payload seal');
}
// The old trust packet is selected only at its complete manifest and two controls.
const trustBase=QA+'/p212_trusted_product_boundary_root01';
const trustRows=text(trustBase+'/SHA256SUMS').split('\n');eq(trustRows.pop(),'','trust manifest LF');
const tm=manifest(trustBase+'/SHA256SUMS',trustRows.length);
for(const n of ['DECISION.json','RECEPTION.md'])eq(hash(read(trustBase+'/'+n)),tm.get(n),'old trust selected bytes');
const initialNative=json(NEW+'/INPUT_KEYS_NATIVE.json');eq(initialNative.result.exit_code,0,'actual author initial key exit');
const initial=JSON.parse(initialNative.result.output);eq(initial.fields,FIELDS,'all ten ordinary document fields');
eq(initial.records.map(k=>k.path),INPUTS,'all 26 original input keys');
eq(read(NEW+'/INPUTS.sha256'),Buffer.from(initial.records.map(k=>k.sha256+'  '+k.path).join('\n')+'\n'),'exact whole input manifest');
for(const k of initial.records)wholeValue(cache.get(k.path).key,k,'initial whole key');
const replayNative=json(SELF+'/AUTHOR_REPLAY_NATIVE.json'),authorNative=json(NEW+'/CHECK_NATIVE.json');
eq(replayNative.result.exit_code,0,'fresh actual author document-check replay');eq(authorNative.run.result.exit_code,0,'original author document-check exit');
eq(replayNative.request.cmd,'node '+NEW+'/CHECK_DOCUMENTS.cjs','only inspected documentary checker replayed');
eq(authorNative.run.request.cmd,replayNative.request.cmd,'same exact checker');
eq(Buffer.from(replayNative.result.output),read(NEW+'/CHECK_RESULT.json'),'fresh replay raw-equal to author result');
eq(Buffer.from(authorNative.run.result.output),read(NEW+'/CHECK_RESULT.json'),'author result raw-equal to actual native stdout');
eq(own('AUTHOR_REPLAY_RESULT.json'),read(NEW+'/CHECK_RESULT.json'),'own complete result attachment raw-equal');
eq(authorNative.checker_read.result.exit_code,0,'author checker source read settled');
eq(Buffer.from(authorNative.checker_read.result.output),read(NEW+'/CHECK_DOCUMENTS.cjs'),'entire actual checker source rendering');
const ar=canonical(NEW+'/CHECK_RESULT.json');eq(ar.checks,17454,'actual author/replay check total');eq(ar.keys.length,42,'all author original keys');
for(const k of ar.keys){ok(cache.has(k.path),'author key is selected before following');wholeValue(cache.get(k.path).key,k,'author full original key');}
const closingNative=json(NEW+'/CLOSING_NATIVE.json');eq(closingNative.result.exit_code,0,'actual original author closure exit');
const closing=JSON.parse(closingNative.result.output);
eq(closing.checks,734,'original author closure assertion count');eq(closing.keys.length,46,'complete author historical closing keys');
eq(closing.physical_names,NEW_NAMES.filter(n=>n!=='CLOSING_NATIVE.json'),'exact preclosing layout kept as history');
eq(closing.preclosing_payloads,20,'historical preclosing payload count');
eq(closing.whole_document_keys,46,'historical whole key count');
eq(closing.check_stdout_bytes,read(NEW+'/CHECK_RESULT.json').length,'full historical stdout bytes');
eq(closing.check_stdout_sha256,hash(read(NEW+'/CHECK_RESULT.json')),'full historical stdout digest');
for(const k of closing.keys){ok(cache.has(k.path),'historical closing key is explicitly selected');wholeValue(cache.get(k.path).key,k,'full unchanged closing key');}
// Do not replay the old preseal inventory checker against the now sealed layout.
let authorReadCount=0,authorReadBytes=0;
for(const [p,list] of [[NEW+'/ORIGINAL_READS_NATIVE.json','reads'],[NEW+'/OWN_READS_NATIVE.json','reads'],[NEW+'/CLOSING_NATIVE.json','reads']]){
  for(const r of json(p)[list]){
    ok(ALLOWED.has(r.path),'literal selected source/prose read');eq(r.result.exit_code,0,'actual author read exit');
    eq(Buffer.from(r.result.output),read(r.path),'whole author read raw equality');authorReadCount++;authorReadBytes+=Buffer.byteLength(r.result.output);
  }
}
const oldSource=text(OLD+'/observe.py'),newSource=text(NEW+'/observe.py');
const aLines=oldSource.split('\n'),bLines=newSource.split('\n');eq(aLines.length,437,'old 436 LF lines');eq(bLines.length,437,'new 436 LF lines');
const lineDeltas=[];for(let i=0;i<aLines.length;i++)if(aLines[i]!==bLines[i])lineDeltas.push({line:i+1,old:aLines[i],new:bLines[i]});
eq(lineDeltas,[
 {line:17,old:"HERE = QA + '/p212_keyed_stdin_source_delta01'",new:"HERE = QA + '/p212_keyed_stdin_cuda_alias_source_delta01'"},
 {line:19,old:"SOURCE_RECEIPT = QA + '/p212_keyed_stdin_source_root01/RECEPTION.md'",new:"SOURCE_RECEIPT = QA + '/p212_keyed_stdin_cuda_alias_source_root01/RECEPTION.md'"}
],'entire source only two exact line replacements');
const rest=ls=>Buffer.from(ls.filter((_,i)=>i!==16&&i!==18).join('\n'));
eq(rest(aLines),rest(bLines),'entire protected observer bytes, imports and all branches');
eq(rest(bLines).length,21990,'protected byte length');eq(hash(rest(bLines)),'d938de449739513fa09278eb98bbcd2bca1f5ba5d35c40b332a90b72486440e9','protected complete digest');
const oldF=canonical(OLD+'/FRONTIER.json'),newF=canonical(NEW+'/FRONTIER.json');
eq(Object.keys(newF),Object.keys(oldF),'no hidden frontier field');
const additions=['/etc/alternatives','/etc/alternatives/cuda','/etc/alternatives/cuda-12'];
for(const k of Object.keys(oldF).filter(k=>k!=='allowed_components'))wholeValue(newF[k],oldF[k],'complete untouched frontier member '+k);
eq(oldF.allowed_components.length,204,'old permission count');eq(newF.allowed_components.length,207,'new permission count');
eq(newF.allowed_components,[...new Set([...oldF.allowed_components,...additions])].sort(),'only exact sorted component union');
eq(newF.allowed_components.filter(p=>!oldF.allowed_components.includes(p)),additions,'only three additions');
eq(oldF.allowed_components.filter(p=>!newF.allowed_components.includes(p)),[],'zero removed components');
eq(newF.targets.length,164,'complete target count');eq(newF.closure_gaps.length,8,'eight unaltered gaps');
const members=newF.targets.filter(t=>t.mode==='membership');eq(members.length,5,'five full memberships');eq(members.reduce((n,t)=>n+t.expected_names.length,0),292,'292 complete names');
const modes={};for(const t of newF.targets)modes[t.mode]=(modes[t.mode]||0)+1;
eq(modes,{metadata:5,file:110,optional_file:32,membership:5,optional_directory:11,absent:1},'all modes retained');
for(const p of additions)ok(!newF.targets.some(t=>t.path===p),'no added content/metadata/membership target');
for(const p of newF.allowed_components){
  ok(p==='/'||/^\/[^/]+(?:\/[^/]+)*$/.test(p),'canonical documentary components');
  ok(!p.split('/').some(x=>x==='.'||x==='..')&&!/[\x00*?\[\]{}]/.test(p),'no wildcard/dot mechanism');
  let s='';for(const c of p.slice(1).split('/').filter(Boolean)){s+='/'+c;ok(newF.allowed_components.includes(s),'finite ancestor closure as data only');}
}
eq(newF.targets.filter(t=>t.path.startsWith(ROOT+'/'+OLD+'/')).map(t=>t.path.slice((ROOT+'/'+OLD+'/').length)),['node_runtime_probe.js','package.json','python_runtime_probe.py'],'three old source-directory target dictionaries retained');
ok(newF.targets.some(t=>t.path===ROOT+'/'+QA+'/p212_keyed_stdin_source_root01/RECEPTION.md'),'old content receipt target retained');
ok(!newF.allowed_components.some(p=>p.includes('p212_keyed_stdin_cuda_alias_source')),'new controls not target components');
const oldAuth=canonical(OLD+'/AUTHORIZATION.disabled.json'),newAuth=canonical(NEW+'/AUTHORIZATION.disabled.json');
const expectedAuth=JSON.parse(JSON.stringify(oldAuth));
expectedAuth.source_receipt.path=ROOT+'/'+QA+'/p212_keyed_stdin_cuda_alias_source_root01/RECEPTION.md';
expectedAuth.frontier.path=ROOT+'/'+NEW+'/FRONTIER.json';
wholeValue(newAuth,expectedAuth,'only two disabled authorization paths');
eq(newAuth.enabled,false,'not enabled');for(const k of ['source_receipt','trust_receipt','frontier'])eq(newAuth[k].pin,null,'no actual invented control pin');
const req=canonical(NEW+'/REQUEST.disabled.json');
eq(req,{
 schema:'p212-cuda-alias-observer-request-preparation-v1',enabled:false,status:'HOLD_SOURCE_REVIEW_ROOT_RECEPTION_PREFIX_AND_ONE_INVOCATION_GRANT',
 observer:{path:ROOT+'/'+NEW+'/observe.py',pin:null},authorization_template:{path:ROOT+'/'+NEW+'/AUTHORIZATION.disabled.json',enabled:false},
 source_receipt:newAuth.source_receipt,trust_receipt:newAuth.trust_receipt,frontier:newAuth.frontier,
 stdin_file_role:ROOT+'/'+QA+'/p212_keyed_stdin_input01/empty.stdin',actual_exec_command_request:null,canonical_authorization_argument:null,
 relocated_prefix_acceptance:null,new_one_invocation_grant:null,actual_observation:null,not_an_executable_request:true
},'entire documentary unresolved request object');
// These full textual regions were manually read, not inferred from token presence.
const regions={native:[120,151],resolve:[160,207],whole_file:[222,255],target:[258,303],control:[306,316],validate:[319,353],main:[356,436]};
for(const [n,[lo,hi]] of Object.entries(regions))eq(Buffer.from(aLines.slice(lo-1,hi).join('\n')),Buffer.from(bLines.slice(lo-1,hi).join('\n')),'unchanged complete manually read region '+n);
const six=['driver.js','outer_contract.py','python_runtime_probe.py','node_runtime_probe.js','node_preload.js','product_capture.js'];
const sixKeys=six.map(n=>cache.get(OLD+'/'+n).key);
eq(sixKeys.reduce((n,k)=>n+k.lf_lines,0),2243,'all unchanged six LF lines');eq(sixKeys.reduce((n,k)=>n+k.bytes,0),126440,'all unchanged six bytes');
const nativeDiffs=[];
for(const name of ['observe.py','FRONTIER.json','AUTHORIZATION.disabled.json']){
  const argv=['-u','--label','original/'+name,'--label','cuda_alias_delta/'+name,OLD+'/'+name,NEW+'/'+name];
  const r=cp.spawnSync('/usr/bin/diff',argv,{cwd:ROOT,encoding:null,maxBuffer:1048576});
  ok(!r.error,'native diff no launch error');eq(r.status,1,'actual changed diff exit');eq(r.signal,null,'diff no signal');eq(r.stderr,Buffer.alloc(0),'diff empty stderr');
  eq(r.stdout,read(NEW+'/diffs/'+name+'.diff'),'actual independent whole raw diff versus frozen original');
  const recorded=json(NEW+'/DIFF_NATIVE.json').diffs.find(x=>x.name===name);
  eq(recorded.result.exit_code,1,'archived native diff exit');eq(Buffer.from(recorded.result.output),r.stdout,'independent diff actual raw-equal to author return');
  nativeDiffs.push({name,request:{executable:'/usr/bin/diff',argv,cwd:ROOT},result:{status:r.status,signal:r.signal,stdout_hex:r.stdout.toString('hex'),stderr_hex:r.stderr.toString('hex')},...pin(r.stdout)});
}
let independentReadCount=0,independentReadBytes=0;
const reads=json(SELF+'/READS_NATIVE.json').reads;eq(reads.length,31,'complete selected own read records');
for(const r of reads){
  const cmd=r.command??r.request.cmd;eq(r.result.exit_code,0,'actual independent document command settled');
  if(cmd.startsWith('sha256sum --check --strict'))continue;
  let wanted;
  if(cmd.startsWith('cat ')){wanted=Buffer.concat(cmd.slice(4).split(' ').map(p=>read(p)));}
  else{
    const m=/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_.\/-]+)$/.exec(cmd);ok(m,'exact known nonexecuting read render');
    const ls=text(m[3]).split('\n');eq(ls.pop(),'','whole source final LF');wanted=Buffer.from(ls.slice(Number(m[1])-1,Number(m[2])).join('\n')+'\n');
  }
  eq(Buffer.from(r.result.output),wanted,'whole independent read output equals exact raw file/slice sequence');
  independentReadCount++;independentReadBytes+=wanted.length;
}
inventory();
const keys=[...cache.values()].map(x=>x.key).sort((a,b)=>a.path<b.path?-1:a.path>b.path?1:0);
for(const k of keys)wholeValue(whole(k.path).key,k,'final whole document key unchanged');
console.log(JSON.stringify({
 scope:'INDEPENDENT_SOURCE_DELTA_AND_DOCUMENT_ORIGINALS_ONLY_UNDER_ORDINARY_TRUSTED_BOOTSTRAP',checks,whole_document_keys:keys.length,
 source_packet:{payloads:21,physical_files:22,payload_bytes:NEW_NAMES.reduce((n,p)=>n+read(NEW+'/'+p).length,0),seal:pin(read(NEW+'/SHA256SUMS'))},
 source:{changed_lines:lineDeltas.map(d=>d.line),new_observer:pin(read(NEW+'/observe.py')),protected:pin(rest(bLines)),unchanged_six:sixKeys.map(({path,bytes,sha256,lf_lines})=>({path,bytes,sha256,lf_lines})),combination_lines:2679,combination_bytes:148568},
 frontier:{targets:164,allowed_before:204,allowed_after:207,additions,memberships:5,membership_names:292,gaps:8,modes,no_removed_components:true,no_changed_target_dictionary:true},
 author_replay:{checks:17454,keys:42,...pin(read(NEW+'/CHECK_RESULT.json')),raw_equal:true},author_closing_keys:46,
 author_read_comparisons:authorReadCount,author_read_bytes:authorReadBytes,independent_read_comparisons:independentReadCount,independent_read_bytes:independentReadBytes,
 native_diffs:nativeDiffs,keys,observer_run:false,host_alias_input_private_probe:false,grant:false,manuscript_review:false,
 boundary:'Author and root receipts reused only in their accepted source/failure scopes; no runtime key or enabled-prefix acceptance is issued.'
},null,2));
