'use strict';
// Documentary file reader only. Never imports or executes submitted sources.
const fs = require('fs');
const crypto = require('crypto');
const path = require('path');
const root = '/root/autodl-tmp/symbolic_dynamics';
const preparation = 'docs/papers211_215_sequence/qa/private_checkpoint_d01_preparation01';
const names = ['CLOSING_NATIVE.json', 'CONTRACT.md', 'DOCUMENTARY_CHECKS.json',
  'DOCUMENT_READS_NATIVE.json', 'GRANT.disabled.json', 'HANDOFF.md',
  'HISTORICAL_ROLE_KEYS.json', 'INPUT_CHECKS_NATIVE.json', 'INPUT_PINS.sha256',
  'PRIMARY_REQUESTS.json', 'PROSPECTIVE_REQUEST.disabled.json', 'SHA256SUMS',
  'SOURCE_READS_NATIVE.json', 'launch.py'];
const context = [
  'docs/papers211_215_sequence/qa/private_checkpoint_executor_ssh_root04/RECEPTION.md',
  'docs/papers211_215_sequence/qa/private_checkpoint_executor_ssh_root04/SHA256SUMS',
  'docs/papers211_215_sequence/qa/private_checkpoint_executor_ssh_delta04/SOURCE_CONTRACT.md',
  'docs/papers211_215_sequence/qa/private_checkpoint_executor_ssh_audit04/REPORT.md'
];
function need(ok, message) { if (!ok) throw new Error(message); }
const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
function meta(s) { return Object.fromEntries(fields.map(f => [f, s[f].toString()])); }
function hash(b) { return crypto.createHash('sha256').update(b).digest('hex'); }
function read(rel) {
  need(!path.isAbsolute(rel) && rel.split('/').every(x => x && x !== '.' && x !== '..'),
    'Invalid relative document path');
  const full = path.join(root, rel);
  const before = fs.lstatSync(full, {bigint:true});
  need(before.isFile() && !before.isSymbolicLink(), 'Not a physical document');
  const fd = fs.openSync(full, fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW);
  try {
    const opened = fs.fstatSync(fd, {bigint:true});
    need(JSON.stringify(meta(before)) === JSON.stringify(meta(opened)), 'Open changed');
    const body = fs.readFileSync(fd);
    const ended = fs.fstatSync(fd, {bigint:true});
    const after = fs.lstatSync(full, {bigint:true});
    need(JSON.stringify(meta(before)) === JSON.stringify(meta(ended))
      && JSON.stringify(meta(before)) === JSON.stringify(meta(after))
      && BigInt(body.length) === before.size, 'Document changed while read');
    return {key:{path:rel,bytes:body.length,sha256:hash(body),metadata:meta(before)},body};
  } finally { fs.closeSync(fd); }
}
need(process.argv.length === 3 && process.argv[2] === 'inventory', 'Inventory only');
const actualNames = fs.readdirSync(path.join(root, preparation)).sort();
need(JSON.stringify(actualNames) === JSON.stringify(names.slice().sort()), 'Input membership');
const rows = names.map(name => read(preparation + '/' + name));
const manifest = rows.find(r => r.key.path.endsWith('/SHA256SUMS'));
need(manifest.key.sha256 === 'bc61e43e136281c0ea4e55809d26d0e34e92a9e88dd6bd4d1a06e1157e5d82ee',
 'Root expected manifest key differs');
const lines = manifest.body.toString('utf8').trimEnd().split('\n');
need(lines.length === 13, 'Expected thirteen payloads');
for (const line of lines) {
  const m = /^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);
  need(m && m[2] !== 'SHA256SUMS', 'Manifest syntax/self');
  const row = rows.find(r => r.key.path === preparation + '/' + m[2]);
  need(row && row.key.sha256 === m[1], 'Payload mismatch');
}
need(new Set(lines.map(x => x.slice(66))).size === 13, 'Repeated payload');
const launcher = rows.find(r => r.key.path.endsWith('/launch.py'));
need(launcher.key.bytes === 17513
 && launcher.key.sha256 === 'b1b39b9ce36f9c7ace171229c6e69ba236e888bf2664e81eab9d557fd69468ce'
 && launcher.body.toString('utf8').split('\n').length - 1 === 327, 'Expected launcher');
const payloadBytes = rows.reduce((s, r) => s+r.key.bytes, 0);
need(payloadBytes === 159985, 'Root expected total bytes');
const oldPins = rows.find(r => r.key.path.endsWith('/INPUT_PINS.sha256')).body.toString('utf8').trimEnd().split('\n');
need(oldPins.length === 14, 'Expected fourteen author input pins');
const referenced = [];
for(const line of oldPins) {
  const m = /^([0-9a-f]{64})  (docs\/[A-Za-z0-9_./-]+)$/.exec(line);
  need(m, 'Historical pin format');
  const r = read(m[2]);
  need(r.key.sha256 === m[1], 'Historical pinned input changed');
  referenced.push(r.key);
}
for(const name of names.filter(n => n.endsWith('.json')))
  JSON.parse(rows.find(r => r.key.path.endsWith('/'+name)).body.toString('utf8'));
const contextual = context.map(rel => read(rel).key);
process.stdout.write(JSON.stringify({
  scope:'Documentary bytes and finite package keys; submitted source never executed or parsed as code',
  package_file_count: rows.length, package_payload_count: lines.length,
  package_bytes:payloadBytes, launcher_lines:327,
  input_package:rows.map(r=>r.key), author_referenced_inputs:referenced,
  context_inputs:contextual
}, null, 2)+'\n');

