// Reviewer-written fixed-whitelist documentary receipt closure; no writes.
import fs from 'node:fs';
import crypto from 'node:crypto';
const ROOT='/root/autodl-tmp/symbolic_dynamics/';
const OWN='docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/';
const SOURCE='docs/papers211_215_sequence/scouting/finite_residual_fresh19/';
const BASE=['ORIGIN_AND_SCOPE.md','REVIEW.md','FINDINGS.json','INPUT_PINS.json','PRIMARY_RETURNS.json','LOCAL_READ_RETURNS.json','check_artifacts.mjs','ARTIFACT_CHECK.json','ARTIFACT_CHECK_NATIVE.json','close_check.mjs'];
const FINAL=[...BASE,'CLOSING_CHECK.json','CLOSING_NATIVE.json','MANIFEST.sha256'];
const SOURCES=['PLAN.md','SOURCE_READS.md','PROOF_AND_DISPOSITION.md','HANDOFF.md','SOURCE_TOOL_RETURNS.json','LOCAL_TOOL_RETURNS.json','INPUT_PINS.json','ARTIFACT_CHECK.json','manifest_sha256.json'];
const OLD=[
  "docs/papers211_215_sequence/scouting/finite_metric_reconstruction_scout01/PROOF_PACKAGE.md",
  "docs/papers211_215_sequence/scouting/finite_metric_reconstruction_scout01/SOURCE_READS.md",
  "docs/papers122_126_sequence/scouting/combinatorial/SCOUT.md",
  "docs/papers117_121_sequence/scouting/ALGEBRAIC_PHASE2B_SCOUT.md",
  "docs/papers204_208_sequence/scouting/algebra/PROOF_NOTES.md",
  "papers/106-synchronous-mis-polarity-dynamics/main.tex",
  "docs/papers211_215_sequence/scouting/set_code_lane/PROOF_PACKAGE.md",
  "docs/papers204_208_sequence/scouting/finite_systems_eighteenth/PROOF_AND_ADAPTERS.md",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh18/PROOF_AND_DISPOSITION.md",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh17/PROOF_PACKAGE.md"
];
const external=[...SOURCES.map(n=>SOURCE+n),...OLD];
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
const ownj=n=>j(OWN+n),pin=(p,bytes)=>({path:p,bytes:bytes.length,sha256:sha(bytes)});
const sourceManifest=j(SOURCE+'manifest_sha256.json'),sourceOld=j(SOURCE+'INPUT_PINS.json');
test('external_source_manifest_pin',b(SOURCE+'manifest_sha256.json').length===1447&&sha(b(SOURCE+'manifest_sha256.json'))==='6e2f1f2508b46072b07b68d1023d5a0813739a1855003524eca649b3282883f6');
test('source_payload_fixed_whitelist',eq(sourceManifest.files.map(p=>p.path),SOURCES.slice(0,8)));
test('source_old_fixed_whitelist',eq(sourceOld.files.map(p=>p.path),OLD));
const expected=[...sourceManifest.files.map(p=>({...p,path:SOURCE+p.path})),pin(SOURCE+'manifest_sha256.json',b(SOURCE+'manifest_sha256.json')),...sourceOld.files];
const pins=ownj('INPUT_PINS.json');
test('receipt_fixed_19_input_pins',eq(pins.files,expected)&&eq(pins.files.map(p=>p.path),external));
test('all_19_unchanged_complete_byte_pins',eq(expected,external.map(p=>pin(p,b(p)))));
const sourceList=fs.readdirSync(ROOT+SOURCE,{withFileTypes:true});
test('source_9_regular_exact_files',eq(sourceList.map(x=>x.name).sort(),[...SOURCES].sort())&&sourceList.every(x=>x.isFile()&&!x.isSymbolicLink()));
test('source_625497_bytes',SOURCES.reduce((s,n)=>s+b(SOURCE+n).length,0)===625497);
const a=ownj('ARTIFACT_CHECK.json'),n=ownj('ARTIFACT_CHECK_NATIVE.json');
test('artifact_full_native_wrapper',eq(Object.keys(n),['request','actual_return']));
test('artifact_native_exact_command',n.request.cmd==='node '+OWN+'check_artifacts.mjs'&&n.request.workdir===ROOT.slice(0,-1));
test('artifact_native_full_keys',eq(Object.keys(n.actual_return),['chunk_id','wall_time_seconds','exit_code','original_token_count','output']));
test('artifact_native_exit_chunk',n.actual_return.exit_code===0&&n.actual_return.chunk_id==='6ddd26');
const artifactRaw=Buffer.from(n.actual_return.output,'utf8');
test('artifact_complete_raw_stdout_byte_equal',artifactRaw.equals(b(OWN+'ARTIFACT_CHECK.json')));
test('artifact_full_parsed_output_equal',eq(JSON.parse(n.actual_return.output),a));
test('artifact_exact_66_assertions_true',a.assertion_count===66&&Object.keys(a.assertions).length===66&&Object.values(a.assertions).every(x=>x===true));
test('artifact_exact_13_full_pairs',a.full_raw_pair_count===13&&a.full_raw_pairs.length===13&&a.full_raw_pairs.every(p=>p.byte_equal&&p.actual_bytes===p.expected_bytes&&p.actual_sha256===p.expected_sha256));
test('artifact_input_pins_full_equal',eq(a.input_pins,pins.files));
test('artifact_documentary_only_scope',a.verdict==='PASS_EXACT_EXAMINED_ARTIFACTS_ONLY'&&a.scientific_execution===false&&a.author_commands_executed===false&&a.host_or_prospective_path_access===false);
test('artifact_native_return_pin_counts',a.local_output_pins.length===18&&a.web_return_pins.length===13);
const f=ownj('FINDINGS.json');
test('finding_census_all_zero',[f.critical,f.major,f.minor,f.current_open,f.examined_new_literal_count,f.pilot_proposals,f.scientific_executions,f.nominations,f.reserves].every(x=>x===0)&&f.findings.length===0);
test('bounded_verdict_and_independence',f.verdict==='ACCEPT_BOUNDED_NEGATIVE_DESK'&&f.personal_author_noncontribution&&f.inherited_root_familiarity_disclosed&&f.author_contact===false&&f.root_adoption_performed===false);
const w=ownj('PRIMARY_RETURNS.json'),r=ownj('LOCAL_READ_RETURNS.json');
test('independent_primary_exact_8_full_return_records',w.records.length===8&&w.records.every((r,i)=>eq(Object.keys(r),['key','request','actual_return'])&&r.key==='fresh19_indep_web'+String(i+1).padStart(2,'0')&&typeof r.actual_return==='string'&&r.actual_return.length>0));
test('independent_local_exact_8_native_records',r.records.length===8&&r.records.every(r=>eq(Object.keys(r),['key','request','actual_return'])&&eq(Object.keys(r.actual_return),['chunk_id','wall_time_seconds','exit_code','original_token_count','output'])&&typeof r.actual_return.output==='string'));
const ownList=fs.readdirSync(ROOT+OWN,{withFileTypes:true});
const nameSet=ownList.map(x=>x.name).sort();
test('owned_exact_supported_freeze_stage',[[...BASE],[...BASE,'CLOSING_CHECK.json','CLOSING_NATIVE.json'],FINAL].some(names=>eq([...names].sort(),nameSet))&&ownList.every(x=>x.isFile()&&!x.isSymbolicLink()));
const basePins=BASE.map(name=>pin(name,b(OWN+name)));
const primaryReturnPins=w.records.map(r=>pin(r.key,Buffer.from(r.actual_return,'utf8')));
const localNativeOutputPins=r.records.map(r=>({...pin(r.key,Buffer.from(r.actual_return.output,'utf8')),chunk_id:r.actual_return.chunk_id,exit_code:r.actual_return.exit_code}));
const result={kind:'FRESH19_INDEPENDENT_RECEIPT_BASE_CLOSURE',verdict:'PASS_EXACT_DOCUMENTARY_CLOSURE_ONLY',
scientific_execution:false,author_commands_executed:false,network_access:false,arbitrary_embedded_paths_followed:false,
base_payload_count:10,base_payload_bytes:basePins.reduce((s,p)=>s+p.bytes,0),source_file_count:9,source_total_bytes:625497,
external_fixed_inputs_same_fd_eof:19,own_base_inputs_same_fd_eof:10,
artifact_stdout_pair:{bytes:artifactRaw.length,sha256:sha(artifactRaw),full_raw_byte_equal:true,full_parsed_object_equal:true},
assertion_count:Object.keys(assertions).length,assertions,base_payload_pins:basePins,
independent_primary_return_pins:primaryReturnPins,independent_local_native_output_pins:localNativeOutputPins,
scope:'Closure of fixed documentary inputs and full native/raw output only. Not mathematical proof execution or root adoption.'};
const canonical=Buffer.from(JSON.stringify(result,null,2)+'\n','utf8');
if(!sealed){process.stdout.write(canonical);process.exit(0);}
const closing=read(OWN+'CLOSING_CHECK.json'),closingNative=read(OWN+'CLOSING_NATIVE.json'),seal=read(OWN+'MANIFEST.sha256');
const cn=JSON.parse(closingNative.toString('utf8'));
const sealAssertions={};
function finalTest(k,v){sealAssertions[k]=Boolean(v);if(!v)throw new Error('SEALED_CLOSURE_FAILED '+k);}
finalTest('current_base_full_raw_canonical_equal',canonical.equals(closing));
finalTest('closing_native_exact_full_wrapper',eq(Object.keys(cn),['request','actual_return'])&&eq(Object.keys(cn.actual_return),['chunk_id','wall_time_seconds','exit_code','original_token_count','output']));
finalTest('closing_native_success_exact_command',cn.actual_return.exit_code===0&&cn.request.cmd==='node '+OWN+'close_check.mjs');
finalTest('closing_native_full_raw_stdout_equal',Buffer.from(cn.actual_return.output,'utf8').equals(closing));
finalTest('closing_native_full_parsed_object_equal',eq(JSON.parse(cn.actual_return.output),JSON.parse(closing.toString('utf8'))));
const payloadBuffers=[...BASE.map(name=>[name,b(OWN+name)]),['CLOSING_CHECK.json',closing],['CLOSING_NATIVE.json',closingNative]];
const expectedSeal=Buffer.from(payloadBuffers.map(([name,bytes])=>sha(bytes)+'  '+name+'\n').join(''),'utf8');
finalTest('nonself_manifest_exact_12_payload_full_bytes',seal.equals(expectedSeal));
finalTest('owned_sealed_exact_13_files',eq(nameSet,[...FINAL].sort()));
const payloadTotal=payloadBuffers.reduce((s,[,bytes])=>s+bytes.length,0);
process.stdout.write(JSON.stringify({kind:'FRESH19_INDEPENDENT_SEALED_RECEIPT_CHECK',verdict:'PASS_EXACT_SEAL_AND_DOCUMENTARY_SCOPE_ONLY',scientific_execution:false,base_assertion_count:result.assertion_count,base_assertions:assertions,sealed_assertion_count:Object.keys(sealAssertions).length,sealed_assertions:sealAssertions,payload_count:12,physical_file_count:13,payload_bytes:payloadTotal,physical_bytes:payloadTotal+seal.length,manifest:pin('MANIFEST.sha256',seal),closing_stdout:pin('CLOSING_CHECK.json',closing),artifact_stdout:pin('ARTIFACT_CHECK.json',artifactRaw),source_manifest:pins.source_manifest},null,2)+'\n');

