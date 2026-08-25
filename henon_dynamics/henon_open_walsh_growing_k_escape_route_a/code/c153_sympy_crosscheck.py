#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C153."""
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


def matrices():
    f = sp.Matrix(3, 3, lambda j, ell: sp.expand_complex(W ** (j * ell) / R))
    p = sp.diag(1, 0, 1)
    a = sp.simplify(f.conjugate().T * p)
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


def qsi(values):
    a, b, c, d = (sp.Rational(value) for value in values)
    return a + b * R + c * I + d * R * I


def same(a, b):
    return sp.simplify(sp.expand(a - b)) == 0


def trace_recurrence(limit, tau, q0):
    values = [sp.Integer(2), tau]
    for _ in range(2, limit + 1):
        values.append(sp.expand(tau * values[-1] - q0 * values[-2]))
    return values


def main():
    data = json.loads((ROOT / "results/c153_walsh_escape_evidence.json").read_text())
    f, p, a = matrices()
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    clean = lambda m: m.applyfunc(sp.simplify)
    check(clean(f.conjugate().T * f - sp.eye(3)) == sp.zeros(3), "unitary DFT")
    check(clean(a.conjugate().T * a - p) == sp.zeros(3), "A*A=P")
    check(a.rank() == 2, "rank A")

    lam = sp.symbols("lambda")
    tau = R / 6 - I / 2
    q0 = -sp.Rational(1, 2) - R * I / 6
    expected = lam * (lam**2 - tau * lam + q0)
    check(same(a.charpoly(lam).as_expr(), expected), "charpoly A")
    check(not same(q0, 0), "q0 nonzero")
    for m in range(0, 21):
        expected_rank = 3 if m == 0 else 2
        check((a**m).rank() == expected_rank, f"rank A^{m}")

    traces = trace_recurrence(20, tau, q0)
    for m in range(1, 21):
        check(same(sp.trace(a**m), traces[m]), f"trace A^{m}")

    for k in range(1, 4):
        b = build_gate(k, a)
        power = sp.eye(3**k)
        for n in range(0, 2 * k + 1):
            if n:
                power = power * b
            expected_rank = 2 ** min(n, k) * 3 ** (k - min(n, k))
            check(power.rank() == expected_rank, f"direct rank k={k},n={n}")
            if n == k:
                tensor = sp.kronecker_product(*([a] * k))
                check(clean(power - tensor) == sp.zeros(3**k), f"tensor identity k={k}")

    for k in range(1, 4):
        b = build_gate(k, a)
        power = sp.eye(3**k)
        for n in range(1, 11):
            power = power * b
            d = gcd(n, k)
            check(same(sp.trace(power), traces[n // d] ** d), f"trace gcd k={k},n={n}")

    for period in data["fixed_period_trace_theorem"]["periods"]:
        n = period["n"]
        seen = {}
        for row in period["divisor_classes"]:
            d = row["d"]
            value = traces[n // d] ** d
            check(same(qsi(row["trace_value_q_sqrt3_i_sqrt3i"]), value), f"cluster n={n},d={d}")
            seen.setdefault(sp.srepr(sp.simplify(value)), []).append(d)
        check(period["distinct_cluster_value_count"] == len(seen), f"cluster count n={n}")

    witness = data["unnormalized_nonconvergence_witness"]
    odd = qsi(witness["odd_k_trace_t2_q_sqrt3_i_sqrt3i"])
    even = qsi(witness["even_k_trace_tau_squared_q_sqrt3_i_sqrt3i"])
    difference = qsi(witness["difference_t2_minus_tau_squared_q_sqrt3_i_sqrt3i"])
    check(same(odd, traces[2]), "witness odd")
    check(same(even, tau**2), "witness even")
    check(same(difference, -2 * q0), "witness difference")
    check(not same(odd, even), "witness distinct")

    # Controls reconstruct the closed parent, projector order, and moved hole.
    a_closed = f.conjugate().T
    check(clean(a_closed.conjugate().T * a_closed - sp.eye(3)) == sp.zeros(3), "closed one-site unitary")
    for k in range(1, 4):
        b_closed = build_gate(k, a_closed)
        check(clean(b_closed.conjugate().T * b_closed - sp.eye(3**k)) == sp.zeros(3**k), f"closed B unitary k={k}")
    a_right = p * f.conjugate().T
    check(clean(a_right - f * a * f.conjugate().T) == sp.zeros(3), "projector-order similarity")
    for m in range(1, 13):
        check(same(sp.trace(a_right**m), sp.trace(a**m)), f"order trace m={m}")
    a0 = f.conjugate().T * sp.diag(0, 1, 1)
    expected_a0 = lam * (lam + I) * (3 * lam + R) / 3
    check(same(a0.charpoly(lam).as_expr(), expected_a0), "moved-hole charpoly")
    for m in range(1, 8):
        check((a0**m).rank() == 2, f"moved-hole rank m={m}")
    check(not same(sp.trace(a0), sp.trace(a)), "moved-hole trace changes")

    check(data["macroscopic_escape_theorem"]["positive_escape_exponent"] == "E(alpha)=min(alpha,1)*log(3/2)", "macro text")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    check(all(value is False for key, value in data["claim_boundary"].items() if key != "finite_k_and_growing_k_source_gate_only"), "boundaries")
    print(json.dumps({"status": "C153_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
