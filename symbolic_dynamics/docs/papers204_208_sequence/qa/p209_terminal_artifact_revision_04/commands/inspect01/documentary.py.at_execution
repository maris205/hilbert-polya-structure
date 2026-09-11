"""Bounded original-byte/schema/predicate preparation, never a target gate.

No old auditor, recorder, lifecycle helper, verifier or builder is imported or
executed. The source/data comparison is documentary and self-familiar: this
preparer authored revision03 and missed its precise root-view predicate.
"""
import ast
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
HERE = BATCH / 'qa/p209_terminal_artifact_revision_04'
OLD = BATCH / 'qa/p209_terminal_artifact_revision_03'
OUT = BATCH / 'qa/p209_terminal_artifact'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
A, B = [BATCH / ('reviews/p209_' + s) for s in ('a', 'b')]
FINAL = PAPER / 'qa_final'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PACKAGES = [
    ('p209_terminal_artifact_preparation', 347, '3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51'),
    ('p209_terminal_artifact_revision_01', 418, '855aba017f5a369c09696272579897324bbd906892b353d17f0c9eb6d7fcbcc5'),
    ('p209_terminal_artifact_revision_02', 79, '6e9c86fad5802ed82df5ffa78e3f7d7bc9c3bec00a04892c96e002db121ed6ed'),
    ('p209_terminal_artifact_revision_03', 47, '4863c739ce8189f19e484f33fd5b42ce8f69f3b292f42768ba638108c105a743'),
    ('p209_terminal_artifact/initial_01', 8, 'deb48a3ed612ad9e292436e2037a879df37a0a5e2204594702f436c73bbe4b04'),
    ('p209_terminal_artifact/initial_02', 8, '89ab791251744f3aa96911f871f108268c2ebb7e5e1da55329eea45eb70bbc96'),
    ('p209_terminal_artifact/initial_03', 8, '45f4751ce36bfdfd432b2b5193ef23c8c7b91fa109b88cc4e305fd59234af921'),
    ('p209_terminal_artifact/initial_04', 8, 'bf5d128c27762025552fc730ba363e05a44874e28b2b2857d02db3fa2c8c4c7d')]
CONTROLS = {
    ROOT / 'SYMBOLIC_DYNAMICS_STATE.md': '736e3f648bc6dda583254dcc58f49fc764043c30ea464ec524fac04f2ec67265',
    BATCH / 'PIPELINE_STATE.md': '70de1375b0b55339408b7399178a17f91f3058b3f068faa7c395ab633e525b47',
    BATCH / 'GIT_SYNC_RECEIPT.md': '303e1ad876f35fc6715d896f2979fd212f64aeb686ebd8ee1e2d649e9628b230',
    PAPER / 'PAPER_MANIFEST.sha256': '84337036dead70c7680aed5678ed770505b1caa0184b5f405d353c4d9a811c77',
    PAPER / 'ROOT_LIFECYCLE.md': '5d0381c67eb47234f19c962ffd55a1ad00f6617129c64bda62ff5736f24b87e4'}
PINS, CHECKS, PIN_CHECKS, ALIASES = {}, [], [], {}


def raw(path):
    path = Path(path)
    assert path.is_file(), str(path)
    if path.is_relative_to(ROOT):
        assert not path.is_symlink(), str(path)
    data = path.read_bytes()
    value = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    assert str(path) not in PINS or PINS[str(path)] == value, ('read changed', str(path))
    PINS[str(path)] = value
    return data


def obj(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            assert key not in result, ('duplicate JSON key', str(path), key)
            result[key] = value
        return result
    return json.loads(raw(path), object_pairs_hook=unique)


def save(name, data):
    path = HERE / name
    assert path.is_relative_to(HERE)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)


