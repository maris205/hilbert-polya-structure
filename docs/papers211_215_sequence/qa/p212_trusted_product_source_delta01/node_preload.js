'use strict';
// SOURCE ONLY. Bounded Node preload for the one contract-only outer entry.
// Derived observational ideas from accepted node_preload05.js; no old
// receiver fs hooks, runtime counts, ENV4 lock or manuscript role are reused.
// Conditional trusted-product model; neither this preload nor its maps attest product startup.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const cp=require('node:child_process'),assert=require('node:assert/strict'),Module=require('node:module');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa';
const SELF=QA+'/p212_trusted_product_source_delta01/node_preload.js';
const DRIVER=QA+'/p212_execution_scope_source_amendment01/driver.js';
const INNER=QA+'/p212_build_dependency_binding01/contract01/BINDING.json';
const OUT=QA+'/p212_build_dependency_outer_capture01/contract01';
const CWD=QA+'/p212_build_dependency_query01/query_cwd';
const ENV8={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',
 SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'};
const PROVENANCE={schema:'p212-trusted-product-boundary-v1',
 assumption:'ordinary_product_observer_bash_env_bootstrap',product_startup_attested:false,
 claim:'finite_received_keys_and_discrete_downstream_observations'};
const STAT=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks',
 'atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const expectedVectors=[['/usr/bin/kpsewhich','--help'],['/usr/bin/kpsewhich','--version']];
function need(v,m){assert.ok(v,m);}
function equal(a,b,m){assert.deepEqual(a,b,m);}
function pin(raw){return {bytes:raw.length,sha256:crypto.createHash('sha256').update(raw).digest('hex')};}
function canonical(raw){const text=raw.toString('utf8'),v=JSON.parse(text);
 need(Buffer.from(text).equals(raw)&&Buffer.from(JSON.stringify(v,null,2)+'\n').equals(raw),'canonical complete JSON');return v;}
function statFields(s){return Object.fromEntries(STAT.map(k=>{need(typeof s[k]==='bigint','full integer stat');return[k,s[k].toString()];}));}
function stable(s){return Object.fromEntries(STAT.filter(k=>k!=='atimeNs').map(k=>[k,s[k]]));}
function physicalOriginal(name){
 const p=OUT+'/'+name;need(fs.realpathSync(p)===p&&!fs.lstatSync(p).isSymbolicLink(),'physical supervisor output original');
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 try{const a=fs.fstatSync(fd,{bigint:true});need(a.isFile(),'supervisor original regular handle');
 const raw=fs.readFileSync(fd),z=fs.fstatSync(fd,{bigint:true});
 equal(stable(statFields(a)),stable(statFields(z)),'supervisor original stable handle');
 equal(BigInt(raw.length),a.size,'whole supervisor original');return raw;}finally{fs.closeSync(fd);}
}
function write(name,v){fs.writeFileSync(OUT+'/'+name,JSON.stringify(v,null,2)+'\n',{flag:'wx',mode:0o600});}
need(require.main!==module,'No direct/probe invocation is granted by this preload');
equal(__filename,SELF,'fixed received preload');
equal({...process.env},ENV8,'exact cleared Node ENV8');
equal(process.execArgv,['--require',SELF],'sole explicitly received loader');
equal(process.argv,[process.execPath,DRIVER,INNER],'exact contract driver argv');
equal(process.cwd(),ROOT,'actual Node cwd');
equal(process.umask(),0o077,'umask set before Node startup');
const originalRaw=physicalOriginal('OUTER_BINDING_ORIGINAL.json');
const outer=canonical(originalRaw),external=canonical(physicalOriginal('BINDING_KEY_BEFORE.json'));
equal(pin(originalRaw),external.expected_nonself_descriptor.content,'outer original matches externally supplied full pin');
equal(outer.schema,'p212-contract-outer-trusted-product-binding-v1','distinct outer schema');
need(outer.enabled===true&&outer.phase==='contract'&&outer.status==='ROOT_BOUND_TRUSTED_PRODUCT_CONTRACT_ONLY','explicit trusted-product contract only');
equal(outer.provenance,PROVENANCE,'fixed conditional model, not product startup attestation');
const inputs=new Map(outer.inputs.map(d=>[d.path,d]));
equal(inputs.size,outer.inputs.length,'unique received input paths');
for(const d of inputs.values())need(!['body','query_result'].includes(d.role),'no body/query channel before main');
const node=outer.runtime.node;
equal(process.execPath,node.executable_resolved,'prebound Node executable');
function readRuntime(p){
 const d=inputs.get(p);need(d&&d.role==='runtime'&&['file','symlink'].includes(d.kind),'exact mapped runtime purpose');
 const r=inputs.get(d.resolved);need(r&&r.kind==='file'&&r.role==='runtime'&&r.path===r.resolved,'regular runtime referent');
 equal(d.stat,r.stat,'alias/referent stat');equal(d.content,r.content,'alias/referent whole pin');
 need(d.content&&Number.isSafeInteger(d.content.bytes)&&d.content.bytes>=0,'nonnull whole runtime bytes');
 equal(fs.realpathSync(p),d.resolved,'current resolved runtime');
 const ls=fs.lstatSync(p,{bigint:true});
 equal(stable(statFields(ls)),stable(d.lstat),'lexical runtime metadata');
 equal(ls.isSymbolicLink()?fs.readlinkSync(p):null,d.symlink_target,'literal runtime link');
 const fd=fs.openSync(d.resolved,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 try{const before=fs.fstatSync(fd,{bigint:true});need(before.isFile(),'actual regular runtime handle');
 equal(stable(statFields(before)),stable(d.stat),'runtime handle before');
 const raw=fs.readFileSync(fd);equal(pin(raw),d.content,'whole pinned runtime');
 const after=fs.fstatSync(fd,{bigint:true});equal(stable(statFields(after)),stable(statFields(before)),'runtime handle after');
 return {path:p,content:pin(raw),handle_before:statFields(before),handle_after:statFields(after)};
 }finally{fs.closeSync(fd);}
}
function sample(){
 const raw=fs.readFileSync('/proc/self/maps'),mapped={};
 for(const line of raw.toString().trimEnd().split('\n')){
  const m=/^[0-9a-f]+-[0-9a-f]+\s+[rwxps-]+\s+[0-9a-f]+\s+[0-9a-f:]+\s+\d+(?:\s+(.*))?$/.exec(line);
  need(m,'complete proc-map row');
  if(m[1]&&m[1].startsWith('/')){
   need(!m[1].endsWith(' (deleted)'),'no deleted map');
   need(node.mapped_paths.includes(m[1]),'every mapped path in preaccepted Node closure');
   if(!Object.hasOwn(mapped,m[1]))mapped[m[1]]=readRuntime(m[1]);
  }
 }
 equal(Object.keys(mapped).sort(),node.mapped_paths,'complete current expected Node map set');
 const natives=process.binding('natives'),fingerprints={};
 for(const k of Object.keys(natives).sort()){
  need(typeof natives[k]==='string'||(k==='configs'&&natives[k]===undefined),'typed native source registry');
  fingerprints[k]=typeof natives[k]==='string'?{type:'string',...pin(Buffer.from(natives[k]))}:{type:'undefined'};
 }
 equal(fingerprints,node.builtin_source_fingerprints,'all preaccepted builtin fingerprints');
 equal(process.versions,node.versions,'entire Node version map');
 equal(process.arch,node.architecture,'received architecture');equal(process.platform,node.platform,'received platform');
 for(const item of process.moduleLoadList){
  need(/^(NativeModule |Internal Binding )/.test(item),'no unclassified Node module role');
  if(item.startsWith('NativeModule '))need(Object.hasOwn(fingerprints,item.slice(13)),'all NativeModule source keys embedded and prebound');
  else need(node.internal_bindings.includes(item),'every internal binding in exact prepared finite list');
 }
 return {executable:process.execPath,versions:process.versions,architecture:process.arch,platform:process.platform,
  argv:process.argv,exec_argv:process.execArgv,environment:{...process.env},cwd:process.cwd(),umask:process.umask(),
  module_load_list:process.moduleLoadList,require_cache:Object.keys(require.cache).sort(),
  builtin_source_fingerprints:fingerprints,mapped_files:mapped,proc_maps_hex:raw.toString('hex'),
  scope:'DISCRETE_SOURCE_AND_MAP_OBSERVATIONS_NOT_STARTUP_OR_CONTINUOUS_OS_TRACE'};
}
const before=sample();equal(before.require_cache,[SELF],'pre-driver CommonJS cache');
write('NODE_BEFORE.json',before);
const spawnVectors=[],events=[],loads=[];
const spawn=cp.spawn;
cp.spawn=function(file,args,options){
 const vector=[file,...args],index=spawnVectors.length;
 need(index<2,'no third native command');equal(vector,expectedVectors[index],'exact next help/version vector');
 equal(Object.keys(options).sort(),['cwd','detached','env','shell','stdio'],'all exact spawn options');
 equal(options.cwd,CWD,'exact query cwd');equal(options.env,ENV8,'no inherited native environment');
 equal(options.detached,true,'inner new native group');equal(options.shell,false,'no shell');
 need(Array.isArray(options.stdio)&&options.stdio.length===3&&options.stdio.every(Number.isSafeInteger),'actual preowned stdio descriptors');
 spawnVectors.push(vector);events.push({type:'ATTEMPT',index,argv:vector,unix_ms:Date.now()});
 const child=spawn.apply(this,arguments);
 child.once('spawn',()=>events.push({type:'SPAWN',index,pid:child.pid,unix_ms:Date.now()}));
 child.once('error',e=>events.push({type:'ERROR',index,code:e.code??null,message:e.message,unix_ms:Date.now()}));
 child.once('exit',(code,signal)=>events.push({type:'EXIT',index,pid:child.pid,code,signal,unix_ms:Date.now()}));
 child.once('close',(code,signal)=>events.push({type:'CLOSE',index,pid:child.pid,code,signal,unix_ms:Date.now()}));
 return child;
};
const load=Module._load;
Module._load=function(request,parent,isMain){
 need(request===DRIVER||['node:fs','node:path','node:crypto','node:child_process','node:assert/strict'].includes(request),
  'only exact driver main and its five explicit builtins');
 loads.push({request,parent:parent?.filename??null,is_main:!!isMain});
 return load.apply(this,arguments);
};
process.on('exit',code=>{
 const errors=[];let after=null;
 try{
  equal(code,0,'successful driver exit');equal(spawnVectors,expectedVectors,'both and only two native vectors');
  for(let index=0;index<2;index++){
   const e=events.filter(x=>x.index===index);equal(e.map(x=>x.type),['ATTEMPT','SPAWN','EXIT','CLOSE'],'complete observed native events');
   need(Number.isSafeInteger(e[1].pid)&&e[1].pid>0,'positive actual native PID');
   for(const x of e.slice(2)){equal(x.pid,e[1].pid,'same actual PID');equal(x.code,0,'help/version native success');equal(x.signal,null,'no native signal');}
  }
  after=sample();equal(after.require_cache,[SELF,DRIVER].sort(),'only preload and driver CommonJS files');
  equal(physicalOriginal('OUTER_BINDING_ORIGINAL.json'),originalRaw,'supervisor original remains raw-equal');
 }catch(e){errors.push(String(e));process.exitCode=78;}
 write('NODE_AFTER.json',{sample:after,errors});
 write('NODE_RESULT.json',{status:errors.length?'FAIL_PRESERVED':'OBSERVED_CONTRACT_NODE_RUNTIME_PENDING_ROOT',
  driver_exit_code:code,errors,spawn_argv:spawnVectors,events,loads,
  provenance:PROVENANCE,pre_node_key:'INDEPENDENT_FINITE_KEY_REQUIRED_NOT_PROVED_BY_PRELOAD',
  lookup_or_body_permission:false,continuous_or_escaped_writer_claim:false});
});
