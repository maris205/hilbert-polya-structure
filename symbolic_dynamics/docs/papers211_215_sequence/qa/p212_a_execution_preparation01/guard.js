'use strict';
// SOURCE ONLY at preparation. A separate exact root grant is mandatory.
const fs = require('node:fs');
const crypto = require('node:crypto');
const child = require('node:child_process');

const WORKSPACE = '/root/autodl-tmp/symbolic_dynamics';
const PREP = 'docs/papers211_215_sequence/qa/p212_a_execution_preparation01';
const ROOT = 'docs/papers211_215_sequence/qa/p212_a_source_root01';
const REVIEW = 'docs/papers211_215_sequence/reviews/p212_a';
const RUNS = 'docs/papers211_215_sequence/qa/p212_a_runs';
const SCIENCE = WORKSPACE + '/' + REVIEW + '/verify.py';
const INTERPRETER = '/usr/bin/python3.10';
const SCIENCE_ARGS = ['-I', '-S', '-B', SCIENCE];
const SCIENCE_ENV = {LANG: 'C', LC_ALL: 'C'};
const TIMEOUT_MS = 600000;
const KEYS = ['dev', 'ino', 'mode', 'size', 'mtimeNs', 'ctimeNs'];
const FIXED = [
  [ROOT + '/RUNTIME_INPUTS.json', 'fd64f171325548a01dc076ceda92685aad6577485334e7622d7a84ee4bc9e22b'],
  [ROOT + '/ORDINARY_RUNTIME_POLICY.md', 'b35af6b5bf9f94bd2f35b0e2f1ad4e97253909a5a46040bb693a60844c3e8739'],
  [ROOT + '/SOURCE_RECEPTION.md', '74e3d189d317b4f6315e5ce4b526f6af8aa5b3335b3d5986669f4c53f8825786'],
  [REVIEW + '/SOURCE_INPUTS.sha256', '939a1889b21ab797b2e95c27266d0e4739e52189d1ffff7c6bfae1ead67d417f'],
  [REVIEW + '/INPUT_PINS.sha256', '98c0eb45f277415ab2213130914c8dd7f5bd43c793ef09d90e4e9dae66bc1a27']
];

function need(ok, why) { if (!ok) throw new Error(why); }
function sha(bytes) { return crypto.createHash('sha256').update(bytes).digest('hex'); }
function metadata(stat) {
  return Object.fromEntries(KEYS.map(k => [k, String(stat[k])]));
}
function same(a, b) { return JSON.stringify(a) === JSON.stringify(b); }
function absolute(path) { return path.startsWith('/') ? path : WORKSPACE + '/' + path; }
function regular(path) {
  const full = absolute(path), fd = fs.openSync(full, 'r');
  try {
    const first = fs.fstatSync(fd, {bigint: true});
    need(first.isFile(), 'not regular: ' + path);
    const bytes = fs.readFileSync(fd);
    const last = fs.fstatSync(fd, {bigint: true});
    need(same(metadata(first), metadata(last)), 'changed during read: ' + path);
    need(same(metadata(last), metadata(fs.statSync(full, {bigint: true}))),
         'path replaced during read: ' + path);
    need(BigInt(bytes.length) === last.size, 'short read: ' + path);
    return {path, kind: 'regular-file', bytes: bytes.length,
            sha256: sha(bytes), metadata: metadata(last)};
  } finally { fs.closeSync(fd); }
}
function absent(path) {
  try { fs.lstatSync(absolute(path)); }
  catch (error) {
    if (error.code === 'ENOENT') return {path, kind: 'required-absence', errno: 'ENOENT'};
    throw error;
  }
  throw new Error('required-absent path exists: ' + path);
}
function pinLines(relative, expectedCount) {
  const text = fs.readFileSync(absolute(relative), 'utf8');
  need(text.endsWith('\n'), 'pin file has no closing newline');
  const rows = text.trimEnd().split('\n').map(line => {
    need(/^[0-9a-f]{64}  [A-Za-z0-9_./-]+$/.test(line), 'bad pin row');
    const path = line.slice(66);
    need(!path.startsWith('/') && !path.split('/').includes('..'), 'bad pin path');
    return [path, line.slice(0, 64)];
  });
  need(rows.length === expectedCount, 'wrong pin count');
  need(new Set(rows.map(row => row[0])).size === rows.length, 'duplicate pin');
  return rows;
}
function writeNew(run, name, value) {
  const fd = fs.openSync(run + '/' + name, 'wx', 0o600);
  try { fs.writeFileSync(fd, JSON.stringify(value, null, 2) + '\n'); fs.fsyncSync(fd); }
  finally { fs.closeSync(fd); }
}

