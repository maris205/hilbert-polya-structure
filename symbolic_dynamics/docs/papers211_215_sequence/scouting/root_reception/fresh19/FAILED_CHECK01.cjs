'use strict';
// Root fixed-workspace DOCUMENT reception. Never import/evaluate any submitted
// source or query its embedded operational/host/private/future path strings.
const fs=require('node:fs'),crypto=require('node:crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics',D="docs/papers211_215_sequence/scouting/finite_residual_fresh19/",A="docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/",OWN="docs/papers211_215_sequence/scouting/root_reception/fresh19/";
const EXTERNAL=["docs/papers211_215_sequence/scouting/finite_residual_fresh19/PLAN.md","docs/papers211_215_sequence/scouting/finite_residual_fresh19/SOURCE_READS.md","docs/papers211_215_sequence/scouting/finite_residual_fresh19/PROOF_AND_DISPOSITION.md","docs/papers211_215_sequence/scouting/finite_residual_fresh19/HANDOFF.md","docs/papers211_215_sequence/scouting/finite_residual_fresh19/SOURCE_TOOL_RETURNS.json","docs/papers211_215_sequence/scouting/finite_residual_fresh19/LOCAL_TOOL_RETURNS.json","docs/papers211_215_sequence/scouting/finite_residual_fresh19/INPUT_PINS.json","docs/papers211_215_sequence/scouting/finite_residual_fresh19/ARTIFACT_CHECK.json","docs/papers211_215_sequence/scouting/finite_residual_fresh19/manifest_sha256.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/ORIGIN_AND_SCOPE.md","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/REVIEW.md","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/FINDINGS.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/INPUT_PINS.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/PRIMARY_RETURNS.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/LOCAL_READ_RETURNS.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/check_artifacts.mjs","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/ARTIFACT_CHECK.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/ARTIFACT_CHECK_NATIVE.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/close_check.mjs","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/CLOSING_CHECK.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/CLOSING_NATIVE.json","docs/papers211_215_sequence/scouting/root_reception/fresh19_independent_intake01/MANIFEST.sha256","docs/papers211_215_sequence/scouting/finite_metric_reconstruction_scout01/PROOF_PACKAGE.md","docs/papers211_215_sequence/scouting/finite_metric_reconstruction_scout01/SOURCE_READS.md","docs/papers122_126_sequence/scouting/combinatorial/SCOUT.md","docs/papers117_121_sequence/scouting/ALGEBRAIC_PHASE2B_SCOUT.md","docs/papers204_208_sequence/scouting/algebra/PROOF_NOTES.md","papers/106-synchronous-mis-polarity-dynamics/main.tex","docs/papers211_215_sequence/scouting/set_code_lane/PROOF_PACKAGE.md","docs/papers204_208_sequence/scouting/finite_systems_eighteenth/PROOF_AND_ADAPTERS.md","docs/papers211_215_sequence/scouting/finite_residual_fresh18/PROOF_AND_DISPOSITION.md","docs/papers211_215_sequence/scouting/finite_residual_fresh17/PROOF_PACKAGE.md"];
const OWN_INPUTS=['ROOT_READS_NATIVE.json','ROOT_WEB_NATIVE.json','REPLAY_NATIVE.json','check_receipt.cjs'];
const allowed=new Set([...EXTERNAL,...OWN_INPUTS.map(n=>OWN+n)]);
const F=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
let checks=0;const need=(v,m)=>{checks++;if(!v)throw new Error(m);};
const same=(a,b,m)=>need(JSON.stringify(a)===JSON.stringify(b),m);
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const pin=b=>({bytes:b.length,sha256:hash(b)});
const raw=new Map(),keys=new Map(),pairs=[];
const fields=s=>Object.fromEntries(F.map(k=>{need(typeof s[k]==='bigint','actual exact documentary integer');return[k,s[k].toString()];}));
function read(p){
 need(allowed.has(p),'literal documentary whitelist: '+p);if(raw.has(p))return raw.get(p);
 const full=ROOT+'/'+p,l=fs.lstatSync(full,{bigint:true}),L=fields(l);need(l.isFile()&&!l.isSymbolicLink(),'regular physical document');
 const fd=fs.openSync(full,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let bytes,row;
 try{const b=fs.fstatSync(fd,{bigint:true}),B=fields(b);need(b.isFile(),'regular descriptor');same(L,B,'same fd before content');
 const pieces=[],buf=Buffer.alloc(65536);let n,total=0,calls=0;do{n=fs.readSync(fd,buf,0,buf.length,null);calls++;need(n>=0&&n<=65536,'actual read count');if(n){total+=n;need(total<=8388608,'8MiB per-document bound');pieces.push(Buffer.from(buf.subarray(0,n)));}}while(n!==0);
 bytes=Buffer.concat(pieces);const Z=fields(fs.fstatSync(fd,{bigint:true})),E=fields(fs.lstatSync(full,{bigint:true}));same(B,Z,'same fd after zero-return EOF');same(L,E,'stable lexical endpoint');need(bytes.length===total&&BigInt(total)===b.size,'whole count');
 need(Buffer.from(bytes.toString('utf8'),'utf8').equals(bytes),'whole UTF8 roundtrip for any text comparison');
 row={path:p,...pin(bytes),lstat_before:L,fstat_before:B,fstat_after:Z,lstat_after:E,fd,read_calls:calls,last_read_return:n,eof:true,close_succeeded:false};
 }finally{fs.closeSync(fd);}row.close_succeeded=true;raw.set(p,bytes);keys.set(p,row);return bytes;
}
const json=p=>{const b=read(p),v=JSON.parse(b.toString());need(Buffer.from(JSON.stringify(v,null,2)+'\n').equals(b),'canonical whole JSON data '+p);return v;};
function pair(label,a,b){need(a.equals(b),'entire RAW equality '+label);pairs.push({label,...pin(a)});}
function manifest(dir,n,sealPin){
 const b=read(dir+'SHA256SUMS');same(pin(b),sealPin,'received commissioned seal');
 need(b.toString().endsWith('\n'),'seal final LF');const entries=b.toString().slice(0,-1).split('\n').map(l=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);need(m,'strict flat nonself seal row');return {sha256:m[1],name:m[2]};});
 need(entries.length===n&&new Set(entries.map(e=>e.name)).size===n,'complete distinct nonself rows');
 same(fs.readdirSync(ROOT+'/'+dir).sort(),[...entries.map(e=>e.name),'SHA256SUMS'].sort(),'exact frozen physical layout');
 let size=b.length;for(const e of entries){need(e.name!=='SHA256SUMS','no seal self member');const x=read(dir+e.name);need(hash(x)===e.sha256,'whole payload hash');size+=x.length;}return {directory:dir,payloads:n,files:n+1,physical_bytes:size,seal:pin(b)};
}

