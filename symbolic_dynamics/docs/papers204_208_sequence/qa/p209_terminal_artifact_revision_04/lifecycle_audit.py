#!/usr/bin/env python3
"""P209 lifecycle-only adaptation of P208's accepted follow-up infrastructure.
Prepared source is not execution or acceptance. Actual future root acceptance
and exact pre-update physical preservation are required; no old auditor,
scientific producer or builder is imported or executed.
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
import subprocess
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
A, B = [BATCH / ('reviews/p209_' + x) for x in ('a', 'b')]
FINAL = PAPER / 'qa_final'
PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_04'
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


def stripped_links(content):
    content = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', content)
    content = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', content)
    content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)


WORK = OUT / 'lifecycle_before'
SOURCE = Path(__file__).resolve()
ROOT_GATE = BATCH / 'qa/P209_TERMINAL_ARTIFACT_ROOT_INSPECTION.actual.json'
ROOT_REPORT = BATCH / 'qa/P209_TERMINAL_ARTIFACT_ROOT_INSPECTION.md'


def save(path, raw):
    with Path(path).open('xb') as stream: stream.write(raw)


def dump(path, value):
    save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def info(path):
    raw = read(path)
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def actual_initial_gate():
    gate = j(ROOT_GATE)
    ck(gate['schema'] == 'p209-terminal-artifact-root-original-closure-v1'
       and gate['status'] == 'PASS_ROOT_P209_TERMINAL_ARTIFACT_COMPLETE_ORIGINAL_CLOSURE'
       and gate['paper'] == 'P209' and gate['actual_exit_code'] == 0
       and gate['current_open_findings'] == 0, 'actual_root_initial_acceptance', 'not a prepared template')
    stdout = Path(gate['audit_stdout']['path'])
    ck(stdout.is_relative_to(OUT) and stdout.name == 'audit.stdout' and
       stdout.parent.parent == OUT and re.fullmatch(r'initial_\d+', stdout.parent.name),
       'actual_stdout_exact_scoped_attempt', str(stdout))
    pin(stdout, gate['audit_stdout'])
    pin(PREPARATION / 'audit_p209.py', gate['auditor_sha256'])
    original = j(stdout)
    ck(original['schema'] == 'p209-terminal-artifact-audit-v1' and
       original['status'] == 'PASS_P209_TERMINAL_ARTIFACT_GATE'
       and original['paper'] == 'P209' and
       original['auditor_sha256'] == gate['auditor_sha256'] and
       original['all_consumed_input_count'] == len(original['all_consumed_inputs_rechecked']) ==
       gate['all_consumed_input_count'], 'actual_initial_full_audit_result', 'exact dynamically measured fields')
    manifest(stdout.parent)
    command0 = j(stdout.parent / 'COMMAND.json')
    ck(command0['exit_code'] == 0 and command0['inputs_unchanged'] and command0['unused_cache_absent'],
       'actual_initial_auditor_process', 'retained exact successful child')
    for stream in ('stdout', 'stderr'): pin(stdout.parent / ('audit.' + stream), command0[stream])
    ck(read(stdout.parent / 'audit.stderr') == b'', 'actual_initial_empty_stderr', str(stdout))
    report = read(ROOT_REPORT).decode()
    ck('HOLD_EXTERNAL' in report, 'actual_root_initial_hold', str(ROOT_REPORT))
    return gate, original


def old_package(gate):
    preserved = WORK / 'INITIAL_PACKAGE_SHA256SUMS'
    pin(preserved, gate['audit_package_manifest_sha256'])
    old = manifest_rows(preserved)
    ck('SHA256SUMS' not in old and len(old) == gate['audit_package_payloads'],
       'initial_entire_nonself_package', 'actual measured count')
    for name, digest in old.items(): pin(safe(OUT, name), digest)
    ck(read(WORK / 'INITIAL_REPORT.md') == read(OUT / 'REPORT.md'),
       'original_report_exact_unchanged', 'initial report is never rewritten')
    return old


def prepare():
    # Invoked only by root AFTER actual original acceptance, BEFORE status edit.
    gate, original = actual_initial_gate()
    ck(not WORK.exists(), 'exclusive_initial_preservation', str(WORK))
    pin(OUT / 'SHA256SUMS', gate['audit_package_manifest_sha256'])
    old = manifest(OUT, count=gate['audit_package_payloads'])
    lifecycle, paperseal = PAPER / 'ROOT_LIFECYCLE.md', PAPER / 'PAPER_MANIFEST.sha256'
    body = read(lifecycle).decode()
    ck('ARTIFACT_GATE_PENDING' in body and 'P209_INTERNALLY_COMPLETE' not in body and
       'HOLD_EXTERNAL' in body, 'preserve_pending_status_before_edit', 'distinct author status immutable')
    manifest(PAPER, 'PAPER_MANIFEST.sha256')
    ledger = original['all_consumed_inputs_rechecked']
    for path in (lifecycle, paperseal):
        ck(str(path) in ledger, 'exact_initial_paper_alias_input', str(path)); pin(path, ledger[str(path)])
    WORK.mkdir(exist_ok=False)
    sources = {
        'INITIAL_PACKAGE_SHA256SUMS': OUT / 'SHA256SUMS',
        'INITIAL_REPORT.md': OUT / 'REPORT.md',
        'ROOT_LIFECYCLE.md': lifecycle,
        'PAPER_MANIFEST.sha256': paperseal,
        'ROOT_GATE.actual.json': ROOT_GATE,
        'ROOT_GATE.md': ROOT_REPORT,
    }
    copied = {}
    for name, origin in sources.items():
        raw = read(origin); save(WORK / name, raw)
        ck(read(WORK / name) == raw, 'physical_exact_preupdate_copy', name)
        copied[str(origin)] = {'copy': str(WORK / name), **info(origin)}
    record = {'status': 'PASS_EXACT_PREUPDATE_PRESERVATION_NOT_LIFECYCLE_ACCEPTANCE',
        'utc': datetime.now(timezone.utc).isoformat(), 'initial_package_payloads': len(old),
        'initial_package_sha256': gate['audit_package_manifest_sha256'],
        'initial_audit_stdout': gate['audit_stdout'], 'root_gate': info(ROOT_GATE), 'copies': copied,
        'exact_two_paper_alias_paths': [str(lifecycle), str(paperseal)], 'source': info(SOURCE),
        'new_scientific_executions': 0, 'new_builds': 0, 'new_views': 0}
    dump(WORK / 'PRESERVATION.json', record)
    files = sorted(p for p in WORK.rglob('*') if p.is_file())
    save(WORK / 'SHA256SUMS', ''.join(info(p)['sha256'] + '  ' + p.relative_to(WORK).as_posix() + '\n' for p in files).encode())
    manifest(WORK)
    print(json.dumps(record, sort_keys=True, indent=2))


def changed_paper(original):
    previous = manifest_rows(WORK / 'PAPER_MANIFEST.sha256')
    current = manifest(PAPER, 'PAPER_MANIFEST.sha256')
    ck(set(current) == set(previous), 'unchanged_whole_paper_names', 'no added or removed payload')
    changed = [name for name in previous if previous[name] != current[name]]
    ck(changed == ['ROOT_LIFECYCLE.md'], 'only_new_root_lifecycle_payload_changed', changed)
    for path, saved in [(PAPER / 'ROOT_LIFECYCLE.md', WORK / 'ROOT_LIFECYCLE.md'),
                        (PAPER / 'PAPER_MANIFEST.sha256', WORK / 'PAPER_MANIFEST.sha256')]:
        pin(saved, original['all_consumed_inputs_rechecked'][str(path)])
    oldraw = read(WORK / 'PAPER_MANIFEST.sha256')
    needle = (previous['ROOT_LIFECYCLE.md'] + '  ROOT_LIFECYCLE.md\n').encode()
    replacement = (current['ROOT_LIFECYCLE.md'] + '  ROOT_LIFECYCLE.md\n').encode()
    ck(oldraw.count(needle) == 1 and read(PAPER / 'PAPER_MANIFEST.sha256') ==
       oldraw.replace(needle, replacement), 'literal_single_rollup_line_change', 'all other bytes identical')
    content = read(PAPER / 'ROOT_LIFECYCLE.md').decode()
    ck('P209_INTERNALLY_COMPLETE' in content and 'HOLD_EXTERNAL' in content and
       'ARTIFACT_GATE_PENDING' not in content, 'actual_root_completion_body', 'P209 only; external hold unchanged')
    pin(PAPER / 'PAPER_STATUS.md', '304c24e871a27bd02bcd6db231abc37870fb263a01d4c081289bdd53e8718a73')
    pin(PAPER / 'ROOT_ADOPTION.md', '8f82ae0af7156131f14e9e6e849198f8b1c98564760c30d4bc121b50cf34f82e')
    return {'whole_payloads': len(current), 'changed_payloads': changed,
        'old_lifecycle_sha256': previous['ROOT_LIFECYCLE.md'], 'new_lifecycle_sha256': current['ROOT_LIFECYCLE.md'],
        'old_whole_manifest_sha256': h(WORK / 'PAPER_MANIFEST.sha256'),
        'new_whole_manifest_sha256': h(PAPER / 'PAPER_MANIFEST.sha256')}


def recheck_resources(original):
    for role in ('author', 'a', 'b'):
        base = BATCH / ('qa/root_replays/p209_' + role + '_strict/root_' + role + '_pair_01')
        modern_presence(base)
        runtime = exact_pair(base, 'RUNTIME_BEFORE.json', 'RUNTIME_AFTER.json')
        ck(declared_runtime_names() <= set(runtime), 'unchanged_strict_declared_runtime_membership', role)
    runtime, tex, conf = terminal_resource_key()
    ledger = original['all_consumed_inputs_rechecked']
    for group in (runtime, tex):
        for path, value in group.items():
            ck(ledger.get(path) == {key: value[key] for key in ('sha256', 'bytes')},
               'entire_resource_retained_in_original_ledger', path)
    return {'runtime': len(runtime), 'tex': len(tex), 'configuration': len(conf)}


def new_links():
    result = []
    for path in (PAPER / 'ROOT_LIFECYCLE.md', BATCH / 'P209_FINAL_QA.md', ROOT_REPORT):
        content = read(path).decode()
        ck('HOLD_EXTERNAL' in content, 'new_document_external_hold', str(path))
        if path != ROOT_REPORT:
            ck('P209_INTERNALLY_COMPLETE' in content, 'new_document_p209_only_completion', str(path))
        for target in stripped_links(content):
            href = target.strip().strip('<>').split('#', 1)[0]
            if not href or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', href): continue
            resolved = (path.parent / unquote(href)).resolve()
            ck(resolved.exists(), 'new_lifecycle_link_closure', (str(path), href))
            result.append({'document': str(path), 'target': href, 'resolved_target': str(resolved)})
    return result


def original_runtime_coverage(sample, ledger):
    for path, value in sample['mapped_files'].items():
        ck(ledger.get(path) == value, 'own_map_covered_by_original_ledger', path)
    for value in sample['modules'].values():
        wanted = {k: value[k] for k in ('sha256', 'bytes')}
        ck(ledger.get(value['path']) == wanted, 'own_module_covered_by_original_ledger', value['path'])


def audit():
    began = datetime.now(timezone.utc).isoformat()
    manifest(PREPARATION); manifest(WORK)
    prepared = j(WORK / 'PRESERVATION.json')
    ck(prepared['status'] == 'PASS_EXACT_PREUPDATE_PRESERVATION_NOT_LIFECYCLE_ACCEPTANCE',
       'actual_preupdate_preservation', 'not acceptance')
    pin(SOURCE, prepared['source'])
    gate, original = actual_initial_gate()
    pin(ROOT_GATE, prepared['root_gate'])
    initial = old_package(gate)
    lifecycle = PAPER / 'ROOT_LIFECYCLE.md'; paperseal = PAPER / 'PAPER_MANIFEST.sha256'
    exact = {str(lifecycle): WORK / 'ROOT_LIFECYCLE.md', str(paperseal): WORK / 'PAPER_MANIFEST.sha256'}
    ck(prepared['exact_two_paper_alias_paths'] == list(exact), 'exact_two_alias_scope', 'no other drift accepted')
    for original_path, row in prepared['copies'].items():
        pin(row['copy'], row)
        if original_path not in exact and original_path != str(OUT / 'SHA256SUMS'):
            pin(original_path, row)
    ledger = original['all_consumed_inputs_rechecked']
    early = actual_auditor_runtime()
    original_runtime_coverage(early, ledger)
    for name, value in ledger.items(): pin(exact.get(name, Path(name)), value)
    change = changed_paper(original)
    for record in original['complete_manifests_validated']:
        base = Path(record['base']); base = base if base.is_absolute() else ROOT / base
        if base == PAPER and record['name'] == 'PAPER_MANIFEST.sha256': continue
        pin(base / record['name'], record['sha256'])
        manifest(base, record['name'], record['complete_nonself'], record['entries'])
    resources = recheck_resources(original)
    for name, resolution in original['host_path_resolutions_rechecked'].items():
        ck(str(Path(name).resolve(strict=True)) == resolution, 'all_original_host_resolutions', name)
    for row in original['all_local_links_checked']:
        path = Path(row['resolved_target']); path = path if path.is_absolute() else ROOT / path
        ck(path.exists(), 'original_link_still_exists', str(path))
    links = new_links()
    late = actual_auditor_runtime()
    original_runtime_coverage(late, ledger)
    for name, value in ledger.items(): pin(exact.get(name, Path(name)), value)
    for name, resolution in original['host_path_resolutions_rechecked'].items():
        ck(str(Path(name).resolve(strict=True)) == resolution, 'all_original_host_resolutions_after', name)
    ck(change == changed_paper(original), 'same_exact_change_after', 'one lifecycle payload')
    old_package(gate)
    consumed = dict(READS)
    for name, wanted in consumed.items():
        raw = Path(name).read_bytes()
        ck(wanted == {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}, 'all_current_inputs_rechecked_after', name)
    print(json.dumps({'schema': 'p209-lifecycle-only-followup-v1', 'paper': 'P209',
        'status': 'PASS_P209_LIFECYCLE_ONLY_FOLLOWUP', 'started_utc': began,
        'ended_utc': datetime.now(timezone.utc).isoformat(), 'checks': sum(CHECKS.values()),
        'checks_by_section': dict(CHECKS), 'initial_package_payloads_preserved': len(initial),
        'initial_package_sha256': gate['audit_package_manifest_sha256'],
        'initial_audit_stdout': gate['audit_stdout'], 'initial_root_gate': info(ROOT_GATE),
        'original_ledger_paths_checked_twice': len(ledger), 'exact_two_old_paper_aliases': {k: str(v) for k, v in exact.items()},
        'paper_change': change, 'current_resource_key': resources,
        'original_links_rechecked': len(original['all_local_links_checked']), 'new_links_checked': links,
        'actual_runtime_before': early, 'actual_runtime_after': late,
        'all_current_read_input_count': len(consumed), 'all_current_read_inputs_rechecked': consumed,
        'new_scientific_executions': 0, 'new_builds': 0, 'new_page_views': 0,
        'role': 'Lifecycle-only reuse after actual accepted initial artifact gate; no third review or new science/build/view.',
        'limits': ['Exactly two preserved old-paper aliases; historical author status/adoption and all initial evidence immutable.',
                   'Complete known input and resource sets with sampled own runtime, not OS-hermetic or continuous tracing.',
                   'Paper P209 only; no five-paper completion, Git or external clearance.'],
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))


def run(label0):
    ck(re.fullmatch(r'lifecycle_\d+', label0) is not None, 'safe_exclusive_attempt_label', label0)
    target = OUT / label0; target.mkdir(exist_ok=False)
    save(target / 'executed_source_snapshot.py', read(SOURCE))
    source_before = info(SOURCE)
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(target / 'unused_pycache'), str(SOURCE), 'child']
    attempt = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
        'started_utc': datetime.now(timezone.utc).isoformat(), 'status': 'ATTEMPTED', 'exit_code': None}
    dump(target / 'ATTEMPT.json', attempt)
    failure = None
    try:
        child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        code, stdout, stderr = child.returncode, child.stdout, child.stderr
    except OSError as exc:
        failure = repr(exc); code, stdout, stderr = 127, b'', str(exc).encode()
    save(target / 'audit.stdout', stdout); save(target / 'audit.stderr', stderr)
    raw = SOURCE.read_bytes(); source_after = {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
    command0 = {**attempt, 'status': 'COMPLETED' if failure is None else 'SPAWN_FAILED', 'failure': failure,
        'ended_utc': datetime.now(timezone.utc).isoformat(), 'exit_code': code,
        'source_before': source_before, 'source_after': source_after, 'source_unchanged': source_before == source_after,
        'unused_cache_absent': not (target / 'unused_pycache').exists(),
        'stdout': info(target / 'audit.stdout'), 'stderr': info(target / 'audit.stderr')}
    dump(target / 'COMMAND.json', command0)
    files = sorted(p for p in target.rglob('*') if p.is_file())
    save(target / 'SHA256SUMS', ''.join(info(p)['sha256'] + '  ' + p.relative_to(target).as_posix() + '\n' for p in files).encode())
    manifest(target)
    print(json.dumps(command0, sort_keys=True, indent=2))
    if code: print(stderr.decode(errors='replace'), file=sys.stderr)
    else:
        result = json.loads(stdout)
        print(json.dumps({k: result[k] for k in ('status', 'checks', 'all_current_read_input_count')}, sort_keys=True))
    ck(command0['source_unchanged'] and command0['unused_cache_absent'], 'actual_outer_controls_after', label0)
    raise SystemExit(code)


def seal(label0):
    ck(re.fullmatch(r'lifecycle_\d+', label0) is not None, 'safe_seal_attempt_label', label0)
    gate, original = actual_initial_gate()
    initial = old_package(gate)
    pin(OUT / 'SHA256SUMS', gate['audit_package_manifest_sha256'])
    target = OUT / label0; manifest(target)
    row, result = j(target / 'COMMAND.json'), j(target / 'audit.stdout')
    ck(row['exit_code'] == 0 and row['source_unchanged'] and row['unused_cache_absent']
       and row['failure'] is None and result['status'] == 'PASS_P209_LIFECYCLE_ONLY_FOLLOWUP',
       'actual_lifecycle_pass_before_seal', label0)
    for stream in ('stdout', 'stderr'): pin(target / ('audit.' + stream), row[stream])
    ck(read(target / 'audit.stderr') == b'', 'actual_lifecycle_empty_stderr', label0)
    pin(SOURCE, row['source_before'])
    for name, value in result['all_current_read_inputs_rechecked'].items(): pin(name, value)
    report = info(OUT / 'LIFECYCLE_REPORT.md')
    receipt = {'status': 'PASS_COMPLETE_P209_INITIAL_AND_LIFECYCLE_PACKAGE_SEAL',
        'utc': datetime.now(timezone.utc).isoformat(), 'initial_payloads_preserved': len(initial),
        'initial_package_sha256': gate['audit_package_manifest_sha256'],
        'initial_package_archived': str(WORK / 'INITIAL_PACKAGE_SHA256SUMS'),
        'followup_command': info(target / 'COMMAND.json'), 'followup_stdout': info(target / 'audit.stdout'),
        'followup_source': info(SOURCE), 'followup_report': report,
        'boundary': 'Only the own artifact package outer seal is replaced after preserving its old bytes; no paper edit.'}
    dump(OUT / 'LIFECYCLE_SEAL_RECEIPT.json', receipt)
    values = [(info(p)['sha256'], p.relative_to(OUT).as_posix()) for p in sorted(OUT.rglob('*'))
              if p.is_file() and p != OUT / 'SHA256SUMS']
    temporary = OUT / 'SHA256SUMS.next'
    save(temporary, ''.join(d + '  ' + n + '\n' for d, n in values).encode())
    pin(OUT / 'SHA256SUMS', gate['audit_package_manifest_sha256'])
    temporary.replace(OUT / 'SHA256SUMS')
    READS.pop(str(OUT / 'SHA256SUMS'))
    complete = manifest(OUT)
    old_package(gate)
    print(json.dumps({'status': receipt['status'], 'payloads': len(complete),
        'manifest_sha256': h(OUT / 'SHA256SUMS'), 'followup_stdout_sha256': row['stdout']['sha256']},
        sort_keys=True, indent=2))


if __name__ == '__main__':
    if not(sys.flags.optimize == 0 and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
           and dict(os.environ) == ENV and Path.cwd() == ROOT and Path(sys.executable).resolve() == Path('/usr/bin/python3.10')
           and SOURCE == PREPARATION / 'lifecycle_audit.py'):
        raise RuntimeError('Require prepared P209 helper, isolated system interpreter, minimal ENV and workspace cwd')
    if sys.argv[1:] == ['prepare']: prepare()
    elif sys.argv[1:] == ['child']:
        ck(sys.pycache_prefix and not Path(sys.pycache_prefix).exists(), 'absent_child_cache_prefix', sys.pycache_prefix)
        audit()
    elif len(sys.argv) == 3 and sys.argv[1] == 'run': run(sys.argv[2])
    elif len(sys.argv) == 3 and sys.argv[1] == 'seal': seal(sys.argv[2])
    else: raise RuntimeError('Require prepare, run lifecycle_N, child or seal lifecycle_N')
