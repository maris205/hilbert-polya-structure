#!/usr/bin/env python3
"""Import-only bounded discovery and native documentary checks; no science."""
import ast
import json
import os
from pathlib import Path
import sys
import traceback
import types

HERE = Path(__file__).resolve().parent
runtime = types.ModuleType('_p211_preparation_runtime')
runtime.__file__ = str(HERE / 'p211_runtime.py')
sys.modules[runtime.__name__] = runtime
exec(compile(Path(runtime.__file__).read_bytes(), runtime.__file__, 'exec'), runtime.__dict__)
core = runtime.core
OLD_B = core.ROOT / 'docs/papers204_208_sequence/qa/p210_b_strict_preparation/run_pair.py'
OLD_OUTER = core.ROOT / 'docs/papers204_208_sequence/qa/p209_author_root_preparation/root_launch_pair.py'
SOURCES = [HERE / name for name in ('runtime_core.py', 'p211_runtime.py', 'prepare_runtime.py', 'test_runtime.py',
                                   'fixtures/verify_fixture.py', 'fixtures/pre_spawn_refusal.py')]


def static_checks():
    trees = {str(p): ast.parse(p.read_bytes(), filename=str(p)) for p in SOURCES}
    for p in SOURCES:
        compile(p.read_bytes(), str(p), 'exec')
    old = ast.parse(OLD_B.read_bytes(), filename=str(OLD_B))
    old_functions = {n.name: n for n in old.body if isinstance(n, ast.FunctionDef)}
    new_functions = {n.name: n for n in trees[str(HERE / 'runtime_core.py')].body if isinstance(n, ast.FunctionDef)}
    reuse = core.read_json(HERE / 'REUSE_MAP.json')
    checked = []
    for name in reuse['unchanged_functions']:
        core.need(ast.dump(old_functions[name], include_attributes=False) ==
                  ast.dump(new_functions[name], include_attributes=False), ('unchanged_accepted_function', name))
        checked.append(name)
    core.need(set(new_functions) == set(checked) | {'command'}, 'exact_selected_core_function_set')
    core.need(ast.dump(old_functions['command'], include_attributes=False) !=
              ast.dump(new_functions['command'], include_attributes=False), 'explicit_disclosed_command_adapter')
    return {'compiled_without_execution': [str(p) for p in SOURCES],
            'unchanged_accepted_functions': checked, 'changed_core_functions': ['command'],
            'scientific_files_read_or_imported': [], 'no_scientific_execution': True}


def loader_configuration_scope(configuration):
    return runtime.loader_search_scope(configuration)


