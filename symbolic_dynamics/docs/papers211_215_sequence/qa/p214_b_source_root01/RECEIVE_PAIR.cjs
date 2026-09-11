'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const W = '/root/autodl-tmp/symbolic_dynamics';
const RUNS = 'docs/papers211_215_sequence/qa/p214_b_runs';
const fields = ['dev', 'ino', 'mode', 'size', 'mtimeNs', 'ctimeNs'];
let checks = 0;
function need(value, message) { checks++; if (!value) throw Error(message); }
function read(path) { return fs.readFileSync(W + '/' + path); }
function sha(bytes) { return crypto.createHash('sha256').update(bytes).digest('hex'); }
function metadata(stat) { return Object.fromEntries(fields.map(k => [k, String(stat[k])])); }
function receive(id, expectedKeys) {
  const base = RUNS + '/' + id;
  const preBytes = read(base + '/PRE.json');
  const postBytes = read(base + '/POST.json');
  need(preBytes.equals(postBytes), id + ' PRE/POST');
  const pre = JSON.parse(preBytes);
  need(pre.length === expectedKeys, id + ' keys');
  for (const row of pre) {
    const bytes = read(row.path);
    const stat = fs.statSync(W + '/' + row.path, { bigint: true });
    need(stat.isFile(), id + ' regular ' + row.path);
    need(bytes.length === row.bytes, id + ' size ' + row.path);
    need(sha(bytes) === row.sha256, id + ' hash ' + row.path);
    need(JSON.stringify(metadata(stat)) === JSON.stringify(row.metadata), id + ' metadata ' + row.path);
  }
  const exit = JSON.parse(read(base + '/EXIT.json'));
  need(exit.status === 0 && exit.signal === null && exit.error === null, id + ' exit');
  const receipt = JSON.parse(read(base + '/RECEIPT.json'));
  need(receipt.run_id === id && receipt.input_keys === expectedKeys && receipt.pre_post_equal === true, id + ' receipt');
  const stdout = read(base + '/stdout.raw');
  const stderr = read(base + '/stderr.raw');
  need(stdout.length === receipt.stdout.bytes && sha(stdout) === receipt.stdout.sha256, id + ' stdout envelope');
  need(stderr.length === 0 && stderr.length === receipt.stderr.bytes && sha(stderr) === receipt.stderr.sha256, id + ' stderr envelope');
  return stdout;
}
function main() {
  const initial = receive('initial01', 44);
  const first = receive('strict01', 45);
  const second = receive('strict02', 45);
  const canonical = read('docs/papers211_215_sequence/reviews/p214_b/CANONICAL.txt');
  need(initial.equals(canonical), 'initial/canonical');
  need(first.equals(canonical), 'strict01/canonical');
  need(second.equals(canonical), 'strict02/canonical');
  need(first.equals(second), 'strict pair');
  need(canonical.length === 641682, 'canonical bytes');
  need(sha(canonical) === '7834b38f93b9dfe5e5a57f230ef8d8bac3082a7f7870e9cb384c0dfb9b9ec8f9', 'canonical hash');
  const report = { schema: 'P214_B_PAIR_RECEIVER_V1', checks, initial_keys: 44,
    strict_keys: 45, stdout_bytes: canonical.length, stdout_sha256: sha(canonical),
    all_stdout_raw_equal: true, all_stderr_empty: true, result: 'PASS' };
  fs.writeFileSync(W + '/docs/papers211_215_sequence/qa/p214_b_source_root01/PAIR_NATIVE.json', JSON.stringify(report, null, 2) + '\n', { flag: 'wx', mode: 0o600 });
  process.stdout.write(JSON.stringify(report) + '\n');
}
try { main(); } catch (error) { process.stderr.write(String(error.stack || error) + '\n'); process.exitCode = 1; }
