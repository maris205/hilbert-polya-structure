"""Root read-only original-package closure; never launches a map producer."""
from pathlib import Path
import contextlib
import hashlib
import io
import json
import runpy
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_seventh'
SEAL = '64e07617dd97aaec2995a1c647554469ad9c97bab46d5151cef3af029abe001f'
seen = {}

def read(path):
    path = Path(path)
    assert path.is_file() and not path.is_symlink(), str(path)
    data = path.read_bytes()
    value = hashlib.sha256(data).hexdigest()
    assert str(path) not in seen or seen[str(path)] == value, str(path)
    seen[str(path)] = value
    return data

def load(path):
    return json.loads(read(path))

def closure():
    manifest = read(BASE / 'SHA256SUMS')
    assert hashlib.sha256(manifest).hexdigest() == SEAL
    rows = {}
    for line in manifest.decode().splitlines():
        value, name = line.split('  ', 1)
        p = Path(name)
        assert not p.is_absolute() and '..' not in p.parts and name not in rows
        assert name != 'SHA256SUMS'
        assert hashlib.sha256(read(BASE / p)).hexdigest() == value
        rows[name] = value
    entries = list(BASE.rglob('*'))
    assert all(not p.is_symlink() for p in entries)
    assert {p.relative_to(BASE).as_posix() for p in entries if p.is_file()} == set(rows) | {'SHA256SUMS'}
    assert len(rows) == 148
    return rows

before = closure()
audit_capture = io.StringIO()
sys.argv = [str(BASE / 'audit.py'), '--manifest']
with contextlib.redirect_stdout(audit_capture):
    audit = runpy.run_path(str(BASE / 'audit.py'), run_name='__main__')
audit_raw = audit_capture.getvalue()
result = json.loads(audit_raw)
assert result['status'] == 'PASS_AUTHOR_ARTIFACT_AND_ORIGINAL_OUTPUT_AUDIT'
assert result['counts']['manifest_payloads'] == 148
assert result['counts']['map_rows'] == 2743
assert result['counts']['independent_support_targets'] == 349
for name, value in audit['observed'].items():
    assert hashlib.sha256(read(name)).hexdigest() == value

run_inputs = []
for serial in (1, 2):
    folder = BASE / f'execution/run_{serial}'
    receipt = load(folder / 'receipt.json')
    assert receipt['exit'] == 0 and receipt['inputs_equal'] is True
    assert receipt['stdin'] == 'DEVNULL' and receipt['close_fds'] is True
    assert receipt['env'] == {'PATH': '/root/miniconda3/bin:/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8'}
    prefix = BASE / f'execution/capsule_{serial}/absent_pycache_prefix'
    assert receipt['argv'] == ['/root/miniconda3/bin/python3', '-I', '-S', '-B', '-X', f'pycache_prefix={prefix}', str(BASE / f'execution/capsule_{serial}/source/pilot.py')]
    assert not prefix.exists() and not prefix.is_symlink()
    pins = load(folder / 'inputs_before.json')
    assert pins == load(folder / 'inputs_after.json') and len(pins) == receipt['input_count'] == 886
    covered = {row['resolved'] for row in pins}
    modules = load(folder / 'observed_modules.json')
    assert modules and all(row['covered'] and row['resolved'] in covered for row in modules)
    stderr = read(folder / 'stderr.bin').decode()
    assert [(row['name'], row['path']) for row in modules] == [tuple(line.split(' ', 2)[1:]) for line in stderr.splitlines() if line.startswith('MODULE ')]
    assert 'optimize=0' in stderr and 'isolated=1' in stderr and 'no_site=1' in stderr
    run_inputs.append(len(pins))
presence = load(BASE / 'execution/config_presence_before.json')
assert presence == load(BASE / 'execution/config_presence_after.json')
for row in presence:
    p = Path(row['path'])
    assert p.exists() == row['exists'] and p.is_file() == row['is_file']

comparisons = []
canonical = BASE / 'execution/CANONICAL.txt'
one, two = (BASE / f'execution/run_{serial}/stdout.bin' for serial in (1, 2))
for a, b in ((one, two), (one, canonical), (two, canonical)):
    argv = ['/usr/bin/cmp', '--', str(a), str(b)]
    read('/usr/bin/cmp')
    proc = subprocess.run(argv, cwd=ROOT, env={'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8'}, capture_output=True, stdin=subprocess.DEVNULL)
    row = {'argv': argv, 'exit': proc.returncode, 'stdout': proc.stdout.decode(), 'stderr': proc.stderr.decode()}
    comparisons.append(row)
    assert proc.returncode == 0 and proc.stdout == proc.stderr == b''
assert closure() == before
for name, value in list(seen.items()):
    assert hashlib.sha256(read(name)).hexdigest() == value
print(json.dumps({'status': 'PASS_ROOT_SCOUT27_ORIGINAL_CLOSURE_NO_PROMOTION',
    'package_payloads': len(before), 'seal_sha256': SEAL,
    'actual_original_auditor_stdout': audit_raw, 'original_auditor_result': result,
    'original_run_input_counts': run_inputs, 'root_raw_comparisons': comparisons,
    'current_read_paths_rechecked_twice': len(seen),
    'scope': 'New root read-only artifact/original-output audit and raw comparisons, not a new map producer, independent candidate gate or strict terminal runtime reuse.'}, indent=2, sort_keys=True))
