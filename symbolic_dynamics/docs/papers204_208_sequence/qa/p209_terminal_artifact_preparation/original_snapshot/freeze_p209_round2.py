#!/usr/bin/env python3
"""Root-only physical P209 Round2 after actual accepted B/root closure.

Infrastructure adaptation of the preserved Round1 V2 freezer. No scientific
module is imported or executed. Existing source/provenance bytes stay exact;
new metadata describes the changed physical location and historical roles.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import traceback
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
ROUND0 = PAPER / 'frozen_round0'
ROUND1 = PAPER / 'frozen_round1'
TARGET = PAPER / 'frozen_round2'
PREPARATION = BATCH / 'qa/p209_round2_preparation'
B_PREPARATION = BATCH / 'qa/p209_b_root_preparation'
REVIEW = BATCH / 'reviews/p209_b'
RESPONSE = BATCH / 'P209_B_RESPONSE.md'
ACCEPTANCE = BATCH / 'qa/P209_B_ROOT_DELTA_INSPECTION.actual.json'
PAIR = BATCH / 'qa/root_replays/p209_b_strict/root_b_pair_01'
LAUNCHER = BATCH / 'qa/root_replays/p209_b_strict/launcher_root_b_pair_01'
AUTHOR_SEAL = '9fd20cd746f1ae03c22a87283313248ad79ffcfb9a0f1ea45458937dd5901a0e'
ROUND0_SEAL = '0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba'
ROUND1_SEAL = 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
PRIOR_WHOLE_SEAL = '3e94a72637733ca46f7950f4feb8508fdf14b5ff6386c971821932ae9231e5a9'
R1_FREEZER = '19cf0898e201f25dc5724233ff1cdef59d8a0001d6239fe5d15aeb9212f63c44'
B_INITIAL_SEAL = 'd88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea'
B_PREPARATION_SEAL = '4beef4a4e9f60c6039ceb89df1f3a12b2d61049ad75654e35825390c4b68133a'
B_RECORDER = '0629216719a87b20482911a55a77fcb9e3ce7e53bf774f139f6c147d6a014865'
B_LAUNCHER = '554e4c269a956ab8bbbd74664e4456563c43ff4265ad4b7897d3cc283343e991'
B_CANONICAL = '612e1463162deba868cf7cf81d61c8f017713f9b28c4c38b81b00d376bac992c'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
ANCHORS = {
    'ROUND1_CORE_MANIFEST.sha256': ROUND1 / 'SHA256SUMS',
    'B_REVIEW_MANIFEST.sha256': REVIEW / 'SHA256SUMS',
    'B_INITIAL_REVIEW_SEAL.sha256': REVIEW / 'INITIAL_REVIEW_SEAL.sha256',
    'B_DELTA.md': REVIEW / 'DELTA.md',
    'B_INITIAL_DELTA.md': REVIEW / 'INITIAL_DELTA.md',
    'B_INITIAL_FINDINGS.json': REVIEW / 'FINDINGS.json',
    'B_CURRENT_FINDINGS.json': REVIEW / 'CURRENT_FINDINGS.json',
    'B_INPUT_PINS.sha256': REVIEW / 'INPUT_PINS.sha256',
    'ROOT_RESPONSE.md': RESPONSE,
    'ROOT_INITIAL_INSPECTION.md': BATCH / 'qa/P209_B_ROOT_INITIAL_INSPECTION.md',
    'ROOT_DELTA_INSPECTION.md': BATCH / 'qa/P209_B_ROOT_DELTA_INSPECTION.md',
    'ROOT_DELTA_CLOSURE.actual.json': ACCEPTANCE,
    'ROOT_PAIR_MANIFEST.sha256': PAIR / 'SHA256SUMS',
    'ROOT_LAUNCHER_MANIFEST.sha256': LAUNCHER / 'SHA256SUMS',
    'PRE_ROUND2_PAPER_MANIFEST.sha256': PAPER / 'PAPER_MANIFEST.sha256',
}
READ_PINS = {}
COMPARISONS = []


def digest(path):
    path = Path(path)
    assert path.is_file() and not path.is_symlink(), 'not a regular nonsymlink file: ' + str(path)
    value = sha256(path.read_bytes()).hexdigest()
    name = str(path)
    assert name not in READ_PINS or READ_PINS[name] == value, 'input changed during freeze: ' + name
    READ_PINS[name] = value
    return value


def safe(name):
    path = Path(name)
    assert name and path.as_posix() == name and not path.is_absolute()
    assert '..' not in path.parts and '.' not in path.parts
    return path


def manifest_rows(path):
    digest(path)
    rows = {}
    for line in path.read_text().splitlines():
        value, name = line.split('  ', 1)
        assert re.fullmatch('[0-9a-f]{64}', value) and name not in rows
        safe(name)
        rows[name] = value
    return rows


def read_manifest(path, base):
    rows = manifest_rows(path)
    for name, value in rows.items():
        assert digest(base / safe(name)) == value, name
    return rows


def complete_manifest(base):
    rows = read_manifest(base / 'SHA256SUMS', base)
    entries = list(base.rglob('*'))
    assert 'SHA256SUMS' not in rows and all(not p.is_symlink() for p in entries)
    assert {p.relative_to(base).as_posix() for p in entries if p.is_file()} == set(rows) | {'SHA256SUMS'}
    return rows


def load(path):
    digest(path)
    return json.loads(path.read_bytes())


def raw_cmp(a, b):
    argv = ['/usr/bin/cmp', '--', str(a), str(b)]
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
           'started_epoch': time.time(), 'exit': None, 'outcome': 'PRE_SPAWN_ATTEMPT',
           'stdout': None, 'stderr': None}
    COMPARISONS.append(row)
    process = subprocess.run(argv, capture_output=True, check=False, cwd=ROOT, env=ENV)
    row.update(exit=process.returncode, outcome='COMPLETED',
               stdout=process.stdout.decode(), stderr=process.stderr.decode())
    assert process.returncode == 0, row


def core_inputs():
    assert digest(ROUND1 / 'SHA256SUMS') == ROUND1_SEAL
    core = complete_manifest(ROUND1)
    assert len(core) == 2003
    assert not any(part.startswith('frozen_round') for name in core for part in safe(name).parts)
    assert digest(ROUND0 / 'SHA256SUMS') == ROUND0_SEAL
    old_core = complete_manifest(ROUND0)
    assert len(old_core) == 1989 and all(core[name] == value for name, value in old_core.items())
    assert digest(PAPER / 'SHA256SUMS') == digest(PAPER / 'AUTHOR_MANIFEST.sha256') == AUTHOR_SEAL
    author = read_manifest(PAPER / 'AUTHOR_MANIFEST.sha256', PAPER)
    assert len(author) == 1985 and read_manifest(ROUND1 / 'AUTHOR_MANIFEST.sha256', ROUND1) == author
    assert all(core[name] == value for name, value in author.items())
    assert digest(ROUND1 / 'ROUND1_FREEZE_ADAPTER.py') == R1_FREEZER
    assert digest(PREPARATION / 'original_snapshot/freeze_p209_round1_v2.py') == R1_FREEZER
    assert digest(BATCH / 'qa/p209_round1_preparation_v2/freeze_p209_round1.py') == R1_FREEZER
    assert digest(PAPER / 'PAPER_MANIFEST.sha256') == PRIOR_WHOLE_SEAL
    prior_whole = read_manifest(PAPER / 'PAPER_MANIFEST.sha256', PAPER)
    assert len(prior_whole) == 5982 and 'PAPER_MANIFEST.sha256' not in prior_whole
    entries = list(PAPER.rglob('*'))
    assert all(not p.is_symlink() for p in entries)
    preexisting = {p.relative_to(PAPER).as_posix() for p in entries if p.is_file()}
    assert preexisting == set(prior_whole) | {'PAPER_MANIFEST.sha256'}
    live = {p.relative_to(PAPER).as_posix() for p in entries
            if p.is_file() and not p.is_relative_to(ROUND0) and not p.is_relative_to(ROUND1)}
    assert live == set(author) | {'SHA256SUMS', 'AUTHOR_MANIFEST.sha256', 'ROOT_ADOPTION.md', 'PAPER_MANIFEST.sha256'}
    assert digest(PAPER / 'PAPER_STATUS.md') == core['PAPER_STATUS.md']
    return core, author, prior_whole, preexisting


def accepted_b(core):
    for path in ANCHORS.values():
        digest(path)
    accepted = load(ACCEPTANCE)
    assert accepted['schema'] == 'p209-b-root-delta-closure-v1'
    assert accepted['status'] == 'ROOT_ACCEPTED_B_DELTA_ORIGINAL_CLOSURE_PASS'
    assert accepted['paper'] == 'P209' and type(accepted['input_round']) is int and accepted['input_round'] == 1
    assert accepted['round1_path'] == str(ROUND1)
    for field in ('reviewer_delta_accepted', 'root_original_inspection_complete', 'root_replay_closure_complete'):
        assert accepted[field] is True, field
    for field, expected in (('current_open_findings', 0), ('unchanged_author_payloads', 1985),
                            ('unchanged_round1_payloads', 2003)):
        assert type(accepted[field]) is int and accepted[field] == expected, field
    assert accepted['author_manifest_sha256'] == AUTHOR_SEAL and accepted['round1_manifest_sha256'] == ROUND1_SEAL
    review_rows = complete_manifest(REVIEW)
    pair_rows, launcher_rows = complete_manifest(PAIR), complete_manifest(LAUNCHER)
    assert type(accepted['review_manifest_entries']) is int and accepted['review_manifest_entries'] == len(review_rows)
    for field, path in (
        ('review_manifest_sha256', REVIEW / 'SHA256SUMS'), ('delta_sha256', REVIEW / 'DELTA.md'),
        ('initial_findings_sha256', REVIEW / 'FINDINGS.json'),
        ('current_findings_sha256', REVIEW / 'CURRENT_FINDINGS.json'), ('response_sha256', RESPONSE),
        ('root_pair_manifest_sha256', PAIR / 'SHA256SUMS'),
        ('root_launcher_manifest_sha256', LAUNCHER / 'SHA256SUMS')):
        assert accepted[field] == digest(path), field
    for name in ('REPORT.md', 'DELTA.md', 'INITIAL_DELTA.md', 'FINDINGS.json', 'CURRENT_FINDINGS.json',
                 'INITIAL_REVIEW_SEAL.sha256', 'INPUT_PINS.sha256', 'verify.py', 'CANONICAL.json',
                 'SOURCE_AND_PROOF.md', 'REPLAY_LOG.md', 'BUILD_REPORT.md'):
        assert name in review_rows, 'missing accepted review role: ' + name
    initial = load(REVIEW / 'FINDINGS.json')
    current = load(REVIEW / 'CURRENT_FINDINGS.json')
    for census in (initial, current):
        assert census['schema'] == 'p209-manuscript-review-findings-v1'
        assert census['reviewer'] == '/root/p209_b_reviewer' and census['input_round'] == 1
    # Initial phase/verdict/delta_status remain historical, not current acceptance.
    assert current['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'
    assert current['current_open_counts'] == {'critical': 0, 'major': 0, 'minor': 0}
    assert current['findings'] == [] and current['scientific_inputs_changed'] is False
    assert current['response_sha256'] == accepted['response_sha256']
    assert current['initial_complete_manifest_role'] == 'INITIAL_REVIEW_SEAL.sha256'
    assert current['initial_complete_manifest_sha256'] == B_INITIAL_SEAL
    assert digest(REVIEW / 'INITIAL_REVIEW_SEAL.sha256') == B_INITIAL_SEAL
    initial_rows = manifest_rows(REVIEW / 'INITIAL_REVIEW_SEAL.sha256')
    assert len(initial_rows) == 1298 and 'SHA256SUMS' not in initial_rows
    assert initial_rows['DELTA.md'] == digest(REVIEW / 'INITIAL_DELTA.md')
    assert initial_rows['DELTA.md'] != digest(REVIEW / 'DELTA.md'), 'accepted delta did not replace initial UNASSESSED body'
    for name, value in initial_rows.items():
        physical = REVIEW / ('INITIAL_DELTA.md' if name == 'DELTA.md' else name)
        assert digest(physical) == value
        assert review_rows[physical.relative_to(REVIEW).as_posix()] == value
    expected_inputs = {str((ROUND1 / name).relative_to(ROOT)): value for name, value in core.items()}
    expected_inputs[str((ROUND1 / 'SHA256SUMS').relative_to(ROOT))] = ROUND1_SEAL
    assert read_manifest(REVIEW / 'INPUT_PINS.sha256', ROOT) == expected_inputs
    assert digest(B_PREPARATION / 'SHA256SUMS') == B_PREPARATION_SEAL
    preparation_rows = complete_manifest(B_PREPARATION)
    assert len(preparation_rows) == 57
    assert digest(B_PREPARATION / 'root_record_pair.py') == B_RECORDER
    assert digest(B_PREPARATION / 'root_launch_pair.py') == B_LAUNCHER
    pair, launcher = load(PAIR / 'RECEIPT.json'), load(LAUNCHER / 'RECEIPT.json')
    assert pair['status'] == 'PASS_ROOT_REVIEW_B_PAIR' and pair['mode'] == 'pair' and pair['failures'] == []
    result = pair['result']
    assert result['canonical_adopted'] is False and result['canonical']['sha256'] == B_CANONICAL
    assert result['canonical']['bytes'] == 800966 and digest(REVIEW / 'CANONICAL.json') == B_CANONICAL
    assert len(result['replays']) == 2
    for replay in result['replays']:
        assert replay['status'] == 'PASS' and replay['total_states'] == 3414 and replay['checks'] == 54794
        assert replay['closure']['uncovered'] == [] and replay['closure']['bytecode'] == []
        assert replay['command']['exit'] == 0 and replay['command']['process_outcome'] == 'COMPLETED'
    assert len(result['comparisons']) == 3
    for comparison in result['comparisons']:
        assert comparison['exit'] == 0 and comparison['process_outcome'] == 'COMPLETED'
    assert launcher['status'] == 'PASS_ROOT_LAUNCH' and launcher['exit'] == 0 and launcher['outcome'] == 'COMPLETED'
    assert launcher['inputs_unchanged'] is True and launcher['cache_absent'] is True
    assert launcher['recorder_seal']['sha256'] == digest(PAIR / 'SHA256SUMS')
    assert launcher['recorder_closure']['payloads'] == len(pair_rows)
    assert launcher['recorder_closure']['status'] == pair['status']
    external = {str(base / name): value for base, rows in
                ((REVIEW, review_rows), (PAIR, pair_rows), (LAUNCHER, launcher_rows),
                 (B_PREPARATION, preparation_rows)) for name, value in rows.items()}
    counts = {'accepted_review_payloads': len(review_rows), 'initial_review_payloads_preserved': 1298,
              'initial_payload_path_aliases': 1, 'root_pair_payloads': len(pair_rows),
              'root_launcher_payloads': len(launcher_rows), 'root_preparation_payloads': 57}
    return accepted, external, counts, initial_rows


def historical_resolution(core, accepted, initial_rows):
    """Resolve exact (original path, old hash) roles, never path alone."""
    prior = load(ROUND1 / 'ROUND1_PROVENANCE.json')
    assert prior['schema'] == 'p209-round1-provenance-v2'
    required, hints = {}, {}

    def need(origin, value, role, hint=None):
        origin = str(origin)
        assert Path(origin).is_absolute() and re.fullmatch('[0-9a-f]{64}', value)
        key = (origin, value)
        required.setdefault(key, set()).add(role)
        if hint is not None:
            hint = Path(hint)
            assert digest(hint) == value
            if key not in hints or hint.is_relative_to(ROUND1):
                hints[key] = hint

    for role in ('all_source_inputs_before_and_rechecked_after', 'accepted_review_and_root_manifest_referents'):
        for origin, value in prior[role].items():
            need(origin, value, 'round1:' + role)
    for row in prior['anchor_mapping'].values():
        need(row['original_path'], row['sha256'], 'round1:physical-acceptance-anchor', ROUND1 / safe(row['physical_path']))
    for row in prior['historical_external_resolution'].values():
        need(row['original_path'], row['sha256'], 'round1:historical-external', row['round1_physical_path'])
    for role in ('round1_core_link_map', 'acceptance_and_historical_anchor_link_map'):
        for row in prior[role]:
            need(row['physical_target'], row['sha256'], 'round1:' + role)
    for origin, value in load(ROUND1 / 'FROZEN_LINK_MAP.json')['external_input_pins'].items():
        need(origin, value, 'round0:historical-external')
    for name, value in initial_rows.items():
        need(REVIEW / name, value, 'B:immutable-initial-payload',
             REVIEW / ('INITIAL_DELTA.md' if name == 'DELTA.md' else name))
    need(REVIEW / 'SHA256SUMS', B_INITIAL_SEAL, 'B:immutable-initial-complete-seal', REVIEW / 'INITIAL_REVIEW_SEAL.sha256')
    supplied = {}
    for row in accepted['historical_input_aliases']:
        assert set(row) == {'original_path', 'sha256', 'physical_path'}
        key = (row['original_path'], row['sha256'])
        physical = Path(row['physical_path'])
        assert key in required and key not in supplied, 'unused/broad/duplicate historical alias'
        assert physical.is_absolute() and physical.is_relative_to(ROOT) and physical.resolve() == physical
        assert str(physical) != key[0] and digest(physical) == key[1]
        complete_manifest(physical.parent)
        supplied[key] = physical
    resolved = []
    copies = {}
    used = set()
    for (origin, value), roles in sorted(required.items()):
        original = Path(origin)
        current = digest(original) if original.is_file() and not original.is_symlink() else None
        key = (origin, value)
        if current != value:
            assert key in hints or key in supplied, 'unmapped historical dependency drift: ' + repr(key)
            physical = hints.get(key, supplied.get(key))
            if key in supplied:
                used.add(key)
        else:
            physical = original
        assert digest(physical) == value
        target_path, copy_relative = physical, None
        if physical.is_relative_to(ROUND1):
            relative = physical.relative_to(ROUND1).as_posix()
            assert core[relative] == value
            target_path = TARGET / relative
            mode = 'preserved-round1-core-alias' if current != value else 'round1-core-remapped-to-round2'
        elif current != value:
            matching = [name for name, source in ANCHORS.items() if source == physical]
            if matching:
                target_path = TARGET / 'ROUND2_ACCEPTANCE' / matching[0]
                mode = 'exact-new-acceptance-anchor-alias'
            else:
                complete_manifest(physical.parent)
                copy_relative = 'ROUND2_HISTORICAL_ALIASES/' + str(len(copies) + 1).zfill(3) + '_' + original.name
                assert copy_relative not in core
                copies[copy_relative] = (physical, value)
                target_path = TARGET / copy_relative
                mode = 'exact-new-historical-alias'
        else:
            mode = 'unchanged-original'
        resolved.append({'original_path': origin, 'sha256': value, 'roles': sorted(roles),
                         'current_original_sha256': current, 'physical_source': str(physical),
                         'round2_physical_path': str(target_path), 'copy_relative': copy_relative, 'mode': mode})
    assert used == set(supplied), 'unused alias for unchanged original'
    return prior, resolved, copies


def link_mapping(core, prior, history):
    resolved = {(row['original_path'], row['sha256']): row for row in history}
    historical_links = []
    for role in ('round1_core_link_map', 'acceptance_and_historical_anchor_link_map'):
        for row in prior[role]:
            physical = Path(resolved[(row['physical_target'], row['sha256'])]['round2_physical_path'])
            historical_links.append({**row, 'source_role': role,
                'round1_physical_target': row['physical_target'], 'physical_target': str(physical)})
    origins = {str(ROUND1 / name): (TARGET / name, value) for name, value in core.items()}
    for name, source in ANCHORS.items():
        origins[str(source)] = (TARGET / 'ROUND2_ACCEPTANCE' / name, digest(source))
    new_links = []
    documents = [('ROUND2_ACCEPTANCE/' + name, source, source) for name, source in ANCHORS.items()]
    documents += [(row['copy_relative'], Path(row['physical_source']), Path(row['original_path']))
                  for row in history if row['copy_relative']]
    for document, source, document_origin in documents:
        if source.suffix != '.md':
            continue
        for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', source.read_text()):
            href = href.strip().strip('<>')
            if href.startswith(('https://', 'http://', 'mailto:', '#')):
                continue
            pathpart = unquote(href.split('#', 1)[0])
            if not pathpart:
                continue
            origin = (document_origin.parent / pathpart).resolve()
            if str(origin) in origins:
                physical, value = origins[str(origin)]
                mode = 'physical-core-or-anchor'
            else:
                if origin.is_dir():
                    complete_manifest(origin)
                    physical = origin / 'SHA256SUMS'
                    mode = 'external-directory-via-complete-manifest'
                else:
                    physical = origin
                    mode = 'current-navigation-original-origin'
                value = digest(physical)
            new_links.append({'document': document, 'source_bytes_path': str(source),
                'original_document': str(document_origin), 'href': href, 'original_target': str(origin),
                'physical_target': str(physical), 'sha256': value, 'mode': mode,
                'historical_target_body_identity_claimed': False})
    return historical_links, new_links


def main():
    created = False
    try:
        assert sys.argv[1:] == ['freeze-round2-after-accepted-b'], 'explicit root invocation required'
        assert Path(__file__).resolve() == PREPARATION / 'freeze_p209_round2.py'
        assert dict(os.environ) == ENV and Path.cwd() == ROOT
        assert sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode
        assert Path(sys.executable).resolve() == Path('/usr/bin/python3.10')
        assert sys.pycache_prefix == str(TARGET / 'never_created_freezer_cache') and not Path(sys.pycache_prefix).exists()
        assert not TARGET.exists() and not TARGET.is_symlink(), 'existing freeze'
        assert PAPER.resolve() == PAPER and PREPARATION.resolve() == PREPARATION
        complete_manifest(PREPARATION)
        digest(Path('/usr/bin/python3.10'))
        digest(Path('/usr/bin/cmp'))
        core, author, prior_whole, preexisting = core_inputs()
        accepted, external, counts, initial_rows = accepted_b(core)
        prior, history, copies = historical_resolution(core, accepted, initial_rows)
        historical_links, anchor_links = link_mapping(core, prior, history)
        source = Path(__file__).resolve(strict=True)
        selfhash = digest(source)
        anchors = {name: digest(path) for name, path in ANCHORS.items()}
        assert len(anchors) == 15
        raw_cmp(PAPER / 'SHA256SUMS', PAPER / 'AUTHOR_MANIFEST.sha256')
        before = dict(READ_PINS)
        # All fixed acceptance, complete input and historical gates are above.
        # No target or acceptance-shaped placeholder is created before this point.
        TARGET.mkdir()
        created = True
        for name in sorted(core):
            destination = TARGET / safe(name)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROUND1 / name, destination)
            assert digest(destination) == core[name]
        acceptance_dir = TARGET / 'ROUND2_ACCEPTANCE'
        acceptance_dir.mkdir()
        for name, origin in ANCHORS.items():
            shutil.copyfile(origin, acceptance_dir / name)
            assert digest(acceptance_dir / name) == anchors[name]
        for name, (origin, value) in sorted(copies.items()):
            destination = TARGET / safe(name)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(origin, destination)
            assert digest(destination) == value
        shutil.copyfile(source, TARGET / 'ROUND2_FREEZE_ADAPTER.py')
        assert digest(TARGET / 'ROUND2_FREEZE_ADAPTER.py') == selfhash
        raw_cmp(PAPER / 'AUTHOR_MANIFEST.sha256', TARGET / 'AUTHOR_MANIFEST.sha256')
        raw_cmp(ROUND1 / 'SHA256SUMS', acceptance_dir / 'ROUND1_CORE_MANIFEST.sha256')
        raw_cmp(REVIEW / 'INITIAL_DELTA.md', acceptance_dir / 'B_INITIAL_DELTA.md')
        assert read_manifest(TARGET / 'AUTHOR_MANIFEST.sha256', TARGET) == author
        for row in historical_links + anchor_links:
            assert digest(Path(row['physical_target'])) == row['sha256']
        for row in history:
            assert digest(Path(row['round2_physical_path'])) == row['sha256']
        assert complete_manifest(ROUND1) == core
        assert read_manifest(PAPER / 'PAPER_MANIFEST.sha256', PAPER) == prior_whole
        assert digest(acceptance_dir / 'PRE_ROUND2_PAPER_MANIFEST.sha256') == PRIOR_WHOLE_SEAL
        assert accepted_b(core) == (accepted, external, counts, initial_rows)
        assert historical_resolution(core, accepted, initial_rows) == (prior, history, copies)
        complete_manifest(PREPARATION)
        assert {p.relative_to(PAPER).as_posix() for p in PAPER.rglob('*')
                if p.is_file() and not p.is_relative_to(TARGET)} == preexisting
        assert not any(p.is_symlink() for p in PAPER.rglob('*'))
        assert all(digest(Path(path)) == value for path, value in before.items())
        metadata = {
            'schema': 'p209-round2-provenance-v1',
            'scope': 'Physical Round2 after actual accepted B delta/root closure; not terminal build/view or five-paper completion.',
            'author_manifest_sha256': AUTHOR_SEAL, 'round1_manifest_sha256': ROUND1_SEAL,
            'author_payloads_preserved': 1985, 'round1_core_payloads_copied': 2003,
            'historical_round0_round1_metadata_and_adapters_unchanged': True,
            'core_source_manifest': str(ROUND1 / 'SHA256SUMS'), 'core_payload_pins': core,
            'new_complete_manifest_role': 'SHA256SUMS covers exactly 2003 unchanged core payloads, 15 physical anchors, actually needed new historical aliases, ROUND2_FREEZE_ADAPTER.py and ROUND2_PROVENANCE.json; prior inner seals retain original historical bases.',
            'anchor_mapping': {name: {'original_path': str(ANCHORS[name]),
                'physical_path': 'ROUND2_ACCEPTANCE/' + name, 'sha256': value} for name, value in anchors.items()},
            'accepted_review_and_root_manifest_referents': external,
            'accepted_root_assertions': accepted, 'accepted_evidence_counts': counts,
            'immutable_initial_census_anchor': 'ROUND2_ACCEPTANCE/B_INITIAL_FINDINGS.json',
            'immutable_initial_delta_anchor': 'ROUND2_ACCEPTANCE/B_INITIAL_DELTA.md',
            'initial_review_manifest_original_base': str(REVIEW),
            'initial_review_manifest_exact_alias': {'original_path': str(REVIEW / 'DELTA.md'),
                'sha256': initial_rows['DELTA.md'], 'physical_path': 'ROUND2_ACCEPTANCE/B_INITIAL_DELTA.md'},
            'current_acceptance_anchors': ['ROUND2_ACCEPTANCE/B_DELTA.md',
                'ROUND2_ACCEPTANCE/B_CURRENT_FINDINGS.json', 'ROUND2_ACCEPTANCE/ROOT_DELTA_CLOSURE.actual.json'],
            'prior_whole_paper_manifest': {'original_path': str(PAPER / 'PAPER_MANIFEST.sha256'),
                'original_referent_base': str(PAPER), 'sha256': PRIOR_WHOLE_SEAL,
                'physical_path': str(acceptance_dir / 'PRE_ROUND2_PAPER_MANIFEST.sha256'),
                'physical_relative_path': 'ROUND2_ACCEPTANCE/PRE_ROUND2_PAPER_MANIFEST.sha256',
                'payloads': 5982, 'original_referent_pins': prior_whole,
                'exact_whole_tree_checked_before_creation': True,
                'original_referents_and_manifest_bytes_rechecked_after_creation': True,
                'complete_current_paper_after_round2': False,
                'lifecycle_rule': 'Root later refreshes only the live whole-paper manifest; this exact physical anchor retains its original PAPER-relative 5982 referents. Never rebase historical rows to the anchor directory.'},
            'historical_input_resolution': history, 'round2_historical_link_map': historical_links,
            'acceptance_and_historical_anchor_link_map': anchor_links,
            'all_source_inputs_before_and_rechecked_after': before,
            'freezer_origin': str(source), 'freezer_sha256': selfhash,
            'original_round1_freezer_sha256': R1_FREEZER,
            'B_source_canonical_runtime_reference': {'preparation': str(B_PREPARATION),
                'preparation_manifest_sha256': B_PREPARATION_SEAL,
                'recorder_sha256': B_RECORDER, 'launcher_sha256': B_LAUNCHER,
                'canonical_sha256': B_CANONICAL, 'canonical_bytes': 800966,
                'runtime_evidence_role': str(PAIR / 'RECEIPT.json'),
                'not_a_new_execution': True},
            'launch_argv': sys.argv, 'launch_orig_argv': sys.orig_argv,
            'environment': ENV, 'cwd': str(ROOT), 'raw_comparisons': COMPARISONS,
            'limitations': 'Root gate attests actual independent B acceptance and original/replay closure. This freezer verifies documentary identities and package closure, not mathematics, runtime validity, build quality or page viewing. Copied historical metadata is not executed. Newly pinned navigation targets are current original-origin checks, not historical target-body identity. Runtime references remain sampled/conservative, not OS-hermetic or continuous tracing.',
            'external': 'OWNER_AMBER / HOLD_EXTERNAL'}
        with (TARGET / 'ROUND2_PROVENANCE.json').open('x') as stream:
            json.dump(metadata, stream, indent=2, sort_keys=True)
            stream.write('\n')
        expected = dict(core)
        expected.update({'ROUND2_ACCEPTANCE/' + name: value for name, value in anchors.items()})
        expected.update({name: value for name, (_, value) in copies.items()})
        expected['ROUND2_FREEZE_ADAPTER.py'] = selfhash
        expected['ROUND2_PROVENANCE.json'] = digest(TARGET / 'ROUND2_PROVENANCE.json')
        assert len(expected) == 2020 + len(copies)
        assert {p.relative_to(TARGET).as_posix(): digest(p) for p in TARGET.rglob('*') if p.is_file()} == expected
        assert all(digest(Path(path)) == value for path, value in before.items())
        with (TARGET / 'SHA256SUMS').open('x') as stream:
            stream.write(''.join(value + '  ' + name + '\n' for name, value in sorted(expected.items())))
        assert complete_manifest(TARGET) == expected
        print(json.dumps({'status': 'PASS_PHYSICAL_P209_ROUND2', 'payloads': len(expected),
            'manifest_sha256': digest(TARGET / 'SHA256SUMS'), 'core_payloads': 2003,
            'acceptance_anchor_payloads': 15, 'author_payloads_unchanged': 1985,
            'physical_new_historical_alias_payloads': len(copies),
            'accepted_root_closure_sha256': anchors['ROOT_DELTA_CLOSURE.actual.json'],
            'raw_comparisons': COMPARISONS,
            'boundary': 'No new science/build/view or terminal/batch-completion inference.'}, indent=2, sort_keys=True))
        return 0
    except BaseException:
        failure = {'status': 'FAIL_ROUND2_PRESERVED' if created else 'REFUSED_BEFORE_ROUND2_CREATION',
            'traceback': traceback.format_exc(), 'target_created_by_this_invocation': created,
            'raw_comparisons': COMPARISONS, 'known_read_pins': READ_PINS,
            'acceptance_or_completion_not_inferred': True}
        if created and not (TARGET / 'SHA256SUMS').exists():
            with (TARGET / 'ROUND2_FAILURE.json').open('x') as stream:
                json.dump(failure, stream, indent=2, sort_keys=True)
                stream.write('\n')
        print(json.dumps(failure, indent=2, sort_keys=True))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
