#!/usr/bin/env python3
"""Record preparation inputs and static documentary evidence; no build imports."""
import ast
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_preparation'
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
SOURCES = ('main.tex', 'math_commands.tex', 'references.bib', 'sections/00_abstract.tex',
           'sections/01_setup.tex', 'sections/02_recurrence.tex', 'sections/03_inverse.tex', 'sections/04_scope.tex')
ORIGINALS = {
    'p208_terminal_v2.py': BATCH / 'qa/run_p208_terminal_builds_v2.py',
    'P208_BUILD_EXECUTION.json': ROOT / 'papers/208-original-snapshot-triangulation-sweeps/qa_final/BUILD_EXECUTION.json',
    'p209_b_record_review.py': BATCH / 'reviews/p209_b/record_review.py',
    'p209_b_launch_review.py': BATCH / 'reviews/p209_b/launch_review.py',
    'p209_record_author.py': PAPER / 'record_author.py',
    'p209_launch_author.py': PAPER / 'launch_author.py',
    'freeze_p209_round2.py': BATCH / 'qa/p209_round2_preparation/freeze_p209_round2.py',
    'ROUND2_ACCEPTANCE_INPUT_CONTRACT.json': BATCH / 'qa/p209_round2_preparation/ACCEPTANCE_INPUT_CONTRACT.json',
    'ARTIFACT_CONTRACT.md': BATCH / 'ARTIFACT_CONTRACT.md',
    'P208_TERMINAL_BUILDER_CODE_AUDIT.md': BATCH / 'qa/P208_TERMINAL_BUILDER_CODE_AUDIT.md',
    'P208_TERMINAL_BUILDER_V2_PREPARATION.md': BATCH / 'qa/P208_TERMINAL_BUILDER_V2_PREPARATION.md',
}


def pin(path):
    path = Path(path)
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return {'sha256': h.hexdigest(), 'bytes': path.stat().st_size,
            'resolved': str(path.resolve()), 'symlink': os.readlink(path) if path.is_symlink() else None}


def write(path, raw):
    with path.open('xb') as stream:
        stream.write(raw)


def save(path, value):
    write(path, (json.dumps(value, indent=2, sort_keys=True) + '\n').encode())


def absent_outputs():
    for path in (PAPER / 'qa_final', BATCH / 'qa/root_replays/p209_terminal_strict'):
        assert not path.exists() and not path.is_symlink(), str(path)


def capture():
    absent_outputs()
    originals = {name: {'original_path': str(p), **pin(p)} for name, p in ORIGINALS.items()}
    sources = {name: {k: pin(PAPER / name)[k] for k in ('sha256', 'bytes')} for name in SOURCES}
    for name, value in sources.items():
        assert value == {k: pin(PAPER / 'frozen_round1' / name)[k] for k in ('sha256', 'bytes')}
    assert pin(ORIGINALS['p208_terminal_v2.py'])['sha256'] == '7399c2db47f08001152277cbddff6a544831a424702ec77ee7af510c8a92ad6c'
    assert pin(ORIGINALS['freeze_p209_round2.py'])['sha256'] == '787357029ae3d4f50c1a9998a3b1e4fe9377786cc06cb024e3a7a96ef95b46c7'
    assert pin(BATCH / 'qa/p209_round2_preparation/SHA256SUMS')['sha256'] == '84fc65f40ca65ed4ec555cd398860e314fe2195bc7f88766d3fbde70a4bb458d'
    save(BASE / 'ORIGINAL_INPUTS.json', originals)
    save(BASE / 'SOURCE_PINS.json', sources)
    save(BASE / 'SOURCE_CAPTURE.json', {'source_names': list(SOURCES), 'live_and_round1_unchanged': True,
         'original_pdf': pin(PAPER / 'frozen_round1/main.pdf'), 'future_round2_hash_supplied': False,
         'preparation_interpreter': pin(sys.executable), 'actual_env': dict(os.environ),
         'actual_argv': sys.orig_argv, 'actual_flags': str(sys.flags), 'output_roots_absent': True,
         'scope': 'Documentary input capture only, no mathematical/build/render/view execution.'})
    print(json.dumps({'status': 'PASS_DOCUMENTARY_SOURCE_CAPTURE', 'originals': len(originals),
                      'source_names': len(sources), 'source_pins': pin(BASE / 'SOURCE_PINS.json'),
                      'output_roots_absent': True, 'builder_executions': 0}, sort_keys=True))


