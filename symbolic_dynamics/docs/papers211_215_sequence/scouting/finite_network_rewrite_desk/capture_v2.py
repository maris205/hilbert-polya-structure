#!/usr/bin/python3.10
"""Additive documentary closeout; preserve all first-seal bytes; no subprocess."""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers211_215_sequence/scouting/finite_network_rewrite_desk'
EXPECTED = {'HANDOFF.md', 'BOUNDARIES.md', 'capture.py', 'SOURCE_RETURNS.json',
            'NATIVE_EVIDENCE.json', 'METADATA_CORRECTION.md',
            'initial_draft/BOUNDARIES.md', 'initial_draft/capture.py',
            'MANIFEST.json', 'FINAL_HANDOFF.md', 'capture_v2.py'}
SELECTED = [
    ('docs/papers117_121_sequence/scouting/COMBINATORIAL_SCOUT.md', [[36, 74], [297, 311]]),
    ('docs/papers204_208_sequence/scouting/finite_systems_sixteenth/PROOF_AND_DISPOSITION.md',
     [[85, 250], [310, 331]]),
    ('papers/205-conflict-triggered-cyclic-increments/PROOF_PACKAGE.md', [[1, 140]]),
]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def rows():
    found = []
    for path in sorted(HERE.rglob('*')):
        assert not path.is_symlink()
        if path.is_file() and path != HERE / 'MANIFEST_V2.json':
            data = path.read_bytes()
            found.append({'path': str(path.relative_to(HERE)), 'bytes': len(data), 'sha256': sha(data)})
    assert {r['path'] for r in found} == EXPECTED
    return found


def decode(row):
    assert row['encoding'] == 'utf-8'
    raw = row['text'].encode('utf-8')
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
    return raw


def historical_checks():
    old = json.loads((HERE / 'MANIFEST.json').read_bytes())
    assert old['excluded_exactly'] == ['MANIFEST.json'] and old['payload_count'] == 8
    assert old['payload_bytes'] == 233267
    assert {r['path'] for r in old['payloads']} == EXPECTED - {'MANIFEST.json', 'FINAL_HANDOFF.md', 'capture_v2.py'}
    for row in old['payloads']:
        raw = (HERE / row['path']).read_bytes()
        assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
    receipt = json.loads((HERE / 'NATIVE_EVIDENCE.json').read_bytes())
    assert receipt['fresh_literals'] == receipt['scientific_runs'] == 0
    assert receipt['runtime_reuse_certificate'] is False
    assert receipt['full_originals_unchanged_before_after'] is True
    pins = receipt['original_pins']
    assert [p['path'] for p in pins] == [p for p, _ in SELECTED]
    originals = {}
    for row in pins:
        raw = (ROOT / row['path']).read_bytes()
        assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
        originals[row['path']] = raw
    inputs = receipt['collector_inputs']
    assert [r['path'] for r in inputs] == [str((HERE / n).relative_to(ROOT)) for n in
        ['capture.py', 'HANDOFF.md', 'BOUNDARIES.md', 'SOURCE_RETURNS.json']]
    for row in inputs:
        origin = ROOT / row['path']
        resolved = HERE / 'initial_draft' / origin.name if origin.name in {'capture.py', 'BOUNDARIES.md'} else origin
        raw = resolved.read_bytes()
        assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
    native = receipt['native_commands']
    assert len(native) == 4
    for row in native:
        assert row['cwd'] == str(ROOT)
        assert row['environment'] == {'LANG': 'C', 'LC_ALL': 'C', 'PATH': '/usr/bin:/bin', 'TZ': 'UTC'}
        assert row['exit_code'] == 0 and decode(row['stderr']) == b''
        assert row['started_utc'] <= row['ended_utc']
        decode(row['stdout'])
    assert native[0]['argv'] == ['/usr/bin/sha256sum'] + [p for p, _ in SELECTED]
    assert decode(native[0]['stdout']) == ''.join(p['sha256'] + '  ' + p['path'] + '\n' for p in pins).encode('ascii')
    for row, (path, ranges) in zip(native[1:], SELECTED):
        argv = ['/usr/bin/sed', '-n']
        for first, last in ranges:
            argv.extend(['-e', str(first) + ',' + str(last) + 'p'])
        assert row['argv'] == argv + [path]
        assert row['selection'] == {'original': path, 'inclusive_line_ranges': ranges, 'exact_raw_bytes_equal': True}
        lines = originals[path].splitlines(keepends=True)
        expected = b''.join(b''.join(lines[a - 1:b]) for a, b in ranges)
        assert decode(row['stdout']) == expected
    sources = json.loads((HERE / 'SOURCE_RETURNS.json').read_bytes())
    assert sources['kind'] == 'actual_tool_responses_not_raw_http'
    assert [r['id'] for r in sources['records']] == list(range(1, 7))
    assert all(r['request'] and r['tool_result'] for r in sources['records'])
    body = sources['records'][3]['tool_result']
    assert 'Phase transition in firefly cellular automata on finite trees' in body
    assert 'completeness of Graph Local Complementation' in body and 'Pablo Concha-Vega' in body


def main(mode):
    historical_checks()
    found = rows()
    current = {'schema': 'complete-nonself-additive-closeout-v2',
        'excluded_exactly': ['MANIFEST_V2.json'], 'payload_count': len(found),
        'payload_bytes': sum(r['bytes'] for r in found), 'payloads': found,
        'historical_seal': 'MANIFEST.json', 'controlling_handoff': 'FINAL_HANDOFF.md'}
    if mode == 'seal':
        target = HERE / 'MANIFEST_V2.json'
        assert not target.exists()
        with target.open('xb') as stream:
            stream.write((json.dumps(current, sort_keys=True, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    else:
        assert current == json.loads((HERE / 'MANIFEST_V2.json').read_bytes())
    print(mode.upper(), len(found), 'payloads', current['payload_bytes'],
        'bytes; initial 8 unchanged; 3 original pins; 4 native records; 3 raw excerpts; 6 source returns; science 0')


if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in {'seal', 'verify'}
    main(sys.argv[1])
