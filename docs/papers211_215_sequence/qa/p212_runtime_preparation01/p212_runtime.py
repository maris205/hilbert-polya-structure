#!/usr/bin/env python3
"""Bounded P212 runtime adapter. Science is disabled without a root binding.

The same source supplies outer capture, launcher, recorder and child modes.
Only the child mode executes a root-bound source; probe is import-only and
never reads/imports a scientific file. No canonical is silently adopted. This author-only SOURCE_ONLY adaptation
requires separate root source reception and approved discovery/science bindings.
"""
import ast
import itertools
import json
import linecache
import locale
import math
import os
from pathlib import Path
import sys
import tokenize
import traceback
import types

HERE = Path(__file__).resolve().parent
CORE_PATH = HERE / 'runtime_core.py'
core = types.ModuleType('_p212_runtime_core')
core.__file__ = str(CORE_PATH)
sys.modules[core.__name__] = core
exec(compile(CORE_PATH.read_bytes(), str(CORE_PATH), 'exec'), core.__dict__)
ROOT = core.ROOT
ENV = core.ENV
PYTHON = Path('/usr/bin/python3.10')
IMPORT_PATH = ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload']
SOURCE_FILES = (Path(__file__).resolve(), CORE_PATH)
ROLE_IMPORTS = ['itertools', 'json', 'math', 'sys', 'fractions']
PAPER = ROOT / 'papers/212-closed-pointer-orbits'
SCIENCE_INTERFACE = {
    'verify.py': {'sha256': '16cc2ff86854c6c28d530de65225b941f9e063fa22159ccd8f0c4082b80654e7', 'bytes': 40430},
    'PARAMETERS.json': {'sha256': '0870d9de8a1e2dde2c568656ea69b39511ae3a8ebf992f787c6e5ae060ca4550', 'bytes': 609},
}
TOP_KEYS = ['schema', 'parameters', 'role', 'method', 'excluded_claims',
            'core_catalogues', 'carriers', 'series', 'coverage_limits',
            'predicates', 'predicate_census', 'summary']
PREPARATION_SOURCES = (CORE_PATH, Path(__file__).resolve(), HERE / 'prepare_runtime.py')
CONFIG_PATHS = (
    '/dev/null',
    '/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
    '/etc/localtime', '/etc/locale.conf', '/etc/default/locale',
    '/etc/nsswitch.conf', '/etc/passwd', '/etc/group',
    '/etc/ssl/openssl.cnf', '/usr/lib/ssl/openssl.cnf',
    '/usr/lib/locale/locale-archive', '/usr/lib/python310.zip',
    '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg',
    '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2',
    '/usr/lib/python3.10/config-3.10-x86_64-linux-gnu/Makefile',
    '/usr/include/python3.10/pyconfig.h',
    '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules',
    '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache',
    '/usr/share/locale/C.UTF-8/LC_MESSAGES/libc.mo',
    '/usr/share/locale/C.utf8/LC_MESSAGES/libc.mo',
    '/usr/share/locale/C/LC_MESSAGES/libc.mo',
)
MEMBER_DIRS = (
    '/usr/lib/locale/C.utf8', '/usr/lib/locale/C.utf8/LC_MESSAGES',
    '/usr/lib/x86_64-linux-gnu/gconv',
    '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.d',
    '/etc/ld.so.conf.d',
)
NATIVE_FILES = ['/usr/bin/python3.10', '/usr/bin/cmp', '/usr/bin/env',
                '/usr/bin/ldd', '/bin/bash', '/bin/sh']


