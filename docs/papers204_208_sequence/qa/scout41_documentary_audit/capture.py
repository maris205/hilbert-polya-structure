#!/usr/bin/env python3
"""Capture actual local documentary outputs; exclusive writes, no overwrite."""
import json
import pathlib
import subprocess
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check

OWN, ROOT = check.OWN, check.ROOT


def main():
    if sys.argv[1:] == ['seal']:
        manifest = OWN / 'SHA256SUMS'
        assert not manifest.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != manifest)
        manifest.write_text(''.join(check.digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps({'nonself_payloads': len(paths), 'manifest_sha256': check.digest(manifest)}))
        return
    assert sys.argv[1:] == ['run']
    paths = check.input_paths()
    before = {str(p): check.digest(p) for p in paths}
    check.save(OWN / 'input_pins_before.json', before)
    argv = [sys.executable, '-B', str(OWN / 'check.py')]
    begin = time.time()
    run = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for name in ('stdout', 'stderr'):
        path = OWN / ('audit.' + name + '.raw')
        assert not path.exists()
        path.write_bytes(getattr(run, name))
    after = {str(p): check.digest(p) for p in paths}
    check.save(OWN / 'input_pins_after.json', after)
    receipt = {'argv': argv, 'invocation': [sys.executable, '-B', str(OWN / 'capture.py'), 'run'],
               'cwd': str(ROOT), 'exit': run.returncode, 'started_epoch': begin, 'finished_epoch': time.time(),
               'input_count': len(paths), 'unchanged': before == after,
               'stdout_sha256': check.digest(OWN / 'audit.stdout.raw'), 'stderr_sha256': check.digest(OWN / 'audit.stderr.raw'),
               'role': 'fresh_documentary_only_no_science_build_or_view',
               'runtime_limit': 'Executable hashes recorded; no strict full linked-runtime capsule or replay-reuse certification.'}
    check.save(OWN / 'receipt.actual.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    print(run.stdout.decode(), end='')
    print(run.stderr.decode(), end='', file=sys.stderr)
    assert before == after
    raise SystemExit(run.returncode)


if __name__ == '__main__':
    main()
