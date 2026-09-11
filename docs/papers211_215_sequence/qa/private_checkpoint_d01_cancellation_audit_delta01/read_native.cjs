'use strict';
// Read archival JSON as data; never dispatch the contained requests.
const fs=require('fs'),crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics/';
const prep='docs/papers211_215_sequence/qa/private_checkpoint_d01_cancellation_delta01/';
const expected={
'NATIVE_READS.json':[100043,'5d90e000d5c46cfd6e29740e8d4f69baa6de09efa66858bfaad26ff9071e0855'],
'CLOSING_NATIVE.json':[18340,'b9ea471139395e7dfc01f90885a2ef5ccf7e086094d00ca5da63f709fdba9e3e']};
const file=process.argv[2],first=process.argv[3],last=process.argv[4];
if(!expected[file])throw Error('Fixed archival file only');
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,s[k].toString()]));
const p=root+prep+file,before=fs.lstatSync(p,{bigint:true});
if(!before.isFile()||before.isSymbolicLink())throw Error('Physical archival file');
const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
try{
const opened=fs.fstatSync(fd,{bigint:true}),b=fs.readFileSync(fd);
const ended=fs.fstatSync(fd,{bigint:true}),after=fs.lstatSync(p,{bigint:true});
if([opened,ended,after].some(s=>JSON.stringify(meta(s))!==JSON.stringify(meta(before))))throw Error('Metadata changed');
const sha256=crypto.createHash('sha256').update(b).digest('hex');
if(b.length!==expected[file][0]||sha256!==expected[file][1])throw Error('Expected whole key differs');
const x=JSON.parse(b.toString('utf8'));
if(!Array.isArray(x.records))throw Error('Expected actual records');
const head={file:prep+file,whole_bytes:b.length,whole_sha256:sha256,metadata:meta(before)};
if(first==='index'&&process.argv.length===4){
 process.stdout.write(JSON.stringify({...head,archive_header:Object.fromEntries(Object.entries(x).filter(([k])=>k!=='records')),
 records:x.records.map((r,i)=>({index:i,request:r.request,result_keys:Object.keys(r.result||r.response||{}),
 output_bytes:Buffer.byteLength((r.result||r.response||{}).output||'')}))},null,2)+'\n');
}else{
 const a=Number(first),z=Number(last);
 if(process.argv.length!==5||!Number.isInteger(a)||!Number.isInteger(z)||a<0||z<a||z>x.records.length)throw Error('Exact record bounds');
 process.stdout.write(JSON.stringify({...head,archive_header:Object.fromEntries(Object.entries(x).filter(([k])=>k!=='records')),
 range_start_inclusive:a,range_end_exclusive:z,records:x.records.slice(a,z)},null,2)+'\n');
}
}finally{fs.closeSync(fd);}
