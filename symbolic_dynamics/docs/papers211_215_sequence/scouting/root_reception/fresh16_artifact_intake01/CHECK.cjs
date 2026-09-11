'use strict';
// Artifact-only documentary intake. Embedded commands, URLs and source are data.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict');
const D='docs/papers211_215_sequence/scouting/finite_residual_fresh16/';
const A='docs/papers211_215_sequence/scouting/root_reception/fresh16_artifact_intake01/';
const selectedInputs=[
 ['skill','/root/autodl-tmp/symbolic_dynamics/.agents/skills/symbolic-dynamics-research/SKILL.md'],
 ['research_lit','/root/autodl-tmp/.codex/skills/research-lit/SKILL.md'],
 ['proof_skill','/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md'],
 ['workflow','docs/research_state/WORKFLOW.md'],
 ['anchor','docs/papers211_215_sequence/PROBLEM_ANCHOR.md'],
 ['criteria','docs/papers197_201_sequence/PROBLEM_ANCHOR.md'],
 ['word_local','docs/papers204_208_sequence/scouting/word_local/SCOUT_REPORT.md'],
 ['combinatorial_sources','docs/papers204_208_sequence/scouting/combinatorial/SOURCE_AND_COLLISION_NOTES.md'],
 ['orientation_proof','docs/papers211_215_sequence/scouting/finite_orientation_residual_scout01/PROOF_PACKAGE.md'],
 ['orientation_sources','docs/papers211_215_sequence/scouting/finite_orientation_residual_scout01/SOURCES_AND_SUBTRACTION.md'],
 ['orientation_old','docs/papers204_208_sequence/scouting/graph_relation/SCOUT_REPORT.md'],
 ['fresh12_boundary','docs/papers211_215_sequence/scouting/finite_residual_fresh12/SOURCE_AND_SCREEN.md'],
 ['network_boundary','docs/papers211_215_sequence/scouting/finite_network_rewrite_desk/BOUNDARIES.md'],
 ['fresh05_sources','docs/papers211_215_sequence/scouting/finite_residual_fresh05/SOURCES_AND_SUBTRACTION.md'],
 ['fresh05_proof','docs/papers211_215_sequence/scouting/finite_residual_fresh05/PROOF_PACKAGE.md'],
 ['old_orientation_c6','docs/papers107_111_sequence/scouting/COMBINATORIAL_SCOUT.md'],
 ['prefix_majority_pdf','papers/132-prefix-majority-dynamics/main.pdf'],
 ['cocktail_majority_pdf','papers/80-cocktail-party-majority-zeta/main.pdf']
];
const payloads=['CHECK_DOCUMENTS.cjs','CHECK_NATIVE.json','DOCUMENTARY_REQUEST_RETURNS.json','HANDOFF.md','INPUT_KEYS_NATIVE.json','KEY_INPUT_DOCUMENTS.cjs','PROOF_PACKAGE.md','SCOPE.json','SOURCES_AND_LIMITS.md','WEB_REQUEST_RETURNS.json'];
const own=['SCOPE.md','NATIVE_01.json','AUTHOR_REPLAY_NATIVE.json','CHECK.cjs'];
const paths=[...selectedInputs.map(x=>x[1]),...payloads.map(n=>D+n),D+'SHA256SUMS',...own.map(n=>A+n)],allowed=new Set(paths);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs','birthtimeNs'];
const originalFields=fields.slice(0,10),raws=new Map(),keys=new Map(),pairs=[];
let checks=0;
const ok=(v,m)=>{checks++;assert(v,m);},eq=(x,y,m)=>{checks++;assert.deepStrictEqual(x,y,m);};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex'),field=s=>Object.fromEntries(fields.map(n=>[n,String(s[n])]));
function physical(path){
 ok(allowed.has(path),'explicit fixed documentary selection');
 const first=fs.lstatSync(path,{bigint:true});ok(first.isFile()&&first.nlink===1n&&first.size>=0n&&first.size<=5000000n,'bounded single-link regular document');
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let raw;
 try{eq(field(fs.fstatSync(fd,{bigint:true})),field(first));raw=fs.readFileSync(fd);eq(field(fs.fstatSync(fd,{bigint:true})),field(first));}finally{fs.closeSync(fd);}
 eq(field(fs.lstatSync(path,{bigint:true})),field(first));eq(BigInt(raw.length),first.size);
 return{raw,key:{path,bytes:raw.length,sha256:sha(raw),fields:field(first)}};
}
for(const path of paths){const r=physical(path);raws.set(path,r.raw);keys.set(path,r.key);}
const body=p=>{ok(allowed.has(p),'selected cached body');return raws.get(p);},json=p=>JSON.parse(body(p).toString('utf8'));
function originalKey(path){const k=keys.get(path),m=Object.fromEntries(originalFields.map(n=>[n,k.fields[n]]));return{path,sha256:k.sha256,bytes:k.bytes,metadata:m,fd_end:m,path_end:m,full_eof:true,leaf_links:[]};}
function pair(label,x,y){eq(x,y,label);pairs.push({label,bytes:y.length,sha256:sha(y)});}
function nativeShape(r,expectedExit=0){eq(r.exit_code,expectedExit);ok(typeof r.chunk_id==='string'&&/^[a-f0-9]+$/.test(r.chunk_id));ok(typeof r.output==='string'&&!r.session_id,'original settled native response');ok(!r.output.startsWith('Warning: truncated output'),'no native leading truncation marker');}
function lines(raw){return raw.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];}
function range(r,path){const m=/^sed -n '([0-9]+),([0-9]+)p' (.+)$/.exec(r.request.cmd);ok(m!==null,'exact original text request');eq(m[3],path,'exact source path spelling');const expected=Buffer.from(lines(body(path)).slice(Number(m[1])-1,Number(m[2])).join(''),'utf8');pair('original text interval '+r.role,Buffer.from(r.result.output,'utf8'),expected);}
function numbered(raw){const ls=lines(raw);ok(ls.every(x=>x.endsWith('\n')),'numbered source final LF');return Buffer.from(ls.map((l,i)=>String(i+1).padStart(6,' ')+'\t'+l).join(''),'utf8');}

