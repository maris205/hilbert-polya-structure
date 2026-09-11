'use strict';
// Ordinary-trusted documentary intake only. Never evaluate scientific source.
const fs = require('fs'), crypto = require('crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics/';
const BASE = 'docs/papers211_215_sequence/qa/';
const OWN = BASE+'p213_source_parameter_root01/';
const PAPER = 'papers/213-receiver-limited-cyclic-transfer/';
const AUDIT = BASE+'p213_source_parameter_audit01/';
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

const receipt=json(OWN+'RECEIVE_DELTA01_NATIVE.json');
const actual=receipt.response;
need(actual.exit_code===0,'successful actual reception');
const received=JSON.parse(actual.output);
need(received.checks===3994&&received.keys.length===88,'exact reception scope');
for(const key of received.keys)need(same(read(key.path).key,key),'unchanged received full key');
const names=inventory(OWN);
need(!names.some(p=>p.endsWith('/SHA256SUMS')||p.endsWith('/CLOSING_NATIVE.json')),'closing before seal/output');
for(const p of names)get(p);
const text=get(OWN+'RECEPTION.md').body.toString('utf8');
const path=require('path');
const links=[...text.matchAll(/\]\(([^)]+)\)/g)].map(m=>m[1]);
for(const link of links){
  need(!link.includes('://'),'only explicit local receipt links');
  const resolved=path.posix.normalize(OWN+link);
  need(get(resolved).key.bytes>0,'existing complete linked original');
}
need(links.length===4,'four controlling originals');
const old=get(OWN+'receive.cjs').body.toString('utf8');
const newer=get(OWN+'receive_delta01.cjs').body.toString('utf8');
const oldRow="[TITLE,'SHA256SUMS','636ea07ac597258f132e4e68f242d45e8c086e0f1974be56748403eaa2a235bc',9,'./',false]";
const newRow="[TITLE,'SHA256SUMS','636ea07ac597258f132e4e68f242d45e8c086e0f1974be56748403eaa2a235bc',9,'',false]";
need(old.includes(oldRow)&&old.replace(oldRow,newRow)===newer,'only exact layout adapter delta');
for(const [p,x]of items)need(same(read(p).key,x.key),'closing complete endpoint');
need(same(inventory(OWN),names),'unchanged closing inventory');
console.log(JSON.stringify({status:'P213_SOURCE_PARAMETER_ROOT_CLOSING_PASS',checks,scientific_or_runtime_execution:false,received_keys_unchanged:88,receipt_links:links.length,preclosing_payloads:names.length,metadata_fields:FIELDS,keys:[...items.values()].map(x=>x.key).sort((a,b)=>a.path.localeCompare(b.path))}));
