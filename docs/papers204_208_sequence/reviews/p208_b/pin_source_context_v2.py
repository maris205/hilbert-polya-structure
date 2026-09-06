"""Correct a documentary pathname; retain old script and partial snapshots."""
from pathlib import Path
import ast
import hashlib
import json
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/reviews/p208_b'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
tree=ast.parse((BASE/'pin_source_context.py').read_text())
selected=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign)
              and any(isinstance(t,ast.Name) and t.id=='selected' for t in n.targets))
selected=[p.replace('/DELTA_ACCEPTANCE.md','/DELTA.md') for p in selected]
assert all((ROOT/p).is_file() for p in selected)
out={};reused=0
for name in selected:
    original=ROOT/name;target=BASE/'source_context'/name;before=sha(original)
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():assert sha(target)==before;reused+=1
    else:
        with target.open('xb') as f:f.write(original.read_bytes())
    assert before==sha(original)==sha(target)
    out[str(original)]={'sha256':before,'snapshot':str(target.relative_to(BASE))}
for branch in ('sources','history_context'):
    for p in sorted((BASE/branch).rglob('*')):
        if p.is_file():out[str(p)]={'sha256':sha(p),'snapshot':str(p.relative_to(BASE))}
with (BASE/'SOURCE_CONTEXT_PINS.json').open('x') as f:
    json.dump({'read_scope':'Selected read bodies and all machine-search evidence; individual limits are in SOURCE_AND_PROOF.md.',
               'paths':out},f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'source_context_paths':len(out),'original_snapshots':len(selected),
                  'verified_partial_snapshots_reused':reused,'status':'PASS'},sort_keys=True))
