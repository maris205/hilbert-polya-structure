#!/usr/bin/env python3
"""Static infrastructure/manifest checks only; never load or run the freezer."""
import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers204_208_sequence/qa/p209_round1_preparation_v2'
OLD = PREP.parent / 'p209_round1_preparation'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
REVIEW = PREP.parent.parent / 'reviews/p209_a'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PINS = {}
COMMANDS = []


def digest(path):
    assert path.is_file() and not path.is_symlink()
    value = sha256(path.read_bytes()).hexdigest()
    key = str(path)
    assert key not in PINS or PINS[key] == value
    PINS[key] = value
    return value


def manifest(path, base, complete=False):
    digest(path)
    rows = {}
    for line in path.read_text().splitlines():
        value, name = line.split('  ', 1)
        relative = Path(name)
        assert re.fullmatch('[0-9a-f]{64}', value) and name not in rows
        assert not relative.is_absolute() and relative.as_posix() == name and '..' not in relative.parts
        assert digest(base / name) == value
        rows[name] = value
    if complete:
        entries = list(base.rglob('*'))
        assert all(not p.is_symlink() for p in entries)
        assert path.parent == base and path.name not in rows
        assert {p.relative_to(base).as_posix() for p in entries if p.is_file()} == set(rows) | {path.name}
    return rows


def command(argv):
    started = time.time()
    process = subprocess.run(argv, capture_output=True, check=False, cwd=ROOT, env=ENV)
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
           'started_epoch': started, 'finished_epoch': time.time(),
           'process_outcome': 'COMPLETED', 'exit': process.returncode,
           'stdout': process.stdout.decode(), 'stderr': process.stderr.decode()}
    COMMANDS.append(row)
    return process