const SOURCE_NAMES=["PLAN.md","SOURCE_READS.md","PROOF_AND_DISPOSITION.md","HANDOFF.md","SOURCE_TOOL_RETURNS.json","LOCAL_TOOL_RETURNS.json","INPUT_PINS.json","ARTIFACT_CHECK.json","manifest_sha256.json"],AUDIT_NAMES=["ORIGIN_AND_SCOPE.md","REVIEW.md","FINDINGS.json","INPUT_PINS.json","PRIMARY_RETURNS.json","LOCAL_READ_RETURNS.json","check_artifacts.mjs","ARTIFACT_CHECK.json","ARTIFACT_CHECK_NATIVE.json","close_check.mjs","CLOSING_CHECK.json","CLOSING_NATIVE.json","MANIFEST.sha256"],OLD=["docs/papers211_215_sequence/scouting/finite_metric_reconstruction_scout01/PROOF_PACKAGE.md","docs/papers211_215_sequence/scouting/finite_metric_reconstruction_scout01/SOURCE_READS.md","docs/papers122_126_sequence/scouting/combinatorial/SCOUT.md","docs/papers117_121_sequence/scouting/ALGEBRAIC_PHASE2B_SCOUT.md","docs/papers204_208_sequence/scouting/algebra/PROOF_NOTES.md","papers/106-synchronous-mis-polarity-dynamics/main.tex","docs/papers211_215_sequence/scouting/set_code_lane/PROOF_PACKAGE.md","docs/papers204_208_sequence/scouting/finite_systems_eighteenth/PROOF_AND_ADAPTERS.md","docs/papers211_215_sequence/scouting/finite_residual_fresh18/PROOF_AND_DISPOSITION.md","docs/papers211_215_sequence/scouting/finite_residual_fresh17/PROOF_PACKAGE.md"];
for(const p of EXTERNAL)read(p);for(const n of OWN_INPUTS)read(OWN+n);
const data=p=>JSON.parse(read(p).toString('utf8'));
const manifestRaw=read(D+'manifest_sha256.json'),manifestValue=data(D+'manifest_sha256.json');
same(pin(manifestRaw),{bytes:1447,sha256:'6e2f1f2508b46072b07b68d1023d5a0813739a1855003524eca649b3282883f6'},'exact author seal');
same(manifestValue.files.map(r=>r.path),SOURCE_NAMES.slice(0,8),'all eight source payload roles');
for(const r of manifestValue.files)same(pin(read(D+r.path)),{bytes:r.bytes,sha256:r.sha256},'whole submitted source payload');
same(fs.readdirSync(ROOT+'/'+D).sort(),SOURCE_NAMES.slice().sort(),'exact nine submitted files');
const auditSeal=read(A+'MANIFEST.sha256');same(pin(auditSeal),{bytes:1019,sha256:'67734126376f76b95a607b6f5dce97f745d44ffcb6d5b2ed15e0470ce12ca32d'},'exact independent seal');
need(auditSeal.toString().endsWith('\n'),'seal LF');
const sealRows=auditSeal.toString().slice(0,-1).split('\n').map(l=>{const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);need(m,'strict nonself flat seal');return{sha256:m[1],name:m[2]};});
same(sealRows.map(r=>r.name),AUDIT_NAMES.slice(0,12),'all twelve independent payload roles');
for(const r of sealRows)need(hash(read(A+r.name))===r.sha256,'whole independent payload');
same(fs.readdirSync(ROOT+'/'+A).sort(),AUDIT_NAMES.slice().sort(),'exact thirteen independent files');
const sourceBytes=SOURCE_NAMES.reduce((n,p)=>n+read(D+p).length,0),auditBytes=AUDIT_NAMES.reduce((n,p)=>n+read(A+p).length,0);
need(sourceBytes===625497&&auditBytes===443550,'complete physical byte counts');
const sourceOld=data(D+'INPUT_PINS.json'),input=data(A+'INPUT_PINS.json');same(sourceOld.files.map(r=>r.path),OLD,'exact ten old filenames');
for(const r of sourceOld.files)same(pin(read(r.path)),{bytes:r.bytes,sha256:r.sha256},'old complete bytes unchanged');
same(input.files.map(r=>r.path),[...SOURCE_NAMES.map(n=>D+n),...OLD],'exact independent nineteen pin roles');
for(const r of input.files)same(pin(read(r.path)),{bytes:r.bytes,sha256:r.sha256},'independent complete input pin');
const independent=data(A+'ARTIFACT_CHECK.json'),native=data(A+'ARTIFACT_CHECK_NATIVE.json'),closing=data(A+'CLOSING_CHECK.json'),nclose=data(A+'CLOSING_NATIVE.json'),replays=data(OWN+'REPLAY_NATIVE.json');
need(native.actual_return.chunk_id==='6ddd26'&&native.actual_return.exit_code===0&&nclose.actual_return.chunk_id==='11db8f'&&nclose.actual_return.exit_code===0,'exact original independent returns');
pair('independent artifact actual stdout',Buffer.from(native.actual_return.output),read(A+'ARTIFACT_CHECK.json'));
pair('independent original closing stdout',Buffer.from(nclose.actual_return.output),read(A+'CLOSING_CHECK.json'));
need(replays.records.length===2,'exact root replay count');const [r,c]=replays.records;
need(r.actual_return.chunk_id==='e75106'&&r.actual_return.exit_code===0&&c.actual_return.chunk_id==='a22eb5'&&c.actual_return.exit_code===0,'actual root documentary successes');
need(r.request.cmd==='node '+A+'check_artifacts.mjs'&&c.request.cmd==='node '+A+'close_check.mjs --sealed','exact reviewed documentary entries');
pair('root artifact replay entire stdout',Buffer.from(r.actual_return.output),read(A+'ARTIFACT_CHECK.json'));
const sealed=JSON.parse(c.actual_return.output);need(sealed.base_assertion_count===23&&sealed.sealed_assertion_count===7&&sealed.physical_bytes===443550&&Object.values(sealed.base_assertions).every(Boolean)&&Object.values(sealed.sealed_assertions).every(Boolean),'actual final root sealed closure');
need(independent.assertion_count===66&&Object.keys(independent.assertions).length===66&&Object.values(independent.assertions).every(v=>v===true),'all actual independent assertions');
need(closing.assertion_count===23&&Object.keys(closing.assertions).length===23&&Object.values(closing.assertions).every(v=>v===true),'all historical closing assertions');
const author=data(D+'ARTIFACT_CHECK.json'),local=data(D+'LOCAL_TOOL_RETURNS.json'),web=data(D+'SOURCE_TOOL_RETURNS.json');
need(local.records.length===18&&web.records.length===13&&author.result.chunk_id==='51ca6c'&&author.result.exit_code===0,'whole author native roles');
need(local.records[0].exit_code===2&&!Object.hasOwn(local.records[0],'cmd'),'missing failed command remains missing');
const lineRange=(b,a,z)=>Buffer.from(b.toString().split(/(?<=\n)/).slice(a-1,z).join(''));
const rows=[[3,OLD[8],null],[4,OLD[9],null],[9,OLD[0],null],[10,OLD[2],[1,62]],[11,OLD[2],[228,272]],[12,OLD[3],[328,350]],[13,OLD[4],null],[14,OLD[5],null],[15,OLD[6],[1,58]],[16,OLD[7],null],[17,OLD[1],null]];
for(const [i,p,range]of rows){const n=local.records[i];pair('old exact source read '+i,Buffer.from(n.r.output),range?lineRange(read(p),...range):read(p));}
pair('author old-pin actual stdout',Buffer.from(local.pin_read.r.output),Buffer.from(JSON.stringify(sourceOld.files,null,2)+'\n'));
const expectedAuthor={kind:'AUTHOR_ARTIFACT_CHECK_ONLY',scientific_execution:false,independent_review:false,verdict:'PASS_ARTIFACTS_ONLY',files:manifestValue.files.slice(0,7).map(f=>({name:f.path,bytes:f.bytes,sha256:f.sha256})),source_record_count:13,local_record_count:18,input_pin_count:10,old_inputs:OLD.map(path=>({path,match:true})),exact_owned_file_set:true};
pair('author historical pre-manifest complete stdout',Buffer.from(author.result.output),Buffer.from(JSON.stringify(expectedAuthor,null,2)+'\n'));
for(const p of independent.local_output_pins){const n=p.index===0?local.records[0]:local.records[p.index].r;need(n.chunk_id===p.chunk_id&&n.exit_code===p.exit_code,'original local return scalar');same(pin(Buffer.from(n.output)),{bytes:p.bytes,sha256:p.sha256},'whole local output string pin');}
for(const p of independent.web_return_pins){const w=web.records.find(r=>r.key===p.key);need(w,'original primary role');same(pin(Buffer.from(w.result)),{bytes:p.bytes,sha256:p.sha256},'whole web return string pin not publisher bytes');}
const f=data(A+'FINDINGS.json');need(f.verdict==='ACCEPT_BOUNDED_NEGATIVE_DESK'&&f.personal_author_noncontribution&&f.author_contact===false&&f.root_adoption_performed===false,'independent scope no root impersonation');
for(const k of ['critical','major','minor','current_open','examined_new_literal_count','pilot_proposals','scientific_executions','nominations','reserves'])need(f[k]===0,'exact zero '+k);need(f.findings.length===0,'zero actual findings');
const selected=data(OWN+'ROOT_READS_NATIVE.json');let selectedPairs=0;
for(const n of selected.records){const m=/^sed -n '(\d+),(\d+)p' ([A-Za-z0-9_./-]+)$/.exec(n.request.cmd);if(!m||!allowed.has(m[3])||n.result.exit_code!==0)continue;
need(!n.result.output.includes('Warning: truncated output'),'selected full native read range');pair('root selected range '+n.result.chunk_id,Buffer.from(n.result.output),lineRange(read(m[3]),Number(m[1]),Number(m[2])));selectedPairs++;}
console.log(JSON.stringify({schema:'fresh19-root-documentary-reception-v1',status:'PASS_EXACT_DOCUMENTARY_ORIGINALS_ZERO_COUNT_DELTA',checks,source_payloads:8,source_files:9,source_bytes:sourceBytes,audit_payloads:12,audit_files:13,audit_bytes:auditBytes,keys_count:keys.size,old_pins:10,raw_pairs:pairs,raw_pair_bytes:pairs.reduce((n,p)=>n+p.bytes,0),selected_root_read_pairs:selectedPairs,new_literals:0,pilot_proposals:0,scientific_runs:0,nominations:0,reserves:0,count_delta:0,keys:[...keys.values()],limits:'Original reviewer helper inspects literal workspace document ancestor metadata. No operational host/prospective strings followed, no scientific code run. Old outputs/website strings are DATA; primary proof scope and interpretation are separately in RECEPTION.md.'},null,2));
