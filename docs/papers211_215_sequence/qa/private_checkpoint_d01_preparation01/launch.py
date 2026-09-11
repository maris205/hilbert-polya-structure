#!/usr/bin/env python3
"""SOURCE ONLY: one separately granted D01; ordinary bootstrap trust, no self-attestation."""
import hashlib
import json
import os
from pathlib import Path
import signal
import stat
import subprocess
import sys
import time
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SELF = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_d01_preparation01/launch.py'
ARGV = ['/usr/bin/ssh', '-V']
ENV5 = ('HOME', 'USER', 'LOGNAME', 'SSH_AUTH_SOCK', 'SSH_AGENT_PID')
FIXED_ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
FIELDS = ('st_dev', 'st_ino', 'st_mode', 'st_nlink', 'st_uid', 'st_gid',
          'st_rdev', 'st_size', 'st_mtime_ns', 'st_ctime_ns')
BUDGET = {'normal_seconds': 14, 'term_seconds': 3, 'kill_seconds': 2, 'drain_seconds': 1}
HISTORICAL = {
    '/usr/bin/ssh': {'bytes': 846888, 'sha256': '3a9c5d143150f0b2816ab1a5a7c58a9f970280b061f617abee54d2834a498b53',
                    'mode': '100755', 'oid': 'e557aa1e4d653aad208f5a81539a913668eaebf4'},
    '/usr/bin/python3.10': {'bytes': 5937704, 'sha256': 'd6bca2b84e73c7775a0dd5e6a76899cfe4ee62863d7c8f88513811d1fda23f49',
                           'mode': '100755', 'oid': '3730413072cb4d299a02004b02307f012f461805'}}
GRANT_KEYS = {'schema', 'status', 'enabled', 'diagnostic', 'invocation_id',
              'source_sha256', 'source_receipt', 'runtime_receipt', 'ordinary_trust_accepted',
              'output_directory', 'argv', 'budget', 'inherited_environment_private',
              'protected_roles_private', 'interpreter_alias_private'}
LIMIT = 32 * 1024 * 1024

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def meta(st):
    return {k: str(getattr(st, k)) for k in FIELDS}

def pin(body):
    return {'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()}

def unique(pairs):
    result = {}
    for k, v in pairs:
        need(k not in result, 'Duplicate JSON key')
        result[k] = v
    return result

def parents(path):
    for parent in reversed(path.parents):
        need(stat.S_ISDIR(parent.lstat().st_mode), 'Nonphysical parent')

def read_key(path, fd, limit=LIMIT, keep=False):
    parents(path)
    before, opened = path.lstat(), os.fstat(fd)
    need(stat.S_ISREG(before.st_mode) and meta(before) == meta(opened), 'Unstable/nonregular role')
    need(before.st_size <= limit, 'Role exceeds byte limit')
    os.lseek(fd, 0, os.SEEK_SET)
    h = hashlib.sha256()
    g = hashlib.sha1(b'blob ' + str(before.st_size).encode() + b'\0')
    chunks, count = [], 0
    while True:
        body = os.read(fd, min(65536, limit - count + 1))
        if not body:
            break
        count += len(body)
        need(count <= limit, 'Role grew beyond byte limit')
        h.update(body)
        g.update(body)
        if keep:
            chunks.append(body)
    ended, after = os.fstat(fd), path.lstat()
    need(meta(before) == meta(ended) == meta(after) and count == before.st_size,
         'Role changed during same-descriptor read')
    parents(path)
    key = {'present': True, 'bytes': count, 'sha256': h.hexdigest(),
           'mode': '100755' if before.st_mode & 0o111 else '100644', 'oid': g.hexdigest(),
           'observation': {'path': str(path), 'metadata': meta(before)}}
    return key, b''.join(chunks) if keep else None

def open_key(path, held, limit=LIMIT, keep=False):
    parents(path)
    need(stat.S_ISREG(path.lstat().st_mode), 'Aliased or nonregular input')
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    held.append(fd)
    key, body = read_key(path, fd, limit, keep)
    return fd, key, body

def alias(resolved_key):
    path = Path('/usr/bin/python3')
    parents(path)
    before = path.lstat()
    need(stat.S_ISLNK(before.st_mode), 'Interpreter spelling must be the accepted alias')
    target = os.readlink(path)
    need(target == 'python3.10' and meta(before) == meta(path.lstat()), 'Interpreter alias changed')
    return {'present': True, 'lexical_metadata': meta(before), 'symlink_target': target,
            'resolved': '/usr/bin/python3.10',
            'resolved_key': {k: resolved_key[k] for k in ('bytes', 'sha256', 'mode', 'oid')}}

def new_file(directory_fd, name):
    return os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                   0o600, dir_fd=directory_fd)

