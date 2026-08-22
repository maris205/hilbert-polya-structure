#!/usr/bin/env python3
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; p=ROOT/"results/c112_border_evidence.json"; b=p.read_bytes(); d=json.loads(b)
assert d["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER" and d["primitive_rows"]
assert sha256((json.dumps(d,sort_keys=True,indent=2)+"\n").encode()).hexdigest()==sha256(b).hexdigest()
print("C112_REPLAY_PASS",sha256(b).hexdigest())
