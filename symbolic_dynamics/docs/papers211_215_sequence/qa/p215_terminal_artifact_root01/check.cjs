'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics',Q=W+'/docs/papers211_215_sequence/qa';
const runs=[Q+'/p215_terminal_run01',Q+'/p215_terminal_run02'];
let checks=0; const need=(v,m)=>{checks++;if(!v)throw Error(m)};
const read=p=>fs.readFileSync(p), text=p=>read(p).toString('utf8');
const sha=p=>crypto.createHash('sha256').update(read(p)).digest('hex');
function walk(d,o=[]){for(const n of fs.readdirSync(d).sort()){const p=path.join(d,n),s=fs.lstatSync(p);need(!s.isSymbolicLink(),'symlink '+p);if(s.isDirectory())walk(p,o);else{need(s.isFile(),'type '+p);o.push(p)}}return o}
function rows(p){const s=text(p);need(s.endsWith('\n')&&!s.includes('\n\n'),'manifest framing '+p);return s.trimEnd().split('\n')}
function manifest(base,p,count){const rr=rows(p);need(rr.length===count,'manifest count '+p);for(const row of rr){need(/^[0-9a-f]{64}  \S/.test(row),'row '+row);const f=path.resolve(base,row.slice(66));need(fs.existsSync(f)&&sha(f)===row.slice(0,64),'manifest payload '+f)}return rr}
const summaries=[];
for(const [i,R] of runs.entries()){
 const files=walk(R);need(files.length===165,'file count '+R);
 const exits=[R+'/controller.exit',...files.filter(p=>p.endsWith('.supervisor_exit'))];need(exits.length===15,'exit roles');for(const p of exits)need(text(p)==='0\n','exit '+p);
 const errs=files.filter(p=>p.includes('stderr'));need(errs.length===27,'stderr count');for(const p of errs)need(read(p).length===0,'stderr '+p);
 for(const role of ['runtime','evidence'])need(read(R+'/'+role+'.before.stdout').equals(read(R+'/'+role+'.after.stdout')),role+' prepost');
 need(read(R+'/live_source.before.stdout').equals(read(R+'/live_source.after.stdout')),'live source prepost');need(read(R+'/cold_source.initial.stdout').equals(read(R+'/cold_source.final.stdout')),'cold source prepost');
 manifest(R+'/source_only',R+'/SOURCE_EXPECTED.sha256',8);const runtime=manifest(W,R+'/RUNTIME_EXPECTED.sha256',227);manifest(W,R+'/EVIDENCE_INPUTS.sha256',5);manifest(W,R+'/REQUEST_AND_BINDING.sha256',4);manifest(R+'/source_only',R+'/FINAL_PRODUCTS.sha256',6);manifest(R,R+'/PAGES.sha256',6);
 for(const s of ['pass1.before','pass1.after','bibtex.before','bibtex.after','pass2.before','pass2.after','pass3.before','pass3.after']){const d=R+'/pass_artifacts/'+s,p=fs.existsSync(d+'/PRESENT.sha256')?rows(d+'/PRESENT.sha256'):[],a=fs.existsSync(d+'/ABSENT.txt')?text(d+'/ABSENT.txt').trimEnd().split('\n'):[];need(p.length+a.length===8,'snapshot '+s);for(const row of p)need(sha(d+'/'+row.slice(66))===row.slice(0,64),'snapshot hash')}
 const fls=text(R+'/source_only/main.fls').split('\n').filter(x=>x.startsWith('INPUT ')).map(x=>x.slice(6)),absolute=[...new Set(fls.filter(path.isAbsolute))],runtimeSet=new Set(runtime.map(x=>x.slice(66)));need(absolute.length===67,'absolute FLS');for(const p of absolute)need(runtimeSet.has(p),'unbound FLS '+p);
 need(text(R+'/raw/final_diagnostics.stdout.raw')==='main.log:3: file:line:error style messages enabled.\n','diagnostic');need(text(R+'/PAGE_COUNT.txt')==='6\n','pages');const fonts=text(R+'/raw/pdffonts.stdout.raw').trimEnd().split('\n').slice(2);need(fonts.length===16,'fonts');for(const row of fonts)need(/ yes yes yes\s+\d+\s+0$/.test(row),'font '+row);
 const pdf=R+'/source_only/main.pdf';need(read(pdf).length===200921,'pdf bytes');const extracted=text(R+'/raw/pdftotext.stdout.raw');for(const phrase of ['An exact sign-run clock','Every inverse fibre','unique largest fibre','Goldberg','Pemantle'])need(extracted.includes(phrase),'text '+phrase);
 for(const src of rows(R+'/SOURCE_EXPECTED.sha256'))need(sha(R+'/source_only/'+src.slice(66))===src.slice(0,64),'cold source '+src.slice(66));
 summaries.push({run:i+1,files:165,exit_roles:15,empty_stderr:27,runtime_rows:227,absolute_fls_inputs:67,fonts:16,pages:6,pdf_bytes:200921,pdf_sha256:sha(pdf)});
}
for(const rel of [...Array.from({length:6},(_,i)=>`pages/page-${String(i+1).padStart(4,'0')}.png`),'source_only/main.aux','source_only/main.bbl','source_only/main.blg','raw/pdftotext.stdout.raw'])need(read(runs[0]+'/'+rel).equals(read(runs[1]+'/'+rel)),'stable pair '+rel);
need(sha(runs[0]+'/source_only/main.pdf')!==sha(runs[1]+'/source_only/main.pdf'),'PDF metadata expected distinct');
const result={status:'P215_TWO_TERMINAL_ARTIFACTS_PASS',checks,runs:summaries,pair_equal_stable_roles:10,pdf_raw_equality_claimed:false,pdf_difference:'build-time metadata; page renders and extracted text are raw equal'};
fs.writeFileSync(__dirname+'/ROOT_RESULT.json',JSON.stringify(result,null,2)+'\n',{flag:'wx',mode:0o600});process.stdout.write(JSON.stringify(result)+'\n');
