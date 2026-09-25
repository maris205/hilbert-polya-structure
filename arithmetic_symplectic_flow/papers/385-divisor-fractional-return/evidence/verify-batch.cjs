// READ-ONLY mechanical integrity/link audit; not mathematical proof or numerics.
// Run from arithmetic_symplectic_flow (no files are written):
// node papers/385-divisor-fractional-return/evidence/verify-batch.cjs --brief
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
const batchLogPath = 'papers/385-divisor-fractional-return/batch-log.md';
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
old.push(...extractAnchors(
  read('papers/370-divisor-renewal-clock/evidence/verify-batch.cjs'),
  /const opening = (\[[\s\S]*?\n\]);/, 5, '365–369'));
old.push(...extractAnchors(
  read('papers/375-odd-distance-coprime-measure/evidence/verify-batch.cjs'),
  /const opening = (\[[\s\S]*?\n\]);/, 5, '370–374'));
old.push(...extractAnchors(
  read('papers/380-factor-allocation-history/evidence/verify-batch.cjs'),
  /const opening = (\[[\s\S]*?\n\]);/, 5, '375–379'));
const opening = [
  ['380-factor-allocation-history',11,'bbbcf85d6dbc77bac1e5850f2540a7c0407283a06cf0379227e006c338c28186'],
  ['381-coprime-exchange-heap',7,'6c8c1dd77ba77b3d80b7bfbef02106a87e3d3a522a62570d920ee92a80374813'],
  ['382-divisor-prefix-recurrence',7,'f06758f33fce925ef2c7cce79ee6e6507704dccc515d40ef924ccb5e1442f223'],
  ['383-bilateral-atomic-cut-control',7,'6b04f783b17923ebf3fc7eab1e0214529440454a003eb19e0e497f632c934d44'],
  ['384-factor-clock-version-gate',7,'14252414d7022cb84416c7b4fbe68a9ba2d9b68c23a57da1cc28ff5584b6e30a']
];
const openingRows = [...batchLog.matchAll(/^\| (38[0-4]) \| (\d+) \| `([a-f0-9]{64})` \|$/gm)];
assert(openingRows.length === 5, 'Five opening bundle receipts required');
for (const [directory, count, hash] of opening) {
  const matches = openingRows.filter(row => row[1] === directory.slice(0, 3));
  assert(matches.length === 1 && Number(matches[0][2]) === count && matches[0][3] === hash,
    'Opening receipt changed: ' + directory);
  old.push([directory, count, hash]);
}
assert(old.length === 37 && new Set(old.map(row => row[0])).size === 37,
  'Unique old348–384 packages required');
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
  ['385-divisor-fractional-return','ANG-20260922-DFR01',[
    [60,'125b34c65c11d7bb9289054d432d62d130ce2830af212bb8b33fffab8c4dd862'],
    [71,'003b19a334ca5957a16c0e34ac7039a96f47c62cb6c8c9252376abf623f4e68a']]],
  ['386-content-reduced-reciprocal','ANG-20260922-CRR01',[
    [55,'172fe27af715c5a2acecd55abdd4c5953518628b2712b93eee01f0c80207891a'],
    [66,'61ed514128aa4a7660a8f60c30cab978bbd35fccd8d0d64f35689cf60af5f781']]],
  ['387-projective-multiplier-gate','ANG-AUDIT-20260922-PMG01',[
    [53,'12dc3aae227685796d83ae38a749b65fe775b8351447e7df2e0de92b55342b83']]],
  ['388-hard-gap-geometric-interface','ANG-SCREEN-20260922-HGI01',[
    [51,'56dd6b3e38d798dd1f401a15285535cbd84966c7967381c4f5b16ce5641b074e'],
    [59,'d3a25f5853d867e4d28cb8852a7d3f9602f226e154e8643e32ee6c808b131c06']]],
  ['389-coordinate-clock-ownership','ANG-AUDIT-20260922-CCG01',[
    [54,'d90790f1f22e80e8918722e8e5030f1d2994b014c0215c1869fd1f23588e6162'],
    [63,'19bee24c132e6e7c10c51825b0b934546bac5d811b25e23d2d4c37f6e1929633']]]
];
const surfaces = ['candidate-card.md', 'paper.md', 'README.md', 'claim-ledger.md'];
const requiredEvidence = ['scope-review.md', 'independent-proof.md', 'review.md'];
const required = packages.flatMap(([directory]) => [
  ...surfaces.map(name => path.join('papers', directory, name)),
  ...requiredEvidence.map(name => path.join('papers', directory, 'evidence', name))
]);
required.push(batchLogPath,
  'papers/385-divisor-fractional-return/batch-summary.md',
  'papers/385-divisor-fractional-return/evidence/verification.md');
const planned = new Set(required.map(file => path.resolve(file)));
for (const file of required) {
  if (preHandoff && !fs.existsSync(file)) pending.add('Missing final artifact: ' + file);
  else assert(fs.existsSync(file), 'Required final artifact missing: ' + file);
}
// Outcomes are root-recorded results, not a predetermined STOP/PASS expectation.
const outcomeRows = [...batchLog.matchAll(/^\| (38[5-9]) \| `outcome: ([^`\n]+)` \|$/gmi)];
assert(new Set(outcomeRows.map(row => row[1])).size === outcomeRows.length,
  'Duplicate final outcome receipt');
const normalizeOutcome = value => value.replace(/\*\*|`/g, '').trim()
  .replace(/[.。]$/, '').replace(/\s+/g, ' ');
