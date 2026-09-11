"""Root complete preparation inspection, using no imported author code or subprocess."""
from pathlib import Path, PurePosixPath
import collections
import hashlib
import json
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_preparation02'
PLAN_SHA = '7d3408300c1dc7f9d0d69ac6ef0e359fe8b8d65493877cbf01cd0350f5bdd8f6'
SOURCE_SHA = '4b34a7735121f0fc51a996daca0c26b7d5e282098708aec8b9bb6e6a98b13ff3'
PREP_SHA = '6b93a2305b2cc675a737f0c694e0d04c4469f1c029e6f74742d43b551fd08430'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def key(path):
    assert path.is_file() and not path.is_symlink() and path.resolve() == path
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': sha(raw),
            'mode': '100755' if path.stat().st_mode & 0o111 else '100644',
            'oid': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}


def safe(name):
    rel = PurePosixPath(name)
    assert not rel.is_absolute() and '..' not in rel.parts and str(rel) == name
    assert re.fullmatch(r'[A-Za-z0-9_./-]+', name)
    return name


def full_seal(directory, seal='MANIFEST.sha256'):
    rows = {}
    for line in (directory / seal).read_text().splitlines():
        digest, name = line.split('  ', 1)
        safe(name)
        assert name not in rows and key(directory / name)['sha256'] == digest
        rows[name] = digest
    assert not any(p.is_symlink() for p in directory.rglob('*'))
    assert {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()} == {seal, *rows}
    return {'rows': len(rows), 'sha256': sha((directory / seal).read_bytes()),
            'bytes': sum((directory / name).stat().st_size for name in rows)}


outer = full_seal(PREP)
assert outer == {'rows': 299, 'sha256': PREP_SHA, 'bytes': 1845459}
assert key(PREP / 'preview02/PLAN.json')['sha256'] == PLAN_SHA
assert key(PREP / 'checkpoint.py')['sha256'] == SOURCE_SHA
plan = read(PREP / 'preview02/PLAN.json')
assert plan['source_sha256'] == SOURCE_SHA
assert plan['closed_literal_boundary'] == 34 and plan['new_scientific_runs'] == 0
assert plan['private_only'] and plan['later_receipts_excluded']
assert plan['base'] == 'f6f3560875f75025624367305b8a9328cbce712e'
assert plan['base_tree'] == '30df2d2b012b6e1567bdd2afa61c50e00a547d16'
assert plan['mirror_base'] == 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
assert plan['remote_url'] == 'git@github.com:maris205/hilbert-polya-structure.git'
assert plan['current_live_control_equality_required'] is False
inventory = plan['inventory']
assert len(inventory) == len(plan['source_mapping']) == 714
assert sum(v['bytes'] for v in inventory.values()) == plan['selected_bytes'] == 11068259
roles = read(PREP / 'controls_preview34/SOURCE_ROLES.json')
assert len(roles['source_mapping']) == 2 and roles['closed_literal_boundary'] == 34
for name, value in inventory.items():
    safe(name)
    source = plan['source_mapping'][name]
    assert source == roles['source_mapping'].get(name, name)
    assert key(ROOT / safe(source)) == value
    assert not any(name == x or name.startswith(x + '/') for x in plan['excluded'])
members = set()
for name in plan['roots']:
    source = ROOT / roles['source_mapping'].get(name, name)
    paths = [source] if source.is_file() else [p for p in source.rglob('*') if p.is_file()]
    for p in paths:
        logical = name if source.is_file() else p.relative_to(ROOT).as_posix()
        assert logical not in members
        members.add(logical)
assert members == set(inventory)
for name, value in roles['inventory'].items():
    assert inventory[name] == value
baseline = plan['baseline_selected']
assert set(baseline) == {*roles['source_mapping'], 'docs/papers211_215_sequence/PROBLEM_ANCHOR.md'}
delta = []
for name, value in sorted(inventory.items()):
    old = baseline.get(name)
    delta.append({'git_path': name, 'source_path': roles['source_mapping'].get(name, name),
                  'old': old, 'new': value,
                  'status': '=' if old == {k: value[k] for k in ('mode', 'oid')} else 'M' if old else 'A'})
assert delta == plan['delta_preview']
assert collections.Counter(r['status'] for r in delta) == {'A': 711, 'M': 2, '=': 1}
qa = {n: v for n, v in inventory.items() if n.startswith('docs/papers211_215_sequence/qa/')}
assert len(qa) == 263 and sum(v['bytes'] for v in qa.values()) == 446322
discovery = read(PREP / 'readonly_discovery01/INVENTORY_PREVIEW.json')
for field, values in [('core_inventory', {n: v for n, v in inventory.items() if n not in qa}),
                      ('optional_prior_qa_inventory', qa)]:
    assert values == {n: {k: v[k] for k in ('bytes', 'sha256', 'mode', 'oid')}
                      for n, v in discovery[field].items()}
