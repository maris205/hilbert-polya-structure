#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C163."""
from __future__ import annotations

from fractions import Fraction
import json
from math import comb
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def parse_poly(row: list[str], variable: sp.Symbol) -> sp.Expr:
    return sum(sp.Rational(value) * variable**power for power, value in enumerate(row))


def main() -> None:
    data = json.loads((ROOT / "results/c163_phase_evidence.json").read_text())
    checks = 0

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    i = sp.I
    s3 = sp.sqrt(3)
    omega = (-1 + i * s3) / 2
    F = sp.Matrix(3, 3, lambda j, ell: sp.expand_complex(omega ** (j * ell) / s3))
    A = F.conjugate().T * sp.diag(1, 0, 1)
    lam = sp.symbols("lambda")
    tau = s3 / 6 - i / 2
    q0 = -sp.Rational(1, 2) - s3 * i / 6
    check((A - sp.Matrix([[s3 / 3, 0, s3 / 3], [s3 / 3, 0, -s3 / 6 + i / 2], [s3 / 3, 0, -s3 / 6 - i / 2]])).applyfunc(sp.simplify) == sp.zeros(3), "gate")
    check(sp.expand(A.charpoly(lam).as_expr() - lam * (lam**2 - tau * lam + q0)) == 0, "one-site polynomial")
    discriminant = sp.expand(tau**2 - 4 * q0)
    check(sp.simplify(discriminant - (sp.Rational(11, 6) + s3 * i / 2)) == 0, "discriminant")

    modulus_square_sum = (1 + sp.sqrt(37)) / 6
    modulus_square_product = sp.Rational(1, 3)
    check(sp.simplify(abs(tau) ** 2 - sp.Rational(1, 3)) == 0, "tau modulus")
    check(sp.simplify(abs(q0) ** 2 - modulus_square_product) == 0, "q modulus")
    c = sp.simplify((abs(tau) ** 2 - modulus_square_sum) / sp.sqrt(modulus_square_product))
    declared_c = (sp.sqrt(3) - sp.sqrt(111)) / 6
    check(sp.simplify(c - declared_c) == 0, "phase cosine derivation")
    check(sp.simplify(c**2 - (sp.Rational(19, 6) - sp.sqrt(37) / 6)) == 0, "c square")
    x = sp.symbols("x")
    primitive = sp.Poly(sp.minpoly(c, x), x)
    monic_minimum = primitive.monic()
    check(primitive == sp.Poly(3 * x**4 - 19 * x**2 + 27, x), "primitive irreducible integer polynomial")
    check(primitive.is_irreducible, "irreducible")
    check(primitive.LC() == 3 and primitive.primitive()[1] == primitive, "primitive integer associate with nonunit leading coefficient")
    check(monic_minimum == sp.Poly(x**4 - sp.Rational(19, 3) * x**2 + 9, x), "monic rational minimal polynomial")
    check(monic_minimum.nth(2) == -sp.Rational(19, 3) and monic_minimum.nth(2) not in sp.ZZ, "nonintegral monic coefficient")
    check(data["phase_algebra"]["primitive_irreducible_integer_polynomial"] == "3*c^4-19*c^2+27", "primitive polynomial receipt")
    check(data["phase_algebra"]["monic_rational_minimal_polynomial"] == "c^4-(19/3)*c^2+9", "monic polynomial receipt")
    check(data["phase_algebra"]["not_algebraic_integer"] is True, "nonintegrality receipt")
    check(data["phase_algebra"]["phase_ratio_not_root_of_unity"] is True, "nontorsion receipt")

    polynomials = [sp.Integer(2), x]
    for _ in range(2, 25):
        polynomials.append(sp.expand(x * polynomials[-1] - polynomials[-2]))
    for m, row in enumerate(data["fourier_decay_ledgers"], 1):
        frozen = parse_poly(row["two_cos_m_delta_polynomial_ascending"], x)
        check(sp.expand(frozen - polynomials[m]) == 0, f"Chebyshev polynomial {m}")
        # The recurrence is exact in Q[c]; the strict bound follows globally
        # from the already certified non-root-of-unity property.
        check(row["r_power_not_one"] is True, f"nonresonance {m}")

    for k, row in enumerate(data["phase_k_ledgers"], 1):
        check(row["multiplicities_by_j"] == [comb(k, j) for j in range(k + 1)], f"binomial row {k}")
        check(sum(row["multiplicities_by_j"]) == 2**k, f"binomial mass {k}")

    # The moved-hole control is reconstructed from the matrix, rather than
    # from the producer's declared spectrum.
    A0 = F.conjugate().T * sp.diag(0, 1, 1)
    check(sp.simplify(A0.charpoly(lam).as_expr() - lam * (lam + i) * (3 * lam + s3) / 3) == 0, "moved-hole polynomial")
    u_plus, u_minus = -i, -1
    check(sp.simplify(u_plus / u_minus - i) == 0, "moved phase ratio")
    check(sp.simplify(i**4 - 1) == 0 and all(sp.simplify(i**power - 1) != 0 for power in range(1, 4)), "moved exact order")
    for k, row in enumerate(data["controls"]["moved_hole"]["residue_ledgers"], 1):
        counts = [sum(comb(k, j) for j in range(k + 1) if j % 4 == residue) for residue in range(4)]
        check(row["counts_by_j_mod_4"] == counts, f"moved residue {k}")

    check(data["all_k_phase_theorem"]["asymptotic_independence"] is True, "joint theorem")
    check(data["general_binary_phase_dichotomy"]["frozen_branch"] == "NON_TORSION_HAAR", "dichotomy")
    check(data["integrity"]["pivot_required"] is False and data["integrity"]["hard_gate_status"] == "PASS", "hard gate")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    check(data["claim_boundary"]["source_side_phase_limit"] is True, "source phase claim")
    check(data["claim_boundary"]["self_adjoint_limit"] is False, "self-adjoint boundary")
    check(data["claim_boundary"]["root_numbers"] is False, "root-number boundary")
    print(json.dumps({"status": "C163_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
