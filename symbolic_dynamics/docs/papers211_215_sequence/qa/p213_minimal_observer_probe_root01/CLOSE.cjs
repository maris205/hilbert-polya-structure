'use strict';
const fs=require('fs'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics/',O='docs/papers211_215_sequence/qa/p213_minimal_observer_probe_root01/';
const own=['GRANT.json','PREFLIGHT_NATIVE.json','MATERIALIZATION_STRICT_NATIVE.json','ATTEMPT_COMMITTED.json','OBSERVATION_NATIVE.json','INITIAL_RAW_RECEIVE_NATIVE.json','PRECISION_LIMIT.md','CHECK_RAW_INTEGERS.cjs','LOSSLESS_NATIVE.json','HANDOFF.md','RAW_INPUTS.sha256','CLOSE.cjs'];
const old=JSON.parse(JSON.parse(fs.readFileSync(ROOT+O+'PREFLIGHT_NATIVE.json','utf8')).result.output);
const rawOld=JSON.parse(JSON.parse(fs.readFileSync(ROOT+O+'INITIAL_RAW_RECEIVE_NATIVE.json','utf8')).result.output);
const allowed=new Set([...old.keys.map(k=>k.path),...rawOld.keys.map(k=>k.path),...own.map(n=>ROOT+O+n)]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs'],meta=s=>Object.fromEntries(fields.map(f=>[f,s[f].toString()])),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
let checks=0;const keys=new Map(),buffers=new Map();function ok(x,m){checks++;if(!x)throw Error(m);}
function read(p){ok(allowed.has(p),'only finite sources/documents/captured outputs');const a=fs.lstatSync(p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink(),'regular file');const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);let b;try{const f=fs.fstatSync(fd,{bigint:true});b=fs.readFileSync(fd);const g=fs.fstatSync(fd,{bigint:true}),z=fs.lstatSync(p,{bigint:true});for(const s of[f,g,z])ok(JSON.stringify(meta(a))===JSON.stringify(meta(s)),'full same-fd/path key');ok(BigInt(b.length)===a.size,'full bytes');}finally{fs.closeSync(fd)}const k={path:p,metadata:meta(a),bytes:b.length,sha256:sha(b)};if(keys.has(p))ok(JSON.stringify(keys.get(p))===JSON.stringify(k),'repeat unchanged');keys.set(p,k);buffers.set(p,b);return b;}
const js=n=>JSON.parse(read(ROOT+O+n).toString('utf8'));
for(const k of [...old.keys,...rawOld.keys]){read(k.path);ok(JSON.stringify(k)===JSON.stringify(keys.get(k.path)),'all source/raw earlier whole keys unchanged');}
for(const n of own)read(ROOT+O+n);
ok(JSON.stringify(fs.readdirSync(ROOT+O).filter(n=>!['CLOSING_NATIVE.json','SHA256SUMS'].includes(n)).sort())===JSON.stringify(own.slice().sort()),'complete own inventory');
const grant=js('GRANT.json'),attempt=js('ATTEMPT_COMMITTED.json'),native=js('OBSERVATION_NATIVE.json');
ok(JSON.stringify(native.request)===JSON.stringify(grant.exact_request)&&JSON.stringify(attempt.exact_request)===JSON.stringify(grant.exact_request),'exact once request');
ok(attempt.attempt_budget_consumed===true&&attempt.no_second_invocation===true,'grant consumed no retry');
ok(native.result.exit_code===0&&native.result.output==='P213_OBSERVER_NATIVE_EXIT=0\n'&&!('session_id' in native.result),'actual complete no-session zero exit');
ok(js('MATERIALIZATION_STRICT_NATIVE.json').result.exit_code===0,'prior strict actual success');
const d=JSON.parse(js('LOSSLESS_NATIVE.json').result.output);
ok(d.integerTokens===4591&&d.unsafeMagnitudeTokens===696&&d.objects===934&&d.allInputConsumed&&d.sourceKeyComparisons.length===10,'actual lossless source-only census');
ok(d.sourceKeyComparisons.every(x=>x.rawInteger===x.documentaryInteger&&x.stages===5),'all fifty exact source metadata comparisons');
ok(d.rawSha256===rawOld.keys[0].sha256&&d.rawBytes===322982,'lossless raw object exact pin');
const pin=read(ROOT+O+'RAW_INPUTS.sha256').toString('utf8');ok(pin===rawOld.keys.map(k=>k.sha256+'  '+k.path.slice(ROOT.length)+'\n').join(''),'complete raw inputs manifest');
for(const p of [...keys.keys()])read(p);
console.log(JSON.stringify({scope:'SINGLE_PROBE_ORIGINAL_EVIDENCE_CLOSING_NOT_INDEPENDENT_RUNTIME_ACCEPTANCE',checks,keys:[...keys.values()],keyCount:keys.size,preservedPreflightKeys:old.keys.length,preservedRawKeys:rawOld.keys.length,grantConsumed:true,actualNativeExit:0,noSession:true,observerRerun:false,runtimeAccepted:false,precisionProjectionWarningRetained:true}));
