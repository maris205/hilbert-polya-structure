'use strict';
// Ordinary workspace documentary checker, not a P212 observer/probe/test.
// Reads only the fixed workspace documents below; never evaluates saved commands
// or loads/parses any inspected Python/JavaScript source as executable code.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const HERE=ROOT+'/docs/papers211_215_sequence/qa/p212_preprobe_native_mask_analysis01';
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
const ten=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const stamp=s=>Object.fromEntries(ten.map(k=>[k,String(s[k])]));
let checks=0;
const need=(x,m)=>{assert.ok(x,m);checks++;};
const equal=(a,b,m)=>{assert.deepEqual(a,b,m);checks++;};
const keys=[];
function whole(filename){
 need(filename.startsWith(ROOT+'/')&&path.normalize(filename)===filename,'fixed workspace file');
 const lst=fs.lstatSync(filename,{bigint:true});
 need(lst.isFile()&&!lst.isSymbolicLink()&&lst.size<=2000000n,'bounded physical workspace document');
 const fd=fs.openSync(filename,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 let raw;
 try{equal(stamp(fs.fstatSync(fd,{bigint:true})),stamp(lst),'same fd before document read');
  raw=fs.readFileSync(fd);
  equal(stamp(fs.fstatSync(fd,{bigint:true})),stamp(lst),'same fd after document read');
 }finally{fs.closeSync(fd);}
 equal(raw.length,Number(lst.size),'whole document length');
 equal(stamp(fs.lstatSync(filename,{bigint:true})),stamp(lst),'document endpoint');
 keys.push({path:filename.slice(ROOT.length+1),bytes:raw.length,sha256:digest(raw),endpoint:stamp(lst)});
 return raw;
}
const lines=whole(HERE+'/INPUT_SHA256SUMS').toString('utf8').trimEnd().split('\n');
const seen=new Set(),before=[],after=[];
for(const line of lines){
 const m=/^([a-f0-9]{64})  (docs\/papers211_215_sequence\/qa\/[A-Za-z0-9_./-]+)$/.exec(line);
 need(m&&!m[2].split('/').includes('..')&&!seen.has(m[2]),'exact unique workspace input pin');
 seen.add(m[2]);
 const raw=whole(ROOT+'/'+m[2]);equal(digest(raw),m[1],'unchanged selected input '+m[2]);
 before.push({path:m[2],bytes:raw.length,sha256:m[1]});
}
equal(before.length,23,'selected input census, not a dependency proof');
const frontierPath=ROOT+'/docs/papers211_215_sequence/qa/p212_preprobe_bootstrap_preparation01/FRONTIER.json';
const f=JSON.parse(whole(frontierPath));
equal(Object.keys(f).sort(),['schema','status','author_probe_execution_allowed','targets','allowed_components','closure_gaps'].sort(),'all frontier fields');
equal(f.schema,'p212-finite-preprobe-frontier-v1','original schema');
equal(f.status,'SOURCE_ONLY_INITIAL_FRONTIER_NOT_CLOSURE','original not-closure status');
equal(f.author_probe_execution_allowed,false,'no probe grant');
const components=p=>['/',...p.split('/').slice(1).filter(Boolean).map((_,i)=>'/'+p.split('/').slice(1,i+2).join('/'))];
equal(f.targets.map(t=>t.path),[...new Set(f.targets.map(t=>t.path))].sort(),'all target order and uniqueness');
equal(f.allowed_components,[...new Set(f.allowed_components)].sort(),'complete permitted component order');
for(const p of f.allowed_components){need(p.startsWith('/')&&path.posix.normalize(p)===p,'literal component spelling');
 for(const ancestor of components(p))need(f.allowed_components.includes(ancestor),'every literal component ancestor');}
for(const t of f.targets){
 equal(Object.keys(t).sort(),['path','mode','role','origin','max_bytes','capture_hex','max_members','expected_names'].sort(),'all target parameters');
 need(f.allowed_components.includes(t.path),'target explicitly permitted');
 need(typeof t.role==='string'&&t.role.length>0&&typeof t.origin==='string'&&t.origin.length>0,'actual role and provenance');
 need(['file','optional_file','directory','optional_directory','membership','absent','metadata'].includes(t.mode),'finite mode');
 need(Number.isSafeInteger(t.max_bytes)&&t.max_bytes>=0&&t.max_bytes<=134217728&&typeof t.capture_hex==='boolean','whole byte parameters');
 need(Number.isSafeInteger(t.max_members)&&t.max_members>=0&&t.max_members<=320,'member bound');
 if(t.mode==='membership'){
  need(Array.isArray(t.expected_names)&&t.expected_names.length<=t.max_members,'explicit bounded membership');
  equal(t.expected_names,[...new Set(t.expected_names)].sort(),'every member unique and ordered');
  for(const name of t.expected_names)need(typeof name==='string'&&!['','.','..'].includes(name)&&!name.includes('/')&&!name.includes('\0')&&Buffer.byteLength(name)<=255,'literal one-level name');
 }else equal([t.max_members,t.expected_names],[0,null],'no hidden membership');
 if(!['file','optional_file'].includes(t.mode))equal([t.max_bytes,t.capture_hex],[0,false],'no metadata body read');
}
equal(f.targets[3],{path:'/dev/null',mode:'metadata',role:'native validation or explicitly permitted component/alias role; never read device content',origin:'ARCHIVED_PATH_ONLY_NOT_CURRENT_KEY',max_bytes:0,capture_hex:false,max_members:0,expected_names:null},'exact fourth target');
equal(f.targets.filter(t=>t.path==='/dev'||t.path.startsWith('/dev/')).map(t=>t.path),['/dev/null'],'all literal dev-subtree targets');
need(f.allowed_components.includes('/dev')&&!f.targets.some(t=>t.path==='/dev'),'dev is ancestor-only allowance');
equal([f.targets.length,f.allowed_components.length],[164,204],'original census cross-check only');
equal(0x17ff&0xfff,0x7ff,'source-level mask conjunction, not another observation');
need(Array.isArray(f.closure_gaps)&&f.closure_gaps.length>0,'closure gaps retained');
const evidence=JSON.parse(whole(HERE+'/READS_NATIVE.json'));
equal(evidence.schema,'p212-source-only-native-mask-analysis-evidence-v1','documentary evidence schema');
need(Array.isArray(evidence.records)&&evidence.records.length===21,'saved evidence records present');
for(const row of evidence.records)need(typeof row.record==='string'&&row.value!==null&&row.value!==undefined,'saved data record');
const links=[];
for(const name of ['REPORT.md','OPTIONS.md']){
 const body=whole(HERE+'/'+name).toString('utf8');
 for(const m of body.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)){
  const rel=m[1].split('#')[0];need(!rel.includes('://'),'local document/source link only');
  const target=path.resolve(HERE,rel);need(target.startsWith(ROOT+'/'),'link remains in workspace');
  need(fs.lstatSync(target).isFile(),'linked workspace original exists');links.push({from:name,target:target.slice(ROOT.length+1)});
 }
 need(!body.includes('SOURCE_ACCEPTED_FOR_EXECUTION'),'no execution acceptance label');
}
for(const input of before){const raw=whole(ROOT+'/'+input.path);equal(digest(raw),input.sha256,'closing unchanged input '+input.path);after.push({path:input.path,bytes:raw.length,sha256:digest(raw)});}
equal(after,before,'complete selected before/after byte-hash vector');
process.stdout.write(JSON.stringify({schema:'p212-mask-analysis-document-check-v1',status:'DOCUMENTS_AND_SELECTED_INPUT_KEYS_CHECKED_NOT_SOURCE_OR_RUNTIME_ACCEPTANCE',checks,input_count:before.length,inputs_before:before,inputs_after:after,keys,links,frontier:{targets:f.targets.length,components:f.allowed_components.length,dev_target:f.targets[3]},not_performed:{source_execution:true,source_parse_or_AST:true,private_or_host_target_read:true,observer_or_probe:true,child_or_science:true,build:true,Git_SSH_external:true}},null,2)+'\n');
