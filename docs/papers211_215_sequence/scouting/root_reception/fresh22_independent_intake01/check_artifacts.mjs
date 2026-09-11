// Documentary intake only. Never execute archived commands or scientific code.
import fs from 'node:fs';
import crypto from 'node:crypto';

const SOURCE='docs/papers211_215_sequence/scouting/finite_residual_fresh22/';
const OWN='docs/papers211_215_sequence/scouting/root_reception/fresh22_independent_intake01/';
const SOURCE_NAMES=['DESK.md','READ_SCOPE.md','NATIVE_READS.json','PRIMARY_RETURNS.json','DOCUMENTARY_RECEIPT.json','SHA256SUMS'];
const OLD=[
 'docs/papers157_161_sequence/scouting/combinatorial/SCOUT.md',
 'docs/papers162_166_sequence/scouting/replacement_posets_languages/SCOUT.md',
 'docs/papers162_166_sequence/scouting/word_combinatorial/SCOUT.md',
 'docs/papers204_208_sequence/scouting/finite_systems_twenty_first/SCOUT_REPORT.md',
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
const inputRaw=read(OWN+'INPUT_PINS.json'), inputs=JSON.parse(inputRaw);
const expectedPaths=[...SOURCE_NAMES.map(x=>SOURCE+x),...OLD];
requireThat(JSON.stringify(inputs.files.map(x=>x.path))===JSON.stringify(expectedPaths),'fixed 12 input identities and order');
const files=new Map();
for(const row of inputs.files){
 requireThat(Number.isSafeInteger(row.bytes)&&/^[0-9a-f]{64}$/.test(row.sha256),'pin schema');
 const b=read(row.path);requireThat(b.length===row.bytes&&hash(b)===row.sha256,'pin '+row.path);files.set(row.path,b);
}
record('fixed_input_files_received',12);
record('all_fixed_input_raw_utf8_and_same_fd_eof_received');
const sourceTotal=SOURCE_NAMES.reduce((s,x)=>s+files.get(SOURCE+x).length,0);
requireThat(sourceTotal===194057&&inputs.source_packet_total_bytes===sourceTotal,'source bytes');
record('source_packet_physical_bytes',sourceTotal);
requireThat(hash(files.get(SOURCE+'SHA256SUMS'))==='2ed5e9fe06302bd7d7897b483b17f5d5b9cc937cf96c69affdb23e131291cd3d','assigned author manifest hash');
const sourceEntries=fs.readdirSync(SOURCE).sort();
requireThat(JSON.stringify(sourceEntries)===JSON.stringify([...SOURCE_NAMES].sort()),'source complete physical census');
const sourceManifest=files.get(SOURCE+'SHA256SUMS').toString('utf8');
const sourceManifestLines=sourceManifest.trimEnd().split('\n');
requireThat(sourceManifestLines.length===5&&sourceManifest.endsWith('\n'),'source manifest shape');
const seen=new Set();
for(const l of sourceManifestLines){
 const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);
 requireThat(m&&SOURCE_NAMES.slice(0,5).includes(m[2])&&!seen.has(m[2]),'source unique nonself leaf');
 seen.add(m[2]);requireThat(hash(files.get(SOURCE+m[2]))===m[1],'source manifest pin');
}
record('source_nonself_payload_count',5);record('source_complete_file_count',6);
const localRaw=read(OWN+'LOCAL_READ_RETURNS.json'),local=JSON.parse(localRaw);
const primaryRaw=read(OWN+'PRIMARY_RETURNS.json'),primary=JSON.parse(primaryRaw);
const findingRaw=read(OWN+'FINDINGS.json'),findings=JSON.parse(findingRaw);
const origin=read(OWN+'ORIGIN_AND_SCOPE.md'),review=read(OWN+'REVIEW.md');
for(const [name,b,v] of [['INPUT_PINS.json',inputRaw,inputs],['LOCAL_READ_RETURNS.json',localRaw,local],['PRIMARY_RETURNS.json',primaryRaw,primary],['FINDINGS.json',findingRaw,findings]]){
 pair('own canonical JSON '+name,b,JSON.stringify(v,null,2)+'\n');
}
requireThat(local.records.length===13,'local record census');
const localMap=new Map(local.records.map(x=>[x.name,x]));requireThat(localMap.size===13,'unique local labels');
const localNatives=local.records.map(x=>{requireThat(typeof x.request.cmd==='string','literal current documentary request');return classifyNative(x.actual_return,'independent '+x.name);});
record('independent_complete_documentary_native_records',localNatives);
requireThat(primary.calls.length===3,'independent browser calls');
for(const x of primary.calls)requireThat(typeof x.name==='string'&&x.request&&typeof x.actual_return==='string','browser request and complete return');
record('independent_primary_browser_calls',3);
const nativeBytes=files.get(SOURCE+'NATIVE_READS.json');
const webBytes=files.get(SOURCE+'PRIMARY_RETURNS.json');
const receiptBytes=files.get(SOURCE+'DOCUMENTARY_RECEIPT.json');
const native=JSON.parse(nativeBytes),web=JSON.parse(webBytes),receipt=JSON.parse(receiptBytes);
for(const [name,bytes,value,recordName] of [
 ['NATIVE_READS.json',nativeBytes,native,'native_full'],
 ['PRIMARY_RETURNS.json',webBytes,web,'primary_full'],
 ['DOCUMENTARY_RECEIPT.json',receiptBytes,receipt,'source_receipt'],
]){
 const original=localMap.get(recordName).actual_return;
 requireThat(original.exit_code===0,'fresh source read success '+name);
 pair('new full native output '+name,original.output,bytes);
 equalTree(value,JSON.parse(original.output),name);
}
record('complete_source_json_trees_received',3);
requireThat(Array.isArray(native)&&native.length===8&&Array.isArray(web)&&web.length===4&&!Array.isArray(receipt),'source archive top-level shapes');
const archivedNatives=[];
for(const x of native){
 requireThat(JSON.stringify(Object.keys(x))===JSON.stringify(['key','cmd','r']),'native archive full row schema');
 requireThat(typeof x.key==='string'&&typeof x.cmd==='string','native archive identities');
 archivedNatives.push(classifyNative(x.r,x.key));
}
for(const name of ['target_absence_native','payload_size_native','initial_four_payload_hash_native']){
 requireThat(typeof receipt[name].cmd==='string','receipt literal command');
 archivedNatives.push(classifyNative(receipt[name].r,name));
}
record('author_complete_native_records',archivedNatives);
requireThat(archivedNatives.length===11,'author complete native census');
for(const x of web){
 requireThat(JSON.stringify(Object.keys(x))===JSON.stringify(['key','req','r']),'web archive complete schema');
 requireThat(typeof x.key==='string'&&typeof x.req==='object'&&typeof x.r==='string','web request result fields');
}
record('author_browser_calls_received',web.map(x=>({key:x.key,return_bytes:Buffer.byteLength(x.r),return_sha256:hash(x.r)})));
requireThat(native[0].r.exit_code===2&&native[0].r.output.includes('literature')&&native[0].r.output.includes('truncated'),'original missing directory and truncation');
record('author_initial_filename_failure_retained');
requireThat(web[2].r.includes('Failed to fetch https://faculty.valpo.edu/lpudwell/papers/popstacks.pdf: (400) Timeout fetching'),'original body timeout');
record('author_pdf_body_timeout_retained');
requireThat(receipt.packet_value_reception.length===2,'partial historical metadata rows');
const serialization=[];
for(const [i,name] of ['NATIVE_READS.json','PRIMARY_RETURNS.json'].entries()){
 const r=receipt.packet_value_reception[i], bytes=files.get(SOURCE+name),text=bytes.toString('utf8'),v=JSON.parse(text);
 requireThat(r.path===name&&r.authored_packet_exact_text_equal===false&&r.decoded_return_values_equal===true,'historical flags retained '+name);
 requireThat(JSON.stringify(Object.keys(r.native).sort())===JSON.stringify(['chunk_id','exit_code','original_token_count'].sort()),'partial metadata not complete native');
 requireThat(r.read_chars===text.length,'historical read character count matches current physical text');
 const single=JSON.stringify(v,null,2)+'\n',double=single+'\n';
 requireThat(text!==single&&text===double,'current physical two-linefeed serialization');
 equalTree(v,JSON.parse(single),'current serialization '+name);
 serialization.push({path:name,historical_authored_packet_exact_text_equal:false,historical_decoded_return_values_equal:true,historical_full_stdout_received:false,current_physical_equals_parsed_plus_one_lf:false,current_physical_equals_parsed_plus_two_lf:true,current_physical_chars:text.length});
}
record('two_historical_raw_false_values_and_missing_full_native_preserved',serialization);
const ranges=[[195,233],[1,110],[1,90],[1,110]];
const selected=ranges.map(([a,b],i)=>lines(files.get(OLD[i]),a,b));
for(let i=0;i<4;i++){
 requireThat(native[i+4].r.exit_code===0,'archived selected history successful');
 pair('author historical selected range '+(i+1),native[i+4].r.output,selected[i]);
}
pair('independent combined four selected ranges plus two full contracts',localMap.get('old_originals').actual_return.output,selected.join('')+files.get(OLD[4]).toString('utf8')+files.get(OLD[5]).toString('utf8'));
record('original_selected_prose_ranges_received',ranges.map(([start,end],i)=>({path:OLD[i],start,end,bytes:Buffer.byteLength(selected[i])})));
record('full_contract_documents_received',2);
const first4=SOURCE_NAMES.slice(0,4);
const wc=first4.map(n=>String(files.get(SOURCE+n).length).padStart(6,' ')+' '+SOURCE+n+'\n').join('')+'189805 total\n';
pair('historical four-payload wc output',receipt.payload_size_native.r.output,wc);
const sha=first4.map(n=>hash(files.get(SOURCE+n))+'  '+n+'\n').join('');
pair('historical four-payload hash output',receipt.initial_four_payload_hash_native.r.output,sha);
requireThat(receipt.target_absence_native.r.exit_code===0&&receipt.target_absence_native.r.output==='','historical absence native DATA only');
record('historical_absence_command_received_not_rerun');
pair('independent full desk reread',localMap.get('desk_reread').actual_return.output,files.get(SOURCE+'DESK.md'));
const prefix=Buffer.concat(['DESK.md','READ_SCOPE.md','DOCUMENTARY_RECEIPT.json','SHA256SUMS'].map(n=>files.get(SOURCE+n)));
const combined=Buffer.from(localMap.get('desk_receipt').actual_return.output,'utf8');
pair('four-source-document prefix of mixed source/instruction native',combined.subarray(0,prefix.length),prefix);
record('mixed_source_instruction_native_compared_only_for_declared_source_prefix');
const sourceCounts={directions:4,new_literals:0,pilots:0,pilot_requests:0,papers:0,reserves:0,closed_literal_increment:0};
equalTree(receipt.counts,sourceCounts,'source counts');
equalTree(findings.negative_lifecycle,sourceCounts,'independent counts');
requireThat(findings.verdict==='ACCEPT_BOUNDED_ZERO_LITERAL_DESK'&&findings.open_findings===0&&['critical','major','minor'].every(x=>Array.isArray(findings[x])&&findings[x].length===0),'bounded verdict with no substantive findings');
record('bounded_zero_literal_lifecycle',sourceCounts);
requireThat(local.orchestration_failure.returned_error.includes('ReferenceError: TextEncoder is not defined'),'new display failure retained');
record('independent_display_failure_retained_no_science');
requireThat(local.control_refresh_limit.full_native_retained_here===false&&local.control_refresh_limit.observed_warning.includes('truncated'),'instruction truncation not invented full native');
record('instruction_only_refresh_partial_limit_preserved');
requireThat(origin.includes(Buffer.from('not blind'))&&review.includes(Buffer.from('historical')),'written boundary disclosures');
record('science_runs',0);record('author_program_executions',0);record('host_runtime_queries',0);record('builds_or_grants',0);record('central_or_git_mutations',0);
record('all_raw_pairs',rawPairs);
record('raw_pair_count',rawPairs.length);
record('raw_pair_bytes_total',rawPairs.reduce((n,x)=>n+x.bytes,0));
record('complete_json_node_comparisons',jsonNodes);
process.stdout.write(JSON.stringify({kind:'FRESH22_DOCUMENTARY_INDEPENDENT_INTAKE',verdict:'PASS_DOCUMENTARY_ONLY',assertion_count:assertions,named_check_count:Object.keys(checks).length,checks,limits:'Not a scientific replay, proof by enumeration, global source clearance, manuscript review, host runtime audit or lifecycle mutation. Historical missing native stdout and failed/truncated returns remain unavailable as described.'},null,2)+'\n');
