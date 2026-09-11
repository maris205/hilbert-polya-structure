'use strict';
// Independently owned workspace-only documentary metadata, not adapter code.
// Reads submitted sources as bytes/text only. No eval/import/AST/compile,
// child process, host lookup, ambient settings read or filesystem write.
const fs = require('node:fs'), crypto = require('node:crypto'), util = require('node:util');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = 'docs/papers211_215_sequence/qa/';
const PREP = QA+'p212_initial_build_preparation01/';
const READS = {}, RICH = {}, LABELS = [], ENVELOPES = [];
const pin = raw => ({bytes:raw.length,sha256:crypto.createHash('sha256').update(raw).digest('hex')});
function need(v,label) { LABELS.push(label); if (!v) throw Error(label); }
function eq(a,b,label) { need(util.isDeepStrictEqual(a,b),label); }
function read(name,expected) {
  need(typeof name==='string' && !name.startsWith('/') && !/[\\\r\n\x00]/.test(name) &&
       name.split('/').every(s=>s && s!=='.' && s!=='..'),'literal workspace path '+name);
  let path=ROOT;
  for(const part of name.split('/')) { path+='/'+part; need(!fs.lstatSync(path).isSymbolicLink(),'no workspace alias '+path); }
  const a=fs.lstatSync(path,{bigint:true}), raw=fs.readFileSync(path), z=fs.lstatSync(path,{bigint:true});
  const meta=s=>Object.fromEntries(['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'].map(k=>[k,String(s[k])]));
  need(a.isFile(),'ordinary workspace original '+name);
  eq(meta(a),meta(z),'all exact decimal-integer stat fields stable '+name);
  const value=pin(raw), rich={...value,resolved:path,symlink:null,stat_decimal_strings:meta(a)};
  if(expected) eq(value,expected,'entire expected original pin '+name);
  if(READS[name]) { eq(value,READS[name],'repeated whole original bytes '+name); eq(rich,RICH[name],'repeated full original stat '+name); }
  READS[name]=value; RICH[name]=rich; return raw;
}
const obj=name=>JSON.parse(read(name));
function workspace(p) { need(p.startsWith(ROOT+'/'),'absolute input stays in workspace'); return p.slice(ROOT.length+1); }
function envelope(record,label) {
  const keys=Object.keys(record).sort();
  const originalMetadataEnvelope = label==='author_complete_metadata' &&
    util.isDeepStrictEqual(keys,['request','result','scope']) &&
    record.scope==='Actual author-side workspace metadata execution, not submitted-source execution or independent review.';
  need(originalMetadataEnvelope || util.isDeepStrictEqual(keys,['request','result']) || util.isDeepStrictEqual(keys,['path','request','result']),
       'complete actual outer schema '+label);
  const r=record.result,q=record.request;
  eq(Object.keys(r).sort(),['chunk_id','exit_code','original_token_count','output','wall_time_seconds'],'all actual native result fields '+label);
  need(typeof q.cmd==='string' && q.cmd && Object.keys(q).every(k=>['cmd','workdir','login','max_output_tokens','yield_time_ms'].includes(k)),
       'actual bounded metadata command request '+label);
  need(q.workdir===undefined || q.workdir===ROOT,'recorded workspace cwd '+label);
  need(Number.isInteger(q.max_output_tokens) && q.max_output_tokens>0,'actual original output limit '+label);
  need(r.exit_code===0 && typeof r.chunk_id==='string' && r.chunk_id && Number.isFinite(r.wall_time_seconds) && r.wall_time_seconds>=0 &&
       Number.isInteger(r.original_token_count) && r.original_token_count>=0 && typeof r.output==='string','actual complete native exit '+label);
  need(!r.output.startsWith('Warning: truncated output'),'complete actual saved native output '+label);
  const raw=Buffer.from(r.output);
  ENVELOPES.push({label,request:pin(Buffer.from(JSON.stringify(q))),whole_output:pin(raw),exit_code:0,chunk_id:r.chunk_id});
  return raw;
}

