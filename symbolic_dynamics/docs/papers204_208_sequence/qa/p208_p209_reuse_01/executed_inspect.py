#!/usr/bin/env python3
"""Read-only current-key reuse inspection, not new science/build/view or acceptance.

Explicit schema adaptation of the pinned P208/P209 original recorders and
accepted artifact predicates. No original program is imported or executed.
Only six declared documentary roles may select historical physical bytes.
"""
import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import sysconfig
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
PREP = BATCH / 'qa/p208_p209_reuse_preparation'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
OLD_ENV = {**ENV, 'LANG': 'C', 'LC_ALL': 'C'}
BUILD_ENV = {**ENV, 'SOURCE_DATE_EPOCH': '1788652800', 'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'}
PY = {208: Path('/root/miniconda3/bin/python3.12'), 209: Path('/usr/bin/python3.10')}
STD = {208: Path('/root/miniconda3/lib/python3.12'), 209: Path('/usr/lib/python3.10')}
TEX209 = tuple(map(Path, ('/usr/share/texlive/texmf-dist', '/usr/share/texmf', '/var/lib/texmf',
    '/etc/texmf', '/usr/local/share/texmf', '/root/texmf', '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')))
TEX208 = tuple(Path('/usr/share/texlive/texmf-dist') / n for n in ('tex', 'fonts', 'web2c', 'bibtex')) + TEX209[1:]
CONF208 = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/share/fonts', '/etc/fonts', '/var/cache/fontconfig',
    '/usr/share/fontconfig', '/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/share/poppler')))
CONF209 = CONF208 + tuple(map(Path, ('/usr/lib/gconv', '/usr/local/share/fonts', '/etc/xdg/fontconfig',
    '/etc/profile.d', '/root/.fonts', '/root/.fontconfig', '/root/.fonts.conf.d', '/root/.config/fontconfig',
    '/root/.cache/fontconfig', '/root/.local/share/fonts')))
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
TEX_TOOLS = tuple(Path('/usr/bin') / n for n in ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo',
    'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp'))
LOADERS = tuple(map(Path, ('/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2')))
CACHE, JSON_CACHE, TREES, MEMBERSHIPS, ABSENCES, ALIASES, USED = {}, {}, {}, [], set(), {}, {}
CONFIGURATIONS, DIRECTORY_STATES = [], []
CASE, CHECKS, RAW_COMPARISONS, LEDGERS = 'setup', 0, 0, []


def need(value, rule, detail=None):
    global CHECKS
    CHECKS += 1
    if not value:
        raise RuntimeError(json.dumps({'case': CASE, 'rule': rule, 'detail': detail}, sort_keys=True))


def measured(path):
    path = Path(path)
    need(path.is_absolute() and path.is_file(), 'Missing absolute regular input', str(path))
    if path.is_relative_to(ROOT):
        need(path.resolve() == path and not path.is_symlink(), 'Workspace alias forbidden', str(path))
    h, size = hashlib.sha256(), 0
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk); size += len(chunk)
    return {'sha256': h.hexdigest(), 'bytes': size, 'resolved': str(path.resolve()),
            'symlink': os.readlink(path) if path.is_symlink() else None}


def pin(path, expected=None, documentary=False):
    path = Path(path)
    expected = {'sha256': expected} if isinstance(expected, str) else expected
    key = (str(path), expected['sha256']) if expected else None
    selected = Path(ALIASES[key]['physical']) if documentary and key in ALIASES and CASE in ALIASES[key]['cases'] else path
    if selected != path:
        USED[str(path) + ' @ ' + expected['sha256']] = {'physical': str(selected), 'case': CASE}
    name = str(selected)
    if name not in CACHE:
        CACHE[name] = measured(selected)
    actual = CACHE[name]
    if expected:
        for field in ('sha256', 'bytes', 'resolved', 'symlink'):
            if field in expected and not (selected != path and field in ('resolved', 'symlink')):
                need(actual[field] == expected[field], 'Changed key: affected fresh check required',
                     {'original': str(path), 'physical': name, 'field': field, 'expected': expected[field], 'actual': actual[field]})
    return actual


def raw(path):
    path = Path(path); before = pin(path); data = path.read_bytes()
    need(hashlib.sha256(data).hexdigest() == before['sha256'] and len(data) == before['bytes'], 'Read changed', str(path))
    return data


def obj(path):
    def unique(pairs):
        value = {}
        for key, item in pairs:
            need(key not in value, 'Duplicate JSON key', str(path)); value[key] = item
        return value
    name = str(path)
    if name not in JSON_CACHE:
        JSON_CACHE[name] = json.loads(raw(path), object_pairs_hook=unique)
    return JSON_CACHE[name]


def equal(left, right):
    global RAW_COMPARISONS
    pin(left); pin(right)
    with Path(left).open('rb') as a, Path(right).open('rb') as b:
        while True:
            x, y = a.read(1024 * 1024), b.read(1024 * 1024)
            need(x == y, 'Current complete raw bytes differ', [str(left), str(right)])
            if not x: break
    RAW_COMPARISONS += 1


def physical(base):
    entries = list(base.rglob('*'))
    need(base.resolve() == base and not any(p.is_symlink() for p in entries), 'Nonphysical package', str(base))
    value = {p.relative_to(base).as_posix() for p in entries if p.is_file()}
    if str(base) in TREES: need(TREES[str(base)] == value, 'Package membership changed', str(base))
    TREES[str(base)] = value
    return value


def package(spec):
    base = Path(spec['root']); seal = base / 'SHA256SUMS'; pin(seal, spec['manifest']); rows = {}
    for line in raw(seal).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'Manifest syntax', str(seal)); digest, name = match.groups(); p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and p.as_posix() == name and
             name != 'SHA256SUMS' and name not in rows, 'Unsafe, self or duplicate manifest entry', name)
        rows[name] = digest; pin(base / name, digest)
    need(len(rows) == spec['payloads'] and set(rows) == physical(base) - {'SHA256SUMS'}, 'Incomplete exact nonself seal', str(base))
    return rows


