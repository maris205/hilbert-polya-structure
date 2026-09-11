'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),a=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',PAPER=ROOT+'/papers/211-kernel-image-projection-feedback',HERE=ROOT+'/docs/papers211_215_sequence/qa/p211_lifecycle_root01',DESK=ROOT+'/docs/papers211_215_sequence/qa/p211_lifecycle_integration_desk01';
const fields=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];let checks=0;const inputs={};
function eq(x,y,m){checks++;a.deepStrictEqual(x,y,m);}function need(x,m){checks++;a.ok(x,m);}
function key(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
function read(p){const b=fs.readFileSync(p),s=fs.statSync(p,{bigint:true}),l=fs.lstatSync(p,{bigint:true});need(s.isFile(),'ordinary resolved input');const k={...key(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null,stat:fields.map(f=>s[f].toString()),lstat:fields.map(f=>l[f].toString())};if(inputs[p])eq(k,inputs[p],'closing stable read');inputs[p]=k;return b;}
function obj(p){return JSON.parse(read(p));}
function walk(p){return fs.readdirSync(p).sort().flatMap(n=>{const q=p+'/'+n,s=fs.lstatSync(q);need(!s.isSymbolicLink(),'physical tree nonlink');return s.isDirectory()?walk(q):[q];});}
function manifest(p,expected){const b=read(p+'/SHA256SUMS');if(expected)eq(key(b).sha256,expected,'fixed expected seal');const rows=b.toString('utf8').trimEnd().split('\n'),names=[];for(const row of rows){const m=/^([a-f0-9]{64})  (.+)$/.exec(row);need(m,'strict nonself seal');need(!path.isAbsolute(m[2])&&!m[2].split('/').includes('..')&&m[2]!=='SHA256SUMS','bounded nonself path');names.push(p+'/'+m[2]);eq(key(read(p+'/'+m[2])).sha256,m[1],'full payload bytes');}eq(names.slice().sort(),walk(p).filter(x=>x!==p+'/SHA256SUMS').sort(),'whole sealed tree');return names.length;}
eq(process.cwd(),ROOT,'exact cwd');eq(process.argv.length,2,'no extra mode');read(__filename);
const r=obj(HERE+'/LIFECYCLE_RESULT.json'),ledger=obj(HERE+'/LIFECYCLE_INPUTS.json'),native=obj(HERE+'/AUDIT_NATIVE02.json');
eq(native.result.exit_code,0,'actual complete outer result');
const summary=JSON.parse(native.result.output);eq(summary.result,key(read(HERE+'/LIFECYCLE_RESULT.json')),'entire original result binding');eq(summary.status,r.status,'actual status');eq(summary.checks,r.checks,'actual counts');
eq(key(read(HERE+'/LIFECYCLE_INPUTS.json')),r.input_key,'whole original ledger');eq(ledger.stat_fields,fields,'full integer stats schema');eq(Object.keys(ledger.files).length,2597,'all2597 inputs');
for(let pass=0;pass<2;pass++)for(const [p,k]of Object.entries(ledger.files)){read(p);eq(inputs[p],k,'every original complete rich key');}
eq(manifest(PAPER,r.paper_seal.sha256),1000,'whole1000 paper seal');eq(key(read(PAPER+'/SHA256SUMS')),r.paper_seal,'all paper seal bytes');
for(const [p,k]of Object.entries(r.SEALS)){eq(key(read(p)),{bytes:k.bytes,sha256:k.sha256},'all53 accepted manifest bytes');}
const links=[];for(const p of [PAPER+'/README.md',PAPER+'/FINAL_QA_REPORT.md']){
 for(const m of read(p).toString('utf8').matchAll(/\[[^\]\n]*\]\(([^)\n]+)\)/g)){
  if(/^(?:https?:|mailto:|#)/.test(m[1]))continue;
  const q=path.resolve(path.dirname(p),decodeURIComponent(m[1].split('#')[0]));need(q.startsWith(ROOT+'/'),'bounded current link');need(fs.existsSync(q),'every final current link now exists');if(fs.statSync(q).isFile())read(q);links.push({source:p,literal:m[1],resolved:q});
 }
}eq(links.length,52,'all52 current lifecycle link occurrences');
for(const p of r.pending_final_links)need(fs.statSync(p).isFile(),'each actual formerly prospective gate now created');
eq(manifest(DESK,'7a95128fe82c2c87adb8360011cfb527076507e5721598406e330f4f52b98088'),10,'complete peer documentary desk');
const pinrows=read(DESK+'/INPUT_PINS_EXACT.sha256').toString('utf8').trimEnd().split('\n');eq(pinrows.length,35,'all35 exact reviewed documentary pins');
for(const row of pinrows){const m=/^([a-f0-9]{64})  (.+)$/.exec(row);need(m,'exact peer input row');const original=ROOT+'/'+m[2],p=original===PAPER+'/README.md'?DESK+'/README.reviewed.exact.md':original;eq(key(read(p)).sha256,m[1],'exact desk reviewed bytes with explicit historical README base');}
const old=read(DESK+'/README.reviewed.exact.md').toString('utf8');
const from='`/root/round211_rational_scout` contributed runtime infrastructure and this\nexecution-documentation update, reading the interface, documentation and';
const to='`/root/round211_rational_scout` contributed runtime infrastructure and the\nearlier author execution-documentation update, reading the interface, documentation and';
eq(old.split(from).length,2,'one exact editorial delta');need(Buffer.from(old.replace(from,to)).equals(read(PAPER+'/README.md')),'entire current README is exact suggested delta');
need(read(DESK+'/FINAL_QA_REPORT.reviewed.exact.md').equals(read(PAPER+'/FINAL_QA_REPORT.md')),'whole QA unchanged after peer desk');
for(const name of ['README','FINAL_QA_REPORT'])need(Buffer.concat([read(DESK+'/'+name+'.reviewed.exact.md'),Buffer.from('\n')]).equals(read(DESK+'/'+name+'.reviewed.md')),'preserved first extraLF failed copy');
const failure=obj(HERE+'/AUDIT_NATIVE01_FAILURE.json');eq(failure.result.exit_code,1,'first real failure preserved');need(failure.result.output.includes('SYMBOLIC_DYNAMICS_STATE.md'),'actual old navigation-key failure');
const diff=obj(HERE+'/SOURCE_V2_DIFF_NATIVE.json');eq(diff.result.exit_code,1,'actual differing source diff');need(diff.result.output.includes('@@ -112,7 +112,18 @@'),'exact single v2 loop hunk');eq((diff.result.output.match(/^@@ /gm)||[]).length,1,'one and only one source hunk');
read(HERE+'/audit_lifecycle.js');read(HERE+'/audit_lifecycle_v2.js');read(HERE+'/AUDIT01_DISPOSITION.md');read(HERE+'/RECEPTION.md');
for(const [p,k]of Object.entries({...inputs})){read(p);eq(inputs[p],k,'all closing inputs remain exact');}
const result={status:'PASS_ROOT_P211_LIFECYCLE_ACCEPTED',checks,input_paths:Object.keys(inputs).length,stat_fields:fields,inputs,original_lifecycle_checks:r.checks,original_lifecycle_input_paths:2597,all_original_keys_checked_twice:true,complete_paper_payloads:1000,complete_paper_files:1001,paper_seal:r.paper_seal,accepted_seals:53,closed_current_link_occurrences:52,peer_desk_payloads:10,peer_exact_pins:35,peer_readme_delta:'exact disclosed two-line historical-authorship clarification',current_open_findings:0,retained_final_warnings_per_build:1,retained_underfull_per_build:2,new_science:0,new_builds:0,new_views:0,paper_complete:true,batch_complete:false,external:'OWNER_AMBER / HOLD_EXTERNAL'};
const b=Buffer.from(JSON.stringify(result,null,2)+'\n');fs.writeFileSync(HERE+'/CLOSING_RESULT.json',b,{flag:'wx'});
console.log(JSON.stringify({status:result.status,checks,input_paths:result.input_paths,paper_complete:true,batch_complete:false,paper_seal:r.paper_seal,result:key(b)}));
