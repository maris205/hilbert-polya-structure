#!/usr/bin/env python3
"""Deterministic exact certificate for the one-species Monod chemostat."""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

SOURCE_COMMIT="b89544f1f7b1043f4158dfdf9db77787b332f146"
EVALUATOR_SHA256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; FIXED_EPOCH=1788048000
ROOT=Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT=ROOT/"results/c254_monod_evidence.json"

CASES=[
 ("survival_01",F(1),F(10),F(3),F(2),F(2)),
 ("survival_02",F(1,2),F(4),F(2),F(1),F(3)),
 ("survival_03",F(2,3),F(5),F(3,2),F(2),F(5,2)),
 ("survival_04",F(3,4),F(7),F(2),F(3),F(4)),
 ("survival_05",F(1,5),F(2),F(5,4),F(1,2),F(3,2)),
 ("survival_06",F(4,3),F(9),F(3),F(1),F(2)),
 ("critical_01",F(1),F(1),F(2),F(1),F(2)),
 ("critical_02",F(2),F(2),F(3),F(1),F(3)),
 ("critical_03",F(1),F(3),F(2),F(3),F(4)),
 ("critical_04",F(2),F(4),F(5,2),F(1),F(5)),
 ("critical_05",F(1),F(1,2),F(3),F(1),F(3,2)),
 ("critical_06",F(1),F(5),F(6,5),F(1),F(7,3)),
 ("washout_01",F(2),F(1),F(2),F(1),F(2)),
 ("washout_02",F(3,2),F(2),F(2),F(2),F(3)),
 ("washout_03",F(1),F(1),F(3,2),F(1),F(4)),
 ("washout_04",F(4),F(5),F(3),F(1),F(5,2)),
 ("washout_05",F(2,3),F(1),F(1),F(1),F(3,2)),
 ("washout_06",F(5,4),F(3),F(2),F(3),F(2)),
]

def qt(x:F|int)->str:
 x=x if isinstance(x,F) else F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def ph(d:dict)->str:
 b=dict(d); b.pop("payload_sha256",None)
 return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def row(case):
 cid,D,Sin,mumax,K,Y=case
 muf=mumax*Sin/(K+Sin); delta=muf-D; threshold=mumax*Sin-D*(K+Sin)
 regime="survival" if threshold>0 else "critical" if threshold==0 else "washout"
 muprime=mumax*K/(K+Sin)**2
 out={"case_id":cid,"D":qt(D),"S_in":qt(Sin),"mu_max":qt(mumax),"K":qt(K),"Y":qt(Y),
      "mu_feed":qt(muf),"growth_margin":qt(delta),"threshold_numerator":qt(threshold),"regime":regime,
      "washout_equilibrium":[qt(Sin),"0"],"washout_eigenvalues":[qt(-D),qt(delta)],
      "washout_charpoly":["1",qt(D-delta),qt(-D*delta)],"mu_prime_feed":qt(muprime),
      "positive_equilibrium":None,"positive_qx_eigenvalues":None,"positive_charpoly":None,
      "leaf_implicit_coefficients":None,"critical_leaf_asymptotic_coefficient":None,
      "proof_role":"exact rational convention receipt; global convergence is proved analytically"}
 if regime=="survival":
  Sstar=D*K/(mumax-D); xstar=Sin-Sstar; Xstar=Y*xstar
  mp=mumax*K/(K+Sstar)**2; rate=xstar*mp
  out["positive_equilibrium"]=[qt(Sstar),qt(Xstar)]
  out["positive_qx_eigenvalues"]=[qt(-D),qt(-rate)]
  out["positive_charpoly"]=["1",qt(D+rate),qt(D*rate)]
  out["leaf_implicit_coefficients"]={"x_star":qt(xstar),"A":qt(mumax-D),"log_x":qt((K+Sin)/xstar),"minus_log_abs_xstar_minus_x":qt((K+Sstar)/xstar)}
 elif regime=="critical":
  out["critical_leaf_asymptotic_coefficient"]=qt(1/muprime)
 return out

