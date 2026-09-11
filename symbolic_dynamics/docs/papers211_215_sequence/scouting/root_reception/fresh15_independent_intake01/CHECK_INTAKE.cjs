"use strict";
// Read-only documentary receiver. No child process, scientific map, target-path decoding or network.
const fs=require("node:fs"),crypto=require("node:crypto");
const D="docs/papers211_215_sequence/scouting/finite_residual_fresh15";
const I="docs/papers211_215_sequence/scouting/root_reception/fresh15_independent_intake01";
const authorNames=["CHECK_DOCUMENTS.cjs","CHECK_NATIVE.json","DOCUMENTARY_REQUEST_RETURNS.json","HANDOFF.md","INPUT_KEYS_NATIVE.json","KEY_INPUT_DOCUMENTS.cjs","PROOF_PACKAGE.md","SCOPE.json","SOURCES_AND_LIMITS.md","WEB_REQUEST_RETURNS.json"];
const fields=["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
const md=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
let checks=0,rawPairs=0,rawBytes=0;const cache=new Map();
function ok(v,m){checks++;if(!v)throw Error(m);}
function file(path){
 if(cache.has(path))return cache.get(path);
 const a=fs.lstatSync(path,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),"regular no-link document "+path);
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  const f=fs.fstatSync(fd,{bigint:true}),b=fs.readFileSync(fd),g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(path,{bigint:true});
  for(const s of[f,g,z])ok(JSON.stringify(md(a))===JSON.stringify(md(s)),"stable ten metadata fields "+path);
  ok(BigInt(b.length)===a.size,"full EOF "+path);
  const key={path,sha256:sha(b),bytes:b.length,metadata:md(a),fd_end:md(g),path_end:md(z),full_eof:true,leaf_links:[]};
  const out={b,key};cache.set(path,out);return out;
 }finally{fs.closeSync(fd);}
}
const json=p=>JSON.parse(file(p).b.toString("utf8"));
function equalKey(old,label){
 const k={...old};delete k.role;
 ok(JSON.stringify(k)===JSON.stringify(file(k.path).key),"complete unchanged native key "+label);
}
function pair(a,b,label){ok(Buffer.isBuffer(a)&&Buffer.isBuffer(b)&&a.equals(b),"raw bytes "+label);rawPairs++;rawBytes+=a.length;}
function native(x,label){
 ok(x&&x.request&&x.result&&typeof x.request.cmd==="string","native request "+label);
 ok(typeof x.result.chunk_id==="string"&&Number.isInteger(x.result.exit_code)&&typeof x.result.output==="string","actual completed return "+label);
 ok(!x.result.session_id,"not running "+label);
}
const seal=file(D+"/SHA256SUMS").b;
ok(sha(seal)==="c8e77c399b41714113d520a320f80127f8ba67eb3315933e5d51d7af00745ada","exact assigned author seal");
ok(seal[seal.length-1]===10,"manifest final LF");
const rows=seal.toString("utf8").trimEnd().split("\n").map(l=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);ok(!!m,"strict basename manifest row");return m;});
ok(rows.length===10,"ten author payloads");
ok(JSON.stringify(rows.map(x=>x[2]).sort())===JSON.stringify(authorNames.slice().sort()),"exact unique author payload selection");
ok(JSON.stringify(fs.readdirSync(D).sort())===JSON.stringify([...authorNames,"SHA256SUMS"].sort()),"eleven original physical files");
for(const [,digest,name]of rows)ok(file(D+"/"+name).key.sha256===digest,"author payload digest "+name);

const baselineNative=json(I+"/INPUT_KEYS_NATIVE.json");native(baselineNative,"independent baseline");
ok(baselineNative.result.exit_code===0,"baseline success");
const baseline=JSON.parse(baselineNative.result.output);
ok(baseline.scope==="FRESH15_INDEPENDENT_POSTREAD_DOCUMENTARY_KEYS"&&baseline.keys.length===32,"32 finite post-read documentary keys");
ok(new Set(baseline.keys.map(x=>x.path)).size===32,"unique independent key paths");
for(const k of baseline.keys)equalKey(k,"independent baseline");

