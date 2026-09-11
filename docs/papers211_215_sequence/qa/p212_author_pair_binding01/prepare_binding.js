'use strict';
// Root forward derivative of the fully read accepted initial binding preparer.
// No Python/AST/import/probe/science; old absent-canonical checker is not rerun.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),a=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const OWN=QA+'p212_author_pair_binding01',PREP=QA+'p212_runtime_preparation01',DISC=QA+'p212_runtime_discovery01',PAPER=ROOT+'/papers/212-closed-pointer-orbits';
const ADOPT=QA+'p212_canonical_adoption_root01',SOURCE=QA+'p212_author_pair_source_reception01',RECEIVER=QA+'p212_pair_receiver_source_root01';
const ATTEMPT=QA+'root_replays/p212_author_pair_01',CACHE=OWN+'/never_created_root_capture_cache';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};const inputs={};let checks=0;
function need(v,l){checks++;a.ok(v,l);}function same(x,y,l){checks++;a.deepStrictEqual(x,y,l);}
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p,k){need(path.normalize(p)===p&&path.isAbsolute(p),'literal bounded input');const l=fs.lstatSync(p),s=fs.statSync(p);need(s.isFile(),'regular resolved original');const raw=fs.readFileSync(p),v={...pin(raw),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};if(inputs[p])same(v,inputs[p],'complete repeated key');if(k)for(const f of ['bytes','sha256','resolved','symlink'])if(Object.hasOwn(k,f))same(v[f],k[f],'complete supplied '+f);inputs[p]=v;return raw;}
const obj=p=>JSON.parse(read(p));
function absent(p){try{fs.lstatSync(p);throw Error('unexpected output '+p);}catch(e){if(e.code!=='ENOENT')throw e;}return {path:p,lexists:false,observed_utc:new Date().toISOString()};}
function write(n,b){fs.writeFileSync(OWN+'/'+n,b,{flag:'wx',mode:0o600});}function json(n,v){write(n,JSON.stringify(v,null,2)+'\n');}
same(Object.fromEntries(Object.entries(process.env)),ENV,'actual literal ENV4');same(process.cwd(),ROOT,'actual workspace cwd');
const beforeAbsence=[ATTEMPT,OWN+'/entry01',OWN+'/BINDING.json',PAPER+'/canonical.stdout.json',CACHE].map(absent);
same(fs.realpathSync(path.dirname(ATTEMPT)),path.dirname(ATTEMPT),'physical existing attempt parent');
function sealed(base,count){const raw=read(base+'/SHA256SUMS');need(raw.at(-1)===10,'complete nonself seal');const expected=[];for(const line of raw.toString().trimEnd().split('\n')){const m=line.match(/^([0-9a-f]{64})  (.+)$/);need(m&&!path.isAbsolute(m[2])&&!m[2].split('/').includes('..')&&m[2]!=='SHA256SUMS'&&!expected.includes(m[2]),'literal nonself row');expected.push(m[2]);read(base+'/'+m[2],{sha256:m[1]});}const actual=[],dirs=[];function walk(d){for(const n of fs.readdirSync(d)){const p=d+'/'+n,s=fs.lstatSync(p);need(!s.isSymbolicLink(),'ordinary accepted tree');if(s.isDirectory()){dirs.push(path.relative(base,p));walk(p);}else{need(s.isFile(),'ordinary accepted leaf');actual.push(path.relative(base,p));}}}walk(base);same(expected.length,count,'complete accepted payload count');same(actual.sort(),[...expected,'SHA256SUMS'].sort(),'complete accepted tree');const wanted=new Set();for(const n of expected){let d=path.dirname(n);while(d!=='.'){wanted.add(d);d=path.dirname(d);}}same(dirs.sort(),[...wanted].sort(),'complete directory membership');return {payloads:count,seal:pin(raw)};}
const acceptedPackages={adoption:sealed(ADOPT,78),controller_source:sealed(SOURCE,7),receiver_source:sealed(RECEIVER,7)};
same(obj(SOURCE+'/RESULT.json').status,'PASS_ROOT_P212_STRICT_PAIR_CONTROLLER_SOURCE_RECEPTION_ONLY');
same(obj(RECEIVER+'/RESULT.json').status,'PASS_ROOT_COMPLETE_P212_PAIR_RECEIVER_SOURCE_AND_STARTUP_AMENDMENT');
for(const p of [SOURCE+'/INPUTS.json',RECEIVER+'/INPUTS.json',ADOPT+'/ADOPTION_CLOSING_INPUTS.json'])for(const[q,k]of Object.entries(obj(p)))read(q,k);
const template=obj(PREP+'/PAIR.pending.json'),b=structuredClone(template);same(b.approved,false);same(b.mode,'pair');
const parameters=obj(PAPER+'/PARAMETERS.json');same(parameters,b.schema.equalities.find(x=>JSON.stringify(x.path)==='["parameters"]').value,'whole typed parameters');
for(const k of b.capsule_files)read(k.path,k);for(const[p,k]of Object.entries(b.adapter_sources))read(p,k);
const scientific=read(PAPER+'/verify.py').toString();same(scientific.split('\n').filter(l=>/^(import |from )/.test(l)),['import itertools','import json','import math','import sys','from fractions import Fraction'],'unchanged whole literal import surface');
const canonical=read(PAPER+'/CANONICAL.json',{bytes:12501943,sha256:'1a32be6bb36dd8b4b27b9891a42876fe235bf2555a3dd9f4e36195a6ad72676c'});
const adoption=obj(ADOPT+'/adoption01/RESULT.json');need(canonical.equals(read(adoption.source)),'whole accepted original output/canonical');
const controller=read(OWN+'/run.py',{bytes:6263,sha256:'2c6f2a7378a7c5411b262376415e1a77bbdc35523eb7821e44b01a787da93fd0'});
need(controller.equals(read(QA+'p212_author_pair_controller_preparation01/run.py')),'whole physical controller source');
const deployment=obj(OWN+'/DEPLOYMENT_NATIVE.json');same(deployment.length,6);for(const r of deployment){same(r.result.exit_code,0);same(r.result.output,'');}
const guardPath=ADOPT+'/guard_runtime.js';read(guardPath,{bytes:3913,sha256:'6819afc1081b5b5cbd64cca958f0827b29e66205c6a17f8de1548b48c6b87933'});
const guard=require(guardPath),lock=obj(DISC+'/RUNTIME_LOCK.json');
const runtime=guard(lock,p=>{const raw=read(p);return {raw,key:inputs[p]};});same(runtime.checks,1241,'complete accepted current runtime/config guard');json('RUNTIME_AT_BINDING.json',runtime);json('ROOT_ABSENCE_AT_BINDING.json',{scope:'Actual preparation-time observations, not yet immediate pre-production or continuous tracing',observations:beforeAbsence});
b.approved=true;b.attempt=ATTEMPT;b.reviewed_static_source_import_closure=true;b.reviewed_schema_and_parameters=true;b.reviewed_compile_exec_interface=true;b.timeouts={science:300,native:60,envelope:900};
b.runtime_lock={path:DISC+'/RUNTIME_LOCK.json',...inputs[DISC+'/RUNTIME_LOCK.json']};b.canonical={path:PAPER+'/CANONICAL.json',...inputs[PAPER+'/CANONICAL.json']};
const selected=[OWN+'/AUTHORITY.md',OWN+'/SOURCE_CALL_INTERFACE.md',OWN+'/ROOT_STARTUP_CONTRACT.md',OWN+'/run.py',OWN+'/prepare_binding.js',OWN+'/DEPLOYMENT_NATIVE.json',OWN+'/RUNTIME_AT_BINDING.json',OWN+'/ROOT_ABSENCE_AT_BINDING.json',
 QA+'p212_author_initial_binding01/SOURCE_CALL_INTERFACE.md',QA+'p212_author_initial_binding01/prepare_binding.js',QA+'p212_author_source_reception/RECEPTION.md',QA+'p212_author_source_reception/ROLE_DECISION.md',QA+'p212_runtime_source_root_reception01/RECEPTION.md',QA+'p212_runtime_discovery_root_reception01/RECEPTION.md',QA+'p212_runtime_discovery_root_reception01/SHA256SUMS',
 ADOPT+'/RECEPTION.md',ADOPT+'/ADOPTION_CLOSING_RESULT.json',ADOPT+'/ADOPTION_CLOSING_INPUTS.json',ADOPT+'/SHA256SUMS',guardPath,SOURCE+'/RECEPTION.md',SOURCE+'/RESULT.json',SOURCE+'/INPUTS.json',SOURCE+'/SHA256SUMS',RECEIVER+'/RECEPTION.md',RECEIVER+'/RESULT.json',RECEIVER+'/INPUTS.json',RECEIVER+'/SHA256SUMS',
 QA+'p212_saved_output_root_reception01/RECEPTION.md',QA+'p212_saved_output_root_reception01/EXECUTION_RECEPTION_RESULT.json',QA+'p212_saved_output_root_reception01/EXECUTION_RECEPTION_INPUTS.json',QA+'p212_saved_output_root_reception01/SHA256SUMS',PREP+'/PLAN.md',PREP+'/BINDING_CONTRACT.md',PREP+'/SHA256SUMS',PAPER+'/OUTPUT_SCHEMA.md',PAPER+'/OUTPUT_PLAN.md'];
