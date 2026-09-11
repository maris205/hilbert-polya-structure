#!/usr/bin/env python3
"""Read-only, P208-specific terminal artifact closure auditor.

Infrastructure adaptation informed by audit_p207.py and the P208 recorders.
No scientific producer/reviewer module is imported or executed. No TeX,
renderer, source search, acceptance decision or filesystem write occurs.
Historical evidence is selected only through explicit original-path/hash maps.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/208-original-snapshot-triangulation-sweeps'
A, B = [BATCH / ('reviews/p208_' + x) for x in ('a', 'b')]
FINAL = PAPER / 'qa_final'
OUT = BATCH / 'qa/p208_terminal_artifact'
CHECKS, READS, ALIASES, USED_ALIASES, HOST_RESOLUTIONS = Counter(), {}, {}, {}, {}
MANIFESTS, LINKS = [], []
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
BUILD_ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8',
             'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1788652800', 'FORCE_SOURCE_DATE': '1',
             'openin_any': 'p', 'openout_any': 'p'}
TEX_ROOTS = tuple(map(Path, ('/usr/share/texlive/texmf-dist/tex',
    '/usr/share/texlive/texmf-dist/fonts', '/usr/share/texlive/texmf-dist/web2c',
    '/usr/share/texlive/texmf-dist/bibtex', '/usr/share/texmf', '/var/lib/texmf',
    '/etc/texmf', '/usr/local/share/texmf', '/root/texmf',
    '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')))
CONFIG_ROOTS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/share/fonts',
    '/etc/fonts', '/var/cache/fontconfig', '/usr/share/fontconfig', '/usr/lib/locale/C.utf8',
    '/usr/lib/x86_64-linux-gnu/gconv', '/usr/share/poppler')))
SOURCE_NAMES = ('main.tex', 'math_commands.tex', 'references.bib',
    'sections/00_abstract.tex', 'sections/01_setup.tex', 'sections/02_cells.tex',
    'sections/03_sources.tex', 'sections/04_extremum.tex', 'sections/05_kmap.tex',
    'sections/06_clock.tex', 'sections/07_scope.tex')


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


def load_aliases():
    for review in (A, B):
        for name in ('FINDINGS.json', 'SHA256SUMS'):
            preserved = review / 'delta/initial_snapshot' / name
            alias(review / name, preserved, h(preserved))
    history = j(B / 'delta/HISTORY_INPUT_MAPPING.json')
    original = j(B / 'history_context/SEARCH_INPUTS_BEFORE.json')
    ck(original == j(B / 'history_context/SEARCH_INPUTS_AFTER.json') and len(history) == 1917,
       'history_scope', 'complete before/after initial search')
    ck(set(history) == {str(ROOT / n) for n in original}, 'history_scope', 'all original names')
    for name, row in history.items():
        rel = Path(name).relative_to(ROOT).as_posix()
        ck(row['historical_path'] == 'delta/history_inputs/' + rel and row['sha256'] == original[rel],
           'history_exact_mapping', name)
        alias(name, safe(B, row['historical_path']), row['sha256'])
    # Original admission contexts and B assignment snapshots have explicit
    # originals in their own before-pin records; they are never guessed by hash.
    base = BATCH / 'qa/p208_round0_input_inspection_v2/historical_workspace_origins'
    for rel, value in manifest_rows(base / 'SHA256SUMS').items():
        alias(ROOT / rel, base / rel, value)
    initial = j(B / 'INITIAL_PIN_RECORD.json')
    ck(len(initial['assignment_context']) == 10, 'initial_assignment_context', 'ten exact original paths')
    for original_name, row in initial['assignment_context'].items():
        alias(ROOT / original_name, B / row['snapshot'], row['before_sha256'])
    return history


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


def frozen_and_author():
    author = manifest(PAPER, 'AUTHOR_MANIFEST.sha256', complete=False, count=483)
    frozen = [manifest(PAPER / ('frozen_round' + str(k)), count=487) for k in range(3)]
    ck(frozen[0] == frozen[1] == frozen[2], 'frozen_full_identical', 'three full 487-entry closures')
    for rel, wanted in frozen[2].items():
        pin(PAPER / rel, wanted)
    ck(all(frozen[2].get(n) == d for n, d in author.items()), 'author_subset', 'all 483 exact author entries')
    for name, status in [('P208_ROUND1_FREEZE.actual.json', None),
                         ('P208_ROUND2_FREEZE.actual.json', 'ROOT_ROUND2_PHYSICAL_FREEZE_PASS')]:
        value = j(BATCH / 'qa' / name)
        if status:
            ck(value['status'] == status and value['copied_inputs'] == 487,
               'actual_round2', 'actual physical copy receipt')
            ck(value['manifest_sha256'] == h(PAPER / 'frozen_round2/SHA256SUMS'),
               'actual_round2', 'exact manifest receipt')
    for name in ('FINAL_THEOREM_CONTRACTS.md', 'P208_A_RESPONSE.md', 'P208_B_RESPONSE.md'):
        content = read(BATCH / name).decode()
        ck('P208' in content or '208' in content, 'contracts_responses', name)
    return {'author_entries': len(author), 'each_frozen_round': len(frozen[0]), 'live_exact': True}


def reviews(history):
    result = {}
    for letter, base, count, initial_count in [('a', A, 764, 743), ('b', B, 3545, 1546)]:
        sealed = manifest(base, count=count)
        findings = j(base / 'FINDINGS.json')
        ck(findings['reviewer'] == '/root/p208_' + letter + '_reviewer' and findings['delta_accepted'] is True,
           'distinct_review_acceptance', letter)
        ck(findings['census']['open'] == {'critical': 0, 'major': 0, 'minor': 0}
           and all(f['status'] == 'resolved' for f in findings['findings']),
           'zero_open_findings', letter)
        ck(findings['mathematical_verdict'] == 'MATH_VALID' and
           findings['value_verdict'] == 'GO_NARROW_TWO_AXIS' and not findings['manuscript_change_requested'],
           'accepted_narrow_verdict', letter)
        delta = read(base / 'DELTA.md').decode()
        ck('HOLD_EXTERNAL' in delta, 'external_hold', letter)
        root = j(BATCH / ('qa/P208_' + letter.upper() + '_ROOT_DELTA_INSPECTION.actual.json'))
        ck(root['status'] == 'ROOT_ACCEPTED_' + letter.upper() + '_DELTA_ORIGINAL_CLOSURE_PASS'
           and root['current_open_findings'] == 0 and root['review_manifest_entries'] == count,
           'actual_root_delta', letter)
        ck(root['review_manifest_sha256'] == h(base / 'SHA256SUMS') and
           root['delta_sha256'] == h(base / 'DELTA.md'), 'actual_root_delta_hashes', letter)
        initial = manifest_rows(base / 'delta/initial_snapshot/SHA256SUMS')
        ck(len(initial) == initial_count, 'initial_review_scope', letter)
        mapping = j(base / 'delta/INITIAL_PAYLOAD_MAPPING.json')
        if letter == 'a':
            ck(len(mapping) == initial_count and {r['original'] for r in mapping} == set(initial),
               'initial_review_mapping', letter)
            mapping = {r['original']: {'historical_path': r['preserved'], 'sha256': r['sha256']} for r in mapping}
        ck(set(mapping) == set(initial), 'initial_review_mapping', letter)
        for rel, row in mapping.items():
            expected = 'delta/initial_snapshot/FINDINGS.json' if rel == 'FINDINGS.json' else rel
            ck(row['historical_path'] == expected and row['sha256'] == initial[rel],
               'initial_review_exact_path', (letter, rel))
            pin(base / expected, initial[rel])
        baseline = j(base / 'delta/INPUTS_BEFORE.json')
        ck(len(baseline) == root['baseline_referents'], 'delta_full_dependency_count', letter)
        if letter == 'a':
            maps(baseline, historical=True)
            after = j(base / 'delta/INPUTS_AFTER.json')
            ck(set(after) == set(baseline), 'delta_full_before_after_names', letter)
            for name, value in baseline.items():
                selected = (base / 'delta/initial_snapshot' / Path(name).name
                            if name in (str(base / 'FINDINGS.json'), str(base / 'SHA256SUMS')) else Path(name))
                expected = {**value, 'pin_path': str(selected),
                            'historical_document_relocated': str(selected) != name}
                ck(after[name] == expected, 'delta_exact_enriched_after_schema', name)
                pin(selected, value)
            responses = pair_map(base / 'delta', 'ROOT_RESPONSE_PINS')
        else:
            for name, row in baseline.items():
                expected = (base / 'delta/initial_snapshot' / Path(name).name
                            if name in (str(base / 'SHA256SUMS'), str(base / 'FINDINGS.json'))
                            else base / history[name]['historical_path'] if name in history else Path(name))
                ck(str(expected) == row['validated_path'], 'delta_exact_dependency_mapping', name)
                pin(expected, row['sha256'])
            responses = j(base / 'delta/ROOT_RESPONSE_PINS_BEFORE.json')
            for name, row in responses.items():
                expected = 'delta/root_context/' + Path(name).relative_to(ROOT).as_posix()
                ck(row['snapshot'] == expected, 'root_response_snapshot_mapping', name)
                pin(name, row['sha256']); pin(base / expected, row['sha256'])
            for phase in ('audit01', 'audit02'):
                ck(j(base / 'delta' / phase / 'INPUTS_AFTER.json') == baseline,
                   'delta_full_before_after', (letter, phase))
                ck(j(base / 'delta' / phase / 'ROOT_RESPONSE_PINS_AFTER.json') == responses,
                   'delta_response_before_after', phase)
            for group in j(base / 'delta/CONFIGURATION_BEFORE.json').values():
                config(group)
        for phase, expected_checks in zip(('audit01', 'audit02'),
                                         (9083, 9091) if letter == 'a' else (120677, 120678)):
            d = base / 'delta' / phase
            cmd, rec = j(d / 'COMMAND.json'), j(d / 'audit.stdout')
            ck(cmd['exit_code'] == 0 and cmd['argv'][1:4] == ['-I', '-S', '-B'],
               'actual_documentary_delta_command', (letter, phase))
            for stream in ('stdout', 'stderr'):
                pin(d / ('audit.' + stream), cmd[stream] if letter == 'a' else cmd[stream + '_sha256'])
            ck(read(d / 'audit.stderr') == b'', 'actual_delta_empty_stderr', (letter, phase))
            ck(rec['assertions' if letter == 'a' else 'checks'] == expected_checks,
               'actual_delta_result', (letter, phase))
        # Preserve and read every resolved issue's actual original evidence.
        for issue in findings['findings']:
            for name in issue['preserved_evidence']:
                p = base / name
                ck(p.exists(), 'failed_history_preserved', (letter, issue['id'], name))
                if p.is_file():
                    read(p)
        result[letter] = {'accepted_manifest': h(base / 'SHA256SUMS'), 'payloads': len(sealed),
                          'initial_payloads_preserved': initial_count, 'dependency_referents': len(baseline),
                          'current_open': findings['census']['open']}
    return result


def strict_replays():
    summaries = {}
    for role, base, count in [('author', PAPER, 62101), ('a', A, 130961), ('b', B, 3144418)]:
        rr = BATCH / ('qa/root_replays/p208_' + role + '_strict')
        manifest(rr, count=38)
        rec = j(rr / 'RECEIPT.json')
        ck(rec['status'] in ('PASS_ROOT_P208_STRICT_PAIR', 'PASS_ROOT_P208_B_STRICT_PAIR')
           and rec['mode'] == role and rec['kind'] == 'ROOT_REPRODUCTION_NOT_AN_INDEPENDENT_REVIEW'
           and not rec['failures'] and len(rec['runs']) == 2, 'strict_pair_actual_result', role)
        inputs = pair_map(rr, 'INPUTS', historical=True)
        runtime = pair_map(rr, 'RUNTIME_INVENTORY')
        libraries = pair_map(rr, 'LIBRARIES')
        conf = j(rr / 'CONFIGURATION_BEFORE.json')
        ck(conf == j(rr / 'CONFIGURATION_AFTER.json'), 'strict_config_before_after', role); config(conf)
        ck((len(inputs), len(runtime), len(libraries), len(conf)) ==
           (rec['inputs'], rec['runtime_inventory'], rec['library_files'], rec['configuration_entries']),
           'strict_inventory_counts', role)
        covered = {str(Path(n).resolve()): (v if isinstance(v, str) else v['sha256'])
                   for group in (inputs, runtime, libraries) for n, v in group.items()}
        covered.update({v['resolved']: v['sha256'] for v in conf.values() if 'sha256' in v})
        ck(len(rec['commands']) == 7, 'strict_all_commands', role)
        for row in rec['commands']:
            argv = command(rr, row, ENV)
            if row['label'].startswith('run') and row['label'] in ('run1', 'run2'):
                ck(argv[1:4] == ['-I', '-S', '-B'] and argv[6] == '-c', 'strict_source_execution', role)
                ck(argv[7].encode() == read(rr / 'executed_wrapper_snapshot.py'),
                   'strict_literal_wrapper', role)
            if '_cmp' in row['label']:
                ck(argv[0] == '/usr/bin/cmp' and read(rr / row['stdout']['path']) == b'',
                   'actual_raw_cmp', row['label'])
                ck(read(Path(argv[1])) == read(Path(argv[2])), 'current_raw_cmp_reuse', row['label'])
        for run in rec['runs']:
            name = run['label']; source = rr / name / 'verify.py'
            initial = j(rr / (name + '_SOURCE_ONLY_INITIAL.json'))
            ck(set(initial) == {'verify.py'} and initial == run['initial_files'] == run['final_files'],
               'strict_source_only_exact', (role, name))
            pin(source, initial['verify.py']); ck(read(source) == read(base / 'verify.py'), 'strict_exact_producer', role)
            ck(physical(rr / name) == {'verify.py'}, 'strict_no_generated_file', (role, name))
            payload = j(rr / (name + '.stdout'))
            key = 'checks' if role == 'b' else 'assertions'
            ck(run[key] == payload[key] == count, 'strict_exact_science_count', (role, name))
            ck(read(rr / (name + '.stdout')) == read(base / 'CANONICAL.json'), 'strict_complete_canonical', (role, name))
            consumed = j(rr / (name + '_CONSUMED_RUNTIME.json'))
            ck(consumed['optimize'] == 0 and consumed['isolated'] == consumed['no_site'] == 1
               and consumed['dont_write_bytecode'] and consumed['cache_absent']
               and consumed['environment'] == ENV and not Path(consumed['pycache_prefix']).exists(),
               'strict_consumed_flags_environment', (role, name))
            observed = dict(consumed['mapped_files'])
            observed.update({v['path']: v['sha256'] for v in consumed['modules'].values() if 'path' in v})
            for path, wanted in observed.items():
                ck(covered.get(path) == wanted and not path.endswith('.pyc'), 'strict_consumed_full_coverage', path)
                pin(path, wanted)
        for when in ('before', 'after'):
            raw = read(rr / ('ldd_' + when + '.stdout')).decode()
            paths = {str(Path(p).resolve()) for p in re.findall(r'/[^\s():]+', raw) if Path(p).is_file()}
            ck('not found' not in raw and paths == set(libraries), 'strict_full_ldd_closure', (role, when))
        summaries[role] = {'runs': 2, 'checks_each': count, 'commands_exit_zero': 7,
                           'science_inputs': len(inputs), 'runtime': len(runtime),
                           'link_inventory_files_not_distinct_libraries': len(libraries), 'configuration': len(conf)}
    compare = j(BATCH / 'qa/P208_B_ROOT_PAYLOAD_INSPECTION.actual.json')
    ck(compare['status'] == 'PASS' and compare['checks'] == 266834 and compare['before'] == compare['after'],
       'complete_payload_comparison_receipt', 'actual root full scientific-field comparison reused')
    for row in compare['before'].values():
        pin(row['path'], row['sha256'])
    ck([r['n'] for r in compare['boxes']] == list(range(3, 11)) and
       sum(r['states'] for r in compare['boxes']) == 2055 and
       all(r['all_author_and_A_scientific_fields_equal'] for r in compare['boxes']),
       'complete_payload_comparison_scope', 'every labelled state in original fixed boxes')
    read(B / 'compare_payloads.py')
    return summaries


def tree_inventory(roots):
    return {str(p.resolve()): {'sha256': h(p.resolve()), 'bytes': len(read(p.resolve()))}
            for root in roots if root.is_dir() for p in root.rglob('*') if p.is_file()}


def terminal():
    manifest(FINAL, count=225)
    rec = j(FINAL / 'BUILD_EXECUTION.json')
    ck(rec['status'] == 'PASS_P208_TERMINAL_BUILD_PAIR_NOT_VIEWED' and not rec['failures']
       and len(rec['builds']) == 2 and len(rec['commands']) == 32,
       'terminal_actual_pair', 'actual two source-only builds, all commands retained')
    ck(rec['visual_review'] == 'PENDING_NOT_INFERRED_FROM_HASH_OR_RENDER',
       'terminal_build_not_view', 'immutable builder record does not counterfeit actual viewing')
    ck(read(FINAL / 'executed_recorder_snapshot.py') == read(BATCH / 'qa/run_p208_terminal_builds_v2.py'),
       'terminal_exact_recorder', 'literal executed v2 source')
    inventories = {}
    for stem in ('INPUTS', 'RUNTIME', 'LIBRARIES', 'TEX_INVENTORY', 'CONSUMED_TEX', 'RECORDER_INPUTS'):
        inventories[stem] = pair_map(FINAL, stem)
    conf = j(FINAL / 'CONFIGURATION_BEFORE.json')
    ck(conf == j(FINAL / 'CONFIGURATION_AFTER.json'), 'terminal_config_before_after', 'all known configuration'); config(conf)
    ck(tree_inventory(TEX_ROOTS) == inventories['TEX_INVENTORY'], 'terminal_tex_recapture', 'complete current tree names and bytes')
    candidates = set(CONFIG_ROOTS + TEX_ROOTS)
    tools = [Path('/usr/bin') / n for n in ('pdflatex', 'bibtex', 'kpsewhich', 'pdfinfo',
             'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp')] + [Path('/bin/bash'), Path(sys.executable).resolve()]
    candidates.update(tools)
    stdlib = Path('/root/miniconda3/lib/python3.12')
    python = Path('/root/miniconda3/bin/python3.12')
    candidates.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
        '/lib/ld-linux.so.2', '/lib64/ld-linux-x86-64.so.2', '/libx32/ld-linux-x32.so.2',
        '/root/miniconda3/lib/python312.zip', '/etc/locale.conf', '/etc/default/locale')))
    candidates.update([python.parent / 'pyvenv.cfg', python.parent.parent / 'pyvenv.cfg',
                       python.with_name(python.name + '._pth'), python.with_name('python._pth')])
    candidates.update(p for root in CONFIG_ROOTS if root.is_dir() for p in root.rglob('*') if p.is_file())
    ck(set(map(str, candidates)) == set(conf), 'terminal_complete_configuration_set', 'recaptured roots/explicit candidates')
    runtime_names = {str(p.resolve()) for p in stdlib.rglob('*') if p.is_file()
                     and 'site-packages' not in p.parts and '__pycache__' not in p.parts} | {str(p.resolve()) for p in tools}
    ck(runtime_names == set(inventories['RUNTIME']), 'terminal_complete_runtime_set', 'entire non-site non-bytecode stdlib and fixed tools')
    normalized = {v['resolved']: {'sha256': v['sha256'], 'bytes': v['bytes']} for v in conf.values() if v['is_file']}
    coverage = {**inventories['INPUTS'], **inventories['RUNTIME'], **inventories['LIBRARIES'],
                **normalized, **inventories['RECORDER_INPUTS']}
    for when in ('BEFORE', 'AFTER'):
        rt = j(FINAL / ('RECORDER_RUNTIME_' + when + '.json'))
        ck(all(t in rt['flags'] for t in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1'))
           and rt['environment'] == BUILD_ENV and not Path(rt['pycache_prefix']).exists(),
           'terminal_parent_runtime', when)
        for name, value in rt['mapped_files'].items():
            ck(coverage.get(name) == value, 'terminal_parent_map_coverage', name); pin(name, value)
        for value in rt['modules'].values():
            small = {k: value[k] for k in ('bytes', 'sha256')}
            ck(coverage.get(value['path']) == small and not value['path'].endswith('.pyc'),
               'terminal_parent_module_coverage', value['path']); pin(value['path'], small)
    bylabel = {}
    for row in rec['commands']:
        argv = command(FINAL, row, BUILD_ENV)
        ck(row['status'] == 'COMPLETED' and row['label'] not in bylabel, 'terminal_actual_command_unique', row['label'])
        bylabel[row['label']] = row
        attempt = j(FINAL / (row['label'] + '.attempt.json'))
        ck(attempt['status'] == 'ATTEMPTED' and attempt['argv'] == argv and attempt['cwd'] == row['cwd']
           and attempt['environment'] == BUILD_ENV and attempt['started_utc'] == row['started_utc'],
           'terminal_attempt_chronology', row['label'])
        if row['label'].endswith('_cmp'):
            ck(argv[0] == '/usr/bin/cmp' and read(Path(argv[1])) == read(Path(argv[2]))
               and read(FINAL / row['stdout']['path']) == b'', 'terminal_actual_raw_cmp', row['label'])
    for when in ('before', 'after'):
        raw = read(FINAL / ('ldd_' + when + '.stdout')).decode()
        found = {str(Path(p).resolve()) for p in re.findall(r'/[^\s():]+', raw) if Path(p).is_file()}
        ck('not found' not in raw and found == set(inventories['LIBRARIES']), 'terminal_full_ldd_closure', when)
    external_consumed = set()
    for k, row in enumerate(rec['builds'], 1):
        name = 'cold_build_' + str(k); cold = FINAL / name
        initial = j(FINAL / (name + '_SOURCE_ONLY_INITIAL.json'))
        ck(row['directory'] == name and initial == row['source_only_initial'] and set(initial) == set(SOURCE_NAMES),
           'terminal_source_only_set', k)
        for n, value in initial.items():
            pin(cold / n, value); pin(PAPER / 'frozen_round2' / n, value)
        for variable in ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR'):
            raw = read(FINAL / (name + '_' + variable + '.stdout')).decode().strip()
            p = Path(raw); p = (p if p.is_absolute() else cold / p).resolve()
            expected = {'query_value': raw, 'resolved': str(p), 'exists': False}
            key = name + ':' + variable
            ck(j(FINAL / (name + '_USER_ROOTS_BEFORE.json'))[key] == expected
               and j(FINAL / 'USER_ROOTS_AFTER.json')[key] == expected and not p.exists(),
               'terminal_effective_cwd_user_roots', key)
        for passno in (1, 2, 3):
            tex = bylabel[name + '_tex' + str(passno)]
            ck(tex['argv'] == ['/usr/bin/pdflatex', '-no-shell-escape', '-recorder',
               '-interaction=nonstopmode', '-halt-on-error', 'main.tex'] and tex['cwd'] == str(cold),
               'terminal_exact_tex_command', (k, passno))
            for line in read(FINAL / (name + '_pass' + str(passno) + '.fls')).decode().splitlines():
                if line.startswith('INPUT '):
                    p = Path(line[6:]); p = (p if p.is_absolute() else cold / p).resolve()
                    if not p.is_relative_to(cold):
                        ck(str(p) in inventories['CONSUMED_TEX'] and
                           inventories['CONSUMED_TEX'][str(p)] == inventories['TEX_INVENTORY'][str(p)],
                           'terminal_all_fls_consumed_coverage', str(p))
                        external_consumed.add(str(p))
        bst = read(FINAL / (name + '_bst.stdout')).decode().strip()
        ck(str(Path(bst).resolve()) in inventories['CONSUMED_TEX'], 'terminal_bibtex_style', bst)
        external_consumed.add(str(Path(bst).resolve()))
        ck(read(FINAL / (name + '_generated.bbl')) == read(cold / 'main.bbl'), 'terminal_actual_generated_bibliography', k)
        log = read(cold / 'main.log').decode()
        diagnostics = {key: re.findall(r'^.*' + pattern + r'.*$', log, re.M) for key, pattern in
                       [('undefined', 'undefined'), ('overfull', 'Overfull'), ('underfull', 'Underfull'), ('warnings', 'Warning')]}
        diagnostics['rerun'] = re.findall(r'^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$', log, re.M)
        ck(diagnostics == row['actual_diagnostics'] and diagnostics['underfull'] ==
           ['Underfull \\hbox (badness 5681) in paragraph at lines 9--13'] and
           all(not diagnostics[n] for n in ('undefined', 'overfull', 'warnings', 'rerun')),
           'terminal_exact_final_diagnostics', k)
        font = read(FINAL / (name + '_pdffonts.stdout')).decode()
        fonts = [s.split()[-5:] for s in font.splitlines()[2:] if s.strip()]
        ck(len(fonts) == row['embedded_fonts'] == 27 and all(v[0] == 'yes' for v in fonts),
           'terminal_all_fonts_embedded', k)
        pdfinfo = read(FINAL / (name + '_pdfinfo.stdout')).decode()
        ck(int(re.search(r'^Pages:\s+(\d+)$', pdfinfo, re.M).group(1)) == row['pages'] == 7,
           'terminal_page_count', k)
        text = read(FINAL / (name + '_main.txt')).decode()
        ck(not any(marker in text for marker in ('[VERIFY]', '??', '[?]')), 'terminal_resolved_text', k)
        pin(cold / 'main.pdf', row['pdf'])
        ck(read(cold / 'main.pdf') == read(PAPER / 'main.pdf'), 'terminal_exact_final_pdf', k)
        ck(physical(cold / 'pages') == {'page-' + str(i) + '.png' for i in range(1, 8)},
           'terminal_complete_render_set', k)
    ck(external_consumed == set(inventories['CONSUMED_TEX']), 'terminal_consumed_exact_union', 'all pass inputs plus located bibliography style')
    return {'payloads': 225, 'commands_actual_exit_zero': 32, 'source_files_per_build': 11,
            'inventories': {k: len(v) for k, v in inventories.items()}, 'configuration': len(conf),
            'pages': 7, 'fonts_embedded': 27, 'retained_underfull_badness': 5681,
            'boundary': rec['boundary']}


def pages_and_links():
    record = j(BATCH / 'qa/P208_TERMINAL_ROOT_VIEWS.actual.json')
    ck(record['status'] == 'ROOT_ACTUALLY_VIEWED_ALL_SEVEN_FINAL_PAGES_PASS' and record['reviewer'] == '/root'
       and record['open_visual_findings'] == 0 and [p['page'] for p in record['pages']] == list(range(1, 8)),
       'actual_root_page_view_receipt', 'seven actual attestations')
    ck(record['terminal_manifest_sha256'] == h(FINAL / 'SHA256SUMS') and
       record['pdf_sha256'] == h(FINAL / 'cold_build_1/main.pdf'), 'actual_root_page_view_exact_artifact', 'exact new terminal pair')
    for page in record['pages']:
        ck(page['path'] == str(FINAL / ('cold_build_1/pages/page-' + str(page['page']) + '.png'))
           and page['actually_displayed_and_viewed'] and bool(page['observation'].strip()),
           'actual_root_page_view_individual', page['page'])
        pin(page['path'], page['sha256'])
    ck('underfull' in record['pages'][-1]['observation'].lower() and '5681' in record['retained_nonblocking_diagnostic'],
       'actual_warning_page_inspected', 'bibliography page seven')
    report = read(BATCH / 'qa/P208_TERMINAL_ROOT_VIEWS.md').decode()
    ck('HOLD_EXTERNAL' in report and '5681' in report, 'actual_view_report_boundary', 'honest warning/external hold')
    # Frozen and source snapshots retain their semantic original directory for
    # relative documentation links. The rules below are structural, not an
    # existence-based fallback that could hide a broken live link.
    docs = [p for folder in (PAPER, A, B) for p in folder.rglob('*.md')]
    docs += [BATCH / n for n in ('P208_A_RESPONSE.md', 'P208_B_RESPONSE.md')]
    docs += list((BATCH / 'qa').glob('P208_*.md'))
    for doc in sorted(set(docs)):
        origin = Path(re.sub(r'/frozen_round[012]/', '/', str(doc)))
        # A searched historical document may itself be an older snapshot;
        # iterate these documented prefix maps until its original is reached.
        for unused in range(10):
            previous = origin
            for token in ('/delta/history_inputs/', '/delta/root_context/', '/history_context/snapshots/',
                          '/source_context/', '/assignment_context/', '/assignment_context_recovery/historical/',
                          '/source_inputs/', '/historical_workspace_origins/'):
                if token in str(origin):
                    tail = str(origin).split(token, 1)[1]
                    if tail.startswith(('docs/', 'papers/', '.agents/')) or tail in ('AGENTS.md', 'SYMBOLIC_DYNAMICS_STATE.md'):
                        origin = ROOT / tail
                        break
            if previous == origin:
                break
        ck(unused < 9, 'finite_nested_snapshot_origins', label(doc))
        # These two older extrema-audit source-only directories use *local*
        # source names, not workspace-relative ones. Their own actual receipt
        # binds the copied documentary bytes to the parent scout original.
        for number in ('01', '02'):
            audit = BATCH / ('scouting/finite_systems_thirteenth/extrema_audit_' + number)
            if origin == audit / 'source_inputs/PROOF_AND_DISPOSITION.md':
                receipt = j(audit / 'RECEIPT.json')
                source = audit.parent / 'PROOF_AND_DISPOSITION.md'
                ck(receipt['all_inputs_before'] == receipt['all_inputs_after'] and
                   receipt['all_inputs_before'][str(source)] == receipt['all_inputs_before'][str(origin)],
                   'historical_local_snapshot_origin', str(origin))
                pin(origin, receipt['all_inputs_before'][str(origin)])
                origin = source
        if '/input_snapshot/' in str(origin):
            origin = PAPER / str(origin).split('/input_snapshot/', 1)[1]
        if origin.parent == A / 'delta/initial_snapshot': origin = A / origin.name
        if origin.parent == B / 'delta/initial_snapshot': origin = B / origin.name
        provisional = BATCH / 'scouting/word_local/UGR_GATE/provisional_hold_01'
        if origin.parent == provisional and origin.name in (
                'CANDIDATE_GATE.md', 'SOURCE_AUDIT.md', 'EXECUTION_RECEIPT.md', 'PROVENANCE.md'):
            archive_note = read(provisional / 'README.md').decode()
            ck('These four working reports preceded manifest closure' in archive_note
               and 'current parent-directory' in archive_note,
               'exact_ugr_four_report_archival_origin', origin.name)
            origin = provisional.parent / origin.name
        content = read(doc).decode()
        # CommonMark code spans/fences do not contain Markdown links. This
        # removes code syntax before link extraction, not missing destinations.
        content = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', content)
        # An indented continuation of a preceding inline-code paragraph is
        # not a new indented code block: require document start or a blank.
        content = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', content)
        content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            target = target.strip().strip('<>').split('#', 1)[0]
            if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target): continue
            destination = (origin.parent / target).resolve()
            ck(destination.exists(), 'local_link_closure', (label(doc), target, label(origin)))
            LINKS.append({'document': label(doc), 'semantic_origin': label(origin), 'target': target,
                          'resolved_target': label(destination)})
    return {'actual_root_attested_pages': 7, 'auditor_views': 0, 'documents': len(set(docs)),
            'local_links': len(LINKS)}


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


def main():
    ck(len(sys.argv) == 1 and sys.flags.optimize == 0 and sys.flags.isolated == 1
       and sys.flags.no_site == 1 and sys.dont_write_bytecode,
       'auditor_invocation', 'no arguments, -I -S -B and optimize zero')
    began = datetime.now(timezone.utc).isoformat()
    read(Path(__file__).resolve())
    runtime_before = actual_auditor_runtime()
    history = load_aliases()
    whole = manifest(PAPER, count=2178)
    frozen = frozen_and_author()
    accepted = reviews(history)
    replays = strict_replays()
    builds = terminal()
    views = pages_and_links()
    status = read(PAPER / 'PAPER_STATUS.md').decode()
    ck('P208' in status and 'HOLD_EXTERNAL' in status and 'ARTIFACT' in status,
       'lifecycle_boundary', 'P208 artifact-stage held lifecycle')
    runtime_after = actual_auditor_runtime()
    before = dict(READS)
    for path, wanted in before.items():
        raw = Path(path).read_bytes()
        ck(wanted == {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)},
           'final_every_read_input_recheck', path)
    for path, resolved in HOST_RESOLUTIONS.items():
        ck(str(Path(path).resolve(strict=True)) == resolved, 'final_host_resolution_recheck', path)
    print(json.dumps({'paper': 'P208', 'status': 'PASS_P208_TERMINAL_ARTIFACT_GATE',
        'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'auditor_sha256': h(Path(__file__).resolve()), 'checks': sum(CHECKS.values()),
        'checks_by_section': dict(CHECKS), 'whole_paper_manifest_entries': len(whole),
        'frozen_and_author': frozen, 'accepted_reviews': accepted, 'root_strict_replays_reused': replays,
        'terminal_builds': builds, 'actual_root_views_and_links': views,
        'complete_manifests_validated': MANIFESTS, 'explicit_historical_aliases_used': USED_ALIASES,
        'actual_auditor_runtime_before': runtime_before, 'actual_auditor_runtime_after': runtime_after,
        'host_path_resolutions_rechecked': HOST_RESOLUTIONS,
        'all_local_links_checked': LINKS, 'all_consumed_input_count': len(before),
        'all_consumed_inputs_rechecked': before,
        'fresh_mathematical_executions': 0, 'fresh_builds': 0, 'fresh_page_views': 0,
        'role': 'Read-only artifact infrastructure; not a third manuscript review or reviewer delta acceptance.',
        'limits': ['Root proof/source judgment remains controlling; this audit proves no all-size theorem.',
                   'Prior actual author/A/B strict pairs are reused only under the entire unchanged recorded input/runtime key.',
                   'Original failures, reviewer development qualifications and accepted documentary deltas remain original evidence.',
                   'Terminal known-resource inventories and sampled parent maps do not reconstruct a hermetic OS or unobserved child/transient loads.',
                   'Actual root final-page attestations are checked, not replaced by hash-based viewing.',
                   'Only P208 is audited; no five-paper batch completion, specialist review or external clearance is asserted.',
                   'Future lifecycle-only edits require a separately preserved follow-up audit, not replacement of this initial result.'],
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
