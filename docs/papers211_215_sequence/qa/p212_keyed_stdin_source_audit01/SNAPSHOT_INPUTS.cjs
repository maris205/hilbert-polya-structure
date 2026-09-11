'use strict';
// Read/hash only workspace documentary files; never execute reviewed sources.
const fs=require('fs'),crypto=require('crypto'),path=require('path');
const root='/root/autodl-tmp/symbolic_dynamics';
if(process.cwd()!==root)throw Error('wrong documentary cwd');
const qa='docs/papers211_215_sequence/qa/';
const author=qa+'p212_keyed_stdin_source_delta01';
const accepted=qa+'p212_preprobe_native_mask_analysis01/INPUT_SHA256SUMS';
const allowedSpecial=new Set([accepted]);
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const cache=new Map();let checks=0;
function ok(c,m){checks++;if(!c)throw Error(m);}
function sha(b){return crypto.createHash('sha256').update(b).digest('hex');}
function meta(s){return Object.fromEntries(fields.map(k=>[k,s[k].toString()]));}
function raw(p){
 ok(p.startsWith(qa)&&!p.includes('..')&&!path.isAbsolute(p),'workspace QA documentary path');
 ok(!p.includes('/p212_keyed_stdin_input01/'),'never inspect proposed input');
 const l0=fs.lstatSync(p,{bigint:true});ok(l0.isFile()&&!l0.isSymbolicLink(),'regular documentary file');
 const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
 try{
  const f0=fs.fstatSync(fd,{bigint:true});ok(f0.isFile()&&f0.size<=67108864n,'regular bounded documentary fd');
  ok(JSON.stringify(meta(l0))===JSON.stringify(meta(f0)),'before-read same key');
  const b=fs.readFileSync(fd),f1=fs.fstatSync(fd,{bigint:true}),l1=fs.lstatSync(p,{bigint:true});
  ok(BigInt(b.length)===f1.size&&JSON.stringify(meta(f0))===JSON.stringify(meta(f1))&&JSON.stringify(meta(f1))===JSON.stringify(meta(l1)),'after whole-byte read key');
  return {bytes:b,key:{path:p,sha256:sha(b),byte_count:b.length,...meta(f1)}};
 }finally{fs.closeSync(fd);}
}
function read(p){if(!cache.has(p))cache.set(p,raw(p));return cache.get(p).bytes;}
function manifest(p,kind){
 const b=read(p),s=b.toString('utf8');ok(Buffer.from(s).equals(b),'manifest UTF8');
 const suffix=allowedSpecial.has(p)?'\n\n':'\n';ok(s.endsWith(suffix)&&!s.endsWith(suffix+'\n'),'exact manifest ending');
 const names=new Set();return s.slice(0,-suffix.length).split('\n').map(line=>{
  const m=/^([a-f0-9]{64})  (\S+)$/.exec(line);ok(!!m&&!names.has(m[2]),'manifest syntax and unique');names.add(m[2]);
  ok(!m[2].includes('..')&&!path.isAbsolute(m[2]),'manifest safe path');
  if(kind==='author')ok(/^(?:[A-Za-z0-9_.]+\/)*[A-Za-z0-9_.]+$/.test(m[2]),'author basename layout');
  else ok(m[2].startsWith(qa),'workspace pin path');
  return {sha256:m[1],path:kind==='author'?author+'/'+m[2]:m[2]};
 });
}
const seal=manifest(author+'/SHA256SUMS','author');
ok(sha(read(author+'/SHA256SUMS'))==='f076522fc7e120c46be0c57b60168784c38c32339e07f65b74e0012694ca1ee8','root-transmitted frozen seal');
ok(seal.length===55,'55 frozen payloads');
const pins=manifest(author+'/SOURCE_INPUTS.sha256','workspace');ok(pins.length===29,'29 original pins');
const controls=manifest(accepted,'workspace');ok(controls.length===23,'23 accepted analysis inputs');
for(const r of [...seal,...pins,...controls])ok(sha(read(r.path))===r.sha256,'complete selected digest '+r.path);
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(dir+'/'+e.name):[dir+'/'+e.name]);}
ok(JSON.stringify(walk(author).sort())===JSON.stringify([...seal.map(r=>r.path),author+'/SHA256SUMS'].sort()),'exact frozen physical inventory');
const keys=[...cache.values()].map(r=>r.key).sort((a,b)=>a.path.localeCompare(b.path,'en'));
for(const k of keys)ok(JSON.stringify(raw(k.path).key)===JSON.stringify(k),'second complete key same');
console.log(JSON.stringify({scope:'DOCUMENTARY_SOURCE_INPUT_SNAPSHOT_NOT_SOURCE_EXECUTION_OR_RUNTIME',status:'INPUT_KEYS_VERIFIED',checks,author_payloads:55,author_files:56,author_seal_sha256:sha(read(author+'/SHA256SUMS')),author_original_pins:29,accepted_analysis_pins:23,accepted_analysis_pin_ending:'EXACT_TWO_LF_RETAINED_NOT_STRICT_SINGLE_LF',distinct_inputs:keys.length,total_bytes:keys.reduce((n,k)=>n+k.byte_count,0),before_after_keys_equal:true,input_keys:keys,live_stdin_inspected:false,reviewed_source_executed:false},null,2));
