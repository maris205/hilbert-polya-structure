'use strict';
// Root-owned document receiver. Never import/evaluate the received sources.
const fs=require('node:fs'),path=require('node:path');
const crypto=require('node:crypto'),assert=require('node:assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const QA='docs/papers211_215_sequence/qa/';
const P=QA+'p212_build_dependency_source_preparation01/';
const A=QA+'p212_build_dependency_source_audit01/';
const O=QA+'p212_dependency_query_driver_preparation01/';
const D=QA+'p212_dependency_query_driver_source_audit01/';
const R=QA+'p212_dependency_query_driver_revision02/';
const S=QA+'p212_dependency_query_driver_revision02_same_reviewer01/';
const HERE=QA+'p212_dependency_source_root01/';
let checks=0;const inputs=new Map(),census=[],pinLists=[],nativeBindings=[];
function eq(a,b,label){checks++;assert.deepEqual(a,b,label);}
function need(a,label){checks++;assert.ok(a,label);}
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const stat=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const stable=s=>Object.fromEntries(Object.entries(s).filter(([k])=>k!=='atimeNs'));
function rel(p){
  if(p.startsWith(ROOT+'/'))p=p.slice(ROOT.length+1);
  need(/^[A-Za-z0-9_./-]+$/.test(p)&&!p.startsWith('/')&&path.normalize(p)===p&&!p.split('/').some(x=>['.','..',''].includes(x)),'workspace path '+p);
  return p;
}
function read(p){
  p=rel(p);const full=ROOT+'/'+p;
  for(let q=path.dirname(full);q.startsWith(ROOT);q=path.dirname(q)){
    const s=fs.lstatSync(q,{bigint:true});need(s.isDirectory()&&!s.isSymbolicLink(),'workspace ancestor '+q);if(q===ROOT)break;
  }
  const ls=fs.lstatSync(full,{bigint:true});need(ls.isFile(),'regular workspace file '+p);
  eq(fs.realpathSync(full),full,'unaliased workspace input');
  const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let b,before,after;
  try{before=fs.fstatSync(fd,{bigint:true});need(before.isFile(),'regular handle');b=fs.readFileSync(fd);after=fs.fstatSync(fd,{bigint:true});}finally{fs.closeSync(fd);}
  const st=fs.statSync(full,{bigint:true}),lsAfter=fs.lstatSync(full,{bigint:true});
  eq(stable(stat(before)),stable(stat(after)),'same handle stable '+p);
  eq(stable(stat(ls)),stable(stat(lsAfter)),'lstat stable '+p);
  eq(stable(stat(before)),stable(stat(st)),'handle/path stable '+p);
  eq(BigInt(b.length),before.size,'whole bytes '+p);
  const row={path:p,...pin(b),resolved:full,lstat:stat(lsAfter),stat:stat(st)};
  if(inputs.has(p)){
    const old=inputs.get(p);eq(pin(b),{bytes:old.bytes,sha256:old.sha256},'repeat whole bytes '+p);
    eq(stable(row.lstat),stable(old.lstat),'repeat lstat '+p);eq(stable(row.stat),stable(old.stat),'repeat stat '+p);
  }else inputs.set(p,row);
  return b;
}
const json=p=>JSON.parse(read(p).toString('utf8'));
function manifest(p,base){
  const b=read(p),s=b.toString('utf8');need(s.endsWith('\n'),'manifest newline');
  const rows=s.slice(0,-1).split('\n').map(line=>{
    const m=/^([a-f0-9]{64})  ([A-Za-z0-9_./-]+)$/.exec(line);need(m,'strict manifest line');return{path:rel(m[2]),sha256:m[1]};
  });eq(new Set(rows.map(x=>x.path)).size,rows.length,'no repeated manifest path');
  for(const r of rows)eq(pin(read(base+r.path)).sha256,r.sha256,'manifest payload '+base+r.path);
  return{pin:pin(b),rows};
}
function sealed(base,count,hash){
  const m=manifest(base+'SHA256SUMS',base);eq(m.pin.sha256,hash,'exact package seal '+base);eq(m.rows.length,count,'complete payload count');
  need(!m.rows.some(x=>x.path==='SHA256SUMS'),'nonself manifest');
  const files=[],dirs=[];
  function walk(sub){for(const name of fs.readdirSync(ROOT+'/'+base+sub).sort()){
    const p=sub+name,s=fs.lstatSync(ROOT+'/'+base+p,{bigint:true});need(!s.isSymbolicLink(),'no package alias');
    if(s.isDirectory()){dirs.push(p);walk(p+'/');}else{need(s.isFile(),'regular package payload');files.push(p);}
  }}walk('');eq(files.sort(),m.rows.map(x=>x.path).concat('SHA256SUMS').sort(),'exact package membership '+base);
  census.push({base,payloads:count,files:files.length,seal:m.pin,directories:dirs,empty_directories:dirs.filter(d=>!files.some(f=>f.startsWith(d+'/')))});
}
function pins(p,count){const m=manifest(p,'');eq(m.rows.length,count,'input count '+p);pinLists.push({path:p,entries:count,pin:m.pin});return m;}
function native(r,label,exit=0){
  need(r&&r.request&&r.result,'actual native object '+label);need(typeof r.request.cmd==='string','exact native request');
  need(typeof r.result.chunk_id==='string','actual chunk');eq(r.result.exit_code,exit,'native exit '+label);
  need(!r.result.session_id,'completed native '+label);need(typeof r.result.output==='string','full actual output');
  need(!r.result.output.startsWith('Warning: truncated output'),'no outer truncation header '+label);
  nativeBindings.push({label,chunk_id:r.result.chunk_id,exit_code:exit,output:pin(Buffer.from(r.result.output))});return Buffer.from(r.result.output);
}
function sedRecord(r,label){
  const m=/^sed -n '(\d+),(\d+|\$)p' ([A-Za-z0-9_./-]+)$/.exec(r.request.cmd);need(m,'exact single sed request '+label);
  const p=rel(m[3]);if(r.path!==undefined)eq(rel(r.path),p,'reported source path');
  const b=read(p),lines=b.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];
  const lo=Number(m[1]),hi=m[2]==='$'?lines.length:Number(m[2]);
  const expected=Buffer.from(lines.slice(lo-1,hi).join(''));eq(native(r,label),expected,'whole selected source-return '+label);
  return{path:p,lo,hi:Math.min(hi,lines.length),file_lines:lines.length,output:r.result.output};
}

