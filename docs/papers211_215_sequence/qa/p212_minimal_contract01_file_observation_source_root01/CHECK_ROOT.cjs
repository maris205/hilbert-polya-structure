'use strict';
// Root original-evidence receiver. Only fixed existing documentary files;
// no submitted source execution, embedded command execution or host queries.
const fs=require('node:fs');
const make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const R='docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_root01/';
const A='docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/';
const I='docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_source_audit01/';
const O='docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/';
const P='docs/papers211_215_sequence/qa/p212_minimal_contract01_source_root01/';
const spec=JSON.parse(fs.readFileSync(R+'INPUT_SPEC.json','utf8'));
const own=['INPUT_SPEC.json','ROOT_READS_NATIVE.json','ROOT_WEB_NATIVE.json','REPLAY_NATIVE.json','CHECK_ROOT.cjs'];
const allowed=new Set([...spec.external.map(p=>p.path),...spec.extra_docs,...own.map(n=>R+n)]);
const r=make(allowed),read=p=>r.read(p),pairs=[];
const json=p=>{const b=read(p),v=JSON.parse(b.toString('utf8'));r.need(Buffer.from(JSON.stringify(v,null,2)+'\n').equals(b),'ENTIRE_CANONICAL_JSON '+p);return v;};
const pin=(p,b)=>({path:p,bytes:b.length,sha256:r.sha(b)});
for(const p of allowed)read(p);
r.need(r.equal(json(R+'INPUT_SPEC.json'),spec),'ENTIRE_BOOTSTRAP_SPEC_RECEIVED');
for(const p of spec.external)r.need(r.equal(pin(p.path,read(p.path)),p),'ENTIRE_FIXED_EXTERNAL_PIN');
function pair(label,a,b){r.need(Buffer.isBuffer(a)&&Buffer.isBuffer(b)&&a.equals(b),'ENTIRE_RAW_PAIR '+label);pairs.push({label,bytes:a.length,sha256:r.sha(a)});}
function inventory(base,count,seal,physical){
 const b=read(base+'SHA256SUMS');r.need(b.length===seal.bytes&&r.sha(b)===seal.sha256,'EXACT_NONSELF_SEAL');
 const lines=b.toString('utf8').split('\n');r.need(lines.pop()==='','MANIFEST_FINAL_LF');
 const names=[],rows=[];
 for(const l of lines){const m=l.match(/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/);r.need(!!m&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'STRICT_DISTINCT_PAYLOAD_ROW');names.push(m[2]);const p=pin(base+m[2],read(base+m[2]));r.need(p.sha256===m[1],'WHOLE_PAYLOAD_HASH');rows.push(p);}
 r.need(names.length===count&&r.equal(names,names.slice().sort()),'EXACT_SORTED_PAYLOAD_CENSUS');
 const entries=fs.readdirSync(base,{withFileTypes:true});r.need(r.equal(entries.map(e=>e.name).sort(),[...names,'SHA256SUMS'].sort())&&entries.every(e=>e.isFile()&&!e.isSymbolicLink()),'EXACT_PHYSICAL_DIRECTORY_LAYOUT');
 const size=rows.reduce((s,p)=>s+p.bytes,b.length);r.need(size===physical,'WHOLE_PHYSICAL_BYTES');
 return {base,payloads:count,files:count+1,physical_bytes:size,seal,rows};
}
const packages=[inventory(A,19,spec.source_seal,737654),inventory(I,13,spec.independent_source_seal,1018625),inventory(O,19,{bytes:1630,sha256:'523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40'},1322853)];
const replay=json(R+'REPLAY_NATIVE.json').records,independent=json(I+'RESULT.json'),inative=json(I+'CHECK_NATIVE.json'),preseal=json(I+'CLOSING_RESULT.json'),pnative=json(I+'CLOSING_NATIVE.json');
r.need(replay.length===2&&replay.every(e=>e.tool==='exec_command'&&e.result.exit_code===0&&!('session_id'in e.result)),'TWO_ACTUAL_DOCUMENTARY_COMPLETIONS');
r.need(replay[0].result.chunk_id==='5840dd'&&replay[1].result.chunk_id==='de5827','ACTUAL_ROOT_NATIVE_IDENTITIES');
for(const [e,cmd]of [[replay[0],'CHECK.cjs'],[replay[1],'CLOSE.cjs --sealed'],[inative,'CHECK.cjs'],[pnative,'CLOSE.cjs']]){
 r.need(r.equal(e.request,{cmd:'node '+I+cmd,workdir:'/root/autodl-tmp/symbolic_dynamics',max_output_tokens:100000}),'ENTIRE_ACTUAL_NATIVE_REQUEST');
 r.need(e.result.exit_code===0&&!('session_id'in e.result)&&typeof e.result.output==='string'&&!e.result.output.startsWith('Warning: truncated output'),'COMPLETE_SUCCESSFUL_NATIVE_RETURN');
 r.need(r.equal(Object.keys(e.result).sort(),['chunk_id','exit_code','original_token_count','output','wall_time_seconds'].sort()),'ALL_ACTUAL_NATIVE_RETURN_FIELDS');
}
pair('independent documentary canonical vs original',read(I+'RESULT.json'),Buffer.from(inative.result.output));
pair('root full documentary replay vs canonical',Buffer.from(replay[0].result.output),read(I+'RESULT.json'));
pair('root full documentary replay vs actual original',Buffer.from(replay[0].result.output),Buffer.from(inative.result.output));
pair('entire independent historical preseal stdout',read(I+'CLOSING_RESULT.json'),Buffer.from(pnative.result.output));
const rootValue=JSON.parse(replay[0].result.output),finalValue=JSON.parse(replay[1].result.output);
r.need(independent.checks===13878&&independent.key_count===50&&independent.old_key_occurrences===116&&independent.raw_pairs.length===66,'EXACT_DOCUMENTARY_REPLAY_SCOPE');
r.need(finalValue.checks===10825&&finalValue.key_count===60&&finalValue.phase==='FINAL_SEALED_LAYOUT'&&finalValue.status==='PASS_INDEPENDENT_DOCUMENTARY_CLOSURE_ONLY','ACTUAL_FINAL_SEALED_CLOSURE_SCOPE');
r.need(preseal.checks===6794&&preseal.key_count===57&&preseal.phase==='PRESEAL_ELEVEN_PAYLOADS','PRESERVED_HISTORICAL_PRESEAL_SCOPE');
const reads=json(A+'READ_NATIVE.json').events,first=reads.filter(e=>e.result.chunk_id==='7b6a29');r.need(first.length===1,'EXACT_OLD_AUTHOR_INTAKE_ORIGINAL');
const authorFirst=JSON.parse(first[0].result.output),authorNative=json(A+'CHECK_NATIVE.json'),authorCloseNative=json(A+'CLOSING_NATIVE.json');
const authorCheck=JSON.parse(authorNative.result.output),authorClose=JSON.parse(authorCloseNative.result.output);
pair('entire original author documentary stdout',Buffer.from(authorNative.result.output),read(A+'DOCUMENTARY_RESULT.json'));
let oldKeys=0;
for(const [label,value]of [['author initial',authorFirst],['author check',authorCheck],['author preseal',authorClose],['independent',independent],['independent preseal',preseal],['root replay',rootValue],['root final',finalValue]]){
 r.need(value.keys.length===value.key_count,'FULL_HISTORICAL_KEY_CENSUS '+label);
 for(const k of value.keys){r.need(allowed.has(k.path),'FIXED_OLD_DOCUMENT_KEY');const current=r.keys.get(k.path);
  for(const name of ['lstat_before','fd_before','fd_after','lstat_after']){
   r.need(r.equal(Object.keys(k[name]).sort(),r.fields.slice().sort()),'EXACT_TEN_FIELDS');
   for(const x of Object.values(k[name]))r.need(typeof x==='string'&&/^-?(0|[1-9][0-9]*)$/.test(x)&&x!=='-0','EXACT_DECIMAL_FIELD');
  }
  for(const name of ['path','eof','eof_zero_return','byte_count','complete','closed','sha256','lstat_before','fd_before','fd_after','lstat_after'])r.need(r.equal(k[name],current[name]),'ALL_COMPLETE_OLD_KEY_FIELDS '+name);
  oldKeys++;
 }
}
r.need(oldKeys===333,'116_AUTHOR_107_INDEPENDENT_110_ROOT_KEYS');
const delta=json(A+'SOURCE_DELTA.json'),original=read(O+'file_keys.mjs');let offset=0;const pieces=[];
for(const e of delta.reader_edits){const x=Buffer.from(e.old_text);pair('old declared derivative span',original.subarray(e.old_byte_offset,e.old_byte_offset+x.length),x);pieces.push(original.subarray(offset,e.old_byte_offset),Buffer.from(e.new_text));offset=e.old_byte_offset+x.length;}
pieces.push(original.subarray(offset));pair('entire two-edit reader source',Buffer.concat(pieces),read(A+'file_keys.proposed.mjs.txt'));
pair('whole unchanged source-gate request',read(A+'FILE_REQUEST.proposed.json'),read(O+'FILE_REQUEST.disabled.json'));
const draft=delta.unexecuted_entry_draft;let derived=read(A+'DRAFT_ENTRY01.mjs.txt').toString('utf8').replace(draft.changes.old_finally,draft.changes.new_finally);
for(const [a,b]of draft.exact_text_replacements)derived=derived.split(a).join(b);
pair('whole preserved-draft to current-entry derivation',Buffer.from(derived),read(A+'collect_files.proposed.mjs.txt'));
const entry=json(A+'ENTRY_REQUEST.proposed.json');pair('complete capture and prospective native command',read(A+'capture.proposed.sh.txt'),Buffer.from(entry.proposed_native_request.arguments.cmd));
r.need(r.sha(read(P+'RECEPTION.md'))==='663fcfdaf3d0541acb3199f2bc31f0e55050f75b74480c025df97abbf78ac1f7','UNCHANGED_ACCEPTED_POLICY_PREMISE');
const findings=json(I+'FINDINGS.json');r.need(r.equal(findings.current_source_findings,{critical:0,major:0,minor:0,open:0})&&findings.findings.length===0&&findings.verdict==='ACCEPT_EXACT_FILE_ONLY_SOURCE_ENTRY_SERIALIZER_CAPTURE_REQUEST'&&!findings.operation_authorized,'EXACT_INDEPENDENT_SOURCE_ONLY_CENSUS');
const covered=[],excluded=[];
for(const e of json(R+'ROOT_READS_NATIVE.json').records){const m=e.request.cmd.match(/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_./-]+)$/);if(e.result.exit_code!==0){excluded.push({chunk:e.result.chunk_id,request:e.request,exit:e.result.exit_code,reason:'Actual failed documentary basename lookup; no source coverage'});continue;}r.need(!!m&&allowed.has(m[3]),'FIXED_ROOT_READ_SCOPE');const text=read(m[3]).toString('utf8'),lines=text.match(/[^\n]*\n|[^\n]+$/g)||[];const expected=Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join(''));pair('entire actual root read '+e.result.chunk_id,Buffer.from(e.result.output),expected);covered.push({path:m[3],start:Number(m[1]),end:Number(m[2]),chunk:e.result.chunk_id,bytes:expected.length});}
r.need(covered.length===spec.root_reads_expected&&excluded.length===spec.failed_root_read_count,'ALL_SUCCESSFUL_AND_FAILED_ROOT_READS_ACCOUNTED');
const web=json(R+'ROOT_WEB_NATIVE.json').records;r.need(web.length===5&&web.every(e=>typeof e.result==='string'&&e.result.length>0),'ALL_FIVE_ACTUAL_SELECTED_PRIMARY_REQUEST_RETURNS');
process.stdout.write(JSON.stringify({schema:'p212-file-only-root-original-source-receipt-v1',status:'PASS_DOCUMENTARY_ORIGINALS_ONLY_SOURCE_DECISION_IN_RECEPTION',checks:r.checks,key_count:r.keys.size,total_read_bytes:r.total,packages,historical_key_occurrences:oldKeys,raw_pairs:pairs,raw_pair_bytes:pairs.reduce((s,p)=>s+p.bytes,0),root_read_coverage:covered,excluded_reads:excluded,source_findings:findings.current_source_findings,submitted_source_executed:false,host_or_future_path_observation:false,operation_grant:false,materialization:false,scientific_acceptance:false,keys:[...r.keys.values()]},null,2)+'\n');
