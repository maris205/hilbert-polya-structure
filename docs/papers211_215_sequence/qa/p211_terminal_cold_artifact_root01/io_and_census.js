'use strict';
// Explicit pure-metadata reuse and independent all-log reconstruction, no submitted execution.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),util=require('util'),vm=require('vm');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa';
const AUD=QA+'/p211_terminal_cold_artifact_audit01',IO=AUD+'/io_lane',OWN=QA+'/p211_terminal_cold_artifact_root01';
const INNER=ROOT+'/papers/211-kernel-image-projection-feedback/qa_final/cold_build_1/inner';
const F=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];let checks=0;const inputs={};
function need(x,m){checks++;if(!x)throw Error(m)}function eq(a,b,m){need(util.isDeepStrictEqual(a,b),m)}
function pin(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')}}
function read(p){need(p.startsWith(ROOT+'/')&&path.normalize(p)===p,'workspace');let q=ROOT;for(let n of path.relative(ROOT,p).split('/')){q+='/'+n;need(!fs.lstatSync(q).isSymbolicLink(),'no alias');}let s=fs.statSync(p,{bigint:true}),l=fs.lstatSync(p,{bigint:true});need(s.isFile()&&l.isFile()&&l.nlink===1n&&fs.realpathSync(p)===p,'ordinary file');let b=fs.readFileSync(p),v={...pin(b),stat:F.map(k=>s[k].toString()),lstat:F.map(k=>l[k].toString())};eq(F.map(k=>fs.statSync(p,{bigint:true})[k].toString()),v.stat,'stable stat');eq(F.map(k=>fs.lstatSync(p,{bigint:true})[k].toString()),v.lstat,'stable lstat');need(BigInt(b.length)===s.size,'whole read');if(inputs[p])eq(v,inputs[p],'stable repeat');inputs[p]=v;return b;}
function obj(p){return JSON.parse(read(p))}
function files(base){let out=[];for(let n of fs.readdirSync(base).sort()){let p=base+'/'+n,s=fs.lstatSync(p);need(!s.isSymbolicLink(),'tree no alias');if(s.isDirectory())out.push(...files(p));else{need(s.isFile(),'regular member');out.push(p);}}return out;}
function seal(base,count){let raw=read(base+'/SHA256SUMS').toString(),names=[];for(let line of raw.trimEnd().split('\n')){let m=/^([a-f0-9]{64})  (.+)$/.exec(line);need(!!m&&!path.isAbsolute(m[2])&&!m[2].split('/').some(n=>['','..','.'].includes(n))&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'unique nonself');names.push(m[2]);eq(pin(read(base+'/'+m[2])).sha256,m[1],'whole payload');}need(names.length===count,'exact payload count');eq(names,[...names].sort(),'seal sorted');eq(files(base),[...names,'SHA256SUMS'].map(n=>base+'/'+n).sort(),'complete tree');return pin(Buffer.from(raw));}
function main(){
 read(OWN+'/io_and_census.js');read(OWN+'/SCOPE.md');const outer=seal(AUD,309);
 eq(outer,{bytes:29007,sha256:'9e088c66880e9f5e787ef0c1173307d45b1e6c55e5d12fca3d430b69022291cc'},'accepted exact outer seal');
 const run=obj(AUD+'/run04/RESULT.json'),beforeRaw=read(AUD+'/run04/READ_INPUTS_BEFORE.json');
 need(beforeRaw.equals(read(AUD+'/run04/READ_INPUTS_AFTER.json')),'entire run04 before/after raw keys equal');
 const before=JSON.parse(beforeRaw);need(Object.keys(before).length===474&&run.read_paths===474&&run.read_bytes===21315014&&run.checks===177773&&run.failure===null&&run.open_findings===1&&!run.build_acceptance,'actual main scope');
 let total=0;for(let [p,k]of Object.entries(before)){eq(pin(read(p)),k,'all474 actual full bytes unchanged');total+=k.bytes;}need(total===21315014,'whole input byte total');
 need(read(AUD+'/run04/executed_checker.py').equals(read(AUD+'/inspect_cold1.py')),'exact current executed source');eq(pin(read(AUD+'/inspect_cold1.py')),run.auditor_source,'main source actual pin');
 const inPins=obj(IO+'/INPUT_PINS.json'),bodies={},pins={},headers=[];need(Object.keys(inPins).length===171,'all171 original I/O inputs');
 for(let [n,k]of Object.entries(inPins)){let b=read(ROOT+'/'+n);eq(pin(b),{bytes:k.bytes,sha256:k.sha256},'whole independent171 byte key');pins[n]=k;if(!n.endsWith('.png')&&!n.endsWith('.pdf'))bodies[n]=b.toString();}
 for(let i=193;i<=198;i++){const h=obj(IO+'/native/read'+i+'.json');need(h.result.exit_code===0&&!Object.hasOwn(h.result,'session_id'),'actual header native exit');eq(h.request.cmd,'od -An -tx1 -N32 '+h.path,'exact header argv');const bytes=Buffer.from(h.result.output.trim().split(/\s+/).map(x=>parseInt(x,16)));need(bytes.equals(read(ROOT+'/'+h.path).subarray(0,32)),'all32 actual header bytes');headers.push(h);}
 const inventory=files(INNER).map(p=>path.relative(ROOT,p)),data={bodies,pins,inventory,headers};
 // Only the fully read, pinned pure independent function is evaluated, without fs/require/process.
 const pureSource=read(IO+'/RECONSTRUCTION.js').toString();
 const reconstructed=vm.runInNewContext(pureSource+'\nreconstructIO(data);',{data},{timeout:20000});
 const reconstructedRaw=Buffer.from(JSON.stringify(reconstructed,null,2)+'\n'),oldRaw=read(IO+'/RECONSTRUCTION_RESULT.json');
 need(reconstructedRaw.equals(oldRaw),'entire pure-metadata output raw equality, not normalized subset');
 need(reconstructed.checks===5132&&reconstructed.failures.length===0&&reconstructed.total_fls_events===2382,'all5132 checks/2382 events');
 eq(JSON.parse(JSON.stringify(reconstructed.reconstructed_roles)),obj(AUD+'/run04/INDEPENDENT_ORDERED_IO_RECONSTRUCTION.json'),'all four independent full role objects');
 const census=obj(IO+'/ALL_LOG_DIAGNOSTIC_CENSUS.json');eq(Object.keys(census),['schema','paths','census'],'entire census schema');need(census.paths===18&&census.census.length===18,'all18 diagnostic inputs');
 const selected=inventory.filter(n=>/\/(?:source_only|pass_artifacts_[^/]+\/(?:before|after))\/main\.(?:log|blg)$/.test(n)||/\/commands\/(?:pass[123]|bibtex)\/stdout\.raw$/.test(n)).sort();
 eq(census.census.map(r=>r.path),selected,'complete all selected log/blg/pass stdout membership');
 const patterns={warning:/warning/i,undefined:/undefined/i,missing_character:/missing character|character .*missing/i,overfull:/overfull/i,underfull:/underfull/i,rerun:/rerun/i,error_or_fatal:/error|fatal/i},rebuilt=[];
 for(let row of census.census){let b=read(ROOT+'/'+row.path),ls=b.toString().split('\n');if(ls.at(-1)==='')ls.pop();let counts=Object.fromEntries(Object.keys(patterns).map(k=>[k,0])),matching=[];
 for(let i=0;i<ls.length;i++){const text=ls[i],categories=Object.keys(patterns).filter(k=>patterns[k].test(text));if(!categories.length)continue;for(let k of categories)counts[k]++;
 let classification='OTHER_LITERAL_MATCH_REQUIRES_CONTEXT';
 if(/^pdfTeX\s+warning\b/i.test(text))classification='ACTUAL_ENGINE_WARNING';
 else if(/^(?:LaTeX|Package\s+\S+|Class\s+\S+)\s+Warning\b/i.test(text))classification='ACTUAL_LATEX_OR_PACKAGE_WARNING';
 else if(/^Missing character\b/i.test(text))classification='ACTUAL_TEX_MISSING_CHARACTER_DIAGNOSTIC';
 else if(/^Package microtype Info: Character .* is missing$/.test(text))classification='MICROTYPE_INFORMATIONAL_PROTRUSION_CONTEXT_NOT_TEX_MISSING_CHARACTER';
 else if(/^Underfull\b/i.test(text))classification='ACTUAL_UNDERFULL_DIAGNOSTIC';
 else if(/^Overfull\b/i.test(text))classification='ACTUAL_OVERFULL_DIAGNOSTIC';
 else if(/^Package:| Info:|rerunfilecheck|file:line:error/.test(text))classification='LOADER_METADATA_OR_INFORMATIONAL_LITERAL_NOT_WARNING_EMISSION';
 matching.push({line:i+1,text,categories,classification,context_first_line:Math.max(0,i-2)+1,context:ls.slice(Math.max(0,i-2),Math.min(ls.length,i+3))});}
 let expected={path:row.path,pin:{sha256:pin(b).sha256,bytes:b.length},line_count:ls.length,matching_lines:matching,counts,actual_engine_warnings:matching.filter(x=>x.classification==='ACTUAL_ENGINE_WARNING'),actual_tex_missing_character_diagnostics:matching.filter(x=>x.classification==='ACTUAL_TEX_MISSING_CHARACTER_DIAGNOSTIC'),scope:'Case-insensitive literal census plus exact contexts; loader/Info matches are not reclassified as warning emissions. No benignness or glyph-loss inference.'};
 eq(expected,row,'complete independently reconstructed diagnostic row '+row.path);rebuilt.push(expected);}
 const final=rebuilt.find(x=>x.path.endsWith('/source_only/main.log'));need(final.actual_engine_warnings.length===1&&final.actual_engine_warnings[0].line===608&&final.actual_tex_missing_character_diagnostics.length===0&&final.counts.undefined===0&&final.counts.overfull===0&&final.counts.underfull===2,'actual final diagnostic counts');
 const censusPin=pin(read(IO+'/ALL_LOG_DIAGNOSTIC_CENSUS.json'));
 const names=Object.keys(inputs);for(let p of names)read(p);need(Object.keys(inputs).length===names.length,'all final inputs close');
 console.log(JSON.stringify({status:'PASS_COMPLETE_COLD1_PACKAGE_IO_AND_DIAGNOSTIC_RECONSTRUCTION_D1_STILL_OPEN',checks,inputs_count:names.length,outer_seal:outer,main_inputs:474,main_documentary_checks_received:177773,pure_io_original_inputs:171,pure_io_checks:5132,pure_io_entire_raw_output:pin(oldRaw),pure_io_raw_equal:true,all_ordered_fls_events:2382,diagnostic_input_files:18,complete_census_received:censusPin,final_actual_warning:final.actual_engine_warnings[0],inputs,stat_fields:F,new_science:0,new_builds:0,new_views:0,host_observations:0,main_python_auditor_reexecuted:false,cold_artifact_acceptance:false,diagnostic_finding:'OPEN_PENDING_ROOT_DIAGNOSTIC_DISPOSITION',external:'OWNER_AMBER / HOLD_EXTERNAL'}));
}
try{main()}catch(e){console.error(e.stack);process.exitCode=1}
