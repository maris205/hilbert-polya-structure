#!/usr/bin/env python3
"""One exclusive complete nonself seal of this owned QA artifact only."""
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / 'MANIFEST.sha256'
assert not TARGET.exists() and not TARGET.is_symlink()
files = []
for path in sorted(HERE.rglob('*')):
    assert not path.is_symlink()
    if path.is_file():
        files.append(path)
assert all(not p.name.endswith(('.pyc', '.pyo')) for p in files)
lines, total = [], 0
for path in files:
    data = path.read_bytes()
    total += len(data)
    lines.append(sha256(data).hexdigest() + '  ' + path.relative_to(HERE).as_posix() + '\n')
data = ''.join(lines).encode()
with TARGET.open('xb') as stream:
    stream.write(data)
assert len(files) == len(lines)
assert {p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()} == {
    p.relative_to(HERE).as_posix() for p in files} | {'MANIFEST.sha256'}
for path, line in zip(files, lines):
    assert sha256(path.read_bytes()).hexdigest() == line.split('  ', 1)[0]
print(json.dumps({'status': 'SEALED_QA_PREPARATION_ONLY', 'payloads': len(files),
                  'payload_bytes': total, 'manifest_sha256': sha256(data).hexdigest(),
                  'manifest_bytes': len(data), 'scientific_executions': 0,
                  'production_adapter_executions': 0}, sort_keys=True))