def interval(base, before, after=None, documentary=False):
    after = after or before.replace('_BEFORE', '_AFTER')
    left, right = obj(base / before), obj(base / after)
    need(type(left) is dict and left == right and left, 'Recorded full before/after interval', [str(base), before])
    for name, value in left.items():
        # Older pin maps stored resolved absolute keys without repeating that
        # field inside each value. Do not permit a new redirect at those keys.
        pin(Path(name), {'resolved': name, **value}, documentary)
    LEDGERS.append({'before': str(base / before), 'after': str(base / after), 'entries': len(left)})
    return left


def absence(path):
    path = Path(path); need(path.is_absolute() and not os.path.lexists(path), 'Previously absent cache/path now exists', str(path))
    ABSENCES.add(str(path))


def configuration(value, remember=True):
    state = {}
    for name, row in value.items():
        p = Path(name)
        need(p.exists() == row['exists'] and str(p.resolve()) == row['resolved'], 'Configuration presence/resolution changed', name)
        if 'is_file' in row: need(p.is_file() == row['is_file'], 'Configuration file-kind changed', name)
        else: need(p.is_file() == ('sha256' in row), 'Older configuration file-kind changed', name)
        if 'sha256' in row: pin(p, row)
        elif not row['exists']: absence(p)
        state[name] = (p.exists(), p.is_file(), p.is_dir(), str(p.resolve()), os.readlink(p) if p.is_symlink() else None)
    if remember: CONFIGURATIONS.append((CASE, value, state))
    return state


def member_check(label, function, expected):
    actual = function()
    need(actual == expected, 'Current exact membership changed: affected fresh check required',
         {'group': label, 'missing': sorted(expected - actual)[:20], 'added': sorted(actual - expected)[:20]})
    MEMBERSHIPS.append((CASE, label, function, expected))


def files_under(roots, resolved=False):
    return {str(p.resolve() if resolved else p) for base in roots if base.is_dir() for p in base.rglob('*') if p.is_file()}


