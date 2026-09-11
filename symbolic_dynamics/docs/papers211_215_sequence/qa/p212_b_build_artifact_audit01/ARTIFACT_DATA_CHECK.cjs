'use strict';
// P212 Review B build DATA receiver SOURCE; exact delta from accepted A receiver. Read-only; no child process,
// proposed-source import, host-manifest follow, repair, build or write API.
const fs=require('node:fs'), path=require('node:path'), crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics', Q=W+'/docs/papers211_215_sequence/qa/';
const P=Q+'p212_b_build_preparation01', B=Q+'p212_b_build_binding01', I=Q+'p212_plain_build_source_proposal03';
const S=W+'/papers/212-closed-pointer-orbits', H=S+'/qa_initial/plain_build01/source_only';
const R=W+'/docs/papers211_215_sequence/reviews/p212_b/build01', C=R+'/source_only';
const A=Q+'p212_a_source_root01', V=W+'/docs/papers211_215_sequence/reviews/p212_a/source_revision01';
const T=Q+'p212_b_source_root01';
const baseChecker=Q+'p212_a_build_artifact_audit01/ARTIFACT_DATA_CHECK.cjs';
const sourceNames=['main.tex','math_commands.tex','references.bib','sections/01_setup.tex','sections/02_returns.tex','sections/03_period_set.tex','sections/04_census.tex','sections/05_scope.tex'];
const products=['main.aux','main.bbl','main.blg','main.log','main.fls','main.out','main.toc','main.pdf'];
const passes=['pass1','bibtex','pass2','pass3'];
const snapshots=passes.flatMap(p=>[p+'.before',p+'.after']);
const bibliographyKeys=['berdine2006','holroyd2008','loginov2007','manna1987','pham2015'];
let checks=0;
function ok(v,m){checks++;if(!v)throw Error(m);}
function eq(a,b,m){ok(JSON.stringify(a)===JSON.stringify(b),m);}
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const bytes=new Map(), externalPins=[], rawPairs=[], findings=[];
const fixedExternal=[...['BUILD_REQUEST.proposed.sh.txt','NATIVE_REQUEST.proposed.json','PROPOSED_SOURCE_ONLY.sha256'].flatMap(n=>[P+'/'+n,I+'/'+n]),Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md',Q+'p212_plain_build_source_root01/RECEPTION.md',Q+'p212_a_build_artifact_root01/RECEPTION.md',baseChecker,...['GRANT.md','ACTUAL_NATIVE.json','CONTINUATION_NATIVE.json','RUNTIME_PREFLIGHT_NATIVE.json','BINDING_NATIVE.json','RUNTIME_INPUTS.sha256','SOURCE_RECEPTION.md'].map(n=>B+'/'+n),T+'/PAIR_RECEPTION.md',A+'/CITATION_REPAIR.md',V+'/CITATION_CLOSURE.md',...sourceNames.flatMap(n=>[H+'/'+n,S+'/'+n])];
const externalAllowed=new Set(fixedExternal);
function readExternal(p){ok(externalAllowed.has(p),'external path allowlist '+p);if(!bytes.has(p)){const st=fs.lstatSync(p);ok(st.isFile()&&!st.isSymbolicLink(),'external regular '+p);const b=fs.readFileSync(p);bytes.set(p,b);externalPins.push({path:p,bytes:b.length,sha256:sha(b)});}return bytes.get(p);}
function decode(b){const t=b.toString('utf8');ok(Buffer.from(t,'utf8').equals(b),'lossless UTF-8');return t;}
const xt=p=>decode(readExternal(p));
const ls=t=>{ok(!t.includes('\r'),'LF-only grammar');return t===''?[]:(ok(t.endsWith('\n'),'terminal LF'),t.slice(0,-1).split('\n'));};
const manifest=t=>{const rows=ls(t).map(l=>{const m=/^([0-9a-f]{64})  ([^\r\n]+)$/.exec(l);ok(!!m,'manifest syntax');return {sha256:m[1],path:m[2]};});ok(new Set(rows.map(r=>r.path)).size===rows.length,'unique manifest names');return rows;};
function sameBuffers(a,b,label){ok(a.equals(b),'RAW equality '+label);rawPairs.push({label,bytes:a.length,sha256:sha(a)});}
// Bind accepted prior SOURCE as bytes only; never import or rerun that checker.
ok(sha(readExternal(baseChecker))==='8c85429624153bd58bfeb483f55866c3e1559a01aa05a052802c4f8efe83d015','accepted A receiver source identity');
ok(xt(Q+'p212_a_build_artifact_root01/RECEPTION.md').includes('ACCEPTED_A_BUILD_ARTIFACT_ONLY'),'accepted A artifact baseline, not B artifact acceptance');
const replaceLiteral=(text,from,to,label)=>{ok(text.split(from).length===2,'one literal '+label);return text.replace(from,to);};
const initialRecipe=xt(I+'/BUILD_REQUEST.proposed.sh.txt');
ok(sha(readExternal(I+'/BUILD_REQUEST.proposed.sh.txt'))==='8d40a51735984e517c10d564019f5c598657d8b31b0d80034753999c96a867a0','accepted initial recipe identity');
const recipeDelta=[
  ['# PROPOSED SOURCE ONLY. Never run before root receives the strict pair,','# PROPOSED SOURCE ONLY. Never run before root receives the B strict pair,'],
  [I,P],[Q+'p212_plain_build_binding01',B],[S+'/qa_initial/plain_build01',R],
  ['P212_INITIAL_BUILD_SUPERVISOR_EXIT','P212_B_BUILD_SUPERVISOR_EXIT'],
  ['# No PDF adoption, Round0, visual PASS or package seal is produced here.','# No PDF adoption, final Review B PASS, Round2 or package seal is produced here.']
];
let expectedRecipe=initialRecipe;for(const [from,to] of recipeDelta)expectedRecipe=replaceLiteral(expectedRecipe,from,to,'recipe delta');
ok(xt(P+'/BUILD_REQUEST.proposed.sh.txt')===expectedRecipe,'whole exact six-line recipe adaptation');
ok(sha(readExternal(P+'/BUILD_REQUEST.proposed.sh.txt'))==='73b189645ceea295bf5ff9fe4ca3edd95f66a44a8006ca23ad163f8ec16991af','B recipe content identity');
const proposal=JSON.parse(xt(P+'/NATIVE_REQUEST.proposed.json'));
const initialRequest=JSON.parse(xt(I+'/NATIVE_REQUEST.proposed.json'));
ok(sha(readExternal(I+'/NATIVE_REQUEST.proposed.json'))==='023381134cb65b8e7a602365156988587a5159fa1ea0a3cdb3e3e4bb470c7f27','accepted initial request identity');
const expectedRequest=JSON.parse(JSON.stringify(initialRequest));
expectedRequest.schema='P212_REVIEW_B_BUILD_SOURCE_ONLY_REQUEST_V1';
expectedRequest.proposed_native_request.arguments.cmd=replaceLiteral(expectedRequest.proposed_native_request.arguments.cmd,I,P,'native recipe path');
expectedRequest.source_hash_manifest='docs/papers211_215_sequence/qa/p212_b_build_preparation01/PROPOSED_SOURCE_ONLY.sha256';
expectedRequest.runtime_manifest.path='docs/papers211_215_sequence/qa/p212_b_build_binding01/RUNTIME_INPUTS.sha256';
expectedRequest.runtime_manifest.scope='PENDING_FRESH_ROOT_REVALIDATION: the accepted initial P212 223-row selected manifest is an archival candidate, not a current Review B key. The adopted staged supplement governs actual new-cwd checks within the separately granted command.';
expectedRequest.proposed_output_directory=R;
expectedRequest.acceptance='Actual B strict pair acceptance precedes build. Root receives this exact adaptation/current eight citation-repaired sources, the already adopted ordinary policy plus staged supplement, fresh selected223 resource/configuration binding and output parent, then separately grants one staged Review B build. New COLD guard precedes TeX within that command. Complete new artifacts/all-page views and reviewer acceptance remain required; no final B PASS, Round2 or terminal credit is produced.';
expectedRequest.supervisor_status_label='P212_B_BUILD_SUPERVISOR_EXIT';
expectedRequest.runtime_candidate={path:'docs/papers211_215_sequence/qa/p212_plain_build_binding01/RUNTIME_INPUTS.sha256',entries:223,sha256:'35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530',current_host_paths_checked:false};
expectedRequest.policy_evidence=['docs/papers211_215_sequence/qa/p212_plain_build_source_root01/RECEPTION.md','docs/papers211_215_sequence/qa/p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md'];
expectedRequest.citation_evidence=['docs/papers211_215_sequence/qa/p212_a_source_root01/CITATION_REPAIR.md','docs/papers211_215_sequence/reviews/p212_a/source_revision01/CITATION_CLOSURE.md'];
eq(proposal,expectedRequest,'whole exact B request role/path delta');
ok(sha(readExternal(P+'/NATIVE_REQUEST.proposed.json'))==='45f59e775a64c2734f6b1751e9d154a6c0ce5bd6bc8956106611923107fe8829','B request content identity');
const launch=JSON.parse(xt(B+'/ACTUAL_NATIVE.json')), continuation=JSON.parse(xt(B+'/CONTINUATION_NATIVE.json'));
eq(launch.arguments,proposal.proposed_native_request.arguments,'whole actual B native request');
ok(launch.result.chunk_id==='ee7d1b'&&launch.result.session_id===98167&&launch.result.output===''&&!Object.hasOwn(launch.result,'exit_code'),'actual B original launch');
eq(continuation.arguments,{session_id:launch.result.session_id,chars:'',yield_time_ms:1000,max_output_tokens:2000},'only real B continuation');
ok(continuation.result.chunk_id==='30adba'&&continuation.result.exit_code===0&&!Object.hasOwn(continuation.result,'session_id'),'actual B sole completion received by root');
ok(continuation.result.output==='P212_B_BUILD_SUPERVISOR_EXIT=0\n','complete native B completion stream');
const grant=xt(B+'/GRANT.md'), policy=xt(Q+'p212_plain_build_source_root01/RECEPTION.md'), aReception=xt(B+'/SOURCE_RECEPTION.md');
const pairReceipt=xt(T+'/PAIR_RECEPTION.md'),citationRepair=xt(A+'/CITATION_REPAIR.md'),citationClosure=xt(V+'/CITATION_CLOSURE.md');
ok(grant.includes('ISSUED_AND_CONSUMED_BEFORE_NEXT_SINGLE_SUBMISSION.')&&grant.includes('No retry, cleanup, resumed tree'),'explicit consumed B grant');
ok(policy.includes('P212-POLICY-TIME1 is therefore CLOSED')&&policy.includes('supplement has precedence'),'adopted staged policy');
ok(sha(readExternal(B+'/SOURCE_RECEPTION.md'))==='964a4e8081d45057e3ed10c713e30f0f5d9cfa850ffb63086c09c9e270b34ae3'&&aReception.includes('Root explicitly adopts the already accepted ordinary-tool policy and staged'),'B source/policy acceptance');
ok(sha(readExternal(T+'/PAIR_RECEPTION.md'))==='3b3902a4790cf82321ac2c28d1b7cc989f35917f42f798facc14a27f23bae527'&&pairReceipt.includes('# P212 B actual strict pair accepted'),'received prior B pair, not new science');
ok(sha(readExternal(A+'/CITATION_REPAIR.md'))==='206eae16708daf0b975472d46e5ea404564c3c019698f3ced3e6396dc782a842','root exact citation repair');
ok(sha(readExternal(V+'/CITATION_CLOSURE.md'))==='f4b91448ba570b97423b8cab5f86eb894e7f19488e47ebf46bd5257493f57ade'&&citationClosure.includes('P212-A-M1 is CLOSED.'),'same-A exact citation closure');
const sourceManifest=readExternal(P+'/PROPOSED_SOURCE_ONLY.sha256');
ok(sha(sourceManifest)==='ac6a5776e0f42298fcd0212ac681f0881549680d05361fe8bd15546c51dcc3a1','B source manifest pin');
const sources=manifest(decode(sourceManifest));eq(sources.map(r=>r.path),sourceNames,'eight exact B sources');
const initialSourceManifest=readExternal(I+'/PROPOSED_SOURCE_ONLY.sha256');
ok(sha(initialSourceManifest)==='fe4abe8535901fbb1e6dd8c63038e0ecef03c9ea5a5d05619559d452494a8288','initial source baseline manifest pin');
const initialSources=manifest(decode(initialSourceManifest));eq(initialSources.map(r=>r.path),sourceNames,'eight exact initial sources');
const runtimeManifest=readExternal(B+'/RUNTIME_INPUTS.sha256');
ok(sha(runtimeManifest)==='35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530','freshly received B selected manifest pin');
const runtime=manifest(decode(runtimeManifest));ok(runtime.length===223&&runtime.every(r=>path.isAbsolute(r.path)),'received finite runtime names');
const runtimeByName=new Map(runtime.map(r=>[r.path,r]));
const binding=JSON.parse(xt(B+'/BINDING_NATIVE.json'));
ok(binding.result.exit_code===0&&binding.result.chunk_id==='d06a3a','B external binding native result');
const boundNames=[P+'/BUILD_REQUEST.proposed.sh.txt',P+'/NATIVE_REQUEST.proposed.json',P+'/PROPOSED_SOURCE_ONLY.sha256',B+'/RUNTIME_INPUTS.sha256',B+'/SOURCE_RECEPTION.md',Q+'p212_plain_build_source_root01/RECEPTION.md',Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md',T+'/PAIR_RECEPTION.md'];
const capacityRecord='Filesystem       1B-blocks        Used   Available Use% Mounted on\n/dev/md0       53687091200 39095754752 14591336448  73% /root/autodl-tmp\n';
const boundOutput=path.dirname(R)+'\n'+capacityRecord+boundNames.map(p=>sha(readExternal(p))+'  '+p.slice(W.length+1)+'\n').join('');
ok(binding.result.output===boundOutput,'whole B parent capacity and eight external content pins');
const bindingCommand=['set -e','cmp docs/papers211_215_sequence/qa/p212_a_build_binding01/RUNTIME_INPUTS.sha256 docs/papers211_215_sequence/qa/p212_b_build_binding01/RUNTIME_INPUTS.sha256','[ -d docs/papers211_215_sequence/reviews/p212_b ]','[ ! -L docs/papers211_215_sequence/reviews/p212_b ]','(cd docs/papers211_215_sequence/reviews/p212_b && pwd -P)','[ ! -e docs/papers211_215_sequence/reviews/p212_b/build01 ]','[ ! -L docs/papers211_215_sequence/reviews/p212_b/build01 ]','df -B1 docs/papers211_215_sequence/reviews/p212_b','sha256sum '+boundNames.map(p=>p.slice(W.length+1)).join(' ')].join('\n');
eq(binding.arguments,{cmd:bindingCommand,max_output_tokens:2500},'whole actual B parent/absence/capacity binding request; cwd implicit in retained native request');
const prep=JSON.parse(xt(B+'/RUNTIME_PREFLIGHT_NATIVE.json'));
const runtimeOK=runtime.map(r=>r.path+': OK\n').join('');
eq(prep.arguments,{cmd:'sha256sum --check --strict docs/papers211_215_sequence/qa/p212_a_build_binding01/RUNTIME_INPUTS.sha256',workdir:W,max_output_tokens:18000},'whole fresh B preflight request as DATA');
ok(prep.result.chunk_id==='9b1e27'&&prep.result.exit_code===0&&prep.result.output===runtimeOK,'all received fresh B pregrant runtime OK rows and full output');
const sourceDelta=[
  {path:'references.bib',from:'  note = {Primary preprint; Theorem 3.8 and Corollary 4.10}\n',to:'  note = {Primary preprint; Theorem 3.8, Lemma 4.9 and Corollary 4.10}\n'},
  {path:'sections/01_setup.tex',from:'Holroyd et al.\\ \\cite[Theorem~3.8]{holroyd2008}.\n',to:'Holroyd et al.\\ \\cite[Lemma~4.9]{holroyd2008}.\n'}
];

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
  const original=readExternal(H+'/'+row.path),live=readExternal(S+'/'+row.path),cold=rb('source_only/'+row.path);
  ok(sha(original)===initialSources.find(r=>r.path===row.path).sha256,'accepted initial cold source pin '+row.path);
  const delta=sourceDelta.find(r=>r.path===row.path);
  const expectedA=delta?Buffer.from(replaceLiteral(decode(original),delta.from,delta.to,'one accepted citation source line '+row.path),'utf8'):original;
  ok(sha(expectedA)===row.sha256,'exact two-line delta gives current B source pin '+row.path);
  sameBuffers(expectedA,live,'accepted initial source plus exact A delta == live '+row.path);
  sameBuffers(expectedA,cold,'accepted initial source plus exact A delta == B cold '+row.path);
  want('source_only/'+row.path);
}
ok(rt('controller.exit')==='0\n'&&rt('controller.stdout.raw')===''&&rt('controller.stderr.raw')==='','full controller success streams');
ok(rt('STATUS.txt')==='CAPTURED_PENDING_FULL_LOG_FLS_CONFIG_PDF_AND_ACTUAL_ALL_PAGE_RECEPTION\n','capture-only status, not acceptance');
const coldRecord=['commands=Bash pwd -P; dotglob/nullglob fixed (*) and (sections/*); exact membership/type/absence tests','expected_cwd='+C,'actual_physical_cwd='+C,'cold_member_count=4',...['main.tex','math_commands.tex','references.bib','sections'].map(n=>'cold_member='+n),'section_member_count=5',...sourceNames.filter(n=>n.startsWith('sections/')).map(n=>'section_member='+n),'relative_tree=texmf ABSENT','relative_tree=.texlive2021 ABSENT','EXACT_TWO_DIRECTORY_MEMBERSHIP_TYPES_AND_RELATIVE_TREE_ABSENCE_CHECKS_PASSED'].join('\n')+'\n';
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
    else if(sourceNames.includes(local)){role='declared-source';pin=sources.find(r=>r.path===local).sha256;}
    else if(outputs.has(local)){role='earlier-same-pass-output';pin=after.get(local).sha256;}
    else if(before.has(local)){role='generated-before';pin=before.get(local).sha256;}
    else{role='UNKNOWN_INPUT';findings.push({severity:'Major',pass,line:i+1,raw:line,reason:'unreceived recorder input; no host follow allowed'});}
    counts[role]=(counts[role]||0)+1;events.push({line:i+1,raw:line,kind,spelling,lexical_absolute:absolute,local,role,evidence_content_sha256:pin});
  }
  ok(counts.cwd===1,'exactly one FLS cwd');eq([...outputs].sort(),['main.aux','main.log','main.pdf'],'actual TeX output roles');
  eq([...new Set(events.filter(e=>e.role==='declared-source').map(e=>e.local))].sort(),sourceNames.filter(n=>n.endsWith('.tex')).sort(),'all seven TeX sources accounted for');
  ordered.push({pass,events,counts});
}

