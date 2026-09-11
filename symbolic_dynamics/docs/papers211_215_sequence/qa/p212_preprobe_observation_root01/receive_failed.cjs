'use strict';
// Data reception of ONE failed observation; no current host-target reread.
const fs=require('fs'),c=require('crypto');
const B='docs/papers211_215_sequence/qa/p212_preprobe_observation_root01/';
const cap='/root/symbolic-dynamics-p212-preprobe-observation-20260909-01/';
const hash=x=>c.createHash('sha256').update(x).digest('hex');
let checks=0;const need=(v,m)=>{checks++;if(!v)throw Error(m);},eq=(a,b,m)=>need(JSON.stringify(a)===JSON.stringify(b),m);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const stamp=s=>Object.fromEntries(fields.map(k=>[k,String(s[k])]));
const intake=JSON.parse(JSON.parse(fs.readFileSync(B+'INITIAL_RAW_INTAKE_NATIVE.json')).result.output);
let j;for(const k of intake.raw_keys){need(k.path===cap+'stdout.raw'||k.path===cap+'stderr.raw','two exact private files');const s=fs.lstatSync(k.path,{bigint:true});eq(stamp(s),k.metadata,'same private original key before');need(s.isFile()&&!s.isSymbolicLink()&&(s.mode&511n)===384n&&s.uid===0n,'0600 owner0');
 const fd=fs.openSync(k.path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let x;try{eq(stamp(fs.fstatSync(fd,{bigint:true})),stamp(s),'fd before body');x=fs.readFileSync(fd);eq(stamp(fs.fstatSync(fd,{bigint:true})),stamp(s),'fdafter');}finally{fs.closeSync(fd);}need(x.length===k.bytes&&hash(x)===k.sha256,'whole raw unchanged');if(k.path.endsWith('stdout.raw')){need(x.every(b=>b<128),'rawASCII');j=JSON.parse(x);need(Buffer.from(JSON.stringify(j,null,2)+'\n').equals(x),'whole canonical rawdata');}else need(x.length===0,'whole empty stderr');}
const actual=JSON.parse(fs.readFileSync(B+'ACTUAL_OBSERVER_NATIVE.json')),request=JSON.parse(fs.readFileSync(B+'REQUEST.json')),g=JSON.parse(fs.readFileSync(B+'AUTHORIZATION.json'));
eq(actual.request,request,'exact requested actual native');
need(actual.result.chunk_id==='d55ac5'&&actual.result.exit_code===78&&actual.result.output==='P212_OBSERVER_EXIT=78\n'&&!actual.result.session_id,'one settled failed native');
eq(j.provenance,g.provenance,'explicit trust');
need(j.schema==='p212-independent-preprobe-observation-v1'&&j.status==='HOLD_FINITE_OBSERVATION_ERRORS','failed schema status');
for(const k of ['observer_bootstrap_attested','author_probe_executed','closure_certified'])need(j[k]===false,'no attestation/phase '+k);
need(j.controls.length===3&&j.closing_controls.length===0&&j.passes.length===1&&j.errors.length===1,'failurestops');
const obs=j.controls.map(r=>r.observation);let bodyBytes=0,captured=0;
for(const r of j.controls){need(['source_receipt','trust_receipt','frontier'].includes(r.role),'namedcontrol');const v=r.observation,pin=g[r.role].pin;need(v.target.path===g[r.role].path&&v.before.resolved===v.target.path&&v.after.resolved===v.target.path,'control physicalpath');const raw=Buffer.from(v.content.raw_hex,'hex');need(raw.length===v.content.bytes&&raw.length===pin.bytes&&hash(raw)===v.content.sha256&&hash(raw)===pin.sha256,'actual control fullraw');need(raw.equals(fs.readFileSync(g[r.role].path)),'current immutable controlwhole');bodyBytes+=raw.length;captured+=raw.length;}
const f=JSON.parse(Buffer.from(j.controls[2].observation.content.raw_hex,'hex'));
need(f.targets.length===164&&f.allowed_components.length===204,'exactfrontier');eq(j.closure_gaps,f.closure_gaps,'gapsretained');
const rows=j.passes[0].targets;need(j.passes[0].number===1&&rows.length===4,'firstpass4only');
for(let i=0;i<4;i++)eq(rows[i].target,f.targets[i],'orderedtargetprefix');
need(rows.slice(0,3).every(r=>r.status==='OBSERVED')&&rows[3].status==='HOLD','3success1fail');
need(rows[3].target.path==='/dev/null'&&rows[3].first_event===98&&rows[3].error_type==='Hold'&&rows[3].error_message==='HOLD missing basic/birthtime mask; raw retained','exact firstfailure');
eq(j.errors[0],{pass:1,...rows[3]},'exact failurecopy');
for(const r of rows.slice(0,3)){obs.push(r);if(r.content){need(r.target.path==='/bin/bash'&&r.content.bytes===1396520&&r.content.sha256==='59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4'&&r.content.raw_hex===null,'one wholekeyonly Bash capture');bodyBytes+=r.content.bytes;}}
need(bodyBytes===j.actual_read_bytes&&bodyBytes===1485016&&captured===j.actual_captured_bytes&&captured===88496,'complete counters');
// Decode returned buffers independently using accepted Linux offsets. Observed device major/minor values are in the bounded low-byte case.
const nfields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const permits=new Set(f.allowed_components);for(const r of Object.values(g).filter(x=>x&&x.path)){let p='';permits.add('/');for(const t of r.path.split('/').slice(1)){p+='/'+t;permits.add(p);}}
const eventFields=new Map();let supported=0;need(j.native_events.length===100,'100nativeevents');
for(const[e,v]of j.native_events.entries()){need(permits.has(v.path),'native approved exactpath');need(v.requested_mask===4095&&v.return===0&&v.errno===0,'actualcall');
 const raw=Buffer.from(v.raw_statx_hex,'hex');need(raw.length===256&&v.raw_statx_hex===raw.toString('hex'),'whole original nativebuffer');need(raw.readUInt32LE(0)===v.mask,'native actualmask');need(v.flags===(v.handle===null?(v.flags===2048?2048:2304):6144),'fd/path flags');
 if(e===99){need(v.path==='/dev'&&v.mask===6143&&(v.mask&4095)===2047&&!('fields'in v)&&!('status'in v),'last unsupported mask notdecoded');continue;}
 need((v.mask&4095)===4095&&v.status==='ACTUAL_MASKED_FIELDS','supported returnedfields');
 const u=o=>BigInt(raw.readUInt32LE(o)),big=o=>raw.readBigUInt64LE(o);
 const ns=o=>{need(u(o+8)<1000000000n,'native nanos');return raw.readBigInt64LE(o)*1000000000n+u(o+8);};
 const dev=(a,b)=>{const major=u(a),minor=u(b);need(major<4096n&&minor<256n,'actual bounded device encoding');return (major<<8n)|minor;};
 const vals=[dev(136,140),big(32),BigInt(raw.readUInt16LE(28)),u(16),u(20),u(24),dev(128,132),big(40),u(4),big(48),ns(64),ns(112),ns(96),ns(80)];
 const decoded=Object.fromEntries(nfields.map((k,i)=>[k,String(vals[i])]));eq(decoded,v.fields,'all14 rawdecoded fields');supported++;const k=v.path+'|'+JSON.stringify(v.fields);eventFields.set(k,true);
}
function fieldAt(path,k){need(eventFields.has(path+'|'+JSON.stringify(k)),'embedded fieldactualnative');}
function resolution(v){need(v.path&&v.resolved&&v.absent_at===null,'successresolution');for(const r of v.chain){fieldAt(r.path,r.lstat);if(r.link!==null)need(j.path_events.some(e=>e.operation==='readlink'&&e.path===r.path&&e.text===r.link),'linktextevent');}fieldAt(v.resolved,v.stat);}
function stable(a,b,ancestor=false){for(const k of ancestor?['dev','ino','mode','uid','gid','rdev','birthtimeNs']:nfields.filter(k=>k!=='atimeNs'))need(a[k]===b[k],'discrete field agreement');}
for(const v of obs){resolution(v.before);resolution(v.after);need(v.before.resolved===v.after.resolved,'same resolved');eq(v.before.chain.map(r=>[r.path,r.link]),v.after.chain.map(r=>[r.path,r.link]),'exactchain');
 for(let i=0;i<v.before.chain.length;i++){const x=v.before.chain[i],y=v.after.chain[i];stable(x.lstat,y.lstat,x.path!==v.before.resolved&&(Number(x.lstat.mode)&61440)===16384);}
 if(v.content){fieldAt(v.before.resolved,v.content.before);fieldAt(v.before.resolved,v.content.after);stable(v.content.before,v.content.after);stable(v.before.stat,v.content.before);need(Number(v.content.before.size)===v.content.bytes,'wholehandlebytes');}}
need(j.path_events.length===4&&j.path_events.every(v=>v.operation==='readlink'&&v.path==='/bin'&&v.text==='usr/bin'),'onlyactual4aliasreads');
need(!j.native_events.some(v=>v.path==='/dev/null'),'no deviceleaf reached');
for(const k of intake.raw_keys)eq(stamp(fs.lstatSync(k.path,{bigint:true})),k.metadata,'closing privatekey');
process.stdout.write(JSON.stringify({status:'PASS_COMPLETE_FAILED_OBSERVATION_RECEPTION_NOT_RUNTIME_ACCEPTANCE',checks,actual_observer_invocations:1,actual_exit:78,raw_original_bytes:[375140,0],actual_native_events:100,complete_supported_field_decodes:supported,unsupported_mask:{path:'/dev',returned:6143,required:4095,missing:2048},complete_control_captures:3,complete_target_rows:3,failed_target:'/dev/null',device_leaf_reached:false,second_pass:false,closing_controls:0,actual_read_bytes:bodyBytes,actual_captured_bytes:captured,private_original_keys:intake.raw_keys,body_values_exported:false,new_host_target_reads:0,new_observer_or_probe_invocations:0,build_git_ssh_science_actions:0},null,2)+'\n');

