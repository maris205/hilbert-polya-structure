#!/usr/bin/env python3
"""P212 source-only infrastructure adaptation of the accepted P211 core.
See INFRASTRUCTURE_LINEAGE.md for the exact original and full native diff.
Only this header and the heartbeat label differ from that accepted source.
No P212 execution or fresh independent infrastructure approval is claimed.
"""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import signal
import time
import sys
import sysconfig

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = None
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
COMMANDS = []
UNFINALIZED_NATIVE = []

def need(test, detail):
    if not test:
        raise AssertionError(detail)


def now():
    return datetime.now(timezone.utc).isoformat()


def lexists(path):
    return os.path.lexists(str(path))


def value(path):
    path = Path(path)
    need(path.is_file(), ('regular_file', str(path)))
    data = path.read_bytes()
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def rich(path):
    path = Path(path)
    return {**value(path), 'resolved': str(path.resolve(strict=True)),
            'symlink': os.readlink(path) if path.is_symlink() else None}


def pin(path, expected):
    actual = value(path)
    wanted = expected if isinstance(expected, dict) else {'sha256': expected}
    need(all(actual[k] == wanted[k] for k in ('sha256', 'bytes') if k in wanted), ('pin', str(path), wanted, actual))
    return actual


def read_json(path):
    return json.loads(Path(path).read_bytes())


def write_bytes(path, data):
    path = Path(path)
    need(path.is_relative_to(OUT), ('write_scope', str(path)))
    need(path.parent.resolve(strict=True) == path.parent, ('physical_write_parent_no_symlink', str(path)))
    with path.open('xb') as stream:
        stream.write(data)


def write_json(path, data):
    write_bytes(path, (json.dumps(data, sort_keys=True, indent=2) + '\n').encode())


def manifest(base, expected=None, count=None):
    base = Path(base)
    if expected is not None:
        pin(base / 'SHA256SUMS', expected)
    rows = {}
    data = (base / 'SHA256SUMS').read_bytes()
    need(data.endswith(b'\n'), ('manifest_final_newline', str(base)))
    for line in data.decode().split('\n')[:-1]:
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, ('manifest_syntax', str(base), line))
        digest, name = match.groups()
        p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and name not in rows and name != 'SHA256SUMS', ('manifest_nonself_safe_unique', name))
        rows[name] = digest
    actual = set()
    for p in base.rglob('*'):
        need(not p.is_symlink(), ('package_symlink', str(p)))
        if p.is_file():
            actual.add(p.relative_to(base).as_posix())
    need(set(rows) == actual - {'SHA256SUMS'}, ('complete_manifest_inventory', str(base)))
    if count is not None:
        need(len(rows) == count, ('manifest_payload_count', str(base), len(rows), count))
    for name, digest in rows.items():
        pin(base / name, digest)
    return rows


def ordinary_sample():
    modules = {}
    for name, module in sorted(sys.modules.items()):
        source = getattr(module, '__file__', None)
        if source and Path(source).is_file():
            path = Path(source).resolve(strict=True)
            need(path.suffix not in {'.pyc', '.pyo'}, ('no_loaded_bytecode', name, str(path)))
            modules[name] = {'path': str(path), **value(path)}
    maps = Path('/proc/self/maps').read_bytes()
    mapped = {}
    for line in maps.decode().splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            need(not fields[5].endswith(' (deleted)'), ('deleted_mapped_file', fields[5]))
            path = Path(fields[5]).resolve(strict=True)
            mapped[str(path)] = value(path)
    return {'modules': modules, 'mapped_files': mapped, 'proc_maps': maps.decode(),
            'proc_maps_sha256': sha256(maps).hexdigest(), 'proc_maps_bytes': len(maps),
            'volatile_proc_maps_not_an_immutable_input': True, 'executable': str(Path(sys.executable).resolve()),
            'version': sys.version, 'flags': repr(sys.flags), 'sys_path': sys.path, 'argv': sys.argv,
            'environment': dict(os.environ), 'cwd': str(Path.cwd()), 'pycache_prefix': sys.pycache_prefix,
            'cache_lexists': lexists(sys.pycache_prefix), 'scope': 'file-backed module/map sample, not continuous or OS syscall tracing'}


