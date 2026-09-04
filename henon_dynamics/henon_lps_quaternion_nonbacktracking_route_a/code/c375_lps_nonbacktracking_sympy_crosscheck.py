#!/usr/bin/env python3
"""Exact symbolic lane for HCS-C375."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import sympy as sp

if sys.flags.optimize:
    raise RuntimeError("C375 SymPy cross-check refuses optimized Python")

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c375_lps_nonbacktracking_evidence.json"


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def mu(n: int) -> int:
    return int(sp.mobius(n))


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text(), parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    payload = dict(evidence)
    claimed = payload.pop("payload_sha256")
    assert hashlib.sha256(canonical(payload)).hexdigest() == claimed
    checks = 1

    a0, a1, a2, a3, iota = sp.symbols("a0 a1 a2 a3 iota")
    matrix = sp.Matrix([[a0 + iota * a1, a2 + iota * a3],
                        [-a2 + iota * a3, a0 - iota * a1]])
    determinant = sp.expand(matrix.det()).subs(iota ** 2, -1)
    assert sp.expand(determinant - (a0 ** 2 + a1 ** 2 + a2 ** 2 + a3 ** 2)) == 0
    checks += 1
    quaternions = [tuple(row) for row in evidence["construction"]["quaternion_generators"]]
    assert len(quaternions) == 6 and len(set(quaternions)) == 6
    checks += 2
    for quaternion in quaternions:
        assert sum(value * value for value in quaternion) == 5
        nonzero_tail = [value for value in quaternion[1:] if value]
        assert quaternion[0] == 1 and len(nonzero_tail) == 1 and abs(nonzero_tail[0]) == 2
        checks += 2

    x, u = sp.symbols("x u")
    polynomials = [sp.Integer(2), x]
    for n in range(2, 13):
        polynomials.append(sp.expand(x * polynomials[-1] - 5 * polynomials[-2]))
    logarithmic = sp.series(-u * sp.diff(sp.log(1 - x * u + 5 * u ** 2), u), u, 0, 13).removeO().expand()
    for n in range(1, 13):
        assert sp.expand(logarithmic.coeff(u, n) - polynomials[n]) == 0
        checks += 1
    rplus, rminus = sp.symbols("rplus rminus")
    for n in range(13):
        reduced = sp.expand(polynomials[n].subs(x, rplus + rminus).subs(rplus * rminus, 5))
        target = rplus ** n + rminus ** n
        # Polynomial division by rplus*rminus-5 certifies equality on the quadratic root surface.
        difference = sp.Poly(sp.expand(reduced - target), rplus, rminus)
        divisor = sp.Poly(rplus * rminus - 5, rplus, rminus)
        assert difference.rem(divisor).as_expr() == 0
        checks += 1

    # Exact 6-regular control: K7 tests the full Bass trace consequence on 42 oriented edges.
    size = 7
    adjacency = sp.ones(size) - sp.eye(size)
    directed = [(v, w) for v in range(size) for w in range(size) if v != w]
    edge_index = {edge: k for k, edge in enumerate(directed)}
    hashimoto = sp.zeros(len(directed))
    for edge, row in edge_index.items():
        v, w = edge
        for z in range(size):
            if z != w and z != v:
                hashimoto[row, edge_index[(w, z)]] = 1
    for n in range(1, 13):
        lhs = int(sp.trace(hashimoto ** n))
        rhs = int(sp.trace(polynomials[n].subs(x, adjacency))) if False else None
        q_of_a = sp.zeros(size)
        poly = sp.Poly(polynomials[n], x)
        for (power,), coefficient in poly.terms():
            q_of_a += coefficient * (adjacency ** power)
        rhs = int(sp.trace(q_of_a)) + (3 * size - size) * (1 + (-1) ** n)
        assert lhs == rhs
        checks += 1

    for panel in evidence["panels"]:
        q = panel["q"]
        root = panel["sqrt_minus_one"]
        assert (root * root + 1) % q == 0
        character = 1 if q % 20 in (1, 9) else -1
        assert panel["legendre_5_over_q"] == character
        expected_size = q * (q * q - 1) // (2 if character == 1 else 1)
        assert panel["vertices"] == expected_size
        assert panel["undirected_edges"] - panel["vertices"] == panel["bass_exponent"]
        checks += 4
        traces = [0] + [row["hashimoto_trace"] for row in panel["iterate_ledger"]]
        for n, row in enumerate(panel["iterate_ledger"], 1):
            exact = sum(mu(d) * traces[n // d] for d in sp.divisors(n))
            assert exact == n * row["primitive_oriented_cycles"]
            assert row["adjacency_trace"] == expected_size * row["adjacency_return_words_per_vertex"]
            assert row["hashimoto_trace"] >= 0
            checks += 3
        assert panel["certified_girth"] == next(n for n in range(1, 13) if traces[n])
        checks += 1

    # A broad integer specialization grid catches sign/branch errors in Q_n.
    for value in range(-40, 41):
        roots = sp.solve(sp.Symbol("t") ** 2 - value * sp.Symbol("t") + 5, sp.Symbol("t"))
        for n in range(1, 13):
            recurrence_value = int(polynomials[n].subs(x, value))
            newton_value = sp.simplify(roots[0] ** n + roots[1] ** n)
            assert sp.simplify(newton_value - recurrence_value) == 0
            checks += 1

    route = evidence["route_a"]
    assert route["tuple"] == ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert route["overall"] == "ROUTE_A_EXPLORATORY"
    assert route["route_b_invocation_allowed"] is False
    assert route["a1_scope"].startswith("the exact primitive ledger is source-local")
    assert len(route["a1_missing_requirements"]) == 4
    assert any("random-phase" in row for row in route["a1_missing_requirements"])
    assert not any(evidence["scope_flags"].values())
    checks += 7
    print(f"C375 SymPy cross-check: PASS ({checks} exact checks)")


if __name__ == "__main__":
    main()
