#!/usr/bin/env python3
"""P210 outer capture revision 02; actual whole-gate preflight binding.

Only paths/documentation and final_builder_binding change from revision 01.
Preparation never imports or executes task source or views a paper page.
Root must read this complete source and actual preparation before launch.
"""
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_terminal_launch_revision_02'
SCRIPT = PREP / 'launch_p210_terminal.py'
BUILDER_PREP = QA / 'p210_terminal_build_revision_02'
BUILDER = BUILDER_PREP / 'build_p210.py'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
BUILD_OUT = PAPER / 'qa_final'
OUT = QA / 'p210_terminal_launch_02'
CACHE = OUT / 'unused_outer_cache'
PYTHON = '/usr/bin/python3.10'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC',
       'SOURCE_DATE_EPOCH': '1704067200', 'FORCE_SOURCE_DATE': '1',
       'openin_any': 'p', 'openout_any': 'p'}
SEARCH_PATH = ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload']
TIMEOUT = 21600


def require(value, label):
    if not value:
        raise RuntimeError(label)


def pin(path):
    path = Path(path)
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return {'sha256': digest.hexdigest(), 'bytes': path.stat().st_size}


def save(path, value):
    raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with Path(path).open('xb') as stream:
        stream.write(raw)


def manifest(base, expected=None, count=None):
    require(base.resolve() == base and not base.is_symlink(), 'Aliased sealed package')
    seal = base / 'SHA256SUMS'
    seal_pin = pin(seal)
    require(expected is None or seal_pin['sha256'] == expected, 'Preparation seal changed')
    pins = {}
    for row in seal.read_text().splitlines():
        digest, name = row.split('  ', 1)
        relative, path = Path(name), base / name
        require(len(digest) == 64 and set(digest) <= set('0123456789abcdef') and
                relative.as_posix() == name and relative.parts and not relative.is_absolute() and
                '..' not in relative.parts and name != 'SHA256SUMS' and str(path) not in pins,
                'Unsafe, duplicate or self manifest member')
        require(path.resolve() == path and not path.is_symlink() and path.is_file(), 'Nonphysical payload')
        pins[str(path)] = pin(path)
        require(pins[str(path)]['sha256'] == digest, 'Changed payload: ' + name)
    entries = list(base.rglob('*'))
    require(not any(p.is_symlink() for p in entries) and set(pins) ==
            {str(p) for p in entries if p.is_file() and p != seal}, 'Incomplete nonself manifest')
    require(count is None or len(pins) == count, 'Changed complete payload count')
    return {**pins, str(seal): seal_pin}