def build():
 rows=[row(c) for c in CASES]
 data={
  "schema":"hcs-c254-monod-chemostat-threshold-v1","candidate_id":"HCS-C254","evaluation_date":"2026-08-31",
  "source_commit":SOURCE_COMMIT,"fixed_epoch":FIXED_EPOCH,"scope_literal":SCOPE,
  "evaluator":{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR_SHA256},
  "headline":"The positive one-species Monod chemostat has an exact total-nutrient reduction, a complete washout/critical/survival threshold atlas, and a closed invariant-leaf transient law.",
  "frozen_object":{"phase_space":"S>=0, X>=0","dynamics":"S'=D(S_in-S)-mu(S)X/Y; X'=(mu(S)-D)X; mu(S)=mu_max S/(K+S)","parameters":"D,S_in,mu_max,K,Y>0; nonnegative initial state","clock":"physical culture time","normalization":"x=X/Y and Q=S+x","arithmetic_origin":"none; source-local continuous-culture ODE","determinant_convention":"none","forbidden_data":"target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, functional equations, Hilbert--Polya operators"},
  "theorem":{
   "positivity_and_total":"The nonnegative quadrant is forward invariant and Q=S+X/Y satisfies Q'=D(S_in-Q), hence Q(t)=S_in+(Q0-S_in)e^{-Dt} and every solution is global and bounded.",
   "threshold":"The sign of mu(S_in)-D, equivalently mu_max S_in-D(K+S_in), gives survival, critical, or washout.",
   "survival":"If D<mu(S_in), then S*=DK/(mu_max-D)<S_in and X*=Y(S_in-S*). Every solution with X0>0 converges to (S*,X*); the invariant boundary X0=0 converges to washout.",
   "washout":"If D>=mu(S_in), every solution converges to (S_in,0). At strict inequality the approach is hyperbolic; equality is the transcritical critical face.",
   "invariant_leaf":"On Q=S_in, x=X/Y obeys x'=(mu_max-D)x(x*-x)/(K+S_in-x). For x*!=0 its separated logarithmic law is exact; at x*=0, (K+S_in)/x+log x=(mu_max-D)t+C and x~1/(mu'(S_in)t).",
   "linearization":"At washout the eigenvalues are -D and mu(S_in)-D. At survival, in (Q,x) coordinates they are -D and -(S_in-S*)mu'(S*).",
   "no_recurrence":"A periodic trajectory forces Q=S_in; the remaining scalar equation has no nonconstant periodic solution. Thus all recurrent states are equilibria.",
   "boundaries":"X0=0 is invariant; D=0 conserves Q and consumes substrate to zero when X0>0; mu_max=0 gives linear washout; S_in=0 converges to the origin. K=0 and Y=0 are singular model changes, not inferred by division.",
   "scope":"The theorem is an idealized data-free ODE statement, not biological parameter inference and not an arithmetic determinant."},
  "regression":{"rows":rows,"row_count":len(rows),"regime_counts":{"survival":6,"critical":6,"washout":6},"boundary_rows":[
    {"boundary":"X0=0","law":"X(t)=0; S(t)=S_in+(S0-S_in)e^{-Dt}"},
    {"boundary":"D=0, X0>0","law":"Q constant; S decreases to 0 and X increases to Y Q0"},
    {"boundary":"mu_max=0","law":"X=X0 e^{-Dt}; S=S_in+(S0-S_in)e^{-Dt}"},
    {"boundary":"S_in=0","law":"Q=Q0 e^{-Dt}, hence (S,X)->(0,0)"},
    {"boundary":"K=0 or Y=0","law":"singular model change; excluded from positive theorem"}],"boundary_row_count":5},
  "exact_identities":[
    "mu(S)=mu_max*S/(K+S)","Q=S+X/Y and Q'=D(S_in-Q)","threshold numerator=mu_max*S_in-D(K+S_in)",
    "S*=DK/(mu_max-D)","X*=Y(S_in-S*)","lambda_washout=(-D,mu(S_in)-D)",
    "lambda_survival=(-D,-(S_in-S*)mu'(S*))","x'=(mu_max-D)x(x*-x)/(K+S_in-x) on Q=S_in",
    "c log x-d log|x*-x|=(mu_max-D)t+C","critical law (K+S_in)/x+log x=(mu_max-D)t+C",
    "critical coefficient 1/mu'(S_in)","periodic Q implies Q=S_in","one-dimensional autonomous flow has no nonconstant cycle",
    "mu'(S)=mu_max*K/(K+S)^2"],
  "route_a":{"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False,"strongest_positive":"An all-positive-parameter global threshold theorem and exact invariant-leaf transient are closed.","strongest_failure":"The monotone chemostat has no nonconstant primitive cycles and no intrinsic rational-prime or determinant owner."},
  "scope_flags":{k:False for k in ["uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"]},
  "citations":[
   {"key":"Monod1949","claim":"source growth-response convention","source":"J. Monod, The Growth of Bacterial Cultures, Annual Review of Microbiology 3 (1949), 371--394","url":"https://doi.org/10.1146/annurev.mi.03.100149.002103"},
   {"key":"HsuHubbellWaltman1977","claim":"continuous-culture dynamical-systems context","source":"S. B. Hsu, S. Hubbell and P. Waltman, A Mathematical Theory for Single-Nutrient Competition in Continuous Cultures of Micro-Organisms, SIAM Journal on Applied Mathematics 32 (1977), 366--383","url":"https://doi.org/10.1137/0132030"},
   {"key":"SmithWaltman1995","claim":"authoritative chemostat model reference","source":"H. L. Smith and P. Waltman, The Theory of the Chemostat, Cambridge University Press (1995)","url":"https://doi.org/10.1017/CBO9780511530043"}],
  "nonclaims":["experimental calibration or biological prediction","a literature-priority or novelty claim","nonconstant primitive periodic orbits","a zeta/Fredholm or target determinant","arithmetic local data, target divisor, functional equation, or Hilbert--Polya operator"]}
 data["payload_sha256"]=ph(data); return data

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,default=DEFAULT_OUTPUT); a=ap.parse_args()
 a.output.parent.mkdir(parents=True,exist_ok=True); d=build(); a.output.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
 print(json.dumps({"status":"C254_PRODUCER_PASS","rows":d["regression"]["row_count"],"boundary_rows":d["regression"]["boundary_row_count"],"payload_sha256":d["payload_sha256"]},sort_keys=True))
if __name__=="__main__": main()
