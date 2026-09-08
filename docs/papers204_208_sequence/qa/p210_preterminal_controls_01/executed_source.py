#!/usr/bin/env python3
"""Preserve the two actual preterminal controls without changing live inputs."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
OUT = QA / 'p210_preterminal_controls_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
EXPECTED = {
    'ROOT_LIFECYCLE.md': '7c0ce6eba60df7ccc98219ccf3f5f12707f118fa3b1f7eff63168735fbf36fe0',
    'PAPER_MANIFEST.sha256': 'f2e772d8e9747d6f9572c119c1fcf2b53713df945066d34040452affeb0cefb4',
}


def key(path):
    assert path.is_file() and not path.is_symlink() and path.resolve() == path
    raw = path.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(path, value):
    raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with path.open('xb') as stream:
        stream.write(raw)


def main():
    source = Path(__file__).resolve()
    assert OUT.resolve() == OUT and not OUT.exists() and not OUT.is_symlink()
    inputs = [PAPER / name for name in EXPECTED] + [source, Path('/usr/bin/cp'), Path('/usr/bin/cmp')]
    before = {str(path): key(path) for path in inputs}
    assert all(before[str(PAPER / name)]['sha256'] == digest for name, digest in EXPECTED.items())
    rows = (PAPER / 'PAPER_MANIFEST.sha256').read_text().splitlines()
    assert len(rows) == 2021 and rows.count(EXPECTED['ROOT_LIFECYCLE.md'] + '  ROOT_LIFECYCLE.md') == 1
    OUT.mkdir(mode=0o700)
    save(OUT / 'INPUTS_BEFORE.json', before)
    save(OUT / 'executed_source.py', source.read_bytes())
    commands, copies = [], {}
    try:
        for name in EXPECTED:
            original, copy = PAPER / name, OUT / name
            assert not copy.exists()
            for argv in (['/usr/bin/cp', '--no-clobber', '--', str(original), str(copy)],
                         ['/usr/bin/cmp', '--', str(original), str(copy)]):
                native = subprocess.run(argv, cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
                commands.append({'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
                                 'exit_code': native.returncode, 'stdout': native.stdout.decode(),
                                 'stderr': native.stderr.decode()})
                assert native.returncode == 0 and native.stdout == native.stderr == b''
            assert key(copy) == before[str(original)] and original.read_bytes() == copy.read_bytes()
            copies[str(original)] = {'physical': str(copy), **key(copy)}
        after = {str(path): key(path) for path in inputs}
        save(OUT / 'INPUTS_AFTER.json', after)
        assert before == after and len(commands) == 4
        receipt = {'status': 'PASS_TWO_ACTUAL_P210_PRETERMINAL_CONTROLS_PRESERVED',
                   'copies': copies, 'commands': commands, 'complete_input_pins': before,
                   'inputs_unchanged': True, 'old_whole_payloads': 2021,
                   'scope': 'Two exact physical documentary copies only. No live edit, new science/build/view, lifecycle refresh or artifact acceptance.',
                   'external': 'OWNER_AMBER / HOLD_EXTERNAL'}
        save(OUT / 'PRESERVATION.actual.json', receipt)
        save(OUT / 'README.md', (
            '# Actual P210 preterminal controls\n\n'
            'The two live controls were copied and independently raw-compared before any\n'
            'terminal lifecycle change. Their exact original roles and four actual native\n'
            'returns are in PRESERVATION.actual.json. The old whole manifest has 2,021\n'
            'payloads and intentionally predates qa_final. These are history anchors,\n'
            'not a terminal build, view, lifecycle or artifact PASS. Live inputs are unchanged.\n'
            'OWNER_AMBER / HOLD_EXTERNAL.\n').encode())
        members = sorted(path for path in OUT.iterdir() if path.is_file())
        assert len(members) == 7
        save(OUT / 'SHA256SUMS', ''.join(key(path)['sha256'] + '  ' + path.name + '\n' for path in members).encode())
        print(json.dumps({'status': receipt['status'], 'copies': copies, 'native_commands': commands,
                          'payloads': len(members), 'seal': key(OUT / 'SHA256SUMS')}, sort_keys=True))
    except BaseException:
        save(OUT / 'FAILURE.actual.json', {'commands': commands, 'copies': copies,
                                         'exception': traceback.format_exc(), 'no_acceptance': True})
        raise


if __name__ == '__main__':
    main()
