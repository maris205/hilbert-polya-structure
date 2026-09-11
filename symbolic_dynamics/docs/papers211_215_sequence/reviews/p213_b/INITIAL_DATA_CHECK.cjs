'use strict';
// DATA-only audit of the one accepted initial capture. Never imports or runs
// verify.py, reads a canonical, traverses captured host paths, or writes files.
const fs = require('node:fs'), crypto = require('node:crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics/';
const BASE = ROOT + 'docs/papers211_215_sequence/';
const RUN = BASE + 'qa/p213_b_initial_run01/';
const PREP = BASE + 'qa/p213_b_execution_preparation01/';
const INTAKE = BASE + 'qa/p213_b_source_root01/';
const OWN = BASE + 'reviews/p213_b/';
const SHA = b => crypto.createHash('sha256').update(b).digest('hex');
let checks = 0;
function ok(value, label) { checks++; if (!value) throw Error(label); }
function same(a,b,label) { ok(JSON.stringify(a) === JSON.stringify(b),label); }
const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const stat = s => Object.fromEntries(fields.map(k => [k,s[k].toString()]));
const evidence = [];
function read(path) {
  ok(path.startsWith(BASE), 'workspace documentary read only');
  const before = fs.lstatSync(path,{bigint:true});
  ok(before.isFile() && !before.isSymbolicLink(), 'regular documentary leaf');
  const data = fs.readFileSync(path);
  same(stat(before),stat(fs.lstatSync(path,{bigint:true})), 'document read stable');
  ok(BigInt(data.length) === before.size,'document complete');
  evidence.push({path,bytes:data.length,sha256:SHA(data)});
  return data;
}
function json(path) { return JSON.parse(read(path).toString('utf8')); }
function shape(o, names, label) { same(Object.keys(o).sort(),names.slice().sort(),label); }
function keyRecord(r,spec) {
  ok(r.path===spec.path && r.kind===spec.kind && r.complete===true,'key identity/complete');
  if (r.kind==='required-absence') {
    shape(r,['path','kind','complete','eof','close_succeeded','absence'],'absence fields');
    same(r.absence,{operation:'lstat',code:'ENOENT',path:r.path},'exact absence');
    ok(r.eof===false && r.close_succeeded===false,'absence not opened');
    return 0;
  }
  shape(r,['path','kind','complete','eof','close_succeeded','begin','fd_before','bytes','sha256','fd_after','end'],'present fields');
  for (const phase of ['begin','fd_before','fd_after','end']) {
    shape(r[phase],fields,'ten-field key');
    for (const f of fields) ok(typeof r[phase][f]==='string' && /^(0|[1-9][0-9]*)$/.test(r[phase][f]),'lossless integer key');
    same(r[phase],r.begin,'four phases unchanged');
  }
  ok(r.eof===true && r.close_succeeded===true,'present EOF/close');
  ok(Number.isSafeInteger(r.bytes) && r.bytes>=0 && BigInt(r.bytes)===BigInt(r.begin.size),'key bytes');
  ok((BigInt(r.begin.mode)&61440n)===32768n && BigInt(r.begin.nlink)>=1n,'regular recorded file');
  ok(/^[0-9a-f]{64}$/.test(r.sha256),'digest syntax');
  if (spec.bytes!==undefined) ok(r.bytes===spec.bytes,'pinned bytes');
  if (spec.sha256!==undefined) ok(r.sha256===spec.sha256,'pinned hash');
  return r.bytes;
}
function keyReport(r,specs,mode) {
  shape(r,['schema','mode','scope','records','total_read_bytes','status'],'key report schema');
  ok(r.schema==='P213_B_EXTERNAL_KEYS_V1' && r.mode===mode,'report version/mode');
  ok(r.scope==='fixed external before/after file observations; ordinary bootstrap and pathname traversal trusted; no own-Python process observer','ordinary trust scope');
  ok(r.status==='COMPLETE_EXTERNAL_KEYS_PENDING_RECEPTION','reported completion');
  ok(r.records.length===specs.length,'exact key inventory');
  let total=0;
  r.records.forEach((record,i) => { total+=keyRecord(record,specs[i]); });
  ok(total===r.total_read_bytes,'aggregate bytes');
}

const depsRaw = read(PREP+'DEPENDENCIES.proposed.json');
ok(SHA(depsRaw)==='1c0b5d506c285f2df7345668a4b673e92d8efb3b4cc9f403517413e59c785e6b','accepted dependency pin');
const deps=JSON.parse(depsRaw);
ok(deps.inputs.length===20,'twenty fixed inputs');
const beforeRaw=read(RUN+'keys.before.json'), afterRaw=read(RUN+'keys.after.json');
ok(beforeRaw.equals(afterRaw),'whole raw before/after equality');
const before=JSON.parse(beforeRaw), after=JSON.parse(afterRaw);
keyReport(before,deps.inputs,'inputs'); keyReport(after,deps.inputs,'inputs');
const preflight=json(INTAKE+'PREFLIGHT_NATIVE.json');
ok(preflight.exit_code===0 && preflight.chunk_id==='881201' && !preflight.session_id,'actual preflight');
ok(Buffer.from(preflight.output,'utf8').equals(beforeRaw),'full preflight/before raw equality');
const launch=json(INTAKE+'INITIAL_ACTUAL_NATIVE.json');
ok(launch.result.exit_code===0 && launch.result.chunk_id==='861b78' && !launch.result.session_id,'actual initial exit');
ok(launch.result.output==='P213_B_CAPTURE_EXIT=0\n','actual controller return');
const request=json(PREP+'REQUEST.initial.ready.json');
same(launch.request,request.proposed_native_request.arguments,'exact accepted launch request');
ok(SHA(Buffer.from(launch.request.cmd))==='1fa098bb269f22c4d08b7554fe4957e470617c682cb6d74b4ecce88402679ea3','exact launch command');
const grant=read(INTAKE+'INITIAL_GRANT.md').toString('utf8');
ok(grant.includes('CONSUMED BEFORE SUBMISSION'),'grant consumed');
const raw = read(RUN+'stdout.bin');
const stderr = read(RUN+'stderr.bin'), status = read(RUN+'python.exit');
ok(stderr.length===0 && status.toString()==='0\n','science status and stderr');
ok(read(RUN+'controller.exit').toString()==='0\n','controller status');
for (const name of ['controller.stdout','controller.stderr','input-key-cmp.stdout','input-key-cmp.stderr',
                    'keys.before.stderr','keys.after.stderr','raw.keys.stderr']) {
  ok(read(RUN+name).length===0,'empty control '+name);
}
const rawKeys=json(RUN+'raw.keys.json');
const rawBuffers=[raw,stderr,status];
keyReport(rawKeys,['stdout.bin','stderr.bin','python.exit'].map((name,i)=>({path:RUN+name,kind:'regular-file',bytes:rawBuffers[i].length,sha256:SHA(rawBuffers[i])})),'outputs');
for (const r of rawKeys.records) ok(r.begin.nlink==='1','single-link recorded raw output');
const sourceSeal=read(OWN+'SHA256SUMS');
ok(SHA(sourceSeal)==='1e92a39a1bf9ca26e68740aab2e70b470b75f7a538448a6ee2e2f4b120efd1ca','historical source seal unchanged');
for (const line of sourceSeal.toString().trimEnd().split('\n')) {
  const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.]+)$/.exec(line);
  ok(!!m,'source manifest row'); ok(SHA(read(OWN+m[2]))===m[1],'source payload unchanged');
}

