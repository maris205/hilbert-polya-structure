#!/usr/bin/env python3
"""Prepared read-only P210 B initial receiver. ROOT MUST EXECUTE, not preparer.

No B writer, scientific program, native command, builder or old receiver is
imported/executed. Only stdout is written. Every B audit-ledger path is fully
hashed before and after; old A's nested 120k ledgers are never expanded.
"""
from collections import Counter
from datetime import datetime, timezone
import gzip
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys
import sysconfig
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_b_initial_reception_preparation'
B = ROOT / 'docs/papers204_208_sequence/reviews/p210_b'
A = ROOT / 'docs/papers204_208_sequence/reviews/p210_a'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
FROZEN = PAPER / 'frozen_round1'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
B_SEAL = '81b5f97a6b25d6f9e82db87001da1a54668c01268038694d4b8a3b61006b02c3'
R1_SEAL = 'be54b79806d90f22037cee877f92074e744b2ef27bcc0b6b2e4f8dfa658446e0'
SEAL_RETURN = QA / 'P210_B_INITIAL_SEAL_NATIVE_RETURN.actual.json'
SEAL_RETURN_KEY = '8f0ae99ae62c571e0b8eb8371ee6e29c75a90059f49d0d2edbbf88132098b019'
PY_PATH = ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload']
CHECKS, SEEN, MANIFESTS, RAW_COMPARISONS, NATIVE, LINKS = Counter(), {}, [], [], [], []
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


def ck(ok, label, detail=''):
    CHECKS[label] += 1
    if not ok:
        raise AssertionError((label, detail))


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


