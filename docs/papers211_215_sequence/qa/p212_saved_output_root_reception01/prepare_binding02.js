'use strict';
// Root exact failure/delta reception and a separately scoped new data binding.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),a=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',OWN=ROOT+'/docs/papers211_215_sequence/qa/p212_saved_output_root_reception01';
const inputs={};let checks=0;
function need(x,s){checks++;a.ok(x,s);}
function same(x,y,s){checks++;a.deepStrictEqual(x,y,s);}
const val=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p,k){need(path.normalize(p)===p&&p.startsWith('/'),'literal input');const l=fs.lstatSync(p);need(fs.statSync(p).isFile(),'ordinary byte input');const b=fs.readFileSync(p),v={...val(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};if(inputs[p])same(v,inputs[p],'stable full byte key');if(k)for(const f of ['sha256','bytes','resolved','symlink'])if(Object.hasOwn(k,f))same(v[f],k[f],'exact supplied '+f);inputs[p]=v;return b;}
const obj=p=>JSON.parse(read(p));
function state(p){let l;try{l=fs.lstatSync(p);}catch(e){if(e.code==='ENOENT'||e.code==='ENOTDIR')return {lexists:false};throw e;}const s=fs.statSync(p),r={lexists:true,is_file:s.isFile(),is_directory:s.isDirectory(),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};if(s.isFile())Object.assign(r,val(read(p)));return r;}
function absent(p){same(state(p),{lexists:false},'fresh output only');}
function write(n,v){fs.writeFileSync(OWN+'/'+n,JSON.stringify(v,null,2)+'\n',{flag:'wx'});read(OWN+'/'+n);}
const old=obj(OWN+'/RUNTIME_BINDING.json'),oldLock=obj(old.node_lock.path),failed=OWN+'/initial01';
for(const p of [OWN+'/initial02',OWN+'/RUNTIME_BINDING02.json',OWN+'/NODE_RUNTIME_LOCK02.json',ROOT+'/papers/212-closed-pointer-orbits/CANONICAL.json',ROOT+'/papers/212-closed-pointer-orbits/canonical.stdout.json'])absent(p);
for(const[p,k]of Object.entries({...old.controlled_python_files,...oldLock.files,...old.input_pins}))read(p,k);
for(const[p,k]of Object.entries(oldLock.configuration))same(state(p),k,'unchanged whole selected Node configuration');
const rows=read(failed+'/SHA256SUMS').toString().trimEnd().split('\n'),names=[];
for(const line of rows){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);need(m&&!m[2].startsWith('/')&&!m[2].split('/').some(v=>['','.','..'].includes(v))&&!names.includes(m[2]),'safe complete old failure manifest');names.push(m[2]);read(failed+'/'+m[2],{sha256:m[1]});}
same(names.length,21,'all actual failed payloads');
const actual=[];function walk(p){for(const n of fs.readdirSync(p)){const f=p+'/'+n,s=fs.lstatSync(f);need(!s.isSymbolicLink(),'no failed artifact alias');if(s.isDirectory())walk(f);else{need(s.isFile(),'ordinary artifact');actual.push(f.slice(failed.length+1));}}}walk(failed);same(actual.sort(),[...names,'SHA256SUMS'].sort(),'whole immutable failed tree');
const result=obj(failed+'/RESULT.json'),tool=obj(OWN+'/FAILED_APPLICATION01_NATIVE.json'),parts=[tool.result,...tool.polls.map(x=>x.result)];same(parts.at(-1).exit_code,1,'actual failed outer exit');
const returned=JSON.parse(parts.map(x=>x.output).join(''));same(returned.status,result.status,'actual failed result status');same(result.status,'FAIL_PRESERVED','failure not accepted');same(returned.seal,{manifest:val(read(failed+'/SHA256SUMS')),payloads:21},'actual complete failure seal');
same(result.commands.map(x=>x.label),['01_ldd_before','02_saved_output','03_ldd_after'],'all three actual failed-attempt native records');
for(const command of result.commands){const p=failed+'/commands/'+command.label,r=obj(p+'/RECEIPT.json');same(Object.fromEntries(Object.entries(command).filter(([k])=>k!=='label')),r,'entire actual native/result record');for(const stream of ['stdout','stderr'])read(p+'/'+stream+'.raw',r[stream]);same(r.streams_complete,true,'complete original native streams');same(r.process_group_settlement.quiescent,true,'actual owned group closed');}
same(read(failed+'/commands/02_saved_output/stdout.raw').length,0,'no successful old semantic receipt');
const err=read(failed+'/commands/02_saved_output/stderr.raw').toString();need(err.includes('Error: receiver exported filesystem write forbidden')&&err.includes('SyncWriteStream._write')&&err.includes('receive_saved_output.js:832:18'),'actual precise standard-stream failure');
const events=obj(failed+'/node_capture/EXPORTED_FS_AND_MODULE_EVENTS.json');same(events.events.filter(x=>x.denied),[{operation:'writeSync',denied:true}],'sole actually denied ordinary-write classification');
same(events.loads.map(x=>x.request),[old.receiver,'node:fs','node:crypto','node:path'],'actual exact four Module loads');
same([...new Set(events.events.filter(x=>x.path).map(x=>x.path))].sort(),[old.receiver,old.binding,old.parameters,old.saved_stdout].sort(),'actual only four source/data read paths');
const oldJs=read(OWN+'/node_preload04.js').toString(),newJs=read(OWN+'/node_preload05.js').toString();
const previous="  for(const op of ['writeFileSync','appendFileSync','writeSync','createWriteStream','unlinkSync','rmSync','renameSync','mkdirSync','rmdirSync','copyFileSync'])";
const next="  fs.writeSync=function(fd,...args){\n    if(internalRead)return original.writeSync(fd,...args);\n    need(fd===1||fd===2,'only preowned stdout/stderr stream descriptors may be written');\n    const written=original.writeSync(fd,...args);events.push({operation:'writeSync',descriptor:fd,native_stream:fd===1?'stdout':'stderr',bytes_written:written});return written;\n  };\n  for(const op of ['writeFileSync','appendFileSync','createWriteStream','unlinkSync','rmSync','renameSync','mkdirSync','rmdirSync','copyFileSync'])";
need(oldJs.includes(previous),'exact unique old guard source');
same(newJs,oldJs.replace("OWN+'/RUNTIME_BINDING.json'","OWN+'/RUNTIME_BINDING02.json'").replace("OWN+'/initial01/node_capture'","OWN+'/initial02/node_capture'").replace(previous,next),'entire source delta: two locators plus stdout/stderr descriptor guard');
const oldPy=read(OWN+'/run_semantics.py').toString(),newPy=read(OWN+'/run_semantics02.py').toString();
same(newPy,oldPy.replace("OWN/'initial01'","OWN/'initial02'").replaceAll("OWN/'run_semantics.py'","OWN/'run_semantics02.py'").replace("OWN/'RUNTIME_BINDING.json'","OWN/'RUNTIME_BINDING02.json'"),'entire controller delta is three literal roles only');
const lock=structuredClone(oldLock);lock.source_options=['--require',OWN+'/node_preload05.js'];same({...lock,source_options:oldLock.source_options},oldLock,'entire unchanged Node dependency object except explicit new preload option');write('NODE_RUNTIME_LOCK02.json',lock);
const b=structuredClone(old);b.attempt=OWN+'/initial02';b.capture=b.attempt+'/node_capture';b.preload=OWN+'/node_preload05.js';b.node_lock={path:OWN+'/NODE_RUNTIME_LOCK02.json',pin:val(read(OWN+'/NODE_RUNTIME_LOCK02.json'))};
for(const p of [OWN+'/node_preload05.js',OWN+'/run_semantics02.py',OWN+'/prepare_binding02.js',OWN+'/APPLICATION01_FAILURE_AND_AUTHORITY02.md',OWN+'/FAILED_APPLICATION01_NATIVE.json',OWN+'/RUNTIME_BINDING.json',OWN+'/NODE_RUNTIME_LOCK02.json',failed+'/SHA256SUMS']){read(p);b.input_pins[p]=inputs[p];}
b.authority_record=OWN+'/APPLICATION01_FAILURE_AND_AUTHORITY02.md';
for(const p of Object.keys(inputs))read(p,inputs[p]);for(const[p,k]of Object.entries(lock.configuration))same(state(p),k,'whole configuration unchanged before reapplication binding');
write('RUNTIME_BINDING02.json',b);write('PREPARATION_INPUTS02.json',inputs);
console.log(JSON.stringify({status:'ROOT_SEPARATELY_BOUND_SECOND_SAVED_OUTPUT_APPLICATION_NOT_EXECUTED',checks,input_paths:Object.keys(inputs).length,old_failure_payloads:21,submitted_receiver_changed:false,science_output_changed:false,node_host_key_changed:false,
  runtime_binding:inputs[OWN+'/RUNTIME_BINDING02.json'],semantic_binding:inputs[old.binding],producer_invocations:0,canonical_adopted:false}));
