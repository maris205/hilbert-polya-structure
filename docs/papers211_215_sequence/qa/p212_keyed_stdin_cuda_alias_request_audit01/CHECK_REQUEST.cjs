'use strict';
// Request-only documentary checker. No subprocess, evaluated command, Python,
// source parser/import, target observation, or embedded destination access.
const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert/strict');
const ROOT = '/root/autodl-tmp/symbolic_dynamics/';
const Q = 'docs/papers211_215_sequence/qa/';
const B = Q + 'p212_keyed_stdin_cuda_alias_request_preparation01/';
const A = Q + 'p212_keyed_stdin_cuda_alias_request_audit01/';
const S = Q + 'p212_keyed_stdin_cuda_alias_source_delta01/';
const SR = Q + 'p212_keyed_stdin_cuda_alias_source_root01/';
const SA = Q + 'p212_keyed_stdin_cuda_alias_source_audit01/';
const TR = Q + 'p212_trusted_product_boundary_root01/';
const OLD = Q + 'p212_keyed_stdin_observation_root01/';
const FAIL = Q + 'p212_keyed_stdin_failed_observation_root01/';
const INPUTS = [SR+'RECEPTION.md',SR+'SHA256SUMS',S+'observe.py',S+'FRONTIER.json',
  S+'AUTHORIZATION.disabled.json',S+'SHA256SUMS',SA+'REPORT.md',SA+'FINDINGS.json',
  SA+'SHA256SUMS',TR+'DECISION.json',TR+'RECEPTION.md',OLD+'RELOCATED_TRUST_DECISION.json',
  OLD+'REQUEST.json',FAIL+'RECEPTION.md',FAIL+'SHA256SUMS'];
const PAYLOADS = ['ARGV.prospective.json','AUTHORIZATION.disabled.json','AUTHORIZATION.prospective.json',
  'CHECK_DOCUMENTS.cjs','CHECK_NATIVE.json','CHECK_RESULT.json','CLOSING_NATIVE.json','CONTRACT.md',
  'HANDOFF.md','INPUT_KEYS_NATIVE.json','PREFIX.proposed.json','PROSPECTIVE_BYTES.json',
  'PROSPECTIVE_PINS_NATIVE.json','READBACK_NATIVE.json','REQUEST.disabled.json','REQUEST.prospective.json',
  'TRANSFORMATION.json'];
const OWN = ['SCOPE.md','READS_NATIVE_01.json','READS_NATIVE_02.json','AUTHOR_REPLAY_NATIVE.json','CHECK_REQUEST.cjs'];
const allowed = new Set([...INPUTS,...PAYLOADS.map(n=>B+n),B+'SHA256SUMS',...OWN.map(n=>A+n)]);
const FIELDS = ['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs','birthtimeNs'];
const rawBodies = new Map(), keys = new Map(), pairs = [];
let checks = 0;
const ok = (v,m) => { checks++; assert(v,m); };
const eq = (x,y,m) => { checks++; assert.deepStrictEqual(x,y,m); };
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const fields = s => Object.fromEntries(FIELDS.map(n=>[n,String(s[n])]));
function physicalRead(path) {
  ok(allowed.has(path),'explicit existing document selection before any filesystem operation');
  const first = fs.lstatSync(path,{bigint:true});
  ok(first.isFile() && first.nlink===1n && first.size>=0n && first.size<=5000000n,'bounded physical single-link document');
  const fd = fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let raw;
  try {
    eq(fields(fs.fstatSync(fd,{bigint:true})),fields(first),'opening same fd');
    raw = fs.readFileSync(fd);
    eq(fields(fs.fstatSync(fd,{bigint:true})),fields(first),'closing same fd');
  } finally { fs.closeSync(fd); }
  eq(fields(fs.lstatSync(path,{bigint:true})),fields(first),'closing physical endpoint');
  eq(BigInt(raw.length),first.size,'whole document bytes');
  return {raw,key:{path,bytes:raw.length,sha256:sha(raw),fields:fields(first)}};
}
function read(path) {
  ok(allowed.has(path),'selected document, never an embedded destination');
  if (!rawBodies.has(path)) { const r=physicalRead(path); rawBodies.set(path,r.raw); keys.set(path,r.key); }
  return rawBodies.get(path);
}
const get = n => read(B+n);
const parse = p => JSON.parse(read(p).toString('utf8'));
const json = n => parse(B+n);
const canon = v => Buffer.from(JSON.stringify(v,null,2)+'\n','utf8');
const pin = p => ({bytes:read(p).length,sha256:sha(read(p))});
const ref = p => ({path:ROOT+p,pin:pin(p)});
function pair(label,actual,expected,details={}) {
  eq(actual,expected,label+' raw bytes');
  pairs.push({label,bytes:expected.length,sha256:sha(expected),...details});
}
function settled(response,label) {
  eq(response.exit_code,0,label+' successful native return');
  ok(!response.session_id && typeof response.output==='string',label+' complete no-session return');
  ok(!response.output.startsWith('Warning: truncated output'),label+' no leading truncation header');
}
for (const path of allowed) read(path);

