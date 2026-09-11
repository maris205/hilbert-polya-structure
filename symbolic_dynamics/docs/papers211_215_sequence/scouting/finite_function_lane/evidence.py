#!/usr/bin/env python3
"""Bounded documentation/source capture only. No scientific map evaluation."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers211_215_sequence/scouting/finite_function_lane'
INPUTS = [
    'docs/papers132_136_sequence/replacement_scout/inversion_rank/SCOUT.md',
    'docs/papers162_166_sequence/scouting/degree_feedback_jump/SCOUT.md',
    'papers/167-minimum-inverse-position-feedback/main.tex',
    'papers/209-ordered-fibre-threading/sections/01_setup.tex',
    'papers/209-ordered-fibre-threading/sections/02_recurrence.tex',
    'papers/148-even-level-plane-tree-contraction/main.tex',
    'docs/papers204_208_sequence/scouting/finite_systems_fortieth/PROOF_PACKAGE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_nineteenth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/algebra_fourth/OTHER_MAP_ADAPTERS.md',
]
SOURCE_URL = 'https://patmorin.me/teaching/5408/notes/BenFar-LA-02.pdf'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def command(out, name, argv, cwd=ROOT):
    prefix = out / name
    if prefix.with_suffix('.command.json').exists():
        raise RuntimeError('refusing to overwrite native command ' + name)
    before = datetime.now(timezone.utc).isoformat()
    write_json(prefix.with_suffix('.command.json'), {
        'argv': argv, 'cwd': str(cwd), 'started_utc': before,
        'scope': 'documentation and source capture; not a scientific pilot',
    })
    result = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, check=False, timeout=55)
    prefix.with_suffix('.stdout').write_bytes(result.stdout)
    prefix.with_suffix('.stderr').write_bytes(result.stderr)
    write_json(prefix.with_suffix('.result.json'), {
        'returncode': result.returncode,
        'ended_utc': datetime.now(timezone.utc).isoformat(),
        'stdout_bytes': len(result.stdout), 'stderr_bytes': len(result.stderr),
        'stdout_sha256': sha(result.stdout), 'stderr_sha256': sha(result.stderr),
    })
    return result


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
        after = original.read_bytes()
        assert data == after == copy.read_bytes()
        rows.append({'path': rel, 'sha256': sha(data), 'bytes': len(data),
                     'raw_equal': True})
    write_json(out / 'original_capture.json', rows)
    (HERE / 'HISTORICAL_INPUTS.sha256').write_text(''.join(
        row['sha256'] + '  ' + row['path'] + '\n' for row in rows))
    rg = shutil.which('rg')
    curl = shutil.which('curl')
    pdftotext = shutil.which('pdftotext')
    if not (rg and curl and pdftotext):
        raise RuntimeError('required documentation tool unavailable')
    commands = []
    commands.append(command(out, '01_decisive_search', [rg, '-n', '-i',
        'S10|S12|root of|depth|ancestor|cyclic|cycle reversal|height-two|height at most two',
        *INPUTS]))
    source = out / 'level_ancestor_2002.pdf'
    commands.append(command(out, '02_primary_fetch', [curl, '--fail', '--location',
        '--silent', '--show-error', '--max-time', '45', '--output', str(source), SOURCE_URL]))
    if commands[-1].returncode == 0:
        assert source.read_bytes().startswith(b'%PDF-')
        commands.append(command(out, '03_primary_extract', [pdftotext, '-layout',
            str(source), str(out / 'level_ancestor_2002.txt')]))
        if commands[-1].returncode == 0:
            commands.append(command(out, '04_primary_definition', [rg, '-n', '-A', '30',
                '3.2 The Jump|Observation 2|2 Definitions',
                str(out / 'level_ancestor_2002.txt')]))
    for row in rows:
        assert sha((ROOT / row['path']).read_bytes()) == row['sha256']
    write_json(out / 'RECEIPT.json', {
        'historical_input_count': len(rows),
        'historical_input_bytes': sum(row['bytes'] for row in rows),
        'raw_copy_checks': len(rows),
        'command_returncodes': [item.returncode for item in commands],
        'scientific_executions': 0, 'pilot_boxes': 0,
        'runtime_scope': 'non-hermetic, no toolchain/library closure claim',
        'source_url': SOURCE_URL, 'source_present': source.is_file(),
        'external_uploads_or_contacts': False,
    })
    print(json.dumps({'historical_inputs': len(rows), 'native_commands': len(commands),
                      'returncodes': [item.returncode for item in commands],
                      'scientific_executions': 0}, sort_keys=True))


def seal():
    payloads = sorted(p for p in HERE.rglob('*') if p.is_file()
                      and p != HERE / 'SHA256SUMS')
    lines = []
    for path in payloads:
        data = path.read_bytes()
        lines.append(sha(data) + '  ' + str(path.relative_to(HERE)) + '\n')
    (HERE / 'SHA256SUMS').write_text(''.join(lines))
    print(json.dumps({'payloads': len(payloads),
                      'payload_bytes': sum(p.stat().st_size for p in payloads)}, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['capture', 'seal'])
    args = parser.parse_args()
    if Path(__file__).resolve() != HERE / 'evidence.py':
        raise RuntimeError('unexpected script location')
    {'capture': capture, 'seal': seal}[args.mode]()
