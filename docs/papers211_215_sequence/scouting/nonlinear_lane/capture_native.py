#!/usr/bin/env python3
"""Artifact-only capture; deliberately contains no scientific experiment."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUTS = [
    'docs/papers172_176_sequence/scouting/fresh_nonlinear_algebra/SCOUT_AND_KILL_LEDGER.md',
    'docs/papers197_201_sequence/scouting/algebra_lane/BREADTH_AND_KILL_LEDGER.md',
    'docs/papers197_201_sequence/scouting/nonlinear_fifth_20260905/SCOUT_AND_DISPOSITION.md',
    'docs/papers204_208_sequence/scouting/algebra/SCOUT_REPORT.md',
    'docs/papers204_208_sequence/scouting/algebra_second/SCOUT_REPORT.md',
    'docs/papers204_208_sequence/scouting/algebra_third/SCOUT_REPORT.md',
    'docs/papers204_208_sequence/scouting/algebra_third/PROOF_AND_ADAPTER_NOTES.md',
    'docs/papers204_208_sequence/scouting/algebra_fourth/SCOUT_REPORT.md',
    'docs/papers152_156_sequence/scouting/algebraic_replacement2/SCOUT.md',
    'docs/papers152_156_sequence/scouting/algebraic_replacement2/OWNER_SEARCH_LOG.md',
]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    native = HERE / 'native'
    native.mkdir(exist_ok=False)
    records = []
    outputs = []
    for number in (1, 2):
        argv = ['/usr/bin/sha256sum', *INPUTS]
        clock = time.monotonic()
        result = subprocess.run(argv, cwd=ROOT, capture_output=True, check=False,
                                timeout=30)
        prefix = f'input{number:02d}'
        (native / f'{prefix}.stdout.raw').write_bytes(result.stdout)
        (native / f'{prefix}.stderr.raw').write_bytes(result.stderr)
        outputs.append(result.stdout)
        records.append({'argv': argv, 'cwd': str(ROOT),
                        'returncode': result.returncode,
                        'elapsed_seconds': time.monotonic() - clock,
                        'stdout': f'{prefix}.stdout.raw',
                        'stderr': f'{prefix}.stderr.raw'})
    compare = subprocess.run(['/usr/bin/cmp', 'input01.stdout.raw',
                              'input02.stdout.raw'], cwd=native,
                             capture_output=True, check=False, timeout=30)
    (native / 'compare.stdout.raw').write_bytes(compare.stdout)
    (native / 'compare.stderr.raw').write_bytes(compare.stderr)
    records.append({'argv': ['/usr/bin/cmp', 'input01.stdout.raw',
                             'input02.stdout.raw'], 'cwd': str(native),
                    'returncode': compare.returncode,
                    'stdout': 'compare.stdout.raw', 'stderr': 'compare.stderr.raw'})
    passed = all(r['returncode'] == 0 for r in records)
    if passed:
        (HERE / 'INPUT_PINS.sha256').write_bytes(outputs[0])
    receipt = {'scope': 'artifact_only_no_scientific_execution',
               'started_utc': started,
               'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'source': {'path': str(Path(__file__).resolve()),
                          'sha256': digest(Path(__file__).resolve())},
               'interpreter': {'path': sys.executable, 'version': sys.version,
                               'sha256': digest(Path(sys.executable).resolve())},
               'tool_pins': {p: digest(Path(p)) for p in
                             ['/usr/bin/sha256sum', '/usr/bin/cmp']},
               'provenance_limit': 'Not a hermetic scientific or loader reuse key.',
               'input_count': len(INPUTS), 'scientific_runs': 0,
               'commands': records, 'pass': passed}
    (native / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    if not passed:
        raise SystemExit('Artifact capture failed; raw evidence retained.')
    print(json.dumps({'artifact_capture': 'PASS', 'inputs': len(INPUTS),
                      'new_scientific_runs': 0, 'raw_compare_exit': compare.returncode}))

if __name__ == '__main__':
    main()
