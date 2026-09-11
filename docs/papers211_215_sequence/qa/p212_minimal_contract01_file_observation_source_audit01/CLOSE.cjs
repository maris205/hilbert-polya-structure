'use strict';
// Scoped documentary closure for THIS independent package. Never execute an
// author's historical preseal checker on a later directory layout.
const fs=require('node:fs');
const {context,BASE,A,O,R,D,AN,ON,W}=require('./CHECK.cjs');
const PRE=['CHECK.cjs','CLOSE.cjs','READ_NATIVE.json','WEB_NATIVE.json','SOURCE_CLAIMS.md','FINDINGS.json','ORIGIN.md','REPORT.md','HANDOFF.md','CHECK_NATIVE.json','RESULT.json'];
const FINAL=[...PRE,'CLOSING_NATIVE.json','CLOSING_RESULT.json'];
const sealed=process.argv.length===3&&process.argv[2]==='--sealed';
const selected=sealed?[...FINAL,'SHA256SUMS']:PRE;
const c=context(selected),report={schema:'p212-eight-file-independent-documentary-closure-v1',phase:sealed?'FINAL_SEALED_LAYOUT':'PRESEAL_ELEVEN_PAYLOADS',status:'RUNNING',operation_authorized:false,host_or_future_path_observation:false,source_program_executed:false};
try {
 c.need(process.argv.length===2||sealed,'only_declared_closure_mode');
 for(const p of [...BASE,...selected.map(n=>D+'/'+n)])c.read(p);
 c.eq(fs.readdirSync(D).sort(),selected.slice().sort(),'exact_phase_directory_layout');
 report.author=c.inventory(A,AN,'8a296cda89323b49cef3a6797a3e8d75b47f0966ff9b440e2c57bc29f0415d0e',736027);
 report.original=c.inventory(O,ON,'523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40',1321223);
 const native=c.data(D+'/CHECK_NATIVE.json',true),result=c.data(D+'/RESULT.json',true);
 c.need(native.tool==='exec_command','actual_independent_check_tool');
 c.eq(native.request,{cmd:'node '+D+'/CHECK.cjs',workdir:W,max_output_tokens:100000},'complete_independent_checker_request');
 c.need(native.result.exit_code===0&&!('session_id'in native.result),'actual_independent_checker_zero');
 c.raw(Buffer.from(native.result.output),c.read(D+'/RESULT.json'),'entire_independent_stdout_and_canonical');
 c.need(result.status==='PASS_EXACT_DOCUMENTARY_SOURCE_RECEIPT_ONLY'&&result.source_program_executed===false&&result.operation_authorized===false&&result.host_or_future_path_observation===false,'only_actual_source_documentary_pass');
 c.need(result.key_count===50&&result.keys.length===50&&result.old_key_occurrences===116,'full_independent_key_census');
 for(const k of result.keys)c.oldKey(k);
 const findings=c.data(D+'/FINDINGS.json',true);
 c.eq(findings.current_source_findings,{critical:0,major:0,minor:0,open:0},'exact_source_finding_census');
 c.need(findings.verdict==='ACCEPT_EXACT_FILE_ONLY_SOURCE_ENTRY_SERIALIZER_CAPTURE_REQUEST'&&findings.operation_authorized===false&&findings.findings.length===0,'scoped_source_verdict_only');
 for(const n of ['REPORT.md','HANDOFF.md','SOURCE_CLAIMS.md','ORIGIN.md'])c.need(c.text(D+'/'+n).includes('HOLD_OPERATIONAL'),'all_reports_keep_operation_hold');
 report.checked_native={chunk_id:native.result.chunk_id,checks:result.checks,keys:result.key_count,stdout_bytes:Buffer.byteLength(native.result.output),stdout_sha256:c.hash(Buffer.from(native.result.output))};
 if(sealed) {
   const old=c.data(D+'/CLOSING_NATIVE.json',true),value=c.data(D+'/CLOSING_RESULT.json',true);
   c.need(old.tool==='exec_command','actual_preseal_tool');
   c.eq(old.request,{cmd:'node '+D+'/CLOSE.cjs',workdir:W,max_output_tokens:100000},'complete_previous_closing_request');
   c.need(old.result.exit_code===0&&!('session_id'in old.result),'actual_preseal_zero');
   c.raw(Buffer.from(old.result.output),c.read(D+'/CLOSING_RESULT.json'),'whole_actual_preseal_stdout');
   c.need(value.phase==='PRESEAL_ELEVEN_PAYLOADS'&&value.status==='PASS_INDEPENDENT_DOCUMENTARY_CLOSURE_ONLY'&&value.key_count===57,'exact_previous_closure_phase');
   for(const k of value.keys)c.oldKey(k);
   const seal=c.text(D+'/SHA256SUMS'),lines=seal.split('\n');c.need(lines.pop()==='','nonself_seal_final_lf');
   const rows=lines.map(l=>{const m=l.match(/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/);c.need(!!m,'strict_final_seal_row');return{sha256:m[1],name:m[2]};});
   c.eq(rows.map(r=>r.name),FINAL.slice().sort(),'complete_thirteen_payload_nonself_manifest');
   for(const r of rows)c.need(c.hash(c.read(D+'/'+r.name))===r.sha256,'exact_current_nonself_payload_hash');
   report.prior_closing_native={chunk_id:old.result.chunk_id,checks:value.checks,keys:value.key_count};
   report.seal=c.pin(D+'/SHA256SUMS');
 }
 report.payloads=(sealed?FINAL:PRE).slice().sort().map(n=>c.pin(D+'/'+n));
 report.payload_bytes=report.payloads.reduce((s,p)=>s+p.bytes,0);
 report.status='PASS_INDEPENDENT_DOCUMENTARY_CLOSURE_ONLY';
}catch(e){report.status='FAIL_INDEPENDENT_DOCUMENTARY_CLOSURE_ONLY';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=c.checks;report.key_count=c.keys.length;report.total_read_bytes=c.readBytes;report.json_numeric_tokens=c.jsonNumbers;report.json_structure_values=c.jsonStructures;report.raw_pairs=c.pairs;report.keys=c.keys;
process.stdout.write(JSON.stringify(report,null,2)+'\n');
