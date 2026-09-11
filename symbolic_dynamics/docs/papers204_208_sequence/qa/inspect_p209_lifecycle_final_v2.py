#!/usr/bin/env python3
"""Prepared read-only final P209 lifecycle original inspector; root must execute.
No import or execution of a previous auditor, lifecycle helper, proof, build or
viewer. The preparer also authored revision04: this is documentary preparation,
not independent mathematical review or acceptance. Only subprocess is raw cmp.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import sysconfig
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
OUT = BATCH / 'qa/p209_terminal_artifact'
WORK = OUT / 'lifecycle_before'
PREP = BATCH / 'qa/p209_terminal_artifact_revision_04'
SOURCE = PREP / 'lifecycle_audit.py'
HELPER_SHA = 'bcd8c981f716cc1a6caa15bbe1aff4ecbe0e680777d39e7a7ab879773c756e23'
INITIAL_SHA = '2c92605aff6e426d026f2a2f7a3893c0a9659dd664df592fe8b3749da8733bd4'
GATE = BATCH / 'qa/P209_TERMINAL_ARTIFACT_ROOT_INSPECTION.actual.json'
GATE_MD = GATE.with_name('P209_TERMINAL_ARTIFACT_ROOT_INSPECTION.md')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
ALIASES = {str(PAPER / name): WORK / name for name in ('ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256')}
READS, CHECKS, CMPS = {}, Counter(), []
TEX_ROOTS = tuple(map(Path, ('/usr/share/texlive/texmf-dist', '/usr/share/texmf', '/var/lib/texmf', '/etc/texmf', '/usr/local/share/texmf', '/root/texmf', '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')))
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
CONFIG_ROOTS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/share/fonts', '/etc/fonts', '/var/cache/fontconfig', '/usr/share/fontconfig', '/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/usr/share/poppler', '/usr/local/share/fonts', '/etc/xdg/fontconfig', '/etc/profile.d', '/root/.fonts', '/root/.fontconfig', '/root/.fonts.conf.d', '/root/.config/fontconfig', '/root/.cache/fontconfig', '/root/.local/share/fonts')))
TOOLS = tuple(Path('/usr/bin') / n for n in ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo', 'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp')) + tuple(map(Path, ('/bin/bash', '/bin/sh', '/usr/bin/env', '/usr/bin/python3.10')))


def ck(test, section, detail):
    CHECKS[section] += 1
    if not test:
        raise AssertionError((section, detail))


def absolute(path):
    path = Path(path)
    return path if path.is_absolute() else ROOT / path


def raw(path):
    path = absolute(path)
    ck(path.is_file(), 'regular_file', str(path))
    if path.is_relative_to(ROOT):
        ck(not path.is_symlink(), 'workspace_regular', str(path))
    data = path.read_bytes()
    value = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    ck(str(path) not in READS or READS[str(path)] == value, 'read_stability', str(path))
    READS[str(path)] = value
    return data


def info(path):
    data = raw(path)
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def pin(path, wanted):
    path = absolute(path)
    value = info(path)
    ck(value['sha256'] == (wanted if isinstance(wanted, str) else wanted['sha256']), 'hash', str(path))
    if isinstance(wanted, dict):
        if 'bytes' in wanted:
            ck(value['bytes'] == wanted['bytes'], 'bytes', str(path))
        if 'resolved' in wanted:
            ck(str(path.resolve(strict=True)) == wanted['resolved'], 'resolution', str(path))
        if 'symlink' in wanted:
            ck((os.readlink(path) if path.is_symlink() else None) == wanted['symlink'], 'symlink', str(path))
    return value


def obj(path):
    return json.loads(raw(path))


def rows(path):
    result = {}
    data = raw(path)
    ck(data.endswith(b'\n'), 'manifest_final_lf', str(path))
    for line in data.decode().split('\n')[:-1]:
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(match is not None, 'manifest_syntax', str(path))
        digest, name = match.groups()
        p = Path(name)
        ck(p.parts and not p.is_absolute() and '..' not in p.parts and name not in result, 'manifest_safe_unique', name)
        result[name] = digest
    return result


def physical(base):
    names = set()
    for path in base.rglob('*'):
        ck(not path.is_symlink(), 'inventory_no_symlink', str(path))
        if path.is_file():
            names.add(path.relative_to(base).as_posix())
    return names


def manifest(base, name='SHA256SUMS', count=None, complete=True, wanted=None):
    if wanted is not None:
        pin(base / name, wanted)
    values = rows(base / name)
    ck(name not in values, 'manifest_nonself', str(base))
    if count is not None:
        ck(len(values) == count, 'manifest_count', (str(base), count))
    if complete:
        ck(set(values) == physical(base) - {name}, 'manifest_full_inventory', str(base))
    for name0, digest in values.items():
        pin(base / name0, digest)
    return values


def full_ledger(ledger, old=False):
    for path, value in ledger.items():
        ck(Path(path).is_absolute() and set(value) == {'sha256', 'bytes'}, 'ledger_schema', path)
        pin(ALIASES.get(path, Path(path)) if old else path, value)


def native(base, source, final_arg, lifecycle=False):
    command, attempt = obj(base / 'COMMAND.json'), obj(base / 'ATTEMPT.json')
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(base / 'unused_pycache'), str(source), final_arg]
    ck(command['argv'] == argv and command['cwd'] == str(ROOT) and command['environment'] == ENV, 'native_exact_invocation', str(base))
    ck(command['status'] == 'COMPLETED' and command['exit_code'] == 0 and command['failure'] is None and command['unused_cache_absent'] is True, 'native_actual_success', str(base))
    ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and all(attempt[k] == command[k] for k in ('argv', 'cwd', 'environment', 'started_utc')), 'native_prespawn_record', str(base))
    ck(datetime.fromisoformat(command['started_utc']) < datetime.fromisoformat(command['ended_utc']), 'native_chronology', str(base))
    ck(not (base / 'unused_pycache').exists(), 'native_cache_absent_now', str(base))
    for stream in ('stdout', 'stderr'):
        pin(base / ('audit.' + stream), command[stream])
    ck(raw(base / 'audit.stderr') == b'', 'native_full_empty_stderr', str(base))
    if lifecycle:
        ck(command['source_before'] == command['source_after'] and command['source_unchanged'] is True, 'native_source_interval', str(base))
        pin(source, command['source_before'])
        ck(raw(source) == raw(base / 'executed_source_snapshot.py'), 'native_exact_source_copy', str(base))
        ck(set(manifest(base, count=5)) == {'COMMAND.json', 'ATTEMPT.json', 'audit.stdout', 'audit.stderr', 'executed_source_snapshot.py'}, 'native_five_payloads', str(base))
    else:
        before = obj(base / 'INPUTS_BEFORE.json')
        ck(command['inputs_unchanged'] is True and before == obj(base / 'INPUTS_AFTER.json') and len(before) == 19, 'initial_native_input_interval', str(base))
        # Exact two old-paper roles also apply to the original native 19-input
        # record, not only its embedded complete ledger. Never map current inputs.
        for name, value in before.items():
            pin(ALIASES.get(name, Path(name)), value)
        manifest(base, count=8)
    return command, obj(base / 'audit.stdout')


def compare(left, right):
    before = {str(p): info(p) for p in (left, right)}
    argv = ['/usr/bin/cmp', '--', str(left), str(right)]
    result = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'exit_code': result.returncode,
           'stdout': result.stdout.decode(), 'stderr': result.stderr.decode(), 'inputs_before': before,
           'inputs_after': {str(p): info(p) for p in (left, right)}}
    CMPS.append(row)
    ck(row['inputs_before'] == row['inputs_after'] and result.returncode == 0 and not result.stdout and not result.stderr, 'fresh_native_full_cmp', argv)


def links(text):
    text = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', text)
    text = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', text)
    text = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', text)
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', text)


def href(value):
    value = value.strip().strip('<>').split('#', 1)[0]
    return value if value and not re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', value) else None


def link_closure(original):
    mapping = {}
    for n in range(3):
        base = PAPER / ('frozen_round' + str(n))
        if n == 0:
            records = obj(base / 'FROZEN_LINK_MAP.json')['links']
        else:
            meta = obj(base / ('ROUND' + str(n) + '_PROVENANCE.json'))
            records = meta['round1_core_link_map' if n == 1 else 'round2_historical_link_map'] + meta['acceptance_and_historical_anchor_link_map']
        for row in records:
            mapping[(str(base / row['document']), row['href'])] = row
    ck(len(mapping) == 779, 'original_frozen_link_table_count', len(mapping))
    grouped = defaultdict(list)
    old_aliases = original['explicit_historical_aliases_used']
    ck(len(old_aliases) == 94, 'original_named_historical_roles_count', 94)
    for key, selected in old_aliases.items():
        origin, digest = key.rsplit(' @ ', 1)
        ck(Path(origin).is_absolute() and Path(selected).is_absolute(), 'original_alias_absolute', key)
        pin(selected, digest)
    for row in original['all_local_links_checked']:
        document = absolute(row['document'])
        grouped[document].append(row)
        destination = absolute(row['resolved_target'])
        ck(destination.exists(), 'original_link_exists', str(destination))
        if row['semantic_origin'] == 'explicit-frozen-link-map':
            recorded = mapping[(str(document), row['target'])]
            selected = old_aliases.get(recorded['physical_target'] + ' @ ' + recorded['sha256'], recorded['physical_target'])
            ck(destination == absolute(selected) and row['sha256'] == recorded['sha256'], 'original_frozen_link_exact_role', row)
            pin(destination, row['sha256'])
        else:
            derived = (absolute(row['semantic_origin']).parent / unquote(row['target'])).resolve()
            ck(derived == destination, 'original_link_semantic_resolution', row)
    for document, records in grouped.items():
        selected = ALIASES.get(str(document), document)
        pin(selected, original['all_consumed_inputs_rechecked'][str(document)])
        actual = Counter(href(value) for value in links(raw(selected).decode()) if href(value))
        expected = Counter(href(row['target']) for row in records)
        ck(actual == expected, 'original_document_entire_link_multiset', str(document))
    ck(len(original['all_local_links_checked']) == 1534, 'original_link_count', 1534)
    result = []
    for document in (PAPER / 'ROOT_LIFECYCLE.md', BATCH / 'P209_FINAL_QA.md', GATE_MD):
        text = raw(document).decode()
        ck('HOLD_EXTERNAL' in text and (document == GATE_MD or 'P209_INTERNALLY_COMPLETE' in text), 'new_document_boundary', str(document))
        for value in links(text):
            target = href(value)
            if target:
                destination = (document.parent / unquote(target)).resolve()
                ck(destination.exists(), 'new_link_exists', (str(document), target))
                result.append({'document': str(document), 'target': target, 'resolved_target': str(destination)})
    return result


def runtime(sample, ledger, cache):
    ck(sample['environment'] == ENV and sample['executable'] == '/usr/bin/python3.10' and sample['pycache_prefix'] == str(cache) and not cache.exists(), 'lifecycle_actual_runtime_settings', str(cache))
    ck(all(value in sample['flags'] for value in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')), 'lifecycle_actual_runtime_flags', sample['flags'])
    for path, value in sample['mapped_files'].items():
        ck(ledger.get(path) == value, 'lifecycle_mapped_original_coverage', path)
        pin(path, value)
    for value in sample['modules'].values():
        wanted = {k: value[k] for k in ('sha256', 'bytes')}
        ck(ledger.get(value['path']) == wanted and not value['path'].endswith(('.pyc', '.pyo')), 'lifecycle_module_original_coverage', value['path'])
        pin(value['path'], wanted)
    return {'mapped_files': len(sample['mapped_files']), 'modules': len(sample['modules'])}


def declared_runtime(build=False):
    names = set()
    for directory, folders, files in os.walk('/usr/lib/python3.10'):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for base in LIB_ROOTS:
        if base.is_dir():
            candidates = base.glob('*') if str(base) == '/usr/local/lib' else base.rglob('*')
            names.update(str(p) for p in candidates if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    names.update(('/usr/bin/env', '/usr/bin/cmp', '/usr/bin/ldd', '/bin/bash', '/bin/sh', '/usr/bin/python3.10'))
    if build:
        names.update('/usr/bin/' + n for n in ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo', 'pdffonts', 'pdftotext', 'pdftoppm'))
    return names


def configuration(values):
    for name, row in values.items():
        p = Path(name)
        ck(p.exists() == row['exists'], 'configuration_existence', name)
        if 'resolved' in row:
            ck(str(p.resolve()) == row['resolved'], 'configuration_resolution', name)
        if 'is_file' in row:
            ck(p.is_file() == row['is_file'], 'configuration_kind', name)
        if row.get('sha256') is not None:
            pin(p, row)
        elif 'sha256' in row:
            ck(not p.is_file(), 'configuration_absent_hash', name)


def paired(base, stem):
    before = obj(base / (stem + '_BEFORE.json'))
    ck(before == obj(base / (stem + '_AFTER.json')), 'resource_exact_interval', (str(base), stem))
    return before


def resources(ledger):
    for role in ('author', 'a', 'b'):
        base = BATCH / ('qa/root_replays/p209_' + role + '_strict/root_' + role + '_pair_01')
        conf = paired(base, 'CONFIGURATION')
        configuration(conf['optional'])
        for name, wanted in conf['directories'].items():
            p = Path(name)
            current = sorted(str(q) for q in p.rglob('*') if q.is_file()) if p.is_dir() else None
            ck(current == wanted, 'strict_full_config_membership', name)
        group = paired(base, 'RUNTIME')
        ck(declared_runtime() <= set(group), 'strict_declared_runtime_membership', role)
        for name, value in group.items():
            pin(name, value)
    base = PAPER / 'qa_final'
    run, tex, conf = [paired(base, key) for key in ('RUNTIME', 'TEX_INVENTORY', 'CONFIGURATION')]
    ck(set(run) == {str(Path(n).resolve()) for n in declared_runtime(True)}, 'terminal_runtime_exact_membership', len(run))
    ck(set(tex) == {str(p.resolve()) for root in TEX_ROOTS if root.is_dir() for p in root.rglob('*') if p.is_file()}, 'terminal_tex_exact_membership', len(tex))
    for group in (run, tex):
        for name, value in group.items():
            ck(ledger.get(name) == {k: value[k] for k in ('sha256', 'bytes')}, 'terminal_resource_original_coverage', name)
            pin(name, value)
    configuration(conf)
    candidates = set(CONFIG_ROOTS + TEX_ROOTS + TOOLS)
    candidates.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload', '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2')))
    stdlib, python = Path(sysconfig.get_path('stdlib')).resolve(), Path('/usr/bin/python3.10')
    candidates.update((stdlib.parent / ('python%d%d.zip' % sys.version_info[:2]), python.parent / 'pyvenv.cfg', python.parent.parent / 'pyvenv.cfg', python.with_name(python.name + '._pth'), python.with_name('python._pth')))
    candidates.update(map(Path, ('/etc/locale.conf', '/etc/default/locale', '/etc/nsswitch.conf', '/etc/localtime', '/etc/bash.bashrc', '/etc/profile', '/usr/lib/locale/locale-archive', '/etc/passwd', '/etc/group', '/root/.fonts.conf', '/root/.config/fontconfig/fonts.conf', '/etc/fonts/local.conf', sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
    pth = {'python._pth', 'python3._pth', 'python%d%d._pth' % sys.version_info[:2], 'python%d.%d._pth' % sys.version_info[:2], python.name + '._pth'}
    for directory in {python.parent, Path(sys.executable).parent, stdlib.parent}:
        candidates.update(directory / n for n in pth)
    for name in ('LDLIBRARY', 'INSTSONAME'):
        value = sysconfig.get_config_var(name)
        if value:
            candidates.add(stdlib.parent / (value + '._pth'))
    ldd = raw('/usr/bin/ldd').decode()
    match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    ck(ldd.splitlines()[0] == '#!/bin/bash' and match is not None, 'ldd_declared_loader_source', '/usr/bin/ldd')
    candidates.update(map(Path, match.group(1).split()))
    candidates.update(p for root in CONFIG_ROOTS if root.is_dir() for p in root.rglob('*') if p.is_file())
    ck(set(conf) == set(map(str, candidates)), 'terminal_config_exact_membership', len(conf))
    return {'runtime': len(run), 'tex': len(tex), 'configuration': len(conf)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expected-manifest-sha256', required=True)
    parser.add_argument('--expected-payloads', required=True, type=int)
    parser.add_argument('--attempt', required=True, choices=['lifecycle_01'])
    args = parser.parse_args()
    ck(re.fullmatch('[0-9a-f]{64}', args.expected_manifest_sha256) and args.expected_payloads > 46, 'explicit_actual_final_seal_arguments', vars(args))
    ck(dict(os.environ) == ENV and Path.cwd() == ROOT and Path(sys.executable).resolve() == Path('/usr/bin/python3.10') and sys.flags.isolated and sys.flags.no_site and sys.flags.optimize == 0 and sys.dont_write_bytecode, 'root_inspector_isolated_invocation', sys.executable)
    began = datetime.now(timezone.utc).isoformat()
    fixed = obj(BATCH / 'qa/p209_lifecycle_root_preparation/INPUT_PINS.json')
    for path, value in fixed['inputs'].items():
        pin(path, value)
    pin(SOURCE, HELPER_SHA)
    final_rows = manifest(OUT, count=args.expected_payloads, wanted=args.expected_manifest_sha256)
    gate = obj(GATE)
    ck(gate['schema'] == 'p209-terminal-artifact-root-original-closure-v1' and gate['paper'] == 'P209' and gate['status'] == 'PASS_ROOT_P209_TERMINAL_ARTIFACT_COMPLETE_ORIGINAL_CLOSURE' and gate['actual_exit_code'] == 0 and gate['current_open_findings'] == 0 and gate['lifecycle_acceptance'] is False, 'original_actual_root_gate', str(GATE))
    pin(gate['root_full_execution']['path'], gate['root_full_execution'])
    root_execution = obj(gate['root_full_execution']['path'])
    ck(root_execution['reviewer'] == '/root' and root_execution['completion']['exit_code'] == 0 and json.loads(root_execution['completion']['output']) == gate['complete_original_inspection'], 'original_root_full_native_result', str(GATE))
    pin(BATCH / 'qa/inspect_p209_terminal_initial_success.py', gate['root_inspector_sha256'])
    ck(gate['audit_package_manifest_sha256'] == INITIAL_SHA and gate['audit_package_payloads'] == 46, 'original_root_initial_seal', INITIAL_SHA)
    pin(OUT / 'initial_05/audit.stdout', gate['audit_stdout'])
    initial_command, original = native(OUT / 'initial_05', PREP / 'audit_p209.py', 'terminal-artifact-after-actual-views')
    ck(original['schema'] == 'p209-terminal-artifact-audit-v1' and original['status'] == 'PASS_P209_TERMINAL_ARTIFACT_GATE' and original['paper'] == 'P209' and original['auditor_sha256'] == gate['auditor_sha256'], 'original_initial_actual_result', 'initial_05')
    pin(PREP / 'audit_p209.py', gate['auditor_sha256'])
    ledger = original['all_consumed_inputs_rechecked']
    ck(original['checks'] == gate['auditor_checks'] == sum(original['checks_by_section'].values()) == 4608965 and len(ledger) == original['all_consumed_input_count'] == gate['all_consumed_input_count'] == 132356, 'original_initial_counts_and_sum', 'initial_05')
    prepared = obj(WORK / 'PRESERVATION.json')
    ck(set(manifest(WORK, count=7)) == {'INITIAL_PACKAGE_SHA256SUMS', 'INITIAL_REPORT.md', 'ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256', 'ROOT_GATE.actual.json', 'ROOT_GATE.md', 'PRESERVATION.json'}, 'exact_seven_preupdate_payloads', str(WORK))
    expected_copies = {str(origin): str(WORK / name) for name, origin in [('INITIAL_PACKAGE_SHA256SUMS', OUT / 'SHA256SUMS'), ('INITIAL_REPORT.md', OUT / 'REPORT.md'), ('ROOT_LIFECYCLE.md', PAPER / 'ROOT_LIFECYCLE.md'), ('PAPER_MANIFEST.sha256', PAPER / 'PAPER_MANIFEST.sha256'), ('ROOT_GATE.actual.json', GATE), ('ROOT_GATE.md', GATE_MD)]}
    ck({k: v['copy'] for k, v in prepared['copies'].items()} == expected_copies and prepared['exact_two_paper_alias_paths'] == list(ALIASES), 'exact_preupdate_copy_roles', expected_copies)
    ck(prepared['status'] == 'PASS_EXACT_PREUPDATE_PRESERVATION_NOT_LIFECYCLE_ACCEPTANCE' and prepared['initial_package_payloads'] == 46 and prepared['initial_package_sha256'] == INITIAL_SHA and prepared['initial_audit_stdout'] == gate['audit_stdout'], 'exact_preupdate_record', str(WORK))
    pin(SOURCE, prepared['source']); pin(GATE, prepared['root_gate'])
    for origin, row in prepared['copies'].items():
        pin(row['copy'], row)
        if origin in ALIASES:
            pin(row['copy'], ledger[origin])
        elif origin != str(OUT / 'SHA256SUMS'):
            compare(Path(origin), Path(row['copy']))
    pin(WORK / 'INITIAL_PACKAGE_SHA256SUMS', INITIAL_SHA)
    old_rows = rows(WORK / 'INITIAL_PACKAGE_SHA256SUMS')
    ck(len(old_rows) == 46 and all(final_rows.get(n) == d for n, d in old_rows.items()), 'all_initial_payloads_retained_in_final', 46)
    measure = gate['complete_initial_seal_measurement']
    ck(measure['exit_code'] == 0 and json.loads(measure['output']) == {'manifest': raw(WORK / 'INITIAL_PACKAGE_SHA256SUMS').decode(), 'manifest_sha256': INITIAL_SHA, 'payloads': 46}, 'original_full_native_seal_measurement', INITIAL_SHA)
    checksum = gate['complete_initial_checksum_check']
    ck(checksum['exit_code'] == 0 and checksum['output'] == ''.join(n + ': OK\n' for n in old_rows), 'original_full_native_checksum_output', 46)
    command, lifecycle = native(OUT / args.attempt, SOURCE, 'child', True)
    compare(SOURCE, OUT / args.attempt / 'executed_source_snapshot.py')
    ck(lifecycle['schema'] == 'p209-lifecycle-only-followup-v1' and lifecycle['paper'] == 'P209' and lifecycle['status'] == 'PASS_P209_LIFECYCLE_ONLY_FOLLOWUP' and lifecycle['checks'] == sum(lifecycle['checks_by_section'].values()), 'actual_lifecycle_result_and_sum', args.attempt)
    ck(datetime.fromisoformat(command['started_utc']) <= datetime.fromisoformat(lifecycle['started_utc']) < datetime.fromisoformat(lifecycle['ended_utc']) <= datetime.fromisoformat(command['ended_utc']), 'actual_lifecycle_native_interval', args.attempt)
    ck(lifecycle['initial_package_payloads_preserved'] == 46 and lifecycle['initial_package_sha256'] == INITIAL_SHA and lifecycle['initial_audit_stdout'] == gate['audit_stdout'] and lifecycle['initial_root_gate'] == info(GATE), 'lifecycle_exact_initial_preservation', 46)
    ck(lifecycle['exact_two_old_paper_aliases'] == {k: str(v) for k, v in ALIASES.items()} and lifecycle['original_ledger_paths_checked_twice'] == len(ledger), 'lifecycle_exact_two_aliases', list(ALIASES))
    current = lifecycle['all_current_read_inputs_rechecked']
    ck(lifecycle['all_current_read_input_count'] == len(current), 'lifecycle_full_current_ledger_count', len(current))
    for phase in range(2):
        full_ledger(ledger, True)
        full_ledger(current)
        for name, destination in original['host_path_resolutions_rechecked'].items():
            ck(str(Path(name).resolve(strict=True)) == destination, 'all_original_host_resolutions_pass_' + str(phase), name)
        if phase == 0:
            continue
    # Complete manifest reopening is independent of previous PASS labels.
    records = original['complete_manifests_validated']
    ck(len(records) == 50, 'all_original_recorded_manifests_count', 50)
    for record in records:
        base = absolute(record['base'])
        if base == PAPER and record['name'] == 'PAPER_MANIFEST.sha256':
            pin(WORK / 'PAPER_MANIFEST.sha256', record['sha256'])
            previous = rows(WORK / 'PAPER_MANIFEST.sha256')
            ck(len(previous) == record['entries'] == 8231 and record['complete_nonself'] is True, 'old_whole_paper_exact_manifest', 8231)
            for name, digest in previous.items():
                pin(WORK / name if name == 'ROOT_LIFECYCLE.md' else PAPER / name, digest)
        else:
            manifest(base, record['name'], record['entries'], record['complete_nonself'], record['sha256'])
    paper = manifest(PAPER, 'PAPER_MANIFEST.sha256', 8231)
    previous = rows(WORK / 'PAPER_MANIFEST.sha256')
    changed = [name for name in previous if previous[name] != paper.get(name)]
    ck(set(previous) == set(paper) and changed == ['ROOT_LIFECYCLE.md'], 'only_lifecycle_payload_changed', changed)
    needle = (previous['ROOT_LIFECYCLE.md'] + '  ROOT_LIFECYCLE.md\n').encode()
    replacement = (paper['ROOT_LIFECYCLE.md'] + '  ROOT_LIFECYCLE.md\n').encode()
    old_seal = raw(WORK / 'PAPER_MANIFEST.sha256')
    ck(old_seal.count(needle) == 1 and raw(PAPER / 'PAPER_MANIFEST.sha256') == old_seal.replace(needle, replacement), 'whole_manifest_literal_one_line_change', 'ROOT_LIFECYCLE.md')
    old_text, new_text = raw(WORK / 'ROOT_LIFECYCLE.md').decode(), raw(PAPER / 'ROOT_LIFECYCLE.md').decode()
    ck('ARTIFACT_GATE_PENDING' in old_text and 'P209_INTERNALLY_COMPLETE' not in old_text and 'HOLD_EXTERNAL' in old_text and 'ARTIFACT_GATE_PENDING' not in new_text and 'P209_INTERNALLY_COMPLETE' in new_text and 'HOLD_EXTERNAL' in new_text, 'actual_distinct_lifecycle_states', 'P209 only')
    pin(PAPER / 'ROOT_LIFECYCLE.md', '4ce497df7f03474bc511770df67f35e915b73c2b040a7770fc7ceac2e8dacbae')
    pin(PAPER / 'PAPER_STATUS.md', '304c24e871a27bd02bcd6db231abc37870fb263a01d4c081289bdd53e8718a73')
    pin(PAPER / 'ROOT_ADOPTION.md', '8f82ae0af7156131f14e9e6e849198f8b1c98564760c30d4bc121b50cf34f82e')
    change = {'whole_payloads': 8231, 'changed_payloads': changed, 'old_lifecycle_sha256': previous['ROOT_LIFECYCLE.md'], 'new_lifecycle_sha256': paper['ROOT_LIFECYCLE.md'], 'old_whole_manifest_sha256': sha256(old_seal).hexdigest(), 'new_whole_manifest_sha256': info(PAPER / 'PAPER_MANIFEST.sha256')['sha256']}
    ck(lifecycle['paper_change'] == change, 'lifecycle_exact_paper_change_result', change)
    resource_counts = resources(ledger)
    ck(resource_counts == lifecycle['current_resource_key'] == {'runtime': 2254, 'tex': 113710, 'configuration': 1822}, 'lifecycle_resource_counts', resource_counts)
    new_links = link_closure(original)
    ck(lifecycle['new_links_checked'] == new_links and lifecycle['original_links_rechecked'] == 1534, 'lifecycle_all_original_and_new_links', len(new_links))
    samples = {phase: runtime(lifecycle['actual_runtime_' + phase], ledger, OUT / args.attempt / 'unused_pycache') for phase in ('before', 'after')}
    for record, fields in ((prepared, ('new_scientific_executions', 'new_builds', 'new_views')), (lifecycle, ('new_scientific_executions', 'new_builds', 'new_page_views'))):
        ck(all(record[k] == 0 for k in fields), 'documentary_zero_new_science_build_view', fields)
    ck(lifecycle['owner'] == 'OWNER_AMBER' and lifecycle['external_status'] == 'HOLD_EXTERNAL', 'lifecycle_boundary', 'P209 only')
    receipt = obj(OUT / 'LIFECYCLE_SEAL_RECEIPT.json')
    ck(receipt['status'] == 'PASS_COMPLETE_P209_INITIAL_AND_LIFECYCLE_PACKAGE_SEAL' and receipt['initial_payloads_preserved'] == 46 and receipt['initial_package_sha256'] == INITIAL_SHA and receipt['initial_package_archived'] == str(WORK / 'INITIAL_PACKAGE_SHA256SUMS'), 'final_seal_receipt_initial_scope', args.attempt)
    for field, path in [('followup_command', OUT / args.attempt / 'COMMAND.json'), ('followup_stdout', OUT / args.attempt / 'audit.stdout'), ('followup_source', SOURCE), ('followup_report', OUT / 'LIFECYCLE_REPORT.md')]:
        pin(path, receipt[field])
    report = raw(OUT / 'LIFECYCLE_REPORT.md').decode()
    ck('HOLD_EXTERNAL' in report and 'P209' in report and args.attempt in report and info(OUT / args.attempt / 'audit.stdout')['sha256'] in report, 'final_report_actual_evidence_and_boundary', 'LIFECYCLE_REPORT.md')
    ck(final_rows.get('LIFECYCLE_REPORT.md') == receipt['followup_report']['sha256'] and final_rows.get('LIFECYCLE_SEAL_RECEIPT.json') == info(OUT / 'LIFECYCLE_SEAL_RECEIPT.json')['sha256'], 'final_outer_exact_receipt_and_report_pins', args.expected_manifest_sha256)
    ck(manifest(OUT, count=args.expected_payloads, wanted=args.expected_manifest_sha256) == final_rows, 'final_outer_seal_stable_after', args.expected_manifest_sha256)
    # Reopen every physical input observed by this root checker, including both
    # ledgers, all originals, manifests, sources and current new output records.
    consumed = dict(READS)
    for name, value in consumed.items():
        pin(name, value)
    print(json.dumps({'status': 'PASS_ROOT_P209_FINAL_LIFECYCLE_ORIGINAL_INSPECTION', 'paper': 'P209', 'started_utc': began,
        'ended_utc': datetime.now(timezone.utc).isoformat(), 'checks': sum(CHECKS.values()), 'checks_by_section': dict(CHECKS),
        'final_manifest_sha256': args.expected_manifest_sha256, 'final_payloads': args.expected_payloads,
        'initial_payloads_preserved': 46, 'initial_package_sha256': INITIAL_SHA, 'lifecycle_attempt': args.attempt,
        'lifecycle_native_exit': command['exit_code'], 'lifecycle_checks': lifecycle['checks'], 'lifecycle_source': info(SOURCE),
        'original_ledger_paths_checked_twice': len(ledger), 'current_ledger_paths_checked_twice': len(current),
        'original_host_resolutions_checked_twice': len(original['host_path_resolutions_rechecked']), 'original_manifests_rechecked': 50,
        'exact_two_old_paper_aliases': {k: str(v) for k, v in ALIASES.items()}, 'paper_change': change,
        'resources': resource_counts, 'original_links': 1534, 'new_links': new_links, 'lifecycle_runtime_samples': samples,
        'all_root_read_paths_rechecked': len(consumed), 'root_read_map_sha256': sha256(json.dumps(consumed, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        'fresh_native_comparisons': CMPS, 'new_scientific_build_or_view_executions': 0, 'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL',
        'limits': ['Original documentary closure, not a third mathematical review.', 'Known inventories and sampled runtime, not OS-hermetic or continuous tracing.', 'P209 only; no five-paper or external clearance.']}, sort_keys=True, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(json.dumps({'status': 'FAIL_ROOT_P209_FINAL_LIFECYCLE_ORIGINAL_INSPECTION', 'failure': repr(exc), 'checks_by_section': dict(CHECKS), 'fresh_native_comparisons': CMPS}, sort_keys=True, indent=2))
        raise
