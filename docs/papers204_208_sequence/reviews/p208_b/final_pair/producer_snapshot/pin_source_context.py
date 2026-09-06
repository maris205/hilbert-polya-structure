"""Freeze exact read-context originals, without claiming all searched text read."""
from pathlib import Path
import hashlib
import json

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/reviews/p208_b'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
selected=[
 'papers/144-leftmost-dyck-reassociation/main.tex',
 'papers/90-rule184-particle-periodic-zeta/main.tex',
 'papers/139-lyndon-factor-start-feedback/main.tex',
 'papers/202-ternary-ordered-reset/main.tex',
 'papers/204-previous-smaller-distance-feedback/sections/01_setup.tex',
 'papers/204-previous-smaller-distance-feedback/sections/03_fibres.tex',
 'papers/206-ternary-cyclic-record-feedback/sections/02_dynamics.tex',
 'docs/papers122_126_sequence/proof_spikes/COMB_PARITY_ROOT_ROTATION_REPORT.md',
 'docs/papers117_121_sequence/scouting/COMBINATORIAL_PHASE2C_SCOUT.md',
 'docs/papers122_126_sequence/scouting/combinatorial/SCOUT.md',
 'docs/papers152_156_sequence/scouting/combinatorial/SCOUT.md',
 'docs/papers162_166_sequence/scouting/open_fresh_p167/SCOUT.md',
 'docs/papers204_208_sequence/scouting/word_local/MNC_GATE/SOURCE_AND_PROOF.md',
 'docs/papers204_208_sequence/scouting/word_local/UGR_GATE/SOURCE_AUDIT.md',
 'docs/papers204_208_sequence/reviews/p208_a/SOURCE_AND_PROOF.md',
 'docs/papers204_208_sequence/reviews/p208_a/REPORT.md',
 'docs/papers204_208_sequence/reviews/p208_a/FINDINGS.json',
 'docs/papers204_208_sequence/reviews/p208_a/DELTA_ACCEPTANCE.md',
 'docs/papers204_208_sequence/reviews/p208_a/SHA256SUMS',
 'docs/papers204_208_sequence/reviews/p208_a/verify.py',
 'docs/papers204_208_sequence/reviews/p208_a/CANONICAL.json']
out={}
for name in selected:
    original=ROOT/name
    target=BASE/'source_context'/name
    target.parent.mkdir(parents=True,exist_ok=True)
    before=sha(original)
    with target.open('xb') as f:f.write(original.read_bytes())
    assert before==sha(original)==sha(target)
    out[str(original)]={'sha256':before,'snapshot':str(target.relative_to(BASE))}
for branch in ('sources','history_context'):
    for p in sorted((BASE/branch).rglob('*')):
        if p.is_file():out[str(p)]={'sha256':sha(p),'snapshot':str(p.relative_to(BASE))}
with (BASE/'SOURCE_CONTEXT_PINS.json').open('x') as f:
    json.dump({'read_scope':'Selected read bodies and all machine-search evidence; individual limits are in SOURCE_AND_PROOF.md.',
               'paths':out},f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'source_context_paths':len(out),'new_original_snapshots':len(selected)},sort_keys=True))
