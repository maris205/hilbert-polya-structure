'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const W = '/root/autodl-tmp/symbolic_dynamics';
const R = 'docs/papers211_215_sequence/qa/p215_a_runs/initial01';
const fields = ['dev', 'ino', 'mode', 'size', 'mtimeNs', 'ctimeNs'];
let checks = 0;
function need(value, message) { checks++; if (!value) throw Error(message); }
function sha(bytes) { return crypto.createHash('sha256').update(bytes).digest('hex'); }
function read(path) { return fs.readFileSync(W + '/' + path); }
function metadata(stat) { return Object.fromEntries(fields.map(k => [k, String(stat[k])])); }
function choose(n, k) {
  if (k < 0 || k > n) return 0;
  let answer = 1;
  for (let j = 1; j <= k; j++) answer = answer * (n - j + 1) / j;
  return answer;
}
function main() {
  const preBytes = read(R + '/PRE.json');
  const postBytes = read(R + '/POST.json');
  need(preBytes.equals(postBytes), 'PRE/POST raw mismatch');
  const pre = JSON.parse(preBytes);
  need(Array.isArray(pre) && pre.length === 29, 'input key count');
  for (const row of pre) {
    const bytes = read(row.path);
    const stat = fs.statSync(W + '/' + row.path, { bigint: true });
    need(stat.isFile(), 'not regular ' + row.path);
    need(bytes.length === row.bytes, 'size ' + row.path);
    need(sha(bytes) === row.sha256, 'hash ' + row.path);
    need(JSON.stringify(metadata(stat)) === JSON.stringify(row.metadata), 'metadata ' + row.path);
  }
  const exit = JSON.parse(read(R + '/EXIT.json'));
  need(exit.status === 0 && exit.signal === null && exit.error === null, 'exit');
  const receipt = JSON.parse(read(R + '/RECEIPT.json'));
  need(receipt.run_id === 'initial01', 'run id');
  need(receipt.input_keys === 29 && receipt.pre_post_equal === true, 'receipt keys');
  const stdout = read(R + '/stdout.raw');
  const stderr = read(R + '/stderr.raw');
  need(stderr.length === 0 && sha(stderr) === receipt.stderr.sha256, 'stderr');
  need(stdout.length === 2060 && stdout.length === receipt.stdout.bytes, 'stdout size');
  need(sha(stdout) === '58f40d2d90505ccf3be39453c213bb99d82aa4b268f88a2c8d6b1e968209d695', 'stdout hash');
  need(sha(stdout) === receipt.stdout.sha256, 'receipt stdout hash');
  const text = stdout.toString('ascii');
  need(text.endsWith('\n'), 'stdout LF');
  const lines = text.trimEnd().split('\n');
  need(lines.length === 39, 'line count');
  need(lines[0] === 'P215_A_REVERSE_AUTOMATON_V1', 'header');
  need(lines[1] === 'PARAM n=0..6 q=0..4', 'parameters');
  let index = 2, statesTotal = 0, assertions = 0;
  for (let n = 0; n <= 6; n++) {
    for (let q = 0; q <= 4; q++) {
      const match = /^CARRIER n=(\d+) q=(\d+) states=(\d+) height=(\d+) image=(\d+) max_fibre=(\d+)$/.exec(lines[index++]);
      need(match !== null, 'carrier syntax');
      const got = match.slice(1).map(Number);
      const states = (q + 1) ** n;
      const height = n && q ? n : 0;
      const image = n ? (q + 1) ** (n - 1) : 1;
      const fibre = choose(q + n, n);
      need(JSON.stringify(got) === JSON.stringify([n, q, states, height, image, fibre]), 'carrier values');
      statesTotal += states;
      assertions += 6 * states + 4;
    }
  }
  need(statesTotal === 26219 && assertions === 157454, 'independent totals');
  need(lines[index++] === 'TOTAL carriers=35 states=26219 assertions=157454', 'total line');
  need(lines[index++] === 'PASS' && index === lines.length, 'terminal line');
  const report = { schema: 'P215_A_INITIAL_RECEIVER_V1', checks, input_keys: pre.length,
    carriers: 35, states: statesTotal, assertions, stdout_bytes: stdout.length,
    stdout_sha256: sha(stdout), stderr_bytes: stderr.length, result: 'PASS' };
  fs.writeFileSync(W + '/docs/papers211_215_sequence/qa/p215_a_source_root01/INITIAL_NATIVE.json', JSON.stringify(report, null, 2) + '\n', { flag: 'wx', mode: 0o600 });
  process.stdout.write(JSON.stringify(report) + '\n');
}
try { main(); } catch (error) { process.stderr.write(String(error.stack || error) + '\n'); process.exitCode = 1; }
