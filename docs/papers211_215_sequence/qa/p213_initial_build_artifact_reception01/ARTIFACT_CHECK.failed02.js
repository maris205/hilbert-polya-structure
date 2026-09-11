'use strict';
// Author-side, read-only artifact reception; no build, child, observer or write API.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const W='/root/autodl-tmp/symbolic_dynamics',Q=W+'/docs/papers211_215_sequence/qa/';
const OWN=Q+'p213_initial_build_artifact_reception01/',SRC=W+'/papers/213-receiver-limited-cyclic-transfer';
const MAP='/usr/share/texlive/texmf-dist/fonts/map/fontname/texfonts.map';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p),txt=p=>read(p).toString('utf8'),lines=s=>s===''?[]:s.replace(/\n$/,'').split('\n');
const parse=s=>lines(s).map(l=>{const m=/^([a-f0-9]{64})  ([^\r\n]+)$/.exec(l);assert.ok(m,l);return{sha256:m[1],path:m[2]};});
const bytePairs=[];function same(a,b){assert.ok(read(a).equals(read(b)),a+' != '+b);bytePairs.push({left:a,right:b,bytes:read(a).length,sha256:sha(read(a))});}
const runtime01=txt(Q+'p213_initial_build_runtime_resolution01/RUNTIME_INPUTS.sha256');
assert.equal(sha(Buffer.from(runtime01)),'9f864f7a3cb727306be073851b1f0baaae07963d142c083a7cadb67e05904078');
const runtime02=txt(Q+'p213_initial_build_binding02/RUNTIME_INPUTS.sha256');
assert.equal(sha(Buffer.from(runtime02)),'35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530');
const oldRuntime=parse(runtime01),newRuntime=parse(runtime02);
assert.equal(oldRuntime.length,222);assert.equal(newRuntime.length,223);
assert.deepEqual(newRuntime.filter(x=>x.path!==MAP),oldRuntime);
assert.deepEqual(newRuntime.filter(x=>x.path===MAP),[{sha256:'d9693993efdc7d0b9ab3df777589995d43e24eeae95f12b6a230a19caadeaa42',path:MAP}]);
const runtimeCurrent=newRuntime.map(x=>{assert.equal(sha(read(x.path)),x.sha256,x.path);return x;});
const sources=parse(txt(Q+'p213_initial_build_preparation01/PROPOSED_SOURCE_ONLY.sha256'));
assert.deepEqual(sources.map(x=>x.path),['main.tex','math_commands.tex','references.bib','sections/00_abstract.tex','sections/01_introduction.tex','sections/02_temporal.tex','sections/03_inverse.tex','sections/04_fibres.tex','sections/05_verification.tex']);
const sourceSet=new Set(sources.map(x=>x.path));
const products=['main.aux','main.bbl','main.blg','main.log','main.fls','main.out','main.toc','main.pdf'];
const steps=['pass1','bibtex','pass2','pass3','pdfinfo','pdffonts','pdftotext','final_diagnostics',...Array.from({length:7},(_,i)=>'page-'+String(i+1).padStart(4,'0'))];
const snapshots=['pass1.before','pass1.after','bibtex.before','bibtex.after','pass2.before','pass2.after','pass3.before','pass3.after'];
const runs=[];const allFiles=[];
for(const num of ['01','02']){
 const R=Q+'p213_initial_build_run'+num,C=R+'/source_only',bind=Q+'p213_initial_build_binding'+num;
 const capture=JSON.parse(txt(OWN+'NATIVE_RUN'+num+'_TEXT_READS.json')).filter(x=>(x.path||R+'/'+x.relative_path).startsWith(R+'/'));
 assert.equal(capture.length,150);
 for(const x of capture){const p=x.path||R+'/'+x.relative_path;assert.equal(x.r.exit_code,0);assert.ok(!x.r.session_id);assert.ok(!x.r.output.includes('Warning: truncated'));assert.ok(read(p).equals(Buffer.from(x.r.output,'utf8')),p+' whole capture');}
 const capturedNames=capture.map(x=>(x.path||R+'/'+x.relative_path).slice(R.length+1));
 const expected=new Set([...capturedNames,...snapshots.filter(x=>x!=='pass1.before').map(x=>'pass_artifacts/'+x+'/main.pdf'),'source_only/main.pdf',...Array.from({length:7},(_,i)=>'pages/page-'+String(i+1).padStart(4,'0')+'.png')]);
 const inventory=[];function walk(d,rel=''){for(const e of fs.readdirSync(d,{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))){const p=d+'/'+e.name,r=rel+e.name;assert.ok(!e.isSymbolicLink(),p);if(e.isDirectory())walk(p,r+'/');else{assert.ok(e.isFile(),p);assert.ok(expected.has(r),'unexpected '+p);inventory.push({path:p,relative:r,bytes:fs.statSync(p).size,sha256:sha(read(p))});}}}
 walk(R);assert.equal(inventory.length,165);assert.deepEqual([...expected].sort(),inventory.map(x=>x.relative).sort());allFiles.push(...inventory);
 const runtime=parse(txt(R+'/RUNTIME_EXPECTED.sha256'));assert.deepEqual(runtime,num==='01'?oldRuntime:newRuntime);
 same(R+'/RUNTIME_EXPECTED.sha256',bind+'/RUNTIME_INPUTS.sha256');
 same(R+'/SOURCE_EXPECTED.sha256',Q+'p213_initial_build_preparation01/PROPOSED_SOURCE_ONLY.sha256');
 for(const x of sources){assert.equal(sha(read(SRC+'/'+x.path)),x.sha256);assert.equal(sha(read(C+'/'+x.path)),x.sha256);same(SRC+'/'+x.path,C+'/'+x.path);}
 const guardNames=['live_source.before','live_source.after','cold_source.initial','cold_source.final',...['pass1','bibtex','pass2','pass3'].map(x=>'raw/'+x+'.sources')];
 const sourceOK=sources.map(x=>x.path+': OK\n').join('');
 for(const n of guardNames){assert.equal(txt(R+'/'+n+'.stdout'),sourceOK);assert.equal(txt(R+'/'+n+'.stderr'),'');}
 for(const n of ['before','after']){assert.equal(txt(R+'/runtime.'+n+'.stdout'),runtime.map(x=>x.path+': OK\n').join(''));assert.equal(txt(R+'/runtime.'+n+'.stderr'),'');}
 assert.equal(txt(R+'/controller.exit'),'0\n');for(const x of ['stdout','stderr'])assert.equal(txt(R+'/controller.'+x+'.raw'),'');
 assert.equal(txt(R+'/STATUS.txt'),'CAPTURED_PENDING_FULL_LOG_FLS_CONFIG_PDF_AND_ACTUAL_ALL_PAGE_RECEPTION\n');
 const commands=[];
 for(const step of steps){const rq=txt(R+'/raw/'+step+'.request.txt');assert.ok(rq.startsWith('cwd='+C+'\nsupervisor_argv=/usr/bin/timeout --signal=TERM --kill-after=10s '));
  assert.equal(txt(R+'/raw/'+step+'.supervisor_exit'),'0\n');assert.equal(txt(R+'/raw/'+step+'.stderr.raw'),'');
  if(/^pass[123]$/.test(step))assert.equal(rq,'cwd='+C+'\nsupervisor_argv=/usr/bin/timeout --signal=TERM --kill-after=10s 600s /usr/bin/pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex \n');
  if(step==='bibtex')assert.equal(rq,'cwd='+C+'\nsupervisor_argv=/usr/bin/timeout --signal=TERM --kill-after=10s 600s /usr/bin/bibtex main \n');
  commands.push({step,request:rq,supervisor_exit:0,stderr_bytes:0,stdout_bytes:read(R+'/raw/'+step+'.stdout.raw').length});
 }
 const present={};
 for(const snap of snapshots){const d=R+'/pass_artifacts/'+snap,p=fs.existsSync(d+'/PRESENT.sha256')?parse(txt(d+'/PRESENT.sha256')):[];
  const absent=lines(txt(d+'/ABSENT.txt'));present[snap]=p.map(x=>x.path);
  assert.deepEqual([...present[snap],...absent].sort(),products.slice().sort());
  assert.deepEqual(fs.readdirSync(d).sort(),[...present[snap],'ABSENT.txt',...(p.length?['PRESENT.sha256']:[])].sort());
  for(const x of p){assert.ok(products.includes(x.path));assert.equal(sha(read(d+'/'+x.path)),x.sha256);}
 }
 assert.deepEqual(present['pass1.before'],[]);assert.deepEqual(present['pass1.after'],['main.aux','main.log','main.fls','main.pdf']);
 assert.deepEqual(present['bibtex.after'],['main.aux','main.bbl','main.blg','main.log','main.fls','main.pdf']);
 for(const [a,b] of [['pass1.after','bibtex.before'],['bibtex.after','pass2.before'],['pass2.after','pass3.before']])for(const f of present[a])same(R+'/pass_artifacts/'+a+'/'+f,R+'/pass_artifacts/'+b+'/'+f);
 for(const f of present['bibtex.before'])same(R+'/pass_artifacts/bibtex.before/'+f,R+'/pass_artifacts/bibtex.after/'+f);
 for(const f of ['main.bbl','main.blg'])for(const pass of ['pass2','pass3'])same(R+'/pass_artifacts/'+pass+'.before/'+f,R+'/pass_artifacts/'+pass+'.after/'+f);
 for(const f of present['pass3.after'])same(R+'/pass_artifacts/pass3.after/'+f,C+'/'+f);
 same(R+'/pass_artifacts/pass2.after/main.aux',R+'/pass_artifacts/pass3.after/main.aux');
 const fls=[];
 for(const pass of ['pass1','pass2','pass3']){
  const observedOutputs=new Set(),before=new Set(present[pass+'.before']),rs=[];
  for(const [i,l] of lines(txt(R+'/pass_artifacts/'+pass+'.after/main.fls')).entries()){const m=/^(PWD|INPUT|OUTPUT) (.+)$/.exec(l);assert.ok(m,l);const kind=m[1],p=m[2];let category,absolute=path.resolve(C,p),local=absolute.startsWith(C+'/')?absolute.slice(C.length+1):null;
   if(kind==='PWD'){assert.equal(i,0);assert.equal(p,C);category='cwd';}
   else if(kind==='OUTPUT'){assert.ok(['main.log','main.aux','main.pdf'].includes(local));observedOutputs.add(local);category='cold-generated-output';}
   else if(runtime.some(x=>x.path===absolute))category='selected-runtime';
   else if(sourceSet.has(local))category='declared-source';
   else if(observedOutputs.has(local))category='earlier-same-pass-output';
   else if(before.has(local))category='generated-before';
   else{assert.equal(num,'01');assert.equal(absolute,MAP);category='historical-missing-prepin';}
   rs.push({line:i+1,raw:l,kind,path:p,absolute,local,category});
  }
  const counts={};for(const x of rs)counts[x.category]=(counts[x.category]||0)+1;
  assert.equal(rs.length,pass==='pass1'?246:253);assert.equal(counts['selected-runtime'],num==='01'?190:191);assert.equal(counts['declared-source'],50);assert.equal(counts['earlier-same-pass-output'],1);assert.equal(counts['cold-generated-output'],3);assert.equal(counts['generated-before']||0,pass==='pass1'?0:7);
  assert.equal(counts['historical-missing-prepin']||0,num==='01'?1:0);
  fls.push({pass,counts,records:rs});
 }
 const diagnostics=[];
 for(const pass of ['pass1','pass2','pass3']){
  for(const role of ['log','stdout']){const p=role==='log'?R+'/pass_artifacts/'+pass+'.after/main.log':R+'/raw/'+pass+'.stdout.raw',ls=lines(txt(p)),records=[];
   for(let i=0;i<ls.length;i++){if(/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!|No file/.test(ls[i])){let end=i+1;if(ls[i].startsWith('LaTeX Warning:'))while(end<ls.length&&ls[end]!=='')end++;
    const raw=ls.slice(i,end).join('\n');let disposition;
    if(raw===' file:line:error style messages enabled.')disposition='informational-enabled-error-format';
    else if(/^No file main\.(aux|bbl)\.$/.test(raw)&&pass==='pass1')disposition='expected-cold-generated-absence';
    else if(/^LaTeX Warning:/.test(raw)&&pass!=='pass3')disposition='resolved-by-final-pass';
    else throw Error('unresolved diagnostic '+p+':'+(i+1)+' '+raw);
    records.push({line:i+1,raw,disposition});i=end-1;
   }}
   diagnostics.push({pass,role,source:p,records,warning_count:records.filter(x=>x.raw.startsWith('LaTeX Warning:')).length});
  }
 }
 assert.deepEqual(diagnostics.filter(x=>x.role==='log').map(x=>x.warning_count),[42,5,0]);
 const blg=txt(R+'/pass_artifacts/bibtex.after/main.blg'),bbl=txt(R+'/pass_artifacts/bibtex.after/main.bbl'),aux=txt(R+'/pass_artifacts/bibtex.before/main.aux');
 assert.ok(blg.includes('The top-level auxiliary file: main.aux\nThe style file: plain.bst\nDatabase file #1: references.bib\n'));
 assert.ok(blg.includes("You've used 3 entries,"));assert.ok(blg.includes('warning$ -- 0\n'));assert.ok(!/Warning--|Error|error|^!/m.test(blg));
 assert.deepEqual([...bbl.matchAll(/\\bibitem\{([^}]+)\}/g)].map(x=>x[1]),['boccara2002','fukuda2023','nishinari1998']);
 assert.ok(aux.includes('\\bibstyle{plain}\n'));assert.ok(aux.includes('\\bibdata{references}\n'));assert.ok(!aux.includes('\\@input'));
 assert.equal(txt(R+'/raw/final_diagnostics.stdout.raw'),'main.log:3: file:line:error style messages enabled.\n');
 const fonts=lines(txt(R+'/raw/pdffonts.stdout.raw')).slice(2);assert.equal(fonts.length,17);for(const l of fonts)assert.match(l,/ Type 1\s+Builtin\s+yes\s+yes\s+yes\s+\d+\s+0$/);
 assert.equal(txt(R+'/PAGE_COUNT.txt'),'7\n');assert.match(txt(R+'/raw/pdfinfo.stdout.raw'),/^Pages:\s+7$/m);
 const pdftext=txt(R+'/raw/pdftotext.stdout.raw');assert.ok(!/\?\?|\[\?\]|\[VERIFY\]/.test(pdftext));assert.equal(pdftext.split('\f').length-1,7);
 for(const [m,base] of [['FINAL_PRODUCTS.sha256',C],['PAGES.sha256',R]])for(const x of parse(txt(R+'/'+m))){const p=path.resolve(base,x.path);assert.ok(p.startsWith(R+'/'));assert.equal(sha(read(p)),x.sha256);}
 runs.push({run:num,artifact_files:inventory.length,artifact_bytes:inventory.reduce((s,x)=>s+x.bytes,0),text_captures:150,runtime_count:runtime.length,source_count:9,commands,present,fls,diagnostics,bibtex:{entries:3,warnings:0,aux:'generated-pass1',database:'declared-source references.bib',style:'selected-runtime plain.bst',recorder_limit:'BibTeX BLG identifies top-level roles, not a complete syscall read trace'},fonts:17,pages:7,pdf_bytes:read(C+'/main.pdf').length});
}
const oldscript=txt(Q+'p213_initial_build_preparation01/BUILD_REQUEST.sh'),newscript=txt(Q+'p213_initial_build_binding02/BUILD_REQUEST.sh');
assert.equal(newscript,oldscript.replace("p213_initial_build_binding01'","p213_initial_build_binding02'").replace("p213_initial_build_run01'","p213_initial_build_run02'"));
const grant=JSON.parse(txt(Q+'p213_initial_build_binding02/GRANT.json')),consumption=JSON.parse(txt(Q+'p213_initial_build_binding02/CONSUMPTION.json')),launch=JSON.parse(txt(Q+'p213_initial_build_binding02/LAUNCH_NATIVE.json')),completion=JSON.parse(txt(Q+'p213_initial_build_binding02/COMPLETION_NATIVE.json'));
assert.equal(sha(Buffer.from(newscript)),grant.script_sha256);assert.equal(sha(Buffer.from(runtime02)),grant.runtime_manifest_sha256);
assert.deepEqual(grant.request,consumption.request);assert.deepEqual(grant.request,launch.request);assert.equal(grant.allowed_submissions,1);assert.equal(consumption.remaining_submissions,0);assert.equal(consumption.status,'CONSUMED_BEFORE_SUBMISSION');
assert.equal(launch.result.session_id,completion.request.session_id);assert.equal(completion.result.exit_code,0);assert.equal(completion.result.output,'P213_INITIAL_BUILD_SUPERVISOR_EXIT=0\n');
for(const rel of ['source_only/main.pdf',...Array.from({length:7},(_,i)=>'pages/page-'+String(i+1).padStart(4,'0')+'.png')])same(Q+'p213_initial_build_run01/'+rel,Q+'p213_initial_build_run02/'+rel);
const report={status:'PASS_AUTHOR_ARTIFACT_RECEPTION_CONFIRMATION02_WITH_HISTORICAL_RUN01_GAP',scope:'ordinary trusted bootstrap; finite selected runtime and full TeX FLS; not hostile closure, science or independent manuscript review',runtime_current:runtimeCurrent,source_pins:sources,runs,byte_pairs:bytePairs,artifacts:allFiles,binding02:{grant,consumption,launch,completion}};
console.log(JSON.stringify({...report,runtime_current:{count:runtimeCurrent.length,all_current_hashes_match:true},runs:runs.map(r=>({...r,fls:r.fls.map(f=>({pass:f.pass,counts:f.counts,records:f.records.length,unique_inputs:new Set(f.records.filter(x=>x.kind==='INPUT').map(x=>x.absolute)).size}))})),byte_pairs:{count:bytePairs.length,all_raw_bytes_equal:true,details_sha256:sha(Buffer.from(JSON.stringify(bytePairs)))},artifacts:{count:allFiles.length,bytes:allFiles.reduce((s,x)=>s+x.bytes,0),inventory_sha256:sha(Buffer.from(JSON.stringify(allFiles)))}},null,2));
