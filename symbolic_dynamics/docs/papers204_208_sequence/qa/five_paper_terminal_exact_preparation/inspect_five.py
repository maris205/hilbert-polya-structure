#!/usr/bin/env python3
"""Exact-five current-key gate; new read-only adapter, not a scientific run.

Reconstruct all original rich keys before three precisely typed historical
rebases. Reuse actual accepted command/review/build/view predicates only under
the complete merged current physical keys and source-defined memberships.
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
HERE = QA / 'five_paper_terminal_exact_preparation'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
HISTORY = QA / 'p210_precompletion_controls_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
CACHE = QA / 'five_paper_terminal_exact_run_01/never_created_reader_cache'
IDS = ['P205', 'P207', 'P208', 'P209', 'P210']
OWN, TREES, COUNTS = {}, {}, Counter()
PENDING = {
    str(PAPER / 'ROOT_LIFECYCLE.md'): {'sha256': 'e0b3bbd041d2fea0c66f8f11d113b8505a06463f0ea3bf629823746f403b7449', 'bytes': 4323},
    str(PAPER / 'PAPER_MANIFEST.sha256'): {'sha256': 'e821f92af0393af33308cce5667b24a93d183ed662a62b9232f25f15cb139ea2', 'bytes': 256888},
}
MODULE_NAMES = ('four_reconstruction', 'p210_reconstruction', 'p210_key_selectors', 'native_provenance')


def need(ok, rule, detail=None):
    COUNTS[rule] += 1
    if not ok:
        raise AssertionError((rule, detail))


def bytes_key(data):
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}


def canonical(value, terminal_lf=False):
    return bytes_key((json.dumps(value, sort_keys=True, separators=(',', ':')) +
                      ('\n' if terminal_lf else '')).encode())


def absolute(path):
    path = Path(path)
    return path if path.is_absolute() else ROOT / path


def rich_schema(row):
    need(set(row) == {'real', 'sha256', 'size', 'symlink'} and
         type(row['real']) is str and Path(row['real']).is_absolute() and
         type(row['size']) is int and row['size'] >= 0 and
         type(row['sha256']) is str and re.fullmatch('[0-9a-f]{64}', row['sha256']) and
         (row['symlink'] is None or type(row['symlink']) is str), 'complete rich file-key schema')


def file_key(path):
    p = absolute(path)
    need(p.is_file(), 'current regular file exists', str(p))
    if p.is_relative_to(ROOT):
        need(not p.is_symlink() and p.resolve() == p, 'physical workspace file without redirects', str(p))
    h, size = hashlib.sha256(), 0
    with p.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
            size += len(block)
    return dict(real=str(p.resolve()), sha256=h.hexdigest(), size=size,
                symlink=os.readlink(p) if p.is_symlink() else None)


def pin(path, expected=None):
    name = str(absolute(path))
    if name not in OWN:
        OWN[name] = file_key(name)
    value = OWN[name]
    if expected is not None:
        expected = {'sha256': expected} if type(expected) is str else expected
        for key, item in expected.items():
            target = {'bytes': 'size', 'resolved': 'real'}.get(key, key)
            need(target in value and value[target] == item, 'expected complete named input field', (name, key))
    return value


def byte_pin(path):
    value = pin(path)
    return {'sha256': value['sha256'], 'bytes': value['size']}


def historical_byte_pin(path, expected):
    name = str(absolute(path))
    if name in PENDING and expected == PENDING[name]:
        return pin(HISTORY / Path(name).name, expected)
    return pin(path, expected)


def raw(path):
    value = pin(path)
    data = absolute(path).read_bytes()
    need(bytes_key(data) == {'sha256': value['sha256'], 'bytes': value['size']},
         'full raw read stable', str(path))
    return data


def decode(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            need(key not in result, 'unique original JSON fields', key)
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=unique)


def obj(path):
    data = raw(path)
    return decode(gzip.decompress(data) if str(path).endswith('.gz') else data)


def physical(base):
    base = absolute(base)
    entries = list(base.rglob('*'))
    need(base.is_dir() and base.resolve() == base and all(not p.is_symlink() for p in entries),
         'physical package no symlink redirection', str(base))
    names = {p.relative_to(base).as_posix() for p in entries if p.is_file()}
    need(str(base) not in TREES or names == TREES[str(base)], 'complete named-package membership stable', str(base))
    TREES[str(base)] = names
    return names


def manifest_rows(path):
    data = raw(path)
    need(data.endswith(b'\n'), 'nonself manifest terminal LF', str(path))
    rows = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'strict two-space manifest row', str(path))
        digest, name = match.groups()
        p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and p.as_posix() == name
             and name not in rows, 'unique bounded manifest member', name)
        rows[name] = digest
    return rows


def manifest(base, seal_name='SHA256SUMS', expected=None):
    base = absolute(base)
    seal = base / seal_name
    if expected is not None:
        pin(seal, expected)
    rows = manifest_rows(seal)
    need(seal_name not in rows and set(rows) == physical(base) - {seal_name},
         'entire nonself package exact membership', str(base))
    for name, value in rows.items():
        pin(base / name, value)
    return rows


def load_module(name):
    need(name in MODULE_NAMES and name not in sys.modules, 'only fresh disclosed adapter module')
    path = HERE / (name + '.py')
    pin(path)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def source_provenance():
    record = obj(HERE / 'SOURCE_PROVENANCE.json')
    for name, spec in record['source_excerpts'].items():
        old = raw(spec['original_source']).decode()
        new = raw(HERE / name).decode()
        def nodes(text):
            result = {}
            for node in ast.parse(text).body:
                key = node.name if isinstance(node, (ast.FunctionDef, ast.ClassDef)) else (
                    node.targets[0].id if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) else None)
                if key:
                    result[key] = ast.get_source_segment(text, node)
            return result
        original_nodes, current_nodes = nodes(old), nodes(new)
        pin(spec['original_source'], spec['original_pin'])
        need(all(original_nodes[key] == current_nodes[key] for key in spec['unchanged_nodes']),
             'every disclosed unchanged function/selector is literal original source', name)
        excerpt = '\n\n'.join(original_nodes[key] for key in spec['unchanged_nodes']) + '\n'
        need(bytes_key(excerpt.encode()) == spec['unchanged_excerpt'],
             'entire selected source excerpt canonical bytes', name)
    return record


def invocation():
    need(Path(__file__) == HERE / 'inspect_five.py' and Path.cwd() == ROOT and
         dict(os.environ) == ENV and sys.executable == '/usr/bin/python3.10' and
         sys.flags.isolated == sys.flags.no_site == 1 and sys.dont_write_bytecode is True and
         sys.flags.optimize == 0 and sys.pycache_prefix == str(CACHE) and not os.path.lexists(CACHE) and
         sys.path == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'] and
         sys.argv == [str(HERE / 'inspect_five.py'), '--expected-preparation-sha256', sys.argv[2]],
         'exact system-only isolated read-only driver invocation')
    need(re.fullmatch('[0-9a-f]{64}', sys.argv[2]) is not None, 'explicit expected preparation seal')
    return dict(executable=sys.executable, argv=list(sys.argv), environment=dict(os.environ),
                cwd=str(Path.cwd()), module_search_path=list(sys.path), cache=str(CACHE),
                cache_absent=True, isolated=1, no_site=1, no_bytecode=True, optimize=0)


def runtime():
    modules = {}
    allowed = {HERE / 'inspect_five.py', *(HERE / (name + '.py') for name in MODULE_NAMES)}
    for name, module in sorted(sys.modules.items()):
        path = getattr(module, '__file__', None)
        if path and Path(path).is_absolute():
            p = Path(path)
            need(p in allowed or p.is_relative_to('/usr/lib/python3.10'),
                 'only new disclosed project modules and system stdlib', (name, path))
            modules[name] = {'path': str(p), **pin(p)}
    maps = Path('/proc/self/maps').read_text()
    files = {}
    for line in maps.splitlines():
        fields = line.split(maxsplit=5)
        if len(fields) == 6 and fields[5].startswith('/'):
            need(not fields[5].endswith(' (deleted)'), 'no deleted mapped file')
            files[fields[5]] = pin(fields[5])
    return dict(modules=modules, mapped_files=files, raw_maps=maps,
                raw_maps_pin=bytes_key(maps.encode()))


def live_ceilings(four_contract):
    path = ROOT / four_contract['current_index']
    data = raw(path).decode()
    need('HOLD_EXTERNAL' in data and set(four_contract['five_ceilings']) == set(IDS),
         'current exact five retained theorem contracts and external hold')
    for ident, row in four_contract['five_ceilings'].items():
        need(data.count('## ' + ident + ' — ') == 1, 'one current section per retained paper', ident)
        section = data.split('## ' + ident + ' — ', 1)[1].split('\n## ', 1)[0]
        body = row['body_start'] + section.split(row['body_start'], 1)[1].split('\nPaper path:', 1)[0]
        need(bytes_key(body.encode()) == {k: row[k] for k in ('sha256', 'bytes')},
             'live mathematical ceiling and exclusions unchanged', ident)
    return {ident: {k: row[k] for k in ('sha256', 'bytes')} for ident, row in four_contract['five_ceilings'].items()}


def lifecycle(initial):
    accepted = obj(QA / 'P210_LIFECYCLE_ROOT_ACCEPTANCE.actual.json')
    need(accepted['schema'] == 'p210-root-final-lifecycle-acceptance-v1' and
         accepted['status'] == 'ROOT_ACCEPTED_P210_FINAL_LIFECYCLE_PAPER_COMPLETE' and
         accepted['paper_completion'] is True and accepted['five_paper_completion'] is False and
         accepted['root'] == '/root' and accepted['paper'] == 'P210' and
         accepted['root_original_inspection_complete'] is accepted['full_current_documentary_map_checked'] is True and
         accepted['native_session'] == 5316 and accepted['native_exit'] == 0 and
         accepted['root_reception_session'] == 93071 and accepted['root_reception_exit'] == 0 and
         accepted['root_reception_checks'] == 35643 and accepted['root_direct_paths'] == 2328 and
         accepted['whole_payloads'] == 2244 and accepted['changed_payloads'] == ['ROOT_LIFECYCLE.md'] and
         accepted['all_scientific_frozen_review_terminal_bytes_unchanged'] is True and
         accepted['external'] == 'OWNER_AMBER / HOLD_EXTERNAL', 'actual final P210 root acceptance exact scope')
    for name, value in accepted['input_pins'].items():
        pin(name, value)
    report = obj(QA / 'p210_terminal_lifecycle_01/LIFECYCLE_REPORT.json')
    need(report['schema'] == 'p210-document-only-lifecycle-followup-v1' and
         report['status'] == 'PASS_P210_DOCUMENT_ONLY_LIFECYCLE_FOLLOWUP_ROOT_ACCEPTANCE_PENDING' and
         report['checks'] == sum(report['checks_by_kind'].values()) == accepted['lifecycle_gate_checks'] == 28659 and
         report['root_acceptance'] is report['paper_completion'] is report['five_paper_completion'] is False and
         all(report[k] == 0 for k in ('new_scientific_runs', 'new_builds', 'new_views',
             'new_manuscript_reviews', 'old_programs_imported_or_executed', 'reader_file_writes')),
         'actual lifecycle result does not self-accept')
    full = report['complete_current_read_keys']
    need(len(full) == report['current_path_keys'] == accepted['current_documentary_keys'] == 2319 and
         canonical(full) == accepted['complete_current_read_map'], 'entire actual lifecycle rich map')
    for row in full.values():
        rich_schema(row)
    roles = report['exact_two_historical_control_roles']
    need(len(roles) == 2 and {r['original_path'] for r in roles} == set(PENDING),
         'exact two and only two P210 documentary rebases')
    rebased, aliases = dict(initial), []
    for row in roles:
        name, target = row['original_path'], row['physical_path']
        old = dict(real=name, sha256=row['sha256'], size=row['bytes'], symlink=None)
        need({k: row[k] for k in ('sha256', 'bytes')} == PENDING[name] and
             target == str(HISTORY / Path(name).name) and rebased.pop(name) == old,
             'old initial rich metadata before precise physical rebase', name)
        physical_row = pin(target, PENDING[name])
        need(target not in rebased or rebased[target] == physical_row, 'historical physical collision equality')
        rebased[target] = physical_row
        aliases.append(dict(logical=name, original=old, physical=target, physical_record=physical_row,
                            provenance=str(QA / 'p210_terminal_lifecycle_01/LIFECYCLE_REPORT.json')))
    manifest(HISTORY, expected='3c4438ff263d1bb5f780a5799ccd0338b721e8a331aa644c3ab5196257b4c480')
    old_whole = manifest_rows(HISTORY / 'PAPER_MANIFEST.sha256')
    current = manifest(PAPER, 'PAPER_MANIFEST.sha256', accepted['input_pins'][str(PAPER / 'PAPER_MANIFEST.sha256')])
    need(len(current) == len(old_whole) == 2244 and set(current) == set(old_whole) and
         [name for name in sorted(current) if current[name] != old_whole[name]] == ['ROOT_LIFECYCLE.md'],
         'entire 2244-row sole lifecycle transition unchanged science')
    transition = report['document_only_transition']
    need(transition['old_lifecycle'] == PENDING[str(PAPER / 'ROOT_LIFECYCLE.md')] and
         transition['old_whole_manifest'] == PENDING[str(PAPER / 'PAPER_MANIFEST.sha256')] and
         transition['current_lifecycle'] == byte_pin(PAPER / 'ROOT_LIFECYCLE.md') and
         transition['current_whole_manifest'] == byte_pin(PAPER / 'PAPER_MANIFEST.sha256'),
         'both exact old and current document values bound')
    return rebased, full, aliases, accepted


def p210_memberships(selectors, report, ledger, nonfiles):
    selectors.need = selectors.ck = need
    selectors.raw, selectors.val = raw, byte_pin
    cases = []
    for label in ('produce01', 'pair01', 'build01', 'build02'):
        directory = QA.parent / 'reviews/p210_b' / label
        before = obj(directory / 'INPUTS_BEFORE.json.gz')
        if label != 'build01':
            need(before == obj(directory / 'INPUTS_AFTER.json.gz'), 'entire actual B membership interval', label)
        cases.append((label, before, label.startswith('build')))
    resources, configuration = None, None
    for role in ('author', 'a', 'b'):
        directory = QA / 'root_replays' / ('p210_' + role + '_strict_pair_01')
        names = obj(directory / 'RESOURCE_NAMES_BEFORE.json')
        conf = obj(directory / 'CONFIGURATION_BEFORE.json')
        need(names == obj(directory / 'RESOURCE_NAMES_AFTER.json') and
             conf == obj(directory / 'CONFIGURATION_AFTER.json') and len(names) == len(set(names)) == 3121 and
             len(conf) == 41, 'entire original strict resource/configuration interval', role)
        need(resources is None or (names == resources and conf == configuration),
             'all three strict scopes agree in full values')
        resources, configuration = names, conf

    def check():
        scopes = {label: selectors.current_membership(value, build) for label, value, build in cases}
        need(scopes == report['actual_B_full_reuse']['current_membership_scopes'],
             'all four exact B source membership scopes')
        need(selectors.current_resources() == resources and selectors.configuration_snapshot() == configuration,
             'all three complete source-defined strict resource and configuration memberships')
        groups = selectors.terminal_membership(ledger)
        need(groups == report['actual_terminal_reused']['known_groups'],
             'entire source-defined terminal groups including absent fixed children')
        for name, row in nonfiles.items():
            need(selectors.terminal_entry(name) == row, 'all initial nonfile presence/link fields current', name)
        return dict(B=scopes, strict=dict(resources=len(resources), configuration=len(configuration),
                    roles=['author', 'a', 'b']), terminal=groups, nonfile_presence_roles=len(nonfiles))
    return check


def p210_reuse(report, accepted):
    reviews = report['accepted_reviews']
    need(set(reviews) == {'a', 'b'} and all(reviews[k]['current_open'] == 0 for k in reviews) and
         reviews['a']['reviewer'] == '/root/p210_a_reviewer' and
         reviews['b']['reviewer'] == '/root/p210_b_reviewer', 'actual distinct accepted P210 manuscript roles')
    pairs = report['actual_strict_pairs_reused']
    need([(r['role'], r['checks_each'], r['known_keys']) for r in pairs] ==
         [('author', [197471, 197471], 3639), ('a', [133978, 133978], 3634), ('b', [51129, 51129], 3558)] and
         all(r['new_science_runs'] == 0 and
             r['reuse'] == 'PREVIOUS_ACTUAL_ROOT_PAIR_REUSED_UNDER_COMPLETE_CURRENT_KEYS' for r in pairs),
         'three original P210 strict pairs reused not rerun')
    for row in pairs:
        manifest(QA / 'root_replays' / ('p210_' + row['role'] + '_strict_pair_01'), expected=row['pair_manifest'])
    for role, count in (('a', 552), ('b', 441)):
        rows = manifest(QA.parent / 'reviews' / ('p210_' + role))
        need(len(rows) == reviews[role]['final_payloads'] == count, 'entire accepted review package', role)
    term = report['actual_terminal_reused']
    need(term['reused_terminal_builds'] == 2 and len(term['measured']) == 2 and
         all(r['pages'] == 6 for r in term['measured']) and
         term['new_builds'] == term['new_views'] == 0 and
         report['actual_root_terminal_and_view_binding']['terminal_builds_and_views_accepted'] is True and
         report['actual_root_terminal_and_view_binding']['actual_six_root_views']['pages_actually_viewed_by_root'] == 6 and
         accepted['paper_completion'] is True, 'two actual terminal builds and six actual prior views under current keys')
    need(len(manifest(PAPER / 'qa_final')) == term['output_payloads'] == 222, 'entire original terminal package')


def merge(*groups):
    result = {}
    for group in groups:
        for name, row in group.items():
            need(Path(name).is_absolute(), 'absolute lexical rich key', name)
            rich_schema(row)
            need(name not in result or result[name] == row, 'full-field overlapping physical keys agree', name)
            result[name] = row
    return result


def main():
    start_invocation = invocation()
    manifest(HERE, expected=sys.argv[2])
    binding = obj(HERE / 'ACTUAL_BINDING.json')
    need(binding['schema'] == 'actual-exact-five-preparation-binding-v1' and binding['not_a_placeholder'] is True and
         binding['retained_papers'] == IDS and binding['root_acceptance'] is False and
         binding['five_paper_completion'] is False and binding['external'] == 'OWNER_AMBER / HOLD_EXTERNAL',
         'actual source-only preparation binding no premature acceptance')
    native = load_module('native_provenance')
    native_result = native.verify(sys.modules[__name__], binding)
    # Native normal closures precede adoption of corresponding package bytes.
    for name, expected in binding['fixed_inputs'].items():
        pin(name, expected)
    source_provenance()
    initial_accept = obj(QA / 'P210_ARTIFACT_ROOT_ACCEPTANCE.actual.json')
    need(initial_accept['status'] == 'ROOT_ACCEPTED_P210_INITIAL_ARTIFACT_LIFECYCLE_FOLLOWUP_PENDING' and
         initial_accept['root_original_inspection_complete'] is initial_accept['complete_current_map_reconstructed'] is True and
         initial_accept['current_file_keys'] == 122149 and initial_accept['root'] == '/root' and
         initial_accept['paper_completion'] is initial_accept['five_paper_completion'] is False,
         'actual initial P210 root acceptance still bounded')
    for name, expected in initial_accept['input_pins'].items():
        historical_byte_pin(name, expected)
    four = load_module('four_reconstruction')
    p210 = load_module('p210_reconstruction')
    selectors = load_module('p210_key_selectors')
    contract = obj(four.HERE / 'FOUR_INPUTS.json')
    ceilings = live_ceilings(contract)
    four_result, four_original = four.reconstruct_four()
    four_current = {name: dict(real=row['resolved'], sha256=row['sha256'], size=row['bytes'], symlink=row['symlink'])
                    for name, row in four_original.items()}
    original = four_current.pop(str(four.FOUR_INDEX))
    physical_row = pin(four.FOUR_INDEX_COPY, four.FOUR_INDEX_KEY['sha256'])
    need(original == dict(real=str(four.FOUR_INDEX), sha256=four.FOUR_INDEX_KEY['sha256'], size=28714, symlink=None) and
         str(four.FOUR_INDEX_COPY) not in four_current, 'four exact index rebase only after whole original digest')
    four_current[str(four.FOUR_INDEX_COPY)] = physical_row
    four_alias = dict(logical=str(four.FOUR_INDEX), original=original,
        physical=str(four.FOUR_INDEX_COPY), physical_record=physical_row,
        provenance=str(QA / 'central_round2_p210/README.md'))
    initial, nonfiles, p210_report, terminal_ledger, p210_recipe = p210.reconstruct(sys.modules[__name__])
    p210_current, lifecycle_keys, p210_aliases, final_accept = lifecycle(initial)
    p210_reuse(p210_report, final_accept)
    scope_check = p210_memberships(selectors, p210_report, terminal_ledger, nonfiles)
    memberships_before = scope_check()
    runtime_before = runtime()
    # All imports and membership callbacks are finished before freezing OWN.
    base = merge(four_current, p210_current, lifecycle_keys)
    own_before = dict(OWN)
    extra = {name: row for name, row in own_before.items() if name not in base}
    merged = merge(base, own_before)
    for phase in (1, 2):
        for name, expected in merged.items():
            need(file_key(name) == expected, 'merged uncached whole rich key reread ' + str(phase), name)
        if phase == 1:
            need(scope_check() == memberships_before, 'P210 full membership reread between content passes')
            for label, function, expected in four.MEMBERSHIPS:
                four.need(function() == expected, 'Exact-five final copied four resource membership', label)
            for (path, schema), value in list(four.STATES.items()):
                four.current_state(path, value)
            for path in list(four.TREES):
                four.physical(path)
            for path in list(TREES):
                physical(path)
    need(scope_check() == memberships_before, 'P210 final exact memberships after second content pass')
    for label, function, expected in four.MEMBERSHIPS:
        four.need(function() == expected, 'Final copied source-defined membership after both reads', label)
    for (path, schema), value in list(four.STATES.items()):
        four.current_state(path, value)
    for path in list(four.TREES):
        four.physical(path)
    for path in list(TREES):
        physical(path)
    runtime_after = runtime()
    need(runtime_after['modules'] == runtime_before['modules'] and
         runtime_after['mapped_files'] == runtime_before['mapped_files'] and OWN == own_before and
         four.READS == four_original and invocation() == start_invocation and live_ceilings(contract) == ceilings,
         'no new unbound imports/keys or changed current invocation/contracts')
    result = dict(schema='exact-five-current-rich-key-gate-v1',
        status='PASS_EXACT_FIVE_GATE_ROOT_ACCEPTANCE_PENDING', papers=IDS,
        retained_papers=5, individually_root_accepted_papers=5, current_open_findings=0,
        reused_strict_author_A_B_pairs=15, reused_terminal_source_only_builds=10,
        reused_actual_prior_root_page_views=27, current_live_theorem_ceilings=ceilings,
        root_acceptance=False, five_paper_completion=False, external='OWNER_AMBER / HOLD_EXTERNAL',
        new_scientific_runs=0, new_builds=0, new_views=0, new_manuscript_reviews=0,
        old_auditors_or_writers_imported_or_executed=0, reader_file_writes=0,
        checks=sum(COUNTS.values()) + four.CHECKS, new_driver_checks=sum(COUNTS.values()),
        new_driver_checks_by_kind=dict(sorted(COUNTS.items())), copied_four_checks=four.CHECKS,
        complete_current_file_keys=len(merged), complete_current_file_map=canonical(merged),
        complete_current_read_keys=merged,
        complete_current_rich_file_reads=2, native_originals=native_result,
        source_defined_P210_memberships=memberships_before,
        copied_four_membership_scopes=len(four.MEMBERSHIPS), copied_four_presence_schemas=len(four.STATES),
        copied_four_named_packages=len(four.TREES), additional_named_packages=len(TREES),
        reconstructed_four_result=four_result, current_runtime_before=runtime_before, current_runtime_after=runtime_after,
        current_key_reconstruction=dict(
            canonical_encoding="json.dumps(map,sort_keys=True,separators=(',',':')).encode(); no terminal LF",
            rich_fields=['real', 'sha256', 'size', 'symlink'],
            original_four=dict(source=str(HERE / 'four_reconstruction.py'), source_pin=byte_pin(HERE / 'four_reconstruction.py'),
                operation='reconstruct_four()[1]', schema_conversion={'real':'resolved','size':'bytes','sha256':'sha256','symlink':'symlink'},
                original_keys=142784, original_compact_LF_sha256='087b90f42ad1a55fef4daa2acb29cee4fca614736c862aa9aed5e2a65d628dc0',
                exact_post_digest_rebase=four_alias, current_keys=len(four_current), current_map=canonical(four_current)),
            original_P210=p210_recipe, exact_post_initial_digest_P210_rebases=p210_aliases,
            rebased_P210_keys=len(p210_current), rebased_P210_map=canonical(p210_current),
            actual_lifecycle=dict(source=str(QA / 'p210_terminal_lifecycle_01/LIFECYCLE_REPORT.json'),
                source_pin=byte_pin(QA / 'p210_terminal_lifecycle_01/LIFECYCLE_REPORT.json'),
                selector=['complete_current_read_keys'], keys=len(lifecycle_keys), complete_map=canonical(lifecycle_keys)),
            merge_rule='union original four after exact rebase, complete initial P210 after two exact rebases, complete actual lifecycle map; overlapping lexical keys require every rich field equal; then disjoint extras',
            base_keys=len(base), base_map=canonical(base), extra_count=len(extra), extra_current_keys=extra,
            complete_keys=len(merged), complete_map=canonical(merged)),
        limitations=['No new mathematics, manuscript review, build or page viewing.',
            'All original failures and historical missing/tracing/source/ownership limitations remain.',
            'Copied four predicates reproduce their entire original rich map before documentary rebasing.',
            'Known inventories and before/after samples are not continuous tracing.',
            'Actual root independent original reception and scoped private Git synchronization remain separate.'])
    output = json.dumps(result, sort_keys=True, separators=(',', ':'))
    if len(output.encode()) + 1 >= 100000000:
        raise AssertionError('Exact-five single complete output exceeds the bounded 100 MB artifact ceiling')
    print(output)


if __name__ == '__main__':
    try:
        main()
    except BaseException:
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
