"use strict";
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const R='docs/papers211_215_sequence/scouting/root_reception/fresh15_17/';
const names=['CHECK.cjs','CHECK_NATIVE.json','CHECK_RESULT.json','CLOSE.cjs','FINAL_PROOF_READS_NATIVE.json','READ_SCOPE.json','RECEPTION.md','ROOT_READS_NATIVE.json','ROOT_REPLAYS_NATIVE.json'];
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs','birthtimeNs','blocks','blksize'];
const sha=b=>crypto.createHash('sha256').update(b).digest('hex'),md=s=>Object.fromEntries(fields.map(n=>[n,String(s[n])]));
let checks=0;const eq=(a,b,m)=>{checks++;assert.deepStrictEqual(a,b,m);},ok=(v,m)=>{checks++;assert(v,m);};
const initial=JSON.parse(fs.readFileSync(R+'CHECK_RESULT.json','utf8'));
const allowed=new Set([...initial.keys.map(k=>k.path),...names.map(n=>R+n)]),keys=new Map(),raws=new Map();
function read(p){ok(allowed.has(p),'fixed document');const a=fs.lstatSync(p,{bigint:true});ok(a.isFile()&&a.nlink===1n);const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b;try{eq(md(fs.fstatSync(fd,{bigint:true})),md(a));b=fs.readFileSync(fd);eq(md(fs.fstatSync(fd,{bigint:true})),md(a));}finally{fs.closeSync(fd);}eq(md(fs.lstatSync(p,{bigint:true})),md(a));eq(BigInt(b.length),a.size);return{b,key:{path:p,bytes:b.length,sha256:sha(b),fields:md(a)}};}
for(const p of allowed){const x=read(p);keys.set(p,x.key);raws.set(p,x.b);}
for(const k of initial.keys)eq(keys.get(k.path),k,'every complete root input unchanged');
const native=JSON.parse(raws.get(R+'CHECK_NATIVE.json'));eq(native.result.exit_code,0);eq(Buffer.from(native.result.output),raws.get(R+'CHECK_RESULT.json'),'whole actual root stdout');
const late=JSON.parse(raws.get(R+'FINAL_PROOF_READS_NATIVE.json')).records;eq(late.length,3);
const pairs=[];const pair=(label,x,y)=>{eq(x,y,label);pairs.push({label,bytes:x.length,sha256:sha(x)});};
const expected=[];
const specs=[['docs/papers122_126_sequence/scouting/combinatorial/SCOUT.md',32,47],['docs/papers162_166_sequence/scouting/open_fresh_p166_round2/SCOUT.md',190,254],['docs/papers211_215_sequence/scouting/set_code_lane/PROOF_PACKAGE.md',105,195],['docs/papers152_156_sequence/scouting/combinatorial/SCOUT.md',312,345]];
for(const[p,a,z]of specs){const ls=raws.get(p).toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];expected.push(Buffer.from(ls.slice(a-1,z).join('')));}
eq(late[0].request.cmd,specs.map(([p,a,z])=>"sed -n '"+a+','+z+"p' "+p).join('\n'));eq(late[0].result.exit_code,0);pair('four actual old proof/literal intervals',Buffer.concat(expected),Buffer.from(late[0].result.output));
const web=JSON.parse(raws.get('docs/papers211_215_sequence/scouting/finite_residual_fresh17/WEB_REQUEST_RETURNS.json'));
for(let i=1;i<3;i++){const role=['erection_higgs_proof_windows','proof_window_completion'][i-1];eq(late[i].result.exit_code,0);ok(late[i].request.cmd.includes("r.role==='"+role+"'"));pair('whole archived primary root read '+role,Buffer.from(late[i].result.output),Buffer.from(web.records.find(r=>r.role===role).result));}
for(const p of allowed){const x=read(p);eq(x.key,keys.get(p));eq(x.b,raws.get(p));}
const manifest=names.map(n=>({name:n,...keys.get(R+n)}));
process.stdout.write(JSON.stringify({schema:'ROOT_FRESH15_17_CLOSING_V1',checks,document_keys:keys.size,previous_root_keys:initial.keys.length,raw_pairs:pairs.length,raw_paired_bytes:pairs.reduce((n,x)=>n+x.bytes,0),pairs,keys:[...keys.values()],preclosing_payloads:manifest,counts:initial.counts,operational_authority:false,external_status:'HOLD_EXTERNAL'},null,2)+'\n');