for name, value in plan['protected_roles'].items():
    p = Path(name)
    assert p.exists() == value['present']
    if value['present']:
        assert key(p) == {k: value[k] for k in ('bytes', 'sha256', 'mode', 'oid')}
assert len(plan['protected_roles']) == 14
inputs = plan['artifacts']['inherited_inputs']
assert len(inputs) == 182
for row in inputs:
    name = row['mapped']
    p = Path(name) if name.startswith('/') else ROOT / plan['source_mapping'].get(name, name)
    value = key(p)
    assert all(row[k] == value[k] for k in ('bytes', 'sha256', 'oid'))
raw_pairs = plan['artifacts']['historical_raw_pairs']
for row in raw_pairs:
    p = ROOT / plan['source_mapping'].get(row['source'], row['source'])
    assert p.read_bytes() == (ROOT / row['snapshot']).read_bytes()
for name, value in plan['artifacts']['local_only_execution_boundary'].items():
    assert key(Path(name)) == value
assert len(plan['artifacts']['local_only_execution_boundary']) == 9
assert not plan['artifacts']['outside_archive_recursively_copied']
subseals = {name: full_seal(PREP / name) for name in (
    'controls_preview34', 'readonly_discovery01', 'failure_preservation01', 'preview02', 'readonly_checks01')}
commands, tree_outputs = [], []
for path in sorted(PREP.glob('*/command_*/ATTEMPT.json')):
    d = path.parent
    a, r, spawn = [read(d / n) for n in ('ATTEMPT.json', 'RESULT.json', 'SPAWN.json')]
    assert r['returncode'] == 0 and not r['timed_out'] and spawn['spawned'] and spawn['pid'] > 0
    assert a['cwd'] == str(ROOT) and a['timeout_seconds'] == 50
    assert a['environment']['GIT_OPTIONAL_LOCKS'] == '0' and 'GIT_INDEX_FILE' not in a['environment']
    assert (d / 'stdin.raw').read_bytes() == b'' and (d / 'stderr.raw').read_bytes() == b''
    argv = a['argv']
    if 'ls-tree' in argv and d.parent.name == 'preview02':
        raw = (d / 'stdout.raw').read_bytes()
        assert not raw or raw.endswith(b'\0')
        rows = {}
        for row in raw.split(b'\0')[:-1]:
            head, name = row.split(b'\t', 1)
            mode, typ, oid = head.decode().split()
            name = name.decode()
            assert typ == 'blob' and name not in rows
            rows[name] = {'mode': mode, 'oid': oid}
        tree_outputs.append(rows)
    commands.append({'directory': d.relative_to(PREP).as_posix(), 'argv': argv,
                     'stdout_bytes': (d / 'stdout.raw').stat().st_size})
assert len(commands) == 45 and len(tree_outputs) == 2 and tree_outputs[-1] == baseline
dependency = tree_outputs[0]
bindings = plan['dependency_git_mapping']['bindings']
assert len(bindings) == 182
for row, binding in zip(inputs, bindings):
    assert binding['original_key'] == row['key'] and binding['sha256'] == row['sha256']
    assert binding['pin_list'] == row['list']
    for name in binding['git_paths']:
        source = inventory.get(name, dependency.get(name))
        assert source and source['oid'] == row['oid']
    assert bool(binding['git_paths']) == (not row['key'].startswith('/'))
assert (PREP / 'controls_preview34/command_001/stdout.raw').read_bytes() == (
    PREP / 'controls_preview34/command_006/stdout.raw').read_bytes()
assert (PREP / 'controls_preview34/command_001/stdout.raw').read_bytes() == ''.join(
    roles['inventory'][n]['sha256'] + '  ' + str(ROOT / n) + '\n'
    for n in ('SYMBOLIC_DYNAMICS_STATE.md', 'docs/papers211_215_sequence/PIPELINE_STATE.md')).encode()
assert 'Truncated dependency metadata stream' in read(PREP / 'preview01/FAILURE.json')['traceback']
print(json.dumps({'status': 'PASS_ROOT_READONLY_PREPARATION', 'plan_sha256': PLAN_SHA,
                  'source_sha256': SOURCE_SHA, 'outer_seal': outer, 'selected_files': 714,
                  'selected_bytes': 11068259, 'delta': {'A': 711, 'M': 2, '=': 1, 'D': 0},
                  'inherited_rows': 182, 'actual_historical_raw_pairs': len(raw_pairs),
                  'native_commands': commands, 'subseals': subseals,
                  'protected_roles': 14, 'closed_literal_boundary': 34,
                  'new_git_commands': 0, 'new_science': 0,
                  'limits': 'Complete preparation inspection; no execution phase, cancellation test or hermetic-loader certification.'},
                 sort_keys=True, indent=2))
