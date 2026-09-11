#!/usr/bin/env node
'use strict';
// Read only documentary pins/metadata; create only fresh owned mapping outputs.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),cp=require('child_process');
const ROOT='/root/autodl-tmp/symbolic_dynamics',B='docs/papers211_215_sequence';
const OWN=ROOT+'/'+B+'/qa/private_checkpoint03_scope_preparation01';
const BASE='7d43cb323adf7d27326263b8ce4158d4eefff43a',BARE='/root/symbolic-dynamics-private-sync-accepted-20260907.git';
const SCOPED=JSON.parse(fs.readFileSync(OWN+'/CANDIDATE_INVENTORY.json'));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function need(x,m){if(!x)throw Error(m);}
function key(p){const s=fs.lstatSync(p,{bigint:true});need(s.isFile()&&!s.isSymbolicLink()&&fs.realpathSync(p)===p,'unsafe '+p);
 const b=fs.readFileSync(p),t=fs.lstatSync(p,{bigint:true});for(const k of ['dev','ino','mode','size','mtimeNs','ctimeNs'])need(s[k]===t[k],'race '+p);
 return{bytes:b.length,sha256:sha(b),oid:crypto.createHash('sha1').update(Buffer.concat([Buffer.from('blob '+b.length+'\0'),b])).digest('hex')};}
function save(n,x){fs.writeFileSync(OWN+'/'+n,JSON.stringify(x,null,2)+'\n',{flag:'wx'});}
const inputs={},pins=new Map(),unrecognized=[];
function input(n){const p=ROOT+'/'+n;inputs[n]=key(p);return fs.readFileSync(p);}
function normalized(n){if(typeof n!=='string')return null;if(n.startsWith(ROOT+'/'))return n.slice(ROOT.length+1);
 if(/^(docs\/|papers\/|\.agents\/|SYMBOLIC_DYNAMICS_STATE\.md$|README\.md$|AGENTS\.md$)/.test(n)&&!n.includes('\n')&&!n.includes('\0'))return n;
 if(n.startsWith('/')&&!n.includes('\n')&&!n.includes('\0'))return n;return null;}
function add(n,d,source){const k=normalized(n);if(!k||!/[0-9a-f]{64}/.test(d??''))return false;
 const id=k+'\0'+d;const old=pins.get(id);if(old){if(!old.pin_sources.includes(source))old.pin_sources.push(source);}
 else pins.set(id,{original:k,sha256:d,pin_sources:[source]});return true;}
function walk(x,source,hint=null){
 if(!x||typeof x!=='object')return;
 if(!Array.isArray(x)&&typeof x.sha256==='string'){
   const options=[hint,x.path,x.source,x.original,x.original_path,x.source_path,x.key,x.absolute,x.resolved];
   let found=false;for(const n of options)found=add(n,x.sha256,source)||found;
   if(!found)unrecognized.push({source,keys:Object.keys(x),path_like:options.filter(n=>typeof n==='string').slice(0,3)});
 }
 if(Array.isArray(x)){for(const r of x)walk(r,source);}
 else for(const [k,v]of Object.entries(x))if(v&&typeof v==='object')walk(v,source,k);
}
const direct=B+'/qa/p211_lifecycle_root01/LIFECYCLE_INPUTS.json';
walk(JSON.parse(input(direct)),direct);
const pinFiles=Object.values(SCOPED.inventory).filter(r=>
 (r.category.includes('35_to_43')||r.category==='p211_admission_originals_and_pilot_failure')&&
 /(?:PIN|HISTOR|INPUT)/i.test(path.basename(r.git_path))&&/\.(?:sha256|json)$/.test(r.git_path)&&
 !r.git_path.includes('/native/')&&!r.git_path.includes('/evidence01/')&&!r.git_path.includes('/raw/'));
