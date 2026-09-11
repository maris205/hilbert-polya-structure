#!/usr/bin/env python3
"""SOURCE ONLY. Observe a fixed finite private-checkpoint boundary; never run Git/SSH.

The only writes are new private evidence in a fresh owned directory.
No current host observation has occurred merely because this source exists.
"""
import hashlib
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure/.git')
BARE = Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git')
FIELDS = ('st_dev', 'st_ino', 'st_mode', 'st_nlink', 'st_uid', 'st_gid',
          'st_rdev', 'st_size', 'st_mtime_ns', 'st_ctime_ns')
ENV5 = ('HOME', 'USER', 'LOGNAME', 'SSH_AUTH_SOCK', 'SSH_AGENT_PID')
ROLES = [MIRROR / x for x in ('config', 'HEAD', 'index', 'packed-refs',
          'refs/heads/main', 'objects/info/alternates')]
ROLES += [BARE / x for x in ('config', 'HEAD', 'index', 'packed-refs',
           'objects/info/alternates')]
ROLES += [Path('/usr/bin/git'), Path('/usr/bin/ssh'), Path('/usr/bin/python3.10')]
BARE_MAIN = BARE / 'refs/heads/main'
CONFIGS = (Path('/root/.ssh/config'), Path('/etc/ssh/ssh_config'))
HOSTKEYS = tuple(Path(x) for x in ('/root/.ssh/known_hosts',
    '/root/.ssh/known_hosts2', '/etc/ssh/ssh_known_hosts', '/etc/ssh/ssh_known_hosts2'))
DROPINS = Path('/etc/ssh/ssh_config.d')
FILE_LIMIT = 32 * 1024 * 1024
CONFIG_LIMIT = 256 * 1024
TOTAL_LIMIT = 80 * 1024 * 1024
READ = 0

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def meta(st):
    return {name: str(getattr(st, name)) for name in FIELDS}

