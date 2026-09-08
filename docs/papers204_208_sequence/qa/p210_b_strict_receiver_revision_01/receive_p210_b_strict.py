#!/usr/bin/env python3
"""Read-only actual P210 B strict-pair receiver, revision 01.
Root executes only after independent full source review. This preparer does not.
Preserves eight original helpers; consumes actual session 31521 and native seal.
No scientific run, child command, old writer import, build, view or mutation.
"""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys
import sysconfig

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_b_strict_preparation'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PREP_SHA = '987367c15fae0bd4d34ebf6c97cd1ee2dc71d1f15782ec57d73f61a332d97eec'
RUNNER_SHA = 'bacc8bf0351bdfbcc2bc671cd61131d6382fe5caccd00f02e3988afbf1d066d1'
REVISION = QA / 'p210_b_strict_receiver_revision_01'
OUT = QA / 'root_replays/p210_b_strict_pair_01'
PACKAGE = ROOT / 'docs/papers204_208_sequence/reviews/p210_b'
OLD_REVIEW = QA / 'p210_b_strict_receiver_static_review'
PAIR_SHA = '54cdd8ca9a00374f53a82e7f84a47fdd91f3fcde8b1519b027b98c7925ace181'
PYTHON = Path('/usr/bin/python3.10')
STDLIB = Path('/usr/lib/python3.10')
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
DATA_ROOTS = tuple(map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')))
ROOT_NATIVE_KEYS = {
    'P210_B_STRICT_ROOT_PREFLIGHT.actual.json': '8b3da0a39372c19d4c354c10dc3890b430dc96add72438e3dfbcd7da6e0fb775',
    'P210_B_STRICT_ROOT_LAUNCH.actual.json': '7a21a33b6268fbada7dcb24f0ddd379959d77d17fdfcd4aa7673d3049ede1024',
    'P210_B_STRICT_ROOT_COMPLETION.actual.json': '93b06e23559c81343a6edd38f8a370c389d8ceefbd9623f9308d387ee5374578',
    'P210_B_STRICT_ROOT_SEAL.actual.json': '381c8b06293b4c346255b55c864f1f8916887603b00ceb37b6ef3c75f6513b10'
}
READS = {}
CHECKS = 0


def need(test, label):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(label)


def raw(path):
    path = Path(path)
    data = path.read_bytes()
    row = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    name = str(path)
    need(name not in READS or READS[name] == row, ('read_changed', name))
    READS[name] = row
    return data


def val(path):
    data = raw(path)
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def js(path):
    return json.loads(raw(path))


def pin(path, expected):
    got = val(path)
    if isinstance(expected, str):
        expected = {'sha256': expected}
    need(all(got[k] == expected[k] for k in ('sha256', 'bytes') if k in expected), ('pin', str(path)))
    if 'resolved' in expected:
        need(str(Path(path).resolve(strict=True)) == expected['resolved'], ('resolved', str(path)))
    if 'symlink' in expected:
        need((os.readlink(path) if Path(path).is_symlink() else None) == expected['symlink'], ('symlink', str(path)))
    return got


def manifest(base, digest, count):
    pin(base / 'SHA256SUMS', digest)
    data = raw(base / 'SHA256SUMS')
    need(data.endswith(b'\n'), ('final_newline', str(base)))
    rows = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, ('manifest_syntax', line))
        h, name = match.groups()
        p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and name not in rows and name != 'SHA256SUMS', ('safe_nonself_unique', name))
        rows[name] = h
    files = list(base.rglob('*'))
    need(all(not p.is_symlink() for p in files), ('package_no_symlinks', str(base)))
    need(set(rows) == {p.relative_to(base).as_posix() for p in files if p.is_file()} - {'SHA256SUMS'}, ('full_inventory', str(base)))
    need(len(rows) == count, ('payload_count', str(base), len(rows), count))
    for name, h in rows.items():
        pin(base / name, h)
    return rows


