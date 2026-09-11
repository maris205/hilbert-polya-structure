#!/usr/bin/env python3
"""Final documentary inspection only; no producer or scientific import."""
import json
from pathlib import Path
import sys
import traceback
import types

HERE = Path(__file__).resolve().parent
runtime = types.ModuleType('_p211_final_runtime')
runtime.__file__ = str(HERE / 'p211_runtime.py')
sys.modules[runtime.__name__] = runtime
exec(compile(Path(runtime.__file__).read_bytes(), runtime.__file__, 'exec'), runtime.__dict__)
core = runtime.core
OLD = core.ROOT / 'docs/papers204_208_sequence/qa'
ORIGINALS = [OLD / name for name in (
    'p210_b_strict_preparation/run_pair.py', 'p209_author_root_preparation/root_launch_pair.py',
    'root_replays/p210_b_strict_pair_01/sources/run_pair.py',
    'root_replays/p209_author_strict/launcher_root_author_pair_01/root_launch_pair.py',
    'P210_B_ROOT_INITIAL_INSPECTION.md', 'P209_ROOT_AUTHOR_STRICT_REPLAY.md')]
ORIGINALS += [core.ROOT / name for name in (
    'docs/papers211_215_sequence/qa/runtime_readiness/PLAN.md',
    'docs/papers211_215_sequence/qa/runtime_readiness/MANIFEST.sha256',
    'docs/research_state/WORKFLOW.md', '.agents/skills/symbolic-dynamics-research/SKILL.md')]


