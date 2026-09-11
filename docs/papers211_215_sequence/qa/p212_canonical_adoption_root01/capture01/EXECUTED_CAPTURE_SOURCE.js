'use strict';
// One actual native helper invocation, after a separately prepared root binding.
// Root-owned documentary/native capture; not another scientific producer.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),a=require('assert').strict,cp=require('child_process');
const guard=require('./guard_runtime.js');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa',GATE=QA+'/p212_canonical_adoption_root01';
const PREP=QA+'/p212_canonical_adoption_preparation01',OUT=GATE+'/capture01',ADOPT=GATE+'/adoption01',CACHE=GATE+'/never_created_adoption_cache';
const TARGET=ROOT+'/papers/212-closed-pointer-orbits/CANONICAL.json',ALIAS=ROOT+'/papers/212-closed-pointer-orbits/canonical.stdout.json';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'},reads={};let checks=0;
const ok=(v,l)=>{checks++;a(v,l)},eq=(x,y,l)=>{checks++;a.deepEqual(x,y,l)};
const identity=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p,k){ok(path.isAbsolute(p)&&path.normalize(p)===p,'literal input');const l=fs.lstatSync(p),s=fs.statSync(p);ok(s.isFile(),'regular input');const b=fs.readFileSync(p),v={...identity(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};if(k)eq(v,k,'whole bound input');if(reads[p])eq(v,reads[p],'unchanged repeated input');reads[p]=v;return {raw:b,key:v};}
const json=p=>JSON.parse(read(p).raw);
function absent(p){try{fs.lstatSync(p);throw Error('lexists '+p);}catch(e){eq(e.code,'ENOENT','fresh output');}}
function write(n,v){const b=Buffer.isBuffer(v)?v:Buffer.from(JSON.stringify(v,null,2)+'\n');const fd=fs.openSync(OUT+'/'+n,'wx',0o600);try{fs.writeFileSync(fd,b);fs.fsyncSync(fd);}finally{fs.closeSync(fd);}}
eq(process.cwd(),ROOT);eq({...process.env},ENV);eq(process.argv.length,4);eq(process.argv[2],GATE+'/BINDING.json');
const bindingRaw=read(process.argv[2]).raw;eq(identity(bindingRaw).sha256,process.argv[3],'actual externally supplied binding digest');const binding=JSON.parse(bindingRaw);
eq(binding.approved,true);eq(binding.authority,'AUTHORIZE_ONE_EXCLUSIVE_P212_RAW_CANONICAL_ADOPTION_NO_PRODUCER_NO_PAIR');
eq(binding.root_capture.controller.path,__filename);eq(binding.root_capture.guard.path,GATE+'/guard_runtime.js');
read(__filename,binding.root_capture.controller.key);read(GATE+'/guard_runtime.js',binding.root_capture.guard.key);
const expected=json(binding.root_capture.input_key.path);eq(identity(read(binding.root_capture.input_key.path).raw),binding.root_capture.input_key.identity);
for(const[p,k]of Object.entries(expected))read(p,k);
for(const role of ['helper','inputs','root_source_reception','authority_record']){const {path:p,...k}=binding[role];read(p,k);}
const lock=json(binding.root_capture.runtime_lock.path);eq(identity(read(binding.root_capture.runtime_lock.path).raw),binding.root_capture.runtime_lock.identity);
const before=guard(lock,read);eq(before,json(GATE+'/RUNTIME_AT_BINDING.json'),'current entire same runtime/config key');
for(const p of [OUT,ADOPT,TARGET,ALIAS,CACHE])absent(p);
const argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+CACHE,PREP+'/adopt_canonical.py','--adopt-once',GATE+'/BINDING.json',process.argv[3],String(bindingRaw.length)];
eq(binding.root_capture.argv_without_binding_digest_and_size,argv.slice(0,-2),'exact declared direct-helper startup');eq(binding.root_capture.timeout_seconds,120);
fs.mkdirSync(OUT,{mode:0o700});const oldKeys=structuredClone(reads);write('INPUTS_BEFORE.json',oldKeys);write('RUNTIME_BEFORE.json',before);write('EXECUTED_CAPTURE_SOURCE.js',read(__filename).raw);
const request={argv,cwd:ROOT,environment:ENV,stdin:'DEVNULL',timeout_seconds:120,started_epoch:Date.now()/1000,source:identity(read(PREP+'/adopt_canonical.py').raw),binding:identity(bindingRaw),python:reads['/usr/bin/python3.10'],cmp:reads['/usr/bin/cmp'],pycache_prefix:CACHE};write('ATTEMPT.json',request);
const r=cp.spawnSync(argv[0],argv.slice(1),{cwd:ROOT,env:ENV,stdio:['ignore','pipe','pipe'],timeout:120000,maxBuffer:1024*1024});
const stdout=r.stdout||Buffer.alloc(0),stderr=r.stderr||Buffer.alloc(0);write('stdout.raw',stdout);write('stderr.raw',stderr);const receipt={...request,ended_epoch:Date.now()/1000,exit_code:r.status,signal:r.signal,error:r.error?{name:r.error.name,message:r.error.message,code:r.error.code||null}:null,stdout:identity(stdout),stderr:identity(stderr)};write('NATIVE.json',receipt);
ok(!r.error&&r.signal===null&&r.status===0&&stderr.length===0,'actual adoption native zero and complete');
const result=JSON.parse(stdout);eq(result,JSON.parse(fs.readFileSync(ADOPT+'/RESULT.json')),'whole native return equals actual result');eq(result.status,'P212_CANONICAL_EXCLUSIVELY_ADOPTED_FROM_ACCEPTED_ACTUAL_INITIAL_STDOUT');eq(result.producer_invocations,0);eq(result.strict_pair_completed,false);
const source=read(binding.source.path).raw,target=fs.readFileSync(TARGET);eq(target,source,'whole adopted raw source equality');eq(identity(target),{bytes:binding.source.bytes,sha256:binding.source.sha256});ok(!fs.lstatSync(TARGET).isSymbolicLink()&&fs.realpathSync(TARGET)===TARGET,'physical canonical');
const cmp=JSON.parse(fs.readFileSync(ADOPT+'/CMP_RECEIPT.json')),at=JSON.parse(fs.readFileSync(ADOPT+'/CMP_ATTEMPT.json'));for(const[k,v]of Object.entries(at))eq(cmp[k],v);for(const[k,v]of Object.entries(binding.cmp))eq(cmp[k],v);eq(cmp.exit_code,0);ok(cmp.started_epoch>=receipt.started_epoch&&cmp.ended_epoch<=receipt.ended_epoch,'cmp within actual helper lifetime');for(const s of ['stdout','stderr']){const b=fs.readFileSync(ADOPT+'/cmp.'+s+'.raw');eq(identity(b),cmp[s]);eq(b.length,0);}
eq(fs.readFileSync(ADOPT+'/BINDING_ORIGINAL.json'),bindingRaw);
const sums=fs.readFileSync(ADOPT+'/SHA256SUMS','utf8');ok(sums.endsWith('\n'));const names=[];for(const line of sums.trimEnd().split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);ok(m);ok(!m[2].includes('/')&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]));names.push(m[2]);const p=ADOPT+'/'+m[2];ok(fs.lstatSync(p).isFile()&&!fs.lstatSync(p).isSymbolicLink());eq(identity(fs.readFileSync(p)).sha256,m[1]);}eq(names.length,7);eq(fs.readdirSync(ADOPT).sort(),[...names,'SHA256SUMS'].sort());
const after=guard(lock,read);eq(after,before,'whole runtime/config key before after');write('RUNTIME_AFTER.json',after);for(const[p,k]of Object.entries(oldKeys))read(p,k);const stable=Object.fromEntries(Object.keys(oldKeys).map(p=>[p,reads[p]]));eq(stable,oldKeys);write('INPUTS_AFTER.json',stable);absent(ALIAS);absent(CACHE);
const summary={status:'PASS_ROOT_CAPTURE_AND_RAW_P212_CANONICAL_ADOPTION',checks,old_byte_keys:Object.keys(oldKeys).length,runtime_guard_checks_per_sample:before.checks,runtime_file_keys:130,resolved_runtime_files:121,configuration_paths:69,membership_entries:292,loader_directories:9,helper_native_exit:0,native_cmp_exit:0,actual_adoption_payloads:7,actual_adoption:result,canonical:{path:TARGET,...identity(target)},producer_invocations:0,pair_executions:0,continuous_trace_claimed:false};write('RESULT.json',summary);process.stdout.write(JSON.stringify(summary)+'\n');
