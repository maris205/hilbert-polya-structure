#!/usr/bin/env python3
"""Decision-support receipts only; no scientific producer or pilot."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
OWN = pathlib.Path(__file__).resolve().parent
CONTROL = {
    'SYMBOLIC_DYNAMICS_STATE.md': ROOT / 'SYMBOLIC_DYNAMICS_STATE.md',
    'PIPELINE_STATE.md': ROOT / 'docs/papers204_208_sequence/PIPELINE_STATE.md',
    'GIT_SYNC_RECEIPT.md': ROOT / 'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md',
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')

def forbidden(path):
    if path.is_relative_to(OWN):
        return False
    parts = path.relative_to(ROOT).parts
    return any(p.lower() in {'qa', 'reviews', 'review', 'freeze', 'freezes', 'build', 'builds'}
               or 'gate' in p.lower() or 'fth' in p.lower() or 'ofs' in p.lower()
               or p.lower().startswith(('208', '209', 'p208', 'p209', 'round0', 'round1', 'round2', 'terminal'))
               for p in parts)

def capture(label, argv, inputs=(), cwd=ROOT):
    directory = OWN / 'commands' / label
    directory.mkdir(parents=True, exist_ok=False)
    paths = sorted(set([pathlib.Path(__file__).resolve()] + [pathlib.Path(p).resolve() for p in inputs]))
    for p in paths:
        assert p.is_file(), str(p)
        assert not p.is_relative_to(ROOT) or not forbidden(p), str(p)
    save(directory / 'pathset.json', [str(p) for p in paths])
    before = {str(p): digest(p) for p in paths}
    save(directory / 'inputs_before.json', before)
    start = time.time()
    result = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (directory / 'stdout.raw').write_bytes(result.stdout)
    (directory / 'stderr.raw').write_bytes(result.stderr)
    after = {str(p): digest(p) for p in paths}
    save(directory / 'inputs_after.json', after)
    receipt = dict(role='new_native_documentary_command_not_scientific_execution',
        label=label, argv=argv, cwd=str(cwd), started_epoch=start, finished_epoch=time.time(),
        exit=result.returncode, input_count=len(paths), unchanged=before == after,
        stdout_sha256=digest(directory / 'stdout.raw'), stderr_sha256=digest(directory / 'stderr.raw'))
    save(directory / 'receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    assert before == after
    return result

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'bootstrap':
        target = OWN / 'controls'
        target.mkdir(exist_ok=False)
        result = capture('01_control_copy', ['cp', '-p'] + [str(p) for p in CONTROL.values()] + [str(target)], CONTROL.values())
        assert result.returncode == 0
        roles = []
        for name, original in CONTROL.items():
            copy = target / name
            assert digest(copy) == digest(original)
            roles.append(dict(original_path=str(original), copy_path=str(copy), sha256=digest(copy),
                              role='exact_physical_copy_before_body_read'))
        save(OWN / 'CONTROL_ROLES.json', roles)
    elif mode == 'controls':
        paths = [OWN / 'controls' / n for n in CONTROL]
        capture('02_control_key_search', ['rg', '-n', 'HVD|NCC|NED|ORR|CTM|GCF|Current|Status|当前', '--'] + [str(p) for p in paths], paths)
    elif mode == 'read':
        label = sys.argv[2]
        paths = [ROOT / p for p in sys.argv[3:]]
        capture(label, ['sed', '-n', '1,4000p'] + [str(p) for p in paths], paths)
    elif mode == 'seal':
        target = OWN / 'SHA256SUMS'
        assert not target.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(nonself_payloads=len(paths), sha256=digest(target))))
    else:
        raise SystemExit('bad mode')
