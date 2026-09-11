'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics';
const Q=W+'/docs/papers211_215_sequence/qa/';
const A=Q+'p215_initial_artifact_audit01';
const P=Q+'p215_initial_build_current01';
const B=Q+'p215_initial_build_binding01';
const R=Q+'p215_initial_build_run01';
const C=R+'/source_only';
const S=W+'/papers/215-prefix-drawdown-clock';
const findings=[],checks=[],inventory=[],dirs=[],bytes=new Map(),rawPairs=[],flsReports=[];
const sourceNames=['main.tex','math_commands.tex','references.bib','sections/0_abstract.tex','sections/1_setup.tex','sections/2_clock.tex','sections/3_inverse.tex','sections/4_scope.tex'];
const texNames=sourceNames.filter(n=>n.endsWith('.tex'));
const products=['main.aux','main.bbl','main.blg','main.log','main.fls','main.out','main.toc','main.pdf'];
const passes=['pass1','bibtex','pass2','pass3'];
const snapshots=passes.flatMap(p=>[p+'.before',p+'.after']);
const bibKeys=['goldberg2017drawdown','pemantle2009barrier'];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function ok(v,label){if(!v)throw Error(label);checks.push(label);}
function eq(a,b,label){ok(JSON.stringify(a)===JSON.stringify(b),label);}
function rb(rel){const p=R+'/'+rel;if(!bytes.has(p)){const st=fs.lstatSync(p);ok(st.isFile()&&!st.isSymbolicLink(),'regular artifact '+rel);bytes.set(p,fs.readFileSync(p));}return bytes.get(p);}
function rt(rel){return rb(rel).toString('utf8');}
function ext(p){const st=fs.lstatSync(p);ok(st.isFile()&&!st.isSymbolicLink(),'regular input '+p.slice(W.length+1));return fs.readFileSync(p);}
function lines(t){return t.split(/\r?\n/).filter(Boolean);}
function manifest(t){const rows=lines(t).map(s=>{const m=/^([0-9a-f]{64})  (.+)$/.exec(s);ok(!!m,'manifest syntax');return{sha256:m[1],path:m[2]};});ok(new Set(rows.map(r=>r.path)).size===rows.length,'manifest unique paths');return rows;}
function same(a,b,label){const x=rb(a),y=rb(b);ok(x.equals(y),'RAW equality '+label);rawPairs.push({label,bytes:x.length,sha256:sha(x)});}
function walk(d,rel=''){dirs.push(rel);for(const e of fs.readdirSync(d,{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))){const p=d+'/'+e.name,r=rel+e.name;if(e.isDirectory())walk(p,r+'/');else{ok(e.isFile()&&!e.isSymbolicLink(),'regular inventory '+r);const z=fs.readFileSync(p);bytes.set(p,z);inventory.push({path:r,bytes:z.length,sha256:sha(z)});}}}

// Fixed accepted inputs and absence of the required outer native receipt.
const currentSource=ext(P+'/SOURCE_ONLY.sha256');
const runtime=ext(B+'/RUNTIME_INPUTS.sha256');
ok(sha(currentSource)==='4a9bae9505450b81d46ca2a94e00c723da2d87eb872e58f59dcb2e50c7d92e7b','current eight-source manifest pin');
ok(sha(runtime)==='35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530','223-resource manifest pin');
const sources=manifest(currentSource.toString('utf8')),runtimeRows=manifest(runtime.toString('utf8'));
eq(sources.map(x=>x.path),sourceNames,'exact eight source roles');
ok(runtimeRows.length===223,'exact 223 selected resources');
const binding=JSON.parse(ext(B+'/BINDING_NATIVE.json'));
ok(binding.runtime_rows===223&&binding.runtime_checks_all_passed&&binding.source_checks_all_passed,'binding records source/resource checks');
ok(binding.runtime_manifest_sha256===sha(runtime)&&binding.source_manifest_sha256===sha(currentSource),'binding manifest identities');
for(const n of ['SOURCE_RECEPTION.md','INPUT_BINDING.md','GRANT.md'])ext(B+'/'+n);
for(const n of ['BUILD_REQUEST.current.sh','NATIVE_REQUEST.current.json','SOURCE_RECEPTION.md'])ext(P+'/'+n);
const outerCandidates=['ACTUAL_NATIVE.json','CONTINUATION_NATIVE.json','BUILD_NATIVE.json','NATIVE_RESULT.json'];
const outerPresent=outerCandidates.filter(n=>fs.existsSync(B+'/'+n));
if(!outerPresent.length)findings.push({severity:'Major',reason:'No persisted outer native launch/session/completion receipt in the build binding; internal controller status cannot substitute for the granted submission result.'});

