#!/usr/bin/env python3
"""Documentary pin check and exclusive seal; no scientific code imports."""
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
target = HERE / 'MANIFEST.sha256'
assert not target.exists() and not target.is_symlink()
before = json.loads((HERE / 'INPUT_PINS_BEFORE.json').read_bytes())
after = json.loads((HERE / 'INPUT_PINS_AFTER.json').read_bytes())
assert before == after and len(before) == 18
for name, pin in before.items():
    data = Path(name).read_bytes()
    assert len(data) == pin['bytes'] and sha256(data).hexdigest() == pin['sha256']
status = json.loads((HERE / 'RESPONSE_STATUS.json').read_bytes())
assert status['status'] == 'CORRECTIONS_SUBMITTED_SAME_REVIEWER_ACCEPTANCE_PENDING'
assert {row['id'] for row in status['findings']} == {'PTR-G-S1', 'PTR-G-C1', 'PTR-G-D1', 'PTR-G-E1'}
assert all(row['reviewer_status'] == 'OPEN' and row['resolved_by_author'] is False for row in status['findings'])
assert status['scientific_executions'] == status['new_proof_claims'] == 0
assert status['paper_number'] is None and status['admission'] is None
assert status['prior_artifacts_modified'] == [] and status['new_larger_boxes'] == []
files = []
for p in sorted(HERE.rglob('*')):
    assert not p.is_symlink()
    if p.is_file():
        assert not p.name.endswith(('.pyc', '.pyo'))
        files.append(p)
rows, total = [], 0
for path in files:
    data = path.read_bytes()
    total += len(data)
    rows.append(sha256(data).hexdigest() + '  ' + path.relative_to(HERE).as_posix() + '\n')
manifest = ''.join(rows).encode()
with target.open('xb') as stream:
    stream.write(manifest)
assert {p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()} == {
    p.relative_to(HERE).as_posix() for p in files} | {'MANIFEST.sha256'}
for p, row in zip(files, rows):
    assert sha256(p.read_bytes()).hexdigest() == row.split('  ', 1)[0]
print(json.dumps({'status': 'SEALED_AUTHOR_RESPONSE_PENDING_REVIEWER', 'payloads': len(files),
                  'payload_bytes': total, 'input_pins': len(before),
                  'manifest_sha256': sha256(manifest).hexdigest(),
                  'manifest_bytes': len(manifest), 'scientific_executions': 0,
                  'self_resolved_findings': 0}, sort_keys=True))
