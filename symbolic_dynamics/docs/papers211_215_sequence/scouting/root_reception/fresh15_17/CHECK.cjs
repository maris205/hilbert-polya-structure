"use strict";
// New-layout, root documentary receiver. Embedded commands/URLs are data only.
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const B='docs/papers211_215_sequence/scouting/',R=B+'root_reception/fresh15_17/';
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs','birthtimeNs','blocks','blksize'];
const raw=new Map(),keys=new Map(),pairs=[];let checks=0,oldOccurrences=0;
const ok=(v,m)=>{checks++;assert(v,m);},eq=(a,b,m)=>{checks++;assert.deepStrictEqual(a,b,m);};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex'),meta=s=>Object.fromEntries(F.map(k=>[k,String(s[k])]));
const selected=JSON.parse(fs.readFileSync(R+'READ_SCOPE.json','utf8'));
const own=['ROOT_REPLAYS_NATIVE.json','ROOT_READS_NATIVE.json','READ_SCOPE.json','CHECK.cjs'];
const allowed=new Set([...selected.fixed_original_paths,...own.map(n=>R+n)]);
const packets=[
 [B+'finite_residual_fresh15','SHA256SUMS','c8e77c399b41714113d520a320f80127f8ba67eb3315933e5d51d7af00745ada',10],
 [B+'finite_residual_fresh16','SHA256SUMS','203d5bd606dc609d6e3470b04f0637174a9c42d0055d4bbec391f069a11a525c',10],
 [B+'finite_residual_fresh17','SHA256SUMS','e209e7a21e84112ea49ed8d08c306a596e2c43f38edaf53b7a11ce99640da7c0',10],
 [B+'root_reception/fresh15_independent_intake01','SHA256SUMS','d3fd5e22abadc14888566e18092870b32816d83e0911a448f78603c9e0dca79c',11],
 [B+'root_reception/fresh16_artifact_intake01','SHA256SUMS','b02e9d79ac1a5a3dd2f9cf1db810615020b5c8a4075db9018afbf0902704bc62',12],
 [B+'root_reception/fresh17_independent_intake01','MANIFEST.json','4edfbf02fcf5f33c2a4454acacc8cec31672a6fcfbb081bc0fc367ffb2cff2bb',11]
];
function fresh(p){
 ok(allowed.has(p),'fixed documentary operand '+p);
 const a=fs.lstatSync(p,{bigint:true});ok(a.isFile()&&a.nlink===1n&&a.size>=0n&&a.size<=5000000n,'single-link bounded regular leaf '+p);
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b;
 try{eq(meta(fs.fstatSync(fd,{bigint:true})),meta(a));b=fs.readFileSync(fd);eq(meta(fs.fstatSync(fd,{bigint:true})),meta(a));}finally{fs.closeSync(fd);}
 eq(meta(fs.lstatSync(p,{bigint:true})),meta(a));eq(BigInt(b.length),a.size,'full EOF');return{b,key:{path:p,bytes:b.length,sha256:sha(b),fields:meta(a)}};
}
function read(p){if(!raw.has(p)){const x=fresh(p);raw.set(p,x.b);keys.set(p,x.key);}return raw.get(p);}
const json=p=>JSON.parse(read(p).toString('utf8'));
function pair(label,a,b){eq(a,b,label);pairs.push({label,bytes:a.length,sha256:sha(a)});}
function old(k,path=k.path){
 const b=read(path),now=keys.get(path);eq(k.bytes,b.length,'whole old byte count');eq(k.sha256,now.sha256,'whole old digest');
 const m=k.metadata||k.fields;ok(m&&Object.keys(m).length>=10,'full declared metadata schema');
 for(const [n,v]of Object.entries(m)){ok(F.includes(n),'known exact metadata field');eq(now.fields[n],v,'unchanged declared field '+n);}
 if(k.metadata){eq(k.fd_end,m,'whole old end descriptor');eq(k.path_end,m,'whole old end path');eq(k.full_eof,true);eq(k.leaf_links,[]);}
 oldOccurrences++;
}
const inventory=[];
for(const[d,seal,digest,count]of packets){
 const sealPath=d+'/'+seal;allowed.add(sealPath);const sb=read(sealPath);eq(sha(sb),digest,'assigned exact nonself seal');
 let entries;
 if(seal==='SHA256SUMS'){
  ok(sb.at(-1)===10,'final LF');entries=sb.toString('utf8').trimEnd().split('\n').map(l=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);ok(m,'strict basename manifest');return{name:m[2],sha256:m[1]};});
 }else{const m=JSON.parse(sb);eq(m.schema,'FRESH17_INDEPENDENT_COMPLETE_NONSELF_MANIFEST_V1');eq(m.owned_directory,d);eq(m.payload_count,count);entries=m.entries;}
 eq(entries.length,count);eq(new Set(entries.map(e=>e.name)).size,count);ok(!entries.some(e=>e.name===seal),'nonself');
 eq(fs.readdirSync(d).sort(),[seal,...entries.map(e=>e.name)].sort(),'all and only frozen physical files');let bytes=0;
 for(const e of entries){ok(/^[A-Za-z0-9_.-]+$/.test(e.name),'safe exact leaf');const p=d+'/'+e.name;allowed.add(p);const b=read(p);eq(sha(b),e.sha256,'payload hash');bytes+=b.length;if(e.metadata)old(e,p);}
 if(seal==='MANIFEST.json')eq(bytes,JSON.parse(sb).payload_bytes);
 inventory.push({directory:d,payloads:count,files:count+1,payload_bytes:bytes,seal_sha256:digest});
}
for(const p of selected.fixed_original_paths)read(p);
for(const n of own)read(R+n);
const replays=json(R+'ROOT_REPLAYS_NATIVE.json'),replayCensus=[];
function result(x){return x.result||x.native||x.record?.result;}
const locations={15:'fresh15_independent_intake01/CHECK_NATIVE.json',16:'fresh16_artifact_intake01/CHECK_NATIVE.json',17:'fresh17_independent_intake01/POSTCHECK_NATIVE.json'};
for(const i of[15,16,17]){
 const a=replays[i],b=json(B+'root_reception/'+locations[i]),ar=result(a),br=result(b);
 eq(ar.exit_code,0);eq(br.exit_code,0);ok(!ar.session_id&&!br.session_id,'actual settled documentary runs');
 pair('root fresh'+i+' whole actual documentary stdout',Buffer.from(ar.output,'utf8'),Buffer.from(br.output,'utf8'));
 const o=JSON.parse(ar.output);eq(o.checks,{15:775,16:1303,17:604}[i]);for(const k of o.keys)old(k);
 replayCensus.push({fresh:i,request:a.request,root_chunk:ar.chunk_id,independent_chunk:br.chunk_id,checks:o.checks,keys:o.keys.length,stdout_bytes:Buffer.byteLength(ar.output),stdout_sha256:sha(Buffer.from(ar.output))});
}
const closures=[['fresh15_independent_intake01/CLOSING_NATIVE.json',42],['fresh16_artifact_intake01/CLOSE_NATIVE.json',39],['fresh17_independent_intake01/PRECHECK_CORRECTED_NATIVE.json',30]];
for(const[n,count]of closures){const x=json(B+'root_reception/'+n),r=result(x);eq(r.exit_code,0);ok(!r.session_id);const o=JSON.parse(r.output);eq(o.keys.length,count);for(const k of o.keys)old(k);}
for(const[n,resultName]of[['fresh16_artifact_intake01/CHECK_NATIVE.json','fresh16_artifact_intake01/CHECK_RESULT.json'],['fresh16_artifact_intake01/CLOSE_NATIVE.json','fresh16_artifact_intake01/CLOSE_RESULT.json']])pair('original complete stdout artifact '+n,Buffer.from(result(json(B+'root_reception/'+n)).output,'utf8'),read(B+'root_reception/'+resultName));
// Historical preclosing commands are archived data; this receiver checks final layouts.
const reads=json(R+'ROOT_READS_NATIVE.json');
for(const x of reads.early){eq(x.result.exit_code,0);let paths,expected;if(x.request.cmd.startsWith('cat ')){paths=[x.request.cmd.slice(4)];expected=read(paths[0]);}else{const m=/^sed -n '(\d+),(\d+)p' (.+)$/.exec(x.request.cmd);ok(m,'literal root source read');paths=[m[3]];const lines=read(paths[0]).toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];expected=Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join(''),'utf8');}pair('actual retained root semantic/code read '+paths[0],Buffer.from(x.result.output,'utf8'),expected);}
eq(reads.absence.result.exit_code,0);eq(reads.absence.result.output,'');eq(reads.absence.request.cmd,'test ! -e '+R.slice(0,-1));
eq(reads.later_native_returns.filter(x=>x.exit_code!==0).map(x=>[x.chunk_id,x.exit_code]),[['106bd2',2],['a41dc0',2],['7ec292',2]],'three retained wrong-basename reads');
const counts=selected.counts;eq(counts,{new_entrances:[0,0,1],closed_before:58,closed_after_if_received:59,retained:3,complete:1,open:2,reserves:0});
eq(json(B+'finite_residual_fresh15/SCOPE.json').counts.new_literal_entrances,0);
eq(json(B+'finite_residual_fresh16/SCOPE.json').counts.new_candidate_entrances,0);
eq(json(B+'finite_residual_fresh17/SCOPE.json').counts.new_literal_desk_attempts,1);
for(const[p,k]of keys){const x=fresh(p);eq(x.key,k,'complete root key closure');eq(x.b,raw.get(p),'root whole-byte closure');}
process.stdout.write(JSON.stringify({schema:'ROOT_FRESH15_17_COMPLETE_DOCUMENTARY_RECEPTION_V1',checks,packets:inventory,old_complete_key_occurrences:oldOccurrences,replays:replayCensus,raw_pairs:pairs.length,raw_paired_bytes:pairs.reduce((n,x)=>n+x.bytes,0),pairs,document_keys:keys.size,keys:[...keys.values()],counts,mathematical_verdict:'Separate root semantic receipt; no pilot or admission',operational_authority:false,external_status:'HOLD_EXTERNAL'},null,2)+'\n');
