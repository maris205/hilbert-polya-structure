"""Preserve unexecuted first draft before correcting static schema findings."""
from pathlib import Path
import hashlib
import json
import shutil

BASE=Path(__file__).resolve().parent
target=BASE/'draft_history'/'unexecuted_01'
target.mkdir(parents=True)
rows={}
for name in ('audit_p209.py','p209_specific.py.fragment'):
    source=BASE/name
    raw=source.read_bytes()
    shutil.copyfile(source,target/name)
    assert (target/name).read_bytes()==raw
    rows[name]={'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
with (target/'ROLE.json').open('x') as stream:
    json.dump({'status':'UNEXECUTED_STATIC_DRAFT','files':rows,
      'finding':'A preserved failed attempt records completion_result.exit_code, not top-level exit_code.',
      'auditor_executions':0},stream,sort_keys=True,indent=2);stream.write('\n')
print(json.dumps({'status':'PASS_EXACT_UNEXECUTED_DRAFT_PRESERVATION','files':rows},sort_keys=True))
