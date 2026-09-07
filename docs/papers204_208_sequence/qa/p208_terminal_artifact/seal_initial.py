"""Complete initial own-scope artifact seal; never modify scientific inputs."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent


def info(path):
    raw = Path(path).read_bytes()
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def save(path, raw):
    with Path(path).open('xb') as stream:
        stream.write(raw)


def check_manifest(base):
    rows = {}
    for line in (base / 'SHA256SUMS').read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        if match is None:
            raise RuntimeError('Malformed manifest')
        digest, name = match.groups()
        p = Path(name)
        if p.is_absolute() or '..' in p.parts or name in rows or name == 'SHA256SUMS':
            raise RuntimeError('Unsafe/duplicate/self manifest entry')
        path = base / p
        if path.is_symlink() or info(path)['sha256'] != digest:
            raise RuntimeError('Manifest referent mismatch')
        rows[name] = digest
    actual = {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file() and p != base / 'SHA256SUMS'}
    if actual != set(rows):
        raise RuntimeError('Incomplete nonself manifest')
    return len(rows)


def main():
    if len(sys.argv) != 1 or (BASE / 'SHA256SUMS').exists():
        raise RuntimeError('Require first exclusive initial seal, no arguments')
    attempts = {}
    for number in range(1, 6):
        name = 'initial_%02d' % number
        path = BASE / name
        count = check_manifest(path)
        command = json.loads((path / 'COMMAND.json').read_bytes())
        expected = 0 if number == 5 else 1
        if command['exit_code'] != expected or not command['inputs_unchanged'] or not command['unused_cache_absent']:
            raise RuntimeError('Actual attempt status mismatch')
        for stream in ('stdout', 'stderr'):
            if info(path / ('audit.' + stream)) != command[stream]:
                raise RuntimeError('Actual stream hash mismatch')
        attempts[name] = {'exit_code': expected, 'payloads': count,
                          'manifest_sha256': info(path / 'SHA256SUMS')['sha256']}
    check_manifest(BASE / 'lifecycle_before')
    accepted = json.loads((BASE / 'initial_05/audit.stdout').read_bytes())
    if accepted['status'] != 'PASS_P208_TERMINAL_ARTIFACT_GATE':
        raise RuntimeError('Missing actual initial PASS')
    if info(BASE.parent / 'audit_p208.py')['sha256'] != accepted['auditor_sha256']:
        raise RuntimeError('Accepted auditor changed')
    lifecycle = json.loads((BASE / 'lifecycle_before/RECEIPT.json').read_bytes())
    for original, row in lifecycle['original_to_snapshot'].items():
        wanted = {k: row[k] for k in ('bytes', 'sha256')}
        if info(original) != wanted or info(BASE / row['snapshot']) != wanted:
            raise RuntimeError('Root lifecycle changed before initial seal')
    files = [p for p in BASE.rglob('*') if p.is_file()]
    receipt = {'status': 'PASS_COMPLETE_INITIAL_P208_ARTIFACT_PACKAGE_SEAL',
               'utc': datetime.now(timezone.utc).isoformat(), 'payload_count': len(files) + 1,
               'attempts': attempts, 'accepted_auditor_sha256': accepted['auditor_sha256'],
               'accepted_stdout': info(BASE / 'initial_05/audit.stdout'),
               'report': info(BASE / 'REPORT.md'),
               'boundary': 'Initial package complete at this time; future lifecycle additions require preserved initial seal and separate closure.'}
    save(BASE / 'PACKAGE_RECEIPT.json', (json.dumps(receipt, sort_keys=True, indent=2) + '\n').encode())
    rows = [(info(p)['sha256'], p.relative_to(BASE).as_posix()) for p in sorted(BASE.rglob('*')) if p.is_file()]
    save(BASE / 'SHA256SUMS', ''.join(d + '  ' + n + '\n' for d, n in rows).encode())
    count = check_manifest(BASE)
    if count != receipt['payload_count']:
        raise RuntimeError('Final payload count mismatch')
    print(json.dumps({'status': receipt['status'], 'payloads': count,
                      'manifest_sha256': info(BASE / 'SHA256SUMS')['sha256']}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
