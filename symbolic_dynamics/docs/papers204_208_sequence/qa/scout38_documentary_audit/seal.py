"""Seal this QA directory only; intermediate native check then complete seal."""
import hashlib
from pathlib import Path
import shutil
import sys

sys.dont_write_bytecode = True
import capture
import check

HERE = Path(__file__).resolve().parent


def write_manifest(path, paths, relative):
    with path.open('x') as f:
        for p in paths:
            name = p.relative_to(HERE).as_posix() if relative else str(p)
            f.write(hashlib.sha256(check.read(p)).hexdigest() + '  ' + name + '\n')


if __name__ == '__main__':
    assert len(sys.argv) == 2
    if sys.argv[1] == 'payload_check':
        paths = sorted(check.files(HERE).values())
        manifest = HERE / 'PAYLOAD_SHA256SUMS'
        write_manifest(manifest, paths, False)
        exe = Path(shutil.which('sha256sum')).resolve()
        pins = sorted(set(paths + [manifest, exe, Path(sys.executable).resolve()]))
        raise SystemExit(capture.capture('payload_check', [str(exe), '-c', str(manifest)], pins))
    assert sys.argv[1] == 'final'
    paths = sorted(check.files(HERE).values())
    assert not (HERE / 'SHA256SUMS').exists()
    write_manifest(HERE / 'SHA256SUMS', paths, True)
    print('complete_nonself_payloads=' + str(len(paths)))
    print('manifest_sha256=' + hashlib.sha256(check.read(HERE / 'SHA256SUMS')).hexdigest())
