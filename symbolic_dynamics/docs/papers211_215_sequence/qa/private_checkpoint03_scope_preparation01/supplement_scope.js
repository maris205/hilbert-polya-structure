#!/usr/bin/env node
'use strict';
// Exact original-location supplement. No Git or external/host execution.
// Only new metadata outputs are written; no source/payload copies occur.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',B='docs/papers211_215_sequence';
const OWN=ROOT+'/'+B+'/qa/private_checkpoint03_scope_preparation01';
const inv=JSON.parse(fs.readFileSync(OWN+'/CANDIDATE_INVENTORY.json')).inventory;
const hash=(b,a='sha256')=>crypto.createHash(a).update(b).digest('hex');
function need(x,m){if(!x)throw Error(m);}
function key(p){const s=fs.lstatSync(p,{bigint:true});need(s.isFile()&&!s.isSymbolicLink()&&fs.realpathSync(p)===p,'unsafe '+p);
 const b=fs.readFileSync(p),t=fs.lstatSync(p,{bigint:true});for(const k of ['dev','ino','mode','size','mtimeNs','ctimeNs'])need(s[k]===t[k],'race '+p);
 return{bytes:b.length,sha256:hash(b),mode:s.mode&73n?'100755':'100644',oid:hash(Buffer.concat([Buffer.from('blob '+b.length+'\0'),b]),'sha1')};}