const scope=json(D+"/SCOPE.json");
ok(scope.author==="/root/round211_functional_surgery_residual"&&scope.owned_directory===D,"author identity/scope");
ok(JSON.stringify(Object.keys(scope.counts).sort())===JSON.stringify(["new_literal_entrances","new_pilots","nominations","new_manuscripts","reserves","promotions"].sort()),"exact six denominator fields");
for(const [name,n]of Object.entries(scope.counts))ok(n===0,"zero "+name);
for(const k of["current_batch_indices_edited","previous_packets_edited","scientific_execution","runtime_or_host_or_private_or_input_or_observer_or_capture_execution","git_or_ssh","external_manuscript_upload","operational_authority","independent_review"])ok(scope[k]===false,"authority false "+k);
ok(scope.hold==="HOLD_EXTERNAL","external hold");
ok(scope.helper_boundary.includes("No helper native request/return objects")&&scope.helper_boundary.includes("no successful primary verification"),"unretained helper receives no native/primary credit");
ok(scope.inherited_orientation.closed_at_entry===56&&scope.inherited_orientation.root_intake_at_entry.includes("pending"),"historical entry orientation not current denominator");

const desk=json(D+"/DOCUMENTARY_REQUEST_RETURNS.json"),web=json(D+"/WEB_REQUEST_RETURNS.json");
ok(desk.records.length===35&&new Set(desk.records.map(x=>x.role)).size===35,"all 35 original shell records");
for(const x of desk.records){native(x,x.role);ok(x.request.workdir==="/root/autodl-tmp/symbolic_dynamics","documentary cwd "+x.role);ok(/^(sed -n |rg |test ! -e )/.test(x.request.cmd),"documentary request class "+x.role);}
const get=r=>desk.records.find(x=>x.role===r),exceptionRoles=[];
for(const x of desk.records){if(x.result.exit_code!==0||x.result.original_token_count>x.request.max_output_tokens)exceptionRoles.push(x.role);}
ok(JSON.stringify(exceptionRoles.sort())===JSON.stringify(["arxiv_script","discovery","old_ut_source","search_noncommutative_combinatorial","state"].sort()),"exact five exceptional original shell records");
ok(get("discovery").result.exit_code===2&&get("old_ut_source").result.exit_code===2&&get("arxiv_script").result.exit_code===1,"three failed shell calls retained");
for(const role of["discovery","state","search_noncommutative_combinatorial"])ok(get(role).result.original_token_count>get(role).request.max_output_tokens,"three original output ceilings retained "+role);
ok(get("absence").result.exit_code===0&&get("absence").result.output==="","original author absence call");
ok(web.records.length===6&&new Set(web.records.map(x=>x.role)).size===6,"all six original web calls");
for(const x of web.records){ok(typeof x.result==="string"&&x.request&&x.result.length>0,"original web return "+x.role);ok(Object.keys(x.request).every(k=>["search_query","open","find","screenshot","response_length"].includes(k)),"bounded primary web classes "+x.role);}
const wg=r=>web.records.find(x=>x.role===r);
ok((wg("primary01").result.match(/Internal Error/g)||[]).length===1,"one inaccessible paper route");
ok(wg("primary01").request.open.some(x=>x.ref_id.includes("citeseerx.ist.psu.edu")),"exact failed primary route selected");
ok((wg("primary05").result.match(/Internal Error/g)||[]).length===2,"both screenshot failures retained");
ok(JSON.stringify(wg("primary05").request.screenshot.map(x=>x.pageno))==="[1,2]"&&wg("primary05").result.includes("web screenshot is not enabled"),"no page-image PASS");
ok(wg("primary04").result.includes("Number of pages: 13")&&wg("primary04").result.includes("May 2, 2020"),"archived Graeffe metadata");
ok(wg("primary04").result.includes("Grs=Gr ∘Gs=Gs ∘Gr")&&wg("primary04").result.includes("15 Aug 2011"),"archived root-power composition/scalar metadata scope");

