#!/usr/bin/env python3
"""P210 terminal artifact reader revision 01, preparation source only.

No scientific code, old writer/reader, builder, view tool or child command
is imported/executed. Preparation does not execute this reader. The final
contract binds actual terminal/root-view acceptance and first pending lifecycle.
"""
import ast
from collections import Counter
from datetime import datetime, timezone
import gzip
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shlex
import sys
import sysconfig
import traceback
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_terminal_artifact_revision_01'
PRIOR = QA / 'p210_terminal_artifact_preparation'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
A, B = QA.parent / 'reviews/p210_a', QA.parent / 'reviews/p210_b'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PY_PATH = ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload']
AUTHOR_SEAL = 'b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c'
R0_SEAL = 'e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26'
R1_SEAL = 'be54b79806d90f22037cee877f92074e744b2ef27bcc0b6b2e4f8dfa658446e0'
R2_SEAL = 'a46fb6688ce56fbf62f69b8c652fff88923e3778c81647294bae544f5e86a703'
CHECKS, SEEN, ALIASES, USED_ALIASES, BASE_KEYS = Counter(), {}, {}, set(), {}
REPORT_KEYS = {}
MANIFESTS, BYTE_COMPARISONS, NATIVE_RECORDS, CURRENT_SCOPES = {}, Counter(), [], []
NATIVE = []
BASE_CONFIG_ROOTS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/lib/locale/C.utf8',
                                  '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv')))
BUILD_CONFIG_ROOTS = tuple(map(Path, ('/usr/local/share/texmf', '/root/texmf',
    '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var',
    '/usr/local/share/fonts', '/root/.fonts', '/root/.fontconfig',
    '/root/.config/fontconfig', '/root/.cache/fontconfig', '/root/.local/share/fonts',
    '/etc/xdg/fontconfig', '/etc/profile.d')))
BUILD_TREE_ROOTS = tuple(map(Path, ('/etc/texmf', '/var/lib/texmf', '/usr/share/texlive/texmf-dist',
    '/usr/share/texmf', '/etc/fonts', '/usr/share/fontconfig', '/var/cache/fontconfig',
    '/usr/share/poppler', '/usr/share/fonts')))
DATA_ROOTS = tuple(map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')))
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
STDLIB = Path('/usr/lib/python3.10')
TREE_ROOTS = tuple(map(Path, ('/usr/lib/python3.10', '/usr/lib/locale', '/usr/lib/x86_64-linux-gnu/gconv')))

def ck(ok, label, detail=''):
    CHECKS[label] += 1
    if not ok:
        raise AssertionError((label, detail))

def need(ok, label):
    ck(ok, 'accepted_strict_helper', label)

def val(path):
    row = pin(path)
    return {'sha256': row['sha256'], 'bytes': row['size']}

def file_key(path):
    p = Path(path)
    ck(p.is_file(), 'physical_file', str(p))
    h = sha256()
    with p.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return {'real': str(p.resolve()), 'sha256': h.hexdigest(), 'size': p.stat().st_size,
            'symlink': os.readlink(p) if p.is_symlink() else None}

def pin(path, expected=None, force=False):
    name = str(Path(path))
    if force or name not in SEEN:
        value = file_key(path)
        ck(name not in SEEN or value == SEEN[name], 'read_key_stability', name)
        SEEN[name] = value
    value = SEEN[name]
    if expected is not None:
        if isinstance(expected, str):
            ck(value['sha256'] == expected, 'expected_sha256', name)
        elif set(expected) == {'real', 'sha256', 'size', 'symlink'}:
            ck(value == expected, 'exact_physical_ledger_key', name)
        else:
            ck(value['sha256'] == expected['sha256'], 'expected_record_sha256', name)
            size = expected.get('bytes', expected.get('size'))
            ck(size is None or value['size'] == size, 'expected_record_size', name)
    return value

def raw(path):
    expected = pin(path)
    value = Path(path).read_bytes()
    ck(len(value) == expected['size'] and sha256(value).hexdigest() == expected['sha256'],
       'full_decoded_input_raw_stability', str(path))
    return value

def obj(path):
    value = raw(path)
    return json.loads(gzip.decompress(value) if str(path).endswith('.gz') else value)

def physical(base):
    files = set()
    for p in base.rglob('*'):
        ck(not p.is_symlink(), 'no_workspace_package_symlink', str(p))
        if p.is_file():
            files.add(p.relative_to(base).as_posix())
    return files

def stripped_links(content):
    content = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', content)
    content = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', content)
    content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)

def current_configuration(path):
    p = Path(path)
    return {'lexists': os.path.lexists(p), 'exists': p.exists(), 'is_file': p.is_file(),
            'is_dir': p.is_dir(), 'resolved': str(p.resolve()),
            'symlink': os.readlink(p) if p.is_symlink() else None}

