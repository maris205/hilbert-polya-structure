"use strict";
// Document-only author check. Never execute/parse/import Python or Bash, and never
// inspect destinations of runtime permission/future output strings.
const fs=require("node:fs"), crypto=require("node:crypto");
const D="docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01";
const ROOT="/root/autodl-tmp/symbolic_dynamics/";
const S="docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01";
const F=ROOT+"docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01";
const INPUTS=[
  {
    "role": "receipt",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta_root01/RECEPTION.md"
  },
  {
    "role": "contract",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/CONTRACT.md"
  },
  {
    "role": "format",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/BINDING_FORMAT.md"
  },
  {
    "role": "collection",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/COLLECTION_DELTA.md"
  },
  {
    "role": "observer",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/observe.py"
  },
  {
    "role": "capture",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/capture.sh"
  },
  {
    "role": "capture_request",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/CAPTURE_REQUEST.disabled.json"
  },
  {
    "role": "binding",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/BINDING.disabled.json"
  },
  {
    "role": "source_seal",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta01/SHA256SUMS"
  },
  {
    "role": "root_seal",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta_root01/SHA256SUMS"
  },
  {
    "role": "audit_report",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta_audit01/REPORT.md"
  },
  {
    "role": "audit_findings",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta_audit01/FINDINGS.json"
  },
  {
    "role": "audit_seal",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_source_delta_audit01/SHA256SUMS"
  },
  {
    "role": "proposal",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_binding_preparation01/PROPOSAL.md"
  },
  {
    "role": "policy",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_binding_preparation01/POLICY.proposed.json"
  },
  {
    "role": "proposal_seal",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_binding_preparation01/SHA256SUMS"
  }
];
const OWN=["KEY_INPUT_DOCUMENTS.cjs","KEY_PREPARED_DOCUMENTS.cjs","ORIENTATION_NATIVE.json","SOURCE_READS_NATIVE.json","INPUT_KEYS_NATIVE.json","INPUTS.sha256","BINDING.prepared.json","BINDING.runtime_literal.json","BINDING.literal.txt","observe.py","capture.sh","observe.proposed.py.txt","capture.proposed.sh.txt","CAPTURE_REQUEST.disabled.json","PROPOSED_REQUEST.json","TRANSFORMATION.json","CONSUMPTION_MAP.json","PREPARED_KEYS_NATIVE.json","PROSPECTIVE_BYTES.json","SOURCE_DIFF_NATIVE.json","PREPARATION.md","READ_SCOPE.md","CHECK_DOCUMENTS.cjs"];
const allowed=new Set([...INPUTS.map(x=>x.path),...OWN.map(x=>D+"/"+x)]);
const fields=["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
let checks=0, rawPairs=0, rawBytes=0;
function ok(x,msg){checks++;if(!x)throw Error(msg);}
function same(a,b,msg){
 ok(typeof a===typeof b,msg+": type");
 if(a===null||b===null||typeof a!=="object"){ok(Object.is(a,b),msg+": scalar");return;}
 ok(Array.isArray(a)===Array.isArray(b),msg+": array/object");
 const ak=Object.keys(a),bk=Object.keys(b);ok(JSON.stringify(ak)===JSON.stringify(bk),msg+": keys/order");
 for(const k of ak)same(a[k],b[k],msg+"."+k);
}
const metadata=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const records=new Map(), buffers=new Map();
function read(path){
 ok(allowed.has(path),"outside exact documentary allowlist: "+path);
 if(buffers.has(path))return buffers.get(path);
 const a=fs.lstatSync(path,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),"regular no-leaf-link document");
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  const f=fs.fstatSync(fd,{bigint:true}),buf=fs.readFileSync(fd),g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(path,{bigint:true});
  for(const p of [f,g,z])same(metadata(a),metadata(p),"stable metadata "+path);
  ok(BigInt(buf.length)===a.size,"whole EOF byte count");
  const rec={path,sha256:crypto.createHash("sha256").update(buf).digest("hex"),bytes:buf.length,metadata:metadata(a),fd_end:metadata(g),path_end:metadata(z),leaf_links:[],full_eof:true};
  records.set(path,rec);buffers.set(path,buf);return buf;
 }finally{fs.closeSync(fd);}
}
const own=n=>read(D+"/"+n), txt=n=>own(n).toString("utf8"), json=n=>JSON.parse(txt(n));
function raw(a,b,msg){
 a=Buffer.isBuffer(a)?a:Buffer.from(a,"utf8");b=Buffer.isBuffer(b)?b:Buffer.from(b,"utf8");
 ok(a.equals(b),msg);rawPairs++;rawBytes+=a.length;
}
const previous=json("INPUT_KEYS_NATIVE.json");ok(previous.result.exit_code===0,"baseline input key exit");
const baseline=JSON.parse(previous.result.output).keys;ok(baseline.length===16,"16 inputs");
for(let i=0;i<INPUTS.length;i++){
 const spec=INPUTS[i],old=baseline[i];same(spec,{role:old.role,path:old.path},"baseline identity");
 read(spec.path);same(records.get(spec.path),Object.fromEntries(Object.entries(old).filter(([k])=>k!=="role")),"complete baseline key unchanged");
}
const get=role=>INPUTS.find(x=>x.role===role).path;
const oldText=role=>read(get(role)).toString("utf8");
const oldJson=role=>JSON.parse(oldText(role));
const rd=json("SOURCE_READS_NATIVE.json").reads;ok(rd.length===16,"16 retained complete source returns");
for(let i=0;i<rd.length;i++){
 same(rd[i].role,INPUTS[i].role,"read role");
 same(rd[i].path,INPUTS[i].path,"read path");ok(rd[i].result.exit_code===0,"source read success");
 raw(rd[i].result.output,read(INPUTS[i].path),"whole raw source read "+rd[i].role);
}
raw(txt("INPUTS.sha256"),baseline.map(x=>x.sha256+"  "+x.path).join("\n")+"\n","input manifest whole bytes");
for(const [role,pin] of [["receipt","ed33654cd077fd43b1d125ed9cc3ad4ec4223590262cd183da36468993d1c743"],["source_seal","98ed7e008e16eef37dfb37dcbb00060cef97479957ef25f4df939b6e3314ee34"],["proposal_seal","98f27ead29fa8862591d3b5a4cc6813eea1f09814f5d03a5edce0571ab278d96"],["audit_seal","303fe92c49db404336292532c9201b95925159f036d84508628d8dbd4b137ff4"],["root_seal","22024e87bc2a75f2e6fff35200575fb22d5725669046325caa7306255547a070"]])ok(records.get(get(role)).sha256===pin,"accepted lineage "+role);
for(const role of ["source_seal","proposal_seal","audit_seal","root_seal"]){
 const p=get(role),prefix=p.slice(0,p.lastIndexOf("/")+1);
 const rows=oldText(role).trimEnd().split("\n").map(line=>{const m=/^([0-9a-f]{64})  ([^/]+)$/.exec(line);ok(!!m,"seal row");return[m[2],m[1]];});
 const names=rows.map(x=>x[0]);ok(new Set(names).size===names.length,"unique old seal");
 for(const x of INPUTS.filter(x=>x.path.startsWith(prefix)&&x.path!==p))ok(new Map(rows).get(x.path.slice(prefix.length))===records.get(x.path).sha256,"selected old sealed member");
}
const original=oldJson("binding"), b=json("BINDING.prepared.json"), literal=json("BINDING.runtime_literal.json");
let relocated=0;
function move(x){
 if(typeof x==="string"&&x===original.observer){relocated++;return F+"/observe.py";}
 if(Array.isArray(x))return x.map(move);
 if(x!==null&&typeof x==="object")return Object.fromEntries(Object.entries(x).map(([k,v])=>[k,move(v)]));
 return x;
}
const expected=move(original);ok(relocated===7,"exactly seven whole-string observer relocations");
expected.schema="P213_FINITE_PERMISSION_BINDING_PREPARED_DISABLED_V1";
expected.id="P213_MINIMAL_FINITE_PERMISSION_OBSERVER_ENABLED01";
expected.modules.__main__.provenance="New prospective enabled01 path explicitly selected for this preparation; not a current presence or executed-source fact";
const pinroles=["observer","capture","binding","policy","receipt","source_seal","proposal_seal","audit_seal","root_seal"];
expected.source_pins={scope:"Accepted predecessor documentary pins, NOT expected self-hashes or runtime observations"};
for(const role of pinroles){const k=records.get(get(role));expected.source_pins[role]={path:ROOT+k.path,sha256:k.sha256,bytes:k.bytes};}
expected.note="Prepared documentary finite permissions only; observe.py never loads this JSON. The 13 consumed top-level fields are embedded literally behind an unconditional preparation gate. Enabled=false and operation_authorized=false are documentary controls, not runtime predicates. Existing observed/current fields remain null. Actual enabled/capture pins are not populated; exact proposed-byte hashes live externally in PROSPECTIVE_BYTES.json. No runtime grant.";
same(b,expected,"entire prepared binding allowed delta only");
const consumed=["id","interpreter","observer","cwd","launch_policy","flag_names","module_names","required_module_names","modules","loader_ids","special_maps","files","bounds"];
same(literal,Object.fromEntries(consumed.map(k=>[k,b[k]])),"entire 13-field runtime projection");
const cm=json("CONSUMPTION_MAP.json");
same(cm.consumed_top_level_fields,consumed,"consumption list");
same(cm.documentary_only_top_level_fields,Object.keys(b).filter(k=>!consumed.includes(k)),"documentary-only list");
function py(v,depth=0){
 if(v===null)return"None";
 if(v===true)return"True";if(v===false)return"False";
 if(typeof v==="number"){ok(Number.isSafeInteger(v),"exact safe integer literal");return String(v);}
 if(typeof v==="string"){ok(!/[^\x20-\x7e]/.test(v),"ASCII printable string literal");return JSON.stringify(v);}
 const pad="  ".repeat(depth),sub="  ".repeat(depth+1);
 if(Array.isArray(v))return v.length?"[\n"+v.map(x=>sub+py(x,depth+1)).join(",\n")+"\n"+pad+"]":"[]";
 ok(v!==null&&typeof v==="object","supported literal object");
 return Object.keys(v).length?"{\n"+Object.entries(v).map(([k,x])=>sub+py(k)+": "+py(x,depth+1)).join(",\n")+"\n"+pad+"}":"{}";
}
raw(txt("BINDING.literal.txt"),py(literal)+"\n","whole deterministic literal text");
ok(b.enabled===false&&b.operation_authorized===false&&b.capture_pins===null,"documentary disabled unobserved capture");
ok(b.files.length===69&&b.module_names.early.length===23&&b.module_names.helper.length===62&&b.module_names.closing.length===62,"finite exact phase cardinalities");
for(const phase of ["early","helper","closing"])ok(b.required_module_names[phase].every(n=>b.module_names[phase].includes(n)),"required phase subset "+phase);
same(b.interpreter,b.files.find(x=>x.lexical===b.interpreter.lexical),"entire duplicate interpreter record");
for(const x of b.files){
 ok(x.lexical===x.final&&x.links.length===0,"leaf no-link permission");
 ok(x.observed_presence===null&&x.observed_key===null,"not invented observed file facts");
}
for(const [name,row] of Object.entries(b.modules))ok(row.observed_row===null,"not invented actual module "+name);
same(b.bounds,original.bounds,"all bounds exact");
same(b.flag_names,original.flag_names,"all flags exact");
same(b.launch_policy.flag_requirements,original.launch_policy.flag_requirements,"all flag values/types exact");
ok(b.launch_policy.flag_requirements.dev_mode===false,"boolean dev_mode, not integer zero");
ok(b.files.filter(x=>x.lexical!==F+"/observe.py").length===68,"68 other files");
ok(b.files.find(x=>x.lexical==="/usr/lib/python310.zip").absence_required===true,"required zip ENOENT");
ok(b.actual_launch_record===null&&b.actual_module_rows===null&&b.launch_policy.full_actual_record===null,"actual records unresolved");
const ogate='raise SystemExit("P213_OBSERVER_DISABLED_ENABLED_PREPARATION")\n';
const ohead='"""P213 exact finite-permission observer; operational authority is external."""\n\n# The preparation copy has an unconditional gate before its complete literal.\n'+ogate+'# Literal permissions only; never loaded from a file or predicted actual rows.\nBINDING = ';
const otext=txt("observe.py"), oldObserver=oldText("observer"), start=oldObserver.indexOf("if BINDING is None:\n");
ok(start>0,"accepted tail anchor exists");
raw(otext,ohead+txt("BINDING.literal.txt")+oldObserver.slice(start),"whole prepared source expected bytes");
raw(otext.slice(otext.indexOf("if BINDING is None:\n")),oldObserver.slice(start),"entire accepted collector tail unchanged");
const used=[...new Set([...oldObserver.matchAll(/\bBINDING\["([^"]+)"\]/g)].map(m=>m[1]))].sort();
same(used,[...consumed].sort(),"all direct top-level consumed fields");
ok(otext.indexOf(ogate)<otext.indexOf("BINDING = ")&&otext.indexOf(ogate)<otext.indexOf("\nimport sys\n"),"physical observer pre-literal gate");
const cgate="printf '%s\\n' 'P213_CAPTURE_DISABLED_ENABLED_PREPARATION' >&2\nexit 78\n";
const chead="# P213 exact finite-permission capture; operational authority is external.\n# The preparation copy has an unconditional gate before cwd/allocation.\n"+cgate+"\n# Chosen paths are permissions, not observations of tool identity or presence.\n# Ordinary trusted bootstrap/filesystem limits are specified in PREPARATION.md.\n";
const ctext=txt("capture.sh"),oldCapture=oldText("capture"),cbegin=oldCapture.indexOf("P213_CAPTURE_ENV=");
ok(cbegin>0,"accepted capture body anchor");
const expectedCaptureBody=oldCapture.slice(cbegin).replace(original.observer,F+"/observe.py");
raw(ctext,chead+expectedCaptureBody,"entire prepared capture expected bytes");
ok(ctext.indexOf(cgate)<ctext.indexOf("P213_CAPTURE_ENV=")&&ctext.indexOf(cgate)<ctext.indexOf("cd --"),"physical capture pre-allocation gate");
const trans=json("TRANSFORMATION.json");
ok(trans.operation_authorized===false&&trans.materialized===false&&trans.operations.length===2,"prospective transform no authority");
for(const [n,gate,proposed,future] of [["observe.py",ogate,"observe.proposed.py.txt",F+"/observe.py"],["capture.sh",cgate,"capture.proposed.sh.txt",F+"/capture.sh"]]){
 const before=txt(n);ok(before.split(gate).length===2,"unique exact gate bytes "+n);
 raw(txt(proposed),before.replace(gate,""),"full exact postacceptance delta "+n);
 const op=trans.operations.find(x=>x.prepared===n);ok(!!op,"operation exists");
 same(op.remove_exact_bytes,gate,"gate bytes");
 ok(op.proposed_text_carrier===proposed&&op.future_path===future,"future exact selected path");
}
const request=json("CAPTURE_REQUEST.disabled.json"), proposed=json("PROPOSED_REQUEST.json");
const oldRequest=oldJson("capture_request");
const wantedRequest={...oldRequest,schema:"P213_SINGLE_CAPTURE_REQUEST_PREPARED_DISABLED_V1",request:{...oldRequest.request,shell:"/bin/bash"},capture_source:F+"/capture.sh",observer_source:F+"/observe.py",source_pins:expected.source_pins,note:"CURRENT REQUEST DISABLED: cmd=null; unconditional physical preparation gates remain. PROPOSED_REQUEST.json describes exact prospective postacceptance tool parameters only. It is not a grant and must not be submitted here."};
same(request,wantedRequest,"entire prepared disabled request only allowed edits");
ok(request.enabled===false&&request.operation_authorized===false&&request.request.cmd===null&&request.output_directory_observed_absence===null,"physical request remains null unauthorized");
same(proposed.proposed_request,{cmd:"exec /usr/bin/env -i LANG=C LC_ALL=C /bin/bash --noprofile --norc '"+F+"/capture.sh'",workdir:ROOT.slice(0,-1),shell:"/bin/bash",login:false,tty:false,yield_time_ms:1000,max_output_tokens:4000},"exact proposed tool invocation");
ok(proposed.enabled===false&&proposed.operation_authorized===false&&proposed.review_accepted===false&&proposed.actual_materialized===false&&proposed.actual_session_id===null&&proposed.actual_output_directory_absence===null,"proposed request no invented actuals/authority");
const coreNative=json("PREPARED_KEYS_NATIVE.json");ok(coreNative.result.exit_code===0,"core baseline success");
const core=JSON.parse(coreNative.result.output).keys;ok(core.length===11,"eleven documentary artifacts");
const manifest=json("PROSPECTIVE_BYTES.json");
same(manifest.current_documentary_artifacts,core.map(x=>({path:x.path.slice(D.length+1),bytes:x.bytes,sha256:x.sha256})),"external current document manifest");
for(const k of core){
 read(k.path);same(records.get(k.path),Object.fromEntries(Object.entries(k).filter(([n])=>n!=="role")),"core document baseline unchanged");
}
for(const [name,path] of [["observe.proposed.py.txt",F+"/observe.py"],["capture.proposed.sh.txt",F+"/capture.sh"]]){
 const k=records.get(D+"/"+name),f=manifest.proposed_future_artifacts.find(x=>x.carrier===name);
 same(f,{carrier:name,future_path:path,proposed_bytes:k.bytes,proposed_sha256:k.sha256,actual_future_metadata:null,actual_future_presence:null,actual_future_hash:null},"future proposed bytes not physical keys");
}
ok(manifest.proposed_future_artifacts.length===2&&manifest.operation_authorized===false&&manifest.independent_review_accepted===false&&manifest.actual_enabled_materialization===false&&manifest.actual_capture_or_observation===false,"exact prospective manifest no grant");
function verifyDiff(entry){
 ok(entry.result.exit_code===1&&!entry.result.session_id,"actual diff complete and differs");
 const before=read(entry.oldPath).toString("utf8"),after=read(entry.newPath).toString("utf8"),diff=entry.result.output;
 ok([before,after,diff].every(x=>x.endsWith("\n")),"complete LF texts");
 const a=before.slice(0,-1).split("\n"),b=after.slice(0,-1).split("\n"),lines=diff.slice(0,-1).split("\n");
 ok(lines[0].startsWith("--- "+entry.oldPath+"\t")&&lines[1].startsWith("+++ "+entry.newPath+"\t"),"exact diff file headers");
 let at=2,ai=0,bi=0,hunks=0;
 while(at<lines.length){
  const m=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(?:.*)$/.exec(lines[at++]);ok(!!m,"valid hunk header");
  const ac=m[2]===undefined?1:Number(m[2]),bc=m[4]===undefined?1:Number(m[4]);
  const as=Number(m[1])-(ac?1:0),bs=Number(m[3])-(bc?1:0);
  ok(as>=ai&&bs>=bi,"nonoverlapping hunks");same(a.slice(ai,as),b.slice(bi,bs),"whole unchanged hunk gap");
  ai=as;bi=bs;let ca=0,cb=0;
  while(at<lines.length&&!lines[at].startsWith("@@ ")){
   const line=lines[at++],mark=line[0],body=line.slice(1);
   ok([" ","-","+"].includes(mark),"ordinary complete diff line");
   if(mark!="+"){ok(a[ai++]===body,"old hunk line");ca++;}
   if(mark!=="-"){ok(b[bi++]===body,"new hunk line");cb++;}
  }
  ok(ca===ac&&cb===bc,"whole hunk counts");hunks++;
 }
 ok(hunks>0,"at least one hunk");same(a.slice(ai),b.slice(bi),"whole unchanged diff suffix");
 return{role:entry.role,hunks,old_bytes:Buffer.byteLength(before),new_bytes:Buffer.byteLength(after),diff_bytes:Buffer.byteLength(diff)};
}
const diffEntries=json("SOURCE_DIFF_NATIVE.json").diffs;
same(diffEntries.map(x=>x.role),["source_observer","source_capture","binding","request","enabled_observer","enabled_capture"],"all six exact native diffs");
const diffs=diffEntries.map(verifyDiff);
const orientation=json("ORIENTATION_NATIVE.json");
ok(orientation.absence.result.exit_code===0,"owned preparation absence result");
ok(orientation.absence.request.cmd==="test ! -e "+D,"only own directory absence target");
const failed=orientation.reads.find(x=>x.role==="request");
ok(failed.result.exit_code===2&&failed.path===S+"/REQUEST.disabled.json","failed documentary navigation retained");
ok(failed.result.output.includes("No such file or directory"),"actual failure diagnostic retained");
for(const name of OWN)read(D+"/"+name);
for(const name of ["PREPARATION.md","READ_SCOPE.md"])ok(txt(name).includes("HOLD_EXTERNAL")||name==="READ_SCOPE.md","document trust scope");
const output={scope:"AUTHOR_DOCUMENTARY_CHECK_ONLY_NOT_PYTHON_BASH_RUNTIME_OR_INDEPENDENT_ACCEPTANCE",checks,raw_pairs:rawPairs,raw_paired_bytes:rawBytes,selected_input_keys:16,prepared_artifact_keys:11,all_document_keys:records.size,relocated_observer_strings:relocated,consumed_top_level_fields:consumed,finite_files:69,finite_modules:62,diffs,keys:[...records.values()]};
process.stdout.write(JSON.stringify(output,null,2)+"\n");
