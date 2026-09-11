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
const packs=[
  [PAPER,'SOURCE_MANIFEST.sha256','e232b73013c3d6d1828e778f800f981bf00921a4a6f56f979aaec6e044ebdc09',29,'./',true],
  [AUDIT,'SHA256SUMS','2e95d4d54a0af957e4641e142e939c5ed6949ab4d30656988d973a83dc61fa7e',16,'./',false],
  [ERRATUM,'SHA256SUMS','ebbe3b0cc7afc72a402989c6d5df7ae8416c8b2b7b931f42784b8bea63de0f47',4,'',false],
  [TITLE,'SHA256SUMS','636ea07ac597258f132e4e68f242d45e8c086e0f1974be56748403eaa2a235bc',9,'',false]
];
const packets=[];
for(const [dir,seal,digest,count,prefix,sections] of packs){
  const paths=inventory(dir,sections);need(paths.length===count+1,'exact packet count');paths.forEach(get);
  need(get(dir+seal).key.sha256===digest,'selected whole seal');
  const rows=get(dir+seal).body.toString('utf8').split('\n');need(rows.pop()===''&&rows.length===count,'strict single-LF nonself rows');
  const names=[];
  for(const row of rows){const m=/^([a-f0-9]{64})  (.+)$/.exec(row);need(m&&m[2].startsWith(prefix),'seal row');const rel=m[2].slice(prefix.length),p=dir+rel;safe(p);need(rel!==seal&&paths.includes(p)&&!names.includes(p),'unique selected payload');need(get(p).key.sha256===m[1],'whole payload hash');names.push(p);}
  need(same([...names,dir+seal].sort(),paths),'complete nonself membership');
  packets.push({path:dir,payloads:count,files:paths.length,bytes:paths.reduce((n,p)=>n+get(p).key.bytes,0),seal_sha256:digest,paths});
}
function pins(p,count) {
  const rows=get(p).body.toString('utf8').split('\n');need(rows.pop()===''&&rows.length===count,'exact strict pin count');const paths=[];
  for(const row of rows){const m=/^([a-f0-9]{64})  ((?:docs|papers)\/[A-Za-z0-9_.\/-]+)$/.exec(row);need(m&&!paths.includes(m[2]),'unique workspace pin');need(get(m[2]).key.sha256===m[1],'complete pin hash');paths.push(m[2]);}return paths;
}
pins(PAPER+'SOURCE_INPUTS.sha256',18);pins(AUDIT+'INPUT_PINS.sha256',48);pins(ERRATUM+'INPUTS.sha256',6);pins(TITLE+'INPUTS.sha256',52);
const result = r => r.response||r.result||r.returned;
function native(r){const v=result(r);need(r.request&&typeof r.request.cmd==='string'&&v&&typeof v.output==='string'&&Number.isInteger(v.exit_code)&&typeof v.chunk_id==='string','actual native request/return');return v;}
function rawEqual(a,b,label){need(Buffer.from(a).equals(Buffer.from(b)),label);}
const invRoot=native(json(OWN+'INVENTORY_REPLAY_NATIVE.json'));
const invBefore=native(json(AUDIT+'INVENTORY_BEFORE_NATIVE.json'));
const invAfter=native(json(AUDIT+'INVENTORY_AFTER_NATIVE.json'));
need([invRoot,invBefore,invAfter].every(x=>x.exit_code===0),'all inventory returns successful');
rawEqual(invRoot.output,invBefore.output,'root inventory raw equals first');rawEqual(invRoot.output,invAfter.output,'root inventory raw equals second');
const inv=JSON.parse(invRoot.output);need(inv.checks===1602&&inv.keys.length===48&&!inv.source_executed&&!inv.source_ast_or_syntax_parsed,'inventory scope');
for(const key of inv.keys)need(same(get(key.path).key,key),'original inventory complete key');
const closureRoot=native(json(OWN+'CLOSURE_REPLAY_NATIVE.json'));
const closureAudit=native(json(AUDIT+'CLOSURE_DELTA01_NATIVE.json').execution);
need(closureRoot.exit_code===0&&closureAudit.exit_code===0,'two successful closure returns');rawEqual(closureRoot.output,closureAudit.output,'closure raw equality');
const closure=JSON.parse(closureRoot.output);need(closure.checks===1437&&closure.exact_compared_read_records===42,'received closure scope');
const titleFirst=native(json(TITLE+'INPUTS_NATIVE.json')),titleLast=native(json(TITLE+'CLOSING_NATIVE.json'));
need(titleFirst.exit_code===0&&titleLast.exit_code===0,'two title documentary successes');rawEqual(titleFirst.output,titleLast.output,'two title raw outputs');
const title=JSON.parse(titleFirst.output);need(title.checks===1499&&title.keys.length===52,'title scope');
for(const key of title.keys)need(same(get(key.path).key,key),'title complete endpoint key');
rawEqual(native(json(ERRATUM+'INPUTS_NATIVE.json')).output,get(ERRATUM+'INPUTS.sha256').body.toString('utf8'),'six erratum raw pins');
const records=[];
function gather(v,label){if(!v||typeof v!=='object')return;if(v.request&&typeof v.request.cmd==='string'&&result(v)){records.push({label,record:v});return;}if(Array.isArray(v)){v.forEach((x,i)=>gather(x,label+'['+i+']'));return;}for(const[k,x]of Object.entries(v))if(x&&typeof x==='object')gather(x,label+'.'+k);}
for(const dir of [AUDIT,TITLE,ERRATUM])for(const p of inventory(dir).filter(p=>p.endsWith('.json')&&!p.endsWith('PRIMARY_ACCESS.json')))gather(json(p),p);
for(const p of inventory(OWN).filter(p=>p.endsWith('_NATIVE.json')))gather(json(p),p);
function expected(command){const parts=[];
  for(const s of command.split(' && ')){
    const m=/^sed -n '([0-9]+),([0-9]+)p' ((?:docs|papers)\/[A-Za-z0-9_.\/-]+)$/.exec(s);if(!m)return null;
    const p=m[3];if(!items.has(p))return null;const b=get(p).body;need(b[b.length-1]===10,'selected source final LF');
    parts.push(b.toString('utf8').slice(0,-1).split('\n').slice(Number(m[1])-1,Number(m[2])).map(x=>x+'\n').join(''));
  }return parts.join('');
}
const comparisons=[];let savedBytes=0;
for(const {label,record}of records){const r=native(record);savedBytes+=Buffer.byteLength(r.output);const e=expected(record.request.cmd);if(e===null||r.exit_code!==0)continue;rawEqual(r.output,e,'selected native raw source '+label);comparisons.push({label,chunk_id:r.chunk_id,bytes:Buffer.byteLength(e),sha256:hash(Buffer.from(e))});}
need(comparisons.length>=40,'substantial original/root raw text coverage');
need(native(json(AUDIT+'CLOSURE_NATIVE.json').execution).exit_code!==0,'old closure failure preserved');
need(native(json(OWN+'TITLE_CODE_READ_NATIVE.json').failure).exit_code!==0,'root display failure preserved');
for(const [p,x]of items)need(same(read(p).key,x.key),'ending full key '+p);
for(const p of packets)need(same(inventory(p.path,p.path===PAPER),p.paths),'ending exact packet membership');
console.log(JSON.stringify({status:'ROOT_DOCUMENTARY_SOURCE_PARAMETER_TITLE_COMBINATION_RECEIVED',checks,science_or_runtime_executed:false,metadata_fields:FIELDS,whole_keys:items.size,packets:packets.map(({paths,...p})=>p),inventory_checks:inv.checks,inventory_raw_bytes:Buffer.byteLength(invRoot.output),inventory_raw_sha256:hash(Buffer.from(invRoot.output)),closure_checks:closure.checks,closure_raw_bytes:Buffer.byteLength(closureRoot.output),closure_raw_sha256:hash(Buffer.from(closureRoot.output)),title_checks:title.checks,title_complete_keys:title.keys.length,selected_native_records:records.length,selected_native_output_bytes:savedBytes,raw_source_comparisons:comparisons.length,raw_source_bytes:comparisons.reduce((n,x)=>n+x.bytes,0),comparisons,keys:[...items.values()].map(x=>x.key).sort((a,b)=>a.path.localeCompare(b.path))}));
