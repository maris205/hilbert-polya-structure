#!/usr/bin/env python3
"""Exclusive source-preparation seal; no receiver import or execution."""
from hashlib import sha256
import json
from pathlib import Path

base = Path(__file__).resolve().parent
target = base / 'MANIFEST.sha256'
assert not target.exists() and not target.is_symlink()
record = json.loads((base / 'DOCUMENTARY_CHECK.json').read_bytes())
assert record['status'] == 'PASS_DOCUMENTARY_SOURCE_PREPARATION_ONLY'
assert record['inputs_before'] == record['inputs_after']
for path, pin in record['inputs_before'].items():
    data = Path(path).read_bytes()
    assert len(data) == pin['bytes'] and sha256(data).hexdigest() == pin['sha256']
source = (base / 'receive_output.py').read_bytes()
assert {'sha256': sha256(source).hexdigest(), 'bytes': len(source)} == record['receiver_pin']
files = sorted(p for p in base.rglob('*') if p.is_file())
assert all(not p.is_symlink() for p in base.rglob('*'))
assert all(not p.name.endswith(('.pyc', '.pyo')) for p in files)
rows, total = [], 0
for path in files:
    data = path.read_bytes()
    total += len(data)
    rows.append(sha256(data).hexdigest() + '  ' + path.relative_to(base).as_posix() + '\n')
raw = ''.join(rows).encode()
with target.open('xb') as stream:
    stream.write(raw)
for path, row in zip(files, rows):
    assert sha256(path.read_bytes()).hexdigest() == row.split('  ', 1)[0]
assert {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()} == {
    p.relative_to(base).as_posix() for p in files} | {'MANIFEST.sha256'}
print(json.dumps({'status': 'SEALED_SOURCE_PREPARATION_ONLY', 'payloads': len(files),
                  'payload_bytes': total, 'manifest_sha256': sha256(raw).hexdigest(),
                  'manifest_bytes': len(raw), 'receiver_executions': 0,
                  'saved_output_reads': 0, 'scientific_executions': 0}, sort_keys=True))
