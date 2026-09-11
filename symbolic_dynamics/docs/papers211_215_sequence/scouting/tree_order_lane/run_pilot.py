"""Native one-run evidence capture; not a hermetic terminal replay claim."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
out = base / 'execution_01'
out.mkdir(exist_ok=False)
inputs = [base / 'INTAKE.md', base / 'pilot.py', Path(__file__).resolve(),
          Path('/usr/bin/python3').resolve()]
pins = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
argv = ['/usr/bin/python3', '-I', '-S', '-B', str(base / 'pilot.py')]
started = time.time_ns()
try:
    proc = subprocess.run(argv, cwd=base, capture_output=True, timeout=60,
                          env={'LC_ALL': 'C', 'LANG': 'C', 'PATH': '/usr/bin:/bin'})
    stdout, stderr, code, timeout = proc.stdout, proc.stderr, proc.returncode, False
except subprocess.TimeoutExpired as exc:
    stdout, stderr, code, timeout = exc.stdout or b'', exc.stderr or b'', None, True
ended = time.time_ns()
(out / 'stdout.txt').write_bytes(stdout)
(out / 'stderr.txt').write_bytes(stderr)
after = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
receipt = {'argv': argv, 'cwd': str(base), 'timeout_seconds': 60,
           'start_unix_ns': started, 'end_unix_ns': ended,
           'duration_seconds': (ended - started) / 1e9,
           'exit_code': code, 'timed_out': timeout,
           'environment': {'LC_ALL': 'C', 'LANG': 'C', 'PATH': '/usr/bin:/bin'},
           'input_sha256_before': pins, 'input_sha256_after': after,
           'stdout_sha256': hashlib.sha256(stdout).hexdigest(),
           'stderr_sha256': hashlib.sha256(stderr).hexdigest(),
           'stdout_bytes': len(stdout), 'stderr_bytes': len(stderr),
           'launcher_python': sys.version, 'launcher_executable': sys.executable,
           'provenance_limits': ['No interpreter/library snapshots',
                                 'No dynamic loader or process maps captured',
                                 'Not a strict terminal replay package',
                                 'One run only; no raw-pair comparison claimed']}
(out / 'NATIVE_RECEIPT.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
print(json.dumps(receipt, indent=2, sort_keys=True))
if code != 0 or timeout or pins != after:
    raise SystemExit(1)
