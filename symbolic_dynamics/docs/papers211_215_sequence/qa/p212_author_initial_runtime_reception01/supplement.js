'use strict';
// Root documentary complement to the already successful full runtime receiver.
// Reads archived native outputs and exact prior keys; executes no submitted code.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),a=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const OWN=QA+'p212_author_initial_runtime_reception01',B=QA+'p212_author_initial_binding01';
const RUN=QA+'root_replays/p212_author_initial_01',D=QA+'p212_runtime_discovery01';
let checks=0;const inputs={};
function same(x,y,s){checks++;a.deepStrictEqual(x,y,s);}
function need(x,s){checks++;a.ok(x,s);}
const val=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p,k){
  need(path.posix.normalize(p)===p&&p.startsWith('/'),'literal absolute input');
  const l=fs.lstatSync(p);need(fs.statSync(p).isFile(),'regular byte input');
  const b=fs.readFileSync(p),v={...val(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};
  if(inputs[p])same(v,inputs[p],'stable entire key');
  if(k)for(const f of ['sha256','bytes','resolved','symlink'])if(Object.hasOwn(k,f))same(v[f],k[f],'supplied full pin '+f);
  inputs[p]=v;return b;
}
const obj=p=>JSON.parse(read(p));
const binding=obj(B+'/BINDING.json'),r=obj(OWN+'/RESULT.json');
same(r.status,'PASS_ROOT_COMPLETE_P212_INITIAL_PRODUCTION_RECORDS_PENDING_SEMANTICS','prior successful receipt');
same(r.checks,699504,'full original gate not this supplement');
read(binding.root_capture.controller.path,binding.root_capture.controller);
const previous=obj(OWN+'/INPUTS_CURRENT.json');
for(const[p,k]of Object.entries(previous.files))read(p,k);
same(Object.keys(previous.files).length,250,'whole prior byte key');
const parents={outer:obj(B+'/entry01/commands/AUTHOR_INITIAL/RECEIPT.json'),
  launcher:obj(RUN+'/outer/commands/01_launcher/RECEIPT.json'),
  recorder:obj(RUN+'/launcher/commands/01_recorder/RECEIPT.json'),
  child01:obj(RUN+'/recorder/commands/03_verify_01/RECEIPT.json')};
const expectedCounts={outer:14,launcher:14,recorder:35,child01:10};
const nativeKeys=['argv','cwd','ended_epoch','ended_utc','environment','exit_code','failure','interrupted','new_owned_session_requested','pid','process_group_settlement','spawned','started_epoch','started_utc','status','stderr','stdin','stdout','stream_scope','streams_complete','timed_out','timeout_seconds','wrapper_exit_code'];
let nativeCount=0;
function nativeTime(n){
  same(Object.keys(n).filter(k=>k!=='label').sort(),nativeKeys.slice().sort(),'entire native field census');
  for(const f of ['started','ended']){
    need(Number.isFinite(n[f+'_epoch'])&&/Z$|\+00:00$/.test(n[f+'_utc']),'finite UTC actual clock');
    need(Math.abs(Date.parse(n[f+'_utc'])/1000-n[f+'_epoch'])<0.01,'separately sampled UTC/epoch within 10ms');
  }
  need(n.started_epoch<=n.ended_epoch,'native clock ordered');
  need(n.ended_epoch-n.started_epoch<n.timeout_seconds,'observed native lifetime within declared limit');
  same(n.stream_scope,'Every emitted native byte retained in exclusive files; hashes finalized only after owned-group quiescence. A timeout/interruption remains an unsuccessful partial computation.','exact known stream limitation');
  nativeCount++;
}
nativeTime(parents.outer);
for(const stage of ['outer','launcher','recorder','child01']){
  const p=RUN+'/'+stage,s=obj(p+'/RESULT.json'),entered=obj(p+'/ENTERED.json'),parent=parents[stage];
  same(Object.keys(s).sort(),['commands','errors','mode','output','role','scope','stage','status','unfinalized_native','unknown_descendant_closure','wrapper_return'].sort(),'whole stage result fields');
  same(s.scope,'Bounded infrastructure execution evidence, not a proof, review or hermetic runtime trace.','explicit runtime scope');
  same(Object.keys(entered).sort(),['argv','cache','cwd','environment','orig_argv','stage','started_utc','status'].sort(),'whole entry fields');
  same(entered.stage,stage,'entry stage');same(entered.status,'ENTERED_NOT_NATIVE_PRESPAWN','not a prespawn claim');
  same(entered.cache,RUN+'/never_created_'+stage+'_cache','actual entry cache role');
  const start=Date.parse(entered.started_utc)/1000;
  need(parent.started_epoch<=start&&start<=parent.ended_epoch,'stage entry enclosed in real parent lifetime');
  let priorEnd=start;
  for(const n of s.commands){
    nativeTime(n);need(priorEnd<=n.started_epoch,'native commands sequential after stage entry');
    need(n.ended_epoch<=parent.ended_epoch,'entire child native lifetime enclosed');priorEnd=n.ended_epoch;
  }
  if(stage==='outer'||stage==='launcher'){
    const child=stage==='outer'?'launcher':'recorder',m=RUN+'/'+child+'/SHA256SUMS';read(m);
    same(s.output,{child_stage:child,native_receipt:s.commands[0],closed_child:{manifest:inputs[m],payloads:expectedCounts[child],status:'PASS'}},'entire propagated child closure and native receipt');
    same(read(p+'/commands/'+s.commands[0].label+'/stdout.raw').length,0,'successful inner envelope stdout empty');
  }else if(stage==='recorder'){
    same(s.output,{actual_raw_comparisons:0,canonical_policy:'initial stdout requires separate root acceptance/publication; pair never adopts or replaces canonical',mode:'initial',raw_stdout:r.raw_stdout},'whole initial output policy');
    const copies=binding.capsule_files.map(k=>({original:k.path,copy:p+'/capsule/'+k.name,bytes:k.bytes,sha256:k.sha256}));
    same(obj(p+'/SOURCE_COPIES.json'),copies,'whole original/copy table');
    copies.forEach((k,i)=>same(s.commands[i].argv,['/usr/bin/cmp','--',k.original,k.copy],'actual ordered copy command vector'));
  }else{
    const src=RUN+'/recorder/capsule/verify.py';read(src);
    same(s.output,{scientific_argv:[src,'--parameters',RUN+'/recorder/capsule/PARAMETERS.json'],parameter_locator:'explicit_absolute_argv',scientific_outcome:'SYSTEM_EXIT_ZERO',source:inputs[src],cwd:RUN+'/recorder/capsule'},'whole scientific execution interface/outcome');
  }
}
same(nativeCount,8,'seven runtime native plus separate root native');
const normalize=p=>read(p).toString().replace(/\(0x[0-9a-f]+\)/g,'(ADDRESS)');
const discovered=normalize(D+'/commands/03_ldd_before/stdout.raw');
same(normalize(D+'/commands/04_ldd_after/stdout.raw'),discovered,'entire discovery target-ordered linkage text modulo addresses');
for(const name of ['01_ldd_before','06_ldd_after'])same(normalize(RUN+'/recorder/commands/'+name+'/stdout.raw'),discovered,'whole per-target actual linkage, not aggregate-only membership');
const prepNative=obj(B+'/BINDING_NATIVE01.json'),parts=[prepNative.result,...prepNative.polls.map(x=>x.result)];
same(parts.at(-1).exit_code,0,'actual binding preparer completed');
same(prepNative.polls[0].request.session_id,parts[0].session_id,'actual preparer yielded session');
same(JSON.parse(parts.map(x=>x.output).join('')),obj(B+'/RESULT.json'),'whole actual preparer tool output versus saved result');
same(prepNative.request.cmd,'/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/node docs/papers211_215_sequence/qa/p212_author_initial_binding01/prepare_binding.js','exact actual documentary preparation command');
const currentPrep=obj(B+'/INPUTS_AT_BINDING.json');for(const[p,k]of Object.entries(currentPrep))read(p,k);
same(Object.keys(currentPrep).length,265,'whole binding input key');
const t=obj(OWN+'/ROOT_NATIVE02.json'),tparts=[t.result,...(t.polls||[]).map(x=>x.result)];
same(tparts.at(-1).exit_code,0,'actual full receiver tool completed');
same(JSON.parse(tparts.map(x=>x.output).join('')),r,'whole actual full receiver output');
read(OWN+'/supplement.js');
for(const p of Object.keys(inputs))read(p,inputs[p]);
fs.writeFileSync(OWN+'/SUPPLEMENT_INPUTS.json',JSON.stringify(inputs,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({status:'PASS_ROOT_P212_INITIAL_RECORD_SUPPLEMENT_PENDING_SEMANTICS',checks,input_paths:Object.keys(inputs).length,native_commands:8,scientific_executions:0,ldd_equality:'entire target-ordered text after replacing only hexadecimal runtime load addresses; not raw-byte equality',input_key:val(fs.readFileSync(OWN+'/SUPPLEMENT_INPUTS.json'))}));
