"""Supplemental capture of exact mechanism originals; no scientific mutations."""
from pathlib import Path
import hashlib
import json
import time
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
HERE=Path(__file__).resolve().parent
names='''docs/papers162_166_sequence/scouting/open_fresh_p167/SCOUT.md
docs/papers162_166_sequence/scouting/open_fresh_p167/verify_scout.py
docs/papers122_126_sequence/proof_spikes/COMB_PARITY_ROOT_ROTATION_REPORT.md
papers/144-leftmost-dyck-reassociation/references.bib
docs/papers204_208_sequence/scouting/graph_geometry_fourth/SCOUT_REPORT.md
docs/papers204_208_sequence/reviews/p204_a/SOURCE_AND_PROOF.md
docs/papers204_208_sequence/reviews/p206_a/SOURCE_AND_PROOF.md
docs/papers204_208_sequence/scouting/word_local/MNC_GATE/SOURCE_AND_PROOF.md
docs/papers204_208_sequence/scouting/word_local/UGR_GATE/SOURCE_AUDIT.md
papers/202-ternary-ordered-reset/main.tex
papers/139-lyndon-factor-start-feedback/main.tex
papers/205-conflict-triggered-cyclic-increments/PROOF_PACKAGE.md
papers/207-upper-neighbor-rank-dynamics/PROOF_PACKAGE.md
docs/research_state/HISTORY_AND_CAVEATS.md'''.splitlines()
assert all((ROOT/p).is_file() for p in names)
dest=HERE/'HISTORY_PINS.sha256'
assert not dest.exists()
payload=''.join(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in sorted(names))
dest.write_text(payload)
(HERE/'HISTORY_CAPTURE.json').write_text(json.dumps({'utc_epoch':time.time(),'count':len(names),'root':str(ROOT),'note':'Supplemental inputs discovered by mechanism. GCM, parity-root, P144 bib, graph_geometry fourth, P204 and P206 source/proof bodies were read before this successful supplemental capture; remaining named proofs captured before body reading. Earlier failed filename capture is preserved. This does not retroactively label the first production as checking these additional referents.'},indent=2)+'\n')
print(len(names),hashlib.sha256(payload.encode()).hexdigest())
