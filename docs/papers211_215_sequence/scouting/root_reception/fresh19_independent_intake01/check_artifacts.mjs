// Reviewer-authored documentary checker. No scientific imports, subprocess,
 // network, author-command execution, glob following, or filesystem writes.
import fs from 'node:fs';
import crypto from 'node:crypto';
const ROOT = '/root/autodl-tmp/symbolic_dynamics/';
const SOURCE = 'docs/papers211_215_sequence/scouting/finite_residual_fresh19/';
const OWN = 'docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/';
const NAMES = ['PLAN.md','SOURCE_READS.md','PROOF_AND_DISPOSITION.md','HANDOFF.md','SOURCE_TOOL_RETURNS.json','LOCAL_TOOL_RETURNS.json','INPUT_PINS.json','ARTIFACT_CHECK.json','manifest_sha256.json'];
const OLD = [
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
const ALLOWED = new Set([...NAMES.map(n=>SOURCE+n),...OLD,OWN+'INPUT_PINS.json']);
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const eq = (a,b) => JSON.stringify(a) === JSON.stringify(b);
const assertions = {};
function check(key,condition) {
  assertions[key]=Boolean(condition);
  if (!condition) throw new Error('CHECK_FAILED: '+key);
}
function readFixed(path) {
  if (!ALLOWED.has(path)) throw new Error('NOT_WHITELISTED');
  let prefix='';
  for (const segment of (ROOT+path).split('/').filter(Boolean)) {
    prefix+='/'+segment;
    if (fs.lstatSync(prefix).isSymbolicLink()) throw new Error('SYMLINK_REJECTED');
  }
  const fd=fs.openSync(ROOT+path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try {
    const before=fs.fstatSync(fd,{bigint:true});
    if (!before.isFile()) throw new Error('NOT_REGULAR');
    const chunks=[];const scratch=Buffer.alloc(65536);let n,reads=0;
    while((n=fs.readSync(fd,scratch,0,scratch.length,null))!==0) {
      chunks.push(Buffer.from(scratch.subarray(0,n)));reads++;
    }
    const bytes=Buffer.concat(chunks),after=fs.fstatSync(fd,{bigint:true});
    for (const field of ['dev','ino','size','mtimeNs','ctimeNs']) if(before[field]!==after[field])throw new Error('MUTATED_DURING_READ');
    if(BigInt(bytes.length)!==after.size)throw new Error('INCOMPLETE_READ');
    return {bytes,pin:{path,bytes:bytes.length,sha256:sha(bytes)},same_fd_eof:true,nonempty_reads:reads};
  } finally {fs.closeSync(fd);}
}
const captured=new Map([...ALLOWED].map(p=>[p,readFixed(p)]));
const buf=p=>captured.get(p).bytes;
const json=p=>JSON.parse(buf(p).toString('utf8'));
for(const [p,c] of captured)check('utf8_roundtrip_'+p,Buffer.from(c.bytes.toString('utf8'),'utf8').equals(c.bytes));
const ip=json(OWN+'INPUT_PINS.json');
const manifest=json(SOURCE+'manifest_sha256.json');
const oldpins=json(SOURCE+'INPUT_PINS.json');
check('source_manifest_exact_external_pin',buf(SOURCE+'manifest_sha256.json').length===1447&&sha(buf(SOURCE+'manifest_sha256.json'))==='6e2f1f2508b46072b07b68d1023d5a0813739a1855003524eca649b3282883f6');
check('manifest_keys',eq(Object.keys(manifest),['scope','files']));
check('manifest_exact_payload_order',eq(manifest.files.map(f=>f.path),NAMES.slice(0,8)));
check('manifest_payload_row_keys',manifest.files.every(f=>eq(Object.keys(f),['path','bytes','sha256'])));
check('old_input_exact_whitelist',eq(oldpins.files.map(f=>f.path),OLD));
const expectedPins=[...manifest.files.map(f=>({...f,path:SOURCE+f.path})),captured.get(SOURCE+'manifest_sha256.json').pin,...oldpins.files];
check('receiver_input_exact_19',eq(ip.files,expectedPins)&&ip.files.length===19);
check('source_manifest_pin_in_receiver',eq(ip.source_manifest,captured.get(SOURCE+'manifest_sha256.json').pin));
const actualPins=expectedPins.map(f=>captured.get(f.path).pin);
check('all_19_complete_byte_pins',eq(actualPins,expectedPins));
const census=fs.readdirSync(ROOT+SOURCE,{withFileTypes:true}).map(d=>({name:d.name,regular:d.isFile(),symbolic:d.isSymbolicLink()})).sort((a,b)=>a.name.localeCompare(b.name));
check('source_exact_9_regular_files',eq(census.map(d=>d.name),[...NAMES].sort((a,b)=>a.localeCompare(b)))&&census.every(d=>d.regular&&!d.symbolic));
const sourceBytes=NAMES.reduce((s,n)=>s+buf(SOURCE+n).length,0);
check('source_total_625497',sourceBytes===625497);
const local=json(SOURCE+'LOCAL_TOOL_RETURNS.json');
const web=json(SOURCE+'SOURCE_TOOL_RETURNS.json');
const author=json(SOURCE+'ARTIFACT_CHECK.json');
check('local_top_keys',eq(Object.keys(local),['scope','records','pin_read']));
check('source_top_keys',eq(Object.keys(web),['scope','records']));
check('local_exact_18_records',local.records.length===18);
check('web_exact_13_records',web.records.length===13);
const nativeKeys=['chunk_id','wall_time_seconds','exit_code','original_token_count','output'];
const nativeOK=r=>eq(Object.keys(r),nativeKeys)&&typeof r.chunk_id==='string'&&Number.isFinite(r.wall_time_seconds)&&Number.isInteger(r.exit_code)&&Number.isInteger(r.original_token_count)&&typeof r.output==='string';
check('first_local_record_explicit_native_without_command',eq(Object.keys(local.records[0]),['key',...nativeKeys])&&!Object.hasOwn(local.records[0],'cmd'));
const firstNative=Object.fromEntries(nativeKeys.map(k=>[k,local.records[0][k]]));
check('first_local_native_shape_and_failed_exit',nativeOK(firstNative)&&firstNative.exit_code===2&&firstNative.chunk_id==='ada80e'&&firstNative.output.startsWith('Warning: truncated output'));
check('remaining_local_full_native_shapes',local.records.slice(1).every(r=>eq(Object.keys(r),['key','cmd','r'])&&typeof r.cmd==='string'&&nativeOK(r.r)&&r.r.exit_code===0));
check('unique_local_keys',new Set(local.records.map(r=>r.key)).size===18);
check('web_full_record_shapes',web.records.every((r,i)=>eq(Object.keys(r),['key','args','result'])&&r.key==='fresh19_web'+String(i+1).padStart(2,'0')&&r.args&&typeof r.args==='object'&&typeof r.result==='string'&&r.result.length>0));
check('author_check_shape',eq(Object.keys(author),['scope','cmd','result'])&&typeof author.cmd==='string'&&nativeOK(author.result)&&author.result.exit_code===0&&author.result.chunk_id==='51ca6c');
check('old_pin_native_shape',eq(Object.keys(local.pin_read),['cmd','r'])&&nativeOK(local.pin_read.r)&&local.pin_read.r.exit_code===0&&local.pin_read.r.chunk_id==='2b76c2');
function lineRange(bytes,start,end){
  const lines=bytes.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];
  return Buffer.from(lines.slice(start-1,end).join(''),'utf8');
}
const fixedReads=[
[3,OLD[8],null],[4,OLD[9],null],[9,OLD[0],null],
[10,OLD[2],[1,62]],[11,OLD[2],[228,272]],[12,OLD[3],[328,350]],
[13,OLD[4],null],[14,OLD[5],null],[15,OLD[6],[1,58]],[16,OLD[7],null],[17,OLD[1],null]
];
const rawPairs=[];
for(const [i,path,range] of fixedReads){
  const r=local.records[i],expectedCommand=range?"sed -n '"+range[0]+','+range[1]+"p' "+path:'cat '+path;
  check('fixed_read_command_'+i,r.cmd===expectedCommand);
  const expected=range?lineRange(buf(path),...range):buf(path),actual=Buffer.from(r.r.output,'utf8');
  const same=actual.equals(expected);
  check('full_raw_fixed_read_'+i,same);
  rawPairs.push({record_index:i,key:r.key,path,range,actual_bytes:actual.length,expected_bytes:expected.length,actual_sha256:sha(actual),expected_sha256:sha(expected),byte_equal:same});
}
const pinExpected=Buffer.from(JSON.stringify(oldpins.files,null,2)+'\n','utf8');
const pinActual=Buffer.from(local.pin_read.r.output,'utf8');
check('full_raw_old_pin_output',pinActual.equals(pinExpected));
rawPairs.push({key:'local.pin_read',actual_bytes:pinActual.length,expected_bytes:pinExpected.length,actual_sha256:sha(pinActual),expected_sha256:sha(pinExpected),byte_equal:pinActual.equals(pinExpected)});
const authorExpectedObject={
kind:'AUTHOR_ARTIFACT_CHECK_ONLY',scientific_execution:false,independent_review:false,verdict:'PASS_ARTIFACTS_ONLY',
files:manifest.files.slice(0,7).map(f=>({name:f.path,bytes:f.bytes,sha256:f.sha256})),
source_record_count:13,local_record_count:18,input_pin_count:10,old_inputs:OLD.map(path=>({path,match:true})),exact_owned_file_set:true
};
const authorExpected=Buffer.from(JSON.stringify(authorExpectedObject,null,2)+'\n','utf8');
const authorActual=Buffer.from(author.result.output,'utf8');
check('full_raw_archived_pre_manifest_artifact_stdout',authorActual.equals(authorExpected));
rawPairs.push({key:'author.ARTIFACT_CHECK.result.output',actual_bytes:authorActual.length,expected_bytes:authorExpected.length,actual_sha256:sha(authorActual),expected_sha256:sha(authorExpected),byte_equal:authorActual.equals(authorExpected)});
check('exact_13_full_raw_pairs',rawPairs.length===13&&rawPairs.every(p=>p.byte_equal));
const localOutputPins=local.records.map((r,i)=>{const n=i===0?r:r.r,b=Buffer.from(n.output,'utf8');return {index:i,key:r.key,chunk_id:n.chunk_id,exit_code:n.exit_code,bytes:b.length,sha256:sha(b),comparison:i===0||[1,2,5,6,7,8].includes(i)?'PIN_AND_SHAPE_ONLY_NO_CURRENT_SEARCH_REPLAY':'FULL_FIXED_READ_RAW_COMPARISON'};});
const webReturnPins=web.records.map(r=>{const b=Buffer.from(r.result,'utf8');return {key:r.key,bytes:b.length,sha256:sha(b),comparison:'ARCHIVED_RETURN_PIN_AND_SHAPE_ONLY_NOT_PUBLISHER_BYTES'};});
const output={
kind:'FRESH19_INDEPENDENT_DOCUMENTARY_ARTIFACT_CHECK',
verdict:'PASS_EXACT_EXAMINED_ARTIFACTS_ONLY',
scientific_execution:false,author_commands_executed:false,network_access:false,
arbitrary_embedded_path_following:false,host_or_prospective_path_access:false,
source_root:SOURCE,source_file_count:9,source_total_bytes:sourceBytes,input_file_count:19,
same_fd_eof_input_count:19,checker_own_pin_file_read_separately:true,
source_manifest:ip.source_manifest,input_pins:actualPins,source_census:census,
assertion_count:Object.keys(assertions).length,assertions,
full_raw_pair_count:rawPairs.length,full_raw_pairs:rawPairs,
local_output_pins:localOutputPins,web_return_pins:webReturnPins,
limits:['No mathematical proof is executed or certified by this checker.','Seven inventory/search outputs are pins and shape only, including the first failed command whose request is absent.','Archived pre-manifest stdout is reconstructed as documentary data; the old author command is not rerun.','Web-return strings are not raw publisher bytes or exhaustive search proof.','Selected old proof claims only; fresh17/fresh18 global validity is not recertified.']
};
process.stdout.write(JSON.stringify(output,null,2)+'\n');

