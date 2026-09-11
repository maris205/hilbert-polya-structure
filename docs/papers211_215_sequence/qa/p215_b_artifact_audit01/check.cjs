'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics';
const R=W+'/docs/papers211_215_sequence/reviews/p215_b/build01';
function need(x,s){if(!x)throw Error(s)}
function read(p){return fs.readFileSync(p)}
function text(p){return read(p).toString('utf8')}
function sha(p){return crypto.createHash('sha256').update(read(p)).digest('hex')}
function walk(dir,out=[]){for(const n of fs.readdirSync(dir).sort()){const p=path.join(dir,n),s=fs.lstatSync(p);need(!s.isSymbolicLink(),'symlink '+p);if(s.isDirectory())walk(p,out);else{need(s.isFile(),'type '+p);out.push(p)}}return out}
const files=walk(R);need(files.length===160,'files '+files.length);
const exits=[R+'/controller.exit',...files.filter(p=>p.endsWith('.supervisor_exit'))];
need(exits.length===15,'exits '+exits.length);for(const p of exits)need(text(p)==='0\n','exit '+p);
const stderr=files.filter(p=>p.includes('stderr'));need(stderr.length===25,'tree stderr '+stderr.length);
for(const p of stderr)need(read(p).length===0,'stderr bytes '+p);
need(text(R+'/runtime.before.stdout')===text(R+'/runtime.after.stdout'),'runtime stdout');
need(text(R+'/live_source.before.stdout')===text(R+'/live_source.after.stdout'),'live source stdout');
need(text(R+'/cold_source.initial.stdout')===text(R+'/cold_source.final.stdout'),'cold source stdout');
const sourceRows=text(R+'/SOURCE_EXPECTED.sha256').trim().split('\n');need(sourceRows.length===8,'source rows');
for(const row of sourceRows){const h=row.slice(0,64),p=row.slice(66);need(sha(R+'/source_only/'+p)===h,'source '+p)}
const runtimeRows=text(R+'/RUNTIME_EXPECTED.sha256').trim().split('\n');need(runtimeRows.length===227,'runtime rows');
const runtime=new Map(runtimeRows.map(row=>[row.slice(66),row.slice(0,64)]));
const fls=text(R+'/source_only/main.fls').split('\n').filter(x=>x.startsWith('INPUT ')).map(x=>x.slice(6));
const absolute=[...new Set(fls.filter(path.isAbsolute))];need(absolute.length===67,'absolute FLS '+absolute.length);
for(const p of absolute)need(runtime.has(p),'unbound FLS '+p);
const diagnostics=text(R+'/raw/final_diagnostics.stdout.raw');
need(diagnostics==='main.log:3: file:line:error style messages enabled.\n','diagnostics');
need(!/Overfull|Underfull|undefined references|Missing character|^!/m.test(diagnostics),'bad diagnostic');
const fonts=text(R+'/raw/pdffonts.stdout.raw').trim().split('\n').slice(2);
need(fonts.length===16,'fonts '+fonts.length);for(const line of fonts)need(/ yes yes yes\s+\d+\s+0$/.test(line),'font '+line);
need(text(R+'/PAGE_COUNT.txt')==='6\n','pages');
const pages=files.filter(p=>/\/pages\/page-\d{4}\.png$/.test(p));need(pages.length===6,'page files');
const pdf=R+'/source_only/main.pdf';need(read(pdf).length===200921,'pdf bytes');
need(sha(pdf)==='c4318f688ced970b2d5d452cf113b0ec697b43e3a634c3084dd856d36e8b2246','pdf sha');
const extracted=text(R+'/raw/pdftotext.stdout.raw');
for(const phrase of ['An exact sign-run clock','Every inverse fibre','unique largest fibre','Goldberg','Pemantle'])need(extracted.includes(phrase),'text '+phrase);
need(text(R+'/source_only/main.bbl').includes('Goldberg')&&text(R+'/source_only/main.bbl').includes('Pemantle'),'bbl');
const result={status:'P215_B_ARTIFACT_DATA_PASS',checks:160+15+25+8+227+67+16+6+12,files:160,symlinks:0,exit_roles:15,empty_stderr_files_in_build_tree:25,runtime_rows:227,source_rows:8,absolute_fls_inputs:67,fonts:16,pages:6,pdf_bytes:200921,pdf_sha256:sha(pdf),diagnostic_interpretation:'The sole 52-byte main.log:3 line reports enabled file:line:error formatting; it is configuration text, not an error.'};
process.stdout.write(JSON.stringify(result)+'\n');
