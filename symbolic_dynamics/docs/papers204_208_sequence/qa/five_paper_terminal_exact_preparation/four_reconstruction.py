#!/usr/bin/env python3
"""New exact-five module: source-preserving reconstruction of accepted four.

All old predicates/selectors below are retained. The only old documentary
read substitution is the exact run02 current-index value, physically saved
at central_round2_p210. Its original lexical key and metadata are retained
only until the entire accepted 142784-key canonical digest is reproduced.
The new exact-five driver separately binds current physical keys and P210.
No original four checker or scientific program is imported or executed.
"""
import argparse
import ast
from collections import Counter
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import sysconfig
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
HERE = QA / 'five_paper_terminal_gate_revision_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
IDS = ('P205', 'P207', 'P208', 'P209')
ZERO = {'critical': 0, 'major': 0, 'minor': 0}
READS, STATES, TREES, ALIASES, USED_ALIASES = {}, {}, {}, {}, {}
MEMBERSHIPS = []
CHECKS, RAW_PAIRS, LINK_COUNT = 0, 0, 0
HISTORICAL_FOUR_PHASE = True
FOUR_INDEX = QA.parent / 'FINAL_THEOREM_CONTRACTS.md'
FOUR_INDEX_COPY = QA / 'central_round2_p210/FINAL_THEOREM_CONTRACTS.md'
FOUR_INDEX_KEY = {'sha256': '329cb32f4764dd59b1a500a8c21ef7dd4b2d83c87dd781d9934a413142f2a914',
    'bytes': 28714, 'resolved': str(FOUR_INDEX), 'symlink': None}


def need(ok, rule, detail=None):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError((rule, detail))


def absolute(path):
    path = Path(path)
    return path if path.is_absolute() else ROOT / path


def historical_read_path(path):
    path = absolute(path)
    if HISTORICAL_FOUR_PHASE and path == FOUR_INDEX:
        need(FOUR_INDEX_COPY.is_file() and FOUR_INDEX_COPY.resolve() == FOUR_INDEX_COPY and
             not FOUR_INDEX_COPY.is_symlink(), 'Exact actual preserved run02 current-index physical role')
        return FOUR_INDEX_COPY
    return path


def measured(path):
    path = absolute(path)
    need(path.is_file(), 'Missing file key', str(path))
    if path.is_relative_to(ROOT):
        need(path.resolve() == path and not path.is_symlink(), 'No workspace symlink alias', str(path))
    h, size = hashlib.sha256(), 0
    with historical_read_path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
            size += len(chunk)
    result = {'sha256': h.hexdigest(), 'bytes': size, 'resolved': str(path.resolve()),
              'symlink': os.readlink(path) if path.is_symlink() else None}
    if HISTORICAL_FOUR_PHASE and path == FOUR_INDEX:
        need(result == FOUR_INDEX_KEY, 'Exact old index bytes and original lexical resolved metadata')
    return result


def selected(path, expected=None, historical=False):
    path = absolute(path)
    digest = expected if isinstance(expected, str) else expected.get('sha256') if expected else None
    key = (str(path), digest, historical)
    if historical and key in ALIASES:
        need(type(historical) is str, 'Exact historical role/case only', (str(path), historical))
        target = absolute(ALIASES[key]['physical'])
        USED_ALIASES[str(path) + ' @ ' + digest + ' [' + historical + ']'] = str(target)
        return target
    return path


def pin(path, expected=None, historical=False):
    origin = absolute(path)
    path = selected(origin, expected, historical)
    name = str(path)
    if name not in READS:
        READS[name] = measured(path)
    actual = READS[name]
    expected = {'sha256': expected} if isinstance(expected, str) else expected
    if expected:
        for field in ('sha256', 'bytes', 'resolved', 'symlink'):
            if field in expected and not (path != origin and field in ('resolved', 'symlink')):
                need(actual[field] == expected[field], 'Changed key: affected check must reopen',
                     {'path': str(origin), 'physical': name, 'field': field})
    return actual


def raw(path, expected=None, historical=False):
    target = selected(path, expected, historical)
    before = pin(path, expected, historical)
    data = historical_read_path(target).read_bytes()
    need(len(data) == before['bytes'] and hashlib.sha256(data).hexdigest() == before['sha256'],
         'Complete read stable', str(target))
    return data


def decode(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            need(key not in result, 'Duplicate JSON field', key)
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=unique)


def obj(path):
    return decode(raw(path))


def equal(left, right):
    global RAW_PAIRS
    pin(left); pin(right)
    with absolute(left).open('rb') as a, absolute(right).open('rb') as b:
        while True:
            x, y = a.read(1024 * 1024), b.read(1024 * 1024)
            need(x == y, 'Complete raw pair mismatch', (str(left), str(right)))
            if not x:
                break
    RAW_PAIRS += 1


