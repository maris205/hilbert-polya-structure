// Root documentary intake only. Never executes/parses Python/Bash or follows embedded host paths.
'use strict';
const fs=require('node:fs'),crypto=require('node:crypto');
const q='docs/papers211_215_sequence/qa/',r=q+'p213_minimal_observer_source_delta_root01/';
const a=q+'p213_minimal_observer_source_delta_audit01/',d=q+'p213_minimal_observer_source_delta01/',p=q+'p213_minimal_observer_binding_preparation01/';
const special=new Set([q+'root_replays/p211_author_pair_01/child01/RUNTIME_BEFORE.json',...['SHA256SUMS','INVENTORY.json','CHECKPOINT.md'].map(n=>q+'quota_interruption_checkpoint01/'+n)]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
let checks=0;const keys=new Map(),bodies=new Map(),pairs=[];
const ok=(v,m)=>{checks++;if(!v)throw Error(m);};
const eq=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function meta(s){return Object.fromEntries(fields.map(n=>{ok(typeof s[n]==='bigint','integer field');return[n,String(s[n])];}));}
function read(path){
 ok((path.startsWith(q+'p213_')||special.has(path))&&!path.split('/').includes('..'),'selected documentary path');
 if(bodies.has(path))return bodies.get(path);
 const s=fs.lstatSync(path,{bigint:true});ok(s.isFile()&&!s.isSymbolicLink()&&s.nlink===1n&&s.size<10000000n,'bounded regular single-link document');
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b,m,z;
 try{const t=fs.fstatSync(fd,{bigint:true});ok(t.isFile(),'regular descriptor');m=meta(t);ok(eq(m,meta(s)),'initial fd/path');b=fs.readFileSync(fd);z=meta(fs.fstatSync(fd,{bigint:true}));}finally{fs.closeSync(fd);}
 ok(eq(m,z)&&eq(m,meta(fs.lstatSync(path,{bigint:true})))&&BigInt(b.length)===BigInt(m.size),'complete stable document');
 bodies.set(path,b);keys.set(path,{path,bytes:b.length,sha256:sha(b),metadata:m});return b;
}
function text(path){const b=read(path),s=b.toString('utf8');ok(Buffer.from(s).equals(b),'lossless UTF8');return s;}
const json=path=>JSON.parse(text(path));
const inventory=[];
for(const [dir,n,pin]of [[a,25,'303fe92c49db404336292532c9201b95925159f036d84508628d8dbd4b137ff4'],[d,24,'98ed7e008e16eef37dfb37dcbb00060cef97479957ef25f4df939b6e3314ee34'],[p,21,'98f27ead29fa8862591d3b5a4cc6813eea1f09814f5d03a5edce0571ab278d96']]){
 const s=text(dir+'SHA256SUMS');ok(sha(Buffer.from(s))===pin&&s.endsWith('\n')&&!s.endsWith('\n\n'),'fixed strict seal');
 const ls=s.slice(0,-1).split('\n'),names=[];ok(ls.length===n,'payload count');
 for(const l of ls){const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(l);ok(m&&m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'unique nonself basename');names.push(m[2]);ok(sha(read(dir+m[2]))===m[1],'payload raw hash');}
 ok(eq(fs.readdirSync(dir).sort(),[...names,'SHA256SUMS'].sort()),'entire physical inventory');
 inventory.push({path:dir,payloads:n,files:n+1,bytes:[...names,'SHA256SUMS'].reduce((n,s)=>n+read(dir+s).length,0),seal_sha256:pin});
}
function compareKey(k){read(k.path);const now=keys.get(k.path);ok(now.bytes===k.bytes&&now.sha256===k.sha256&&eq(now.metadata,k.metadata||k.ten_fields),'original full key unchanged '+k.path);}
const pins=text(a+'INPUTS.sha256').trimEnd().split('\n');ok(pins.length===71,'all 71 independent input pins');const seen=new Set();
for(const l of pins){const m=/^([a-f0-9]{64})  (docs\/[A-Za-z0-9_./-]+)$/.exec(l);ok(m&&!seen.has(m[2]),'unique input');seen.add(m[2]);ok(sha(read(m[2]))===m[1],'input pin');}
const replay=json(r+'ROOT_REPLAYS_NATIVE.json').records;
for(const [i,origPath,count,nkeys]of [[0,d+'CHECK_NATIVE.json',5031,31],[1,p+'CHECK_NATIVE.json',2484,18],[2,a+'CHECK_NATIVE.json',13039,75]]){
 const now=replay[i].result,old=json(origPath).result;ok(now.exit_code===0&&old.exit_code===0&&!now.session_id&&!old.session_id,'actual finite replay exits');
 const b=Buffer.from(now.output);ok(b.equals(Buffer.from(old.output)),'fresh root raw stdout equal');
 const j=JSON.parse(now.output);ok(j.checks===count&&j.keys.length===nkeys,'replay scope census');for(const k of j.keys)compareKey(k);
 pairs.push({kind:'fresh_root_replay',path:origPath,chunk:now.chunk_id,bytes:b.length,sha256:sha(b),checks:count,keys:nkeys});
}
const received=JSON.parse(replay[2].result.output);
ok(received.raw_pair_count===47&&received.raw_pair_bytes===592867&&received.complete_diff_count===6&&received.baseline_keys_unchanged===68,'full independent evidence census');
const finalCarrier=json(a+'FINAL_CLOSING_NATIVE.json');ok(finalCarrier.result.exit_code===0&&!finalCarrier.result.session_id,'successful final audit closure');
const final=JSON.parse(finalCarrier.result.output);ok(final.checks===5767&&final.keys.length===95&&final.preclosing_payloads===24&&final.own_raw_pair_bytes===42417,'final census');
for(const k of final.keys)compareKey(k);
const failed=json(a+'CLOSING_NATIVE.json');ok(failed.result.exit_code===1&&failed.result.output.includes('five own raw bodies total'),'first closure failure retained');
const diagnosis=json(a+'CLOSING_BYTE_COUNT_NATIVE.json');ok(diagnosis.result.exit_code===0,'actual byte diagnosis');const diag=JSON.parse(diagnosis.result.output);ok(diag.characters===42411&&diag.utf8_bytes===42417,'measured bytes not characters');
for(const x of json(a+'READBACK_NATIVE.json').records){ok(x.result.exit_code===0&&!x.result.session_id&&Buffer.from(x.result.output).equals(read(x.path)),'five own raw readback');pairs.push({kind:'independent_final_readback',path:x.path,bytes:read(x.path).length,sha256:sha(read(x.path))});}
const rr=json(r+'ROOT_READS_NATIVE.json').records;ok(rr.length===23,'all selected root raw read records');
for(const x of rr){if(x.role.startsWith('binding_')||x.role==='policy_dispositions')continue;const m=/ (docs\/[A-Za-z0-9_./-]+)$/.exec(x.request.cmd);ok(m&&x.result.exit_code===0&&!x.result.session_id,'whole selected root read');ok(Buffer.from(x.result.output).equals(read(m[1])),'whole root native raw body');pairs.push({kind:'root_whole_document',path:m[1],bytes:read(m[1]).length,sha256:sha(read(m[1]))});}
const parts=['binding_1_750','binding_751_1500','binding_1501_2179'].map(role=>rr.find(x=>x.role===role));ok(parts.every(x=>x&&x.result.exit_code===0&&!x.result.session_id),'three actual binding segments');
const bindingBytes=Buffer.concat(parts.map(x=>Buffer.from(x.result.output)));ok(bindingBytes.equals(read(d+'BINDING.disabled.json')),'complete 2179-line binding raw concatenation');pairs.push({kind:'root_whole_binding',path:d+'BINDING.disabled.json',bytes:bindingBytes.length,sha256:sha(bindingBytes)});
const f=json(a+'FINDINGS.json');ok(f.current_source_policy_census.open===0&&f.current_source_policy_census.Major===0&&f.original_census_unchanged.open===2&&f.findings.length===2&&f.findings.every(x=>x.original_status==='OPEN'&&x.delta_status==='CLOSED_IN_EXACT_SOURCE_POLICY_COMBINATION'),'exact derivative findings no history rewrite');
ok(!f.enabled_literal_accepted&&!f.probe_authorized&&!f.runtime_observed_or_accepted&&!f.reviewed_programs_executed_or_parsed,'remaining gates explicit');
const oldFindings=json(q+'p213_minimal_observer_source_audit01/FINDINGS.json');
ok(text(q+'p213_minimal_observer_source_audit01/FINDINGS.json').includes('P213-MOS-F01')&&text(q+'p213_minimal_observer_source_audit01/FINDINGS.json').includes('P213-MOS-F02'),'original finding identities preserved');
read(r+'CHECK_RECEPTION.cjs');read(r+'PRIMARY_SCOPE.json');
for(const k of keys.values())ok(eq(meta(fs.lstatSync(k.path,{bigint:true})),k.metadata),'closing endpoint');
process.stdout.write(JSON.stringify({scope:'ROOT_DOCUMENTARY_RECEPTION_ONLY',checks,inventory,independent_input_pins:71,independent_checks:13039,independent_raw_pairs:47,independent_raw_bytes:592867,independent_final_keys:95,root_replay_count:3,root_raw_pairs:pairs.length,root_raw_bytes:pairs.reduce((n,x)=>n+x.bytes,0),pairs,keys:[...keys.values()],source_policy_accepted_by_checker:false,runtime_accepted:false,observer_executed:false},null,2)+'\n');