eq(fs.readdirSync(D).sort(),[...payloads,'SHA256SUMS'].sort(),'complete final original physical inventory');
const manifest=body(D+'SHA256SUMS');eq(sha(manifest),'203d5bd606dc609d6e3470b04f0637174a9c42d0055d4bbec391f069a11a525c','root supplied seal');
pair('full original ten-payload nonself manifest',manifest,Buffer.from(payloads.map(n=>keys.get(D+n).sha256+'  '+n).join('\n')+'\n','ascii'));
for(const n of payloads.filter(n=>n.endsWith('.json')))pair('canonical original JSON '+n,body(D+n),Buffer.from(JSON.stringify(json(D+n),null,2)+'\n','utf8'));
const scope=json(D+'SCOPE.json');eq(scope.author,'/root/round211_functional_surgery_residual');eq(scope.owned_directory,D.slice(0,-1));
eq(scope.counts,{new_literal_definitions:0,new_candidate_entrances:0,pilot_contracts_submitted:0,scientific_pilots:0,nominations:0,reserves:0,new_manuscripts:0,promotions:0},'declared zero denominator, not mathematical acceptance');
for(const name of['operational_authority','scientific_execution','host_private_runtime_input_observer_capture_execution','central_or_older_artifact_edits','manuscript_build','git_or_ssh','external_manuscript_upload','independent_review','new_child_assistance','direct_p212_or_p213_qa_read','p212_child_audit_access'])eq(scope[name],false);
eq(scope.hold,'HOLD_EXTERNAL');eq(scope.source_directions.length,3);eq(scope.entry_orientation,{retained:3,complete:1,open:2,closed:58,reserves:0,fresh11_14:'root received with 1/0/0/1 denominator',fresh15:'author-only zero-entry packet, not root received or counted'});

