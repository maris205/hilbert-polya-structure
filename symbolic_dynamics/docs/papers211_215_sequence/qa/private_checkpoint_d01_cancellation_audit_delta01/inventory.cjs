'use strict';
// Finite documentary reader only. Never executes submitted or archival commands.
const fs=require('fs'),crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics/';
const prep='docs/papers211_215_sequence/qa/private_checkpoint_d01_cancellation_delta01/';
const names=['CLOSING_NATIVE.json','DOCUMENTARY_CHECKS.json','EXACT_DELTA.patch',
'HANDOFF.md','INPUT_PINS.sha256','NATIVE_READS.json','PRIMARY_REQUESTS.json',
'TECHNICAL_RESPONSE.md','launch.py','SHA256SUMS'].sort();
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const meta=s=>Object.fromEntries(fields.map(k=>[k,s[k].toString()]));
const need=(x,s)=>{if(!x)throw Error(s);};
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
function read(p){
 need(p.startsWith('docs/')&&p.split('/').every(s=>s&&s!=='.'&&s!=='..'),'Document path');
 const before=fs.lstatSync(root+p,{bigint:true});need(before.isFile()&&!before.isSymbolicLink(),'Physical document');
 const fd=fs.openSync(root+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
 try{
  need(JSON.stringify(meta(before))===JSON.stringify(meta(fs.fstatSync(fd,{bigint:true}))),'Open metadata');
  const body=fs.readFileSync(fd);
  need(BigInt(body.length)===before.size&&[fs.fstatSync(fd,{bigint:true}),fs.lstatSync(root+p,{bigint:true})]
  .every(s=>JSON.stringify(meta(s))===JSON.stringify(meta(before))),'Read endpoints');
  return {key:{path:p,bytes:body.length,sha256:hash(body),metadata:meta(before)},body};
 }finally{fs.closeSync(fd);}
}
need(process.argv.length===2,'No mode or runtime argument');
need(JSON.stringify(fs.readdirSync(root+prep).sort())===JSON.stringify(names),'Exact input membership');
const rows=names.map(n=>read(prep+n)),manifest=rows.find(r=>r.key.path===prep+'SHA256SUMS');
need(manifest.key.sha256==='dbe83bea29b244561b420624064d2771f114ef8354e17d9a6fa179b057a80fc3','Root manifest key');
const lines=manifest.body.toString('utf8').trimEnd().split('\n');need(lines.length===9,'Nine payloads');
const seen=new Set();
for(const line of lines){
 const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);
 need(m&&m[2]!=='SHA256SUMS'&&!seen.has(m[2]),'Nonself manifest format');
 seen.add(m[2]);need(rows.find(r=>r.key.path===prep+m[2])?.key.sha256===m[1],'Whole payload key');
}
const source=rows.find(r=>r.key.path===prep+'launch.py');
need(source.key.bytes===18364&&source.key.sha256==='fa765db377179ad10770fa981f93b6fcc76e1adc49f79825d1631c90b5e29d96'
 &&source.body.toString('utf8').split('\n').length-1===347,'Exact new source');
const pins=rows.find(r=>r.key.path===prep+'INPUT_PINS.sha256').body.toString('utf8').trimEnd().split('\n');
need(pins.length===9,'Nine author input pins');
const historical=pins.map(line=>{
 const m=/^([0-9a-f]{64})  (docs\/[A-Za-z0-9_./-]+)$/.exec(line);need(m,'Document pin format');
 const r=read(m[2]);need(r.key.sha256===m[1],'Historical input changed');return r.key;
});
for(const r of rows.filter(r=>r.key.path.endsWith('.json')))JSON.parse(r.body.toString('utf8'));
process.stdout.write(JSON.stringify({scope:'documentary source-only',author_payloads:9,
author_files:10,author_bytes:rows.reduce((n,r)=>n+r.key.bytes,0),
author_inputs:rows.map(r=>r.key),historical_inputs:historical},null,2)+'\n');
