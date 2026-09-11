'use strict';
// Root documentary binding assembly. No Python AST/import/compile/science.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),a=require('node:assert/strict'),cp=require('node:child_process');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const OWN=QA+'p212_author_initial_binding01',PREP=QA+'p212_runtime_preparation01',REC=QA+'p212_runtime_discovery_root_reception01';
const AUD=QA+'p212_runtime_discovery_independent01',DISC=QA+'p212_runtime_discovery01',PAPER=ROOT+'/papers/212-closed-pointer-orbits',ATTEMPT=QA+'root_replays/p212_author_initial_01';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};
const inputs={};let checks=0;
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function need(x,s){checks++;a.ok(x,s);}
function same(x,y,s){checks++;a.deepStrictEqual(x,y,s);}
function read(p,k){
  need(path.posix.normalize(p)===p&&p.startsWith('/'),'literal input');const l=fs.lstatSync(p),s=fs.statSync(p);need(s.isFile(),'ordinary resolved byte input');
  const b=fs.readFileSync(p),v={...pin(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};
  if(inputs[p])same(v,inputs[p],'entire repeated key');if(k)for(const field of ['bytes','sha256','resolved','symlink'])if(Object.hasOwn(k,field))same(v[field],k[field],'exact supplied '+field);
  inputs[p]=v;return b;
}
const obj=p=>JSON.parse(read(p));
function absent(p){try{fs.lstatSync(p);throw Error('existing forbidden output '+p);}catch(e){if(e.code!=='ENOENT')throw e;}}
function write(n,b){fs.writeFileSync(OWN+'/'+n,b,{flag:'wx',mode:0o600});}
function json(n,v){write(n,JSON.stringify(v,null,2)+'\n');}
for(const p of [ATTEMPT,OWN+'/entry01',OWN+'/BINDING.json',PAPER+'/CANONICAL.json',PAPER+'/canonical.stdout.json'])absent(p);
same(fs.realpathSync(path.dirname(ATTEMPT)),path.dirname(ATTEMPT),'existing physical attempt parent');
const oldReception=obj(REC+'/RESULT.json');
same(oldReception.status,'PASS_ROOT_COMPLETE_DOCUMENTARY_IMPORT_DISCOVERY_RECEPTION_INITIAL_BINDING_PREPARATION_ONLY','actual accepted reception status');
for(const[p,k]of Object.entries(oldReception.input_pins))read(p,k);
for(const base of [REC,AUD,PREP]){
  const seal=read(base+'/SHA256SUMS').toString();need(seal.endsWith('\n'),'complete received seal');const names=[];
  for(const line of seal.trimEnd().split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);need(m&&!m[2].startsWith('/')&&!m[2].split('/').includes('..'),'safe payload row');names.push(m[2]);read(base+'/'+m[2],{sha256:m[1]});}
  same(fs.readdirSync(base).sort(),[...names,'SHA256SUMS'].sort(),'complete flat received package');
}
const request={argv:['/usr/bin/node',AUD+'/receive_discovery.js'],cwd:ROOT,environment:ENV,timeout_ms:60000,stdin:'ignore'};
json('DISCOVERY_PRECHECK.ATTEMPT.json',request);
const r=cp.spawnSync(request.argv[0],request.argv.slice(1),{cwd:ROOT,env:ENV,timeout:60000,input:Buffer.alloc(0),maxBuffer:8*1024*1024});
const stdout=r.stdout||Buffer.alloc(0),stderr=r.stderr||Buffer.alloc(0);
write('DISCOVERY_PRECHECK.stdout.raw',stdout);write('DISCOVERY_PRECHECK.stderr.raw',stderr);
const receipt={...request,exit_code:r.status,signal:r.signal,pid:r.pid,error:r.error?String(r.error):null,stdout:pin(stdout),stderr:pin(stderr),scope:'Actual read-only unchanged documentary checker, not import/probe/science or an independent new implementation.'};json('DISCOVERY_PRECHECK.RECEIPT.json',receipt);
same(r.status,0,'fresh full dependency/configuration precheck');same(r.signal,null,'no native signal');need(!r.error,'native streams settled');same(stderr.length,0,'empty documentary stderr');
const check=JSON.parse(stdout);same(check.checks,109613,'complete prior documentary gate');same(check.input_files,228,'all byte input keys');same(check.state_paths,336,'all configuration-state keys');
need(stdout.equals(Buffer.from(obj(AUD+'/CHECKS_NATIVE.json').records[0].result.output)),'whole original/recheck equality');
for(const[p,k]of Object.entries(check.input_pins))read(p,k);
const template=obj(PREP+'/INITIAL.pending.json'),b=structuredClone(template);
same(b.approved,false,'original disabled template unchanged');same(b.mode,'initial','initial role');
const parameters=obj(PAPER+'/PARAMETERS.json');same(parameters,b.schema.equalities.find(x=>JSON.stringify(x.path)==='["parameters"]').value,'whole exact typed parameter equality');
for(const k of b.capsule_files)read(k.path,k);
const source=read(PAPER+'/verify.py').toString();
same(source.split('\n').filter(s=>/^(import |from )/.test(s)),['import itertools','import json','import math','import sys','from fractions import Fraction'],'exact declared source imports from fully read pinned source');
for(const[p,k]of Object.entries(b.adapter_sources))read(p,k);
const lock=obj(DISC+'/RUNTIME_LOCK.json');same(Object.keys(lock.files).length,130,'actual new runtime key');for(const[p,k]of Object.entries(lock.files))read(p,k);
b.approved=true;b.attempt=ATTEMPT;b.reviewed_static_source_import_closure=true;b.reviewed_schema_and_parameters=true;b.reviewed_compile_exec_interface=true;
b.timeouts={science:300,native:60,envelope:900};
b.runtime_lock={path:DISC+'/RUNTIME_LOCK.json',...inputs[DISC+'/RUNTIME_LOCK.json']};
const selected=[OWN+'/SOURCE_CALL_INTERFACE.md',OWN+'/AUTHORITY.md',OWN+'/run.py',OWN+'/prepare_binding.js',OWN+'/DISCOVERY_PRECHECK.ATTEMPT.json',OWN+'/DISCOVERY_PRECHECK.RECEIPT.json',OWN+'/DISCOVERY_PRECHECK.stdout.raw',OWN+'/DISCOVERY_PRECHECK.stderr.raw',
  QA+'p212_author_source_reception/RECEPTION.md',QA+'p212_author_source_reception/ROLE_DECISION.md',QA+'p212_runtime_source_root_reception01/RECEPTION.md',
  REC+'/RECEPTION.md',REC+'/RESULT.json',REC+'/ROOT_NATIVE01.json',REC+'/ROOT_CLOSING_NATIVE.json',REC+'/SHA256SUMS',AUD+'/REPORT.md',AUD+'/FINDINGS.json',AUD+'/SHA256SUMS',
  PREP+'/PLAN.md',PREP+'/BINDING_CONTRACT.md',PREP+'/SHA256SUMS',PAPER+'/OUTPUT_SCHEMA.md',PAPER+'/OUTPUT_PLAN.md'];
