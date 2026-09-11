#!/usr/bin/env python3
"""Documentary controller; runs only the separately frozen named-import probe.

Uses accepted infrastructure code for provenance/configuration/native capture.
It never loads the new production adapter or any scientific source. AST/compile
checks below apply only to the three new infrastructure sources named here.
"""
import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import sys
import traceback
import types

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / 'p211_runtime_preparation'
OLD_LOCK = OLD / 'discovery02/RUNTIME_LOCK.json'
OLD_PINS = {
    OLD / 'runtime_core.py': '2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934',
    OLD / 'p211_runtime.py': 'bff2dcf25ee846b04eac0bbd46eb7b3e58c728c6d7e8e9ce591c9cef1ae4e421',
    OLD_LOCK: '1499a93909e39b49c16408985053936b7eb7efcf664e91fd75fa77de607be2ab',
}
for path, digest in OLD_PINS.items():
    assert sha256(path.read_bytes()).hexdigest() == digest
runtime = types.ModuleType('_finite_pointer_preparation_accepted_runtime')
runtime.__file__ = str(OLD / 'p211_runtime.py')
sys.modules[runtime.__name__] = runtime
exec(compile((OLD / 'p211_runtime.py').read_bytes(), runtime.__file__, 'exec'), runtime.__dict__)
core = runtime.core
SOURCE_NAMES = ('import_probe.py', 'pointer_runtime.py', 'prepare_runtime02.py')
FRACTION_PATHS = (
    '/usr/lib/python3.10/fractions.py', '/usr/lib/python3.10/decimal.py',
    '/usr/lib/python3.10/numbers.py',
    '/usr/lib/python3.10/lib-dynload/_decimal.cpython-310-x86_64-linux-gnu.so',
    '/usr/lib/x86_64-linux-gnu/libmpdec.so.3',
    '/usr/lib/python3.10/encodings/ascii.py',  # discovery01 map-reader dependency; root-authorized prefix
)
DECLARED = ['collections', 'fractions', 'itertools', 'json', 'math', 'sys']


