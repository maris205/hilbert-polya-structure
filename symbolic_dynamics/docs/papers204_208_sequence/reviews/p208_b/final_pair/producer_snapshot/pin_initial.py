"""Capture immutable reviewed referents and prereading design, before science."""
import hashlib
import json
from pathlib import Path
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/reviews/p208_b'
FREEZE = ROOT / 'papers/208-original-snapshot-triangulation-sweeps/frozen_round1'
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
manifest = FREEZE / 'SHA256SUMS'
assert digest(manifest) == '12dca26eeb68503737846c633170bd427101648c21a9e89ef710d9ddaef01ace'
pins = {}
for line in manifest.read_text().splitlines():
    sha, name = line.split('  ', 1)
    p = FREEZE / name
    assert digest(p) == sha, name
    pins[str(p.relative_to(ROOT))] = sha
assert len(pins) == 487
pins[str(manifest.relative_to(ROOT))] = digest(manifest)
(BASE / 'INPUT_PINS.sha256').write_text(''.join(f'{h}  {p}\n' for p, h in sorted(pins.items())))
initial = {name: digest(BASE / name) for name in ('INITIAL_DESIGN.md', 'initial_kernel.py', 'pin_initial.py')}
context_names = ['AGENTS.md', 'SYMBOLIC_DYNAMICS_STATE.md',
    '.agents/skills/symbolic-dynamics-research/SKILL.md', 'docs/research_state/WORKFLOW.md',
    'docs/papers204_208_sequence/PIPELINE_STATE.md', 'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md',
    'docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md',
    'docs/papers204_208_sequence/qa/P208_A_ROOT_DELTA_INSPECTION.md',
    'docs/papers204_208_sequence/qa/P208_A_ROOT_DELTA_INSPECTION.actual.json',
    'docs/papers204_208_sequence/qa/P208_ROUND1_FREEZE.actual.json']
context = {}
for name in context_names:
    p = ROOT / name
    dest = BASE / 'assignment_context' / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(p.read_bytes())
    context[name] = {'before_sha256': digest(p), 'snapshot': str(dest.relative_to(BASE))}
record = {'time_utc': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
          'freeze_referents': len(pins)-1, 'freeze_manifest': digest(manifest),
          'initial_files': initial, 'assignment_context': context,
          'chronology': 'Written and pinned before first scientific execution and before author/A proof/code reads.'}
(BASE / 'INITIAL_PIN_RECORD.json').write_text(json.dumps(record, indent=2, sort_keys=True)+'\n')
print(json.dumps(record, sort_keys=True))