def runtime_names(number, build=False):
    std, python = STD[number], PY[number]
    if number == 208:
        paths = {p for p in std.rglob('*') if p.is_file() and 'site-packages' not in p.parts and '__pycache__' not in p.parts}
        paths |= set(TEX_TOOLS if build else (Path('/usr/bin/cmp'), Path('/usr/bin/ldd')))
        paths |= {python, Path('/bin/bash')}
        return {str(p.resolve()) for p in paths}
    names = set()
    for directory, folders, files in os.walk(std):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for base in LIB_ROOTS:
        paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        names.update(str(p) for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    names.update(('/usr/bin/env', '/usr/bin/cmp', '/usr/bin/ldd', '/bin/bash', '/bin/sh', str(python)))
    if build: names.update(map(str, TEX_TOOLS))
    return {str(Path(p).resolve()) for p in names} if build else names


def config_names(number, build, role=''):
    python, std = PY[number], STD[number]
    paths = {Path('/etc/ld.so.cache'), Path('/etc/ld.so.conf'), Path('/etc/ld.so.preload'), *LOADERS,
             std.parent / ('python312.zip' if number == 208 else 'python310.zip')}
    if number == 208 and not build:
        paths.update(Path('/etc/ld.so.conf.d').glob('*'))
        if role == 'b':
            paths.update(python.parent / n for n in ('pyvenv.cfg', 'python._pth', 'python3._pth'))
            paths.add(python.parent.parent / 'pyvenv.cfg')
        return set(map(str, paths))
    paths.update((python.parent / 'pyvenv.cfg', python.parent.parent / 'pyvenv.cfg',
                  python.with_name(python.name + '._pth'), python.with_name('python._pth'),
                  Path('/etc/locale.conf'), Path('/etc/default/locale')))
    if number == 208:
        paths.update(CONF208 + TEX208 + TEX_TOOLS + (Path('/bin/bash'), python))
        paths.update(map(Path, files_under(CONF208)))
        return set(map(str, paths))
    paths.update(map(Path, ('/etc/nsswitch.conf', '/etc/localtime', '/etc/bash.bashrc', '/etc/profile', '/usr/lib/locale/locale-archive')))
    paths.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
    for base in {python.parent, Path(sys.executable).parent, std.parent}:
        paths.update(base / n for n in ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
    for key in ('LDLIBRARY', 'INSTSONAME'):
        if sysconfig.get_config_var(key): paths.add(std.parent / (sysconfig.get_config_var(key) + '._pth'))
    ldd = raw(Path('/usr/bin/ldd')).decode(); match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    need(ldd.startswith('#!/bin/bash\n') and match, 'Recorded ldd loader rule changed'); paths.update(map(Path, match.group(1).split()))
    if build:
        paths.update(CONF209 + TEX209 + TEX_TOOLS + (Path('/bin/bash'), Path('/bin/sh'), Path('/usr/bin/env'), python))
        paths.update(map(Path, ('/etc/passwd', '/etc/group', '/root/.fonts.conf', '/root/.config/fontconfig/fonts.conf', '/etc/fonts/local.conf')))
        paths.update(map(Path, files_under(CONF209)))
    return set(map(str, paths))


def flat_command(base, row, environment, build=False):
    label = row['label']; need(row == obj(base / (label + '.command.json')), 'Embedded native command differs', label)
    need(row['exit_code'] == 0 and row['environment'] == environment and row['argv'] and
         datetime.fromisoformat(row['started_utc']) <= datetime.fromisoformat(row['ended_utc']), 'Native command result/settings', label)
    for name in ('stdout', 'stderr'):
        item = row[name]; need(Path(item['path']).name == item['path'], 'Unsafe stream path', label); pin(base / item['path'], item)
    need(pin(base / row['stderr']['path'])['bytes'] == 0, 'Native stderr is not empty', label)
    if build:
        attempt = obj(base / (label + '.attempt.json'))
        pre_exit = 'exit_code' not in attempt if build == 208 else ('exit_code' in attempt and attempt['exit_code'] is None)
        need(row['status'] == 'COMPLETED' and attempt['status'] == 'ATTEMPTED' and pre_exit and
             all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc')), 'Native pre-spawn agreement', label)
    return row['argv']


def map_paths(text):
    return sorted({str(Path(parts[5]).resolve()) for line in text.splitlines()
                   if len(parts := line.split(None, 5)) == 6 and parts[5].startswith('/')})


def observed_modern(value, known, generated=()):
    need(value['mapped_files'] == map_paths(value['maps']), 'Stored raw map/sample mismatch')
    paths = set(value['mapped_files']) | set(value.get('opened_existing_files', []))
    for item in value['modules'].values():
        paths.update(p for p in (item.get('file'), item.get('origin')) if p and p.startswith('/'))
    need(not any(p.endswith(('.pyc', '.pyo')) for p in paths), 'Bytecode in source-only observation')
    need(paths <= set(known) | set(generated), 'Uncovered original sampled/opened file', sorted(paths - set(known) - set(generated))[:20])
    return paths


def flags(value, environment, python, cache, cwd=None):
    field = 'environment' if 'environment' in value else 'env'
    need(value[field] == environment and all(s in value['flags'] for s in
         ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')), 'Recorded isolation/environment changed')
    need(value.get('executable', str(python)) == str(python), 'Recorded interpreter role')
    need(value.get('pycache_prefix', value.get('cache_prefix')) == str(cache), 'Recorded cache role')
    need(not value.get('cache_exists', False) and value.get('cache_absent', True), 'Recorded cache was present')
    if cwd is not None: need(value['cwd'] == str(cwd), 'Recorded cwd role')
    if 'sys_path' in value:
        number = 208 if python == PY[208] else 209
        wanted = [str(STD[number].parent / ('python312.zip' if number == 208 else 'python310.zip')), str(STD[number]), str(STD[number] / 'lib-dynload')]
        need(value['sys_path'] == wanted, 'Recorded isolated search path')
    absence(cache)


def flat_ldd(base, libraries):
    for when in ('before', 'after'):
        text = raw(base / ('ldd_' + when + '.stdout')).decode()
        paths = {str(Path(p).resolve()) for p in re.findall(r'/[^\s():]+', text) if Path(p).is_file()}
        need('not found' not in text and paths == set(libraries), 'Complete archived ldd closure', when)


def old_pair(spec):
    base, producer, role = Path(spec['package']['root']), Path(spec['producer']), spec['role']
    package(spec['package']); equal(base / 'executed_harness_snapshot.py', spec['recorder_source'])
    rec = obj(base / 'RECEIPT.json')
    need(rec['status'] == spec['status'] and rec['mode'] == role and not rec['failures'] and len(rec['runs']) == 2 and
         rec['kind'] == 'ROOT_REPRODUCTION_NOT_AN_INDEPENDENT_REVIEW', 'Original strict pair was not successful')
    inputs = interval(base, 'INPUTS_BEFORE.json', documentary=True)
    runtime = interval(base, 'RUNTIME_INVENTORY_BEFORE.json'); libraries = interval(base, 'LIBRARIES_BEFORE.json')
    conf = obj(base / 'CONFIGURATION_BEFORE.json'); need(conf == obj(base / 'CONFIGURATION_AFTER.json'), 'Configuration interval'); configuration(conf)
    need((len(inputs), len(runtime), len(libraries), len(conf)) ==
         (spec['input_count'], 918, 112, 33 if role == 'b' else 29), 'Recorded strict input census')
    member_check('P208 strict runtime', lambda: runtime_names(208), set(runtime))
    member_check('P208 strict configuration', lambda: config_names(208, False, role), set(conf))
    covered = {str(Path(p).resolve()): v['sha256'] for group in (inputs, runtime, libraries) for p, v in group.items()}
    covered.update({v['resolved']: v['sha256'] for v in conf.values() if 'sha256' in v})
    labels = ['ldd_before', 'run1', 'run1_canonical_cmp', 'run2', 'run2_canonical_cmp', 'pair_cmp', 'ldd_after']
    need([r['label'] for r in rec['commands']] == labels, 'All seven native commands/order')
    commands = {r['label']: r for r in rec['commands']}
    for row in rec['commands']:
        argv = flat_command(base, row, OLD_ENV)
        if row['label'].endswith('_cmp'):
            targets = [base / 'run1.stdout', base / 'run2.stdout'] if row['label'] == 'pair_cmp' else [base / (row['label'].split('_')[0] + '.stdout'), producer / 'CANONICAL.json']
            need(argv == ['/usr/bin/cmp', *map(str, targets)] and pin(base / row['stdout']['path'])['bytes'] == 0, 'Archived exact raw comparator')
            equal(argv[1], argv[2])
    for index, run in enumerate(rec['runs'], 1):
        name = 'run' + str(index); folder = base / name; initial = obj(base / (name + '_SOURCE_ONLY_INITIAL.json'))
        need(run['label'] == name and initial == run['initial_files'] == run['final_files'] and set(initial) == {'verify.py'} and
             physical(folder) == {'verify.py'}, 'Exact source-only child capsule')
        pin(folder / 'verify.py', initial['verify.py']); equal(folder / 'verify.py', producer / 'verify.py')
        equal(base / (name + '.stdout'), producer / 'CANONICAL.json')
        payload = obj(base / (name + '.stdout')); field = 'checks' if role == 'b' else 'assertions'
        need(payload[field] == run[field] == spec['checks_each'], 'Original scientific count')
        argv = commands[name]['argv']; cache = base / (name + '_unused_pycache')
        need(argv == [str(PY[208]), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(cache), '-c',
             raw(base / 'executed_wrapper_snapshot.py').decode(), str(base / (name + '_CONSUMED_RUNTIME.json'))] and
             commands[name]['cwd'] == str(folder), 'Exact native source wrapper/cwd')
        obs = obj(base / (name + '_CONSUMED_RUNTIME.json')); flags(obs, OLD_ENV, PY[208], cache)
        used = dict(obs['mapped_files']); used.update({v['path']: v['sha256'] for v in obs['modules'].values() if 'path' in v})
        for p, digest in used.items():
            need(covered.get(p) == digest and not p.endswith(('.pyc', '.pyo')), 'Original consumed runtime coverage', p); pin(p, digest)
    flat_ldd(base, libraries)
    return {'runs_reused': 2, 'native_commands': 7, 'checks_each': spec['checks_each'], 'input_entries': len(inputs), 'runtime_entries': len(runtime)}


def modern_commands(base, known):
    entries = obj(base / 'ALL_COMMAND_RECORDS.json'); need(len(entries) == 85, 'All 85 native commands')
    seen, union = set(), set()
    for entry in entries:
        folder, tag, row = Path(entry['folder']), entry['tag'], entry['command']
        need(folder.is_relative_to(base) and folder.resolve() == folder, 'Command identity')
        identity = (str(folder), tag); need(identity not in seen, 'Duplicate native command'); seen.add(identity)
        need(obj(folder / (tag + '.command.json')) == row, 'Native embedded row')
        attempt = obj(folder / (tag + '.attempt.json'))
        need(row['exit'] == 0 and row['process_outcome'] == 'COMPLETED' and row['spawn_error'] is None and
             row['cleanup'] == [] and row['start_new_session'] and row['env'] == ENV and
             row['started_epoch'] <= row['finished_epoch'], 'Native successful completion/settings', tag)
        need(attempt['record_kind'] == 'PRE_SPAWN_ATTEMPT' and attempt['exit'] is None and attempt['process_outcome'] == 'NOT_STARTED' and
             all(attempt[k] == row[k] for k in ('argv', 'cwd', 'env', 'stdout', 'stderr', 'started_epoch')), 'Native attempt/receipt chronology', tag)
        for stream in ('stdout', 'stderr'):
            need(Path(row[stream]).name == row[stream], 'Exact local native stream role', tag)
            pin(folder / row[stream], row[stream + '_info'])
        need(pin(folder / row['stderr'])['bytes'] == 0, 'Native strict stderr', tag)
        samples = obj(folder / (tag + '.maps.json')); observed = set()
        for sample in samples['samples']:
            need(map_paths(sample['maps']) == sample['mapped_files'], 'Raw native map sample', tag); observed.update(sample['mapped_files'])
        need(sorted(observed) == entry['mapped_files'] and observed <= set(known), 'Native sample union/coverage', tag); union.update(observed)
    return entries, union


def modern_outer(spec, inner, build=False):
    launch = Path(spec['launcher']['root']); package(spec['launcher']); rec = obj(launch / 'RECEIPT.json')
    before = interval(launch, 'INPUTS_BEFORE.json', documentary=True); attempt = obj(launch / 'PRE_SPAWN_ATTEMPT.json')
    environment = BUILD_ENV if build else ENV
    need(rec['exit'] == 0 and rec['outcome'] == 'COMPLETED' and rec['failure'] is None and rec['inputs_unchanged'] and
         rec['cache_absent'] and rec['env'] == environment and rec['cwd'] == str(ROOT) and
         rec['started_epoch'] <= rec['finished_epoch'], 'Actual outer native success')
    need(attempt['exit'] is None and attempt['outcome'] == 'NOT_STARTED' and
         all(attempt[k] == rec[k] for k in ('argv', 'cwd', 'env', 'started_epoch')), 'Outer exact pre-spawn agreement')
    base = Path(spec['package']['root']); argv = [str(PY[209]), '-I', '-S', '-B', '-X',
        'pycache_prefix=' + str(base / 'never_created_parent_cache'), spec['recorder_source']]
    argv += ['terminal-pair-after-round2'] if build else ['pair', base.name]
    need(rec['argv'] == argv, 'Exact actual outer source launch')
    need(rec['recorder_closure']['status'] == inner['status'] and rec['recorder_closure']['payloads'] == spec['package']['payloads'], 'Outer/inner result agreement')
    pin(base / 'SHA256SUMS', rec['recorder_seal'])
    for name in ('recorder.stdout', 'recorder.stderr'): pin(launch / name, rec[name + '_pin'])
    need(pin(launch / 'recorder.stderr')['bytes'] == 0, 'Outer native stderr')
    parsed = obj(launch / 'recorder.stdout'); need(parsed['status'] == inner['status'], 'Full outer stdout result')
    absence(launch / 'never_created_launcher_cache'); absence(base / 'never_created_parent_cache')
    need(rec['launcher_cache'] == str(launch / 'never_created_launcher_cache') and
         all(flag in rec['launcher_flags'] for flag in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')),
         'Original launcher flags and cache')
    for source in (spec['recorder_source'], spec['launcher_source']): equal(launch / Path(source).name, source)
    if build:
        need(rec['status'] == 'PASS_ROOT_TERMINAL_LAUNCH_NOT_VIEWED' and rec['launcher_observed_input_closure'], 'Terminal launcher observation closure')
        covered = {v['resolved']: v for v in before.values()}
        for phase in ('BEFORE', 'AFTER'):
            obs = obj(launch / ('LAUNCHER_RUNTIME_' + phase + '.json'))
            flags(obs, BUILD_ENV, PY[209], launch / 'never_created_launcher_cache', ROOT)
            for p, v in obs['mapped_files'].items(): need(covered[p] == v, 'Outer mapped key')
            for v in obs['modules'].values(): need(covered[v['path']] == {k: v[k] for k in ('bytes', 'sha256', 'resolved')}, 'Outer module key')
    else:
        need(rec['status'] == 'PASS_ROOT_LAUNCH', 'Pair launcher status')
        for name in ('bootstrap.py', 'verify.py'): equal(launch / name, Path(spec['producer']) / name)


def new_pair(spec):
    base, producer = Path(spec['package']['root']), Path(spec['producer']); package(spec['package'])
    equal(base / 'executed_recorder.py', spec['recorder_source']); rec = obj(base / 'RECEIPT.json')
    need(rec['status'] == spec['status'] and rec['mode'] == 'pair' and rec['failures'] == [] and rec['result']['canonical_adopted'] is False, 'Original P209 pair success')
    inputs = interval(base, 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json', 'ALL_INPUTS_AFTER.json', True)
    runtime = interval(base, 'RUNTIME_BEFORE.json'); need(len(inputs) == spec['input_count'] and len(runtime) == 3133, 'Exact P209 input census')
    need(all(inputs[p] == value for p, value in runtime.items()), 'Whole runtime prepinned')
    conf = obj(base / 'CONFIGURATION_BEFORE.json'); need(conf == obj(base / 'CONFIGURATION_AFTER.json'), 'Modern configuration interval'); configuration(conf['optional'])
    member_check('P209 optional configuration', lambda: config_names(209, False), set(conf['optional']))
    needed_names = runtime_names(209)
    needed_names |= {p for p, v in conf['optional'].items() if 'sha256' in v}
    for directory, names in conf['directories'].items():
        p = Path(directory); need((sorted(files_under((p,))) if p.is_dir() else None) == names, 'Modern configuration-directory role', directory)
        DIRECTORY_STATES.append((CASE, p, names is not None, p.exists(), str(p.resolve()), p.is_symlink()))
        member_check('configuration directory: ' + directory, lambda p=p: files_under((p,)), set(names or [])); needed_names.update(names or [])
    discovery = obj(base / 'INTERPRETER_CONFIGURATION.json')
    need(discovery['sysconfig_paths'] == sysconfig.get_paths() and discovery['sysconfig_vars'] == json.loads(json.dumps(sysconfig.get_config_vars())), 'Exact original system-interpreter configuration')
    # Extra pre-key names come only from the original early parent sample.
    early = obj(base / 'PARENT_BEFORE.json')
    early_names = set(early['mapped_files'])
    for v in early['modules'].values(): early_names.update(p for p in (v.get('file'), v.get('origin')) if p and p.startswith('/') and p != spec['recorder_source'])
    needed_names.update(early_names)
    member_check('P209 whole runtime membership', lambda: runtime_names(209) |
        {p for p, v in conf['optional'].items() if 'sha256' in v} |
        set().union(*(files_under((Path(d),)) for d in conf['directories'])) | early_names, set(runtime))
    known = {v['resolved']: v for v in inputs.values()}; entries, native_used = modern_commands(base, known)
    science = obj(base / 'SCIENCE_BEFORE.json')
    need(science and all(inputs[p] == v for p, v in science.items()), 'Original whole science map is included in full key')
    links = obj(base / 'LINKAGE.json'); need(not links['pending_targets'] and len(links['entries']) == 80, 'Complete 80-command linkage')
    for link in links['entries']:
        need(link['status'] == 'VALIDATED' and link['command'] == obj(base / 'linkage' / (link['tag'] + '.command.json')), 'Linkage native result')
        text = raw(base / 'linkage' / (link['tag'] + '.stdout')).decode()
        dependencies = sorted({str(Path(p).resolve()) for p in re.findall(r'/[^\s()]+', text) if Path(p).is_file()})
        need('not found' not in text and dependencies == link['dependencies'] and set(dependencies + [link['target']]) <= set(known), 'Complete native link dependencies')
    closure = obj(base / 'OBSERVED_CLOSURE.json')
    need(closure['uncovered'] == closure['bytecode'] == [], 'Original parent observed closure')
    generated = set(closure['generated_receipt_or_build_reads'])
    need(all(Path(p).is_relative_to(base) and not p.endswith(('.py', '.pyc', '.pyo')) for p in generated), 'Only sealed generated documentary reads')
    sealed = {str(base / n) for n in TREES[str(base)]}
    need(generated | set(closure['exact_validated_generated_manifests']) <= sealed, 'Every generated read belongs to exact sealed original package')
    for p in generated: pin(p)
    for phase in ('BEFORE', 'AFTER'):
        obs = obj(base / ('PARENT_' + phase + '.json')); flags(obs, ENV, PY[209], base / 'never_created_parent_cache', ROOT)
        observed_modern(obs, known, generated)
    for index in (1, 2):
        child = base / ('replay_0' + str(index)); receipt = obj(child / 'RECEIPT.json')
        need(receipt['status'] == 'PASS' and receipt['failure'] is None and receipt['inputs_unchanged'] and
             receipt['checks'] == spec['checks_each'] and receipt['total_states'] == 3414 and
             receipt['source_only_initial_names'] == ['bootstrap.py', 'verify.py'], 'Successful scientific child/census')
        need(physical(child / 'source_inputs') == {'bootstrap.py', 'verify.py'}, 'Child source-only physical set')
        child_inputs = interval(child, 'INPUTS_BEFORE.json', documentary=True)
        for name in ('bootstrap.py', 'verify.py'): equal(child / 'source_inputs' / name, producer / name)
        equal(child / 'producer.stdout', producer / 'CANONICAL.json')
        payload = obj(child / 'producer.stdout'); need(payload['checks'] == spec['checks_each'], 'Canonical exact check count')
        state_field = 'states' if spec['role'] == 'b' else 'state_count'
        need([b['n'] for b in payload['boxes']] == list(range(6)) and [b[state_field] for b in payload['boxes']] == [1, 1, 4, 27, 256, 3125], 'Unchanged original scientific box')
        row = obj(child / 'producer.command.json'); need(receipt['command'] == row and row['argv'] == [str(PY[209]), '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(child / 'never_created_child_cache'), str(child / 'source_inputs/bootstrap.py')], 'Exact native child source command')
        child_known = {v['resolved']: v for v in child_inputs.values()}
        need(receipt['closure']['uncovered'] == receipt['closure']['bytecode'] == [], 'Original child closure')
        for phase in ('before', 'after'):
            obs = obj(child / ('child.' + phase + '.json')); flags(obs, ENV, PY[209], child / 'never_created_child_cache', child)
            need(obs['orig_argv'] == row['argv'], 'Child actual original argv'); observed_modern(obs, child_known)
    comparison = base / 'comparison'; interval(comparison, 'INPUTS_BEFORE.json')
    for index, tag in enumerate(('pair', 'canonical_01', 'canonical_02')):
        targets = [base / 'replay_01/producer.stdout', base / 'replay_02/producer.stdout'] if tag == 'pair' else [base / ('replay_' + tag[-2:] + '/producer.stdout'), producer / 'CANONICAL.json']
        row = obj(comparison / (tag + '.command.json')); need(row == rec['result']['comparisons'][index] and row['argv'] == ['/usr/bin/cmp', '--', *map(str, targets)], 'Three archived exact full raw comparisons')
        equal(row['argv'][2], row['argv'][3]); need(pin(comparison / row['stdout'])['bytes'] == 0, 'Native comparator stdout')
    modern_outer(spec, rec)
    return {'runs_reused': 2, 'native_commands': 85, 'checks_each': spec['checks_each'], 'input_entries': len(inputs), 'runtime_entries': len(runtime)}


def build_pair(spec):
    number, base, paper = spec['paper_number'], Path(spec['package']['root']), Path(spec['paper'])
    package(spec['package']); equal(base / 'executed_recorder_snapshot.py', spec['recorder_source']); rec = obj(base / 'BUILD_EXECUTION.json')
    need(rec['status'] == spec['status'] and rec['failures'] == [] and len(rec['builds']) == 2 and
         rec['visual_review'] == 'PENDING_NOT_INFERRED_FROM_HASH_OR_RENDER', 'Original terminal pair, not fabricated viewing')
    for place in (paper, paper / 'frozen_round2'):
        member_check('exact manuscript section names: ' + str(place),
            lambda place=place: {p.relative_to(place).as_posix() for p in (place / 'sections').glob('*.tex')},
            {n for n in spec['source_pins'] if n.startswith('sections/')})
    inventories = {stem: interval(base, stem + '_BEFORE.json', documentary=(stem == 'INPUTS'))
                   for stem in ('INPUTS', 'RUNTIME', 'LIBRARIES', 'TEX_INVENTORY', 'CONSUMED_TEX', 'RECORDER_INPUTS')}
    conf = obj(base / 'CONFIGURATION_BEFORE.json'); need(conf == obj(base / 'CONFIGURATION_AFTER.json'), 'Build configuration interval'); configuration(conf)
    member_check('complete terminal runtime', lambda: runtime_names(number, True), set(inventories['RUNTIME']))
    member_check('complete terminal TeX roots', lambda: files_under(TEX208 if number == 208 else TEX209, True), set(inventories['TEX_INVENTORY']))
    member_check('complete terminal configuration', lambda: config_names(number, True), set(conf))
    countmap = dict(zip(('input_count', 'runtime_count', 'resolved_link_file_count', 'tex_inventory_count', 'consumed_tex_count'),
                       (len(inventories[s]) for s in ('INPUTS', 'RUNTIME', 'LIBRARIES', 'TEX_INVENTORY', 'CONSUMED_TEX'))))
    countmap['configuration_count'] = len(conf); need(countmap == spec['counts'] and all(rec[k] == v for k, v in countmap.items()), 'Complete recorded terminal key counts')
    covered = {p: v for group in inventories.values() for p, v in group.items()}
    covered.update({v['resolved']: {k: v[k] for k in ('sha256', 'bytes')} for v in conf.values() if v['is_file']})
    for phase in ('BEFORE', 'AFTER'):
        obs = obj(base / ('RECORDER_RUNTIME_' + phase + '.json'))
        cache = Path('/tmp/p208-terminal-v2-actual-unused-20260906') if number == 208 else base / 'never_created_parent_cache'
        flags(obs, BUILD_ENV, PY[number], cache, ROOT)
        need(obs['original_argv'] == rec['parent_launch'] and rec['parent_cwd'] == str(ROOT) and rec['parent_environment'] == BUILD_ENV, 'Actual terminal parent launch binding')
        for p, v in obs['mapped_files'].items(): need(covered.get(p) == v, 'Terminal parent mapped coverage', p); pin(p, v)
        for v in obs['modules'].values():
            wanted = {k: v[k] for k in ('sha256', 'bytes')}; need(covered.get(v['path']) == wanted and not v['path'].endswith(('.pyc', '.pyo')), 'Terminal parent module coverage', v['path']); pin(v['path'], wanted)
    labels = ['ldd_before', 'pdflatex_version', 'bibtex_version', 'texmf_roots']
    for index in (1, 2): labels.extend('cold_build_' + str(index) + '_' + n for n in ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR', 'tex1', 'bst', 'bibtex', 'tex2', 'tex3', 'pdfinfo', 'pdffonts', 'pdftotext', 'render', 'frozen_pdf_cmp'))
    labels += ['pair_pdf_cmp', 'ldd_after']; need([r['label'] for r in rec['commands']] == labels, 'All 32 original native terminal commands')
    bylabel = {row['label']: row for row in rec['commands']}
    for row in rec['commands']:
        argv = flat_command(base, row, BUILD_ENV, number)
        if row['label'].endswith('_cmp'):
            targets = argv[2:] if number == 209 else argv[1:]
            expected = [base / 'cold_build_1/main.pdf', base / 'cold_build_2/main.pdf'] if row['label'] == 'pair_pdf_cmp' else [base / ('_'.join(row['label'].split('_')[:3]) + '/main.pdf'), paper / 'frozen_round2/main.pdf']
            need(argv == ['/usr/bin/cmp', *(['--'] if number == 209 else []), *map(str, expected)] and pin(base / row['stdout']['path'])['bytes'] == 0, 'Terminal exact native raw comparator'); equal(*targets)
    flat_ldd(base, inventories['LIBRARIES']); external, generated = set(), {}
    for index, row in enumerate(rec['builds'], 1):
        name = 'cold_build_' + str(index); cold = base / name; initial = obj(base / (name + '_SOURCE_ONLY_INITIAL.json'))
        need(row['directory'] == name and initial == row['source_only_initial'] == spec['source_pins'] and len(initial) == (11 if number == 208 else 8), 'Exact terminal source-only inputs')
        for n, value in initial.items():
            for location in (cold, paper, paper / 'frozen_round2'): pin(location / n, value)
        for variable in ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR'):
            text = raw(base / (name + '_' + variable + '.stdout')).decode().strip(); p = Path(text); p = (p if p.is_absolute() else cold / p).resolve()
            wanted = {'query_value': text, 'resolved': str(p), 'exists': False}; key = name + ':' + variable
            need(obj(base / (name + '_USER_ROOTS_BEFORE.json'))[key] == obj(base / 'USER_ROOTS_AFTER.json')[key] == wanted, 'Recorded absent TeX user root'); absence(p)
        for passno in (1, 2, 3):
            command = bylabel[name + '_tex' + str(passno)]
            need(command['argv'] == ['/usr/bin/pdflatex', '-no-shell-escape', '-recorder', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'] and command['cwd'] == str(cold), 'Exact terminal TeX pass command')
            for line in raw(base / (name + '_pass' + str(passno) + '.fls')).decode().splitlines():
                if not line.startswith('INPUT '): continue
                p = Path(line[6:]); p = (p if p.is_absolute() else cold / p).resolve()
                if p.is_relative_to(cold):
                    rel = p.relative_to(cold).as_posix(); need(rel in initial or p.suffix in {'.aux', '.bbl', '.out', '.toc'}, 'Only recorded local generated TeX roles')
                else:
                    need(str(p) in inventories['CONSUMED_TEX'] and inventories['CONSUMED_TEX'][str(p)] == inventories['TEX_INVENTORY'][str(p)], 'Every external TeX input in original pre-key', str(p)); external.add(str(p))
            if number == 209:
                perpass = obj(base / (name + '_pass' + str(passno) + '_TEX_INPUTS.json'))
                need(all(inventories['CONSUMED_TEX'].get(p) == v for p, v in perpass['consumed_external'].items()), 'Per-pass external ledger'); generated.update(perpass['generated_local'])
        bst = str(Path(raw(base / (name + '_bst.stdout')).decode().strip()).resolve()); need(bst in inventories['CONSUMED_TEX'], 'Located bibliography style'); external.add(bst)
        equal(base / (name + '_generated.bbl'), cold / 'main.bbl')
        log = raw(cold / 'main.log').decode(); diagnostics = {key: re.findall(r'^.*' + pattern + r'.*$', log, re.M) for key, pattern in
            (('undefined', 'undefined'), ('overfull', 'Overfull'), ('underfull', 'Underfull'), ('warnings', 'Warning'))}
        diagnostics['rerun'] = re.findall(r'^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$', log, re.M)
        need(diagnostics == row['actual_diagnostics'] == spec['diagnostics'] and all(not diagnostics[k] for k in ('undefined', 'overfull', 'warnings', 'rerun')), 'Exact retained final diagnostics')
        metadata = raw(base / (name + '_pdfinfo.stdout')).decode(); pages = int(re.search(r'^Pages:\s+(\d+)$', metadata, re.M).group(1))
        need(pages == row['pages'] == spec['pages'], 'Original PDF page measurement')
        fonts = [s.split()[-5:] for s in raw(base / (name + '_pdffonts.stdout')).decode().splitlines()[2:] if s.strip()]
        need(len(fonts) == row['embedded_fonts'] == spec['fonts'] and all(v[0] == 'yes' for v in fonts), 'All measured fonts embedded')
        need(not any(marker in raw(base / (name + '_main.txt')).decode() for marker in ('[VERIFY]', '??', '[?]')), 'Resolved final PDF text')
        for pdf in (cold / 'main.pdf', paper / 'main.pdf', paper / 'frozen_round2/main.pdf'): pin(pdf, spec['pdf'])
        equal(cold / 'main.pdf', paper / 'main.pdf')
        need(physical(cold / 'pages') == {'page-' + str(p) + '.png' for p in range(1, pages + 1)}, 'Every original rendered frame retained')
    need(external == set(inventories['CONSUMED_TEX']), 'Full per-pass external input union')
    if number == 209: need(generated == obj(base / 'GENERATED_LOCAL_TEX_INPUTS.json'), 'Full recorded P209 generated union')
    view = obj(spec['view_record']); need(view['reviewer'] == '/root' and view['open_visual_findings'] == 0 and
        view['status'] == ('ROOT_ACTUALLY_VIEWED_ALL_SEVEN_FINAL_PAGES_PASS' if number == 208 else 'ROOT_ACTUALLY_VIEWED_ALL_FOUR_FINAL_PAGES_PASS') and
        view['terminal_manifest_sha256'] == spec['package']['manifest']['sha256'] and view['pdf_sha256'] == spec['pdf']['sha256'] and
        [p['page'] for p in view['pages']] == list(range(1, spec['pages'] + 1)), 'Original actual all-page view attestation')
    for page in view['pages']:
        need(page['path'] == str(base / ('cold_build_1/pages/page-' + str(page['page']) + '.png')) and page['actually_displayed_and_viewed'] is True and page['observation'].strip(), 'Individual actual viewed-frame binding'); pin(page['path'], page['sha256'])
    need(view['retained_nonblocking_diagnostic'] == (spec['diagnostics']['underfull'][0] if number == 208 else None), 'Original view diagnostic boundary')
    if number == 209: need(view['measured_page_count'] == 4, 'Actual root measured page count')
    if number == 209: modern_outer(spec, rec, True)
    return {'builds_reused': 2, 'native_commands': 32, 'pages_each': spec['pages'], 'previous_actual_pages_reused': spec['pages'], 'key_counts': countmap}


def main():
    global CASE, ALIASES
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--expected-preparation-sha256', required=True); args = parser.parse_args()
    need(Path(__file__) == PREP / 'inspect.py' and Path.cwd() == ROOT and Path(sys.executable).resolve() == PY[209] and
         dict(os.environ) == ENV and sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode,
         'Require exact source/system interpreter/cwd/minimal environment and -I -S -B')
    need(sys.pycache_prefix and re.fullmatch(re.escape(str(BATCH / 'qa')) + r'/p208_p209_reuse_[0-9]{2,}/unused_checker_cache', sys.pycache_prefix), 'Require exact scoped absent caller-chosen cache')
    absence(sys.pycache_prefix)
    package({'root': str(PREP), 'manifest': {'sha256': args.expected_preparation_sha256}, 'payloads': 5})
    contract = obj(PREP / 'INPUT_PINS.json'); declarations = obj(PREP / 'ALIASES.json')
    need(len(declarations) == 6, 'Only six exact documentary alias roles')
    for row in declarations:
        key = (row['original'], row['sha256']); need(key not in ALIASES, 'Duplicate alias role')
        need(Path(row['original']).name in {'FINDINGS.json', 'SHA256SUMS', 'FINAL_THEOREM_CONTRACTS.md'}, 'Scientific/runtime alias forbidden')
        need(row['cases'] in (['p208_a'], ['p208_b'], ['p209_b']), 'Only declared strict-pair documentary role')
        pin(row['physical'], row['sha256']); pin(row['provenance'], contract['fixed_inputs'][row['provenance']])
        if row['selector'] == 'exact_root_pair_relocations':
            need(any(v['original'] == row['original'] and v['preserved'] == row['physical'] and v['historical']['sha256'] == row['sha256']
                     for v in obj(row['provenance'])[row['selector']]), 'Exact P208 A original relocation')
        elif row['selector'] == 'exact_original_at_hash':
            need(obj(row['provenance'])[row['original'] + ' @ ' + row['sha256']] == row['physical'], 'Exact P209 B original relocation')
        elif row['selector'].startswith('initial_'):
            need(obj(row['provenance'])[row['selector']] == row['sha256'] and Path(row['physical']).parent == Path(row['provenance']).parent / 'initial_snapshot', 'Exact P208 B initial documentary snapshot')
        else:
            need(row['sha256'] + '  ' + row['selector'] in raw(row['provenance']).decode().splitlines() and
                 Path(row['provenance']).parent / row['selector'] == Path(row['physical']), 'Exact archived theorem-contract row')
        ALIASES[key] = row
    for path, expected in contract['fixed_inputs'].items(): pin(path, expected)
    for spec in contract['accepted_packages']: package(spec)
    results = {}
    for CASE, spec in contract['pairs'].items(): results[CASE] = old_pair(spec) if spec['paper_number'] == 208 else new_pair(spec)
    for CASE, spec in contract['builds'].items(): results[CASE] = build_pair(spec)
    need(set(USED) == {p + ' @ ' + digest for p, digest in ALIASES}, 'Every declared documentary alias is exactly used')
    for CASE, value, state in CONFIGURATIONS:
        need(configuration(value, False) == state, 'Configuration presence/kind/symlink changed during inspection')
    for CASE, p, is_dir, exists, resolved, symlink in DIRECTORY_STATES:
        need((p.is_dir(), p.exists(), str(p.resolve()), p.is_symlink()) == (is_dir, exists, resolved, symlink), 'Directory presence/kind changed during inspection', str(p))
    CASE = 'final_reread'
    for case, label, function, expected in MEMBERSHIPS:
        need(function() == expected, 'Membership changed during inspection', {'case': case, 'group': label})
    for name in ABSENCES: absence(name)
    for name in list(TREES): physical(Path(name))
    before = dict(CACHE)
    for name, value in before.items(): need(measured(name) == value, 'Final complete reread changed', name)
    digest = hashlib.sha256((json.dumps(before, sort_keys=True, separators=(',', ':')) + '\n').encode()).hexdigest()
    print(json.dumps({'status': 'PASS_CURRENT_KEYS_REUSED_NOT_NEW_EXECUTIONS_OR_BATCH_ACCEPTANCE', 'results': results,
        'checks': CHECKS, 'current_paths_reread': len(before), 'current_read_key_sha256': digest,
        'original_ledger_references': LEDGERS, 'documentary_aliases_used': USED, 'raw_byte_comparisons_read_only': RAW_COMPARISONS,
        'mathematical_executions': 0, 'builds': 0, 'page_views': 0, 'external': 'HOLD_EXTERNAL',
        'boundary': 'Complete named known keys and archived native evidence; recorded settings and sampled coverage reused. No old code imports, new process execution, OS reconstruction or continuous tracing.'}, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except BaseException as error:
        print(json.dumps({'status': 'FAIL_REUSE_KEY_AFFECTED_FRESH_CHECK_REQUIRED', 'case': CASE,
            'error': str(error), 'traceback': traceback.format_exc(), 'checks_completed': CHECKS,
            'current_paths_seen': len(CACHE), 'mathematical_executions': 0, 'builds': 0, 'page_views': 0,
            'no_scientific_or_runtime_alias_fallback': True}, sort_keys=True))
        raise SystemExit(1)
