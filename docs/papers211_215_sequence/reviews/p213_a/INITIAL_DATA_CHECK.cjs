'use strict';
// Read-only reception of existing records, never executes/imports verify.py.
const fs=require('node:fs'), crypto=require('node:crypto');
const base='/root/autodl-tmp/symbolic_dynamics/';
const run=base+'docs/papers211_215_sequence/qa/p213_a_initial_run01/';
const prep=base+'docs/papers211_215_sequence/qa/p213_a_execution_preparation01/';
const review=base+'docs/papers211_215_sequence/reviews/p213_a/';
let checks=0;
function ok(x,m){checks++;if(!x)throw Error(m);}
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const raw=fs.readFileSync(run+'stdout.bin');
ok(raw.length===40888,'full output length');
ok(hash(raw)==='8846c5ba91c095a079f356a193fbd8721c145160190294f63300a07169771aac','raw stdout pin');
ok(raw.every(c=>c===10||(c>=32&&c<=126))&&raw.at(-1)===10,'ASCII LF');
for(const p of ['stderr.bin','controller.stdout','controller.stderr','keys.before.stderr','keys.after.stderr','raw.keys.stderr','input-key-cmp.stdout','input-key-cmp.stderr'])ok(fs.readFileSync(run+p).length===0,'empty '+p);
for(const p of ['python.exit','controller.exit'])ok(fs.readFileSync(run+p).equals(Buffer.from('0\n')),'exit '+p);
const before=fs.readFileSync(run+'keys.before.json');
ok(before.equals(fs.readFileSync(run+'keys.after.json')),'raw complete before/after equality');
const root=base+'docs/papers211_215_sequence/qa/p213_a_source_root01/';
const preflight=JSON.parse(fs.readFileSync(root+'PREFLIGHT_NATIVE.json'));
ok(preflight.exit_code===0&&Buffer.from(preflight.output).equals(before),'full preflight raw equals launch inputs');
const launch=JSON.parse(fs.readFileSync(root+'INITIAL_NATIVE.json'));
const finish=JSON.parse(fs.readFileSync(root+'INITIAL_CONTINUATION01.json'));
ok(launch.result.session_id===13328&&launch.result.chunk_id==='0fd081'&&launch.result.output==='','one actual session');
ok(finish.exit_code===0&&finish.chunk_id==='717c23'&&finish.output==='P213_A_CAPTURE_EXIT=0\n','actual sole completion');
ok(hash(Buffer.from(launch.request.cmd))==='f154bbca53b6a2f9bbad4f512a5d367d223a935560a19308d5cae3ff8e7e9135','executed command pin');
ok(hash(fs.readFileSync(prep+'EXTERNAL_KEYS.cjs'))==='ea89a37e57f3fed6909fd568c972d8b97537ecb07ae86febc130470f971abdac','collector source pin');
ok(hash(fs.readFileSync(prep+'DEPENDENCIES.proposed.json'))==='23cf1daad6b0873cc703ecf7e726e588ec08affb9de35910ecb59db42af11979','dependency document pin');
const inputs=JSON.parse(before), outputs=JSON.parse(fs.readFileSync(run+'raw.keys.json'));
const deps=JSON.parse(fs.readFileSync(prep+'DEPENDENCIES.proposed.json'));
ok(inputs.records.length===20&&inputs.total_read_bytes===9779303,'input count bytes');
for(const report of [inputs,outputs]){
 ok(report.schema==='P213_A_EXTERNAL_KEYS_V1'&&report.status==='COMPLETE_EXTERNAL_KEYS_PENDING_RECEPTION','key status');
 let sum=0;
 for(const r of report.records){
  ok(r.complete===true&&!r.failure,'complete record');
  if(r.kind==='required-absence'){
   ok(r.absence.operation==='lstat'&&r.absence.code==='ENOENT'&&r.absence.path===r.path,'recorded absence');continue;
  }
  ok(r.eof===true&&r.close_succeeded===true,'EOF close');
  ok(eq(r.begin,r.fd_before)&&eq(r.begin,r.fd_after)&&eq(r.begin,r.end),'all four full keys');
  ok(BigInt(r.bytes)===BigInt(r.begin.size),'byte count size');
  sum+=r.bytes;
 }
 ok(sum===report.total_read_bytes,'key total');
}
for(let i=0;i<20;i++){
 const r=inputs.records[i],d=deps.inputs[i];ok(r.path===d.path&&r.kind===d.kind,'ordered dependency');
 if(r.kind==='regular-file')ok(r.bytes===d.bytes&&r.sha256===d.sha256,'dependency content');
}
const source=inputs.records[19], st=fs.lstatSync(review+'verify.py',{bigint:true});
ok(hash(fs.readFileSync(review+'verify.py'))===source.sha256,'current source hash');
for(const k of ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'])ok(st[k].toString()===source.begin[k],'current source full key '+k);
ok(outputs.records.length===3,'raw key count');
for(const [i,p] of ['stdout.bin','stderr.bin','python.exit'].entries()){
 const r=outputs.records[i],b=fs.readFileSync(run+p);ok(r.path===run+p&&r.bytes===b.length&&r.sha256===hash(b),'raw recorded content');
 const s=fs.lstatSync(run+p,{bigint:true});
 for(const k of ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'])ok(s[k].toString()===r.begin[k],'current raw full key '+p+' '+k);
}
const lines=raw.toString('ascii').slice(0,-1).split('\n');
ok(lines.shift()==='P213_A_CURRENT_FOREST_V1'&&lines.shift()==='PARAM n=1..6 N=0..4','headers');
ok(lines.pop()==='PASS'&&lines.pop()==='TOTAL carriers=30 states=461','trailer');
let cursor=0,total=0,edges=0,fixedTotal=0,depthTotal=0,carrierResults=[];
const vec=s=>s.split(',').map(Number);
const sum=a=>a.reduce((s,v)=>s+v,0);
const key=a=>a.join(',');
const cmp=(a,b)=>{for(let i=0;i<a.length;i++){if(a[i]!==b[i])return a[i]-b[i];}return 0;};
const author=fs.readFileSync(base+'papers/213-receiver-limited-cyclic-transfer/frozen_round0/canonical_stdout.txt','ascii').trimEnd().split('\n').filter(l=>l.startsWith('TARGET '));
const authorMap=new Map(author.map(l=>{const t=Object.fromEntries(l.split(' ').slice(1).map(v=>v.split('=')));return [t.n+'/'+t.N+'/'+t.y,t];}));
for(let n=1;n<=6;n++)for(let N=0;N<=4;N++){
 const rows=[];
 while(cursor<lines.length&&lines[cursor].startsWith('STATE ')){
  const m=/^STATE n=(\d+) N=(\d+) a=([\d,]+) next=([\d,]+) tau=(\d+) terminal=([\d,]+) sources=(-|[\d,;]+)$/.exec(lines[cursor++]);
  ok(m&&+m[1]===n&&+m[2]===N,'state grammar and grouping');
  const a=vec(m[3]),b=vec(m[4]),terminal=vec(m[6]),tau=+m[5],sources=m[7]==='-'?[]:m[7].split(';').map(vec);
  for(const v of [a,b,terminal,...sources])ok(v.length===n&&v.every(x=>Number.isSafeInteger(x)&&x>=0)&&sum(v)===N,'vector member');
  if(rows.length)ok(cmp(rows.at(-1).a,a)<0,'state unique order');
  for(let j=1;j<sources.length;j++)ok(cmp(sources[j-1],sources[j])<0,'source unique order');
  const old=authorMap.get(n+'/'+N+'/'+key(a));
  ok(old&&old.next===key(b)&&old.tau===String(tau)&&old.terminal===key(terminal)&&old.sources===m[7]&&+old.indegree===sources.length,'all fields vs accepted author TARGET');
  rows.push({a,b,terminal,tau,sources});
 }
 let count=1;for(let j=1;j<n;j++)count=count*(N+j)/j;
 ok(rows.length===count,'full carrier cardinality');
 const table=new Map(rows.map(r=>[key(r.a),r]));
 let height=0,maximum=0,fixed=0;
 for(const r of rows){
  const {a,b,terminal,tau,sources}=r;
  const successor=table.get(key(b));ok(!!successor,'successor member');
  for(let i=0;i<n;i++)ok(b[i]===a[i]-Math.min(a[i],a[(i+1)%n])+Math.min(a[(i+n-1)%n],a[i]),'observed arrow literal');
  ok(Math.min(...a)===Math.min(...b),'observed minimum');
  const expected=rows.filter(t=>eq(t.b,a)).map(t=>t.a);
  ok(eq(sources,expected),'complete reverse arrow set');
  if(eq(a,b)){ok(tau===0&&eq(terminal,a),'fixed state labels');fixed++;}
  else ok(tau===successor.tau+1&&eq(terminal,successor.terminal),'strict forest depth labels');
  height=Math.max(height,tau);maximum=Math.max(maximum,sources.length);edges+=sources.length;depthTotal+=tau;
 }
 const m=/^CARRIER n=(\d+) N=(\d+) states=(\d+) height=(\d+) maximum=(\d+) recurrent=(\d+)$/.exec(lines[cursor++]);
 ok(m&&eq(m.slice(1).map(Number),[n,N,count,height,maximum,fixed]),'carrier summary');
 let expectedHeight=0;if(n>=3&&N>0){if(n===3){while(2**expectedHeight<N)expectedHeight++;}else expectedHeight=N-1;}
 ok(height===expectedHeight,'height claim');
 carrierResults.push({n,N,states:count,height,maximum,recurrent:fixed});total+=count;fixedTotal+=fixed;
}
ok(cursor===lines.length&&total===461&&edges===461&&authorMap.size===461,'complete all records');
const inventory=fs.readdirSync(run).sort().map(p=>{const b=fs.readFileSync(run+p);return {path:p,bytes:b.length,sha256:hash(b)};});
ok(inventory.length===14,'complete raw inventory');
console.log(JSON.stringify({status:'ACCEPT_INITIAL_DATA_ORDINARY_TRUST_ONLY',checks,source_sha256:source.sha256,stdout_bytes:raw.length,stdout_sha256:hash(raw),lines:495,states:total,carriers:30,edges,fixed_states:fixedTotal,depth_sum:depthTotal,carrierResults,inventory},null,2));
