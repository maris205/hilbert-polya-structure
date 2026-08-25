#!/usr/bin/env python3
"""Independent SymPy reconstruction and parity proof sentinels for HCS-C156."""
from __future__ import annotations

from collections import Counter
import json
from math import lcm
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form


ROOT = Path(__file__).resolve().parents[1]


def parse(value):
    return sp.Rational(str(value))


def q(value):
    x, y = value
    return x * (x - 1) + x * y + y * (y - 1) / 2


def reduce_shift(shift, hnf):
    first, second = shift
    quotient = second // int(hnf[1, 1])
    return ((first - quotient * int(hnf[0, 1])) % int(hnf[0, 0]),
            second % int(hnf[1, 1]))


def main():
    data = json.loads((ROOT / "results/c156_primary_module_evidence.json").read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not bool(condition):
            raise AssertionError(message)

    # Derive the canonical correction from the Heisenberg cocycle rather than
    # importing either standard-library implementation.
    a, b, c, d = sp.symbols("a b c d", integer=True)
    x, y, X, Y = sp.symbols("x y X Y")
    qB = a*c*x*(x-1)/2 + b*c*x*y + b*d*y*(y-1)/2
    qBW = qB.xreplace({x: X, y: Y})
    qBsum = qB.xreplace({x: x + X, y: y + Y})
    target = (a*x+b*y)*(c*X+d*Y)-x*Y
    defect = sp.factor(2 * sp.expand(qBsum - qB - qBW - target))
    check(defect == -2*Y*x*(a*d-b*c-1), "canonical q_B polarization under det B=1")

    v1, v2, w1, w2, m1, m2, u1, u2 = sp.symbols(
        "v1 v2 w1 w2 m1 m2 u1 u2")
    cocycle_polarization = (v1+m1)*(w2+u2)-v1*w2
    rho_polarization = sp.expand(
        cocycle_polarization-(m1+u1)*(v2+w2)+m1*v2+u1*w2)
    check(rho_polarization == v1*u2-u1*v2+m1*u2, "correct rho polarization")

    A = sp.Matrix([[2, 1], [1, 1]])
    for row in data["iterate_ledger"]:
        n = row["n"]
        B = A ** n
        M = B - sp.eye(2)
        H = hermite_normal_form(M)
        S = smith_normal_form(M, domain=sp.ZZ)
        invariants = sorted(abs(int(S[index, index])) for index in range(2))
        check(B.tolist() == row["A_power"], f"power {n}")
        check(M.tolist() == row["M=A_power-I"], f"M {n}")
        check(H.tolist() == row["column_hnf"], f"HNF {n}")
        check(invariants == row["smith_invariants"], f"Smith {n}")

        # A third full rational path reconstructs all primary histograms
        # through n=10.  It uses SymPy matrices and direct symbolic iteration.
        if n <= 10:
            Minv = M.inv()
            for component in row["primary_components"]:
                prime_power = component["cyclic_projector_order"]
                idempotent = component["crt_idempotent_mod_h"]
                shifts = sorted({
                    reduce_shift((idempotent * first, idempotent * second), H)
                    for first in range(prime_power) for second in range(prime_power)
                })
                histogram = Counter()
                for shift in shifts:
                    value = Minv * sp.Matrix(shift)
                    point = value
                    total = sp.Rational(0)
                    for _ in range(n):
                        total += q((point[0], point[1]))
                        point = A * point
                    residue = sp.Mod(sp.together(total - shift[0] * value[1]), 1)
                    histogram[str(residue)] += 1
                    check(sp.denom(residue * prime_power) == 1,
                          f"local denominator {n},{component['prime']}")
                frozen = {item["rotation"]: item["multiplicity"]
                          for item in component["histogram"]}
                check(histogram == frozen, f"primary histogram {n},{component['prime']}")

    # All-n parity lemma.  For either branch write M=gU, U=[[r,s],[s,t]],
    # scale v by h (h=g in the odd branch and h=5g in the even branch).
    # Modulo two both branches have the same numerator below because 5=1.
    g, r, s, t, xx, yy = sp.symbols("g r s t xx yy", integer=True)
    reduced = (s*(g*r+1)*(g+1)*xx + s*(g*t+1)*(g+1)*yy
               + (g*(r*t+s*s)+r+t)*xx*yy)
    # Fibonacci and Lucas pairs both have mod-two period three.  Thus actual
    # branch states are exactly: g=0 -> (r,s,t)=(1,0,1), while g=1 has
    # r+t=1 and rt+s^2=1.  Exhausting x,y parity proves the numerator even.
    parity_states = [(0, 1, 0, 1), (1, 1, 1, 0), (1, 0, 1, 1)]
    for state in parity_states:
        for xbit in (0, 1):
            for ybit in (0, 1):
                value = reduced.subs(dict(zip((g, r, s, t), state))).subs({xx: xbit, yy: ybit})
                check(int(value) % 2 == 0, f"parity lemma {state},{xbit},{ybit}")

    # Recurrence closure certifies the period-three parity statement rather
    # than treating a long finite prefix as its proof.
    fib_states = []
    state = (0, 1)
    for _ in range(3):
        fib_states.append(state)
        state = (state[1], (state[0] + state[1]) % 2)
    check(state == (0, 1) and fib_states == [(0, 1), (1, 1), (1, 0)], "F parity cycle")
    luc_states = []
    state = (0, 1)
    for _ in range(3):
        luc_states.append(state)
        state = (state[1], (state[0] + state[1]) % 2)
    check(state == (0, 1) and luc_states == fib_states, "L parity cycle")

    check(data["canonical_cocycle_and_denominator"]["sharpness_claimed_all_n"] is False,
          "finite sharpness boundary")
    check(data["primary_decomposition_theorem"]["terminology_boundary"].startswith(
        "primary means group-theoretic"), "no arithmetic-local terminology")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B disabled")
    print(json.dumps({"status": "C156_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