function inspect() {
  const payloadNames=['BINDING.disabled.json','HANDOFF.md','HISTORICAL_LOCK_GAP.json','INPUT_PINS.json','LINEAGE.json',
    'NATIVE_METADATA.json','NATIVE_READS.json','PLAN.md','PRESEAL_NATIVE.json','SOURCE_GRAPH.json','SOURCE_PROFILE_DELTA.json'].sort();
  const manifestRaw=read(PREP+'SHA256SUMS');
  need(manifestRaw.at(-1)===10,'complete nonself seal LF');
  const rows={};
  for(const line of manifestRaw.toString().trimEnd().split('\n')) {
    const m=/^([0-9a-f]{64})  ([^/]+)$/.exec(line);
    need(m && payloadNames.includes(m[2]) && !rows[m[2]],'exact unique original payload row');
    const value=pin(read(PREP+m[2])); eq(value.sha256,m[1],'entire sealed original '+m[2]); rows[m[2]]=value;
  }
  eq(Object.keys(rows).sort(),payloadNames,'all11 submitted payloads');
  eq(fs.readdirSync(ROOT+'/'+PREP).sort(),[...payloadNames,'SHA256SUMS'].sort(),'complete original12file tree, no directories');
  eq(manifestRaw,Buffer.from(payloadNames.map(n=>rows[n].sha256+'  '+n+'\n').join('')),'whole sorted original seal reconstruction');
  const inputs=obj(PREP+'INPUT_PINS.json'), graph=obj(PREP+'SOURCE_GRAPH.json'), lineage=obj(PREP+'LINEAGE.json');
  const gap=obj(PREP+'HISTORICAL_LOCK_GAP.json'),delta=obj(PREP+'SOURCE_PROFILE_DELTA.json'),binding=obj(PREP+'BINDING.disabled.json');
  eq(inputs.schema,'p212-initial-build-preparation-workspace-input-pins-v1','original pin-list schema');
  eq(Object.keys(inputs.pins).length,28,'complete28 original selected paths');
  for(const[n,value]of Object.entries(inputs.pins)) read(n,value);
  const oldBinding=obj(lineage.old_accepted_binding.path), oldLock=obj(workspace(lineage.old_lock.path));
  eq(oldBinding.adapter_pins,lineage.old_adapter_pins,'complete accepted old5adapter binding');
  eq(oldLock.code_observations,lineage.old_adapter_pins,'complete old5code observations');
  eq(oldBinding.dependency_lock,lineage.old_lock,'exact accepted full old lock reference');
  eq(oldBinding.source_pins,oldLock.source_observations,'complete old9source binding/lock key');
  eq(Object.keys(oldLock.source_observations).length,9,'old source count really9');
  eq(oldBinding.root_read_receipt,{path:ROOT+'/'+lineage.old_infrastructure_reception.path,pin:lineage.old_infrastructure_reception.pin},
     'actual old infrastructure acceptance pointer');
  for(const[n,value]of Object.entries(lineage.old_adapter_pins)) read(lineage.old_adapter_root+'/'+n,value);
  for(const key of ['old_accepted_binding','old_lock','old_infrastructure_reception','old_actual_build_reception']) {
    const r=lineage[key]; read(r.path.startsWith('/')?workspace(r.path):r.path,r.pin);
  }
  eq(Object.keys(oldLock.entries).length,840,'entire historical840 row census');
  eq(Object.keys(oldLock.selector_specs).sort(),Object.keys(oldLock.entries).sort(),'all original selector/entry spellings');
  eq(Object.keys(oldLock.selection_reasons).sort(),Object.keys(oldLock.entries).sort(),'all original selection reasons');
  const fingerprints=Object.fromEntries(Object.entries(oldLock).map(([k,v])=>[k,{type:Array.isArray(v)?'array':typeof v,
    items:v&&typeof v==='object'?Object.keys(v).length:null,pin_of_JSON_stringify_in_original_property_order:pin(Buffer.from(JSON.stringify(v)))}]));
  eq(Object.keys(fingerprints).length,15,'entire15 old object fields');
  eq(fingerprints,gap.original_top_level_fields,'all15 entire original serialized field fingerprints');
  eq(gap.original_lock,lineage.old_lock,'gap retains exact original lock');
  const directNames=['article.cls','plain.bst','geometry.sty','amsmath.sty','amssymb.sty','amsthm.sty','booktabs.sty','array.sty','fontenc.sty','hyperref.sty'];
  const matches=Object.fromEntries(directNames.map(n=>[n,{old_entry_spellings:Object.keys(oldLock.entries).filter(p=>p.split('/').at(-1)===n),
    old_query_resolution:oldLock.queries.explicit_graph_seeds.resolutions[n]??null}]));
  eq(matches,gap.direct_source_name_matches,'all10 direct historical names, no host dereference');
  for(const n of ['plain.bst','array.sty']) eq(matches[n],{old_entry_spellings:[],old_query_resolution:null},'both entry/query absent in old object '+n);
  eq(matches['article.cls'],{old_entry_spellings:['/usr/share/texlive/texmf-dist/tex/latex/base/article.cls'],old_query_resolution:null},
     'article only historical row, not an explicit old seed query');
  need(gap.host_reads===0 && gap.ambient_environment_read===false && gap.new_dependency_lock===null,'original gap honestly no new host key');
  const sourceNames=['main.tex','math_commands.tex','references.bib','sections/01_setup.tex','sections/02_returns.tex',
    'sections/03_period_set.tex','sections/04_census.tex','sections/05_scope.tex'];
  eq(graph.paper_root,'papers/212-closed-pointer-orbits','actual P212 graph root');
  eq(graph.accepted_source_original_root,QA+'p212_author_source_reception/source_preparation_original','physical accepted source root');
  eq(Object.keys(graph.source_pins),sourceNames,'complete ordered8 build inputs');
  const texts={},pairs=[];
  for(const name of sourceNames) {
    const current=read(graph.paper_root+'/'+name,graph.source_pins[name]),original=read(graph.accepted_source_original_root+'/'+name,graph.source_pins[name]);
    eq(current,original,'entire raw current/accepted source pair '+name); texts[name]=current.toString();
    pairs.push({current:graph.paper_root+'/'+name,original:graph.accepted_source_original_root+'/'+name,pin:pin(current)});
  }
  const sourceTotal=Object.values(graph.source_pins).reduce((s,v)=>s+v.bytes,0);
  eq([graph.total_files,graph.tex_files,graph.bib_files,graph.total_bytes],[8,7,1,sourceTotal],'full source counts and bytes');
  eq(sourceTotal,19659,'actual19659 source bytes');
  const main=texts['main.tex'];
  const classes=[...main.matchAll(/\\documentclass(?:\[([^\]]*)\])?\{([^}]+)\}/g)].map(m=>({name:m[2],options:m[1]?m[1].split(','):[]}));
  eq(classes,[{name:'article',options:['10pt']}],'literal single article10pt class, not inherited A4');
  eq(graph.document_class,classes[0],'whole actual class/options record');
  const packages=[...main.matchAll(/\\usepackage(?:\[([^\]]*)\])?\{([^}]+)\}/g)].flatMap(m=>m[2].split(',').map(name=>({name,options:m[1]?m[1].split(','):[]})));
  eq(packages,graph.packages,'all ordered package names and option arrays');
  eq(packages,[{name:'geometry',options:['margin=0.85in']},{name:'amsmath',options:[]},{name:'amssymb',options:[]},{name:'amsthm',options:[]},
    {name:'booktabs',options:[]},{name:'array',options:[]},{name:'fontenc',options:['T1']},{name:'hyperref',options:['hidelinks']}],
    'P212 full8package profile independently literal');
  const includes=[...main.matchAll(/\\input\{([^}]+)\}/g)].map(m=>m[1]);
  eq(includes,sourceNames.filter(n=>!['main.tex','references.bib'].includes(n)).map(n=>n.slice(0,-4)),'complete ordered main input graph');
  eq(graph.main_inputs,includes,'declared main input graph');
  eq([...main.matchAll(/\\bibliographystyle\{([^}]+)\}/g)].map(m=>m[1]),['plain'],'actual single plain bibliography style');
  eq([...main.matchAll(/\\bibliography\{([^}]+)\}/g)].map(m=>m[1]),['references'],'actual single references database');
  eq([graph.bibliography_style,graph.bibliography,graph.external_figures],['plain',['references'],[]],'graph bibliography/figure roles');
  for(const[n,t]of Object.entries(texts)) {
    need(!/\\(?:include|includegraphics|write18|openin|openout|read|catcode)\b/.test(t),'no literal unsupported external TeX input '+n);
    if(n!=='main.tex') need(!/\\(?:input|usepackage|RequirePackage|documentclass)\b/.test(t),'no nested literal input graph '+n);
  }
  eq(fs.readdirSync(ROOT+'/'+graph.paper_root+'/sections').sort(),sourceNames.filter(n=>n.startsWith('sections/')).map(n=>n.slice(9)).sort(),'actual exact5section membership');
  const sourceManifest=read(graph.accepted_source_original_root+'/SOURCE_PREP_MANIFEST.sha256').toString();
  const sourceRows={}; for(const line of sourceManifest.trimEnd().split('\n')) { const m=/^([a-f0-9]{64})  (.+)$/.exec(line); need(m&&!sourceRows[m[2]],'complete21row accepted source manifest syntax');sourceRows[m[2]]=m[1]; }
  eq(Object.keys(sourceRows).length,21,'historical source seal remains21, not a whole current paper seal');
  for(const n of sourceNames) eq(sourceRows[n],graph.source_pins[n].sha256,'all8 original build sources in accepted21manifest');
  read(graph.accepted_source_preparation_receipt.path,graph.accepted_source_preparation_receipt.pin);
  const env={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'};
  eq(binding.environment,env,'exact literal proposed ENV8'); eq(oldLock.environment,env,'whole original ENV8 equality'); eq(gap.stored_environment,env,'gap stored ENV8');
  need(binding.enabled===false && binding.paper_id===212 && binding.schema==='p212-initial-source-only-build-proposal-v1' &&
       binding.status==='SOURCE_ONLY_DISABLED_INCOMPLETE_PENDING_EXACT_ADAPTER_AND_P212_DEPENDENCY_RECEPTION' &&
       binding.scope==='ONE_INITIAL_BUILD_ONLY_NOT_TERMINAL','explicit disabled initial proposal, not a runner schema');
  eq(binding.output,ROOT+'/'+QA+'p212_initial_build_01','future initial output name only, not probed');
  eq(binding.source_root,ROOT+'/'+graph.paper_root,'proposal correct source root'); eq(binding.source_pins,graph.source_pins,'all8 real proposal source pins');
  for(const k of ['adapter_pins','dependency_lock','runtime_settings_observations','cwd_relative_configuration','root_read_receipt']) eq(binding[k],null,'operational field remains null '+k);
  eq(binding.receipt_references,{paper_source_preparation:graph.accepted_source_preparation_receipt,fresh_P212_build_infrastructure:null,
    P212_build_dependency_and_setup:null,complete_current_build_key_and_settings:null},'all actual/pending receipt roles');
  eq(binding.root_authorization,{issuer:null,decision:null,record:null},'no issuer/decision/record invented');
  for(const k of ['round2_required','scientific_execution','manuscript_review','terminal_acceptance']) eq(binding[k],false,'separate gate '+k);
  eq(Object.keys(binding.future_cwd_relative_roles).sort(),['TEXMFCONFIG','TEXMFHOME','TEXMFVAR'],'all3 future cwd roles');
  for(const[k,v]of Object.entries(binding.future_cwd_relative_roles)) {
    eq(v.relative,oldLock.cwd_relative_absence_roles[k].relative,'historical relative spelling only '+k);
    eq(v.required_state,'ABSENT','future required state only '+k); eq(v.actual_observation,null,'no actual cwd absence invented '+k);
  }
  eq(delta.old_source,{path:lineage.old_adapter_root+'/build_core.py',pin:lineage.old_adapter_pins['build_core.py']},'exact profile old-source identity');
  const oldCore=read(delta.old_source.path,delta.old_source.pin).toString();
  const ids=['paper-root','eight-source-profile','eight-package-profile','class-literal','plain-bibliography-contract','profile-return-labels','source-count-documentation'];
  eq(delta.changes.map(r=>r.id),ids,'exact7 profile substitution roles');
  let prospective=oldCore; const deltaRows=[];
  for(const row of delta.changes) {
    eq(row.operation,'replace_once_literal_text','only literal substitution '+row.id);
    eq(prospective.split(row.before).length,2,'exact unique original anchor '+row.id);
    need(typeof row.after==='string' && row.after!==row.before,'substantive exact profile replacement '+row.id);
    prospective=prospective.replace(row.before,row.after);
    deltaRows.push({id:row.id,old_bytes:Buffer.byteLength(row.before),new_bytes:Buffer.byteLength(row.after)});
  }
  const expectAfter=["PAPER = ROOT / 'papers/212-closed-pointer-orbits'",
    "SOURCES = ('main.tex', 'math_commands.tex', 'references.bib',\n           'sections/01_setup.tex', 'sections/02_returns.tex',\n           'sections/03_period_set.tex', 'sections/04_census.tex',\n           'sections/05_scope.tex')",
    "PACKAGES = ('geometry', 'amsmath', 'amssymb', 'amsthm',\n            'booktabs', 'array', 'fontenc', 'hyperref')",
    "require('\\\\documentclass[10pt]{article}' in main, 'Expected article[10pt]')",
    "require('\\\\bibliographystyle{plain}' in main and\n            '\\\\bibliography{references}' in main, 'Expected plain/references')",
    "return {'sources': list(SOURCES), 'class': 'article', 'bibliography_style': 'plain',",
    '"""Validate the read eight-file literal graph, not general TeX safety."""'];
  eq(delta.changes.map(r=>r.after),expectAfter,'all7 complete independent intended replacement texts');
  let reversed=prospective; for(const row of [...delta.changes].reverse()) { eq(reversed.split(row.after).length,2,'unique reverse anchor '+row.id); reversed=reversed.replace(row.after,row.before); }
  eq(Buffer.from(reversed),Buffer.from(oldCore),'entire seven-substitution reverse delta restores every original byte');
  need(prospective.includes("'p211-native-attempt-v1'") && prospective.includes("qa/p211_build_revision01"),'partial delta still has unapplied operational roles, not executable approval');
  for(const k of ['submitted_source_parsed_as_code','changes_applied_to_files','complete_P212_runner_available']) eq(delta[k],false,'partial delta boundary '+k);
  eq(lineage.prospective_operational_roles,['build_core.py','build_p212.py','launch_build.py'],'three future roles only');
  eq([lineage.new_operational_sources_materialized,lineage.new_operational_source_pins],[false,null],'no adapter materialized or pinned');

  const originals=obj(PREP+'NATIVE_READS.json'); eq(originals.records.length,20,'all20 actual selected author records');
  let fullSources=0;
  for(let i=0;i<originals.records.length;i++) {
    const rec=originals.records[i],raw=envelope(rec,'author_selected_'+i), m=/^sed -n '(\d+),(\d+)p' ([^\s]+)$/.exec(rec.request.cmd);
    if(m) {
      eq(rec.path,m[3],'native source declared original path '+i);
      const body=read(m[3]), lines=body.toString().match(/[^\n]*\n|[^\n]+$/g)||[];
      eq(raw,Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join('')),'entire original sed output '+i);
      eq(raw,body,'complete original source body binding '+i);fullSources++;
    } else {
      const data=JSON.parse(raw);
      if(rec.path==='DATA_ONLY_LOCK_AND_P212_SOURCE_GRAPH') {
        const dataInputs={ [workspace(lineage.old_lock.path)]:lineage.old_lock.pin };
        for(const p of pairs) { dataInputs[p.current]=p.pin; dataInputs[p.original]=p.pin; }
        eq(data,{status:'P212_BUILD_SOURCE_AND_P211_LOCK_DATA_ONLY_NOT_CURRENT_HOST_CHECK',sources:graph.source_pins,total_source_bytes:19659,
          old_lock_pin:lineage.old_lock.pin,old_lock_fields:fingerprints,old_environment:oldLock.environment,old_cwd_relative_roles:oldLock.cwd_relative_absence_roles,
          old_explicit_seed_query:oldLock.queries.explicit_graph_seeds,old_query_commands:oldLock.query_commands,direct_P212_name_matches:matches,inputs:dataInputs,
          host_referents_dereferenced:0,ambient_environment_collected:false,submitted_sources_imported_AST_compiled_executed:false},'entire saved source/lock metadata projection');
      } else {
        eq(rec.path,'DATA_ONLY_COMPLETE_SELECTED_LINEAGE_PINS','second exact original metadata role');
        eq(data,{status:'AUTHOR_WORKSPACE_ONLY_SOURCE_LINEAGE_PINS_NOT_HOST_CHECK',pins:inputs.pins,inputs:28,
          old_adapter_pins:lineage.old_adapter_pins,old_full_lock:lineage.old_lock,
          accepted_P212_build_source_seal_entries_checked:8,host_reads:0,submitted_source_executions:0},
          'entire second saved original metadata projection including complete lock reference');
      }
    }
  }
  eq(fullSources,18,'all18 entire saved author source-output bindings');
  const actualMetadata=obj(PREP+'NATIVE_METADATA.json'),metadataRaw=envelope(actualMetadata,'author_complete_metadata'),metadata=JSON.parse(metadataRaw);
  const firstNames=['SOURCE_GRAPH.json','LINEAGE.json','HISTORICAL_LOCK_GAP.json','SOURCE_PROFILE_DELTA.json','BINDING.disabled.json','INPUT_PINS.json','NATIVE_READS.json','PLAN.md'].sort();
  const firstPins=Object.fromEntries(firstNames.map(n=>[n,rows[n]]));
  const expectedMetadata={status:'AUTHOR_SMALL_DELTA_SOURCE_PREPARATION_METADATA_CLOSED_NOT_BUILD_READY',actual_utc:metadata.actual_utc,checks:1412,
    original_pins:28,workspace_read_files:36,source_files:8,source_bytes:19659,complete_saved_native_source_reads:18,all_selected_native_records:20,
    original_lock_fields:15,old_selector_rows:840,confirmed_missing_old_entry_names:['plain.bst','array.sty'],
    confirmed_missing_old_explicit_query_names:['article.cls','plain.bst','array.sty'],partial_literal_delta_rows:deltaRows,partial_text_not_written:true,
    disabled_template:true,round2_required:false,payload_pins:firstPins,original_pin_map:inputs.pins,host_referents_dereferenced:0,ambient_environment_read:false,
    submitted_import_AST_compile_execution:0,new_operational_sources:0,new_runtime_or_host_keys:0,science_canonical_PDF_read:false,builds:0,renders:0,page_views:0,
    root_authority:false,independent_review:false};
  eq(metadata,expectedMetadata,'entire author saved1412 metadata output reconstruction; no rerun of author command');
  eq(metadataRaw,Buffer.from(JSON.stringify(expectedMetadata,null,2)+'\n'),'complete actual metadata JSON stdout bytes');
  const actualPreseal=obj(PREP+'PRESEAL_NATIVE.json'),presealRaw=envelope(actualPreseal,'author_complete_preseal'),preseal=JSON.parse(presealRaw);
  const presealNames=payloadNames.filter(n=>n!=='PRESEAL_NATIVE.json');
  const presealPins=Object.fromEntries(presealNames.map(n=>[n,rows[n]]));
  const expectedPreseal={status:'AUTHOR_SMALL_DELTA_PRESEAL_COMPLETE_NOT_EXECUTION_READY',actual_utc:preseal.actual_utc,payloads:10,
    payload_bytes:Object.values(presealPins).reduce((s,v)=>s+v.bytes,0),payload:presealPins,native_metadata_chunk:actualMetadata.result.chunk_id,
    native_metadata_stdout_pin:pin(metadataRaw),original_inputs_checked_twice:28,disabled_template_retained:true,operational_sources_created:0,
    new_runtime_or_host_keys:0,host_referents_read:0,ambient_environment_read:false,science_build_render_page_view:0,independent_review:false,root_authority:false};
  eq(preseal,expectedPreseal,'entire author10payload preseal projection reconstruction');
  eq(presealRaw,Buffer.from(JSON.stringify(expectedPreseal)+'\n'),'whole actual preseal native stdout bytes');
  need(/^2026-09-09T\d\d:\d\d:\d\d\.\d{3}Z$/.test(metadata.actual_utc) && /^2026-09-09T\d\d:\d\d:\d\d\.\d{3}Z$/.test(preseal.actual_utc) &&
       metadata.actual_utc<preseal.actual_utc,'actual original chronological timestamp syntax/order only');
  const linkClosures=[];
  for(const name of ['PLAN.md','HANDOFF.md']) for(const m of read(PREP+name).toString().matchAll(/\[[^\]]*\]\(([^)]+)\)/g)) {
    need(/^[A-Za-z0-9_.]+$/.test(m[1]) && payloadNames.includes(m[1]),'exact local preparation document link '+m[1]);
    linkClosures.push({document:name,href:m[1],pin:pin(read(PREP+m[1]))});
  }
  eq(Object.keys(READS).length,40,'all12 submitted files plus28 originals, no other file read');
  for(let pass=0;pass<2;pass++) for(const[name,value]of Object.entries({...READS})) read(name,value);
  eq(fs.readdirSync(ROOT+'/'+PREP).sort(),[...payloadNames,'SHA256SUMS'].sort(),'complete source package final membership');
  return {status:'PASS_INDEPENDENT_SOURCE_ONLY_PLAN_HOLD_OPERATIONAL',checks:LABELS.length,workspace_read_paths:40,
    submitted_payloads:11,submitted_files:12,submitted_payload_bytes:Object.values(rows).reduce((s,v)=>s+v.bytes,0),submitted_seal:pin(manifestRaw),
    original_input_rows:28,source_pairs:pairs,source_profile:graph,whole_old_field_fingerprints:fingerprints,all10_historical_name_comparisons:matches,
    partial_profile_text_pin:pin(Buffer.from(prospective)),partial_delta_rows:deltaRows,profile_delta_written_or_executed:false,
    original_native_envelopes:ENVELOPES,complete_original_source_output_bindings:18,author_saved_metadata_checks:1412,original_preseal_payloads:10,
    all_preparation_local_links:linkClosures,host_referents_dereferenced:0,submitted_import_AST_compile_execution:0,dependency_queries:0,
    build_render_page_view:0,source_only_plan_accepted:true,executable_adapter_accepted:false,root_authority:false,mathematical_manuscript_review:false,
    external:'OWNER_AMBER / HOLD_EXTERNAL',READ_INPUTS:READS,RICH_INPUTS:RICH};
}
try { const result=inspect(); process.stdout.write(JSON.stringify(result,null,2)+'\n'); }
catch(error) { process.stdout.write(JSON.stringify({status:'FAIL_INDEPENDENT_SOURCE_METADATA_PRESERVE_ORIGINALS',checks:LABELS.length,error:String(error.stack),READ_INPUTS:READS,RICH_INPUTS:RICH},null,2)+'\n');process.exitCode=1; }
