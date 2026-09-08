#!/usr/bin/env python3
"""New exact-five P210 metadata reconstruction, not an old reader import.

All original B and terminal rows are reconstructed before projection or
rebasing. The driver supplies measured I/O and performs the merged current
map content reads. No function runs merely by importing this new module.
"""
from pathlib import Path
import json

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
INITIAL = QA / 'p210_terminal_artifact_03'
INITIAL_PREP = QA / 'p210_terminal_artifact_revision_03'
ROLES = QA / 'p210_terminal_artifact_preparation/ACTUAL_ROLES.json'
B = QA.parent / 'reviews/p210_b'


def reconstruct(driver):
    need, obj, pin = driver.need, driver.obj, driver.pin
    byte_pin, canonical = driver.byte_pin, driver.canonical
    report = obj(INITIAL / 'ARTIFACT_REPORT.json')
    rec = report['complete_current_key_reconstruction']
    need(report['schema'] == 'p210-terminal-artifact-reader-revision-03' and
         report['status'] == 'PASS_P210_TERMINAL_ARTIFACT_INITIAL_LIFECYCLE_FOLLOWUP_PENDING' and
         report['paper'] == 'P210' and report['checks'] == sum(report['checks_by_kind'].values()) == 5838453 and
         report['root_acceptance'] is report['paper_completion'] is report['five_paper_completion'] is False and
         all(report[name] == 0 for name in ('new_scientific_runs', 'new_builds', 'new_views',
             'new_manuscript_reviews', 'reader_file_writes', 'old_programs_imported_or_executed')) and
         report['external'] == 'OWNER_AMBER / HOLD_EXTERNAL', 'actual P210 initial artifact scope')
    roles = obj(ROLES)
    aliases = []

    def alias(logical, physical, expected, provenance):
        driver.rich_schema(expected)
        need(expected['real'] == logical and expected['symlink'] is None,
             'exact original documentary role metadata', logical)
        physical_record = pin(physical)
        need(byte_pin(physical) == {'sha256': expected['sha256'], 'bytes': expected['size']},
             'actual preserved historical physical bytes', physical)
        aliases.append(dict(logical=logical, original=expected, physical=physical,
                            physical_record=physical_record, provenance=provenance))

    for row in roles['exact_available_historical_aliases']:
        alias(row['logical'], row['physical'],
              dict(real=row['logical'], sha256=row['original_sha256'],
                   size=row['original_size'], symlink=None), row['provenance_role'])
    round2_path = PAPER / 'frozen_round2/ROUND2_PROVENANCE.json'
    round2 = obj(round2_path)
    for logical, row in roles['actual_b_final_map_recipe']['old_control_roles_requiring_actual_Round2_history'].items():
        anchor = round2['anchors']['PRE_ROUND2_' + Path(logical).name]
        need(anchor['original_path'] == logical and anchor['sha256'] == row['sha256'],
             'actual Round2 old-control source anchor', logical)
        alias(logical, str(PAPER / 'frozen_round2' / anchor['physical_path']), row, str(round2_path))
    preserved = QA / 'p210_preterminal_controls_01/PRESERVATION.actual.json'
    for logical, row in obj(preserved)['copies'].items():
        alias(logical, row['physical'],
              dict(real=logical, sha256=row['sha256'], size=row['bytes'], symlink=None), str(preserved))
    by_key = {(row['logical'], row['original']['sha256'], row['original']['size']): row for row in aliases}
    need(len(aliases) == len(by_key) == 10 and
         [by_key[key] for key in sorted(by_key)] == rec['exact_historical_aliases'],
         'all and only ten complete source-defined P210 initial aliases')

    def rebase(name, row):
        driver.rich_schema(row)
        selected = by_key.get((name, row['sha256'], row['size']))
        if selected is not None:
            need(selected['original'] == row, 'complete old alias metadata unchanged', name)
            return selected['physical'], selected['physical_record']
        return name, row

    basis = roles['actual_b_final_map_recipe']
    common = obj(basis['common_path'])
    need(common == obj(B / 'DELTA_INPUTS_AFTER.json.gz') and len(common) == 121013,
         'entire actual B common before-after map')
    original_b = {}
    for name, row in common.items():
        need(set(row) == {'resolved', 'sha256', 'bytes', 'symlink'},
             'actual B original four-field schema', name)
        original_b[name] = dict(real=row['resolved'], sha256=row['sha256'],
                                size=row['bytes'], symlink=row['symlink'])
    b_native = obj(basis['root_completion'])
    need(b_native['result']['exit_code'] == 0, 'actual accepted B root normal completion')
    b_received = json.loads(b_native['result']['output'])
    extra_b = b_received['current_read_keys_outside_B_common']
    need(len(extra_b) == 44 and not set(original_b) & set(extra_b), 'B44 original extras are disjoint')
    original_b.update(extra_b)
    need(len(original_b) == 121057 and
         canonical(original_b) == {'sha256': basis['canonical_sha256'], 'bytes': basis['canonical_bytes']} and
         basis == rec['b_final_basis'] and basis['canonical_sha256'] ==
         b_received['complete_current_read_map_canonical_sha256'] ==
         'c75e67753bb7cec027c788b1d00a78c977cfb99fb53153d9fe57511e546fea2d',
         'complete original B121057 canonical, before physical rebase')

    terminal_path = QA / 'p210_terminal_root_reception_01/ROOT_RECEPTION.json'
    terminal = obj(terminal_path)
    terminal_basis = rec['terminal_receiver_basis']
    need(terminal_basis['path'] == str(terminal_path) and terminal_basis['pin'] == byte_pin(terminal_path) and
         terminal_basis['selector'] == ['current_key_reconstruction'], 'exact actual terminal recipe source')
    recipe = terminal['current_key_reconstruction']
    need(recipe['known_ledger'] == str(PAPER / 'qa_final/KNOWN_INPUTS_BEFORE.json.gz') and
         recipe['known_ledger_pin'] == byte_pin(recipe['known_ledger']),
         'fixed terminal grouped-ledger path and pin')
    ledger = obj(recipe['known_ledger'])
    need(ledger == obj(PAPER / 'qa_final/KNOWN_INPUTS_AFTER.json.gz') and
         set(ledger) == {'runtime', 'configuration', 'tex'}, 'complete original terminal grouped interval')
    known = {}
    for group in ledger.values():
        for name, row in group.items():
            need(name not in known or known[name] == row, 'same-spelling terminal group duplicates agree', name)
            known[name] = row
    need(len(known) == 123595 and len(recipe['extra_entries']) == 1904 and
         not set(known) & set(recipe['extra_entries']), 'complete terminal disjoint123595+1904 before projection')
    original_terminal = known | recipe['extra_entries']
    need(len(original_terminal) == 125499 and
         canonical(original_terminal) == recipe['complete_map'] == terminal_basis['original_map'],
         'complete original terminal presence-rich canonical')
    files, nonfiles = {}, {}
    for name, row in original_terminal.items():
        need(Path(name).is_absolute() and
             set(row) == {'exists', 'symlink', 'link', 'resolved', 'is_file', 'is_dir'} |
             ({'sha256', 'bytes'} if row['is_file'] else set()) and
             all(type(row[field]) is bool for field in ('exists', 'symlink', 'is_file', 'is_dir')) and
             (type(row['link']) is str if row['symlink'] else row['link'] is None),
             'complete original terminal row schema', name)
        if row['is_file']:
            need(row['exists'] is True and row['is_dir'] is False, 'original terminal regular-file role', name)
            files[name] = dict(real=row['resolved'], sha256=row['sha256'], size=row['bytes'],
                               symlink=row['link'] if row['symlink'] else None)
        else:
            nonfiles[name] = row
    need(nonfiles == rec['nonfile_presence_roles'] and len(nonfiles) == rec['nonfile_presence_count'] == 5271,
         'all5271 initial nonfile roles retained without file projection loss')
    base = {}
    for group in (original_b, files):
        for name, value in group.items():
            target, row = rebase(name, value)
            need(target not in base or base[target] == row, 'whole rebased physical duplicate equality', target)
            base[target] = row
    need(len(base) == rec['base_union_keys'] == 121899 and canonical(base) == rec['base_union_canonical'],
         'whole initial B-plus-terminal physical base')
    extra = rec['extra_current_keys']
    need(len(extra) == rec['extra_count'] == 250 and not set(base) & set(extra), 'initial250 extras disjoint')
    initial_full = base | extra
    need(len(initial_full) == rec['complete_keys'] == 122149 and canonical(initial_full) == rec['canonical_map'] ==
         {'bytes': 33828798, 'sha256': '7a6de120440fb8658e6b354d54531586714d73cc3c0066d5852022e2dc1659ef'},
         'entire122149 initial rich map reconstructed, not count-only')
    for row in extra.values():
        driver.rich_schema(row)
    runtime = report['current_reader_runtime']
    need(len(runtime['modules']) == 52 and len(runtime['mapped_files']) == 11 and
         driver.bytes_key(runtime['raw_maps'].encode()) ==
         {'sha256': runtime['raw_maps_sha256'], 'bytes': runtime['raw_maps_bytes']},
         'entire actual initial52-module11-map sample')
    for row in runtime['modules'].values():
        need(initial_full[row['path']] == {k: v for k, v in row.items() if k != 'path'},
             'actual initial module full fields covered')
    for name, row in runtime['mapped_files'].items():
        need(initial_full[name] == row, 'actual initial mapped full fields covered', name)
    return initial_full, nonfiles, report, ledger, dict(
        source=str(INITIAL / 'ARTIFACT_REPORT.json'), source_pin=byte_pin(INITIAL / 'ARTIFACT_REPORT.json'),
        selector=['complete_current_key_reconstruction'], original_B_keys=len(original_b),
        original_terminal_presence_keys=len(original_terminal), exact_historical_aliases=10,
        original_base_keys=len(base), original_extra_keys=len(extra), original_complete_keys=len(initial_full),
        original_complete_map=rec['canonical_map'])
