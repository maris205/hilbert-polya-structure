"""Root's read-only gate reception: no gate/author scientific import or run."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers211_215_sequence/scouting'
G = SCOUT / 'kip_candidate_gate'

def read(path):
    return Path(path).read_bytes()

def pin(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def doc(path):
    return json.loads(read(path))

def check_pin(raw, row):
    assert pin(raw) == {key: row[key] for key in ('bytes', 'sha256')}

def inventory(folder, name):
    raw = read(folder / name)
    if name.endswith('.json'):
        data = json.loads(raw)
        assert data['self_excluded'] == name
        source = data['files']
    else:
        source = []
        for line in raw.decode().splitlines():
            digest, rel = line.split('  ', 1)
            source.append({'path': rel, 'sha256': digest,
                           'bytes': len(read(folder / rel))})
    result = {}
    for row in source:
        rel = row['path']
        assert rel not in result and not Path(rel).is_absolute() and '..' not in Path(rel).parts
        value = read(folder / rel)
        check_pin(value, row)
        result[rel] = value
    actual = set()
    for path in folder.rglob('*'):
        assert not path.is_symlink()
        if path.is_file() and path != folder / name:
            actual.add(path.relative_to(folder).as_posix())
    assert actual == result.keys()
    return result, {'directory': str(folder),
        'manifest': {'path': str(folder / name), **pin(raw)},
        'payload_files': len(result), 'payload_bytes': sum(map(len, result.values())),
        'payload': [{'path': row['path'], **pin(result[row['path']])} for row in source]}

g, meta = inventory(G, 'SHA256SUMS')
assert meta['payload_files'] == 78 and meta['payload_bytes'] == 2017173
assert meta['manifest']['sha256'] == '11cc87ac615849ae33718ff63edde8b43b6456343d046e4d2a19717e41eebeda'
packages = {}
for name, folder, manifest in [
    ('AUTHOR_PACKAGE_CHECK.json', 'finite_semigroup_lane', 'MANIFEST.json'),
    ('SOURCE_DESK_CHECK.json', 'kip_source_desk', 'MANIFEST.sha256'),
    ('PILOT_PACKAGE_CHECK.json', 'finite_semigroup_pilot', 'MANIFEST.json')]:
    payload, actual = inventory(SCOUT / folder, manifest)
    assert json.loads(g[name]) == actual
    packages[folder] = (payload, actual)

history = json.loads(g['HISTORICAL_PINS.json'])
assert len(history['author_historical']) == 15 and len(history['inherited']) == 2
history_rows = history['author_historical'] + history['inherited']
for row in history_rows:
    raw = g[row['gate_snapshot']]
    check_pin(raw, row)
    assert row['raw_equal'] is True and raw == read(row['source'])
    if 'author_snapshot' in row:
        assert raw == read(row['author_snapshot'])
assert g['HISTORICAL_INPUTS.sha256'] == b''.join(
    (row['sha256'] + '  ' + row['source'] + '\n').encode() for row in history_rows)
author = packages['finite_semigroup_lane'][0]
assert author['native/01.stdout'] == b''.join(g[r['gate_snapshot']] for r in history['author_historical'])
archive = json.loads(g['PILOT_ARCHIVE_PINS.json'])
assert len(archive) == 17
for row in archive:
    raw = g[row['snapshot']]
    assert row['raw_equal'] is True and raw == read(row['source'])
    check_pin(raw, row)

native_names = sorted(k for k in g if k.startswith('native/') and k.endswith('.json'))
assert len(native_names) == 7
native_rows = []
for rel in native_names:
    row = json.loads(g[rel])
    assert row['exit_code'] == 0
    assert datetime.datetime.fromisoformat(row['started_utc']) <= datetime.datetime.fromisoformat(row['ended_utc'])
    assert row['scope'] == 'documentation_source_or_archived_evidence_only'
    assert row['argv'] and Path(row['cwd']).is_dir()
    for key in ('stdout', 'stderr'):
        file = Path(row[key]['path'])
        assert file == G / Path(rel).with_suffix('.' + key)
        assert read(file) == g[file.relative_to(G).as_posix()]
        check_pin(read(file), row[key])
    native_rows.append(row)
assert native_rows[0]['argv'] == ['sha256sum', '-c', str(G / 'HISTORICAL_INPUTS.sha256')]
assert g['native/01_historical_sha.stdout'] == b''.join((r['source'] + ': OK\n').encode() for r in history_rows)
assert native_rows[1]['argv'] == ['python', 'capture.py', 'verify']
assert native_rows[2]['argv'] == ['sha256sum', '-c', 'MANIFEST.sha256']
source = packages['kip_source_desk'][0]
source_names = [line.split('  ', 1)[1] for line in read(SCOUT / 'kip_source_desk/MANIFEST.sha256').decode().splitlines()]
assert g['native/03_source_desk_seal.stdout'] == ''.join(k + ': OK\n' for k in source_names).encode()
assert native_rows[3]['argv'][:6] == ['curl', '--fail', '--location', '--max-time', '45',
 'https://repository.essex.ac.uk/24377/1/Semigroup%20Forum%20Involution%20paper%202019.pdf']
assert native_rows[4]['argv'] == ['pdftotext', '-layout', str(G/'sources/higgins_2019.pdf'), str(G/'sources/higgins_2019.txt')]
assert native_rows[5]['argv'] == ['pdftoppm', '-f', '12', '-l', '13', '-scale-to', '1500', '-png',
 str(G/'sources/higgins_2019.pdf'), str(G/'sources/higgins_page')]
assert native_rows[5]['stderr']['bytes'] == 93149
assert native_rows[6]['argv'] == ['/usr/bin/python3.10', '-I', '-S', '-B',
 str(SCOUT/'finite_semigroup_pilot/artifact_closeout_v2.py'), 'verify']
for rel in ('sources/higgins_2019.pdf', 'sources/higgins_page-12.png', 'sources/higgins_page-13.png'):
    assert g[rel].startswith(b'%PDF-' if rel.endswith('.pdf') else b'\x89PNG\r\n\x1a\n')
record = json.loads(g['PILOT_ARCHIVED_RECORD_CHECK.json'])
assert record['state_records'] == 2353 and record['input_raw_pairs'] == 98
assert record['assertion_total_from_record'] == 14523 and record['scientific_runs_by_gate'] == 0
assert record['strict_observed_runtime_prelock'] == 'FAIL_PRESERVED' and record['strict_reuse_eligible'] is False
audit = json.loads(g['AUDIT_EXEC_RETURN.json'])
assert audit['result']['exit_code'] == 0
assert json.loads(audit['result']['output']) == {'audit': 'archived_documentation_only',
 'historical_raw_pairs': 17, 'gate_native_bindings': 7, 'author_native_bindings': 3,
 'author_full_snapshot_concat_raw_equal': True, 'scientific_executions_by_gate': 0}
assert inventory(G, 'SHA256SUMS') == (g, meta)
print(json.dumps({'status': 'PASS_ROOT_GATE_ORIGINALS_ONLY', 'payloads': 78,
 'payload_bytes': 2017173, 'historical_raw_pairs': 17, 'pilot_raw_pairs': 17,
 'native_records': 7, 'author_source_pilot_payloads': [39, 12, 119],
 'strict_pilot_failure': 'FAIL_PRESERVED', 'new_science': 0,
 'root_actual_higgins_pages_viewed': [12, 13], 'manuscript_reviews': 0}, sort_keys=True))
