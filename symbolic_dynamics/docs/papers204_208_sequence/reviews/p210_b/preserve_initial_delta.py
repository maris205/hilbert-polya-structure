"""Physically preserve the exact initial B DELTA/seal before any replacement."""
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert dict(os.environ) == ENV and Path.cwd() == ROOT
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0
assert sys.pycache_prefix and not os.path.lexists(sys.pycache_prefix)
start = time.time()


def key(path):
    body = path.read_bytes()
    return {'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body)}


seal = HERE / 'SHA256SUMS'
assert key(seal)['sha256'] == '81b5f97a6b25d6f9e82db87001da1a54668c01268038694d4b8a3b61006b02c3'
payloads = {}
for line in seal.read_text().splitlines():
    match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
    assert match
    digest, name = match.groups()
    p = Path(name)
    assert not p.is_absolute() and '..' not in p.parts and name not in payloads and name != 'SHA256SUMS'
    actual = key(HERE / name)
    assert actual['sha256'] == digest
    payloads[name] = actual
assert len(payloads) == 407
extras = {'preserve_initial_delta.py', 'native/delta_preserve01/ATTEMPT.json',
          'native/delta_preserve01/stdout', 'native/delta_preserve01/stderr'}
physical = {p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()}
assert physical == set(payloads) | {'SHA256SUMS'} | extras
assert key(HERE / 'DELTA.md')['sha256'] == '6b59ce7b8f12206a5fe9f761e1aa1d3990c8fa66451961cd9645db63d5d9d618'
response = ROOT / 'docs/papers204_208_sequence/P210_B_RESPONSE.md'
assert key(response)['sha256'] == '10d856f1c5b0ab7aa12229c9b4262b6888b439bacaa28b0374483f9a60cf12c7'
target = HERE / 'history/initial_before_delta'
target.mkdir()
for name in ['DELTA.md', 'SHA256SUMS']:
    with (target / name).open('xb') as stream:
        stream.write((HERE / name).read_bytes())
    assert key(target / name) == key(HERE / name)
rows = []
for name, wanted in sorted(payloads.items()):
    selected = target / name if name == 'DELTA.md' else HERE / name
    assert key(selected) == wanted
    rows.append({'initial_name': name, 'original_path': str(HERE / name),
                 'physical_path': str(selected), **wanted})
rows.append({'initial_name': 'SHA256SUMS', 'original_path': str(seal),
             'physical_path': str(target / 'SHA256SUMS'), **key(target / 'SHA256SUMS')})
with (HERE / 'INITIAL_PRESERVED_PINS.sha256').open('x') as stream:
    for row in rows:
        stream.write(row['sha256'] + '  ' + str(Path(row['physical_path']).relative_to(ROOT)) + '\n')
record = {'status': 'INITIAL_PHYSICALLY_PRESERVED_BEFORE_DELTA_REPLACEMENT',
          'started_epoch': start, 'ended_epoch': time.time(), 'environment': ENV,
          'argv': sys.orig_argv, 'cwd': str(ROOT), 'source': key(Path(__file__)),
          'initial_payloads': 407, 'unchanged_in_place_payloads_after_future_delta_replacement': 406,
          'complete_preserved_roles_including_seal': 408, 'roles': rows,
          'exact_response': {'path': str(response), **key(response)},
          'current_DELTA_still_initial': True, 'current_seal_still_initial': True,
          'accepted_delta': False, 'original_failures_retained': True}
with (HERE / 'INITIAL_PRESERVATION.actual.json').open('x') as stream:
    json.dump(record, stream, sort_keys=True, indent=2)
    stream.write('\n')
print(json.dumps({'status': record['status'], 'initial_payloads': 407, 'all_physical_preserved_roles': 408,
                  'preservation_record': key(HERE / 'INITIAL_PRESERVATION.actual.json'),
                  'initial_seal': key(target / 'SHA256SUMS'), 'accepted_delta': False}, sort_keys=True))
