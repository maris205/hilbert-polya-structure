#!/usr/bin/env python3
"""Independent exact checker for HCS-C162."""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import mpmath as mp


EXPECTED_UPSTREAM="de4f1a278c576fd4584e7a20ff5d35144f68b4369a4e93a5acdcf625f09af567"
def digest(path): return sha256(path.read_bytes()).hexdigest()
def payload_hash(data):
    clean=dict(data);clean.pop("payload_sha256")
    return sha256(json.dumps(clean,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def main():
    root=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser();parser.add_argument("--evidence",type=Path,default=root/"results/c162_branch_amplitude_evidence.json")
    args=parser.parse_args();data=json.loads(args.evidence.read_text());checks=0
    assert set(data)=={"schema","candidate_id","evaluation_date","scope_literal","source_commit","source_lock","hard_gate",
                       "renormalization_theorem","formal_lift","shell_summary","shell_ledger","local_convergence_sentinels",
                       "route_a","claim_boundary","payload_sha256"};checks+=1
    assert set(data["source_lock"])=={"object","upstream_c157_evidence_sha256","trace","clock","normalization",
                                      "determinant_convention","cutoff","precision","training_data","forbidden_data"};checks+=1
    assert set(data["hard_gate"])=={"required","status","advance_over_c157"};checks+=1
    assert set(data["renormalization_theorem"])=={"positive_time","negative_time","shell_multiplicity","branch_calculation",
                                                  "remainder","coincident_poles","weyl_and_constant_terms",
                                                  "isolated_stability_amplitude_claimed"};checks+=1
    assert set(data["formal_lift"])=={"operator","hilbert_space","trace_identity","same_clock",
                                      "self_adjoint_source_operator","target_operator_claimed"};checks+=1
    assert set(data["shell_summary"])=={"occupied_shells","total_nonzero_lattice_vectors","coincident_pole_shells",
                                        "first_four_ordered_positive_direction_collision_N"};checks+=1
    assert set(data["route_a"])=={"tuple","overall","route_b_invocation_allowed"};checks+=1
    assert set(data["claim_boundary"])=={"isolated_primitive_orbit_determinant","isolated_stability_amplitude",
                                         "target_trace_identity","target_divisor_matching","target_functional_equation",
                                         "target_counting_law","arithmetic_local_data","euler_factors","root_numbers",
                                         "automorphy","hilbert_polya_operator"};checks+=1
    assert data["payload_sha256"]==payload_hash(data);checks+=1
    assert data["schema"]=="hcs-c162-square-billiard-renormalized-branch-amplitude-evidence-v1";checks+=1
    assert data["candidate_id"]=="HCS-C162";checks+=1
    assert data["evaluation_date"]=="2026-08-25";checks+=1
    assert data["source_commit"]=="63f75cf476711de93e6096ef74ac16969e1127d0";checks+=1
    assert data["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER";checks+=1
    assert data["source_lock"]=={
        "object":"the C157 Dirichlet Abel half-wave trace W_D(s) on the unit square",
        "upstream_c157_evidence_sha256":EXPECTED_UPSTREAM,
        "trace":"W_D(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2)), Re(s)>0",
        "clock":"half-wave time t under the boundary approach s=epsilon-i*t",
        "normalization":"epsilon^(3/2) at a nonzero source shell time t=plus_or_minus 2*sqrt(N)",
        "determinant_convention":"none; clean lattice families are not isolated-orbit determinants",
        "cutoff":{"all_shell_theorem":True,"exact_source_shell_N_at_most":800},
        "precision":"exact lattice arithmetic and 60-decimal local branch sentinels",
        "training_data":"none",
        "forbidden_data":"target zero/prime tables, target divisors/counting laws, arithmetic local or Euler factors, root numbers, automorphy, Hilbert--Polya, Route B"};checks+=1
    assert data["hard_gate"]=={
        "required":"a proved regularization/normalization theorem, not another higher-precision branch table",
        "status":"PASS_NO_MODEL_PIVOT",
        "advance_over_c157":"the full trace has a canonical epsilon^(3/2) boundary limit at every nonzero lattice shell, including times where a simple boundary pole coincides"};checks+=1
    assert data["route_a"]["route_b_invocation_allowed"] is False;checks+=1
    assert data["route_a"]["tuple"]==["A1_WEAK","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"];checks+=1
    assert data["route_a"]["overall"]=="ROUTE_A_EXPLORATORY";checks+=1
    assert not any(data["claim_boundary"].values());checks+=len(data["claim_boundary"])
    expected_theorem={
        "positive_time":"lim_(epsilon down to 0) epsilon^(3/2) W_D(epsilon-i*2*sqrt(N))=exp(i*pi/4)*r2_source(N)/(8*pi*N^(1/4))",
        "negative_time":"the corresponding limit at -2*sqrt(N) is the complex conjugate",
        "shell_multiplicity":"r2_source(N)=#{m in Z^2: |m|^2=N}; this is source lattice multiplicity only",
        "branch_calculation":"epsilon^(3/2)*(s^2+4N)^(-3/2)=(epsilon-2*i*t+o(1))^(-3/2) on the principal branch",
        "remainder":"for fixed t0 and 0<epsilon<=1, choose R with 4|m|^2>=2(t0^2+1) outside R; then |s^2+4|m|^2|>=2|m|^2, so the tail is uniformly dominated by a constant times sum |m|^-3; finitely many nonmatching shells stay bounded and all vanish after epsilon^(3/2)",
        "coincident_poles":"-1/(exp(pi*s)-1) is at worst O(epsilon^-1), so its normalized contribution is O(epsilon^(1/2)) and vanishes",
        "weyl_and_constant_terms":"bounded at every nonzero shell time and therefore vanish after normalization",
        "isolated_stability_amplitude_claimed":False}
    assert data["renormalization_theorem"]==expected_theorem;checks+=1
    assert data["formal_lift"]=={
        "operator":"sqrt(Delta_D) for the unit-square Dirichlet Laplacian",
        "hilbert_space":"L^2((0,1)^2) with Dirichlet boundary conditions",
        "trace_identity":"W_D(s)=Tr exp(-s*sqrt(Delta_D)) for Re(s)>0",
        "same_clock":"the half-wave boundary time t in s=epsilon-i*t is unchanged",
        "self_adjoint_source_operator":True,"target_operator_claimed":False};checks+=1
    upstream=root.parent/"henon_square_billiard_abel_wave_trace_route_a/results/c157_abel_trace_evidence.json"
    assert digest(upstream)==EXPECTED_UPSTREAM==data["source_lock"]["upstream_c157_evidence_sha256"];checks+=1

    cutoff=data["source_lock"]["cutoff"]["exact_source_shell_N_at_most"]
    count=Counter()
    radius=isqrt(cutoff)
    for x in range(-radius,radius+1):
        for y in range(-radius,radius+1):
            norm=x*x+y*y
            if 0<norm<=cutoff:count[norm]+=1
    assert len(count)==data["shell_summary"]["occupied_shells"];checks+=1
    assert sum(count.values())==data["shell_summary"]["total_nonzero_lattice_vectors"];checks+=1
    assert sum(isqrt(n)**2==n for n in count)==data["shell_summary"]["coincident_pole_shells"];checks+=1
    assert data["shell_summary"]["first_four_ordered_positive_direction_collision_N"]==65;checks+=1
    rows={row["N"]:row for row in data["shell_ledger"]}
    assert set(rows)==set(count);checks+=1
    for norm,multiplicity in count.items():
        row=rows[norm]
        assert set(row)=={"N","time_symbol","r2_source_shell_multiplicity","axis_vector_count","nonaxis_vector_count",
                          "coincident_boundary_pole","normalized_positive_time_coefficient","primitive_repetition_classes"};checks+=1
        assert row["r2_source_shell_multiplicity"]==multiplicity;checks+=1
        assert row["axis_vector_count"]==(4 if isqrt(norm)**2==norm else 0);checks+=1
        assert row["axis_vector_count"]+row["nonaxis_vector_count"]==multiplicity;checks+=1
        assert row["coincident_boundary_pole"]==(isqrt(norm)**2==norm);checks+=1
        assert row["normalized_positive_time_coefficient"]==f"{multiplicity}*exp(i*pi/4)/(8*pi*{norm}^(1/4))";checks+=1
        assert sum(item["multiplicity"] for item in row["primitive_repetition_classes"])==multiplicity;checks+=1

    mp.mp.dps=70
    for row in data["local_convergence_sentinels"]:
        norm=row["N"];mult=count[norm];t=2*mp.sqrt(norm)
        target=mult*mp.e**(mp.j*mp.pi/4)/(8*mp.pi*norm**(mp.mpf(1)/4))
        assert abs(target-mp.mpc(row["target"]["real"],row["target"]["imag"]))<mp.mpf("1e-34");checks+=1
        previous=None
        for item in row["approximants"]:
            eps=mp.mpf(item["epsilon"]);s=eps-mp.j*t
            value=eps**(mp.mpf(3)/2)*mult*s/(2*mp.pi)*(s*s+4*norm)**(-mp.mpf(3)/2)
            stored=mp.mpc(item["value"]["real"],item["value"]["imag"])
            error=abs(value-target)
            assert abs(value-stored)<mp.mpf("1e-34");checks+=1
            assert abs(error-mp.mpf(item["absolute_error"]))<mp.mpf("1e-24");checks+=1
            if previous is not None:assert error<previous;checks+=1
            previous=error
    print(json.dumps({"status":"C162_INDEPENDENT_CHECK_PASS","assertions":checks,
                      "shells":len(count),"vectors":sum(count.values())},sort_keys=True))
if __name__=="__main__":main()
