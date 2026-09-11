'use strict';
// Read-only finite documentary closure. No producer or prior census execution.
const fs=require('node:fs'),crypto=require('node:crypto'),{load}=require('./CHECK.cjs');
const O='docs/papers211_215_sequence/qa/p213_author_strict_pair_data_audit01/';
const R='docs/papers211_215_sequence/qa/p213_author_strict_pair_execution_root01/';
const PRE=['ATTEMPTS_NATIVE.json','CHECK.cjs','CHECK_NATIVE.json','CLOSE.cjs','FINDINGS.json','HANDOFF.md','INPUT_NATIVE.json','NEGATIVE.cjs','NEGATIVE_NATIVE.json','ORIGIN.md','PAIR_DATA.cjs','RESULT.json'].sort();
const final=process.argv.length===3&&process.argv[2]==='--sealed';
if(!(process.argv.length===3&&['--preseal','--sealed'].includes(process.argv[2])))throw Error('exact read-only closure mode');
const f=load(),make=require('../p213_initial_science_enabled_root01/READ_FIXED.cjs'),names=[...PRE,...(final?['CLOSING_NATIVE.json','CLOSING_RESULT.json']:[])].sort(),all=[...names,...(final?['SHA256SUMS']:[])];
const r=make(new Set(all.map(n=>O+n))),{need,read,keys,equal,sha}=r;all.forEach(n=>read(O+n));
need(equal(fs.readdirSync(O).sort(),all.slice().sort()),'exact nonself packet inventory');
const json=n=>JSON.parse(read(O+n));let old=0,rawPairs=0;
function raw(a,b,m){need(a.equals(b),'complete RAW '+m);rawPairs++;}
function inputKey(k,label){f.full(k,label);old++;}
const main=json('CHECK_NATIVE.json'),result=json('RESULT.json');
need(main.request.cmd==='node '+O+'CHECK.cjs'&&main.request.workdir===process.cwd()&&main.result.chunk_id==='cf087d'&&main.result.exit_code===0&&!main.result.session_id,'actual complete final independent checker original');
raw(Buffer.from(main.result.output),read(O+'RESULT.json'),'whole actual audit stdout/result');
need(result.status==='PASS_INDEPENDENT_NEW_STRICT_PAIR_DATA_PENDING_ROOT_RECEPTION'&&result.keys.length===103,'whole current audit status/keys');
result.keys.forEach(k=>inputKey(k,'final audit'));
const neg=json('NEGATIVE_NATIVE.json'),nv=JSON.parse(neg.result.output);
need(neg.request.cmd==='node '+O+'NEGATIVE.cjs'&&neg.request.workdir===process.cwd()&&neg.result.chunk_id==='9cdcdb'&&neg.result.exit_code===0&&!neg.result.session_id,'actual current negative original');
need(nv.status==='PASS_ACTUAL_NEGATIVE_PAIR_DATA_CONTROLS'&&nv.negative_cases===29&&nv.findings.length===29&&nv.findings.every(x=>x.rejected===true),'all actual current negative DATA cases');
nv.keys.forEach(k=>inputKey(k,'current negative'));
const attempts=json('ATTEMPTS_NATIVE.json'),delta=attempts.exact_checker_delta,oldNeg=attempts.earlier_negative,oldReport=JSON.parse(oldNeg.result.output);
need(attempts.failed_audit.result.chunk_id==='f374ee'&&attempts.failed_audit.result.exit_code===1&&JSON.parse(attempts.failed_audit.result.output).failure.message==='entire grant fields','actual failed uniform grant-field schema preserved');
need(oldNeg.result.chunk_id==='e62b4b'&&oldNeg.result.exit_code===0&&oldReport.negative_cases===29,'earlier successful negative original preserved');
need(delta.path===O+'CHECK.cjs'&&typeof delta.before==='string'&&typeof delta.after==='string'&&delta.before!==delta.after&&delta.old_source.split(delta.before).length===2,'one exact whole-line checker delta');
raw(Buffer.from(delta.old_source.replace(delta.before,delta.after)),f.read(O+'CHECK.cjs'),'complete old/current checker exact correction');
const oldChecker=oldReport.keys.find(k=>k.path===O+'CHECK.cjs');
need(Buffer.byteLength(delta.old_source)===oldChecker.byte_count&&sha(Buffer.from(delta.old_source))===oldChecker.sha256,'entire old checker bytes bound to actual old current key');
for(const k of oldReport.keys)if(k.path!==O+'CHECK.cjs')inputKey(k,'unchanged earlier-negative input');
need(attempts.own_source_read.result.chunk_id==='958145'&&attempts.own_source_read.result.exit_code===0,'actual complete personally inspected source read');
raw(Buffer.from(attempts.own_source_read.result.output),Buffer.concat([f.read(O+'PAIR_DATA.cjs'),Buffer.from(delta.old_source),f.read(O+'NEGATIVE.cjs')]),'entire three-source original read');
need(attempts.complete_grants_read.result.chunk_id==='929718'&&attempts.complete_grants_read.result.exit_code===0,'actual complete two-grant read');
raw(Buffer.from(attempts.complete_grants_read.result.output),Buffer.concat([f.read(R+'GRANT.replay01.json'),f.read(R+'GRANT.replay02.json')]),'entire actual two-grant read');
const initial=json('INPUT_NATIVE.json'),early=initial.early,ev=JSON.parse(early.result.output);
need(early.result.chunk_id==='a04905'&&early.result.exit_code===0&&ev.results.length===2&&ev.results.every(x=>x.checks===36788),'actual earlier whole-control DATA check');
ev.keys.forEach(k=>inputKey(k,'early whole-control source/raw input'));
need(initial.earlier_read_archive_gaps.full_originals_claimed_inside_packet===false&&initial.aborted_read09.saved_native_original_available===false,'explicit missing historical read originals, no fabricated receipt');
for(const k of keys.values())if(f.keys.has(k.path))need(equal(k,f.keys.get(k.path)),'whole separately reread current owned input');
if(final){
 const n=json('CLOSING_NATIVE.json'),v=json('CLOSING_RESULT.json');
 need(n.request.cmd==='node '+O+'CLOSE.cjs --preseal'&&n.result.exit_code===0&&!n.result.session_id&&v.status==='PASS_PAIR_DATA_NONSELF_PRECLOSE','actual preseal native boundary');
 raw(Buffer.from(n.result.output),read(O+'CLOSING_RESULT.json'),'whole actual preseal stdout/result');
 for(const k of v.keys){need(keys.has(k.path)&&equal(k,keys.get(k.path)),'whole old/current preseal payload key');old++;}
 raw(Buffer.from(names.map(n=>sha(read(O+n))+'  '+n+'\n').join('')),read(O+'SHA256SUMS'),'entire14-payload nonself manifest');
}
const payloads=names.map(n=>({name:n,bytes:read(O+n).length,sha256:sha(read(O+n))}));
process.stdout.write(JSON.stringify({status:final?'PASS_PAIR_DATA_FINAL_NONSELF_CLOSURE':'PASS_PAIR_DATA_NONSELF_PRECLOSE',phase:final?'FINAL_14_PAYLOADS':'PRESEAL_12_PAYLOADS',checks:r.checks+f.r.checks,current_input_key_count:f.keys.size,whole_old_current_keys:old,complete_raw_pairs:rawPairs,key_count:keys.size,keys:[...keys.values()],payloads,payload_bytes:payloads.reduce((s,x)=>s+x.bytes,0),seal:final?{bytes:read(O+'SHA256SUMS').length,sha256:sha(read(O+'SHA256SUMS'))}:null,source_execution:false,host_queries:false,new_grant:false,manuscript_review:false},null,2)+'\n');
