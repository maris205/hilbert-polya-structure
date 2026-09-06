#!/usr/bin/env python3
"""Exclusive raw-byte recorder for this one read-only terminal artifact check."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CHECKER = HERE.parent/'audit_p207.py'


def info(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def save(path, raw):
    with path.open('xb') as stream:
        stream.write(raw)


def main():
    if len(sys.argv) != 2 or not re.fullmatch('[a-z0-9_]+', sys.argv[1]):
        raise SystemExit('Expected one new lowercase attempt label')
    out = HERE/sys.argv[1]
    out.mkdir(exist_ok=False)
    source = CHECKER.read_bytes()
    save(out/'executed_source_snapshot.py', source)
    python = str(Path(sys.executable).resolve())
    command = [python, '-I', '-B', str(CHECKER)]
    before = {'checker': info(CHECKER), 'recorder': info(Path(__file__).resolve()), 'python': info(Path(python))}
    started = datetime.now(timezone.utc).isoformat()
    with (out/'run.stdout').open('xb') as stdout, (out/'run.stderr').open('xb') as stderr:
        child = subprocess.run(command, cwd=ROOT, stdout=stdout, stderr=stderr, check=False)
    after = {'checker': info(CHECKER), 'recorder': info(Path(__file__).resolve()), 'python': info(Path(python))}
    raw = (out/'run.stdout').read_bytes()
    parsed = json.loads(raw) if child.returncode == 0 else None
    passed = child.returncode == 0 and before == after and parsed.get('status') == 'PASS_P207_TERMINAL_ARTIFACT_GATE'
    record = {'kind': 'ACTUAL_P207_TERMINAL_ARTIFACT_CHECK_NOT_MATHEMATICS_BUILD_OR_VIEW',
              'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
              'command': command, 'cwd': str(ROOT), 'exit_code': child.returncode,
              'execution_succeeded_and_inputs_stable': passed,
              'before_execution_inputs': before, 'after_execution_inputs': after,
              'executed_source_snapshot': {'path': 'executed_source_snapshot.py', **info(out/'executed_source_snapshot.py')},
              'source_execution_note': 'Original checker path executed; source snapshot equals its bytes before and after, not relocated execution.',
              'stdout': {'path': 'run.stdout', **info(out/'run.stdout')},
              'stderr': {'path': 'run.stderr', **info(out/'run.stderr')},
              'raw_output_note': 'Captured directly to binary files by subprocess; no text normalization, JSON reserialization or patch transport.',
              'artifact_checks': parsed.get('checks') if parsed else None,
              'fresh_mathematical_executions': 0, 'fresh_builds': 0, 'fresh_visual_views': 0}
    save(out/'RECEIPT.json', (json.dumps(record, indent=2, sort_keys=True)+'\n').encode())
    rows = ''.join(sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in sorted(out.iterdir()) if p.is_file())
    save(out/'SHA256SUMS', rows.encode())
    print(json.dumps({'pass': passed, 'exit_code': child.returncode, 'artifact_checks': record['artifact_checks'],
                      'receipt': str(out/'RECEIPT.json'), 'stdout': record['stdout'], 'stderr': record['stderr']}, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
