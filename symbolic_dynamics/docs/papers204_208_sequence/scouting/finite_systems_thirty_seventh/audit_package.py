#!/usr/bin/env python3
"""Bounded documentary audit: never import or rerun the candidate program."""
import collections
import hashlib
import importlib.util
import json
import pathlib
import re
import sys

OWN = pathlib.Path(__file__).absolute().parent
ROOT = OWN.parents[3]
LABEL = '08_documentary_audit'
EXCLUDE = OWN / 'commands' / LABEL
LEDGER = {}


def read(path):
    path = pathlib.Path(path)
    assert path.is_absolute() and path.is_file() and not path.is_symlink(), str(path)
    body = path.read_bytes()
    row = dict(bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    if str(path) in LEDGER:
        assert LEDGER[str(path)] == row, ('changed-during-read', str(path))
    LEDGER[str(path)] = row
    return body


def obj(path):
    return json.loads(read(path))


def own_files():
    return sorted(p for p in OWN.rglob('*') if p.is_file()
                  and not p.is_relative_to(EXCLUDE) and p.name != 'SHA256SUMS')


def main():
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
    assert not sys.flags.optimize
    existing = own_files()
    for path in existing:
        read(path)
    roles = obj(OWN / 'CONTROL_ROLES.json')
    assert len(roles) == 3
    control = {row['original_path']: row for row in roles}
    assert len(control) == 3
    for row in roles:
        assert row['role'] == 'exact_control_copy_before_recorded_body_search'
        copy = pathlib.Path(row['copy_path'])
        assert copy.parent == OWN / 'controls'
        read(copy)
        assert LEDGER[str(copy)]['sha256'] == row['sha256']

    def pin(path, expected):
        if path in control:
            assert expected == control[path]['sha256']
            physical = control[path]['copy_path']
        else:
            physical = path
        read(physical)
        assert LEDGER[physical]['sha256'] == expected, ('original-input-pin', path)

    native_rows = []
    command_folders = sorted(p for p in (OWN / 'commands').iterdir()
                             if p.is_dir() and p != EXCLUDE)
    assert [p.name[:2] for p in command_folders] == ['01', '02', '03', '04', '05', '06', '07']
    for folder in command_folders:
        assert {p.name for p in folder.iterdir()} == {
            'inputs_before.json', 'inputs_after.json', 'receipt.json', 'stdout.raw', 'stderr.raw'}
        before = obj(folder / 'inputs_before.json')
        after = obj(folder / 'inputs_after.json')
        rec = obj(folder / 'receipt.json')
        out, err = read(folder / 'stdout.raw'), read(folder / 'stderr.raw')
        assert before == after and rec['unchanged'] is True
        assert rec['input_count'] == len(before) and rec['exit'] == 0 and err == b''
        assert rec['cwd'] == str(ROOT)
        assert rec['role'] == 'native_documentary_command_not_candidate_scientific_execution'
        assert rec['started_epoch'] <= rec['finished_epoch']
        assert rec['stdout_sha256'] == hashlib.sha256(out).hexdigest()
        assert rec['stderr_sha256'] == hashlib.sha256(err).hexdigest()
        for path, sha in before.items():
            pin(path, sha)
        argv = rec['argv']
        if argv[0] == 'cp':
            assert argv[:2] == ['cp', '-p'] and argv[-1] == str(OWN / 'controls')
            paths = argv[2:-1]
            assert set(paths) == set(control) and out == b''
        elif argv[0] == 'sed':
            assert argv[:3] == ['sed', '-n', '1,4000p']
            paths = argv[3:]
            complete = b''.join(read(p) for p in paths)
            assert len(complete.splitlines()) <= 4000 and out == complete
        elif argv[0] == 'rg':
            assert argv[1] == '-n' and argv[3] == '--'
            paths = argv[4:]
            pattern = re.compile(argv[2])
            expected = []
            for path in paths:
                for number, line in enumerate(read(path).decode().splitlines(), 1):
                    if pattern.search(line):
                        expected.append(f'{path}:{number}:{line}')
            # rg may group files in a different order; all actual raw bytes stay archived.
            assert collections.Counter(out.decode().splitlines()) == collections.Counter(expected)
        else:
            assert folder.name == '07_archived_pilot_analysis'
            assert argv == ['python3', '-I', '-B', str(OWN / 'analyze_pilot.py')]
            paths = [str(OWN / 'analyze_pilot.py'), str(OWN / 'pilot_run/stdout.raw')]
        assert set(before) == set(paths) | {str(OWN / 'record.py')}
        native_rows.append(dict(command=folder.name, input_count=len(before),
                                stdout_bytes=len(out), exit=0, unchanged=True))

    run = OWN / 'pilot_run'
    assert {p.name for p in run.iterdir()} == {
        'inputs_before.json', 'inputs_after.json', 'attempt.json',
        'receipt.json', 'stdout.raw', 'stderr.raw'}
    before, after = obj(run / 'inputs_before.json'), obj(run / 'inputs_after.json')
    attempt, rec = obj(run / 'attempt.json'), obj(run / 'receipt.json')
    assert before == after and len(before) == rec['input_count'] == 7
    expected_paths = {str(OWN / name) for name in (
        'INTAKE.md', 'SOURCE_DESK.md', 'PROOF_PACKAGE.md', 'PILOT_CONTRACT.md', 'pilot.py', 'run_pilot.py')}
    expected_paths.add(str(pathlib.Path(attempt['python_executable']).resolve()))
    assert set(before) == expected_paths
    for path, metadata in before.items():
        read(path)
        assert LEDGER[path] == metadata, ('pilot-input-pin', path)
    assert rec['argv'] == attempt['argv'] == [attempt['python_executable'], '-I', '-S', '-B', str(OWN / 'pilot.py')]
    assert rec['cwd'] == attempt['cwd'] == str(ROOT)
    assert rec['role'] == attempt['role'] == 'one_original_fixed_box_scientific_pilot_not_admission'
    assert rec['started_epoch'] == attempt['started_epoch'] <= rec['finished_epoch']
    assert attempt['timeout_seconds'] == 60 and rec['timed_out'] is False
    assert rec['exit'] == 0 and rec['unchanged'] is True
    raw, err = read(run / 'stdout.raw'), read(run / 'stderr.raw')
    assert len(raw) == rec['stdout_bytes'] == 68160 and len(err) == rec['stderr_bytes'] == 0
    assert hashlib.sha256(raw).hexdigest() == rec['stdout_sha256'] == '193c76c203510faaacabb5161ec0fb5c81e06a6a515ef20b42f42889e3f5e9b1'
    assert hashlib.sha256(err).hexdigest() == rec['stderr_sha256']
    data = json.loads(raw)
    assert raw == (json.dumps(data, sort_keys=True, separators=(',', ':')) + '\n').encode()
    assert data['status'] == 'PASS_FIXED_BOX_PILOT_NOT_ALL_FIELD_TEMPORAL_PROOF'
    assert data['candidate'] == 'SMV' and data['literal_maps'] == data['original_pilots'] == 1
    assert data['primes'] == [3, 5, 7, 17]
    assert data['total_states'] == data['total_targets'] == 5408 and data['checks'] == 124629
    assert [b['prime'] for b in data['boxes']] == data['primes']
    assert sum(b['state_count'] for b in data['boxes']) == 5408
    compact = {k: data[k] for k in ('status', 'total_states', 'total_targets', 'checks')}
    compact['fields'] = [{k: b[k] for k in ('prime', 'state_count', 'maximum_depth',
        'cycle_length_histogram', 'image_size', 'fibre_histogram')} for b in data['boxes']]
    assert compact == rec['compact_result']
    for box in data['boxes']:
        n = box['state_count']
        assert n == box['prime'] ** 3
        for name in ('successor_indices', 'every_target_fibre_size', 'every_state_depth', 'every_state_eventual_period'):
            assert len(box[name]) == n
        assert all(0 <= i < n for i in box['successor_indices'])
        assert sum(box['every_target_fibre_size']) == n
        assert sum(c['basin_states'] for c in box['cycles']) == n
        assert all(len(c['nodes']) == c['length'] for c in box['cycles'])
    analysis = obj(OWN / 'commands/07_archived_pilot_analysis/stdout.raw')
    assert analysis['role'] == 'analysis_of_archived_canonical_only_not_new_pilot'
    assert analysis['new_successor_evaluations'] == analysis['extra_fields'] == analysis['extrapolated_theorems'] == 0
    assert analysis['total_states'] == 5408 and analysis['checks_in_original_pilot'] == 124629
    assert [r['prime'] for r in analysis['rows']] == [3, 5, 7, 17]
    assert analysis['rows'][-1]['recurrent_all_distinct_squares'] == 48
    sources = sorted((OWN / 'sources').glob('*.json'))
    assert [p.name[:2] for p in sources] == ['02', '03', '04', '05', '06']
    for path in sources:
        source = obj(path)
        assert set(source) == {'role', 'request', 'result'}
        assert isinstance(source['request'], dict) and source['result']
        assert 'not native HTTP' in source['role']
    # Result analysis skill was read after the earlier instruction capture.
    read('/root/autodl-tmp/.codex/skills/analyze-results/SKILL.md')
    snapshot = dict(LEDGER)
    for path, metadata in snapshot.items():
        read(path)
        assert LEDGER[path] == metadata
    assert LEDGER == snapshot and own_files() == existing
    print(json.dumps(dict(status='PASS_BOUNDED_DOCUMENTARY_AUDIT_NOT_MATH_REVIEW',
        original_native_commands=native_rows, original_scientific_pilots=1,
        pilot_checks_claim_checked_against_original=124629, pilot_canonical_bytes=68160,
        new_successor_evaluations=0, candidate_or_analysis_replays=0,
        web_serializations=5, native_http_archives=0,
        control_originals_resolved_to_exact_historical_copies=roles,
        consumed_file_count=len(LEDGER), complete_consumed_inputs_read_twice_unchanged=LEDGER),
        indent=2, sort_keys=True))


if __name__ == '__main__':
    if sys.argv[1:] == ['--record']:
        spec = importlib.util.spec_from_file_location('lane37_recorder', OWN / 'record.py')
        recorder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(recorder)
        result = recorder.capture(LABEL, [sys.executable, '-I', '-S', '-B', str(OWN / 'audit_package.py')], own_files())
        raise SystemExit(result.returncode)
    assert len(sys.argv) == 1
    main()
