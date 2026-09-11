// Author documentary integrity/text check only. Never evaluates reviewed source.
'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const base = 'docs/papers211_215_sequence/qa/p213_minimal_observer_source01/';
let checks = 0;
function ok(value, message) { checks++; if (!value) throw new Error(message); }
const fields = ['dev', 'ino', 'mode', 'nlink', 'uid', 'gid', 'rdev', 'size', 'mtimeNs', 'ctimeNs'];
function stat(s) {
  return Object.fromEntries(fields.map(k => { ok(typeof s[k] === 'bigint', 'integer ' + k); return [k, String(s[k])]; }));
}
const keys = new Map();
function read(path) {
  const a = fs.lstatSync(path, {bigint:true});
  ok(a.isFile() && !a.isSymbolicLink(), 'document regular ' + path);
  const fd = fs.openSync(path, fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK);
  let body;
  let before;
  let after;
  try {
    const fdStat = fs.fstatSync(fd, {bigint:true});
    ok(fdStat.isFile(), 'document fd regular');
    before = stat(fdStat);
    ok(JSON.stringify(before) === JSON.stringify(stat(a)), 'path/fd before');
    body = fs.readFileSync(fd);
    after = stat(fs.fstatSync(fd, {bigint:true}));
  } finally { fs.closeSync(fd); }
  ok(JSON.stringify(before) === JSON.stringify(after), 'document fd changed');
  ok(JSON.stringify(before) === JSON.stringify(stat(fs.lstatSync(path, {bigint:true}))), 'document path changed');
  ok(BigInt(body.length) === BigInt(before.size), 'whole documentary read');
  const key = {path, bytes:body.length, sha256:crypto.createHash('sha256').update(body).digest('hex'), metadata:before};
  if (keys.has(path)) ok(JSON.stringify(keys.get(path)) === JSON.stringify(key), 'repeat key changed');
  keys.set(path, key);
  return body;
}
function json(name) { return JSON.parse(read(base + name).toString('utf8')); }
function text(name) { return read(base + name).toString('utf8'); }
const pins = text('INPUTS.sha256');
ok(pins.endsWith('\n') && !pins.endsWith('\n\n'), 'single terminal LF');
const lines = pins.trimEnd().split('\n');
ok(lines.length === 9, 'nine explicit archival inputs');
const inputs = new Map();
for (const line of lines) {
  const match = /^([a-f0-9]{64})  ([A-Za-z0-9_./-]+)$/.exec(line);
  ok(match && !match[2].startsWith('/') && !match[2].includes('..'), 'strict pin format');
  ok(!inputs.has(match[2]), 'unique pin');
  const body = read(match[2]);
  ok(crypto.createHash('sha256').update(body).digest('hex') === match[1], 'input pin');
  inputs.set(match[2], body);
}
const sourceReads = json('SOURCE_READS_NATIVE.json').records;
ok(sourceReads.length === 10, 'nine reads and one failure');
let rawInputBytes = 0;
let readCount = 0;
for (const record of sourceReads) {
  if (record.result.exit_code !== 0) {
    ok(record.result.exit_code === 2 && record.path.endsWith('/SOURCE_INPUTS.sha256'), 'preserved wrong filename failure');
    continue;
  }
  ok(inputs.has(record.path), 'read is selected input');
  ok(record.request.cmd === "sed -n '1,2400p' " + record.path, 'whole read command');
  const actual = Buffer.from(record.result.output, 'utf8');
  ok(inputs.get(record.path).equals(actual), 'raw full input read');
  rawInputBytes += actual.length;
  readCount++;
}
ok(readCount === 9, 'complete selected inputs');
const finalReads = json('FINAL_READS_NATIVE.json').records;
ok(finalReads.length === 7, 'seven source/interface readbacks');
let rawSourceBytes = 0;
for (const record of finalReads) {
  ok(record.path.startsWith(base) && record.result.exit_code === 0, 'final read scope/exit');
  const actual = Buffer.from(record.result.output, 'utf8');
  ok(read(record.path).equals(actual), 'raw final source/interface read');
  rawSourceBytes += actual.length;
}
ok(rawSourceBytes === 46256, 'exact seven bodies byte total');
const source = text('observe.py');
const imports = source.split('\n').filter(line => /^\s*(import|from)\s+/.test(line)).map(line => line.trim());
ok(JSON.stringify(imports) === JSON.stringify(['import sys', 'import os', 'import hashlib', 'import json']), 'four declared imports');
const ordered = ['BINDING = None', 'import sys', 'EARLY_MODULES = module_snapshot("early")',
  'EARLY_MAPS = raw_maps("early_pre_helpers")', 'SECOND_MODULES = module_snapshot("second_prehelper")',
  '    import os', '    import hashlib', '    import json'];
