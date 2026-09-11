#!/usr/bin/env python3
"""Read-only exact-baseline/capacity diagnostics. Only writes this preparation."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import time

HERE = Path(__file__).resolve().parent
SOURCE = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
DEST = Path('/root/symbolic-dynamics-private-sync-20260907')
BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'


def dump(path, obj):
    with path.open('x') as f:
        json.dump(obj, f, sort_keys=True, indent=2)
        f.write('\n')


def main():
    out = HERE / 'diagnostics_01'
    out.mkdir()
    commands = []
    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0',
               GIT_SSH_COMMAND='ssh -o BatchMode=yes -o ConnectTimeout=20 -o ConnectionAttempts=1')

    def run(argv, allowed=(0,)):
        stem = out / ('command_%03d' % (len(commands) + 1))
        start = time.time()
        p = subprocess.run(argv, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=50)
        stem.with_suffix('.stdout.raw').write_bytes(p.stdout)
        stem.with_suffix('.stderr.raw').write_bytes(p.stderr)
        rec = {'argv': argv, 'cwd': str(SOURCE), 'start_epoch': start, 'end_epoch': time.time(),
               'exit': p.returncode, 'stdout_bytes': len(p.stdout), 'stderr_bytes': len(p.stderr),
               'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(),
               'stderr_sha256': hashlib.sha256(p.stderr).hexdigest(),
               'environment_overrides_only': {k: env[k] for k in ('GIT_OPTIONAL_LOCKS', 'GIT_TERMINAL_PROMPT', 'GIT_SSH_COMMAND')}}
        dump(stem.with_suffix('.actual.json'), rec)
        commands.append(rec)
        assert p.returncode in allowed, (argv, p.returncode)
        return p.stdout

    def git(*args):
        return run(['git', '-C', str(MIRROR), *args])

    run(['df', '-B1', '--output=source,fstype,size,used,avail,pcent,target', '/root', str(SOURCE), str(MIRROR)])
    run(['stat', '-f', '-c', '%T %S %b %a %n', '/root', str(SOURCE), str(MIRROR)])
    head = git('rev-parse', 'HEAD').decode().strip()
    tree = git('rev-parse', 'HEAD^{tree}').decode().strip()
    branch = git('symbolic-ref', '--short', 'HEAD').decode().strip()
    refs = git('show-ref', '--heads', '--tags')
    tracking = git('rev-parse', 'refs/remotes/origin/main').decode().strip()
    status = git('status', '--porcelain=v1', '-z', '--untracked-files=all')
    divergence = git('rev-list', '--left-right', '--count', 'HEAD...origin/main').decode().strip()
    remote = git('ls-remote', '--exit-code', 'origin', 'refs/heads/main').decode().strip()
    run(['du', '-sb', str(MIRROR / '.git'), str(SOURCE / 'docs/papers204_208_sequence/qa/p209_completion_private_checkpoint')])
    inventory = git('ls-tree', '-r', '-z', '--full-tree', BASE, '--', 'docs/papers204_208_sequence', 'papers/210-weakly-increasing-run-aggregation', 'SYMBOLIC_DYNAMICS_STATE.md')
    assert head == tracking == remote.split()[0] == BASE
    assert not status and divergence.split() == ['0', '0'] and branch == 'main'
    assert not DEST.exists() and not DEST.is_symlink()
    assert Path('/root').stat().st_dev != SOURCE.stat().st_dev
    summary = {'status': 'READ_ONLY_DIAGNOSTICS_PASS_NO_SYNC_EXECUTION', 'baseline': head, 'tree': tree,
               'branch': branch, 'remote_ref': remote.split()[1], 'remote_sha': remote.split()[0],
               'clean': True, 'divergence': [0, 0], 'source': str(SOURCE), 'original_mirror': str(MIRROR),
               'proposed_supplementary_clone': str(DEST), 'destination_absent': True,
               'source_device': SOURCE.stat().st_dev, 'destination_parent_device': Path('/root').stat().st_dev,
               'destination_parent_free_bytes': os.statvfs('/root').f_bavail * os.statvfs('/root').f_frsize,
               'source_free_bytes': os.statvfs(SOURCE).f_bavail * os.statvfs(SOURCE).f_frsize,
               'git_ls_tree_record': 'command_012.stdout.raw', 'commands': len(commands),
               'git_sync_log_file': 'Not found by filename in either data root; use GIT_SYNC_RECEIPT.md and actual accepted prior executor path mapping.'}
    dump(out / 'RESULT.actual.json', summary)
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    main()
