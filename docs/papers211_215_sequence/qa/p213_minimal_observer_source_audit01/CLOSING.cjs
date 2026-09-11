// Finite documentary closing only; no reviewed program or archived request is run.
'use strict';
const fs=require('node:fs'),crypto=require('node:crypto');
const base='docs/papers211_215_sequence/qa/p213_minimal_observer_source_audit01/';
const source='docs/papers211_215_sequence/qa/p213_minimal_observer_source01/';
const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
let checks=0;const keys=new Map(),bodies=new Map(),pairs=[];
function ok(v,m){checks++;if(!v)throw Error(m);}
function sha(b){return crypto.createHash('sha256').update(b).digest('hex');}
function read(p){
  const a=fs.lstatSync(p,{bigint:true});ok(a.isFile()&&!a.isSymbolicLink()&&a.size<1000000n,'bounded regular documentary file');
  const fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NONBLOCK|fs.constants.O_NOFOLLOW);
  const meta=s=>Object.fromEntries(fields.map(n=>{ok(typeof s[n]==='bigint','integer field');return [n,String(s[n])];}));
  let first,last,b;try{const s=fs.fstatSync(fd,{bigint:true});ok(s.isFile(),'regular fd');first=meta(s);ok(JSON.stringify(first)===JSON.stringify(meta(a)),'path/fd before');b=fs.readFileSync(fd);last=meta(fs.fstatSync(fd,{bigint:true}));}finally{fs.closeSync(fd);}
  ok(JSON.stringify(first)===JSON.stringify(last)&&JSON.stringify(first)===JSON.stringify(meta(fs.lstatSync(p,{bigint:true}))),'fd/path endpoints');
  ok(BigInt(b.length)===BigInt(first.size),'whole bytes');
  const k={path:p,bytes:b.length,sha256:sha(b),metadata:first};if(keys.has(p))ok(JSON.stringify(k)===JSON.stringify(keys.get(p)),'repeat key');
  keys.set(p,k);bodies.set(p,b);return b;
}
const names=fs.readdirSync(base).sort();
ok(names.every(n=>/^[A-Za-z0-9_.-]+$/.test(n)),'own finite names');
for(const n of names)read(base+n);
function j(n){return JSON.parse(bodies.get(base+n));}
function raw(a,b,label){ok(a.equals(b),'raw compare '+label);pairs.push({label,bytes:a.length,sha256:sha(a)});}
const first=j('CHECK01_NATIVE.json'),second=j('CHECK02_NATIVE.json');
ok(first.native.exit_code===0&&second.native.exit_code===0,'two documentary check exits');
raw(Buffer.from(first.native.output),Buffer.from(second.native.output),'own-3420-check-pair');
const data=JSON.parse(first.native.output);
ok(data.checks===3420&&data.keys.length===33,'first counts');
const pins=bodies.get(base+'INPUTS.sha256').toString('utf8');
ok(pins===data.keys.map(k=>k.sha256+'  '+k.path+'\n').join(''),'all33 input pins');
for(const k of data.keys){
  ok(k.path.startsWith(source)||k.path.startsWith('docs/papers211_215_sequence/qa/p213_runtime_')||/^papers\/213-receiver-limited-cyclic-transfer\/(RUNTIME_PLAN|SCIENTIFIC_DEPENDENCIES)\.md$/.test(k.path),'closing selected documentary input');
  read(k.path);ok(JSON.stringify(keys.get(k.path))===JSON.stringify(k),'closing full old key');
}
const author=JSON.parse(bodies.get(source+'CHECK_NATIVE.json'));
const replay=j('REPLAY_NATIVE.json');
ok(replay.length===2&&replay[1].label==='author-documentary-replay'&&replay[1].native.exit_code===0,'actual author replay');
raw(Buffer.from(author.result.output),Buffer.from(replay[1].native.output),'author-2189-check-replay');
raw(bodies.get(base+'CHECK_ARCHIVE.cjs'),Buffer.from(replay[0].native.output),'own-whole-checker-read');
const src=j('SOURCE_READS_NATIVE.json');
ok(src.length===4,'four whole source read groups');
const observe=bodies.get(source+'observe.py').toString('utf8').split('\n');
const slice=(a,b)=>Buffer.from(observe.slice(a-1,b).join('\n')+'\n');
raw(slice(1,245),Buffer.from(src[0].native.output),'observer-first245');
raw(Buffer.concat([slice(246,438),bodies.get(source+'capture.disabled.sh')]),Buffer.from(src[1].native.output),'observer-last193-capture40');
const catNames=['CONTRACT.md','BINDING_FORMAT.md','BINDING.disabled.json','CAPTURE_REQUEST.disabled.json'];
raw(Buffer.concat(catNames.map(n=>bodies.get(source+n))),Buffer.from(src[2].native.output),'whole-contracts-disabled');
const finalNames=['SELECTION_REQUEST.md','HANDOFF.md','READ_SCOPE.md','INPUTS.sha256','SHA256SUMS','CHECK_DOCUMENTS.cjs'];
raw(Buffer.concat(finalNames.map(n=>bodies.get(source+n))),Buffer.from(src[3].native.output),'whole-selection-provenance-seals-checker');
raw(Buffer.concat([bodies.get(base+'REPORT.md'),bodies.get(base+'FINDINGS.json')]),Buffer.from(j('REPORT_READ_NATIVE.json').native.output),'whole-report-findings');
const findings=j('FINDINGS.json');
ok(findings.finding_census.Major===2&&findings.finding_census.open===2&&findings.findings.every(f=>f.status==='OPEN'),'two open source findings');
ok(findings.source_accepted===false&&findings.probe_authorized===false&&findings.runtime_accepted===false,'no acceptance/operation grant');
ok(observe[338].includes('os.stat("/proc/self/exe")')&&observe[341].includes('need(record["proc_exe"] == entry["final"]'),'F01 exact source anchors');
ok(observe[112].includes('exc.args[0] if type(exc) is RuntimeError'),'F02 exact source anchor');
const snapshot=[...keys.values()];for(const k of snapshot)read(k.path);
process.stdout.write(JSON.stringify({status:'INDEPENDENT_SOURCE_AUDIT_DOCUMENTARY_CLOSING',checks,source_runtime_execution:false,source_accepted:false,
original_findings_open:2,selected_input_keys:33,preclosing_own_files:names.length,raw_pairs:pairs,keys:[...keys.values()]},null,2)+'\n');