def configuration_scope(build):
    roots = TREE_ROOTS + (BUILD_TREE_ROOTS if build else ())
    conf_roots = BASE_CONFIG_ROOTS + (BUILD_CONFIG_ROOTS if build else ())
    conf = set(LIB_ROOTS + conf_roots + roots)
    conf.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
        '/etc/locale.conf', '/etc/default/locale', '/etc/nsswitch.conf', '/etc/localtime',
        '/etc/ssl/openssl.cnf', '/usr/lib/ssl/openssl.cnf', '/usr/lib/locale/locale-archive',
        '/usr/lib/python310.zip', '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg',
        '/etc/fonts/local.conf', '/root/.fonts.conf', '/root/.config/fontconfig/fonts.conf',
        sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
    for base in map(Path, ('/usr/bin', '/usr/lib')):
        conf.update(base / n for n in ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
    for name in ('LDLIBRARY', 'INSTSONAME'):
        value = sysconfig.get_config_var(name)
        if value:
            conf.add(Path('/usr/lib') / (value + '._pth'))
    loader = re.search(r'^RTLDLIST="([^"]+)"', raw('/usr/bin/ldd').decode(), re.M)
    ck(loader is not None, 'actual_ldd_loader_declaration')
    conf.update(map(Path, loader.group(1).split()))
    return roots, conf_roots, conf

def selected_tree_path(path, roots, conf_roots):
    p = Path(path)
    if any(p.is_relative_to(base) and p != base for base in conf_roots):
        return True
    if any(p.is_relative_to(base) and p != base for base in roots):
        if not any(x in {'__pycache__', 'site-packages', 'dist-packages'} for x in p.parts) and p.suffix not in {'.pyc', '.pyo'}:
            return True
    for base in LIB_ROOTS:
        if p.is_relative_to(base) and p != base and (p.name.endswith('.so') or '.so.' in p.name):
            if base != Path('/usr/local/lib') or len(p.relative_to(base).parts) == 1:
                return True
    return False

def current_membership(ledger, build):
    roots, conf_roots, conf = configuration_scope(build)
    ck(set(ledger['configuration']) == set(map(str, conf)), 'exact_declared_configuration_scope', build)
    for name, expected in ledger['configuration'].items():
        ck(current_configuration(name) == expected, 'current_configuration_presence_link', name)
    discovered = set()
    for base in roots:
        if base.is_dir():
            discovered.update(str(p) for p in base.rglob('*') if p.is_file() and
                not any(x in {'__pycache__', 'site-packages', 'dist-packages'} for x in p.parts)
                and p.suffix not in {'.pyc', '.pyo'})
    for base in conf_roots:
        if base.is_dir():
            discovered.update(str(p) for p in base.rglob('*') if p.is_file())
    for base in LIB_ROOTS:
        choices = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        discovered.update(str(p) for p in choices if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    fixed = {p for p in ledger['files'] if not selected_tree_path(p, roots, conf_roots)}
    current = fixed | discovered | {str(p) for p in conf if p.is_file()}
    ck(current == set(ledger['files']), 'current_selected_membership_exact',
       {'added': sorted(current - set(ledger['files'])), 'removed': sorted(set(ledger['files']) - current)})
    return {'files': len(current), 'configuration': len(conf), 'fixed_named_files': len(fixed),
            'selected_current_tree_files': len(discovered)}

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


def native(directory, expected):
    attempt, result = obj(directory / 'ATTEMPT.json'), obj(directory / 'RESULT.json')
    ck(attempt['environment'] == ENV, 'native_exact_environment', str(directory))
    ck(type(result['native_returncode']) is int and result['native_returncode'] == expected,
       'actual_integer_native_exit', str(directory))
    ck(attempt['argv'] and Path(attempt['argv'][0]).is_absolute() and Path(attempt['cwd']).is_absolute(),
       'absolute_actual_native_command', str(directory))
    pin(attempt['argv'][0], attempt.get('executable'))
    inner = 'start_ns' in attempt
    if inner:
        ck(type(attempt['start_ns']) is int and type(result['end_ns']) is int and
           result['end_ns'] >= attempt['start_ns'] and result['timed_out'] is False,
           'inner_native_chronology_timeout', str(directory))
        owner, settlement = result['native_pid'], result['process_group_settlement']
    else:
        ck(all(result.get(k) == v for k, v in attempt.items()), 'outer_start_fields_retained', str(directory))
        ck(result['ended_epoch'] >= attempt['started_epoch'] and attempt['timeout_seconds'] == 600,
           'outer_native_chronology_timeout', str(directory))
        owner, settlement = result['pid'], result['settlement']
        name = directory.name
        launcher = 'launch_build_v2.py' if name == 'build02' else 'launch.py' if name in ('produce01', 'pair01', 'build01') else 'launch_command.py'
        pin(B / launcher, attempt['launcher_source'])
        if 'engine_source' in attempt:
            pin(B / 'instrumentation' / ('evidence_build_v2.py' if name == 'build02' else 'evidence.py'), attempt['engine_source'])
    ck(type(owner) is int and owner > 0 and result['owned_pgid'] == result['owned_sid'] == owner,
       'actual_owned_group_identity', str(directory))
    ck(settlement['quiescent'] is True and all(r['state'] == 'Z' and r['sid'] == owner
       and r.get('pgid', owner) == owner for r in settlement['remaining_members']),
       'settled_native_raw_streams', str(directory))
    for name in ('stdout', 'stderr'):
        pin(directory / name, result[name] if name in result else result[name + '_sha256'])
    for arg in attempt['argv']:
        if arg.startswith('pycache_prefix='):
            cache = Path(arg.split('=', 1)[1])
            ck(cache.is_absolute() and not os.path.lexists(cache), 'declared_absent_native_cache', str(cache))
    NATIVE.append({'directory': directory.relative_to(B).as_posix(), 'native_returncode': expected,
                   'argv': attempt['argv'], 'cwd': attempt['cwd'], 'owner': owner,
                   'streams': {name: pin(directory / name) for name in ('stdout', 'stderr')}})
    return attempt, result


def sha_record(record):
    ck(isinstance(record, dict) and set(record) == {'sha256', 'bytes'}, 'exact byte-key record')
    ck(re.fullmatch('[0-9a-f]{64}', record['sha256']) is not None and
       type(record['bytes']) is int and record['bytes'] >= 0, 'valid byte-key fields')
    return record


def current_record(record):
    ck(isinstance(record, dict) and set(record) == {'real', 'sha256', 'size', 'symlink'},
       'exact current rich-key schema')
    ck(Path(record['real']).is_absolute() and type(record['size']) is int and record['size'] >= 0 and
       re.fullmatch('[0-9a-f]{64}', record['sha256']) is not None and
       (record['symlink'] is None or type(record['symlink']) is str), 'valid current rich fields')
    return record


def convert_rich(record):
    ck(isinstance(record, dict) and set(record) == {'resolved', 'sha256', 'bytes', 'symlink'},
       'exact original rich-key schema')
    return current_record({'real': record['resolved'], 'sha256': record['sha256'],
                           'size': record['bytes'], 'symlink': record['symlink']})


def register_alias(logical, physical, original, provenance):
    """Only explicit actual (logical path, hash, size) roles; no search/fallback."""
    logical, physical = str(Path(logical)), str(Path(physical))
    current_record(original)
    ck(Path(logical).is_absolute() and Path(physical).is_absolute() and logical != physical,
       'distinct absolute exact historical role')
    ck(original['real'] == logical and original['symlink'] is None,
       'original documentary resolution retained not overwritten by history')
    actual = pin(physical, {'sha256': original['sha256'], 'bytes': original['size']})
    ck(actual['real'] == physical and actual['symlink'] is None, 'actual physical history resolution')
    key = (logical, original['sha256'], original['size'])
    row = {'logical': logical, 'original': original, 'physical': physical,
           'physical_record': actual, 'provenance': provenance}
    ck(key not in ALIASES or ALIASES[key] == row, 'one physical target per exact historical triple')
    ALIASES[key] = row
    return row


def historical_record(logical, expected):
    expected = current_record(expected)
    key = (str(Path(logical)), expected['sha256'], expected['size'])
    if key in ALIASES:
        row = ALIASES[key]
        ck(expected == row['original'], 'all original logical rich fields retained')
        USED_ALIASES.add(key)
        pin(row['physical'], row['physical_record'])
        return row['physical'], row['physical_record']
    return str(Path(logical)), pin(logical, expected)


def historic_hash_path(logical, digest):
    """Legacy hash-only manifest role uses its one declared actual-size triple.

    This is not a generic missing-file fallback: only already registered exact
    documentary aliases may match; every other role remains its original path.
    """
    matches = [row for key, row in ALIASES.items() if key[:2] == (str(Path(logical)), digest)]
    ck(len(matches) <= 1, 'legacy role has at most one actual-size history triple')
    if matches:
        row = matches[0]
        return historical_record(logical, row['original'])[0]
    pin(logical, digest)
    return str(Path(logical))


def original_bytes(logical, digest):
    return raw(historic_hash_path(logical, digest))


def full_compare(left, right, label, left_sha=None, right_sha=None):
    l = raw(left) if left_sha is None else original_bytes(left, left_sha)
    r = raw(right) if right_sha is None else original_bytes(right, right_sha)
    ck(l == r, 'full Python raw comparison not a native command', label)
    BYTE_COMPARISONS[label] += 1


def manifest_rows(path):
    data = raw(path)
    ck(data.endswith(b'\n'), 'manifest complete newline', str(path))
    result = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(match is not None, 'exact manifest row', str(path))
        digest, name = match.groups()
        part = Path(name)
        ck(part.parts and not part.is_absolute() and '..' not in part.parts and
           part.as_posix() == name and name not in result and '\x00' not in name,
           'manifest safe unique relative role', name)
        result[name] = digest
    return result


def complete_package(base, expected, count, seal_name='SHA256SUMS'):
    base = Path(base)
    pin(base / seal_name, expected)
    rows = manifest_rows(base / seal_name)
    ck(len(rows) == count and seal_name not in rows and physical(base) == set(rows) | {seal_name},
       'complete nonself physical package', str(base))
    for name, digest in rows.items():
        pin(base / name, digest)
    MANIFESTS[str(base / seal_name)] = rows
    return rows


def historical_package_rows(base, digest, count):
    selected = historic_hash_path(Path(base) / 'SHA256SUMS', digest)
    rows = manifest_rows(selected)
    ck(len(rows) == count and 'SHA256SUMS' not in rows, 'entire original package manifest role')
    for name, value in rows.items():
        historic_hash_path(Path(base) / name, value)
    return rows


def utc_timestamp(value):
    instant = datetime.fromisoformat(value)
    ck(instant.tzinfo is not None and instant.utcoffset().total_seconds() == 0,
       'actual UTC timestamp')
    return instant


def bind_full_base(original_map, expected_count, label, original_schema=True):
    ck(isinstance(original_map, dict) and len(original_map) == expected_count,
       'full recorded dependency map census', label)
    physical_map = {}
    for name, record in original_map.items():
        ck(Path(name).is_absolute(), 'absolute recorded logical path')
        original = convert_rich(record) if original_schema else current_record(record)
        physical_name, current = historical_record(name, original)
        ck(physical_name not in physical_map or physical_map[physical_name] == current,
           'compatible exact historical rebase', label)
        physical_map[physical_name] = current
        ck(physical_name not in BASE_KEYS or BASE_KEYS[physical_name] == current,
           'all reused bases agree on complete physical key', label)
        BASE_KEYS[physical_name] = current
    return physical_map


def original_native_summary(launch_name, completion_name, expected_session, author=False):
    launch, completion = obj(QA / launch_name), obj(QA / completion_name)
    if author:
        ck(launch['session_id'] == completion['session_id'] == expected_session and
           launch['output'] == '' and completion['exit_code'] == 0 and
           completion['output_truncated'] is False, 'actual author parent envelope')
        return json.loads(completion['stdout'])
    ck(launch['result']['session_id'] == completion['session_id'] == expected_session and
       launch['result']['output'] == '' and type(completion['result']['exit_code']) is int and
       completion['result']['exit_code'] == 0, 'actual complete nested parent envelope')
    return json.loads(completion['result']['output'])


def recorded_manifest_native(record, rows, expected_base):
    ck(record['argv'] == ['/usr/bin/sha256sum', '--check', 'SHA256SUMS'] and
       record['cwd'] == str(expected_base) and record['environment'] == ENV and
       type(record['exit']) is int and record['exit'] == 0 and record['stderr_utf8'] == '',
       'actual archived complete manifest command')
    expected_stdout = ''.join(name + ': OK\n' for name in rows)
    ck(record['stdout_utf8'] == expected_stdout and
       record['stdout_sha256'] == sha256(expected_stdout.encode()).hexdigest() and
       record['stderr_sha256'] == sha256(b'').hexdigest(), 'entire archived native manifest stdout')
    NATIVE_RECORDS.append({'kind': 'old_native_manifest', 'argv': record['argv'], 'cwd': record['cwd']})


def strict_sample(data, known, cache, argv):
    ck(data['environment'] == ENV and data['cwd'] == str(ROOT) and
       data['executable'] == '/usr/bin/python3.10' and data['sys_path'] == PY_PATH and data['argv'] == argv,
       'exact strict runtime identity path argv')
    ck(data['pycache_prefix'] == str(cache) and data['cache_lexists'] is False and
       not os.path.lexists(cache), 'strict exact absent cache')
    ck(all(value in data['flags'] for value in ('optimize=0', 'isolated=1', 'no_site=1',
       'dont_write_bytecode=1', 'ignore_environment=1')), 'strict isolated source-only flags')
    maps = data['proc_maps'].encode()
    ck(len(maps) == data['proc_maps_bytes'] and sha256(maps).hexdigest() == data['proc_maps_sha256'],
       'entire original raw process maps')
    mapped = set()
    for line in data['proc_maps'].splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            ck(not fields[5].endswith(' (deleted)'), 'no recorded deleted strict mapping')
            mapped.add(str(Path(fields[5]).resolve(strict=True)))
    ck(mapped == set(data['mapped_files']) and data['volatile_proc_maps_not_an_immutable_input'] is True,
       'complete raw maps reconstructed with bounded sample scope')
    for name, row in list(data['mapped_files'].items()) + [(row['path'], row) for row in data['modules'].values()]:
        ck(name in known and all(known[name][key] == row[key] for key in ('bytes', 'sha256')) and
           Path(name).suffix not in {'.pyc', '.pyo'}, 'all strict sampled modules/maps covered by full keys')
        pin(name, {'bytes': row['bytes'], 'sha256': row['sha256']})


def strict_commands(role, prep, package, out, resources):
    extensions = sorted(name for name in resources if name.startswith(str(STDLIB) + '/') and name.endswith('.so'))
    cmp = lambda left, right: ['/usr/bin/cmp', '--', str(left), str(right)]
    commands = {'00_cmp_runner_source': cmp(prep / 'run_pair.py', out / 'sources/run_pair.py'),
                '01_cmp_verifier_source': cmp(package / 'verify.py', out / 'sources/verify.py')}
    if role != 'author':
        commands['01a_cmp_parameters_source'] = cmp(package / 'PARAMETERS.json', out / 'sources/PARAMETERS.json')
    commands['02_ldd_before'] = ['/usr/bin/ldd', '/usr/bin/python3.10', '/usr/bin/cmp'] + extensions
    for number in ('01', '02'):
        commands['03_verify_' + number] = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(out / ('unused_child_' + number + '_cache')),
            str(out / 'sources/run_pair.py'), 'child', number, 'p210_' + role]
    for number in ('01', '02'):
        commands['04_cmp_canonical_' + number] = cmp(out / ('commands/03_verify_' + number + '/stdout.raw'), package / 'CANONICAL.json')
    commands['05_cmp_pair'] = cmp(out / 'commands/03_verify_01/stdout.raw', out / 'commands/03_verify_02/stdout.raw')
    commands['06_ldd_after'] = ['/usr/bin/ldd', '/usr/bin/python3.10', '/usr/bin/cmp'] + extensions
    return commands


def strict_native_records(role, out, result, expected, entered_time):
    commands = result['commands']
    ck([command['label'] for command in commands] == list(expected) and
       {path.name for path in (out / 'commands').iterdir()} == set(expected), 'all actual strict native labels/directories')
    end_result = utc_timestamp(result['ended_utc'])
    previous, groups = entered_time, set()
    for command in commands:
        label = command['label']
        directory = out / 'commands' / label
        attempt, receipt = obj(directory / 'ATTEMPT.json'), obj(directory / 'RECEIPT.json')
        common = {'argv': expected[label], 'cwd': str(ROOT), 'environment': ENV,
                  'started_utc': attempt['started_utc'], 'timeout_seconds':
                  (300 if role == 'b' else 600) if label.startswith('03_verify_') else 60}
        if role == 'b':
            common.update(stdin='DEVNULL', new_owned_session_requested=True)
        ck(attempt == dict(common, status='ATTEMPTED', exit_code=None), 'all original native prespawn fields exact')
        expected_fields = set(common) | {'status', 'exit_code', 'ended_utc', 'wrapper_exit_code', 'spawned',
            'streams_complete', 'timed_out', 'failure', 'stream_scope', 'stdout', 'stderr'}
        if role == 'b':
            expected_fields.update(('interrupted', 'process_group_settlement'))
        ck(set(receipt) == expected_fields and all(receipt[key] == value for key, value in common.items()) and
           command == dict(receipt, label=label), 'full original receipt schema no retrofit fields')
        ck(receipt['status'] == 'COMPLETED' and receipt['failure'] is None and receipt['spawned'] is True and
           receipt['streams_complete'] is True and receipt['timed_out'] is False and
           all(type(receipt[key]) is int and receipt[key] == 0 for key in ('exit_code', 'wrapper_exit_code')),
           'actual completed strict native success')
        started, ended = utc_timestamp(receipt['started_utc']), utc_timestamp(receipt['ended_utc'])
        ck(previous <= started <= ended <= end_result and
           (ended - started).total_seconds() <= receipt['timeout_seconds'], 'whole original strict command chronology')
        previous = ended
        if role == 'b':
            settlement = receipt['process_group_settlement']
            ck(receipt['interrupted'] is False and set(settlement) == {'native_returncode', 'owned_pgid',
               'owned_sid', 'quiescent', 'remaining_members', 'signals'} and
               type(settlement['native_returncode']) is int and settlement['native_returncode'] == 0 and
               type(settlement['owned_pgid']) is type(settlement['owned_sid']) is int and
               settlement['owned_pgid'] == settlement['owned_sid'] > 0 and settlement['quiescent'] is True and
               settlement['signals'] == settlement['remaining_members'] == [], 'actual B owned settlement only')
            groups.add(settlement['owned_pgid'])
        expected_scope = ('Every emitted native byte retained in exclusive files; hashes finalized only after owned-group '
            'quiescence. A timeout/interruption remains an unsuccessful partial computation.' if role == 'b' else
            'Native child streams; timeout captures are partial. Spawn failure has no native child streams/returncode; '
            'its diagnostic is failure above.')
        ck(receipt['stream_scope'] == expected_scope, 'exact accepted generation of stream scope')
        for stream in ('stdout', 'stderr'):
            pin(directory / (stream + '.raw'), sha_record(receipt[stream]))
        ck(raw(directory / 'stderr.raw') == b'', 'full old strict empty stderr')
        if expected[label][0] == '/usr/bin/cmp':
            ck(raw(directory / 'stdout.raw') == b'', 'full old strict comparison stdout')
            full_compare(expected[label][-2], expected[label][-1], role + '_old_native_cmp_operand')
        NATIVE_RECORDS.append({'kind': 'old_strict_native', 'role': role, 'label': label,
                               'argv': expected[label], 'owned_settlement_recorded': role == 'b'})
    ck(role != 'b' or len(groups) == 10, 'ten distinct actual B groups')
    ck(obj(out / 'COMMAND_CLOSURE.json') == {'command_count': len(expected),
       'native_streams_rechecked': 2 * len(expected),
       'scope': 'Every entire recorded receipt, pre-spawn record and raw stream rechecked after the pair.'},
       'entire strict command closure')


def strict_original_canonical(role, data, parameters):
    if role == 'author':
        ck(data['schema'] == 'P210_AUTHOR_FULL_CANONICAL_V1' and data['mass_box'] == [1, 12] and
           data['checks'] == sum(data['checks_by_kind'].values()) == 197471 and
           data['totals'] == {'states': 4095, 'edges': 4095, 'targets': 4095, 'image_objects': 265,
                              'triangular_objects': 265, 'surplus_witnesses': 28}, 'original author schema and complete census')
        ck([row['N'] for row in data['masses']] == list(range(1, 13)) and
           sum(len(row['states']) for row in data['masses']) == 4095 and
           sum(len(row['targets']) for row in data['masses']) == 4095 and
           sum(len(row['triangular_objects']) for row in data['masses']) == 265, 'all original author output rows')
    elif role == 'a':
        ck(data['schema'] == 'p210-review-a-cut-graph-v1' and data['parameters'] == parameters ==
           {'mass_min': 1, 'mass_max': 12, 'carrier': 'cumulative-cut-bitmask',
            'update': 'synchronous-old-weak-increasing-run-sums'} and
           data['checks'] == 133978 and data['total_states'] == 4095, 'original A schema and exact parameter contract')
        ck([row['N'] for row in data['tables']] == list(range(1, 13)) and
           all(len(row['states']) == len(row['targets']) == 1 << (row['N'] - 1) for row in data['tables']) and
           sum(len(row['triangular']) for row in data['tables']) == 265 and
           sum(len(row['witnesses']) for row in data['tables']) == 28 and
           sum(row['image_count'] for row in data['tables']) == 265, 'entire original A output rows')
    else:
        ck(set(data) == {'reviewer', 'representation', 'edge_construction', 'checks', 'states', 'census'} and
           data['reviewer'] == 'p210_b_reviewer' and data['checks'] == 51129 and
           data['representation'] == parameters['carrier'] == 'integer partitions followed by distinct multiset permutations' and
           data['edge_construction'] == parameters['edges'] == 'inverse weakly sorted refinements with strict boundary descents' and
           parameters['masses'] == [row['mass'] for row in data['census']] == list(range(1, 13)) and
           data['states'] == sum(len(row['states']) for row in data['census']) == 4095 and
           sum(len(row['triangular_codes']) for row in data['census']) == sum(row['image_size'] for row in data['census']) == 265 and
           all(row['carrier_size'] == len(row['states']) == 1 << (row['mass'] - 1) and
               sum(state['fibre'] for state in row['states']) == row['carrier_size'] for row in data['census']),
           'entire original B census and exact parameter representation')


def strict_pair(role, original_roles):
    captured = original_roles['pairs'][role]
    out, prep = Path(captured['directory']), QA / ('p210_' + role + '_strict_preparation')
    role_name = 'p210_' + role
    source = raw(prep / 'run_pair.py')
    tree = ast.parse(source)
    specs = [ast.literal_eval(node.value) for node in tree.body if isinstance(node, ast.Assign) and
             any(isinstance(target, ast.Name) and target.id == 'SPECS' for target in node.targets)]
    ck(len(specs) == 1 and set(specs[0]) == {role_name}, 'exact original recorder role AST never import')
    spec, package = specs[0][role_name], ROOT / specs[0][role_name]['package']
    prep_seals = {'author': '7d395ea1e6157c8a3cb0985d0f93a3a104b88540608626de1956916d0d00cecb',
                  'a': '260c698d7bac08bf938be0ddb090021b7566eaec953ad4fb7c7ea87e78a04ae8',
                  'b': '987367c15fae0bd4d34ebf6c97cd1ee2dc71d1f15782ec57d73f61a332d97eec'}
    prep_sha = prep_seals[role]
    preparation = complete_package(prep, prep_sha, 4)
    original_rows = historical_package_rows(package, spec['manifest_sha'], spec['payloads'])
    input_pins = obj(prep / 'INPUT_PINS.json')['inputs']
    for name, value in input_pins.items():
        selected = historic_hash_path(name, value['sha256'])
        pin(selected, value)
    pin(package / 'verify.py', spec['verifier_sha'])
    pin(package / 'CANONICAL.json', {'sha256': spec['canonical_sha'], 'bytes': spec['canonical_bytes']})
    pair_rows = complete_package(out, captured['manifest_sha256'], captured['payloads'])
    prefix = 'P210_' + role.upper() + '_STRICT'
    if role == 'b':
        prefix += '_ROOT'
    native = original_native_summary(prefix + '_LAUNCH.actual.json', prefix + '_COMPLETION.actual.json',
                                     {'author': 53547, 'a': 16907, 'b': 31521}[role], role == 'author')
    expected_native = {'status': 'PASS_ROOT_P210_' + role.upper() + '_STRICT_PAIR', 'errors': [],
        'source': val(prep / 'run_pair.py'), 'verifier': val(package / 'verify.py'), 'role': role_name,
        'known_inputs': captured['known_keys'], 'checks_each': [spec['checks']] * 2,
        'command_count': captured['native_command_count'],
        'closure': {'payloads': len(pair_rows), 'manifest': val(out / 'SHA256SUMS')},
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}
    ck(native == expected_native, 'entire old strict parent result including actual full seal')
    baseline = {'role': role_name, 'package_payloads': len(original_rows),
        'package_manifest': val(historic_hash_path(package / 'SHA256SUMS', spec['manifest_sha'])),
        'preparation_manifest': val(prep / 'SHA256SUMS'), 'verifier': val(package / 'verify.py'),
        'canonical': val(package / 'CANONICAL.json'),
        'package_files': sorted(str(package / name) for name in original_rows) + [str(package / 'SHA256SUMS')],
        'preparation_files': sorted(str(prep / name) for name in preparation) + [str(prep / 'SHA256SUMS')]}
    if role != 'author':
        pin(package / 'PARAMETERS.json', spec['parameters_sha'])
        baseline['parameters'] = val(package / 'PARAMETERS.json')
    ck(obj(out / 'PACKAGE_AND_PREPARATION_CLOSURE.json') == {'before': baseline, 'after': baseline},
       'complete original package/preparation role set independently rebuilt')
    copies = obj(out / 'SOURCE_ONLY_INITIAL.json')
    names = ['run_pair.py', 'verify.py'] + ([] if role == 'author' else ['PARAMETERS.json'])
    expected_copies = {}
    for name in names:
        origin = prep / name if name == 'run_pair.py' else package / name
        copy = out / 'sources' / name
        expected_copies[name] = {'origin': str(origin), 'copy': str(copy), **val(origin)}
        full_compare(origin, copy, role + '_source_copy')
    ck(copies == expected_copies and physical(out / 'sources') == set(names), 'exact original physical source-only capsule')
    resources, conf = obj(out / 'RESOURCE_NAMES_BEFORE.json'), obj(out / 'CONFIGURATION_BEFORE.json')
    ck(resources == obj(out / 'RESOURCE_NAMES_AFTER.json') == current_resources() and len(resources) == 3121,
       'entire strict current resource membership')
    ck(conf == obj(out / 'CONFIGURATION_AFTER.json') == configuration_snapshot() and len(conf) == 41,
       'entire strict reconstructed configuration scope')
    known = obj(out / 'INPUTS_BEFORE.json')
    known_names = set(baseline['package_files']) | set(baseline['preparation_files']) | set(resources) | set(input_pins)
    known_names.update(row['copy'] for row in copies.values())
    known_names.update(name for name, row in conf.items() if row['is_file'])
    known_names |= {str(Path(name).resolve(strict=True)) for name in known_names}
    ck(known == obj(out / 'INPUTS_AFTER.json') and set(known) == known_names and len(known) == captured['known_keys'],
       'all exact logical strict inputs rebuilt independently')
    bind_full_base(known, captured['known_keys'], role + '_strict')
    parent_argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
        'pycache_prefix=' + str(out / 'unused_parent_cache'), str(prep / 'run_pair.py'),
        'run', '--role', role_name, '--expected-preparation-sha256', prep_sha]
    launch = obj(QA / (prefix + '_LAUNCH.actual.json'))
    ck(shlex.split(launch['command']) == ['/usr/bin/env', '-i',
       *[key + '=' + value for key, value in ENV.items()], *parent_argv],
       'exact archived parent shell argv and ENV4 no synthesized native stderr')
    if role == 'a':
        ck(launch['cwd'] == str(ROOT), 'actual A outer cwd present')
    else:
        ck('cwd' not in launch, 'older author and B outer missing cwd remains missing')
    entered = obj(out / 'RUN_ENTERED.json')
    ck(entered['status'] == 'ENTERED_NOT_A_PRESPAWN_RECEIPT' and entered['argv'] == parent_argv[6:] and
       entered['interpreter_argv'] == parent_argv and entered['cwd'] == str(ROOT) and entered['environment'] == ENV and
       convert_rich(entered['source']) == pin(prep / 'run_pair.py'), 'actual entered strict record not new outer trace')
    for phase in ('before', 'after'):
        strict_sample(obj(out / ('observations/parent_' + phase + '.json')), known, out / 'unused_parent_cache', parent_argv[6:])
    result = obj(out / 'RESULT.json')
    ck(result['status'] == native['status'] and result['role'] == role_name and result['errors'] == [] and
       result['known_input_count'] == len(known) and result['source_only_system_python'] == '/usr/bin/python3.10' and
       result['OS_syscall_trace'] == 'NOT_COLLECTED' and result['no_new_all_size_proof_or_review'] is True and
       result['owner'] == 'OWNER_AMBER' and result['external_status'] == 'HOLD_EXTERNAL', 'actual strict pair accepted scope')
    ck(role != 'b' or result['unfinalized_native_labels'] == [], 'actual B has no unfinalized native groups')
    commands = strict_commands(role, prep, package, out, resources)
    strict_native_records(role, out, result, commands, utc_timestamp(entered['started_utc']))
    outputs = []
    for number in ('01', '02'):
        observed = obj(out / ('observations/child_' + number + '.json'))
        ck(observed['status'] == 'RETURNED' and observed['volatile_open_paths'] == [] and
           observed['source'] == {'path': str(out / 'sources/verify.py'), **val(package / 'verify.py')},
           'actual strict returned child and source role')
        if role == 'author':
            ck(not {'scientific_argv', 'parameters', 'parameter_locator'} & set(observed),
               'old author absent scientific argv fields not manufactured')
            scientific_argv = [str(out / 'sources/run_pair.py'), 'child', number, role_name]
        else:
            scientific_argv = [str(out / 'sources/verify.py')]
            if role == 'a':
                scientific_argv.append(str(out / 'sources/PARAMETERS.json'))
                ck('parameter_locator' not in observed, 'A explicit parameter argv not invented locator')
            else:
                ck(observed['parameter_locator'] == 'sibling of scientific __file__', 'actual B sibling parameter locator')
            ck(observed['scientific_argv'] == scientific_argv and observed['parameters'] ==
               {'path': str(out / 'sources/PARAMETERS.json'), **val(package / 'PARAMETERS.json')}, 'exact actual scientific parameter interface')
        cache = out / ('unused_child_' + number + '_cache')
        for phase in ('before', 'after'):
            strict_sample(observed[phase], known, cache, scientific_argv)
            ck(all(not Path(row['path']).is_relative_to(ROOT) or row['path'] == str(out / 'sources/run_pair.py')
                   for row in observed[phase]['modules'].values()), 'no extra project module in original strict child')
        opened_names = ['verify.py'] + ([] if role == 'author' else ['PARAMETERS.json'])
        opens = {str(out / 'sources' / name): val(out / 'sources' / name) for name in opened_names}
        ck(observed['opened_ordinary_files'] == opens and observed['python_open_events'] ==
           [{'path': name, 'mode': 'r', 'flags': os.O_RDONLY | os.O_CLOEXEC} for name in opens] and
           observed['nonfile_open_paths_at_end'] == [], 'all actual bounded open events no fabricated OS trace')
        for name, value in opens.items():
            ck(all(known[name][key] == value[key] for key in ('sha256', 'bytes')), 'strict opened source full-key coverage')
        output = out / ('commands/03_verify_' + number + '/stdout.raw')
        full_compare(output, package / 'CANONICAL.json', role + '_complete_canonical')
        data = obj(output)
        strict_original_canonical(role, data, None if role == 'author' else obj(package / 'PARAMETERS.json'))
        outputs.append({'number': number, 'checks': spec['checks'], 'stdout': val(output)})
    ck(result['results'] == outputs and result['raw_canonical_comparisons'] == 2 and
       result['raw_pair_comparisons'] == 1, 'entire strict two-result and three-comparison summary')
    linked = obj(out / 'LINKED_RUNTIME.json')
    ck(set(linked) == {'before', 'after'} and linked['before'] == linked['after'] and
       all(name in known for name in linked['before']), 'entire strict linked runtime interval')
    for label, phase in (('02_ldd_before', 'before'), ('06_ldd_after', 'after')):
        body = raw(out / ('commands/' + label + '/stdout.raw'))
        found = sorted({str(Path(os.fsdecode(name)).resolve()) for name in re.findall(rb'(/[^\s()]+)', body)
                        if Path(os.fsdecode(name)).is_file()})
        ck(b'not found' not in body and found == linked[phase], 'full original ldd output parsed exactly')
    CURRENT_SCOPES.append(('strict', resources, conf))
    return {'role': role, 'checks_each': [spec['checks']] * 2, 'known_keys': len(known),
            'native_commands': len(commands), 'pair_manifest': val(out / 'SHA256SUMS'),
            'reuse': 'PREVIOUS_ACTUAL_ROOT_PAIR_REUSED_UNDER_COMPLETE_CURRENT_KEYS',
            'missing_old_owned_settlement_fields_preserved': role != 'b', 'new_science_runs': 0}


def actual_history_roles(original_roles):
    for row in original_roles['exact_available_historical_aliases']:
        original = {'real': row['logical'], 'sha256': row['original_sha256'],
                    'size': row['original_size'], 'symlink': None}
        register_alias(row['logical'], row['physical'], original, row['provenance_role'])
        actual = obj(row['provenance_role'])
        if '/frozen_round1/' in row['physical']:
            anchor = actual['anchors'][Path(row['physical']).name]
            ck(anchor['original_path'] == row['logical'] and anchor['sha256'] == row['original_sha256'] and
               str(PAPER / 'frozen_round1' / anchor['physical_path']) == row['physical'], 'exact actual PRE_ROUND1 provenance')
        else:
            aliases = actual['initial_review_aliases']
            if isinstance(aliases, list):
                selected = [alias for alias in aliases if alias['original_path'] == row['logical']]
                ck(len(selected) == 1 and selected[0]['physical_path'] == row['physical'] and
                   selected[0]['sha256'] == row['original_sha256'], 'actual accepted A initial role')
            else:
                ck(aliases[row['logical']] == {'physical': row['physical'], 'sha256': row['original_sha256']},
                   'actual accepted B initial role')
    r2 = PAPER / 'frozen_round2'
    provenance = obj(r2 / 'ROUND2_PROVENANCE.json')
    old = original_roles['actual_b_final_map_recipe']['old_control_roles_requiring_actual_Round2_history']
    for logical, record in old.items():
        name = 'PRE_ROUND2_' + Path(logical).name
        anchor = provenance['anchors'][name]
        physical_name = r2 / anchor['physical_path']
        ck(anchor['original_path'] == logical and anchor['physical_path'] == 'ROUND2_ACCEPTANCE/' + name and
           anchor['sha256'] == record['sha256'], 'actual exact pre Round2 control role')
        register_alias(logical, physical_name, record, str(r2 / 'ROUND2_PROVENANCE.json'))
    preserved = QA / 'p210_preterminal_controls_01'
    complete_package(preserved, 'a6f2fa041a62dbbd824386b0af33e27588a7285835e2fd50a954824b4a962649', 7)
    receipt = obj(preserved / 'PRESERVATION.actual.json')
    parent = obj(QA / 'P210_PRETERMINAL_CONTROLS_ROOT.actual.json')
    ck(parent['result']['exit_code'] == 0 and parent['result']['chunk_id'] == 'cec83d' and
       parent['cwd'] == str(ROOT), 'actual root preterminal preservation outer native')
    returned = json.loads(parent['result']['output'])
    ck(returned['status'] == receipt['status'] == 'PASS_TWO_ACTUAL_P210_PRETERMINAL_CONTROLS_PRESERVED' and
       returned['copies'] == receipt['copies'] and returned['native_commands'] == receipt['commands'] and
       returned['payloads'] == 7 and returned['seal'] == val(preserved / 'SHA256SUMS') and
       receipt['old_whole_payloads'] == 2021 and receipt['inputs_unchanged'] is True,
       'entire actual two-control preservation result')
    expected_commands = []
    for name in ('ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256'):
        logical = str(PAPER / name)
        record = receipt['copies'][logical]
        ck(record['physical'] == str(preserved / name), 'exact preterminal physical role no guessed path')
        register_alias(logical, record['physical'], {'real': logical, 'sha256': record['sha256'],
                       'size': record['bytes'], 'symlink': None}, str(preserved / 'PRESERVATION.actual.json'))
        for argv in (['/usr/bin/cp', '--no-clobber', '--', logical, record['physical']],
                     ['/usr/bin/cmp', '--', logical, record['physical']]):
            expected_commands.append({'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
                                      'exit_code': 0, 'stdout': '', 'stderr': ''})
    ck(receipt['commands'] == expected_commands and len(receipt['complete_input_pins']) == 5,
       'four actual preservation native commands complete stdout/stderr')
    for path, expected in receipt['complete_input_pins'].items():
        selected = historic_hash_path(path, expected['sha256'])
        pin(selected, expected)
    NATIVE_RECORDS.extend({'kind': 'old_preterminal_preservation', **row} for row in expected_commands)
    ck(len(ALIASES) == 10, 'only ten physically available exact history triples')


