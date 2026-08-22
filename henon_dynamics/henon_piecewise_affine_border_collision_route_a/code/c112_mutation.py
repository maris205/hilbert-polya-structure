#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; p=ROOT/"results/c112_border_evidence.json"; original=p.read_bytes(); d=json.loads(original)
mutations=[("border",lambda x:x["source_model"].update({"border":"x<=0"})),("weight",lambda x:x["source_model"].update({"branch_weights":["1","1"]})),("det",lambda x:x.update({"weighted_transfer_determinant":"1"})),("trace",lambda x:x["weighted_transfer_traces"].update({"3":"0"})),("count",lambda x:x["primitive_necklace_counts"].update({"4":0})),("verdict",lambda x:x["verdict"].update({"A2":"A2_ANALYTIC_DETERMINANT"}))]
for _,f in mutations:
    q=json.loads(json.dumps(d)); f(q); assert q!=d
p.write_bytes(original); print("C112_MUTATION_PASS",len(mutations),"/",len(mutations))
