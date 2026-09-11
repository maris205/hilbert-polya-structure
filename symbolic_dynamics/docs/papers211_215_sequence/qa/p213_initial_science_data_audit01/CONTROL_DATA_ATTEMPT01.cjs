"use strict";
// Independent predicates on received DATA only. No file or process APIs in this module.
const {typedEqual,canonicalIntegerJSON}=require("../p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs");
module.exports=function receiveControl(x,binding,external){
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
 keys(binding,["id","interpreter","observer","cwd","launch_policy","flag_names","module_names","required_module_names","modules","loader_ids","special_maps","files","bounds","science"],"binding");
 const boundExpected={modules:62n,maps_bytes:65536n,files:70n,file_bytes:8388608n,total_bytes:67108864n,scalar_chars:1024n,sequence_items:128n,link_hops:1n,stdout_bytes:16777216n};
 eq(binding.bounds,boundExpected,"exact accepted numeric bounds");path(binding.observer,"observer role");path(binding.cwd,"cwd role");
 arr(binding.files,"file permissions");ok(binding.files.length===70,"70 permissions");
 const entries=new Map();for(const e of binding.files){
  keys(e,["lexical","final","links","optional","absence_required","earliest_phase","roles","observed_presence","observed_key"],"permission");path(e.lexical,"permission path");eq(e.final,e.lexical,"same lexical/final permission");eq(e.links,[],"no leaf aliases permitted");
  ok(!entries.has(e.lexical),"unique permission path");entries.set(e.lexical,e);ok(typeof e.optional==="boolean"&&typeof e.absence_required==="boolean","actual boolean permission fields");
  ok(["early","helper"].includes(e.earliest_phase),"permission phase");arr(e.roles,"permission roles");unique(e.roles,"permission roles");ok(e.roles.length>0&&e.roles.every(r=>["direct_script_source","mapped_file","source_or_matching_source","eligible_nonoptimized_cache","extension_origin","startup_zip_must_be_absent","scientific_source_exact_bytes"].includes(r)),"finite file role vocabulary");
  ok(e.absence_required===e.roles.includes("startup_zip_must_be_absent")&&(!e.absence_required||e.optional),"zip absence relation");ok(e.observed_presence===null&&e.observed_key===null,"permission placeholders not claimed observations");
 }
 eq(binding.interpreter,entries.get(binding.interpreter.lexical),"whole duplicated interpreter permission");ok(entries.get(binding.observer)?.optional===false&&binding.interpreter.optional===false,"mandatory source/interpreter");
 eq(binding.flag_names,binding.launch_policy.flag_names,"flag order duplicate");eq(Object.keys(binding.launch_policy.flag_requirements).sort(),binding.flag_names.slice().sort(),"complete flag policy");ok(binding.flag_names.length===17,"17 exact flags");
 for(const phase of["early","helper","closing"]){arr(binding.module_names[phase],"phase permissions");unique(binding.module_names[phase],"phase module names");ok(binding.module_names[phase].every(n=>Object.hasOwn(binding.modules,n)),"module permissions defined");ok(binding.required_module_names[phase].every(n=>binding.module_names[phase].includes(n)),"required module subset");}
 ok(Object.keys(binding.modules).length===62&&binding.module_names.early.length===23,"fixed module frontier");
 for(const [name,p]of Object.entries(binding.modules)){boundedString(name,"module policy name");ok(p.observed_row===null,"no predicted row");ok(Object.hasOwn(binding.loader_ids,p.mechanism),"finite mechanism");for(const r of p.file_roles){keys(r,["path","role","content_required"],"module permission role");path(r.path,"module role path");ok(entries.has(r.path)&&entries.get(r.path).roles.includes(r.role)&&typeof r.content_required==="boolean","role joins finite file entry");}}


 keys(binding.science,["source","source_bytes","source_sha256","stdout_bytes","control_fd","execution","compile_flags","dont_inherit","optimize"],"science binding");
 eq(binding.science,{source:"/root/autodl-tmp/symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/verify.py",source_bytes:17539n,source_sha256:"a01d3d93619cea90adfc2e5be1bdfd8089d7eae6fcaae153b4fb4af398fc1812",stdout_bytes:67108864n,control_fd:3n,execution:"compile_exact_bytes_isolated_dictionary",compile_flags:0n,dont_inherit:true,optimize:0n},"entire unchanged science binding");
 eq(binding.id,"P213_INITIAL_SCIENCE_WRAPPER_PROPOSED01","literal binding id");
 keys(x,["after_keys","before_keys","binding_id","canonical_adopted","closing","early_launch","early_modules","early_roles","environment_matches","files","final_environment_matches","helper_launch","helper_module_delta","helper_modules","helper_observed_map_additions","helper_roles","maps","module_snapshots","outputs_begin","outputs_final","post_science","pre_science","process_begin","runtime_accepted","schema","science","science_accepted","second_launch","second_modules","status","strict_pair_completed","total_file_read_bytes"],"complete initial science control");
 eq(x.binding_id,binding.id,"binding id");eq(x.schema,"P213_EXACT_SOURCE_SCIENCE_WRAPPER_PROPOSAL_V1","schema");eq(x.status,"SCIENCE_COMPLETE_PENDING_INDEPENDENT_RECEPTION","producer progress not verdict");
 for(const n of["runtime_accepted","science_accepted","canonical_adopted","strict_pair_completed"])eq(x[n],false,"producer explicitly pending "+n);
 for(const n of["environment_matches","final_environment_matches"])eq(x[n],true,"cached environment predicate "+n);
 const statNames=["st_dev","st_ino","st_mode","st_nlink","st_uid","st_gid","st_rdev","st_size","st_mtime_ns","st_ctime_ns"];
 function stat(s,label){keys(s,statNames,label);for(const k of statNames){integer(s[k],label+" "+k);statFields++;}ok((s.st_mode&0o170000n)===0o100000n,label+" regular mode");ok(s.st_size>=0n&&s.st_nlink>=1n,label+" size/link");return s;}
 function point(p,e,label,absent){keys(p,absent?["absence","lexical","links"]:["absence","final_lstat","lexical","links"],label);eq(p.lexical,e.lexical,label+" lexical");eq(p.links,[],label+" no leaf alias");
  if(absent)eq(p.absence,{errno:2n,operation:"lstat",path:e.lexical},label+" exact ENOENT");else{eq(p.absence,null,label+" no absence");stat(p.final_lstat,label+" lstat");}}
 let complete=0,absent=0,total=0n;
 function file(f,e,label,closing,sourceLoad=false){
  const missing=f.absent===true;const names=missing?["absent","begin","byte_count","complete","eof","lexical","roles","sha256_of_read_bytes"]:["after_read","begin","byte_count","complete","eof","fd_after","fd_before","lexical","roles","sha256_of_read_bytes"];
  if(closing)names.push("closing");if(sourceLoad)names.splice(names.indexOf("roles"),1);keys(f,names,label);
  eq(f.lexical,e.lexical,label+" exact path");if(!sourceLoad)eq(f.roles,e.roles,label+" exact roles");integer(f.byte_count,label+" read count");
  ok(typeof f.sha256_of_read_bytes==="string"&&/^[0-9a-f]{64}$/.test(f.sha256_of_read_bytes),label+" digest shape");
  point(f.begin,e,label+" begin",missing);if(closing){point(f.closing,e,label+" closing",missing);eq(f.closing,f.begin,label+" closing equal begin");}
  if(missing){absent++;ok(e.optional,label+" permitted absence");eq(f.byte_count,0n,label+" zero unobserved bytes");eq(f.eof,false,label+" no absence EOF");eq(f.complete,false,label+" no absent content key");eq(f.sha256_of_read_bytes,"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",label+" zero-read digest");}
  else{complete++;ok(!e.absence_required,label+" mandatory absence not present");eq(f.eof,true,label+" actual EOF");eq(f.complete,true,label+" complete");point(f.after_read,e,label+" after-read",false);stat(f.fd_before,label+" fd-before");stat(f.fd_after,label+" fd-after");eq(f.begin.final_lstat,f.fd_before,label+" path/fd identity");eq(f.fd_before,f.fd_after,label+" same descriptor");eq(f.begin,f.after_read,label+" endpoint identity");eq(f.byte_count,f.fd_before.st_size,label+" complete file size");ok(f.byte_count<=binding.bounds.file_bytes,label+" bounded file");total+=f.byte_count;}
 }
 const paths=binding.files.map(e=>e.lexical);
 keys(x.before_keys,paths,"whole before dictionary");keys(x.after_keys,paths,"whole after dictionary");arr(x.files,"ordered records");ok(x.files.length===140,"exactly two finite passes");
 const keyed=new Map();
 for(let i=0;i<70;i++){const e=binding.files[i],before=x.before_keys[e.lexical],after=x.after_keys[e.lexical];file(before,e,"before "+i,false);file(after,e,"after "+i,true);eq(before,x.files[i],"first-pass ordered record alias");eq(after,x.files[i+70],"second-pass ordered record alias");const sans=Object.fromEntries(Object.entries(after).filter(([k])=>k!=="closing"));eq(before,sans,"all original pre/post file-key fields unchanged");keyed.set(e.lexical,before);}
 eq(paths.filter(p=>x.before_keys[p].absent===true),["/usr/lib/python310.zip"],"one exact required absence per pass");
 keys(x.science,["attempted","compile_completed","execution","expected_bytes","expected_sha256","globals_policy","returned_normally","source","source_load","stdout_flushed"],"whole scientific progress");
 for(const n of["attempted","compile_completed","returned_normally","stdout_flushed"])eq(x.science[n],true,"producer completed "+n);
 eq(x.science.source,binding.science.source,"scientific exact source");eq(x.science.expected_bytes,binding.science.source_bytes,"source length");eq(x.science.expected_sha256,binding.science.source_sha256,"science digest");eq(x.science.execution,binding.science.execution,"compile mode");
 eq(x.science.globals_policy,{__name__:"__main__",__file__:binding.science.source,__package__:null,__spec__:null,__cached__:null,__loader__:null,__builtins__:"actual sys.modules['builtins'] module; ordinary shared builtin trust",globals_equal_locals:true,sys.argv_and_sys.modules_are_not_modified:true},"entire isolated dictionary/shared-builtins policy");
 file(x.science.source_load,entries.get(binding.science.source),"science saved-byte single descriptor",false,true);
 const source=keyed.get(binding.science.source);for(const n of["begin","fd_before","fd_after","after_read","byte_count","eof","complete","sha256_of_read_bytes"])eq(x.science.source_load[n],source[n],"whole loaded-source key equality "+n);
 eq(source.sha256_of_read_bytes,binding.science.source_sha256,"loaded exact byte pin");eq(source.byte_count,binding.science.source_bytes,"loaded byte count");eq(x.total_file_read_bytes,total,"two passes plus independent source-load accounting");ok(total<=binding.bounds.total_bytes,"total source content bound");
 const boundaryNames=["environment_matches","launch","maps","modules","outputs","process","roles"];
 for(const name of["pre_science","post_science","closing"]){keys(x[name],name==="pre_science"?[...boundaryNames,"helper_delta"]:boundaryNames,"whole "+name+" boundary");eq(x[name].environment_matches,true,"cached environment "+name);}
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

 const builtinNames=launch(x.early_launch,"early");
 for(const [label,value]of [["second",x.second_launch],["helper",x.helper_launch],["pre_science",x.pre_science.launch],["post_science",x.post_science.launch],["closing",x.closing.launch]]){launch(value,label);eq(value,x.early_launch,"whole launch unchanged "+label);}
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

 arr(x.module_snapshots,"all module snapshots");const phases=["early","second_prehelper","helper","pre_science","post_science","closing","postclosing_check"],topRows=[x.early_modules,x.second_modules,x.helper_modules,x.pre_science.modules,x.post_science.modules,x.closing.modules,x.closing.modules];ok(x.module_snapshots.length===7,"seven actual module sampling points");const moduleStats=[];
 for(let i=0;i<7;i++){const s=x.module_snapshots[i];keys(s,["complete","phase","rows"],"complete snapshot");eq(s.phase,phases[i],"actual label order");eq(s.complete,true,"completed snapshot");eq(s.rows,topRows[i],"full top/snapshot duplicate");const category=i<2?"early":i===2?"helper":"closing";const a=moduleSet(s.rows,category,s.phase);moduleStats.push({phase:s.phase,rows:s.rows.length,mechanisms:a.mechanisms,roles:a.roles.length});if(i===0)eq(a.roles,x.early_roles,"all early role rows");if(i===2)eq(a.roles,x.helper_roles,"all helper role rows");if(i>=3&&i<=5)eq(a.roles,x[phases[i]].roles,"all boundary role rows");}
 eq(x.early_modules,x.second_modules,"no prehelper registry change");eq(x.pre_science.modules,x.post_science.modules,"whole science registry unchanged");eq(x.post_science.modules,x.closing.modules,"whole closing registry unchanged");
 function delta(a,b){const left=new Map(a.map(r=>[r[0],r])),right=new Map(b.map(r=>[r[0],r]));return {added:setdiff([...right.keys()],[...left.keys()]),removed:setdiff([...left.keys()],[...right.keys()]),changed:[...left.keys()].filter(n=>right.has(n)&&!typedEqual(left.get(n),right.get(n))).sort()};}
 for(const [r,a,b]of[[x.helper_module_delta,x.early_modules,x.helper_modules],[x.pre_science.helper_delta,x.helper_modules,x.pre_science.modules]]){keys(r,["added","changed","removed"],"whole module delta");eq(r,delta(a,b),"all recomputed module delta fields");eq(r.removed,[],"no removed module");eq(r.changed,[],"no changed module");}
 function device(d){integer(d,"device integer");ok(d>=0n&&d<=0xffffffffffffffffn,"unsigned 64-bit Linux dev_t");return [((d>>8n)&0xfffn)|((d>>32n)&0xfffff000n),(d&0xffn)|((d>>12n)&0xffffff00n)];}
 const phaseMaps=["early_pre_helpers","helper","pre_science","post_science","closing"],mapDataPhases=["early","helper","pre_science","post_science","closing"],mapStats=[];arr(x.maps,"maps");ok(x.maps.length===5,"all five raw maps");
 for(let i=0;i<5;i++){
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

 eq(x.helper_observed_map_additions,setdiff(mapStats[1].paths,mapStats[0].paths),"all observed helper map additions");
 for(let i=2;i<5;i++){eq(x.maps[i],x[["pre_science","post_science","closing"][i-2]].maps,"full duplicate boundary maps");if(i>2)eq(mapStats[i].paths,mapStats[i-1].paths,"unchanged mapped-file path set across science/closing");}
 for(const [label,r]of[["begin",x.process_begin],["pre_science",x.pre_science.process],["post_science",x.post_science.process],["closing",x.closing.process]]){keys(r,["cwd","exe_stat","proc_cwd","proc_exe"],"process "+label);eq(r.cwd,binding.cwd,"literal cwd");eq(r.proc_cwd,binding.cwd,"proc cwd data");eq(r.proc_exe,binding.interpreter.final,"proc exe data");stat(r.exe_stat,label+" exe");eq(r.exe_stat,keyed.get(binding.interpreter.lexical).fd_before,"full interpreter identity");eq(r,x.process_begin,"all process point fields unchanged");}
 const nameMap={st_dev:"dev",st_ino:"ino",st_mode:"mode",st_nlink:"nlink",st_uid:"uid",st_gid:"gid",st_rdev:"rdev",st_size:"size",st_mtime_ns:"mtimeNs",st_ctime_ns:"ctimeNs"};
 let externalComparisons=0;
 for(const sourcePath of[binding.observer,binding.science.source]){
  const f=keyed.get(sourcePath),ext=external.sources[sourcePath];ok(!!ext,"separate fixed documentary source key");eq(f.sha256_of_read_bytes,ext.sha256,"whole external source digest");eq(f.byte_count,BigInt(ext.byte_count),"whole external source length");
  for(const s of[f.begin.final_lstat,f.fd_before,f.fd_after,f.after_read.final_lstat,x.after_keys[sourcePath].closing.final_lstat])for(const [a,b]of Object.entries(nameMap)){eq(s[a].toString(),ext.fd_before[b],"exact external source metadata "+a);externalComparisons++;}
 }
 const outputs=[["begin",x.outputs_begin],["pre_science",x.pre_science.outputs],["post_science",x.post_science.outputs],["closing",x.closing.outputs],["final_precontrol_write",x.outputs_final]];
 for(const [label,o]of outputs){keys(o,["1","2","3"],"output descriptors "+label);const ids=[];for(const fd of["1","2","3"]){stat(o[fd],label+" output "+fd);eq(o[fd].st_nlink,1n,"single linked capture");ids.push(o[fd].st_dev+":"+o[fd].st_ino);for(const f of keyed.values())if(f.complete)ok(o[fd].st_dev!==f.fd_before.st_dev||o[fd].st_ino!==f.fd_before.st_ino,"all output/input inode separation");for(const k of statNames.slice(0,7))eq(o[fd][k],x.outputs_begin[fd][k],"permanent output descriptor identity");}
  unique(ids,"three capture descriptors");eq(o["2"],x.outputs_begin["2"],"empty stderr unchanged");eq(o["3"],x.outputs_begin["3"],"control remains empty before its final write");if(label==="begin"||label==="pre_science")for(const fd of["1","2","3"])eq(o[fd].st_size,0n,"all initial captures empty");else{eq(o["1"].st_size,BigInt(external.raw.stdout.byte_count),"exact scientific output size");eq(o["1"],x.outputs_final["1"],"completed stdout no later writes");}}
 eq(x.pre_science.outputs,x.outputs_begin,"whole pre-science unchanged outputs");
 for(const [fd,name]of[["1","stdout"],["2","stderr"],["3","control"]]){const ext=external.raw[name];eq(ext.fd_before.mode,"33152","current original raw0600");eq(ext.fd_before.nlink,"1","current original raw single link");const s=x.outputs_final[fd];for(const [a,b]of Object.entries(nameMap)){if(fd==="3"&&!statNames.slice(0,7).includes(a))continue;eq(s[a].toString(),ext.fd_before[b],"original captured output metadata "+fd+" "+a);externalComparisons++;}}
 return {status:"PASS_CAPTURED_INITIAL_CONTROL_DATA_ONLY",checks,taggedFacts,moduleRows,statFields,mapRows,mapFileRows,mapSpecialRows,moduleStats,mapStats,completeFileRecords:complete,absentFileRecords:absent,totalFileReadBytes:total.toString(),externalComparisons,helperAddedModules:x.helper_module_delta.added,unobservedPermittedHelperModules:setdiff(binding.module_names.helper,x.helper_modules.map(r=>r[0])),rawControlCanonicalBytes:Buffer.byteLength(canonicalIntegerJSON(x)+"\n"),producerAcceptanceFlags:false,hostContentHashesRecomputed:false,hostPathQueries:false,sourceExecution:false};
};