// The full frozen proposal, not a transitive source-packet recertification.
eq(fs.readdirSync(B).sort(),[...PAYLOADS,'SHA256SUMS'].sort(),'exact physical 17-payload packet inventory');
eq(sha(get('SHA256SUMS')),'c7a4349d3ff0021d52ef2d88fb8d695b09a1e108b2c4db45f104c877b311edba','root supplied proposal seal');
const manifest = get('SHA256SUMS').toString('ascii');
ok(manifest.endsWith('\n') && !manifest.includes('\r'),'manifest LF');
const lines = manifest.slice(0,-1).split('\n');
eq(lines.length,17,'complete payload denominator');
const manifestNames = [];
for (const line of lines) {
  const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);
  ok(m!==null,'strict one-level manifest record');
  ok(PAYLOADS.includes(m[2]),'manifest name chosen before read');
  manifestNames.push(m[2]); eq(sha(get(m[2])),m[1],'manifest body '+m[2]);
}
eq(manifestNames,PAYLOADS,'complete ordered nonself manifest');
eq(pin(SR+'RECEPTION.md'),{bytes:6626,sha256:'7d763ca0bda72085c5deabe1f888452bf44fcdfe30b2e012b537b30f81898901'},'accepted source receipt');
eq(sha(read(SR+'SHA256SUMS')),'4c302b5c5eb67892ed846b4cfc33c9aa3d70478bd78fe457a3cea88357ca5def','accepted root seal');
eq(pin(S+'observe.py'),{bytes:22128,sha256:'cbacb868df156a422a619531720f0488ea0b1944972b188f2e6246e2cfc62408'},'accepted observer bytes untouched');
eq(pin(S+'FRONTIER.json'),{bytes:77865,sha256:'55ffe83e365c9ab07f84543b3b2ab0f2438a5c0e17966363fd5d18b5dfcf01cc'},'accepted full frontier untouched');
eq(sha(read(S+'SHA256SUMS')),'32c3c6da8cc47ef0adf96723a98ec8244ae004990582effdca407a49537aa10d','accepted source seal input');
eq(sha(read(SA+'SHA256SUMS')),'62779c39dd68545e4f650dd79d13960693839289a669a29faff83cede2492747','separate source audit seal input');
eq(sha(get('HANDOFF.md')),'5cd50dc2f1b4dc3c5369deb80bccd9720704b1ac9c9fc1d0677a96aa8d7ba0bd','root supplied handoff');
const sourceCensus=parse(SA+'FINDINGS.json');
eq(sourceCensus.auditor,'/root/p212_cuda_delta_audit','source acceptance belongs to separate auditor');
eq(sourceCensus.census,{Blocker:0,Major:0,Minor:0},'existing source finding scope only');

