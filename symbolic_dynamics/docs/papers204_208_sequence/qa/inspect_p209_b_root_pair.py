#!/usr/bin/env python3
"""Read-only root closure of the new B pair; no producer or build launch.

Reuses only pin/manifest/JSON readers from the fully inspected initial
archive auditor. No mathematical or replay implementation is imported.
"""
import json
from pathlib import Path
import runpy
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
REVIEW = ROOT / 'docs/papers204_208_sequence/reviews/p209_b'
BASE = QA / 'root_replays/p209_b_strict'
PAIR = BASE / 'root_b_pair_01'
LAUNCH = BASE / 'launcher_root_b_pair_01'
PREP = QA / 'p209_b_root_preparation'
HELPER = QA / 'inspect_p209_a_initial.py'
D = runpy.run_path(str(HELPER))
pin, obj, checkpin, manifest = (D[n] for n in ('pin', 'obj', 'checkpin', 'manifest'))
ENV = D['ENV']


def settings(obs, folder, parent=False):
    assert obs['env'] == ENV and obs['cwd'] == str(ROOT if parent else folder)
    assert not obs['cache_exists']
    if parent:
        assert obs['optimization'] == 0
        flags = obs['flags']
        for flag in ('optimize=0', 'dont_write_bytecode=1', 'no_site=1', 'isolated=1'):
            assert flag in flags
        cache = folder / 'never_created_parent_cache'
    else:
        assert obs['optimize'] == 0 and obs['isolated'] == obs['no_site'] == 1
        assert obs['dont_write_bytecode']
        cache = folder / 'never_created_child_cache'
    assert obs['pycache_prefix'] == str(cache) and not cache.exists()


