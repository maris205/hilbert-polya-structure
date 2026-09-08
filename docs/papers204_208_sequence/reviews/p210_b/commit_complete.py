"""Pin complete independent mathematical source before comparison access."""
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
path = HERE / 'COMPLETE_SOURCE_COMMITMENT.actual.json'
assert not path.exists()
record = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'prior_mathematical_read': 'Round1 PROOF_PACKAGE.md, SOURCE_AUDIT.md, references.bib, main.tex',
          'author_A_code_or_canonical_semantics_read': False,
          'change': 'Added explicit codec from mathematical definitions, not implementation',
          'files': {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                    for name in ['verify.py', 'PARAMETERS.json', 'INPUT_PINS.sha256',
                                 'COMMITMENT.actual.json', 'commit_complete.py']}}
(HERE / 'verify.committed.py').write_bytes((HERE / 'verify.py').read_bytes())
path.write_text(json.dumps(record, sort_keys=True, indent=2) + '\n')
print(json.dumps(record, sort_keys=True))
