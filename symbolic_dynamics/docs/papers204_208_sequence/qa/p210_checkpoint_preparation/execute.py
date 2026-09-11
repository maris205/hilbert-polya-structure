#!/usr/bin/env python3
"""UNEXECUTED proposal. Every phase needs an exact, externally authored approval.

Only the overlay clone and overlay evidence directory are mutation targets.
The original mirror and source tree are read-only. Failures are single-use
receipts; there is no retry, delete, reset, force push or automatic merge.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import time
import traceback

HERE = Path(__file__).resolve().parent
PREP = HERE / 'preparation_01'
SOURCE = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
DEST = Path('/root/symbolic-dynamics-private-sync-20260907')
EVIDENCE = Path('/root/symbolic-dynamics-private-sync-evidence-20260907')
BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
PHASES = ('preflight', 'clone', 'copy', 'stage', 'commit', 'push')
ENV = dict(os.environ, GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0',
           GIT_SSH_COMMAND='ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=20 -o ConnectionAttempts=1',
           GIT_LITERAL_PATHSPECS='0')


def dump(path, obj):
    with path.open('x') as f:
        json.dump(obj, f, sort_keys=True, indent=2)
        f.write('\n')


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def pin(path):
    assert path.is_file() and not path.is_symlink(), str(path)
    size = path.stat().st_size
    h, g = hashlib.sha256(), hashlib.sha1(b'blob ' + str(size).encode() + b'\0')
    count = 0
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
            g.update(b)
            count += len(b)
    assert count == size == path.stat().st_size
    return {'bytes': size, 'sha256': h.hexdigest(), 'git_blob_sha1': g.hexdigest(),
            'mode': '100755' if path.stat().st_mode & 0o111 else '100644'}


def check_file(base, row):
    name = row['path']
    assert not name.startswith(('/', ':')) and '..' not in Path(name).parts
    assert not any(c in name for c in '\0\r\n\t')
    path = base / name
    assert path.resolve().is_relative_to(base.resolve()), name
    assert pin(path) == {k: row[k] for k in ('bytes', 'sha256', 'git_blob_sha1', 'mode')}, name


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase', choices=PHASES)
    ap.add_argument('--approval', required=True, type=Path)
    args = ap.parse_args()
    # A -C argument must never be redirected by an inherited Git environment.
    # Only variable names are mentioned on refusal, never their values.
    redirect_keys = ('GIT_DIR','GIT_WORK_TREE','GIT_COMMON_DIR','GIT_INDEX_FILE',
                     'GIT_OBJECT_DIRECTORY','GIT_ALTERNATE_OBJECT_DIRECTORIES',
                     'GIT_CONFIG','GIT_CONFIG_COUNT','GIT_CONFIG_PARAMETERS','GIT_NAMESPACE')
    assert not [k for k in redirect_keys if os.environ.get(k)], 'inherited Git redirection requires root inspection'
    # A placeholder/template never authorizes execution; root must supply exact pins.
    approval = json.loads(args.approval.read_text())
    scope = json.loads((PREP / 'SCOPE.json').read_text())
    assert approval['status'] == 'ROOT_APPROVED_EXACT_P210_ROUND0_OVERLAY_CHECKPOINT'
    assert approval['scope_sha256'] == digest(PREP / 'SCOPE.json')
    assert approval['executor_sha256'] == digest(Path(__file__))
    assert approval['supplementary_clone'] == str(DEST)
    assert approval['overlay_execution_evidence'] == str(EVIDENCE)
    assert approval['approved_phases'] == list(PHASES)
    assert approval['allow_exact_ignored_paths'] == scope['ignored_selected_paths']
    assert approval['allow_original_mirror_alternates_readonly'] is True
    assert approval['allow_readonly_original_config_include'] is True
    assert approval['allow_two_unique_blob_lossless_gzip_captures'] is True
    assert scope['baseline'] == BASE
    assert scope['selected_json_sha256'] == digest(PREP / 'SELECTED_PATHS.json')
    assert scope['expected_json_sha256'] == digest(PREP / 'EXPECTED_BLOBS.json')
    selected = json.loads((PREP / 'SELECTED_PATHS.json').read_text())
    expected = json.loads((PREP / 'EXPECTED_BLOBS.json').read_text())
    selected_names = {r['path'] for r in selected}
    assert len(selected_names) == scope['selected_count'] == len(selected)
    assert len(expected) == scope['expected_blob_count']
    assert not any(p.startswith(x) for p in selected_names for x in scope['excluded_prefixes'])
    assert EVIDENCE.parent == DEST.parent == Path('/root')
    assert SOURCE.stat().st_dev != Path('/root').stat().st_dev
    assert not DEST.is_symlink() and not EVIDENCE.is_symlink()
    if args.phase == 'preflight':
        assert not DEST.exists() and not EVIDENCE.exists()
        EVIDENCE.mkdir()
        (EVIDENCE / 'empty_hooks').mkdir()
        (EVIDENCE / 'empty_template').mkdir()
    else:
        previous = PHASES[PHASES.index(args.phase) - 1]
        prev = json.loads((EVIDENCE / previous / 'RESULT.actual.json').read_text())
        assert prev['status'] == 'PASS' and prev['scope_sha256'] == approval['scope_sha256']
        assert prev['executor_sha256'] == approval['executor_sha256']
    phase = EVIDENCE / args.phase
    phase.mkdir()
    commands = []
    dump(phase / 'APPROVAL_BINDING.actual.json', {'approval_path': str(args.approval.resolve()),
          'approval_sha256': digest(args.approval), 'approval': approval})

    def command(argv, stdin=None, allowed=(0,), timeout=60):
        stem = phase / ('command_%03d' % (len(commands) + 1))
        if stdin is not None:
            stem.with_suffix('.stdin.raw').write_bytes(stdin)
        start = time.time()
        with stem.with_suffix('.stdout.raw').open('xb') as out, stem.with_suffix('.stderr.raw').open('xb') as err:
            try:
                p = subprocess.run(argv, input=stdin, stdout=out, stderr=err, env=ENV, timeout=timeout)
                code = p.returncode
            except subprocess.TimeoutExpired:
                code = 'TIMEOUT'
        rec = {'argv': argv, 'cwd': str(SOURCE), 'started_epoch': start, 'ended_epoch': time.time(),
               'exit': code, 'environment_overrides_only': {k: ENV[k] for k in ('GIT_OPTIONAL_LOCKS','GIT_TERMINAL_PROMPT','GIT_SSH_COMMAND','GIT_LITERAL_PATHSPECS')},
               'stdout': {'path': stem.with_suffix('.stdout.raw').name, 'sha256': digest(stem.with_suffix('.stdout.raw'))},
               'stderr': {'path': stem.with_suffix('.stderr.raw').name, 'sha256': digest(stem.with_suffix('.stderr.raw'))}}
        dump(stem.with_suffix('.actual.json'), rec)
        commands.append(rec)
        assert code in allowed, (stem.name, code)
        return stem.with_suffix('.stdout.raw').read_bytes()

    def git(repo, *argv, **kwargs):
        # The private origin is resolved in memory by Git from the unchanged
        # original config. No remote URL/credential is copied into argv or output.
        options = []
        if repo == DEST:
            options = ['-c', 'include.path=' + str(MIRROR / '.git/config'),
                       '-c', 'core.worktree=' + str(DEST), '-c', 'core.bare=false',
                       '-c', 'core.hooksPath=' + str(EVIDENCE / 'empty_hooks'),
                       '-c', 'core.fsmonitor=false', '-c', 'gc.auto=0',
                       '-c', 'commit.gpgSign=false', '-c', 'core.autocrlf=false']
        return command(['git', '-C', str(repo), *options, *argv], **kwargs)

    def remote(repo, ref=BASE):
        data = git(repo, 'ls-remote', '--exit-code', 'origin', 'refs/heads/main')
        assert data.decode().split() == [ref, 'refs/heads/main'], 'remote changed: root must inspect overlap; no automatic merge'

    def baseline_unchanged():
        assert git(MIRROR, 'rev-parse', 'HEAD').decode().strip() == BASE
        assert git(MIRROR, 'rev-parse', 'refs/remotes/origin/main').decode().strip() == BASE
        assert not git(MIRROR, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
        assert git(MIRROR, 'rev-list', '--left-right', '--count', 'HEAD...origin/main').split() == [b'0', b'0']
        current = {'config': digest(MIRROR / '.git/config'),
                   'refs': hashlib.sha256(git(MIRROR, 'show-ref')).hexdigest()}
        binding = EVIDENCE / 'preflight/ORIGINAL_MIRROR_BINDING.json'
        if args.phase == 'preflight' and not binding.exists():
            dump(binding, current)
        else:
            assert current == json.loads(binding.read_text())

    def all_source_pins():
        for row in expected:
            check_file(SOURCE, row)
        for package in scope['packages']:
            base = package['base']
            names = {r['path'] for r in expected if r['path'].startswith(base + '/')}
            physical = {p.relative_to(SOURCE).as_posix() for p in (SOURCE / base).rglob('*') if p.is_file()}
            assert physical == names, ('package gained/lost source path', base)

    def overlay_files():
        for row in selected:
            check_file(DEST, row)
        physical = {p.relative_to(DEST).as_posix() for p in DEST.rglob('*') if p.is_file() and '.git' not in p.relative_to(DEST).parts}
        assert physical == selected_names, 'only explicit selected worktree paths may be materialized'

    def tree_check(tree):
        prefixes = [p['base'] for p in scope['packages']] + scope['exact_extra_paths']
        data = git(DEST, '--literal-pathspecs', 'ls-tree', '-r', '-z', '--full-tree', tree, '--', *prefixes)
        got = {}
        for row in data.split(b'\0'):
            if row:
                fields, name = row.split(b'\t', 1)
                mode, kind, oid = fields.decode().split()
                assert kind == 'blob'
                got[name.decode()] = (mode, oid)
        assert got == {r['path']: (r['mode'], r['git_blob_sha1']) for r in expected}, 'complete named tree path/mode/blob coverage'

    def blob_stream_check():
        # One payload per unique object. Every expected path is independently
        # mapped to that actual object by tree_check; duplicate paths do not
        # trigger duplicate multi-gigabyte native streams.
        unique = {}
        for r in expected:
            if r['git_blob_sha1'] in unique:
                old = unique[r['git_blob_sha1']]
                assert (old['sha256'], old['bytes']) == (r['sha256'], r['bytes'])
            unique[r['git_blob_sha1']] = r
        stem = phase / ('command_%03d' % (len(commands) + 1))
        stdin = b''.join((oid + '\n').encode() for oid in sorted(unique))
        stem.with_suffix('.stdin.raw').write_bytes(stdin)
        argv = ['git', '-C', str(DEST), 'cat-file', '--batch']
        start, stream_size, payload_size = time.time(), 0, 0
        stream_sha = hashlib.sha256()
        result_rows = []
        native_code = None
        try:
            with stem.with_suffix('.stdin.raw').open('rb') as inp, stem.with_suffix('.stderr.raw').open('xb') as err, stem.with_suffix('.stdout.raw.gz').open('xb') as raw:
                with gzip.GzipFile(filename='', mode='wb', fileobj=raw, compresslevel=1, mtime=0) as zipped:
                    p = subprocess.Popen(argv, stdin=inp, stdout=subprocess.PIPE, stderr=err, env=ENV)
                    def capture(b):
                        nonlocal stream_size
                        stream_size += len(b)
                        stream_sha.update(b)
                        zipped.write(b)
                    try:
                        for oid in sorted(unique):
                            row = unique[oid]
                            header = p.stdout.readline()
                            capture(header)
                            assert header == (oid + ' blob ' + str(row['bytes']) + '\n').encode(), oid
                            h = hashlib.sha256()
                            g = hashlib.sha1(b'blob ' + str(row['bytes']).encode() + b'\0')
                            remaining = row['bytes']
                            while remaining:
                                block = p.stdout.read(min(remaining, 1024 * 1024))
                                assert block, ('short object', oid)
                                capture(block)
                                h.update(block)
                                g.update(block)
                                remaining -= len(block)
                            end = p.stdout.read(1)
                            capture(end)
                            assert end == b'\n' and h.hexdigest() == row['sha256'] and g.hexdigest() == oid
                            payload_size += row['bytes']
                            result_rows.append({'git_blob_sha1': oid, 'bytes': row['bytes'], 'sha256': h.hexdigest()})
                        extra = p.stdout.read()
                        capture(extra)
                        assert not extra
                        native_code = p.wait(timeout=30)
                    finally:
                        if p.poll() is None:
                            p.terminate()
                            p.wait(timeout=30)
                        if native_code is None:
                            native_code = p.returncode
        finally:
            rec = {'argv': argv, 'started_epoch': start, 'ended_epoch': time.time(), 'exit': native_code,
                   'stdin_sha256': hashlib.sha256(stdin).hexdigest(),
                   'stdout_lossless_gzip': stem.with_suffix('.stdout.raw.gz').name,
                   'raw_stream_bytes': stream_size, 'raw_stream_sha256': stream_sha.hexdigest(),
                   'gzip_bytes': stem.with_suffix('.stdout.raw.gz').stat().st_size,
                   'gzip_sha256': digest(stem.with_suffix('.stdout.raw.gz')),
                   'stderr_sha256': digest(stem.with_suffix('.stderr.raw')),
                   'unique_blob_count': len(result_rows), 'verified_payload_bytes': payload_size}
            dump(stem.with_suffix('.actual.json'), rec)
            commands.append(rec)
        assert native_code == 0 and not stem.with_suffix('.stderr.raw').read_bytes()
        # Prove the retained gzip is lossless by a separate streaming reread.
        h, n = hashlib.sha256(), 0
        with gzip.open(stem.with_suffix('.stdout.raw.gz'), 'rb') as f:
            for block in iter(lambda: f.read(1024 * 1024), b''):
                h.update(block)
                n += len(block)
        assert n == stream_size and h.hexdigest() == stream_sha.hexdigest()
        dump(phase / 'BLOB_KEYS.actual.json', result_rows)
        return rec

    result = {'status': 'PASS', 'phase': args.phase, 'scope_sha256': approval['scope_sha256'],
              'executor_sha256': approval['executor_sha256'], 'baseline': BASE}
    try:
        baseline_unchanged()
        all_source_pins()
        free = shutil.disk_usage('/root').free
        if args.phase in ('preflight', 'clone'):
            assert free > scope['conservative_overlay_storage_budget_bytes'], ('overlay capacity', free)
        if args.phase == 'preflight':
            remote(MIRROR)
            # Strict read-only remote configuration checks output only names,
            # never URL/token values. The actual private origin stays in Git config.
            run_config = git(MIRROR, 'config', '--name-only', '--get-regexp', r'^remote\.origin\.(url|pushurl)$')
            assert run_config.splitlines() == [b'remote.origin.url'], 'explicit root review required for multiple/pushurl origins'
            result.update(selected_count=len(selected), selected_bytes=scope['selected_source_bytes'], overlay_free_bytes=free)
        elif args.phase == 'clone':
            assert not DEST.exists()
            git(MIRROR, 'clone', '--shared', '--no-checkout', '--origin', 'source-mirror',
                '--template=' + str(EVIDENCE / 'empty_template'), str(MIRROR), str(DEST))
            alternate = DEST / '.git/objects/info/alternates'
            assert alternate.read_text().strip() == str(MIRROR / '.git/objects')
            assert git(DEST, 'rev-parse', 'HEAD').decode().strip() == BASE
            git(DEST, 'read-tree', BASE)
            tracked = git(DEST, 'ls-files', '-z')
            git(DEST, 'update-index', '--skip-worktree', '-z', '--stdin', stdin=tracked)
            present = b''.join(r['path'].encode() + b'\0' for r in selected if r['baseline'] is not None)
            git(DEST, 'update-index', '--no-skip-worktree', '-z', '--stdin', stdin=present)
            git(DEST, 'fetch', '--no-tags', 'origin', 'refs/heads/main:refs/remotes/origin/main', timeout=60)
            assert git(DEST, 'rev-parse', 'origin/main').decode().strip() == BASE
            remote(DEST)
            result['sparse_mechanism'] = 'no checkout; full base index, skip-worktree on every unselected baseline path'
        elif args.phase == 'copy':
            # Before any selected materialization, freeze exact pinned controls
            # on overlay. No current control is edited or read by a moving name.
            snapshots = phase / 'source_control_snapshot'
            snapshots.mkdir()
            for row in scope['mutable_controls_pinned_but_not_physically_copied']:
                target = snapshots / row['path']
                target.parent.mkdir(parents=True, exist_ok=True)
                with (SOURCE / row['path']).open('rb') as src, target.open('xb') as dst:
                    shutil.copyfileobj(src, dst, 1024 * 1024)
                target.chmod(0o755 if row['mode'] == '100755' else 0o644)
                check_file(snapshots, row)
            for row in selected:
                target = DEST / row['path']
                assert not target.exists() and not target.is_symlink(), ('no overwrite', str(target))
                target.parent.mkdir(parents=True, exist_ok=True)
                from_base = snapshots if row['path'] in {c['path'] for c in scope['mutable_controls_pinned_but_not_physically_copied']} else SOURCE
                with (from_base / row['path']).open('rb') as src, target.open('xb') as dst:
                    shutil.copyfileobj(src, dst, 1024 * 1024)
                target.chmod(0o755 if row['mode'] == '100755' else 0o644)
            all_source_pins()
            overlay_files()
            result['copied_count'] = len(selected)
        elif args.phase == 'stage':
            overlay_files()
            data = b''.join(p.encode() + b'\0' for p in sorted(selected_names))
            attrs = git(DEST, 'check-attr', '--cached', '-z', '--stdin', 'filter','text','eol','working-tree-encoding','ident', stdin=data)
            fields = attrs.split(b'\0')[:-1]
            assert len(fields) == 15 * len(selected) and all(fields[i] in (b'unspecified', b'unset') for i in range(2,len(fields),3))
            ignored = set(scope['ignored_selected_paths'])
            ordinary = b''.join(p.encode()+b'\0' for p in sorted(selected_names-ignored))
            exact_ignored = b''.join(p.encode()+b'\0' for p in sorted(ignored))
            git(DEST, '--literal-pathspecs', 'add', '--pathspec-from-file=-', '--pathspec-file-nul', stdin=ordinary)
            git(DEST, '--literal-pathspecs', 'add', '-f', '--pathspec-from-file=-', '--pathspec-file-nul', stdin=exact_ignored)
            changed = git(DEST, 'diff', '--cached', '--name-status', '-z', '--no-renames', BASE, '--').split(b'\0')[:-1]
            assert len(changed) == 2 * len(selected)
            assert {changed[i+1].decode(): changed[i].decode() for i in range(0,len(changed),2)} == {r['path']:r['change'] for r in selected}
            tree = git(DEST, 'write-tree').decode().strip()
            tree_check(tree)
            result.update(tree=tree, object_stream=blob_stream_check())
        elif args.phase == 'commit':
            overlay_files()
            stage = json.loads((EVIDENCE / 'stage/RESULT.actual.json').read_text())
            assert git(DEST, 'write-tree').decode().strip() == stage['tree']
            tree_check(stage['tree'])
            git(DEST, 'commit', '-m', 'Private checkpoint: P210 Round0 and accepted batch evidence; HOLD_EXTERNAL', timeout=60)
            commit = git(DEST, 'rev-parse', 'HEAD').decode().strip()
            assert git(DEST, 'rev-list', '--parents', '-n', '1', 'HEAD').decode().split() == [commit, BASE]
            assert git(DEST, 'rev-parse', 'HEAD^{tree}').decode().strip() == stage['tree']
            tree_check(commit)
            result.update(commit=commit, tree=stage['tree'], object_stream=blob_stream_check())
            assert not git(DEST, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
        elif args.phase == 'push':
            overlay_files()
            committed = json.loads((EVIDENCE / 'commit/RESULT.actual.json').read_text())
            commit = committed['commit']
            assert git(DEST, 'rev-parse', 'HEAD').decode().strip() == commit
            assert not git(DEST, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
            tree_check(commit)
            remote(DEST)
            git(DEST, 'push', 'origin', commit + ':refs/heads/main', timeout=60)
            remote(DEST, commit)
            git(DEST, 'fetch', '--no-tags', 'origin', 'refs/heads/main:refs/remotes/origin/main', timeout=60)
            assert git(DEST, 'rev-list', '--left-right', '--count', 'HEAD...origin/main').split() == [b'0',b'0']
            assert not git(DEST, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
            result.update(commit=commit, tree=committed['tree'], actual_remote_confirmed=True,
                          divergence=[0,0], original_mirror_intentionally_still_at=BASE)
        baseline_unchanged()
        result['commands'] = len(commands)
        dump(phase / 'RESULT.actual.json', result)
        print(json.dumps({k:v for k,v in result.items() if k != 'object_stream'}, sort_keys=True))
    except BaseException:
        dump(phase / 'FAILURE.actual.json', {'phase': args.phase, 'scope_sha256': approval['scope_sha256'],
             'executor_sha256': approval['executor_sha256'], 'completed_commands': len(commands),
             'exception': traceback.format_exc(), 'no_automatic_retry_or_cleanup': True})
        raise


if __name__ == '__main__':
    main()