def main():
    core.need(len(sys.argv) == 2, 'ABSOLUTE_NEW_DOCUMENTARY_ATTEMPT')
    out = Path(sys.argv[1])
    core.need(out.is_absolute() and out.parent == HERE and not core.lexists(out), 'exclusive_own_attempt')
    runtime.settings(out / 'never_created_preparer_cache', core.ROOT)
    out.mkdir(mode=0o700)
    (out / 'commands').mkdir()
    (out / 'empty_probe_capsule').mkdir()
    core.OUT, core.COMMANDS, core.UNFINALIZED_NATIVE = out, [], []
    errors, before, config, lock = [], None, None, None
    try:
        source_paths = [HERE / name for name in SOURCE_NAMES] + list(OLD_PINS) + [
            HERE / 'REQUEST02.json', HERE / 'BINDING.pending.json', HERE / 'PLAN.md',
            HERE.parent / 'p211_runtime_root_reception/RECEPTION.md']
        source_pins = {str(p): core.rich(p) for p in source_paths}
        core.write_json(out / 'SOURCE_INPUTS_BEFORE.json', source_pins)
        request = core.read_json(HERE / 'REQUEST02.json')
        for p, pin in request['frozen_sources'].items():
            core.pin(p, pin)
        core.need(sys.orig_argv == request['argv'] and dict(os.environ) == request['environment'] and
                  str(Path.cwd()) == request['cwd'], 'actual_exact_frozen_controller_request')
        core.write_json(out / 'CONTROLLER_SETTINGS.json', {
            'orig_argv': sys.orig_argv, 'argv': sys.argv, 'environment': dict(os.environ),
            'cwd': str(Path.cwd()), 'flags': repr(sys.flags), 'cache': sys.pycache_prefix,
            'scope': 'Documentary controller reuses accepted infrastructure, not the named-import child.'})
        static = {}
        for name in SOURCE_NAMES:
            p = HERE / name
            tree = ast.parse(p.read_bytes(), filename=str(p))
            compile(p.read_bytes(), str(p), 'exec')
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports += [n.name for n in node.names]
                elif isinstance(node, ast.ImportFrom):
                    imports += [node.module + '.' + n.name for n in node.names]
            static[name] = {'imports': imports, 'syntax_compiled_only_not_executed': True,
                            'pin': core.rich(p)}
        core.need(static['import_probe.py']['imports'] == [
            'sys', 'json', 'collections.Counter', 'fractions.Fraction',
            'itertools.product', 'math.factorial'], 'named_probe_imports_only')
        core.write_json(out / 'INFRASTRUCTURE_STATIC_CHECK.json', static)
        old_lock = core.read_json(OLD_LOCK)
        for p, pin in old_lock['files'].items():
            core.pin(p, pin)
            core.need(core.rich(p) == pin, ('old_exact_rich_pin', p))
        config = runtime.configuration()
        core.need(config == old_lock['configuration'], 'accepted_configuration_unchanged')
        dirs = runtime.loader_search_scope(config)
        core.need(dirs == old_lock['loader_search_directory_states'], 'accepted_loader_dirs_unchanged')
        names = set(old_lock['files']) | set(FRACTION_PATHS) | set(source_pins)
        names.update(str(Path(p).resolve(strict=True)) for p in list(names))
        before = {p: core.rich(p) for p in sorted(names)}
        core.write_json(out / 'RUNTIME_INPUTS_BEFORE.json', before)
        core.write_json(out / 'CONFIGURATION_BEFORE.json', config)
        core.write_json(out / 'LOADER_DIRECTORIES_BEFORE.json', dirs)
        targets = sorted(set(old_lock['ldd_targets']) | {FRACTION_PATHS[3]})
        def linkage(label):
            raw = core.command(label, ['/usr/bin/ldd'] + targets, timeout=60, cwd=core.ROOT)
            core.need(b'not found' not in raw, 'no_unresolved_linkage')
            linked = sorted({os.fsdecode(p) for p in core.re.findall(rb'(/[^\s()]+)', raw)
                             if Path(os.fsdecode(p)).is_file()})
            core.need(all(p in before for p in linked), 'all_ELF_linkage_prefrozen')
            for p in linked:
                core.pin(p, before[p])
            return linked
        linked = linkage('01_ldd_before')
        cache = out / 'never_created_probe_cache'
        cwd = out / 'empty_probe_capsule'
        argv = [str(runtime.PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(cache),
                str(HERE / 'import_probe.py'), str(cache), str(cwd)]
        core.write_json(out / 'PROBE_REQUEST.json', {
            'argv': argv, 'cwd': str(cwd), 'environment': core.ENV, 'timeout_seconds': 60,
            'source_pin': source_pins[str(HERE / 'import_probe.py')],
            'source_frozen_and_inputs_pinned_before_invocation': True,
            'scientific_execution_authorized': False})
        raw = core.command('02_named_import_probe', argv, timeout=60, cwd=cwd)
        row = json.loads(raw)
        core.need(row['status'] == 'IMPORT_ONLY_NO_SCIENCE' and row['orig_argv'] == argv and
                  row['cwd'] == str(cwd) and row['environment'] == core.ENV and
                  row['cache_absent'] is True and row['scientific_executions'] == 0,
                  'actual_probe_exact_settings_and_scope')
        observed = {str(Path(m['file']).resolve(strict=True)) for m in row['modules'].values() if m['file']}
        mapped = set()
        for line in row['proc_maps'].splitlines():
            fields = line.split(None, 5)
            if len(fields) == 6 and fields[5].startswith('/'):
                core.need(not fields[5].endswith(' (deleted)'), 'no_deleted_mapping')
                mapped.add(str(Path(fields[5]).resolve(strict=True)))
        observed.update(mapped)
        absent, volatile = [], []
        for event in row['audit_events']:
            if event['event'] != 'open':
                continue
            p = Path(event['path'])
            core.need(p.is_absolute(), 'absolute_probe_open')
            if p == Path('/proc/self/maps'):
                volatile.append(str(p))
            elif p.is_file():
                observed.add(str(p.resolve(strict=True)))
            else:
                core.need(p.is_relative_to(cache) and not core.lexists(p), 'only_absent_cache_probes')
                absent.append(str(p))
        core.need(observed <= set(before), ('unknown_observed_runtime_HOLD_NO_ADOPTION', sorted(observed - set(before))))
        for p in observed:
            core.pin(p, before[p])
        core.write_json(out / 'OBSERVED_CLOSURE.json', {
            'ordinary_files': {p: before[p] for p in sorted(observed)},
            'mapped_files': sorted(mapped), 'absent_cache_opens': absent, 'volatile_reads': volatile,
            'new_vs_old122_keys': sorted(set(before) - set(old_lock['files'])),
            'all_observed_files_prefrozen': True, 'unregistered_observed_files': []})
        core.need(linkage('03_ldd_after') == linked, 'same_linkage_membership_after')
        runtime_files = {p: pin for p, pin in before.items() if p not in source_pins or p in old_lock['files']}
        # The three production adapter sources are separately bound; documentary
        # controller, plan and request do not become scientific runtime inputs.
        lock = {'format': 'p211-bounded-runtime-lock-v1',
                'adapter_variant': 'finite-pointer-initial-v1',
                'status': 'PREPARED_IMPORT_CLOSURE_ROOT_APPROVAL_PENDING',
                'declared_imports': DECLARED, 'files': runtime_files,
                'configuration': config, 'loader_search_directory_states': dirs,
                'ldd_targets': targets, 'ldd_paths': linked,
                'discovery': 'One frozen named-stdlib-only child; old122 accepted infrastructure closure freshly rehashed.',
                'limits': 'Bounded observed modules/opens/maps plus listed config and ELF linkage; not hermetic or OS/startup/native-open tracing.',
                'scientific_executions': 0, 'run_authorized': False}
        core.write_json(out / 'RUNTIME_LOCK.json', lock)
    except BaseException as exc:
        errors.append({'type': type(exc).__name__, 'error': repr(exc), 'traceback': traceback.format_exc()})
    finally:
        if before is not None:
            try:
                after = {p: core.rich(p) for p in before}
                core.write_json(out / 'RUNTIME_INPUTS_AFTER.json', after)
                core.need(after == before, 'all_prefrozen_inputs_unchanged')
                after_config = runtime.configuration()
                core.write_json(out / 'CONFIGURATION_AFTER.json', after_config)
                core.need(after_config == config, 'all_configuration_unchanged')
                after_dirs = runtime.loader_search_scope(after_config)
                core.write_json(out / 'LOADER_DIRECTORIES_AFTER.json', after_dirs)
                core.need(after_dirs == dirs, 'all_loader_directory_states_unchanged')
                core.need(not core.lexists(out / 'never_created_probe_cache') and
                          not core.lexists(out / 'never_created_preparer_cache'), 'no_created_cache')
            except BaseException as exc:
                errors.append({'stage': 'after', 'error': repr(exc), 'traceback': traceback.format_exc()})
    result = {'status': 'FAIL_PRESERVED' if errors else 'PASS_DOCUMENTARY_PREPARATION_ONLY',
              'errors': errors, 'commands': core.COMMANDS, 'scientific_executions': 0,
              'science_sources_read_imported_compiled_or_evaluated': [],
              'runtime_keys': len(lock['files']) if lock else None,
              'production_adapter_executions': 0, 'root_approval_pending': True}
    core.write_json(out / 'RESULT.json', result)
    seal = core.seal() if not core.UNFINALIZED_NATIVE else None
    print(json.dumps({'status': result['status'], 'errors': errors, 'output': str(out), 'seal': seal}, sort_keys=True))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
