"""Exclusive artifact-auditor execution records; no scientific code is run."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
SOURCE = BASE.parent / 'audit_p208.py'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}


def info(path):
    raw = Path(path).read_bytes()
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def save(path, raw):
    with Path(path).open('xb') as stream:
        stream.write(raw)


def dump(path, value):
    save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def main():
    if len(sys.argv) != 2 or not sys.argv[1].replace('_', '').isalnum():
        raise RuntimeError('Require one safe new attempt label')
    if sys.flags.optimize or not (sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):
        raise RuntimeError('Require -I -S -B and optimization zero')
    target = BASE / sys.argv[1]
    target.mkdir(exist_ok=False)
    save(target / 'executed_auditor_snapshot.py', SOURCE.read_bytes())
    save(target / 'executed_recorder_snapshot.py', Path(__file__).read_bytes())
    before = {'auditor': info(SOURCE), 'recorder': info(__file__),
              'python': info(Path(sys.executable).resolve()),
              'paper_manifest': info(ROOT / 'papers/208-original-snapshot-triangulation-sweeps/SHA256SUMS')}
    dump(target / 'INPUTS_BEFORE.json', before)
    cache = target / 'unused_pycache'
    argv = [str(Path(sys.executable).resolve()), '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(cache), str(SOURCE)]
    started = datetime.now(timezone.utc).isoformat()
    dump(target / 'ATTEMPT.json', {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
                                 'started_utc': started, 'status': 'ATTEMPTED'})
    child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
    for name, raw in [('audit.stdout', child.stdout), ('audit.stderr', child.stderr)]:
        save(target / name, raw)
    after = {'auditor': info(SOURCE), 'recorder': info(__file__),
             'python': info(Path(sys.executable).resolve()),
             'paper_manifest': info(ROOT / 'papers/208-original-snapshot-triangulation-sweeps/SHA256SUMS')}
    dump(target / 'INPUTS_AFTER.json', after)
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_utc': started,
           'ended_utc': datetime.now(timezone.utc).isoformat(), 'exit_code': child.returncode,
           'unused_cache_absent': not cache.exists(), 'inputs_unchanged': before == after,
           'stdout': info(target / 'audit.stdout'), 'stderr': info(target / 'audit.stderr'),
           'role': 'Actual documentary artifact audit execution; no new science, build or views.'}
    dump(target / 'COMMAND.json', row)
    rows = [(info(p)['sha256'], p.relative_to(target).as_posix())
            for p in sorted(target.rglob('*')) if p.is_file()]
    save(target / 'SHA256SUMS', ''.join(d + '  ' + n + '\n' for d, n in rows).encode())
    print(json.dumps(row, indent=2, sort_keys=True))
    if child.returncode:
        print(child.stderr.decode(), file=sys.stderr)
    elif before != after or cache.exists():
        raise RuntimeError('Post-audit recorder input/cache check failed')
    else:
        result = json.loads(child.stdout)
        print(json.dumps({k: result[k] for k in ('status', 'checks', 'all_consumed_input_count')}, sort_keys=True))
    raise SystemExit(child.returncode)


if __name__ == '__main__':
    main()