def accepted_reviews():
    outputs = {}
    for role, package, expected_count, expected_seal, initial_count in (
            ('a', A, 552, 'f6b92663cb2a7909f85a25a892ee4433ccd6177e84c07bf7ceccc9555b191f6d', 484),
            ('b', B, 441, '57b7b7919846e3ff5890543f0373439b03cc7f0cf0e896b9db38cd14d5171462', 407)):
        final = complete_package(package, expected_seal, expected_count)
        initial_path = package / 'history/initial_before_delta/SHA256SUMS'
        initial = manifest_rows(initial_path)
        ck(len(initial) == initial_count and set(initial) <= set(final) and
           {name for name in initial if initial[name] != final[name]} == {'DELTA.md'},
           'only exact initial review DELTA changed all other payloads retained', role)
        for name, digest in initial.items():
            target = historic_hash_path(package / name, digest)
            ck(pin(target)['sha256'] == digest, 'every original review payload physically retained', role)
        current = obj(package / 'CURRENT_FINDINGS.json')
        original = obj(package / 'FINDINGS.json')
        root = obj(QA / ('P210_A_ROOT_DELTA_INSPECTION.actual.json' if role == 'a' else 'P210_B_ROOT_DELTA_INSPECTION.actual.json'))
        ck(root['paper'] == 'P210' and root['reviewer'] == '/root/p210_' + role + '_reviewer' and
           root['reviewer_delta_accepted'] is True and root['root_original_inspection_complete'] is True and
           root['root_replay_closure_complete'] is True and root['current_open_findings'] == 0 and
           root['author_manifest_sha256'] == AUTHOR_SEAL and root['review_manifest_sha256'] == expected_seal,
           'actual independent reviewer and full root acceptance')
        if role == 'a':
            ck(current['schema'] == 'p210-a-current-findings-v1' and current['reviewer'] == '/root/p210_a_reviewer' and
               current['verdict'] == 'ACCEPTED_EXACT_NO_CHANGE_DELTA' and current['census'] ==
               {'Critical': {'open': 0, 'resolved': 0}, 'Major': {'open': 0, 'resolved': 1},
                'Minor': {'open': 0, 'resolved': 0}, 'total_open': 0, 'total_resolved': 1} and
               len(current['findings']) == 1 and current['findings'][0]['id'] == 'P210-A-E1' and
               current['findings'][0]['status'] == 'resolved' and current['findings'][0]['severity'] == 'Major',
               'accepted A current zero open and historical resolved Major retained')
            ck(current['initial_findings_sha256'] == val(package / 'FINDINGS.json')['sha256'] and
               current['response_sha256'] == root['response_sha256'] == val(QA.parent / 'P210_A_RESPONSE.md')['sha256'] and
               current['findings'][0]['changed_scientific_inputs'] == [] and
               'unavailable' in current['findings'][0]['historical_loss_not_repaired'], 'A exact response and missing history not repaired')
        else:
            ck(current['reviewer'] == '/root/p210_b_reviewer' and current['same_actual_initial_reviewer'] is True and
               current['phase'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA' and current['accepted_delta'] is True and
               current['verdict'] == 'PASS_NARROW' and current['root_response_reviewed'] is True and
               current['current_open_counts'] == original['current_open_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 0} and
               current['current_manuscript_findings'] == original['current_manuscript_findings'] == [] and
               current['reviewer_infrastructure_resolved_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 2},
               'accepted B exact current census not initial verdict substitution')
            ck(current['inherited_A_findings'] == original['inherited_A_findings'] and
               [(row['id'], row['severity'], row['status']) for row in current['reviewer_infrastructure_findings']] ==
               [(row['id'], row['severity'], row['status']) for row in original['reviewer_infrastructure_findings']] and
               current['initial_findings_sha256'] == val(package / 'FINDINGS.json')['sha256'] and
               current['initial_report_sha256'] == val(package / 'REPORT.md')['sha256'] and
               current['accepted_response_sha256'] == root['response_sha256'] == val(QA.parent / 'P210_B_RESPONSE.md')['sha256'],
               'all B initial decisions failures inherited Major and exact response retained')
        for path, digest in root['evidence'].items():
            historic_hash_path(path, digest)
        outputs[role] = {'reviewer': current['reviewer'], 'final_payloads': len(final),
                         'initial_payloads_preserved': len(initial), 'current_open': 0,
                         'initial': initial, 'final': final, 'root': root}
    ck(outputs['a']['reviewer'] != outputs['b']['reviewer'], 'two actually distinct nonauthor reviewer identities')
    return outputs


def b_complete_reuse(original_roles, reviews):
    recipe = original_roles['actual_b_final_map_recipe']
    common = obj(recipe['common_path'])
    ck(common == obj(B / 'DELTA_INPUTS_AFTER.json.gz') and len(common) == 121013,
       'entire decoded B common interval not gzip byte equality')
    actual = original_native_summary('P210_B_FINAL_ORIGINALS_ROOT_LAUNCH.actual.json',
                                     'P210_B_FINAL_ORIGINALS_ROOT_COMPLETION.actual.json', 7664)
    ck(actual['schema'] == 'p210-B-final-root-original-receiver-v1' and actual['status'] ==
       'PASS_ROOT_P210_B_FINAL_SAME_REVIEWER_DELTA_AND_ORIGINAL_RECEPTION' and actual['checks'] == 2338172 and
       actual['physical_paths_fully_reread_twice'] == 121057 and actual['accepted_same_reviewer_delta'] is True,
       'actual complete B final root reception not a future result')
    extra = actual['current_read_keys_outside_B_common']
    ck(len(extra) == 44 and not set(common) & set(extra), 'exact actual disjoint B final extras')
    complete = {name: convert_rich(value) for name, value in common.items()} | extra
    encoded = json.dumps(complete, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()
    ck(len(complete) == 121057 and len(encoded) == recipe['canonical_bytes'] and
       sha256(encoded).hexdigest() == recipe['canonical_sha256'] ==
       actual['complete_current_read_map_canonical_sha256'] ==
       'c75e67753bb7cec027c788b1d00a78c977cfb99fb53153d9fe57511e546fea2d',
       'entire actual B root read map reconstructed independently')
    REPORT_KEYS.update(bind_full_base(complete, 121057, 'B_final_root_full_map', False))
    audit = obj(B / 'AUDIT_INPUTS.actual.json.gz')
    bind_full_base(audit, 120840, 'B_original_audit_full_map')
    initial_outer = obj(QA / 'P210_B_INITIAL_ORIGINALS_ROOT_COMPLETION.actual.json')
    initial_root = json.loads(initial_outer['result']['output'])
    old_extra = initial_root['extra_read_keys_not_in_B_audit_ledger']
    ck(len(old_extra) == 55 and not set(old_extra) & set(audit) and sha256(json.dumps(
       audit | old_extra, sort_keys=True, separators=(',', ':')).encode()).hexdigest() ==
       initial_root['all_current_read_keys_canonical_json_sha256'], 'complete initial B root map retained')
    # Independent membership reconstruction covers the four actually selected B
    # source/runtime scopes. Failed build01 has no invented successful interval.
    scopes = {}
    for label in ('produce01', 'pair01', 'build01', 'build02'):
        ledger = obj(B / label / 'INPUTS_BEFORE.json.gz')
        ck(ledger['membership'] == sorted(ledger['files']), 'entire original B membership array')
        if label != 'build01':
            ck(ledger == obj(B / label / 'INPUTS_AFTER.json.gz'), 'actual successful original B complete interval')
        for name, row in ledger['files'].items():
            historical_record(name, convert_rich(row))
        scopes[label] = current_membership(ledger, label.startswith('build'))
        CURRENT_SCOPES.append(('B', label, ledger, scopes[label]))
    ck(scopes == actual['current_B_scope_membership'], 'all B scopes equal actual accepted source-defined memberships')
    for phase in ('before', 'after'):
        summary = obj(B / ('DELTA_' + phase.upper() + '.actual.json'))
        ck(summary['checks'] == {'before': 1978529, 'after': 1978541}[phase] and
           summary['same_reviewer'] == '/root/p210_b_reviewer', 'actual B before after verdicts retained')
        roles = obj(B / ('DELTA_ROLES_' + phase.upper() + '.actual.json'))
        additions = {} if phase == 'before' else obj(B / 'DELTA_AFTER_EXTRA_INPUTS.actual.json')
        ck(all(values == sorted(set(values)) for values in roles.values()) and
           set().union(*(set(values) for values in roles.values())) == set(common) | set(additions),
           'all actual delta role groups and after-only additions')
        for name, value in additions.items():
            historical_record(name, convert_rich(value))
    closure = obj(B / 'DELTA_CLOSURE.actual.json')
    ck(closure['status'] == 'PASS_ACCEPTED_SAME_B_DELTA_FINAL_SEAL_GATE' and
       closure['native_record_count'] == len(closure['native_records']) == 66 and
       closure['initial_payloads_preserved'] == 407 and closure['common_input_keys'] == 121013,
       'actual full B final seal census and initial preservation')
    directories = sorted(str(path.parent.relative_to(B)) for path in B.rglob('RESULT.json')
                         if (path.parent / 'ATTEMPT.json').is_file())
    ck(directories == [row['directory'] for row in closure['native_records']], 'all actual B native directories')
    for row in closure['native_records']:
        native(B / row['directory'], row['native_returncode'])
    ck(len(NATIVE) == 66 and Counter(row['native_returncode'] for row in NATIVE) == {0: 64, 1: 2},
       'all B original plus delta natives two real failures unchanged')
    comparisons = obj(B / 'DELTA_FULL_BYTE_COMPARISONS.actual.json')
    ck(len(comparisons) == 995 and Counter(row['role'] for row in comparisons) ==
       actual['phase_reception']['comparison_roles'], 'all actual B full comparison operand roles')
    for row in comparisons:
        ck(set(row) == {'left', 'right', 'role', 'method'} and row['method'] == 'full Python bytes, not another native cmp',
           'actual original comparison schema')
        full_compare(row['left'], row['right'], 'B_delta_' + row['role'])
    found_links = []
    for doc in sorted(B.glob('*.md')):
        for href in stripped_links(raw(doc).decode()):
            target = href.strip().strip('<>').split('#', 1)[0]
            if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
                continue
            path = (doc.parent / unquote(target)).resolve()
            value = pin(path)
            found_links.append({'document': doc.name, 'href': href, 'physical': str(path),
                'sha256': value['sha256'], 'bytes': value['size'], 'resolved': value['real'], 'symlink': value['symlink']})
    ck(found_links == closure['links'] and len(found_links) == 29, 'entire B genuine Markdown link closure')
    return {'complete_original_map': recipe, 'reused_root_checks': actual['checks'], 'full_keys': 121057,
            'B_native_records': 66, 'preserved_native_failures': 2, 'raw_operand_comparisons': 995,
            'current_membership_scopes': scopes, 'new_scientific_runs': 0, 'new_reviews': 0}


def original_hrefs(path):
    # The frozen maps were made by this literal parser. Keep that recorded
    # occurrence convention distinct from the stricter new-document parser.
    return [href for token in re.findall(r'\[[^\]]*\]\(([^)]+)\)', raw(path).decode())
            if (href := token.strip().strip('<>')) and
            not href.startswith(('https://', 'http://', 'mailto:', '#')) and href.split('#', 1)[0]]


def round0_closure(author):
    r0 = PAPER / 'frozen_round0'
    frozen = complete_package(r0, R0_SEAL, 493)
    source = QA / 'freeze_p210_round0.py'
    expected = dict(author)
    expected.update({'AUTHOR_MANIFEST.sha256': AUTHOR_SEAL,
        'ROOT_ADOPTION.md': pin(PAPER / 'ROOT_ADOPTION.md')['sha256'],
        'FREEZE_ADAPTER.py': pin(source)['sha256'],
        'FROZEN_LINK_MAP.json': pin(r0 / 'FROZEN_LINK_MAP.json')['sha256']})
    ck(frozen == expected and manifest_rows(r0 / 'AUTHOR_MANIFEST.sha256') == author,
       'Round0 exact493 payloads and489 original author roles')
    for name, digest in author.items():
        full_compare(PAPER / name, r0 / name, 'R0_author_payload', digest)
    for name in ('AUTHOR_MANIFEST.sha256', 'ROOT_ADOPTION.md'):
        full_compare(PAPER / name, r0 / name, 'R0_extra_original')
    full_compare(source, r0 / 'FREEZE_ADAPTER.py', 'R0_executed_source')
    old = obj(r0 / 'FROZEN_LINK_MAP.json')
    archive = obj(PAPER / 'sources/ARCHIVE_INPUTS.actual.json')
    ck(archive['count'] == len(archive['records']) == 19, 'all19 original archived source rows')
    origins, external = {}, {}
    for row in archive['records']:
        full_compare(PAPER / row['copy'], row['original'], 'R0_archive_original')
        pin(row['original'], row['sha256'])
        origins[row['copy']] = row['original']
        external[row['original']] = row['sha256']
    for prefix in ('author_produce_01', 'author_pair_01', 'author_pair_02'):
        name = prefix + '/source/SOURCE_AUDIT.md'
        full_compare(PAPER / name, PAPER / 'SOURCE_AUDIT.md', 'R0_exact_capsule_origin')
        origins[name] = str(PAPER / 'SOURCE_AUDIT.md')
    for name, original in {
        'sources/archive/CRG_SCOUT.md': 'docs/papers162_166_sequence/scouting/replacement_crossclass/SCOUT.md',
        'sources/archive/FPT_LEDGER.md': 'docs/papers182_186_sequence/scouting/combinatorial_lane/SCOUT_AND_KILL_LEDGER.md',
        'sources/archive/PDCF_CANDIDATES.md': 'docs/papers187_191_sequence/scouting/combinatorial_lane/CANDIDATES.md'}.items():
        ck(origins[name].endswith('/inputs/originals/' + original), 'exact three recorded workspace origins')
        origins[name] = str(ROOT / original)
    ck(origins == old['exact_document_origin_roles'], 'entire recorded original document origin map')
    links = []
    for name in sorted(expected):
        if not name.endswith('.md'):
            continue
        origin = Path(origins.get(name, str(PAPER / name)))
        for href in original_hrefs(r0 / name):
            candidate = (origin.parent / unquote(href.split('#', 1)[0])).resolve()
            if candidate == PAPER / 'SHA256SUMS':
                target, digest, mode = r0 / 'AUTHOR_MANIFEST.sha256', AUTHOR_SEAL, 'exact-author-seal-alias'
            elif candidate.is_relative_to(PAPER) and candidate.relative_to(PAPER).as_posix() in expected:
                relative = candidate.relative_to(PAPER).as_posix()
                target, digest, mode = r0 / relative, expected[relative], 'physical-copied-input'
            else:
                ck(str(candidate) in old['external_input_pins'], 'only declared R0 exact external link role')
                target, digest, mode = candidate, old['external_input_pins'][str(candidate)], 'external-exact-original-origin'
                external[str(candidate)] = digest
            links.append(dict(document=name, document_sha256=expected[name], exact_markdown_origin=str(origin),
                href=href, mode=mode, physical_target=str(target), sha256=digest))
            historic_hash_path(target, digest)
    ck(links == old['links'] and len(links) == 57 and external == old['external_input_pins'] and
       len(external) == 33 and old['historical_author_manifest_sha256'] == AUTHOR_SEAL and
       old['author_payloads'] == 489 and old['copied_input_count'] == 491 and
       old['freezer_origin'] == str(source) and old['freezer_sha256'] == pin(source)['sha256'],
       'Round0 complete exact57 links33 external and physical source')
    for path, digest in old['prerequisite_pins'].items():
        historic_hash_path(path, digest)
    launch = obj(QA / 'P210_ROUND0_FREEZE_LAUNCH.actual.json')
    ck(launch['exit_code'] == 0 and launch['cwd'] == str(ROOT) and
       shlex.split(launch['command']) == ['/usr/bin/python3.10', '-I', '-S', '-B', str(source)],
       'actual Round0 freezer parent original native')
    actual = json.loads(launch['output'])
    ck(actual['status'] == 'PASS_PHYSICAL_P210_ROUND0' and actual['manifest_sha256'] == R0_SEAL and
       actual['payloads'] == 493 and actual['links'] == 57 and actual['external_paths'] == 33,
       'actual Round0 output not a newer invented freeze')
    pairs = [(PAPER / 'SHA256SUMS', PAPER / 'AUTHOR_MANIFEST.sha256'),
             (PAPER / 'AUTHOR_MANIFEST.sha256', r0 / 'AUTHOR_MANIFEST.sha256'),
             (PAPER / 'main.pdf', r0 / 'main.pdf')]
    expected_cmp = [{'argv': ['/usr/bin/cmp', '--', str(left), str(right)], 'cwd': str(ROOT),
                     'environment': ENV, 'exit_code': 0, 'stdout': '', 'stderr': ''} for left, right in pairs]
    ck(actual['raw_comparisons'] == expected_cmp, 'all three actual Round0 freezer native raw comparisons')
    completion = obj(QA / 'P210_ROUND0_ROOT_CLOSURE_COMPLETION.actual.json')
    root = json.loads(completion['output'])
    ck(completion['session_id'] == 99187 and completion['exit_code'] == 0 and
       root['status'] == 'PASS_ROOT_PHYSICAL_P210_ROUND0_CLOSURE' and root['current_paths_reread'] == 1022 and
       root['manifest_sha256'] == R0_SEAL and root['author_payloads'] == 489 and root['frozen_payloads'] == 493,
       'actual Round0 root full original closure; absent full map not manufactured')
    checksum = []
    for base, name, rows in ((r0, 'SHA256SUMS', frozen), (PAPER, 'AUTHOR_MANIFEST.sha256', author),
                             (r0, 'AUTHOR_MANIFEST.sha256', author)):
        checksum.append({'argv': ['/usr/bin/sha256sum', '-c', name], 'cwd': str(base), 'environment': ENV,
                         'exit_code': 0, 'stdout': ''.join(n + ': OK\n' for n in rows), 'stderr': ''})
    ck(root['native_commands'] == checksum + expected_cmp, 'entire six original Round0 root native outputs')
    NATIVE_RECORDS.extend({'kind': 'old_R0_native', **row} for row in actual['raw_comparisons'] + root['native_commands'])
    return frozen, old


def round_anchor_roles(number, binding=None):
    if number == 1:
        return dict(zip(('ROUND0_CORE_MANIFEST.sha256', 'A_REVIEW_MANIFEST.sha256', 'A_DELTA.md',
            'A_INITIAL_FINDINGS.json', 'A_CURRENT_FINDINGS.json', 'A_INPUT_PINS.sha256', 'ROOT_RESPONSE.md',
            'ROOT_DELTA_CLOSURE.actual.json', 'ROOT_PAIR_MANIFEST.sha256', 'PRE_ROUND1_PAPER_MANIFEST.sha256',
            'PRE_ROUND1_ROOT_LIFECYCLE.md', 'A_INITIAL_REVIEW_MANIFEST.sha256', 'A_INITIAL_DELTA.md'), map(str, (
            PAPER / 'frozen_round0/SHA256SUMS', A / 'SHA256SUMS', A / 'DELTA.md', A / 'FINDINGS.json',
            A / 'CURRENT_FINDINGS.json', A / 'INPUT_PINS.sha256', QA.parent / 'P210_A_RESPONSE.md',
            QA / 'P210_A_ROOT_DELTA_INSPECTION.actual.json', QA / 'root_replays/p210_a_strict_pair_01/SHA256SUMS',
            PAPER / 'PAPER_MANIFEST.sha256', PAPER / 'ROOT_LIFECYCLE.md',
            A / 'history/initial_before_delta/SHA256SUMS', A / 'history/initial_before_delta/DELTA.md'))))
    names = dict(zip(('round1_manifest', 'review_manifest', 'accepted_delta', 'initial_findings',
        'current_findings', 'review_input_pins', 'response', 'root_final_closure', 'root_pair_manifest',
        'prior_whole_manifest', 'prior_lifecycle', 'initial_review_manifest', 'initial_delta'),
        ('ROUND1_CORE_MANIFEST.sha256', 'B_REVIEW_MANIFEST.sha256', 'B_ACCEPTED_DELTA.md', 'B_INITIAL_FINDINGS.json',
         'B_CURRENT_FINDINGS.json', 'B_INPUT_PINS.sha256', 'ROOT_B_RESPONSE.md', 'ROOT_B_FINAL_CLOSURE.json',
         'ROOT_B_PAIR_MANIFEST.sha256', 'PRE_ROUND2_PAPER_MANIFEST.sha256', 'PRE_ROUND2_ROOT_LIFECYCLE.md',
         'B_INITIAL_REVIEW_MANIFEST.sha256', 'B_INITIAL_DELTA.md')))
    ck(set(binding['roles']) == set(names) and len(binding['selectors']) == 26 and
       binding['schema'] == 'p210-round2-actual-final-b-binding-v1' and binding['bound_by'] == '/root' and
       binding['status'] == 'BOUND_AFTER_ACTUAL_B_ACCEPTANCE_AND_ROOT_FINAL_CLOSURE', 'actual exact final B binding')
    result = {name: binding['roles'][role]['path'] for role, name in names.items()}
    for role in binding['roles'].values():
        path = historic_hash_path(role['path'], role['sha256'])
        pin(path, {'sha256': role['sha256'], 'bytes': role['bytes']})
    return result, names


def successive_round_links(number, core, provenance, prior_links, anchors, binding=None, role_names=None):
    previous, target = PAPER / ('frozen_round' + str(number - 1)), PAPER / ('frozen_round' + str(number))
    ck(Counter((name, href) for name in core if name.endswith('.md') for href in original_hrefs(previous / name)) ==
       Counter((row['document'], row['href']) for row in prior_links), 'entire inherited link occurrence census')
    moved = []
    for row in prior_links:
        old = Path(row['physical_target'])
        inside = old.is_relative_to(previous)
        physical_target = target / old.relative_to(previous) if inside else old
        historic_hash_path(old, row['sha256'])
        if number == 1:
            moved.append({**row, 'round0_physical_target': str(old), 'physical_target': str(physical_target),
                          'round1_mode': 'physical-unchanged-core-copy' if inside else 'unchanged-exact-external-original'})
        else:
            moved.append(dict(document=row['document'], document_sha256=core[row['document']], href=row['href'],
                round1_physical_target=str(old), physical_target=str(physical_target), sha256=row['sha256'],
                mode='physical-unchanged-Round1-copy' if inside else 'unchanged-exact-external-role', previous_role=row))
    map_name = 'round1_core_link_map' if number == 1 else 'round2_historical_link_map'
    ck(moved == provenance[map_name], 'exact full previous-role migration never prefix alias')
    origins = {(str(previous / name), value): target / name for name, value in core.items()}
    for name, value in core.items():
        if (PAPER / name).is_file():
            historic_hash_path(PAPER / name, value)
            origins[(str(PAPER / name), value)] = target / name
    origins[(str(PAPER / 'SHA256SUMS'), AUTHOR_SEAL)] = target / 'AUTHOR_MANIFEST.sha256'
    for role in provenance['anchors'].values():
        origins[(role['original_path'], role['sha256'])] = target / role['physical_path']
    if number == 1:
        docs = [(name, source, str(A / 'DELTA.md') if name == 'A_INITIAL_DELTA.md' else source)
                for name, source in anchors.items() if name.endswith('.md')]
    else:
        docs = [(role_names[role], binding['roles'][role]['path'], origin)
                for role, origin in binding['markdown_origins'].items()]
    added = []
    for name, source, origin in docs:
        source_sha = provenance['anchors'][name]['sha256']
        actual_source = historic_hash_path(source, source_sha)
        for href in original_hrefs(actual_source):
            original = (Path(origin).parent / unquote(href.split('#', 1)[0])).resolve()
            # Link targets may reference a historical lifecycle or review seal.
            # The stored role selects a hash, but its source/origin/href/target
            # tuple must independently match before that exact alias is used.
            candidates = [row for row in provenance['acceptance_anchor_link_map'] if
                row['document'] == 'ROUND' + str(number) + '_ACCEPTANCE/' + name and
                row['href'] == href and row['original_target'] == str(original)]
            ck(candidates and len({row['sha256'] for row in candidates}) == 1, 'one exact original anchor-link key')
            digest = candidates[0]['sha256']
            historic_hash_path(original, digest)
            physical_target = origins.get((str(original), digest), original)
            mode = ('explicit-core-or-anchor' if number == 1 else 'explicit-current-core-or-anchor') if physical_target != original else 'exact-current-original-document-origin'
            added.append(dict(document='ROUND' + str(number) + '_ACCEPTANCE/' + name,
                source_bytes_path=source, original_document=origin, href=href, original_target=str(original),
                physical_target=str(physical_target), sha256=digest, mode=mode))
    ck(added == provenance['acceptance_anchor_link_map'] and len(added) == {1: 14, 2: 15}[number],
       'entire actual new acceptance-anchor link map')
    all_links = moved + added
    ck(Counter((name, href) for name in physical(target) if name.endswith('.md') for href in original_hrefs(target / name)) ==
       Counter((row['document'], row['href']) for row in all_links), 'complete final frozen Markdown link occurrence map')
    for row in all_links:
        historic_hash_path(row['physical_target'], row['sha256'])
    return all_links


def successive_round(number, core, prior_links, old_external, reviews):
    r = PAPER / ('frozen_round' + str(number))
    previous = PAPER / ('frozen_round' + str(number - 1))
    seal, count, previous_count, old_count = (R1_SEAL, 508, 493, 987) if number == 1 else (R2_SEAL, 524, 508, 1496)
    prefix = 'P210_ROUND' + str(number)
    prep = QA / ('p210_round' + str(number) + '_preparation')
    frozen = complete_package(r, seal, count)
    prov = obj(r / ('ROUND' + str(number) + '_PROVENANCE.json'))
    ck(prov['schema'] == 'p210-round' + str(number) + '-provenance-v1' and prov['core_payload_pins'] == core and
       prov['author_payloads_preserved'] == 489 and prov['round' + str(number - 1) + '_core_payloads_copied'] == previous_count and
       prov['acceptance_anchor_payloads'] == 12 + number, 'actual exact Round core and anchor census')
    binding, role_names = None, None
    if number == 1:
        anchors = round_anchor_roles(1)
        ck(prov['accepted_root_assertions'] == reviews['a']['root'] and prov['round0_external_aliases'] == [],
           'actual accepted A assertions and no global alias')
    else:
        binding = prov['actual_final_b_binding']
        anchors, role_names = round_anchor_roles(2, binding)
        anchors['FINAL_B_BINDING.json'] = str(QA / 'p210_round2_binding/FINAL_B_BINDING.json')
        ck(obj(anchors['FINAL_B_BINDING.json']) == binding and prov['actual_final_b_binding_sha256'] ==
           pin(anchors['FINAL_B_BINDING.json'])['sha256'] and prov['round1_external_aliases'] == [],
           'actual final B binding source identity and no generic alias')
    ck(set(anchors) == set(prov['anchors']), 'only named original acceptance anchors')
    expected = dict(core)
    for name, digest in core.items():
        ck(frozen[name] == digest, 'unchanged complete preceding physical core')
        full_compare(previous / name, r / name, 'R' + str(number) + '_core')
    for name, source in anchors.items():
        row = prov['anchors'][name]
        ck(row['original_path'] == source and row['physical_path'] == 'ROUND' + str(number) + '_ACCEPTANCE/' + name,
           'exact accepted anchor logical and physical identities')
        full_compare(source, r / row['physical_path'], 'R' + str(number) + '_anchor', row['sha256'])
        expected[row['physical_path']] = row['sha256']
    source = prep / ('freeze_p210_round' + str(number) + '.py')
    copied = 'ROUND' + str(number) + '_FREEZE_ADAPTER.py'
    full_compare(source, r / copied, 'R' + str(number) + '_source')
    expected[copied] = pin(source)['sha256']
    expected['ROUND' + str(number) + '_PROVENANCE.json'] = pin(r / ('ROUND' + str(number) + '_PROVENANCE.json'))['sha256']
    ck(frozen == expected and prov['freezer_sha256'] == expected[copied], 'entire final physical freeze layout')
    ck(prov['round0_external_original_pins'] == old_external and len(old_external) == 33,
       'all original33 external key roles retained')
    links = successive_round_links(number, core, prov, prior_links, anchors, binding, role_names)
    for path, digest in prov['accepted_review_and_root_manifest_referents'].items():
        historic_hash_path(path, digest)
    bind_full_base(prov['full_source_input_pins_before_and_reread_after'], {1: 1653, 2: 2077}[number],
                   'R' + str(number) + '_full_actual_freezer_map', False)
    comparisons = prov['raw_byte_comparisons']
    ck(type(comparisons) is list and len(comparisons) == {1: 1000, 2: 1016}[number],
       'actual freezer comparison field is full record list not an integer')
    for row in comparisons:
        ck(set(row) == {'bytes', 'equal', 'left', 'method', 'right', 'role'} and row['equal'] is True and
           row['method'] == 'complete Python bytes comparison; not a native cmp command' and
           type(row['bytes']) is int and row['bytes'] >= 0 and type(row['role']) is str and row['role'],
           'every original freezer complete comparison row schema')
        values = []
        for side in ('left', 'right'):
            logical = row[side]
            ck(Path(logical).is_absolute(), 'actual comparison operand absolute path')
            original = prov['full_source_input_pins_before_and_reread_after'].get(logical)
            ck(original is not None or (Path(logical).is_relative_to(r) and
               Path(logical).relative_to(r).as_posix() in frozen), 'every non-source-map operand is an exact sealed frozen copy')
            selected = historical_record(logical, original)[0] if original is not None else logical
            values.append(raw(selected))
        ck(values[0] == values[1] and len(values[0]) == row['bytes'],
           'every full actual1000-or1016 raw comparison rechecked with exact history')
        BYTE_COMPARISONS['R' + str(number) + '_all_original_freezer_comparisons'] += 1
    old = manifest_rows(r / ('ROUND' + str(number) + '_ACCEPTANCE/PRE_ROUND' + str(number) + '_PAPER_MANIFEST.sha256'))
    ck(len(old) == old_count and old == prov['prior_whole_manifest']['original_referent_pins'] and
       prov['prior_whole_manifest']['complete_before_creation_only'] is True and
       prov['prior_whole_manifest']['current_whole_manifest_after_creation'] is False,
       'old whole manifest is exact prior scope never current terminal membership')
    for name, digest in old.items():
        historic_hash_path(PAPER / name, digest)
    freeze = original_native_summary(prefix + '_ROOT_FREEZE_LAUNCH.actual.json',
        prefix + '_ROOT_FREEZE_COMPLETION.actual.json', {1: 67481, 2: 6427}[number])
    ck(freeze['status'] == 'PASS_PHYSICAL_P210_ROUND' + str(number) and freeze['payloads'] == count and
       freeze['physical_files'] == count + 1 and freeze['manifest_sha256'] == seal and
       freeze['freezer_sha256'] == expected[copied] and
       freeze['complete_raw_byte_comparisons'] == len(comparisons), 'actual completed freezer native parent')
    launch = obj(QA / (prefix + '_ROOT_FREEZE_LAUNCH.actual.json'))
    ck(launch['cwd'] == prov['cwd'] == str(ROOT) and prov['environment'] == ENV and
       shlex.split(launch['command']) == ['/usr/bin/env', '-i',
       *[key + '=' + value for key, value in ENV.items()], *prov['launch_orig_argv']] and
       prov['launch_orig_argv'][:7] == ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
       'pycache_prefix=' + str(r / 'never_created_freezer_cache'), str(source)] and
       prov['launch_argv'] == prov['launch_orig_argv'][6:] and
       not os.path.lexists(r / 'never_created_freezer_cache'), 'entire actual freezer native source argv ENV4')
    reception = QA / ('p210_round' + str(number) + '_root_reception')
    receipt = obj(reception / 'ROOT_RECEPTION.json')
    root = original_native_summary(prefix + '_ROOT_INSPECTION_LAUNCH.actual.json',
        prefix + '_ROOT_INSPECTION_COMPLETION.actual.json', {1: 81319, 2: 34834}[number])
    ck(root['status'] == receipt['status'] == 'PASS_ROOT_PHYSICAL_P210_ROUND' + str(number) + '_RECEPTION' and
       receipt['checks'] == root['checks'] == {1: 29273, 2: 38968}[number] and
       receipt['current_input_count'] == root['current_input_count'] == {1: 2164, 2: 2603}[number] and
       receipt['full_raw_copy_comparisons'] == previous_count + 13 + number and
       receipt['core_links'] == {1: 57, 2: 71}[number] and receipt['anchor_links'] == 13 + number and
       receipt['current_open_findings'] == 0, 'entire actual separate root physical reception census')
    complete_package(reception, root['root_reception_manifest_sha256'], 1)
    bind_full_base(receipt['complete_input_pins'], {1: 2164, 2: 2603}[number], 'R' + str(number) + '_full_actual_root_map', False)
    reviewer = A if number == 1 else B
    pair = QA / ('root_replays/p210_' + ('a' if number == 1 else 'b') + '_strict_pair_01')
    ck(len(receipt['actual_native_commands']) == root['native_commands_all_zero'] == 6,
       'six actual commands retained not reexecuted')
    for row, base in zip(receipt['actual_native_commands'][:5], (previous, r, reviewer, pair, prep)):
        recorded_manifest_native(row, manifest_rows(base / 'SHA256SUMS'), base)
    cmp_row = receipt['actual_native_commands'][5]
    ck(cmp_row == dict(argv=['/usr/bin/cmp', str(r / 'AUTHOR_MANIFEST.sha256'), str(PAPER / 'AUTHOR_MANIFEST.sha256')],
        cwd=str(ROOT), environment=ENV, exit=0, stdout_utf8='', stderr_utf8='',
        stdout_sha256=sha256(b'').hexdigest(), stderr_sha256=sha256(b'').hexdigest()), 'complete actual author-seal native comparison')
    NATIVE_RECORDS.append({'kind': 'old_round_native_raw_comparison', **cmp_row})
    return frozen, links


def actual_round2_lifecycle_refresh():
    old_base = PAPER / 'frozen_round2/ROUND2_ACCEPTANCE'
    preserved = QA / 'p210_preterminal_controls_01'
    old_whole = manifest_rows(old_base / 'PRE_ROUND2_PAPER_MANIFEST.sha256')
    new_whole = manifest_rows(preserved / 'PAPER_MANIFEST.sha256')
    ck(len(old_whole) == 1496 and len(new_whole) == 2021 and set(old_whole) <= set(new_whole) and
       {name for name in old_whole if old_whole[name] != new_whole[name]} == {'ROOT_LIFECYCLE.md'} and
       set(new_whole) - set(old_whole) == {'frozen_round2/' + name for name in physical(PAPER / 'frozen_round2')},
       'exact actual R2 document-only transition all525 new frozen files and single old-life change')
    for name, digest in new_whole.items():
        historic_hash_path(PAPER / name, digest)
    receipt = obj(QA / 'P210_ROUND2_LIFECYCLE_REFRESH.actual.json')
    summary = original_native_summary('P210_ROUND2_LIFECYCLE_REFRESH_ROOT_LAUNCH.actual.json',
        'P210_ROUND2_LIFECYCLE_REFRESH_ROOT_COMPLETION.actual.json', 42389)
    ck({k: v for k, v in receipt.items() if k != 'native'} == summary and
       summary['status'] == 'PASS_P210_ROUND2_LIFECYCLE_AND_WHOLE_MANIFEST_REFRESH' and
       summary['current_payloads'] == 2021 and summary['old_payloads'] == 1496 and
       summary['physical_files'] == 2022 and summary['added_round2_files'] == 525 and
       summary['sole_changed_old_payload'] == 'ROOT_LIFECYCLE.md' and
       summary['old_lifecycle_sha256'] == pin(old_base / 'PRE_ROUND2_ROOT_LIFECYCLE.md')['sha256'] and
       summary['old_whole_sha256'] == pin(old_base / 'PRE_ROUND2_PAPER_MANIFEST.sha256')['sha256'] and
       summary['new_lifecycle_sha256'] == pin(preserved / 'ROOT_LIFECYCLE.md')['sha256'] and
       summary['new_whole_sha256'] == pin(preserved / 'PAPER_MANIFEST.sha256')['sha256'] and
       summary['round2_sha256'] == R2_SEAL, 'actual original lifecycle receipt not current terminal scope')
    pin(QA / 'refresh_p210_round2_whole_manifest.py', summary['source_sha256'])
    native = receipt['native']
    ck(native == dict(argv=['/usr/bin/sha256sum', '--check', 'PAPER_MANIFEST.sha256'], cwd=str(PAPER),
       environment=ENV, exit=0, stdout=''.join(name + ': OK\n' for name in new_whole), stderr=''),
       'whole actual2021-line checksum native stdout and actual ENV4')
    NATIVE_RECORDS.append({'kind': 'old_R2_lifecycle_native', **native})
    return {'prior_payloads': 1496, 'new_payloads_at_actual_R2_transition': 2021,
            'added_frozen_payloads_and_seal': 525, 'sole_changed_old_payload': 'ROOT_LIFECYCLE.md',
            'current_whole_membership_claim': False}


# Terminal-only record schemas differ from strict replay schemas above.
# These selection/record checks are a disclosed textual adaptation of the
# fully read P210 terminal receiver preparation; neither it nor a builder is
# imported or executed. Actual source/seal/native binding is supplied last.
TERM_ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC',
            'SOURCE_DATE_EPOCH': '1704067200', 'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'}
TERM_TOOLS = {Path('/usr/bin') / name for name in ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo',
              'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp', 'env', 'python3.10')} | {Path('/bin/bash'), Path('/bin/sh')}
TERM_TEX_ROOTS = tuple(map(Path, ('/usr/share/texlive/texmf-dist', '/usr/share/texmf', '/var/lib/texmf', '/etc/texmf',
    '/usr/local/share/texmf', '/root/texmf', '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')))
TERM_CONFIG_ROOTS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/share/fonts', '/etc/fonts', '/var/cache/fontconfig',
    '/usr/share/fontconfig', '/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv',
    '/usr/share/poppler', '/usr/local/share/fonts', '/etc/xdg/fontconfig', '/etc/profile.d', '/root/.fonts',
    '/root/.fontconfig', '/root/.fonts.conf.d', '/root/.config/fontconfig', '/root/.cache/fontconfig', '/root/.local/share/fonts')))
