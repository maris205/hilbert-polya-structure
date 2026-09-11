#!/usr/bin/env python3
"""Read-only documentary integrity check; no imports of any project source.
No runtime discovery, producer, formula or probe is invoked by this file.
"""
from hashlib import sha256
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
reads = {}
checks = 0
def need(test, reason):
    global checks
    checks += 1
    if not test:
        raise AssertionError(reason)

def read(path):
    path = Path(path)
    need(not str(path).endswith(('/pointer_pilot.py', '/PARAMETERS.json')), 'no_scientific_artifact_read')
    need(not path.is_symlink() or not path.is_relative_to(HERE), 'no_owned_artifact_symlink')
    data = path.read_bytes()
    reads[str(path)] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    return data

def obj(path):
    return json.loads(read(path))

def verify(path, pin):
    data = read(path)
    need(sha256(data).hexdigest() == pin['sha256'], ('sha256', str(path)))
    if 'bytes' in pin:
        need(len(data) == pin['bytes'], ('size', str(path)))

def main():
    native_commands = []
    results = {}
    for name, count, status in [('discovery01', 19, 'FAIL_PRESERVED'),
                                ('discovery02', 25, 'PASS_DOCUMENTARY_PREPARATION_ONLY')]:
        base = HERE / name
        manifest = read(base / 'SHA256SUMS').decode().splitlines()
        names = []
        for line in manifest:
            digest, rel = line.split('  ', 1)
            p = Path(rel)
            need(not p.is_absolute() and '..' not in p.parts and rel != 'SHA256SUMS', 'safe_nonself_manifest')
            verify(base / rel, {'sha256': digest})
            names.append(rel)
        need(len(names) == len(set(names)) == count, 'unique_exact_manifest_count')
        actual = {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
        need(actual == set(names) | {'SHA256SUMS'}, 'complete_inventory')
        result = obj(base / 'RESULT.json')
        need(result['status'] == status and result['scientific_executions'] == 0 and
             result['production_adapter_executions'] == 0, 'true_attempt_scope')
        for stem in ('RUNTIME_INPUTS', 'CONFIGURATION', 'LOADER_DIRECTORIES'):
            need(read(base / (stem + '_BEFORE.json')) == read(base / (stem + '_AFTER.json')),
                 ('exact_prepost_bytes', name, stem))
        before = obj(base / 'RUNTIME_INPUTS_BEFORE.json')
        for p, pin in before.items():
            verify(p, pin)
        for p, pin in obj(base / 'SOURCE_INPUTS_BEFORE.json').items():
            need(p in before and before[p] == pin, 'sources_in_full_prepost_set')
        for row in result['commands']:
            folder = base / 'commands' / row['label']
            rec = obj(folder / 'RECEIPT.json')
            need(rec == {key: value for key, value in row.items() if key != 'label'}, 'complete_recorded_command')
            need(rec['exit_code'] == 0 and rec['streams_complete'] is True and
                 rec['process_group_settlement']['quiescent'] is True and
                 rec['process_group_settlement']['signals'] == [], 'native_completed_without_signals')
            for stream in ('stdout', 'stderr'):
                verify(folder / (stream + '.raw'), rec[stream])
            need(rec['stderr']['bytes'] == 0, 'empty_native_stderr')
            attempt = obj(folder / 'ATTEMPT.json')
            need(all(rec[k] == v for k, v in attempt.items() if k not in ('status', 'exit_code')),
                 'attempt_matches_native_completion')
            native_commands.append({'attempt': name, 'label': row['label'], 'exit_code': 0,
                                    'stdout_bytes': rec['stdout']['bytes']})
        probe = obj(base / 'commands/02_named_import_probe/stdout.raw')
        req = obj(base / 'PROBE_REQUEST.json')
        need(probe['orig_argv'] == req['argv'] and probe['environment'] == req['environment'] and
             probe['cwd'] == req['cwd'] and probe['scientific_executions'] == 0, 'exact_probe_binding')
        results[name] = {'status': status, 'payloads': count, 'prepost_keys': len(before),
                         'loaded_module_names': len(probe['modules'])}
    lock = obj(HERE / 'discovery02/RUNTIME_LOCK.json')
    need(len(lock['files']) == 129 and len(lock['loader_search_directory_states']) == 9, 'exact_lock_counts')
    old = obj(HERE.parent / 'p211_runtime_preparation/discovery02/RUNTIME_LOCK.json')
    need(all(lock['files'][p] == pin for p, pin in old['files'].items()), 'unchanged_old122_members')
    additions = sorted(set(lock['files']) - set(old['files']))
    need(len(additions) == 7, 'exact_new_seven_runtime_keys')
    binding = obj(HERE / 'BINDING.pending.json')
    need(binding['approved'] is False and binding['run_authorized'] is False and
         binding['attempt'] is None and binding['execution_root'] is None and
         binding['strict_pair_authorized'] is False and binding['automatic_retry_authorized'] is False and
         binding['canonical_adoption_authorized'] is False, 'still_disabled')
    need(len(native_commands) == 5, 'two_then_three_documentary_commands_only')
    print(json.dumps({'status': 'PASS_DOCUMENTARY_ARTIFACT_CHECK_ONLY', 'checks': checks,
          'read_paths': len(reads), 'attempts': results, 'native_commands': native_commands,
          'runtime_keys': len(lock['files']), 'new_runtime_keys': additions,
          'scientific_executions': 0, 'production_adapter_executions': 0,
          'limits': 'Hash/schema/native-archive reception only; not a new discovery, scientific run or independent runtime acceptance.'},
          sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
