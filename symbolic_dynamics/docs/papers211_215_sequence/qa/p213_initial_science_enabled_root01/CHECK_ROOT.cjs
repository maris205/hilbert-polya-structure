'use strict';
// Root documentary evidence reception. All operational strings remain DATA.
const fs=require('node:fs');
const makeReader=require('./READ_FIXED.cjs');
const R="docs/papers211_215_sequence/qa/p213_initial_science_enabled_root01/",A="docs/papers211_215_sequence/qa/p213_initial_science_enabled_source_audit01/";
const P='docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/';
const O='docs/papers211_215_sequence/qa/p213_initial_science_preparation01/';
const B='docs/papers211_215_sequence/qa/p213_initial_science_source_root01/';
const FIXED_INPUTS=[{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/SHA256SUMS","bytes":680,"sha256":"8071e2eaddbe6a01bccca9d0cd63bee96af9b44e8b11d97b43e905eb5ce35cbf"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/CHECK_NATIVE.json","bytes":35085,"sha256":"516b77a6a153eb8b99f0bb33dfcf8013408bbecfbc78022a9483f1f978198453"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/CHECK_ROOT.cjs","bytes":13098,"sha256":"7141eb93c24d58a8a46926b5e326dc596205ad0a77afc235cb082e1f82621617"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/CLOSE.cjs","bytes":2582,"sha256":"e5cc40fb24c599c984538ae042be0cb04123be1a33d59eaef66a94a120aa5a57"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/CLOSING_NATIVE.json","bytes":24511,"sha256":"41bbbd0858323ae235e5d2f2c8c4a911a849781ed7b23fd0ab010123d6807c59"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/RECEPTION.md","bytes":7455,"sha256":"de2892a93661d177f78bacbb4c15904a7e33d88d509fe96eb38c3e23ae03b5df"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/ROOT_AUDIT_READS_NATIVE.json","bytes":45877,"sha256":"cc3dee08b507b49683b07008ae757330c5fac7401dde0744f8caae16502ef4ee"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/ROOT_READS_NATIVE.json","bytes":281328,"sha256":"533f58d1e7484f39f76b8614a581930618fa95f7e8a16266e2860edd22325f36"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/ROOT_REPLAY_NATIVE.json","bytes":73429,"sha256":"4b8e1febb3a3b53f90a1e122e1562b228beb9b3aee3b70cacfa76c5f90287177"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SHA256SUMS","bytes":1508,"sha256":"ef1e95d740634c6531706aaa3b4fda0f0f99fbb14f604c80bc24f3d3235a7cdf"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/BINDING.proposed.json","bytes":66395,"sha256":"78da1d06c05cd6244e9de9c1565a843823051e98c8702c07c5447e20d1da3ab6"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/CHECK_NATIVE.json","bytes":96548,"sha256":"6253a4dc5318adcfde9592fe8fcc7eca6ea9354e0ececea1f3cd70c288f12a52"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/COLLECTOR_REUSE_CHECK.json","bytes":3302,"sha256":"162a054e1f0f3e4ac0cf34f01cfbe214ea6e7fc7c04a637f5aa9879a55a835be"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/CREATION_NATIVE.json","bytes":1252,"sha256":"a0e9a260565255dd231c28a8f092bf1ed4f259e5f745e3a4395b7849bcca4c86"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/DEPENDENCY_CONTRACT.md","bytes":11195,"sha256":"c52d389d4bbcf944905b241a6c8ef14b23082362f9f003848f143b8ef2dbb307"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/EXECUTION_SEQUENCE.md","bytes":5079,"sha256":"3c35cab1996c0207755755323ccc3b508ed4f86e6c9b35e5c4483e6b4b908c11"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/HANDOFF.md","bytes":5367,"sha256":"ac9290b2eb34fc02445dcc42493783a1c4013f9eba0cc30e0c849d41976697db"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/PREPARATION.md","bytes":7820,"sha256":"1268b6f5b2c0da7dca2b460782e7a26637065c63fc0125217612dad3b55b9f3a"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/REQUEST.disabled.json","bytes":5909,"sha256":"d7e01fe79599289d3a05538ffca2b896eff960dff35d5659a58caee5b4f68b17"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SOURCE_DELTA.md","bytes":4991,"sha256":"0cc248fc9a1e6640cae462ed398aed78a2d1f934168816f93f19158996602b5c"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SOURCE_INPUTS.sha256","bytes":2291,"sha256":"33767cd63ab4c5b7f44669dee5ebdc7f60ec9563536ac4d01b05df0f06fac41d"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SOURCE_TEXT_READS_NATIVE.json","bytes":226946,"sha256":"51b9e15d5d7e59064d63c99c35994af4d95ff10b9ae3f908558b02a834d3126a"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/WORKSPACE_READS_NATIVE.json","bytes":316289,"sha256":"d395e20dab0f0d0cce5e538ef2b487c7bcc517e9811e0f541b3d2a27a8075bd5"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.initial.disabled.sh","bytes":1759,"sha256":"d16d681d44f95784d15d26929a3fddd5a3775c48a5e032759bef52c61679614c"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.replay01.disabled.sh","bytes":1762,"sha256":"35a9af07787bf526b64aeedee2a67f64959f4e2deab68c800798d1bb557f4500"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.replay02.disabled.sh","bytes":1762,"sha256":"d3a223d9b73ef0c2813f5fe451320eb50bb31418e7ca52f42cc0cdeab3115888"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/run_science.disabled.py","bytes":108770,"sha256":"2dcc96f6540e3caa5078f7cd9d92b307fea2a62e069415a50e333367e91ca7a9"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/SHA256SUMS","bytes":999,"sha256":"27890badfbebbac1db8ddb4046d98c847555c7cc62995253b1ebf23064c10dcf"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/AUDIT.md","bytes":15311,"sha256":"7d5c2ba9f62a312aeae3f424ba0e0f67df5d1310c602a63bc87a09a9c89a727d"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CHECK_FAILURE01_NATIVE.json","bytes":75893,"sha256":"8d13c7e9a9fa75cbded5c522d8c0f1068c219642f39aae8cab66b35b4fbde3f4"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CHECK_NATIVE.json","bytes":94152,"sha256":"e9a8bfb78c2e1085b58bac95897c03d496a5dc4825c03e8ba7a7dfcf7acd1961"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CHECK_SOURCE.cjs","bytes":16426,"sha256":"590b405446c40e2a62fbfb221812f623b1f79f9a4be11031323a9481bcb02e84"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CHECK_SOURCE_FAILURE01.cjs.txt","bytes":16096,"sha256":"64425b259e98c3a52a3aa9292d9478cb5b4dcc457a28147725a21af4dcfe2697"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CLOSE_DOCUMENTS.cjs","bytes":5944,"sha256":"0da72837e055433d6b71e10a66487282b20a5566a04b59a763b401718ff16d85"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CLOSURE_NATIVE.json","bytes":21543,"sha256":"ed23eb46ef5a6fdd83252369885dec5537d4fcf4cc3fbdad9a6ab41988c01fb4"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/FINDINGS.json","bytes":2209,"sha256":"737f3dc9824c7a051090f892a4cb0a7639bc27d2b423debcb06fe314a2d29721"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/HANDOFF.md","bytes":2194,"sha256":"2fb72a401702047ec1a71be139da66808fb292ddaabcf84c42c58be5770e4e4c"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/INPUTS.sha256","bytes":5064,"sha256":"aa17440c2339ce843b633fc980cfed47066406d75ef777b43ae0792b62032290"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/PLAN.md","bytes":1544,"sha256":"d20c8514bc403dd6e9e4e9ea47afb85adb9e9afdffaaa30673232b5c4db3e804"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/READ_NATIVE.json","bytes":697287,"sha256":"cb64667cab5767e08d7609443c7bf84753215c70f2afaed5e57009930e211ab7"},{"path":"papers/213-receiver-limited-cyclic-transfer/verify.py","bytes":17539,"sha256":"a01d3d93619cea90adfc2e5be1bdfd8089d7eae6fcaae153b4fb4af398fc1812"},{"path":"papers/213-receiver-limited-cyclic-transfer/VERIFICATION_PARAMETERS.json","bytes":1452,"sha256":"7454c9462903bc305a43438004f362317ae3b2cad514674d72a945519fb338df"},{"path":"papers/213-receiver-limited-cyclic-transfer/OUTPUT_SCHEMA.md","bytes":6947,"sha256":"c0ff52c4705de83f59ca858cb82e21a679da918b906e7d2698b3d7aad92fef6b"},{"path":"papers/213-receiver-limited-cyclic-transfer/SCIENTIFIC_DEPENDENCIES.md","bytes":3340,"sha256":"d4e70a87586e6f09ff126e2bb91b11142f9b89c77169ec63279d990ff5e38984"},{"path":"papers/213-receiver-limited-cyclic-transfer/RUNTIME_PLAN.md","bytes":4430,"sha256":"65751565f6165af8187fe4eb456646b1e82fb8fc12b635902c034b54c2f129d8"},{"path":"papers/213-receiver-limited-cyclic-transfer/REVIEW_INTERFACES.md","bytes":2532,"sha256":"6e9568c69e70229c90769448f5bb4735a992783e91fa9e139a879f4196d0bd52"},{"path":".agents/skills/symbolic-dynamics-research/SKILL.md","bytes":1596,"sha256":"1af30c2095702a0cc722e87389c8d515a4d668b22e85af25edb2fce02c10d22d"},{"path":"docs/research_state/WORKFLOW.md","bytes":6861,"sha256":"dd6c109a695d8774b3dacff5fa9d76d28aa5e72e99b33c4abe0ac7afb1a26324"},{"path":"AGENTS.md","bytes":1618,"sha256":"bbc2d46f26aa43474f9f09fbffd93f6f4faf29982c1ffae2ece18b1fa48fbd35"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/CHECK_DOCUMENTS.cjs","sha256":"b9efad193e4e9ad278dbb8f833b6ee92e537a5b0abaf051fa8fec4b383cdda2c"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/CHECK_NATIVE.json","sha256":"280abed0a0294a0853391285a454f9337c1b80444ee85e8a80c1ba9f55e82233"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/CLOSE.cjs","sha256":"b7e3e0c97a2435cb2cc713f96f02fb79df87b9d9817a59907c457f0c52090036"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/CLOSING_NATIVE.json","sha256":"5eaf079f0dd26d3bf26eb96f02eb61965465632aadc196c90660bdac908e77c5"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/CONTRACT.md","sha256":"3a26cc83bb3c06ffa2d17e4a047f5c8012020af8a4828b37cbf4591f1afaed65"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/CREATION_NATIVE.json","sha256":"b11d970795cdf679bfe42e6f37a53043fa133ac7c36845c2ffa934d905e833b7"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/HANDOFF.md","sha256":"daec26422f4ebee273927d5361eeafb42af982b32500bd934866843f2dd86603"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/INPUTS.sha256","sha256":"32fbc456c1e2c7c30e432b8371e1bf6644a384385198e0f5536a636f7bc581b0"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/PINSET.json","sha256":"47ad2de9504c03c473323dce18f23b48cde24584672cb659f179a579e50dc8df"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/READ_NATIVE.json","sha256":"9179135cdc31d8272a7a100588aba28c4d398402c6ef49e7d5e41bfc61c566da"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/REQUEST.initial.proposed.json","sha256":"83afb8f6b2d0286048fcb3f84e6bac11e9aed0e1e2808b37e1929dd602d9b27c"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/REQUEST.replay01.proposed.json","sha256":"1d70fb92308b5f604334d12b89c8f2d1118d5ea1fece1c63d1874208675557ea"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/REQUEST.replay02.proposed.json","sha256":"3814e6984b28b540c80879b52d55e71166157ad8759625f27ee4c9e171e59346"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/SOURCE_DELTA.json","sha256":"8ebfe4921b6a4aad93a7d02a62d565907ab4c25ebe94fb92f1a7d9c06a30d652"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/capture.initial.proposed.sh.txt","sha256":"c0d5c51be1de58531d897bf97f4c7fc7458aa37858ff6cb005bfce5607f08e25"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/capture.replay01.proposed.sh.txt","sha256":"013144ba4673f7440efe9873ad851b2c1b4f19ecbabd4ce9af2d70a5f0bcd2fa"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/capture.replay02.proposed.sh.txt","sha256":"92ba8b7ae2e57274fafd93be5bd7b3f998b515832eeeb52cad17e263c4d3ffa8"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/run_science.proposed.py.txt","sha256":"87cd4409bf5394792f66318893cc9e187ff43c1419bcfd819f17f874cdb7c121"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/SHA256SUMS","sha256":"c6a2f9806136a91b3765c26a4c8882db8027b8b8848c4f2f81372c5b50b0224d"}];
const AUDIT_NAMES=["SHA256SUMS","AUDIT.md","CHECK_DOCUMENTS.cjs","CHECK_NATIVE.json","CLOSE_DOCUMENTS.cjs","CLOSING_NATIVE.json","DOCUMENTARY_CANONICAL.json","FINDINGS.json","HANDOFF.md","INPUTS.sha256","PLAN.md","READ_NATIVE.json"];
const OWN=["READ_FIXED.cjs","INPUT_SPEC.json","ROOT_READS_NATIVE.json","ROOT_AUDIT_READS_NATIVE.json","ADDITIONAL_READS_NATIVE.json","ROOT_REPLAY_NATIVE.json","CHECK_ROOT.cjs"];
const allowed=new Set([...FIXED_INPUTS.map(x=>x.path),...AUDIT_NAMES.map(n=>A+n),...OWN.map(n=>R+n)]);

const r=makeReader(allowed), {need,read,keys,sha,equal}=r;
const json=p=>JSON.parse(read(p).toString('utf8'));
const pin=p=>{const b=read(p);return {path:p,bytes:b.length,sha256:sha(b)};};
const pairs=[],received=[],exceptions=[];
function raw(a,b,label){
 a=Buffer.isBuffer(a)?a:Buffer.from(a,'utf8'); b=Buffer.isBuffer(b)?b:Buffer.from(b,'utf8');
 need(a.equals(b),'COMPLETE_RAW_EQUAL '+label);pairs.push({label,bytes:a.length,sha256:sha(a)});
}
function keySet(arr,label){
 need(Array.isArray(arr),'FULL_KEY_ARRAY '+label);
 for(const k of arr){read(k.path);need(equal(k,keys.get(k.path)),'EVERY_KEY_FIELD '+label+' '+k.path);}
 received.push({label,occurrences:arr.length});
}
function native(e,chunk,command){
 need(e.tool==='exec_command'&&e.result.exit_code===0&&e.result.chunk_id===chunk&&!e.result.session_id,'ACTUAL_NATIVE '+chunk);
 need(e.request.cmd===command&&e.request.workdir==='/root/autodl-tmp/symbolic_dynamics','EXACT_REQUEST '+chunk);
 need(typeof e.result.output==='string'&&!e.result.output.startsWith('Warning: truncated output'),'NATIVE_COMPLETE '+chunk);
 return JSON.parse(e.result.output);
}
function sed(e,label){
 const request=e.request, result=e.result||e.native;
 if(!request||!result)return false;
 const m=/^sed -n '(\d+),(\d+)p' (.+)$/.exec(request.cmd);
 if(!m)return false;
 if(result.exit_code!==0||result.output.startsWith('Warning: truncated output')){
   exceptions.push({label,chunk:result.chunk_id,exit:result.exit_code,command:request.cmd,truncated:result.output.startsWith('Warning: truncated output')});return false;
 }
 const paths=m[3].split(' ');
 if(!paths.every(p=>allowed.has(p)))return false;
 const source=Buffer.concat(paths.map(read)),lines=source.toString('utf8').split(/(?<=\n)/);
 raw(result.output,lines.slice(Number(m[1])-1,Number(m[2])).join(''),label+' '+result.chunk_id);
 return true;
}
const report={scope:'ROOT_EXACT_P213_ENABLED_SOURCE_AND_FULL_REQUEST_RECEPTION_ONLY',status:'RUNNING',
 operation_granted:false,materialization:false,future_operands_queried:false,science_executed:false,
 canonical_adopted:false,strict_pair_complete:false,external_status:'HOLD_EXTERNAL'};
try{
 need(process.argv.length===2&&process.cwd()==='/root/autodl-tmp/symbolic_dynamics','EXACT_CHECKER_CONTEXT');
 for(const p of allowed)read(p);
 for(const p of FIXED_INPUTS){
   const q=pin(p.path);need(q.sha256===p.sha256&&(!Object.hasOwn(p,'bytes')||q.bytes===p.bytes),'ENTIRE_FIXED_DOCUMENT_PIN');
 }
 const spec=json(R+'INPUT_SPEC.json');
 need(equal(spec.inputs,FIXED_INPUTS),'SPEC_EXACT_FIXED_INPUT_LIST');
 const groups=[...spec.source_packages,{path:A.slice(0,-1),payloads:11,files:12,bytes:1033547,seal:'c9efba83170779fbb5492c5bf28c2f471224ac2492d6d720a21a12536d8cc60d'}];
 report.packages=[];
 for(const g of groups){
   const prefix=g.path+'/', b=read(prefix+'SHA256SUMS'),t=b.toString('utf8');
   need(sha(b)===g.seal&&t.endsWith('\n'),'EXACT_NONSELF_SEAL');
   const lines=t.slice(0,-1).split('\n'),names=[];
   need(lines.length===g.payloads,'EXACT_MANIFEST_LENGTH');
   let total=b.length;
   for(const line of lines){
     const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);
     need(m!==null&&m[2]!=='SHA256SUMS','STRICT_NONSELF_ROW');
     names.push(m[2]);const payload=read(prefix+m[2]);need(sha(payload)===m[1],'ALL_PAYLOAD_HASHES');total+=payload.length;
   }
   need(new Set(names).size===names.length&&equal(fs.readdirSync(prefix).sort(),['SHA256SUMS',...names].sort()),'COMPLETE_PHYSICAL_INVENTORY');
   need(total===g.bytes&&names.length+1===g.files,'ENTIRE_PACKAGE_BYTES');
   report.packages.push(g);
 }
 raw(read(A+'SHA256SUMS'),spec.independent_package.manifest_text,'original independent full manifest return');
 const original=json(A+'CHECK_NATIVE.json'), replay=json(R+'ROOT_REPLAY_NATIVE.json');
 const x=native(original,'6afc23','node '+A+'CHECK_DOCUMENTS.cjs');
 const y=native(replay,'7cffdb','node '+A+'CHECK_DOCUMENTS.cjs');
 raw(original.result.output,read(A+'DOCUMENTARY_CANONICAL.json'),'independent original stdout vs documentary canonical');
 raw(replay.result.output,original.result.output,'actual root replay vs original whole stdout');
 need(x.status==='PASS_EXACT_ENABLED_DERIVATIVE_REQUEST_SOURCE_ONLY'&&x.checks===34129&&x.key_count===68&&x.total_read_bytes===3488866,'COMPLETE_REPLAY_CENSUS');
 need(equal(x,y),'ENTIRE_PARSED_REPLAY_REPORT');
 keySet(x.keys,'independent 6afc23');keySet(y.keys,'root replay7cffdb');
 raw(read(A+'INPUTS.sha256'),x.input_pins.map(p=>p.sha256+'  '+p.path+'\n').join(''),'entire independent pin list');
 for(const p of x.input_pins)need(equal(pin(p.path),p),'ALL_COMPLETE_INPUT_PINS');
 const authorArchive=json(P+'READ_NATIVE.json');
 const intake=authorArchive.entries.find(e=>e.result.chunk_id==='19ce5d');
 need(intake&&intake.result.exit_code===0,'ACTUAL_AUTHOR_INITIAL_INTAKE');
 for(const [e,n] of [[intake,57],[json(P+'CHECK_NATIVE.json'),65],[json(P+'CLOSING_NATIVE.json'),66]]){
   const d=JSON.parse(e.result.output);need(e.result.exit_code===0&&d.key_count===n&&d.keys.length===n,'AUTHOR_FULL_KEY_CENSUS');
   keySet(d.keys,'author '+e.result.chunk_id);
   raw(e.result.output,JSON.stringify(d,null,2)+'\n','entire author native JSON '+e.result.chunk_id);
 }
 const closure=json(A+'CLOSING_NATIVE.json');
 const c=native(closure.closing,'7a721f','node '+A+'CLOSE_DOCUMENTS.cjs');
 need(c.status==='PASS_INDEPENDENT_AUDIT_PRECLOSURE_ONLY'&&c.checks===1172&&c.key_count===78&&c.keys.length===78,'EXACT_HISTORICAL_PRECLOSE_DATA');
 keySet(c.keys,'independent historical preseal7a721f');
 for(const p of c.preclosing_files)need(equal(pin(p.path),p),'ALL_TEN_PRECLOSING_FILES');
 need(c.preclosing_files.length===10,'EXACT_PRESEAL_CUTOFF');
 sed(closure.source_read,'independent full closing source original');
 const f=json(A+'FINDINGS.json');
 need(f.disposition===x.status&&f.noncontributor===true&&f.author_contact===false&&equal(f.current_open,{critical:0,major:0,minor:0})&&f.findings.length===0,'FULL_FINDING_CENSUS_AND_ROLE');
 need(f.root_grant===null&&!f.materialization_accepted&&!f.science_accepted&&!f.canonical_adopted&&!f.strict_pair_complete,'NO_GRANT_FROM_REVIEW');
 const delta=json(P+'SOURCE_DELTA.json');
 for(const d of delta.changes){
   const old=read(d.old.path),now=read(d.proposed.path);
   raw(old.subarray(0,d.old_prefix_bytes),d.old_prefix,'exact old prefix '+d.old.path);
   raw(now.subarray(0,d.new_prefix_bytes),d.new_prefix,'exact new prefix '+d.proposed.path);
   raw(old.subarray(d.old_prefix_bytes),now.subarray(d.new_prefix_bytes),'entire unchanged suffix '+d.proposed.path);
   need(now.length===d.proposed.bytes&&sha(now)===d.proposed.sha256,'ENTIRE_DERIVATIVE_PIN');
 }
 for(const stage of ['initial','replay01','replay02']){
   const d=json(P+'REQUEST.'+stage+'.proposed.json');
   raw(d.proposed_native_request.arguments.cmd,read(P+'capture.'+stage+'.proposed.sh.txt'),'whole proposed native capture '+stage);
   need(d.operation_authorized===false&&d.root_grant===null&&d.actual_native_request===null&&d.actual_native_result===null&&d.actual_session_id===null,'UNCHANGED_PROPOSAL_NOT_AUTHORITY');
 }
 let rootSlices=0,independentSlices=0;
 for(const n of ['ROOT_READS_NATIVE.json','ROOT_AUDIT_READS_NATIVE.json'])
   for(const e of json(R+n).entries)if(sed(e,'complete root text read'))rootSlices++;
 for(const e of json(A+'READ_NATIVE.json').entries)if(sed(e,'complete original independent text read'))independentSlices++;
 need(independentSlices===24,'ALL_ORIGINAL_INDEPENDENT_SLICES');
 need(exceptions.length===1&&exceptions[0].chunk==='f1a867'&&exceptions[0].truncated,'PRESERVED_ROOT_INTRINSIC_TRUNCATION_ONLY');
 const oldReads=json(B+'ROOT_READS_NATIVE.json').records;
 const wrapper=oldReads.filter(e=>/^sed -n '\d+,\d+p' docs\/papers211_215_sequence\/qa\/p213_initial_science_preparation01\/run_science.disabled.py$/.test(e.command));
 const science=oldReads.filter(e=>/^sed -n '\d+,\d+p' papers\/213-receiver-limited-cyclic-transfer\/verify.py$/.test(e.command));
 need(wrapper.length===10,'TEN_PREVIOUS_FULL_WRAPPER_RANGES');
 raw(wrapper.map(e=>e.result.output).join(''),read(O+'run_science.disabled.py'),'prior received entire3083line disabled wrapper');
 raw(science.map(e=>e.result.output).join(''),read('papers/213-receiver-limited-cyclic-transfer/verify.py'),'prior received entire451line unchanged verifier');
 report.current_source_census=f.current_open;report.root_read_slices=rootSlices;report.independent_read_slices=independentSlices;
 report.replay_checks=34129;report.historical_preseal_data_checks=1172;report.historical_preseal_reexecuted=false;
 report.excluded_root_reads=exceptions;report.full_key_receptions=received;
 report.full_key_occurrences=received.reduce((s,e)=>s+e.occurrences,0);
 report.raw_pairs=pairs;report.raw_pair_count=pairs.length;report.raw_pair_bytes=pairs.reduce((s,p)=>s+p.bytes,0);
 report.complete_enabled_suffix_received=true;report.unchanged_accepted_verifier=true;report.status='PASS_ROOT_SOURCE_REQUEST_RECEPTION_ONLY';
}catch(e){report.status='FAIL_ROOT_SOURCE_REQUEST_RECEPTION_ONLY';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
report.checks=r.checks;report.key_count=keys.size;report.total_read_bytes=r.total;report.keys=[...keys.values()];
process.stdout.write(JSON.stringify(report,null,2)+'\n');
