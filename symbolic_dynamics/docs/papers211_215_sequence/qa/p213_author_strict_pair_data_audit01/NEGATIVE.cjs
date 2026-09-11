'use strict';
// Actual in-memory DATA mutations only. No producer or filesystem mutation.
const {load}=require('./CHECK.cjs'),pair=require('./PAIR_DATA.cjs');
const f=load(),{r,need,runs,binding,canonicalIntegerJSON,parseIntegerJSON}=f;
const findings=[];const baseline=pair(runs,binding);
function cloneRuns(){return runs.map(x=>({...x,control:structuredClone(x.control),controlRaw:Buffer.from(x.controlRaw),external:structuredClone(x.external)}));}
function test(name,mutate,expected,{refresh=true}={}){
 const copy=cloneRuns();mutate(copy);if(refresh)for(const x of copy)x.controlRaw=Buffer.from(canonicalIntegerJSON(x.control)+'\n','ascii');
 let message=null;try{pair(copy,binding);}catch(e){message=e.message;}
 need(typeof message==='string'&&message.includes(expected),'negative '+name+' expected '+expected+' observed '+message);
 findings.push({name,rejected:true,message});
}
test('run order swapped',x=>x.reverse(),'exact run order/identity');
test('borrowed first native identity',x=>{x[1].nativeId=x[0].nativeId;},'actual distinct original native identity');
test('borrowed first grant identity',x=>{x[1].grantId=x[0].grantId;},'actual distinct consumed grant identity');
test('run02 key joined to run01 path',x=>{x[1].external.raw.stdout.path=x[0].external.raw.stdout.path;},'exact per-run raw role/path');
test('wrong same-size source-key pathname',x=>{x[1].external.sources[binding.science.source].path+='x';},'current source key exact lexical join');
test('unrecognized adapter field',x=>{x[1].normalization=true;},'complete adapter run fields');
test('unrecognized control top field',x=>{x[1].control.extra=true;},'complete initial science control exact fields');
test('collapsed large integer',x=>{const p=binding.files[0].lexical;x[1].control.before_keys[p].fd_before.st_mtime_ns=Number(x[1].control.before_keys[p].fd_before.st_mtime_ns);},'unsupported output scalar type',{refresh:false});
test('integer instead of boolean',x=>{x[1].control.runtime_accepted=0n;},'producer explicitly pending runtime_accepted');
test('missing whole before entry',x=>{delete x[1].control.before_keys[binding.files[0].lexical];},'whole before dictionary exact fields');
test('missing ordered second pass',x=>{x[1].control.files.pop();},'exactly two finite passes');
test('one-unit exact metadata corruption',x=>{x[1].control.before_keys[binding.files[0].lexical].fd_before.st_mtime_ns+=1n;},'path/fd identity');
test('zip absence error changed',x=>{x[1].control.before_keys['/usr/lib/python310.zip'].begin.absence.errno=20n;},'exact ENOENT');
test('saved source bytes digest changed',x=>{x[1].control.science.source_load.sha256_of_read_bytes='0'.repeat(64);},'whole loaded-source key equality');
test('missing module phase',x=>{x[1].control.module_snapshots.pop();},'seven actual module sampling points');
test('module loader record omitted',x=>{x[1].control.helper_modules[0].pop();},'full top/snapshot duplicate');
test('map parsed address changed without its raw bytes',x=>{x[1].control.maps[0].parsed[0].start+=1n;},'every independent parsed map field');
test('map raw byte count changed',x=>{x[1].control.maps[0].byte_count+=1n;},'complete ASCII raw map bytes');
test('whole control transport normalized',x=>{x[1].controlRaw=Buffer.from(JSON.stringify({not_the_original:true})+'\n');},'whole lossless control raw binding',{refresh:false});
test('stdout incorrectly bound to equal-size other run metadata',x=>{x[1].external.raw.stdout.fd_before=structuredClone(x[0].external.raw.stdout.fd_before);},'original captured output metadata 1 st_ino');
test('producer control descriptor extent treated as settled extent',x=>{x[1].control.outputs_final['3'].st_size=BigInt(x[1].external.raw.control.byte_count);},'control remains empty before its final write');
test('stdout completed extent changed',x=>{x[1].control.post_science.outputs['1'].st_size+=1n;},'exact scientific output size');
function allObjects(x,fn){if(x&&typeof x==='object'){fn(x);for(const v of Object.values(x))allObjects(v,fn);}}
const host=binding.files.find(e=>e.lexical.startsWith('/usr/lib/python3.10/')&&!e.absence_required).lexical;
test('coherent host digest change across all within-run aliases',x=>{allObjects(x[1].control,o=>{if(o.lexical===host&&Object.hasOwn(o,'sha256_of_read_bytes'))o.sha256_of_read_bytes='0'.repeat(64);});},'unapproved shared-key/scalar change');
test('coherent host timestamp change across all within-run aliases',x=>{allObjects(x[1].control,o=>{if(o.lexical===host&&Object.hasOwn(o,'sha256_of_read_bytes'))allObjects(o,s=>{if(Object.hasOwn(s,'st_mtime_ns'))s.st_mtime_ns+=1n;});});},'unapproved shared-key/scalar change');
test('coherent nonpolicy launch field changed in all six snapshots',x=>{allObjects(x[1].control,o=>{if(Array.isArray(o)&&o.length===2&&o[0]==='hexversion'&&Array.isArray(o[1]))o[1][1]+=1n;});},'unapproved shared-key/scalar change');
test('coherent map permission change cannot hide in dynamic addresses',x=>{const m=x[1].control.maps[0],p=m.parsed[0].perms,changed=(p[0]==='r'?'-':'r')+p.slice(1);const lines=Buffer.from(m.raw_hex,'hex').toString('ascii').split('\n');lines[0]=lines[0].replace(p,changed);m.raw_hex=Buffer.from(lines.join('\n'),'ascii').toString('hex');m.parsed[0].perms=changed;},'unapproved shared-key/scalar change');
for(const[name,text,expected]of[['duplicate JSON key','{"x":1,"x":2}','duplicate'],['float token','{"x":1.0}','integer'],['trailing transport','{} {}','trailing']]){
 let message=null;try{parseIntegerJSON(text);}catch(e){message=e.message;}need(typeof message==='string'&&message.includes(expected),'parser negative '+name);findings.push({name,rejected:true,message});
}
for(let i=0;i<2;i++)need(Buffer.from(canonicalIntegerJSON(runs[i].control)+'\n','ascii').equals(runs[i].controlRaw),'originals unchanged after DATA mutations');
process.stdout.write(JSON.stringify({status:'PASS_ACTUAL_NEGATIVE_PAIR_DATA_CONTROLS',negative_cases:findings.length,baseline_status:baseline.status,baseline_control_checks:baseline.controls.map(x=>x.checks),findings,checks:r.checks,key_count:r.keys.size,total_read_bytes:r.total,keys:[...r.keys.values()],source_execution:false,host_queries:false,originals_modified:false},null,2)+'\n');

