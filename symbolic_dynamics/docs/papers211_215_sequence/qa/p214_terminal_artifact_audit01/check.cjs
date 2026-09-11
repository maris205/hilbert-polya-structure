'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics',Q=W+'/docs/papers211_215_sequence/qa';
const runs=[Q+'/p214_terminal_run01',Q+'/p214_terminal_run02'];
let checks=0; function need(v,m){checks++;if(!v)throw Error(m)}
function read(p){return fs.readFileSync(p)} function txt(p){return read(p).toString('utf8')}
function sha(p){return crypto.createHash('sha256').update(read(p)).digest('hex')}
function walk(d,o=[]){for(const n of fs.readdirSync(d).sort()){const p=path.join(d,n),s=fs.lstatSync(p);need(!s.isSymbolicLink(),'symlink '+p);if(s.isDirectory())walk(p,o);else{need(s.isFile(),'type '+p);o.push(p)}}return o}
function rows(p){const s=txt(p);need(!s.includes('\n\n'),'blank manifest '+p);return s.trimEnd().split('\n')}
function checkManifest(base,p,count){const rr=rows(p);need(rr.length===count,'rows '+p);for(const row of rr){need(/^[0-9a-f]{64}  \S/.test(row),'row '+row);const f=path.resolve(base,row.slice(66));need(fs.existsSync(f),'missing '+f);need(sha(f)===row.slice(0,64),'hash '+f)}return rr}
const summaries=[];
for(const [i,R] of runs.entries()){
 const files=walk(R);need(files.length===171,'files '+R+' '+files.length);
 const exits=[R+'/controller.exit',...files.filter(p=>p.endsWith('.supervisor_exit'))];need(exits.length===16,'exit count');for(const p of exits)need(txt(p)==='0\n','exit '+p);
 const errs=files.filter(p=>p.includes('stderr'));need(errs.length===28,'stderr count');for(const p of errs)need(read(p).length===0,'stderr '+p);
 for(const role of ['runtime','evidence','source'])need(txt(R+'/'+role+'.before.stdout')===txt(R+'/'+role+'.after.stdout'),role+' pre/post');need(txt(R+'/cold_source.initial.stdout')===txt(R+'/cold_source.final.stdout'),'cold pre/post');
 checkManifest(R+'/source_only',R+'/SOURCE_EXPECTED.sha256',9);checkManifest(W,R+'/RUNTIME_EXPECTED.sha256',223);checkManifest(W,R+'/EVIDENCE_INPUTS.sha256',5);checkManifest(W,R+'/REQUEST_AND_BINDING.sha256',4);checkManifest(R+'/source_only',R+'/FINAL_PRODUCTS.sha256',6);checkManifest(R,R+'/PAGES.sha256',7);
 const snaps=['pass1.before','pass1.after','bibtex.before','bibtex.after','pass2.before','pass2.after','pass3.before','pass3.after'];for(const s of snaps){const d=R+'/pass_artifacts/'+s, present=fs.existsSync(d+'/PRESENT.sha256')?rows(d+'/PRESENT.sha256'):[], absent=fs.existsSync(d+'/ABSENT.txt')?txt(d+'/ABSENT.txt').trimEnd().split('\n'):[];need(present.length+absent.length===8,'snapshot '+s);for(const row of present){need(sha(d+'/'+row.slice(66))===row.slice(0,64),'snapshot hash')}}
 const fls=txt(R+'/source_only/main.fls').split('\n').filter(x=>x.startsWith('INPUT ')).map(x=>x.slice(6));const absolute=[...new Set(fls.filter(path.isAbsolute))];need(absolute.length===58,'absolute FLS '+absolute.length);const runtime=new Set(rows(R+'/RUNTIME_EXPECTED.sha256').map(x=>x.slice(66)));for(const p of absolute)need(runtime.has(p),'unbound FLS '+p);
 need(txt(R+'/raw/final_diagnostics.stdout.raw')==='main.log:3: file:line:error style messages enabled.\n','diagnostic');need(txt(R+'/PAGE_COUNT.txt')==='7\n','pages');const fonts=txt(R+'/raw/pdffonts.stdout.raw').trimEnd().split('\n').slice(2);need(fonts.length===15,'fonts');for(const row of fonts)need(/ yes yes yes\s+\d+\s+0$/.test(row),'font '+row);
 const pdf=R+'/source_only/main.pdf';need(read(pdf).length===191549,'pdf bytes');need(sha(pdf)==='a1f95a79c607436ea062f136be50c208b5505ef79568d2df5e73f4ed83a5eed8','pdf hash');need(read(pdf).equals(read(W+'/papers/214-nilpotent-bilinear-clock/frozen_round2/main.pdf')),'frozen pdf');const extracted=txt(R+'/raw/pdftotext.stdout.raw');for(const phrase of ['cancellation-safe clock','polynomial map','largest fibre size','Alexander Bors','Fibonacci complex dynamical systems'])need(extracted.includes(phrase),'text '+phrase);
 summaries.push({run:i+1,files:171,bytes:files.reduce((n,p)=>n+read(p).length,0),exit_roles:16,empty_stderr:28,absolute_fls_inputs:58,fonts:15,pages:7,pdf_bytes:191549,pdf_sha256:sha(pdf)});
}
for(const rel of ['source_only/main.pdf','source_only/main.log','source_only/main.aux','source_only/main.bbl','source_only/main.blg',...Array.from({length:7},(_,i)=>`pages/page-${String(i+1).padStart(4,'0')}.png`)])need(read(runs[0]+'/'+rel).equals(read(runs[1]+'/'+rel)),'pair '+rel);
const fls0=txt(runs[0]+'/source_only/main.fls').replaceAll('p214_terminal_run01','p214_terminal_runXX'),fls1=txt(runs[1]+'/source_only/main.fls').replaceAll('p214_terminal_run02','p214_terminal_runXX');need(fls0===fls1,'normalized FLS pair');
const report={status:'P214_TWO_TERMINAL_ARTIFACTS_PASS',checks,runs:summaries,pair_equal_roles:12,normalized_fls_equal:true};fs.writeFileSync(__dirname+'/RESULT.json',JSON.stringify(report,null,2)+'\n',{flag:'wx',mode:0o600});process.stdout.write(JSON.stringify(report)+'\n');
