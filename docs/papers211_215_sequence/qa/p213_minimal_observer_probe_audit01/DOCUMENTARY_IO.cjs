"use strict";
// Fixed file capability set: decoded runtime module/map/file paths are never opened.
const fs=require("node:fs"),crypto=require("node:crypto");
const Q="docs/papers211_215_sequence/qa/",ROOT="/root/autodl-tmp/symbolic_dynamics/";
const packages={
 p213_minimal_observer_probe_root01:["SHA256SUMS","CLOSING_NATIVE.json","CLOSE.cjs","RAW_INPUTS.sha256","HANDOFF.md","PRECISION_LIMIT.md","LOSSLESS_NATIVE.json","CHECK_RAW_INTEGERS.cjs","INITIAL_RAW_RECEIVE_NATIVE.json","OBSERVATION_NATIVE.json","ATTEMPT_COMMITTED.json","MATERIALIZATION_STRICT_NATIVE.json","PREFLIGHT_NATIVE.json","GRANT.json"],
 p213_minimal_observer_materialization01:["SHA256SUMS","RECEIPT.md","SOURCE_SEAL_NATIVE.json","BYTE_MATCH_NATIVE.json","ALLOCATION_NATIVE.json","PRECONDITIONS_NATIVE.json","DECISION.md"],
 p213_minimal_observer_enabled_root01:["SHA256SUMS","CLOSING_NATIVE.json","CLOSE.cjs","RECEPTION.md","CHECK_NATIVE.json","CHECK_ROOT.cjs","DISPLAY_LIMITS_NATIVE.json","ROOT_REPLAYS_NATIVE.json","ROOT_READS_NATIVE.json"],
 p213_minimal_observer_enabled01:["SHA256SUMS","observe.py","capture.sh"],
 p213_minimal_observer_enabled_preparation01:["SHA256SUMS","PREPARATION.md","BINDING.runtime_literal.json","PROPOSED_REQUEST.json","observe.proposed.py.txt","capture.proposed.sh.txt"],
 p213_minimal_observer_enabled_preparation_audit01:["SHA256SUMS","REPORT.md","FINDINGS.json","ACCEPTANCE.json"],
 p213_minimal_observer_source_delta01:["CONTRACT.md","BINDING_FORMAT.md","COLLECTION_DELTA.md"]
};
const documents=Object.entries(packages).flatMap(([p,names])=>names.map(n=>Q+p+"/"+n)).concat([".agents/skills/symbolic-dynamics-research/SKILL.md","docs/research_state/WORKFLOW.md","docs/papers204_208_sequence/ARTIFACT_CONTRACT.md"]);
const capture=Q+"p213_minimal_observer_probe01",rawFiles=[capture+"/stdout.bin",capture+"/stderr.bin"];
const permitted=new Set([...documents,...rawFiles]);
const fields=["dev","ino","mode","nlink","uid","gid","rdev","size","blksize","blocks","mtimeNs","ctimeNs","birthtimeNs"];
const md=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
function relative(p){if(p.startsWith(ROOT))p=p.slice(ROOT.length);return p;}
function openDocument(path){
 path=relative(path);if(!permitted.has(path))throw Error("path outside finite documentary/raw capability set");
 const before=fs.lstatSync(path,{bigint:true});if(!before.isFile()||before.isSymbolicLink())throw Error("nonregular/link documentary leaf");
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  const start=fs.fstatSync(fd,{bigint:true}),bytes=fs.readFileSync(fd),end=fs.fstatSync(fd,{bigint:true}),after=fs.lstatSync(path,{bigint:true});
  if([start,end,after].some(s=>JSON.stringify(md(s))!==JSON.stringify(md(before)))||BigInt(bytes.length)!==before.size)throw Error("unstable/incomplete documentary bytes");
  return {bytes,key:{path,sha256:sha(bytes),bytes:bytes.length,metadata:md(before),fd_before:md(start),fd_after:md(end),path_end:md(after),full_eof:true,leaf_links:[]}};
 }finally{fs.closeSync(fd);}
}
function captureDirectory(){
 const a=fs.lstatSync(capture,{bigint:true});if(!a.isDirectory()||a.isSymbolicLink())throw Error("invalid exact capture directory");
 const inventory=fs.readdirSync(capture).sort(),z=fs.lstatSync(capture,{bigint:true});
 if(JSON.stringify(md(a))!==JSON.stringify(md(z)))throw Error("changed capture directory metadata");
 if(a.mode!==16832n||a.uid!==0n||a.gid!==0n||JSON.stringify(inventory)!=='["stderr.bin","stdout.bin"]')throw Error("capture scope/owner/mode");
 return {path:capture,metadata:md(a),path_end:md(z),inventory};
}
module.exports={packages,documents,rawFiles,capture,fields,md,sha,relative,openDocument,captureDirectory};
