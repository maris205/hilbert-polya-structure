// Read-only scoped preservation check; JSON stdout only. No network or mutations.
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const sha = x => crypto.createHash('sha256').update(x).digest('hex');
const receiptPath = 'BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY2_RESUMPTION_RECEIPT.json';
const lockPath = 'BATCH_ROUND10_STAGE4_5_ROUND4_INPUT_LOCK.json';
const receipt = JSON.parse(fs.readFileSync(receiptPath, 'utf8'));
const lock = JSON.parse(fs.readFileSync(lockPath, 'utf8'));
function observe(p) {
  if (path.isAbsolute(p) || p.split('/').some(x => !x || x === '.' || x === '..')) throw Error('Noncanonical path: ' + p);
  let loc = '.';
  for (const part of p.split('/')) { loc = path.join(loc, part); if (fs.lstatSync(loc).isSymbolicLink()) throw Error('Symlink: ' + p); }
  if (!fs.statSync(p).isFile()) throw Error('Not regular file: ' + p);
  const b = fs.readFileSync(p); return {path:p,bytes:b.length,sha256:sha(b)};
}
const mismatches = [], checked = [];
for (const before of receipt.preservation.existing_inventory) {
  try { const actual = observe(before.path); checked.push(actual);
    if (actual.sha256 !== before.sha256 || actual.bytes !== before.bytes) mismatches.push({before,actual});
  } catch (e) { mismatches.push({before,error:e.message}); }
}
function walk(dir) {
  const found = [];
  for (const name of fs.readdirSync(dir).sort()) { const p = dir + '/' + name, st = fs.lstatSync(p);
    if (st.isSymbolicLink()) throw Error('Symlink: ' + p);
    if (st.isDirectory()) found.push(...walk(p)); else found.push(observe(p));
  } return found;
}
const science = lock.protected_science_trees.map(t => {
  const actual = walk(t.path), before = t.files;
  const unchanged = actual.length === before.length && actual.every((x,i) => ['path','bytes','sha256'].every(k => x[k] === before[i][k]));
  if (!unchanged) mismatches.push({science_tree:t.path,before,actual});
  return {paper_id:t.paper_id,path:t.path,unchanged,files:actual};
});
const auditPaths = fs.readdirSync('.').filter(n=>n.startsWith('BATCH_ROUND10_STAGE4_5_ROUND4_')).map(n=>n);
for (const p of lock.papers) {
  const notes = 'papers/' + p.paper_slug + '/notes';
  for (const n of fs.readdirSync(notes)) if(n.startsWith('stage4_5_round4_')) auditPaths.push(notes+'/'+n);
}
const inventory = auditPaths.sort().map(observe);
const old = new Set(receipt.preservation.existing_inventory.map(x=>x.path));
console.log(JSON.stringify({status:mismatches.length?'FAIL':'PASS',scope:'1168 Recovery2 frozen files and15 scientific trees; exact current audit inventory, excluding this yet-unwritten output receipt to avoid a self-hash cycle.',observed_at:new Date().toISOString(),baseline_receipt:observe(receiptPath),input_lock:observe(lockPath),protected_file_count:checked.length,science_tree_count:science.length,mismatches,science_trees:science,audit_inventory:inventory,new_since_recovery2:inventory.filter(x=>!old.has(x.path)),current_manuscript_changed:false,scientific_execution:false,no_stage5_or6:true}));
process.exitCode = mismatches.length ? 1 : 0;

