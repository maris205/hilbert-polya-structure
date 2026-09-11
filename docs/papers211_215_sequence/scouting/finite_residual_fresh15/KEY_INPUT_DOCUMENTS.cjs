"use strict";
// Documentary keys only; no runtime, scientific, private, or embedded path query.
const fs=require("node:fs"),crypto=require("node:crypto");
const inputs=[
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
];
const fields=["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
const md=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
function key(x){
 const a=fs.lstatSync(x.path,{bigint:true});
 if(!a.isFile()||a.isSymbolicLink())throw Error("not regular no-link document: "+x.role);
 const fd=fs.openSync(x.path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  const f=fs.fstatSync(fd,{bigint:true}),b=fs.readFileSync(fd),g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(x.path,{bigint:true});
  if([f,g,z].some(s=>JSON.stringify(md(s))!==JSON.stringify(md(a)))||BigInt(b.length)!==a.size)throw Error("document changed: "+x.role);
  return {...x,sha256:crypto.createHash("sha256").update(b).digest("hex"),bytes:b.length,metadata:md(a),fd_end:md(g),path_end:md(z),full_eof:true,leaf_links:[]};
 }finally{fs.closeSync(fd);}
}
process.stdout.write(JSON.stringify({scope:"POSTREAD_DOCUMENTARY_KEYS_ONLY_NOT_PRE_READ_BRACKET",keys:inputs.map(key)},null,2)+"\n");