walk(R);
ok(inventory.length===160,'exact 160 artifact files');
eq(dirs.slice().sort(),['','pages/','pass_artifacts/','raw/','source_only/','source_only/sections/',...snapshots.map(s=>'pass_artifacts/'+s+'/')].sort(),'exact directory inventory');
const actualNames=new Set(inventory.map(x=>x.path));
const want=n=>ok(actualNames.has(n),'inventory role '+n);
const rootFiles=['COLD_CWD.actual.txt','FINAL_PRODUCTS.sha256','PAGES.sha256','PAGE_COUNT.txt','REQUEST_AND_BINDING.sha256','RUNTIME_EXPECTED.sha256','SOURCE_EXPECTED.sha256','STATUS.txt','controller.exit','controller.stderr.raw','controller.stdout.raw',...['cold_source.final','cold_source.initial','live_source.after','live_source.before','runtime.after','runtime.before'].flatMap(x=>[x+'.stdout',x+'.stderr'])];
for(const n of rootFiles)want(n);
ok(rt('controller.exit')==='0\n','controller exit zero');
ok(rt('controller.stdout.raw')===''&&rt('controller.stderr.raw')==='','controller raw streams empty');
ok(rt('STATUS.txt')==='CAPTURED_PENDING_FULL_LOG_FLS_CONFIG_PDF_AND_ACTUAL_ALL_PAGE_RECEPTION\n','build status marker');
ok(rb('SOURCE_EXPECTED.sha256').equals(currentSource),'captured source manifest RAW');
ok(rb('RUNTIME_EXPECTED.sha256').equals(runtime),'captured runtime manifest RAW');
const sourceOK=sources.map(x=>x.path+': OK\n').join('');
for(const n of ['cold_source.final','cold_source.initial','live_source.after','live_source.before']){ok(rt(n+'.stdout')===sourceOK,'complete source guard '+n);ok(rt(n+'.stderr')==='','empty source guard stderr '+n);}
const runtimeOK=runtimeRows.map(x=>x.path+': OK\n').join('');
for(const n of ['runtime.before','runtime.after']){ok(rt(n+'.stdout')===runtimeOK,'complete 223-row runtime guard '+n);ok(rt(n+'.stderr')==='','empty runtime guard stderr '+n);}
for(const row of sources){const live=ext(S+'/'+row.path),cold=rb('source_only/'+row.path);ok(sha(live)===row.sha256,'live source pin '+row.path);ok(sha(cold)===row.sha256,'cold source pin '+row.path);ok(live.equals(cold),'live/cold RAW '+row.path);want('source_only/'+row.path);}
const cwd=lines(rt('COLD_CWD.actual.txt'));
ok(cwd.includes('cold_member_count=4')&&cwd.includes('section_member_count=5'),'cold member counts');
ok(cwd.includes('relative_tree=texmf ABSENT')&&cwd.includes('relative_tree=.texlive2021 ABSENT'),'relative TeX trees absent');
ok(cwd.at(-1)==='EXACT_TWO_DIRECTORY_MEMBERSHIP_TYPES_AND_RELATIVE_TREE_ABSENCE_CHECKS_PASSED','cold cwd completion marker');

const pageCount=Number(rt('PAGE_COUNT.txt').trim());ok(pageCount===6,'actual six-page count');
const pageLabels=Array.from({length:pageCount},(_,i)=>'page-'+String(i+1).padStart(4,'0'));
const commandLabels=[...passes,'pdfinfo','pdffonts','pdftotext','final_diagnostics',...pageLabels];
for(const label of commandLabels){for(const suffix of ['request.txt','stdout.raw','stderr.raw','supervisor_exit'])want('raw/'+label+'.'+suffix);ok(rt('raw/'+label+'.supervisor_exit')==='0\n','step exit zero '+label);ok(rt('raw/'+label+'.stderr.raw')==='','step stderr empty '+label);if(passes.includes(label)){for(const suffix of ['stdout','stderr'])want('raw/'+label+'.sources.'+suffix);ok(rt('raw/'+label+'.sources.stdout')===sourceOK&&rt('raw/'+label+'.sources.stderr')==='','per-pass source guard '+label);}}

