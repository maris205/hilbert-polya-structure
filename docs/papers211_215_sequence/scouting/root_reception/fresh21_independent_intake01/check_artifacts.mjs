// Reviewer-authored Fresh21 fixed-document DATA audit. Read-only.
// Reuses this reviewer's prior fixed-file audit mechanics, not author code.
// No author command, scientific source, subprocess, network or write occurs.
import fs from 'node:fs';
import crypto from 'node:crypto';
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const OWN='docs/papers211_215_sequence/scouting/root_reception/fresh21_independent_intake01/';
const SOURCE='docs/papers211_215_sequence/scouting/finite_residual_fresh21/';
const EXPECTED=[
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/CLOSURE_TOOL_RETURNS.json",
    "bytes": 8246,
    "sha256": "b06166ccaf730bb2cb55ccdd50462345e7cd7f7501242ddad37b30f850dabf2b"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/HANDOFF.md",
    "bytes": 3244,
    "sha256": "0ac1c4cef32462f5caa2b9d0951f7329f8f86e581e1808e3da3d8ea2dacb586d"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/INPUT_PINS.sha256",
    "bytes": 948,
    "sha256": "7627e7020539923140323156967dab50c4e10913a5928a4d60074dcca60fcc65"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/INTEGRATION_TOOL_RETURNS.json",
    "bytes": 79399,
    "sha256": "9dc458e54c4d9c90a04d94d9d3dbbf3ac55404b80dc6aae5c7aeea88d23b3e85"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/LOCAL_TOOL_RETURNS.json",
    "bytes": 197268,
    "sha256": "c1e87191027bb13f851edf3c75a23707f64d59ab675a4c668881d2d5ed5be489"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/PLAN.md",
    "bytes": 3939,
    "sha256": "da549eef81e3e7d9741de96d79e24c5f4fc2f22914475dbdb792b01b04f335b4"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/PROOF_PACKAGE.md",
    "bytes": 9065,
    "sha256": "64ee7dd25f98ac4a232338b394c8399e7a99ad24656c063d87a95eb469eb471d"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/SOURCE_READS.md",
    "bytes": 7889,
    "sha256": "1480220bf7c3cdbbd87401aaccd1daea5ad682692900a3e6ba49b9a8bc872843"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/SOURCE_TOOL_RETURNS.json",
    "bytes": 161950,
    "sha256": "fbd01e0db812b057b9c0a7026a11170aab268f60c012bf9f451d8f9f66e05c82"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/HANDOFF.md",
    "bytes": 4648,
    "sha256": "648cb18d892433868610156966f1e85c971e4892c8aedb270a153cffaa71c8f7"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/PROOF_PACKAGE.md",
    "bytes": 3983,
    "sha256": "dd5e26362bfafacae07731b4bd133c926fcd001589600626e6a6a079d8abd025"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/READ01_MISSING_ORIGINAL.md",
    "bytes": 1401,
    "sha256": "c03602f623a9899ba564f270984a8622d8bfd064c5bad8844e1f015683f25d56"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read02.json",
    "bytes": 10041,
    "sha256": "f4f13b7257d6e4f7d0b08fc12130f13fd95e0c309819d880a18516b5906ff713"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read03.json",
    "bytes": 4648,
    "sha256": "16d7a52752f431ede9a3fb9ec5774de1fffb665f8e7445a8415c6b0f60fb1f95"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read04.json",
    "bytes": 42723,
    "sha256": "0b353dcd8bfe59809bdb7080d33cdb0d23cdf4f137e3f88634ee620fbd734912"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read05.json",
    "bytes": 31084,
    "sha256": "80f1d773a52d1088dd10b68445aca560eab7e062d50bcf530c93881193e79f2d"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read06.json",
    "bytes": 26900,
    "sha256": "ce70939771ee359127fc0ce6cac609fba021bdc57ed7b336eacfa9f6bd5c4d0e"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read07.json",
    "bytes": 17198,
    "sha256": "346f418cf10de87cb4390da228dfe8b9d94f940276b313033516e222c4436249"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read08.json",
    "bytes": 23971,
    "sha256": "22f7a7fb0df734d1020e3efb5aa91afe76ede7124f8a798db84363714256a8a2"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read09.json",
    "bytes": 25335,
    "sha256": "8eaa3a243326e0f200d9af28223a169afc6a53882bd6e7669e833847a4725015"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read10.json",
    "bytes": 7835,
    "sha256": "490cc8b2599aaf9e53d6794c8fe45fdb7367cb411fe2d734c8f567098f1a9a18"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/read11_closing.json",
    "bytes": 5175,
    "sha256": "a0b38c3617411fb060f55d762f87f7cc52d09ce965f9d48405feb083bcdace5e"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/web01.json",
    "bytes": 398,
    "sha256": "ff6e0d8c6ac39147fc77d24b2718d2f210a520805e1249a4b719b6223a46772d"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/web02.json",
    "bytes": 19160,
    "sha256": "fb1f1f0a30c545e28707f0464875c8ebf2e2a7fca0291a776d72446aff83620a"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/web03.json",
    "bytes": 23632,
    "sha256": "3b6c5fcea94faff1bb16f29e7b8e86a4d75469440b9e7309931ee398938d5afe"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/web04.json",
    "bytes": 9528,
    "sha256": "8bd04fcf413afa8100b6bd4e82870bf99796b315ecc9d598f411667288551040"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/side_lane/raw/web05.json",
    "bytes": 11217,
    "sha256": "6e53f19fd3c8501514a0cf62dcc079bc988541bd9c31a0f27b4fdc7878f50f61"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh21/MANIFEST.sha256",
    "bytes": 2435,
    "sha256": "d05381e309a7ef2a274f8b564df78a03f95d1762f2a3053f5f89acbb451599db"
  },
  {
    "path": "docs/papers204_208_sequence/scouting/finite_algebra_ninth/PROOF_AND_ADAPTER_NOTES.md",
    "bytes": 15627,
    "sha256": "e420c05e2c7c0727f9485636c9e50d8090160af432ceba5216a24517ad49e519"
  },
  {
    "path": "docs/papers204_208_sequence/scouting/finite_algebra_ninth/INTAKE.md",
    "bytes": 4784,
    "sha256": "2fb12a4c343e71f382eeede3069f45fd878226331a971d112419674874b07719"
  },
  {
    "path": "docs/papers204_208_sequence/scouting/finite_systems_fifteenth/PROOF_AND_DISPOSITION.md",
    "bytes": 10025,
    "sha256": "98a5c1116ba6b4ed0e181744447e9d413d3fab8a99c9f0bd94728af014b173f0"
  },
  {
    "path": "docs/papers204_208_sequence/scouting/finite_systems_fifteenth/INTAKE.md",
    "bytes": 8482,
    "sha256": "eccf1ba1b6ebd86a62346c894681ca8a6a78976048bed50f928ad2256e75169d"
  },
  {
    "path": "docs/papers204_208_sequence/scouting/order_geometry_tenth_desk/SOURCE_BOUNDARY.md",
    "bytes": 15182,
    "sha256": "df3cf24965b0fb08bd8009eaea96063af4ed23386e2ecc2e93b18ff349970bd2"
  },
  {
    "path": "docs/papers211_215_sequence/PROBLEM_ANCHOR.md",
    "bytes": 3168,
    "sha256": "8d85811edd394b41802e71ada676d77ae9d8d9211251b9df4998cb15718f665b"
  },
  {
    "path": "docs/papers197_201_sequence/PROBLEM_ANCHOR.md",
    "bytes": 2463,
    "sha256": "4c02a736cb9ebca544b05ca94a9bf621b244780f95a4f5651a0a62600003f91e"
  },
  {
    "path": "docs/papers204_208_sequence/scouting/order_geometry_tenth_desk/PROOF_AND_ADAPTER.md",
    "bytes": 20281,
    "sha256": "181f18e946fb2d526af67addb1f06e8bfff257d82ada054ba90069f9176daeb9"
  }
];
const NAMES=["CLOSURE_TOOL_RETURNS.json","HANDOFF.md","INPUT_PINS.sha256","INTEGRATION_TOOL_RETURNS.json","LOCAL_TOOL_RETURNS.json","PLAN.md","PROOF_PACKAGE.md","SOURCE_READS.md","SOURCE_TOOL_RETURNS.json","side_lane/HANDOFF.md","side_lane/PROOF_PACKAGE.md","side_lane/READ01_MISSING_ORIGINAL.md","side_lane/raw/read02.json","side_lane/raw/read03.json","side_lane/raw/read04.json","side_lane/raw/read05.json","side_lane/raw/read06.json","side_lane/raw/read07.json","side_lane/raw/read08.json","side_lane/raw/read09.json","side_lane/raw/read10.json","side_lane/raw/read11_closing.json","side_lane/raw/web01.json","side_lane/raw/web02.json","side_lane/raw/web03.json","side_lane/raw/web04.json","side_lane/raw/web05.json","MANIFEST.sha256"];
const OLD=["docs/papers204_208_sequence/scouting/finite_algebra_ninth/PROOF_AND_ADAPTER_NOTES.md","docs/papers204_208_sequence/scouting/finite_algebra_ninth/INTAKE.md","docs/papers204_208_sequence/scouting/finite_systems_fifteenth/PROOF_AND_DISPOSITION.md","docs/papers204_208_sequence/scouting/finite_systems_fifteenth/INTAKE.md","docs/papers204_208_sequence/scouting/order_geometry_tenth_desk/SOURCE_BOUNDARY.md","docs/papers211_215_sequence/PROBLEM_ANCHOR.md","docs/papers197_201_sequence/PROBLEM_ANCHOR.md"];
const EXTRA='docs/papers204_208_sequence/scouting/order_geometry_tenth_desk/PROOF_AND_ADAPTER.md';
const allowed=new Set([...EXPECTED.map(p=>p.path),OWN+'INPUT_PINS.json']);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const assertions={};
function check(k,v){assertions[k]=Boolean(v);if(!v)throw new Error('DOCUMENTARY_CHECK_FAILED '+k);}
function read(p){
  if(!allowed.has(p))throw new Error('OUTSIDE_FIXED_DOCUMENT_WHITELIST');
  let ancestor='';for(const s of (ROOT+p).split('/').filter(Boolean)){ancestor+='/'+s;if(fs.lstatSync(ancestor).isSymbolicLink())throw new Error('SYMLINK_DOCUMENT_ANCESTOR');}
  const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try{
    const before=fs.fstatSync(fd,{bigint:true});if(!before.isFile())throw new Error('NOT_REGULAR_DOCUMENT');
    const chunks=[],scratch=Buffer.alloc(65536);let n;
    while((n=fs.readSync(fd,scratch,0,scratch.length,null))!==0)chunks.push(Buffer.from(scratch.subarray(0,n)));
    const bytes=Buffer.concat(chunks),after=fs.fstatSync(fd,{bigint:true});
    for(const k of ['dev','ino','size','mtimeNs','ctimeNs'])if(before[k]!==after[k])throw new Error('CHANGED_DURING_READ');
    if(BigInt(bytes.length)!==after.size)throw new Error('EOF_SIZE_MISMATCH');
    return bytes;
  }finally{fs.closeSync(fd);}
}
const captured=new Map([...allowed].map(p=>[p,read(p)]));
const b=p=>captured.get(p),j=p=>JSON.parse(b(p).toString('utf8')),s=n=>j(SOURCE+n);
const pin=(path,bytes)=>({path,bytes:bytes.length,sha256:sha(bytes)});
for(const [p,bytes]of captured)check('utf8_roundtrip_'+p,Buffer.from(bytes.toString('utf8'),'utf8').equals(bytes));
const receiver=j(OWN+'INPUT_PINS.json');
check('exact_36_fixed_input_pins',EXPECTED.length===36&&eq(EXPECTED,receiver.files)&&eq(EXPECTED,EXPECTED.map(p=>pin(p.path,b(p.path)))));
check('source_manifest_exact_2435_byte_pin',eq(receiver.source_manifest,EXPECTED[27])&&b(SOURCE+'MANIFEST.sha256').length===2435&&sha(b(SOURCE+'MANIFEST.sha256'))==='d05381e309a7ef2a274f8b564df78a03f95d1762f2a3053f5f89acbb451599db');
const sourceSeal=Buffer.from(EXPECTED.slice(0,27).map(p=>p.sha256+'  '+p.path.slice(SOURCE.length)+'\n').join(''),'utf8');
check('source_nonself_27_payload_full_seal_bytes',b(SOURCE+'MANIFEST.sha256').equals(sourceSeal));
const oldSeal=Buffer.from(EXPECTED.slice(28,35).map(p=>p.sha256+'  '+p.path+'\n').join(''),'utf8');
check('old_exact_seven_full_pin_lines',b(SOURCE+'INPUT_PINS.sha256').equals(oldSeal)&&eq(EXPECTED.slice(28,35).map(p=>p.path),OLD));
const dirs=['','side_lane/','side_lane/raw/'];
for(const dir of dirs){
  const directFiles=NAMES.filter(n=>n.startsWith(dir)&&!n.slice(dir.length).includes('/')).map(n=>n.slice(dir.length));
  const subdirs=dir===''?['side_lane']:dir==='side_lane/'?['raw']:[];
  const entries=fs.readdirSync(ROOT+SOURCE+dir,{withFileTypes:true});
  check('source_exact_regular_census_'+(dir||'root'),eq(entries.map(e=>e.name).sort(),[...directFiles,...subdirs].sort())&&entries.every(e=>!e.isSymbolicLink()&&(subdirs.includes(e.name)?e.isDirectory():e.isFile())));
}
check('source_exact_28_files_743260_bytes',NAMES.length===28&&NAMES.reduce((sum,n)=>sum+b(SOURCE+n).length,0)===743260);
const local=s('LOCAL_TOOL_RETURNS.json'),web=s('SOURCE_TOOL_RETURNS.json'),integration=s('INTEGRATION_TOOL_RETURNS.json'),closure=s('CLOSURE_TOOL_RETURNS.json');
const groups=[['LOCAL_TOOL_RETURNS.json',local,'fresh21_local_tool_returns_v1',17],['SOURCE_TOOL_RETURNS.json',web,'fresh21_tool_returns_v1',8],['INTEGRATION_TOOL_RETURNS.json',integration,'fresh21_integration_tool_returns_v1',6],['CLOSURE_TOOL_RETURNS.json',closure,'fresh21_documentary_closure_v1',4]];
const nativeKeys=['chunk_id','wall_time_seconds','exit_code','original_token_count','output'];
const nativeOK=r=>eq(Object.keys(r),nativeKeys)&&typeof r.chunk_id==='string'&&Number.isFinite(r.wall_time_seconds)&&Number.isInteger(r.exit_code)&&Number.isInteger(r.original_token_count)&&typeof r.output==='string';
for(const [name,obj,schema,count]of groups)check('schema_and_row_count_'+name,eq(Object.keys(obj),['schema','scope','returns'])&&obj.schema===schema&&typeof obj.scope==='string'&&obj.returns.length===count);
for(const [name,obj]of [['local',local],['integration',integration],['closure',closure]])check('all_complete_native_row_keys_'+name,obj.returns.every(r=>eq(Object.keys(r),['key','cmd','r'])&&typeof r.key==='string'&&typeof r.cmd==='string'&&nativeOK(r.r)));
check('all_main_web_complete_keys',web.returns.every((r,i)=>eq(Object.keys(r),['key','args','r'])&&r.key==='fresh21_web'+String(i+1).padStart(2,'0')&&typeof r.args==='object'&&typeof r.r==='string'));
const expectedChunks=[
['71423b','0f4430','0eb925','786748','8106c1','ae07c6','56183a','51a455','7ef754','84e473','d1b22f','32ad4d','639283','5a727a','7ce83f','20b578','7ebaeb'],
['5bea45','db0f1c','c4c1f7','b39166','f7eb44','3287cc'],
['375a59','87f78b','7691a8','dcfcfd']];
[local,integration,closure].forEach((o,i)=>check('main_exact_native_chunk_order_'+i,eq(o.returns.map(r=>r.r.chunk_id),expectedChunks[i])));
check('main_exact_exit_statuses',eq(local.returns.map(r=>r.r.exit_code),[...Array(16).fill(0),2])&&integration.returns.every(r=>r.r.exit_code===0)&&eq(closure.returns.map(r=>r.r.exit_code),[0,127,0,0]));
const sideReads=NAMES.filter(n=>/^side_lane\/raw\/read/.test(n)).map(n=>[n,s(n)]);
const sideWeb=NAMES.filter(n=>/^side_lane\/raw\/web/.test(n)).map(n=>[n,s(n)]);
check('side_exact_10_native_wrappers',sideReads.length===10&&sideReads.every(([name,r],i)=>eq(Object.keys(r),i===9?['request','result']:['id','request','result'])&&nativeOK(r.result)&&r.request.workdir===(i===9?ROOT+SOURCE+'side_lane':ROOT.slice(0,-1))&&typeof r.request.cmd==='string'&&(i===9||r.id==='read'+String(i+2).padStart(2,'0'))));
check('side_exact_native_chunks',eq(sideReads.map(([,r])=>r.result.chunk_id),['667307','d9fd4d','c8026c','fea4c5','6838f8','db8348','a5d089','383810','892feb','9298ca']));
check('side_exact_native_exit_statuses',eq(sideReads.map(([,r])=>r.result.exit_code),[0,2,0,0,0,1,0,0,0,0]));
check('side_exact_5_web_wrappers',sideWeb.length===5&&sideWeb.every(([,r])=>eq(Object.keys(r),['request','result'])&&r.request&&typeof r.request==='object'&&typeof r.result==='string'));
check('all_three_known_native_truncations_preserved',local.returns[4].r.output.startsWith('Warning: truncated output')&&local.returns[5].r.output.startsWith('Warning: truncated output')&&integration.returns[3].r.output.startsWith('Warning: truncated output'));
check('failed_guessed_v3_preserved',sideWeb[0][1].request.open[0].ref_id==='https://arxiv.org/html/2112.08124v3'&&sideWeb[0][1].result.includes('(404) Not Found'));
const lines=bytes=>bytes.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];
const range=(bytes,start,end)=>Buffer.from(lines(bytes).slice(start-1,end).join(''),'utf8');
const rawPairs=[],partialPairs=[];
function pair(key,actual,expected,details={}){
  check('full_raw_'+key,actual.equals(expected));
  rawPairs.push({key,...details,actual_bytes:actual.length,expected_bytes:expected.length,actual_sha256:sha(actual),expected_sha256:sha(expected),byte_equal:actual.equals(expected)});
}
const reads=[[10,OLD[0],1,220],[11,OLD[1],1,95],[12,OLD[2],185,260],[14,OLD[2],140,185],[15,OLD[3],12,40]];
for(const [idx,path,start,end]of reads){
  const r=local.returns[idx];check('fixed_sed_command_'+idx,r.cmd==="sed -n '"+start+','+end+"p' "+path);
  pair('local_'+idx,Buffer.from(r.r.output,'utf8'),range(b(path),start,end),{record_id:r.key,path,range:[start,end]});
}
check('uss_find_exact_command',local.returns[13].cmd==="rg -n 'USS|triang|substitution' "+OLD[2]);
const rgUSS=Buffer.from(lines(b(OLD[2])).map((line,i)=>/USS|triang|substitution/.test(line)?(i+1)+':'+line:'').join(''),'utf8');
pair('local_13_exact_uss_rg',Buffer.from(local.returns[13].r.output,'utf8'),rgUSS,{record_id:local.returns[13].key,path:OLD[2]});
pair('local_16_missing_workflow_error',Buffer.from(local.returns[16].r.output,'utf8'),Buffer.from("sed: can't read .agents/skills/symbolic-dynamics-research/references/WORKFLOW.md: No such file or directory\n",'utf8'),{record_id:local.returns[16].key,note:'Archived failed text only; no absent-path query is repeated.'});
const sideDocs=['side_lane/HANDOFF.md','side_lane/PROOF_PACKAGE.md','side_lane/READ01_MISSING_ORIGINAL.md'];
check('integration_side_exact_cat_command',integration.returns[1].cmd==='cat '+sideDocs.map(n=>SOURCE+n).join(' '));
pair('integration_1_side_documents',Buffer.from(integration.returns[1].r.output,'utf8'),Buffer.concat(sideDocs.map(n=>b(SOURCE+n))),{record_id:integration.returns[1].key});
check('integration_web_exact_cat_command',integration.returns[2].cmd==='cat '+SOURCE+'side_lane/raw/web05.json '+SOURCE+'side_lane/raw/web04.json');
pair('integration_2_complete_web_json_bytes',Buffer.from(integration.returns[2].r.output,'utf8'),Buffer.concat([b(SOURCE+'side_lane/raw/web05.json'),b(SOURCE+'side_lane/raw/web04.json')]),{record_id:integration.returns[2].key});
check('integration_geometry_exact_sed_command',integration.returns[4].cmd==="sed -n '43,57p' "+OLD[4]);
pair('integration_4_old_geometry',Buffer.from(integration.returns[4].r.output,'utf8'),range(b(OLD[4]),43,57),{record_id:integration.returns[4].key,path:OLD[4],range:[43,57]});
check('integration_old_hash_exact_command',integration.returns[5].cmd==='sha256sum '+OLD.join(' '));
pair('integration_5_seven_hashes',Buffer.from(integration.returns[5].r.output,'utf8'),oldSeal,{record_id:integration.returns[5].key});
check('closure_old_hashcheck_exact_command',closure.returns[0].cmd==='sha256sum -c '+SOURCE+'INPUT_PINS.sha256');
pair('closure_0_seven_hashchecks',Buffer.from(closure.returns[0].r.output,'utf8'),Buffer.from(OLD.map(p=>p+': OK\n').join(''),'utf8'),{record_id:closure.returns[0].key});
pair('closure_1_jq_failure',Buffer.from(closure.returns[1].r.output,'utf8'),Buffer.from('/bin/bash: line 1: jq: command not found\n','utf8'),{record_id:closure.returns[1].key,note:'Original exit127 text received; no jq call or install repeated.'});
const preJSON=['INTEGRATION_TOOL_RETURNS.json','LOCAL_TOOL_RETURNS.json','SOURCE_TOOL_RETURNS.json',...NAMES.filter(n=>n.startsWith('side_lane/raw/')&&n.endsWith('.json'))];
check('exact_18_preclosure_json_objects',preJSON.length===18&&preJSON.every(n=>{const obj=s(n);return obj!==null&&typeof obj==='object'&&!Array.isArray(obj);}));
pair('closure_3_preclosure_object_shape_stdout',Buffer.from(closure.returns[3].r.output,'utf8'),Buffer.from(preJSON.map(n=>SOURCE+n+': JSON_OBJECT_OK\n').join(''),'utf8'),{record_id:closure.returns[3].key,note:'Historical syntax-only Perl stdout reconstructed as DATA, not executing its command.'});
const sidePre=['HANDOFF.md','PROOF_PACKAGE.md','READ01_MISSING_ORIGINAL.md',...Array.from({length:9},(_,i)=>'raw/read'+String(i+2).padStart(2,'0')+'.json'),...Array.from({length:5},(_,i)=>'raw/web'+String(i+1).padStart(2,'0')+'.json')];
const sideTotal=sidePre.reduce((sum,n)=>sum+b(SOURCE+'side_lane/'+n).length,0),width=String(sideTotal).length;
check('side_historical_17_files_263702_bytes',sidePre.length===17&&sideTotal===263702);
const sideWC=sidePre.map(n=>String(b(SOURCE+'side_lane/'+n).length).padStart(width,' ')+' '+n+'\n').join('')+sideTotal+' total\n';
check('side_closing_exact_command',sideReads[9][1].request.cmd==='wc -c '+sidePre.join(' ')+" && sed -n '1,125p' PROOF_PACKAGE.md");
pair('side_closing_wc_and_proof_full_stdout',Buffer.from(sideReads[9][1].result.output,'utf8'),Buffer.concat([Buffer.from(sideWC,'utf8'),range(b(SOURCE+'side_lane/PROOF_PACKAGE.md'),1,125)]),{record_id:'side_lane/read11_closing'});
function partial(key,record,expected,mode,path,rng){
  const body=Buffer.from(record.result.output,'utf8');const at=mode==='prefix'?0:mode==='suffix'?body.length-expected.length:body.indexOf(expected);
  const ok=at>=0&&body.subarray(at,at+expected.length).equals(expected)&&(mode!=='unique-infix'||body.indexOf(expected,at+1)===-1);
  check('partial_exact_'+key,ok);partialPairs.push({key,path,range:rng,mode,offset_bytes:at,matched_bytes:expected.length,matched_sha256:sha(expected),byte_equal:ok,scope:'EXACT_DECLARED_RANGE_ONLY_NOT_COMPLETE_NATIVE_STDOUT_REPLAY'});
}
partial('side_read03_anchor_prefix',sideReads[1][1],b(OLD[5]),'prefix',OLD[5],null);
partial('side_read04_old_anchor_prefix',sideReads[2][1],b(OLD[6]),'prefix',OLD[6],null);
partial('side_read06_geometry_suffix',sideReads[4][1],range(b(OLD[4]),1,72),'suffix',OLD[4],[1,72]);
partial('side_read07_QAS_infix',sideReads[5][1],range(b(EXTRA),1,90),'unique-infix',EXTRA,[1,90]);
check('exact_15_full_raw_pairs_and_4_selected_ranges',rawPairs.length===15&&partialPairs.length===4);
const allNative=[...local.returns.map((r,i)=>({key:r.key,document:'LOCAL_TOOL_RETURNS.json',index:i,command:r.cmd,r:r.r})),...integration.returns.map((r,i)=>({key:r.key,document:'INTEGRATION_TOOL_RETURNS.json',index:i,command:r.cmd,r:r.r})),...closure.returns.map((r,i)=>({key:r.key,document:'CLOSURE_TOOL_RETURNS.json',index:i,command:r.cmd,r:r.r})),...sideReads.map(([document,r])=>({key:r.id||'read11_closing',document,request:r.request,r:r.result}))];
const nativePins=allNative.map(r=>({key:r.key,document:r.document,...(r.index===undefined?{request:r.request}:{index:r.index,command:r.command}),native_keys:Object.keys(r.r),chunk_id:r.r.chunk_id,exit_code:r.r.exit_code,original_token_count:r.r.original_token_count,output:pin('output',Buffer.from(r.r.output,'utf8')),returned_output_reports_truncation:r.r.output.startsWith('Warning: truncated output'),scope:'COMPLETE_RETURNED_OBJECT_PIN; full stdout equality only for separately named complete raw pairs.'}));
const webPins=[...web.returns.map((r,i)=>({key:r.key,document:'SOURCE_TOOL_RETURNS.json',index:i,request:r.args,returned_string:pin('r',Buffer.from(r.r,'utf8'))})),...sideWeb.map(([document,r])=>({document,request:r.request,returned_string:pin('result',Buffer.from(r.result,'utf8'))}))];
check('all_37_native_and_13_web_returns_bound',nativePins.length===37&&webPins.length===13);
const structured=[];
function walk(v,path,rows){
  if(Array.isArray(v)){rows.push({path,type:'array',length:v.length});v.forEach((x,i)=>walk(x,path+'['+i+']',rows));}
  else if(v!==null&&typeof v==='object'){rows.push({path,type:'object',keys:Object.keys(v)});for(const [k,x]of Object.entries(v))walk(x,path+'.'+k,rows);}
  else if(typeof v==='string')rows.push({path,type:'string',utf8_bytes:Buffer.byteLength(v),sha256:sha(Buffer.from(v,'utf8'))});
  else rows.push({path,type:v===null?'null':typeof v,value:v});
}
for(const document of NAMES.filter(n=>n.endsWith('.json'))){const obj=s(document),nodes=[];check('source_json_is_object_'+document,obj!==null&&typeof obj==='object'&&!Array.isArray(obj));walk(obj,'$',nodes);structured.push({document,full_key_value_node_count:nodes.length,nodes});}
check('exact_19_current_structured_documents',structured.length===19);
const result={kind:'FRESH21_INDEPENDENT_FIXED_DOCUMENT_AUDIT',verdict:'PASS_EXACT_EXAMINED_DOCUMENTS_ONLY',
scientific_execution:false,author_commands_executed:false,scientific_source_imported:false,network_access:false,host_private_raw_future_operands_queried:false,arbitrary_embedded_paths_followed:false,
document_ancestor_metadata_scope:'Only ancestors of the 36 exact workspace documents and own fixed pin file; no operational host/private/raw/prospective operands.',
source_payload_count:27,source_file_count:28,source_total_bytes:743260,source_manifest:EXPECTED[27],
fixed_external_input_count:36,complete_same_fd_eof_external_inputs:36,own_pin_file_read_separately:true,input_pins:EXPECTED,
assertion_count:Object.keys(assertions).length,assertions,full_raw_pair_count:rawPairs.length,full_raw_pairs:rawPairs,selected_range_pair_count:partialPairs.length,selected_range_pairs:partialPairs,
author_native_output_pins:nativePins,author_web_return_pins:webPins,full_fixed_json_structures:structured,
limits:['Source searches and changed historical directory inventories are not rerun.','Three source native output strings contain truncation warnings; complete returned objects are not complete process stdout.','Main initial bundled capture and side read01 full original remain missing.','Reported final-seal observations a31b47/9a366f/e1b0b5 are not filesystem-archived here and are not claimed received.','Author 18-JSON and 17-side-file cutoffs remain historical DATA; current source has 19 JSON objects and 28 files.','All mathematical verdicts come from declared proof/source reading, not this documentary program.']};
process.stdout.write(JSON.stringify(result,null,2)+'\n');

