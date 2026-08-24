#!/usr/bin/env python3
"""Independent SymPy cross-check for the C134 faithful-character package."""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c134_character_evidence.json"


def qstr(value):
    value = sp.Rational(value)
    return str(value.p) if value.q == 1 else f"{value.p}/{value.q}"


def laurent_dict(expr, x):
    out = {}
    for term in sp.Add.make_args(sp.expand(expr)):
        coefficient, exponent = term.as_coeff_exponent(x)
        exponent = int(exponent)
        out[exponent] = sp.simplify(out.get(exponent, 0) + coefficient)
    return {e: c for e, c in out.items() if c != 0}


def receipt(expr, x):
    return {str(e): qstr(c) for e, c in sorted(laurent_dict(expr, x).items())}


def greceipt(value):
    return {"real": qstr(sp.re(sp.expand_complex(value))), "imag": qstr(sp.im(sp.expand_complex(value)))}


def reduce_mod5(expr, x):
    row = [sp.Rational(0)] * 5
    for exponent, coefficient in laurent_dict(expr, x).items():
        row[exponent % 5] += coefficient
    return [qstr(value) for value in row]


def canonical_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(path.read_text())
    checks = 0

    def ck(condition, label):
        nonlocal checks
        if condition is not True and condition != sp.S.true:
            raise AssertionError(label)
        checks += 1

    ck(data["payload_sha256"] == canonical_hash(data), "payload hash")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    x, z = sp.symbols("x z", nonzero=True)
    lam = sp.Symbol("lam")
    A = sp.Matrix([[sp.Rational(3, 16), sp.Rational(-1, 32)], [sp.Rational(1, 4), 0]])
    B = sp.Matrix([[1, 1, 0], [1, 0, 1], [1, 0, 0]])
    weights = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 5)]
    ck(A.eigenvals() == {sp.Rational(1, 8): 1, sp.Rational(1, 16): 1}, "spectrum")
    ck(max(sum(abs(A[i, j]) for j in range(2)) for i in range(2)) == sp.Rational(1, 4), "norm")
    q = sp.Rational(3, 5) + sp.I * sp.Rational(4, 5)
    ck(sp.simplify(q * sp.conjugate(q)) == 1, "unit modulus")
    ck(sp.minpoly(q, lam) == 5 * lam**2 - 6 * lam + 5, "minimal polynomial")
    ck(sp.trace(sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])) == sp.Rational(6, 5), "quadratic trace")

    examples = data["frozen_family"]["examples"]
    z5_receipts = {}
    for k in (1, 6):
        t = [-2 * k, 0, 2 * k]
        W = B * sp.diag(*[weights[j] * x ** t[j] for j in range(3)])
        delta = sp.expand((sp.eye(3) - z * W).det())
        expected_delta = 1 - sp.Rational(1, 2) * x ** t[0] * z - sp.Rational(1, 6) * x ** (t[0] + t[1]) * z**2 - sp.Rational(1, 30) * x ** sum(t) * z**3
        ck(sp.simplify(delta - expected_delta) == 0, f"delta k={k}")
        delta_coefficients = [sp.expand(delta).coeff(z, n) for n in range(4)]
        ck(examples[str(k)]["symbolic_delta_z0_to_z3"] == [receipt(value, x) for value in delta_coefficients], f"delta receipt k={k}")
        ck(examples[str(k)]["q_delta_z0_to_z3"] == [greceipt(value.subs(x, q)) for value in delta_coefficients], f"q delta k={k}")
        traces = {}
        z5 = {}
        for n in range(1, 9):
            denominator = (1 - sp.Rational(1, 8) ** n) * (1 - sp.Rational(1, 16) ** n)
            traces[n] = sp.expand(sp.trace(W**n) / denominator)
            z5[str(n)] = reduce_mod5(sp.trace(W**n), x)
            ck(examples[str(k)]["universal_hardy_traces_n1_to_8"][str(n)] == receipt(traces[n], x), f"trace k={k},n={n}")
        coeff = [sp.Integer(1)]
        for n in range(1, 9):
            coeff.append(sp.expand(-sum(traces[j] * coeff[n - j] for j in range(1, n + 1)) / n))
        ck(examples[str(k)]["universal_fredholm_coefficients_z0_to_z8"] == [receipt(value, x) for value in coeff], f"coefficients k={k}")
        ck(examples[str(k)]["first_coordinate_radius"] == qstr(sp.Rational(21 * k, 32)), f"radius k={k}")
        ck(examples[str(k)]["pairwise_minimum_gap"] == qstr(sp.Rational(11 * k, 16)), f"gap k={k}")
        z5_receipts[str(k)] = z5
    ck(z5_receipts["1"] == z5_receipts["6"], "complete mod5 alias")
    ck(sp.simplify(q**-2 - q**-12) != 0, "faithful separation")
    ck(greceipt(q**-2) == {"real": "-7/25", "imag": "-24/25"}, "q^-2 receipt")

    for row in data["universal_recovery"]["permutation_receipts"]:
        t = tuple(int(v) for v in row["translations"])
        partial = [t[0], t[0] + t[1], sum(t)]
        decoded = [partial[0], partial[1] - partial[0], partial[2] - partial[1]]
        ck(row["partial_sum_exponents"] == partial, f"partial {t}")
        ck(row["decoded_translations"] == [str(v) for v in decoded] == [str(v) for v in t], f"decode {t}")

    ck(data["controls"]["labelled_parameter_boundary"] == "without the orientation-labelled character parameter, t and -t obey D_{-t,u}(z)=D_{t,u^{-1}}(z)", "labelled boundary")
    ck(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    print(json.dumps({"status": "C134_SYMPY_CROSSCHECK_PASS", "symbolic_checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
