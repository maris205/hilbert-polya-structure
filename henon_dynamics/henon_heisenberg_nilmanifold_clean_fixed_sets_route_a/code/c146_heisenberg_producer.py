#!/usr/bin/env python3
"""Produce exact HCS-C146 Heisenberg nilmanifold evidence."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


CUTOFF = 20
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
A = ((2, 1), (1, 1))


def matmul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def matpow(matrix, exponent):
    result = ((1, 0), (0, 1))
    base = matrix
    while exponent:
        if exponent & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        exponent //= 2
    return result


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def lucas(index):
    a, b = 2, 1
    for _ in range(index):
        a, b = b, a + b
    return a


def q(value):
    x, y = value
    return x * (x - 1) + x * y + Fraction(1, 2) * y * (y - 1)


def phi(value):
    x, y, z = value
    return 2 * x + y, x + y, z + q((x, y))


def group(left, right):
    x, y, z = left
    X, Y, Z = right
    return x + X, y + Y, z + Z + x * Y


def f(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_hash(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build_evidence():
    ledger = []
    for n in range(1, CUTOFF + 1):
        power = matpow(A, n)
        shifted = ((power[0][0] - 1, power[0][1]), (power[1][0], power[1][1] - 1))
        determinant = det2(shifted)
        trace = power[0][0] + power[1][1]
        ledger.append({
            "n": n,
            "A_power": [list(power[0]), list(power[1])],
            "trace": trace,
            "lucas_L_2n": lucas(2 * n),
            "det_A_power_minus_I": determinant,
            "toral_isolated_fixed_points": abs(determinant),
            "certified_nilmanifold_fixed_circle_lower_bound": 1,
            "central_multiplier": 1,
            "ordinary_isolated_denominator": "0",
            "lefschetz_number": 0,
        })

    # A concrete horizontal fixed class for A^2 that does not lift to a fixed
    # central fibre.  This freezes the correction found during internal audit.
    v = (Fraction(1, 5), Fraction(2, 5))
    av = phi((v[0], v[1], Fraction(0)))
    a2v = phi(av)
    horizontal_shift = (a2v[0] - v[0], a2v[1] - v[1])
    vertical_shift = a2v[2] - horizontal_shift[0] * v[1]

    payload = {
        "schema": "hcs-c146-heisenberg-clean-fixed-evidence-v1",
        "candidate_id": "HCS-C146",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_lock": {
            "object": "Gamma\\H for the upper-triangular real Heisenberg group with Gamma=Z^3 and the lattice automorphism Phi_A",
            "group_law": "(x,y,z)*(X,Y,Z)=(x+X,y+Y,z+Z+xY)",
            "matrix_A": [[2, 1], [1, 1]],
            "automorphism": "Phi_A(x,y,z)=(2x+y,x+y,z+x(x-1)+xy+y(y-1)/2)",
            "clock": "iterate number n",
            "normalization": "central lattice period one; no fitted parameter",
            "determinant_convention": "ordinary isolated-orbit stability factor det(I-DPhi_A^n), tested only as an obstruction",
            "cutoff": {"iterate_ledger": CUTOFF},
            "precision": "exact integer and rational arithmetic",
            "allowed_data": "the frozen Heisenberg group, integer lattice, and matrix A only",
            "forbidden_data": "target tables, prime tables, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "lattice_automorphism_theorem": {
            "correction_q": "q(x,y)=x(x-1)+xy+y(y-1)/2",
            "polarization_identity": "q(v+w)-q(v)-q(w)=2xx'+xy'+x'y+yy'",
            "integer_valued_on_Z2": True,
            "group_homomorphism": True,
            "lattice_bijection": True,
            "center_fixed_pointwise": True,
        },
        "clean_fixed_circle_theorem": {
            "embedded_circle": "C={(0,0,z):z mod 1}",
            "fixed_by_every_positive_iterate": True,
            "fixed_set_is_never_discrete": True,
            "clean_kernel_identity": "ker(I-DPhi_A^n)=T C along C because I-A^n is invertible",
            "derivative_eigenvalue_one": "central direction for every point and iterate",
            "isolated_stability_denominator_all_iterates": "det(I-DPhi_A^n)=det(I-A^n)*(1-1)=0",
            "lefschetz_number_all_iterates": "1-tr(A^n)+tr(A^n)-1=0",
        },
        "iterate_ledger": ledger,
        "horizontal_torus_negative_control": {
            "object": "the induced hyperbolic toral automorphism [v] -> [Av] on T^2",
            "fixed_count_formula": "|det(A^n-I)|=L_(2n)-2",
            "all_fixed_points_isolated": True,
            "ordinary_stability_denominator_nonzero": True,
        },
        "rejected_naive_component_lift": {
            "claim": "every horizontal fixed class lifts to a fixed central circle",
            "status": "REFUTED_FOR_THE_FROZEN_STANDARD_LATTICE_AUTOMORPHISM",
            "iterate": 2,
            "horizontal_class": [f(v[0]), f(v[1])],
            "A2v_minus_v": [f(horizontal_shift[0]), f(horizontal_shift[1])],
            "q2_value": f(a2v[2]),
            "left_quotient_vertical_fixed_condition_value": f(vertical_shift),
            "condition_required": "q_2(v)-k_x*y must be an integer",
            "condition_holds": vertical_shift.denominator == 1,
            "full_nilmanifold_component_count_through_20": "NOT_ASSERTED",
        },
        "formal_lift_hint": {
            "operator": "Koopman U_Phi f=f composed with Phi on L2(N,Haar)",
            "domain": "all of L2(N,Haar); U_Phi is bounded",
            "unitary": True,
            "reason": "Phi is a Haar-volume-preserving nilmanifold automorphism",
            "iterate_clock_preserved": True,
            "isolated_orbit_weight_bridge_constructed": False,
            "status": "FORMAL_HINT_ONLY",
        },
        "route_a": {
            "tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "all_horizontal_classes_lift_to_fixed_circles": False,
            "full_fixed_component_count_claimed": False,
            "isolated_primitive_orbit_ledger": False,
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
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results/c146_heisenberg_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "C146_PRODUCER_PASS", "payload_sha256": payload["payload_sha256"], "ledger_rows": CUTOFF}, sort_keys=True))


if __name__ == "__main__":
    main()
