"use strict";
// Independent predicates on received DATA only. No file or process APIs in this module.
const {typedEqual,canonicalIntegerJSON}=require("./LOSSLESS_JSON.cjs");
module.exports=function receiveRuntime(x,binding,sourceExternal){
 let checks=0,taggedFacts=0,moduleRows=0,statFields=0,mapRows=0,mapFileRows=0,mapSpecialRows=0;
 const ok=(v,m)=>{checks++;if(!v)throw Error("runtime-data: "+m);};
 const eq=(a,b,m)=>ok(typedEqual(a,b),m);
 const keys=(v,n,m)=>{ok(v!==null&&!Array.isArray(v)&&typeof v==="object",m+" object");eq(Object.keys(v).sort(),n.slice().sort(),m+" exact fields");};
 const arr=(v,m)=>ok(Array.isArray(v),m+" array");
 const integer=(v,m)=>ok(typeof v==="bigint",m+" exact integer token");
 const boundedString=(v,m)=>ok(typeof v==="string"&&v.length<=Number(binding.bounds.scalar_chars),m+" bounded string");
 const unique=(xs,m)=>ok(new Set(xs).size===xs.length,m+" unique");
 const setdiff=(a,b)=>[...new Set(a)].filter(z=>!new Set(b).has(z)).sort();
 const nullOrMissing=v=>typedEqual(v,["null"])||typedEqual(v,["missing"]);
 function frozen(v){if(v===null)return ["null"];if(Array.isArray(v))return ["sequence",v.map(frozen)];if(["string","bigint","boolean"].includes(typeof v))return ["value",v];throw Error("unsupported binding value");}
 function tag(v,label){
  taggedFacts++;arr(v,label);ok(v.length>=1&&typeof v[0]==="string",label+" tag name");
  if(v[0]==="missing"||v[0]==="null"){ok(v.length===1,label+" one-member missing/null");return;}
  ok(v.length===2,label+" two-member scalar/sequence");
  if(v[0]==="value"){ok(["string","bigint","boolean"].includes(typeof v[1]),label+" exact allowed scalar type");if(typeof v[1]==="string")boundedString(v[1],label);return;}
  ok(v[0]==="sequence",label+" supported sequence tag");arr(v[1],label+" contents");ok(BigInt(v[1].length)<=binding.bounds.sequence_items,label+" sequence bound");for(const z of v[1])tag(z,label+" child");
 }
 function path(p,label){boundedString(p,label);ok(/^\/[\x20-\x7e]+$/.test(p)&&!p.includes("\\")&&!p.slice(1).split("/").some(s=>["",".",".."].includes(s)),label+" exact lexical grammar");}
 keys(binding,["id","interpreter","observer","cwd","launch_policy","flag_names","module_names","required_module_names","modules","loader_ids","special_maps","files","bounds"],"binding");
 const boundExpected={modules:62n,maps_bytes:65536n,files:69n,file_bytes:8388608n,total_bytes:67108864n,scalar_chars:1024n,sequence_items:128n,link_hops:1n,stdout_bytes:16777216n};
 eq(binding.bounds,boundExpected,"exact accepted numeric bounds");path(binding.observer,"observer role");path(binding.cwd,"cwd role");
 arr(binding.files,"file permissions");ok(binding.files.length===69,"69 permissions");
 const entries=new Map();for(const e of binding.files){
  keys(e,["lexical","final","links","optional","absence_required","earliest_phase","roles","observed_presence","observed_key"],"permission");path(e.lexical,"permission path");eq(e.final,e.lexical,"same lexical/final permission");eq(e.links,[],"no leaf aliases permitted");
  ok(!entries.has(e.lexical),"unique permission path");entries.set(e.lexical,e);ok(typeof e.optional==="boolean"&&typeof e.absence_required==="boolean","actual boolean permission fields");
  ok(["early","helper"].includes(e.earliest_phase),"permission phase");arr(e.roles,"permission roles");unique(e.roles,"permission roles");ok(e.roles.length>0&&e.roles.every(r=>["direct_script_source","mapped_file","source_or_matching_source","eligible_nonoptimized_cache","extension_origin","startup_zip_must_be_absent"].includes(r)),"finite file role vocabulary");
  ok(e.absence_required===e.roles.includes("startup_zip_must_be_absent")&&(!e.absence_required||e.optional),"zip absence relation");ok(e.observed_presence===null&&e.observed_key===null,"permission placeholders not claimed observations");
 }
 eq(binding.interpreter,entries.get(binding.interpreter.lexical),"whole duplicated interpreter permission");ok(entries.get(binding.observer)?.optional===false&&binding.interpreter.optional===false,"mandatory source/interpreter");
 eq(binding.flag_names,binding.launch_policy.flag_names,"flag order duplicate");eq(Object.keys(binding.launch_policy.flag_requirements).sort(),binding.flag_names.slice().sort(),"complete flag policy");ok(binding.flag_names.length===17,"17 exact flags");
 for(const phase of["early","helper","closing"]){arr(binding.module_names[phase],"phase permissions");unique(binding.module_names[phase],"phase module names");ok(binding.module_names[phase].every(n=>Object.hasOwn(binding.modules,n)),"module permissions defined");ok(binding.required_module_names[phase].every(n=>binding.module_names[phase].includes(n)),"required module subset");}
 ok(Object.keys(binding.modules).length===62&&binding.module_names.early.length===23,"fixed module frontier");
 for(const [name,p]of Object.entries(binding.modules)){boundedString(name,"module policy name");ok(p.observed_row===null,"no predicted row");ok(Object.hasOwn(binding.loader_ids,p.mechanism),"finite mechanism");for(const r of p.file_roles){keys(r,["path","role","content_required"],"module permission role");path(r.path,"module role path");ok(entries.has(r.path)&&entries.get(r.path).roles.includes(r.role)&&typeof r.content_required==="boolean","role joins finite file entry");}}

 keys(x,["binding_id","closing_launch","closing_module_delta","closing_modules","closing_observed_map_additions","closing_roles","early_launch","early_modules","early_roles","environment","files","helper_launch","helper_module_delta","helper_modules","helper_observed_map_additions","helper_roles","maps","module_snapshots","process_after_keys","process_begin","process_closing","runtime_accepted","schema","second_launch","second_modules","status","total_file_read_bytes"],"successful raw document");
 ok(x.schema==="P213_FINITE_PERMISSION_OBSERVER_V2"&&x.binding_id===binding.id,"schema and non-grant label");ok(x.status==="OBSERVED_PENDING_INDEPENDENT_RECEPTION"&&x.runtime_accepted===false,"producer status is not acceptance");
 const statNames=["st_dev","st_ino","st_mode","st_nlink","st_uid","st_gid","st_rdev","st_size","st_mtime_ns","st_ctime_ns"];
 function stat(s,label){keys(s,statNames,label);for(const k of statNames){integer(s[k],label+" "+k);statFields++;}ok((s.st_mode&0o170000n)===0o100000n,label+" regular file mode");return s;}
 function point(p,e,label,absent){
  keys(p,absent?["absence","lexical","links"]:["absence","final_lstat","lexical","links"],label);eq(p.lexical,e.lexical,label+" lexical");eq(p.links,[],label+" no observed leaf aliases");
  if(absent){keys(p.absence,["errno","operation","path"],label+" absence");eq(p.absence,{errno:2n,operation:"lstat",path:e.lexical},label+" exact ENOENT operation");}
  else{ok(p.absence===null,label+" not absent");stat(p.final_lstat,label+" lstat");}
 }
 arr(x.files,"raw files");ok(x.files.length===binding.files.length,"one record for every finite permission");const keyed=new Map();let total=0n,complete=0,absent=0;
 for(let i=0;i<x.files.length;i++){
  const f=x.files[i],e=binding.files[i];eq(f.lexical,e.lexical,"fixed one-pass file order");eq(f.roles,e.roles,"complete role array");ok(!keyed.has(f.lexical),"unique actual record");keyed.set(f.lexical,f);
  integer(f.byte_count,"file byte_count");ok(typeof f.sha256_of_read_bytes==="string"&&/^[0-9a-f]{64}$/.test(f.sha256_of_read_bytes),"reported full/partial digest shape");
  if(f.absent===true){
   absent++;keys(f,["absent","begin","byte_count","closing","complete","eof","lexical","roles","sha256_of_read_bytes"],"absent record");ok(e.optional,"absence permitted");ok(f.byte_count===0n&&f.complete===false&&f.eof===false,"absence not a complete empty content key");eq(f.sha256_of_read_bytes,"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","empty read digest in absence");point(f.begin,e,"absence begin",true);point(f.closing,e,"absence closing",true);eq(f.begin,f.closing,"unchanged absence points");
  }else{
   complete++;keys(f,["after_read","begin","byte_count","closing","complete","eof","fd_after","fd_before","lexical","roles","sha256_of_read_bytes"],"complete record");ok(!e.absence_required&&f.complete===true&&f.eof===true,"complete present not required-absent");
   point(f.begin,e,"begin",false);point(f.after_read,e,"after-read",false);point(f.closing,e,"closing",false);stat(f.fd_before,"fd-before");stat(f.fd_after,"fd-after");
   eq(f.begin.final_lstat,f.fd_before,"path/fd initial identity");eq(f.fd_before,f.fd_after,"same fd endpoint identity");eq(f.begin,f.after_read,"path endpoint after read");eq(f.begin,f.closing,"closing full endpoint identity");
   ok(f.byte_count===f.fd_before.st_size&&f.byte_count>=0n&&f.byte_count<=binding.bounds.file_bytes,"whole EOF size and per-file bound");total+=f.byte_count;
  }
 }
 eq(x.total_file_read_bytes,total,"complete total content accounting");ok(total<=binding.bounds.total_bytes,"whole read total bound");
 const requiredAbsences=binding.files.filter(e=>e.absence_required).map(e=>e.lexical);eq(requiredAbsences,["/usr/lib/python310.zip"],"one required absence permission");ok(keyed.get(requiredAbsences[0]).absent===true,"required zip absence actually obtained");

 const launchNames=["executable","orig_argv","argv","version","version_info","path","prefix","base_prefix","exec_prefix","base_exec_prefix","dont_write_bytecode","pycache_prefix","platform","byteorder","abiflags","hexversion","maxsize","builtin_module_names"];
 function launch(r,label){
  arr(r,label);ok(r.length===7,label+" seven-part launch");const [values,flags,text,impl,streams,encoding,errors]=r;
  for(const [rows,names,sub]of[[values,launchNames,"values"],[flags,binding.flag_names,"flags"]]){arr(rows,sub);eq(rows.map(z=>z[0]),names,sub+" exact names/order");for(const row of rows){arr(row,sub);ok(row.length===2,sub+" pair");tag(row[1],sub);}}
  const v=Object.fromEntries(values),p=binding.launch_policy;
  const expected={executable:binding.interpreter.lexical,orig_argv:p.orig_argv,argv:p.argv,version_info:p.release,path:p.sys_path,prefix:p.prefixes_must_equal,base_prefix:p.prefixes_must_equal,exec_prefix:p.prefixes_must_equal,base_exec_prefix:p.prefixes_must_equal,dont_write_bytecode:p.dont_write_bytecode,pycache_prefix:p.pycache_prefix,platform:p.platform};
  for(const [name,want]of Object.entries(expected))eq(v[name],frozen(want),label+" launch invariant "+name);
  for(const [name,w]of flags)eq(w,frozen(p.flag_requirements[name]),label+" typed flag "+name);
  boundedString(text,label+" actual full flag text");const flagRender="sys.flags("+flags.map(([n,t])=>n+"="+(typeof t[1]==="boolean"?(t[1]?"True":"False"):t[1].toString())).join(", ")+")";eq(text,flagRender,"flag text consistent with typed named flags");
  arr(impl,label+" implementation");ok(BigInt(impl.length)<=binding.bounds.sequence_items,"implementation member bound");const implNames=impl.map(z=>z[0]);unique(implNames,"implementation names");eq(implNames,implNames.slice().sort(),"sorted implementation names");for(const z of impl){arr(z,"implementation pair");ok(z.length===2,"implementation two fields");boundedString(z[0],"implementation name");tag(z[1],"implementation value");}
  const im=Object.fromEntries(impl);for(const [n,w]of[["name",p.implementation],["cache_tag",p.cache_tag],["version",p.release]])eq(im[n],frozen(w),"implementation policy "+n);
  arr(streams,label+" streams");eq(streams.map(s=>s[0]),["stdout","stderr"],"two stream identities");for(const s of streams){ok(s.length===3,"stream tuple");tag(s[1],"stream encoding");tag(s[2],"stream errors");ok(p.encodings_allowed.some(e=>typedEqual(s[1],frozen(e))),"stream encoding policy");eq(s[2],frozen(p[s[0]+"_errors"]),"stream errors policy");}
  boundedString(encoding,"filesystem encoding");boundedString(errors,"filesystem errors");ok(p.encodings_allowed.includes(encoding)&&errors===p.filesystem_errors,"filesystem encoding policy");
  ok(v.builtin_module_names[0]==="sequence"&&v.builtin_module_names[1].every(t=>t[0]==="value"&&typeof t[1]==="string"),"actual builtin name sequence");const builtin=v.builtin_module_names[1].map(t=>t[1]);unique(builtin,"actual builtin names");return new Set(builtin);
 }
 const builtinNames=launch(x.early_launch,"early");for(const n of["second_launch","helper_launch","closing_launch"]){launch(x[n],n);eq(x[n],x.early_launch,"whole immutable launch "+n);}
 function moduleSet(rows,phase,label){
  arr(rows,label);ok(BigInt(rows.length)<=binding.bounds.modules,label+" module bound");const names=rows.map(r=>r[0]);unique(names,label+" registry names");eq(names,names.slice().sort(),label+" sorted registry");ok(names.every(n=>binding.module_names[phase].includes(n)),label+" finite name membership");ok(binding.required_module_names[phase].every(n=>names.includes(n)),label+" required core present");
  const roles=[],mechanisms={};
  for(const row of rows){
   moduleRows++;arr(row,"actual module row");ok(row.length===8,"eight complete module fields");const [name,present,builtin,spec,loader,filename,cached,search]=row,p=binding.modules[name];boundedString(name,"actual module name");ok(present===true&&typeof builtin==="boolean","registry presence and builtin boolean");ok(builtin===(p.mechanism==="builtin")&&builtin===builtinNames.has(name),"policy and independent observed builtin-name membership");
   eq(loader,binding.loader_ids[p.mechanism],"exact class/instance module loader");tag(filename,"module file tag");tag(cached,"module cache tag");tag(search,"module package tag");mechanisms[p.mechanism]=(mechanisms[p.mechanism]||0)+1;
   if(p.mechanism==="direct_script"){ok(name==="__main__","direct script name");eq(spec,["null"],"direct script null spec");eq(filename,frozen(binding.observer),"actual observer file");eq(cached,["null"],"direct script cached null");ok(nullOrMissing(search),"direct script package absent");}
   else{
    arr(spec,"module spec");ok(spec.length===5&&spec[0]==="spec","five spec fields");tag(spec[1],"spec origin");eq(spec[2],binding.loader_ids[p.mechanism],"exact spec loader");tag(spec[3],"spec location flag");tag(spec[4],"spec search locations");
    if(["builtin","frozen"].includes(p.mechanism)){eq(spec[1],frozen(p.mechanism==="builtin"?"built-in":"frozen"),"nonfile origin");eq(spec[3],frozen(false),"nonfile no location bool");eq(spec[4],["null"],"nonfile no search");ok(nullOrMissing(search)&&nullOrMissing(cached),"nonfile cache/package absent");ok(nullOrMissing(filename)||(p.mechanism==="frozen"&&typedEqual(filename,frozen(p.nominal_file))),"nonfile filename policy");}
    else{
     ok(["source_file","extension_file"].includes(p.mechanism),"finite file mechanism");eq(spec[1],frozen(p.origin),"file origin");eq(filename,frozen(p.file),"module exact file");eq(spec[3],frozen(true),"file has location bool");
     if(p.mechanism==="source_file")eq(cached,frozen(p.cache),"exact cache eligibility label");else ok(nullOrMissing(cached),"extension cache absent");
     if(p.package_path===null){eq(spec[4],["null"],"nonpackage spec null search");ok(nullOrMissing(search),"nonpackage module search absent");}else{eq(spec[4],frozen([p.package_path]),"one exact package spec directory");eq(search,frozen([p.package_path]),"one exact module package directory");}
    }
   }
   for(const role of p.file_roles){const e=entries.get(role.path),f=keyed.get(role.path);ok(e&&e.roles.includes(role.role),"joined module permission");ok(phase!=="early"||e.earliest_phase==="early","no early backfill");ok(f&&(f.complete===true||(!role.content_required&&e.optional&&f.absent===true)),"actual source/cache requirement backed by prior whole key/eligible absence");roles.push({phase,module:name,mechanism:p.mechanism,path:role.path,role:role.role});}
  }
  const rowsByName=new Map(rows.map(r=>[r[0],r]));if(rowsByName.has("os.path")&&rowsByName.has("posixpath"))eq(rowsByName.get("os.path").slice(1),rowsByName.get("posixpath").slice(1),"alias remaining seven fields");return {roles,mechanisms,names};
 }
 arr(x.module_snapshots,"snapshots");const phases=["early","second_prehelper","helper","closing","postclosing_check"],topRows=[x.early_modules,x.second_modules,x.helper_modules,x.closing_modules,x.closing_modules];ok(x.module_snapshots.length===5,"five complete sampling points");const moduleStats=[];
 for(let i=0;i<5;i++){const s=x.module_snapshots[i];keys(s,["complete","phase","rows"],"snapshot");ok(s.complete===true&&s.phase===phases[i],"complete phase order");eq(s.rows,topRows[i],"actual snapshot aliases");const phase=i<2?"early":i===2?"helper":"closing";const a=moduleSet(s.rows,phase,s.phase);moduleStats.push({phase:s.phase,rows:s.rows.length,mechanisms:a.mechanisms,roles:a.roles.length});if([0,2,3].includes(i))eq(a.roles,x[phase+"_roles"],"all ordered actual role rows "+phase);}
 eq(x.early_modules,x.second_modules,"both prehelper module copies unchanged");
 function delta(a,b){const left=new Map(a.map(r=>[r[0],r])),right=new Map(b.map(r=>[r[0],r]));return {added:setdiff([...right.keys()],[...left.keys()]),removed:setdiff([...left.keys()],[...right.keys()]),changed:[...left.keys()].filter(n=>right.has(n)&&!typedEqual(left.get(n),right.get(n))).sort()};}
 for(const [r,a,b]of[[x.helper_module_delta,x.early_modules,x.helper_modules],[x.closing_module_delta,x.helper_modules,x.closing_modules]]){keys(r,["added","changed","removed"],"module delta");eq(r,delta(a,b),"complete independently recomputed module delta");eq(r.removed,[],"no removed module");eq(r.changed,[],"no changed module");}

 function device(d){integer(d,"device integer");ok(d>=0n&&d<=0xffffffffffffffffn,"unsigned 64-bit Linux dev_t");return [((d>>8n)&0xfffn)|((d>>32n)&0xfffff000n),(d&0xffn)|((d>>12n)&0xffffff00n)];}
 const phaseMaps=["early_pre_helpers","helper","closing"],mapDataPhases=["early","helper","closing"],mapStats=[];arr(x.maps,"maps");ok(x.maps.length===3,"all three raw maps");
 for(let i=0;i<3;i++){
  const m=x.maps[i],phase=mapDataPhases[i];keys(m,["byte_count","eof","parsed","phase","raw_hex"],"raw map record");ok(m.phase===phaseMaps[i]&&m.eof===true,"ordered full map phase");integer(m.byte_count,"map byte count");ok(m.byte_count>0n&&m.byte_count<=binding.bounds.maps_bytes,"map byte bound");
  ok(typeof m.raw_hex==="string"&&/^(?:[0-9a-f]{2})+$/.test(m.raw_hex),"lossless lowercase raw map hex");const raw=Buffer.from(m.raw_hex,"hex");ok(BigInt(raw.length)===m.byte_count&&raw.every(v=>v<128)&&raw[raw.length-1]===10,"complete ASCII raw map bytes and final LF");
  const parsed=[];for(const line of raw.toString("ascii").slice(0,-1).split("\n")){
   const re=/^([0-9a-fA-F]+)-([0-9a-fA-F]+)[ \t]+([r-][w-][x-][ps])[ \t]+([0-9a-fA-F]+)[ \t]+([0-9a-fA-F]+):([0-9a-fA-F]+)[ \t]+([0-9]+)(?:[ \t]+(.*))?$/;
   const z=re.exec(line);ok(!!z,"independent complete map line grammar");const p=z[8]||"";const row={start:BigInt("0x"+z[1]),end:BigInt("0x"+z[2]),perms:z[3],offset:BigInt("0x"+z[4]),device:[BigInt("0x"+z[5]),BigInt("0x"+z[6])],inode:BigInt(z[7]),path:p,phase};mapRows++;
   ok(row.start<row.end&&!p.endsWith(" (deleted)"),"map address order/no deletion");
   if(p.startsWith("/")){mapFileRows++;path(p,"mapped path data");const e=entries.get(p),f=keyed.get(p);ok(e&&e.roles.includes("mapped_file"),"finite mapped-file role");ok(phase!=="early"||e.earliest_phase==="early","no early map backfill");ok(f?.complete===true&&row.inode>0n,"complete mapped key");eq(row.device,device(f.fd_before.st_dev),"exact device major/minor from recorded key only");eq(row.inode,f.fd_before.st_ino,"exact mapped inode identity");}
   else{mapSpecialRows++;ok(binding.special_maps.includes(p),"exact special/anonymous spelling");eq(row.device,[0n,0n],"special zero device");eq(row.inode,0n,"special zero inode");}
   parsed.push(row);
  }
  eq(parsed,m.parsed,"every independent parsed map field against original output");const paths=[...new Set(parsed.filter(r=>r.path.startsWith("/")).map(r=>r.path))].sort();mapStats.push({phase:m.phase,bytes:raw.length,rows:parsed.length,paths});
 }
 eq(x.helper_observed_map_additions,setdiff(mapStats[1].paths,mapStats[0].paths),"actual helper map additions");eq(x.closing_observed_map_additions,setdiff(mapStats[2].paths,mapStats[1].paths),"actual closing map additions");
 for(const [label,p]of[["begin",x.process_begin],["after_keys",x.process_after_keys],["closing",x.process_closing]]){keys(p,["cwd","exe_stat","proc_cwd","proc_exe"],"process point "+label);eq(p.cwd,binding.cwd,"literal cwd");eq(p.proc_cwd,binding.cwd,"proc cwd string");eq(p.proc_exe,binding.interpreter.final,"proc exe string");stat(p.exe_stat,"process exe "+label);eq(p.exe_stat,keyed.get(binding.interpreter.lexical).fd_before,"whole interpreter identity at process point");eq(p,x.process_begin,"all process point fields unchanged");}
 keys(x.environment,["closing_matches","expected","matches","scope"],"environment");eq(x.environment,{closing_matches:true,expected:{LANG:"C",LC_ALL:"C"},matches:true,scope:"os.environ_cached_mapping"},"cached environment predicate only");
 const source=keyed.get(binding.observer);ok(source.complete===true&&source.byte_count===98365n,"complete exact observer self-read");eq(source.sha256_of_read_bytes,sourceExternal.sha256,"source digest vs separate accepted external bytes");
 const nameMap={st_dev:"dev",st_ino:"ino",st_mode:"mode",st_nlink:"nlink",st_uid:"uid",st_gid:"gid",st_rdev:"rdev",st_size:"size",st_mtime_ns:"mtimeNs",st_ctime_ns:"ctimeNs"};let sourceComparisons=0;
 for(const point of[source.begin.final_lstat,source.fd_before,source.fd_after,source.after_read.final_lstat,source.closing.final_lstat])for(const [k,n]of Object.entries(nameMap)){eq(point[k].toString(),sourceExternal.metadata[n],"lossless source/external metadata "+k);sourceComparisons++;}
 return {scope:"ONE_RECORDED_P213_PROBE_RUNTIME_DATA_ONLY_NO_FUTURE_PROCESS_KEY",checks,taggedFacts,moduleRows,statFields,mapRows,mapFileRows,mapSpecialRows,moduleStats,mapStats,completeFiles:complete,absentFiles:absent,totalFileReadBytes:total.toString(),sourceComparisons,helperAddedModules:x.helper_module_delta.added,unobservedPermittedHelperModules:setdiff(binding.module_names.helper,x.helper_modules.map(r=>r[0])),runtimePayloadCanonicalBytes:Buffer.byteLength(canonicalIntegerJSON(x)+"\n"),failureFields:0};
};
