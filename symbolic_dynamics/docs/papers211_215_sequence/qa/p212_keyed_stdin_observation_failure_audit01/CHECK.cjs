'use strict';
// Independent archive DATA checker. Never executes/imports the observer, a
// recorded command, a target, or any dynamically recovered host pathname.
const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert/strict');
const ROOT = '/root/autodl-tmp/symbolic_dynamics/';
const QA = ROOT + 'docs/papers211_215_sequence/qa/';
const R = QA + 'p212_keyed_stdin_observation_root01/';
const S = QA + 'p212_keyed_stdin_source_delta01/';
const OWN = QA + 'p212_keyed_stdin_observation_failure_audit01/';
const PRIVATE = '/root/symbolic-dynamics-p212-keyed-stdin-observation-20260910-01';
const STDIN = QA + 'p212_keyed_stdin_input01/empty.stdin';
const STOP = '/etc/alternatives/cuda-12';
const EMPTY = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855';
const DOC_FIELDS = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const FIELDS = ['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const IDENTITY = ['dev','ino','mode','uid','gid','rdev','birthtimeNs'];
let checks = 0;
function ok(v, label) { checks++; assert(v, label); }
function eq(a, b, label) { checks++; assert.deepEqual(a, b, label); }
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const canonical = x => JSON.stringify(x, null, 2) + '\n';
const meta = s => Object.fromEntries(DOC_FIELDS.map(k => [k,String(s[k])]));
const objects = new Map(), keys = new Map();
const selection = new Set([
  ...['GRANT.md','REQUEST.json','ARGV.json','AUTHORIZATION.json','RELOCATED_TRUST_DECISION.json',
  'REQUEST_RECEPTION_NATIVE.json','CAPTURE_PREPARATION_NATIVE.json','ACTUAL_OBSERVER_NATIVE.json',
  'INITIAL_RAW_INTAKE_NATIVE.json','FAILURE_SHAPE_NATIVE.json','CAPTURE_PREPARATION_DECISION.md',
  'PROPOSAL_RECEPTION.md','PROPOSAL_CHECK_NATIVE.json','PROPOSAL_SHAPE_NATIVE.json',
  'PROPOSAL_REPLAY_NATIVE.json','PROPOSAL_READS_NATIVE.json'].map(n=>R+n),
  S+'observe.py',S+'FRONTIER.json',
  QA+'p212_trusted_product_boundary_root01/RECEPTION.md',
  QA+'p212_trusted_product_boundary_root01/DECISION.json',
  ROOT+'AGENTS.md',ROOT+'.agents/skills/symbolic-dynamics-research/SKILL.md',
  ROOT+'docs/research_state/WORKFLOW.md'
]);
const packets = [
 ['p212_keyed_stdin_source_root01',16,'0f65f815ca28d4153bc968b0d8dd041f3571287ebe639c942abce6064bb32380'],
 ['p212_keyed_stdin_nonlineage_audit01',24,'ff622be9502a7bd931820cf1c22b5e858bc09243ef3e0488fe7d65cfbea71887'],
 ['p212_keyed_stdin_input_preparation_root01',5,'aa3d3cf04d02766b6efe6c9184c81876bac019472ca915cecc5d17239b7b9bca']
];
for (const [name] of packets) selection.add(QA+name+'/SHA256SUMS');
// Only these two private files may be read; no raw-derived pathname is fed to fs.
for (const name of ['stdout.raw','stderr.raw']) selection.add(PRIVATE+'/'+name);
function read(p) {
  ok(selection.has(p), 'explicit finite document/two-original read selection');
  const before = fs.lstatSync(p,{bigint:true});
  ok(before.isFile()&&!before.isSymbolicLink()&&before.size<=134217728n,'physical bounded regular original');
  if(p.startsWith(PRIVATE+'/')) { eq(before.uid,0n,'private owner'); eq(before.mode&0o777n,0o600n,'private permissions'); }
  const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let data, opening, closing;
  try {
    opening=meta(fs.fstatSync(fd,{bigint:true})); eq(opening,meta(before),'same-fd opening ten-field key');
    data=fs.readFileSync(fd); closing=meta(fs.fstatSync(fd,{bigint:true}));
    eq(closing,opening,'same-fd closing ten-field key');
  } finally { fs.closeSync(fd); }
  eq(meta(fs.lstatSync(p,{bigint:true})),opening,'path endpoint ten-field key');
  eq(String(data.length),opening.size,'whole bytes');
  const key={path:p,bytes:data.length,sha256:sha(data),metadata:opening};
  if(keys.has(p)) eq(key,keys.get(p),'unchanged complete key');
  keys.set(p,key); objects.set(p,data); return data;
}
const packetResults=[];
for(const [name,count,digest] of packets) {
  const base=QA+name+'/', seal=read(base+'SHA256SUMS'); eq(sha(seal),digest,'fixed packet seal');
  const rows=seal.toString().trimEnd().split('\n').map(line=>{
    const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);ok(m&&m[2]!=='SHA256SUMS','bare-relative manifest');
    selection.add(base+m[2]);return {name:m[2],sha256:m[1]};
  });
  eq(rows.length,count,'complete payload count');eq(new Set(rows.map(x=>x.name)).size,count,'unique names');
  eq(fs.readdirSync(base).sort(),[...rows.map(x=>x.name),'SHA256SUMS'].sort(),'physical packet membership');
  for(const row of rows)eq(sha(read(base+row.name)),row.sha256,'whole payload');
  packetResults.push({directory:base,payloads:count,files:count+1,seal_sha256:digest});
}
for(const p of selection) if(!objects.has(p)&&!p.startsWith(PRIVATE+'/'))read(p);
const json = p => JSON.parse(objects.get(p));
const source=objects.get(S+'observe.py');
eq(source.length,22106,'exact source bytes');eq(source.toString().split('\n').length-1,436,'exact full source lines');
eq(sha(source),'957baf304ecbd458c9f02830bc1c65d81a5c4b720b334d1abcfd697895b57537','exact observer source');
const auth=json(R+'AUTHORIZATION.json'),argv=json(R+'ARGV.json'),request=json(R+'REQUEST.json');
const trust=json(R+'RELOCATED_TRUST_DECISION.json'),native=json(R+'ACTUAL_OBSERVER_NATIVE.json');
for(const name of ['AUTHORIZATION.json','ARGV.json','REQUEST.json','RELOCATED_TRUST_DECISION.json'])
  eq(objects.get(R+name),Buffer.from(canonical(json(R+name))),'canonical request/control');