function save(n,x){fs.writeFileSync(OWN+'/'+n,JSON.stringify(x,null,2)+'\n',{flag:'wx'});}
function members(p){const s=fs.lstatSync(p);need(!s.isSymbolicLink()&&fs.realpathSync(p)===p,'alias');return s.isDirectory()?fs.readdirSync(p).sort().flatMap(n=>members(p+'/'+n)):[p];}
try{
 const pilot=B+'/scouting/finite_semigroup_pilot', sources=[
 pilot+'/PRE_EXECUTION_PINS.json',B+'/scouting/kip_candidate_gate/pilot_archive/PRE_EXECUTION_PINS.json'];
 const first=fs.readFileSync(ROOT+'/'+sources[0]),second=fs.readFileSync(ROOT+'/'+sources[1]);
 need(first.equals(second),'archived prelock raw mismatch');
 const x=JSON.parse(first),rows=[];
 need(x.rows.length===98,'prelock census');
 for(const r of x.rows){
  const n=pilot+'/'+r.frozen,k=key(ROOT+'/'+n);need(inv[n]&&k.sha256===r.sha256&&k.bytes===r.bytes,'physical prelock key '+n);
  const origin=r.origin.startsWith(ROOT+'/')?r.origin.slice(ROOT.length+1):null;
  rows.push({...r,original_location_base:pilot,selected_frozen_path:n,key:k,
    current_original_selected:!!(origin&&inv[origin]&&inv[origin].sha256===r.sha256),
    origin_role:origin?'workspace original or prior pin; frozen exact key is selected':'host-local original; no current host read or copy'});
 }
 const dm=B+'/scouting/finite_semigroup_lane/MANIFEST.json',dk=key(ROOT+'/'+dm);
 need(inv[dm]&&dk.sha256===x.desk_manifest.sha256&&dk.bytes===x.desk_manifest.bytes,'desk manifest key');
 const controls=B+'/scouting/root_reception/ordered_algebra_memory/control_before_reception/MAPPING.json';
 const mappings=JSON.parse(fs.readFileSync(ROOT+'/'+controls)).map(r=>{
  const n=r.physical_original.slice(ROOT.length+1),k=key(r.physical_original);
  need(inv[n]&&k.sha256===r.pin.sha256&&k.bytes===r.pin.bytes,'physical control mismatch');
  return {...r,selected_physical_path:n,key:k,future_live_equality_required:false};});
 need(mappings.length===2,'control census');
 save('PIN_SHAPE_SUPPLEMENT.json',{status:'PASS_200_DECLARED_NON_GENERIC_SHAPES_EXPLICITLY_RESOLVED',
  source_key:key(__filename),generic_mapper_unchanged:true,
  shapes:200,composition:'Two copies of (98 origin/frozen rows plus one desk_manifest) plus two nested historical control pins.',
  original_prelock_sources:sources.map(n=>({path:n,key:key(ROOT+'/'+n)})),
  archive_copy_preserves_original_base:true,prelock_rows:rows,desk_manifest:{path:dm,key:dk},historical_controls:mappings,
  missing_launcher_environment_not_reconstructed:true,old_strict_audit_status:'FAIL_PRESERVED_NOT_REPAIRED',
  no_frozen_copy_or_host_read:true});
 const packages=[
  B+'/scouting/finite_word_tree_new_desk',
  B+'/scouting/finite_local_state_fresh_desk',
  B+'/qa/finite_pointer_output_receiver_preparation01',
  B+'/scouting/finite_nonlinear_feedback_fresh_desk'];
 const bridge={},groups=[];
 for(const p of packages){let bytes=0,n=0;for(const abs of members(ROOT+'/'+p)){
   const rel=path.relative(ROOT,abs);need(!inv[rel],'bridge overlaps core');const k=key(abs);bytes+=k.bytes;n++;
   bridge[rel]={source_path:abs,git_path:rel,...k,scope:'OPTIONAL_SEPARATE_APPROVAL_NOT_IN_CORE'};
  }groups.push({path:p,files:n,bytes});}
 const minimal=[
  packages[0]+'/HANDOFF.md',packages[1]+'/PROOF_PACKAGE.md',packages[3]+'/HANDOFF.md',
  ...Object.keys(bridge).filter(n=>n.startsWith(packages[2]+'/'))];
 const totals=ns=>({files:ns.length,bytes:ns.reduce((a,n)=>a+bridge[n].bytes,0)});
 save('OPTIONAL_OLD_SCOUT_BRIDGE_INVENTORY.json',{status:'OPTIONAL_PROPOSED_NOT_SELECTED_OR_APPROVED',
  reason:'Five exact inherited workspace pin versions outside the core/base. This inventories stable old source packets, not P212 current query/runtime archives.',
  groups,complete_four_packet_option:totals(Object.keys(bridge)),minimal_original_pin_plus_complete_receiver_option:totals(minimal),
  minimal_option_paths:minimal,inventory:bridge,
  transitive_boundary:'No recursive pointer history/runtime or further input closure is proposed; package-local and old temporal links remain original-location semantics.',
  core_inventory_unchanged:true});
 const categories={};for(const r of Object.values(inv)){const c=categories[r.category]??={files:0,bytes:0};c.files++;c.bytes+=r.bytes;}
 const unique=new Map(Object.values(inv).map(r=>[r.oid,r.bytes]));
 save('SIZE_AND_BOUNDARY_SUMMARY.json',{core:{files:Object.keys(inv).length,bytes:Object.values(inv).reduce((a,r)=>a+r.bytes,0),
   unique_blob_oids:unique.size,unique_blob_bytes:[...unique.values()].reduce((a,b)=>a+b,0),
   maximum_single_file_bytes:Math.max(...Object.values(inv).map(r=>r.bytes))},categories,
  optional_complete_bridge:totals(Object.keys(bridge)),optional_minimal_bridge:totals(minimal),
  current_p212_query_and_runtime_appendix:'NOT_SELECTED_OR_RECURSIVELY_SIZED',
  compression_or_remote_pack_size:'NOT_MEASURED_NOT_PREDICTED',
  failed_pilot_binaries:'Existing sealed workspace frozen copies are retained. No new host binaries were copied.'});
 console.log(JSON.stringify({status:'PASS_EXPLICIT_PIN_SHAPES_AND_OPTIONAL_BRIDGE_SIZING',shapes:200,
  unique_prelock_rows:98,archive_prelock_copy_raw_equal:true,historical_control_mappings:2,
  complete_bridge:totals(Object.keys(bridge)),minimal_bridge:totals(minimal),git_commands:0,copies:0,new_science:0}));
}catch(e){save('SUPPLEMENT_FAILURE.json',{error:String(e),stack:e.stack,no_retry:true,partial_outputs_preserved:true});throw e;}