TERM_SOURCE_NAMES = ('main.tex', 'math_commands.tex', 'references.bib', 'sections/0_abstract.tex',
    'sections/1_introduction.tex', 'sections/2_clock.tex', 'sections/3_image.tex', 'sections/4_coding.tex',
    'sections/5_fibres.tex', 'sections/6_scope.tex')
TERM_USER_VARS = ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR')
TERM_NONFILES = {}


def terminal_entry(path):
    p = Path(path)
    row = dict(exists=p.exists(), symlink=p.is_symlink(), link=os.readlink(p) if p.is_symlink() else None,
               resolved=str(p.resolve()), is_file=p.is_file(), is_dir=p.is_dir())
    if row['is_file']:
        row.update(val(p))
    else:
        ck(str(p) not in TERM_NONFILES or TERM_NONFILES[str(p)] == row, 'terminal nonfile presence/link stability')
        TERM_NONFILES[str(p)] = row
    return row


def terminal_ledger(directory, phase):
    path = directory / ('KNOWN_INPUTS_' + phase + '.json.gz')
    compressed = raw(path)
    body = gzip.decompress(compressed)
    data = json.loads(body)
    ck(body.endswith(b'\n') and compressed[:4] == b'\x1f\x8b\x08\x00' and compressed[4:8] == b'\x00' * 4,
       'entire lossless terminal ledger gzip header and JSON newline')
    ck(obj(str(path) + '.meta.json') == dict(encoding='gzip of exact UTF-8 JSON with terminal LF; mtime=0',
       json_bytes=len(body), json_sha256=sha256(body).hexdigest(), compressed=val(path),
       semantic_groups={name: len(group) for name, group in data.items()}), 'entire terminal gzip sidecar')
    return data, {'bytes': len(body), 'sha256': sha256(body).hexdigest()}


