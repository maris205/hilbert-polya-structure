#!/usr/bin/env python3
"""Produce normalized square-billiard branch amplitudes for HCS-C162."""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path

import mpmath as mp


N_CUTOFF = 800
SOURCE_COMMIT = "63f75cf476711de93e6096ef74ac16969e1127d0"
UPSTREAM_SHA256 = "de4f1a278c576fd4584e7a20ff5d35144f68b4369a4e93a5acdcf625f09af567"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical_hash(payload):
    return sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False).encode()).hexdigest()


def shell_ledger():
    shells = defaultdict(list)
    radius = isqrt(N_CUTOFF)
    for first in range(-radius, radius + 1):
        for second in range(-radius, radius + 1):
            norm = first * first + second * second
            if 0 < norm <= N_CUTOFF:
                shells[norm].append((first, second))
    rows = []
    for norm in sorted(shells):
        vectors = sorted(shells[norm])
        axes = [list(v) for v in vectors if v[0] == 0 or v[1] == 0]
        primitive_classes = defaultdict(int)
        for first, second in vectors:
            repetition = gcd(abs(first), abs(second))
            primitive_classes[(first // repetition, second // repetition, repetition)] += 1
        rows.append({
            "N": norm,
            "time_symbol": f"2*sqrt({norm})",
            "r2_source_shell_multiplicity": len(vectors),
            "axis_vector_count": len(axes),
            "nonaxis_vector_count": len(vectors) - len(axes),
            "coincident_boundary_pole": isqrt(norm) ** 2 == norm,
            "normalized_positive_time_coefficient":
                f"{len(vectors)}*exp(i*pi/4)/(8*pi*{norm}^(1/4))",
            "primitive_repetition_classes": [
                {"primitive_vector": [first, second], "repetition": repetition,
                 "multiplicity": multiplicity}
                for (first, second, repetition), multiplicity in sorted(primitive_classes.items())
            ],
        })
    return rows


def complex_parts(value):
    return {"real": mp.nstr(mp.re(value), 35), "imag": mp.nstr(mp.im(value), 35)}


def convergence_row(norm, multiplicity):
    time = 2 * mp.sqrt(norm)
    target = multiplicity * mp.e ** (mp.j * mp.pi / 4) / (8 * mp.pi * norm ** (mp.mpf(1) / 4))
    approximants = []
    for epsilon in (mp.mpf("0.04"), mp.mpf("0.01"), mp.mpf("0.0025"), mp.mpf("0.000625")):
        s = epsilon - mp.j * time
        value = (epsilon ** (mp.mpf(3) / 2) * multiplicity * s / (2 * mp.pi) *
                 (s * s + 4 * norm) ** (-mp.mpf(3) / 2))
        approximants.append({"epsilon": str(epsilon), "value": complex_parts(value),
                             "absolute_error": mp.nstr(abs(value - target), 25)})
    assert all(mp.mpf(approximants[i + 1]["absolute_error"]) <
               mp.mpf(approximants[i]["absolute_error"]) for i in range(3))
    return {"N": norm, "target": complex_parts(target), "approximants": approximants,
            "strict_error_decrease": True}


def build_evidence():
    mp.mp.dps = 60
    ledger = shell_ledger()
    by_norm = {row["N"]: row for row in ledger}
    sentinels = [convergence_row(norm, by_norm[norm]["r2_source_shell_multiplicity"])
                 for norm in (1, 2, 5, 13, 65)]
    payload = {
        "schema": "hcs-c162-square-billiard-renormalized-branch-amplitude-evidence-v1",
        "candidate_id": "HCS-C162",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "the C157 Dirichlet Abel half-wave trace W_D(s) on the unit square",
            "upstream_c157_evidence_sha256": UPSTREAM_SHA256,
            "trace": "W_D(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2)), Re(s)>0",
            "clock": "half-wave time t under the boundary approach s=epsilon-i*t",
            "normalization": "epsilon^(3/2) at a nonzero source shell time t=plus_or_minus 2*sqrt(N)",
            "determinant_convention": "none; clean lattice families are not isolated-orbit determinants",
            "cutoff": {"all_shell_theorem": True, "exact_source_shell_N_at_most": N_CUTOFF},
            "precision": "exact lattice arithmetic and 60-decimal local branch sentinels",
            "training_data": "none",
            "forbidden_data": "target zero/prime tables, target divisors/counting laws, arithmetic local or Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "hard_gate": {
            "required": "a proved regularization/normalization theorem, not another higher-precision branch table",
            "status": "PASS_NO_MODEL_PIVOT",
            "advance_over_c157": "the full trace has a canonical epsilon^(3/2) boundary limit at every nonzero lattice shell, including times where a simple boundary pole coincides",
        },
        "renormalization_theorem": {
            "positive_time": "lim_(epsilon down to 0) epsilon^(3/2) W_D(epsilon-i*2*sqrt(N))=exp(i*pi/4)*r2_source(N)/(8*pi*N^(1/4))",
            "negative_time": "the corresponding limit at -2*sqrt(N) is the complex conjugate",
            "shell_multiplicity": "r2_source(N)=#{m in Z^2: |m|^2=N}; this is source lattice multiplicity only",
            "branch_calculation": "epsilon^(3/2)*(s^2+4N)^(-3/2)=(epsilon-2*i*t+o(1))^(-3/2) on the principal branch",
            "remainder": "for fixed t0 and 0<epsilon<=1, choose R with 4|m|^2>=2(t0^2+1) outside R; then |s^2+4|m|^2|>=2|m|^2, so the tail is uniformly dominated by a constant times sum |m|^-3; finitely many nonmatching shells stay bounded and all vanish after epsilon^(3/2)",
            "coincident_poles": "-1/(exp(pi*s)-1) is at worst O(epsilon^-1), so its normalized contribution is O(epsilon^(1/2)) and vanishes",
            "weyl_and_constant_terms": "bounded at every nonzero shell time and therefore vanish after normalization",
            "isolated_stability_amplitude_claimed": False,
        },
        "formal_lift": {
            "operator": "sqrt(Delta_D) for the unit-square Dirichlet Laplacian",
            "hilbert_space": "L^2((0,1)^2) with Dirichlet boundary conditions",
            "trace_identity": "W_D(s)=Tr exp(-s*sqrt(Delta_D)) for Re(s)>0",
            "same_clock": "the half-wave boundary time t in s=epsilon-i*t is unchanged",
            "self_adjoint_source_operator": True,
            "target_operator_claimed": False,
        },
        "shell_summary": {
            "occupied_shells": len(ledger),
            "total_nonzero_lattice_vectors": sum(row["r2_source_shell_multiplicity"] for row in ledger),
            "coincident_pole_shells": sum(row["coincident_boundary_pole"] for row in ledger),
            "first_four_ordered_positive_direction_collision_N": 65,
        },
        "shell_ledger": ledger,
        "local_convergence_sentinels": sentinels,
        "route_a": {"tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                    "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False},
        "claim_boundary": {
            "isolated_primitive_orbit_determinant": False, "isolated_stability_amplitude": False,
            "target_trace_identity": False, "target_divisor_matching": False,
            "target_functional_equation": False, "target_counting_law": False,
            "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
            "automorphy": False, "hilbert_polya_operator": False,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] /
                        "results/c162_branch_amplitude_evidence.json")
    args = parser.parse_args(); payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status":"C162_PRODUCER_PASS","payload_sha256":payload["payload_sha256"],
                      **payload["shell_summary"]},sort_keys=True))


if __name__ == "__main__": main()
