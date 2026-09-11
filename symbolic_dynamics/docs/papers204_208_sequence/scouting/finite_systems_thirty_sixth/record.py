#!/usr/bin/env python3
"""Scoped documentary recorder for source-first scouting, not a science kernel."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import time

OWN = pathlib.Path(__file__).resolve().parent
ROOT = OWN.parents[3]
CONTROLS = [ROOT / 'SYMBOLIC_DYNAMICS_STATE.md', ROOT / 'docs/papers204_208_sequence/PIPELINE_STATE.md',
            ROOT / 'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def forbidden(path):
    if path.is_relative_to(OWN):
        return False
    if not path.is_relative_to(ROOT):
        return False
    for part in path.relative_to(ROOT).parts:
        token = part.lower()
        if token in {'qa', 'review', 'reviews', 'freeze', 'freezes', 'build', 'builds', 'history', 'snapshots', 'capsules', 'capsule', 'runtime'}:
            return True
        if 'gate' in token or token.startswith(('p208', 'p209', '208-', '209-', 'ofs', 'fth', 'round0', 'round1', 'round2', 'terminal')):
            return True
        if re.search(r'(^|[^a-z0-9])(ofs|fth|p208|p209)([^a-z0-9]|$)', token):
            return True
        if any(name in token for name in ('order_geometry_tenth', 'finite_systems_tenth', 'finite_systems_nineteenth', 'finite_systems_twentieth')):
            return True
    return False


def capture(label, argv, inputs=(), cwd=ROOT):
    target = OWN / 'commands' / label
    target.mkdir(parents=True, exist_ok=False)
    paths = sorted(set([pathlib.Path(__file__).resolve()] + [pathlib.Path(p).resolve() for p in inputs]))
    for p in paths:
        assert p.is_file() and not p.is_symlink() and not forbidden(p), str(p)
    before = {str(p): digest(p) for p in paths}
    save(target / 'pathset.json', [str(p) for p in paths])
    save(target / 'inputs_before.json', before)
    started = time.time()
    result = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (target / 'stdout.raw').write_bytes(result.stdout)
    (target / 'stderr.raw').write_bytes(result.stderr)
    after = {str(p): digest(p) for p in paths}
    save(target / 'inputs_after.json', after)
    receipt = dict(argv=argv, cwd=str(cwd), started_epoch=started, finished_epoch=time.time(),
                   exit=result.returncode, input_count=len(paths), unchanged=before == after,
                   stdout_sha256=digest(target / 'stdout.raw'), stderr_sha256=digest(target / 'stderr.raw'),
                   role='native_documentary_command_not_scientific_execution')
    save(target / 'receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    assert before == after
    return result


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'bootstrap':
        dest = OWN / 'controls'
        dest.mkdir(exist_ok=False)
        result = capture('01_control_copy', ['cp', '-p'] + [str(p) for p in CONTROLS] + [str(dest)], CONTROLS)
        assert result.returncode == 0
        roles = []
        for original in CONTROLS:
            copy = dest / original.name
            assert digest(original) == digest(copy)
            roles.append(dict(original_path=str(original), copy_path=str(copy), sha256=digest(copy), role='physical_copy_before_body_read'))
        save(OWN / 'CONTROL_ROLES.json', roles)
    elif mode == 'controls':
        paths = [OWN / 'controls' / p.name for p in CONTROLS[:2]]
        result = capture('02_control_bodies', ['sed', '-n', '1,4000p'] + [str(p) for p in paths], paths)
        assert result.returncode == 0
    elif mode == 'read':
        label = sys.argv[2]
        paths = [ROOT / p for p in sys.argv[3:]]
        result = capture(label, ['sed', '-n', '1,4000p'] + [str(p) for p in paths], paths)
        assert result.returncode == 0
    elif mode == 'seal':
        target = OWN / 'SHA256SUMS'
        assert not target.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(nonself_payloads=len(paths), sha256=digest(target))))
    else:
        raise SystemExit('bad mode')