def current_resources():
    names = {'/usr/bin/python3.10', '/usr/bin/cmp', '/usr/bin/ldd', '/usr/bin/env', '/bin/bash', '/bin/sh'}
    for directory, folders, files in os.walk('/usr/lib/python3.10'):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for base in map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')):
        if base.is_dir():
            paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
            names.update(str(p) for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    for base in map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')):
        if base.is_dir():
            names.update(str(p) for p in base.rglob('*') if p.is_file())
    return sorted(names)


def sample(data, known, cache):
    need(data['environment'] == ENV and data['cwd'] == str(ROOT) and data['executable'] == '/usr/bin/python3.10', 'runtime_identity')
    need(data['sys_path'] == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'], 'runtime_path')
    need(data['pycache_prefix'] == str(cache) and not data['cache_lexists'] and not os.path.lexists(cache), 'no_old_or_new_cache')
    need(all(s in data['flags'] for s in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')), 'runtime_flags')
    maps = data['proc_maps'].encode()
    need(sha256(maps).hexdigest() == data['proc_maps_sha256'] and len(maps) == data['proc_maps_bytes'], 'entire_maps')
    for name, row in list(data['mapped_files'].items()) + [(r['path'], r) for r in data['modules'].values()]:
        need(name in known and all(known[name][k] == row[k] for k in ('sha256', 'bytes')), ('runtime_sample_coverage', name))
        need(Path(name).suffix not in {'.pyc', '.pyo'}, ('no_sampled_bytecode', name))
        pin(name, row)


def rich_current(path):
    return {**val(path), 'resolved': str(Path(path).resolve(strict=True)),
            'symlink': os.readlink(path) if Path(path).is_symlink() else None}


def timestamp(value):
    parsed = datetime.fromisoformat(value)
    need(parsed.tzinfo is not None and parsed.utcoffset().total_seconds() == 0, 'actual_UTC_timestamp')
    return parsed


def configuration_snapshot():
    """Reconstruct exact source-defined names independently, never import runner."""
    paths = set(LIB_ROOTS + DATA_ROOTS + (STDLIB,))
    paths.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
    paths.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload', '/etc/localtime', '/etc/locale.conf',
        '/etc/default/locale', '/etc/nsswitch.conf', '/etc/passwd', '/etc/group', '/etc/bash.bashrc', '/etc/profile',
        '/etc/ssl/openssl.cnf', '/usr/lib/ssl/openssl.cnf',
        '/usr/lib/locale/locale-archive', '/usr/lib/python310.zip', '/root/miniconda3/lib/python312.zip',
        '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg', '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2')))
    pth = ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth')
    for directory in (Path('/usr/bin'), Path('/usr/lib')):
        paths.update(directory / name for name in pth)
    for key in ('LDLIBRARY', 'INSTSONAME'):
        name = sysconfig.get_config_var(key)
        if name:
            paths.add(Path('/usr/lib') / (name + '._pth'))
    ldd = raw('/usr/bin/ldd').decode()
    match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    need(ldd.splitlines()[0] == '#!/bin/bash' and match is not None, 'known_ldd_script_and_loader_declaration')
    paths.update(map(Path, match.group(1).split()))
    result = {}
    for p in sorted(paths, key=str):
        row = {'lexists': os.path.lexists(p), 'exists': p.exists(), 'is_file': p.is_file(), 'is_dir': p.is_dir(),
               'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}
        if p.is_file():
            row.update(val(p))
        result[str(p)] = row
    need(not result['/etc/ld.so.preload']['lexists'] and not result['/usr/lib/python310.zip']['lexists'],
         'no_preload_or_system_python_zip')
    need(all(not row['lexists'] for name, row in result.items() if name.endswith(('._pth', '/pyvenv.cfg'))),
         'no_interpreter_path_injection_files')
    return result


def exact_sample(data, known, cache):
    sample(data, known, cache)
    mapped = set()
    for line in data['proc_maps'].splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            need(not fields[5].endswith(' (deleted)'), 'no_recorded_deleted_mapping')
            mapped.add(str(Path(fields[5]).resolve(strict=True)))
    need(set(data['mapped_files']) == mapped, 'entire_raw_maps_to_declared_mapped_file_set')
    need(data['volatile_proc_maps_not_an_immutable_input'] is True, 'recorded_volatile_sample_scope')


def exact_native_argv(resources):
    extensions = sorted(n for n in resources if n.startswith(str(STDLIB) + '/') and n.endswith('.so'))
    compare = lambda left, right: ['/usr/bin/cmp', '--', str(left), str(right)]
    expected = {
        '00_cmp_runner_source': compare(PREP / 'run_pair.py', OUT / 'sources/run_pair.py'),
        '01_cmp_verifier_source': compare(PACKAGE / 'verify.py', OUT / 'sources/verify.py'),
        '01a_cmp_parameters_source': compare(PACKAGE / 'PARAMETERS.json', OUT / 'sources/PARAMETERS.json'),
        '02_ldd_before': ['/usr/bin/ldd', str(PYTHON), '/usr/bin/cmp'] + extensions}
    for number in ('01', '02'):
        expected['03_verify_' + number] = [str(PYTHON), '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(OUT / ('unused_child_' + number + '_cache')),
            str(OUT / 'sources/run_pair.py'), 'child', number, 'p210_b']
    for number in ('01', '02'):
        expected['04_cmp_canonical_' + number] = compare(
            OUT / ('commands/03_verify_' + number + '/stdout.raw'), PACKAGE / 'CANONICAL.json')
    expected['05_cmp_pair'] = compare(OUT / 'commands/03_verify_01/stdout.raw', OUT / 'commands/03_verify_02/stdout.raw')
    expected['06_ldd_after'] = ['/usr/bin/ldd', str(PYTHON), '/usr/bin/cmp'] + extensions
    return expected


def parent_argv(mode):
    return [str(PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(OUT / 'unused_parent_cache'),
        str(PREP / 'run_pair.py'), mode, '--role', 'p210_b', '--expected-preparation-sha256', PREP_SHA]


def parent_command(mode):
    return ' '.join(['/usr/bin/env', '-i', 'PATH=/usr/bin:/bin', 'LANG=C.UTF-8',
                     'LC_ALL=C.UTF-8', 'TZ=UTC'] + parent_argv(mode))


def known_names(baseline, resources, input_pins, copies, conf):
    base = set(baseline['package_files']) | set(baseline['preparation_files']) | set(resources)
    base.update(input_pins)
    base.update(row['copy'] for row in copies.values())
    base.update(name for name, row in conf.items() if row['is_file'])
    return base | {str(Path(name).resolve(strict=True)) for name in base}


def main():
    need(len(sys.argv) == 3 and sys.argv[1] == 'strict-B-actual-only' and
         re.fullmatch(r'[0-9a-f]{64}', sys.argv[2]), 'exact_root_revision_invocation')
    need(sys.flags.isolated == sys.flags.no_site == 1 and sys.dont_write_bytecode and sys.flags.optimize == 0,
         'isolated_readonly_inspector')
    need(dict(os.environ) == ENV and Path.cwd() == ROOT, 'inspector_environment')
    need(Path(__file__).resolve() == REVISION / 'receive_p210_b_strict.py' and
         Path(sys.executable).resolve() == PYTHON, 'exact_revision_source_and_interpreter')
    need(sys.pycache_prefix == str(REVISION / 'never_created_receiver_cache') and
         not os.path.lexists(sys.pycache_prefix) and
         sys.path == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'],
         'separate_absent_receiver_cache_and_source_only_path')
    started = datetime.now(timezone.utc).isoformat()
    manifest(REVISION, sys.argv[2], 7)
    manifest(OLD_REVIEW, '62c3d32b698cdaaa1ea9ae4dd01c1e538ece12bf88349065fac412d77e8a9719', 5)
    pin(OLD_REVIEW / 'inspect_p210_b_strict_pair.before_root_followup.py',
        '7234bba399e556b5d22560412785f2d64886471642baf53b7544ae9b41d6053a')
    prep_rows = manifest(PREP, PREP_SHA, 4)
    need(set(prep_rows) == {'run_pair.py', 'README.md', 'INPUT_PINS.json', 'STATIC_CHECK.json'}, 'exact_preparation_payloads')
    pin(PREP / 'run_pair.py', RUNNER_SHA)
    tree = ast.parse(raw(PREP / 'run_pair.py'))
    specs = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and
                 any(isinstance(t, ast.Name) and t.id == 'SPECS' for t in n.targets))
    need(set(specs) == {'p210_b'}, 'exact_one_role')
    spec = specs['p210_b']
    need(ROOT / spec['package'] == PACKAGE, 'literal_B_package_role')
    input_pins = js(PREP / 'INPUT_PINS.json')['inputs']
    need(len(input_pins) == 17, 'all_seventeen_explicit_preparation_inputs')
    for name, row in input_pins.items():
        pin(name, row)
    package_rows = manifest(PACKAGE, spec['manifest_sha'], 407)
    need(spec['payloads'] == 407, 'actual_initial_B_payload_count')
    for name, digest in [('verify.py', spec['verifier_sha']), ('verify.committed.py', spec['verifier_sha']),
                         ('PARAMETERS.json', spec['parameters_sha'])]:
        pin(PACKAGE / name, digest)
    pin(PACKAGE / 'CANONICAL.json', {'sha256': spec['canonical_sha'], 'bytes': spec['canonical_bytes']})
    need(raw(PACKAGE / 'CANONICAL.json') == raw(PACKAGE / 'produce01/commands/run_1/stdout'),
         'full_original_B_canonical_actual_producer_bytes')
    complete = js(PACKAGE / 'COMPLETE_SOURCE_COMMITMENT.actual.json')
    prior_compare = js(PACKAGE / 'PRE_COMPARISON_PROOF_CODE_COMMITMENT.actual.json')
    need(complete['author_A_code_or_canonical_semantics_read'] is False and
         complete['files']['verify.py'] == spec['verifier_sha'] and
         complete['files']['PARAMETERS.json'] == spec['parameters_sha'] and
         prior_compare['author_A_verifier_or_canonical_body_semantics_read'] is False and
         prior_compare['pins']['CANONICAL.json'] == spec['canonical_sha'], 'actual_declared_B_source_commitments')
    baseline = {'role': 'p210_b', 'package_payloads': 407,
        'package_manifest': val(PACKAGE / 'SHA256SUMS'), 'preparation_manifest': val(PREP / 'SHA256SUMS'),
        'verifier': val(PACKAGE / 'verify.py'), 'canonical': val(PACKAGE / 'CANONICAL.json'),
        'parameters': val(PACKAGE / 'PARAMETERS.json'),
        'package_files': sorted(str(PACKAGE / n) for n in package_rows) + [str(PACKAGE / 'SHA256SUMS')],
        'preparation_files': sorted(str(PREP / n) for n in prep_rows) + [str(PREP / 'SHA256SUMS')]}
    for name, digest in ROOT_NATIVE_KEYS.items():
        pin(QA / name, digest)
    preflight = js(QA / 'P210_B_STRICT_ROOT_PREFLIGHT.actual.json')
    need(preflight['role'] == 'ACTUAL_ROOT_READ_ONLY_PREFLIGHT_NOT_PAIR_EXECUTION' and
         preflight['cwd'] == str(ROOT) and preflight['command'] == parent_command('preflight') and
         type(preflight['result']['exit_code']) is int and preflight['result']['exit_code'] == 0,
         'actual_complete_preflight_outer_command_and_native_exit')
    expected_preflight = {k: baseline[k] for k in
        ('role', 'package_payloads', 'package_manifest', 'preparation_manifest', 'verifier', 'canonical')}
    expected_preflight.update({'status': 'PASS_READ_ONLY_PREFLIGHT_NOT_EXECUTION_OR_ACCEPTANCE',
        'target_not_created': str(OUT), 'fresh_scientific_executions': 0})
    need(json.loads(preflight['result']['output']) == expected_preflight, 'full_actual_preflight_stdout_not_pair_execution')
    prep_seal = preflight['preparation_seal_check']
    need(prep_seal['command'] == 'sha256sum -c SHA256SUMS' and prep_seal['cwd'] == str(PREP) and
         type(prep_seal['result']['exit_code']) is int and prep_seal['result']['exit_code'] == 0 and
         prep_seal['result']['output'] == ''.join(n + ': OK\n' for n in prep_rows),
         'full_actual_four_payload_native_preparation_seal')
    launch_record = js(QA / 'P210_B_STRICT_ROOT_LAUNCH.actual.json')
    completion_record = js(QA / 'P210_B_STRICT_ROOT_COMPLETION.actual.json')
    need(set(launch_record) == {'role', 'command', 'result'} and
         launch_record['role'] == 'actual root strict B pair launch' and
         launch_record['command'] == parent_command('run'), 'exact_actual_launch_no_invented_cwd_field')
    launch, completion = launch_record['result'], completion_record['result']
    need(type(launch['session_id']) is int and launch['session_id'] == completion_record['session_id'] == 31521 and
         launch['output'] == '' and launch['chunk_id'] == '9f665e' and
         completion_record['role'] == 'actual root strict B pair completion' and
         completion_record['launch_record'] == 'P210_B_STRICT_ROOT_LAUNCH.actual.json' and
         type(completion['exit_code']) is int and completion['exit_code'] == 0 and completion['chunk_id'] == '9c6226',
         'actual_empty_launch_same_31521_session_complete_native_zero_return')
    # The pinned real completion is one complete JSON object, with no heartbeat.
    native = json.loads(completion['output'])
    pair_rows = manifest(OUT, PAIR_SHA, 59)
    expected_native = {'status': 'PASS_ROOT_P210_B_STRICT_PAIR', 'errors': [],
        'source': val(PREP / 'run_pair.py'), 'verifier': val(PACKAGE / 'verify.py'),
        'role': 'p210_b', 'known_inputs': 3558, 'checks_each': [51129, 51129],
        'command_count': 10, 'closure': {'payloads': 59, 'manifest': val(OUT / 'SHA256SUMS')},
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}
    need(native == expected_native, 'entire_actual_parent_stdout_including_source_and_full_pair_seal')
    native_seal = js(QA / 'P210_B_STRICT_ROOT_SEAL.actual.json')
    need(native_seal['command'] == '/usr/bin/sha256sum -c SHA256SUMS' and native_seal['cwd'] == str(OUT) and
         type(native_seal['result']['exit_code']) is int and native_seal['result']['exit_code'] == 0 and
         native_seal['result']['chunk_id'] == 'a2b7e5' and
         native_seal['result']['output'] == ''.join(n + ': OK\n' for n in pair_rows),
         'independent_actual_all_59_payload_native_seal_full_stdout')
    entered = js(OUT / 'RUN_ENTERED.json')
    need(set(entered) == {'status', 'started_utc', 'argv', 'interpreter_argv', 'environment', 'cwd', 'source'} and
         entered['status'] == 'ENTERED_NOT_A_PRESPAWN_RECEIPT' and entered['argv'] == parent_argv('run')[6:] and
         entered['interpreter_argv'] == parent_argv('run') and entered['environment'] == ENV and
         entered['cwd'] == str(ROOT) and entered['source'] == rich_current(PREP / 'run_pair.py'),
         'entire_actual_entered_record_not_reconstructed_outer_prespawn')
    entered_time = timestamp(entered['started_utc'])
    expected_copies = {}
    for name, origin in [('run_pair.py', PREP / 'run_pair.py'), ('verify.py', PACKAGE / 'verify.py'),
                         ('PARAMETERS.json', PACKAGE / 'PARAMETERS.json')]:
        target = OUT / 'sources' / name
        expected_copies[name] = {'origin': str(origin), 'copy': str(target), **val(origin)}
        need(raw(origin) == raw(target), ('complete_original_source_copy', name))
    copies = js(OUT / 'SOURCE_ONLY_INITIAL.json')
    need(copies == expected_copies and {p.name for p in (OUT / 'sources').iterdir()} == set(copies),
         'entire_three_source_origin_copy_record_and_source_only_capsule')
    closure = js(OUT / 'PACKAGE_AND_PREPARATION_CLOSURE.json')
    need(closure == {'before': baseline, 'after': baseline}, 'complete_independently_reconstructed_preflight_closure')
    resources = js(OUT / 'RESOURCE_NAMES_BEFORE.json')
    need(resources == js(OUT / 'RESOURCE_NAMES_AFTER.json') == current_resources() and len(resources) == 3121,
         'entire_actual_and_current_3121_resource_membership')
    conf = js(OUT / 'CONFIGURATION_BEFORE.json')
    need(conf == js(OUT / 'CONFIGURATION_AFTER.json') == configuration_snapshot() and len(conf) == 41,
         'entire_independently_reconstructed_41_configuration_names_and_values')
    known = js(OUT / 'INPUTS_BEFORE.json')
    need(known == js(OUT / 'INPUTS_AFTER.json') and len(known) == 3558 and
         set(known) == known_names(baseline, resources, input_pins, copies, conf),
         'complete_expected_3558_known_union_including_all_resolved_roles')
    for name, row in known.items():
        need(set(row) == {'sha256', 'bytes', 'resolved', 'symlink'}, ('exact_known_rich_key_schema', name))
        pin(name, row)
    for phase in ('before', 'after'):
        parent_sample = js(OUT / ('observations/parent_' + phase + '.json'))
        need(parent_sample['argv'] == parent_argv('run')[6:], 'exact_actual_parent_observation_argv')
        exact_sample(parent_sample, known, OUT / 'unused_parent_cache')
    result = js(OUT / 'RESULT.json')
    need(result['status'] == native['status'] and result['errors'] == [] and result['role'] == 'p210_b' and
         result['unfinalized_native_labels'] == [] and result['no_new_all_size_proof_or_review'] is True and
         result['known_input_count'] == 3558 and result['source_only_system_python'] == str(PYTHON) and
         result['OS_syscall_trace'] == 'NOT_COLLECTED' and result['owner'] == 'OWNER_AMBER' and
         result['external_status'] == 'HOLD_EXTERNAL', 'actual_pair_result_and_unavailable_trace_scope')
    result_time = timestamp(result['ended_utc'])
    expected_commands = exact_native_argv(resources)
    commands = result['commands']
    need([c['label'] for c in commands] == list(expected_commands), 'all_ten_actual_native_labels_exact_order')
    need({p.name for p in (OUT / 'commands').iterdir()} == set(expected_commands), 'no_undeclared_native_command_directory')
    previous_end, settlements = entered_time, []
    for command in commands:
        label = command['label']
        folder = OUT / 'commands' / label
        receipt, attempt = js(folder / 'RECEIPT.json'), js(folder / 'ATTEMPT.json')
        need(receipt == {k: v for k, v in command.items() if k != 'label'}, ('entire_actual_native_record', label))
        expected_attempt = {'argv': expected_commands[label], 'cwd': str(ROOT), 'environment': ENV,
            'started_utc': attempt['started_utc'], 'timeout_seconds': 300 if label.startswith('03_verify_') else 60,
            'status': 'ATTEMPTED', 'exit_code': None, 'stdin': 'DEVNULL', 'new_owned_session_requested': True}
        need(attempt == expected_attempt and
             all(receipt[k] == v for k, v in expected_attempt.items() if k not in {'status', 'exit_code'}),
             ('all_prespawn_fields_exact_command_timeout_and_receipt_binding', label))
        need(set(receipt) == set(expected_attempt) | {'ended_utc', 'wrapper_exit_code', 'spawned', 'streams_complete',
             'timed_out', 'interrupted', 'failure', 'process_group_settlement', 'stream_scope', 'stdout', 'stderr'},
             ('complete_success_receipt_schema', label))
        need(receipt['status'] == 'COMPLETED' and
             all(type(receipt[k]) is int and receipt[k] == 0 for k in ('exit_code', 'wrapper_exit_code')) and
             receipt['streams_complete'] is True and receipt['spawned'] is True and receipt['timed_out'] is False and
             receipt['interrupted'] is False and receipt['failure'] is None, ('exact_actual_native_success_fields', label))
        begin, end = timestamp(receipt['started_utc']), timestamp(receipt['ended_utc'])
        need(previous_end <= begin <= end <= result_time, ('actual_entry_ten_command_result_chronology', label))
        previous_end = end
        settlement = receipt['process_group_settlement']
        need(set(settlement) == {'owned_pgid', 'owned_sid', 'signals', 'remaining_members', 'quiescent', 'native_returncode'} and
             type(settlement['owned_pgid']) is type(settlement['owned_sid']) is int and
             settlement['owned_pgid'] == settlement['owned_sid'] > 0 and
             settlement['quiescent'] is True and settlement['signals'] == [] and
             type(settlement['native_returncode']) is int and settlement['native_returncode'] == 0 and
             all(r['state'] == 'Z' and r['pgid'] == r['sid'] == settlement['owned_pgid'] for r in settlement['remaining_members']),
             ('actual_owned_positive_native_identity_and_settlement', label))
        settlements.append({'label': label, **settlement})
        need(receipt['stream_scope'] == 'Every emitted native byte retained in exclusive files; hashes finalized only after owned-group quiescence. A timeout/interruption remains an unsuccessful partial computation.',
             ('exact_emitted_stream_scope', label))
        for stream in ('stdout', 'stderr'):
            pin(folder / (stream + '.raw'), receipt[stream])
        need(raw(folder / 'stderr.raw') == b'', ('full_actual_empty_stderr', label))
        if receipt['argv'][0] == '/usr/bin/cmp':
            need(raw(folder / 'stdout.raw') == b'' and raw(receipt['argv'][-2]) == raw(receipt['argv'][-1]),
                 ('complete_raw_actual_native_cmp_operands', label))
    need(len({row['owned_pgid'] for row in settlements}) == 10, 'ten_distinct_actual_owned_groups')
    need(js(OUT / 'COMMAND_CLOSURE.json') == {'command_count': 10, 'native_streams_rechecked': 20,
         'scope': 'Every entire recorded receipt, pre-spawn record and raw stream rechecked after the pair.'},
         'entire_actual_command_closure_10_receipts_20_streams')
    expected_results = []
    for number in ('01', '02'):
        observed = js(OUT / ('observations/child_' + number + '.json'))
        need(observed['status'] == 'RETURNED' and observed['volatile_open_paths'] == [] and
             observed['source'] == {'path': str(OUT / 'sources/verify.py'), **val(PACKAGE / 'verify.py')} and
             observed['parameters'] == {'path': str(OUT / 'sources/PARAMETERS.json'), **val(PACKAGE / 'PARAMETERS.json')} and
             observed['scientific_argv'] == [str(OUT / 'sources/verify.py')] and
             observed['parameter_locator'] == 'sibling of scientific __file__', 'actual_single_argv_sibling_parameter_interface')
        cache = OUT / ('unused_child_' + number + '_cache')
        for phase in ('before', 'after'):
            need(observed[phase]['argv'] == observed['scientific_argv'], 'observed_scientific_argv')
            exact_sample(observed[phase], known, cache)
            need(all(not Path(r['path']).is_relative_to(ROOT) or r['path'] == str(OUT / 'sources/run_pair.py')
                     for r in observed[phase]['modules'].values()), 'no_author_A_or_other_project_module_import')
        expected_opens = {str(OUT / 'sources' / n): val(OUT / 'sources' / n) for n in ('verify.py', 'PARAMETERS.json')}
        need(observed['opened_ordinary_files'] == expected_opens and
             observed['python_open_events'] == [{'path': name, 'mode': 'r', 'flags': os.O_RDONLY | os.O_CLOEXEC}
                for name in expected_opens] and observed['nonfile_open_paths_at_end'] == [],
             'all_actual_two_raw_open_events_exact_reclassification_not_continuous_trace')
        for name, row in observed['opened_ordinary_files'].items():
            need(name in known and all(row[k] == known[name][k] for k in ('sha256', 'bytes')), ('open_coverage', name))
            pin(name, row)
        output = OUT / ('commands/03_verify_' + number + '/stdout.raw')
        need(raw(output) == raw(PACKAGE / 'CANONICAL.json'), 'entire_actual_B_canonical_bytes_not_new_science')
        data, parameters = js(output), js(PACKAGE / 'PARAMETERS.json')
        need(set(data) == {'reviewer', 'representation', 'edge_construction', 'checks', 'states', 'census'} and
             data['reviewer'] == 'p210_b_reviewer' and data[spec['check_field']] == spec['checks'] == 51129 and
             data['representation'] == parameters['carrier'] == 'integer partitions followed by distinct multiset permutations' and
             data['edge_construction'] == parameters['edges'] == 'inverse weakly sorted refinements with strict boundary descents' and
             parameters['masses'] == [row['mass'] for row in data['census']] == list(range(1, 13)) and
             data['states'] == sum(len(row['states']) for row in data['census']) == 4095 and
             sum(len(row['triangular_codes']) for row in data['census']) == sum(row['image_size'] for row in data['census']) == 265 and
             all(row['carrier_size'] == len(row['states']) == 1 << (row['mass'] - 1) and
                 sum(s['fibre'] for s in row['states']) == row['carrier_size'] for row in data['census']),
             'all_actual_original_B_schema_and_recorded_census_invariants')
        expected_results.append({'number': number, 'checks': 51129, 'stdout': val(output)})
    need(result['results'] == expected_results and [r['checks'] for r in expected_results] == native['checks_each'] and
         result['raw_canonical_comparisons'] == 2 and result['raw_pair_comparisons'] == 1,
         'entire_two_results_and_three_actual_raw_comparison_bindings')
    links = js(OUT / 'LINKED_RUNTIME.json')
    need(set(links) == {'before', 'after'} and links['before'] == links['after'] and
         all(n in known for n in links['before']), 'entire_ldd_closure')
    for label, phase in [('02_ldd_before', 'before'), ('06_ldd_after', 'after')]:
        body = raw(OUT / ('commands/' + label + '/stdout.raw'))
        paths = sorted({str(Path(os.fsdecode(p)).resolve()) for p in re.findall(rb'(/[^\s()]+)', body)
                        if Path(os.fsdecode(p)).is_file()})
        need(b'not found' not in body and paths == links[phase], 'full_actual_archived_ldd_parse')
    need(resources == current_resources() and conf == configuration_snapshot() and
         set(known) == known_names(baseline, resources, input_pins, copies, conf),
         'current_complete_resource_configuration_known_membership_second_check')
    for name, row in known.items():
        pin(name, row)
    initial_reads = dict(READS)
    for name, row in initial_reads.items():
        pin(name, row)
    extra_keys = {name: row for name, row in READS.items() if name not in known}
    print(json.dumps({'schema': 'p210-B-strict-actual-root-receiver-revision-01',
        'status': 'PASS_ROOT_P210_B_STRICT_PAIR_ORIGINAL_RECEPTION_REVISION_01',
        'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'source': val(Path(__file__).resolve()), 'preparation_seal': val(REVISION / 'SHA256SUMS'),
        'checks': CHECKS, 'physical_read_paths_rechecked': len(initial_reads),
        'read_ledger_sha256': sha256(json.dumps(initial_reads, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        'all_3558_actual_rich_keys_rechecked': True, 'known_input_ledger': val(OUT / 'INPUTS_BEFORE.json'),
        'extra_read_keys_outside_original_known_ledger': extra_keys,
        'actual_parent_session': 31521, 'actual_parent_native_exit': 0,
        'actual_root_native_seal_check': val(QA / 'P210_B_STRICT_ROOT_SEAL.actual.json'),
        'pair_manifest': val(OUT / 'SHA256SUMS'), 'pair_payloads': 59,
        'known_inputs': 3558, 'resource_names': 3121, 'configuration_names': 41,
        'checks_each': [51129, 51129], 'full_recorded_native_commands': 10,
        'all_native_argv_and_timeout_reconstructed': True, 'actual_owned_groups': settlements,
        'outer_native_bindings': {n: val(QA / n) for n in ROOT_NATIVE_KEYS},
        'outer_launch_wrapper_cwd_field': 'NOT_RECORDED; actual cwd bound by RUN_ENTERED and existing preflight, not retrofilled',
        'actual_root_stdout': 'empty first chunk + one complete final JSON, no heartbeat in this actual run',
        'actual_new_scientific_runs_in_pair': 2, 'fresh_scientific_runs_by_this_inspector': 0,
        'new_child_commands_by_this_inspector': 0, 'new_builds': 0, 'new_page_views': 0,
        'old_runner_or_inspector_imports_or_executions': 0,
        'scope': 'Actual initial-B strict-pair originals only. No accepted B delta, proof, review, Round2, terminal build/view or five-paper PASS. No old A deep resource-ledger expansion or reconstructed OS/startup trace.',
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
