'use strict';

const fs = require('node:fs');
const crypto = require('node:crypto');

const W = '/root/autodl-tmp/symbolic_dynamics';
const Q = 'docs/papers211_215_sequence/qa';
const HERE = `${Q}/p215_b_data_receiver_source03`;
const CAPTURE = `${Q}/p215_b_initial_run01`;
const PREP = `${Q}/p215_b_execution_preparation02`;
const REVIEW = 'docs/papers211_215_sequence/reviews/p215_b';
const VERIFY = `${REVIEW}/verify.cjs`;
const VERIFY_SHA = '5371b96ec0b253045e310ee152bfd0e98229d27985627b2a72f04c6e34bd2022';
const EXPECTED_CAPTURE = [
  'OUTPUTS.sha256', 'controller.exit', 'controller.stderr.raw',
  'controller.stdout.raw', 'inputs.after.stderr', 'inputs.after.stdout',
  'inputs.before.stderr', 'inputs.before.stdout', 'node.exit',
  'package.after.stderr', 'package.after.stdout', 'package.before.stderr',
  'package.before.stdout', 'preparation.after.stderr',
  'preparation.after.stdout', 'preparation.before.stderr',
  'preparation.before.stdout', 'preparation_package.after.stderr',
  'preparation_package.after.stdout', 'preparation_package.before.stderr',
  'preparation_package.before.stdout', 'runtime.after.stderr',
  'runtime.after.stdout', 'runtime.before.stderr', 'runtime.before.stdout',
  'stderr.raw', 'stdout.raw'
].sort();

let checks = 0;
let transitionChecks = 0;
let reconstructedPredecessors = 0;

