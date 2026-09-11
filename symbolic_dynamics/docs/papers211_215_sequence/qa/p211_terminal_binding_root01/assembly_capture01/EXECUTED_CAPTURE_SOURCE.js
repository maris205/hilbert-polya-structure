'use strict';
// One exact disabled documentary assembly, not an operational builder.
const fs=require('node:fs'),crypto=require('node:crypto'),u=require('node:util'),cp=require('node:child_process');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const HERE=QA+'p211_terminal_binding_root01',OUT=HERE+'/assembly_capture01',DRAFT=HERE+'/disabled_assembly01';
const PREP=QA+'p211_terminal_binding_preparation01',A=QA+'p211_terminal_binding_independent01',RECEPTION=QA+'p211_terminal_binding_source_root01';
const ENV={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'},KEYS=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];
const reads={};let checks=0;
function need(x,s){checks++;if(!x)throw Error(s);}
function eq(a,b,s){need(u.isDeepStrictEqual(a,b),s);}
function pin(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
function read(p){need(p.startsWith(ROOT+'/')||p==='/usr/bin/python3.10','exact read scope');const a=fs.lstatSync(p,{bigint:true});need(a.isFile()&&!a.isSymbolicLink()&&fs.realpathSync(p)===p,'ordinary exact path');const b=fs.readFileSync(p),z=fs.lstatSync(p,{bigint:true}),key={...pin(b),stat:KEYS.map(k=>String(a[k]))};eq(key.stat,KEYS.map(k=>String(z[k])),'stable whole stat');if(reads[p])eq(reads[p],key,'whole repeated key');reads[p]=key;return b;}
function obj(p){return JSON.parse(read(p));}
function put(n,v){const b=Buffer.isBuffer(v)?v:Buffer.from(JSON.stringify(v,null,2)+'\n');const fd=fs.openSync(OUT+'/'+n,'wx',0o600);try{fs.writeFileSync(fd,b);fs.fsyncSync(fd);}finally{fs.closeSync(fd);}}
function absent(p){try{fs.lstatSync(p);need(false,'must remain absent '+p);}catch(e){if(e.code!=='ENOENT')throw e;}}
need(process.cwd()===ROOT,'actual root cwd');eq({...process.env},ENV,'literal ENV4 only');
absent(OUT);absent(DRAFT);for(const i of [1,2])absent(ROOT+'/papers/211-kernel-image-projection-feedback/qa_final/cold_build_'+i);
read(__filename);read(HERE+'/ASSEMBLY_AUTHORITY.md');
const rec=obj(RECEPTION+'/RESULT.json');need(rec.status==='PASS_ROOT_TERMINAL_BINDING_SOURCE_AND_INDEPENDENT_METADATA_RECEPTION_ONLY'&&rec.independent_checks===22191&&rec.native_cmp_exit===0,'actual source reception');
read(RECEPTION+'/RECEPTION.md');read(RECEPTION+'/SHA256SUMS');
const old=JSON.parse(obj(A+'/NATIVE_CHECK.json').result.output);eq(old.read_stat_schema,KEYS,'whole original stat schema');
function prior(){for(const [n,p] of Object.entries(old.read_pins)){need(!n.startsWith('/')&&n.split('/').every(x=>x&&x!=='.'&&x!=='..'),'literal accepted input');eq(pin(read(ROOT+'/'+n)),p,'all190 input byte pins');eq(reads[ROOT+'/'+n].stat,old.read_stats[n],'all190 input rich stats');}}
prior();const plan=obj(PREP+'/INPUT_PLAN.json');for(const [n,p] of Object.entries(plan.input_pins))eq(pin(read(ROOT+'/'+n)),p,'all166 explicit plan pins');
const source=read(PREP+'/assemble_disabled.py');eq(pin(source),{bytes:14376,sha256:'5ffced2f708475a65c56ccff42759fca8fe01de34c5be6c8acc40c8a3edd61c6'},'exact fully read assembly source');
const executable=read('/usr/bin/python3.10');
fs.mkdirSync(OUT,{mode:0o700});put('INPUTS_BEFORE.json',reads);put('EXECUTED_CAPTURE_SOURCE.js',read(__filename));
const argv=['/usr/bin/python3.10','-I','-S','-B',PREP+'/assemble_disabled.py','--write-disabled-candidates'];
const at={argv,cwd:ROOT,environment:ENV,stdin:'empty pipe',timeout_ms:60000,started_utc:new Date().toISOString(),source:pin(source),executable:reads['/usr/bin/python3.10'],authority:pin(read(HERE+'/ASSEMBLY_AUTHORITY.md'))};put('ATTEMPT.json',at);
const r=cp.spawnSync(argv[0],argv.slice(1),{cwd:ROOT,env:ENV,input:Buffer.alloc(0),encoding:null,timeout:60000,maxBuffer:1024*1024});
const stdout=r.stdout||Buffer.alloc(0),stderr=r.stderr||Buffer.alloc(0);put('stdout.raw',stdout);put('stderr.raw',stderr);
const native={...at,ended_utc:new Date().toISOString(),status:r.status,signal:r.signal,error:r.error?{name:r.error.name,message:r.error.message,code:r.error.code||null}:null,stdout:pin(stdout),stderr:pin(stderr)};put('NATIVE.json',native);
need(r.status===0&&r.signal===null&&!r.error&&stderr.length===0,'actual disabled assembly native success');
const result=JSON.parse(stdout);eq(result,obj(DRAFT+'/RESULT.json'),'whole actual stdout equals saved result');need(result.status==='DISABLED_TERMINAL_CANDIDATES_ONLY_NOT_ROOT_ACCEPTANCE'&&!result.root_authority_issued&&!result.whole_round2_accepted&&result.builds===0,'actual disabled-only result');
const input=obj(DRAFT+'/INPUTS.json');for(const [p,v] of Object.entries(input))eq(pin(read(p)),v,'whole actual assembly consumed input');
const recipe=obj(PREP+'/LOCK_DERIVATION_PLAN.json'),original=obj(plan.original_lock.path),expected={...original,...recipe.new_field_values};
for(const i of [1,2]){const lockPath=DRAFT+'/build_'+i+'/DEPENDENCY_LOCK.candidate.json',raw=read(lockPath);eq(JSON.parse(raw),expected,'whole actual candidate exact four-field derivation');const disabled=obj(DRAFT+'/build_'+i+'/BINDING.disabled.json'),before=obj(PREP+'/BINDING_'+i+'.disabled.json');eq(disabled,{...before,dependency_lock:{path:lockPath,pin:pin(raw)}},'whole actual disabled binding only lock-reference delta');need(disabled.enabled===false&&disabled.cwd_relative_configuration===null&&disabled.root_authorization.issuer===null&&disabled.root_authorization.decision===null&&disabled.root_authorization.record===null,'all operational blockers retained');}
eq(read(DRAFT+'/build_1/DEPENDENCY_LOCK.candidate.json'),read(DRAFT+'/build_2/DEPENDENCY_LOCK.candidate.json'),'two equal raw candidate locks separate files');
prior();eq(read('/usr/bin/python3.10'),executable,'native executable unchanged');eq(read(PREP+'/assemble_disabled.py'),source,'actual submitted source unchanged');
for(const [p,v] of Object.entries({...reads})){read(p);eq(reads[p],v,'complete capture key closes');}put('INPUTS_AFTER.json',reads);
const summary={status:'ACTUAL_DISABLED_TERMINAL_ASSEMBLY_OUTPUT_RECEIVED_NO_BUILD_AUTHORITY',checks,read_paths:Object.keys(reads).length,actual_assembly:result,assembly_inputs:Object.keys(input).length,whole_stdout:pin(stdout),native_exit:0,builds:0,science:0,root_build_authority:false};put('RESULT.json',summary);process.stdout.write(JSON.stringify(summary)+'\n');
