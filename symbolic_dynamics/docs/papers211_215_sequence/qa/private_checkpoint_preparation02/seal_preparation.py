#!/usr/bin/env python3
"""Single-use complete author preparation seal, not a Git or scientific phase."""
from pathlib import Path
import json
import runpy
import sys

HERE = Path(__file__).resolve().parent
m = runpy.run_path(str(HERE / 'checkpoint.py'), run_name='preparation_sealer_only')
m['need'](sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode, 'Require -I -S -B')
m['need'](not (HERE / 'MANIFEST.sha256').exists(), 'Never overwrite a preparation seal')
plan_path = HERE / 'preview02/PLAN.json'
plan = m['approved_plan'](plan_path, m['key'](plan_path)['sha256'])
assert m['inventory']() == plan['inventory']
assert m['artifacts']() == plan['artifacts']
assert m['protected_roles']() == plan['protected_roles']
counts = {}
for name in ('controls_preview34', 'readonly_discovery01', 'preview01',
             'failure_preservation01', 'preview02', 'readonly_checks01'):
    directory = HERE / name
    commands = sorted(directory.glob('command_*'))
    assert [p.name for p in commands] == [f'command_{n:03d}' for n in range(1, len(commands) + 1)]
    for command in commands:
        record = m['read'](command / 'RESULT.json')
        assert record['returncode'] == 0 and record['timed_out'] is False
        assert (command / 'ATTEMPT.json').is_file() and (command / 'SPAWN.json').is_file()
        assert all((command / (s + '.raw')).is_file() for s in ('stdin', 'stdout', 'stderr'))
    if name != 'preview01':
        m['complete_manifest'](directory, 'MANIFEST.sha256')
    else:
        assert (directory / 'FAILURE.json').is_file() and (directory / 'FAILED_EXECUTOR.py').is_file()
        assert not (directory / 'PLAN.json').exists()
    counts[name] = len(commands)
assert counts == {'controls_preview34': 6, 'readonly_discovery01': 12, 'preview01': 11,
                  'failure_preservation01': 2, 'preview02': 12, 'readonly_checks01': 2}
sources = m['read'](HERE / 'readonly_checks01/RESULT.json')['sources']
assert sources == {name: m['key'](HERE / name) for name in sources}
seal = m['finish'](HERE, {'status': 'PREPARED_ONLY_COMPLETE_AUTHOR_SEAL',
    'approved_candidate_plan_sha256': m['key'](plan_path)['sha256'],
    'executor_sha256': m['key'](HERE / 'checkpoint.py')['sha256'],
    'selected_files': 714, 'selected_bytes': 11068259,
    'delta': {'A': 711, 'M': 2, '=': 1, 'D': 0},
    'recorded_native_commands_by_subpacket': counts,
    'recorded_native_commands': sum(counts.values()),
    'git_commands': 35, 'git_mutations': 0, 'scientific_runs': 0,
    'capture_stage_commit_push_executed': False,
    'independent_review': False, 'protected_roles': 14,
    'inherited_rows': 182, 'local_only_execution_boundary_files': 9})
files = [p for p in HERE.rglob('*') if p.is_file() and p != HERE / 'MANIFEST.sha256']
print(json.dumps({'manifest_sha256': seal, 'payload_files': len(files),
    'payload_bytes': sum(p.stat().st_size for p in files),
    'selected_files': 714, 'selected_bytes': 11068259,
    'git_mutations': 0, 'capture_stage_commit_push_executed': False}))