read(HERE+'PLAN.md');read(HERE+'receive_source.js');read(HERE+'receive_source02.js');
for(const [base,count,hash]of [
  [P,15,'4dcf15a60e6e94d6001f0f0503ae8151317b470d1d6030519c1200d9473e1d5d'],
  [A,12,'c3527ff4c6e3002bb5c923fe3936b2a5826e776342a985dd1f8e85e9c0918a0c'],
  [O,6,'bbb6bed92196fcb2876db00dc83f0aad41f630f3d738f292f2047e91222d7917'],
  [D,11,'fbaacd59bef6cfa59a33615697a187e10859138a434a900035df9b00f3bddcfb'],
  [D+'context_contract/',4,'85b729ae7a34320a5a8c22942b3c53d33cc3f66045c79b23f10003dd1e9a1ccf'],
  [R,24,'629ecd398206b000f6da3d140fb031890a771d254a1aae952d8ee7bc4b87612b'],
  [S,8,'1ac37c6ecdabc9536dc053bf3b650dab094d4ea4e9fce306fdf1a1d0fd8d55cb'],
  [QA+'p212_initial_build_preparation01/',11,'9ff857383047b6160b2db56183c376e2fad25b1433bb49c932ea47c17fcf7f43'],
  [QA+'p212_initial_build_source_audit01/',17,'c8377cf4ac692f71622554efcb2fc95e5c41b1807fea1bf02be48622b8582359']
])sealed(base,count,hash);
for(const[p,count]of [[A+'INPUTS.sha256',75],[O+'SOURCE_INPUT_PINS.sha256',30],[D+'INPUTS.sha256',40],[D+'context_contract/INPUTS.sha256',17],[R+'MATERIAL_SOURCE_INPUTS.sha256',19],[R+'REVIEW_INPUTS.sha256',6],[R+'SAME_REVIEWER_DECISION_PINS.sha256',9],[S+'INPUT_PINS.sha256',40]])pins(p,count);

