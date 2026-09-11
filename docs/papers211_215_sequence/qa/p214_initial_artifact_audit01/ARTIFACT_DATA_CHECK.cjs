'use strict';
// Independent P214 initial-build artifact DATA receiver; exact delta from accepted P212 A.
// Read-only; no producer import, host-manifest follow, child, repair, build or write API.
const fs=require('node:fs'), path=require('node:path'), crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics', Q=W+'/docs/papers211_215_sequence/qa/';
const P=Q+'p214_initial_build_preparation01', B=Q+'p214_initial_build_binding01', I=Q+'p212_a_build_preparation01';
const S=W+'/papers/214-nilpotent-bilinear-clock', R=Q+'p214_initial_build_run01', C=R+'/source_only';
const A=Q+'p214_runtime_root01', Z=Q+'p214_source_root01';
const INPUT_PINS=Q+'p214_initial_artifact_audit01/INPUT_PINS.sha256';
const baseChecker=Q+'p212_a_build_artifact_audit01/ARTIFACT_DATA_CHECK.cjs';
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
const fixedExternal=[...['BUILD_REQUEST.proposed.sh.txt','NATIVE_REQUEST.proposed.json','PROPOSED_SOURCE_ONLY.sha256'].map(n=>P+'/'+n),...['BUILD_REQUEST.proposed.sh.txt','NATIVE_REQUEST.proposed.json'].map(n=>I+'/'+n),Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md',Q+'p212_plain_build_source_root01/RECEPTION.md',Q+'p212_plain_build_source_proposal03/CONTRACT.md',Q+'p212_a_build_artifact_root01/RECEPTION.md',baseChecker,...['GRANT.md','ACTUAL_NATIVE.json','CONTINUATION_NATIVE.json','RUNTIME_PREFLIGHT_NATIVE.json','BINDING_NATIVE.json','RUNTIME_INPUTS.sha256','SOURCE_RECEPTION.md'].map(n=>B+'/'+n),A+'/PAIR_RECEPTION.md',Z+'/SOURCE_RECEPTION.md',Z+'/ADOPTED_SOURCE_INPUTS.sha256',...sourceNames.map(n=>S+'/'+n)];
const externalAllowed=new Set(fixedExternal);
externalAllowed.add(INPUT_PINS);
function readExternal(p){ok(externalAllowed.has(p),'external path allowlist '+p);if(!bytes.has(p)){const st=fs.lstatSync(p);ok(st.isFile()&&!st.isSymbolicLink(),'external regular '+p);const b=fs.readFileSync(p);bytes.set(p,b);externalPins.push({path:p,bytes:b.length,sha256:sha(b)});}return bytes.get(p);}
function decode(b){const t=b.toString('utf8');ok(Buffer.from(t,'utf8').equals(b),'lossless UTF-8');return t;}
const xt=p=>decode(readExternal(p));
const ls=t=>{ok(!t.includes('\r'),'LF-only grammar');return t===''?[]:(ok(t.endsWith('\n'),'terminal LF'),t.slice(0,-1).split('\n'));};
const manifest=t=>{const rows=ls(t).map(l=>{const m=/^([0-9a-f]{64})  ([^\r\n]+)$/.exec(l);ok(!!m,'manifest syntax');return {sha256:m[1],path:m[2]};});ok(new Set(rows.map(r=>r.path)).size===rows.length,'unique manifest names');return rows;};
function sameBuffers(a,b,label){ok(a.equals(b),'RAW equality '+label);rawPairs.push({label,bytes:a.length,sha256:sha(a)});}
const pinnedDocuments=manifest(xt(INPUT_PINS));
eq(pinnedDocuments.map(r=>r.path),fixedExternal.map(p=>p.slice(W.length+1)).sort(),'exact complete documentary input pin set');
for(const row of pinnedDocuments)ok(sha(readExternal(W+'/'+row.path))===row.sha256,'whole pinned document '+row.path);
// The accepted old checker is read as bytes only, never imported or rerun.
ok(sha(readExternal(baseChecker))==='8c85429624153bd58bfeb483f55866c3e1559a01aa05a052802c4f8efe83d015','accepted P212 A receiver source identity');
ok(sha(readExternal(Q+'p212_a_build_artifact_root01/RECEPTION.md'))==='b32e54e33a5330c2cdbb3b0332d913a6054ab5cbc7a40f58fb5038b752662bdf'&&xt(Q+'p212_a_build_artifact_root01/RECEPTION.md').includes('ACCEPTED_A_BUILD_ARTIFACT_ONLY'),'accepted baseline scope, not P214 output reuse');
const replaceLiteral=(text,from,to,label)=>{ok(text.split(from).length===2,'one literal '+label);return text.replace(from,to);};
const baseRecipe=xt(I+'/BUILD_REQUEST.proposed.sh.txt');
ok(sha(readExternal(I+'/BUILD_REQUEST.proposed.sh.txt'))==='811a7b4026a1d972072a96f25d3b7374cb926944ce820a77adc0313de78201d3','accepted base recipe identity');
const recipePathDelta=[
  [I,P],[W+'/papers/212-closed-pointer-orbits',S],
  [Q+'p212_a_build_binding01',B],[W+'/docs/papers211_215_sequence/reviews/p212_a/build01',R]
];
let expectedRecipe=baseRecipe;
for(const [from,to] of recipePathDelta)expectedRecipe=replaceLiteral(expectedRecipe,from,to,'recipe path');
expectedRecipe=expectedRecipe.replaceAll('P212','P214').replaceAll('p212','p214');
const recipeDelta=[
  ['# PROPOSED SOURCE ONLY. Never run before root receives the A strict pair,','# PROPOSED SOURCE ONLY. Never run before root receives the author strict pair,'],
  ['# documentary delta, exact request and finite runtime/trust binding.','# current source, exact request and fresh finite runtime/trust binding.'],
  ['P214_A_BUILD_SUPERVISOR_EXIT','P214_INITIAL_BUILD_SUPERVISOR_EXIT'],
  ['P214_SOURCES=(main.tex math_commands.tex references.bib sections/01_setup.tex sections/02_returns.tex sections/03_period_set.tex sections/04_census.tex sections/05_scope.tex)','P214_SOURCES=('+sourceNames.join(' ')+')'],
  ['SECTION_MEMBERS[@]}" == 5','SECTION_MEMBERS[@]}" == 6'],
  ['sections/01_setup.tex|sections/02_returns.tex|sections/03_period_set.tex|sections/04_census.tex|sections/05_scope.tex',sourceNames.filter(n=>n.startsWith('sections/')).join('|')],
  ['# No PDF adoption, final Review A PASS, Round1 or package seal is produced here.','# No PDF adoption, initial artifact acceptance, Round0 or package seal is produced here.']
];
for(const [from,to] of recipeDelta)expectedRecipe=replaceLiteral(expectedRecipe,from,to,'recipe role/source delta');
ok(xt(P+'/BUILD_REQUEST.proposed.sh.txt')===expectedRecipe,'whole exact recipe adaptation; other body unchanged');
ok(sha(readExternal(P+'/BUILD_REQUEST.proposed.sh.txt'))==='f81626f9bc257b6be0aa53e5790da29b020fafd92a0a21cfe84072df2b68aa7d','accepted P214 recipe content identity');
const proposal=JSON.parse(xt(P+'/NATIVE_REQUEST.proposed.json')), baseRequest=JSON.parse(xt(I+'/NATIVE_REQUEST.proposed.json'));
ok(sha(readExternal(I+'/NATIVE_REQUEST.proposed.json'))==='2c2a6b4d2b0a837cc47b9c8600a2975f8d57ce68d07b27c13390122d9172a189','accepted base request identity');
ok(sha(readExternal(P+'/NATIVE_REQUEST.proposed.json'))==='0fb2cfc07ca7dea77306d9c5f64ddf9a4ccb143ad37a963667462f1a1b74a64e','whole root-read P214 request bytes');
const expectedNative=JSON.parse(JSON.stringify(baseRequest.proposed_native_request));
expectedNative.arguments.cmd=replaceLiteral(expectedNative.arguments.cmd,I,P,'native recipe path');
eq(proposal.proposed_native_request,expectedNative,'entire native vector unchanged except exact recipe path');
eq(proposal.environment,baseRequest.environment,'all thirteen fixed environment variables');
eq(proposal.build_sequence,baseRequest.build_sequence,'unchanged four-pass sequence');
eq(proposal.source_list,sourceNames,'exact nine proposed sources');
eq(proposal.proposed_cwd_check.expected_counts,{root:4,sections:6,source_files:9},'four-root six-section source staging');
eq(proposal.bibliography_keys,bibliographyKeys,'exact P214 two bibliography roles');
ok(proposal.schema==='P214_INITIAL_BUILD_SOURCE_ONLY_REQUEST_V1'&&!proposal.operation_authorized&&proposal.root_grant===null,'source request is not a grant');
ok(proposal.source_root===S&&proposal.proposed_output_directory===R&&proposal.supervisor_status_label==='P214_INITIAL_BUILD_SUPERVISOR_EXIT','P214 source/output/native roles');
const launch=JSON.parse(xt(B+'/ACTUAL_NATIVE.json')), continuation=JSON.parse(xt(B+'/CONTINUATION_NATIVE.json'));
eq(launch.arguments,proposal.proposed_native_request.arguments,'whole actual P214 native request');
ok(launch.result.chunk_id==='b39b7b'&&launch.result.session_id===95222&&launch.result.output===''&&!Object.hasOwn(launch.result,'exit_code'),'actual original launch');
eq(continuation.arguments,{session_id:95222,chars:'',yield_time_ms:1000,max_output_tokens:2000},'only actual continuation; waiting controls recorded not invented');
ok(continuation.result.chunk_id==='0f0b87'&&continuation.result.exit_code===0&&!Object.hasOwn(continuation.result,'session_id'),'actual sole completion received by root');
ok(continuation.result.output==='P214_INITIAL_BUILD_SUPERVISOR_EXIT=0\n','whole native completion stream');
const grant=xt(B+'/GRANT.md'),policy=xt(Q+'p212_plain_build_source_root01/RECEPTION.md'),sourceReception=xt(B+'/SOURCE_RECEPTION.md');
const supplement=xt(Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md'),contract=xt(Q+'p212_plain_build_source_proposal03/CONTRACT.md');
const pairReceipt=xt(A+'/PAIR_RECEPTION.md'),adoptedReception=xt(Z+'/SOURCE_RECEPTION.md');
ok(grant.includes('ISSUED_AND_CONSUMED_BEFORE_NEXT_SINGLE_SUBMISSION.')&&grant.includes('No retry, cleanup'),'explicit consumed initial grant and no retry');
ok(policy.includes('P212-POLICY-TIME1 is therefore CLOSED')&&policy.includes('supplement has precedence'),'adopted staged policy');
ok(sha(readExternal(Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md'))==='055b06bc5e47ffa1fd6459101e473c86808fbfe44a2d56f186012efb9fa2f1b3','unchanged staged supplement');
ok(sha(readExternal(B+'/SOURCE_RECEPTION.md'))==='419de630121109e1a2d8badd18c13d132951bf852112af4d4794268953cf4f1b'&&sourceReception.includes('Root explicitly adopts the already accepted ordinary-tool policy and staged'),'P214 explicit source/policy adoption');
ok(sha(readExternal(A+'/PAIR_RECEPTION.md'))==='0bc99d9ec61ae8fe36151fd081654c53e2a077038b66c41244a0a3d76ba8cfc3'&&pairReceipt.includes('ACCEPT_AUTHOR_STRICT_PAIR_UNCHANGED_SEMANTICS_REUSE'),'actual author pair acceptance, not new science');
ok(sha(readExternal(Z+'/SOURCE_RECEPTION.md'))==='580d6531617ee0ebb5aee511477ca8cda1a5ab896b83bb3d6d0f17897b372f7f'&&adoptedReception.includes('ACCEPT_SOURCE_ONLY'),'accepted paper-source provenance');
const sourceManifest=readExternal(P+'/PROPOSED_SOURCE_ONLY.sha256');
ok(sha(sourceManifest)==='7844ffa35be54db6b98ba131882bae2d6059ec11fb6609fbbf92d428dc1d596e','P214 initial nine-source manifest pin');
const sources=manifest(decode(sourceManifest));eq(sources.map(r=>r.path),sourceNames,'nine exact current source roles');
const adoptedManifest=readExternal(Z+'/ADOPTED_SOURCE_INPUTS.sha256');
ok(sha(adoptedManifest)==='1b9e81528623d20a433b7d180c4b9785319ea39df3ce19c1829be0333e7c9444','adopted paper-source manifest identity');
const adoptedSources=manifest(decode(adoptedManifest));ok(adoptedSources.length===28,'complete adopted documentary key as data');
for(const row of sources)ok(adoptedSources.some(r=>r.path===S.slice(W.length+1)+'/'+row.path&&r.sha256===row.sha256),'each selected build role is actually adopted '+row.path);
const runtimeManifest=readExternal(B+'/RUNTIME_INPUTS.sha256');
ok(sha(runtimeManifest)==='35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530','fresh selected manifest pin');
const runtime=manifest(decode(runtimeManifest));ok(runtime.length===223&&runtime.every(r=>path.isAbsolute(r.path)),'finite selected runtime names as archival DATA only');
const runtimeByName=new Map(runtime.map(r=>[r.path,r]));
const binding=JSON.parse(xt(B+'/BINDING_NATIVE.json'));
ok(binding.result.exit_code===0&&binding.result.chunk_id==='c86afe','actual external binding native result');
const boundNames=[P+'/BUILD_REQUEST.proposed.sh.txt',P+'/NATIVE_REQUEST.proposed.json',P+'/PROPOSED_SOURCE_ONLY.sha256',B+'/RUNTIME_INPUTS.sha256',B+'/SOURCE_RECEPTION.md',Q+'p212_plain_build_source_root01/RECEPTION.md',Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md',A+'/PAIR_RECEPTION.md'];
const diskObservation='Filesystem       1B-blocks        Used   Available Use% Mounted on\n/dev/md0       53687091200 38973558784 14713532416  73% /root/autodl-tmp\n';
const boundOutput=path.dirname(R)+'\n'+diskObservation+boundNames.map(p=>sha(readExternal(p))+'  '+p.slice(W.length+1)+'\n').join('');
ok(binding.result.output===boundOutput,'whole physical-parent/capacity/eight-pin archival binding output');
const bindingCommand=['set -e','cmp docs/papers211_215_sequence/qa/p212_a_build_binding01/RUNTIME_INPUTS.sha256 docs/papers211_215_sequence/qa/p214_initial_build_binding01/RUNTIME_INPUTS.sha256','[ -d docs/papers211_215_sequence/qa ]','[ ! -L docs/papers211_215_sequence/qa ]','(cd docs/papers211_215_sequence/qa && pwd -P)','[ ! -e docs/papers211_215_sequence/qa/p214_initial_build_run01 ]','[ ! -L docs/papers211_215_sequence/qa/p214_initial_build_run01 ]','df -B1 docs/papers211_215_sequence/qa','sha256sum '+boundNames.map(p=>p.slice(W.length+1)).join(' ')].join('\n');
eq(binding.arguments,{cmd:bindingCommand,login:false,max_output_tokens:2500},'whole actual copy-comparison/parent/absence/capacity request as archived DATA');
const prep=JSON.parse(xt(B+'/RUNTIME_PREFLIGHT_NATIVE.json'));
const runtimeOK=runtime.map(r=>r.path+': OK\n').join('');
eq(prep.arguments,{cmd:'sha256sum -c --strict docs/papers211_215_sequence/qa/p212_a_build_binding01/RUNTIME_INPUTS.sha256',login:false,max_output_tokens:15000},'whole fresh preflight request as DATA');
ok(prep.result.chunk_id==='900070'&&prep.result.exit_code===0&&prep.result.output===runtimeOK,'all 223 received fresh pregrant OK rows and whole output');

// The only enumerated tree is the completed, fixed workspace output.
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
  const live=readExternal(S+'/'+row.path),cold=rb('source_only/'+row.path);
  ok(sha(live)===row.sha256,'whole live accepted initial source pin '+row.path);
  sameBuffers(live,cold,'accepted live initial source == complete cold copy '+row.path);
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
const report={status:findings.length?'HOLD_ARTIFACT_FINDINGS':'DATA_CHECK_COMPLETE_PENDING_INDEPENDENT_SEMANTIC_AND_ROOT_RECEPTION',scope:'One P214 initial source build, ordinary trusted tools/configuration; no host re-read, syscall closure, science, final manuscript verdict or visual/PDF adoption',checks,summary,findings,provenance:{launch,continuation,grant,external_binding:binding,runtime_preflight:prep,adopted_policy:policy,staged_supplement:supplement,archived_contract:contract,p214_source_reception:sourceReception,accepted_author_pair:pairReceipt,paper_source_reception:adoptedReception},adaptation:{base_checker_sha256:sha(readExternal(baseChecker)),recipe_path_delta:recipePathDelta,identifier_delta:'P212/p212 to P214/p214 throughout reviewed recipe',recipe_role_source_delta:recipeDelta,adopted_paper_source_pins:adoptedSources,bibliography_items:bibliographyItems},source_pins:sources,runtime_pins_as_data_only:runtime,external_pins:externalPins,cold_cwd_record:rt('COLD_CWD.actual.txt'),commands,snapshots:snapshotData,raw_pairs:rawPairs,ordered_fls:ordered,diagnostics,bibliography:{keys:bibliographyKeys,bbl_order:bblKeys,final_bibcite:bibcite,source_citations:sourceCitations,labels:finalLabels,references,bibtex_role_limit:'Complete AUX/BLG/BBL top-level roles, not a BibTeX syscall trace'},fonts,pages:pageImages,text_extraction_controls:textControls,text_extraction_limit:'Raw math extraction can lose layout or encode delimiter glyphs as controls; full raw output retained, actual all-page viewing is separate',inventory,complete_text_captures:textCaptures};
process.stdout.write(JSON.stringify(report,null,2)+'\n');
if(findings.length)process.exitCode=1;
