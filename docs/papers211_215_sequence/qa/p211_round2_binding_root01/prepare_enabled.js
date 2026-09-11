'use strict';
// Root-only exact documentary enablement; no freeze, host import or science.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa/';
const HERE=QA+'p211_round2_binding_root01/',OUT=HERE+'enabled01/';
const PREP=QA+'p211_round2_binding_preparation01/',AUDIT=QA+'p211_round2_binding_source_audit01/';
const DRAFT=QA+'p211_round2_binding_root/disabled_selection01/';
const READS={},EXTRA={},checks=[];
function need(v,l){checks.push(l);assert(v,l);}
function same(a,b,l){checks.push(l);assert.deepStrictEqual(a,b,l);}
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function rel(p){const n=p.startsWith(ROOT+'/')?p.slice(ROOT.length+1):p;need(n&&!path.isAbsolute(n)&&path.posix.normalize(n)===n&&!n.split('/').some(x=>!x||x==='.'||x==='..'),'literal workspace spelling');return n;}
function read(p,k){p=ROOT+'/'+rel(p);const a=fs.lstatSync(p,{bigint:true});need(a.isFile()&&!a.isSymbolicLink()&&fs.realpathSync(p)===p,'ordinary explicit input');const b=fs.readFileSync(p),z=fs.lstatSync(p,{bigint:true});same([a.size,a.ino,a.mtimeNs,a.ctimeNs],[z.size,z.ino,z.mtimeNs,z.ctimeNs],'stable full read');const q=pin(b);if(k)same(q,{bytes:k.bytes,sha256:k.sha256},'original input pin');if(READS[p])same(q,READS[p],'closing whole input bytes');READS[p]=q;return b;}
function obj(p){return JSON.parse(read(p));}
function consume(p,k,role='actual root original evidence'){const b=read(p,k),n=rel(p);if(!EXTRA[n])EXTRA[n]={physical_path:n,pin:pin(b),roles:[role]};else same(EXTRA[n].pin,pin(b),'unique extra bytes');return b;}
function ref(p){consume(p);return {path:rel(p),pin:READS[ROOT+'/'+rel(p)]};}
function parseSums(b){need(b.at(-1)===10,'whole newline-terminated sum');const rows={};for(const line of b.toString().trimEnd().split('\n')){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);need(m&&!Object.hasOwn(rows,m[2]),'whole unique sum line');rows[m[2]]=m[1];}return rows;}
function members(base){const names=[],dirs=['.'];function walk(d){const p=base+(d?d+'/':'');need(fs.realpathSync(p)===p.replace(/\/$/,''),'physical tree directory');for(const e of fs.readdirSync(p,{withFileTypes:true})){const n=d?d+'/'+e.name:e.name;need(!e.isSymbolicLink(),'ordinary selected member');if(e.isDirectory()){dirs.push(n);walk(n);}else{need(e.isFile(),'file member');names.push(n);}}}walk('');return {files:names.sort(),dirs:dirs.sort()};}
function sealNew(base){const scope=members(base);need(!scope.files.includes('SHA256SUMS'),'new owned scope unsealed');const raw=scope.files.map(n=>pin(read(base+n)).sha256+'  '+n+'\n').join('');fs.writeFileSync(base+'SHA256SUMS',raw,{flag:'wx',mode:0o600});return scope.files.length;}
function tree(base,acceptance){const m=members(base),rows=parseSums(consume(base+'SHA256SUMS'));same(m.files,[...Object.keys(rows),'SHA256SUMS'].sort(),'exact complete nonself tree');for(const[n,h]of Object.entries(rows))same(pin(consume(base+n)).sha256,h,'entire sealed payload bytes');return {root:rel(base.replace(/\/$/,'')),files:m.files,empty_directories:[],manifest:'SHA256SUMS',accepted_scope_reference:ref(acceptance)};}
function actualNative(p,saved){const n=obj(p);const final=n.polls.length?n.polls.at(-1).result:n.result;need(final.exit_code===0&&!final.session_id,'actual complete outer native');const emitted=n.result.output+n.polls.map(x=>x.result.output).join('');same(JSON.parse(emitted),saved,'entire outer stdout/saved result');consume(p);}
need(process.cwd()===ROOT,'exact root cwd');need(!fs.existsSync(OUT),'exclusive enabled output');
for(const p of [QA+'p211_round2_execution01',ROOT+'/papers/211-kernel-image-projection-feedback/frozen_round2',ROOT+'/papers/211-kernel-image-projection-feedback/qa_final'])need(!fs.existsSync(p),'physical execution still absent');
const b=obj(DRAFT+'BINDING_DISABLED_DRAFT.json'),before=JSON.parse(JSON.stringify(b));
same(b.enabled,false,'disabled source draft');same(b.root_authorization,{issuer:null,decision:null,record:null},'no existing root authority');
const assembly=obj(HERE+'assembly01/RESULT.json');same(assembly.status,'PASS_ACTUAL_DISABLED_ASSEMBLY_PENDING_ENABLED_BINDING_RECEPTION','actual successful disabled reception');actualNative(HERE+'ASSEMBLY_NATIVE02.json',assembly);
const draftResult=obj(DRAFT+'RESULT.json'),draftKey=obj(DRAFT+'INPUTS.json');same([draftResult.workspace_read_paths,draftResult.external_files,draftResult.external_trees],[3107,3104,33],'actual source output scope');same(Object.keys(draftKey).length,3107,'whole actual source key');for(const[n,k]of Object.entries(draftKey))consume(n,k,'whole actual submitted assembly input');
same(assembly.actual,draftResult,'actual inner/outer result equality');
const pre=obj(HERE+'refresh02/precopy01/RESULT.json');same([pre.status,pre.checks,pre.read_paths,pre.r1_all_original_rows_full_stat_checked_twice],['PASS_COMPLETE_ACCEPTED_KEY_HOST_RUNTIME_AND_BUILD_SETTINGS_RECHECK',24347,3359,2255],'actual fresh full original rich precopy');actualNative(HERE+'refresh02/PRECOPY_NATIVE01.json',pre);
const preKey=obj(HERE+'refresh02/precopy01/READ_INPUTS.json');same(Object.keys(preKey).length,3359,'whole fresh precopy key');for(const[p,k]of Object.entries(preKey))if(p.startsWith(ROOT+'/'))consume(p,k,'actual precopy workspace original');
const build=obj(HERE+'refresh02/BUILD_PRECOPY_NATIVE01.json'),oldBuild=obj(QA+'p211_b_final_root/BUILD_REUSE_NATIVE01.json');same(build.result.exit_code,0,'actual new build-key check exit');same(build.result.output,oldBuild.result.output,'whole accepted build-key output unchanged');same(JSON.parse(build.result.output).checks,5974,'whole build-key comparator checks');
const rootFiles=['ASSEMBLY_AUTHORITY.md','ASSEMBLY_CAPTURE_CORRECTION01.md','ASSEMBLY_RECEPTION.md','PHYSICAL_AUTHORITY.md','assemble_capture.js','FAILED_ASSEMBLE_CAPTURE01.js','FAILED_ASSEMBLY_NATIVE01.json','FAILED_ASSEMBLY_SOURCE_COPY01.json','ASSEMBLY_NATIVE02.json','invoke_round2.py','prepare_enabled.js','refresh02/recheck.py','refresh02/BUILD_PRECOPY_NATIVE01.json','refresh02/PRECOPY_NATIVE01.json','refresh02/SOURCE_READ_NATIVE01.json'];
for(const n of rootFiles)consume(HERE+n);
// These are closed root-owned scopes; no whole live binding parent is sealed.
for(const p of [HERE+'source_reception01/',HERE+'assembly01/',DRAFT,HERE+'refresh02/precopy01/'])sealNew(p);
const newTrees=[
  tree(PREP,HERE+'source_reception01/RECEPTION.md'),tree(AUDIT,HERE+'source_reception01/RECEPTION.md'),
  tree(HERE+'source_reception01/',HERE+'PHYSICAL_AUTHORITY.md'),tree(HERE+'assembly01/',HERE+'ASSEMBLY_RECEPTION.md'),
  tree(DRAFT,HERE+'ASSEMBLY_RECEPTION.md'),tree(HERE+'refresh02/precopy01/',HERE+'ASSEMBLY_RECEPTION.md')];