for(const r of pinFiles){
 const b=input(r.git_path);if(r.git_path.endsWith('.json'))walk(JSON.parse(b),r.git_path);
 else for(const line of b.toString().split('\n'))if(line){const m=line.match(/^([0-9a-f]{64})  (.+)$/);need(m,'pin framing '+r.git_path);
   if(!add(m[2],m[1],r.git_path))unrecognized.push({source:r.git_path,line});}
}
const selectedByHash=new Map();
for(const r of Object.values(SCOPED.inventory)){const a=selectedByHash.get(r.sha256)??[];a.push({path:r.git_path,oid:r.oid});selectedByHash.set(r.sha256,a);}
const rows=[],candidatePaths=new Set();
for(const v of pins.values()){
 const local=v.original.startsWith('/'),selected=!local?SCOPED.inventory[v.original]:null;
 const snapshots=selectedByHash.get(v.sha256)??[];
 let current=null;
 if(!local){const p=ROOT+'/'+v.original;if(fs.existsSync(p)&&fs.lstatSync(p).isFile()&&!fs.lstatSync(p).isSymbolicLink())current=key(p);
   candidatePaths.add(v.original);candidatePaths.add('symbolic_dynamics/'+v.original);}
 rows.push({...v,host_local:local,selected_current:!!selected,current,selected_snapshot_paths:snapshots.map(s=>s.path),
  expected_oid:current?.sha256===v.sha256?current.oid:snapshots[0]?.oid??null});
}
const env={PATH:'/usr/bin:/bin',LANG:'C',LC_ALL:'C',TZ:'UTC',GIT_OPTIONAL_LOCKS:'0',GIT_TERMINAL_PROMPT:'0',GIT_CONFIG_NOSYSTEM:'1',GIT_CONFIG_GLOBAL:'/dev/null'};
const prefix=['--git-dir='+BARE,'-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false','-c','core.untrackedCache=false','-c','gc.auto=0','-c','maintenance.auto=false','-c','commit.gpgSign=false'];
let serial=0;
function git(args){const name='dependency_git_'+String(++serial).padStart(2,'0'),argv=['/usr/bin/git',...prefix,...args];
 save(name+'_ATTEMPT.json',{argv,cwd:ROOT,environment:env,stdin_base64:'',timeout_ms:50000,max_buffer_bytes:16000000,started_utc:new Date().toISOString()});
 const r=cp.spawnSync(argv[0],argv.slice(1),{cwd:ROOT,env,input:Buffer.alloc(0),encoding:null,timeout:50000,maxBuffer:16000000,killSignal:'SIGKILL'});
 save(name+'_RESULT.json',{pid:r.pid??null,native_exit:r.status,signal:r.signal,error:r.error?String(r.error):null,
 stdout_base64:r.stdout?r.stdout.toString('base64'):null,stderr_base64:r.stderr?r.stderr.toString('base64'):null,ended_utc:new Date().toISOString()});
 need(r.status===0&&!r.error,'metadata command failed '+name);return r.stdout;
}
try{
 need(git(['rev-parse','refs/heads/main']).toString().trim()===BASE,'base advanced');
 const baseline={},targets=[...candidatePaths].sort();
 for(let i=0;i<targets.length;i+=100){
   const b=git(['ls-tree','-r','-z','--full-tree',BASE,'--',...targets.slice(i,i+100)]);
   need(b.length===0||b[b.length-1]===0,'truncated tree');
   for(const row of b.toString().split('\0').slice(0,-1)){
     const m=row.match(/^(\d+) blob ([0-9a-f]{40})\t(.+)$/);need(m,'bad metadata row');
     baseline[m[3]]={mode:m[1],oid:m[2]};
   }
 }
 for(const r of rows){
  r.exact_baseline_paths=r.host_local||!r.expected_oid?[]:[r.original,'symbolic_dynamics/'+r.original].filter(p=>baseline[p]?.oid===r.expected_oid);
  r.classification=r.host_local?'HOST_LOCAL_ONLY_NO_COPY':
   SCOPED.inventory[r.original]?.sha256===r.sha256?'EXACT_SELECTED_ORIGINAL':
   r.exact_baseline_paths.length?'EXACT_ACCEPTED_BASELINE_OBJECT':
   r.selected_snapshot_paths.length?'EXACT_SELECTED_HISTORICAL_SNAPSHOT':
   'LOCAL_ONLY_OR_UNRESOLVED_NOT_PROMISED_IN_CHECKPOINT';
 }
 const original=JSON.parse(fs.readFileSync(OWN+'/LIFECYCLE_DEPENDENCY_BOUNDARY.json'));
 const directUnselected=original.dependencies.filter(r=>r.relative&&!r.selected).map(d=>rows.find(r=>r.original===d.relative&&r.sha256===d.recorded_sha256));
 need(directUnselected.length===16&&directUnselected.every(Boolean),'lost direct dependency');
 const summaries={};for(const r of rows)summaries[r.classification]=(summaries[r.classification]??0)+1;
 const boundaryRun='/root/symbolic-dynamics-closed-scout-checkpoint-4dtz40s2';
 const exactOld=['RUN.json','PLAN.json','executed_source.py','capture/MANIFEST.sha256','stage/MANIFEST.sha256','commit/MANIFEST.sha256','push/MANIFEST.sha256','frozen/SYMBOLIC_DYNAMICS_STATE.md','frozen/'+B+'/PIPELINE_STATE.md'];
 const protocolWorkspace=[B+'/qa/root_checkpoint_inspection02/RECEPTION.md',B+'/qa/root_checkpoint_inspection02/CAPTURE_APPROVAL.md',
  B+'/qa/private_checkpoint_preparation02/PLAN.md',B+'/qa/private_checkpoint_preparation02/checkpoint.py',
  '.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md','docs/research_state/HISTORY_AND_CAVEATS.md'];
 const oldBoundary={archive_role:'LOCAL_ONLY_EXACT_NINE_KEYS_NO_RECURSIVE_COPY_OR_GATE_REPLAY',
  archive:Object.fromEntries(exactOld.map(n=>[boundaryRun+'/'+n,key(boundaryRun+'/'+n)])),
  controlling_documents:Object.fromEntries(protocolWorkspace.map(n=>[n,key(ROOT+'/'+n)]))};
 for(const [n,k]of Object.entries(inputs))need(key(ROOT+'/'+n).sha256===k.sha256,'input changed '+n);
 need(git(['rev-parse','refs/heads/main']).toString().trim()===BASE,'base advanced after metadata reads');
 const currentControls=Object.fromEntries(['SYMBOLIC_DYNAMICS_STATE.md',B+'/PIPELINE_STATE.md'].map(n=>[n,{
   proposed:SCOPED.inventory[n],currently_observed:key(ROOT+'/'+n),
   frozen:false,policy:'Temporal pin only; final approved immutable mapping still required. Source drift invalidates this candidate capture boundary.'}]));
 save('HISTORICAL_DEPENDENCY_MAPPING.json',{status:'DOCUMENTARY_METADATA_MAPPING_NOT_REPLAY',base:BASE,
  source_key:key(__filename),input_pins:inputs,summary:summaries,unique_pin_rows:rows.length,
  scope:'Direct complete lifecycle ledger plus exact listed accepted scout/admission pin ledgers; not transitive proof or whole-history closure.',
  direct_lifecycle_16_workspace_dependencies:directUnselected,rows,
  unrecognized_path_shapes:unrecognized,commands:serial,current_controls:currentControls});
 save('PRIOR_PROTOCOL_LOCAL_ONLY_BOUNDARY.json',oldBoundary);
 console.log(JSON.stringify({status:'PASS_READONLY_DEPENDENCY_MAPPING',summary:summaries,unique_pin_rows:rows.length,
  input_ledgers:Object.keys(inputs).length,direct_lifecycle_16:directUnselected.map(r=>({path:r.original,classification:r.classification,git:r.exact_baseline_paths})),
  unresolved:rows.filter(r=>r.classification==='LOCAL_ONLY_OR_UNRESOLVED_NOT_PROMISED_IN_CHECKPOINT').map(r=>({path:r.original,sha256:r.sha256})),
  unrecognized_path_shapes:unrecognized.length,commands:serial}));
}catch(e){save('DEPENDENCY_FAILURE.json',{error:String(e),stack:e.stack,partial_outputs_preserved:true,no_retry:true});throw e;}

