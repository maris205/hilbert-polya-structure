'use strict';

const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const W = '/root/autodl-tmp/symbolic_dynamics';
const PREP = 'docs/papers211_215_sequence/qa/p215_b_execution_preparation02';
const RUN = 'docs/papers211_215_sequence/qa/p215_b_initial_run01';
const REVIEW = 'docs/papers211_215_sequence/reviews/p215_b';
const REPORT = 'docs/papers211_215_sequence/qa/p215_b_data_receiver_source01/INITIAL_NATIVE.json';
const VERIFIER = 'docs/papers211_215_sequence/reviews/p215_b/verify.cjs';

const CAPTURE_MEMBERS = [
  'OUTPUTS.sha256',
  'controller.exit',
  'controller.stderr.raw',
  'controller.stdout.raw',
  'inputs.after.stderr',
  'inputs.after.stdout',
  'inputs.before.stderr',
  'inputs.before.stdout',
  'node.exit',
  'package.after.stderr',
  'package.after.stdout',
  'package.before.stderr',
  'package.before.stdout',
  'preparation.after.stderr',
  'preparation.after.stdout',
  'preparation.before.stderr',
  'preparation.before.stdout',
  'preparation_package.after.stderr',
  'preparation_package.after.stdout',
  'preparation_package.before.stderr',
  'preparation_package.before.stdout',
  'runtime.after.stderr',
  'runtime.after.stdout',
  'runtime.before.stderr',
  'runtime.before.stdout',
  'stderr.raw',
  'stdout.raw'
];

