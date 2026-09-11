#!/usr/bin/env python3
"""Whole named recorded-row schemas and exact source delta only; no reader call."""
import ast
from collections import Counter
import difflib
import gzip
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
B = QA.parent / 'reviews/p210_b'
HERE = Path(__file__).resolve().parent
PINS, MAPS = {}, {}
CURRENT = {'real', 'sha256', 'size', 'symlink'}
ORIGINAL = {'resolved', 'sha256', 'bytes', 'symlink'}


def read(path):
    data = path.read_bytes()
    PINS[str(path)] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    return data


def obj(path):
    raw = read(path)
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def rows(label, mapping, current, count=None):
    expected = CURRENT if current else ORIGINAL
    assert type(mapping) is dict and mapping and (count is None or len(mapping) == count)
    census = Counter()
    for path, row in mapping.items():
        assert Path(path).is_absolute() and type(row) is dict
        census[tuple(sorted(row))] += 1
        assert set(row) == expected
        target, size = row['real' if current else 'resolved'], row['size' if current else 'bytes']
        assert type(target) is str and Path(target).is_absolute()
        assert type(size) is int and size >= 0 and type(row['sha256']) is str
        assert re.fullmatch('[0-9a-f]{64}', row['sha256']) is not None
        assert row['symlink'] is None or type(row['symlink']) is str
    MAPS[label] = {'complete_rows_checked': len(mapping), 'expected_exact_schema': sorted(expected),
                  'actual_complete_schema_census': [{'fields': list(key), 'rows': value} for key, value in sorted(census.items())],
                  'reader_branch': 'current_record' if current else 'convert_rich',
                  'all_field_types_and_absolute_original_and_resolved_paths_checked': True}


