#!/usr/bin/env python3
"""Seal all physical payloads after actual outer audit evidence is complete."""
import hashlib
import json
from pathlib import Path

gate=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/scouting/MNA_GATE')
target=gate/'SHA256SUMS'
if target.exists():
    raise RuntimeError('refuse rewriting an existing final seal')
receipt=json.loads((gate/'evidence/outer_audit_final/receipt.json').read_text())
audit=json.loads((gate/'evidence/outer_audit_final/stdout.raw').read_text())
if receipt['exit']!=0 or audit['status']!='PASS':
    raise RuntimeError('final evidence audit did not actually pass')
payloads=sorted(p for p in gate.rglob('*') if p.is_file() and p!=target)
if any(p.is_symlink() for p in payloads):
    raise RuntimeError('no unresolved payload symlinks allowed')
rows=[]
for p in payloads:
    rows.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(gate)))
target.write_text('\n'.join(rows)+'\n')
for row in target.read_text().splitlines():
    sha,rel=row.split('  ',1)
    if hashlib.sha256((gate/rel).read_bytes()).hexdigest()!=sha:
        raise RuntimeError(('postseal_payload_mismatch',rel))
print(json.dumps({'status':'PASS','payloads':len(rows),'complete_nonself_coverage':True,
                  'sha256':hashlib.sha256(target.read_bytes()).hexdigest()},sort_keys=True))
