#!/usr/bin/env python3
"""Root read-only archive inspection; no subprocess, Git write or science."""
import hashlib
import json
from pathlib import Path
import sys

RUN = Path('/root/symbolic-dynamics-closed-scout-checkpoint-bllqdh27')
PHASES = ('capture', 'stage', 'commit', 'push')
PLAN_SHA = 'b6118e7ec9956145b2f733da52bbdb26506ff9a893073af3fb1feb01a19112a0'
ROOT = Path('/root/autodl-tmp/symbolic_dynamics')

def digest(b):
    return hashlib.sha256(b).hexdigest()

def read(p):
    return json.loads(p.read_bytes())

def key(p):
    b = p.read_bytes()
    return {'sha256': digest(b), 'bytes': len(b),
            'oid': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest(),
            'mode': '100755' if p.stat().st_mode & 0o111 else '100644'}

plan = read(RUN / 'PLAN.json')
assert digest((RUN / 'PLAN.json').read_bytes()) == PLAN_SHA
assert digest((RUN / 'executed_source.py').read_bytes()) == plan['source_sha256']
inventory = plan['inventory']
assert {p.relative_to(RUN / 'frozen').as_posix() for p in (RUN / 'frozen').rglob('*')
        if p.is_file()} == set(inventory)
for n, v in inventory.items():
    assert key(RUN / 'frozen' / n) == v, n
for n, v in plan['protected_roles'].items():
    p = Path(n)
    assert p.exists() == v['present'], n
    if v['present']:
        assert key(p) == {k: x for k, x in v.items() if k != 'present'}, n
for row in plan['artifacts']['inherited_inputs']:
    p = Path(row['mapped'])
    if not p.is_absolute():
        p = (RUN / 'frozen' if row['mapped'] in inventory else ROOT) / p
    assert digest(p.read_bytes()) == row['sha256'], row

expected = {n: (v['mode'], v['oid']) for n, v in inventory.items()}
base = {n: (v['mode'], v['oid']) for n, v in plan['baseline_selected'].items()}
changed = {n: v for n, v in expected.items() if base.get(n) != v}
assert len(changed) == 117 and len(base) == 1
summary = []
previous_seal = None
for phase in PHASES[:PHASES.index(sys.argv[1]) + 1]:
    d = RUN / phase
    manifest = {}
    for row in (d / 'MANIFEST.sha256').read_text().splitlines():
        h, n = row.split('  ', 1)
        assert n not in manifest and not n.startswith('/') and '..' not in Path(n).parts
        manifest[n] = h
        assert digest((d / n).read_bytes()) == h, n
    assert set(manifest) == {p.relative_to(d).as_posix() for p in d.rglob('*')
                            if p.is_file()} - {'MANIFEST.sha256'}
    result = read(d / 'RESULT.json')
    assert result['status'] == 'PASS_PRIVATE_CHECKPOINT_' + phase.upper()
    assert result['approved_plan_sha256'] == PLAN_SHA
    assert result['source_sha256'] == plan['source_sha256']
    assert result['previous_phase_sha256'] == previous_seal
    commands = sorted(d.glob('command_*'))
    assert [p.name for p in commands] == [f'command_{i:03}' for i in range(1, result['commands'] + 1)]
    kinds = {}
    for c in commands:
        a, r, spawn = (read(c / n) for n in ('ATTEMPT.json', 'RESULT.json', 'SPAWN.json'))
        assert r['returncode'] == 0 and not r['timed_out'] and spawn['spawned'] and spawn['pid'] > 0
        assert a['timeout_seconds'] == 50 and a['cwd'] == str(ROOT)
        assert a['environment']['GIT_OPTIONAL_LOCKS'] == '0'
        streams = {n: (c / (n + '.raw')).read_bytes() for n in ('stdin', 'stdout', 'stderr')}
        argv, out = a['argv'], streams['stdout']
        if 'ls-tree' in argv:
            assert out.endswith(b'\0')
            rows = {}
            for row in out.split(b'\0')[:-1]:
                head, name = row.split(b'\t', 1)
                mode, typ, oid = head.decode().split()
                assert typ == 'blob' and name.decode() not in rows
                rows[name.decode()] = (mode, oid)
            assert rows == (base if phase == 'capture' else expected)
        if 'ls-files' in argv:
            rows = {}
            assert out.endswith(b'\0')
            for row in out.split(b'\0')[:-1]:
                head, name = row.split(b'\t', 1)
                mode, oid, stage = head.decode().split()
                assert stage == '0' and name.decode() not in rows
                rows[name.decode()] = (mode, oid)
            assert rows == expected
        if 'diff-tree' in argv:
            assert argv[-2:] == [plan['base_tree'], result['tree']]
            rows = out.split(b'\0')
            assert rows.pop() == b'' and len(rows) == 2 * len(changed)
            seen = set()
            for i in range(0, len(rows), 2):
                n = rows[i + 1].decode()
                assert n in changed and n not in seen
                seen.add(n)
                oldmode, oldoid = base.get(n, ('000000', '0' * 40))
                mode, oid = changed[n]
                assert rows[i].decode() == f':{oldmode} {mode} {oldoid} {oid} ' + ('M' if n in base else 'A')
            assert seen == set(changed)
        if '--batch-check' in argv:
            objects = {v['oid']: v['bytes'] for v in inventory.values()}
            assert streams['stdin'] == ''.join(n + '\n' for n in sorted(objects)).encode()
            assert out == ''.join(f'{n} blob {objects[n]}\n' for n in sorted(objects)).encode()
        if 'ls-remote' in argv:
            assert argv[-2:] == [plan['remote_url'], 'refs/heads/main']
            assert out in ((plan['base'] + '\trefs/heads/main\n').encode(),
                           (result.get('commit', plan['base']) + '\trefs/heads/main\n').encode())
        kinds[c.name] = {'argv': argv, 'returncode': r['returncode'],
                         'raw': {n: {'bytes': len(v), 'sha256': digest(v)} for n, v in streams.items()}}
    previous_seal = digest((d / 'MANIFEST.sha256').read_bytes())
    summary.append({'phase': phase, 'manifest_rows': len(manifest), 'sha256': previous_seal,
                    'result': result, 'commands_checked': len(kinds),
                    'native_files_byte_read': 6 * len(kinds)})
print(json.dumps({'status': 'PASS_ROOT_ARCHIVE_INSPECTION', 'selected_files': len(inventory),
                  'selected_bytes': sum(v['bytes'] for v in inventory.values()),
                  'inherited_rows': len(plan['artifacts']['inherited_inputs']),
                  'protected_roles': len(plan['protected_roles']), 'phases': summary,
                  'new_git_queries': 0, 'new_science': 0}, sort_keys=True))
