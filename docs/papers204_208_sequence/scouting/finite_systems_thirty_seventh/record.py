#!/usr/bin/env python3
"""Small native documentary recorder; no general runtime inventory."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
OWN = pathlib.Path(__file__).absolute().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as stream:
        stream.write(json.dumps(value, indent=2, sort_keys=True) + '\n')


def allowed(path):
    if path.is_relative_to(OWN):
        return True
    if not path.is_relative_to(ROOT):
        return str(path) in {
            '/root/autodl-tmp/.codex/skills/research-lit/SKILL.md',
            '/root/autodl-tmp/.codex/skills/idea-creator/SKILL.md',
            '/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md'}
    for part in path.relative_to(ROOT).parts:
        key = part.lower()
        if key in {'qa', 'qa_final', 'review', 'reviews', 'freeze', 'build', 'builds',
                   'finite_systems_tenth', 'finite_systems_nineteenth', 'finite_systems_twentieth'}:
            return False
        if 'gate' in key or key.startswith(('208-', '209-', 'p208', 'p209', 'ofs', 'fth', 'frozen_', 'capsule')):
            return False
    return True


def capture(label, argv, inputs, cwd=ROOT):
    folder = OWN / 'commands' / label
    folder.mkdir(parents=True, exist_ok=False)
    paths = sorted(set([pathlib.Path(__file__).absolute()] + list(inputs)))
    for p in paths:
        assert p.is_file() and not p.is_symlink() and allowed(p), str(p)
    before = {str(p): digest(p) for p in paths}
    save(folder / 'inputs_before.json', before)
    started = time.time()
    result = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    for name, body in [('stdout.raw', result.stdout), ('stderr.raw', result.stderr)]:
        with (folder / name).open('xb') as stream:
            stream.write(body)
    after = {str(p): digest(p) for p in paths}
    save(folder / 'inputs_after.json', after)
    receipt = dict(argv=argv, cwd=str(cwd), exit=result.returncode, started_epoch=started,
                   finished_epoch=time.time(), input_count=len(before), unchanged=before == after,
                   stdout_sha256=digest(folder / 'stdout.raw'), stderr_sha256=digest(folder / 'stderr.raw'),
                   role='native_documentary_command_not_candidate_scientific_execution')
    save(folder / 'receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    assert before == after
    return result


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'controls':
        paths = [ROOT / 'SYMBOLIC_DYNAMICS_STATE.md', ROOT / 'docs/papers204_208_sequence/PIPELINE_STATE.md',
                 ROOT / 'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md']
        target = OWN / 'controls'
        target.mkdir(exist_ok=False)
        result = capture('01_control_copy', ['cp', '-p'] + [str(p) for p in paths] + [str(target)], paths)
        assert result.returncode == 0
        rows = []
        for p in paths:
            q = target / p.name
            assert p.read_bytes() == q.read_bytes()
            rows.append(dict(original_path=str(p), copy_path=str(q), sha256=digest(q), role='exact_control_copy_before_recorded_body_search'))
        save(OWN / 'CONTROL_ROLES.json', rows)
    elif mode == 'read':
        paths = [pathlib.Path(p).absolute() for p in sys.argv[3:]]
        result = capture(sys.argv[2], ['sed', '-n', '1,4000p'] + [str(p) for p in paths], paths)
        assert result.returncode == 0
    elif mode == 'search':
        paths = [pathlib.Path(p).absolute() for p in sys.argv[4:]]
        result = capture(sys.argv[2], ['rg', '-n', sys.argv[3], '--'] + [str(p) for p in paths], paths)
        assert result.returncode in (0, 1)
    else:
        raise SystemExit('unknown documentary mode')
