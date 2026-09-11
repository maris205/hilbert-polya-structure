'use strict';
// Documentary root reception only: no scientific enumeration or submitted-code execution.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),cp=require('child_process');
const ROOT='/root/autodl-tmp/symbolic_dynamics',OUT=__dirname;
const DIR=path.join(ROOT,'docs/papers211_215_sequence/scouting/finite_orientation_residual_scout01');
const SCI=path.join(ROOT,'docs/papers211_215_sequence/scouting');
const labels=[],key={},commands=[];
function need(v,s){if(!v)throw Error(s);labels.push(s);}
function sha(b){return crypto.createHash('sha256').update(b).digest('hex');}
function rich(p){const a=fs.lstatSync(p,{bigint:true}),s=fs.statSync(p,{bigint:true});return {path:p,resolved:fs.realpathSync(p),link:a.isSymbolicLink()?fs.readlinkSync(p):null,lmode:String(a.mode),mode:String(s.mode),nlink:String(s.nlink),bytes:Number(s.size),mtime_ns:String(s.mtimeNs),sha256:sha(fs.readFileSync(p))};}
function read(p){p=path.isAbsolute(p)?p:path.join(ROOT,p);const r=rich(p);need(fs.statSync(p).isFile(),'regular:'+p);if(key[p])need(JSON.stringify(key[p])===JSON.stringify(r),'repeat_same:'+p);key[p]=r;return fs.readFileSync(p);}
function json(p){return JSON.parse(read(p));}
function save(n,j){fs.writeFileSync(path.join(OUT,n),JSON.stringify(j,null,2)+'\n',{flag:'wx'});}
function list(n,base,count,complete){const out={};for(const l of read(n).toString().trimEnd().split('\n')){const m=l.match(/^([a-f0-9]{64})  (.+)$/);need(!!m,'manifest_line:'+n);need(!(m[2]in out)&&!m[2].split('/').includes('..'),'unique_safe:'+m[2]);out[m[2]]=m[1];need(sha(read(path.join(base,m[2])))===m[1],'pin:'+m[2]);}need(Object.keys(out).length===count,'exact_pin_count:'+n);if(complete){const members=fs.readdirSync(base).sort();need(JSON.stringify(members)===JSON.stringify([...Object.keys(out),path.basename(n)].sort()),'exact_complete_nonself_members');for(const m of members){const p=path.join(base,m),s=fs.lstatSync(p);need(s.isFile()&&!s.isSymbolicLink()&&s.nlink===1,'ordinary_singlelink:'+m);read(p);}}return out;}
function bytes(ids,files,records){const actual=Buffer.concat(ids.map(i=>Buffer.from(records[i].result.output)));const expected=Buffer.concat(files.map(p=>read(p)));need(actual.equals(expected),'actual_whole_cat:'+ids.join(','));return {ids,bytes:actual.length,sha256:sha(actual)};}
function lines(p,a,z){return Buffer.concat(read(p).toString().match(/[^\n]*\n|[^\n]+$/g).slice(a-1,z).map(s=>Buffer.from(s)));}
function native(argv,cwd,expect){const i=commands.length,request={argv,cwd,timeout_ms:60000,shell:false,environment:process.env};save('COMMAND_'+i+'_ATTEMPT.json',request);const r=cp.spawnSync(argv[0],argv.slice(1),{cwd,encoding:null,timeout:60000,input:Buffer.alloc(0)});need(!r.error&&!r.signal,'native_completed:'+i);for(const s of ['stdout','stderr'])fs.writeFileSync(path.join(OUT,'COMMAND_'+i+'_'+s+'.bin'),r[s],{flag:'wx'});const record={request,exit_code:r.status,stdout:{bytes:r.stdout.length,sha256:sha(r.stdout)},stderr:{bytes:r.stderr.length,sha256:sha(r.stderr)}};save('COMMAND_'+i+'_NATIVE.json',record);commands.push(record);need(r.status===expect&&r.stderr.length===0,'native_expected:'+i);return r.stdout;}
need(!fs.existsSync(path.join(OUT,'RESULT.json')),'fresh_result');read(__filename);
const seal=list(path.join(DIR,'SHA256SUMS'),DIR,7,true);need(sha(read(path.join(DIR,'SHA256SUMS')))==='67dec3bbc3ce1ef6d6dbdcad7072be3e1731f67899843004ae97d86cd2a03b42','exact_delivered_seal');
need(Object.keys(seal).reduce((n,p)=>n+read(path.join(DIR,p)).length,0)===174244,'exact_payload_bytes');
list(path.join(DIR,'INPUTS.sha256'),ROOT,12,false);
const reads=json(path.join(DIR,'NATIVE_READS.json')),checks=json(path.join(DIR,'CHECKS_NATIVE.json')),browser=json(path.join(DIR,'BROWSER_METADATA.json'));
need(reads.records.length===12&&checks.records.length===2&&browser.records.length===9,'actual_record_censuses');
for(const [group,rows]of [['read',reads.records],['check',checks.records]])for(const[i,r]of rows.entries()){need(typeof r.request.cmd==='string'&&typeof r.result.output==='string'&&typeof r.result.chunk_id==='string'&&!('session_id'in r.result),'complete_envelope:'+group+i);need(r.result.exit_code===(group==='read'&&i===7?1:0),'preserved_exit:'+group+i);need(!r.result.output.startsWith('Warning: truncated output'),'native_return_not_truncated:'+group+i);}
const r=reads.records,binding=[];
binding.push(bytes([2],['papers/112-tournament-score-upset-reversal/main.tex','papers/145-random-vertex-push-orientation-chain/main.tex'],r));
binding.push(bytes([3],['finite_graph_rewiring_desk01/HANDOFF.md','finite_graph_memory_fresh_desk/HANDOFF.md','tree_order_lane/HANDOFF.md'].map(p=>path.join(SCI,p)),r));
binding.push(bytes([4],['tree_order_lane/SOURCE_AND_COLLISION.md','finite_graph_rewiring_desk01/INTAKE.md','finite_graph_rewiring_desk01/PROOF_PACKAGE.md'].map(p=>path.join(SCI,p)),r));
need(Buffer.from(r[5].result.output).equals(lines('papers/195-odd-side-least-neighbor-trees/main.tex',1,235)),'entire_native_P195_first_range');
binding.push(bytes([9],['docs/papers211_215_sequence/P211_REVIEW_CONTRACT.md'],r));
const lar=lines(path.join(SCI,'tree_order_lane/PROOF_PACKAGE.md'),1,95),tail=lines('papers/195-odd-side-least-neighbor-trees/main.tex',235,325),p212=read('docs/papers211_215_sequence/P212_THEOREM_CONTRACT.md');
const missing=Buffer.from('cat: docs/papers211_215_sequence/P211_THEOREM_CONTRACT.md: No such file or directory\n');
need(Buffer.from(r[7].result.output).equals(Buffer.concat([lar,tail,missing,p212])),'entire_actual_failed_combined_read_with_missing_path');
need(Buffer.from(r[11].result.output).equals(read(path.join(DIR,'INPUTS.sha256'))),'entire_original_input_pin_stdout');
const recheck=JSON.parse(checks.records[1].result.output);need(recheck.actual_native_byte_pairs.length===5&&recheck.scientific_invocations===0,'actual_old_documentary_census');
for(const p of recheck.actual_native_byte_pairs){const row=r.find(x=>x.key===p.key);need(!!row&&Buffer.byteLength(row.result.output)===p.bytes&&p.raw_equal===true,'old_actual_byte_pair:'+p.key);}
need(browser.archive_status==='DERIVED_REQUEST_AND_ACCESS_METADATA_ONLY_NOT_COMPLETE_PROVIDER_OUTPUTS','browser_metadata_not_full_bodies');
need(browser.records.reduce((n,x)=>n+(x.request.search_query||[]).length,0)===16,'sixteen_search_formulations');
need(browser.records.reduce((n,x)=>n+(x.request.open||[]).length,0)===7,'seven_opens');
for(const b of browser.records){need(b.response_kind==='DERIVED_CANDID_SELECTED_METADATA_NOT_FULL_NATIVE_RESPONSE'&&b.actual_original_response_type==='string'&&Number.isInteger(b.actual_original_response_char_count)&&b.actual_original_response_char_count>0,'candid_derived_scope:'+b.key);}
for(const n of ['HANDOFF.md','PROOF_PACKAGE.md','SOURCES_AND_SUBTRACTION.md'])for(const m of read(path.join(DIR,n)).toString().matchAll(/\]\(([^)]+)\)/g)){if(/^https?:/.test(m[1]))continue;need(fs.statSync(path.resolve(DIR,m[1])).isFile(),'local_link:'+m[1]);}
native(['/usr/bin/sha256sum','-c','SHA256SUMS'],DIR,0);
native(['/usr/bin/sha256sum','-c',path.join(DIR,'INPUTS.sha256')],ROOT,0);
for(const[p,v]of Object.entries(key))need(JSON.stringify(rich(p))===JSON.stringify(v),'entire_rich_key_before_after:'+p);
const result={status:'PASS_ZERO_LITERAL_NEGATIVE_DESK_ARTIFACT_RECEPTION',checks:labels.length,labels,input_count:Object.keys(key).length,input_key:key,cat_bindings:binding,native:commands,scientific_executions:0,new_literal_proposals:0,reserves:0,limits:'Documentary originals and direct proof/source reception; source browser metadata is not nine full bodies. No global novelty, manuscript review, canonical, build/view or admission claim.'};save('RESULT.json',result);console.log(JSON.stringify({status:result.status,checks:result.checks,input_count:result.input_count,result_bytes:fs.statSync(path.join(OUT,'RESULT.json')).size,result_sha256:sha(fs.readFileSync(path.join(OUT,'RESULT.json')))}));
