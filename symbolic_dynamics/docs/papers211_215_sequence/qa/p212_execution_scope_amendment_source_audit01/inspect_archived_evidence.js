'use strict';
// Independent documentary reads of existing saved outputs; no submitted source import/evaluation.
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics/', Q='docs/papers211_215_sequence/qa/';
let checks=0;
const eq=(a,b,m)=>{assert.deepEqual(a,b,m);checks++;}, yes=(a,m)=>{assert.ok(a,m);checks++;};
const read=p=>fs.readFileSync(ROOT+p), json=p=>JSON.parse(read(p)), pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
const EXPECTED={bytes:12501943,sha256:'1a32be6bb36dd8b4b27b9891a42876fe235bf2555a3dd9f4e36195a6ad72676c'};
const canonical='papers/212-closed-pointer-orbits/CANONICAL.json', cb=read(canonical); eq(pin(cb),EXPECTED,'canonical complete bytes');
const rows=[];
for(const [role,dir,cmd] of [['initial','p212_author_initial_01','03_verify_01'],['pair1','p212_author_pair_01','03_verify_01'],['pair2','p212_author_pair_01','03_verify_02']]) {
  const prefix=Q+'root_replays/'+dir+'/recorder/commands/'+cmd+'/', b=read(prefix+'stdout.raw'),r=json(prefix+'RECEIPT.json'),a=json(prefix+'ATTEMPT.json'),j=JSON.parse(b);
  eq(pin(b),EXPECTED,role+' full raw pin'); yes(b.equals(cb),role+' raw canonical equality'); eq(read(prefix+'stderr.raw').length,0,role+' stderr');
  eq(r.argv,a.argv,role+' exact attempted vector'); eq(r.exit_code,0,role+' real native exit'); eq(r.wrapper_exit_code,0,role+' wrapper exit'); eq(r.status,'COMPLETED',role+' state'); eq(r.streams_complete,true,role+' complete streams'); eq(r.stdout,pin(b),role+' raw binding');
  eq(r.process_group_settlement.native_returncode,0,role+' native settlement'); eq(r.process_group_settlement.quiescent,true,role+' group sample'); eq(r.process_group_settlement.remaining_members,[],role+' no sampled members'); eq(r.process_group_settlement.signals,[],role+' no interventions'); yes(r.ended_epoch>r.started_epoch,role+' elapsed');
  eq(j.summary.predicate_count,72476,role+' named checks'); eq(j.predicate_census.length,46,role+' named classes'); eq(j.predicates.length,72476,role+' named array'); eq(j.predicate_census.reduce((s,x)=>s+x.checks,0),72476,role+' census total'); eq(j.predicate_census.map(x=>x.failures),Array(46).fill(0),role+' archived census'); eq(j.summary.passed,true,role+' archived pass'); eq(j.summary.failure_ids,[],role+' archived no failures');
  eq(j.parameters.carrier_sizes,[1,2,3,4],role+' exact four boxes'); eq(j.carriers.map(x=>x.states.length),[1,16,243,4096],role+' stored original states'); eq(j.summary.state_count,4356,role+' total original states'); eq(j.coverage_limits.map(x=>x.first_core_size),[5,6,5],role+' unexercised starts'); eq(j.coverage_limits.map(x=>x.observed_group_references),[[],[],[]],role+' no empirical family data'); eq(j.coverage_limits.map(x=>x.finite_status),Array(3).fill('not_exercised_in_n_1_2_3_4'),role+' bounds');
  rows.push({role,prefix,raw:pin(b),attempt:a,receipt:r,summary:j.summary,predicate_census:j.predicate_census,parameters:j.parameters,coverage_limits:j.coverage_limits});
}
const comparisons=[];
const pair=Q+'root_replays/p212_author_pair_01/recorder/commands/';
for(const [label,left,right] of [['04_canonical_1',pair+'03_verify_01/stdout.raw',canonical],['04_canonical_2',pair+'03_verify_02/stdout.raw',canonical],['05_pair',pair+'03_verify_01/stdout.raw',pair+'03_verify_02/stdout.raw']]) {
  const a=json(pair+label+'/ATTEMPT.json'),r=json(pair+label+'/RECEIPT.json');
  eq(a.argv,['/usr/bin/cmp','--',ROOT+left,ROOT+right],label+' complete operand vector'); eq(r.argv,a.argv,label+' actual operand vector'); eq(r.exit_code,0,label+' actual exit'); eq(r.wrapper_exit_code,0,label+' wrapper');eq(read(pair+label+'/stdout.raw').length,0,label+' stdout');eq(read(pair+label+'/stderr.raw').length,0,label+' stderr');yes(read(left).equals(read(right)),label+' actual archived raw operand equality');
  comparisons.push({label,attempt:a,receipt:r,current_raw_equal:true});
}
const semantic=Q+'p212_saved_output_root_reception01/initial02/commands/02_saved_output/',sb=read(semantic+'stdout.raw'),s=JSON.parse(sb),sr=json(semantic+'RECEIPT.json');
eq(sr.stdout,pin(sb),'entire semantic output bound');eq(sr.exit_code,0,'actual semantic native exit');eq(sr.wrapper_exit_code,0,'semantic wrapper');eq(read(semantic+'stderr.raw').length,0,'semantic stderr');eq(s.semantic_checks,12375789,'distinct primitive semantic count');eq(s.scientific_producer_invocations,0,'semantic not a producer');eq(s.submitted_code_imports,0,'semantic no submitted import');eq(s.saved_stdout_bytes,EXPECTED.bytes,'semantic original byte size');eq(s.saved_stdout_sha256,EXPECTED.sha256,'semantic original full hash');eq(s.semantics.predicate_count,72476,'semantic named count');eq(s.semantics.total_states,4356,'semantic complete states');eq(s.semantics.predicate_census.length,46,'semantic named classes');eq(s.semantics.predicate_census,rows[0].predicate_census,'semantic full archived census matches');
process.stdout.write(JSON.stringify({schema:'p212-execution-scope-archived-evidence-audit-v1',status:'PASS_DOCUMENTARY_ARCHIVED_OUTPUT_FIELDS_AND_NATIVE_RECORDS',documentary_checks:checks,producer_invocations_by_this_audit:0,semantic_reconstructions_by_this_audit:0,scientific_claim:'No finite algorithm or theorem recomputation; original accepted semantics explicitly reused by root receipts.',canonical:EXPECTED,producer_rows:rows,archived_native_comparisons:comparisons,semantic_native_receipt:sr,semantic_stdout_raw_text:sb.toString('utf8')},null,2)+'\n');
