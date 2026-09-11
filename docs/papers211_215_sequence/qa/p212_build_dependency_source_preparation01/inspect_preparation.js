'use strict';
// Author-owned workspace documentary validation only. Never execute query_frontier.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert').strict;
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa';
const BASE=QA+'/p212_build_dependency_source_preparation01';
const PREP=QA+'/p212_initial_build_preparation01',AUDIT=QA+'/p212_initial_build_source_audit01';
let checks=0;const reads={};
function eq(x,y){checks++;assert.deepEqual(x,y);}
function need(x){checks++;assert(x);}
const identity=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function read(p){
  need(typeof p==='string'&&p.startsWith(ROOT+'/')&&path.normalize(p)===p);
  for(let q=p;q.startsWith(ROOT);q=path.dirname(q)){need(!fs.lstatSync(q).isSymbolicLink());if(q===ROOT)break;}
  need(fs.statSync(p).isFile());eq(fs.realpathSync(p),p);
  const b=fs.readFileSync(p),k={...identity(b),resolved:p,symlink:null};
  if(reads[p])eq(reads[p],k);reads[p]=k;return b;
}
const obj=p=>JSON.parse(read(p));
function sealed(base,count){
  const b=read(base+'/SHA256SUMS');need(b.toString().endsWith('\n'));const rows={},dirs=[];
  for(const line of b.toString().slice(0,-1).split('\n')){
    const m=/^([a-f0-9]{64})  ([A-Za-z0-9_./-]+)$/.exec(line);
    need(m&&!m[2].startsWith('/')&&!m[2].split('/').some(s=>s==='..'||s==='.')&&!rows[m[2]]&&m[2]!=='SHA256SUMS');
    const data=read(base+'/'+m[2]);eq(identity(data).sha256,m[1]);rows[m[2]]=identity(data);
  }
  const actual=[];
  function walk(p){for(const n of fs.readdirSync(p).sort()){
    const q=p+'/'+n;need(!fs.lstatSync(q).isSymbolicLink());
    if(fs.statSync(q).isDirectory()){dirs.push(path.relative(base,q));walk(q);}else actual.push(path.relative(base,q));
  }}walk(base);eq(Object.keys(rows).length,count);eq(actual.sort(),Object.keys(rows).concat(['SHA256SUMS']).sort());
  return{payloads:count,files:actual.length,manifest:identity(b),payload_pins:rows,directories:dirs};
}
const oldPrep=sealed(PREP,11),oldAudit=sealed(AUDIT,17);
eq(oldPrep.manifest.sha256,'9ff857383047b6160b2db56183c376e2fad25b1433bb49c932ea47c17fcf7f43');
eq(oldPrep.directories,[]);eq(oldAudit.directories,['run02']);
const inputs=obj(PREP+'/INPUT_PINS.json');eq(Object.keys(inputs.pins).length,28);
for(const[p,k]of Object.entries(inputs.pins)){need(!p.startsWith('/'));eq(identity(read(ROOT+'/'+p)),k);}
const graph=obj(PREP+'/SOURCE_GRAPH.json'),lineage=obj(PREP+'/LINEAGE.json');
eq(graph.total_files,8);eq(graph.total_bytes,19659);
for(const[n,k]of Object.entries(graph.source_pins)){
  const a=read(ROOT+'/'+graph.paper_root+'/'+n),b=read(ROOT+'/'+graph.accepted_source_original_root+'/'+n);
  eq(a,b);eq(identity(a),k);
}
eq(fs.readdirSync(ROOT+'/'+graph.paper_root+'/sections').sort(),Object.keys(graph.source_pins).filter(n=>n.startsWith('sections/')).map(n=>n.slice(9)).sort());
const main=read(ROOT+'/'+graph.paper_root+'/main.tex').toString();
eq([...main.matchAll(/\\documentclass(?:\[([^\]]*)\])?\{([^}]+)\}/g)].map(m=>({name:m[2],options:m[1].split(',')})),[{name:'article',options:['10pt']}]);
const packages=[...main.matchAll(/\\usepackage(?:\[([^\]]*)\])?\{([^}]+)\}/g)].flatMap(m=>m[2].split(',').map(name=>({name,options:m[1]?m[1].split(','):[]})));
eq(packages,graph.packages);
eq([...main.matchAll(/\\input\{([^}]+)\}/g)].map(m=>m[1]),graph.main_inputs);
eq([...main.matchAll(/\\bibliographystyle\{([^}]+)\}/g)].map(m=>m[1]),['plain']);
eq([...main.matchAll(/\\bibliography\{([^}]+)\}/g)].map(m=>m[1]),['references']);
const lockBytes=read(lineage.old_lock.path),lock=JSON.parse(lockBytes);
eq(identity(lockBytes),lineage.old_lock.pin);eq(Object.keys(lock.entries).length,840);
const names=['article.cls','plain.bst','array.sty'];
const gap=Object.fromEntries(names.map(n=>[n,{entries:Object.keys(lock.entries).filter(p=>p.split('/').at(-1)===n),query:lock.queries.explicit_graph_seeds.resolutions[n]??null}]));
eq(gap['plain.bst'],{entries:[],query:null});eq(gap['array.sty'],{entries:[],query:null});eq(gap['article.cls'].entries.length,1);eq(gap['article.cls'].query,null);
const historicalNative=obj(BASE+'/HISTORICAL_LOCK_DOCUMENT_NATIVE.json');
eq(historicalNative.result.exit_code,0);
const projection={path:lineage.old_lock.path.slice(ROOT.length+1),...identity(lockBytes),fields:Object.keys(lock),entry_count:840,queries:lock.queries,query_commands:lock.query_commands,cwd_relative_absence_roles:lock.cwd_relative_absence_roles,host_referents_dereferenced:0};
eq(Buffer.from(historicalNative.result.output),Buffer.from(JSON.stringify(projection,null,2)+'\n'));
const archived=obj(QA+'/p211_build_preparation/NATIVE_TOOL_ENVELOPES.json');
const oldMechanism={scope:archived.scope,notes:archived.notes,graph_reads:archived.graph_reads};
eq(obj(BASE+'/OLD_TEX_MECHANISM.json'),oldMechanism);
need(archived.graph_reads.amsart_context.returned.output.includes('\\InputIfFileExists{amsart.cfg}'));
const originals=obj(BASE+'/ORIGINAL_READS_NATIVE.json');let sourceBindings=0;
for(const r of [...originals.intake,...originals.sources,...originals.paper_sources]){
  eq(r.result.exit_code,0);eq(Buffer.from(r.result.output),read(ROOT+'/'+r.path));sourceBindings++;
}
eq(sourceBindings,25);eq(originals.old_graph_excerpt_projection.result.exit_code,0);
eq(Buffer.from(originals.old_graph_excerpt_projection.result.output),read(BASE+'/OLD_TEX_MECHANISM.json'));
const origin=obj(BASE+'/SOURCE_ORIGIN.json');eq(origin.operational_source_reuse,false);eq(origin.query_emitter_source_executed,false);eq(origin.current_dependency_lock,null);
for(let i=0;i<5;i++){eq(origin.old_sources_consulted[i].path,originals.sources[i].path);eq(origin.old_sources_consulted[i].read_native_chunk,originals.sources[i].result.chunk_id);}
const f=obj(BASE+'/QUERY_FRONTIER.json'),d=obj(BASE+'/INTERFACE.disabled.json');
eq(Object.keys(f),["schema","status","approved","environment","command_cwd_proposal","command_cwd_observation","profile","initial_name_seeds","generation_policy","ordered_command_proposals","native_commands_executed","host_dependency_bodies_received","actual_resolutions","actual_source_edges","actual_class_configuration_semantics","actual_font_selector","actual_format_provenance","actual_runtime_tool_linkage_key","actual_effective_build_cwd_configuration","dependency_lock","root_authority","continuation"]);
eq(f.continuation,"Stop after receiving this finite frontier and all returned dependency bodies; a separately inspected source-derived edge table and any next finite query source are required. No automatic recursive discovery, build-driven lock enlargement, guessed article.cfg, lmodern regex, metric list or inherited840 rows.");
eq(f.schema,'p212-build-finite-query-frontier-source-v1');eq(f.status,'SOURCE_ONLY_PLAN_NOT_A_QUERY_EXECUTOR_OR_DEPENDENCY_LOCK');eq(f.approved,false);
const env={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'};
eq(f.environment,env);eq(f.environment,lock.environment);
eq(f.profile,{source_graph_path:'docs/papers211_215_sequence/qa/p212_initial_build_preparation01/SOURCE_GRAPH.json',paper_root:graph.paper_root,source_pins:graph.source_pins,source_files:8,source_bytes:19659,document_class:graph.document_class,packages:graph.packages,main_inputs:graph.main_inputs,bibliography_style:'plain',bibliography:['references'],external_figures:[]});
const seeds=f.initial_name_seeds;eq(seeds.length,19);
eq(seeds.slice(0,10).map(x=>x.name),['article.cls',...graph.packages.map(x=>x.name+'.sty'),'plain.bst']);
eq(seeds.slice(0,9).map(x=>x.program),Array(9).fill('pdflatex'));eq(seeds[9].program,'bibtex');
eq(seeds.slice(10).map(x=>x.name),['texmf.cnf','texmf.cnf','pdflatex.fmt','pdftexconfig.tex','latex.ltx','pdftex.map','fmtutil.cnf','updmap.cfg','texfonts.map']);
eq(seeds.filter(x=>x.required).map(x=>x.name),['article.cls',...graph.packages.map(x=>x.name+'.sty'),'plain.bst','pdflatex.fmt']);
need(seeds.every(x=>x.engine==='pdftex'&&!/article\.cfg|amsart|lmodern|\.tfm$|\.fd$/.test(x.name)));
const vars=['TEXMF','TEXMFCNF','TEXMFHOME','TEXMFCONFIG','TEXMFVAR','TEXMFDBS','TEXINPUTS','BIBINPUTS','BSTINPUTS','shell_escape','openin_any','openout_any'];
const flags=['--no-mktex=tex','--no-mktex=fmt','--no-mktex=tfm','--no-mktex=pk'];
eq(f.generation_policy.requested_no_generation_flags,flags);
eq(f.generation_policy.status,'NOT_ESTABLISHED_UNTIL_INSTALLED_HELP_AND_RUNTIME_SOURCE_RECEIVED');
const expected=[
{label:'contract_help',phase:'CONTRACT_ONLY',argv:['/usr/bin/kpsewhich','--help'],expected_exit_codes:[0],result:null},
{label:'contract_version',phase:'CONTRACT_ONLY',argv:['/usr/bin/kpsewhich','--version'],expected_exit_codes:[0],result:null}
],later='LOOKUP_ONLY_AFTER_SEPARATE_OPTION_AND_RUNTIME_SOURCE_ACCEPTANCE';
for(const s of seeds)for(const mode of ['default','all'])expected.push({label:s.label+'_'+mode,phase:later,argv:['/usr/bin/kpsewhich','--progname='+s.program,'--engine='+s.engine,...flags,...(mode==='all'?['--all']:[]),s.name],expected_exit_codes:[0,1],result:null});
for(const n of vars)expected.push({label:'var_'+n,phase:later,argv:['/usr/bin/kpsewhich','--progname='+(['BIBINPUTS','BSTINPUTS'].includes(n)?'bibtex':'pdflatex'),'--engine=pdftex',...flags,'-var-value='+n],expected_exit_codes:[0,1],result:null});
expected.push({label:'expanded_TEXMF',phase:later,argv:['/usr/bin/kpsewhich','--progname=pdflatex','--engine=pdftex',...flags,'-expand-path=$TEXMF'],expected_exit_codes:[0,1],result:null});
eq(expected.length,53);eq(new Set(expected.map(x=>x.label)).size,53);eq(f.ordered_command_proposals,expected);
for(const k of ['command_cwd_observation','actual_resolutions','actual_source_edges','actual_class_configuration_semantics','actual_font_selector','actual_format_provenance','actual_runtime_tool_linkage_key','actual_effective_build_cwd_configuration','dependency_lock','root_authority'])eq(f[k],null);
eq(f.native_commands_executed,0);eq(f.host_dependency_bodies_received,0);
eq(d.enabled,false);eq(d.emitter.may_issue_native_children,false);eq(d.emitter.may_read_files,false);eq(d.emitter.may_write_files,false);
for(const[k,v]of Object.entries(d))if(k.endsWith('_authorized'))eq(v,false);
for(const k of ['dependency_lock','build_binding','actual_native_results','actual_body_pins','actual_class_configuration','actual_font_metrics_maps','actual_format_key','actual_configuration_key'])eq(d[k],null);
eq(d.future_binding.pin,null);eq(d.future_capture.source,null);eq(d.future_capture.source_pin,null);eq(d.future_capture.runtime_key,null);eq(d.future_capture.manifest,null);eq(d.future_capture.root_original_receipt,null);
eq(d.future_cwd.path,f.command_cwd_proposal);eq(d.future_cwd.observation,null);eq(d.root_authorization,{issuer:null,decision:null,record:null});
const header="'use strict';\n// AUTHOR SOURCE_ONLY finite command-plan emitter; never a host-query executor.\n// Only writes prospective JSON to stdout. No imports, reads, children or eval.\n// The separately inspected future capture source is intentionally not supplied.\n",tail="const commands = [\n  {label:'contract_help',phase:'CONTRACT_ONLY',argv:['/usr/bin/kpsewhich','--help'],expected_exit_codes:[0],result:null},\n  {label:'contract_version',phase:'CONTRACT_ONLY',argv:['/usr/bin/kpsewhich','--version'],expected_exit_codes:[0],result:null}\n];\nconst later = 'LOOKUP_ONLY_AFTER_SEPARATE_OPTION_AND_RUNTIME_SOURCE_ACCEPTANCE';\nfor (const seed of seeds) for (const mode of ['default','all']) commands.push({\n  label:seed.label+'_'+mode, phase:later,\n  argv:['/usr/bin/kpsewhich','--progname='+seed.program,'--engine='+seed.engine,\n        ...generation.requested_no_generation_flags,...(mode==='all'?['--all']:[]),seed.name],\n  expected_exit_codes:[0,1],result:null\n});\nfor (const name of variables) commands.push({\n  label:'var_'+name,phase:later,\n  argv:['/usr/bin/kpsewhich','--progname='+(['BIBINPUTS','BSTINPUTS'].includes(name)?'bibtex':'pdflatex'),\n        '--engine=pdftex',...generation.requested_no_generation_flags,'-var-value='+name],\n  expected_exit_codes:[0,1],result:null\n});\ncommands.push({label:'expanded_TEXMF',phase:later,\n  argv:['/usr/bin/kpsewhich','--progname=pdflatex','--engine=pdftex',\n        ...generation.requested_no_generation_flags,'-expand-path=$TEXMF'],\n  expected_exit_codes:[0,1],result:null\n});\nconst frontier = {\n  schema:'p212-build-finite-query-frontier-source-v1',\n  status:'SOURCE_ONLY_PLAN_NOT_A_QUERY_EXECUTOR_OR_DEPENDENCY_LOCK',approved:false,\n  environment,command_cwd_proposal:cwd,command_cwd_observation:null,profile,\n  initial_name_seeds:seeds,generation_policy:generation,ordered_command_proposals:commands,\n  native_commands_executed:0,host_dependency_bodies_received:0,actual_resolutions:null,\n  actual_source_edges:null,actual_class_configuration_semantics:null,actual_font_selector:null,\n  actual_format_provenance:null,actual_runtime_tool_linkage_key:null,\n  actual_effective_build_cwd_configuration:null,dependency_lock:null,root_authority:null,\n  continuation:\"Stop after receiving this finite frontier and all returned dependency bodies; a separately inspected source-derived edge table and any next finite query source are required. No automatic recursive discovery, build-driven lock enlargement, guessed article.cfg, lmodern regex, metric list or inherited840 rows.\"\n};\nprocess.stdout.write(JSON.stringify(frontier,null,2)+'\\n');\n";
const expectedSource=header+'const environment = '+JSON.stringify(f.environment)+';\nconst cwd = '+JSON.stringify(f.command_cwd_proposal)+';\nconst profile = '+JSON.stringify(f.profile,null,2)+';\nconst seeds = [\n'+seeds.map((x,i)=>'  '+JSON.stringify(x)+(i===seeds.length-1?'':',')).join('\n')+'\n];\nconst variables = '+JSON.stringify(vars)+';\nconst generation = '+JSON.stringify(f.generation_policy,null,2)+';\n'+tail;
eq(read(BASE+'/query_frontier.js'),Buffer.from(expectedSource));
const obligations=obj(BASE+'/SELECTOR_OBLIGATIONS.json'),capture=obj(BASE+'/CAPTURE_CONTRACT.json');
eq(obligations.initial_frontier,{names:19,command_proposals:53,actual_queries:0,body_pins:null});
eq(obligations.stages.map(x=>x.id),['S0_QUERY_RUNTIME_AND_OPTIONS','S1_DIRECT_BODIES','S2_CLASS_AND_ORDERED_PACKAGE_GRAPH','S3_T1_AND_MATH_FONT_GRAPH','S4_FORMAT_AND_CONFIG_GRAPH','S5_NATIVE_AND_RENDER_TOOL_GRAPH','S6_FRESH_LOCK_AND_ACTUAL_BUILD_CWD']);
need(obligations.stages.every(x=>x.actual_evidence===null));eq(capture.current_queries,0);eq(capture.current_host_reads,0);eq(capture.current_body_captures,0);eq(capture.build_or_engine_or_setup_authority,false);
for(const v of Object.values(capture.future_results))eq(v,null);
const prepared={};for(const n of ['query_frontier.js','QUERY_FRONTIER.json','INTERFACE.disabled.json','SELECTOR_OBLIGATIONS.json','CAPTURE_CONTRACT.json','SOURCE_ORIGIN.json','OLD_TEX_MECHANISM.json','ORIGINAL_READS_NATIVE.json','HISTORICAL_LOCK_DOCUMENT_NATIVE.json','PLAN.md','inspect_preparation.js'])prepared[n]=identity(read(BASE+'/'+n));
const originalPins={...reads};
for(const[p,k]of Object.entries(originalPins))eq({...identity(read(p)),resolved:p,symlink:null},k);
const result={status:'SOURCE_ONLY_STAGED_DEPENDENCY_PREPARATION_VALID_NOT_QUERY_OR_LOCK',checks,workspace_input_paths:Object.keys(reads).length,old_preparation:oldPrep,old_source_audit:oldAudit,source_pairs:8,source_bytes:19659,whole_original_source_read_bindings:sourceBindings,whole_archived_graph_projection_received:true,whole_historical_lock_projection_received:true,historical_gap:gap,first_frontier_names:19,first_frontier_command_proposals:53,actual_dependency_queries:0,current_host_body_reads:0,query_emitter_executions:0,submitted_python_import_AST_compile:0,science_build_setup_PDF_queries:0,new_dependency_lock:null,root_authority:false,independent_review:false,prepared_files:prepared,workspace_pins:reads};
process.stdout.write(JSON.stringify(result,null,2)+'\n');
