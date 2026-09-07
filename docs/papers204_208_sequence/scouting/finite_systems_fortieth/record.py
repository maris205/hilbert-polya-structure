#!/usr/bin/env python3
"""Small native documentary recorder, with explicit declared file inputs."""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
import time

OWN = pathlib.Path(__file__).absolute().parent
ROOT = OWN.parents[3]


def metadata(path):
    body = path.read_bytes()
    return dict(sha256=hashlib.sha256(body).hexdigest(), bytes=len(body))


def save(path, value):
    with path.open('x') as stream:
        stream.write(json.dumps(value, indent=2, sort_keys=True) + '\n')


def allowed(path):
    if path.is_relative_to(OWN):
        return True
    if path == pathlib.Path(sys.executable).resolve():
        return True
    if not path.is_relative_to(ROOT):
        return str(path) in {
            '/root/autodl-tmp/.codex/skills/research-lit/SKILL.md',
            '/root/autodl-tmp/.codex/skills/idea-creator/SKILL.md',
            '/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md'}
    for part in path.relative_to(ROOT).parts:
        s = part.lower()
        if s in {'qa', 'qa_final', 'review', 'reviews', 'freeze', 'build', 'builds',
                 'finite_systems_tenth', 'finite_systems_nineteenth', 'finite_systems_twentieth'}:
            return False
        if s.startswith(('208-', '209-', 'p208', 'p209', 'ofs', 'fth', 'lnr', 'ned', 'orr',
                         'frozen_', 'capsule')) or 'gate' in s:
            return False
    return True


def main():
    split = sys.argv.index('--')
    parser = argparse.ArgumentParser()
    parser.add_argument('label')
    parser.add_argument('--input', action='append', default=[])
    parser.add_argument('--role', default='native_documentary_command_declared_inputs_not_runtime_inventory')
    args = parser.parse_args(sys.argv[1:split])
    argv = sys.argv[split + 1:]
    assert argv
    inputs = sorted(set([pathlib.Path(__file__).absolute(), pathlib.Path(sys.executable).resolve()]
                        + [pathlib.Path(p).absolute() for p in args.input]))
    for path in inputs:
        assert path.is_file() and not path.is_symlink() and allowed(path), str(path)
    folder = OWN / 'commands' / args.label
    folder.mkdir(parents=True, exist_ok=False)
    before = {str(p): metadata(p) for p in inputs}
    save(folder / 'inputs_before.json', before)
    started = time.time()
    save(folder / 'attempt.json', dict(argv=argv, cwd=str(ROOT), role=args.role,
                                      started_epoch=started, timeout_seconds=60))
    try:
        result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                timeout=60, check=False)
        code, out, err, timeout = result.returncode, result.stdout, result.stderr, False
    except subprocess.TimeoutExpired as ex:
        code, out, err, timeout = 124, ex.stdout or b'', ex.stderr or b'', True
    for name, body in [('stdout.raw', out), ('stderr.raw', err)]:
        with (folder / name).open('xb') as stream:
            stream.write(body)
    after = {str(p): metadata(p) for p in inputs}
    save(folder / 'inputs_after.json', after)
    receipt = dict(argv=argv, cwd=str(ROOT), role=args.role, exit=code,
                   started_epoch=started, finished_epoch=time.time(), timed_out=timeout,
                   input_count=len(before), unchanged=before == after,
                   stdout=metadata(folder / 'stdout.raw'), stderr=metadata(folder / 'stderr.raw'))
    save(folder / 'receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    assert before == after, 'declared input changed during command'
    raise SystemExit(code)


if __name__ == '__main__':
    main()
