#!/usr/bin/env python3
"""Actual native pure-infrastructure tests, never any scientific source."""
import json
from pathlib import Path
import sys
import traceback
import types

HERE = Path(__file__).resolve().parent
runtime = types.ModuleType('_p211_test_runtime')
runtime.__file__ = str(HERE / 'p211_runtime.py')
sys.modules[runtime.__name__] = runtime
exec(compile(Path(runtime.__file__).read_bytes(), runtime.__file__, 'exec'), runtime.__dict__)
core = runtime.core


def check(condition, label, checks):
    core.need(condition, label)
    checks.append(label)


def raises(action, label, checks):
    try:
        action()
    except (AssertionError, ValueError, RuntimeError, KeyError):
        checks.append(label)
        return
    raise AssertionError('Expected refusal: ' + label)


def python_args(cache, code):
    return [str(runtime.PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(cache), '-c', code]


def fixture_binding(out, lock_path, mode):
    params = out / 'parameters.fixture.json'
    source = HERE / 'fixtures/verify_fixture.py'
    canonical = out / 'CANONICAL.fixture.json'
    return {'format': 'p211-runtime-binding-v1', 'approved': True,
            'purpose': 'INFRASTRUCTURE_TEST_ONLY', 'role': 'infra_fixture', 'mode': mode,
            'attempt': str(out / ('fixture_' + mode)),
            'reviewed_static_source_import_closure': True, 'reviewed_schema_and_parameters': True,
            'declared_imports': runtime.ROLE_IMPORTS, 'local_helper_imports': [],
            'adapter_sources': {str(p): core.rich(p) for p in runtime.SOURCE_FILES},
            'runtime_lock': {'path': str(lock_path), **core.rich(lock_path)},
            'entry': 'verify.py', 'parameters': 'parameters.json',
            'capsule_files': [{'name': 'verify.py', 'path': str(source), **core.value(source)},
                              {'name': 'parameters.json', 'path': str(params), **core.value(params)}],
            'argv_template': ['$ENTRY', '--parameters', '$PARAMETERS'],
            'parameter_locator': 'explicit_absolute_argv',
            'canonical': {'path': str(canonical), **(core.value(canonical) if mode == 'pair' else {'sha256': None, 'bytes': None})},
            'schema': {'top_keys': ['fixture_only', 'value'], 'equalities':
                       [{'path': ['fixture_only'], 'value': True}, {'path': ['value'], 'value': 17}], 'lengths': []},
            'success_stderr': 'empty', 'timeouts': {'science': 30, 'native': 30, 'envelope': 90},
            'provenance_inputs': []}


def main():
    core.need(len(sys.argv) == 3, 'ABSOLUTE_NEW_TEST_OUTPUT ABSOLUTE_RUNTIME_LOCK')
    out, lock_path = map(Path, sys.argv[1:])
    core.need(out.is_absolute() and out.parent == HERE and not core.lexists(out), 'new_owned_test_attempt')
    runtime.settings(out / 'never_created_tester_cache', core.ROOT)
    out.mkdir(mode=0o700)
    (out / 'commands').mkdir()
    (out / 'source_snapshots').mkdir()
    core.OUT, core.COMMANDS, core.UNFINALIZED_NATIVE = out, [], []
    checks, errors, source_before = [], [], None
    try:
        sources = list(runtime.SOURCE_FILES) + [Path(__file__).resolve(), HERE / 'fixtures/verify_fixture.py', lock_path]
        source_before = {str(p): core.rich(p) for p in sources}
        core.write_json(out / 'SOURCE_INPUTS_BEFORE.json', source_before)
        core.write_json(out / 'TESTER_SETTINGS.json', {'argv': sys.argv, 'orig_argv': sys.orig_argv,
                        'cwd': str(Path.cwd()), 'environment': dict(core.os.environ),
                        'flags': repr(sys.flags), 'cache': sys.pycache_prefix})
        for number, p in enumerate(sources[:-1]):
            dest = out / 'source_snapshots' / p.name
            core.command('00_snapshot_' + str(number), ['/usr/bin/cp', '--no-clobber', '--', str(p), str(dest)],
                         timeout=30, cwd=core.ROOT)
            core.command('00_snapshot_cmp_' + str(number), ['/usr/bin/cmp', '--', str(p), str(dest)],
                         timeout=30, cwd=core.ROOT)
        good = b'{"fixture_only":true,"value":17}\n'
        schema = {'top_keys': ['fixture_only', 'value'],
                  'equalities': [{'path': ['value'], 'value': 17}], 'lengths': []}
        check(runtime.check_schema(good, schema)['value'] == 17, 'exact_JSON_schema_positive', checks)
        for data, label in [(b'{"a":1,"a":2}\n', 'reject_duplicate_JSON'),
                            (b'{"a":NaN}\n', 'reject_nonfinite_JSON'),
                            (b'{"value": 17}\n', 'reject_noncompact_JSON'),
                            (good + b'\n', 'reject_extra_stdout_byte')]:
            raises(lambda data=data: runtime.exact_json(data), label, checks)
        pending = HERE / 'BINDING.pending.json'
        raises(lambda: runtime.load_binding(pending, core.value(pending)['sha256'], out / 'never_created_pending'),
               'reject_unapproved_science_binding_before_attempt', checks)
        check(not (out / 'never_created_pending').exists(), 'pending_binding_created_no_attempt', checks)
        source = HERE / 'fixtures/verify_fixture.py'
        raises(lambda: runtime.covered_opens([{'path': str(source)}], {}, out / 'absent_cache', out, True, set()),
               'reject_unfrozen_existing_ordinary_input', checks)
        core.command('01_success', python_args(out / 'unused_success_cache', 'print("native fixture success")'),
                     timeout=10, cwd=core.ROOT)
        row = core.COMMANDS[-1]
        check(row['exit_code'] == 0 and row['streams_complete'] and row['pid'] == row['process_group_settlement']['owned_pgid'] and
              not row['process_group_settlement']['remaining_members'], 'actual_success_native_identity_and_quiescence', checks)
        core.command('02_nonzero', python_args(out / 'unused_nonzero_cache',
                     'import sys; print("partial fixture"); sys.stderr.write("fixture error\\n"); sys.exit(7)'),
                     timeout=10, cwd=core.ROOT, require_success=False)
        row = core.COMMANDS[-1]
        check(row['exit_code'] == row['wrapper_exit_code'] == 7 and row['streams_complete'] and row['stderr']['bytes'] > 0,
              'actual_nonzero_preserved_not_success', checks)
        core.command('03_timeout', python_args(out / 'unused_timeout_cache',
                     'import time; print("before timeout", flush=True); time.sleep(20)'),
                     timeout=0.2, cwd=core.ROOT, require_success=False)
        row = core.COMMANDS[-1]
        check(row['timed_out'] and row['wrapper_exit_code'] == 124 and not row['streams_complete'] and
              row['process_group_settlement']['quiescent'] and row['process_group_settlement']['signals'],
              'actual_timeout_owned_cleanup_does_not_upgrade_outcome', checks)
        core.command('04_spawn_failure', [str(out / 'absent_executable')], timeout=10, cwd=core.ROOT,
                     require_success=False)
        row = core.COMMANDS[-1]
        check(row['status'] == 'SPAWN_FAILED' and row['exit_code'] is None and row['wrapper_exit_code'] == 127 and
              row['process_group_settlement'] is None, 'actual_spawn_failure_not_fabricated_native_exit', checks)
        bad_cache = out / 'existing_cache'
        bad_cache.mkdir()
        argv = [str(runtime.PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(bad_cache),
                str(HERE / 'p211_runtime.py'), 'probe', 'outer', str(bad_cache), str(core.ROOT)]
        core.command('05_existing_cache_refusal', argv, timeout=10, cwd=core.ROOT, require_success=False)
        check(core.COMMANDS[-1]['exit_code'] != 0, 'actual_existing_cache_refused_before_probe', checks)
        env_cache = out / 'unused_wrong_environment_cache'
        argv = ['/usr/bin/env', 'LC_ALL=C', str(runtime.PYTHON), '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(env_cache), str(HERE / 'p211_runtime.py'), 'probe', 'launcher',
                str(env_cache), str(core.ROOT)]
        core.command('06_environment_refusal', argv, timeout=10, cwd=core.ROOT, require_success=False)
        check(core.COMMANDS[-1]['exit_code'] != 0, 'actual_wrong_child_environment_refused', checks)
        core.write_json(out / 'parameters.fixture.json', {'fixture_only': True, 'value': 17})
        for mode in ('initial', 'pair'):
            binding = fixture_binding(out, lock_path, mode)
            path = out / (mode + '.binding.json')
            core.write_json(path, binding)
            attempt = Path(binding['attempt'])
            raw = core.command('07_fixture_' + mode,
                               runtime.worker_argv('outer', path, core.value(path)['sha256'], attempt),
                               timeout=120, cwd=core.ROOT, require_success=False)
            row = core.COMMANDS[-1]
            core.need(row['exit_code'] == 0 and row['streams_complete'] and row['stderr']['bytes'] == 0,
                      ('full_fixture_pipeline_failed_preserved', mode, row))
            core.manifest(attempt)
            result = core.read_json(attempt / 'recorder/RESULT.json')
            check(result['status'] == 'PASS' and result['output']['actual_raw_comparisons'] == (0 if mode == 'initial' else 3),
                  'actual_full_' + mode + '_pipeline', checks)
            if mode == 'initial':
                stdout = Path(result['output']['raw_stdout'][0]['path'])
                canonical = out / 'CANONICAL.fixture.json'
                check(stdout.read_bytes() == good and not canonical.exists(), 'initial_does_not_adopt_canonical', checks)
                core.command('08_fixture_publish_copy', ['/usr/bin/cp', '--no-clobber', '--', str(stdout), str(canonical)],
                             timeout=30, cwd=core.ROOT)
                core.command('08_fixture_publish_cmp', ['/usr/bin/cmp', '--', str(stdout), str(canonical)],
                             timeout=30, cwd=core.ROOT)
        # Failure injection is explicit: the native process really exits, but
        # the settlement report is withheld. The code under test must not seal.
        saved_settle = core.settle_group
        actual_settlement = []
        def withhold_settlement(process, terminate=False):
            actual = saved_settle(process, terminate=terminate)
            actual_settlement.append(actual)
            return {**actual, 'quiescent': False, 'test_injected_unknown_settlement': True}
        core.settle_group = withhold_settlement
        try:
            raises(lambda: core.command('09_injected_unfinalized', ['/usr/bin/true'], timeout=10,
                                        cwd=core.ROOT, require_success=False), 'injected_unfinalized_refuses_stream_hashes', checks)
            raises(core.seal, 'injected_unfinalized_refuses_seal', checks)
        finally:
            core.settle_group = saved_settle
        check(actual_settlement and actual_settlement[0]['quiescent'] and
              not actual_settlement[0]['remaining_members'], 'separate_actual_settlement_before_test_envelope_seal', checks)
        core.write_json(out / 'INJECTED_SETTLEMENT_TEST.json',
                        {'injection': 'Deliberately report unknown quiescence after actual native settlement.',
                         'actual_settlement': actual_settlement, 'code_under_test_refused_its_seal': True,
                         'limitation': 'Not an actual escaped or unkillable descendant test.',
                         'preserved_unfinalized_labels': list(core.UNFINALIZED_NATIVE)})
        core.UNFINALIZED_NATIVE = []
    except BaseException as exc:
        errors.append({'type': type(exc).__name__, 'error': repr(exc), 'traceback': traceback.format_exc()})
    finally:
        if source_before is not None:
            try:
                after = {p: core.rich(p) for p in source_before}
                core.write_json(out / 'SOURCE_INPUTS_AFTER.json', after)
                core.need(after == source_before, 'unchanged_entire_test_source_and_runtime_lock')
            except BaseException as exc:
                errors.append({'stage': 'source_closure', 'error': repr(exc)})
    core.write_json(out / 'RESULT.json', {'status': 'FAIL_PRESERVED' if errors else 'PASS_PURE_INFRASTRUCTURE_TESTS',
                    'checks': checks, 'errors': errors, 'commands': core.COMMANDS,
                    'scientific_executions': 0, 'fixture_producer_invocations_if_complete': 3,
                    'KIP_source_read_or_imported': False})
    seal = core.seal() if not core.UNFINALIZED_NATIVE else None
    print(json.dumps({'status': 'FAIL_PRESERVED' if errors else 'PASS_PURE_INFRASTRUCTURE_TESTS',
                      'checks': len(checks), 'errors': errors, 'output': str(out), 'seal': seal}, sort_keys=True))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
