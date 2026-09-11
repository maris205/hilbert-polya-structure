#!/usr/bin/env python3
"""One-time mechanical rolling-manifest refresh after preserved completion lifecycle."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
P = ROOT / 'papers/210-weakly-increasing-run-aggregation'
QA = ROOT / 'docs/papers204_208_sequence/qa'
T = P / 'qa_final'
H = QA / 'p210_precompletion_controls_01'
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
    output = QA / 'P210_COMPLETION_LIFECYCLE_REFRESH.actual.json'
    assert not output.exists() and not output.is_symlink()
    acceptance = QA / 'P210_ARTIFACT_ROOT_ACCEPTANCE.actual.json'
    acceptance_sha256 = digest(acceptance)
    actual = json.loads(acceptance.read_bytes())
    required = {'schema': 'p210-root-initial-artifact-acceptance-v1',
        'status': 'ROOT_ACCEPTED_P210_INITIAL_ARTIFACT_LIFECYCLE_FOLLOWUP_PENDING',
        'paper': 'P210', 'root': '/root', 'native_session': 16560, 'native_exit': 0,
        'root_original_inspection_complete': True, 'complete_current_map_reconstructed': True,
        'paper_completion': False, 'five_paper_completion': False, 'external': 'OWNER_AMBER / HOLD_EXTERNAL'}
    assert all(type(actual[name]) is type(value) and actual[name] == value for name, value in required.items())
    for name, path in (('artifact_raw', QA / 'p210_terminal_artifact_03/ARTIFACT_REPORT.json'),
                       ('artifact_seal', QA / 'p210_terminal_artifact_03/SHA256SUMS')):
        assert path.is_file() and not path.is_symlink()
        raw = path.read_bytes()
        assert actual[name] == {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
        if name == 'artifact_raw':
            assert json.loads(raw)['status'] == 'PASS_P210_TERMINAL_ARTIFACT_INITIAL_LIFECYCLE_FOLLOWUP_PENDING'
    old_copy = H / 'PAPER_MANIFEST.sha256'
    old = P / 'PAPER_MANIFEST.sha256'
    assert digest(old) == digest(old_copy) == 'e821f92af0393af33308cce5667b24a93d183ed662a62b9232f25f15cb139ea2'
    assert old.read_bytes() == old_copy.read_bytes()
    prior = parse(old_copy)
    assert len(prior) == 2244
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
        assert digest(T / name) == h and expected['qa_final/' + name] == h
    assert expected['qa_final/SHA256SUMS'] == digest(T / 'SHA256SUMS')
    physical = list(P.rglob('*'))
    assert all(not p.is_symlink() for p in physical)
    names = {p.relative_to(P).as_posix() for p in physical if p.is_file()}
    assert len(expected) == 2244 and set(expected) == set(prior) and names == set(expected) | {'PAPER_MANIFEST.sha256'}
    assert [name for name in prior if prior[name] != expected[name]] == ['ROOT_LIFECYCLE.md']
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
    assert check.returncode == 0 and check.stderr == b'' and check.stdout == ''.join(name + ': OK\n' for name in sorted(expected)).encode()
    assert digest(acceptance) == acceptance_sha256
    receipt = {'status': 'PASS_P210_COMPLETION_LIFECYCLE_AND_WHOLE_MANIFEST_REFRESH', 'old_payloads': 2244,
        'current_payloads': 2244, 'physical_files': 2245, 'added_files': 0, 'deleted_files': 0,
        'sole_changed_old_payload': 'ROOT_LIFECYCLE.md', 'old_whole_sha256': digest(old_copy),
        'old_lifecycle_sha256': prior['ROOT_LIFECYCLE.md'], 'new_lifecycle_sha256': new_lifecycle,
        'new_whole_sha256': digest(old), 'terminal_sha256': digest(T / 'SHA256SUMS'),
        'initial_artifact_root_acceptance_sha256': acceptance_sha256,
        'artifact_raw': actual['artifact_raw'], 'artifact_seal': actual['artifact_seal'],
        'native': {'argv': ['/usr/bin/sha256sum', '--check', 'PAPER_MANIFEST.sha256'], 'cwd': str(P),
            'environment': ENV, 'exit': check.returncode, 'stdout': check.stdout.decode(), 'stderr': check.stderr.decode()},
        'source_sha256': digest(Path(__file__)), 'scope': 'Mechanical rolling manifest plus documentary lifecycle only; all original/frozen science and qa_final bytes unchanged. No new science/build/view or final artifact/five-paper acceptance.'}
    with output.open('x') as stream:
        json.dump(receipt, stream, sort_keys=True, indent=2)
        stream.write('\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'native'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
