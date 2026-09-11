'use strict';
// Root original-evidence reception. No submitted source or producer is run.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),a=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',OWN=ROOT+'/docs/papers211_215_sequence/qa/p212_saved_output_root_reception01',RUN=OWN+'/initial02';
const inputs={};let checks=0;
function need(x,s){checks++;a.ok(x,s);}
function same(x,y,s){checks++;a.deepStrictEqual(x,y,s);}
const val=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p,k){need(path.normalize(p)===p&&p.startsWith('/'),'literal original');const l=fs.lstatSync(p);need(fs.statSync(p).isFile(),'ordinary byte original');const b=fs.readFileSync(p),v={...val(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};if(inputs[p])same(v,inputs[p],'stable full key');if(k)for(const f of ['sha256','bytes','resolved','symlink'])if(Object.hasOwn(k,f))same(v[f],k[f],'supplied exact '+f);inputs[p]=v;return b;}
const obj=p=>JSON.parse(read(p));
function state(p){let l;try{l=fs.lstatSync(p);}catch(e){if(e.code==='ENOENT'||e.code==='ENOTDIR')return {lexists:false};throw e;}const s=fs.statSync(p),r={lexists:true,is_file:s.isFile(),is_directory:s.isDirectory(),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};if(s.isFile())Object.assign(r,val(read(p)));return r;}
const rb=OWN+'/RUNTIME_BINDING02.json',b=obj(rb),lock=obj(b.node_lock.path),binding=obj(b.binding),r=obj(RUN+'/RESULT.json'),tool=obj(OWN+'/APPLICATION02_NATIVE.json');
same(r.status,'CAPTURED_COMPLETE_SAVED_OUTPUT_SEMANTICS_PENDING_ROOT_RECEPTION','actual successful received candidate');same(r.errors,[],'no actual receiver/controller error');
const before=obj(RUN+'/INPUTS_BEFORE.json'),after=obj(RUN+'/INPUTS_AFTER.json');same(before,after,'whole actual root pre/post key');
const expected={...b.controlled_python_files,...lock.files,...b.input_pins,[rb]:inputs[rb]};same(before,expected,'entire expected actual root input set');
for(const[p,k]of Object.entries(before))read(p,k);
need(read(RUN+'/EXECUTED_CONTROLLER.py').equals(read(OWN+'/run_semantics02.py')),'actual executed controller byte snapshot');need(read(RUN+'/RUNTIME_BINDING_ORIGINAL.json').equals(read(rb)),'whole actual binding snapshot');
const seal=read(RUN+'/SHA256SUMS').toString(),names=[];need(seal.endsWith('\n'),'entire manifest LF');
for(const line of seal.trimEnd().split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);need(m&&!m[2].startsWith('/')&&!m[2].split('/').some(v=>['','.','..'].includes(v))&&!names.includes(m[2]),'complete safe unique seal');names.push(m[2]);read(RUN+'/'+m[2],{sha256:m[1]});}
same(names.length,21,'whole successful execution payloads');
const actual=[],dirs=['.'];function walk(p){for(const n of fs.readdirSync(p)){const f=p+'/'+n,l=fs.lstatSync(f);need(!l.isSymbolicLink(),'physical artifact entry');if(l.isDirectory()){dirs.push(f.slice(RUN.length+1));walk(f);}else{need(l.isFile(),'no special artifact');actual.push(f.slice(RUN.length+1));}}}walk(RUN);
same(actual.sort(),[...names,'SHA256SUMS'].sort(),'whole actual file inventory');same(dirs.sort(),['.','commands','commands/01_ldd_before','commands/02_saved_output','commands/03_ldd_after','node_capture'],'whole actual directory membership');
same(r.commands.map(x=>x.label),['01_ldd_before','02_saved_output','03_ldd_after'],'entire native order');let last=0;
const env={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};
for(const n of r.commands){
  const p=RUN+'/commands/'+n.label,c=obj(p+'/RECEIPT.json'),attempt=obj(p+'/ATTEMPT.json');same(Object.fromEntries(Object.entries(n).filter(([k])=>k!=='label')),c,'entire native/result row');
  same(attempt,{...Object.fromEntries(Object.keys(attempt).filter(k=>!['status','exit_code'].includes(k)).map(k=>[k,c[k]])),status:'ATTEMPTED',exit_code:null},'actual prespawn record');
  same(c.environment,env,'exact native ENV4');same(c.cwd,ROOT,'exact cwd');
  need(c.status==='COMPLETED'&&c.exit_code===0&&c.wrapper_exit_code===0&&c.spawned&&c.streams_complete&&!c.timed_out&&!c.interrupted&&c.failure===null,'actual successful fully closed native');
  same(c.process_group_settlement,{native_returncode:0,owned_pgid:c.pid,owned_sid:c.pid,quiescent:true,remaining_members:[],signals:[]},'entire owned native settlement');
  need(c.started_epoch>=last&&c.ended_epoch>=c.started_epoch&&c.ended_epoch-c.started_epoch<c.timeout_seconds,'actual native sequence/deadline');last=c.ended_epoch;
  for(const t of ['started','ended'])need(Math.abs(Date.parse(c[t+'_utc'])/1000-c[t+'_epoch'])<0.01,'actual UTC/epoch ordered samples');
  for(const stream of ['stdout','stderr'])read(p+'/'+stream+'.raw',c[stream]);same(c.stderr.bytes,0,'entire stderr empty');
  same(c.stdin,'DEVNULL','no uncontrolled stdin');same(c.new_owned_session_requested,true,'actual owned sessions');
  if(n.label==='02_saved_output')same(c.argv,['/usr/bin/env','-i',...Object.entries(env).map(([k,v])=>k+'='+v),'/usr/bin/node','--require',b.preload,b.receiver,'--binding',b.binding],'entire actual semantic native argv');
  else same(c.argv,['/usr/bin/ldd','/usr/bin/node'],'whole actual ELF target');
}
const reference=obj(OWN+'/NODE_LDD_DISCOVERY_NATIVE.json').result.output.replace(/\(0x[0-9a-f]+\)/g,'(ADDRESS)');
for(const n of ['01_ldd_before','03_ldd_after'])same(read(RUN+'/commands/'+n+'/stdout.raw').toString().replace(/\(0x[0-9a-f]+\)/g,'(ADDRESS)'),reference,'whole target linkage modulo load addresses, not raw equality');
const nb=obj(RUN+'/node_capture/BEFORE.json'),na=obj(RUN+'/node_capture/AFTER.json'),nr=obj(RUN+'/node_capture/RESULT.json'),events=obj(RUN+'/node_capture/EXPORTED_FS_AND_MODULE_EVENTS.json'),probe=obj(b.discovery.path).sample;
same(nb.source_inputs,b.input_pins,'complete preloaded source key');same(nr.source_inputs,b.input_pins,'complete returned preloaded source key');
same(nb.runtime_binding,val(read(rb)),'actual Node binding bytes');same(nr.status,'PASS_BOUNDED_NODE_RECEIVER_RUNTIME','actual Node exit capture');same(nr.errors,[],'no Node runtime error');same(nr.receiver_exit_code,0,'actual semantic exit');
same(nb.dependency_key,na.dependency_key,'entire actual Node before/after key');same(nb.dependency_key,{files:lock.files,configuration:lock.configuration},'whole prebound Node files/configuration');
for(const[p,k]of Object.entries(lock.configuration))same(state(p),k,'current whole selected configuration');
for(const s of [nb.sample,na.sample]){
  same(Object.keys(s).sort(),Object.keys(probe).sort(),'all sampled fields handled');
  for(const k of ['executable','versions','architecture','platform','cwd','environment','builtin_source_fingerprints','mapped_files'])same(s[k],probe[k],'whole stable actual Node '+k);
  same(s.argv,['/usr/bin/node',b.receiver,'--binding',b.binding],'whole actual sampled argv');same(s.exec_argv,['--require',b.preload],'actual sole preload');same(val(Buffer.from(s.proc_maps)),s.proc_maps_pin,'whole raw proc-map identity');
  const mapped=new Set();for(const line of s.proc_maps.trimEnd().split('\n')){const m=/^[0-9a-f]+-[0-9a-f]+\s+[rwxps-]+\s+[0-9a-f]+\s+[0-9a-f:]+\s+\d+(?:\s+(.*))?$/.exec(line);need(m,'every actual proc-map row');if(m[1]&&m[1].startsWith('/')){need(!m[1].endsWith(' (deleted)'),'no deleted file map');mapped.add(fs.realpathSync(m[1]));}}same([...mapped].sort(),Object.keys(s.mapped_files).sort(),'all actual file-backed maps');
  for(const entry of s.module_load_list){need(/^(NativeModule |Internal Binding )/.test(entry),'embedded Node role');if(entry.startsWith('NativeModule '))same(s.builtin_source_fingerprints[entry.slice(13)].type,'string','every actually loaded native module has prekeyed source');}
}
same(nb.sample.require_cache,[b.preload],'only preload before receiver');same(na.sample.require_cache,[b.preload,b.receiver].sort(),'only actual two commonJS source entries');
same(na.sample.module_load_list,[...nb.sample.module_load_list,'NativeModule internal/fs/sync_write_stream'],'exact lazy standard-output builtin addition, source prekeyed at discovery');
same(events.loads,[{request:b.receiver,is_main:true,parent:null},...['node:fs','node:crypto','node:path'].map(request=>({request,is_main:false,parent:b.receiver}))],'all actual module load events');
const allowed=[b.receiver,b.binding,b.parameters,b.saved_stdout].sort(),operations={},seen=new Set(),fd=new Set();let written=0;
for(const e of events.events){operations[e.operation]=(operations[e.operation]||0)+1;need(!e.denied,'no denied operation');if(e.operation==='writeSync'){same(Object.keys(e).sort(),['bytes_written','descriptor','native_stream','operation'],'all stream-write fields');same(e.descriptor,1,'only actual stdout output');same(e.native_stream,'stdout','actual native stream');need(Number.isSafeInteger(e.bytes_written)&&e.bytes_written>0,'actual written bytes');written+=e.bytes_written;}else{same(Object.keys(e).sort(),['descriptor','flags','operation','path'],'all read-event fields');need(allowed.includes(e.path),'every observed read in four exact inputs');seen.add(e.path);if(e.operation==='openSync')same(e.flags,131072,'actual O_RDONLY|O_NOFOLLOW flag');else same(e.flags,null,'no invented read flags');if(e.descriptor!==null){need(Number.isInteger(e.descriptor)&&e.descriptor>2,'owned read descriptor');if(e.operation==='fstatSync'||e.operation==='readFileSync')fd.add(e.descriptor);if(e.operation==='closeSync')fd.delete(e.descriptor);}}}
same([...seen].sort(),allowed,'all four observed source/data input paths');same(fd.size,0,'all observed read descriptors closed');
same(operations,{realpathSync:2,readFileSync:9,lstatSync:16,openSync:8,fstatSync:16,closeSync:8,writeSync:1},'complete sixty exported-fs events');
const raw=read(RUN+'/commands/02_saved_output/stdout.raw'),receipt=JSON.parse(raw);same(written,raw.length,'all standard-output write bytes equal native retained stream');same(r.receiver_receipt,receipt,'whole captured semantic receipt');
const semantic=obj(binding.saved_stdout.path);same(receipt.semantics.predicate_census,semantic.predicate_census,'all 46 census rows actually returned after complete semantic reconstruction');same(receipt.semantics.predicate_count,semantic.predicates.length,'all actual named predicate records');same(receipt.semantics.total_states,semantic.summary.state_count,'exact actual state total');
same(receipt.semantics.carriers,semantic.carriers.map(c=>({n:c.n,states:c.state_count,groups:c.groups.length,orbits:c.orbit_count,periods:c.period_set})),'entire compact actual carrier receipt');same(receipt.semantics.predicate_census.length,46,'all named census entries');same(receipt.semantics.predicate_census.reduce((s,x)=>s+x.checks,0),receipt.semantics.predicate_count,'entire predicate census totals');need(receipt.semantics.predicate_census.every(x=>x.failures===0),'no finite predicate failure');
same(receipt.inputs_before,receipt.inputs_after,'whole actual semantic before/after rich key');same(receipt.inputs_before.map(x=>x.path),[b.binding,b.receiver,b.parameters,b.saved_stdout],'four ordered semantic input roles');
for(const k of receipt.inputs_before){read(k.path,k);const s=fs.lstatSync(k.path,{bigint:true});same({...k,device:String(s.dev),inode:String(s.ino),mode:String(s.mode),size_bytes:String(s.size),link_count:String(s.nlink),mtime_ns:String(s.mtimeNs),ctime_ns:String(s.ctimeNs)},k,'entire current semantic nanosecond/stat key');}
same(receipt.binding_sha256,inputs[b.binding].sha256,'exact semantic binding');same(receipt.receiver_sha256,inputs[b.receiver].sha256,'actual submitted receiver source');same(receipt.saved_stdout_sha256,inputs[b.saved_stdout].sha256,'actual original scientific raw source');same(receipt.saved_stdout_bytes,inputs[b.saved_stdout].bytes,'entire saved scientific byte length');same(receipt.source_parameter_sha256,inputs[b.parameters].sha256,'actual unchanged parameters');
need(Number.isSafeInteger(receipt.semantic_checks)&&receipt.semantic_checks>0,'actual primitive semantic counter, not independent theorem count');
for(const k of ['scientific_producer_invocations','submitted_code_imports','canonical_accesses','filesystem_writes'])same(receipt[k],0,'exact receiver boundary '+k);
const parts=[tool.result,...tool.polls.map(x=>x.result)];same(parts.at(-1).exit_code,0,'actual successful product completion');same(tool.polls[0].request.session_id,tool.result.session_id,'real yielded native session');
same(JSON.parse(parts.map(x=>x.output).join('')),{attempt:RUN,canonical_adopted:false,errors:[],native_commands:3,scientific_producer_invocations:0,seal:{manifest:val(read(RUN+'/SHA256SUMS')),payloads:21},status:r.status},'whole actual product/output seal relation');
same(tool.request.cmd,'/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B '+OWN+'/run_semantics02.py '+rb+' '+inputs[rb].sha256,'entire actual root launch vector');
for(const n of ['CANONICAL.json','canonical.stdout.json'])same(state(ROOT+'/papers/212-closed-pointer-orbits/'+n),{lexists:false},'root reception before canonical adoption');
read(OWN+'/receive_execution.js');for(const p of Object.keys(inputs))read(p,inputs[p]);
fs.writeFileSync(OWN+'/EXECUTION_RECEPTION_INPUTS.json',JSON.stringify(inputs,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({status:'PASS_ROOT_COMPLETE_P212_INITIAL_SAVED_OUTPUT_SEMANTICS',checks,input_paths:Object.keys(inputs).length,runtime_payloads:21,native_commands:3,node_file_keys:10,node_configuration_paths:19,typed_builtin_entries:360,node_modules_before:nb.sample.module_load_list.length,node_modules_after:na.sample.module_load_list.length,exported_fs_events:events.events.length,
  actual_semantic_primitive_checks:receipt.semantic_checks,actual_named_predicates:receipt.semantics.predicate_count,actual_states:receipt.semantics.total_states,actual_carriers:receipt.semantics.carriers,actual_semantic_stdout:val(raw),saved_scientific_stdout:binding.saved_stdout,
  producer_invocations_in_reception:0,canonical_adopted:false,independent_manuscript_review:false,scope:'Root whole original/source/key/native reception of the actual successful author-side all-field saved-output reconstruction; no additional mathematical producer invocation.'}));
