#!/usr/bin/env python3
"""P210 outer capture revision 01; actual builder/root-preparation binding.

Minimal correction of the sealed first source's manifest ordering defect.
No task program import, execution or page view occurs during preparation.
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
PREP = QA / 'p210_terminal_launch_revision_01'
SCRIPT = PREP / 'launch_p210_terminal.py'
BUILDER_PREP = QA / 'p210_terminal_build_revision_01'
BUILDER = BUILDER_PREP / 'build_p210.py'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
BUILD_OUT = PAPER / 'qa_final'
OUT = QA / 'p210_terminal_launch_01'
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
    """Exact real builder preparation/root gate; never import or call its code.

    The builder owns its eight-package B/root/Round2 preflight. This outer
    binds its entire sealed preparation and actual root/static originals,
    without repeating that gate or expanding any B/host dependency map.
    """
    seal = '37c6e8f996dc693ebd8280faf4705d35db8d04fbc19bb306de264ca56af972e7'
    required = manifest(BUILDER_PREP, seal, 19)
    gate_path = QA / 'P210_TERMINAL_BUILD_PREPARATION_ROOT.actual.json'
    required[str(gate_path)] = pin(gate_path)
    require(required[str(gate_path)] == {
        'sha256': '396f81291143cf2d047767bca23823d04917692923b0033b028c2d227ff2d5ad', 'bytes': 7564},
        'Exact actual root preparation original')
    gate = json.loads(gate_path.read_bytes())
    require(gate['cwd'] == str(ROOT) and gate['launch']['session_id'] == 26258 and
            gate['launch']['output'] == '' and gate['completion']['chunk_id'] == '52c454' and
            type(gate['completion']['exit_code']) is int and gate['completion']['exit_code'] == 0,
            'Actual root preparation native session/completion')
    accepted = json.loads(gate['completion']['output'])
    require(accepted['status'] == 'PASS_ROOT_P210_FINAL_BUILDER_SOURCE_AND_ACTUAL_BINDING_STATIC' and
            accepted['source'] == required[str(BUILDER)] and accepted['source_lines'] == 711 and
            accepted['static_input_keys_rehashed'] == 1610 and accepted['complete_package_count'] == 8 and
            accepted['package_payloads'] == 1560 and accepted['named_roles'] == 41 and
            accepted['exact_original_input_union'] == 1594 and accepted['actual_round2_anchors_raw_compared'] == 14 and
            accepted['actual_static_native_data_equal'] is True and accepted['actual_capture_native_data_equal'] is True and
            accepted['full_source_delta_bytes_equal'] is True and
            accepted['new_builds'] == accepted['views'] == accepted['task_gate_invocations'] == 0,
            'Exact root-read source and bounded actual binding reception')
    names = {'README.md', 'INPUT_CONTRACT.json', 'static_check.py', 'STATIC_CHECK.actual.json',
             'STATIC_NATIVE_RETURN.actual.json', 'ACTUAL_BINDING_BASELINE.actual.json',
             'ACTUAL_BINDING_NATIVE.actual.json', 'SOURCE_DELTA.diff'}
    require(set(accepted['preparation_documents']) == names and
            all(required[str(BUILDER_PREP / name)] == value for name, value in accepted['preparation_documents'].items()),
            'All eight actual root-read preparation document keys')
    recipe = json.loads((BUILDER_PREP / 'INPUT_CONTRACT.json').read_bytes())
    baseline = json.loads((BUILDER_PREP / 'ACTUAL_BINDING_BASELINE.actual.json').read_bytes())
    capture = json.loads((BUILDER_PREP / 'ACTUAL_BINDING_NATIVE.actual.json').read_bytes())
    static = json.loads((BUILDER_PREP / 'STATIC_CHECK.actual.json').read_bytes())
    native = json.loads((BUILDER_PREP / 'STATIC_NATIVE_RETURN.actual.json').read_bytes())
    require(recipe['schema'] == 'p210-terminal-build-actual-bound-contract-v1' and
            recipe['stage'] == 'ACTUAL_B_ROOT_DELTA_PHYSICAL_ROUND2_BOUND_NOT_EXECUTED' and
            set(recipe['final_schema_binding']['papers']) == {'P210'} and
            recipe == baseline['contract'] and baseline['status'] == 'PASS_READ_ONLY_ACTUAL_BINDING_CAPTURE' and
            baseline['checks'] == 8137 and baseline['named_paths_reread_twice'] == 1606 and
            capture['cwd'] == str(ROOT) and capture['launch']['session_id'] == 60603 and
            capture['launch']['output'] == '' and capture['completion']['exit_code'] == 0 and
            json.loads(capture['completion']['output']) == baseline,
            'Actual full baseline/native bytes and bound recipe, not a caller gate')
    require(native['cwd'] == str(ROOT) and native['result']['exit_code'] == 0 and
            json.loads(native['result']['output']) == static and
            static['status'] == 'PASS_P210_ACTUAL_BINDING_AST_AND_DATA_ONLY' and static['checks'] == 6707 and
            static['named_current_inputs_rechecked_twice'] == 1610 and static['source'] == required[str(BUILDER)] and
            static['source_lines'] == 711 and static['builder_gate_old_programs_science_build_view_executions'] == 0 and
            static['host_ledger_entries_expanded'] == 0 and
            static['complete_current_input_pins'][str(BUILDER_PREP / 'INPUT_CONTRACT.json')] ==
            required[str(BUILDER_PREP / 'INPUT_CONTRACT.json')], 'Actual full static/native source and contract binding')
    return {'preparation_sha256': seal, 'preparation_payloads': 19, 'required_input_pins': required}


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
