'use strict';
// Independent P212 initial-build DATA receiver. Read-only; no child process,
// proposed-source import, host-manifest follow, repair, build or write API.
const fs=require('node:fs'), path=require('node:path'), crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics', Q=W+'/docs/papers211_215_sequence/qa/';
const P=Q+'p212_plain_build_source_proposal03', B=Q+'p212_plain_build_binding01';
const S=W+'/papers/212-closed-pointer-orbits', R=S+'/qa_initial/plain_build01', C=R+'/source_only';
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
const fixedExternal=[P+'/BUILD_REQUEST.proposed.sh.txt',P+'/NATIVE_REQUEST.proposed.json',P+'/PROPOSED_SOURCE_ONLY.sha256',P+'/CONTRACT.md',Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md',Q+'p212_plain_build_source_root01/RECEPTION.md',...['GRANT.md','ACTUAL_NATIVE.json','CONTINUATION_NATIVE.json','PREPARATION_NATIVE.json','PARENT_AND_LIVE_NATIVE.json','BINDING_NATIVE.json','RUNTIME_INPUTS.sha256'].map(n=>B+'/'+n),...sourceNames.flatMap(n=>[P+'/proposed/'+n,S+'/'+n])];
const externalAllowed=new Set(fixedExternal);
function readExternal(p){ok(externalAllowed.has(p),'external path allowlist '+p);if(!bytes.has(p)){const st=fs.lstatSync(p);ok(st.isFile()&&!st.isSymbolicLink(),'external regular '+p);const b=fs.readFileSync(p);bytes.set(p,b);externalPins.push({path:p,bytes:b.length,sha256:sha(b)});}return bytes.get(p);}
function decode(b){const t=b.toString('utf8');ok(Buffer.from(t,'utf8').equals(b),'lossless UTF-8');return t;}
const xt=p=>decode(readExternal(p));
const ls=t=>{ok(!t.includes('\r'),'LF-only grammar');return t===''?[]:(ok(t.endsWith('\n'),'terminal LF'),t.slice(0,-1).split('\n'));};
const manifest=t=>{const rows=ls(t).map(l=>{const m=/^([0-9a-f]{64})  ([^\r\n]+)$/.exec(l);ok(!!m,'manifest syntax');return {sha256:m[1],path:m[2]};});ok(new Set(rows.map(r=>r.path)).size===rows.length,'unique manifest names');return rows;};
function sameBuffers(a,b,label){ok(a.equals(b),'RAW equality '+label);rawPairs.push({label,bytes:a.length,sha256:sha(a)});}
const proposal=JSON.parse(xt(P+'/NATIVE_REQUEST.proposed.json'));
const launch=JSON.parse(xt(B+'/ACTUAL_NATIVE.json')), continuation=JSON.parse(xt(B+'/CONTINUATION_NATIVE.json'));
eq(launch.arguments,proposal.proposed_native_request.arguments,'whole actual native request');
ok(launch.result.chunk_id==='799607'&&launch.result.session_id===9370&&launch.result.output===''&&!Object.hasOwn(launch.result,'exit_code'),'actual original launch');
eq(continuation.arguments,{session_id:launch.result.session_id,chars:'',yield_time_ms:10000,max_output_tokens:16000},'only real continuation');
ok(continuation.result.chunk_id==='d1e0bb'&&continuation.result.exit_code===0&&!Object.hasOwn(continuation.result,'session_id'),'actual completion');
ok(continuation.result.output==='P212_INITIAL_BUILD_SUPERVISOR_EXIT=0\n','complete native completion stream');
const grant=xt(B+'/GRANT.md'), policy=xt(Q+'p212_plain_build_source_root01/RECEPTION.md');
ok(grant.includes('ISSUED_AND_CONSUMED_BEFORE_SUBMISSION')&&grant.includes('Exactly one launch'),'explicit consumed grant');
ok(policy.includes('P212-POLICY-TIME1 is therefore CLOSED')&&policy.includes('supplement has precedence'),'adopted staged policy');
const sourceManifest=readExternal(P+'/PROPOSED_SOURCE_ONLY.sha256');
ok(sha(sourceManifest)==='fe4abe8535901fbb1e6dd8c63038e0ecef03c9ea5a5d05619559d452494a8288','adopted source manifest pin');
const sources=manifest(decode(sourceManifest));eq(sources.map(r=>r.path),sourceNames,'eight exact sources');
const runtimeManifest=readExternal(B+'/RUNTIME_INPUTS.sha256');
ok(sha(runtimeManifest)==='35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530','received P212 selected manifest pin');
const runtime=manifest(decode(runtimeManifest));ok(runtime.length===223&&runtime.every(r=>path.isAbsolute(r.path)),'received finite runtime names');
const runtimeByName=new Map(runtime.map(r=>[r.path,r]));
const binding=JSON.parse(xt(B+'/BINDING_NATIVE.json'));
ok(binding.result.exit_code===0&&binding.result.chunk_id==='07d878','external binding native result');
const boundNames=[P+'/BUILD_REQUEST.proposed.sh.txt',P+'/NATIVE_REQUEST.proposed.json',P+'/PROPOSED_SOURCE_ONLY.sha256',P+'/CONTRACT.md',Q+'p212_plain_build_source_audit01/STAGED_POLICY_SUPPLEMENT.md',Q+'p212_plain_build_source_root01/RECEPTION.md',B+'/RUNTIME_INPUTS.sha256'];
const boundOutput=boundNames.map(p=>sha(readExternal(p))+'  '+p.slice(W.length+1)+'\n').join('')+'EXACT_NEW_OUTPUT_ABSENT\n';
ok(binding.result.output===boundOutput,'whole seven external content pins and genuine old output absence');
ok(sha(readExternal(P+'/BUILD_REQUEST.proposed.sh.txt'))==='8d40a51735984e517c10d564019f5c598657d8b31b0d80034753999c96a867a0','actual reviewed recipe');
ok(sha(readExternal(P+'/NATIVE_REQUEST.proposed.json'))==='023381134cb65b8e7a602365156988587a5159fa1ea0a3cdb3e3e4bb470c7f27','actual reviewed request');
const prep=JSON.parse(xt(B+'/PREPARATION_NATIVE.json')),parent=JSON.parse(xt(B+'/PARENT_AND_LIVE_NATIVE.json'));
const runtimeOK=runtime.map(r=>r.path+': OK\n').join('');
ok(prep.result.chunk_id==='a54983'&&prep.result.exit_code===0&&prep.result.output.startsWith(runtimeOK),'all received pregrant runtime OK rows');
const prepTail=prep.result.output.slice(runtimeOK.length);
ok(prepTail.startsWith("directory|papers/212-closed-pointer-orbits|755\nstat: cannot statx 'papers/212-closed-pointer-orbits/qa_initial': No such file or directory\nOUTPUT_NOT_PRESENT\n"),'retain parent ENOENT, not false success');
ok(!/FAILED|WARNING:/.test(prep.result.output),'no concealed hash failure');
ok(parent.result.chunk_id==='c1566f'&&parent.result.exit_code===0,'separate actual parent reception');
const parentOutput=S+'/qa_initial\ndirectory|papers/212-closed-pointer-orbits/qa_initial|755\n'+sourceNames.map(n=>'LIVE_PROPOSED_RAW_EQUAL '+n+'\n').join('');
ok(parent.result.output===parentOutput,'whole parent physical path and eight source comparisons');

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
for(const row of sources){const a=readExternal(P+'/proposed/'+row.path),b=readExternal(S+'/'+row.path),c=rb('source_only/'+row.path);ok(sha(a)===row.sha256,'source content pin');sameBuffers(a,b,'proposed == live '+row.path);sameBuffers(a,c,'proposed == cold '+row.path);want('source_only/'+row.path);}
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
const report={status:findings.length?'HOLD_ARTIFACT_FINDINGS':'DATA_CHECK_COMPLETE_PENDING_INDEPENDENT_SEMANTIC_AND_ROOT_RECEPTION',scope:'One P212 initial build, ordinary trusted tools/configuration; no host re-read, syscall closure, science, manuscript review or visual/PDF adoption',checks,summary,findings,provenance:{launch,continuation,grant,external_binding:binding,preparation:prep,parent,adopted_policy:policy},source_pins:sources,runtime_pins_as_data_only:runtime,external_pins:externalPins,cold_cwd_record:rt('COLD_CWD.actual.txt'),commands,snapshots:snapshotData,raw_pairs:rawPairs,ordered_fls:ordered,diagnostics,bibliography:{keys:bibliographyKeys,bbl_order:bblKeys,final_bibcite:bibcite,source_citations:sourceCitations,labels:finalLabels,references,bibtex_role_limit:'Complete AUX/BLG/BBL top-level roles, not a BibTeX syscall trace'},fonts,pages:pageImages,text_extraction_controls:textControls,text_extraction_limit:'Raw math extraction can lose layout or encode delimiter glyphs as controls; full raw output retained, actual all-page viewing is separate',inventory,complete_text_captures:textCaptures};
process.stdout.write(JSON.stringify(report,null,2)+'\n');
if(findings.length)process.exitCode=1;
