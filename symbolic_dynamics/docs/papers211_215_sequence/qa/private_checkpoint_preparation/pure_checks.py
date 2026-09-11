#!/usr/bin/env python3
"""Pure parsing/phase-allowlist checks. No subprocess, Git, or fixture writes."""
import ast
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'checkpoint.py'
ast.parse(SOURCE.read_text())
m = runpy.run_path(str(SOURCE), run_name='pure_check_import')
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

name = m['SCOUT'] + 'root_reception/EXAMPLE.md'
old, new = '1' * 40, '2' * 40
tree = f'100644 blob {new}\t{name}\0'.encode()
check(m['tree_map'](tree) == {name: {'mode': '100644', 'oid': new}})
rejected(m['tree_map'], tree[:-1])
rejected(m['tree_map'], tree + tree)
rejected(m['tree_map'], f'160000 commit {new}\t{name}\0'.encode())
rejected(m['tree_map'], f'100644 blob {new}\tdocs/unselected.md\0'.encode())
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
    if phase != 'stage':
        rejected(command.git, 'read-tree')
check(m['selected'](m['SCOUT'] + 'tree_order_lane/MANIFEST.sha256'))
for excluded in m['EXCLUDED']:
    check(not m['selected'](excluded))
print(json.dumps({'status': 'PASS_PURE_STATIC_AND_PARSER_CHECKS', 'checks': count,
                  'git_commands_executed': 0, 'filesystem_mutations': 0,
                  'boundary': 'No capture/stage/commit/push behavior has been executed.'}))