// Canonical authorization is ASCII JSON with exact int/bool types and final LF.
const d=json('PREFIX.proposed.json'), z=json('AUTHORIZATION.disabled.json'), a=json('AUTHORIZATION.prospective.json');
const argv=json('ARGV.prospective.json'), r=json('REQUEST.prospective.json'), disabled=json('REQUEST.disabled.json');
const transform=json('TRANSFORMATION.json'), prospective=json('PROSPECTIVE_BYTES.json');
for (const name of PAYLOADS.filter(n=>n.endsWith('.json'))) pair('canonical JSON '+name,get(name),canon(json(name)));
const authBytes=get('AUTHORIZATION.prospective.json');
ok(authBytes.every(c=>c<128) && authBytes.length<=32768 && authBytes[authBytes.length-1]===10,'source canonical ASCII argument bound including LF');
function safeJSON(value) {
  if (typeof value==='number') ok(Number.isSafeInteger(value),'exact integral JSON number, no NaN/infinity/float');
  else if (Array.isArray(value)) value.forEach(safeJSON);
  else if (value!==null && typeof value==='object') Object.values(value).forEach(safeJSON);
}
safeJSON(a);
eq(Object.keys(a),['schema','enabled','status','provenance','source_receipt','trust_receipt','frontier'],'exact seven-key consumed interface');
eq(a.schema,'p212-independent-preprobe-observer-authorization-v1'); eq(a.enabled,true);
eq(a.status,'ROOT_BOUND_FINITE_OBSERVATION_ONLY');
const provenance={schema:'p212-trusted-product-boundary-v1',assumption:'ordinary_product_observer_bash_env_bootstrap',product_startup_attested:false,claim:'finite_received_keys_and_discrete_downstream_observations'};
eq(a.provenance,provenance,'fixed ordinary trust, not startup attestation');
const controls={source_receipt:ref(SR+'RECEPTION.md'),trust_receipt:ref(TR+'RECEPTION.md'),frontier:ref(S+'FRONTIER.json')};
for (const role of Object.keys(controls)) {
  eq(a[role],controls[role],'fixed complete control '+role);
  eq(Object.keys(a[role]),['path','pin']); eq(Object.keys(a[role].pin),['bytes','sha256']);
  ok(Number.isSafeInteger(a[role].pin.bytes) && a[role].pin.bytes>=0 && a[role].pin.bytes<=1048576,'control bound');
  ok(/^[a-f0-9]{64}$/.test(a[role].pin.sha256),'control digest spelling');
}
const enabledFromDisabled={...z,enabled:true,status:'ROOT_BOUND_FINITE_OBSERVATION_ONLY'};
eq(enabledFromDisabled,a,'only two enabled/status deltas');
eq(z.enabled,false); eq(z.status,'HOLD_EXACT_REQUEST_INDEPENDENT_AUDIT_AND_ROOT_GRANT');
const sourceTemplate=parse(S+'AUTHORIZATION.disabled.json');
for (const role of Object.keys(controls)) { eq(sourceTemplate[role].path,a[role].path); eq(sourceTemplate[role].pin,null); sourceTemplate[role].pin=a[role].pin; }
sourceTemplate.enabled=true; sourceTemplate.status='ROOT_BOUND_FINITE_OBSERVATION_ONLY'; eq(sourceTemplate,a,'existing source interface fully resolved, no extra field');
eq(d.provenance,provenance); eq(d.controls,controls);
eq(d.accepted_source_reception,{...controls.source_receipt,packet_manifest_sha256:sha(read(SR+'SHA256SUMS'))});
eq(d.observer_source,{...ref(S+'observe.py'),lf_lines:436,source_manifest_sha256:sha(read(S+'SHA256SUMS')),self_attested:false});
eq(d.independent_source_audit,{...ref(SA+'REPORT.md'),manifest_sha256:sha(read(SA+'SHA256SUMS'))});
eq(d.historical_trust_decision,ref(TR+'DECISION.json')); eq(d.historical_prefix_relocation_automatic,false);

