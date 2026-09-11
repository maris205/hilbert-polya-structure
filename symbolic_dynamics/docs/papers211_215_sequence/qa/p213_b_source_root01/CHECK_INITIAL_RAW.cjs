'use strict';
const fs=require('fs'),assert=require('assert/strict'),crypto=require('crypto');
const base='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/';
const dir=base+'p213_b_initial_run01/';
const fields='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' ');
const st=s=>Object.fromEntries(fields.map(k=>[k,s[k].toString()]));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins=[];
function read(path,bound=67108864){const a=fs.lstatSync(path,{bigint:true});assert(a.isFile()&&!a.isSymbolicLink());assert(a.size<=BigInt(bound));const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let raw;try{assert.deepEqual(st(fs.fstatSync(fd,{bigint:true})),st(a));raw=fs.readFileSync(fd);assert.deepEqual(st(fs.fstatSync(fd,{bigint:true})),st(a));}finally{fs.closeSync(fd);}assert.deepEqual(st(fs.lstatSync(path,{bigint:true})),st(a));assert.equal(BigInt(raw.length),a.size);pins.push({path,key:st(a),bytes:raw.length,sha256:sha(raw)});return raw;}
const req=JSON.parse(read(base+'p213_b_execution_preparation01/REQUEST.initial.ready.json'));
assert.deepEqual(fs.readdirSync(dir).sort(),req.output_files.slice().sort());
const data={};for(const name of req.output_files){data[name]=read(dir+name);assert.equal(pins.at(-1).key.nlink,'1');}
for(const name of ['stderr.bin','keys.before.stderr','keys.after.stderr','input-key-cmp.stdout','input-key-cmp.stderr','raw.keys.stderr','controller.stdout','controller.stderr'])assert.equal(data[name].length,0);
for(const name of ['python.exit','controller.exit'])assert.equal(data[name].toString(),'0\n');
assert(data['keys.before.json'].equals(data['keys.after.json']));
const before=JSON.parse(data['keys.before.json']),after=JSON.parse(data['keys.after.json']);
const pre=JSON.parse(JSON.parse(read(base+'p213_b_source_root01/PREFLIGHT_NATIVE.json')).output);
assert.deepEqual(before,after);assert.deepEqual(before,pre);assert.equal(before.records.length,20);
for(const r of before.records){assert(r.complete);if(r.kind==='required-absence'){try{fs.lstatSync(r.path);throw Error('expected absence');}catch(e){assert.equal(e.code,'ENOENT');}continue;}const bytes=read(r.path,8388608),p=pins.at(-1);assert(r.eof&&r.close_succeeded);assert.equal(r.bytes,p.bytes);assert.equal(r.sha256,p.sha256);for(const k of ['begin','fd_before','fd_after','end'])assert.deepEqual(r[k],p.key);}
const rawKeys=JSON.parse(data['raw.keys.json']);assert.equal(rawKeys.records.length,3);
for(const r of rawKeys.records){const p=pins.find(p=>p.path===r.path);assert(p);assert(r.complete&&r.eof&&r.close_succeeded);assert.equal(r.bytes,p.bytes);assert.equal(r.sha256,p.sha256);for(const k of ['begin','fd_before','fd_after','end'])assert.deepEqual(r[k],p.key);}
const out=data['stdout.bin'];assert(out.length>0&&out.length<=67108864);assert([...out].every(b=>b===10||(b>=32&&b<=126)));assert.equal(out.at(-1),10);
const lines=out.toString('ascii').slice(0,-1).split('\n');assert.equal(lines.length,19366);
const counts=Object.fromEntries(['STATE','CHAMBER','CARRIER','PASS'].map(k=>[k,lines.filter(l=>l.startsWith(k+' ')).length]));assert.deepEqual(counts,{STATE:461,CHAMBER:18872,CARRIER:30,PASS:1});assert(lines.every(l=>l.length+1<=2048));
console.log(JSON.stringify({status:'PASS_INITIAL_B_RAW_CURRENT_KEYS_FRAMING_ONLY',counts,lines:lines.length,headers:lines.slice(0,2),trailer:lines.at(-1),stdout:{bytes:out.length,sha256:sha(out)},pins}));
