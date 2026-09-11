'use strict';
// Root documentary receiver only. No submitted import/AST/probe/Git/host reads.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),util=require('util');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const QA='docs/papers211_215_sequence/qa/';
const P=QA+'private_checkpoint_executor_preparation03';
const A=QA+'private_checkpoint_executor_source_audit03';
const C=A+'/git_phase_consult01';
const R=QA+'private_checkpoint_executor_source_root03';
const OLD=QA+'private_checkpoint_preparation02/checkpoint.py';
let checks=0; const keys=new Map(),bodies=new Map(),evidence=[];
function need(x,m){checks++;if(!x)throw Error(m);}
const eq=util.isDeepStrictEqual;
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const sk=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
function safe(n){need(typeof n==='string'&&/^[A-Za-z0-9_.\/-]+$/.test(n)&&!n.startsWith('/')&&n.split('/').every(x=>x&&x!=='.'&&x!=='..'),'unsafe documentary name '+n);return n;}
function obtain(n){
 safe(n);const p=ROOT+'/'+n;need(fs.realpathSync.native(p)===p,'alias '+n);
 const a=fs.lstatSync(p,{bigint:true});need(a.isFile()&&!a.isSymbolicLink(),'nonregular '+n);
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 let b,c,raw;try{b=fs.fstatSync(fd,{bigint:true});raw=fs.readFileSync(fd);c=fs.fstatSync(fd,{bigint:true});}finally{fs.closeSync(fd);}
 const d=fs.lstatSync(p,{bigint:true});const marks=[a,b,c,d].map(sk);
 need(marks.every(x=>eq(x,marks[0]))&&fs.realpathSync.native(p)===p&&BigInt(raw.length)===a.size,'unstable complete read '+n);
 const v={path:n,bytes:raw.length,sha256:sha(raw),stat:marks[0],four_keys_equal:true,physical:true};
 if(keys.has(n))need(eq(keys.get(n),v),'repeat drift '+n);
 keys.set(n,v);bodies.set(n,raw);return raw;
}
const json=n=>JSON.parse(obtain(n).toString('utf8'));
function names(n){const out=[];safe(n);need(fs.realpathSync.native(ROOT+'/'+n)===ROOT+'/'+n,'directory alias');for(const e of fs.readdirSync(ROOT+'/'+n,{withFileTypes:true})){const p=n+'/'+e.name;need(!e.isSymbolicLink(),'package alias');if(e.isDirectory())out.push(...names(p));else{need(e.isFile(),'nonregular package');out.push(p);}}return out.sort();}
function pins(n,base=null){const raw=obtain(n).toString();need(raw.endsWith('\n'),'no final LF '+n);const rows=raw.slice(0,-1).split('\n').map(line=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.\/-]+)$/.exec(line);need(m,'bad manifest row');return{path:base?base+'/'+safe(m[2]):safe(m[2]),sha256:m[1]};});need(new Set(rows.map(x=>x.path)).size===rows.length,'duplicate pin');for(const r of rows)need(sha(obtain(r.path))===r.sha256,'pin mismatch '+r.path);return rows;}
function seal(n,count,digest){need(sha(obtain(n+'/SHA256SUMS'))===digest,'changed sealed input '+n);const rows=pins(n+'/SHA256SUMS',n);need(rows.length===count&&eq(names(n),rows.map(x=>x.path).concat(n+'/SHA256SUMS').sort()),'incomplete nonself seal '+n);return{path:n,payload:rows.length,files:rows.length+1,bytes:rows.reduce((s,x)=>s+keys.get(x.path).bytes,0),seal_sha256:digest};}
const seals=[seal(P,19,'c10cbafe54725530bd7dc359b9c951d29e983496e557f09adfc7ba1a5f17f4d0'),seal(A,41,'6de3b00a4ef8b221422c07744bd7a3c7f678f2f9963ba784333ba7abf2862cbc'),seal(C,5,'7825edfcebc1fd996c02a22ae9a017844213f7846f0c0b5a5802257491c67a0d')];
const pinsets=[pins(P+'/REVIEW_INPUTS.sha256'),pins(P+'/SOURCE_INPUTS.sha256'),pins(A+'/INPUT_PINS.sha256'),pins(C+'/INPUT_PINS.sha256')];
need(eq(pinsets.map(x=>x.length),[12,15,40,16]),'input pin census');
for(const n of ['ROOT_SOURCE_READS_NATIVE.json','ROOT_DIFF_NATIVE.json','PRIMARY_READS.json','receive.cjs','receive02.cjs','FAILED_RECEIVE01_NATIVE.json'])obtain(R+'/'+n);
function native(n){const x=json(n);need(x.result&&typeof x.result.output==='string'&&x.result.exit_code===0&&typeof x.result.chunk_id==='string'&&!x.result.session_id&&!x.result.output.startsWith('Warning: truncated output'),'incomplete native '+n);return JSON.parse(x.result.output);}
const before=native(A+'/INPUTS_BEFORE_V2_NATIVE.json'),after=native(A+'/INPUTS_AFTER_V2_NATIVE.json');
need(before.inputs.length===40&&eq(before,after),'independent full forty-key interval');
for(const v of before.inputs){obtain(v.path);need(eq(keys.get(v.path),v),'independent before/current ten-field key '+v.path);}
function records(x,out=[]){if(x&&typeof x==='object'){if(x.request&&x.result&&typeof x.request.cmd==='string'&&typeof x.result.output==='string')out.push(x);else if(Array.isArray(x))for(const v of x)records(v,out);else for(const v of Object.values(x))records(v,out);}return out;}
function rawResult(r,expected,exit=0){need(r.result.exit_code===exit&&typeof r.result.chunk_id==='string'&&!r.result.session_id,'native status');need(Buffer.from(r.result.output).equals(expected),'complete native raw bytes '+r.result.chunk_id);}
function slice(n,lo,hi){const raw=obtain(n),ls=raw.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];return Buffer.from(ls.slice(lo-1,hi).join(''));}
function sourceSet(recordName,target,count){const rr=records(json(recordName));need(rr.length===count,'source native count');for(const r of rr){const m=/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_.\/-]+)$/.exec(r.request.cmd);need(m&&m[3]===target,'wrong source native request');rawResult(r,slice(target,+m[1],+m[2]));}need(Buffer.concat(rr.map(x=>Buffer.from(x.result.output))).equals(obtain(target)),'whole source native coverage');evidence.push({record:recordName,target,complete_native_reads:count,bytes:keys.get(target).bytes});}
sourceSet(A+'/NEW_EXECUTOR_READS_NATIVE.json',P+'/checkpoint.py',4);
sourceSet(A+'/OLD_EXECUTOR_READS_NATIVE.json',OLD,4);
const authorFinal=records(json(P+'/FINAL_SOURCE_READS_NATIVE.json'));need(authorFinal.length===12,'author final twelve reads');
for(const r of authorFinal){const m=/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_.\/-]+)$/.exec(r.request.cmd);need(m&&keys.has(m[3]),'author selected read');rawResult(r,slice(m[3],+m[1],+m[2]));}
need(Buffer.concat(authorFinal.slice(0,3).map(x=>Buffer.from(x.result.output))).equals(obtain(P+'/checkpoint.py')),'author whole source');
const diff=obtain(P+'/EXECUTOR.diff');
for(const n of [P+'/EXECUTOR_DIFF_NATIVE.json',A+'/INDEPENDENT_DIFF_NATIVE.json']){const rr=records(json(n));need(rr.length===1,'exact diff result');rawResult(rr[0],diff,1);}
const rootDiff=json(R+'/ROOT_DIFF_NATIVE.json');rawResult(rootDiff.actual_diff,diff,1);rawResult(rootDiff.saved_diff_read,diff);
const rootReads=records(json(R+'/ROOT_SOURCE_READS_NATIVE.json'));
for(const r of rootReads){const m=/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_.\/-]+)$/.exec(r.request.cmd);need(m&&keys.has(m[3]),'root selected read');rawResult(r,slice(m[3],+m[1],+m[2]));}
const rootNew=rootReads.filter(x=>x.request.cmd.endsWith(P+'/checkpoint.py')),rootOld=rootReads.filter(x=>x.request.cmd.endsWith(OLD));
need(Buffer.concat(rootNew.map(x=>Buffer.from(x.result.output))).equals(obtain(P+'/checkpoint.py'))&&Buffer.concat(rootOld.map(x=>Buffer.from(x.result.output))).equals(obtain(OLD)),'root full direct old/new text');
const nativeIndex=[],matched=[];
for(const dir of [P,A])for(const n of names(dir).filter(n=>n.endsWith('.json'))){const rr=records(json(n));for(const r of rr){const v={record:n,chunk:r.result.chunk_id||null,exit:r.result.exit_code??null,session:r.result.session_id??null,output_bytes:Buffer.byteLength(r.result.output),truncated:r.result.output.startsWith('Warning: truncated output')};nativeIndex.push(v);const m=/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_.\/ -]+)$/.exec(r.request.cmd);if(m&&r.result.exit_code===0&&!v.truncated){const targets=m[3].split(' ');if(targets.every(n=>keys.has(n))){const combined=Buffer.concat(targets.map(obtain)).toString('utf8');const lines=combined.match(/[^\n]*\n|[^\n]+$/g)||[];const expected=Buffer.from(lines.slice(+m[1]-1,+m[2]).join(''));rawResult(r,expected);matched.push({...v,targets});}}}}
const summary=json(A+'/SUMMARY.json');need(summary.blocking_source_findings.length===0&&summary.material_boundaries.length===5&&summary.operational.git_calls===0&&summary.operational.checkpoint_invocation===false,'audit verdict scope');
const consult=json(C+'/FINDINGS.json');need(consult.blocking_findings.length===0&&consult.informational_boundaries.length===5&&consult.claim_limits.git_or_ssh_commands===0,'consult scope');
const chosen=json(QA+'private_checkpoint03_scope_root01/CHOSEN_SCOPE.json');need(chosen.inventory.length===8207&&chosen.counts.bytes===386716363&&chosen.status==='ROOT_SOURCE_SCOPE_SELECTED_NOT_OPERATIVE_AUTHORITY','chosen accepted data interface');
const mapping=json(QA+'control_before_residual46_accepted01/MAPPING.json');for(const row of mapping.rows){obtain(row.copy);need(keys.get(row.copy).bytes===row.bytes&&keys.get(row.copy).sha256===row.sha256,'exact physical controls');const c=chosen.inventory.find(x=>x.git_path===row.original);need(c&&c.source_path===ROOT+'/'+row.copy&&c.bytes===row.bytes&&c.sha256===row.sha256,'chosen control mapping');}
for(const phase of ['capture','stage','commit','push']){const b=json(P+'/bindings/'+phase+'.disabled.json');need(b.phase===phase&&b.enabled===false&&b.status==='SOURCE_ONLY_NOT_AUTHORITY'&&b.source_receipt===null&&b.runtime_receipt===null,'author example enabled');}
const entries=[...keys.values()].sort((a,b)=>a.path.localeCompare(b.path));for(const v of entries){obtain(v.path);need(eq(v,keys.get(v.path)),'root endpoint key drift');}
for(const s of seals)need(eq(names(s.path),[...bodies.keys()].filter(n=>n.startsWith(s.path+'/')).sort()),'final exact package membership');
const result={schema:'checkpoint03-root-source-original-reception-v1',status:'PASS_ROOT_DOCUMENTARY_INPUT_RECEPTION_NOT_OPERATION',checks,seals,pin_counts:pinsets.map(x=>x.length),independent_full_key_count:before.inputs.length,root_full_key_count:entries.length,author_final_raw_reads:authorFinal.length,root_actual_raw_reads:rootReads.length,source_native_coverage:evidence,diff_bytes:diff.length,diff_sha256:sha(diff),complete_source_native_raw_matches:matched.length,native_index:nativeIndex,matched_source_reads:matched,inputs:entries,limits:['source-only opinion; no runtime/startup/protected-role acceptance','five audit boundaries remain operative prerequisites','current selected payload not re-received; prior root scope acceptance reused','no code import/AST/probe/Git/checkpoint/science/build','ten-field documentary key excludes atime and is not P212 statx fourteen-field interface','actual private scope remains older43; current48/P212 excluded'],hold_operational:true,hold_external:true};
console.log(JSON.stringify(result,null,2));
