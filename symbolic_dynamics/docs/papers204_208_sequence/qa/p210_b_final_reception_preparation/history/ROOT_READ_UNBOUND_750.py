#!/usr/bin/env python3
"""Prepared root read-only P210 B final reception; preparer MUST NOT execute.

No original writer, receiver, science, build or native command is imported or
executed. Final bindings are unavailable until the same reviewer's real final
decision, phase results, completed native receipts and non-self seal exist.
"""
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
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_b_final_reception_preparation'
B = QA.parent / 'reviews/p210_b'
H = B / 'history/initial_before_delta'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
FROZEN = PAPER / 'frozen_round1'
PAIR = QA / 'root_replays/p210_b_strict_pair_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PY_PATH = ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload']
INITIAL = '81b5f97a6b25d6f9e82db87001da1a54668c01268038694d4b8a3b61006b02c3'
OLD_DELTA = '6b59ce7b8f12206a5fe9f761e1aa1d3990c8fa66451961cd9645db63d5d9d618'
RESPONSE = '10d856f1c5b0ab7aa12229c9b4262b6888b439bacaa28b0374483f9a60cf12c7'
ALIASES = {str(B / 'DELTA.md'): (H / 'DELTA.md', OLD_DELTA),
           str(B / 'SHA256SUMS'): (H / 'SHA256SUMS', INITIAL)}
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
BASE_CONFIG_ROOTS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/lib/locale/C.utf8',
                                  '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv')))
BUILD_CONFIG_ROOTS = tuple(map(Path, ('/usr/local/share/texmf', '/root/texmf',
    '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var',
    '/usr/local/share/fonts', '/root/.fonts', '/root/.fontconfig',
    '/root/.config/fontconfig', '/root/.cache/fontconfig', '/root/.local/share/fonts',
    '/etc/xdg/fontconfig', '/etc/profile.d')))
TREE_ROOTS = tuple(map(Path, ('/usr/lib/python3.10', '/usr/lib/locale', '/usr/lib/x86_64-linux-gnu/gconv')))
BUILD_TREE_ROOTS = tuple(map(Path, ('/etc/texmf', '/var/lib/texmf', '/usr/share/texlive/texmf-dist',
    '/usr/share/texmf', '/etc/fonts', '/usr/share/fontconfig', '/var/cache/fontconfig',
    '/usr/share/poppler', '/usr/share/fonts')))
