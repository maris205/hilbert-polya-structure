#!/usr/bin/env python3
"""Documentary preparation checks only; never import/run B or root code."""
import ast
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = Path(__file__).resolve().parent
REVIEW = ROOT / 'docs/papers204_208_sequence/reviews/p209_b'
FREEZE = ROOT / 'papers/209-ordered-fibre-threading/frozen_round1'
OUTPUT = ROOT / 'docs/papers204_208_sequence/qa/root_replays/p209_b_strict'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
REVIEW_SEAL = 'd88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea'
FREEZE_SEAL = 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
NAMES = ('verify.py', 'bootstrap.py', 'record_review.py', 'launch_review.py', 'PARAMETERS.json',
         'INDEPENDENCE_DESIGN.md', 'INDEPENDENCE_COMMITMENT.sha256', 'intake.py',
         'prepare_infrastructure.py', 'INFRASTRUCTURE_INPUT_PINS.sha256', 'ADAPTATION.diff',
         'INPUT_PINS.sha256', 'CANONICAL.json', 'SHA256SUMS')


def pin(path):
    path = Path(path)
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return {'sha256': digest.hexdigest(), 'bytes': path.stat().st_size,
            'resolved': str(path.resolve()), 'symlink': os.readlink(path) if path.is_symlink() else None}


def write(path, data):
    with path.open('xb') as stream:
        stream.write(data)


def save(path, value):
    write(path, (json.dumps(value, indent=2, sort_keys=True) + '\n').encode())


def check_seal(base, expected, count):
    manifest = base / 'SHA256SUMS'
    before = pin(manifest)
    assert before['sha256'] == expected
    rows = {}
    for line in manifest.read_text().splitlines():
        digest, name = line.split('  ', 1)
        relative = Path(name)
        assert len(digest) == 64 and set(digest) <= set('0123456789abcdef')
        assert not relative.is_absolute() and '..' not in relative.parts
        assert name != 'SHA256SUMS' and name not in rows
        path = base / relative
        assert path.resolve() == path and not path.is_symlink()
        value = pin(path)
        assert value['sha256'] == digest, name
        rows[str(path)] = value
    actual = {str(p) for p in base.rglob('*') if p.is_file() and p != manifest}
    assert set(rows) == actual and len(rows) == count
    assert pin(manifest) == before
    return {'manifest': before, 'payloads': len(rows), 'files': rows}


def command(tag, argv, paths, expected_exit, cwd=ROOT):
    folder = BASE / 'checks' / tag
    folder.mkdir(parents=True)
    before = {str(p): pin(p) for p in sorted(set(map(Path, paths)) | {Path(argv[0])})}
    save(folder / 'INPUTS_BEFORE.json', before)
    row = {'argv': argv, 'cwd': str(cwd), 'env': ENV, 'started_epoch': time.time(),
           'exit': None, 'scope': 'DOCUMENTARY_BYTE_COMPARISON_OR_DIFF_ONLY'}
    save(folder / 'ATTEMPT.json', row)
    with (folder / 'stdout').open('xb') as out, (folder / 'stderr').open('xb') as err:
        result = subprocess.run(argv, cwd=cwd, env=ENV, stdout=out, stderr=err, check=False)
    after = {p: pin(p) for p in before}
    save(folder / 'INPUTS_AFTER.json', after)
    row.update(exit=result.returncode, finished_epoch=time.time(), inputs_unchanged=before == after,
               stdout=pin(folder / 'stdout'), stderr=pin(folder / 'stderr'))
    save(folder / 'RECEIPT.json', row)
    assert result.returncode == expected_exit and before == after, row
    return row, (folder / 'stdout').read_bytes()


