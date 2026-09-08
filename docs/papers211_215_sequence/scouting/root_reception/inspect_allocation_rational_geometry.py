"""Read-only root evidence reception. No science, subprocess, or author import."""
from pathlib import Path, PurePosixPath
import base64
import hashlib
import json

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers211_215_sequence/scouting'


def pin_bytes(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def pin(path):
    return pin_bytes(path.read_bytes())


def read(path):
    return json.loads(path.read_bytes())


def safe(base, name):
    rel = PurePosixPath(name)
    assert not rel.is_absolute() and '..' not in rel.parts and str(rel) == name
    path = base / name
    assert path.is_file() and not path.is_symlink()
    return path


def sha_list(base, path, expected):
    rows = []
    for line in path.read_text().splitlines():
        digest, name = line.split('  ', 1)
        actual = pin(safe(base, name))
        assert actual['sha256'] == digest, name
        rows.append({'path': name, **actual})
    assert len(rows) == len({r['path'] for r in rows}) == expected
    return rows


def manifest(base, name, expected):
    if name.endswith('.json'):
        rows = read(base / name)['files']
        assert len(rows) == len({r['path'] for r in rows}) == expected
        for row in rows:
            assert pin(safe(base, row['path'])) == {k: row[k] for k in ('bytes', 'sha256')}
    else:
        rows = sha_list(base, base / name, expected)
    assert not any(p.is_symlink() for p in base.rglob('*'))
    actual = {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()}
    assert actual == {name, *(r['path'] for r in rows)}
    return {'payloads': len(rows), 'bytes': sum(r['bytes'] for r in rows),
            'seal': pin(base / name)}


allocation = SCOUT / 'finite_allocation_lane'
allocation_result = manifest(allocation, 'SHA256SUMS', 60)
sha_list(ROOT, allocation / 'HISTORICAL_INPUTS.sha256', 8)
evidence = allocation / 'evidence01'
for row in read(evidence / 'original_capture.json'):
    data = safe(ROOT, row['path']).read_bytes()
    assert data == safe(evidence / 'originals', row['path']).read_bytes()
    assert pin_bytes(data) == {k: row[k] for k in ('bytes', 'sha256')}
inputs = read(evidence / 'PILOT_INPUTS.json')
assert len(inputs) == 4
for row in inputs:
    data = safe(allocation, row['path']).read_bytes()
    assert data == safe(evidence / 'pilot_inputs', row['path']).read_bytes()
    assert pin_bytes(data) == {k: row[k] for k in ('bytes', 'sha256')}
runtime = read(evidence / 'PILOT_RUNTIME.json')
assert pin(Path(runtime['python']))['sha256'] == runtime['python_sha256']
allocation_commands = []
for path in sorted(evidence.glob('*.command.json')):
    stem = path.name.removesuffix('.command.json')
    command = read(path)
    result = read(evidence / (stem + '.result.json'))
    assert command['cwd'] == str(ROOT) and result['returncode'] == 0
    for stream in ('stdout', 'stderr'):
        assert pin(evidence / (stem + '.' + stream)) == {
            k: result[stream + '_' + k] for k in ('bytes', 'sha256')}
    stderr = (evidence / (stem + '.stderr')).read_bytes()
    expected_stderr = (b'Syntax Warning: Bad bounding box in Type 3 glyph\n'
                       if stem == '04_distinct_blocks_page2' else b'')
    assert stderr == expected_stderr
    allocation_commands.append({'stem': stem, **command, **result})
assert len(allocation_commands) == 7
records = [json.loads(line) for line in (evidence / '05_sole_pilot.stdout').read_bytes().splitlines()]
summary = read(evidence / 'pilot_summary.json')
assert records[-1] == {'kind': 'summary', **summary}
assert len(records) == 5705 and summary['state_count'] == 5704
assert summary['deductive_assertions'] == 17919 and len(summary['boxes']) == 30
assert summary['scientific_executions_in_this_lane'] == 1
assert summary['constant_max_proved_all_parameters'] is False
keys = [(r['m'], r['N'], tuple(r['state'])) for r in records[:-1]]
assert len(keys) == len(set(keys)) == 5704
assert all(r['kind'] == 'state' for r in records[:-1])
for box in summary['boxes']:
    archived = [r for r in records[:-1] if (r['m'], r['N']) == (box['m'], box['N'])]
    assert len(archived) == box['states'] == box['m'] ** box['N']
    assert all(len(r['state']) == box['N'] and all(0 <= x < box['m'] for x in r['state'])
               for r in archived)
allocation_result.update({'historical_raw_pairs': 8, 'frozen_pilot_input_raw_pairs': 4,
                          'archived_records': 5704, 'archived_assertions': 17919,
                          'native_commands': allocation_commands})

rational = SCOUT / 'rational_coupling_lane'
rational_result = manifest(rational, 'MANIFEST.sha256', 47)
sha_list(ROOT, rational / 'INPUT_PINS.sha256', 12)
native = rational / 'native02'
receipt = read(native / 'receipt.json')
assert receipt['scientific_runs'] == 0 and receipt['command_contract_pass']
assert len(receipt['commands']) == 10
for row in receipt['commands']:
    assert row['returncode'] == 0 and row['returncode'] in row['accepted_codes']
    safe(native, row['stdout']).read_bytes()
    assert safe(native, row['stderr']).read_bytes() == b''
assert pin(rational / receipt['source']['path'])['sha256'] == receipt['source']['sha256']
assert pin(Path(receipt['interpreter']['path']))['sha256'] == receipt['interpreter']['sha256']
for path, digest in receipt['tool_pins'].items():
    assert pin(Path(path))['sha256'] == digest
pins = (rational / 'INPUT_PINS.sha256').read_bytes()
assert pins == (native / 'historical_before.stdout.raw').read_bytes()
assert pins == (native / 'historical_after.stdout.raw').read_bytes()
assert pins == (rational / 'native/historical_before.stdout.raw').read_bytes()
assert (native / 'historical_compare.stdout.raw').read_bytes() == b''
assert len(receipt['control_snapshots']) == 2
for row in receipt['control_snapshots']:
    assert pin(safe(rational, row['snapshot']))['sha256'] == row['sha256']
    # The original controls may legitimately advance after this reception.
    # Their immutable physical bytes, not future live controls, are input roles.
assert len(receipt['source_fetches']) == 2
for row in receipt['source_fetches']:
    assert row['curl_exit'] == row['extraction_exit'] == 0
    assert row['http_observation'].splitlines()[0] == '200'
    pdf = safe(rational, row['path'])
    assert pin(pdf) == {k: row[k] for k in ('bytes', 'sha256')}
    assert pdf.read_bytes().startswith(b'%PDF-')
    assert (native / ('fetch_' + row['label'] + '.stdout.raw')).read_bytes() == row['http_observation'].encode()
    assert (native / ('extract_' + row['label'] + '.stdout.raw')).stat().st_size > 0
partial = sorted((rational / 'native').glob('*.raw'))
assert len(partial) == 10 and not (rational / 'native/receipt.json').exists()
assert all(p.read_bytes() == b'' for p in partial if p.name != 'historical_before.stdout.raw')
rational_result.update({'historical_inputs': 12, 'physical_control_snapshots': receipt['control_snapshots'],
                        'native_commands': receipt['commands'], 'source_fetches': receipt['source_fetches'],
                        'partial_initial_raws': 10, 'initial_receipt_missing_preserved': True})

geometry = SCOUT / 'discrete_geometry_gap_desk'
geometry_result = manifest(geometry, 'MANIFEST.json', 41)
rows = read(geometry / 'INPUT_PINS.json')['inputs']
assert len(rows) == len({r['source'] for r in rows}) == 8
for row in rows:
    data = safe(ROOT, row['source']).read_bytes()
    assert data == safe(geometry, row['snapshot']).read_bytes()
    assert pin_bytes(data) == {k: row[k] for k in ('bytes', 'sha256')}
geometry_commands = []
for path in sorted((geometry / 'native').glob('[0-9][0-9].json')):
    row = read(path)
    assert row['exit'] == 0 and row['timed_out'] is False and row['cwd'] == str(geometry)
    assert pin(Path(row['executable'])) == row['executable_pin']
    for stream in ('stdout', 'stderr'):
        data = base64.b64decode(row[stream + '_b64'], validate=True)
        assert pin_bytes(data) == row[stream + '_pin']
    geometry_commands.append({k: v for k, v in row.items() if not k.endswith('_b64')})
assert len(geometry_commands) == 12
receipt = read(geometry / 'native/RECEIPT.json')
assert receipt['producer'] == pin(geometry / 'capture.py')
assert receipt['python_pin'] == pin(Path(receipt['python']))
assert receipt['scientific_runs'] == 0 and receipt['commands'] == 12
for stem in ('tfpl', 'ornament', 'billiards', 'zhu'):
    assert (geometry / 'sources' / (stem + '.pdf')).read_bytes().startswith(b'%PDF-')
    assert (geometry / 'sources' / (stem + '.txt')).stat().st_size > 0
geometry_result.update({'historical_raw_pairs': 8, 'native_commands': geometry_commands,
                        'new_literals': 0, 'scientific_runs': 0})

print(json.dumps({'status': 'PASS_NEGATIVE_ARTIFACT_RECEPTION',
                  'allocation': allocation_result, 'rational': rational_result,
                  'geometry': geometry_result, 'new_scientific_executions': 0,
                  'limits': 'Read-only archive checks, not independent proof review, hermetic runtime or new scientific replay.'},
                 indent=2, sort_keys=True))