for(const p of selected)read(p);
b.provenance_inputs=selected.map(p=>({path:p,...inputs[p]}));
b.pending_obligations=['Actual initial execution with this exact root binding, then complete native/dependency and every saved semantic field reception','Exclusive raw CANONICAL.json adoption remains separately held','Separate strict-pair binding and paper review/build/freezes remain later'];
b.root_authority_decision='AUTHORIZE_ONE_P212_AUTHOR_INITIAL_NO_ADOPTION';
b.root_execution_interface='pinned compile/exec in a fresh isolated child, exact main/file/argv/capsule cwd; not direct python verify.py';
b.root_capture={entry:OWN+'/entry01',timeout_seconds:1200,environment:ENV,controller:{path:OWN+'/run.py',...inputs[OWN+'/run.py']},outer_argv_without_binding_digest:['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+ATTEMPT+'/never_created_outer_cache',PREP+'/p212_runtime.py','outer',OWN+'/BINDING.json',ATTEMPT]};
const reverse=structuredClone(b);
for(const k of ['approved','attempt','reviewed_static_source_import_closure','reviewed_schema_and_parameters','reviewed_compile_exec_interface','timeouts','runtime_lock','provenance_inputs','pending_obligations'])reverse[k]=structuredClone(template[k]);
for(const k of ['root_authority_decision','root_execution_interface','root_capture'])delete reverse[k];same(reverse,template,'whole exact reverse delta of disabled template');
for(const p of Object.keys(inputs))read(p);
for(const p of [ATTEMPT,OWN+'/entry01',PAPER+'/CANONICAL.json',PAPER+'/canonical.stdout.json'])absent(p);
json('INPUTS_AT_BINDING.json',inputs);json('BINDING.json',b);
const result={status:'ROOT_P212_INITIAL_BINDING_READY_NOT_EXECUTED',binding:{path:OWN+'/BINDING.json',...pin(fs.readFileSync(OWN+'/BINDING.json'))},checks,input_paths:Object.keys(inputs).length,runtime_keys:130,documentary_precheck:{checks:check.checks,input_files:check.input_files,state_paths:check.state_paths,stdout:pin(stdout)},provenance_count:selected.length,attempt:ATTEMPT,entry:OWN+'/entry01',scientific_executions:0,canonical_absent:true,reverse_delta_passed:true};
json('RESULT.json',result);console.log(JSON.stringify(result));