eq(native.request,request,'actual exact submitted request');eq(native.return.chunk_id,'ad435d');
eq(native.return.exit_code,78);eq(native.return.output,'');eq(native.return.original_token_count,0);
ok(!('session_id' in native.return),'settled invocation, no yielded process');
eq(auth.enabled,true);eq(auth.status,'ROOT_BOUND_FINITE_OBSERVATION_ONLY');eq(auth.provenance,trust.provenance);
eq(argv,[...trust.exact_native_prefix,canonical(auth)],'whole canonical final argument');
eq(argv.length,16);eq(trust.scope.maximum_observer_invocations,1);eq(trust.scope.automatic_retries,0);
eq(trust.author_probes_authorized,false);eq(trust.historical_prefix_relocation_automatic,false);
const q=s=>"'"+s.replace(/'/g,"'\"'\"'")+"'";
eq(request,{cmd:'umask 077\nset -C\nexec '+argv.map(q).join(' ')+' < '+q(STDIN)+' > '+q(PRIVATE+'/stdout.raw')+' 2> '+q(PRIVATE+'/stderr.raw')+'\n',workdir:ROOT.slice(0,-1),shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:2000},'exact one-call native binding');
function archived(name,chunk,exit=0) {
 const n=json(R+name);eq(n.return.chunk_id,chunk,'native original identity');eq(n.return.exit_code,exit,'native settlement');
 return JSON.parse(n.return.output);
}
const requestReception=archived('REQUEST_RECEPTION_NATIVE.json','b3af8f');
eq(requestReception.request,request);eq(requestReception.argv,argv);eq(requestReception.checks,891);
eq(requestReception.keys.length,44);eq(requestReception.actual_observer_invocations,0);
const capturePreparation=archived('CAPTURE_PREPARATION_NATIVE.json','79af47');
eq(capturePreparation.status,'CAPTURE_PREPARED_NO_OBSERVER_GRANT');eq(capturePreparation.members,[]);
const initial=archived('INITIAL_RAW_INTAKE_NATIVE.json','484d04');
const shape=archived('FAILURE_SHAPE_NATIVE.json','b9c08f');
// No new query of the input or its ancestors: archived preparation is DATA.
const inputPreparation=JSON.parse(json(QA+'p212_keyed_stdin_input_preparation_root01/PREPARATION_NATIVE.json').return.output);
eq(inputPreparation.input,requestReception.input_standard_key,'archived input ten-field agreement');
for(const k of requestReception.keys) {
 const p=k.path.startsWith(ROOT)?k.path:ROOT+k.path;
 if(keys.has(p))eq({...keys.get(p),path:k.path},k,'selected request-reception whole ten-field key');
}
const d0=fs.lstatSync(PRIVATE,{bigint:true});ok(d0.isDirectory()&&!d0.isSymbolicLink(),'physical exact private directory');
eq(d0.uid,0n);eq(d0.mode&0o777n,0o700n);
for(const f of ['dev','ino','mode','uid','gid','rdev'])eq(String(d0[f]),capturePreparation.directory_metadata[f],'capture stable identity');
const raw=read(PRIVATE+'/stdout.raw'),err=read(PRIVATE+'/stderr.raw');
eq(raw.length,7802105);eq(sha(raw),'4c430a238251197d811a03b3f43e148ceed9ca34d4381ecaa0da284cf59e2f50');
eq(err.length,0);eq(sha(err),EMPTY);
for(const k of initial.keys)eq(keys.get(k.path),k,'same private originals as root intake');
const result=JSON.parse(raw);
eq(raw,Buffer.from(canonical(result)),'whole canonical raw JSON, no ignored trailing bytes/duplicates');
eq(Object.keys(result),['schema','status','provenance','observer_bootstrap_attested','author_probe_executed','closure_certified','controls','closing_controls','passes','errors','closure_gaps','native_events','path_events','actual_read_bytes','actual_captured_bytes']);
eq(result.schema,'p212-independent-preprobe-observation-v1');eq(result.status,'HOLD_FINITE_OBSERVATION_ERRORS');
eq(result.provenance,auth.provenance);eq(result.observer_bootstrap_attested,false);eq(result.author_probe_executed,false);eq(result.closure_certified,false);
eq(result.controls.length,3);eq(result.closing_controls,[]);eq(result.passes.length,1);eq(result.errors.length,1);
eq(result.native_events.length,2235);eq(result.path_events.length,321);eq(result.errors,shape.errors);
eq(result.actual_read_bytes,148918458);eq(result.actual_captured_bytes,1675778);
const frontier=json(S+'FRONTIER.json');
eq(objects.get(S+'FRONTIER.json'),Buffer.from(canonical(frontier)),'canonical exact frontier');
eq(Object.keys(frontier).sort(),['schema','status','author_probe_execution_allowed','targets','allowed_components','closure_gaps'].sort());
eq(frontier.schema,'p212-finite-preprobe-frontier-v1');eq(frontier.status,'SOURCE_ONLY_INITIAL_FRONTIER_NOT_CLOSURE');eq(frontier.author_probe_execution_allowed,false);
eq(frontier.targets.length,164);eq(frontier.allowed_components.length,204);eq(frontier.closure_gaps.length,8);eq(result.closure_gaps,frontier.closure_gaps);
const allowed=new Set(frontier.allowed_components);
function components(p) { let out=['/'],current='';for(const n of p.split('/').slice(1))if(n){current+='/'+n;out.push(current);}return out; }
function physical(p) { return typeof p==='string'&&p.startsWith('/')&&!p.startsWith('//')&&!p.includes('\0')&&Buffer.byteLength(p)<=4096&&(p==='/'||p.split('/').slice(1).every(x=>x&&x!=='.'&&x!=='..')); }
eq(frontier.allowed_components,[...allowed].sort());
for(const p of allowed) {ok(physical(p));ok(components(p).every(x=>allowed.has(x)),'finite ancestor closure as DATA');}
eq(frontier.targets.map(x=>x.path),[...new Set(frontier.targets.map(x=>x.path))].sort());
let membershipNames=0;
for(const t of frontier.targets) {
 eq(Object.keys(t).sort(),['path','mode','role','origin','max_bytes','capture_hex','max_members','expected_names'].sort());
 ok(allowed.has(t.path));ok(typeof t.role==='string'&&typeof t.origin==='string');
 ok(['file','optional_file','directory','optional_directory','membership','absent','metadata'].includes(t.mode));
 ok(Number.isInteger(t.max_bytes)&&t.max_bytes>=0&&t.max_bytes<=134217728);ok(typeof t.capture_hex==='boolean');
 ok(Number.isInteger(t.max_members)&&t.max_members>=0&&t.max_members<=320);
 if(t.mode==='membership') {eq(t.expected_names,[...new Set(t.expected_names)].sort());ok(t.expected_names.length<=t.max_members);membershipNames+=t.expected_names.length;for(const n of t.expected_names)ok(typeof n==='string'&&n&&!['.','..'].includes(n)&&!n.includes('/')&&!n.includes('\0')&&Buffer.byteLength(n)<=255);}
 else {eq(t.max_members,0);eq(t.expected_names,null);}
 if(!['file','optional_file'].includes(t.mode)){eq(t.max_bytes,0);eq(t.capture_hex,false);}
}
eq(membershipNames,292);
// Explicit Linux little-endian LP64 Statx offsets from the fully read source.
// Buffers below are archived DATA, not a syscall, ffi, probe, or source import.
function device(major,minor) {const a=BigInt(major),b=BigInt(minor);return (b&255n)|((a&4095n)<<8n)|((b&~255n)<<12n)|((a&~4095n)<<32n);}
const maskCounts={},errnoCounts={};let decoded=0,absences=0;
for(const e of result.native_events) {
 eq(e.requested_mask,4095);ok(typeof e.path==='string');ok(e.handle===null||(Number.isInteger(e.handle)&&e.handle>=0));
 eq(e.flags,e.handle!==null?6144:([2048,2304].includes(e.flags)?e.flags:-1));
 ok(/^[a-f0-9]{512}$/.test(e.raw_statx_hex),'whole 256 native bytes');const b=Buffer.from(e.raw_statx_hex,'hex');
 if(e.return===0){
  eq(Object.keys(e).sort(),['path','handle','flags','requested_mask','return','errno','mask','raw_statx_hex','fields','status'].sort());
  eq(e.errno,0);eq(e.mask,b.readUInt32LE(0));eq(e.mask&4095,4095);eq(e.status,'ACTUAL_MASKED_FIELDS');
  const ns=o=>{const n=b.readUInt32LE(o+8);ok(n<1000000000,'native timestamp range');return b.readBigInt64LE(o)*1000000000n+BigInt(n);};
  const values=[device(b.readUInt32LE(136),b.readUInt32LE(140)),b.readBigUInt64LE(32),b.readUInt16LE(28),b.readUInt32LE(16),b.readUInt32LE(20),b.readUInt32LE(24),device(b.readUInt32LE(128),b.readUInt32LE(132)),b.readBigUInt64LE(40),b.readUInt32LE(4),b.readBigUInt64LE(48),ns(64),ns(112),ns(96),ns(80)];
  eq(e.fields,Object.fromEntries(FIELDS.map((f,i)=>[f,String(values[i])])),'all fourteen native values');
  decoded++;maskCounts[e.mask]=(maskCounts[e.mask]||0)+1;
 }else{
  eq(Object.keys(e).sort(),['path','handle','flags','requested_mask','return','errno','mask','raw_statx_hex','status'].sort());
  eq(e.return,-1);ok([2,20].includes(e.errno));eq(e.mask,null);eq(e.status,'ABSENCE_ERRNO_ONLY_NO_DECODED_FIELDS');
  absences++;errnoCounts[e.errno]=(errnoCounts[e.errno]||0)+1;
 }
}
let eventAt=0,pathAt=0,readBytes=0,capturedBytes=0,bodyCount=0,capturedCount=0;
const eventSpans=[];
class DataHold extends Error {}
function need(v,m){ok(typeof m==='string');if(!v)throw new DataHold(m);checks++;}
function kind(k,type){return k!==null&&(Number(BigInt(k.mode))&0o170000)===type;}
function stable(a,b,ancestor=false){ok(a!==null&&b!==null,'nonnull stable keys');for(const f of ancestor?IDENTITY:FIELDS.filter(x=>x!=='atimeNs'))eq(a[f],b[f],'recorded stable field');}
function take(path,flags,handle=null){const e=result.native_events[eventAt++];ok(e,'native event exists');eq(e.path,path,'exact archived event order/path');eq(e.flags,flags,'exact archived flags');eq(e.handle,handle,'exact archived descriptor');return e.return===0?e.fields:null;}
function resolve(path,scope){
 let queue=path==='/'?[]:path.split('/').slice(1),current='/',chain=[],links=0,steps=0,lexical=null;
 const root=take('/',2304);need(kind(root,0o040000),'physical root directory');chain.push({path:'/',lstat:root,link:null});
 while(queue.length){need(++steps<=1024,'component-step ceiling');const name=queue.shift(),candidate=current.replace(/\/$/,'')+'/'+name;
  need(scope.has(candidate),'unapproved component; not read: '+candidate);const key=take(candidate,2304),row={path:candidate,lstat:key,link:null};chain.push(row);
  if(key===null)return {path,resolved:null,absent_at:candidate,chain};if(!queue.length&&lexical===null)lexical=key;
  if(kind(key,0o120000)){need(++links<=40&&BigInt(key.size)<=4096n,'link count/byte ceiling');const pe=result.path_events[pathAt++];
   eq(Object.keys(pe).sort(),['operation','path','text'].sort());eq(pe.operation,'readlink');eq(pe.path,candidate);const link=pe.text;row.link=link;
   need(Buffer.byteLength(link)<=4096,'link byte ceiling');stable(key,take(candidate,2304));
   need(link&&link.replace(/^\/+/, '').split('/').every(x=>!['.','..',''].includes(x)),'dot/empty link component requires an explicit mechanism delta');
   const target=link.startsWith('/')?link:current.replace(/\/$/,'')+'/'+link;need(physical(target),'noncanonical link target');
   need(components(target).every(p=>scope.has(p)),'unapproved link target; link text retained, referent not read: '+target);
   queue=target.split('/').slice(1).concat(queue);current='/';continue;
  }
  current=candidate;
  if(queue.length&&!kind(key,0o040000)){const full=current+'/'+queue.join('/');need(scope.has(full),'unapproved blocked leaf');const k=take(full,2304);need(k===null&&result.native_events[eventAt-1].errno===20,'actual ENOTDIR required after observed non-directory component');return {path,resolved:null,absent_at:full,chain};}
 }
 const leaf=chain.at(-1).lstat,followed=take(current,2048);stable(leaf,followed);return {path,resolved:current,absent_at:null,chain,lstat:lexical||leaf,stat:followed};
}
function compare(a,b){eq([a.path,a.resolved,a.absent_at],[b.path,b.resolved,b.absent_at]);eq(a.chain.length,b.chain.length);a.chain.forEach((x,i)=>{const y=b.chain[i];eq([x.path,x.link],[y.path,y.link]);if(x.lstat===null||y.lstat===null)eq(x.lstat,y.lstat);else stable(x.lstat,y.lstat,x.path!==a.resolved&&kind(x.lstat,0o040000));});}
function observe(target,row,scope){
 const before=resolve(target.path,scope);eq(row.before,before,'whole opening resolution from events');eq(row.target,target,'entire target role/origin/schema');
 const path=target.path,mode=target.mode;
 if(before.resolved===null){need(['absent','optional_file','optional_directory'].includes(mode),'required target absent: '+path);eq(row.content,null);eq(row.members,null);}
 else {
  need(mode!=='absent','required absence is present: '+path);
  if(path===STDIN){eq(mode,'file');eq(target.max_bytes,0);eq(target.capture_hex,true);eq(before.resolved,path);ok(before.chain.every(x=>x.link===null));ok(kind(before.stat,0o100000));eq(before.stat.size,'0');}
  if(['file','optional_file'].includes(mode)){
   ok(kind(before.stat,0o100000));eq(row.members,null);const c=row.content;
   eq(Object.keys(c).sort(),['bytes','sha256','before','after','raw_hex'].sort());
   const fd=result.native_events[eventAt].handle;ok(Number.isInteger(fd)&&fd>=0);const first=take(before.resolved,6144,fd);
   eq(c.before,first);ok(kind(first,0o100000));ok(BigInt(first.size)<=BigInt(target.max_bytes));stable(before.stat,first);
   const last=take(before.resolved,6144,fd);eq(c.after,last);stable(first,last);eq(c.bytes,Number(first.size));
   ok(Number.isSafeInteger(c.bytes)&&c.bytes>=0&&c.bytes<=target.max_bytes);ok(/^[a-f0-9]{64}$/.test(c.sha256));
   if(target.capture_hex){ok(typeof c.raw_hex==='string'&&/^(?:[a-f0-9]{2})*$/.test(c.raw_hex));const body=Buffer.from(c.raw_hex,'hex');eq(body.length,c.bytes);eq(sha(body),c.sha256,'archived complete captured body hash');ok(c.bytes<=1048576);capturedBytes+=c.bytes;capturedCount++;}
   else eq(c.raw_hex,null,'uncaptured bytes remain unavailable, no reread');
   if(path===STDIN){eq(c.bytes,0);eq(c.sha256,EMPTY);eq(c.raw_hex,'');}
   bodyCount++;readBytes+=c.bytes;
  }else{
   eq(row.content,null);
   if(['directory','optional_directory','membership'].includes(mode))ok(kind(before.stat,0o040000));else eq(mode,'metadata');
   if(mode==='membership'){const names=[];for(let i=0;i<target.expected_names.length;i++){const pe=result.path_events[pathAt++];eq(Object.keys(pe).sort(),['operation','directory','name','ordinal'].sort());eq(pe.operation,'membership_name');eq(pe.directory,path);eq(pe.ordinal,i+1);ok(Buffer.byteLength(pe.name)<=255);names.push(pe.name);}eq(names.sort(),target.expected_names);eq(row.members,target.expected_names);}
   else eq(row.members,null);
  }
 }
 const after=resolve(path,scope);eq(row.after,after,'whole closing resolution from events');compare(before,after);
}
for(const [i,role] of ['source_receipt','trust_receipt','frontier'].entries()){
 const c=result.controls[i],ref=auth[role];eq(Object.keys(c),['role','observation']);eq(c.role,role);eq(ref,trust.controls[role]);
 eq(ref.pin,{bytes:objects.get(ref.path).length,sha256:sha(objects.get(ref.path))});
 eq(Object.keys(c.observation).sort(),['target','before','content','members','after'].sort());
 const target={path:ref.path,mode:'file',max_bytes:ref.pin.bytes,capture_hex:true};
 const start=eventAt;observe(target,c.observation,new Set(components(ref.path)));eq(c.observation.before.resolved,ref.path);
 eq(Buffer.from(c.observation.content.raw_hex,'hex'),objects.get(ref.path),'whole actual control vs pinned documentary original');
 eventSpans.push({role,first_event:start,after_event:eventAt});
}
eq(result.passes[0].number,1);eq(Object.keys(result.passes[0]),['number','targets']);const rows=result.passes[0].targets;eq(rows.length,157);
const modes={},roles={};let inputEvidence=null;
for(let i=0;i<156;i++){
 const row=rows[i],target=frontier.targets[i],start=eventAt;
 eq(Object.keys(row).sort(),['target','before','content','members','after','status'].sort());eq(row.status,'OBSERVED');
 observe(target,row,allowed);eventSpans.push({target_index:i,first_event:start,after_event:eventAt,status:row.status});
 modes[target.mode]=(modes[target.mode]||0)+1;roles[target.role]=(roles[target.role]||0)+1;
 if(target.path===STDIN){
  for(const f of DOC_FIELDS)eq(row.content.before[f],inputPreparation.input.metadata[f],'archived native input vs preparation ten-field agreement');
  inputEvidence={target_index:i,pass:1,first_event:start,after_event:eventAt,physical_chain:true,chain_entries:row.before.chain.length,bytes:0,sha256:EMPTY,opening_key:row.content.before,closing_key:row.content.after,completed_single_pass:true,second_pass_observed:false,fd0_attested:false};
 }
}
ok(inputEvidence,'selected input actually completed before failure');
const failed=rows[156],start=eventAt;
eq(Object.keys(failed).sort(),['target','status','error_type','error_message','first_event'].sort());eq(failed.target,frontier.targets[156]);
eq(failed.target.path,'/usr/local/cuda-12/targets/x86_64-linux/lib');eq(failed.target.mode,'optional_directory');
eq(failed.first_event,start);eq(start,2230);eq(failed.status,'HOLD');eq(failed.error_type,'Hold');
let caught=null;try{resolve(failed.target.path,allowed);}catch(e){if(!(e instanceof DataHold))throw e;caught=e.message;}
eq(caught,failed.error_message);eq(caught,'unapproved link target; link text retained, referent not read: '+STOP);
eq(result.errors,[{pass:1,...failed}]);eq(eventAt,result.native_events.length,'all native events consumed exactly once');eq(pathAt,result.path_events.length,'all path events consumed exactly once');
eq(result.native_events.slice(start).map(e=>e.path),['/','/usr','/usr/local','/usr/local/cuda-12','/usr/local/cuda-12']);
eq(result.path_events.at(-1),{operation:'readlink',path:'/usr/local/cuda-12',text:STOP});
ok(!allowed.has(STOP),'unapproved component genuinely outside exact frontier');
ok(result.native_events.every(e=>e.path!==STOP&&!e.path.startsWith(STOP+'/')),'no referent native event anywhere');
eq(readBytes,result.actual_read_bytes,'all completed retained content byte totals');eq(capturedBytes,result.actual_captured_bytes,'all captured body totals');
ok(readBytes<=536870912&&capturedBytes<=8388608&&raw.length<=134217728);
eq(decoded+absences,2235);
// Closing document and raw rereads are audit endpoints only, never new host observation.
for(const p of [...keys.keys()])read(p);
eq(meta(fs.lstatSync(PRIVATE,{bigint:true})),meta(d0),'private directory unchanged at audit endpoints');
const out={schema:'p212-independent-failed-observation-original-audit-v1',verdict:'ACCEPT_FAILED_RAW_ORIGINALS_ONLY',checks,
 independent_role:'No contribution to P212 proof/source/binding/erratum/observation; archive artifact audit only, not mathematical review',
 observation_packet_scope:'Explicit selected files only; active root packet not represented as frozen',
 packets:packetResults,document_and_private_keys:[...keys.values()],private_directory_key:meta(d0),
 actual_invocation:{chunk_id:'ad435d',exit_code:78,tool_stdout_bytes:0,extra_invocations_by_auditor:0},
 raw_shape:{status:result.status,controls:3,closing_controls:0,passes:1,target_records:157,completed_targets:156,failed_targets:1,unattempted_targets:7,native_events:2235,path_events:321,read_bytes:readBytes,captured_bytes:capturedBytes},
 native_decode:{successful_full_fourteen_field_records:decoded,absence_records:absences,requested_mask:4095,mask_counts:maskCounts,errno_counts:errnoCounts,all_256_byte_records_checked:true,all_events_consumed:true},
 content_checks:{completed_bodies:bodyCount,captured_bodies:capturedCount,uncaptured_bodies:bodyCount-capturedCount,captured_bytes_hashed:capturedBytes,uncaptured_digest_values_not_live_verified:true},
 completed_mode_counts:modes,input_archived_single_pass_evidence:inputEvidence,
 failure:{target_index:156,target:failed.target,first_event:start,after_event:eventAt,native_paths:result.native_events.slice(start).map(e=>e.path),error_type:failed.error_type,error_message:failed.error_message,last_path_event:result.path_events.at(-1),referent_read:false},
 unattempted_target_values:frontier.targets.slice(157),event_spans:eventSpans,
 limitations:['No whole bootstrap/runtime/native-key PASS','No second pass or closing controls observed','No current target/input/ancestor reread','No inherited fd0 identity or descriptor handoff attestation','Ordinary trusted source/runtime/transport semantics remain assumptions','Uncaptured file bodies not independently reconstructed','Failure retains events but not a completed failed-target resolution object','No retry or policy repair authorized'],
 protected_raw_body_disclosed:false};
process.stdout.write(canonical(out));
