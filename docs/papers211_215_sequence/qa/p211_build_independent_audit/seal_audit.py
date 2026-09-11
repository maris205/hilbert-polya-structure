#!/usr/bin/python3.10
"""Seal this completed independent audit only; never reads original targets."""
from hashlib import sha256
import json
from pathlib import Path

base = Path(__file__).resolve().parent
manifest = base / 'SHA256SUMS'
assert not manifest.exists() and all(not p.is_symlink() for p in base.rglob('*'))
rows = {p.relative_to(base).as_posix(): sha256(p.read_bytes()).hexdigest()
        for p in sorted(base.rglob('*')) if p.is_file()}
raw = ''.join(digest + '  ' + name + '\n' for name, digest in rows.items()).encode()
with manifest.open('xb') as stream:
    stream.write(raw)
assert {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()} == set(rows) | {'SHA256SUMS'}
assert all(sha256((base / name).read_bytes()).hexdigest() == digest for name, digest in rows.items())
print(json.dumps({'status': 'PASS_COMPLETE_NONSELF_FINDING_PACKAGE_SEAL', 'payloads': len(rows),
                  'manifest_sha256': sha256(raw).hexdigest(), 'finding': 'BLD-I1 remains Major/open'}, sort_keys=True))