def final_builder_binding():
    """Bind actual whole-gate preflight, raw capture and root native originals.

    The builder alone owns its B/root/Round2 semantic gate. No task source is
    imported or invoked here; the complete actual input map is reread by main.
    """
    seal = '2e99af39ab35bfb9e3fec7c9944927c574fe459b56a1b764a5948dde0266e31a'
    required = manifest(BUILDER_PREP, seal, 9)
    capture = QA / 'p210_terminal_preflight_02'
    raw_result = (capture / 'RESULT.json').read_bytes()
    result = json.loads(raw_result)
    require(type(result['pid']) is int and result['pid'] == 777535 and
            type(result['original_wait_exit_code']) is int and result['original_wait_exit_code'] == 0 and
            result['cleanup_wait_exit_code'] == 0 and result['timed_out'] is False and
            result['wait_error'] is None and result['cleanup_events'] == [] and
            result['child_reaped'] is True and result['process_group_absent'] is True and
            group_absent(result['pid']) and not os.path.lexists(capture / 'UNCLOSED.json'),
            'Actual preflight normal-zero/reaped/absent before capture hashing')
    required.update(manifest(capture, 'd6adc396a8562e8683f66df348aa420ce3f97997b4bf73c0c674f621aac7fb1c', 6))
    require(required[str(capture / 'RESULT.json')] == {
        'sha256': hashlib.sha256(raw_result).hexdigest(), 'bytes': len(raw_result)}, 'Same checked preflight RESULT')
    extras = {
        'record_p210_terminal_preflight_02.py': ('275be1480ee7dedb67abae5215c47189f70beb4cb50ec8f0dfbc3c33e767ba26', 6228),
        'P210_TERMINAL_PREFLIGHT02_ROOT_LAUNCH.actual.json': ('2359f6160563c5e7c4cbed780ea52274fc7cdc3881029cbf866b858aa338ab33', 457),
        'P210_TERMINAL_PREFLIGHT02_ROOT_COMPLETION.actual.json': ('74d231e8fe72bc58427a2a88896af7e405291f918beeed214cdbb85cfe149673', 958),
        'P210_TERMINAL_PREFLIGHT02_ROOT_RECEPTION.actual.json': ('3c0d42a85bf09fe6b42dcd06cad13193b748f31d069cb4a92cffe11460d1c422', 4624)}
    for name, (digest, size) in extras.items():
        required[str(QA / name)] = pin(QA / name)
        require(required[str(QA / name)] == {'sha256': digest, 'bytes': size}, 'Exact actual preflight original: ' + name)
    recorder = QA / 'record_p210_terminal_preflight_02.py'
    launch = json.loads((QA / 'P210_TERMINAL_PREFLIGHT02_ROOT_LAUNCH.actual.json').read_bytes())
    completion = json.loads((QA / 'P210_TERMINAL_PREFLIGHT02_ROOT_COMPLETION.actual.json').read_bytes())
    reception = json.loads((QA / 'P210_TERMINAL_PREFLIGHT02_ROOT_RECEPTION.actual.json').read_bytes())
    require(launch['command'] == PYTHON + ' -I -S -B ' + str(recorder) +
            ' --expected-builder-preparation-sha256 ' + seal and launch['cwd'] == str(ROOT) and
            launch['result']['chunk_id'] == '25035d' and launch['result']['session_id'] == 78288 and
            launch['result']['output'] == '' and completion['session_id'] == 78288 and
            completion['launch_record'] == 'P210_TERMINAL_PREFLIGHT02_ROOT_LAUNCH.actual.json' and
            completion['result']['chunk_id'] == '11728b' and completion['result']['exit_code'] == 0,
            'Actual root recorder launch/completion chain')
    attempt = json.loads((capture / 'ATTEMPT.json').read_bytes())
    spawn = json.loads((capture / 'SPAWN.json').read_bytes())
    argv = [PYTHON, '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(BUILD_OUT / 'unused_parent_cache'),
            str(BUILDER), '--output', str(BUILD_OUT), '--expected-preparation-sha256', seal, '--preflight-only']
    require(result['argv'] == attempt['argv'] == argv and result['cwd'] == attempt['cwd'] == str(ROOT) and
            result['environment'] == attempt['environment'] == ENV and attempt['timeout_seconds'] == 600 and
            attempt['start_new_session'] is True and attempt['paper_terminal_absent_before'] is True and
            result['paper_terminal_absent_after'] is True and result['inputs_unchanged'] is True and
            spawn['pid'] == spawn['process_group_id'] == result['pid'] and
            attempt['started_epoch'] <= spawn['spawned_epoch'] <= result['finished_epoch'] and
            result['inputs_before'] == result['inputs_after'] == attempt['inputs_before'],
            'Actual complete preflight invocation and stable recorder inputs')
    recorder_inputs = result['inputs_before']
    require(set(recorder_inputs) == {str(recorder), str(BUILDER), str(BUILDER_PREP / 'INPUT_CONTRACT.json'),
            str(BUILDER_PREP / 'SHA256SUMS'), PYTHON} and
            (capture / 'executed_source.py').read_bytes() == recorder.read_bytes(), 'Exact executed recorder/source roles')
    data = json.loads((capture / 'stdout').read_bytes())
    require(all(result[name] == required[str(capture / name)] for name in ('stdout', 'stderr')) and
            (capture / 'stderr').read_bytes() == b'' and data['status'] == 'PASS_P210_FINAL_SCHEMA_PREFLIGHT_ONLY' and
            data['source'] == required[str(BUILDER)] and data['preparation_seal'] == required[str(BUILDER_PREP / 'SHA256SUMS')] and
            data['output'] == str(BUILD_OUT) and data['output_created'] is False and
            data['child_commands'] == data['host_inventory_collections'] == data['new_science_build_view_executions'] == 0 and
            data['terminal_acceptance'] is False and data['original_input_count'] == len(data['original_input_pins']) == 1619,
            'Full actual raw preflight source/seal/map and zero-execution scope')
    final = data['final_schema_binding_return']
    recipe = json.loads((BUILDER_PREP / 'INPUT_CONTRACT.json').read_bytes())
    require(final['status'] == 'BOUND_ACTUAL_P210_B_ROOT_ROUND2_PRETERMINAL_ORIGINALS' and
            set(final['papers']) == {'P210'} and final['papers'] == recipe['final_schema_binding']['papers'] and
            len(final['required_input_pins']) == 1594 and
            all(data['original_input_pins'].get(path) == value for path, value in final['required_input_pins'].items()),
            'Actual complete final-schema return and required-map subset, not repeated semantic gate')
    require(json.loads(completion['result']['output']) == {
        'status': 'PASS_ACTUAL_P210_PREFLIGHT_CAPTURE', 'output': str(capture), 'original_wait_exit_code': 0,
        'stdout': result['stdout'], 'stderr': result['stderr'], 'result': required[str(capture / 'RESULT.json')],
        'seal': required[str(capture / 'SHA256SUMS')], 'original_input_count': 1619, 'terminal_acceptance': False},
        'Exact reconstructed native recorder summary from full raw originals')
    require(reception['cwd'] == str(ROOT) and reception['result']['chunk_id'] == 'dd97dc' and
            reception['result']['exit_code'] == 0 and json.loads(reception['result']['output']) == {
        'status': 'PASS_ROOT_ACTUAL_PREFLIGHT02_FULL_RAW_ORIGINAL_RECEPTION', 'actual_parent_session': 78288,
        'original_wait_exit_code': 0, 'builder_pid': result['pid'], 'owned_group_currently_absent': True,
        'all_actual_input_pins_rehashed': 1619, 'full_final_binding_required_pins': 1594,
        'complete_raw_stdout': result['stdout'], 'complete_raw_stderr': result['stderr'],
        'complete_capture_payloads': 6, 'capture_seal': required[str(capture / 'SHA256SUMS')],
        'qa_final_absent': True, 'new_scientific_build_or_visual_executions': 0, 'terminal_acceptance': False},
        'Exact actual root full-raw reception, not another confirmation layer')
    for mapping in (recorder_inputs, data['original_input_pins']):
        for path, value in mapping.items():
            require(path not in required or required[path] == value, 'Conflicting actual preflight input pin')
            required[path] = value
    return {'preparation_sha256': seal, 'preparation_payloads': 9, 'required_input_pins': required}