DATA_ROOTS = tuple(map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')))
STDLIB = Path('/usr/lib/python3.10')
CHECKS, SEEN, USED, MANIFESTS, LINKS, NATIVE = Counter(), {}, set(), [], [], []

def ck(ok, label, detail=''):
    CHECKS[label] += 1
    if not ok:
        raise AssertionError((label, detail))

def need(ok, label):
    ck(ok, 'strict_helper', label)

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

def rich(row):
    ck(set(row) in ({'real','sha256','size','symlink'}, {'resolved','sha256','bytes','symlink'}),
       'exact_complete_rich_key_schema', sorted(row))
    return {'real': row.get('real', row.get('resolved')), 'sha256': row['sha256'],
            'size': row.get('size', row.get('bytes')), 'symlink': row['symlink']}

def historical(path, expected):
    name = str(path)
    if name in ALIASES:
        selected, digest = ALIASES[name]
        ck(expected['sha256'] == digest, 'only_exact_initial_documentary_alias', name)
        old = rich(expected) if 'symlink' in expected else None
        if old is not None:
            ck(old['real'] == name and old['symlink'] is None, 'historical_logical_metadata', name)
        size = expected.get('size', expected.get('bytes'))
        row = pin(selected, {'sha256': digest, 'bytes': size})
        ck(row['real'] == str(selected) and row['symlink'] is None, 'physical_historical_copy', name)
        USED.add(name)
        return row
    return pin(path, rich(expected) if 'symlink' in expected else expected)

def rows(path):
    body = raw(path)
    ck(body.endswith(b'\n'), 'manifest_complete_newline', str(path))
    result = {}
    for line in body.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(match is not None, 'manifest_exact_row', str(path))
        digest, name = match.groups()
        p = Path(name)
        ck(p.parts and not p.is_absolute() and '..' not in p.parts and p.as_posix() == name
           and name not in result, 'manifest_safe_unique_path', name)
        result[name] = digest
    return result

def manifest(base, path, expected, count, complete=False, old=False):
    pin(path, expected)
    result = rows(path)
    ck(len(result) == count, 'manifest_exact_census', str(path))
    for name, digest in result.items():
        target = base / name
        historical(target, {'sha256': digest}) if old else pin(target, digest)
    if complete:
        ck(path.parent == base and path.name not in result and set(result) == physical(base) - {path.name},
           'entire_nonself_physical_membership', str(base))
    MANIFESTS.append({'path': str(path), 'base': str(base), 'payloads': count, 'old_roles': old,
                      'complete_nonself': complete, **val(path)})
    return result

def canonical_digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def actual_root(stem, expected, identity):
    launch = obj(QA / (stem + '_LAUNCH.actual.json'))
    completion = obj(QA / (stem + '_COMPLETION.actual.json'))
    ck(launch['result']['output'] == '' and launch['result']['session_id'] == completion['session_id'] == expected['session']
       and completion['launch_record'] == stem + '_LAUNCH.actual.json', 'original_complete_root_launch', stem)
    ret = completion['result']
    ck(type(ret['exit_code']) is int and ret['exit_code'] == 0 and 'Warning: truncated' not in ret['output'],
       'original_root_native_exit_and_full_output', stem)
    ck(shlex.split(launch['command']) == expected['command_argv'], 'exact_original_root_command', stem)
    data = json.loads(ret['output'])
    ck(data['status'] == expected['status'] and data[identity] == expected['identity'], 'original_root_exact_schema', stem)
    return data

def initial_preservation(initial, final):
    ck(set(initial) <= set(final) and {n for n in initial if initial[n] != final[n]} == {'DELTA.md'},
       'only_initial_DELTA_changed')
    projected = {str((H / n if n == 'DELTA.md' else B / n).relative_to(ROOT)): digest
                 for n, digest in initial.items()}
    projected[str((H / 'SHA256SUMS').relative_to(ROOT))] = INITIAL
    ck(rows(B / 'INITIAL_PRESERVED_PINS.sha256') == projected, 'all_408_ROOT_relative_initial_pins')
    original = obj(B / 'INITIAL_PRESERVATION.actual.json')
    expected_rows = []
    for name, digest in sorted(initial.items()):
        p = H / name if name == 'DELTA.md' else B / name
        expected_rows.append({'initial_name': name, 'original_path': str(B / name),
                              'physical_path': str(p), 'sha256': digest, 'bytes': pin(p)['size']})
    expected_rows.append({'initial_name': 'SHA256SUMS', 'original_path': str(B / 'SHA256SUMS'),
                         'physical_path': str(H / 'SHA256SUMS'), **val(H / 'SHA256SUMS')})
    ck(original['roles'] == expected_rows and original['status'] == 'INITIAL_PHYSICALLY_PRESERVED_BEFORE_DELTA_REPLACEMENT'
       and original['initial_payloads'] == 407 and original['complete_preserved_roles_including_seal'] == 408
       and original['unchanged_in_place_payloads_after_future_delta_replacement'] == 406
       and original['accepted_delta'] is False and original['current_DELTA_still_initial'] is True
       and original['current_seal_still_initial'] is True, 'actual_complete_pre_replacement_record')
    pin(B / 'REPORT.md', 'd2d42801e61ef278affc16af6659ba708bf5dec0ca7585b3cb1cf5d738877dfb')
    pin(B / 'FINDINGS.json', '0db9eea2a59a6bfb01b5ce3dbd57c84aa2cb84ab4ac952e2a72829a3f56f5bbb')
    return original

def old_reception(binding, initial):
    audit = obj(B / 'AUDIT_INPUTS.actual.json.gz')
    ck(len(audit) == 120840, 'entire_original_B_120840')
    for name, expected in audit.items():
        historical(name, expected)
    root = actual_root('P210_B_INITIAL_ORIGINALS_ROOT', binding['root_native']['P210_B_INITIAL_ORIGINALS_ROOT'], 'checks')
    extra = root['extra_read_keys_not_in_B_audit_ledger']
    ck(len(extra) == 55 and not set(audit) & set(extra), 'exact_55_initial_extra_roles')
    ck(canonical_digest(audit | extra) == root['all_current_read_keys_canonical_json_sha256']
       == '6e1c3750bfbb413ea077daca5ddb9e18d6eeabef9616b1e118def449c2c0c9ef'
       and root['all_current_read_keys_count'] == 120895, 'reconstructed_entire_initial_root_map')
    for name, expected in extra.items():
        historical(name, expected)
    ck(root['B_named_keys_fully_read_twice'] == 120840 and root['native_originals_bound'] == 63
       and root['full_python_raw_comparisons'] == 515 and root['accepted_delta'] is False,
       'accepted_initial_scope_preserved')
    ledgers, scopes = {}, {}
    for label in ('produce01','pair01','build01','build02'):
        ledger = obj(B / label / 'INPUTS_BEFORE.json.gz')
        if label != 'build01':
            ck(ledger == obj(B / label / 'INPUTS_AFTER.json.gz'), 'entire_original_B_ledger_interval', label)
        ck(ledger['membership'] == sorted(ledger['files']), 'original_exact_membership_array', label)
        for name, expected in ledger['files'].items():
            historical(name, expected)
        ledgers[label] = ledger
        scopes[label] = current_membership(ledger, label.startswith('build'))
    known = obj(PAIR / 'INPUTS_BEFORE.json')
    ck(known == obj(PAIR / 'INPUTS_AFTER.json') and len(known) == 3558, 'all_strict_original_rich_keys')
    for name, expected in known.items():
        historical(name, expected)
    strict = actual_root('P210_B_STRICT_ORIGINALS_ROOT', binding['root_native']['P210_B_STRICT_ORIGINALS_ROOT'], 'checks')
    extra = strict['extra_read_keys_outside_original_known_ledger']
    ck(len(extra) == 75 and not set(extra) & set(known), 'exact_75_strict_extra_roles')
    projected = {n: {k:v[k] for k in ('sha256','bytes')} for n,v in known.items()} | extra
    ck(len(projected) == 3633 and canonical_digest(projected) == strict['read_ledger_sha256']
       == '21a8c5c38511712b73b12485e9f7182fbb2b34b31f958d1a1c264ab0ccf26037',
       'entire_actual_strict_receiver_map')
    for name, expected in extra.items():
        historical(name, expected)
    manifest(PAIR, PAIR / 'SHA256SUMS', '54cdd8ca9a00374f53a82e7f84a47fdd91f3fcde8b1519b027b98c7925ace181', 59, True)
    resources = obj(PAIR / 'RESOURCE_NAMES_BEFORE.json')
    conf = obj(PAIR / 'CONFIGURATION_BEFORE.json')
    ck(resources == obj(PAIR / 'RESOURCE_NAMES_AFTER.json') == current_resources() and len(resources) == 3121,
       'strict_full_resource_membership_now')
    ck(conf == obj(PAIR / 'CONFIGURATION_AFTER.json') == configuration_snapshot() and len(conf) == 41,
       'strict_exact_reconstructed_configuration_now')
    ck(USED == set(ALIASES), 'only_both_exact_initial_aliases_used')
    return audit, known, ledgers, scopes, resources, conf, root, strict

def nochange_reception(binding, initial):
    data = actual_root('P210_B_EXACT_NOCHANGE', binding['root_native']['P210_B_EXACT_NOCHANGE'], 'checks')
    definitions = [('round1', FROZEN, 'SHA256SUMS', 508, True),
        ('round0', PAPER / 'frozen_round0', 'SHA256SUMS', 493, True),
        ('author', PAPER, 'AUTHOR_MANIFEST.sha256', 489, False),
        ('whole', PAPER, 'PAPER_MANIFEST.sha256', 1496, True)]
    names = {str(QA / 'check_p210_b_response.py'), str(B / 'SHA256SUMS')} | {str(B / n) for n in initial}
    manifests = {'review': initial}
    for role, base, name, count, complete in definitions:
        manifests[role] = manifest(base, base / name, data['seals'][role], count, complete)
        names.add(str(base / name)); names.update(str(base / n) for n in manifests[role])
    result = {}
    for name in names:
        key = historical(name, {'sha256': ALIASES[name][1]}) if name in ALIASES else pin(name)
        ck(key['symlink'] is None, 'physical_original_nochange_input', name)
        result[name] = {'resolved': name, 'symlink': None, 'bytes': key['size'], 'sha256': key['sha256']}
    ck(len(result) == data['current_paths_reread'] == 1906 and canonical_digest(result) == data['complete_key_digest']
       == '7f7abc5e77795069dfbaa5ba06275af4719793a45618042a664fc5fa9018d06c',
       'entire_exact_old_nochange_map')
    expected = {str((FROZEN / n).relative_to(ROOT)): h for n,h in manifests['round1'].items()}
    expected[str((FROZEN / 'SHA256SUMS').relative_to(ROOT))] = data['seals']['round1']
    ck(rows(B / 'INPUT_PINS.sha256') == expected, 'all_509_actual_reviewed_Round1_inputs')
    return data

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

def delta_native(label, expected):
    directory = B / 'native' / label
    attempt, result = obj(directory / 'ATTEMPT.json'), obj(directory / 'RESULT.json')
    ck(set(attempt) == {'argv','cwd','environment','started_epoch','timeout_seconds','launcher_source','executable'},
       'exact_delta_native_attempt_schema', label)
    ck(set(result) == set(attempt) | {'ended_epoch','native_returncode','pid','owned_pgid','owned_sid','settlement','stdout','stderr'},
       'exact_delta_native_result_schema', label)
    ck(attempt['argv'] == expected['argv'] and attempt['cwd'] == str(ROOT) and attempt['environment'] == ENV
       and attempt['timeout_seconds'] == 600 and all(result[k] == v for k,v in attempt.items()),
       'all_exact_delta_prestart_fields_retained', label)
    ck(type(result['native_returncode']) is int and result['native_returncode'] == expected['native_returncode']
       and isinstance(attempt['started_epoch'], (int,float)) and isinstance(result['ended_epoch'], (int,float))
       and result['ended_epoch'] >= attempt['started_epoch'], 'actual_delta_native_exit_and_chronology', label)
    owner = result['pid']
    ck(type(owner) is int and owner > 0 and result['owned_pgid'] == result['owned_sid'] == owner
       and result['settlement'] == {'quiescent': True, 'remaining_members': []},
       'actual_delta_owned_settled_group', label)
    pin(B / 'launch_command.py', attempt['launcher_source'])
    pin(attempt['argv'][0], attempt['executable'])
    for stream in ('stdout','stderr'):
        pin(directory / stream, result[stream])
    ck(raw(directory / 'stderr') == b'', 'complete_successful_delta_empty_stderr', label)
    for token in attempt['argv']:
        if token.startswith('pycache_prefix='):
            cache = Path(token.split('=', 1)[1])
            ck(cache.is_absolute() and not os.path.lexists(cache), 'actual_absent_delta_cache', str(cache))
    return attempt, result, obj(directory / 'stdout')

def runtime_record(path, native_argv, common, known):
    interval = obj(path)
    ck(set(interval) == {'before','after'}, 'entire_actual_delta_runtime_interval', str(path))
    consumed = set()
    for phase, sample in interval.items():
        ck(set(sample) == {'argv','cwd','environment','executable','flags','modules','proc_maps','pycache_prefix','scope','sys_path'},
           'exact_actual_delta_runtime_schema', phase)
        ck(sample['argv'] == native_argv and sample['cwd'] == str(ROOT) and sample['environment'] == ENV
           and sample['executable'] == '/usr/bin/python3.10' and sample['sys_path'] == PY_PATH
           and sample['pycache_prefix'] == native_argv[5].split('=',1)[1]
           and not os.path.lexists(sample['pycache_prefix']), 'actual_delta_runtime_identity', phase)
        ck(all(token in sample['flags'] for token in ('optimize=0','isolated=1','no_site=1','dont_write_bytecode=1'))
           and sample['scope'] == 'before/after file-backed module/maps, not OS/startup or continuous tracing',
           'bounded_actual_source_only_runtime_scope', phase)
        names = {name for name in sample['modules'].values() if name}
        for line in sample['proc_maps'].splitlines():
            fields = line.split(None, 5)
            if len(fields) == 6 and fields[5].startswith('/'):
                ck(not fields[5].endswith(' (deleted)'), 'no_deleted_recorded_delta_map')
                names.add(fields[5])
        for name in names:
            p = Path(name)
            ck(p.is_absolute() and p.suffix not in {'.pyc','.pyo'} and name in common,
               'every_actual_delta_module_and_raw_map_in_common_keys', name)
            ck(p.is_relative_to(B) or str(p.resolve()) in known, 'all_external_delta_runtime_in_strict_known', name)
            pin(name, rich(common[name]))
        consumed.update(names)
    return consumed

def comparisons_record():
    expected = []
    def append(left, right, role):
        expected.append({'left': str(left), 'right': str(right), 'role': role,
                         'method': 'full Python bytes, not another native cmp'})
    copies = obj(PAIR / 'SOURCE_ONLY_INITIAL.json')
    for name, row in copies.items():
        append(row['origin'], row['copy'], 'exact strict source copy')
    for row in obj(PAIR / 'RESULT.json')['commands']:
        if row['argv'][0] == '/usr/bin/cmp':
            append(row['argv'][-2], row['argv'][-1], 'rechecked actual native cmp operands')
    for number in ('01','02'):
        append(PAIR / ('commands/03_verify_' + number + '/stdout.raw'), B / 'CANONICAL.json', 'complete actual strict output')
    append(PAPER / 'SHA256SUMS', PAPER / 'AUTHOR_MANIFEST.sha256', 'unchanged author seal alias')
    append(PAPER / 'AUTHOR_MANIFEST.sha256', FROZEN / 'AUTHOR_MANIFEST.sha256', 'unchanged frozen author seal')
    for name in rows(PAPER / 'AUTHOR_MANIFEST.sha256'):
        append(PAPER / name, FROZEN / name, 'unchanged all author input bytes')
    for name in rows(PAPER / 'frozen_round0/SHA256SUMS'):
        append(PAPER / 'frozen_round0' / name, FROZEN / name, 'unchanged all Round0 core bytes')
    actual = obj(B / 'DELTA_FULL_BYTE_COMPARISONS.actual.json')
    ck(actual == expected and len(actual) == 995, 'all_995_comparison_operands_roles_reconstructed')
    for row in actual:
        ck(raw(row['left']) == raw(row['right']), 'full_Python_raw_comparison_not_native', row['role'])
    return Counter(row['role'] for row in actual)

def final_phase_records(binding, known, audit, ledgers, initial_root, strict_root, scopes):
    common = obj(B / 'DELTA_INPUTS_BEFORE.json.gz')
    after = obj(B / 'DELTA_INPUTS_AFTER.json.gz')
    ck(common == after and len(common) == 121013, 'decoded_entire_121013_common_interval_not_gzip_byte_equality')
    for name, expected in common.items():
        ck(Path(name).is_absolute(), 'absolute_actual_common_physical_path', name)
        pin(name, rich(expected))
    extra = obj(B / 'DELTA_AFTER_EXTRA_INPUTS.actual.json')
    ck(set(extra) == {str(B / n) for n in ('DELTA_INPUTS_BEFORE.json.gz','CURRENT_FINDINGS.json','DELTA.md')}
       and not set(extra) & set(common), 'exact_three_actual_after_only_inputs')
    for name, expected in extra.items():
        pin(name, rich(expected))
    all_phase_keys = common | extra
    native_folders = {p.name for p in (B / 'native').iterdir() if p.is_dir() and p.name.startswith('delta_')}
    ck(native_folders == set(binding['delta_native']), 'all_actual_added_delta_native_commands')
    native_records = {name: delta_native(name, wanted) for name,wanted in binding['delta_native'].items()}
    preserved = native_records['delta_preserve01']
    preservation = obj(B / 'INITIAL_PRESERVATION.actual.json')
    ck(preserved[2] == {'status': preservation['status'], 'initial_payloads': 407, 'all_physical_preserved_roles': 408,
       'preservation_record': val(B / 'INITIAL_PRESERVATION.actual.json'), 'initial_seal': val(H / 'SHA256SUMS'),
       'accepted_delta': False}, 'actual_preservation_complete_native_stdout')
    ck(preserved[0]['started_epoch'] <= preservation['started_epoch'] <= preservation['ended_epoch']
       <= preserved[1]['ended_epoch'], 'actual_preservation_inner_outer_chronology')
    pin(B / 'preserve_initial_delta.py', preservation['source'])
    ck(preservation['argv'] == preserved[0]['argv'] and preservation['cwd'] == str(ROOT) and preservation['environment'] == ENV,
       'actual_preservation_source_runtime')
    expected_aliases = {name: {'physical': str(target), 'sha256': digest,
        'scope': 'exact initial role, not current same-named lifecycle bytes'} for name,(target,digest) in ALIASES.items()}
    projected_scopes = {label: {'files': row['files'], 'configuration': row['configuration'],
        'fixed': row['fixed_named_files'], 'discovered': row['selected_current_tree_files']} for label,row in scopes.items()}
    summaries, role_maps, runtime_names = {}, {}, {}
    for phase in ('before','after'):
        summary = obj(B / ('DELTA_' + phase.upper() + '.actual.json'))
        attempt, result, stdout = native_records['delta_' + phase + '01']
        ck(summary == stdout == binding['phase_summaries'][phase], 'actual_complete_phase_record_and_native_stdout', phase)
        ck(summary['status'] == 'PASS_SAME_B_EXACT_NOCHANGE_DELTA_' + phase.upper() and summary['phase'] == phase
           and attempt['started_epoch'] <= summary['started_epoch'] <= summary['ended_epoch'] <= result['ended_epoch'],
           'actual_phase_identity_and_complete_chronology', phase)
        ck(summary['same_reviewer'] == '/root/p210_b_reviewer' and summary['response'] ==
           {'path': str(QA.parent / 'P210_B_RESPONSE.md'), 'sha256': RESPONSE, 'bytes': 4469}
           and summary['exact_initial_aliases'] == expected_aliases and summary['full_physical_input_paths_reread_twice'] == len(common)
           and summary['root_native_wrappers_checked'] == 4 and summary['root_actual_strict_native_commands_checked'] == 10
           and summary['full_Python_byte_comparisons'] == 995 and summary['B_original_reuse_scope'] == projected_scopes,
           'entire_phase_documentary_role_census', phase)
        ck(summary['root_initial_receiver_map'] == initial_root['all_current_read_keys_canonical_json_sha256']
           and summary['root_strict_receiver_map'] == strict_root['read_ledger_sha256']
           and summary['root_nochange_map'] == '7f7abc5e77795069dfbaa5ba06275af4719793a45618042a664fc5fa9018d06c'
           and summary['all_120840_B_reuse_keys_current'] is True and summary['root_checks_each'] == [51129,51129],
           'three_accepted_logical_maps_and_original_box', phase)
        ck(summary['initial_payloads_preserved'] == 407 and summary['unchanged_in_place_initial_payloads_except_delta'] == 406
           and summary['manuscript_changed'] is False and summary['accepted_delta_written_by_this_program'] is False
           and all(summary[k] == 0 for k in ('new_scientific_runs','new_builds','new_views','old_writers_executed'))
           and summary['owner'] == 'OWNER_AMBER' and summary['external'] == 'HOLD_EXTERNAL',
           'actual_non_scientific_non_author_acceptance_boundary', phase)
        ck(summary['historical_unconsumed_PDF_keys_only'] == initial_root['intermediate_unconsumed_pdf_historical_keys_only'],
           'three_unconsumed_old_PDF_keys_only_not_bytes', phase)
        role_maps[phase] = obj(B / ('DELTA_ROLES_' + phase.upper() + '.actual.json'))
        ck(all(v == sorted(set(v)) for v in role_maps[phase].values()), 'all_role_arrays_unique_sorted', phase)
        expected_union = set(common) | (set(extra) if phase == 'after' else set())
        ck(set().union(*map(set,role_maps[phase].values())) == expected_union, 'complete_all_recorded_role_union', phase)
        for name in expected_union:
            pin(name, rich(all_phase_keys[name]))
        runtime_names[phase] = runtime_record(B / ('DELTA_RUNTIME_' + phase.upper() + '.actual.json'), attempt['argv'], common, known)
        ck(set(role_maps[phase]['delta_runtime_module_or_map']) == runtime_names[phase],
           'all_delta_runtime_roles_reconstructed_from_raw_samples', phase)
        summaries[phase] = summary
    ck(summaries['after']['all_common_before_after_keys_equal'] is True
       and summaries['after']['accepted_decision_independently_authored_before_this_check'] is True,
       'actual_after_decision_closure')
    ck(native_records['delta_preserve01'][1]['ended_epoch'] < native_records['delta_before01'][0]['started_epoch']
       and native_records['delta_before01'][1]['ended_epoch'] < native_records['delta_after01'][0]['started_epoch'],
       'complete_preserve_before_after_native_order')
    def selected(names):
        return {str(ALIASES[n][0]) if n in ALIASES else n for n in names}
    expected_roles = {
        'all_120840_original_B_dependency_keys': selected(audit),
        'all_3558_strict_dependency_keys': selected(known),
        'all_55_initial_receiver_extra_keys': selected(initial_root['extra_read_keys_not_in_B_audit_ledger']),
        'all_75_strict_receiver_extra_keys': selected(strict_root['extra_read_keys_outside_original_known_ledger']),
        'all_408_initial_physical_roles': {r['physical_path'] for r in preservation['roles']},
        'old_run_full_dependency_key': selected(set().union(*(set(v['files']) for v in ledgers.values())))}
    for label, names in expected_roles.items():
        ck(all(set(role_maps[p][label]) == names for p in role_maps), 'exact_original_key_role_projection', label)
    for label in set(role_maps['before']) | set(role_maps['after']):
        difference = set(role_maps['after'].get(label, [])) - set(role_maps['before'].get(label, []))
        ck(set(role_maps['before'].get(label, [])) <= set(role_maps['after'].get(label, [])) and difference <= set(extra),
           'only_three_after_inputs_may_extend_roles', label)
    findings, original = obj(B / 'CURRENT_FINDINGS.json'), obj(B / 'FINDINGS.json')
    ck(findings['reviewer'] == '/root/p210_b_reviewer' and findings['same_actual_initial_reviewer'] is True
       and findings['phase'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA' and findings['verdict'] == 'PASS_NARROW'
       and findings['accepted_delta'] is True and findings['root_response_reviewed'] is True
       and findings['accepted_response_sha256'] == RESPONSE and findings['accepted_response_bytes'] == 4469,
       'actual_same_independent_B_current_decision')
    ck(findings['current_open_counts'] == original['current_open_counts'] == {'Critical':0,'Major':0,'Minor':0}
       and findings['current_manuscript_findings'] == original['current_manuscript_findings'] == []
       and findings['reviewer_infrastructure_resolved_counts'] == original['reviewer_infrastructure_resolved_counts']
       == {'Critical':0,'Major':0,'Minor':2} and findings['inherited_A_findings'] == original['inherited_A_findings'],
       'all_current_and_historical_finding_censuses_retained')
    for field in ('id','severity','status','scope','manuscript_change_required'):
        ck([r[field] for r in findings['reviewer_infrastructure_findings']] ==
           [r[field] for r in original['reviewer_infrastructure_findings']], 'all_two_infrastructure_findings_preserved', field)
    ck(findings['root_final_original_reception'] == 'SEPARATE_PENDING_GATE'
       and all(findings[k] == 'NOT_PREGRANTED' for k in ('round2','terminal_acceptance','five_paper_completion'))
       and findings['owner_status'] == 'OWNER_AMBER' and findings['external_status'] == 'HOLD_EXTERNAL',
       'actual_decision_does_not_pregrant_downstream_gates')
    body = raw(B / 'DELTA.md').decode()
    ck('ACCEPTED_EXACT_NOCHANGE_DELTA' in body and RESPONSE in body, 'actual_delta_text_exact_response')
    comparisons = comparisons_record()
    for page in initial_root['intermediate_unconsumed_pdf_historical_keys_only']:
        ck(page['old_bytes_reread'] is False and page['pass_number'] in (1,2,3),
           'original_unconsumed_old_PDF_boundary')
        products = obj(B / ('build02/commands/pass_' + str(page['pass_number']) + '/SOURCE_AFTER.json'))
        ck(products[str(B / 'build02/source/main.pdf')] == page['recorded_key'], 'old_PDF_historical_record_only')
    ck(not any(Path(r['path']).name == 'main.pdf' for r in obj(B / 'build02/FLS_CLOSURE.json')),
       'old_intermediate_PDF_unconsumed_recorder_scope')
    pair_root = actual_root('P210_B_STRICT_ROOT', binding['root_native']['P210_B_STRICT_ROOT'], 'checks_each')
    recorded = obj(B / 'DELTA_ROOT_NATIVE_BINDINGS.actual.json')
    expected_parents = [{'completion': str(QA / (stem + '_COMPLETION.actual.json')),
        'launch': str(QA / (stem + '_LAUNCH.actual.json')), 'native_exit': 0,
        'root_stem': stem, 'session': binding['root_native'][stem]['session']}
        for stem in ('P210_B_INITIAL_ORIGINALS_ROOT','P210_B_STRICT_ROOT','P210_B_STRICT_ORIGINALS_ROOT','P210_B_EXACT_NOCHANGE')]
    groups = [{'label': r['label'], **r['process_group_settlement']} for r in obj(PAIR / 'RESULT.json')['commands']]
    ck(recorded == {'parents': expected_parents, 'strict_native_groups': groups}
       and groups == strict_root['actual_owned_groups'] and len(groups) == 10
       and pair_root['known_inputs'] == 3558, 'all_four_prior_native_parents_and_ten_groups_exact')
    return {'common_keys':len(common), 'after_extra_keys':len(extra), 'delta_native_commands':len(native_records),
        'phase_checks':{p:r['checks'] for p,r in summaries.items()}, 'raw_comparisons':995,
        'comparison_roles':dict(comparisons), 'role_counts':{p:{k:len(v) for k,v in m.items()} for p,m in role_maps.items()}}


def final_seal_reception(binding, initial_root):
    closure = obj(B / 'DELTA_CLOSURE.actual.json')
    ck(closure['status'] == 'PASS_ACCEPTED_SAME_B_DELTA_FINAL_SEAL_GATE'
       and closure['initial_payloads_preserved'] == 407 and closure['initial_unchanged_in_place_except_delta'] == 406
       and closure['common_input_keys'] == 121013 and closure['later_decision_input_keys'] == 3
       and closure['native_record_count'] == 66, 'actual_same_B_final_seal_closure')
    expected_native = sorted(initial_root['native_census'] +
        [{'directory':'native/' + name, 'native_returncode':r['native_returncode']} for name,r in binding['delta_native'].items()],
        key=lambda r:r['directory'])
    current_native = sorted(str(p.parent.relative_to(B)) for p in B.rglob('RESULT.json') if (p.parent / 'ATTEMPT.json').is_file())
    ck(closure['native_records'] == expected_native and current_native == [r['directory'] for r in expected_native]
       and len(expected_native) == 66, 'all_63_original_plus_3_delta_completed_native_records')
    for row in initial_root['native_census']:
        native(B / row['directory'], row['native_returncode'])
    ck(len(NATIVE) == 63 and Counter(r['native_returncode'] for r in NATIVE) == {0:61,1:2},
       'original_two_native_failures_retained_not_relabelled')
    for label, path in [('source',B / 'seal_delta.py'), ('initial_seal',H / 'SHA256SUMS'),
        ('current_findings',B / 'CURRENT_FINDINGS.json'), ('accepted_delta',B / 'DELTA.md'),
        ('accepted_response',QA.parent / 'P210_B_RESPONSE.md'),
        ('before_summary',B / 'DELTA_BEFORE.actual.json'), ('after_summary',B / 'DELTA_AFTER.actual.json')]:
        pin(path, rich(closure[label]))
    ck(closure['no_new_full_host_reaudit_by_sealer'] is True and closure['full_host_keys_checked_twice_in_each_actual_delta_phase'] is True
       and closure['root_final_reception'] == 'SEPARATE_PENDING_GATE'
       and closure['round2_or_terminal_completion'] == 'NOT_PREGRANTED'
       and closure['owner'] == 'OWNER_AMBER' and closure['external'] == 'HOLD_EXTERNAL',
       'actual_sealer_limits_and_downstream_gate_boundary')
    after_native = obj(B / 'native/delta_after01/RESULT.json')
    ck(after_native['ended_epoch'] <= closure['started_epoch'] <= closure['ended_epoch'], 'actual_final_seal_after_completed_phase')
    for doc in sorted(B.glob('*.md')):
        for href in stripped_links(raw(doc).decode()):
            target = href.strip().strip('<>').split('#',1)[0]
            if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
                continue
            path = (doc.parent / unquote(target)).resolve()
            key = pin(path)
            LINKS.append({'document': doc.name, 'href': href, 'physical': str(path),
                'sha256':key['sha256'], 'bytes':key['size'], 'resolved':key['real'], 'symlink':key['symlink']})
    ck(LINKS == closure['links'], 'all_actual_genuine_Markdown_links_accepted_code_stripping_parser')
    external = obj(binding['external_final_seal']['path'])
    ck(external == binding['external_final_seal']['record'], 'exact_complete_external_final_seal_native_record')
    ret = external['result']
    ck(type(ret['exit_code']) is int and ret['exit_code'] == 0 and 'Warning: truncated' not in ret['output'],
       'actual_external_final_seal_native_zero_complete_stdout')
    data = json.loads(ret['output'])
    ck(data['status'] == 'SEALED_ACCEPTED_SAME_B_EXACT_NOCHANGE_DELTA'
       and data['manifest_sha256'] == binding['final_manifest_sha256']
       and data['payloads'] == binding['final_payload_count'] and data['physical_files'] == data['payloads'] + 1
       and data['actual_native_records'] == 66 and data['common_delta_keys'] == 121013
       and data['initial_payloads_preserved'] == 407 and data['unchanged_initial_payloads_in_place_except_delta'] == 406
       and data['current_open'] == {'Critical':0,'Major':0,'Minor':0}
       and data['root_final_reception'] == 'SEPARATE_PENDING_GATE',
       'entire_actual_final_seal_native_output')
    return {'native_records':66,'preserved_native_failures':2,'genuine_local_links':len(LINKS),
            'final_seal_checks':data['checks_including_final_manifest'], 'closure_checks':closure['checks']}


def main():
    started = datetime.now(timezone.utc).isoformat()
    ck(len(sys.argv) == 3 and sys.argv[1] == 'final-B-actual-only' and re.fullmatch('[0-9a-f]{64}', sys.argv[2]),
       'exact_receiver_cli')
    ck(Path(__file__).resolve() == PREP / 'receive_p210_b_final.py' and Path.cwd() == ROOT
       and Path(sys.executable).resolve() == Path('/usr/bin/python3.10'), 'exact_source_interpreter_cwd')
    ck(dict(os.environ) == ENV and sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.optimize == 0
       and sys.dont_write_bytecode and sys.path == PY_PATH
       and sys.pycache_prefix == str(PREP / 'never_created_receiver_cache') and not os.path.lexists(sys.pycache_prefix),
       'isolated_source_only_exact_settings')
    binding = obj(PREP / 'INPUT_BINDINGS.json')
    ck(binding['stage'] == 'ACTUAL_FINAL_SCHEMA_BOUND_NOT_EXECUTED', 'final_schema_binding_required')
    manifest(PREP, PREP / 'SHA256SUMS', sys.argv[2], binding['preparation_payload_count'], True)
    for name, expected in binding['fixed_inputs'].items():
        pin(name, expected)
    final = manifest(B, B / 'SHA256SUMS', binding['final_manifest_sha256'], binding['final_payload_count'], True)
    initial = manifest(B, H / 'SHA256SUMS', INITIAL, 407, False, True)
    preservation = initial_preservation(initial, final)
    audit, known, ledgers, scopes, resources, conf, initial_root, strict_root = old_reception(binding, initial)
    nochange = nochange_reception(binding, initial)
    phases = final_phase_records(binding, known, audit, ledgers, initial_root, strict_root, scopes)
    seal = final_seal_reception(binding, initial_root)
    ck({label: current_membership(ledger,label.startswith('build')) for label,ledger in ledgers.items()} == scopes
       and current_resources() == resources and configuration_snapshot() == conf,
       'full_current_known_membership_and_configuration_second_check')
    reads = dict(SEEN)
    for name, wanted in reads.items():
        pin(name, wanted, force=True)
    ck(physical(B) == set(final) | {'SHA256SUMS'} and USED == set(ALIASES)
       and not os.path.lexists(sys.pycache_prefix), 'final_complete_membership_exact_aliases_and_absent_cache')
    print(json.dumps({'schema':'p210-B-final-root-original-receiver-v1',
        'status':'PASS_ROOT_P210_B_FINAL_SAME_REVIEWER_DELTA_AND_ORIGINAL_RECEPTION',
        'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),
        'source':val(Path(__file__).resolve()),'preparation_seal':val(PREP / 'SHA256SUMS'),
        'checks':sum(CHECKS.values()),'checks_by_kind':dict(CHECKS),
        'physical_paths_fully_reread_twice':len(reads),'complete_current_read_map_canonical_sha256':canonical_digest(reads),
        'B_final_payloads':len(final),'B_final_manifest':val(B / 'SHA256SUMS'),
        'initial_payloads_preserved':407,'initial_unchanged_in_place':406,'initial_roles_including_seal':408,
        'original_B_keys':len(audit),'original_initial_root_extra_keys':55,'strict_rich_known_keys':len(known),
        'original_strict_root_extra_keys':75,'unchanged_paper_map_keys':1906,
        'phase_reception':phases,'final_seal_reception':seal,'current_B_scope_membership':scopes,
        'strict_resource_names':len(resources),'strict_configuration_names':len(conf),
        'exact_two_historical_aliases':{n:{'physical':str(p),'sha256':h} for n,(p,h) in ALIASES.items()},
        'accepted_same_reviewer_delta':True,'current_open':{'Critical':0,'Major':0,'Minor':0},
        'resolved_B_infrastructure_Minor':2,'resolved_inherited_A_Major':1,
        'new_scientific_runs':0,'new_native_child_commands':0,'new_builds':0,'new_page_views':0,
        'old_writers_or_receivers_imported_or_executed':0,'root_acceptance_report_written':False,
        'paper_complete':False,'Round2_accepted':False,'terminal_accepted':False,'five_paper_acceptance':False,
        'scope':'Exact same-B final documentary reception. Previously accepted initial/strict/original gates reused only under full current dependency keys and exact two historical roles. Old unconsumed intermediate PDFs remain historical keys only. No deep expansion of old A host ledgers, no recreated old OS/startup trace.',
        'owner':'OWNER_AMBER','external':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
