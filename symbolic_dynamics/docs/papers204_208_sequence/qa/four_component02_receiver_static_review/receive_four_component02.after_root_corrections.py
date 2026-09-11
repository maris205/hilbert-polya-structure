#!/usr/bin/env python3
"""Root original reception of the actual successful four-paper component run02.
Read-only adaptation of the accepted P208/P209 wrapper receiver.
All 3266 parent known keys are reconstructed and reread; the actual child's
142784-key result is received, not recursively re-executed here. No child
commands, science, builds, page views, old writer imports or local writes.
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
HERE = QA
OUT = QA / 'five_paper_terminal_component_run_02'
FAILED = QA / 'five_paper_terminal_component_run_01'
CHECKER_PREP = QA / 'five_paper_terminal_gate_revision_01'
LAUNCHER_PREP = QA / 'five_paper_terminal_component_launch_revision_01'
OLD_CHECKER = QA / 'five_paper_terminal_gate_preparation'
OLD_LAUNCHER = QA / 'five_paper_terminal_component_launch_preparation'
PYTHON = Path('/usr/bin/python3.10')
STDLIB = Path('/usr/lib/python3.10')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
CONFIG_DIRS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/lib/locale/C.utf8', '/etc/profile.d',
    '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv')))
OUTPUT_SEAL = '7eda9f4c4452d3d1dc0656ca592cef8e7783a120ccada3fd671cc2238aaf6ebe'
CHECKER_SEAL = '3863616519c14cc2f70d92deced93d745978a34f7e90f78aed5f00dd12ca8238'
LAUNCHER_SEAL = 'd86a67b5b2fd43230b4259090bb3df8a8d5a39c19fbe849ba4326682d253f9d2'
CHECKER_SOURCE = '0d84acf3034af513bd57227d626e227c3f3d7d8462859c8678943d2da517f399'
LAUNCHER_SOURCE = 'a78aa9d3c9ec1badb1c77c775d99d7b1f52689f65832e000f938acbd12036558'
CHILD_STATUS = 'FOUR_COMPLETED_COMPONENT_PASS_P210_NOT_ASSESSED_NOT_FIVE_PAPER_PASS'
PARENT_STATUS = 'PASS_NATIVE_FOUR_COMPLETED_COMPONENT_NOT_FIVE_PAPER_ACCEPTANCE'
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
    need(len(value) == meta['entries'] == 3266 and isinstance(value, dict), 'all3266 actual parent known keys')
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
                   str(LAUNCHER_PREP / 'launcher.py'), 'launch-four-completed-component', LAUNCHER_SEAL]
    child_argv = [str(PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(OUT / 'unused_checker_cache'),
                  str(CHECKER_PREP / 'four_completed.py'), '--expected-preparation-sha256', CHECKER_SEAL,
                  '--reuse-root-binding', str(CHECKER_PREP / 'ROOT_REUSE_BINDING.json'),
                  '--reuse-root-binding-sha256', 'b722f61ae2abcc4220a99473b6d9bb104962b52ea509c258f976c0136d08affd']
    launch = obj(QA / 'FIVE_FOUR_COMPONENT_RUN02_ROOT_LAUNCH.actual.json')
    completion = obj(QA / 'FIVE_FOUR_COMPONENT_RUN02_ROOT_COMPLETION.actual.json')
    need(launch['role'] == 'actual root four component run02 launch' and launch['cwd'] == str(ROOT) and
         launch['command'] == ' '.join(['/usr/bin/env', '-i', *[key + '=' + value for key, value in ENV.items()], *parent_argv]),
         'actual exact outer root launcher command')
    need(launch['result']['session_id'] == completion['session_id'] == 21492 and launch['result']['output'] == '' and
         completion['role'] == 'actual root four component run02 native return' and completion['result']['exit_code'] == 0,
         'actual root session binding and outer native exit0')
    progress = obj(QA / 'FIVE_FOUR_COMPONENT_RUN02_ROOT_PROGRESS01.actual.json')
    need(progress['launch_record'] == completion['launch_record'] == 'FIVE_FOUR_COMPONENT_RUN02_ROOT_LAUNCH.actual.json' and
         progress['session_id'] == 21492 and progress['result']['session_id'] == 21492 and
         completion['prior_progress_records'] == ['FIVE_FOUR_COMPONENT_RUN02_ROOT_PROGRESS01.actual.json'],
         'actual segmented transport record chain')
    events = [parse_bytes(line) for line in (progress['result']['output'] + completion['result']['output']).splitlines()]
    need(len(events) == 7, 'actual six heartbeat lines followed by complete final JSON')
    outer = events[-1]
    receipt, native = obj(OUT / 'RECEIPT.json'), obj(OUT / 'NATIVE_RESULT.json')
    need(outer == {'checker_exit': 0, 'checker_json_status': CHILD_STATUS, 'output': str(OUT),
         'output_seal': {'manifest': pin(OUT / 'SHA256SUMS'), 'payloads': 20}, 'status': PARENT_STATUS}, 'complete actual parent stdout receipt binding')
    need(receipt['native'] == native and receipt['status'] == PARENT_STATUS and receipt['failures'] == [] and
         receipt['checker_json_status'] == CHILD_STATUS and receipt['complete_checker_json'] == 'checker.stdout' and
         receipt['external'] == 'HOLD_EXTERNAL', 'complete original native result and parsed receipt')
    for field in ('known_inputs_unchanged', 'runtime_membership_unchanged', 'scoped_inputs_unchanged', 'configuration_unchanged'):
        need(receipt[field] is True, 'actual completed parent closure field: ' + field)
    need(all(type(receipt[field]) is int and receipt[field] == 0 for field in ('scientific_executions', 'builds', 'page_views', 'new_reviews')) and
         receipt['p210_accepted'] is False and receipt['five_paper_acceptance'] is False and receipt['owner'] == 'OWNER_AMBER',
         'parent claims zero new science/build/view/review and no P210 or five-paper acceptance')
    expected = {'argv': child_argv, 'cwd': str(ROOT), 'env': ENV, 'stdin': 'DEVNULL', 'stdout': 'checker.stdout',
        'stderr': 'checker.stderr', 'start_new_session': True, 'timeout_seconds': 600, 'heartbeat_seconds': 30}
    attempt, spawned = obj(OUT / 'PRE_SPAWN_ATTEMPT.json'), obj(OUT / 'SPAWNED.json')
    need(all(native[key] == value and attempt[key] == value for key, value in expected.items()), 'exact child original argv/cwd/env/stream roles')
    need(attempt['exit'] is None and attempt['outcome'] == 'NOT_STARTED' and attempt['cleanup'] == [] and
         attempt['started_epoch'] == native['started_epoch'] and attempt['heartbeats'] == [], 'actual child pre-spawn intent precedes completion')
    need(native['exit'] == 0 and native['outcome'] == 'COMPLETED' and native['process_group_settled'] is True and
         native['spawn_attempted'] is True and spawned['pid'] == spawned['process_group'] == native['pid'] == native['process_group'] == 770811 and
         spawned['argv'] == child_argv and spawned['start_new_session'] is True and
         native['started_epoch'] <= spawned['epoch'] <= native['finished_epoch'], 'successful native child and owned group identity')
    need(len(native['cleanup']) == 1 and native['cleanup'][0]['state'] == 'ABSENT' and native['cleanup'][0]['error'] is None and
         native['cleanup'][0]['probe'] == 'killpg(pid,0)' and native['cleanup'][0]['owned_process_group'] == native['pid'] and
         'signal' not in native['cleanup'][0] and spawned['epoch'] <= native['cleanup'][0]['epoch'] <= native['finished_epoch'],
         'actual settled absent group, no cleanup signal or uncertainty')
    need(events[:-1] == native['heartbeats'] and len(native['heartbeats']) == 6 and
         all(e['pid'] == native['pid'] and e['status'] == 'FOUR_COMPONENT_NATIVE_RUNNING' and
             native['started_epoch'] <= e['epoch'] <= native['finished_epoch'] for e in native['heartbeats']) and
         all(a['epoch'] < b['epoch'] for a, b in zip(native['heartbeats'], native['heartbeats'][1:])),
         'all actual emitted heartbeat bytes bound in order to owned child')
    launcher = obj(OUT / 'LAUNCHER_ATTEMPT.json')
    need(launcher['orig_argv'] == parent_argv and launcher['cwd'] == str(ROOT) and launcher['env'] == ENV and
         launcher['output'] == str(OUT) and launcher['expected_launcher_preparation_sha256'] == LAUNCHER_SEAL and
         launcher['checker_preparation_sha256'] == CHECKER_SEAL and launcher['epoch'] <= native['started_epoch'], 'actual parent pre-launch binding')
    for stream in ('checker.stdout', 'checker.stderr'):
        need(pin(OUT / stream) == receipt['streams'][stream], 'complete settled raw native stream')
    need(pin(OUT / 'checker.stdout')['sha256'] == 'dade493f165bbc3c5f9b09233ec34215f0ec75199c3b26642513318327057b76' and
         pin(OUT / 'checker.stdout')['bytes'] == 5733 and pin(OUT / 'checker.stderr')['bytes'] == 0, 'full original JSON bytes and empty native stderr')
    return parent_argv, launcher, native, obj(OUT / 'checker.stdout')


def aliases_and_child(contract, child):
    declarations = contract['aliases']
    need(len(declarations) == 13 and sum(len(r['cases']) for r in declarations) == 18,
         'exact original documentary declaration census')
    allowed = {}
    for row in declarations:
        need(row['kind'] == 'documentary_exact_old_path_hash', 'never a scientific/runtime alias')
        pin(row['physical'], row['sha256'])
        for case in row['cases']:
            key = row['original'] + ' @ ' + row['sha256'] + ' [' + case + ']'
            need(key not in allowed or allowed[key] == row['physical'], 'unambiguous declared documentary case')
            allowed[key] = row['physical']
    used = child['documentary_aliases_used']
    need(len(used) == 14 and all(allowed.get(k) == v for k, v in used.items()),
         'all fourteen actual used roles among the original eighteen declared cases')
    need(child['status'] == CHILD_STATUS and child['checks'] == 10270582 and
         child['current_file_keys_reread'] == 142784 and
         child['current_file_key_sha256'] == '087b90f42ad1a55fef4daa2acb29cee4fca614736c862aa9aed5e2a65d628dc0' and
         child['complete_raw_comparisons_read_only'] == 20 and child['local_links_checked'] == 6312 and
         child['papers_checked'] == ['P205', 'P207', 'P208', 'P209'] and child['prior_completed_papers'] == 4 and
         child['required_final_five'] == ['P205', 'P207', 'P208', 'P209', 'P210'] and
         child['p210_accepted_by_this_component'] is False and child['current_valid_author_A_B_pairs'] == 12 and
         child['current_valid_source_only_builds'] == 8 and child['actual_prior_page_attestations_bound'] == 21 and
         child['five_contract_ceilings_checked'] == 5 and child['owner'] == 'OWNER_AMBER' and child['external'] == 'HOLD_EXTERNAL' and
         all(type(child[k]) is int and child[k] == 0 for k in
             ('new_scientific_executions', 'new_builds', 'new_page_views', 'new_reviews', 'old_auditors_or_writers_executed', 'files_written')),
         'entire actual read-only four-paper boundary, explicitly no P210 or five-paper PASS')
    return used

def failure_preservation():
    failed = package(FAILED, '7500e71709616871e75e004d87ac0ebbbd66b112246c3fbe5bc649131aa0c724', 20)
    oldcheck = package(OLD_CHECKER, 'b984a1d494d0304a39704da1773782e1f6b10902fa4d8b0dbae77bad86c84e20', 14)
    oldlaunch = package(OLD_LAUNCHER, 'a0212daf50345b202da47e74dcb29ef4f03f0ae6edaf95f8da96d8d552d1ca74', 5)
    pins = obj(CHECKER_PREP / 'REVISION_PROVENANCE.json')['inputs']
    need(len(pins) == 53 and set(failed) | set(oldcheck) | set(oldlaunch) <= set(pins),
         'all prior failure/preparation originals contained in exact revision pins')
    for name, row in pins.items():
        pin(name, row)
    before, parent = obj(FAILED / 'checker.stdout'), obj(FAILED / 'RECEIPT.json')
    need(before['status'] == 'FOUR_COMPONENT_FAIL_NO_FIVE_PAPER_ACCEPTANCE' and before['checks_completed'] == 8940156 and
         parent['status'] == 'FAIL_PRESERVED' and parent['native']['exit'] == 1 and
         obj(QA / 'FIVE_FOUR_COMPONENT_ROOT_COMPLETION.actual.json')['result']['exit_code'] == 1,
         'real typed-role-as-path initial failure retained, not relabelled success')
    copies = obj(CHECKER_PREP / 'REVISION_PROVENANCE.json')['unchanged_byte_copies']
    need(len(copies) == 8, 'all original selector and contract copies')
    for name, row in copies.items():
        pin(CHECKER_PREP / name, row)
        equal(CHECKER_PREP / name, OLD_CHECKER / name, 'unchanged selector/contract: ' + name)
    return len(pins)

def main():
    need(len(sys.argv) == 1 and Path(__file__).resolve() == QA / 'receive_four_component02.py' and
         Path.cwd() == ROOT and Path(sys.executable).resolve() == PYTHON, 'exact root-only source/interpreter/cwd')
    need(dict(os.environ) == ENV and sys.flags.isolated == sys.flags.no_site == 1 and
         sys.flags.dont_write_bytecode and sys.flags.optimize == 0 and
         sys.path == ['/usr/lib/python310.zip', str(STDLIB), str(STDLIB / 'lib-dynload')], 'safe source-only receiver settings')
    cache = QA / 'four_component02_receiver_unused_cache'
    need(sys.pycache_prefix == str(cache) and not os.path.lexists(cache), 'separate absent receiver cache')
    pin(Path(__file__).resolve())
    package(OUT, OUTPUT_SEAL, 20)
    checker = package(CHECKER_PREP, CHECKER_SEAL, 14)
    launcher = package(LAUNCHER_PREP, LAUNCHER_SEAL, 5)
    pin(CHECKER_PREP / 'four_completed.py', CHECKER_SOURCE)
    pin(LAUNCHER_PREP / 'launcher.py', LAUNCHER_SOURCE)
    equal(OUT / 'executed_four_completed.py', CHECKER_PREP / 'four_completed.py', 'actual child source bytes bound to accepted revised checker')
    equal(OUT / 'executed_launcher.py', LAUNCHER_PREP / 'launcher.py', 'actual parent source bytes bound to accepted revised launcher')
    parent_argv, parent_attempt, native, child = original_native()
    contract = obj(CHECKER_PREP / 'FOUR_INPUTS.json')
    scoped_before, scoped_after = obj(OUT / 'SCOPED_INPUTS_BEFORE.json'), obj(OUT / 'SCOPED_INPUTS_AFTER.json')
    binding = obj(CHECKER_PREP / 'ROOT_REUSE_BINDING.json')
    pin(CHECKER_PREP / 'ROOT_REUSE_BINDING.json', 'b722f61ae2abcc4220a99473b6d9bb104962b52ea509c258f976c0136d08affd')
    anchors = {binding[k]: pin(binding[k], binding[k + '_pin']) for k in ('native', 'report')}
    need(obj(binding['native'])['result']['exit_code'] == 0 and binding['accepted_status'] in raw(binding['report']).decode(),
         'actual accepted original reuse-root binding')
    index = Path(contract['current_index'])
    index = index if index.is_absolute() else ROOT / index
    anchors[str(index)] = pin(index)
    provenance = obj(LAUNCHER_PREP / 'PROVENANCE.json')['inputs']
    expected_scoped = {'launcher_preparation': launcher, 'component_preparation': checker,
        'fixed_inputs': {name: pin(name, row) for name, row in contract['fixed_inputs'].items()},
        'actual_root_binding_and_live_ceiling_index': anchors,
        'adaptation_inputs': {name: pin(name, row) for name, row in provenance.items()}}
    need(len(contract['fixed_inputs']) == 54 and len(provenance) == 75 and
         scoped_before == scoped_after == expected_scoped, 'all exact current original scoped groups')
    equal(OUT / 'SCOPED_INPUTS_BEFORE.json', OUT / 'SCOPED_INPUTS_AFTER.json', 'full original scoped key bytes')
    before, after = ledger('KNOWN_INPUTS_BEFORE'), ledger('KNOWN_INPUTS_AFTER')
    need(before == after, 'all original3266 before/after known keys agree')
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
    seal_native = obj(QA / 'FIVE_FOUR_COMPONENT_RUN02_ROOT_SEAL.actual.json')
    need(seal_native['command'] == '/usr/bin/sha256sum -c SHA256SUMS' and seal_native['cwd'] == str(OUT) and
         seal_native['result']['exit_code'] == 0 and seal_native['result']['chunk_id'] == '1c8942' and
         seal_native['result']['output'] == ''.join(line[66:] + ': OK\n' for line in raw(OUT / 'SHA256SUMS').decode().splitlines()),
         'complete actual native all20 output seal check')
    need(not os.path.lexists('/usr/lib/python310.zip') and not os.path.lexists('/etc/ld.so.preload') and
         all(not row['exists'] and row['symlink'] is None for name, row in config['presence'].items()
             if name.endswith(('._pth', '/pyvenv.cfg'))), 'actual no-injection configuration guards')
    failures_preserved = failure_preservation()
    for cache in (OUT / 'unused_launcher_cache', OUT / 'unused_checker_cache', cache):
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
    print(json.dumps({'status': 'PASS_ROOT_FOUR_COMPONENT02_ORIGINAL_RECEPTION_NOT_FIVE_PAPER_ACCEPTANCE',
        'checks': CHECKS, 'receiver_source': pin(Path(__file__).resolve()),
        'actual_output_manifest_sha256': OUTPUT_SEAL, 'actual_outer_session': 21492, 'actual_outer_exit': 0,
        'actual_child_exit': 0, 'parent_known_keys_rechecked': len(before),
        'current_receiver_read_paths': len(final_before),
        'current_receiver_key_sha256': sha256((json.dumps(final_before, sort_keys=True, separators=(',', ':')) + '\n').encode()).hexdigest(),
        'extra_read_keys_not_in_parent_ledger': {n: v for n, v in final_before.items() if n not in before},
        'scoped_group_counts': {k: len(v) for k, v in expected_scoped.items()},
        'failed01_preservation_input_pins': failures_preserved, 'all_actual_raw_comparisons': COMPARISONS,
        'actual_six_heartbeats_bound': True, 'actual_child_result': child,
        'reused_author_A_B_pairs': 12, 'reused_terminal_builds': 8, 'reused_previous_actual_page_attestations': 21,
        'new_scientific_executions': 0, 'new_builds': 0, 'new_page_views': 0, 'new_original_program_executions': 0,
        'scope': 'Actual20 wrapper originals and all3266 current parent keys; original142784-path child result received, not rerun. No OS/startup/continuous trace. No P210 acceptance or first exact-five PASS.',
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
