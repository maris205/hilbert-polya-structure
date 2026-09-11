#!/usr/bin/env node
'use strict';
// Final preparation-only integrity check. No Git/native children/science/copy.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',B='docs/papers211_215_sequence';
const OWN=ROOT+'/'+B+'/qa/private_checkpoint03_scope_preparation01';
const hash=(b,a='sha256')=>crypto.createHash(a).update(b).digest('hex');
let checks=0;
function need(x,m){checks++;if(!x)throw Error(m);}
function key(p){const s=fs.lstatSync(p,{bigint:true});need(s.isFile()&&!s.isSymbolicLink()&&fs.realpathSync(p)===p,'unsafe '+p);
 const b=fs.readFileSync(p),t=fs.lstatSync(p,{bigint:true});for(const k of ['dev','ino','mode','size','mtimeNs','ctimeNs'])need(s[k]===t[k],'race '+p);
 return{bytes:b.length,sha256:hash(b),mode:s.mode&73n?'100755':'100644',oid:hash(Buffer.concat([Buffer.from('blob '+b.length+'\0'),b]),'sha1')};}
function j(n){return JSON.parse(fs.readFileSync(OWN+'/'+n));}
function members(p){const s=fs.lstatSync(p);need(!s.isSymbolicLink()&&fs.realpathSync(p)===p,'alias '+p);return s.isDirectory()?fs.readdirSync(p).sort().flatMap(n=>members(p+'/'+n)):[p];}
function save(n,x){fs.writeFileSync(OWN+'/'+n,JSON.stringify(x,null,2)+'\n',{flag:'wx'});}
try{
 const initial=j('CANDIDATE_INVENTORY.json'),final=j('FINAL_CANDIDATE_INVENTORY.json'),result=j('FINAL_CANDIDATE_RESULT.json');
 need(key(OWN+'/FINAL_CANDIDATE_INVENTORY.json').sha256==='c38a3ac6a2a08d3d1069d62abb15faa410a038b15cbe7853fa5b9c8e8a05f74f','final inventory digest');
 need(final.counts.files===8179&&final.counts.bytes===386132699,'final totals');
 const controls=['SYMBOLIC_DYNAMICS_STATE.md',B+'/PIPELINE_STATE.md'],drift=[];
 for(const r of Object.values(final.inventory)){
  const k=key(r.source_path),same=['bytes','sha256','mode','oid'].every(f=>r[f]===k[f]);
  if(!same&&controls.includes(r.git_path))drift.push({path:r.git_path,proposed:r,currently_observed:k,policy:'Temporal drift; no approved physical capture. Source proposal cannot be executed against replacement bytes.'});
  else need(same,'noncontrol selected changed '+r.git_path);
 }
 for(const g of final.groups){const actual=members(ROOT+'/'+g.relative).map(p=>path.relative(ROOT,p));need(actual.length===g.files&&actual.every(n=>final.inventory[n]),'membership '+g.relative);}
 for(const r of final.delta_preview){
  const n=final.inventory[r.git_path],expected=!r.old?'A':r.old.oid===n.oid&&r.old.mode===n.mode?'=':'M';
  need(r.status===expected,'exact status '+r.git_path);
 }
 const roles=j('READONLY_ROLE_RESULT.json');
 for(const[p,k]of Object.entries(roles.protected_before)){
   if(k.present===false)need(!fs.existsSync(p),'protected absent role changed '+p);
   else{const now=key(p);for(const f of ['bytes','sha256','mode','oid'])need(now[f]===k[f],'protected key '+p);}
 }
 const records=[];
 for(const stem of ['git','dependency_git']){
   const count=stem==='git'?12:56;
   for(let i=1;i<=count;i++){
    const n=stem+'_'+String(i).padStart(2,'0'),a=j(n+'_ATTEMPT.json'),r=j(n+'_RESULT.json');
    need(a.argv[0]==='/usr/bin/git'&&a.cwd===ROOT&&a.stdin_base64==='','native request '+n);
    let at=1;if(a.argv[at]==='-C')at+=2;else{need(a.argv[at]==='--git-dir=/root/symbolic-dynamics-private-sync-accepted-20260907.git','bare argv');at++;}
    while(a.argv[at]==='-c')at+=2;
    need(['rev-parse','symbolic-ref','rev-list','remote','status','show','ls-tree'].includes(a.argv[at]),'non-readonly native '+n);
    need(Number.isInteger(r.pid)&&r.pid>0&&r.native_exit===0&&r.signal===null&&!r.error,'native final '+n);
    need(typeof r.stdout_base64==='string'&&typeof r.stderr_base64==='string','raw encoded streams '+n);
    need(Buffer.from(r.stdout_base64,'base64').toString('base64')===r.stdout_base64&&Buffer.from(r.stderr_base64,'base64').length===0,'raw framing/nonempty stderr '+n);
    need(a.environment.GIT_OPTIONAL_LOCKS==='0'&&a.environment.GIT_CONFIG_GLOBAL==='/dev/null'&&a.environment.GIT_CONFIG_NOSYSTEM==='1','Git environment '+n);
    records.push({record:n,operation:a.argv[at],pid:r.pid,exit:r.native_exit,stdout_bytes:Buffer.from(r.stdout_base64,'base64').length,stderr_bytes:0});
   }
 }
 const helpers=[
 ['COLLECTION_TOOL_RETURN.json','collect_scope.js','PASS_LOCAL_READONLY_SCOPE_PREPARATION'],
 ['DEPENDENCY_TOOL_RETURN.json','map_dependencies.js','PASS_READONLY_DEPENDENCY_MAPPING'],
 ['SUPPLEMENT_TOOL_RETURN.json','supplement_scope.js','PASS_EXPLICIT_PIN_SHAPES_AND_OPTIONAL_BRIDGE_SIZING'],
 ['FINALIZATION_TOOL_RETURN.json','finalize_candidate.js','PASS_FINAL_SOURCE_ONLY_SCOPE_PREPARATION']];
 const native=[];
 for(const[n,source,status]of helpers){
  const x=j(n),r=x.result_final??x.result;
  need(r.exit_code===0&&!r.session_id,'helper complete '+n);
  need(x.attempt.source_sha256===key(OWN+'/'+source).sha256,'helper source '+n);
  if(x.result_final)need(x.result.session_id===x.poll.session_id&&Number.isInteger(x.result.session_id),'actual session chain '+n);
  const output=JSON.parse(r.output);need(output.status===status,'actual helper status '+n);
  native.push({record:n,source,status,initial_chunk:x.result.chunk_id,session:x.result.session_id??null,final_chunk:r.chunk_id,exit:r.exit_code});
 }
 const seals=j('ACCEPTED_SEAL_AND_LINK_CHECKS.json');
 need(seals.verified_seals.length===55&&seals.lifecycle_links.length===52,'known seal/link census');
 for(const s of seals.verified_seals)need(key(s.path).sha256===s.sha256,'known seal changed');
 const dep=j('HISTORICAL_DEPENDENCY_MAPPING.json');
 need(dep.direct_lifecycle_16_workspace_dependencies.length===16&&dep.direct_lifecycle_16_workspace_dependencies.every(r=>r.classification==='EXACT_ACCEPTED_BASELINE_OBJECT'&&r.exact_baseline_paths.length>0),'16 baseline mappings');
 need(j('PIN_SHAPE_SUPPLEMENT.json').shapes===200,'special shapes');
 const optional=j('OPTIONAL_OLD_SCOUT_BRIDGE_INVENTORY.json');
 need(Object.keys(optional.inventory).length===28,'optional bridge files');
 for(const r of Object.values(optional.inventory)){const k=key(r.source_path);for(const f of ['bytes','sha256','mode','oid'])need(k[f]===r[f],'optional changed');}
 const oldMapPath=B+'/qa/control_before_p212_dependency_source_received01/MAPPING.json';
 const map=JSON.parse(fs.readFileSync(ROOT+'/'+oldMapPath)),resolved=[];
 for(const r of map.files){
   const expected=initial.inventory[r.original_path],actual=key(ROOT+'/'+r.physical_copy_path);
   need(expected&&actual.bytes===expected.bytes&&actual.sha256===expected.sha256,'old candidate control physical mapping');
   resolved.push({original_path:r.original_path,physical_copy_path:r.physical_copy_path,key:actual});
 }
 need(resolved.length===2,'old control count');
 const output={status:'PASS_PREPARATION_INTEGRITY_NOT_CHECKPOINT_ACCEPTANCE',checks,
   final_candidate_sha256:result.inventory_key.sha256,counts:final.counts,git_native_records:records,
   actual_helper_tool_chains:native,protected_original_role_keys_unchanged:true,
   original_candidate_controls_exact_physical_resolution:{mapping_path:oldMapPath,mapping_key:key(ROOT+'/'+oldMapPath),rows:resolved},
   current_control_drift_since_proposal:drift,controls_frozen:false,main_selected_p212_packets:0,
   optional_bridge_selected:false,new_science:0,new_builds:0,new_views:0,input_copies:0,git_mutations:0,
   operative_executor_written:false,remote_requeried:false,hold_external:true,
   scope:'Documentary integrity only. Source-only candidate, current-role observations and original proofs/reviews remain distinct.'};
 output.checks=checks; // Include the final mapping-key read performed during object assembly.
 save('CLOSING_RESULT.json',output);
 console.log(JSON.stringify({status:output.status,checks,files:final.counts.files,bytes:final.counts.bytes,
   git_native_records:records.length,actual_helper_tool_chains:native.length,current_control_drift:drift.length,
   final_candidate_sha256:result.inventory_key.sha256,git_mutations:0,input_copies:0}));
}catch(e){save('CLOSING_FAILURE.json',{error:String(e),stack:e.stack,checks,failed_not_success:true,originals_preserved:true});throw e;}
