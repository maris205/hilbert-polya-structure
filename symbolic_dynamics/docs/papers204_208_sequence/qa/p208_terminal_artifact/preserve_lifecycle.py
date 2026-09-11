"""Preserve the two initial lifecycle bytes before any root-owned status edit.

Not an acceptance, science execution, or build. Exclusive own-scope output.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
PAPER = ROOT / 'papers/208-original-snapshot-triangulation-sweeps'


def info(path):
    raw = Path(path).read_bytes()
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def save(path, raw):
    with Path(path).open('xb') as stream:
        stream.write(raw)


def main():
    if len(sys.argv) != 2 or not sys.argv[1].replace('_', '').isalnum():
        raise RuntimeError('Require the exact passing attempt label')
    attempt = BASE / sys.argv[1]
    result = json.loads((attempt / 'audit.stdout').read_bytes())
    command = json.loads((attempt / 'COMMAND.json').read_bytes())
    if (result['status'] != 'PASS_P208_TERMINAL_ARTIFACT_GATE' or command['exit_code'] != 0
            or not command['inputs_unchanged'] or not command['unused_cache_absent']):
        raise RuntimeError('No successful original artifact audit to preserve')
    for stream in ('stdout', 'stderr'):
        if info(attempt / ('audit.' + stream)) != command[stream]:
            raise RuntimeError('Actual audit stream pin mismatch')
    if info(BASE.parent / 'audit_p208.py')['sha256'] != result['auditor_sha256']:
        raise RuntimeError('Passing auditor source changed')
    before = {}
    for name, archive_name in [('PAPER_STATUS.md', 'PAPER_STATUS.md'), ('SHA256SUMS', 'PAPER_SHA256SUMS')]:
        original = PAPER / name
        value = info(original)
        if value != result['all_consumed_inputs_rechecked'][str(original)]:
            raise RuntimeError('Lifecycle changed before preservation')
        before[str(original)] = {'snapshot': 'lifecycle_before/' + archive_name, **value}
    output = BASE / 'lifecycle_before'
    output.mkdir(exist_ok=False)
    for name, row in before.items():
        target = BASE / row['snapshot']
        save(target, Path(name).read_bytes())
        if info(target) != {k: row[k] for k in ('bytes', 'sha256')}:
            raise RuntimeError('Lifecycle snapshot copy mismatch')
    record = {'status': 'PASS_INITIAL_LIFECYCLE_BYTES_PRESERVED_NOT_ROOT_ACCEPTANCE',
              'utc': datetime.now(timezone.utc).isoformat(), 'initial_attempt': sys.argv[1],
              'initial_audit_stdout': info(attempt / 'audit.stdout'),
              'initial_attempt_manifest': info(attempt / 'SHA256SUMS'),
              'original_to_snapshot': before,
              'scope': 'Only the exact initial PAPER_STATUS.md and whole-paper manifest are copied; no input is edited.'}
    save(output / 'RECEIPT.json', (json.dumps(record, sort_keys=True, indent=2) + '\n').encode())
    rows = [(info(p)['sha256'], p.name) for p in sorted(output.iterdir()) if p.is_file()]
    save(output / 'SHA256SUMS', ''.join(d + '  ' + n + '\n' for d, n in rows).encode())
    print(json.dumps(record, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
