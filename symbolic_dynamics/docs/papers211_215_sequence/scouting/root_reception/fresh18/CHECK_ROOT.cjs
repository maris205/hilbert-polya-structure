'use strict';
// Root documentary intake only. No scientific code or operational strings run.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics';
const F='docs/papers211_215_sequence/scouting/finite_residual_fresh18/';
const D='docs/papers211_215_sequence/scouting/finite_residual_fresh18_addendum01/';
const A='docs/papers211_215_sequence/scouting/root_reception/fresh18_independent_intake01/';
const R='docs/papers211_215_sequence/scouting/root_reception/fresh18/';
const own=['ROOT_READS_NATIVE.json','ROOT_WEB_NATIVE.json','ROOT_REPLAY_NATIVE.json','ROOT_AUDIT_READS_NATIVE.json','ROOT_AUDIT_REPLAY_NATIVE.json','CHECK_ROOT.cjs'];
const extra=[A+'CHECK_NATIVE.json',A+'REPORT.md',A+'FINAL_READS_NATIVE.json',A+'SHA256SUMS'];
const aEnvelope=JSON.parse(fs.readFileSync(path.join(ROOT,A+'CHECK_NATIVE.json'),'utf8'));
const prior=JSON.parse(aEnvelope.execution.result.output);
const oldKeys=[...prior.input_keys,...prior.own_preclosure_keys];
const allowed=new Set([...oldKeys.map(k=>k.path),...extra,...own.map(n=>R+n)]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
let checks=0;const cache=new Map(),keys=new Map(),pairs=[];
function ok(x,m){checks++;if(!x)throw Error(m);}
function read(p){
 ok(allowed.has(p),'finite document permission '+p);
 const full=path.resolve(ROOT,p),a=fs.lstatSync(full,{bigint:true});
 ok(a.isFile()&&!a.isSymbolicLink(),'regular no-link leaf');
 const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);let data,k;
 try{
  const b=fs.fstatSync(fd,{bigint:true});data=fs.readFileSync(fd);
  const c=fs.fstatSync(fd,{bigint:true}),d=fs.lstatSync(full,{bigint:true});
  for(const s of [b,c,d])ok(same(meta(a),meta(s)),'same-fd/endpoint full ten-field key');
  ok(BigInt(data.length)===a.size,'whole EOF byte count');
  k={path:p,resolved_path:full,sha256:sha(data),metadata:meta(a)};
 }finally{fs.closeSync(fd);}
 if(keys.has(p))ok(same(k,keys.get(p)),'unchanged repeated full key');
 keys.set(p,k);cache.set(p,data);return data;
}
const get=p=>cache.has(p)?cache.get(p):read(p);
const json=p=>JSON.parse(get(p).toString('utf8'));
function raw(a,b,label){
 a=Buffer.isBuffer(a)?a:Buffer.from(a,'utf8');b=Buffer.isBuffer(b)?b:Buffer.from(b,'utf8');
 ok(a.equals(b),'whole raw bytes '+label);pairs.push({label,bytes:a.length,sha256:sha(a)});
}
function slice(b,lo,hi){
 let at=0,line=1;const out=[];
 while(at<b.length){const lf=b.indexOf(10,at),end=lf<0?b.length:lf+1;
  if(line>=lo&&line<=hi)out.push(b.subarray(at,end));if(line>=hi)break;at=end;line++;
 }return Buffer.concat(out);
}
ok(aEnvelope.execution.result.exit_code===0&&aEnvelope.execution.result.chunk_id==='38e49d','actual independent execution');
ok(prior.checks===511&&prior.input_keys.length===31&&prior.own_preclosure_keys.length===6,'full independent census');
for(const k of oldKeys){read(k.path);ok(same(k,keys.get(k.path)),'every original independent full key');}
for(const p of [...extra,...own.map(n=>R+n)])read(p);
const seals=[];
function flatSeal(prefix,digest,count,physical){
 const seal=get(prefix+'SHA256SUMS');ok(sha(seal)===digest,'external exact nonself seal');
 const s=seal.toString('utf8');ok(s.endsWith('\n'),'seal final LF');
 const rows=s.slice(0,-1).split('\n').map(l=>{const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);ok(!!m,'strict flat row');return {hash:m[1],name:m[2]};});
 ok(rows.length===count&&new Set(rows.map(e=>e.name)).size===count&&!rows.some(e=>e.name==='SHA256SUMS'),'nonself exact census');
 ok(same(fs.readdirSync(path.join(ROOT,prefix)).sort(),[...rows.map(e=>e.name),'SHA256SUMS'].sort()),'complete physical inventory');
 let total=seal.length;for(const e of rows){const b=get(prefix+e.name);ok(sha(b)===e.hash,'every nonself payload');total+=b.length;}
 ok(total===physical,'exact packet bytes');seals.push({prefix,payloads:count,files:count+1,physicalBytes:total,seal:digest});
}
flatSeal(D,'64a3ffa4c286f9938ecaac83798015f1a2fd01fff5715f51404871607dcefad8',3,16631);
flatSeal(A,'fe950838508c542d99d649c4d2ec5b3bac8bf6310ac4b2447d15273f70ca1e98',9,772131);
const fm=json(F+'MANIFEST.json');
ok(sha(get(F+'MANIFEST.json'))==='ad679d4d641f466b98070caff403b0e735eeaca2e085076a96c727cd77df3088','fixed original manifest');
ok(fm.excluded_self==='MANIFEST.json'&&fm.entries.length===11&&fm.payload_count===11,'original nonself layout');
ok(same(fs.readdirSync(path.join(ROOT,F)).sort(),[...fm.entries.map(e=>e.path),'MANIFEST.json'].sort()),'all original physical files');
let fb=get(F+'MANIFEST.json').length;
for(const e of fm.entries){const p=F+e.path,b=get(p),k=keys.get(p);ok(k.sha256===e.sha256&&k.resolved_path===e.resolved_path&&same(k.metadata,e.metadata),'whole original manifest key');fb+=b.length;}
ok(fb===486498,'all original packet bytes');seals.push({prefix:F,payloads:11,files:12,physicalBytes:fb,seal:sha(get(F+'MANIFEST.json'))});
const findings=json(A+'FINDINGS.json');
ok(findings.verdict==='ACCEPT_NEGATIVE_INTAKE_WITH_EXPLICIT_CLAIM_EXCLUSION','not blanket PASS');
ok(findings.census.minor_scope===1&&findings.census.frozen_author_wording_exclusions===1&&findings.census.accepted_scope_open===0,'unrepaired singleton scope distinction');
ok(findings.census.new_literals===0&&findings.census.closed_attempt_delta===0&&findings.census.pilots===0&&findings.census.nominations===0,'zero new attempts');
ok(sha(get(A+'REPORT.md'))==='729378adc587d9249a2bf35ed86e42e84e3d01fb660666d03de26a2427b9cce0','independent report pin');
ok(sha(get(A+'PROOF_AUDIT.md'))==='c66ff3c4d38eb4ba0a1bf52f34675afbdf639a95e8a37fcd603fc190fcd3cfe9','independent proof pin');
for(const [p,old,chunk,cmd,n]of [
 [R+'ROOT_REPLAY_NATIVE.json',json(F+'CHECK_NATIVE.json').native,'0abcd0','node '+F+'CHECK_ARTIFACTS.cjs',266],
 [R+'ROOT_AUDIT_REPLAY_NATIVE.json',aEnvelope.execution.result,'bde532','node '+A+'CHECK_INTAKE.cjs',511]]){
 const r=json(p);ok(r.request.cmd===cmd&&r.result.exit_code===0&&r.result.chunk_id===chunk&&!r.result.session_id,'actual inspected root documentary replay');
 ok(JSON.parse(r.result.output).checks===n,'actual root checks');raw(r.result.output,old.output,'complete root replay '+n);
}
const rootReads=[...json(R+'ROOT_READS_NATIVE.json').records,...json(R+'ROOT_AUDIT_READS_NATIVE.json').records];
let receivedReads=0;
for(const r of rootReads){
 const m=/^sed -n '(\d+),(\d+)p' (.+)$/.exec(r.command);
 ok(r.result.exit_code===0&&!r.result.session_id,'actual completed root document read');
 if(m){ok(allowed.has(m[3]),'read exact fixed premise');raw(r.result.output,slice(get(m[3]),Number(m[1]),Number(m[2])),'root source/proof read '+r.result.chunk_id);receivedReads++;}
}
const finalReads=json(A+'FINAL_READS_NATIVE.json').calls;
ok(finalReads.length===4,'four original independent closing note reads');
for(const r of finalReads){const m=/^sed -n '1,3000p' (.+)$/.exec(r.request.cmd);ok(!!m&&r.result.exit_code===0,'actual complete closing note read');raw(r.result.output,get(m[1]),'independent final note '+r.name);}
const prep=json(D+'SEAL_PREPARATION_NATIVE.json');
ok(prep.native.chunk_id==='e04509'&&prep.native.exit_code===0,'original preserved historical preparation');
const pd=JSON.parse(prep.native.output);
ok(pd.checks===150&&pd.prior_unchanged_keys===24&&pd.final_read_pairs===6&&pd.final_read_bytes===29417,'original preparation fields');
ok(same(pd.manifest,fm),'entire generated old manifest received as DATA only');
const web=json(R+'ROOT_WEB_NATIVE.json');
ok(web.records.length===2&&web.records.every(r=>r.request&&r.result),'actual two direct primary-return records; excerpt scope only');
for(const p of [...keys.keys()])read(p);
console.log(JSON.stringify({scope:'ROOT_FRESH18_NEGATIVE_INTAKE_RECEIVED_WITH_SINGLETON_CLAIM_EXCLUSION',checks,keys:[...keys.values()],keyCount:keys.size,oldFullKeysPreserved:oldKeys.length,sealedPackets:seals,rootDocumentReads:receivedReads,rawPairs:pairs,rawPairCount:pairs.length,rawPairedBytes:pairs.reduce((s,p)=>s+p.bytes,0),rootReplays:[266,511],historical150Reexecuted:false,reportedUnstoredClosuresNotClaimedReceived:[22,211],closedAttemptDelta:0,closedAttemptsRemain:59,retained:3,complete:1,openSeats:2,reserves:0,sourceScope:'local full proof and full independent audit; exact old selected premises; direct primary excerpts not whole-source or PDF certification',scientificExecution:false,manuscriptReview:false,externalStatus:'HOLD_EXTERNAL'}));

