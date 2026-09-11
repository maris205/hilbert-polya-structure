'use strict';
// Outside workspace raw reception only; no JSON body interpretation or host read.
const fs=require('fs'),c=require('crypto'),a=require('assert/strict');
const base='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/',own=base+'p212_three_terminal_root01/';
const F='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' '),stat=s=>Object.fromEntries(F.map(k=>[k,String(s[k])])),sha=b=>c.createHash('sha256').update(b).digest('hex');
const pf=JSON.parse(JSON.parse(fs.readFileSync(own+'PREFLIGHT_NATIVE.json')).output),native=JSON.parse(fs.readFileSync(own+'ACTUAL_NATIVE.json'));
a.equal(native.result.exit_code,0);a.equal(native.result.chunk_id,'136a9c');a.equal(native.result.output,'');a.equal(native.result.session_id,undefined);
const keys=[];
for(const [path,limit] of [...pf.keys.map(k=>[k.path,65536]),[base+'p212_three_terminal_raw01/stdout.json',268435456],[base+'p212_three_terminal_raw01/stderr.raw',8388608]]){
 a(path.startsWith(base));const begin=fs.lstatSync(path,{bigint:true});a(begin.isFile()&&!begin.isSymbolicLink()&&begin.nlink===1n&&begin.size>=0n&&begin.size<=BigInt(limit));
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW),fd_before=fs.fstatSync(fd,{bigint:true});a.deepEqual(stat(begin),stat(fd_before));const chunks=[],buf=Buffer.alloc(65536);let bytes=0,fd_after,eof=false;
 try{for(;;){const n=fs.readSync(fd,buf,0,Math.min(buf.length,limit+1-bytes),null);if(n===0){eof=true;break;}chunks.push(Buffer.from(buf.subarray(0,n)));bytes+=n;a(bytes<=limit);}fd_after=fs.fstatSync(fd,{bigint:true});a.deepEqual(stat(begin),stat(fd_after));}finally{fs.closeSync(fd);}
 const end=fs.lstatSync(path,{bigint:true});a.deepEqual(stat(begin),stat(end));a.equal(BigInt(bytes),begin.size);const raw=Buffer.concat(chunks),key={path,begin:stat(begin),fd_before:stat(fd_before),fd_after:stat(fd_after),end:stat(end),bytes,sha256:sha(raw),eof,close_succeeded:true};
 const prior=pf.keys.find(k=>k.path===path);if(prior){for(const field of ['begin','fd_before','fd_after','end','bytes','sha256','eof','close_succeeded'])a.deepEqual(key[field],prior[field]);}else{a.equal(begin.uid,0n);a.equal(begin.gid,0n);a.equal(begin.mode&0o7777n,0o600n);}
 keys.push(key);
}
const rawdir=base+'p212_three_terminal_raw01',before=fs.lstatSync(rawdir,{bigint:true}),members=fs.readdirSync(rawdir).sort();a.deepEqual(members,['stderr.raw','stdout.json']);a.deepEqual(stat(before),stat(fs.lstatSync(rawdir,{bigint:true})));
for(const d of pf.directories){const now=stat(fs.lstatSync(d.path,{bigint:true}));if(d.path===rawdir){for(const f of F.slice(0,7))a.equal(now[f],d.end[f]);}else a.deepEqual(now,d.end);}
a.equal(keys.length,11);a.equal(keys.at(-1).bytes,0);
console.log(JSON.stringify({status:'CLOSED_RAW_NINE_OUTSIDE_KEYS_ACCEPTED_DATA_PENDING',actual_chunk:native.result.chunk_id,inputs:keys.slice(0,9),raw:keys.slice(9),raw_directory:{path:rawdir,key:stat(before),members},host_candidates_reopened:false},null,2));
