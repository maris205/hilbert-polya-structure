#!/usr/bin/env python3
"""UNEXECUTED identity-only commit/push continuation from accepted staged tree.

Existing configured user identity is reused command-locally; no config write.
Both failed attempts and accepted stage_revision_01 remain immutable.
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
ORIGINAL = HERE.parent / 'p210_checkpoint_preparation'
STAGE_REVISION = HERE.parent / 'p210_checkpoint_stage_revision_01'
PREP = ORIGINAL / 'preparation_01'
SOURCE = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
DEST = Path('/root/symbolic-dynamics-private-sync-20260907')
EVIDENCE = Path('/root/symbolic-dynamics-private-sync-evidence-20260907')
BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
PHASES = ('commit', 'push')
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
                     'GIT_CONFIG','GIT_CONFIG_COUNT','GIT_CONFIG_PARAMETERS','GIT_NAMESPACE',
                     'GIT_AUTHOR_NAME','GIT_AUTHOR_EMAIL','GIT_COMMITTER_NAME','GIT_COMMITTER_EMAIL')
    assert not [k for k in redirect_keys if os.environ.get(k)], 'inherited Git redirection requires root inspection'
    # A placeholder/template never authorizes execution; root must supply exact pins.
    approval = json.loads(args.approval.read_text())
    scope = json.loads((PREP / 'SCOPE.json').read_text())
    assert approval['status'] == 'ROOT_APPROVED_P210_IDENTITY_REVISION_01_CONTINUATION'
    assert approval['commit_identity'] == {'user.name':'mariswang','user.email':'wangliang.f@gmail.com'}
    assert approval['identity_read_sha256'] == digest(HERE.parent / 'P210_CHECKPOINT_EXISTING_IDENTITY_ROOT_READ.actual.json')
    assert approval['identity_input_pins_sha256'] == digest(HERE / 'IDENTITY_INPUT_PINS.json')
    assert approval['accepted_stage_executor_sha256'] == digest(STAGE_REVISION / 'execute.py') == '497db8a936d1080523f9407799d3f9e094275ec18557c30f4307cf4c0babc1f8'
    assert approval['accepted_stage_tree'] == 'a26e19ee04c7a25fd0b0d00c67df784206baba4c'
    assert approval['process_support_sha256'] == digest(HERE / 'process_support.py')
    from process_support import run_files, TimedReader, settle_group, existing_overlay_writers
    assert approval['inspection_sha256'] == digest(STAGE_REVISION / 'inspection_01/RESULT.actual.json')
    assert approval['residue_pins_sha256'] == digest(STAGE_REVISION / 'FAILED_RESIDUE_PINS.actual.json')
    assert approval['prior_executor_sha256'] == digest(ORIGINAL / 'execute.py') == '8d42285eeebcfc23c145da9b0bf6bb8b82b2db1f04533f5d73c145665f4cdcba'
    assert approval['allow_owned_new_session_timeout_settlement'] is True
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
    assert DEST.is_dir() and EVIDENCE.is_dir()
    assert not existing_overlay_writers(DEST), 'existing overlay Git writer requires root inspection'
    assert not (DEST / '.git/index.lock').exists(), 'root must separately preserve the exact stale lock; no cleanup here'
    lock_receipt_path = Path(approval['lock_preservation_receipt'])
    assert lock_receipt_path == EVIDENCE / 'stage_revision_01_lock_preservation/ROOT_PRESERVATION.actual.json'
    assert digest(lock_receipt_path) == approval['lock_preservation_receipt_sha256']
    assert approval['lock_preservation_receipt_sha256'] == '208b59678887f7741403dc3110d0585f10b730ceca94788203d3bc92403fa00e'
    lock_receipt = json.loads(lock_receipt_path.read_text())
    residues = json.loads((STAGE_REVISION / 'FAILED_RESIDUE_PINS.actual.json').read_text())
    assert lock_receipt['status'] == 'ROOT_CONFIRMED_EXACT_ORPHAN_LOCK_PRESERVATION'
    assert lock_receipt['source'] == residues['pins'][0]['path']
    assert lock_receipt['preserved_path'] == residues['proposed_lock_archive']
    assert lock_receipt['source_pin'] == residues['pins'][0]
    assert lock_receipt['no_live_holders_immediately_before_move'] is True
    assert lock_receipt['actual_native_exit'] == 0 and lock_receipt['no_deleted_bytes'] is True
    preserved_lock = Path(lock_receipt['preserved_path'])
    assert preserved_lock.is_file() and not preserved_lock.is_symlink()
    assert digest(preserved_lock) == residues['pins'][0]['sha256']
    assert preserved_lock.stat().st_ino == residues['pins'][0]['inode']
    assert preserved_lock.stat().st_dev == residues['pins'][0]['device']
    assert preserved_lock.stat().st_size == residues['pins'][0]['bytes']
    assert preserved_lock.stat().st_mtime_ns == residues['pins'][0]['mtime_ns']
    assert preserved_lock.stat().st_mode == residues['pins'][0]['mode']
    if args.phase == 'commit':
        prev = json.loads((EVIDENCE / 'stage_revision_01/RESULT.actual.json').read_text())
        assert prev['executor_sha256'] == approval['accepted_stage_executor_sha256']
        assert prev['tree'] == approval['accepted_stage_tree']
        assert not (EVIDENCE / 'push_revision_01').exists()
    else:
        prev = json.loads((EVIDENCE / 'commit_revision_02/RESULT.actual.json').read_text())
        assert prev['executor_sha256'] == approval['executor_sha256']
    assert prev['status'] == 'PASS' and prev['scope_sha256'] == approval['scope_sha256']
    phase = EVIDENCE / (args.phase + '_revision_02')
    phase.mkdir()
    commands = []
    dump(phase / 'APPROVAL_BINDING.actual.json', {'approval_path': str(args.approval.resolve()),
          'approval_sha256': digest(args.approval), 'approval': approval})

    def command(argv, stdin=None, allowed=(0,), timeout=300):
        stem = phase / ('command_%03d' % (len(commands) + 1))
        # A physical stdin file avoids a blocked write-before-read pipe.
        inp = stem.with_suffix('.stdin.raw')
        inp.write_bytes(b'' if stdin is None else stdin)
        out, err = stem.with_suffix('.stdout.raw'), stem.with_suffix('.stderr.raw')
        try:
            native = run_files(argv, inp, out, err, ENV, timeout=timeout)
        except BaseException:
            rec = {'argv': argv, 'exit': 'RECORDER_FAILED_UNFINALIZED', 'stdout_path': out.name,
                   'stderr_path': err.name, 'output_hashes_not_finalized': True,
                   'exception': traceback.format_exc()}
            dump(stem.with_suffix('.actual.json'), rec)
            commands.append(rec)
            raise
        rec = {'argv': argv, 'cwd': str(SOURCE), **native,
               'environment_overrides_only': {k: ENV[k] for k in ('GIT_OPTIONAL_LOCKS','GIT_TERMINAL_PROMPT','GIT_SSH_COMMAND','GIT_LITERAL_PATHSPECS')},
               'stdin': {'path': inp.name, 'sha256': digest(inp)},
               'stdout': {'path': out.name, 'sha256': digest(out)},
               'stderr': {'path': err.name, 'sha256': digest(err)}}
        assert native['process_group_settlement']['quiescent']
        dump(stem.with_suffix('.actual.json'), rec)
        commands.append(rec)
        assert native['exit'] in allowed, (stem.name, native['exit'])
        return out.read_bytes()

    def git(repo, *argv, **kwargs):
        # The private origin is resolved in memory by Git from the unchanged
        # original config. No remote URL/credential is copied into argv or output.
        options = []
        if repo == DEST:
            options = ['-c', 'include.path=' + str(MIRROR / '.git/config'),
                       '-c', 'core.worktree=' + str(DEST), '-c', 'core.bare=false',
                       '-c', 'core.hooksPath=' + str(EVIDENCE / 'empty_hooks'),
                       '-c', 'core.fsmonitor=false', '-c', 'gc.auto=0',
                       '-c', 'commit.gpgSign=false', '-c', 'core.autocrlf=false',
                       '-c', 'user.name=mariswang', '-c', 'user.email=wangliang.f@gmail.com']
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

    def historical_failure_preserved():
        for row in json.loads((HERE / 'IDENTITY_INPUT_PINS.json').read_text()):
            assert digest(Path(row['path'])) == row['sha256'], row['path']
        for row in json.loads((STAGE_REVISION / 'inspection_01/ORIGINAL_INPUT_PINS.json').read_text()):
            assert digest(Path(row['path'])) == row['sha256'], row['path']
        for row in residues['pins'][1:]:
            p = Path(row['path'])
            assert p.is_file() and not p.is_symlink()
            assert p.stat().st_size == row['bytes'] and digest(p) == row['sha256'], row['path']
        assert digest(preserved_lock) == residues['pins'][0]['sha256']
        assert not (DEST / '.git/index.lock').exists()

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
        settlement = None
        try:
            with stem.with_suffix('.stdin.raw').open('rb') as inp, stem.with_suffix('.stderr.raw').open('xb') as err, stem.with_suffix('.stdout.raw.gz').open('xb') as raw:
                with gzip.GzipFile(filename='', mode='wb', fileobj=raw, compresslevel=1, mtime=0) as zipped:
                    p = subprocess.Popen(argv, stdin=inp, stdout=subprocess.PIPE, stderr=err, env=ENV, start_new_session=True)
                    reader = TimedReader(p.stdout, p.pid, timeout=300)
                    def capture(b):
                        nonlocal stream_size
                        stream_size += len(b)
                        stream_sha.update(b)
                        zipped.write(b)
                    try:
                        for oid in sorted(unique):
                            row = unique[oid]
                            header = reader.readline()
                            capture(header)
                            assert header == (oid + ' blob ' + str(row['bytes']) + '\n').encode(), oid
                            h = hashlib.sha256()
                            g = hashlib.sha1(b'blob ' + str(row['bytes']).encode() + b'\0')
                            remaining = row['bytes']
                            while remaining:
                                block = reader.read(min(remaining, 1024 * 1024))
                                assert block, ('short object', oid)
                                capture(block)
                                h.update(block)
                                g.update(block)
                                remaining -= len(block)
                            end = reader.read(1)
                            capture(end)
                            assert end == b'\n' and h.hexdigest() == row['sha256'] and g.hexdigest() == oid
                            payload_size += row['bytes']
                            result_rows.append({'git_blob_sha1': oid, 'bytes': row['bytes'], 'sha256': h.hexdigest()})
                        extra = reader.read()
                        capture(extra)
                        assert not extra
                        native_code = p.wait(timeout=30)
                    finally:
                        settlement = settle_group(p, terminate=native_code is None)
                        reader.close()
                        assert settlement['quiescent'], 'unfinished native writer: no final output hashing'
                        if native_code is None:
                            native_code = p.returncode
        finally:
            assert settlement is not None and settlement['quiescent'], 'native blob streams not quiescent; preserve raw files without final hashes'
            rec = {'argv': argv, 'started_epoch': start, 'ended_epoch': time.time(), 'exit': native_code,
                   'process_group_settlement': settlement, 'timeout_seconds': 300,
                   'stdin_sha256': hashlib.sha256(stdin).hexdigest(),
                   'stdout_lossless_gzip': stem.with_suffix('.stdout.raw.gz').name,
                   'raw_stream_bytes': stream_size, 'raw_stream_sha256': stream_sha.hexdigest(),
                   'gzip_bytes': stem.with_suffix('.stdout.raw.gz').stat().st_size,
                   'gzip_sha256': digest(stem.with_suffix('.stdout.raw.gz')),
                   'stderr_sha256': digest(stem.with_suffix('.stderr.raw')),
                   'unique_blob_count': len(result_rows), 'verified_payload_bytes': payload_size}
            dump(stem.with_suffix('.actual.json'), rec)
            commands.append(rec)
        assert native_code == 0 and not settlement['signals'] and not stem.with_suffix('.stderr.raw').read_bytes()
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
        historical_failure_preserved()
        free = shutil.disk_usage('/root').free
        assert free > 3 * 658584369 + 1024**3, ('remaining overlay reservation', free)
        if args.phase == 'commit':
            overlay_files()
            stage = json.loads((EVIDENCE / 'stage_revision_01/RESULT.actual.json').read_text())
            assert stage['tree'] == approval['accepted_stage_tree']
            assert not git(DEST, 'diff', '--cached', '--name-status', '-z', stage['tree'], '--')
            assert git(DEST, 'write-tree').decode().strip() == stage['tree']
            tree_check(stage['tree'])
            git(DEST, 'commit', '-m', 'Private checkpoint: P210 Round0 and accepted batch evidence; HOLD_EXTERNAL', timeout=300)
            commit = git(DEST, 'rev-parse', 'HEAD').decode().strip()
            identity = git(DEST, 'show', '-s', '--format=%an%x00%ae%x00%cn%x00%ce', 'HEAD').decode().rstrip('\n').split('\0')
            assert identity == ['mariswang','wangliang.f@gmail.com','mariswang','wangliang.f@gmail.com']
            result['commit_identity'] = approval['commit_identity']
            assert git(DEST, 'rev-list', '--parents', '-n', '1', 'HEAD').decode().split() == [commit, BASE]
            assert git(DEST, 'rev-parse', 'HEAD^{tree}').decode().strip() == stage['tree']
            tree_check(commit)
            result.update(commit=commit, tree=stage['tree'], object_stream=blob_stream_check())
            assert not git(DEST, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
        elif args.phase == 'push':
            overlay_files()
            committed = json.loads((EVIDENCE / 'commit_revision_02/RESULT.actual.json').read_text())
            commit = committed['commit']
            assert git(DEST, 'rev-parse', 'HEAD').decode().strip() == commit
            assert not git(DEST, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
            tree_check(commit)
            remote(DEST)
            git(DEST, 'push', 'origin', commit + ':refs/heads/main', timeout=300)
            remote(DEST, commit)
            git(DEST, 'fetch', '--no-tags', 'origin', 'refs/heads/main:refs/remotes/origin/main', timeout=300)
            assert git(DEST, 'rev-list', '--left-right', '--count', 'HEAD...origin/main').split() == [b'0',b'0']
            assert not git(DEST, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
            result.update(commit=commit, tree=committed['tree'], actual_remote_confirmed=True,
                          divergence=[0,0], original_mirror_intentionally_still_at=BASE)
        baseline_unchanged()
        historical_failure_preserved()
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

