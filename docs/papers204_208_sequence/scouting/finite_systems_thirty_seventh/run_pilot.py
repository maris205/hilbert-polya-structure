#!/usr/bin/env python3
"""Capture exactly one own original SMV pilot and its bounded dependency pins."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

OWN = pathlib.Path(__file__).absolute().parent
ROOT = OWN.parents[3]
RUN = OWN / 'pilot_run'
RUN.mkdir(exist_ok=False)
inputs = [OWN / name for name in ('INTAKE.md', 'SOURCE_DESK.md', 'PROOF_PACKAGE.md',
                                  'PILOT_CONTRACT.md', 'pilot.py', 'run_pilot.py')]
inputs.append(pathlib.Path(sys.executable).resolve())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, value):
    with (RUN / name).open('x') as stream:
        stream.write(json.dumps(value, sort_keys=True, indent=2) + '\n')


before = {str(p): dict(sha256=digest(p), bytes=p.stat().st_size) for p in sorted(set(inputs))}
save('inputs_before.json', before)
argv = [sys.executable, '-I', '-S', '-B', str(OWN / 'pilot.py')]
started = time.time()
save('attempt.json', dict(argv=argv, cwd=str(ROOT), started_epoch=started, timeout_seconds=60,
                          role='one_original_fixed_box_scientific_pilot_not_admission',
                          python_version=sys.version, python_executable=sys.executable))
try:
    result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, check=False)
    code, stdout, stderr, timed_out = result.returncode, result.stdout, result.stderr, False
except subprocess.TimeoutExpired as error:
    code, stdout, stderr, timed_out = 124, error.stdout or b'', error.stderr or b'', True
for name, body in [('stdout.raw', stdout), ('stderr.raw', stderr)]:
    with (RUN / name).open('xb') as stream:
        stream.write(body)
after = {str(p): dict(sha256=digest(p), bytes=p.stat().st_size) for p in sorted(set(inputs))}
save('inputs_after.json', after)
receipt = dict(argv=argv, cwd=str(ROOT), started_epoch=started, finished_epoch=time.time(), exit=code,
               timed_out=timed_out, unchanged=before == after, input_count=len(before),
               stdout_bytes=len(stdout), stderr_bytes=len(stderr),
               stdout_sha256=hashlib.sha256(stdout).hexdigest(), stderr_sha256=hashlib.sha256(stderr).hexdigest(),
               role='one_original_fixed_box_scientific_pilot_not_admission',
               canonical_output='pilot_run/stdout.raw; full raw output, no normalized-text substitution')
if code == 0:
    result = json.loads(stdout)
    receipt['compact_result'] = {k: result[k] for k in ('status', 'total_states', 'total_targets', 'checks')}
    receipt['compact_result']['fields'] = [{k: row[k] for k in ('prime', 'state_count', 'maximum_depth', 'cycle_length_histogram', 'image_size', 'fibre_histogram')} for row in result['boxes']]
save('receipt.json', receipt)
print(json.dumps(receipt, sort_keys=True))
if code:
    print(stderr.decode(), file=sys.stderr, end='')
assert before == after
raise SystemExit(code)
