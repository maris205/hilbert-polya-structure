#!/usr/bin/env python3
"""Fresh root P205/P207 author/A/B original-scope pairs with strict reuse keys.
Only child() executes unchanged science. Six frozen scientific sources and
canonical transcripts stay intact. Source-only no-site/no-old-cache Python,
before/after known runtime keys, complete native streams and actual raw cmp.
Samples and post-hook opens are not exhaustive OS or startup tracing.
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
PREP = ROOT / 'docs/papers204_208_sequence/qa/batch_terminal_strict_preparation'
SPECS = {
    "p205_author": {
        "package": "papers/205-conflict-triggered-cyclic-increments",
        "payloads": 256,
        "manifest_sha": "103d82e34d9926ac3284f7ae90b08903aef73ca6acbb8e889fb36379a6e21c68",
        "verifier_sha": "329b2c8bf19bdfd77cfbb5e3f16d6bfc78aa90f557444cf45d5e35d44868afe9",
        "canonical_sha": "41ca0312bd5115fc0343310ebfbd493c44ee927d267de7ca438328af92bae2f7",
        "canonical_bytes": 4433,
        "check_field": "total_checks",
        "checks": 1029769,
        "status": "PASS_BOUNDED_AUTHOR_PROOF_PRESSURE_NOT_INDEPENDENT_REVIEW"
    },
    "p205_a": {
        "package": "docs/papers204_208_sequence/reviews/p205_a",
        "payloads": 60,
        "manifest_sha": "494de5c1d4b77300b62631dbad8ad3d595a78acba869980a278219c64b9e8a1c",
        "verifier_sha": "3a4cbce7210f93addc9a65bed2aef822b0cae3f859a9c93df66beb57f7bebeaa",
        "canonical_sha": "742ab7299ac4e44f15f42f56393abce02c41271164d1ae33a3b1cc80f093a626",
        "canonical_bytes": 11589,
        "check_field": "assertions",
        "checks": 11265033,
        "status": "PASS"
    },
    "p205_b": {
        "package": "docs/papers204_208_sequence/reviews/p205_b",
        "payloads": 56,
        "manifest_sha": "97a4d5ea7f278cbad5a6fb733abac95dd9856aad9917b7352c6990898e5090ba",
        "verifier_sha": "98c74ab0e43171e673c232a9e6e2cf3f517825f9133eca9974a384fb4e846e97",
        "canonical_sha": "9125dc56e504cafb295cb29b5469a4b941d5a0d63ccedcf3a32076272d5aedb9",
        "canonical_bytes": 14444,
        "check_field": "total_assertions",
        "checks": 12023630,
        "status": "PASS_FINITE_CHECKS_NOT_ALL_PARAMETER_PROOF"
    },
    "p207_author": {
        "package": "papers/207-upper-neighbor-rank-dynamics",
        "payloads": 614,
        "manifest_sha": "1d52015974faf842c50e9fc0a5ca481d4973af0c26b3c19c4b540ca5c6016a95",
        "verifier_sha": "5018b0fe6d6a032e0eadeb7cd53a6de47c789193580fa1707312b592cd4a3c93",
        "canonical_sha": "306d4e7dea07ad10234f06c69912561425792ed61fadeff3b165b09d1a106992",
        "canonical_bytes": 288808,
        "check_field": "assertions",
        "checks": 1384012,
        "status": "PASS"
    },
    "p207_a": {
        "package": "docs/papers204_208_sequence/reviews/p207_a",
        "payloads": 133,
        "manifest_sha": "e76bd37687e00a2a641832f0b1c8bb2c00d8889432b6c9f5da5c338fc8532aa3",
        "verifier_sha": "2b0e0d9c0bde25c7f9e5dc132b15d58f8ab20f6760c6898ba6abf12e330b5ee2",
        "canonical_sha": "d4c1f4264d628f38c83d85e0532d036056fad89695ab399e25c9d19e6d09243e",
        "canonical_bytes": 37971,
        "check_field": "assertions",
        "checks": 1326321,
        "status": "PASS"
    },
    "p207_b": {
        "package": "docs/papers204_208_sequence/reviews/p207_b",
        "payloads": 138,
        "manifest_sha": "8274a5062034ce86e60bd6f81d8814019ef83e412efc4c48154392f74e4a484d",
        "verifier_sha": "8c364da4c9bdaa206910f95357cf813f544454fbceb021f89b8e79d09906c44a",
        "canonical_sha": "b7206f01180dcbe5eca24dbaec67cc96ae5dc80f86004455d382e7723c786fda",
        "canonical_bytes": 1558382,
        "check_field": "assertions",
        "checks": 2158999,
        "status": "PASS"
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
    need(role in SPECS, ('exact_six_role_scope', role))
    ROLE, SPEC = role, SPECS[role]
    PACKAGE = ROOT / SPEC['package']
    OUT = ROOT / ('docs/papers204_208_sequence/qa/root_replays/batch_terminal_strict_' + role + '_01')
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
    need(data[SPEC['check_field']] == SPEC['checks'] and data['status'] == SPEC['status'], 'original_count_and_status')
    return {'role': ROLE, 'package_payloads': len(rows), 'package_manifest': value(PACKAGE / 'SHA256SUMS'),
            'preparation_manifest': value(PREP / 'SHA256SUMS'), 'verifier': value(PACKAGE / 'verify.py'),
            'canonical': value(PACKAGE / 'CANONICAL.json'),
            'package_files': sorted(str(PACKAGE / n) for n in rows) + [str(PACKAGE / 'SHA256SUMS')],
            'preparation_files': sorted(str(PREP / n) for n in prep_rows) + [str(PREP / 'SHA256SUMS')]}


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
            need(data[SPEC['check_field']] == SPEC['checks'] and data['status'] == SPEC['status'], ('fixed_original_box_result', number))
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
    summary = {'status': 'FAIL_ROOT_BATCH_TERMINAL_STRICT_PAIR' if errors else 'PASS_ROOT_BATCH_TERMINAL_STRICT_PAIR', 'errors': errors,
        'completion_boundary': 'Execution/input checks only here: complete closure additionally requires the successful parent native return and verified full SHA256SUMS seal.',
        'role': ROLE, 'scientific_scope': 'Actual root fresh execution of unchanged accepted author/reviewer code and its exact original canonical. No fresh review or theorem.',
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