def runtime(phase):
    modules = {}
    for name, module in sorted(sys.modules.items()):
        value = getattr(module, '__file__', None)
        if value and Path(value).is_file():
            path = Path(value).resolve()
            require(path.suffix not in {'.pyc', '.pyo'}, 'Launcher consumed bytecode')
            modules[name] = {'path': str(path), **pin(path)}
    maps = Path('/proc/self/maps').read_bytes()
    mapped = {}
    for line in maps.decode().splitlines():
        parts = line.split(None, 5)
        if len(parts) == 6 and parts[5].startswith('/'):
            path = Path(parts[5]).resolve()
            mapped[str(path)] = pin(path)
    require(dict(os.environ) == ENV and sys.path == SEARCH_PATH and not os.path.lexists(CACHE),
            'Launcher environment/path/cache changed')
    return {'phase': phase, 'modules': modules, 'maps_raw': maps.decode(), 'mapped_files': mapped,
            'orig_argv': sys.orig_argv, 'flags': str(sys.flags), 'cwd': str(Path.cwd()),
            'environment': dict(os.environ), 'executable': sys.executable, 'sys_path': sys.path,
            'cache_prefix': sys.pycache_prefix, 'cache_absent': True,
            'scope': 'Only early/late own modules and file-backed maps; no host-tree inventory, OS/startup or child trace.'}