def main():
    core.need(len(sys.argv) == 2, 'ABSOLUTE_NEW_PREPARATION_OUTPUT')
    out = Path(sys.argv[1])
    core.need(out.is_absolute() and out.parent == HERE and not core.lexists(out), 'new_owned_preparation_attempt')
    runtime.settings(out / 'never_created_preparer_cache', core.ROOT)
    out.mkdir(mode=0o700)
    (out / 'commands').mkdir()
    (out / 'source_snapshots').mkdir()
    (out / 'empty_probe_capsule').mkdir()
    core.OUT, core.COMMANDS, core.UNFINALIZED_NATIVE = out, [], []
    errors, lock, source_before = [], None, None
    try:
        sources = SOURCES + [HERE / 'REUSE_MAP.json', HERE / 'baseline/p210_b_run_pair.py',
                             HERE / 'baseline/p209_root_launch_pair.py', OLD_B, OLD_OUTER]
        source_before = {str(p): core.rich(p) for p in sources}
        core.write_json(out / 'SOURCE_INPUTS_BEFORE.json', source_before)
        core.write_json(out / 'PREPARER_SETTINGS.json', {'argv': sys.argv, 'orig_argv': sys.orig_argv,
                        'cwd': str(Path.cwd()), 'environment': dict(os.environ), 'cache': sys.pycache_prefix,
                        'flags': repr(sys.flags), 'scope': 'Documentary preparer, not a scientific producer'})
        for number, p in enumerate(SOURCES):
            target = out / 'source_snapshots' / p.name
            core.command('00_snapshot_' + str(number), ['/usr/bin/cp', '--no-clobber', '--', str(p), str(target)],
                         timeout=60, cwd=core.ROOT)
            core.command('00_snapshot_cmp_' + str(number), ['/usr/bin/cmp', '--', str(p), str(target)],
                         timeout=60, cwd=core.ROOT)
        for label, original, copy in [('01_baseline_B', OLD_B, HERE / 'baseline/p210_b_run_pair.py'),
                                     ('01_baseline_outer', OLD_OUTER, HERE / 'baseline/p209_root_launch_pair.py')]:
            core.command(label, ['/usr/bin/cmp', '--', str(original), str(copy)], timeout=60, cwd=core.ROOT)
        for label, original, adapted in [('02_core_diff', OLD_B, HERE / 'runtime_core.py'),
                                        ('02_outer_adapter_diff', OLD_OUTER, HERE / 'p211_runtime.py')]:
            core.command(label, ['/usr/bin/diff', '-u', '--', str(original), str(adapted)],
                         timeout=60, cwd=core.ROOT, require_success=False)
            core.need(core.COMMANDS[-1]['exit_code'] == 1 and core.COMMANDS[-1]['stderr']['bytes'] == 0,
                      'expected_complete_diff_exit_one')
        core.write_json(out / 'STATIC_CHECK.json', static_checks())
        probes = []
        for tag in ('outer', 'launcher', 'recorder', 'child'):
            cache = out / ('never_created_probe_' + tag + '_cache')
            cwd = out / 'empty_probe_capsule' if tag == 'child' else core.ROOT
            argv = [str(runtime.PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(cache),
                    str(HERE / 'p211_runtime.py'), 'probe', tag, str(cache), str(cwd)]
            raw = core.command('03_probe_' + tag, argv, timeout=60, cwd=cwd)
            row = json.loads(raw)
            core.need(row['status'] == 'IMPORT_ONLY_NO_SCIENTIFIC_SOURCE_READ' and row['layer'] == tag and
                      row['declared_imports'] == runtime.ROLE_IMPORTS, 'actual_exact_probe_scope')
            core.need(row['sample']['environment'] == core.ENV and row['sample']['cwd'] == str(cwd) and
                      row['sample']['pycache_prefix'] == str(cache) and not core.lexists(cache), 'actual_probe_settings')
            probes.append(row)
        conf = probes[0]['configuration']
        core.need(all(row['configuration'] == conf for row in probes), 'all_layer_configuration_agreement')
        search_dirs = loader_configuration_scope(conf)
        names = set(runtime.NATIVE_FILES)
        for probe in probes:
            names.update(probe['sample']['mapped_files'])
            names.update(row['path'] for row in probe['sample']['modules'].values())
        names.update(p for p, row in conf['paths'].items() if row['is_file'])
        targets = sorted(set(runtime.NATIVE_FILES) - {'/usr/bin/ldd'} |
                         {p for p in names if p.endswith('.so') and p.startswith('/usr/lib/python3.10/')})
        raw = core.command('04_ldd_before', ['/usr/bin/ldd'] + targets, timeout=60, cwd=core.ROOT)
        core.need(b'not found' not in raw, 'no_unresolved_linkage')
        linked = sorted({os.fsdecode(p) for p in core.re.findall(rb'(/[^\s()]+)', raw)
                         if Path(os.fsdecode(p)).is_file()})
        names.update(linked)
        names.update(str(Path(p).resolve(strict=True)) for p in list(names))
        before = {p: core.rich(p) for p in sorted(names)}
        core.write_json(out / 'RUNTIME_INPUTS_BEFORE.json', before)
        raw_after = core.command('05_ldd_after', ['/usr/bin/ldd'] + targets, timeout=60, cwd=core.ROOT)
        linked_after = sorted({os.fsdecode(p) for p in core.re.findall(rb'(/[^\s()]+)', raw_after)
                               if Path(os.fsdecode(p)).is_file()})
        core.need(linked_after == linked, 'identical_resolved_linkage_membership')
        after = {p: core.rich(p) for p in before}
        core.write_json(out / 'RUNTIME_INPUTS_AFTER.json', after)
        core.need(after == before and runtime.configuration() == conf, 'entire_bounded_runtime_unchanged')
        lock = {'format': 'p211-bounded-runtime-lock-v1', 'status': 'INFRA_IMPORT_CLOSURE_ONLY_PENDING_ROOT_SCIENCE_REVIEW',
                'declared_imports': runtime.ROLE_IMPORTS, 'files': before, 'configuration': conf,
                'ldd_targets': targets, 'ldd_paths': linked, 'loader_search_directory_states': search_dirs,
                'probe_layers': [row['layer'] for row in probes],
                'source_import_completeness': 'Infrastructure sources inspected; root must independently review actual science static/conditional imports before approval.',
                'limits': 'Known files plus import-only module/map samples; no full-host recursion, OS/startup trace, native-open trace or hermetic claim.'}
        core.write_json(out / 'RUNTIME_LOCK.json', lock)
    except BaseException as exc:
        errors.append({'type': type(exc).__name__, 'error': repr(exc), 'traceback': traceback.format_exc()})
    finally:
        if source_before is not None:
            try:
                after = {p: core.rich(p) for p in source_before}
                core.write_json(out / 'SOURCE_INPUTS_AFTER.json', after)
                core.need(after == source_before, 'entire_source_inputs_unchanged')
            except BaseException as exc:
                errors.append({'stage': 'source_closure', 'error': repr(exc)})
    result = {'status': 'FAIL_PRESERVED' if errors else 'PASS_PREPARATION_ONLY', 'errors': errors,
              'commands': core.COMMANDS, 'runtime_file_count': len(lock['files']) if lock else None,
              'scientific_executions': 0, 'science_sources_read_or_imported': []}
    core.write_json(out / 'RESULT.json', result)
    if not core.UNFINALIZED_NATIVE:
        seal = core.seal()
    else:
        seal = None
    print(json.dumps({'status': result['status'], 'errors': errors, 'output': str(out), 'seal': seal}, sort_keys=True))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
