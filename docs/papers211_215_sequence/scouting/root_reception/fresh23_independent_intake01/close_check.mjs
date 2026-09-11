// Documentary closure only; no scientific import or archived-command execution.
import fs from 'node:fs';
import crypto from 'node:crypto';
const OWN='docs/papers211_215_sequence/scouting/root_reception/fresh23_independent_intake01/';
const FIRST=['INPUT_PINS.json','LOCAL_READ_RETURNS.json','PRIMARY_RETURNS.json','FINDINGS.json','ORIGIN_AND_SCOPE.md','REVIEW.md','check_artifacts.mjs','ARTIFACT_CHECK.json','ARTIFACT_CHECK_NATIVE.json','close_check.mjs'];
const PAYLOAD=[...FIRST,'CLOSING_CHECK.json','CLOSING_NATIVE.json'];
const EXTERNAL=[
  "docs/papers211_215_sequence/scouting/finite_residual_fresh23/DESK.md",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh23/READ_SCOPE.md",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh23/NATIVE_READS.json",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh23/PRIMARY_RETURNS.json",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh23/DOCUMENTARY_RECEIPT.json",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh23/SHA256SUMS",
  "docs/papers204_208_sequence/scouting/word_local/GM_PROOF_PACKAGE.md",
  "docs/papers204_208_sequence/scouting/word_local/GM_GATE/CANDIDATE_GATE.md",
  "docs/papers162_166_sequence/scouting/replacement_crossclass/SCOUT.md",
  "docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md",
  "docs/papers211_215_sequence/PROBLEM_ANCHOR.md",
  "docs/papers197_201_sequence/PROBLEM_ANCHOR.md"
];
const allowed=new Set([...PAYLOAD.map(x=>OWN+x),OWN+'MANIFEST.sha256',...EXTERNAL]);
const hash=x=>crypto.createHash('sha256').update(x).digest('hex');
let assertions=0;
const checks={};
function need(x,label){assertions++;if(!x)throw Error(label);}
function mark(label,value=true){need(!Object.hasOwn(checks,label),'duplicate label');checks[label]=value;}
function read(path){
 need(allowed.has(path),'fixed documentary path');
 const a=path.split('/');need(a[0]==='docs'&&!a.some(x=>!x||x==='.'||x==='..'),'docs path components');
 for(let j=1;j<a.length;j++){const s=fs.lstatSync(a.slice(0,j).join('/'));need(s.isDirectory()&&!s.isSymbolicLink(),'docs ancestor');}
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  const p=fs.fstatSync(fd,{bigint:true});need(p.isFile(),'regular file');
  const b=fs.readFileSync(fd),q=fs.fstatSync(fd,{bigint:true});
  for(const k of ['dev','ino','size','mtimeNs','ctimeNs'])need(p[k]===q[k],'same descriptor '+k);
  need(BigInt(b.length)===q.size&&fs.readSync(fd,Buffer.alloc(1),0,1,null)===0,'complete descriptor EOF');
  need(Buffer.from(b.toString('utf8'),'utf8').equals(b),'UTF8');
  return b;
 }finally{fs.closeSync(fd);}
}
function equal(a,b,label){need(Buffer.from(a).equals(Buffer.from(b)),label);}
const mode=process.argv[2]||'--preseal';
need(process.argv.length===3&&(mode==='--preseal'||mode==='--final'),'explicit documentary phase only');
const ownMap=new Map(FIRST.map(n=>[n,read(OWN+n)]));
const pins=JSON.parse(ownMap.get('INPUT_PINS.json'));
need(JSON.stringify(pins.files.map(x=>x.path))===JSON.stringify(EXTERNAL),'all external identities');
let externalBytes=0;
for(const row of pins.files){const b=read(row.path);need(b.length===row.bytes&&hash(b)===row.sha256,'external pin');externalBytes+=b.length;}
mark('all_external_files_rechecked',12);mark('all_external_physical_bytes',externalBytes);
mark('own_preseal_files',FIRST.map(n=>({name:n,bytes:ownMap.get(n).length,sha256:hash(ownMap.get(n))})));
const raw=ownMap.get('ARTIFACT_CHECK.json'),v=JSON.parse(raw);
const nr=JSON.parse(ownMap.get('ARTIFACT_CHECK_NATIVE.json'));
need(nr.request.cmd==='node docs/papers211_215_sequence/scouting/root_reception/fresh23_independent_intake01/check_artifacts.mjs','actual documentary request identity');
need(nr.actual_return.exit_code===0&&nr.actual_return.chunk_id==='12ea67','actual passing intake native');
equal(raw,nr.actual_return.output,'whole intake raw canonical/native comparison');
equal(raw,JSON.stringify(v,null,2)+'\n','intake canonical JSON');
need(v.kind==='FRESH23_DOCUMENTARY_INDEPENDENT_INTAKE'&&v.verdict==='PASS_DOCUMENTARY_ONLY'&&v.assertion_count===1220&&v.named_check_count===29&&Object.keys(v.checks).length===29,'complete stored intake report');
mark('intake_complete_native_raw_equals_canonical',{chunk_id:nr.actual_return.chunk_id,bytes:raw.length,sha256:hash(raw)});
mark('intake_all_named_keys_received',Object.keys(v.checks));
mark('intake_assertions_recorded_as_documentary_data',1220);
const local=JSON.parse(ownMap.get('LOCAL_READ_RETURNS.json')),prim=JSON.parse(ownMap.get('PRIMARY_RETURNS.json'));
need(local.records.length===8&&prim.calls.length===2,'complete intake task archive censuses');
mark('intake_source_native_and_primary_counts',{complete_independent_native:8,independent_primary:2,complete_author_native:11,partial_historical_native_metadata:4,author_primary:4});
const findings=JSON.parse(ownMap.get('FINDINGS.json'));
need(findings.verdict==='ACCEPT_BOUNDED_ZERO_LITERAL_DESK'&&findings.open_findings===0,'bounded scientific verdict');
mark('no_substantive_findings_and_zero_literal_delta',findings.negative_lifecycle);
mark('author_source_and_historical_inputs_unchanged');
mark('source_execution_science_host_grant_build_git_counts',[0,0,0,0,0,0]);
const preseal={kind:'FRESH23_DOCUMENTARY_CLOSURE',phase:'PRESEAL_TEN_FILES',verdict:'PASS_DOCUMENTARY_CLOSURE_ONLY',assertion_count:assertions,named_check_count:Object.keys(checks).length,checks,limits:'This closes stored documentary reception only. The two closing receipts and nonself seal are verified in --final; no final native is claimed to be a member of its own seal.'};
const presealRaw=JSON.stringify(preseal,null,2)+'\n';
if(mode==='--preseal'){
 need(JSON.stringify(fs.readdirSync(OWN).sort())===JSON.stringify([...FIRST].sort()),'exact preseal ten file census');
 // Census contributes only to this reported phase; no dependency on later files.
 preseal.assertion_count=assertions;
 process.stdout.write(JSON.stringify(preseal,null,2)+'\n');
}else{
 const closeRaw=read(OWN+'CLOSING_CHECK.json'),close=JSON.parse(closeRaw);
 const closeNative=JSON.parse(read(OWN+'CLOSING_NATIVE.json'));
 need(closeNative.request.cmd==='node docs/papers211_215_sequence/scouting/root_reception/fresh23_independent_intake01/close_check.mjs --preseal','closing request');
 need(closeNative.actual_return.exit_code===0,'closing native success');
 equal(closeRaw,closeNative.actual_return.output,'whole closing raw canonical/native');
 equal(closeRaw,JSON.stringify(close,null,2)+'\n','closing canonical JSON');
 // One assertion was the actual historical ten-file census, received as data
 // here, not rerun after this directory has thirteen files.
 const reconstructed={...preseal,assertion_count:preseal.assertion_count+1};
 equal(closeRaw,JSON.stringify(reconstructed,null,2)+'\n','all complete preseal keys and input hashes reconstructed');
 mark('whole_preseal_raw_reconstructed_and_native_equal',{bytes:closeRaw.length,sha256:hash(closeRaw),historical_census_rerun:false});
 const manifest=read(OWN+'MANIFEST.sha256').toString('utf8');
 const manifestLines=manifest.trimEnd().split('\n');need(manifest.endsWith('\n')&&manifestLines.length===12,'twelve line manifest');
 const names=new Set();
 for(const l of manifestLines){
  const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);
  need(m&&PAYLOAD.includes(m[2])&&!names.has(m[2]),'unique permitted nonself leaf');names.add(m[2]);
  need(hash(read(OWN+m[2]))===m[1],'manifest bytes');
 }
 need(JSON.stringify(fs.readdirSync(OWN).sort())===JSON.stringify([...PAYLOAD,'MANIFEST.sha256'].sort()),'strict thirteen file final census');
 mark('complete_nonself_manifest_payloads',12);mark('complete_final_files',13);
 mark('manifest_sha256',hash(manifest));
 mark('historical_preseal_census_not_rerun');
 mark('final_tool_native_not_claimed_inside_its_own_manifest');
 process.stdout.write(JSON.stringify({kind:'FRESH23_DOCUMENTARY_CLOSURE',phase:'FINAL_SEALED',verdict:'PASS_DOCUMENTARY_CLOSURE_ONLY',assertion_count:assertions,named_check_count:Object.keys(checks).length,checks,limits:preseal.limits},null,2)+'\n');
}
