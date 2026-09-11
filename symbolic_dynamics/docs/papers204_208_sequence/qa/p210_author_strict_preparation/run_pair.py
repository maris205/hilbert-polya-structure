#!/usr/bin/env python3
"""Root strict P210 author pair on the unchanged original N=1..12 box.
Only child() executes the pinned verifier. Source-only no-site/no-old-cache
Python, full known before/after dependency keys and complete raw native cmp.
Initial author package is complete at this pair; later root lifecycle/freeze
additions never rewrite its immutable author-handoff seal or historical keys.
This is root integration by a proof contributor, not manuscript review.
"""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import sysconfig

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers204_208_sequence/qa/p210_author_strict_preparation'
SPECS = {
    "p210_author": {
        "package": "papers/210-weakly-increasing-run-aggregation",
        "payloads": 489,
        "manifest_sha": "b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c",
        "verifier_sha": "3a39b297b7140f6c63373ecd5434c8e631ed0d0da3dd41df2442f87c0c8a1c94",
        "canonical_sha": "6804839eaff6983bcf363232ae71fecfac60b98c6c55814d75a3fc400c1d56fc",
        "canonical_bytes": 6471668,
        "check_field": "checks",
        "checks": 197471
    }
}
ROLE = SPEC = PACKAGE = OUT = VERIFIER_SHA = None
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PYTHON = Path('/usr/bin/python3.10')
STDLIB = Path('/usr/lib/python3.10')
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
DATA_ROOTS = tuple(map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')))
IMPORT_PATH = ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload']
COMMANDS = []


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


def settings(cache, script):
    need(Path(__file__).resolve() == script, ('exact_entry_source', str(script)))
    need(Path(sys.executable).resolve() == PYTHON and sys.version_info[:2] == (3, 10), 'require_system_python_3_10')
    need(sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode, 'require_I_S_B_unoptimized')
    need(dict(os.environ) == ENV and Path.cwd() == ROOT, 'require_exact_sanitized_environment_and_workspace_cwd')
    need(sys.pycache_prefix == str(cache) and not lexists(cache), ('require_absent_explicit_cache', str(cache)))
    need(sys.path == IMPORT_PATH and not lexists(IMPORT_PATH[0]), ('require_source_only_system_import_path_and_absent_zip', sys.path))


def select_role(role):
    global ROLE, SPEC, PACKAGE, OUT, VERIFIER_SHA
    need(role in SPECS, ('exact_P210_author_role', role))
    ROLE, SPEC = role, SPECS[role]
    PACKAGE = ROOT / SPEC['package']
    OUT = ROOT / 'docs/papers204_208_sequence/qa/root_replays/p210_author_strict_pair_01'
    VERIFIER_SHA = SPEC['verifier_sha']


def preflight(args):
    rows = manifest(PACKAGE, SPEC['manifest_sha'], SPEC['payloads'])
    prep_rows = manifest(PREP, args.expected_preparation_sha256, 4)
    need(set(prep_rows) == {'run_pair.py', 'README.md', 'INPUT_PINS.json', 'STATIC_CHECK.json'}, 'exact_preparation_payloads')
    for name, expected in read_json(PREP / 'INPUT_PINS.json')['inputs'].items():
        pin(name, expected)
    pin(PACKAGE / 'verify.py', VERIFIER_SHA)
    pin(PACKAGE / 'CANONICAL.json', {'sha256': SPEC['canonical_sha'], 'bytes': SPEC['canonical_bytes']})
    data = read_json(PACKAGE / 'CANONICAL.json')
    check_original_output(data)
    return {'role': ROLE, 'package_payloads': len(rows), 'package_manifest': value(PACKAGE / 'SHA256SUMS'),
            'preparation_manifest': value(PREP / 'SHA256SUMS'), 'verifier': value(PACKAGE / 'verify.py'),
            'canonical': value(PACKAGE / 'CANONICAL.json'),
            'package_files': sorted(str(PACKAGE / n) for n in rows) + [str(PACKAGE / 'SHA256SUMS')],
            'preparation_files': sorted(str(PREP / n) for n in prep_rows) + [str(PREP / 'SHA256SUMS')]}


def check_original_output(data):
    need(data['schema'] == 'P210_AUTHOR_FULL_CANONICAL_V1' and data['mass_box'] == [1, 12], 'literal_original_scope')
    need(data['checks'] == sum(data['checks_by_kind'].values()) == 197471, 'exact_original_assertion_count')
    need(data['totals'] == {'states': 4095, 'edges': 4095, 'targets': 4095, 'image_objects': 265,
                           'triangular_objects': 265, 'surplus_witnesses': 28}, 'entire_original_census')
    need([m['N'] for m in data['masses']] == list(range(1, 13)) and
         sum(len(m['states']) for m in data['masses']) == 4095 and
         sum(len(m['targets']) for m in data['masses']) == 4095 and
         sum(len(m['triangular_objects']) for m in data['masses']) == 265, 'complete_original_output_rows')


def resource_names():
    names = {str(PYTHON), '/usr/bin/cmp', '/usr/bin/ldd', '/usr/bin/env', '/bin/bash', '/bin/sh'}
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for base in LIB_ROOTS:
        if base.is_dir():
            candidates = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
            names.update(str(p) for p in candidates if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    names.update(str(p) for base in DATA_ROOTS if base.is_dir() for p in base.rglob('*') if p.is_file())
    return sorted(names)


def configuration():
    paths = set(LIB_ROOTS + DATA_ROOTS + (STDLIB,))
    # Development headers/Makefile may be absent in the runtime installation.
    # Their exact absence is configuration, not a fabricated required file.
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
    ldd = Path('/usr/bin/ldd').read_text()
    match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    need(ldd.splitlines()[0] == '#!/bin/bash' and match is not None, 'known_ldd_script_and_loader_declaration')
    paths.update(map(Path, match.group(1).split()))
    result = {}
    for p in sorted(paths, key=str):
        row = {'lexists': lexists(p), 'exists': p.exists(), 'is_file': p.is_file(), 'is_dir': p.is_dir(),
               'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}
        if p.is_file():
            row.update(value(p))
        result[str(p)] = row
    need(not result['/etc/ld.so.preload']['lexists'] and not result['/usr/lib/python310.zip']['lexists'], 'no_preload_or_system_python_zip')
    need(all(not row['lexists'] for name, row in result.items() if name.endswith(('._pth', '/pyvenv.cfg'))), 'no_interpreter_path_injection_files')
    return result


def inventory(names):
    return {name: rich(name) for name in sorted(set(names))}


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


def covered_sample(sample, inputs, cache):
    need(sample['environment'] == ENV and sample['executable'] == str(PYTHON) and sample['cwd'] == str(ROOT) and
         sample['sys_path'] == IMPORT_PATH and sample['pycache_prefix'] == str(cache) and not sample['cache_lexists'] and not lexists(cache), 'sample_exact_settings')
    need(all(s in sample['flags'] for s in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')), 'sample_flags')
    need(sha256(sample['proc_maps'].encode()).hexdigest() == sample['proc_maps_sha256'] and len(sample['proc_maps'].encode()) == sample['proc_maps_bytes'], 'entire_volatile_maps_bytes')
    for name, wanted in list(sample['mapped_files'].items()) + [(v['path'], {k: v[k] for k in ('sha256', 'bytes')}) for v in sample['modules'].values()]:
        need(name in inputs and all(inputs[name][k] == wanted[k] for k in ('sha256', 'bytes')), ('sample_input_coverage', name))
        pin(name, wanted)


def child(number):
    need(number in ('01', '02'), 'fixed_pair_child')
    cache = OUT / ('unused_child_' + number + '_cache')
    settings(cache, OUT / 'sources/run_pair.py')
    source = OUT / 'sources/verify.py'
    pin(source, VERIFIER_SHA)
    before = ordinary_sample()
    events = []
    active = True
    def observe(event, args):
        if active and event == 'open' and isinstance(args[0], (str, bytes)):
            events.append({'path': os.fsdecode(args[0]), 'mode': args[1], 'flags': args[2]})
    sys.addaudithook(observe)
    outcome = 'RAISED'
    try:
        code = compile(source.read_bytes(), str(source), 'exec')
        exec(code, {'__name__': '__main__', '__file__': str(source)})
        outcome = 'RETURNED'
    finally:
        active = False
        after = ordinary_sample()
        opened_files, absent, volatile = {}, [], []
        for name in sorted({row['path'] for row in events}):
            path = Path(name)
            path = path if path.is_absolute() else ROOT / path
            if str(path).startswith('/proc/'):
                volatile.append(str(path))
            elif path.is_file():
                selected = path.resolve(strict=True)
                need(selected.suffix not in {'.pyc', '.pyo'}, ('observed_existing_bytecode', name))
                opened_files[str(selected)] = value(selected)
            else:
                absent.append({'path': str(path), 'lexists_after': lexists(path), 'exists_after': path.exists(), 'is_dir_after': path.is_dir()})
        write_json(OUT / ('observations/child_' + number + '.json'), {'status': outcome, 'source': {'path': str(source), **value(source)},
            'before': before, 'after': after, 'python_open_events': events, 'opened_ordinary_files': opened_files,
            'nonfile_open_paths_at_end': absent, 'volatile_open_paths': volatile,
            'scope': 'Hook installed after observer imports; source execution opens plus before/after module/map samples. Not OS/startup/continuous tracing.'})


def command(label, argv):
    timeout = 600 if label.startswith('03_verify_') else 60
    folder = OUT / 'commands' / label
    folder.mkdir()
    entry = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_utc': now(), 'timeout_seconds': timeout,
             'status': 'ATTEMPTED', 'exit_code': None}
    write_json(folder / 'ATTEMPT.json', entry)
    failure, timed_out, spawned, streams_complete = None, False, True, True
    try:
        process = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, timeout=timeout, check=False)
        code, wrapper_code, stdout, stderr = process.returncode, process.returncode, process.stdout, process.stderr
    except subprocess.TimeoutExpired as exc:
        code, wrapper_code, stdout, stderr = None, 124, exc.stdout or b'', exc.stderr or b''
        timed_out, streams_complete, failure = True, False, repr(exc)
    except OSError as exc:
        code, wrapper_code, stdout, stderr = None, 127, b'', b''
        spawned, streams_complete, failure = False, False, repr(exc)
    write_bytes(folder / 'stdout.raw', stdout)
    write_bytes(folder / 'stderr.raw', stderr)
    receipt = {**entry, 'status': 'COMPLETED' if failure is None else 'TIMED_OUT' if timed_out else 'SPAWN_FAILED',
               'ended_utc': now(), 'exit_code': code, 'wrapper_exit_code': wrapper_code, 'spawned': spawned,
               'streams_complete': streams_complete, 'timed_out': timed_out, 'failure': failure,
               'stream_scope': 'Native child streams; timeout captures are partial. Spawn failure has no native child streams/returncode; its diagnostic is failure above.',
               'stdout': value(folder / 'stdout.raw'), 'stderr': value(folder / 'stderr.raw')}
    write_json(folder / 'RECEIPT.json', receipt)
    COMMANDS.append({'label': label, **receipt})
    need(code == 0 and not stderr, ('actual_native_command_failed', label, receipt))
    if argv[0] == '/usr/bin/cmp':
        need(stdout == b'', ('native_cmp_full_empty_stdout', label))
    return stdout


def ldd_closure(label, extensions, inputs):
    output = command(label, ['/usr/bin/ldd', str(PYTHON), '/usr/bin/cmp'] + extensions)
    need(b'not found' not in output, ('ldd_unresolved_dependency', label))
    paths = sorted({str(Path(os.fsdecode(p)).resolve()) for p in re.findall(rb'(/[^\s()]+)', output) if Path(os.fsdecode(p)).is_file()})
    for name in paths:
        need(name in inputs, ('ldd_dependency_outside_before', name))
        pin(name, inputs[name])
    return paths


def seal():
    files = sorted(p for p in OUT.rglob('*') if p.is_file())
    need(not lexists(OUT / 'SHA256SUMS') and all(not p.is_symlink() for p in OUT.rglob('*')), 'exclusive_output_seal')
    write_bytes(OUT / 'SHA256SUMS', ''.join(value(p)['sha256'] + '  ' + p.relative_to(OUT).as_posix() + '\n' for p in files).encode())
    rows = manifest(OUT, count=len(files))
    return {'payloads': len(rows), 'manifest': value(OUT / 'SHA256SUMS')}


def run(args):
    need(not lexists(OUT), ('refuse_existing_attempt', str(OUT)))
    need(OUT.parent.is_dir() and OUT.parent.resolve(strict=True) == OUT.parent, 'exact_existing_output_parent_no_symlink')
    OUT.mkdir()
    write_json(OUT / 'RUN_ENTERED.json', {'status': 'ENTERED_NOT_A_PRESPAWN_RECEIPT', 'started_utc': now(),
        'argv': sys.argv, 'interpreter_argv': sys.orig_argv, 'environment': ENV, 'cwd': str(ROOT), 'source': rich(PREP / 'run_pair.py')})
    errors, inputs, resources, conf, baseline = [], None, None, None, None
    samples, results = {}, []
    try:
        baseline = preflight(args)
        (OUT / 'sources').mkdir()
        (OUT / 'commands').mkdir()
        (OUT / 'observations').mkdir()
        copied = {}
        for name, origin in [('run_pair.py', PREP / 'run_pair.py'), ('verify.py', PACKAGE / 'verify.py')]:
            data = origin.read_bytes()
            write_bytes(OUT / 'sources' / name, data)
            need((OUT / 'sources' / name).read_bytes() == data, ('exact_source_copy', name))
            copied[name] = {'origin': str(origin), 'copy': str(OUT / 'sources' / name), **value(origin)}
        write_json(OUT / 'SOURCE_ONLY_INITIAL.json', copied)
        need({p.name for p in (OUT / 'sources').iterdir()} == {'run_pair.py', 'verify.py'}, 'exact_two_source_files_only')
        resources, conf = resource_names(), configuration()
        known = set(baseline['package_files']) | set(baseline['preparation_files']) | set(resources)
        known.update(read_json(PREP / 'INPUT_PINS.json')['inputs'])
        known.update(row['copy'] for row in copied.values())
        known.update(name for name, row in conf.items() if row['is_file'])
        # Preserve lexical paths and resolved physical dependency names.
        known.update(str(Path(name).resolve(strict=True)) for name in list(known))
        inputs = inventory(known)
        write_json(OUT / 'INPUTS_BEFORE.json', inputs)
        write_json(OUT / 'RESOURCE_NAMES_BEFORE.json', resources)
        write_json(OUT / 'CONFIGURATION_BEFORE.json', conf)
        samples['before'] = ordinary_sample()
        covered_sample(samples['before'], inputs, OUT / 'unused_parent_cache')
        write_json(OUT / 'observations/parent_before.json', samples['before'])
        command('00_cmp_runner_source', ['/usr/bin/cmp', '--', str(PREP / 'run_pair.py'), str(OUT / 'sources/run_pair.py')])
        command('01_cmp_verifier_source', ['/usr/bin/cmp', '--', str(PACKAGE / 'verify.py'), str(OUT / 'sources/verify.py')])
        extensions = sorted(name for name in resources if name.startswith(str(STDLIB) + '/') and name.endswith('.so'))
        links_before = ldd_closure('02_ldd_before', extensions, inputs)
        for number in ('01', '02'):
            cache = OUT / ('unused_child_' + number + '_cache')
            need(not lexists(cache), ('exclusive_child_cache', str(cache)))
            output = command('03_verify_' + number, [str(PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(cache), str(OUT / 'sources/run_pair.py'), 'child', number, ROLE])
            observed = read_json(OUT / ('observations/child_' + number + '.json'))
            need(observed['status'] == 'RETURNED' and observed['source'] == {'path': str(OUT / 'sources/verify.py'), **value(PACKAGE / 'verify.py')}, ('actual_unchanged_scientific_source', number))
            for phase in ('before', 'after'):
                covered_sample(observed[phase], inputs, cache)
            for name, expected in observed['opened_ordinary_files'].items():
                need(name in inputs and all(inputs[name][k] == expected[k] for k in ('sha256', 'bytes')), ('python_open_input_coverage', number, name))
                pin(name, expected)
            need(not observed['volatile_open_paths'], ('unexpected_verifier_volatile_open', number))
            for row in observed['nonfile_open_paths_at_end']:
                need(Path(row['path']).is_relative_to(cache) and not row['lexists_after'] and not row['exists_after'] and
                     not row['is_dir_after'] and not lexists(cache), ('only_explicit_absent_cache_probes_allowed', number, row))
            data = json.loads(output)
            check_original_output(data)
            results.append({'number': number, 'checks': data[SPEC['check_field']], 'stdout': value(OUT / ('commands/03_verify_' + number + '/stdout.raw'))})
        for number in ('01', '02'):
            command('04_cmp_canonical_' + number, ['/usr/bin/cmp', '--', str(OUT / ('commands/03_verify_' + number + '/stdout.raw')), str(PACKAGE / 'CANONICAL.json')])
        command('05_cmp_pair', ['/usr/bin/cmp', '--', str(OUT / 'commands/03_verify_01/stdout.raw'), str(OUT / 'commands/03_verify_02/stdout.raw')])
        links_after = ldd_closure('06_ldd_after', extensions, inputs)
        need(links_before == links_after, 'exact_resolved_ldd_membership_before_after')
        write_json(OUT / 'LINKED_RUNTIME.json', {'before': links_before, 'after': links_after})
    except Exception as exc:
        errors.append({'stage': 'run', 'error': repr(exc)})
    finally:
        if inputs is not None:
            for label, action in [('inputs', lambda: inventory(inputs)), ('resources', resource_names), ('configuration', configuration),
                                  ('parent_runtime', ordinary_sample)]:
                try:
                    after = action()
                    filename = {'inputs': 'INPUTS_AFTER.json', 'resources': 'RESOURCE_NAMES_AFTER.json', 'configuration': 'CONFIGURATION_AFTER.json',
                                'parent_runtime': 'observations/parent_after.json'}[label]
                    write_json(OUT / filename, after)
                    if label == 'parent_runtime':
                        covered_sample(after, inputs, OUT / 'unused_parent_cache')
                    else:
                        expected = {'inputs': inputs, 'resources': resources, 'configuration': conf}[label]
                        need(after == expected, ('entire_before_after_equality', label))
                except Exception as exc:
                    errors.append({'stage': 'after_' + label, 'error': repr(exc)})
        try:
            post = preflight(args)
            need(baseline is not None and post == baseline, 'entire_original_package_and_preparation_unchanged')
            need(all(not lexists(OUT / name) for name in ('unused_parent_cache', 'unused_child_01_cache', 'unused_child_02_cache')), 'all_cache_paths_absent_after')
            if baseline is not None:
                write_json(OUT / 'PACKAGE_AND_PREPARATION_CLOSURE.json', {'before': baseline, 'after': post})
        except Exception as exc:
            errors.append({'stage': 'final_closed_package', 'error': repr(exc)})
    try:
        for row in COMMANDS:
            folder = OUT / 'commands' / row['label']
            need(read_json(folder / 'RECEIPT.json') == {k: v for k, v in row.items() if k != 'label'}, ('complete_native_receipt_unchanged', row['label']))
            attempt = read_json(folder / 'ATTEMPT.json')
            need(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and
                 all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc', 'timeout_seconds')), ('complete_prespawn_record_unchanged', row['label']))
            for stream in ('stdout', 'stderr'):
                pin(folder / (stream + '.raw'), row[stream])
        write_json(OUT / 'COMMAND_CLOSURE.json', {'command_count': len(COMMANDS), 'native_streams_rechecked': 2 * len(COMMANDS),
            'scope': 'Every entire recorded receipt, pre-spawn record and raw stream rechecked after the pair.'})
    except Exception as exc:
        errors.append({'stage': 'native_record_closure', 'error': repr(exc)})
    if not errors:
        expected_labels = ['00_cmp_runner_source', '01_cmp_verifier_source', '02_ldd_before', '03_verify_01', '03_verify_02',
                           '04_cmp_canonical_01', '04_cmp_canonical_02', '05_cmp_pair', '06_ldd_after']
        if [row['label'] for row in COMMANDS] != expected_labels or len(results) != 2:
            errors.append({'stage': 'complete_command_census', 'error': 'Exact nine-command / two-result census missing'})
    summary = {'status': 'FAIL_ROOT_P210_AUTHOR_STRICT_PAIR' if errors else 'PASS_ROOT_P210_AUTHOR_STRICT_PAIR', 'errors': errors,
        'completion_boundary': 'Execution/input checks only here: complete closure additionally requires the successful parent native return and verified full SHA256SUMS seal.',
        'role': ROLE, 'scientific_scope': 'Actual root pair of unchanged initial P210 author code and original full canonical; integration by proof contributor, not manuscript review.',
        'ended_utc': now(), 'known_input_count': len(inputs) if inputs else None, 'results': results,
        'commands': COMMANDS, 'raw_canonical_comparisons': sum(c['label'].startswith('04_cmp_canonical_') for c in COMMANDS),
        'raw_pair_comparisons': sum(c['label'] == '05_cmp_pair' for c in COMMANDS), 'source_only_system_python': str(PYTHON),
        'bounds': 'Exactly the original entire pinned canonical; no cutoff changes',
        'OS_syscall_trace': 'NOT_COLLECTED', 'observation_limit': 'Parent/child module/maps samples and post-hook Python opens; not OS/startup/continuous tracing.',
        'no_new_all_size_proof_or_review': True, 'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}
    write_json(OUT / 'RESULT.json', summary)
    closed = seal()
    print(json.dumps({'status': summary['status'], 'errors': errors, 'source': value(PREP / 'run_pair.py'), 'verifier': value(PACKAGE / 'verify.py'),
        'role': ROLE, 'known_inputs': summary['known_input_count'], 'checks_each': [r['checks'] for r in results],
        'command_count': len(COMMANDS), 'closure': closed,
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))
    return 1 if errors else 0


def main():
    if len(sys.argv) == 4 and sys.argv[1] == 'child':
        select_role(sys.argv[3])
        child(sys.argv[2])
        return 0
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['preflight', 'run'])
    parser.add_argument('--role', choices=sorted(SPECS), required=True)
    parser.add_argument('--expected-preparation-sha256', required=True)
    args = parser.parse_args()
    select_role(args.role)
    need(re.fullmatch(r'[0-9a-f]{64}', args.expected_preparation_sha256), 'exact_preparation_pin_required')
    settings(OUT / 'unused_parent_cache', PREP / 'run_pair.py')
    if args.mode == 'preflight':
        need(not lexists(OUT), ('future_target_must_be_new', str(OUT)))
        data = preflight(args)
        print(json.dumps({'status': 'PASS_READ_ONLY_PREFLIGHT_NOT_EXECUTION_OR_ACCEPTANCE', 'role': ROLE, 'package_payloads': data['package_payloads'],
            'package_manifest': data['package_manifest'], 'preparation_manifest': data['preparation_manifest'],
            'verifier': data['verifier'], 'canonical': data['canonical'], 'target_not_created': str(OUT), 'fresh_scientific_executions': 0}, sort_keys=True, indent=2))
        return 0
    return run(args)


if __name__ == '__main__':
    raise SystemExit(main())
