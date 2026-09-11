#!/usr/bin/python3.10
"""Seal this completed independent audit only, without reading its targets."""
from hashlib import sha256
import json
from pathlib import Path

base = Path(__file__).resolve().parent
manifest = base / 'MANIFEST.sha256'
assert not manifest.exists()
files = sorted(p for p in base.rglob('*') if p.is_file())
assert all(not p.is_symlink() for p in base.rglob('*'))
rows = {p.relative_to(base).as_posix(): sha256(p.read_bytes()).hexdigest() for p in files}
raw = ''.join(digest + '  ' + name + '\n' for name, digest in rows.items()).encode()
with manifest.open('xb') as stream:
    stream.write(raw)
assert {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()} == set(rows) | {'MANIFEST.sha256'}
assert all(sha256((base / name).read_bytes()).hexdigest() == digest for name, digest in rows.items())
print(json.dumps({'status': 'PASS_COMPLETE_NONSELF_AUDIT_SEAL', 'payloads': len(rows),
                  'manifest_sha256': sha256(raw).hexdigest(), 'manifest_bytes': len(raw)}, sort_keys=True))
