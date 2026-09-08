"""Read-only negative evidence reception; no scientific evaluator/import."""
from pathlib import Path, PurePosixPath
import hashlib
import json

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers211_215_sequence/scouting'


def pin(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def read(path):
    return json.loads(path.read_bytes())


def safe(base, name):
    rel = PurePosixPath(name)
    assert not rel.is_absolute() and '..' not in rel.parts and str(rel) == name
    path = base / name
    assert path.is_file() and not path.is_symlink()
    return path


base = SCOUT / 'incidence_rewiring_lane'
rows = read(base / 'MANIFEST.json')['files']
assert len(rows) == len({r['path'] for r in rows}) == 38
assert not any(p.is_symlink() for p in base.rglob('*'))
assert {r['path'] for r in rows} == {str(p.relative_to(base)) for p in base.rglob('*')
                                  if p.is_file() and p.name != 'MANIFEST.json'}
for row in rows:
    assert pin(safe(base, row['path'])) == {k: row[k] for k in ('bytes', 'sha256')}
inputs = read(base / 'INPUT_PINS.json')['inputs']
assert len(inputs) == len({r['source'] for r in inputs}) == 10
for row in inputs:
    source, snapshot = safe(ROOT, row['source']), safe(base, row['snapshot'])
    assert source.read_bytes() == snapshot.read_bytes()
    assert pin(source) == {k: row[k] for k in ('bytes', 'sha256')}
commands = read(base / 'native/COMMANDS.json')
assert len(commands) == 6 and [r['exit'] for r in commands] == [0] * 4 + [22, 22]
for i, row in enumerate(commands, 1):
    assert row == read(base / f'native/{i:02d}.record.json')
    assert row['timeout'] is False and row['cwd'] == str(base)
    assert pin(Path(row['executable'])) == row['executable_pin']
    stdout, stderr = safe(base, row['stdout']).read_bytes(), safe(base, row['stderr']).read_bytes()
    if row['argv'][0] == 'sed':
        first, last = map(int, row['argv'][2][:-1].split(','))
        assert stdout == b''.join(Path(row['argv'][3]).read_bytes().splitlines(keepends=True)[first-1:last])
    else:
        assert row['argv'][0] == 'curl' and b'403' in stderr and row['exit'] == 22
        assert not (base / row['argv'][row['argv'].index('--output') + 1]).exists()
receipt = read(base / 'native/CAPTURE_RECEIPT.json')
assert receipt['producer'] == pin(base / 'capture.py')
assert receipt['python_pin'] == pin(Path(receipt['python']))
assert receipt['input_raw_copy_pairs_checked_before_after'] == 10
assert receipt['scientific_runs'] == 0 and receipt['commands'] == 6

profile = SCOUT / 'root_profile_preflight'
counts = []
for parent, name in ((ROOT, 'HISTORY_INPUTS.sha256'), (profile, 'SHA256SUMS')):
    keys = []
    for line in (profile / name).read_text().splitlines():
        digest, rel = line.split('  ', 1)
        assert digest == pin(safe(parent, rel))['sha256']
        keys.append(rel)
    assert len(keys) == len(set(keys)) == 4
    if name == 'SHA256SUMS':
        assert set(keys) == {str(p.relative_to(profile)) for p in profile.rglob('*')
                             if p.is_file() and p.name != name}
    counts.append(len(keys))

print(json.dumps({'status': 'PASS_NEGATIVE_ARTIFACT_ONLY',
                  'incidence_payloads': 38, 'incidence_payload_bytes': sum(r['bytes'] for r in rows),
                  'incidence_seal': pin(base / 'MANIFEST.json'),
                  'incidence_raw_copy_pairs': 10, 'incidence_native_commands': commands,
                  'raw_original_stdout_slice_pairs': 4,
                  'profile_history_and_payloads': counts, 'profile_seal': pin(profile / 'SHA256SUMS'),
                  'scientific_runs': 0,
                  'limits': 'No new science, hermetic runtime, independent manuscript review or source completeness claim.'},
                 indent=2, sort_keys=True))
