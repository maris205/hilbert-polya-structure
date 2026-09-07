#!/usr/bin/env python3
"""Bounded filename-first original scouting-note search, with pre-body filtering."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record

SELF = pathlib.Path(__file__).resolve()
ROOTS = [record.ROOT / 'docs' / batch / 'scouting' for batch in (
    'papers204_208_sequence', 'papers197_201_sequence', 'papers192_196_sequence',
    'papers187_191_sequence', 'papers172_176_sequence', 'papers157_161_sequence')]
NAMES = {'SCOUT.md', 'SCOUT_REPORT.md', 'SCOUT_AND_KILL_LEDGER.md', 'KILL_LEDGER.md',
         'INTAKE.md', 'PROOF_AND_DISPOSITION.md', 'PROOF_AND_ADAPTERS.md', 'PROOF_PACKAGE.md'}


def exclusion(path):
    if path.is_relative_to(record.OWN):
        return 'own_new_lane'
    if record.forbidden(path):
        return 'protected_or_mixed_path'
    parts = path.relative_to(record.ROOT).parts
    if any(part.lower() in {'inputs', 'controls', 'sources', 'commands', 'public_sources', 'discovery'}
           or part.lower().startswith(('evidence_capture', 'replay', 'source_only', 'strict_', 'input_', 'history_'))
           for part in parts):
        return 'copied_or_execution_artifact'
    if any(part.startswith(('ORR_', 'LNR_', 'NED_', 'LAST_SEAT_'))
           or part in {'finite_systems_thirty_third', 'finite_systems_thirty_fourth'} for part in parts):
        return 'explicit_old_task_exclusion'
    if path.name not in NAMES:
        return 'not_selected_note_basename'
    for base in ROOTS:
        if path.is_relative_to(base) and len(path.relative_to(base).parts) <= 3:
            return None
    return 'outside_direct_note_depth'


if __name__ == '__main__':
    inventory = record.capture('05_scoped_filename_inventory', ['rg', '--files', '-g', '*.md'] + [str(p) for p in ROOTS], [SELF])
    assert inventory.returncode == 0
    paths = sorted(set(pathlib.Path(line) for line in inventory.stdout.decode().splitlines()))
    selected = []
    denied = {}
    for p in paths:
        reason = exclusion(p)
        if reason:
            denied[reason] = denied.get(reason, 0) + 1
        else:
            selected.append(p)
    assert selected
    record.save(record.OWN / 'DISCOVERY_SCOPE.json', dict(roots=[str(p) for p in ROOTS], filenames_seen=len(paths),
        body_paths_selected=[str(p) for p in selected], denied_counts=denied,
        role='all_filtering_completed_before_body_rg'))
    pattern = 'run[- ]length|constant[- ]run|adjacent equal|equal adjacent|plateau|pointer[- ]jump|parent squar|grandparent|leaf.{0,18}(prun|promot|contract)|noncrossing.{0,18}closure|crossing.{0,18}merge|block.{0,18}cardinality'
    result = record.capture('06_scoped_body_search', ['rg', '-n', '-i', pattern, '--'] + [str(p) for p in selected], [SELF, record.OWN / 'DISCOVERY_SCOPE.json'] + selected)
    assert result.returncode in (0, 1)
    print('Selected note bodies:', len(selected), 'metadata paths:', len(paths), 'matching lines:', len(result.stdout.splitlines()))
