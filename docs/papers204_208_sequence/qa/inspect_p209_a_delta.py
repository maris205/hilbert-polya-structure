#!/usr/bin/env python3
"""Root final A delta/original closure; never launches mathematics or TeX.

The main process separately read the actual accepted DELTA, original proof/
source review, failed and corrected audit code and the seal code. This
program measures their complete artifact/input closure. Only the single
explicit historical Git-receipt path has an exact old-byte physical alias.
"""
import json
from pathlib import Path
import runpy
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
BASE = ROOT / 'docs/papers204_208_sequence/reviews/p209_a'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
FROZEN = PAPER / 'frozen_round0'
PAIR = QA / 'root_replays/p209_a_strict/root_a_pair_01'
LAUNCH = PAIR.parent / 'launcher_root_a_pair_01'
RESPONSE = QA.parent / 'P209_A_RESPONSE.md'
ALIAS = QA / 'central_lifecycle_p209_a/GIT_SYNC_RECEIPT.before.md'
OLD_CONTROL = QA.parent / 'GIT_SYNC_RECEIPT.md'
INITIAL = '7105dd2c22a7fb8df5586a59880fdc47e26f62f2d7573d3f08570eda5c62fb0c'
FINAL = 'dbc1f31fd1ba6324f421bed5b78bd1566b641e21d3d552630e688ab5cea7c7b3'
OLD_CONTROL_HASH = 'af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da'
HELPER = QA / 'inspect_p209_a_initial.py'
D = runpy.run_path(str(HELPER))
pin, obj, checkpin, manifest = (D[n] for n in ('pin', 'obj', 'checkpin', 'manifest'))
ENV = D['ENV']


def h(p):
    return pin(p)['sha256']