def write_fd(fd, body):
    view = memoryview(body)
    while view:
        written = os.write(fd, view)
        need(written > 0, 'Short private write')
        view = view[written:]
    os.fsync(fd)
    return pin(body)

def save(directory_fd, name, value, raw=False):
    body = value if raw else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    fd = new_file(directory_fd, name)
    try:
        return write_fd(fd, body)
    finally:
        os.close(fd)

def owned_signal(proc, sig, events):
    event = {'signal': int(sig), 'sent': False}
    try:
        # poll may reap; after a reaped leader no group ownership is invented.
        if proc.poll() is not None:
            event['reason'] = 'DIRECT_CHILD_ALREADY_REAPED'
        else:
            pgid, sid = os.getpgid(proc.pid), os.getsid(proc.pid)
            event.update(observed_pgid=pgid, observed_sid=sid)
            if pgid == sid == proc.pid:
                os.killpg(pgid, sig)
                event['sent'] = True
            else:
                event['reason'] = 'OWNED_SESSION_NOT_CONFIRMED'
    except BaseException as error:
        event['error_type'] = type(error).__name__
        event['error_private'] = str(error)
    events.append(event)

def capture(environment, directory_fd):
    native = {'argv': ARGV, 'cwd': str(ROOT), 'start_new_session_requested': True,
              'pid': None, 'returncode': None, 'pipes_eof': False, 'timed_out': False,
              'cancelled_or_exception': False, 'signal_events': [], 'wait_events': []}
    stdout, stderr, proc = b'', b'', None
    try:
        proc = subprocess.Popen(ARGV, cwd=ROOT, env=environment, stdin=subprocess.DEVNULL,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                shell=False, close_fds=True, start_new_session=True)
        native['pid'] = proc.pid
        origin = time.monotonic()  # Budget starts at successful Popen return, not product startup.
        native['budget_origin_monotonic'] = origin
        try:
            save(directory_fd, 'SPAWN.json', {'pid': proc.pid, 'start_new_session_requested': True,
                 'budget_origin_monotonic': origin, 'native_closed': False})
        except BaseException as error:
            # A receipt-write failure must not skip this child's bounded cleanup.
            native['cancelled_or_exception'] = True
            native['spawn_receipt_error_private'] = repr(error)
        for phase, offset, sig in (('normal', 14, None), ('term', 17, signal.SIGTERM),
                                  ('kill', 19, signal.SIGKILL), ('drain', 20, None)):
            if time.monotonic() >= origin + 20:
                native['timed_out'] = True
                break
            if sig is not None:
                owned_signal(proc, sig, native['signal_events'])
            remaining = origin + offset - time.monotonic()
            if remaining <= 0:
                native['timed_out'] = True
                native['wait_events'].append({'phase': phase, 'result': 'NO_TIME_REMAINING'})
                continue
            try:
                stdout, stderr = proc.communicate(timeout=remaining)
                native['pipes_eof'] = True
                if time.monotonic() > origin + offset:
                    native['timed_out'] = True
                native['wait_events'].append({'phase': phase, 'result': 'COMMUNICATE_COMPLETE'})
                break
            except subprocess.TimeoutExpired as error:
                native['timed_out'] = True
                if error.output is not None:
                    stdout = error.output
                if error.stderr is not None:
                    stderr = error.stderr
                native['wait_events'].append({'phase': phase, 'result': 'TIMEOUT'})
            except BaseException as error:
                native['cancelled_or_exception'] = True
                native['wait_events'].append({'phase': phase, 'result': 'EXCEPTION',
                    'error_type': type(error).__name__, 'error_private': str(error)})
        native['returncode'] = proc.poll()
        native['elapsed_after_spawn_seconds'] = time.monotonic() - origin
        if native['elapsed_after_spawn_seconds'] > 20:
            native['timed_out'] = True
    except BaseException as error:
        native['cancelled_or_exception'] = True
        native['exception_private'] = traceback.format_exc()
        if proc is not None:
            native['returncode'] = proc.poll()
    finally:
        if proc is not None:
            for stream in (proc.stdout, proc.stderr):
                if stream is not None:
                    stream.close()  # No implicit wait or unowned-group cleanup.
    native['native_closed_success'] = (native['returncode'] == 0 and native['pipes_eof']
        and not native['timed_out'] and not native['cancelled_or_exception'])
    return native, stdout, stderr