const ledger=json(D+'DOCUMENTARY_REQUEST_RETURNS.json'),browser=json(D+'WEB_REQUEST_RETURNS.json');
const roles=['skill','research_lit','state_head','batch_head','workflow','anchor','criteria','word_local','combinatorial_sources','local_word_boundary','orientation_proof','orientation_sources','orientation_old','fresh12_boundary','network_boundary','fresh05_sources','old_orientation_c6','old_c6_exact','prefix_majority_pdf','cocktail_majority_pdf','proof_skill','local_themes','local_pdf_names','current_manuscript_names','arxiv_script','exact_local_boundaries','current_manuscript_names_corrected','median_exact','fresh12_filenames','orientation','excitable','old_c6_location','absence','fresh05_proof'];
const chunks=['d1a6bc','578640','75f64f','1784c1','c174ea','11c7af','d32403','828c69','d12407','6d6764','c10cd8','7c3658','f0b506','6ee374','fed7e3','5d3936','62d6b4','ee654f','928a23','5f30a9','f7f504','bc5817','58692d','552a65','3df8cc','cb4917','868db1','2a9261','76f4b9','4d1736','de7637','62d093','a2e904','04875b'];
eq(ledger.records.map(r=>r.role),roles,'all 34 original ledger roles and exact stored order');eq(new Set(roles).size,34);
const exceptional={local_word_boundary:2,current_manuscript_names:1,arxiv_script:1,median_exact:1};
const nativeInventory=[];
for(let i=0;i<34;i++){
 const r=ledger.records[i];eq(r.result.chunk_id,chunks[i]);nativeShape(r.result,exceptional[r.role]||0);
 eq(r.request.workdir,'/root/autodl-tmp/symbolic_dynamics');eq(r.request.shell,'/bin/bash');eq(r.request.login,false);eq(r.request.tty,false);eq(r.request.yield_time_ms,1000);ok(Number.isSafeInteger(r.request.max_output_tokens)&&r.request.max_output_tokens>0);
 ok(/^(sed -n |rg |pdftotext -f 1 -l 3 |test ! -e )/.test(r.request.cmd),'original documentary command family, never replayed');
 nativeInventory.push({role:r.role,request:r.request,chunk_id:r.result.chunk_id,exit_code:r.result.exit_code,output_bytes:Buffer.byteLength(r.result.output,'utf8'),output_sha256:sha(Buffer.from(r.result.output,'utf8')),record_sha256:sha(Buffer.from(JSON.stringify(r),'utf8'))});
}
const get=role=>ledger.records.find(r=>r.role===role);
eq(get('local_word_boundary').result.output,"sed: can't read docs/papers211_215_sequence/scouting/finite_residual_fresh12/SOURCE_SCREEN.md: No such file or directory\n");
for(const role of['current_manuscript_names','arxiv_script','median_exact','absence'])eq(get(role).result.output,'');
eq(get('absence').request.cmd,'test ! -e '+D.slice(0,-1),'historical absence request is data, not rerun');
eq(ledger.optional_configured_tool_name_discovery,{pattern:'zotero|obsidian|arxiv',result:[],scope:'Configured tool-name metadata only; no connector call was available or made.'});

