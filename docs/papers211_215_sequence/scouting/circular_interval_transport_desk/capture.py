#!/usr/bin/env python3
"""Documentary old-source capture and nonself inventory; no science imports."""

import hashlib
import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers211_215_sequence/scouting/circular_interval_transport_desk'
ENV = {'LANG': 'C', 'LC_ALL': 'C', 'PATH': '/usr/bin:/bin', 'TZ': 'UTC'}
INPUTS = [
    ('p198', 'papers/198-cyclic-monomer-matching/main.tex', [(73, 205)]),
    ('mrt', 'docs/papers204_208_sequence/scouting/finite_systems_thirtieth/PROOF_PACKAGE.md', [(1, 160)]),
    ('omd_hur', 'docs/papers162_166_sequence/scouting/replacement_matchings_incidence/SCOUT.md', [(17, 45), (82, 89)]),
    ('uuc_intake', 'docs/papers211_215_sequence/scouting/transport_lane/INTAKE.md', [(1, 200)]),
    ('uuc_proof', 'docs/papers211_215_sequence/scouting/transport_lane/PROOF_PACKAGE.md', [(1, 220)]),
    ('planar_handoff', 'docs/papers211_215_sequence/scouting/planar_matching_lane/HANDOFF.md', [(1, 180)]),
    ('planar_proof', 'docs/papers211_215_sequence/scouting/planar_matching_lane/PROOF_PACKAGE.md', [(1, 180)]),
]


