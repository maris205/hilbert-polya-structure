#!/usr/bin/env python3
"""Preserve four actual pre-final central controls; do not change live inputs."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
OUT = QA / 'central_five_completion_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
EXPECTED = {
    'SYMBOLIC_DYNAMICS_STATE.md': '2dc4cdb6d5c41105b584a91720ff6b15a6ec772782e69ddbe9c1292a74e3f5d8',
    'docs/papers204_208_sequence/PIPELINE_STATE.md': '526671c3bbfd079ecd9c22c376ff3bf532be7e61ffe27b44dde48da86e6b67b3',
    'docs/papers204_208_sequence/FINAL_THEOREM_CONTRACTS.md': 'e22b39bfe4728890cb5e5f94231f6ae5f9b9805667d0f913c6466cd5fdfd0bb8',
    'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md': '55b13eb843175a36a7027eafcaa3324dc0251970920faf5ff4b58b1cab1215cc',
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
    inputs = [ROOT / name for name in EXPECTED] + [source, Path('/usr/bin/cp'), Path('/usr/bin/cmp')]
    before = {str(path): key(path) for path in inputs}
    assert all(before[str(ROOT / name)]['sha256'] == digest for name, digest in EXPECTED.items())
    assert len({Path(name).name for name in EXPECTED}) == 4
    OUT.mkdir(mode=0o700)
    save(OUT / 'INPUTS_BEFORE.json', before)
    save(OUT / 'executed_source.py', source.read_bytes())
    commands, copies = [], {}
    try:
        for name in EXPECTED:
            original, copy = ROOT / name, OUT / Path(name).name
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
        assert before == after and len(commands) == 8
        receipt = {'status': 'PASS_FOUR_ACTUAL_PRE_FINAL_CENTRAL_CONTROLS_PRESERVED',
                   'copies': copies, 'commands': commands, 'complete_input_pins': before,
                   'inputs_unchanged': True, 'original_controls': 4,
                   'scope': 'Four exact physical documentary copies only. No live edit, new science/build/view, five-paper acceptance or Git mutation.',
                   'external': 'OWNER_AMBER / HOLD_EXTERNAL'}
        save(OUT / 'PRESERVATION.actual.json', receipt)
        save(OUT / 'README.md', (
            '# Actual pre-final central controls\n\n'
            'The four live central controls were copied and independently raw-compared\n'
            'before the final index changes. Their exact original roles and eight actual\n'
            'native returns are in PRESERVATION.actual.json. These are history anchors,\n'
            'not current status, five-paper acceptance or a new Git push. The copies retain\n'
            'their original document origins. Live inputs and scientific evidence are unchanged.\n'
            'OWNER_AMBER / HOLD_EXTERNAL.\n').encode())
        members = sorted(path for path in OUT.iterdir() if path.is_file())
        assert len(members) == 9
        save(OUT / 'SHA256SUMS', ''.join(key(path)['sha256'] + '  ' + path.name + '\n' for path in members).encode())
        print(json.dumps({'status': receipt['status'], 'copies': copies, 'native_commands': commands,
                          'payloads': len(members), 'seal': key(OUT / 'SHA256SUMS')}, sort_keys=True))
    except BaseException:
        save(OUT / 'FAILURE.actual.json', {'commands': commands, 'copies': copies,
                                         'exception': traceback.format_exc(), 'no_acceptance': True})
        raise


if __name__ == '__main__':
    main()
