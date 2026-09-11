#!/usr/bin/env python3
"""Narrow root reception of the ACTUAL successful P208/P209 reuse_02 wrapper.

Read-only: no imports/execution of original checker, launcher or science;
no subprocess, build, rendering, page view, output directory or file writes.
The 3276 parent keys are reread; the child's 136582-path inspection is received
as its actual pinned result, NOT re-expanded into a second full child audit.
Runtime/configuration discovery transcribes the fully read original launcher.
"""
import gzip
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys
import sysconfig
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
HERE = QA / 'p208_p209_reuse_root_preparation'
OUT = QA / 'p208_p209_reuse_02'
FAILED = QA / 'p208_p209_reuse_01'
CHECKER_PREP = QA / 'p208_p209_reuse_revision_01'
LAUNCHER_PREP = QA / 'p208_p209_reuse_launcher_revision_01'
OLD_CHECKER = QA / 'p208_p209_reuse_preparation'
OLD_LAUNCHER = QA / 'p208_p209_reuse_launcher_preparation'
PYTHON = Path('/usr/bin/python3.10')
STDLIB = Path('/usr/lib/python3.10')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
CONFIG_DIRS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/lib/locale/C.utf8', '/etc/profile.d',
    '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv')))
OUTPUT_SEAL = 'a7fbfa8531515b9e6fcd506a0ff12223cc0b92eb059ab012b3d8b604bc8f97e3'
CHECKER_SEAL = 'ac8fe8834360fdb35e70860416a3c7bb2283b8e32f738251ffc5a1acdfc52a46'
LAUNCHER_SEAL = 'ec70465a84e2f701b01c0c46bb05008ce7dbcfe08cde793b9f468db6e6feee47'
CHECKER_SOURCE = '8b38768261afe5bd6db8d769a8209b4aa3daec40119189c953e69c9b20e60ea0'
LAUNCHER_SOURCE = 'a3c818292a05eee0023e0f891f798cd9e7488eb08d2f762bdced94a557d9b742'
CHILD_STATUS = 'PASS_CURRENT_KEYS_REUSED_NOT_NEW_EXECUTIONS_OR_BATCH_ACCEPTANCE'
PARENT_STATUS = 'PASS_NATIVE_READ_ONLY_REUSE_LAUNCH_NOT_BATCH_ACCEPTANCE'
CURRENT, MEMBERSHIPS, COMPARISONS = {}, {}, []
CHECKS = 0


def need(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)


def measure(path):
    path = Path(path)
    need(path.is_absolute() and path.is_file(), 'absolute regular input: ' + str(path))
    if path.is_relative_to(ROOT):
        need(path.resolve() == path and not path.is_symlink(), 'no workspace path aliases: ' + str(path))
    h, length = sha256(), 0
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
            length += len(block)
    return {'sha256': h.hexdigest(), 'bytes': length, 'resolved': str(path.resolve()),
            'symlink': os.readlink(path) if path.is_symlink() else None}


def pin(path, expected=None):
    name = str(path)
    if name not in CURRENT:
        CURRENT[name] = measure(path)
    actual = CURRENT[name]
    if isinstance(expected, str):
        expected = {'sha256': expected}
    if expected is not None:
        need(set(expected) <= {'sha256', 'bytes', 'resolved', 'symlink'}, 'only explicit file-key fields')
        need(all(actual[key] == value for key, value in expected.items()), 'exact current key changed: ' + name)
    return actual


def raw(path):
    before = pin(path)
    data = Path(path).read_bytes()
    need(sha256(data).hexdigest() == before['sha256'] and len(data) == before['bytes'], 'complete read still matches key')
    return data


def parse_bytes(data):
    def unique(pairs):
        value = {}
        for key, item in pairs:
            need(key not in value, 'no duplicate JSON keys')
            value[key] = item
        return value
    return json.loads(data, object_pairs_hook=unique)


def obj(path):
    return parse_bytes(raw(path))


def equal(left, right, role):
    need(raw(left) == raw(right), 'complete raw bytes differ: ' + role)
    COMPARISONS.append({'left': str(left), 'right': str(right), 'role': role,
        'bytes': pin(left)['bytes'], 'method': 'complete Python bytes equality; no native cmp command', 'equal': True})


