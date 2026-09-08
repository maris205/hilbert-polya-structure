"""Adopt exact actual producer bytes; pin proof before other canonical reading."""
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

report = json.loads((HERE / 'produce01/REPORT.json').read_bytes())
assert report['status'] == 'PASS'
source = HERE / 'produce01/commands/run_1/stdout'
data = json.loads(source.read_bytes())
assert data['states'] == 4095
with (HERE / 'CANONICAL.json').open('xb') as out:
    out.write(source.read_bytes())
assert (HERE / 'CANONICAL.json').read_bytes() == source.read_bytes()
record = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'author_A_verifier_or_canonical_body_semantics_read': False,
          'actual_producer': str(source), 'states': data['states'], 'checks': data['checks'],
          'pins': {n: digest(HERE / n) for n in ['verify.py', 'verify.committed.py',
              'PARAMETERS.json', 'INDEPENDENT_PROOF.md', 'CANONICAL.json', 'capture_canonical.py']}}
with (HERE / 'PRE_COMPARISON_PROOF_CODE_COMMITMENT.actual.json').open('x') as out:
    json.dump(record, out, sort_keys=True, indent=2)
    out.write('\n')
print(json.dumps(record, sort_keys=True))
