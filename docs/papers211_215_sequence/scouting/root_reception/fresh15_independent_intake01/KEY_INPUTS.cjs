"use strict";
// Finite documentary inventory only: never execute imported programs or probe targets.
const fs = require("node:fs"), crypto = require("node:crypto");
const D = "docs/papers211_215_sequence/scouting/finite_residual_fresh15";
const names = ["CHECK_DOCUMENTS.cjs","CHECK_NATIVE.json","DOCUMENTARY_REQUEST_RETURNS.json","HANDOFF.md","INPUT_KEYS_NATIVE.json","KEY_INPUT_DOCUMENTS.cjs","PROOF_PACKAGE.md","SCOPE.json","SOURCES_AND_LIMITS.md","WEB_REQUEST_RETURNS.json","SHA256SUMS"];
const extra = ["docs/papers204_208_sequence/ARTIFACT_CONTRACT.md"];
const fields = ["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
const md = s => Object.fromEntries(fields.map(k => [k,String(s[k])]));
function key(path) {
 const a = fs.lstatSync(path,{bigint:true});
 if (!a.isFile() || a.isSymbolicLink()) throw Error("not regular no-link documentary leaf: "+path);
 const fd = fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try {
  const b0=fs.fstatSync(fd,{bigint:true}), b=fs.readFileSync(fd), b1=fs.fstatSync(fd,{bigint:true}), z=fs.lstatSync(path,{bigint:true});
  if ([b0,b1,z].some(x=>JSON.stringify(md(x))!==JSON.stringify(md(a))) || BigInt(b.length)!==a.size) throw Error("unstable or incomplete document: "+path);
  return {path,sha256:crypto.createHash("sha256").update(b).digest("hex"),bytes:b.length,metadata:md(a),fd_end:md(b1),path_end:md(z),full_eof:true,leaf_links:[]};
 } finally {fs.closeSync(fd);}
}
const original = JSON.parse(JSON.parse(fs.readFileSync(D+"/INPUT_KEYS_NATIVE.json","utf8")).result.output).keys;
// Inputs are literal finite documentary paths, not paths decoded from host/observer logs.
if(original.length!==20 || original.some(x=>typeof x.path!=="string" || !/^(docs\/|\/root\/autodl-tmp\/(symbolic_dynamics\/\.agents\/skills\/|\.codex\/skills\/))/.test(x.path))) throw Error("unexpected original documentary selection");
const paths=[...new Set([...names.map(n=>D+"/"+n),...original.map(x=>x.path),...extra])];
process.stdout.write(JSON.stringify({scope:"FRESH15_INDEPENDENT_POSTREAD_DOCUMENTARY_KEYS",keys:paths.map(key)},null,2)+"\n");
