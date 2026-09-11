// Root documentary receiver derived transparently from the fully read independent preseal metadata source.
// No submitted builder/scientific imports, host lookups, ambient probes or child process. All writes are the product-captured stdout only.
const fs=require('node:fs'),crypto=require('node:crypto'),util=require('node:util');
const ROOT='/root/autodl-tmp/symbolic_dynamics',B='docs/papers211_215_sequence/qa/p212_initial_build_source_audit01/',P='docs/papers211_215_sequence/qa/p212_initial_build_preparation01/';
const READ_INPUTS={},RICH_INPUTS={};
let checks=0;const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
function need(x,s){checks++;if(!x)throw Error(s);}function eq(a,b,s){need(util.isDeepStrictEqual(a,b),s);}
function read(n){need(!n.startsWith('/')&&n.split('/').every(x=>x&&x!=='.'&&x!=='..'),'workspace only');let p=ROOT;for(const t of n.split('/')){p+='/'+t;need(!fs.lstatSync(p).isSymbolicLink(),'no alias');}const a=fs.lstatSync(p,{bigint:true}),b=fs.readFileSync(p),z=fs.lstatSync(p,{bigint:true});need(a.isFile(),'ordinary');const m=s=>Object.fromEntries(['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'].map(k=>[k,String(s[k])]));eq(m(a),m(z),'full stat stable');const rich={...pin(b),resolved:p,symlink:null,stat_decimal_strings:m(a)}; if(READ_INPUTS[n])eq(rich,RICH_INPUTS[n],'repeated root exact input');READ_INPUTS[n]=pin(b);RICH_INPUTS[n]=rich;return {raw:b,rich};}const raw=n=>read(n).raw,obj=n=>JSON.parse(raw(n));
const names=['PLAN.md','inspect_source.js','INSPECTION_NATIVE01.json','INSPECTION.stdout.raw','RESULT.json','inspect_source02.js','CORRECTION_NATIVE.json','run02/INSPECTION_NATIVE.json','run02/INSPECTION.stdout.raw','run02/RESULT.json','ORIGINAL_PINS.json','INPUTS.sha256','COMPARISON_NATIVE.json','NATIVE_READS.json','REPORT.md','FINDINGS.json'].sort();
let actual=[];for(const e of fs.readdirSync(ROOT+'/'+B,{withFileTypes:true})){if(e.isDirectory()){eq(e.name,'run02','sole directory');for(const q of fs.readdirSync(ROOT+'/'+B+e.name))actual.push(e.name+'/'+q);}else actual.push(e.name);}eq(actual.sort(),[...names,'PRESEAL_NATIVE.json','SHA256SUMS'].sort(),'exact18 frozen audit files');
const pins=Object.fromEntries(names.map(n=>[n,pin(raw(B+n))]));
const failed=obj(B+'INSPECTION.stdout.raw'),good=obj(B+'run02/INSPECTION.stdout.raw');
eq(failed.status,'FAIL_INDEPENDENT_SOURCE_METADATA_PRESERVE_ORIGINALS','failure remains');eq(failed.checks,1344,'real failure point');
eq(good.status,'PASS_INDEPENDENT_SOURCE_ONLY_PLAN_HOLD_OPERATIONAL','actual success');eq(good.checks,2476,'actual success count');eq(good.workspace_read_paths,40,'all40 current originals');
for(const [nativeName,stdoutName,resultName,expectedCode,sourceName]of [['INSPECTION_NATIVE01.json','INSPECTION.stdout.raw','RESULT.json',1,'inspect_source.js'],['run02/INSPECTION_NATIVE.json','run02/INSPECTION.stdout.raw','run02/RESULT.json',0,'inspect_source02.js']]){
 const n=obj(B+nativeName),output=raw(B+stdoutName),x=JSON.parse(output);eq(n.request.cmd,'env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/node '+B+sourceName,'exact original owned invocation');eq(n.result.exit_code,expectedCode,'actual exit');need(!n.result.session_id&&!n.result.output.startsWith('Warning: truncated output'),'complete actual result');eq(Buffer.from(n.result.output),output,'entire actual native output raw');eq(obj(B+resultName),Object.fromEntries(Object.entries(x).filter(([k])=>!['READ_INPUTS','RICH_INPUTS'].includes(k))),'whole compact projection');
}
eq(failed.READ_INPUTS,good.READ_INPUTS,'complete first-failure/current original byte map');eq(failed.RICH_INPUTS,good.RICH_INPUTS,'all original first/current rich metadata agrees');
const old=raw(B+'inspect_source.js').toString(),current=raw(B+'inspect_source02.js').toString();
const before="  need(util.isDeepStrictEqual(keys,['request','result']) || util.isDeepStrictEqual(keys,['path','request','result']),\n       'complete actual outer schema '+label);";
const after="  const originalMetadataEnvelope = label==='author_complete_metadata' &&\n    util.isDeepStrictEqual(keys,['request','result','scope']) &&\n    record.scope==='Actual author-side workspace metadata execution, not submitted-source execution or independent review.';\n  need(originalMetadataEnvelope || util.isDeepStrictEqual(keys,['request','result']) || util.isDeepStrictEqual(keys,['path','request','result']),\n       'complete actual outer schema '+label);";
eq(old.split(before).length,2,'one actual correction anchor');eq(old.replace(before,after),current,'whole only-original-envelope correction');
const correction=obj(B+'CORRECTION_NATIVE.json');eq(correction.result.exit_code,1,'actual source diff expected1');need(correction.result.output.startsWith('--- ')&&!correction.result.output.startsWith('Warning:'),'whole actual source diff');
const ip=obj(B+'ORIGINAL_PINS.json');eq(ip.pins,good.READ_INPUTS,'full40 input pin file');eq(ip.entries,40,'40 input rows');for(let pass=0;pass<2;pass++)for(const[n,v]of Object.entries(good.RICH_INPUTS))eq(read(n).rich,v,'all exact current40 original rich keys');
const mraw=raw(B+'INPUTS.sha256').toString(),mp={};for(const line of mraw.trimEnd().split('\n')){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);need(m&&m[2].startsWith(ROOT+'/'),'literal manifest');const n=m[2].slice(ROOT.length+1);need(!mp[n],'unique input');eq(good.READ_INPUTS[n].sha256,m[1],'exact original manifest pin');mp[n]=m[1];}eq(Object.keys(mp).sort(),Object.keys(good.READ_INPUTS).sort(),'complete40 native manifest scope');
const comparisons=obj(B+'COMPARISON_NATIVE.json');eq(comparisons.records.length,9,'all9 actual commands');for(let i=0;i<9;i++){const r=comparisons.records[i];eq(r.result.exit_code,0,'actual native comparison success');need(!r.result.session_id&&!r.result.output.startsWith('Warning:'),'complete comparison output');if(i<8){const p=good.source_pairs[i];eq(r.request.cmd,'/usr/bin/cmp -- '+p.current+' '+p.original,'exact actual source pair argv');eq(r.result.output,'','empty full actual raw cmp output');}else eq(r.result.output,mraw.trimEnd().split('\n').map(l=>l.slice(66)+': OK\n').join(''),'whole40 successful native sha output');}
const reads=obj(B+'NATIVE_READS.json');eq(reads.records.length,21,'all21 selected actual owned reads');const rr={};for(const r of reads.records){need(!rr[r.record_id],'unique saved own read');rr[r.record_id]=r;eq(r.result.exit_code,0,'actual owned navigation result0');need(!r.result.output.startsWith('Warning: truncated output'),'saved native read complete');}
function groups(ids){const result=[];for(const line of ids.map(id=>rr[id].result.output).join('').match(/[^\n]*\n|[^\n]+$/g)||[]){const m=/^ *(\d+)\t/.exec(line);if(!m)continue;const n=Number(m[1]);if(n===1)result.push([]);need(result.length&&n===result.at(-1).length+1,'complete own source numbering');result.at(-1).push(line.slice(line.indexOf('\t')+1));}return result.map(v=>Buffer.from(v.join('')));}
const oldBase='docs/papers211_215_sequence/qa/p211_initial_build_01/outer/executed_adapter/';
const specifications=[[['full_old_core'],0,oldBase+'build_core.py',299],[['full_old_builder_1','full_old_builder_2'],0,oldBase+'build_p211.py',407],[['full_old_launcher'],0,oldBase+'launch_build.py',174],[['full_old_selector_1','full_old_selector_tail_and_static'],0,oldBase+'prepare_build.py',278],[['full_old_selector_1','full_old_selector_tail_and_static'],1,oldBase+'static_checks.py',96]];
const a=['main.tex','math_commands.tex','references.bib','sections/01_setup.tex'],b=['sections/02_returns.tex','sections/03_period_set.tex','sections/04_census.tex','sections/05_scope.tex'];
for(let i=0;i<4;i++){specifications.push([['full_p212_sources_0'],i,'papers/212-closed-pointer-orbits/'+a[i],[34,8,43,75][i]]);specifications.push([['full_p212_sources_1'],i,'papers/212-closed-pointer-orbits/'+b[i],[91,30,94,12][i]]);}
const bindings=[];for(const[ids,index,path,lines]of specifications){const output=groups(ids)[index];eq(output,raw(path),'entire own source read original binding');eq(output.toString().split('\n').length-1,lines,'complete actual source lines');bindings.push({ids,index,path,lines,pin:pin(output)});}eq(bindings.length,13,'all13 complete owned source bodies');
const links=[];for(const href of raw(B+'REPORT.md').toString().matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){need(names.includes(href[1]),'report local link is exact preseal file');links.push({href:href[1],pin:pin(raw(B+href[1]))});}
const findings=obj(B+'FINDINGS.json');eq(findings.current_findings,{Critical:0,Major:0,Minor:0,total:0},'source-only findings census');eq(findings.operational_status,'HOLD_OPERATIONAL_NOT_EXECUTION_READY','no operational acceptance');need(!findings.root_authority&&!findings.executable_adapter_accepted&&!findings.paper_complete,'no unsupported authority');
for(const[n,p]of Object.entries(pins))eq(pin(raw(B+n)),p,'all16 own original bytes still stable');
const reconstructed={status:'PASS_COMPLETE_INDEPENDENT_SOURCE_AUDIT_PRESEAL_HOLD_OPERATIONAL',checks:4830,payloads:names.length,payload_bytes:Object.values(pins).reduce((s,v)=>s+v.bytes,0),payload_pins:pins,original_workspace_rows:40,whole_original_rich_key_passes:2,all_owned_attempts:2,preserved_failed_attempts:1,passing_checks:2476,actual_native_comparisons:9,selected_owned_native_reads:21,complete_owned_source_bindings:bindings,report_local_links:links,report_pin:pins['REPORT.md'],failed_source_pin:pins['inspect_source.js'],passing_source_pin:pins['inspect_source02.js'],allowed_next_appends:['PRESEAL_NATIVE.json','SHA256SUMS'],host_referent_reads:0,dependency_queries:0,submitted_code_execution:0,science:0,build:0,root_authority:false};
const OUR='docs/papers211_215_sequence/qa/p212_initial_build_source_root01/';
const presealNative=obj(B+'PRESEAL_NATIVE.json');
eq(presealNative.result.exit_code,0,'original preseal actual exit0');
eq(presealNative.result.chunk_id,'74c222','original actual preseal identity');
eq(Buffer.from(presealNative.result.output),Buffer.from(JSON.stringify(reconstructed,null,2)+'\n'),'entire archived4830 preseal output reconstruction');
const sealRaw=raw(B+'SHA256SUMS'),sealNames=[...names,'PRESEAL_NATIVE.json'].sort();
eq(sealRaw,Buffer.from(sealNames.map(n=>pin(raw(B+n)).sha256+'  '+n+'\n').join('')),'entire17payload original seal');
const rootRaw=raw(OUR+'ROOT_REPLAY.stdout.raw'),rootNative=obj(OUR+'ROOT_REPLAY_NATIVE.json'),rootResult=obj(OUR+'ROOT_REPLAY_RESULT.json');
eq(rootRaw,raw(B+'run02/INSPECTION.stdout.raw'),'whole actual fresh root2476 output byte-equal to independent result');
eq(Buffer.from(rootNative.result.output),rootRaw,'complete actual root native output binding');
eq(rootNative.request,{cmd:'env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/node '+B+'inspect_source02.js',workdir:ROOT,login:false,max_output_tokens:24000,yield_time_ms:1000},'exact actual root documentary invocation');
eq(rootNative.result.exit_code,0,'actual root exit0');
eq(rootNative.result.chunk_id,'db4d6c','actual root native identity');
need(!rootNative.result.session_id&&!rootNative.result.output.startsWith('Warning:'),'root final complete output no outstanding session');
eq(rootResult,Object.fromEntries(Object.entries(JSON.parse(rootRaw)).filter(([k])=>!['READ_INPUTS','RICH_INPUTS'].includes(k))),'whole root compact projection');
eq(rootResult,obj(B+'run02/RESULT.json'),'all independent/root compact semantic fields same');
const oldReads=obj(B+'NATIVE_READS.json');
for(const r of oldReads.records){
 eq(Object.keys(r.result).sort(),['chunk_id','exit_code','original_token_count','output','wall_time_seconds'],'all actual native result fields '+r.record_id);
 need(typeof r.request.cmd==='string'&&r.request.cmd&&typeof r.result.chunk_id==='string'&&Number.isInteger(r.result.original_token_count)&&r.result.wall_time_seconds>=0,'full saved actual source envelope '+r.record_id);
}
const sourcePath=OUR+'receive_audit.js';raw(sourcePath);raw(OUR+'SOURCE_DERIVATION.json');
for(let pass=0;pass<2;pass++)for(const[n,v]of Object.entries({...RICH_INPUTS}))eq(read(n).rich,v,'whole root current rich key '+n);
const result={status:'PASS_ROOT_P212_INITIAL_BUILD_SOURCE_PLAN_AND_ORIGINAL_AUDIT_ONLY',checks,
 source_profile:'article10pt/plain/array/T1;8sources19659bytes',
 documentary_replay:{checks:2476,workspace_files:40,complete_output:pin(rootRaw),native_chunk:'db4d6c',new_science_or_build:false},
 received_audit:{payloads:17,files:18,seal:pin(sealRaw),complete_preseal_checks_reconstructed:4830,originals:40,source_body_bindings:13,saved_own_reads:21,native_comparisons:9,preserved_failed_metadata_attempts:1},
 preparation:{payloads:11,files:12,original_inputs:28,whole_original_source_body_bindings:18,original_native_envelopes:22},
 source_only_plan_accepted:true,executable_adapter_accepted:false,dependency_lock_accepted:false,root_build_authority:false,
 scientific_executions:0,builds:0,renders:0,views:0,mathematical_manuscript_reviews:0,
 historical_section05_unchanged:true,operational_prerequisites:findings.operational_prerequisites,
 limitations:['Documentary point-in-time original-byte/stat checks, not operational runtime or OS-hermetic tracing.','Prior metadata logic is transparently derived, not an additional independent review.','Source plan accepts no future host selector or builder until separately read and bound.','All original failures and truncated/non-evidentiary navigation preserved.'],
 external:'OWNER_AMBER / HOLD_EXTERNAL',READ_INPUTS,RICH_INPUTS};
process.stdout.write(JSON.stringify(result,null,2)+'\n');