const snapshotMaps=new Map();
for(const snap of snapshots){const prefix='pass_artifacts/'+snap+'/';const present=actualNames.has(prefix+'PRESENT.sha256')?manifest(rt(prefix+'PRESENT.sha256')):[];const absent=actualNames.has(prefix+'ABSENT.txt')?lines(rt(prefix+'ABSENT.txt')):[];ok(present.length+absent.length===8,'snapshot eight product partition '+snap);eq([...present.map(x=>x.path),...absent].sort(),products.slice().sort(),'snapshot exact products '+snap);for(const row of present){want(prefix+row.path);ok(sha(rb(prefix+row.path))===row.sha256,'snapshot hash '+snap+'/'+row.path);}snapshotMaps.set(snap,new Map(present.map(x=>[x.path,x])));}
ok(snapshotMaps.get('pass1.before').size===0,'initial products absent');
eq([...snapshotMaps.get('pass1.after').keys()].sort(),['main.aux','main.fls','main.log','main.pdf'],'pass1 products');
eq([...snapshotMaps.get('bibtex.after').keys()].sort(),['main.aux','main.bbl','main.blg','main.fls','main.log','main.pdf'],'BibTeX products');
for(const n of ['main.aux','main.fls','main.log','main.pdf'])same('pass_artifacts/pass1.after/'+n,'pass_artifacts/bibtex.before/'+n,'pass1-to-bibtex bridge '+n);
for(const n of ['main.bbl','main.blg'])same('pass_artifacts/bibtex.after/'+n,'pass_artifacts/pass2.before/'+n,'BibTeX-to-pass2 bridge '+n);
for(const n of ['main.aux','main.bbl','main.blg','main.fls','main.log','main.pdf'])same('pass_artifacts/pass2.after/'+n,'pass_artifacts/pass3.before/'+n,'pass2-to-pass3 bridge '+n);
for(const n of ['main.aux','main.bbl','main.blg','main.fls','main.log','main.pdf']){want('source_only/'+n);same('pass_artifacts/pass3.after/'+n,'source_only/'+n,'final product '+n);}
same('pass_artifacts/pass2.after/main.aux','pass_artifacts/pass3.after/main.aux','settled AUX');

const runtimeByPath=new Map(runtimeRows.map(x=>[x.path,x]));
for(const pass of ['pass1','pass2','pass3']){const rel='pass_artifacts/'+pass+'.after/main.fls',before=snapshotMaps.get(pass+'.before'),after=snapshotMaps.get(pass+'.after');const events=[];for(const [i,line] of lines(rt(rel)).entries()){if(i===0){ok(line==='PWD '+C,'FLS PWD '+pass);continue;}const m=/^(INPUT|OUTPUT) (.+)$/.exec(line);ok(!!m,'FLS event syntax '+pass);const kind=m[1],spelling=m[2],absolute=path.posix.normalize(path.posix.isAbsolute(spelling)?spelling:C+'/'+spelling);let role;if(kind==='OUTPUT'){const local=path.posix.relative(C,absolute);ok(after.has(local),'FLS output captured '+pass+'/'+local);role='generated-output';}else if(runtimeByPath.has(absolute))role='selected-runtime';else{const local=path.posix.relative(C,absolute);if(texNames.includes(local))role='declared-source';else if(before.has(local))role='generated-before';else if(after.has(local))role='earlier-same-pass-output';else throw Error('unknown FLS input '+absolute);}events.push({line:i+1,kind,spelling,absolute,role});}eq([...new Set(events.filter(e=>e.role==='declared-source').map(e=>path.posix.relative(C,e.absolute)))].sort(),texNames.slice().sort(),'all seven TeX source roles '+pass);ok(events.filter(e=>e.role==='selected-runtime').every(e=>runtimeByPath.has(e.absolute)),'all runtime FLS inputs covered '+pass);flsReports.push({pass,events:events.length,counts:Object.fromEntries([...new Set(events.map(e=>e.role))].map(role=>[role,events.filter(e=>e.role===role).length]))});}

const tex=texNames.map(n=>rt('source_only/'+n)).join('\n');
const citations=[...tex.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));eq([...new Set(citations)].sort(),bibKeys,'two source citation keys');
const bib=rt('source_only/references.bib'),sourceBib=[...bib.matchAll(/^@[A-Za-z]+\{([^,]+),/gm)].map(m=>m[1]);eq(sourceBib.slice().sort(),bibKeys,'two bibliography entries');
const aux=rt('source_only/main.aux'),bbl=rt('source_only/main.bbl'),blg=rt('source_only/main.blg');
const auxCites=[...aux.matchAll(/\\citation\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));eq(auxCites,citations,'AUX citation sequence');
eq([...bbl.matchAll(/\\bibitem\{([^}]+)\}/g)].map(m=>m[1]),bibKeys,'BBL item order');
eq([...aux.matchAll(/\\bibcite\{([^}]+)\}/g)].map(m=>m[1]),bibKeys,'AUX bibcite order');
ok(blg.includes("You've used 2 entries,")&&blg.includes('warning$ -- 0'),'BibTeX two entries zero warnings');
for(const token of ['Lisa~R. Goldberg','Ola Mahmoud','Mathematics and Financial Economics','11(3):275--297, 2017','Robin Pemantle','Herbert~S. Wilf','The Electronic Journal of Combinatorics','16(1):R60, 2009'])ok(bbl.includes(token),'BBL field '+token);

