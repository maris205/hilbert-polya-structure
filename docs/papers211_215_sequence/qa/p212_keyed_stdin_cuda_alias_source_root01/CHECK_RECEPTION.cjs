'use strict';
// New root documentary receiver. No reviewed source, embedded host path or subprocess execution.
const fs=require('node:fs'),crypto=require('node:crypto');
const q='docs/papers211_215_sequence/qa/',r=q+'p212_keyed_stdin_cuda_alias_source_root01/';
const a=q+'p212_keyed_stdin_cuda_alias_source_audit01/',d=q+'p212_keyed_stdin_cuda_alias_source_delta01/';
const fields=['dev','ino','mode','nlink','uid','gid','size','mtimeNs','ctimeNs','birthtimeNs'];
let checks=0;const keys=new Map(),bodies=new Map(),pairs=[];
const ok=(v,m)=>{checks++;if(!v)throw Error(m);};
const eq=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function meta(s){return Object.fromEntries(fields.map(n=>{ok(typeof s[n]==='bigint','full integer field');return[n,String(s[n])];}));}
function read(path){
 ok(path.startsWith(q+'p212_')&&!path.split('/').includes('..'),'selected P212 document');
 if(bodies.has(path))return bodies.get(path);
 const st=fs.lstatSync(path,{bigint:true});ok(st.isFile()&&!st.isSymbolicLink()&&st.nlink===1n&&st.size<10000000n,'bounded regular document');
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b,m,z;
 try{const t=fs.fstatSync(fd,{bigint:true});m=meta(t);ok(t.isFile()&&eq(m,meta(st)),'same selected descriptor');b=fs.readFileSync(fd);z=meta(fs.fstatSync(fd,{bigint:true}));}finally{fs.closeSync(fd);}
 ok(eq(m,z)&&eq(m,meta(fs.lstatSync(path,{bigint:true})))&&BigInt(b.length)===BigInt(m.size),'complete stable document');
 bodies.set(path,b);keys.set(path,{path,bytes:b.length,sha256:sha(b),lf_lines:b.reduce((n,c)=>n+(c===10),0),fields:m});return b;
}
function text(p){const b=read(p),s=b.toString('utf8');ok(Buffer.from(s).equals(b),'lossless UTF8');return s;}
const json=p=>JSON.parse(text(p));
const inventory=[];
function packet(dir,count,pin){
 const t=text(dir+'SHA256SUMS');ok(sha(Buffer.from(t))===pin&&t.endsWith('\n')&&!t.endsWith('\n\n'),'fixed strict seal');
 const names=[],ls=t.slice(0,-1).split('\n');ok(ls.length===count,'payload count');
 for(const l of ls){const m=/^([a-f0-9]{64})  ([A-Za-z0-9_./-]+)$/.exec(l);ok(m&&!m[2].split('/').includes('..')&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'unique safe nonself entry');names.push(m[2]);ok(sha(read(dir+m[2]))===m[1],'payload raw hash');}
 function files(path,prefix=''){const out=[];for(const n of fs.readdirSync(path)){const st=fs.lstatSync(path+n);ok(!st.isSymbolicLink(),'physical inventory');if(st.isDirectory()){ok(dir===d&&prefix===''&&n==='diffs','one exact source subdirectory');out.push(...files(path+n+'/',n+'/'));}else{ok(st.isFile(),'regular inventory');out.push(prefix+n);}}return out.sort();}
 ok(eq(files(dir),[...names,'SHA256SUMS'].sort()),'entire physical inventory');
 inventory.push({path:dir,payloads:count,files:count+1,physical_bytes:[...names,'SHA256SUMS'].reduce((n,x)=>n+read(dir+x).length,0),seal_sha256:pin});
}
packet(d,21,'32c3c6da8cc47ef0adf96723a98ec8244ae004990582effdca407a49537aa10d');
packet(a,16,'62779c39dd68545e4f650dd79d13960693839289a669a29faff83cede2492747');
const pinLines=text(a+'INPUTS.sha256').trimEnd().split('\n'),seen=new Set();ok(pinLines.length===52,'all 52 independent pins');
for(const l of pinLines){const m=/^([a-f0-9]{64})  (docs\/[A-Za-z0-9_./-]+)$/.exec(l);ok(m&&!seen.has(m[2]),'unique selected input');seen.add(m[2]);ok(sha(read(m[2]))===m[1],'unchanged audit input');}
function compareKey(k){read(k.path);const n=keys.get(k.path);ok(n.bytes===k.bytes&&n.sha256===k.sha256&&n.lf_lines===k.lf_lines&&eq(n.fields,k.fields),'all original key fields unchanged');}
const rr=json(r+'ROOT_NATIVE.json').records;ok(rr.length===17,'selected raw scope');
for(const [role,dir,count,nkeys]of [['author_replay',d,17454,42],['independent_replay',a,16959,58]]){
 const now=rr.find(x=>x.role===role).response,old=json(dir+'CHECK_NATIVE.json').run.result;
 ok(now.exit_code===0&&old.exit_code===0&&!now.session_id&&!old.session_id,'actual finite replay exits');
 const b=Buffer.from(now.output);ok(b.equals(Buffer.from(old.output))&&b.equals(read(dir+'CHECK_RESULT.json')),'fresh root raw-equal original and canonical');
 const j=JSON.parse(now.output);ok(j.checks===count&&j.keys.length===nkeys,'replay census');for(const k of j.keys)compareKey(k);
 pairs.push({kind:role,path:dir+'CHECK_RESULT.json',chunk:now.chunk_id,bytes:b.length,sha256:sha(b),checks:count,keys:nkeys});
}
const artifacts=rr.find(x=>x.role==='independent_artifacts'),ar=JSON.parse(artifacts.response.output);
ok(artifacts.response.exit_code===0&&!artifacts.response.session_id&&ar.mode==='sealed'&&ar.checks===1297&&ar.keys.length===69&&ar.own_payloads===16&&ar.physical_files===17,'actual complete sealed-layout check');
for(const k of ar.keys)compareKey(k);
const closingCarrier=json(a+'CLOSING_NATIVE.json'),closing=JSON.parse(closingCarrier.run.result.output);
ok(closingCarrier.run.result.exit_code===0&&closing.checks===1059&&closing.keys.length===67,'frozen original audit closure');for(const k of closing.keys)compareKey(k);
for(const rec of rr.slice(3)){
 const x=rec.response;ok(x.exit_code===0&&!x.session_id,'complete root selected read');
 const paths=rec.role==='all_diffs'?['observe.py','FRONTIER.json','AUTHORIZATION.disabled.json'].map(n=>d+'diffs/'+n+'.diff'):[/ (docs\/[A-Za-z0-9_./-]+)$/.exec(rec.request.cmd)[1]];
 const b=Buffer.concat(paths.map(read));ok(Buffer.from(x.output).equals(b),'root raw whole source/document read');
 pairs.push({kind:rec.role,paths,bytes:b.length,sha256:sha(b)});
}
const ind=json(a+'CHECK_RESULT.json'),f=json(a+'FINDINGS.json');
ok(ind.frontier.targets===164&&ind.frontier.membership_names===292&&ind.frontier.gaps===8&&ind.frontier.allowed_after===207&&ind.frontier.no_changed_target_dictionary,'complete target invariants');
ok(ind.author_closing_keys===46&&ind.author_read_comparisons===25&&ind.author_read_bytes===317714&&ind.independent_read_comparisons===29&&ind.independent_read_bytes===377171,'all original read evidence');
ok(eq(f.census,{Blocker:0,Major:0,Minor:0})&&f.findings.length===0&&f.independence.process_separated&&!f.independence.p212_source_contribution&&!f.independence.p212_proof_contribution&&!f.operational_authorization,'exact source independent verdict only');
read(r+'CHECK_RECEPTION.cjs');
for(const k of keys.values())ok(eq(meta(fs.lstatSync(k.path,{bigint:true})),k.fields),'closing endpoint unchanged');
process.stdout.write(JSON.stringify({scope:'ROOT_DOCUMENTARY_SOURCE_RECEPTION_ONLY',checks,inventory,independent_input_pins:52,root_replays:2,root_artifact_checks:1297,independent_closing_keys:67,root_raw_pairs:pairs.length,root_raw_bytes:pairs.reduce((n,x)=>n+x.bytes,0),pairs,keys:[...keys.values()],observer_executed:false,host_private_input_observed:false,grant:false,manuscript_review:false},null,2)+'\n');
