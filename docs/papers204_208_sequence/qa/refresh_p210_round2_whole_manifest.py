#!/usr/bin/env python3
"""One-time mechanical rolling-manifest refresh after preserved Round2 lifecycle."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
P = ROOT / 'papers/210-weakly-increasing-run-aggregation'
QA = ROOT / 'docs/papers204_208_sequence/qa'
R2 = P / 'frozen_round2'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def digest(path):
    assert path.is_file() and not path.is_symlink()
    return sha256(path.read_bytes()).hexdigest()


def parse(path):
    rows = {}
    for line in path.read_text().splitlines():
        h, name = line.split('  ', 1)
        assert len(h) == 64 and all(c in '0123456789abcdef' for c in h)
        assert name not in rows and '..' not in Path(name).parts and not Path(name).is_absolute()
        rows[name] = h
    return rows


def main():
    actual = json.loads((QA / 'P210_ROUND2_ROOT_INSPECTION_COMPLETION.actual.json').read_bytes())['result']
    assert actual['exit_code'] == 0 and json.loads(actual['output'])['status'] == 'PASS_ROOT_PHYSICAL_P210_ROUND2_RECEPTION'
    old_copy = R2 / 'ROUND2_ACCEPTANCE/PRE_ROUND2_PAPER_MANIFEST.sha256'
    old = P / 'PAPER_MANIFEST.sha256'
    assert digest(old) == digest(old_copy) == 'a1abc5b290ed6a74cb6f8b1fb959f479d84926886ff9ce0b8d8179b806e6c94f'
    assert old.read_bytes() == old_copy.read_bytes()
    prior = parse(old_copy)
    assert len(prior) == 1496
    expected = dict(prior)
    for name, h in prior.items():
        path = R2 / 'ROUND2_ACCEPTANCE/PRE_ROUND2_ROOT_LIFECYCLE.md' if name == 'ROOT_LIFECYCLE.md' else P / name
        assert digest(path) == h, name
    new_lifecycle = digest(P / 'ROOT_LIFECYCLE.md')
    assert new_lifecycle != prior['ROOT_LIFECYCLE.md']
    expected['ROOT_LIFECYCLE.md'] = new_lifecycle
    assert digest(R2 / 'SHA256SUMS') == 'a46fb6688ce56fbf62f69b8c652fff88923e3778c81647294bae544f5e86a703'
    frozen = parse(R2 / 'SHA256SUMS')
    assert len(frozen) == 524
    for name, h in frozen.items():
        assert digest(R2 / name) == h
        expected['frozen_round2/' + name] = h
    expected['frozen_round2/SHA256SUMS'] = digest(R2 / 'SHA256SUMS')
    physical = list(P.rglob('*'))
    assert all(not p.is_symlink() for p in physical)
    names = {p.relative_to(P).as_posix() for p in physical if p.is_file()}
    assert len(expected) == 2021 and names == set(expected) | {'PAPER_MANIFEST.sha256'}
    for name, h in expected.items():
        assert digest(P / name) == h
    data = ''.join(h + '  ' + name + '\n' for name, h in sorted(expected.items())).encode()
    # This is the sole rolling output; its exact previous bytes are physical
    # and validated above. No immutable author/review/frozen file is modified.
    old.write_bytes(data)
    assert old.read_bytes() == data and parse(old) == expected
    for name, h in expected.items():
        assert digest(P / name) == h
    check = subprocess.run(['/usr/bin/sha256sum', '--check', 'PAPER_MANIFEST.sha256'], cwd=P, env=ENV,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
    assert check.returncode == 0 and not check.stderr and check.stdout.decode().splitlines() == [name + ': OK' for name in sorted(expected)]
    receipt = {'status': 'PASS_P210_ROUND2_LIFECYCLE_AND_WHOLE_MANIFEST_REFRESH', 'old_payloads': 1496,
        'current_payloads': 2021, 'physical_files': 2022, 'added_round2_files': 525,
        'sole_changed_old_payload': 'ROOT_LIFECYCLE.md', 'old_whole_sha256': digest(old_copy),
        'old_lifecycle_sha256': prior['ROOT_LIFECYCLE.md'], 'new_lifecycle_sha256': new_lifecycle,
        'new_whole_sha256': digest(old), 'round2_sha256': digest(R2 / 'SHA256SUMS'),
        'native': {'argv': ['/usr/bin/sha256sum', '--check', 'PAPER_MANIFEST.sha256'], 'cwd': str(P),
            'environment': ENV, 'exit': check.returncode, 'stdout': check.stdout.decode(), 'stderr': check.stderr.decode()},
        'source_sha256': digest(Path(__file__)), 'scope': 'Mechanical rolling manifest plus documentary lifecycle only; all original/frozen science bytes unchanged.'}
    output = QA / 'P210_ROUND2_LIFECYCLE_REFRESH.actual.json'
    with output.open('x') as stream:
        json.dump(receipt, stream, sort_keys=True, indent=2)
        stream.write('\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'native'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()