const awkRE=/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!/;
const expectedDiag=['main.log','main.blg'].flatMap(n=>lines(rt('source_only/'+n)).flatMap((s,i)=>awkRE.test(s)?[n+':'+(i+1)+':'+s+'\n']:[])).join('');
ok(rt('raw/final_diagnostics.stdout.raw')===expectedDiag,'exact final diagnostic capture');
eq(lines(expectedDiag),['main.log:3: file:line:error style messages enabled.'],'only informational final diagnostic');
for(const pass of ['pass1','pass2','pass3']){const log=rt('pass_artifacts/'+pass+'.after/main.log');if(/Overfull|Underfull|Missing character/.test(log))findings.push({severity:'Major',reason:'box or glyph diagnostic',pass});}
ok(!/LaTeX Warning|undefined references|undefined citations|Rerun to get/.test(rt('source_only/main.log')),'no final LaTeX/citation/reference warning');

const fontLines=lines(rt('raw/pdffonts.stdout.raw'));ok(fontLines.length>=3,'font report has rows');const fonts=fontLines.slice(2).map(s=>{const m=/^(\S+)\s+(Type 1|Type 3|TrueType|CID Type 0C|CID TrueType|Type 1C)\s+(\S+)\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+(\d+)\s+(\d+)$/.exec(s);ok(!!m,'font row parsed');if(m[2]!=='Type 1'||m[4]!=='yes'||m[5]!=='yes'||m[6]!=='yes')findings.push({severity:'Major',reason:'font type/embedding',row:s});return s;});
ok(fonts.length===16,'sixteen embedded font rows');
const pdf=rb('source_only/main.pdf'),info=rt('raw/pdfinfo.stdout.raw'),pdfText=rt('raw/pdftotext.stdout.raw');
ok(pdf.subarray(0,5).toString()==='%PDF-'&&pdf.includes(Buffer.from('%%EOF')),'PDF boundaries');
ok(info.includes('Pages:           6')&&info.includes('File size:       '+pdf.length+' bytes'),'PDF info page/byte count');
for(const token of ['Exact Clocks and Inverse Fibres for Iterated Prefix','Anonymous','References','Lisa R. Goldberg','Ola Mahmoud','Robin Pemantle','Herbert S. Wilf'])ok(pdfText.includes(token),'PDF text token '+token);
ok(!pdfText.includes('[?]')&&!pdfText.includes('??')&&!pdfText.includes('[VERIFY]'),'no extracted placeholders');
const pageRows=manifest(rt('PAGES.sha256'));ok(pageRows.length===6,'six page pins');for(const [i,row] of pageRows.entries()){const rel='pages/'+pageLabels[i]+'.png';want(rel);const z=rb(rel);ok(row.path===R+'/'+rel&&sha(z)===row.sha256,'page pin '+(i+1));ok(z.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10]))&&z.readUInt32BE(16)===1241&&z.readUInt32BE(20)===1754,'page PNG dimensions '+(i+1));}
const finals=manifest(rt('FINAL_PRODUCTS.sha256'));eq(finals.map(x=>x.path),['main.pdf','main.log','main.fls','main.aux','main.bbl','main.blg'],'final manifest roles');for(const row of finals)ok(sha(rb('source_only/'+row.path))===row.sha256,'final manifest pin '+row.path);
for(const item of inventory){const now=fs.readFileSync(R+'/'+item.path);ok(sha(now)===item.sha256,'closing artifact stability '+item.path);}

const status=findings.length?'HOLD_EVIDENCE_GAP':'ACCEPT_INITIAL_ARTIFACT_DATA';
const report={status,scope:'Independent complete P215 initial-build artifact DATA audit; no PDF adoption, live edit, Round0, manuscript review, Git or external action.',checks:checks.length,summary:{artifact_files:inventory.length,artifact_bytes:inventory.reduce((a,x)=>a+x.bytes,0),directories:dirs.length-1,runtime_resources:runtimeRows.length,sources:sources.length,pages:pageCount,fonts:fonts.length,pdf_bytes:pdf.length,pdf_sha256:sha(pdf),fls:flsReports,raw_pairs:rawPairs.length,findings:findings.length},findings,outer_native_receipts_present:outerPresent,source_pins:sources,runtime_pins:runtimeRows,fls:flsReports,raw_pairs:rawPairs,inventory};
process.stdout.write(JSON.stringify(report,null,2)+'\n');
process.exitCode=findings.length?1:0;
