'use strict';
// Independent read-only documentary receiver. No submitted Python/import/probe,
// science, ambient-environment read, subprocess, or filesystem write.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const PREP=QA+'p212_runtime_preparation01',DISC=QA+'p212_runtime_discovery01';
const CONTROL=QA+'p212_import_discovery_root01',ENTRY=CONTROL+'/entry01';
const OWN=QA+'p212_runtime_discovery_independent01';
const ENV={LANG:'C.UTF-8',LC_ALL:'C.UTF-8',PATH:'/usr/bin:/bin',TZ:'UTC'};
const imports=['itertools','json','math','sys','fractions'],tags=['outer','launcher','recorder','child'];
const sourceNames=['runtime_core.py','p212_runtime.py','prepare_runtime.py'];
const oldNames=['runtime_core.py','p211_runtime.py','prepare_runtime.py'];
const pins={},states={},stateInputs={},coverage={},hostAllowed=new Set();
let checks=0;
function need(v,label){checks++;if(!v)throw Error(label);}
function same(a,b,label){checks++;assert.deepStrictEqual(a,b,label);}
function names(a,b,label){same([...a].sort(),[...b].sort(),label);}
function pin(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
function bytePin(v){return {bytes:v.bytes,sha256:v.sha256};}
function abs(p){need(typeof p==='string'&&p.startsWith('/')&&path.posix.normalize(p)===p&&!/[\x00\r\n\t]/.test(p),'literal absolute path');return p;}
function allowed(p){
  abs(p);need(!p.startsWith(ROOT+'/papers/'),'no mathematical/scientific paper file read');
  need(p.startsWith(QA)||p===ROOT+'/.agents/skills/symbolic-dynamics-research/SKILL.md'||p===ROOT+'/docs/research_state/WORKFLOW.md'||hostAllowed.has(p),'exact workspace/documentary or named host input '+p);
}
function statKey(s){return {dev:String(s.dev),ino:String(s.ino),mode:String(s.mode),nlink:String(s.nlink),size:String(s.size),mtimeNs:String(s.mtimeNs),ctimeNs:String(s.ctimeNs)};}
function read(p){
  allowed(p);const a=fs.lstatSync(p,{bigint:true}),r=fs.realpathSync(p),sa=fs.statSync(p,{bigint:true});
  need(sa.isFile(),'ordinary byte input '+p);const raw=fs.readFileSync(p);
  const z=fs.lstatSync(p,{bigint:true}),sz=fs.statSync(p,{bigint:true});
  same(statKey(a),statKey(z),'stable lexical input '+p);same(statKey(sa),statKey(sz),'stable resolved input '+p);
  const q={...pin(raw),resolved:r,symlink:a.isSymbolicLink()?fs.readlinkSync(p):null};
  if(pins[p]){same(pins[p],q,'whole repeated original key '+p);same(states[p],{lexical:statKey(z),resolved:statKey(sz)},'repeated within-audit metadata '+p);}
  pins[p]=q;states[p]={lexical:statKey(z),resolved:statKey(sz)};return raw;
}
function strictJSON(raw){
  const s=raw.toString('utf8');need(Buffer.from(s).equals(raw),'UTF8 JSON bytes');
  let i=0;function ws(){while(/[ \t\r\n]/.test(s[i]||'\0'))i++;}
  function str(){const start=i;need(s[i++]==='"','JSON string');while(i<s.length){if(s[i]==='\\'){i+=2;continue;}if(s[i++]==='"')return JSON.parse(s.slice(start,i));}throw Error('unterminated JSON');}
  function val(){ws();if(s[i]==='{'){i++;const keys=new Set();ws();if(s[i]==='}'){i++;return;}
      for(;;){ws();const k=str();need(!keys.has(k),'no duplicate JSON object key');keys.add(k);ws();need(s[i++]===':','JSON colon');val();ws();if(s[i]==='}'){i++;return;}need(s[i++ ]===',','JSON object comma');}}
    if(s[i]==='['){i++;ws();if(s[i]===']'){i++;return;}for(;;){val();ws();if(s[i]===']'){i++;return;}need(s[i++ ]===',','JSON array comma');}}
    if(s[i]==='"'){str();return;}const m=/^(?:true|false|null|-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?)/.exec(s.slice(i));need(m,'JSON token');i+=m[0].length;}
  val();ws();same(i,s.length,'complete single JSON value');return JSON.parse(s);
}
function obj(p){return strictJSON(read(p));}
function checkPin(p,k){same(bytePin(pins[p]||pin(read(p))),bytePin(k),'exact original bytes '+p);}
function richCheck(p,k){read(p);same(pins[p],k,'entire original rich key '+p);}
function sums(raw){const s=raw.toString('utf8');need(s.endsWith('\n'),'complete SHA LF');const out={};
  for(const line of s.slice(0,-1).split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);need(m&&!Object.hasOwn(out,m[2]),'unique exact SHA row');need(path.posix.normalize(m[2])===m[2]&&!m[2].startsWith('/')&&!m[2].split('/').includes('..'),'safe package-relative SHA row');out[m[2]]=m[1];}return out;}