const inputNative=json(D+"/INPUT_KEYS_NATIVE.json");native(inputNative,"original postread keys");ok(inputNative.result.exit_code===0,"original key success");
const input=JSON.parse(inputNative.result.output);
ok(input.scope==="POSTREAD_DOCUMENTARY_KEYS_ONLY_NOT_PRE_READ_BRACKET"&&input.keys.length===20,"twenty original post-read pins, not read bracket");
for(const k of input.keys){
 equalKey(k,k.role);const r=get(k.role);native(r,"read pin "+k.role);
 const m=/^sed -n '1,([0-9]+)p' (.+)$/.exec(r.request.cmd);ok(!!m&&m[2]===k.path,"literal role read path "+k.role);
 const lines=file(k.path).b.toString("utf8").match(/[^\n]*\n|[^\n]+$/g)||[];
 pair(Buffer.from(lines.slice(0,Number(m[1])).join("")),Buffer.from(r.result.output),"original requested source lines "+k.role);
}
const authorCheck=json(D+"/CHECK_NATIVE.json");native(authorCheck,"author checker");native(authorCheck.source_read,"author checker source read");
ok(authorCheck.result.exit_code===0&&authorCheck.source_read.result.exit_code===0,"author documentary checker/source success");
pair(file(D+"/CHECK_DOCUMENTS.cjs").b,Buffer.from(authorCheck.source_read.result.output),"complete original checker read");
const authorOutput=JSON.parse(authorCheck.result.output);
ok(authorOutput.checks===374&&authorOutput.raw_pairs===20&&authorOutput.raw_paired_bytes===110768&&authorOutput.keys.length===29,"original 374 / 20 pair / 29 key result");
for(const k of authorOutput.keys)equalKey(k,"all original checker keys");
const replay=json(I+"/REPLAY_NATIVE.json");native(replay,"fresh documentary replay");
ok(replay.request.cmd==="node "+D+"/CHECK_DOCUMENTS.cjs"&&replay.result.exit_code===0,"fresh inspected documentary replay only");
pair(Buffer.from(replay.result.output),Buffer.from(authorCheck.result.output),"actual fresh author replay raw stdout");

const intake=json(I+"/INTAKE_READS_NATIVE.json");
ok(intake.records.length===32&&intake.orientation_records.length===5,"captured independent call census 32 plus 5");
for(const [ix,x]of [...intake.orientation_records,...intake.records].entries())native(x,"intake "+ix);
ok(intake.records.some(x=>x.request.cmd==="test ! -e "+I&&x.result.exit_code===0&&x.result.output===""),"actual intake absence before creation");
let semanticPairs=0;
for(const x of intake.records){
 const m=/^sed -n '1,([0-9]+)p' (.+)$/.exec(x.request.cmd);
 if(!m||x.result.exit_code!==0||!baseline.keys.some(k=>k.path===m[2]))continue;
 const lines=file(m[2]).b.toString("utf8").match(/[^\n]*\n|[^\n]+$/g)||[];
 pair(Buffer.from(lines.slice(0,Number(m[1])).join("")),Buffer.from(x.result.output),"actual independent read "+m[2]);semanticPairs++;
}
const primaryRead=intake.records.find(x=>x.request.cmd.includes('x.role==="primary04"'));
const screenshotRead=intake.records.find(x=>x.request.cmd.includes('x.role==="primary05"'));
ok(primaryRead&&screenshotRead,"actual archived-primary read calls retained");
pair(Buffer.from(primaryRead.result.output),Buffer.from(wg("primary04").result),"complete archived primary04 read");
pair(Buffer.from(screenshotRead.result.output),Buffer.from(wg("primary05").result),"complete archived screenshot-failure read");
ok(intake.records.filter(x=>x.result.exit_code!==0).length===1,"one captured independent wrong-path failure retained");
ok(intake.records.some(x=>x.request.cmd==="sed -n '1,280p' docs/research_state/ARTIFACT_CONTRACT.md"&&x.result.exit_code===2),"specific captured missing contract path");

const report=file(I+"/REPORT.md").b.toString("utf8"),census=json(I+"/CENSUS.json");
ok(report.includes("ACCEPT_ZERO_ENTRANCE_DOCUMENTARY_INTAKE_WITH_SCOPE_WARNING")&&report.includes("HOLD_EXTERNAL"),"bounded report verdict");
ok(census.new_entrances===0&&census.new_pilots===0&&census.nominations===0&&census.closed_increment===0,"independent denominator exactly zero");
ok(census.open_intake_blockers===0&&census.retained_scope_warnings.length===1&&!census.manuscript_review&&!census.operational_authority,"bounded warning, no paper review or authority");
process.stdout.write(JSON.stringify({scope:"FRESH15_INDEPENDENT_DOCUMENTARY_INTAKE_NOT_SCIENCE_OR_OPERATIONAL_AUTHORITY",checks,author_payloads:10,author_files:11,author_shell_records:35,author_web_records:6,original_exceptional_shell_records:exceptionRoles,original_failed_web_subrequests:3,independent_baseline_keys:32,author_postread_keys:20,author_checker_keys:29,independent_captured_calls:37,independent_semantic_read_raw_pairs:semanticPairs,raw_pairs:rawPairs,raw_paired_bytes:rawBytes,replay_stdout_bytes:Buffer.byteLength(replay.result.output),new_entrances:0,new_pilots:0,nominations:0,closed_increment:0,open_intake_blockers:0,retained_scope_warnings:1,keys:[...cache.values()].map(x=>x.key)},null,2)+"\n");