const outcomes = new Map(outcomeRows.map(row => [row[1], normalizeOutcome(row[2])]));
let markdown = 0, links = 0, frozenPrefixes = 0, identitySurfaces = 0, statusSurfaces = 0;
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
    file === 'papers/385-divisor-fractional-return/evidence/verify-batch.cjs'),
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
  const outcome = outcomes.get(directory.slice(0, 3));
  if (preHandoff && !outcome) pending.add('Final outcome receipt pending: ' + directory);
  else assert(outcome, 'Missing final outcome receipt: ' + directory);
  for (const name of surfaces) {
    const file = path.join(base, name);
    if (preHandoff && !fs.existsSync(file)) continue;
    const source = read(file);
    assert(source.includes(id), 'Candidate ID missing: ' + file);
    identitySurfaces++;
    // Frozen cards keep historical OPEN; only the appended outcome owns final status.
    const statusSurface = name === 'candidate-card.md'
      ? source.split('\n').slice(Math.max(...freezes.map(row => row[0]))).join('\n')
      : source.split('\n').slice(0, 20).join('\n');
    const declared = statusSurface.split('\n')
      .map(line => normalizeOutcome(line).replace(/^>\s*/, ''))
      .map(line => line.match(/^(?:Final\s+)?Outcome:\s*(.+)$/i))
      .filter(Boolean).map(match => normalizeOutcome(match[1]));
    assert(declared.length <= 1, 'Ambiguous final Outcome field: ' + file);
    if (preHandoff && (!outcome || declared.length === 0)) {
      pending.add('Final Outcome field/receipt pending: ' + file);
    } else {
      assert(declared.length === 1 && declared[0] === outcome,
        'Final Outcome field disagrees with batch receipt: ' + file);
      statusSurfaces++;
    }
  }
}
const receiptRows = [...batchLog.matchAll(/^\| (38[5-9]) \| `([a-f0-9]{64})` \| `([a-f0-9]{64})` \| `([a-f0-9]{64})` \|$/gm)];
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
  assert(row, 'Missing final CP1/raw/review receipt: ' + directory);
  const base = path.join('papers', directory, 'evidence');
  const scope = path.join(base, 'scope-review.md'), raw = path.join(base, 'independent-proof.md');
  const reviewFile = path.join(base, 'review.md');
  assert([scope, raw, reviewFile].every(file => fs.existsSync(file)),
    'Receipt without evidence files: ' + directory);
  assert(sha(fs.readFileSync(scope)) === row[2], 'CP1 scope receipt mismatch: ' + directory);
  assert(sha(fs.readFileSync(raw)) === row[3], 'Independent proof receipt mismatch: ' + directory);
  const review = read(reviewFile);
  assert(sha(fs.readFileSync(reviewFile)) === row[4], 'Final review receipt mismatch: ' + directory);
  assert(/\bCP2\s*:?\s*(?:\*\*|`)?PASS\b/.test(review) && /\bCP3\s*:?\s*(?:\*\*|`)?PASS\b/.test(review),
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
  boundEvidenceReceipts += 3;
}
const overview = [
  ['readme.md','# Arithmetic Symplectic Flow\n\n> **Round 2 — Candidate Engineering / Structural Synthesis**\n',
    '> **Preceding batch handoff (2026-09-22): FULL-TRANSPORT',
    '> **Current workflow state (2026-09-22): FULL-TRANSPORT',
    'da65968393fa068932446e96a961fe7057c130a1d979d6f43e22e68585e2420e'],
  ['papers/README.md','# Markdown paper registry\n\n',
    '**Preceding batch handoff (2026-09-22): Full-transport',
    '**Current workflow state (2026-09-22): Full-transport',
    '1d2e383a938c43192187b76ed1e51f67fabdff2f46a4659b7b926d45f7fecd98']
];
for (const [file, prefix, marker, originalMarker, hash] of overview) {
  const source = read(file), index = source.indexOf(marker);
  checkMarkdown(source, file); // All overview links, including byte-preserved history.
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
  preservedOverviewArchives++;
}
if (preHandoff) pending.add('Pre-handoff mode: rerun without --pre-handoff for final handoff');
else {
  assert(identitySurfaces === 20 && statusSurfaces === 20 && outcomes.size === 5 &&
    boundEvidenceReceipts === 15 && boundSurfaceReceipts === 20 &&
    preservedOverviewArchives === 2 && pending.size === 0, 'Incomplete strict handoff');
}
console.log(JSON.stringify({
  result: preHandoff ? 'PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL' : 'PASS',
  scope: 'Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.',
  packages: packages.length, identitySurfaces, statusSurfaces, markdown, relativeLinks: links,
  frozenPrefixes, preservedPackages: old.length, preservedAnchors: anchors.length,
  preservedOverviewArchives, boundEvidenceReceipts, boundSurfaceReceipts,
  pending: [...pending], inputs: args.has('--brief') ? undefined : inputs
}, null, 2));
// EOF — all operations above read local files or write the result to stdout only.
