"use strict";
// DOCUMENTARY INPUTS ONLY. Never inspect any path string inside those JSON documents.
const fs = require("node:fs"), crypto = require("node:crypto");
const inputs = [
  {
    "role": "observe.py",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/observe.py"
  },
  {
    "role": "capture.sh",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/capture.sh"
  },
  {
    "role": "observe.proposed.py.txt",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/observe.proposed.py.txt"
  },
  {
    "role": "capture.proposed.sh.txt",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/capture.proposed.sh.txt"
  },
  {
    "role": "BINDING.prepared.json",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/BINDING.prepared.json"
  },
  {
    "role": "BINDING.runtime_literal.json",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/BINDING.runtime_literal.json"
  },
  {
    "role": "BINDING.literal.txt",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/BINDING.literal.txt"
  },
  {
    "role": "CAPTURE_REQUEST.disabled.json",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/CAPTURE_REQUEST.disabled.json"
  },
  {
    "role": "PROPOSED_REQUEST.json",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/PROPOSED_REQUEST.json"
  },
  {
    "role": "TRANSFORMATION.json",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/TRANSFORMATION.json"
  },
  {
    "role": "CONSUMPTION_MAP.json",
    "path": "docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/CONSUMPTION_MAP.json"
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
process.stdout.write(JSON.stringify({scope:"P213_PREPARED_AND_PROSPECTIVE_TEXT_DOCUMENT_KEYS_ONLY",keys:inputs.map(x=>({role:x.role,...key(x.path)}))},null,2)+"\n");
