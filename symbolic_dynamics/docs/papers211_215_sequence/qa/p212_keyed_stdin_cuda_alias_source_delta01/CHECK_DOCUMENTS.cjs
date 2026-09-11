'use strict';
// Documentary checker only. Never load/execute/parse a reviewed program.
const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert/strict');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = 'docs/papers211_215_sequence/qa';
const OLD = QA + '/p212_keyed_stdin_source_delta01';
const HERE = QA + '/p212_keyed_stdin_cuda_alias_source_delta01';
const INPUTS = [
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_decision01/DECISION.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_decision01/FRONTIER_DOCUMENT_SELECTION_NATIVE.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_decision01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_failed_observation_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_failed_observation_root01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_linecount_erratum01/ERRATUM.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_linecount_erratum01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_nonlineage_audit01/FINDINGS.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_nonlineage_audit01/HANDOFF.md",
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
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_source_root01/SHA256SUMS"
];
const OWN = [
  'observe.py', 'FRONTIER.json', 'AUTHORIZATION.disabled.json', 'REQUEST.disabled.json',
  'DELTA.md', 'CONTRACT.md', 'INPUTS.sha256', 'INPUT_KEYS_NATIVE.json',
  'ORIGINAL_READS_NATIVE.json', 'OWN_READS_NATIVE.json', 'DIFF_NATIVE.json',
  'PREPARATION_NATIVE.json', 'diffs/observe.py.diff', 'diffs/FRONTIER.json.diff',
  'diffs/AUTHORIZATION.disabled.json.diff', 'CHECK_DOCUMENTS.cjs'
];
const permission = new Set([...INPUTS, ...OWN.map(n => HERE + '/' + n)]);
const FIELDS = ['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs','birthtimeNs'];
let checks = 0;
function ok(value, label) { checks++; assert(value, label); }
function equal(a, b, label) { checks++; assert.deepStrictEqual(a, b, label); }
function tree(a, b, label) {
  equal(a === null, b === null, label + ': null');
  equal(typeof a, typeof b, label + ': type');
  if (a === null || typeof a !== 'object') { equal(a,b,label); return; }
  equal(Array.isArray(a),Array.isArray(b),label+': array');
  equal(Object.keys(a).sort(),Object.keys(b).sort(),label+': whole keys');
  for (const key of Object.keys(a)) tree(a[key],b[key],label+'.'+key);
}
const hash = raw => crypto.createHash('sha256').update(raw).digest('hex');
const shape = s => Object.fromEntries(FIELDS.map(k => [k,String(s[k])]));
const cache = new Map();
function whole(path) {
  ok(permission.has(path),'exact documentary selection before any filesystem access: '+path);
  const lexical = fs.lstatSync(path,{bigint:true});
  ok(lexical.isFile() && !lexical.isSymbolicLink() && lexical.nlink === 1n,'single-link regular document');
  const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try {
    const a=fs.fstatSync(fd,{bigint:true});
    equal(shape(lexical),shape(a),'same selected document fd');
    const raw=fs.readFileSync(fd);
    equal(shape(a),shape(fs.fstatSync(fd,{bigint:true})),'unchanged same-fd whole document');
    equal(shape(a),shape(fs.lstatSync(path,{bigint:true})),'unchanged lexical document');
    equal(BigInt(raw.length),a.size,'complete document length');
    const key={path,bytes:raw.length,sha256:hash(raw),lf_lines:raw.reduce((n,b)=>n+(b===10),0),fields:shape(a)};
    return {raw,key};
  } finally { fs.closeSync(fd); }
}
function read(path) { if (!cache.has(path)) cache.set(path,whole(path)); return cache.get(path).raw; }
function own(name) { return read(HERE+'/'+name); }
function text(path) { const raw=read(path),s=raw.toString('utf8'); equal(Buffer.from(s),raw,'lossless UTF-8'); return s; }
function json(path) { return JSON.parse(text(path)); }
function ownJSON(name) { return json(HERE+'/'+name); }
function once(s,a,b) {
  equal(s.split(a).length,2,'exact single substitution');
  return s.replace(a,b);
}
const initialNative=ownJSON('INPUT_KEYS_NATIVE.json');
equal(initialNative.result.exit_code,0,'actual initial input command');
const initial=JSON.parse(initialNative.result.output);
equal(initial.records.map(k=>k.path),INPUTS,'exact 26 input selection');
equal(initial.fields,FIELDS,'entire ten documentary fields');
equal(own('INPUTS.sha256'),Buffer.from(initial.records.map(k=>k.sha256+'  '+k.path).join('\n')+'\n'),'exact input manifest');
for (const key of initial.records) {
  read(key.path);
  tree(cache.get(key.path).key,key,'whole initial input key '+key.path);
}
const seals = [
 ['p212_keyed_stdin_source_delta01','f076522fc7e120c46be0c57b60168784c38c32339e07f65b74e0012694ca1ee8',55],
 ['p212_keyed_stdin_source_root01','0f65f815ca28d4153bc968b0d8dd041f3571287ebe639c942abce6064bb32380',16],
 ['p212_keyed_stdin_nonlineage_audit01','ff622be9502a7bd931820cf1c22b5e858bc09243ef3e0488fe7d65cfbea71887',24],
 ['p212_keyed_stdin_linecount_erratum01','7876c67cf7a4f436e746bf7ac282868dce74aa7c5ef31063725af815371c4007',7],
 ['p212_keyed_stdin_failed_observation_root01','0c99b21b1e0401bc771abb0561e5969f8bb6fc7925ddb0ce0d36a32ccf4f16be',10],
 ['p212_keyed_stdin_cuda_alias_decision01','c1c05f3714d9b1a803091bd6e76c0676d2657396452da2bf523493bd312eff69',2]
];
for(const [name,digest,count] of seals){
  const base=QA+'/'+name,raw=read(base+'/SHA256SUMS'),rows=raw.toString('utf8').trimEnd().split('\n');
  equal(hash(raw),digest,'fixed accepted/decision seal '+name);equal(rows.length,count,'whole manifest row census');
  const map=new Map();
  for(const row of rows){const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.\/-]+)$/.exec(row);
    ok(m,'strict bare-relative nonself manifest grammar');ok(!m[2].startsWith('/')&&!m[2].split('/').some(p=>p===''||p==='.'||p==='..')&&m[2]!=='SHA256SUMS','manifest finite names');
    ok(!map.has(m[2]),'no duplicate manifest entry');map.set(m[2],m[1]);}
  for(const path of INPUTS.filter(p=>p.startsWith(base+'/')&&!p.endsWith('/SHA256SUMS')))
    equal(hash(read(path)),map.get(path.slice(base.length+1)),'whole selected payload against seal');
}
// Seals commit their other payloads; this checker does not reopen unselected files.
const originalReads=ownJSON('ORIGINAL_READS_NATIVE.json');
equal(originalReads.reads.length,17,'complete actual original read selection');
let originalReadBytes=0;
for(const item of originalReads.reads){
  ok(INPUTS.includes(item.path),'selected original render path');
  equal(item.result.exit_code,0,'native source read settled zero');
  ok(!item.result.output.startsWith('Warning: truncated output'),'no actual leading truncation header');
  equal(Buffer.from(item.result.output),read(item.path),'whole actual original raw return');
  originalReadBytes+=Buffer.byteLength(item.result.output);
}
const ownReads=ownJSON('OWN_READS_NATIVE.json');
equal(ownReads.reads.map(x=>x.name),['observe.py','FRONTIER.json','AUTHORIZATION.disabled.json','REQUEST.disabled.json','DELTA.md','CONTRACT.md'],'six complete derivative reads');
let derivativeReadBytes=0;
for(const item of ownReads.reads){
  equal(item.path,HERE+'/'+item.name,'own exact render selection');
  equal(item.result.exit_code,0,'own read settled');
  ok(!item.result.output.startsWith('Warning: truncated output'),'complete derivative return');
  equal(Buffer.from(item.result.output),own(item.name),'whole derivative raw return');
  derivativeReadBytes+=Buffer.byteLength(item.result.output);
}
const oldObserver=text(OLD+'/observe.py'),newObserver=text(HERE+'/observe.py');
const replacements=[
 ["HERE = QA + '/p212_keyed_stdin_source_delta01'","HERE = QA + '/p212_keyed_stdin_cuda_alias_source_delta01'"],
 ["SOURCE_RECEIPT = QA + '/p212_keyed_stdin_source_root01/RECEPTION.md'","SOURCE_RECEIPT = QA + '/p212_keyed_stdin_cuda_alias_source_root01/RECEPTION.md'"]
];
let expected=oldObserver,reverse=newObserver;
for(const [a,b] of replacements){expected=once(expected,a,b);reverse=once(reverse,b,a);}
equal(Buffer.from(expected),own('observe.py'),'entire only-two-lines forward reconstruction');
equal(Buffer.from(reverse),read(OLD+'/observe.py'),'entire only-two-lines reverse reconstruction');
const oldLines=oldObserver.split('\n'),newLines=newObserver.split('\n');
equal(oldLines.length,437,'old exact LF lines');equal(newLines.length,437,'new exact LF lines');
const changed=[];
for(let i=0;i<oldLines.length;i++) if(oldLines[i]!==newLines[i]) changed.push(i+1);
equal(changed,[17,19],'only exact two constant lines');
const oldProtected=oldLines.filter((_,i)=>i!==16&&i!==18).join('\n');
const newProtected=newLines.filter((_,i)=>i!==16&&i!==18).join('\n');
equal(Buffer.from(oldProtected),Buffer.from(newProtected),'all other program bytes including imports and every guard');
for(const literal of [
 "FRONTIER = HERE + '/FRONTIER.json'",
 "TRUST_RECEIPT = QA + '/p212_trusted_product_boundary_root01/RECEPTION.md'",
 "STDIN_FILE = QA + '/p212_keyed_stdin_input01/empty.stdin'",
 "flags, 0xFFF, ctypes.byref(data)", "need(data.mask & 0xFFF == 0xFFF",
 "NATIVE_EVENTS.append(event)", "need(candidate in allowed",
 "need(all(p in allowed for p in components(target))",
 "queue = target.split('/')[1:] + queue", "stable(expected, before)",
 "for pass_number in (1, 2)", "if not result['errors']:",
 "authorization['enabled'] is True", "initialize_native()"
]) ok(newObserver.includes(literal),'preserved exact protected literal '+literal);
const oldF=json(OLD+'/FRONTIER.json'),newF=ownJSON('FRONTIER.json');
equal(own('FRONTIER.json'),Buffer.from(JSON.stringify(newF,null,2)+'\n'),'canonical frontier raw bytes');
equal(newF.targets.length,164,'all targets');
tree(newF.targets,oldF.targets,'all complete target dictionaries');
tree(newF.closure_gaps,oldF.closure_gaps,'all exact gap text');
equal(newF.closure_gaps.length,8,'eight gaps');
const additions=['/etc/alternatives','/etc/alternatives/cuda','/etc/alternatives/cuda-12'];
equal(oldF.allowed_components.length,204,'old component count');
equal(newF.allowed_components.length,207,'new component count');
equal(newF.allowed_components,[...new Set([...oldF.allowed_components,...additions])].sort(),'exact finite union');
equal(newF.allowed_components.filter(p=>!oldF.allowed_components.includes(p)),additions,'only three added names');
equal(oldF.allowed_components.filter(p=>!newF.allowed_components.includes(p)),[],'no removed name');
for(const key of Object.keys(oldF).filter(k=>k!=='allowed_components')) tree(newF[key],oldF[key],'unchanged entire frontier member '+key);
const expectedFrontier=once(text(OLD+'/FRONTIER.json'),'    "/etc",\n','    "/etc",\n'+additions.map(p=>'    "'+p+'",\n').join(''));
equal(Buffer.from(expectedFrontier),own('FRONTIER.json'),'entire frontier is one literal insertion');
const members=newF.targets.filter(t=>t.mode==='membership');
equal(members.length,5,'five original memberships');equal(members.reduce((n,t)=>n+t.expected_names.length,0),292,'all names');
const modes={};for(const target of newF.targets)modes[target.mode]=(modes[target.mode]||0)+1;
tree(modes,{file:110,optional_file:32,optional_directory:11,membership:5,metadata:5,absent:1},'all original modes');
function components(path){
  equal(typeof path,'string','documentary path string');
  ok(path==='/'||/^\/[^/]+(?:\/[^/]+)*$/.test(path),'literal normalized path');
  ok(!path.split('/').some(p=>p==='.'||p==='..')&&!path.includes('\x00'),'no dot/null components');
  let current='';return ['/'].concat(path==='/'?[]:path.slice(1).split('/').map(name=>(current+='/'+name)));
}
for(const p of newF.allowed_components)for(const c of components(p))ok(newF.allowed_components.includes(c),'documentary ancestor closure only');
for(const added of additions)ok(!newF.targets.some(t=>t.path===added),'no new alias target');
const oldSourceTargets=newF.targets.filter(t=>t.path.startsWith(ROOT+'/'+OLD+'/'));
equal(oldSourceTargets.map(t=>t.path.slice((ROOT+'/'+OLD+'/').length)),['node_runtime_probe.js','package.json','python_runtime_probe.py'],'three old source target rows remain');
ok(newF.targets.some(t=>t.path===ROOT+'/'+QA+'/p212_keyed_stdin_source_root01/RECEPTION.md'),'old receipt target is retained');
ok(!newF.allowed_components.some(p=>p.includes('p212_keyed_stdin_cuda_alias_source')),'new controls not smuggled into target components');
for(const c of components('/usr/local/cuda-12.8/targets/x86_64-linux/lib'))ok(oldF.allowed_components.includes(c),'old selected cuda-12.8 literal chain only');
const oldA=json(OLD+'/AUTHORIZATION.disabled.json'),newA=ownJSON('AUTHORIZATION.disabled.json');
equal(own('AUTHORIZATION.disabled.json'),Buffer.from(JSON.stringify(newA,null,2)+'\n'),'canonical disabled authorization');
const wanted=JSON.parse(JSON.stringify(oldA));
wanted.source_receipt.path=ROOT+'/'+QA+'/p212_keyed_stdin_cuda_alias_source_root01/RECEPTION.md';
wanted.frontier.path=ROOT+'/'+HERE+'/FRONTIER.json';
tree(newA,wanted,'entire authorization changed only two paths');
equal(newA.enabled,false,'disabled');equal(newA.status,'HOLD_SOURCE_ONLY_NO_OBSERVER_OR_AUTHOR_PROBE','unchanged HOLD status');
for(const role of ['source_receipt','trust_receipt','frontier'])equal(newA[role].pin,null,'no fake receipt or control pin');
const req=ownJSON('REQUEST.disabled.json');
equal(own('REQUEST.disabled.json'),Buffer.from(JSON.stringify(req,null,2)+'\n'),'canonical documentary request');
equal(req.schema,'p212-cuda-alias-observer-request-preparation-v1','distinct request schema');
equal(req.enabled,false,'documentary request disabled');equal(req.not_an_executable_request,true,'no executable request');
equal(req.authorization_template,{path:ROOT+'/'+HERE+'/AUTHORIZATION.disabled.json',enabled:false},'disabled template role');
equal(req.observer,{path:ROOT+'/'+HERE+'/observe.py',pin:null},'selected source role not actual key');
for(const role of ['source_receipt','trust_receipt','frontier'])tree(req[role],newA[role],'same unresolved request role');
equal(req.stdin_file_role,ROOT+'/'+QA+'/p212_keyed_stdin_input01/empty.stdin','unchanged input literal role only');
for(const name of ['actual_exec_command_request','canonical_authorization_argument','relocated_prefix_acceptance','new_one_invocation_grant','actual_observation'])equal(req[name],null,'no invented future '+name);
const requestKeys=['schema','enabled','status','observer','authorization_template','source_receipt','trust_receipt','frontier','stdin_file_role','actual_exec_command_request','canonical_authorization_argument','relocated_prefix_acceptance','new_one_invocation_grant','actual_observation','not_an_executable_request'];
equal(Object.keys(req),requestKeys,'complete documentary request schema');
// Reconstruct both complete files from each native unified diff as text, not language source.
function reconstruct(diff,before,after,name) {
  const lines=diff.split('\n');equal(lines.pop(),'','diff final LF');
  equal(lines.shift(),'--- original/'+name,'old exact diff label');
  equal(lines.shift(),'+++ cuda_alias_delta/'+name,'new exact diff label');
  const original=before.split('\n'),target=after.split('\n');
  equal(original.pop(),'','original final LF');equal(target.pop(),'','derivative final LF');
  let i=0,oldPos=0,newPos=0,hunks=0,added=0,removed=0;const forward=[],back=[];
  while(i<lines.length){
    const m=/^@@ -(\d+),(\d+) \+(\d+),(\d+) @@$/.exec(lines[i++]);ok(m,'exact unified hunk');
    const os=Number(m[1])-1,oc=Number(m[2]),ns=Number(m[3])-1,nc=Number(m[4]);
    ok(os>=oldPos&&ns>=newPos,'nonoverlapping ordered hunks');
    const oldGap=original.slice(oldPos,os),newGap=target.slice(newPos,ns);
    equal(oldGap,newGap,'whole unchanged interhunk bytes');forward.push(...oldGap);back.push(...newGap);
    oldPos=os;newPos=ns;let usedOld=0,usedNew=0;
    while(i<lines.length&&!lines[i].startsWith('@@ ')){
      const line=lines[i++],tag=line[0],body=line.slice(1);
      ok([' ','+','-'].includes(tag),'strict diff line');
      if(tag!=='+' ){equal(original[oldPos++],body,'whole removed/context line');back.push(body);usedOld++;}
      if(tag!=='-' ){equal(target[newPos++],body,'whole inserted/context line');forward.push(body);usedNew++;}
      added+=tag==='+';removed+=tag==='-';
    }
    equal(usedOld,oc,'whole old hunk count');equal(usedNew,nc,'whole new hunk count');hunks++;
  }
  equal(original.slice(oldPos),target.slice(newPos),'whole unchanged tail');
  forward.push(...original.slice(oldPos));back.push(...target.slice(newPos));
  equal(Buffer.from(forward.join('\n')+'\n'),Buffer.from(after),'whole native diff forward');
  equal(Buffer.from(back.join('\n')+'\n'),Buffer.from(before),'whole native diff reverse');
  return {name,hunks,added,removed,bytes:Buffer.byteLength(diff),sha256:hash(Buffer.from(diff))};
}
const nativeDiffs=ownJSON('DIFF_NATIVE.json');
equal(nativeDiffs.diffs.map(x=>x.name),['observe.py','FRONTIER.json','AUTHORIZATION.disabled.json'],'all three native differences');
const differences=[];
for(const item of nativeDiffs.diffs){
  equal(item.old_path,OLD+'/'+item.name,'fixed original diff operand');equal(item.new_path,HERE+'/'+item.name,'fixed new diff operand');
  equal(item.request.cmd,'diff -u --label original/'+item.name+' --label cuda_alias_delta/'+item.name+' '+item.old_path+' '+item.new_path,'entire native diff command');
  equal(item.result.exit_code,1,'expected actual native difference exit');
  equal(Buffer.from(item.result.output),own('diffs/'+item.name+'.diff'),'complete native stdout attachment');
  differences.push(reconstruct(item.result.output,text(item.old_path),text(item.new_path),item.name));
}
tree(differences.map(({name,hunks,added,removed})=>({name,hunks,added,removed})),[
 {name:'observe.py',hunks:1,added:2,removed:2},
 {name:'FRONTIER.json',hunks:1,added:3,removed:0},
 {name:'AUTHORIZATION.disabled.json',hunks:2,added:2,removed:2}
],'entire exact difference budget');
const preparation=ownJSON('PREPARATION_NATIVE.json');
equal(preparation.new_directory_absence.result.exit_code,0,'actual new-only destination check');
equal(preparation.authorship.independent_reviewer,null,'author checks are not review');
const refinement=preparation.preseal_contract_wording_refinement;
equal(refinement.old_read.result.exit_code,0,'historical full prose read');
equal(refinement.new_read.result.exit_code,0,'final full prose read');
const oldPhrase='- Required-file type and full expected native identity precede body open/\n  read; before/after same-fd and resolution comparisons remain. Ancestor\n';
const newPhrase='- Required-file type is checked before open; the same-fd native key is\n  compared with the expected key before content read. Before/after same-fd\n  and resolution comparisons remain. Ancestor\n';
equal(Buffer.from(once(refinement.old_read.result.output,oldPhrase,newPhrase)),own('CONTRACT.md'),'exact retained prose refinement');
equal(Buffer.from(refinement.new_read.result.output),own('CONTRACT.md'),'final prose raw original');
const programNames=['observe.py','driver.js','outer_contract.py','python_runtime_probe.py','node_runtime_probe.js','node_preload.js','product_capture.js'];
const programKeys=programNames.map(name=>cache.get(OLD+'/'+name).key);
equal(programKeys.reduce((n,k)=>n+k.lf_lines,0),2679,'accepted erratum program total');
equal(programKeys.reduce((n,k)=>n+k.bytes,0),148546,'whole seven old program bytes');
for(const name of OWN)own(name);
const keys=[...cache.values()].map(x=>x.key).sort((a,b)=>a.path.localeCompare(b.path));
for(const key of keys)tree(whole(key.path).key,key,'unchanged entire closing documentary key');
console.log(JSON.stringify({
 scope:'DOCUMENT_ONLY_NO_REVIEWED_SOURCE_EXECUTION_IMPORT_AST_SYNTAX_OR_EMBEDDED_PATH_PROBE',
 checks,old_input_count:INPUTS.length,old_input_bytes:initial.records.reduce((n,k)=>n+k.bytes,0),
 whole_document_keys:keys.length,original_full_read_bytes:originalReadBytes,derivative_full_read_bytes:derivativeReadBytes,
 source_changed_lines:changed,protected_source_bytes:Buffer.byteLength(newProtected),protected_source_sha256:hash(Buffer.from(newProtected)),
 frontier:{targets:164,old_components:204,new_components:207,added_components:additions,memberships:5,membership_names:292,closure_gaps:8,modes},
 differences,original_programs:programKeys.map(({path,bytes,sha256,lf_lines})=>({path,bytes,sha256,lf_lines})),
 keys,independent_review:false,observer_run:false,authorization_enabled:false
},null,2));
