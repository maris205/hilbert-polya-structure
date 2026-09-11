"use strict";
// Final documentary closing only; never inspect destinations within source/binding/request data.
const fs=require("node:fs"),crypto=require("node:crypto");
const D="docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01";
const OWN=[
  "BINDING.literal.txt",
  "BINDING.prepared.json",
  "BINDING.runtime_literal.json",
  "CAPTURE_REQUEST.disabled.json",
  "CHECK_DOCUMENTS.cjs",
  "CHECK_INITIAL_NATIVE.json",
  "CHECK_NATIVE.json",
  "CHECK_SOURCE_NATIVE.json",
  "CLOSE_DOCUMENTS.cjs",
  "CONSUMPTION_MAP.json",
  "EVIDENCE.md",
  "HANDOFF.md",
  "HANDOFF_READS_NATIVE.json",
  "INPUTS.sha256",
  "INPUT_KEYS_NATIVE.json",
  "KEY_INPUT_DOCUMENTS.cjs",
  "KEY_PREPARED_DOCUMENTS.cjs",
  "ORIENTATION_NATIVE.json",
  "PREPARATION.md",
  "PREPARED_KEYS_NATIVE.json",
  "PROPOSED_REQUEST.json",
  "PROSPECTIVE_BYTES.json",
  "READBACK_NATIVE.json",
  "READ_SCOPE.md",
  "SOURCE_DIFF_NATIVE.json",
  "SOURCE_READS_NATIVE.json",
  "TRANSFORMATION.json",
  "capture.proposed.sh.txt",
  "capture.sh",
  "observe.proposed.py.txt",
  "observe.py"
], INPUTS=[
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
const allow=new Set([...OWN.map(n=>D+"/"+n),...INPUTS.map(x=>x.path)]);
const fields=["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
let checks=0,pairs=0,pairedBytes=0;
function ok(v,msg){checks++;if(!v)throw Error(msg);}
const equal=(a,b,msg)=>ok(JSON.stringify(a)===JSON.stringify(b),msg);
const metadata=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const records=new Map(),bufs=new Map(),sha=b=>crypto.createHash("sha256").update(b).digest("hex");
function read(p){
 ok(allow.has(p),"exact document scope "+p);if(bufs.has(p))return bufs.get(p);
 const a=fs.lstatSync(p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),"regular no leaf link");
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
 const f=fs.fstatSync(fd,{bigint:true}),b=fs.readFileSync(fd),g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(p,{bigint:true});
 for(const x of [f,g,z])equal(metadata(a),metadata(x),"stable complete metadata");
 ok(BigInt(b.length)===a.size,"full EOF count");
 records.set(p,{path:p,sha256:sha(b),bytes:b.length,metadata:metadata(a),fd_end:metadata(g),path_end:metadata(z),leaf_links:[],full_eof:true});bufs.set(p,b);return b;
 }finally{fs.closeSync(fd);}
}
const own=n=>read(D+"/"+n),text=n=>own(n).toString("utf8"),json=n=>JSON.parse(text(n));
function raw(a,b,msg){
 a=Buffer.isBuffer(a)?a:Buffer.from(a,"utf8");b=Buffer.isBuffer(b)?b:Buffer.from(b,"utf8");ok(a.equals(b),msg);pairs++;pairedBytes+=a.length;
}
const actualNames=fs.readdirSync(D).filter(x=>x!=="CLOSING_NATIVE.json"&&x!=="SHA256SUMS").sort();
equal(actualNames,OWN,"entire owned preseal physical set (only closing/seal excluded)");
for(const name of OWN)read(D+"/"+name);
const finalNative=json("CHECK_NATIVE.json"),initialNative=json("CHECK_INITIAL_NATIVE.json");
ok(finalNative.result.exit_code===0&&initialNative.result.exit_code===0,"both actual checks succeeded");
const final=JSON.parse(finalNative.result.output),initial=JSON.parse(initialNative.result.output);
ok(final.checks===33405&&final.all_document_keys===39&&final.raw_pairs===23&&final.raw_paired_bytes===534754,"actual final documentary metrics");
ok(Buffer.byteLength(finalNative.result.output)===46843,"whole final check UTF-8 bytes");
ok(initial.keys.length===final.keys.length,"same initial/final scope");
for(let i=0;i<final.keys.length;i++){
 const k=final.keys[i];read(k.path);equal(records.get(k.path),k,"all 39 final-check keys unchanged");
 ok(initial.keys[i].path===k.path,"same check key order");
 if(k.path!==D+"/PREPARATION.md")equal(initial.keys[i],k,"all non-prose initial keys unchanged");
}
const reads=json("READBACK_NATIVE.json"),oldSentence="JSON data is parsed only by the separate Node documentary checker.\n",newSentence="JSON values are handled as documentary data by JavaScript; neither Python\nnor Bash source is parsed or executed.\n";
ok(reads.reads.length===7,"seven retained first readbacks");
for(const row of reads.reads){
 ok(row.result.exit_code===0,"readback success");
 if(row.name==="PREPARATION.md"){
 const oldKey=initial.keys.find(k=>k.path===row.path);
 ok(sha(Buffer.from(row.result.output,"utf8"))===oldKey.sha256&&Buffer.byteLength(row.result.output)===oldKey.bytes,"exact retained initial prose bytes");
 ok(row.result.output.split(oldSentence).length===2,"unique precise prose clarification");
 raw(row.result.output.replace(oldSentence,newSentence),own(row.name),"only exact documented prose clarification");
 }else raw(row.result.output,own(row.name),"whole final raw readback "+row.name);
}
ok(reads.final_preparation_read.result.exit_code===0,"final preparation read success");
raw(reads.final_preparation_read.result.output,own("PREPARATION.md"),"complete final preparation raw readback");
const checker=json("CHECK_SOURCE_NATIVE.json");
ok(checker.draft_read.result.exit_code===0&&checker.final_read.result.exit_code===0,"checker source readbacks retained");
const bad='ok(b.files.length===69&&b.module_names.length===62,"finite exact cardinalities");\nok(b.required_module_names.early.every(n=>b.module_names.includes(n)),"early required subset");';
const good='ok(b.files.length===69&&b.module_names.early.length===23&&b.module_names.helper.length===62&&b.module_names.closing.length===62,"finite exact phase cardinalities");\nfor(const phase of ["early","helper","closing"])ok(b.required_module_names[phase].every(n=>b.module_names[phase].includes(n)),"required phase subset "+phase);';
ok(checker.draft_read.result.output.split(bad).length===2,"one draft module_names check block");
raw(checker.draft_read.result.output.replace(bad,good),own("CHECK_DOCUMENTS.cjs"),"exact never-executed draft correction only");
raw(checker.final_read.result.output,own("CHECK_DOCUMENTS.cjs"),"whole final checker source readback");
const handoffReads=json("HANDOFF_READS_NATIVE.json").reads;
ok(handoffReads.length===2,"two handoff reads");
for(const r of handoffReads){ok(r.result.exit_code===0,"handoff read exit");raw(r.result.output,own(r.name),"complete handoff/evidence native read");}
const old=json("INPUT_KEYS_NATIVE.json");ok(old.result.exit_code===0,"input baseline success");
const oldkeys=JSON.parse(old.result.output).keys;
for(const k of oldkeys){read(k.path);equal(records.get(k.path),Object.fromEntries(Object.entries(k).filter(([n])=>n!=="role")),"all 16 input baseline keys unchanged");}
const core=JSON.parse(json("PREPARED_KEYS_NATIVE.json").result.output).keys;
for(const k of core)equal(records.get(k.path),Object.fromEntries(Object.entries(k).filter(([n])=>n!=="role")),"all eleven core baseline keys unchanged");
const manifest=json("PROSPECTIVE_BYTES.json");
for(const k of manifest.current_documentary_artifacts){
 const r=records.get(D+"/"+k.path);ok(r.bytes===k.bytes&&r.sha256===k.sha256,"every core external byte commitment");
}
const baselineScope={selected_predecessors:16,final_check_keys:39,unchanged_core_artifacts:11,owned_preclosing_payloads:OWN.length};
const ownkeys=OWN.map(n=>records.get(D+"/"+n)), allkeys=[...records.values()];
process.stdout.write(JSON.stringify({scope:"AUTHOR_FINAL_DOCUMENTARY_CLOSING_ONLY_NO_RUNTIME_OR_INDEPENDENT_ACCEPTANCE",checks,raw_pairs:pairs,raw_paired_bytes:pairedBytes,baseline_scope:baselineScope,keys:allkeys,owned_payload_bytes:ownkeys.reduce((s,k)=>s+k.bytes,0),owned_preclosing_manifest:ownkeys.map(k=>({name:k.path.slice(D.length+1),bytes:k.bytes,sha256:k.sha256})),nonself_rule:"CLOSING_NATIVE.json and SHA256SUMS are excluded here to avoid recursive self-records; the subsequent complete physical SHA256SUMS includes this native return and all other payloads, excluding only itself."},null,2)+"\n");
