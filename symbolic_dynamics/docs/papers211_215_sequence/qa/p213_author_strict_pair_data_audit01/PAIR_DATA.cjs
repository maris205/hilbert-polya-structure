'use strict';
// Pure DATA adapter. No filesystem/process API and no producer import.
const control=require('../p213_initial_science_data_audit01/CONTROL_DATA.cjs');
const {typedEqual,canonicalIntegerJSON}=require('../p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs');
module.exports=function receivePair(runs,binding){
 let checks=0,scalarPairs=0,equalScalars=0,differentScalars=0;const differenceClasses={},mapPairs=[],outputDifferences=[];
 const need=(v,m)=>{checks++;if(!v)throw Error('pair-data: '+m);};
 const eq=(a,b,m)=>need(typedEqual(a,b),m);
 need(Array.isArray(runs)&&runs.length===2,'exact two distinct run records');
 const Q='docs/papers211_215_sequence/qa/',base='/root/autodl-tmp/symbolic_dynamics/';
 const names=['stdout.bin','stderr.bin','runtime_control.bin'],roles=['stdout','stderr','control'];
 const controls=[],ids=[];
 for(let i=0;i<2;i++){
  const run=runs[i],num=i===0?'01':'02',raw=Q+'p213_author_strict_pair_run'+num+'/';
  eq(Object.keys(run).sort(),['id','stage','nativeId','grantId','control','controlRaw','external'].sort(),'complete adapter run fields');
  eq(run.id,num,'exact run order/identity');eq(run.stage,'replay'+num,'exact stage identity');
  eq(run.nativeId,i===0?'2aa611':'384c57','actual distinct original native identity');
  eq(run.grantId,'P213_AUTHOR_STRICT_PAIR_NEW_RUN_'+num,'actual distinct consumed grant identity');
  need(Buffer.isBuffer(run.controlRaw),'original raw control buffer');
  need(Buffer.from(canonicalIntegerJSON(run.control)+'\n','ascii').equals(run.controlRaw),'whole lossless control raw binding '+num);
  eq(Object.keys(run.external).sort(),['raw','sources'],'exact external joins');
  eq(Object.keys(run.external.raw).sort(),roles.slice().sort(),'all three external raw roles');
  for(let j=0;j<3;j++){const k=run.external.raw[roles[j]];
   eq(k.path,raw+names[j],'exact per-run raw role/path '+num+' '+roles[j]);
   need(k.eof===true&&k.complete===true&&k.closed===true&&k.eof_zero_return===0,'complete separately received output key');
   eq(k.fd_before.mode,'33152','exact0600 raw');eq(k.fd_before.nlink,'1','single-link raw');
   eq(k.fd_before.uid,'0','root raw owner');eq(k.fd_before.gid,'0','root raw group');
   ids.push(k.fd_before.dev+':'+k.fd_before.ino);
  }
  eq(Object.keys(run.external.sources).sort(),[binding.observer,binding.science.source].sort(),'exact two current source joins');
  for(const p of [binding.observer,binding.science.source])eq(base+run.external.sources[p].path,p,'current source key exact lexical join');
  controls.push(control(run.control,binding,run.external));
 }
 need(new Set(ids).size===6,'six distinct actual raw identities, no run/role reuse');
 eq(runs[0].external.sources,runs[1].external.sources,'complete shared current source keys');
 function leafClass(path){
  if(/^\$\.(?:maps\[[0-4]\]|(?:pre_science|post_science|closing)\.maps)\.parsed\[\d+\]\.(?:start|end)$/.test(path))return 'individually_parsed_map_address';
  if(/^\$\.(?:maps\[[0-4]\]|(?:pre_science|post_science|closing)\.maps)\.raw_hex$/.test(path))return 'whole_reparsed_raw_map_bytes';
  if(/^\$\.(?:outputs_begin|outputs_final|(?:pre_science|post_science|closing)\.outputs)\.[123]\.(?:st_ino|st_mtime_ns|st_ctime_ns)$/.test(path))return 'separately_bound_output_identity_or_time';
  return null;
 }
 function walk(a,b,path){
  need(typeof a===typeof b,'shared scalar/container type '+path);
  if(a===null||b===null||typeof a!=='object'){
   scalarPairs++;if(a===b){equalScalars++;return;}
   differentScalars++;const kind=leafClass(path);need(kind!==null,'unapproved shared-key/scalar change '+path);
   need(kind==='whole_reparsed_raw_map_bytes'?typeof a==='string':typeof a==='bigint','exact dynamic-field type '+path);
   const label=path.replace(/\[\d+\]/g,'[*]');differenceClasses[label]=(differenceClasses[label]||0)+1;
   if(kind==='separately_bound_output_identity_or_time')outputDifferences.push({path,left:a.toString(),right:b.toString()});
   return;
  }
  need(Array.isArray(a)===Array.isArray(b),'shared container kind '+path);
  eq(Object.keys(a),Object.keys(b),'whole shared ordered member shape '+path);
  for(const k of Object.keys(a))walk(a[k],b[k],Array.isArray(a)?path+'['+k+']':path+'.'+k);
 }
 walk(runs[0].control,runs[1].control,'$');
 // All original maps were individually reparsed above. This retains each actual
 // endpoint and makes no normalized-map or cross-run same-address assertion.
 for(let i=0;i<5;i++){const a=runs[0].control.maps[i],b=runs[1].control.maps[i];
  mapPairs.push({phase:a.phase,left_bytes:a.byte_count.toString(),right_bytes:b.byte_count.toString(),
   raw_equal:a.raw_hex===b.raw_hex,address_pairs:a.parsed.map((r,j)=>({row:j,left:[r.start.toString(),r.end.toString()],right:[b.parsed[j].start.toString(),b.parsed[j].end.toString()]}))});
 }
 return {status:'PASS_TWO_NEW_CONTROLS_AND_COMPLETE_SHARED_KEYS_DATA_ONLY',checks,controls,scalarPairs,equalScalars,differentScalars,differenceClasses,outputDifferences,mapPairs,
  shared_file_records:140,shared_source_load:true,shared_launches:6,shared_module_snapshots:7,
  mapped_file_raw_reparsed_per_run:true,maps_normalized:false,host_hashes_recomputed:false,host_queries:false,science_execution:false,manuscript_review:false};
};
