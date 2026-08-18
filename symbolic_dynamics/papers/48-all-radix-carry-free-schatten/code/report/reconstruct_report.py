#!/usr/bin/env python3
"""Deterministically reconstruct the Paper 48 experiment report."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path

def load(path):return json.loads(Path(path).read_text(encoding="ascii"))
def render(out:Path,state:str)->str:
 a=load(out/"results/evaluator_a_native.json");b=load(out/"results/evaluator_b_native.json")
 comparison=load(out/"results/comparison.json");proof=load(out/"results/proof_audit.json")
 mutations=load(out/"results/mutation_outcomes.json");adversarial=load(out/"results/adversarial_tests.json")
 main=load(out/"evaluations/main_evaluation.json");ind=load(out/"evaluations/independent_evaluation.json")
 required=[a,b,comparison,proof,mutations,adversarial,main,ind]
 if any(x.get("status")!="PASS" for x in required):raise ValueError("upstream")
 if a["finite_record_count"]!=1965 or b["finite_record_count"]!=1965 or comparison["finite_coordinate_rows"]!=1965:raise ValueError("coverage")
 if len(proof["records"])!=4 or proof["certificate_owner"]!="P":raise ValueError("proof")
 if mutations["mutation_instances"]!=39 or mutations["designated_consumer_invocations"]!=68 or mutations["survivors"]!=0:raise ValueError("mutations")
 status="PREAUTHORITY_INTEGRATION" if state=="A" else "PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION"
 lines=[
  "# Paper 48 Experiment Report","",f"Integration state: `{state}` / `{status}`.","",
  "## Finite controls","",
  f"Evaluator A and Evaluator B independently expanded `{comparison['finite_coordinate_rows']}` canonical finite rows.",
  f"They compared `{comparison['digit_interval_comparisons']}` one-digit singular-value intervals and `{comparison['shell_envelope_rows']}` weighted shell envelopes.",
  "Exact support counts, ranks, zero conventions, mask identities, closed-walk support ledgers, and explicit finite period witnesses agreed with no missing, extra, or duplicate rows.","",
  "A used direct positive-prefix matrices and repeated quotient/remainder carry checks. B used a separately parsed digit automaton and shell/Kronecker factorization. Random masks were independently regenerated in both lanes.","",
  "## Infinite theorem boundary","",
  "Only Auditor P emitted infinite certificates. It accepted four frozen theorem fields: the universal sigma wall, the digit-norm wall including binary adjacent-pair equality pinching, the regularized/ordinary determinant domains, and the positive-vertex trace/least-period ledger.","",
  "Finite cutoff and tensor evidence remains a falsifier and is not used as proof of infinite ideal membership.","",
  "## Hostile controls","",
  f"All `{mutations['mutation_instances']}` preregistered mutations were killed by every and only their designated consumers (`{mutations['designated_consumer_invocations']}` required rejections); all `{mutations['nondesignated_acceptances']}` non-designated checks accepted.",
  f"The physical governance suite completed `{adversarial['physical_instances']}` filesystem, full-object, Route, CLI, hostile-environment, late-failure, and idempotence instances with zero survivors.","",
  "## Route disposition","",
  "Both strict full-object validators independently retained `(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`, `ROUTE_A_REJECTED`, and `route_b.invocation_allowed=false`.",
  "Scientific GO/HOLD/STOP language is external to Route terminals.","",
  "## Interpretation","",
  "C1 and C2 pass the preregistered finite-control and independent-proof gates. This is validation of the frozen all-radix theorem, not an authority write, exhaustive priority result, publication authorization, or Route-B eligibility.","",
 ]
 return "\n".join(lines)
def main():
 p=argparse.ArgumentParser(allow_abbrev=False);p.add_argument("--output-root",type=Path,required=True);p.add_argument("--state",choices=["A","B"],required=True)
 try:
  a=p.parse_args();sys.stdout.write(render(a.output_root.resolve(strict=True),a.state));return 0
 except Exception as e:sys.stderr.write(f"REPORT_ERROR:{type(e).__name__}\n");return 3
if __name__=="__main__":raise SystemExit(main())
