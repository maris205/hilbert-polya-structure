'use strict';
// Documentary data only: never execute/import the reviewed paper or scout sources.
const fs = require('node:fs'), crypto = require('node:crypto');
const path = require('node:path'), assert = require('node:assert/strict');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const SC = 'docs/papers211_215_sequence/scouting/';
const OUT = SC + 'root_reception/fresh09_10/';
const FIELDS = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const seen = new Map(), cache = new Map();
let checks = 0;
const need = (c,m) => { checks++; assert(c,m); };
const same = (a,b,m) => { checks++; assert.deepEqual(a,b,m); };
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const allowedSkills = new Set(['/root/autodl-tmp/.codex/skills/research-lit/SKILL.md','/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md']);
function safe(p) {
  need(typeof p === 'string' && (allowedSkills.has(p) || (!path.isAbsolute(p) && path.normalize(p) === p && !p.startsWith('../'))), 'documentary scope '+p);
}
function stat(s) { return Object.fromEntries(FIELDS.map(k=>[k,String(s[k]) ])); }
function read(p) {
  safe(p); const a=fs.lstatSync(p,{bigint:true});
  need(a.isFile()&&!a.isSymbolicLink(),'regular documentary file '+p);
  const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  let b;
  try {
    same(stat(fs.fstatSync(fd,{bigint:true})),stat(a),'initial fd '+p);
    b=fs.readFileSync(fd);
    same(stat(fs.fstatSync(fd,{bigint:true})),stat(a),'final fd '+p);
  } finally { fs.closeSync(fd); }
  same(stat(fs.lstatSync(p,{bigint:true})),stat(a),'final path '+p);
  same(BigInt(b.length),a.size,'whole bytes '+p);
  const k={path:p,bytes:b.length,sha256:sha(b),stat:stat(a)};
  if(seen.has(p)) same(k,seen.get(p),'repeated whole key '+p);
  else seen.set(p,k);
  cache.set(p,b); return b;
}
function rows(p) {
  const text=read(p).toString('utf8');
  need(text.endsWith('\n')&&!text.endsWith('\n\n'),'strict single closing LF '+p);
  const result=text.slice(0,-1).split('\n').map(line=>{
    const m=/^([a-f0-9]{64})  (.+)$/.exec(line); need(m!==null,'manifest row '+p);
    return {sha256:m[1],path:m[2]};
  });
  same(new Set(result.map(r=>r.path)).size,result.length,'unique rows '+p);
  return result;
}
function packet(id,expected) {
  const dir=SC+'finite_residual_fresh'+id;
  const manifest=dir+'/SHA256SUMS', list=rows(manifest);
  same(sha(cache.get(manifest)),expected,'frozen seal '+id);
  same(list.length,9,'nine payloads '+id);
  same(fs.readdirSync(dir).sort(),[...list.map(x=>x.path),'SHA256SUMS'].sort(),'exact nonself inventory '+id);
  for(const row of list) {
    need(!row.path.includes('/')&&row.path!=='SHA256SUMS','flat nonself payload '+id);
    same(sha(read(dir+'/'+row.path)),row.sha256,'payload '+row.path);
  }
  const pins=rows(dir+'/INPUT_PINS.sha256');
  same(pins.length,id==='09'?22:20,'selected post-read pins '+id);
  for(const row of pins) same(sha(read(row.path)),row.sha256,'input '+row.path);
  const pinObj=JSON.parse(cache.get(dir+'/PIN_OBSERVATION_NATIVE.json'));
  const pinRecord=pinObj.record||pinObj;
  same(pinRecord.response.exit_code,0,'actual post-read hash exit '+id);
  same(Buffer.from(pinRecord.response.output),cache.get(dir+'/INPUT_PINS.sha256'),'actual pin stdout bytes '+id);
  return {id,dir,manifest_sha256:expected,payloads:9,files:10,pins:pins.length,
    payload_bytes:list.reduce((n,r)=>n+cache.get(dir+'/'+r.path).length,0)};
}
const packets=[
 packet('09','8e1672c595de0e080c760e5d5fae1453cfa9d67aa821b8c0222921b445eb85da'),
 packet('10','20455c9010f118a1a82bcc18b6d04d6c36dad624324dd62b29c06af30b4aa973')
];
const native=[], web=[];
for(const p of packets) {
  const a=JSON.parse(cache.get(p.dir+'/DOCUMENTARY_REQUEST_RETURNS.json'));
  const b=JSON.parse(cache.get(p.dir+'/CHECKS_NATIVE.json'));
  const w=JSON.parse(cache.get(p.dir+'/WEB_REQUEST_RETURNS.json'));
  const ar=a.entries||a.records, br=b.entries||b.records, wr=w.entries||w.records;
  same(ar.length,p.id==='09'?53:47,'documentary record count');
  same(br.length,p.id==='09'?5:6,'closing documentary record count');
  same(wr.length,p.id==='09'?10:7,'actual web record count');
  for(const [kind,records] of [['documentary',ar],['checks',br]]) for(const [i,r] of records.entries()) {
    need(r.request&&typeof r.request.cmd==='string','actual command');
    need(r.response&&Number.isInteger(r.response.exit_code)&&typeof r.response.output==='string'&&typeof r.response.chunk_id==='string','actual return fields');
    const out=Buffer.from(r.response.output);
    native.push({packet:p.id,kind,i,request:r.request,chunk_id:r.response.chunk_id,exit:r.response.exit_code,
      output_bytes:out.length,output_sha256:sha(out),capped:/truncat|bytes omitted|Total output lines/i.test(r.response.output)});
  }
  for(const [i,r] of wr.entries()) {
    need(r.request&&typeof r.request==='object','web request');
    need(typeof r.response==='string'||(r.response&&typeof r.response==='object'),'decoded web return');
    const data=Buffer.from(typeof r.response==='string'?r.response:JSON.stringify(r.response));
    web.push({packet:p.id,i,request:r.request,decoded_type:typeof r.response,decoded_bytes:data.length,decoded_sha256:sha(data)});
  }
  if(p.id==='10') {
    same(br.filter(r=>r.response.exit_code===127).length,2,'both jq failures retained');
    need(br.filter(r=>r.response.exit_code===127).every(r=>r.request.cmd.startsWith('jq ')&&r.response.output.includes('command not found')),'jq unavailability not PASS');
  }
}
const rootReads=JSON.parse(read(OUT+'ROOT_READS_NATIVE.json'));
same(rootReads.length,15,'root actual substantive read records');
let rawBytes=0;
const readPairs=[];
for(const r of rootReads) {
  same(r.return.exit_code,0,'root substantive read success');
  need(!/truncated output|tokens truncated/.test(r.return.output),'root complete returned slice');
  const m=/^sed -n '(\d+),(\d+)p' ([^ \n]+)$/.exec(r.request.cmd);
  need(m!==null,'declared simple sed slice');
  const full=read(m[3]), text=full.toString('utf8');
  same(Buffer.from(text),full,'lossless UTF8 source');
  const lines=text.match(/[^\n]*\n|[^\n]+$/g)||[];
  const expected=Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join(''));
  same(Buffer.from(r.return.output),expected,'raw original source slice '+r.key);
  rawBytes+=expected.length;
  readPairs.push({key:r.key,path:m[3],first:Number(m[1]),last:Math.min(Number(m[2]),lines.length),bytes:expected.length,sha256:sha(expected)});
}
const shapes=JSON.parse(read(OUT+'SHAPE_RETURNS_NATIVE.json'));
same(shapes.length,3,'preserved root shape attempts');
need(shapes.slice(0,2).every(r=>r.return.output.includes('truncated output')),'both excessive previews disclosed');
same(shapes[2].return.exit_code,0,'typed bounded shape return');
const before=[...seen.values()];
for(const k of before) same(sha(read(k.path)),k.sha256,'closing complete reread '+k.path);
process.stdout.write(JSON.stringify({status:'DOCUMENTARY_NEGATIVE_PACKET_RECEPTION_NOT_SCIENCE_OR_ADMISSION',checks,
  packets,full_keys:[...seen.values()],native,web,root_raw_source_pairs:readPairs,root_raw_source_bytes:rawBytes,
  science_runs:0,source_executions:0},null,2)+'\n');

