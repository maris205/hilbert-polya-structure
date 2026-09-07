#!/usr/bin/env python3
"""Print a bounded documentary capture; never execute scientific models."""
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OWN = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_thirty_fifth'
INPUTS = {
 'algebraic_C8_SCOUT.md': 'docs/papers122_126_sequence/scouting/algebraic/SCOUT.md',
 'eleventh_INTAKE.md': 'docs/papers204_208_sequence/scouting/finite_systems_eleventh/INTAKE.md',
 'eleventh_PROOF_AND_DISPOSITION.md': 'docs/papers204_208_sequence/scouting/finite_systems_eleventh/PROOF_AND_DISPOSITION.md',
 'eleventh_SOURCE_AND_COLLISION.md': 'docs/papers204_208_sequence/scouting/finite_systems_eleventh/SOURCE_AND_COLLISION.md',
 'twenty_third_INTAKE.md': 'docs/papers204_208_sequence/scouting/finite_systems_twenty_third/INTAKE.md',
}
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
assert Path.cwd() == ROOT
records = []
for name, rel in INPUTS.items():
    p = ROOT / rel
    assert p.is_file() and not p.is_symlink() and p.resolve() == p
    raw = p.read_bytes()
    assert raw.endswith(b'\n')
    records.append({'original_path': str(p), 'snapshot_path': 'original_snapshot/' + name,
                    'sha256': sha256(raw).hexdigest(), 'bytes': len(raw), 'text': raw.decode()})
for row in records:
    assert sha256(Path(row['original_path']).read_bytes()).hexdigest() == row['sha256']
print(json.dumps({'schema': 'scout35-direct-original-capture-v1',
                  'scope': 'Five named original text files only, no descendant traversal; not a scientific run.',
                  'inputs': records}, indent=2, sort_keys=True))
