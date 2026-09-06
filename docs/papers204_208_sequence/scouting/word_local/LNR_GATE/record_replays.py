#!/usr/bin/env python3
"""Capture two fresh child executions, complete stdout/stderr and raw cmp exits."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import os
import platform
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
INPUTS = [
    'docs/papers204_208_sequence/scouting/word_local/LNR_TEMPORAL_PROOF.md',
    'docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/PROOF_PACKAGE.md',
    'docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/SOURCE_BOUNDARY.md',
    'docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/Tro22-Matrix-Analysis-LN.pdf',
    'papers/112-tournament-score-upset-reversal/main.tex',
    'papers/186-rank-compression-support/PROOF_PACKAGE.md',
]


def stamp():
    return datetime.now(timezone.utc).isoformat()


def pins():
    return {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in INPUTS}


def main():
    before = pins()
    (HERE / 'INPUT_PINS.sha256').write_text(''.join(f'{digest}  {name}\n' for name, digest in before.items()))
    folder = HERE / 'replays'
    folder.mkdir(exist_ok=True)
    receipt = {'started_utc': stamp(), 'cwd': str(ROOT), 'python': sys.version,
               'platform': platform.platform(), 'before_input_pins': before,
               'producer_sha256': sha256((HERE / 'verify_gate.py').read_bytes()).hexdigest(),
               'canonical_sha256': sha256((HERE / 'CANONICAL.json').read_bytes()).hexdigest(),
               'runs': []}
    env = os.environ.copy()
    env['PYTHONHASHSEED'] = '0'
    for number in (1, 2):
        output = folder / f'run_{number}.stdout.json'
        error = folder / f'run_{number}.stderr'
        command = [sys.executable, str(HERE / 'verify_gate.py')]
        record = {'number': number, 'started_utc': stamp(), 'command': command,
                  'PYTHONHASHSEED': '0'}
        with output.open('wb') as out, error.open('wb') as err:
            child = subprocess.run(command, cwd=ROOT, env=env, stdout=out, stderr=err)
        compare_command = ['cmp', '--', str(output), str(HERE / 'CANONICAL.json')]
        compared = subprocess.run(compare_command, capture_output=True)
        (folder / f'run_{number}.cmp.stdout').write_bytes(compared.stdout)
        (folder / f'run_{number}.cmp.stderr').write_bytes(compared.stderr)
        record.update({'finished_utc': stamp(), 'child_exit': child.returncode,
                       'compare_command': compare_command, 'raw_cmp_exit': compared.returncode,
                       'stdout_bytes': output.stat().st_size, 'stderr_bytes': error.stat().st_size,
                       'stdout_sha256': sha256(output.read_bytes()).hexdigest()})
        receipt['runs'].append(record)
        (folder / 'RECEIPT.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
        if child.returncode or compared.returncode:
            raise SystemExit(1)
    receipt['after_input_pins'] = pins()
    receipt['unchanged_input_pins'] = before == receipt['after_input_pins']
    receipt['finished_utc'] = stamp()
    receipt['status'] = 'FRESH_PAIR_RAW_CANONICAL_PASS' if receipt['unchanged_input_pins'] else 'INPUTS_CHANGED'
    (folder / 'RECEIPT.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not receipt['unchanged_input_pins']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
