#!/usr/bin/env python3
"""Produce exact primitive-family evidence for HCS-C147 square billiards."""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


BOUND = 40
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def mobius(n):
    factors = 0
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            factors += 1
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors += 1
    return -1 if factors % 2 else 1


def canonical_hash(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build_evidence():
    directions = []
    groups = defaultdict(list)
    for m in range(1, BOUND + 1):
        for n in range(1, BOUND + 1):
            if gcd(m, n) != 1:
                continue
            square = m * m + n * n
            directions.append({
                "m": m,
                "n": n,
                "gcd": 1,
                "unfolded_displacement": [2 * m, 2 * n],
                "length": f"2*sqrt({square})",
                "length_squared": 4 * square,
                "wall_reflections": 2 * (m + n),
                "dirichlet_reflection_phase": 1,
                "orientation_convention": "ABSOLUTE_REPRESENTATIVE_WITH_SIGNED_SECTOR_MULTIPLICITIES",
                "signed_unfolded_sector_multiplicity": 4,
                "time_reversal_quotient_sector_multiplicity": 2,
                "family_dimension": 1,
                "family_tangent_multiplier": 1,
            })
            groups[square].append([m, n])

    degeneracies = [
        {"m2_plus_n2": value, "ordered_multiplicity": len(pairs), "directions": pairs}
        for value, pairs in sorted(groups.items()) if len(pairs) > 1
    ]
    symmetry_reduced = defaultdict(set)
    for row in directions:
        symmetry_reduced[row["m"] ** 2 + row["n"] ** 2].add(tuple(sorted((row["m"], row["n"]))))
    inequivalent = [
        {"m2_plus_n2": value, "symmetry_reduced_multiplicity": len(pairs), "representatives": [list(pair) for pair in sorted(pairs)]}
        for value, pairs in sorted(symmetry_reduced.items()) if len(pairs) > 1
    ]
    mobius_count = sum(mobius(d) * (BOUND // d) ** 2 for d in range(1, BOUND + 1))
    first = inequivalent[0]

    payload = {
        "schema": "hcs-c147-square-billiard-family-evidence-v1",
        "candidate_id": "HCS-C147",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_lock": {
            "object": "unit square billiard flow unfolded to straight translations on the doubled square torus",
            "primitive_direction": "ordered positive absolute representative (m,n) with gcd(m,n)=1; four signed unfolded sectors, two after time reversal; coordinate swap retained",
            "axis_boundary_classes": "(1,0) horizontal and (0,1) vertical are two time-reversal-quotiented classes, separately recorded and excluded from the positive ledger",
            "clock": "geometric billiard length L_(m,n)=2*sqrt(m^2+n^2)",
            "normalization": "unit side length and unit speed; no fitted parameter",
            "determinant_convention": "ordinary isolated-orbit factor det(I-DP_gamma) for the full reduced Poincare linearization, tested only as an obstruction",
            "cutoff": {"m_max": BOUND, "n_max": BOUND},
            "precision": "exact integer arithmetic with symbolic square roots",
            "allowed_data": "the frozen square, primitive lattice directions, and exact unfolding only",
            "forbidden_data": "target tables, prime tables, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "family_theorem": {
            "unfolded_primitive_displacement": "(2m,2n)",
            "length_formula": "L_(m,n)=2*sqrt(m^2+n^2)",
            "primitive_iff": "gcd(m,n)=1 for m,n>0",
            "transverse_parameter": "a one-dimensional transverse circle minus finitely many vertex-hitting offsets, decomposing into open cylinders",
            "positive_transverse_length": True,
            "ambient_liouville_positive_measure": False,
            "local_section_coordinates": "s transverse to the primitive vector and theta angular deviation",
            "local_reduced_return": "P(s,theta)=(s+L*tan(theta),theta)",
            "linearization_at_family": "DP(s,0)=[[1,L],[0,1]]",
            "poincare_return_on_fixed_curve": "identity",
            "full_reduced_poincare_statement": "ker(I-DP_gamma) is exactly the fixed-family tangent",
            "family_tangent_multiplier": 1,
            "ordinary_isolated_denominator": "det(I-DP_gamma)=0 because L>0",
            "reflection_count": "2(m+n)",
            "dirichlet_reflection_phase": "+1",
        },
        "count_certificate": {
            "positive_primitive_direction_count": len(directions),
            "mobius_formula": "sum_(d=1)^40 mu(d)*floor(40/d)^2",
            "mobius_formula_value": mobius_count,
            "axis_boundary_class_count": 2,
            "full_signed_oriented_sector_count": 4 * len(directions),
            "full_signed_time_reversal_quotient_sector_count": 2 * len(directions),
        },
        "primitive_direction_ledger": directions,
        "length_square_degeneracy_groups": degeneracies,
        "symmetry_reduced_degeneracy_groups": inequivalent,
        "minimal_nontrivial_collision": {
            "m2_plus_n2": first["m2_plus_n2"],
            "representatives": first["representatives"],
            "witness": [[1, 8], [4, 7]],
            "common_length": "2*sqrt(65)",
            "minimality_domain": "positive primitive directions after quotienting coordinate swap, exhaustively exact through the first collision",
        },
        "aspect_ratio_control": {
            "rectangle_width": "1",
            "rectangle_height": "2^(1/4)",
            "height_squared": "sqrt(2)",
            "length_formula": "2*sqrt(m^2+sqrt(2)*n^2)",
            "basis_independence": "1 and sqrt(2) are Q-linearly independent",
            "distinct_positive_direction_collisions": 0,
            "proof": "equality forces m^2=m'^2 and n^2=n'^2; positivity then forces the same ordered pair",
        },
        "natural_quantization": {
            "operator": "positive Dirichlet half-wave H=sqrt(-Delta_D) on the unit square",
            "underlying_laplacian": "-Delta_D with domain H^2 intersect H_0^1",
            "hilbert_space": "L2 of the unit square",
            "domain": "H_0^1, the form domain of -Delta_D",
            "self_adjoint": True,
            "unitary_group": "U(t)=exp(-itH)",
            "principal_symbol_and_clock": "|p|, giving the unit-speed billiard length clock on |p|=1",
            "antiunitary_time_reversal": "K is complex conjugation, K^2=I and K U(t) K=U(-t)",
            "dirichlet_phase_bridge": "phase -1 per regular reflection and +1 over 2(m+n) reflections",
            "clean_family_trace_bridge_constructed": False,
            "status": "NATURAL_INTEGRABLE_QUANTIZATION",
            "target_matching": False,
            "limitation": "the natural quantization does not convert the clean orbit cylinders into an isolated-orbit determinant or provide any target match",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "isolated_periodic_orbits": False,
            "ordinary_isolated_orbit_determinant_valid": False,
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
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results/c147_billiard_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "C147_PRODUCER_PASS", "payload_sha256": payload["payload_sha256"], "primitive_directions": payload["count_certificate"]["positive_primitive_direction_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
