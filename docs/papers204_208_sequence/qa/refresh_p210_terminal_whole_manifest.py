#!/usr/bin/env python3
"""One-time mechanical rolling-manifest refresh after preserved terminal lifecycle."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
P = ROOT / 'papers/210-weakly-increasing-run-aggregation'
QA = ROOT / 'docs/papers204_208_sequence/qa'
T = P / 'qa_final'
H = QA / 'p210_preterminal_controls_01'
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
    actual = json.loads((QA / 'P210_TERMINAL_RECEIVER01_ROOT_COMPLETION.actual.json').read_bytes())['result']
    assert actual['exit_code'] == 0 and json.loads(actual['output'])['status'] == 'PASS_ACTUAL_P210_TERMINAL_RECEPTION_CAPTURE'
    old_copy = H / 'PAPER_MANIFEST.sha256'
    old = P / 'PAPER_MANIFEST.sha256'
    assert digest(old) == digest(old_copy) == 'f2e772d8e9747d6f9572c119c1fcf2b53713df945066d34040452affeb0cefb4'
    assert old.read_bytes() == old_copy.read_bytes()
    prior = parse(old_copy)
    assert len(prior) == 2021
    expected = dict(prior)
    for name, h in prior.items():
        path = H / 'ROOT_LIFECYCLE.md' if name == 'ROOT_LIFECYCLE.md' else P / name
        assert digest(path) == h, name
    new_lifecycle = digest(P / 'ROOT_LIFECYCLE.md')
    assert new_lifecycle != prior['ROOT_LIFECYCLE.md']
    expected['ROOT_LIFECYCLE.md'] = new_lifecycle
    assert digest(T / 'SHA256SUMS') == '659b493dbc4e84137cf873643c1673b725294455d057c62b41e82572ffd31fd1'
    terminal = parse(T / 'SHA256SUMS')
    assert len(terminal) == 222
    for name, h in terminal.items():
        assert digest(T / name) == h
        expected['qa_final/' + name] = h
    expected['qa_final/SHA256SUMS'] = digest(T / 'SHA256SUMS')
    physical = list(P.rglob('*'))
    assert all(not p.is_symlink() for p in physical)
    names = {p.relative_to(P).as_posix() for p in physical if p.is_file()}
    assert len(expected) == 2244 and names == set(expected) | {'PAPER_MANIFEST.sha256'}
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
    receipt = {'status': 'PASS_P210_TERMINAL_LIFECYCLE_AND_WHOLE_MANIFEST_REFRESH', 'old_payloads': 2021,
        'current_payloads': 2244, 'physical_files': 2245, 'added_terminal_files': 223,
        'sole_changed_old_payload': 'ROOT_LIFECYCLE.md', 'old_whole_sha256': digest(old_copy),
        'old_lifecycle_sha256': prior['ROOT_LIFECYCLE.md'], 'new_lifecycle_sha256': new_lifecycle,
        'new_whole_sha256': digest(old), 'terminal_sha256': digest(T / 'SHA256SUMS'),
        'native': {'argv': ['/usr/bin/sha256sum', '--check', 'PAPER_MANIFEST.sha256'], 'cwd': str(P),
            'environment': ENV, 'exit': check.returncode, 'stdout': check.stdout.decode(), 'stderr': check.stderr.decode()},
        'source_sha256': digest(Path(__file__)), 'scope': 'Mechanical rolling manifest plus documentary lifecycle only; all original/frozen science bytes unchanged.'}
    output = QA / 'P210_TERMINAL_LIFECYCLE_REFRESH.actual.json'
    with output.open('x') as stream:
        json.dump(receipt, stream, sort_keys=True, indent=2)
        stream.write('\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'native'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()

