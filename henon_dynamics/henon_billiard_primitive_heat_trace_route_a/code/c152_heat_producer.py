#!/usr/bin/env python3
"""Produce exact primitive-direction heat-transform evidence for HCS-C152."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path


S_MAX = 20000
RADII = (10, 20, 40, 80, 120, 160, 200)
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def mobius(n):
    remaining = n
    factors = 0
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            factors += 1
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        factors += 1
    return -1 if factors % 2 else 1


def dense_hash(values):
    return sha256((",".join(str(value) for value in values) + "\n").encode()).hexdigest()


def canonical_hash(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build_evidence():
    all_coefficients = [0] * (S_MAX + 1)
    primitive_coefficients = [0] * (S_MAX + 1)
    limit = isqrt(S_MAX)
    for m in range(1, limit + 1):
        for n in range(1, isqrt(S_MAX - m * m) + 1):
            square = m * m + n * n
            all_coefficients[square] += 1
            if gcd(m, n) == 1:
                primitive_coefficients[square] += 1

    factorized = [0] * (S_MAX + 1)
    for d in range(1, limit + 1):
        mu = mobius(d)
        if mu == 0:
            continue
        d2 = d * d
        for u in range(2, S_MAX // d2 + 1):
            factorized[d2 * u] += mu * all_coefficients[u]
    assert factorized == primitive_coefficients

    coefficient_ledger = [
        {"s=m2+n2": s, "ordered_positive_primitive_multiplicity": primitive_coefficients[s]}
        for s in range(2, S_MAX + 1) if primitive_coefficients[s]
    ]
    collisions = [row for row in coefficient_ledger if row["ordered_positive_primitive_multiplicity"] >= 4]
    count_ledger = []
    for radius in RADII:
        direct = sum(primitive_coefficients[: radius * radius + 1]) if radius * radius <= S_MAX else sum(
            1 for m in range(1, radius + 1) for n in range(1, isqrt(radius*radius-m*m)+1) if gcd(m,n)==1
        )
        inversion = 0
        for d in range(1, radius + 1):
            mu = mobius(d)
            if mu:
                inversion += mu * sum(1 for a in range(1, radius // d + 1) for b in range(1, radius // d + 1) if d*d*(a*a+b*b) <= radius*radius)
        assert direct == inversion
        count_ledger.append({
            "R": radius,
            "N_primitive": direct,
            "mobius_inversion_value": inversion,
            "leading_ratio_N_over_R2": f"{direct}/{radius*radius}",
        })

    payload = {
        "schema": "hcs-c152-billiard-primitive-heat-evidence-v1",
        "candidate_id": "HCS-C152",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": "2d4e6211a254ef49d87718569d23466f4c6dcf4c",
        "source_lock": {
            "object": "ordered positive coprime directions of the unit square billiard",
            "direction_convention": "m,n>=1 ordered; coordinate swap retained; axes excluded; equal lengths retain multiplicity",
            "length": "L_(m,n)=2*sqrt(m^2+n^2)",
            "transform": "H_prim(t)=sum_(m,n>=1,gcd=1) exp(-4*t*(m^2+n^2)), t>0",
            "clock": "squared geometric length in a positive heat transform",
            "normalization": "unit side and unit speed; no fitted parameter",
            "cutoff": {"coefficient_s_max": S_MAX, "count_radii": list(RADII)},
            "precision": "exact integer coefficients and counts; analytic asymptotic proved separately",
            "forbidden_data": "target tables, prime tables, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "heat_transform_theorem": {
            "absolute_convergence": "for every t>0, dominated by the full positive Gaussian lattice sum",
            "theta_plus": "theta_+(u)=sum_(k>=1) exp(-u*k^2)",
            "mobius_factorization": "H_prim(t)=sum_(d>=1) mu(d)*theta_+(4*t*d^2)^2",
            "absolute_interchange_bound": "theta_+(4*t*d^2)<=sqrt(pi)/(4*d*sqrt(t)), so the absolute d-sum is bounded by pi/(16*t)*sum d^(-2)",
            "collision_convention": "each ordered positive primitive direction contributes once; coincident lengths add their multiplicities",
            "not_a_wave_trace": True,
            "not_a_dirichlet_spectral_trace": True,
            "not_an_isolated_orbit_determinant": True,
        },
        "counting_theorem": {
            "Q_definition": "Q(R)=# ordered pairs m,n>=1 with m^2+n^2<=R^2; axes excluded",
            "quarter_disk_estimate": "Q(R)=pi*R^2/4+O(R+1)",
            "mobius_identity": "N_prim(R)=sum_(d<=R/sqrt(2)) mu(d)*Q(R/d)",
            "primitive_count_asymptotic": "N_prim(R)=3*R^2/(2*pi)+O(R*log R)",
            "heat_asymptotic": "H_prim(t)=3/(8*pi*t)+O(t^(-1/2)*log(1/t)) as t decreases to zero",
            "stieltjes_identity": "H_prim(t)=8*t*integral_0^infinity r*exp(-4*t*r^2)*N_prim(r) dr",
            "proof_status": "PROVED_FROM_QUARTER_DISK_BOUND_MOBIUS_INVERSION_AND_STIELTJES_INTEGRATION",
        },
        "coefficient_certificate": {
            "s_max": S_MAX,
            "dense_primitive_vector_sha256": dense_hash(primitive_coefficients),
            "dense_mobius_factorized_vector_sha256": dense_hash(factorized),
            "coefficient_identity_all_s_through_cutoff": True,
            "nonzero_coefficient_count": len(coefficient_ledger),
            "collision_coefficient_count": len(collisions),
            "first_multiplicity_four_square": collisions[0]["s=m2+n2"],
        },
        "coefficient_ledger": coefficient_ledger,
        "count_ledger": count_ledger,
        "natural_quantization_boundary": {
            "operator": "positive Dirichlet half-wave sqrt(-Delta_D) on the unit square",
            "self_adjoint": True,
            "unitary_group": "exp(-it*sqrt(-Delta_D))",
            "same_unit_square_classical_geometry": True,
            "heat_transform_equals_operator_trace": False,
            "clean_family_trace_bridge_constructed": False,
            "status": "NATURAL_INTEGRABLE_QUANTIZATION_WITHOUT_TRACE_IDENTITY",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "clean_wave_trace": False,
            "isolated_orbit_determinant": False,
            "dirichlet_spectral_trace_identity": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "prime_like_correspondence": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results/c152_heat_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "C152_PRODUCER_PASS", "payload_sha256": payload["payload_sha256"], "nonzero_coefficients": payload["coefficient_certificate"]["nonzero_coefficient_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
