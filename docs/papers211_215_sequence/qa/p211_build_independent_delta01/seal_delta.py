#!/usr/bin/python3.10
"""Seal the completed independent delta report only; no target execution."""
from hashlib import sha256
import json
from pathlib import Path

base = Path(__file__).resolve().parent
manifest = base / 'SHA256SUMS'
assert not manifest.exists() and all(not p.is_symlink() for p in base.rglob('*'))
load = lambda p: json.loads(p.read_bytes())
assert load(base / 'READ_INPUTS_BEFORE.json') == load(base / 'READ_INPUTS_AFTER.json')
result = load(base / 'RESULT.json')
actual = load(base / 'TOOL_RETURN.actual.json')['returned']
assert actual['exit_code'] == 0 and json.loads(actual['output']) == result
assert result['status'] == 'BLD_I1_RESOLVED_FOR_REVISION01_PENDING_EXACT_ROOT_BINDING'
attempts = sorted((base / 'native').rglob('ATTEMPT.json'))
assert len(attempts) == 10
for p in attempts:
    row = load(p.with_name('RECEIPT.json'))
    assert all(row[k] == v for k, v in load(p).items())
    assert row['native_exit_code'] in row['expected_exit_codes']
    for name in ('stdout', 'stderr'):
        raw = p.with_name(name + '.raw').read_bytes()
        assert row[name] == {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}
rows = {p.relative_to(base).as_posix(): sha256(p.read_bytes()).hexdigest()
        for p in sorted(base.rglob('*')) if p.is_file()}
raw = ''.join(digest + '  ' + name + '\n' for name, digest in rows.items()).encode()
with manifest.open('xb') as stream:
    stream.write(raw)
assert {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()} == set(rows) | {'SHA256SUMS'}
assert all(sha256((base / name).read_bytes()).hexdigest() == digest for name, digest in rows.items())
print(json.dumps({'status': 'PASS_COMPLETE_NONSELF_INDEPENDENT_DELTA_SEAL',
                  'payloads': len(rows), 'manifest_bytes': len(raw),
                  'manifest_sha256': sha256(raw).hexdigest(),
                  'finding': 'BLD-I1 resolved only for revision01; original report unchanged; exact root binding pending'}, sort_keys=True))
