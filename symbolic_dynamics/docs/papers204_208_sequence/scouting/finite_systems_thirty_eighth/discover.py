#!/usr/bin/env python3
"""Filename-first scoped historical desk; never loads protected body paths."""
import contextlib
import io
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record

SELF = pathlib.Path(__file__).resolve()
ROOTS = [record.ROOT / 'docs' / name / 'scouting' for name in (
    'papers204_208_sequence', 'papers197_201_sequence', 'papers192_196_sequence',
    'papers187_191_sequence', 'papers172_176_sequence', 'papers157_161_sequence')]
NAMES = {'SCOUT.md', 'SCOUT_REPORT.md', 'SCOUT_AND_KILL_LEDGER.md', 'KILL_LEDGER.md',
         'INTAKE.md', 'PROOF_AND_DISPOSITION.md', 'PROOF_AND_ADAPTERS.md', 'PROOF_PACKAGE.md'}


def exclude(path):
    if path.is_relative_to(record.OWN):
        return 'own_lane'
    if record.forbidden(path):
        return 'protected_or_mixed'
    parts = path.relative_to(record.ROOT).parts
    if any(part.lower() in {'inputs', 'controls', 'sources', 'commands', 'public_sources', 'discovery', 'word_local'}
           or part.lower().startswith(('evidence_capture', 'replay', 'source_only', 'strict_', 'input_', 'history_'))
           for part in parts):
        return 'artifact_or_out_of_scope_word_lane'
    if any(part.startswith(('ORR_', 'LNR_', 'NED_', 'CTM_', 'HVD_', 'NCC_', 'GCF_', 'LAST_SEAT_'))
           or part in {'finite_systems_thirty_third', 'finite_systems_thirty_fourth', 'finite_systems_thirty_sixth'}
           for part in parts):
        return 'old_hold_or_own_prior_lane'
    if path.name not in NAMES:
        return 'unselected_basename'
    if not any(path.is_relative_to(base) and len(path.relative_to(base).parts) <= 3 for base in ROOTS):
        return 'outside_note_depth'
    return None


if __name__ == '__main__':
    with contextlib.redirect_stdout(io.StringIO()):
        inv = record.capture('03_filename_inventory', ['rg', '--files', '-g', '*.md'] + [str(p) for p in ROOTS], [SELF])
    assert inv.returncode == 0
    all_paths = sorted(set(pathlib.Path(s) for s in inv.stdout.decode().splitlines()))
    selected = []
    denied = {}
    for path in all_paths:
        reason = exclude(path)
        if reason:
            denied[reason] = denied.get(reason, 0) + 1
        else:
            selected.append(path)
    record.save(record.OWN / 'DISCOVERY_SCOPE.json', dict(metadata_paths=len(all_paths),
        selected_paths=[str(p) for p in selected], denied_counts=denied,
        role='entire_pathset_filtered_before_body_search'))
    pattern = 'solitaire|chip[- ]fir|load[- ]balanc|allocat|pile|redistribut|sink.{0,15}revers|source.{0,15}revers|revers.{0,15}sink|greedy'
    with contextlib.redirect_stdout(io.StringIO()):
        result = record.capture('04_scoped_body_search', ['rg', '-n', '-i', pattern, '--'] + [str(p) for p in selected],
            [SELF, record.OWN / 'DISCOVERY_SCOPE.json'] + selected)
    assert result.returncode in (0, 1)
    print(dict(metadata_paths=len(all_paths), selected_bodies=len(selected),
               hit_lines=len(result.stdout.splitlines()), exits=[inv.returncode, result.returncode],
               full_argv_and_streams='commands/03_filename_inventory and commands/04_scoped_body_search'))
