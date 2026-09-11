'use strict';
// Independent P214 display-repair artifact DATA receiver; accepted initial receiver delta.
// Read-only ordinary workspace DATA: no producer import, host follow, child, build or write.
const fs=require('node:fs'), path=require('node:path'), crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics', Q=W+'/docs/papers211_215_sequence/qa/';
const P=Q+'p214_display_repair_preparation01', B=Q+'p214_display_repair_binding01', I=Q+'p214_initial_build_preparation01';
const S=W+'/papers/214-nilpotent-bilinear-clock', R=Q+'p214_display_repair_run01', C=R+'/source_only';
const A=Q+'p214_runtime_root01', Z=Q+'p214_source_root01', H=Q+'p214_initial_build_run01';
const INITIAL_AUDIT=Q+'p214_initial_artifact_audit01', SOURCE_AUDIT=Q+'p214_display_repair_source_audit01';
const INITIAL_RECEIPT=Q+'p214_initial_artifact_root01/RECEPTION.md', INPUT_PINS=Q+'p214_display_repair_artifact_audit01/INPUT_PINS.sha256';
const baseChecker=INITIAL_AUDIT+'/ARTIFACT_DATA_CHECK.cjs';
const sourceNames=['main.tex','math_commands.tex','references.bib','sections/0_abstract.tex','sections/1_setup.tex','sections/2_clock.tex','sections/3_fibres.tex','sections/4_controls.tex','sections/5_scope.tex'];
const products=['main.aux','main.bbl','main.blg','main.log','main.fls','main.out','main.toc','main.pdf'];
const passes=['pass1','bibtex','pass2','pass3'];
const snapshots=passes.flatMap(p=>[p+'.before',p+'.after']);
const bibliographyKeys=['Bors2017','ElAbdalaouiEtAl2016'];
let checks=0;
function ok(v,m){checks++;if(!v)throw Error(m);}
function eq(a,b,m){ok(JSON.stringify(a)===JSON.stringify(b),m);}
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const bytes=new Map(), externalPins=[], rawPairs=[], findings=[];
const fixedExternal=[...['BUILD_REQUEST.proposed.sh.txt','NATIVE_REQUEST.proposed.json','PROPOSED_SOURCE_ONLY.sha256','BEFORE_SOURCE_ONLY.sha256','SOURCE.diff','PLAN.md'].map(n=>P+'/'+n),...['BUILD_REQUEST.proposed.sh.txt','NATIVE_REQUEST.proposed.json','PROPOSED_SOURCE_ONLY.sha256'].map(n=>I+'/'+n),Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md',Q+'p212_plain_build_source_root01/RECEPTION.md',Q+'p212_plain_build_source_proposal03/CONTRACT.md',INITIAL_RECEIPT,baseChecker,...['stdout.raw','stderr.raw','SHA256SUMS','SOURCE_SHA256SUMS'].map(n=>INITIAL_AUDIT+'/'+n),...['GRANT.md','ACTUAL_NATIVE.json','CONTINUATION_NATIVE.json','RUNTIME_PREFLIGHT_NATIVE.json','BINDING_NATIVE.json','RUNTIME_INPUTS.sha256','SOURCE_RECEPTION.md','ADOPTED_SOURCE_INPUTS.sha256'].map(n=>B+'/'+n),A+'/PAIR_RECEPTION.md',Q+'p214_author_data_root01/RECEPTION.md',Z+'/SOURCE_RECEPTION.md',Z+'/ADOPTED_SOURCE_INPUTS.sha256',...['REPORT.md','INPUT_PINS.sha256','SHA256SUMS'].map(n=>SOURCE_AUDIT+'/'+n),...['originals','proposed'].flatMap(d=>['sections/2_clock.tex','sections/5_scope.tex'].map(n=>P+'/'+d+'/'+n)),...sourceNames.map(n=>S+'/'+n)];
const externalAllowed=new Set(fixedExternal);externalAllowed.add(INPUT_PINS);
function readExternal(p){ok(externalAllowed.has(p),'external path allowlist '+p);if(!bytes.has(p)){const st=fs.lstatSync(p);ok(st.isFile()&&!st.isSymbolicLink(),'external regular '+p);const b=fs.readFileSync(p);bytes.set(p,b);externalPins.push({path:p,bytes:b.length,sha256:sha(b)});}return bytes.get(p);}
function decode(b){const t=b.toString('utf8');ok(Buffer.from(t,'utf8').equals(b),'lossless UTF-8');return t;}
const xt=p=>decode(readExternal(p));
const ls=t=>{ok(!t.includes('\r'),'LF-only grammar');return t===''?[]:(ok(t.endsWith('\n'),'terminal LF'),t.slice(0,-1).split('\n'));};
const manifest=t=>{const rows=ls(t).map(l=>{const m=/^([0-9a-f]{64})  ([^\r\n]+)$/.exec(l);ok(!!m,'manifest syntax');return {sha256:m[1],path:m[2]};});ok(new Set(rows.map(r=>r.path)).size===rows.length,'unique manifest names');return rows;};
function sameBuffers(a,b,label){ok(a.equals(b),'RAW equality '+label);rawPairs.push({label,bytes:a.length,sha256:sha(a)});}
const pinnedDocuments=manifest(xt(INPUT_PINS));
eq(pinnedDocuments.map(r=>r.path),fixedExternal.map(p=>p.slice(W.length+1)).sort(),'exact complete documentary input pin set');
for(const row of pinnedDocuments)ok(sha(readExternal(W+'/'+row.path))===row.sha256,'whole pinned document '+row.path);
ok(sha(readExternal(baseChecker))==='510da893509d05e4f93d9474c41a02c945c2f59f34f63c5eaafd7be74d544aea','accepted initial checker bytes, never imported or rerun');
const initialReceipt=xt(INITIAL_RECEIPT);
ok(sha(readExternal(INITIAL_RECEIPT))==='5332df9872384be622f3a7bbf42227eb69af447ba2731b6fed4cef3750e4414c'&&initialReceipt.includes('HOLD retained'),'complete accepted historical HOLD reception');
ok(sha(readExternal(INITIAL_AUDIT+'/SHA256SUMS'))==='744b527953ea9e3f4ed8d8349f030b670ee44dd3c4d349d56bfa47d951bbea61'&&sha(readExternal(INITIAL_AUDIT+'/SOURCE_SHA256SUMS'))==='2d7c023ee6ed4fada0ba32af46034ab8aa9b672c0f55dc6f9518580a150a2792','both historical seals unchanged');
const initialRaw=readExternal(INITIAL_AUDIT+'/stdout.raw');
ok(initialRaw.length===905048&&sha(initialRaw)==='ede7ca45a53a0292df8c56f6e43bc12b19813dfb3338be336266c22045716f81'&&readExternal(INITIAL_AUDIT+'/stderr.raw').length===0,'whole historical initial report/empty stderr retained');
const initialData=JSON.parse(decode(initialRaw));
ok(initialData.status==='HOLD_ARTIFACT_FINDINGS'&&initialData.checks===3281&&initialData.findings.length===6,'historical complete HOLD, not waived');
eq(initialData.findings.map(f=>{ok(f.severity==='Major'&&f.raw.includes('paragraph at lines 90--94'),'original generic finding retained');return /^Overfull \\hbox \(([0-9.]+)pt/.exec(f.raw)[1];}),['16.91365','16.91365','19.01251','19.01251','19.01251','19.01251'],'all six old occurrences, one paragraph cause');
const replaceLiteral=(text,from,to,label)=>{ok(text.split(from).length===2,'one literal '+label);return text.replace(from,to);};
const recipePathDelta=[[I,P],[Q+'p214_initial_build_binding01',B],[H,R]];
const recipeDelta=[['# current source, exact request and fresh finite runtime/trust binding.','# adopted display/status delta, exact request and fresh runtime/trust binding.'],['P214_INITIAL_BUILD_SUPERVISOR_EXIT','P214_DISPLAY_REPAIR_BUILD_SUPERVISOR_EXIT']];
let expectedRecipe=xt(I+'/BUILD_REQUEST.proposed.sh.txt');
ok(sha(readExternal(I+'/BUILD_REQUEST.proposed.sh.txt'))==='f81626f9bc257b6be0aa53e5790da29b020fafd92a0a21cfe84072df2b68aa7d','accepted initial recipe identity');
for(const [from,to]of [...recipePathDelta,...recipeDelta])expectedRecipe=replaceLiteral(expectedRecipe,from,to,'exact repair recipe delta');
ok(xt(P+'/BUILD_REQUEST.proposed.sh.txt')===expectedRecipe&&sha(readExternal(P+'/BUILD_REQUEST.proposed.sh.txt'))==='10e4c1e1b5ca79ea768ab0209596f038c397fba2a3072a2c6a673b22ffd4663e','whole five-location recipe adaptation; all other bytes unchanged');
const proposal=JSON.parse(xt(P+'/NATIVE_REQUEST.proposed.json')),baseRequest=JSON.parse(xt(I+'/NATIVE_REQUEST.proposed.json'));
ok(sha(readExternal(I+'/NATIVE_REQUEST.proposed.json'))==='0fb2cfc07ca7dea77306d9c5f64ddf9a4ccb143ad37a963667462f1a1b74a64e'&&sha(readExternal(P+'/NATIVE_REQUEST.proposed.json'))==='f12dde9ccea25db44d430c7cd53600447e4837bda0ee691f3ce56948fefc6fd7','whole root-read initial and repair requests');
const expectedNative=JSON.parse(JSON.stringify(baseRequest.proposed_native_request));expectedNative.arguments.cmd=replaceLiteral(expectedNative.arguments.cmd,I,P,'native recipe path');
eq(proposal.proposed_native_request,expectedNative,'whole native vector unchanged except exact recipe path');eq(proposal.environment,baseRequest.environment,'all thirteen variables');eq(proposal.build_sequence,baseRequest.build_sequence,'four unchanged passes');eq(proposal.source_list,sourceNames,'nine source roles');eq(proposal.proposed_cwd_check.expected_counts,{root:4,sections:6,source_files:9},'unchanged staged membership');eq(proposal.bibliography_keys,bibliographyKeys,'two bibliography roles');
ok(proposal.schema==='P214_DISPLAY_REPAIR_BUILD_SOURCE_ONLY_REQUEST_V1'&&!proposal.operation_authorized&&proposal.root_grant===null,'proposal itself is not a grant');ok(proposal.source_root===S&&proposal.proposed_output_directory===R&&proposal.supervisor_status_label==='P214_DISPLAY_REPAIR_BUILD_SUPERVISOR_EXIT','new exact build role');
const launch=JSON.parse(xt(B+'/ACTUAL_NATIVE.json')),continuation=JSON.parse(xt(B+'/CONTINUATION_NATIVE.json'));
eq(launch.arguments,proposal.proposed_native_request.arguments,'whole actual repair native request');ok(launch.result.chunk_id==='3a4987'&&launch.result.session_id===1244&&launch.result.output===''&&!Object.hasOwn(launch.result,'exit_code'),'actual repair launch');
eq(continuation.arguments,{session_id:1244,chars:'',yield_time_ms:1000,max_output_tokens:2000},'sole actual continuation');ok(continuation.result.chunk_id==='cf150d'&&continuation.result.exit_code===0&&!Object.hasOwn(continuation.result,'session_id')&&continuation.result.output==='P214_DISPLAY_REPAIR_BUILD_SUPERVISOR_EXIT=0\n','actual complete repair native exit/stream');
const grant=xt(B+'/GRANT.md'),policy=xt(Q+'p212_plain_build_source_root01/RECEPTION.md'),sourceReception=xt(B+'/SOURCE_RECEPTION.md'),supplement=xt(Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md'),contract=xt(Q+'p212_plain_build_source_proposal03/CONTRACT.md');
const pairReceipt=xt(A+'/PAIR_RECEPTION.md'),authorDataReceipt=xt(Q+'p214_author_data_root01/RECEPTION.md'),adoptedReception=xt(Z+'/SOURCE_RECEPTION.md'),sourceAudit=xt(SOURCE_AUDIT+'/REPORT.md');
ok(grant.includes('ISSUED_AND_CONSUMED_BEFORE_NEXT_SINGLE_SUBMISSION.')&&grant.includes('No retry, cleanup'),'new consumed grant and no retry');ok(policy.includes('P212-POLICY-TIME1 is therefore CLOSED')&&policy.includes('supplement has precedence'),'retained adopted ordinary/staged policy');
ok(sha(readExternal(Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md'))==='055b06bc5e47ffa1fd6459101e473c86808fbfe44a2d56f186012efb9fa2f1b3','unchanged staged supplement');ok(sha(readExternal(B+'/SOURCE_RECEPTION.md'))==='0424f17f6c4f9690cfb3fd4bf18254549d39523c557748e495489e427b021bb4'&&sourceReception.includes('Only sections/2_clock.tex and sections/5_scope.tex were then replaced'),'actual exact source adoption and policy receipt');
ok(sha(readExternal(SOURCE_AUDIT+'/REPORT.md'))==='8ef2f2e13e584587b3d78b21203b8a0d902666025d6f37a18fabce5d77c71094'&&sourceAudit.includes('SOURCE_ACCEPTABLE'),'independent repair source audit, not layout closure');
ok(sha(readExternal(A+'/PAIR_RECEPTION.md'))==='0bc99d9ec61ae8fe36151fd081654c53e2a077038b66c41244a0a3d76ba8cfc3'&&pairReceipt.includes('ACCEPT_AUTHOR_STRICT_PAIR_UNCHANGED_SEMANTICS_REUSE'),'accepted actual author pair, not new science');ok(sha(readExternal(Q+'p214_author_data_root01/RECEPTION.md'))==='196201ccf7cac6ef000922f52e5491ec5454a4c0cb9771930a7699b2a7ef5dce','accepted full finite DATA evidence for new statement');
const sourceManifest=readExternal(P+'/PROPOSED_SOURCE_ONLY.sha256'),beforeManifest=readExternal(P+'/BEFORE_SOURCE_ONLY.sha256');
ok(sha(sourceManifest)==='3e92cd23388e8e26b7b75d2ecc290aedf7d3c96168cbdd54c73c0d685b95fb05'&&sha(beforeManifest)==='7844ffa35be54db6b98ba131882bae2d6059ec11fb6609fbbf92d428dc1d596e','distinct before/repair placement pins');
sameBuffers(beforeManifest,readExternal(I+'/PROPOSED_SOURCE_ONLY.sha256'),'unchanged historical initial placement key');
const sources=manifest(decode(sourceManifest)),beforeSources=manifest(decode(beforeManifest));eq(sources.map(r=>r.path),sourceNames,'nine new source roles');eq(beforeSources,initialData.source_pins,'historical source key matches accepted HOLD report');
const adoptedSources=manifest(xt(B+'/ADOPTED_SOURCE_INPUTS.sha256')),oldAdoptedSources=manifest(xt(Z+'/ADOPTED_SOURCE_INPUTS.sha256'));
eq(adoptedSources.map(x=>x.path),oldAdoptedSources.map(x=>x.path),'same complete 28 documentary roles');ok(adoptedSources.length===28,'28 adopted roles');eq(adoptedSources.filter((x,i)=>x.sha256!==oldAdoptedSources[i].sha256).map(x=>x.path),['sections/2_clock.tex','sections/5_scope.tex'].map(n=>S.slice(W.length+1)+'/'+n),'only two of28 adopted document pins change');
for(const row of sources)ok(adoptedSources.some(r=>r.path===S.slice(W.length+1)+'/'+row.path&&r.sha256===row.sha256),'each actual adopted build role '+row.path);
const sourceDelta=[
  {path:'sections/2_clock.tex',from:'therefore gives $q^{\\lceil h/2\\rceil}q^{\\lfloor h/2\\rfloor}=q^h$\n',to:'therefore gives\n\\[\n q^{\\lceil h/2\\rceil}q^{\\lfloor h/2\\rfloor}=q^h\n\\]\n'},
  {path:'sections/5_scope.tex',from:'The accompanying author-verifier source is restricted to\n$q\\in\\{2,3,4\\}$ and $m\\in\\{2,3,4\\}$. It is designed to enumerate every\n',to:'The accompanying author verifier was run for\n$q\\in\\{2,3,4\\}$ and $m\\in\\{2,3,4\\}$. It exhaustively checked every\n'},
  {path:'sections/5_scope.tex',from:'predecessor set of every target, before checking the displayed formulas.\n',to:'predecessor set of every target against the displayed formulas.\n'},
  {path:'sections/5_scope.tex',from:'At this source-draft stage, no execution or computational result is claimed.\n',to:'The nine carriers contain 5,271 states, and the complete output contains\n10,646 records. Two further strict runs reproduced the canonical output\nbyte for byte. These finite checks do not establish the all-parameter\nstatements.\n'}
];
eq(sources.filter((x,i)=>x.sha256!==beforeSources[i].sha256).map(x=>x.path),[...new Set(sourceDelta.map(x=>x.path))],'exact two changed placement roles');
const runtimeManifest=readExternal(B+'/RUNTIME_INPUTS.sha256');ok(sha(runtimeManifest)==='35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530','new freshly bound selected manifest');
const runtime=manifest(decode(runtimeManifest));ok(runtime.length===223&&runtime.every(r=>path.isAbsolute(r.path)),'finite runtime strings as archival DATA only');const runtimeByName=new Map(runtime.map(r=>[r.path,r]));
const binding=JSON.parse(xt(B+'/BINDING_NATIVE.json'));ok(binding.result.exit_code===0&&binding.result.chunk_id==='7365b2','actual repair pregrant binding');
const boundNames=[P+'/BUILD_REQUEST.proposed.sh.txt',P+'/NATIVE_REQUEST.proposed.json',P+'/PROPOSED_SOURCE_ONLY.sha256',B+'/RUNTIME_INPUTS.sha256',B+'/SOURCE_RECEPTION.md',Q+'p212_plain_build_source_root01/RECEPTION.md',Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md',A+'/PAIR_RECEPTION.md'];
const diskObservation='Filesystem       1B-blocks        Used   Available Use% Mounted on\n/dev/md0       53687091200 39033626624 14653464576  73% /root/autodl-tmp\n';
ok(binding.result.output===path.dirname(R)+'\n'+diskObservation+boundNames.map(p=>sha(readExternal(p))+'  '+p.slice(W.length+1)+'\n').join(''),'whole archived parent/capacity/eight-pin output');
const bindingCommand=['set -e','cmp docs/papers211_215_sequence/qa/p214_initial_build_binding01/RUNTIME_INPUTS.sha256 docs/papers211_215_sequence/qa/p214_display_repair_binding01/RUNTIME_INPUTS.sha256','[ -d docs/papers211_215_sequence/qa ]','[ ! -L docs/papers211_215_sequence/qa ]','(cd docs/papers211_215_sequence/qa && pwd -P)','[ ! -e docs/papers211_215_sequence/qa/p214_display_repair_run01 ]','[ ! -L docs/papers211_215_sequence/qa/p214_display_repair_run01 ]','df -B1 docs/papers211_215_sequence/qa','sha256sum '+boundNames.map(p=>p.slice(W.length+1)).join(' ')].join('\n');
eq(binding.arguments,{cmd:bindingCommand,max_output_tokens:2000},'whole actual binding request, no invented defaults');
const prep=JSON.parse(xt(B+'/RUNTIME_PREFLIGHT_NATIVE.json')),runtimeOK=runtime.map(r=>r.path+': OK\n').join('');
eq(prep.arguments,{cmd:'sha256sum --check --strict docs/papers211_215_sequence/qa/p214_initial_build_binding01/RUNTIME_INPUTS.sha256',workdir:W,max_output_tokens:18000},'whole actual fresh preflight request as DATA');ok(prep.result.chunk_id==='5d2c9a'&&prep.result.exit_code===0&&prep.result.output===runtimeOK,'all223fresh pregrant received rows and whole output');
// Confirm the fixed initial artifact archive is unchanged; never reopen its live-source pins.
const archivedRows=initialData.inventory,archivedNames=new Set(archivedRows.map(x=>x.path)),archivePins=[],archiveDirectories=[],archiveSeen=[];
ok(archivedRows.length===161&&archivedNames.size===161,'complete accepted initial archive membership');
for(const row of archivedRows)ok(!path.isAbsolute(row.path)&&row.path.split('/').every(n=>n!==''&&n!=='.'&&n!=='..'),'bounded initial archive member');
function archiveWalk(d,rel=''){
  const st=fs.lstatSync(d);ok(st.isDirectory()&&!st.isSymbolicLink(),'ordinary initial archive directory');archiveDirectories.push(rel);
  for(const e of fs.readdirSync(d,{withFileTypes:true}).sort((a,b)=>a.name<b.name?-1:a.name>b.name?1:0)){
    const n=rel+e.name,p=d+'/'+e.name;ok(!e.isSymbolicLink(),'no initial archive symlink');
    if(e.isDirectory())archiveWalk(p,n+'/');else{ok(e.isFile()&&archivedNames.has(n),'known ordinary initial archive artifact');const b=fs.readFileSync(p),row=archivedRows.find(x=>x.path===n);ok(b.length===row.bytes&&sha(b)===row.sha256,'whole unchanged initial artifact '+n);bytes.set(p,b);archivePins.push({path:n,bytes:b.length,sha256:sha(b)});archiveSeen.push(n);}
  }
}
archiveWalk(H);eq(archiveSeen.slice().sort(),[...archivedNames].sort(),'exact unchanged initial files');
eq(archiveDirectories.slice().sort(),['','pages/','raw/','source_only/','source_only/sections/','pass_artifacts/',...snapshots.map(s=>'pass_artifacts/'+s+'/')].sort(),'exact unchanged initial directories');
const archivedBody=n=>{ok(archivedNames.has(n),'known initial archived body');return bytes.get(H+'/'+n);};

// The second enumerated tree is only the fixed completed repair output.
const inventory=[], directories=[];
function walk(d,rel=''){
  const st=fs.lstatSync(d);ok(st.isDirectory()&&!st.isSymbolicLink(),'ordinary output directory '+rel);directories.push(rel);
  for(const e of fs.readdirSync(d,{withFileTypes:true}).sort((a,b)=>a.name<b.name?-1:a.name>b.name?1:0)){
    const r=rel+e.name,p=d+'/'+e.name;ok(!e.isSymbolicLink(),'no output symlink '+r);
    if(e.isDirectory())walk(p,r+'/');else{ok(e.isFile(),'regular output '+r);const b=fs.readFileSync(p);bytes.set(p,b);inventory.push({path:r,bytes:b.length,sha256:sha(b)});}
  }
}
walk(R);
const actualNames=new Set(inventory.map(r=>r.path));
const rb=n=>{ok(actualNames.has(n),'recorded artifact '+n);return bytes.get(R+'/'+n);};
const rt=n=>decode(rb(n));
function same(a,b){sameBuffers(rb(a),rb(b),a+' == '+b);}
const expected=new Set();const want=n=>{ok(!expected.has(n),'nonduplicate expected artifact '+n);expected.add(n);};
const rootFiles=['controller.stdout.raw','controller.stderr.raw','controller.exit','SOURCE_EXPECTED.sha256','RUNTIME_EXPECTED.sha256','REQUEST_AND_BINDING.sha256','COLD_CWD.actual.txt','PAGE_COUNT.txt','PAGES.sha256','FINAL_PRODUCTS.sha256','STATUS.txt',...['runtime.before','runtime.after','live_source.before','live_source.after','cold_source.initial','cold_source.final'].flatMap(n=>[n+'.stdout',n+'.stderr'])];
rootFiles.forEach(want);
const sourceOK=sources.map(r=>r.path+': OK\n').join('');
for(const n of ['live_source.before','live_source.after','cold_source.initial','cold_source.final']){ok(rt(n+'.stdout')===sourceOK,'whole source guard '+n);ok(rt(n+'.stderr')==='','source guard stderr '+n);}
for(const when of ['before','after']){ok(rt('runtime.'+when+'.stdout')===runtimeOK,'whole selected runtime guard '+when);ok(rt('runtime.'+when+'.stderr')==='','runtime stderr '+when);}
sameBuffers(rb('SOURCE_EXPECTED.sha256'),sourceManifest,'captured source manifest == accepted');
sameBuffers(rb('RUNTIME_EXPECTED.sha256'),runtimeManifest,'captured runtime manifest == accepted');
const capturedBinding=[P+'/BUILD_REQUEST.proposed.sh.txt',P+'/NATIVE_REQUEST.proposed.json',B+'/RUNTIME_INPUTS.sha256'].map(p=>sha(readExternal(p))+'  '+p+'\n').join('');
ok(rt('REQUEST_AND_BINDING.sha256')===capturedBinding,'whole inner binding names/hashes');
for(const row of sources){
  const old=archivedBody('source_only/'+row.path),live=readExternal(S+'/'+row.path),cold=rb('source_only/'+row.path);
  ok(sha(old)===beforeSources.find(x=>x.path===row.path).sha256,'whole original cold source pin '+row.path);
  const edits=sourceDelta.filter(x=>x.path===row.path);let expectedSource=old;
  if(edits.length){sameBuffers(old,readExternal(P+'/originals/'+row.path),'physical repair original == initial cold '+row.path);let text=decode(old);for(const e of edits)text=replaceLiteral(text,e.from,e.to,'received source edit '+row.path);expectedSource=Buffer.from(text,'utf8');sameBuffers(expectedSource,readExternal(P+'/proposed/'+row.path),'exact edit == complete received proposal '+row.path);}
  ok(sha(expectedSource)===row.sha256,'exact repair source content pin '+row.path);sameBuffers(expectedSource,live,'old cold plus exact repair == live '+row.path);sameBuffers(expectedSource,cold,'old cold plus exact repair == new cold '+row.path);
  want('source_only/'+row.path);
}
ok(rt('controller.exit')==='0\n'&&rt('controller.stdout.raw')===''&&rt('controller.stderr.raw')==='','full controller success streams');
ok(rt('STATUS.txt')==='CAPTURED_PENDING_FULL_LOG_FLS_CONFIG_PDF_AND_ACTUAL_ALL_PAGE_RECEPTION\n','capture-only status, not acceptance');
const coldRecord=['commands=Bash pwd -P; dotglob/nullglob fixed (*) and (sections/*); exact membership/type/absence tests','expected_cwd='+C,'actual_physical_cwd='+C,'cold_member_count=4',...['main.tex','math_commands.tex','references.bib','sections'].map(n=>'cold_member='+n),'section_member_count=6',...sourceNames.filter(n=>n.startsWith('sections/')).map(n=>'section_member='+n),'relative_tree=texmf ABSENT','relative_tree=.texlive2021 ABSENT','EXACT_TWO_DIRECTORY_MEMBERSHIP_TYPES_AND_RELATIVE_TREE_ABSENCE_CHECKS_PASSED'].join('\n')+'\n';
ok(rt('COLD_CWD.actual.txt')===coldRecord,'complete exact actual cwd record');

const pageField=[...rt('raw/pdfinfo.stdout.raw').matchAll(/^Pages:[ \t]+([1-9][0-9]*)$/gm)];ok(pageField.length===1,'unique positive actual PDF page count');
const pageCount=Number(pageField[0][1]);ok(Number.isSafeInteger(pageCount)&&pageCount<=actualNames.size,'page count bounded by real inventory');
ok(rt('PAGE_COUNT.txt')===pageCount+'\n','page counter matches full PDF info');
const pageLabels=Array.from({length:pageCount},(_,i)=>'page-'+String(i+1).padStart(4,'0'));
const awkProgram='/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!/ {print FILENAME ":" FNR ":" $0}';
const texArgs=['/usr/bin/pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','main.tex'];
const commandVectors=[...passes.map(p=>({label:p,seconds:600,args:p==='bibtex'?['/usr/bin/bibtex','main']:texArgs})),{label:'pdfinfo',seconds:180,args:['/usr/bin/pdfinfo','main.pdf']},{label:'pdffonts',seconds:180,args:['/usr/bin/pdffonts','main.pdf']},{label:'pdftotext',seconds:180,args:['/usr/bin/pdftotext','-layout','main.pdf','-']},{label:'final_diagnostics',seconds:180,args:['/usr/bin/awk',awkProgram,'main.log','main.blg']},...pageLabels.map((label,i)=>({label,seconds:180,args:['/usr/bin/pdftoppm','-f',String(i+1),'-l',String(i+1),'-singlefile','-png','-r','150','main.pdf',R+'/pages/'+label]}))];
// Literal printable-ASCII subset of Bash printf %q used by these fixed vectors.
function bashQ(s){ok(s!==''&&/^[\x20-\x7e]+$/.test(s),'fixed printable argv');return [...s].map(c=>/[A-Za-z0-9_@%+=:,./-]/.test(c)?c:'\\'+c).join('');}
const commands=[];
for(const {label,seconds,args} of commandVectors){
  for(const suffix of ['request.txt','stdout.raw','stderr.raw','supervisor_exit'])want('raw/'+label+'.'+suffix);
  const rq='cwd='+C+'\nsupervisor_argv='+['/usr/bin/timeout','--signal=TERM','--kill-after=10s',seconds+'s',...args].map(bashQ).join(' ')+' \n';
  ok(rt('raw/'+label+'.request.txt')===rq,'exact complete step argv/cwd '+label);
  ok(rt('raw/'+label+'.supervisor_exit')==='0\n','step supervisor returned zero '+label);
  ok(rt('raw/'+label+'.stderr.raw')==='','complete step stderr '+label);
  if(label.startsWith('page-'))ok(rt('raw/'+label+'.stdout.raw')==='','page stdout');
  if(passes.includes(label)){for(const suffix of ['stdout','stderr'])want('raw/'+label+'.sources.'+suffix);ok(rt('raw/'+label+'.sources.stdout')===sourceOK&&rt('raw/'+label+'.sources.stderr')==='','per-pass source guards');}
  commands.push({label,supervisor_argv:['/usr/bin/timeout','--signal=TERM','--kill-after=10s',seconds+'s',...args],cwd:C,supervisor_exit:0,stdout_bytes:rb('raw/'+label+'.stdout.raw').length,stderr_bytes:0});
}

const snapshotData={};
for(const snap of snapshots){
  const prefix='pass_artifacts/'+snap+'/',havePresent=actualNames.has(prefix+'PRESENT.sha256'),haveAbsent=actualNames.has(prefix+'ABSENT.txt');
  const present=havePresent?manifest(rt(prefix+'PRESENT.sha256')):[],absent=haveAbsent?ls(rt(prefix+'ABSENT.txt')):[];
  ok((present.length>0)===havePresent&&(absent.length>0)===haveAbsent,'snapshot manifests iff nonempty');
  ok(new Set(absent).size===absent.length,'unique absent products');
  eq([...present.map(r=>r.path),...absent].sort(),[...products].sort(),'complete snapshot partition '+snap);
  eq(present.map(r=>r.path),products.filter(n=>present.some(r=>r.path===n)),'present recipe order');eq(absent,products.filter(n=>absent.includes(n)),'absent recipe order');
  if(havePresent)want(prefix+'PRESENT.sha256');if(haveAbsent)want(prefix+'ABSENT.txt');
  for(const row of present){ok(products.includes(row.path),'fixed product name');want(prefix+row.path);ok(sha(rb(prefix+row.path))===row.sha256,'snapshot whole product hash');}
  snapshotData[snap]={present,absent};
}
ok(snapshotData['pass1.before'].present.length===0,'all eight products genuinely absent before first pass');
const presentNames=snap=>snapshotData[snap].present.map(r=>r.path);
for(const [a,b] of [['pass1.after','bibtex.before'],['bibtex.after','pass2.before'],['pass2.after','pass3.before']]){eq(presentNames(a),presentNames(b),'adjacent snapshot presence');for(const n of presentNames(a))same('pass_artifacts/'+a+'/'+n,'pass_artifacts/'+b+'/'+n);}
for(const n of presentNames('bibtex.before'))same('pass_artifacts/bibtex.before/'+n,'pass_artifacts/bibtex.after/'+n);
eq(presentNames('bibtex.after').filter(n=>!presentNames('bibtex.before').includes(n)).sort(),['main.bbl','main.blg'],'BibTeX adds only two products');
for(const pass of ['pass2','pass3'])for(const n of ['main.bbl','main.blg'])same('pass_artifacts/'+pass+'.before/'+n,'pass_artifacts/'+pass+'.after/'+n);
const finalProducts=presentNames('pass3.after');
for(const n of ['main.aux','main.bbl','main.blg','main.log','main.fls','main.pdf'])ok(finalProducts.includes(n),'required final product '+n);
for(const n of finalProducts){want('source_only/'+n);same('pass_artifacts/pass3.after/'+n,'source_only/'+n);}
same('pass_artifacts/pass2.after/main.aux','pass_artifacts/pass3.after/main.aux');

// Preserve all events and original spellings. Path resolution here is lexical,
// not a realpath or an I/O operation; unknown host paths are never followed.
const ordered=[];
for(const pass of ['pass1','pass2','pass3']){
  const before=new Map(snapshotData[pass+'.before'].present.map(r=>[r.path,r])),after=new Map(snapshotData[pass+'.after'].present.map(r=>[r.path,r]));
  const outputs=new Set(),counts={},events=[];
  for(const [i,line] of ls(rt('pass_artifacts/'+pass+'.after/main.fls')).entries()){
    const m=/^(PWD|INPUT|OUTPUT) (.+)$/.exec(line);ok(!!m,'FLS grammar');const kind=m[1],spelling=m[2],absolute=path.resolve(C,spelling),local=absolute.startsWith(C+'/')?absolute.slice(C.length+1):null;
    let role,pin=null;
    if(kind==='PWD'){ok(i===0&&spelling===C,'unique first real FLS cwd');role='cwd';}
    else if(kind==='OUTPUT'){
      if(!['main.log','main.aux','main.pdf'].includes(local)){role='UNKNOWN_OUTPUT';findings.push({severity:'Major',pass,line:i+1,raw:line,reason:'unapproved recorder output'});}
      else{ok(after.has(local),'output present in after snapshot');outputs.add(local);role='generated-output';pin=after.get(local).sha256;}
    }else if(runtimeByName.has(absolute)){role='selected-runtime';pin=runtimeByName.get(absolute).sha256;}
    else if(sourceNames.filter(n=>n.endsWith('.tex')).includes(local)){role='declared-source';pin=sources.find(r=>r.path===local).sha256;}
    else if(outputs.has(local)){role='earlier-same-pass-output';pin=after.get(local).sha256;}
    else if(before.has(local)){role='generated-before';pin=before.get(local).sha256;}
    else{role='UNKNOWN_INPUT';findings.push({severity:'Major',pass,line:i+1,raw:line,reason:'unreceived recorder input; no host follow allowed'});}
    counts[role]=(counts[role]||0)+1;events.push({line:i+1,raw:line,kind,spelling,lexical_absolute:absolute,local,role,evidence_content_sha256:pin});
  }
  ok(counts.cwd===1,'exactly one FLS cwd');eq([...outputs].sort(),['main.aux','main.log','main.pdf'],'actual TeX output roles');
  eq([...new Set(events.filter(e=>e.role==='declared-source').map(e=>e.local))].sort(),sourceNames.filter(n=>n.endsWith('.tex')).sort(),'all eight TeX sources accounted for; database handled separately');
  ordered.push({pass,events,counts});
}

const texText=sourceNames.filter(n=>n.endsWith('.tex')).map(n=>rt('source_only/'+n)).join('\n');
const sourceCitations=[...texText.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
eq([...new Set(sourceCitations)].sort(),bibliographyKeys,'two source citations');
const bibSource=rt('source_only/references.bib'),bibKeys=[...bibSource.matchAll(/^@[A-Za-z]+\{([^,]+),/gm)].map(m=>m[1]);eq(bibKeys.slice().sort(),bibliographyKeys,'two pinned P214 Bib entries');
const auxBefore=rt('pass_artifacts/bibtex.before/main.aux'),auxFinal=rt('source_only/main.aux'),bbl=rt('source_only/main.bbl'),blg=rt('source_only/main.blg');
const citationKeys=t=>[...t.matchAll(/^\\citation\{([^}]+)\}$/gm)].flatMap(m=>m[1].split(','));
eq(citationKeys(auxBefore),sourceCitations,'real AUX-before citations');eq(citationKeys(auxFinal),sourceCitations,'final AUX citations');
for(const aux of [auxBefore,auxFinal]){eq([...aux.matchAll(/^\\bibstyle\{([^}]+)\}$/gm)].map(m=>m[1]),['plain'],'exact bibliography style');eq([...aux.matchAll(/^\\bibdata\{([^}]+)\}$/gm)].map(m=>m[1]),['references'],'exact bibliography database');ok(!aux.includes('\\@input'),'no unreceived nested AUX');}
ok(!auxBefore.includes('\\bibcite'),'cold AUX has no fabricated previous bibliography mapping');
const bblKeys=[...bbl.matchAll(/^\\bibitem\{([^}]+)\}$/gm)].map(m=>m[1]);eq(bblKeys.slice().sort(),bibliographyKeys,'two actual BBL items, no duplicates');
const bibcite=[...auxFinal.matchAll(/^\\bibcite\{([^}]+)\}\{([^}]+)\}$/gm)].map(m=>({key:m[1],number:m[2]}));
eq(bibcite,bblKeys.map((key,i)=>({key,number:String(i+1)})),'settled final numeric bibliography mapping');
ok(blg.includes('The top-level auxiliary file: main.aux\nThe style file: plain.bst\nDatabase file #1: references.bib\n'),'complete BibTeX top-level roles');
eq([...blg.matchAll(/You've used ([0-9]+) entries,/g)].map(m=>Number(m[1])),[bibliographyKeys.length],'actual BibTeX entry count');
ok(blg.includes('warning$ -- 0\n')&&!/Warning--|Error|error|^!/m.test(blg),'zero actual BibTeX warning/error');
// P214 has no P212 accent/name obligation; its two actual entries are received below.
ok(runtime.some(r=>r.path==='/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst'),'selected plain style content role');
const sourceLabels=[...texText.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);ok(new Set(sourceLabels).size===sourceLabels.length,'unique source labels');
const finalLabels=[...auxFinal.matchAll(/^\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{([0-9]+)\}\}$/gm)].map(m=>({key:m[1],number:m[2],page:Number(m[3])}));
eq(finalLabels.map(r=>r.key).sort(),sourceLabels.slice().sort(),'all final AUX labels exact');ok(finalLabels.every(r=>r.number!==''&&r.page>=1&&r.page<=pageCount),'labels have valid final numbers/pages');
const references=[...texText.matchAll(/\\(?:eqref|ref)\{([^}]+)\}/g)].map(m=>m[1]);for(const k of references)ok(finalLabels.some(r=>r.key===k),'resolved reference '+k);

const diagnostics=[];
const diagnosticRE=/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!|No file/;
for(const pass of ['pass1','pass2','pass3'])for(const role of ['log','stdout']){
  const name=role==='log'?'pass_artifacts/'+pass+'.after/main.log':'raw/'+pass+'.stdout.raw',lines=ls(rt(name)),records=[];
  for(let i=0;i<lines.length;i++)if(diagnosticRE.test(lines[i])){
    let end=i+1;if(lines[i].startsWith('LaTeX Warning:')||/^(?:Overfull|Underfull) \\[hv]box/.test(lines[i]))while(end<lines.length&&lines[end]!=='')end++;
    const raw=lines.slice(i,end).join('\n');let disposition='UNRESOLVED';
    const cite=/^LaTeX Warning: Citation `([^']+)'/.exec(raw),ref=/^LaTeX Warning: Reference `([^']+)'/.exec(raw);
    if(raw===' file:line:error style messages enabled.')disposition='informational error-format announcement';
    else if(pass==='pass1'&&/^No file main\.(aux|bbl)\.$/.test(raw))disposition='documented cold generated absence';
    else if(pass!=='pass3'&&cite&&bibliographyKeys.includes(cite[1]))disposition='interim citation resolved by final AUX/BBL and final diagnostics';
    else if(pass!=='pass3'&&ref&&finalLabels.some(r=>r.key===ref[1]))disposition='interim reference resolved by final AUX and final diagnostics';
    else if(pass!=='pass3'&&['LaTeX Warning: There were undefined references.','LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.'].includes(raw))disposition='interim rerun resolved by final AUX stability and final diagnostics';
    if(disposition==='UNRESOLVED')findings.push({severity:'Major',file:name,line:i+1,raw,reason:'unresolved actual diagnostic'});
    records.push({line:i+1,raw,disposition});i=end-1;
  }
  diagnostics.push({pass,role,file:name,records,warning_count:records.filter(r=>r.raw.startsWith('LaTeX Warning:')).length});
}
const awkRE=/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!/;
const expectedDiagnostics=['main.log','main.blg'].flatMap(n=>ls(rt('source_only/'+n)).flatMap((line,i)=>awkRE.test(line)?[n+':'+(i+1)+':'+line+'\n']:[])).join('');
ok(rt('raw/final_diagnostics.stdout.raw')===expectedDiagnostics,'exact complete diagnostic selection matches full logs');

const fontLines=ls(rt('raw/pdffonts.stdout.raw'));ok(fontLines.length>=3&&fontLines[0].startsWith('name ')&&/^[- ]+$/.test(fontLines[1]),'complete font table header');
const fonts=fontLines.slice(2).map(line=>{const m=/^(\S+)\s+(Type 1|Type 3|TrueType|CID Type 0C|CID TrueType|Type 1C)\s+(\S+)\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+([0-9]+)\s+([0-9]+)$/.exec(line);ok(!!m,'font row fully parsed');const r={raw:line,name:m[1],type:m[2],encoding:m[3],embedded:m[4],subset:m[5],unicode:m[6],object:m[7],generation:m[8]};if(r.type!=='Type 1'||r.embedded!=='yes'||r.subset!=='yes'||r.unicode!=='yes')findings.push({severity:'Major',reason:'font embedding/type needs reception',font:r});return r;});
ok(new Set(fonts.map(f=>f.name)).size===fonts.length,'distinct font rows');
const pdf=rb('source_only/main.pdf');ok(pdf.subarray(0,5).toString('ascii')==='%PDF-'&&pdf.subarray(-32).includes(Buffer.from('%%EOF')),'complete PDF container boundaries');
const pdfInfo=rt('raw/pdfinfo.stdout.raw');eq([...pdfInfo.matchAll(/^File size:[ \t]+([0-9]+) bytes$/gm)].map(m=>Number(m[1])),[pdf.length],'actual PDF byte count');
const pdfText=rt('raw/pdftotext.stdout.raw');ok((pdfText.match(/\f/g)||[]).length===pageCount&&pdfText.endsWith('\f'),'all extracted page frames');ok(!/\?\?|\[\?\]|\[VERIFY\]|\uFFFD/.test(pdfText),'no unresolved reference/replacement placeholders');
const textControls=[...pdfText].flatMap((ch,i)=>ch.charCodeAt(0)<32&&!['\n','\r','\t','\f'].includes(ch)?[{character_index:i,codepoint:ch.charCodeAt(0)}]:[]);
// Mathematical extraction control codes are reported, never silently normalized
// or treated as proof of a missing glyph; actual page views decide rendering.
ok(pdfText.includes('References')&&['Bors','El Abdalaoui','Bonnot','Messaoudi','Sester'].every(n=>pdfText.includes(n)),'both entries and all named authors represented in complete extracted text');
const referencesAt=pdfText.lastIndexOf('References');ok(referencesAt>=0,'actual PDF references section');
const bodyText=pdfText.slice(0,referencesAt).replace(/\s+/g,' '),referencesText=pdfText.slice(referencesAt).replace(/\s+/g,' ');
ok(bodyText.includes('A cancellation-safe clock for nilpotent bilinear dynamics')&&bodyText.includes('Anonymous Authors'),'P214 title and anonymous author in extracted body');
// Compare complete factual sentence spans only with declared typography folding.
const statementFold=s=>s.replace(/-\n[ \t]*(?=[a-z])/g,'').replace(/\s+/g,' ').replace(/([A-Za-z])-(?=[A-Za-z])/g,'$1');
const statementText=statementFold(pdfText.slice(0,referencesAt));
const statementAnchors=['The accompanying author verifier was run for','It exhaustively checked every state, its literal transition and orbit-derived depth, and the full predecessor set of every target against the displayed formulas.','The nine carriers contain 5,271 states, and the complete output contains 10,646 records.','Two further strict runs reproduced the canonical output byte for byte.','These finite checks do not establish the all-parameter statements.'];
const statementMatches=statementAnchors.map(text=>({text,offset:statementText.indexOf(statementFold(text))}));
for(const match of statementMatches)if(match.offset<0)findings.push({severity:'Major',reason:'updated factual statement absent from actual full PDF text',expected:match.text});
if(statementText.includes(statementFold('At this source-draft stage, no execution or computational result is claimed.')))findings.push({severity:'Major',reason:'obsolete source-stage execution statement remains in actual PDF text'});
const currentOverfull=diagnostics.flatMap(d=>d.records.filter(x=>/^Overfull /.test(x.raw)).map(x=>({file:d.file,...x})));
const repairReception={source_delta:sourceDelta,statement_matches:statementMatches,statement_scope:'Only factual-text tests join line-ending word hyphens, fold whitespace and remove intra-letter ASCII hyphens from both anchors and extracted text; full raw text retained, not RAW equality or visual closure',new_overfull_occurrences:currentOverfull,log_only_overfull_closure:currentOverfull.length===0,actual_all_page_visual_reception:'REQUIRED_SEPARATELY; no view or final artifact PASS supplied by this checker'};
const bblAnchors={
  Bors2017:['Alexander Bors','On the dynamics of endomorphisms of finite groups','Applicable Algebra in Engineering, Communication and Computing','28(3):205--214, 2017'],
  ElAbdalaouiEtAl2016:['El Houcein El Abdalaoui','Sylvain Bonnot','Ali Messaoudi','Olivier Sester','On the Fibonacci complex dynamical systems','Discrete and Continuous Dynamical Systems','36(5):2449--2471, 2016']
};
const bibliographyItems=bblKeys.map((key,i)=>{
  const start=bbl.indexOf('\\bibitem{'+key+'}'),end=i+1<bblKeys.length?bbl.indexOf('\\bibitem{'+bblKeys[i+1]+'}',start+1):bbl.indexOf('\\end{thebibliography}',start+1);
  ok(start>=0&&end>start,'complete bibliography item boundary '+key);
  const raw=bbl.slice(start,end),folded=raw.replace(/\\(?:em|newblock)\b/g,'').replace(/[{}]/g,'').replace(/~/g,' ').replace(/\s+/g,' ');
  for(const anchor of bblAnchors[key])ok(folded.includes(anchor),'actual complete BBL bibliographic field '+key+' '+anchor);
  return {key,number:bibcite.find(r=>r.key===key).number,raw_bbl:raw,anchors:bblAnchors[key],comparison_scope:'Only bibliographic anchor tests use declared TeX-command removal/brace removal/TeX-space tie conversion/whitespace folding; full raw item remains evidence, not RAW equivalence or page viewing'};
});
ok(referencesText.includes('On the dynamics of endomorphisms of finite groups')&&referencesText.includes('On the Fibonacci complex dynamical systems'),'both actual titles in extracted references');
const pageRows=manifest(rt('PAGES.sha256'));eq(pageRows.map(r=>r.path),pageLabels.map(l=>R+'/pages/'+l+'.png'),'exact actual page list');
const pageImages=pageRows.map((row,i)=>{const n='pages/'+pageLabels[i]+'.png';want(n);const b=rb(n);ok(sha(b)===row.sha256,'whole PNG pin');ok(b.length>=33&&b.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10]))&&b.readUInt32BE(8)===13&&b.subarray(12,16).toString('ascii')==='IHDR','PNG header');const width=b.readUInt32BE(16),height=b.readUInt32BE(20);ok(width>0&&height>0,'positive PNG dimensions');return{page:i+1,path:n,bytes:b.length,sha256:sha(b),width,height};});
const finalRows=manifest(rt('FINAL_PRODUCTS.sha256'));eq(finalRows.map(r=>r.path),['main.pdf','main.log','main.fls','main.aux','main.bbl','main.blg'],'fixed final manifest roles');for(const row of finalRows)ok(sha(rb('source_only/'+row.path))===row.sha256,'final product pin');
eq([...expected].sort(),[...actualNames].sort(),'complete exact recipe-derived inventory');
eq(directories.slice().sort(),['','pages/','raw/','source_only/','source_only/sections/','pass_artifacts/',...snapshots.map(s=>'pass_artifacts/'+s+'/')].sort(),'exact finite directory inventory');
const textCaptures=inventory.filter(r=>!r.path.endsWith('.pdf')&&!r.path.endsWith('.png')).map(r=>({...r,raw_utf8:rt(r.path)}));
// Finite end-of-check RAW stability; no timestamps, host metadata hierarchy or
// claim of continuous process/descendant attestation.
for(const [p,b] of bytes)ok(fs.readFileSync(p).equals(b),'whole received input unchanged '+p);
const summary={artifact_files:inventory.length,artifact_bytes:inventory.reduce((s,r)=>s+r.bytes,0),subdirectories:directories.length-1,complete_text_files:textCaptures.length,external_inputs:externalPins.length,full_raw_pairs:rawPairs.length,runtime_selected:runtime.length,sources:sources.length,pages:pageCount,fonts:fonts.length,pdf_bytes:pdf.length,pdf_sha256:sha(pdf),fls:ordered.map(r=>({pass:r.pass,events:r.events.length,counts:r.counts})),warnings:diagnostics.filter(d=>d.role==='log').map(d=>({pass:d.pass,count:d.warning_count})),findings:findings.length,text_extraction_control_occurrences:textControls.length};
const report={status:findings.length?'HOLD_ARTIFACT_FINDINGS':'DATA_CHECK_COMPLETE_PENDING_INDEPENDENT_SEMANTIC_AND_ROOT_RECEPTION',scope:'One P214 display-repair source build plus immutable initial HOLD archive; ordinary trusted tools/configuration; no host re-read, syscall closure, science, manuscript verdict or visual/PDF adoption',checks,summary,findings,provenance:{launch,continuation,grant,external_binding:binding,runtime_preflight:prep,adopted_policy:policy,staged_supplement:supplement,archived_contract:contract,p214_source_reception:sourceReception,accepted_author_pair:pairReceipt,paper_source_reception:adoptedReception,accepted_author_data:authorDataReceipt,independent_repair_source_audit:sourceAudit},adaptation:{base_checker_sha256:sha(readExternal(baseChecker)),recipe_path_delta:recipePathDelta,identifier_delta:'No P214 scientific identifier change; only exact build paths and supervisor role',recipe_role_source_delta:recipeDelta,adopted_paper_source_pins:adoptedSources,bibliography_items:bibliographyItems,repair_reception:repairReception},historical_initial:{receipt:initialReceipt,status:initialData.status,checks:initialData.checks,report_sha256:sha(initialRaw),summary:initialData.summary,findings:initialData.findings,unchanged_artifact_pins:archivePins,scope:'All161initialartifacts/oldreport/seals preserved; the six old occurrences remain historical and are not silently reclassified or erased'},source_pins:sources,runtime_pins_as_data_only:runtime,external_pins:externalPins,cold_cwd_record:rt('COLD_CWD.actual.txt'),commands,snapshots:snapshotData,raw_pairs:rawPairs,ordered_fls:ordered,diagnostics,bibliography:{keys:bibliographyKeys,bbl_order:bblKeys,final_bibcite:bibcite,source_citations:sourceCitations,labels:finalLabels,references,bibtex_role_limit:'Complete AUX/BLG/BBL top-level roles, not a BibTeX syscall trace'},fonts,pages:pageImages,text_extraction_controls:textControls,text_extraction_limit:'Raw math extraction can lose layout or encode delimiter glyphs as controls; full raw output retained, actual all-page viewing is separate',inventory,complete_text_captures:textCaptures};
process.stdout.write(JSON.stringify(report,null,2)+'\n');
if(findings.length)process.exitCode=1;
