#!/usr/bin/env python3
"""Independent SymPy cross-check for the C135 edge-roof suspension."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c135_edge_roof_evidence.json"


def receipt(poly, variables):
    p = sp.Poly(sp.expand(poly), *variables)
    return {",".join(map(str, powers)): int(coefficient) for powers, coefficient in sorted(p.terms())}


def canonical_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def edge_counts(word):
    out = [0, 0, 0, 0]
    for k, source in enumerate(word):
        out[2 * source + word[(k + 1) % len(word)]] += 1
    return tuple(out)


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
    x00, x01, x10, x11, s = sp.symbols("x00 x01 x10 x11 s")
    variables = (x00, x01, x10, x11)
    M = sp.Matrix([[x00, x01], [x10, x11]])
    delta = sp.expand((sp.eye(2) - M).det())
    expected_delta = 1 - x00 - x11 + x00 * x11 - x01 * x10
    ck(sp.expand(delta - expected_delta) == 0, "formal determinant")
    ck(data["frozen_model"]["formal_determinant_receipt"] == receipt(delta, variables), "det receipt")
    laplace = M.subs({x00: sp.exp(-s), x01: sp.exp(-sp.sqrt(2) * s), x10: sp.exp(-sp.sqrt(3) * s), x11: sp.exp(-sp.sqrt(6) * s)})
    specialized = sp.expand((sp.eye(2) - laplace).det())
    target = 1 - sp.exp(-s) - sp.exp(-sp.sqrt(6) * s) + sp.exp(-(1 + sp.sqrt(6)) * s) - sp.exp(-(sp.sqrt(2) + sp.sqrt(3)) * s)
    ck(sp.simplify(specialized - target) == 0, "Laplace determinant")
    ck(sp.minpoly(sp.sqrt(2), sp.Symbol("y")) == sp.Symbol("y")**2 - 2, "sqrt2")
    ck(sp.minpoly(sp.sqrt(3), sp.Symbol("y")) == sp.Symbol("y")**2 - 3, "sqrt3")
    ck(sp.minpoly(sp.sqrt(6), sp.Symbol("y")) == sp.Symbol("y")**2 - 6, "sqrt6")
    ck(sp.simplify(1 - sp.sqrt(2) - sp.sqrt(3) + sp.sqrt(6)) != 0, "separation nonzero")

    rows = data["replay_prefix"]["rows"]
    for n in range(1, 11):
        trace = sp.expand(sp.trace(M**n))
        ck(rows[n - 1]["trace_edge_count_coefficients"] == receipt(trace, variables), f"trace n={n}")
        ck(sum(receipt(trace, variables).values()) == 2**n, f"rooted total n={n}")
    trace6 = sp.Poly(sp.expand(sp.trace(M**6)), *variables)
    monomial_a = x00**2 * x01 * x10 * x11**2
    monomial_b = x00 * x01**2 * x10**2 * x11
    ck(trace6.coeff_monomial(monomial_a) == 6, "period6 multiplicity 6")
    ck(trace6.coeff_monomial(monomial_b) == 12, "period6 multiplicity 12")

    a = tuple(map(int, "000111"))
    b = tuple(map(int, "001011"))
    c = tuple(map(int, "001101"))
    ck(edge_counts(a) == (2, 1, 1, 2), "a counts")
    ck(edge_counts(b) == edge_counts(c) == (1, 2, 2, 1), "collision counts")
    length = lambda counts: counts[0] + counts[1] * sp.sqrt(2) + counts[2] * sp.sqrt(3) + counts[3] * sp.sqrt(6)
    ck(sp.simplify(length(edge_counts(a)) - length(edge_counts(b)) - (1 - sp.sqrt(2) - sp.sqrt(3) + sp.sqrt(6))) == 0, "length difference")
    ck(sp.simplify(length(edge_counts(b)) - length(edge_counts(c))) == 0, "remaining collision")
    ck(data["edge_sector_theorem"]["orientation_blindness"] == "tau01-tau10 is invisible to every periodic trace and determinant coefficient", "orientation boundary")
    ck(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    print(json.dumps({"status": "C135_SYMPY_CROSSCHECK_PASS", "symbolic_checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
