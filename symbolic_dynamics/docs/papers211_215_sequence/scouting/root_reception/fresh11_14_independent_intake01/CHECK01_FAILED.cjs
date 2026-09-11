'use strict';
// Document-only intake. No commands, research imports, network or private paths.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const OWN = 'docs/papers211_215_sequence/scouting/root_reception/fresh11_14_independent_intake01';
const BASE = 'docs/papers211_215_sequence/scouting/finite_residual_fresh';
let checks = 0;
function ok(value, message) { checks++; if (!value) throw new Error(message); }
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const seen = new Map();
const outside = new Set(['/root/autodl-tmp/.codex/skills/research-lit/SKILL.md', '/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md']);
function fullKey(p) {
  const absolute = path.isAbsolute(p) ? p : path.join(ROOT, p);
  ok(absolute.startsWith(ROOT + '/') || outside.has(absolute), 'unscoped path: ' + p);
  const a = fs.lstatSync(absolute, {bigint:true});
  ok(a.isFile() && !a.isSymbolicLink(), 'not ordinary documentary file: ' + p);
  const bytes = fs.readFileSync(absolute);
  const b = fs.lstatSync(absolute, {bigint:true});
  // atime is deliberately not an identity/stability field: a read can change it.
  const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs'];
  for (const k of fields) ok(a[k] === b[k], 'read instability ' + p + ' ' + k);
  ok(BigInt(bytes.length) === b.size, 'byte length ' + p);
  return {path:p, type:'regular', ...Object.fromEntries(fields.map(k=>[k,b[k].toString()])), bytes:bytes.length, sha256:sha(bytes)};
}
function read(p) {
  const k = fullKey(p);
  if (seen.has(p)) ok(JSON.stringify(k) === JSON.stringify(seen.get(p)), 'changed repeated input: ' + p);
  else seen.set(p,k);
  return fs.readFileSync(path.isAbsolute(p)?p:path.join(ROOT,p));
}
function json(p) { return JSON.parse(read(p).toString('utf8')); }
function lines(p) { const s=read(p).toString('utf8'); ok(s.endsWith('\n'), 'missing newline: '+p); return s.slice(0,-1).split('\n'); }
function pins(p) {
  const rows=lines(p).map(line=>{const m=/^([0-9a-f]{64})  (.+)$/.exec(line);ok(!!m,'strict digest line: '+p);return {sha256:m[1],path:m[2]};});
  ok(new Set(rows.map(x=>x.path)).size===rows.length,'duplicate pin '+p); return rows;
}
function inventory(dir) {
  const out=[];
  for(const ent of fs.readdirSync(path.join(ROOT,dir),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))) {
    const p=dir+'/'+ent.name; ok(!ent.isSymbolicLink(),'symlink entry: '+p);
    if(ent.isDirectory()) out.push(...inventory(p)); else {ok(ent.isFile(),'nonfile entry: '+p);out.push(p);}
  }
  return out;
}
function seal(dir, expected, count) {
  const mf=dir+'/SHA256SUMS'; ok(sha(read(mf))===expected,'seal anchor: '+mf);
  const entries=pins(mf);ok(entries.length===count,'payload count: '+dir);
  const names=[];
  for(const entry of entries){const rel=entry.path.replace(/^\.\//,'');ok(rel!== 'SHA256SUMS'&&!path.isAbsolute(rel)&&!rel.split('/').some(x=>x==='..'||x==='.'||x===''),'scope: '+rel);const p=dir+'/'+rel;names.push(p);ok(sha(read(p))===entry.sha256,'payload hash: '+p);}
  const actual=inventory(dir).filter(p=>p!==mf).sort();
  ok(JSON.stringify(names.sort())===JSON.stringify(actual),'complete nonself inventory: '+dir);
  return {dir,payloads:count,files:actual.length+1,totalBytes:[mf,...actual].reduce((s,p)=>s+seen.get(p).bytes,0),sealSha256:expected};
}
const adapters = {
  11: {dir:'docs/papers211_215_sequence/qa/control_before_p212_stdin_p213_original_received01', kind:'entries'},
  12: {dir:'docs/papers211_215_sequence/qa/control_before_quota_interruption01',kind:'files'}
};
const mapRows=[];
for(const [n,a] of Object.entries(adapters)) {
  const map=json(a.dir+'/MAPPING.json');
  ok(Array.isArray(map[a.kind])&&map[a.kind].length===2,'exact mapping schema '+n);
  a.rows=map[a.kind];
  if(n==='11') { const receipt=json(a.dir+'/PRESERVATION_NATIVE.json');ok(receipt.return.exit_code===0 && typeof receipt.return.output==='string','old physical-copy receipt');a.nativeCopyChunk=receipt.return.chunk_id; }
  else {ok(map.status==='PHYSICAL_PRE_UPDATE_COPIES_RAW_CMP_EXIT_ZERO'&&map.native_chunk==='e471b5','historical mapping assertion');a.nativeCopyChunk=map.native_chunk;}
}
const specs = [
  [11,'65b3130a2bd1d88703f9ec39a18afe0b761da11e91907bee67085282db4c3926',8,19,40,4,4],
  [12,'0fffe156537235ede43e4f966b03362bc80c48a29c951a9714a72b8f868f123b',7,16,28,6,3],
  [13,'faf224e8c1da30c93b8edf29d7aad37dfa7024dab69741a823497e52ef121051',16,23,15,3,5],
  [14,'60da759766b818bcb0b27ec174c17e00d68554fdb3b3826508e869f0b11cc8c9',8,17,16,7,3]
];
const packageRows=[], pinRows=[], recordRows=[], exceptionRows=[];
function arrayOf(v) { const a=Array.isArray(v)?v:v.records??v.checks;ok(Array.isArray(a),'record array');return a; }
function inspectRecord(file,index,r,kind) {
  ok(r&&typeof r.request==='object'&&!Array.isArray(r.request),'request envelope '+file+' '+index);
  const ret=r.response??r.result; const id=file+'#'+index;
  let s;
  const row={id,kind,label:r.record_id??r.label??null,request:r.request,requestJsonSha256:sha(JSON.stringify(r.request)),returnType:typeof ret};
  if(kind==='web') {ok(typeof ret==='string','browser complete returned string '+id);s=ret;}
  else {
    ok(ret&&typeof ret==='object'&&typeof ret.output==='string'&&Number.isInteger(ret.exit_code),'native envelope '+id);
    ok(typeof ret.chunk_id==='string'&&typeof ret.wall_time_seconds==='number'&&Number.isInteger(ret.original_token_count),'native metadata '+id);
    ok(!('session_id' in ret),'unfinished native command '+id);
    s=ret.output; Object.assign(row,{chunkId:ret.chunk_id,exitCode:ret.exit_code,originalTokenCount:ret.original_token_count,returnKeys:Object.keys(ret).sort()});
  }
  row.returnJsonSha256=sha(JSON.stringify(ret));row.returnJsonBytes=Buffer.byteLength(JSON.stringify(ret));
  row.outputBytes=Buffer.byteLength(s);row.outputSha256=sha(s);
  // Only tool-envelope markers count as truncation; mentions in quoted prose do not.
  row.toolTruncated=/^Warning: truncated output \(original token count:/m.test(s);
  row.shellErrorLines=kind==='web'?[]:s.split('\n').filter(x=>/^(?:rg|sed|cat|sha256sum|wc):.*(?:No such file|Permission denied|FAILED|error)/.test(x));
  row.webFailureLines=kind==='web'?s.split('\n').filter(x=>/^Internal Error|^L\d+: (?:Failed to fetch|Unable to resolve)|Timeout fetching|content type is not|not.*application\/pdf/i.test(x)):[];
  if((row.exitCode??0)!==0||row.toolTruncated||row.shellErrorLines.length||row.webFailureLines.length) exceptionRows.push({...row,retainedOriginal:file,classification:'retain actual tool result; not converted into source/command success'});
  recordRows.push(row);return ret;
}
for(const [n,digest,count,np,nd,nw,nc] of specs) {
  const dir=BASE+n; packageRows.push(seal(dir,digest,count));
  const declared=pins(dir+'/INPUT_PINS.sha256');ok(declared.length===np,'declared pins '+n);
  for(const entry of declared) {
    let physical=entry.path;let adapted=false;
    if(entry.path==='SYMBOLIC_DYNAMICS_STATE.md'||entry.path==='docs/papers211_215_sequence/PIPELINE_STATE.md') {
      const a=adapters[n];ok(!!a,'mutable central requires exact adapter');
      const m=a.rows.find(x=>x.original===entry.path);ok(!!m&&m.sha256===entry.sha256,'old mapping assertion '+n+' '+entry.path);
      physical=a.kind==='entries'?m.physical_copy:a.dir+'/'+m.copy; adapted=true;
      const b=read(physical);ok(b.length===m.bytes,'snapshot bytes');
      mapRows.push({scout:n,logical:entry.path,physical,bytes:m.bytes,sha256:m.sha256,mapping:a.dir+'/MAPPING.json',historicalNativeCopyChunk:a.nativeCopyChunk,scope:'historical content identity only; no original-inode equivalence or current-central equality claim'});
    }
    const b=read(physical);ok(sha(b)===entry.sha256,'pin content '+n+' '+entry.path);
    pinRows.push({scout:n,logical:entry.path,physical,sha256:entry.sha256,bytes:b.length,historicalAdapter:adapted});
  }
  for(const [file,kind,num] of [['DOCUMENTARY_REQUEST_RETURNS.json','documentary',nd],['WEB_REQUEST_RETURNS.json','web',nw],['CHECKS_NATIVE.json','check',nc]]){
    const full=dir+'/'+file;const arr=arrayOf(json(full));ok(arr.length===num,'exact record count '+full);
    arr.forEach((r,i)=>inspectRecord(full,i,r,kind));
  }
  const pf=dir+'/PIN_OBSERVATION_NATIVE.json';const obj=json(pf);const r=obj.record??obj;const ret=inspectRecord(pf,0,r,'pin');
  ok(ret.exit_code===0,'original pin command success');
  const fromReturn=ret.output.trimEnd().split('\n');const expected=declared.map(x=>x.sha256+'  '+x.path);
  ok(JSON.stringify(fromReturn)===JSON.stringify(expected),'all original pin output bytes/lines bind declared pins '+n);
  const checksOriginal=arrayOf(json(dir+'/CHECKS_NATIVE.json'));
  const pc=checksOriginal.find(r=>r.request.cmd.includes('INPUT_PINS.sha256'));
  ok(!!pc,'old strict pin check exists');const cr=pc.response??pc.result;
  ok(cr.exit_code===0&&cr.output===declared.map(x=>x.path+': OK\n').join(''),'complete old strict pin check output '+n);
}
const child=BASE+'13/primary_blocker_check';
const childSeal=seal(child,'1333bb5ddda6bda2cda2f5d52359c8d039b7519ebad05e8f41b119c42e78a20a',7);
for(let i=1;i<=3;i++) {const request=json(child+'/BROWSER0'+i+'_REQUEST.json');const result=json(child+'/BROWSER0'+i+'_RETURN.json');inspectRecord(child+'/BROWSER0'+i+'_RETURN.json',0,{request,result},'web');}
// Re-read all bytes and stable file identity fields after the complete data check.
const before=[...seen.values()].sort((a,b)=>a.path.localeCompare(b.path));
for(const old of before){const now=fullKey(old.path);ok(JSON.stringify(old)===JSON.stringify(now),'closing whole key '+old.path);}
const report={scope:'four frozen scout documentary intake only; no scientific execution or source ownership decision',checks,packageRows,childSeal,totalDeclaredPins:pinRows.length,totalUniqueDocumentaryKeys:before.length,totalRecords:recordRows.length,totalNativeRecords:recordRows.filter(x=>x.kind!=='web').length,totalWebRecords:recordRows.filter(x=>x.kind==='web').length,historicalAdapters:mapRows,pins:pinRows,recordCensus:recordRows,exceptions:exceptionRows,fullKeys:before,fullKeyDefinition:'logical path; regular type; dev,ino,mode,nlink,uid,gid,rdev,size,blksize,blocks,mtimeNs,ctimeNs,birthtimeNs as exact decimal strings; complete content bytes and SHA256. atime excluded explicitly as read-sensitive. All listed fields rechecked after reads.'};
if(process.argv[2]==='--close') {
  const original=JSON.parse(fs.readFileSync(path.join(ROOT,OWN,'CHECK_NATIVE.json'),'utf8'));
  ok(original.result.exit_code===0,'original intake native success');
  const old=JSON.parse(original.result.output);
  ok(JSON.stringify(old.fullKeys)===JSON.stringify(report.fullKeys),'original-to-closing full keys');
  ok(JSON.stringify(old.packageRows)===JSON.stringify(report.packageRows),'original-to-closing package counts');
  ok(JSON.stringify(old.recordCensus)===JSON.stringify(report.recordCensus),'original-to-closing complete record digests and requests');
  console.log(JSON.stringify({status:'DOCUMENTARY_CLOSING_PASS',checks,fullKeys:before.length,packages:packageRows,records:recordRows.length,rawOriginalReportSha256:sha(original.result.output),scientificRuns:0},null,2));
} else console.log(JSON.stringify(report,null,2));
