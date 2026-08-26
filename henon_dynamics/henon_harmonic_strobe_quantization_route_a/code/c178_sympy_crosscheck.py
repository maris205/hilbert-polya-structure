#!/usr/bin/env python3
"""SymPy reconstruction of C178 without importing producer code."""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c178_harmonic_strobe_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    theta, eta = sp.symbols("theta eta", real=True)
    rotation = sp.Matrix(
        [[sp.cos(theta), sp.sin(theta)], [-sp.sin(theta), sp.cos(theta)]]
    )
    rotation_eta = sp.Matrix(
        [[sp.cos(eta), sp.sin(eta)], [-sp.sin(eta), sp.cos(eta)]]
    )
    reflection = sp.diag(1, -1)
    check(sp.simplify(rotation.det() - 1) == 0, "rotation determinant")
    check(sp.simplify(rotation.T * rotation - sp.eye(2)) == sp.zeros(2), "rotation orthogonal")
    check(
        sp.simplify(rotation * rotation_eta - rotation.subs(theta, theta + eta))
        == sp.zeros(2),
        "rotation group law",
    )
    check(
        sp.simplify(reflection * rotation * reflection - rotation.subs(theta, -theta))
        == sp.zeros(2),
        "classical reversor",
    )

    q, p = sp.symbols("q p", real=True)
    image = rotation * sp.Matrix([q, p])
    check(sp.simplify(image.dot(image) - q**2 - p**2) == 0, "Hamiltonian invariance")
    jacobian = image.jacobian([q, p])
    check(sp.simplify(jacobian.det() - 1) == 0, "Jacobian")

    # Exact differential-operator commutators on a polynomial core.
    x = sp.symbols("x", real=True)
    I = sp.I

    def qhat(f: sp.Expr) -> sp.Expr:
        return x * f

    def phat(f: sp.Expr) -> sp.Expr:
        return -I * sp.diff(f, x)

    def hhat(f: sp.Expr) -> sp.Expr:
        return (-sp.diff(f, x, 2) + x**2 * f) / 2

    for degree in range(13):
        f = x**degree
        check(sp.expand(hhat(qhat(f)) - qhat(hhat(f)) + I * phat(f)) == 0, f"[H,q] degree {degree}")
        check(sp.expand(hhat(phat(f)) - phat(hhat(f)) - I * qhat(f)) == 0, f"[H,p] degree {degree}")

    # Generalized Laguerre orthogonality and normalization on a finite exact core.
    y = sp.symbols("y", nonnegative=True)
    for ell in range(5):
        for k in range(6):
            polynomial = sp.assoc_laguerre(k, ell, y)
            integral = sp.integrate(sp.exp(-y) * y**ell * polynomial**2, (y, 0, sp.oo))
            expected = sp.factorial(k + ell) / sp.factorial(k)
            check(sp.simplify(integral - expected) == 0, f"Laguerre norm {ell},{k}")
            for j in range(k):
                other = sp.assoc_laguerre(j, ell, y)
                cross = sp.integrate(sp.exp(-y) * y**ell * polynomial * other, (y, 0, sp.oo))
                check(sp.simplify(cross) == 0, f"Laguerre cross {ell},{k},{j}")

    # Rational angle fixed-set and phase ledgers are reconstructed arithmetically.
    fixed_rows = data["finite_regression_sentinels"]["rational_fixed_rows"]
    for row in fixed_rows:
        a, b, n = row["a"], row["b"], row["n"]
        check(gcd(a, b) == 1, f"reduced {a}/{b}")
        check(row["resonant"] == ((a * n) % b == 0), f"resonance {a}/{b},{n}")

    koopman_rows = data["finite_regression_sentinels"]["koopman_phase_rows"]
    for row in koopman_rows:
        check(row["root_exponent"] == (row["a"] * row["m"]) % row["b"], "Koopman phase")

    quantum_rows = data["finite_regression_sentinels"]["quantum_phase_rows"]
    for row in quantum_rows:
        energy_twice = 2 * row["level"] + 1
        root_order = 2 * row["b"]
        check(row["energy_twice"] == energy_twice, "Hermite energy")
        check(
            row["root_exponent"]
            == (-row["a"] * energy_twice) % root_order,
            "Hermite phase",
        )
        check(row["representative_is_real_time"] is True, "real-time representative")
        check(row["two_pi_shifted_numerator"] == row["a"] + row["b"], "2pi numerator")
        check(
            row["two_pi_shifted_root_exponent"]
            == (-(row["a"] + row["b"]) * energy_twice) % root_order,
            "2pi shifted phase",
        )
        check(row["two_pi_phase_ratio_exponent"] == row["b"], "2pi negative sign")
        check(row["four_pi_shifted_numerator"] == row["a"] + 2 * row["b"], "4pi numerator")
        check(
            row["four_pi_shifted_root_exponent"] == row["root_exponent"],
            "4pi phase return",
        )

    for level in range(16):
        energy = sp.Rational(2 * level + 1, 2)
        check(sp.simplify(sp.exp(-2 * sp.pi * sp.I * energy) + 1) == 0, f"2pi sign {level}")
        check(sp.simplify(sp.exp(-4 * sp.pi * sp.I * energy) - 1) == 0, f"4pi return {level}")

    # Irrational controls use their exact minimal polynomials.
    irrational_rows = data["finite_regression_sentinels"]["irrational_fixed_rows"]
    roots = {
        "sqrt(2)": sp.sqrt(2),
        "sqrt(3)": sp.sqrt(3),
        "golden_ratio": (1 + sp.sqrt(5)) / 2,
    }
    for row in irrational_rows:
        alpha = roots[row["alpha"]]
        check(sp.ask(sp.Q.irrational(alpha)) is True, f"irrational {row['alpha']}")
        check(sp.ask(sp.Q.integer(row["n"] * alpha)) is False, f"noninteger {row['alpha']},{row['n']}")

    check(data["classical_theorem"]["fixed_set_dichotomy"].startswith("Fix(T_theta^n)=R^2"), "evidence classical")
    check(data["gaussian_koopman_theorem"]["basis_action"].endswith("exp(i*m*theta)*psi_(k,m)"), "evidence Koopman")
    check(data["quantum_theorem"]["egorov_q"].startswith("Q_theta^* qhat"), "evidence Egorov")
    check(data["quantum_theorem"]["parameter_domain"].startswith("Q_theta is an operator family on physical real time"), "evidence real time")
    check(data["quantum_theorem"]["metaplectic_periodicity"].startswith("Q_(theta+2*pi)=-Q_theta"), "evidence metaplectic cover")
    check(data["quantum_theorem"]["heat_wick_boundary"].startswith("exp(-t*Hhat)"), "evidence clock")

    print(json.dumps({"status": "C178_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
