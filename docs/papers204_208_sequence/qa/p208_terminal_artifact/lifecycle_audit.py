#!/usr/bin/env python3
"""P208 lifecycle-only follow-up; original terminal auditor is never executed.

The two original paper-path/hash aliases are exact and fixed. Initial report,
all attempted executions, accepted reviews, scientific inputs and builds stay
unchanged. Only this package's own evolving outer seal is replaced at closure,
after its exact initial bytes have been preserved.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/208-original-snapshot-triangulation-sweeps'
WORK = BASE / 'lifecycle_01'
SOURCE = Path(__file__).resolve()
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
INITIAL_SEAL = 'e3b64033ca95f890e87f1ca7fa669077212fd924277febfa9bc97d71cd74c1b1'
INITIAL_STDOUT = '394f79aa4a5f100430014a1fcc290b2e30523708ec5a2db396d1b6a176cfd72c'
INITIAL_AUDITOR = '086170c8a4784ed3dc560a7fc19ff0de0fbfd22f6afc0ea7ec18fd0fa53c36d8'
OLD_STATUS = '1baa2adda556eba4acc1edeb9b9d4bf3974214b507333db93c33f9a18be58f05'
OLD_PAPER_SEAL = '926afeafef8eb2e2d5d642fb1b5f9b48d81fa7d7f1dc9bdabd42e155031a93dc'
NEW_STATUS = '31b404fa539c5b67c02395d30f5a4aa677bd82f77d8d7df76a85d82ac0d07e01'
NEW_PAPER_SEAL = '0cb42abfb9e639920a973d412ffc7ab2e418df4c26819c6a0d4719007a273e46'
ALIASES = {
    str(PAPER / 'PAPER_STATUS.md'): (OLD_STATUS, BASE / 'lifecycle_before/PAPER_STATUS.md'),
    str(PAPER / 'SHA256SUMS'): (OLD_PAPER_SEAL, BASE / 'lifecycle_before/PAPER_SHA256SUMS'),
}
NEW_DOCUMENTS = (PAPER / 'PAPER_STATUS.md', PAPER / 'SHA256SUMS',
    BATCH / 'P208_FINAL_QA.md', BATCH / 'qa/P208_TERMINAL_ROOT_INSPECTION.md',
    BATCH / 'qa/P208_TERMINAL_ROOT_INSPECTION.actual.json')
TEX_ROOTS = tuple(map(Path, ('/usr/share/texlive/texmf-dist/tex', '/usr/share/texlive/texmf-dist/fonts',
    '/usr/share/texlive/texmf-dist/web2c', '/usr/share/texlive/texmf-dist/bibtex', '/usr/share/texmf',
    '/var/lib/texmf', '/etc/texmf', '/usr/local/share/texmf', '/root/texmf',
    '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')))
CONFIG_ROOTS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/share/fonts', '/etc/fonts',
    '/var/cache/fontconfig', '/usr/share/fontconfig', '/usr/lib/locale/C.utf8',
    '/usr/lib/x86_64-linux-gnu/gconv', '/usr/share/poppler')))
CHECKS, READS, RESOLUTIONS = Counter(), {}, {}


def ck(ok, kind, detail):
    CHECKS[kind] += 1
    if not ok:
        raise AssertionError((kind, detail))


def read(path):
    path = Path(path)
    ck(path.is_file(), 'regular_file', str(path))
    if path.is_relative_to(ROOT):
        ck(not path.is_symlink(), 'workspace_not_symlink', str(path))
    else:
        resolved = str(path.resolve(strict=True))
        ck(str(path) not in RESOLUTIONS or RESOLUTIONS[str(path)] == resolved,
           'host_resolution_stability', str(path))
        RESOLUTIONS[str(path)] = resolved
    raw = path.read_bytes()
    value = {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
    ck(str(path) not in READS or READS[str(path)] == value, 'read_stability', str(path))
    READS[str(path)] = value
    return raw


def info(path):
    raw = read(path)
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def j(path):
    return json.loads(read(path))


def pin(path, wanted):
    got = info(path)
    if isinstance(wanted, str):
        ck(got['sha256'] == wanted, 'exact_hash', str(path))
    else:
        ck(got['sha256'] == wanted['sha256'], 'exact_hash', str(path))
        if 'bytes' in wanted:
            ck(got['bytes'] == wanted['bytes'], 'exact_recorded_size', str(path))


def save(path, raw):
    with Path(path).open('xb') as stream:
        stream.write(raw)


def dump(path, value):
    save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def rows(path):
    result = {}
    for line in read(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(match is not None, 'manifest_syntax', str(path))
        digest, name = match.groups(); rel = Path(name)
        ck(rel.parts and not rel.is_absolute() and '..' not in rel.parts and name not in result,
           'manifest_safe_unique', (str(path), name))
        result[name] = digest
    return result


def physical(base):
    result = set()
    for path in base.rglob('*'):
        ck(not path.is_symlink(), 'owned_no_symlink', str(path))
        if path.is_file(): result.add(path.relative_to(base).as_posix())
    return result


def manifest(base, name='SHA256SUMS', complete=True, count=None):
    declared = rows(base / name)
    ck(name not in declared, 'manifest_nonself', str(base))
    if count is not None: ck(len(declared) == count, 'manifest_count', (str(base), count))
    if complete: ck(set(declared) == physical(base) - {name}, 'manifest_complete', str(base))
    for rel, digest in declared.items(): pin(base / rel, digest)
    return declared


def initial_payloads():
    pin(WORK / 'INITIAL_PACKAGE_SHA256SUMS', INITIAL_SEAL)
    declared = rows(WORK / 'INITIAL_PACKAGE_SHA256SUMS')
    ck(len(declared) == 54 and 'SHA256SUMS' not in declared, 'initial_package_count', '54 nonself payloads')
    for name, digest in declared.items(): pin(BASE / name, digest)
    ck(read(WORK / 'INITIAL_REPORT.md') == read(BASE / 'REPORT.md'), 'initial_report_unchanged', 'exact archived bytes')
    pin(BASE / 'initial_05/audit.stdout', INITIAL_STDOUT)
    pin(BASE.parent / 'audit_p208.py', INITIAL_AUDITOR)
    result = j(BASE / 'initial_05/audit.stdout')
    ck(result['status'] == 'PASS_P208_TERMINAL_ARTIFACT_GATE' and result['checks'] == 2232943
       and result['all_consumed_input_count'] == 115334, 'original_actual_initial_pass', 'exact record')
    return result


def paper_change():
    pin(PAPER / 'PAPER_STATUS.md', NEW_STATUS); pin(PAPER / 'SHA256SUMS', NEW_PAPER_SEAL)
    pin(BASE / 'lifecycle_before/PAPER_STATUS.md', OLD_STATUS)
    pin(BASE / 'lifecycle_before/PAPER_SHA256SUMS', OLD_PAPER_SEAL)
    old = rows(BASE / 'lifecycle_before/PAPER_SHA256SUMS')
    current = manifest(PAPER, count=2178)
    ck(set(old) == set(current) and len(old) == 2178, 'unchanged_full_paper_directory_set', '2178 original paths')
    changed = [name for name in old if old[name] != current[name]]
    ck(changed == ['PAPER_STATUS.md'] and old['PAPER_STATUS.md'] == OLD_STATUS
       and current['PAPER_STATUS.md'] == NEW_STATUS, 'exact_one_payload_change', changed)
    old_raw = read(BASE / 'lifecycle_before/PAPER_SHA256SUMS')
    expected = old_raw.replace((OLD_STATUS + '  PAPER_STATUS.md\n').encode(),
                               (NEW_STATUS + '  PAPER_STATUS.md\n').encode())
    ck(expected != old_raw and read(PAPER / 'SHA256SUMS') == expected,
       'literal_single_manifest_line_change', 'same order/names/all other bytes')
    return {'payload_count': 2178, 'changed_payloads': changed,
            'old_status_sha256': OLD_STATUS, 'new_status_sha256': NEW_STATUS,
            'old_manifest_sha256': OLD_PAPER_SEAL, 'new_manifest_sha256': NEW_PAPER_SEAL}


def prepare():
    # Exactly one new implementation file can precede initial preservation.
    pin(BASE / 'SHA256SUMS', INITIAL_SEAL)
    initial = rows(BASE / 'SHA256SUMS')
    ck(len(initial) == 54, 'initial_preservation_count', 'initial complete set')
    ck(physical(BASE) == set(initial) | {'SHA256SUMS', SOURCE.name},
       'initial_preservation_exact_scope', 'only this new scoped helper precedes snapshots')
    for name, value in initial.items(): pin(BASE / name, value)
    WORK.mkdir(exist_ok=False)
    save(WORK / 'INITIAL_PACKAGE_SHA256SUMS', read(BASE / 'SHA256SUMS'))
    save(WORK / 'INITIAL_REPORT.md', read(BASE / 'REPORT.md'))
    save(WORK / 'prepared_source_snapshot.py', read(SOURCE))
    before = {}
    for path in NEW_DOCUMENTS:
        value = info(path)
        target = WORK / 'root_context' / path.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        save(target, read(path)); pin(target, value)
        before[str(path)] = {'snapshot': str(target.relative_to(BASE)), **value}
    original = initial_payloads()
    change = paper_change()
    root = j(BATCH / 'qa/P208_TERMINAL_ROOT_INSPECTION.actual.json')
    ck(root['actual_exit_code'] == 0 and root['result']['status'] ==
       'ROOT_P208_INITIAL_TERMINAL_ARTIFACT_ORIGINAL_INSPECTION_PASS', 'actual_root_acceptance', 'original receipt')
    ck(root['result']['initial_package_seal']['sha256'] == INITIAL_SEAL and
       root['result']['actual_stdout']['sha256'] == INITIAL_STDOUT, 'root_acceptance_exact_initial', 'same package/result')
    ledger = original['all_consumed_inputs_rechecked']
    for path, (old_hash, target) in ALIASES.items():
        ck(ledger[path]['sha256'] == old_hash, 'fixed_alias_old_key', path)
        pin(target, ledger[path])
    dump(WORK / 'ROOT_DOCUMENTS_BEFORE.json', before)
    receipt = {'status': 'PASS_LIFECYCLE_PREPARATION_NOT_FINAL_AUDIT',
               'utc': datetime.now(timezone.utc).isoformat(), 'initial_payloads_preserved': 54,
               'initial_seal_sha256': INITIAL_SEAL, 'initial_report': info(BASE / 'REPORT.md'),
               'source': info(SOURCE), 'paper_change': change, 'new_document_count': len(before),
               'exact_aliases': {p: {'old_sha256': v[0], 'preserved_path': str(v[1])} for p, v in ALIASES.items()}}
    dump(WORK / 'PREPARATION.json', receipt)
    print(json.dumps(receipt, sort_keys=True, indent=2))


def validate_config(record):
    for name, value in record.items():
        path = Path(name)
        ck(path.exists() == value['exists'], 'config_existence', name)
        if 'resolved' in value: ck(str(path.resolve()) == value['resolved'], 'config_resolution', name)
        if 'is_file' in value: ck(path.is_file() == value['is_file'], 'config_kind', name)
        if value.get('sha256') is not None: pin(path, value)
        elif 'sha256' in value: ck(not path.is_file(), 'config_null_hash_absence', name)


def runtime_and_resource_key(original):
    for role in ('author', 'a', 'b'):
        base = BATCH / ('qa/root_replays/p208_' + role + '_strict')
        conf = j(base / 'CONFIGURATION_BEFORE.json')
        ck(conf == j(base / 'CONFIGURATION_AFTER.json'), 'strict_recorded_config_pair', role)
        validate_config(conf)
    final = PAPER / 'qa_final'
    conf = j(final / 'CONFIGURATION_BEFORE.json')
    ck(conf == j(final / 'CONFIGURATION_AFTER.json'), 'terminal_recorded_config_pair', 'exact')
    validate_config(conf)
    for group in j(BATCH / 'reviews/p208_b/delta/CONFIGURATION_BEFORE.json').values(): validate_config(group)
    tex = j(final / 'TEX_INVENTORY_BEFORE.json')
    ck(tex == j(final / 'TEX_INVENTORY_AFTER.json'), 'terminal_recorded_tex_pair', 'exact')
    current_tex = {str(p.resolve()) for root in TEX_ROOTS if root.is_dir() for p in root.rglob('*') if p.is_file()}
    ck(current_tex == set(tex), 'complete_current_tex_names', 'no newly added/removed resource path')
    stdlib = Path('/root/miniconda3/lib/python3.12'); python = Path('/root/miniconda3/bin/python3.12')
    toolpaths = [Path('/usr/bin') / n for n in ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo',
        'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp')] + [Path('/bin/bash'), python]
    current_runtime = {str(p.resolve()) for p in stdlib.rglob('*') if p.is_file()
                       and 'site-packages' not in p.parts and '__pycache__' not in p.parts} | {str(p.resolve()) for p in toolpaths}
    runtime = j(final / 'RUNTIME_BEFORE.json')
    ck(runtime == j(final / 'RUNTIME_AFTER.json') and current_runtime == set(runtime),
       'complete_current_runtime_names', 'full non-site/non-bytecode stdlib and exact tools')
    candidates = set(CONFIG_ROOTS + TEX_ROOTS) | set(toolpaths)
    candidates.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
        '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2',
        '/root/miniconda3/lib/python312.zip', '/etc/locale.conf', '/etc/default/locale')))
    candidates.update([python.parent / 'pyvenv.cfg', python.parent.parent / 'pyvenv.cfg',
                       python.with_name(python.name + '._pth'), python.with_name('python._pth')])
    candidates.update(p for root in CONFIG_ROOTS if root.is_dir() for p in root.rglob('*') if p.is_file())
    ck(set(map(str, candidates)) == set(conf), 'complete_current_config_names', 'full declared roots/candidates')
    ledger = original['all_consumed_inputs_rechecked']
    for group in (tex, runtime):
        for name, value in group.items():
            ck(ledger.get(name) == value, 'current_named_resource_in_original_ledger', name)
    return {'runtime_files': len(runtime), 'tex_files': len(tex), 'configuration_records': len(conf)}


def own_runtime(coverage):
    modules, mapped = {}, {}
    for name, module in sorted(sys.modules.items()):
        origin = getattr(module, '__file__', None)
        if origin and Path(origin).is_file():
            path = Path(origin).resolve()
            ck(path.suffix != '.pyc', 'own_no_bytecode_source', name)
            value = info(path)
            ck(coverage.get(str(path)) == value, 'own_runtime_covered', str(path))
            modules[name] = {'path': str(path), **value}
    for line in Path('/proc/self/maps').read_text().splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            path = Path(fields[5]).resolve(); value = info(path)
            ck(coverage.get(str(path)) == value, 'own_maps_covered', str(path))
            mapped[str(path)] = value
    return {'modules': modules, 'mapped_files': mapped, 'flags': repr(sys.flags),
            'environment': dict(os.environ), 'sys_path': sys.path,
            'pycache_prefix': sys.pycache_prefix, 'maps_scope': 'This lifecycle-auditor process only; samples, not a syscall trace.'}


def new_links():
    all_links = []
    for path in (PAPER / 'PAPER_STATUS.md', BATCH / 'P208_FINAL_QA.md', BATCH / 'qa/P208_TERMINAL_ROOT_INSPECTION.md'):
        content = read(path).decode()
        ck('HOLD_EXTERNAL' in content, 'new_document_external_hold', str(path))
        if path.name != 'P208_TERMINAL_ROOT_INSPECTION.md':
            ck('P208_INTERNALLY_COMPLETE' in content, 'new_document_internal_complete', str(path))
        # These three inspected lifecycle documents have no code fences or
        # indented code blocks. Code spans cannot create artificial links.
        content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            target = target.strip('<>').split('#', 1)[0]
            if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target): continue
            destination = (path.parent / target).resolve()
            ck(destination.exists(), 'new_document_link', (str(path), target))
            all_links.append({'document': str(path), 'target': target, 'resolved': str(destination)})
    return all_links


def audit():
    ck(sys.flags.optimize == 0 and sys.flags.isolated == sys.flags.no_site == 1 and sys.dont_write_bytecode
       and sys.pycache_prefix and not Path(sys.pycache_prefix).exists() and dict(os.environ) == ENV,
       'actual_child_controls', '-I -S -B exact environment, optimization zero, absent cache')
    started = datetime.now(timezone.utc).isoformat()
    prepared = j(WORK / 'PREPARATION.json')
    revision = j(WORK / 'SOURCE_REVISION.json')
    ck(revision['originally_prepared_source'] == prepared['source'] and
       revision['kind'] == 'PRE_CHILD_EXECUTION_CONFIGURATION_SCHEMA_REPAIR',
       'explicit_preexecution_source_revision', 'original preparation remains unchanged')
    pin(WORK / 'prepared_source_snapshot.py', prepared['source'])
    pin(SOURCE, revision['revised_source'])
    original = initial_payloads()
    ledger = original['all_consumed_inputs_rechecked']
    ck(len(ledger) == 115334 and set(ALIASES) <= set(ledger), 'entire_original_ledger', 'exact names/count')
    coverage = dict(ledger); coverage[str(SOURCE)] = revision['revised_source']
    early = own_runtime(coverage)
    for when in ('before', 'after'):
        if when == 'after': break
        for name, value in ledger.items():
            selected = Path(name)
            if name in ALIASES:
                old_hash, selected = ALIASES[name]
                ck(value['sha256'] == old_hash, 'exact_two_old_hash_aliases', name)
            pin(selected, value)
    changes = paper_change()
    for record in original['complete_manifests_validated']:
        base = ROOT / record['base']; name = record['name']
        if base == PAPER and name == 'SHA256SUMS': continue
        pin(base / name, record['sha256'])
        manifest(base, name, record['complete_nonself'], record['entries'])
    key = runtime_and_resource_key(original)
    for path, resolved in original['host_path_resolutions_rechecked'].items():
        ck(str(Path(path).resolve(strict=True)) == resolved, 'all_original_host_resolutions', path)
    for row in original['all_local_links_checked']:
        target = Path(row['resolved_target']); target = target if target.is_absolute() else ROOT / target
        ck(target.exists(), 'all_original_links_still_exist', str(target))
    root_before = j(WORK / 'ROOT_DOCUMENTS_BEFORE.json')
    ck(set(root_before) == set(map(str, NEW_DOCUMENTS)), 'exact_new_document_set', 'five original current files')
    for path, value in root_before.items():
        wanted = {k: value[k] for k in ('sha256', 'bytes')}
        pin(path, wanted); pin(BASE / value['snapshot'], wanted)
    root = j(BATCH / 'qa/P208_TERMINAL_ROOT_INSPECTION.actual.json')
    ck(root['actual_exit_code'] == 0 and root['result']['status'] ==
       'ROOT_P208_INITIAL_TERMINAL_ARTIFACT_ORIGINAL_INSPECTION_PASS'
       and root['result']['initial_package_seal']['sha256'] == INITIAL_SEAL,
       'root_accepted_initial_original', 'actual exact acceptance')
    links = new_links()
    late = own_runtime(coverage)
    for name, value in ledger.items():
        selected = ALIASES[name][1] if name in ALIASES else Path(name)
        pin(selected, value)
    for path, resolved in original['host_path_resolutions_rechecked'].items():
        ck(str(Path(path).resolve(strict=True)) == resolved, 'all_original_host_resolutions_after', path)
    initial_payloads()
    ck(changes == paper_change(), 'new_paper_closure_after', 'exact same lifecycle-only change')
    for path, value in root_before.items(): pin(path, {k: value[k] for k in ('bytes', 'sha256')})
    consumed = dict(READS)
    for path, value in consumed.items():
        raw = Path(path).read_bytes()
        ck({'bytes': len(raw), 'sha256': sha256(raw).hexdigest()} == value,
           'all_current_read_inputs_after', path)
    ck(not Path(sys.pycache_prefix).exists(), 'unused_cache_after', 'absent')
    print(json.dumps({'status': 'PASS_P208_LIFECYCLE_ONLY_FOLLOWUP', 'started_utc': started,
        'ended_utc': datetime.now(timezone.utc).isoformat(), 'checks': sum(CHECKS.values()),
        'checks_by_section': dict(CHECKS), 'original_ledger_paths_checked_twice': len(ledger),
        'original_host_resolutions_checked_twice': len(original['host_path_resolutions_rechecked']),
        'unchanged_original_package_payloads': 54, 'initial_audit_stdout_sha256': INITIAL_STDOUT,
        'exact_aliases': prepared['exact_aliases'], 'paper_change': changes,
        'current_resource_key': key, 'original_links_rechecked': len(original['all_local_links_checked']),
        'new_links_checked': links, 'new_document_pins': root_before,
        'runtime_before': early, 'runtime_after': late,
        'all_current_read_input_count': len(consumed), 'all_current_read_inputs_rechecked': consumed,
        'new_scientific_executions': 0, 'new_builds': 0, 'new_page_views': 0,
        'role': 'Lifecycle-only artifact follow-up after actual root acceptance; not a new scientific gate, review or delta.',
        'limits': ['The exact two aliases preserve historical paper lifecycle bytes; no other original ledger change is permitted.',
                   'Accepted all-size claims and original actual science/build/view evidence are reused unchanged.',
                   'Runtime/resource recapture and sampled own maps are not continuous tracing or a hermetic historical OS.',
                   'Only P208 is checked; five-paper completion, Git synchronization and external clearance are not asserted.'],
        'external': 'OWNER_AMBER / HOLD_EXTERNAL'}, sort_keys=True, indent=2))


def run(label):
    ck(label.replace('_', '').isalnum(), 'safe_attempt_label', label)
    target = WORK / label; target.mkdir(exist_ok=False)
    save(target / 'executed_source_snapshot.py', read(SOURCE))
    source_before = info(SOURCE)
    argv = [str(Path(sys.executable).resolve()), '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(target / 'unused_pycache'), str(SOURCE), 'child']
    started = datetime.now(timezone.utc).isoformat()
    attempt = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_utc': started, 'status': 'ATTEMPTED'}
    dump(target / 'ATTEMPT.json', attempt)
    child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
    save(target / 'audit.stdout', child.stdout); save(target / 'audit.stderr', child.stderr)
    # Do not reuse read-stability checks as a substitute for recording change.
    source_after_raw = SOURCE.read_bytes()
    source_after = {'bytes': len(source_after_raw), 'sha256': sha256(source_after_raw).hexdigest()}
    command = {k: attempt[k] for k in ('argv', 'cwd', 'environment', 'started_utc')}
    command.update(ended_utc=datetime.now(timezone.utc).isoformat(), exit_code=child.returncode,
                   source_before=source_before, source_after=source_after,
                   source_unchanged=source_before == source_after,
                   unused_cache_absent=not (target / 'unused_pycache').exists(),
                   stdout=info(target / 'audit.stdout'), stderr=info(target / 'audit.stderr'))
    dump(target / 'COMMAND.json', command)
    values = [(info(p)['sha256'], p.relative_to(target).as_posix()) for p in sorted(target.rglob('*')) if p.is_file()]
    save(target / 'SHA256SUMS', ''.join(d + '  ' + n + '\n' for d, n in values).encode())
    manifest(target)
    print(json.dumps(command, sort_keys=True, indent=2))
    if child.returncode:
        print(child.stderr.decode(), file=sys.stderr)
    else:
        result = json.loads(child.stdout)
        print(json.dumps({k: result[k] for k in ('status', 'checks', 'all_current_read_input_count')}, sort_keys=True))
    ck(source_before == source_after and command['unused_cache_absent'], 'recorder_after_controls', label)
    raise SystemExit(child.returncode)


def seal(label):
    # Initial outer seal remains available at its historical copy. This final
    # operation updates only the current own-scope outer SHA256SUMS.
    pin(BASE / 'SHA256SUMS', INITIAL_SEAL)
    original = initial_payloads()
    target = WORK / label; manifest(target)
    command, result = j(target / 'COMMAND.json'), j(target / 'audit.stdout')
    ck(command['exit_code'] == 0 and command['source_unchanged'] and command['unused_cache_absent']
       and result['status'] == 'PASS_P208_LIFECYCLE_ONLY_FOLLOWUP', 'final_actual_lifecycle_pass', label)
    for stream in ('stdout', 'stderr'): pin(target / ('audit.' + stream), command[stream])
    pin(SOURCE, command['source_before'])
    for path, value in result['all_current_read_inputs_rechecked'].items(): pin(path, value)
    report = info(BASE / 'LIFECYCLE_REPORT.md')
    receipt = {'status': 'PASS_COMPLETE_P208_INITIAL_AND_LIFECYCLE_PACKAGE_SEAL',
               'utc': datetime.now(timezone.utc).isoformat(), 'initial_package_sha256': INITIAL_SEAL,
               'initial_package_archived': 'lifecycle_01/INITIAL_PACKAGE_SHA256SUMS',
               'initial_report_archived': 'lifecycle_01/INITIAL_REPORT.md',
               'accepted_followup': label, 'followup_command': info(target / 'COMMAND.json'),
               'followup_stdout': info(target / 'audit.stdout'), 'followup_source': info(SOURCE),
               'followup_checks': result['checks'], 'followup_report': report,
               'payload_count': len([p for p in BASE.rglob('*') if p.is_file() and p != BASE / 'SHA256SUMS']) + 1,
               'boundary': 'The sole replaced own-package original is the evolving outer seal; its initial bytes and all 54 initial payloads remain preserved.'}
    dump(WORK / 'FINAL_SEAL_RECEIPT.json', receipt)
    values = [(info(p)['sha256'], p.relative_to(BASE).as_posix()) for p in sorted(BASE.rglob('*'))
              if p.is_file() and p != BASE / 'SHA256SUMS']
    # This generated manifest replacement is the explicitly scoped lifecycle
    # sealing output, not an edit to an initial report, command or source.
    with (BASE / 'SHA256SUMS').open('wb') as stream:
        stream.write(''.join(d + '  ' + n + '\n' for d, n in values).encode())
    # Clear only that deliberately superseded read record, retaining its old
    # bytes in the already pinned INITIAL_PACKAGE_SHA256SUMS.
    READS.pop(str(BASE / 'SHA256SUMS'))
    final = manifest(BASE)
    ck(len(final) == receipt['payload_count'], 'final_complete_payload_count', len(final))
    print(json.dumps({'status': receipt['status'], 'payloads': len(final),
                      'manifest_sha256': info(BASE / 'SHA256SUMS')['sha256'],
                      'followup_stdout_sha256': command['stdout']['sha256']}, sort_keys=True, indent=2))


if __name__ == '__main__':
    ck(sys.flags.optimize == 0 and sys.flags.isolated == sys.flags.no_site == 1 and sys.dont_write_bytecode,
       'invocation_flags', '-I -S -B and optimization zero')
    if len(sys.argv) == 2 and sys.argv[1] == 'prepare': prepare()
    elif len(sys.argv) == 2 and sys.argv[1] == 'child': audit()
    elif len(sys.argv) == 3 and sys.argv[1] == 'run': run(sys.argv[2])
    elif len(sys.argv) == 3 and sys.argv[1] == 'seal': seal(sys.argv[2])
    else: raise RuntimeError('Require prepare, run NEW_LABEL, child or seal PASSED_LABEL')
