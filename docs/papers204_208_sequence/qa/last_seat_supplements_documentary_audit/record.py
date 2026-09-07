#!/usr/bin/env python3
"""Capture one new checker invocation in own immutable generated run directory."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

OWN = pathlib.Path(__file__).absolute().parent
ROOT = OWN.parents[3]
assert sys.flags.isolated and sys.dont_write_bytecode
assert len(sys.argv) == 2 and sys.argv[1].startswith('run_') and '/' not in sys.argv[1]
RUN = OWN / sys.argv[1]
RUN.mkdir(exist_ok=False)
argv = ['python3', '-I', '-B', str(OWN / 'check.py')]
started = time.time()
result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
for name, body in [('stdout.raw', result.stdout), ('stderr.raw', result.stderr)]:
    with (RUN / name).open('xb') as output:
        output.write(body)
receipt = dict(argv=argv, cwd=str(ROOT), started_epoch=started, finished_epoch=time.time(),
               exit=result.returncode, stdout_bytes=len(result.stdout), stderr_bytes=len(result.stderr),
               stdout_sha256=hashlib.sha256(result.stdout).hexdigest(), stderr_sha256=hashlib.sha256(result.stderr).hexdigest(),
               role='new_documentary_checker_execution_not_science_or_independent_mathematical_review')
if result.returncode == 0:
    receipt['summary'] = json.loads(result.stdout)['summary']
with (RUN / 'receipt.json').open('x') as output:
    output.write(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
print(json.dumps(receipt, sort_keys=True))
if result.returncode:
    print(result.stderr.decode(), file=sys.stderr, end='')
raise SystemExit(result.returncode)
