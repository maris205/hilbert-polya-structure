// Author document/data integrity checks only; never imports or executes reviewed Python/Bash.
'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const base = 'docs/papers211_215_sequence/qa/p213_minimal_observer_binding_preparation01/';
let checks = 0;
function ok(v,m) { checks++; if(!v) throw Error(m); }
const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
function metadata(s) { return Object.fromEntries(fields.map(k=>{ok(typeof s[k]==='bigint','integer metadata');return[k,String(s[k])];})); }
const keys = new Map();
const bodies = new Map();
function read(path) {
 const p = fs.lstatSync(path,{bigint:true});
 ok(p.isFile()&&!p.isSymbolicLink()&&p.nlink===1n,'ordinary document');
 const fd = fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 let a,b,z;
 try { a=metadata(fs.fstatSync(fd,{bigint:true})); b=fs.readFileSync(fd); z=metadata(fs.fstatSync(fd,{bigint:true})); } finally {fs.closeSync(fd);}
 ok(JSON.stringify(a)===JSON.stringify(z)&&JSON.stringify(a)===JSON.stringify(metadata(p))&&JSON.stringify(a)===JSON.stringify(metadata(fs.lstatSync(path,{bigint:true}))),'stable document');
 ok(BigInt(b.length)===BigInt(a.size),'whole EOF bytes');
 const key={path,bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex'),metadata:a};
 keys.set(path,key); bodies.set(path,b); return b;
}
function body(name){const path=base+name;return bodies.get(path)||read(path);}
function data(name){return JSON.parse(body(name).toString('utf8'));}
const old=data('INPUT_KEYS_NATIVE.json');
ok(old.result.exit_code===0,'actual six-key command succeeded');
const inputKeys=JSON.parse(old.result.output).keys;
ok(inputKeys.length===6,'six keys');
const inputPins=body('INPUTS.sha256').toString();
ok(inputPins===inputKeys.map(k=>k.sha256+'  '+k.path).join('\n')+'\n','six exact pins');
for(const k of inputKeys){read(k.path);ok(JSON.stringify(keys.get(k.path))===JSON.stringify(k),'unchanged old full key');}
const originalReads=data('SOURCE_READS_NATIVE.json').records;
ok(originalReads.length===6,'six raw original reads');
for(const r of originalReads){ok(r.result.exit_code===0,'native read success');ok(Buffer.from(r.result.output).equals(bodies.get(r.path)),'full original raw read equality');}
const archivePath=inputKeys[2].path;
const archive=JSON.parse(bodies.get(archivePath));
ok(inputKeys[0].sha256==='a83cade1aae8054b2ab8ec0dfa51f03ccbdd59a53a6fdff08dabd672dc375f93','root decision pin');
ok(inputKeys[1].sha256==='ba44b1b7c61b28d8180e4564d6c1e9f4363bfa683c9a8d4b2ed5fc5124661186','root seal pin');
ok(inputKeys[2].sha256==='024c8f6bc7530ea2321216f24c532071d3e7b6e0fa3bdc599ac203153803e1aa','archive pin');
ok(inputKeys[3].sha256==='97198b16d87c504a2574a773133f8a4574d01f1751d810146b1237bb6359e65b','frozen source pin');
ok(inputKeys[5].sha256==='5517fa99464c02c5d21170a133b0f5a6d540f18ca549dd6296503f2fc0d29d55','frozen source seal');
for(const [sealIndex,entryIndex,name]of[[1,0,'SELECTION.md'],[5,3,'observe.py'],[5,4,'BINDING_FORMAT.md']]){
 const line=inputKeys[entryIndex].sha256+'  '+name;
 ok(bodies.get(inputKeys[sealIndex].path).toString().trimEnd().split('\n').filter(x=>x===line).length===1,'selected original manifest membership');
}
const mapBytes=Buffer.from(archive.proc_maps);
ok(mapBytes.length===6692&&mapBytes.length===archive.proc_maps_bytes,'archived maps raw bytes');
ok(crypto.createHash('sha256').update(mapBytes).digest('hex')===archive.proc_maps_sha256,'archived maps raw digest');
const filter=data('ARCHIVE_FILTER.json');
const p=data('POLICY.proposed.json');
ok(p.enabled===false&&p.operation_authorized===false&&p.source_delta_implemented===false,'proposal stays disabled');
ok(p.old_exact_launch_record===null&&p.old_exact_module_rows===null,'no fabricated rows');
ok(Object.values(p.unresolved_observations).every(x=>x===null),'all current observations unresolved');
ok(p.proposed_paths.source_pins===null&&p.proposed_paths.capture_pins===null&&p.proposed_paths.directory_absence===null,'future pins/absence unresolved');
ok(filter.historical_not_current===true&&filter.selected_archive===archivePath,'historical boundary');
ok(filter.modules.length===57&&Object.keys(archive.modules).length===57,'57 archive modules');
const names=new Set();
for(const x of filter.modules){
 ok(!names.has(x.name),'unique old module');names.add(x.name);
 ok(JSON.stringify(x.archived_file)===JSON.stringify(archive.modules[x.name]),'historical module exact row');
 ok(typeof x.reason==='string'&&x.reason.length>30,'explicit module reason');
 ok(['PROPOSED_FINITE_CANDIDATE','REJECT_OLD_MODULE'].includes(x.disposition),'finite disposition');
}
ok(filter.modules.filter(x=>x.disposition==='PROPOSED_FINITE_CANDIDATE').length===32,'32 retained');
ok(filter.modules.filter(x=>x.disposition==='REJECT_OLD_MODULE').length===25,'25 rejected');
ok(filter.modules.find(x=>x.name==='__main__').disposition==='REJECT_OLD_MODULE','old main rejected');
const mp=p.module_policy;
ok(mp.file_modules.length===32,'32 candidate module rows');
ok(mp.builtin_early_names.length===13&&mp.builtin_helper_names.length===7&&mp.builtin_hash_conditional_names.length===6,'26 builtin mechanism-only names');
ok(Object.keys(mp.frozen_nominal_names).length===3,'three frozen');
const all=[...mp.builtin_early_names,...mp.builtin_helper_names,...mp.builtin_hash_conditional_names,...Object.keys(mp.frozen_nominal_names),...mp.file_modules.map(x=>x.name),'__main__'].sort();
ok(all.length===62&&new Set(all).size===62&&JSON.stringify(all)===JSON.stringify(mp.helper_and_closing_allowed_names),'exact 62 nonwildcard names');
ok(mp.early_allowed_names.length===23&&new Set(mp.early_allowed_names).size===23&&mp.early_allowed_names.every(x=>all.includes(x)),'23 early subset');
for(const list of [mp.early_required_names,mp.helper_and_closing_required_names])ok(list.every(x=>all.includes(x)),'required subset');
for(const x of filter.modules.filter(x=>x.disposition==='REJECT_OLD_MODULE'&&x.name!=='__main__'))ok(!all.includes(x.name),'no rejected wrapper admission');
function cache(path){return path.slice(0,path.lastIndexOf('/')+1)+'__pycache__/'+path.slice(path.lastIndexOf('/')+1,-3)+'.cpython-310.pyc';}
const sources=new Set(),caches=new Set();
const fileMap=new Map(p.files.map(x=>[x.lexical,x]));
ok(fileMap.size===69&&p.files.length===69&&p.bounds.files===69,'69 unique candidates');
for(const m of mp.file_modules){
 ok(filter.modules.some(x=>x.name===m.name&&x.disposition==='PROPOSED_FINITE_CANDIDATE'),'module justified by retained ledger');
 ok(m.file===archive.modules[m.name].path&&m.origin===m.file&&m.observed_row===null,'literal historical path only');
 ok(fileMap.has(m.file),'module file candidate');
 if(m.mechanism==='source_file'){
  ok(m.file.endsWith('.py')&&m.cache===cache(m.file),'static cache derivation');
  sources.add(m.file);caches.add(m.cache);
  ok(fileMap.has(m.cache),'cache candidate');
  ok(m.package_path===(m.file.endsWith('/__init__.py')?m.file.slice(0,-12):null),'package path derivation');
 }else{ok(m.mechanism==='extension_file'&&m.cache===null&&m.file.endsWith('.so'),'exact extension mechanism');}
}
ok(sources.size===29&&caches.size===29,'29 source/cache pairs');
for(const e of p.files){
 ok(e.lexical.startsWith('/')&&!e.lexical.includes('..')&&!e.lexical.includes('\\')&&!e.lexical.includes('//'),'finite literal path grammar');
 ok(e.final_policy==='must_equal_lexical'&&e.links_policy==='no_leaf_symlink','no guessed alias');
 ok(e.observed_presence===null&&e.observed_key===null&&typeof e.optional==='boolean','facts not prefilled');
 ok(e.roles.length>0&&new Set(e.roles).size===e.roles.length,'justified finite roles');
}
ok(filter.mapped_files.length===11&&Object.keys(archive.mapped_files).length===11,'11 archived maps');
for(const x of filter.mapped_files)ok(JSON.stringify(x.archived_key)===JSON.stringify(archive.mapped_files[x.path]),'exact historical map key');
const retainedMaps=filter.mapped_files.filter(x=>x.disposition==='PROPOSED_FINITE_CANDIDATE');
ok(retainedMaps.length===9&&p.map_policy.file_names.length===9,'nine candidate maps');
ok(retainedMaps.reduce((a,x)=>a+x.archived_key.bytes,0)===14212024,'historical retained native byte total');
for(const x of retainedMaps)ok(fileMap.get(x.path).roles.includes('mapped_file')&&p.map_policy.file_names.some(y=>y.path===x.path&&y.earliest_phase===x.earliest_phase),'exact mapped role');
for(const x of filter.mapped_files.filter(x=>x.disposition==='REJECT_OLD_ENVIRONMENT_MAP'))ok(!fileMap.has(x.path),'old locale map excluded');
ok(p.map_policy.special_names.length===6&&p.map_policy.no_executable_only_filter===true&&p.map_policy.actual_maps===null,'map scope');
ok(fileMap.get('/usr/lib/python310.zip').roles.includes('startup_zip_must_be_absent'),'zip absence-only');
ok(fileMap.get(p.proposed_paths.observer).optional===false&&fileMap.get('/usr/bin/python3.10').optional===false,'mandatory observer/interpreter');
ok(!p.files.some(x=>x.lexical.endsWith('/verify.py')),'no scientific verifier read');
const la=p.launch_admissibility,rc=p.root_choices;
ok(JSON.stringify(rc.child_environment)==='{"LANG":"C","LC_ALL":"C"}'&&JSON.stringify(rc.interpreter_flags)==='["-I","-S","-B"]','new exact launch environment/flags');
ok(la.full_actual_record===null&&la.pycache_prefix===null&&la.flag_names.length===17,'actual launch unresolved and full flag layout');
ok(Object.keys(la.flag_requirements).length===17&&la.flag_names.every(x=>Object.hasOwn(la.flag_requirements,x)),'all 17 flag policy fields');
ok(la.flag_requirements.utf8_mode===1&&la.flag_requirements.optimize===0&&la.cache_tag==='cpython-310','cache/UTF8 invariants');
ok(JSON.stringify(la.release)==='[3,10,12,"final",0]','new narrow supported release predicate');
ok(JSON.stringify(la.argv)===JSON.stringify([p.proposed_paths.observer])&&JSON.stringify(la.orig_argv)===JSON.stringify([rc.interpreter,'-I','-S','-B',p.proposed_paths.observer]),'direct argv policy');
ok(mp.direct_script.file===p.proposed_paths.observer&&mp.direct_script.spec==='must_be_null_not_missing'&&mp.direct_script.cached==='must_be_null','direct main policy');
for(const [kind,loader]of Object.entries(p.loader_permission_records)){
 ok(loader.length===3&&['class','instance'].includes(loader[0]),'qualified loader shape');
 ok(loader[1][0]==='value'&&loader[2][0]==='value','literal loader tags');
 ok(loader[0]===(['builtin','frozen'].includes(kind)?'class':'instance'),'class versus instance');
}
ok(Object.values(p.bounds).every(x=>Number.isSafeInteger(x)&&x>0),'positive finite bounds');
ok(p.bounds.modules===62&&p.bounds.maps_bytes===65536&&p.bounds.file_bytes===8388608&&p.bounds.total_bytes===67108864&&p.bounds.stdout_bytes===16777216,'justified bounded budget');
const finalReads=data('FINAL_READS_NATIVE.json').records;
ok(finalReads.length===5,'five authored readbacks');
for(const r of finalReads){const b=read(r.path);ok(r.result.exit_code===0&&Buffer.from(r.result.output).equals(b),'authored complete raw readback');}
const primary=data('PRIMARY_NATIVE.json').records;
ok(primary.length===8&&primary.every(x=>x.request&&typeof x.result==='string'&&x.result.length>0),'eight actual public returns');
const patch=data('PATCH_NATIVE.json');
ok(typeof patch.patch==='string'&&Object.hasOwn(patch,'result'),'actual construction patch return');
const orientation=data('ORIENTATION_NATIVE.json').records;
ok(orientation.length===4&&orientation.every(x=>x.result.exit_code===0),'orientation actual returns');
ok(bodies.get(inputKeys[3].path).toString().includes('BINDING = None\nif BINDING is None:'),'old source gate unchanged');
for(const name of ['PROPOSAL.md','READ_SCOPE.md','HANDOFF.md'])ok(body(name).toString().includes('SOURCE')||body(name).toString().includes('source'),'scope documents present');
const snapshots=[...keys.values()];
for(const k of snapshots){read(k.path);ok(JSON.stringify(keys.get(k.path))===JSON.stringify(k),'all complete keys stable');}
process.stdout.write(JSON.stringify({status:'AUTHOR_DOCUMENTARY_PROPOSAL_CHECK_ONLY',checks,keys:snapshots,old_full_read_bytes:inputKeys.reduce((a,x)=>a+x.bytes,0),authored_full_read_bytes:finalReads.reduce((a,x)=>a+Buffer.byteLength(x.result.output),0),retained_old_modules:32,rejected_old_modules:25,total_module_names:62,early_module_names:23,candidate_files:69,source_or_runtime_accepted:false,runtime_observed:false})+'\n');
