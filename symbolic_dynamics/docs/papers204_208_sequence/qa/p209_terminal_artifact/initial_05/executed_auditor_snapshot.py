#!/usr/bin/env python3
"""Read-only P209 terminal artifact auditor, prepared but never pre-accepted.

Disclosed adaptation of the actual accepted P208 artifact infrastructure.
P208 generic integrity functions remain exact; P209-specific roles replace
the old paper/review/runtime/build/link sections. No scientific producer,
old auditor, root recorder or builder is imported or executed. No TeX,
renderer, page-view call, acceptance synthesis or filesystem write occurs.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys
import sysconfig
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
A, B = [BATCH / ('reviews/p209_' + x) for x in ('a', 'b')]
FINAL = PAPER / 'qa_final'
PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_04'
ORIGINAL_PREPARATION = BATCH / 'qa/p209_terminal_artifact_preparation'
OUT = BATCH / 'qa/p209_terminal_artifact'
TERMINAL_PREP = BATCH / 'qa/p209_terminal_preparation'
TERMINAL_LAUNCH = BATCH / 'qa/root_replays/p209_terminal_strict/launcher_terminal_pair_01'
CHECKS, READS, ALIASES, USED_ALIASES, HOST_RESOLUTIONS = Counter(), {}, {}, {}, {}
MANIFESTS, LINKS = [], []
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
BUILD_ENV = {**ENV, 'SOURCE_DATE_EPOCH': '1788652800', 'FORCE_SOURCE_DATE': '1',
             'openin_any': 'p', 'openout_any': 'p'}
TEX_ROOTS = tuple(Path(p) for p in ('/usr/share/texlive/texmf-dist', '/usr/share/texmf',
    '/var/lib/texmf', '/etc/texmf', '/usr/local/share/texmf', '/root/texmf',
    '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var'))
LIB_ROOTS = tuple(Path(p) for p in ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib'))
CONFIG_ROOTS = tuple(Path(p) for p in ('/etc/ld.so.conf.d', '/usr/share/fonts', '/etc/fonts',
    '/var/cache/fontconfig', '/usr/share/fontconfig', '/usr/lib/locale/C.utf8',
    '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/usr/share/poppler',
    '/usr/local/share/fonts', '/etc/xdg/fontconfig', '/etc/profile.d', '/root/.fonts',
    '/root/.fontconfig', '/root/.fonts.conf.d', '/root/.config/fontconfig',
    '/root/.cache/fontconfig', '/root/.local/share/fonts'))
TERMINAL_TOOLS = tuple(Path('/usr/bin') / n for n in ('pdflatex', 'bibtex', 'kpsewhich',
    'pdfinfo', 'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp')) + tuple(
    Path(p) for p in ('/bin/bash', '/bin/sh', '/usr/bin/env', '/usr/bin/python3.10'))
SOURCE_NAMES = ('main.tex', 'math_commands.tex', 'references.bib',
    'sections/00_abstract.tex', 'sections/01_setup.tex', 'sections/02_recurrence.tex',
    'sections/03_inverse.tex', 'sections/04_scope.tex')

def ck(test, section, detail):
    CHECKS[section] += 1
    if not test:
        raise AssertionError((section, detail))


def label(path):
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def read(path):
    path = Path(path)
    ck(path.is_file(), 'regular_file', str(path))
    if path.is_relative_to(ROOT):
        ck(not path.is_symlink(), 'regular_workspace_file', label(path))
    else:
        resolved = str(path.resolve(strict=True))
        ck(str(path) not in HOST_RESOLUTIONS or HOST_RESOLUTIONS[str(path)] == resolved,
           'host_resolution_stability', str(path))
        HOST_RESOLUTIONS[str(path)] = resolved
    raw = path.read_bytes()
    value = {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
    key = str(path)
    ck(key not in READS or READS[key] == value, 'read_stability', key)
    READS[key] = value
    return raw


def j(path):
    return json.loads(read(path))


def h(path):
    return sha256(read(path)).hexdigest()


def safe(base, rel):
    p = Path(rel)
    ck(bool(p.parts) and not p.is_absolute() and '..' not in p.parts,
       'safe_relative_reference', (str(base), rel))
    return base / p


def pin(path, value, historical=False):
    path = Path(path)
    wanted = value if isinstance(value, str) else value['sha256']
    selected = ALIASES.get((str(path), wanted), path) if historical else path
    if selected != path:
        USED_ALIASES[str(path) + ' @ ' + wanted] = str(selected)
    raw = read(selected)
    ck(sha256(raw).hexdigest() == wanted, 'referent_hash', (str(path), str(selected)))
    if isinstance(value, dict) and 'bytes' in value:
        ck(len(raw) == value['bytes'], 'referent_size', str(path))
    return selected


def manifest_rows(path):
    rows = {}
    for line in read(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(match is not None, 'manifest_syntax', str(path))
        digest, rel = match.groups()
        safe(path.parent, rel)
        ck(rel not in rows, 'manifest_duplicate', (str(path), rel))
        rows[rel] = digest
    return rows


def physical(base):
    files = set()
    for p in base.rglob('*'):
        ck(not p.is_symlink(), 'package_no_symlink', label(p))
        if p.is_file():
            files.add(p.relative_to(base).as_posix())
    return files


def manifest(base, name='SHA256SUMS', complete=True, count=None):
    rows = manifest_rows(base / name)
    ck(name not in rows, 'manifest_nonself', label(base))
    if count is not None:
        ck(len(rows) == count, 'manifest_exact_count', (label(base), len(rows), count))
    if complete:
        ck(set(rows) == physical(base) - {name}, 'manifest_full_coverage', label(base))
    for rel, digest in rows.items():
        pin(safe(base, rel), digest)
    MANIFESTS.append({'base': label(base), 'name': name, 'entries': len(rows),
                      'complete_nonself': complete, 'sha256': h(base / name)})
    return rows


def alias(original, preserved, value):
    original, preserved = Path(original), Path(preserved)
    wanted = value if isinstance(value, str) else value['sha256']
    pin(preserved, value)
    key = (str(original), wanted)
    if key in ALIASES:
        ck(read(ALIASES[key]) == read(preserved), 'alias_duplicate_exact_bytes', key)
    else:
        ALIASES[key] = preserved


def maps(record, historical=False):
    for name, value in record.items():
        pin(Path(name) if Path(name).is_absolute() else ROOT / name, value, historical)


def config(record):
    for name, row in record.items():
        p = Path(name)
        ck(p.exists() == row['exists'], 'configuration_existence', name)
        if 'resolved' in row:
            ck(str(p.resolve()) == row['resolved'], 'configuration_resolution', name)
        if 'is_file' in row:
            ck(p.is_file() == row['is_file'], 'configuration_file_kind', name)
        if 'sha256' in row and row['sha256'] is not None:
            pin(p, row)
        elif 'sha256' in row:
            ck(not p.is_file(), 'configuration_explicit_absent_hash', name)


def pair_map(base, stem, historical=False):
    before = j(base / (stem + '_BEFORE.json'))
    ck(before == j(base / (stem + '_AFTER.json')), 'exact_before_after_map', (label(base), stem))
    maps(before, historical)
    return before


def command(base, row, expected_env, allow_stderr=False):
    ck(row['exit_code'] == 0 and row['environment'] == expected_env,
       'actual_command_exit_environment', (label(base), row.get('label', row.get('argv'))))
    argv = row['argv']
    ck(isinstance(argv, list) and argv and '-O' not in argv and '-OO' not in argv,
       'actual_command_argv', label(base))
    for stream in ('stdout', 'stderr'):
        entry = row[stream]
        pin(safe(base, entry['path']), entry)
    if not allow_stderr:
        ck(read(base / row['stderr']['path']) == b'', 'actual_empty_stderr', argv[0])
    if row.get('label'):
        ck(j(base / (row['label'] + '.command.json')) == row,
           'actual_embedded_command_equality', row['label'])
    return argv


def actual_auditor_runtime():
    modules, mapped = {}, {}
    for name, module in sorted(sys.modules.items()):
        original = getattr(module, '__file__', None)
        if original and Path(original).is_file():
            path = Path(original).resolve()
            ck(path.suffix != '.pyc', 'auditor_source_module_not_bytecode', name)
            modules[name] = {'path': str(path), 'sha256': h(path), 'bytes': len(read(path))}
    for line in Path('/proc/self/maps').read_text().splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            path = Path(fields[5]).resolve()
            mapped[str(path)] = {'sha256': h(path), 'bytes': len(read(path))}
    ck(dict(os.environ) == ENV and not Path(sys.pycache_prefix).exists(),
       'auditor_exact_actual_environment_cache', 'controlled actual artifact audit')
    return {'modules': modules, 'mapped_files': mapped, 'flags': repr(sys.flags),
            'executable': str(Path(sys.executable).resolve()), 'sys_path': sys.path,
            'environment': dict(os.environ), 'pycache_prefix': sys.pycache_prefix,
            'scope': 'Current artifact-auditor file-backed maps; samples, not continuous tracing.'}

# P209-specific replacement sections for the complete disclosed P208 adapter.
# This is assembly input, not an imported or executed module.

def rich_pin(path, value, historical=False):
    selected = pin(path, value, historical)
    if isinstance(value, dict) and selected == Path(path):
        if 'resolved' in value:
            ck(str(selected.resolve()) == value['resolved'], 'recorded_path_resolution', str(path))
        if 'symlink' in value:
            ck((os.readlink(selected) if selected.is_symlink() else None) == value['symlink'],
               'recorded_symlink_value', str(path))
    return selected


def exact_map(record, historical=True):
    for name, value in record.items():
        rich_pin(Path(name) if Path(name).is_absolute() else ROOT / name, value, historical)


def exact_pair(base, before, after, count=None, historical=True):
    first = j(base / before)
    ck(first == j(base / after), 'entire_recorded_before_after_equal', (label(base), before, after))
    if count is not None:
        ck(len(first) == count, 'exact_recorded_input_count', (label(base), count))
    exact_map(first, historical)
    return first


def revision_originals_and_failure():
    # Original preparation and real initial_01 remain exact historical evidence.
    pin(ORIGINAL_PREPARATION / 'SHA256SUMS',
        '3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51')
    manifest(ORIGINAL_PREPARATION, count=347)
    failed = OUT / 'initial_01'
    pin(failed / 'SHA256SUMS', 'deb48a3ed612ad9e292436e2037a879df37a0a5e2204594702f436c73bbe4b04')
    manifest(failed, count=8)
    for snapshot, source in [('executed_auditor_snapshot.py', 'audit_p209.py'),
                             ('executed_recorder_snapshot.py', 'record_audit.py')]:
        ck(read(failed / snapshot) == read(ORIGINAL_PREPARATION / source),
           'initial_failed_exact_executed_sources', snapshot)
    row, attempt = j(failed / 'COMMAND.json'), j(failed / 'ATTEMPT.json')
    expected = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(failed / 'unused_pycache'),
                str(ORIGINAL_PREPARATION / 'audit_p209.py'), 'terminal-artifact-after-actual-views']
    ck(row['exit_code'] == 1 and row['status'] == 'COMPLETED' and row['failure'] is None
       and row['inputs_unchanged'] and row['unused_cache_absent'] and not (failed / 'unused_pycache').exists()
       and row['argv'] == expected and row['cwd'] == str(ROOT) and row['environment'] == ENV,
       'initial_failed_child_remains_failure', 'real exit one; not an unexecuted draft')
    ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and
       all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc')),
       'initial_failed_prespawn_record', 'original fields')
    exact_pair(failed, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 7, historical=True)
    for stream in ('stdout', 'stderr'):
        pin(failed / ('audit.' + stream), row[stream])
    ck(read(failed / 'audit.stdout') == b'' and
       h(failed / 'audit.stderr') == '6c070f981a6b6f6ae05363e32f8047efda4f2a0e8c458f22dd9152990ccfb7cf',
       'initial_failed_full_raw_streams', 'unchanged full historical traceback')
    execution = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_01.failed.actual.json'
    pin(execution, '9e7efd7bbc5555269037f17021d2c61cbee7870d133622442f4a1d99fbe262c4')
    outer = j(execution)
    ck(outer['completion']['exit_code'] == 1 and
       read(failed / 'audit.stderr').decode() in outer['completion']['output'],
       'initial_failed_root_wrapper_remains_failure', 'traceback does not print round or expected hash')
    # Revision 01 and its real initial_02 failure are an additional immutable
    # historical layer. They are not replaced by this new prepared attempt.
    previous = BATCH / 'qa/p209_terminal_artifact_revision_01'
    pin(previous / 'SHA256SUMS',
        '855aba017f5a369c09696272579897324bbd906892b353d17f0c9eb6d7fcbcc5')
    manifest(previous, count=418)
    second = OUT / 'initial_02'
    pin(second / 'SHA256SUMS', '89ab791251744f3aa96911f871f108268c2ebb7e5e1da55329eea45eb70bbc96')
    manifest(second, count=8)
    for snapshot, source in [('executed_auditor_snapshot.py', 'audit_p209.py'),
                             ('executed_recorder_snapshot.py', 'record_audit.py')]:
        ck(read(second / snapshot) == read(previous / source),
           'second_failed_exact_executed_sources', snapshot)
    row, attempt = j(second / 'COMMAND.json'), j(second / 'ATTEMPT.json')
    expected = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(second / 'unused_pycache'),
                str(previous / 'audit_p209.py'), 'terminal-artifact-after-actual-views']
    ck(row['exit_code'] == 1 and row['status'] == 'COMPLETED' and row['failure'] is None
       and row['inputs_unchanged'] and row['unused_cache_absent'] and not (second / 'unused_pycache').exists()
       and row['argv'] == expected and row['cwd'] == str(ROOT) and row['environment'] == ENV,
       'second_failed_child_remains_failure', 'real initial_02 exit one; not a gate PASS')
    ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and
       all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc')),
       'second_failed_prespawn_record', 'original fields')
    exact_pair(second, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 10, historical=True)
    for stream in ('stdout', 'stderr'):
        pin(second / ('audit.' + stream), row[stream])
    ck(read(second / 'audit.stdout') == b'' and
       h(second / 'audit.stderr') == '87df565befc65ce9d96c25cf6e28f470521bea9207750c17ee1123ed6384c09b',
       'second_failed_full_raw_streams', 'unchanged 871-byte initial census A traceback')
    execution = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_02.failed.actual.json'
    pin(execution, 'cb4872647ea63e9e2e9253dcb7d11d090947f8399c497a358239223241f9e602')
    outer = j(execution)
    ck(outer['completion']['exit_code'] == 1 and
       read(second / 'audit.stderr').decode() in outer['completion']['output'],
       'second_failed_root_wrapper_remains_failure', 'both original child and root wrapper remain exit one')
    # Revision 02 and the real initial_03 schema failure remain immutable in
    # place; this correction does not replace either earlier preparation.
    revision02 = BATCH / 'qa/p209_terminal_artifact_revision_02'
    pin(revision02 / 'SHA256SUMS',
        '6e9c86fad5802ed82df5ffa78e3f7d7bc9c3bec00a04892c96e002db121ed6ed')
    manifest(revision02, count=79)
    third = OUT / 'initial_03'
    pin(third / 'SHA256SUMS', '45f4751ce36bfdfd432b2b5193ef23c8c7b91fa109b88cc4e305fd59234af921')
    manifest(third, count=8)
    for snapshot, source in [('executed_auditor_snapshot.py', 'audit_p209.py'),
                             ('executed_recorder_snapshot.py', 'record_audit.py')]:
        ck(read(third / snapshot) == read(revision02 / source),
           'third_failed_exact_executed_sources', snapshot)
    row, attempt = j(third / 'COMMAND.json'), j(third / 'ATTEMPT.json')
    expected = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(third / 'unused_pycache'),
                str(revision02 / 'audit_p209.py'), 'terminal-artifact-after-actual-views']
    ck(row['exit_code'] == 1 and row['status'] == 'COMPLETED' and row['failure'] is None
       and row['inputs_unchanged'] and row['unused_cache_absent'] and not (third / 'unused_pycache').exists()
       and row['argv'] == expected and row['cwd'] == str(ROOT) and row['environment'] == ENV,
       'third_failed_child_remains_failure', 'real initial_03 exit one; no default canonical PASS')
    ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and
       all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc')),
       'third_failed_prespawn_record', 'original fields')
    exact_pair(third, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 13, historical=True)
    for stream in ('stdout', 'stderr'):
        pin(third / ('audit.' + stream), row[stream])
    ck(read(third / 'audit.stdout') == b'' and len(read(third / 'audit.stderr')) == 674 and
       h(third / 'audit.stderr') == '33820efd46d6cc2adf5c8c1ad27c6f4eb25f054e4607c0306f8409fe352c4077',
       'third_failed_full_raw_streams', 'unchanged complete KeyError status traceback')
    execution = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_03.failed.actual.json'
    pin(execution, '816cb77c887baca09e28a6a71b9c25fafadd2942bca587e20bd4a8ca4cf0581e')
    outer = j(execution)
    ck(outer['completion']['exit_code'] == 1 and
       read(third / 'audit.stderr').decode() in outer['completion']['output'],
       'third_failed_root_wrapper_remains_failure', 'both original child and root wrapper remain exit one')
    # Preserve revision03 and the real initial04 root-view schema failure.
    # This appended documentary layer does not alter any older failure branch.
    revision03 = BATCH / 'qa/p209_terminal_artifact_revision_03'
    pin(revision03 / 'SHA256SUMS',
        '4863c739ce8189f19e484f33fd5b42ce8f69f3b292f42768ba638108c105a743')
    manifest(revision03, count=47)
    fourth = OUT / 'initial_04'
    pin(fourth / 'SHA256SUMS', 'bf5d128c27762025552fc730ba363e05a44874e28b2b2857d02db3fa2c8c4c7d')
    manifest(fourth, count=8)
    for snapshot, source in [('executed_auditor_snapshot.py', 'audit_p209.py'),
                             ('executed_recorder_snapshot.py', 'record_audit.py')]:
        ck(read(fourth / snapshot) == read(revision03 / source),
           'fourth_failed_exact_executed_sources', snapshot)
    row, attempt = j(fourth / 'COMMAND.json'), j(fourth / 'ATTEMPT.json')
    expected = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(fourth / 'unused_pycache'),
                str(revision03 / 'audit_p209.py'), 'terminal-artifact-after-actual-views']
    ck(row['exit_code'] == 1 and row['status'] == 'COMPLETED' and row['failure'] is None
       and row['inputs_unchanged'] and row['unused_cache_absent'] and not (fourth / 'unused_pycache').exists()
       and row['argv'] == expected and row['cwd'] == str(ROOT) and row['environment'] == ENV,
       'fourth_failed_child_remains_failure', 'real initial_04 exit one; no reconstructed page view')
    ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and
       all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc')),
       'fourth_failed_prespawn_record', 'original fields')
    exact_pair(fourth, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 16, historical=True)
    for stream in ('stdout', 'stderr'):
        pin(fourth / ('audit.' + stream), row[stream])
    ck(read(fourth / 'audit.stdout') == b'' and len(read(fourth / 'audit.stderr')) == 652 and
       h(fourth / 'audit.stderr') == 'cffcade469b9bc33938a9102303db6a4fb7dd675943b58abe77645469a45881f',
       'fourth_failed_full_raw_streams', 'unchanged complete KeyError page_count traceback')
    execution = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_04.failed.actual.json'
    pin(execution, '483bac2c8955b9958ed02eb3741ed8bbeda6c48f36ad1ae9f1996fe26d32a340')
    outer = j(execution)
    ck(outer['completion']['exit_code'] == 1 and
       read(fourth / 'audit.stderr').decode() in outer['completion']['output'],
       'fourth_failed_root_wrapper_remains_failure', 'both original child and root wrapper remain exit one')
    return {'revision': 'p209_terminal_artifact_revision_04', 'original_preparation_payloads': 347,
            'preserved_revision_03_payloads': 47, 'preserved_initial_04_payloads': 8,
            'fourth_child_exit': 1, 'fourth_wrapper_exit': 1,
            'preserved_revision_02_payloads': 79, 'preserved_initial_03_payloads': 8,
            'third_child_exit': 1, 'third_wrapper_exit': 1,
            'previous_revision_payloads': 418, 'preserved_initial_02_payloads': 8,
            'second_child_exit': 1, 'second_wrapper_exit': 1,
            'preserved_initial_01_payloads': 8, 'original_child_exit': 1, 'original_wrapper_exit': 1,
            'explicit_git_history_roles': 2, 'round1_role': 'REAFFIRMED', 'round2_role': 'REGISTERED',
            'not_a_new_scientific_review_or_execution': True}


def load_aliases():
    roles = j(B / 'delta_check_02/EXACT_HISTORY_ALIASES.json')
    ck(len(roles) == 32, 'exact_B_alias_scope', 'all 32 declared roles, not a count of drifted files')
    for key, target in roles.items():
        original, digest = key.rsplit(' @ ', 1)
        alias(original, target, digest)
    aroles = j(A / 'delta_check_02/HISTORICAL_PIN_ROLE_MAP.json')
    for original, row in aroles['exact_documentary_aliases'].items():
        alias(original, row['preserved_exact_path'], row['original_sha256'])
    row = aroles['initial_manifest_role']
    alias(row['original_path'], row['preserved_exact_path'], row['original_sha256'])
    for number in (1, 2):
        freeze = PAPER / ('frozen_round' + str(number))
        meta = j(freeze / ('ROUND' + str(number) + '_PROVENANCE.json'))
        for row in meta['anchor_mapping'].values():
            alias(row['original_path'], safe(freeze, row['physical_path']), row['sha256'])
        if number == 1:
            for row in meta['historical_external_resolution'].values():
                alias(row['original_path'], row['round1_physical_path'], row['sha256'])
        else:
            for row in meta['historical_input_resolution']:
                alias(row['original_path'], row['round2_physical_path'], row['sha256'])
    for letter in ('A', 'B'):
        root = j(BATCH / ('qa/P209_' + letter + '_ROOT_DELTA_INSPECTION.actual.json'))
        for row in root['historical_input_aliases']:
            ck(set(row) == {'original_path', 'sha256', 'physical_path'}, 'root_exact_alias_schema', letter)
            alias(row['original_path'], row['physical_path'], row['sha256'])
    # Two named at-freezer-current roles; Round1 already exists in B's map.
    # Reaffirming it still checks exact duplicate bytes through alias().
    receipt = BATCH / 'GIT_SYNC_RECEIPT.md'
    for number, directory, digest, seal in [
        (1, 'qa/central_lifecycle_p209_round1',
         '2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24',
         '2ecf22568096dffbf49213869d82e58f1a43d6506968f0753e6197b451558c22'),
        (2, 'qa/central_lifecycle_p209_terminal_push',
         'a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865',
         'e5b02d4594deba8e6bec8a5d31dac9b20dd2f40f8245be57dbf56bc5a39fad80')]:
        holder = BATCH / directory
        pin(holder / 'SHA256SUMS', seal); manifest(holder, count=5)
        capture = j(holder / 'CAPTURE.actual.json')
        if number == 1:
            rows = [row for row in capture['copies'] if row['original_path'] == str(receipt)]
            ck(len(rows) == 1 and rows[0]['physical_path'] == str(holder / 'GIT_SYNC_RECEIPT.before.md')
               and rows[0]['sha256'] == digest and rows[0]['actual_cmp']['exit_code'] == 0
               and rows[0]['actual_cmp']['output'] == '',
               'named_round1_current_receipt_capture', 'distinct from af175 historical receipt')
            for field in ('actual_before_hash_command', 'actual_after_hash_command'):
                ck(capture[field]['exit_code'] == 0 and
                   digest + '  ' + str(receipt) in capture[field]['output'].splitlines(),
                   'named_round1_current_receipt_original_hashes', field)
        else:
            rel = receipt.relative_to(ROOT).as_posix()
            rows = [row for row in capture['copies'] if row['source'] == rel]
            ck(capture['status'] == 'ACTUAL_EXACT_PRE_UPDATE_CONTROL_COPIES' and len(rows) == 1
               and rows[0]['copy'] == (holder / 'GIT_SYNC_RECEIPT.before.md').relative_to(ROOT).as_posix()
               and rows[0]['actual_comparison']['exit_code'] == 0 and rows[0]['actual_comparison']['output'] == ''
               and capture['original_sha256_command']['exit_code'] == 0 and
               digest + '  ' + rel in capture['original_sha256_command']['output'].splitlines(),
               'named_round2_current_receipt_capture', 'actual pre-terminal-push snapshot')
        read(holder / 'README.md')
        meta = j(PAPER / ('frozen_round' + str(number)) / ('ROUND' + str(number) + '_PROVENANCE.json'))
        ck(meta['all_source_inputs_before_and_rechecked_after'][str(receipt)] == digest,
           'named_current_receipt_exact_frozen_observation', number)
        alias(receipt, holder / 'GIT_SYNC_RECEIPT.before.md', digest)
    return {'declared_exact_roles': len(ALIASES), 'no_omitted_historical_pins': True}


def historical_manifest(path, base, count=None, delta_alias=False):
    rows = manifest_rows(path)
    if count is not None:
        ck(len(rows) == count, 'historical_manifest_count', (label(path), count))
    for name, digest in rows.items():
        target = base / ('INITIAL_DELTA.md' if delta_alias and name == 'DELTA.md' else name)
        rich_pin(target, digest, True)
    return rows


def frozen_and_author():
    ck(h(PAPER / 'SHA256SUMS') == h(PAPER / 'AUTHOR_MANIFEST.sha256') ==
       '9fd20cd746f1ae03c22a87283313248ad79ffcfb9a0f1ea45458937dd5901a0e',
       'immutable_author_seal_roles', 'historical SHA256SUMS is NOT current whole-paper rollup')
    author = manifest(PAPER, 'AUTHOR_MANIFEST.sha256', complete=False, count=1985)
    frozen = [manifest(PAPER / ('frozen_round' + str(k)), count=(1989, 2003, None)[k]) for k in range(3)]
    ck(h(PAPER / 'frozen_round0/SHA256SUMS') == '0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba',
       'exact_round0', 'original physical seal')
    ck(h(PAPER / 'frozen_round1/SHA256SUMS') == 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57',
       'exact_round1', 'original physical seal')
    ck(all(frozen[1].get(n) == d for n, d in frozen[0].items()) and
       all(frozen[2].get(n) == d for n, d in frozen[1].items()),
       'nested_immutable_frozen_cores', '1989 to 2003 to measured Round2, not identical whole manifests')
    for n, digest in author.items():
        ck(all(rows.get(n) == digest for rows in frozen), 'author_in_every_round', n)
    ck(author['PAPER_STATUS.md'] == '304c24e871a27bd02bcd6db231abc37870fb263a01d4c081289bdd53e8718a73',
       'immutable_author_status', 'use separate ROOT_LIFECYCLE.md')
    pin(PAPER / 'ROOT_ADOPTION.md', '8f82ae0af7156131f14e9e6e849198f8b1c98564760c30d4bc121b50cf34f82e')
    fixed = j(TERMINAL_PREP / 'SOURCE_PINS.json')
    ck(set(fixed) == set(SOURCE_NAMES), 'exact_eight_source_contract', 'no extra source/bibliography inputs')
    for n, value in fixed.items():
        for base in (PAPER, PAPER / 'frozen_round0', PAPER / 'frozen_round1', PAPER / 'frozen_round2'):
            pin(base / n, value)
    root = j(BATCH / 'qa/P209_ROUND2_ROOT_INSPECTION.actual.json')
    ck(root['schema'] == 'p209-round2-root-physical-closure-v1' and
       root['status'] == 'PASS_ROOT_ROUND2_COMPLETE_PHYSICAL_CLOSURE' and root['paper'] == 'P209'
       and type(root['round']) is int and root['round'] == 2 and root['current_open_findings'] == 0,
       'actual_root_round2_gate', 'measured physical closure, not a preparation result')
    ck(root['round2_manifest_sha256'] == h(PAPER / 'frozen_round2/SHA256SUMS') and
       root['round2_payloads'] == len(frozen[2]), 'actual_root_round2_count_hash', 'actual exact seal')
    ck(set(root['source_pins']) == {str(PAPER / n) for n in SOURCE_NAMES}, 'round2_exact_source_keys', 'absolute live paths')
    for n, value in fixed.items():
        ck(all(root['source_pins'][str(PAPER / n)][k] == value[k] for k in ('sha256', 'bytes')),
           'round2_source_values', n)
    for letter in ('A', 'B'):
        ck(root['accepted_' + letter + '_root_gate_sha256'] ==
           h(BATCH / ('qa/P209_' + letter + '_ROOT_DELTA_INSPECTION.actual.json')),
           'round2_actual_acceptance_hashes', letter)
    read(BATCH / 'qa/P209_ROUND2_ROOT_INSPECTION.md')
    metadata = []
    for number, previous in ((1, frozen[0]), (2, frozen[1])):
        base = PAPER / ('frozen_round' + str(number))
        meta = j(base / ('ROUND' + str(number) + '_PROVENANCE.json'))
        ck(meta['schema'] == ('p209-round1-provenance-v2' if number == 1 else 'p209-round2-provenance-v1'),
           'exact_physical_provenance_schema', number)
        ck(meta['core_payload_pins'] == previous, 'exact_physical_core_provenance', number)
        for role in ('all_source_inputs_before_and_rechecked_after', 'accepted_review_and_root_manifest_referents'):
            exact_map(meta[role], historical=True)
        for name, row in meta['anchor_mapping'].items():
            pin(safe(base, row['physical_path']), row['sha256'])
            rich_pin(row['original_path'], row['sha256'], True)
        prior = meta['prior_whole_paper_manifest']
        ck(prior['original_referent_base'] == str(PAPER), 'old_whole_manifest_original_base', number)
        old = historical_manifest(Path(prior['physical_path']), PAPER, prior['payloads'])
        ck(old == prior['original_referent_pins'], 'old_whole_manifest_full_roles', number)
        pin(prior['physical_path'], prior['sha256'])
        links = (meta['round1_core_link_map'] if number == 1 else meta['round2_historical_link_map'])
        links += meta['acceptance_and_historical_anchor_link_map']
        for row in links:
            rich_pin(row['physical_target'], row['sha256'], True)
        metadata.append(meta)
    r2 = metadata[-1]
    ck(r2['author_payloads_preserved'] == 1985 and r2['round1_core_payloads_copied'] == 2003,
       'round2_exact_preservation_counts', 'author and Round1')
    ck(r2['accepted_root_assertions'] == j(BATCH / 'qa/P209_B_ROOT_DELTA_INSPECTION.actual.json'),
       'round2_exact_B_root_snapshot', 'full root JSON')
    aliases = {row['copy_relative']: row['sha256'] for row in r2['historical_input_resolution'] if row['copy_relative'] is not None}
    expected = set(frozen[1]) | {'ROUND2_ACCEPTANCE/' + n for n in r2['anchor_mapping']} | set(aliases)
    expected |= {'ROUND2_PROVENANCE.json', 'ROUND2_FREEZE_ADAPTER.py'}
    ck(len(r2['anchor_mapping']) == 15 and set(frozen[2]) == expected and len(frozen[2]) == 2020 + len(aliases),
       'round2_full_exact_physical_layout', '2003 core +15 anchors +2 metadata +actual aliases')
    pin(PAPER / 'frozen_round2/ROUND2_FREEZE_ADAPTER.py', '787357029ae3d4f50c1a9998a3b1e4fe9377786cc06cb024e3a7a96ef95b46c7')
    for row in r2['historical_input_resolution']:
        pin(row['round2_physical_path'], row['sha256'])
    return {'author_entries': len(author), 'round0_payloads': 1989, 'round1_payloads': 2003,
            'round2_payloads': len(frozen[2]), 'actual_new_round2_aliases': len(aliases),
            'source_files': len(fixed), 'immutable_author_status': True}


def modern_commands(base, filename='ALL_COMMAND_RECORDS.json', expected=85, env=ENV):
    entries = j(base / filename)
    ck(len(entries) == expected, 'actual_modern_command_count', (label(base), expected))
    for entry in entries:
        folder, tag, row = Path(entry['folder']), entry['tag'], entry['command']
        ck(folder.is_relative_to(base) and j(folder / (tag + '.command.json')) == row,
           'exact_embedded_command', (label(base), tag))
        attempt = j(folder / (tag + '.attempt.json'))
        ck(all(attempt[k] == row[k] for k in ('argv', 'cwd', 'env', 'stdout', 'stderr')),
           'exact_modern_attempt_fields', tag)
        ck(row['exit'] == 0 and row['process_outcome'] == 'COMPLETED' and row['spawn_error'] is None
           and row['cleanup'] == [] and row['env'] == env, 'actual_modern_command_pass', tag)
        for stream in ('stdout', 'stderr'):
            rich_pin(folder / row[stream], row[stream + '_info'])
        samples = j(folder / (tag + '.maps.json'))
        observed = sorted({p for sample in samples['samples'] for p in sample['mapped_files']})
        ck(observed == entry['mapped_files'], 'exact_recorded_map_union', tag)
    return entries


def review_dependency_keys():
    a = exact_pair(A / 'delta_check_02', 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 124214)
    b = exact_pair(B / 'delta_check_02', 'INPUTS_FULL_BEFORE.json', 'INPUTS_FULL_AFTER.json', 128227)
    exact_map(j(A / 'initial_audit_01/CURRENT_INPUT_CLOSURE.json'))
    exact_pair(B / 'artifact_audit_03', 'DOCUMENTARY_INPUTS_BEFORE.json', 'DOCUMENTARY_INPUTS_AFTER.json', 127544)
    # The failures stay failures. Their original streams are sealed by their
    # accepted review manifests; successful later evidence cannot rewrite them.
    failed_a = j(A / 'delta_check_01/EXECUTION.actual.json')
    ck(failed_a['completion_result']['exit_code'] == 1,
       'preserved_A_delta_failure', 'real first documentary failure; original nested execution schema')
    bad = j(B / 'delta_check_01/CLOSURE_AFTER_FAILURE.json')
    ck(bad['actual_outer_exit'] == 1 and bad['actual_child_exit'] == 0 and
       bad['status'] == 'FAIL_PRESERVED_OUTER_WRAPPER_FILENAME_COLLISION',
       'preserved_B_wrapper_failure', 'not a successful wrapper')
    good = j(B / 'delta_check_02/DELTA_EVIDENCE_RESULT.json')
    ck(good['status'] == 'PASS_EXACT_NOCHANGE_DELTA_EVIDENCE' and good['all_inputs_unchanged']
       and good['accepted_decision_not_written_by_checker'] and good['delta_full_input_paths'] == len(b),
       'actual_B_documentary_result', 'no acceptance fabricated by an integrity program')
    wrapper = j(B / 'delta_check_02/RECEIPT.json')
    ck(wrapper['status'] == 'PASS' and wrapper['failure'] is None and wrapper['inputs_unchanged'],
       'actual_B_documentary_wrapper', 'corrected separate attempt')
    modern_commands(B / 'delta_check_02', 'WRAPPER_COMMAND_RECORDS.json', 1)
    modern_commands(B / 'delta_check_02', expected=8)
    exact_pair(B / 'delta_check_02', 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 5166)
    return {'a_complete_delta_inputs': len(a), 'b_complete_delta_inputs': len(b),
            'a_original_documentary_pins': 120491, 'b_original_documentary_pins': 127544}


def reviews(history):
    result = {}
    for letter, base, input_round, count, old_count in [('a', A, 0, 1342, 1227), ('b', B, 1, 1472, 1298)]:
        sealed = manifest(base, count=count)
        initial, current = j(base / 'FINDINGS.json'), j(base / 'CURRENT_FINDINGS.json')
        for census in (initial, current):
            ck(census['schema'] == 'p209-manuscript-review-findings-v1' and
               census['reviewer'] == '/root/p209_' + letter + '_reviewer' and census['input_round'] == input_round,
               'distinct_original_review_census', letter)
        expected_initial = {'a': 'NOT_YET_SUBMITTED_OR_ASSESSED', 'b': 'UNASSESSED'}
        ck(initial['delta_status'] == expected_initial[letter], 'initial_census_remains_initial', letter)
        ck(current['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA' and
           current['current_open_counts'] == {'critical': 0, 'major': 0, 'minor': 0} and
           current['findings'] == [] and current['scientific_inputs_changed'] is False,
           'actual_current_accepted_census', letter)
        root = j(BATCH / ('qa/P209_' + letter.upper() + '_ROOT_DELTA_INSPECTION.actual.json'))
        ck(root['schema'] == 'p209-' + letter + '-root-delta-closure-v1' and
           root['status'] == 'ROOT_ACCEPTED_' + letter.upper() + '_DELTA_ORIGINAL_CLOSURE_PASS' and
           root['paper'] == 'P209' and root['input_round'] == input_round and root['current_open_findings'] == 0,
           'actual_accepted_root_delta', letter)
        ck(all(root[k] is True for k in ('reviewer_delta_accepted', 'root_original_inspection_complete', 'root_replay_closure_complete')),
           'actual_original_and_replay_root_closure', letter)
        ck(root['review_manifest_entries'] == count, 'actual_review_payload_count', letter)
        for key, path in [('review_manifest_sha256', base / 'SHA256SUMS'), ('delta_sha256', base / 'DELTA.md'),
                          ('current_findings_sha256', base / 'CURRENT_FINDINGS.json'),
                          ('response_sha256', BATCH / ('P209_' + letter.upper() + '_RESPONSE.md')),
                          ('findings_sha256' if letter == 'a' else 'initial_findings_sha256', base / 'FINDINGS.json')]:
            pin(path, root[key])
        ck(current['response_sha256'] == root['response_sha256'], 'same_reviewer_exact_response', letter)
        pin(base / 'INITIAL_REVIEW_SEAL.sha256', current['initial_complete_manifest_sha256'])
        original = historical_manifest(base / 'INITIAL_REVIEW_SEAL.sha256', base, old_count, letter == 'b')
        ck(original['REPORT.md'] == sealed['REPORT.md'] and original['FINDINGS.json'] == sealed['FINDINGS.json'],
           'initial_report_census_unchanged_in_place', letter)
        for name in ('REPORT.md', 'DELTA.md', 'SOURCE_AND_PROOF.md', 'REPLAY_LOG.md', 'BUILD_REPORT.md'):
            ck('HOLD_EXTERNAL' in read(base / name).decode(), 'review_scope_hold', (letter, name))
        frozen = PAPER / ('frozen_round' + str(input_round))
        expected = {str((frozen / n).relative_to(ROOT)): d for n, d in manifest_rows(frozen / 'SHA256SUMS').items()}
        expected[str((frozen / 'SHA256SUMS').relative_to(ROOT))] = h(frozen / 'SHA256SUMS')
        ck(historical_manifest(base / 'INPUT_PINS.sha256', ROOT) == expected,
           'review_exact_whole_freeze_inputs', letter)
        read(BATCH / ('qa/P209_' + letter.upper() + '_ROOT_DELTA_INSPECTION.md'))
        for path in sorted(base.rglob('SHA256SUMS')):
            if path != base / 'SHA256SUMS': manifest(path.parent)
        result[letter] = {'accepted_manifest': h(base / 'SHA256SUMS'), 'payloads': count,
                          'initial_payloads_preserved': old_count, 'initial_same_paths': old_count - (letter == 'b'),
                          'initial_delta_aliases': int(letter == 'b'), 'current_open': current['current_open_counts']}
    result['complete_dependency_reuse'] = review_dependency_keys()
    return result


def modern_presence(base):
    before = j(base / 'CONFIGURATION_BEFORE.json')
    ck(before == j(base / 'CONFIGURATION_AFTER.json'), 'strict_configuration_interval', label(base))
    config(before['optional'])
    for name, names in before['directories'].items():
        p = Path(name)
        actual = sorted(str(q) for q in p.rglob('*') if q.is_file()) if p.is_dir() else None
        ck(actual == names, 'strict_config_directory_membership', name)
        for value in names or []: read(value)
    return before


def declared_runtime_names(build=False):
    stdlib = Path('/usr/lib/python3.10')
    paths = set()
    for directory, folders, files in os.walk(stdlib):
        folders[:] = [f for f in folders if f not in {'site-packages', 'dist-packages', '__pycache__'}]
        paths.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for root in LIB_ROOTS:
        if root.is_dir():
            iterator = root.glob('*') if root == Path('/usr/local/lib') else root.rglob('*')
            paths.update(str(p) for p in iterator if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    tools = ['/usr/bin/env', '/usr/bin/cmp', '/usr/bin/ldd', '/bin/bash', '/bin/sh', '/usr/bin/python3.10']
    if build: tools += ['/usr/bin/' + n for n in ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo', 'pdffonts', 'pdftotext', 'pdftoppm')]
    paths.update(tools)
    return paths


def strict_replays():
    summaries = {}
    for role, base, count, input_count, status in [
        ('author', PAPER, 98278, 3211, 'PASS_ROOT_AUTHOR_PAIR'),
        ('a', A, 135605, 5147, 'PASS_ROOT_REVIEW_A_PAIR'),
        ('b', B, 54794, 5164, 'PASS_ROOT_REVIEW_B_PAIR')]:
        rr = BATCH / ('qa/root_replays/p209_' + role + '_strict/root_' + role + '_pair_01')
        launcher = rr.parent / ('launcher_root_' + role + '_pair_01')
        manifest(rr, count=462); manifest(launcher, count=10)
        rec = j(rr / 'RECEIPT.json')
        ck(rec['status'] == status and rec['mode'] == 'pair' and not rec['failures']
           and rec['result']['canonical_adopted'] is False, 'strict_pair_actual_result', role)
        inputs = exact_pair(rr, 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json', 'ALL_INPUTS_AFTER.json', input_count)
        runtime = exact_pair(rr, 'RUNTIME_BEFORE.json', 'RUNTIME_AFTER.json')
        conf = modern_presence(rr)
        ck(declared_runtime_names() <= set(runtime), 'strict_full_fixed_runtime_names', role)
        known = {v['resolved'] for v in inputs.values()}
        ck(all(inputs[n] == v for n, v in runtime.items()), 'strict_runtime_entirely_prepinned', role)
        for phase in ('BEFORE', 'AFTER'):
            parent = j(rr / ('PARENT_' + phase + '.json'))
            ck(parent['env'] == ENV and parent['cwd'] == str(ROOT) and parent['optimization'] == 0
               and not parent['cache_exists'] and not Path(parent['pycache_prefix']).exists(),
               'strict_parent_actual_settings', (role, phase))
            ck(all(s in parent['flags'] for s in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')),
               'strict_parent_actual_flags', (role, phase))
        entries = modern_commands(rr)
        ck(all(set(e['mapped_files']) <= known for e in entries), 'strict_all_command_samples_covered', role)
        linkage = j(rr / 'LINKAGE.json')
        ck(not linkage['pending_targets'] and len(linkage['entries']) == 80 and
           all(e['status'] == 'VALIDATED' for e in linkage['entries']), 'strict_actual_linkage_closure', role)
        closure = j(rr / 'OBSERVED_CLOSURE.json')
        ck(closure['uncovered'] == closure['bytecode'] == [], 'strict_observed_closure', role)
        for label0 in ('replay_01', 'replay_02'):
            folder = rr / label0; child = j(folder / 'RECEIPT.json')
            ck(child['status'] == 'PASS' and child['failure'] is None and child['inputs_unchanged']
               and child['checks'] == count and child['total_states'] == 3414,
               'strict_actual_complete_child', (role, label0))
            ck(child['source_only_initial_names'] == ['bootstrap.py', 'verify.py'], 'strict_child_source_only_names', role)
            for name in ('bootstrap.py', 'verify.py'):
                ck(read(folder / 'source_inputs' / name) == read(base / name), 'strict_unchanged_child_source', (role, name))
            ck(physical(folder / 'source_inputs') == {'bootstrap.py', 'verify.py'}, 'strict_source_capsule_no_products', role)
            exact_pair(folder, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
            ck(read(folder / 'producer.stdout') == read(base / 'CANONICAL.json'), 'strict_full_raw_canonical_reuse', (role, label0))
            payload = j(folder / 'producer.stdout')
            # Exact original emitter contracts differ by role. Reviewer A has
            # no top-level status field; success is independently required in
            # the real child receipt above, and full raw equality is unchanged.
            canonical_fields = {
                'author': {'schema': 'p209-author-v1', 'status': 'PASS', 'checks': 98278,
                           'total_states': 3414,
                           'scope': 'Exhaustive n=0,...,5 only; finite pressure, not all-size proof.',
                           'entrance_field_scope': 'Observed orbit index only; no all-size clock claim.'},
                'a': {'schema': 'p209-review-a-independent-v1', 'checks': 135605},
                'b': {'schema': 'p209-b-ports-constructive-carrier-v1', 'status': 'PASS',
                      'checks': 54794, 'states': 3414, 'max_n': 5}}[role]
            ck(type(payload) is dict and set(payload) == set(canonical_fields) | {'boxes'}
               and all(payload[key] == value for key, value in canonical_fields.items())
               and payload['checks'] == count,
               'strict_exact_role_canonical_schema_and_scalars', role)
            state_field = 'states' if role == 'b' else 'state_count'
            boxes = payload['boxes']
            ck(type(boxes) is list and [box['n'] for box in boxes] == list(range(6))
               and [box[state_field] for box in boxes] == [1, 1, 4, 27, 256, 3125]
               and sum(box[state_field] for box in boxes) == 3414,
               'strict_exact_original_canonical_census', role)
            ck(child['closure']['uncovered'] == child['closure']['bytecode'] == [], 'strict_child_recorded_closure', role)
            for when in ('before', 'after'):
                obs = j(folder / ('child.' + when + '.json'))
                ck(obs['env'] == ENV and obs['optimize'] == 0 and obs['isolated'] == obs['no_site'] == 1
                   and obs['dont_write_bytecode'] and not obs['cache_exists'] and not Path(obs['pycache_prefix']).exists(),
                   'strict_child_runtime_settings', (role, label0, when))
        launch = j(launcher / 'RECEIPT.json')
        ck(launch['status'] == 'PASS_ROOT_LAUNCH' and launch['exit'] == 0 and launch['outcome'] == 'COMPLETED'
           and launch['failure'] is None and launch['inputs_unchanged'] and launch['cache_absent']
           and launch['env'] == ENV and launch['cwd'] == str(ROOT), 'strict_actual_outer_pass', role)
        ck(launch['recorder_closure']['payloads'] == 462 and launch['recorder_closure']['status'] == status,
           'strict_exact_outer_inner_agreement', role)
        rich_pin(rr / 'SHA256SUMS', launch['recorder_seal'])
        exact_pair(launcher, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
        for name in ('recorder.stdout', 'recorder.stderr'): rich_pin(launcher / name, launch[name + '_pin'])
        ck(j(launcher / 'recorder.stdout')['status'] == status, 'strict_outer_full_actual_stdout', role)
        summaries[role] = {'runs': 2, 'checks_each': count, 'states_each': 3414,
                           'actual_commands': 85, 'inputs': input_count, 'runtime': len(runtime),
                           'config_directory_count': len(conf['directories']), 'new_executions': 0}
    reconciliation = j(B / 'auxiliary_01/reconcile.stdout')
    ck(reconciliation['status'] == 'PASS_FULL_MATHEMATICAL_PAYLOAD_RECONCILIATION'
       and reconciliation['row_count'] == 3414 and reconciliation['checks'] == 78548
       and len(reconciliation['rows']) == 3414 and all(row['status'] == 'ALL_EQUAL' for row in reconciliation['rows']),
       'complete_prior_normalized_reconciliation', 'all rows retained; unlike canonicals are not raw-equal')
    modern_commands(B / 'auxiliary_01', expected=4)
    exact_pair(B / 'auxiliary_01', 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 5168)
    return summaries


def terminal_resource_key():
    runtime = exact_pair(FINAL, 'RUNTIME_BEFORE.json', 'RUNTIME_AFTER.json')
    names = {str(Path(p).resolve()) for p in declared_runtime_names(build=True)}
    ck(names == set(runtime), 'terminal_full_runtime_membership', 'complete declared stdlib/potential OS libraries/fixed tools')
    tex = exact_pair(FINAL, 'TEX_INVENTORY_BEFORE.json', 'TEX_INVENTORY_AFTER.json')
    names = {str(p.resolve()) for root in TEX_ROOTS if root.is_dir() for p in root.rglob('*') if p.is_file()}
    ck(names == set(tex), 'terminal_full_tex_membership', 'all known resource names, not old hashes alone')
    conf = j(FINAL / 'CONFIGURATION_BEFORE.json')
    ck(conf == j(FINAL / 'CONFIGURATION_AFTER.json'), 'terminal_configuration_interval', 'exact')
    config(conf)
    # Exact configuration membership is copied structurally from the fixed
    # terminal builder, using this same system interpreter/sysconfig only.
    candidates = set(CONFIG_ROOTS + TEX_ROOTS + TERMINAL_TOOLS)
    candidates.update(Path(p) for p in ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
        '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2'))
    stdlib = Path(sysconfig.get_path('stdlib')).resolve(); python = Path('/usr/bin/python3.10')
    candidates.add(stdlib.parent / ('python%d%d.zip' % sys.version_info[:2]))
    candidates.update([python.parent / 'pyvenv.cfg', python.parent.parent / 'pyvenv.cfg',
        python.with_name(python.name + '._pth'), python.with_name('python._pth'),
        Path('/etc/locale.conf'), Path('/etc/default/locale'), Path('/etc/nsswitch.conf'), Path('/etc/localtime'),
        Path('/etc/bash.bashrc'), Path('/etc/profile'), Path('/usr/lib/locale/locale-archive'), Path('/etc/passwd'), Path('/etc/group'),
        Path('/root/.fonts.conf'), Path('/root/.config/fontconfig/fonts.conf'), Path('/etc/fonts/local.conf'),
        Path(sysconfig.get_makefile_filename()), Path(sysconfig.get_config_h_filename())])
    pth = {'python._pth', 'python3._pth', 'python%d%d._pth' % sys.version_info[:2],
           'python%d.%d._pth' % sys.version_info[:2], python.name + '._pth'}
    for directory in {python.parent, Path(sys.executable).parent, stdlib.parent}:
        candidates.update(directory / n for n in pth)
    for name in ('LDLIBRARY', 'INSTSONAME'):
        value = sysconfig.get_config_var(name)
        if value: candidates.add(stdlib.parent / (value + '._pth'))
    ldd = read(Path('/usr/bin/ldd')).decode(); match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    ck(ldd.splitlines()[0] == '#!/bin/bash' and match is not None, 'terminal_ldd_loader_source', 'known shell/script')
    candidates.update(Path(p) for p in match.group(1).split())
    candidates.update(p for root in CONFIG_ROOTS if root.is_dir() for p in root.rglob('*') if p.is_file())
    ck(set(map(str, candidates)) == set(conf), 'terminal_complete_configuration_membership', 'exact declared candidates')
    return runtime, tex, conf


def terminal():
    whole = manifest(FINAL)
    pin(TERMINAL_PREP / 'SHA256SUMS', '983dba0c90f72a8ef7580f455780d5c2363d675c84e2e19f0c507c1f2ca7e616')
    manifest(TERMINAL_PREP, count=190)
    pin(TERMINAL_PREP / 'root_terminal_builds.py', 'b2489d74647e72ccecbce9906a3f790e94712a724337271f0c99aa77a945dae1')
    pin(TERMINAL_PREP / 'root_launch_terminal.py', '773ffba4850783614366732d47ae54aa9ad73c947048e6e9013ba4d0d90ec462')
    ck(read(FINAL / 'executed_recorder_snapshot.py') == read(TERMINAL_PREP / 'root_terminal_builds.py'),
       'terminal_exact_builder_source', 'actual source-only P209 builder, not P208 outputs')
    rec = j(FINAL / 'BUILD_EXECUTION.json')
    ck(rec['status'] == 'PASS_P209_TERMINAL_BUILD_PAIR_NOT_VIEWED' and not rec['failures']
       and rec['command_census_complete'] and rec['visual_review'] == 'PENDING_NOT_INFERRED_FROM_HASH_OR_RENDER'
       and len(rec['builds']) == 2 and len(rec['commands']) == 32,
       'terminal_actual_complete_pair', 'real builder remains NOT_VIEWED')
    inputs = exact_pair(FINAL, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    runtime, tex, conf = terminal_resource_key()
    libraries = exact_pair(FINAL, 'LIBRARIES_BEFORE.json', 'LIBRARIES_AFTER.json')
    consumed = exact_pair(FINAL, 'CONSUMED_TEX_BEFORE.json', 'CONSUMED_TEX_AFTER.json')
    parent_inputs = exact_pair(FINAL, 'RECORDER_INPUTS_BEFORE.json', 'RECORDER_INPUTS_AFTER.json')
    ck((len(inputs), len(runtime), len(tex), len(conf), len(libraries), len(consumed)) ==
       (rec['input_count'], rec['runtime_count'], rec['tex_inventory_count'], rec['configuration_count'],
        rec['resolved_link_file_count'], rec['consumed_tex_count']), 'terminal_recorded_exact_inventory_counts', 'measured not prefilled')
    expected = ['ldd_before', 'pdflatex_version', 'bibtex_version', 'texmf_roots']
    for k in (1, 2):
        label0 = 'cold_build_' + str(k)
        expected.extend(label0 + '_' + v for v in ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR'))
        expected.extend(label0 + '_' + v for v in ('tex1', 'bst', 'bibtex', 'tex2', 'tex3', 'pdfinfo', 'pdffonts', 'pdftotext', 'render', 'frozen_pdf_cmp'))
    expected += ['pair_pdf_cmp', 'ldd_after']
    ck([row['label'] for row in rec['commands']] == rec['expected_command_labels'] == expected,
       'terminal_exact_command_order', 'all 32 actual commands')
    bylabel = {}
    for row in rec['commands']:
        argv = command(FINAL, row, BUILD_ENV)
        expected_cwd = FINAL / row['label'][:12] if row['label'].startswith(('cold_build_1_', 'cold_build_2_')) else FINAL
        ck(row['cwd'] == str(expected_cwd), 'terminal_exact_actual_command_cwd', row['label'])
        ck(row['status'] == 'COMPLETED' and row['cleanup'] == [] and row['start_new_session'],
           'terminal_actual_closed_child', row['label'])
        attempt = j(FINAL / (row['label'] + '.attempt.json'))
        ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and
           all(attempt[key] == row[key] for key in ('argv', 'cwd', 'environment', 'started_utc')),
           'terminal_actual_prespawn_chronology', row['label'])
        if row['label'].endswith('_cmp'):
            ck(argv[:2] == ['/usr/bin/cmp', '--'] and len(argv) == 4 and
               read(Path(argv[2])) == read(Path(argv[3])), 'terminal_actual_raw_comparison_reuse', row['label'])
        bylabel[row['label']] = row
    for when in ('before', 'after'):
        raw = read(FINAL / ('ldd_' + when + '.stdout')).decode()
        found = {str(Path(p).resolve()) for p in re.findall(r'/[^\s():]+', raw) if Path(p).is_file()}
        ck('not found' not in raw and found == set(libraries), 'terminal_full_recorded_ldd_closure', when)
    covered = {**inputs, **runtime, **libraries, **parent_inputs,
               **{v['resolved']: {k: v[k] for k in ('sha256', 'bytes')} for v in conf.values() if v['is_file']}}
    for phase in ('BEFORE', 'AFTER'):
        obs = j(FINAL / ('RECORDER_RUNTIME_' + phase + '.json'))
        ck(obs['environment'] == BUILD_ENV and obs['cwd'] == str(ROOT) and obs['executable'] == '/usr/bin/python3.10'
           and obs['pycache_prefix'] == str(FINAL / 'never_created_parent_cache') and not Path(obs['pycache_prefix']).exists(),
           'terminal_actual_parent_settings', phase)
        ck(all(s in obs['flags'] for s in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')),
           'terminal_actual_parent_flags', phase)
        for path, value in obs['mapped_files'].items():
            ck(covered.get(path) == value, 'terminal_parent_mapped_input_coverage', path); pin(path, value)
        for value in obs['modules'].values():
            wanted = {k: value[k] for k in ('sha256', 'bytes')}
            ck(covered.get(value['path']) == wanted and not value['path'].endswith(('.pyc', '.pyo')),
               'terminal_parent_source_module_coverage', value['path']); pin(value['path'], wanted)
    external_union, generated_union = set(), {}
    pages, diagnostic_rows = [], []
    for k, row in enumerate(rec['builds'], 1):
        label0 = 'cold_build_' + str(k); cold = FINAL / label0
        initial = j(FINAL / (label0 + '_SOURCE_ONLY_INITIAL.json'))
        ck(row['directory'] == label0 and initial == row['source_only_initial'] and set(initial) == set(SOURCE_NAMES),
           'terminal_exact_eight_source_only_inputs', label0)
        for name, value in initial.items():
            pin(cold / name, value); pin(PAPER / 'frozen_round2' / name, value); pin(PAPER / name, value)
        for variable in ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR'):
            raw = read(FINAL / (label0 + '_' + variable + '.stdout')).decode().strip()
            path = Path(raw); path = (path if path.is_absolute() else cold / path).resolve()
            expected_root = {'query_value': raw, 'resolved': str(path), 'exists': False}; key = label0 + ':' + variable
            ck(j(FINAL / (label0 + '_USER_ROOTS_BEFORE.json'))[key] == j(FINAL / 'USER_ROOTS_AFTER.json')[key] == expected_root
               and not path.exists(), 'terminal_effective_user_roots_absent', key)
        for passno in (1, 2, 3):
            ck(bylabel[label0 + '_tex' + str(passno)]['argv'] == ['/usr/bin/pdflatex', '-no-shell-escape', '-recorder',
               '-interaction=nonstopmode', '-halt-on-error', 'main.tex'], 'terminal_exact_tex_command', (label0, passno))
            for line in read(FINAL / (label0 + '_pass' + str(passno) + '.fls')).decode().splitlines():
                if not line.startswith('INPUT '): continue
                path = Path(line[6:]); path = (path if path.is_absolute() else cold / path).resolve()
                if not path.is_relative_to(cold):
                    ck(str(path) in consumed and consumed[str(path)] == tex[str(path)], 'terminal_every_external_fls_input', str(path))
                    external_union.add(str(path))
                else:
                    name = path.relative_to(cold).as_posix()
                    if name in initial: pin(path, initial[name])
                    else:
                        ck(path.suffix in {'.aux', '.bbl', '.out', '.toc'}, 'terminal_only_generated_local_inputs', name)
            perpass = j(FINAL / (label0 + '_pass' + str(passno) + '_TEX_INPUTS.json'))
            ck(all(consumed.get(p) == v for p, v in perpass['consumed_external'].items()), 'terminal_perpass_external_inventory', (label0, passno))
            generated_union.update(perpass['generated_local'])
        bst = read(FINAL / (label0 + '_bst.stdout')).decode().strip()
        external_union.add(str(Path(bst).resolve()))
        ck(str(Path(bst).resolve()) in consumed, 'terminal_bibtex_style_pinned', bst)
        ck(read(FINAL / (label0 + '_generated.bbl')) == read(cold / 'main.bbl'), 'terminal_actual_bibliography_output', k)
        measured = j(FINAL / (label0 + '_MEASURED_PDF.json'))
        info_text = read(FINAL / (label0 + '_pdfinfo.stdout')).decode()
        page_count = int(re.search(r'^Pages:\s+(\d+)$', info_text, re.M).group(1))
        ck(measured['pages'] == measured['rendered_pages'] == row['pages'] == page_count == 4 and measured['expected_pages'] == 4,
           'terminal_measured_four_pages', k)
        pin(cold / 'main.pdf', measured['pdf']); pin(cold / 'main.pdf', row['pdf'])
        ck(read(cold / 'main.pdf') == read(PAPER / 'main.pdf'), 'terminal_final_pdf_unchanged', k)
        font_text = read(FINAL / (label0 + '_pdffonts.stdout')).decode()
        fonts = [s.split()[-5:] for s in font_text.splitlines()[2:] if s.strip()]
        ck(fonts and len(fonts) == row['embedded_fonts'] and all(v[0] == 'yes' for v in fonts), 'terminal_all_fonts_embedded', k)
        log = read(cold / 'main.log').decode()
        diagnostics = {key: re.findall(r'^.*' + pattern + r'.*$', log, re.M) for key, pattern in
                       [('undefined', 'undefined'), ('overfull', 'Overfull'), ('underfull', 'Underfull'), ('warnings', 'Warning')]}
        diagnostics['rerun'] = re.findall(r'^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$', log, re.M)
        ck(diagnostics == row['actual_diagnostics'] == j(FINAL / (label0 + '_DIAGNOSTICS.json'))['diagnostics'],
           'terminal_exact_measured_diagnostics', k)
        ck(all(not diagnostics[n] for n in ('undefined', 'overfull', 'rerun')), 'terminal_no_blocking_diagnostic', k)
        ck(not any(marker in read(FINAL / (label0 + '_main.txt')).decode() for marker in ('[VERIFY]', '??', '[?]')),
           'terminal_resolved_extracted_text', k)
        ck(physical(cold / 'pages') == {'page-' + str(n) + '.png' for n in range(1, 5)}, 'terminal_complete_render_set', k)
        pages.append(page_count); diagnostic_rows.append(diagnostics)
    ck(external_union == set(consumed) and generated_union == j(FINAL / 'GENERATED_LOCAL_TEX_INPUTS.json'),
       'terminal_exact_consumed_and_generated_union', 'every per-pass record retained')
    launch = TERMINAL_LAUNCH; manifest(launch)
    outer = j(launch / 'RECEIPT.json')
    ck(outer['argv'] == ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
       'pycache_prefix=' + str(FINAL / 'never_created_parent_cache'),
       str(TERMINAL_PREP / 'root_terminal_builds.py'), 'terminal-pair-after-round2']
       and outer['cwd'] == str(ROOT), 'terminal_actual_exact_parent_launch', 'unchanged prepared builder')
    ck(outer['status'] == 'PASS_ROOT_TERMINAL_LAUNCH_NOT_VIEWED' and outer['exit'] == 0 and outer['outcome'] == 'COMPLETED'
       and outer['failure'] is None and outer['inputs_unchanged'] and outer['cache_absent']
       and outer['launcher_observed_input_closure'] and outer['env'] == BUILD_ENV,
       'actual_terminal_outer_pass', 'full actual outer stream closure remains NOT_VIEWED')
    ck(outer['recorder_closure']['payloads'] == len(whole) and outer['recorder_closure']['status'] == rec['status'],
       'terminal_outer_exact_inner_seal_count', 'no prefilled future count')
    rich_pin(FINAL / 'SHA256SUMS', outer['recorder_seal'])
    outer_inputs = exact_pair(launch, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    for name in ('recorder.stdout', 'recorder.stderr'): rich_pin(launch / name, outer[name + '_pin'])
    actual_stdout = j(launch / 'recorder.stdout')
    ck(all(actual_stdout[k] == rec[k] for k in actual_stdout), 'terminal_full_outer_stdout_consistency', 'actual builder result')
    outer_coverage = {v['resolved']: {k: v[k] for k in ('sha256', 'bytes', 'resolved')} for v in outer_inputs.values()}
    for phase in ('BEFORE', 'AFTER'):
        obs = j(launch / ('LAUNCHER_RUNTIME_' + phase + '.json'))
        ck(obs['environment'] == BUILD_ENV and not obs['cache_exists'] and not Path(obs['cache_prefix']).exists(),
           'terminal_launcher_actual_settings', phase)
        ck(obs['cwd'] == str(ROOT) and obs['cache_prefix'] == str(launch / 'never_created_launcher_cache')
           and all(s in obs['flags'] for s in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')),
           'terminal_launcher_exact_flags_cwd_cache', phase)
        for path, value in obs['mapped_files'].items(): ck(outer_coverage.get(path) == value, 'terminal_launcher_map_coverage', path)
        for value in obs['modules'].values():
            ck(outer_coverage.get(value['path']) == {k: value[k] for k in ('sha256', 'bytes', 'resolved')},
               'terminal_launcher_module_coverage', value['path'])
    return {'payloads': len(whole), 'actual_commands': 32, 'sources_per_build': 8, 'pages': pages,
            'runtime': len(runtime), 'tex': len(tex), 'configuration': len(conf), 'diagnostics': diagnostic_rows,
            'builder_visual_state': rec['visual_review'], 'new_builds_or_views_by_this_auditor': 0}


def root_page_views(builds):
    record = j(BATCH / 'qa/P209_TERMINAL_ROOT_VIEWS.actual.json')
    ck(record['schema'] == 'p209-terminal-root-every-page-view-v1' and record['paper'] == 'P209'
       and record['status'] == 'ROOT_ACTUALLY_VIEWED_ALL_FOUR_FINAL_PAGES_PASS' and record['reviewer'] == '/root'
       and record['measured_page_count'] == 4 and record['open_visual_findings'] == 0
       and [row['page'] for row in record['pages']] == list(range(1, 5)),
       'actual_root_every_page_attestation', 'four actual individual observations, not hashes inferred as views')
    ck(record['terminal_manifest_sha256'] == h(FINAL / 'SHA256SUMS') and
       record['pdf_sha256'] == h(FINAL / 'cold_build_1/main.pdf'), 'root_view_exact_artifact', 'actual new terminal output')
    for page in record['pages']:
        ck(page['path'] == str(FINAL / ('cold_build_1/pages/page-' + str(page['page']) + '.png'))
           and page['actually_displayed_and_viewed'] is True and bool(page['observation'].strip()),
           'actual_root_individual_view', page['page'])
        pin(page['path'], page['sha256'])
    nonblocking = [line for row in builds['diagnostics'] for kind in ('underfull', 'warnings') for line in row[kind]]
    if nonblocking:
        ck(isinstance(record['retained_nonblocking_diagnostic'], str) and record['retained_nonblocking_diagnostic'].strip(),
           'actual_nonblocking_diagnostic_disclosed', nonblocking)
    else:
        ck(record['retained_nonblocking_diagnostic'] is None, 'no_fabricated_build_diagnostic', 'actual lists empty')
    report = read(BATCH / 'qa/P209_TERMINAL_ROOT_VIEWS.md').decode()
    ck('HOLD_EXTERNAL' in report, 'actual_view_report_external_hold', 'root report')
    return {'actually_attested_pages': 4, 'auditor_views': 0, 'root_record_sha256': h(BATCH / 'qa/P209_TERMINAL_ROOT_VIEWS.actual.json')}


def stripped_links(content):
    content = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', content)
    content = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', content)
    content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)


def pages_and_links():
    # Explicit frozen link tables preserve historical destinations and hashes.
    mapped = {}
    for number in (0, 1, 2):
        base = PAPER / ('frozen_round' + str(number))
        if number == 0:
            rows = j(base / 'FROZEN_LINK_MAP.json')['links']
        else:
            meta = j(base / ('ROUND' + str(number) + '_PROVENANCE.json'))
            rows = (meta['round1_core_link_map'] if number == 1 else meta['round2_historical_link_map'])
            rows += meta['acceptance_and_historical_anchor_link_map']
        for row in rows:
            key = (str(base / row['document']), row['href'])
            rich_pin(row['physical_target'], row['sha256'], True)
            mapped[key] = row
    origins = {}
    for (original, digest), preserved in ALIASES.items():
        if preserved.suffix == '.md' and (preserved.is_relative_to(A) or preserved.is_relative_to(B)):
            pin(preserved, digest)
            origins.setdefault(str(preserved), Path(original))
    # Semantic document origins are not historical input-hash aliases. Keep
    # both real A attempts, including the failed one, at their named origins.
    for attempt0 in ('delta_check_01', 'delta_check_02'):
        for original, row in j(A / (attempt0 + '/RESPONSE_ORIGINALS_AND_COPIES.json')).items():
            source, copied = Path(original), Path(row['copy'])
            ck(source.is_relative_to(ROOT) and copied == A / attempt0 / 'exact_response_inputs' / source.name,
               'exact_A_response_copy_origin_path', (attempt0, original))
            pin(copied, row['sha256'])
            # Four named Round2 identity-input pins are not document origins.
            # Their exact A source/copy rows supply the semantic origin; no
            # other conflict, path or hash is exempted from the original check.
            exact_self_origin_roles = {
                ('delta_check_01', 'P209_A_RESPONSE.md'):
                    (BATCH / 'P209_A_RESPONSE.md', '3b84c6c6a39b890562a63fbcb76a1a1fdf683886b9f6670b4bdd05544c6e9459'),
                ('delta_check_02', 'P209_A_RESPONSE.md'):
                    (BATCH / 'P209_A_RESPONSE.md', '3b84c6c6a39b890562a63fbcb76a1a1fdf683886b9f6670b4bdd05544c6e9459'),
                ('delta_check_01', 'P209_A_ROOT_INITIAL_INSPECTION.md'):
                    (BATCH / 'qa/P209_A_ROOT_INITIAL_INSPECTION.md', 'c095b7365d9083b83f6cd802ea6a3c9fa372a8b670ba9b28ae11e29d562fe690'),
                ('delta_check_02', 'P209_A_ROOT_INITIAL_INSPECTION.md'):
                    (BATCH / 'qa/P209_A_ROOT_INITIAL_INSPECTION.md', 'c095b7365d9083b83f6cd802ea6a3c9fa372a8b670ba9b28ae11e29d562fe690')}
            role_key = (attempt0, copied.name)
            if role_key in exact_self_origin_roles:
                named_source, named_digest = exact_self_origin_roles[role_key]
                ck(source == named_source and row['sha256'] == named_digest and origins.get(str(copied)) == copied,
                   'exact_four_A_identity_pin_semantic_origin_roles', role_key)
                origins[str(copied)] = source
            ck(str(copied) not in origins or origins[str(copied)] == source,
               'same_explicit_document_origin', str(copied))
            origins[str(copied)] = source
    # The author collector recorded an additional literal workspace/ layer.
    # Use its sealed table, not path-existence or matching-digest search.
    source_mapping = PAPER / 'source_context/MAPPING.json'
    pin(source_mapping, 'cc642a35e810b072e9cd4dcc8a9353e6fe0afc9f3c68eb2ff5546f876089245f')
    for original, row in j(source_mapping).items():
        if not row['snapshot'].startswith('source_context/workspace/'): continue
        source = Path(original)
        ck(source.is_relative_to(ROOT) and row['snapshot'] ==
           'source_context/workspace/' + source.relative_to(ROOT).as_posix(),
           'exact_author_workspace_snapshot_origin_path', original)
        copied = safe(PAPER, row['snapshot']); pin(copied, row)
        ck(str(copied) not in origins or origins[str(copied)] == source,
           'same_explicit_document_origin', str(copied))
        origins[str(copied)] = source
    failed_b_roles = j(B / 'delta_check_01/EXACT_HISTORY_ALIASES.json')
    for name, digest in [('PAPER_STATUS.md', '304c24e871a27bd02bcd6db231abc37870fb263a01d4c081289bdd53e8718a73'),
                         ('ROOT_ADOPTION.md', '8f82ae0af7156131f14e9e6e849198f8b1c98564760c30d4bc121b50cf34f82e')]:
        source = PAPER / name; copied = B / 'delta_check_01/response_anchors' / name
        ck(failed_b_roles[str(source) + ' @ ' + digest] == str(copied),
           'exact_failed_B_anchor_origin_path', name)
        pin(copied, digest)
        ck(str(copied) not in origins or origins[str(copied)] == source,
           'same_explicit_document_origin', str(copied))
        origins[str(copied)] = source
    for row in j(B / 'assignment_context/ROLES.json'): origins[row['preserved']] = Path(row['original'])
    for row in j(B / 'delta_intake_01/INTAKE_RESULT.json')['copies']: origins[row['physical']] = Path(row['original'])
    docs = [p for base in (PAPER, A, B) for p in base.rglob('*.md')]
    docs += [BATCH / n for n in ('P209_A_RESPONSE.md', 'P209_B_RESPONSE.md')]
    docs += list((BATCH / 'qa').glob('P209_*.md'))
    for doc in sorted(set(docs)):
        origin = origins.get(str(doc), doc)
        for unused in range(12):
            previous = origin
            # Physical frozen top-level links use their exact tables above.
            # For nested historical snapshots, retained workspace tails state
            # the original document directory; never search for a matching hash.
            for token in ('/source_context/', '/assignment_context/', '/exact_response_inputs/', '/original_snapshot/'):
                if token in str(origin):
                    tail = str(origin).split(token, 1)[1]
                    if tail.startswith(('docs/', 'papers/', '.agents/')) or tail in ('AGENTS.md', 'SYMBOLIC_DYNAMICS_STATE.md'):
                        origin = ROOT / tail; break
            if origin == previous: break
        ck(unused < 11, 'finite_explicit_snapshot_origin', str(doc))
        for href in stripped_links(read(doc).decode()):
            target = href.strip().strip('<>').split('#', 1)[0]
            if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target): continue
            if (str(doc), href) in mapped:
                row = mapped[(str(doc), href)]
                selected = rich_pin(row['physical_target'], row['sha256'], True)
                LINKS.append({'document': label(doc), 'semantic_origin': 'explicit-frozen-link-map', 'target': href,
                              'resolved_target': label(selected), 'sha256': row['sha256']})
            else:
                destination = (origin.parent / unquote(target)).resolve()
                ck(destination.exists(), 'local_link_closure', (label(doc), target, label(origin)))
                LINKS.append({'document': label(doc), 'semantic_origin': label(origin), 'target': target,
                              'resolved_target': label(destination)})
    return {'documents': len(set(docs)), 'local_links': len(LINKS), 'explicit_frozen_link_rows': len(mapped)}


def main():
    if sys.argv[1:] != ['terminal-artifact-after-actual-views'] or Path(__file__).resolve() != PREPARATION / 'audit_p209.py':
        raise RuntimeError('Require exact P209 prepared auditor and terminal-artifact-after-actual-views')
    if not (sys.flags.optimize == 0 and sys.flags.isolated == sys.flags.no_site == 1 and sys.dont_write_bytecode
            and Path(sys.executable).resolve() == Path('/usr/bin/python3.10') and dict(os.environ) == ENV
            and sys.pycache_prefix and not Path(sys.pycache_prefix).exists() and Path.cwd() == ROOT):
        raise RuntimeError('Require exact isolated system interpreter, minimal ENV, absent cache and workspace cwd')
    began = datetime.now(timezone.utc).isoformat()
    manifest(PREPARATION)
    runtime_before = actual_auditor_runtime()
    history = load_aliases()
    revision = revision_originals_and_failure()
    whole = manifest(PAPER, 'PAPER_MANIFEST.sha256')
    frozen = frozen_and_author()
    accepted = reviews(history)
    replays = strict_replays()
    builds = terminal()
    views = root_page_views(builds)
    links = pages_and_links()
    lifecycle = read(PAPER / 'ROOT_LIFECYCLE.md').decode()
    ck(all(word in lifecycle for word in ('P209', 'HOLD_EXTERNAL', 'ARTIFACT_GATE_PENDING')) and
       'P209_INTERNALLY_COMPLETE' not in lifecycle, 'separate_pending_root_lifecycle', 'not historical PAPER_STATUS')
    runtime_after = actual_auditor_runtime()
    before = dict(READS)
    for path, wanted in before.items():
        raw = Path(path).read_bytes()
        ck(wanted == {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}, 'final_every_read_input_recheck', path)
    for path, resolved in HOST_RESOLUTIONS.items():
        ck(str(Path(path).resolve(strict=True)) == resolved, 'final_host_resolution_recheck', path)
    print(json.dumps({'schema': 'p209-terminal-artifact-audit-v1', 'paper': 'P209',
        'status': 'PASS_P209_TERMINAL_ARTIFACT_GATE', 'started_utc': began,
        'ended_utc': datetime.now(timezone.utc).isoformat(), 'auditor_sha256': h(Path(__file__).resolve()),
        'checks': sum(CHECKS.values()), 'checks_by_section': dict(CHECKS),
        'infrastructure_revision': revision,
        'whole_paper_manifest_entries': len(whole), 'frozen_and_author': frozen, 'accepted_reviews': accepted,
        'root_strict_replays_reused': replays, 'terminal_builds': builds, 'actual_root_views': views, 'link_summary': links,
        'complete_manifests_validated': MANIFESTS, 'explicit_historical_aliases_used': USED_ALIASES,
        'actual_auditor_runtime_before': runtime_before, 'actual_auditor_runtime_after': runtime_after,
        'host_path_resolutions_rechecked': HOST_RESOLUTIONS, 'all_local_links_checked': LINKS,
        'all_consumed_input_count': len(before), 'all_consumed_inputs_rechecked': before,
        'lifecycle_role': 'ROOT_LIFECYCLE.md; original PAPER_STATUS.md and ROOT_ADOPTION.md immutable',
        'fresh_mathematical_executions': 0, 'fresh_builds': 0, 'fresh_page_views': 0,
        'role': 'Read-only scoped artifact infrastructure, not a third review or an acceptance decision.',
        'limits': ['Original proof/source judgment remains controlling; no new all-size theorem or novelty claim.',
                   'Existing author/A/B pairs are reused with complete unchanged recorded inputs and settings.',
                   'Actual root every-page attestations are checked, never synthesized from PNG existence.',
                   'Known inventories and sampled process observations are not OS-hermetic or continuous/startup/grandchild tracing.',
                   'Later lifecycle-only changes require exact old-byte preservation and a separate follow-up.',
                   'This P209 paper-level gate is not the five-paper final gate or external clearance.'],
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__': main()