def package(base, expected_sha, count):
    seal = base / 'SHA256SUMS'
    pin(seal, expected_sha)
    rows = {}
    for line in raw(seal).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'strict nonself manifest syntax')
        value, name = match.groups()
        path = Path(name)
        need(path.parts and path.as_posix() == name and not path.is_absolute() and '..' not in path.parts and
             name not in rows and name != 'SHA256SUMS', 'unique contained nonself manifest role')
        rows[name] = pin(base / name, value)
    entries = list(base.rglob('*'))
    physical = {path.relative_to(base).as_posix() for path in entries if path.is_file()}
    need(base.resolve() == base and all(not path.is_symlink() for path in entries) and
         len(rows) == count and physical == set(rows) | {'SHA256SUMS'}, 'complete exact physical package: ' + str(base))
    key = str(base)
    need(key not in MEMBERSHIPS or MEMBERSHIPS[key] == physical, 'package membership changed')
    MEMBERSHIPS[key] = physical
    return {str(base / name): value for name, value in rows.items()} | {str(seal): pin(seal)}


def ledger(stem):
    compressed = OUT / (stem + '.json.gz')
    meta = obj(OUT / (stem + '.meta.json'))
    data = raw(compressed)
    need(meta['encoding'] == 'lossless gzip of UTF-8 JSON, mtime=0' and data[:3] == b'\x1f\x8b\x08' and
         data[4:8] == b'\x00' * 4 and pin(compressed) == meta['compressed'], 'exact compressed bytes, metadata and zero mtime')
    decoded = gzip.decompress(data)
    need(meta['json'] == {'bytes': len(decoded), 'sha256': sha256(decoded).hexdigest()}, 'full decompressed native JSON bytes')
    value = parse_bytes(decoded)
    need(len(value) == meta['entries'] == 3276 and isinstance(value, dict), 'all3276 actual parent known keys')
    need(decoded == (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode(), 'exact original lossless JSON serialization')
    for name, row in value.items():
        need(set(row) == {'sha256', 'bytes', 'resolved', 'symlink'}, 'complete original parent key schema')
        pin(Path(name), row)
    return value


def state(path):
    return {'exists': path.exists(), 'is_file': path.is_file(), 'is_dir': path.is_dir(),
            'resolved': str(path.resolve()), 'symlink': os.readlink(path) if path.is_symlink() else None}


def configuration():
    # Exact original launcher discovery rule; no original function is called.
    optional = set(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
        '/etc/nsswitch.conf', '/etc/localtime', '/etc/locale.conf', '/etc/default/locale',
        '/usr/lib/locale/locale-archive', '/etc/bash.bashrc', '/etc/profile', '/etc/passwd', '/etc/group',
        '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2')))
    optional.update((Path(sysconfig.get_makefile_filename()), Path(sysconfig.get_config_h_filename()),
        STDLIB.parent / 'python310.zip', PYTHON.parent / 'pyvenv.cfg', PYTHON.parent.parent / 'pyvenv.cfg'))
    for directory in {PYTHON.parent, Path(sys.executable).parent, STDLIB.parent}:
        optional.update(directory / name for name in ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
    for name in ('LDLIBRARY', 'INSTSONAME'):
        if sysconfig.get_config_var(name):
            optional.add(STDLIB.parent / (sysconfig.get_config_var(name) + '._pth'))
    ldd = raw(Path('/usr/bin/ldd')).decode()
    loaders = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    need(ldd.startswith('#!/bin/bash\n') and loaders is not None, 'exact original loader discovery')
    optional.update(map(Path, loaders.group(1).split()))
    names = optional | set(CONFIG_DIRS) | set(LIB_ROOTS) | {STDLIB}
    directories = {str(path): {str(child): state(child) for child in sorted(path.rglob('*'))}
                   if path.is_dir() else None for path in CONFIG_DIRS}
    return {'presence': {str(path): state(path) for path in sorted(names)}, 'directories': directories,
        'ldd_loaders': loaders.group(1).split(), 'sysconfig_paths': sysconfig.get_paths(),
        'sysconfig_vars': json.loads(json.dumps(sysconfig.get_config_vars()))}


def runtime_names(config):
    names = {str(PYTHON), '/usr/bin/env', '/usr/bin/ldd', '/bin/bash', '/bin/sh'}
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [name for name in folders if name not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / name) for name in files if not name.endswith(('.pyc', '.pyo')))
    for directory in LIB_ROOTS:
        iterator = directory.glob('*') if directory == Path('/usr/local/lib') else directory.rglob('*')
        names.update(str(path) for path in iterator if path.is_file() and (path.name.endswith('.so') or '.so.' in path.name))
    names.update(name for name, row in config['presence'].items() if row['is_file'])
    for group in config['directories'].values():
        names.update(name for name, row in (group or {}).items() if row['is_file'])
    return names