def state(path, with_bytes=True):
    p = Path(path)
    row = {'lexists': core.lexists(p), 'exists': p.exists(),
           'is_file': p.is_file(), 'is_dir': p.is_dir(),
           'is_character_device': p.is_char_device(),
           'resolved': str(p.resolve()),
           'symlink': os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        info = p.stat()
        row['character_device'] = {'major': os.major(info.st_rdev), 'minor': os.minor(info.st_rdev),
                                   'mode': info.st_mode}
    if with_bytes and p.is_file():
        row.update(core.value(p))
    return row


def configuration():
    paths = set(CONFIG_PATHS)
    for directory in ('/usr/bin', '/usr/lib'):
        paths.update(str(Path(directory) / name) for name in
                     ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
    members = {}
    for directory in MEMBER_DIRS:
        p = Path(directory)
        row = {'directory': state(p, False), 'members': {}}
        if p.is_dir():
            row['members'] = {q.name: state(q, False) for q in sorted(p.iterdir())}
            if directory != '/usr/lib/x86_64-linux-gnu/gconv':
                paths.update(str(q) for q in p.iterdir() if q.is_file())
        members[directory] = row
    config = {p: state(p) for p in sorted(paths)}
    core.need(config['/dev/null']['is_character_device'] and
              config['/dev/null']['character_device']['major'] == 1 and
              config['/dev/null']['character_device']['minor'] == 3, 'declared_DEVNULL_character_device')
    core.need(not config['/etc/ld.so.preload']['lexists'] and
              not config['/usr/lib/python310.zip']['lexists'], 'no_preload_or_system_zip')
    core.need(all(not row['lexists'] for p, row in config.items()
                  if p.endswith(('._pth', '/pyvenv.cfg'))), 'no_path_injection_configuration')
    core.need(config['/usr/lib/locale/C.utf8/LC_CTYPE']['is_file'], 'explicit_launcher_LC_CTYPE')
    core.need(config['/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache']['is_file'],
              'explicit_launcher_gconv_cache')
    return {'paths': config, 'memberships': members,
            'scope': 'Listed configuration and direct directory membership only; no host/library/stdlib recursion.'}


def loader_search_scope(config):
    lines = [s.strip() for s in Path('/etc/ld.so.conf').read_text().splitlines()
             if s.strip() and not s.lstrip().startswith('#')]
    core.need(lines == ['include /etc/ld.so.conf.d/*.conf'], 'reviewed_single_loader_include')
    result = {}
    for ptext in config['paths']:
        p = Path(ptext)
        if p.parent == Path('/etc/ld.so.conf.d') and p.is_file():
            for line in p.read_text().splitlines():
                clean = line.split('#', 1)[0].strip()
                if not clean:
                    continue
                core.need(clean.startswith('/') and not any(c in clean for c in '*?[]\t '),
                          ('unreviewed_loader_configuration_directive_HOLD', ptext, clean))
                result[clean] = state(clean, False)
    return result


def settings(cache, cwd):
    core.need(Path(sys.executable).resolve() == PYTHON and sys.version_info[:2] == (3, 10),
              'system_python_3_10')
    core.need(dict(os.environ) == ENV and Path.cwd() == Path(cwd), 'actual_ENV4_and_cwd')
    core.need(sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.optimize == 0 and
              sys.dont_write_bytecode, 'actual_I_S_B_unoptimized')
    core.need(sys.pycache_prefix == str(cache) and not core.lexists(cache), 'distinct_absent_cache')
    core.need(sys.path == IMPORT_PATH and not core.lexists(IMPORT_PATH[0]), 'source_only_import_path')


def sample():
    return {**core.ordinary_sample(), 'interpreter_argv': sys.orig_argv,
            'filesystem_encoding': sys.getfilesystemencoding(),
            'filesystem_errors': sys.getfilesystemencodeerrors(),
            'default_encoding': sys.getdefaultencoding(),
            'preferred_encoding': locale.getpreferredencoding(False),
            'LC_CTYPE': locale.setlocale(locale.LC_CTYPE),
            'stdin_encoding': sys.stdin.encoding, 'stdout_encoding': sys.stdout.encoding,
            'stderr_encoding': sys.stderr.encoding}


def covered_sample(row, known, cache, cwd, allowed_project_modules):
    settings(cache, cwd)
    core.need(row['environment'] == ENV and row['cwd'] == str(cwd) and
              row['executable'] == str(PYTHON) and row['sys_path'] == IMPORT_PATH and
              row['pycache_prefix'] == str(cache) and not row['cache_lexists'], 'sample_settings')
    for p, pin in list(row['mapped_files'].items()) + [
            (m['path'], {k: m[k] for k in ('sha256', 'bytes')}) for m in row['modules'].values()]:
        core.need(p in known and all(known[p][k] == pin[k] for k in pin), ('sample_input_coverage', p))
        core.pin(p, pin)
    for module in row['modules'].values():
        p = Path(module['path'])
        core.need(not p.is_relative_to(ROOT) or str(p) in allowed_project_modules,
                  ('project_module_not_registered', str(p)))


def hook_events(attempt, scientific=False):
    events, active = [], [True]
    def hook(event, args):
        if active[0] and scientific and event in (
                'subprocess.Popen', 'os.fork', 'os.forkpty', 'os.posix_spawn',
                'os.exec', 'os.system', 'os.kill', 'os.killpg'):
            events.append({'forbidden_process_event': event})
            raise RuntimeError('scientific process/signal creation is outside this binding: ' + event)
        if not active[0] or event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        p = Path(os.fsdecode(args[0]))
        p = p if p.is_absolute() else Path.cwd() / p
        flags = args[2] if isinstance(args[2], int) else 0
        writing = bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        events.append({'path': str(p), 'mode': args[1], 'flags': args[2], 'writing': writing})
        allowed_devnull = not scientific and p == Path('/dev/null') and p.is_char_device()
        if writing and not allowed_devnull and (scientific or not p.is_relative_to(attempt)):
            raise RuntimeError('unapproved ordinary file write: ' + str(p))
        if p.suffix in ('.pyc', '.pyo') and core.lexists(p):
            raise RuntimeError('inherited bytecode read: ' + str(p))
    sys.addaudithook(hook)
    return events, active


def covered_opens(events, known, cache, attempt, scientific, capsule_files):
    ordinary, absent, volatile, outputs, devices = {}, [], [], [], {}
    core.need(all('forbidden_process_event' not in row for row in events), 'no_scientific_process_events')
    for ptext in sorted({row['path'] for row in events}):
        p = Path(ptext)
        if p == Path('/dev/null') and not scientific:
            core.need(p.is_char_device(), 'DEVNULL_still_character_device')
            devices[ptext] = state(p, False)
        elif ptext.startswith('/proc/'):
            core.need(not scientific, ('scientific_volatile_read', ptext))
            volatile.append(ptext)
        elif not scientific and p.is_relative_to(attempt):
            outputs.append(ptext)
        elif p.is_file():
            resolved = str(p.resolve(strict=True))
            core.need(resolved in known, ('unfrozen_ordinary_input', ptext, resolved))
            core.pin(p, known[resolved])
            if scientific and p.is_relative_to(ROOT):
                core.need(resolved in capsule_files, ('scientific_read_outside_own_capsule', resolved))
            ordinary[resolved] = core.value(p)
        else:
            core.need(p.is_relative_to(cache) and not core.lexists(p) and not core.lexists(cache),
                      ('unregistered_nonfile_open', ptext))
            absent.append(ptext)
    return {'events': events, 'ordinary_files': ordinary, 'absent_cache_probes': absent,
            'volatile_proc_reads': volatile, 'own_attempt_io': outputs,
            'nonordinary_devices': devices,
            'scope': 'Post-hook Python opens and discrete file-backed maps/modules; not OS/startup/escaped-descendant tracing.'}


def exact_json(data):
    def pairs(items):
        result = {}
        for key, val in items:
            core.need(key not in result, ('duplicate_JSON_key', key))
            result[key] = val
        return result
    def bad_constant(value):
        raise ValueError('nonfinite JSON constant: ' + value)
    result = json.loads(data, object_pairs_hook=pairs, parse_constant=bad_constant, parse_float=bad_constant)
    core.need(isinstance(result, dict), 'one_JSON_object')
    encoded = (json.dumps(result, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False) + '\n').encode()
    core.need(data == encoded, 'entire_deterministic_compact_sorted_JSON_plus_LF')
    return result


def check_schema(data, schema):
    row = exact_json(data)
    core.need(set(row) == set(schema['top_keys']), 'exact_role_top_keys')
    core.need(bool(schema['equalities']), 'nonempty_root_reviewed_schema_checks')
    for check in schema['equalities']:
        value = row
        for key in check['path']:
            value = value[key]
        core.need(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False) ==
                  json.dumps(check['value'], sort_keys=True, separators=(',', ':'), allow_nan=False),
                  ('role_schema_equality_type_sensitive', check['path']))
    for check in schema.get('lengths', []):
        value = row
        for key in check['path']:
            value = value[key]
        core.need(len(value) == check['value'], ('role_schema_length', check['path']))
    return row


def load_binding(path, digest, attempt):
    path = Path(path)
    core.pin(path, digest)
    binding = core.read_json(path)
    core.need(binding['format'] == 'p212-runtime-binding-v1' and binding['approved'] is True,
              'ROOT_APPROVED_BINDING_REQUIRED_NO_SCIENCE')
    core.need(binding['mode'] in ('initial', 'pair') and binding['role'] == 'author',
              'explicit_single_role_and_mode')
    core.need(binding['attempt'] == str(attempt) and attempt.is_absolute() and
              attempt.parent.resolve(strict=True) == attempt.parent, 'exact_new_physical_attempt_parent')
    parent = ROOT / 'docs/papers211_215_sequence/qa/root_replays'
    core.need(binding['purpose'] == 'P212_AUTHOR_MANUSCRIPT' and attempt.parent == parent,
              'root_only_author_attempt_scope')
    core.need(binding['reviewed_static_source_import_closure'] is True and
              binding['reviewed_schema_and_parameters'] is True and
              binding['reviewed_compile_exec_interface'] is True and
              binding['complete_semantic_reception_is_separate'] is True, 'root_source_review_gate')
    core.need(binding['schema']['top_keys'] == TOP_KEYS, 'exact_received_P212_top_key_role')
    core.need(binding['declared_imports'] == ROLE_IMPORTS and binding['local_helper_imports'] == [],
              'current_adapter_supports_only_reviewed_standalone_interface_HOLD_other_imports')
    core.need(set(binding['adapter_sources']) == {str(p) for p in SOURCE_FILES}, 'exact_adapter_sources')
    for p, pin in binding['adapter_sources'].items():
        core.pin(p, pin)
    core.need(all(type(binding['timeouts'][key]) is int and binding['timeouts'][key] > 0
                  for key in ('science', 'native', 'envelope')), 'frozen_positive_deadlines')
    core.need(binding['success_stderr'] == 'empty', 'declared_empty_science_stderr')
    names = [row['name'] for row in binding['capsule_files']]
    core.need(len(names) == len(set(names)) and set(names) == {binding['entry'], binding['parameters']},
              'exact_two_file_standalone_capsule')
    core.need(all(Path(n).name == n and n not in ('', '.', '..') and
                  not n.endswith(('.pyc', '.pyo')) for n in names), 'safe_source_only_capsule_names')
    core.need(binding['entry'] == 'verify.py' and binding['parameters'] == 'PARAMETERS.json' and
              binding['argv_template'] == ['$ENTRY', '--parameters', '$PARAMETERS'] and
              binding['parameter_locator'] == 'explicit_absolute_argv',
              'exact_P212_two_file_absolute_parameter_interface')
    core.need(names == ['verify.py', 'PARAMETERS.json'], 'exact_ordered_P212_capsule_roles')
    for row in binding['capsule_files']:
        core.need(row['path'] == str(PAPER / row['name']) and
                  {key: row[key] for key in ('sha256', 'bytes')} == SCIENCE_INTERFACE[row['name']],
                  ('exact_received_P212_source_interface', row['name']))
    core.need(not core.lexists(PAPER / 'canonical.stdout.json'), 'historical_prospective_name_stays_absent')
    canonical = binding['canonical']
    core.need(canonical['path'] == str(PAPER / 'CANONICAL.json'), 'formal_root_fixed_canonical_role')
    if binding['mode'] == 'initial':
        core.need(canonical['sha256'] is None and canonical['bytes'] is None and not core.lexists(canonical['path']),
                  'INITIAL_requires_absent_unadopted_canonical_target')
    else:
        core.pin(canonical['path'], canonical)
    core.need(bool(binding['provenance_inputs']), 'nonempty_root_reception_and_authority_provenance')
    return binding


def load_discovery(path, digest):
    path = Path(path)
    core.need(path.is_absolute(), 'absolute_discovery_approval')
    core.pin(path, digest)
    binding = core.read_json(path)
    core.need(binding['format'] == 'p212-import-discovery-binding-v1' and binding['approved'] is True and
              binding['scope'] == 'IMPORT_ONLY_NO_SCIENTIFIC_SOURCE_READ' and
              binding['reviewed_all_preparation_sources'] is True, 'SEPARATE_ROOT_DISCOVERY_APPROVAL_REQUIRED')
    core.need(binding['declared_imports'] == ROLE_IMPORTS, 'exact_discovery_import_declaration')
    core.need(set(binding['source_inputs']) == {str(p) for p in PREPARATION_SOURCES},
              'exact_three_preparation_source_inputs')
    for p, pin in binding['source_inputs'].items():
        core.pin(p, pin)
    core.need(type(binding['native_timeout_seconds']) is int and binding['native_timeout_seconds'] > 0,
              'finite_positive_integer_discovery_deadline')
    out = Path(binding['output'])
    core.need(out.is_absolute() and out.parent == ROOT / 'docs/papers211_215_sequence/qa' and
              out.name.startswith('p212_runtime_discovery') and
              out.parent.resolve(strict=True) == out.parent, 'exact_external_discovery_output_role')
    core.need(bool(binding['provenance_inputs']), 'documented_root_discovery_authority')
    for row in binding['provenance_inputs']:
        core.need(Path(row['path']).suffix in ('.md', '.json', '.sha256'),
                  'discovery_documentary_provenance_only')
        core.need(not Path(row['path']).is_relative_to(PAPER), 'no_paper_file_read_during_discovery')
        core.pin(row['path'], row)
    return binding


def frozen_inputs(binding, binding_path):
    lock_path = Path(binding['runtime_lock']['path'])
    core.pin(lock_path, binding['runtime_lock'])
    lock = core.read_json(lock_path)
    core.need(lock['format'] == 'p212-bounded-runtime-lock-v1' and lock['declared_imports'] == ROLE_IMPORTS,
              'matching_prepared_import_closure')
    config = configuration()
    core.need(config == lock['configuration'], 'entire_pre_frozen_config_and_membership')
    core.need(loader_search_scope(config) == lock['loader_search_directory_states'],
              'entire_pre_frozen_loader_search_directory_states')
    expected = dict(lock['files'])
    expected.update(binding['adapter_sources'])
    expected[str(binding_path)] = core.rich(binding_path)
    expected[str(lock_path)] = core.rich(lock_path)
    for row in binding['capsule_files'] + binding.get('provenance_inputs', []):
        expected[row['path']] = row
    if binding['mode'] == 'pair':
        expected[binding['canonical']['path']] = binding['canonical']
    known = {}
    for p, pin in sorted(expected.items()):
        core.pin(p, pin)
        actual = core.rich(p)
        if 'resolved' in pin:
            core.need(actual == {k: pin[k] for k in actual}, ('entire_runtime_rich_pin', p))
        known[p] = actual
        known[actual['resolved']] = core.rich(actual['resolved'])
    return known, lock, config


def full_input_recapture(known):
    return {p: core.rich(p) for p in known}


def stage_path(attempt, stage):
    core.need(stage in ('outer', 'launcher', 'recorder', 'child01', 'child02'), 'exact_stage')
    return attempt / stage


def worker_argv(stage, binding_path, digest, attempt):
    return [str(PYTHON), '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(attempt / ('never_created_' + stage + '_cache')),
            str(Path(__file__).resolve()), stage, str(binding_path), digest, str(attempt)]


def closed_stage(attempt, stage, exit_code):
    out = stage_path(attempt, stage)
    rows = core.manifest(out)
    result = core.read_json(out / 'RESULT.json')
    core.need(result['stage'] == stage and result['status'] in ('PASS', 'FAIL_PRESERVED'),
              'closed_stage_result')
    core.need((exit_code == 0) == (result['status'] == 'PASS'), 'actual_native_exit_matches_stage_result')
    return {'status': result['status'], 'payloads': len(rows), 'manifest': core.rich(out / 'SHA256SUMS')}


def ldd_check(label, lock, known, binding, cwd):
    raw = core.command(label, ['/usr/bin/ldd'] + lock['ldd_targets'],
                       timeout=binding['timeouts']['native'], cwd=cwd)
    core.need(b'not found' not in raw, 'no_unresolved_ELF_linkage')
    paths = sorted({os.fsdecode(p) for p in core.re.findall(rb'(/[^\s()]+)', raw)
                    if Path(os.fsdecode(p)).is_file()})
    core.need(paths == lock['ldd_paths'], 'exact_frozen_ELF_linkage_membership')
    for p in paths:
        core.need(p in known, ('ELF_path_not_prefrozen', p))
        core.pin(p, known[p])
    return paths


def run_stage(stage, binding_path, digest, attempt):
    binding = load_binding(binding_path, digest, attempt)
    out = stage_path(attempt, stage)
    cache = attempt / ('never_created_' + stage + '_cache')
    capsule = attempt / 'recorder/capsule'
    cwd = capsule if stage.startswith('child') else ROOT
    settings(cache, cwd)
    if stage == 'outer':
        core.need(not core.lexists(attempt), 'refuse_existing_attempt')
        attempt.mkdir(mode=0o700)
    core.need(attempt.is_dir() and not core.lexists(out), 'exclusive_stage_attempt')
    out.mkdir(mode=0o700)
    (out / 'commands').mkdir()
    core.OUT, core.COMMANDS, core.UNFINALIZED_NATIVE = out, [], []
    core.write_json(out / 'ENTERED.json', {'stage': stage, 'argv': sys.argv, 'orig_argv': sys.orig_argv,
                    'cwd': str(Path.cwd()), 'environment': dict(os.environ), 'cache': str(cache),
                    'started_utc': core.now(), 'status': 'ENTERED_NOT_NATIVE_PRESPAWN'})
    errors, known, lock, config, output_info = [], None, None, None, {}
    unknown_descendants, exit_code = False, 0
    try:
        known, lock, config = frozen_inputs(binding, binding_path)
        if stage.startswith('child'):
            for row in binding['capsule_files']:
                p = capsule / row['name']
                core.pin(p, row)
                known[str(p)] = core.rich(p)
        core.write_json(out / 'INPUTS_BEFORE.json', known)
        core.write_json(out / 'CONFIGURATION_BEFORE.json', config)
        before = sample()
        covered_sample(before, known, cache, cwd, {str(p) for p in SOURCE_FILES})
        core.write_json(out / 'RUNTIME_BEFORE.json', before)
        events, active = hook_events(attempt, scientific=stage.startswith('child'))
        try:
            if stage in ('outer', 'launcher'):
                child_stage = 'launcher' if stage == 'outer' else 'recorder'
                core.command('01_' + child_stage, worker_argv(child_stage, binding_path, digest, attempt),
                             timeout=binding['timeouts']['envelope'], cwd=ROOT,
                             require_success=False, stderr_policy='retain')
                row = core.COMMANDS[-1]
                try:
                    closure = closed_stage(attempt, child_stage, row['exit_code'])
                except BaseException:
                    unknown_descendants = True
                    raise
                core.need(row['exit_code'] == 0 and row['streams_complete'] and
                          not row['process_group_settlement']['signals'] and closure['status'] == 'PASS',
                          'successful_closed_native_envelope')
                output_info = {'child_stage': child_stage, 'native_receipt': row, 'closed_child': closure}
            elif stage == 'recorder':
                capsule.mkdir()
                copies = []
                for number, row in enumerate(binding['capsule_files']):
                    p = capsule / row['name']
                    core.write_bytes(p, Path(row['path']).read_bytes())
                    core.pin(p, row)
                    known[str(p)] = core.rich(p)
                    copies.append({'original': row['path'], 'copy': str(p), **core.value(p)})
                    core.command('00_copy_' + str(number), ['/usr/bin/cmp', '--', row['path'], str(p)],
                                 timeout=binding['timeouts']['native'], cwd=ROOT)
                core.need({p.name for p in capsule.iterdir()} == {r['name'] for r in binding['capsule_files']},
                          'exact_source_only_capsule_inventory')
                core.write_json(out / 'SOURCE_COPIES.json', copies)
                core.write_json(out / 'CAPSULE_ADDED_INPUTS.json', {r['copy']: known[r['copy']] for r in copies})
                core.write_json(out / 'INPUTS_BEFORE_SCIENCE.json', known)
                ldd_check('01_ldd_before', lock, known, binding, ROOT)
                streams = []
                for number in ('01',) if binding['mode'] == 'initial' else ('01', '02'):
                    label = '03_verify_' + number
                    raw = core.command(label, worker_argv('child' + number, binding_path, digest, attempt),
                                       timeout=binding['timeouts']['science'], cwd=capsule, require_success=False)
                    row = core.COMMANDS[-1]
                    try:
                        closure = closed_stage(attempt, 'child' + number, row['exit_code'])
                    except BaseException:
                        unknown_descendants = True
                        raise
                    core.need(row['exit_code'] == 0 and row['streams_complete'] and row['stderr']['bytes'] == 0 and
                              not row['process_group_settlement']['signals'] and closure['status'] == 'PASS',
                              'successful_scientific_native_command')
                    check_schema(raw, binding['schema'])
                    streams.append(out / 'commands' / label / 'stdout.raw')
                if binding['mode'] == 'pair':
                    for number, p in enumerate(streams, 1):
                        core.command('04_canonical_' + str(number), ['/usr/bin/cmp', '--', str(p), binding['canonical']['path']],
                                     timeout=binding['timeouts']['native'], cwd=ROOT)
                    core.command('05_pair', ['/usr/bin/cmp', '--', str(streams[0]), str(streams[1])],
                                 timeout=binding['timeouts']['native'], cwd=ROOT)
                ldd_check('06_ldd_after', lock, known, binding, ROOT)
                expected = ['00_copy_0', '00_copy_1', '01_ldd_before', '03_verify_01']
                if binding['mode'] == 'pair':
                    expected += ['03_verify_02', '04_canonical_1', '04_canonical_2', '05_pair']
                expected += ['06_ldd_after']
                core.need([r['label'] for r in core.COMMANDS] == expected, 'exact_declared_command_census')
                output_info = {'mode': binding['mode'], 'raw_stdout': [{'path': str(p), **core.value(p)} for p in streams],
                               'canonical_policy': 'initial stdout requires separate root acceptance/publication; pair never adopts or replaces canonical',
                               'actual_raw_comparisons': 3 if binding['mode'] == 'pair' else 0}
            else:
                replacements = {'$ENTRY': str(capsule / binding['entry']), '$PARAMETERS': str(capsule / binding['parameters'])}
                sys.argv = [replacements.get(token, token) for token in binding['argv_template']]
                scientific_argv = list(sys.argv)
                source = capsule / binding['entry']
                try:
                    exec(compile(source.read_bytes(), str(source), 'exec'),
                         {'__name__': '__main__', '__file__': str(source)})
                    outcome = 'RETURNED'
                except SystemExit as exc:
                    if exc.code not in (None, 0):
                        raise
                    outcome = 'SYSTEM_EXIT_ZERO'
                core.need(sys.argv == scientific_argv, 'scientific_argv_not_mutated')
                output_info = {'scientific_argv': scientific_argv, 'parameter_locator': binding['parameter_locator'],
                               'scientific_outcome': outcome, 'source': core.rich(source), 'cwd': str(cwd)}
        finally:
            active[0] = False
            core.write_json(out / 'OPEN_EVENTS_RAW.json', events)
            observed = covered_opens(events, known, cache, attempt, stage.startswith('child'),
                                     {str(capsule / r['name']) for r in binding['capsule_files']})
            core.write_json(out / 'OPEN_OBSERVATIONS.json', observed)
    except BaseException as exc:
        errors.append({'type': type(exc).__name__, 'error': repr(exc), 'traceback': traceback.format_exc()})
        if stage.startswith('child'):
            traceback.print_exc(file=sys.stderr)
        exit_code = exc.code if isinstance(exc, SystemExit) and isinstance(exc.code, int) and exc.code != 0 else 1
    finally:
        if known is not None:
            try:
                after_known = full_input_recapture(known)
                core.write_json(out / 'INPUTS_AFTER.json', after_known)
                core.need(after_known == known, 'entire_input_set_unchanged')
                after_config = configuration()
                core.write_json(out / 'CONFIGURATION_AFTER.json', after_config)
                core.need(after_config == config, 'entire_configuration_membership_unchanged')
                core.need(loader_search_scope(after_config) == lock['loader_search_directory_states'],
                          'entire_loader_search_directory_states_unchanged')
                after = sample()
                core.write_json(out / 'RUNTIME_AFTER.json', after)
                covered_sample(after, known, cache, cwd, {str(p) for p in SOURCE_FILES})
                if binding['mode'] == 'initial':
                    core.need(not core.lexists(binding['canonical']['path']), 'initial_target_still_unpublished')
                core.need(not core.lexists(PAPER / 'canonical.stdout.json'), 'historical_name_still_absent')
                core.need(all(not core.lexists(attempt / ('never_created_' + s + '_cache'))
                              for s in ('outer', 'launcher', 'recorder', 'child01', 'child02')), 'all_cache_prefixes_remain_absent')
            except BaseException as exc:
                errors.append({'stage': 'after', 'error': repr(exc), 'traceback': traceback.format_exc()})
                exit_code = 1
    result = {'stage': stage, 'role': binding['role'], 'mode': binding['mode'],
              'status': 'FAIL_PRESERVED' if errors else 'PASS', 'errors': errors,
              'wrapper_return': exit_code, 'commands': core.COMMANDS, 'output': output_info,
              'unknown_descendant_closure': unknown_descendants, 'unfinalized_native': core.UNFINALIZED_NATIVE,
              'scope': 'Bounded infrastructure execution evidence, not a proof, review or hermetic runtime trace.'}
    core.write_json(out / 'RESULT.json', result)
    if unknown_descendants or core.UNFINALIZED_NATIVE:
        core.write_json(out / 'UNCLOSED_NO_SEAL.json', {'status': 'UNCLOSED_NO_SEAL', 'reason': 'unknown or unsettled native writer'})
        return 1
    core.seal()
    if stage == 'outer':
        core.OUT = attempt
        final = core.seal()
        print(json.dumps({'status': result['status'], 'attempt': str(attempt), 'seal': final}, sort_keys=True))
    return exit_code


def probe(tag, cache, cwd, approval_path, digest):
    approval = load_discovery(approval_path, digest)
    core.need(tag in ('outer', 'launcher', 'recorder', 'child'), 'all_layer_probe_tag')
    out = Path(approval['output'])
    expected_cwd = out / 'empty_probe_capsule' if tag == 'child' else ROOT
    core.need(cache == out / ('never_created_probe_' + tag + '_cache') and cwd == expected_cwd,
              'exact_bound_probe_cache_and_cwd')
    if tag == 'child':
        core.need(cwd.is_dir() and not list(cwd.iterdir()), 'empty_import_only_probe_capsule')
    settings(cache, cwd)
    for name in ROLE_IMPORTS:
        __import__(name)
    config = configuration()
    row = sample()
    print(json.dumps({'status': 'IMPORT_ONLY_NO_SCIENTIFIC_SOURCE_READ', 'layer': tag,
                      'declared_imports': ROLE_IMPORTS, 'configuration': config, 'sample': row}, sort_keys=True))


def main():
    if len(sys.argv) == 7 and sys.argv[1] == 'probe':
        probe(sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4]), Path(sys.argv[5]), sys.argv[6])
        return 0
    core.need(len(sys.argv) == 5, 'stage BINDING EXPECTED_BINDING_SHA256 ABSOLUTE_ATTEMPT')
    return run_stage(sys.argv[1], Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4]))


if __name__ == '__main__':
    raise SystemExit(main())
