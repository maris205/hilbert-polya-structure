#!/usr/bin/env python3
"""Explicit owned no-deletion private-mirror copy; never stages or pushes."""
from hashlib import sha256
import json
from pathlib import Path
import shutil

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
B = 'docs/papers204_208_sequence/'
DIRECTORIES = (
    'papers/209-ordered-fibre-threading',
    B + 'reviews/p209_a',
    B + 'scouting/finite_systems_twenty_sixth',
    B + 'scouting/finite_systems_twenty_seventh',
    B + 'qa/p209_a_root_preparation',
    B + 'qa/root_replays/p209_a_strict',
    B + 'qa/p209_round1_preparation',
    B + 'qa/p209_round1_preparation_v2',
    B + 'qa/central_lifecycle_p209_a',
    B + 'qa/central_lifecycle_p209_round1',
    B + 'qa/central_lifecycle_p209_20260907',
)
FILES = ('SYMBOLIC_DYNAMICS_STATE.md',) + tuple(B + name for name in (
    'PIPELINE_STATE.md', 'GIT_SYNC_RECEIPT.md', 'P209_A_RESPONSE.md',
    'scouting/TWENTY_SIXTH_ROOT_INSPECTION.md',
    'scouting/TWENTY_SEVENTH_ROOT_INSPECTION.md',
    'qa/GIT_OBJECT_P209_ROUND0_F8EE398C.json',
    'qa/P209_A_ROOT_PAIR_PREPARATION.actual.json',
    'qa/P209_A_ROOT_INITIAL_INSPECTION.actual.json',
    'qa/P209_A_ROOT_INITIAL_INSPECTION.md',
    'qa/P209_A_ROOT_PAIR_INSPECTION.actual.json',
    'qa/P209_A_ROOT_PREEXECUTION.actual.json',
    'qa/P209_A_EXACT_NOCHANGE_CHECK.actual.json',
    'qa/P209_A_SUBMITTED_CURRENT_LINKS.actual.json',
    'qa/P209_A_ROOT_DELTA_INSPECTION.md',
    'qa/P209_A_ROOT_DELTA_INSPECTION.actual.json',
    'qa/P209_A_ROOT_DELTA_INSPECTION.execution.json',
    'qa/inspect_p209_a_initial.py', 'qa/inspect_p209_a_root_pair.py',
    'qa/inspect_p209_a_delta.py',
    'qa/P209_ROUND1_ROOT_INSPECTION.md',
    'qa/P209_ROUND1_ROOT_INSPECTION.actual.json',
    'qa/P209_ROUND1_FREEZE.execution.json',
    'qa/P209_ROUND1_PREFLIGHT.actual.json',
    'qa/P209_ROUND1_LIFECYCLE.actual.json',
    'qa/inspect_p209_round1_root.py', 'qa/preflight_p209_round1_root.py',
    'qa/inspect_p209_round1_lifecycle.py',
    'qa/SCOUT26_ROOT_INSPECTION.actual.json',
    'qa/SCOUT26_POST_LIFECYCLE_MAPPING.actual.json',
    'qa/SCOUT27_ROOT_INSPECTION.actual.json',
    'qa/SCOUT27_ROOT_INSPECTION_v1.execution.json',
    'qa/inspect_scout27_root.py', 'qa/inspect_scout27_root_v2.py',
    'qa/P209_ROUND1_CURRENT_LINKS.actual.json',
    'qa/sync_p209_round1.py',
))
RECORD = B + 'qa/P209_ROUND1_SCOPED_COPY.actual.json'
FORBIDDEN = (B+'reviews/p209_b/', B+'scouting/finite_systems_twenty_eighth/',
             B+'scouting/finite_systems_twenty_ninth/')

def digest(path):
    assert path.is_file() and not path.is_symlink(), str(path)
    h = sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()

def main():
    assert (MIRROR/'.git').is_dir() and not (ROOT/'.git').exists()
    assert not (ROOT/RECORD).exists() and not (MIRROR/RECORD).exists()
    names = set(FILES)
    for rel in DIRECTORIES:
        base = ROOT/rel
        assert base.is_dir() and not base.is_symlink()
        contents = list(base.rglob('*'))
        assert all(not p.is_symlink() for p in contents)
        names.update(p.relative_to(ROOT).as_posix() for p in contents if p.is_file())
    assert not any(name.startswith(FORBIDDEN) for name in names)
    before = {name:digest(ROOT/name) for name in sorted(names)}
    changed = []
    for name,value in before.items():
        target = MIRROR/name
        assert not target.is_symlink()
        if target.exists() and digest(target)==value:
            continue
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/name,target)
        changed.append(name)
    assert {name:digest(ROOT/name) for name in before}==before
    assert {name:digest(MIRROR/name) for name in before}==before
    record = {'status':'PASS_SCOPED_COPY_NO_DELETIONS',
        'selected_files':len(names),'copied_files':len(changed),
        'selected_pins':before,'copied_paths':changed,
        'stage_scopes':list(DIRECTORIES)+list(FILES)+[RECORD],
        'excluded':list(FORBIDDEN)+['all unrelated workspace/mirror paths'],
        'record_role':'Generated after successful copy; deliberately not a referent of its own selected_pins. Its measured hash is emitted by the actual command.',
        'boundary':'No Git stage/commit/push or new scientific verification by this command.'}
    with (ROOT/RECORD).open('x') as stream:
        json.dump(record,stream,indent=2,sort_keys=True)
        stream.write('\n')
    shutil.copyfile(ROOT/RECORD,MIRROR/RECORD)
    assert digest(ROOT/RECORD)==digest(MIRROR/RECORD)
    print(json.dumps({'status':record['status'],'selected_files':len(names),
        'copied_files':len(changed),'actual_record_path':str(ROOT/RECORD),
        'actual_record_sha256':digest(ROOT/RECORD),'excluded':record['excluded'],
        'boundary':record['boundary']},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