def capture_inputs():
    review = check_seal(REVIEW, REVIEW_SEAL, 1298)
    freeze = check_seal(FREEZE, FREEZE_SEAL, 2003)
    paths = set(map(Path, freeze['files'])) | {FREEZE / 'SHA256SUMS'}
    paths |= {REVIEW / n for n in NAMES}
    paths |= {p for p in (REVIEW / 'infrastructure_originals').rglob('*') if p.is_file()}
    fixed = {str(p): pin(p) for p in sorted(paths)}
    assert all(p.is_relative_to(FREEZE) or p.is_relative_to(REVIEW) for p in paths)
    assert all(v['symlink'] is None and p == v['resolved'] for p, v in fixed.items())
    input_manifest = REVIEW / 'INPUT_PINS.sha256'
    rows = {}
    for line in input_manifest.read_text().splitlines():
        digest, name = line.split('  ', 1)
        path = ROOT / name
        assert path in paths and str(path) not in rows
        assert fixed[str(path)]['sha256'] == digest
        rows[str(path)] = digest
    assert set(rows) == set(freeze['files']) | {str(FREEZE / 'SHA256SUMS')}
    parameters = json.loads((REVIEW / 'PARAMETERS.json').read_bytes())
    canonical = json.loads((REVIEW / 'CANONICAL.json').read_bytes())
    assert parameters['n_values'] == list(range(6)) and parameters['total_states'] == 3414
    assert parameters['CLI'] == ['--max-n', '5']
    assert parameters['schema'] == canonical['schema'] == 'p209-b-ports-constructive-carrier-v1'
    assert canonical['checks'] == 54794 and canonical['states'] == 3414 and canonical['max_n'] == 5
    assert [b['n'] for b in canonical['boxes']] == list(range(6))
    assert sum(b['states'] for b in canonical['boxes']) == 3414
    assert all(len(b['rows']) == b['states'] for b in canonical['boxes'])
    assert not OUTPUT.exists() and not OUTPUT.is_symlink()
    save(BASE / 'FIXED_INPUTS.json', fixed)
    save(BASE / 'PIN_CAPTURE.json', {'status': 'PASS_DOCUMENTARY_INPUT_CAPTURE',
         'review': review, 'round1': freeze, 'fixed_inputs': len(fixed), 'B_input_manifest_rows': len(rows),
         'parameters': parameters, 'canonical_read_only_shape': {'schema': canonical['schema'],
             'checks': canonical['checks'], 'states': canonical['states'], 'max_n': canonical['max_n'],
             'boxes': [{k: b[k] for k in ('n', 'states', 'recurrent', 'image_size', 'max_inverse')}
                       for b in canonical['boxes']]},
         'output_root_absent': True, 'scientific_executions': 0,
         'scope': 'Hash closure and JSON shape only, not proof review or verifier execution.'})
    print(json.dumps({'status': 'PASS_DOCUMENTARY_INPUT_CAPTURE', 'fixed_inputs': len(fixed),
                      'fixed_manifest': pin(BASE / 'FIXED_INPUTS.json'), 'B_payloads': 1298,
                      'round1_payloads': 2003, 'scientific_executions': 0}, sort_keys=True))


def comparisons():
    fixed = json.loads((BASE / 'FIXED_INPUTS.json').read_bytes())
    assert fixed == {p: pin(p) for p in fixed}
    copies = []
    for source in sorted((BASE / 'original_snapshot').iterdir()):
        row, raw = command('copy_' + source.name.replace('.', '_'),
                           ['/usr/bin/cmp', '--', str(REVIEW / source.name), str(source)],
                           [REVIEW / source.name, source], 0)
        assert not raw
        copies.append(row)
    diffs, functions = [], []
    for old, new, allowed in (
        ('record_review.py', 'root_record_pair.py', {'science', 'pair', 'main'}),
        ('launch_review.py', 'root_launch_pair.py', {'check_closed_recorder', 'main'})):
        original, adapted = BASE / 'original_snapshot' / old, BASE / new
        row, raw = command('diff_' + new.replace('.', '_'),
            ['/usr/bin/diff', '-u', '--label', 'original_snapshot/' + old, '--label', new,
             str(original), str(adapted)], [original, adapted], 1)
        diffs.append(raw)
        a, b = original.read_text(), adapted.read_text()
        oa, ob = ast.parse(a), ast.parse(b)
        fa = {n.name: n for n in oa.body if isinstance(n, ast.FunctionDef)}
        fb = {n.name: n for n in ob.body if isinstance(n, ast.FunctionDef)}
        assert fa.keys() == fb.keys()
        changed = {n for n in fa if ast.dump(fa[n]) != ast.dump(fb[n])}
        assert changed == allowed, changed
        for name in fa.keys() - allowed:
            x, y = fa[name], fb[name]
            assert a.splitlines(keepends=True)[x.lineno-1:x.end_lineno] == b.splitlines(keepends=True)[y.lineno-1:y.end_lineno]
        assert [ast.dump(n) for n in oa.body if isinstance(n, (ast.Import, ast.ImportFrom))] == [ast.dump(n) for n in ob.body if isinstance(n, (ast.Import, ast.ImportFrom))]
        assert 'bytesave(canonical' not in b and 'shutil.copyfile(raw' not in b
        functions.append({'original': old, 'adapted': new, 'changed_functions': sorted(changed),
                          'unchanged_function_blocks': len(fa) - len(changed), 'lines': len(b.splitlines())})
    write(BASE / 'ADAPTATION.diff', b''.join(diffs))
    assert fixed == {p: pin(p) for p in fixed}
    assert not OUTPUT.exists() and not OUTPUT.is_symlink()
    save(BASE / 'STATIC_CHECK.json', {'status': 'PASS_STATIC_PREPARATION_ONLY', 'copies': len(copies),
         'function_checks': functions, 'fixed_inputs_unchanged': len(fixed), 'output_root_absent': True,
         'scientific_executions': 0, 'diff_bytes': sum(map(len, diffs)),
         'scope': 'AST parsing, actual source cmp and ordinary unified diff; no wrapper imported or run.'})
    print((BASE / 'STATIC_CHECK.json').read_text(), end='')


assert Path.cwd() == ROOT and dict(os.environ) == ENV
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0
assert BASE == ROOT / 'docs/papers204_208_sequence/qa/p209_b_root_preparation'
if sys.argv[1:] == ['pin_inputs']:
    capture_inputs()
elif sys.argv[1:] == ['comparisons']:
    comparisons()
else:
    raise SystemExit('prepare_checks.py pin_inputs|comparisons; documentary only')
