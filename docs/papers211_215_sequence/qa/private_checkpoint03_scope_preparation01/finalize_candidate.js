#!/usr/bin/env node
'use strict';
// Additive final temporal-control proposal; no copy/Git/science or prior output edits.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',B='docs/papers211_215_sequence';
const OWN=ROOT+'/'+B+'/qa/private_checkpoint03_scope_preparation01';
const hash=(b,a='sha256')=>crypto.createHash(a).update(b).digest('hex');
function need(x,m){if(!x)throw Error(m);}
function key(p){const s=fs.lstatSync(p,{bigint:true});need(s.isFile()&&!s.isSymbolicLink()&&fs.realpathSync(p)===p,'unsafe '+p);
 const b=fs.readFileSync(p),t=fs.lstatSync(p,{bigint:true});for(const k of ['dev','ino','mode','size','mtimeNs','ctimeNs'])need(s[k]===t[k],'race '+p);
 return{bytes:b.length,sha256:hash(b),mode:s.mode&73n?'100755':'100644',oid:hash(Buffer.concat([Buffer.from('blob '+b.length+'\0'),b]),'sha1')};}
function save(n,x){const b=Buffer.from(JSON.stringify(x,null,2)+'\n');fs.writeFileSync(OWN+'/'+n,b,{flag:'wx'});return{bytes:b.length,sha256:hash(b)};}
function members(p){const s=fs.lstatSync(p);need(!s.isSymbolicLink()&&fs.realpathSync(p)===p,'alias '+p);return s.isDirectory()?fs.readdirSync(p).sort().flatMap(n=>members(p+'/'+n)):[p];}
try{
 const initialKey=key(OWN+'/CANDIDATE_INVENTORY.json'),v=JSON.parse(fs.readFileSync(OWN+'/CANDIDATE_INVENTORY.json'));
 const expected={
 'SYMBOLIC_DYNAMICS_STATE.md':{bytes:67918,sha256:'97a02532fe1c015fee817f0d9494e1deb22c3e1b3caa8dad263d77e583ae3786'},
 [B+'/PIPELINE_STATE.md']:{bytes:62541,sha256:'04abd6ea82962031e660fca9372cded0014da59ab23207eadbe382a88ad92d37'}};
 const changes=[];
 for(const [n,r]of Object.entries(v.inventory)){
   const k=key(r.source_path),want=expected[n];
   if(want){need(k.sha256===want.sha256&&k.bytes===want.bytes,'final control key mismatch '+n);
     changes.push({git_path:n,old:{bytes:r.bytes,sha256:r.sha256,oid:r.oid},new:k});
     Object.assign(r,k);
   }else for(const field of ['bytes','sha256','mode','oid'])need(k[field]===r[field],'noncontrol drift '+n);
   need(!n.startsWith('papers/212-')&&!n.startsWith(B+'/qa/p212_'),'P212 actual package selected');
 }
 for(const g of v.groups){
   const names=members(ROOT+'/'+g.relative).map(p=>path.relative(ROOT,p)).sort();
   need(names.length===g.files&&names.every(n=>v.inventory[n]),'membership drift '+g.relative);
   g.bytes=names.reduce((a,n)=>a+v.inventory[n].bytes,0);
 }
 for(const r of Object.values(v.inventory)){const k=key(r.source_path);for(const field of ['bytes','sha256','mode','oid'])need(k[field]===r[field],'closing drift '+r.git_path);}
 v.categories={};for(const r of Object.values(v.inventory)){const c=v.categories[r.category]??={files:0,bytes:0};c.files++;c.bytes+=r.bytes;}
 v.counts.bytes=Object.values(v.inventory).reduce((a,r)=>a+r.bytes,0);
 need(v.counts.files===8179&&v.counts.bytes===386132699,'final census');
 v.excluded=v.excluded.map(n=>n==='papers/212-closed-pointer-reversal'?'papers/212-closed-pointer-orbits':n);
 v.status='FINAL_PROPOSED_EXACT_SCOPE_NOT_AUTHORIZED_OR_FROZEN';
 v.initial_candidate_key=initialKey;v.finalizer_source_key=key(__filename);
 v.finalized_utc=new Date().toISOString();v.control_changes=changes;
 v.control_policy='Exact root-announced milestone keys checked twice. No input copy or immutable control capture occurred. Any later drift requires a new proposal or root-approved exact historical source mapping.';
 v.delta_preview=v.delta_preview.map(r=>({...r})); // Status remains A/M/=; original old Git objects unchanged.
 const inventoryKey=save('FINAL_CANDIDATE_INVENTORY.json',v);
 const unique=new Map(Object.values(v.inventory).map(r=>[r.oid,r.bytes]));
 const cap=fs.statfsSync('/root',{bigint:true}),available=cap.bavail*cap.bsize;
 const controlLinkBoundary=[];
 for(const n of Object.keys(expected)){
  const text=fs.readFileSync(ROOT+'/'+n,'utf8');
  for(const m of text.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){
   const literal=m[1];if(/^(?:https?:|#|mailto:)/.test(literal))continue;
   const clean=literal.split('#')[0];if(!clean)continue;
   const resolved=path.resolve(path.dirname(ROOT+'/'+n),clean),relative=path.relative(ROOT,resolved);
   if(!resolved.startsWith(ROOT+'/')){controlLinkBoundary.push({source:n,literal,resolved,role:'outside_workspace_reference'});continue;}
   const selected=!!v.inventory[relative]||(fs.existsSync(resolved)&&fs.statSync(resolved).isDirectory()&&members(resolved).every(p=>v.inventory[path.relative(ROOT,p)]));
   if(!selected)controlLinkBoundary.push({source:n,literal,resolved,relative,currently_exists:fs.existsSync(resolved),
    role:relative.startsWith(B+'/qa/p212_')||relative.startsWith('papers/212-')?'P212_EXCLUDED_LOCAL_ONLY_TEMPORAL_LINK':'NONSELECTED_BASELINE_OR_LOCAL_ONLY_REFERENCE'});
  }
 }
 save('FINAL_CONTROL_TEMPORAL_BOUNDARY.json',{status:'CURRENT_CONTROL_KEYS_VERIFIED_NOT_FROZEN',changes,
  actual_current_control_links_outside_selected_set:controlLinkBoundary,
  link_policy:'This is not global broken-link/semantic-closure certification. Existing earlier Git paths remain where documented. P212 and unselected local links are not silently synchronized.',
  original_exclusion_label_correction:'Initial explanatory label papers/212-closed-pointer-reversal did not exist; actual papers/212-closed-pointer-orbits is the final exclusion. Neither ever belonged to the exact positive allowlist.',
  new_copies:0});
 const budget=400000000;
 save('FINAL_CANDIDATE_RESULT.json',{status:'PASS_FINAL_SOURCE_ONLY_SCOPE_PREPARATION',inventory_key:inventoryKey,
   counts:v.counts,categories:v.categories,unique_blob_oids:unique.size,
   unique_blob_bytes:[...unique.values()].reduce((a,b)=>a+b,0),
   maximum_single_file_bytes:Math.max(...Object.values(v.inventory).map(r=>r.bytes)),
   capacity_observed:{available_bytes:available.toString(),statfs_time_utc:new Date().toISOString(),not_an_execution_reservation:true},
   proposed_hard_selected_bytes:budget,proposed_capture_free_space_floor_bytes:5*v.counts.bytes+budget,
   controls_frozen:false,operative_checkpoint_executor_written:false,git_mutations:0,input_copies:0,
   new_science:0,new_builds:0,new_views:0,private_push:false,hold_external:true});
 console.log(JSON.stringify({status:'PASS_FINAL_SOURCE_ONLY_SCOPE_PREPARATION',inventory_key:inventoryKey,
   counts:v.counts,controls_frozen:false,unique_blob_oids:unique.size,
   unique_blob_bytes:[...unique.values()].reduce((a,b)=>a+b,0),capacity_available_bytes:available.toString(),
   nonselected_control_links:controlLinkBoundary.length}));
}catch(e){save('FINALIZATION_FAILURE.json',{error:String(e),stack:e.stack,partial_outputs_preserved:true,no_retry:true});throw e;}