for (let i = 1; i < ordered.length; i++) ok(source.indexOf(ordered[i-1]) < source.indexOf(ordered[i]), 'literal phase order');
for (const literal of ['("missing",)', '("null",)', 'kind = loader if is_class else type(loader)',
  'name == "__main__" and spec == ("null",)', '"os.environ_cached_mapping"', '"close_failure"',
  '"late_unkeyed_module"', '"late_unkeyed_map"', '"deleted_mapping"', '"nonregular_fd"',
  '"closing_file_or_absence_changed"', '"sha256_of_read_bytes"', '"OBSERVED_PENDING_INDEPENDENT_RECEPTION"',
  '"runtime_accepted": False', 'os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC']) ok(source.includes(literal), 'source literal ' + literal);
for (const field of ['st_dev','st_ino','st_mode','st_nlink','st_uid','st_gid','st_rdev','st_size','st_mtime_ns','st_ctime_ns']) {
  ok(source.slice(source.indexOf('FIELDS ='), source.indexOf('EARLY =')).includes('"' + field + '"'), 'ten-field declaration');
}
for (const forbidden of ['subprocess.', 'os.system(', '__import__(', 'find_spec(', 'reload_environ(', 'statx(', 'eval(', 'exec(', 'compile(']) {
  ok(!source.includes(forbidden), 'no prohibited source operation token');
}
const binding = json('BINDING.disabled.json');
const capture = json('CAPTURE_REQUEST.disabled.json');
ok(binding.enabled === false && binding.operation_authorized === false, 'binding disabled');
ok(capture.enabled === false && capture.operation_authorized === false, 'capture disabled');
for (const name of ['env','bash','capture_mkdir','interpreter','cwd','launch_record','flag_names','modules','loader_ids','special_maps','files']) ok(binding[name] === null, 'unresolved ' + name);
ok(Object.values(binding.bounds).every(value => value === null), 'all numeric bounds unresolved');
ok(Object.values(binding.module_names).every(value => value === null), 'module sets unresolved');
ok(capture.request.cmd === null && capture.request.workdir === null && capture.request.login === false && capture.request.tty === false, 'native request disabled');
ok(JSON.stringify(binding.child_environment) === JSON.stringify({LANG:'C', LC_ALL:'C'}), 'literal child environment');
const shell = text('capture.disabled.sh');
ok(shell.indexOf('\nexit 78\n') < shell.indexOf('umask 077'), 'capture unconditional gate');
ok(shell.includes('"$P213_CAPTURE_MKDIR" -m 700 -- "$P213_CAPTURE_DIRECTORY" || exit 78'), 'exclusive nonrecursive directory request');
ok(shell.includes('1>&3 2>&4 3>&- 4>&-'), 'separate stream descriptors');
ok(!shell.includes('/dev/null') && !shell.includes('rm ') && !shell.includes('kill '), 'no device/cleanup/controller');
ok(text('CONTRACT.md').includes('This author cannot independently audit its own source or runtime.'), 'author boundary');
ok(text('SELECTION_REQUEST.md').includes('exact workspace-relative filename'), 'finite selection request');
const before = [...keys.values()];
for (const key of before) read(key.path);
process.stdout.write(JSON.stringify({status:'DOCUMENTARY_CHECK_ONLY', checks, source_audit:false,
  runtime_observed:false, python_or_reviewed_shell_executed:false, selected_inputs:inputs.size,
  raw_input_read_bytes:rawInputBytes, raw_source_read_bytes:rawSourceBytes,
  keys:[...keys.values()]}, null, 2) + '\n');