def main():
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
    assert not (PAPER / 'frozen_round1').exists()
    assert not (PAPER / 'frozen_round1').is_symlink()
    assert digest(OLD / 'SHA256SUMS') == 'f8396ff69a16f4c215f9a221110c1d039104b1b0764d4f570c52c794036094b1'
    old_rows = manifest(OLD / 'SHA256SUMS', OLD, complete=True)
    assert len(old_rows) == 10
    source_path = PREP / 'freeze_p209_round1.py'
    digest(source_path)
    source = source_path.read_text()
    syntax = ast.parse(source, filename=str(source_path))
    imports = {node.module if isinstance(node, ast.ImportFrom) else alias.name
               for node in ast.walk(syntax) if isinstance(node, (ast.Import, ast.ImportFrom))
               for alias in node.names}
    assert imports == {'hashlib', 'json', 'os', 'pathlib', 're', 'shutil',
                       'subprocess', 'sys', 'time', 'traceback', 'urllib.parse'}
    calls = [node for node in ast.walk(syntax) if isinstance(node, ast.Call)]
    assert not any(isinstance(node.func, ast.Name) and node.func.id in
                   {'exec', 'eval', 'compile', '__import__'} for node in calls)
    assert not any(isinstance(node.func, ast.Attribute) and node.func.attr in
                   {'copytree', 'rmtree', 'unlink', 'rename', 'replace'} for node in calls)
    anchors = next(node.value for node in syntax.body if isinstance(node, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == 'ANCHORS' for t in node.targets))
    names = [ast.literal_eval(key) for key in anchors.keys]
    assert len(names) == len(set(names)) == 11
    assert 'A_CURRENT_FINDINGS.json' in names and 'PRE_ROUND1_PAPER_MANIFEST.sha256' in names
    first_creation = source.index('        TARGET.mkdir()')
    assert source.index('        core, author, live, prior_whole = core_inputs()') < first_creation
    assert source.index('        accepted, accepted_external, counts = accepted_a(core)') < first_creation
    assert source.index('        history, core_links, anchor_links = link_mapping(core, accepted)') < first_creation
    assert "assert len(expected) == 2002 + len(alias_copies)" in source
    assert "assert live == set(author) | {'SHA256SUMS', 'AUTHOR_MANIFEST.sha256', 'ROOT_ADOPTION.md', 'PAPER_MANIFEST.sha256'}" in source
    assert "assert read_manifest(PAPER / 'PAPER_MANIFEST.sha256', PAPER) == prior_whole" in source[first_creation:]
    assert 'complete_manifest(PAPER)' not in source
    assert "'complete_current_paper_after_round1': False" in source
    assert "findings['delta_status']" not in source and "findings['phase']" not in source
    assert "current['phase'] == 'ACTUAL_EXACT_NOCHANGE_DELTA'" in source
    assert "current['verdict'] == current['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'" in source
    assert "current['response_sha256'] == accepted['response_sha256'] == digest(RESPONSE)" in source
    assert "assert all(review_rows.get(name) == value for name, value in initial_rows.items())" in source
    assert "'immutable_initial_census_anchor': 'ROUND1_ACCEPTANCE/A_INITIAL_FINDINGS.json'" in source
    assert "'p209-round1-provenance-v2'" in source
    assert "'original_referent_base': str(PAPER)" in source
    assert "PREPARATION = BATCH / 'qa/p209_round1_preparation_v2'" in source

    r0 = PREP / 'original_snapshot/freeze_p209_round0.py'
    v1 = PREP / 'original_snapshot/freeze_p209_round1_v1.py'
    for left, right in ((r0, PREP.parent / 'freeze_p209_round0.py'),
                        (r0, PAPER / 'frozen_round0/FREEZE_ADAPTER.py'),
                        (v1, OLD / 'freeze_p209_round1.py')):
        assert command(['/usr/bin/cmp', '--', str(left), str(right)]).returncode == 0
        assert digest(left) == digest(right)
    assert digest(r0) == '95473c820d305410ae042eed50c288fef02244e6ab41234648db641f0dd7866a'
    assert digest(v1) == 'e62f11c0eaed932c364fe2bd44f37cc9a92a4819739fc51d306f41c01a2b0096'
    for original, output in ((r0, 'ADAPTATION.diff'), (v1, 'V1_TO_V2.diff')):
        result = command(['/usr/bin/diff', '-u', '--label', str(original.relative_to(PREP)),
                          '--label', 'freeze_p209_round1.py', str(original), str(source_path)])
        assert result.returncode == 1 and result.stderr == b''
        assert result.stdout == (PREP / output).read_bytes()
        digest(PREP / output)

    prior = PAPER / 'PAPER_MANIFEST.sha256'
    assert digest(prior) == 'cd8b345c2e8c7e71afa9d2d2d64e6ca74332828b4447e43ba6894c5a8398a4b2'
    whole = manifest(prior, PAPER, complete=True)
    assert len(whole) == 3978
    core = manifest(PAPER / 'frozen_round0/SHA256SUMS', PAPER / 'frozen_round0', complete=True)
    author = manifest(PAPER / 'AUTHOR_MANIFEST.sha256', PAPER)
    assert len(core) == 1989 and len(author) == 1985
    live = {p.relative_to(PAPER).as_posix() for p in PAPER.rglob('*')
            if p.is_file() and not p.is_relative_to(PAPER / 'frozen_round0')}
    assert live == set(author) | {'SHA256SUMS', 'AUTHOR_MANIFEST.sha256',
                                 'ROOT_ADOPTION.md', 'PAPER_MANIFEST.sha256'}

    acceptance_path = PREP.parent / 'P209_A_ROOT_DELTA_INSPECTION.actual.json'
    digest(acceptance_path)
    accepted = json.loads(acceptance_path.read_text())
    contract_path = PREP / 'ACCEPTANCE_INPUT_CONTRACT.json'
    digest(contract_path)
    contract = json.loads(contract_path.read_text())
    for key, value in contract['required_literal_fields'].items():
        assert accepted[key] == value
    review = manifest(REVIEW / 'SHA256SUMS', REVIEW, complete=True)
    assert len(review) == accepted['review_manifest_entries'] == 1342
    assert digest(REVIEW / 'SHA256SUMS') == accepted['review_manifest_sha256']
    for field, name in (('delta_sha256', 'DELTA.md'), ('findings_sha256', 'FINDINGS.json'),
                        ('current_findings_sha256', 'CURRENT_FINDINGS.json')):
        assert digest(REVIEW / name) == accepted[field]
    current = json.loads((REVIEW / 'CURRENT_FINDINGS.json').read_text())
    assert current['phase'] == 'ACTUAL_EXACT_NOCHANGE_DELTA'
    assert current['verdict'] == current['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'
    assert current['reviewer'] == '/root/p209_a_reviewer' and current['input_round'] == 0
    assert current['schema'] == 'p209-manuscript-review-findings-v1'
    assert current['response_sha256'] == accepted['response_sha256']
    assert current['current_open_counts'] == {'critical': 0, 'major': 0, 'minor': 0}
    assert current['findings'] == [] and current['scientific_inputs_changed'] is False
    assert current['initial_complete_manifest_role'] == 'INITIAL_REVIEW_SEAL.sha256'
    initial = manifest(REVIEW / 'INITIAL_REVIEW_SEAL.sha256', REVIEW)
    assert digest(REVIEW / 'INITIAL_REVIEW_SEAL.sha256') == current['initial_complete_manifest_sha256']
    assert len(initial) == accepted['initial_review_payloads_preserved'] == 1227
    assert all(review.get(name) == value for name, value in initial.items())

    oldmap_path = PAPER / 'frozen_round0/FROZEN_LINK_MAP.json'
    digest(oldmap_path)
    oldmap = json.loads(oldmap_path.read_text())
    aliases = {row['original_path']: row for row in accepted['historical_input_aliases']}
    used = set()
    for origin, value in oldmap['external_input_pins'].items():
        if digest(Path(origin)) != value:
            row = aliases[origin]
            assert set(row) == {'original_path', 'sha256', 'physical_path'}
            assert row['sha256'] == value
            physical = Path(row['physical_path'])
            assert physical.resolve() == physical and digest(physical) == value
            manifest(physical.parent / 'SHA256SUMS', physical.parent, complete=True)
            used.add(origin)
    assert used == set(aliases) and len(used) == 1
    assert len(oldmap['links']) == 243
    before = dict(PINS)
    assert all(digest(Path(path)) == value for path, value in before.items())
    assert manifest(OLD / 'SHA256SUMS', OLD, complete=True) == old_rows
    assert not (PAPER / 'frozen_round1').exists()
    print(json.dumps({'status': 'PASS_STATIC_PREPARATION_ONLY',
        'not_a_freezer_invocation': True, 'round1_absent': True,
        'not_scientific_or_build_or_review_validation': True,
        'source_lines': len(source.splitlines()), 'anchors': names,
        'preserved_v1_complete_payloads': len(old_rows),
        'prior_whole_payloads_verified': len(whole), 'round0_core_payloads': len(core),
        'author_payloads': len(author), 'accepted_review_manifest_payloads': len(review),
        'preserved_initial_review_payloads': len(initial),
        'historical_external_pins_checked': len(oldmap['external_input_pins']),
        'used_historical_aliases': len(used), 'planned_payload_count': 2002 + len(used),
        'raw_commands': COMMANDS, 'input_paths_rechecked_twice': len(before),
        'verified_manifest_pins': {path: value for path, value in before.items()
            if Path(path).name in {'SHA256SUMS', 'AUTHOR_MANIFEST.sha256',
                'PAPER_MANIFEST.sha256', 'INITIAL_REVIEW_SEAL.sha256'}},
        'static_input_inventory_sha256': sha256(json.dumps(before,
            sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        'limitations': 'AST/text/schema/full-manifest checks and raw source/diff comparisons only; no freezer or scientific program was imported or executed. No new acceptance, root replay/build/view, physical Round1, B review or terminal closure.',
        'external': 'OWNER_AMBER / HOLD_EXTERNAL'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
