'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const cp = require('node:child_process');
const W = '/root/autodl-tmp/symbolic_dynamics';
const rel = p => W + '/' + p;
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
function need(x, m) { if (!x) throw Error(m); }
function rows(path) {
  return fs.readFileSync(rel(path), 'utf8').trim().split('\n').map(line => {
    const m = /^([0-9a-f]{64})  (.+)$/.exec(line); need(m, 'manifest row ' + path); return { hash: m[1], path: m[2] };
  });
}
function main() {
  const run = process.argv[2]; need(run === 'strict01' || run === 'strict02', 'run id');
  const grant = `docs/papers211_215_sequence/qa/p215_b_strict_preparation01/GRANT.${run}.json`;
  const out = `docs/papers211_215_sequence/qa/p215_b_strict_runs/${run}`;
  need(!fs.existsSync(rel(out)), 'output exists');
  const fixed = [
    'docs/papers211_215_sequence/reviews/p215_b/CANONICAL.txt',
    'docs/papers211_215_sequence/reviews/p215_b/SHA256SUMS',
    'docs/papers211_215_sequence/reviews/p215_b/INPUT_PINS.sha256',
    'docs/papers211_215_sequence/qa/p215_b_source_root02/INITIAL_RECEPTION.md',
    'docs/papers211_215_sequence/qa/p215_b_source_root02/CANONICAL_ADOPTION.md',
    'docs/papers211_215_sequence/qa/p215_b_data_receiver_source03/run01/DATA_REPORT.json',
    'docs/papers211_215_sequence/qa/p215_b_strict_preparation01/RUN_STRICT.cjs',
    'docs/papers211_215_sequence/qa/p215_b_strict_preparation01/SHA256SUMS', grant
  ];
  const expanded = rows('docs/papers211_215_sequence/reviews/p215_b/SHA256SUMS').map(x => 'docs/papers211_215_sequence/reviews/p215_b/' + x.path)
    .concat(rows('docs/papers211_215_sequence/reviews/p215_b/INPUT_PINS.sha256').map(x => x.path));
  const paths = [...new Set(fixed.concat(expanded).concat(['/usr/bin/node']))].sort();
  const fields = ['dev','ino','mode','size','mtimeNs','ctimeNs'];
  function snap() { return paths.map(path => { const full = path[0] === '/' ? path : rel(path); const b = fs.readFileSync(full); const s = fs.statSync(full, {bigint:true}); return {path, bytes:b.length, sha256:sha(b), metadata:Object.fromEntries(fields.map(k=>[k,String(s[k])]))}; }); }
  const grantBody = JSON.parse(fs.readFileSync(rel(grant), 'utf8'));
  need(grantBody.schema === 'P215_B_STRICT_ONE_USE_GRANT_V1' && grantBody.run_id === run && grantBody.consumed === false, 'grant');
  fs.mkdirSync(rel(out), {recursive:false, mode:0o700});
  const pre = Buffer.from(JSON.stringify(snap(), null, 2) + '\n'); fs.writeFileSync(rel(out + '/PRE.json'), pre, {flag:'wx',mode:0o600});
  const child = cp.spawnSync('/usr/bin/node', [rel('docs/papers211_215_sequence/reviews/p215_b/verify.cjs')], {cwd:W, env:{PATH:'/usr/bin:/bin',LANG:'C',LC_ALL:'C',TZ:'UTC'}, input:Buffer.alloc(0), encoding:null, maxBuffer:16*1024*1024});
  fs.writeFileSync(rel(out + '/stdout.raw'), child.stdout || Buffer.alloc(0), {flag:'wx',mode:0o600});
  fs.writeFileSync(rel(out + '/stderr.raw'), child.stderr || Buffer.alloc(0), {flag:'wx',mode:0o600});
  const exit = {status:child.status, signal:child.signal, error:child.error ? String(child.error) : null, pid:child.pid};
  fs.writeFileSync(rel(out + '/EXIT.json'), JSON.stringify(exit,null,2)+'\n', {flag:'wx',mode:0o600});
  const post = Buffer.from(JSON.stringify(snap(), null, 2) + '\n'); fs.writeFileSync(rel(out + '/POST.json'), post, {flag:'wx',mode:0o600});
  need(pre.equals(post), 'PRE POST mismatch'); need(exit.status === 0 && exit.signal === null && exit.error === null, 'child exit');
  need((child.stderr || Buffer.alloc(0)).length === 0, 'stderr');
  const canonical = fs.readFileSync(rel('docs/papers211_215_sequence/reviews/p215_b/CANONICAL.txt'));
  need((child.stdout || Buffer.alloc(0)).equals(canonical), 'canonical raw mismatch');
  const receipt={schema:'P215_B_STRICT_CAPTURE_V1',run_id:run,input_keys:paths.length,pre_post_equal:true,stdout:{bytes:child.stdout.length,sha256:sha(child.stdout)},stderr:{bytes:child.stderr.length,sha256:sha(child.stderr)},canonical_sha256:sha(canonical),result:'PASS'};
  fs.writeFileSync(rel(out + '/RECEIPT.json'),JSON.stringify(receipt,null,2)+'\n',{flag:'wx',mode:0o600});
  process.stdout.write(JSON.stringify(receipt)+'\n');
}
try { main(); } catch(e) { process.stderr.write(String(e.stack||e)+'\n'); process.exitCode=1; }
