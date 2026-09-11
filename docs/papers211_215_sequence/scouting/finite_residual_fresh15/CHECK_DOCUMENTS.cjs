"use strict";
// READ-ONLY DOCUMENTARY CHECK. No model map, old code, build or observer is executed.
const fs=require("node:fs"),crypto=require("node:crypto");
const D="docs/papers211_215_sequence/scouting/finite_residual_fresh15",inputs=[
  {
    "role": "skill",
    "path": "/root/autodl-tmp/symbolic_dynamics/.agents/skills/symbolic-dynamics-research/SKILL.md"
  },
  {
    "role": "research_lit",
    "path": "/root/autodl-tmp/.codex/skills/research-lit/SKILL.md"
  },
  {
    "role": "proof_skill",
    "path": "/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md"
  },
  {
    "role": "workflow",
    "path": "docs/research_state/WORKFLOW.md"
  },
  {
    "role": "anchor",
    "path": "docs/papers211_215_sequence/PROBLEM_ANCHOR.md"
  },
  {
    "role": "old_criteria",
    "path": "docs/papers197_201_sequence/PROBLEM_ANCHOR.md"
  },
  {
    "role": "fresh11",
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh11/HANDOFF.md"
  },
  {
    "role": "fresh12",
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh12/HANDOFF.md"
  },
  {
    "role": "fresh13",
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh13/HANDOFF.md"
  },
  {
    "role": "fresh14",
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh14/HANDOFF.md"
  },
  {
    "role": "old_algebra",
    "path": "docs/papers204_208_sequence/scouting/algebra/SCOUT_REPORT.md"
  },
  {
    "role": "current_normal_form",
    "path": "docs/papers211_215_sequence/scouting/finite_algebraic_normal_form_fresh_desk/HANDOFF.md"
  },
  {
    "role": "ring_as_boundary",
    "path": "docs/papers211_215_sequence/scouting/arithmetic_automata_residual02/HANDOFF.md"
  },
  {
    "role": "fresh14_sources",
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh14/SOURCES_AND_LIMITS.md"
  },
  {
    "role": "old_utas",
    "path": "docs/papers162_166_sequence/scouting/open_fresh_p166/SCOUT.md"
  },
  {
    "role": "old_thuemorse_ledger",
    "path": "docs/papers162_166_sequence/scouting/open_fresh_p166/IDEA_LEDGER.md"
  },
  {
    "role": "old_semigroup",
    "path": "docs/papers204_208_sequence/scouting/algebra_second/SCOUT_REPORT.md"
  },
  {
    "role": "old_ut_owner",
    "path": "docs/papers162_166_sequence/scouting/open_fresh_p166/OWNER_SEARCH_LOG.md"
  },
  {
    "role": "old_histogram",
    "path": "docs/papers204_208_sequence/scouting/word_local/NCC_PROOF_BOUNDARY.md"
  },
  {
    "role": "old_matrix_owner",
    "path": "docs/papers204_208_sequence/scouting/algebra/SOURCE_AND_COLLISION_NOTES.md"
  }
],base=["CHECK_DOCUMENTS.cjs","DOCUMENTARY_REQUEST_RETURNS.json","HANDOFF.md","INPUT_KEYS_NATIVE.json","KEY_INPUT_DOCUMENTS.cjs","PROOF_PACKAGE.md","SCOPE.json","SOURCES_AND_LIMITS.md","WEB_REQUEST_RETURNS.json"];
const fields=["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"],md=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
let checks=0,rawPairs=0,rawBytes=0;
const ok=(v,m)=>{checks++;if(!v)throw Error(m);};
const sha=b=>crypto.createHash("sha256").update(b).digest("hex"),cache=new Map();
function file(path){
 if(cache.has(path))return cache.get(path);
 const a=fs.lstatSync(path,{bigint:true});
 ok(a.isFile()&&!a.isSymbolicLink(),"regular no leaf link "+path);
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  const f=fs.fstatSync(fd,{bigint:true}),b=fs.readFileSync(fd),g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(path,{bigint:true});
  for(const x of[f,g,z])ok(JSON.stringify(md(a))===JSON.stringify(md(x)),"stable full metadata "+path);
  ok(BigInt(b.length)===a.size,"full EOF "+path);
  const r={path,sha256:sha(b),bytes:b.length,metadata:md(a),fd_end:md(g),path_end:md(z),full_eof:true,leaf_links:[]};
  const out={r,b};cache.set(path,out);return out;
 }finally{fs.closeSync(fd);}
}
const json=n=>JSON.parse(file(D+"/"+n).b.toString("utf8"));
const names=fs.readdirSync(D).sort();
ok(base.every(n=>names.includes(n)),"all base payloads present");
ok(names.every(n=>base.includes(n)||["CHECK_NATIVE.json","SHA256SUMS"].includes(n)),"exact owned file scope");
for(const n of base)file(D+"/"+n);
const scope=json("SCOPE.json");
ok(scope.owned_directory===D,"exact owned path");
for(const [k,v]of Object.entries(scope.counts))ok(v===0,"zero count "+k);
for(const k of["current_batch_indices_edited","previous_packets_edited","scientific_execution","runtime_or_host_or_private_or_input_or_observer_or_capture_execution","git_or_ssh","external_manuscript_upload","operational_authority","independent_review"])ok(scope[k]===false,"explicit boundary "+k);
const native=json("DOCUMENTARY_REQUEST_RETURNS.json"),web=json("WEB_REQUEST_RETURNS.json");
ok(native.records.length===35,"35 original documentary calls");
ok(new Set(native.records.map(x=>x.role)).size===35,"unique documentary roles");
for(const x of native.records){
 ok(x.request.workdir==="/root/autodl-tmp/symbolic_dynamics","fixed read cwd "+x.role);
 ok(typeof x.result.output==="string"&&typeof x.result.chunk_id==="string","actual native shape "+x.role);
 ok(Number.isInteger(x.result.exit_code),"completed original native "+x.role);
}
const get=r=>native.records.find(x=>x.role===r);
ok(get("absence").result.exit_code===0&&get("absence").result.output==="","actual initial absence success");
ok(get("discovery").result.exit_code===2,"preserve failed broad navigation");
ok(get("old_ut_source").result.exit_code===2,"preserve missing guessed document");
ok(get("arxiv_script").result.exit_code===1,"preserve script non-hit");
for(const r of["state","discovery","search_noncommutative_combinatorial"])ok(get(r).result.original_token_count>get(r).request.max_output_tokens,"preserve truncated native "+r);
ok(web.records.length===6&&new Set(web.records.map(x=>x.role)).size===6,"six original web calls");
for(const x of web.records)ok(x.request&&typeof x.result==="string","actual string web return "+x.role);
ok(web.records.find(x=>x.role==="primary01").result.includes("Internal Error"),"preserve inaccessible primary route");
ok(web.records.find(x=>x.role==="primary05").request.screenshot.length===2,"two attempted primary page images");
ok(web.records.find(x=>x.role==="primary05").result.includes("web screenshot is not enabled"),"preserve unavailable screenshot failure");
const pinNative=json("INPUT_KEYS_NATIVE.json");
ok(pinNative.result.exit_code===0,"actual input key success");
const pins=JSON.parse(pinNative.result.output);
ok(pins.scope==="POSTREAD_DOCUMENTARY_KEYS_ONLY_NOT_PRE_READ_BRACKET","postread boundary explicit");
ok(pins.keys.length===inputs.length&&inputs.length===20,"20 selected input keys");
for(const x of inputs){
 const old=pins.keys.find(k=>k.role===x.role),cur=file(x.path),read=get(x.role);
 ok(old&&old.path===x.path,"exact input role/path "+x.role);
 const oldWithoutRole={...old};delete oldWithoutRole.role;
 ok(JSON.stringify(oldWithoutRole)===JSON.stringify(cur.r),"all full postread keys unchanged "+x.role);
 const m=/^sed -n '1,([0-9]+)p' /.exec(read.request.cmd);
 ok(!!m,"explicit bounded documentary read "+x.role);
 const lineParts=cur.b.toString("utf8").match(/[^\n]*\n|[^\n]+$/g)||[];
 const expected=Buffer.from(lineParts.slice(0,Number(m[1])).join(""),"utf8");
 const actual=Buffer.from(read.result.output,"utf8");
 ok(expected.equals(actual),"actual read equals exact requested document lines "+x.role);
 rawPairs++;rawBytes+=actual.length;
}
for(const n of["HANDOFF.md","SOURCES_AND_LIMITS.md","PROOF_PACKAGE.md"])ok(file(D+"/"+n).b.toString("utf8").includes("HOLD_EXTERNAL")||n==="PROOF_PACKAGE.md","hold/readable document "+n);
for(const n of["HANDOFF.md","SOURCES_AND_LIMITS.md"])ok(file(D+"/"+n).b.toString("utf8").includes("ZERO_NEW_ENTRANCE"),"explicit zero handoff "+n);
process.stdout.write(JSON.stringify({scope:"FRESH15_DOCUMENTARY_ONLY_NOT_SCIENCE_OR_INDEPENDENT_REVIEW",checks,raw_pairs:rawPairs,raw_paired_bytes:rawBytes,original_documentary_calls:native.records.length,original_web_calls:web.records.length,postread_input_keys:inputs.length,base_payloads:base.length,zero_new_entrances:scope.counts.new_literal_entrances,keys:[...cache.values()].map(x=>x.r)},null,2)+"\n");