const hostRef=ref(HERE+'refresh02/precopy01/RESULT.json');
same(b.host_reuse_boundary.precopy_recheck_references,[],'all old missing prechecks explicit');b.host_reuse_boundary.precopy_recheck_references=[hostRef];
let hostCount=0;const roleCounts=[];
for(const[role,spec]of Object.entries(b.inherited_input_keys)){
  const raw=obj(ROOT+'/'+spec.reference.path);same(Object.keys(spec.resolutions).sort(),Object.keys(raw).sort(),'whole original map preserved');let hosts=0;
  for(const[spelling,entry]of Object.entries(raw)){
    const q=spec.resolutions[spelling],k=spec.entry_layout==='WRAPPED_EXTERNAL_PIN'?entry.pin:entry;
    if(q.kind==='HOST_SEPARATE_ROOT'){same(q.physical_path,spelling,'literal absolute original host');same(q.accepted_resolution_reference,null,'only prior null host');q.accepted_resolution_reference=hostRef;hosts++;hostCount++;}
    else {same(q.kind,'WORKSPACE_FILE','ordinary workspace role');consume(q.physical_path,k,'complete inherited original workspace');}
  }
  roleCounts.push({role,rows:Object.keys(raw).length,host:hosts});
}
const inv=obj(QA+'p211_round2_preparation01/INTENDED_INVENTORY.json'),selection=Object.fromEntries(inv.rows.map(r=>[r.destination,r]));
const listCounts=[];for(const spec of b.pin_list_bases){const rows=parseSums(read(ROOT+'/'+selection[spec.document].source));same(Object.keys(rows).sort(),Object.keys(spec.resolutions).sort(),'whole copied list preserved');let hosts=0;for(const[p,h]of Object.entries(rows)){const q=spec.resolutions[p];same(q.pin.sha256,h,'unchanged original list digest');if(q.resolution.kind==='HOST_SEPARATE_ROOT'){same(q.resolution.physical_path,p,'exact original absolute list host');same(q.resolution.accepted_resolution_reference,null,'old list null remains prior missing');q.resolution.accepted_resolution_reference=hostRef;hosts++;hostCount++;}else consume(q.resolution.physical_path,q.pin,'entire list workspace original');}listCounts.push({document:spec.document,rows:Object.keys(rows).length,host:hosts});}
same(hostCount,1730,'all and only missing host references filled');
same(Object.keys(b.document_origins).length,35,'whole MD origins');same(Object.keys(b.json_pin_bases).length,57,'whole JSON origins');
const external=new Map(b.external_inputs.map(r=>[r.physical_path,r]));same(external.size,3104,'original entire external rows');for(const row of external.values())read(row.physical_path,row.pin);
for(const[n,r]of Object.entries(EXTRA)){if(external.has(n))same(external.get(n).pin,r.pin,'old external immutable');else external.set(n,r);}
b.external_inputs=[...external.values()].sort((a,z)=>a.physical_path.localeCompare(z.physical_path,'en'));
b.external_trees.push(...newTrees);same(new Set(b.external_trees.map(r=>r.root)).size,39,'33 retained plus six exact new scopes');
b.enabled=true;b.root_authorization={issuer:'/root',decision:'AUTHORIZE_PHYSICAL_P211_ROUND2_FROM_ACCEPTED_FINAL_B',record:ref(HERE+'PHYSICAL_AUTHORITY.md')};
// Authority ref already in EXTRA/external before map assembly; never a future output.
need(external.has(b.root_authorization.record.path),'actual authority fully consumed');
const reversed=JSON.parse(JSON.stringify(b));reversed.enabled=false;reversed.root_authorization=before.root_authorization;
reversed.host_reuse_boundary.precopy_recheck_references=[];reversed.external_inputs=before.external_inputs;reversed.external_trees=before.external_trees;
for(const spec of Object.values(reversed.inherited_input_keys))for(const q of Object.values(spec.resolutions))if(q.kind==='HOST_SEPARATE_ROOT')q.accepted_resolution_reference=null;
for(const spec of reversed.pin_list_bases)for(const q of Object.values(spec.resolutions))if(q.resolution.kind==='HOST_SEPARATE_ROOT')q.resolution.accepted_resolution_reference=null;
same(reversed,before,'exact field-level reverse delta preserves every old binding field');
for(const[p,k]of Object.entries({...READS}))read(p,k);
fs.mkdirSync(OUT,{mode:0o700});const bytes=Buffer.from(JSON.stringify(b,null,2)+'\n');fs.writeFileSync(OUT+'BINDING.json',bytes,{flag:'wx',mode:0o600});
const result={status:'PASS_EXACT_ENABLED_BINDING_PREPARATION_NO_FREEZE',checks:checks.length,read_paths:Object.keys(READS).length,binding:pin(bytes),original_external_files:3104,external_files:b.external_inputs.length,external_trees:39,original_maps:roleCounts,sha_lists:listCounts,host_resolution_rows_bound:hostCount,source_and_plan_fields_preserved_by_exact_reverse_delta:true,precopy_reference:hostRef,root_authority:b.root_authorization,scientific_runs:0,physical_round2_created:false};
for(const[n,v]of [['RESULT.json',result],['INPUTS.json',READS]])fs.writeFileSync(OUT+n,JSON.stringify(v,null,2)+'\n',{flag:'wx',mode:0o600});
console.log(JSON.stringify(result));
