#!/usr/bin/env python3
"""SOURCE ONLY: separately root-bound checkpoint03 capture/stage/commit/push.

No prepare mode, phase chaining, Git config/default-index mutation, force,
cleanup, science or public release. Native success remains ROOT_PRODUCT_PENDING.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import stat
import subprocess
import sys
import tempfile
import time
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
PREP = QA / 'private_checkpoint_executor_ssh_delta04'
SELF = PREP / 'checkpoint.py'
SCOPE_PATH = QA / 'private_checkpoint03_scope_root01/CHOSEN_SCOPE.json'
SCOPE_PIN = {'bytes': 6162898, 'sha256': '76e633c45920f46fc6c1d3e840d9d82fd7025946b31a397356c1d771b1ba5c92'}
SCOPE_RECEIPT = QA / 'private_checkpoint03_scope_root01/RECEPTION.md'
SCOPE_RECEIPT_SHA = 'b6db83e7109a6c853a4d0a04d9603ecb6c2b64dd77b891d8a7e6bbe177c80930'
CORE_PATH = QA / 'private_checkpoint03_scope_preparation01/FINAL_CANDIDATE_INVENTORY.json'
CORE_PIN = {'bytes': 6558074, 'sha256': 'c38a3ac6a2a08d3d1069d62abb15faa410a038b15cbe7853fa5b9c8e8a05f74f'}
BRIDGE_PATH = QA / 'private_checkpoint03_scope_preparation01/OPTIONAL_OLD_SCOUT_BRIDGE_INVENTORY.json'
BRIDGE_PIN = {'bytes': 19762, 'sha256': '8c80c8845a8c855bd33e3f49cb4ffc3c780e7da3867bd8945091132679f8a7c5'}
BARE = Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
BASE = '7d43cb323adf7d27326263b8ce4158d4eefff43a'
BASE_TREE = '64feab3a9eff397179a6670aff5b1ff7d0595796'
MIRROR_BASE = 'a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
REMOTE = 'git@github.com:maris205/hilbert-polya-structure.git'
IDENTITY = ('mariswang', 'wangliang.f@gmail.com')
PHASES = ('capture', 'stage', 'commit', 'push')
RUN_PREFIX = 'symbolic-dynamics-checkpoint03-'
COUNTS = {'files': 8207, 'bytes': 386716363, 'additions': 8204,
          'modifications': 2, 'unchanged': 1, 'deletions': 0}
LIMIT, MIN_FREE, PATH_BATCH = 400000000, 2333581815, 512
CONTROL_SOURCES = {
    'SYMBOLIC_DYNAMICS_STATE.md': str(QA / 'control_before_residual46_accepted01/STATE.before.md'),
    'docs/papers211_215_sequence/PIPELINE_STATE.md':
        str(QA / 'control_before_residual46_accepted01/PIPELINE.before.md')}
INHERITED_NAMES = ('HOME', 'USER', 'LOGNAME', 'SSH_AUTH_SOCK', 'SSH_AGENT_PID')
COMMIT_MESSAGE = (
    b'Checkpoint P211 complete and accepted 43-closed research boundary\n\n'
    b'Two retained, one complete, three open seats; preserve P211 warnings and failures.\n'
    b'Include exact old-source bridge; exclude current 46-closed controls and ongoing P212.\n'
    b'Private documentary synchronization only; no five-paper completion. HOLD_EXTERNAL\n')
GIT_SETTINGS = ('-c', 'core.hooksPath=/dev/null', '-c', 'core.fsmonitor=false',
    '-c', 'core.untrackedCache=false', '-c', 'gc.auto=0',
    '-c', 'maintenance.auto=false', '-c', 'commit.gpgSign=false')
KEY_FIELDS = ('bytes', 'sha256', 'mode', 'oid')
STAT_FIELDS = ('st_dev', 'st_ino', 'st_mode', 'st_nlink', 'st_uid', 'st_gid',
               'st_rdev', 'st_size', 'st_mtime_ns', 'st_ctime_ns')

def need(condition, message):
    if not condition:
        raise RuntimeError(message)

def sha(body):
    return hashlib.sha256(body).hexdigest()

def projection(value):
    return {k: value[k] for k in KEY_FIELDS}

def pairs(items):
    value = {}
    for name, item in items:
        need(name not in value, 'Duplicate JSON key')
        value[name] = item
    return value

def parse(body):
    def reject(value):
        raise RuntimeError('Non-integer JSON number or constant: ' + str(value))
    return json.loads(body, object_pairs_hook=pairs, parse_float=reject, parse_constant=reject)

def save(path, value):
    body = value if isinstance(value, bytes) else (
        json.dumps(value, indent=2, sort_keys=True) + '\n').encode()
    with Path(path).open('xb') as stream:
        stream.write(body)
        stream.flush()
        os.fsync(stream.fileno())

def metadata(value):
    return {name: str(getattr(value, name)) for name in STAT_FIELDS}

def safe_name(name):
    need(isinstance(name, str) and re.fullmatch(r'[A-Za-z0-9_.\-/]+', name)
         and not name.startswith('/')
         and all(p not in ('', '.', '..') for p in name.split('/')),
         'Unsafe/noncanonical relative pathname: ' + repr(name))
    return name

def physical(path):
    path = Path(path)
    need(path.is_absolute() and str(path) == os.path.normpath(str(path))
         and path.resolve(strict=True) == path, 'Missing/aliased physical path: ' + str(path))
    return path

def blob(path):
    path = physical(path)
    before = path.lstat()
    need(stat.S_ISREG(before.st_mode), 'Expected physical regular file: ' + str(path))
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        opened = os.fstat(fd)
        with os.fdopen(fd, 'rb', closefd=False) as stream:
            body = stream.read()
        ended = os.fstat(fd)
    finally:
        os.close(fd)
    after = path.lstat()
    marks = [metadata(v) for v in (before, opened, ended, after)]
    need(marks == [marks[0]] * 4 and path.resolve(strict=True) == path,
         'Changed file identity/metadata during complete read: ' + str(path))
    value = {'sha256': sha(body), 'bytes': len(body),
             'mode': '100755' if before.st_mode & 0o111 else '100644',
             'oid': hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest()}
    return value, body, {'path': str(path), 'metadata': marks[0]}

def key(path):
    return blob(path)[0]

def read(path):
    return parse(blob(path)[1])

def pinned(path, pin):
    need(set(pin) == {'bytes', 'sha256'} and type(pin['bytes']) is int
         and pin['bytes'] >= 0 and re.fullmatch('[0-9a-f]{64}', pin['sha256']),
         'Incomplete complete-file pin')
    value, body, observation = blob(path)
    need({k: value[k] for k in ('bytes', 'sha256')} == pin, 'Whole input pin mismatch: ' + str(path))
    return body, observation

def ref_input(ref):
    need(isinstance(ref, dict) and set(ref) == {'path', 'pin'}, 'Invalid receipt/reference')
    path = Path(ref['path'])
    need(path.is_relative_to(QA), 'Receipt/reference is outside physical QA scope')
    body, observation = pinned(path, ref['pin'])
    return body, observation

def load_scope(path, core_path, bridge_path):
    raw, scope_observation = pinned(path, SCOPE_PIN)
    core_raw, core_observation = pinned(core_path, CORE_PIN)
    bridge_raw, bridge_observation = pinned(bridge_path, BRIDGE_PIN)
    scope, core, bridge = parse(raw), parse(core_raw), parse(bridge_raw)
    need(scope['status'] == 'ROOT_SOURCE_SCOPE_SELECTED_NOT_OPERATIVE_AUTHORITY'
         and scope['base'] == BASE and scope['base_tree'] == BASE_TREE
         and scope['counts'] == COUNTS and scope['max_selected_bytes'] == LIMIT
         and scope['minimum_free_bytes'] == MIN_FREE
         and scope['scientific_runs'] == 0 and scope['git_mutations'] == 0
         and scope['private_push'] is False, 'Wrong selected scope boundary')
    need(scope['original_core_key']['path'] == str(CORE_PATH.relative_to(ROOT))
         and projection(scope['original_core_key']) == key(core_path)
         and scope['bridge_key']['path'] == str(BRIDGE_PATH.relative_to(ROOT))
         and projection(scope['bridge_key']) == key(bridge_path), 'Chosen scope source companions differ')
    values, sources = {}, {}
    for row in scope['inventory']:
        bridge_row = row.get('source_role') == 'EXACT_OLD_SOURCE_BRIDGE'
        row_fields = {'source_path', 'git_path', 'bytes', 'sha256', 'mode', 'oid', 'source_role'}
        need(set(row) == row_fields | ({'scope'} if bridge_row else {'category'}),
             'Unexpected selected inventory row schema')
        name = safe_name(row['git_path'])
        need(name not in values, 'Duplicate selected Git pathname')
        expect_source = CONTROL_SOURCES.get(name, str(ROOT / name))
        expect_role = ('EXACT_PHYSICAL_43_CONTROL' if name in CONTROL_SOURCES else
                       'EXACT_OLD_SOURCE_BRIDGE' if name in bridge['inventory'] else 'UNCHANGED_WORKSPACE_ORIGINAL')
        need(row['source_path'] == expect_source and row['source_role'] == expect_role,
             'Physical source mapping changed: ' + name)
        need(type(row['bytes']) is int and 0 <= row['bytes'] <= LIMIT
             and row['mode'] in ('100644', '100755')
             and re.fullmatch('[0-9a-f]{64}', row['sha256'])
             and re.fullmatch('[0-9a-f]{40}', row['oid']), 'Unsupported selected whole-file key')
        if bridge_row:
            need(row['scope'] == 'OPTIONAL_SEPARATE_APPROVAL_NOT_IN_CORE', 'Historical bridge schema changed')
        else:
            need(row['category'] == core['inventory'][name]['category'], 'Core category differs')
        values[name], sources[name] = projection(row), row['source_path']
    need(len(values) == COUNTS['files'] and sum(v['bytes'] for v in values.values()) == COUNTS['bytes'],
         'Selected census differs')
    need(set(core['inventory']).isdisjoint(bridge['inventory'])
         and set(values) == set(core['inventory']) | set(bridge['inventory']),
         'Core/complete bridge union differs from chosen per-file set')
    for name, row in {**core['inventory'], **bridge['inventory']}.items():
        need(name == row['git_path'] and values[name] == projection(row), 'Companion file key differs')
    groups = [g['relative'] for g in core['groups']] + [g['path'] for g in bridge['groups']]
    need(len(core['groups']) == 178 and len(bridge['groups']) == 4
         and len(groups) == len(set(groups)), 'Complete source groups differ')
    assigned = []
    for group in groups:
        safe_name(group)
        members_ = sorted(n for n in values if n == group or n.startswith(group + '/'))
        need(members_, 'Empty approved source group')
        assigned.extend(members_)
    need(len(assigned) == len(set(assigned)) and set(assigned) == set(values), 'Group partition differs')
    baseline, delta = {}, {}
    for row in scope['delta_preview']:
        need(set(row) == {'git_path', 'old', 'status'}, 'Invalid baseline preview schema')
        name = safe_name(row['git_path'])
        need(name in values and name not in delta and row['status'] in ('A', 'M', '='), 'Invalid baseline row')
        old = row['old']
        if old is not None:
            need(set(old) == {'mode', 'oid'} and old['mode'] in ('100644', '100755')
                 and re.fullmatch('[0-9a-f]{40}', old['oid']), 'Invalid baseline key')
            baseline[name] = old
        new = {k: values[name][k] for k in ('mode', 'oid')}
        expected_status = '=' if old == new else 'M' if old is not None else 'A'
        need(row['status'] == expected_status, 'Wrong selected baseline status')
        delta[name] = row['status']
    need(set(delta) == set(values) and [sum(s == k for s in delta.values()) for k in ('A', 'M', '=')]
         == [8204, 2, 1], 'Full baseline preview census differs')
    return {'raw': raw, 'core_raw': core_raw, 'bridge_raw': bridge_raw,
            'values': values, 'sources': sources, 'groups': groups, 'baseline': baseline,
            'observations': [scope_observation, core_observation, bridge_observation]}

def source_path(plan, name, frozen=None):
    return Path(plan['sources'][name]) if frozen is None else frozen / name

def membership(plan, frozen=None):
    result = []
    for group in plan['groups']:
        expected = sorted(n for n in plan['values'] if n == group or n.startswith(group + '/'))
        path = source_path(plan, group, frozen) if group in plan['values'] else (
            ROOT / group if frozen is None else frozen / group)
        physical(path)
        if path.is_file():
            got = [group]
        else:
            need(path.is_dir(), 'Unsupported selected source group')
            got = []
            for directory, folders, files in os.walk(path, followlinks=False):
                for name in folders:
                    need(not (Path(directory) / name).is_symlink(), 'Directory alias in complete source group')
                for name in files:
                    child = Path(directory) / name
                    physical(child)
                    need(child.is_file(), 'Nonregular source-group member')
                    got.append(group + '/' + child.relative_to(path).as_posix())
            got.sort()
        need(got == expected, 'Complete approved source-group membership drift: ' + group)
        result.extend(got)
    need(len(result) == len(set(result)) and set(result) == set(plan['values']),
         'Selected membership is not the exact chosen file set')
    if frozen is not None:
        actual = sorted(p.relative_to(frozen).as_posix() for p in frozen.rglob('*') if p.is_file())
        need(actual == sorted(plan['values']) and not any(p.is_symlink() for p in frozen.rglob('*')),
             'Unexpected frozen file or alias outside selected groups')
    return sorted(result)

def inventory(plan, frozen=None):
    names = membership(plan, frozen)
    values, observations = {}, {}
    for name in names:
        values[name], body, observations[name] = blob(source_path(plan, name, frozen))
        need(values[name] == plan['values'][name], 'Selected source/frozen whole-file mismatch: ' + name)
    need(names == membership(plan, frozen), 'Selected membership changed during complete read')
    return {'inventory': values, 'observations': observations, 'membership': names}

def environment(inherited, index=None, identity=False):
    env = dict(inherited)
    env.update(PATH='/usr/bin:/bin', LANG='C', LC_ALL='C', TZ='UTC', GIT_OPTIONAL_LOCKS='0',
        GIT_TERMINAL_PROMPT='0', GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL='/dev/null',
        GIT_NO_REPLACE_OBJECTS='1',
        GIT_SSH_COMMAND='/usr/bin/ssh -F none -a -x -T '
                        '-o BatchMode=yes '
                        '-o StrictHostKeyChecking=yes '
                        '-o ConnectTimeout=20 '
                        '-o ConnectionAttempts=1 '
                        '-o UpdateHostKeys=no '
                        '-o CheckHostIP=no '
                        '-o VerifyHostKeyDNS=no '
                        '-o KnownHostsCommand=none '
                        '-o AddKeysToAgent=no '
                        '-o ControlMaster=no '
                        '-o ControlPath=none '
                        '-o ControlPersist=no '
                        '-o ClearAllForwardings=yes '
                        '-o Tunnel=no '
                        '-o ProxyCommand=none '
                        '-o ProxyJump=none '
                        '-o PermitLocalCommand=no '
                        '-o LocalCommand=none '
                        '-o RemoteCommand=none '
                        '-o CanonicalizeHostname=no '
                        '-o ForkAfterAuthentication=no '
                        '-o EscapeChar=none '
                        '-o PKCS11Provider=none '
                        '-o SecurityKeyProvider=none '
                        '-o PreferredAuthentications=publickey '
                        '-o PubkeyAuthentication=yes '
                        '-o GSSAPIAuthentication=no '
                        '-o GSSAPIDelegateCredentials=no '
                        '-o HostbasedAuthentication=no '
                        '-o PasswordAuthentication=no '
                        '-o KbdInteractiveAuthentication=no')
    if index is not None:
        env['GIT_INDEX_FILE'] = str(index)
    if identity:
        env.update(GIT_AUTHOR_NAME=IDENTITY[0], GIT_AUTHOR_EMAIL=IDENTITY[1],
                   GIT_COMMITTER_NAME=IDENTITY[0], GIT_COMMITTER_EMAIL=IDENTITY[1])
    return env

def stop_child(process):
    record = {'leader_pid': process.pid, 'leader_returncode_before': process.poll(), 'signals': []}
    if process.returncode is None:
        for signum, seconds in ((signal.SIGTERM, 5), (signal.SIGKILL, 3)):
            try:
                os.killpg(process.pid, signum)
                record['signals'].append({'signal': int(signum), 'sent': True})
            except ProcessLookupError:
                record['signals'].append({'signal': int(signum), 'sent': False, 'reason': 'ESRCH'})
            try:
                process.wait(timeout=seconds)
                break
            except subprocess.TimeoutExpired:
                record['signals'][-1]['wait_timed_out'] = True
    record['leader_returncode_after'] = process.poll()
    record['scope'] = 'Accepted bounded owned-group timeout handling, not complete process-tree census'
    return record

def interrupted(signum, frame):
    raise InterruptedError('Checkpoint interrupted by signal ' + str(signum))

class Commands:
    def __init__(self, directory, phase, inherited):
        self.directory, self.phase, self.inherited, self.count = directory, phase, inherited, 0

    def run(self, argv, stdin=b'', index=None, identity=False):
        self.count += 1
        directory = self.directory / f'command_{self.count:03d}'
        directory.mkdir()
        env = environment(self.inherited, index, identity)
        save(directory / 'stdin.raw', stdin)
        save(directory / 'ATTEMPT.json', {'argv': argv, 'cwd': str(ROOT), 'environment': env,
            'timeout_seconds': 50, 'stdout_stderr_transport': 'owned pipes; exact bytes saved to preopened raw files',
            'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()})
        process, output, errors, eof, timed_out, exception, handling = None, b'', b'', False, False, None, None
        start = time.monotonic()
        with (directory / 'stdout.raw').open('xb') as out, (directory / 'stderr.raw').open('xb') as err:
            try:
                process = subprocess.Popen(argv, cwd=ROOT, env=env, stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
                save(directory / 'SPAWN.json', {'pid': process.pid, 'spawned': True,
                    'start_new_session': True, 'signal_group_from_start_new_session': process.pid,
                    'separate_proc_group_sample': False})
                try:
                    output, errors = process.communicate(stdin, timeout=50)
                    eof = True
                except subprocess.TimeoutExpired as caught:
                    timed_out = True
                    output, errors = caught.output or b'', caught.stderr or b''
                    save(directory / 'TIMEOUT_PARTIAL.json', {'stdout_hex': output.hex(), 'stderr_hex': errors.hex()})
                    handling = stop_child(process)
                    try:
                        output, errors = process.communicate(timeout=3)
                        eof = True
                    except subprocess.TimeoutExpired as final:
                        output, errors = final.output or output, final.stderr or errors
                        exception = 'Post-handling pipe EOF remains unknown; no complete stream claim'
            except BaseException:
                exception = traceback.format_exc()
                if process is not None:
                    try:
                        handling = stop_child(process)
                        output, errors = process.communicate(timeout=3)
                        eof = True
                    except BaseException as caught:
                        if isinstance(caught, subprocess.TimeoutExpired):
                            output, errors = caught.output or output, caught.stderr or errors
                        handling = {'preceding_handling': handling, 'handling_exception': traceback.format_exc()}
            finally:
                out.write(output)
                err.write(errors)
                out.flush()
                err.flush()
                os.fsync(out.fileno())
                os.fsync(err.fileno())
                code = process.poll() if process is not None else None
                save(directory / 'RESULT.json', {'returncode': code, 'pipes_eof': eof,
                    'timed_out': timed_out, 'handling': handling, 'exception': exception,
                    'elapsed_seconds': time.monotonic() - start, 'stdout_bytes': len(output),
                    'stderr_bytes': len(errors), 'stdout_sha256': sha(output) if eof else None,
                    'stderr_sha256': sha(errors) if eof else None})
                if process is not None:
                    for stream in (process.stdin, process.stdout, process.stderr):
                        if stream is not None:
                            stream.close()
        need(code == 0 and eof and not timed_out and exception is None,
             'Native command failed/unknown; originals retained: ' + str(directory))
        return output

    def git(self, *args, stdin=b'', index=None, identity=False):
        mutations = {'stage': {'read-tree', 'hash-object', 'update-index', 'write-tree'},
                     'commit': {'commit-tree'}, 'push': {'push', 'update-ref'}}
        readonly = {'rev-parse', 'symbolic-ref', 'remote', 'ls-remote', 'ls-tree', 'ls-files',
                    'diff-tree', 'cat-file', 'rev-list', 'show'}
        need(args[0] in readonly or args[0] in mutations.get(self.phase, set()), 'Git operation outside phase')
        need(identity == (args[0] == 'commit-tree'), 'Commit identity may only accompany commit-tree')
        return self.run(['/usr/bin/git', '--git-dir=' + str(BARE), *GIT_SETTINGS, *args],
                        stdin, index, identity)

    def mirror(self, *args):
        need(args in (('rev-parse', 'HEAD'), ('remote', 'get-url', 'origin'),
                      ('status', '--porcelain=v1', '-z', '--untracked-files=all')),
             'Original mirror operation outside read-only allowlist')
        return self.run(['/usr/bin/git', '-C', str(MIRROR), *GIT_SETTINGS, *args])

def protected_roles():
    paths = [MIRROR / '.git' / p for p in ('config', 'HEAD', 'index', 'packed-refs',
             'refs/heads/main', 'objects/info/alternates')]
    paths += [BARE / p for p in ('config', 'HEAD', 'index', 'packed-refs', 'objects/info/alternates')]
    paths += [Path('/usr/bin/git'), Path('/usr/bin/ssh'), Path('/usr/bin/python3').resolve(strict=True)]
    result = {}
    for path in paths:
        try:
            path.lstat()
        except FileNotFoundError:
            result[str(path)] = {'present': False}
        else:
            value, body, observation = blob(path)
            result[str(path)] = {'present': True, **value, 'observation': observation}
    spelling = Path('/usr/bin/python3')
    before = spelling.lstat()
    target = os.readlink(spelling) if stat.S_ISLNK(before.st_mode) else None
    resolved = spelling.resolve(strict=True)
    need(metadata(before) == metadata(spelling.lstat()) and resolved == spelling.resolve(strict=True),
         'Interpreter spelling/alias changed')
    result[str(spelling)] = {'present': True, 'lexical_metadata': metadata(before),
        'symlink_target': target, 'resolved': str(resolved), 'resolved_key': key(resolved)}
    return result

def remote(command, expected):
    output = command.git('ls-remote', '--exit-code', REMOTE, 'refs/heads/main')
    need(output == (expected + '\trefs/heads/main\n').encode(), 'Actual remote differs or is unconfirmed')

def repository(command, expected=BASE):
    need(command.git('rev-parse', '--is-bare-repository') == b'true\n', 'Destination is not bare')
    need(command.git('symbolic-ref', 'HEAD') == b'refs/heads/main\n', 'Bare HEAD differs')
    need(command.git('rev-parse', 'refs/heads/main') == (expected + '\n').encode(), 'Bare main differs')
    need(command.git('rev-parse', '--show-object-format') == b'sha1\n', 'Object format differs')
    need(command.git('rev-parse', BASE + '^{tree}') == (BASE_TREE + '\n').encode(), 'BASE tree differs')
    need(command.git('remote') == b'', 'Bare remote config changed')
    need(command.mirror('rev-parse', 'HEAD') == (MIRROR_BASE + '\n').encode(), 'Mirror HEAD differs')
    need(command.mirror('status', '--porcelain=v1', '-z', '--untracked-files=all') == b'', 'Mirror not clean')
    need(command.mirror('remote', 'get-url', 'origin') == (REMOTE + '\n').encode(), 'Mirror origin differs')
    remote(command, expected)

def tree_map(raw, names):
    need(not raw or raw.endswith(b'\0'), 'Truncated tree stream')
    result = {}
    for row in raw.split(b'\0')[:-1]:
        head, name = row.split(b'\t', 1)
        mode, kind, oid = head.decode().split()
        name = safe_name(name.decode())
        need(name in names and name not in result and kind == 'blob'
             and mode in ('100644', '100755') and re.fullmatch('[0-9a-f]{40}', oid), 'Invalid selected tree record')
        result[name] = {'mode': mode, 'oid': oid}
    return result

def selected_tree(command, ref, values):
    names, result = sorted(values), {}
    for begin in range(0, len(names), PATH_BATCH):
        batch = names[begin:begin + PATH_BATCH]
        got = tree_map(command.git('ls-tree', '-r', '-z', '--full-tree', ref, '--', *batch), set(batch))
        need(not set(result) & set(got), 'Repeated selected tree entry')
        result.update(got)
    return result

def diff_map(raw, names):
    need(not raw or raw.endswith(b'\0'), 'Truncated complete diff stream')
    fields, result = raw.split(b'\0')[:-1], {}
    need(len(fields) % 2 == 0, 'Invalid full diff framing')
    for i in range(0, len(fields), 2):
        attrs, name = fields[i].decode().split(), safe_name(fields[i + 1].decode())
        need(len(attrs) == 5 and attrs[0].startswith(':') and attrs[4] in ('A', 'M')
             and name not in result and name in names, 'Deletion/rename/nonselected diff forbidden')
        oldmode, newmode, oldoid, newoid, status_ = attrs
        need(newmode in ('100644', '100755') and re.fullmatch('[0-9a-f]{40}', oldoid)
             and re.fullmatch('[0-9a-f]{40}', newoid), 'Invalid diff key')
        result[name] = {'oldmode': oldmode[1:], 'mode': newmode, 'oldoid': oldoid, 'oid': newoid, 'status': status_}
    return result

def verify_tree(command, plan, tree, index):
    need(re.fullmatch('[0-9a-f]{40}', tree), 'Invalid actual tree OID')
    values, baseline = plan['values'], plan['baseline']
    expected = {n: {k: v[k] for k in ('mode', 'oid')} for n, v in values.items()}
    need(selected_tree(command, tree, values) == expected, 'Selected new tree differs')
    actual, names = {}, sorted(values)
    for begin in range(0, len(names), PATH_BATCH):
        batch = names[begin:begin + PATH_BATCH]
        raw = command.git('ls-files', '--stage', '-z', '--', *batch, index=index)
        need(not raw or raw.endswith(b'\0'), 'Truncated selected index stream')
        for row in raw.split(b'\0')[:-1]:
            head, name = row.split(b'\t', 1)
            mode, oid, stage = head.decode().split()
            name = safe_name(name.decode())
            need(stage == '0' and name in batch and name not in actual, 'Unmerged/duplicate/unselected index entry')
            actual[name] = {'mode': mode, 'oid': oid}
    need(actual == expected, 'Selected isolated index differs')
    delta = diff_map(command.git('diff-tree', '--no-commit-id', '--raw', '-r', '-z',
                                '--no-renames', BASE_TREE, tree), set(values))
    changed = {n for n, v in expected.items() if baseline.get(n) != v}
    need(len(changed) == 8206 and set(delta) == changed, 'Whole unfiltered diff differs')
    for name, value in delta.items():
        old = baseline.get(name, {'mode': '000000', 'oid': '0' * 40})
        need(value == {'oldmode': old['mode'], 'mode': expected[name]['mode'], 'oldoid': old['oid'],
             'oid': expected[name]['oid'], 'status': 'M' if name in baseline else 'A'}, 'Exact changed record differs')
    unique = {}
    for value in values.values():
        need(value['oid'] not in unique or unique[value['oid']] == value['bytes'], 'Inconsistent blob length')
        unique[value['oid']] = value['bytes']
    objects = sorted(unique)
    output = command.git('cat-file', '--batch-check', stdin=''.join(n + '\n' for n in objects).encode())
    need(output == ''.join(f'{n} blob {unique[n]}\n' for n in objects).encode(), 'Selected object metadata differs')
    return len(changed)

def complete_manifest(directory, expected):
    raw, observation = pinned(directory / 'MANIFEST.sha256', expected)
    rows = {}
    for line in raw.decode().splitlines():
        digest, name = line.split('  ', 1)
        safe_name(name)
        need(name not in rows and re.fullmatch('[0-9a-f]{64}', digest), 'Malformed phase manifest')
        rows[name] = digest
    actual = {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()}
    need(not any(p.is_symlink() for p in directory.rglob('*')) and set(rows) == actual - {'MANIFEST.sha256'}
         and 'MANIFEST.sha256' not in rows, 'Incomplete/self phase manifest')
    for name, digest in rows.items():
        need(key(directory / name)['sha256'] == digest, 'Phase manifest byte mismatch: ' + name)
    return raw

def binding(path, expected_sha, phase):
    need(re.fullmatch('[0-9a-f]{64}', expected_sha or ''), 'Exact external binding hash is required')
    physical(path)
    need(path.parent == QA / 'private_checkpoint03_bindings' and path.name == phase + '.json',
         'Binding must be the separately root-owned exact phase path')
    value, raw, observation = blob(path)
    need(value['sha256'] == expected_sha, 'Externally selected binding bytes differ')
    b = parse(raw)
    need(set(b) == {'schema', 'status', 'enabled', 'phase', 'source_sha256', 'scope_sha256',
         'scope_receipt', 'source_receipt', 'runtime_receipt', 'run', 'run_record_pin', 'previous_phase',
         'previous_root_receipt', 'inherited_environment', 'protected_roles', 'policy'},
         'Unsupported phase binding schema')
    need(b['schema'] == 'checkpoint03-phase-binding-v1' and b['enabled'] is True
         and b['status'] == 'ROOT_BOUND_ONE_CHECKPOINT_PHASE' and b['phase'] == phase,
         'Disabled/non-root/wrong-phase binding')
    need(b['scope_sha256'] == SCOPE_PIN['sha256'] and re.fullmatch('[0-9a-f]{64}', b['source_sha256']),
         'Wrong scope/source binding')
    need(b['policy'] == {'private_only': True, 'closed_boundary': 43, 'selected_files': 8207,
         'selected_bytes': 386716363, 'max_selected_bytes': LIMIT, 'minimum_free_bytes': MIN_FREE,
         'per_native_timeout_seconds': 50, 'path_batch': PATH_BATCH,
         'automatic_next_phase': False, 'default_index_or_config_write': False,
         'force_push_or_history_rewrite': False, 'cleanup_or_retry': False,
         'full_runtime_hermeticity_claim': False, 'hold_external': True}, 'Binding policy changed')
    receipts = {}
    for role in ('scope_receipt', 'source_receipt', 'runtime_receipt'):
        body, mark = ref_input(b[role])
        receipts[role] = {'ref': b[role], 'raw_hex': body.hex(), 'observation': mark}
    need(b['scope_receipt']['path'] == str(SCOPE_RECEIPT)
         and b['scope_receipt']['pin']['sha256'] == SCOPE_RECEIPT_SHA, 'Wrong root-selected scope receipt')
    inherited = {k: os.environ[k] for k in INHERITED_NAMES if k in os.environ}
    need(b['inherited_environment'] == inherited and all(isinstance(v, str) for v in inherited.values()),
         'Current allowed inherited Git/SSH environment roles differ')
    need(b['protected_roles'] == protected_roles(), 'Fresh protected role key differs')
    return b, raw, observation, receipts

def previous(run, phase, expected, root_ref, source_sha, run_pin):
    number = PHASES.index(phase)
    if number == 0:
        need(expected is None and root_ref is None, 'Capture cannot claim a previous phase')
        return None
    earlier = PHASES[number - 1]
    directory = run / earlier
    complete_manifest(directory, expected)
    need(root_ref['path'] == str(directory / 'ROOT_RECEPTION.json'), 'Wrong prior root reception path')
    receipt_raw, mark = pinned(Path(root_ref['path']), root_ref['pin'])
    receipt, result = parse(receipt_raw), read(directory / 'RESULT.json')
    need(receipt == {'schema': 'checkpoint03-phase-root-reception-v1',
         'status': 'ROOT_ACCEPTED_PRIVATE_CHECKPOINT_PHASE', 'phase': earlier, 'run': str(run),
         'scope_sha256': SCOPE_PIN['sha256'], 'source_sha256': source_sha,
         'result_sha256': key(directory / 'RESULT.json')['sha256'],
         'actual_outer_product_closed': True, 'complete_native_streams_received': True,
         'previous_phase': result['previous_phase']}, 'Prior root receipt is missing or mismatched')
    need(result['status'] == 'NATIVE_PHASE_COMPLETE_ROOT_PRODUCT_PENDING'
         and result['phase'] == earlier and result['scope_sha256'] == SCOPE_PIN['sha256']
         and result['source_sha256'] == source_sha and result['run'] == str(run)
         and result['run_record_pin'] == run_pin,
         'Prior native result scope mismatch')
    old_b = read(directory / 'BINDING_ORIGINAL.json')
    need(old_b['phase'] == earlier and old_b['source_sha256'] == source_sha
         and old_b['scope_sha256'] == SCOPE_PIN['sha256'], 'Prior binding scope mismatch')
    previous(run, earlier, result['previous_phase'], old_b['previous_root_receipt'], source_sha, run_pin)
    return result

def frozen_guard(run, plan, source_sha):
    need(key(run / 'PLAN.json')['sha256'] == SCOPE_PIN['sha256']
         and key(run / 'executed_source.py')['sha256'] == source_sha, 'Frozen chosen plan/executor changed')
    current = load_scope(run / 'PLAN.json', run / 'CORE_GROUPS_ORIGINAL.json', run / 'BRIDGE_GROUPS_ORIGINAL.json')
    need(current['values'] == plan['values'] and current['sources'] == plan['sources']
         and current['baseline'] == plan['baseline'], 'Frozen plan companions changed')
    return inventory(plan, run / 'frozen')

def execute(args):
    path = Path(args.binding)
    b, binding_raw, before_binding, receipts = binding(path, args.binding_sha256, args.phase)
    source_key, source_raw, source_mark = blob(Path(__file__).resolve(strict=True))
    need(source_key['sha256'] == b['source_sha256'], 'Actual executor source differs')
    if args.phase == 'capture':
        need(Path(__file__).resolve(strict=True) == SELF and b['run'] is None
             and b['run_record_pin'] is None and b['previous_phase'] is None and b['previous_root_receipt'] is None,
             'Capture requires the received live source and no existing run')
        plan = load_scope(SCOPE_PATH, CORE_PATH, BRIDGE_PATH)
        before_inventory = inventory(plan)
        capacities = []
        for destination in (Path('/root'), BARE):
            value = os.statvfs(physical(destination))
            available = value.f_bavail * value.f_frsize
            need(available >= MIN_FREE and MIN_FREE == 5 * COUNTS['bytes'] + LIMIT, 'Insufficient fresh capacity')
            capacities.append({'path': str(destination), 'available_bytes': available, 'required_bytes': MIN_FREE})
        run = Path(tempfile.mkdtemp(prefix=RUN_PREFIX, dir='/root'))
        print(json.dumps({'run': str(run), 'phase': args.phase, 'status': 'RUN_CREATED_NOT_COMPLETE'}), flush=True)
        (run / 'frozen').mkdir()
        indexdir = Path(tempfile.mkdtemp(prefix='index-', dir=run))
        save(run / 'RUN.json', {'index': str(indexdir / 'index'), 'scope_sha256': SCOPE_PIN['sha256'],
                               'source_sha256': source_key['sha256'], 'run': str(run)})
        save(run / 'PLAN.json', plan['raw'])
        save(run / 'CORE_GROUPS_ORIGINAL.json', plan['core_raw'])
        save(run / 'BRIDGE_GROUPS_ORIGINAL.json', plan['bridge_raw'])
        save(run / 'executed_source.py', source_raw)
        run_pin = {k: key(run / 'RUN.json')[k] for k in ('bytes', 'sha256')}
    else:
        run = Path(b['run'])
        need(run.parent == Path('/root') and re.fullmatch(RUN_PREFIX + '[a-z0-9_]+', run.name)
             and physical(run) == run and Path(__file__).resolve(strict=True) == run / 'executed_source.py',
             'Later phase requires the actual physically frozen executor/run')
        plan = load_scope(run / 'PLAN.json', run / 'CORE_GROUPS_ORIGINAL.json', run / 'BRIDGE_GROUPS_ORIGINAL.json')
        before_inventory = frozen_guard(run, plan, b['source_sha256'])
        capacities = None
        run_pin = b['run_record_pin']
        pinned(run / 'RUN.json', run_pin)
    prior = previous(run, args.phase, b['previous_phase'], b['previous_root_receipt'], b['source_sha256'], run_pin)
    info = read(run / 'RUN.json')
    need(info['scope_sha256'] == SCOPE_PIN['sha256'] and info['source_sha256'] == b['source_sha256']
         and info['run'] == str(run), 'Run/source/scope key differs')
    index = Path(info['index'])
    need(index.parent.parent == run and re.fullmatch('index-[a-z0-9_]+', index.parent.name)
         and index.name == 'index' and index.resolve() == index, 'Unowned isolated index')
    physical(index.parent)
    if args.phase in ('capture', 'stage'):
        need(list(index.parent.iterdir()) == [], 'Isolated index parent must still be empty')
    else:
        need(key(index) == prior['isolated_index_key'] and list(index.parent.iterdir()) == [index],
             'Received isolated index bytes/membership changed')
    directory = run / args.phase
    directory.mkdir(exist_ok=False)
    command = Commands(directory, args.phase, b['inherited_environment'])
    try:
        save(directory / 'BINDING_ORIGINAL.json', binding_raw)
        save(directory / 'INPUTS_BEFORE.json', {'binding': before_binding, 'executor': source_mark,
             'receipts': receipts, 'selected': before_inventory, 'protected_roles': b['protected_roles'],
             'capacity': capacities, 'argv': sys.argv, 'executable': sys.executable,
             'interpreter_flags': {'isolated': sys.flags.isolated, 'no_site': sys.flags.no_site,
                                   'dont_write_bytecode': sys.dont_write_bytecode}})
        repository(command)
        if args.phase == 'capture':
            need(selected_tree(command, BASE, plan['values']) == plan['baseline'], 'Fresh selected BASE differs')
            copies = {}
            for name, expected in sorted(plan['values'].items()):
                value, raw, mark = blob(source_path(plan, name))
                need(value == expected, 'Source changed before exact copy')
                target = run / 'frozen' / name
                target.parent.mkdir(parents=True, exist_ok=True)
                save(target, raw)
                target.chmod(0o555 if expected['mode'] == '100755' else 0o444)
                frozen_value, frozen_raw, frozen_mark = blob(target)
                after_value, after_raw, after_mark = blob(source_path(plan, name))
                need(frozen_raw == raw == after_raw and frozen_value == value == after_value
                     and mark == after_mark, 'Raw source/copy/after or metadata differs')
                copies[name] = {'source_before': mark, 'source_after': after_mark, 'frozen': frozen_mark}
            save(directory / 'EXACT_COPY_RECORDS.json', copies)
            save(directory / 'FROZEN_AFTER.json', frozen_guard(run, plan, b['source_sha256']))
            after_inventory = inventory(plan)
            need(after_inventory == before_inventory, 'Live source complete key changed during capture')
            need(not os.path.lexists(index), 'Capture unexpectedly created isolated index')
            result = {'git_mutations': 0, 'selected_paths': 8207, 'selected_bytes': 386716363}
        else:
            if args.phase == 'stage':
                need(not os.path.lexists(index), 'Do not overwrite an existing or failed isolated index')
                command.git('read-tree', BASE, index=index)
                changed = [n for n, v in sorted(plan['values'].items())
                           if plan['baseline'].get(n) != {k: v[k] for k in ('mode', 'oid')}]
                need(len(changed) == 8206, 'Wrong changed path census')
                input_paths = ''.join(json.dumps(str(run / 'frozen' / n)) + '\n' for n in changed).encode()
                written = command.git('hash-object', '-w', '--no-filters', '--stdin-paths', stdin=input_paths, index=index)
                need(written == ''.join(plan['values'][n]['oid'] + '\n' for n in changed).encode(),
                     'Actual frozen object OIDs differ')
                rows = b''.join((plan['values'][n]['mode'] + ' ' + plan['values'][n]['oid'] + '\t' + n).encode()
                                + b'\0' for n in changed)
                command.git('update-index', '-z', '--index-info', stdin=rows, index=index)
                tree_raw = command.git('write-tree', index=index)
                tree = tree_raw.decode().removesuffix('\n')
                need(tree_raw == (tree + '\n').encode(), 'Unexpected write-tree framing')
                result = {'tree': tree, 'changed_paths': verify_tree(command, plan, tree, index)}
            elif args.phase == 'commit':
                tree = prior['tree']
                verify_tree(command, plan, tree, index)
                commit_raw = command.git('commit-tree', tree, '-p', BASE, stdin=COMMIT_MESSAGE, identity=True)
                commit = commit_raw.decode().removesuffix('\n')
                need(re.fullmatch('[0-9a-f]{40}', commit) and commit_raw == (commit + '\n').encode(), 'Invalid commit result')
                verify_commit(command, tree, commit)
                result = {'tree': tree, 'commit': commit, 'local_main_unchanged': True}
            else:
                tree, commit = prior['tree'], prior['commit']
                verify_tree(command, plan, tree, index)
                verify_commit(command, tree, commit)
                remote(command, BASE)
                frozen_guard(run, plan, b['source_sha256'])
                need(protected_roles() == b['protected_roles'], 'Protected roles changed before normal push')
                command.git('push', '--porcelain', REMOTE, commit + ':refs/heads/main')
                remote(command, commit)
                command.git('update-ref', 'refs/heads/main', commit, BASE)
                repository(command, expected=commit)
                verify_tree(command, plan, tree, index)
                verify_commit(command, tree, commit)
                result = {'tree': tree, 'commit': commit, 'actual_remote_confirmed': True}
            after_inventory = frozen_guard(run, plan, b['source_sha256'])
            need(after_inventory == before_inventory, 'Frozen complete identity/key changed during phase')
        repository(command, expected=result['commit'] if args.phase == 'push' else BASE)
        need(protected_roles() == b['protected_roles'], 'Protected original role changed')
        pinned(run / 'RUN.json', run_pin)
        final_source_key, final_source_raw, final_source_mark = blob(Path(__file__).resolve(strict=True))
        need(final_source_key == source_key and final_source_raw == source_raw and final_source_mark == source_mark,
             'Actual executor complete byte/identity key changed')
        index_key = None if args.phase == 'capture' else key(index)
        if args.phase in ('commit', 'push'):
            need(index_key == prior['isolated_index_key'], 'Isolated index changed during non-index phase')
        final_key, final_binding_raw, final_binding_mark = blob(path)
        need(final_binding_raw == binding_raw and final_binding_mark == before_binding,
             'Selected phase binding raw/identity changed')
        for role in receipts:
            raw, mark = ref_input(b[role])
            need(raw.hex() == receipts[role]['raw_hex'] and mark == receipts[role]['observation'],
                 'Receipt source changed during phase')
        save(directory / 'INPUTS_AFTER.json', {'binding': final_binding_mark, 'selected': after_inventory,
             'protected_roles': b['protected_roles'], 'receipts': receipts, 'executor': final_source_mark,
             'run_record_pin': run_pin, 'isolated_index_key': index_key})
        result.update(schema='checkpoint03-native-phase-result-v1',
             status='NATIVE_PHASE_COMPLETE_ROOT_PRODUCT_PENDING', phase=args.phase, run=str(run),
             source_sha256=b['source_sha256'], scope_sha256=SCOPE_PIN['sha256'],
             run_record_pin=run_pin, isolated_index_key=index_key,
             previous_phase=b['previous_phase'], commands=command.count, phase_seal=None,
             no_nonselected_changes=True, no_deletions=True, no_force_push=True,
             automatic_next_phase=False, no_new_science=True, hold_external=True)
        save(directory / 'RESULT.json', result)
        print(json.dumps(result, sort_keys=True), flush=True)
    except BaseException:
        save(directory / 'FAILURE.json', {'phase': args.phase, 'traceback': traceback.format_exc(),
             'run': str(run), 'no_rollback': True, 'raw_evidence_preserved': True,
             'possible_partial_git_or_remote_state': True, 'automatic_retry_cleanup_next_phase': False})
        raise

def verify_commit(command, tree, commit):
    need(command.git('rev-list', '--parents', '-n', '1', commit) == (commit + ' ' + BASE + '\n').encode(),
         'Commit does not have exactly BASE as parent')
    need(command.git('rev-parse', commit + '^{tree}') == (tree + '\n').encode(), 'Commit tree differs')
    got = command.git('show', '-s', '--format=%an%x00%ae%x00%cn%x00%ce', commit)
    need(got == ('\0'.join([*IDENTITY, *IDENTITY]) + '\n').encode(), 'Command-local identity differs')
    raw = command.git('cat-file', '-p', commit)
    need(hashlib.sha1(b'commit ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == commit,
         'Complete actual commit bytes/OID differ')
    header, message = raw.split(b'\n\n', 1)
    lines = header.splitlines()
    need(len(lines) == 4 and lines[0] == ('tree ' + tree).encode()
         and lines[1] == ('parent ' + BASE).encode()
         and lines[2].startswith(b'author mariswang <wangliang.f@gmail.com> ')
         and lines[3].startswith(b'committer mariswang <wangliang.f@gmail.com> ')
         and message == COMMIT_MESSAGE, 'Unexpected commit headers/message/signature')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=PHASES)
    parser.add_argument('--binding', required=True)
    parser.add_argument('--binding-sha256', required=True)
    args = parser.parse_args()
    need(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.dont_write_bytecode
         and sys.flags.optimize == 0 and Path(sys.executable).resolve(strict=True)
         == Path('/usr/bin/python3').resolve(strict=True)
         and Path.cwd() == ROOT and os.environ.get('PYTHONPATH') is None,
         'Use the externally received /usr/bin/python3 -I -S -B startup and physical ROOT cwd')
    for signum in (signal.SIGTERM, signal.SIGHUP):
        signal.signal(signum, interrupted)
    execute(args)

if __name__ == '__main__':
    main()