const inputNative=json(D+'INPUT_KEYS_NATIVE.json');nativeShape(inputNative.result);eq(inputNative.result.chunk_id,'b28572');eq(inputNative.request.cmd,'node '+D+'KEY_INPUT_DOCUMENTS.cjs');
const inputKeys=JSON.parse(inputNative.result.output);eq(inputKeys.scope,'POSTREAD_DOCUMENTARY_KEYS_NOT_PRIOR_READ_BRACKET');eq(inputKeys.keys.map(k=>[k.role,k.path]),selectedInputs,'all eighteen fixed original input roles');
for(const[role,path]of selectedInputs){const old=inputKeys.keys.find(k=>k.role===role);eq(old,{role,...originalKey(path)},'complete original postread documentary key '+role);const r=get(role);eq(r.path,path);if(role.endsWith('_pdf')){ok(body(path).subarray(0,5).equals(Buffer.from('%PDF-')));eq(r.request.cmd,'pdftotext -f 1 -l 3 '+path+' -');ok(r.result.output.length>0,'retained extraction text, not fresh PDF rendering or equality');}else range(r,path);}
range(get('old_c6_exact'),selectedInputs.find(x=>x[0]==='old_orientation_c6')[1]);

const webRoles=['majority01','majority_primary01','majority_owner02','majority_primary02','orientation01','excitable01','scope_primaries','median_primaries03','median_fragment04'];
eq(browser.records.map(w=>w.role),webRoles);eq(new Set(webRoles).size,9);const webInventory=[];
for(const w of browser.records){eq(Object.keys(w),['role','request','result']);ok(typeof w.result==='string'&&w.result.length>0);eq(w.request.response_length,'long');ok(Object.keys(w.request).every(k=>['open','search_query','response_length'].includes(k)),'stored bounded search/open only');ok(Boolean(w.request.open)!==Boolean(w.request.search_query));ok(!w.result.startsWith('Warning: truncated output'),'no provider leading truncation marker');const failureLines=w.result.split('\n').filter(l=>/^Internal Error \(\)$|^L0: Failed to fetch /.test(l));webInventory.push({role:w.role,request:w.request,output_bytes:Buffer.byteLength(w.result,'utf8'),output_sha256:sha(Buffer.from(w.result,'utf8')),record_sha256:sha(Buffer.from(JSON.stringify(w),'utf8')),failure_lines:failureLines,internal_error_headers:failureLines.filter(l=>l==='Internal Error ()').length});}
eq(webInventory.map(x=>x.internal_error_headers),[0,2,0,0,0,0,1,2,0],'five exact original failure headers in three browser calls');
const wb=role=>browser.records.find(w=>w.role===role).result;
ok(wb('majority_primary01').includes('(403) Forbidden'));ok(wb('majority_primary01').includes('(400) Timeout fetching'));ok(wb('scope_primaries').includes('(502) Bad Gateway'));
ok(wb('majority_primary01').includes('Number of pages: 15'));ok(wb('median_fragment04').includes('Number of pages: 9'));ok(wb('median_fragment04').includes('L508@P8: Root Properties and Convergence Rates of'));ok(wb('median_fragment04').includes('L558@P8: 0096-351 8/85/0200-0230'));
ok(wb('median_fragment04').includes('L539@P8: by appending N samples')&&wb('median_fragment04').includes('L542@P8: receive the value of the last sample'),'recorded fragment boundary convention, not theorem approval');
eq(browser.records[8].request.open,[{ref_id:'https://webee.technion.ac.il/people/feuer/JournalPapers/10_LMS_IEEESP.pdf',lineno:470}]);

