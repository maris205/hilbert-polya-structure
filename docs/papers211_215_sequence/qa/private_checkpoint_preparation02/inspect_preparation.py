#!/usr/bin/env python3
"""Author preparation integrity and exact-delta checks, with no Git or science."""
import collections
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
m = runpy.run_path(str(HERE / 'checkpoint.py'), run_name='author_preparation_integrity_helpers')
plan_path = HERE / 'preview02/PLAN.json'
plan = m['approved_plan'](plan_path, m['key'](plan_path)['sha256'])
assert plan['inventory'] == m['inventory']()
assert plan['artifacts'] == m['artifacts']()
assert plan['protected_roles'] == m['protected_roles']()
assert len(plan['inventory']) == 714 and plan['selected_bytes'] == 11068259
assert collections.Counter(r['status'] for r in plan['delta_preview']) == {'A': 711, 'M': 2, '=': 1}
assert len(plan['baseline_selected']) == 3
qa = {n: v for n, v in plan['inventory'].items()
      if any(n == p or n.startswith(p + '/') for p in m['PRIOR_QA_ROOTS'])}
assert len(qa) == 263 and sum(v['bytes'] for v in qa.values()) == 446322
discovery = m['read'](HERE / 'readonly_discovery01/INVENTORY_PREVIEW.json')
assert {n: v for n, v in plan['inventory'].items() if n not in qa} == {
    n: {k: v[k] for k in ('bytes', 'mode', 'oid', 'sha256')}
    for n, v in discovery['core_inventory'].items()}
assert qa == {n: {k: v[k] for k in ('bytes', 'mode', 'oid', 'sha256')}
              for n, v in discovery['optional_prior_qa_inventory'].items()}
assert len(plan['artifacts']['local_only_execution_boundary']) == 9
assert not any(m['selected'](n) for n in m['EXCLUDED'])
for logical, physical in m['CONTROL_SOURCES'].items():
    assert plan['source_mapping'][logical] == physical
    assert m['key'](m['ROOT'] / physical) == plan['inventory'][logical]
assert 'total **34**, zero reserves.' in m['source_path']('docs/papers211_215_sequence/PIPELINE_STATE.md').read_text()
assert len(plan['artifacts']['packages']) == 12
assert plan['delta_preview'] == m['delta_preview'](plan['inventory'], plan['baseline_selected'])
assert len(plan['dependency_git_mapping']['bindings']) == len(plan['artifacts']['inherited_inputs'])
for row in plan['dependency_git_mapping']['bindings']:
    if row['original_key'].startswith('/'):
        assert not row['git_paths'] and row['status'].startswith('local-only host')
    else:
        assert row['git_paths'], ('Unclosed workspace historical Git dependency', row)
commands = []
for directory in sorted((HERE / 'preview02').glob('command_*')):
    attempt, result, spawn = [m['read'](directory / n) for n in ('ATTEMPT.json', 'RESULT.json', 'SPAWN.json')]
    assert result['returncode'] == 0 and not result['timed_out'] and spawn['spawned']
    assert attempt['cwd'] == str(m['ROOT']) and attempt['environment']['GIT_OPTIONAL_LOCKS'] == '0'
    assert 'GIT_INDEX_FILE' not in attempt['environment']
    assert (directory / 'stdin.raw').read_bytes() == b''
    assert (directory / 'stderr.raw').read_bytes() == b''
    commands.append(attempt['argv'])
assert len(commands) == 12
coverage = {name: m['complete_manifest'](HERE / name, 'MANIFEST.sha256')
            for name in ('controls_preview34', 'readonly_discovery01', 'failure_preservation01', 'preview02')}
failed = HERE / 'preview01/FAILED_EXECUTOR.py'
preserved = m['read'](HERE / 'failure_preservation01/RESULT.json')
assert m['key'](failed) == preserved['source_key']
assert 'Truncated dependency metadata stream' in m['read'](HERE / 'preview01/FAILURE.json')['traceback']
dependency_status = collections.Counter(r['status'] for r in plan['dependency_git_mapping']['bindings'])
print(json.dumps({'status': 'PASS_AUTHOR_PREPARATION_INTEGRITY_ONLY',
    'files': len(plan['inventory']), 'bytes': plan['selected_bytes'],
    'delta': {'A': 711, 'M': 2, '=': 1, 'D': 0},
    'protected_roles': len(plan['protected_roles']),
    'sealed_scientific_or_negative_packages': len(plan['artifacts']['packages']),
    'inherited_rows': len(plan['artifacts']['inherited_inputs']),
    'inherited_git_binding_status': dict(dependency_status),
    'prior_qa_files': len(qa), 'local_only_boundary_files': 9,
    'native_readonly_commands': len(commands), 'subpacket_seals': coverage,
    'git_commands_executed_by_this_inspector': 0, 'scientific_runs': 0,
    'independent_review': False,
    'public_wording_already_in_core_discovery': True}, sort_keys=True))
