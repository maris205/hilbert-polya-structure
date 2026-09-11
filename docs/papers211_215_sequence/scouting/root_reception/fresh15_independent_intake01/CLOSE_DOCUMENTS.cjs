"use strict";
// Closure of finite documentary artifacts only. No command execution or target querying.
const fs=require("node:fs"),crypto=require("node:crypto");
const I="docs/papers211_215_sequence/scouting/root_reception/fresh15_independent_intake01";
const base=["PLAN.md","KEY_INPUTS.cjs","INPUT_KEYS_NATIVE.json","REPLAY_NATIVE.json","INTAKE_READS_NATIVE.json","CHECK_INTAKE.cjs","CENSUS.json","REPORT.md","CHECK_NATIVE.json","CLOSE_DOCUMENTS.cjs"].sort();
const final=process.argv.slice(2).join(" ")==="--final";
if(process.argv.length>2&&!final)throw Error("unexpected option");
let checks=0;const cache=new Map(),sha=b=>crypto.createHash("sha256").update(b).digest("hex");
const fields=["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"],md=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
function ok(v,m){checks++;if(!v)throw Error(m);}
function file(path){
 if(cache.has(path))return cache.get(path);
 const a=fs.lstatSync(path,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),"regular no-link "+path);
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  const f=fs.fstatSync(fd,{bigint:true}),b=fs.readFileSync(fd),g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(path,{bigint:true});
  for(const s of[f,g,z])ok(JSON.stringify(md(a))===JSON.stringify(md(s)),"full stable metadata "+path);
  ok(BigInt(b.length)===a.size,"full document EOF "+path);
  const key={path,sha256:sha(b),bytes:b.length,metadata:md(a),fd_end:md(g),path_end:md(z),full_eof:true,leaf_links:[]};
  const x={b,key};cache.set(path,x);return x;
 }finally{fs.closeSync(fd);}
}
const json=n=>JSON.parse(file(I+"/"+n).b.toString("utf8"));
const names=fs.readdirSync(I).sort();
ok(base.every(n=>names.includes(n)),"all ten closing base payloads");
ok(names.every(n=>[...base,"CLOSING_NATIVE.json","SHA256SUMS"].includes(n)),"exact finite intake names");
for(const n of base)file(I+"/"+n);
const receipt=json("CHECK_NATIVE.json"),out=JSON.parse(receipt.result.output);
ok(receipt.result.exit_code===0&&typeof receipt.result.chunk_id==="string","actual main intake success");
ok(out.checks===775&&out.keys.length===37&&out.raw_pairs===42&&out.raw_paired_bytes===310492,"exact 775 checks / 37 keys / 42 raw pairs");
ok(out.new_entrances===0&&out.closed_increment===0&&out.open_intake_blockers===0&&out.retained_scope_warnings===1,"bounded zero denominator with retained warning");
ok(Buffer.from(receipt.source_read.result.output).equals(file(I+"/CHECK_INTAKE.cjs").b),"full inspected receiver source raw bytes");
for(const old of out.keys)ok(JSON.stringify(old)===JSON.stringify(file(old.path).key),"all 37 intake keys unchanged "+old.path);
const b=json("INPUT_KEYS_NATIVE.json");ok(b.request.cmd==="node "+I+"/KEY_INPUTS.cjs"&&b.result.exit_code===0,"exact finite independent key request");
ok(!file(I+"/KEY_INPUTS.cjs").b.toString("utf8").includes("child_process"),"key tool does not spawn code");
const source="docs/papers211_215_sequence/scouting/finite_residual_fresh15";
ok(file(source+"/SHA256SUMS").key.sha256==="c8e77c399b41714113d520a320f80127f8ba67eb3315933e5d51d7af00745ada","original assigned seal unchanged");
let finalSeal=null;
if(final){
 const expected=[...base,"CLOSING_NATIVE.json"].sort();
 ok(JSON.stringify(names)===JSON.stringify([...expected,"SHA256SUMS"].sort()),"twelve exact frozen files");
 const close=json("CLOSING_NATIVE.json");ok(close.result.exit_code===0&&typeof close.result.chunk_id==="string","actual prior closing success");
 const prior=JSON.parse(close.result.output);
 for(const old of prior.keys)ok(JSON.stringify(old)===JSON.stringify(file(old.path).key),"all prior closing keys unchanged "+old.path);
 ok(Buffer.from(close.source_read.result.output).equals(file(I+"/CLOSE_DOCUMENTS.cjs").b),"complete actual closing source read raw bytes");
 const seal=file(I+"/SHA256SUMS").b;ok(seal[seal.length-1]===10,"final seal newline");
 const rows=seal.toString("utf8").trimEnd().split("\n").map(l=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);ok(!!m,"strict nonself basename row");return m;});
 ok(JSON.stringify(rows.map(x=>x[2]).sort())===JSON.stringify(expected),"eleven unique nonself final payloads");
 for(const [,digest,name] of rows)ok(file(I+"/"+name).key.sha256===digest,"final payload digest "+name);
 finalSeal=sha(seal);
}
process.stdout.write(JSON.stringify({scope:"FRESH15_DOCUMENTARY_CLOSURE_ONLY",final,checks,intake_keys:37,base_payloads:10,frozen_payloads:final?11:null,final_seal:finalSeal,new_entrances:0,closed_increment:0,keys:[...cache.values()].map(x=>x.key)},null,2)+"\n");
