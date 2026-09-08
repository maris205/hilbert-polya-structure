#!/usr/bin/env python3
"""Scoped source capture, one pilot launch, and additive final sealing."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers211_215_sequence/scouting/finite_allocation_lane'
INPUTS = [
    'docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md',
    'docs/papers204_208_sequence/scouting/finite_systems_thirty_first/PROOF_AND_DISPOSITION.md',
    'docs/papers204_208_sequence/scouting/graph_relation_second/SCOUT_REPORT.md',
    'docs/papers204_208_sequence/scouting/graph_relation_second/GENERIC_PROOFS.md',
    'docs/papers204_208_sequence/scouting/finite_systems_thirty_eighth/LC_LITERAL.md',
    'papers/169-successor-transfer-set-partitions/main.tex',
    'papers/193-mutual-best-block-refinement/main.tex',
    'docs/papers211_215_sequence/scouting/algebra_lane/PROOF_PACKAGE.md',
]
SOURCES = [
    ('ballistic_ags', 'https://www-n.oca.eu/etc7/AGS.pdf'),
    ('distinct_blocks', 'https://www-users.cse.umn.edu/~odlyzko/doc/unequal.block.partitions.pdf'),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def command(out, name, argv, scope, timeout=55):
    prefix = out / name
    if prefix.with_suffix('.command.json').exists():
        raise RuntimeError('refusing to overwrite command ' + name)
    write_json(prefix.with_suffix('.command.json'), {
        'argv': argv, 'cwd': str(ROOT), 'scope': scope,
        'started_utc': datetime.now(timezone.utc).isoformat(),
    })
    run = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, timeout=timeout, check=False)
    prefix.with_suffix('.stdout').write_bytes(run.stdout)
    prefix.with_suffix('.stderr').write_bytes(run.stderr)
    write_json(prefix.with_suffix('.result.json'), {
        'returncode': run.returncode, 'stdout_bytes': len(run.stdout),
        'stderr_bytes': len(run.stderr), 'stdout_sha256': sha(run.stdout),
        'stderr_sha256': sha(run.stderr),
        'ended_utc': datetime.now(timezone.utc).isoformat(),
    })
    return run.returncode


def capture():
    out = HERE / 'evidence01'
    out.mkdir(exist_ok=False)
    rows = []
    for rel in INPUTS:
        original = ROOT / rel
        data = original.read_bytes()
        copy = out / 'originals' / rel
        copy.parent.mkdir(parents=True, exist_ok=True)
        copy.write_bytes(data)
        assert original.read_bytes() == copy.read_bytes() == data
        rows.append({'path': rel, 'sha256': sha(data), 'bytes': len(data), 'raw_equal': True})
    write_json(out / 'original_capture.json', rows)
    (HERE / 'HISTORICAL_INPUTS.sha256').write_text(''.join(
        r['sha256'] + '  ' + r['path'] + '\n' for r in rows))
    required = ['rg', 'curl', 'pdftotext', 'pdftoppm']
    executable = {name: shutil.which(name) for name in required}
    if not all(executable.values()):
        raise RuntimeError('documentation executable unavailable')
    codes = [command(out, '01_old_mechanism', [executable['rg'], '-n', '-i',
        'BA —|RMA|maximum|mass|successor|master|LC|coalesc|inverse', *INPUTS], 'old-source read')]
    for index, (stem, url) in enumerate(SOURCES, 2):
        pdf = out / (stem + '.pdf')
        code = command(out, f'{index:02d}_{stem}_fetch', [executable['curl'],
            '--fail', '--location', '--silent', '--show-error', '--max-time', '45',
            '--output', str(pdf), url], 'primary-source download only')
        codes.append(code)
        if code == 0:
            assert pdf.read_bytes().startswith(b'%PDF-')
            codes.append(command(out, f'{index:02d}_{stem}_text', [executable['pdftotext'],
                '-layout', str(pdf), str(out / (stem + '.txt'))], 'primary-source extraction'))
    if (out / 'distinct_blocks.pdf').exists():
        codes.append(command(out, '04_distinct_blocks_page2', [executable['pdftoppm'],
            '-f', '2', '-singlefile', '-scale-to', '1500', '-png',
            str(out / 'distinct_blocks.pdf'), str(out / 'distinct_blocks_page2')],
            'primary-source page rendering, not yet a visual read'))
    for row in rows:
        assert sha((ROOT / row['path']).read_bytes()) == row['sha256']
    write_json(out / 'CAPTURE_RECEIPT.json', {
        'historical_input_count': len(rows),
        'historical_input_bytes': sum(row['bytes'] for row in rows),
        'raw_copy_checks': len(rows), 'command_returncodes': codes,
        'scientific_executions': 0, 'source_urls': dict(SOURCES),
        'scope': 'non-hermetic documentation capture, no independent review',
    })
    print(json.dumps({'originals': len(rows), 'returncodes': codes, 'science': 0}))


def pilot():
    out = HERE / 'evidence01'
    input_names = ['INTAKE.md', 'PROOF_NOTES.md', 'pilot.py', 'evidence.py']
    inputs = []
    for name in input_names:
        path = HERE / name
        data = path.read_bytes()
        frozen = out / 'pilot_inputs' / name
        frozen.parent.mkdir(exist_ok=True)
        if frozen.exists():
            raise RuntimeError('refusing to overwrite pilot input')
        frozen.write_bytes(data)
        assert frozen.read_bytes() == data
        inputs.append({'path': name, 'sha256': sha(data), 'bytes': len(data)})
    write_json(out / 'PILOT_INPUTS.json', inputs)
    executable = Path(sys.executable).resolve()
    write_json(out / 'PILOT_RUNTIME.json', {
        'python': str(executable), 'python_sha256': sha(executable.read_bytes()),
        'python_version': sys.version, 'hermetic': False,
        'limitation': 'No complete standard-library, OS or loaded-object closure; no strict-reuse claim.',
        'm': [1, 2, 3, 4, 5], 'N': [0, 1, 2, 3, 4, 5],
    })
    code = command(out, '05_sole_pilot', [sys.executable, '-I', '-B', str(HERE / 'pilot.py')],
                   'sole scientific execution: frozen 30 boxes / 5704 states')
    for row in inputs:
        assert sha((HERE / row['path']).read_bytes()) == row['sha256']
    print(json.dumps({'pilot_returncode': code, 'scientific_executions': 1}))
    if code:
        raise SystemExit(code)


def seal():
    destination = HERE / 'SHA256SUMS'
    if destination.exists():
        raise RuntimeError('sealed package is immutable')
    payloads = sorted(p for p in HERE.rglob('*') if p.is_file())
    destination.write_text(''.join(sha(p.read_bytes()) + '  ' + str(p.relative_to(HERE)) + '\n'
                                   for p in payloads))
    print(json.dumps({'payloads': len(payloads),
                      'payload_bytes': sum(p.stat().st_size for p in payloads)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['capture', 'pilot', 'seal'])
    args = parser.parse_args()
    if Path(__file__).resolve() != HERE / 'evidence.py':
        raise RuntimeError('unexpected evidence producer location')
    {'capture': capture, 'pilot': pilot, 'seal': seal}[args.mode]()