let run = null, submitted = false;
try {
  need(process.cwd() === WORKSPACE, 'wrong cwd');
  need(process.argv.length === 3, 'usage: node guard.js initial01');
  const runId = process.argv[2];
  need(/^(initial|strict)[0-9]{2}$/.test(runId), 'invalid run id');
  need(fs.realpathSync(__filename) === absolute(PREP + '/guard.js'), 'wrong guard path');
  fs.mkdirSync(absolute(RUNS), {recursive: true});
  const candidate = absolute(RUNS + '/' + runId);
  fs.mkdirSync(candidate, {recursive: false, mode: 0o700});
  run = candidate; // Existing directories are never adopted or overwritten.

  const grantPath = ROOT + '/GRANT.' + runId + '.json';
  const grantKey = regular(grantPath);
  const grant = JSON.parse(fs.readFileSync(absolute(grantPath), 'utf8'));
  need(same(regular(grantPath), grantKey), 'grant changed during parse');
  const selfKey = regular(PREP + '/guard.js');
  const prepKey = regular(PREP + '/PREPARATION_INPUTS.sha256');
  const command = {executable: INTERPRETER, args: SCIENCE_ARGS,
                   cwd: WORKSPACE, env: SCIENCE_ENV, stdin: '/dev/null',
                   timeout_ms: TIMEOUT_MS};
  need(grant.schema === 'P212_A_ONE_RUN_GRANT_V1' && grant.authority === 'root' &&
       grant.action === 'execute_once' && grant.run_id === runId &&
       grant.run_directory === run && grant.guard_sha256 === selfKey.sha256 &&
       grant.preparation_manifest_sha256 === prepKey.sha256 &&
       grant.source_manifest_sha256 === FIXED[3][1] &&
       same(grant.command, command), 'grant does not bind this exact submission');
  writeNew(run, 'REQUEST.json', {grant_path: grantPath, grant_key: grantKey,
           grant, command, run_id: runId, run_directory: run,
           guard_key: selfKey, preparation_manifest_key: prepKey});

  const expected = new Map();
  function add(path, hash) {
    need(!expected.has(path) || expected.get(path) === hash, 'conflicting pins');
    expected.set(path, hash);
  }
  FIXED.forEach(row => add(...row));
  add(PREP + '/PREPARATION_INPUTS.sha256', prepKey.sha256);
  add(grantPath, grantKey.sha256);
  // Check fixed policy/manifests before reading any manifest-controlled paths.
  for (const [path, hash] of expected) need(regular(path).sha256 === hash, 'fixed pin: ' + path);
  pinLines(REVIEW + '/SOURCE_INPUTS.sha256', 16).forEach(row => add(...row));
  pinLines(REVIEW + '/INPUT_PINS.sha256', 25).forEach(row => add(...row));
  pinLines(PREP + '/PREPARATION_INPUTS.sha256', 3).forEach(row => add(...row));
  const runtime = JSON.parse(fs.readFileSync(absolute(ROOT + '/RUNTIME_INPUTS.json'), 'utf8'));
  need(runtime.roles.length === 19 && runtime.roles.filter(r => r.kind === 'regular-file').length === 18,
       'runtime role census');
  need(new Set(runtime.roles.map(r => r.path)).size === 19, 'duplicate runtime role');
  const contentInputs = [...expected].sort((a, b) => a[0].localeCompare(b[0], 'en'));
  function snapshot() {
    const rows = [], errors = [], baselineChanges = [];
    for (const [path, hash] of contentInputs) {
      try {
        const row = regular(path);
        rows.push(row);
        if (row.sha256 !== hash) errors.push('input hash mismatch: ' + path);
      } catch (error) { errors.push(error.message); }
    }
    for (const role of runtime.roles) {
      try {
        const row = role.kind === 'required-absence' ? absent(role.path) : regular(role.path);
        rows.push(row);
        const fields = role.kind === 'required-absence' ? ['path', 'kind', 'errno'] :
                                                       ['path', 'kind', 'bytes', 'sha256'];
        if (!fields.every(k => row[k] === role[k])) errors.push('runtime content mismatch: ' + role.path);
        if (role.metadata && !same(row.metadata, role.metadata))
          baselineChanges.push({path: role.path, historical: role.metadata, current: row.metadata});
      } catch (error) { errors.push(error.message); }
    }
    return {schema: 'P212_A_KEYS_V1', keys: rows, errors,
            runtime_baseline_metadata_changes: baselineChanges};
  }
  const pre = snapshot();
  writeNew(run, 'PRE.json', pre);
  need(pre.errors.length === 0, 'preflight contains input errors');
  const out = fs.openSync(run + '/stdout.raw', 'wx', 0o600);
  const err = fs.openSync(run + '/stderr.raw', 'wx', 0o600);
  const input = fs.openSync('/dev/null', 'r');
  let result;
  try {
    submitted = true;
    result = child.spawnSync(INTERPRETER, SCIENCE_ARGS, {
      cwd: WORKSPACE, env: SCIENCE_ENV, stdio: [input, out, err],
      timeout: TIMEOUT_MS, killSignal: 'SIGKILL'
    });
    fs.fsyncSync(out); fs.fsyncSync(err);
  } finally { fs.closeSync(input); fs.closeSync(out); fs.closeSync(err); }
  const exit = {status: result.status, signal: result.signal,
                error: result.error ? {code: result.error.code || null,
                                       message: result.error.message} : null,
                pid: result.pid, science_submitted: submitted};
  writeNew(run, 'EXIT.json', exit);
  const post = snapshot();
  writeNew(run, 'POST.json', post);
  need(post.errors.length === 0, 'postflight contains input errors');
  need(same(pre, post), 'selected pre/post metadata or content changed');
  const stdout = regular(run + '/stdout.raw'), stderr = regular(run + '/stderr.raw');
  const completed = result.status === 0 && !result.signal && !result.error;
  writeNew(run, 'RECEIPT.json', {schema: 'P212_A_CAPTURE_V1', run_id: runId,
       ordinary_runtime_only: true, pre_post_equal: true, exit,
       stdout, stderr, execution_completed_zero: completed,
       semantic_reception: 'NOT_PERFORMED', canonical_adoption: 'NOT_AUTHORIZED'});
  need(completed, 'scientific process did not exit zero');
  console.log(JSON.stringify({status: 'CAPTURED_ZERO_EXIT_NOT_SEMANTIC_PASS', run_directory: run,
                             stdout_sha256: stdout.sha256, stdout_bytes: stdout.bytes}));
} catch (error) {
  if (run !== null) {
    try { writeNew(run, 'GUARD_FAILURE.json', {message: error.message,
              science_submitted: submitted, no_canonical_adoption: true}); }
    catch (recordError) { console.error('failure-record error: ' + recordError.message); }
  }
  console.error(error.stack || String(error));
  process.exitCode = 1;
}
