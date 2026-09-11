// Root documentary endpoint guard. No subprocess, submitted-code import, or grant.
'use strict';
const fs=require('fs'), path=require('path'), crypto=require('crypto'), util=require('util');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const QA=ROOT+'/docs/papers211_215_sequence/qa';
const PREP=QA+'/p211_terminal_enable_preparation01';
const DEST=QA+'/p211_terminal_enable_root01';
const SELF=DEST+'/entry_source01/precheck.js';
const ENV4={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};
const FIELDS=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];
let checks=0, reads={}, host=new Set();
function need(v,s){checks++;if(!v)throw Error(s)}
function equal(a,b,s){need(util.isDeepStrictEqual(a,b),s)}
function pin(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')}}
function stat(s){return Object.fromEntries(FIELDS.map(k=>[k,s[k].toString()]))}
function exists(p){try{fs.lstatSync(p);return true}catch(e){if(e.code==='ENOENT'||e.code==='ENOTDIR')return false;throw e}}
function physical(p){
  if(exists(p))return fs.realpathSync(p);
  let parent=path.dirname(p);need(parent!==p,'resolvable absent ancestor');
  return path.join(physical(parent),path.basename(p));
}
function read(p){
  need(path.isAbsolute(p)&&(p.startsWith(ROOT+'/')||host.has(p)),'predeclared input '+p);
  let ls=fs.lstatSync(p,{bigint:true}),s=fs.statSync(p,{bigint:true});
  need(s.isFile(),'regular resolved file '+p);
  let resolved=fs.realpathSync(p),symlink=ls.isSymbolicLink()?fs.readlinkSync(p):null;
  if(p.startsWith(ROOT+'/'))need(resolved===p&&symlink===null,'physical workspace '+p);
  let raw=fs.readFileSync(p),v={...pin(raw),resolved,symlink,stat:stat(s),lstat:stat(ls)};
  equal(stat(fs.statSync(p,{bigint:true})),v.stat,'stable stat '+p);
  equal(stat(fs.lstatSync(p,{bigint:true})),v.lstat,'stable lstat '+p);
  need(fs.realpathSync(p)===resolved&&BigInt(raw.length)===s.size,'stable whole bytes '+p);
  if(reads[p])equal(v,reads[p],'repeat rich input '+p);
  reads[p]=v;return raw;
}
function obj(p){return JSON.parse(read(p))}
function reference(r){equal(pin(read(r.path)),r.pin,'exact reference '+r.path);return r.path}
function entry(p,members=false){
  need(p.startsWith(ROOT+'/')||host.has(p),'predeclared configuration '+p);
  let present=exists(p),symlink=present&&fs.lstatSync(p).isSymbolicLink();
  let v={path:p,present,symlink,resolved:physical(p)};
  if(symlink)v.link=fs.readlinkSync(p);
  if(present){let s=fs.statSync(p,{bigint:true});
    if(s.isFile())Object.assign(v,{kind:'file'},pin(read(p)));
    else if(s.isDirectory()){v.kind='directory';if(members)v.members=fs.readdirSync(p).sort()}
    else if(s.isCharacterDevice()){
      let d=s.rdev;Object.assign(v,{kind:'character_device',major:Number(((d>>8n)&0xfffn)|((d>>32n)&0xfffff000n)),minor:Number((d&0xffn)|((d>>12n)&0xffffff00n))});
    }else Object.assign(v,{kind:'other',mode:Number(s.mode&0o170000n)});
  }return v;
}
function tree(base){
  need(fs.statSync(base).isDirectory()&&!fs.lstatSync(base).isSymbolicLink()&&fs.realpathSync(base)===base,'physical package');
  let files=[],directories=[],ids=new Set();
  function walk(dir){for(let name of fs.readdirSync(dir).sort()){
    let p=dir+'/'+name,s=fs.lstatSync(p,{bigint:true}),n=path.relative(base,p);
    need(!s.isSymbolicLink(),'no package symlink');
    if(s.isDirectory()){directories.push(n);walk(p)}
    else{need(s.isFile()&&s.nlink===1n&&!ids.has(s.dev+':'+s.ino),'ordinary distinct payload');ids.add(s.dev+':'+s.ino);files.push(n)}
  }}walk(base);return {files:files.sort(),directories:directories.sort()};
}
function seal(base){
  let lines=read(base+'/SHA256SUMS').toString().trimEnd().split('\n'),names=[],rows={};
  for(let line of lines){let m=/^([0-9a-f]{64})  (.+)$/.exec(line);need(!!m,'seal grammar');
    let n=m[2];need(n!=='SHA256SUMS'&&!path.isAbsolute(n)&&!n.split('/').some(x=>['','.','..'].includes(x))&&!rows[n],'safe unique nonself');
    need(pin(read(base+'/'+n)).sha256===m[1],'entire seal payload');rows[n]=m[1];names.push(n);
  }
  equal(names,[...names].sort(),'sorted seal');let dirs=new Set();for(let n of names){let d=path.dirname(n);while(d!=='.'){dirs.add(d);d=path.dirname(d)}}
  equal(tree(base),{files:names.concat('SHA256SUMS').sort(),directories:[...dirs].sort()},'whole seal membership');return names.length;
}
function put(dir,name,value){let raw=Buffer.from(JSON.stringify(value,null,2)+'\n');fs.writeFileSync(dir+'/'+name,raw,{flag:'wx',mode:0o600});return pin(raw)}
function main(){
  const [mode,phase,num]=process.argv.slice(2);
  need(process.argv.length===5&&['before','after'].includes(mode)&&['refresh','enable','capture'].includes(phase)&&['1','2'].includes(num),'literal mode/phase/build');
  need(process.cwd()===ROOT&&process.argv[1]===SELF,'literal root/source');equal({...process.env},ENV4,'exact documentary ENV4');
  const plan=obj(PREP+'/INPUT_PLAN.json');equal(pin(read(PREP+'/INPUT_PLAN.json')),{bytes:94596,sha256:'4e41d0c20016e9d331a7faf22cc683dad3fbedd00288d935fbff55ad343394a3'},'accepted plan');
  equal(pin(read(PREP+'/terminal_control.py')),{bytes:41305,sha256:'238369a33404a06ee4789af4bb7afd447213d70c21266b72cdca5d4a047ecea4'},'accepted unchanged controller');
  equal(pin(read(DEST+'/SOURCE_RECEPTION.md')),{bytes:5765,sha256:'a49d0145e184af65c976e2a199fb91c9ee560774a11482686fc93ce872e406f4'},'accepted source gate');
  read(SELF);read(DEST+'/entry_source01/SOURCE_RECEPTION.md');
  let hs=obj(PREP+'/HOST_SCOPE.json');need(hs.entries===841&&hs.paths.length===841,'exact host scope');host=new Set(hs.paths);
  for(let r of Object.values(plan.dependency_references))reference(r);
  let old=obj(plan.dependency_references.original_lock.path),key=obj(plan.dependency_references.prior_read_key.path),config=obj(plan.dependency_references.prior_configuration_key.path);
  let mapping=Object.fromEntries(obj(plan.dependency_references.historical_mapping.path).map(r=>[r.logical_path,r]));
  need(Object.keys(key).length===1299&&Object.keys(config).length===843&&Object.keys(old.entries).length===840,'full fixed scopes');
  let selected={},current={};
  for(let [p,spec]of Object.entries(old.selector_specs)){selected[p]=entry(p,!!spec.members);equal(selected[p],old.entries[p],'whole selector '+p)}
  for(let [p,v]of Object.entries(config)){current[p]=entry(p,'members' in v);equal(current[p],v,'whole historical configuration '+p)}
  let substitutions={};
  for(let [p,v]of Object.entries(key)){let target=p;if(mapping[p]){equal(mapping[p].pin,v,'original mapping pin');target=mapping[p].physical_original;substitutions[p]=target}equal(pin(read(target)),v,'full inherited byte key '+p)}
  equal(substitutions,plan.exact_historical_substitutions,'only two physical historical substitutions');
  need(Object.keys(plan.workspace_input_pins).length===272,'all272 planned originals');for(let [p,v]of Object.entries(plan.workspace_input_pins))equal(pin(read(p)),v,'planned original '+p);
  for(let [p,t]of Object.entries(plan.exact_input_package_trees))equal(tree(p),{files:[...t.files].sort(),directories:[...t.directories].sort()},'complete accepted input package '+p);
  need(seal(PREP)===9,'preparation9');need(seal(QA+'/p211_initial_build_01')===362,'oldbuild362');need(seal(QA+'/p211_initial_build_independent_reception')===18,'oldaudit18');need(seal(ROOT+'/papers/211-kernel-image-projection-feedback/frozen_round0')===32,'oldfreeze32');
  const b=plan.builds[num],authority=b.authority_paths[phase],phaseDir=b.phase_outputs[phase],dest=b.root_parent+'/'+phase+'_entry01';
  let authorityRaw=read(authority).toString(),blocks=[...authorityRaw.matchAll(/^```json\n([\s\S]*?)\n```$/gm)];need(blocks.length===1,'one actual root grant');let grant=JSON.parse(blocks[0][1]);
  need(grant.issuer==='/root'&&grant.phase===phase&&grant.build_number===Number(num)&&grant.phase_output===phaseDir&&grant.cold_output===b.cold_output,'actual scoped root authority');
  reference(grant.controller);reference(grant.input_plan);reference(grant.preparation_seal);for(let r of Object.values(grant.required_receipts))reference(r);
  equal(grant.controller_environment,ENV4,'grant environment');
  need(fs.statSync(b.root_parent).isDirectory()&&fs.realpathSync(b.root_parent)===b.root_parent,'ordinary root parent');
  const finalParent=path.dirname(b.cold_output);need(fs.statSync(finalParent).isDirectory()&&fs.realpathSync(finalParent)===finalParent&&!fs.lstatSync(finalParent).isSymbolicLink(),'ordinary separately created qa_final');
  let absent=[phaseDir+'/unused_controller_cache',b.outer_pycache_prefix,b.inner_pycache_prefix,...b.cwd_relative_paths];
  if(mode==='before'||phase!=='capture')absent.push(b.cold_output);
  if(mode==='before'){absent.push(phaseDir);need(!exists(dest),'new literal entry packet');}
  const absences={};for(let p of absent){need(!exists(p)&&physical(p)===p,'exact future absence '+p);absences[p]={present:false,resolved:p}}
  const argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+phaseDir+'/unused_controller_cache',PREP+'/terminal_control.py',phase,num,authority,String(Buffer.byteLength(authorityRaw)),pin(Buffer.from(authorityRaw)).sha256];
  for(let p of ['/usr/bin/python3.10','/usr/bin/env','/usr/bin/bash','/dev/null'])need(host.has(p),'inherited product/controller launch spelling '+p);
  if(mode==='before')fs.mkdirSync(dest,{mode:0o700});
  else{
    let native=JSON.parse(fs.readFileSync(dest+'/CONTROLLER_TOOL_NATIVE.json'));
    need(native.results.length>=1&&native.results.at(-1).exit_code!==undefined&&!('session_id' in native.results.at(-1)),'actual settled product completion before endpoint closure');
    let prev=JSON.parse(fs.readFileSync(dest+'/INPUTS_BEFORE.json'));
    equal(reads,prev,'all exact byte/stat inputs unchanged across actual controller');
    let previous=JSON.parse(fs.readFileSync(dest+'/CONFIGURATION_BEFORE.json'));equal({selected,current},{selected:previous.selected,current:previous.current},'all840/843 configuration endpoints');
  }
  let suffix=mode.toUpperCase(),configuration={selected,current,absences};
  const outputs={inputs:put(dest,'INPUTS_'+suffix+'.json',reads),configuration:put(dest,'CONFIGURATION_'+suffix+'.json',configuration)};
  let result={status:'PASS_ROOT_'+suffix+'_CONTROLLER_ENDPOINT_CHECK',phase,build_number:Number(num),checks,read_paths:Object.keys(reads).length,host_scope:841,inherited_files:1299,selector:840,configuration:843,planned_originals:272,argv,environment:ENV4,cwd:ROOT,authority:pin(Buffer.from(authorityRaw)),outputs,new_controller_invocations:0,new_science:0,new_builds:0,source_only_diagnostic_runtime:{node:process.version,execPath:process.execPath,os_trace:false},limits:'Metadata endpoint guard; no scientific/TeX execution, no host discovery, no authority or acceptance, and no continuous startup/process trace.'};
  const resultPin=put(dest,'RESULT_'+suffix+'.json',result);console.log(JSON.stringify({status:result.status,checks,result:{path:dest+'/RESULT_'+suffix+'.json',pin:resultPin},read_paths:result.read_paths,argv,new_controller_invocations:0}));
}
try{main()}catch(e){console.error(e.stack);process.exitCode=1}
