"""Native retained wrapper for one scientific subprocess only."""
import hashlib
import json
import pathlib
import resource
import subprocess
import sys
import time

BASE = pathlib.Path(__file__).resolve().parent
ROOT = BASE.parents[3]
OUT = BASE / 'sole_pilot'
OUT.mkdir(exist_ok=False)
INPUTS = ['pilot_spr.py', 'run_sole_pilot.py', 'PREREG_SPR.md',
          'SPR_PROOF_PACKAGE.md', 'INTAKE.md', 'MPR_CLOSURE.md']


def pins():
    return {name: hashlib.sha256((BASE / name).read_bytes()).hexdigest()
            for name in INPUTS}


def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (55, 56))
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))


before = pins()
environment = {'PATH': '/usr/bin:/bin', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC',
               'PYTHONHASHSEED': '0', 'PYTHONDONTWRITEBYTECODE': '1',
               'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1'}
executable = str(pathlib.Path(sys.executable).resolve())
command = [executable, '-I', '-S', '-B', str(BASE / 'pilot_spr.py')]
start = time.time_ns()
timed_out = False
with (OUT / 'stdout.raw').open('xb') as stdout, (OUT / 'stderr.raw').open('xb') as stderr:
    try:
        result = subprocess.run(command, cwd=ROOT, env=environment,
                                stdout=stdout, stderr=stderr,
                                timeout=60, preexec_fn=limits, check=False)
        returncode = result.returncode
    except subprocess.TimeoutExpired:
        timed_out = True
        returncode = None
end = time.time_ns()
after = pins()
outputs = {path.name: {'bytes': path.stat().st_size,
                     'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
           for path in sorted(OUT.iterdir()) if path.is_file()}
receipt = {'kind': 'sole_scientific_native_subprocess', 'command': command,
           'cwd': str(ROOT), 'environment': environment, 'start_unix_ns': start,
           'end_unix_ns': end, 'elapsed_seconds': (end-start)/1e9,
           'exit_code': returncode, 'timed_out': timed_out,
           'limits': {'wall_seconds': 60, 'cpu_soft_seconds': 55,
                      'cpu_hard_seconds': 56, 'address_space_bytes': 512*1024**2},
           'inputs_before': before, 'inputs_after': after,
           'inputs_unchanged': before == after,
           'interpreter_realpath': executable,
           'interpreter_sha256': hashlib.sha256(pathlib.Path(executable).read_bytes()).hexdigest(),
           'wrapper_python_version': sys.version,
           'outputs': outputs,
           'limitations': 'Author run. No syscall-level dependency closure or independent replay. '
                          'Child declares imported-module and mapped-file runtime surface only. '
                          'OS/kernel/CPU/loader/tool-host state not fully pinned. Sources do not enter child numerics.'}
(OUT / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, sort_keys=True))
sys.exit(0 if returncode == 0 and not timed_out and before == after else 1)
