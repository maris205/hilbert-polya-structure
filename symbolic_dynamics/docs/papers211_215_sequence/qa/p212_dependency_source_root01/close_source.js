'use strict';
// Read-only close of the new root document packet; no submitted code import.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',BASE=ROOT+'/docs/papers211_215_sequence/qa/p212_dependency_source_root01';
let checks=0;const eq=(a,b,s)=>{checks++;assert.deepEqual(a,b,s);},need=(a,s)=>{checks++;assert.ok(a,s);};
const pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const stat=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const stable=s=>Object.fromEntries(Object.entries(s).filter(([k])=>k!=='atimeNs'));
function read(p){need(p.startsWith(ROOT+'/')&&path.normalize(p)===p,'workspace-only');need(fs.lstatSync(p).isFile(),'regular input');eq(fs.realpathSync(p),p,'unaliased');return fs.readFileSync(p);}
const json=p=>JSON.parse(read(p));
const rb=read(BASE+'/RESULT.json'),r=JSON.parse(rb),n=json(BASE+'/RECEPTION_NATIVE02.json');
eq(pin(rb),{bytes:230592,sha256:'a9d2058df1255adbd4ee5bd8acfc0bc991bbd87f4637ad0b25093f51d84756e7'});
eq(n.result.exit_code,0);need(!n.result.session_id);eq(Buffer.from(n.result.output),rb,'entire actual product stdout');
eq(n.result.chunk_id,'72f589');eq(r.checks,16515);eq(r.inputs.length,150);eq(r.workspace_input_paths,150);
const failed=json(BASE+'/RECEPTION_NATIVE01_FAILURE.json');eq(failed.result.exit_code,1);eq(failed.result.chunk_id,'c5feb8');need(failed.result.output.includes('no truncation marker preparation original 15'));
eq(pin(read(BASE+'/receive_source.js')).sha256,'cb8690b6a3bb9bf0bb0c252eaeae3f9d58ec2eeab395132f9dadfcdc0da27067');
eq(pin(read(BASE+'/receive_source02.js')).sha256,'472b114a7ed03a60d5f8ec0feae75df4f8160a7f601f59de68b4e10958fa93d6');
for(let endpoint=0;endpoint<2;endpoint++)for(const k of r.inputs){
 const p=ROOT+'/'+k.path,b=read(p);eq(pin(b),{bytes:k.bytes,sha256:k.sha256},'whole immutable original '+p);
 eq(stable(stat(fs.lstatSync(p,{bigint:true}))),stable(k.lstat),'all stable lstat fields');
 eq(stable(stat(fs.statSync(p,{bigint:true}))),stable(k.stat),'all stable stat fields');
}
for(const pack of r.packages){
 const b=read(ROOT+'/'+pack.base+'SHA256SUMS');eq(pin(b),pack.seal,'whole original seal');
 const entries=b.toString().slice(0,-1).split('\n').map(line=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_./-]+)$/.exec(line);need(m);return{hash:m[1],name:m[2]};});
 eq(entries.length,pack.payloads);for(const e of entries)eq(pin(read(ROOT+'/'+pack.base+e.name)).sha256,e.hash);
 const files=[],dirs=[];function walk(q){for(const name of fs.readdirSync(ROOT+'/'+pack.base+q).sort()){const p=q+name,s=fs.lstatSync(ROOT+'/'+pack.base+p);need(!s.isSymbolicLink());if(s.isDirectory()){dirs.push(p);walk(p+'/');}else{need(s.isFile());files.push(p);}}}walk('');
 eq(files.sort(),entries.map(x=>x.name).concat('SHA256SUMS').sort());eq(dirs,pack.directories);
}
const comparisons=json(BASE+'/ACTUAL_COMPARISONS_NATIVE.json');eq(comparisons.records.length,4);
for(let i=0;i<4;i++){const x=comparisons.records[i];eq(x.result.exit_code,i===0?1:0);need(!x.result.session_id);if(i)eq(x.result.output,'');else eq(Buffer.from(x.result.output),read(BASE+'/ACTUAL_DRIVER.diff'));}
eq(read(BASE+'/ACTUAL_DRIVER.diff'),read(ROOT+'/docs/papers211_215_sequence/qa/p212_dependency_query_driver_revision02/DRIVER.diff'));
const links=[];for(const m of read(BASE+'/RECEPTION.md').toString().matchAll(/\]\(([^)]+)\)/g)){
 const dest=path.resolve(BASE,m[1]);need(dest.startsWith(ROOT+'/'));need(fs.lstatSync(dest).isFile(),'receipt link exists');links.push({path:m[1],pin:pin(read(dest))});
}
eq(links.length,9);
const payloads=fs.readdirSync(BASE).sort().map(name=>{need(name!=='SHA256SUMS','not already sealed');const p=BASE+'/'+name;need(fs.lstatSync(p).isFile(),'flat root packet');return{name,...pin(read(p))};});
process.stdout.write(JSON.stringify({schema:'p212-root-source-packet-closing-v1',status:'PASS_COMPLETE_ORIGINAL_SOURCE_KEYS_AND_NATIVE_RECEIPT',checks,input_keys_twice:150,whole_package_seals:9,complete_root_native_comparisons:4,current_receipt_links:links.length,links,payloads_before_closing_output:payloads,science:false,driver:false,host:false,build:false,operational_authority:false,external:'HOLD_EXTERNAL'},null,2)+'\n');