def terminal_membership(snapshot):
    std = {STDLIB}
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [name for name in folders if name not in {'site-packages', 'dist-packages', '__pycache__'}]
        std.update(Path(directory) / name for name in files if not name.endswith(('.pyc', '.pyo')))
    runtime = std | TERM_TOOLS | set(LIB_ROOTS)
    for base in LIB_ROOTS:
        paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        runtime.update(p for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    groups = {'runtime': {str(p) for p in runtime}}
    for name, roots in (('tex', TERM_TEX_ROOTS), ('configuration', TERM_CONFIG_ROOTS)):
        selected = set(roots)
        for base in roots:
            if base.is_dir():
                selected.update(base.rglob('*'))
        if name == 'configuration':
            selected.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
                '/etc/locale.conf', '/etc/default/locale', '/etc/nsswitch.conf', '/etc/localtime',
                '/etc/bash.bashrc', '/etc/profile', '/etc/passwd', '/etc/group', '/etc/fonts/local.conf',
                '/usr/lib/locale/locale-archive', '/root/.fonts.conf', '/root/.config/fontconfig/fonts.conf',
                '/usr/lib/python310.zip', '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg')))
            for base in (Path('/usr/bin'), Path('/usr/lib')):
                selected.update(base / child for child in ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
            selected.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
            for key in ('LDLIBRARY', 'INSTSONAME'):
                value = sysconfig.get_config_var(key)
                if value:
                    selected.add(STDLIB.parent / (value + '._pth'))
            body = raw('/usr/bin/ldd').decode()
            match = re.search(r'^RTLDLIST="([^"]+)"', body, re.M)
            ck(body.startswith('#!/bin/bash\n') and match is not None, 'terminal original ldd loader list rule')
            selected.update(map(Path, match.group(1).split()))
        groups[name] = {str(p) for p in selected}
    ck(set(snapshot) == set(groups) and all(set(snapshot[name]) == values for name, values in groups.items()),
       'exact source-defined current terminal candidate membership including absent fixed children')
    return {name: len(values) for name, values in groups.items()}


def terminal_commands(out, prep, paper):
    commands = {}
    def add(label, argv, cwd, direct=(), mutable=()):
        commands[label] = (list(map(str, argv)), str(cwd), {str(argv[0]), *map(str, direct)}, set(map(str, mutable)))
    add('source_cmp', ['/usr/bin/cmp', '--', prep / 'build_p210.py', out / 'executed_source.py'], out,
        [prep / 'build_p210.py', out / 'executed_source.py'])
    elf = sorted(str(p) for p in TERM_TOOLS | set((STDLIB / 'lib-dynload').glob('*.so')) if raw(p)[:4] == b'\x7fELF')
    add('ldd_before', ['/usr/bin/ldd', *elf], out, elf)
    for tool in ('pdflatex', 'bibtex'):
        add(tool + '_version', ['/usr/bin/' + tool, '--version'], out)
    add('texmf_roots', ['/usr/bin/kpsewhich', '-var-value=TEXMF'], out)
    frozen_pdf = Path(paper['freeze']) / 'main.pdf'
    add('P210_round2_pdfinfo', ['/usr/bin/pdfinfo', frozen_pdf], out, [frozen_pdf])
    for number in (1, 2):
        label = 'P210_cold_build_' + str(number)
        cold = out / ('cold_build_' + str(number))
        pdf = cold / 'main.pdf'
        for variable in TERM_USER_VARS:
            add(label + '_' + variable, ['/usr/bin/kpsewhich', '-var-value=' + variable], cold)
        for n in (1, 2, 3):
            add(label + '_pass' + str(n), ['/usr/bin/pdflatex', '-no-shell-escape', '-recorder',
                '-interaction=nonstopmode', '-halt-on-error', 'main.tex'], cold,
                [cold / name for name in paper['source_names']], [cold / ('main.' + s) for s in ('aux', 'bbl', 'out', 'toc')])
            if n == 1:
                add(label + '_bst', ['/usr/bin/kpsewhich', 'plainnat.bst'], cold)
                bst = Path(raw(out / 'commands' / (label + '_bst') / 'stdout').decode().strip()).resolve()
                add(label + '_bibtex', ['/usr/bin/bibtex', 'main'], cold, [cold / 'main.aux', cold / 'references.bib', bst])
        for tool in ('pdfinfo', 'pdffonts'):
            add(label + '_' + tool, ['/usr/bin/' + tool, 'main.pdf'], cold, [pdf])
        add(label + '_pdftotext', ['/usr/bin/pdftotext', '-layout', 'main.pdf', out / (label + '.txt')], cold, [pdf])
        add(label + '_frozen_cmp', ['/usr/bin/cmp', '--', pdf, frozen_pdf], cold, [pdf, frozen_pdf])
        if number == 1:
            add(label + '_render', ['/usr/bin/pdftoppm', '-png', '-r', '105', 'main.pdf', cold / 'pages/page'], cold, [pdf])
    pair = [out / ('cold_build_' + str(n)) / 'main.pdf' for n in (1, 2)]
    add('P210_pair_cmp', ['/usr/bin/cmp', '--', *pair], out, pair)
    add('ldd_after', ['/usr/bin/ldd', *elf], out, elf)
    return commands


def terminal_native_records(out, result, expected):
    ck(result['expected_command_count'] == len(expected) == 33 and result['expected_command_labels'] == list(expected) and
       [row['label'] for row in result['commands']] == list(expected) and
       {p.name for p in (out / 'commands').iterdir()} == set(expected), 'all33 actual terminal commands exact order/directories')
    rows, previous, pids = {}, 0, set()
    attempt_keys = {'label', 'argv', 'cwd', 'env', 'started_epoch', 'timeout_seconds', 'start_new_session',
                    'exit_code', 'status', 'inputs_before', 'generated_inputs_before'}
    receipt_keys = attempt_keys | {'pid', 'ended_epoch', 'error', 'streams_settled', 'inputs_after',
                                   'generated_inputs_after', 'streams'}
    for row in result['commands']:
        label = row['label']
        directory = out / 'commands' / label
        attempt, receipt = obj(directory / 'ATTEMPT.json'), obj(directory / 'RECEIPT.json')
        argv, cwd, direct, mutable = expected[label]
        ck(receipt == row and set(attempt) == attempt_keys and set(receipt) == receipt_keys and
           {k: v for k, v in attempt.items() if k not in {'status', 'exit_code'}} ==
           {k: row[k] for k in attempt if k not in {'status', 'exit_code'}}, 'complete native attempt/result/receipt schema')
        ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and row['status'] == 'COMPLETED' and
           type(row['exit_code']) is int and row['exit_code'] == 0 and row['error'] is None and row['streams_settled'] is True,
           'actual settled native command exit no old failed/cleanup field suppressed')
        ck(row['argv'] == argv and row['cwd'] == cwd and row['env'] == TERM_ENV and row['timeout_seconds'] == 600 and
           row['start_new_session'] is True and type(row['pid']) is int and row['pid'] > 0 and
           previous <= row['started_epoch'] <= row['ended_epoch'] and
           row['ended_epoch'] - row['started_epoch'] <= 600, 'entire actual terminal argv ENV process and chronology')
        previous = row['ended_epoch']
        pids.add(row['pid'])
        ck(set(row['inputs_before']) == direct and row['inputs_before'] == row['inputs_after'] and
           set(row['generated_inputs_before']) == set(row['generated_inputs_after']) == mutable,
           'complete original immutable and mutable native input roles')
        for name, value in row['inputs_before'].items():
            path = out / (label[:-7] + '_pass1.aux') if label.endswith('_bibtex') and name == str(Path(cwd) / 'main.aux') else Path(name)
            pin(path, sha_record(value))
        ck(set(row['streams']) == {'stdout', 'stderr'}, 'both actual terminal stream pins')
        for stream in ('stdout', 'stderr'):
            pin(directory / stream, sha_record(row['streams'][stream]))
            raw(directory / stream)
        if argv[0] == '/usr/bin/cmp':
            ck(raw(directory / 'stdout') == raw(directory / 'stderr') == b'', 'entire actual native cmp streams empty')
            full_compare(argv[2], argv[3], 'terminal_native_raw_operands')
        ck(physical(directory) == {'ATTEMPT.json', 'RECEIPT.json', 'stdout', 'stderr'}, 'complete closed native record membership')
        NATIVE_RECORDS.append({'kind': 'old_terminal_native', 'label': label, 'argv': argv})
        rows[label] = row
    ck(len(pids) == 33, 'all33 actual child PIDs distinct')
    return rows


def terminal_build_records(out, number, paper, rows, known):
    label = 'P210_cold_build_' + str(number)
    cold = out / ('cold_build_' + str(number))
    initial = obj(out / (label + '_SOURCE_ONLY_INITIAL.json'))
    ck(initial == paper['source_pins'] and tuple(paper['source_names']) == TERM_SOURCE_NAMES and
       set(initial) == set(TERM_SOURCE_NAMES), 'actual ten source-only initial roles no generated input')
    for name, value in initial.items():
        pin(cold / name, sha_record(value))
        full_compare(cold / name, Path(paper['freeze']) / name, 'terminal_source_only_copy')
    consumed, bookmarks, previous = {}, [], None
    for n in (1, 2, 3):
        stem = label + '_pass' + str(n)
        before, after = rows[stem]['generated_inputs_before'], rows[stem]['generated_inputs_after']
        for path in before:
            suffix = Path(path).suffix
            for moment, record in (('before', before[path]), ('after', after[path])):
                base = dict(exists=record['is_file'], symlink=False, link=None, resolved=path,
                            is_file=record['is_file'], is_dir=False)
                ck(type(record['is_file']) is bool and record == {**base,
                   **({k: record[k] for k in ('sha256', 'bytes')} if record['is_file'] else {})},
                   'entire original generated auxiliary-state schema')
                if record['is_file']:
                    value = sha_record({k: record[k] for k in ('sha256', 'bytes')})
                    if suffix == '.aux':
                        saved_pass = n if moment == 'after' else n - 1
                        ck(saved_pass >= 1, 'actual saved aux pass exists')
                        pin(out / (label + '_pass' + str(saved_pass) + '.aux'), value)
                    elif suffix == '.bbl':
                        pin(out / (label + '.bbl'), value)
                    elif suffix == '.out' and value != val(cold / 'main.out'):
                        ck((n, moment) in {(1, 'after'), (2, 'before')}, 'only actual first-pass bookmark historical hash role')
                        bookmarks.append(dict(command=stem, moment=moment, path=path, **value))
                    else:
                        pin(path, value)
            if n == 1:
                ck(before[path]['exists'] is False, 'cold first pass has no aux/bbl/out/toc input')
            elif suffix == '.bbl' and n == 2:
                ck(before[path]['is_file'] and before[path] == after[path], 'actual BibTeX insertion then unchanged bibliography')
            else:
                ck(before[path] == previous[path], 'entire original auxiliary succession')
        previous = after
        recorded = obj(out / (stem + '_INPUTS.json'))
        expected = {'local': {}, 'external': {}}
        for line in raw(out / (stem + '.fls')).decode().splitlines():
            if not line.startswith('INPUT '):
                continue
            path = Path(line[6:])
            path = (path if path.is_absolute() else cold / path).resolve()
            if path.is_relative_to(cold):
                name = path.relative_to(cold).as_posix()
                if name in initial:
                    value = initial[name]
                else:
                    ck(path.suffix in {'.aux', '.bbl', '.out', '.toc'} and str(path) in after and
                       after[str(path)]['is_file'], 'only exact native generated FLS role')
                    value = {k: after[str(path)][k] for k in ('sha256', 'bytes')}
                expected['local'][str(path)] = value
            else:
                ck(str(path) in known and val(path) == known[str(path)], 'every actual external FLS input in original complete key')
                expected['external'][str(path)] = val(path)
                consumed[str(path)] = val(path)
        ck(recorded == expected, 'entire raw FLS-to-recorded input map including duplicate raw lines bound')
        ck('Output written on main.pdf' in raw(out / (stem + '.log')).decode(), 'complete actual engine-pass log')
    for suffix in ('aux', 'fls', 'log'):
        full_compare(cold / ('main.' + suffix), out / (label + '_pass3.' + suffix), 'terminal_final_pass_snapshot')
    for suffix in ('bbl', 'blg'):
        full_compare(cold / ('main.' + suffix), out / (label + '.' + suffix), 'terminal_bibliography_snapshot')
    ck(re.search(r"(?im)Warning--|I couldn't open|There (?:was|were) [1-9][0-9]* error messages?",
       raw(out / (label + '.blg')).decode()) is None, 'complete BibTeX warning/error scan')
    bst = str(Path(raw(out / 'commands' / (label + '_bst') / 'stdout').decode().strip()).resolve())
    ck(val(bst) == known[bst], 'exact actual bibliography-style dependency')
    consumed[bst] = val(bst)
    metadata = raw(out / 'commands' / (label + '_pdfinfo') / 'stdout').decode()
    fonts = raw(out / 'commands' / (label + '_pdffonts') / 'stdout').decode()
    font_rows = [line.split()[-5:] for line in fonts.splitlines()[2:] if line.strip()]
    ck(font_rows and all(len(row) == 5 and row[0] == 'yes' for row in font_rows), 'all actual complete font records embedded')
    pages = int(re.search(r'^Pages:\s+(\d+)$', metadata, re.M)[1])
    ck(pages == paper['pages'] == 6 and val(cold / 'main.pdf') == paper['pdf_pin'] and
       int(re.search(r'^File size:\s+(\d+) bytes$', metadata, re.M)[1]) == paper['pdf_pin']['bytes'] and
       re.search(r'^Author:[ \t]*$', metadata, re.M), 'actual complete six-page PDF metadata and anonymous author')
    log = raw(cold / 'main.log').decode()
    diagnostics = {name: re.findall(pattern, log, re.M) for name, pattern in dict(undefined=r'^.*undefined.*$',
        overfull=r'^.*Overfull.*$', underfull=r'^.*Underfull.*$', warnings=r'^.*Warning.*$',
        rerun=r'^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$').items()}
    ck(diagnostics['underfull'] == paper['underfull'] == [] and
       all(not value for key, value in diagnostics.items() if key != 'underfull'), 'all actual final TeX diagnostics')
    extracted = raw(out / (label + '.txt')).decode()
    ck(not any(marker in extracted for marker in ('[VERIFY]', '??', '[?]')), 'complete extracted PDF text unresolved-marker scan')
    text_pages = extracted.split('\f')
    if text_pages and not text_pages[-1].strip():
        text_pages.pop()
    ck(len(text_pages) == pages, 'actual complete PDF/text page census')
    reference_pages = [i + 1 for i, body in enumerate(text_pages)
                       if re.search(r'^\s*(?:References|Bibliography)\s*$', body, re.M)]
    ck(reference_pages, 'actual reference heading location no invented venue page limit')
    round2_metadata = raw(out / 'commands/P210_round2_pdfinfo/stdout').decode()
    round2_pages = int(re.search(r'^Pages:\s+(\d+)$', round2_metadata, re.M)[1])
    ck(round2_pages == pages and int(re.search(r'^File size:\s+(\d+) bytes$', round2_metadata, re.M)[1]) ==
       paper['pdf_pin']['bytes'], 'actual native Round2 page-and-byte baseline')
    measured = dict(label=label, pages=pages, pdf=val(cold / 'main.pdf'), fonts=len(font_rows),
        diagnostics=diagnostics, source_count=len(initial), visual_review='NOT_VIEWED',
        reference_heading_pages=reference_pages, round2_measured_pages=round2_pages,
        venue_page_limit=None, bibtex_warnings_or_errors=[])
    ck(obj(out / (label + '_MEASURED.json')) == measured, 'entire exact original measured build result')
    products = {'main.' + suffix for suffix in ('aux', 'bbl', 'blg', 'fls', 'log', 'out', 'pdf')}
    rendered = {'pages/page-' + str(n) + '.png' for n in range(1, pages + 1)} if number == 1 else set()
    ck(physical(cold) == set(initial) | products | rendered, 'entire actual cold directory sources/generated products only')
    for name in rendered:
        ck(raw(cold / name).startswith(b'\x89PNG\r\n\x1a\n'), 'PNG bytes verified not a new visual review')
    return measured, consumed, bookmarks


def terminal_runtime(out, phase, known, original, argv):
    row = obj(out / ('PARENT_RUNTIME_' + phase + '.json'))
    ck(row['argv'] == argv and row['cwd'] == str(ROOT) and row['env'] == TERM_ENV and row['sys_path'] == PY_PATH and
       row['phase'] == ('before_first_child' if phase == 'BEFORE' else 'after_last_child_and_inventory'),
       'entire actual early/late terminal runtime sample context')
    for flag in ('dont_write_bytecode', 'no_user_site', 'no_site', 'ignore_environment', 'isolated'):
        ck(re.search(r'(?:\(|, )' + flag + r'=1(?:,|\))', row['flags']), 'actual isolated terminal runtime flag')
    ck('optimize=0' in row['flags'] and row['cache_absent'] is True and row['cache_prefix'] ==
       str(out / 'unused_parent_cache') and not os.path.lexists(row['cache_prefix']), 'exact absent terminal parent bytecode prefix')
    body = row['maps_raw'].encode()
    ck(len(body) == row['maps_bytes'] and sha256(body).hexdigest() == row['maps_sha256'], 'entire original terminal raw process maps')
    mapped = set()
    for line in row['maps_raw'].splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            ck(not fields[5].endswith(' (deleted)'), 'no recorded deleted terminal mapping')
            mapped.add(str(Path(fields[5]).resolve()))
    ck(mapped == set(row['mapped_files']), 'complete raw terminal map-to-file reconstruction')
    allowed = known | original
    for path, value in row['mapped_files'].items():
        ck(val(path) == value == allowed[path], 'every actual mapped terminal file covered')
    for value in row['modules'].values():
        path = value['path']
        ck(Path(path).suffix not in {'.pyc', '.pyo'} and not {'site-packages', 'dist-packages'} & set(Path(path).parts) and
           {k: value[k] for k in ('sha256', 'bytes')} == val(path) == allowed[path], 'every actual source-only terminal parent module')
    return {'phase': phase, 'modules': len(row['modules']), 'mapped': len(mapped)}