def physical(base):
    base = absolute(base)
    entries = list(base.rglob('*'))
    need(base.is_dir() and base.resolve() == base and all(not p.is_symlink() for p in entries),
         'Physical package, no redirect', str(base))
    names = {p.relative_to(base).as_posix() for p in entries if p.is_file()}
    if str(base) in TREES:
        need(names == TREES[str(base)], 'Package membership changed', str(base))
    TREES[str(base)] = names
    return names


def manifest(spec, historical=False):
    seal = absolute(spec['path'])
    base = absolute(spec.get('base', str(seal.parent)))
    pin(seal, spec['sha256'], historical)
    data = raw(seal, spec['sha256'], historical)
    need(data.endswith(b'\n'), 'Nonself manifest terminal LF', str(seal))
    rows = {}
    own = seal.relative_to(base).as_posix()
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'Strict manifest syntax', str(seal))
        digest, name = match.groups(); p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and p.as_posix() == name and
             name != own and name not in rows, 'Safe unique nonself member', name)
        rows[name] = digest
        pin(base / name, digest, historical)
    need(len(rows) == spec['payload_rows'] and set(rows) == physical(base) - {own},
         'Complete nonself physical manifest', str(seal))
    return rows


def package(spec):
    return manifest({'path': str(Path(spec['root']) / 'SHA256SUMS'),
                     'sha256': spec['manifest']['sha256'], 'payload_rows': spec['payloads']})


def current_state(path, expected):
    path = absolute(path)
    symlink = path.is_symlink()
    actual = {'exists': path.exists(), 'lexists': os.path.lexists(path), 'is_file': path.is_file(),
              'is_dir': path.is_dir(), 'resolved': str(path.resolve()), 'link': os.readlink(path) if symlink else None}
    actual['symlink'] = symlink if type(expected.get('symlink')) is bool else actual['link']
    if path.is_file():
        actual.update({k: pin(path)[k] for k in ('sha256', 'bytes')})
    need(set(expected) <= set(actual), 'Unknown state fields', (str(path), sorted(set(expected) - set(actual))))
    need(all(actual[k] == v for k, v in expected.items()), 'Current configuration/presence key', str(path))
    # Retain every exact recorder schema. A bool-valued symlink field in the
    # four-build key and a string-valued link field in a strict pair are not
    # interchangeable schemas, though they may name the same physical file.
    state_key = (str(path), json.dumps(expected, sort_keys=True))
    STATES[state_key] = expected


def absent(path):
    current_state(path, {'lexists': False, 'exists': False, 'is_file': False, 'is_dir': False})


def interval(before, after, historical=False, expected_entries=None):
    left = obj(before)
    need(left and left == obj(after), 'Complete original before/after key', str(before))
    if expected_entries is not None:
        need(len(left) == expected_entries, 'Exact original interval cardinality', str(before))
    for name, value in left.items():
        pin(name, value, historical)
    return left


def membership(label, function, expected):
    actual = function()
    need(actual == expected, 'Current exact resource membership', label)
    MEMBERSHIPS.append((label, function, expected))


