'use strict';
// New-only exact basename-layout adapter; CHECK_INPUTS.cjs failure stays intact.
// Ordinary workspace documentary checking, not a P213 runtime observer.
const fs = require('fs');
const crypto = require('crypto');
const path = require('path');
const workspace = '/root/autodl-tmp/symbolic_dynamics';
if (process.cwd() !== workspace) throw Error('wrong documentary cwd');
const prep = 'docs/papers211_215_sequence/qa/p213_runtime_preparation01';
const paper = 'papers/213-receiver-limited-cyclic-transfer';
const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const prepNames = ['CLOSING_NATIVE.json','DESIGN.md','HANDOFF.md','INPUTS.sha256',
  'PRIMARY_NATIVE.json','READS_NATIVE.json','READ_SCOPE.md','SHA256SUMS'];
const paperNames = ['RUNTIME_PLAN.md','SCIENTIFIC_DEPENDENCIES.md',
  'VERIFICATION_PARAMETERS.json','SOURCE_MANIFEST.sha256'];
const names = [...prepNames.map(n => prep+'/'+n), ...paperNames.map(n => paper+'/'+n)].sort();
let checks = 0;
function check(condition, message) { checks++; if (!condition) throw Error(message); }
function sha(bytes) { return crypto.createHash('sha256').update(bytes).digest('hex'); }
function meta(s) { return Object.fromEntries(fields.map(k => [k, s[k].toString()])); }
function equal(a,b) { return JSON.stringify(a) === JSON.stringify(b); }
function get(name) {
  check(names.includes(name), 'unapproved documentary input');
  const st0 = fs.lstatSync(name, {bigint:true});
  check(st0.isFile() && !st0.isSymbolicLink(), 'nonregular input '+name);
  const fd = fs.openSync(name, fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW);
  try {
    const s0 = fs.fstatSync(fd, {bigint:true});
    check(s0.isFile() && s0.size < 16777216n, 'bound/type '+name);
    const bytes = fs.readFileSync(fd);
    const s1 = fs.fstatSync(fd, {bigint:true});
    const st1 = fs.lstatSync(name, {bigint:true});
    check(equal(meta(st0),meta(s0)) && equal(meta(s0),meta(s1)) && equal(meta(s1),meta(st1)), 'point metadata change '+name);
    check(BigInt(bytes.length) === s1.size, 'size '+name);
    return {bytes, key:{path:name,sha256:sha(bytes),byte_count:bytes.length,...meta(s1)}};
  } finally { fs.closeSync(fd); }
}
const before = new Map(names.map(n => [n,get(n)]));
function content(n) { check(before.has(n),'unread input'); return before.get(n).bytes; }
function manifest(buf, kind) {
  const text = buf.toString('utf8');
  check(Buffer.from(text,'utf8').equals(buf),'manifest UTF8');
  check(text.endsWith('\n'),'manifest final newline');
  const seen = new Set();
  return text.slice(0,-1).split('\n').map(line => {
    const m = /^([a-f0-9]{64})  (\S+)$/.exec(line);
    check(!!m,'strict manifest syntax');
    check(!seen.has(m[2]),'duplicate manifest member'); seen.add(m[2]);
    check(!m[2].includes('..') && !path.isAbsolute(m[2]),'unsafe manifest path');
    if (kind === 'relative') check(m[2].startsWith('./'),'relative ./ prefix');
    return {sha256:m[1],name:m[2]};
  });
}
const seal = manifest(content(prep+'/SHA256SUMS'),'basename');
check(seal.every(r => /^[A-Za-z0-9_.]+$/.test(r.name)), 'preparation basename-only layout');
check(seal.length === 7,'seven preparation payloads');
check(equal(seal.map(r => r.name).sort(),prepNames.filter(n => n !== 'SHA256SUMS').sort()),'exact preparation seal membership');
check(equal(fs.readdirSync(prep).sort(), [...prepNames].sort()),'exact physical preparation tree');
for (const r of seal) check(sha(content(prep+'/'+r.name)) === r.sha256,'preparation seal digest');
check(sha(content(prep+'/SHA256SUMS')) === 'f0e254caa515275cbd95848ba9845909a94b94d681e7c3e58569f9a5c2e1fefa','expected preparation seal');
check(sha(content(prep+'/DESIGN.md')) === '6dcfb89b271cfa1904ee8129831ab89f0a09eb3d1551542ca521517ab5373d84','expected design');
const inputs = manifest(content(prep+'/INPUTS.sha256'),'workspace');
check(equal(inputs.map(r => r.name).sort(),paperNames.map(n => paper+'/'+n).sort()),'exact four declared inputs');
for (const r of inputs) check(sha(content(r.name)) === r.sha256,'declared input digest');
const paperSeal = manifest(content(paper+'/SOURCE_MANIFEST.sha256'),'relative');
check(paperSeal.length === 29,'declared paper manifest length only');
for (const n of paperNames.filter(n => n !== 'SOURCE_MANIFEST.sha256')) {
  const r = paperSeal.find(r => r.name === './'+n);
  check(!!r && sha(content(paper+'/'+n)) === r.sha256,'three paper interface leaves');
}
// This design audit does not read or hash the other 26 paper payloads.
const params = JSON.parse(content(paper+'/VERIFICATION_PARAMETERS.json'));
check(params.status === 'DECLARED_SOURCE_ONLY_NOT_EXECUTED','parameter source status');
check(params.carrier.n_min === 1 && params.carrier.n_max === 6 && params.carrier.mass_min === 0 && params.carrier.mass_max === 4,'declared box');
check(params.carrier.expected_carriers === 30 && params.carrier.expected_states === 461,'declared totals only');
const reads = JSON.parse(content(prep+'/READS_NATIVE.json'));
const close = JSON.parse(content(prep+'/CLOSING_NATIVE.json'));
check(reads.records.length === 6 && close.records.length === 5,'native record census');
const rawComparisons = [];
function raw(record, expected, label) {
  check(record && record.result && record.result.exit_code === 0 && !record.result.session_id,'completed archived native '+label);
  check(typeof record.result.output === 'string','native output type');
  const actual = Buffer.from(record.result.output,'utf8');
  check(actual.equals(expected),'raw archived documentary output '+label);
  rawComparisons.push({label,bytes:actual.length,sha256:sha(actual),equal:true});
}
for (let i=0; i<4; i++) {
  const limit = i < 2 ? 240 : (i === 2 ? 180 : 120);
  check(reads.records[i].request.cmd === "sed -n '1,"+limit+"p' "+paper+'/'+paperNames[i],'archived whole-file request');
  raw(reads.records[i],content(paper+'/'+paperNames[i]),'whole paper interface '+paperNames[i]);
}
raw(reads.records[4],content(prep+'/INPUTS.sha256'),'four sha256sum lines');
function wcRows(record, allowed) {
  check(record.result.exit_code === 0 && !record.result.session_id,'completed wc');
  const lines = record.result.output.trimEnd().split('\n');
  check(lines.length === allowed.length+1,'wc row census');
  let sumLines=0,sumBytes=0;
  for (let i=0;i<allowed.length;i++) {
    const m = /^\s*(\d+)\s+(\d+)\s+(\S+)$/.exec(lines[i]);
    check(!!m && m[3] === allowed[i],'wc path');
    const b=content(allowed[i]); const count=b.reduce((n,c)=>n+(c===10?1:0),0);
    check(Number(m[1])===count && Number(m[2])===b.length,'wc declared bytes/lines');
    sumLines+=count;sumBytes+=b.length;
  }
  const t=/^\s*(\d+)\s+(\d+)\s+total$/.exec(lines.at(-1));
  check(!!t && Number(t[1])===sumLines && Number(t[2])===sumBytes,'wc totals');
}
wcRows(reads.records[5],paperNames.map(n => paper+'/'+n));
raw(close.records[0],Buffer.from(paperNames.map(n => paper+'/'+n+': OK\n').join('')),'four input strict OK lines');
wcRows(close.records[1],['DESIGN.md','READ_SCOPE.md','HANDOFF.md','INPUTS.sha256','READS_NATIVE.json','PRIMARY_NATIVE.json'].map(n=>prep+'/'+n));
const designLines=content(prep+'/DESIGN.md').toString('utf8').split('\n');
check(designLines.length===236,'235 design lines');
raw(close.records[2],Buffer.from(designLines.slice(109,157).join('\n')+'\n'),'design lines 110 through 157');
raw(close.records[3],content(prep+'/READ_SCOPE.md'),'complete design read scope');
raw(close.records[4],content(prep+'/HANDOFF.md'),'complete design handoff');
const primary=JSON.parse(content(prep+'/PRIMARY_NATIVE.json'));
check(primary.scope==='ACTUAL_PUBLIC_PRIMARY_DOCUMENT_EXCERPT_ACCESS_NOT_INSTALLED_HOST_ATTESTATION','primary source scope');
check(primary.record.request.open.length===7 && typeof primary.record.result==='string','primary access request/return census');
check(primary.record.request.open.every(r=>/^https:\/\/(docs\.python\.org|raw\.githubusercontent\.com|www\.kernel\.org)\//.test(r.ref_id)),'public reference hosts');
const after=names.map(n=>get(n).key);
for (let i=0;i<names.length;i++) check(equal(before.get(names[i]).key,after[i]),'before/after full documentary key');
console.log(JSON.stringify({status:'DOCUMENTARY_INPUTS_AND_ARCHIVED_RAW_RETURNS_VERIFIED',
  checks,scoped_input_files:names.length,total_input_bytes:[...before.values()].reduce((n,v)=>n+v.bytes.length,0),
  preparation:{files:8,payloads:7,bytes:prepNames.reduce((n,v)=>n+content(prep+'/'+v).length,0),seal_sha256:sha(content(prep+'/SHA256SUMS'))},
  paper_interfaces:4,raw_comparisons:rawComparisons,semantic_wc_tables:2,
  author_native_records:11,public_request_members:7,
  input_keys:after,before_after_full_keys_equal:true,
  scientific_execution:false,live_runtime_observation:false,source_or_probe_authority:false},null,2));
