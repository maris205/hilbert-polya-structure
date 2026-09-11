"""Native exclusive-attempt recorder for this revision's documentary helpers."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
HERE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def info(path):
    data = Path(path).read_bytes()
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def save(path, data):
    with path.open('xb') as f:
        f.write(data)


def dump(path, value):
    save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def main():
    assert HERE == BATCH / 'qa/p209_terminal_artifact_revision_04' and dict(os.environ) == ENV and Path.cwd() == ROOT
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert len(sys.argv) == 3 and sys.argv[1] in {'scope', 'inspect', 'prepare', 'validate'} and sys.argv[2].replace('_', '').isalnum()
    mode, label = sys.argv[1:]
    script = HERE / ('documentary.py' if mode in {'scope', 'inspect'} else mode + '_revision.py')
    target = HERE / 'commands' / label
    target.mkdir(parents=True, exist_ok=False)
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', str(script)] + ([mode] if mode in {'scope', 'inspect'} else [])
    paths = {Path(__file__).resolve(), script, Path(sys.executable).resolve(), Path('/usr/bin/cmp'), Path('/usr/bin/diff')}
    if mode != 'scope':
        scope = HERE / 'SCOPE.json'
        paths.add(scope)
        paths.update(Path(p) for p in json.loads(scope.read_bytes())['input_pins'])
        paths.update(p for p in HERE.rglob('*') if p.is_file() and not p.is_relative_to(target))
    else:
        # Scope discovery has fixed seed pins plus first-read/after pins inside
        # SCOPE.json. Subsequent inspection has the complete discovered set
        # pinned before spawning; this is not retroactive pre-read provenance.
        old = BATCH / 'qa/p209_terminal_artifact_revision_03'
        paths.update(old / n for n in ('SHA256SUMS', 'audit_p209.py', 'record_audit.py', 'lifecycle_audit.py'))
        paths.update(p for p in (BATCH / 'qa/p209_terminal_artifact/initial_04').iterdir() if p.is_file())
        paths.add(BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_04.failed.actual.json')
    paths = sorted(paths)
    before = {str(p): info(p) for p in paths}
    dump(target / 'INPUTS_BEFORE.json', before)
    for path in {Path(__file__).resolve(), script}:
        save(target / (path.name + '.at_execution'), path.read_bytes())
    invocation = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_utc': datetime.now(timezone.utc).isoformat(),
                  'status': 'ATTEMPTED', 'exit_code': None, 'scope': 'documentary helper only; never target auditor/lifecycle/science/build/view'}
    dump(target / 'ATTEMPT.json', invocation)
    failure = None
    try:
        child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        code, stdout, stderr = child.returncode, child.stdout, child.stderr
    except OSError as exc:
        failure = repr(exc)
        code, stdout, stderr = 127, b'', str(exc).encode()
    save(target / 'stdout.raw', stdout)
    save(target / 'stderr.raw', stderr)
    after = {str(p): info(p) for p in paths}
    dump(target / 'INPUTS_AFTER.json', after)
    result = {**invocation, 'status': 'COMPLETED' if failure is None else 'SPAWN_FAILED', 'failure': failure,
              'exit_code': code, 'ended_utc': datetime.now(timezone.utc).isoformat(), 'input_count': len(before),
              'inputs_unchanged': before == after, 'stdout': info(target / 'stdout.raw'), 'stderr': info(target / 'stderr.raw')}
    dump(target / 'COMMAND.json', result)
    print(json.dumps(result, sort_keys=True))
    if code:
        print(stderr.decode(errors='replace'), file=sys.stderr)
    assert before == after
    raise SystemExit(code)


if __name__ == '__main__':
    main()
