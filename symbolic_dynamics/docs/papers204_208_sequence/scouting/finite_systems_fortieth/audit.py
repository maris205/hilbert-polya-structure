#!/usr/bin/env python3
"""Read-only artifact audit; does not execute any scientific transition."""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path

OWN = Path(__file__).absolute().parent
ROOT = OWN.parents[3]


def meta(path):
    body = path.read_bytes()
    return {'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()}


def read(path):
    return json.loads(path.read_text())


def main():
    for path in OWN.rglob('*'):
        assert not path.is_symlink(), ('symlink', str(path))
    folders = sorted(p for p in (OWN / 'commands').iterdir()
                     if p.is_dir() and not p.name.startswith('20_'))
    assert [int(p.name[:2]) for p in folders] == list(range(1, 20))
    current_meta = {}
    failure_rows = []
    for folder in folders:
        assert {p.name for p in folder.iterdir()} == {
            'attempt.json', 'inputs_before.json', 'inputs_after.json',
            'stdout.raw', 'stderr.raw', 'receipt.json'}
        attempt = read(folder / 'attempt.json')
        before = read(folder / 'inputs_before.json')
        after = read(folder / 'inputs_after.json')
        receipt = read(folder / 'receipt.json')
        assert before == after and receipt['unchanged'] is True
        assert receipt['input_count'] == len(before)
        assert receipt['argv'] == attempt['argv']
        assert receipt['cwd'] == attempt['cwd'] == str(ROOT)
        assert receipt['role'] == attempt['role']
        assert receipt['started_epoch'] == attempt['started_epoch']
        assert receipt['finished_epoch'] >= receipt['started_epoch']
        assert receipt['timed_out'] is False and attempt['timeout_seconds'] == 60
        for stream in ('stdout', 'stderr'):
            assert receipt[stream] == meta(folder / (stream + '.raw'))
        number = int(folder.name[:2])
        expected_exit = {8: 1, 13: 35}.get(number, 0)
        assert receipt['exit'] == expected_exit, (folder.name, receipt['exit'])
        if expected_exit:
            failure_rows.append({'command': folder.name, 'exit': expected_exit,
                                 'stdout_bytes': receipt['stdout']['bytes'],
                                 'stderr_bytes': receipt['stderr']['bytes']})
        else:
            assert receipt['stderr']['bytes'] == 0
        for name, pinned in before.items():
            path = Path(name)
            assert path.is_absolute() and path.is_file() and not path.is_symlink()
            if name not in current_meta:
                current_meta[name] = meta(path)
            assert current_meta[name] == pinned, ('declared original drift', name)
    role_counts = {}
    for filename in ('CONTROL_ROLES.json', 'ROOT_REFERENCE_ROLES.json'):
        roles = read(OWN / filename)
        for role in roles:
            original, copy = Path(role['original_path']), Path(role['copy_path'])
            expected = {'bytes': role['bytes'], 'sha256': role['sha256']}
            assert copy.is_relative_to(OWN) and not copy.is_symlink()
            assert meta(original) == meta(copy) == expected
            assert original.read_bytes() == copy.read_bytes()
        role_counts[filename] = len(roles)
    source_files = sorted((OWN / 'sources').glob('*.json'))
    assert len(source_files) == 10
    for path in source_files:
        obj = read(path)
        assert isinstance(obj, dict) and 'request' in obj and 'result' in obj
    code_names = ('record.py', 'mna_pilot.py', 'audit.py', 'run_final_audit.py', 'seal.py')
    for name in code_names:
        ast.parse((OWN / name).read_text(), filename=name)
    pilot = OWN / 'commands/17_one_mna_pilot'
    receipt = read(pilot / 'receipt.json')
    assert receipt['exit'] == 0 and receipt['input_count'] == 6
    assert receipt['stdout'] == {
        'bytes': 712674,
        'sha256': 'aef1162de01dd4833278df8071a425ca8e26bb5a48d380ef750f5ceeacacb2af'}
    rows = [json.loads(line) for line in (pilot / 'stdout.raw').read_text().splitlines()]
    assert Counter(row['type'] for row in rows) == {
        'contract': 1, 'state': 4095, 'summary': 12, 'completion': 1}
    assert rows[0]['N_min'] == 1 and rows[0]['N_max'] == 12
    assert rows[-1]['status'] == 'PASS' and rows[-1]['total_states'] == 4095
    assert rows[-1]['event_checks'] == {
        'deleted_cut_A': 17215, 'new_block_B': 9956,
        'previous_round_right_block': 3106}
    expected_images = [1, 1, 2, 3, 4, 7, 11, 16, 25, 40, 61, 94]
    summaries = [row for row in rows if row['type'] == 'summary']
    assert [row['N'] for row in summaries] == list(range(1, 13))
    assert [row['image'] for row in summaries] == expected_images
    for summary in summaries:
        n = summary['N']
        records = [row for row in rows if row['type'] == 'state' and row['N'] == n]
        assert len(records) == summary['states'] == 1 << (n - 1)
        assert len({tuple(row['state']) for row in records}) == len(records)
        recorded_tails = Counter(row['tail'] for row in records)
        assert {str(k): v for k, v in recorded_tails.items()} == summary['tail_histogram']
        assert max(recorded_tails) == summary['max_tail'] == summary['bound']
        assert sum(row['image_threshold'] for row in records) == summary['image']
        assert max(row['fibre'] for row in records) == summary['max_fibre']
        assert sum(row['fibre'] for row in records) == len(records)
        for row in records:
            assert row['fibre'] == row['fibre_formula']
            assert row['image_threshold'] == (row['fibre'] > 0)
            assert len(row['orbit']) == row['tail'] + 1
            assert row['orbit'][0] == row['state']
            assert row['orbit'][-1] == row['terminal']
    print(json.dumps({
        'status': 'PASS', 'role': 'documentary_artifact_audit_not_scientific_reexecution',
        'completed_native_commands_checked': 19,
        'unique_prior_declared_file_inputs_checked': len(current_meta),
        'role_maps': role_counts, 'main_source_return_files': len(source_files),
        'own_python_files_AST_checked': list(code_names),
        'scientific_executions_retained': 1, 'scientific_state_records': 4095,
        'preserved_nonzero_native_commands': failure_rows,
        'extra_auxiliary_tool_failure': read(OWN / 'EXTRA_TOOL_RETURN.json')['exit_code'],
        'central_controls_equal_pinned_physical_copies': True,
        'protected_science_not_opened_by_audit_except_predeclared_hash_reads': True
    }, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
