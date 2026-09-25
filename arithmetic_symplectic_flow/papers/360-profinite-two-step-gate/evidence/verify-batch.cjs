// Mechanical integrity/link audit, not a mathematical or numerical experiment.
// Run from arithmetic_symplectic_flow:
// node papers/360-profinite-two-step-gate/evidence/verify-batch.cjs --brief
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const sha = x => crypto.createHash('sha256').update(x).digest('hex');
const read = f => fs.readFileSync(f, 'utf8');
const assert = (ok, msg) => { if (!ok) throw Error(msg); };
const files = dir => fs.readdirSync(dir, {withFileTypes:true}).flatMap(e => {
  const f = path.join(dir,e.name); return e.isDirectory() ? files(f) : [f];
}).sort();
const old = [
  ['348-reeb-contact-refinement',11,'5255ca400be05283270cc95553d041004469a866853a26e260f25a3f0d9cc0d6'],
  ['349-reeb-orbit-zeta',10,'7607376f515dd6bc628e4c326baae68fe772d086ca14102e5a5256d686a4988f'],
  ['350-transverse-graded-trace',9,'323cadfaf5876726cc9c4790899c3183cdf63c7922b3c3f43fe6b34dfa877656'],
  ['351-contact-differential-complex',8,'59c2349a409b10897f899fd1b2f37931d758fbeb666cdc8263871e8b9097d97a'],
  ['352-contact-order-cohomology',7,'d7acfaca74a292599fe8cfe168e169ea1131179c5228086ecf947fc92118a312'],
  ['353-arithmetic-clock-rigidity',7,'06e1c81c0a61548632cf158574af2b6bf5367ea09f8fa5343993fd8f6aab7312'],
  ['354-local-factor-refinement',7,'ff634f8dbd185fa471eedd028bfa33e5d3421e08ed3596a58020fb71ba529ef3'],
  ['355-affine-clock-covariance',11,'9c70ea10f6bce29e9e734dc660452575537125bbce7d32387a981d4a01b46658'],
  ['356-finite-module-feedback',7,'a7f2eba91de6029b9b2924ccf566ab48e12c8d9c20e2927a532b683dbb3492dd'],
  ['357-euclidean-energy-contact',7,'d9e7203e1e4216895c3d07d61bcca3da955f922ef77df39580c76d1e220cad25'],
  ['358-profinite-content-feedback',7,'d50eb33c5d6dafd14ceda9938abf90a30c2ef4b4f819de704eb5ee35a981694c'],
  ['359-finite-rank-clock-boundary',7,'3a38084ce4d31a2d662b6c623a87eba364cb3ec3c61fe072ffc390f8b40b72b6']
];
for (const [d,n,h] of old) {
  const base=path.join('papers',d), ff=files(base);
  const bundle=ff.map(f=>path.relative(base,f)+'\t'+sha(fs.readFileSync(f))+'\n').join('');
  assert(ff.length===n && sha(bundle)===h, 'Frozen package changed: '+d);
}
const anchors = [
  ['AGENTS.md','86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d'],
  ['plan.md','9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0'],
  ['docs/prior_work/README.md','d2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd'],
  ['papers/paper-template.md','ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b'],
  ['papers/283-nonlinear-residue-clock-screen/paper.md','50429784fc1f634da86aa6aae1aac1b0e109b7fcc82a6169a68bb80a5bf95d38']
];
for (const [f,h] of anchors) assert(sha(fs.readFileSync(f))===h, 'Anchor changed: '+f);
const overview = [
  ['readme.md','# Arithmetic Symplectic Flow\n\n> **Round 2 — Candidate Engineering / Structural Synthesis**\n','> **Preceding batch handoff (2026-09-21):','> **Current workflow state (2026-09-21):','b9bf8e9b0c6da8599673a9703a8f24917c7d9a9b8b52e031b7db328820f47441'],
  ['papers/README.md','# Markdown paper registry\n\n','**Preceding batch handoff (2026-09-21):','**Current workflow state (2026-09-21):','72ffe34d0a6d9dc87735070cb9aa8acd3988b7c800dfd71576c93009afc01b02']
];
const packages = [
  ['360-profinite-two-step-gate','ANG-AUDIT-20260921-PC2A01','TWO-STEP WINDOW EMPTY; MAIN T2 OPEN — FORK',[[109,'63d8db64fcc242cdf38515197a9379849ddba64fda0c34aff1e40a141272cde8']]],
  ['361-matrix-arithmetic-action','ANG-20260921-MAA01','OWNED MATRIX CLOCK; PAIRED PACKET MULTIPLICITY — STOP / FORK',[[111,'2bad5e774342c181007959ec127cff22192375c7fcb7fb618f5c8a0c064940c7'],[118,'67cbafaf771cbc6ae3849d21f8a13165ea9eb24863a98ded81fa49a66d0ab2f4']]],
  ['362-variable-multiplier-admission','ANG-SCREEN-20260921-VMA01','NONSINGULARITY AND COUNTABLE ATLAS FAIL — SCOPED STOP / FORK',[[93,'0755f26b9b18287cca9f0a0c6ab4ad42e0e3c56703e4011389abe43d8bb9cba8']]],
  ['363-reversible-uniform-clock-gate','ANG-AUDIT-20260921-RUI01','ZERO UNIFORM-IMAGE CLOCK — CLASS FILTER ESTABLISHED',[[109,'7fde5b7afe594d08449debe5fac23a88ee8771fcf03dd8b543afa4a7213511fa'],[116,'3db55fb8bbb9b89882c54ba893f06232dd6977aadcd5370be725cc932baed568']]],
  ['364-symbolic-index-branching-gate','ANG-AUDIT-20260921-SIB01','BRANCHING / ESCAPE CRITERION ESTABLISHED — CONDITIONAL FILTER',[[113,'ea095eca49dbaa720f1b6973ee25f7005c6184dc83babaf27105e3a53ea99e98']]]
];
let markdown=0, links=0, frozenPrefixes=0;
const inputs=[];
function checkLinks(s,f) {
  for (const m of s.matchAll(/\]\(([^)]+)\)/g)) {
    const target=m[1].split('#')[0];
    if(target && !/^(https?:|mailto:)/.test(target)) {
      assert(fs.existsSync(path.resolve(path.dirname(f),target)), 'Broken link '+f+' -> '+target); links++;
    }
  }
}
for (const [d,id,status,freezes] of packages) {
  const base=path.join('papers',d);
  assert(files(base).every(f=>f.endsWith('.md')||f.endsWith('/evidence/verify-batch.cjs')),
    'Unexpected non-Markdown artifact '+d);
  for (const f of files(base).filter(f=>f.endsWith('.md'))) {
    const s=read(f); markdown++;
    assert(s.endsWith('\n') && (s.match(/^```/gm)||[]).length%2===0,'Markdown format '+f);
    checkLinks(s,f); inputs.push({file:f,lines:s.split('\n').length-1,sha256:sha(s)});
  }
  for (const name of ['candidate-card.md','paper.md','README.md','claim-ledger.md']) {
    const s=read(path.join(base,name)); assert(s.includes(id)&&s.includes(status),'ID/status '+d+'/'+name);
  }
  const card=read(path.join(base,'candidate-card.md'));
  for (const [n,h] of freezes) {
    assert(sha(card.split('\n').slice(0,n).join('\n')+'\n')===h,'Frozen prefix '+d+' '+n); frozenPrefixes++;
  }
}
for (const [f,prefix,marker,oldMarker,h] of overview) {
  const s=read(f), i=s.indexOf(marker); assert(i>=0,'Archive marker '+f);
  assert(sha(prefix+s.slice(i).replace(marker,oldMarker))===h,'Overview archive '+f);
  checkLinks(s.slice(0,i),f);
}
console.log(JSON.stringify({result:'PASS',packages:packages.length,identitySurfaces:20,markdown,
  relativeLinks:links,frozenPrefixes,preservedPackages:old.length,preservedAnchors:anchors.length,
  preservedOverviewArchives:overview.length,inputs:process.argv.includes('--brief')?undefined:inputs},null,2));