def terminal_originals(out, prep, preparation_rows):
    recipe = obj(prep / 'INPUT_CONTRACT.json')
    final = obj(out / 'FINAL_SCHEMA_BINDING_RETURN.json')
    ck(final['status'] == 'BOUND_ACTUAL_P210_B_ROOT_ROUND2_PRETERMINAL_ORIGINALS' and
       set(final['papers']) == {'P210'}, 'actual final prerequisite return one-paper scope')
    bound = recipe['final_schema_binding']
    required = {}
    for spec in bound['manifests'].values():
        base = Path(spec['path'])
        rows = complete_package(base, spec['seal']['sha256'], spec['payloads'])
        for name, digest in rows.items():
            value = val(base / name)
            ck(value['sha256'] == digest, 'actual terminal prerequisite payload pin')
            required[str(base / name)] = value
        required[str(base / 'SHA256SUMS')] = val(base / 'SHA256SUMS')
    for value in bound['roles'].values():
        expected = {'sha256': value['sha256'], 'bytes': value['bytes']}
        physical_name = historic_hash_path(value['path'], expected['sha256'])
        pin(physical_name, expected)
        ck(value['path'] not in required or required[value['path']] == expected,
           'compatible complete original terminal prerequisite role')
        required[value['path']] = expected
    ck(final['required_input_pins'] == required and final['papers'] == bound['papers'],
       'entire original terminal prerequisite map independently rebuilt from complete packages and actual roles')
    expected = {str(prep / name): val(prep / name) for name in preparation_rows}
    expected[str(prep / 'SHA256SUMS')] = val(prep / 'SHA256SUMS')
    for path, value in recipe['infrastructure_pins'].items():
        ck(path not in required or required[path] == value, 'no conflicting consumed infrastructure role')
    for path, value in (recipe['infrastructure_pins'] | required).items():
        physical_name = historic_hash_path(path, value['sha256'])
        pin(physical_name, sha_record(value))
        expected[path] = value
    paper = final['papers']['P210']
    ck(paper['paper'] == str(PAPER) and paper['freeze'] == str(PAPER / 'frozen_round2') and
       paper['round'] == 2 and paper['freeze_payloads'] == 524 and
       paper['freeze_manifest'] == val(PAPER / 'frozen_round2/SHA256SUMS') and
       tuple(paper['source_names']) == TERM_SOURCE_NAMES and set(paper['source_pins']) == set(TERM_SOURCE_NAMES) and
       paper['pages'] == 6 and paper['underfull'] == [], 'actual exact physical Round2 ten-source six-page contract')
    for base in (PAPER, PAPER / 'frozen_round2'):
        ck(physical(base / 'sections') == {str(Path(name).relative_to('sections')) for name in TERM_SOURCE_NAMES
           if name.startswith('sections/')}, 'entire accepted section source membership')
        for name, value in (paper['source_pins'] | {'main.pdf': paper['pdf_pin']}).items():
            pin(base / name, sha_record(value))
            expected[str(base / name)] = value
        main_source = raw(base / 'main.tex').decode()
        inputs = {name if name.endswith('.tex') else name + '.tex' for name in re.findall(r'\\input\{([^}]+)\}', main_source)}
        ck(inputs == set(TERM_SOURCE_NAMES) - {'main.tex', 'references.bib'} and
           '\\bibliography{references}' in main_source and '\\bibliographystyle{plainnat}' in main_source and
           '\\author{Anonymous}' in main_source and 'pdfauthor={}' in main_source, 'entire main TeX source graph bibliography and anonymous metadata')
    ck(expected == obj(out / 'ORIGINALS_BEFORE.json') == obj(out / 'ORIGINALS_AFTER.json'),
       'entire original terminal prerequisite before-after ledger not summary counts')
    return expected, final


def terminal_complete_receiver_map(actual, out, before):
    ck(actual['status'] == 'PASS_P210_TERMINAL_BUILD_ORIGINAL_DOCUMENTS_ONLY' and
       actual['original_commands'] == 33 and actual['new_science_executions'] == 0 and
       actual['new_builds'] == 0 and actual['new_views'] == 0 and actual['manuscript_reviews'] == 0 and
       actual['root_acceptance'] is False, 'actual receiver documentary-only scope not an independent manuscript review')
    recipe = actual['current_key_reconstruction']
    ck(recipe['known_ledger'] == str(out / 'KNOWN_INPUTS_BEFORE.json.gz') and
       recipe['known_ledger_pin'] == val(out / 'KNOWN_INPUTS_BEFORE.json.gz') and
       recipe['canonical_encoding'] == "json.dumps(complete_map, sort_keys=True, separators=(',', ':')).encode('utf-8'); ensure_ascii=True; no terminal LF" and
       recipe['merge_rule'] == 'Union all three original ledger groups by original path spelling with exact duplicate equality, then disjoint extra_entries; no resolved-path substitution.',
       'exact complete original receiver map reconstruction convention')
    known = {}
    for group in before.values():
        for path, row in group.items():
            ck(path not in known or known[path] == row, 'all original same-spelling ledger entries agree')
            known[path] = row
    extra = recipe['extra_entries']
    ck(not set(known) & set(extra) and len(known) == recipe['known_original_paths'] and
       len(extra) == recipe['extra_count'], 'exact disjoint full terminal receiver key basis')
    complete = known | extra
    encoded = json.dumps(complete, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()
    ck(len(complete) == recipe['complete_entries'] == actual['current_path_keys'] and
       recipe['complete_map'] == {'sha256': sha256(encoded).hexdigest(), 'bytes': len(encoded)} and
       sha256(json.dumps(sorted(complete), separators=(',', ':')).encode()).hexdigest() == actual['current_path_keys_sha256'],
       'entire actual terminal root complete key map independently reconstructed')
    files, nonfiles = {}, {}
    for path, row in complete.items():
        ck(Path(path).is_absolute() and set(row) == {'exists', 'symlink', 'link', 'resolved', 'is_file', 'is_dir'} |
           ({'sha256', 'bytes'} if row['is_file'] else set()) and
           all(type(row[key]) is bool for key in ('exists', 'symlink', 'is_file', 'is_dir')) and
           (type(row['link']) is str if row['symlink'] else row['link'] is None), 'entire original terminal presence-rich schema')
        if row['is_file']:
            original = {'real': row['resolved'], 'sha256': row['sha256'], 'size': row['bytes'],
                        'symlink': row['link'] if row['symlink'] else None}
            selected, current = historical_record(path, original)
            ck(row['exists'] is True and row['is_dir'] is False, 'original terminal regular-file state')
            ck(selected not in files or files[selected] == current, 'compatible exact terminal historical rebase')
            files[selected] = current
        else:
            ck(terminal_entry(path) == row, 'every actual original terminal nonfile presence/link row current')
            nonfiles[path] = row
    for path, value in files.items():
        ck(path not in BASE_KEYS or BASE_KEYS[path] == value, 'terminal and scientific complete current key bases agree')
        BASE_KEYS[path] = value
        ck(path not in REPORT_KEYS or REPORT_KEYS[path] == value, 'two report reconstruction bases agree')
        REPORT_KEYS[path] = value
    return {'recipe': recipe, 'physical_file_keys': len(files), 'nonfile_presence_roles': len(nonfiles)}


def terminal_build_package(spec, actual_receiver):
    out, prep = Path(spec['output']), Path(spec['preparation'])
    ck(out == PAPER / 'qa_final' and prep.parent == QA and prep.name.startswith('p210_terminal_build_revision_'),
       'actual physical terminal output and separately sealed revision role')
    prep_rows = complete_package(prep, spec['preparation_seal']['sha256'], spec['preparation_payloads'])
    output_rows = complete_package(out, spec['output_seal']['sha256'], spec['output_payloads'])
    ck(val(prep / 'SHA256SUMS') == spec['preparation_seal'] and val(out / 'SHA256SUMS') == spec['output_seal'],
       'both entire actual preparation/output byte-size-and-hash seals')
    full_compare(prep / 'build_p210.py', out / 'executed_source.py', 'terminal_actual_executed_source')
    original, final = terminal_originals(out, prep, prep_rows)
    paper = final['papers']['P210']
    result = obj(out / 'RESULT.json')
    ck(result['status'] == 'PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED' and result['failures'] == [] and
       result['new_mathematical_executions'] == 0 and result['external'] == 'OWNER_AMBER / HOLD_EXTERNAL' and
       result['visual_review'] == 'NOT_VIEWED_ROOT_ACTUAL_PAGE_INSPECTION_REQUIRED' and
       result['paper_completion'] is False and result['five_paper_completion'] is False,
       'actual two-build result has no future paper/view/batch acceptance')
    before, before_raw = terminal_ledger(out, 'BEFORE')
    after, after_raw = terminal_ledger(out, 'AFTER')
    ck(before == after and before_raw == after_raw, 'entire original terminal gzip pre/post interval')
    membership = terminal_membership(before)
    known = {}
    for group in before.values():
        for path, value in group.items():
            ck(terminal_entry(path) == value, 'every actual original terminal candidate byte/presence/link key current')
            if value['is_file']:
                simple = {'sha256': value['sha256'], 'bytes': value['bytes']}
                ck(value['resolved'] not in known or known[value['resolved']] == simple, 'compatible original resolved terminal coverage')
                known[value['resolved']] = simple
    rows = terminal_native_records(out, result, terminal_commands(out, prep, paper))
    measured, consumed, bookmarks = [], {}, []
    user_roots = obj(out / 'USER_ROOTS.json')
    ck(len(user_roots) == 6, 'all six actual terminal user-root queries')
    for number in (1, 2):
        label = 'P210_cold_build_' + str(number)
        value, external, historical = terminal_build_records(out, number, paper, rows, known)
        measured.append(value)
        consumed.update(external)
        bookmarks.extend(historical)
        for variable in TERM_USER_VARS:
            raw_query = raw(out / 'commands' / (label + '_' + variable) / 'stdout').decode().strip()
            query = Path(raw_query)
            resolved = (query if query.is_absolute() else out / ('cold_build_' + str(number)) / query).resolve()
            ck(user_roots[label + ':' + variable] == dict(query=raw_query, resolved=str(resolved), absent=True) and
               not os.path.lexists(resolved), 'every actual queried user TeX directory still absent')
            terminal_entry(resolved)
    ck(measured == result['builds'] == actual_receiver['original_builds'] and obj(out / 'CONSUMED_TEX_BEFORE.json') ==
       obj(out / 'CONSUMED_TEX_AFTER.json') == consumed, 'all actual measured build rows and full consumed-TeX union')
    libraries = []
    for phase in ('BEFORE', 'AFTER'):
        body = raw(out / 'commands' / ('ldd_' + phase.lower()) / 'stdout').decode()
        paths = {str(Path(path).resolve()) for path in re.findall(r'(/[^\s():]+)', body)}
        record = obj(out / ('LIBRARIES_' + phase + '.json'))
        ck('not found' not in body and paths == set(record), 'entire actual ldd headers and linked-file closure')
        for path, value in record.items():
            ck(val(path) == value == known[path], 'every actual linked terminal file covered')
        libraries.append(record)
    ck(libraries[0] == libraries[1], 'entire original terminal link-time pre/post interval')
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(out / 'unused_parent_cache'),
            str(prep / 'build_p210.py'), '--output', str(out), '--expected-preparation-sha256', spec['preparation_seal']['sha256']]
    runtime = [terminal_runtime(out, phase, known, original, argv) for phase in ('BEFORE', 'AFTER')]
    ck(raw(out / 'commands/texmf_roots/stdout') ==
       b'{{}./.texlive2021/texmf-config,./.texlive2021/texmf-var,./texmf,!!/usr/local/share/texmf,/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf,!!/usr/share/texlive/texmf-dist}\n',
       'actual complete TeX search-root configuration return')
    stdout = json.dumps(dict(status=result['status'], output=str(out), commands=33, builds=measured,
                            failures=[], seal=val(out / 'SHA256SUMS'), payloads=len(output_rows)), sort_keys=True) + '\n'
    expected_native = dict(argv=['/usr/bin/env', '-i', *[key + '=' + value for key, value in TERM_ENV.items()], *argv],
                           cwd=str(ROOT), exit_code=0, stdout=stdout, stderr='')
    complete_map = terminal_complete_receiver_map(actual_receiver, out, before)
    ck(actual_receiver['build_seal'] == spec['output_seal']['sha256'] and actual_receiver['original_payloads'] == len(output_rows) and
       actual_receiver['gzip_groups'] == membership and actual_receiver['original_inputs'] == len(original) and
       actual_receiver['consumed_tex'] == len(consumed) and actual_receiver['linked_files'] == len(libraries[0]) and
       actual_receiver['parent_runtime_samples'] == runtime and
       actual_receiver['historical_first_pass_bookmark_hash_roles'] == bookmarks, 'entire actual terminal documentary reception census')
    CURRENT_SCOPES.append(('terminal', before, membership))
    return dict(output_payloads=len(output_rows), reused_terminal_builds=2, native_commands=33,
        measured=measured, known_groups=membership, full_map=complete_map,
        historical_bookmark_hash_roles_not_physical_old_bytes=bookmarks, expected_native=expected_native,
        new_science_runs=0, new_builds=0, new_views=0)


def terminal_failed_attempt_and_preflight():
    failed = QA / 'p210_terminal_launch_01'
    ck(physical(failed) == {'UNCLOSED.json', 'SPAWNED.json', 'builder.stderr', 'builder.stdout',
       'PRE_SPAWN_ATTEMPT.json', 'executed_builder.py', 'executed_launcher.py',
       'LAUNCHER_RUNTIME_BEFORE.json', 'INPUTS_BEFORE.json'} and not os.path.lexists(failed / 'SHA256SUMS'),
       'all nine actual first-failure files remain unsealed unchanged no invented completion')
    complete_package(QA / 'p210_terminal_build_revision_01',
                     '37c6e8f996dc693ebd8280faf4705d35db8d04fbc19bb306de264ca56af972e7', 19)
    complete_package(QA / 'p210_terminal_launch_revision_01',
                     'abb0d66a498241cf3262c4f8e4e0c22fd7cf812b8d9e6213f0cbb861d559e7de', 11)
    full_compare(failed / 'executed_builder.py', QA / 'p210_terminal_build_revision_01/build_p210.py', 'failed_terminal_builder_original')
    full_compare(failed / 'executed_launcher.py', QA / 'p210_terminal_launch_revision_01/launch_p210_terminal.py', 'failed_terminal_launcher_original')
    inputs = obj(failed / 'INPUTS_BEFORE.json')
    for path, value in inputs.items():
        pin(historic_hash_path(path, value['sha256']), sha_record(value))
    attempt, spawned, failure = (obj(failed / name) for name in ('PRE_SPAWN_ATTEMPT.json', 'SPAWNED.json', 'UNCLOSED.json'))
    completed = obj(QA / 'P210_TERMINAL_OUTER_ROOT_COMPLETION.actual.json')
    diagnosis = obj(QA / 'P210_TERMINAL_FAILURE01_ROOT_DIAGNOSIS.actual.json')
    diagnosed = json.loads(diagnosis['result']['output'])
    ck(completed['result']['exit_code'] == failure['original_wait_exit_code'] == failure['cleanup_exit_code'] == 1 and
       failure['original_wait_outcome'] == 'COMPLETED' and failure['failure'] is None and
       failure['original_wait_exception'] is None and failure['builder_reaped'] is failure['builder_group_absent'] is True and
       failure['cleanup_events'] == [] and failure['status'] == 'UNCLOSED_OR_FAILED_NO_SEAL' and
       failure['streams_hashed'] is False and failure['outer_native_exit'] is None,
       'original normal failed return preserved without retroactive seal or native fields')
    ck(attempt['argv'] == failure['argv'] and attempt['cwd'] == failure['cwd'] == str(ROOT) and
       attempt['env'] == failure['env'] == TERM_ENV and attempt['original_wait_exit_code'] is None and
       attempt['original_wait_outcome'] == 'NOT_STARTED' and attempt['started_epoch'] == failure['started_epoch'] and
       spawned == dict(pid=failure['pid'], owned_pgid=failure['pid'], start_new_session=True),
       'entire actual failed prespawn/spawn identity')
    ck(diagnosis['result']['exit_code'] == 0 and diagnosed['status'] ==
       'ROOT_DIAGNOSED_TERMINAL_ATTEMPT01_PREOUTPUT_SCHEMA_FAILURE' and diagnosed['actual_native_exit'] == 1 and
       diagnosed['builder_pid'] == failure['pid'] and diagnosed['current_owned_group_absent'] is True and
       diagnosed['qa_final_absent'] is True and diagnosed['terminal_native_build_commands'] == 0 and
       diagnosed['old_failure_package_left_unsealed'] is True and diagnosed['actual_field_type'] == 'list' and
       diagnosed['actual_field_length'] == 1016 and diagnosed['all_actual_comparison_rows_schema_and_equal_true'] is True,
       'actual historical diagnosis before qa_final creation not a current absence claim')
    for name, value in diagnosed['streams'].items():
        ck(set(value) == {'utf8', 'bytes', 'sha256'} and raw(failed / name).decode() == value['utf8'],
           'entire separate root-diagnosed failure stream')
        pin(failed / name, {'sha256': value['sha256'], 'bytes': value['bytes']})
    ck(raw(failed / 'builder.stdout') == b'' and
       raw(failed / 'builder.stderr').endswith(b'RuntimeError: Actual Round2 accepted binding and provenance\n'),
       'exact first actual before-output gate failure retained')
    preflight = QA / 'p210_terminal_preflight_02'
    complete_package(preflight, 'd6adc396a8562e8683f66df348aa420ce3f97997b4bf73c0c674f621aac7fb1c', 6)
    full_compare(preflight / 'executed_source.py', QA / 'record_p210_terminal_preflight_02.py', 'actual_preflight_recorder_source')
    a, s, r = (obj(preflight / name) for name in ('ATTEMPT.json', 'SPAWN.json', 'RESULT.json'))
    result = original_native_summary('P210_TERMINAL_PREFLIGHT02_ROOT_LAUNCH.actual.json',
        'P210_TERMINAL_PREFLIGHT02_ROOT_COMPLETION.actual.json', 78288)
    ck(result['status'] == 'PASS_ACTUAL_P210_PREFLIGHT_CAPTURE' and result['output'] == str(preflight) and
       result['result'] == val(preflight / 'RESULT.json') and result['seal'] == val(preflight / 'SHA256SUMS') and
       result['terminal_acceptance'] is False, 'actual completed preflight parent capture only')
    ck(r['original_wait_exit_code'] == r['cleanup_wait_exit_code'] == 0 and r['timed_out'] is False and
       r['wait_error'] is None and r['cleanup_events'] == [] and r['child_reaped'] is r['process_group_absent'] is True and
       r['inputs_before'] == r['inputs_after'] == a['inputs_before'] and r['inputs_unchanged'] is True and
       r['argv'] == a['argv'] and r['cwd'] == a['cwd'] == str(ROOT) and r['environment'] == a['environment'] == TERM_ENV and
       r['paper_terminal_absent_after'] is a['paper_terminal_absent_before'] is True and
       s['pid'] == s['process_group_id'] == r['pid'] and
       a['started_epoch'] <= s['spawned_epoch'] <= r['finished_epoch'], 'entire actual preflight settled return and interval')
    for path, value in r['inputs_before'].items():
        pin(path, sha_record(value))
    for stream in ('stdout', 'stderr'):
        ck(r[stream] == result[stream] == val(preflight / stream), 'both actual preflight raw stream pins')
    ck(raw(preflight / 'stderr') == b'', 'entire actual preflight stderr empty')
    data = obj(preflight / 'stdout')
    ck(data['status'] == 'PASS_P210_FINAL_SCHEMA_PREFLIGHT_ONLY' and data['output'] == str(PAPER / 'qa_final') and
       data['output_created'] is False and data['child_commands'] == data['host_inventory_collections'] ==
       data['new_science_build_view_executions'] == 0 and data['terminal_acceptance'] is False and
       len(data['original_input_pins']) == data['original_input_count'] == result['original_input_count'] == 1619,
       'actual preflight full original gate no TeX science inventory or views')
    for path, value in data['original_input_pins'].items():
        pin(historic_hash_path(path, value['sha256']), sha_record(value))
    acceptance = obj(QA / 'P210_TERMINAL_PREFLIGHT02_ROOT_RECEPTION.actual.json')
    accepted = json.loads(acceptance['result']['output'])
    ck(acceptance['result']['exit_code'] == 0 and accepted['status'] == 'PASS_ROOT_ACTUAL_PREFLIGHT02_FULL_RAW_ORIGINAL_RECEPTION' and
       accepted['actual_parent_session'] == 78288 and accepted['all_actual_input_pins_rehashed'] == 1619 and
       accepted['full_final_binding_required_pins'] == 1594 and accepted['complete_capture_payloads'] == 6 and
       accepted['capture_seal'] == val(preflight / 'SHA256SUMS') and accepted['new_scientific_build_or_visual_executions'] == 0 and
       accepted['terminal_acceptance'] is False, 'separate actual root preflight reception remains nonterminal')
    return {'first_actual_failed_native_exit': 1, 'first_failed_files_preserved_unsealed': 9,
            'first_failed_terminal_children': 0, 'preflight_original_inputs': 1619,
            'preflight_new_science_build_view_executions': 0}


