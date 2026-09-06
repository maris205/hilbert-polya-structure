"""One-time, root-relative input digest capture; never modifies inputs."""
from pathlib import Path
import hashlib
import json
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = Path(__file__).resolve().parent
scout = ROOT / 'docs/papers204_208_sequence/scouting'
inputs = set()
for name in ('order_geometry_tenth', 'order_geometry_tenth_desk'):
    inputs.update(p for p in (scout/name).rglob('*') if p.is_file())
for name in ('order_geometry_tenth/INPUTS.sha256', 'order_geometry_tenth_desk/INPUT_PINS.sha256', 'order_geometry_tenth_desk/AUTHOR_EVIDENCE_PINS.sha256'):
    for line in (scout/name).read_text().splitlines():
        if line.strip():
            inputs.add(ROOT / line.split('  ',1)[1])
for rel in ('papers/90-rule184-particle-periodic-zeta/main.tex',
            'docs/papers204_208_sequence/scouting/TENTH_ROOT_INSPECTION.md'):
    inputs.add(ROOT / rel)
dest = OUT/'INPUT_PINS.sha256'
assert not dest.exists()
payload = ''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(ROOT))+'\n' for p in sorted(inputs))
dest.write_text(payload)
(OUT/'INPUT_CAPTURE.json').write_text(json.dumps({'utc_epoch':time.time(),'count':len(inputs),'root':str(ROOT),'policy':'All original author and desk package files, including failed evidence and caches, plus referents of named root-relative pin lists; capture after instruction reading and initial author proof read, before any mathematical code or source work. No retrospective pre-read claim.','sha256':hashlib.sha256(payload.encode()).hexdigest()},indent=2)+'\n')
print(len(inputs),hashlib.sha256(payload.encode()).hexdigest())
