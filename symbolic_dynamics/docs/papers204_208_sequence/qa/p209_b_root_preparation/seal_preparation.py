#!/usr/bin/env python3
"""Seal/audit only this preparation; no original or adapter code is executed."""
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = Path(__file__).resolve().parent
REVIEW = ROOT / 'docs/papers204_208_sequence/reviews/p209_b'
FREEZE = ROOT / 'papers/209-ordered-fibre-threading/frozen_round1'
OUTPUT = ROOT / 'docs/papers204_208_sequence/qa/root_replays/p209_b_strict'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def pin(path):
    path = Path(path)
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return {'sha256': h.hexdigest(), 'bytes': path.stat().st_size,
            'resolved': str(path.resolve()), 'symlink': os.readlink(path) if path.is_symlink() else None}


def verify(base):
    target = base / 'SHA256SUMS'
    initial = pin(target)
    seen = set()
    for line in target.read_text().splitlines():
        digest, name = line.split('  ', 1)
        relative = Path(name)
        assert len(digest) == 64 and set(digest) <= set('0123456789abcdef')
        assert not relative.is_absolute() and '..' not in relative.parts
        assert name != 'SHA256SUMS' and name not in seen
        p = base / name
        assert p.resolve() == p and not p.is_symlink() and pin(p)['sha256'] == digest
        seen.add(name)
    assert seen == {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file() and p != target}
    assert all(not p.is_symlink() for p in base.rglob('*'))
    assert pin(target) == initial
    return {'manifest': initial, 'payloads': len(seen)}


def documentary_closure():
    capture = json.loads((BASE / 'PIN_CAPTURE.json').read_bytes())
    originals = {}
    for key, base, count in (('review', REVIEW, 1298), ('round1', FREEZE, 2003)):
        prior = capture[key]
        now = verify(base)
        assert now['payloads'] == count and now['manifest'] == prior['manifest']
        assert prior['files'] == {p: pin(p) for p in prior['files']}
        originals[key] = now
    assert pin(BASE / 'FIXED_INPUTS.json')['sha256'] == '09a5033597e9b218296f624c256fe2d370331e08269bf1fcc2928352104fb7c8'
    fixed = json.loads((BASE / 'FIXED_INPUTS.json').read_bytes())
    assert len(fixed) == 2021 and fixed == {p: pin(p) for p in fixed}
    static = json.loads((BASE / 'STATIC_CHECK.json').read_bytes())
    assert static['status'] == 'PASS_STATIC_PREPARATION_ONLY' and static['copies'] == 5
    assert static['scientific_executions'] == 0 and static['fixed_inputs_unchanged'] == len(fixed)
    commands = []
    for folder in sorted((BASE / 'checks').iterdir()):
        row = json.loads((folder / 'RECEIPT.json').read_bytes())
        before = json.loads((folder / 'INPUTS_BEFORE.json').read_bytes())
        after = json.loads((folder / 'INPUTS_AFTER.json').read_bytes())
        assert before == after == {p: pin(p) for p in before}
        assert row['inputs_unchanged'] and row['env'] == ENV and row['cwd'] == str(ROOT)
        assert row['stdout'] == pin(folder / 'stdout') and row['stderr'] == pin(folder / 'stderr')
        assert row['stderr']['bytes'] == 0
        expected = 0 if folder.name.startswith('copy_') else 1
        assert row['exit'] == expected
        if expected == 0:
            assert row['stdout']['bytes'] == 0
        commands.append({'tag': folder.name, 'exit': row['exit'], 'stdout_bytes': row['stdout']['bytes']})
    assert len(commands) == 7
    actual_diff = b''.join((BASE / 'checks' / n / 'stdout').read_bytes() for n in
                          ('diff_root_record_pair_py', 'diff_root_launch_pair_py'))
    assert actual_diff == (BASE / 'ADAPTATION.diff').read_bytes() and len(actual_diff) == 15552
    assert pin(BASE / 'root_record_pair.py')['sha256'] == '0629216719a87b20482911a55a77fcb9e3ce7e53bf774f139f6c147d6a014865'
    assert pin(BASE / 'root_launch_pair.py')['sha256'] == '554e4c269a956ab8bbbd74664e4456563c43ff4265ad4b7897d3cc283343e991'
    for p in (BASE / 'original_snapshot').iterdir():
        assert p.read_bytes() == (REVIEW / p.name).read_bytes()
    assert not OUTPUT.exists() and not OUTPUT.is_symlink()
    assert not any(p.name == '__pycache__' or p.suffix in {'.pyc', '.pyo'} for p in BASE.rglob('*'))
    return {'status': 'PASS_DOCUMENTARY_PREPARATION_CLOSURE', 'originals': originals,
            'fixed_inputs': len(fixed), 'commands': commands, 'diff_bytes': len(actual_diff),
            'source_copies': 5, 'output_root_absent': True, 'scientific_executions': 0,
            'scope': 'Preparation-only source, seal, byte-comparison and static evidence; not execution, independent review, delta or acceptance.',
            'external': 'HOLD_EXTERNAL'}


assert Path.cwd() == ROOT and dict(os.environ) == ENV
assert BASE == ROOT / 'docs/papers204_208_sequence/qa/p209_b_root_preparation'
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0
assert sys.argv[1:] in (['seal'], ['audit'])
result = documentary_closure()
if sys.argv[1:] == ['seal']:
    assert not (BASE / 'SHA256SUMS').exists()
    with (BASE / 'FINAL_CHECK.json').open('x') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    paths = sorted(p for p in BASE.rglob('*') if p.is_file())
    assert all(not p.is_symlink() for p in paths)
    with (BASE / 'SHA256SUMS').open('x') as stream:
        for p in paths:
            stream.write(pin(p)['sha256'] + '  ' + p.relative_to(BASE).as_posix() + '\n')
seal = verify(BASE)
assert json.loads((BASE / 'FINAL_CHECK.json').read_bytes()) == result
print(json.dumps({'status': 'PASS_PREPARED_NOT_EXECUTED', 'seal': seal, 'fixed_inputs': 2021,
                  'source_copies': 5, 'documentary_commands': 7, 'diff_bytes': 15552,
                  'output_root_absent': True, 'scientific_executions': 0}, sort_keys=True))
