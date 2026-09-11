'use strict';
// Auditor-owned documentary reader. No reviewed source is executed or parsed.
const fs=require('fs'),crypto=require('crypto'),cp=require('child_process'),path=require('path');
const ROOT='/root/autodl-tmp/symbolic_dynamics', QA='docs/papers211_215_sequence/qa/';
const A=QA+'p212_keyed_stdin_source_delta01', O=QA+'p212_keyed_stdin_source_audit01';
if(process.cwd()!==ROOT) throw Error('documentary cwd');
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const asserts=[];
function need(c,m){checks++; if(!c)throw Error(m);asserts.push(m);}
function meta(s){return Object.fromEntries(fields.map(k=>[k,s[k].toString()]));}
function raw(p){
 need(p.startsWith(QA)&&!p.includes('..')&&!path.isAbsolute(p)&&!p.includes('/p212_keyed_stdin_input01/'),'documentary path '+p);
 const a=fs.lstatSync(p,{bigint:true});need(a.isFile()&&!a.isSymbolicLink(),'documentary regular '+p);
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 try{const b=fs.fstatSync(fd,{bigint:true});need(JSON.stringify(meta(a))===JSON.stringify(meta(b)),'open key '+p);
 const data=fs.readFileSync(fd),c=fs.fstatSync(fd,{bigint:true}),d=fs.lstatSync(p,{bigint:true});
 need(BigInt(data.length)===c.size&&JSON.stringify(meta(b))===JSON.stringify(meta(c))&&JSON.stringify(meta(c))===JSON.stringify(meta(d)),'whole byte and key '+p);
 return{data,key:{path:p,sha256:sha(data),byte_count:data.length,...meta(c)}};}finally{fs.closeSync(fd);}
}
function read(p){return raw(p).data;}
function json(p){return JSON.parse(read(p).toString('utf8'));}
const inputEnvelope=json(O+'/INITIAL_KEYS_NATIVE.json');
const baseline=JSON.parse(inputEnvelope.record.result.output);
need(baseline.distinct_inputs===91&&baseline.input_keys.length===91,'91 initial documentary keys');
const inputKeys=baseline.input_keys.map(k=>{const got=raw(k.path).key;need(JSON.stringify(got)===JSON.stringify(k),'complete key unchanged '+k.path);return got;});
const origin=json(A+'/SOURCE_ORIGIN.json');need(origin.derivatives.length===19,'19 exact derivative pairs');
const diffs=[];let hunks=0,insertions=0,deletions=0;
for(const row of origin.derivatives){
 const oldB=read(row.old_path),newB=read(row.new_path);
 const old=oldB.toString('utf8'),neu=newB.toString('utf8');
 need(Buffer.from(old).equals(oldB)&&Buffer.from(neu).equals(newB)&&old.endsWith('\n')&&neu.endsWith('\n'),'entire UTF8 LF source '+row.name);
 const archive=A+'/diffs/'+row.name.replaceAll('/','__')+'.diff', archived=read(archive);
 const argv=['-u',row.old_path,row.new_path];
 const native=cp.spawnSync('diff',argv,{cwd:ROOT,encoding:null,maxBuffer:16777216});
 need(!native.error&&native.signal===null&&[0,1].includes(native.status),'actual diff return '+row.name);
 need(native.stderr.length===0&&native.stdout.equals(archived),'actual raw diff exact archived '+row.name);
 const diff=archived.toString('utf8');need(Buffer.from(diff).equals(archived),'whole diff UTF8 '+row.name);
 let cursor=0,result=[],localHunks=0,added=0,removed=0;
 const lines=diff?diff.slice(0,-1).split('\n'):[],before=old.slice(0,-1).split('\n'),after=neu.slice(0,-1).split('\n');
 if(diff){need(diff.endsWith('\n')&&lines[0].startsWith('--- '+row.old_path+'\t')&&lines[1].startsWith('+++ '+row.new_path+'\t'),'exact diff headers '+row.name);
 for(let i=2;i<lines.length;){const h=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(?:.*)$/.exec(lines[i++]);need(!!h,'hunk header '+row.name);
 const oldStart=Number(h[1])-1,oldCount=h[2]===undefined?1:Number(h[2]),newStart=Number(h[3])-1,newCount=h[4]===undefined?1:Number(h[4]);
 need(oldStart>=cursor&&oldCount>0&&newCount>0,'ordered nonempty complete hunk '+row.name);result.push(...before.slice(cursor,oldStart));cursor=oldStart;need(result.length===newStart,'new coordinate '+row.name);
 let oc=0,nc=0;while(i<lines.length&&!lines[i].startsWith('@@ ')){const line=lines[i++],tag=line[0],body=line.slice(1);need([' ','+','-'].includes(tag),'ordinary unified line '+row.name);
 if(tag!=='+' ){need(before[cursor]===body,'exact old hunk line '+row.name);cursor++;oc++;}if(tag!=='-'){result.push(body);nc++;}if(tag==='+')added++;if(tag==='-')removed++;}
 need(oc===oldCount&&nc===newCount,'exact hunk counts '+row.name);localHunks++;}
 result.push(...before.slice(cursor));need(Buffer.from(result.join('\n')+'\n').equals(newB),'entire reconstructed new source '+row.name);
 }else need(oldB.equals(newB),'zero diff entire bytes '+row.name);
 need((native.status===0)===oldB.equals(newB),'exit equality '+row.name);
 hunks+=localHunks;insertions+=added;deletions+=removed;
 diffs.push({name:row.name,old_path:row.old_path,new_path:row.new_path,old_lines:before.length,new_lines:after.length,old_bytes:oldB.length,new_bytes:newB.length,old_sha256:sha(oldB),new_sha256:sha(newB),hunks:localHunks,insertions:added,deletions:removed,request:{command:'diff',argv,cwd:ROOT},result:{status:native.status,signal:native.signal,stdout:native.stdout.toString('utf8'),stderr:native.stderr.toString('utf8'),stdout_bytes:native.stdout.length,stderr_bytes:native.stderr.length}});
}
const programs=diffs.filter(r=>/\.(py|js)$/.test(r.name));need(programs.length===7,'seven programs');
const sums=rs=>({old_lines:rs.reduce((n,r)=>n+r.old_lines,0),new_lines:rs.reduce((n,r)=>n+r.new_lines,0),old_bytes:rs.reduce((n,r)=>n+r.old_bytes,0),new_bytes:rs.reduce((n,r)=>n+r.new_bytes,0),hunks:rs.reduce((n,r)=>n+r.hunks,0),insertions:rs.reduce((n,r)=>n+r.insertions,0),deletions:rs.reduce((n,r)=>n+r.deletions,0)});
need(sums(programs).new_lines===2679&&sums(programs).new_bytes===148546,'independent corrected program counts');
need(sums(diffs).new_lines===6208&&sums(diffs).new_bytes===313551,'all 19 derivative counts');
function block(s,start,end){const i=s.indexOf(start);need(i>=0&&s.indexOf(start,i+1)<0,'unique source block start');const j=s.indexOf(end,i+start.length);need(j>i,'source block end');return s.slice(i,j);}
const protectedBlocks=[];
for(const name of ['outer_contract.py']){const row=origin.derivatives.find(r=>r.name===name),old=read(row.old_path).toString(),neu=read(row.new_path).toString();const x=block(old,'def full_stat(', '\ndef '),y=block(neu,'def full_stat(', '\ndef ');need(x===y,'entire full_stat and historical failure schema unchanged '+name);protectedBlocks.push({name,block:'def full_stat to next def',bytes:Buffer.byteLength(x),sha256:sha(Buffer.from(x))});}
{const row=origin.derivatives.find(r=>r.name==='python_runtime_probe.py'),old=read(row.old_path).toString(),neu=read(row.new_path).toString();const start='        data = (ctypes.c_ubyte * 256)()';const x=block(old,start,'        rows.append('),y=block(neu,start,'        if p == STDIN_FILE:');need(x===y,'probe inline native call/mask/decode and historical failure schema unchanged');protectedBlocks.push({name:row.name,block:'inline data allocation, statx call, mask, decode before new stdin predicate',bytes:Buffer.byteLength(x),sha256:sha(Buffer.from(x))});}
for(const name of ['native','stable','resolve','compare_resolution','whole_file']){const row=origin.derivatives.find(r=>r.name==='observe.py'),old=read(row.old_path).toString(),neu=read(row.new_path).toString();const x=block(old,'def '+name+'(', '\ndef '),y=block(neu,'def '+name+'(', '\ndef ');need(x===y,'observer entire protected block unchanged '+name);protectedBlocks.push({name:'observe.py',block:name,bytes:Buffer.byteLength(x),sha256:sha(Buffer.from(x))});}
const f=json(A+'/FRONTIER.json');need(f.targets.length===164&&f.allowed_components.length===204&&f.closure_gaps.length===8,'frontier finite counts');
const stdin=ROOT+'/'+QA+'p212_keyed_stdin_input01/empty.stdin';const t=f.targets.filter(r=>r.path===stdin);need(t.length===1&&t[0].mode==='file'&&t[0].max_bytes===0&&t[0].capture_hex===true&&t[0].expected_names===null&&t[0].max_members===0,'one exact true-empty stdin frontier target');
need(!f.targets.some(r=>r.path==='/dev/null')&&!f.allowed_components.includes('/dev/null')&&!f.allowed_components.includes('/dev'),'old dev path removed from finite frontier');
need(new Set(f.targets.map(r=>r.path)).size===164&&new Set(f.allowed_components).size===204,'unique target and component sets');
need(f.targets.every(r=>f.allowed_components.includes(r.path)),'all targets have finite component permission');
need(f.targets.reduce((n,r)=>n+(Array.isArray(r.expected_names)?r.expected_names.length:0),0)===292,'292 exact listed members');
for(const n of ['AUTHORIZATION.disabled.json','INTERFACE.disabled.json','OUTER_INTERFACE.disabled.json']){const j=json(A+'/'+n);need(j.enabled===false,'disabled '+n);}
const driver=read(A+'/driver.js').toString();
for(const row of origin.unchanged_companions){const b=read(row.path);need(driver.includes('"path": "'+row.path+'"')&&driver.includes(sha(b)),'old companion literal workspace-relative path and actual whole-byte digest '+row.name);}
const capture=read(A+'/companions/CAPTURE_CONTRACT.json');need(driver.includes('"path": "'+A+'/companions/CAPTURE_CONTRACT.json"')&&driver.includes(sha(capture)),'new capture workspace-relative path and full digest');
const outer=read(A+'/outer_contract.py').toString();need(outer.includes(sha(read(A+'/driver.js'))),'actual new driver digest in outer');
const finalKeys=inputKeys.map(k=>{const got=raw(k.path).key;need(JSON.stringify(got)===JSON.stringify(k),'closing complete key unchanged '+k.path);return got;});
console.log(JSON.stringify({schema:'p212-keyed-stdin-independent-documentary-check-v1',scope:'DOCUMENTARY_READ_DIFF_JSON_STRING_ONLY_NOT_SOURCE_EXECUTION',status:'SOURCE_TEXT_AND_COMPLETE_KEYS_VERIFIED_DOCUMENTARY_MINOR_OPEN',checks,distinct_input_keys:finalKeys.length,input_keys:finalKeys,derivative_count:diffs.length,changed_pairs:diffs.filter(r=>r.result.status===1).length,unchanged_pairs:diffs.filter(r=>r.result.status===0).length,all_derivatives:sums(diffs),seven_programs:sums(programs),protected_blocks:protectedBlocks,frontier:{targets:164,allowed_components:204,exact_members:292,closure_gaps:8,stdin_target:t[0]},open_finding:{id:'P212-KSI-F1',severity:'Minor',location:A+'/HANDOFF.md:18',claimed_lines:2779,actual_lines:2679,actual_bytes:148546,disposition:'OPEN_ORIGINAL_AUDIT_REQUIRES_NEW_ONLY_ERRATUM'},diffs,reviewed_source_executed:false,stdin_inspected:false,host_observed:false},null,2));