def observed_pins(value):
    return {**value['mapped_files'], **{v['path']: {k: v[k] for k in ('sha256', 'bytes')}
                                      for v in value['modules'].values()}}


def group_absent(pid):
    try:
        os.killpg(pid, 0)
    except ProcessLookupError:
        return True
    return False


def interrupted(signum, frame):
    raise KeyboardInterrupt('Outer received signal ' + str(signum))


def settle(proc, row):
    """Never overwrite original_wait_* with cleanup return codes.

    SIGINT lets the builder's own BaseException handler close commands that
    use their own sessions. SIGKILL here owns only the builder group; it does
    not prove detached command closure. Any cleanup forbids a success seal.
    """
    row['cleanup_events'] = []
    row['cleanup_exit_code'] = None
    if proc is None:
        row['builder_reaped'] = False
        row['builder_group_absent'] = None
        return False
    try:
        if not group_absent(proc.pid):
            for sig, seconds in ((signal.SIGINT, 30), (signal.SIGKILL, 10)):
                event = {'signal': int(sig), 'wait_seconds': seconds, 'started_epoch': time.time()}
                row['cleanup_events'].append(event)
                try:
                    os.killpg(proc.pid, sig)
                except ProcessLookupError:
                    event['group_already_absent'] = True
                deadline = time.monotonic() + seconds
                while time.monotonic() < deadline:
                    proc.poll()
                    if group_absent(proc.pid):
                        break
                    time.sleep(0.1)
                event['group_absent_after'] = group_absent(proc.pid)
                if event['group_absent_after']:
                    break
        row['cleanup_exit_code'] = proc.wait(timeout=10)
        row['builder_reaped'] = True
        row['builder_group_absent'] = group_absent(proc.pid)
    except BaseException:
        row['cleanup_error'] = traceback.format_exc()
        row['builder_reaped'] = proc.returncode is not None
        row['builder_group_absent'] = None
    return row['builder_reaped'] and row['builder_group_absent'] is True


def builder_closure():
    result_raw = (BUILD_OUT / 'RESULT.json').read_bytes()
    result = json.loads(result_raw)
    labels = ['source_cmp', 'ldd_before', 'pdflatex_version', 'bibtex_version', 'texmf_roots', 'P210_round2_pdfinfo']
    for number in (1, 2):
        stem = 'P210_cold_build_' + str(number)
        labels.extend(stem + '_' + name for name in ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR', 'pass1',
            'bst', 'bibtex', 'pass2', 'pass3', 'pdfinfo', 'pdffonts', 'pdftotext', 'frozen_cmp'))
        if number == 1:
            labels.append(stem + '_render')
    labels += ['P210_pair_cmp', 'ldd_after']
    require(result['status'] == 'PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED' and
            result['failures'] == [] and len(result['builds']) == 2 and len(result['commands']) == 33 and
            result['expected_command_count'] == 33 and result['expected_command_labels'] == labels and
            [row['label'] for row in result['commands']] == labels and
            result['visual_review'] == 'NOT_VIEWED_ROOT_ACTUAL_PAGE_INSPECTION_REQUIRED' and
            all(build['visual_review'] == 'NOT_VIEWED' for build in result['builds']) and
            result['paper_completion'] is False and result['five_paper_completion'] is False,
            'Builder RESULT does not describe the exact closed unviewed pair')
    for command in result['commands']:
        require(command['status'] == 'COMPLETED' and type(command['exit_code']) is int and
                command['exit_code'] == 0 and command['error'] is None and command['streams_settled'] is True and
                command['start_new_session'] is True and command['timeout_seconds'] == 600 and
                'cleanup' not in command and type(command['pid']) is int and command['pid'] > 0 and
                group_absent(command['pid']), 'Builder native command not successfully closed')
    require(not os.path.lexists(BUILD_OUT / 'UNCLOSED.json'), 'Unclosed builder evidence present')
    # Only closed recorded command groups may precede any builder payload hash.
    pins = manifest(BUILD_OUT)
    require(pins[str(BUILD_OUT / 'RESULT.json')] == {
        'sha256': hashlib.sha256(result_raw).hexdigest(), 'bytes': len(result_raw)},
        'Verified manifest binds the exact RESULT bytes checked before hashing')
    return {'manifest': pins[str(BUILD_OUT / 'SHA256SUMS')], 'payloads': len(pins) - 1,
            'result': pins[str(BUILD_OUT / 'RESULT.json')], 'status': result['status']}


