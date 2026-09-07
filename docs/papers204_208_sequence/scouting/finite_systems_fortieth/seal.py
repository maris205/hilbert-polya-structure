#!/usr/bin/env python3
"""Create and verify one complete nonself manifest after actual audit closure."""
import hashlib
import json
from pathlib import Path

OWN = Path(__file__).absolute().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = OWN / 'SHA256SUMS'
    assert not manifest.exists(), 'refuse to replace a sealed manifest'
    audit_dir = OWN / 'commands/20_artifact_audit'
    receipt = json.loads((audit_dir / 'receipt.json').read_text())
    assert receipt['exit'] == 0 and receipt['unchanged'] is True
    assert receipt['stderr']['bytes'] == 0
    assert digest(audit_dir / 'stdout.raw') == receipt['stdout']['sha256']
    assert json.loads((audit_dir / 'stdout.raw').read_text())['status'] == 'PASS'
    before = json.loads((audit_dir / 'inputs_before.json').read_text())
    after = json.loads((audit_dir / 'inputs_after.json').read_text())
    assert before == after
    for name, pinned in before.items():
        path = Path(name)
        assert path.is_file() and not path.is_symlink()
        assert digest(path) == pinned['sha256'] and path.stat().st_size == pinned['bytes']
    files = sorted(p for p in OWN.rglob('*') if p.is_file())
    assert all(not p.is_symlink() for p in OWN.rglob('*'))
    lines = [digest(p) + '  ' + p.relative_to(OWN).as_posix() for p in files]
    with manifest.open('x') as stream:
        stream.write('\n'.join(lines) + '\n')
    declared = {}
    for line in manifest.read_text().splitlines():
        sha, name = line.split('  ', 1)
        assert name not in declared and name != 'SHA256SUMS'
        declared[name] = sha
        assert digest(OWN / name) == sha
    actual = {p.relative_to(OWN).as_posix() for p in OWN.rglob('*')
              if p.is_file() and p != manifest}
    assert set(declared) == actual
    print(json.dumps({'status': 'PASS', 'role': 'complete_nonself_manifest_seal_no_science',
                      'files': len(declared), 'manifest_sha256': digest(manifest),
                      'bytes_total_excluding_manifest': sum(p.stat().st_size for p in files),
                      'audit_exit': receipt['exit'], 'central_controls_unchanged': True},
                     sort_keys=True))


if __name__ == '__main__':
    main()