def current_reader_runtime():
    ck(Path(__file__).resolve() == PREP / 'inspect_p210_artifact.py' and Path.cwd() == ROOT and
       Path(sys.executable).resolve() == Path('/usr/bin/python3.10') and dict(os.environ) == ENV and
       sys.path == PY_PATH and sys.flags.isolated == sys.flags.no_site == 1 and
       sys.flags.optimize == 0 and sys.flags.dont_write_bytecode == 1,
       'current artifact reader exact isolated source-only interpreter ENV4 cwd')
    cache = str(QA / 'p210_terminal_artifact_01/never_created_reader_cache')
    ck(sys.pycache_prefix == cache and not os.path.lexists(cache), 'current artifact reader exact absent bytecode prefix')
    modules = {}
    for name, module in sorted(sys.modules.items()):
        value = getattr(module, '__file__', None)
        if value is None or not Path(value).is_file():
            continue
        path = Path(value).resolve()
        ck(path.suffix not in {'.pyc', '.pyo'} and not {'site-packages', 'dist-packages'} & set(path.parts) and
           (not path.is_relative_to(ROOT) or path == PREP / 'inspect_p210_artifact.py'),
           'no old project program or bytecode imported by current artifact reader')
        modules[name] = {'path': str(path), **pin(path)}
    body = Path('/proc/self/maps').read_bytes()
    mapped = {}
    for line in body.decode().splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            ck(not fields[5].endswith(' (deleted)'), 'current artifact reader no deleted mapped input')
            path = str(Path(fields[5]).resolve())
            mapped[path] = pin(path)
    return dict(argv=sys.orig_argv, cwd=str(ROOT), environment=dict(os.environ), executable=sys.executable,
        sys_path=sys.path, flags=str(sys.flags), cache_prefix=cache, cache_absent=True, modules=modules,
        mapped_files=mapped, raw_maps=body.decode(), raw_maps_sha256=sha256(body).hexdigest(), raw_maps_bytes=len(body),
        scope='Current reader sample only; volatile maps are not immutable inputs or a continuous execution trace.')


def final_current_closure():
    before = dict(SEEN)
    for path, value in before.items():
        ck(pin(path, force=True) == value, 'final entire uncached physical rich input key reread')
    for path, value in list(TERM_NONFILES.items()):
        ck(terminal_entry(path) == value, 'final entire terminal nonfile presence/link reread')
    for scope in CURRENT_SCOPES:
        if scope[0] == 'B':
            _, label, ledger, original = scope
            ck(current_membership(ledger, label.startswith('build')) == original,
               'final exact original B source-defined candidate membership')
        elif scope[0] == 'strict':
            _, resources, configuration = scope
            ck(current_resources() == resources and configuration_snapshot() == configuration,
               'final exact strict resources and all41 configuration roles')
        else:
            ck(scope[0] == 'terminal' and terminal_membership(scope[1]) == scope[2],
               'final exact original terminal source-defined candidate membership')
    for manifest_path, rows in MANIFESTS.items():
        path = Path(manifest_path)
        ck(manifest_rows(path) == rows and physical(path.parent) == set(rows) | {path.name},
           'every entire sealed physical package remains unchanged')
    ck(set(SEEN) == set(before) and SEEN == before, 'no unreported read key added after final full reread')
    ck(USED_ALIASES == set(ALIASES) and len(ALIASES) == 10, 'all and only ten actual historical triples exercised')
    ck(set(REPORT_KEYS) <= set(SEEN) and all(SEEN[path] == value for path, value in REPORT_KEYS.items()),
       'current report bases are exact subset of entire current read map')
    extra = {path: value for path, value in SEEN.items() if path not in REPORT_KEYS}
    ck(not set(REPORT_KEYS) & set(extra) and REPORT_KEYS | extra == SEEN,
       'complete disjoint two-basis reconstruction plus current rich extras')
    encoded = json.dumps(SEEN, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()
    base_encoded = json.dumps(REPORT_KEYS, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()
    return dict(complete_keys=len(SEEN), canonical_map={'sha256': sha256(encoded).hexdigest(), 'bytes': len(encoded)},
        canonical_encoding="json.dumps(current_map,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode(); no LF",
        base_union_keys=len(REPORT_KEYS), base_union_canonical={'sha256': sha256(base_encoded).hexdigest(), 'bytes': len(base_encoded)},
        base_rule='B-final full121057 original rich map and terminal receiver original file-rich map; exact recorded logical/hash/size aliases rebased to their pinned physical rows, duplicate physical keys must agree.',
        extra_current_keys=extra, extra_count=len(extra), exact_historical_aliases=[ALIASES[key] for key in sorted(ALIASES)],
        nonfile_presence_roles=TERM_NONFILES, nonfile_presence_count=len(TERM_NONFILES),
        current_directory_membership_reconstructed_again=True, all_current_physical_keys_fully_reread_twice=True,
        new_host_ledger_files_written=0)


def current_pending_whole_and_links(contract, terminal):
    roles = contract['pending_lifecycle']
    ck(roles['lifecycle_path'] == str(PAPER / 'ROOT_LIFECYCLE.md') and
       roles['whole_manifest_path'] == str(PAPER / 'PAPER_MANIFEST.sha256'), 'exact current pending lifecycle/whole roles')
    pin(roles['lifecycle_path'], sha_record(roles['lifecycle_pin']))
    pin(roles['whole_manifest_path'], sha_record(roles['whole_manifest_pin']))
    before = manifest_rows(QA / 'p210_preterminal_controls_01/PAPER_MANIFEST.sha256')
    rows = complete_package(PAPER, roles['whole_manifest_pin']['sha256'],
                            2021 + terminal['output_payloads'] + 1, 'PAPER_MANIFEST.sha256')
    expected_added = {'qa_final/' + name for name in physical(PAPER / 'qa_final')}
    ck(len(before) == 2021 and set(before) <= set(rows) and set(rows) - set(before) == expected_added and
       len(expected_added) == terminal['output_payloads'] + 1 and
       {name for name in before if rows[name] != before[name]} == {'ROOT_LIFECYCLE.md'} and
       rows['ROOT_LIFECYCLE.md'] == roles['lifecycle_pin']['sha256'],
       'actual first terminal pending refresh adds only sealed qa_final files and changes only live lifecycle')
    body = raw(PAPER / 'ROOT_LIFECYCLE.md').decode()
    ck('TERMINAL_BUILDS_VIEWS_COMPLETE' in body and 'ARTIFACT_GATE_PENDING' in body and
       'HOLD_EXTERNAL' in body, 'actual initial-gate pending stage not a prematurely complete lifecycle')
    links = []
    for href in stripped_links(body):
        reference = href.strip().strip('<>').split('#', 1)[0]
        if not reference or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', reference):
            continue
        path = (PAPER / unquote(reference)).resolve()
        ck(path.is_relative_to(ROOT) and path.is_file(), 'new lifecycle genuine local link resolves to exact bounded file')
        links.append(dict(document=str(PAPER / 'ROOT_LIFECYCLE.md'), href=href, path=str(path), pin=pin(path)))
    ck(links and set(roles['required_actual_link_targets']) <= {row['path'] for row in links},
       'pending lifecycle links include exact actual accepted terminal/view evidence')
    source = QA / 'refresh_p210_terminal_whole_manifest.py'
    pin(source, '4f89eef8a28e6bc697c17b6f22e1032885521095f85ee3de4e9b98ca998248fb')
    refresh = obj(QA / 'P210_TERMINAL_LIFECYCLE_REFRESH.actual.json')
    expected_native = dict(argv=['/usr/bin/sha256sum', '--check', 'PAPER_MANIFEST.sha256'], cwd=str(PAPER),
        environment=ENV, exit=0, stdout=''.join(name + ': OK\n' for name in sorted(rows)), stderr='')
    ck(refresh == dict(status='PASS_P210_TERMINAL_LIFECYCLE_AND_WHOLE_MANIFEST_REFRESH', old_payloads=2021,
       current_payloads=2244, physical_files=2245, added_terminal_files=223,
       sole_changed_old_payload='ROOT_LIFECYCLE.md',
       old_whole_sha256=val(QA / 'p210_preterminal_controls_01/PAPER_MANIFEST.sha256')['sha256'],
       old_lifecycle_sha256=before['ROOT_LIFECYCLE.md'], new_lifecycle_sha256=roles['lifecycle_pin']['sha256'],
       new_whole_sha256=roles['whole_manifest_pin']['sha256'], terminal_sha256=val(PAPER / 'qa_final/SHA256SUMS')['sha256'],
       native=expected_native, source_sha256=val(source)['sha256'],
       scope='Mechanical rolling manifest plus documentary lifecycle only; all original/frozen science bytes unchanged.'),
       'entire actual first pending refresh receipt and complete original2244-line native stdout')
    NATIVE_RECORDS.append(dict(kind='actual_first_pending_whole_refresh', **expected_native))
    return dict(status='ACTUAL_TERMINAL_BUILDS_VIEWS_COMPLETE_ARTIFACT_GATE_PENDING',
        current_whole_payloads=len(rows), old_whole_payloads=2021, added_terminal_files=len(expected_added),
        sole_changed_old_payload='ROOT_LIFECYCLE.md', lifecycle=val(PAPER / 'ROOT_LIFECYCLE.md'),
        whole_manifest=val(PAPER / 'PAPER_MANIFEST.sha256'), genuine_local_links=links,
        actual_refresh_receipt=val(QA / 'P210_TERMINAL_LIFECYCLE_REFRESH.actual.json'),
        complete_original_native_whole_lines=len(rows),
        current_paper_complete=False, required_distinct_after_artifact_lifecycle_followup=True)


def actual_terminal_outer():
    outer, prep = QA / 'p210_terminal_launch_02', QA / 'p210_terminal_launch_revision_02'
    builder_prep, output = QA / 'p210_terminal_build_revision_02', PAPER / 'qa_final'
    prep_rows = complete_package(prep, '6adbded08080db7be5ec261c59c18adf298464f6012e3e266b20e51d56b29bc2', 8)
    complete_package(outer, '42fed5ca10fc44fb36159f955f9193342d0775ec0f2886efd09237293e96e773', 11)
    builder_rows = complete_package(builder_prep, '2e99af39ab35bfb9e3fec7c9944927c574fe459b56a1b764a5948dde0266e31a', 9)
    full_compare(outer / 'executed_launcher.py', prep / 'launch_p210_terminal.py', 'terminal_actual_outer_source')
    full_compare(outer / 'executed_builder.py', builder_prep / 'build_p210.py', 'terminal_actual_outer_builder_copy')
    launch = obj(QA / 'P210_TERMINAL_OUTER02_ROOT_LAUNCH.actual.json')
    completed = obj(QA / 'P210_TERMINAL_OUTER02_ROOT_COMPLETION.actual.json')
    outer_argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(outer / 'unused_outer_cache'),
                  str(prep / 'launch_p210_terminal.py'), '--expected-preparation-sha256', val(prep / 'SHA256SUMS')['sha256']]
    ck(shlex.split(launch['command']) == ['/usr/bin/env', '-i',
       *[key + '=' + value for key, value in TERM_ENV.items()], *outer_argv] and launch['cwd'] == str(ROOT) and
       launch['result']['session_id'] == completed['session_id'] == 91983 and launch['result']['output'] == '' and
       completed['launch_record'] == 'P210_TERMINAL_OUTER02_ROOT_LAUNCH.actual.json' and
       completed['result']['exit_code'] == 0 and not os.path.lexists(outer / 'unused_outer_cache'),
       'actual normal-zero terminal outer parent command/session no synthesized parent stderr')
    attempt, spawn, receipt = (obj(outer / name) for name in ('PRE_SPAWN_ATTEMPT.json', 'SPAWNED.json', 'RECEIPT.json'))
    builder_argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(output / 'unused_parent_cache'),
                    str(builder_prep / 'build_p210.py'), '--output', str(output), '--expected-preparation-sha256',
                    val(builder_prep / 'SHA256SUMS')['sha256']]
    expected_attempt = dict(argv=builder_argv, cwd=str(ROOT), env=TERM_ENV, started_epoch=attempt['started_epoch'],
        timeout_seconds=21600, start_new_session=True, original_wait_outcome='NOT_STARTED',
        original_wait_exit_code=None, original_wait_exception=None, stdout='builder.stdout', stderr='builder.stderr',
        outer_native_exit=None, outer_native_scope='Unknown here. Root must archive the actual tool completion separately.')
    ck(attempt == expected_attempt and set(receipt) == set(attempt) | {'pid', 'cleanup_events', 'cleanup_exit_code',
       'builder_reaped', 'builder_group_absent', 'finished_epoch', 'inputs_unchanged', 'failures', 'observed_runtime_closed',
       'builder_closure', 'streams', 'streams_hashed', 'cache_absent', 'visual_review', 'status'} and
       all(receipt[key] == value for key, value in attempt.items() if key not in {'original_wait_outcome', 'original_wait_exit_code'}),
       'entire actual outer attempt/receipt schema and unchanged pre-spawn context')
    ck(receipt['status'] == 'PASS_P210_OUTER_CAPTURE_NOT_VIEWED' and receipt['original_wait_outcome'] == 'COMPLETED' and
       receipt['original_wait_exit_code'] == receipt['cleanup_exit_code'] == 0 and receipt['cleanup_events'] == [] and
       receipt['builder_reaped'] is receipt['builder_group_absent'] is receipt['inputs_unchanged'] is True and
       receipt['observed_runtime_closed'] is receipt['streams_hashed'] is receipt['cache_absent'] is True and
       receipt['failures'] == [] and receipt['visual_review'] == 'NOT_VIEWED' and
       receipt['finished_epoch'] >= receipt['started_epoch'] and type(receipt['pid']) is int and receipt['pid'] > 0 and
       spawn == dict(pid=receipt['pid'], owned_pgid=receipt['pid'], start_new_session=True),
       'actual native outer zero/no cleanup/settled evidence not retrospective PID liveness')
    closure = dict(manifest=val(output / 'SHA256SUMS'), payloads=222, result=val(output / 'RESULT.json'),
                   status='PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED')
    ck(receipt['builder_closure'] == closure and json.loads(completed['result']['output']) ==
       dict(status=receipt['status'], output=str(outer), builder_exit_code=0,
            launcher_seal=val(outer / 'SHA256SUMS'), builder_closure=closure), 'entire actual outer root native return')
    before, after = obj(outer / 'INPUTS_BEFORE.json'), obj(outer / 'INPUTS_AFTER.json')
    expected = {}
    for base, rows in ((prep, prep_rows), (builder_prep, builder_rows),
                       (QA / 'p210_terminal_preflight_02', manifest_rows(QA / 'p210_terminal_preflight_02/SHA256SUMS'))):
        expected.update({str(base / name): val(base / name) for name in rows})
        expected[str(base / 'SHA256SUMS')] = val(base / 'SHA256SUMS')
    for name in ('record_p210_terminal_preflight_02.py', 'P210_TERMINAL_PREFLIGHT02_ROOT_LAUNCH.actual.json',
                 'P210_TERMINAL_PREFLIGHT02_ROOT_COMPLETION.actual.json', 'P210_TERMINAL_PREFLIGHT02_ROOT_RECEPTION.actual.json'):
        expected[str(QA / name)] = val(QA / name)
    for mapping in (obj(QA / 'p210_terminal_preflight_02/RESULT.json')['inputs_before'],
                    obj(QA / 'p210_terminal_preflight_02/stdout')['original_input_pins']):
        for path, value in mapping.items():
            ck(path not in expected or expected[path] == value, 'compatible actual outer preflight input role')
            expected[path] = value
    samples = []
    for phase in ('BEFORE', 'AFTER'):
        row = obj(outer / ('LAUNCHER_RUNTIME_' + phase + '.json'))
        ck(row['phase'] == ('BEFORE_BUILDER_AND_OUTPUT_CREATION' if phase == 'BEFORE' else 'AFTER_CLOSED_BUILDER_AND_INPUT_REREAD') and
           row['orig_argv'] == outer_argv and row['cwd'] == str(ROOT) and row['environment'] == TERM_ENV and
           row['executable'] == '/usr/bin/python3.10' and row['sys_path'] == PY_PATH and
           row['cache_prefix'] == str(outer / 'unused_outer_cache') and row['cache_absent'] is True,
           'entire actual outer early/late runtime sample context')
        ck(all(re.search(r'(?:\(|, )' + flag + '=1(?:,|\\))', row['flags']) for flag in
           ('isolated', 'no_site', 'ignore_environment', 'dont_write_bytecode')) and 'optimize=0' in row['flags'],
           'actual outer source-only isolated flags')
        mapped = set()
        for line in row['maps_raw'].splitlines():
            fields = line.split(None, 5)
            if len(fields) == 6 and fields[5].startswith('/'):
                ck(not fields[5].endswith(' (deleted)'), 'no recorded deleted outer mapping')
                mapped.add(str(Path(fields[5]).resolve()))
        ck(mapped == set(row['mapped_files']), 'entire recorded outer raw maps reconstructed')
        observed = dict(row['mapped_files'])
        for value in row['modules'].values():
            path = value['path']
            ck(Path(path).suffix not in {'.pyc', '.pyo'} and not {'site-packages', 'dist-packages'} & set(Path(path).parts),
               'actual outer source-only imported modules')
            observed[path] = {key: value[key] for key in ('sha256', 'bytes')}
        for path, value in observed.items():
            pin(path, sha_record(value))
            if phase == 'BEFORE':
                ck(path not in expected or expected[path] == value, 'compatible early outer dependency role')
                expected[path] = value
            else:
                ck(before[path] == value, 'every late outer runtime dependency already in before key')
        samples.append({'phase': phase, 'modules': len(row['modules']), 'mapped_files': len(mapped)})
    expected['/usr/bin/python3.10'] = val('/usr/bin/python3.10')
    ck(before == after == expected, 'entire actual outer input ledger independently reconstructed')
    for path, value in before.items():
        pin(historic_hash_path(path, value['sha256']), sha_record(value))
    ck(set(receipt['streams']) == {'builder.stdout', 'builder.stderr'}, 'actual outer captured complete dual streams')
    for name, value in receipt['streams'].items():
        pin(outer / name, sha_record(value))
    ck(raw(outer / 'builder.stderr') == b'', 'entire actual captured builder stderr empty')
    return (dict(argv=['/usr/bin/env', '-i', *[key + '=' + value for key, value in TERM_ENV.items()], *builder_argv],
                cwd=str(ROOT), exit_code=receipt['original_wait_exit_code'], stdout=raw(outer / 'builder.stdout').decode(), stderr=''),
                dict(actual_parent_session=91983, original_outer_exit=0, actual_outer_payloads=11,
                     original_input_keys=len(before), own_runtime_samples=samples, actual_builder_commands=33,
                     old_not_viewed_fields_retained=True))


def actual_six_root_views():
    path = QA / 'P210_TERMINAL_ROOT_VIEWS.actual.json'
    view = obj(path)
    ck(view['schema'] == 'p210-terminal-root-every-page-view-v1' and
       view['status'] == 'ROOT_ACTUALLY_VIEWED_ALL_SIX_FINAL_PAGES_PASS' and view['reviewer'] == '/root' and
       view['paper'] == 'P210' and view['terminal_manifest_sha256'] == pin(PAPER / 'qa_final/SHA256SUMS')['sha256'] and
       view['pdf_sha256'] == pin(PAPER / 'qa_final/cold_build_1/main.pdf')['sha256'] and
       view['measured_page_count'] == 6 and view['open_visual_findings'] == 0 and
       [row['page'] for row in view['pages']] == list(range(1, 7)) and
       view['external'] == 'OWNER_AMBER / HOLD_EXTERNAL', 'actual six-page root visual receipt not rendered-file existence')
    for row in view['pages']:
        ck(set(row) == {'bytes', 'page', 'path', 'sha256', 'actually_displayed_and_viewed', 'observation'} and
           row['path'] == str(PAPER / 'qa_final/cold_build_1/pages' / ('page-' + str(row['page']) + '.png')) and
           row['actually_displayed_and_viewed'] is True and type(row['observation']) is str and row['observation'],
           'all actual selected page identities and root observations')
        pin(row['path'], {'sha256': row['sha256'], 'bytes': row['bytes']})
    inputs = obj(QA / 'P210_TERMINAL_ROOT_VIEWS_INPUTS.actual.json')
    measured = json.loads(inputs['result']['output'])
    ck(inputs['result']['exit_code'] == 0 and measured['status'] == 'PASS_ROOT_TERMINAL_SEALED_VIEW_INPUT_BINDING' and
       measured['terminal_manifest'] == val(PAPER / 'qa_final/SHA256SUMS') and measured['complete_terminal_payloads'] == 222 and
       measured['actual_native_commands'] == 33 and measured['current_owned_groups_absent'] is True and
       measured['full_pdf_raw_pair_and_frozen_equality'] is True and measured['pdf'] == val(PAPER / 'qa_final/cold_build_1/main.pdf') and
       measured['builds'] == obj(PAPER / 'qa_final/RESULT.json')['builds'] and measured['pages'] ==
       [{key: value for key, value in row.items() if key in {'bytes', 'page', 'path', 'sha256'}} for row in view['pages']],
       'actual separate root native view-input binding retains nonvisual scope')
    return dict(actual_root_view_record=str(path), view_pin=val(path), pages_actually_viewed_by_root=6,
                current_open_visual_findings=0, new_views_by_this_reader=0,
                historical_author_pending_text_retained=view['historical_author_text'])


