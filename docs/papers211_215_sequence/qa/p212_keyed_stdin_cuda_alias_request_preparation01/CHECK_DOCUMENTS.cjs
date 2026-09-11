'use strict';
// Author-side documentary proposal checker; no subprocess, reviewed-source parse/run or embedded-path probe.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics/',Q='docs/papers211_215_sequence/qa/';
const B=Q+'p212_keyed_stdin_cuda_alias_request_preparation01/';
const INPUTS=[
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_root01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/observe.py",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/FRONTIER.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/AUTHORIZATION.disabled.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_delta01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_audit01/REPORT.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_audit01/FINDINGS.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_cuda_alias_source_audit01/SHA256SUMS",
  "docs/papers211_215_sequence/qa/p212_trusted_product_boundary_root01/DECISION.json",
  "docs/papers211_215_sequence/qa/p212_trusted_product_boundary_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_observation_root01/RELOCATED_TRUST_DECISION.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_observation_root01/REQUEST.json",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_failed_observation_root01/RECEPTION.md",
  "docs/papers211_215_sequence/qa/p212_keyed_stdin_failed_observation_root01/SHA256SUMS"
];
const OWN=['INPUT_KEYS_NATIVE.json','PREFIX.proposed.json','AUTHORIZATION.prospective.json','AUTHORIZATION.disabled.json','ARGV.prospective.json','REQUEST.prospective.json','REQUEST.disabled.json','TRANSFORMATION.json','PROSPECTIVE_BYTES.json','PROSPECTIVE_PINS_NATIVE.json','CONTRACT.md','CHECK_DOCUMENTS.cjs'];
const permitted=new Set([...INPUTS,...OWN.map(n=>B+n)]),F=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs','birthtimeNs'];
let checks=0;const bodies=new Map(),keys=new Map();const ok=(v,m)=>{checks++;assert(v,m);},equal=(x,y,m)=>{checks++;assert.deepStrictEqual(x,y,m);};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex'),shape=s=>Object.fromEntries(F.map(k=>[k,String(s[k])]));
function read(p){ok(permitted.has(p),'exact document selection before any filesystem operand');if(bodies.has(p))return bodies.get(p);
 const s=fs.lstatSync(p,{bigint:true});ok(s.isFile()&&s.nlink===1n&&s.size<10000000n,'bounded physical regular input');
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let raw;
 try{equal(shape(fs.fstatSync(fd,{bigint:true})),shape(s),'same fd');raw=fs.readFileSync(fd);equal(shape(fs.fstatSync(fd,{bigint:true})),shape(s),'closing fd');}finally{fs.closeSync(fd);}
 equal(shape(fs.lstatSync(p,{bigint:true})),shape(s),'closing endpoint');equal(BigInt(raw.length),s.size,'complete body');
 bodies.set(p,raw);keys.set(p,{path:p,bytes:raw.length,sha256:sha(raw),fields:shape(s)});return raw;
}
const get=n=>read(B+n),json=n=>JSON.parse(get(n)),parse=p=>JSON.parse(read(p)),canonical=j=>Buffer.from(JSON.stringify(j,null,2)+'\n');
for(const p of permitted)read(p);
const inputNative=json('INPUT_KEYS_NATIVE.json');ok(inputNative.response.exit_code===0&&!inputNative.response.session_id,'actual initial document keys');
const initial=JSON.parse(inputNative.response.output);equal(initial.keys.map(k=>k.path),INPUTS,'all exact 15 initial inputs');
for(const k of initial.keys)equal(keys.get(k.path),k,'full initial documentary key unchanged');
const D=json('PREFIX.proposed.json'),A=json('AUTHORIZATION.prospective.json'),Z=json('AUTHORIZATION.disabled.json'),V=json('ARGV.prospective.json'),R=json('REQUEST.prospective.json'),N=json('REQUEST.disabled.json'),T=json('TRANSFORMATION.json'),P=json('PROSPECTIVE_BYTES.json');
for(const n of OWN.filter(n=>n.endsWith('.json')))equal(get(n),canonical(json(n)),'canonical complete JSON '+n);
equal(Object.keys(A),['schema','enabled','status','provenance','source_receipt','trust_receipt','frontier'],'exact seven consumed fields');
const disabledClone=structuredClone(Z);disabledClone.enabled=true;disabledClone.status='ROOT_BOUND_FINITE_OBSERVATION_ONLY';equal(disabledClone,A,'only enabled/status changes from bound disabled argument');
equal(Z.enabled,false,'disabled false');equal(Z.status,'HOLD_EXACT_REQUEST_INDEPENDENT_AUDIT_AND_ROOT_GRANT','disabled hold');
const old= parse(Q+'p212_keyed_stdin_observation_root01/RELOCATED_TRUST_DECISION.json'),oldReq=parse(Q+'p212_keyed_stdin_observation_root01/REQUEST.json');
const source=Q+'p212_keyed_stdin_cuda_alias_source_delta01/',receipt=Q+'p212_keyed_stdin_cuda_alias_source_root01/RECEPTION.md',trust=Q+'p212_trusted_product_boundary_root01/RECEPTION.md';
const ref=p=>({path:ROOT+p,pin:{bytes:read(p).length,sha256:sha(read(p))}});
equal(A.source_receipt,ref(receipt),'new fixed already-existing receipt');equal(A.trust_receipt,ref(trust),'unchanged fixed historical trust receipt');equal(A.frontier,ref(source+'FRONTIER.json'),'new fixed frontier');
const authorDisabled=parse(source+'AUTHORIZATION.disabled.json');authorDisabled.enabled=true;authorDisabled.status='ROOT_BOUND_FINITE_OBSERVATION_ONLY';for(const role of ['source_receipt','trust_receipt','frontier'])authorDisabled[role].pin=A[role].pin;
equal(authorDisabled,A,'no uncommissioned authorization field');
equal(A.provenance,old.provenance,'unchanged explicit ordinary trust');
equal(D.provenance,A.provenance);equal(D.controls,{source_receipt:A.source_receipt,trust_receipt:A.trust_receipt,frontier:A.frontier});
equal(D.historical_prefix_relocation_automatic,false);equal(D.accepted_source_reception.path,ROOT+receipt);equal(D.accepted_source_reception.pin,A.source_receipt.pin);
equal(D.accepted_source_reception.packet_manifest_sha256,sha(read(Q+'p212_keyed_stdin_cuda_alias_source_root01/SHA256SUMS')));
equal(D.observer_source.path,ROOT+source+'observe.py');equal(D.observer_source.pin,ref(source+'observe.py').pin);equal(D.observer_source.source_manifest_sha256,sha(read(source+'SHA256SUMS')));
equal(D.observer_source.self_attested,false);equal(D.observer_source.lf_lines,436);
equal(D.historical_trust_decision,ref(Q+'p212_trusted_product_boundary_root01/DECISION.json'));
equal(D.independent_source_audit.path,ROOT+Q+'p212_keyed_stdin_cuda_alias_source_audit01/REPORT.md');equal(D.independent_source_audit.pin,ref(Q+'p212_keyed_stdin_cuda_alias_source_audit01/REPORT.md').pin);
equal(D.independent_source_audit.manifest_sha256,sha(read(Q+'p212_keyed_stdin_cuda_alias_source_audit01/SHA256SUMS')));
equal(D.environment_after_env,old.environment_after_env);equal(D.shell,old.shell);equal(D.scope.bounds,old.scope.bounds);equal(D.scope.bound_limits,old.scope.bound_limits);
const prefix=old.exact_native_prefix.slice();prefix[prefix.length-1]=ROOT+source+'observe.py';equal(D.exact_native_prefix,prefix);equal(V,[...prefix,get('AUTHORIZATION.prospective.json').toString('ascii')],'exact complete final argv argument');
ok(get('AUTHORIZATION.prospective.json').every(c=>c<128)&&get('AUTHORIZATION.prospective.json').length<=32768,'canonical ASCII bound including LF');
const quote=s=>"'"+s.replaceAll("'","'\\''")+"'";
const capture='/root/symbolic-dynamics-p212-cuda-alias-observation-20260910-01';
equal(D.capture,{directory:capture,stdout:capture+'/stdout.raw',stderr:capture+'/stderr.raw',pathnames_only:true,absence_queried:false,allocated:false,preparation_native:null,capacity_observed:null});
const expected={...oldReq,cmd:'umask 077\nset -C\nexec '+V.map(quote).join(' ')+' < '+quote(old.stdin.path)+' > '+quote(capture+'/stdout.raw')+' 2> '+quote(capture+'/stderr.raw')+'\n'};
equal(R,expected,'whole exact request no unreviewed option');equal(D.stdin.path,old.stdin.path);equal(D.stdin.required_content,old.stdin.required_content);
equal(D.stdin.actual_current_key,null);equal(D.stdin.observed_or_prepared_by_this_packet,false);equal(D.stdin.inherited_fd0_identity_attested,false);
equal(D.stdin.prior_evidence.partial_single_pass_empty_regular_native_fields_and_empty_content_received,true);equal(D.stdin.prior_evidence.complete_two_pass_native_key_received,false);equal(D.stdin.prior_evidence.old_grant_consumed,true);
equal(D.stdin.prior_evidence.path,ROOT+Q+'p212_keyed_stdin_failed_observation_root01/RECEPTION.md');equal(D.stdin.prior_evidence.pin,ref(Q+'p212_keyed_stdin_failed_observation_root01/RECEPTION.md').pin);
equal(N.cmd,null);equal(N.operational_authorization,false);equal(N.old_grant_reusable,false);equal(T.operational_authorization,false);equal(T.allowed_changes_to_source_or_frontier,[]);
const future=ROOT+Q+'p212_keyed_stdin_cuda_alias_observation_root01/';equal(D.activation.future_directory_string_only,future);equal(T.future_directory_string_only,future);
equal(D.activation,{independent_exact_request_audit_received:false,root_request_reception:false,capture_prepared:false,grant:null,enabled_files_materialized:false,future_directory_string_only:future,exact_copies:['AUTHORIZATION.prospective.json => AUTHORIZATION.json','ARGV.prospective.json => ARGV.json','REQUEST.prospective.json => REQUEST.json'],no_further_semantic_change_allowed:true});
equal(D.scope.maximum_proposed_observer_invocations,1);equal(D.scope.actual_invocations_by_this_proposal,0);equal(D.scope.automatic_retries,0);equal(D.scope.observer_spawned_children,0);equal(D.scope.author_probes,0);equal(D.scope.scientific_runs,0);equal(D.scope.builds,0);
equal([D.scope.frontier.target_count,D.scope.frontier.component_count,D.scope.frontier.membership_sets,D.scope.frontier.membership_names,D.scope.frontier.closure_gaps],[164,207,5,292,8]);
equal(D.scope.frontier.path,A.frontier.path);equal(D.scope.frontier.pin,A.frontier.pin);equal(D.future_runtime_acceptance,false);equal(D.author_probes_authorized,false);equal(D.external_status,'HOLD_EXTERNAL');
const names=['AUTHORIZATION','ARGV','REQUEST'];equal(P.entries.length,3);equal(T.prospective_copies.length,3);
for(let i=0;i<3;i++){const n=names[i],raw=get(n+'.prospective.json');equal(P.entries[i],{source:B+n+'.prospective.json',future_path_string_only:future+n+'.json',bytes:raw.length,sha256:sha(raw)});equal(T.prospective_copies[i],{from:n+'.prospective.json',to:future+n+'.json'});}
const pn=json('PROSPECTIVE_PINS_NATIVE.json');ok(pn.response.exit_code===0&&!pn.response.session_id,'actual prospective document pin command');equal(Buffer.from(pn.response.output),get('PROSPECTIVE_BYTES.json'),'actual raw prospective map output');
for(const k of keys.values())equal(shape(fs.lstatSync(k.path,{bigint:true})),k.fields,'all selected endpoints unchanged');
process.stdout.write(JSON.stringify({scope:'AUTHOR_DOCUMENTARY_REQUEST_PREPARATION_ONLY',checks,input_keys:15,document_keys:keys.size,prospective:P.entries,keys:[...keys.values()],independent_review:false,source_executed:false,host_private_input_observed:false,operational_authorization:false},null,2)+'\n');
