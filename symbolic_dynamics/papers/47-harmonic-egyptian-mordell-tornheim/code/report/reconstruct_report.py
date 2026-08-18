#!/usr/bin/env python3
"""Mechanically reconstruct the canonical experiment report from results."""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from typing import Any
def c(v:Any)->bytes:return (json.dumps(v,sort_keys=True,indent=2,ensure_ascii=True,separators=(",",": "))+"\n").encode("ascii")
def pairs(s:list[tuple[str,Any]])->dict[str,Any]:
 o={}
 for k,v in s:
  if k in o:raise ValueError("duplicate")
  o[k]=v
 return o
def load(p:Path)->dict[str,Any]:
 raw=p.read_bytes();o=json.loads(raw.decode("ascii"),object_pairs_hook=pairs)
 if type(o) is not dict or raw!=c(o):raise ValueError("canonical")
 return o
def q(v:dict[str,int])->str:return f"{v['numerator']}/{v['denominator']}"
def main()->None:
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--output-root",required=True);a=p.parse_args()
 try:
  r=Path(a.output_root).resolve(strict=True)
  paths={"D":"results/evaluator_d.json","P":"results/evaluator_p.json","X":"results/exact_comparison.json","A":"audits/proof_result_audit.json","S":"audits/source_audit.json","T":"audits/type_audit.json","I":"audits/independence_audit.json","L":"audits/literature_audit.json","R1":"audits/route_primary.json","R2":"audits/route_independent.json","M":"tests/mutation_results.json","E":"tests/expanded_mutation_results.json","F":"audits/external_auditor_mutations.json"}
  obj={k:load(r/v) for k,v in paths.items()}
  if any(x.get("status")!="PASS" for x in obj.values()):raise ValueError("status")
  if obj["R1"]["payload"]!=obj["R2"]["payload"]:raise ValueError("route disagreement")
  d=obj["D"]["payload"];pobj=obj["P"]["payload"]
  edge_counts=[(x["N"],len(x["ordered_edges"]),len(x["loops"])) for x in d["cutoffs"]]
  trace=[x for x in d["trace_summary"] if x["N"]==128]
  if len(trace)!=2:raise ValueError("trace summary")
  checks=obj["X"]["payload"]["checks"]
  lines=["# Paper 47 exact integration report","","**Candidate:** SD-C49  ","**Evidence:** finite exact controls plus independently owned analytic certificates  ","**Status:** PASS","","## Independent support controls","","| N | ordered edges | loops |","|---:|---:|---:|"]
  lines += [f"| {n} | {e} | {l} |" for n,e,l in edge_counts]
  lines += ["","D constructed support only by `(mn) % (m+n) == 0`. P constructed it only from coprime-scale triples and constructed complete rows separately from divisors of `m^2`. Exact row, matrix, quotient, loop, and based-walk projections agree.","","## Exact traces at N=128","","| s | Tr A_N | Tr A_N^2 |","|---:|---:|---:|"]
  lines += [f"| {x['s']} | {q(x['trace_1_direct_diagonal'])} | {q(x['trace_2_direct_ordered_edges'])} |" for x in trace]
  lines += ["","The finite second trace uses the termwise `(a,b)` cutoff `floor(N/((a+b)max(a,b)))`; no finite zeta factor was extracted. The rectangular primitive/full MT controls are a separate domain.","","## Exact comparison checks",""]
  lines += [f"- `{k}`: {checks[k]}" for k in sorted(checks)]
  lines += ["","## Audits and adversarial controls","",f"- theorem/governance mutations: {obj['M']['payload']['instance_count']} instances, {obj['M']['payload']['consumer_invocation_count']} designated invocations, {obj['M']['payload']['survivors']} survivors",f"- expanded nested-schema mutations: {obj['E']['payload']['instance_count']} instances, {obj['E']['payload']['consumer_invocation_count']} designated invocations, {obj['E']['payload']['survivors']} survivors",f"- frozen-auditor mutations: {obj['F']['payload']['instance_count']} instances, {obj['F']['payload']['survivors']} survivors","- proof/source/type/independence/literature audits: PASS","- two full Route-v0.2 validators: byte-identical route SHA-256 and PASS","", "## Analytic and ownership boundary","","The phase walls `0, 1/2, 1`, compactness, determinant domains, and infinite zeta/MT identities are proof-certificate claims, not numerical extrapolations. Classical Egyptian parameterization and Mordell--Tornheim theory receive zero novelty credit. `STOP_DUPLICATE` remains a live external publication disposition and is not a Route terminal.","","Route A is rejected: graph cycles are not rational-prime primitives, no completed target divisor is supplied, and no fixed self-adjoint Hilbert--Polya lift is constructed.",""]
  sys.stdout.buffer.write("\n".join(lines).encode("ascii"))
 except Exception as e:sys.stderr.write(f"REPORT_ERROR:{type(e).__name__}\n");raise SystemExit(3)
if __name__=="__main__":main()
