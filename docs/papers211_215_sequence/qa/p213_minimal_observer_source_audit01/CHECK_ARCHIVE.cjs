// Documentary receiver only. Python/Bash and all archived commands remain opaque text.
'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const base = 'docs/papers211_215_sequence/qa/p213_minimal_observer_source01/';
const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const names = ['BINDING.disabled.json','BINDING_FORMAT.md','CAPTURE_REQUEST.disabled.json','CHECK_DOCUMENTS.cjs','CHECK_NATIVE.json','CHECK_SOURCE_NATIVE.json','CLOSING_NATIVE.json','CONTRACT.md','DRAFT_READS_NATIVE.json','FINAL_READS_NATIVE.json','HANDOFF.md','INPUTS.sha256','INPUT_KEYS_AFTER_NATIVE.json','INPUT_KEYS_NATIVE.json','ORIENTATION_NATIVE.json','PATCHES_NATIVE.json','PRIMARY_NATIVE.json','READ_SCOPE.md','REPORT_READS_NATIVE.json','SELECTION_REQUEST.md','SHA256SUMS','SOURCE_READS_NATIVE.json','capture.disabled.sh','observe.py'];
let checks = 0;
function ok(v,m) { checks++; if (!v) throw new Error(m); }
const eq = (a,b) => JSON.stringify(a) === JSON.stringify(b);
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const keys = new Map(), bodies = new Map(), native = [], rawPairs = [];
const allowed = new Set(names.map(n=>base+n));
function metadata(s) {
  return Object.fromEntries(fields.map(n=>{ok(typeof s[n] === 'bigint','integer '+n);return [n,String(s[n])];}));
}
function read(p) {
  ok(allowed.has(p),'read outside finite documentary selection '+p);
  const start = fs.lstatSync(p,{bigint:true});
  ok(start.isFile() && !start.isSymbolicLink(),'regular document '+p);
  const fd = fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NONBLOCK|fs.constants.O_NOFOLLOW);
  let b, first, last;
  try {
    const s=fs.fstatSync(fd,{bigint:true});
    ok(s.isFile() && s.size <= 1000000n,'bounded regular document');
    first=metadata(s);
    ok(eq(first,metadata(start)),'start path/fd');
    b=fs.readFileSync(fd);
    last=metadata(fs.fstatSync(fd,{bigint:true}));
  } finally {fs.closeSync(fd);}
  ok(eq(first,last) && eq(first,metadata(fs.lstatSync(p,{bigint:true}))),'same fd and path endpoints');
  ok(BigInt(b.length)===BigInt(first.size),'whole read byte count');
  const key={path:p,bytes:b.length,sha256:sha(b),metadata:first};
  if(keys.has(p)) ok(eq(keys.get(p),key),'repeat document key '+p);
  keys.set(p,key); bodies.set(p,b); return b;
}
function parseSeal(b,local) {
  const s=b.toString('utf8');
  ok(s.endsWith('\n') && !s.endsWith('\n\n'),'strict terminal LF');
  const seen=new Set();
  return s.slice(0,-1).split('\n').map(l=>{
    const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.\/-]+)$/.exec(l);
    ok(m && !m[2].startsWith('/') && !m[2].split('/').includes('..'),'pin syntax');
    if(local) ok(!m[2].includes('/') && m[2]!=='SHA256SUMS','local nonself basename');
    ok(!seen.has(m[2]),'unique pin');seen.add(m[2]);return {sha256:m[1],path:m[2]};
  });
}
ok(eq(fs.readdirSync(base).sort(),names.slice().sort()),'exact physical source packet');
const seal=read(base+'SHA256SUMS');
ok(sha(seal)==='5517fa99464c02c5d21170a133b0f5a6d540f18ca549dd6296503f2fc0d29d55','frozen parent seal');
const leaves=parseSeal(seal,true);ok(leaves.length===23,'23 nonself payloads');
ok(eq(leaves.map(x=>x.path).sort(),names.filter(n=>n!=='SHA256SUMS').sort()),'nonself full membership');
for(const x of leaves) ok(sha(read(base+x.path))===x.sha256,'payload '+x.path);
const sourceBytes=names.reduce((n,p)=>n+bodies.get(base+p).length,0);
ok(sourceBytes===421765,'24-file byte total');
const pins=parseSeal(bodies.get(base+'INPUTS.sha256'),false);
ok(pins.length===9,'nine archive input pins');
const selectedPrefix='docs/papers211_215_sequence/qa/';
for(const x of pins) {
  ok(x.path.startsWith(selectedPrefix+'p213_runtime_') ||
     /^papers\/213-receiver-limited-cyclic-transfer\/(RUNTIME_PLAN|SCIENTIFIC_DEPENDENCIES)\.md$/.test(x.path),'input-only scope');
  allowed.add(x.path);ok(sha(read(x.path))===x.sha256,'input '+x.path);
}
const before=[...keys.values()];
function j(n) {return JSON.parse(bodies.get(base+n).toString('utf8'));}
function resultCheck(r,where) {
  ok(r && r.request && r.result && typeof r.request.cmd==='string','native request '+where);
  const q=r.result;
  ok(Number.isInteger(q.exit_code) && typeof q.output==='string' && typeof q.chunk_id==='string' && !q.session_id,'complete documentary native '+where);
  native.push({where,cmd:r.request.cmd,chunk_id:q.chunk_id,exit_code:q.exit_code,output_bytes:Buffer.byteLength(q.output),output_sha256:sha(Buffer.from(q.output))});
}
function pair(r,p,where) {
  resultCheck(r,where);
  ok(r.result.exit_code===0 && allowed.has(p),'raw pair scope/exit');
  const b=Buffer.from(r.result.output,'utf8');ok(bodies.get(p).equals(b),'raw native bytes '+where);
  rawPairs.push({where,path:p,bytes:b.length,sha256:sha(b)});
}
const oldReads=j('SOURCE_READS_NATIVE.json').records;ok(oldReads.length===10,'source read records');
let failures=0;
for(const [i,r] of oldReads.entries()) {
  if(r.result.exit_code!==0) {
    resultCheck(r,'source/'+i);
    ok(r.result.exit_code===2 && r.path.endsWith('/SOURCE_INPUTS.sha256'),'preserved exact wrong suffix');
    failures++;
  } else {ok(pins.some(p=>p.path===r.path),'selected source input');pair(r,r.path,'source/'+i);}
}
ok(failures===1,'one author navigation failure');
const finals=j('FINAL_READS_NATIVE.json');
ok(finals.records.length===7,'seven final read records');
for(const [i,r] of finals.records.entries()) pair(r,r.path,'final/'+i);
for(const [i,r] of j('REPORT_READS_NATIVE.json').records.entries()) pair(r,r.path,'report/'+i);
const checkerSource=j('CHECK_SOURCE_NATIVE.json');
pair(checkerSource.read,base+'CHECK_DOCUMENTS.cjs','checker-source');
ok(typeof checkerSource.patch==='string' && checkerSource.patch.includes('*** Add File: '+base+'CHECK_DOCUMENTS.cjs'),'checker construction provenance');
resultCheck(finals.wc,'final/wc');
const wc=finals.wc.result.output.trimEnd().split('\n');
ok(wc.length===8,'seven wc rows and total');
let totalLines=0,totalBytes=0;
for(const l of wc) {
  const m=/^\s*(\d+)\s+(\d+)\s+(.+)$/.exec(l);ok(m,'wc row');
  if(m[3]==='total') {ok(+m[1]===totalLines && +m[2]===totalBytes,'wc totals');continue;}
  ok(allowed.has(m[3]),'wc finite source');const b=bodies.get(m[3]);
  const count=b.reduce((n,c)=>n+(c===10),0);ok(+m[1]===count && +m[2]===b.length,'actual wc row');
  totalLines+=count;totalBytes+=b.length;
}
ok(totalLines===898 && totalBytes===46256,'exact full source line/byte count');
const keyBefore=j('INPUT_KEYS_NATIVE.json').before;resultCheck(keyBefore,'author-input-keys-before');
ok(Buffer.from(keyBefore.result.output).equals(bodies.get(base+'INPUTS.sha256')),'raw author before pins');
const keyAfter=j('INPUT_KEYS_AFTER_NATIVE.json');resultCheck(keyAfter,'author-input-keys-after');
ok(keyAfter.result.exit_code===0 && keyAfter.result.output===pins.map(x=>x.path+': OK\n').join(''),'raw strict author after pins');
const check=j('CHECK_NATIVE.json');resultCheck(check,'author-check');
const checkData=JSON.parse(check.result.output);
ok(check.result.exit_code===0 && checkData.checks===2189 && checkData.status==='DOCUMENTARY_CHECK_ONLY','author check provenance/status');
ok(checkData.source_audit===false && checkData.runtime_observed===false && checkData.python_or_reviewed_shell_executed===false,'author no source/runtime claim');
ok(checkData.keys.length===19 && checkData.selected_inputs===9 && checkData.raw_input_read_bytes===45206 && checkData.raw_source_read_bytes===46256,'author check counts');
for(const k of checkData.keys) ok(eq(keys.get(k.path),k),'complete historical author key '+k.path);
const closing=j('CLOSING_NATIVE.json');resultCheck(closing,'author-closing');
const closingData=JSON.parse(closing.result.output);
ok(closingData.status==='AUTHOR_DOCUMENTARY_CLOSING_ONLY' && closingData.checks===2882 && closingData.inventory.length===22,'author closing status/count');
ok(closingData.preclosing_bytes===403306 && closingData.preclosing_payloads===22,'author closing totals');
for(const k of closingData.inventory) ok(eq(keys.get(k.path),k),'complete author closing key '+k.path);
for(const [i,r] of j('ORIENTATION_NATIVE.json').records.entries()) resultCheck(r,'orientation/'+i);
for(const [i,r] of j('DRAFT_READS_NATIVE.json').records.entries()) {resultCheck(r,'draft/'+i);ok(r.result.exit_code===0,'draft read exit');}
const patches=j('PATCHES_NATIVE.json').records;ok(patches.length===7,'seven authored patches');
for(const r of patches) {
  ok(typeof r.patch==='string' && r.patch.startsWith('*** Begin Patch\n') && r.patch.endsWith('*** End Patch'),'full stored patch framing');
  const targets=[...r.patch.matchAll(/^\*\*\* (?:Add|Update) File: (.+)$/gm)].map(m=>m[1]);
  ok(targets.length>0 && targets.every(p=>p.startsWith(base) && allowed.has(p)),'author patch scope only');
  ok(r.result && typeof r.result==='object','patch result retained');
}
const primary=j('PRIMARY_NATIVE.json');
ok(primary.records.length===4,'four author primary requests preserved');
for(const r of primary.records) ok(r.request && r.result!==undefined,'primary request-return data retained');
const observer=bodies.get(base+'observe.py').toString('utf8');
const capture=bodies.get(base+'capture.disabled.sh').toString('utf8');
ok(observer.split('\n').length-1===438 && capture.split('\n').length-1===40,'exact program line counts');
ok(observer.includes('BINDING = None\nif BINDING is None:\n    raise SystemExit("P213_OBSERVER_DISABLED_UNRESOLVED_BINDING")\n\nimport sys'),'observer disabled before first import');
ok(capture.startsWith('# P213 SOURCE ONLY.') && capture.indexOf('\nexit 78\n')<capture.indexOf('umask 077'),'capture disabled before allocation');
const binding=j('BINDING.disabled.json'),request=j('CAPTURE_REQUEST.disabled.json');
ok(binding.enabled===false && binding.operation_authorized===false && request.enabled===false && request.operation_authorized===false,'no operation authorization');
ok(binding.launch_record===null && binding.modules===null && Object.values(binding.bounds).every(x=>x===null),'unresolved expected facts/bounds preserved');
ok(request.request.cmd===null && request.request.workdir===null && request.request.login===false && request.request.tty===false,'disabled native request');
for(const k of before) read(k.path);
const summary={status:'INDEPENDENT_DOCUMENTARY_INTEGRITY_ONLY',checks,source_semantics_proved_by_this_checker:false,reviewed_programs_executed:false,runtime_observed:false,
source_payloads:23,source_files:24,source_bytes:sourceBytes,source_seal_sha256:sha(seal),input_pins:pins.length,keys:[...keys.values()],native,raw_pairs:rawPairs,
author_failed_filename_records:failures,author_draft_and_patches_retained:true,author_primary_records:4};
process.stdout.write(JSON.stringify(summary,null,2)+'\n');