def group_members(pgid):
    members=[]
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            raw=(proc/'stat').read_text()
            fields=raw[raw.rfind(')')+2:].split()
            if int(fields[2])==pgid:
                members.append({'pid':int(proc.name),'state':fields[0],'ppid':int(fields[1]),
                                'pgid':int(fields[2]),'sid':int(fields[3]),'start_ticks':int(fields[19])})
        except (OSError,ProcessLookupError,PermissionError):
            continue
    return members


def settle_group(p, terminate=False):
    """Signals are limited to the new session/group created by this launcher.

    No output digest may be finalized unless quiescent is true. Zombies have
    no file-writing capability; their identities are retained separately.
    """
    events=[]
    def live():
        members=group_members(p.pid)
        assert all(m['sid']==p.pid for m in members),'unexpected process-group/session identity'
        return [m for m in members if m['state']!='Z']
    def send(sig):
        if live():
            try:
                os.killpg(p.pid,sig)
                events.append({'signal':signal.Signals(sig).name,'epoch':time.time()})
            except ProcessLookupError:
                pass
    if terminate:
        send(signal.SIGTERM)
    end=time.monotonic()+5
    while live() and time.monotonic()<end:
        p.poll()
        time.sleep(0.1)
    if live():
        send(signal.SIGTERM)
        end=time.monotonic()+3
        while live() and time.monotonic()<end:
            p.poll()
            time.sleep(0.1)
    if live():
        send(signal.SIGKILL)
        end=time.monotonic()+5
        while live() and time.monotonic()<end:
            p.poll()
            time.sleep(0.1)
    p.poll()
    remaining=group_members(p.pid)
    return {'owned_pgid':p.pid,'owned_sid':p.pid,'signals':events,
            'remaining_members':remaining,'quiescent':not any(m['state']!='Z' for m in remaining),
            'native_returncode':p.returncode}


