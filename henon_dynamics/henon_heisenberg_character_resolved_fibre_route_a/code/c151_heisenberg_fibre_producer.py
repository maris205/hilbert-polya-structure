#!/usr/bin/env python3
"""Produce exact character-resolved Heisenberg fibre evidence for HCS-C151."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd, lcm
from pathlib import Path


CUTOFF = 12
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
A = ((2, 1), (1, 1))


def matmul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def matpow(matrix, exponent):
    out = ((1, 0), (0, 1))
    base = matrix
    while exponent:
        if exponent & 1:
            out = matmul(out, base)
        base = matmul(base, base)
        exponent //= 2
    return out


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def xgcd(a, b):
    old_r, r = abs(a), abs(b)
    old_s, s, old_t, t = 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s * (1 if a >= 0 else -1), old_t * (1 if b >= 0 else -1)


def column_hnf(matrix):
    """Return [[h11,h12],[0,h22]] spanning the same column lattice."""
    determinant = abs(det2(matrix))
    h22, s, t = xgcd(matrix[1][0], matrix[1][1])
    h11 = determinant // h22
    h12 = (s * matrix[0][0] + t * matrix[0][1]) % h11
    return ((h11, h12), (0, h22))


def q(value):
    x, y = value
    return x * (x - 1) + x * y + Fraction(1, 2) * y * (y - 1)


def apply_a(value):
    x, y = value
    return 2 * x + y, x + y


def q_iterate(value, n):
    total = Fraction(0)
    point = value
    for _ in range(n):
        total += q(point)
        point = apply_a(point)
    return total


def q_iterate_coefficients(n):
    """Coefficients of q_n(x,y)=a*x^2+b*x*y+c*y^2+d*x+e*y."""
    a = b = c = d = e = Fraction(0)
    power = ((1, 0), (0, 1))
    for _ in range(n):
        p, r = power[0]
        s, u = power[1]
        a += p*p + p*s + Fraction(s*s, 2)
        b += 2*p*r + p*u + r*s + s*u
        c += r*r + r*u + Fraction(u*u, 2)
        d -= p + Fraction(s, 2)
        e -= r + Fraction(u, 2)
        power = matmul(A, power)
    return a, b, c, d, e


def evaluate_quadratic(coefficients, value):
    a, b, c, d, e = coefficients
    x, y = value
    return a*x*x + b*x*y + c*y*y + d*x + e*y


def frac(value):
    value %= 1
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_hash(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def rotation_ledger():
    ledger = []
    for n in range(1, CUTOFF + 1):
        power = matpow(A, n)
        matrix = ((power[0][0] - 1, power[0][1]), (power[1][0], power[1][1] - 1))
        determinant = det2(matrix)
        order = abs(determinant)
        hnf = column_hnf(matrix)
        coefficients = q_iterate_coefficients(n)
        histogram = Counter()
        for first in range(hnf[0][0]):
            for second in range(hnf[1][1]):
                # v=M^{-1}m for the quotient representative m=(first,second).
                v = (
                    Fraction(matrix[1][1] * first - matrix[0][1] * second, determinant),
                    Fraction(-matrix[1][0] * first + matrix[0][0] * second, determinant),
                )
                rho = (evaluate_quadratic(coefficients, v) - first * v[1]) % 1
                assert (rho * (2 * order * order)).denominator == 1
                histogram[rho] += 1
        denominator_lcm = 1
        for residue in histogram:
            denominator_lcm = lcm(denominator_lcm, residue.denominator)
        rows = [{"rotation": frac(residue), "multiplicity": histogram[residue]} for residue in sorted(histogram)]
        ledger.append({
            "n": n,
            "A_power": [list(power[0]), list(power[1])],
            "M=A_power-I": [list(matrix[0]), list(matrix[1])],
            "det_M": determinant,
            "horizontal_fixed_class_count": order,
            "column_hnf": [list(hnf[0]), list(hnf[1])],
            "universal_projector_order_Q": 2 * order * order,
            "observed_denominator_lcm": denominator_lcm,
            "rotation_support_size": len(rows),
            "fixed_circle_component_count": histogram[Fraction(0)],
            "histogram": rows,
        })
    return ledger


def build_evidence():
    ledger = rotation_ledger()
    payload = {
        "schema": "hcs-c151-heisenberg-character-fibre-evidence-v1",
        "candidate_id": "HCS-C151",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": "2d4e6211a254ef49d87718569d23466f4c6dcf4c",
        "source_lock": {
            "object": "Gamma\\H for the standard real Heisenberg group and the frozen C146 lattice automorphism Phi",
            "group_law": "(x,y,z)*(X,Y,Z)=(x+X,y+Y,z+Z+xY)",
            "matrix_A": [[2, 1], [1, 1]],
            "correction_q": "q(x,y)=x(x-1)+xy+y(y-1)/2",
            "automorphism": "Phi(v,z)=(Av,z+q(v))",
            "clock": "iterate number n",
            "quotient_convention": "left quotient Gamma\\H",
            "cutoff": {"exact_rotation_histogram": CUTOFF},
            "precision": "exact integer and rational arithmetic",
            "forbidden_data": "target tables, prime tables, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "fibre_rotation_theorem": {
            "horizontal_classes": "Z^2/(A^n-I)Z^2, represented by m with v=(A^n-I)^(-1)m",
            "iterate_cocycle": "q_n(v)=sum_(j=0)^(n-1) q(A^j v)",
            "rotation": "rho_n(v)=q_n(v)-m_1*v_2 mod 1, where m=(A^n-I)v",
            "fixed_fibre_iff": "rho_n(v)=0 mod 1",
            "fixed_component": "when rho_n(v)=0, the entire central fibre is a clean fixed circle",
            "nonzero_rotation": "when rho_n(v)!=0, the horizontal class contributes no fixed point",
            "representative_invariance": "rho_n(v+r)-rho_n(v) is integral for every r in Z^2",
            "representative_invariance_proof_key": "area preservation det(A^n v,A^n r)=det(v,r) reduces the change to q_n(r)-m_1 r_2+m_2 r_1+s_1 m_2-s_1 r_2 with s=(A^n-I)r",
            "clean_kernel": "along a fixed fibre, ker(I-DPhi^n) is exactly its central tangent because A^n-I is invertible",
        },
        "central_root_of_unity_projector": {
            "D_n": "abs(det(A^n-I))",
            "denominator_bound": "rho_n belongs to (1/Q_n)Z/Z for Q_n=2*D_n^2",
            "component_count": "C_n=(1/Q_n) sum_(a=0)^(Q_n-1) sum_([m] in Z2/(A^n-I)Z2) exp(2*pi*i*a*rho_n(m))",
            "reason": "finite root-of-unity orthogonality is one exactly at rotation zero and zero otherwise",
            "rho_is_horizontal_group_homomorphism": False,
            "terminology_boundary": "central cyclic root-of-unity filter; not a character of the horizontal quotient group",
            "all_iterates": True,
        },
        "rotation_ledger": ledger,
        "discarded_pattern": {
            "status": "FINITE_PATTERN_REJECTED_NOT_EXTRAPOLATED",
            "description": "early Lucas/parity/mod-3 guesses for the zero-rotation count fail at later certified iterates",
            "witnesses": {"n10_fixed_circles": ledger[9]["fixed_circle_component_count"], "n12_fixed_circles": ledger[11]["fixed_circle_component_count"]},
            "all_n_closed_form_claimed": False,
        },
        "formal_lift_hint": {
            "operator": "Koopman U_Phi f=f composed with Phi on L2(N,Haar)",
            "unitary": True,
            "iterate_clock_preserved": True,
            "character_filter_is_trace_formula": False,
            "isolated_orbit_weight_bridge_constructed": False,
            "status": "FORMAL_HINT_ONLY",
        },
        "route_a": {
            "tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "isolated_primitive_orbit_ledger": False,
            "all_horizontal_classes_lift": False,
            "all_n_closed_component_formula": False,
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
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results/c151_heisenberg_fibre_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "C151_PRODUCER_PASS", "payload_sha256": payload["payload_sha256"], "ledger_rows": CUTOFF, "n12_horizontal": payload["rotation_ledger"][-1]["horizontal_fixed_class_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
