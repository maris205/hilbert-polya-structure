'use strict';
// Root documentary reconstruction only. The pure I/O function is an explicitly
// disclosed derivative of the received cold1 independent lane; all cold2 bytes
// are read afresh. No Python, submitted adapter, host lookup, build or page view.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),util=require('util'),vm=require('vm');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa';
const OWN=QA+'/p211_terminal_cold_artifact_root02',AUD=QA+'/p211_terminal_cold_artifact_audit02',RUN=AUD+'/run01';
const IO1=QA+'/p211_terminal_cold_artifact_audit01/io_lane';
const INNER=ROOT+'/papers/211-kernel-image-projection-feedback/qa_final/cold_build_2/inner';
const F=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];let checks=0;const inputs={};
function need(x,m){checks++;if(!x)throw Error(m)}
function plain(x){return JSON.parse(JSON.stringify(x))}function eq(a,b,m){need(util.isDeepStrictEqual(a,b),m)}
function pin(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')}}
function read(p){need(p.startsWith(ROOT+'/')&&path.normalize(p)===p,'normalized workspace path');let q=ROOT;for(let n of path.relative(ROOT,p).split('/')){q+='/'+n;need(!fs.lstatSync(q).isSymbolicLink(),'no path alias');}let s=fs.statSync(p,{bigint:true}),l=fs.lstatSync(p,{bigint:true});need(s.isFile()&&l.isFile()&&l.nlink===1n&&fs.realpathSync(p)===p,'ordinary file');let b=fs.readFileSync(p),v={...pin(b),stat:F.map(k=>s[k].toString()),lstat:F.map(k=>l[k].toString())};eq(F.map(k=>fs.statSync(p,{bigint:true})[k].toString()),v.stat,'stable stat');eq(F.map(k=>fs.lstatSync(p,{bigint:true})[k].toString()),v.lstat,'stable lstat');need(BigInt(b.length)===s.size,'whole read');if(inputs[p])eq(v,inputs[p],'stable repeat');inputs[p]=v;return b;}
function obj(p){return JSON.parse(read(p))}
function files(base){let out=[];for(let n of fs.readdirSync(base).sort()){let p=base+'/'+n,s=fs.lstatSync(p);need(!s.isSymbolicLink(),'tree no alias');if(s.isDirectory())out.push(...files(p));else{need(s.isFile(),'regular member');out.push(p);}}return out;}
function seal(base,count){const b=read(base+'/SHA256SUMS'),names=[];for(let line of b.toString().trimEnd().split('\n')){let m=/^([a-f0-9]{64})  (.+)$/.exec(line);need(!!m&&!path.isAbsolute(m[2])&&!m[2].split('/').some(n=>['','..','.'].includes(n))&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'unique nonself payload');names.push(m[2]);eq(pin(read(base+'/'+m[2])).sha256,m[1],'whole payload');}need(names.length===count,'exact payload count');eq(names,[...names].sort(),'sorted seal');eq(files(base),[...names,'SHA256SUMS'].map(n=>base+'/'+n).sort(),'complete tree');return pin(b);}
function main(){
 const outputDir=OWN+'/io_run03';need(!fs.existsSync(outputDir),'exclusive documentary output directory absent');
 read(OWN+'/io_and_census.js');const outer=seal(AUD,31);eq(outer,{bytes:2892,sha256:'415922d930f963acff38c5c600733deebcbc7702ef82fac1080e8485511b6e83'},'exact cold2 capture seal');
 eq(seal(RUN,11),{bytes:984,sha256:'7530082a3c055fef4a36ce042166fa452031d0d60366df0a6b01ac08559eb294'},'exact run seal');
 const r=obj(RUN+'/RESULT.json'),beforeRaw=read(RUN+'/READ_INPUTS_BEFORE.json');need(beforeRaw.equals(read(RUN+'/READ_INPUTS_AFTER.json')),'entire490 raw before/after');const key=JSON.parse(beforeRaw);
 need(r.checks===178308&&r.read_paths===490&&r.read_bytes===25395690&&r.failure===null&&r.inputs_equal&&r.open_findings===1&&!r.build_acceptance&&!r.terminal_acceptance,'actual documentary outcome');
 need(Object.keys(key).length===490,'490 actual byte keys');let total=0;for(const [p,k]of Object.entries(key)){eq(pin(read(p)),k,'all490 full current inputs');total+=k.bytes;}need(total===r.read_bytes,'whole byte total');
 const roleInventory=obj(IO1+'/INPUT_PINS.json'),names1=Object.keys(roleInventory);need(names1.length===171,'171 original declared roles');
 const unchangedDocuments=['.agents/skills/symbolic-dynamics-research/SKILL.md','docs/papers204_208_sequence/ARTIFACT_CONTRACT.md','docs/papers211_215_sequence/PROBLEM_ANCHOR.md','docs/research_state/WORKFLOW.md'];
 const names=names1.map(n=>n.replace('/cold_build_1/','/cold_build_2/')),bodies={},pins={};need(new Set(names).size===171,'171 distinct cold2 roles');
 eq(names.filter(n=>!Object.hasOwn(key,ROOT+'/'+n)),unchangedDocuments,'exact four non-build instruction inputs outside490');
 for(const n of names){const b=read(ROOT+'/'+n);pins[n]=pin(b);if(unchangedDocuments.includes(n))eq(pins[n],roleInventory[n],'four unchanged instruction bytes');else eq(pins[n],key[ROOT+'/'+n],'all167 fresh cold2/documentary role bytes in490');if(!n.endsWith('.png')&&!n.endsWith('.pdf'))bodies[n]=b.toString();}
 const headers=obj(OWN+'/HEADERS_NATIVE.json');need(headers.length===6,'six actual headers');for(const h of headers){need(h.result.exit_code===0&&!Object.hasOwn(h.result,'session_id'),'header native finished');eq(h.request.cmd,'od -An -tx1 -N32 '+h.path,'header exact request');const b=Buffer.from(h.result.output.trim().split(/\s+/).map(x=>parseInt(x,16)));need(b.length===32&&b.equals(read(ROOT+'/'+h.path).subarray(0,32)),'all32 header bytes');}
 const source=read(OWN+'/RECONSTRUCTION.js').toString(),oldSource=read(IO1+'/RECONSTRUCTION.js').toString();
 eq(source,oldSource.replaceAll('cold_build_1','cold_build_2').replaceAll('P211-COLD1-IO-D1','P211-COLD2-DIAGNOSTIC-CENSUS'),'exact disclosed two-literal pure-source derivative');
 const inventory=files(INNER).map(p=>path.relative(ROOT,p)),data={bodies,pins,inventory,headers};
 const reconstructed=plain(vm.runInNewContext(source+'\nreconstructIO(data);',{data},{timeout:20000}));
 need(reconstructed.checks===5132&&reconstructed.failures.length===0&&reconstructed.total_fls_events===2382,'5132 pure IO checks /2382 ordered events');
 eq(reconstructed.reconstructed_roles,obj(RUN+'/INDEPENDENT_ORDERED_IO_RECONSTRUCTION.json'),'all four complete independent role objects');
 // Independently implement the accepted full case-insensitive/context contract
 // on every current cold2 log, then compare the ENTIRE emitted census product.
 const product=obj(RUN+'/FULL_LOG_DIAGNOSTIC_CENSUS.json');
 const roles=inventory.filter(n=>/\/(?:source_only|pass_artifacts_[^/]+\/(?:before|after))\/main\.(?:log|blg)$/.test(n)||/\/commands\/(?:pass[123]|bibtex)\/stdout\.raw$/.test(n)).map(n=>n.slice(path.relative(ROOT,INNER).length+1)).sort();
 need(roles.length===18,'complete eighteen diagnostic role membership');eq(product.role_names,roles,'all role names');
 const specs=[['warning','\\bwarning\\b'],['undefined','undefined'],['missing_character','missing\\s+character|character.*missing'],['overfull','overfull'],['underfull','underfull'],['rerun','rerun'],['error_or_fatal','\\berror\\b|\\bfatal\\b|emergency stop|^!']];
 const patterns=specs.map(([k,s])=>[k,new RegExp(s,'i')]);const emissions=['ACTUAL_ENGINE_WARNING','ACTUAL_LATEX_PACKAGE_OR_CLASS_WARNING','ACTUAL_BIBTEX_WARNING'];const census=[],logPins={};
 for(const role of roles){const p=INNER+'/'+role,b=read(p),t=b.toString();need(Buffer.from(t).equals(b),'strict round-trip UTF8 log');const ls=t.split('\n');if(ls.at(-1)==='')ls.pop();const matches=[];logPins[p]=pin(b);
  for(let i=0;i<ls.length;i++){const text=ls[i],categories=patterns.filter(([k,rx])=>rx.test(text)).map(([k])=>k);if(!categories.length)continue;let classification='OTHER_LITERAL_MATCH_REQUIRES_CONTEXT';
   if(/^(?:pdftex|xetex|luatex|luahbtex)\s+warning\b/i.test(text))classification='ACTUAL_ENGINE_WARNING';
   else if(/^(?:latex(?:\s+font)?|package\s+\S+|class\s+\S+)\s+warning\b/i.test(text))classification='ACTUAL_LATEX_PACKAGE_OR_CLASS_WARNING';
   else if(/^warning--/i.test(text))classification='ACTUAL_BIBTEX_WARNING';
   else if(/^warning\$ -- [0-9]+$/i.test(text))classification='BIBTEX_FUNCTION_CALL_COUNTER_NOT_WARNING_EMISSION';
   else if(/^underfull\b/i.test(text))classification='ACTUAL_UNDERFULL_DIAGNOSTIC';
   else if(/^overfull\b/i.test(text))classification='ACTUAL_OVERFULL_DIAGNOSTIC';
   else if(/^missing\s+character\b/i.test(text))classification='ACTUAL_TEX_MISSING_CHARACTER_DIAGNOSTIC';
   else if(/^(?:!|emergency stop|fatal error)/i.test(text))classification='ACTUAL_ERROR_OR_FATAL_DIAGNOSTIC';
   else if(/^\(rerunfilecheck\)\s+rerun\b/i.test(text))classification='ACTUAL_RERUN_REQUEST_CONTINUATION';
   else if(/^package microtype info: character .* is missing$/i.test(text))classification='MICROTYPE_INFO_PROTRUSION_CONTEXT_NOT_TEX_MISSING_CHARACTER';
   else if(/^(?:Package:|File:|[(/]| file:line:error|Package rerunfilecheck Info:|Package uniquecounter Info:)/.test(text)||text.includes('Providing info/warning/error'))classification='LOADER_METADATA_OR_INFORMATIONAL_LITERAL_NOT_WARNING_EMISSION';
   const first=Math.max(0,i-2),end=Math.min(ls.length,i+3);matches.push({line:i+1,text,categories,classification,context_first_line:first+1,context_last_line:end,context:ls.slice(first,end)});
  }
  census.push({relative_role:role,path:p,pin:pin(b),line_count:ls.length,trailing_lf:t.endsWith('\n'),matching_lines:matches,literal_match_counts:Object.fromEntries(patterns.map(([k])=>[k,matches.filter(m=>m.categories.includes(k)).length])),actual_engine_warnings:matches.filter(m=>m.classification==='ACTUAL_ENGINE_WARNING'),actual_warning_emission_count:matches.filter(m=>emissions.includes(m.classification)).length,actual_tex_missing_character_diagnostic_count:matches.filter(m=>m.classification==='ACTUAL_TEX_MISSING_CHARACTER_DIAGNOSTIC').length,unclassified_matches:matches.filter(m=>m.classification==='OTHER_LITERAL_MATCH_REQUIRES_CONTEXT'),interpretation_limit:'Literal census/categories are not harmlessness, glyph loss, whole-build validity, diagnostic disposition or acceptance.'});
 }
 const final=census.find(r=>r.relative_role==='source_only/main.log'),measurementPath=INNER+'/MEASURED_NOT_VIEWED.json',measurement=obj(measurementPath),measurementPin=pin(read(measurementPath)),recorded=measurement.diagnostics.warnings;
 need(Array.isArray(recorded)&&recorded.every(s=>typeof s==='string'),'recorded warnings strings');const emitted=final.matching_lines.filter(m=>emissions.includes(m.classification)),remaining=[...recorded],only=[];
 for(const row of emitted){const i=remaining.indexOf(row.text);if(i<0)only.push(row);else remaining.splice(i,1);}
 const comparison={measurement_path:measurementPath,measurement_pin:measurementPin,recorded_warning_lines:recorded,actual_final_warning_emissions:emitted,emitted_not_recorded:only,recorded_not_emitted:remaining,matching_method:'exact text multiset, preserving duplicates',diagnostic_disposition:'PENDING_ROOT'};
 const finding=only.length||remaining.length?{id:'P211-COLD2-DIAGNOSTIC-CENSUS',severity:'Minor',status:'OPEN_PENDING_ROOT_DIAGNOSTIC_DISPOSITION',scope:'actual emitted-versus-recorded warning census',final_log:{path:final.path,pin:final.pin},measurement:{path:measurementPath,pin:measurementPin},emitted_not_recorded:only,recorded_not_emitted:remaining,inference_limits:['Not a claim of harmlessness or glyph loss.','Does not close other artifact findings or grant acceptance.','No source/log/measurement repair or rebuild is authorized.'],required_next_gate:'Preserve originals and obtain an immutable supplemental root diagnostic disposition under the full artifact gate.'}:null;
 const rebuilt={schema:'p211-cold2-full-log-diagnostic-census-v1',status:'CENSUS_RECORDED_PENDING_ROOT_DIAGNOSTIC_DISPOSITION',case_insensitive_patterns:specs.map(([category,pattern])=>({category,pattern,flags:'I'})),context_radius:2,role_names:roles,raw_log_pins_before:logPins,raw_log_pins_after:logPins,census,recorded_warning_comparison:comparison,finding,uses_prepared_census_as_evidence:false,terminal_acceptance:false,diagnostic_disposition:'PENDING_ROOT',visual_review_by_this_function:false};
 eq(rebuilt,product,'ENTIRE eighteen-log census, patterns, pins, contexts, multisets and finding');eq(obj(RUN+'/FINDINGS.json'),[finding],'complete actual finding array');
 const metadata='LOADER_METADATA_OR_INFORMATIONAL_LITERAL_NOT_WARNING_EMISSION',protrusion='MICROTYPE_INFO_PROTRUSION_CONTEXT_NOT_TEX_MISSING_CHARACTER';
 const hard=final.matching_lines.filter(r=>r.categories.some(c=>['undefined','overfull','rerun','error_or_fatal'].includes(c))&&r.classification!==metadata),missing=final.matching_lines.filter(r=>r.categories.includes('missing_character')&&r.classification!==protrusion),underfull=final.matching_lines.filter(r=>r.classification==='ACTUAL_UNDERFULL_DIAGNOSTIC');
 eq(hard,[],'no final actual hard diagnostics');eq(missing,[],'no final actual missing-character diagnostics');need(underfull.length===2&&emitted.length===1&&emitted[0].line===608,'actual final 2 underfull /1 warning');
 const consumed=Object.keys(inputs);for(const p of consumed)read(p);need(Object.keys(inputs).length===consumed.length,'all rich inputs fully closed');
 const output={status:'PASS_COMPLETE_COLD2_IO_AND_CENSUS_RECONSTRUCTION_D1_STILL_OPEN',checks,input_count:consumed.length,stat_fields:F,inputs,capture_seal:outer,actual_python_checks_received:178308,actual_python_inputs:490,actual_python_input_bytes:25395690,pure_io_input_roles:171,pure_io_checks:5132,pure_io_events:2382,pure_io_source_derivation:'Explicit cold1 pure metadata function; two literal substitutions only; all cold2 bytes/keys newly read; no old result compared or reused.',pure_io_full_product:reconstructed,full_independent_census:rebuilt,hard_final_diagnostics:hard,missing_final_diagnostics:missing,underfull_final:underfull,main_python_auditor_executions:0,new_science:0,new_builds:0,new_views:0,new_host_queries:0,cold_artifact_acceptance:false,diagnostic_disposition:'PENDING_ROOT',external:'OWNER_AMBER / HOLD_EXTERNAL'};
 // Generated audit artifacts use exclusive creation; stdout only carries pins.
 const outputBytes=Buffer.from(JSON.stringify(output)+'\n'),sourceBytes=read(OWN+'/io_and_census.js');
 fs.mkdirSync(outputDir,{mode:0o700});fs.writeFileSync(outputDir+'/RESULT.json',outputBytes,{flag:'wx'});fs.writeFileSync(outputDir+'/executed_checker.js',sourceBytes,{flag:'wx'});
 const manifest=Buffer.from(pin(outputBytes).sha256+'  RESULT.json\n'+pin(sourceBytes).sha256+'  executed_checker.js\n');fs.writeFileSync(outputDir+'/SHA256SUMS',manifest,{flag:'wx'});
 console.log(JSON.stringify({status:output.status,checks:output.checks,input_count:output.input_count,pure_io_checks:5132,pure_io_events:2382,output:outputDir+'/RESULT.json',result_pin:pin(outputBytes),source_pin:pin(sourceBytes),manifest_pin:pin(manifest),payloads:2,diagnostic_disposition:'PENDING_ROOT'}));
}
try{main()}catch(e){console.error(e.stack);process.exitCode=1;}