def main():
    out = Path(sys.argv[1])
    core.need(out.parent == HERE and not core.lexists(out), 'exclusive_final_documentary_output')
    runtime.settings(out / 'never_created_final_checker_cache', core.ROOT)
    out.mkdir()
    (out / 'commands').mkdir()
    core.OUT, core.COMMANDS, core.UNFINALIZED_NATIVE = out, [], []
    errors, checks = [], {}
    inputs = {str(p): core.rich(p) for p in ORIGINALS}
    core.write_json(out / 'ORIGINAL_INPUTS_BEFORE.json', inputs)
    try:
        for index, (first, second) in enumerate([
                (ORIGINALS[0], HERE / 'baseline/p210_b_run_pair.py'),
                (ORIGINALS[1], HERE / 'baseline/p209_root_launch_pair.py'),
                (ORIGINALS[0], ORIGINALS[2]), (ORIGINALS[1], ORIGINALS[3])]):
            core.command('00_baseline_cmp_' + str(index), ['/usr/bin/cmp', '--', str(first), str(second)],
                         timeout=30, cwd=core.ROOT)
        for name in ('runtime_core.py', 'p211_runtime.py', 'prepare_runtime.py', 'test_runtime.py'):
            core.command('01_revision_diff_' + name, ['/usr/bin/diff', '-u', '--',
                         str(HERE / 'discovery01/source_snapshots' / name), str(HERE / name)],
                         timeout=30, cwd=core.ROOT, require_success=False)
            core.need(core.COMMANDS[-1]['exit_code'] == 1 and core.COMMANDS[-1]['stderr']['bytes'] == 0,
                      'complete_expected_revision_diff')
        checks['package_manifests'] = {name: len(core.manifest(HERE / name))
                                       for name in ('discovery01', 'tests01', 'discovery02', 'tests02')}
        old = core.read_json(HERE / 'discovery01/SOURCE_INPUTS_BEFORE.json')
        restored = HERE / 'historical_metadata/REUSE_MAP.discovery01.restored.json'
        core.pin(restored, old[str(HERE / 'REUSE_MAP.json')])
        checks['metadata_restoration'] = {'path': str(restored), **core.value(restored),
            'method': 'After-the-fact exact metadata restoration by removing only the documented new adaptation line; hash matches original pre-correction pin. Not claimed as a pre-edit physical copy.'}
        lock_path = HERE / 'discovery02/RUNTIME_LOCK.json'
        lock = core.read_json(lock_path)
        for p, row in lock['files'].items():
            core.need(core.rich(p) == row, ('current_bounded_runtime_pin', p))
        config = runtime.configuration()
        core.need(config == lock['configuration'] and
                  runtime.loader_search_scope(config) == lock['loader_search_directory_states'], 'current_complete_config_closure')
        checks['runtime_files'] = len(lock['files'])
        checks['loader_search_directories'] = len(lock['loader_search_directory_states'])
        checks['runtime_lock'] = core.rich(lock_path)
        tests = HERE / 'tests02'
        receipts = sorted(tests.rglob('commands/*/RECEIPT.json'))
        for p in receipts:
            row = core.read_json(p)
            attempt = core.read_json(p.with_name('ATTEMPT.json'))
            core.need(row['environment'] == core.ENV and attempt['status'] == 'ATTEMPTED' and
                      attempt['exit_code'] is None and all(attempt[k] == row[k] for k in attempt if k not in ('status', 'exit_code')),
                      ('literal_native_ATTEMPT_binding', str(p)))
            for stream in ('stdout', 'stderr'):
                core.pin(p.with_name(stream + '.raw'), row[stream])
            if row['spawned']:
                settled = row['process_group_settlement']
                core.need(settled['quiescent'] and settled['native_returncode'] == row['exit_code'] and
                          row['pid'] == settled['owned_pgid'], 'actual_native_settlement_identity')
            else:
                core.need(row['status'] == 'SPAWN_FAILED' and row['exit_code'] is None, 'no_fabricated_spawn_exit')
        checks['test_complete_native_receipts'] = len(receipts)
        checks['test_actual_attempt_records'] = len(list(tests.rglob('commands/*/ATTEMPT.json')))
        phases = []
        for mode in ('initial', 'pair'):
            attempt = tests / ('fixture_' + mode)
            stages = ('outer', 'launcher', 'recorder', 'child01') + (('child02',) if mode == 'pair' else ())
            for stage in stages:
                p = attempt / stage
                core.need(core.read_json(p / 'RESULT.json')['status'] == 'PASS', 'fixture_stage_pass')
                before_name = 'INPUTS_BEFORE_SCIENCE.json' if stage == 'recorder' else 'INPUTS_BEFORE.json'
                core.need(core.read_json(p / before_name) == core.read_json(p / 'INPUTS_AFTER.json'), 'full_stage_input_equality')
                for phase in ('BEFORE', 'AFTER'):
                    sample = core.read_json(p / ('RUNTIME_' + phase + '.json'))
                    core.need(sample['environment'] == core.ENV and not core.lexists(sample['pycache_prefix']), 'all_layer_actual_ENV_cache')
                    core.need(core.sha256(sample['proc_maps'].encode()).hexdigest() == sample['proc_maps_sha256'] and
                              len(sample['proc_maps'].encode()) == sample['proc_maps_bytes'], 'entire_maps_sample_bytes')
                entered = core.read_json(p / 'ENTERED.json')
                bind_path = tests / (mode + '.binding.json')
                core.need(entered['orig_argv'] == runtime.worker_argv(stage, bind_path, core.value(bind_path)['sha256'], attempt),
                          'actual_all_layer_original_argv')
                phases.append(mode + ':' + stage)
        checks['closed_fixture_stages'] = phases
        checks['test_predicate_groups'] = len(core.read_json(tests / 'RESULT.json')['checks'])
        core.need(core.read_json(tests / 'RESULT.json')['status'] == 'PASS_PURE_INFRASTRUCTURE_TESTS', 'actual_pure_test_status')
    except BaseException as exc:
        errors.append({'error': repr(exc), 'traceback': traceback.format_exc()})
    after = {p: core.rich(p) for p in inputs}
    core.write_json(out / 'ORIGINAL_INPUTS_AFTER.json', after)
    if after != inputs:
        errors.append({'error': 'original inputs changed'})
    core.write_json(out / 'RESULT.json', {'status': 'FAIL_PRESERVED' if errors else 'PASS_DOCUMENTARY_CHECKS',
                    'checks': checks, 'errors': errors, 'commands': core.COMMANDS, 'scientific_executions': 0})
    seal = core.seal() if not core.UNFINALIZED_NATIVE else None
    print(json.dumps({'status': 'FAIL_PRESERVED' if errors else 'PASS_DOCUMENTARY_CHECKS',
                      'checks': checks, 'errors': errors, 'output': str(out), 'seal': seal}, sort_keys=True))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