def main():
    provenance = obj(HERE / 'REVISION_PROVENANCE.json')
    old = read(Path(provenance['prior_sealed_preparation']['path']) / 'inspect_p210_artifact.py').decode()
    source = read(HERE / 'inspect_p210_artifact.py').decode()
    before = ast.parse(old)
    after = ast.parse(source)
    reproduced = old
    for change in provenance['exact_source_replacements']:
        assert reproduced.count(change['before']) == 1
        reproduced = reproduced.replace(change['before'], change['after'])
    assert reproduced == source
    delta = ''.join(difflib.unified_diff(old.splitlines(True), source.splitlines(True),
        fromfile='sealed-revision-01/inspect_p210_artifact.py', tofile='revision-02/inspect_p210_artifact.py'))
    assert read(HERE / 'SOURCE_DELTA.diff') == delta.encode()
    calls = [n for n in ast.walk(after) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'bind_full_base']
    assert len(calls) == 5
    selected = {}
    for call in calls:
        label = ast.get_source_segment(source, call.args[2])
        actual = ast.literal_eval(call.args[3]) if len(call.args) == 4 else True
        if call.keywords:
            assert len(call.keywords) == 1 and call.keywords[0].arg == 'original_schema'
            actual = ast.literal_eval(call.keywords[0].value)
        selected[label] = {'original_schema': actual, 'complete_call_source': ast.get_source_segment(source, call)}
    assert selected["'B_original_audit_full_map'"]['original_schema'] is False
    assert selected["'B_final_root_full_map'"]['original_schema'] is False
    assert selected["role + '_strict'"]['original_schema'] is True
    assert all(value['original_schema'] is False for key, value in selected.items() if key.startswith("'R'"))
    b_function = next(n for n in after.body if isinstance(n, ast.FunctionDef) and n.name == 'b_complete_reuse')
    segment = ast.get_source_segment(source, b_function)
    assert 'historical_record(name, current_record(row))' in segment
    assert 'historical_record(name, convert_rich(value))' in segment
    roles = obj(QA / 'p210_terminal_artifact_preparation/ACTUAL_ROLES.json')
    for role in ('author', 'a', 'b'):
        directory = QA / 'root_replays' / ('p210_' + role + '_strict_pair_01')
        data = obj(directory / 'INPUTS_BEFORE.json')
        assert data == obj(directory / 'INPUTS_AFTER.json')
        rows(role + '_strict_known', data, False, roles['pairs'][role]['known_keys'])
        entered = obj(directory / 'RUN_ENTERED.json')
        rows(role + '_entered_source', {str(QA / ('p210_' + role + '_strict_preparation/run_pair.py')): entered['source']}, False, 1)
    common = obj(B / 'DELTA_INPUTS_BEFORE.json.gz')
    assert common == obj(B / 'DELTA_INPUTS_AFTER.json.gz')
    rows('B_common_original', common, False, 121013)
    actual = json.loads(obj(QA / 'P210_B_FINAL_ORIGINALS_ROOT_COMPLETION.actual.json')['result']['output'])
    extra = actual['current_read_keys_outside_B_common']
    rows('B_final_root_extra', extra, True, 44)
    complete = {path: {'real': row['resolved'], 'size': row['bytes'], 'sha256': row['sha256'], 'symlink': row['symlink']}
                for path, row in common.items()}
    assert not set(complete).intersection(extra)
    complete.update(extra)
    rows('B_final_complete_after_explicit_common_conversion', complete, True, 121057)
    assert sha256(json.dumps(complete, sort_keys=True, separators=(',', ':')).encode()).hexdigest() == \
        actual['complete_current_read_map_canonical_sha256'] == 'c75e67753bb7cec027c788b1d00a78c977cfb99fb53153d9fe57511e546fea2d'
    rows('B_original_audit', obj(B / 'AUDIT_INPUTS.actual.json.gz'), True, 120840)
    for label, count in (('produce01', 3651), ('pair01', 3653), ('build01', 118353), ('build02', 118355)):
        ledger = obj(B / label / 'INPUTS_BEFORE.json.gz')
        assert ledger['membership'] == sorted(ledger['files'])
        rows('B_' + label + '_files', ledger['files'], True, count)
        if label != 'build01':
            assert ledger == obj(B / label / 'INPUTS_AFTER.json.gz')
    rows('B_delta_after_extra_original', obj(B / 'DELTA_AFTER_EXTRA_INPUTS.actual.json'), False, 3)
    for number, source_count, root_count in ((1, 1653, 2164), (2, 2077, 2603)):
        provenance = obj(PAPER / ('frozen_round' + str(number)) / ('ROUND' + str(number) + '_PROVENANCE.json'))
        rows('R' + str(number) + '_freezer', provenance['full_source_input_pins_before_and_reread_after'], True, source_count)
        receipt = obj(QA / ('p210_round' + str(number) + '_root_reception/ROOT_RECEPTION.json'))
        rows('R' + str(number) + '_root', receipt['complete_input_pins'], True, root_count)
    capture = QA / 'p210_terminal_artifact_01'
    assert {p.name for p in capture.iterdir() if p.is_file()} == {'ARTIFACT_REPORT.json', 'ATTEMPT.json', 'RESULT.json', 'SPAWN.json', 'executed_source.py', 'stderr'}
    assert not (capture / 'SHA256SUMS').exists()
    report, result = obj(capture / 'ARTIFACT_REPORT.json'), obj(capture / 'RESULT.json')
    assert report['status'] == 'FAIL_P210_TERMINAL_ARTIFACT_NO_ACCEPTANCE' and report['checks_completed'] == 1709801
    assert result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 1
    assert result['wait_error'] is None and result['timed_out'] is False and result['cleanup_events'] == []
    assert result['child_reaped'] is result['process_group_absent'] is True
    for role, name in (('stdout', 'ARTIFACT_REPORT.json'), ('stderr', 'stderr')):
        data = read(capture / name)
        assert {'sha256': sha256(data).hexdigest(), 'bytes': len(data)} == result[role]
    print(json.dumps({'status': 'PASS_ALL_NAMED_ROW_SCHEMAS_AND_SIX_LINE_SOURCE_DELTA_ONLY_NO_READER',
        'source': PINS[str(HERE / 'inspect_p210_artifact.py')], 'source_lines': len(source.splitlines()),
        'bind_full_base_callers': selected, 'whole_recorded_map_schemas': MAPS,
        'total_recorded_rows_checked': sum(row['complete_rows_checked'] for row in MAPS.values()),
        'named_original_data_pins': PINS,
        'first_actual_failure_unchanged': {'checks_completed': 1709801, 'native_exit': 1, 'payloads': 6, 'sealed': False},
        'second_scope_schema_defect_was_static_not_a_second_gate_execution': True,
        'reader_imported_or_executed': False, 'reader_function_calls': 0, 'old_programs_imported_or_executed': 0,
        'host_membership_or_current_dependency_rehash_passes': 0, 'new_science_builds_views': 0,
        'root_acceptance': False, 'paper_completion': False, 'five_paper_completion': False}, sort_keys=True))


if __name__ == '__main__':
    main()
