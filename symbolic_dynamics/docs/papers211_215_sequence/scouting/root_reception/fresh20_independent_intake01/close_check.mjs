// Reviewer-written fixed-document receipt closure; read-only.
// Documentary mechanics adapted from this reviewer's frozen Fresh19 closure.
// This code imports no author/scientific source and executes no subprocess.
import fs from 'node:fs';
import crypto from 'node:crypto';
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const OWN='docs/papers211_215_sequence/scouting/root_reception/fresh20_independent_intake01/';
const SOURCE='docs/papers211_215_sequence/scouting/finite_residual_fresh20/';
const EXPECTED=[
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh20/HANDOFF.md",
    "bytes": 1961,
    "sha256": "a7c179b59d5f4efac6b18155f18c785771a60661a9a2f9c46e625c4ce9b38a0a"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh20/INPUT_PINS.json",
    "bytes": 2961,
    "sha256": "a21b75648c51691d81ee4ccdf096d41bce43180b6b1e6df1d29a424c0bf99a5e"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh20/LOCAL_TOOL_RETURNS.json",
    "bytes": 62001,
    "sha256": "8e7903e749278fae8806bf0d5699758f61f3db5f9177b770289600d13a366fe7"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh20/PLAN.md",
    "bytes": 3146,
    "sha256": "8817c063f3ff516a255b92adea2ce67adcb5ab94bf84b7cfec1d684e265231a9"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh20/PROOF_PACKAGE.md",
    "bytes": 12981,
    "sha256": "8b69b02c675e8184d2f251ac3c5381d796435fa312ed8f4e9e4ae8ffc9eaaede"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh20/SOURCE_READS.md",
    "bytes": 6490,
    "sha256": "0c36b72a0c697aa83388a234fadeacbf0b179993e2f2800b4b3c3fd1d2928256"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh20/SOURCE_TOOL_RETURNS.json",
    "bytes": 433348,
    "sha256": "d6ecc445f51ee67caca2601cd1ba6280e861760857303cdbebbec303b1722854"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh20/VALIDATION_TOOL_RETURN.json",
    "bytes": 6469,
    "sha256": "0341bb79c2f116e6cf7fdde7e2c45ea664605b8a475c185100f48e71fd3840c0"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_residual_fresh20/SHA256SUMS",
    "bytes": 673,
    "sha256": "81f283494acc5405f122800efad73fbd26b341bdb371fff6736a93255354d2f3"
  },
  {
    "path": "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/SCOUT.md",
    "bytes": 3485,
    "sha256": "b0e4093de77887ed95a73ee8eb642a86c1a2df589f5a5104b8e42781beddce0f"
  },
  {
    "path": "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/THEOREM_CONTRACT.md",
    "bytes": 1884,
    "sha256": "042e3bba1efe6d1809cea629306f85b84d62c9bfb1a8c438c5ac9428f9becf2e"
  },
  {
    "path": "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/PROOF_PACKAGE.md",
    "bytes": 5778,
    "sha256": "e5488d3af2a1694f8bf52ca7352af7eb3b0a424268aea2fb1e884bda21bf3186"
  },
  {
    "path": "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/DERIVATION_PACKAGE.md",
    "bytes": 7145,
    "sha256": "3a64688bea6e63c5c08f680e32bd25c61332e763e1fc2a4c19378bbf523312b8"
  },
  {
    "path": "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/OWNER_AUDIT.md",
    "bytes": 2059,
    "sha256": "1e1dccbbd732423f331588d6c1da10661d9e3e28fe561a9014eaa3bb49a7f6f8"
  },
  {
    "path": "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/COLLISION_GATE.md",
    "bytes": 3306,
    "sha256": "b36ecf57c910819afa77c7edfe575dc1a953445beb61f66d6d5de32ca0fd8c74"
  },
  {
    "path": "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/OWNER_SEARCH_LOG.md",
    "bytes": 2372,
    "sha256": "79d7c0d642d97a7e2a8cd651b6847ac2f163aacf6d5d98ed9c5ce3fb1a0ec6bd"
  },
  {
    "path": "docs/papers204_208_sequence/scouting/word_local/pilot.py",
    "bytes": 3635,
    "sha256": "47ef2ae36194132f91d6f70d83f2ae2c8cb841107c49bc3e8142badcfe56347c"
  },
  {
    "path": "docs/papers204_208_sequence/scouting/word_local/SCOUT_REPORT.md",
    "bytes": 9991,
    "sha256": "409386c784732f459bff9a4fb2214e27633d50e51e3ea49eaea288a2c6b54dd4"
  },
  {
    "path": "docs/papers204_208_sequence/scouting/finite_systems_thirty_fourth/SLATE.md",
    "bytes": 3032,
    "sha256": "e5c0988d442159b9bcda809d946d15670764dd8cbd5573b462cd2d00ff54ff4a"
  },
  {
    "path": "docs/papers211_215_sequence/scouting/finite_function_lane/PROOF_PACKAGE.md",
    "bytes": 12034,
    "sha256": "b03e77ef6ea707f9ebfdc6defefb331c069ce2b9cc66f6f3af8929a0fd12e1a8"
  }
];
const BASE=['ORIGIN_AND_SCOPE.md','REVIEW.md','FINDINGS.json','INPUT_PINS.json','PRIMARY_RETURNS.json','LOCAL_READ_RETURNS.json','check_artifacts.mjs','ARTIFACT_CHECK.json','ARTIFACT_CHECK_NATIVE.json','close_check.mjs'];
const FINAL=[...BASE,'CLOSING_CHECK.json','CLOSING_NATIVE.json','MANIFEST.sha256'];
const NAMES=['HANDOFF.md','INPUT_PINS.json','LOCAL_TOOL_RETURNS.json','PLAN.md','PROOF_PACKAGE.md','SOURCE_READS.md','SOURCE_TOOL_RETURNS.json','VALIDATION_TOOL_RETURN.json','SHA256SUMS'];
const external=EXPECTED.map(p=>p.path),OLD=external.slice(9,19);
const whitelist=new Set([...FINAL.map(n=>OWN+n),...external]);
const sealed=process.argv.length===3&&process.argv[2]==='--sealed';
if(process.argv.length>2&&!sealed)throw new Error('UNSUPPORTED_ARGUMENT');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const assertions={};
function test(k,v){assertions[k]=Boolean(v);if(!v)throw new Error('CLOSURE_FAILED '+k);}
function read(p){
  if(!whitelist.has(p))throw new Error('OUTSIDE_LITERAL_WHITELIST');
  let current='';for(const s of (ROOT+p).split('/').filter(Boolean)){current+='/'+s;if(fs.lstatSync(current).isSymbolicLink())throw new Error('SYMLINK');}
  const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try{
    const before=fs.fstatSync(fd,{bigint:true});if(!before.isFile())throw new Error('NOT_REGULAR');
    const chunks=[],scratch=Buffer.alloc(65536);let n;
    while((n=fs.readSync(fd,scratch,0,scratch.length,null))!==0)chunks.push(Buffer.from(scratch.subarray(0,n)));
    const b=Buffer.concat(chunks),after=fs.fstatSync(fd,{bigint:true});
    for(const k of ['dev','ino','size','mtimeNs','ctimeNs'])if(before[k]!==after[k])throw new Error('CHANGED_DURING_READ');
    if(BigInt(b.length)!==after.size)throw new Error('EOF_SIZE');
    return b;
  }finally{fs.closeSync(fd);}
}
const captured=new Map([...BASE.map(n=>OWN+n),...external].map(p=>[p,read(p)]));
const b=p=>captured.get(p),j=p=>JSON.parse(b(p).toString('utf8'));
const ownj=n=>j(OWN+n),pin=(path,bytes)=>({path,bytes:bytes.length,sha256:sha(bytes)});
test('all_30_fixed_inputs_utf8_roundtrip',captured.size===30&&[...captured.values()].every(v=>Buffer.from(v.toString('utf8'),'utf8').equals(v)));
test('external_fixed_20_complete_pins',eq(EXPECTED,external.map(p=>pin(p,b(p)))));
const pins=ownj('INPUT_PINS.json'),old=j(SOURCE+'INPUT_PINS.json');
test('receipt_exact_20_pin_rows',eq(Object.keys(pins),['scope','source_manifest','files'])&&eq(pins.files,EXPECTED)&&eq(pins.source_manifest,EXPECTED[8]));
test('source_manifest_fixed_pin',b(SOURCE+'SHA256SUMS').length===673&&sha(b(SOURCE+'SHA256SUMS'))==='81f283494acc5405f122800efad73fbd26b341bdb371fff6736a93255354d2f3');
const expectedSeal=Buffer.from(EXPECTED.slice(0,8).map(p=>p.sha256+'  '+p.path.slice(SOURCE.length)+'\n').join(''),'utf8');
test('source_nonself_8_payload_exact_seal_bytes',b(SOURCE+'SHA256SUMS').equals(expectedSeal));
test('source_old_exact_10_paths_and_pins',eq(old.inputs.map(p=>p.path),OLD)&&old.inputs.every((p,i)=>p.bytes===EXPECTED[i+9].bytes&&p.sha256===EXPECTED[i+9].sha256));
const sourceList=fs.readdirSync(ROOT+SOURCE,{withFileTypes:true});
test('source_9_regular_exact_files',eq(sourceList.map(x=>x.name).sort(),[...NAMES].sort())&&sourceList.every(x=>x.isFile()&&!x.isSymbolicLink()));
test('source_530030_bytes',NAMES.reduce((s,n)=>s+b(SOURCE+n).length,0)===530030);
const a=ownj('ARTIFACT_CHECK.json'),n=ownj('ARTIFACT_CHECK_NATIVE.json');
test('artifact_full_native_wrapper',eq(Object.keys(n),['request','actual_return']));
test('artifact_native_exact_request',eq(n.request,{cmd:'node '+OWN+'check_artifacts.mjs',workdir:ROOT.slice(0,-1),max_output_tokens:45000}));
const nativeKeys=['chunk_id','wall_time_seconds','exit_code','original_token_count','output'];
test('artifact_native_full_keys',eq(Object.keys(n.actual_return),nativeKeys));
test('artifact_native_exit_chunk',n.actual_return.exit_code===0&&n.actual_return.chunk_id==='3f6331');
const artifactRaw=Buffer.from(n.actual_return.output,'utf8');
test('artifact_complete_raw_stdout_byte_equal',artifactRaw.equals(b(OWN+'ARTIFACT_CHECK.json')));
test('artifact_full_parsed_output_equal',eq(JSON.parse(n.actual_return.output),a));
const artifactKeys=['kind','verdict','scientific_execution','author_or_scientific_source_executed','network_access','host_private_raw_future_operands_queried','arbitrary_embedded_paths_followed','document_ancestor_metadata_scope','source_file_count','source_total_bytes','source_payload_count','source_manifest','fixed_external_input_count','complete_same_fd_eof_external_inputs','own_pin_file_read_separately','input_pins','assertion_count','assertions','full_raw_pair_count','full_raw_pairs','author_native_output_pins','author_source_return_pins','full_fixed_json_structures','limits'];
test('artifact_exact_all_24_top_keys',eq(Object.keys(a),artifactKeys));
test('artifact_exact_74_assertions_true',a.assertion_count===74&&Object.keys(a.assertions).length===74&&Object.values(a.assertions).every(x=>x===true));
test('artifact_exact_14_full_raw_pairs',a.full_raw_pair_count===14&&a.full_raw_pairs.length===14&&a.full_raw_pairs.every(p=>p.byte_equal===true&&p.actual_bytes===p.expected_bytes&&p.actual_sha256===p.expected_sha256));
test('artifact_input_and_manifest_full_equal',eq(a.input_pins,EXPECTED)&&eq(a.source_manifest,EXPECTED[8])&&a.fixed_external_input_count===20&&a.complete_same_fd_eof_external_inputs===20&&a.own_pin_file_read_separately===true);
test('artifact_documentary_scope',a.verdict==='PASS_EXACT_EXAMINED_DOCUMENTS_ONLY'&&[a.scientific_execution,a.author_or_scientific_source_executed,a.network_access,a.host_private_raw_future_operands_queried,a.arbitrary_embedded_paths_followed].every(x=>x===false));
const local=j(SOURCE+'LOCAL_TOOL_RETURNS.json'),web=j(SOURCE+'SOURCE_TOOL_RETURNS.json'),author=j(SOURCE+'VALIDATION_TOOL_RETURN.json');
const localPins=local.records.map((r,i)=>({record_id:r.record_id,...pin('local.records['+i+'].native_return.output',Buffer.from(r.native_return.output,'utf8')),chunk_id:r.native_return.chunk_id,exit_code:r.native_return.exit_code,coverage:[0,1,2,4].includes(i)?'COMPLETE_RETURN_PIN_AND_SHAPE_NOT_CURRENT_DISCOVERY_REPLAY':'COMPLETE_FIXED_DOCUMENT_RAW_COMPARISON'}));
const webPins=web.records.map((r,i)=>({record_id:r.record_id,...pin('web.records['+i+'].result',Buffer.from(r.result,'utf8')),coverage:'COMPLETE_ARCHIVED_RETURN_PIN_NOT_PUBLISHER_BYTES'}));
test('artifact_all_17_native_output_rows_recomputed',localPins.length===17&&eq(localPins,a.author_native_output_pins));
test('artifact_all_17_browser_return_rows_recomputed',webPins.length===17&&eq(webPins,a.author_source_return_pins));
function walk(v,path,rows){
  if(Array.isArray(v)){rows.push({path,type:'array',length:v.length});v.forEach((x,i)=>walk(x,path+'['+i+']',rows));}
  else if(v!==null&&typeof v==='object'){rows.push({path,type:'object',keys:Object.keys(v)});for(const [k,x]of Object.entries(v))walk(x,path+'.'+k,rows);}
  else if(typeof v==='string')rows.push({path,type:'string',utf8_bytes:Buffer.byteLength(v),sha256:sha(Buffer.from(v,'utf8'))});
  else rows.push({path,type:v===null?'null':typeof v,value:v});
}
const structures=[];
for(const [document,obj]of [['INPUT_PINS.json',old],['LOCAL_TOOL_RETURNS.json',local],['SOURCE_TOOL_RETURNS.json',web],['VALIDATION_TOOL_RETURN.json',author]]){
  const nodes=[];walk(obj,'$',nodes);structures.push({document,full_key_value_node_count:nodes.length,nodes});
}
test('all_four_fixed_json_complete_key_value_trees_recomputed',eq(structures,a.full_fixed_json_structures));
test('all_four_node_censuses_exact',eq(structures.map(x=>x.full_key_value_node_count),[55,157,250,9]));
const f=ownj('FINDINGS.json');
test('finding_census_all_zero',[f.critical,f.major,f.minor,f.current_open].every(x=>x===0)&&f.findings.length===0);
test('denominator_exact_one_new_one_closed',f.new_literal_attempts===1&&f.closed_attempts===1&&[f.pilot_proposals,f.scientific_executions,f.nominations,f.reserves,f.central_count_change].every(x=>x===0));
test('bounded_verdict_and_independence',f.verdict==='ACCEPT_BOUNDED_ONE_ATTEMPT_CLOSURE'&&f.author_disposition==='KILL_OLD_NULLITY_FACTOR_NO_SECOND_RESIDUAL'&&f.personal_author_noncontribution===true&&f.inherited_root_familiarity_disclosed===true&&f.author_contact===false&&f.root_adoption_performed===false);
test('no_central_or_seat_transition',f.central_closed_count_at_assignment===59&&f.retained===3&&f.complete===1&&f.open_seats===2);
const w=ownj('PRIMARY_RETURNS.json'),r=ownj('LOCAL_READ_RETURNS.json');
test('independent_primary_exact_4_full_return_records',eq(Object.keys(w),['scope','records'])&&w.records.length===4&&w.records.every((x,i)=>eq(Object.keys(x),['key','request','actual_return'])&&x.key==='fresh20_indep_web'+String(i+1).padStart(2,'0')&&typeof x.actual_return==='string'&&x.actual_return.length>0));
const readKeys=['fresh20_indep_navigation','fresh20_indep_fulldocs','fresh20_indep_oldproof','fresh20_indep_oldcontext','fresh20_indep_archive_shape','fresh20_indep_archive_shape2','fresh20_indep_extra_original','fresh20_indep_fixedpins','fresh20_indep_scope_census'];
test('independent_local_exact_9_selected_full_native_records',eq(Object.keys(r),['scope','records'])&&eq(r.records.map(x=>x.key),readKeys)&&r.records.every(x=>eq(Object.keys(x),['key','request','actual_return'])&&eq(Object.keys(x.actual_return),nativeKeys)&&typeof x.actual_return.output==='string'));
const ownList=fs.readdirSync(ROOT+OWN,{withFileTypes:true}),nameSet=ownList.map(x=>x.name).sort();
test('owned_exact_supported_freeze_stage',[[...BASE],[...BASE,'CLOSING_CHECK.json','CLOSING_NATIVE.json'],FINAL].some(names=>eq([...names].sort(),nameSet))&&ownList.every(x=>x.isFile()&&!x.isSymbolicLink()));
const basePins=BASE.map(name=>pin(name,b(OWN+name)));
const primaryReturnPins=w.records.map(x=>pin(x.key,Buffer.from(x.actual_return,'utf8')));
const localNativeOutputPins=r.records.map(x=>({...pin(x.key,Buffer.from(x.actual_return.output,'utf8')),chunk_id:x.actual_return.chunk_id,exit_code:x.actual_return.exit_code}));
const result={kind:'FRESH20_INDEPENDENT_RECEIPT_BASE_CLOSURE',verdict:'PASS_EXACT_DOCUMENTARY_CLOSURE_ONLY',
scientific_execution:false,author_or_scientific_source_executed:false,network_access:false,host_private_raw_future_operands_queried:false,arbitrary_embedded_paths_followed:false,
base_payload_count:10,base_payload_bytes:basePins.reduce((s,p)=>s+p.bytes,0),source_file_count:9,source_total_bytes:530030,external_fixed_inputs_same_fd_eof:20,own_base_inputs_same_fd_eof:10,
artifact_stdout_pair:{bytes:artifactRaw.length,sha256:sha(artifactRaw),full_raw_byte_equal:true,full_parsed_object_equal:true},
source_json_node_censuses:structures.map(x=>({document:x.document,full_key_value_node_count:x.full_key_value_node_count})),
assertion_count:Object.keys(assertions).length,assertions,base_payload_pins:basePins,
independent_primary_return_pins:primaryReturnPins,independent_local_native_output_pins:localNativeOutputPins,
scope:'Closure of fixed documentary inputs, complete JSON key/value trees and full native/raw output only. Not mathematical proof execution, candidate admission or root adoption.'};
const canonical=Buffer.from(JSON.stringify(result,null,2)+'\n','utf8');
if(!sealed){process.stdout.write(canonical);process.exit(0);}
const closing=read(OWN+'CLOSING_CHECK.json'),closingNative=read(OWN+'CLOSING_NATIVE.json'),seal=read(OWN+'MANIFEST.sha256');
const cn=JSON.parse(closingNative.toString('utf8')),sealAssertions={};
function finalTest(k,v){sealAssertions[k]=Boolean(v);if(!v)throw new Error('SEALED_CLOSURE_FAILED '+k);}
finalTest('current_base_full_raw_canonical_equal',canonical.equals(closing));
finalTest('closing_native_exact_full_wrapper',eq(Object.keys(cn),['request','actual_return'])&&eq(Object.keys(cn.actual_return),nativeKeys));
finalTest('closing_native_success_exact_command',cn.actual_return.exit_code===0&&cn.request.cmd==='node '+OWN+'close_check.mjs'&&cn.request.workdir===ROOT.slice(0,-1));
finalTest('closing_native_full_raw_stdout_equal',Buffer.from(cn.actual_return.output,'utf8').equals(closing));
finalTest('closing_native_full_parsed_object_equal',eq(JSON.parse(cn.actual_return.output),JSON.parse(closing.toString('utf8'))));
const payloadBuffers=[...BASE.map(name=>[name,b(OWN+name)]),['CLOSING_CHECK.json',closing],['CLOSING_NATIVE.json',closingNative]];
const receiptSeal=Buffer.from(payloadBuffers.map(([name,bytes])=>sha(bytes)+'  '+name+'\n').join(''),'utf8');
finalTest('nonself_manifest_exact_12_payload_full_bytes',seal.equals(receiptSeal));
finalTest('owned_sealed_exact_13_files',eq(nameSet,[...FINAL].sort()));
const payloadTotal=payloadBuffers.reduce((s,[,bytes])=>s+bytes.length,0);
process.stdout.write(JSON.stringify({kind:'FRESH20_INDEPENDENT_SEALED_RECEIPT_CHECK',verdict:'PASS_EXACT_SEAL_AND_DOCUMENTARY_SCOPE_ONLY',scientific_execution:false,base_assertion_count:result.assertion_count,base_assertions:assertions,sealed_assertion_count:Object.keys(sealAssertions).length,sealed_assertions:sealAssertions,payload_count:12,physical_file_count:13,payload_bytes:payloadTotal,physical_bytes:payloadTotal+seal.length,manifest:pin('MANIFEST.sha256',seal),closing_stdout:pin('CLOSING_CHECK.json',closing),artifact_stdout:pin('ARTIFACT_CHECK.json',artifactRaw),source_manifest:pins.source_manifest},null,2)+'\n');