function need(value, message) {
  checks++;
  if (!value) throw new Error(message);
}
function sha(bytes) {
  return crypto.createHash('sha256').update(bytes).digest('hex');
}
function abs(path) {
  return path.startsWith('/') ? path : `${W}/${path}`;
}
function read(path) {
  return fs.readFileSync(abs(path));
}
function regular(path) {
  const stat = fs.lstatSync(abs(path));
  need(stat.isFile() && !stat.isSymbolicLink(), `not a regular non-link file: ${path}`);
  return stat;
}
function parseManifest(path, base = '') {
  regular(path);
  const text = read(path).toString('ascii');
  need(text.endsWith('\n'), `manifest final LF: ${path}`);
  const rows = text.slice(0, -1).split('\n').map((line) => {
    const match = /^([0-9a-f]{64})  (\S+)$/.exec(line);
    need(match !== null, `manifest row: ${path}`);
    return { digest: match[1], shown: match[2], path: base ? `${base}/${match[2]}` : match[2] };
  });
  need(new Set(rows.map((row) => row.shown)).size === rows.length, `duplicate manifest path: ${path}`);
  return rows;
}
function verifyRows(rows, label, skipVerifier = false) {
  for (const row of rows) {
    regular(row.path);
    if (skipVerifier && row.path === VERIFY) {
      need(row.digest === VERIFY_SHA, `${label} verifier digest`);
    } else {
      need(sha(read(row.path)) === row.digest, `${label} digest: ${row.path}`);
    }
  }
}
function verifyRuntimeRows(rows) {
  for (const row of rows) {
    const stat = fs.statSync(abs(row.path));
    need(stat.isFile(), `runtime target is not a file: ${row.path}`);
    need(sha(read(row.path)) === row.digest, `runtime digest: ${row.path}`);
  }
}
function expectedCheckLog(rows) {
  return Buffer.from(rows.map((row) => `${row.shown}: OK\n`).join(''), 'ascii');
}
function exactPair(stem, rows) {
  const beforeOut = read(`${CAPTURE}/${stem}.before.stdout`);
  const afterOut = read(`${CAPTURE}/${stem}.after.stdout`);
  const beforeErr = read(`${CAPTURE}/${stem}.before.stderr`);
  const afterErr = read(`${CAPTURE}/${stem}.after.stderr`);
  need(beforeOut.equals(afterOut), `${stem} stdout pre/post`);
  need(beforeErr.equals(afterErr), `${stem} stderr pre/post`);
  need(beforeErr.length === 0, `${stem} stderr empty`);
  const expected = expectedCheckLog(rows);
  need(beforeOut.equals(expected), `${stem} exact check log`);
}
function choose(n, k) {
  if (!Number.isInteger(n) || !Number.isInteger(k) || k < 0 || k > n || n < 0) return 0;
  k = Math.min(k, n - k);
  let value = 1;
  for (let i = 1; i <= k; i++) value = value * (n - k + i) / i;
  return value;
}
function enumerateStates(n, q) {
  const states = [];
  const word = Array(n).fill(0);
  function visit(i) {
    if (i === n) { states.push(word.slice()); return; }
    for (let value = 0; value <= q; value++) {
      word[i] = value;
      visit(i + 1);
    }
  }
  visit(0);
  return states;
}
function key(word) {
  return word.join(',');
}
function mapWord(word) {
  let maximum = 0;
  return word.map((value) => {
    maximum = Math.max(maximum, value);
    return maximum - value;
  });
}
function signRuns(word) {
  let previous = 0;
  let lastSign = 0;
  let runs = 0;
  for (const value of word) {
    const delta = value - previous;
    const sign = Math.sign(delta);
    if (sign !== 0 && sign !== lastSign) { runs++; lastSign = sign; }
    previous = value;
  }
  return runs;
}
function compareWord(a, b) {
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) return a[i] - b[i];
  }
  return 0;
}
function heightDP(target, q) {
  const zeros = [];
  for (let i = 0; i < target.length; i++) if (target[i] === 0) zeros.push(i);
  const barriers = [];
  let prefixBarrier = 0;
  for (let j = 0; j < zeros.length; j++) {
    const end = j + 1 < zeros.length ? zeros[j + 1] : target.length;
    let blockMaximum = 0;
    for (let i = zeros[j]; i < end; i++) blockMaximum = Math.max(blockMaximum, target[i]);
    prefixBarrier = Math.max(prefixBarrier, blockMaximum);
    barriers.push(prefixBarrier);
  }
  let dp = new Map([[-1, [[]]]]);
  for (let j = 0; j < barriers.length; j++) {
    const next = new Map();
    for (const [last, paths] of dp) {
      for (let level = Math.max(last, barriers[j]); level <= q; level++) {
        if (!next.has(level)) next.set(level, []);
        for (const path of paths) next.get(level).push(path.concat(level));
      }
    }
    dp = next;
  }
  const heights = [...dp.values()].flat();
  const sources = heights.map((levels) => {
    const source = Array(target.length);
    for (let j = 0; j < zeros.length; j++) {
      const end = j + 1 < zeros.length ? zeros[j + 1] : target.length;
      for (let i = zeros[j]; i < end; i++) source[i] = levels[j] - target[i];
    }
    return source;
  });
  return { barriers, sources };
}
function recurrenceCount(barriers, q) {
  const c = barriers.slice().reverse().map((value) => q - value);
  const A = [1];
  for (let m = 1; m <= c.length; m++) {
    let value = choose(c[m - 1] + m, m);
    for (let i = 1; i < m; i++) {
      value -= A[i - 1] * choose(c[m - 1] - c[i - 1] + m - i, m - i + 1);
    }
    A[m] = value;
  }
  return A[c.length];
}
function deriveCarrier(n, q) {
  const states = enumerateStates(n, q);
  const index = new Map(states.map((state, i) => [key(state), i]));
  need(index.size === states.length, `state uniqueness n=${n} q=${q}`);
  const transitions = [];
  const predecessors = Array.from({ length: states.length }, () => []);
  const indegree = Array(states.length).fill(0);
  for (let i = 0; i < states.length; i++) {
    const image = mapWord(states[i]);
    const target = index.get(key(image));
    need(target !== undefined, `transition closure n=${n} q=${q}`);
    transitions[i] = target;
    predecessors[target].push(i);
    indegree[target]++;
    transitionChecks++;
  }

  const queue = [];
  const remaining = Array(states.length).fill(true);
  for (let i = 0; i < states.length; i++) if (indegree[i] === 0) queue.push(i);
  for (let head = 0; head < queue.length; head++) {
    const vertex = queue[head];
    remaining[vertex] = false;
    const target = transitions[vertex];
    indegree[target]--;
    if (indegree[target] === 0) queue.push(target);
  }
  const recurrent = [];
  for (let i = 0; i < states.length; i++) if (remaining[i]) recurrent.push(i);
  const zero = index.get(key(Array(n).fill(0)));
  need(recurrent.length === 1 && recurrent[0] === zero, `unique recurrent zero n=${n} q=${q}`);

  const depth = Array(states.length).fill(-1);
  depth[zero] = 0;
  const layers = [zero];
  for (let head = 0; head < layers.length; head++) {
    const target = layers[head];
    for (const source of predecessors[target]) {
      if (source !== target && depth[source] === -1) {
        depth[source] = depth[target] + 1;
        layers.push(source);
      }
    }
  }
  need(layers.length === states.length, `complete reverse layers n=${n} q=${q}`);
  let height = 0;
  for (let i = 0; i < states.length; i++) {
    need(depth[i] >= 0 && depth[i] <= n, `bounded depth n=${n} q=${q}`);
    need(depth[i] === signRuns(states[i]), `sign-run depth n=${n} q=${q} state=${key(states[i])}`);
    if (i === zero) need(transitions[i] === zero, `zero fixed n=${n} q=${q}`);
    else need(depth[transitions[i]] === depth[i] - 1, `first-zero layer n=${n} q=${q} state=${key(states[i])}`);
    height = Math.max(height, depth[i]);
  }

  let imageSize = 0;
  let maxFibre = -1;
  const maximizers = [];
  for (let t = 0; t < states.length; t++) {
    const target = states[t];
    const bucket = predecessors[t].map((i) => states[i]).sort(compareWord);
    let rebuilt = [];
    let recurrence = 0;
    if (n === 0 || target[0] === 0) {
      const result = heightDP(target, q);
      rebuilt = result.sources.sort(compareWord);
      recurrence = recurrenceCount(result.barriers, q);
      for (const source of rebuilt) {
        need(source.length === n && source.every((value) => Number.isInteger(value) && value >= 0 && value <= q), `DP source bounds n=${n} q=${q}`);
        need(key(mapWord(source)) === key(target), `DP literal transition n=${n} q=${q}`);
        reconstructedPredecessors++;
        transitionChecks++;
      }
    }
    need(recurrence === rebuilt.length, `recurrence count n=${n} q=${q} target=${key(target)}`);
    need(rebuilt.length === bucket.length, `fibre size n=${n} q=${q} target=${key(target)}`);
    need(rebuilt.every((source, i) => compareWord(source, bucket[i]) === 0), `fibre members n=${n} q=${q} target=${key(target)}`);
    if (bucket.length > 0) imageSize++;
    if (bucket.length > maxFibre) { maxFibre = bucket.length; maximizers.length = 0; maximizers.push(t); }
    else if (bucket.length === maxFibre) maximizers.push(t);
  }
  need(maximizers.length === 1 && maximizers[0] === zero, `unique maximizing zero n=${n} q=${q}`);
  const expected = {
    states: (q + 1) ** n,
    height: n > 0 && q > 0 ? n : 0,
    image: n > 0 ? (q + 1) ** (n - 1) : 1,
    maxfibre: choose(q + n, n)
  };
  need(states.length === expected.states, `closed states n=${n} q=${q}`);
  need(height === expected.height, `closed height n=${n} q=${q}`);
  need(imageSize === expected.image, `closed image n=${n} q=${q}`);
  need(maxFibre === expected.maxfibre, `closed fibre n=${n} q=${q}`);
  return { n, q, states: states.length, height, image: imageSize, maxfibre: maxFibre };
}
function main() {
  const grant = JSON.parse(read(`${HERE}/GRANT.receiver01.json`));
  need(grant.schema === 'P215_B_DATA_RECEIVER_ROOT_CORRECTION_GRANT_V1' && grant.authority === 'root', 'grant identity');
  need(grant.action === 'execute_receiver_once' && grant.consumption === 'immediate_single_execution_no_retry', 'grant action');
  need(grant.source_manifest === `${HERE}/SOURCE_SHA256SUMS`, 'grant source manifest');
  need(sha(read(grant.source_manifest)) === grant.source_manifest_sha256, 'grant source seal');
  need(sha(read(`${Q}/p215_b_initial_binding01/GRANT.md`)) === grant.initial_grant_sha256, 'initial grant pin');
  need(sha(read(`${Q}/p215_b_initial_binding01/ACTUAL_NATIVE.json`)) === grant.initial_actual_native_sha256, 'initial actual-native pin');
  need(sha(read(`${PREP}/SHA256SUMS`)) === grant.preparation_manifest_sha256, 'preparation manifest pin');
  need(sha(read(`${REVIEW}/INPUT_PINS.sha256`)) === grant.scientific_input_manifest_sha256, 'scientific manifest pin');
  need(sha(read(`${REVIEW}/SHA256SUMS`)) === grant.review_package_manifest_sha256, 'review package manifest pin');
  const sourceRows = parseManifest(grant.source_manifest);
  need(sourceRows.length === 3, 'source seal rows');
  verifyRows(sourceRows, 'receiver source');

  const captureStat = fs.lstatSync(abs(CAPTURE));
  need(captureStat.isDirectory() && !captureStat.isSymbolicLink(), 'capture directory');
  const members = fs.readdirSync(abs(CAPTURE)).sort();
  need(JSON.stringify(members) === JSON.stringify(EXPECTED_CAPTURE), 'exact capture membership');
  for (const member of members) regular(`${CAPTURE}/${member}`);

  const prepInputs = parseManifest(`${PREP}/INPUTS.sha256`);
  const runtimeRows = parseManifest(`${PREP}/RUNTIME_BINARIES.sha256`);
  const prepPackage = parseManifest(`${PREP}/SHA256SUMS`, PREP);
  const scientificRows = parseManifest(`${REVIEW}/INPUT_PINS.sha256`);
  const reviewPackage = parseManifest(`${REVIEW}/SHA256SUMS`, REVIEW);
  need(prepInputs.length === 11, 'preparation inputs count');
  need(runtimeRows.length === 15, 'runtime pins count');
  need(prepPackage.length === 11, 'preparation package count');
  need(scientificRows.length === 43, 'scientific input count');
  need(reviewPackage.length === 9, 'review package count');
  verifyRows(prepInputs, 'preparation input', true);
  verifyRuntimeRows(runtimeRows);
  verifyRows(prepPackage, 'preparation package');
  verifyRows(scientificRows, 'scientific input');
  verifyRows(reviewPackage, 'review package', true);
  const prepVerify = prepInputs.find((row) => row.path === VERIFY);
  const packageVerify = reviewPackage.find((row) => row.path === VERIFY);
  need(prepVerify && packageVerify && prepVerify.digest === packageVerify.digest && packageVerify.digest === VERIFY_SHA, 'verifier cross-manifest pin');

  exactPair('preparation', prepInputs);
  exactPair('runtime', runtimeRows);
  exactPair('preparation_package', prepPackage);
  exactPair('inputs', scientificRows);
  exactPair('package', reviewPackage);
  const emptyStderr = ['controller.stderr.raw', 'stderr.raw'];
  for (const name of emptyStderr) need(read(`${CAPTURE}/${name}`).length === 0, `empty ${name}`);
  need(read(`${CAPTURE}/node.exit`).equals(Buffer.from('0\n')), 'node exit');
  need(read(`${CAPTURE}/controller.exit`).equals(Buffer.from('0\n')), 'controller exit');
  need(read(`${CAPTURE}/controller.stdout.raw`).equals(Buffer.from('P215_B_INITIAL_CAPTURE_COMPLETE_PENDING_DATA_RECEPTION\n')), 'controller stdout');

  const outputRows = parseManifest(`${CAPTURE}/OUTPUTS.sha256`);
  need(outputRows.length === 3, 'output receipt count');
  need(JSON.stringify(outputRows.map((row) => row.path)) === JSON.stringify([
    `${CAPTURE}/stdout.raw`, `${CAPTURE}/stderr.raw`, `${CAPTURE}/node.exit`
  ]), 'output receipt order');
  verifyRows(outputRows, 'capture output');
  const actual = JSON.parse(read(`${Q}/p215_b_initial_binding01/ACTUAL_NATIVE.json`));
  need(actual.schema === 'P215_B_INITIAL_ACTUAL_NATIVE_V1' && actual.exit_code === 0 && actual.retry === false, 'actual native status');
  need(actual.output_root === CAPTURE && actual.stdout_lines === 34 && actual.stderr_bytes === 0, 'actual native envelope');

  const stdout = read(`${CAPTURE}/stdout.raw`);
  const stderr = read(`${CAPTURE}/stderr.raw`);
  need(stdout.length === actual.stdout_bytes, 'actual stdout bytes');
  need(sha(stdout) === actual.stdout_sha256, 'actual stdout hash');
  need(stderr.length === actual.stderr_bytes, 'actual stderr bytes');
  need(stdout.length > 0 && stdout[stdout.length - 1] === 0x0a, 'stdout final LF');
  need([...stdout].every((byte) => byte === 0x0a || (byte >= 0x20 && byte <= 0x7e)), 'stdout strict ASCII');
  const lines = stdout.toString('ascii').split('\n');
  need(lines.pop() === '' && lines.length === 34, 'stdout exact line count');
  need(lines[0] === 'P215_B_FLOYD_FLAGGED_SUBSETS_V1', 'wire header');
  need(lines[1] === 'PARAM|n=0..5|q=0..4', 'wire parameters');

  const derived = [];
  let totalStates = 0;
  for (let n = 0; n <= 5; n++) {
    for (let q = 0; q <= 4; q++) {
      const carrier = deriveCarrier(n, q);
      derived.push(carrier);
      totalStates += carrier.states;
    }
  }
  need(derived.length === 30 && totalStates === 5704, 'independent carrier totals');
  let cursor = 2;
  for (const carrier of derived) {
    const expected = `CARRIER|n=${carrier.n}|q=${carrier.q}|states=${carrier.states}|height=${carrier.height}|image=${carrier.image}|maxfibre=${carrier.maxfibre}`;
    need(lines[cursor++] === expected, `wire carrier n=${carrier.n} q=${carrier.q}`);
  }
  const totalMatch = /^TOTAL\|carriers=30\|states=5704\|assertions=([1-9][0-9]*)$/.exec(lines[cursor++]);
  need(totalMatch !== null, 'wire total');
  const observedAssertions = Number(totalMatch[1]);
  need(Number.isSafeInteger(observedAssertions) && observedAssertions === actual.observed_assertions, 'observed assertion binding');
  need(lines[cursor++] === 'PASS' && cursor === lines.length, 'wire terminal');

  const report = {
    schema: 'P215_B_INITIAL_DATA_RECEPTION_V1',
    status: 'INITIAL_DATA_ACCEPTED_ONLY',
    capture: CAPTURE,
    capture_members: members.length,
    preparation_inputs: prepInputs.length,
    runtime_pins: runtimeRows.length,
    preparation_package: prepPackage.length,
    scientific_inputs: scientificRows.length,
    review_package: reviewPackage.length,
    carriers: derived.length,
    states: totalStates,
    reconstructed_predecessors: reconstructedPredecessors,
    literal_transition_checks: transitionChecks,
    observed_verifier_assertions: observedAssertions,
    observed_assertions_role: 'WIRE_FIELD_ONLY_NOT_RECEIVER_PROOF',
    receiver_checks: checks + 1,
    stdout_bytes: stdout.length,
    stdout_sha256: sha(stdout),
    stderr_bytes: stderr.length,
    result: 'PASS',
    limitations: ['NO_CANONICAL', 'NO_STRICT', 'NO_DELTA', 'NO_FINAL_B', 'NO_BUILD', 'NO_ROUND2', 'HOLD_EXTERNAL']
  };
  const reportBytes = Buffer.from(JSON.stringify(report, null, 2) + '\n');
  fs.writeFileSync(abs(`${HERE}/run01/DATA_REPORT.json`), reportBytes, { flag: 'wx', mode: 0o600 });
  process.stdout.write(JSON.stringify(report) + '\n');
}

try {
  main();
} catch (error) {
  process.stderr.write(String(error.stack || error) + '\n');
  process.exitCode = 1;
}
