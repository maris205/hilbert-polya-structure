"""P210 B owned native launch with safe explicit environment and full streams."""
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def write(path, data):
    with path.open('x') as stream:
        json.dump(data, stream, sort_keys=True, indent=2)
        stream.write('\n')


def pin(path):
    return {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}


label, mode = sys.argv[1:3]
assert mode in ('produce', 'pair', 'build')
assert label.replace('_', '').isalnum()
assert dict(os.environ) == ENV
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0
work = HERE / 'native' / label
work.mkdir(parents=True)
out = HERE / label
assert not out.exists()
paper = ROOT / 'papers/210-weakly-increasing-run-aggregation/frozen_round1' if mode == 'build' else HERE
argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
        'pycache_prefix=' + str(HERE / ('absent_driver_cache_' + label)),
        str(HERE / 'instrumentation/evidence.py'), mode,
        '--paper', str(paper), '--out', str(out)]
start = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
         'started_epoch': time.time(), 'timeout_seconds': 600,
         'launcher_source': pin(Path(__file__)), 'engine_source': pin(HERE / 'instrumentation/evidence.py')}
write(work / 'ATTEMPT.json', start)
with (work / 'stdout').open('xb') as stdout, (work / 'stderr').open('xb') as stderr:
    process = subprocess.Popen(argv, cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL,
                stdout=stdout, stderr=stderr, start_new_session=True)
    deadline = time.monotonic() + 600
    while process.poll() is None:
        if time.monotonic() >= deadline:
            os.killpg(process.pid, signal.SIGTERM)
            process.wait(timeout=10)
            break
        try:
            process.wait(timeout=20)
        except subprocess.TimeoutExpired:
            print(json.dumps({'status': 'RUNNING', 'label': label,
                              'pid': process.pid, 'elapsed': time.time() - start['started_epoch']}), flush=True)
members = []
for path in Path('/proc').iterdir():
    if not path.name.isdigit():
        continue
    try:
        raw = (path / 'stat').read_text()
        fields = raw[raw.rfind(')') + 2:].split()
        if int(fields[2]) == process.pid:
            members.append({'pid': int(path.name), 'state': fields[0], 'sid': int(fields[3])})
    except (OSError, ProcessLookupError, PermissionError):
        continue
assert not any(row['state'] != 'Z' for row in members), 'Unsettled native owner'
result = {**start, 'ended_epoch': time.time(), 'native_returncode': process.returncode,
          'pid': process.pid, 'owned_pgid': process.pid, 'owned_sid': process.pid,
          'settlement': {'quiescent': True, 'remaining_members': members},
          'stdout': pin(work / 'stdout'), 'stderr': pin(work / 'stderr')}
write(work / 'RESULT.json', result)
print(json.dumps(result, sort_keys=True))
raise SystemExit(process.returncode)
