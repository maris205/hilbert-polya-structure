// READ-ONLY mechanical integrity/link audit; not mathematical proof or numerics.
// Run from arithmetic_symplectic_flow (no files are written):
// node papers/370-divisor-renewal-clock/evidence/verify-batch.cjs --brief
// --pre-handoff reports pending final artifacts/checks; it NEVER returns PASS.
'use strict';
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const args = new Set(process.argv.slice(2));
for (const arg of args) {
  if (!['--brief', '--pre-handoff'].includes(arg)) throw Error('Unknown option: ' + arg);
}
const preHandoff = args.has('--pre-handoff');
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const read = file => fs.readFileSync(file, 'utf8');
const assert = (ok, message) => { if (!ok) throw Error(message); };
const pending = new Set();
const files = directory => fs.readdirSync(directory, {withFileTypes: true})
  .flatMap(entry => {
    const file = path.join(directory, entry.name);
    assert(!entry.isSymbolicLink(), 'Unexpected symlink: ' + file);
    return entry.isDirectory() ? files(file) : [file];
  }).sort();
const batchLogPath = 'papers/370-divisor-renewal-clock/batch-log.md';
const batchLog = read(batchLogPath);
const extractAnchors = (source, pattern, expected, label) => {
  const block = source.match(pattern);
  assert(block, 'Missing anchor block: ' + label);
  const rows = [...block[1].matchAll(/\['([^']+)',(\d+),'([a-f0-9]{64})'\]/g)]
    .map(match => [match[1], Number(match[2]), match[3]]);
  assert(rows.length === expected, 'Anchor count: ' + label);
  return rows;
};
// Read anchor literals as data. Never require/eval/run an archived verifier.
const old = extractAnchors(
  read('papers/360-profinite-two-step-gate/evidence/verify-batch.cjs'),
  /const old = (\[[\s\S]*?\n\]);/, 12, '348–359');
old.push(...extractAnchors(
  read('papers/365-divisibility-scheduled-radix/evidence/verify-batch.cjs'),
  /old\.push\(([\s\S]*?)\n\);/, 5, '360–364'));
const opening = [
  ['365-divisibility-scheduled-radix',11,'a3e4eea16876deb2531b3d15df9802409ef44a58dde39bee65da1fd3c234afa4'],
  ['366-local-visit-memory',7,'08066c5e4b5ab15969a8dd1fdcc85f88b81905ca67c6c5a7338c5cf3e0fad734'],
  ['367-global-coprime-memory',7,'4997471c76503fcf5567f3ef3f5701df02f618c37cd3606b5108d13019c02335'],
  ['368-atomic-memory-clock',7,'b5ac51037b941dbfdd6cd1c17c33b2ca5a24f20daae3c3e8f3e26b37ddd0ccfb'],
  ['369-finite-write-memory-clock',7,'92e8a1d8c0772b4a99915c28e3944194871697ef94d6672b9ac5bec167073f21']
];
const openingRows = [...batchLog.matchAll(/^\| (36[5-9]) \| (\d+) \| `([a-f0-9]{64})` \|$/gm)];
assert(openingRows.length === 5, 'Five opening bundle receipts required');
for (const [directory, count, hash] of opening) {
  const matches = openingRows.filter(row => row[1] === directory.slice(0, 3));
  assert(matches.length === 1 && Number(matches[0][2]) === count && matches[0][3] === hash,
    'Opening receipt changed: ' + directory);
  old.push([directory, count, hash]);
}
assert(old.length === 22 && new Set(old.map(row => row[0])).size === 22,
  'Unique old348–369 packages required');
for (const [directory, count, hash] of old) {
  const base = path.join('papers', directory), listed = files(base);
  const bundle = listed.map(file => path.relative(base, file) + '\t' +
    sha(fs.readFileSync(file)) + '\n').join('');
  assert(listed.length === count && sha(bundle) === hash, 'Frozen bundle changed: ' + directory);
}
const anchors = [
  ['AGENTS.md','86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d'],
  ['plan.md','9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0'],
  ['docs/prior_work/README.md','d2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd'],
  ['papers/paper-template.md','ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b'],
  ['papers/283-nonlinear-residue-clock-screen/paper.md','50429784fc1f634da86aa6aae1aac1b0e109b7fcc82a6169a68bb80a5bf95d38']
];
for (const [file, hash] of anchors) {
  assert(sha(fs.readFileSync(file)) === hash, 'Immutable anchor changed: ' + file);
}
const packages = [
  ['370-divisor-renewal-clock','ANG-20260922-DRE01',[
    [100,'46e18a3aa59d3eebfc744cf858c4b5ca516327d93124281bf47e4cfa2b5a3b08'],
    [112,'f4a1a914d117365671d88e946d75061d525b2065cf6080b88be22a3cc0cc7e8c']]],
  ['371-random-lookback-coprime','ANG-20260922-RLC01',[
    [94,'3f11f7cd57dbf8717d0d8e2db29f7bf32bc76b2fd4267592633563aa00e3c037']]],
  ['372-arithmetic-mixture-version','ANG-SCREEN-20260922-AMV01',[
    [89,'2a68f215f31c8cbe16c1f32511c19d0a3c0d5eff7390b9776e270305c3092a37'],
    [98,'0a13ed2c9e66084f1cc856c20a299aa7830cceb6bfd4ee401d1ddf5384cdf07b']]],
  ['373-global-divisor-reindex','ANG-20260922-GDR01',[
    [86,'29b2759103d3c1024e76c4109d5a8bf2b0a70fe20366d4e8410e57558d593cae']]],
  ['374-hard-coprime-history-control','ANG-CONTROL-20260922-HCH01',[
    [88,'d970a8ed78a30f2bd70323c88b322ecdfe7d4b5abdd5b2490d029e4fb82755bd']]]
];
const surfaces = ['candidate-card.md', 'paper.md', 'README.md', 'claim-ledger.md'];
const requiredEvidence = ['scope-review.md', 'independent-proof.md', 'review.md'];
const required = packages.flatMap(([directory]) => [
  ...surfaces.map(name => path.join('papers', directory, name)),
  ...requiredEvidence.map(name => path.join('papers', directory, 'evidence', name))
]);
required.push(batchLogPath,
  'papers/370-divisor-renewal-clock/batch-summary.md',
  'papers/370-divisor-renewal-clock/evidence/verification.md');
const planned = new Set(required.map(file => path.resolve(file)));
for (const file of required) {
  if (preHandoff && !fs.existsSync(file)) pending.add('Missing final artifact: ' + file);
  else assert(fs.existsSync(file), 'Required final artifact missing: ' + file);
}
let markdown = 0, links = 0, frozenPrefixes = 0, identitySurfaces = 0;
let boundEvidenceReceipts = 0, boundSurfaceReceipts = 0, preservedOverviewArchives = 0;
const inputs = [];
function markdownBody(source, file) {
  assert(source.endsWith('\n') && !source.includes('\r'), 'LF/final newline: ' + file);
  let fence = null;
  const body = source.split('\n').map(line => {
    if (fence) {
      const close = line.match(/^ {0,3}(`{3,}|~{3,})\s*$/);
      if (close && close[1][0] === fence[0] && close[1].length >= fence.length) fence = null;
      return '';
    }
    const open = line.match(/^ {0,3}(`{3,}|~{3,})/);
    if (open) { fence = open[1]; return ''; }
    return line;
  }).join('\n');
  assert(fence === null, 'Unclosed Markdown fence: ' + file);
  return body;
}
function checkDestination(destination, file) {
  const target = destination.replace(/^<|>$/g, '').split('#')[0];
  if (!target || /^[a-z][a-z0-9+.-]*:/i.test(target) || target.startsWith('//')) return;
  const resolved = path.resolve(path.dirname(file), decodeURIComponent(target));
  if (preHandoff && !fs.existsSync(resolved) && planned.has(resolved)) {
    pending.add('Pending linked final artifact: ' + path.relative(process.cwd(), resolved));
    return;
  }
  assert(fs.existsSync(resolved), 'Broken local link: ' + file + ' -> ' + target);
  links++;
}
function checkMarkdown(source, file) {
  const body = markdownBody(source, file);
  // Inline destinations and reference definitions; no network/fragment validation.
  for (const match of body.matchAll(/\]\((<[^>\n]+>|[^\s)]+)(?:\s+["'][^\n]*?["'])?\)/g)) {
    checkDestination(match[1], file);
  }
  for (const match of body.matchAll(/^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)/gm)) {
    checkDestination(match[1], file);
  }
}
for (const [directory, id, freezes] of packages) {
  const base = path.join('papers', directory), listed = files(base);
  assert(listed.every(file => file.endsWith('.md') ||
    file === 'papers/370-divisor-renewal-clock/evidence/verify-batch.cjs'),
  'Unexpected non-Markdown artifact: ' + directory);
  for (const file of listed.filter(file => file.endsWith('.md'))) {
    const source = read(file);
    checkMarkdown(source, file);
    markdown++;
    inputs.push({file, lines: source.split('\n').length - 1, sha256: sha(source)});
  }
  const card = read(path.join(base, 'candidate-card.md'));
  for (const [count, hash] of freezes) {
    assert(sha(card.split('\n').slice(0, count).join('\n') + '\n') === hash,
      'Frozen card prefix changed: ' + directory + '/' + count);
    frozenPrefixes++;
  }
  for (const name of surfaces) {
    const file = path.join(base, name);
    if (preHandoff && !fs.existsSync(file)) continue;
    const source = read(file);
    assert(source.includes(id), 'Candidate ID missing: ' + file);
    // Frozen cards keep historical OPEN; only the appended outcome owns final status.
    const statusSurface = name === 'candidate-card.md'
      ? source.split('\n').slice(Math.max(...freezes.map(row => row[0]))).join('\n')
      : source.split('\n').slice(0, 20).join('\n');
    const statusOK = name === 'paper.md' ? /\bSTOP\b/.test(statusSurface)
      : /STOP\s*\/\s*FORK/.test(statusSurface);
    if (preHandoff && !statusOK) pending.add('Final STOP status not yet appended: ' + file);
    else assert(statusOK, 'Final STOP status missing: ' + file);
    if (statusOK) identitySurfaces++;
  }
}
const receiptRows = [...batchLog.matchAll(/^\| (37[0-4]) \| `([a-f0-9]{64})` \| `([a-f0-9]{64})` \|$/gm)];
assert(new Set(receiptRows.map(row => row[1])).size === receiptRows.length,
  'Duplicate final evidence receipt');
const receiptAliases = {
  'paper.md': /^\s*(?:[-*+]|\|)?\s*(?:\*\*)?Paper(?:\*\*)?(?=[,\s:|])/i,
  'candidate-card.md': /^\s*(?:[-*+]|\|)?\s*(?:\*\*)?Card(?:\*\*)?(?=[,\s:|])/i,
  'claim-ledger.md': /^\s*(?:[-*+]|\|)?\s*(?:\*\*)?(?:FINAL\s+)?ledger(?:\*\*)?(?=[,\s:|])/i,
  'README.md': /^\s*(?:[-*+]|\|)?\s*(?:\*\*)?README(?:\*\*)?(?=[,\s:|])/i
};
for (const [directory] of packages) {
  const row = receiptRows.find(match => match[1] === directory.slice(0, 3));
  if (preHandoff && !row) { pending.add('Final evidence receipt pending: ' + directory); continue; }
  assert(row, 'Missing final raw/review receipt: ' + directory);
  const base = path.join('papers', directory, 'evidence');
  const raw = path.join(base, 'independent-proof.md'), reviewFile = path.join(base, 'review.md');
  assert(fs.existsSync(raw) && fs.existsSync(reviewFile), 'Receipt without evidence files: ' + directory);
  assert(sha(fs.readFileSync(raw)) === row[2], 'Independent proof receipt mismatch: ' + directory);
  const review = read(reviewFile);
  assert(sha(fs.readFileSync(reviewFile)) === row[3], 'Final review receipt mismatch: ' + directory);
  assert(/\bCP2\s+(?:\*\*)?PASS\b/.test(review) && /\bCP3\s+(?:\*\*)?PASS\b/.test(review),
    'Final CP2/CP3 PASS markers missing: ' + directory);
  const reviewLines = review.split('\n');
  for (const name of surfaces) {
    const hash = sha(fs.readFileSync(path.join('papers', directory, name)));
    // Clear aliases bind only one same-line hash, never a nearby historical hash.
    const aliasRows = reviewLines.filter(line => {
      const hashes = line.match(/\b[a-f0-9]{64}\b/g) || [];
      return receiptAliases[name].test(line) && hashes.length === 1 && hashes[0] === hash;
    });
    assert(aliasRows.length <= 1, 'Ambiguous aliased surface receipt: ' + directory + '/' + name);
    const bound = aliasRows.length === 1 || reviewLines.some((line, index) => {
      if (!line.includes(name)) return false;
      if (line.includes(hash)) return true;
      if (surfaces.some(other => other !== name && line.includes(other))) return false;
      // Accommodate a wrapped hash; do not cross another named surface receipt.
      for (const next of reviewLines.slice(index + 1, index + 3)) {
        if (surfaces.some(other => next.includes(other))) break;
        if (next.includes(hash)) return true;
      }
      return false;
    });
    assert(bound,
      'Reviewed final-surface receipt mismatch: ' + directory + '/' + name);
    boundSurfaceReceipts++;
  }
  boundEvidenceReceipts += 2;
}
const overview = [
  ['readme.md','# Arithmetic Symplectic Flow\n\n> **Round 2 — Candidate Engineering / Structural Synthesis**\n',
    '> **Preceding batch handoff (2026-09-21): LONG-MEMORY',
    '> **Current workflow state (2026-09-21): LONG-MEMORY',
    '6fab239265a177fdaf5a1f0e27174b6511e724eac1d08dd8ffabeb35237fdc9b'],
  ['papers/README.md','# Markdown paper registry\n\n',
    '**Preceding batch handoff (2026-09-21): Long-memory',
    '**Current workflow state (2026-09-21): Long-memory',
    '8dacc66e16b32181244d04ad146c5ccf77293fb155b39d2baddee95378197fda']
];
for (const [file, prefix, marker, originalMarker, hash] of overview) {
  const source = read(file), index = source.indexOf(marker);
  if (preHandoff && sha(fs.readFileSync(file)) === hash) {
    pending.add('New overview handoff not yet prepended: ' + file);
    continue;
  }
  assert(index >= 0, 'Old overview archive marker missing: ' + file);
  assert(sha(prefix + source.slice(index).replace(marker, originalMarker)) === hash,
    'Old overview archive changed: ' + file);
  const current = source.slice(0, index);
  assert(current.includes('2026-09-22') && current.includes('5/5'),
    'Current five-round overview marker missing: ' + file);
  for (const [directory] of packages) {
    assert(current.includes(directory + '/README.md'), 'Current overview package missing: ' + file + '/' + directory);
  }
  checkMarkdown(current, file);
  preservedOverviewArchives++;
}
if (preHandoff) pending.add('Pre-handoff mode: rerun without --pre-handoff for final handoff');
else {
  assert(identitySurfaces === 20 && boundEvidenceReceipts === 10 && boundSurfaceReceipts === 20 &&
    preservedOverviewArchives === 2 && pending.size === 0, 'Incomplete strict handoff');
}
console.log(JSON.stringify({
  result: preHandoff ? 'PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL' : 'PASS',
  scope: 'Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.',
  packages: packages.length, identitySurfaces, markdown, relativeLinks: links,
  frozenPrefixes, preservedPackages: old.length, preservedAnchors: anchors.length,
  preservedOverviewArchives, boundEvidenceReceipts, boundSurfaceReceipts,
  pending: [...pending], inputs: args.has('--brief') ? undefined : inputs
}, null, 2));
// EOF — all operations above read local files or write the result to stdout only.
