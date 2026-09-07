"""Seal this completed static preparation only; never invokes target code.

The final native checksum output is returned, not appended to the sealed
directory. SHA256SUMS is the only file excluded from its own complete seal.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def info(path):
    raw = Path(path).read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def main():
    assert HERE == ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_03'
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    assert sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode
    assert not (HERE / 'SHA256SUMS').exists()
    assert not (ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_artifact/initial_04').exists()
    result = json.loads((HERE / 'STATIC_RESULT.json').read_bytes())
    assert result['status'] == 'PASS_STATIC_PREPARATION_ONLY_NOT_ARTIFACT_GATE'
    assert result['target_auditor_lifecycle_guard_executions'] == result['new_science_build_render_views'] == 0
    assert all(info(path) == value for path, value in result['original_inputs_after'].items())
    files = sorted(path for path in HERE.rglob('*') if path.is_file())
    assert all(not path.is_symlink() for path in HERE.rglob('*'))
    manifest = ''.join(info(path)['sha256'] + '  ' + path.relative_to(HERE).as_posix() + '\n' for path in files)
    with (HERE / 'SHA256SUMS').open('xb') as stream:
        stream.write(manifest.encode())
    argv = ['/usr/bin/sha256sum', '-c', 'SHA256SUMS']
    native = subprocess.run(argv, cwd=HERE, env=ENV, capture_output=True, check=False)
    assert native.returncode == 0 and native.stderr == b''
    assert len(native.stdout.decode().splitlines()) == len(files)
    print(json.dumps({'status': 'SEALED_STATIC_PREPARATION_ONLY_NOT_ARTIFACT_GATE', 'payloads': len(files),
        'manifest_sha256': info(HERE / 'SHA256SUMS')['sha256'], 'only_nonself_exclusion': 'SHA256SUMS',
        'actual_native_command': {'argv': argv, 'cwd': str(HERE), 'env': ENV, 'exit_code': native.returncode,
                                 'stdout': native.stdout.decode(), 'stderr': native.stderr.decode()},
        'target_executions': 0}, sort_keys=True))


if __name__ == '__main__':
    main()
