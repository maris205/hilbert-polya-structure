#!/usr/bin/env python3
"""Future root-approved import-only discovery. SOURCE_ONLY; not executed.

Adapted from accepted P211 prepare_runtime.py, without old baseline/test/fixture
execution. Discovery is not scientific production and its output is not approval.
Actual source reception and an immutable enabled approval must precede invocation.
"""
import json
import os
from pathlib import Path
import sys
import traceback
import types

HERE = Path(__file__).resolve().parent
runtime = types.ModuleType('_p212_preparation_runtime')
runtime.__file__ = str(HERE / 'p212_runtime.py')
sys.modules[runtime.__name__] = runtime
exec(compile(Path(runtime.__file__).read_bytes(), runtime.__file__, 'exec'), runtime.__dict__)
core = runtime.core
SOURCES = runtime.PREPARATION_SOURCES
ORIGINAL = core.ROOT / 'docs/papers211_215_sequence/qa/p211_runtime_preparation'
ORIGINAL_NAMES = ('runtime_core.py', 'p211_runtime.py', 'prepare_runtime.py')


def main():
    core.need(len(sys.argv) == 3, 'ABSOLUTE_DISCOVERY_APPROVAL EXPECTED_APPROVAL_SHA256')
    approval_path = Path(sys.argv[1])
    approval = runtime.load_discovery(approval_path, sys.argv[2])
    out = Path(approval['output'])
    core.need(not core.lexists(out), 'exclusive_root_bound_discovery_output')
    runtime.settings(out / 'never_created_preparer_cache', core.ROOT)
    expected_originals = {str(ORIGINAL / name) for name in ORIGINAL_NAMES}
    core.need(set(approval['lineage_inputs']) == expected_originals, 'exact_three_old_infrastructure_inputs')
    for p, pin in approval['lineage_inputs'].items():
        core.pin(p, pin)
    out.mkdir(mode=0o700)
    (out / 'commands').mkdir()
    (out / 'source_snapshots').mkdir()
    (out / 'empty_probe_capsule').mkdir()
    core.OUT, core.COMMANDS, core.UNFINALIZED_NATIVE = out, [], []
    errors, lock, source_before = [], None, None
    deadline = approval['native_timeout_seconds']
    try:
        paths = list(approval['source_inputs']) + list(approval['lineage_inputs'])
        paths += [str(approval_path)] + [row['path'] for row in approval['provenance_inputs']]
        core.need(len(paths) == len(set(paths)), 'unique_discovery_documentary_input_paths')
        source_before = {p: core.rich(p) for p in paths}
        core.write_json(out / 'SOURCE_INPUTS_BEFORE.json', source_before)
        core.write_json(out / 'PREPARER_SETTINGS.json', {'argv': sys.argv, 'orig_argv': sys.orig_argv,
                        'cwd': str(Path.cwd()), 'environment': dict(os.environ), 'cache': sys.pycache_prefix,
                        'flags': repr(sys.flags), 'sample': runtime.sample(),
                        'scope': 'Root-approved import-only preparer, not scientific source execution'})
        for number, p in enumerate(SOURCES):
            target = out / 'source_snapshots' / p.name
            core.write_bytes(target, p.read_bytes())
            core.command('00_snapshot_cmp_' + str(number), ['/usr/bin/cmp', '--', str(p), str(target)],
                         timeout=deadline, cwd=core.ROOT)
        for number, (old_name, source) in enumerate(zip(ORIGINAL_NAMES, SOURCES)):
            core.command('01_source_diff_' + str(number), ['/usr/bin/diff', '-u', '--',
                         str(ORIGINAL / old_name), str(source)], timeout=deadline,
                         cwd=core.ROOT, require_success=False)
            row = core.COMMANDS[-1]
            core.need(row['exit_code'] == 1 and row['streams_complete'] and
                      row['stderr']['bytes'] == 0 and not row['process_group_settlement']['signals'],
                      'expected_complete_disclosed_source_diff')
        probes = []
        for tag in ('outer', 'launcher', 'recorder', 'child'):
            cache = out / ('never_created_probe_' + tag + '_cache')
            cwd = out / 'empty_probe_capsule' if tag == 'child' else core.ROOT
            argv = [str(runtime.PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(cache),
                    str(HERE / 'p212_runtime.py'), 'probe', tag, str(cache), str(cwd),
                    str(approval_path), sys.argv[2]]
            raw = core.command('02_probe_' + tag, argv, timeout=deadline, cwd=cwd)
            row = json.loads(raw)
            core.need(row['status'] == 'IMPORT_ONLY_NO_SCIENTIFIC_SOURCE_READ' and row['layer'] == tag and
                      row['declared_imports'] == runtime.ROLE_IMPORTS, 'actual_exact_import_only_probe_scope')
            core.need(row['sample']['environment'] == core.ENV and row['sample']['cwd'] == str(cwd) and
                      row['sample']['pycache_prefix'] == str(cache) and not core.lexists(cache), 'actual_probe_settings')
            core.need('fractions' in row['sample']['modules'] and 'decimal' in row['sample']['modules'],
                      'actual_fractions_decimal_source_modules_recorded')
            probes.append(row)
        conf = probes[0]['configuration']
        core.need(all(row['configuration'] == conf for row in probes), 'all_layer_configuration_agreement')
        search_dirs = runtime.loader_search_scope(conf)
        preparer = runtime.sample()
        names = set(runtime.NATIVE_FILES) | {'/usr/bin/diff'}
        for sample in [preparer] + [row['sample'] for row in probes]:
            names.update(sample['mapped_files'])
            names.update(row['path'] for row in sample['modules'].values())
        names.update(p for p, row in conf['paths'].items() if row['is_file'])
        targets = sorted(set(runtime.NATIVE_FILES) - {'/usr/bin/ldd'} | {'/usr/bin/diff'} |
                         {p for p in names if p.endswith('.so') and p.startswith('/usr/lib/python3.10/')})
        raw = core.command('03_ldd_before', ['/usr/bin/ldd'] + targets, timeout=deadline, cwd=core.ROOT)
        core.need(b'not found' not in raw, 'no_unresolved_linkage')
        linked = sorted({os.fsdecode(p) for p in core.re.findall(rb'(/[^\s()]+)', raw)
                         if Path(os.fsdecode(p)).is_file()})
        names.update(linked)
        names.update(str(Path(p).resolve(strict=True)) for p in list(names))
        before = {p: core.rich(p) for p in sorted(names)}
        core.write_json(out / 'RUNTIME_INPUTS_BEFORE.json', before)
        raw_after = core.command('04_ldd_after', ['/usr/bin/ldd'] + targets, timeout=deadline, cwd=core.ROOT)
        core.need(b'not found' not in raw_after, 'no_unresolved_post_linkage')
        linked_after = sorted({os.fsdecode(p) for p in core.re.findall(rb'(/[^\s()]+)', raw_after)
                               if Path(os.fsdecode(p)).is_file()})
        core.need(linked_after == linked, 'identical_resolved_linkage_membership')
        after = {p: core.rich(p) for p in before}
        core.write_json(out / 'RUNTIME_INPUTS_AFTER.json', after)
        core.need(after == before and runtime.configuration() == conf, 'entire_bounded_runtime_unchanged')
        core.need(runtime.loader_search_scope(conf) == search_dirs, 'entire_loader_search_states_unchanged')
        core.need(not list((out / 'empty_probe_capsule').iterdir()), 'no_scientific_probe_capsule_contents')
        core.need(all(not core.lexists(out / ('never_created_probe_' + tag + '_cache'))
                      for tag in ('outer', 'launcher', 'recorder', 'child')) and
                  not core.lexists(out / 'never_created_preparer_cache'), 'all_discovery_cache_prefixes_absent')
        expected_labels = ['00_snapshot_cmp_' + str(n) for n in range(3)]
        expected_labels += ['01_source_diff_' + str(n) for n in range(3)]
        expected_labels += ['02_probe_' + tag for tag in ('outer', 'launcher', 'recorder', 'child')]
        expected_labels += ['03_ldd_before', '04_ldd_after']
        core.need([row['label'] for row in core.COMMANDS] == expected_labels, 'exact_twelve_discovery_native_attempts')
        lock = {'format': 'p212-bounded-runtime-lock-v1',
                'status': 'INFRA_IMPORT_CLOSURE_ONLY_PENDING_ROOT_COMPLETE_RECEPTION',
                'declared_imports': runtime.ROLE_IMPORTS, 'files': before, 'configuration': conf,
                'ldd_targets': targets, 'ldd_paths': linked, 'loader_search_directory_states': search_dirs,
                'probe_layers': [row['layer'] for row in probes],
                'source_import_completeness': 'Declared import-only probes; root must receive all static/conditional source, extension, ELF and configuration dependencies before scientific approval.',
                'limits': 'Selected known files, import-only module/map samples and explicit configuration; no scientific source executed for discovery, no host recursion or OS/startup/native-open/escaped-descendant trace.'}
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
              'scientific_executions': 0, 'science_sources_read_or_imported': [],
              'limits': 'Not root acceptance, independent infrastructure certification, scientific production or manuscript PASS.'}
    core.write_json(out / 'RESULT.json', result)
    seal = core.seal() if not core.UNFINALIZED_NATIVE else None
    print(json.dumps({'status': result['status'], 'errors': errors, 'output': str(out), 'seal': seal}, sort_keys=True))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
