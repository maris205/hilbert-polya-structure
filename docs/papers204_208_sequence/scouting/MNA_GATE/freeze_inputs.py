#!/usr/bin/env python3
"""One-shot documentary preservation; no scientific computation."""
import hashlib
import json
from pathlib import Path
import shutil
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
GATE = ROOT / 'docs/papers204_208_sequence/scouting/MNA_GATE'
AUTHOR = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_fortieth'
EXPECTED = '807914fee97a2fa9380074688ad1ab803a601215e10011869f6a713075a9a55a'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    destination = GATE / 'inputs/author_lane40'
    destination.mkdir()
    original_manifest = AUTHOR / 'SHA256SUMS'
    if digest(original_manifest) != EXPECTED:
        raise ValueError('Original author manifest differs from assigned seal')
    roles = []
    lines = original_manifest.read_text().splitlines()
    if len(lines) != 155:
        raise ValueError(('author payload count', len(lines)))
    names = []
    for line in lines:
        sha, name = line.split('  ', 1)
        rel = Path(name)
        if rel.is_absolute() or '..' in rel.parts or name == 'SHA256SUMS':
            raise ValueError(('unsafe manifest name', name))
        names.append(name)
        original = AUTHOR / rel
        if digest(original) != sha:
            raise ValueError(('author payload mismatch', name))
        copied = destination / rel
        copied.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, copied)
        if copied.read_bytes() != original.read_bytes():
            raise ValueError(('raw copy mismatch', name))
        roles.append({'role':'frozen_author_payload', 'original':str(original),
                      'copy':str(copied), 'sha256':sha, 'bytes':copied.stat().st_size})
    actual = sorted(str(p.relative_to(AUTHOR)) for p in AUTHOR.rglob('*') if p.is_file() and p.name != 'SHA256SUMS')
    if sorted(names) != actual:
        raise ValueError('author nonself manifest coverage mismatch')
    shutil.copyfile(original_manifest, destination / 'SHA256SUMS')
    roles.append({'role':'author_manifest_at_original_author_base', 'original':str(original_manifest),
                  'copy':str(destination/'SHA256SUMS'), 'sha256':EXPECTED,
                  'bytes':original_manifest.stat().st_size})
    additional = [
      'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md',
      'docs/papers204_208_sequence/PROBLEM_ANCHOR.md',
      'docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md',
      'docs/papers162_166_sequence/scouting/replacement_crossclass/SCOUT.md',
      'docs/papers182_186_sequence/scouting/combinatorial_lane/SCOUT_AND_KILL_LEDGER.md',
      'docs/papers187_191_sequence/scouting/combinatorial_lane/CANDIDATES.md',
      'papers/147-adjacent-run-consolidation/main.tex',
      'papers/147-adjacent-run-consolidation/references.bib',
      'papers/121-random-product-plus-one-coalescence/main.tex',
      'papers/121-random-product-plus-one-coalescence/references.bib',
    ]
    for rel in additional:
        original = ROOT / rel
        copied = GATE / 'inputs/originals' / rel
        copied.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, copied)
        if original.read_bytes() != copied.read_bytes():
            raise ValueError(('historical raw mismatch', rel))
        roles.append({'role':'exact_contract_or_collision_original', 'original':str(original),
                      'copy':str(copied), 'sha256':digest(copied),'bytes':copied.stat().st_size})
    controls = {
      'AGENTS.md':'AGENTS.md',
      'SYMBOLIC_DYNAMICS_STATE.md':'SYMBOLIC_DYNAMICS_STATE.md',
      'PIPELINE_STATE.md':'docs/papers204_208_sequence/PIPELINE_STATE.md',
      'WORKFLOW.md':'docs/research_state/WORKFLOW.md',
      'SYMBOLIC_SKILL.md':'.agents/skills/symbolic-dynamics-research/SKILL.md',
    }
    for name, rel in controls.items():
        original, copied = ROOT/rel, GATE/'controls'/name
        roles.append({'role':'orientation_snapshot_not_current_live_alias', 'original':str(original),
                      'copy':str(copied),'sha256':digest(copied),'bytes':copied.stat().st_size,
                      'original_at_documentation_sha256':digest(original),
                      'raw_equal_at_documentation':original.read_bytes()==copied.read_bytes()})
    for skill in ['research-review','novelty-check']:
        original = Path('/root/autodl-tmp/.codex/skills') / ('skills-codex' if skill=='research-review' else '') / skill / 'SKILL.md'
        copied = GATE/'controls'/(skill+'_SKILL.md')
        shutil.copyfile(original,copied)
        roles.append({'role':'selected_skill', 'original':str(original),'copy':str(copied),
                      'sha256':digest(copied),'bytes':copied.stat().st_size})
    result = {'status':'PASS','role':'actual_documentary_freeze_not_science',
              'epoch':time.time(),'author_payloads':155,'roles':roles}
    (GATE/'INPUT_ROLES.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    # Input pins deliberately target exact physical copies, never mutable live controls.
    pins = []
    for row in roles:
        pins.append(row['sha256']+'  '+str(Path(row['copy']).relative_to(ROOT)))
    (GATE/'INPUT_PINS.sha256').write_text('\n'.join(sorted(pins))+'\n')
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