// Mathematical record reception, independently written from manuscript rule.
// Recursive mass splits and direct scalar flux/orbit evaluation differ from
// the executed multiset/token/layer implementation. No scientific source load.
function carrier(n,mass) {
  if(n===1) return [[mass]];
  const result=[];
  for(let x=0;x<=mass;x++) for(const tail of carrier(n-1,mass-x)) result.push([x,...tail]);
  return result;
}
const enc=a=>a.join(',');
const list=rows=>rows.length?rows.map(enc).join(';'):'-';
function flux(a) { const n=a.length; return a.map((x,i)=>x-Math.min(x,a[(i+1)%n])+Math.min(a[(i+n-1)%n],x)); }
function comparison(a) {return a.map((x,i)=>Number(x<=a[(i+1)%a.length]));}
function terminal(a) {
  const n=a.length,m=Math.min(...a),out=Array(n).fill(m);
  for(let e=0;e<n;e++) if(a[e]>m && a[(e+1)%n]===m) {
    let i=e;
    do {out[e]+=a[i]-m;i=(i+n-1)%n;} while(a[i]>m);
  }
  return out;
}
const text=raw.toString('ascii');
ok(Buffer.from(text,'ascii').equals(raw),'ASCII exactness');
ok(!text.includes('\r') && text.endsWith('\n'),'LF convention');
const lines=text.slice(0,-1).split('\n'); let cursor=0;
function expect(line) {ok(lines[cursor++]===line,'complete exact record line '+cursor);}
expect('P213_B_OCCUPATION_RELATION_LAYERS_V1'); expect('PARAM n=1..6 N=0..4');
let stateCount=0,chamberCount=0,carrierCount=0,emptyChambers=0,intervalCount=0,maxDimensions=0;
for(let n=1;n<=6;n++) for(let mass=0;mass<=4;mass++) {
  const states=carrier(n,mass), keys=states.map(enc), next=new Map(states.map(a=>[enc(a),flux(a)]));
  const pre=new Map(states.map(a=>[enc(a),states.filter(b=>enc(flux(b))===enc(a))]));
  const times=new Map(),ends=new Map(),layers=[];
  for(const a of states) {
    let current=a,t=0; const visited=new Set();
    while(enc(flux(current))!==enc(current)) {
      ok(!visited.has(enc(current)),'no nonfixed recurrence'); visited.add(enc(current));
      current=flux(current); t++;
    }
    times.set(enc(a),t); ends.set(enc(a),current); layers[t]=(layers[t]||0)+1;
    same(current,terminal(a),'terminal endpoint theorem');
    const b=next.get(enc(a)),m=Math.min(...a);
    ok(Math.min(...b)===m && a.every((x,i)=>x!==m || b[i]===m),'exact minima and barriers');
    ok(a.every((x,i)=>(x-m)*(a[(i+1)%n]-m)===0)===(t===0),'fixed/recurrent classification');
  }
  const height=Math.max(...times.values()),maxFibre=Math.max(...[...pre.values()].map(v=>v.length));
  ok(height===(n<=2||mass===0?0:n===3?Math.ceil(Math.log2(mass)):mass-1),'sharp height formula');
  for(const y of states) {
    const key=enc(y),sources=pre.get(key);
    expect(['STATE',n,mass,key,'NEXT',enc(next.get(key)),'TIME',times.get(key),'END',enc(ends.get(key)),'PRE',list(sources)].join(' ')); stateCount++;
    if(times.get(key)===0) {
      const m=Math.min(...y),spikes=y.map((x,i)=>x>m?i:-1).filter(i=>i>=0);
      let product=1;
      for(let j=0;j<spikes.length;j++) {
        const gap=((spikes[j]-spikes[(j+spikes.length-1)%spikes.length]+n-1)%n);
        if(gap>=2) product*=Math.floor((y[spikes[j]]-m)/2)+1;
      }
      ok(sources.length===product,'full fixed target product');
    }
    if(n>=3) for(let code=0;code<2**n;code++) {
      const s=Array.from({length:n},(_,i)=>(code>>i)&1);
      const members=sources.filter(a=>enc(comparison(a))===enc(s));
      const bounds=[];
      if(members.length) {
        for(let p=0;p<n;p++) if(s[(p+n-2)%n]===1 && s[(p+n-1)%n]===1 && s[p]===0) {
          const i=(p+n-1)%n,right=(p+1)%n,lo=y[i],sum=y[p]+members[0][right];
          const hi=Math.min(Math.floor(sum/2),y[p]-1);
          ok(members.every(a=>a[right]===members[0][right] && a[i]+a[p]===sum),'forced right and peak sum');
          const values=[...new Set(members.map(a=>a[i]))].sort((a,b)=>a-b);
          same(values,Array.from({length:hi-lo+1},(_,j)=>lo+j),'full interval projection');
          bounds.push([i,lo,hi]);
        }
        bounds.sort((a,b)=>a[0]-b[0]);
        let product=1; for(const [i,lo,hi] of bounds) {ok(lo<=hi,'interval nonempty');product*=hi-lo+1;}
        const parameterKeys=members.map(a=>enc(bounds.map(b=>a[b[0]])));
        ok(new Set(parameterKeys).size===members.length && product===members.length,'full rectangle bijection');
        const varying=new Set(bounds.flatMap(b=>[b[0],(b[0]+1)%n]));
        for(let i=0;i<n;i++) if(!varying.has(i)) ok(members.every(a=>a[i]===members[0][i]),'all forced coordinates');
      } else emptyChambers++;
      ok(bounds.length<=Math.floor(n/3),'three-edge packing');
      intervalCount+=bounds.length;maxDimensions=Math.max(maxDimensions,bounds.length);
      expect(['CHAMBER',n,mass,key,'WORD',enc(s),'PRE',list(members),'INTERVALS',list(bounds)].join(' '));chamberCount++;
    }
  }
  if(n>=3) {
    const k=Math.floor(n/3);
    ok(maxFibre<=(2**n-1)*(mass+1)**k,'finite upper bound');
    if(mass>=2*k) ok(maxFibre*(2*k)**k>=mass**k,'finite lower bound');
  } else ok(maxFibre===1,'short-cycle inverse');
  expect(['CARRIER',n,mass,'STATES',states.length,'HEIGHT',height,'LAYERS',enc(layers),'MAXFIBRE',maxFibre].join(' '));
  carrierCount++;
  console.log('CARRIER_DATA_ACCEPTED',n,mass,states.length,height,maxFibre);
}
expect('PASS CARRIERS 30 STATES 461 CHAMBERS 18872');
ok(cursor===lines.length && lines.length===19366,'every line consumed exactly');
same([stateCount,chamberCount,carrierCount],[461,18872,30],'exact record census');
ok(maxDimensions===2,'two-dimensional chamber observed');
console.log(JSON.stringify({status:'B_INITIAL_DATA_ACCEPTED_NOT_CANONICAL_NOT_STRICT',checks,stdout_bytes:raw.length,stdout_sha256:SHA(raw),lines:lines.length,states:stateCount,chambers:chamberCount,empty_chambers:emptyChambers,intervals:intervalCount,max_dimensions:maxDimensions,carriers:carrierCount,input_records:before.records.length,raw_output_records:rawKeys.records.length,evidence}));
