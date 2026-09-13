// Read-only final preservation check. No writes, network, subprocess, or inference of science PASS.
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const sha = x => crypto.createHash('sha256').update(x).digest('hex');
const receiptPath = 'BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_RESUMPTION_RECEIPT.json';
const lockPath = 'BATCH_ROUND10_STAGE4_5_ROUND4_INPUT_LOCK.json';
const receipt = JSON.parse(fs.readFileSync(receiptPath, 'utf8'));
const lock = JSON.parse(fs.readFileSync(lockPath, 'utf8'));
function observe(p) {
  if (path.isAbsolute(p) || p.split('/').some(x => !x || x === '.' || x === '..')) throw Error('Noncanonical path: ' + p);
  let loc = '.';
  for (const part of p.split('/')) { loc = path.join(loc, part); if (fs.lstatSync(loc).isSymbolicLink()) throw Error('Symlink: ' + p); }
  if (!fs.statSync(p).isFile()) throw Error('Not regular file: ' + p);
  const raw = fs.readFileSync(p); return {path:p, bytes:raw.length, sha256:sha(raw)};
}
function walk(dir) {
  const rows = [];
  for (const name of fs.readdirSync(dir).sort()) {
    const p = dir + '/' + name, st = fs.lstatSync(p);
    if (st.isSymbolicLink()) throw Error('Symlink: ' + p);
    if (st.isDirectory()) rows.push(...walk(p)); else rows.push(observe(p));
  }
  return rows;
}
const mismatches = [], checked = [];
for (const before of receipt.preservation.existing_inventory) {
  try {
    const actual = observe(before.path); checked.push(actual);
    if (actual.sha256 !== before.sha256 || actual.bytes !== before.bytes) mismatches.push({before, actual});
  } catch (e) { mismatches.push({before, error:e.message}); }
}
const science = lock.protected_science_trees.map(t => {
  const actual = walk(t.path), before = t.files;
  const unchanged = actual.length === before.length && actual.every((x,i) => ['path','bytes','sha256'].every(k => x[k] === before[i][k]));
  if (!unchanged) mismatches.push({science_tree:t.path, before, actual});
  return {paper_id:t.paper_id, path:t.path, unchanged, files:actual};
});
const auditPaths = fs.readdirSync('.').filter(n => n.startsWith('BATCH_ROUND10_STAGE4_5_ROUND4_'));
for (const paper of lock.papers) {
  const dir = 'papers/' + paper.paper_slug + '/notes';
  for (const n of fs.readdirSync(dir)) if (n.startsWith('stage4_5_round4_')) auditPaths.push(dir + '/' + n);
}
const inventory = auditPaths.sort().map(observe);
const beforePaths = new Set(receipt.preservation.existing_inventory.map(x => x.path));
const newlyPresent = inventory.filter(x => !beforePaths.has(x.path));
const allowed = p => p.startsWith('BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_') || p.startsWith('papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round4_recovery3_');
for (const item of newlyPresent) if (!allowed(item.path)) mismatches.push({unexpected_new_round4_path:item.path});
console.log(JSON.stringify({status:mismatches.length?'FAIL':'PASS', observed_at:new Date().toISOString(),
  scope:'1301 Recovery3-frozen files and 15 protected scientific trees; current audit-prefix inventory; not a whole-filesystem write monitor.',
  baseline_receipt:observe(receiptPath), input_lock:observe(lockPath), checker:observe('BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_preservation_check.js'),
  protected_file_count:checked.length, science_tree_count:science.length, mismatches, science_trees:science,
  audit_inventory:inventory, new_since_recovery3:newlyPresent,
  output_self_excluded:'BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY3_FINAL_PRESERVATION.json is written after this observation and cannot contain its own digest.',
  no_scientific_execution_or_stage5_or6:true}));
process.exitCode = mismatches.length ? 1 : 0;