const texText=sourceNames.filter(n=>n.endsWith('.tex')).map(n=>rt('source_only/'+n)).join('\n');
const sourceCitations=[...texText.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
eq([...new Set(sourceCitations)].sort(),bibliographyKeys,'five source citations');
const bibSource=rt('source_only/references.bib'),bibKeys=[...bibSource.matchAll(/^@[A-Za-z]+\{([^,]+),/gm)].map(m=>m[1]);eq(bibKeys.slice().sort(),bibliographyKeys,'five unchanged Bib entries');
const auxBefore=rt('pass_artifacts/bibtex.before/main.aux'),auxFinal=rt('source_only/main.aux'),bbl=rt('source_only/main.bbl'),blg=rt('source_only/main.blg');
const citationKeys=t=>[...t.matchAll(/^\\citation\{([^}]+)\}$/gm)].flatMap(m=>m[1].split(','));
eq(citationKeys(auxBefore),sourceCitations,'real AUX-before citations');eq(citationKeys(auxFinal),sourceCitations,'final AUX citations');
for(const aux of [auxBefore,auxFinal]){eq([...aux.matchAll(/^\\bibstyle\{([^}]+)\}$/gm)].map(m=>m[1]),['plain'],'exact bibliography style');eq([...aux.matchAll(/^\\bibdata\{([^}]+)\}$/gm)].map(m=>m[1]),['references'],'exact bibliography database');ok(!aux.includes('\\@input'),'no unreceived nested AUX');}
ok(!auxBefore.includes('\\bibcite'),'cold AUX has no fabricated previous bibliography mapping');
const bblKeys=[...bbl.matchAll(/^\\bibitem\{([^}]+)\}$/gm)].map(m=>m[1]);eq(bblKeys.slice().sort(),bibliographyKeys,'five actual BBL items, no duplicates');
const bibcite=[...auxFinal.matchAll(/^\\bibcite\{([^}]+)\}\{([^}]+)\}$/gm)].map(m=>({key:m[1],number:m[2]}));
eq(bibcite,bblKeys.map((key,i)=>({key,number:String(i+1)})),'settled final numeric bibliography mapping');
ok(blg.includes('The top-level auxiliary file: main.aux\nThe style file: plain.bst\nDatabase file #1: references.bib\n'),'complete BibTeX top-level roles');
eq([...blg.matchAll(/You've used ([0-9]+) entries,/g)].map(m=>Number(m[1])),[bibliographyKeys.length],'actual BibTeX entry count');
ok(blg.includes('warning$ -- 0\n')&&!/Warning--|Error|error|^!/m.test(blg),'zero actual BibTeX warning/error');
ok(bbl.includes("M{\\'e}sz{\\'a}ros"),'actual two accent commands retained');
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
    let end=i+1;if(lines[i].startsWith('LaTeX Warning:'))while(end<lines.length&&lines[end]!=='')end++;
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
ok(pdfText.includes('References')&&pdfText.includes('Manna')&&pdfText.includes('Holroyd')&&pdfText.includes('Loginov')&&pdfText.includes('Pham')&&pdfText.includes('Berdine'),'five entries represented in extracted text');
// The changed dependency needs new actual locator output, not only five keys.
const holroydNumber=bibcite.find(r=>r.key==='holroyd2008').number;
const holroydStart=bbl.indexOf('\\bibitem{holroyd2008}'),nextBib=bbl.indexOf('\\bibitem{',holroydStart+1);
ok(holroydStart>=0,'actual Holroyd BBL item');
const holroydBBL=bbl.slice(holroydStart,nextBib<0?bbl.length:nextBib);
const locatorNote='Primary preprint; Theorem 3.8, Lemma 4.9 and Corollary 4.10';
ok(holroydBBL.replace(/\s+/g,' ').includes(locatorNote),'corrected actual BBL locator note');
const referencesAt=pdfText.lastIndexOf('References');ok(referencesAt>=0,'actual PDF references section');
const bodyText=pdfText.slice(0,referencesAt).replace(/\s+/g,' '),referencesText=pdfText.slice(referencesAt).replace(/\s+/g,' ');
const correctedBody='Holroyd et al. ['+holroydNumber+', Lemma 4.9]';
const obsoleteBody='Holroyd et al. ['+holroydNumber+', Theorem 3.8]';
ok(bodyText.includes(correctedBody)&&!bodyText.includes(obsoleteBody),'actual rendered-text body locator Lemma 4.9');
ok(referencesText.includes(locatorNote),'actual rendered-text bibliography keeps all three locators');
const citationLocator={source_delta:sourceDelta,body_expected:correctedBody,body_match_offset:bodyText.indexOf(correctedBody),bibliography_note:locatorNote,bibliography_match_offset:referencesText.indexOf(locatorNote),holroyd_bbl_raw:holroydBBL,comparison_scope:'Whitespace-folded locator checks only; complete raw PDF text and BBL retained; not RAW equality or an actual visual review'};
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
const report={status:findings.length?'HOLD_ARTIFACT_FINDINGS':'DATA_CHECK_COMPLETE_PENDING_INDEPENDENT_SEMANTIC_AND_ROOT_RECEPTION',scope:'One P212 Review B source build, ordinary trusted tools/configuration; no host re-read, syscall closure, science, final manuscript verdict or visual/PDF adoption',checks,summary,findings,provenance:{launch,continuation,grant,external_binding:binding,runtime_preflight:prep,adopted_policy:policy,b_source_reception:aReception,accepted_B_pair:pairReceipt,citation_repair:citationRepair,citation_closure:citationClosure},adaptation:{base_checker_sha256:sha(readExternal(baseChecker)),recipe_delta:recipeDelta,initial_source_pins:initialSources,citation_locator:citationLocator},source_pins:sources,runtime_pins_as_data_only:runtime,external_pins:externalPins,cold_cwd_record:rt('COLD_CWD.actual.txt'),commands,snapshots:snapshotData,raw_pairs:rawPairs,ordered_fls:ordered,diagnostics,bibliography:{keys:bibliographyKeys,bbl_order:bblKeys,final_bibcite:bibcite,source_citations:sourceCitations,labels:finalLabels,references,bibtex_role_limit:'Complete AUX/BLG/BBL top-level roles, not a BibTeX syscall trace'},fonts,pages:pageImages,text_extraction_controls:textControls,text_extraction_limit:'Raw math extraction can lose layout or encode delimiter glyphs as controls; full raw output retained, actual all-page viewing is separate',inventory,complete_text_captures:textCaptures};
process.stdout.write(JSON.stringify(report,null,2)+'\n');
if(findings.length)process.exitCode=1;
