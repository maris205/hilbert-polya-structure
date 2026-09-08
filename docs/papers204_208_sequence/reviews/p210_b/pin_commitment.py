"""Create the actual pre-semantic-reading input/source commitment."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = ROOT / 'docs/papers204_208_sequence/reviews/p210_b'
FROZEN = ROOT / 'papers/210-weakly-increasing-run-aggregation/frozen_round1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


files = sorted(p for p in FROZEN.rglob('*') if p.is_file())
assert len(files) == 509
assert sha(FROZEN / 'SHA256SUMS') == 'be54b79806d90f22037cee877f92074e744b2ef27bcc0b6b2e4f8dfa658446e0'
for line in (FROZEN / 'SHA256SUMS').read_text().splitlines():
    digest, relative = line.split('  ', 1)
    assert sha(FROZEN / relative) == digest
pins = OUT / 'INPUT_PINS.sha256'
assert not pins.exists()
pins.write_text(''.join(f'{sha(p)}  {p.relative_to(ROOT)}\n' for p in files))
names = ['verify.py', 'PARAMETERS.json', 'INDEPENDENCE_COMMITMENT.md',
         'pin_commitment.py', 'INPUT_PINS.sha256']
record = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'physical_inputs': len(files), 'freeze_manifest': sha(FROZEN / 'SHA256SUMS'),
          'semantic_author_A_code_or_canonical_read': False,
          'files': {name: sha(OUT / name) for name in names}}
target = OUT / 'COMMITMENT.actual.json'
assert not target.exists()
target.write_text(json.dumps(record, sort_keys=True, indent=2) + '\n')
print(json.dumps(record, sort_keys=True))
