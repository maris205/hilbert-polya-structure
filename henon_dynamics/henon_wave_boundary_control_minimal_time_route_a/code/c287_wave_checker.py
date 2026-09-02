#!/usr/bin/env python3
"""Independent d'Alembert/Fourier checker for HCS-C287."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c287_wave_evidence.json"
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
VALUES = (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3))
EXPECTED_THEOREM = {
    "revival": "the least positive full-energy wave-group identity time is 2L/c",
    "critical_identity": "at T=2L/c, integral |u_x(L,t)|^2 dt=4E(0)/c^3",
    "observability": "one-end observability holds for every T>=2L/c, equality included",
    "short_time_failure": "every T<2L/c misses a nonzero smooth periodic traveling profile",
    "hum": "duality gives exact L2 Dirichlet boundary control on the transposition state space at exactly the same threshold",
    "boundary": "no zero mode; endpoint reversal, T=0, half revival, and all positive L,c scalings are explicit",
}
EXPECTED_PROOF = {
    "periodic_coordinate": "u(x,t)=F(x+ct)-F(-x+ct) with 2L-periodic F",
    "energy_coordinate": "E=c^2 integral_0^(2L)|F'|^2",
    "trace_coordinate": "u_x(L,t)=2F'(L+ct)",
    "missed_arc": "if cT<2L, support a nonzero smooth mean-zero F' in the complementary arc",
    "revival_phases": "all nonzero modes have frequencies n*pi*c/L and common gcd one",
    "finite_role": "exact cells audit constants and conventions but do not prove infinite-dimensional observability",
}


class Audit:
    def __init__(self): self.n=0
    def ok(self, cond, label):
        self.n += 1
        if not cond: raise AssertionError(label)


def F(x): return Fraction(x)


def phash(data):
    body=dict(data); body.pop("payload_sha256",None)
    raw=json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def main():
    parser=argparse.ArgumentParser(); parser.add_argument("input",nargs="?",type=Path,default=DEFAULT); args=parser.parse_args()
    d=json.loads(args.input.read_text()); a=Audit()
    a.ok(d["payload_sha256"]==phash(d),"hash")
    a.ok(d["schema"]=="hcs-c287-wave-boundary-control-v1","schema")
    a.ok(d["candidate_id"]=="HCS-C287","candidate")
    a.ok(d["evaluation_date"]=="2026-09-02","date")
    a.ok(d["source_commit"]==SOURCE,"source")
    a.ok(d["fixed_epoch"]==1788307200,"epoch")
    a.ok(d["scope_literal"]==SCOPE,"scope")
    a.ok(d["evaluator"]=={"version":"0.2.0","sha256":EVALUATOR},"evaluator")
    model={"pde":"u_tt-c^2 u_xx=0 on (0,L)","adjoint_boundary":"u(0,t)=u(L,t)=0","adjoint_space":"H_0^1(0,L) x L^2(0,L)","observation":"u_x(L,t)","controlled_space":"L^2(0,L) x H^{-1}(0,L) by L^2 Dirichlet control at x=L","energy":"E=(1/2) integral (|u_t|^2+c^2|u_x|^2)"}
    a.ok(d["model"]==model,"model")
    a.ok(d["route_a"]=={"tuple":TUPLE,"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"route")
    a.ok(not any(d["scope_flags"].values()),"flags")
    a.ok(set(d["scope_flags"])=={"arithmetic_local_data","euler_factors","root_numbers","automorphy","target_divisor_or_counting_law","target_functional_equation","target_zero_match","hilbert_polya_operator","route_b_input"},"flag keys")
    a.ok(set(d["theorem_contract"])=={"revival","critical_identity","observability","short_time_failure","hum","boundary"},"theorem keys")
    a.ok(d["theorem_contract"]==EXPECTED_THEOREM,"exact theorem contract")
    a.ok("equality included" in d["theorem_contract"]["observability"],"critical equality")
    a.ok("nonzero smooth" in d["theorem_contract"]["short_time_failure"],"smooth failure")
    a.ok(set(d["proof_contract"])=={"periodic_coordinate","energy_coordinate","trace_coordinate","missed_arc","revival_phases","finite_role"},"proof keys")
    a.ok(d["proof_contract"]==EXPECTED_PROOF,"exact proof contract")
    a.ok("do not prove" in d["proof_contract"]["finite_role"],"finite role")
    a.ok(d["enumeration"]=={"parameter_rows":16,"modal_cells":256,"revival_cells":16,"subcritical_cells":16,"mode_min":1,"mode_max":16},"exact enumeration")
    rows=d["parameter_rows"]
    a.ok(len(rows)==d["enumeration"]["parameter_rows"]==16,"parameter count")
    parameter_keys=set()
    for row in rows:
        L,c=F(row["L"]),F(row["c"])
        key=(L,c)
        a.ok(key not in parameter_keys,"unique parameter key")
        parameter_keys.add(key)
        a.ok(L>0 and c>0,"positive parameters")
        a.ok(F(row["critical_time"])==2*L/c,"critical time")
        a.ok(F(row["observation_energy_ratio"])==4/c**3,"ratio")
    a.ok(parameter_keys=={(L,c) for L in VALUES for c in VALUES},"complete parameter key set")
    modal=d["modal_cells"]
    a.ok(len(modal)==d["enumeration"]["modal_cells"]==256,"modal count")
    modal_keys=set()
    for row in modal:
        L,c,n=F(row["L"]),F(row["c"]),row["n"]
        key=(L,c,n)
        a.ok(key not in modal_keys,"unique modal key")
        modal_keys.add(key)
        # Independent derivation: int sin^2=int cos^2=L/2; time norms=T*/2=L/c.
        energy_a=c*c*n*n/(4*L); energy_b=L/4
        obs_a=n*n/(L*c); obs_b=L/c**3
        a.ok(F(row["energy_displacement_pi2"])==energy_a,"energy a")
        a.ok(F(row["energy_velocity"])==energy_b,"energy b")
        a.ok(F(row["observation_displacement_pi2"])==obs_a,"obs a")
        a.ok(F(row["observation_velocity"])==obs_b,"obs b")
        a.ok(obs_a/energy_a==F(row["displacement_ratio"])==4/c**3,"ratio a")
        a.ok(obs_b/energy_b==F(row["velocity_ratio"])==4/c**3,"ratio b")
        a.ok(F(row["critical_cosine_norm"])==L/c,"cos norm")
        a.ok(F(row["critical_sine_norm"])==L/c,"sin norm")
        a.ok(F(row["critical_cross_term"])==0,"cross")
    a.ok(modal_keys=={(L,c,n) for L in VALUES for c in VALUES for n in range(1,17)},"complete modal key set")
    revival=d["revival_cells"]
    a.ok(len(revival)==d["enumeration"]["revival_cells"]==16,"revival count")
    revival_keys=set()
    for row in revival:
        n=row["n"]
        a.ok(n not in revival_keys,"unique revival key")
        revival_keys.add(n)
        a.ok(row["critical_cos"]=="1" and row["critical_sin"]=="0","critical phase")
        a.ok(F(row["half_cos"])==(-1)**n and row["half_sin"]=="0","half phase")
    a.ok(revival_keys==set(range(1,17)),"complete revival key set")
    a.ok(any(F(row["half_cos"])==-1 for row in revival),"half not identity")
    missed=d["subcritical_cells"]
    a.ok(len(missed)==d["enumeration"]["subcritical_cells"]==16,"missed count")
    subcritical_keys=set()
    for row in missed:
        r=F(row["time_ratio_T_over_Tstar"])
        a.ok(r not in subcritical_keys,"unique subcritical key")
        subcritical_keys.add(r)
        a.ok(0<=r<1,"subcritical")
        a.ok(F(row["observed_arc_fraction"])==r,"observed arc")
        a.ok(F(row["complement_fraction"])==1-r>0,"complement")
        a.ok(row["smooth_nonzero_mean_zero_support_exists"] is True,"support")
        a.ok(row["boundary_trace_on_window"]=="0","zero trace")
    a.ok(subcritical_keys=={Fraction(j,16) for j in range(16)},"complete subcritical key set")
    a.ok(d["enumeration"]["mode_min"]==1 and d["enumeration"]["mode_max"]==16,"no zero mode")
    a.ok({r["identifier"] for r in d["references"]}=={"10.1137/1030001","10.1137/0330055"},"references")
    a.ok({r["role"] for r in d["references"]}=={"HUM owner","boundary geometric control owner"},"roles")
    a.ok(len(d["nonclaims"])==3,"nonclaims")
    a.ok("not a proof" in d["nonclaims"][0],"finite nonclaim")
    a.ok("not claimed as new" in d["nonclaims"][1],"priority nonclaim")
    a.ok("not a target determinant" in d["nonclaims"][2],"target nonclaim")
    print(f"C287 independent checker: PASS ({a.n} assertions)")


if __name__=="__main__": main()
