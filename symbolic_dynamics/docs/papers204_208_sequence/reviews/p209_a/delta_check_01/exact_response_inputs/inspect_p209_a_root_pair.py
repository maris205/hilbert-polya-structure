#!/usr/bin/env python3
"""Read-only root closure of the new A pair; no producer or build launch.

Reuses only pin/manifest/JSON readers from the fully inspected initial
archive auditor. No mathematical or replay implementation is imported.
"""
import json
from pathlib import Path
import runpy
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
REVIEW = ROOT / 'docs/papers204_208_sequence/reviews/p209_a'
BASE = QA / 'root_replays/p209_a_strict'
PAIR = BASE / 'root_a_pair_01'
LAUNCH = BASE / 'launcher_root_a_pair_01'
PREP = QA / 'p209_a_root_preparation'
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
    expected = [(PAIR, 'e1d7a773e1ed5c7ef347922926774f258dd42a096bafff4b50907d0e68a02728', 462),
                (LAUNCH, 'c12927453cd0f09591a2d36f21c29e9baa3a6c7613a5e16a65198fd43641e3b6', 10),
                (PREP, 'bcbf02f2fdfde47e21cee023cdad8a35aaa8230b4be8717962530e1da57feea2', 6),
                (REVIEW, D['SEAL'], 1227)]
    saved = {}
    for base, h, n in expected:
        assert pin(base / 'SHA256SUMS')['sha256'] == h
        saved[str(base)] = manifest(base / 'SHA256SUMS', complete=True)
        assert len(saved[str(base)]) == n
    for p in sorted(BASE.rglob('SHA256SUMS')):
        manifest(p, complete=True)
    r = obj(PAIR / 'RECEIPT.json')
    assert r['status'] == 'PASS_ROOT_REVIEW_A_PAIR' and r['failures'] == []
    assert not r['result']['canonical_adopted']
    before = obj(PAIR / 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json')
    assert before == obj(PAIR / 'ALL_INPUTS_AFTER.json') and len(before) == 5147
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
    for label in ('replay_01', 'replay_02'):
        folder = PAIR / label
        child = obj(folder / 'RECEIPT.json')
        assert child['status'] == 'PASS' and child['checks'] == 135605 and child['total_states'] == 3414
        assert child['source_only_initial_names'] == ['bootstrap.py', 'verify.py']
        for name in child['source_only_initial_names']:
            assert pin(folder / 'source_inputs' / name)['sha256'] == pin(REVIEW / name)['sha256']
        for phase in ('before', 'after'): settings(obj(folder / ('child.' + phase + '.json')), folder)
        assert obj(folder / 'INPUTS_BEFORE.json') == obj(folder / 'INPUTS_AFTER.json')
    l = obj(LAUNCH / 'RECEIPT.json')
    assert l['status'] == 'PASS_ROOT_LAUNCH' and l['exit'] == 0 and l['outcome'] == 'COMPLETED'
    assert l['failure'] is None and l['inputs_unchanged'] and l['cache_absent']
    assert l['env'] == ENV and l['cwd'] == str(ROOT) and not Path(l['launcher_cache']).exists()
    for flag in ('optimize=0', 'dont_write_bytecode=1', 'no_site=1', 'isolated=1'): assert flag in l['launcher_flags']
    inputs = obj(LAUNCH / 'INPUTS_BEFORE.json')
    assert inputs == obj(LAUNCH / 'INPUTS_AFTER.json')
    for p, v in inputs.items(): checkpin(p, v)
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
    for p in list(D['READS']): pin(p, fresh=True)
    for base, _, _ in expected: assert manifest(base / 'SHA256SUMS', complete=True) == saved[str(base)]
    print(json.dumps({'status': 'PASS_ROOT_NEW_A_PAIR_FULL_CLOSURE', 'pair_payloads': 462, 'launcher_payloads': 10,
        'current_review_payloads': 1227, 'known_pair_inputs': len(before), 'all_current_paths_twice': len(D['READS']),
        'checks_each': 135605, 'original_states': 3414, 'commands_exit_zero': 85, 'canonical_adopted': False,
        'canonical': r['result']['canonical'], 'actual_new_root_raw_comparisons': comparisons,
        'boundary': 'Actual root mathematical pair has completed; this command inspects its full originals and current dependencies. No delta, new build/view, or new independent review.'}, indent=2))


if __name__ == '__main__':
    main()
