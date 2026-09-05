#!/usr/bin/env python3
"""Canonical source-system AB receipt; finite checks are not completeness proofs."""
if not __debug__:
    raise RuntimeError("c383 producer refuses optimized Python")
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVALUATION = ROOT / "evaluations/route_a/HCS-C383/2026-09-05.yaml"
OUTPUT = ROOT / "results/c383_ab_evidence.json"
BASELINE = "0596f9d680277288225062a6fdd7ad7ce116e01d"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
BETAS = (F(0), F(1,7), F(1,4), F(1,3), F(1,2), F(2,3), F(3,4), F(6,7))
FLAGS = ("claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number", "claims_automorphy", "claims_target_divisor_or_counting_law", "claims_target_functional_equation", "claims_target_zero_match", "claims_hilbert_polya_operator", "invokes_route_b")

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()

def fraction(x):
    return [x.numerator, x.denominator]

def decimal(x):
    return mp.nstr(x, 40, min_fixed=0, max_fixed=0)

def produce():
    channels = []
    gauges = []
    symmetries = []
    cutoffs = []
    for beta in BETAS:
        for m in range(-32, 33):
            nu = abs(m-beta)
            channels.append({"beta": fraction(beta), "m": m, "nu": fraction(nu), "phase_over_pi": fraction(F(abs(m))-nu), "limit_circle": nu < 1})
        for n in range(-2, 3):
            for m in range(-8, 9):
                gauges.append({"beta": fraction(beta), "shift": n, "m": m, "shifted_m": m+n, "shifted_beta": fraction(beta+n), "order": fraction(abs(m-beta))})
        symmetries.append({"beta": fraction(beta), "position_preserving_TR": (2*beta).denominator == 1, "required_winding": fraction(2*beta), "reflection_K_symmetry": True})
        for cutoff in range(65):
            symmetric = sum((F(abs(m))-abs(m-beta) for m in range(-cutoff,cutoff+1)), F(0))
            shifted = sum((F(abs(m))-abs(m-beta) for m in range(-cutoff,cutoff+2)), F(0))
            cutoffs.append({"beta": fraction(beta), "M": cutoff, "symmetric_phase_over_pi": fraction(symmetric), "shifted_phase_over_pi": fraction(shifted)})
    hp = []
    with mp.workdps(85):
        for nu, r, rp, t in ((F(0),F(1),F(1),F(1)),(F(1,7),F(1),F(2),F(1)),(F(1,2),F(2),F(1),F(1,2)),(F(2,3),F(1,2),F(3,2),F(2)),(F(3),F(1),F(2),F(3,2)),(F(7,2),F(2),F(2),F(1))):
            n,a,b,c = [mp.mpf(x.numerator)/x.denominator for x in (nu,r,rp,t)]
            closed = mp.exp(-(a*a+b*b)/(4*c))*mp.besseli(n,a*b/(2*c))/(2*c)
            hp.append({"nu":fraction(nu),"r":fraction(r),"rp":fraction(rp),"t":fraction(t),"radial_heat_kernel":decimal(closed)})
        amplitudes=[]
        for beta in (F(1,7),F(1,2),F(6,7)):
            for theta_pi in (F(1,4),F(1,2),F(1),F(3,2)):
                b=mp.mpf(beta.numerator)/beta.denominator
                th=mp.pi*theta_pi.numerator/theta_pi.denominator
                cross=mp.sin(mp.pi*b)**2/(2*mp.pi*mp.sin(th/2)**2)
                amplitudes.append({"beta":fraction(beta),"theta_over_pi":fraction(theta_pi),"k":[1,1],"cross_section":decimal(cross)})
    raw=EVALUATION.read_bytes()
    evaluation=yaml.safe_load(raw)
    obj={"schema":"hcs-c383-ab-v1","candidate_id":"HCS-C383","obstruction_id":"HEN-O367","source_commit":BASELINE,"fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"evaluator":{"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":AUTHORITY_SHA},"route_a_yaml":{"path":"evaluations/route_a/HCS-C383/2026-09-05.yaml","raw_sha256":hashlib.sha256(raw).hexdigest(),"semantic_sha256":hashlib.sha256(canonical(evaluation)).hexdigest()},"route_a":{"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_UNITARY_OR_SCATTERING_CANDIDATE"],"overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"channels":channels,"gauge_rows":gauges,"time_reversal_rows":symmetries,"cutoff_rows":cutoffs,"heat_rows":hp,"cross_section_rows":amplitudes,"counts":{"channels":len(channels),"gauges":len(gauges),"time_reversal":len(symmetries),"cutoffs":len(cutoffs),"heat":len(hp),"cross_section":len(amplitudes)},"theorem_boundary":"Friedrichs extension only; all-channel completeness is analytic; finite decimal checks are numerical regression, not interval certification; no ordinary global heat trace or ordinary Fredholm scattering determinant; no Hilbert-Polya operator and no Route B"}
    obj["payload_sha256"]=hashlib.sha256(canonical(obj)).hexdigest()
    return obj

def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=OUTPUT);a=p.parse_args()
    blob=json.dumps(produce(),sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False).encode()+b"\n"
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(blob)
    print("C383 producer PASS",hashlib.sha256(blob).hexdigest())

if __name__=="__main__":main()
