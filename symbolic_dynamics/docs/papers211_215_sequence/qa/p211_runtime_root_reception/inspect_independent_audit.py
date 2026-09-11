"""Root reception of independent infrastructure evidence; no submitted import."""
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT/'docs/papers211_215_sequence/qa/p211_runtime_independent_audit'
OUT = Path(__file__).resolve().parent/'control_runtime_independent_audit'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
reads = {}


def raw(path):
    path = Path(path)
    data = path.read_bytes()
    assert not path.is_symlink()
    if str(path) in reads:
        assert reads[str(path)] == data
    reads[str(path)] = data
    return data


def value(data):
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def doc(path):
    return json.loads(raw(path))


seal = raw(BASE/'MANIFEST.sha256')
assert sha256(seal).hexdigest() == '229ceab89ee40c196b980adece6132b02f54466ff66f3ab07cc3be461a0213a3'
rows = {}
for line in seal.decode().splitlines():
    match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
    assert match
    digest, name = match.groups()
    path = Path(name)
    assert name not in rows and name != 'MANIFEST.sha256' and not path.is_absolute() and '..' not in path.parts
    rows[name] = digest
assert len(rows) == 41
assert {p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()} == set(rows) | {'MANIFEST.sha256'}
assert all(not p.is_symlink() for p in BASE.rglob('*'))
for name, pin in rows.items():
    assert sha256(raw(BASE/name)).hexdigest() == pin
before = doc(BASE/'READ_INPUTS_BEFORE.json')
assert before == doc(BASE/'READ_INPUTS_AFTER.json') and len(before) == 372
for p, pin in before.items():
    assert value(raw(p)) == pin
assert sum(p['bytes'] for p in before.values()) == 4870631
result = doc(BASE/'RESULT.json')
assert result['status'] == 'PASS_BOUNDED_INFRASTRUCTURE_ORIGINAL_INSPECTION'
assert len(doc(BASE/'CHECKS.json')) == result['checks'] == 1502
census = doc(BASE/'SAVED_NATIVE_CENSUS.json')
assert len(census) == result['saved_native_receipts'] == 53
prep = ROOT/'docs/papers211_215_sequence/qa/p211_runtime_preparation'
for row in census:
    path = prep/row['path']
    source = doc(path)
    assert all(row[k] == source[k] for k in row if k != 'path')
    for stream in ('stdout', 'stderr'):
        assert value(raw(path.with_name(stream+'.raw'))) == row[stream]
native = sorted((BASE/'native').glob('*/RECEIPT.json'))
assert len(native) == 8 == result['fresh_cmp_commands']
for p in native:
    rec, attempt = doc(p), doc(p.with_name('ATTEMPT.json'))
    assert rec['environment'] == ENV and rec['cwd'] == str(ROOT)
    assert all(rec[k] == attempt[k] for k in ('argv', 'cwd', 'environment', 'started_epoch'))
    assert rec['argv'][:2] == ['/usr/bin/cmp', '--'] and rec['exit_code'] == 0
    assert raw(rec['argv'][-2]) == raw(rec['argv'][-1])
    for stream in ('stdout', 'stderr'):
        assert raw(p.with_name(stream+'.raw')) == b'' and value(b'') == rec[stream]
    assert rec['ended_epoch'] >= rec['started_epoch']
control = doc(BASE/'TOOL_RETURN.actual.json')
assert isinstance(control, dict)
controls = {}
for name in ('SYMBOLIC_DYNAMICS_STATE.md', 'docs/papers211_215_sequence/PIPELINE_STATE.md'):
    original = ROOT/name
    assert str(original) in before
    controls[name] = raw(original)
if len(sys.argv) == 2 and sys.argv[1] == '--archive-controls':
    assert not OUT.exists() and not OUT.is_symlink()
    OUT.mkdir()
    mapping = []
    for name, data in controls.items():
        target = OUT/Path(name).name
        with target.open('xb') as stream:
            stream.write(data)
        assert target.read_bytes() == data
        mapping.append({'original': str(ROOT/name), 'copy': str(target), **value(data)})
    with (OUT/'MAPPING.json').open('xb') as stream:
        stream.write((json.dumps({'scope': 'Exact two controls before post-runtime root refresh; independent audit historical pin resolution only.', 'files': mapping}, sort_keys=True, indent=2)+'\n').encode())
else:
    assert len(sys.argv) == 1
for p, data in reads.items():
    assert Path(p).read_bytes() == data
print(json.dumps({'status': 'PASS_ROOT_INDEPENDENT_RUNTIME_AUDIT_RECEPTION',
    'audit_payloads': len(rows), 'audit_payload_bytes': sum(len(reads[str(BASE/name)]) for name in rows),
    'audit_manifest_sha256': sha256(seal).hexdigest(), 'complete_read_inputs': len(before),
    'complete_read_input_bytes': 4870631, 'archived_native_receipts': 53,
    'fresh_agent_native_raw_comparisons_received': len(native),
    'actual_root_read_paths': len(reads), 'physical_controls_created': len(controls) if len(sys.argv) == 2 else 0,
    'new_scientific_or_submitted_source_executions': 0,
    'scope': 'Complete independent audit payload and pinned originals; receives agent comparisons, does not relabel them root executions.'}, sort_keys=True, indent=2))
