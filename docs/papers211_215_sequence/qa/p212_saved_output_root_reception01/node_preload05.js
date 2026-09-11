'use strict';
// Root bounded Node builtin/runtime observations for saved-output reception.
// --probe imports builtins only. A separate exact binding precedes the receiver.
// This observes exported fs calls/discrete maps, not OS/startup/continuous tracing.
const fs=require('node:fs'),crypto=require('node:crypto'),path=require('node:path'),Module=require('node:module');
const ROOT='/root/autodl-tmp/symbolic_dynamics',OWN=ROOT+'/docs/papers211_215_sequence/qa/p212_saved_output_root_reception01';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};
const original={};for(const k of Object.keys(fs))if(typeof fs[k]==='function')original[k]=fs[k].bind(fs);
const stable=v=>JSON.stringify(v,(_,x)=>typeof x==='bigint'?String(x):x);
function sorted(v){if(Array.isArray(v))return v.map(sorted);if(v&&typeof v==='object')return Object.fromEntries(Object.keys(v).sort().map(k=>[k,sorted(v[k])]));return v;}
function need(ok,s){if(!ok)throw Error(s);}
function equal(a,b,s){need(stable(sorted(a))===stable(sorted(b)),s);}
const value=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
let internalRead=0;
function read(p){internalRead++;try{return original.readFileSync(p);}finally{internalRead--;}}
function rich(p){const l=original.lstatSync(p),b=read(p);need(original.statSync(p).isFile(),'ordinary pinned byte file');return {...value(b),resolved:original.realpathSync(p),symlink:l.isSymbolicLink()?original.readlinkSync(p):null};}
function state(p){
  let l;try{l=original.lstatSync(p);}catch(e){if(e.code==='ENOENT'||e.code==='ENOTDIR')return {lexists:false};throw e;}
  const s=original.statSync(p),r={lexists:true,is_file:s.isFile(),is_directory:s.isDirectory(),resolved:original.realpathSync(p),symlink:l.isSymbolicLink()?original.readlinkSync(p):null};
  if(s.isFile())Object.assign(r,value(read(p)));return r;
}
function sample(){
  const maps=read('/proc/self/maps'),mapped={};
  for(const line of maps.toString().trimEnd().split('\n')){
    const m=/^[0-9a-f]+-[0-9a-f]+\s+[rwxps-]+\s+[0-9a-f]+\s+[0-9a-f:]+\s+\d+(?:\s+(.*))?$/.exec(line);need(m,'complete proc-map row');
    if(m[1]&&m[1].startsWith('/')){need(!m[1].endsWith(' (deleted)'),'no deleted file map');const p=original.realpathSync(m[1]);mapped[p]=rich(p);}
  }
  // The complete native-source strings are embedded in the pinned executable.
  const natives=process.binding('natives'),nativeSources={};
  for(const k of Object.keys(natives).sort()){need(typeof natives[k]==='string'||(k==='configs'&&natives[k]===undefined),'exact native source value kind');nativeSources[k]=typeof natives[k]==='string'?{type:'string',...value(Buffer.from(natives[k]))}:{type:'undefined'};}
  return {executable:process.execPath,versions:process.versions,architecture:process.arch,platform:process.platform,
    argv:process.argv,exec_argv:process.execArgv,cwd:process.cwd(),environment:{...process.env},
    module_load_list:process.moduleLoadList,require_cache:Object.keys(require.cache).sort(),
    builtin_source_fingerprints:nativeSources,mapped_files:mapped,proc_maps:maps.toString(),proc_maps_pin:value(maps)};
}
equal({...process.env},ENV,'exact cleared ENV4 only');
if(require.main===module){
  equal(process.argv,[process.execPath,__filename,'--probe'],'exact import-only probe');
  equal(process.execArgv,[],'no inherited Node loader options');
  process.stdout.write(JSON.stringify({status:'BUILTIN_ONLY_NODE_RUNTIME_PROBE_NO_RECEIVER',sample:sample()})+'\n');
}else{
  const runtimePath=OWN+'/RUNTIME_BINDING02.json',runtimeRaw=read(runtimePath),b=JSON.parse(runtimeRaw);
  need(b.approved===true&&b.role==='P212_INITIAL_SAVED_OUTPUT_RECEPTION','explicit separate root runtime approval');
  equal(process.argv,[process.execPath,b.receiver,'--binding',b.binding],'exact actual receiver argv');
  equal(process.execArgv,['--require',__filename],'exact sole explicit Node preload');
  equal(b.capture,OWN+'/initial02/node_capture','one exclusive current capture');
  equal(process.cwd(),ROOT,'actual root cwd');
  const lock=JSON.parse(read(b.node_lock.path)),discovery=JSON.parse(read(b.discovery.path)).sample;
  equal(value(read(b.node_lock.path)),b.node_lock.pin,'bound whole Node dependency lock');
  equal(value(read(b.discovery.path)),b.discovery.pin,'bound actual import-only sample');
  const sourceInputs={};
  for(const[p,k]of Object.entries(b.input_pins)){sourceInputs[p]=rich(p);equal(sourceInputs[p],k,'entire source input pin');}
  need(Object.hasOwn(sourceInputs,__filename)&&Object.hasOwn(sourceInputs,b.receiver)&&Object.hasOwn(sourceInputs,b.binding),'all actual source/binding paths prekeyed');
  function currentKey(){
    const files={},configuration={};
    for(const[p,k]of Object.entries(lock.files)){files[p]=rich(p);equal(files[p],k,'current whole Node file key');}
    for(const[p,k]of Object.entries(lock.configuration)){configuration[p]=state(p);equal(configuration[p],k,'current bounded Node configuration');}
    return {files,configuration};
  }
  function checkedSample(){
    const s=sample();
    for(const f of ['executable','versions','architecture','platform','cwd','environment','builtin_source_fingerprints'])equal(s[f],discovery[f],'whole stable import-only Node '+f);
    equal(s.mapped_files,discovery.mapped_files,'entire actual file-backed Node map roles');
    for(const[p,k]of Object.entries(s.mapped_files)){need(Object.hasOwn(lock.files,p),'every map prelocked');equal(k,lock.files[p],'every actual map exact key');}
    need(s.module_load_list.every(x=>/^(NativeModule |Internal Binding )/.test(x)),'all module-load entries embedded Node roles');
    return s;
  }
  const beforeKey=currentKey(),before=checkedSample();
  equal(before.require_cache,[__filename],'exact pre-receiver CommonJS cache');
  original.mkdirSync(b.capture);
  const write=(n,v)=>{internalRead++;try{return original.writeFileSync(b.capture+'/'+n,JSON.stringify(v,null,2)+'\n',{flag:'wx'});}finally{internalRead--;}};
  write('BEFORE.json',{runtime_binding:value(runtimeRaw),source_inputs:sourceInputs,dependency_key:beforeKey,sample:before});
  const allowed=new Set([b.receiver,b.binding,b.parameters,b.saved_stdout]);
  const events=[],fds=new Map(),loads=[];
  function fileEvent(operation,name,flags){
    const p=typeof name==='number'?fds.get(name):typeof name==='string'?path.resolve(name):null;
    need(p&&allowed.has(p),'receiver exported fs path outside four bound inputs');
    events.push({operation,path:p,descriptor:typeof name==='number'?name:null,flags:flags===undefined?null:flags});
    return p;
  }
  fs.openSync=function(name,flags,...args){
    if(internalRead)return original.openSync(name,flags,...args);
    const p=fileEvent('openSync',name,flags);
    need(flags==='r'||(Number.isInteger(flags)&&!(flags&(fs.constants.O_WRONLY|fs.constants.O_RDWR|fs.constants.O_CREAT|fs.constants.O_TRUNC|fs.constants.O_APPEND))),'receiver read-only exported open');
    const fd=original.openSync(name,flags,...args);fds.set(fd,p);return fd;
  };
  fs.readFileSync=function(name,...args){if(!internalRead)fileEvent('readFileSync',name);return original.readFileSync(name,...args);};
  for(const op of ['lstatSync','statSync','realpathSync'])fs[op]=function(name,...args){if(!internalRead)fileEvent(op,name);return original[op](name,...args);};
  fs.fstatSync=function(fd,...args){if(!internalRead)fileEvent('fstatSync',fd);return original.fstatSync(fd,...args);};
  fs.closeSync=function(fd){if(internalRead)return original.closeSync(fd);fileEvent('closeSync',fd);const r=original.closeSync(fd);fds.delete(fd);return r;};
  fs.writeSync=function(fd,...args){
    if(internalRead)return original.writeSync(fd,...args);
    need(fd===1||fd===2,'only preowned stdout/stderr stream descriptors may be written');
    const written=original.writeSync(fd,...args);events.push({operation:'writeSync',descriptor:fd,native_stream:fd===1?'stdout':'stderr',bytes_written:written});return written;
  };
  for(const op of ['writeFileSync','appendFileSync','createWriteStream','unlinkSync','rmSync','renameSync','mkdirSync','rmdirSync','copyFileSync'])fs[op]=function(){if(internalRead)return original[op](...arguments);events.push({operation:op,denied:true});throw Error('receiver exported filesystem write forbidden');};
  const load=Module._load;
  Module._load=function(request,parent,isMain){
    need(request===b.receiver||['node:fs','node:crypto','node:path'].includes(request),'receiver exact embedded builtin imports only');
    loads.push({request,is_main:!!isMain,parent:parent?parent.filename:null});return load.apply(this,arguments);
  };
  process.on('exit',code=>{
    const errors=[];let afterKey=null,after=null;
    try{
      need(code===0,'successful receiver exit');
      afterKey=currentKey();equal(afterKey,beforeKey,'entire unchanged Node key');
      after=checkedSample();equal(after.require_cache,[__filename,b.receiver].sort(),'only preload plus submitted receiver CommonJS cache');
      equal(value(read(runtimePath)),value(runtimeRaw),'unchanged actual runtime binding');
      for(const[p,k]of Object.entries(sourceInputs))equal(rich(p),k,'unchanged entire source input');
      need(fds.size===0,'all observed opened descriptors closed');
    }catch(e){errors.push(String(e));process.exitCode=1;}
    write('AFTER.json',{dependency_key:afterKey,sample:after});
    write('EXPORTED_FS_AND_MODULE_EVENTS.json',{events,loads,scope:'Exported fs calls and CommonJS Module._load after preload; no continuous OS/startup claim.'});
    write('RESULT.json',{status:errors.length?'FAIL_PRESERVED':'PASS_BOUNDED_NODE_RECEIVER_RUNTIME',receiver_exit_code:code,errors,
      source_inputs:sourceInputs,dependency_files:Object.keys(lock.files).length,configuration_paths:Object.keys(lock.configuration).length,
      scope:'Exact source/runtime/settings key and discrete loaded-file/builtin/exported-fs observations. Not hermetic tracing or independent mathematics.'});
  });
}