def main():
    require(sys.argv[1:2] == ['--expected-preparation-sha256'] and len(sys.argv) == 3,
            'Require exact launcher preparation-seal argument')
    require(Path(__file__) == SCRIPT and SCRIPT.resolve() == SCRIPT and Path.cwd() == ROOT and
            sys.executable == PYTHON and Path(PYTHON).resolve() == Path(PYTHON), 'Exact launcher/interpreter/cwd')
    require(dict(os.environ) == ENV and sys.flags.isolated == 1 and sys.flags.no_site == 1 and
            sys.flags.optimize == 0 and sys.dont_write_bytecode and sys.path == SEARCH_PATH and
            sys.pycache_prefix == str(CACHE) and not os.path.lexists(CACHE), 'Exact isolated source-only settings')
    require(sys.orig_argv == [PYTHON, '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(CACHE),
            str(SCRIPT), '--expected-preparation-sha256', sys.argv[2]], 'Exact outer argv')
    for path in (OUT, BUILD_OUT):
        require(path.resolve() == path and not os.path.lexists(path), 'Refuse aliased/existing output or retry')
    binding = final_builder_binding()
    before = manifest(PREP, sys.argv[2])
    before.update(manifest(BUILDER_PREP, binding['preparation_sha256'], binding['preparation_payloads']))
    for name, expected in binding['required_input_pins'].items():
        path = Path(name)
        require(path.is_absolute() and path.resolve() == path and not path.is_symlink() and pin(path) == expected,
                'Actual final builder original changed: ' + name)
        require(name not in before or before[name] == expected, 'Conflicting actual preparation/original pin')
        before[name] = expected
    require(str(BUILDER) in before and str(SCRIPT) in before, 'Full actual builder and launcher preparations required')
    early = runtime('BEFORE_BUILDER_AND_OUTPUT_CREATION')
    for name, value in observed_pins(early).items():
        require(name not in before or before[name] == value, 'Conflicting own observed runtime pin')
        before[name] = value
    before[PYTHON] = pin(PYTHON)
    require(all(pin(path) == value for path, value in before.items()), 'Complete immediate preflight reread')
    OUT.mkdir(mode=0o700)
    save(OUT / 'INPUTS_BEFORE.json', before)
    save(OUT / 'LAUNCHER_RUNTIME_BEFORE.json', early)
    save(OUT / 'executed_launcher.py', SCRIPT.read_bytes())
    save(OUT / 'executed_builder.py', BUILDER.read_bytes())
    require(pin(OUT / 'executed_launcher.py') == before[str(SCRIPT)] and
            pin(OUT / 'executed_builder.py') == before[str(BUILDER)], 'Pre-pinned executed source copies')
    argv = [PYTHON, '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(BUILD_OUT / 'unused_parent_cache'),
            str(BUILDER), '--output', str(BUILD_OUT), '--expected-preparation-sha256', binding['preparation_sha256']]
    row = {'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'started_epoch': time.time(),
           'timeout_seconds': TIMEOUT, 'start_new_session': True, 'original_wait_outcome': 'NOT_STARTED',
           'original_wait_exit_code': None, 'original_wait_exception': None,
           'stdout': 'builder.stdout', 'stderr': 'builder.stderr', 'outer_native_exit': None,
           'outer_native_scope': 'Unknown here. Root must archive the actual tool completion separately.'}
    save(OUT / 'PRE_SPAWN_ATTEMPT.json', row)
    proc = None
    try:
        signal.signal(signal.SIGTERM, interrupted)
        signal.signal(signal.SIGHUP, interrupted)
        with (OUT / 'builder.stdout').open('xb') as stdout, (OUT / 'builder.stderr').open('xb') as stderr:
            proc = subprocess.Popen(argv, cwd=ROOT, env=ENV, stdout=stdout, stderr=stderr, start_new_session=True)
            row['pid'] = proc.pid
            save(OUT / 'SPAWNED.json', {'pid': proc.pid, 'owned_pgid': proc.pid, 'start_new_session': True})
            row['original_wait_exit_code'] = proc.wait(timeout=TIMEOUT)
            row['original_wait_outcome'] = 'COMPLETED'
    except BaseException as error:
        row['original_wait_outcome'] = 'TIMED_OUT' if isinstance(error, subprocess.TimeoutExpired) else 'INTERRUPTED_OR_FAILED'
        row['original_wait_exception'] = traceback.format_exc()
    settled = settle(proc, row)
    closure, failure = None, None
    if (settled and row['original_wait_outcome'] == 'COMPLETED' and
            row['original_wait_exit_code'] == 0 and not row['cleanup_events']):
        try:
            closure = builder_closure()
        except BaseException:
            failure = traceback.format_exc()
    if closure is None:
        row.update(status='UNCLOSED_OR_FAILED_NO_SEAL', failure=failure, finished_epoch=time.time(),
                   streams_hashed=False, scope='All raw evidence retained; no final stream hashes/seal, retries, cleanup deletion or inferred child closure.')
        save(OUT / 'UNCLOSED.json', row)
        print(json.dumps({'status': row['status'], 'output': str(OUT), 'original_wait_exit_code': row['original_wait_exit_code']}, sort_keys=True))
        return 1
    after, late_closed = None, False
    failures = []
    try:
        after = {path: pin(path) for path in before}
        save(OUT / 'INPUTS_AFTER.json', after)
        require(after == before, 'Pinned inputs changed')
    except BaseException:
        failures.append({'phase': 'inputs_after', 'exception': traceback.format_exc()})
    try:
        late = runtime('AFTER_CLOSED_BUILDER_AND_INPUT_REREAD')
        save(OUT / 'LAUNCHER_RUNTIME_AFTER.json', late)
        late_closed = all(before.get(path) == value for path, value in observed_pins(late).items())
        require(late_closed, 'Unpinned late own runtime observation')
    except BaseException:
        failures.append({'phase': 'runtime_after', 'exception': traceback.format_exc()})
    row.update(finished_epoch=time.time(), inputs_unchanged=before == after, failures=failures,
               observed_runtime_closed=late_closed, builder_closure=closure,
               streams={name: pin(OUT / name) for name in ('builder.stdout', 'builder.stderr')},
               streams_hashed=True, cache_absent=not os.path.lexists(CACHE), visual_review='NOT_VIEWED')
    okay = not failures and row['cache_absent'] and late_closed and before == after
    row['status'] = 'PASS_P210_OUTER_CAPTURE_NOT_VIEWED' if okay else 'FAIL_PRESERVED'
    save(OUT / 'RECEIPT.json', row)
    paths = sorted(p for p in OUT.rglob('*') if p.is_file())
    save(OUT / 'SHA256SUMS', ''.join(pin(p)['sha256'] + '  ' + p.relative_to(OUT).as_posix() + '\n' for p in paths).encode())
    manifest(OUT)
    print(json.dumps({'status': row['status'], 'output': str(OUT), 'builder_exit_code': row['original_wait_exit_code'],
                      'launcher_seal': pin(OUT / 'SHA256SUMS'), 'builder_closure': closure}, sort_keys=True))
    return 0 if okay else 1


if __name__ == '__main__':
    raise SystemExit(main())