def command(label, argv, *, timeout, cwd, require_success=True, stderr_policy='empty'):
    need(isinstance(timeout, (int, float)) and timeout > 0, 'explicit_positive_timeout')
    need(stderr_policy in ('empty', 'retain'), 'declared_stderr_policy')
    cwd = Path(cwd)
    need(cwd.is_dir() and cwd.resolve(strict=True) == cwd, 'exact_physical_command_cwd')
    folder = OUT / 'commands' / label
    folder.mkdir()
    entry = {'argv': argv, 'cwd': str(cwd), 'environment': ENV, 'started_utc': now(), 'started_epoch': time.time(), 'timeout_seconds': timeout,
             'status': 'ATTEMPTED', 'exit_code': None, 'stdin': 'DEVNULL', 'new_owned_session_requested': True}
    write_json(folder / 'ATTEMPT.json', entry)
    process = settlement = None
    failure, timed_out, interrupted = None, False, False
    code, wrapper_code, spawned = None, 127, False
    with (folder / 'stdout.raw').open('xb') as out, (folder / 'stderr.raw').open('xb') as err:
        try:
            process = subprocess.Popen(argv, cwd=cwd, env=ENV, stdin=subprocess.DEVNULL,
                                       stdout=out, stderr=err, start_new_session=True)
            spawned = True
            deadline = time.monotonic() + timeout
            try:
                while process.poll() is None:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        timed_out = True
                        failure = 'native command exceeded its explicit deadline'
                        break
                    try:
                        process.wait(timeout=min(30, remaining))
                    except subprocess.TimeoutExpired:
                        print(json.dumps({'status': 'P212_OWNED_NATIVE_RUNNING', 'label': label,
                                          'pid': process.pid, 'timeout_seconds': timeout}), flush=True)
            except BaseException as exc:
                interrupted, failure = True, repr(exc)
            finally:
                try:
                    settlement = settle_group(process, terminate=timed_out or interrupted or process.poll() is None)
                except BaseException as exc:
                    settlement = {'quiescent': False, 'owned_pgid': process.pid, 'settlement_failure': repr(exc)}
                    failure = repr(exc)
            code = process.returncode
            wrapper_code = 124 if timed_out else 130 if interrupted else code
        except OSError as exc:
            failure = repr(exc)
            if process is not None:
                try:
                    settlement = settle_group(process, terminate=True)
                except BaseException as settlement_error:
                    settlement = {'quiescent': False, 'owned_pgid': process.pid, 'settlement_failure': repr(settlement_error)}
                code = process.returncode
        except BaseException as exc:
            # An audit-hook failure/interruption before Popen returns is not
            # evidence that no process exists. Do not invent SPAWN_FAILED or
            # finalize streams without a native handle and settled identity.
            failure = repr(exc)
            if process is not None:
                try:
                    settlement = settle_group(process, terminate=True)
                except BaseException as settlement_error:
                    settlement = {'quiescent': False, 'owned_pgid': process.pid,
                                  'settlement_failure': repr(settlement_error)}
            UNFINALIZED_NATIVE.append(label)
            write_json(folder / 'UNFINALIZED_NATIVE.json', {**entry, 'ended_utc': now(),
                'status': 'NO_COMPLETED_SPAWN_OR_COMMAND_RESULT',
                'pid': process.pid if process is not None else None,
                'process_group_settlement': settlement, 'failure': failure,
                'output_hashes_not_finalized': True,
                'stdout_path': 'stdout.raw', 'stderr_path': 'stderr.raw'})
            raise RuntimeError('unknown pre-return native outcome: preserve attempt without a stream seal') from exc
    if process is not None and (settlement is None or not settlement['quiescent']):
        UNFINALIZED_NATIVE.append(label)
        write_json(folder / 'UNFINALIZED_NATIVE.json', {**entry, 'ended_utc': now(),
            'process_group_settlement': settlement, 'output_hashes_not_finalized': True,
            'stdout_path': 'stdout.raw', 'stderr_path': 'stderr.raw', 'failure': failure})
        raise RuntimeError('owned native group is not quiescent: do not hash or seal its mutable streams')
    streams_complete = spawned and not timed_out and not interrupted and settlement['quiescent']
    receipt = {**entry, 'status': 'TIMED_OUT' if timed_out else 'INTERRUPTED' if interrupted else 'SPAWN_FAILED' if not spawned else 'COMPLETED',
               'ended_utc': now(), 'ended_epoch': time.time(), 'pid': process.pid if process is not None else None,
               'exit_code': code, 'wrapper_exit_code': wrapper_code, 'spawned': spawned,
               'streams_complete': streams_complete, 'timed_out': timed_out, 'interrupted': interrupted, 'failure': failure,
               'process_group_settlement': settlement,
               'stream_scope': 'Every emitted native byte retained in exclusive files; hashes finalized only after owned-group quiescence. A timeout/interruption remains an unsuccessful partial computation.',
               'stdout': value(folder / 'stdout.raw'), 'stderr': value(folder / 'stderr.raw')}
    write_json(folder / 'RECEIPT.json', receipt)
    COMMANDS.append({'label': label, **receipt})
    if require_success:
        need(code == 0 and streams_complete and
             (stderr_policy == 'retain' or not receipt['stderr']['bytes']) and not settlement['signals'],
             ('actual_owned_native_command_failed', label, receipt))
    stdout = (folder / 'stdout.raw').read_bytes()
    if require_success and argv[0] == '/usr/bin/cmp':
        need(stdout == b'', ('native_cmp_full_empty_stdout', label))
    return stdout


def seal():
    need(not UNFINALIZED_NATIVE, 'refuse_to_seal_unsettled_native_output')
    files = sorted(p for p in OUT.rglob('*') if p.is_file())
    need(not lexists(OUT / 'SHA256SUMS') and all(not p.is_symlink() for p in OUT.rglob('*')), 'exclusive_output_seal')
    write_bytes(OUT / 'SHA256SUMS', ''.join(value(p)['sha256'] + '  ' + p.relative_to(OUT).as_posix() + '\n' for p in files).encode())
    rows = manifest(OUT, count=len(files))
    return {'payloads': len(rows), 'manifest': value(OUT / 'SHA256SUMS')}
