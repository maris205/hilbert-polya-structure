"use strict";
// Finite frozen documentary/source/capture bytes plus the two original raw streams only.
// Stored request strings are DATA: no child_process, eval, Python, shell or target recrawl.
const fs=require("node:fs"),io=require("./DOCUMENTARY_IO.cjs");
const Q="docs/papers211_215_sequence/qa/",A=Q+"p213_minimal_observer_probe_audit01/";
let checks=0,oldKeyComparisons=0;const ok=(v,m)=>{checks++;if(!v)throw Error("documentary: "+m)};
function equal(a,b){if(a===b)return true;if(!a||!b||typeof a!==typeof b||typeof a!=="object"||Array.isArray(a)!==Array.isArray(b))return false;const ak=Object.keys(a).sort(),bk=Object.keys(b).sort();return JSON.stringify(ak)===JSON.stringify(bk)&&ak.every(k=>equal(a[k],b[k]));}
const eq=(a,b,m)=>ok(equal(a,b),m);
const begin=io.captureDirectory(),inputs=new Map([...io.documents,...io.rawFiles].map(p=>[p,io.openDocument(p)]));
const get=p=>{p=io.relative(p);ok(inputs.has(p),"reference belongs to fixed allowed documentary/raw set");return inputs.get(p)};
const doc=p=>JSON.parse(get(p).bytes.toString("utf8")); // native envelopes have floats; all compared external metadata are integer STRINGS.
const baseline=JSON.parse(fs.readFileSync(A+"BASELINE_NATIVE.json","utf8"));
const base=JSON.parse((baseline.native||baseline.result).output);
ok((baseline.native||baseline.result).exit_code===0,"actual independent baseline exit");
eq(begin,base.capture_before,"whole original capture directory key and inventory unchanged");
ok(base.keys.length===51&&inputs.size===51,"finite 49 documentary / 2 stream keys");
for(const k of base.keys)eq(get(k.path).key,k,"all 13 metadata fields/fd stages/full bytes/hash versus baseline");
function oldKey(k){const now=get(k.path).key;eq(Object.keys(k).sort(),["bytes","metadata","path","sha256"],"producer old complete key schema");eq(k,{path:"/root/autodl-tmp/symbolic_dynamics/"+now.path,metadata:now.metadata,bytes:now.bytes,sha256:now.sha256},"whole producer documented key unchanged");oldKeyComparisons++;}
function native(path,chunk){const d=doc(path);ok(d.result&&d.result.exit_code===0&&d.result.chunk_id===chunk&&!Object.hasOwn(d.result,"session_id"),"exact complete archived native "+chunk);ok(typeof d.result.output==="string"&&!d.result.output.includes("tokens truncated"),"untruncated archived native string");return {envelope:d,data:JSON.parse(d.result.output)};}
const packageSpec={
 p213_minimal_observer_probe_root01:{seal:"6584a60e1b5309d5253dae92ec130ba0d566c5a835dcbee53e9a91d5492d0f82",count:13},
 p213_minimal_observer_materialization01:{seal:"35c1d67dadfd7c5d7abb5c16d95902c26e816fd4a3f5a47b566a744f3424381d",count:6},
 p213_minimal_observer_enabled_root01:{seal:"43c9e6401cd9189461df4e081d6d6aff219afb1bab8bd82df82d0b6cbdccf45c",count:8},
 p213_minimal_observer_enabled01:{seal:"b325f1f4b51b436f6390a50217b95ad65deec65e6ea3e298aefba547c22cc0dc",count:2}
};
function manifest(pkg){const s=get(Q+pkg+"/SHA256SUMS");ok(s.bytes[s.bytes.length-1]===10,"manifest final LF");const rows=s.bytes.toString("ascii").slice(0,-1).split("\n").map(l=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_][A-Za-z0-9_.-]*)$/.exec(l);ok(!!m,"strict flat manifest grammar");return {name:m[2],sha:m[1]}});ok(new Set(rows.map(x=>x.name)).size===rows.length&&rows.every(x=>x.name!=="SHA256SUMS"),"manifest no duplicate/self");eq(rows.map(x=>x.name),rows.map(x=>x.name).sort(),"manifest sorted names");return {key:s.key,rows};}
const packages=[];
for(const [pkg,p]of Object.entries(packageSpec)){
 const m=manifest(pkg);eq(m.key.sha256,p.seal,"externally commissioned package seal");ok(m.rows.length===p.count,"exact sealed payload count");
 const d=Q+pkg,before=fs.lstatSync(d,{bigint:true});ok(before.isDirectory()&&!before.isSymbolicLink(),"finite frozen documentary package directory");
 const inventory=fs.readdirSync(d).sort(),after=fs.lstatSync(d,{bigint:true});eq(io.md(before),io.md(after),"documentary package directory stable during inventory");
 eq(inventory,["SHA256SUMS",...m.rows.map(x=>x.name)].sort(),"strict exact no-extra package inventory");eq(inventory,io.packages[pkg].slice().sort(),"inventory within predeclared finite package capability");
 for(const r of m.rows)eq(get(Q+pkg+"/"+r.name).key.sha256,r.sha,"whole payload against manifest");packages.push({path:d,seal:m.key.sha256,payloads:m.rows.length,files:inventory.length,directory:io.md(before)});
}
const grant=doc(Q+"p213_minimal_observer_probe_root01/GRANT.json"),attempt=doc(Q+"p213_minimal_observer_probe_root01/ATTEMPT_COMMITTED.json"),observation=doc(Q+"p213_minimal_observer_probe_root01/OBSERVATION_NATIVE.json"),request=doc(Q+"p213_minimal_observer_enabled_preparation01/PROPOSED_REQUEST.json");
ok(grant.schema==="P213_ROOT_ONE_EXACT_PROBE_GRANT_V1"&&grant.issuer==="/root"&&grant.authorization==="ONE_ATTEMPT_ONLY_CONDITIONAL_ON_EXACT_PRECHECK_NO_RETRY","one exact root grant");
ok(grant.exact_tool==="exec_command"&&grant.science_build_or_manuscript_authority===false&&grant.external_status==="HOLD_EXTERNAL","precise tool and authority boundary");
eq(grant.raw_reception.stdout,"/root/autodl-tmp/symbolic_dynamics/"+io.rawFiles[0],"only original stdout authority");eq(grant.raw_reception.stderr,"/root/autodl-tmp/symbolic_dynamics/"+io.rawFiles[1],"only original stderr authority");ok(grant.raw_reception.native_exit_zero_is_acceptance===false,"no producer self acceptance");
for(const k of[grant.basis.source_root_receipt,grant.basis.independent_acceptance,grant.basis.materialization_receipt])eq(get(k.path).key.sha256,k.sha256,"exact authority basis");
eq(grant.basis.source_root_seal,packageSpec.p213_minimal_observer_enabled_root01.seal,"source reception seal basis");eq(grant.basis.materialization_seal,packageSpec.p213_minimal_observer_materialization01.seal,"materialization basis");eq(grant.basis.enabled_source_seal,packageSpec.p213_minimal_observer_enabled01.seal,"real source basis");
for(const r of[request.proposed_request,attempt.exact_request,observation.request])eq(r,grant.exact_request,"exact seven-field request equality");
eq(Object.keys(grant.exact_request).sort(),["cmd","login","max_output_tokens","shell","tty","workdir","yield_time_ms"],"complete native request fields");
ok(request.enabled===false&&request.operation_authorized===false&&request.actual_session_id===null,"prospective request retained not retroactively enabled");
ok(attempt.attempt_budget_consumed===true&&attempt.native_invocation_result_not_yet_observed===true&&attempt.no_second_invocation===true&&attempt.preflight_native_chunk==="6fae0c"&&attempt.preflight_exit===0,"immutable consumed intent");
eq(observation.result,{chunk_id:"5ac0e8",wall_time_seconds:0.00000351,exit_code:0,original_token_count:7,output:"P213_OBSERVER_NATIVE_EXIT=0\n"},"sole actual native result exact including no session");
const preflight=native(Q+"p213_minimal_observer_probe_root01/PREFLIGHT_NATIVE.json","6fae0c");
ok(preflight.data.checks===81&&preflight.data.keys.length===13&&preflight.data.observerInvoked===false,"original preflight count and phase");for(const k of preflight.data.keys)oldKey(k);
eq(preflight.data.request,grant.exact_request,"preflight request commitment");eq(preflight.data.probeAbsence,{operation:"lstat",path:"/root/autodl-tmp/symbolic_dynamics/"+io.capture,code:"ENOENT"},"historical exact absence, not fresh query");
ok(BigInt(preflight.data.availableBytes)>=67108864n&&preflight.data.capacityMinimum==="67108864","historical finite capacity sufficient");
const chronology=["GRANT.json","PREFLIGHT_NATIVE.json","ATTEMPT_COMMITTED.json"].map(n=>BigInt(get(Q+"p213_minimal_observer_probe_root01/"+n).key.metadata.mtimeNs));
ok(chronology[0]<chronology[1]&&chronology[1]<chronology[2]&&chronology[2]<BigInt(begin.metadata.birthtimeNs)&&BigInt(begin.metadata.birthtimeNs)<=BigInt(get(io.rawFiles[0]).key.metadata.mtimeNs)&&BigInt(get(io.rawFiles[0]).key.metadata.mtimeNs)<BigInt(get(Q+"p213_minimal_observer_probe_root01/OBSERVATION_NATIVE.json").key.metadata.mtimeNs),"recorded documentary chronology agrees with precommit then capture then receipt; ordinary clock trust only");
const matchdoc=doc(Q+"p213_minimal_observer_materialization01/BYTE_MATCH_NATIVE.json"),match=JSON.parse(matchdoc.result.output);ok(matchdoc.result.exit_code===0&&match.keys.length===4&&match.rawPairs.length===2&&match.bytes===100314&&match.observerExecuted===false&&match.probeAllocatedOrQueried===false,"actual four materialization keys and two pairs");for(const k of match.keys)oldKey(k);
const exactPairs=[];for(const [carrier,real,n]of[["observe.proposed.py.txt","observe.py",98365],["capture.proposed.sh.txt","capture.sh",1949]]){const a=get(Q+"p213_minimal_observer_enabled_preparation01/"+carrier),b=get(Q+"p213_minimal_observer_enabled01/"+real);ok(a.bytes.equals(b.bytes)&&a.bytes.length===n,"whole actual/prospective physical bytes equal");exactPairs.push({carrier:a.key.path,real:b.key.path,bytes:n,sha256:b.key.sha256})}
const acceptance=doc(Q+"p213_minimal_observer_enabled_preparation_audit01/ACCEPTANCE.json");ok(acceptance.verdict==="ACCEPT_EXACT_PROSPECTIVE_SOURCE_LITERAL_CAPTURE_REQUEST"&&acceptance.operation_or_allocation_grant===false&&acceptance.runtime_or_scientific_acceptance===false,"prior nonauthor accepted exact source scope only");
const prep=manifest("p213_minimal_observer_enabled_preparation01");eq(prep.key.sha256,acceptance.author_sha256sums,"accepted complete preparation seal only; not full historical payload re-audit");
for(const n of io.packages.p213_minimal_observer_enabled_preparation01.filter(x=>x!=="SHA256SUMS")){const r=prep.rows.find(r=>r.name===n);ok(!!r,"selected exact preparation member exists");eq(get(Q+"p213_minimal_observer_enabled_preparation01/"+n).key.sha256,r.sha,"selected preparation member exact hash")}
for(const [n,h]of Object.entries(acceptance.exact_contracts))if(["PROPOSED_REQUEST.json","BINDING.runtime_literal.json"].includes(n))eq(get(Q+"p213_minimal_observer_enabled_preparation01/"+n).key.sha256,h,"explicit accepted request/binding commitment");
for(const p of acceptance.reviewed_prospective_artifacts){const a=get(Q+"p213_minimal_observer_enabled_preparation01/"+p.existing_documentary_carrier),b=get(p.exact_future_destination_string);ok(a.key.sha256===p.sha256&&b.key.sha256===p.sha256&&a.key.bytes===p.bytes&&b.key.bytes===p.bytes,"prior acceptance exact pair commitments")}
const previous=manifest("p213_minimal_observer_enabled_preparation_audit01");for(const n of ["ACCEPTANCE.json","REPORT.md","FINDINGS.json"]){const r=previous.rows.find(r=>r.name===n);ok(!!r,"selected prior review member");eq(get(Q+"p213_minimal_observer_enabled_preparation_audit01/"+n).key.sha256,r.sha,"selected prior review hash")}
const initial=native(Q+"p213_minimal_observer_probe_root01/INITIAL_RAW_RECEIVE_NATIVE.json","a7ce2d");ok(initial.data.checks===16&&initial.data.keys.length===2&&initial.data.probeRerun===false&&initial.data.runtime_accepted===false,"original preliminary receive not acceptance");
for(const k of initial.data.keys)oldKey(k);eq(initial.data.directory,{path:"/root/autodl-tmp/symbolic_dynamics/"+begin.path,metadata:begin.metadata},"original whole capture directory key");
const warning=get(Q+"p213_minimal_observer_probe_root01/PRECISION_LIMIT.md").bytes.toString("utf8");ok(warning.includes("MUST NOT")&&warning.includes("rounds integer values")&&warning.includes("bytes\nare unchanged"),"original precision warning retained");
// Deliberately do not compare INITIAL_RAW_RECEIVE_NATIVE's rounded sourceKey numbers.
const lossless=native(Q+"p213_minimal_observer_probe_root01/LOSSLESS_NATIVE.json","4a1f09");ok(lossless.data.rawBytes===322982&&lossless.data.rawSha256===get(io.rawFiles[0]).key.sha256&&lossless.data.integerTokens===4591&&lossless.data.unsafeMagnitudeTokens===696&&lossless.data.objects===934&&lossless.data.sourceKeyComparisons.length===10,"supplementary limited producer integer check retained");
const close=native(Q+"p213_minimal_observer_probe_root01/CLOSING_NATIVE.json","14acd2");ok(close.data.checks===411&&close.data.keys.length===26&&close.data.keyCount===26&&close.data.runtimeAccepted===false&&close.data.observerRerun===false&&close.data.precisionProjectionWarningRetained===true,"original producer close, not independent verdict");for(const k of close.data.keys)oldKey(k);
eq(get(Q+"p213_minimal_observer_probe_root01/HANDOFF.md").key.sha256,"6c8cadbdd0e1ef47bf1167f67274ba44a6f5803e7985e9f7f951c7c07576a395","commissioned exact handoff");
const rawManifest=get(Q+"p213_minimal_observer_probe_root01/RAW_INPUTS.sha256").bytes.toString("utf8");for(const p of io.rawFiles)ok(rawManifest.includes(get(p).key.sha256+"  "+"/root/autodl-tmp/symbolic_dynamics/"+p),"exact raw manifest entry");
eq(io.captureDirectory(),begin,"closing authorized capture inventory/key unchanged");
process.stdout.write(JSON.stringify({verdict:"DOCUMENTARY_AND_EXACT_RUNTIME_INPUT_CHAIN_PASS",checks,oldKeyComparisons,wholeInputKeys:inputs.size,documentaryFiles:io.documents.length,rawFiles:io.rawFiles.length,packages,selectedHistoricalManifestPins:[{package:"p213_minimal_observer_enabled_preparation01",seal:prep.key.sha256,selected:5},{package:"p213_minimal_observer_enabled_preparation_audit01",seal:previous.key.sha256,selected:3}],exactPairs,originalActualNative:observation.result,chronologyNanoseconds:chronology.map(String),allBaselineInputKeysPreserved:true,allProducerKeysPreserved:true,exactRawDirectoryAndStreamsPreserved:true,precisionProjectionRetainedNotUsedAsExactRuntimeKey:true,observerRerun:false,observedRuntimeTargetsRecrawled:false,scienceBuildOrManuscriptAuthority:false,externalStatus:"HOLD_EXTERNAL"},null,2)+"\n");
