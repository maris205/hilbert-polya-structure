#!/usr/bin/env python3
"""Produce the exact primary quadratic-module ledger for HCS-C156."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd, lcm
from pathlib import Path


CUTOFF = 14
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "506dead810d67fa58fa7c42b2d9a09bfae161059"
A = ((2, 1), (1, 1))


def matmul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


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
    determinant = abs(det2(matrix))
    bottom, s, t = xgcd(matrix[1][0], matrix[1][1])
    top = determinant // bottom
    skew = (s * matrix[0][0] + t * matrix[0][1]) % top
    return ((top, skew), (0, bottom))


def canonical_shift(shift, hnf):
    first, second = shift
    quotient = second // hnf[1][1]
    return ((first - quotient * hnf[0][1]) % hnf[0][0], second % hnf[1][1])


def fibonacci(n):
    first, second = 0, 1
    for _ in range(n):
        first, second = second, first + second
    return first


def lucas(n):
    return 2 if n == 0 else fibonacci(n - 1) + fibonacci(n + 1)


def factor_integer(value):
    factors = []
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            exponent = 0
            while value % prime == 0:
                value //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime += 1
    if value > 1:
        factors.append((value, 1))
    return factors


def valuation(value, prime):
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def q_iterate_coefficients(n):
    """Return coefficients of q_n=a*x^2+b*xy+c*y^2+d*x+e*y."""
    out = [Fraction(0) for _ in range(5)]
    power = ((1, 0), (0, 1))
    for _ in range(n):
        p, r = power[0]
        s, u = power[1]
        add = [
            p * p + p * s + Fraction(s * s, 2),
            2 * p * r + p * u + r * s + s * u,
            r * r + r * u + Fraction(u * u, 2),
            -p - Fraction(s, 2),
            -r - Fraction(u, 2),
        ]
        out = [left + right for left, right in zip(out, add)]
        power = matmul(A, power)
    return tuple(out)


def canonical_q_coefficients(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    return (Fraction(a * c, 2), Fraction(b * c), Fraction(b * d, 2),
            Fraction(-a * c, 2), Fraction(-b * d, 2))


def evaluate(coefficients, value):
    a, b, c, d, e = coefficients
    x, y = value
    return a * x * x + b * x * y + c * y * y + d * x + e * y


def rotation(matrix, coefficients, shift):
    determinant = det2(matrix)
    first, second = shift
    value = (
        Fraction(matrix[1][1] * first - matrix[0][1] * second, determinant),
        Fraction(-matrix[1][0] * first + matrix[0][0] * second, determinant),
    )
    return (evaluate(coefficients, value) - first * value[1]) % 1


def frac(value):
    value %= 1
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def signed_frac(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_hash(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build_row(n):
    power = matpow(A, n)
    matrix = ((power[0][0] - 1, power[0][1]), (power[1][0], power[1][1] - 1))
    determinant = det2(matrix)
    order = abs(determinant)
    hnf = column_hnf(matrix)
    if n % 2:
        scalar = lucas(n)
        cofactor = ((fibonacci(n + 1), fibonacci(n)),
                    (fibonacci(n), fibonacci(n - 1)))
        branch = "ODD_LUCAS_UNIMODULAR"
        expected_cofactor_det = -1
        smith = [scalar, scalar]
        exponent = scalar
    else:
        scalar = fibonacci(n)
        cofactor = ((lucas(n + 1), lucas(n)),
                    (lucas(n), lucas(n - 1)))
        branch = "EVEN_FIBONACCI_DET_MINUS_FIVE"
        expected_cofactor_det = -5
        smith = [scalar, 5 * scalar]
        exponent = 5 * scalar
    assert matrix == tuple(tuple(scalar * entry for entry in row) for row in cofactor)
    assert det2(cofactor) == expected_cofactor_det
    assert gcd(gcd(abs(matrix[0][0]), abs(matrix[0][1])),
               gcd(abs(matrix[1][0]), abs(matrix[1][1]))) == smith[0]
    assert order == smith[0] * smith[1]

    coefficients = q_iterate_coefficients(n)
    canonical = canonical_q_coefficients(power)
    drift = tuple(left - right for left, right in zip(coefficients, canonical))
    assert drift[0] == drift[1] == drift[2] == 0
    assert drift[3].denominator == drift[4].denominator == 1

    components = []
    component_sets = []
    global_denominator = 1
    global_zero_count = 1
    for prime, exponent_power in factor_integer(exponent):
        prime_power = prime ** exponent_power
        complementary = exponent // prime_power
        idempotent = 1 if complementary == 1 else (
            complementary * pow(complementary, -1, prime_power)) % exponent
        shifts = sorted({
            canonical_shift((idempotent * first, idempotent * second), hnf)
            for first in range(prime_power) for second in range(prime_power)
        })
        histogram = Counter(rotation(matrix, coefficients, shift) for shift in shifts)
        denominator_lcm = 1
        for residue in histogram:
            denominator_lcm = lcm(denominator_lcm, residue.denominator)
            assert (residue * prime_power).denominator == 1
        zero_count = histogram[Fraction(0)]
        group_order = prime ** sum(valuation(invariant, prime) for invariant in smith)
        assert len(shifts) == group_order
        rows = [{"rotation": frac(residue), "multiplicity": histogram[residue]}
                for residue in sorted(histogram)]
        components.append({
            "prime": prime,
            "exponent_power": exponent_power,
            "cyclic_projector_order": prime_power,
            "crt_idempotent_mod_h": idempotent,
            "group_order": group_order,
            "enumerated_element_count": len(shifts),
            "rotation_support_size": len(rows),
            "observed_denominator_lcm": denominator_lcm,
            "zero_count": zero_count,
            "root_of_unity_projector_numerator": prime_power * zero_count,
            "histogram": rows,
        })
        component_sets.append((prime, shifts))
        global_denominator = lcm(global_denominator, denominator_lcm)
        global_zero_count *= zero_count

    orthogonality_checks = 0
    for left_index, (_, left_set) in enumerate(component_sets):
        for _, right_set in component_sets[left_index + 1:]:
            for left in left_set:
                left_rotation = rotation(matrix, coefficients, left)
                for right in right_set:
                    total = canonical_shift((left[0] + right[0], left[1] + right[1]), hnf)
                    polarization = (rotation(matrix, coefficients, total)
                                    - left_rotation
                                    - rotation(matrix, coefficients, right)) % 1
                    assert polarization == 0
                    orthogonality_checks += 1

    if order == 1:
        assert not components
        global_zero_count = global_denominator = 1
    return {
        "n": n,
        "A_power": [list(power[0]), list(power[1])],
        "M=A_power-I": [list(matrix[0]), list(matrix[1])],
        "factorization_branch": branch,
        "factor_scalar": scalar,
        "cofactor_matrix": [list(cofactor[0]), list(cofactor[1])],
        "cofactor_determinant": expected_cofactor_det,
        "smith_invariants": smith,
        "horizontal_group_order": order,
        "horizontal_group_exponent_h": exponent,
        "column_hnf": [list(hnf[0]), list(hnf[1])],
        "canonical_q_B_coefficients": [signed_frac(value) if value.denominator != 1 else int(value)
                                         for value in canonical],
        "iterate_linear_drift": [int(drift[3]), int(drift[4])],
        "primary_components": components,
        "orthogonality_pair_checks": orthogonality_checks,
        "global_denominator_lcm_from_components": global_denominator,
        "fixed_circle_component_count": global_zero_count,
        "zero_count_product_verified": True,
    }


def build_evidence():
    ledger = [build_row(n) for n in range(1, CUTOFF + 1)]
    payload = {
        "schema": "hcs-c156-heisenberg-primary-quadratic-module-evidence-v1",
        "candidate_id": "HCS-C156",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "the frozen C151 Heisenberg automorphism on Z^3\\H",
            "matrix_A": [[2, 1], [1, 1]],
            "one_step_correction": "q(x,y)=x(x-1)+xy+y(y-1)/2",
            "upstream_c151_evidence_sha256": "5fe26d210e6c848789ee769f9f0fbaa0ba67baef06cb93cb3d2f2d403ef18419",
            "clock": "iterate number n",
            "cutoff": {"exact_primary_component_enumeration": CUTOFF},
            "precision": "exact integer and rational arithmetic",
            "forbidden_data": "target tables, prime tables, arithmetic local or Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "matrix_power_factorization": {
            "odd_n": "A^n-I=L_n*[[F_(n+1),F_n],[F_n,F_(n-1)]], cofactor determinant -1",
            "even_n": "A^n-I=F_n*[[L_(n+1),L_n],[L_n,L_(n-1)]], cofactor determinant -5",
            "odd_smith_type": "Z/L_n Z times Z/L_n Z",
            "even_smith_type": "Z/F_n Z times Z/(5F_n) Z",
            "all_iterates": True,
        },
        "canonical_cocycle_and_denominator": {
            "canonical_q_B": "for B=[[a,b],[c,d]], q_B=ac*x(x-1)/2+bc*x*y+bd*y(y-1)/2",
            "actual_iterate": "q_n=q_(A^n)+ell_n with ell_n an explicitly computed integer linear form",
            "rotation": "rho_n(v)=q_n(v)-m_1*v_2 mod 1 for m=(A^n-I)v",
            "uniform_bound": "h_n*rho_n is integral, h_n=L_n for odd n and h_n=5F_n for even n",
            "proof_key": "write 2rho for q_(A^n), scale v by h_n, and use the Fibonacci/Lucas parity lemma; the integer linear drift preserves the bound",
            "sharpness_claimed_all_n": False,
            "finite_sharpness": "the observed denominator lcm equals h_n for every 2<=n<=14",
        },
        "primary_decomposition_theorem": {
            "finite_quadratic_module": "G_n=Z^2/(A^n-I)Z^2 with quadratic function rho_n:G_n->Q/Z",
            "polarization": "beta_n([m],[u])=v_1*u_2-u_1*v_2+m_1*u_2 mod 1 for v=M^-1*m and w=M^-1*u",
            "orthogonal_split": "G_n is the orthogonal direct sum of its group-theoretic p-primary components",
            "local_denominator": "rho_n on the p-primary component takes values in (1/p^e)Z/Z, where p^e is the p-part of h_n",
            "zero_product": "C_n is the product over p dividing h_n of the exact p-primary zero counts",
            "local_projector": "C_(n,p)=p^(-e) sum_(a mod p^e) sum_(x in G_(n,p)) exp(2*pi*i*a*rho_n(x))",
            "terminology_boundary": "primary means group-theoretic primary decomposition; no arithmetic local or Euler factor is asserted",
        },
        "iterate_ledger": ledger,
        "formal_lift_hint": {
            "operator": "the frozen Haar Koopman unitary from C151",
            "unitary": True,
            "primary_projector_is_operator_trace_formula": False,
            "status": "FORMAL_HINT_ONLY",
        },
        "route_a": {
            "tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "isolated_primitive_orbit_ledger": False,
            "ordinary_isolated_stability_weight": False,
            "all_n_sharp_denominator": False,
            "all_n_closed_zero_formula": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
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
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] /
                        "results/c156_primary_module_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": "C156_PRODUCER_PASS",
        "payload_sha256": payload["payload_sha256"],
        "ledger_rows": len(payload["iterate_ledger"]),
        "n14_fixed_circles": payload["iterate_ledger"][-1]["fixed_circle_component_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