def read_selector(name, provenance):
    """Only our sealed key-selection excerpt is imported, never an old program."""
    record = provenance[name]
    pin(record['source'], record['source_sha256'])
    original = raw(record['source']).decode()
    blocks = []
    for node in ast.parse(original).body:
        key = node.name if isinstance(node, (ast.FunctionDef, ast.ClassDef)) else (
            node.targets[0].id if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) else None)
        if key in record['selected_nodes']:
            blocks.append(ast.get_source_segment(original, node))
    excerpt = '\n\n'.join(blocks) + '\n'
    need(len(blocks) == len(record['selected_nodes']) and hashlib.sha256(excerpt.encode()).hexdigest() ==
         record['excerpt_sha256'] and raw(HERE / name).decode().endswith(excerpt),
         'Exact disclosed unchanged selector excerpt', name)
    spec = importlib.util.spec_from_file_location(name[:-3], HERE / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.raw = raw
    module.need = module.require = need
    return module


def bind_alias(row):
    origin, target = absolute(row['original']), absolute(row['physical'])
    need(target.is_relative_to(ROOT) and row['kind'] == 'documentary_exact_old_path_hash',
         'No scientific/runtime alias', row)
    need(origin.suffix.lower() in {'.md', '.json', '.sha256'} or origin.name.startswith('SHA256SUMS'),
         'Explicit documentary alias extension', str(origin))
    for case in row['cases']:
        key = (str(origin), row['sha256'], case)
        if key in ALIASES:
            need(absolute(ALIASES[key]['physical']) == target, 'Conflicting exact historical role', str(origin))
        ALIASES[key] = row
    pin(target, row['sha256'])


def census(paper, row, actual):
    role = row['role']
    need(actual['reviewer'] == row['reviewer'],
         'Exact accepted current census/reviewer', (paper, role))
    if paper == 'P205':
        need(all(v == 0 for v in actual['counts'].values()) and not actual['findings'] and
             actual['acceptance']['delta_status'] == 'ACCEPTED_EXACT_NO_CHANGE' and
             actual['review_state'] == role + '_ACCEPTED_NO_CHANGE' and
             actual['input'].endswith('frozen_round' + str(row['input_round'])) and
             not actual['independence']['is_proof_or_manuscript_author'] and
             not actual['independence']['supplied_new_lemma_or_manuscript_text'], 'P205 exact accepted schema')
    elif paper in ('P207', 'P208'):
        need(actual['census']['open'] == ZERO and all(f['status'] == 'resolved' for f in actual['findings']),
             'Exact zero current findings with history retained', (paper, role))
        need(actual['accepted_delta'] is True if paper == 'P207' else actual['delta_accepted'] is True,
             'Actual accepted documentary/no-change delta', (paper, role))
    else:
        need(actual['current_open_counts'] == ZERO and not actual['findings'] and
             actual['input_round'] == row['input_round'] and
             (actual['verdict'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA' if role == 'A' else
              actual['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'), 'P209 exact CURRENT_FINDINGS schema')


def theorem_ceilings(contract):
    live = raw(contract['current_index']).decode()
    need('HOLD_EXTERNAL' in live, 'Current theorem-index external hold')
    for ident, row in contract['five_ceilings'].items():
        section = live.split('## ' + ident + ' — ', 1)[1].split('\n## ', 1)[0]
        body = section.split(row['body_start'], 1)[1].split('\nPaper path:', 1)[0]
        body = row['body_start'] + body
        need(hashlib.sha256(body.encode()).hexdigest() == row['sha256'] and len(body.encode()) == row['bytes'],
             'Exact retained mathematical ceiling changed; review required', ident)
    need(set(contract['five_ceilings']) == {*IDS, 'P210'}, 'All five exact theorem ceilings, no duplicate seats')


def completion_artifacts(contract):
    need([p['id'] for p in contract['papers']] == list(IDS), 'Exactly four previously completed IDs')
    for p in contract['papers']:
        ident, base = p['id'], absolute(p['paper'])
        manifest(p['completion_key']['whole_paper'])
        if 'package' in p['completion_key']:
            manifest(p['completion_key']['package'])
        need([r['round'] for r in p['physical_freezes']] == [0, 1, 2], 'Three physical accepted rounds', ident)
        for freeze in p['physical_freezes']:
            manifest(freeze['manifest'])
            for name, value in p['scientific_pins'].items():
                # Accepted scientific bytes are stable; growing documentary
                # acceptance anchors retain their own distinct round seals.
                pin(base / ('frozen_round' + str(freeze['round'])) / name, value)
                pin(base / name, value)
        need([r['role'] for r in p['accepted_reviews']] == ['A', 'B'] and
             [r['input_round'] for r in p['accepted_reviews']] == [0, 1], 'Exactly two chronological manuscript roles', ident)
        reviewers = []
        for row in p['accepted_reviews']:
            manifest(row['final_manifest'])
            for name in ('REPORT.md', 'SOURCE_AND_PROOF.md', 'REPLAY_LOG.md', 'BUILD_REPORT.md',
                         'verify.py', 'CANONICAL.json', 'INPUT_PINS.sha256', 'DELTA.md'):
                pin(absolute(row['accepted_delta']).parent / name)
            pins = raw(absolute(row['accepted_delta']).parent / 'INPUT_PINS.sha256').decode().splitlines()
            names = set()
            for line in pins:
                match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
                need(match is not None, 'Exact workspace-relative review input pin')
                digest, name = match.groups(); target = Path(name)
                need(target.parts and not target.is_absolute() and '..' not in target.parts and
                     name not in names, 'Safe unique reviewed input role', name)
                names.add(name); pin(ROOT / name, digest)
            prefix = p['paper'] + '/frozen_round' + str(row['input_round']) + '/'
            need(any(name.startswith(prefix) for name in names) and not any(
                 p['paper'] + '/frozen_round' + str(n) + '/' in name for name in names for n in range(3) if n != row['input_round']),
                 'Actual A-from-Round0/B-from-Round1 pinned start', (ident, row['role']))
            pin(row['current_census'], row['current_census_pin'])
            census(ident, row, obj(row['current_census']))
            reviewers.append(row['reviewer'])
            need(row['reviewer'] not in p['proof_contributors'], 'Reviewer is a disclosed noncontributor', ident)
            pin(row['accepted_delta'], row['accepted_delta_pin'])
        need(len(set(reviewers)) == 2, 'Distinct actual A/B processes', ident)
    # Physical preservation, not quota-based renumbering or acceptance.
    for row in contract['rejected_preservation']:
        for name, value in row['pins'].items():
            pin(name, value)


def supplemental_pairs(contract, strict):
    record = obj(contract['strict_root_completion'])
    need(record['exit_code'] == 0, 'Actual root six-pair receiver exit')
    result = decode(record['output'].encode())
    need(result['status'] == 'PASS_ROOT_SIX_STRICT_PAIR_ORIGINAL_RECEPTION' and result['checks'] == 108000,
         'Pinned passing six-pair original reception')
    expected_roles = {p.lower() + '_' + role for p in IDS[:2] for role in ('author', 'a', 'b')}
    need(set(contract['supplemental_pairs']) == expected_roles, 'Exactly six strict replacements')
    received_pairs = {row['role']: row for row in result['pairs']}
    need(set(received_pairs) == expected_roles, 'All six root-received pair roles')
    for role, spec in contract['supplemental_pairs'].items():
        base = absolute(spec['directory'])
        received = received_pairs[role]
        need(received['pair_manifest']['sha256'] == spec['manifest']['sha256'] and
             received['checks_each'] == spec['checks_each'] and received['native_commands'] == 9,
             'Root original result binds exact supplemental manifest/count', role)
        manifest(spec['manifest'])
        result = obj(base / 'RESULT.json')
        need(result['status'] == 'PASS_ROOT_BATCH_TERMINAL_STRICT_PAIR' and not result['errors'] and
             result['role'] == role and result['raw_canonical_comparisons'] == 2 and
             result['raw_pair_comparisons'] == 1, 'Actual strict supplemental pair', role)
        interval(base / 'INPUTS_BEFORE.json', base / 'INPUTS_AFTER.json')
        names = obj(base / 'RESOURCE_NAMES_BEFORE.json')
        need(names == obj(base / 'RESOURCE_NAMES_AFTER.json'), 'Original resource membership interval')
        membership(role, strict.current_resources, names)
        conf = obj(base / 'CONFIGURATION_BEFORE.json')
        need(conf == obj(base / 'CONFIGURATION_AFTER.json'), 'Strict configuration interval')
        for name, row in conf.items():
            current_state(name, row)
        for suffix in ('parent', 'child_01', 'child_02'):
            absent(base / ('unused_' + suffix + '_cache'))
        pin(spec['producer'], spec['producer_pin']); pin(spec['canonical'], spec['canonical_pin'])
        for number in ('01', '02'):
            output = base / ('commands/03_verify_' + number + '/stdout.raw')
            equal(output, spec['canonical'])
            need(obj(output)[spec['check_field']] == spec['checks_each'], 'Unchanged scientific box/canonical count', role)


def supplemental_builds(contract, buildkeys):
    outer = obj(contract['four_build_root_completion'])['result']
    need(outer['exit_code'] == 0, 'Actual four-build root receiver exit')
    accepted = decode(outer['output'].encode())
    need(accepted['status'] == 'PASS_FOUR_BUILD_ORIGINAL_DOCUMENTS_ONLY' and accepted['checks'] == 400754,
         'Pinned passing corrected original four-build reception')
    spec = contract['supplemental_builds']; base = absolute(spec['directory'])
    need(accepted['build_seal'] == spec['manifest']['sha256'] and accepted['original_payloads'] == 387 and
         accepted['original_commands'] == 58, 'Root original result binds exact four-build package')
    manifest(spec['manifest'])
    groups = []
    for phase in ('BEFORE', 'AFTER'):
        path = base / ('KNOWN_INPUTS_' + phase + '.json.gz')
        compressed = raw(path); body = gzip.decompress(compressed); value = decode(body)
        meta = obj(str(path) + '.meta.json')
        need(meta == {'encoding': 'gzip of exact UTF-8 JSON with terminal LF; mtime=0',
                     'json_bytes': len(body), 'json_sha256': hashlib.sha256(body).hexdigest(),
                     'compressed': {k: pin(path)[k] for k in ('sha256', 'bytes')},
                     'semantic_groups': {k: len(v) for k, v in value.items()}}, 'Complete lossless existing key ledger')
        groups.append(value)
    need(groups[0] == groups[1], 'Full original build key interval')
    buildkeys.known_membership(groups[0])
    MEMBERSHIPS.append(('four-build grouped selection', lambda: buildkeys.known_membership(groups[0]), None))
    for values in groups[0].values():
        for name, value in values.items():
            current_state(name, value)
    for stem in ('ORIGINALS', 'LIBRARIES', 'CONSUMED_TEX'):
        interval(base / (stem + '_BEFORE.json'), base / (stem + '_AFTER.json'))
    views = obj(contract['four_build_views'])
    need(views['status'] == 'PASS_ROOT_TEN_ACTUAL_SUPPLEMENTAL_TERMINAL_PAGE_VIEWS' and
         views['viewer'] == '/root' and [r['paper'] for r in views['papers']] == ['P205', 'P207'],
         'Actual separate ten-page root attestation, not PNG existence')
    for view in views['papers']:
        ident = view['paper']; expected = spec['papers'][ident]
        need(view['page_count'] == expected['pages'] and view['pdf_pin'] == expected['pdf'], 'Selected final PDF/view key')
        for number in (1, 2):
            cold = base / (ident + '_cold_build_' + str(number))
            initial = obj(base / (cold.name + '_SOURCE_ONLY_INITIAL.json'))
            need(initial == expected['source_pins'], 'Exact original source-only start', str(cold))
            for name, value in initial.items():
                pin(cold / name, value)
            pin(cold / 'main.pdf', expected['pdf'])
            equal(cold / 'main.pdf', expected['paper'] + '/main.pdf')
        need([r['number'] for r in view['pages']] == list(range(1, expected['pages'] + 1)), 'Every final page exactly once')
        for row in view['pages']:
            need(row['viewed'] is True and row['observation'].strip() and row['path'] ==
                 str(base / (ident + '_cold_build_1/pages/page-' + str(row['number']) + '.png')), 'Actual exact viewed frame')
            pin(row['path'], {'sha256': row['sha256'], 'bytes': row['bytes']})


def old_pair_memberships(spec, keys):
    base, number, role = Path(spec['package']['root']), spec['paper_number'], spec['role']
    conf = obj(base / 'CONFIGURATION_BEFORE.json')
    need(conf == obj(base / 'CONFIGURATION_AFTER.json'), 'Original pair complete configuration interval')
    if number == 208:
        for name, row in conf.items():
            current_state(name, row)
        runtime = obj(base / 'RUNTIME_INVENTORY_BEFORE.json')
        membership('P208 pair runtime', lambda: keys.runtime_names(208), set(runtime))
        membership('P208 pair configurations', lambda: keys.config_names(208, False, role), set(conf))
        for i in (1, 2): absent(base / ('run' + str(i) + '_unused_pycache'))
    else:
        for name, row in conf['optional'].items(): current_state(name, row)
        membership('P209 pair configurations', lambda: keys.config_names(209, False), set(conf['optional']))
        for name, rows in conf['directories'].items():
            directory = Path(name)
            membership('P209 recorded configuration directory ' + name,
                       lambda p=directory: sorted(keys.files_under((p,))) if p.is_dir() else None, rows)
        discovery = obj(base / 'INTERPRETER_CONFIGURATION.json')
        need(discovery['sysconfig_paths'] == sysconfig.get_paths() and
             discovery['sysconfig_vars'] == decode(json.dumps(sysconfig.get_config_vars()).encode()),
             'Recorded exact interpreter configuration')
        early = obj(base / 'PARENT_BEFORE.json'); extra = set(early['mapped_files'])
        for row in early['modules'].values():
            extra.update(p for p in (row.get('file'), row.get('origin')) if p and p.startswith('/') and p != spec['recorder_source'])
        def names():
            return keys.runtime_names(209) | {p for p, row in conf['optional'].items() if 'sha256' in row} | \
                set().union(*(keys.files_under((Path(d),)) for d in conf['directories'])) | extra
        membership('P209 complete pair runtime', names, set(obj(base / 'RUNTIME_BEFORE.json')))
        absent(base / 'never_created_parent_cache')
        absent(Path(spec['launcher']['root']) / 'never_created_launcher_cache')
        for i in (1, 2): absent(base / ('replay_0' + str(i) + '/never_created_child_cache'))


def reuse_208_209(contract, keys, root_reception):
    fixed = obj(contract['reuse_inputs'])
    package(contract['reuse_output_package'])
    native = obj(contract['reuse_native'])
    result = obj(contract['reuse_result'])
    need(native['native']['exit'] == 0 and not native['failures'] and
         result['status'] == 'PASS_CURRENT_KEYS_REUSED_NOT_NEW_EXECUTIONS_OR_BATCH_ACCEPTANCE' and
         result['checks'] == 3988646 and result['current_paths_reread'] == 136582,
         'Actual passing current-key result, not new science or acceptance')
    pin(root_reception['native'], root_reception['native_pin'])
    receipt = obj(root_reception['native'])
    # The root binding is supplied only after its actual completed receiver.
    for key in root_reception['native_exit_selector']:
        receipt = receipt[key]
    need(receipt == 0, 'Actual root reuse-original reception exit')
    pin(root_reception['report'], root_reception['report_pin'])
    need(root_reception['accepted_status'] in raw(root_reception['report']).decode(), 'Root explicit accepted reception report')
    for spec in fixed['accepted_packages']: package(spec)
    for path, expected in fixed['fixed_inputs'].items(): pin(path, expected)
    for row in result['original_ledger_references']:
        cases = []
        for case, spec in {**fixed['pairs'], **fixed['builds']}.items():
            roots = [spec['package']['root']]
            if 'launcher' in spec: roots.append(spec['launcher']['root'])
            if any(Path(row['before']).is_relative_to(Path(root)) for root in roots): cases.append(case)
        need(len(cases) == 1, 'Exactly one original reuse ledger case', row['before'])
        interval(row['before'], row['after'], cases[0], row['entries'])
    need(len(result['original_ledger_references']) == 40 and len(fixed['pairs']) == 6 and len(fixed['builds']) == 2,
         'Exactly six reusable pairs/four builds and all forty named key intervals')
    for spec in fixed['pairs'].values():
        package(spec['package']); old_pair_memberships(spec, keys)
    for spec in fixed['builds'].values():
        base, number = Path(spec['package']['root']), spec['paper_number']
        package(spec['package'])
        conf = obj(base / 'CONFIGURATION_BEFORE.json')
        need(conf == obj(base / 'CONFIGURATION_AFTER.json'), 'Original build configuration interval')
        for name, row in conf.items(): current_state(name, row)
        membership('P208/P209 build runtime', lambda n=number: keys.runtime_names(n, True), set(obj(base / 'RUNTIME_BEFORE.json')))
        membership('P208/P209 build configuration', lambda n=number: keys.config_names(n, True), set(conf))
        membership('P208/P209 build TeX', lambda n=number: keys.files_under(keys.TEX208 if n == 208 else keys.TEX209, True),
                   set(obj(base / 'TEX_INVENTORY_BEFORE.json')))
        for name, row in obj(base / 'USER_ROOTS_AFTER.json').items():
            need(row['exists'] is False, 'Recorded absent user TeX root', name); absent(row['resolved'])
        absent('/tmp/p208-terminal-v2-actual-unused-20260906' if number == 208 else base / 'never_created_parent_cache')
        view = obj(spec['view_record'])
        need(view['reviewer'] == '/root' and view['open_visual_findings'] == 0 and
             view['terminal_manifest_sha256'] == spec['package']['manifest']['sha256'] and
             view['pdf_sha256'] == spec['pdf']['sha256'] and
             [p['page'] for p in view['pages']] == list(range(1, spec['pages'] + 1)), 'Actual P208/P209 every-final-page bindings')
        for row in view['pages']:
            need(row['actually_displayed_and_viewed'] is True and row['observation'].strip(), 'Actual frame attestation')
            pin(row['path'], row['sha256'])
        for number in (1, 2):
            cold = base / ('cold_build_' + str(number))
            for name, value in spec['source_pins'].items(): pin(cold / name, value)
            pin(cold / 'main.pdf', spec['pdf']); equal(cold / 'main.pdf', Path(spec['paper']) / 'main.pdf')


def local_targets(data, modern=False):
    result = []
    content = data.decode()
    if modern:
        # Exact accepted P208/P209 parser: code is not Markdown links. This
        # is not a missing-destination exemption or a changed old parser.
        content = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', content)
        content = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', content)
        content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
    for value in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        target = (value.strip() if modern else value).strip('<>').split('#', 1)[0]
        if target and not re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target): result.append(target)
    return result


def p209_frozen_link_roles(base, result):
    """Receive the exact typed link map, not a document-origin pathname.

    The accepted P209 auditor first selected a frozen (document, href) row,
    then applied its recorded exact (absolute path, digest) alias. These are
    per-link physical roles only: no global input/runtime alias is added.
    """
    need(base == ROOT / 'papers/209-ordered-fibre-threading' and
         result['paper'] == 'P209' and result['status'] == 'PASS_P209_TERMINAL_ARTIFACT_GATE',
         'Typed frozen links only from the accepted P209 initial artifact')
    aliases = result['explicit_historical_aliases_used']
    need(len(aliases) == 94, 'Exact original P209 recorded alias-table census')
    census, roles = Counter(), {}
    for number, count in ((0, 243), (1, 259), (2, 298)):
        frozen = base / ('frozen_round' + str(number))
        meta = obj(frozen / ('FROZEN_LINK_MAP.json' if number == 0 else
                             'ROUND' + str(number) + '_PROVENANCE.json'))
        rows = meta['links'] if number == 0 else (
            meta['round1_core_link_map' if number == 1 else 'round2_historical_link_map'] +
            meta['acceptance_and_historical_anchor_link_map'])
        need(len(rows) == count, 'All original frozen link-map occurrences', number)
        for row in rows:
            relative, href = Path(row['document']), row['href']
            need(relative.parts and not relative.is_absolute() and '..' not in relative.parts and
                 relative.as_posix() == row['document'] and
                 href == href.strip().strip('<>').split('#', 1)[0],
                 'Exact P209 frozen document/href grammar', row['document'])
            document, digest = str(frozen / relative), row['sha256']
            original = str(absolute(row['physical_target']))
            target = str(absolute(aliases.get(original + ' @ ' + digest, original)))
            need(Path(target).is_relative_to(ROOT), 'Recorded frozen physical target remains in workspace', target)
            role = roles.setdefault(document, {'kind': 'p209-explicit-frozen-link-map',
                                                'links': {}, 'occurrences': Counter()})
            value = {'physical_target': target, 'sha256': digest}
            need(href not in role['links'] or role['links'][href] == value,
                 'Duplicate frozen href must retain identical physical role', (document, href))
            role['links'][href] = value
            role['occurrences'][href] += 1
            census[(document, href, target, digest)] += 1
    recorded = Counter((str(absolute(row['document'])), row['target'],
                        str(absolute(row['resolved_target'])), row['sha256'])
                       for row in result['all_local_links_checked']
                       if row.get('semantic_origin') == 'explicit-frozen-link-map')
    need(recorded == census and sum(census.values()) == 800 and len(census) == 779 and len(roles) == 71,
         'All exact map/recorded-alias/accepted-link-row occurrences agree')
    return roles


def links_from_document(document, origin, expected=None, historical=False, modern=False):
    global LINK_COUNT
    data = raw(document, expected, historical)
    targets = local_targets(data, modern)
    if isinstance(origin, dict):
        need(modern and origin['kind'] == 'p209-explicit-frozen-link-map' and
             Counter(targets) == origin['occurrences'], 'Entire explicit frozen document link census', str(document))
        for target in targets:
            row = origin['links'][target]
            pin(row['physical_target'], row['sha256'])
            LINK_COUNT += 1
        return
    for target in targets:
        destination = (absolute(origin).parent / target).resolve()
        need(destination.exists(), 'Unclosed exact-origin local link', (str(document), str(origin), target))
        if destination.is_file(): pin(destination)
        else:
            need(destination.is_dir(), 'Link is a regular file or directory')
            current_state(destination, {'exists': True, 'is_dir': True, 'resolved': str(destination)})
        LINK_COUNT += 1


def lifecycle_keys_and_links(contract):
    """Reuse already passing artifact predicates only under all current keys.

    Original link-origin rows are read as data; no old auditor is run against
    the changed lifecycle.  Initial and current old-status aliases remain
    separate records.  Physical package closure above preserves every failed
    artifact and initial review without making it a current open finding.
    """
    for p in contract['papers']:
        ident, base = p['id'], absolute(p['paper'])
        modern = ident in ('P208', 'P209')
        origins = {}
        for role in p['artifact_keys']:
            result = obj(role['output'])
            need(result['status'] == role['status'], 'Actual prior passing artifact result', ident)
            if role.get('ledger_field'):
                ledger = result[role['ledger_field']]
                need(len(ledger) == role['entries'], 'Full accepted documentary dependency ledger', ident)
                for name, expected in ledger.items(): pin(name, expected, role['case'])
            else: ledger = {}
            if role.get('resolutions_field'):
                for name, target in result[role['resolutions_field']].items():
                    need(str(absolute(name).resolve()) == target, 'Original host resolution key', name)
            declared_manifests = result.get('validated_manifests', result.get('complete_manifests_validated', []))
            for row in declared_manifests:
                if not row['complete_nonself']:
                    continue
                seal = absolute(row['path']) if 'path' in row else absolute(row['base']) / row['name']
                digest = row.get('sha256')
                if digest is None:
                    key = str(seal.relative_to(ROOT)) if str(seal) not in ledger else str(seal)
                    need(key in ledger, 'Original complete manifest has a recorded ledger pin', str(seal))
                    digest = ledger[key]['sha256']
                manifest({'path': str(seal), 'base': row['base'], 'sha256': digest,
                          'payload_rows': row['entries']}, role['case'])
            rows = result
            for key in role.get('links_selector', []): rows = rows[key]
            if not role.get('links_selector'): rows = []
            frozen_roles = p209_frozen_link_roles(base, result) if ident == 'P209' and role['case'] == 'artifact_p209_initial' else {}
            for row in rows:
                document = absolute(row['document'])
                if row.get('semantic_origin') == 'explicit-frozen-link-map':
                    need(str(document) in frozen_roles, 'No unbound or cross-paper typed frozen-link role', str(document))
                    origin = frozen_roles[str(document)]
                else:
                    origin = absolute(row.get('semantic_origin', row['document']))
                need(str(document) not in origins or origins[str(document)] == origin, 'Unambiguous exact logical Markdown origin', str(document))
                origins[str(document)] = origin
            # Inspect every distinct original linked document at its original
            # hash where given; the only substitutions are explicit old roles.
            for document in {absolute(r['document']) for r in rows}:
                expected = ledger.get(str(document), ledger.get(str(document.relative_to(ROOT)))) if document.is_relative_to(ROOT) else ledger.get(str(document))
                links_from_document(document, origins[str(document)], expected, role['case'] if expected is not None else False, modern)
        for folder in (base, *(absolute(r['accepted_delta']).parent for r in p['accepted_reviews'])):
            for document in folder.rglob('*.md'):
                if ident == 'P205':
                    origin = Path(re.sub(r'/frozen_round[012]/', '/', str(document)))
                else:
                    need(str(document) in origins or not local_targets(raw(document), modern),
                         'No guessed Markdown origin for newly linked document', str(document))
                    origin = origins.get(str(document), document)
                links_from_document(document, origin, modern=modern)


def verify_four(root_reception):
    contract = obj(HERE / 'FOUR_INPUTS.json')
    for path, value in contract['fixed_inputs'].items(): pin(path, value)
    for row in contract['aliases']: bind_alias(row)
    theorem_ceilings(contract)
    provenance = obj(HERE / 'KEY_SELECTOR_PROVENANCE.json')
    for path, value in obj(HERE / 'LINK_PARSER_PROVENANCE.json')['sources'].items(): pin(path, value)
    strict = read_selector('strict_key_selectors.py', provenance)
    builds = read_selector('four_build_key_selectors.py', provenance)
    reuse = read_selector('reuse_key_selectors.py', provenance)
    completion_artifacts(contract)
    supplemental_pairs(contract, strict)
    supplemental_builds(contract, builds)
    reuse_208_209(contract, reuse, root_reception)
    lifecycle_keys_and_links(contract)
    for label, function, expected in MEMBERSHIPS:
        need(function() == expected, 'Final resource membership reread', label)
    for (path, schema), value in list(STATES.items()): current_state(path, value)
    for path in list(TREES): physical(path)
    before = dict(READS)
    for path, value in before.items(): need(measured(path) == value, 'Final uncached complete file-key reread', path)
    return {'status': 'FOUR_COMPLETED_COMPONENT_PASS_P210_NOT_ASSESSED_NOT_FIVE_PAPER_PASS',
            'papers_checked': list(IDS), 'prior_completed_papers': 4,
            'required_final_five': [*IDS, 'P210'], 'p210_accepted_by_this_component': False,
            'current_valid_author_A_B_pairs': 12, 'current_valid_source_only_builds': 8,
            'actual_prior_page_attestations_bound': 21, 'five_contract_ceilings_checked': 5,
            'checks': CHECKS, 'current_file_keys_reread': len(before),
            'current_file_key_sha256': hashlib.sha256((json.dumps(before, sort_keys=True, separators=(',', ':')) + '\n').encode()).hexdigest(),
            'documentary_aliases_used': USED_ALIASES, 'local_links_checked': LINK_COUNT,
            'complete_raw_comparisons_read_only': RAW_PAIRS,
            'new_scientific_executions': 0, 'new_builds': 0, 'new_page_views': 0, 'new_reviews': 0,
            'old_auditors_or_writers_executed': 0, 'files_written': 0,
            'supersession': 'P205/P207 old weak runtime/build reuse keys remain historical; six strict pairs/four source-only builds are separately accepted supplements, not retroactive upgrades.',
            'boundary': 'Prior accepted theorem/review/command predicates are received under complete named unchanged keys. Known inventories and recorded samples are not continuous tracing, new proof or new viewing.',
            'owner': 'OWNER_AMBER', 'external': 'HOLD_EXTERNAL'}


def reconstruct_four():
    """Execute copied predicates in this new module, not the old entry point.

    The driver must measure its own files in a separate map before this
    call. No new preparation/native file enters the historical READS map.
    """
    global HISTORICAL_FOUR_PHASE
    need(not READS and not STATES and not TREES and not ALIASES and not MEMBERSHIPS and
         HISTORICAL_FOUR_PHASE is True, 'Single fresh historical four reconstruction')
    manifest({'path': str(HERE / 'SHA256SUMS'),
        'sha256': '3863616519c14cc2f70d92deced93d745978a34f7e90f78aed5f00dd12ca8238', 'payload_rows': 14})
    for path, expected in obj(HERE / 'REVISION_PROVENANCE.json')['inputs'].items():
        pin(path, expected)
    binding = obj(HERE / 'ROOT_REUSE_BINDING.json')
    need(binding['schema'] == 'actual-p208-p209-root-reuse-reception-binding-v1' and
         binding['not_a_placeholder'] is True, 'Original actual root reception binding remains required')
    result = verify_four(binding)
    need(result['current_file_keys_reread'] == len(READS) == 142784 and
         result['current_file_key_sha256'] ==
         '087b90f42ad1a55fef4daa2acb29cee4fca614736c862aa9aed5e2a65d628dc0',
         'Entire original 142784 rich-key sorted compact JSON plus LF digest, never count-only')
    original = dict(READS)
    need(original[str(FOUR_INDEX)] == FOUR_INDEX_KEY and str(FOUR_INDEX_COPY) not in original,
         'Old index original key retained until historical digest closes')
    HISTORICAL_FOUR_PHASE = False
    return result, original
