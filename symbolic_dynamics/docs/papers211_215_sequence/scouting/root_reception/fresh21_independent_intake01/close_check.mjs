// Reviewer-written read-only Fresh21 fixed-document receipt closure.
// Documentary mechanics adapted from this reviewer's earlier receipt closures.
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
const BASE=['ORIGIN_AND_SCOPE.md','REVIEW.md','FINDINGS.json','INPUT_PINS.json','PRIMARY_RETURNS.json','LOCAL_READ_RETURNS.json','check_artifacts.mjs','ARTIFACT_CHECK.json','ARTIFACT_CHECK_NATIVE.json','close_check.mjs'];
const FINAL=[...BASE,'CLOSING_CHECK.json','CLOSING_NATIVE.json','MANIFEST.sha256'];
const external=EXPECTED.map(p=>p.path),allowed=new Set([...external,...FINAL.map(n=>OWN+n)]);
const sealed=process.argv.length===3&&process.argv[2]==='--sealed';
if(process.argv.length>2&&!sealed)throw new Error('UNSUPPORTED_ARGUMENT');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b),assertions={};
function test(k,v){assertions[k]=Boolean(v);if(!v)throw new Error('DOCUMENTARY_CLOSURE_FAILED '+k);}
function read(p){
  if(!allowed.has(p))throw new Error('OUTSIDE_LITERAL_WHITELIST');
  let ancestor='';for(const s of (ROOT+p).split('/').filter(Boolean)){ancestor+='/'+s;if(fs.lstatSync(ancestor).isSymbolicLink())throw new Error('DOCUMENT_ANCESTOR_SYMLINK');}
  const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try{
    const before=fs.fstatSync(fd,{bigint:true});if(!before.isFile())throw new Error('NOT_REGULAR');
    const chunks=[],scratch=Buffer.alloc(65536);let n;
    while((n=fs.readSync(fd,scratch,0,scratch.length,null))!==0)chunks.push(Buffer.from(scratch.subarray(0,n)));
    const bytes=Buffer.concat(chunks),after=fs.fstatSync(fd,{bigint:true});
    for(const k of ['dev','ino','size','mtimeNs','ctimeNs'])if(before[k]!==after[k])throw new Error('DOCUMENT_CHANGED_DURING_READ');
    if(BigInt(bytes.length)!==after.size)throw new Error('EOF_SIZE');
    return bytes;
  }finally{fs.closeSync(fd);}
}
const captured=new Map([...external,...BASE.map(n=>OWN+n)].map(p=>[p,read(p)]));
const b=p=>captured.get(p),j=p=>JSON.parse(b(p).toString('utf8')),ownj=n=>j(OWN+n),src=n=>j(SOURCE+n);
const pin=(path,bytes)=>({path,bytes:bytes.length,sha256:sha(bytes)});
test('all_46_fixed_inputs_utf8_reversible',captured.size===46&&[...captured.values()].every(v=>Buffer.from(v.toString('utf8'),'utf8').equals(v)));
test('all_36_external_complete_byte_pins_unchanged',eq(EXPECTED,external.map(p=>pin(p,b(p)))));
const pins=ownj('INPUT_PINS.json');
test('receipt_exact_36_pins_and_source_manifest',eq(Object.keys(pins),['scope','source_manifest','files'])&&eq(pins.files,EXPECTED)&&eq(pins.source_manifest,EXPECTED[27]));
test('source_manifest_exact_pin',b(SOURCE+'MANIFEST.sha256').length===2435&&sha(b(SOURCE+'MANIFEST.sha256'))==='d05381e309a7ef2a274f8b564df78a03f95d1762f2a3053f5f89acbb451599db');
const sourceSeal=Buffer.from(EXPECTED.slice(0,27).map(p=>p.sha256+'  '+p.path.slice(SOURCE.length)+'\n').join(''),'utf8');
test('source_nonself_exact_27_payload_seal_bytes',sourceSeal.equals(b(SOURCE+'MANIFEST.sha256')));
test('source_seven_old_pin_lines',b(SOURCE+'INPUT_PINS.sha256').equals(Buffer.from(EXPECTED.slice(28,35).map(p=>p.sha256+'  '+p.path+'\n').join(''),'utf8')));
for(const dir of ['','side_lane/','side_lane/raw/']){
  const directFiles=NAMES.filter(n=>n.startsWith(dir)&&!n.slice(dir.length).includes('/')).map(n=>n.slice(dir.length));
  const subdirs=dir===''?['side_lane']:dir==='side_lane/'?['raw']:[];
  const entries=fs.readdirSync(ROOT+SOURCE+dir,{withFileTypes:true});
  test('source_exact_regular_census_'+(dir||'root'),eq(entries.map(e=>e.name).sort(),[...directFiles,...subdirs].sort())&&entries.every(e=>!e.isSymbolicLink()&&(subdirs.includes(e.name)?e.isDirectory():e.isFile())));
}
test('source_28_files_743260_bytes',NAMES.length===28&&NAMES.reduce((sum,n)=>sum+b(SOURCE+n).length,0)===743260);
const a=ownj('ARTIFACT_CHECK.json'),n=ownj('ARTIFACT_CHECK_NATIVE.json'),nativeKeys=['chunk_id','wall_time_seconds','exit_code','original_token_count','output'];
test('artifact_exact_native_wrapper_keys',eq(Object.keys(n),['request','actual_return'])&&eq(Object.keys(n.actual_return),nativeKeys));
test('artifact_exact_native_request_and_success',eq(n.request,{cmd:'node '+OWN+'check_artifacts.mjs',workdir:ROOT.slice(0,-1),max_output_tokens:55000})&&n.actual_return.exit_code===0&&n.actual_return.chunk_id==='0205a0');
const artifactRaw=Buffer.from(n.actual_return.output,'utf8');
test('artifact_entire_raw_stdout_byte_equal',artifactRaw.equals(b(OWN+'ARTIFACT_CHECK.json')));
test('artifact_complete_parsed_object_equal',eq(JSON.parse(n.actual_return.output),a));
test('artifact_all_27_top_keys',eq(Object.keys(a),["kind","verdict","scientific_execution","author_commands_executed","scientific_source_imported","network_access","host_private_raw_future_operands_queried","arbitrary_embedded_paths_followed","document_ancestor_metadata_scope","source_payload_count","source_file_count","source_total_bytes","source_manifest","fixed_external_input_count","complete_same_fd_eof_external_inputs","own_pin_file_read_separately","input_pins","assertion_count","assertions","full_raw_pair_count","full_raw_pairs","selected_range_pair_count","selected_range_pairs","author_native_output_pins","author_web_return_pins","full_fixed_json_structures","limits"]));
test('artifact_all_118_assertions_true',a.assertion_count===118&&Object.keys(a.assertions).length===118&&Object.values(a.assertions).every(x=>x===true));
test('artifact_all_15_full_raw_pairs',a.full_raw_pair_count===15&&a.full_raw_pairs.length===15&&a.full_raw_pairs.every(p=>p.byte_equal===true&&p.actual_bytes===p.expected_bytes&&p.actual_sha256===p.expected_sha256));
test('artifact_all_4_declared_partial_ranges',a.selected_range_pair_count===4&&a.selected_range_pairs.length===4&&a.selected_range_pairs.every(p=>p.byte_equal===true&&p.scope==='EXACT_DECLARED_RANGE_ONLY_NOT_COMPLETE_NATIVE_STDOUT_REPLAY'));
test('artifact_all_inputs_and_documentary_scope',eq(a.input_pins,EXPECTED)&&eq(a.source_manifest,EXPECTED[27])&&a.verdict==='PASS_EXACT_EXAMINED_DOCUMENTS_ONLY'&&a.fixed_external_input_count===36&&a.complete_same_fd_eof_external_inputs===36&&[a.scientific_execution,a.author_commands_executed,a.scientific_source_imported,a.network_access,a.host_private_raw_future_operands_queried,a.arbitrary_embedded_paths_followed].every(x=>x===false));
const local=src('LOCAL_TOOL_RETURNS.json'),integration=src('INTEGRATION_TOOL_RETURNS.json'),closure=src('CLOSURE_TOOL_RETURNS.json'),web=src('SOURCE_TOOL_RETURNS.json');
const sideReads=NAMES.filter(n=>/^side_lane\/raw\/read/.test(n)).map(n=>[n,src(n)]);
const sideWeb=NAMES.filter(n=>/^side_lane\/raw\/web/.test(n)).map(n=>[n,src(n)]);
const allNative=[...local.returns.map((r,i)=>({key:r.key,document:'LOCAL_TOOL_RETURNS.json',index:i,command:r.cmd,r:r.r})),...integration.returns.map((r,i)=>({key:r.key,document:'INTEGRATION_TOOL_RETURNS.json',index:i,command:r.cmd,r:r.r})),...closure.returns.map((r,i)=>({key:r.key,document:'CLOSURE_TOOL_RETURNS.json',index:i,command:r.cmd,r:r.r})),...sideReads.map(([document,r])=>({key:r.id||'read11_closing',document,request:r.request,r:r.result}))];
const nativePins=allNative.map(r=>({key:r.key,document:r.document,...(r.index===undefined?{request:r.request}:{index:r.index,command:r.command}),native_keys:Object.keys(r.r),chunk_id:r.r.chunk_id,exit_code:r.r.exit_code,original_token_count:r.r.original_token_count,output:pin('output',Buffer.from(r.r.output,'utf8')),returned_output_reports_truncation:r.r.output.startsWith('Warning: truncated output'),scope:'COMPLETE_RETURNED_OBJECT_PIN; full stdout equality only for separately named complete raw pairs.'}));
const webPins=[...web.returns.map((r,i)=>({key:r.key,document:'SOURCE_TOOL_RETURNS.json',index:i,request:r.args,returned_string:pin('r',Buffer.from(r.r,'utf8'))})),...sideWeb.map(([document,r])=>({document,request:r.request,returned_string:pin('result',Buffer.from(r.result,'utf8'))}))];
test('all_37_complete_author_native_pin_rows_recomputed',nativePins.length===37&&eq(nativePins,a.author_native_output_pins));
test('all_13_complete_author_web_pin_rows_recomputed',webPins.length===13&&eq(webPins,a.author_web_return_pins));
function walk(v,path,rows){
  if(Array.isArray(v)){rows.push({path,type:'array',length:v.length});v.forEach((x,i)=>walk(x,path+'['+i+']',rows));}
  else if(v!==null&&typeof v==='object'){rows.push({path,type:'object',keys:Object.keys(v)});for(const [k,x]of Object.entries(v))walk(x,path+'.'+k,rows);}
  else if(typeof v==='string')rows.push({path,type:'string',utf8_bytes:Buffer.byteLength(v),sha256:sha(Buffer.from(v,'utf8'))});
  else rows.push({path,type:v===null?'null':typeof v,value:v});
}
const structures=NAMES.filter(n=>n.endsWith('.json')).map(document=>{const nodes=[];walk(src(document),'$',nodes);return {document,full_key_value_node_count:nodes.length,nodes};});
test('all_19_complete_source_json_key_value_trees_recomputed',structures.length===19&&eq(structures,a.full_fixed_json_structures));
test('all_513_source_json_nodes_exact_census',eq(structures.map(x=>x.full_key_value_node_count),[40,58,157,108,11,11,11,11,11,11,11,11,11,11,7,9,8,8,8])&&structures.reduce((sum,x)=>sum+x.nodes.length,0)===513);
const f=ownj('FINDINGS.json');
test('finding_census_all_zero',[f.critical,f.major,f.minor,f.current_open].every(x=>x===0)&&f.findings.length===0);
test('literal_denominator_one_plus_zero_closed_one',f.main_new_literal_attempts===1&&f.side_new_literal_attempts===0&&f.closed_attempts===1);
test('no_pilot_science_nomination_reserve_or_central_delta',[f.pilot_proposals,f.scientific_executions,f.nominations,f.reserves,f.central_count_change].every(x=>x===0));
test('bounded_verdict_and_independence',f.verdict==='ACCEPT_BOUNDED_ONE_ATTEMPT_CLOSURE'&&f.author_disposition==='CLOSE_SOURCE_PRIMITIVE_TRIANGULAR_SINGLETON'&&f.personal_author_noncontribution===true&&f.inherited_root_routing_familiarity_disclosed===true&&f.author_contact===false&&f.root_adoption_performed===false);
test('assignment_count_snapshot_unchanged',f.central_closed_count_at_assignment===59&&f.retained===3&&f.complete===1&&f.open_seats===2);
const w=ownj('PRIMARY_RETURNS.json'),r=ownj('LOCAL_READ_RETURNS.json');
test('independent_exact_3_primary_records',eq(Object.keys(w),['scope','records'])&&w.records.length===3&&w.records.every((x,i)=>eq(Object.keys(x),['key','request','actual_return'])&&x.key==='fresh21_indep_web'+String(i+1).padStart(2,'0')&&typeof x.actual_return==='string'));
test('independent_exact_9_native_records',eq(Object.keys(r),['scope','records'])&&eq(r.records.map(x=>x.key),["fresh21_indep_navigation","fresh21_indep_workflow_inventory","fresh21_indep_main_documents","fresh21_indep_side_and_old","fresh21_indep_source_shapes","fresh21_indep_source_shapes2","fresh21_indep_old_and_closure","fresh21_indep_fixedpins","fresh21_indep_archived_primary_slices"])&&r.records.every(x=>eq(Object.keys(x),['key','request','actual_return'])&&eq(Object.keys(x.actual_return),nativeKeys)&&typeof x.actual_return.output==='string'));
const ownList=fs.readdirSync(ROOT+OWN,{withFileTypes:true}),nameSet=ownList.map(x=>x.name).sort();
test('owned_exact_supported_freeze_stage',[[...BASE],[...BASE,'CLOSING_CHECK.json','CLOSING_NATIVE.json'],FINAL].some(ns=>eq([...ns].sort(),nameSet))&&ownList.every(x=>x.isFile()&&!x.isSymbolicLink()));
const basePins=BASE.map(name=>pin(name,b(OWN+name)));
const result={kind:'FRESH21_INDEPENDENT_RECEIPT_BASE_CLOSURE',verdict:'PASS_EXACT_DOCUMENTARY_CLOSURE_ONLY',scientific_execution:false,author_commands_executed:false,network_access:false,host_private_raw_future_operands_queried:false,arbitrary_embedded_paths_followed:false,base_payload_count:10,base_payload_bytes:basePins.reduce((sum,p)=>sum+p.bytes,0),source_file_count:28,source_total_bytes:743260,external_fixed_inputs_same_fd_eof:36,own_base_inputs_same_fd_eof:10,artifact_stdout_pair:{bytes:artifactRaw.length,sha256:sha(artifactRaw),full_raw_byte_equal:true,full_parsed_object_equal:true},source_json_node_censuses:structures.map(x=>({document:x.document,nodes:x.nodes.length})),assertion_count:Object.keys(assertions).length,assertions,base_payload_pins:basePins,independent_primary_return_pins:w.records.map(x=>pin(x.key,Buffer.from(x.actual_return,'utf8'))),independent_local_native_output_pins:r.records.map(x=>({...pin(x.key,Buffer.from(x.actual_return.output,'utf8')),chunk_id:x.actual_return.chunk_id,exit_code:x.actual_return.exit_code})),scope:'Fixed-document and complete native/raw/key-value closure only; not science, root adoption or global source certification.'};
const canonical=Buffer.from(JSON.stringify(result,null,2)+'\n','utf8');
if(!sealed){process.stdout.write(canonical);process.exit(0);}
const closing=read(OWN+'CLOSING_CHECK.json'),closingNative=read(OWN+'CLOSING_NATIVE.json'),seal=read(OWN+'MANIFEST.sha256'),cn=JSON.parse(closingNative.toString('utf8')),sealedAssertions={};
function finalTest(k,v){sealedAssertions[k]=Boolean(v);if(!v)throw new Error('SEALED_CLOSURE_FAILED '+k);}
finalTest('current_full_raw_base_canonical_equal',canonical.equals(closing));
finalTest('closing_complete_native_wrapper_keys',eq(Object.keys(cn),['request','actual_return'])&&eq(Object.keys(cn.actual_return),nativeKeys));
finalTest('closing_native_exact_command_and_success',cn.request.cmd==='node '+OWN+'close_check.mjs'&&cn.request.workdir===ROOT.slice(0,-1)&&cn.actual_return.exit_code===0);
finalTest('closing_native_complete_raw_stdout_equal',Buffer.from(cn.actual_return.output,'utf8').equals(closing));
finalTest('closing_native_complete_parsed_object_equal',eq(JSON.parse(cn.actual_return.output),JSON.parse(closing.toString('utf8'))));
const payloadBuffers=[...BASE.map(n=>[n,b(OWN+n)]),['CLOSING_CHECK.json',closing],['CLOSING_NATIVE.json',closingNative]];
const expectedSeal=Buffer.from(payloadBuffers.map(([n,bytes])=>sha(bytes)+'  '+n+'\n').join(''),'utf8');
finalTest('receipt_nonself_exact_12_payload_seal',seal.equals(expectedSeal));
finalTest('receipt_sealed_exact_13_regular_files',eq(nameSet,[...FINAL].sort()));
const payloadTotal=payloadBuffers.reduce((sum,[,bytes])=>sum+bytes.length,0);
process.stdout.write(JSON.stringify({kind:'FRESH21_INDEPENDENT_SEALED_RECEIPT_CHECK',verdict:'PASS_EXACT_SEAL_AND_DOCUMENTARY_SCOPE_ONLY',scientific_execution:false,base_assertion_count:result.assertion_count,base_assertions:assertions,sealed_assertion_count:Object.keys(sealedAssertions).length,sealed_assertions:sealedAssertions,payload_count:12,physical_file_count:13,payload_bytes:payloadTotal,physical_bytes:payloadTotal+seal.length,manifest:pin('MANIFEST.sha256',seal),closing_stdout:pin('CLOSING_CHECK.json',closing),artifact_stdout:pin('ARTIFACT_CHECK.json',artifactRaw),source_manifest:pins.source_manifest},null,2)+'\n');

