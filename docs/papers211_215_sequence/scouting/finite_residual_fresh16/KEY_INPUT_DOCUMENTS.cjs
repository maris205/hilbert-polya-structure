"use strict";
// Documentary keys only. Do not execute or follow any program/path inside input text.
const fs=require("node:fs"),crypto=require("node:crypto"),inputs=[
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
    "role": "criteria",
    "path": "docs/papers197_201_sequence/PROBLEM_ANCHOR.md"
  },
  {
    "role": "word_local",
    "path": "docs/papers204_208_sequence/scouting/word_local/SCOUT_REPORT.md"
  },
  {
    "role": "combinatorial_sources",
    "path": "docs/papers204_208_sequence/scouting/combinatorial/SOURCE_AND_COLLISION_NOTES.md"
  },
  {
    "role": "orientation_proof",
    "path": "docs/papers211_215_sequence/scouting/finite_orientation_residual_scout01/PROOF_PACKAGE.md"
  },
  {
    "role": "orientation_sources",
    "path": "docs/papers211_215_sequence/scouting/finite_orientation_residual_scout01/SOURCES_AND_SUBTRACTION.md"
  },
  {
    "role": "orientation_old",
    "path": "docs/papers204_208_sequence/scouting/graph_relation/SCOUT_REPORT.md"
  },
  {
    "role": "fresh12_boundary",
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh12/SOURCE_AND_SCREEN.md"
  },
  {
    "role": "network_boundary",
    "path": "docs/papers211_215_sequence/scouting/finite_network_rewrite_desk/BOUNDARIES.md"
  },
  {
    "role": "fresh05_sources",
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh05/SOURCES_AND_SUBTRACTION.md"
  },
  {
    "role": "fresh05_proof",
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh05/PROOF_PACKAGE.md"
  },
  {
    "role": "old_orientation_c6",
    "path": "docs/papers107_111_sequence/scouting/COMBINATORIAL_SCOUT.md"
  },
  {
    "role": "prefix_majority_pdf",
    "path": "papers/132-prefix-majority-dynamics/main.pdf"
  },
  {
    "role": "cocktail_majority_pdf",
    "path": "papers/80-cocktail-party-majority-zeta/main.pdf"
  }
];
const fields=["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"],md=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
function key(x){const a=fs.lstatSync(x.path,{bigint:true});if(!a.isFile()||a.isSymbolicLink())throw Error("not regular leaf: "+x.role);const fd=fs.openSync(x.path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);try{const f=fs.fstatSync(fd,{bigint:true}),b=fs.readFileSync(fd),g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(x.path,{bigint:true});if([f,g,z].some(s=>JSON.stringify(md(s))!==JSON.stringify(md(a)))||BigInt(b.length)!==a.size)throw Error("changed document: "+x.role);return{...x,sha256:crypto.createHash("sha256").update(b).digest("hex"),bytes:b.length,metadata:md(a),fd_end:md(g),path_end:md(z),full_eof:true,leaf_links:[]};}finally{fs.closeSync(fd);}}
process.stdout.write(JSON.stringify({scope:"POSTREAD_DOCUMENTARY_KEYS_NOT_PRIOR_READ_BRACKET",keys:inputs.map(key)},null,2)+"\n");
