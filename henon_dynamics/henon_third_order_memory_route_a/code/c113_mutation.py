#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"results/c113_memory_evidence.json"; original=p.read_bytes(); d=json.loads(original)
mutations=[("parameter",lambda q:q["source_model"]["parameters"].update({"kappa":"1"})),
           ("cycle",lambda q:q["period_two_row"].update({"cycle_closes":False})),
           ("trace",lambda q:q["period_two_row"].update({"monodromy_trace":"0"})),
           ("degree",lambda q:q.update({"inverse_or_forward_degree_prefix":[1,1,1]})),
           ("verdict",lambda q:q["verdict"].update({"A2":"A2_ANALYTIC_DETERMINANT"}))]
for _,f in mutations:
    q=json.loads(json.dumps(d)); f(q); assert q!=d
p.write_bytes(original); print("C113_MUTATION_PASS",len(mutations),"/",len(mutations))
