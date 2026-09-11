'use strict';
// Root-owned one-shot capture of the accepted disabled documentary assembler.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),cp=require('node:child_process'),assert=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const HERE=QA+'p211_round2_binding_root01/',PREP=QA+'p211_round2_binding_preparation01/';
const OUT=HERE+'assembly01/',DRAFT=QA+'p211_round2_binding_root/disabled_selection01/';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'},inputs={};
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p,k){const s=fs.lstatSync(p);assert(s.isFile()&&!s.isSymbolicLink()&&fs.realpathSync(p)===p);const b=fs.readFileSync(p),v=pin(b);if(k)assert.deepStrictEqual(v,{bytes:k.bytes,sha256:k.sha256});if(inputs[p])assert.deepStrictEqual(v,inputs[p]);inputs[p]=v;return b;}
function write(n,b){fs.writeFileSync(OUT+n,b,{flag:'wx',mode:0o600});}
function jsonWrite(n,o){write(n,JSON.stringify(o,null,2)+'\n');}
assert.equal(process.cwd(),ROOT);assert.deepStrictEqual({...process.env},ENV);
assert(!fs.existsSync(OUT)&&!fs.existsSync(DRAFT));
for(const p of [QA+'p211_round2_execution01',ROOT+'/papers/211-kernel-image-projection-feedback/frozen_round2',ROOT+'/papers/211-kernel-image-projection-feedback/qa_final'])assert(!fs.existsSync(p));
const sourceKey=JSON.parse(read(HERE+'source_reception01/INPUTS.json'));
read(HERE+'source_reception01/RECEPTION.md');read(HERE+'ASSEMBLY_AUTHORITY.md');read(__filename);
read(HERE+'ASSEMBLY_CAPTURE_CORRECTION01.md');read(HERE+'FAILED_ASSEMBLY_NATIVE01.json');read(HERE+'FAILED_ASSEMBLE_CAPTURE01.js');
for(const [base,sealHash]of [[PREP,'8c640abe8708bac71416cc062cc94728b34a4b3daa5100030863f456605a67b9'],[QA+'p211_round2_binding_source_audit01/','6828243c2dd72d8966eda3fb9a0ba6b561af052d3e65a42f8101a438c142dbfe']]){
  const raw=read(base+'SHA256SUMS',sourceKey[base+'SHA256SUMS']);assert.equal(pin(raw).sha256,sealHash);
  for(const line of raw.toString().trimEnd().split('\n')){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);assert(m);assert.equal(pin(read(base+m[2],sourceKey[base+m[2]])).sha256,m[1]);}
}
assert.equal(inputs[PREP+'assemble_disabled.py'].sha256,'6fec3ca8f1d7f3bdf970db460acc967ba4a7991d9f0de3757718e2c5cec4f684');
assert.equal(JSON.parse(read(HERE+'source_reception01/RESULT.json')).status,'PASS_ROOT_BINDING_SOURCE_RECEPTION_ONLY');
const parent=path.dirname(DRAFT.slice(0,-1));if(!fs.existsSync(parent))fs.mkdirSync(parent,{mode:0o700});else assert(fs.lstatSync(parent).isDirectory()&&fs.realpathSync(parent)===parent);
fs.mkdirSync(OUT,{mode:0o700});
const argv=['/usr/bin/python3.10','-I','-S','-B',PREP+'assemble_disabled.py','--write-disabled-draft'];
const started=new Date().toISOString();jsonWrite('INPUTS_BEFORE.json',inputs);jsonWrite('ATTEMPT.json',{decision:'AUTHORIZE_ONE_DISABLED_P211_ROUND2_ASSEMBLY',argv,cwd:ROOT,environment:ENV,stdin:'empty pipe',timeout_ms:60000,started_utc:started});
const r=cp.spawnSync(argv[0],argv.slice(1),{cwd:ROOT,env:ENV,input:Buffer.alloc(0),encoding:null,timeout:60000,maxBuffer:8*1024*1024});
const stdout=r.stdout||Buffer.alloc(0),stderr=r.stderr||Buffer.alloc(0);write('stdout.raw',stdout);write('stderr.raw',stderr);
const receipt={argv,cwd:ROOT,environment:ENV,status:r.status,signal:r.signal,error:r.error?String(r.error):null,started_utc:started,ended_utc:new Date().toISOString(),stdout:pin(stdout),stderr:pin(stderr),scope:'actual direct documentary child only; no submitted native grandchildren'};jsonWrite('RECEIPT.json',receipt);
let result;try{
  assert.equal(r.status,0);assert.equal(r.signal,null);assert(!r.error);assert.equal(stderr.length,0);
  const actual=JSON.parse(stdout),saved=JSON.parse(read(DRAFT+'RESULT.json'));assert.deepStrictEqual(actual,saved);
  assert.equal(actual.status,'DISABLED_DRAFT_ASSEMBLED_PENDING_SEPARATE_ROOT_AUTHORITY');
  const key=JSON.parse(read(DRAFT+'INPUTS.json'));for(const[n,k]of Object.entries(key))read(ROOT+'/'+n,k);
  assert.equal(Object.keys(key).length,actual.workspace_read_paths);
  const b=JSON.parse(read(DRAFT+'BINDING_DISABLED_DRAFT.json'));
  assert.equal(b.enabled,false);assert.deepStrictEqual(b.root_authorization,{issuer:null,decision:null,record:null});
  assert.deepStrictEqual(b.host_reuse_boundary.precopy_recheck_references,[]);assert.equal(b.host_reuse_boundary.postcopy_root_recheck_required,true);
  let hosts=0;for(const v of Object.values(b.inherited_input_keys))for(const q of Object.values(v.resolutions))if(q.kind==='HOST_SEPARATE_ROOT'){assert.equal(q.accepted_resolution_reference,null);hosts++;}
  for(const l of b.pin_list_bases)for(const q of Object.values(l.resolutions))if(q.resolution.kind==='HOST_SEPARATE_ROOT'){assert.equal(q.resolution.accepted_resolution_reference,null);hosts++;}
  assert.deepStrictEqual(fs.readdirSync(DRAFT).sort(),['BINDING_DISABLED_DRAFT.json','INPUTS.json','RESULT.json']);
  for(const[n,k]of Object.entries({...inputs}))read(n,k);
  result={status:'PASS_ACTUAL_DISABLED_ASSEMBLY_PENDING_ENABLED_BINDING_RECEPTION',actual,host_resolution_rows_intentionally_null:hosts,capture_inputs:Object.keys(inputs).length,commands:1,science_runs:0,physical_round2_created:false};
}catch(e){result={status:'FAIL_PRESERVED',error:String(e),stack:e.stack};}
jsonWrite('INPUTS_AFTER.json',inputs);jsonWrite('RESULT.json',result);console.log(JSON.stringify(result));process.exitCode=result.status.startsWith('PASS_')?0:1;
