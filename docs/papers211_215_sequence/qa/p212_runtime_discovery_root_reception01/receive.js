'use strict';
// Root documentary reception and explicitly reused nonauthor checker.
// No submitted Python, probe, producer, ambient environment or scientific file.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),a=require('node:assert/strict'),cp=require('node:child_process');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const OWN=QA+'p212_runtime_discovery_root_reception01',AUD=QA+'p212_runtime_discovery_independent01';
const PREP=QA+'p212_runtime_preparation01',CONTROL=QA+'p212_import_discovery_root01';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'};
const inputs={},native=[];let checks=0;
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function same(x,y,label){checks++;a.deepStrictEqual(x,y,label);}
function need(x,label){checks++;a.ok(x,label);}
function read(p){
  need(path.posix.normalize(p)===p&&p.startsWith('/'),'literal absolute input');
  need(!p.startsWith(ROOT+'/papers/')&&!p.includes('/root_diagnostic_private'),'no scientific/private read');
  const s=fs.lstatSync(p),real=fs.realpathSync(p),raw=fs.readFileSync(p);
  need(fs.statSync(p).isFile(),'ordinary resolved byte input');
  const k={...pin(raw),resolved:real,symlink:s.isSymbolicLink()?fs.readlinkSync(p):null};
  if(inputs[p])same(k,inputs[p],'unchanged whole repeated key');inputs[p]=k;return raw;
}
const obj=p=>JSON.parse(read(p));
function write(n,b){fs.writeFileSync(OWN+'/'+n,b,{flag:'wx',mode:0o600});}
function json(n,v){write(n,JSON.stringify(v,null,2)+'\n');}
function rows(raw,absolute){
  const text=raw.toString();need(text.endsWith('\n'),'complete manifest LF');const out={};
  for(const line of text.slice(0,-1).split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);need(m&&!Object.hasOwn(out,m[2]),'unique manifest row');
    need(path.posix.normalize(m[2])===m[2]&&!m[2].split('/').includes('..'),'safe manifest path');same(m[2].startsWith('/'),absolute,'explicit manifest base');out[m[2]]=m[1];}return out;
}
function byte(k){return {bytes:k.bytes,sha256:k.sha256};}
const seal=read(AUD+'/SHA256SUMS');same(pin(seal),{bytes:751,sha256:'945dcdb5f0027657a9ba8eef3650a48bf1596ad9aea8d57e86c6bbc4468fa87f'},'exact delivered independent seal');
const manifest=rows(seal,false);same(Object.keys(manifest).length,9,'whole nine payloads');
same(fs.readdirSync(AUD).sort(),[...Object.keys(manifest),'SHA256SUMS'].sort(),'whole ten-file inventory');
for(const[n,h]of Object.entries(manifest)){need(!fs.lstatSync(AUD+'/'+n).isSymbolicLink(),'physical independent payload');same(pin(read(AUD+'/'+n)).sha256,h,'all independent nonself hashes');}
same(Object.keys(manifest).reduce((n,k)=>n+inputs[AUD+'/'+k].bytes,0)+seal.length,644302,'whole independent package bytes');
const original=obj(AUD+'/CHECKS_NATIVE.json');same(original.records.length,1,'one actual original helper invocation');
const one=original.records[0];same(one.request.cmd,'node docs/papers211_215_sequence/qa/p212_runtime_discovery_independent01/receive_discovery.js','actual original checker source');
same(one.result.exit_code,0,'actual original checker success');same(one.result.chunk_id,'280c9b','actual original chunk');need(!one.result.session_id,'original completed native return');
const old=JSON.parse(one.result.output);same(old.checks,109613,'whole original predicate count');same(old.input_files,228,'whole original key');same(old.state_paths,336,'whole original state scope');
for(const[p,k]of Object.entries(old.input_pins)){read(p);same(inputs[p],k,'whole original rich key received');}
const external=rows(read(AUD+'/INPUTS.sha256'),true);
same(external,Object.fromEntries(Object.entries(old.input_pins).filter(([p])=>![AUD+'/receive_discovery.js',AUD+'/ELF_NATIVE.json'].includes(p)).map(([p,k])=>[p,k.sha256])),'exact entire 226-file external manifest');
same(Object.keys(external).length,226,'external count');
const reads=obj(AUD+'/NATIVE_READS.json'),closing=obj(AUD+'/CLOSING_NATIVE.json'),sup=obj(AUD+'/SUPPLEMENTAL_NATIVE.json'),elf=obj(AUD+'/ELF_NATIVE.json');
same(reads.records.length,26,'all26 source/metadata native records');same(closing.records.length,8,'all8 closing native records');same(sup.records.length,4,'all4 supplemental native records');
const recordGroups=[['reads',reads.records],['closing',closing.records],['supplement',sup.records],['ELF',[elf]],['checker',[one]]];
const recordCoverage=[];
for(const[group,list]of recordGroups)for(const[i,r]of list.entries()){
  need(typeof r.request.cmd==='string'&&r.request.cmd.length>0,'actual native command retained');
  need(typeof r.result.output==='string'&&typeof r.result.chunk_id==='string'&&Number.isInteger(r.result.exit_code),'complete actual native envelope');
  need(!r.result.session_id,'terminal native record');
  const wanted=group==='reads'&&i===8?2:group==='closing'&&i===5?1:0;same(r.result.exit_code,wanted,'exact successful or preserved failed native exit');
  recordCoverage.push({group,index:i,chunk:r.result.chunk_id,exit_code:r.result.exit_code,output:pin(Buffer.from(r.result.output))});
}
function record(id){const r=reads.records.find(r=>r.record_id===id);need(r,'known exact source read');return r;}
for(const[n,ids]of [['prepare_runtime.py',['p212discaudit_source0']],['runtime_core.py',['p212discaudit_source1']],['p212_runtime.py',['p212discaudit_source2','p212discaudit_source3']]]){
  let line=0,body='';for(const id of ids){const raw=record(id).result.output;const ls=raw.split('\n');same(ls.pop(),'','whole numbered read LF');
    for(const s of ls){const m=/^\s*(\d+)\t(.*)$/.exec(s);need(m,'whole numbered source row');same(Number(m[1]),++line,'all source lines ordered');body+=m[2]+'\n';}}
  need(Buffer.from(body).equals(read(PREP+'/'+n)),'entire independent source read bytes');
}
const rootRead=['run.py','AUTHORITY.md','APPROVAL.json','ROOT_NATIVE01.json'].map(n=>CONTROL+'/'+n);
need(Buffer.concat(rootRead.map(read)).equals(Buffer.from(record('p212discaudit_root_read0').result.output)),'four complete actual root read bodies');
for(const[id,files]of [['p212discaudit_static_native0',['/usr/bin/ldd']],['p212discaudit_static_native1',[QA+'p212_runtime_discovery01/commands/03_ldd_before/stdout.raw',QA+'p212_runtime_discovery01/commands/04_ldd_after/stdout.raw']],['p212discaudit_static_native2',[QA+'p212_runtime_discovery01/commands/01_source_diff_0/stdout.raw',QA+'p212_runtime_discovery01/commands/01_source_diff_1/stdout.raw']],['p212discaudit_static_native3',[QA+'p212_runtime_discovery01/commands/01_source_diff_2/stdout.raw']]])
  need(Buffer.concat(files.map(read)).equals(Buffer.from(record(id).result.output)),'whole actual native/static read bodies');