def main():
    held, directory_fd, public = [], None, {'status': 'D01_PRECAPTURE_FAILED_NO_SUCCESSOR'}
    try:
        need(len(sys.argv) == 3 and sys.argv[0] == str(SELF), 'Exact source, grant and external hash required')
        need(Path.cwd() == ROOT and ROOT.resolve(strict=True) == ROOT, 'Wrong physical cwd')
        need(sys.executable == '/usr/bin/python3' and sys.flags.isolated == 1 and
             sys.flags.no_site == 1 and sys.dont_write_bytecode and sys.flags.optimize == 0,
             'Expected accepted Python spelling and -I -S -B')
        need(os.getuid() == os.geteuid() == 0 and os.environ.get('PYTHONPATH') is None,
             'Expected root process and absent PYTHONPATH')
        grant_path, external_hash = Path(sys.argv[1]), sys.argv[2]
        token = grant_path.name.removeprefix('symbolic-dynamics-d01-grant-').removesuffix('.json')
        need(grant_path == Path('/root') / ('symbolic-dynamics-d01-grant-' + token + '.json')
             and len(token) == 32 and all(c in '0123456789abcdef' for c in token),
             'Grant path outside exact private namespace')
        need(len(external_hash) == 64 and all(c in '0123456789abcdef' for c in external_hash),
             'External grant hash required')
        grant_fd, grant_key, grant_body = open_key(grant_path, held, 65536, True)
        st = os.fstat(grant_fd)
        need(st.st_uid == st.st_gid == 0 and st.st_nlink == 1 and stat.S_IMODE(st.st_mode) == 0o600,
             'Grant must be owner-only regular original')
        need(grant_key['sha256'] == external_hash, 'Grant differs from external selection')
        grant = json.loads(grant_body, object_pairs_hook=unique)
        need(set(grant) == GRANT_KEYS and grant['schema'] == 'private-d01-single-grant-v1'
             and grant['status'] == 'ROOT_GRANTED_D01_ONCE' and grant['enabled'] is True
             and grant['diagnostic'] == 'D01_VERSION_ONLY' and grant['invocation_id'] == token
             and grant['ordinary_trust_accepted'] is True and grant['argv'] == ARGV
             and grant['budget'] == BUDGET, 'Grant does not select exactly D01')
        for role in ('source_receipt', 'runtime_receipt'):
            need(isinstance(grant[role], dict) and set(grant[role]) == {'path', 'bytes', 'sha256'}
                 and isinstance(grant[role]['path'], str) and isinstance(grant[role]['bytes'], int)
                 and grant[role]['bytes'] > 0 and isinstance(grant[role]['sha256'], str)
                 and len(grant[role]['sha256']) == 64, 'Genuine external receipt reference required')
        out = Path('/root') / ('symbolic-dynamics-d01-' + token)
        need(grant['output_directory'] == str(out), 'Root-chosen private output differs')
        parents(out)
        root_stat = Path('/root').lstat()
        need(root_stat.st_uid == root_stat.st_gid == 0 and stat.S_IMODE(root_stat.st_mode) == 0o700,
             'Private parent boundary differs')
        os.umask(0o077)
        os.mkdir(out, 0o700)  # Exact exclusive creation; existing output is never reused.
        directory_fd = os.open(out, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        held.append(directory_fd)
        dst = os.fstat(directory_fd)
        need(dst.st_uid == dst.st_gid == 0 and stat.S_IMODE(dst.st_mode) == 0o700,
             'Private output ownership differs')
        raw_fds = []
        for name in ('stdout.raw', 'stderr.raw'):
            fd = new_file(directory_fd, name)
            held.append(fd)
            raw_fds.append(fd)
        save(directory_fd, 'GRANT.json', grant_body, raw=True)
        source_fd, source_key, source_body = open_key(SELF, held, 65536, True)
        need(source_key['sha256'] == grant['source_sha256'], 'Source differs from granted full hash')
        save(directory_fd, 'EXECUTED_SOURCE.py', source_body, raw=True)
        inherited = {k: os.environ[k] for k in ENV5 if k in os.environ}
        need(inherited == grant['inherited_environment_private'], 'Inherited value or absence differs')
        environment = dict(inherited, **FIXED_ENV)
        need(isinstance(grant['protected_roles_private'], dict) and
             set(grant['protected_roles_private']) == set(HISTORICAL), 'Only two regular tool roles allowed')
        bound, before = {}, {}
        for path_string, old_key in HISTORICAL.items():
            path = Path(path_string)
            fd, key, _ = open_key(path, held)
            need({k: key[k] for k in old_key} == old_key, 'Historical tool content differs')
            need(key == grant['protected_roles_private'][path_string], 'Expected full role key differs')
            bound[path_string], before[path_string] = fd, key
        spelling = alias(before['/usr/bin/python3.10'])
        need(spelling == grant['interpreter_alias_private'], 'Expected full alias role differs')
        runtime = {'argv': sys.argv, 'cwd': str(ROOT), 'executable': sys.executable,
                   'version_info': list(sys.version_info), 'uid': os.getuid(), 'euid': os.geteuid(),
                   'gid': os.getgid(), 'egid': os.getegid(), 'isolated': sys.flags.isolated,
                   'no_site': sys.flags.no_site, 'dont_write_bytecode': sys.dont_write_bytecode,
                   'optimize': sys.flags.optimize, 'pythonpath_absent': True}
        save(directory_fd, 'ATTEMPT.json', {'argv': ARGV, 'cwd': str(ROOT), 'stdin': 'DEVNULL_EOF',
             'environment_private': environment, 'inherited_environment_private': inherited,
             'budget': BUDGET, 'runtime_downstream': runtime, 'source_key': source_key,
             'grant_key': grant_key, 'protected_before': before, 'interpreter_alias_before': spelling})
        native, stdout, stderr = capture(environment, directory_fd)
        stream_pins = [write_fd(fd, body) for fd, body in zip(raw_fds, (stdout, stderr))]
        native.update(stdout_pin=stream_pins[0], stderr_pin=stream_pins[1],
                      streams_complete=native['pipes_eof'], outer_product_accepted=False)
        save(directory_fd, 'NATIVE.json', native)
        after = {p: read_key(Path(p), fd)[0] for p, fd in bound.items()}
        need(after == before and alias(after['/usr/bin/python3.10']) == spelling,
             'Tool or alias endpoint changed')
        need(read_key(SELF, source_fd, 65536)[0] == source_key and
             read_key(grant_path, grant_fd, 65536)[0] == grant_key, 'Source or grant endpoint changed')
        need(inherited == {k: os.environ[k] for k in ENV5 if k in os.environ},
             'Inherited endpoint changed')
        result = {'status': 'D01_NATIVE_CLOSED_ROOT_RECEPTION_PENDING' if native['native_closed_success']
                  else 'D01_FAILED_OR_UNCLOSED_NO_SUCCESSOR', 'native': native,
                  'protected_after': after, 'interpreter_alias_after': spelling,
                  'source_endpoint_equal': True, 'grant_endpoint_equal': True,
                  'inherited_endpoint_equal': True, 'ordinary_trust_not_startup_attestation': True,
                  'D02_or_checkpoint_authority': False}
        result_pin = save(directory_fd, 'PRIVATE_RESULT.json', result)
        public = {'status': result['status'], 'private_result_pin': result_pin,
                  'stdout_pin': stream_pins[0], 'stderr_pin': stream_pins[1],
                  'regular_tool_role_count': 2, 'alias_role_count': 1,
                  'inherited_present_count': len(inherited), 'root_reception_pending': True}
    except BaseException:
        public = {'status': 'D01_FAILED_NO_SUCCESSOR', 'private_failure_pin': None}
        if directory_fd is not None:
            try:
                public['private_failure_pin'] = save(directory_fd, 'PRIVATE_FAILURE.json',
                    {'status': public['status'], 'traceback_private': traceback.format_exc()})
            except BaseException:
                pass  # Preserve original partial files; safe outer failure remains mandatory.
    finally:
        for fd in reversed(held):
            try:
                os.close(fd)
            except OSError:
                pass
    print(json.dumps(public, sort_keys=True), flush=True)
    return 0 if public['status'] == 'D01_NATIVE_CLOSED_ROOT_RECEPTION_PENDING' else 1

if __name__ == '__main__':
    raise SystemExit(main())
