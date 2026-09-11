'use strict';
// Root documentary reception; disclosed unchanged reuse of the independent
// metadata checker, never execution/import of the submitted assembler/freeze.
const fs=require('node:fs'), path=require('node:path'), crypto=require('node:crypto');
const cp=require('node:child_process'), assert=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const QA=ROOT+'/docs/papers211_215_sequence/qa/';
const HERE=QA+'p211_round2_binding_root01/source_reception01/';
const PREP=QA+'p211_round2_binding_preparation01/';
const AUDIT=QA+'p211_round2_binding_source_audit01/';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};
const INPUTS={},LABELS=[],COMMANDS=[];
function need(v,l){LABELS.push(l);if(!v)throw Error(l);}
function same(a,b,l){LABELS.push(l);assert.deepStrictEqual(a,b,l);}
function pin(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
function meta(s){return Object.fromEntries(['dev','ino','size','mode','nlink','mtimeNs','ctimeNs'].map(k=>[k,String(s[k])]));}
function read(p,k){
  p=path.resolve(ROOT,p);need(p.startsWith(ROOT+'/'),'workspace only '+p);
  const a=fs.lstatSync(p,{bigint:true});
  need(a.isFile()&&!a.isSymbolicLink()&&fs.realpathSync(p)===p,'physical input '+p);
  const b=fs.readFileSync(p),z=fs.lstatSync(p,{bigint:true});same(meta(a),meta(z),'stable read '+p);
  const q={...pin(b),state:meta(z)};
  if(k)same(pin(b),{bytes:k.bytes,sha256:k.sha256},'original byte pin '+p);
  if(INPUTS[p])same(INPUTS[p],q,'unchanged root full key '+p);INPUTS[p]=q;return b;
}
function json(p){return JSON.parse(read(p));}
function write(p,b){fs.writeFileSync(p,b,{flag:'wx',mode:0o600});}
function writeJSON(p,v){write(p,JSON.stringify(v,null,2)+'\n');}
function sumRows(b){need(b.at(-1)===10,'complete SHA list');const rows={};for(const l of b.toString().trimEnd().split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(l);need(m&&!Object.hasOwn(rows,m[2]),'unique exact SHA row');rows[m[2]]=m[1];}return rows;}
function sealed(base,count,sealHash){
  const b=read(base+'SHA256SUMS');same(pin(b).sha256,sealHash,'exact package seal');const rows=sumRows(b);
  same(Object.keys(rows).length,count,'whole package count');
  same(fs.readdirSync(base).sort(),[...Object.keys(rows),'SHA256SUMS'].sort(),'whole flat nonself membership');
  let bytes=b.length;for(const[n,h]of Object.entries(rows)){const raw=read(base+n);same(pin(raw).sha256,h,'sealed payload '+n);bytes+=raw.length;}
  return {payloads:count,files:count+1,bytes,seal:pin(b)};
}
function native(record,label){
  need(record.request&&typeof record.request.cmd==='string','actual native request '+label);
  const r=record.result;need(r&&typeof r.output==='string'&&Number.isInteger(r.exit_code)&&!r.session_id,'complete native envelope '+label);
  return {label,chunk_id:r.chunk_id,exit_code:r.exit_code,output:pin(Buffer.from(r.output)),limited:r.output.startsWith('Warning: truncated output')};
}
function command(label,argv,cwd=ROOT){
  const dir=HERE+'commands/'+label;fs.mkdirSync(dir,{recursive:false});
  const started=new Date().toISOString();
  writeJSON(dir+'/ATTEMPT.json',{label,argv,cwd,environment:ENV,timeout_ms:60000,started_utc:started,stdin:'pipe empty',scope:'read-only documentary child; not operational submitted source'});
  const r=cp.spawnSync(argv[0],argv.slice(1),{cwd,env:ENV,input:Buffer.alloc(0),encoding:null,timeout:60000,maxBuffer:16*1024*1024});
  const out=r.stdout||Buffer.alloc(0),err=r.stderr||Buffer.alloc(0);
  write(dir+'/stdout.raw',out);write(dir+'/stderr.raw',err);
  const receipt={label,argv,cwd,environment:ENV,started_utc:started,ended_utc:new Date().toISOString(),status:r.status,signal:r.signal,error:r.error?String(r.error):null,stdout:pin(out),stderr:pin(err),scope:'direct synchronous metadata child only; no escaped-descendant/hermetic claim'};
  writeJSON(dir+'/RECEIPT.json',receipt);COMMANDS.push(receipt);
  need(r.status===0&&r.signal===null&&!r.error&&err.length===0,'actual successful metadata child '+label);return out;
}
need(process.cwd()===ROOT,'exact workspace cwd');
need(!fs.existsSync(HERE+'RESULT.json')&&!fs.existsSync(HERE+'commands'),'fresh reception outputs');
fs.mkdirSync(HERE+'commands');
let result;
try{
  read(__filename);
  const packages={preparation:sealed(PREP,9,'8c640abe8708bac71416cc062cc94728b34a4b3daa5100030863f456605a67b9'),audit:sealed(AUDIT,8,'6828243c2dd72d8966eda3fb9a0ba6b561af052d3e65a42f8101a438c142dbfe')};
  const f=json(AUDIT+'FINDINGS.json');same(f.open_findings,{Critical:0,Major:0,Minor:0,total:0},'actual independent zero-open census');
  same(f.decision,'GO_DISABLED_BINDING_PREPARATION_ONLY','bounded source decision');same(f.operational_status,'HOLD_OPERATIONAL','no operational permission');
  const checks=json(AUDIT+'CHECKS_NATIVE.json');same(checks.records.length,1,'one actual prior metadata execution');
  const old=checks.records[0];native(old,'independent checker');same(old.result.exit_code,0,'old actual successful exit');
  const oldResult=JSON.parse(old.result.output);same([oldResult.checks,oldResult.input_files],[157585,3116],'whole independent result counts');
  same(Object.keys(oldResult.input_pins).length,3116,'whole independent result key');
  for(const[n,k]of Object.entries(oldResult.input_pins))read(n,k);
  const ext=sumRows(read(AUDIT+'INPUTS.sha256'));same(Object.keys(ext).length,3115,'all external pins');
  for(const[n,h]of Object.entries(ext))same(pin(read(n)).sha256,h,'whole external SHA input');
  const nativeRows=[];
  for(const [name,expected]of [['NATIVE_READS.json',18],['CLOSING_NATIVE.json',7]]){
    const j=json(AUDIT+name);same(j.records.length,expected,'whole audit native '+name);
    j.records.forEach((r,i)=>nativeRows.push(native(r,name+':'+i)));
  }
  const close=json(AUDIT+'CLOSING_NATIVE.json').records;
  same(close.map(r=>r.result.exit_code),Array(7).fill(0),'all seven audit closing exits');
  const pre=JSON.parse(close[6].result.output);same(pre.payload_count_at_check,7,'exact preclosing payload census');
  for(const[n,k]of Object.entries(pre.pins))read(AUDIT+n,k);
  const auditReads=json(AUDIT+'NATIVE_READS.json').records;
  for(const [ids,target]of [
    [['r2bindingaudit_new_assemble01','r2bindingaudit_new_assemble02'],PREP+'assemble_disabled.py'],
    [['r2bindingaudit_old_assemble01','r2bindingaudit_old_assemble02'],QA+'p211_round1_binding_root/assemble_binding02.py'],
    [['r2bindingaudit_old_recheck'],QA+'p211_round1_binding_root/recheck02.py']
  ]){
    const b=Buffer.from(ids.map(id=>{const r=auditReads.find(x=>x.record_id===id);need(r&&r.result.exit_code===0,'actual whole numbered source read');return r.result.output.replace(/^ *[0-9]+\t/gm,'');}).join(''));
    need(b.equals(read(target)),'whole original numbered source binding '+target);
  }
  same(close[5].result.output,Object.keys(ext).map(n=>n+': OK\n').join(''),'whole actual external native stdout');
  let links=0;for(const m of read(AUDIT+'REPORT.md').toString().matchAll(/\[[^\]\n]*\]\(([^)\n]+)\)/g)){
    const target=path.resolve(AUDIT,m[1].replace(/:\d+$/,''));read(target);links++;
  }
  command('01_prep_seal',['/usr/bin/sha256sum','-c','SHA256SUMS'],PREP);
  command('02_audit_seal',['/usr/bin/sha256sum','-c','SHA256SUMS'],AUDIT);
  write(HERE+'INDEPENDENT_ORIGINAL_STDOUT.raw',Buffer.from(old.result.output));
  const fresh=command('03_disclosed_unchanged_metadata_reuse',['/usr/bin/node',AUDIT+'audit_metadata.js']);
  need(fresh.equals(Buffer.from(old.result.output)),'entire independent metadata output unchanged');
  command('04_whole_raw_cmp',['/usr/bin/cmp',HERE+'INDEPENDENT_ORIGINAL_STDOUT.raw',HERE+'commands/03_disclosed_unchanged_metadata_reuse/stdout.raw']);
  for(const[n,k]of Object.entries({...INPUTS}))read(n,k);
  result={status:'PASS_ROOT_BINDING_SOURCE_RECEPTION_ONLY',packages,checks:LABELS.length,input_files:Object.keys(INPUTS).length,independent_reused_checks:oldResult.checks,independent_reused_inputs:oldResult.input_files,whole_reused_output:pin(fresh),audit_native_records:nativeRows,report_links:links,commands:COMMANDS,submitted_assembler_executed:false,authority_issued:false,host_dereference:false,science_runs:0,builds:0,round2_created:false,scope:'Whole source and independent documentary evidence received; fresh documentary assembly requires separate actual root authority. Complete host/settings/build precopy checks remain separately scoped.'};
}catch(e){result={status:'FAIL_PRESERVED',error:String(e),stack:e.stack,checks:LABELS.length,input_files:Object.keys(INPUTS).length,commands:COMMANDS};}
writeJSON(HERE+'INPUTS.json',INPUTS);writeJSON(HERE+'CHECK_LABELS.json',LABELS);writeJSON(HERE+'RESULT.json',result);
console.log(JSON.stringify({...result,audit_native_records:undefined,commands:COMMANDS.map(r=>({label:r.label,status:r.status,stdout:r.stdout,stderr:r.stderr}))}));
process.exitCode=result.status==='PASS_ROOT_BINDING_SOURCE_RECEPTION_ONLY'?0:1;