function inventory(base,files,empties=[]){
  const found=[],dirs=['.'];function walk(rel){const p=base+(rel?'/'+rel:'');need(fs.lstatSync(p).isDirectory()&&fs.realpathSync(p)===p,'physical explicit package directory');
    for(const d of fs.readdirSync(p,{withFileTypes:true})){const n=rel?rel+'/'+d.name:d.name;need(!d.isSymbolicLink(),'no package symlink');if(d.isDirectory()){dirs.push(n);walk(n);}else{need(d.isFile(),'ordinary package member');found.push(n);}}}
  walk('');names(found,files,'whole package file inventory '+base);const expectedDirs=new Set(['.']);
  for(const n of [...files,...empties]){if(empties.includes(n))expectedDirs.add(n);let d=path.posix.dirname(n);while(d!=='.'){expectedDirs.add(d);d=path.posix.dirname(d);}}
  names(dirs,expectedDirs,'whole package directory inventory '+base);
  for(const d of empties)same(fs.readdirSync(base+'/'+d),[],'explicit empty capsule');return {files:found.length,directories:dirs.length,empty_directories:empties};
}
function sealed(base,wanted,count,empties=[]){read(base+'/SHA256SUMS');same(bytePin(pins[base+'/SHA256SUMS']),wanted,'exact original seal '+base);const rows=sums(read(base+'/SHA256SUMS'));same(Object.keys(rows).length,count,'exact full payload count');
  const inv=inventory(base,[...Object.keys(rows),'SHA256SUMS'],empties);
  for(const[n,h]of Object.entries(rows)){read(base+'/'+n);same(pins[base+'/'+n].sha256,h,'whole nonself payload hash');}
  return {...inv,payloads:count,bytes:Object.keys(rows).reduce((n,k)=>n+pins[base+'/'+k].bytes,0)+wanted.bytes,seal:wanted};
}
coverage.discovery=sealed(DISC,{bytes:5887,sha256:'d11634200197a54df1b944e36472c9ee9ab527b8c116da377e2d22dc23213ab7'},58,['empty_probe_capsule']);
coverage.entry=sealed(ENTRY,{bytes:861,sha256:'1a3670bdbb42bf1585345ccd14767981027c20a15e75fa07772c6c3eb85024da'},9);
const approval=obj(CONTROL+'/APPROVAL.json'),rootNative=obj(CONTROL+'/ROOT_NATIVE01.json');
same(pins[CONTROL+'/APPROVAL.json'].sha256,'c9fcc109ce9f1e077abb6aa1b516d6aa0bc94fd9fe13d972a66dae18da4f4609','actual approval digest');
same(approval.format,'p212-import-discovery-binding-v1','approval format');same(approval.approved,true,'actual approved import-only');
same(approval.scope,'IMPORT_ONLY_NO_SCIENTIFIC_SOURCE_READ','non-science scope');same(approval.reviewed_all_preparation_sources,true,'separate whole-source gate');
same(approval.root_authority_decision,'AUTHORIZE_ONE_P212_IMPORT_ONLY_DISCOVERY_NO_SCIENCE','separate root authority');
same(approval.declared_imports,imports,'exact declared imports');same(approval.output,DISC,'exact fresh discovery role');same(approval.native_timeout_seconds,60,'exact positive native deadline');
names(Object.keys(approval.source_inputs),sourceNames.map(n=>PREP+'/'+n),'exact three sources');
names(Object.keys(approval.lineage_inputs),oldNames.map(n=>QA+'p211_runtime_preparation/'+n),'exact three lineage files');
for(const [p,k]of Object.entries({...approval.source_inputs,...approval.lineage_inputs})){read(p);checkPin(p,k);}
same(approval.provenance_inputs.length,3,'whole authority provenance');
for(const r of approval.provenance_inputs){read(r.path);checkPin(r.path,r);}
same(approval.root_capture.entry,ENTRY,'literal capture output');
same(approval.root_capture.timeout_seconds,300,'root native deadline');same(approval.root_capture.environment,ENV,'root ENV4');
same(approval.root_capture.controller.path,CONTROL+'/run.py','root controller path');
read(CONTROL+'/run.py');checkPin(CONTROL+'/run.py',approval.root_capture.controller);
need(read(CONTROL+'/run.py').equals(read(ENTRY+'/EXECUTED_CONTROLLER.py')),'entire executed controller bytes');
need(read(CONTROL+'/APPROVAL.json').equals(read(ENTRY+'/APPROVAL_ORIGINAL.json')),'entire actual approval bytes');
const digest=pins[CONTROL+'/APPROVAL.json'].sha256;
const preparerArgv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+DISC+'/never_created_preparer_cache',PREP+'/prepare_runtime.py',CONTROL+'/APPROVAL.json',digest];
same(approval.root_capture.child_argv_without_approval_digest,preparerArgv.slice(0,-1),'approved exact startup argv');
const outerArgv=['/usr/bin/env','-i','PATH=/usr/bin:/bin','LANG=C.UTF-8','LC_ALL=C.UTF-8','TZ=UTC',...preparerArgv];
same(rootNative.request.cmd,['/usr/bin/env','-i','PATH=/usr/bin:/bin','LANG=C.UTF-8','LC_ALL=C.UTF-8','TZ=UTC','/usr/bin/python3.10','-I','-S','-B',CONTROL+'/run.py',CONTROL+'/APPROVAL.json',digest].join(' '),'exact actual root tool argv');
same(rootNative.request.workdir,ROOT,'actual outer cwd');
need(Number.isInteger(rootNative.result.session_id)&&!Object.hasOwn(rootNative.result,'exit_code'),'genuine initial running handle');
same(rootNative.result.output,'','original first output empty');same(rootNative.polls.length,1,'one actual root completion poll');
same(rootNative.polls[0].request.session_id,rootNative.result.session_id,'same original session');same(rootNative.polls[0].request.chars,'','read-only poll');
same(rootNative.polls[0].result.exit_code,0,'settled root native exit');need(!rootNative.polls[0].result.session_id,'root native terminal completion');
const outerReturned=strictJSON(Buffer.from(rootNative.result.output+rootNative.polls[0].result.output));
same(outerReturned,{entry:ENTRY,errors:[],root_native_commands:1,scientific_executions:0,seal:{manifest:coverage.entry.seal,payloads:9},status:'CAPTURED_IMPORT_DISCOVERY_PENDING_ROOT_COMPLETE_RECEPTION'},'entire actual root returned summary');
const entryResult=obj(ENTRY+'/RESULT.json'),result=obj(DISC+'/RESULT.json'),lock=obj(DISC+'/RUNTIME_LOCK.json');
same(entryResult.status,'CAPTURED_IMPORT_DISCOVERY_PENDING_ROOT_COMPLETE_RECEPTION','entry status pending root');
same(entryResult.errors,[],'no root capture errors');same(entryResult.runtime_lock_accepted,false,'root capture not lock acceptance');same(entryResult.canonical_created,false,'no adoption');same(entryResult.scientific_executions,0,'no science');
same(result.status,'PASS_PREPARATION_ONLY','preparation-only result');same(result.errors,[],'no preparation errors');same(result.scientific_executions,0,'zero scientific invocations');same(result.science_sources_read_or_imported,[],'no scientific read/import list');
same(result.runtime_file_count,130,'actual new runtime count');same(result.commands.length,12,'twelve internal native commands');
same(lock.format,'p212-bounded-runtime-lock-v1','new lock format');same(lock.status,'INFRA_IMPORT_CLOSURE_ONLY_PENDING_ROOT_COMPLETE_RECEPTION','lock not authority');
same(lock.declared_imports,imports,'lock declaration');same(lock.probe_layers,tags,'four role samples');
for(const p of Object.keys(lock.files))hostAllowed.add(p);
for(const k of Object.values(lock.files))hostAllowed.add(k.resolved);
const staticExtras=['/usr/bin/readelf','/usr/lib/python3.10/_pydecimal.py','/usr/lib/python3.10/contextvars.py'];
for(const p of staticExtras){hostAllowed.add(p);if(fs.existsSync(p))hostAllowed.add(fs.realpathSync(p));}
const before=obj(DISC+'/SOURCE_INPUTS_BEFORE.json'),after=obj(DISC+'/SOURCE_INPUTS_AFTER.json');
same(before,after,'whole original source key before/after');
const wantedSource=[...Object.keys(approval.source_inputs),...Object.keys(approval.lineage_inputs),CONTROL+'/APPROVAL.json',...approval.provenance_inputs.map(r=>r.path)];
names(Object.keys(before),wantedSource,'entire ten source/authority inputs');
for(const[p,k]of Object.entries(before))richCheck(p,k);
const eb=obj(ENTRY+'/INPUTS_BEFORE.json'),ea=obj(ENTRY+'/INPUTS_AFTER.json');same(eb,ea,'whole root capture key before/after');
names(Object.keys(eb),[CONTROL+'/run.py',...wantedSource],'whole root11 inputs');
for(const[p,k]of Object.entries(eb))richCheck(p,k);
const rb=obj(DISC+'/RUNTIME_INPUTS_BEFORE.json'),ra=obj(DISC+'/RUNTIME_INPUTS_AFTER.json');
same(rb,ra,'whole actual runtime before/after');same(lock.files,rb,'entire lock identical to actual before/after key');
same(Object.keys(rb).length,130,'all130 lexical runtime spellings');
for(const[p,k]of Object.entries(rb))richCheck(p,k);
coverage.keys={source_inputs:10,root_inputs:11,runtime_spellings:130,resolved_runtime_files:new Set(Object.values(rb).map(v=>v.resolved)).size,host_spellings:Object.keys(rb).filter(p=>!p.startsWith(ROOT+'/')).length};
const wantedLabels=sourceNames.map((_,i)=>'00_snapshot_cmp_'+i).concat(sourceNames.map((_,i)=>'01_source_diff_'+i),tags.map(t=>'02_probe_'+t),['03_ldd_before','04_ldd_after']);
same(result.commands.map(r=>r.label),wantedLabels,'exact complete ordered12 labels');same(entryResult.commands.length,1,'one root preparer command');
const emptyPin=pin(Buffer.alloc(0));
function native(base,row,argv,expectedCode,timeout,cwd){
  const label=row.label,dir=base+'/commands/'+label,attempt=obj(dir+'/ATTEMPT.json'),receipt=obj(dir+'/RECEIPT.json');
  const copy={...row};delete copy.label;same(copy,receipt,'whole receipt/result command binding '+label);
  const expectedAttempt={argv,cwd,environment:ENV,exit_code:null,new_owned_session_requested:true,started_epoch:receipt.started_epoch,started_utc:receipt.started_utc,status:'ATTEMPTED',stdin:'DEVNULL',timeout_seconds:timeout};
  same(attempt,expectedAttempt,'whole exact original ATTEMPT '+label);
  same(receipt.argv,argv,'native exact argv '+label);same(receipt.cwd,cwd,'native exact cwd');same(receipt.environment,ENV,'native actual ENV4');
  same(receipt.exit_code,expectedCode,'native actual exit');same(receipt.wrapper_exit_code,expectedCode,'actual wrapper exit');
  same(receipt.timeout_seconds,timeout,'explicit deadline');same(receipt.stdin,'DEVNULL','stdin role');
  for(const k of ['spawned','streams_complete','new_owned_session_requested'])same(receipt[k],true,'successful terminal '+k);
  for(const k of ['timed_out','interrupted'])same(receipt[k],false,'no unsuccessful native flag');
  same(receipt.failure,null,'no native failure');same(receipt.status,'COMPLETED','completed actual command');
  need(Number.isInteger(receipt.pid)&&receipt.pid>0,'actual positive native pid');
  same(receipt.process_group_settlement,{native_returncode:expectedCode,owned_pgid:receipt.pid,owned_sid:receipt.pid,quiescent:true,remaining_members:[],signals:[]},'whole settled owned group');
  need(receipt.ended_epoch>=receipt.started_epoch,'native nonnegative time');
  need(Math.abs(Date.parse(receipt.started_utc)/1000-receipt.started_epoch)<0.01&&Math.abs(Date.parse(receipt.ended_utc)/1000-receipt.ended_epoch)<0.01,'actual UTC/epoch correspondence');
  const stdout=read(dir+'/stdout.raw'),stderr=read(dir+'/stderr.raw');
  same(pin(stdout),receipt.stdout,'all raw stdout bytes');same(pin(stderr),receipt.stderr,'all raw stderr bytes');same(receipt.stderr,emptyPin,'whole empty stderr');
  return {label,receipt,stdout};
}
const rootCommand=native(ENTRY,entryResult.commands[0],outerArgv,0,300,ROOT);
same(strictJSON(rootCommand.stdout),{status:'PASS_PREPARATION_ONLY',errors:[],output:DISC,seal:{manifest:coverage.discovery.seal,payloads:58}},'entire saved preparer summary');
coverage.native=[];const rawCommands={};
for(let i=0;i<12;i++){
  const label=wantedLabels[i];let argv,code=0,cwd=ROOT;
  if(i<3)argv=['/usr/bin/cmp','--',PREP+'/'+sourceNames[i],DISC+'/source_snapshots/'+sourceNames[i]];
  else if(i<6){code=1;argv=['/usr/bin/diff','-u','--',QA+'p211_runtime_preparation/'+oldNames[i-3],PREP+'/'+sourceNames[i-3]];}
  else if(i<10){const tag=tags[i-6],cache=DISC+'/never_created_probe_'+tag+'_cache';if(tag==='child')cwd=DISC+'/empty_probe_capsule';argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+cache,PREP+'/p212_runtime.py','probe',tag,cache,cwd,CONTROL+'/APPROVAL.json',digest];}
  else argv=['/usr/bin/ldd',...lock.ldd_targets];
  const out=native(DISC,result.commands[i],argv,code,60,cwd);rawCommands[label]=out;
  need(out.receipt.started_epoch>=rootCommand.receipt.started_epoch&&out.receipt.ended_epoch<=rootCommand.receipt.ended_epoch,'native command within actual outer lifetime');
  if(i)need(out.receipt.started_epoch>=result.commands[i-1].ended_epoch,'actual sequential native order');
  if(i<3){same(out.stdout.length,0,'actual snapshot cmp empty');need(read(PREP+'/'+sourceNames[i]).equals(read(DISC+'/source_snapshots/'+sourceNames[i])),'whole actual source snapshot bytes');}
  coverage.native.push({label,exit_code:code,pid:out.receipt.pid,stdout:out.receipt.stdout,stderr:out.receipt.stderr});
}
function patchDiff(oldRaw,newRaw,diffRaw,oldName,newName){
  const lines=diffRaw.toString('utf8').split('\n');need(lines[0].startsWith('--- '+oldName+'\t')&&lines[1].startsWith('+++ '+newName+'\t'),'native exact source lineage headers');
  const orig=oldRaw.toString('utf8').split('\n');same(orig.pop(),'','complete old source LF');let pos=0,out=[],hunks=0;
  for(let i=2;i<lines.length;){if(!lines[i]){i++;continue;}const m=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@/.exec(lines[i++]);need(m,'complete unified diff hunk');hunks++;
    const start=Number(m[1])-1;out.push(...orig.slice(pos,start));pos=start;let removed=0,added=0;
    while(i<lines.length&&!lines[i].startsWith('@@ ')){const l=lines[i++];if(l==='')continue;need([' ','+','-'].includes(l[0]),'whole ordinary diff body');
      if(l[0]!=='+'){same(l.slice(1),orig[pos++],'old native diff byte-line');removed++;}if(l[0]!=='-'){out.push(l.slice(1));added++;}}
    same(removed,Number(m[2]||1),'whole old hunk');same(added,Number(m[4]||1),'whole new hunk');
  }
  out.push(...orig.slice(pos));need(Buffer.from(out.join('\n')+'\n').equals(newRaw),'exact source reconstruction from actual complete native diff');return hunks;
}
coverage.source_diffs=[];
for(let i=0;i<3;i++){const old=QA+'p211_runtime_preparation/'+oldNames[i],cur=PREP+'/'+sourceNames[i];coverage.source_diffs.push({old,source:cur,hunks:patchDiff(read(old),read(cur),rawCommands['01_source_diff_'+i].stdout,old,cur)});}
const settings=obj(DISC+'/PREPARER_SETTINGS.json'),probes=tags.map(t=>strictJSON(rawCommands['02_probe_'+t].stdout));
const config=lock.configuration;
for(const row of probes){same(row.configuration,config,'whole four-layer configuration equality');same(row.declared_imports,imports,'whole probe declaration');same(row.status,'IMPORT_ONLY_NO_SCIENTIFIC_SOURCE_READ','actual non-science probe status');}
const sampleKeys=['LC_CTYPE','argv','cache_lexists','cwd','default_encoding','environment','executable','filesystem_encoding','filesystem_errors','flags','interpreter_argv','mapped_files','modules','preferred_encoding','proc_maps','proc_maps_bytes','proc_maps_sha256','pycache_prefix','scope','stderr_encoding','stdin_encoding','stdout_encoding','sys_path','version','volatile_proc_maps_not_an_immutable_input'];
const flags='sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=1, no_user_site=1, no_site=1, ignore_environment=1, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=1, dev_mode=False, utf8_mode=0, warn_default_encoding=0, int_max_str_digits=-1)';
function sample(s,argv,cwd,cache,project){
  names(Object.keys(s),sampleKeys,'every actual sample field');
  same(s.argv,argv.slice(6),'actual Python sys.argv');same(s.interpreter_argv,argv,'actual original interpreter argv');same(s.cwd,cwd,'sample exact cwd');same(s.pycache_prefix,cache,'sample cache prefix');same(s.cache_lexists,false,'sample cache absent');
  same(s.environment,ENV,'whole sample ENV4');same(s.executable,'/usr/bin/python3.10','exact sampled interpreter');same(s.flags,flags,'all sampled flags');
  same(s.sys_path,['/usr/lib/python310.zip','/usr/lib/python3.10','/usr/lib/python3.10/lib-dynload'],'whole isolated source path');
  same(s.version,'3.10.12 (main, Mar  3 2026, 11:56:32) [GCC 11.4.0]','sampled binary version string');
  for(const k of ['default_encoding','filesystem_encoding','stdin_encoding','stdout_encoding','stderr_encoding'])same(s[k],'utf-8','actual encoding '+k);
  same(s.filesystem_errors,'surrogateescape','filesystem errors');same(s.preferred_encoding,'UTF-8','preferred encoding');same(s.LC_CTYPE,'C.UTF-8','actual locale');
  same(s.volatile_proc_maps_not_an_immutable_input,true,'maps limitation retained');
  same(s.scope,'file-backed module/map sample, not continuous or OS syscall tracing','sample boundary');
  const raw=Buffer.from(s.proc_maps);same(pin(raw),{bytes:s.proc_maps_bytes,sha256:s.proc_maps_sha256},'whole original proc-map bytes');
  const mapped=new Set();for(const line of s.proc_maps.trimEnd().split('\n')){
    const m=/^([0-9a-f]+)-([0-9a-f]+)\s+([rwxps-]{4})\s+([0-9a-f]+)\s+([0-9a-f]+:[0-9a-f]+)\s+(\d+)(?:\s+(.*))?$/.exec(line);need(m,'complete original maps line');
    need(BigInt('0x'+m[2])>BigInt('0x'+m[1]),'actual maps nonempty range');const p=m[7];if(p&&p.startsWith('/')){need(!p.endsWith(' (deleted)'),'no deleted mapped file');need(hostAllowed.has(p)||p.startsWith(QA),'mapped known local/host file');mapped.add(fs.realpathSync(p));}
  }
  names(Object.keys(s.mapped_files),mapped,'complete actual file-backed maps');
  for(const[p,k]of Object.entries(s.mapped_files)){need(Object.hasOwn(rb,p),'every actual mapped file in new key');same(k,bytePin(rb[p]),'actual mapped bytes match lock');richCheck(p,rb[p]);}
  for(const[n,k]of Object.entries(s.modules)){names(Object.keys(k),['path','bytes','sha256'],'full module record shape');need(Object.hasOwn(rb,k.path),'all file-backed modules keyed');same(bytePin(k),bytePin(rb[k.path]),'actual module bytes match lock');
    need(!/\.(pyc|pyo)$/.test(k.path),'no loaded bytecode');if(k.path.startsWith(ROOT+'/'))need(project.includes(k.path),'only allowed infrastructure project module');}
  return {modules:Object.keys(s.modules).length,mapped_files:Object.keys(s.mapped_files).length,proc_maps:pin(raw)};
}
coverage.samples=[];
for(let i=0;i<4;i++){
  const row=probes[i],tag=tags[i],cache=DISC+'/never_created_probe_'+tag+'_cache',cwd=tag==='child'?DISC+'/empty_probe_capsule':ROOT;
  names(Object.keys(row),['configuration','declared_imports','layer','sample','status'],'complete probe object fields');same(row.layer,tag,'actual exact layer');
  coverage.samples.push({layer:tag,...sample(row.sample,rawCommands['02_probe_'+tag].receipt.argv,cwd,cache,[PREP+'/p212_runtime.py',PREP+'/runtime_core.py'])});
  same(Object.keys(row.sample.modules).length,61,'whole actual61 file-backed modules');
  for(const name of ['fractions','decimal','numbers','_decimal'])need(Object.hasOwn(row.sample.modules,name),'actual selected decimal role '+name);
  need(!Object.hasOwn(row.sample.modules,'_pydecimal'),'no observed inactive fallback');
  if(i){same(row.sample.modules,probes[0].sample.modules,'same full module byte-map all roles');same(row.sample.mapped_files,probes[0].sample.mapped_files,'same full file-backed map pins all roles');}
}
names(Object.keys(settings),['argv','cache','cwd','environment','flags','orig_argv','sample','scope'],'entire preparer settings fields');
same(settings.argv,preparerArgv.slice(6),'preparer argv');same(settings.orig_argv,preparerArgv,'preparer actual original argv');
same(settings.environment,ENV,'preparer ENV4');same(settings.flags,flags,'preparer flags');same(settings.cwd,ROOT,'preparer cwd');same(settings.cache,DISC+'/never_created_preparer_cache','preparer cache');
coverage.preparer_sample=sample(settings.sample,preparerArgv,ROOT,settings.cache,sourceNames.map(n=>PREP+'/'+n));
// Python Path.resolve(strict=False) behavior for this exact declared state scope.
function resolveLoose(input){
  let todo=abs(input).split('/').filter(Boolean),done=[],links=0;
  while(todo.length){const n=todo.shift();if(n==='.')continue;if(n==='..'){done.pop();continue;}
    const p='/'+[...done,n].join('/');let s;try{s=fs.lstatSync(p);}catch(e){if(e.code!=='ENOENT'&&e.code!=='ENOTDIR')throw e;}
    if(s&&s.isSymbolicLink()){need(++links<=40,'no symlink loop');const target=fs.readlinkSync(p);if(target.startsWith('/'))done=[];todo=target.split('/').filter(Boolean).concat(todo);}else done.push(n);}
  return '/'+done.join('/');
}
function pathState(p,withBytes){
  abs(p);let ls=null,st=null;try{ls=fs.lstatSync(p);}catch(e){if(e.code!=='ENOENT'&&e.code!=='ENOTDIR')throw e;}
  try{st=fs.statSync(p);}catch(e){if(e.code!=='ENOENT'&&e.code!=='ENOTDIR')throw e;}
  const q={lexists:ls!==null,exists:st!==null,is_file:!!st?.isFile(),is_dir:!!st?.isDirectory(),is_character_device:!!st?.isCharacterDevice(),resolved:resolveLoose(p),symlink:ls?.isSymbolicLink()?fs.readlinkSync(p):null};
  if(q.is_character_device){const d=BigInt(st.rdev);q.character_device={major:Number(((d>>8n)&0xfffn)|((d>>32n)&0xfffff000n)),minor:Number((d&0xffn)|((d>>12n)&0xffffff00n)),mode:st.mode};}
  if(withBytes&&q.is_file){hostAllowed.add(p);Object.assign(q,bytePin(pin(read(p))));}
  return q;
}
function stateCheck(p,wanted,withBytes){
  const q=pathState(p,withBytes);same(q,wanted,'complete current path state '+p);
  const role=withBytes?'with_bytes':'without_bytes';
  if(stateInputs[p]?.[role])same(stateInputs[p][role],q,'same state interpretation');
  (stateInputs[p] ||= {})[role]=q;
}
same(Object.keys(config.paths).length,69,'whole69 config paths');
same(Object.keys(config.memberships).length,5,'whole5 membership scopes');
for(const[p,v]of Object.entries(config.paths))stateCheck(p,v,true);
let memberCount=0;
for(const[d,v]of Object.entries(config.memberships)){
  names(Object.keys(v),['directory','members'],'whole membership fields');stateCheck(d,v.directory,false);
  const actual=v.directory.is_dir?fs.readdirSync(d).sort():[];names(actual,Object.keys(v.members),'entire direct membership '+d);
  for(const[n,q]of Object.entries(v.members)){need(path.posix.basename(n)===n,'literal member');stateCheck(d+'/'+n,q,false);memberCount++;}
}
same(memberCount,292,'all292 declared direct members');
same(Object.keys(lock.loader_search_directory_states).length,9,'whole9 loader-state roles');
const loaderLines=read('/etc/ld.so.conf').toString('utf8').split('\n').map(s=>s.trim()).filter(s=>s&&!s.startsWith('#'));
same(loaderLines,['include /etc/ld.so.conf.d/*.conf'],'actual supported loader include');
const loaderNames=new Set();
for(const p of Object.keys(config.paths))if(path.posix.dirname(p)==='/etc/ld.so.conf.d'&&config.paths[p].is_file){
  for(const line of read(p).toString('utf8').split('\n')){const text=line.split('#')[0].trim();if(!text)continue;need(text.startsWith('/')&&!/[*?\[\]\t ]/.test(text),'actual bounded loader directive');loaderNames.add(text);}
}
names(loaderNames,Object.keys(lock.loader_search_directory_states),'whole actual loader directive targets');
for(const[p,q]of Object.entries(lock.loader_search_directory_states))stateCheck(p,q,false);
coverage.configuration={paths:69,membership_directories:5,membership_entries:292,loader_directories:9,device:config.paths['/dev/null'].character_device};
function linkage(raw){
  const groups={};let current=null;
  for(const line of raw.toString('utf8').trimEnd().split('\n')){
    const head=/^(\/[^:]+):$/.exec(line);
    if(head){current=head[1];need(!Object.hasOwn(groups,current),'unique ldd target');groups[current]={libraries:{},loader:null,vdso:false,statically_linked:false};continue;}
    need(current,'ldd body has target');const g=groups[current],s=line.trim();let m;
    if((m=/^(\S+) => (\/\S+) \(0x[0-9a-f]+\)$/.exec(s))){need(!Object.hasOwn(g.libraries,m[1]),'unique ldd soname');g.libraries[m[1]]=m[2];}
    else if((m=/^(\/\S+) \(0x[0-9a-f]+\)$/.exec(s))){same(g.loader,null,'one loader');g.loader=m[1];}
    else if(/^linux-vdso\.so\.1 \(0x[0-9a-f]+\)$/.test(s)){same(g.vdso,false,'one vdso');g.vdso=true;}
    else {same(s,'statically linked','fully understood ldd output line');g.statically_linked=true;}
  }
  names(Object.keys(groups),lock.ldd_targets,'all exact ldd target sections');
  const all=new Set();for(const g of Object.values(groups)){for(const p of Object.values(g.libraries))all.add(p);if(g.loader)all.add(g.loader);}
  names(all,lock.ldd_paths,'all exact old/new ldd dependency paths');return groups;
}
const lddBefore=linkage(rawCommands['03_ldd_before'].stdout),lddAfter=linkage(rawCommands['04_ldd_after'].stdout);
same(lddBefore,lddAfter,'whole normalized linkage including per-target roles, not raw ASLR bytes');
same(lock.ldd_targets.length,9,'actual9 ELF targets');same(lock.ldd_paths.length,8,'actual8 lexical linked dependencies');
const nativeFiles=['/usr/bin/python3.10','/usr/bin/cmp','/usr/bin/env','/usr/bin/ldd','/bin/bash','/bin/sh'];
const expectedFiles=new Set([...nativeFiles,'/usr/bin/diff']);
for(const s of [settings.sample,...probes.map(r=>r.sample)]){for(const p of Object.keys(s.mapped_files))expectedFiles.add(p);for(const m of Object.values(s.modules))expectedFiles.add(m.path);}
for(const[p,v]of Object.entries(config.paths))if(v.is_file)expectedFiles.add(p);
const expectedTargets=[...new Set([...nativeFiles.filter(p=>p!=='/usr/bin/ldd'),'/usr/bin/diff',...[...expectedFiles].filter(p=>p.startsWith('/usr/lib/python3.10/')&&p.endsWith('.so'))])].sort();
same(lock.ldd_targets,expectedTargets,'exact derivation of complete ELF target set');
for(const p of lock.ldd_paths)expectedFiles.add(p);for(const p of [...expectedFiles])expectedFiles.add(fs.realpathSync(p));
names(expectedFiles,Object.keys(rb),'exact runtime key reconstructed from persisted samples/config/native/linkage and aliases');
const elfRecord=obj(OWN+'/ELF_NATIVE.json');same(elfRecord.result.exit_code,0,'actual independent static ELF query exit');
const elf={};let node=null;
for(const line of elfRecord.result.output.split('\n')){const h=/^File: (\/.+)$/.exec(line);if(h){node=h[1];elf[node]={needed:[],soname:null,rpath:null,runpath:null};continue;}
  let m;if(node&&(m=/\(NEEDED\).*\[([^\]]+)\]/.exec(line)))elf[node].needed.push(m[1]);
  if(node&&(m=/\(SONAME\).*\[([^\]]+)\]/.exec(line)))elf[node].soname=m[1];
  if(node&&(m=/\((RPATH|RUNPATH)\).*\[([^\]]+)\]/.exec(line)))elf[node][m[1].toLowerCase()]=m[2];
}
names(Object.keys(elf),[...lock.ldd_targets,...lock.ldd_paths],'whole17 independently read dynamic tables');
const sonames={};for(const[p,g]of Object.entries(elf))if(g.soname){need(!Object.hasOwn(sonames,g.soname),'unique keyed SONAME');sonames[g.soname]=p;}
for(const[p,g]of Object.entries(elf)){need(rb[p],'all actual ELF targets keyed');same(g.rpath,null,'no unreviewed RPATH');same(g.runpath,null,'no unreviewed RUNPATH');for(const soname of g.needed)need(Object.hasOwn(sonames,soname),'complete finite DT_NEEDED closure '+soname);}
same(elf['/usr/lib/python3.10/lib-dynload/_decimal.cpython-310-x86_64-linux-gnu.so'].needed,['libmpdec.so.3','libc.so.6'],'actual C decimal direct linkage');
same(elf['/usr/lib/python3.10/lib-dynload/_json.cpython-310-x86_64-linux-gnu.so'].needed,[],'_json has no DT_NEEDED, not a standalone executable assertion');
coverage.ELF={targets:9,linked_paths:8,dynamic_tables:17,graph:elf,raw_ldd_byte_equality_claimed:false};
for(const p of staticExtras)read(p);
for(const p of [ROOT+'/.agents/skills/symbolic-dynamics-research/SKILL.md',ROOT+'/docs/research_state/WORKFLOW.md',QA+'p212_runtime_source_root_reception01/RECEPTION.md',PREP+'/PLAN.md',PREP+'/BINDING_CONTRACT.md',PREP+'/INTERFACE.json'])read(p);
// Pin all source-preparation payloads as opaque bytes; do not inspect scientific
// source text embedded in old documentary archives or import any submitted code.
coverage.preparation=sealed(PREP,{bytes:1262,sha256:'c78360b5be2c6f82bf7e8429700d381d800e95c693a6d98e2eac99f698c2ba78'},15);
const absent=[DISC+'/never_created_preparer_cache',...tags.map(t=>DISC+'/never_created_probe_'+t+'_cache'),
  ROOT+'/papers/212-closed-pointer-orbits/CANONICAL.json',ROOT+'/papers/212-closed-pointer-orbits/canonical.stdout.json'];
for(const p of absent){const s=pathState(p,false);same(s.lexists,false,'continued exact absence '+p);}
same(fs.readdirSync(DISC+'/empty_probe_capsule'),[],'genuinely empty child import capsule');
read(OWN+'/receive_discovery.js');
for(const p of Object.keys(pins))read(p);
for(const[p,roles]of Object.entries(stateInputs))for(const[role,v]of Object.entries(roles))same(pathState(p,role==='with_bytes'),v,'complete final state recheck '+p);
coverage.boundaries={all_five_cache_prefixes_absent:true,canonical_and_historical_spelling_absent:true,scientific_source_files_read:0,submitted_sources_executed_by_auditor:0,ambient_environment_read:false,host_dependency_files_compared:true,late_preparer_sample_not_separately_archived:true,discovery_not_prelocked_science:true};
console.log(JSON.stringify({status:'PASS_INDEPENDENT_DOCUMENTARY_IMPORT_DISCOVERY_RECEPTION_NOT_SCIENCE_AUTHORITY',checks,coverage,input_files:Object.keys(pins).length,state_paths:Object.keys(stateInputs).length,input_pins:Object.fromEntries(Object.keys(pins).sort().map(p=>[p,pins[p]])),complete_current_state_key:stateInputs}));