def archive_commands(folder):
    before = obj(folder / 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json')
    assert before == obj(folder / 'ALL_INPUTS_AFTER.json') and len(before) == 5147
    for p, row in before.items(): checkpin(p, row)
    commands = obj(folder / 'ALL_COMMAND_RECORDS.json')
    assert len(commands) == 85
    for e in commands:
        where, tag, row = Path(e['folder']), e['tag'], e['command']
        assert where.is_relative_to(folder) and obj(where / (tag + '.command.json')) == row
        attempt = obj(where / (tag + '.attempt.json'))
        assert all(attempt[k] == row[k] for k in ('argv', 'cwd', 'env', 'stdout', 'stderr'))
        assert row['process_outcome'] == 'COMPLETED' and row['exit'] == 0 and row['env'] == ENV
        assert row['spawn_error'] is None and row['cleanup'] == []
        for stream in ('stdout', 'stderr'): checkpin(where / row[stream], row[stream + '_info'])
    receipt = obj(folder / 'RECEIPT.json')
    assert receipt['status'] == 'PASS_ROOT_REVIEW_A_PAIR' and receipt['failures'] == []
    assert not receipt['result']['canonical_adopted']
    for label in ('replay_01', 'replay_02'):
        p = folder / label
        child = obj(p / 'RECEIPT.json')
        assert child['status'] == 'PASS' and child['checks'] == 135605 and child['total_states'] == 3414
        for phase in ('before', 'after'):
            v = obj(p / ('child.' + phase + '.json'))
            assert v['env'] == ENV and v['cwd'] == str(p) and v['optimize'] == 0
            assert v['isolated'] == v['no_site'] == 1 and v['dont_write_bytecode']
            assert not v['cache_exists'] and not Path(v['pycache_prefix']).exists()
    launch = obj(LAUNCH / 'RECEIPT.json')
    assert launch['status'] == 'PASS_ROOT_LAUNCH' and launch['exit'] == 0
    assert launch['outcome'] == 'COMPLETED' and launch['failure'] is None
    assert launch['inputs_unchanged'] and launch['cache_absent']
    for stream in ('recorder.stdout', 'recorder.stderr'): checkpin(LAUNCH / stream, launch[stream + '_pin'])
    return len(before)


def main():
    pin(HELPER); pin(Path(__file__))
    assert h(BASE / 'SHA256SUMS') == FINAL
    outer = manifest(BASE / 'SHA256SUMS', complete=True)
    assert len(outer) == 1342
    assert h(BASE / 'INITIAL_REVIEW_SEAL.sha256') == INITIAL
    initial = manifest(BASE / 'INITIAL_REVIEW_SEAL.sha256')
    assert len(initial) == 1227 and all(outer[n] == v for n, v in initial.items())
    assert len(manifest(BASE / 'INITIAL_ARTIFACTS.sha256')) == 1226
    final_audit = obj(BASE / 'delta_final_audit_01/RESULT.json')
    assert final_audit['status'] == 'PASS_FINAL_DELTA_ORIGINAL_AND_INPUT_CLOSURE'
    assert final_audit['successful_delta_input_paths_rechecked'] == 124214
    preseal = obj(BASE / 'delta_final_audit_01/PRESEAL_PAYLOADS.json')
    assert len(preseal) == 1340 and all(h(BASE / n) == v for n, v in preseal.items())
    for row in obj(BASE / 'delta_check_02/MANIFEST_ROLES.json'):
        assert h(row['manifest']) == row['sha256']
        assert len(manifest(row['manifest'], complete=row['complete_at_current_path'])) == row['payloads']
    before = obj(BASE / 'delta_check_02/INPUTS_BEFORE.json')
    assert before == obj(BASE / 'delta_check_02/INPUTS_AFTER.json') and len(before) == 124214
    for p, value in before.items(): assert h(p) == value, p
    original_map = obj(BASE / 'initial_audit_01/CURRENT_INPUT_CLOSURE.json')
    assert len(original_map) == 120491 and original_map[str(OLD_CONTROL)] == OLD_CONTROL_HASH
    rolemap = obj(BASE / 'delta_check_02/HISTORICAL_PIN_ROLE_MAP.json')
    assert rolemap['excluded_current_paths'] == {} and rolemap['original_path_count'] == 120491
    assert rolemap['same_path_recheck_count'] == 120490
    aliases = rolemap['exact_documentary_aliases']
    assert set(aliases) == {str(OLD_CONTROL)}
    assert aliases[str(OLD_CONTROL)]['original_sha256'] == OLD_CONTROL_HASH
    assert aliases[str(OLD_CONTROL)]['preserved_exact_path'] == str(ALIAS)
    for p, value in original_map.items(): assert h(ALIAS if p == str(OLD_CONTROL) else p) == value, p
    assert h(ALIAS) == OLD_CONTROL_HASH and h(OLD_CONTROL) != OLD_CONTROL_HASH
    for stage in ('delta_check_01', 'delta_check_02'):
        folder = BASE / stage
        snapshots = obj(folder / 'RESPONSE_ORIGINALS_AND_COPIES.json')
        assert len(snapshots) == 9
        for p, v in snapshots.items(): assert h(p) == h(v['copy']) == v['sha256']
        attempt = obj(folder / 'ATTEMPT.json')
        assert attempt['env'] == ENV and attempt['cwd'] == str(ROOT)
        for token in ('optimize=0', 'dont_write_bytecode=1', 'no_site=1', 'isolated=1'): assert token in attempt['flags']
        source = BASE / ('check_delta.py' if stage.endswith('01') else 'check_delta_02.py')
        assert attempt['script_sha256'] == h(source)
        record = obj(folder / 'EXECUTION.actual.json')
        expected_exit = 1 if stage.endswith('01') else 0
        assert record['completion_result']['exit_code'] == expected_exit
        commands = sorted(folder.glob('raw_cmp_*.command.json'))
        assert len(commands) == (6 if expected_exit else 12)
        for p in commands:
            row = obj(p); prefix = p.name.removesuffix('.command.json')
            pre = obj(folder / (prefix + '.attempt.json'))
            assert all(pre[k] == row[k] for k in ('argv', 'env', 'cwd'))
            assert row['exit'] == 0 and row['env'] == ENV and row['cwd'] == str(ROOT)
            for s in ('stdout', 'stderr'):
                checkpin(folder / (prefix + '.' + s), {'sha256': row[s + '_sha256'], 'bytes': row[s + '_bytes']})
                assert row[s + '_bytes'] == 0
        if expected_exit:
            assert 'AssertionError' in record['completion_result']['output']
            assert not (folder / 'RESULT.json').exists() and not (folder / 'INPUTS_AFTER.json').exists()
        else:
            assert json.loads(record['completion_result']['output']) == obj(folder / 'RESULT.json')
    modes = [D['settings_and_commands'](BASE / ('review_' + mode + '_01'), mode) for mode in ('pair', 'build')]
    root_inputs = archive_commands(PAIR)
    current = obj(BASE / 'CURRENT_FINDINGS.json')
    old = obj(BASE / 'FINDINGS.json')
    assert old['phase'] == 'INITIAL_REVIEW' and old['delta_status'] == 'NOT_YET_SUBMITTED_OR_ASSESSED'
    assert current['verdict'] == current['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'
    assert current['reviewer'] == '/root/p209_a_reviewer' and current['input_round'] == 0
    assert current['findings'] == [] and current['current_open_counts'] == {'critical': 0, 'major': 0, 'minor': 0}
    assert h(BASE / 'DELTA.md') == final_audit['delta_sha256'] == '4ac8b9924864e5a22099f3529c479c452e368b01aa7b24e1dcd1c4bd9c1b5414'
    assert h(BASE / 'CURRENT_FINDINGS.json') == final_audit['current_findings_sha256']
    assert h(RESPONSE) == current['response_sha256'] == '3b84c6c6a39b890562a63fbcb76a1a1fdf683886b9f6670b4bdd05544c6e9459'
    assert obj(BASE / 'auxiliary_01/PDF_PREFLIGHT.json')['verdict'] == 'UNAVAILABLE'
    assert obj(BASE / 'PREFLIGHT_INITIAL_FAILURE.json')['exit'] == 1
    frozen = manifest(FROZEN / 'SHA256SUMS', complete=True)
    author = manifest(PAPER / 'AUTHOR_MANIFEST.sha256')
    assert len(frozen) == 1989 and len(author) == 1985
    assert h(PAPER / 'SHA256SUMS') == h(PAPER / 'AUTHOR_MANIFEST.sha256') == h(FROZEN / 'AUTHOR_MANIFEST.sha256')
    external = obj(FROZEN / 'FROZEN_LINK_MAP.json')['external_input_pins']
    assert len(external) == 132
    for p, value in external.items(): assert h(ALIAS if p == str(OLD_CONTROL) else p) == value
    comparisons = []
    raw1, raw2 = PAIR / 'replay_01/producer.stdout', PAIR / 'replay_02/producer.stdout'
    for a, b in ((raw1, raw2), (raw1, BASE / 'CANONICAL.json'), (raw2, BASE / 'CANONICAL.json'),
                 (PAPER / 'main.pdf', FROZEN / 'main.pdf'),
                 (PAPER / 'SHA256SUMS', FROZEN / 'AUTHOR_MANIFEST.sha256')):
        argv = ['/usr/bin/cmp', '--', str(a), str(b)]
        result = subprocess.run(argv, capture_output=True, env=ENV)
        assert result.returncode == 0
        comparisons.append({'argv': argv, 'exit': result.returncode, 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()})
    for p in list(D['READS']): pin(p, fresh=True)
    assert h(BASE / 'SHA256SUMS') == FINAL and manifest(BASE / 'SHA256SUMS', complete=True) == outer
    print(json.dumps({'schema': 'p209-a-root-delta-closure-v1', 'status': 'ROOT_ACCEPTED_A_DELTA_ORIGINAL_CLOSURE_PASS',
        'paper': 'P209', 'input_round': 0, 'reviewer_delta_accepted': True,
        'root_original_inspection_complete': True, 'root_replay_closure_complete': True,
        'current_open_findings': 0, 'unchanged_author_payloads': len(author), 'unchanged_round0_payloads': len(frozen),
        'author_manifest_sha256': h(PAPER / 'AUTHOR_MANIFEST.sha256'), 'round0_manifest_sha256': h(FROZEN / 'SHA256SUMS'),
        'review_manifest_entries': len(outer), 'review_manifest_sha256': FINAL, 'delta_sha256': h(BASE / 'DELTA.md'),
        'findings_sha256': h(BASE / 'FINDINGS.json'), 'current_findings_sha256': h(BASE / 'CURRENT_FINDINGS.json'),
        'response_sha256': h(RESPONSE), 'root_pair_manifest_sha256': h(PAIR / 'SHA256SUMS'),
        'root_launcher_manifest_sha256': h(LAUNCH / 'SHA256SUMS'),
        'historical_input_aliases': [{'original_path': str(OLD_CONTROL), 'sha256': OLD_CONTROL_HASH, 'physical_path': str(ALIAS)}],
        'initial_review_payloads_preserved': len(initial), 'successful_delta_input_paths': len(before),
        'historical_dependency_pins': len(original_map), 'all_current_read_paths_checked_twice': len(D['READS']),
        'root_pair_input_paths': root_inputs, 'rechecked_original_runtime_and_build_modes': modes,
        'actual_root_raw_comparisons': comparisons, 'failed_delta_audit_exit_preserved': 1,
        'successful_delta_audit_exit': 0, 'optional_structural_preflight': 'UNAVAILABLE',
        'inspection_script_sha256': h(__file__),
        'scope': 'Complete final original/current-input closure plus actual raw comparisons. The already successful root mathematical pair is reused with unchanged full scientific dependency key; no new math/build/render/view or Round1 in this command.'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