def main():
    pin(HELPER); pin(Path(__file__))
    expected = [(PAIR, '51dd81f7c6dac413612ef57437dde389c3b20a44e94412dd7bee008a77c9c841', 462),
                (LAUNCH, '7874f814ce0cf9177b417ae1d1b1e10f233f51fd92c3826d5753f388ed994eed', 10),
                (PREP, '4beef4a4e9f60c6039ceb89df1f3a12b2d61049ad75654e35825390c4b68133a', 57),
                (REVIEW, 'd88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea', 1298)]
    saved = {}
    for base, h, n in expected:
        assert pin(base / 'SHA256SUMS')['sha256'] == h
        saved[str(base)] = manifest(base / 'SHA256SUMS', complete=True)
        assert len(saved[str(base)]) == n
    for p in sorted(BASE.rglob('SHA256SUMS')):
        manifest(p, complete=True)
    r = obj(PAIR / 'RECEIPT.json')
    assert r['status'] == 'PASS_ROOT_REVIEW_B_PAIR' and r['failures'] == []
    assert not r['result']['canonical_adopted']
    before = obj(PAIR / 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json')
    assert before == obj(PAIR / 'ALL_INPUTS_AFTER.json') and len(before) == 5164
    for p, value in before.items(): checkpin(p, value)
    for stem in ('RUNTIME', 'CONFIGURATION', 'SCIENCE'):
        a = obj(PAIR / (stem + '_BEFORE.json'))
        if stem != 'SCIENCE': assert a == obj(PAIR / (stem + '_AFTER.json'))
    config = obj(PAIR / 'CONFIGURATION_BEFORE.json')
    for p, v in config['optional'].items():
        q = Path(p)
        assert q.exists() == v['exists'] and q.is_file() == v['is_file'] and str(q.resolve()) == v['resolved']
        if q.is_file(): checkpin(q, {k: v[k] for k in ('sha256', 'bytes')})
    for p, names in config['directories'].items():
        q = Path(p)
        assert (sorted(str(x) for x in q.rglob('*') if x.is_file()) if q.is_dir() else None) == names
    closure = obj(PAIR / 'OBSERVED_CLOSURE.json')
    assert closure['uncovered'] == closure['bytecode'] == []
    for phase in ('BEFORE', 'AFTER'): settings(obj(PAIR / ('PARENT_' + phase + '.json')), PAIR, True)
    commands = obj(PAIR / 'ALL_COMMAND_RECORDS.json')
    assert len(commands) == 85 and sum(x['tag'].startswith('ldd_') for x in commands) == 80
    for entry in commands:
        folder, tag, row = Path(entry['folder']), entry['tag'], entry['command']
        assert folder.is_relative_to(PAIR) and obj(folder / (tag + '.command.json')) == row
        attempt = obj(folder / (tag + '.attempt.json'))
        assert all(attempt[k] == row[k] for k in ('argv', 'cwd', 'env', 'stdout', 'stderr'))
        assert row['process_outcome'] == 'COMPLETED' and row['exit'] == 0
        assert row['spawn_error'] is None and row['cleanup'] == [] and row['env'] == ENV
        for stream in ('stdout', 'stderr'): checkpin(folder / row[stream], row[stream + '_info'])
        maps = obj(folder / (tag + '.maps.json'))
        assert sorted({p for sample in maps['samples'] for p in sample['mapped_files']}) == entry['mapped_files']
        for p in entry['mapped_files']:
            assert str(Path(p).resolve()) in {v['resolved'] for v in before.values()}
    linkage = obj(PAIR / 'LINKAGE.json')
    assert not linkage['pending_targets'] and len(linkage['entries']) == 80
    assert all(x['status'] == 'VALIDATED' for x in linkage['entries'])
    science = obj(PAIR / 'SCIENCE_BEFORE.json')
    assert len(science) == 2025
    assert all(before[p] == v for p, v in science.items())
    runtime = obj(PAIR / 'RUNTIME_BEFORE.json')
    assert len(runtime) == 3133 and all(before[p] == v for p, v in runtime.items())
    for label in ('replay_01', 'replay_02'):
        folder = PAIR / label
        child = obj(folder / 'RECEIPT.json')
        assert child['status'] == 'PASS' and child['checks'] == 54794 and child['total_states'] == 3414
        assert child['source_only_initial_names'] == ['bootstrap.py', 'verify.py']
        for name in child['source_only_initial_names']:
            assert pin(folder / 'source_inputs' / name)['sha256'] == pin(REVIEW / name)['sha256']
        for phase in ('before', 'after'): settings(obj(folder / ('child.' + phase + '.json')), folder)
        child_before = obj(folder / 'INPUTS_BEFORE.json')
        assert child_before == obj(folder / 'INPUTS_AFTER.json')
        for p, value in child_before.items(): checkpin(p, value)
        assert child['inputs_unchanged'] and child['failure'] is None
        assert not child['closure']['uncovered'] and not child['closure']['bytecode']
        for phase in ('before', 'after'):
            assert obj(folder / ('child.' + phase + '.json'))['orig_argv'] == child['command']['argv']
        payload = obj(folder / 'producer.stdout')
        assert payload['schema'] == 'p209-b-ports-constructive-carrier-v1'
        assert payload['max_n'] == 5 and payload['states'] == 3414 and payload['checks'] == 54794
        assert [b['n'] for b in payload['boxes']] == list(range(6))
        assert all(len(b['rows']) == b['states'] for b in payload['boxes'])
    l = obj(LAUNCH / 'RECEIPT.json')
    assert l['status'] == 'PASS_ROOT_LAUNCH' and l['exit'] == 0 and l['outcome'] == 'COMPLETED'
    assert l['failure'] is None and l['inputs_unchanged'] and l['cache_absent']
    assert l['env'] == ENV and l['cwd'] == str(ROOT) and not Path(l['launcher_cache']).exists()
    for flag in ('optimize=0', 'dont_write_bytecode=1', 'no_site=1', 'isolated=1'): assert flag in l['launcher_flags']
    inputs = obj(LAUNCH / 'INPUTS_BEFORE.json')
    assert inputs == obj(LAUNCH / 'INPUTS_AFTER.json')
    for p, v in inputs.items(): checkpin(p, v)
    assert len(inputs) == 2026
    for name in ('root_launch_pair.py', 'root_record_pair.py'):
        assert pin(LAUNCH / name)['sha256'] == pin(PREP / name)['sha256']
    for name in ('bootstrap.py', 'verify.py'):
        assert pin(LAUNCH / name)['sha256'] == pin(REVIEW / name)['sha256']
    fixed = obj(PREP / 'FIXED_INPUTS.json')
    assert len(fixed) == 2021
    for p, v in fixed.items(): checkpin(p, v)
    attempt = obj(LAUNCH / 'PRE_SPAWN_ATTEMPT.json')
    assert attempt['exit'] is None and attempt['outcome'] == 'NOT_STARTED'
    assert all(attempt[k] == l[k] for k in ('argv', 'cwd', 'env', 'stdout', 'stderr', 'launcher_orig_argv', 'launcher_flags', 'launcher_cache'))
    assert l['argv'] == ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
        'pycache_prefix=' + str(PAIR / 'never_created_parent_cache'),
        str(PREP / 'root_record_pair.py'), 'pair', 'root_b_pair_01']
    assert l['recorder_closure']['payloads'] == 462 and l['recorder_closure']['status'] == r['status']
    checkpin(PAIR / 'SHA256SUMS', l['recorder_seal'])
    for stream in ('recorder.stdout', 'recorder.stderr'): checkpin(LAUNCH / stream, l[stream + '_pin'])
    assert obj(LAUNCH / 'recorder.stdout')['status'] == r['status']
    assert pin(PAIR / 'executed_recorder.py')['sha256'] == pin(PREP / 'root_record_pair.py')['sha256']
    raw1, raw2, canonical = PAIR / 'replay_01/producer.stdout', PAIR / 'replay_02/producer.stdout', REVIEW / 'CANONICAL.json'
    comparisons = []
    for a, b in ((raw1, raw2), (raw1, canonical), (raw2, canonical)):
        argv = ['/usr/bin/cmp', '--', str(a), str(b)]
        result = subprocess.run(argv, capture_output=True, env=ENV)
        assert result.returncode == 0
        comparisons.append({'argv': argv, 'exit': result.returncode, 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()})
    comparison_before = obj(PAIR / 'comparison/INPUTS_BEFORE.json')
    assert comparison_before == obj(PAIR / 'comparison/INPUTS_AFTER.json')
    for p, v in comparison_before.items(): checkpin(p, v)
    for p in list(D['READS']): pin(p, fresh=True)
    for base, _, _ in expected: assert manifest(base / 'SHA256SUMS', complete=True) == saved[str(base)]
    print(json.dumps({'status': 'PASS_ROOT_NEW_B_PAIR_FULL_CLOSURE', 'pair_payloads': 462, 'launcher_payloads': 10,
        'current_review_payloads': 1298, 'known_pair_inputs': len(before), 'all_current_paths_twice': len(D['READS']),
        'checks_each': 54794, 'original_states': 3414, 'commands_exit_zero': 85, 'canonical_adopted': False,
        'canonical': r['result']['canonical'], 'actual_new_root_raw_comparisons': comparisons,
        'boundary': 'Actual root mathematical pair has completed; this command inspects its full originals and current dependencies. No delta, new build/view, or new independent review.'}, indent=2))


if __name__ == '__main__':
    main()
