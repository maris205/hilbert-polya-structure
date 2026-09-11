#!/usr/bin/python3.10
"""Read-only documentary collection; not a science/runtime replay verifier."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers211_215_sequence/scouting/finite_network_rewrite_desk'
ENV = {'LANG': 'C', 'LC_ALL': 'C', 'PATH': '/usr/bin:/bin', 'TZ': 'UTC'}
SELECTED = [
    ('docs/papers117_121_sequence/scouting/COMBINATORIAL_SCOUT.md',
     [(36, 74), (297, 311)]),
    ('docs/papers204_208_sequence/scouting/finite_systems_sixteenth/PROOF_AND_DISPOSITION.md',
     [(85, 250), (310, 331)]),
    ('papers/205-conflict-triggered-cyclic-increments/PROOF_PACKAGE.md',
     [(1, 140)]),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def identify(path, data=None):
    if data is None:
        data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': digest(data)}


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def encoded(data):
    text = data.decode('utf-8', errors='strict')
    assert text.encode('utf-8') == data
    return {'encoding': 'utf-8', 'text': text, 'bytes': len(data),
            'sha256': digest(data)}


def decoded(record):
    assert record['encoding'] == 'utf-8'
    data = record['text'].encode('utf-8')
    assert len(data) == record['bytes'] and digest(data) == record['sha256']
    return data


def command(argv):
    started = now()
    run = subprocess.run(argv, cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         timeout=30, check=False)
    return {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
            'started_utc': started, 'ended_utc': now(), 'exit_code': run.returncode,
            'stdout': encoded(run.stdout), 'stderr': encoded(run.stderr)}


def selected_bytes(data, ranges):
    lines = data.splitlines(keepends=True)
    return b''.join(b''.join(lines[first - 1:last]) for first, last in ranges)


def selected_argv(path, ranges):
    argv = ['/usr/bin/sed', '-n']
    for first, last in ranges:
        argv.extend(['-e', str(first) + ',' + str(last) + 'p'])
    return argv + [path]


def write_new(name, value):
    target = HERE / name
    assert not target.exists(), 'preserve existing artifact: ' + name
    data = (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')
    with target.open('xb') as stream:
        stream.write(data)


def collect():
    assert not (HERE / 'MANIFEST.json').exists()
    assert not (HERE / 'NATIVE_EVIDENCE.json').exists()
    originals = {path: (ROOT / path).read_bytes() for path, _ in SELECTED}
    pins = [identify(ROOT / path, originals[path]) for path, _ in SELECTED]
    inputs = [identify(HERE / name) for name in
              ['capture.py', 'HANDOFF.md', 'BOUNDARIES.md', 'SOURCE_RETURNS.json']]
    records = [command(['/usr/bin/sha256sum'] + [path for path, _ in SELECTED])]
    for path, ranges in SELECTED:
        record = command(selected_argv(path, ranges))
        actual = decoded(record['stdout'])
        expected = selected_bytes(originals[path], ranges)
        assert actual == expected, 'raw excerpt mismatch: ' + path
        record['selection'] = {'original': path, 'inclusive_line_ranges': ranges,
                               'exact_raw_bytes_equal': True}
        records.append(record)
    assert all(r['exit_code'] == 0 and decoded(r['stderr']) == b'' for r in records)
    expected_hashes = ''.join(pin['sha256'] + '  ' + pin['path'] + '\n' for pin in pins).encode('ascii')
    assert decoded(records[0]['stdout']) == expected_hashes
    assert all((ROOT / path).read_bytes() == original for path, original in originals.items())
    assert all(identify(ROOT / pin['path']) == pin for pin in inputs)
    write_new('NATIVE_EVIDENCE.json', {
        'schema': 'bounded-documentary-native-v1', 'scientific_runs': 0,
        'fresh_literals': 0, 'runtime_reuse_certificate': False,
        'original_pins': pins, 'collector_inputs': inputs,
        'full_originals_unchanged_before_after': True,
        'native_commands': records,
        'limits': 'New read-only checks, not retrospective navigation receipts; no exhaustive dependency lock.'})
    print('COLLECTED 3 original pins; 4 native commands; 3 raw excerpt checks; science 0')


def payload_rows():
    rows = []
    for path in sorted(HERE.rglob('*')):
        assert not path.is_symlink(), 'symlink unsupported'
        if path.is_file() and path.name != 'MANIFEST.json':
            raw = path.read_bytes()
            rows.append({'path': str(path.relative_to(HERE)), 'bytes': len(raw), 'sha256': digest(raw)})
    return rows


def seal():
    assert (HERE / 'NATIVE_EVIDENCE.json').is_file()
    rows = payload_rows()
    assert {r['path'] for r in rows} == {'HANDOFF.md', 'BOUNDARIES.md', 'capture.py',
                                        'SOURCE_RETURNS.json', 'NATIVE_EVIDENCE.json'}
    write_new('MANIFEST.json', {'schema': 'complete-nonself-payload-v1',
        'excluded_exactly': ['MANIFEST.json'], 'payload_count': len(rows),
        'payload_bytes': sum(r['bytes'] for r in rows), 'payloads': rows})
    print('SEALED', len(rows), 'payloads', sum(r['bytes'] for r in rows), 'bytes')


def verify():
    manifest = json.loads((HERE / 'MANIFEST.json').read_bytes())
    rows = payload_rows()
    assert manifest['excluded_exactly'] == ['MANIFEST.json']
    assert rows == manifest['payloads']
    assert len(rows) == manifest['payload_count'] == 5
    assert sum(r['bytes'] for r in rows) == manifest['payload_bytes']
    data = json.loads((HERE / 'NATIVE_EVIDENCE.json').read_bytes())
    assert data['scientific_runs'] == data['fresh_literals'] == 0
    assert data['runtime_reuse_certificate'] is False
    assert data['full_originals_unchanged_before_after'] is True
    pins = data['original_pins']
    assert [p['path'] for p in pins] == [p for p, _ in SELECTED]
    assert all(identify(ROOT / p['path']) == p for p in pins + data['collector_inputs'])
    records = data['native_commands']
    assert len(records) == 4
    assert records[0]['argv'] == ['/usr/bin/sha256sum'] + [p for p, _ in SELECTED]
    expected = ''.join(p['sha256'] + '  ' + p['path'] + '\n' for p in pins).encode('ascii')
    assert decoded(records[0]['stdout']) == expected
    for record in records:
        assert record['cwd'] == str(ROOT) and record['environment'] == ENV
        assert record['exit_code'] == 0 and decoded(record['stderr']) == b''
        decoded(record['stdout'])
        assert record['started_utc'] <= record['ended_utc']
    for record, (path, ranges) in zip(records[1:], SELECTED):
        assert record['argv'] == selected_argv(path, ranges)
        assert record['selection'] == {'original': path,
            'inclusive_line_ranges': [list(r) for r in ranges], 'exact_raw_bytes_equal': True}
        assert decoded(record['stdout']) == selected_bytes((ROOT / path).read_bytes(), ranges)
    source = json.loads((HERE / 'SOURCE_RETURNS.json').read_bytes())
    assert source['kind'] == 'actual_tool_responses_not_raw_http'
    assert [r['id'] for r in source['records']] == list(range(1, 7))
    assert all(r['request'] and r['tool_result'] for r in source['records'])
    print('VERIFIED', len(rows), 'payloads', manifest['payload_bytes'],
          'bytes; 3 original pins; 4 native commands; 3 raw excerpts; 6 browser returns; science 0')


if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in {'collect', 'seal', 'verify'}
    {'collect': collect, 'seal': seal, 'verify': verify}[sys.argv[1]]()
