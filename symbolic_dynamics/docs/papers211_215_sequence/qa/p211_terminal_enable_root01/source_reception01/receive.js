// Root workspace-only source receiver. Transparent derivation from completely read successful preparation metadata, with full original native projections and rich stat keys added.
// No Python/AST/import/eval/compile, host referent, child process or file writes.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert/strict');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa',HERE=QA+'/p211_terminal_enable_preparation01';
let checks=0;const reads={};function check(v,m){checks++;assert(v,m);}
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
const RICH={},FIELDS=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];const meta=s=>FIELDS.map(k=>String(s[k]));
function read(p){check(p.startsWith(ROOT+'/')&&!p.slice(ROOT.length+1).split('/').some(x=>!x||x==='.'||x==='..'),'workspace-only metadata');let prefix=ROOT;for(const part of p.slice(ROOT.length+1).split('/')){prefix+='/'+part;check(!fs.lstatSync(prefix).isSymbolicLink(),'no workspace ancestor alias');}const s=fs.lstatSync(p,{bigint:true});check(s.isFile()&&!s.isSymbolicLink()&&fs.realpathSync(p)===p,'ordinary workspace file');const b=fs.readFileSync(p);const v=pin(b),m=meta(s);eq(meta(fs.lstatSync(p,{bigint:true})),m,'stable full integer read');if(reads[p]){eq(reads[p],v,'repeat bytes');eq(RICH[p],m,'repeat full metadata');}reads[p]=v;RICH[p]=m;return b;}
const obj=p=>JSON.parse(read(p));const eq=(a,b,m)=>{checks++;assert.deepStrictEqual(a,b,m);};
const plan=obj(HERE+'/INPUT_PLAN.json'),host=obj(HERE+'/HOST_SCOPE.json'),source=read(HERE+'/terminal_control.py').toString();
check(Object.keys(plan.workspace_input_pins).length===272,'all272 prep inputs');for(const[p,v]of Object.entries(plan.workspace_input_pins))eq(pin(read(p)),v,p);
function tree(base){const files=[],dirs=[];function walk(d){for(const n of fs.readdirSync(d)){const p=d+'/'+n,s=fs.lstatSync(p);check(!s.isSymbolicLink(),'no package alias');if(s.isDirectory()){dirs.push(path.relative(base,p));walk(p);}else{check(s.isFile()&&s.nlink===1,'ordinary single-link file');files.push(path.relative(base,p));}}}walk(base);return {files:files.sort(),directories:dirs.sort()};}
for(const[p,t]of Object.entries(plan.exact_input_package_trees))eq(tree(p),t,'entire input tree');
const old=obj(plan.dependency_references.original_lock.path),key=obj(plan.dependency_references.prior_read_key.path),config=obj(plan.dependency_references.prior_configuration_key.path),mapping=obj(plan.dependency_references.historical_mapping.path);
const physical={},substitutions={};for(const[p,v]of Object.entries(key)){const m=mapping.find(x=>x.logical_path===p);if(m){eq(m.pin,v,'mapping full pin');substitutions[p]=m.physical_original;}physical[m?.physical_original||p]=v;}
eq(substitutions,plan.exact_historical_substitutions,'exact two mappings');
let workspaceOld=0;for(const[p,v]of Object.entries(physical))if(p.startsWith(ROOT+'/')){eq(pin(read(p)),v,'all old workspace key bytes');workspaceOld++;}
check(workspaceOld===503&&Object.keys(physical).length===1299,'503workspace+796unprobedhost old key');
const aliases=[...new Set([...Object.keys(old.selector_specs),...Object.keys(config),...Object.keys(physical),...Object.values(old.entries).filter(v=>v.kind==='file').map(v=>v.resolved)])].filter(p=>!p.startsWith(ROOT+'/')).sort();
eq(aliases,host.paths,'all841 prior-only host strings');check(host.entries===aliases.length&&aliases.length===841,'host count');
check(Object.keys(old).length===15&&Object.keys(old.entries).length===840&&Object.keys(config).length===843,'old scope');
eq(Object.keys(old.selector_specs).sort(),Object.keys(old.entries).sort(),'all old selectors');eq(Object.keys(old.selection_reasons).sort(),Object.keys(old.entries).sort(),'all reasons');
check(Object.keys(old.queries).length===16&&Object.keys(old.query_commands).length===16&&old.ldd_elf_inputs.length===33,'query/elf data scope');
eq(old.ldd_elf_inputs,plan.runtime_and_parameters.ldd_elf_inputs,'exact ELF list');
eq(Object.fromEntries(Object.entries(old.queries).filter(([k,v])=>typeof v==='string')),plan.runtime_and_parameters.effective_scalar_queries,'all13 scalar query data');
for(const b of Object.values(plan.builds)){const disabled=obj(b.disabled_binding.path),candidate=obj(b.candidate_lock.path);
const expected={...old,schema:'p211-terminal-bounded-dependency-lock-v1',status:'ROOT_BOUND_EXACT_INHERITED_HOST_KEY_NEW_ADAPTER_ONLY',code_observations:plan.new_adapter_pins,terminal_derivation:{original_lock:plan.dependency_references.original_lock,allowed_changes:['schema','status','code_observations','terminal_derivation'],host_candidate_extension:false}};
eq(candidate,expected,'entire candidate derivation');eq(pin(read(b.candidate_lock.path)),b.candidate_lock.pin,'candidate wholebytes');
check(disabled.enabled===false&&disabled.cwd_relative_configuration===null&&disabled.root_authorization.issuer===null&&disabled.root_authorization.decision===null&&disabled.root_authorization.record===null,'disabled no authority');
eq(disabled.source_pins,plan.source_pins,'all nine sourcepins');eq(disabled.adapter_pins,plan.new_adapter_pins,'fresh adapters');eq(disabled.original_adapter_pins,plan.original_adapter_pins,'old adapters');
check(b.cwd_relative_paths.length===3&&b.cwd_relative_observations===null,'only future cwd roles; no probes');
const r2=disabled.round2_package;check(Object.keys(r2.all_file_pins).length===124&&r2.payload_count===123&&r2.total_file_count===124,'full R2 package');
const names=Object.keys(r2.all_file_pins).sort();eq(tree(r2.root).files,names,'whole R2 file set');
for(const[n,v]of Object.entries(r2.all_file_pins))eq(pin(read(r2.root+'/'+n)),v,'entire R2 bytepins');
eq(read(r2.root+'/SHA256SUMS').toString(),names.filter(n=>n!=='SHA256SUMS').map(n=>r2.all_file_pins[n].sha256+'  '+n+'\n').join(''),'whole R2 seal');}
function manifest(base,count){const b=read(base+'/SHA256SUMS'),names=[];for(const line of b.toString().trimEnd().split('\n')){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);check(m!==null,'manifest syntax');check(m[2]!=='SHA256SUMS'&&!path.isAbsolute(m[2])&&!m[2].split('/').some(p=>p==='.'||p==='..'||p===''),'manifest safe');eq(pin(read(base+'/'+m[2])).sha256,m[1],'whole original payload hash');names.push(m[2]);}check(names.length===count,'manifest payloadcount');eq(tree(base).files,[...names,'SHA256SUMS'].sort(),'whole payload membership');eq(b.toString(),names.slice().sort().map(n=>reads[base+'/'+n].sha256+'  '+n+'\n').join(''),'whole sorted manifest');return pin(b);}
const oldNative=obj(plan.dependency_references.historical_comparator_native.path),oldRaw=Buffer.from(oldNative.result.output),baseline=JSON.parse(oldRaw);
eq(pin(oldRaw),plan.prior_comparator_whole_stdout,'whole actual6223 stdout');check(oldNative.result.exit_code===0&&!('session_id'in oldNative.result),'actual native completion');
eq(Object.keys(baseline).sort(),plan.prior_comparator_complete_fields,'whole old outputfieldlist');
eq(manifest(QA+'/p211_initial_build_01',362),baseline.manifests.build,'whole old build');
eq(manifest(QA+'/p211_initial_build_independent_reception',18),baseline.manifests.initial_build_audit,'whole old audit');
eq(manifest(ROOT+'/papers/211-kernel-image-projection-feedback/frozen_round0',32),baseline.manifests.freeze,'whole old freeze');
eq(manifest(QA+'/p211_round2_original_root01',25),plan.whole_round2_original_gate_seal.pin,'whole rootR2 gate');
check(source.endsWith('\n')&&!source.includes('\r')&&!source.includes('\t'),'source canonical line endings/no tabs');
check((source.match(/subprocess\.Popen\(/g)||[]).length===1,'one native launch implementation');
check(!/\b(?:eval|exec|compile)\(/.test(source),'no helper source evaluation/AST');
check((source.match(/native\('terminal_outer'/g)||[]).length===1,'only one builder call site');
for(const text of ["len(key)==1299 and len(configuration)==843","len(selected)==840","len(old_current)==843","len(old['queries'])==len(old['query_commands'])==16","len(old['ldd_elf_inputs'])==33","scope['entries']==len(host)==841","sealed_input(HERE,grant['preparation_seal']['pin'],9)","if phase=='enable':","if phase=='capture':","need(READS==prior","NO_NATIVE_HANDLE_UNKNOWN_LAUNCH","UN C L O S E D".replaceAll(' ',''),"FAIL_PRESERVED_NO_RETRY_NO_IMPLICIT_ENABLE_OR_ACCEPTANCE"])check(source.includes(text),'source literal '+text);
const imports=source.split('\n').filter(s=>/^(?:import |from )/.test(s));eq(imports,['import hashlib','import json','import locale','import os','from pathlib import Path','import re','import signal','import stat','import subprocess','import sys','import time','import traceback'],'exact declared controller imports');
const pureModules=imports.map(s=>s.startsWith('from ')?s.split(' ')[1]:s.split(' ')[1]).filter(s=>!['sys','time','signal'].includes(s));for(const n of pureModules){const paths=['/usr/lib/python3.10/'+n+'.py','/usr/lib/python3.10/'+n+'/__init__.py'];check(paths.some(p=>Object.hasOwn(old.entries,p)),'already-pinned import source string '+n);}
for(const[p,v]of Object.entries(reads))eq(pin(fs.readFileSync(p)),v,'all metadata originalbytes close');

const beforeNames=['HOST_SCOPE.json','INPUT_PLAN.json','NATIVE_READS.json','PHASE_TEMPLATES.disabled.json','PLAN.md','SOURCE_DERIVATION.diff','SOURCE_DERIVATION_NATIVE.json','terminal_control.py'].sort();
eq(tree(HERE),{files:[...beforeNames,'PREPARATION_NATIVE.json','SHA256SUMS'].sort(),directories:[]},'all ten sealed original source-package files');
const diff=read(HERE+'/SOURCE_DERIVATION.diff').toString(),dNative=obj(HERE+'/SOURCE_DERIVATION_NATIVE.json');
eq(diff,dNative.result.output,'full actual native diff output');check(dNative.result.exit_code===1&&!('session_id'in dNative.result),'actual completed native difference');
const original=read(QA+'/p211_initial_build_binding01/prepare_binding.py').toString(),diffLines=diff.trimEnd().split('\n');
eq(diffLines.slice(0,2),['--- accepted_initial_prepare_binding.py','+++ terminal_control.py'],'literal diff labels');
let originalCursor=0,rebuilt=[];for(let i=2;i<diffLines.length;){const h=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@$/.exec(diffLines[i++]);check(h!==null,'whole diff hunk header');const start=Number(h[1])-1,oldCount=Number(h[2]??1),newCount=Number(h[4]??1);const oldLines=original.trimEnd().split('\n');rebuilt.push(...oldLines.slice(originalCursor,start));originalCursor=start;let consumed=0,produced=0;while(i<diffLines.length&&!diffLines[i].startsWith('@@ ')){const row=diffLines[i++],tag=row[0],body=row.slice(1);check([' ','+','-'].includes(tag),'every full diff line prefix');if(tag!=='+' ){eq(oldLines[originalCursor++],body,'exact original diff line');consumed++;}if(tag!=='-'){rebuilt.push(body);produced++;}}check(consumed===oldCount&&produced===newCount,'whole hunk cardinality');}rebuilt.push(...original.trimEnd().split('\n').slice(originalCursor));eq(rebuilt.join('\n')+'\n',source,'complete source reconstructed from actual original/diff');
const templates=obj(HERE+'/PHASE_TEMPLATES.disabled.json');check(templates.templates.length===6&&templates.decisions_issued===0&&templates.issuer===null,'all six disabled templates');
const grantKeys=['schema','issuer','phase','build_number','decision','controller','preparation_seal','input_plan','phase_output','cold_output','controller_environment','build_environment','cwd','required_receipts','new_science','new_page_views','terminal_acceptance','external'].sort();
for(const row of templates.templates){const b=plan.builds[row.build_number],g=row.grant_with_nulls_not_accepted;
eq(Object.keys(g).sort(),grantKeys,'entire planned authority field set');check(row.disabled===true&&g.issuer===null&&g.decision===null&&g.preparation_seal.pin===null,'never an actual authority');
eq(g.controller,{path:HERE+'/terminal_control.py',pin:pin(Buffer.from(source))},'actual source pin in every template');eq(g.input_plan,{path:HERE+'/INPUT_PLAN.json',pin:pin(read(HERE+'/INPUT_PLAN.json'))},'actual plan pin');
eq(g.phase_output,b.phase_outputs[row.phase],'exact phase role');eq(g.cold_output,b.cold_output,'exact cold role');
eq(row.authority_path,b.authority_paths[row.phase],'exact root authority role');
eq(row.required_cli_argv.slice(0,7),[...plan.runtime_and_parameters.controller_argv_prefix,'pycache_prefix='+g.phase_output+'/unused_controller_cache',HERE+'/terminal_control.py'],'whole runtime launch prefix');
eq(row.required_cli_argv.slice(7,10),[row.phase,String(row.build_number),row.authority_path],'whole phase/build/authority argv');
const expectedRoles=[...Object.keys(plan.gate_references),'controller_source_reception',...(row.phase!=='refresh'?['current_key_reception','refresh_result','refresh_seal']:[]),...(row.phase==='capture'?['enabled_binding_reception','enabled_binding','enable_seal']:[])].sort();
eq(Object.keys(g.required_receipts).sort(),expectedRoles,'every separate root prerequisite');
for(const [role,ref]of Object.entries(plan.gate_references))eq(g.required_receipts[role],ref,'fixed accepted root gate pin');
for(const[role,ref]of Object.entries(g.required_receipts))if(!(role in plan.gate_references))check(ref.pin===null,'future root pin stays null');
eq(g.controller_environment,{PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC'},'ENV4');
eq(g.build_environment,old.environment,'full ENV8');check(g.new_science===0&&g.new_page_views===0&&g.terminal_acceptance===false,'no science/view/acceptance grant');}
const n=obj(HERE+'/NATIVE_READS.json'),rr=n.source_reads;check(rr.length===16,'complete saved selected source-read census');
for(const r of rr)check(r.result.exit_code===0&&!('session_id'in r.result)&&typeof r.result.output==='string','actual complete source-read native return');
eq(rr[0].result.output+rr[1].result.output,read(QA+'/p211_round2_preparation01/terminal_build/build_core.py').toString(),'whole fresh core source read');
eq(rr[2].result.output,['launch_build.py','prepare_build.py','static_checks.py'].map(x=>read(QA+'/p211_round2_preparation01/terminal_build/'+x).toString()).join(''),'whole other three fresh program reads');
eq(rr[3].result.output+rr[4].result.output+rr[5].result.output,read(QA+'/p211_round2_preparation01/terminal_build/build_p211.py').toString(),'whole fresh inner source read');
eq(rr[6].result.output,original,'whole initial controller read');eq(rr[7].result.output,read(plan.dependency_references.accepted_readonly_comparator.path).toString(),'whole unchanged comparator read');
eq(rr[9].result.output+rr[10].result.output,read(QA+'/p211_terminal_binding_preparation01/assemble_disabled.py').toString(),'whole disabled assembler read');
eq(rr[11].result.output,read(QA+'/p211_terminal_binding_source_root01/receive.js').toString(),'whole accepted source receiver read');
eq(rr[12].result.output,read(QA+'/p211_terminal_binding_root01/assemble_capture.js').toString(),'whole root assembly capture source read');
eq(rr[13].result.output+rr[14].result.output,read(QA+'/p211_initial_build_01/outer/executed_adapter/build_core.py').toString(),'whole actual old core source read');
check(n.schema_truncated_native.result.output.includes('tokens truncated'),'real limited schema envelope retained');
check(n.schema_complete_native.result.exit_code===0&&!n.schema_complete_native.result.output.includes('tokens truncated'),'separate complete schema rerun');
check(n.failed_source_assembly.actual_tool_response==='Script failed\nWall time 0.0 seconds\nOutput:\nScript error:\nSyntaxError: Invalid or unexpected token'&&n.failed_source_assembly.request_body_preserved===false,'exact failure text and limit disclosed');
for(const[p,v]of Object.entries(reads))eq(pin(fs.readFileSync(p)),v,'complete final workspace byte endpoints');
const payloads=Object.fromEntries(beforeNames.map(n=>[n,pin(read(HERE+'/'+n))]));
const expectedOriginalSummary={status:'PASS_FINAL_WORKSPACE_ONLY_CONTROLLER_PREPARATION_METADATA',checks:10602,workspace_paths:807,prepared_payload_count:beforeNames.length,final_payload_count_after_this_native:9,expected_sealed_file_count:10,source:pin(Buffer.from(source)),source_lines:source.trimEnd().split('\n').length,complete_diff_bytes:Buffer.byteLength(diff),templates:templates.templates.length,workspace_old_key_files:503,host_strings:841,host_referent_probes:0,Python:false,AST:false,helper_execution:false,builds:0,authorities:0,qa_final_created:false,source_authorship:'documentary adaptation; not independent review',payloads,failed_evidence_preserved:true,terminal_acceptance:false,external:'OWNER_AMBER / HOLD_EXTERNAL'};
const GATE=QA+'/p211_terminal_enable_root01/source_reception01';
const prepared=obj(HERE+'/PREPARATION_NATIVE.json');
eq(prepared.result,expectedOriginalSummary,'whole original10602 metadata result reconstruction');
eq(Buffer.from(prepared.successful_final_metadata02.result.output),Buffer.from(JSON.stringify(expectedOriginalSummary,null,2)+'\n'),'entire actual successful10602 native stdout');
eq(prepared.successful_final_metadata02.result.exit_code,0,'actual preparation success0');
eq(prepared.failed_final_metadata01.result.exit_code,1,'original metadata false-positive retained');
check(prepared.failed_final_metadata01.result.output.includes('actual complete source-read native return'),'actual old failure cause retained');
const prepSeal=manifest(HERE,9);
const inventoryExpected={workspace_inputs:272,workspace_pins:plan.workspace_input_pins,package_trees:plan.exact_input_package_trees,host_scope:host,historical_substitutions:substitutions,source_pins:plan.source_pins,new_adapter_pins:plan.new_adapter_pins,original_adapter_pins:plan.original_adapter_pins};
eq(Buffer.from(n.workspace_input_inventory_native.result.output),Buffer.from(JSON.stringify(inventoryExpected,null,2)+'\n'),'entire122342-byte original inventory native');
const inheritedPlan=obj(QA+'/p211_terminal_binding_preparation01/INPUT_PLAN.json');
const disabledOne=obj(plan.builds['1'].disabled_binding.path);
const schemaExpected={
plan_keys:Object.keys(inheritedPlan),plan_pins:Object.keys(inheritedPlan.input_pins).length,old_fields:Object.keys(old),
selector_count:Object.keys(old.selector_specs).length,selector_entry_kinds:Object.values(old.entries).reduce((a,e)=>(a[e.kind||'absent']=(a[e.kind||'absent']||0)+1,a),{}),
key_paths:Object.keys(key).length,key_workspace:Object.keys(key).filter(p=>p.startsWith(ROOT+'/')).length,key_host:Object.keys(key).filter(p=>!p.startsWith(ROOT+'/')).length,
config_entries:Object.keys(config).length,host_union_aliases:aliases.length,host_resolved_not_selector:Object.values(old.entries).filter(e=>e.kind==='file'&&!(e.resolved in old.selector_specs)).map(e=>e.resolved),
old_cwd_roles:old.cwd_relative_absence_roles,full_mapping:mapping,full_fixed_environment:old.environment,full_queries:old.queries,full_query_commands:old.query_commands,full_elf_list:old.ldd_elf_inputs,
binding_fields:Object.keys(disabledOne),binding_tail:Object.fromEntries(Object.entries(disabledOne).filter(([k])=>!['round2_package','adapter_pins','original_adapter_pins','receipt_references'].includes(k))),
prior_build_native_request:oldNative.request,prior_build_native_fields:Object.keys(oldNative),prior_build_output_pin:pin(oldRaw),prior_build_result:baseline,
full_key_refs:Object.fromEntries(['p211_initial_build_independent_reception/run01/READ_INPUTS_BEFORE.json','p211_initial_build_01/inner/CONFIGURATION_BEFORE.json','p211_initial_build_adoption01/HISTORICAL_MAPPING.json','p211_round2_original_root01/RECEPTION.md','p211_round2_original_root01/SHA256SUMS'].map(p=>[QA+'/'+p,pin(read(QA+'/'+p))]))};
eq(Buffer.from(n.schema_complete_native.result.output),Buffer.from(JSON.stringify(schemaExpected,null,2)+'\n'),'entire76072-byte original schema output');
eq(n.schema_truncated_native.request.cmd,n.schema_complete_native.request.cmd,'actual limited/full schema source identical, budget only changes');
const initialMetadataExpected={status:'PASS_WORKSPACE_ONLY_SOURCE_METADATA_NOT_PYTHON_EXECUTION',checks:8512,workspace_paths:802,original_workspace_key_paths:503,host_referent_probes:0,host_strings:841,source:pin(Buffer.from(source)),source_lines:724,input_plan:pin(read(HERE+'/INPUT_PLAN.json')),host_scope:pin(read(HERE+'/HOST_SCOPE.json')),old_comparator_stdout:pin(oldRaw),imports,source_execution:false,AST:false,builds:0,authorities:0,qa_final_created:false,independent_review:false};
// 'source' above is the actual submitted Python text, not this JS receiver.
eq(Buffer.from(n.workspace_metadata_check01.result.output),Buffer.from(JSON.stringify(initialMetadataExpected,null,2)+'\n'),'whole initial8512 metadata result');
const aliasesProbe=['/usr/bin/python3','/usr/bin/python3.10','/usr/bin/bash','/bin/bash','/usr/lib/python3.10/locale.py','/usr/lib/python3.10/copy.py'];
const aliasRaw=aliasesProbe.map(p=>JSON.stringify({path:p,entry:old.entries[p]??null,read_key:key[p]??null})+'\n').join('')+JSON.stringify({query_keys:Object.keys(old.queries),prior_native_output_fields:Object.keys(baseline)})+'\n';
eq(Buffer.from(n.prior_alias_schema_native.result.output),Buffer.from(aliasRaw),'whole original alias metadata no new host probe');
const sourceRecords=[...rr,...['schema_truncated_native','schema_complete_native','prior_alias_schema_native','workspace_input_inventory_native','tail_schema_native','workspace_metadata_check01'].map(k=>n[k]),dNative,prepared.failed_final_metadata01,prepared.successful_final_metadata02];
for(const r of sourceRecords){
 eq(Object.keys(r.result).sort(),['chunk_id','exit_code','original_token_count','output','wall_time_seconds'],'full native result schema');
 check(typeof r.request.cmd==='string'&&r.request.cmd&&typeof r.result.chunk_id==='string'&&Number.isInteger(r.result.original_token_count)&&r.result.wall_time_seconds>=0,'whole actual envelope');
}
const sourceBindings=[];
for(const r of rr){
 const commands=r.request.cmd.split('\n').filter(Boolean),out=[];
 for(const command of commands){const m=/^sed -n '(\d+),(\d+)p' (\S+)$/.exec(command);check(m,'bounded actual source-read command');const p=m[3].startsWith('/')?m[3]:ROOT+'/'+m[3];const lines=read(p).toString().match(/[^\n]*\n|[^\n]+$/g)||[];out.push(lines.slice(Number(m[1])-1,Number(m[2])).join(''));sourceBindings.push({record_id:r.record_id,path:p,first:Number(m[1]),last:Number(m[2]),whole_file_pin:reads[p]});}
 eq(Buffer.from(out.join('')),Buffer.from(r.result.output),'every entire source-read native body');
}
const tail=n.tail_schema_native,tailNames=['build_p211.py','build_core.py'];const pattern=/SOURCE_ONLY_INITIAL|def seal|TERMINAL_RECEIPT_ROLES|ROOT_AUTHORIZED/;
const expectedTail=tailNames.map(name=>{const p=QA+'/p211_round2_preparation01/terminal_build/'+name;return read(p).toString().split('\n').flatMap((line,i)=>pattern.test(line)?[(p.slice(ROOT.length+1))+':'+(i+1)+':'+line+'\n']:[]).join('');}).join('');
// rg emits its finite files in native traversal order; bind every complete row without inventing a new run.
eq(tail.result.output.trimEnd().split('\n').sort(),expectedTail.trimEnd().split('\n').sort(),'all exact original rg rows and line numbers');
for(const row of templates.templates){
 const b=plan.builds[row.build_number],g=row.grant_with_nulls_not_accepted;
 eq(g.phase,row.phase,'exact phase');eq(g.build_number,row.build_number,'exact number');
 const dynamic={controller_source_reception:plan.controller_root+'/SOURCE_RECEPTION.md'};
 if(row.phase!=='refresh')Object.assign(dynamic,{current_key_reception:b.root_parent+'/CURRENT_KEY_RECEPTION.md',refresh_result:b.phase_outputs.refresh+'/RESULT.json',refresh_seal:b.phase_outputs.refresh+'/SHA256SUMS'});
 if(row.phase==='capture')Object.assign(dynamic,{enabled_binding_reception:b.root_parent+'/ENABLED_BINDING_RECEPTION.md',enabled_binding:b.phase_outputs.enable+'/BINDING.json',enable_seal:b.phase_outputs.enable+'/SHA256SUMS'});
 for(const[k,p]of Object.entries(dynamic))eq(g.required_receipts[k],{path:p,pin:null},'exact future null role');
 eq(g.cwd,ROOT,'exact cwd');eq(row.controller_environment,plan.controller_environment,'exact controller ENV4');
 eq(row.required_cli_argv.slice(10),['<ACTUAL_POSITIVE_AUTHORITY_BYTES>','<ACTUAL_64_LOWERCASE_HEX_AUTHORITY_SHA256>'],'only unissued CLI pins');
}
read(GATE+'/receive.js');read(GATE+'/SOURCE_DERIVATION.json');
for(let pass=0;pass<2;pass++)for(const[p,v]of Object.entries({...reads})){eq(pin(read(p)),v,'all root original byte keys');}
const fullInputs={fields:['path','bytes','sha256',...FIELDS],physical_workspace_only:true,resolved_equals_path:true,symlink:null,lstat_equals_stat:true,rows:Object.keys(reads).sort().map(p=>[p,reads[p].bytes,reads[p].sha256,...RICH[p]])};
console.log(JSON.stringify({status:'PASS_ROOT_P211_TERMINAL_CONTROLLER_SOURCE_ONLY',checks,workspace_read_files:Object.keys(reads).length,
 complete_preparation:{payloads:9,files:10,seal:prepSeal,source:pin(Buffer.from(source)),source_lines:724,plan:pin(read(HERE+'/INPUT_PLAN.json'))},
 original_fields_received:{planned_workspace_inputs:272,old_workspace_keys:503,old_total_read_key:1299,old_configuration_entries:843,old_host_selector:840,old_host_strings:841,round2_files:124,complete_original_native_envelopes:sourceRecords.length,source_read_bindings:sourceBindings.length,full_native_inventory_bytes:122342,full_native_schema_bytes:76072},
 source_bindings:sourceBindings,old_metadata_checks_reconstructed:[8512,10602],controller_execution:false,host_reads:0,dependency_queries:0,builds:0,authority:false,
 source_scope:'Root derivative of fully read author metadata; not independent review, runtime/key acceptance or build authority.',
 external:'OWNER_AMBER / HOLD_EXTERNAL',INPUTS:fullInputs},null,2));
