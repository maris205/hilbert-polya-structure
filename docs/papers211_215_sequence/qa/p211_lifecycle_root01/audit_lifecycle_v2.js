'use strict';
// Documentary lifecycle audit. Imports only Node builtins; never spawns a child.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const PAPER=ROOT+'/papers/211-kernel-image-projection-feedback';
const BATCH=ROOT+'/docs/papers211_215_sequence',QA=BATCH+'/qa';
const HERE=QA+'/p211_lifecycle_root01';
const FIELDS=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];
const ENV4={LANG:'C.UTF-8',LC_ALL:'C.UTF-8',PATH:'/usr/bin:/bin',TZ:'UTC'};
const READS={},SEALS={},LINKS=[];let checks=0;
function need(ok,label){checks++;assert.ok(ok,label);}
function equal(x,y,label){checks++;assert.deepStrictEqual(x,y,label);}
function key(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
function read(p){
 need(path.isAbsolute(p),'absolute read');const b=fs.readFileSync(p),s=fs.statSync(p,{bigint:true}),l=fs.lstatSync(p,{bigint:true});
 need(s.isFile(),'regular resolved file');const k={...key(b),resolved:fs.realpathSync(p),symlink:l.isSymbolicLink()?fs.readlinkSync(p):null,stat:FIELDS.map(f=>s[f].toString()),lstat:FIELDS.map(f=>l[f].toString())};
 if(READS[p])equal(k,READS[p],'whole rich input stable '+p);READS[p]=k;return b;
}
function obj(p){return JSON.parse(read(p));}
function projection(k,fields){return Object.fromEntries(fields.map(f=>[f,k[f]]));}
function checkKey(p,expected){read(p);for(const k of Object.keys(expected))need(['bytes','sha256','resolved','symlink','stat','lstat'].includes(k),'known full-key field');equal(projection(READS[p],Object.keys(expected)),expected,'entire expected key '+p);}
function tree(base){
 const names=[];
 for(const n of fs.readdirSync(base).sort()){
  const p=base+'/'+n,s=fs.lstatSync(p);need(!s.isSymbolicLink(),'no physical package symlinks');
  if(s.isDirectory())for(const f of tree(p))names.push(n+'/'+f);else{need(s.isFile(),'ordinary package file');names.push(n);}
 }
 return names;
}
function manifest(base,complete=true,name='SHA256SUMS'){
 const raw=read(base+'/'+name),text=raw.toString('utf8');need(text.endsWith('\n'),'complete LF manifest');
 const map={};for(const row of text.slice(0,-1).split('\n')){
  const m=/^([a-f0-9]{64})  (.+)$/.exec(row);need(m,'strict manifest row');const p=m[2];
  need(!path.isAbsolute(p)&&!p.split('/').some(x=>['','..','.'].includes(x))&&p!==name,'safe nonself member');need(!map[p],'unique manifest member');
  const b=read(base+'/'+p);equal(key(b).sha256,m[1],'entire payload hash');map[p]=m[1];
 }
 if(complete)equal(Object.keys(map).sort(),tree(base).filter(n=>n!==name).sort(),'complete manifest membership '+base);
 SEALS[base+'/'+name]={...key(raw),payloads:Object.keys(map).length};return map;
}
function same(p,q){const a=read(p),b=read(q);need(a.equals(b),'whole raw byte equality '+p+' / '+q);return key(a);}
function save(n,x){const b=Buffer.from(JSON.stringify(x,null,2)+'\n');fs.writeFileSync(HERE+'/'+n,b,{flag:'wx'});return key(b);}
function localLinks(p,pending){
 const body=read(p).toString('utf8');
 for(const m of body.matchAll(/\[[^\]\n]*\]\(([^)\n]+)\)/g)){
  let target=m[1];if(/^(?:https?:|mailto:)/.test(target)||target.startsWith('#'))continue;
  need(!/\s/.test(target),'simple explicit local Markdown target');target=decodeURIComponent(target.split('#')[0]);
  const resolved=path.resolve(path.dirname(p),target);need(resolved.startsWith(ROOT+'/'),'workspace lifecycle link');
  const exists=fs.existsSync(resolved);need(exists||pending.has(resolved),'resolved current lifecycle link '+resolved);
  if(exists){const s=fs.statSync(resolved);need(s.isFile()||s.isDirectory(),'ordinary local link target');if(s.isFile())read(resolved);}
  LINKS.push({source:p,literal:target,resolved,exists,pending_exact_future_gate:!exists});
 }
}
function receipt(p){
 const r=obj(p);equal(r.exit_code,0,'actual original native exit');equal(r.wrapper_exit_code,0,'actual original wrapper exit');equal(r.failure,null,'actual original failure null');
 equal(r.status,'COMPLETED','actual original completion');equal(r.streams_complete,true,'whole original native streams');equal(r.timed_out,false,'no timeout');equal(r.interrupted,false,'no interruption');
 equal(r.environment,ENV4,'entire original environment');
 equal(r.process_group_settlement.quiescent,true,'accepted original quiescence');equal(r.process_group_settlement.remaining_members,[],'no original remaining members');
 const base=path.dirname(p);equal(key(read(base+'/stdout.raw')),r.stdout,'whole actual stdout');equal(key(read(base+'/stderr.raw')),r.stderr,'whole actual stderr');return r;
}
function scientific(){
 const sroot=QA+'/p211_lifecycle_scientific_key_root01';equal(Object.keys(manifest(sroot)).length,13,'complete scientific root package');
 const result=obj(sroot+'/RUN_RESULT.json');equal(result.status,'PASS_ROOT_CURRENT_SCIENTIFIC_KEY','accepted separate current key');
 equal(result.checker_checks,26038,'actual current documentary check');equal(result.scientific_keys,427,'complete427');
 for(const [p,k]of Object.entries(result.READ_INPUTS))checkKey(p,k);
 const s=obj(QA+'/p211_lifecycle_scientific_key_desk01/SCIENTIFIC_REUSE_SPEC_v2.json');
 const output=obj(sroot+'/stdout.json');equal(output.DOMAIN_BEFORE,output.DOMAIN_AFTER,'entire scientific endpoints');
 equal(output.DOMAIN_AFTER.scientific_files,s.files,'full427 returned domain');equal(output.DOMAIN_AFTER.configuration_paths,s.configuration.paths,'full69 returned settings');
 equal(output.DOMAIN_AFTER.memberships,s.configuration.memberships,'full5/292 returned members');equal(output.DOMAIN_AFTER.loader_states,s.loader_search_directory_states,'full9 returned loader states');
 equal(Object.values(output.DOMAIN_AFTER.cache_lexists),Array(15).fill(false),'all15 actual absent caches');
 need(!s.files[PAPER+'/README.md'],'changed lifecycle README is not a scientific replay input');
 const pairs=[];
 for(const [role,r] of Object.entries(s.roles)){
  const base=r.attempt;equal(Object.keys(manifest(base)).length,104,'entire accepted strict pair package');
  for(const stage of ['outer','launcher','recorder','child01','child02'])manifest(base+'/'+stage);
  const commands=base+'/recorder/commands',p1=commands+'/03_verify_01/stdout.raw',p2=commands+'/03_verify_02/stdout.raw';
  const canonical=r.canonical.path;const k=same(p1,canonical);same(p2,canonical);same(p1,p2);equal(k,{bytes:r.canonical.bytes,sha256:r.canonical.sha256},'whole role canonical');
  for(let i=1;i<=2;i++){
   const rec=receipt(commands+'/03_verify_0'+i+'/RECEIPT.json');equal(rec.argv.slice(0,6),['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+base+'/never_created_child0'+i+'_cache'],'exact child role flags/cache');
   equal(rec.argv[7],'child0'+i,'actual original child role');equal(rec.argv[8],r.binding,'actual pair binding');equal(rec.argv[9],key(read(r.binding)).sha256,'entire original pair binding');equal(rec.cwd,base+'/recorder/capsule','original child capsule cwd');
  }
  const compare=[['04_canonical_1',p1,canonical],['04_canonical_2',p2,canonical],['05_pair',p1,p2]];
  for(const [name,a,b]of compare){const rec=receipt(commands+'/'+name+'/RECEIPT.json');equal(rec.argv,['/usr/bin/cmp','--',a,b],'actual original three byte comparisons');equal(rec.stdout.bytes,0,'cmp empty stdout');equal(rec.stderr.bytes,0,'cmp empty stderr');}
  pairs.push({role,canonical:k,strict_producers:2,original_native_comparisons:3,new_science:0});
 }
 return {current_key_root:result.status,current_read_paths:result.read_paths,pairs,scientific_keys:427,new_science:0};
}
function reviewsAndFreezes(mapping){
 const aBase=BATCH+'/reviews/p211_a',bBase=BATCH+'/reviews/p211_b';
 const am=manifest(aBase),bm=manifest(bBase);equal(Object.keys(am).length,50,'acceptedA50');equal(Object.keys(bm).length,39,'acceptedB39');
 equal(SEALS[aBase+'/SHA256SUMS'].sha256,'a0677d174d3e9af26b32fabb8a97e099d12753101734a6fe43252eea636b97cc','immutable accepted A seal');
 equal(SEALS[bBase+'/SHA256SUMS'].sha256,'45b7c0337259da2fccb078cf4d7b84ec7228a16a6bf6089167c19a26c477ca46','immutable accepted B seal');
 const a=obj(aBase+'/DELTA_ACCEPTANCE.json'),b=obj(bBase+'/DELTA_ACCEPTANCE.json');
 equal(a.status,'ACCEPTED_EXACT_NO_CHANGE_BY_SAME_A_REVIEWER','actual sameA');equal(b.decision,'SAME_B_ACCEPTED_EXACT_NO_CHANGE','actual sameB');
 for(const r of [a,b]){equal(r.delta_accepted,true,'actual delta accepted');equal(r.delta_received,true,'actual delta received');}
 equal(a.current_open_findings.total,0,'A current0');equal(b.current_finding_census.current_open_total,0,'B current0');need(a.reviewer!==b.reviewer,'distinct A/B processes');
 equal(obj(aBase+'/FINDINGS.json').current_open_total,0,'historical A report0');equal(obj(bBase+'/FINDINGS.json').current_open_total,0,'historical B report0');
 equal(key(read(ROOT+'/'+a.response.path)),{bytes:a.response.bytes,sha256:a.response.sha256},'exact A response');checkKey(b.actual_response.path,b.actual_response.key);
 const f=[0,1,2].map(i=>PAPER+'/frozen_round'+i),m=f.map(p=>manifest(p));
 equal(m.map(x=>Object.keys(x).length),[32,83,123],'whole physical freeze payload counts');
 for(const n of Object.keys(m[0])){
  same(f[0]+'/'+n,f[1]+'/'+n);same(f[1]+'/'+n,f[2]+'/'+n);
  same(f[2]+'/'+n,n==='README.md'?mapping.mappings[0].physical_copy:PAPER+'/'+n);
 }
 for(const n of [...Object.keys(am),'SHA256SUMS']){same(aBase+'/'+n,f[1]+'/review_a/'+n);same(aBase+'/'+n,f[2]+'/review_a/'+n);}
 for(const n of [...Object.keys(bm),'SHA256SUMS'])same(bBase+'/'+n,f[2]+'/review_b/'+n);
 for(const p of ['p211_round0_root_reception','p211_round1_root_reception','p211_round2_original_root01','p211_a_final_root','p211_b_final_root'])read(QA+'/'+p+'/RECEPTION.md');
 return {A:{reviewer:a.reviewer,payloads:50,open:0},B:{reviewer:b.reviewer,payloads:39,open:0},freeze_payloads:[32,83,123],new_reviews:0};
}
function artifacts(){
 const diagBase=QA+'/p211_terminal_diagnostic_disposition01';equal(Object.keys(manifest(diagBase)).length,6,'entire accepted disposition packet');
 const d=obj(diagBase+'/DOCUMENTARY_CHECK.json');equal(d.terminal_artifact_acceptance,true,'current terminal artifact decision');equal(d.current_open_findings,[],'no current census finding');
 equal(d.current_findings.map(x=>x.id),['P211-COLD1-IO-D1','P211-COLD2-DIAGNOSTIC-CENSUS'],'exact two resolved findings');
 for(const x of d.current_findings)equal(x.status,'RESOLVED_BY_ADDITIVE_COMPLETE_CENSUS_AND_ROOT_DISPOSITION','additive finding resolution');
 equal(d.stat_fields,FIELDS,'exact full rich-key statistic schema');equal(Object.keys(d.inputs).length,1452,'entire accepted semantic/documentary key');
 const historicalBase=QA+'/control_before_p211_terminal_artifacts_accepted01';
 const historical=obj(historicalBase+'/MAPPING.json');manifest(historicalBase);
 equal(historical.stat_fields,FIELDS,'accepted old central full-stat schema');
 const central=[ROOT+'/SYMBOLIC_DYNAMICS_STATE.md',BATCH+'/PIPELINE_STATE.md'];
 equal(Object.keys(historical.original_keys).sort(),central.slice().sort(),'only two explicit original navigation roles');
 for(const [p,k]of Object.entries(d.inputs)){
  if(!central.includes(p)){checkKey(p,k);continue;}
  equal(historical.original_keys[p],k,'entire exact old navigation key, including original integer stats');
  const copy=historical.copies.filter(x=>x.source===p);equal(copy.length,1,'unique accepted physical historical copy');
  equal(copy[0].result.exit_code,0,'actual original physical copy');equal(copy[0].comparison.result.exit_code,0,'actual original raw comparison');
  equal(key(read(copy[0].archive)),{bytes:k.bytes,sha256:k.sha256},'entire archived original navigation bytes');
 }
 for(const p of ['p211_terminal_cold_artifact_root01','p211_terminal_cold_artifact_root02','p211_font_warning_root01','p211_terminal_pair_pages_root01'])manifest(QA+'/'+p);
 const cold=[1,2].map(i=>PAPER+'/qa_final/cold_build_'+i),phases=[];
 for(let i=1;i<=2;i++){
  const base=cold[i-1];equal(Object.keys(manifest(base)).length,362,'complete accepted cold tree');manifest(base+'/inner');
  equal(key(read(base+'/SHA256SUMS')),d.complete_cold_build_seals[String(i)],'exact accepted cold seal');
  for(const phase of ['refresh','enable','capture']){
   const dir=QA+'/p211_terminal_enable_root01/build_'+i;
   manifest(dir+'/'+phase+'01');manifest(dir+'/'+phase+'_entry01');manifest(dir+'/'+phase+'_reception01');
   const r=obj(dir+'/'+phase+'_reception01/RESULT.json');equal(r.phase,phase,'received actual phase');equal(r.build_number,i,'distinct actual build');
   need(r.status.startsWith('PASS'),'actual phase reception success');phases.push({build:i,phase,checks:r.checks,actual_controller_checks:r.actual_controller_checks});
  }
  const b=d.builds[i-1];equal(b.final_actual_warning_emissions.length,1,'one retained font expansion warning');equal(b.retained_underfull.length,2,'two retained underfull');equal(b.warning_free,false,'never warning free');
  equal(b.final_unresolved_actual_diagnostics,[],'no unresolved reference/error class');equal(b.final_missing_character_diagnostics,[],'no actual missing-character diagnostics');
  equal(key(read(base+'/inner/source_only/main.pdf')),b.final_pdf,'actual whole terminal PDF');
  const log=read(b.final_log.path).toString('utf8').split('\n');
  for(const row of [...b.final_actual_warning_emissions,...b.retained_underfull])equal(log[row.line-1],row.text,'exact actual retained diagnostic line');
  const names=['main.tex','math_commands.tex','references.bib',...fs.readdirSync(PAPER+'/sections').sort().map(n=>'sections/'+n)];equal(names.length,9,'nine build sources');
  for(const n of names){same(PAPER+'/'+n,PAPER+'/frozen_round2/'+n);same(PAPER+'/'+n,base+'/inner/source_only/'+n);}
 }
 for(const row of d.raw_log_pairs){equal(same(row.cold1,row.cold2),row.pin,'all18 whole actual log pairs');}
 equal(d.raw_log_pairs.length,18,'all18 log roles');same(cold[0]+'/inner/source_only/main.pdf',cold[1]+'/inner/source_only/main.pdf');
 for(let i=1;i<=5;i++){
  const name='page-'+String(i).padStart(4,'0')+'.png',p=cold[0]+'/inner/pages/'+name;same(p,cold[1]+'/inner/pages/'+name);
  const v=obj(QA+'/p211_terminal_pair_pages_root01/PAGE'+i+'_VIEW_NATIVE.json');equal(v.tool,'view_image','original actual view tool');equal(v.request,{path:p,detail:'original'},'exact original view request');
  const prefix='data:application/octet-stream;base64,';need(v.result.image_url.startsWith(prefix),'actual original image MIME');need(Buffer.from(v.result.image_url.slice(prefix.length),'base64').equals(read(p)),'entire actual viewed bytes');
 }
 return {phases,actual_terminal_builds:2,actual_view_calls:5,view_reuse_for_identical_second:true,new_builds:0,new_views:0,current_open_findings:0,retained_font_warnings_each:1,retained_underfull_each:2};
}
function main(){
 equal(process.cwd(),ROOT,'exact cwd');equal(process.argv.length,2,'no expanded mode');read(__filename);read(HERE+'/PLAN.md');
 const baseline=obj(HERE+'/PAPER_BEFORE.json');equal(baseline.stat_fields,FIELDS,'baseline full integer stats');equal(Object.keys(baseline.files).length,999,'all999 old paper files');
 const mapping=obj(HERE+'/MAPPING.json');equal(mapping.mappings.length,3,'three physical old controls');
 for(const row of mapping.mappings){checkKey(row.physical_copy,row.copy_full_key);equal(key(read(row.physical_copy)),{bytes:row.original_full_key.bytes,sha256:row.original_full_key.sha256},'complete original physical bytes');}
 const expected=Object.keys(baseline.files).map(p=>p.slice(PAPER.length+1)).concat('FINAL_QA_REPORT.md').sort();equal(tree(PAPER),expected,'only declared new finalQA before seal');
 for(const [p,k]of Object.entries(baseline.files))if(p!==PAPER+'/README.md')checkKey(p,k);
 need(key(read(PAPER+'/README.md')).sha256!==baseline.files[PAPER+'/README.md'].sha256,'only expected README changed');
 const science=scientific(),reviews=reviewsAndFreezes(mapping),terminal=artifacts();
 const pending=new Set([HERE+'/LIFECYCLE_RESULT.json',HERE+'/RECEPTION.md',PAPER+'/SHA256SUMS']);
 for(const p of [PAPER+'/README.md',PAPER+'/FINAL_QA_REPORT.md'])localLinks(p,pending);
 for(const [p,k]of Object.entries({...READS}))checkKey(p,k);
 // All scientific/build/review checks above are reuse/documentary operations.
 // The first current whole-paper seal is emitted only after their success.
 const names=tree(PAPER);equal(names.length,1000,'complete current1000 payloads');
 const seal=Buffer.from(names.map(n=>key(read(PAPER+'/'+n)).sha256+'  '+n+'\n').join(''));
 fs.writeFileSync(PAPER+'/SHA256SUMS',seal,{flag:'wx'});manifest(PAPER);
 const inputs={...READS};for(const [p,k]of Object.entries(inputs))checkKey(p,k);
 const inputKey=save('LIFECYCLE_INPUTS.json',{stat_fields:FIELDS,files:READS});
 const result={status:'PASS_ROOT_P211_LIFECYCLE_CHECKS_PENDING_FINAL_ORIGINAL_RECEPTION',checks,input_paths:Object.keys(READS).length,input_key:inputKey,paper_payloads:1000,paper_files:1001,paper_seal:key(seal),old_paper_files:999,unchanged_old_files:998,changed_existing:['README.md'],added:['FINAL_QA_REPORT.md','SHA256SUMS'],science,reviews,terminal,SEALS,LINKS,pending_final_links:[...new Set(LINKS.filter(r=>!r.exists).map(r=>r.resolved))],new_scientific_runs:0,new_builds:0,new_views:0,paper_complete:false,batch_complete:false,external:'OWNER_AMBER / HOLD_EXTERNAL'};
 const output=save('LIFECYCLE_RESULT.json',result);console.log(JSON.stringify({status:result.status,checks,input_paths:result.input_paths,paper_payloads:1000,paper_files:1001,paper_seal:result.paper_seal,result:output}));
}
try{main();}catch(e){console.error(e.stack||String(e));process.exitCode=1;}
