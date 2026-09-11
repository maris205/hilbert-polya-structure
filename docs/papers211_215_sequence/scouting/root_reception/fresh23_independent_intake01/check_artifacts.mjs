// Documentary intake only. Never execute archived commands or scientific code.
import fs from 'node:fs';
import crypto from 'node:crypto';

const SOURCE='docs/papers211_215_sequence/scouting/finite_residual_fresh23/';
const OWN='docs/papers211_215_sequence/scouting/root_reception/fresh23_independent_intake01/';
const SOURCE_NAMES=['DESK.md','READ_SCOPE.md','NATIVE_READS.json','PRIMARY_RETURNS.json','DOCUMENTARY_RECEIPT.json','SHA256SUMS'];
const OLD=[
 'docs/papers204_208_sequence/scouting/word_local/GM_PROOF_PACKAGE.md',
 'docs/papers204_208_sequence/scouting/word_local/GM_GATE/CANDIDATE_GATE.md',
 'docs/papers162_166_sequence/scouting/replacement_crossclass/SCOUT.md',
 'docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md',
 'docs/papers211_215_sequence/PROBLEM_ANCHOR.md',
 'docs/papers197_201_sequence/PROBLEM_ANCHOR.md',
];
const OWN_NAMES=['INPUT_PINS.json','LOCAL_READ_RETURNS.json','PRIMARY_RETURNS.json','FINDINGS.json','ORIGIN_AND_SCOPE.md','REVIEW.md'];
const ALLOWED=new Set([...SOURCE_NAMES.map(x=>SOURCE+x),...OLD,...OWN_NAMES.map(x=>OWN+x)]);
let assertions=0, jsonNodes=0;
const checks={};
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
function requireThat(x,label){assertions++;if(!x)throw Error(label);}
function record(label,value=true){requireThat(!Object.hasOwn(checks,label),'duplicate check label');checks[label]=value;}
function read(path){
 requireThat(ALLOWED.has(path),'not a fixed documentary input');
 const a=path.split('/');
 requireThat(a[0]==='docs'&&!a.some(x=>!x||x==='.'||x==='..'),'relative docs scope');
 for(let j=1;j<a.length;j++){const s=fs.lstatSync(a.slice(0,j).join('/'));requireThat(s.isDirectory()&&!s.isSymbolicLink(),'document ancestor');}
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  const before=fs.fstatSync(fd,{bigint:true});requireThat(before.isFile(),'regular file');
  const b=fs.readFileSync(fd), after=fs.fstatSync(fd,{bigint:true});
  for(const k of ['dev','ino','size','mtimeNs','ctimeNs'])requireThat(before[k]===after[k],'same descriptor '+k);
  const probe=Buffer.alloc(1);requireThat(fs.readSync(fd,probe,0,1,null)===0,'descriptor EOF');
  requireThat(BigInt(b.length)===after.size,'full declared bytes');
  requireThat(Buffer.from(b.toString('utf8'),'utf8').equals(b),'reversible UTF8');
  return b;
 }finally{fs.closeSync(fd);}
}
const rawPairs=[];
function pair(label,a,b){
 const left=Buffer.isBuffer(a)?a:Buffer.from(a,'utf8');
 const right=Buffer.isBuffer(b)?b:Buffer.from(b,'utf8');
 requireThat(left.equals(right),'raw pair '+label);
 rawPairs.push({label,bytes:left.length,sha256:hash(left)});
}
function equalTree(a,b,path='$'){
 jsonNodes++;requireThat(typeof a===typeof b&&Array.isArray(a)===Array.isArray(b),'JSON type '+path);
 if(a===null||b===null||typeof a!=='object'){requireThat(Object.is(a,b),'JSON scalar '+path);return;}
 const ka=Object.keys(a), kb=Object.keys(b);
 requireThat(JSON.stringify(ka)===JSON.stringify(kb),'complete JSON keys '+path);
 for(const k of ka)equalTree(a[k],b[k],path+'/'+k);
}
function classifyNative(r,label){
 requireThat(r&&typeof r==='object'&&!Array.isArray(r),'native object '+label);
 requireThat(JSON.stringify(Object.keys(r).sort())===JSON.stringify(['chunk_id','exit_code','original_token_count','output','wall_time_seconds'].sort()),'complete native fields '+label);
 requireThat(typeof r.chunk_id==='string'&&Number.isInteger(r.exit_code)&&Number.isInteger(r.original_token_count)&&typeof r.wall_time_seconds==='number'&&typeof r.output==='string','native field types '+label);
 return {label,chunk_id:r.chunk_id,exit_code:r.exit_code,original_token_count:r.original_token_count,wall_time_seconds:r.wall_time_seconds,output_bytes:Buffer.byteLength(r.output),output_sha256:hash(r.output)};
}
function lines(buffer,start,end){return (buffer.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[]).slice(start-1,end).join('');}
const inputRaw=read(OWN+'INPUT_PINS.json'),inputs=JSON.parse(inputRaw);
const expectedPaths=[...SOURCE_NAMES.map(x=>SOURCE+x),...OLD];
requireThat(JSON.stringify(inputs.files.map(x=>x.path))===JSON.stringify(expectedPaths),'fixed twelve input identities/order');
const files=new Map();
for(const row of inputs.files){
 requireThat(Number.isSafeInteger(row.bytes)&&/^[0-9a-f]{64}$/.test(row.sha256),'pin schema');
 const b=read(row.path);requireThat(b.length===row.bytes&&hash(b)===row.sha256,'input pin');files.set(row.path,b);
}
record('fixed_input_files_received',12);
record('all_fixed_input_raw_utf8_and_same_fd_eof_received');
const sourceTotal=SOURCE_NAMES.reduce((s,x)=>s+files.get(SOURCE+x).length,0);
requireThat(sourceTotal===164497&&inputs.source_packet_total_bytes===sourceTotal,'source byte census');
record('source_packet_physical_bytes',sourceTotal);
requireThat(hash(files.get(SOURCE+'SHA256SUMS'))==='c358c30c3f348460535febb257455d41cac313570f69a1140c4ca5a2175c739d','assigned source seal');
requireThat(JSON.stringify(fs.readdirSync(SOURCE).sort())===JSON.stringify([...SOURCE_NAMES].sort()),'source six files');
const manifest=files.get(SOURCE+'SHA256SUMS').toString('utf8'),manifestLines=manifest.trimEnd().split('\n'),seen=new Set();
requireThat(manifest.endsWith('\n')&&manifestLines.length===5,'source nonself manifest shape');
for(const l of manifestLines){
 const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);
 requireThat(m&&SOURCE_NAMES.slice(0,5).includes(m[2])&&!seen.has(m[2]),'source unique nonself leaf');
 seen.add(m[2]);requireThat(hash(files.get(SOURCE+m[2]))===m[1],'source manifest bytes');
}
record('source_nonself_payload_count',5);record('source_complete_file_count',6);
const localRaw=read(OWN+'LOCAL_READ_RETURNS.json'),local=JSON.parse(localRaw);
const primaryRaw=read(OWN+'PRIMARY_RETURNS.json'),primary=JSON.parse(primaryRaw);
const findingRaw=read(OWN+'FINDINGS.json'),findings=JSON.parse(findingRaw);
const origin=read(OWN+'ORIGIN_AND_SCOPE.md'),review=read(OWN+'REVIEW.md');
for(const [name,b,v] of [['INPUT_PINS.json',inputRaw,inputs],['LOCAL_READ_RETURNS.json',localRaw,local],['PRIMARY_RETURNS.json',primaryRaw,primary],['FINDINGS.json',findingRaw,findings]]){
 pair('own canonical JSON '+name,b,JSON.stringify(v,null,2)+'\n');
}
requireThat(local.records.length===8,'local native census');
const localMap=new Map(local.records.map(x=>[x.name,x]));requireThat(localMap.size===8,'unique local names');
record('independent_complete_documentary_native_records',local.records.map(x=>{
 requireThat(typeof x.request.cmd==='string','literal documentary request');
 requireThat(x.actual_return.exit_code===0&&!x.actual_return.output.startsWith('Warning: truncated output'),'current native success/untruncated');
 return classifyNative(x.actual_return,x.name);
}));
requireThat(primary.calls.length===2,'independent primary census');
for(const x of primary.calls)requireThat(typeof x.name==='string'&&x.request&&typeof x.actual_return==='string','complete primary request and return');
record('independent_primary_browser_calls',2);
const nativeBytes=files.get(SOURCE+'NATIVE_READS.json'),webBytes=files.get(SOURCE+'PRIMARY_RETURNS.json'),receiptBytes=files.get(SOURCE+'DOCUMENTARY_RECEIPT.json');
const native=JSON.parse(nativeBytes),web=JSON.parse(webBytes),receipt=JSON.parse(receiptBytes);
for(const [name,bytes,value,recordName] of [
 ['NATIVE_READS.json',nativeBytes,native,'native_full'],
 ['PRIMARY_RETURNS.json',webBytes,web,'primary_full'],
 ['DOCUMENTARY_RECEIPT.json',receiptBytes,receipt,'receipt_full'],
]){
 const nr=localMap.get(recordName).actual_return;
 pair('new full native output '+name,nr.output,bytes);
 equalTree(value,JSON.parse(nr.output),name);
}
record('complete_source_json_trees_received',3);
requireThat(Array.isArray(native)&&native.length===9&&Array.isArray(web)&&web.length===4&&!Array.isArray(receipt),'source archive top-level shapes');
const authorNative=[];
for(const x of native){
 requireThat(JSON.stringify(Object.keys(x))===JSON.stringify(['key','cmd','r']),'complete author source row schema');
 requireThat(typeof x.key==='string'&&typeof x.cmd==='string','source command data');
 requireThat(x.r.exit_code===0&&!x.r.output.startsWith('Warning: truncated output'),'original source-read success/untruncated');
 authorNative.push(classifyNative(x.r,x.key));
}
record('author_source_native_records',9);
for(const k of ['initial_four_payload_hash_native','initial_four_payload_size_native']){
 requireThat(typeof receipt[k].cmd==='string','receipt archive command');
 authorNative.push(classifyNative(receipt[k].r,k));
}
requireThat(authorNative.length===11,'author full native census');
record('author_complete_native_records',authorNative);
for(const x of web){
 requireThat(JSON.stringify(Object.keys(x))===JSON.stringify(['key','req','r']),'complete source browser row');
 requireThat(typeof x.key==='string'&&x.req&&typeof x.r==='string','complete browser request/result');
}
record('author_browser_calls_received',web.map(x=>({key:x.key,return_bytes:Buffer.byteLength(x.r),return_sha256:hash(x.r)})));
requireThat(web[1].r.includes('Failed to fetch https://www.sciencedirect.com/science/article/pii/S0020019003002990: (403) Forbidden'),'publisher403');
requireThat(web[2].r.includes('which is not safe to open (non-retryable error)')&&web[2].r.includes('Failed to fetch https://citeseerx.ist.psu.edu/document?doi=fe5b38db97966cdda508ba9c9a33eb6caafe5982'),'unsafe redirected source failure');
record('both_failed_primary_body_returns_retained_no_retry');
requireThat(receipt.source_native_records===9&&receipt.primary_native_call_objects===4&&receipt.retained_failures.length===2,'receipt source census');
record('old_source_execution_census_received_not_rerun',{source_local:9,browser:4,failed_body_opens:2});
const partial=[];
requireThat(receipt.author_text_checks.length===4,'four author readback metadata rows');
for(let i=0;i<4;i++){
 const name=SOURCE_NAMES[i],b=files.get(SOURCE+name),s=b.toString('utf8'),r=receipt.author_text_checks[i];
 const expectedKeys=['name','command','exit_code','chunk_id','whole_text_matches_authored_payload','output_chars',...(i>=2?['decoded_values_equal']:[])];
 requireThat(JSON.stringify(Object.keys(r))===JSON.stringify(expectedKeys),'exact partial readback schema');
 requireThat(r.name===name&&r.exit_code===0&&typeof r.command==='string'&&typeof r.chunk_id==='string'&&r.whole_text_matches_authored_payload===true,'reported author flags preserved');
 requireThat(r.output_chars===s.length,'current physical text char count');
 requireThat(!Object.hasOwn(r,'output')&&!Object.hasOwn(r,'r'),'absent complete historical native remains absent');
 if(i>=2){
  requireThat(r.decoded_values_equal===true,'author decoded result remains TRUE');
  pair('current parsed source JSON one-LF '+name,b,JSON.stringify(JSON.parse(s),null,2)+'\n');
  equalTree(JSON.parse(s),JSON.parse(JSON.stringify(JSON.parse(s))),'current serialization '+name);
 }
 partial.push({name,chunk_id:r.chunk_id,historical_authored_text_equality_reported:true,historical_decoded_equality_reported:i>=2?true:null,historical_full_stdout_received:false,current_physical_chars:s.length,current_physical_bytes:b.length});
}
record('four_historical_readback_metadata_rows_preserved',partial);
requireThat(receipt.freeze.includes('Final seal/manifest tool returns remain session-held'),'missing source final natives explicitly retained');
record('source_final_seal_native_not_invented');
const selectors=[
 [OLD[0],1,1000,true],[OLD[1],1,1000,true],[OLD[2],1,40,false],[OLD[3],269,306,false],[OLD[2],103,153,false],
];
const selected=selectors.map(([p,a,b,full])=>{const s=lines(files.get(p),a,b);if(full)requireThat(Buffer.from(s).equals(files.get(p)),'declared full original');return s;});
for(let i=0;i<5;i++)pair('author exact original range '+(i+1),native[i+4].r.output,selected[i]);
pair('independent combined five originals plus two full contracts',localMap.get('old_originals').actual_return.output,selected.join('')+files.get(OLD[4]).toString('utf8')+files.get(OLD[5]).toString('utf8'));
record('old_exact_read_ranges_received',selectors.map(([path,start,end,full_file],i)=>({path,start,end,full_file,bytes:Buffer.byteLength(selected[i])})));
record('full_contract_documents_received',2);
const first4=SOURCE_NAMES.slice(0,4);
const sha=first4.map(n=>hash(files.get(SOURCE+n))+'  '+n+'\n').join('');
pair('historical four-file hash output',receipt.initial_four_payload_hash_native.r.output,sha);
const wc=first4.map(n=>String(files.get(SOURCE+n).length).padStart(6,' ')+' '+n+'\n').join('')+'160353 total\n';
pair('historical four-file size output',receipt.initial_four_payload_size_native.r.output,wc);
record('historical_four_payload_phase_received_as_data_not_current_census');
const four=Buffer.concat(['DESK.md','READ_SCOPE.md','DOCUMENTARY_RECEIPT.json','SHA256SUMS'].map(n=>files.get(SOURCE+n)));
pair('whole independent source prose receipt and seal native',localMap.get('source_desk').actual_return.output,four);
const counts={directions:4,new_literals:0,closed_literal_increment:0,pilots:0,pilot_requests:0,admissions:0,reserves:0};
equalTree(receipt.counts,counts,'author zero counts');equalTree(findings.negative_lifecycle,counts,'independent zero counts');
requireThat(findings.verdict==='ACCEPT_BOUNDED_ZERO_LITERAL_DESK'&&findings.open_findings===0&&['critical','major','minor'].every(k=>Array.isArray(findings[k])&&findings[k].length===0),'bounded finding census');
record('bounded_zero_literal_lifecycle',counts);
requireThat(local.display_limit.actual_local_native_truncated===false&&local.display_limit.complete_native_and_browser_records_retained===true&&localMap.get('old_originals').actual_return.chunk_id==='04a65e','display/native limits kept distinct');
record('aggregate_display_limit_preserved_complete_underlying_records');
requireThat(origin.includes(Buffer.from('not blind'))&&review.includes(Buffer.from('historical')),'origin/boundary disclosures');
record('science_runs',0);record('author_program_executions',0);record('host_runtime_queries',0);record('builds_or_grants',0);record('central_or_git_mutations',0);
record('all_raw_pairs',rawPairs);record('raw_pair_count',rawPairs.length);record('raw_pair_bytes_total',rawPairs.reduce((s,x)=>s+x.bytes,0));record('complete_json_node_comparisons',jsonNodes);
process.stdout.write(JSON.stringify({kind:'FRESH23_DOCUMENTARY_INDEPENDENT_INTAKE',verdict:'PASS_DOCUMENTARY_ONLY',assertion_count:assertions,named_check_count:Object.keys(checks).length,checks,limits:'Documentary reception only, not source/scientific execution, universal novelty exclusion, manuscript gate or host runtime acceptance. Four partial old readbacks and absent final natives are not invented; two original body-fetch failures are retained.'},null,2)+'\n');
