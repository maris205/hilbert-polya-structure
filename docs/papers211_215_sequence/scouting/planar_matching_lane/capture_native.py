#!/usr/bin/env python3
"""Read-only historical evidence collection; no mathematical verifier is run."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
OUT = HERE / 'native01'
INPUTS = [
    'papers/130-crossing-component-fibre-geometry/main.tex',
    'papers/144-leftmost-dyck-reassociation/main.tex',
    'docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md',
    'docs/papers197_201_sequence/scouting/word_poset_lane/BREADTH_AND_KILL_LEDGER.md',
    'papers/130-crossing-component-fibre-geometry/main.pdf',
    'papers/144-leftmost-dyck-reassociation/main.pdf',
]

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    OUT.mkdir(exist_ok=False)
    bins = {x: str(Path(shutil.which(x)).resolve())
            for x in ('sha256sum', 'sed', 'pdftotext', 'cmp')}
    env = {'PATH': os.environ.get('PATH', ''), 'LANG': 'C.UTF-8',
           'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
    receipt = {
        'schema': 'planar-desk-native-v1',
        'scope': 'old excerpt/PDF extraction and input identity only',
        'scientific_executions': 0, 'git_commands': 0,
        'cwd': str(ROOT), 'environment': env,
        'collector_sha256': digest(__file__),
        'python': {'path': sys.executable, 'version': sys.version,
                   'sha256': digest(Path(sys.executable).resolve())},
        'tools': {x: {'path': p, 'sha256': digest(p)} for x, p in bins.items()},
        'commands': [],
    }

    def persist():
        (OUT / 'RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n')

    def run(tag, tool, *args):
        argv = [bins[tool], *map(str, args)]
        start = time.time_ns()
        result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True)
        stop = time.time_ns()
        outpath, errpath = OUT / (tag + '.stdout'), OUT / (tag + '.stderr')
        outpath.write_bytes(result.stdout)
        errpath.write_bytes(result.stderr)
        receipt['commands'].append({
            'tag': tag, 'argv': argv, 'start_unix_ns': start, 'end_unix_ns': stop,
            'exit_code': result.returncode,
            'stdout': {'path': outpath.name, 'size': len(result.stdout),
                       'sha256': digest(outpath)},
            'stderr': {'path': errpath.name, 'size': len(result.stderr),
                       'sha256': digest(errpath)},
        })
        persist()
        if result.returncode:
            raise RuntimeError(f'{tag} failed with native exit {result.returncode}')
        return result.stdout

    persist()
    try:
        pins = run('01_historical_before', 'sha256sum', *INPUTS)
        (HERE / 'HISTORICAL_INPUT_PINS.sha256').write_bytes(pins)
        run('02_p130_excerpt', 'sed', '-n', '1,310p', INPUTS[0])
        run('03_p144_excerpt', 'sed', '-n', '1,270p;285,353p', INPUTS[1])
        run('04_old_m01_excerpt', 'sed', '-n', '44,177p', INPUTS[2])
        run('05_old_motzkin_excerpt', 'sed', '-n', '65,88p', INPUTS[3])
        run('06_p130_pdf_first_three', 'pdftotext', '-f', '1', '-l', '3',
            '-layout', INPUTS[4], '-')
        run('07_p144_pdf_first_three', 'pdftotext', '-f', '1', '-l', '3',
            '-layout', INPUTS[5], '-')
        run('08_historical_after', 'sha256sum', *INPUTS)
        run('09_historical_raw_cmp', 'cmp', '-s',
            OUT / '01_historical_before.stdout', OUT / '08_historical_after.stdout')
        receipt['status'] = 'PASS_AUTHOR_ARTIFACT_COLLECTION_ONLY'
    except Exception as exc:
        receipt['status'] = 'FAILED_PRESERVED'
        receipt['exception'] = repr(exc)
        raise
    finally:
        persist()
    print(json.dumps({'status': receipt['status'], 'native_commands': len(receipt['commands']),
                      'historical_inputs': len(INPUTS), 'science': 0}))

if __name__ == '__main__':
    main()
