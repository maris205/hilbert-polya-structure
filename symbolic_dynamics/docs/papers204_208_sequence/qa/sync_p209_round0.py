#!/usr/bin/env python3
"""Scoped no-deletion workspace-to-private-mirror checkpoint copy.

Only the fixed owned paths below are copied. No Git command is issued here;
root checks/stages explicit returned paths and verifies committed objects.
Active P209 A and twenty-sixth scouting are excluded.
"""
from hashlib import sha256
import json
from pathlib import Path
import shutil

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
BATCH = 'docs/papers204_208_sequence/'
DIRECTORIES = (
    'papers/209-ordered-fibre-threading',
    BATCH + 'scouting/finite_systems_twenty_third',
    BATCH + 'scouting/finite_systems_twenty_fourth',
    BATCH + 'scouting/finite_systems_twenty_fifth',
    BATCH + 'scouting/ORR_SECOND_CLOCK_ATTEMPT',
    BATCH + 'qa/p209_author_root_preparation',
    BATCH + 'qa/root_replays/p209_author_strict',
    BATCH + 'qa/scout25_documentary_audit',
    BATCH + 'qa/central_lifecycle_p209_round0',
    BATCH + 'qa/central_lifecycle_scout25',
)
FILES = (
    'SYMBOLIC_DYNAMICS_STATE.md',
    BATCH + 'PIPELINE_STATE.md', BATCH + 'FINAL_THEOREM_CONTRACTS.md',
    BATCH + 'GIT_SYNC_RECEIPT.md',
    BATCH + 'scouting/TWENTY_THIRD_ROOT_INSPECTION.md',
    BATCH + 'scouting/TWENTY_FOURTH_ROOT_INSPECTION.md',
    BATCH + 'scouting/TWENTY_FIFTH_ROOT_INSPECTION.md',
    BATCH + 'scouting/ORR_ROOT_CLOCK_BOUNDARY.md',
    BATCH + 'scouting/ORR_SECOND_ROOT_INSPECTION.md',
    BATCH + 'qa/SCOUT23_ROOT_INSPECTION.actual.json',
    BATCH + 'qa/SCOUT24_ROOT_INSPECTION.actual.json',
    BATCH + 'qa/SCOUT25_ROOT_INSPECTION.actual.json',
    BATCH + 'qa/GIT_OBJECT_P208_COMPLETE_2EBE9F4E.json',
    BATCH + 'qa/P209_ROOT_CONTEXT_INSPECTION.actual.json',
    BATCH + 'qa/P209_AUTHOR_PAIR_ROOT_INSPECTION.actual.json',
    BATCH + 'qa/P209_AUTHOR_BUILDS_ROOT_INSPECTION.actual.json',
    BATCH + 'qa/P209_AUTHOR_ROOT_VIEWS.md',
    BATCH + 'qa/P209_FINAL_AUTHOR_ROOT_INSPECTION.actual.json',
    BATCH + 'qa/P209_ROOT_AUTHOR_STRICT_REPLAY.actual.json',
    BATCH + 'qa/P209_ROOT_AUTHOR_STRICT_REPLAY.md',
    BATCH + 'qa/P209_ROUND0_FREEZE.actual.json',
    BATCH + 'qa/P209_ROUND0_ROOT_CLOSURE.actual.json',
    BATCH + 'qa/P209_ROUND0_ROOT_INSPECTION.md',
    BATCH + 'qa/inspect_p209_author_builds.py',
    BATCH + 'qa/freeze_p209_round0.py',
    BATCH + 'qa/sync_p209_round0.py',
)


def digest(p):
    assert p.is_file() and not p.is_symlink(), str(p)
    h = sha256()
    with p.open('rb') as f:
        for data in iter(lambda: f.read(1024 * 1024), b''):
            h.update(data)
    return h.hexdigest()


def main():
    assert (MIRROR / '.git').is_dir() and not (ROOT / '.git').exists()
    names = set(FILES)
    for rel in DIRECTORIES:
        base = ROOT / rel
        assert base.is_dir() and not base.is_symlink()
        entries = list(base.rglob('*'))
        assert all(not p.is_symlink() for p in entries)
        names.update(p.relative_to(ROOT).as_posix() for p in entries if p.is_file())
    assert all(not x.startswith((BATCH + 'reviews/p209_a/',
                                BATCH + 'scouting/finite_systems_twenty_sixth/')) for x in names)
    before = {name: digest(ROOT / name) for name in sorted(names)}
    changed = []
    for name, value in before.items():
        target = MIRROR / name
        assert not target.is_symlink()
        if target.exists() and digest(target) == value:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
        changed.append(name)
    assert {name: digest(ROOT / name) for name in before} == before
    assert {name: digest(MIRROR / name) for name in before} == before
    print(json.dumps({'status': 'PASS_SCOPED_COPY_NO_DELETIONS',
                      'selected_files': len(names), 'copied_files': len(changed),
                      'selected_pins': before, 'copied_paths': changed,
                      'excluded': ['active P209 manuscript A and root A preflight',
                                   'active twenty-sixth scout', 'all unrelated paths'],
                      'boundary': 'No Git stage/commit/push by this command'},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
