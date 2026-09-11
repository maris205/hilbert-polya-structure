'use strict';
// Ordinary-trusted documentary intake only. Never evaluate scientific source.
const fs = require('fs'), crypto = require('crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics/';
const BASE = 'docs/papers211_215_sequence/qa/';
const OWN = BASE+'p213_runtime_design_root01/';
const PAPER = 'papers/213-receiver-limited-cyclic-transfer/';
const AUDIT = BASE+'p213_runtime_design_audit01/';
const TITLE = BASE+'p213_source_parameter_title_delta01/';
const ERRATUM = BASE+'p213_source_title_erratum01/';
const FIELDS = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const items = new Map();
let checks = 0;
function need(ok,label) { checks++; if (!ok) throw Error(label); }
const same = (a,b) => JSON.stringify(a)===JSON.stringify(b);
const hash = b => crypto.createHash('sha256').update(b).digest('hex');
const meta = st => FIELDS.map(k=>st[k].toString());
function safe(p) {
  need(/^(docs|papers)\/[A-Za-z0-9_.\/-]+$/.test(p)&&!p.split('/').some(x=>!x||x==='.'||x==='..'),'workspace spelling');
  const bits=p.split('/');
  for(let i=1;i<bits.length;i++) need(fs.lstatSync(ROOT+bits.slice(0,i).join('/')).isDirectory(),'physical parent');
}
function read(p) {
  safe(p); const st=fs.lstatSync(ROOT+p,{bigint:true});
  need(st.isFile()&&st.size<=8388608n,'bounded regular document');
  const fd=fs.openSync(ROOT+p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let body;
  try {
    need(same(meta(st),meta(fs.fstatSync(fd,{bigint:true}))),'opened descriptor');
    const parts=[];let size=0;
    for(;;){const b=Buffer.alloc(Math.min(65536,8388608-size+1)),n=fs.readSync(fd,b,0,b.length,null);if(!n)break;size+=n;need(size<=8388608,'bounded whole read');parts.push(b.subarray(0,n));}
    body=Buffer.concat(parts);need(same(meta(st),meta(fs.fstatSync(fd,{bigint:true}))),'descriptor endpoint');
  } finally { fs.closeSync(fd); }
  need(same(meta(st),meta(fs.lstatSync(ROOT+p,{bigint:true}))),'path endpoint');
  need(BigInt(body.length)===st.size,'exact byte count');safe(p);
  return {body,key:{path:p,bytes:body.length,sha256:hash(body),metadata:meta(st)}};
}
function get(p) {if(!items.has(p))items.set(p,read(p));return items.get(p);}
const json = p => JSON.parse(get(p).body);
function inventory(dir,sections=false) {
  safe(dir.slice(0,-1));need(fs.lstatSync(ROOT+dir).isDirectory(),'physical packet');
  const out=[];
  for(const name of fs.readdirSync(ROOT+dir).sort()){
    const p=dir+name,st=fs.lstatSync(ROOT+p);
    if(st.isDirectory()){need(sections&&name==='sections','only selected section directory');out.push(...inventory(p+'/'));}
    else {need(st.isFile(),'regular inventory entry');out.push(p);}
  }
  return out.sort();
}

const PREP=BASE+'p213_runtime_preparation01/';
const packs=[[PREP,7,'','f0e254caa515275cbd95848ba9845909a94b94d681e7c3e58569f9a5c2e1fefa'],[AUDIT,13,'./','ccc7b8d49dd1d4c03a42620a7bb9c5398129b9b9bc3fc10ba87758b030cbf7cb']];
const packets=[];
for(const[dir,count,prefix,digest]of packs){
 const paths=inventory(dir);need(paths.length===count+1,'exact packet files');paths.forEach(get);
 const seal=get(dir+'SHA256SUMS');need(seal.key.sha256===digest,'selected whole seal');
 const rows=seal.body.toString().split('\n');need(rows.pop()===''&&rows.length===count,'strict nonself rows');const members=[];
 for(const row of rows){const m=/^([a-f0-9]{64})  (.+)$/.exec(row);need(m&&m[2].startsWith(prefix),'exact manifest prefix');const member=m[2].slice(prefix.length);need(/^[A-Za-z0-9_.]+$/.test(member)&&member!=='SHA256SUMS'&&!members.includes(member),'unique bare member');need(get(dir+member).key.sha256===m[1],'payload hash');members.push(member);}
 need(same([...members,'SHA256SUMS'].map(x=>dir+x).sort(),paths),'exact nonself coverage');
 packets.push({path:dir,payloads:count,files:paths.length,bytes:paths.reduce((n,p)=>n+get(p).key.bytes,0),sha256:digest,paths});
}
const response=r=>r.response||r.result||r.returned;
function native(r){const v=response(r);need(r.request&&typeof r.request.cmd==='string'&&v&&typeof v.output==='string'&&Number.isInteger(v.exit_code)&&typeof v.chunk_id==='string','actual request/return');return v;}
const ownRun=native(json(OWN+'REPLAY_NATIVE.json')),otherRun=native(json(AUDIT+'CHECK_NATIVE.json').record);
need(ownRun.exit_code===0&&otherRun.exit_code===0,'successful actual documentary replays');
need(Buffer.from(ownRun.output).equals(Buffer.from(otherRun.output)),'complete raw replay equality');
const data=JSON.parse(ownRun.output);need(data.checks===415&&data.input_keys.length===12&&!data.scientific_execution&&!data.live_runtime_observation,'exact documentary scope');
for(const key of data.input_keys){const now=get(key.path).key;need(now.sha256===key.sha256&&now.bytes===key.byte_count&&FIELDS.every((f,i)=>now.metadata[i]===key[f]),'twelve original complete keys');}
for(const[dir,count]of [[PREP,4],[AUDIT,12]]){const rows=get(dir+'INPUTS.sha256').body.toString().split('\n');need(rows.pop()===''&&rows.length===count,'strict input count');const seen=[];for(const row of rows){const m=/^([a-f0-9]{64})  ((?:papers|docs)\/[A-Za-z0-9_.\/-]+)$/.exec(row);need(m&&!seen.includes(m[2]),'unique input pin');need(get(m[2]).key.sha256===m[1],'input hash');seen.push(m[2]);}}
const sourceRoot=BASE+'p213_source_parameter_root01/';
need(get(sourceRoot+'SHA256SUMS').key.sha256==='d2fdf9d1b2e3d73329e166c6c55b018f1c2236e7354f75cfb3963c8334796d70','accepted source root seal');
need(get(sourceRoot+'RECEPTION.md').key.sha256==='9b6ce21ef4de793e69722b50704985fe525c36cb374fe026b4a284400ce24edc','accepted source root receipt');
const report=get(AUDIT+'REPORT.md');need(report.key.sha256==='8e81bb4af248492649b6d61061ebc8b73d73841542ec6029d5a8fbc87a908214','selected complete report');
const findings=json(AUDIT+'FINDINGS.json');need(findings.open_design_defects_found===0&&findings.concrete_design_blockers.length===0&&findings.mandatory_future_source_acceptance_obligations.length===7&&!findings.probe_authorization&&!findings.runtime_acceptance&&!findings.source_acceptance,'scoped decision not grant');
const records=[];
function gather(v,label){if(!v||typeof v!=='object')return;if(v.request&&typeof v.request.cmd==='string'&&response(v)){records.push({label,record:v});return;}if(Array.isArray(v)){v.forEach((x,i)=>gather(x,label+'['+i+']'));return;}for(const[k,x]of Object.entries(v))if(x&&typeof x==='object')gather(x,label+'.'+k);}
for(const dir of [PREP,AUDIT,OWN])for(const p of inventory(dir).filter(p=>p.endsWith('_NATIVE.json')&&!p.endsWith('/PRIMARY_NATIVE.json')))gather(json(p),p);
let rawBytes=0;const raw=[];let allBytes=0;
for(const{label,record}of records){
 const r=native(record);allBytes+=Buffer.byteLength(r.output);if(r.exit_code!==0)continue;
 const outputs=[];let selected=true;
 for(const part of record.request.cmd.split(' && ')){const m=/^sed -n '([0-9]+),([0-9]+)p' ((?:docs|papers)\/[A-Za-z0-9_.\/-]+)$/.exec(part);if(!m||!items.has(m[3])){selected=false;break;}const b=get(m[3]).body;need(b[b.length-1]===10,'source final LF');outputs.push(b.toString().slice(0,-1).split('\n').slice(Number(m[1])-1,Number(m[2])).map(x=>x+'\n').join(''));}
 if(!selected)continue;const bytes=Buffer.from(outputs.join(''));need(bytes.equals(Buffer.from(r.output)),'selected raw read '+label);rawBytes+=bytes.length;raw.push({chunk_id:r.chunk_id,bytes:bytes.length,sha256:hash(bytes),label});
}
need(raw.length>=10,'substantive raw original coverage');
const errors=json(AUDIT+'CHECK_FAILED_NATIVE.json').records;need(native(errors[0]).exit_code!==0,'old exact-layout failure preserved');
const close=json(AUDIT+'CLOSING_NATIVE.json').records;
need(close.length===4,'four auditor closing commands');
for(const r of close)need(native(r).exit_code===0,'actual successful audit closing');
need(JSON.parse(native(close[3]).output).checks===150,'actual closing scope');
for(const[p,x]of items)need(same(read(p).key,x.key),'unchanged full endpoints');
for(const p of packets)need(same(inventory(p.path),p.paths),'unchanged membership');
console.log(JSON.stringify({status:'P213_MINIMAL_DESIGN_AND_INDEPENDENT_AUDIT_RECEIVED_NOT_RUNTIME',checks,whole_keys:items.size,metadata_fields:FIELDS,packets:packets.map(({paths,...p})=>p),documentary_replay:{checks:415,raw_bytes:Buffer.byteLength(ownRun.output),raw_sha256:hash(Buffer.from(ownRun.output)),equals_independent:true},selected_native_records:records.length,selected_native_output_bytes:allBytes,raw_source_records:raw.length,raw_source_bytes:rawBytes,raw,source_or_runtime_operations:false,keys:[...items.values()].map(x=>x.key).sort((a,b)=>a.path.localeCompare(b.path))}));
