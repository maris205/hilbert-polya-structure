#!/usr/bin/env python3
"""Initial-only pointer adapter over pinned, unchanged accepted P211 guards.

This file has NOT been used to execute science. It is disabled without an
independently root-approved exact binding. No pair or canonical adoption.
"""
from hashlib import sha256
import json
from pathlib import Path
import sys
import types

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / 'p211_runtime_preparation'
PINS = {
    'runtime_core.py': '2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934',
    'p211_runtime.py': 'bff2dcf25ee846b04eac0bbd46eb7b3e58c728c6d7e8e9ce591c9cef1ae4e421',
}
for name, digest in PINS.items():
    assert sha256((OLD / name).read_bytes()).hexdigest() == digest
runtime = types.ModuleType('_finite_pointer_accepted_runtime')
runtime.__file__ = str(OLD / 'p211_runtime.py')
sys.modules[runtime.__name__] = runtime
exec(compile((OLD / 'p211_runtime.py').read_bytes(), runtime.__file__, 'exec'), runtime.__dict__)
core = runtime.core
runtime.ROLE_IMPORTS = ['collections', 'fractions', 'itertools', 'json', 'math', 'sys']
runtime.SOURCE_FILES = (Path(__file__).resolve(), OLD / 'p211_runtime.py', OLD / 'runtime_core.py')


def load_binding(path, digest, attempt):
    core.pin(path, digest)
    binding = core.read_json(path)
    core.need(binding['format'] == 'finite-pointer-initial-binding-v1' and
              binding['approved'] is True and binding['run_authorized'] is True,
              'ROOT_EXACT_INITIAL_AUTHORIZATION_REQUIRED')
    core.need(binding['purpose'] == 'FINITE_POINTER_BOUNDED_INITIAL_PILOT' and
              binding['role'] == 'author' and binding['mode'] == 'initial', 'INITIAL_ONLY_NO_PAIR')
    core.need(binding['attempt'] == str(attempt) and attempt.is_absolute() and
              attempt.parent.resolve(strict=True) == attempt.parent and
              str(attempt.parent) == binding['execution_root'] and
              attempt.parent.is_relative_to(core.ROOT / 'docs/papers211_215_sequence/qa'),
              'root_bound_exact_physical_execution_root_and_attempt')
    core.need(binding['reviewed_static_source_import_closure'] is True and
              binding['reviewed_schema_and_parameters'] is True and
              binding['reviewed_full_runtime_source_lock_and_probe_records'] is True,
              'root_full_source_schema_runtime_gate')
    core.need(binding['declared_imports'] == runtime.ROLE_IMPORTS and
              binding['local_helper_imports'] == [], 'exact_standalone_import_interface')
    core.need(set(binding['adapter_sources']) == {str(p) for p in runtime.SOURCE_FILES},
              'exact_three_adapter_sources')
    for p, pin in binding['adapter_sources'].items():
        core.pin(p, pin)
    core.need(all(type(binding['timeouts'][key]) is int and 0 < binding['timeouts'][key] <= 3600
                  for key in ('science', 'native', 'envelope')), 'finite_positive_integer_deadlines')
    core.need(binding['success_stderr'] == 'empty', 'empty_scientific_stderr')
    core.need(binding['entry'] == 'pointer_pilot.py' and binding['parameters'] == 'PARAMETERS.json',
              'exact_pointer_capsule_names')
    names = [row['name'] for row in binding['capsule_files']]
    core.need(len(names) == 2 and set(names) == {binding['entry'], binding['parameters']},
              'exact_two_source_only_files')
    core.need(binding['argv_template'] == ['$ENTRY', '$PARAMETERS'] and
              binding['parameter_locator'] == 'explicit_absolute_argv', 'reviewed_two_positional_argv')
    core.need(binding['scientific_scope'] == {'n_values': [1, 2, 3, 4], 'total_states': 4356},
              'immutable_four_boxes')
    canonical = binding['canonical']
    core.need(canonical['sha256'] is None and canonical['bytes'] is None and
              Path(canonical['path']).is_absolute() and not core.lexists(canonical['path']),
              'unpublished_target_only_no_canonical_adoption')
    core.need(binding['canonical_adoption_authorized'] is False and
              binding['automatic_retry_authorized'] is False and
              binding['strict_pair_authorized'] is False, 'one_initial_only')
    return binding


def worker_argv(stage, binding_path, digest, attempt):
    core.need(stage in ('outer', 'launcher', 'recorder', 'child01'), 'only_initial_stages')
    return [str(runtime.PYTHON), '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(attempt / ('never_created_' + stage + '_cache')),
            str(Path(__file__).resolve()), stage, str(binding_path), digest, str(attempt)]


runtime.load_binding = load_binding
runtime.worker_argv = worker_argv


def main():
    core.need(len(sys.argv) == 5 and sys.argv[1] in ('outer', 'launcher', 'recorder', 'child01'),
              'INITIAL_STAGE_BINDING_DIGEST_ATTEMPT_NO_PROBE_OR_PAIR')
    return runtime.run_stage(sys.argv[1], Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4]))


if __name__ == '__main__':
    raise SystemExit(main())