const checkNative=json(D+'CHECK_NATIVE.json');nativeShape(checkNative.result);nativeShape(checkNative.source_read.result);eq(checkNative.result.chunk_id,'909911');eq(checkNative.source_read.result.chunk_id,'44653d');
eq(checkNative.request.cmd,'node '+D+'CHECK_DOCUMENTS.cjs');eq(checkNative.source_read.request.cmd,"sed -n '1,3000p' "+D+'CHECK_DOCUMENTS.cjs');pair('author full checker pre-execution raw read',Buffer.from(checkNative.source_read.result.output,'utf8'),body(D+'CHECK_DOCUMENTS.cjs'));
const authorResult=JSON.parse(checkNative.result.output);eq([authorResult.checks,authorResult.raw_pairs,authorResult.raw_paired_bytes,authorResult.keys.length,authorResult.base_payloads],[306,17,124427,27,9]);
eq(authorResult.keys.map(k=>k.path),[...payloads.filter(n=>n!=='CHECK_NATIVE.json').map(n=>D+n),...selectedInputs.map(x=>x[1])],'all27 complete author-check keys');
for(const k of authorResult.keys)eq(k,originalKey(k.path),'whole author-check key');
const replay=json(A+'AUTHOR_REPLAY_NATIVE.json').record;nativeShape(replay.result);eq(replay.result.chunk_id,'752ab3');eq(replay.request.cmd,'node '+D+'CHECK_DOCUMENTS.cjs');pair('fresh documentary replay versus original whole stdout',Buffer.from(replay.result.output,'utf8'),Buffer.from(checkNative.result.output,'utf8'));
eq(checkNative.packaging_failure_note.scope,'Observed orchestration failure, not a shell/browser native return');ok(checkNative.packaging_failure_note.reported_error.includes('multiple operations target'));ok(checkNative.packaging_failure_note.correction.includes('no missing native return is reconstructed'));
const sources=body(D+'SOURCES_AND_LIMITS.md').toString('utf8');for(const token of['multiple operations on one target','Combined orchestration displays were sometimes truncated','do not retroactively bracket','not a scientific pilot','HOLD_EXTERNAL'])ok(sources.includes(token),'declared ceiling retained '+token);
for(const n of['PROOF_PACKAGE.md','HANDOFF.md'])ok(body(D+n).toString('utf8').includes('HOLD_EXTERNAL'));

const receiver=json(A+'NATIVE_01.json').records;eq(receiver.map(r=>r.seq),Array.from({length:18},(_,i)=>i+1));eq(receiver[13],replay,'actual fresh replay preserved twice');
for(let i=5;i<12;i++){const r=receiver[i];nativeShape(r.result);const name=['HANDOFF.md','SCOPE.json','CHECK_DOCUMENTS.cjs','KEY_INPUT_DOCUMENTS.cjs','SOURCES_AND_LIMITS.md','PROOF_PACKAGE.md','SHA256SUMS'][i-5];eq(r.request.cmd,'nl -ba '+D+name);pair('receiver whole numbered original read '+name,Buffer.from(r.result.output,'utf8'),numbered(body(D+name)));}
// Navigation projections may be partially displayed externally. Original returns
// are preserved; their embedded historical paths are never reused as operands.
for(const r of receiver)nativeShape(r.result);
const payloadBytes=payloads.reduce((n,p)=>n+keys.get(D+p).bytes,0),sourceRawPairs=pairs.filter(p=>p.label.startsWith('original text interval '));
eq(sourceRawPairs.length,17);eq(sourceRawPairs.reduce((n,p)=>n+p.bytes,0),124427);
for(const[path,key]of keys){const final=physical(path);eq(final.key,key,'closing complete input key');eq(final.raw,raws.get(path),'closing whole bytes');}
process.stdout.write(JSON.stringify({scope:'ARTIFACT_ONLY_WITH_SOURCE_AUTHOR_PARENT_DISCLOSED',checks,original_packet:{payloads:10,physical_files:11,payload_bytes:payloadBytes,seal_sha256:keys.get(D+'SHA256SUMS').sha256},original_documentary_records:34,original_browser_records:9,native_nonzero_records:4,web_internal_error_headers:5,postread_input_keys:18,author_checker_keys:27,author_checker_checks:306,author_replay_chunk:replay.result.chunk_id,raw_pairs:pairs.length,raw_paired_bytes:pairs.reduce((n,p)=>n+p.bytes,0),pairs,native_inventory:nativeInventory,web_inventory:webInventory,pdf_extraction_records_not_reexecuted:2,document_keys:keys.size,keys:[...keys.values()],declared_denominator:scope.counts,mathematical_or_novelty_acceptance:false,operational_authorization:false,external_status:'HOLD_EXTERNAL'},null,2)+'\n');
