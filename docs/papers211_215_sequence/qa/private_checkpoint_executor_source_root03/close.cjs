'use strict';
// Read-only root source-reception closure; no reviewed import or host follow.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),util=require('util');
const ROOT='/root/autodl-tmp/symbolic_dynamics',R='docs/papers211_215_sequence/qa/private_checkpoint_executor_source_root03';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');let checks=0;
const need=(x,m)=>{checks++;if(!x)throw Error(m);};
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const stat=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
function read(n){need(/^[A-Za-z0-9_.\/-]+$/.test(n)&&!n.startsWith('/')&&n.split('/').every(x=>x&&x!=='.'&&x!=='..'),'unsafe');const p=ROOT+'/'+n;need(fs.realpathSync.native(p)===p,'alias');const a=fs.lstatSync(p,{bigint:true});need(a.isFile(),'nonregular');const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b,c,raw;try{b=fs.fstatSync(fd,{bigint:true});raw=fs.readFileSync(fd);c=fs.fstatSync(fd,{bigint:true});}finally{fs.closeSync(fd);}const d=fs.lstatSync(p,{bigint:true});need([b,c,d].every(x=>util.isDeepStrictEqual(stat(a),stat(x)))&&fs.realpathSync.native(p)===p&&BigInt(raw.length)===a.size,'drift');return{raw,key:{path:n,bytes:raw.length,sha256:sha(raw),stat:stat(a),four_keys_equal:true,physical:true}};}
const resultFile=read(R+'/RESULT.json'),result=JSON.parse(resultFile.raw),run=JSON.parse(read(R+'/RUN_NATIVE.json').raw);
need(result.status==='PASS_ROOT_DOCUMENTARY_INPUT_RECEPTION_NOT_OPERATION'&&result.checks===3638&&result.root_full_key_count===86,'actual result');need(run.result.exit_code===0&&run.result.chunk_id==='e1bebe'&&Buffer.from(run.result.output).equals(resultFile.raw),'actual full native output');
for(const k of result.inputs)need(util.isDeepStrictEqual(k,read(k.path).key),'old full key '+k.path);
const replay=JSON.parse(read(R+'/DOCUMENTARY_REPLAY_NATIVE.json').raw),original=JSON.parse(replay.original_read.result.output);
const after=JSON.parse(read('docs/papers211_215_sequence/qa/private_checkpoint_executor_source_audit03/INPUTS_AFTER_V2_NATIVE.json').raw);
need(replay.replay.result.exit_code===0&&Buffer.byteLength(replay.replay.result.output)===27039&&Buffer.from(replay.replay.result.output).equals(Buffer.from(original.result.output))&&Buffer.from(replay.replay.result.output).equals(Buffer.from(after.result.output)),'actual raw documentary replay');
const files=[];function walk(n){for(const e of fs.readdirSync(ROOT+'/'+n,{withFileTypes:true})){const p=n+'/'+e.name;need(!e.isSymbolicLink(),'package alias');if(e.isDirectory())walk(p);else{need(e.isFile(),'package nonregular');files.push(p);}}}walk(R);files.sort();need(!files.includes(R+'/SHA256SUMS'),'source root already sealed');
const entries=files.map(n=>{const v=read(n);if(n.endsWith('.json'))JSON.parse(v.raw);return{path:n.slice(R.length+1),bytes:v.key.bytes,sha256:v.key.sha256};});
need(read(R+'/RECEPTION.md').raw.toString().includes('SOURCE_ACCEPTED_WITH_DECLARED_BOUNDARIES'),'missing substantive receipt');
console.log(JSON.stringify({status:'PASS_ROOT_EXECUTOR_SOURCE_CLOSING_KEYS_NOT_OPERATION',checks,input_keys_rechecked:result.inputs.length,root_native_chunk:run.result.chunk_id,documentary_replay_chunk:replay.replay.result.chunk_id,existing_payload_files:entries.length,existing_payload_bytes:entries.reduce((s,x)=>s+x.bytes,0),entries,hold_operational:true,hold_external:true},null,2));
