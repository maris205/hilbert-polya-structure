"""Scoped documentation link check; no paper or runtime action."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers211_215_sequence'
FILES = [ROOT/'SYMBOLIC_DYNAMICS_STATE.md', BATCH/'PIPELINE_STATE.md',
 BATCH/'PROBLEM_ANCHOR.md', BATCH/'qa/root_checkpoint_inspection02/RECEPTION.md']
FILES += [BATCH/'scouting/root_reception'/name for name in [
 'PARTITION_RUN_ERASURE_RECEPTION.md', 'LATTICE_PLANAR_RECEPTION.md',
 'KIP_ADMISSION_RECEPTION.md', 'control_kip_admission/README.md']]
results = []
for file in FILES:
    source = file.read_bytes()
    links = []
    for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',source.decode()):
        if target.startswith(('http:','https:','mailto:','#')):
            continue
        target = unquote(target.strip('<>').split('#',1)[0])
        path = Path(target) if target.startswith('/') else file.parent/target
        assert path.exists(), (str(file),target)
        links.append(str(path.resolve()))
    assert file.read_bytes() == source
    results.append({'path':str(file), 'sha256':hashlib.sha256(source).hexdigest(),
                    'bytes':len(source), 'local_links':links})
print(json.dumps({'status':'PASS_SCOPED_DOCUMENT_LINKS', 'documents':len(FILES),
 'local_links':sum(len(row['local_links']) for row in results), 'inputs':results,
 'new_science':0,'new_git':0},sort_keys=True))
