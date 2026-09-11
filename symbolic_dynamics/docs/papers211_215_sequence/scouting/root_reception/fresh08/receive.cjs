'use strict';
// Ordinary-trusted documentary intake only. Never evaluate scientific source.
const fs = require('fs'), crypto = require('crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics/';
const BASE = 'docs/papers211_215_sequence/qa/';
const OWN = 'docs/papers211_215_sequence/scouting/root_reception/fresh08/';
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
    if(st.isDirectory()){need(sections&&name==='shift_source_check','only selected section directory');out.push(...inventory(p+'/'));}
    else {need(st.isFile(),'regular inventory entry');out.push(p);}
  }
  return out.sort();
}

const PACK='docs/papers211_215_sequence/scouting/finite_residual_fresh08/';
const CHILD=PACK+'shift_source_check/';
const inventories=[];
for(const[dir,count,digest,subdir]of [[PACK,15,'333ffd015671bad53d7cf100701ba7ab2d1bb9edc7a27f06f0d29ff5435ba438',true],[CHILD,4,'c7ba071f128b5d0d3bc7774387f485eb645bacf7137efc781ccea969b44c44a8',false]]){
 const files=inventory(dir,subdir);need(files.length===count+1,'complete packet file count');files.forEach(get);
 const seal=get(dir+'SHA256SUMS');need(seal.key.sha256===digest,'exact selected whole seal');
 const rows=seal.body.toString().split('\n');need(rows.pop()===''&&rows.length===count,'strict nonself rows');const paths=[];
 for(const row of rows){const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.\/-]+)$/.exec(row);need(m,'strict manifest row');const p=dir+m[2];safe(p);need(p!==dir+'SHA256SUMS'&&files.includes(p)&&!paths.includes(p),'unique nonself payload');need(get(p).key.sha256===m[1],'whole payload hash');paths.push(p);}
 need(same([...paths,dir+'SHA256SUMS'].sort(),files),'exact coverage');
 inventories.push({path:dir,payloads:count,files:files.length,bytes:files.reduce((n,p)=>n+get(p).key.bytes,0),sha256:digest,paths:files});
}
const result=r=>r.response||r.result||r.returned;
function native(r){const v=result(r);need(r.request&&typeof r.request.cmd==='string'&&v&&typeof v.output==='string'&&Number.isInteger(v.exit_code)&&typeof v.chunk_id==='string','actual paired native');return v;}
const pinRecord=json(PACK+'INPUT_PINS_NATIVE.json');
const pinBody=native(pinRecord);need(pinBody.exit_code===0,'actual two-pin observation');
const pinRows=pinBody.output.split('\n');need(pinRows.pop()===''&&pinRows.length===2,'two pin rows');
const historical=[];
for(const row of pinRows){const m=/^([a-f0-9]{64})  ((?:docs|papers)\/[A-Za-z0-9_.\/-]+)$/.exec(row);need(m&&get(m[2]).key.sha256===m[1],'whole parent historical pin');historical.push(m[2]);}
const childPins=json(CHILD+'INPUT_PINS.json').pins;need(childPins.length===5,'five child pins');
for(const pin of childPins){need(!historical.includes(pin.path)&&get(pin.path).key.sha256===pin.sha256,'whole child historical pin');historical.push(pin.path);}
const records=[];
function gather(v,label){if(!v||typeof v!=='object')return;if(v.request&&typeof v.request.cmd==='string'&&result(v)&&typeof result(v)==='object'){records.push({label,record:v});return;}if(Array.isArray(v)){v.forEach((x,i)=>gather(x,label+'['+i+']'));return;}for(const[k,x]of Object.entries(v))if(x&&typeof x==='object')gather(x,label+'.'+k);}
for(const p of inventory(PACK,true).filter(p=>p.endsWith('.json')))gather(json(p),p);
gather(json(OWN+'ROOT_READS_NATIVE.json'),'root');
const path=require('path'),raw=[];let allBytes=0,failures=0,truncated=0;
for(const{label,record}of records){
 const r=native(record);allBytes+=Buffer.byteLength(r.output);if(r.exit_code!==0)failures++;if(r.output.includes('Warning: truncated output'))truncated++;
 const selected=label.startsWith('root')||record.request.cmd.split(' && ').every(part=>{const m=/^sed -n '[0-9]+,[0-9]+p' (.+)$/.exec(part);return m&&historical.includes(m[1]);});
 if(!selected||r.exit_code!==0)continue;
 const parts=[];let understood=true;
 for(const part of record.request.cmd.split(' && ')){
   const m=/^sed -n '([0-9]+),([0-9]+)p' ([A-Za-z0-9_.\/-]+)$/.exec(part);if(!m){understood=false;break;}
   const absolute=path.posix.resolve(record.request.workdir||ROOT,m[3]);need(absolute.startsWith(ROOT),'selected path in workspace');
   const relative=absolute.slice(ROOT.length);const b=get(relative).body;need(b[b.length-1]===10,'selected text finalLF');
   parts.push(b.toString().slice(0,-1).split('\n').slice(Number(m[1])-1,Number(m[2])).map(x=>x+'\n').join(''));
 }
 if(!understood)continue;const expected=Buffer.from(parts.join(''));need(expected.equals(Buffer.from(r.output)),'selected exact raw source '+label);raw.push({label,chunk_id:r.chunk_id,bytes:expected.length,sha256:hash(expected)});
}
need(raw.length>=10,'substantive complete raw source comparisons');
const childRecords=json(CHILD+'RECORDS.json').records;
need(childRecords.length===16&&childRecords.filter(r=>r.kind==='WEB').length===8&&childRecords.filter(r=>r.kind==='LOCAL').length===8,'child complete record kinds');
const lone=json(PACK+'LOCAL_NATIVE_RETURNS.json').fresh08_lyness_local;
need(typeof lone.output==='string'&&Number.isInteger(lone.exit_code),'preserved original without saved paired request');
need(native(json(CHILD+'POSTWRITE_CHECK.json').initial_failed_check).exit_code!==0,'old child working-directory failure retained');
const recordsOut={paired_records:records.length,paired_output_bytes:allBytes,failed_paired:failures,explicit_truncated_paired:truncated,unpaired_selected_native:1,unpaired_output_bytes:Buffer.byteLength(lone.output)};
for(const[p,x]of items)need(same(read(p).key,x.key),'unchanged complete document endpoints');
for(const p of inventories)need(same(inventory(p.path,p.path===PACK),p.paths),'unchanged frozen inventory');
console.log(JSON.stringify({status:'FRESH08_NEGATIVE_ORIGINALS_RECEIVED_NOT_PROMOTION',checks,whole_keys:items.size,metadata_fields:FIELDS,packets:inventories.map(({paths,...p})=>p),historical_pins:7,...recordsOut,raw_comparisons:raw.length,raw_bytes:raw.reduce((n,x)=>n+x.bytes,0),raw,scientific_source_or_runtime_executed:false,keys:[...items.values()].map(x=>x.key).sort((a,b)=>a.path.localeCompare(b.path))}));
