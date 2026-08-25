#!/usr/bin/env python3
"""Independent SymPy reconstruction of the C148 Walsh-gate identities."""
from __future__ import annotations

import json
from itertools import product
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
R = sp.sqrt(3)
I = sp.I
W = (-1 + I * R) / 2


def receipt(values):
    a, b, c, d = (sp.Rational(value) for value in values)
    return a + b * R + c * I + d * R * I


def same(a, b):
    return sp.expand(a - b) == 0


def matrices():
    f = sp.Matrix(3, 3, lambda j, ell: sp.expand_complex(W ** (j * ell) / R))
    p = sp.diag(1, 0, 1)
    a = sp.Matrix(
        [
            [R / 3, 0, R / 3],
            [R / 3, 0, -R / 6 + I / 2],
            [R / 3, 0, -R / 6 - I / 2],
        ]
    )
    return f, p, a


def build_gate(k, a):
    basis = list(product(range(3), repeat=k))
    index = {word: j for j, word in enumerate(basis)}
    entries = {}
    for source in basis:
        for target_symbol in range(3):
            value = a[target_symbol, source[0]]
            if value != 0:
                entries[index[source[1:] + (target_symbol,)], index[source]] = value
    return sp.SparseMatrix(3**k, 3**k, entries)


def traces_a(a, limit):
    # The characteristic polynomial is checked independently below.  Its two
    # nonzero roots give this exact power-sum recurrence without expression
    # swell from repeated symbolic matrix powers.
    trace = R / 6 - I / 2
    product_nonzero = -sp.Rational(1, 2) - R * I / 6
    answer = [sp.Integer(2), trace]
    for _ in range(2, limit + 1):
        answer.append(sp.expand(trace * answer[-1] - product_nonzero * answer[-2]))
    return answer


def coefficients(k, ta):
    coeff = [sp.Integer(1)]
    for n in range(1, 2**k + 1):
        value = -sum(
            coeff[n - j] * ta[j // gcd(j, k)] ** gcd(j, k)
            for j in range(1, n + 1)
        ) / n
        coeff.append(sp.expand(value))
    return coeff


def main():
    data = json.loads((ROOT / "results/c148_walsh_baker_evidence.json").read_text())
    f, p, a = matrices()
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    clean = lambda m: m.applyfunc(sp.expand)
    check(clean(f.conjugate().T * f - sp.eye(3)) == sp.zeros(3), "unitary Fourier")
    check(clean(a.conjugate().T * a - p) == sp.zeros(3), "A*A")
    aa = clean(a * a.conjugate().T)
    check(clean(aa * aa - aa) == sp.zeros(3), "AA* projection")
    check(a.rank() == 2, "rank A")
    lam = sp.symbols("lambda")
    expected_a = lam * (lam**2 - (R / 6 - I / 2) * lam - sp.Rational(1, 2) - R * I / 6)
    check(same(a.charpoly(lam).as_expr(), expected_a), "A characteristic polynomial")

    ta = traces_a(a, 32)
    for n in range(1, 13):
        check(same(ta[n], receipt(data["trace_ledgers"]["1"][n - 1]["trace_Bk_power_q_sqrt3_i_sqrt3i"])), f"A trace n={n}")

    # Literal sparse matrices independently verify the shift convention.
    for k in range(1, 3):
        b = build_gate(k, a)
        check(b.rank() == 2 * 3 ** (k - 1), f"direct rank k={k}")
        check(clean(b**k - sp.kronecker_product(*([a] * k))) == sp.zeros(3**k), f"direct B^k k={k}")
        power = sp.eye(3**k)
        for n in range(1, 9):
            power = power * b
            direct = sp.trace(power)
            formula = ta[n // gcd(n, k)] ** gcd(n, k)
            check(same(direct, formula), f"direct gcd trace k={k},n={n}")

    for k in range(1, 6):
        coeff = coefficients(k, ta)
        listed = [receipt(value) for value in data["characteristic_polynomials_k1_to_k5"][str(k)]["secular_coefficients_ascending"]]
        check(len(coeff) == len(listed) == 2**k + 1, f"coefficient length k={k}")
        for j, (actual, expected) in enumerate(zip(coeff, listed)):
            check(same(actual, expected), f"coefficient k={k},j={j}")
        check(not same(coeff[-1], 0), f"exact degree k={k}")

    for row in data["primitive_path_ledger"]["rows"]:
        n = row["n"]
        check(same(receipt(row["closed_walk_amplitude_sum_q_sqrt3_i_sqrt3i"]), ta[n // gcd(n, 2)] ** gcd(n, 2)), f"path trace n={n}")

    # Exact closed, order, and hole controls.
    check(clean(f.conjugate().T * f - sp.eye(3)) == sp.zeros(3), "closed control")
    a_right = p * f.conjugate().T
    check(clean(a_right - f * a * f.conjugate().T) == sp.zeros(3), "order similarity")
    for n in range(1, 13):
        check(same(sp.trace(a_right**n), sp.trace(a**n)), f"order trace n={n}")
    a0 = f.conjugate().T * sp.diag(0, 1, 1)
    check(same(sp.trace(a0), -R / 3 - I), "hole trace")
    check(not same(sp.trace(a0), sp.trace(a)), "hole changes spectrum")
    check(data["controls"]["antiunitary_symmetry"] == "NOT_ASSERTED", "symmetry boundary")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B boundary")
    check(all(value is False for key, value in data["claim_boundary"].items() if key != "finite_k_scattering_gate_only"), "claim boundary")
    print(json.dumps({"status": "PASS", "sympy_checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
