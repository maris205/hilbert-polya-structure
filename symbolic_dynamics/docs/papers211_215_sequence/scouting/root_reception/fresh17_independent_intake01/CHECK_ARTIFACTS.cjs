"use strict";
// Independent, read-only documentary receipt. No source evaluation, imports,
// network, process discovery, scientific maps, Python, or child processes.
const fs=require("node:fs"),crypto=require("node:crypto");
const CWD="/root/autodl-tmp/symbolic_dynamics";
const D="docs/papers211_215_sequence/scouting/finite_residual_fresh17";
const O="docs/papers211_215_sequence/scouting/root_reception/fresh17_independent_intake01";
const phase=process.argv[2];
if(!["before","after"].includes(phase)||process.argv.length!==3)throw Error("Use only before or after");
const names=["CHECK_DOCUMENTS.cjs","CHECK_NATIVE.json","DOCUMENTARY_REQUEST_RETURNS.json","HANDOFF.md","INPUT_KEYS_NATIVE.json","KEY_INPUT_DOCUMENTS.cjs","PROOF_PACKAGE.md","SCOPE.json","SOURCES_AND_LIMITS.md","WEB_REQUEST_RETURNS.json","SHA256SUMS"].sort();
const inputs=[
["skill",CWD+"/.agents/skills/symbolic-dynamics-research/SKILL.md"],
["research_lit","/root/autodl-tmp/.codex/skills/research-lit/SKILL.md"],
["workflow","docs/research_state/WORKFLOW.md"],
["anchor","docs/papers211_215_sequence/PROBLEM_ANCHOR.md"],
["criteria","docs/papers197_201_sequence/PROBLEM_ANCHOR.md"],
["proof_skill","/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md"],
["combinatorial","docs/papers204_208_sequence/scouting/combinatorial/SCOUT_REPORT.md"],
["combinatorial_second","docs/papers204_208_sequence/scouting/combinatorial_second/SCOUT_REPORT.md"],
["permutation_boundary","docs/papers211_215_sequence/scouting/finite_permutation_gap_desk01/SOURCES_AND_SUBTRACTION.md"],
["word_tree","docs/papers211_215_sequence/scouting/finite_word_tree_new_desk/HANDOFF.md"],
["pla_original","docs/papers152_156_sequence/scouting/combinatorial/SCOUT.md"],
["geometry_report","docs/papers211_215_sequence/scouting/discrete_geometry_gap_desk/REPORT.md"],
["geometry_sources","docs/papers211_215_sequence/scouting/discrete_geometry_gap_desk/SOURCE_READS.md"],
["matroid_parity_old","docs/papers122_126_sequence/scouting/combinatorial/SCOUT.md"],
["matroid_simplification_old","docs/papers162_166_sequence/scouting/open_fresh_p166_round2/SCOUT.md"],
["matroid_coloop_old","docs/papers211_215_sequence/scouting/set_code_lane/PROOF_PACKAGE.md"],
["matroid_coloop_intake","docs/papers211_215_sequence/scouting/set_code_lane/INTAKE.md"]
];
const fields=["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
const md=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const allowed=new Set([...names.map(n=>D+"/"+n),...inputs.map(x=>x[1]),O+"/SOURCE_READ_NATIVE.json",O+"/CHECK_ARTIFACTS.cjs",O+"/PRECHECK_CORRECTED_NATIVE.json",O+"/AUTHOR_REPLAY_NATIVE.json"]);
const cache=new Map();let checks=0,pairedBytes=0;
function ok(v,m){checks++;if(!v)throw Error(m);}
function file(p){
  ok(allowed.has(p),"fixed allowlist "+p);
  if(cache.has(p))return cache.get(p);
  const a=fs.lstatSync(p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),"regular nonsymlink leaf "+p);
  const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try{
    const f=fs.fstatSync(fd,{bigint:true}),b=fs.readFileSync(fd),g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(p,{bigint:true});
    for(const x of[f,g,z])ok(eq(md(a),md(x)),"all metadata stable "+p);
    ok(BigInt(b.length)===a.size,"full EOF "+p);
    const r={path:p,sha256:sha(b),bytes:b.length,metadata:md(a),fd_end:md(g),path_end:md(z),full_eof:true,leaf_links:[]};
    const value={b,r};cache.set(p,value);return value;
  }finally{fs.closeSync(fd);}
}
const json=p=>JSON.parse(file(p).b.toString("utf8"));
ok(process.cwd()===CWD,"literal cwd");
ok(eq(fs.readdirSync(D).sort(),names),"strict 11-file source inventory");
for(const n of names)file(D+"/"+n);
const seal=file(D+"/SHA256SUMS");
ok(seal.r.sha256==="e209e7a21e84112ea49ed8d08c306a596e2c43f38edaf53b7a11ce99640da7c0","frozen source seal");
const entries=seal.b.toString("utf8").trimEnd().split("\n").map(line=>{
  const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.]+)$/.exec(line);ok(!!m,"literal manifest line");return{sha256:m[1],name:m[2]};
});
ok(entries.length===10&&new Set(entries.map(x=>x.name)).size===10,"nonself source manifest unique");
ok(eq(entries.map(x=>x.name).sort(),names.filter(n=>n!=="SHA256SUMS")),"all and only 10 payloads");
let payloadBytes=0;
for(const e of entries){const x=file(D+"/"+e.name);ok(x.r.sha256===e.sha256,"manifest payload "+e.name);payloadBytes+=x.b.length;}
ok(payloadBytes===694573,"frozen source payload byte count");
const native=json(D+"/DOCUMENTARY_REQUEST_RETURNS.json"),web=json(D+"/WEB_REQUEST_RETURNS.json");
ok(native.records.length===31&&new Set(native.records.map(x=>x.role)).size===31,"31 unique author native records");
const nativeCensus=native.records.map(x=>{
  ok(x.request.workdir===CWD&&typeof x.result.output==="string"&&typeof x.result.chunk_id==="string"&&Number.isInteger(x.result.exit_code),"native original shape "+x.role);
  const b=Buffer.from(x.result.output,"utf8");
  return{role:x.role,request:x.request,chunk_id:x.result.chunk_id,exit_code:x.result.exit_code,original_token_count:x.result.original_token_count,output_bytes:b.length,output_sha256:sha(b),native_truncation:/^Warning: truncated output\b/.test(x.result.output)};
});
const get=r=>native.records.find(x=>x.role===r);
ok(get("arxiv_script").result.exit_code===1&&get("arxiv_script").result.output==="","original missing script");
ok(get("geometry_old").result.exit_code===2&&get("geometry_old").result.output.includes("No such file"),"original wrong filename");
ok(get("prior_carrier_search").result.original_token_count===122034&&/truncat/i.test(get("prior_carrier_search").result.output.slice(0,180)),"original truncated search");
ok(get("absence").result.exit_code===0,"original successful absence");
ok(eq(native.optional_configured_tool_name_discovery.result,[]),"original optional-tool nonhit");
ok(web.records.length===9&&new Set(web.records.map(x=>x.role)).size===9,"nine unique original web records");
const webCensus=web.records.map(x=>{
  ok(x.request&&typeof x.result==="string","archived provider string "+x.role);
  const b=Buffer.from(x.result,"utf8");return{role:x.role,request:x.request,output_bytes:b.length,output_sha256:sha(b)};
});
ok(web.records.find(x=>x.role==="owner_primary_bodies").result.includes("Internal Error"),"original direct publisher failure");
const keyNative=json(D+"/INPUT_KEYS_NATIVE.json"),oldCheckNative=json(D+"/CHECK_NATIVE.json");
ok(keyNative.result.exit_code===0&&oldCheckNative.result.exit_code===0,"actual author key/check success");
const pins=JSON.parse(keyNative.result.output),oldCheck=JSON.parse(oldCheckNative.result.output);
ok(pins.scope==="POSTREAD_DOCUMENTARY_KEYS_NOT_PRIOR_READ_BRACKET"&&pins.keys.length===17,"17 post-read input keys only");
ok(oldCheck.checks===291&&oldCheck.raw_pairs===18&&oldCheck.raw_paired_bytes===94309&&oldCheck.keys.length===26,"exact old author documentary counters");
const pairs=[];
function rawPair(read,p,label){
  ok(read.result.exit_code===0,"successful exact read "+label);
  const m=/^sed -n '(\d+),(\d+)p' (.+)$/.exec(read.request.cmd);ok(!!m,"exact line selector "+label);
  const canonical=x=>x.startsWith(CWD+"/")?x.slice(CWD.length+1):x;
  ok(canonical(m[3])===canonical(p),"exact old source target "+label);
  const b=file(p).b,lines=b.toString("utf8").match(/[^\n]*\n|[^\n]+$/g)||[];
  const expected=Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join(""),"utf8"),actual=Buffer.from(read.result.output,"utf8");
  ok(expected.equals(actual),"actual complete selected UTF8 pair "+label);
  pairedBytes+=actual.length;pairs.push({label,path:p,from:Number(m[1]),to:Number(m[2]),bytes:actual.length,sha256:sha(actual),chunk_id:read.result.chunk_id});
}
for(const[role,p]of inputs){
  const old={...pins.keys.find(k=>k.role===role)};delete old.role;
  ok(eq(file(p).r,old),"all post-read full input keys unchanged "+role);
  rawPair(get(role),p,role);
}
rawPair(keyNative.source_read,D+"/KEY_INPUT_DOCUMENTS.cjs","author key source");
rawPair(oldCheckNative.source_read,D+"/CHECK_DOCUMENTS.cjs","author checker source");
ok(oldCheckNative.note_source_readbacks.length===3,"three full author proof/source/handoff readbacks");
for(const x of oldCheckNative.note_source_readbacks){
  const p=x.request.cmd.match(/^sed -n '\d+,\d+p' (.+)$/)?.[1];
  ok(["PROOF_PACKAGE.md","SOURCES_AND_LIMITS.md","HANDOFF.md"].some(n=>p===D+"/"+n),"fixed note readback");
  rawPair(x,p,"author "+p.split("/").at(-1));
}
ok(pairs.length===22,"22 exact original read pairs");
for(const k of oldCheck.keys)ok(eq(file(k.path).r,k),"all 26 complete archived author-check keys");
const scope=json(D+"/SCOPE.json");
ok(scope.owned_directory===D&&scope.counts.new_literal_desk_attempts===1&&scope.counts.substantive_directions===3,"literal denominator");
for(const[k,v]of Object.entries(scope.counts))if(!["new_literal_desk_attempts","substantive_directions"].includes(k))ok(v===0,"zero source count "+k);
for(const k of ["operational_authority","scientific_execution","host_private_runtime_input_observer_capture_execution","central_or_older_artifact_edits","manuscript_build","git_or_ssh","external_manuscript_upload","independent_review","child_source_contribution","child_intake_assistance","p212_or_p213_audit_or_raw_access","fresh16_child_intake_access"])ok(scope[k]===false,"scope false "+k);
const ownSource=file(O+"/CHECK_ARTIFACTS.cjs"),readLog=json(O+"/SOURCE_READ_NATIVE.json");
ok(readLog.schema==="FRESH17_INDEPENDENT_ACTUAL_SOURCE_READS_V1","own actual log scope");
const ownCensus=readLog.records.map((x,i)=>{
  ok(x.request&&typeof x.native.output==="string"&&typeof x.native.chunk_id==="string"&&Number.isInteger(x.native.exit_code),"own native original "+i);
  const b=Buffer.from(x.native.output,"utf8");return{index:i,chunk_id:x.native.chunk_id,exit_code:x.native.exit_code,output_bytes:b.length,output_sha256:sha(b),native_truncation:/^Warning: truncated output\b/.test(x.native.output)};
});
ok(readLog.records.some(x=>x.request.cmd==="sed -n '1,400p' "+O+"/CHECK_ARTIFACTS.cjs"&&x.native.exit_code===0&&Buffer.from(x.native.output,"utf8").equals(ownSource.b)),"complete own checker read before first run");
let replay=null;
if(phase==="after"){
  const beforeNative=json(O+"/PRECHECK_CORRECTED_NATIVE.json"),actual=json(O+"/AUTHOR_REPLAY_NATIVE.json");
  ok(beforeNative.native.exit_code===0&&actual.native.exit_code===0,"actual precheck and author replay successful");
  const before=JSON.parse(beforeNative.native.output);
  ok(before.phase==="before"&&before.source_payload_bytes===694573,"actual precheck scope");
  for(const k of before.keys)ok(eq(file(k.path).r,k),"every precheck full key unchanged "+k.path);
  ok(actual.request.cmd==="node "+D+"/CHECK_DOCUMENTS.cjs"&&actual.request.workdir===CWD,"exact reviewed author documentary command");
  const current=JSON.parse(actual.native.output);ok(eq(current,oldCheck),"complete author canonical equals actual independent replay");
  replay={chunk_id:actual.native.chunk_id,checks:current.checks,raw_pairs:current.raw_pairs,raw_paired_bytes:current.raw_paired_bytes,full_output_equal:true,precheck_keys_unchanged:before.keys.length};
}
process.stdout.write(JSON.stringify({
  scope:"INDEPENDENT_FRESH17_DOCUMENTARY_RECEIPT_NOT_MATH_OR_REVIEW_ACCEPTANCE",phase,checks,
  source_payloads:10,source_files:11,source_payload_bytes:payloadBytes,source_seal_sha256:seal.r.sha256,
  author_native_records:31,author_web_records:9,postread_inputs:17,original_raw_pairs:pairs.length,original_paired_bytes:pairedBytes,
  original_raw_pairs_census:pairs,author_native_census:nativeCensus,author_web_census:webCensus,
  own_actual_read_records:ownCensus.length,own_actual_read_census:ownCensus,replay,
  counts:{new_literal_entrances:1,new_control_entrances:0,pilots:0,nominations:0,central_mutations:0},
  trust_boundary:"UTF8 actual tool/provider text and full current documentary metadata; no retrospective read bracket, raw HTTP, subprocess stdout/stderr, hostile-runtime or scientific certification.",
  keys:[...cache.values()].map(x=>x.r)
},null,2)+"\n");
