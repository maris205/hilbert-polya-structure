'use strict';
// Root metadata/binding assembly only; no submitted semantic/scientific execution.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),a=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const OWN=QA+'p212_saved_output_root_reception01',PREP=QA+'p212_saved_output_semantic_preparation01';
const RUNTIME=QA+'p212_author_initial_runtime_reception01',PAPER=ROOT+'/papers/212-closed-pointer-orbits';
let checks=0;const inputs={};
function need(x,s){checks++;a.ok(x,s);}
function same(x,y,s){checks++;a.deepStrictEqual(x,y,s);}
const val=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p,k){
  need(path.normalize(p)===p&&p.startsWith('/'),'literal absolute byte input');
  const l=fs.lstatSync(p),s=fs.statSync(p);need(s.isFile(),'ordinary byte source');
  const b=fs.readFileSync(p),v={...val(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};
  if(inputs[p])same(v,inputs[p],'whole stable byte key');if(k)for(const f of ['bytes','sha256','resolved','symlink'])if(Object.hasOwn(k,f))same(v[f],k[f],'supplied full pin '+f);inputs[p]=v;return b;
}
const obj=p=>JSON.parse(read(p));
function state(p){
  let l;try{l=fs.lstatSync(p);}catch(e){if(e.code==='ENOENT'||e.code==='ENOTDIR')return {lexists:false};throw e;}
  const s=fs.statSync(p),r={lexists:true,is_file:s.isFile(),is_directory:s.isDirectory(),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};
  if(s.isFile())Object.assign(r,val(read(p)));return r;
}
function absent(p){same(state(p),{lexists:false},'exact absent output');}
function write(n,v){fs.writeFileSync(OWN+'/'+n,JSON.stringify(v,null,2)+'\n',{flag:'wx'});read(OWN+'/'+n);}
function manifest(base,name){
  const raw=read(base+'/'+name).toString();need(raw.endsWith('\n'),'full manifest LF');const names=[];
  for(const line of raw.trimEnd().split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);need(m&&!m[2].startsWith('/')&&!m[2].split('/').some(x=>['','.','..'].includes(x))&&!names.includes(m[2]),'safe unique manifest row');names.push(m[2]);read(base+'/'+m[2],{sha256:m[1]});}same(fs.readdirSync(base).sort(),[...names,name].sort(),'entire flat accepted package');return names;
}
for(const p of [OWN+'/BINDING.json',OWN+'/RUNTIME_BINDING.json',OWN+'/NODE_RUNTIME_LOCK.json',OWN+'/initial01',PAPER+'/CANONICAL.json',PAPER+'/canonical.stdout.json'])absent(p);
same(manifest(PREP,'MANIFEST.sha256').length,5,'complete submitted source package');
same(manifest(RUNTIME,'SHA256SUMS').length,14,'complete accepted runtime record reception');
const sr=obj(OWN+'/SOURCE_RESULT.json'),sn=obj(OWN+'/SOURCE_NATIVE.json');
same(sr,JSON.parse(sn.result.output),'actual complete successful source-reception output');same(sn.result.exit_code,0,'actual source reception completion');
for(const[p,k]of Object.entries(obj(OWN+'/SOURCE_INPUTS.json')))read(p,k);
const initial=obj(RUNTIME+'/RESULT.json');same(initial.actual_author_invocations_received,1,'exact one actual initial producer');
same(initial.raw_stdout.length,1,'one saved initial output');const saved=initial.raw_stdout[0];read(saved.path,saved);
const nodeProbe=obj(OWN+'/NODE_PROBE04.json'),native=obj(OWN+'/NODE_PROBE04_NATIVE.json');
const parts=[native.result,...native.polls.map(x=>x.result)];same(parts.at(-1).exit_code,0,'actual source04 import-probe completion');
same(JSON.parse(parts.map(x=>x.output).join('')),nodeProbe,'whole actual probe/result relation');
same(nodeProbe.status,'BUILTIN_ONLY_NODE_RUNTIME_PROBE_NO_RECEIVER','no submitted receiver in discovery');
same(nodeProbe.sample.argv,['/usr/bin/node',OWN+'/node_preload04.js','--probe'],'actual exact probe argv');
same(nodeProbe.sample.exec_argv,[],'no extra import-probe loader flags');
same(nodeProbe.sample.environment,{PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'},'cleared actual Node ENV4');
same(nodeProbe.sample.require_cache,[OWN+'/node_preload04.js'],'no receiver/pilot in actual probe');
same(Object.keys(nodeProbe.sample.builtin_source_fingerprints).length,360,'359 embedded source strings and one typed undefined entry');
same(nodeProbe.sample.builtin_source_fingerprints.configs,{type:'undefined'},'explicit undefined configs boundary');
for(const[k,v]of Object.entries(nodeProbe.sample.builtin_source_fingerprints))if(k!=='configs'){same(v.type,'string','every other native is source text');need(Number.isSafeInteger(v.bytes)&&/^[a-f0-9]{64}$/.test(v.sha256),'complete actual embedded source fingerprint');}
for(const[p,k]of Object.entries(nodeProbe.sample.mapped_files))read(p,k);
const ldd=obj(OWN+'/NODE_LDD_DISCOVERY_NATIVE.json');same(ldd.result.exit_code,0,'actual original Node linkage');
const linked=[...ldd.result.output.matchAll(/(\/[^\s()]+)/g)].map(m=>m[1]);
const nodeFiles={...nodeProbe.sample.mapped_files};for(const p of linked){read(p);nodeFiles[p]=inputs[p];const r=fs.realpathSync(p);read(r);nodeFiles[r]=inputs[r];}
same([...new Set(linked.map(p=>fs.realpathSync(p)))].sort(),Object.keys(nodeProbe.sample.mapped_files).filter(p=>p!=='/usr/bin/node').sort(),'all original target linkage versus eight actual maps');
const configPaths=new Set(['/etc/ld.so.cache','/etc/ld.so.preload','/etc/ld.so.conf','/etc/ssl/openssl.cnf','/usr/lib/ssl/openssl.cnf','/etc/localtime','/etc/locale.conf','/etc/default/locale','/usr/lib/locale/locale-archive','/usr/share/locale/locale.alias']);
for(const base of [OWN,PREP]){let p=base;while(true){configPaths.add(p+'/package.json');if(p==='/')break;p=path.dirname(p);if(p==='/'){configPaths.add('/package.json');break;}}}
const configuration=Object.fromEntries([...configPaths].sort().map(p=>[p,state(p)]));
const nodeLock={schema:'root-p212-bounded-node-saved-output-key-v1',files:nodeFiles,configuration,
  node_versions:nodeProbe.sample.versions,builtin_source_fingerprints:nodeProbe.sample.builtin_source_fingerprints,
  environment:nodeProbe.sample.environment,source_options:['--require',OWN+'/node_preload04.js'],
  scope:'Exact binary/ELF/builtin-source and bounded loader/configuration/package-ancestor key. Discrete probe and future exported-fs hooks, not complete OS/startup tracing.'};
write('NODE_RUNTIME_LOCK.json',nodeLock);
const receiver=PREP+'/receive_saved_output.js',parameters=PAPER+'/PARAMETERS.json';read(receiver,sr.receiver);read(parameters,{bytes:609,sha256:'0870d9de8a1e2dde2c568656ea69b39511ae3a8ebf992f787c6e5ae060ca4550'});
write('BINDING.json',{schema:'p212-saved-output-semantic-binding-v1',approved:true,role:'author',saved_stdout:saved,
  parameters:{path:parameters,bytes:inputs[parameters].bytes,sha256:inputs[parameters].sha256},
  receiver:{path:receiver,bytes:inputs[receiver].bytes,sha256:inputs[receiver].sha256}});
const pythonLock=obj(QA+'p212_runtime_discovery01/RUNTIME_LOCK.json');same(Object.keys(pythonLock.files).length,130,'whole inherited accepted Python dependency key');
for(const[p,k]of Object.entries(pythonLock.files))read(p,k);
const extra=[OWN+'/AUTHORITY.md',OWN+'/node_preload04.js',OWN+'/run_semantics.py',OWN+'/prepare_binding.js',OWN+'/NODE_RUNTIME_LOCK.json',OWN+'/BINDING.json',
  OWN+'/NODE_PROBE04.json',OWN+'/NODE_PROBE04_NATIVE.json',OWN+'/NODE_LDD_DISCOVERY_NATIVE.json',OWN+'/SOURCE_RESULT.json',OWN+'/SOURCE_NATIVE.json',OWN+'/SOURCE_INPUTS.json',
  OWN+'/NODE_PROBE01_CORRECTION.md',OWN+'/NODE_PROBE02_CORRECTION.md',OWN+'/PRELOAD04_SOURCE_DELTA.md',
  RUNTIME+'/RECEPTION.md',RUNTIME+'/RESULT.json',RUNTIME+'/SUPPLEMENT_RESULT.json',RUNTIME+'/SHA256SUMS',PREP+'/PLAN.md',PREP+'/MANIFEST.sha256',
  QA+'p212_runtime_preparation01/runtime_core.py',QA+'p212_runtime_discovery01/RUNTIME_LOCK.json',receiver,parameters,saved.path];
for(const p of extra)read(p);
const b={approved:true,role:'P212_INITIAL_SAVED_OUTPUT_RECEPTION',authority:'AUTHORIZE_ONE_SAVED_OUTPUT_RECONSTRUCTION_NO_PRODUCER_NO_ADOPTION',
  attempt:OWN+'/initial01',capture:OWN+'/initial01/node_capture',receiver,parameters,saved_stdout:saved.path,binding:OWN+'/BINDING.json',preload:OWN+'/node_preload04.js',
  node_lock:{path:OWN+'/NODE_RUNTIME_LOCK.json',pin:val(read(OWN+'/NODE_RUNTIME_LOCK.json'))},
  discovery:{path:OWN+'/NODE_PROBE04.json',pin:val(read(OWN+'/NODE_PROBE04.json'))},
  input_pins:Object.fromEntries(extra.map(p=>[p,inputs[p]])),controlled_python_files:pythonLock.files,environment:nodeProbe.sample.environment,
  timeouts:{receiver:300,native:60},canonical_adoption:false,producer_invocations:0};
for(const p of Object.keys(inputs))read(p,inputs[p]);for(const[p,k]of Object.entries(configuration))same(state(p),k,'entire selected configuration unchanged before binding');
for(const p of [OWN+'/initial01',PAPER+'/CANONICAL.json',PAPER+'/canonical.stdout.json'])absent(p);
write('RUNTIME_BINDING.json',b);write('PREPARATION_INPUTS.json',inputs);
console.log(JSON.stringify({status:'ROOT_BOUND_ONE_SAVED_OUTPUT_RECEPTION_NOT_EXECUTED',checks,input_paths:Object.keys(inputs).length,node_file_keys:Object.keys(nodeFiles).length,node_configuration_paths:Object.keys(configuration).length,
  controlled_python_files:130,semantic_binding:inputs[OWN+'/BINDING.json'],runtime_binding:inputs[OWN+'/RUNTIME_BINDING.json'],saved_stdout:saved,producer_invocations:0,canonical_adopted:false}));