let checks = 0;
let scienceChecks = 0;
function need(value, message) {
  checks++;
  if (!value) throw new Error(message);
}
function scienceNeed(value, message) {
  scienceChecks++;
  if (!value) throw new Error(message);
}
function sha(bytes) {
  return crypto.createHash('sha256').update(bytes).digest('hex');
}
function workspaceRead(relative) {
  return fs.readFileSync(path.join(W, relative));
}
function regularFile(filename, label) {
  const stat = fs.lstatSync(filename);
  need(stat.isFile() && !stat.isSymbolicLink(), 'not a regular non-symlink: ' + label);
}
function parseManifest(relative, base) {
  const bytes = workspaceRead(relative);
  const text = bytes.toString('ascii');
  need(Buffer.from(text, 'ascii').equals(bytes), 'non-ASCII manifest: ' + relative);
  need(text.endsWith('\n'), 'manifest lacks final LF: ' + relative);
  const rows = text.slice(0, -1).split('\n').map((line) => {
    const match = /^([0-9a-f]{64})  ([^\n]+)$/.exec(line);
    need(match !== null, 'bad manifest row: ' + relative);
    const listed = match[2];
    const resolved = path.isAbsolute(listed) ? path.normalize(listed) : path.resolve(base, listed);
    need(path.isAbsolute(listed) || resolved === W || resolved.startsWith(W + path.sep),
      'manifest path escapes workspace: ' + listed);
    return { digest: match[1], listed, resolved };
  });
  need(new Set(rows.map((row) => row.listed)).size === rows.length, 'duplicate manifest member: ' + relative);
  return rows;
}
function verifyCurrent(rows, label) {
  for (const row of rows) {
    regularFile(row.resolved, label + ': ' + row.listed);
    // The independent receiver never opens the B verifier. Its bytes are bound
    // by both captured pre/post sha256sum records and cross-manifest pins.
    if (row.resolved === path.join(W, VERIFIER)) continue;
    need(sha(fs.readFileSync(row.resolved)) === row.digest, 'current hash mismatch: ' + row.listed);
  }
}
function expectedCheckLog(rows) {
  return Buffer.from(rows.map((row) => row.listed + ': OK\n').join(''), 'ascii');
}
function checkLogPair(stem, rows) {
  const before = workspaceRead(RUN + '/' + stem + '.before.stdout');
  const after = workspaceRead(RUN + '/' + stem + '.after.stdout');
  const expected = expectedCheckLog(rows);
  need(before.equals(after), stem + ' stdout pre/post mismatch');
  need(before.equals(expected), stem + ' stdout does not match manifest order');
  need(workspaceRead(RUN + '/' + stem + '.before.stderr').length === 0, stem + ' before stderr');
  need(workspaceRead(RUN + '/' + stem + '.after.stderr').length === 0, stem + ' after stderr');
}
function choose(n, k) {
  if (k < 0 || k > n) return 0;
  let result = 1;
  for (let i = 1; i <= k; i++) result = result * (n - i + 1) / i;
  return result;
}
function vector(code, base, n) {
  const result = [];
  for (let i = 0; i < n; i++) {
    result.push(code % base);
    code = Math.floor(code / base);
  }
  return result;
}
function vectorId(values, base) {
  let id = 0;
  let place = 1;
  for (const value of values) {
    id += value * place;
    place *= base;
  }
  return id;
}
function drawdown(values) {
  let maximum = 0;
  return values.map((value) => {
    maximum = Math.max(maximum, value);
    return maximum - value;
  });
}
function turnCount(values) {
  let previous = 0;
  let sign = 0;
  let count = 0;
  for (const value of values) {
    const difference = value - previous;
    const nextSign = Math.sign(difference);
    if (nextSign !== 0 && nextSign !== sign) {
      count++;
      sign = nextSign;
    }
    previous = value;
  }
  return count;
}
function fibreRecurrence(barriers, q) {
  const c = barriers.slice().reverse().map((value) => q - value);
  const A = [1];
  for (let m = 1; m <= c.length; m++) {
    let value = choose(c[m - 1] + m, m);
    for (let i = 1; i < m; i++) {
      value -= A[i - 1] * choose(c[m - 1] - c[i - 1] + m - i, m - i + 1);
    }
    A.push(value);
  }
  return A[c.length];
}
function reconstructFibre(target, q) {
  const n = target.length;
  if (n === 0) return { ids: [0], recurrence: 1 };
  if (target[0] !== 0) return { ids: [], recurrence: 0 };
  const zeros = [];
  for (let i = 0; i < n; i++) if (target[i] === 0) zeros.push(i);
  const barriers = [];
  let prefixBarrier = 0;
  for (let block = 0; block < zeros.length; block++) {
    const end = block + 1 < zeros.length ? zeros[block + 1] : n;
    let blockMaximum = 0;
    for (let i = zeros[block]; i < end; i++) blockMaximum = Math.max(blockMaximum, target[i]);
    prefixBarrier = Math.max(prefixBarrier, blockMaximum);
    barriers.push(prefixBarrier);
  }

  // Dynamic programming keeps every admissible prefix of nondecreasing
  // record heights. This is not flagged-subset enumeration.
  let prefixes = [[]];
  for (const barrier of barriers) {
    const extended = [];
    for (const prefix of prefixes) {
      const lower = Math.max(barrier, prefix.length === 0 ? 0 : prefix[prefix.length - 1]);
      for (let height = lower; height <= q; height++) extended.push(prefix.concat(height));
    }
    prefixes = extended;
  }
  const ids = prefixes.map((heights) => {
    const source = Array(n);
    for (let block = 0; block < zeros.length; block++) {
      const end = block + 1 < zeros.length ? zeros[block + 1] : n;
      for (let i = zeros[block]; i < end; i++) source[i] = heights[block] - target[i];
    }
    scienceNeed(source.every((value) => Number.isInteger(value) && value >= 0 && value <= q),
      'reconstructed source outside carrier');
    scienceNeed(drawdown(source).every((value, i) => value === target[i]),
      'reconstructed source has wrong transition');
    return vectorId(source, q + 1);
  }).sort((a, b) => a - b);
  scienceNeed(new Set(ids).size === ids.length, 'duplicate DP reconstruction');
  return { ids, recurrence: fibreRecurrence(barriers, q) };
}
function sameNumbers(left, right) {
  return left.length === right.length && left.every((value, i) => value === right[i]);
}
function deriveCarrier(n, q) {
  const base = q + 1;
  const states = base ** n;
  const transition = Array(states);
  const predecessors = Array.from({ length: states }, () => []);
  const indegree = Array(states).fill(0);
  for (let id = 0; id < states; id++) {
    const source = vector(id, base, n);
    const targetId = vectorId(drawdown(source), base);
    transition[id] = targetId;
    predecessors[targetId].push(id);
    indegree[targetId]++;
    scienceNeed(targetId >= 0 && targetId < states, 'transition outside carrier');
  }

  // Peel the functional graph by indegree. The surviving vertices are the
  // recurrent set; reverse peel order then gives every first-entry depth.
  const queue = [];
  for (let id = 0; id < states; id++) if (indegree[id] === 0) queue.push(id);
  const removed = [];
  for (let at = 0; at < queue.length; at++) {
    const id = queue[at];
    removed.push(id);
    const next = transition[id];
    indegree[next]--;
    scienceNeed(indegree[next] >= 0, 'negative indegree');
    if (indegree[next] === 0) queue.push(next);
  }
  const recurrent = [];
  for (let id = 0; id < states; id++) if (indegree[id] > 0) recurrent.push(id);
  scienceNeed(sameNumbers(recurrent, [0]), 'recurrent set is not the zero state');
  scienceNeed(transition[0] === 0, 'zero state is not fixed');
  const depth = Array(states).fill(undefined);
  depth[0] = 0;
  for (let i = removed.length - 1; i >= 0; i--) {
    const id = removed[i];
    scienceNeed(depth[transition[id]] !== undefined, 'depth dependency missing');
    depth[id] = depth[transition[id]] + 1;
  }
  let height = 0;
  for (let id = 0; id < states; id++) {
    scienceNeed(Number.isInteger(depth[id]) && depth[id] >= 0 && depth[id] <= n,
      'invalid bounded depth');
    scienceNeed(depth[id] === turnCount(vector(id, base, n)), 'turn-word/depth mismatch');
    if (id !== 0) scienceNeed(depth[id] === depth[transition[id]] + 1, 'depth recurrence mismatch');
    height = Math.max(height, depth[id]);
  }

  let image = 0;
  let maxFibre = 0;
  let maxTargets = [];
  for (let targetId = 0; targetId < states; targetId++) {
    const target = vector(targetId, base, n);
    const rebuilt = reconstructFibre(target, q);
    scienceNeed(sameNumbers(rebuilt.ids, predecessors[targetId]), 'literal/DP fibre mismatch');
    scienceNeed(rebuilt.recurrence === predecessors[targetId].length, 'recurrence/fibre mismatch');
    if (predecessors[targetId].length > 0) image++;
    if (predecessors[targetId].length > maxFibre) {
      maxFibre = predecessors[targetId].length;
      maxTargets = [targetId];
    } else if (predecessors[targetId].length === maxFibre) {
      maxTargets.push(targetId);
    }
  }
  const expectedHeight = n > 0 && q > 0 ? n : 0;
  const expectedImage = n > 0 ? base ** (n - 1) : 1;
  const expectedMaximum = choose(q + n, n);
  scienceNeed(height === expectedHeight, 'closed-form height mismatch');
  scienceNeed(image === expectedImage, 'closed-form image mismatch');
  scienceNeed(maxFibre === expectedMaximum, 'closed-form maximum fibre mismatch');
  scienceNeed(sameNumbers(maxTargets, [0]), 'maximum fibre target is not uniquely zero');
  return { n, q, states, height, image, maxfibre: maxFibre };
}
function decodeWire(bytes) {
  if (bytes.length === 0) throw new Error('empty stdout');
  for (const byte of bytes) if (byte > 0x7f) throw new Error('stdout is not strict ASCII');
  if (bytes[bytes.length - 1] !== 0x0a) throw new Error('stdout lacks final LF');
  const text = bytes.toString('ascii');
  if (text.includes('\r')) throw new Error('stdout contains CR');
  const lines = text.slice(0, -1).split('\n');
  if (lines.length !== 34) throw new Error('stdout line count is not 34');
  if (lines.some((line) => line.length === 0)) throw new Error('stdout contains empty line');
  return lines;
}
function receive() {
  const runPath = path.join(W, RUN);
  const runStat = fs.lstatSync(runPath);
  need(runStat.isDirectory() && !runStat.isSymbolicLink(), 'capture is not a regular directory');
  const members = fs.readdirSync(runPath).sort();
  need(sameNumbers(members, CAPTURE_MEMBERS), 'capture membership mismatch');
  for (const member of members) regularFile(path.join(runPath, member), 'capture member ' + member);

  const prepInputs = parseManifest(PREP + '/INPUTS.sha256', W);
  const runtimeInputs = parseManifest(PREP + '/RUNTIME_BINARIES.sha256', W);
  const prepPackage = parseManifest(PREP + '/SHA256SUMS', path.join(W, PREP));
  const scientificInputs = parseManifest(REVIEW + '/INPUT_PINS.sha256', W);
  const reviewPackage = parseManifest(REVIEW + '/SHA256SUMS', path.join(W, REVIEW));
  need(prepInputs.length === 11, 'preparation input count');
  need(runtimeInputs.length === 15, 'runtime input count');
  need(prepPackage.length === 11, 'preparation package count');
  need(scientificInputs.length === 43, 'scientific input count');
  need(reviewPackage.length === 9, 'review package count');
  verifyCurrent(prepInputs, 'preparation input');
  verifyCurrent(runtimeInputs, 'runtime input');
  verifyCurrent(prepPackage, 'preparation package');
  verifyCurrent(scientificInputs, 'scientific input');
  verifyCurrent(reviewPackage, 'review package');

  const verifierPins = [];
  for (const rows of [prepInputs, reviewPackage]) {
    for (const row of rows) if (row.resolved === path.join(W, VERIFIER)) verifierPins.push(row.digest);
  }
  need(verifierPins.length === 2 && new Set(verifierPins).size === 1, 'verifier cross-pin mismatch');
  const binding = JSON.parse(workspaceRead(PREP + '/RUNTIME_BINDING.json'));
  need(binding.schema === 'P215_B_INITIAL_RUNTIME_BINDING_V1', 'runtime binding schema');
  need(binding.workspace === W && binding.controlled_output === RUN, 'runtime binding paths');
  need(binding.child.path === '/usr/bin/node' && binding.child.script === VERIFIER, 'runtime child binding');
  need(binding.child.sha256 === runtimeInputs.find((row) => row.listed === '/usr/bin/node').digest,
    'runtime node pin mismatch');
  need(binding.child.script_sha256 === verifierPins[0], 'runtime verifier pin mismatch');
  need(JSON.stringify(binding.child.arguments) === '[]' && binding.child.stdin === '/dev/null', 'runtime arguments');
  need(JSON.stringify(binding.environment) === JSON.stringify({ PATH: '/usr/bin:/bin', LANG: 'C', LC_ALL: 'C', TZ: 'UTC' }),
    'runtime environment');
  need(JSON.stringify(binding.source_declarations) === JSON.stringify({ imports: [], external_reads: [], canonical_reads: [] }),
    'runtime source declarations');

  checkLogPair('preparation', prepInputs);
  checkLogPair('runtime', runtimeInputs);
  checkLogPair('preparation_package', prepPackage);
  checkLogPair('inputs', scientificInputs);
  checkLogPair('package', reviewPackage);
  need(workspaceRead(RUN + '/node.exit').equals(Buffer.from('0\n')), 'child exit');
  need(workspaceRead(RUN + '/controller.exit').equals(Buffer.from('0\n')), 'controller exit');
  need(workspaceRead(RUN + '/stderr.raw').length === 0, 'child stderr');
  need(workspaceRead(RUN + '/controller.stderr.raw').length === 0, 'controller stderr');
  need(workspaceRead(RUN + '/controller.stdout.raw').equals(
    Buffer.from('P215_B_INITIAL_CAPTURE_COMPLETE_PENDING_DATA_RECEPTION\n')), 'controller stdout');

  const stdout = workspaceRead(RUN + '/stdout.raw');
  const stderr = workspaceRead(RUN + '/stderr.raw');
  const nodeExit = workspaceRead(RUN + '/node.exit');
  const outputRows = parseManifest(RUN + '/OUTPUTS.sha256', W);
  need(outputRows.length === 3, 'output manifest count');
  const expectedOutputNames = [RUN + '/stdout.raw', RUN + '/stderr.raw', RUN + '/node.exit'];
  need(sameNumbers(outputRows.map((row) => row.listed), expectedOutputNames), 'output manifest order');
  need(outputRows[0].digest === sha(stdout) && outputRows[1].digest === sha(stderr) &&
    outputRows[2].digest === sha(nodeExit), 'output manifest digest');

  const carriers = [];
  let reconstructedStates = 0;
  for (let n = 0; n <= 5; n++) {
    for (let q = 0; q <= 4; q++) {
      const carrier = deriveCarrier(n, q);
      carriers.push(carrier);
      reconstructedStates += carrier.states;
    }
  }
  scienceNeed(carriers.length === 30, 'carrier total');
  scienceNeed(reconstructedStates === 5704, 'state total');

  const lines = decodeWire(stdout);
  need(lines[0] === 'P215_B_FLOYD_FLAGGED_SUBSETS_V1', 'wire header');
  need(lines[1] === 'PARAM|n=0..5|q=0..4', 'wire parameters');
  let at = 2;
  for (const expected of carriers) {
    const match = /^CARRIER\|n=(\d+)\|q=(\d+)\|states=(\d+)\|height=(\d+)\|image=(\d+)\|maxfibre=(\d+)$/.exec(lines[at++]);
    need(match !== null, 'carrier wire syntax');
    const got = match.slice(1).map(Number);
    need(sameNumbers(got, [expected.n, expected.q, expected.states, expected.height,
      expected.image, expected.maxfibre]), 'carrier wire value/order mismatch');
  }
  const total = /^TOTAL\|carriers=30\|states=5704\|assertions=([1-9]\d*)$/.exec(lines[at++]);
  need(total !== null && Number.isSafeInteger(Number(total[1])), 'TOTAL wire syntax/assertions');
  need(lines[at++] === 'PASS' && at === lines.length, 'wire terminal/order');

  const report = {
    schema: 'P215_B_INITIAL_DATA_RECEIVER_V1',
    result: 'PASS',
    preparation: PREP,
    capture: RUN,
    capture_members: members.length,
    preparation_input_pins: prepInputs.length,
    runtime_pins: runtimeInputs.length,
    preparation_package_pins: prepPackage.length,
    scientific_input_pins: scientificInputs.length,
    review_package_pins: reviewPackage.length,
    verifier_runtime_read: false,
    carriers: carriers.length,
    reconstructed_states: reconstructedStates,
    reconstructed_targets: reconstructedStates,
    receiver_checks: checks,
    scientific_checks: scienceChecks,
    observed_verifier_assertions: Number(total[1]),
    stdout_bytes: stdout.length,
    stdout_sha256: sha(stdout),
    stderr_bytes: stderr.length,
    stderr_sha256: sha(stderr),
    scope: 'INITIAL_DATA_ONLY'
  };
  fs.writeFileSync(path.join(W, REPORT), JSON.stringify(report, null, 2) + '\n', { flag: 'wx', mode: 0o600 });
  process.stdout.write(JSON.stringify(report) + '\n');
}
function selfTest() {
  const fixtures = [
    Buffer.alloc(0),
    Buffer.from('x'),
    Buffer.from('x\r\n'),
    Buffer.from([0x80, 0x0a]),
    Buffer.from('x\n\n')
  ];
  for (const fixture of fixtures) {
    let rejected = false;
    try { decodeWire(fixture); } catch (_) { rejected = true; }
    if (!rejected) throw new Error('negative framing fixture accepted');
  }
  if (/^CARRIER\|n=(\d+)\|q=(\d+)\|states=(\d+)\|height=(\d+)\|image=(\d+)\|maxfibre=(\d+)$/.test(
    'CARRIER|n=x|q=x|states=x|height=x|image=x|max_fibre=x')) {
    throw new Error('legacy max_fibre spelling accepted');
  }
  process.stdout.write('P215_B_DATA_RECEIVER_NEGATIVE_SELF_TEST_PASS\n');
}

try {
  if (process.argv.length === 3 && process.argv[2] === '--self-test') selfTest();
  else if (process.argv.length === 3 && process.argv[2] === '--receive-initial') receive();
  else throw new Error('usage: node RECEIVE_INITIAL.cjs --self-test|--receive-initial');
} catch (error) {
  process.stderr.write(String(error.stack || error) + '\n');
  process.exitCode = 1;
}