def map_paths(text):
    return sorted({str(Path(parts[5]).resolve()) for line in text.splitlines()
                   if len(parts := line.split(None, 5)) == 6 and parts[5].startswith('/')})


def consumed(value):
    need(value['mapped_files'] == map_paths(value['maps']), 'actual raw sample and mapped names agree')
    names = set(value['mapped_files'])
    for row in value.get('modules', {}).values():
        names.update(str(Path(path).resolve()) for path in (row.get('file'), row.get('origin')) if path and path.startswith('/'))
    need(not any(path.endswith(('.pyc', '.pyo')) for path in names), 'no bytecode in retained source-only samples')
    return names


def original_native():
    parent_argv = [str(PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(OUT / 'unused_launcher_cache'),
                   str(LAUNCHER_PREP / 'launcher.py'), 'launch-current-p208-p209', LAUNCHER_SEAL]
    child_argv = [str(PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(OUT / 'unused_checker_cache'),
                  str(CHECKER_PREP / 'inspect.py'), '--expected-preparation-sha256', CHECKER_SEAL]
    launch = obj(QA / 'P208_P209_REUSE02_ROOT_LAUNCH.actual.json')
    completion = obj(QA / 'P208_P209_REUSE02_ROOT_COMPLETION.actual.json')
    need(launch['role'] == 'ACTUAL_ROOT_NATIVE_REVISED_READONLY_REUSE_LAUNCH' and launch['cwd'] == str(ROOT) and
         launch['command'] == ' '.join(['/usr/bin/env', '-i', *[key + '=' + value for key, value in ENV.items()], *parent_argv]),
         'actual exact outer root launcher command')
    need(launch['result']['session_id'] == completion['session_id'] == 68034 and launch['result']['output'] == '' and
         completion['role'] == 'ACTUAL_ROOT_NATIVE_REVISED_READONLY_REUSE_COMPLETION' and completion['result']['exit_code'] == 0,
         'actual root session binding and outer native exit0')
    outer = parse_bytes(completion['result']['output'])
    receipt, native = obj(OUT / 'RECEIPT.json'), obj(OUT / 'NATIVE_RESULT.json')
    need(outer == {'checker_exit': 0, 'checker_json_status': CHILD_STATUS, 'output': str(OUT),
         'output_seal': {'manifest': pin(OUT / 'SHA256SUMS'), 'payloads': 20}, 'status': PARENT_STATUS}, 'complete actual parent stdout receipt binding')
    need(receipt['native'] == native and receipt['status'] == PARENT_STATUS and receipt['failures'] == [] and
         receipt['checker_json_status'] == CHILD_STATUS and receipt['complete_checker_json'] == 'checker.stdout' and
         receipt['external'] == 'HOLD_EXTERNAL', 'complete original native result and parsed receipt')
    for field in ('known_inputs_unchanged', 'runtime_membership_unchanged', 'scoped_inputs_unchanged', 'configuration_unchanged'):
        need(receipt[field] is True, 'actual completed parent closure field: ' + field)
    need(all(type(receipt[field]) is int and receipt[field] == 0 for field in ('scientific_executions', 'builds', 'page_views')),
         'parent claims zero new science/build/view')
    expected = {'argv': child_argv, 'cwd': str(ROOT), 'env': ENV, 'stdin': 'DEVNULL', 'stdout': 'checker.stdout',
        'stderr': 'checker.stderr', 'start_new_session': True, 'timeout_seconds': 600}
    attempt, spawned = obj(OUT / 'PRE_SPAWN_ATTEMPT.json'), obj(OUT / 'SPAWNED.json')
    need(all(native[key] == value and attempt[key] == value for key, value in expected.items()), 'exact child original argv/cwd/env/stream roles')
    need(attempt['exit'] is None and attempt['outcome'] == 'NOT_STARTED' and attempt['cleanup'] == [] and
         attempt['started_epoch'] == native['started_epoch'], 'actual child pre-spawn intent precedes completion')
    need(native['exit'] == 0 and native['outcome'] == 'COMPLETED' and native['process_group_settled'] is True and
         native['spawn_attempted'] is True and spawned['pid'] == spawned['process_group'] == native['pid'] == native['process_group'] == 762004 and
         spawned['argv'] == child_argv and spawned['start_new_session'] is True and
         native['started_epoch'] <= spawned['epoch'] <= native['finished_epoch'], 'successful native child and owned group identity')
    need(len(native['cleanup']) == 1 and native['cleanup'][0]['state'] == 'ABSENT' and native['cleanup'][0]['error'] is None and
         native['cleanup'][0]['probe'] == 'killpg(pid,0)' and native['cleanup'][0]['owned_process_group'] == native['pid'] and
         'signal' not in native['cleanup'][0] and spawned['epoch'] <= native['cleanup'][0]['epoch'] <= native['finished_epoch'],
         'actual settled absent group, no cleanup signal or uncertainty')
    launcher = obj(OUT / 'LAUNCHER_ATTEMPT.json')
    need(launcher['orig_argv'] == parent_argv and launcher['cwd'] == str(ROOT) and launcher['env'] == ENV and
         launcher['output'] == str(OUT) and launcher['expected_launcher_preparation_sha256'] == LAUNCHER_SEAL and
         launcher['checker_preparation_sha256'] == CHECKER_SEAL and launcher['epoch'] <= native['started_epoch'], 'actual parent pre-launch binding')
    for stream in ('checker.stdout', 'checker.stderr'):
        need(pin(OUT / stream) == receipt['streams'][stream], 'complete settled raw native stream')
    need(pin(OUT / 'checker.stdout')['sha256'] == 'b5f7d0c90bb2f79f2213837231de2f949b3e39db0454d545e9936cef2ab1fb2a' and
         pin(OUT / 'checker.stdout')['bytes'] == 15638 and pin(OUT / 'checker.stderr')['bytes'] == 0, 'full original JSON bytes and empty native stderr')
    return parent_argv, launcher, native, obj(OUT / 'checker.stdout')


def aliases_and_child(contract, child):
    declarations = obj(CHECKER_PREP / 'ALIASES.json')
    need(len(declarations) == 6, 'only six original declared documentary aliases')
    expected_used = {}
    for row in declarations:
        need(Path(row['original']).name in {'FINDINGS.json', 'SHA256SUMS', 'FINAL_THEOREM_CONTRACTS.md'} and
             row['cases'] in (['p208_a'], ['p208_b'], ['p209_b']), 'never a scientific/runtime alias')
        pin(row['physical'], row['sha256'])
        pin(row['provenance'], contract['fixed_inputs'][row['provenance']])
        selector = row['selector']
        if selector == 'exact_root_pair_relocations':
            need(any(value['original'] == row['original'] and value['preserved'] == row['physical'] and
                 value['historical']['sha256'] == row['sha256'] for value in obj(row['provenance'])[selector]), 'exact P208 A documentary provenance')
        elif selector == 'exact_original_at_hash':
            need(obj(row['provenance'])[row['original'] + ' @ ' + row['sha256']] == row['physical'], 'exact P209 B documentary provenance')
        elif selector.startswith('initial_'):
            need(obj(row['provenance'])[selector] == row['sha256'] and Path(row['physical']).parent ==
                 Path(row['provenance']).parent / 'initial_snapshot', 'exact P208 B documentary provenance')
        else:
            need(row['sha256'] + '  ' + selector in raw(row['provenance']).decode().splitlines() and
                 Path(row['provenance']).parent / selector == Path(row['physical']), 'exact original theorem-contract manifest role')
        key = row['original'] + ' @ ' + row['sha256']
        need(key not in expected_used, 'unique documentary alias role')
        expected_used[key] = {'case': row['cases'][0], 'physical': row['physical']}
    need(child['documentary_aliases_used'] == expected_used, 'all and only six declared aliases actually used')
    expected_results = {}
    for case, spec in contract['pairs'].items():
        old = spec['paper_number'] == 208
        expected_results[case] = {'checks_each': spec['checks_each'], 'input_entries': spec['input_count'],
            'native_commands': 7 if old else 85, 'runs_reused': 2, 'runtime_entries': 918 if old else 3133}
    for case, spec in contract['builds'].items():
        expected_results[case] = {'builds_reused': 2, 'key_counts': spec['counts'], 'native_commands': 32,
            'pages_each': spec['pages'], 'previous_actual_pages_reused': spec['pages']}
    need(child['results'] == expected_results and len(contract['pairs']) == 6 and len(contract['builds']) == 2,
         'six old pairs/four old builds/eleven old actual views, not new executions')
    need(child['status'] == CHILD_STATUS and child['checks'] == 3988646 and child['current_paths_reread'] == 136582 and
         child['current_read_key_sha256'] == 'fcc96e90fa34494ad95896763e476978c4435a0c9533c685825cd4b62a0a2a4f' and
         child['raw_byte_comparisons_read_only'] == 84 and child['external'] == 'HOLD_EXTERNAL' and
         all(type(child[key]) is int and child[key] == 0 for key in ('mathematical_executions', 'builds', 'page_views')),
         'exact original child reuse-only result semantics')
    refs = child['original_ledger_references']
    need(len(refs) == 40 and len({(row['before'], row['after']) for row in refs}) == 40 and
         all(set(row) == {'before', 'after', 'entries'} and Path(row['before']).is_absolute() and Path(row['after']).is_absolute() and
             Path(row['before']).is_relative_to(ROOT) and Path(row['after']).is_relative_to(ROOT) and type(row['entries']) is int and row['entries'] > 0 for row in refs),
         'all40 original ledger references are authenticated output roles; no re-expansion here')
    return declarations


def failure_preservation():
    inventory = obj(CHECKER_PREP / 'FAILURE_PINS.json')
    failed = package(FAILED, '88d504f5a04a74c0e03f313946180899ba3259f4d9d554e8fa59068bee0314a3', 20)
    oldcheck = package(OLD_CHECKER, '8fc25ed0775c40e38ec8e006eae53f5d762f92a3496bda6349872a46c6adacfc', 5)
    oldlaunch = package(OLD_LAUNCHER, 'e2632c186851d1edbcf3c0616483584446a35738fb6adab0fd7b1ccec633f742', 4)
    expected = set(failed) | set(oldcheck) | set(oldlaunch) | {str(QA / ('P208_P209_REUSE_' + suffix + '.actual.json')) for suffix in ('LAUNCH', 'COMPLETION')}
    need(set(inventory) == expected and len(inventory) == 34, 'all34 original failed attempt/preparation/root records preserved')
    for name, value in inventory.items():
        pin(name, value)
    failed_child, failed_parent = obj(FAILED / 'checker.stdout'), obj(FAILED / 'RECEIPT.json')
    need(failed_child['status'] == 'FAIL_REUSE_KEY_AFFECTED_FRESH_CHECK_REQUIRED' and failed_child['case'] == 'p208_a' and
         failed_child['checks_completed'] == 79727 and failed_child['current_paths_seen'] == 11844 and
         parse_bytes(failed_child['error'])['rule'] == 'Archived exact raw comparator' and
         failed_parent['status'] == 'FAIL_PRESERVED' and failed_parent['native']['exit'] == 1 and
         obj(QA / 'P208_P209_REUSE_COMPLETION.actual.json')['result']['exit_code'] == 1,
         'real canonical-operand failure remains a failed original, not relabelled PASS')
    equal(OLD_CHECKER / 'INPUT_PINS.json', CHECKER_PREP / 'INPUT_PINS.json', 'unchanged128 fixed inputs across revision')
    equal(OLD_CHECKER / 'ALIASES.json', CHECKER_PREP / 'ALIASES.json', 'unchanged six declarations across revision')
    return len(inventory)


def main():
    need(len(sys.argv) == 4 and sys.argv[1:3] == ['receive-actual-reuse02-wrapper', '--expected-preparation-sha256'] and
         re.fullmatch('[0-9a-f]{64}', sys.argv[3]) is not None, 'exact root-only read-only receiver command')
    need(Path(__file__).resolve() == HERE / 'receive.py' and Path.cwd() == ROOT and Path(sys.executable).resolve() == PYTHON,
         'fixed receiver/system interpreter/workspace')
    need(set(os.environ) == set(ENV), 'only four allowed environment names; never record inherited values')
    need(all(os.environ[key] == value for key, value in ENV.items()), 'exact safe ENV4')
    need(sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and sys.flags.optimize == 0 and
         sys.path == ['/usr/lib/python310.zip', str(STDLIB), str(STDLIB / 'lib-dynload')], 'source-only isolated unoptimized system interpreter')
    need(sys.pycache_prefix == str(HERE / 'never_created_receiver_cache') and not os.path.lexists(sys.pycache_prefix), 'exact absent unwritten receiver cache')
    package(HERE, sys.argv[3], 5)
    direct = obj(HERE / 'INPUT_PINS.json')
    need(direct['schema'] == 'p208-p209-reuse02-root-receiver-input-pins-v1' and len(direct['pins']) == 16, 'exact preparation direct-input contract')
    for name, value in direct['pins'].items():
        pin(name, value)
    package(OUT, OUTPUT_SEAL, 20)
    checker = package(CHECKER_PREP, CHECKER_SEAL, 7)
    launcher = package(LAUNCHER_PREP, LAUNCHER_SEAL, 5)
    pin(CHECKER_PREP / 'inspect.py', CHECKER_SOURCE)
    pin(LAUNCHER_PREP / 'launcher.py', LAUNCHER_SOURCE)
    equal(OUT / 'executed_inspect.py', CHECKER_PREP / 'inspect.py', 'actual child source bytes bound to accepted revised checker')
    equal(OUT / 'executed_launcher.py', LAUNCHER_PREP / 'launcher.py', 'actual parent source bytes bound to accepted revised launcher')
    parent_argv, parent_attempt, native, child = original_native()
    contract = obj(CHECKER_PREP / 'INPUT_PINS.json')
    scoped_before, scoped_after = obj(OUT / 'SCOPED_INPUTS_BEFORE.json'), obj(OUT / 'SCOPED_INPUTS_AFTER.json')
    expected_scoped = {'launcher_preparation': launcher, 'checker_preparation': checker,
        'fixed_inputs': {name: pin(name, value) for name, value in contract['fixed_inputs'].items()}}
    need(len(contract['fixed_inputs']) == 128 and scoped_before == scoped_after == expected_scoped,
         'all scoped14 preparation and128 fixed original keys/current physical membership')
    equal(OUT / 'SCOPED_INPUTS_BEFORE.json', OUT / 'SCOPED_INPUTS_AFTER.json', 'full original scoped key bytes')
    before, after = ledger('KNOWN_INPUTS_BEFORE'), ledger('KNOWN_INPUTS_AFTER')
    need(before == after, 'all original3276 before/after known keys agree')
    equal(OUT / 'KNOWN_INPUTS_BEFORE.json.gz', OUT / 'KNOWN_INPUTS_AFTER.json.gz', 'complete original lossless known-key bytes')
    config = obj(OUT / 'CONFIGURATION_BEFORE.json')
    need(config == obj(OUT / 'CONFIGURATION_AFTER.json') == configuration(), 'complete original/current configuration, sysconfig, nested presence and membership')
    equal(OUT / 'CONFIGURATION_BEFORE.json', OUT / 'CONFIGURATION_AFTER.json', 'complete original configuration bytes')
    parents = [obj(OUT / ('PARENT_' + when + '.json')) for when in ('BEFORE', 'AFTER')]
    known_resolved = {value['resolved'] for value in before.values()}
    for index, parent in enumerate(parents):
        need(parent['phase'] == ('BEFORE_KNOWN_KEY_AND_CHILD' if index == 0 else 'AFTER_CHILD_AND_SETTLING') and
             parent['env'] == ENV and parent['cwd'] == str(ROOT) and parent['executable'] == str(PYTHON) and
             parent['orig_argv'] == parent_argv and parent['flags'] == parent_attempt['flags'] and
             parent['sys_path'] == ['/usr/lib/python310.zip', str(STDLIB), str(STDLIB / 'lib-dynload')] and
             parent['pycache_prefix'] == str(OUT / 'unused_launcher_cache') and parent['cache_exists'] is False and
             all(flag in parent['flags'] for flag in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')),
             'exact actual parent runtime settings and isolated source-only sample')
        need(consumed(parent) <= known_resolved, 'all original parent module/map names covered by known keys')
    need(parents[0]['pid'] == parents[1]['pid'] and parent_attempt['epoch'] <= parents[0]['epoch'] <= native['started_epoch'] and
         native['finished_epoch'] <= parents[1]['epoch'], 'actual parent identity and before/native/after chronology')
    samples = obj(OUT / 'CHILD_MAP_SAMPLES.json')
    need(samples['successful_samples'] >= 1 and samples['sample_errors'] == [] and samples['interval_seconds'] == 0.25,
         'actual retained child samples, no invented continuous trace')
    for sample in (samples['first'], samples['last']):
        need(sample['pid'] == native['pid'] and native['started_epoch'] <= sample['epoch'] <= native['finished_epoch'] and
             consumed(sample) <= known_resolved, 'actual first/last child raw-map coverage')
    need(samples['first']['epoch'] <= samples['last']['epoch'], 'ordered retained samples')
    runtime = runtime_names(config)
    need(runtime | consumed(parents[0]) | set().union(*(set(group) for group in expected_scoped.values())) == set(before),
         'all and only original runtime/early-sample/scoped known-key membership')
    declarations = aliases_and_child(contract, child)
    failures_preserved = failure_preservation()
    for cache in (OUT / 'unused_launcher_cache', OUT / 'unused_checker_cache', HERE / 'never_created_receiver_cache'):
        need(not os.path.lexists(cache), 'all explicit source-only cache roles remain absent')
    # Every actually consumed file, including both original ledgers and all
    # actual parent keys, is fully reread. No child ledger is re-expanded.
    final_before = dict(CURRENT)
    for name, value in final_before.items():
        need(measure(name) == value, 'final complete current-key reread: ' + name)
    need(configuration() == config and runtime_names(config) == runtime, 'final current configuration/runtime membership unchanged')
    for base, expected in MEMBERSHIPS.items():
        paths = list(Path(base).rglob('*'))
        need(all(not path.is_symlink() for path in paths) and
             {path.relative_to(base).as_posix() for path in paths if path.is_file()} == expected, 'all bounded original package memberships unchanged')
    print(json.dumps({'status': 'PASS_ROOT_ORIGINAL_REUSE02_WRAPPER_RECEPTION_NOT_BATCH_ACCEPTANCE', 'checks': CHECKS,
        'scope': 'Actual20 wrapper originals and all3276 current parent keys; NOT another full136582-path child re-audit.',
        'receiver_source_sha256': pin(HERE / 'receive.py')['sha256'], 'receiver_preparation_sha256': sys.argv[3],
        'actual_output_manifest_sha256': OUTPUT_SEAL, 'actual_outer_session': 68034, 'actual_outer_exit': 0, 'actual_child_exit': 0,
        'parent_known_keys_rechecked': len(before), 'scoped_fixed_inputs': 128, 'revised_preparation_payloads': [7, 5],
        'failed01_original_pins_preserved': failures_preserved, 'documentary_aliases': declarations,
        'actual_current_receiver_read_paths': len(final_before),
        'actual_current_receiver_key_sha256': sha256((json.dumps(final_before, sort_keys=True, separators=(',', ':')) + '\n').encode()).hexdigest(),
        'full_current_inputs_scope': 'Reconstructible from the pinned original3276-key ledger plus exact packages/direct pins; no new broad ledger archive.',
        'actual_complete_raw_comparisons': COMPARISONS,
        'received_original_child_result': {'checks': child['checks'], 'current_paths_reread': child['current_paths_reread'],
            'current_read_key_sha256': child['current_read_key_sha256'], 'read_only_raw_comparisons': 84,
            'original_ledger_reference_count': 40, 'result_scope': 'Original actual child execution, not work newly performed by this receiver.'},
        'reused_strict_pairs': 6, 'reused_scientific_runs': 12, 'reused_terminal_builds': 4, 'reused_previous_actual_page_views': 11,
        'new_scientific_executions': 0, 'new_builds': 0, 'new_page_views': 0, 'new_original_program_executions': 0,
        'environment': ENV, 'cwd': str(ROOT), 'orig_argv': sys.orig_argv,
        'limits': ['Known named files and recorded sampled coverage; no historical OS reconstruction or continuous trace.',
            'The failed01 canonical-operand adapter attempt is preserved with native1; revision did not change science/runtime or six aliases.',
            'Source hashes and current frames do not constitute new proof review or viewing.', 'P210 and first five-paper terminal gate remain separate.'],
        'external': 'OWNER_AMBER / HOLD_EXTERNAL'}, sort_keys=True, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception:
        print(json.dumps({'status': 'FAIL_ROOT_WRAPPER_RECEPTION_NO_ACCEPTANCE', 'checks_completed': CHECKS,
            'traceback': traceback.format_exc(), 'current_paths_seen': len(CURRENT), 'no_original_program_execution': True,
            'no_science_build_view': True, 'no_files_written': True}, sort_keys=True, indent=2))
        raise SystemExit(1)
