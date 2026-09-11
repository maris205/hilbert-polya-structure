#!/usr/bin/env python3
"""Capture the new documentary inspector once per fresh labelled output folder.

Generated artifacts are owned by this audit only. This is not an old producer.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time

HERE = Path(__file__).absolute().parent
ROOT = HERE.parents[3]


def metadata(body):
    return {'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()}


def save(path, obj):
    with path.open('x') as stream:
        stream.write(json.dumps(obj, sort_keys=True, indent=2) + '\n')


def main():
    label = sys.argv[1]
    if not re.fullmatch(r'attempt_[0-9]{2}', label):
        raise ValueError('fresh exact attempt label required')
    folder = HERE / label
    folder.mkdir()
    executable = str(Path(sys.executable).resolve())
    argv = [executable, '-I', '-S', '-B', str(HERE / 'inspect.py')]
    inputs = {str(p): metadata(p.read_bytes()) for p in (HERE / 'inspect.py', Path(__file__).absolute(), Path(executable))}
    started = time.time()
    save(folder / 'attempt.json', {'argv': argv, 'cwd': str(ROOT), 'started_epoch': started,
                                'timeout_seconds': 60, 'producer_input_pins': inputs,
                                'role': 'documentary_inspector_capture_not_scientific_execution'})
    try:
        result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                timeout=60, check=False)
        out, err, code, timed_out = result.stdout, result.stderr, result.returncode, False
    except subprocess.TimeoutExpired as ex:
        out, err, code, timed_out = ex.stdout or b'', ex.stderr or b'', 124, True
    for name, body in [('stdout.raw', out), ('stderr.raw', err)]:
        with (folder / name).open('xb') as stream:
            stream.write(body)
    after = {p: metadata(Path(p).read_bytes()) for p in inputs}
    receipt = {'argv': argv, 'cwd': str(ROOT), 'started_epoch': started, 'finished_epoch': time.time(),
               'exit': code, 'timed_out': timed_out, 'stdout': metadata(out), 'stderr': metadata(err),
               'producer_inputs_before': inputs, 'producer_inputs_after': after, 'producer_unchanged': inputs == after}
    save(folder / 'receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True, indent=2))
    if inputs != after:
        raise RuntimeError('documentary producer changed')
    raise SystemExit(code)


if __name__ == '__main__':
    main()