same(new Set(selected).size,selected.length,'no duplicate provenance roles');for(const p of selected)read(p);b.provenance_inputs=selected.map(p=>({path:p,...inputs[p]}));
b.pending_obligations=['Actual separately bound strict pair and three native raw comparisons','Complete actual native/dependency/configuration/startup reception and unchanged-key canonical semantic reuse','Initial build, manuscript reviews and freezes, terminal builds/views remain separate'];
b.root_authority_decision='AUTHORIZE_ONE_P212_AUTHOR_STRICT_PAIR_NO_ADOPTION';b.root_execution_interface='pinned compile/exec in a fresh isolated child, exact main/file/argv/capsule cwd; not direct python verify.py';
b.root_capture={entry:OWN+'/entry01',timeout_seconds:1200,environment:ENV,controller:{path:OWN+'/run.py',...inputs[OWN+'/run.py']},outer_argv_without_binding_digest:['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+ATTEMPT+'/never_created_outer_cache',PREP+'/p212_runtime.py','outer',OWN+'/BINDING.json',ATTEMPT]};
const reverse=structuredClone(b);for(const k of ['approved','attempt','reviewed_static_source_import_closure','reviewed_schema_and_parameters','reviewed_compile_exec_interface','timeouts','canonical','runtime_lock','provenance_inputs','pending_obligations'])reverse[k]=structuredClone(template[k]);for(const k of ['root_authority_decision','root_execution_interface','root_capture'])delete reverse[k];same(reverse,template,'whole exact reverse delta');
for(const p of Object.keys(inputs))read(p,inputs[p]);same(guard(lock,p=>{const raw=read(p);return {raw,key:inputs[p]};}),runtime,'whole runtime/config state unchanged during binding');
for(const p of [ATTEMPT,OWN+'/entry01',PAPER+'/canonical.stdout.json',CACHE])absent(p);
json('INPUTS_AT_BINDING.json',inputs);json('BINDING.json',b);
const result={status:'ROOT_P212_PAIR_BINDING_READY_NOT_EXECUTED',binding:{path:OWN+'/BINDING.json',...pin(fs.readFileSync(OWN+'/BINDING.json'))},checks,input_paths:Object.keys(inputs).length,runtime_keys:130,resolved_runtime_keys:121,configuration_paths:69,membership_paths:292,loader_paths:9,full_guard_checks:1241,provenance_count:selected.length,accepted_packages:acceptedPackages,attempt:ATTEMPT,entry:OWN+'/entry01',scientific_executions:0,canonical_absent:false,canonical_unchanged:true,root_startup_prefix:CACHE,root_prefix_absent_observed:true,reverse_delta_passed:true};
json('RESULT.json',result);console.log(JSON.stringify(result));
