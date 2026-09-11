"""Compact native documentation-command capture; not a science verifier."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

BASE = pathlib.Path(__file__).resolve().parent
ROOT = BASE.parents[3]
name = sys.argv[1]
assert name.replace('_', '').isalnum()
command = sys.argv[2:]
assert command
out = BASE / 'commands' / name
out.mkdir(parents=True, exist_ok=False)
started = time.time_ns()
result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, timeout=60, check=False)
finished = time.time_ns()
(out / 'stdout.raw').write_bytes(result.stdout)
(out / 'stderr.raw').write_bytes(result.stderr)
receipt = {'kind': 'documentation_command_not_science', 'cwd': str(ROOT),
           'argv': command, 'start_unix_ns': started, 'end_unix_ns': finished,
           'exit_code': result.returncode,
           'stdout_bytes': len(result.stdout), 'stderr_bytes': len(result.stderr),
           'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
           'stderr_sha256': hashlib.sha256(result.stderr).hexdigest(),
           'runtime_limitations': 'No syscall/dependency closure; command and complete raw outputs only.'}
(out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, sort_keys=True))
sys.exit(result.returncode)