def manifest(path, base, count, complete=False, aliases=None):
    aliases = {} if aliases is None else aliases
    result = {}
    for line in raw(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(match is not None, 'manifest_syntax', str(path))
        digest, name = match.groups()
        relative = Path(name)
        ck(name not in result and not relative.is_absolute() and '..' not in relative.parts and
           relative.as_posix() == name, 'manifest_unique_safe_relative', (str(path), name))
        result[name] = digest
        original = str(base / name)
        pin(aliases.get(original, original), digest)
    ck(count is None or len(result) == count, 'manifest_count', (str(path), len(result), count))
    if complete:
        ck(path.parent == base and path.name not in result and
           set(result) == physical(base) - {path.name}, 'complete_nonself_manifest', str(path))
    MANIFESTS.append({'path': str(path), 'base': str(base), 'entries': len(result),
                      'complete_nonself': complete, 'sha256': pin(path)['sha256'], 'aliases': aliases})
    return result


def compare(left, right, role):
    ck(raw(left) == raw(right), 'complete_python_byte_equality', (str(left), str(right), role))
    RAW_COMPARISONS.append({'left': str(left), 'right': str(right), 'role': role})


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


def map_paths(text):
    result = []
    for line in text.splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            result.append(Path(fields[5]))
    return result


def source_only_flags(flags):
    return all(value in flags for value in ('optimize=0', 'dont_write_bytecode=1', 'no_site=1', 'isolated=1'))


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


def main():
    ck(len(sys.argv) == 3 and sys.argv[1] == 'initial-B-only' and
       re.fullmatch('[0-9a-f]{64}', sys.argv[2]), 'exact_root_invocation')
    ck(Path(__file__).resolve() == PREP / 'receive_p210_b_initial.py' and Path.cwd() == ROOT and
       Path(sys.executable).resolve() == Path('/usr/bin/python3.10'), 'exact_receiver_source_interpreter_cwd')
    ck(dict(os.environ) == ENV and sys.flags.isolated == sys.flags.no_site == 1 and
       sys.flags.optimize == 0 and sys.dont_write_bytecode and sys.path == PY_PATH and
       sys.pycache_prefix == str(PREP / 'never_created_cache') and not os.path.lexists(sys.pycache_prefix),
       'isolated_safe_source_only_receiver_settings')
    started = datetime.now(timezone.utc).isoformat()
    pin(PREP / 'SHA256SUMS', sys.argv[2])
    manifest(PREP / 'SHA256SUMS', PREP, None, True)
    pin(B / 'SHA256SUMS', B_SEAL)
    package = manifest(B / 'SHA256SUMS', B, 407, True)
    ck(not any(Path(n).suffix in {'.pyc', '.pyo'} for n in package), 'no_B_package_bytecode')
    pin(SEAL_RETURN, SEAL_RETURN_KEY)
    external = obj(SEAL_RETURN)
    ck(external['role'] == 'ACTUAL_B_INITIAL_SEAL_EXTERNAL_NATIVE_RETURN' and external['cwd'] == str(ROOT)
       and type(external['result']['exit_code']) is int and external['result']['exit_code'] == 0,
       'actual_external_seal_native_exit')
    exact_seal_command = ('env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC '
        '/usr/bin/python3.10 -I -S -B -X pycache_prefix=' + str(B / 'absent_initial_seal_cache') +
        ' ' + str(B / 'seal_initial.py'))
    ck(external['command'] == exact_seal_command and not os.path.lexists(B / 'absent_initial_seal_cache'),
       'actual_external_seal_command_cache')
    seal_stdout = json.loads(external['result']['output'])
    ck(seal_stdout == {'checks_including_manifest': 1371, 'complete_native_receipts_checked': 63,
       'manifest_sha256': B_SEAL, 'manuscript_open': {'Critical': 0, 'Major': 0, 'Minor': 0},
       'payloads': 407, 'physical_files': 408, 'status': 'SEALED_INITIAL_PENDING_ROOT_RESPONSE'},
       'actual_complete_seal_stdout')
    audit, seal = obj(B / 'AUDIT.actual.json'), obj(B / 'SEAL_AUDIT.actual.json')
    ck(audit['status'] == 'PASS_INITIAL_EVIDENCE_AUDIT' and audit['checks'] == 259277 and
       audit['full_byte_read_paths'] == 120840 and audit['full_python_byte_comparisons'] == 515 and
       audit['native_commands_checked'] == 62 and audit['accepted_delta'] is False and
       audit['current_manuscript_changes'] is False, 'actual_B_initial_audit_schema')
    ck(seal['status'] == 'PASS_INITIAL_SEAL_GATE_NOT_ACCEPTED_DELTA' and seal['checks'] == 963 and
       seal['native_receipts_checked'] == 63 and seal['payload_files_including_this_gate'] == 407 and
       seal['initial_phase'] == 'INITIAL_PENDING_ROOT_RESPONSE', 'actual_B_initial_seal_schema')
    pin(B / 'seal_initial.py', seal['source_sha256'])
    pin(B / seal['prior_full_audit']['path'], seal['prior_full_audit']['sha256'])
    audit_inputs, audit_roles = obj(B / 'AUDIT_INPUTS.actual.json.gz'), obj(B / 'AUDIT_ROLES.actual.json')
    ck(len(audit_inputs) == 120840 and len(audit_roles) == 50 and
       set().union(*map(set, audit_roles.values())) == set(audit_inputs), 'complete_B_audit_role_partition_union')
    ck(all(v == sorted(set(v)) for v in audit_roles.values()), 'unique_sorted_declared_audit_roles')
    for path, expected in audit_inputs.items():
        ck(Path(path).is_absolute() and set(expected) == {'real', 'sha256', 'size', 'symlink'},
           'exact_B_ledger_key_schema', path)
        pin(path, expected, force=True)

    pin(FROZEN / 'SHA256SUMS', R1_SEAL)
    frozen = manifest(FROZEN / 'SHA256SUMS', FROZEN, 508, True)
    review_input = manifest(B / 'INPUT_PINS.sha256', ROOT, 509)
    ck(set(review_input) == {str((FROZEN / n).relative_to(ROOT)) for n in set(frozen) | {'SHA256SUMS'}},
       'B_pins_all_509_physical_Round1_inputs')
    prov = obj(FROZEN / 'ROUND1_PROVENANCE.json')
    ck(prov['round0_external_aliases'] == [] and len(prov['initial_review_aliases']) == 2,
       'only_exact_declared_initial_A_aliases')
    aliases = {}
    for row in prov['initial_review_aliases']:
        ck(row['original_path'] in {str(A / 'DELTA.md'), str(A / 'SHA256SUMS')} and
           Path(row['physical_path']) == A / 'history/initial_before_delta' / Path(row['original_path']).name,
           'exact_initial_A_historical_role_path', row)
        pin(row['physical_path'], row['sha256'])
        aliases[row['original_path']] = row['physical_path']
    ck(len(aliases) == 2, 'two_distinct_initial_A_alias_roles')
    pin(A / 'SHA256SUMS', 'f6b92663cb2a7909f85a25a892ee4433ccd6177e84c07bf7ceccc9555b191f6d')
    manifest(A / 'SHA256SUMS', A, 552, True)
    manifest(A / 'history/initial_before_delta/SHA256SUMS', A, 484, aliases=aliases)
    for label, count in (('round0_external_original_pins', 33), ('accepted_review_and_root_manifest_referents', 611)):
        ck(len(prov[label]) == count, 'exact_inherited_named_referent_count', label)
        for path, digest in prov[label].items():
            pin(path, digest)
    for label, count in (('round1_core_link_map', 57), ('acceptance_anchor_link_map', 14)):
        ck(len(prov[label]) == count, 'exact_frozen_link_map_count', label)
        for row in prov[label]:
            doc = FROZEN / row['document']
            ck(row['href'] in stripped_links(raw(doc).decode()), 'genuine_explicit_frozen_href', row['document'])
            pin(row['physical_target'], row['sha256'])
            if 'document_sha256' in row:
                pin(doc, row['document_sha256'])
            if 'round0_physical_target' in row:
                pin(row['round0_physical_target'], row['sha256'])
    core = manifest(PAPER / 'frozen_round0/SHA256SUMS', PAPER / 'frozen_round0', 493, True)
    ck(core == prov['core_payload_pins'], 'exact_493_Round0_core_roles')
    author = manifest(FROZEN / 'AUTHOR_MANIFEST.sha256', FROZEN, 489)
    for name, digest in author.items():
        pin(PAPER / name, digest)
    historical = {str(PAPER / 'ROOT_LIFECYCLE.md'): FROZEN / 'ROUND1_ACCEPTANCE/PRE_ROUND1_ROOT_LIFECYCLE.md',
                  str(PAPER / 'PAPER_MANIFEST.sha256'): FROZEN / 'ROUND1_ACCEPTANCE/PRE_ROUND1_PAPER_MANIFEST.sha256'}
    ck(len(prov['anchors']) == 13, 'thirteen_physical_Round1_acceptance_roles')
    for row in prov['anchors'].values():
        selected = FROZEN / row['physical_path']
        pin(selected, row['sha256'])
        if row['original_path'] in historical:
            ck(selected == historical[row['original_path']], 'exact_prior_control_anchor_role', row)
        else:
            pin(row['original_path'], row['sha256'])
    old_manifest = prov['prior_whole_manifest']
    ck(old_manifest['original_referent_base'] == str(PAPER) and old_manifest['complete_before_creation_only'] is True
       and old_manifest['current_whole_manifest_after_creation'] is False, 'historical_whole_manifest_scope_not_current')
    old_rows = manifest(historical[str(PAPER / 'PAPER_MANIFEST.sha256')], PAPER, 987,
                        aliases={str(PAPER / 'ROOT_LIFECYCLE.md'): str(historical[str(PAPER / 'ROOT_LIFECYCLE.md')])})
    ck(old_rows == old_manifest['original_referent_pins'], 'exact_all_987_old_whole_roles')

    first = obj(B / 'COMMITMENT.actual.json')
    complete = obj(B / 'COMPLETE_SOURCE_COMMITMENT.actual.json')
    precompare = obj(B / 'PRE_COMPARISON_PROOF_CODE_COMMITMENT.actual.json')
    for name, digest in first['files'].items():
        pin(B / ('history/verify.initial_reconstructed.py' if name == 'verify.py' else name), digest)
    for commitment, field in ((complete, 'files'), (precompare, 'pins')):
        for name, digest in commitment[field].items():
            pin(B / name, digest)
    ck(first['semantic_author_A_code_or_canonical_read'] is False and
       complete['author_A_code_or_canonical_semantics_read'] is False and
       precompare['author_A_verifier_or_canonical_body_semantics_read'] is False,
       'declared_precomparison_independence_scope_not_blindness')
    commitment_times = [datetime.fromisoformat(d['utc']).timestamp() for d in (first, complete, precompare)]
    ck(commitment_times == sorted(commitment_times) and len(set(commitment_times)) == 3,
       'three_recorded_commitment_times_order')
    old_engine, new_engine = raw(B / 'instrumentation/evidence.py'), raw(B / 'instrumentation/evidence_build_v2.py')
    ck(new_engine == old_engine.replace(b'for v in cap.before.values()', b'for v in cap.before["files"].values()'),
       'exact_one_line_failed_build_adapter_correction')
    old_audit, new_audit = raw(B / 'history/audit_package.attempt01.py'), raw(B / 'audit_package.py')
    corrected_audit = old_audit.replace(b"str(PAPER / 'SHA256SUMS')", b"str(PAPER / 'PAPER_MANIFEST.sha256')")
    corrected_audit = corrected_audit.replace(b"directory.name == 'build01'", b"directory.name in {'build01', 'audit01'}")
    ck(new_audit == corrected_audit, 'exact_two_line_old_control_and_retained_audit_failure_correction')
    comparison_rows = obj(B / 'AUDIT_COMPARISONS.actual.json')
    ck(len(comparison_rows) == 515, 'all_515_declared_raw_comparisons')
    for row in comparison_rows:
        ck(row['equal'] is True and row['method'] == 'complete Python byte equality, not native cmp',
           'actual_raw_comparison_method_not_native_count')
        compare(row['left'], row['right'], row['role'])
    ck(Counter(r['role'] for r in RAW_COMPARISONS) == {'493_round0_round1_full_copy': 493,
       'physical_committed_science': 1, 'science_source_copy': 6, 'canonical_from_actual_stdout': 2,
       'second_native_canonical': 1, 'pair_canonical_input': 1, '10_source_only_build_copies': 10,
       'B_round1_pdf_complete_bytes': 1}, 'exact_raw_comparison_role_census')
    receipt_dirs = {p.parent.relative_to(B).as_posix() for p in B.rglob('RESULT.json')
                    if (p.parent / 'ATTEMPT.json').is_file()}
    ck(receipt_dirs == {r['directory'] for r in seal['native_receipts']} and len(receipt_dirs) == 63,
       'all_63_actual_native_pairs_in_final_seal')
    for directory in sorted(receipt_dirs):
        native(B / directory, 1 if directory in ('native/build01', 'native/audit01') else 0)
    ck([{'directory': r['directory'], 'native_returncode': r['native_returncode']} for r in NATIVE]
       == seal['native_receipts'], 'exact_native_seal_census_binding')
    replay_keys = obj(B / 'REPLAY_KEYS.json')
    ck(set(replay_keys['raw_native_command_directories']) == {str(B / n) for n in receipt_dirs - {'native/audit02'}},
       'audit_62_plus_completed_audit02_not_inflight_fabrication')
    ck(obj(B / 'native/audit02/stdout') == audit, 'complete_actual_audit02_stdout_result')
    semantic = obj(B / 'native/compare01/stdout')
    ck(semantic['checks'] == 198189 and semantic['status'] == 'PASS_FULL_SEMANTIC_COMPARISON_NOT_RAW_CROSS_SCHEMA_EQUALITY'
       and semantic['inputs_before'] == semantic['inputs_after'] and len(semantic['inputs_before']) == 7,
       'archived_full_semantic_comparison_binding_not_rerun')
    for path, expected in semantic['inputs_before'].items():
        pin(path, expected)
    ck(commitment_times[-1] < obj(B / 'native/compare01/ATTEMPT.json')['started_epoch'],
       'recorded_precomparison_commitment_before_actual_comparison')
    canonical = obj(B / 'CANONICAL.json')
    ck(canonical['checks'] == 51129 and sum(len(x['states']) for x in canonical['census']) == 4095 and
       [x['mass'] for x in canonical['census']] == list(range(1, 13)), 'original_B_canonical_census_not_new_science')
    ck(obj(B / 'PARAMETERS.json')['masses'] == list(range(1, 13)), 'original_parameter_box_unchanged')

    ledgers, membership_before, failed_extras = {}, {}, {}
    for label, count, configs in (('produce01', 3651, 40), ('pair01', 3653, 40),
                                  ('build01', 118353, 61), ('build02', 118355, 61)):
        folder = B / label
        before = obj(folder / 'INPUTS_BEFORE.json.gz')
        ck(set(before) == {'files', 'configuration', 'membership'} and len(before['files']) == count and
           len(before['configuration']) == configs and before['membership'] == sorted(before['files']),
           'complete_decoded_B_ledger_schema', label)
        extras = set(before['files']) - set(audit_inputs)
        ck(not extras if label != 'build01' else len(extras) == 12 and all(
           Path(p).is_relative_to(folder) and Path(p).relative_to(B).as_posix() in package for p in extras),
           'only_actual_failed_build_package_extra_roles', (label, sorted(extras)))
        for path, expected in before['files'].items():
            pin(path, expected)
            if path in extras:
                failed_extras[path] = expected
        membership_before[label] = current_membership(before, label.startswith('build'))
        context = obj(folder / 'CONTEXT.json')
        ck(context['environment'] == ENV and source_only_flags(context['flags']) and context['interpreter'] == '/usr/bin/python3.10',
           'recorded_inner_driver_settings', label)
        known = {v['real'] for v in before['files'].values()}
        phases = ('BEFORE',) if label == 'build01' else ('BEFORE', 'AFTER')
        for phase in phases:
            sample = obj(folder / ('PARENT_MAPS_' + phase + '.json'))
            for p in map_paths(sample['raw']) + [Path(p) for p in sample['modules'].values() if p]:
                ck(p.is_file() and str(p.resolve()) in known, 'archived_driver_observed_scope', (label, str(p)))
        if label == 'build01':
            ck(not (folder / 'INPUTS_AFTER.json.gz').exists() and not (folder / 'REPORT.json').exists() and
               not list((folder / 'commands').glob('pass_*')) and
               b"KeyError: 'real'" in raw(B / 'native/build01/stderr'), 'failed_build01_retained_incomplete')
        else:
            after, report = obj(folder / 'INPUTS_AFTER.json.gz'), obj(folder / 'REPORT.json')
            ck(before == after and report['status'] == 'PASS' and report['checks_passed'] is True and
               report['changed_inputs'] == [] and report['input_count'] == count and report['driver_cache_remained_absent'] is True,
               'full_original_before_after_and_report', label)
            payloads = obj(folder / 'PAYLOADS.json')
            ck(set(payloads) == {str(folder / n) for n in physical(folder) - {'PAYLOADS.json'}},
               'complete_run_nonself_payload_inventory', label)
            for path, expected in payloads.items():
                pin(path, expected)
            ck({n for n, code in report['native_commands']} == {p.name for p in (folder / 'commands').iterdir()}
               and all(code == 0 for n, code in report['native_commands']), 'complete_successful_run_command_census', label)
            for runtime in sorted(folder.glob('runtime_*.json')):
                sample = obj(runtime)
                settings = sample['settings']
                ck(settings['environment'] == ENV and settings['path'] == PY_PATH and source_only_flags(settings['flags'])
                   and not os.path.lexists(settings['xoptions']['pycache_prefix']), 'actual_scientific_source_only_settings', str(runtime))
                observed = [Path(p) for p in sample['existing_reads']] + map_paths(sample['maps_before']) + map_paths(sample['maps_after'])
                observed += [Path(p) for p in sample['modules'].values() if p]
                for p in observed:
                    ck(p.is_file() and str(p.resolve()) in known and p.suffix not in {'.pyc', '.pyo'} and
                       not any(v in p.parts for v in ('site-packages', 'dist-packages')), 'actual_scientific_observed_input_scope', str(p))
        ledgers[label] = before

    build = B / 'build02'
    products, historical_pdf_keys = {}, []
    for number in range(1, 5):
        directory = build / 'commands' / ('pass_' + str(number))
        before, after = obj(directory / 'SOURCE_BEFORE.json'), obj(directory / 'SOURCE_AFTER.json')
        ck(number == 1 or before == products[number - 1]['after'], 'complete_pass_product_key_chain', number)
        for path, expected in after.items():
            p = Path(path)
            ck(p.is_relative_to(build / 'source'), 'exact_local_generated_product_role', path)
            if p.suffix in ('.tex', '.bib'):
                ck(before[path] == expected, 'ten_manuscript_sources_unchanged_per_pass', path)
                pin(p, expected)
            elif p.name != 'main.pdf':
                ck(p.name in ('main.log', 'main.fls', 'main.aux', 'main.bbl', 'main.blg', 'main.out', 'main.toc'),
                   'named_preserved_product_role', path)
                pin(directory / p.name, expected['sha256'])
                ck(pin(directory / p.name)['size'] == expected['size'], 'preserved_pass_product_size', path)
            elif number < 4:
                historical_pdf_keys.append({'pass_number': number, 'recorded_key': expected,
                    'old_bytes_reread': False, 'role': 'intermediate output not consumed by FLS; no preserved old PDF assertion'})
            else:
                pin(p, expected)
        products[number] = {'before': before, 'after': after}
    ck(len(products[1]['before']) == 10 and all(Path(p).suffix in ('.tex', '.bib') for p in products[1]['before']),
       'actual_cold_source_only_initial_product_census')
    rebuilt_fls = []
    known = {v['real']: v['sha256'] for v in ledgers['build02']['files'].values()}
    for number in (1, 3, 4):
        directory = build / 'commands' / ('pass_' + str(number))
        prior = {v['real']: v['sha256'] for v in products[number]['before'].values()}
        generated = set()
        for line in raw(directory / 'main.fls').decode().splitlines():
            if not line.startswith(('INPUT ', 'OUTPUT ')):
                continue
            kind, spelling = line.split(' ', 1)
            p = Path(spelling); p = (p if p.is_absolute() else build / 'source' / p).resolve()
            if kind == 'OUTPUT':
                generated.add(str(p)); continue
            role = 'pinned_external' if str(p) in known else 'prior_product' if str(p) in prior else 'same_pass_recorded_output' if str(p) in generated else 'unresolved'
            ck(role != 'unresolved' and p.name != 'main.pdf', 'all_actual_consumed_FLS_roles_no_intermediate_PDF', str(p))
            selected = directory / p.name if p.is_relative_to(build / 'source') and p.suffix not in ('.tex', '.bib') else p
            rebuilt_fls.append({'pass_number': number, 'path': str(p), 'role': role,
                                'final_sha256': pin(selected)['sha256']})
    ck(rebuilt_fls == obj(build / 'FLS_CLOSURE.json') and len(rebuilt_fls) == 2461,
       'all_2461_recorder_events_exact_reclassified_physical_roles')
    final_log = raw(build / 'commands/pass_4/main.log').decode()
    ck(not re.search(r'undefined|multiply defined|Rerun to|Label\(s\) may have changed|Overfull|Underfull', final_log),
       'actual_final_build_log_diagnostics')
    text = raw(build / 'commands/pdftotext/stdout').decode()
    ck(not any(x in text for x in ('??', '[?]', '[VERIFY]')), 'actual_final_PDF_text_markers')
    metadata, fonts = raw(build / 'commands/pdfinfo/stdout').decode(), raw(build / 'commands/pdffonts/stdout').decode()
    embedding = re.findall(r'\s+(yes|no)\s+(?:yes|no)\s+(?:yes|no)\s+\d+\s+\d+\s*$', fonts, re.M)
    ck(re.search(r'^Pages:\s+6$', metadata, re.M) and len(embedding) == 20 and set(embedding) == {'yes'},
       'actual_measured_six_pages_twenty_embedded_fonts')
    view = obj(B / 'VIEW_build02.actual.json')
    ck(view['reviewer'] == '/root/p210_b_reviewer' and view['status'] == 'ALL_SIX_PAGES_ACTUALLY_VIEWED' and
       view['new_terminal_build_claim'] is False and [r['page'] for r in view['pages']] == list(range(1, 7)),
       'six_original_actual_view_declarations_not_receiver_view')
    pin(view['pdf_path'], view['pdf'])
    for row in view['pages']:
        ck(row['actually_viewed'] is True and bool(row['observation']), 'actual_page_observation_record', row['page'])
        pin(row['image_path'], row['image'])
    for doc in sorted(B.glob('*.md')):
        for href in stripped_links(raw(doc).decode()):
            target = href.strip().strip('<>').split('#', 1)[0]
            if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
                continue
            resolved = (doc.parent / unquote(target)).resolve()
            pin(resolved)
            LINKS.append({'document': doc.relative_to(B).as_posix(), 'href': target,
                          'physical': str(resolved), 'sha256': pin(resolved)['sha256']})
    link_key = lambda row: (row['document'], row['href'], row['physical'], row['sha256'])
    ck(sorted(LINKS, key=link_key) == sorted(seal['links'], key=link_key) and len(LINKS) == 17,
       'all_17_actual_B_local_links_independent_of_directory_enumeration_order')
    findings = obj(B / 'FINDINGS.json')
    ck(findings['phase'] == 'INITIAL_PENDING_ROOT_RESPONSE' and findings['current_manuscript_findings'] == [] and
       findings['current_open_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 0} and
       findings['reviewer_infrastructure_resolved_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 2} and
       findings['accepted_delta'] is False and findings['root_response_reviewed'] is False and
       b'INITIAL_PENDING_ROOT_RESPONSE' in raw(B / 'DELTA.md'), 'initial_findings_not_accepted_delta')
    membership_after = {label: current_membership(ledger, label.startswith('build')) for label, ledger in ledgers.items()}
    ck(membership_before == membership_after, 'current_known_membership_before_after')
    original_reads = dict(SEEN)
    for path, expected in original_reads.items():
        pin(path, expected, force=True)
    ck(all(SEEN[p] == v for p, v in audit_inputs.items()), 'all_120840_B_keys_exact_second_full_read')
    extra_keys = {p: v for p, v in SEEN.items() if p not in audit_inputs}
    full_key_digest = sha256(json.dumps(SEEN, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return {'schema': 'p210-B-initial-root-original-receiver-v1',
        'status': 'PASS_P210_B_INITIAL_ORIGINAL_RECEPTION_NOT_DELTA_ACCEPTANCE',
        'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'receiver_source': pin(Path(__file__).resolve()), 'checks': sum(CHECKS.values()), 'checks_by_kind': dict(CHECKS),
        'B_initial_manifest': pin(B / 'SHA256SUMS'), 'B_payloads': 407, 'Round1_physical_inputs': 509,
        'actual_external_seal_return': pin(SEAL_RETURN), 'native_originals_bound': len(NATIVE),
        'native_census': seal['native_receipts'], 'full_python_raw_comparisons': len(RAW_COMPARISONS),
        'raw_comparison_roles': dict(Counter(r['role'] for r in RAW_COMPARISONS)),
        'original_B_audit_ledger': pin(B / 'AUDIT_INPUTS.actual.json.gz'), 'B_named_keys_fully_read_twice': len(audit_inputs),
        'all_current_read_keys_count': len(SEEN), 'all_current_read_keys_canonical_json_sha256': full_key_digest,
        'canonical_key_encoding': 'json.dumps(full_map, sort_keys=True, separators=(comma,colon), ensure_ascii=True).encode()',
        'extra_read_keys_not_in_B_audit_ledger': extra_keys, 'failed_build01_twelve_sealed_extra_roles': failed_extras,
        'current_ledger_scope_closure': membership_after, 'frozen_link_rows': 71, 'B_local_links': len(LINKS),
        'intermediate_unconsumed_pdf_historical_keys_only': historical_pdf_keys,
        'initial_A_aliases': aliases, 'prior_control_physical_roles': {k: str(v) for k, v in historical.items()},
        'manifests': MANIFESTS, 'new_scientific_runs': 0, 'new_native_child_commands': 0,
        'new_builds': 0, 'new_page_views': 0, 'old_B_writers_or_receivers_executed': 0,
        'root_strict_B_pair': 'SEPARATE_OBLIGATION_NOT_BOUND_OR_PREGRANTED_HERE', 'accepted_delta': False,
        'scope': 'B initial artifacts only; fixed B120840 plus explicitly consumed package/inherited roles. No deep expansion of old A resource ledgers, no old intermediate PDF-byte claim, no reconstructed historical OS/outer startup trace.',
        'external': 'OWNER_AMBER / HOLD_EXTERNAL'}


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, indent=2))
