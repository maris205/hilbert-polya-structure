'use strict';
// Root documentary reception/capture only. No scientific program is imported.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const cp = require('node:child_process');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = ROOT + '/docs/papers211_215_sequence/qa';
const DESK = QA + '/p211_lifecycle_scientific_key_desk01';
const HERE = QA + '/p211_lifecycle_scientific_key_root01';
const SOURCE = DESK + '/check_scientific_reuse_v2.py';
const SPEC = DESK + '/SCIENTIFIC_REUSE_SPEC_v2.json';
const SOURCE_HASH = '92c4d83bfb2c61305958c454ef5cb1a398d59d43aa8eb6fa0c055a2cdedd1ead';
const SPEC_HASH = 'a1c9fd87629b9a175a53fe5fd60680def880d81796018c8ea87eda8b227ea50c';
const ENV4 = {PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};
let checks = 0;
const reads = {};
function need(b,m) { checks++; assert.ok(b,m); }
function equal(a,b,m) { checks++; assert.deepStrictEqual(a,b,m); }
function identity(b) { return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')}; }
function rich(p) {
  need(path.isAbsolute(p),'absolute read spelling');
  const b=fs.readFileSync(p), l=fs.lstatSync(p);
  need(fs.statSync(p).isFile(),'regular resolved file');
  const k={...identity(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null};
  if(reads[p]) equal(k,reads[p],'unchanged on repeated read '+p);
  reads[p]=k; return {b,k};
}
function obj(p,hash) { const r=rich(p); if(hash) equal(r.k.sha256,hash,p); return JSON.parse(r.b); }
function four(k) { return Object.fromEntries(['bytes','sha256','resolved','symlink'].map(f=>[f,k[f]])); }
function save(name,value) { const b=Buffer.from(JSON.stringify(value,null,2)+'\n'); fs.writeFileSync(HERE+'/'+name,b,{flag:'wx'}); return identity(b); }
function inventory(base) {
  const out=[];
  for(const name of fs.readdirSync(base).sort()) {
    const p=base+'/'+name,s=fs.lstatSync(p);
    need(!s.isSymbolicLink(),'no package symlink');
    if(s.isDirectory()) for(const q of inventory(p)) out.push(name+'/'+q);
    else {need(s.isFile(),'regular package payload');out.push(name);}
  }
  return out;
}
function seal(base) {
  const rows=rich(base+'/SHA256SUMS').b.toString('utf8').trimEnd().split('\n');
  const names=[];
  for(const row of rows) {
    const m=/^([0-9a-f]{64})  (.+)$/.exec(row);need(m,'strict manifest row');
    const n=m[2];need(n!=='SHA256SUMS'&&!path.isAbsolute(n)&&!n.split('/').includes('..'),'nonself safe manifest');
    need(!names.includes(n),'unique manifest member');names.push(n);
    equal(rich(base+'/'+n).k.sha256,m[1],'complete manifest payload '+n);
  }
  equal(names.slice().sort(),inventory(base).filter(n=>n!=='SHA256SUMS').sort(),'complete nonself inventory');
  return {payloads:names.length,seal:reads[base+'/SHA256SUMS']};
}
function preflight() {
  equal(process.cwd(),ROOT,'exact cwd');
  equal(rich(SOURCE).k.sha256,SOURCE_HASH,'entire personally read source');
  const spec=obj(SPEC,SPEC_HASH), basis={};
  for(const [p,k] of Object.entries(spec.basis_inputs)) {need(p.startsWith(ROOT+'/'),'workspace-only basis');basis[p]=obj(p,k.sha256);}
  equal(Object.keys(basis).length,10,'all original basis documents');
  const union={};
  for(const r of Object.values(spec.roles)) {
    const child=basis[r.child_key],outer=basis[r.outer_key],binding=basis[r.binding];
    equal(Object.keys(outer).length,r.outer_entries,'whole original outer');
    equal(Object.keys(child).length,r.child_entries,'whole original child');
    const extended={...outer};
    for(const row of binding.capsule_files) extended[r.attempt+'/recorder/capsule/'+row.name]={...four(row),resolved:r.attempt+'/recorder/capsule/'+row.name,symlink:null};
    equal(extended,child,'exact two-file child augmentation');
    for(const [p,k] of Object.entries(child)) {if(union[p])equal(union[p],k,'role overlap');union[p]=k;}
  }
  equal(union,spec.files,'entire independently collated427 key');equal(Object.keys(union).length,427,'427 keys');
  const lock=basis[spec.lock];
  equal(spec.configuration,lock.configuration,'all69/5/292 settings original');
  equal(spec.loader_search_directory_states,lock.loader_search_directory_states,'all9 loader states');
  const later=obj(spec.later_accepted_file_key.path,spec.later_accepted_file_key.sha256);
  equal(Object.keys(later).length,4929,'full accepted later ledger');
  for(const [p,k] of Object.entries(union)) equal(four(later[p]),k,'all427 covered by later accepted original');
  const last=spec.accepted_last_scientific_settings_check;
  const native=obj(last.path,last.sha256);
  equal(native.argv,['/usr/bin/python3.10','-I','-S','-B',last.source.path],'actual latest full settings checker');
  equal(native.native_exit_code,0,'actual success');equal(native.exception,null,'no native exception');
  equal(native.stdout,last.whole_stdout,'entire recorded original stdout');
  equal(rich(last.source.path).k.sha256,last.source.sha256,'original recapture source');
  const original=rich(QA+'/p211_round2_root_reception01/01_recheck.stdout.raw');
  equal(identity(original.b),last.whole_stdout,'full original raw output');
  const result=JSON.parse(original.b);equal(result.checks,488474,'actual original predicate count');
  const rows=rich(DESK+'/INPUTS_V2.sha256').b.toString('utf8').trimEnd().split('\n');
  equal(rows.length,56,'all56 preparation provenance pins');
  for(const row of rows) {const m=/^([0-9a-f]{64})  (.+)$/.exec(row);need(m,'pin schema');equal(rich(ROOT+'/'+m[2]).k.sha256,m[1],'exact original provenance');}
  const packageSeal=seal(DESK);
  for(const [p,k] of Object.entries({...reads}))equal(rich(p).k,k,'source reception closing input');
  return {spec,packageSeal};
}
function main() {
  need(process.argv.length===3&&['receive','run'].includes(process.argv[2]),'separate explicit phase');
  const {spec,packageSeal}=preflight();
  if(process.argv[2]==='receive') {
    const out={status:'PASS_ROOT_SOURCE_RECEPTION_ONLY',checks,read_paths:Object.keys(reads).length,READ_INPUTS:reads,packageSeal,scientific_keys:427,new_scientific_runs:0,new_host_checks:0,run_authorized:false,paper_complete:false};
    const key=save('SOURCE_RESULT.json',out);console.log(JSON.stringify({status:out.status,checks,read_paths:out.read_paths,result:key}));return;
  }
  const received=obj(HERE+'/SOURCE_RESULT.json');
  need(received.status==='PASS_ROOT_SOURCE_RECEPTION_ONLY','separate actual source reception');
  for(const [p,k] of Object.entries(received.READ_INPUTS)) equal(rich(p).k,k,'received inputs remain same');
  const authority=rich(HERE+'/AUTHORITY.md');
  need(authority.b.includes(Buffer.from(SOURCE_HASH))&&authority.b.includes(Buffer.from('ONE_READONLY_INVOCATION')),'exact explicit root grant document');
  const args=['-I','-S','-B',SOURCE,'--root-authorized-read-only'];
  const exe=rich('/usr/bin/python3.10');equal(exe.k,spec.files['/usr/bin/python3.10'],'exact existing scientific runtime executable');
  const pre={source:rich(SOURCE).k,spec:rich(SPEC).k,executable:exe.k,root_source:rich(__filename).k,authority:authority.k,argv:['/usr/bin/python3.10',...args],environment:ENV4,cwd:ROOT};
  save('BEFORE.json',pre);
  const start=Date.now(),mono=process.hrtime.bigint();
  const child=cp.spawnSync('/usr/bin/python3.10',args,{cwd:ROOT,env:ENV4,stdio:['ignore','pipe','pipe'],timeout:30000,maxBuffer:8*1024*1024});
  const end=Date.now(),duration=(process.hrtime.bigint()-mono).toString();
  const stdout=child.stdout||Buffer.alloc(0),stderr=child.stderr||Buffer.alloc(0);
  fs.writeFileSync(HERE+'/stdout.json',stdout,{flag:'wx'});fs.writeFileSync(HERE+'/stderr.bin',stderr,{flag:'wx'});
  const native={...pre,started_epoch_ms:start,ended_epoch_ms:end,duration_ns:duration,pid:child.pid,native_exit_code:child.status,signal:child.signal,error:child.error?String(child.error):null,stdin:'ignore /dev/null',timeout_ms:30000,max_buffer_bytes:8*1024*1024,stdout:identity(stdout),stderr:identity(stderr),invocations:1};
  save('NATIVE.json',native);
  need(!child.error&&child.status===0&&child.signal===null&&stderr.length===0,'successful whole documentary invocation');
  const r=JSON.parse(stdout);
  equal(r.status,'PASS_BOUNDED_SCIENTIFIC_REUSE_KEY_RECONCILIATION_PENDING_ROOT_ACCEPTANCE','actual checker success');
  equal(r.DOMAIN_BEFORE,r.DOMAIN_AFTER,'complete original returned endpoints');
  equal(r.DOMAIN_BEFORE.scientific_files,spec.files,'all427 returned file keys');
  equal(r.DOMAIN_BEFORE.configuration_paths,spec.configuration.paths,'full returned configuration');
  equal(r.DOMAIN_BEFORE.memberships,spec.configuration.memberships,'complete292 returned member states');
  equal(r.DOMAIN_BEFORE.loader_states,spec.loader_search_directory_states,'complete returned loader states');
  equal(Object.keys(r.DOMAIN_BEFORE.cache_lexists).sort(),spec.absent_cache_paths.slice().sort(),'all original cache paths');
  need(Object.values(r.DOMAIN_BEFORE.cache_lexists).every(x=>x===false),'every original cache absent');
  for(const [p,k] of Object.entries(r.READ_INPUTS)) equal(rich(p).k,k,'complete actual returned read-key reception');
  for(const [p,k] of Object.entries({...reads})) equal(rich(p).k,k,'all root inputs close');
  const out={status:'PASS_ROOT_CURRENT_SCIENTIFIC_KEY',root_checks:checks,checker_checks:r.checks,read_paths:Object.keys(reads).length,READ_INPUTS:reads,scientific_keys:427,scientific_runtime_files:122,configuration_paths:69,membership_directories:5,membership_entries:292,loader_states:9,cache_absences:15,actual_stdout:identity(stdout),new_scientific_runs:0,new_builds:0,new_page_views:0,scientific_pairs_explicitly_reused:true,paper_complete:false};
  const key=save('RUN_RESULT.json',out);console.log(JSON.stringify({status:out.status,root_checks:checks,checker_checks:r.checks,read_paths:out.read_paths,result:key,stdout:identity(stdout)}));
}
try {main();} catch(e) {console.error(String(e.stack||e));process.exitCode=1;}
