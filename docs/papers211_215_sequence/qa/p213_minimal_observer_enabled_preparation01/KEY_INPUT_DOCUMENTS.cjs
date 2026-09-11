"use strict";
// DOCUMENTARY INPUTS ONLY. Never inspect any path string inside those JSON documents.
const fs = require("node:fs"), crypto = require("node:crypto");
const inputs = [
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
const fields = ["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
const stat = s => Object.fromEntries(fields.map(k=>[k,String(s[k])]));
function key(path) {
  const a = fs.lstatSync(path,{bigint:true});
  if (!a.isFile() || a.isSymbolicLink()) throw Error("document must be regular no leaf link: "+path);
  const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try {
    const f=fs.fstatSync(fd,{bigint:true}), bytes=fs.readFileSync(fd), g=fs.fstatSync(fd,{bigint:true});
    const z=fs.lstatSync(path,{bigint:true});
    if ([f,g,z].some(s=>JSON.stringify(stat(s))!==JSON.stringify(stat(a))) || BigInt(bytes.length)!==a.size) throw Error("document changed: "+path);
    return {path,sha256:crypto.createHash("sha256").update(bytes).digest("hex"),bytes:bytes.length,metadata:stat(a),fd_end:stat(g),path_end:stat(z),leaf_links:[],full_eof:true};
  } finally {fs.closeSync(fd);}
}
process.stdout.write(JSON.stringify({scope:"P213_ENABLED_PREPARATION_DOCUMENTARY_INPUT_KEYS_ONLY",keys:inputs.map(x=>({role:x.role,...key(x.path)}))},null,2)+"\n");
