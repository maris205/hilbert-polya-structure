#!/usr/bin/env python3
"""Root native capture for exactly one preflight and one fresh MNA pair.

No scientific implementation is imported here. Every output is exclusive.
Actual success additionally requires the child's full nonself seal inspection.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers204_208_sequence/qa/mna_root_pair_execution'
PREP = ROOT / 'docs/papers204_208_sequence/qa/mna_root_pair_preparation'
OUT = ROOT / 'docs/papers204_208_sequence/qa/root_replays/mna_gate_pair_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}

def meta(data):
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def save(path, obj):
    with path.open('x') as stream:
        stream.write(json.dumps(obj, sort_keys=True, indent=2) + '\n')

def main():
    assert len(sys.argv) == 2 and sys.argv[1] in ('preflight', 'run')
    mode = sys.argv[1]
    assert HERE.resolve() == Path(__file__).resolve().parent
    folder = HERE / (mode + '_01')
    folder.mkdir()
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
        'pycache_prefix=' + str(OUT / 'unused_parent_cache'), str(PREP / 'run_pair.py'), mode,
        '--expected-gate-sha256', '5e15111b5dc6b4a585126e32fc59752b10cba8605f846d225e9efa26c656dc34',
        '--expected-verifier-sha256', '06db46cd3af7a192771d1d6494996dd1cac2e1f80ddabbaccfc128d2166e2239',
        '--expected-preparation-sha256', '3fce5fb3ce11f27f03d55828acb4522f69e03e55cafd4b2d02ac924b17f1bbf2']
    names = [Path(__file__).resolve(), PREP / 'run_pair.py', PREP / 'SHA256SUMS', Path('/usr/bin/python3.10')]
    before = {str(p): meta(p.read_bytes()) for p in names}
    attempt = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
        'started_utc': datetime.now(timezone.utc).isoformat(), 'timeout_seconds': 240,
        'inputs_before': before, 'role': 'root_native_parent_capture_not_an_independent_review'}
    save(folder / 'ATTEMPT.json', attempt)
    failure, timed_out, spawned, complete = None, False, True, True
    try:
        p = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, timeout=240, check=False)
        out, err, code, wrapper_code = p.stdout, p.stderr, p.returncode, p.returncode
    except subprocess.TimeoutExpired as exc:
        out, err, code, wrapper_code = exc.stdout or b'', exc.stderr or b'', None, 124
        failure, timed_out, complete = repr(exc), True, False
    except OSError as exc:
        out, err, code, wrapper_code = b'', b'', None, 127
        failure, spawned, complete = repr(exc), False, False
    for name, data in [('stdout.raw', out), ('stderr.raw', err)]:
        with (folder / name).open('xb') as stream:
            stream.write(data)
    after = {str(p): meta(p.read_bytes()) for p in names}
    receipt = {**attempt, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'exit_code': code, 'wrapper_exit_code': wrapper_code, 'failure': failure,
        'timed_out': timed_out, 'spawned': spawned, 'streams_complete': complete,
        'stdout': meta(out), 'stderr': meta(err), 'inputs_after': after,
        'inputs_unchanged': before == after}
    save(folder / 'RECEIPT.json', receipt)
    print(json.dumps(receipt, sort_keys=True, indent=2))
    if before != after:
        return 1
    return wrapper_code

if __name__ == '__main__':
    raise SystemExit(main())