def actual_terminal_receiver_capture(contract):
    directory = QA / 'p210_terminal_root_reception_01'
    prep = QA / 'p210_terminal_reception_revision_01'
    source = QA / 'record_p210_terminal_reception_01.py'
    spec = contract['terminal']
    complete_package(prep, '9a4b0d50cb8e70cd1aaddf6d1ab0c9351778a604e45395bf86af52cf3807ae88', 9)
    complete_package(directory, spec['root_receiver_capture_seal']['sha256'], 6)
    ck(val(directory / 'SHA256SUMS') == spec['root_receiver_capture_seal'] and
       spec['root_receiver_result_path'] == str(directory / 'ROOT_RECEPTION.json'),
       'exact actual receiver full raw stdout path and physical six-payload capture')
    full_compare(source, directory / 'executed_source.py', 'actual_terminal_receiver_recorder_source')
    attempt, spawn, result = (obj(directory / name) for name in ('ATTEMPT.json', 'SPAWN.json', 'RESULT.json'))
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(directory / 'unused_receiver_cache'), str(prep / 'inspect_p210_terminal.py')]
    paths = (source, prep / 'inspect_p210_terminal.py', prep / 'INPUT_CONTRACT.json', prep / 'SHA256SUMS',
             PAPER / 'qa_final/SHA256SUMS', QA / 'p210_terminal_launch_02/SHA256SUMS',
             QA / 'P210_TERMINAL_OUTER02_ROOT_COMPLETION.actual.json', Path('/usr/bin/python3.10'))
    inputs = {str(path): val(path) for path in paths}
    ck(attempt == dict(argv=argv, cwd=str(ROOT), environment=TERM_ENV, inputs_before=inputs,
       timeout_seconds=600, start_new_session=True, started_epoch=attempt['started_epoch'],
       paper_terminal_present_before=True), 'entire actual documentary receiver pre-spawn attempt')
    ck(set(result) == {'argv', 'cwd', 'environment', 'pid', 'original_wait_exit_code', 'cleanup_wait_exit_code',
       'timed_out', 'wait_error', 'cleanup_events', 'child_reaped', 'process_group_absent', 'inputs_before',
       'inputs_after', 'inputs_unchanged', 'stdout', 'stderr', 'paper_terminal_present_after', 'finished_epoch'} and
       result['argv'] == argv and result['cwd'] == str(ROOT) and result['environment'] == TERM_ENV and
       result['inputs_before'] == result['inputs_after'] == inputs and result['inputs_unchanged'] is True and
       result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 0 and
       result['timed_out'] is False and result['wait_error'] is None and result['cleanup_events'] == [] and
       result['child_reaped'] is result['process_group_absent'] is result['paper_terminal_present_after'] is True and
       type(result['pid']) is int and result['pid'] > 0 and
       attempt['started_epoch'] <= spawn['spawned_epoch'] <= result['finished_epoch'] and
       spawn == dict(pid=result['pid'], process_group_id=result['pid'], spawned_epoch=spawn['spawned_epoch']) and
       not os.path.lexists(directory / 'unused_receiver_cache'),
       'entire actual documentary native wait-zero settled process/time and exact input interval')
    ck(result['stdout'] == val(directory / 'ROOT_RECEPTION.json') and
       result['stderr'] == val(directory / 'stderr') and raw(directory / 'stderr') == b'',
       'entire actual independent receiver captured stdout and empty stderr')
    data = obj(directory / 'ROOT_RECEPTION.json')
    ck(data['status'] == 'PASS_P210_TERMINAL_BUILD_ORIGINAL_DOCUMENTS_ONLY' and data['root_acceptance'] is False and
       data['new_science_executions'] == data['new_builds'] == data['new_views'] == data['manuscript_reviews'] == 0 and
       data['checks'] == 533864 and data['current_path_keys'] == 125499 and
       data['original_payloads'] == 222 and data['original_commands'] == 33 and data['original_inputs'] == 1619 and
       data['raw_documentary_pairs'] == 17, 'actual full original receiver report documentary-only scope')
    launch = obj(QA / 'P210_TERMINAL_RECEIVER01_ROOT_LAUNCH.actual.json')
    completion = obj(QA / 'P210_TERMINAL_RECEIVER01_ROOT_COMPLETION.actual.json')
    ck(shlex.split(launch['command']) == ['/usr/bin/python3.10', '-I', '-S', '-B', str(source),
       '--expected-receiver-preparation-sha256', val(prep / 'SHA256SUMS')['sha256']] and launch['cwd'] == str(ROOT) and
       launch['result']['session_id'] == completion['session_id'] == 91772 and launch['result']['output'] == '' and
       completion['launch_record'] == 'P210_TERMINAL_RECEIVER01_ROOT_LAUNCH.actual.json' and
       completion['result']['exit_code'] == 0,
       'actual parent recorder command/session and normal native completion, no invented environment or stderr')
    expected_return = dict(status='PASS_ACTUAL_P210_TERMINAL_RECEPTION_CAPTURE', output=str(directory),
        original_wait_exit_code=0, stdout=result['stdout'], stderr=result['stderr'], result=val(directory / 'RESULT.json'),
        seal=val(directory / 'SHA256SUMS'), original_input_count=data['original_inputs'],
        current_path_keys=data['current_path_keys'], terminal_acceptance=False)
    ck(completion['result']['output'] == json.dumps(expected_return, sort_keys=True) + '\n',
       'entire actual parent native raw receiver capture return')
    return data, dict(parent_session=91772, original_native_exit=0, captured_receiver_input_keys=8,
        captured_payloads=6, original_documentary_checks=data['checks'], raw_stdout=val(directory / 'ROOT_RECEPTION.json'),
        own_root_acceptance=False, full_map_independently_reconstructed_later=True)


def bind_actual_terminal_documents(contract):
    # Read real normal parent closures BEFORE hashing their output packages.
    # Neither a caller boolean nor a stored author PASS grants acceptance.
    for stem, session in (('OUTER02', 91983), ('RECEIVER01', 91772),
                          ('CAPTURE_ROOT_READ', 88422), ('LIFECYCLE_REFRESH', 94702)):
        name = 'P210_TERMINAL_' + stem + ('_' if stem == 'CAPTURE_ROOT_READ' else '_ROOT_')
        launch = obj(QA / (name + 'LAUNCH.actual.json'))
        completed = obj(QA / (name + 'COMPLETION.actual.json'))
        ck(launch['result']['session_id'] == completed['session_id'] == session and
           launch['result']['output'] == '' and 'exit_code' not in launch['result'] and
           completed['launch_record'] == name + 'LAUNCH.actual.json' and
           completed['result']['exit_code'] == 0 and 'session_id' not in completed['result'] and
           launch['cwd'] == str(ROOT), 'actual normal parent closure before any corresponding capture-stream hash')
    spec = contract['terminal']
    ck(spec == dict(output=str(PAPER / 'qa_final'), preparation=str(QA / 'p210_terminal_build_revision_02'),
       preparation_seal={'sha256': '2e99af39ab35bfb9e3fec7c9944927c574fe459b56a1b764a5948dde0266e31a', 'bytes': 793},
       preparation_payloads=9,
       output_seal={'sha256': '659b493dbc4e84137cf873643c1673b725294455d057c62b41e82572ffd31fd1', 'bytes': 22762},
       output_payloads=222, root_receiver_result_path=str(QA / 'p210_terminal_root_reception_01/ROOT_RECEPTION.json'),
       root_receiver_capture_seal={'sha256': '1037dc53ebff5fdd4ebfec909ce408c9c401589b9ac6a9e1993b6faacbf215e2', 'bytes': 478}),
       'entire actual final terminal role contract, no future schema or prefix fallback')
    actual_native, outer = actual_terminal_outer()
    receiver, captured = actual_terminal_receiver_capture(contract)
    views = actual_six_root_views()
    accepted = obj(QA / 'P210_TERMINAL_ROOT_ACCEPTANCE.actual.json')
    ck(accepted['schema'] == 'p210-root-terminal-build-view-acceptance-v1' and
       accepted['status'] == 'ROOT_ACCEPTED_P210_TERMINAL_BUILDS_AND_ALL_SIX_VIEWS' and
       accepted['paper'] == 'P210' and accepted['root'] == '/root' and
       accepted['receiver_source_fully_read'] is accepted['receiver_original_capture_accepted'] is
       accepted['root_original_inspection_complete'] is True and
       accepted['receiver_native_session'] == 91772 and accepted['receiver_native_exit'] == 0 and
       accepted['receiver_documentary_checks'] == receiver['checks'] and
       accepted['root_reception_native_session'] == 88422 and accepted['root_reception_native_exit'] == 0 and
       accepted['root_reception_checks'] == 250068 and
       accepted['current_path_keys'] == receiver['current_path_keys'] and
       accepted['known_original_paths'] == receiver['current_key_reconstruction']['known_original_paths'] and
       accepted['disjoint_current_extras'] == receiver['current_key_reconstruction']['extra_count'] and
       accepted['complete_current_map'] == receiver['current_key_reconstruction']['complete_map'] and
       accepted['terminal_manifest_sha256'] == spec['output_seal']['sha256'] and accepted['terminal_payloads'] == 222 and
       accepted['terminal_native_commands'] == 33 and accepted['terminal_builds'] == 2 and
       accepted['actual_root_viewed_pages'] == views['pages_actually_viewed_by_root'] == 6 and
       accepted['open_visual_findings'] == 0 and accepted['pdf'] == val(PAPER / 'qa_final/cold_build_1/main.pdf') and
       accepted['raw_both_pdfs_equal_accepted_round2'] is True and
       accepted['new_scientific_runs'] == accepted['new_manuscript_reviews'] == 0 and
       accepted['paper_completion'] is accepted['five_paper_completion'] is False and
       accepted['external'] == 'OWNER_AMBER / HOLD_EXTERNAL' and 'ARTIFACT_GATE_PENDING' in accepted['next'],
       'entire actual root terminal and six-view acceptance retains paper/five pending scope')
    ck(len(accepted['input_pins']) == 13, 'all actual formal root terminal acceptance inputs')
    for path, value in accepted['input_pins'].items():
        ck(contract['named_input_pins'][path] == value, 'actual acceptance input pin explicitly bound by final contract')
        pin(path, sha_record(value))
    root_source = QA / 'receive_p210_terminal_root_capture.py'
    pin(root_source, '753a6f22edfc3869f93243f69a2b88902129bad4276f8006ab3a0a9c800e588d')
    root_launch = obj(QA / 'P210_TERMINAL_CAPTURE_ROOT_READ_LAUNCH.actual.json')
    root_completed = obj(QA / 'P210_TERMINAL_CAPTURE_ROOT_READ_COMPLETION.actual.json')
    expected_root = dict(status='PASS_ROOT_P210_TERMINAL_CAPTURE_ORIGINAL_RECEPTION', checks=250068,
        current_path_keys=receiver['current_path_keys'], known_original_paths=accepted['known_original_paths'],
        disjoint_extras=accepted['disjoint_current_extras'], reconstructed_current_map=accepted['complete_current_map'],
        receiver_raw=val(spec['root_receiver_result_path']), receiver_seal=spec['root_receiver_capture_seal'],
        native_session=91772, native_completion_chunk='0317d6', terminal_seal=spec['output_seal'],
        original_terminal_builds=2, original_actual_root_views=6, new_science_executions=0, new_builds=0, new_views=0,
        paper_completion=False, five_paper_completion=False)
    ck(shlex.split(root_launch['command']) == ['/usr/bin/python3.10', '-I', '-S', '-B', str(root_source)] and
       root_completed['result']['output'] == json.dumps(expected_root, sort_keys=True) + '\n',
       'entire actual separately source-read root original reception command and native stdout')
    refresh_source = QA / 'refresh_p210_terminal_whole_manifest.py'
    refresh_launch = obj(QA / 'P210_TERMINAL_LIFECYCLE_REFRESH_ROOT_LAUNCH.actual.json')
    refresh_completed = obj(QA / 'P210_TERMINAL_LIFECYCLE_REFRESH_ROOT_COMPLETION.actual.json')
    refresh = obj(QA / 'P210_TERMINAL_LIFECYCLE_REFRESH.actual.json')
    ck(shlex.split(refresh_launch['command']) == ['/usr/bin/python3.10', '-I', '-S', '-B', str(refresh_source)] and
       refresh_completed['result']['output'] == json.dumps({key: value for key, value in refresh.items()
          if key != 'native'}, sort_keys=True, indent=2) + '\n' and
       refresh['new_lifecycle_sha256'] == contract['pending_lifecycle']['lifecycle_pin']['sha256'] and
       refresh['new_whole_sha256'] == contract['pending_lifecycle']['whole_manifest_pin']['sha256'],
       'entire actual first pending refresh parent command and native stdout, not future complete lifecycle')
    # Genuine link targets are separately consumed by the pending whole branch.
    for name in ('P210_TERMINAL_BUILD_ROOT_INSPECTION.md', 'P210_TERMINAL_ROOT_VIEWS.md'):
        body = raw(QA / name).decode()
        ck('HOLD_EXTERNAL' in body, 'actual bounded root documentary report external hold')
        for href in stripped_links(body):
            relative = href.strip().strip('<>').split('#', 1)[0]
            if relative and not re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', relative):
                target = (QA / unquote(relative)).resolve()
                ck(target.is_relative_to(ROOT) and target.is_file(), 'genuine actual root report local link')
                pin(target)
    return receiver, dict(actual_native=actual_native, original_outer=outer, original_receiver_capture=captured,
        actual_six_root_views=views, root_acceptance_record=val(QA / 'P210_TERMINAL_ROOT_ACCEPTANCE.actual.json'),
        root_original_reception=expected_root, first_pending_refresh_parent_session=94702,
        terminal_builds_and_views_accepted=True, paper_completion=False, five_paper_completion=False)


def main():
    ck(len(sys.argv) == 3 and sys.argv[1] == '--expected-preparation-sha256' and
       re.fullmatch('[0-9a-f]{64}', sys.argv[2]) is not None, 'explicit final root-reviewed preparation seal')
    before_runtime = current_reader_runtime()
    # Root's capture directory may already exist and contain its own open
    # stdout/stderr. This reader never creates/writes/seals that directory.
    rows = complete_package(PREP, sys.argv[2], len(manifest_rows(PREP / 'SHA256SUMS')))
    ck('ACTUAL_BINDING.json' in rows and 'SOURCE_INHERITANCE.json' in rows,
       'final actual bound source package not prior unbound design')
    contract = obj(PREP / 'ACTUAL_BINDING.json')
    ck(contract['schema'] == 'p210-terminal-artifact-actual-binding-v1' and
       contract['stage'] == 'ACTUAL_TERMINAL_ROOT_VIEWS_AND_FIRST_PENDING_LIFECYCLE_BOUND' and
       contract['paper'] == 'P210' and contract['root_acceptance'] is False,
       'actual first-artifact input contract never grants this reader root acceptance')
    complete_package(PRIOR, '408485bb7f50b7fa90879e9914547cf62ac140e452e136a42f7d65f3f391ec44', 10)
    original_roles = obj(PRIOR / 'ACTUAL_ROLES.json')
    ck(original_roles['schema'] == 'p210-terminal-artifact-unbound-actual-role-capture-v1' and
       original_roles['stage'] == 'UNBOUND_DESIGN_ONLY' and original_roles['reader_executed_or_imported'] is False and
       len(original_roles['named_actual_file_keys']) == 217, 'original unbound role capture preserved as data only')
    actual_history_roles(original_roles)
    # The ten actual documentary aliases are registered first, but no old
    # host map or broad membership is consumed before actual terminal binding.
    actual_receiver, bound_terminal = bind_actual_terminal_documents(contract)
    for path, value in original_roles['named_actual_file_keys'].items():
        historical_record(path, value)
    for path, value in contract['named_input_pins'].items():
        pin(historic_hash_path(path, value['sha256']), sha_record(value))
    author = manifest_rows(PAPER / 'AUTHOR_MANIFEST.sha256')
    ck(len(author) == 489 and pin(PAPER / 'AUTHOR_MANIFEST.sha256')['sha256'] == AUTHOR_SEAL and
       pin(PAPER / 'SHA256SUMS')['sha256'] == AUTHOR_SEAL, 'both immutable original489 author seal spellings')
    for name, value in author.items():
        pin(PAPER / name, value)
    reviews = accepted_reviews()
    strict = [strict_pair(role, original_roles) for role in ('author', 'a', 'b')]
    b_reuse = b_complete_reuse(original_roles, reviews)
    r0, old = round0_closure(author)
    r1, links1 = successive_round(1, r0, old['links'], old['external_input_pins'], reviews)
    r2, links2 = successive_round(2, r1, links1, old['external_input_pins'], reviews)
    refresh = actual_round2_lifecycle_refresh()
    failure_history = terminal_failed_attempt_and_preflight()
    terminal = terminal_build_package(contract['terminal'], actual_receiver)
    ck(terminal['expected_native'] == bound_terminal['actual_native'],
       'entire reconstructed terminal native argv cwd exit and raw streams equal actual root-bound originals')
    pending = current_pending_whole_and_links(contract, terminal)
    runtime = current_reader_runtime()
    ck(before_runtime['environment'] == runtime['environment'] and before_runtime['argv'] == runtime['argv'],
       'current documentary reader runtime invocation remains unchanged')
    complete = final_current_closure()
    complete['b_final_basis'] = original_roles['actual_b_final_map_recipe']
    complete['terminal_receiver_basis'] = dict(path=contract['terminal']['root_receiver_result_path'],
        pin=contract['named_input_pins'][contract['terminal']['root_receiver_result_path']],
        selector=['current_key_reconstruction'], original_map=actual_receiver['current_key_reconstruction']['complete_map'])
    # All underlying original recipes/maps and every new extra are emitted or
    # exactly referenced. No reconstructed full host ledger is copied to disk.
    report = dict(schema='p210-terminal-artifact-reader-revision-01',
        status='PASS_P210_TERMINAL_ARTIFACT_INITIAL_LIFECYCLE_FOLLOWUP_PENDING', paper='P210',
        checks=sum(CHECKS.values()), checks_by_kind=dict(CHECKS),
        complete_current_key_reconstruction=complete,
        accepted_reviews={role: {key: value for key, value in row.items() if key in
            {'reviewer', 'final_payloads', 'initial_payloads_preserved', 'current_open'}} for role, row in reviews.items()},
        actual_strict_pairs_reused=strict, actual_B_full_reuse=b_reuse,
        physical_frozen_payloads=[len(r0), len(r1), len(r2)], physical_frozen_link_roles=[len(old['links']), len(links1), len(links2)],
        actual_round2_document_only_refresh=refresh, failed_terminal_attempt_and_preflight=failure_history,
        actual_terminal_reused={key: value for key, value in terminal.items() if key != 'expected_native'},
        actual_root_terminal_and_view_binding={key: value for key, value in bound_terminal.items() if key != 'actual_native'},
        pending_lifecycle_and_whole=pending, full_raw_comparisons=dict(BYTE_COMPARISONS),
        original_native_records_rechecked=len(NATIVE_RECORDS) + len(NATIVE), current_reader_runtime=runtime,
        new_scientific_runs=0, new_builds=0, new_views=0, new_manuscript_reviews=0,
        old_programs_imported_or_executed=0, reader_file_writes=0, root_acceptance=False,
        paper_completion=False, five_paper_completion=False, external='OWNER_AMBER / HOLD_EXTERNAL',
        limits=['Actual old author/A/B science, two builds and six root page views are reused under complete current keys; none rerun here.',
            'Previous resolved findings, missing histories, first failed unsealed terminal attempt and every older failure remain preserved.',
            'Sampled runtime/open/FLS/ldd evidence is not continuous startup, child-map, transient-dlopen, non-FLS or OS tracing.',
            'A separate actual root reception and exact post-artifact lifecycle/whole transition plus follow-up remain required.'])
    print(json.dumps(report, sort_keys=True, separators=(',', ':'), ensure_ascii=True))


if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print(json.dumps(dict(status='FAIL_P210_TERMINAL_ARTIFACT_NO_ACCEPTANCE',
            checks_completed=sum(CHECKS.values()), traceback=traceback.format_exc(),
            reader_file_writes=0, new_scientific_runs=0, new_builds=0, new_views=0,
            root_acceptance=False, paper_completion=False, five_paper_completion=False), sort_keys=True))
        raise SystemExit(1)