def command(tag, argv, paths, expected):
    folder = BASE / 'checks' / tag
    folder.mkdir(parents=True)
    before = {str(p): pin(p) for p in sorted(set(map(Path, paths)) | {Path(argv[0])})}
    save(folder / 'INPUTS_BEFORE.json', before)
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_epoch': time.time(),
           'exit': None, 'outcome': 'PRE_SPAWN_ATTEMPT'}
    save(folder / 'ATTEMPT.json', row)
    with (folder / 'stdout').open('xb') as out, (folder / 'stderr').open('xb') as err:
        child = subprocess.run(argv, cwd=ROOT, env=ENV, stdout=out, stderr=err, check=False)
    after = {p: pin(p) for p in before}
    save(folder / 'INPUTS_AFTER.json', after)
    row.update(exit=child.returncode, outcome='COMPLETED', ended_epoch=time.time(),
               inputs_unchanged=before == after, stdout=pin(folder / 'stdout'), stderr=pin(folder / 'stderr'))
    save(folder / 'RECEIPT.json', row)
    assert row['exit'] == expected and before == after
    return (folder / 'stdout').read_bytes()


def checks():
    absent_outputs()
    original_pins = json.loads((BASE / 'ORIGINAL_INPUTS.json').read_bytes())
    for name, row in original_pins.items():
        assert {k: row[k] for k in ('sha256', 'bytes', 'resolved', 'symlink')} == pin(row['original_path'])
        raw = command('copy_' + name.replace('.', '_'), ['/usr/bin/cmp', '--', row['original_path'],
                       str(BASE / 'original_snapshot' / name)],
                      [Path(row['original_path']), BASE / 'original_snapshot' / name], 0)
        assert not raw
    for name in SOURCES:
        target = BASE / 'source_snapshot' / name
        raw = command('source_' + name.replace('/', '_').replace('.', '_'),
                       ['/usr/bin/cmp', '--', str(PAPER / name), str(target)], [PAPER / name, target], 0)
        assert not raw
    diffs = []
    for old, new in (('p208_terminal_v2.py', 'root_terminal_builds.py'),
                     ('p209_b_launch_review.py', 'root_launch_terminal.py')):
        a, b = BASE / 'original_snapshot' / old, BASE / new
        diffs.append(command('diff_' + new.replace('.', '_'), ['/usr/bin/diff', '-u',
            '--label', 'original_snapshot/' + old, '--label', new, str(a), str(b)], [a, b], 1))
        ast.parse(b.read_text())
    write(BASE / 'ADAPTATION.diff', b''.join(diffs))
    for path in BASE.rglob('*.py'):
        ast.parse(path.read_text())
    absent_outputs()
    save(BASE / 'STATIC_CHECK.json', {'status': 'PASS_STATIC_PREPARATION_ONLY',
         'exact_original_copies': len(original_pins), 'exact_source_copies': len(SOURCES),
         'actual_documentary_commands': len(original_pins) + len(SOURCES) + 2,
         'complete_diff_bytes': sum(map(len, diffs)), 'builder_executions': 0,
         'source_inputs_unchanged': True, 'output_roots_absent': True,
         'scope': 'Actual cmp/diff plus AST parse only; no recorder or launcher imported/executed.'})
    print((BASE / 'STATIC_CHECK.json').read_text(), end='')


assert Path(__file__).resolve().parent == BASE and Path.cwd() == ROOT and dict(os.environ) == ENV
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0
if sys.argv[1:] == ['capture']:
    capture()
elif sys.argv[1:] == ['checks']:
    checks()
else:
    raise SystemExit('capture_preparation.py capture|checks; documentary only')
