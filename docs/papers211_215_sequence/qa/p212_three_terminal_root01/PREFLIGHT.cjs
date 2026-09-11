'use strict';
const fs=require('fs'),c=require('crypto');
const base='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/';
const names=['p212_three_terminal_preparation01/three_terminals.proposed.mjs.txt','p212_three_terminal_preparation01/ENTRY.proposed.mjs.txt','p212_three_terminal_enabled01/three_leaves.mjs','p212_three_terminal_enabled01/ENTRY.mjs','p212_three_terminal_binding01/REQUEST.json','p212_three_terminal_root01/CONDITIONAL_GRANT.md','p212_three_terminal_preparation01/OPERATION_REQUEST.proposed.json','p212_three_terminal_preparation01/capture.proposed.sh.txt','p212_three_terminal_preparation01/REQUEST.disabled.json'];
const F='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' '),stat=s=>Object.fromEntries(F.map(k=>[k,s[k].toString()]));
const sha=b=>c.createHash('sha256').update(b).digest('hex'),eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b),need=(v,m)=>{if(!v)throw Error(m);};
const bodies=[],keys=[];
for(const name of names){
 const p=base+name,a=fs.lstatSync(p,{bigint:true});need(a.isFile()&&!a.isSymbolicLink()&&a.nlink===1n&&a.size<=65536n,'regular bounded control');
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW),b=fs.fstatSync(fd,{bigint:true});need(eq(stat(a),stat(b)),'before');
 const chunks=[],buf=Buffer.alloc(8192);let size=0,eof=false;try{for(;;){const n=fs.readSync(fd,buf,0,Math.min(buf.length,65537-size),null);if(n===0){eof=true;break;}chunks.push(Buffer.from(buf.subarray(0,n)));size+=n;need(size<=65536,'bounded read');}const z=fs.fstatSync(fd,{bigint:true});need(eq(stat(b),stat(z)),'after fd');keys.push({path:p,begin:stat(a),fd_before:stat(b),fd_after:stat(z),eof});}finally{fs.closeSync(fd);}
 const end=fs.lstatSync(p,{bigint:true});need(eq(stat(a),stat(end))&&BigInt(size)===a.size,'end');const raw=Buffer.concat(chunks);bodies.push(raw);Object.assign(keys.at(-1),{end:stat(end),bytes:size,sha256:sha(raw),close_succeeded:true});
}
need(Buffer.from(bodies[0].toString().replace(' const SOURCE_ENABLED=false;',' const SOURCE_ENABLED=true;')).equals(bodies[2])&&bodies[1].equals(bodies[3]),'exact source copies');
need(sha(bodies[0])==='9ce3b9e51a39244f3bc39720b73d806e6bf3de022afc39d3fc71c78fd71c05ee'&&sha(bodies[1])==='97429441bbdf46b2b413065ceabe233b9c207ac71c0312f383e46f9c0a630803','accepted sources');
const request=JSON.parse(bodies[4]),template=JSON.parse(bodies[8]),ref={path:base+names[5],pin:{bytes:bodies[5].length,sha256:sha(bodies[5])}};
need(request.enabled===true&&request.status==='ROOT_BOUND_THREE_LEXICAL_LEAVES_ONLY'&&eq(request.permission_receipt,ref),'binding grant');
need(eq({...request,enabled:false,status:template.status,permission_receipt:null},template),'entire binding delta');
const native=JSON.parse(bodies[6]);need(Buffer.from(native.proposed_native_request.arguments.cmd).equals(bodies[7])&&sha(bodies[7])==='2c03c54bfc981b833171ebe3de4906107991614b7a7a1cb3df06fc480805b6c9','exact native capture');
need(sha(bodies[6])==='6bc0ba416aa68dea034f93fc2558ecbabbb69c98572e22dac009c402400d2178','operation document');
const directories=[];for(const d of ['p212_three_terminal_enabled01','p212_three_terminal_binding01','p212_three_terminal_raw01']){const p=base+d,a=fs.lstatSync(p,{bigint:true});need(a.isDirectory()&&a.uid===0n&&a.gid===0n&&(a.mode&0o7777n)===0o700n,'private directory');const entries=fs.readdirSync(p).sort();need(eq(entries,d.endsWith('enabled01')?['ENTRY.mjs','three_leaves.mjs']:d.endsWith('binding01')?['REQUEST.json']:[]),'exact directory entries');const z=fs.lstatSync(p,{bigint:true});need(eq(stat(a),stat(z)),'directory stable');directories.push({path:p,begin:stat(a),end:stat(z),entries});}
console.log(JSON.stringify({status:'PASS_SOURCE_COPIES_BOUND_REQUEST_FRESH_DIRECTORIES',keys,directories,request},null,2));
