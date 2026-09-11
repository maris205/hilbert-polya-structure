"""Read-only OM archive reception, no map implementation or scientific calls."""
from pathlib import Path, PurePosixPath
import hashlib
import json

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers211_215_sequence/scouting/queue_transfer_lane'


def pin(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def safe(base, name):
    rel = PurePosixPath(name)
    assert not rel.is_absolute() and '..' not in rel.parts and str(rel) == name
    path = base / name
    assert path.is_file() and not path.is_symlink()
    return path


manifest = json.loads((BASE / 'MANIFEST.json').read_bytes())
rows = manifest['files']
assert len(rows) == len({r['path'] for r in rows}) == 31
assert not any(p.is_symlink() for p in BASE.rglob('*'))
assert {str(p.relative_to(BASE)) for p in BASE.rglob('*') if p.is_file()} == {
    'MANIFEST.json', *(r['path'] for r in rows)}
for row in rows:
    assert pin(safe(BASE, row['path'])) == {k: row[k] for k in ('bytes', 'sha256')}
inputs = json.loads((BASE / 'HISTORY_PINS.json').read_bytes())
assert len(inputs) == len({r['source'] for r in inputs}) == 10
controls = {'SYMBOLIC_DYNAMICS_STATE.md', 'docs/papers211_215_sequence/PIPELINE_STATE.md'}
assert {r['source'] for r in inputs if r['source'] in controls} == controls
for row in inputs:
    snapshot = safe(BASE, row['snapshot'])
    assert pin(snapshot) == {k: row[k] for k in ('bytes', 'sha256')}
    assert row['raw_equal'] is True
    if row['source'] not in controls:
        assert snapshot.read_bytes() == safe(ROOT, row['source']).read_bytes()
    else:
        preview = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_preparation02/controls_preview34' / Path(row['source']).name
        assert snapshot.read_bytes() == preview.read_bytes()
commands = []
for i in range(1, 4):
    row = json.loads((BASE / 'native' / f'{i:02d}.json').read_bytes())
    assert row['exit_code'] == (1 if i == 1 else 0)
    assert row['cwd'] == str(BASE if i == 2 else ROOT)
    for stream in ('stdout', 'stderr'):
        assert pin(BASE / 'native' / f'{i:02d}.{stream}') == row[stream]
    assert (BASE / 'native' / f'{i:02d}.stderr').read_bytes() == b''
    commands.append(row)
assert (BASE / 'native/01.stdout').read_bytes() == b''
assert (BASE / 'native/02.stdout').read_bytes() == b''.join(
    safe(BASE, r['snapshot']).read_bytes() for r in inputs)
assert commands[1]['argv'] == ['cat', *(r['snapshot'] for r in inputs)]
print(json.dumps({'status': 'PASS_NEGATIVE_ARTIFACT_ONLY', 'payloads': len(rows),
                  'payload_bytes': sum(r['bytes'] for r in rows), 'seal': pin(BASE / 'MANIFEST.json'),
                  'snapshots_checked': 10, 'unchanged_live_raw_pairs': 8,
                  'exact_preview34_control_raw_pairs': 2, 'native_commands': commands,
                  'complete_raw_concatenation_equal': True, 'scientific_executions': 0,
                  'limits': 'Archive inspection only; no scientific replay, source PDF byte archive, page viewing or hermetic runtime claim.'},
                 indent=2, sort_keys=True))
