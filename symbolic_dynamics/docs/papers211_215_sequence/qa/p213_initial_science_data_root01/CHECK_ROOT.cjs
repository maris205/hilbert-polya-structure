'use strict';
// Root fixed original DATA reception. No producer, Python, source import,
// control-derived host path, canonical target or strict-run path is executed/read.
const fs=require('node:fs');
const make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs');
const R='docs/papers211_215_sequence/qa/p213_initial_science_data_root01/';
const I='docs/papers211_215_sequence/qa/p213_initial_science_data_audit01/';
const Q='docs/papers211_215_sequence/qa/';
const spec=JSON.parse(fs.readFileSync(R+'INPUT_SPEC.json','utf8'));
const own=['INPUT_SPEC.json','ROOT_READS_NATIVE.json','REPLAY_NATIVE.json','CHECK_ROOT.cjs'];
const allowed=new Set([...spec.external.map(x=>x.path),...own.map(n=>R+n)]);
const r=make(allowed),read=p=>r.read(p),json=p=>JSON.parse(read(p).toString('utf8'));
const pairs=[];function pair(label,a,b){r.need(Buffer.isBuffer(a)&&Buffer.isBuffer(b)&&a.equals(b),'ENTIRE_RAW_EQUAL '+label);pairs.push({label,bytes:a.length,sha256:r.sha(a)});}
for(const p of allowed)read(p);
r.need(r.equal(json(R+'INPUT_SPEC.json'),spec),'ENTIRE_BOOTSTRAP_SPEC');
for(const p of spec.external)r.need(read(p.path).length===p.bytes&&r.sha(read(p.path))===p.sha256,'EXACT_WHOLE_CURRENT_INPUT_PIN '+p.path);
r.need(r.sha(read(Q+'p213_initial_science_enabled_root01/READ_FIXED.cjs'))===spec.readerPin,'ENTIRE_REUSED_READER_PIN');
const entries=fs.readdirSync(I,{withFileTypes:true});r.need(r.equal(entries.map(e=>e.name).sort(),spec.independentNames)&&entries.every(e=>e.isFile()&&!e.isSymbolicLink()),'EXACT_28_PHYSICAL_AUDIT_FILES');
const seal=read(I+'SHA256SUMS'),rows=seal.toString('utf8').split('\n');r.need(rows.pop()===''&&r.sha(seal)===spec.independentSeal,'EXACT_ENTIRE_INDEPENDENT_SEAL');
const payloads=[];for(const line of rows){const m=line.match(/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/);r.need(!!m&&m[2]!=='SHA256SUMS'&&!payloads.some(p=>p.name===m[2])&&spec.independentNames.includes(m[2]),'STRICT_DISTINCT_NONSELF_PAYLOAD');const b=read(I+m[2]);r.need(r.sha(b)===m[1],'WHOLE_FROZEN_PAYLOAD');payloads.push({name:m[2],bytes:b.length,sha256:m[1]});}
r.need(payloads.length===27&&r.equal(payloads.map(p=>p.name),spec.independentNames.filter(n=>n!=='SHA256SUMS')),'COMPLETE_SORTED_NONSELF_CENSUS');
r.need(payloads.reduce((n,p)=>n+p.bytes,0)===spec.independentPayloadBytes,'COMPLETE_PAYLOAD_BYTE_CENSUS');
const replay=json(R+'REPLAY_NATIVE.json').records;
r.need(replay.length===3,'EXACT_THREE_ROOT_DATA_CALLS');
for(const [index,cmd,chunk]of [[0,'CHECK_DATA.cjs','4dcc30'],[1,'CHECK_NEGATIVE.cjs','a8314c'],[2,'CLOSE.cjs --final','68568e']]){
 const e=replay[index];r.need(r.equal(e.request,{cmd:'node '+I+cmd,workdir:'/root/autodl-tmp/symbolic_dynamics',max_output_tokens:100000}),'ENTIRE_ROOT_DATA_REQUEST');
 r.need(e.result.exit_code===0&&e.result.chunk_id===chunk&&!('session_id'in e.result)&&!e.result.output.startsWith('Warning: truncated output'),'ACTUAL_COMPLETE_ROOT_DATA_RETURN');
 r.need(r.equal(Object.keys(e.result).sort(),['chunk_id','wall_time_seconds','exit_code','original_token_count','output'].sort()),'ALL_NATIVE_RETURN_FIELDS');
}
const original=json(I+'CHECK_NATIVE.json'),negative=json(I+'NEGATIVE_NATIVE.json'),preclose=json(I+'CLOSING_NATIVE.json');
for(const [e,cmd,chunk]of [[original,'CHECK_DATA.cjs','a18585'],[negative,'CHECK_NEGATIVE.cjs','dd57ff'],[preclose,'CLOSE.cjs','1c3194']]){
 r.need(r.equal(e.request,{cmd:'node '+I+cmd,workdir:'/root/autodl-tmp/symbolic_dynamics',max_output_tokens:100000}),'ENTIRE_ORIGINAL_AUDIT_REQUEST');
 r.need(e.native.exit_code===0&&e.native.chunk_id===chunk&&!('session_id'in e.native)&&!e.native.output.startsWith('Warning: truncated output'),'ACTUAL_ORIGINAL_COMPLETE_RETURN');
 r.need(r.equal(Object.keys(e.native).sort(),['chunk_id','wall_time_seconds','exit_code','original_token_count','output'].sort()),'ALL_ORIGINAL_RETURN_FIELDS');
}
pair('original entire DATA stdout vs documentary canonical',Buffer.from(original.native.output),read(I+'DOCUMENTARY_CANONICAL.txt'));
pair('root entire DATA replay vs original native',Buffer.from(replay[0].result.output),Buffer.from(original.native.output));
pair('root entire DATA replay vs documentary canonical',Buffer.from(replay[0].result.output),read(I+'DOCUMENTARY_CANONICAL.txt'));
pair('root entire negative replay vs original native',Buffer.from(replay[1].result.output),Buffer.from(negative.native.output));
const d=JSON.parse(original.native.output),n=JSON.parse(negative.native.output),c=JSON.parse(preclose.native.output),rd=JSON.parse(replay[0].result.output),rn=JSON.parse(replay[1].result.output),rc=JSON.parse(replay[2].result.output);
r.need(d.status==='PASS_INDEPENDENT_INITIAL_CAPTURE_CONTROL_AND_BOUNDED_SCIENCE_DATA'&&d.documentary_checks===5757&&d.control.checks===36788&&d.science.checks===736244&&d.science.source_assertions_reconstructed===25015&&d.key_count===53&&d.total_read_bytes===4219676,'COMPLETE_ACTUAL_DATA_SCOPE');
r.need(n.status==='PASS_IN_MEMORY_NEGATIVE_DATA_CONTROLS'&&n.total===41&&n.controls===23&&n.scientific===15&&n.parsers===3&&n.checks===274&&n.key_count===10&&n.findings.length===41&&n.findings.every(f=>f.rejected===true),'ALL_ACTUAL_NEGATIVE_REJECTIONS');
r.need(c.status==='PASS_DOCUMENTARY_CLOSURE'&&c.phase==='PRESEAL_26_PAYLOADS'&&c.checks===1620&&c.key_count===75,'ORIGINAL_PRESEAL_IS_NOT_FINAL');
r.need(rc.status==='PASS_DOCUMENTARY_CLOSURE'&&rc.phase==='FINAL_27_PAYLOADS_28_FILES'&&rc.checks===1888&&rc.key_count===77&&rc.original_current_key_comparisons===236&&rc.final_nonself_payloads===27,'ACTUAL_ROOT_FINAL_LAYOUT_SCOPE');
const fail=json(I+'ATTEMPT01_NATIVE.json'),middle=json(I+'ATTEMPT02_NATIVE.json');
r.need(fail.native.exit_code===1&&fail.native.chunk_id==='1d3228'&&middle.native.exit_code===0&&middle.native.chunk_id==='7f7531','PRESERVED_FAILED_AND_INTERMEDIATE_ACTUALS');
const fd=JSON.parse(fail.native.output),md=JSON.parse(middle.native.output);
r.need(fd.status==='HOLD_INDEPENDENT_DATA_AUDIT_FAILURE'&&md.status==='PASS_INDEPENDENT_INITIAL_CAPTURE_CONTROL_AND_BOUNDED_SCIENCE_DATA','FAILURE_NOT_RECLASSIFIED');
let oldKeys=0;for(const [label,value]of [['independent DATA',d],['independent negative',n],['independent preseal',c],['failed DATA',fd],['intermediate DATA',md],['root DATA',rd],['root negative',rn],['root final',rc]]){
 r.need(value.keys.length===value.key_count,'WHOLE_PREVIOUS_KEY_CENSUS');
 for(const k of value.keys){r.need(allowed.has(k.path),'EXACT_FIXED_OLD_KEY_PATH');const current=r.keys.get(k.path);r.need(r.equal(k,current),'ENTIRE_PREVIOUS_KEY '+label+' '+k.path);for(const name of ['lstat_before','fd_before','fd_after','lstat_after']){r.need(r.equal(Object.keys(k[name]).sort(),r.fields.slice().sort()),'ALL_TEN_BIGINT_DECIMAL_FIELDS');for(const v of Object.values(k[name]))r.need(typeof v==='string'&&/^(0|-?[1-9][0-9]*)$/.test(v),'LOSSLESS_INTEGER_STRING');}oldKeys++;}
}
r.need(oldKeys===376,'ALL_236_ORIGINAL_AND_140_ROOT_KEY_OCCURRENCES');
const acceptance=json(I+'ACCEPTANCE.json'),findings=json(I+'FINDINGS.json');
r.need(acceptance.status==='ACCEPT_EXACT_INITIAL_CONTROL_AND_BOUNDED_SCIENCE_DATA_PENDING_ROOT_RECEPTION'&&r.equal(acceptance.current_open_findings,{science:0,control:0,documentary:0}),'SCOPED_NONSELF_ACCEPTANCE');
r.need(findings.scientific_findings_open===0&&findings.control_findings_open===0&&findings.documentary_findings_open===0&&findings.completed_audit_corrections.length===4&&findings.completed_audit_corrections.every(x=>x.status.startsWith('CLOSED_')),'COMPLETE_FINDING_AND_FAILURE_CENSUS');
for(const flag of ['source_author_contributed_to_audit','manuscript_review_A','manuscript_review_B','canonical_adopted','strict_pair_complete','new_science_execution_in_audit','new_pilot','host_or_control_derived_paths_queried','old_probe_rerun'])r.need(acceptance[flag]===false,'NO_NEW_AUTHORITY_OR_LATER_GATE '+flag);
const rawSpecs=acceptance.accepted_originals;r.need(rawSpecs.length===3&&rawSpecs.every(p=>p.path.startsWith(Q+'p213_initial_science_run01/')),'THREE_ORIGINALS_ONLY');
for(const p of rawSpecs)r.need(allowed.has(p.path)&&read(p.path).length===p.bytes&&r.sha(read(p.path))===p.sha256,'EVERY_WHOLE_ORIGINAL_RAW_BYTE_PIN');
r.need(rawSpecs.reduce((s,p)=>s+p.bytes,0)===2451590,'ORIGINAL_TOTAL_RAW_BYTES');
const parser=require('../p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs');
r.need(r.sha(read(Q+'p213_minimal_observer_probe_audit01/LOSSLESS_JSON.cjs'))==='9d6e081b7c8940f6730cc41c62bfc67862738eb49ded8f4021b6875583120471','REUSED_PURE_LOSSLESS_PARSER_PIN');
const controlRaw=read(Q+'p213_initial_science_run01/runtime_control.bin');r.need(controlRaw.every(x=>x<128),'WHOLE_CONTROL_ASCII');const parsed=parser.parseIntegerJSON(controlRaw.toString('ascii'));
pair('root entire type-preserving integer control roundtrip',Buffer.from(parser.canonicalIntegerJSON(parsed.data)+'\n'),controlRaw);
r.need(r.equal(parsed.counts,d.control_integer_counts),'ALL_CONTROL_NODE_AND_EXACT_INTEGER_COUNTS');
r.need(d.control.moduleRows===326&&d.control.statFields===6440&&d.control.mapRows===284&&d.control.mapFileRows===225&&d.control.mapSpecialRows===59&&d.control.completeFileRecords===139&&d.control.absentFileRecords===2,'COMPLETE_CONTROL_ROW_CENSUS');
r.need(d.science.lines===18485&&d.science.carriers===30&&d.science.states===461&&d.science.words===17990&&d.science.two_site===18&&d.science.degree_two===18&&d.science.captured_orbit_points===873&&d.science.accepted_interval_cell_points===435,'COMPLETE_BOUNDED_SCIENCE_CENSUS');
const rootReads=json(R+'ROOT_READS_NATIVE.json').records,coverage=[];
for(const e of rootReads){const m=e.request.cmd.match(/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_./-]+)$/);r.need(!!m&&e.result.exit_code===0&&allowed.has(m[3]),'ALL_ACTUAL_ROOT_READ_SCOPES');const lines=read(m[3]).toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[],expected=Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join(''));pair('whole actual root source range '+e.result.chunk_id,Buffer.from(e.result.output),expected);coverage.push({path:m[3],start:Number(m[1]),end:Number(m[2]),chunk:e.result.chunk_id,bytes:expected.length,reused_saved_return:spec.reusedSavedReadChunks.includes(e.result.chunk_id)});}
r.need(coverage.length===spec.rootReadCount&&coverage.filter(x=>x.reused_saved_return).length===1,'COMPLETE_CURRENT_AND_REUSED_ROOT_SOURCE_READS');
const structure=[];for(const [label,value]of [['DATA',d],['NEGATIVE',n],['ROOT_FINAL',rc],['ACCEPTANCE',acceptance],['FINDINGS',findings]]){let objects=0,arrays=0,scalars=0;function walk(x){if(Array.isArray(x)){arrays++;for(const y of x)walk(y);}else if(x!==null&&typeof x==='object'){objects++;for(const [k,y]of Object.entries(x)){r.need(typeof k==='string','JSON_KEY');walk(y);}}else{scalars++;if(typeof x==='number')r.need(Number.isFinite(x),'FINITE_DOCUMENTARY_NUMBER');}}walk(value);structure.push({label,objects,arrays,scalars});}
process.stdout.write(JSON.stringify({status:'PASS_ROOT_ORIGINAL_INITIAL_CONTROL_AND_BOUNDED_SCIENCE_DATA',checks:r.checks,key_count:r.keys.size,total_read_bytes:r.total,independent_package:{payloads:27,files:28,payload_bytes:spec.independentPayloadBytes,physical_bytes:spec.independentPayloadBytes+seal.length,seal:{bytes:seal.length,sha256:r.sha(seal)}},historical_key_occurrences:oldKeys,raw_pairs:pairs,raw_pair_bytes:pairs.reduce((s,p)=>s+p.bytes,0),root_read_coverage:coverage,complete_documentary_structure_census:structure,control_counts:parsed.counts,science_scope:d.science,scientific_execution:false,host_or_control_path_query:false,canonical_adoption:false,strict_pair:false,new_operation_grant:false,keys:[...r.keys.values()]},null,2)+'\n');