// Explicit prefix and shell quotation, compared as data without a shell parser.
const env={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'};
const prefix=['/usr/bin/env','-i',...Object.entries(env).map(([k,v])=>k+'='+v),'/usr/bin/python3.10','-I','-S','-B',ROOT+S+'observe.py'];
eq(d.environment_after_env,env); eq(d.exact_native_prefix,prefix); eq(argv,[...prefix,authBytes.toString('ascii')]); eq(argv.length,16);
eq(Buffer.from(argv[15],'ascii'),authBytes,'single whole canonical final argument');
const stdin=ROOT+Q+'p212_keyed_stdin_input01/empty.stdin';
const capture='/root/symbolic-dynamics-p212-cuda-alias-observation-20260910-01';
const future=ROOT+Q+'p212_keyed_stdin_cuda_alias_observation_root01/';
// These four constants are comparison strings only and are NOT in allowed.
for (const path of [stdin,capture,capture+'/stdout.raw',capture+'/stderr.raw',future]) ok(!allowed.has(path),'forbidden destination not a reader operand');
const operands=[...argv,stdin,capture+'/stdout.raw',capture+'/stderr.raw'];
ok(operands.every(s=>typeof s==='string' && !s.includes("'") && !s.includes('\0')),'all operands fit exact ordinary single-quote representation');
const quote=s=>"'"+s+"'";
const expectedCmd='umask 077\nset -C\nexec '+argv.map(quote).join(' ')+' < '+quote(stdin)+' > '+quote(capture+'/stdout.raw')+' 2> '+quote(capture+'/stderr.raw')+'\n';
eq(r,{cmd:expectedCmd,workdir:ROOT.slice(0,-1),shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:2000},'whole exact tool request including bootstrap/redirection order');
eq(d.shell,{path:'/bin/bash',login:false,tty:false,cwd:ROOT.slice(0,-1)});
const old=parse(OLD+'RELOCATED_TRUST_DECISION.json'), oldRequest=parse(OLD+'REQUEST.json');
eq(env,old.environment_after_env); eq(d.shell,old.shell); eq(d.scope.bounds,old.scope.bounds); eq(d.scope.bound_limits,old.scope.bound_limits);
eq({...oldRequest,cmd:r.cmd},r,'no changed non-command tool option');
eq(prefix.slice(0,-1),old.exact_native_prefix.slice(0,-1),'only observer spelling changes in native prefix');
eq(d.stdin.path,stdin); eq(old.stdin.path,stdin); eq(d.stdin.required_content,{bytes:0,sha256:'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'});
eq(d.stdin.actual_current_key,null); eq(d.stdin.observed_or_prepared_by_this_packet,false); eq(d.stdin.inherited_fd0_identity_attested,false); eq(d.stdin.null_device_equivalence,false);
eq(d.stdin.prior_evidence,{...ref(FAIL+'RECEPTION.md'),partial_single_pass_empty_regular_native_fields_and_empty_content_received:true,complete_two_pass_native_key_received:false,old_grant_consumed:true});
eq(d.capture,{directory:capture,stdout:capture+'/stdout.raw',stderr:capture+'/stderr.raw',pathnames_only:true,absence_queried:false,allocated:false,preparation_native:null,capacity_observed:null});
eq(disabled.cmd,null); eq(disabled.operational_authorization,false); eq(disabled.old_grant_reusable,false);
eq(disabled.requires,['independent exact prospective-byte/request audit','root request reception','separate exact private capture preparation','fresh one-invocation root grant']);

// All source-derived frontier data remain documentary, never live path inputs.
const frontier=parse(S+'FRONTIER.json'); pair('full frontier canonical bytes',read(S+'FRONTIER.json'),canon(frontier));
const memberships=frontier.targets.filter(t=>t.mode==='membership');
eq([frontier.targets.length,frontier.allowed_components.length,memberships.length,memberships.reduce((n,t)=>n+t.expected_names.length,0),frontier.closure_gaps.length],[164,207,5,292,8]);
eq(d.scope.frontier.path,controls.frontier.path); eq(d.scope.frontier.pin,controls.frontier.pin);
eq([d.scope.frontier.target_count,d.scope.frontier.component_count,d.scope.frontier.membership_sets,d.scope.frontier.membership_names,d.scope.frontier.closure_gaps],[164,207,5,292,8]);
eq(d.scope.bounds,{max_targets:384,max_components:768,max_native_calls:60000,max_all_read_bytes:536870912,max_captured_source_bytes:8388608,max_output_bytes:134217728,chunk_bytes:65536,max_one_file_bytes:134217728,max_one_captured_file_bytes:1048576,max_members_per_directory:320,max_link_count:40,max_component_steps:1024,max_path_bytes:4096,max_link_text_bytes:4096,max_member_name_bytes:255,max_authorization_argument_bytes:32768});
eq(d.scope.internal_target_passes,2); eq(d.scope.maximum_proposed_observer_invocations,1);
for (const k of ['actual_invocations_by_this_proposal','automatic_retries','observer_spawned_children','author_probes','scientific_runs','builds']) eq(d.scope[k],0,k+' remains zero');
eq(d.scope.git_ssh_external,false); eq(d.future_runtime_acceptance,false); eq(d.author_probes_authorized,false); eq(d.external_status,'HOLD_EXTERNAL');
eq(d.old_strict_product_startup,'UNSATISFIED_NOT_CLOSED_OR_RELABELLED'); eq(d.old_dev_mask_failure,'UNSATISFIED_NOT_REPAIRED');

// Compatibility landmarks corroborate the complete manual source reading.
const source=read(S+'observe.py').toString('utf8'); eq(source.split('\n').length-1,436);
for (const token of ["HERE = QA + '/p212_keyed_stdin_cuda_alias_source_delta01'","SOURCE_RECEIPT = QA + '/p212_keyed_stdin_cuda_alias_source_root01/RECEPTION.md'","TRUST_RECEIPT = QA + '/p212_trusted_product_boundary_root01/RECEPTION.md'","return json.dumps(value, ensure_ascii=True, indent=2, allow_nan=False) + '\\n'","need(canonical(value).encode('ascii') == raw, 'noncanonical JSON/duplicates')","need(len(sys.argv) == 2 and len(sys.argv[1].encode('utf-8')) <= 32768,","for pass_number in (1, 2):","need(data.mask & 0xFFF == 0xFFF,"]) ok(source.includes(token),'accepted interface landmark '+token);
ok(source.indexOf('import ctypes')<source.indexOf('def main()'),'imports precede gate; no refusal test');

eq(transform.operational_authorization,false); eq(transform.source_frozen,true); eq(transform.allowed_changes_to_source_or_frontier,[]);
eq(transform.future_directory_string_only,future); eq(transform.no_future_path_query_or_allocation_here,true);
eq(transform.disabled_auth_to_prospective.only_changed_fields,{enabled:{from:false,to:true},status:{from:'HOLD_EXACT_REQUEST_INDEPENDENT_AUDIT_AND_ROOT_GRANT',to:'ROOT_BOUND_FINITE_OBSERVATION_ONLY'}});
const names=['AUTHORIZATION','ARGV','REQUEST'];
eq(prospective.entries.length,3); eq(transform.prospective_copies.length,3);
for (let i=0;i<3;i++) {
  const name=names[i], input=B+name+'.prospective.json';
  eq(prospective.entries[i],{source:input,future_path_string_only:future+name+'.json',...pin(input)});
  eq(transform.prospective_copies[i],{from:name+'.prospective.json',to:future+name+'.json'});
}
eq(d.activation,{independent_exact_request_audit_received:false,root_request_reception:false,capture_prepared:false,grant:null,enabled_files_materialized:false,future_directory_string_only:future,exact_copies:names.map(n=>n+'.prospective.json => '+n+'.json'),no_further_semantic_change_allowed:true});

// Receive the complete actual author evidence, without executing embedded code.
const initial=json('INPUT_KEYS_NATIVE.json'); settled(initial.response,'author initial keys');
eq(initial.response.chunk_id,'79877a'); const initialResult=JSON.parse(initial.response.output);
eq(initialResult.keys.map(k=>k.path),INPUTS,'all fifteen initial keys, no unselected operand');
for (const k of initialResult.keys) eq(keys.get(k.path),k,'full initial ten-field key '+k.path);
const authorNative=json('CHECK_NATIVE.json'), authorResult=json('CHECK_RESULT.json');
settled(authorNative.checker_read.response,'author full checker read'); settled(authorNative.run.response,'author checker run');
eq(authorNative.run.response.chunk_id,'a5803d'); eq(authorResult.checks,347); eq(authorResult.keys.length,27);
pair('author complete checker read',Buffer.from(authorNative.checker_read.response.output,'utf8'),get('CHECK_DOCUMENTS.cjs'));
pair('author canonical result raw return',Buffer.from(authorNative.run.response.output,'utf8'),get('CHECK_RESULT.json'));
for (const k of authorResult.keys) { ok(allowed.has(k.path),'author key explicitly selected'); eq(keys.get(k.path),k,'full author key'); }
const prospectiveNative=json('PROSPECTIVE_PINS_NATIVE.json'); settled(prospectiveNative.response,'author prospective pins'); eq(prospectiveNative.response.chunk_id,'cdd154');
pair('author prospective pins raw return',Buffer.from(prospectiveNative.response.output,'utf8'),get('PROSPECTIVE_BYTES.json'));
const readbacks=json('READBACK_NATIVE.json'); eq(readbacks.records.length,3);
const expectedReadbackNames=['PREFIX.proposed.json','CONTRACT.md','AUTHORIZATION.prospective.json','AUTHORIZATION.disabled.json','ARGV.prospective.json','REQUEST.prospective.json','REQUEST.disabled.json','TRANSFORMATION.json','PROSPECTIVE_BYTES.json','HANDOFF.md'];
const seenReadbacks=[]; let readbackBytes=0;
for (const x of readbacks.records) {
  settled(x.response,'author proposal readback');
  ok(x.paths.every(p=>expectedReadbackNames.some(n=>p===B+n)),'fixed substantive readback inputs');
  eq(x.request.cmd,'cat '+x.paths.join(' '),'exact historical read request');
  const raw=Buffer.concat(x.paths.map(read)); pair('author complete proposal readback',Buffer.from(x.response.output,'utf8'),raw,{paths:x.paths});
  seenReadbacks.push(...x.paths); readbackBytes+=raw.length;
}
eq([...seenReadbacks].sort(),expectedReadbackNames.map(n=>B+n).sort(),'all ten substantive documents exactly once');
const closing=json('CLOSING_NATIVE.json'); settled(closing.response,'author historical preclosing'); eq(closing.response.chunk_id,'5ded93');
const closeResult=JSON.parse(closing.response.output);
eq([closeResult.checks,closeResult.preclosing_payloads,closeResult.original_keys,closeResult.raw_pairs,closeResult.raw_bytes,closeResult.keys.length],[436,16,27,5,55277,31]);
eq(closeResult.raw_bytes,readbackBytes+get('CHECK_DOCUMENTS.cjs').length+get('CHECK_RESULT.json').length,'all historical closing raw bytes');
for (const k of closeResult.keys) { ok(allowed.has(k.path),'closing input chosen explicitly'); eq(keys.get(k.path),k,'full historical closing key'); }
// Its historical 16-file checker is NOT rerun against the final 18-file layout.
const replay=parse(A+'AUTHOR_REPLAY_NATIVE.json').record; settled(replay.result,'fresh author documentary replay');
eq(replay.request.cmd,'node '+B+'CHECK_DOCUMENTS.cjs');
pair('fresh replay versus author canonical',Buffer.from(replay.result.output,'utf8'),get('CHECK_RESULT.json'));
pair('fresh replay versus original native',Buffer.from(replay.result.output,'utf8'),Buffer.from(authorNative.run.response.output,'utf8'));

// Original reviewer native read renderings are reconciled, not merely cited.
let numberedReads=0, partialReads=0;
const reviewerRecords=[...parse(A+'READS_NATIVE_01.json').records,...parse(A+'READS_NATIVE_02.json').records];
eq(reviewerRecords.map(x=>x.seq),Array.from({length:35},(_,i)=>i+1),'complete actual early read/replay sequence');
function numbered(raw) { const text=raw.toString('utf8'); ok(text.endsWith('\n'),'numbered source final LF'); return Buffer.from(text.slice(0,-1).split('\n').map((line,i)=>String(i+1).padStart(6,' ')+'\t'+line+'\n').join(''),'utf8'); }
for (const item of reviewerRecords) {
  settled(item.result,'reviewer native '+item.seq);
  const m=/^nl -ba (docs\/papers211_215_sequence\/qa\/[A-Za-z0-9_./-]+)$/.exec(item.request.cmd);
  if (m) { pair('reviewer complete numbered read '+item.seq,Buffer.from(item.result.output,'utf8'),numbered(read(m[1])),{path:m[1]}); numberedReads++; }
  if (item.seq===31 || item.seq===32) {
    const path=B+(item.seq===31?'READBACK_NATIVE.json':'CLOSING_NATIVE.json');
    pair('reviewer exact seven-line native-envelope view '+item.seq,Buffer.from(item.result.output,'utf8'),Buffer.from(read(path).toString('utf8').split('\n').slice(0,7).join('\n')+'\n','utf8'));
    partialReads++;
  }
}
eq(numberedReads,25); eq(partialReads,2);

const proposalSummary={payloads:17,physical_files:18,payload_bytes:PAYLOADS.reduce((n,p)=>n+get(p).length,0),seal_sha256:sha(get('SHA256SUMS'))};
// Close every complete documentary key with another same-fd whole-byte read.
for (const [path,key] of keys) { const after=physicalRead(path); eq(after.key,key,'final full key unchanged '+path); eq(after.raw,rawBodies.get(path),'final whole body unchanged '+path); }
process.stdout.write(JSON.stringify({
  scope:'PERSONAL_NONCONTRIBUTOR_REQUEST_ONLY_REVIEW_WITH_SOURCE_AUTHOR_PARENT_DISCLOSED',
  checks,proposal:proposalSummary,
  prospective:prospective.entries,author:{initial_keys:15,checker_checks:347,checker_keys:27,historical_closing_checks:436,historical_closing_keys:31,historical_closing_raw_bytes:55277,fresh_replay_chunk:replay.result.chunk_id},
  raw_comparisons:pairs.length,raw_comparison_bytes:pairs.reduce((n,x)=>n+x.bytes,0),pairs,
  reviewer_numbered_whole_reads:numberedReads,reviewer_partial_envelope_reads:partialReads,
  document_keys:keys.size,keys:[...keys.values()],source_acceptance_reused_not_reissued:true,
  observer_or_python_or_capture_executed:false,host_private_stdin_future_paths_observed:false,operational_authorization:false
},null,2)+'\n');
