#!/usr/bin/env python3
"""Generate a complete nonself preparation seal; never invokes Git."""
import hashlib
import json
from pathlib import Path

base = Path(__file__).resolve().parent
target = base / 'MANIFEST.sha256'
assert not target.exists(), 'Preserve any earlier preparation seal.'
files = sorted(p for p in base.rglob('*') if p.is_file() and p != target)
assert not any(p.is_symlink() for p in base.rglob('*'))
assert sum(p.stat().st_size for p in files) < 10_000_000
rows = [(hashlib.sha256(p.read_bytes()).hexdigest(), p.relative_to(base).as_posix()) for p in files]
with target.open('x') as stream:
    stream.writelines(digest + '  ' + name + '\n' for digest, name in rows)
for digest, name in rows:
    assert hashlib.sha256((base / name).read_bytes()).hexdigest() == digest
print(json.dumps({'status': 'PASS_PREPARATION_SEAL_ONLY', 'payloads': len(rows),
                  'bytes': sum(p.stat().st_size for p in files),
                  'manifest_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
                  'checkpoint_phases_executed': 0}))
