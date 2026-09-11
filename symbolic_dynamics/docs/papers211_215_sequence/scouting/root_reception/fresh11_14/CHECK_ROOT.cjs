'use strict';
// Root documentary receiver only: fixed frozen packets, root readback slices and archival browser data.
const fs=require('fs'),path=require('path'),c=require('crypto');
const W='/root/autodl-tmp/symbolic_dynamics/',S='docs/papers211_215_sequence/scouting/';
const R=S+'root_reception/fresh11_14/',A=S+'root_reception/fresh11_14_independent_intake01/';
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs'];
const outside=new Set(['/root/autodl-tmp/.codex/skills/research-lit/SKILL.md','/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md']);
const bodies=new Map(),keys=new Map(),pairs=[];let checks=0;
const sha=b=>c.createHash('sha256').update(b).digest('hex'),eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const ok=(v,m)=>{checks++;if(!v)throw Error(m);};
function shape(s){return Object.fromEntries(F.map(n=>[n,String(s[n])]));}
function read(p){
 ok((!path.isAbsolute(p)&&!p.split('/').includes('..')&&(p.startsWith('docs/')||p.startsWith('papers/')||p.startsWith('.agents/')))||outside.has(p),'document selected before filesystem operand');
 if(bodies.has(p))return bodies.get(p);const real=path.isAbsolute(p)?p:W+p;
 const l=fs.lstatSync(real,{bigint:true});ok(l.isFile()&&!l.isSymbolicLink()&&l.size<15000000n,'bounded physical regular document');
 const fd=fs.openSync(real,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b,m;
 try{m=shape(fs.fstatSync(fd,{bigint:true}));ok(eq(m,shape(l)),'same selected descriptor');b=fs.readFileSync(fd);ok(eq(m,shape(fs.fstatSync(fd,{bigint:true}))),'unchanged fd');}finally{fs.closeSync(fd);}
 ok(eq(m,shape(fs.lstatSync(real,{bigint:true})))&&BigInt(b.length)===l.size,'complete stable endpoint');
 bodies.set(p,b);keys.set(p,{path:p,type:'regular',...m,bytes:b.length,sha256:sha(b)});return b;
}
function str(p){const b=read(p),s=b.toString('utf8');ok(Buffer.from(s).equals(b),'lossless text');return s;}
const json=p=>JSON.parse(str(p));
function pair(kind,raw,expected,detail){ok(raw.equals(expected),'actual raw pair '+kind);pairs.push({kind,...detail,bytes:raw.length,sha256:sha(raw)});}
const seal=str(A+'SHA256SUMS');ok(sha(Buffer.from(seal))==='3c2261559ab7d429b967f603df2599639a0430112f4fb9d6eb36992a27378f64'&&seal.endsWith('\n')&&!seal.endsWith('\n\n'),'fixed final independent seal');
const rows=seal.slice(0,-1).split('\n'),names=[];ok(rows.length===13,'all independent payloads');
for(const l of rows){const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);ok(m&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'unique nonself name');names.push(m[2]);ok(sha(read(A+m[2]))===m[1],'complete independent payload');}
ok(eq(fs.readdirSync(A).sort(),[...names,'SHA256SUMS'].sort()),'entire independent physical inventory');
const originals=json(A+'CHECK_NATIVE.json'),old=JSON.parse(originals.result.output);
const replays=json(R+'ROOT_REPLAYS_NATIVE.json').records;
ok(originals.result.exit_code===0&&!originals.result.session_id&&replays.length===2,'original/replay scope');
for(const [i,n]of [[0,'CHECK_NATIVE.json'],[1,'CLOSING_NATIVE.json']]){
 const v=replays[i].response,o=json(A+n).result;ok(v.exit_code===0&&o.exit_code===0&&!v.session_id&&!o.session_id,'actual finite documentary replay');
 pair('fresh root documentary replay',Buffer.from(v.output),Buffer.from(o.output),{path:A+n,chunk:v.chunk_id});
}
ok(old.checks===5398&&old.totalUniqueDocumentaryKeys===96&&old.totalDeclaredPins===75&&old.totalRecords===141&&old.totalNativeRecords===118&&old.totalWebRecords===23&&old.exceptions.length===22,'complete independent census');
for(const k of old.fullKeys){read(k.path);ok(eq(keys.get(k.path),k),'all 13-field original whole keys unchanged');}
ok(eq(old.packageRows.map(x=>[x.payloads,x.files]),[[8,9],[7,8],[16,17],[8,9]])&&old.packageRows.reduce((n,x)=>n+x.totalBytes,0)===1634923,'four complete parent inventories');
ok(old.childSeal.payloads===7&&old.childSeal.files===8&&old.childSeal.totalBytes===35541,'child failed packet received without double counting');
ok(old.historicalAdapters.length===4&&old.pins.filter(x=>x.historicalAdapter).length===4,'four explicit historical adapters');
for(const p of old.pins){ok(sha(read(p.physical))===p.sha256&&read(p.physical).length===p.bytes,'all original pins at exact mapped physical documents');}
const rr=json(R+'ROOT_READS_NATIVE.json').records;ok(rr.length===21,'selected substantive raw scope');
for(const x of rr){
 const cmd=x.request.cmd,res=x.response;
 if(x.role==='fresh14_sources_root_read'){ok(res.exit_code===2&&res.output.includes('No such file or directory'),'root guessed-path failure retained');continue;}
 ok(res.exit_code===0&&!res.session_id,'actual completed root read');
 let p,m,body;
 if((m=/^cat ([A-Za-z0-9_./-]+)$/.exec(cmd))){p=m[1];body=read(p);}
 else {m=/^sed -n '([0-9]+),([0-9]+)p' ([A-Za-z0-9_./-]+)$/.exec(cmd);ok(m,'explicit whole/range command');p=m[3];const lines=read(p).toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];body=Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join(''));}
 pair('root exact document/range',Buffer.from(res.output),body,{role:x.role,path:p,command:cmd});
}
const pr=json(R+'PRIMARY_NATIVE.json');ok(typeof pr.direct_browser.response==='string'&&pr.direct_browser.request.open.length===3,'actual direct browser response retained as string');
ok(pr.direct_browser.response.includes('The probability that an operator is nilpotent')&&pr.direct_browser.response.includes('###### Theorem 5.')&&pr.direct_browser.response.includes('Timeout fetching'),'Leinster body and two failures not converted to all-source success');
for(const x of pr.archive_readbacks){
 ok(x.response.exit_code===0&&!x.response.session_id,'actual complete archived source response read');
 const data=json(x.source_archive),arr=Array.isArray(data)?data:data.records,v=arr[x.record_index];ok(v&&typeof(v.response||v.result)==='string','exact archived response identity');
 pair('root archived primary body',Buffer.from(x.response.output),Buffer.from(v.response||v.result),{source_archive:x.source_archive,record_index:x.record_index,chunk:x.response.chunk_id});
}
const failed=json(A+'CHECK01_FAILED_NATIVE.json'),truncated=json(A+'CHECK02_TRUNCATED_NATIVE.json');ok(failed.result.exit_code===1&&truncated.result.output.startsWith('Warning: truncated output'),'actual intake failures retained');
ok(str(A+'SELF_FAILURES.md').includes('source')&&str(A+'PLAN.md').includes('1/0/0/1'),'scope/task corrections retained');
read(R+'CHECK_ROOT.cjs');
for(const k of keys.values()){const abs=path.isAbsolute(k.path)?k.path:W+k.path;ok(eq(shape(fs.lstatSync(abs,{bigint:true})),Object.fromEntries(F.map(n=>[n,k[n]]))),'closing full endpoint');}
process.stdout.write(JSON.stringify({scope:'ROOT_NEGATIVE_SCOUT_ARTIFACT_RECEPTION_ONLY',checks,independent_payloads:13,independent_physical_files:14,independent_physical_bytes:[...names,'SHA256SUMS'].reduce((n,x)=>n+read(A+x).length,0),original_parent_payloads:39,original_physical_files:43,original_input_pins:75,original_keys:96,original_records:141,original_exceptions:22,root_raw_pairs:pairs.length,root_raw_bytes:pairs.reduce((n,x)=>n+x.bytes,0),pairs,keys:[...keys.values()],new_mathematical_admission:false,new_science:false,new_host_private_runtime_observation:false},null,2)+'\n');
