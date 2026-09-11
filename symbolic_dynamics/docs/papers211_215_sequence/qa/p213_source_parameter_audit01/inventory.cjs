'use strict';
// Ordinary-trusted workspace data inventory; never load or execute paper code.
const fs = require('fs');
const crypto = require('crypto');
const ROOT = "/root/autodl-tmp/symbolic_dynamics";
const PAPER = "papers/213-receiver-limited-cyclic-transfer";
const PAPER_FILES = [
  "papers/213-receiver-limited-cyclic-transfer/AUTHORSHIP.md",
  "papers/213-receiver-limited-cyclic-transfer/CLAIMS_EVIDENCE.md",
  "papers/213-receiver-limited-cyclic-transfer/HANDOFF.md",
  "papers/213-receiver-limited-cyclic-transfer/INTEGRITY_NATIVE.json",
  "papers/213-receiver-limited-cyclic-transfer/NARRATIVE_REPORT.md",
  "papers/213-receiver-limited-cyclic-transfer/OUTPUT_SCHEMA.md",
  "papers/213-receiver-limited-cyclic-transfer/PAPER_PLAN.md",
  "papers/213-receiver-limited-cyclic-transfer/PRIMARY_ACCESS.json",
  "papers/213-receiver-limited-cyclic-transfer/PROOF_PACKAGE.md",
  "papers/213-receiver-limited-cyclic-transfer/README.md",
  "papers/213-receiver-limited-cyclic-transfer/READS_NATIVE.json",
  "papers/213-receiver-limited-cyclic-transfer/READ_SCOPE.md",
  "papers/213-receiver-limited-cyclic-transfer/REVIEW_INTERFACES.md",
  "papers/213-receiver-limited-cyclic-transfer/RUNTIME_PLAN.md",
  "papers/213-receiver-limited-cyclic-transfer/SCIENTIFIC_DEPENDENCIES.md",
  "papers/213-receiver-limited-cyclic-transfer/SOURCE_AUDIT.md",
  "papers/213-receiver-limited-cyclic-transfer/SOURCE_INPUTS.sha256",
  "papers/213-receiver-limited-cyclic-transfer/SOURCE_MANIFEST.sha256",
  "papers/213-receiver-limited-cyclic-transfer/SOURCE_TEXT_CHECKS.json",
  "papers/213-receiver-limited-cyclic-transfer/VERIFICATION_PARAMETERS.json",
  "papers/213-receiver-limited-cyclic-transfer/main.tex",
  "papers/213-receiver-limited-cyclic-transfer/math_commands.tex",
  "papers/213-receiver-limited-cyclic-transfer/references.bib",
  "papers/213-receiver-limited-cyclic-transfer/sections/00_abstract.tex",
  "papers/213-receiver-limited-cyclic-transfer/sections/01_introduction.tex",
  "papers/213-receiver-limited-cyclic-transfer/sections/02_temporal.tex",
  "papers/213-receiver-limited-cyclic-transfer/sections/03_inverse.tex",
  "papers/213-receiver-limited-cyclic-transfer/sections/04_fibres.tex",
  "papers/213-receiver-limited-cyclic-transfer/sections/05_verification.tex",
  "papers/213-receiver-limited-cyclic-transfer/verify.py"
];
const EXTERNAL_FILES = [
  "docs/papers204_208_sequence/scouting/finite_systems_fortieth/MNA_PROOF.md",
  "docs/papers211_215_sequence/P213_THEOREM_CONTRACT.md",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh07/INPUTS.sha256",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh07/MANIFEST.sha256",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh07/PROOF_PACKAGE.md",
  "docs/papers211_215_sequence/scouting/finite_residual_fresh07/SOURCE_AND_COLLISION.md",
  "docs/papers211_215_sequence/scouting/fresh07_gate01/MANIFEST.sha256",
  "docs/papers211_215_sequence/scouting/fresh07_gate01/REPORT.md",
  "docs/papers211_215_sequence/scouting/fresh07_gate01/SOURCE_CHECK.md",
  "docs/papers211_215_sequence/scouting/fresh07_gate_delta01/DELTA_ACCEPTANCE.md",
  "docs/papers211_215_sequence/scouting/fresh07_gate_delta01/MANIFEST.sha256",
  "docs/papers211_215_sequence/scouting/fresh07_source_erratum01/ERRATUM.md",
  "docs/papers211_215_sequence/scouting/fresh07_source_erratum01/SHA256SUMS",
  "docs/papers211_215_sequence/scouting/root_reception/fresh07_candidate01/RECEPTION.md",
  "docs/papers211_215_sequence/scouting/root_reception/fresh07_candidate01/SHA256SUMS",
  "docs/papers211_215_sequence/scouting/transport_lane/PROOF_PACKAGE.md",
  "papers/211-kernel-image-projection-feedback/sections/1_introduction.tex",
  "papers/212-closed-pointer-orbits/sections/01_setup.tex"
];
const ALL = [...new Set([...PAPER_FILES, ...EXTERNAL_FILES])].sort();
const FIELDS = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const LIMIT = 8 * 1024 * 1024;
let checks = 0;
function need(ok, label) { checks++; if (!ok) throw Error(label); }
function digest(body) { return crypto.createHash('sha256').update(body).digest('hex'); }
function mark(st) { return FIELDS.map(k => st[k].toString()); }
function equal(a,b) { return JSON.stringify(a) === JSON.stringify(b); }
function pathOf(rel) {
  need(/^(papers|docs)\/[A-Za-z0-9_.\/-]+$/.test(rel) && !rel.split('/').some(x => !x || x === '.' || x === '..'), 'fixed relative path');
  return ROOT + '/' + rel;
}
function parents(rel) {
  const pieces = rel.split('/');
  for (let i = 1; i < pieces.length; i++) {
    const st = fs.lstatSync(ROOT + '/' + pieces.slice(0,i).join('/'), {bigint:true});
    need(st.isDirectory(), 'physical workspace parent: ' + rel);
  }
}
function read(rel) {
  const path = pathOf(rel);
  parents(rel);
  const before = fs.lstatSync(path, {bigint:true});
  need(before.isFile() && before.size <= BigInt(LIMIT), 'bounded regular input: ' + rel);
  const fd = fs.openSync(path, fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK);
  let body;
  try {
    need(equal(mark(before), mark(fs.fstatSync(fd, {bigint:true}))), 'opened key: ' + rel);
    const parts = [];
    let count = 0;
    while (true) {
      const chunk = Buffer.alloc(Math.min(65536, LIMIT - count + 1));
      const got = fs.readSync(fd, chunk, 0, chunk.length, null);
      if (!got) break;
      count += got;
      need(count <= LIMIT, 'bounded read: ' + rel);
      parts.push(chunk.subarray(0,got));
    }
    body = Buffer.concat(parts);
    need(equal(mark(before),mark(fs.fstatSync(fd,{bigint:true}))), 'descriptor ending key: ' + rel);
  } finally { fs.closeSync(fd); }
  need(equal(mark(before),mark(fs.lstatSync(path,{bigint:true}))), 'path ending key: ' + rel);
  need(BigInt(body.length) === before.size, 'whole byte count: ' + rel);
  parents(rel);
  return {body, key:{path:rel,bytes:body.length,sha256:digest(body),metadata:mark(before)}};
}
function listPaper(rel) {
  parents(rel);
  need(fs.lstatSync(pathOf(rel), {bigint:true}).isDirectory(), 'physical paper directory');
  const out = [];
  for (const name of fs.readdirSync(pathOf(rel)).sort()) {
    const child = rel + '/' + name;
    const st = fs.lstatSync(pathOf(child), {bigint:true});
    if (st.isDirectory()) {
      need(child === PAPER + '/sections', 'no unselected subdirectory');
      out.push(...listPaper(child));
    } else {
      need(st.isFile(), 'no alias or nonregular paper entry');
      out.push(child);
    }
  }
  return out.sort();
}
need(process.argv.length === 2, 'no modes or external paths');
need(equal(listPaper(PAPER), PAPER_FILES), 'exact thirty-file paper inventory');
const before = new Map(ALL.map(rel => [rel,read(rel)]));
const textOf = rel => before.get(rel).body.toString('utf8');
const seal = PAPER + '/SOURCE_MANIFEST.sha256';
need(before.get(seal).key.sha256 === 'e232b73013c3d6d1828e778f800f981bf00921a4a6f56f979aaec6e044ebdc09', 'root-selected whole paper seal');
const manifestLines = textOf(seal).split('\n');
need(manifestLines.pop() === '' && manifestLines.length === 29, 'strict nonself manifest lines');
const named = [];
for (const line of manifestLines) {
  const match = /^([a-f0-9]{64})  \.\/([A-Za-z0-9_.\/-]+)$/.exec(line);
  need(match !== null, 'manifest row grammar');
  const rel = PAPER + '/' + match[2];
  need(before.has(rel) && rel !== seal && !named.includes(rel), 'unique manifest membership');
  need(before.get(rel).key.sha256 === match[1], 'manifest whole hash: ' + rel);
  named.push(rel);
}
need(equal([...named,seal].sort(),PAPER_FILES), 'all payloads and only payloads sealed');
const pinLines = textOf(PAPER + '/SOURCE_INPUTS.sha256').split('\n');
need(pinLines.pop() === '' && pinLines.length === 18, 'strict eighteen historical pins');
const pinned = [];
for (const line of pinLines) {
  const match = /^([a-f0-9]{64})  ([A-Za-z0-9_.\/-]+)$/.exec(line);
  need(match !== null && EXTERNAL_FILES.includes(match[2]) && !pinned.includes(match[2]), 'explicit historical pin');
  need(before.get(match[2]).key.sha256 === match[1], 'historical whole hash: ' + match[2]);
  pinned.push(match[2]);
}
need(equal(pinned.sort(), [...EXTERNAL_FILES].sort()), 'exact pinned historical membership');
const source = textOf(PAPER + '/verify.py');
need(before.get(PAPER + '/verify.py').key.sha256 === 'a01d3d93619cea90adfc2e5be1bdfd8089d7eae6fcaae153b4fb4af398fc1812', 'root-selected verifier whole hash');
need(source.length === 17539 && /^[\x00-\x7f]*$/.test(source) && source.split('\n').length-1 === 451, 'whole ASCII source size and lines');
const parameters = JSON.parse(textOf(PAPER + '/VERIFICATION_PARAMETERS.json'));
const expectedConstants = {N_MIN:1,N_MAX:6,MASS_MIN:0,MASS_MAX:4,EXPECTED_CARRIERS:30,EXPECTED_STATES:461};
need(equal(parameters.code_constants,expectedConstants), 'exact parameter constants object');
for (const [key,value] of Object.entries(expectedConstants)) {
  need(source.split('\n').filter(line=>line === key + ' = ' + value).length === 1, 'literal constant agreement: ' + key);
}
need(parameters.carrier.labelled === true && parameters.carrier.rotation_quotient === false && parameters.literal.simultaneous_old_state === true, 'literal carrier declarations');
need(parameters.imports.length === 0 && parameters.runtime_parameter_reads.length === 0 && parameters.old_artifact_imports.length === 0, 'empty declared data inputs');
need(!/^\s*(?:import|from)\s+/m.test(source), 'no import statement spelling');
const binomial = (a,b) => { let v=1n; for(let j=1;j<=b;j++) v=v*BigInt(a-b+j)/BigInt(j); return Number(v); };
const parameterCounts = [];
for (let n=1;n<=6;n++) parameterCounts.push({n,carriers:5,states:binomial(n+4,4)});
const carriers = parameterCounts.reduce((s,x)=>s+x.carriers,0);
const states = parameterCounts.reduce((s,x)=>s+x.states,0);
const words = parameterCounts.filter(x=>x.n>=3).reduce((s,x)=>s+x.states*(2**x.n-2),0);
need(carriers === 30 && states === 461 && words === 17990, 'combinatorial parameter counts only');
const main = textOf(PAPER + '/main.tex');
const includes = [...main.matchAll(/\\input\{([^}]+)\}/g)].map(m=>m[1]);
need(equal(includes,['math_commands','sections/00_abstract','sections/01_introduction','sections/02_temporal','sections/03_inverse','sections/04_fibres','sections/05_verification']), 'exact local TeX include order');
const texPaths = PAPER_FILES.filter(p=>p.endsWith('.tex'));
const tex = texPaths.map(textOf).join('\n');
const labels = [...tex.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
need(labels.length === new Set(labels).size, 'unique TeX labels as text');
for(const match of tex.matchAll(/\\(?:eqref|ref)\{([^}]+)\}/g)) need(labels.includes(match[1]),'resolved local TeX label');
const bibKeys = [...textOf(PAPER+'/references.bib').matchAll(/^@article\{([^,]+),/gm)].map(m=>m[1]).sort();
const citeKeys = [...new Set([...tex.matchAll(/\\cite\{([^}]+)\}/g)].flatMap(m=>m[1].split(',')))].sort();
need(equal(bibKeys,citeKeys) && bibKeys.length===3, 'three exact bibliography/citation keys, not metadata re-verification');
for (const rel of ALL) need(equal(read(rel).key,before.get(rel).key), 'unchanged complete document endpoints: '+rel);
need(equal(listPaper(PAPER),PAPER_FILES), 'unchanged paper inventory endpoint');
console.log(JSON.stringify({schema:'p213-independent-source-document-inventory-v1',status:'DOCUMENTARY_PASS_NOT_SCIENCE_OR_RUNTIME',checks,source_executed:false,source_ast_or_syntax_parsed:false,whole_input_count:ALL.length,paper_payloads:29,paper_files:30,paper_bytes:PAPER_FILES.reduce((s,p)=>s+before.get(p).key.bytes,0),metadata_fields:FIELDS,parameter_counts_only:parameterCounts,derived_transport_counts:{carriers,states,words,total_lines:words+states+carriers+4,not_observed_output:true},keys:ALL.map(p=>before.get(p).key)}));
