"""Records only static_revision.py; never invokes prepared target infrastructure."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def info(p):
    raw = p.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(p, raw):
    with p.open('xb') as stream:
        stream.write(raw)


def dump(p, value):
    save(p, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def main():
    assert sys.argv[1:] == ['static_01']
    folder = BASE / 'checks/static_01'; folder.mkdir(parents=True, exist_ok=False)
    inputs = {str(p): info(p) for p in sorted(BASE.rglob('*')) if p.is_file()}
    dump(folder / 'INPUTS_BEFORE.json', inputs)
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', str(BASE / 'static_revision.py')]
    attempt = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
               'started_utc': datetime.now(timezone.utc).isoformat(), 'exit_code': None, 'status': 'ATTEMPTED'}
    dump(folder / 'ATTEMPT.json', attempt)
    child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
    save(folder / 'stdout', child.stdout); save(folder / 'stderr', child.stderr)
    after = {p: info(Path(p)) for p in inputs}; dump(folder / 'INPUTS_AFTER.json', after)
    receipt = {**attempt, 'ended_utc': datetime.now(timezone.utc).isoformat(), 'exit_code': child.returncode,
               'status': 'COMPLETED', 'inputs_unchanged': inputs == after,
               'stdout': info(folder / 'stdout'), 'stderr': info(folder / 'stderr'),
               'scope': 'Static source/JSON/copy/diff checks only; target auditor, lifecycle and guard invocations zero.'}
    dump(folder / 'RECEIPT.json', receipt)
    print(child.stdout.decode(), end='')
    print(json.dumps({'actual_static_child_exit': child.returncode, 'stderr_bytes': len(child.stderr), 'inputs_unchanged': inputs == after}))
    if child.returncode:
        print(child.stderr.decode(), file=sys.stderr)
    assert child.returncode == 0 and not child.stderr and inputs == after


if __name__ == '__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    main()
