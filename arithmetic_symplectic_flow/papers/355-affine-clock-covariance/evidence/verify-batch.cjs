// Mechanical Markdown/identity/preservation audit, not a mathematical experiment.
// Run from arithmetic_symplectic_flow: node papers/355-affine-clock-covariance/evidence/verify-batch.cjs
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const hash = x => crypto.createHash('sha256').update(x).digest('hex');
function files(dir) {
  return fs.readdirSync(dir, {withFileTypes: true}).flatMap(e => {
    const p = path.join(dir, e.name);
    return e.isDirectory() ? files(p) : [p];
  }).sort();
}
function assert(ok, message) { if (!ok) throw Error(message); }
const preserved = [
  ['348-reeb-contact-refinement', 11, '5255ca400be05283270cc95553d041004469a866853a26e260f25a3f0d9cc0d6'],
  ['349-reeb-orbit-zeta', 10, '7607376f515dd6bc628e4c326baae68fe772d086ca14102e5a5256d686a4988f'],
  ['350-transverse-graded-trace', 9, '323cadfaf5876726cc9c4790899c3183cdf63c7922b3c3f43fe6b34dfa877656'],
  ['351-contact-differential-complex', 8, '59c2349a409b10897f899fd1b2f37931d758fbeb666cdc8263871e8b9097d97a'],
  ['352-contact-order-cohomology', 7, 'd7acfaca74a292599fe8cfe168e169ea1131179c5228086ecf947fc92118a312'],
  ['353-arithmetic-clock-rigidity', 7, '06e1c81c0a61548632cf158574af2b6bf5367ea09f8fa5343993fd8f6aab7312'],
  ['354-local-factor-refinement', 7, 'ff634f8dbd185fa471eedd028bfa33e5d3421e08ed3596a58020fb71ba529ef3']
];
const anchors = [
  ['AGENTS.md', '86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d'],
  ['plan.md', '9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0'],
  ['docs/prior_work/README.md', 'd2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd'],
  ['papers/paper-template.md', 'ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b']
];
for (const [dir, count, expected] of preserved) {
  const base = path.join('papers', dir), ff = files(base);
  const bundle = ff.map(f => path.relative(base, f)+'\t'+hash(fs.readFileSync(f))+'\n').join('');
  assert(ff.length === count && hash(bundle) === expected, 'Changed frozen package '+dir);
}
for (const [f, expected] of anchors) assert(hash(fs.readFileSync(f)) === expected, 'Changed anchor '+f);
const overviews = [
  ['readme.md', '# Arithmetic Symplectic Flow\n\n> **Round 2 — Candidate Engineering / Structural Synthesis**\n', '> **Preceding batch handoff (2026-09-21):', '> **Current workflow state (2026-09-21):', '89063e315db0947383302d5672e22994dfc10188a163a0f8f6959a1a9fd42d78'],
  ['papers/README.md', '# Markdown paper registry\n\n', '**Preceding batch handoff (2026-09-21):', '**Current workflow state (2026-09-21):', '40d581f7ab6c25a655fd40ec03dcd90d16e80d2a93b3a3c1d9e6b8167acd63b3']
];
for (const [f, prefix, marker, oldMarker, expected] of overviews) {
  const s = fs.readFileSync(f, 'utf8'), i = s.indexOf(marker);
  assert(i >= 0, 'Missing archive boundary '+f);
  assert(hash(prefix+s.slice(i).replace(marker, oldMarker)) === expected, 'Changed overview archive '+f);
}
const packages = [
  ['355-affine-clock-covariance', 'ANG-AUDIT-20260921-ACC01', 'CONDITIONAL AFFINE RIGIDITY; EXECUTOR ORIGIN NOT ESTABLISHED', 131, '2c035f026cb0b9ab67933d0c7a132b7a611045d379e87d31cd8a583f66291ed4'],
  ['356-finite-module-feedback', 'ANG-20260921-FMK01', 'OWNED MODULE-PATH CLOCK; COMPOSITE PRIMITIVES — STOP / FORK', 146, 'ad9619f06da6b7ecff7505d0e8d6210c52f291007f4d1c22e35186359757a449'],
  ['357-euclidean-energy-contact', 'ANG-20260921-EEC01', 'OWNED COVER REEB / QUOTIENT-SET TIME; WRONG PRIMITIVE — STOP / FORK', 115, '435fa4906a0790fdb64cdd4141268e9290bde67eda576128fe83f0ad7e021333'],
  ['358-profinite-content-feedback', 'ANG-20260921-PCF01', 'OWNED HAAR CONTENT CLOCK; BOUNDED FIXED-POINT TESTS NEGATIVE; T2 OPEN', 114, '70f0f0eedde02f5cf6daace6161f74534fd8c31a788533f9bf18e9aff87a0224'],
  ['359-finite-rank-clock-boundary', 'ANG-AUDIT-20260921-FRC01', 'FINITE-RANK PRIME-RETURN BOUND ESTABLISHED; CONDITIONAL FILTER ONLY', 116, '1054a232c9d6c7e27f60a9f9bbfc4dd3a3822f1ca9da5ceaeb3b0444c1a9c374']
];
let links = 0, markdown = 0;
const inputs = [];
for (const [dir, id, status, frozenLines, frozenHash] of packages) {
  const base = path.join('papers', dir);
  for (const f of files(base).filter(f => f.endsWith('.md'))) {
    const s = fs.readFileSync(f, 'utf8'); markdown++;
    assert(s.endsWith('\n') && (s.match(/^```/gm)||[]).length % 2 === 0, 'Format '+f);
    for (const m of s.matchAll(/\]\(([^)]+)\)/g)) {
      const target = m[1].split('#')[0];
      if (target && !/^(https?:|mailto:)/.test(target)) {
        assert(fs.existsSync(path.resolve(path.dirname(f), target)), 'Broken link '+f+' '+target); links++;
      }
    }
    inputs.push({file: f, lines: s.split('\n').length-1, sha256: hash(s)});
  }
  for (const f of ['candidate-card.md', 'paper.md', 'README.md', 'claim-ledger.md']) {
    const s = fs.readFileSync(path.join(base, f), 'utf8');
    assert(s.includes(id) && s.includes(status), 'Identity/status '+dir+'/'+f);
  }
  const card = fs.readFileSync(path.join(base, 'candidate-card.md'), 'utf8');
  assert(hash(card.split('\n').slice(0, frozenLines).join('\n')+'\n') === frozenHash, 'Changed P0 '+dir);
}
for (const [f, prefix, marker] of overviews) {
  const s = fs.readFileSync(f, 'utf8').split(marker)[0];
  for (const m of s.matchAll(/\]\(([^)]+)\)/g)) {
    const target = m[1].split('#')[0];
    if (target && !/^(https?:|mailto:)/.test(target)) {
      assert(fs.existsSync(path.resolve(path.dirname(f), target)), 'Overview link '+f+' '+target); links++;
    }
  }
}
console.log(JSON.stringify({result:'PASS',packages:packages.length,markdown,relativeLinks:links,
  preservedPackages:preserved.length,preservedAnchors:anchors.length,preservedOverviewArchives:overviews.length,
  inputs:process.argv.includes('--brief') ? undefined : inputs}, null, 2));