def dump(directory, name, data):
    body = (json.dumps(data, sort_keys=True, indent=2) + '\n').encode()
    fd = os.open(directory / name, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, 'wb', closefd=False) as stream:
            stream.write(body)
            stream.flush()
            os.fsync(stream.fileno())
    finally:
        os.close(fd)
    return {'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()}

def parent_chain(path):
    for parent in reversed(path.parents):
        st = parent.lstat()
        need(stat.S_ISDIR(st.st_mode), 'Nonphysical parent of fixed role')
    return str(path)

def read_role(path, keep=False, limit=FILE_LIMIT):
    global READ
    parent_chain(path)
    try:
        before = path.lstat()
    except FileNotFoundError:
        return {'present': False}, None
    need(stat.S_ISREG(before.st_mode), 'Nonregular or aliased fixed role')
    need(before.st_size <= limit and READ + before.st_size <= TOTAL_LIMIT,
         'Fixed byte ceiling exceeded before opening role')
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    pieces = [] if keep else None
    h = hashlib.sha256()
    g = hashlib.sha1(b'blob ' + str(before.st_size).encode() + b'\0')
    count = 0
    try:
        opened = os.fstat(fd)
        while True:
            body = os.read(fd, min(65536, limit - count + 1))
            if not body:
                break
            count += len(body)
            READ += len(body)
            need(count <= limit and READ <= TOTAL_LIMIT, 'Read byte ceiling exceeded')
            h.update(body)
            g.update(body)
            if keep:
                pieces.append(body)
        ended = os.fstat(fd)
    finally:
        os.close(fd)
    after = path.lstat()
    need(meta(before) == meta(opened) == meta(ended) == meta(after),
         'Fixed role changed during descriptor read')
    need(count == before.st_size, 'File length differed from stable metadata')
    parent_chain(path)
    value = {'present': True, 'bytes': count, 'sha256': h.hexdigest(),
             'mode': '100755' if before.st_mode & 0o111 else '100644',
             'oid': g.hexdigest(),
             'observation': {'path': str(path), 'metadata': meta(before)}}
    return value, b''.join(pieces) if keep else None

def interpreter_spelling():
    p = Path('/usr/bin/python3')
    parent_chain(p)
    before = p.lstat()
    target = os.readlink(p) if stat.S_ISLNK(before.st_mode) else None
    need(target == 'python3.10', 'Interpreter alias differs; new target is not read')
    need(meta(before) == meta(p.lstat()), 'Interpreter alias changed')
    return {'present': True, 'lexical_metadata': meta(before),
            'symlink_target': target, 'resolved': '/usr/bin/python3.10'}

def dropin_names():
    parent_chain(DROPINS)
    try:
        before = DROPINS.lstat()
    except FileNotFoundError:
        return {'present': False}
    need(stat.S_ISDIR(before.st_mode), 'Aliased/non-directory drop-in frontier')
    entries = []
    with os.scandir(DROPINS) as scan:
        for item in scan:
            need(len(entries) < 32, 'More than 32 immediate drop-in entries')
            entries.append({'name': item.name, 'metadata': meta(item.stat(follow_symlinks=False))})
    need(meta(before) == meta(DROPINS.lstat()), 'Drop-in directory changed during listing')
    return {'present': True, 'metadata': meta(before),
            'entries': sorted(entries, key=lambda x: x['name']),
            'member_contents_read': False}

def main():
    need(len(sys.argv) == 1, 'No modes, filenames or remote arguments are accepted')
    need(Path.cwd() == ROOT and ROOT.resolve(strict=True) == ROOT, 'Wrong physical cwd')
    need(sys.flags.isolated == 1 and sys.flags.no_site == 1 and
         sys.dont_write_bytecode and sys.flags.optimize == 0, 'Expected -I -S -B flags')
    need(os.environ.get('PYTHONPATH') is None, 'PYTHONPATH must be absent')
    need(os.getuid() == 0 and os.geteuid() == 0, 'Only the proposed local root role is in scope')
    need(sys.executable == '/usr/bin/python3',
         'Observed interpreter spelling differs from the exact proposed argv')
    out = Path(tempfile.mkdtemp(prefix='symbolic-dynamics-checkpoint03-runtime-', dir='/root'))
    print(json.dumps({'private_evidence_directory': str(out),
                      'status': 'OBSERVATION_STARTED_NOT_ACCEPTED'}), flush=True)
    try:
        inherited = {k: os.environ[k] for k in ENV5 if k in os.environ}
        runtime = {'argv': sys.argv, 'cwd': str(Path.cwd()), 'executable': sys.executable,
                   'version_info': list(sys.version_info), 'isolated': sys.flags.isolated,
                   'no_site': sys.flags.no_site, 'dont_write_bytecode': sys.dont_write_bytecode,
                   'optimize': sys.flags.optimize, 'uid': os.getuid(), 'euid': os.geteuid(),
                   'gid': os.getgid(), 'egid': os.getegid(), 'pythonpath_absent': True}
        spelling = interpreter_spelling()
        roles = {str(p): read_role(p)[0] for p in ROLES}
        spelling['resolved_key'] = {k: roles['/usr/bin/python3.10'][k]
                                   for k in ('bytes', 'sha256', 'mode', 'oid')}
        roles['/usr/bin/python3'] = spelling
        extra = {str(BARE_MAIN): read_role(BARE_MAIN)[0]}
        hostkeys = {str(p): read_role(p)[0] for p in HOSTKEYS}
        configs = {}
        for p in CONFIGS:
            mark, body = read_role(p, keep=True, limit=CONFIG_LIMIT)
            configs[str(p)] = {'key': mark, 'whole_body_hex_private': body.hex() if body is not None else None}
        frontier = dropin_names()
        before_end_roles = roles
        ending_roles = {str(p): read_role(p)[0] for p in ROLES}
        ending_spelling = interpreter_spelling()
        ending_spelling['resolved_key'] = spelling['resolved_key']
        ending_roles['/usr/bin/python3'] = ending_spelling
        need(before_end_roles == ending_roles, 'Protected role endpoints differ')
        need(extra == {str(BARE_MAIN): read_role(BARE_MAIN)[0]}, 'Bare-main endpoints differ')
        need(hostkeys == {str(p): read_role(p)[0] for p in HOSTKEYS}, 'Hostkey file endpoints differ')
        need({str(p): configs[str(p)]['key'] for p in CONFIGS} ==
             {str(p): read_role(p, limit=CONFIG_LIMIT)[0] for p in CONFIGS},
             'Base config endpoints differ')
        need(frontier == dropin_names(), 'Drop-in name frontier endpoints differ')
        need(inherited == {k: os.environ[k] for k in ENV5 if k in os.environ},
             'Allowed inherited roles changed')
        report = {'schema': 'checkpoint03-runtime-observation-v1',
                  'status': 'OBSERVED_ROOT_RECEIPT_AND_SSH_POLICY_PENDING',
                  'runtime': runtime, 'inherited_environment_private': inherited,
                  'protected_roles': roles, 'separate_bare_main': extra,
                  'hostkey_file_keys_no_contents': hostkeys, 'base_configs_private': configs,
                  'dropin_name_frontier_private': frontier,
                  'config_evaluation_or_includes_followed': False,
                  'git_ssh_network_or_agent_calls': 0, 'checkpoint_executor_invoked': False,
                  'observer_executed': True,
                  'atime_may_change_from_reads': True, 'continuous_launch_attestation': False}
        pin = dump(out, 'PRIVATE_OBSERVATION.json', report)
        public = {'schema': report['schema'], 'status': report['status'],
                  'private_evidence_directory': str(out), 'private_observation_pin': pin,
                  'protected_role_count': len(roles), 'base_config_count': len(configs),
                  'hostkey_role_count': len(hostkeys), 'ssh_policy_accepted': False,
                  'four_operation_phases': 'HOLD'}
        dump(out, 'SUMMARY.json', public)
        print(json.dumps(public, sort_keys=True), flush=True)
    except BaseException:
        dump(out, 'PRIVATE_FAILURE.json', {'traceback_private': traceback.format_exc(),
                                          'status': 'OBSERVATION_FAILED_NO_OPERATION_AUTHORITY'})
        print(json.dumps({'private_evidence_directory': str(out),
                          'status': 'OBSERVATION_FAILED_NO_OPERATION_AUTHORITY'}), flush=True)
        raise SystemExit(1)

if __name__ == '__main__':
    main()