for(const i of [0,1,2])same(closing.records[i].result.output,'','actual successful native source cmp empty');
same(closing.records[3].result.output,Object.keys(external).map(p=>p+': OK\n').join(''),'entire actual external native sha output');
need(Buffer.from(closing.records[4].result.output).equals(read(AUD+'/SUPPLEMENTAL_NATIVE.json')),'whole supplement actual read output');
need(closing.records[5].result.output.includes('TypeError'),'preseal selector failure preserved');
const preseal=JSON.parse(closing.records[7].result.output);same(preseal.preseal_payload_count,8,'all eight preseal payloads');
same(Object.keys(preseal.preseal_key).sort(),Object.keys(manifest).filter(n=>n!=='CLOSING_NATIVE.json').sort(),'exact preseal inventory');
for(const[n,k]of Object.entries(preseal.preseal_key))same(pin(read(AUD+'/'+n)),k,'whole preseal bytes retained');
same(sup.records.map(r=>r.result.chunk_id),['2483ab','0c6e8b','845d04','37536e'],'exact diagnostic native origins');
same(sup.relevant_checked_pins.length,10,'all ten supplement byte pins');
for(const k of sup.relevant_checked_pins)same(pin(read(k.path)),byte(k),'every supplemental pin');
same(sup.provenance_limitations.length,5,'all supplemental limitations retained');
const findings=obj(AUD+'/FINDINGS.json');same(findings.current_open,{Critical:0,Major:0,Minor:0},'actual independent census');same(findings.findings,[],'no invented findings');same(findings.decision,'GO_INITIAL_BINDING_PREPARATION_ONLY','exact limited independent decision');
const report=read(AUD+'/REPORT.md').toString();let links=0;
for(const m of report.matchAll(/\]\(([^)]+)\)/g)){const p=path.resolve(AUD,m[1]);need(fs.existsSync(p),'every report reference resolves');links++;}
read(OWN+'/receive.js');read('/usr/bin/node');read('/usr/bin/cmp');
// This is explicitly a new root execution of the unchanged independent
// documentary checker, not a second independent implementation or science.
function command(label,argv){
  const attempt={argv,cwd:ROOT,environment:ENV,stdin:'ignore',timeout_ms:60000,started_utc:new Date().toISOString()};json(label+'.ATTEMPT.json',attempt);
  const r=cp.spawnSync(argv[0],argv.slice(1),{cwd:ROOT,env:ENV,input:Buffer.alloc(0),timeout:60000,maxBuffer:8*1024*1024});
  const stdout=r.stdout||Buffer.alloc(0),stderr=r.stderr||Buffer.alloc(0);write(label+'.stdout.raw',stdout);write(label+'.stderr.raw',stderr);
  const receipt={...attempt,ended_utc:new Date().toISOString(),exit_code:r.status,signal:r.signal,pid:r.pid,error:r.error?String(r.error):null,stdout:pin(stdout),stderr:pin(stderr),scope:'actual bounded read-only documentary child; no independent whole process-tree settlement claim'};
  json(label+'.RECEIPT.json',receipt);native.push({label,...receipt});same(r.status,0,'actual root documentary child success');same(r.signal,null,'no signal');need(!r.error,'no spawn/capture failure');same(stderr.length,0,'empty actual root documentary stderr');return stdout;
}
write('independent_original.stdout.raw',Buffer.from(one.result.output));
const replay=command('01_reused_independent_checker',['/usr/bin/node',AUD+'/receive_discovery.js']);
need(replay.equals(Buffer.from(one.result.output)),'entire original/reused checker byte equality');
command('02_actual_raw_cmp',['/usr/bin/cmp','--',OWN+'/01_reused_independent_checker.stdout.raw',OWN+'/independent_original.stdout.raw']);
for(const p of Object.keys(inputs))read(p);
const result={status:'PASS_ROOT_COMPLETE_DOCUMENTARY_IMPORT_DISCOVERY_RECEPTION_INITIAL_BINDING_PREPARATION_ONLY',checks,independent_reuse:{source:AUD+'/receive_discovery.js',checks:old.checks,input_files:old.input_files,state_paths:old.state_paths,whole_original_stdout:pin(replay),actual_raw_cmp:true},independent_package:{payloads:9,files:10,bytes:644302,seal:pin(seal)},native,original_native_records:recordCoverage,report_links:links,input_paths:Object.keys(inputs).length,input_pins:Object.fromEntries(Object.keys(inputs).sort().map(p=>[p,inputs[p]])),findings:findings.current_open,scientific_executions:0,submitted_python_or_probes_executed:0,canonical_adopted:false,operational_authority:false,limitations:findings.explicit_limitations};
json('RESULT.json',result);console.log(JSON.stringify({status:result.status,checks,input_paths:result.input_paths,independent_checks:old.checks,whole_reused_stdout:pin(replay),native_commands:native.length,original_native_records:recordCoverage.length,science_runs:0}));
