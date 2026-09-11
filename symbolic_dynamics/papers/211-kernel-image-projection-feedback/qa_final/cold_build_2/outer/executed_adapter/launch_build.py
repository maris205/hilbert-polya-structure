#!/usr/bin/env python3
"""Root-facing outer recorder for one P211 terminal build, pending root binding.

Its child native stdout/stderr are separate raw files. The product's actual
outer tool session/completion still has to be preserved separately by root.
"""
import argparse
import json
import os
from pathlib import Path
import sys
import traceback

HERE = Path(__file__).resolve().parent
# The new reviewed source is loaded directly under -I -S -B; never import
# an old helper or the independent scientific runtime adapter.
scope = {'__name__': 'p211_build_loaded_source', '__file__': str(HERE / 'build_p211.py')}
exec(compile((HERE / 'build_p211.py').read_bytes(), str(HERE / 'build_p211.py'), 'exec'), scope)
globals().update({k: v for k, v in scope.items() if not k.startswith('__')})


def launch(binding_path, binding_sha256, preflight_only=False):
    require(pin(binding_path)['sha256'] == binding_sha256, 'Expected actual root binding digest')
    binding, lock, before_configuration, originals = binding_inputs(binding_path, role='outer')
    runtime_before = runtime_sample()
    check_runtime(runtime_before, file_coverage(before_configuration), originals)
    if preflight_only:
        print(json.dumps({'status': 'OUTER_BOUND_PREFLIGHT_ONLY_NO_NATIVE_CHILD',
                          'binding': pin(binding_path), 'originals': originals,
                          'configuration_count': len(before_configuration),
                          'runtime': runtime_before, 'output_created': False,
                          'tex_compilations': 0, 'acceptance': False}, sort_keys=True))
        return 0
    out = Path(binding['output'])
    out.mkdir(mode=0o700)
    outer = out / 'outer'
    outer.mkdir()
    snapshots = outer / 'executed_adapter'
    snapshots.mkdir()
    for name in CODE_NAMES:
        write_new(snapshots / name, (PREP / name).read_bytes())
        require(pin(snapshots / name) == binding['adapter_pins'][name], 'Physical adapter snapshot')
    write_new(outer / 'ENTERED.json', {'binding': pin(binding_path), 'inner_started': False,
                                     'argv': sys.orig_argv, 'cwd': str(Path.cwd()),
                                     'environment': dict(os.environ),
                                     'outer_native_context': 'ROOT_PRODUCT_SESSION_RECEIPT_REQUIRED'})
    write_new(outer / 'ORIGINALS_BEFORE.json', originals)
    write_new(outer / 'CONFIGURATION_BEFORE.json', before_configuration)
    write_new(outer / 'PARENT_RUNTIME_BEFORE.json', runtime_before)
    write_new(outer / 'SOURCES_BEFORE.json', physical_sources())
    argv = [str(PYTHON), '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(out / 'unused_inner_cache'), str(PREP / 'build_p211.py'),
            '--binding', str(binding_path), '--binding-sha256', binding_sha256]
    failures, command = [], None
    try:
        command, raw = run_native(outer, 'inner_builder', argv, ROOT,
                                  [Path(p) for p in originals], timeout=3600)
        require(command['successful'], 'Inner native builder did not complete successfully')
    except BaseException:
        failures.append(traceback.format_exc())
    pending = incomplete_native(out)
    if list(out.rglob('UNCLOSED.json')) or pending:
        write_new(outer / 'UNCLOSED.json', {'status': 'UNCLOSED_NO_SEAL', 'failures': failures,
                                          'pending_native_attempts': pending})
        return 1
    for name, collect, expected in (
        ('SOURCES_AFTER', physical_sources, binding['source_pins']),
        ('ORIGINALS_AFTER', lambda: {p: pin(p) for p in originals}, originals),
        ('CONFIGURATION_AFTER', lambda: snapshot(configuration_key(binding, lock)[0]), before_configuration)):
        try:
            observed = collect()
            write_new(outer / (name + '.json'), observed)
            require(observed == expected, 'Outer before/after mismatch: ' + name)
        except BaseException:
            failures.append(traceback.format_exc())
    try:
        late = runtime_sample()
        write_new(outer / 'PARENT_RUNTIME_AFTER.json', late)
        check_runtime(late, file_coverage(before_configuration), originals)
    except BaseException:
        failures.append(traceback.format_exc())
    inner_result = None
    if (out / 'inner/RESULT.json').is_file():
        inner_result = json.loads((out / 'inner/RESULT.json').read_bytes())
    if inner_result is None or inner_result['status'] != 'TERMINAL_BUILD_RECORDED_NOT_VIEWED_NOT_ACCEPTED':
        failures.append('Terminal inner build result missing or failed; no acceptance.')
    result = {'status': 'FAIL_PRESERVED' if failures else 'TERMINAL_BUILD_CAPTURED_PENDING_ROOT_INSPECTION',
              'failures': failures, 'native_builder': command,
              'inner_result_pin': pin(out / 'inner/RESULT.json') if inner_result is not None else None,
              'visual_review': 'NOT_VIEWED', 'build_acceptance': False,
              'terminal_acceptance': False, 'scientific_executions': 0,
              'A_B_review_gates': 'SEPARATE_NOT_EXECUTED',
              'outer_native_context': 'ROOT_MUST_RETAIN_ACTUAL_PRODUCT_SESSION_AND_COMPLETION',
              'scope': 'Owned-session settlement and bounded source/config/native/FLS evidence, not OS-hermetic tracing.'}
    write_new(outer / 'RESULT.json', result)
    result['seal'] = seal(out)
    print(json.dumps(result, sort_keys=True))
    return 1 if failures else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--binding', type=Path, required=True)
    parser.add_argument('--binding-sha256', required=True)
    parser.add_argument('--preflight-only', action='store_true')
    args = parser.parse_args()
    raise SystemExit(launch(args.binding, args.binding_sha256, args.preflight_only))
