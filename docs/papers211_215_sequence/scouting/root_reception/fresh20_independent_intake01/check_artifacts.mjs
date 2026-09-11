// Fresh20 independently adapted fixed-document audit. Read-only.
// No author/source import, subprocess, scientific operation, network or writes.
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
const OLD=[
  "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/SCOUT.md",
  "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/THEOREM_CONTRACT.md",
  "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/PROOF_PACKAGE.md",
  "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/DERIVATION_PACKAGE.md",
  "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/OWNER_AUDIT.md",
  "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/COLLISION_GATE.md",
  "docs/papers162_166_sequence/scouting/root_nullity_feedback_jordan_power/OWNER_SEARCH_LOG.md",
  "docs/papers204_208_sequence/scouting/word_local/pilot.py",
  "docs/papers204_208_sequence/scouting/word_local/SCOUT_REPORT.md",
  "docs/papers204_208_sequence/scouting/finite_systems_thirty_fourth/SLATE.md"
];
const NAMES=['HANDOFF.md','INPUT_PINS.json','LOCAL_TOOL_RETURNS.json','PLAN.md','PROOF_PACKAGE.md','SOURCE_READS.md','SOURCE_TOOL_RETURNS.json','VALIDATION_TOOL_RETURN.json','SHA256SUMS'];
const EXTRA='docs/papers211_215_sequence/scouting/finite_function_lane/PROOF_PACKAGE.md';
const ALLOWED=new Set([...EXPECTED.map(p=>p.path),OWN+'INPUT_PINS.json']);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const assertions={};
function check(k,v){assertions[k]=Boolean(v);if(!v)throw new Error('DOCUMENTARY_CHECK_FAILED '+k);}
function readFixed(p){
  if(!ALLOWED.has(p))throw new Error('OUTSIDE_FIXED_DOCUMENT_WHITELIST');
  let ancestor='';for(const part of (ROOT+p).split('/').filter(Boolean)){ancestor+='/'+part;if(fs.lstatSync(ancestor).isSymbolicLink())throw new Error('DOCUMENT_ANCESTOR_SYMLINK');}
  const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  try{
    const before=fs.fstatSync(fd,{bigint:true});if(!before.isFile())throw new Error('NOT_REGULAR_DOCUMENT');
    const chunks=[],scratch=Buffer.alloc(65536);let n;
    while((n=fs.readSync(fd,scratch,0,scratch.length,null))!==0)chunks.push(Buffer.from(scratch.subarray(0,n)));
    const bytes=Buffer.concat(chunks),after=fs.fstatSync(fd,{bigint:true});
    for(const k of ['dev','ino','size','mtimeNs','ctimeNs'])if(before[k]!==after[k])throw new Error('DOCUMENT_CHANGED_DURING_READ');
    if(BigInt(bytes.length)!==after.size)throw new Error('EOF_LENGTH_MISMATCH');
    return bytes;
  }finally{fs.closeSync(fd);}
}
const captured=new Map([...ALLOWED].map(p=>[p,readFixed(p)]));
const b=p=>captured.get(p),j=p=>JSON.parse(b(p).toString('utf8'));
const pin=(path,bytes)=>({path,bytes:bytes.length,sha256:sha(bytes)});
for(const [p,bytes]of captured)check('utf8_roundtrip_'+p,Buffer.from(bytes.toString('utf8'),'utf8').equals(bytes));
const receiver=j(OWN+'INPUT_PINS.json');
check('receiver_exact_20_fixed_pins',eq(receiver.files,EXPECTED)&&EXPECTED.length===20);
check('all_20_complete_document_pins',eq(EXPECTED,EXPECTED.map(p=>pin(p.path,b(p.path)))));
check('source_manifest_exact_pin',b(SOURCE+'SHA256SUMS').length===673&&sha(b(SOURCE+'SHA256SUMS'))==='81f283494acc5405f122800efad73fbd26b341bdb371fff6736a93255354d2f3');
check('receiver_source_manifest_binding',eq(receiver.source_manifest,EXPECTED[8]));
const expectedSeal=Buffer.from(EXPECTED.slice(0,8).map(p=>p.sha256+'  '+p.path.slice(SOURCE.length)+'\n').join(''),'utf8');
check('source_nonself_seal_exact_full_bytes',b(SOURCE+'SHA256SUMS').equals(expectedSeal));
const entries=fs.readdirSync(ROOT+SOURCE,{withFileTypes:true});
check('source_exact_9_regular_file_census',eq(entries.map(p=>p.name).sort(),[...NAMES].sort())&&entries.every(p=>p.isFile()&&!p.isSymbolicLink()));
check('source_exact_530030_bytes',NAMES.reduce((s,n)=>s+b(SOURCE+n).length,0)===530030);
const local=j(SOURCE+'LOCAL_TOOL_RETURNS.json'),web=j(SOURCE+'SOURCE_TOOL_RETURNS.json'),author=j(SOURCE+'VALIDATION_TOOL_RETURN.json'),op=j(SOURCE+'INPUT_PINS.json');
check('old_pin_top_keys',eq(Object.keys(op),['schema','workspace_root','scope','inputs']));
check('old_pin_schema_and_root',op.schema==='fresh20.old-input-pins.v1'&&op.workspace_root===ROOT.slice(0,-1));
check('old_pin_exact_10_paths',eq(op.inputs.map(p=>p.path),OLD)&&op.inputs.length===10);
check('old_pin_all_row_keys',op.inputs.every(p=>eq(Object.keys(p),['sha256','path','bytes','read_scope'])));
check('old_pin_values_match_complete_originals',op.inputs.every(p=>p.bytes===b(p.path).length&&p.sha256===sha(b(p.path))));
check('local_top_keys_and_schema',eq(Object.keys(local),['schema','scope','records'])&&local.schema==='fresh20.selected-native-returns.v1');
check('web_top_keys_and_schema',eq(Object.keys(web),['schema','scope','records'])&&web.schema==='fresh20.browser-returns.v1');
check('local_exact_17_selected_records',local.records.length===17);
check('web_exact_17_records',web.records.length===17);
const nativeKeys=['chunk_id','wall_time_seconds','exit_code','original_token_count','output'];
const nativeOK=r=>eq(Object.keys(r),nativeKeys)&&typeof r.chunk_id==='string'&&Number.isFinite(r.wall_time_seconds)&&Number.isInteger(r.exit_code)&&Number.isInteger(r.original_token_count)&&typeof r.output==='string';
const localIds=['fresh20_rdp_history01','fresh20_rdp_history02','fresh20_rdp_history03','fresh20_rdp_history04','fresh20_jordan01','fresh20_jordan02','fresh20_jordan03','fresh20_jordan04','fresh20_jordan05','fresh20_jordan06','fresh20_jordan07','fresh20_jordan08','fresh20_close_local01','fresh20_close_local02','fresh20_close_local03','fresh20_input_hash_native','fresh20_input_bytes_native'];
const chunks=['3d526c','59590a','285f2c','92efdb','a6b1b0','4160e0','13b563','86d004','7895c3','abd701','b70c73','97d5c4','196597','0eefee','1338fb','bfca93','469f40'];
check('local_all_complete_record_and_native_keys',local.records.every(r=>eq(Object.keys(r),['record_id','command','native_return'])&&typeof r.command==='string'&&nativeOK(r.native_return)));
check('local_exact_record_id_order',eq(local.records.map(r=>r.record_id),localIds));
check('local_exact_chunks_and_success',eq(local.records.map(r=>r.native_return.chunk_id),chunks)&&local.records.every(r=>r.native_return.exit_code===0));
check('web_complete_record_keys',web.records.every(r=>eq(Object.keys(r),['record_id','request','result'])&&r.request&&typeof r.request==='object'&&typeof r.result==='string'));
check('web_exact_record_id_order',web.records.every((r,i)=>r.record_id==='fresh20_web'+String(i+1).padStart(2,'0')));
check('author_validation_complete_keys',eq(Object.keys(author),['schema','command','native_return'])&&author.schema==='fresh20.documentary-validation-return.v1'&&typeof author.command==='string'&&nativeOK(author.native_return));
check('author_validation_original_success',author.native_return.exit_code===0&&author.native_return.chunk_id==='8998af');
function lines(bytes){return bytes.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];}
function range(bytes,start,end){return Buffer.from(lines(bytes).slice(start-1,end).join(''),'utf8');}
const rawPairs=[];
function pair(key,actual,expected,details={}){
  const ok=actual.equals(expected);check('full_raw_'+key,ok);
  rawPairs.push({key,...details,actual_bytes:actual.length,expected_bytes:expected.length,actual_sha256:sha(actual),expected_sha256:sha(expected),byte_equal:ok});
}
const fixedReads=[[3,EXTRA,[1,210]],[5,OLD[4],null],[6,OLD[6],null],[7,OLD[0],null],[8,OLD[1],null],[9,OLD[2],null],[10,OLD[3],null],[11,OLD[5],null],[13,OLD[8],[1,35]],[14,OLD[9],null]];
for(const [i,path,rng]of fixedReads){
  const rec=local.records[i],command=rng?"sed -n '"+rng[0]+','+rng[1]+"p' "+path:'cat '+path;
  check('fixed_read_command_'+i,rec.command===command);
  pair('local_'+i,Buffer.from(rec.native_return.output,'utf8'),rng?range(b(path),...rng):b(path),{record_id:rec.record_id,path,range:rng});
}
const ps=local.records[12];
check('fixed_ps_rg_command',ps.command==="rg -n -A 18 -B 3 '^def palindrome_suffix' "+OLD[7]);
const psLines=lines(b(OLD[7]));
check('fixed_ps_match_unique_at_27',psLines.map((line,i)=>/^def palindrome_suffix/.test(line)?i+1:null).filter(x=>x!==null).join(',')==='27');
const psExpected=Buffer.from(psLines.slice(23,45).map((line,i)=>(i+24)+(i+24===27?':':'-')+line).join(''),'utf8');
pair('local_12_rg_ps',Buffer.from(ps.native_return.output,'utf8'),psExpected,{record_id:ps.record_id,path:OLD[7],range:[24,45],note:'One fixed match; exact rg line-prefix rendering reconstructed without executing pilot.py or rg.'});
check('fixed_old_hash_command',local.records[15].command==='sha256sum '+OLD.join(' '));
pair('local_15_hash',Buffer.from(local.records[15].native_return.output,'utf8'),Buffer.from(OLD.map(p=>sha(b(p))+'  '+p+'\n').join(''),'utf8'),{record_id:local.records[15].record_id});
check('fixed_old_wc_command',local.records[16].command==='wc -c '+OLD.join(' '));
const oldTotal=OLD.reduce((s,p)=>s+b(p).length,0),width=String(oldTotal).length;
const wcExpected=OLD.map(p=>String(b(p).length).padStart(width,' ')+' '+p+'\n').join('')+oldTotal+' total\n';
pair('local_16_wc',Buffer.from(local.records[16].native_return.output,'utf8'),Buffer.from(wcExpected,'utf8'),{record_id:local.records[16].record_id});
const firstSeven=EXPECTED.slice(0,7).map(p=>({path:p.path.slice(SOURCE.length),bytes:p.bytes,sha256:p.sha256}));
const validationExpected={
scope:'Documentary preseal validation only; no scientific map or old verifier executed',payload_files:7,
total_payload_bytes:firstSeven.reduce((s,p)=>s+p.bytes,0),browser_records:17,selected_local_records:17,input_pin_matches:10,
files:firstSeven,inputChecks:op.inputs.map(p=>({path:p.path,bytes:p.bytes,sha256:p.sha256,match:true})),scientific_execution:false,independent_review:false};
check('author_seven_payload_data_522888',validationExpected.total_payload_bytes===522888);
pair('author_preseal_validation',Buffer.from(author.native_return.output,'utf8'),Buffer.from(JSON.stringify(validationExpected,null,2)+'\n','utf8'),{record_id:'VALIDATION_TOOL_RETURN',note:'Historical seven-file preseal stdout received as DATA; the archived command is not rerun.'});
check('exact_14_full_raw_pairs',rawPairs.length===14&&rawPairs.every(p=>p.byte_equal));
const nativeOutputPins=local.records.map((r,i)=>({record_id:r.record_id,...pin('local.records['+i+'].native_return.output',Buffer.from(r.native_return.output,'utf8')),chunk_id:r.native_return.chunk_id,exit_code:r.native_return.exit_code,coverage:[0,1,2,4].includes(i)?'COMPLETE_RETURN_PIN_AND_SHAPE_NOT_CURRENT_DISCOVERY_REPLAY':'COMPLETE_FIXED_DOCUMENT_RAW_COMPARISON'}));
const sourceReturnPins=web.records.map((r,i)=>({record_id:r.record_id,...pin('web.records['+i+'].result',Buffer.from(r.result,'utf8')),coverage:'COMPLETE_ARCHIVED_RETURN_PIN_NOT_PUBLISHER_BYTES'}));
const documentStructures=[];
function structure(value,path,rows){
  if(Array.isArray(value)){rows.push({path,type:'array',length:value.length});value.forEach((v,i)=>structure(v,path+'['+i+']',rows));}
  else if(value!==null&&typeof value==='object'){rows.push({path,type:'object',keys:Object.keys(value)});for(const [k,v]of Object.entries(value))structure(v,path+'.'+k,rows);}
  else if(typeof value==='string')rows.push({path,type:'string',utf8_bytes:Buffer.byteLength(value),sha256:sha(Buffer.from(value,'utf8'))});
  else rows.push({path,type:value===null?'null':typeof value,value});
}
for(const [name,obj]of [['INPUT_PINS.json',op],['LOCAL_TOOL_RETURNS.json',local],['SOURCE_TOOL_RETURNS.json',web],['VALIDATION_TOOL_RETURN.json',author]]){
  const rows=[];structure(obj,'$',rows);documentStructures.push({document:name,full_key_value_node_count:rows.length,nodes:rows});
}
const result={kind:'FRESH20_INDEPENDENT_FIXED_DOCUMENT_AUDIT',verdict:'PASS_EXACT_EXAMINED_DOCUMENTS_ONLY',
scientific_execution:false,author_or_scientific_source_executed:false,network_access:false,
host_private_raw_future_operands_queried:false,arbitrary_embedded_paths_followed:false,
document_ancestor_metadata_scope:'Only ancestors of the exact twenty workspace documents and own fixed pin file; not operational host or prospective operands.',
source_file_count:9,source_total_bytes:530030,source_payload_count:8,source_manifest:EXPECTED[8],
fixed_external_input_count:20,complete_same_fd_eof_external_inputs:20,own_pin_file_read_separately:true,
input_pins:EXPECTED,assertion_count:Object.keys(assertions).length,assertions,
full_raw_pair_count:rawPairs.length,full_raw_pairs:rawPairs,author_native_output_pins:nativeOutputPins,author_source_return_pins:sourceReturnPins,
full_fixed_json_structures:documentStructures,
limits:['Four archived history/inventory outputs are identity/shape only, not current repository discovery replays.','Unarchived early regex-error/truncated broad-search originals are unavailable and not reconstructed.','Author preseal seven-file validation is archived DATA; current source census is nine.','Whole original files are byte-bound; semantic read scope is declared separately.','No scientific execution, theorem enumeration, manuscript A/B, candidate admission or central count change is performed.']};
process.stdout.write(JSON.stringify(result,null,2)+'\n');

