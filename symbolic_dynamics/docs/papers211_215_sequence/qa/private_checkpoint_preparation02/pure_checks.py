#!/usr/bin/env python3
"""Pure source/selector/metadata-parser checks; no subprocess or fixture writes."""
import ast
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
source = HERE / 'checkpoint.py'
ast.parse(source.read_text())
m = runpy.run_path(str(source), run_name='pure_static_checkpoint_inspection')
count = 1
def check(value):
    global count
    assert value
    count += 1
def rejected(function, *args):
    global count
    try:
        function(*args)
    except (RuntimeError, ValueError):
        count += 1
        return
    raise AssertionError('Expected rejection')

name = m['SCOUT'] + 'root_reception/ALLOCATION_RATIONAL_GEOMETRY_RECEPTION.md'
old, new = '1' * 40, '2' * 40
tree = f'100644 blob {new}\t{name}\0'.encode()
check(m['tree_map'](tree) == {name: {'mode': '100644', 'oid': new}})
rejected(m['tree_map'], tree[:-1])
rejected(m['tree_map'], tree + tree)
rejected(m['tree_map'], f'160000 commit {new}\t{name}\0'.encode())
rejected(m['tree_map'], f'100644 blob {new}\tdocs/unselected.md\0'.encode())
check(m['dependency_tree'](tree) == {name: {'mode': '100644', 'oid': new}})
rejected(m['dependency_tree'], tree[:-1])
rejected(m['dependency_tree'], tree + tree)
rejected(m['dependency_tree'], f'100644 blob {new}\\t{name}\\0'.encode())
raw = f':100644 100644 {old} {new} M\0{name}\0'.encode()
check(m['diff_map'](raw)[name] == {'oldmode': '100644', 'mode': '100644',
    'oldoid': old, 'oid': new, 'status': 'M'})
rejected(m['diff_map'], raw[:-1])
rejected(m['diff_map'], raw + raw)
rejected(m['diff_map'], f':100644 000000 {old} {new} D\0{name}\0'.encode())
rejected(m['diff_map'], f':100644 100644 {old} {new} M\0docs/unselected.md\0'.encode())
rejected(m['diff_map'], f':100644 100644 {old} {new} R100\0{name}\0another\0'.encode())
for unsafe in ('../a', '/root/a', 'x//y', 'x/./y', 'x/../y', 'x\ny', 'x\ty', ''):
    rejected(m['safe_name'], unsafe)
for phase in ('prepare', 'capture', 'stage', 'commit', 'push'):
    command = m['Commands'](HERE, phase)
    command.run = lambda *a, **kw: b'NOT_EXECUTED'
    for forbidden in ('config', 'reset', 'checkout', 'clean', 'fetch', 'gc'):
        rejected(command.git, forbidden)
    rejected(command.mirror, 'remote', 'add', 'origin', 'anything')
    check(command.git('rev-parse', 'HEAD') == b'NOT_EXECUTED')
    if phase != 'push':
        rejected(command.git, 'push')
        rejected(command.git, 'update-ref')
    if phase != 'stage':
        rejected(command.git, 'read-tree')
    if phase != 'commit':
        rejected(command.git, 'commit-tree')
for excluded in m['EXCLUDED']:
    check(not m['selected'](excluded))
check(not m['selected'](m['SCOUT'] + 'root_reception/FUTURE_QUEUE_RECEIPT.md'))
for name, mapped in m['CONTROL_SOURCES'].items():
    check(m['source_path'](name) == m['ROOT'] / mapped)
    fake = Path('/root/EXAMPLE_FROZEN_NOT_CREATED')
    check(m['source_path'](name, fake) == fake / name)
check(len(m['LOCAL_ONLY_FILES']) == 9)
check(len(m['PRIOR_QA_ROOTS']) == 2)
check(m['BASE'] == 'f6f3560875f75025624367305b8a9328cbce712e')
check(m['BASE_TREE'] == '30df2d2b012b6e1567bdd2afa61c50e00a547d16')
check(m['environment']()['GIT_OPTIONAL_LOCKS'] == '0')
check('GIT_INDEX_FILE' not in m['environment']())
check(m['environment'](Path('/root/EXAMPLE_NOT_CREATED/index'))['GIT_INDEX_FILE'] == '/root/EXAMPLE_NOT_CREATED/index')
print(json.dumps({'status': 'PASS_PURE_STATIC_SELECTOR_AND_PARSER_CHECKS',
    'checks': count, 'git_commands_executed': 0, 'filesystem_mutations': 0,
    'scope': 'No capture/stage/commit/push/cancellation behavior executed.'}))