def dump(name, value):
    save(name, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def observe(key, matched, actual):
    CHECKS.append({'predicate': key, 'matched': bool(matched), 'actual_values': actual})


def pin(path, value, role, historical=False):
    original = Path(path)
    expected = value if isinstance(value, str) else value['sha256']
    selected = ALIASES.get((str(original), expected), original) if historical else original
    data = raw(selected)
    ok = sha256(data).hexdigest() == expected
    if isinstance(value, dict) and 'bytes' in value:
        ok = ok and len(data) == value['bytes']
    PIN_CHECKS.append({'original_path': str(original), 'physical_path': str(selected), 'wanted': value,
                      'actual': PINS[str(selected)], 'matched': ok, 'role': role})
    assert ok, ('pin mismatch', role, str(original), str(selected))
    return selected


def alias(original, target, digest):
    selected = pin(target, digest, 'declared_historical_alias')
    key = (str(original), digest)
    if key in ALIASES:
        assert raw(ALIASES[key]) == raw(selected), key
    else:
        ALIASES[key] = selected


def get_aliases():
    for key, target in obj(B / 'delta_check_02/EXACT_HISTORY_ALIASES.json').items():
        original, digest = key.rsplit(' @ ', 1)
        alias(original, target, digest)
    meta = obj(A / 'delta_check_02/HISTORICAL_PIN_ROLE_MAP.json')
    for original, row in meta['exact_documentary_aliases'].items():
        alias(original, row['preserved_exact_path'], row['original_sha256'])
    row = meta['initial_manifest_role']
    alias(row['original_path'], row['preserved_exact_path'], row['original_sha256'])
    for number in (1, 2):
        base = PAPER / ('frozen_round' + str(number))
        meta = obj(base / ('ROUND' + str(number) + '_PROVENANCE.json'))
        for row in meta['anchor_mapping'].values():
            alias(row['original_path'], base / row['physical_path'], row['sha256'])
        if number == 1:
            for row in meta['historical_external_resolution'].values():
                alias(row['original_path'], row['round1_physical_path'], row['sha256'])
        else:
            for row in meta['historical_input_resolution']:
                alias(row['original_path'], row['round2_physical_path'], row['sha256'])
    for letter in ('A', 'B'):
        for row in obj(BATCH / ('qa/P209_' + letter + '_ROOT_DELTA_INSPECTION.actual.json'))['historical_input_aliases']:
            assert set(row) == {'original_path', 'sha256', 'physical_path'}
            alias(row['original_path'], row['physical_path'], row['sha256'])
    for folder, digest in [
        ('central_lifecycle_p209_round1', '2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24'),
        ('central_lifecycle_p209_terminal_push', 'a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865')]:
        alias(BATCH / 'GIT_SYNC_RECEIPT.md', BATCH / 'qa' / folder / 'GIT_SYNC_RECEIPT.before.md', digest)


def rows(path):
    result = {}
    for line in raw(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match
        digest, rel = match.groups()
        assert rel not in result and not Path(rel).is_absolute() and '..' not in Path(rel).parts
        result[rel] = digest
    return result


def package(base, expected=None, count=None, name='SHA256SUMS'):
    data = rows(base / name)
    assert expected is None or PINS[str(base / name)]['sha256'] == expected
    physical = {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
    assert all(not p.is_symlink() for p in base.rglob('*'))
    assert set(data) == physical - {name} and name not in data
    assert count is None or len(data) == count
    for rel, digest in data.items():
        pin(base / rel, digest, 'complete_original_package:' + str(base))
    return {'base': str(base), 'manifest_name': name, 'payloads': len(data),
            'sha256': PINS[str(base / name)]['sha256'], 'complete_nonself': True}


def documents():
    paths = [p for base in (PAPER, A, B) for p in base.rglob('*.md')]
    paths += [BATCH / s for s in ('P209_A_RESPONSE.md', 'P209_B_RESPONSE.md')]
    paths += list((BATCH / 'qa').glob('P209_*.md'))
    return sorted(set(paths))


def strip_links(content):
    # Independent use of the inspected literal parser: not target execution.
    content = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', content)
    content = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', content)
    content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)


def links(corrected=False):
    mapped, origins, links0, origin_records, corrections = {}, {}, [], [], []
    for number in (0, 1, 2):
        base = PAPER / ('frozen_round' + str(number))
        if number == 0:
            table = obj(base / 'FROZEN_LINK_MAP.json')['links']
        else:
            meta = obj(base / ('ROUND' + str(number) + '_PROVENANCE.json'))
            table = list(meta['round1_core_link_map'] if number == 1 else meta['round2_historical_link_map'])
            table += meta['acceptance_and_historical_anchor_link_map']
        for row in table:
            pin(row['physical_target'], row['sha256'], 'frozen_link_target', historical=True)
            mapped[(str(base / row['document']), row['href'])] = row
    for (original, digest), preserved in ALIASES.items():
        if preserved.suffix == '.md' and (preserved.is_relative_to(A) or preserved.is_relative_to(B)):
            pin(preserved, digest, 'alias_semantic_origin')
            origins.setdefault(str(preserved), Path(original))
    for attempt in ('delta_check_01', 'delta_check_02'):
        for original, row in obj(A / attempt / 'RESPONSE_ORIGINALS_AND_COPIES.json').items():
            source, copy = Path(original), Path(row['copy'])
            observe('exact_A_response_copy_origin_path', source.is_relative_to(ROOT) and copy == A / attempt / 'exact_response_inputs' / source.name,
                    {'attempt': attempt, 'original': original, 'copy': str(copy)})
            pin(copy, row['sha256'], 'A_response_origin_copy')
            if corrected and (attempt, copy.name) in {
                ('delta_check_01', 'P209_A_RESPONSE.md'), ('delta_check_02', 'P209_A_RESPONSE.md'),
                ('delta_check_01', 'P209_A_ROOT_INITIAL_INSPECTION.md'), ('delta_check_02', 'P209_A_ROOT_INITIAL_INSPECTION.md')}:
                expected_source, expected_hash = {
                    'P209_A_RESPONSE.md': (BATCH / 'P209_A_RESPONSE.md', '3b84c6c6a39b890562a63fbcb76a1a1fdf683886b9f6670b4bdd05544c6e9459'),
                    'P209_A_ROOT_INITIAL_INSPECTION.md': (BATCH / 'qa/P209_A_ROOT_INITIAL_INSPECTION.md', 'c095b7365d9083b83f6cd802ea6a3c9fa372a8b670ba9b28ae11e29d562fe690')}[copy.name]
                previous = origins.get(str(copy))
                identity_rows = [r for r in obj(PAPER / 'frozen_round2/ROUND2_PROVENANCE.json')['historical_input_resolution']
                                 if r['original_path'] == str(copy) and r['round2_physical_path'] == str(copy)]
                observe('exact_four_A_identity_pin_semantic_origin_roles', source == expected_source and row['sha256'] == expected_hash
                        and previous == copy and len(identity_rows) == 1 and identity_rows[0]['sha256'] == expected_hash,
                        {'attempt': attempt, 'source': str(source), 'copy': str(copy), 'digest': row['sha256'],
                         'previous_alias_origin': str(previous), 'round2_identity_rows': identity_rows})
                corrections.append({'attempt': attempt, 'original_path': str(source), 'copy_path': str(copy), 'sha256': row['sha256'],
                                    'previous_alias_derived_origin': str(previous), 'correct_source_origin': str(source),
                                    'source_copy_table': str(A / attempt / 'RESPONSE_ORIGINALS_AND_COPIES.json'),
                                    'round2_identity_role': identity_rows[0]})
                origins[str(copy)] = source
            observe('same_explicit_document_origin', str(copy) not in origins or origins[str(copy)] == source, {'copy': str(copy), 'source': str(source)})
            origins[str(copy)] = source
    mapping = PAPER / 'source_context/MAPPING.json'
    pin(mapping, 'cc642a35e810b072e9cd4dcc8a9353e6fe0afc9f3c68eb2ff5546f876089245f', 'author_source_mapping_literal')
    for original, row in obj(mapping).items():
        if row['snapshot'].startswith('source_context/workspace/'):
            source, copy = Path(original), PAPER / row['snapshot']
            observe('exact_author_workspace_snapshot_origin_path', source.is_relative_to(ROOT) and row['snapshot'] == 'source_context/workspace/' + source.relative_to(ROOT).as_posix(),
                    {'original': original, 'snapshot': row['snapshot']})
            pin(copy, row, 'author_workspace_origin_copy')
            observe('same_explicit_document_origin', str(copy) not in origins or origins[str(copy)] == source, {'copy': str(copy), 'source': str(source)})
            origins[str(copy)] = source
    broles = obj(B / 'delta_check_01/EXACT_HISTORY_ALIASES.json')
    for name, digest in [('PAPER_STATUS.md', '304c24e871a27bd02bcd6db231abc37870fb263a01d4c081289bdd53e8718a73'),
                         ('ROOT_ADOPTION.md', '8f82ae0af7156131f14e9e6e849198f8b1c98564760c30d4bc121b50cf34f82e')]:
        source, copy = PAPER / name, B / 'delta_check_01/response_anchors' / name
        observe('exact_failed_B_anchor_origin_path', broles[str(source) + ' @ ' + digest] == str(copy), {'source': str(source), 'copy': str(copy), 'digest': digest})
        pin(copy, digest, 'failed_B_origin_copy')
        observe('same_explicit_document_origin', str(copy) not in origins or origins[str(copy)] == source, {'copy': str(copy), 'source': str(source)})
        origins[str(copy)] = source
    for row in obj(B / 'assignment_context/ROLES.json'):
        origins[row['preserved']] = Path(row['original'])
    for row in obj(B / 'delta_intake_01/INTAKE_RESULT.json')['copies']:
        origins[row['physical']] = Path(row['original'])
    for doc in documents():
        origin = origins.get(str(doc), doc)
        trace = [str(origin)]
        for iteration in range(12):
            previous = origin
            for token in ('/source_context/', '/assignment_context/', '/exact_response_inputs/', '/original_snapshot/'):
                if token in str(origin):
                    tail = str(origin).split(token, 1)[1]
                    if tail.startswith(('docs/', 'papers/', '.agents/')) or tail in ('AGENTS.md', 'SYMBOLIC_DYNAMICS_STATE.md'):
                        origin = ROOT / tail
                        break
            trace.append(str(origin))
            if origin == previous:
                break
        observe('finite_explicit_snapshot_origin', iteration < 11, {'document': str(doc), 'origin_trace': trace})
        origin_records.append({'document': str(doc), 'origin_trace': trace})
        for href in strip_links(raw(doc).decode()):
            target = href.strip().strip('<>').split('#', 1)[0]
            if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
                continue
            if (str(doc), href) in mapped:
                row = mapped[(str(doc), href)]
                selected = pin(row['physical_target'], row['sha256'], 'selected_frozen_link', historical=True)
                links0.append({'document': str(doc), 'semantic_origin': 'explicit-frozen-link-map', 'href': href, 'target': str(selected), 'sha256': row['sha256']})
            else:
                destination = (origin.parent / unquote(target)).resolve()
                observe('local_link_closure', destination.exists(), {'document': str(doc), 'href': href, 'origin': str(origin), 'resolved_target': str(destination)})
                links0.append({'document': str(doc), 'semantic_origin': str(origin), 'href': href, 'target': str(destination),
                               'exists': destination.exists(), 'is_file': destination.is_file(), 'is_dir': destination.is_dir()})
                if destination.is_file():
                    raw(destination)
    return {'documents': len(documents()), 'local_links': len(links0), 'explicit_frozen_link_rows': len(mapped),
            'resolved_links': links0, 'document_origins': origin_records,
            'origin_field_values': {k: str(v) for k, v in origins.items()}, 'named_four_role_corrections': corrections}


def views():
    path = BATCH / 'qa/P209_TERMINAL_ROOT_VIEWS.actual.json'
    record = obj(path)
    expected = {'schema': 'p209-terminal-root-every-page-view-v1', 'paper': 'P209',
                'status': 'ROOT_ACTUALLY_VIEWED_ALL_FOUR_FINAL_PAGES_PASS', 'reviewer': '/root',
                'measured_page_count': 4, 'open_visual_findings': 0}
    observe('actual_root_every_page_attestation.corrected_exact_field', all(record[k] == v for k, v in expected.items())
            and [p['page'] for p in record['pages']] == list(range(1, 5)) and 'page_count' not in record,
            {'expected': expected, 'actual': record, 'old_page_count_key_absent': 'page_count' not in record})
    pin(FINAL / 'SHA256SUMS', record['terminal_manifest_sha256'], 'root_view_exact_terminal_seal')
    pin(FINAL / 'cold_build_1/main.pdf', record['pdf_sha256'], 'root_view_exact_pdf')
    observe('root_view_exact_artifact', True, {k: record[k] for k in ('terminal_manifest_sha256', 'pdf_sha256')})
    for page in record['pages']:
        observe('actual_root_individual_view', page['path'] == str(FINAL / ('cold_build_1/pages/page-' + str(page['page']) + '.png'))
                and page['actually_displayed_and_viewed'] is True and bool(page['observation'].strip()), page)
        pin(page['path'], page['sha256'], 'archived_root_page_png_not_fresh_view')
    build = obj(FINAL / 'BUILD_EXECUTION.json')
    diagnostics = []
    for n in (1, 2):
        item = obj(FINAL / ('cold_build_' + str(n) + '_DIAGNOSTICS.json'))['diagnostics']
        observe('terminal_diagnostics_original_value_agreement', item == build['builds'][n - 1]['actual_diagnostics'], {'build': n, 'diagnostics': item})
        diagnostics.append(item)
    nonblocking = [line for row in diagnostics for kind in ('underfull', 'warnings') for line in row[kind]]
    observe('actual_nonblocking_diagnostic_disclosed' if nonblocking else 'no_fabricated_build_diagnostic',
            isinstance(record['retained_nonblocking_diagnostic'], str) and bool(record['retained_nonblocking_diagnostic'].strip()) if nonblocking else record['retained_nonblocking_diagnostic'] is None,
            {'original_nonblocking_rows': nonblocking, 'recorded': record['retained_nonblocking_diagnostic']})
    report = raw(BATCH / 'qa/P209_TERMINAL_ROOT_VIEWS.md').decode()
    observe('actual_view_report_external_hold', 'HOLD_EXTERNAL' in report, report)
    return {'actual_original_record': record, 'source_pin': PINS[str(path)], 'diagnostics': diagnostics, 'new_views': 0}


def failure04():
    base = OUT / 'initial_04'
    record, attempt = obj(base / 'COMMAND.json'), obj(base / 'ATTEMPT.json')
    wrapper_path = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_04.failed.actual.json'
    wrapper = obj(wrapper_path)
    pin(wrapper_path, '483bac2c8955b9958ed02eb3741ed8bbeda6c48f36ad1ae9f1996fe26d32a340', 'actual_root_failure_wrapper')
    before, after = obj(base / 'INPUTS_BEFORE.json'), obj(base / 'INPUTS_AFTER.json')
    observe('fourth_before_after_full_maps', before == after and len(before) == 16, {'before': before, 'after': after})
    for name, value in before.items():
        pin(name, value, 'fourth_original_before', historical=True)
    for name, value in after.items():
        pin(name, value, 'fourth_original_after', historical=True)
    expected_argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(base / 'unused_pycache'), str(OLD / 'audit_p209.py'), 'terminal-artifact-after-actual-views']
    observe('fourth_failed_child_remains_failure', record['exit_code'] == 1 and record['status'] == 'COMPLETED' and record['failure'] is None
            and record['inputs_unchanged'] and record['unused_cache_absent'] and not (base / 'unused_pycache').exists()
            and record['argv'] == expected_argv and record['cwd'] == str(ROOT) and record['environment'] == ENV, record)
    observe('fourth_failed_prespawn_record', attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None
            and all(attempt[k] == record[k] for k in ('argv', 'cwd', 'environment', 'started_utc')), attempt)
    for stream in ('stdout', 'stderr'):
        pin(base / ('audit.' + stream), record[stream], 'fourth_native_' + stream)
    error = raw(base / 'audit.stderr')
    observe('fourth_failed_full_raw_streams', raw(base / 'audit.stdout') == b'' and len(error) == 652 and sha256(error).hexdigest() == 'cffcade469b9bc33938a9102303db6a4fb7dd675943b58abe77645469a45881f', error.decode())
    observe('fourth_failed_root_wrapper_remains_failure', wrapper['completion']['exit_code'] == 1 and error.decode() in wrapper['completion']['output'], wrapper)
    for snapshot, source in [('executed_auditor_snapshot.py', 'audit_p209.py'), ('executed_recorder_snapshot.py', 'record_audit.py')]:
        observe('fourth_failed_exact_executed_sources', raw(base / snapshot) == raw(OLD / source), {'snapshot': str(base / snapshot), 'source': str(OLD / source)})
    return {'command': record, 'attempt': attempt, 'wrapper': wrapper, 'inputs_before': before, 'inputs_after': after}


def lifecycle_and_flow():
    body = raw(PAPER / 'ROOT_LIFECYCLE.md').decode()
    observe('separate_pending_root_lifecycle', all(word in body for word in ('P209', 'HOLD_EXTERNAL', 'ARTIFACT_GATE_PENDING')) and 'P209_INTERNALLY_COMPLETE' not in body, body)
    pin(PAPER / 'PAPER_STATUS.md', '304c24e871a27bd02bcd6db231abc37870fb263a01d4c081289bdd53e8718a73', 'unchanged_author_lifecycle_status')
    pin(PAPER / 'ROOT_ADOPTION.md', '8f82ae0af7156131f14e9e6e849198f8b1c98564760c30d4bc121b50cf34f82e', 'unchanged_author_adoption')
    absent = [BATCH / 'qa/P209_TERMINAL_ARTIFACT_ROOT_INSPECTION.actual.json', BATCH / 'qa/P209_TERMINAL_ARTIFACT_ROOT_INSPECTION.md',
              BATCH / 'P209_FINAL_QA.md', OUT / 'lifecycle_before', OUT / 'REPORT.md', OUT / 'SHA256SUMS', OUT / 'initial_05']
    states = {str(p): {'exists': p.exists(), 'is_file': p.is_file(), 'is_dir': p.is_dir()} for p in absent}
    observe('future_lifecycle_inputs_not_yet_created', not any(p.exists() for p in absent), states)
    sources = {}
    predicates = []
    for name in ('audit_p209.py', 'record_audit.py', 'lifecycle_audit.py'):
        source = raw(OLD / name).decode()
        tree = ast.parse(source)
        compile(tree, str(OLD / name), 'exec', dont_inherit=True, optimize=0)
        functions0 = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
        for fn in functions0:
            if name == 'audit_p209.py' and fn.name not in ('root_page_views', 'pages_and_links', 'stripped_links', 'main'):
                continue
            for node in ast.walk(fn):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'ck':
                    section = ast.literal_eval(node.args[1]) if isinstance(node.args[1], ast.Constant) else ast.get_source_segment(source, node.args[1])
                    predicates.append({'file': name, 'function': fn.name, 'line': node.lineno, 'section': section,
                                       'expression': ast.get_source_segment(source, node.args[0]),
                                       'source_sha256': sha256(ast.get_source_segment(source, node).encode()).hexdigest(),
                                       'phase': 'original static predicate inventory, NOT target execution'})
        sources[name] = {'source_pin': PINS[str(OLD / name)], 'functions': [fn.name for fn in functions0]}
    main = next(n for n in ast.parse(raw(OLD / 'audit_p209.py')).body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    calls = [n.value.func.id for n in main.body if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name)]
    observe('final_flow_exact_assigned_call_order', calls == ['actual_auditor_runtime', 'load_aliases', 'revision_originals_and_failure', 'manifest', 'frozen_and_author', 'reviews', 'strict_replays', 'terminal', 'root_page_views', 'pages_and_links', 'actual_auditor_runtime', 'dict'], calls)
    return {'current_lifecycle_body': body, 'future_input_presence': states, 'complete_source_predicates': predicates,
            'original_source_functions': sources, 'current_initial04_result': 'FAIL; no successful stdout ledger exists',
            'future_only_constraints': [
                'actual_initial_gate requires real ROOT_GATE/root report and a successful native initial_N audit stdout: absent, NOT EVALUATED.',
                'prepare requires accepted gate and complete OUT rollup before making six exact copies: gate/rollup absent, NOT EXECUTED.',
                'audit requires PRESERVATION.json, exact two old-paper aliases, actual lifecycle-only edit and prior success ledger: absent, NOT EVALUATED.',
                'original_runtime_coverage and recheck_resources require future successful audit ledger, current resource membership and actual process samples: NOT EVALUATED or synthesized.',
                'changed_paper requires only ROOT_LIFECYCLE.md plus its literal rollup line to change; current inputs are still pending and unchanged.',
                'new_links requires actual final QA/root report and completion text: not yet present, NOT EVALUATED.',
                'run and seal require genuine native child success and full streams before a new closure; neither was invoked.'],
            'independent_review': False, 'lifecycle_execution_count': 0}


def run(mode):
    assert Path(__file__).resolve() == HERE / 'documentary.py' and Path.cwd() == ROOT and dict(os.environ) == ENV
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    raw(Path(__file__)); raw(Path(sys.executable).resolve()); raw(HERE / 'record_documentary.py')
    for path, digest in CONTROLS.items():
        pin(path, digest, 'unchanged_central_and_paper_controls')
    original_packages = [package(BATCH / 'qa' / name, digest, count) for name, count, digest in PACKAGES]
    get_aliases()
    result = {'failure04': failure04(), 'views': views(), 'links': links(), 'lifecycle_and_final_flow': lifecycle_and_flow(),
              'original_packages': original_packages}
    if mode == 'inspect':
        result['corrected_links'] = links(corrected=True)
        dump('EXACT_FOUR_A_ORIGIN_ROLES.json', result['corrected_links']['named_four_role_corrections'])
        source_scope = obj(HERE / 'SCOPE.json')['input_pins']
        original_only = {k: v for k, v in PINS.items() if not Path(k).is_relative_to(HERE)}
        assert all(source_scope.get(k) == v for k, v in original_only.items()), 'new unscoped original read'
        selected = [OLD / p for p in ('audit_p209.py', 'record_audit.py', 'lifecycle_audit.py', 'REMAINING_SCHEMA_INSPECTION.md', 'inspect_originals.py')]
        selected += sorted(p for p in (OUT / 'initial_04').iterdir() if p.is_file())
        selected += [BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_04.failed.actual.json', BATCH / 'qa/P209_TERMINAL_ROOT_VIEWS.actual.json',
                     BATCH / 'qa/P209_TERMINAL_ROOT_VIEWS.md', PAPER / 'ROOT_LIFECYCLE.md', PAPER / 'PAPER_MANIFEST.sha256']
        copies = []
        for path in selected:
            target = HERE / 'original_snapshot' / path.relative_to(ROOT)
            save(target.relative_to(HERE), raw(path))
            argv = ['/usr/bin/cmp', '--', str(path), str(target)]
            child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
            copies.append({'original': str(path), 'copy': str(target), 'pin': PINS[str(path)], 'argv': argv,
                           'cwd': str(ROOT), 'env': ENV, 'exit_code': child.returncode, 'stdout': child.stdout.decode(), 'stderr': child.stderr.decode()})
            assert child.returncode == 0 and child.stdout == child.stderr == b''
        result['selected_native_copy_comparisons'] = copies
    before = dict(PINS)
    after = {name: {'sha256': sha256(Path(name).read_bytes()).hexdigest(), 'bytes': Path(name).stat().st_size} for name in before}
    assert before == after
    result.update({'schema': 'p209-revision04-original-predicate-documentary-v1', 'mode': mode, 'input_pins': before,
                   'inputs_after': after, 'inputs_unchanged': True, 'checks': CHECKS, 'pin_checks': PIN_CHECKS,
                   'unmatched_predicates': [row for row in CHECKS if not row['matched']],
                   'target_executions': 0, 'new_science_build_views': 0})
    dump('SCOPE.json' if mode == 'scope' else 'ORIGINAL_PREDICATE_INSPECTION.json', result)
    print(json.dumps({'mode': mode, 'original_and_execution_input_paths': len(before), 'predicates': len(CHECKS),
                      'unmatched': result['unmatched_predicates'], 'links': result['links']['local_links'],
                      'old_packages_preserved': len(original_packages), 'target_executions': 0}, sort_keys=True))
    if mode == 'scope':
        assert not result['unmatched_predicates'], 'actual original predicate mismatch retained in full output'
    else:
        expected = {str(A / attempt / 'exact_response_inputs' / name) for attempt in ('delta_check_01', 'delta_check_02')
                    for name in ('P209_A_RESPONSE.md', 'P209_A_ROOT_INITIAL_INSPECTION.md')}
        assert len(result['unmatched_predicates']) == 4
        assert all(r['predicate'] == 'same_explicit_document_origin' for r in result['unmatched_predicates'])
        assert {r['actual_values']['copy'] for r in result['unmatched_predicates']} == expected
        assert len(result['corrected_links']['named_four_role_corrections']) == 4


if __name__ == '__main__':
    assert sys.argv[1:] in (['scope'], ['inspect'])
    run(sys.argv[1])