def digest(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def encode(value):
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def write_new(relative, data):
    target = BASE / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('xb') as stream:
        stream.write(data)


def file_record(path):
    p = pathlib.Path(path)
    return {'path': str(p), **digest(p.read_bytes())}


def collect():
    assert pathlib.Path(__file__).resolve() == BASE / 'capture.py'
    assert not (BASE / 'native').exists(), 'refuse documentary recapture overwrite'
    assert not (BASE / 'snapshots').exists(), 'refuse snapshot overwrite'
    originals = {name: (ROOT / path).read_bytes() for name, path, _ in INPUTS}
    pins = []
    for name, path, ranges in INPUTS:
        relative = 'snapshots/' + path
        write_new(relative, originals[name])
        assert (BASE / relative).read_bytes() == originals[name]
        pins.append({'key': name, 'original': path, 'snapshot': relative,
                     'read_line_ranges': ranges, **digest(originals[name])})
    write_new('HISTORICAL_INPUTS.json', encode({
        'schema': 'circular-interval-documentary-inputs-v1',
        'origin_base': str(ROOT), 'rows': pins,
        'limits': 'Seven selected original byte copies, not an exhaustive discovery universe.'}))

    commands = []
    def run(key, argv, excerpt=None):
        started = time.time_ns()
        child = subprocess.run(argv, cwd=ROOT, env=ENV, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, timeout=30, check=False)
        finished = time.time_ns()
        stdout = 'native/' + key + '.stdout'
        stderr = 'native/' + key + '.stderr'
        write_new(stdout, child.stdout)
        write_new(stderr, child.stderr)
        row = {'key': key, 'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
               'started_unix_ns': started, 'finished_unix_ns': finished,
               'returncode': child.returncode, 'executable': file_record(argv[0]),
               'stdout': {'path': stdout, **digest(child.stdout)},
               'stderr': {'path': stderr, **digest(child.stderr)}}
        if excerpt is not None:
            row['excerpt_binding'] = excerpt
        commands.append(row)
        # Persist even a failed child before refusing further collection.
        receipt = {'schema': 'circular-interval-native-documentary-v1',
                   'kind': 'read_only_documentary_no_scientific_execution',
                   'driver': file_record(BASE / 'capture.py'),
                   'interpreter': file_record(sys.executable),
                   'commands': commands,
                   'limits': 'Native child streams only; not hermetic runtime provenance.'}
        receipt_path = BASE / 'native' / 'RECEIPT.json'
        receipt_path.write_bytes(encode(receipt))
        assert child.returncode == 0, (key, child.returncode)
        assert not child.stderr, (key, 'unexpected stderr preserved')
        return child.stdout

    paths = [path for _, path, _ in INPUTS]
    before = run('01_before', ['/usr/bin/sha256sum', *paths])
    for index, (name, path, ranges) in enumerate(INPUTS, 2):
        argv = ['/usr/bin/sed', '-n']
        for lo, hi in ranges:
            argv += ['-e', str(lo) + ',' + str(hi) + 'p']
        argv += [path]
        output = run(str(index).zfill(2) + '_' + name, argv,
                     {'original': path, 'snapshot': 'snapshots/' + path,
                      'line_ranges': ranges})
        lines = originals[name].splitlines(keepends=True)
        expected = b''.join(b''.join(lines[lo - 1:hi]) for lo, hi in ranges)
        assert output == expected, (name, 'raw excerpt mismatch')
    after = run('09_after', ['/usr/bin/sha256sum', *paths])
    run('10_compare', ['/usr/bin/cmp', '-s',
        str(BASE / 'native/01_before.stdout'), str(BASE / 'native/09_after.stdout')])
    assert before == after
    for name, path, _ in INPUTS:
        assert (ROOT / path).read_bytes() == originals[name], (name, 'original changed')
    print(json.dumps({'status': 'DOCUMENTARY_CAPTURE_PASS', 'input_files': len(pins),
                      'native_commands': len(commands), 'scientific_executions': 0}, sort_keys=True))


def verify_inputs():
    pins = json.loads((BASE / 'HISTORICAL_INPUTS.json').read_bytes())['rows']
    assert len(pins) == len(INPUTS)
    assert {r['key'] for r in pins} == {name for name, _, _ in INPUTS}
    for row in pins:
        old = (ROOT / row['original']).read_bytes()
        copy = (BASE / row['snapshot']).read_bytes()
        assert copy == old, row['original']
        assert digest(copy) == {key: row[key] for key in ('bytes', 'sha256')}
    receipt = json.loads((BASE / 'native/RECEIPT.json').read_bytes())
    assert receipt['kind'] == 'read_only_documentary_no_scientific_execution'
    assert len(receipt['commands']) == 10
    assert receipt['driver'] == file_record(BASE / 'capture.py')
    assert receipt['interpreter'] == file_record(sys.executable)
    for command in receipt['commands']:
        assert command['returncode'] == 0
        assert command['executable'] == file_record(command['argv'][0])
        assert command['environment'] == ENV and command['cwd'] == str(ROOT)
        for stream in ('stdout', 'stderr'):
            record = command[stream]
            data = (BASE / record['path']).read_bytes()
            assert digest(data) == {key: record[key] for key in ('bytes', 'sha256')}
            if stream == 'stderr':
                assert not data
        if 'excerpt_binding' in command:
            binding = command['excerpt_binding']
            lines = (BASE / binding['snapshot']).read_bytes().splitlines(keepends=True)
            expected = b''.join(b''.join(lines[lo - 1:hi]) for lo, hi in binding['line_ranges'])
            assert (BASE / command['stdout']['path']).read_bytes() == expected
    expected_hashes = ''.join(row['sha256'] + '  ' + row['original'] + '\n' for row in pins).encode('ascii')
    assert (BASE / 'native/01_before.stdout').read_bytes() == expected_hashes
    assert (BASE / 'native/09_after.stdout').read_bytes() == expected_hashes
    assert not (BASE / 'native/10_compare.stdout').read_bytes()
    return pins, receipt


def inventory():
    rows = []
    for path in sorted(BASE.rglob('*')):
        assert not path.is_symlink(), str(path)
        if path.is_file() and path != BASE / 'MANIFEST.json':
            rows.append({'path': path.relative_to(BASE).as_posix(), **digest(path.read_bytes())})
    return rows


def seal():
    verify_inputs()
    rows = inventory()
    manifest = {'schema': 'complete-nonself-sha256-inventory-v1',
                'excluded_only': ['MANIFEST.json'], 'rows': rows,
                'payload_count': len(rows), 'payload_bytes': sum(r['bytes'] for r in rows)}
    write_new('MANIFEST.json', encode(manifest))
    print(json.dumps({'status': 'SEALED', 'payloads': len(rows),
                      'bytes': manifest['payload_bytes']}, sort_keys=True))


def verify():
    pins, receipt = verify_inputs()
    manifest = json.loads((BASE / 'MANIFEST.json').read_bytes())
    rows = inventory()
    assert manifest['excluded_only'] == ['MANIFEST.json']
    assert manifest['rows'] == rows
    assert manifest['payload_count'] == len(rows)
    assert manifest['payload_bytes'] == sum(r['bytes'] for r in rows)
    print(json.dumps({'status': 'ARCHIVE_VERIFY_PASS', 'payloads': len(rows),
                      'bytes': manifest['payload_bytes'], 'historical_inputs': len(pins),
                      'native_commands': len(receipt['commands']),
                      'fresh_literals': 0, 'scientific_executions': 0,
                      'not_claimed': ['hermetic_runtime', 'mathematical_replay',
                                      'independent_review', 'candidate_admission']}, sort_keys=True))


if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in ('collect', 'seal', 'verify')
    {'collect': collect, 'seal': seal, 'verify': verify}[sys.argv[1]]()
