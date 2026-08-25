#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C168."""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    data = json.loads((ROOT / "results/c168_rank_three_evidence.json").read_text())
    checks = 0

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    i = sp.I
    x = sp.symbols("x")
    F = sp.Matrix(4, 4, lambda row, column: i ** (row * column) / 2)
    F_star = F.conjugate().T
    P1 = sp.diag(1, 0, 1, 1)
    A1 = F_star * P1
    expected_polynomial = x * (x - 1) * (x**2 + i * x / 2 - sp.Rational(1, 2))
    check((F_star * F - sp.eye(4)).applyfunc(sp.simplify) == sp.zeros(4), "F4 unitary")
    check(sp.expand(A1.charpoly(x).as_expr() - expected_polynomial) == 0, "one-site polynomial")
    check(A1.rank() == 3, "rank three")

    lam_plus = (sp.sqrt(7) - i) / 4
    lam_minus = (-sp.sqrt(7) - i) / 4
    roots = [sp.Integer(0), sp.Integer(1), lam_plus, lam_minus]
    for root in roots:
        check(sp.simplify(expected_polynomial.subs(x, root)) == 0, f"root {root}")
    for left in range(len(roots)):
        for right in range(left + 1, len(roots)):
            check(sp.simplify(roots[left] - roots[right]) != 0, f"distinct roots {left},{right}")
    check(A1.is_diagonalizable(), "diagonalizable")
    check(sp.simplify(sp.Abs(lam_plus) - 1 / sp.sqrt(2)) == 0, "plus modulus")
    check(sp.simplify(sp.Abs(lam_minus) - 1 / sp.sqrt(2)) == 0, "minus modulus")

    u_plus = (sp.sqrt(7) - i) / (2 * sp.sqrt(2))
    u_minus = (-sp.sqrt(7) - i) / (2 * sp.sqrt(2))
    check(sp.simplify(lam_plus / u_plus - 1 / sp.sqrt(2)) == 0, "plus phase normalization")
    check(sp.simplify(lam_minus / u_minus - 1 / sp.sqrt(2)) == 0, "minus phase normalization")
    check(sp.simplify(u_plus * sp.conjugate(u_plus) - 1) == 0, "plus unit")
    check(sp.simplify(u_minus * sp.conjugate(u_minus) - 1) == 0, "minus unit")
    check(sp.simplify(u_plus + u_minus + i / sp.sqrt(2)) == 0, "phase sum")
    check(sp.simplify(u_plus * u_minus + 1) == 0, "phase product")
    ratio = sp.simplify(u_plus / u_minus)
    declared_ratio = (-3 + i * sp.sqrt(7)) / 4
    check(sp.simplify(ratio - declared_ratio) == 0, "phase ratio")
    check(sp.simplify(ratio + 1 / ratio + sp.Rational(3, 2)) == 0, "ratio trace")
    check(sp.Rational(-3, 2) not in sp.ZZ, "nonintegral rational trace")
    check(data["one_site_spectrum"]["ratio_not_root_of_unity"] is True, "nontorsion receipt")

    # Independently reconstruct the exact Q(i/sqrt(2)) recurrence.
    phase_sums = [sp.Integer(2), -i / sp.sqrt(2)]
    for _ in range(2, 25):
        phase_sums.append(sp.expand_complex((-i / sp.sqrt(2)) * phase_sums[-1] + phase_sums[-2]))
    for m, row in enumerate(data["fourier_ledgers"], 1):
        a_text, b_text = row["phase_sum_coefficients_a_b"]
        frozen_sum = sp.Rational(a_text) + sp.Rational(b_text) * i / sp.sqrt(2)
        direct_sum = sp.expand_complex(u_plus**m + u_minus**m)
        check(sp.simplify(frozen_sum - phase_sums[m]) == 0, f"recurrence sum {m}")
        check(sp.simplify(frozen_sum - direct_sum) == 0, f"direct sum {m}")
        q = sp.simplify((1 + frozen_sum) / 3)
        q_squared = sp.simplify(q * sp.conjugate(q))
        check(q_squared == sp.Rational(row["one_step_fourier_modulus_squared"]), f"Fourier modulus {m}")
        check(q_squared < 1, f"strict contraction sentinel {m}")

    # Secular multiplicity receipts use two independent multinomial sums.
    for k, row in enumerate(data["spectral_ledgers"], 1):
        triple_sum = 0
        for a_value in range(k + 1):
            for b_value in range(k - a_value + 1):
                c_value = k - a_value - b_value
                triple_sum += sp.factorial(k) // (
                    sp.factorial(a_value) * sp.factorial(b_value) * sp.factorial(c_value)
                )
        damped = [comb(k, j) * 2**j for j in range(k + 1)]
        check(triple_sum == 3**k, f"multinomial mass {k}")
        check(row["damped_count_multiplicities_by_j"] == damped, f"damped ledger {k}")
        check(sum(damped) == row["nonzero_secular_degree"] == 3**k, f"secular degree {k}")
        check(row["zero_generalized_eigenspace_dimension"] == 4**k - 3**k, f"zero space {k}")
        check(row["multinomial_label_count"] == comb(k + 2, 2), f"label count {k}")
        check(row["distinct_phase_count_claimed"] is False, f"collision boundary {k}")

    # A k=2 tensor matrix verifies the nullity and nonzero spectral degree
    # without using the combinatorial producer.
    A2 = sp.kronecker_product(A1, A1)
    check(A2.shape == (16, 16), "k2 tensor dimension")
    check(A2.rank() == 9, "k2 tensor rank")
    check(16 - A2.rank() == 4**2 - 3**2, "k2 zero space")

    # Formal log(2)-coefficients determine the exact mean and variance.
    values = [sp.Integer(0), -sp.Rational(1, 2), -sp.Rational(1, 2)]
    mean = sum(values) / 3
    variance = sum((value - mean) ** 2 for value in values) / 3
    check(mean == -sp.Rational(1, 3), "log modulus mean coefficient")
    check(variance == sp.Rational(1, 18), "log modulus variance coefficient")
    check(data["log_modulus_joint_theorem"]["mean"] == "-log(2)/3", "mean receipt")
    check(data["log_modulus_joint_theorem"]["variance"] == "log(2)^2/18", "variance receipt")

    # Hole-zero finite-group control reconstructed directly from its gate.
    P0 = sp.diag(0, 1, 1, 1)
    A0 = F_star * P0
    control_polynomial = x * (x - 1) * (x + sp.Rational(1, 2)) * (x + i)
    check(sp.expand(A0.charpoly(x).as_expr() - control_polynomial) == 0, "hole-zero polynomial")
    phase_steps = [sp.Integer(1), sp.Integer(-1), -i]
    for mode in (1, 2, 3):
        coefficient = sp.simplify(sum(step**mode for step in phase_steps) / 3)
        check(sp.simplify(coefficient * sp.conjugate(coefficient) - sp.Rational(1, 9)) == 0, f"control Fourier {mode}")
    counts = [1, 0, 0, 0]
    for k, row in enumerate(data["hole_zero_ledgers"], 1):
        new_counts = [0, 0, 0, 0]
        for residue, count in enumerate(counts):
            for increment in (0, 2, 3):
                new_counts[(residue + increment) % 4] += count
        counts = new_counts
        numerator = sum(abs(4 * count - 3**k) for count in counts)
        check(row["counts_by_i_exponent_mod_4"] == counts, f"control counts {k}")
        check(row["count_sum"] == 3**k, f"control mass {k}")
        check(row["tv_to_uniform_numerator"] == numerator, f"control tv {k}")
        check(numerator <= row["fourier_bound_numerator_same_denominator"] == 12, f"control bound {k}")

    # Reflection and antiunitary/projector-order controls are exact matrix
    # identities.  K is represented by entrywise conjugation.
    R = F**2
    P3 = sp.diag(1, 1, 1, 0)
    A3 = F_star * P3
    check((R**2 - sp.eye(4)).applyfunc(sp.simplify) == sp.zeros(4), "reflection involution")
    check((R * A1 * R - A3).applyfunc(sp.simplify) == sp.zeros(4), "hole reflection")
    anti_image = F * A1.conjugate() * F_star
    check((anti_image - A3.conjugate().T).applyfunc(sp.simplify) == sp.zeros(4), "antiunitary image")
    check((anti_image - P3 * F).applyfunc(sp.simplify) == sp.zeros(4), "projector order")
    check((A1 - A1.conjugate().T).applyfunc(sp.simplify) != sp.zeros(4), "not self-adjoint")
    check(data["antiunitary_control"]["fixed_hole_self_adjoint_limit"] is False, "self-adjoint boundary")

    check(data["phase_limit_theorem"]["all_m_uniform_gap_claimed"] is False, "no uniform gap")
    check(data["phase_limit_theorem"]["finite_k_tv_to_continuous_haar"] == "1", "atomic TV boundary")
    check(data["all_k_secular_theorem"]["phase_labels_may_collide"] is True, "collision warning")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B boundary")
    check(data["claim_boundary"]["root_numbers"] is False, "root-number boundary")
    check(data["claim_boundary"]["hilbert_polya_operator"] is False, "Hilbert--Polya boundary")
    check(data["integrity"]["finite_ledgers_are_proof"] is False, "finite-ledger boundary")
    print(json.dumps({"status": "C168_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
