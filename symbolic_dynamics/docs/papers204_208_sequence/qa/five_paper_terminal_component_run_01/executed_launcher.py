#!/usr/bin/env python3
"""One bounded native launch of the sealed four-completed-paper component.

Adapted from the actually accepted P208/P209 read-only reuse launcher.
The component and its three selectors remain at their exact sealed source
paths; no old auditor, writer, scientific producer or build is executed.
This wrapper can only accept a FOUR-paper component, never five-paper PASS.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import sysconfig
import time
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'five_paper_terminal_component_launch_preparation'
CHECKER_PREP = QA / 'five_paper_terminal_gate_preparation'
CHECKER = CHECKER_PREP / 'four_completed.py'
CHECKER_SEAL = 'b984a1d494d0304a39704da1773782e1f6b10902fa4d8b0dbae77bad86c84e20'
CHECKER_SOURCE = '0f762c56781041094a0650abcd5b706360722a2afe72aff812485beaa46738bc'
ROOT_BINDING = CHECKER_PREP / 'ROOT_REUSE_BINDING.json'
ROOT_BINDING_SHA = 'b722f61ae2abcc4220a99473b6d9bb104962b52ea509c258f976c0136d08affd'
OUT = QA / 'five_paper_terminal_component_run_01'
PYTHON = Path('/usr/bin/python3.10')
STDLIB = Path('/usr/lib/python3.10')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
CONFIG_DIRS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/lib/locale/C.utf8', '/etc/profile.d',
    '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv')))
TIMEOUT_SECONDS = 600
SAMPLE_INTERVAL_SECONDS = 0.25
HEARTBEAT_SECONDS = 30
PROC = None
SPAWN_ATTEMPTED = False
SPAWNING, DEFERRED_SIGNAL = False, None
PHASE = 'guard'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def interrupted(signum, frame):
    global DEFERRED_SIGNAL
    if SPAWNING:
        DEFERRED_SIGNAL = signum
        return
    raise RuntimeError('Launcher interrupted by signal ' + str(signum))


def pin(path):
    p = Path(path)
    require(p.is_absolute() and p.is_file(), 'Missing absolute regular input: ' + str(p))
    if p.is_relative_to(ROOT):
        require(p.resolve() == p and not p.is_symlink(), 'Aliased workspace input: ' + str(p))
    digest, length = hashlib.sha256(), 0
    with p.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk); length += len(chunk)
    return {'sha256': digest.hexdigest(), 'bytes': length, 'resolved': str(p.resolve()),
            'symlink': os.readlink(p) if p.is_symlink() else None}


def pins(paths, tolerant=False):
    result = {}
    for name in sorted(set(map(str, paths))):
        try:
            result[name] = pin(name)
        except BaseException:
            if not tolerant: raise
            result[name] = {'read_error': traceback.format_exc()}
    return result


def raw_save(path, data):
    path = Path(path)
    require(path.is_relative_to(OUT) and path.parent.resolve(strict=True) == path.parent,
            'Write outside the exclusive physical component output')
    with path.open('xb') as stream:
        stream.write(data)


def save(path, value):
    raw_save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def compressed_ledger(name, value):
    data = (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode()
    compressed = gzip.compress(data, mtime=0)
    raw_save(OUT / (name + '.json.gz'), compressed)
    meta = {'encoding': 'lossless gzip of UTF-8 JSON, mtime=0',
            'json': {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()},
            'compressed': pin(OUT / (name + '.json.gz')), 'entries': len(value)}
    save(OUT / (name + '.meta.json'), meta)
    return meta


def package(base, expected_sha256, payloads):
    require(base.resolve() == base and not base.is_symlink(), 'Aliased preparation directory')
    seal = base / 'SHA256SUMS'; seal_pin = pin(seal)
    require(seal_pin['sha256'] == expected_sha256, 'Preparation seal changed: ' + str(base))
    rows = {}
    for line in seal.read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(match is not None, 'Preparation manifest syntax')
        digest, name = match.groups(); relative = Path(name)
        require(relative.parts and not relative.is_absolute() and '..' not in relative.parts and
                relative.as_posix() == name and name != 'SHA256SUMS' and name not in rows,
                'Unsafe, self or duplicate preparation manifest entry')
        value = pin(base / name); require(value['sha256'] == digest, 'Preparation payload changed: ' + name)
        rows[name] = value
    entries = list(base.rglob('*'))
    require(len(rows) == payloads and all(not p.is_symlink() for p in entries) and
            set(rows) == {p.relative_to(base).as_posix() for p in entries if p.is_file() and p != seal},
            'Preparation complete physical membership changed')
    return {str(base / n): v for n, v in rows.items()} | {str(seal): seal_pin}


def scoped_inputs(own_seal):
    own = package(PREP, own_seal, 5)
    checker = package(CHECKER_PREP, CHECKER_SEAL, 14)
    require(checker[str(CHECKER)]['sha256'] == CHECKER_SOURCE, 'Component source identity changed')
    require(checker[str(ROOT_BINDING)]['sha256'] == ROOT_BINDING_SHA, 'Actual root reuse binding changed')
    contract = json.loads((CHECKER_PREP / 'FOUR_INPUTS.json').read_bytes())
    expected = contract['fixed_inputs']; require(len(expected) == 54, 'Four-component fixed input count changed')
    actual = pins(expected)
    require(all(all(actual[p][k] == v[k] for k in ('sha256', 'bytes')) for p, v in expected.items()),
            'One of 54 fixed four-component inputs changed')
    binding = json.loads(ROOT_BINDING.read_bytes())
    require(binding['schema'] == 'actual-p208-p209-root-reuse-reception-binding-v1' and
            binding['not_a_placeholder'] is True and binding['native_exit_selector'] == ['result', 'exit_code'],
            'Actual accepted root binding schema, not a future placeholder')
    anchors = pins((binding['native'], binding['report']))
    for role in ('native', 'report'):
        require(all(anchors[binding[role]][k] == binding[role + '_pin'][k] for k in ('sha256', 'bytes')),
                'Bound actual root reception input changed')
    receipt = json.loads(Path(binding['native']).read_bytes())
    require(receipt['result']['exit_code'] == 0 and
            binding['accepted_status'] in Path(binding['report']).read_text(),
            'Bound root reuse reception is not actually accepted')
    # Lifecycle text may change before launch. The component checks the five
    # fixed theorem-block hashes; this wrapper fences the whole live index
    # only over this actual launch interval, never an invented historical pin.
    index = Path(contract['current_index'])
    index = index if index.is_absolute() else ROOT / index
    require(index.is_relative_to(ROOT), 'Current theorem index outside workspace')
    anchors.update(pins((index,)))
    provenance = json.loads((PREP / 'PROVENANCE.json').read_bytes())['inputs']
    adaptation = pins(provenance)
    require(all(all(adaptation[p][k] == v[k] for k in ('sha256', 'bytes')) for p, v in provenance.items()),
            'Pinned accepted launcher/contract adaptation input changed')
    return {'launcher_preparation': own, 'component_preparation': checker, 'fixed_inputs': actual,
            'actual_root_binding_and_live_ceiling_index': anchors, 'adaptation_inputs': adaptation}

def configuration():
    optional = set(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
        '/etc/nsswitch.conf', '/etc/localtime', '/etc/locale.conf', '/etc/default/locale',
        '/usr/lib/locale/locale-archive', '/etc/bash.bashrc', '/etc/profile', '/etc/passwd', '/etc/group',
        '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2')))
    optional.update((Path(sysconfig.get_makefile_filename()), Path(sysconfig.get_config_h_filename()),
        STDLIB.parent / 'python310.zip', PYTHON.parent / 'pyvenv.cfg', PYTHON.parent.parent / 'pyvenv.cfg'))
    for directory in {PYTHON.parent, Path(sys.executable).parent, STDLIB.parent}:
        optional.update(directory / name for name in ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
    for name in ('LDLIBRARY', 'INSTSONAME'):
        if sysconfig.get_config_var(name): optional.add(STDLIB.parent / (sysconfig.get_config_var(name) + '._pth'))
    ldd = Path('/usr/bin/ldd').read_text(); loaders = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    require(ldd.startswith('#!/bin/bash\n') and loaders is not None, 'Unexpected ldd loader configuration')
    optional.update(map(Path, loaders.group(1).split()))
    roots = set(CONFIG_DIRS) | set(LIB_ROOTS) | {STDLIB}
    names = optional | roots
    present = {str(p): {'exists': p.exists(), 'is_file': p.is_file(), 'is_dir': p.is_dir(),
        'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None} for p in sorted(names)}
    directories = {str(p): {str(q): {'exists': q.exists(), 'is_file': q.is_file(), 'is_dir': q.is_dir(),
        'resolved': str(q.resolve()), 'symlink': os.readlink(q) if q.is_symlink() else None}
        for q in sorted(p.rglob('*'))} if p.is_dir() else None for p in CONFIG_DIRS}
    return {'presence': present, 'directories': directories, 'ldd_loaders': loaders.group(1).split(),
            'sysconfig_paths': sysconfig.get_paths(), 'sysconfig_vars': sysconfig.get_config_vars()}


def runtime_names(config):
    names = {str(PYTHON), '/usr/bin/env', '/usr/bin/ldd', '/bin/bash', '/bin/sh'}
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for directory in LIB_ROOTS:
        iterator = directory.glob('*') if directory == Path('/usr/local/lib') else directory.rglob('*')
        names.update(str(p) for p in iterator if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    names.update(p for p, row in config['presence'].items() if row['is_file'])
    for group in config['directories'].values(): names.update(p for p, row in (group or {}).items() if row['is_file'])
    return names


def map_paths(data):
    return sorted({str(Path(parts[5]).resolve()) for line in data.splitlines()
        if len(parts := line.split(None, 5)) == 6 and parts[5].startswith('/')})


def parent_observation(phase):
    require(dict(os.environ) == ENV, 'Parent actual environment no longer equals ENV4; mismatching values are not recorded')
    modules = {name: {'file': getattr(module, '__file__', None),
        'origin': getattr(getattr(module, '__spec__', None), 'origin', None)} for name, module in sorted(sys.modules.items())}
    maps = Path('/proc/self/maps').read_text()
    return {'phase': phase, 'epoch': time.time(), 'pid': os.getpid(), 'modules': modules,
        'maps': maps, 'mapped_files': map_paths(maps), 'orig_argv': sys.orig_argv,
        'flags': str(sys.flags), 'cwd': str(Path.cwd()), 'env': dict(os.environ), 'executable': sys.executable,
        'sys_path': sys.path, 'pycache_prefix': sys.pycache_prefix,
        'cache_exists': os.path.lexists(sys.pycache_prefix),
        'scope': 'Actual early/late parent module and file-backed raw-map samples, not continuous tracing.'}


def consumed(observation):
    names = set(observation['mapped_files'])
    for row in observation.get('modules', {}).values():
        names.update(str(Path(p).resolve()) for p in (row.get('file'), row.get('origin')) if p and p.startswith('/'))
    return names


def group_state(pid, actions):
    try:
        os.killpg(pid, 0)
        state, error = 'PRESENT', None
    except ProcessLookupError:
        state, error = 'ABSENT', None
    except BaseException:
        state, error = 'UNKNOWN', traceback.format_exc()
    actions.append({'epoch': time.time(), 'probe': 'killpg(pid,0)', 'owned_process_group': pid, 'state': state, 'error': error})
    return state


def settle(proc, actions):
    # Only the process group created by this Popen(start_new_session=True).
    # Unknown probes/errors never become affirmative disappearance evidence.
    uncertain = False
    for sig, grace in ((None, 0.0), (signal.SIGTERM, 3.0), (signal.SIGKILL, 3.0)):
        try:
            code = proc.poll(); state = group_state(proc.pid, actions)
            if code is not None and state == 'ABSENT': return not uncertain
            if state == 'UNKNOWN': uncertain = True
            if sig is not None and state == 'PRESENT':
                try:
                    os.killpg(proc.pid, sig)
                    actions.append({'epoch': time.time(), 'signal': int(sig), 'outcome': 'SENT_TO_OWNED_GROUP'})
                except ProcessLookupError:
                    actions.append({'epoch': time.time(), 'signal': int(sig), 'outcome': 'GROUP_ALREADY_ABSENT'})
                except BaseException:
                    uncertain = True; actions.append({'epoch': time.time(), 'signal': int(sig), 'error': traceback.format_exc()})
            deadline = time.monotonic() + grace
            while time.monotonic() < deadline:
                code = proc.poll(); state = group_state(proc.pid, actions)
                if state == 'UNKNOWN': uncertain = True
                if code is not None and state == 'ABSENT': return not uncertain
                time.sleep(0.05)
        except BaseException:
            uncertain = True; actions.append({'epoch': time.time(), 'error': traceback.format_exc()})
    try:
        proc.wait(timeout=1)
    except BaseException:
        uncertain = True; actions.append({'epoch': time.time(), 'reap_error': traceback.format_exc()})
    final = group_state(proc.pid, actions)
    actions.append({'epoch': time.time(), 'final_group_state': final, 'leader_returncode': proc.returncode})
    return not uncertain and proc.returncode is not None and final == 'ABSENT'


def native_child(row, samples):
    global PROC, SPAWN_ATTEMPTED, SPAWNING
    save(OUT / 'PRE_SPAWN_ATTEMPT.json', row)
    with (OUT / 'checker.stdout').open('xb') as stdout, (OUT / 'checker.stderr').open('xb') as stderr:
        SPAWN_ATTEMPTED = True
        SPAWNING = True
        try:
            PROC = subprocess.Popen(row['argv'], cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL,
                stdout=stdout, stderr=stderr, start_new_session=True)
            row.update(pid=PROC.pid, process_group=PROC.pid, outcome='RUNNING')
            save(OUT / 'SPAWNED.json', {'pid': PROC.pid, 'process_group': PROC.pid, 'epoch': time.time(),
                'argv': row['argv'], 'start_new_session': True})
        finally:
            SPAWNING = False
        if DEFERRED_SIGNAL is not None: interrupted(DEFERRED_SIGNAL, None)
        deadline = time.monotonic() + TIMEOUT_SECONDS
        next_heartbeat = time.monotonic() + HEARTBEAT_SECONDS
        while PROC.poll() is None:
            try:
                raw_maps = Path('/proc/' + str(PROC.pid) + '/maps').read_text()
                item = {'epoch': time.time(), 'pid': PROC.pid, 'maps': raw_maps, 'mapped_files': map_paths(raw_maps)}
                if samples['first'] is None: samples['first'] = item
                samples['last'] = item; samples['successful_samples'] += 1
            except Exception:
                samples['sample_errors'].append({'epoch': time.time(), 'error': traceback.format_exc()})
            current = time.monotonic()
            if current >= next_heartbeat:
                event = {'epoch': time.time(), 'pid': PROC.pid, 'status': 'FOUR_COMPONENT_NATIVE_RUNNING'}
                row['heartbeats'].append(event)
                print(json.dumps(event, sort_keys=True), flush=True)
                next_heartbeat = current + HEARTBEAT_SECONDS
            if current >= deadline:
                row['outcome'] = 'TIMED_OUT'; break
            time.sleep(SAMPLE_INTERVAL_SECONDS)
        if row['outcome'] == 'RUNNING': row['outcome'] = 'COMPLETED'


def seal_output():
    entries = list(OUT.rglob('*'))
    require(all(not p.is_symlink() for p in entries), 'Output symlink detected')
    paths = sorted(p for p in entries if p.is_file())
    require(not (OUT / 'SHA256SUMS').exists(), 'Never replace an output seal')
    data = ''.join(pin(p)['sha256'] + '  ' + p.relative_to(OUT).as_posix() + '\n' for p in paths)
    raw_save(OUT / 'SHA256SUMS', data.encode())
    return {'manifest': pin(OUT / 'SHA256SUMS'), 'payloads': len(paths)}


def main():
    global PHASE
    require(len(sys.argv) == 3 and sys.argv[1] == 'launch-four-completed-component' and
            re.fullmatch(r'[0-9a-f]{64}', sys.argv[2]), 'Require exact launcher mode and own preparation digest')
    require(Path(__file__) == PREP / 'launcher.py' and Path.cwd() == ROOT and Path(sys.executable).resolve() == PYTHON and
            dict(os.environ) == ENV and sys.flags.isolated == sys.flags.no_site == 1 and
            sys.flags.optimize == 0 and sys.dont_write_bytecode and sysconfig.get_path('stdlib') == str(STDLIB),
            'Require exact prepared source, cwd, ENV4 and system Python -I -S -B; inherited environment is not recorded')
    require(sys.path == ['/usr/lib/python310.zip', str(STDLIB), str(STDLIB / 'lib-dynload')], 'Unexpected isolated source-only search path')
    require(not os.path.lexists('/usr/lib/python310.zip') and not os.path.lexists('/etc/ld.so.preload'),
            'Unexpected interpreter zip or loader preload injection')
    require(sys.pycache_prefix == str(OUT / 'unused_launcher_cache') and not os.path.lexists(sys.pycache_prefix) and
            not os.path.lexists(OUT / 'unused_checker_cache'), 'Require separate exact absent cache roles')
    require(OUT.parent.resolve() == OUT.parent and not os.path.lexists(OUT), 'Refuse existing or aliased output')
    own_seal = sys.argv[2]; OUT.mkdir(mode=0o700)
    save(OUT / 'LAUNCHER_ATTEMPT.json', {'epoch': time.time(), 'orig_argv': sys.orig_argv, 'cwd': str(ROOT),
        'env': ENV, 'flags': str(sys.flags), 'pycache_prefix': sys.pycache_prefix, 'output': str(OUT),
        'expected_launcher_preparation_sha256': own_seal, 'checker_preparation_sha256': CHECKER_SEAL})
    row = {'argv': [str(PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(OUT / 'unused_checker_cache'),
        str(CHECKER), '--expected-preparation-sha256', CHECKER_SEAL,
        '--reuse-root-binding', str(ROOT_BINDING), '--reuse-root-binding-sha256', ROOT_BINDING_SHA], 'cwd': str(ROOT), 'env': ENV,
        'stdin': 'DEVNULL', 'stdout': 'checker.stdout', 'stderr': 'checker.stderr', 'start_new_session': True,
        'timeout_seconds': TIMEOUT_SECONDS, 'heartbeat_seconds': HEARTBEAT_SECONDS, 'heartbeats': [],
        'started_epoch': None, 'exit': None, 'outcome': 'NOT_STARTED', 'cleanup': []}
    failures, before, scoped_before, config_before, names_before, extra = [], None, None, None, None, set()
    parent_before, child_samples = None, None
    try:
        PHASE = 'baseline'
        scoped_before = scoped_inputs(own_seal); save(OUT / 'SCOPED_INPUTS_BEFORE.json', scoped_before)
        config_before = configuration(); save(OUT / 'CONFIGURATION_BEFORE.json', config_before)
        require(all(not row['exists'] and row['symlink'] is None for name, row in config_before['presence'].items()
                    if name.endswith(('._pth', '/pyvenv.cfg'))), 'Unexpected interpreter path-injection file')
        parent_before = parent_observation('BEFORE_KNOWN_KEY_AND_CHILD'); save(OUT / 'PARENT_BEFORE.json', parent_before)
        names_before = runtime_names(config_before); extra = consumed(parent_before)
        require(not any(p.endswith(('.pyc', '.pyo')) for p in extra), 'Parent bytecode observation')
        before = pins(names_before | extra | set().union(*(set(v) for v in scoped_before.values())))
        compressed_ledger('KNOWN_INPUTS_BEFORE', before)
        for source in (PREP / 'launcher.py', CHECKER):
            data = source.read_bytes(); require(hashlib.sha256(data).hexdigest() == before[str(source)]['sha256'], 'Source copy raced')
            raw_save(OUT / ('executed_' + source.name), data)
        PHASE = 'native_child'; row['started_epoch'] = time.time()
        child_samples = {'first': None, 'last': None, 'successful_samples': 0, 'sample_errors': [],
            'interval_seconds': SAMPLE_INTERVAL_SECONDS,
            'scope': 'Only first and last successful sampled /proc/PID/maps are retained. Intermediate samples were replaced, not a continuous trace.'}
        native_child(row, child_samples)
    except BaseException:
        failures.append({'phase': PHASE, 'error': traceback.format_exc()})
        if SPAWN_ATTEMPTED and PROC is None: row['outcome'] = 'SPAWN_ATTEMPT_WITHOUT_RETURNED_HANDLE'
        elif PROC is not None and row['outcome'] != 'TIMED_OUT': row['outcome'] = 'INTERRUPTED_OR_EXCEPTION'
    settled = not SPAWN_ATTEMPTED
    if PROC is not None:
        try: settled = settle(PROC, row['cleanup'])
        except BaseException:
            settled = False; failures.append({'phase': 'settling', 'error': traceback.format_exc()})
        row['exit'] = PROC.returncode
    row.update(finished_epoch=time.time(), process_group_settled=settled, spawn_attempted=SPAWN_ATTEMPTED)
    save(OUT / 'NATIVE_RESULT.json', row)
    if child_samples is not None: save(OUT / 'CHILD_MAP_SAMPLES.json', child_samples)
    if not settled:
        save(OUT / 'UNCLOSED.json', {'status': 'UNCLOSED_NO_SETTLED_HASHES_OR_SEAL', 'native': row, 'failures': failures})
        print(json.dumps({'status': 'UNCLOSED_NO_SETTLED_HASHES_OR_SEAL', 'output': str(OUT), 'exit': row['exit']}, sort_keys=True))
        return 1
    # No stream hashes or final seal are computed until the owned group is gone.
    streams = {}
    for name in ('checker.stdout', 'checker.stderr'):
        if (OUT / name).is_file():
            try: streams[name] = pin(OUT / name)
            except BaseException:
                streams[name] = {'read_error': traceback.format_exc()}; failures.append({'phase': 'settled_stream_pin', 'name': name, **streams[name]})
    after, scoped_after, config_after, names_after, parent_after, parsed = None, None, None, None, None, None
    for phase, action in (
        ('scoped_after', lambda: {group: pins(values, tolerant=True) for group, values in (scoped_before or {}).items()}),
        ('configuration_after', configuration),
        ('parent_after', lambda: parent_observation('AFTER_CHILD_AND_SETTLING'))):
        try:
            value = action()
            if phase == 'scoped_after': scoped_after = value; save(OUT / 'SCOPED_INPUTS_AFTER.json', value)
            elif phase == 'configuration_after': config_after = value; save(OUT / 'CONFIGURATION_AFTER.json', value)
            else: parent_after = value; save(OUT / 'PARENT_AFTER.json', value)
        except BaseException: failures.append({'phase': phase, 'error': traceback.format_exc()})
    try:
        require(scoped_inputs(own_seal) == scoped_after, 'Complete after preparation/fixed-input semantic validation failed')
    except BaseException: failures.append({'phase': 'after_preparation_validation', 'error': traceback.format_exc()})
    try:
        names_after = runtime_names(config_after) if config_after is not None else set()
        current_names = names_after | extra | (set(before) if before is not None else set())
        after = pins(current_names, tolerant=True); compressed_ledger('KNOWN_INPUTS_AFTER', after)
        require(before is not None and after == before and names_before == names_after, 'Complete known runtime/input bytes or membership changed')
        require(scoped_before == scoped_after and config_before == config_after, 'Preparation/fixed input/configuration key changed')
        require(parent_after is not None and not parent_after['cache_exists'], 'Parent final observation/cache missing or changed')
        require(all(parent_before[k] == parent_after[k] for k in ('env', 'flags', 'cwd', 'executable', 'sys_path', 'pycache_prefix')),
                'Actual parent runtime/isolation settings changed')
        known = {v['resolved'] for v in before.values()}
        parent_used = consumed(parent_before) | consumed(parent_after)
        require(parent_used <= known and not any(p.endswith(('.pyc', '.pyo')) for p in parent_used), 'Parent sampled source/runtime closure failed')
        require(child_samples is not None and child_samples['first'] is not None and child_samples['last'] is not None,
                'No actual retained first/last child map samples')
        child_used = set(child_samples['first']['mapped_files']) | set(child_samples['last']['mapped_files'])
        require(child_used <= known and not any(p.endswith(('.pyc', '.pyo')) for p in child_used), 'Child retained map coverage failed')
        require(not os.path.lexists(OUT / 'unused_checker_cache') and not os.path.lexists(OUT / 'unused_launcher_cache'), 'Source-only cache role was created')
        parsed = json.loads((OUT / 'checker.stdout').read_bytes())
        require(row['exit'] == 0 and row['outcome'] == 'COMPLETED' and streams['checker.stderr']['bytes'] == 0 and
                not any('signal' in item for item in row['cleanup']) and
                parsed['status'] == 'FOUR_COMPLETED_COMPONENT_PASS_P210_NOT_ASSESSED_NOT_FIVE_PAPER_PASS' and
                parsed['papers_checked'] == ['P205', 'P207', 'P208', 'P209'] and
                parsed['prior_completed_papers'] == 4 and parsed['p210_accepted_by_this_component'] is False and
                parsed['required_final_five'] == ['P205', 'P207', 'P208', 'P209', 'P210'] and
                parsed['current_valid_author_A_B_pairs'] == 12 and parsed['current_valid_source_only_builds'] == 8 and
                parsed['actual_prior_page_attestations_bound'] == 21 and parsed['five_contract_ceilings_checked'] == 5 and
                all(parsed[key] == 0 for key in ('new_scientific_executions', 'new_builds', 'new_page_views',
                    'new_reviews', 'old_auditors_or_writers_executed', 'files_written')) and
                parsed['owner'] == 'OWNER_AMBER' and parsed['external'] == 'HOLD_EXTERNAL',
                'Native result does not establish the exact read-only FOUR-paper component boundary')
    except BaseException: failures.append({'phase': 'final_closure', 'error': traceback.format_exc()})
    status = 'PASS_NATIVE_FOUR_COMPLETED_COMPONENT_NOT_FIVE_PAPER_ACCEPTANCE' if not failures else 'FAIL_PRESERVED'
    receipt = {'status': status, 'native': row, 'streams': streams, 'failures': failures,
        'known_inputs_unchanged': before is not None and before == after, 'runtime_membership_unchanged': names_before is not None and names_before == names_after,
        'scoped_inputs_unchanged': scoped_before is not None and scoped_before == scoped_after,
        'configuration_unchanged': config_before is not None and config_before == config_after,
        'checker_json_status': parsed.get('status') if isinstance(parsed, dict) else None,
        'complete_checker_json': 'checker.stdout' if 'checker.stdout' in streams else None,
        'scientific_executions': 0, 'builds': 0, 'page_views': 0, 'new_reviews': 0,
        'p210_accepted': False, 'five_paper_acceptance': False, 'owner': 'OWNER_AMBER', 'external': 'HOLD_EXTERNAL',
        'boundary': 'One actual direct read-only FOUR-completed-paper component. Known source/runtime/configuration before/after keys and retained parent/child samples only; no OS reconstruction or continuous trace. P210 and full five-paper acceptance remain separate.'}
    save(OUT / 'RECEIPT.json', receipt); closure = seal_output()
    print(json.dumps({'status': status, 'output': str(OUT), 'checker_exit': row['exit'],
        'checker_json_status': receipt['checker_json_status'], 'output_seal': closure}, sort_keys=True))
    return 0 if not failures else 1


if __name__ == '__main__':
    old_handlers = {sig: signal.signal(sig, interrupted) for sig in (signal.SIGTERM, signal.SIGINT)}
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except BaseException:
        # Actual outer tool stdout retains this if storage/guard handling fails.
        # Never fabricate a seal, child exit or inherited-environment dump.
        print(json.dumps({'status': 'LAUNCHER_EXCEPTION_NO_ACCEPTANCE', 'phase': PHASE,
            'output': str(OUT), 'error': traceback.format_exc()}, sort_keys=True))
        raise SystemExit(1)
    finally:
        for sig, handler in old_handlers.items(): signal.signal(sig, handler)