// Fixed whole companions: acceptance is only for these exact files, never a
// selective-field validator for arbitrary altered future data.
for(const[n,h]of Object.entries({
 'QUERY_FRONTIER.json':'762645257c2bea4f1d5c081de471cdee9eeb2b00dd312aab48d7dd4ed59cad1f',
 'INTERFACE.disabled.json':'2087003781dccd2bf4096031b903f0d2f9c5dfb833ae13407fd71af54dda10df',
 'CAPTURE_CONTRACT.json':'6f6b122d844b778bdf5ed4a0a7ddb1ddd583136cbc77306a8f7f4f62abb1483b',
 'SELECTOR_OBLIGATIONS.json':'2f20ab8b0df5bb67ddea8610839655cd05128ae9192c567573bac2248400d960'
})){
 const b=read(P+n);eq(pin(b).sha256,h,'entire fixed companion');eq(b,Buffer.from(JSON.stringify(JSON.parse(b),null,2)+'\n'),'canonical whole JSON');
 need(read(R+'driver.js').toString().includes(h),'exact operative hardcoded companion pin');
}
const f=json(P+'QUERY_FRONTIER.json');
const tuples=[['class_article','article.cls','pdflatex',true],['package_01_geometry','geometry.sty','pdflatex',true],['package_02_amsmath','amsmath.sty','pdflatex',true],['package_03_amssymb','amssymb.sty','pdflatex',true],['package_04_amsthm','amsthm.sty','pdflatex',true],['package_05_booktabs','booktabs.sty','pdflatex',true],['package_06_array','array.sty','pdflatex',true],['package_07_fontenc','fontenc.sty','pdflatex',true],['package_08_hyperref','hyperref.sty','pdflatex',true],['style_plain','plain.bst','bibtex',true],['config_pdflatex_texmf','texmf.cnf','pdflatex',false],['config_bibtex_texmf','texmf.cnf','bibtex',false],['format_pdflatex','pdflatex.fmt','pdflatex',true],['source_pdftexconfig','pdftexconfig.tex','pdflatex',false],['source_latex_kernel','latex.ltx','pdflatex',false],['map_pdftex','pdftex.map','pdflatex',false],['config_fmtutil','fmtutil.cnf','pdflatex',false],['config_updmap','updmap.cfg','pdflatex',false],['config_texfonts','texfonts.map','pdflatex',false]];
eq(f.initial_name_seeds.map(s=>[s.label,s.name,s.program,s.required]),tuples,'all independent 19 contexts');
eq(f.initial_name_seeds.map(s=>s.engine),Array(19).fill('pdftex'),'all engines');
const flags=['--no-mktex=tex','--no-mktex=fmt','--no-mktex=tfm','--no-mktex=pk'];
const later='LOOKUP_ONLY_AFTER_SEPARATE_OPTION_AND_RUNTIME_SOURCE_ACCEPTANCE';
const commands=['help','version'].map(x=>({label:'contract_'+x,phase:'CONTRACT_ONLY',argv:['/usr/bin/kpsewhich','--'+x],expected_exit_codes:[0],result:null}));
for(const[label,name,program]of tuples)for(const mode of ['default','all'])commands.push({label:label+'_'+mode,phase:later,argv:['/usr/bin/kpsewhich','--progname='+program,'--engine=pdftex',...flags,...(mode==='all'?['--all']:[]),name],expected_exit_codes:[0,1],result:null});
for(const name of ['TEXMF','TEXMFCNF','TEXMFHOME','TEXMFCONFIG','TEXMFVAR','TEXMFDBS','TEXINPUTS','BIBINPUTS','BSTINPUTS','shell_escape','openin_any','openout_any'])commands.push({label:'var_'+name,phase:later,argv:['/usr/bin/kpsewhich','--progname='+(['BIBINPUTS','BSTINPUTS'].includes(name)?'bibtex':'pdflatex'),'--engine=pdftex',...flags,'-var-value='+name],expected_exit_codes:[0,1],result:null});
commands.push({label:'expanded_TEXMF',phase:later,argv:['/usr/bin/kpsewhich','--progname=pdflatex','--engine=pdftex',...flags,'-expand-path=$TEXMF'],expected_exit_codes:[0,1],result:null});
eq(commands.length,53);eq(f.ordered_command_proposals,commands,'every ordered full proposal');
eq(f.environment,{PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'});
const graph=json(QA+'p212_initial_build_preparation01/SOURCE_GRAPH.json');
eq(f.profile.source_pins,graph.source_pins);eq(graph.total_files,8);eq(graph.total_bytes,19659);
let sourceBytes=0;for(const[name,k]of Object.entries(graph.source_pins)){
 const b=read(graph.paper_root+'/'+name);eq(pin(b),k);eq(b,read(graph.accepted_source_original_root+'/'+name),'raw physical source pair '+name);sourceBytes+=b.length;
}eq(sourceBytes,19659);
const initial=json(P+'METADATA_NATIVE01.json'),closing=json(P+'CLOSING_NATIVE.json');
eq(native(initial,'preparation actual helper'),read(P+'PREPARATION_RESULT.json'),'entire original helper stdout');
eq(native(closing.metadata_repeat,'preparation actual repeat'),read(P+'PREPARATION_RESULT.json'),'entire actual repeat stdout');
const prep=json(P+'PREPARATION_RESULT.json');eq(prep.checks,2321);eq(prep.workspace_input_paths,70);eq(Object.keys(prep.workspace_pins).length,70);
for(const[p,k]of Object.entries(prep.workspace_pins)){eq(pin(read(p)),{bytes:k.bytes,sha256:k.sha256});eq(k.resolved,p);eq(k.symlink,null);}
for(const[n,k]of Object.entries(prep.prepared_files))eq(pin(read(P+n)),k);
const orig=json(P+'ORIGINAL_READS_NATIVE.json');let originalReads=0;
for(const r of [...orig.intake,...orig.sources,...orig.paper_sources]){sedRecord(r,'preparation original '+originalReads);originalReads++;}eq(originalReads,25);
eq(native(orig.old_graph_excerpt_projection,'archived graph projection'),read(P+'OLD_TEX_MECHANISM.json'));
for(const r of closing.source_reads){const out=native(r,'closing source '+r.name);eq(out,read(P+r.name));}
// Four full auditor read archives, including a complete six-part old lock.
let sourceAuditReads=0;const lockParts=[];
for(const filename of ['NATIVE_PACKET_READS.json','NATIVE_ORIGINAL_READS.json','NATIVE_ADDITIONAL_READS.json','NATIVE_LOCK_READS.json']){
 for(const r of json(A+filename).records){const row=sedRecord(r,filename+'/'+sourceAuditReads++);if(filename==='NATIVE_LOCK_READS.json')lockParts.push(row);}
}eq(sourceAuditReads,80);eq(lockParts.length,6);
eq(Buffer.from(lockParts.map(x=>x.output).join('')),read(lockParts[0].path),'whole historical lock from all six original parts');
const historical=json(P+'HISTORICAL_LOCK_DOCUMENT_NATIVE.json');
const lineage=json(QA+'p212_initial_build_preparation01/LINEAGE.json');const lockBytes=read(lineage.old_lock.path),lock=JSON.parse(lockBytes);
eq(pin(lockBytes),lineage.old_lock.pin);eq(Object.keys(lock.entries).length,840);
const projection={path:rel(lineage.old_lock.path),...pin(lockBytes),fields:Object.keys(lock),entry_count:840,queries:lock.queries,query_commands:lock.query_commands,cwd_relative_absence_roles:lock.cwd_relative_absence_roles,host_referents_dereferenced:0};
eq(native(historical,'whole historical lock projection'),Buffer.from(JSON.stringify(projection,null,2)+'\n'));
const documentary=json(A+'DOCUMENTARY_CHECKS.json');eq(documentary.checks,252);eq(documentary.failed,0);eq(documentary.records.length,252);need(documentary.records.every(r=>r.pass===true),'actual archived 252 labels preserved');
const am=json(A+'NATIVE_METADATA.json');eq(am.raw_source_comparisons.length,8);
for(const r of am.raw_source_comparisons){eq(native(r,'source audit actual raw cmp '+r.name),Buffer.alloc(0));}
const findings=json(A+'FINDINGS.json');eq(findings.census,{critical:0,major:0,minor_coverage_observations:2,current_payload_violations:0,mandatory_current_plan_revisions:0});
eq(findings.observations.map(x=>[x.id,x.current_payload_defect]),[['DSA-O1',false],['DSA-O2',false]]);

const old=read(O+'driver.js'),revised=read(R+'driver.js'),difference=read(R+'DRIVER.diff');
eq(pin(old),{bytes:49231,sha256:'fc61b463fbb8cb6c09887f12a85152e9e345c242ec0c3693621f396c42066381'});
eq(pin(revised),{bytes:51293,sha256:'57ce0d5815e3b0d051925dd351030d26067eb796a47f7058cf8f3a08c5e90032'});
eq(old.toString().split('\n').length-1,938);eq(revised.toString().split('\n').length-1,978);
eq(pin(difference),{bytes:11044,sha256:'c390010877b2f6c1d185cc701d9b9d3e62fde9c924699661fbbc9314b49ba414'});
eq(read(R+'INTERFACE.disabled.json'),read(O+'INTERFACE.disabled.json'),'raw disabled equality');eq(json(R+'INTERFACE.disabled.json').enabled,false);
const review=json(S+'DELTA_ACCEPTANCE.json'),oldFinding=json(D+'FINDINGS.json');
eq(oldFinding.census.major_open,1);eq(oldFinding.findings[0].id,'DQD-S1');eq(oldFinding.findings[0].status,'OPEN_SOURCE_REVISION_REQUIRED');
eq(review.reviewer,'/root/round211_functional_surgery_residual');eq(review.same_as_original_reviewer,true);eq(review.reviewer_is_implementation_contributor,false);
eq(review.current_source_census,{critical_open:0,major_open:0,other_blocking_source_findings:0,retained_nonblocking_minor_coverage_observations:1,executed_incidents:0});
eq(review.finding_outcomes[0].current_exact_revision_status,'RESOLVED_SOURCE_DELTA_ACCEPTED');eq(review.finding_outcomes[1].id,'DQD-O1');eq(review.finding_outcomes[1].implemented_by_revision,false);
eq(pin(read(review.exact_review_inputs.manifest_path)),{bytes:922,sha256:'3ac8a24d5eb5d791a207cd70086a79530344c03903d99c6fc04390005947b012'});
const target=manifest(review.exact_review_inputs.manifest_path,'');eq(target.rows,review.exact_review_inputs.members);eq(target.rows.length,6);
for(const[k,v]of Object.entries(review.authority))eq(v,k==='source_delta_review_accepted'?true:k==='external'?'HOLD_EXTERNAL':false,'exact decision authority '+k);
const rr=json(S+'NATIVE_READS.json');eq(rr.records.length,28);const success=[],failures=[];
for(let i=0;i<rr.records.length;i++){
 const r=rr.records[i];if(i===17){native(r,'retained navigation failure',2);need(r.request.cmd.endsWith('/STAGED_BINDING_AND_READ_CONTRACT.md'),'exact failed guessed filename');failures.push({index:i,request:r.request,result:r.result});}
 else success.push(sedRecord(r,'same-reviewer source '+i));
}eq(success.length,27);
for(const[p,expected]of [[O+'driver.js',938],[R+'driver.js',978],[P+'QUERY_FRONTIER.json',1325]]){
 const pieces=success.filter(x=>x.path===p).sort((a,b)=>a.lo-b.lo);let next=1;
 for(const piece of pieces){eq(piece.lo,next,'contiguous full source');next=piece.hi+1;}eq(next,expected+1,'complete source EOF');
 eq(Buffer.from(pieces.map(x=>x.output).join('')),read(p),'whole reviewer source reconstruction');
}
const integrity=json(S+'INTEGRITY_NATIVE.json');
eq(native(integrity.initial_checks[0],'reviewer actual original diff',1),difference);eq(read(S+'ACTUAL_DRIVER_DIFF.raw'),difference);
eq(native(integrity.initial_checks[1],'reviewer actual disabled cmp'),Buffer.alloc(0));
eq(native(integrity.final_delta_and_pin_checks[0],'reviewer actual diff cmp'),Buffer.alloc(0));
eq(native(integrity.actual_pin_generation,'reviewer actual40 input generation'),read(S+'INPUT_PINS.sha256'));
const forty=manifest(S+'INPUT_PINS.sha256','');
eq(native(integrity.final_delta_and_pin_checks[1],'reviewer actual40 closing check'),Buffer.from(forty.rows.map(x=>x.path+': OK\n').join('')));
const ad=json(R+'DIFF_AND_READ_ENTRY_NATIVE.json');eq(native(ad.records[0],'author actual original diff',1),difference);eq(native(ad.records[1],'author actual disabled cmp'),Buffer.alloc(0));

// Complete input recheck. The final result is document evidence only.
for(const p of [...inputs.keys()])read(p);
const result={schema:'p212-root-finite-dependency-source-reception-v1',status:'PASS_SOURCE_ORIGINALS_ONLY_HOLD_OPERATIONAL',checks,
 workspace_input_paths:inputs.size,packages:census,input_pin_lists:pinLists,
 source_pairs:8,source_bytes:sourceBytes,frontier_names:19,ordered_proposals:53,
 preparation_archived_checks:2321,preparation_whole_original_read_bindings:originalReads,
 independent_plan_archived_checks:252,independent_plan_whole_read_bindings:sourceAuditReads,
 same_reviewer_successful_source_ranges:27,same_reviewer_preserved_navigation_failures:failures,
 original_driver:pin(old),accepted_revised_driver:pin(revised),complete_difference:pin(difference),
 same_reviewer_exact_six_input_manifest:target.pin,
 limitations:['DSA-O1/DSA-O2 are preserved validator limits, not arbitrary-data acceptance','DQD-S1 remains open for immutable old source, resolved for exact revision02 only','DQD-O1 and outer startup/product/session key remain pending','Archived2321/252 are not newly executed helper checks','No submitted source/driver/emitter import, AST or execution','No host-like document path dereferenced; old840 is opaque data','14 integer fields sampled; access time excluded only from stability, no continuous-race/hermeticity claim'],
 actual_native_bindings:nativeBindings,inputs:[...inputs.values()],
 authority:{source_only:true,host_query:false,body_capture:false,driver_execution:false,installed_option_acceptance:false,dependency_lock:false,build:false,science:false,manuscript_review:false,visual_review:false,paper_completion:false,batch_completion:false,Git:false,external:'HOLD_EXTERNAL'}};
process.stdout.write(JSON.stringify(result,null,2)+'\n');
