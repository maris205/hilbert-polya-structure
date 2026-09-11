'use strict';
// Root original receiver: fixed workspace-only bytes and archived native records.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),util=require('util');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa';
const OWN=QA+'/p211_terminal_entry_independent_root01',AUD=QA+'/p211_terminal_entry_independent_audit01';
const F=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs'];
let checks=0;const inputs={};
function need(x,m){checks++;if(!x)throw Error(m)}
function eq(a,b,m){need(util.isDeepStrictEqual(a,b),m)}
function pin(b){return {bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')}}
function read(p){need(p.startsWith(ROOT+'/')&&path.normalize(p)===p,'workspace literal');let q=ROOT;
 for(const n of path.relative(ROOT,p).split('/')){q+='/'+n;need(!fs.lstatSync(q).isSymbolicLink(),'no host alias')}
 const l=fs.lstatSync(p,{bigint:true}),s=fs.statSync(p,{bigint:true});need(l.isFile()&&s.isFile()&&l.nlink===1n&&fs.realpathSync(p)===p,'ordinary physical file');
 const b=fs.readFileSync(p),v={...pin(b),stat:F.map(k=>s[k].toString()),lstat:F.map(k=>l[k].toString())};
 eq(F.map(k=>fs.statSync(p,{bigint:true})[k].toString()),v.stat,'stable exact stat');eq(F.map(k=>fs.lstatSync(p,{bigint:true})[k].toString()),v.lstat,'stable exact lstat');
 need(BigInt(b.length)===s.size,'complete read');if(inputs[p])eq(v,inputs[p],'all repeated input bytes/metadata');inputs[p]=v;return b;}
function obj(p){return JSON.parse(read(p))}
function settled(r){need(r.exit_code===0&&!Object.hasOwn(r,'session_id')&&typeof r.output==='string','actual settled native');}
function lines(t){return t.match(/[^\n]*\n|[^\n]+$/g)||[]}
function sed(v){settled(v.result);const m=/^sed -n '(\d+),(\d+)p' (\S+)$/.exec(v.request.cmd);need(!!m,'exact sed request');
 const text=read(ROOT+'/'+m[3]).toString();eq(v.result.output,lines(text).slice(Number(m[1])-1,Number(m[2])).join(''),'whole original source slice bytes');}
function numbered(t){return lines(t).map((s,i)=>String(i+1).padStart(6,' ')+'\t'+s).join('');}
function main(){
 read(OWN+'/receive.js');read(OWN+'/SCOPE.md');read(OWN+'/NAVIGATION_LIMITS.md');
 const manifest=read(AUD+'/SHA256SUMS').toString(),names=[];for(const line of manifest.trimEnd().split('\n')){
 const m=/^([a-f0-9]{64})  ([^/]+)$/.exec(line);need(!!m&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'unique nonself audit manifest');
 names.push(m[2]);eq(pin(read(AUD+'/'+m[2])).sha256,m[1],'every entire independent payload');}
 need(names.length===10,'all10 payloads');eq(names,[...names].sort(),'canonical seal order');eq(fs.readdirSync(AUD).sort(),[...names,'SHA256SUMS'].sort(),'complete11-file audit tree');
 const pn=obj(AUD+'/NATIVE_CHECK.json'),cn=obj(AUD+'/NATIVE_CLOSURE.json');
 eq(pn.request.cmd,'node '+AUD+'/audit.js','actual old metadata command');eq(cn.request.cmd,'node '+AUD+'/closing.js','actual old closure command');
 need(pn.result.session_id===87717&&pn.result.output===''&&!Object.hasOwn(pn.result,'exit_code'),'actual yielded independent handle');
 eq(pn.poll_request,{session_id:87717,chars:'',max_output_tokens:200000,yield_time_ms:1000},'exact poll continuity');settled(pn.poll_result);settled(cn.result);
 const originals=[pn.poll_result.output,cn.result.output],pairs=[];
 for(let i=0;i<2;i++){const role=i?'closing':'audit',rn=obj(OWN+'/'+role.toUpperCase()+'_RECHECK_NATIVE.json');
 eq(rn.request,{cmd:'/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/node '+AUD+'/'+role+'.js',workdir:ROOT,shell:'/usr/bin/bash',login:false,max_output_tokens:400000,yield_time_ms:1000},'exact root metadata request');
 const last=rn.results.at(-1);settled(last);if(i===0){need(rn.results.length===2&&rn.results[0].session_id===50083&&rn.results[0].output===''&&!Object.hasOwn(rn.results[0],'exit_code'),'root owned initial handle');eq(rn.poll_requests,[{session_id:50083,chars:'',yield_time_ms:1000,max_output_tokens:400000}],'exact root poll');}
 else{need(rn.results.length===1,'one settled closure');eq(rn.poll_requests,[],'no invented poll');}
 const raw=Buffer.from(rn.results.map(x=>x.output).join(''));need(raw.equals(Buffer.from(originals[i])),'whole original/raw output equal; no JSON normalization');
 const v=JSON.parse(originals[i]);need(v.checks===(i?21995:1313460)&&v.inputs_count===(i?858:847),'exact actual count');
 eq(v.stat_array_fields,F,'full stat fields');need(Object.keys(v.inputs).length===v.inputs_count,'entire input census');
 for(const [p,k]of Object.entries(v.inputs)){read(p);eq(inputs[p],k,'all original rich input keys unchanged');}
 pairs.push({role,checks:v.checks,inputs:v.inputs_count,stdout:pin(raw),raw_equal:true});}
 const first=obj(AUD+'/NATIVE_SOURCE_READS.json').records;need(first.length===8,'all8 original source reads');for(const v of first)sed(v);
 const later=obj(AUD+'/CLOSING_SOURCE_READS.json').records;need(later.length===9,'all9 closing reads');
 for(const i of [0,1,3,4,5,6,8])sed(later[i]);
 settled(later[2].result);eq(later[2].result.output.trimEnd().split('\n').sort(),fs.readdirSync(QA+'/p211_terminal_enable_root01/entry_source02').map(n=>'docs/papers211_215_sequence/qa/p211_terminal_enable_root01/entry_source02/'+n).sort(),'all rg members, sorting explicitly not raw equality');
 settled(later[7].result);const ns=['ORIGINAL_SOURCE_READ_NATIVE.json','SOURCE_READ_NATIVE.json'];let expected='';
 for(const n of ns){const o=obj(QA+'/p211_terminal_enable_root01/entry_source02/'+n);
 expected+=JSON.stringify({n,fields:Object.keys(o),request:o.request,result:o.result?{...o.result,output:{bytes:Buffer.byteLength(o.result.output),first:o.result.output.slice(0,130),last:o.result.output.slice(-100)}}:o},null,2)+'\n';}
 eq(later[7].result.output,expected,'full source metadata navigation output');
 const second=obj(AUD+'/SECOND_LOOK_NATIVE.json');need(Object.keys(second).length===12,'all12 secondlook bodies');for(const v of Object.values(second))settled(v.result||v);
 need(second.entry_static_gate_0.result.output.startsWith('Warning: truncated output'),'old navigation truncation preserved');
 eq(second.entry_static_precheck_full.result.output,numbered(read(QA+'/p211_terminal_enable_root01/entry_source01/precheck.js').toString()),'entire numbered118 source read');
 eq([1,2,3,4].map(n=>second['entry_static_controller_'+n].result.output).join(''),numbered(read(QA+'/p211_terminal_enable_preparation01/terminal_control.py').toString()),'entire numbered724 source read');
 const pre=obj(AUD+'/PRESEAL_NATIVE.json');for(const k of ['first_workspace_preseal','secondlook_schema_navigation','final_preseal'])settled(pre[k].result);
 for(const k of ['first_workspace_preseal','final_preseal']){let v=JSON.parse(pre[k].result.output),pp=v.payload_pins||v.payloads;need(Object.keys(pp).length===9,'full9 historical preseal payloads');for(const [n,p]of Object.entries(pp))eq(pin(read(AUD+'/'+n)),p,'unchanged complete historical preseal payloads');need(v.closed_rich_inputs===858,'full declared closure scope');}
 const findings=obj(AUD+'/FINDINGS.json');eq(findings.actual_refresh_defects,{critical:0,major:0,minor:0},'actual firstrefresh only zero defects');eq(findings.findings.map(x=>x.id),['F1','L1','L2','L3'],'all limitations retained');
 const namesNow=Object.keys(inputs);for(const p of namesNow)read(p);need(Object.keys(inputs).length===namesNow.length,'full endpoint census');
 console.log(JSON.stringify({status:'ROOT_ACCEPTED_INDEPENDENT_FIRST_REFRESH_ENTRY_ORIGINALS_ONLY',checks,inputs_count:namesNow.length,independent_payloads:10,metadata_reuses:pairs,original_source_native_records:17,secondlook_native_records:12,preseal_native_records:3,inputs,stat_array_fields:F,host_observations:0,new_controller_invocations:0,new_science:0,new_builds:0,new_page_views:0,cold_artifact_acceptance:false,manuscript_review:false,paper_complete:false,external:'OWNER_AMBER / HOLD_EXTERNAL'}));
}
try{main()}catch(e){console.error(e.stack);process.exitCode=1}
