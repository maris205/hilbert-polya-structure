#!/usr/bin/env python3
"""Lane39 native documentary recorder; adapted infrastructure, no science."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import time

sys.dont_write_bytecode = True
OWN = pathlib.Path(__file__).resolve().parent
ROOT = OWN.parents[3]
SELF = pathlib.Path(__file__).resolve()
CONTROLS = [ROOT / 'SYMBOLIC_DYNAMICS_STATE.md', ROOT / 'docs/papers204_208_sequence/PIPELINE_STATE.md']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def forbidden(path):
    if path.is_relative_to(OWN) or not path.is_relative_to(ROOT):
        return False
    for part in path.relative_to(ROOT).parts:
        v = part.lower()
        if v in {'qa', 'review', 'reviews', 'freeze', 'freezes', 'build', 'builds', 'history', 'snapshots', 'capsules', 'capsule', 'runtime'}:
            return True
        if 'gate' in v or v.startswith(('p208', 'p209', '208-', '209-', 'ofs', 'fth', 'round0', 'round1', 'round2', 'terminal')):
            return True
        if re.search(r'(^|[^a-z0-9])(ofs|fth|p208|p209)([^a-z0-9]|$)', v):
            return True
        if any(name in v for name in ('order_geometry_tenth', 'finite_systems_tenth', 'finite_systems_nineteenth', 'finite_systems_twentieth')):
            return True
    return False


def capture(label, argv, inputs=()):
    target = OWN / 'commands' / label
    target.mkdir(parents=True, exist_ok=False)
    paths = sorted(set([SELF] + [pathlib.Path(p).resolve() for p in inputs]))
    for p in paths:
        assert p.is_file() and not p.is_symlink() and not forbidden(p), str(p)
    before = {str(p): sha(p) for p in paths}
    save(target / 'inputs_before.json', before)
    started = time.time()
    run = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (target / 'stdout.raw').write_bytes(run.stdout)
    (target / 'stderr.raw').write_bytes(run.stderr)
    after = {str(p): sha(p) for p in paths}
    save(target / 'inputs_after.json', after)
    receipt = dict(argv=argv, cwd=str(ROOT), started_epoch=started, finished_epoch=time.time(),
        exit=run.returncode, input_count=len(paths), unchanged=before == after,
        stdout_sha256=sha(target / 'stdout.raw'), stderr_sha256=sha(target / 'stderr.raw'),
        role='native_documentary_not_scientific_execution')
    save(target / 'receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    assert before == after
    return run


if __name__ == '__main__':
    if sys.argv[1:] == ['controls']:
        destination = OWN / 'controls'
        destination.mkdir(exist_ok=False)
        run = capture('01_control_copy', ['cp', '-p'] + [str(p) for p in CONTROLS] + [str(destination)], CONTROLS)
        assert run.returncode == 0
        roles = []
        for original in CONTROLS:
            copied = destination / original.name
            assert sha(original) == sha(copied)
            roles.append(dict(original_path=str(original), copy_path=str(copied), sha256=sha(copied),
                role='physical_copy_before_packaged_control_read_after_initial_navigation'))
        save(OWN / 'CONTROL_ROLES.json', roles)
        copied_paths = [destination / p.name for p in CONTROLS]
        run = capture('02_control_relevant', ['sed', '-n', '1,70p'] + [str(p) for p in copied_paths], copied_paths)
        assert run.returncode == 0
    elif sys.argv[1] == 'read':
        label, selection = sys.argv[2:4]
        paths = [ROOT / p for p in sys.argv[4:]]
        run = capture(label, ['sed', '-n', selection] + [str(p) for p in paths], paths)
        assert run.returncode == 0
    elif sys.argv[1:] == ['seal']:
        target = OWN / 'SHA256SUMS'
        assert not target.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
        target.write_text(''.join(sha(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(nonself_payloads=len(paths), sha256=sha(target))))
    else:
        raise SystemExit('bad mode')
