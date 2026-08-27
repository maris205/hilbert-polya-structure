#!/usr/bin/env python3
"""Produce the exact C204 finite-linear-dynamics evidence ledger.

All polynomial coefficient lists are low-to-high and monic.  Elements of GF(4)
are encoded by 0,1,a,a+1 = 0,1,2,3, with a^2=a+1.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C204_OUTPUT", ROOT / "results" / "c204_finite_linear_evidence.json"))
MAX_N = 18


class Field:
    def __init__(self, name: str, q: int):
        self.name, self.q = name, q

    def add(self, x: int, y: int) -> int:
        if self.name == "GF4":
            return x ^ y
        return (x + y) % self.q

    def neg(self, x: int) -> int:
        if self.name == "GF4":
            return x
        return (-x) % self.q

    def mul(self, x: int, y: int) -> int:
        if self.name != "GF4":
            return (x * y) % self.q
        # binary polynomials modulo t^2+t+1
        z = 0
        for i in range(2):
            if (y >> i) & 1:
                z ^= x << i
        if z & 4:
            z ^= 0b111
        return z

    def inv(self, x: int) -> int:
        if not x:
            raise ZeroDivisionError
        for y in range(1, self.q):
            if self.mul(x, y) == 1:
                return y
        raise AssertionError("field inverse absent")


def trim(a: list[int]) -> list[int]:
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_divmod(a: list[int], b: list[int], F: Field) -> tuple[list[int], list[int]]:
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError
    q = [0] * max(1, len(a) - len(b) + 1)
    inv_lc = F.inv(b[-1])
    while a != [0] and len(a) >= len(b):
        k = len(a) - len(b)
        c = F.mul(a[-1], inv_lc)
        q[k] = c
        for j, bj in enumerate(b):
            a[j + k] = F.add(a[j + k], F.neg(F.mul(c, bj)))
        a = trim(a)
    return trim(q), trim(a)


def poly_gcd(a: list[int], b: list[int], F: Field) -> list[int]:
    a, b = trim(a), trim(b)
    while b != [0]:
        _, r = poly_divmod(a, b, F)
        a, b = b, r
    if a == [0]:
        return a
    u = F.inv(a[-1])
    return trim([F.mul(u, x) for x in a])


def poly_mul(a: list[int], b: list[int], F: Field) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = F.add(c[i + j], F.mul(x, y))
    return trim(c)


def x_pow_minus_one(n: int, F: Field) -> list[int]:
    p = [0] * (n + 1)
    p[0], p[n] = F.neg(1), 1
    return trim(p)


def companion(f: list[int], F: Field) -> list[list[int]]:
    d = len(f) - 1
    M = [[0] * d for _ in range(d)]
    for j in range(d - 1):
        M[j + 1][j] = 1
    for i in range(d):
        M[i][d - 1] = F.neg(f[i])
    return M


def block_diagonal(blocks: list[list[list[int]]]) -> list[list[int]]:
    d = sum(len(B) for B in blocks)
    M = [[0] * d for _ in range(d)]
    offset = 0
    for B in blocks:
        for i, row in enumerate(B):
            for j, x in enumerate(row):
                M[offset + i][offset + j] = x
        offset += len(B)
    return M


def matvec(M: list[list[int]], v: tuple[int, ...], F: Field) -> tuple[int, ...]:
    out = []
    for row in M:
        s = 0
        for x, y in zip(row, v):
            s = F.add(s, F.mul(x, y))
        out.append(s)
    return tuple(out)


def mobius(n: int) -> int:
    m, mu, p = n, 1, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            mu = -mu
            while m % p == 0:
                m //= p
        p += 1
    return -mu if m > 1 else mu


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b


def direct_graph(M: list[list[int]], F: Field) -> dict:
    states = list(itertools.product(range(F.q), repeat=len(M)))
    image = {v: matvec(M, v, F) for v in states}
    max_tail = 0
    cycle_hist: dict[int, int] = {}
    cycle_nodes: set[tuple[int, ...]] = set()
    counted: set[tuple[int, ...]] = set()
    for start in states:
        path, pos, u = [], {}, start
        while u not in pos and u not in counted:
            pos[u] = len(path)
            path.append(u)
            u = image[u]
        if u in pos:
            cyc = path[pos[u]:]
            cycle_hist[len(cyc)] = cycle_hist.get(len(cyc), 0) + 1
            cycle_nodes.update(cyc)
            max_tail = max(max_tail, pos[u])
        else:
            # Determine tail length to the already processed periodic core.
            v, tail = start, 0
            while v not in cycle_nodes:
                v, tail = image[v], tail + 1
            max_tail = max(max_tail, tail)
        counted.update(path)
    fixed = {}
    for n in range(1, MAX_N + 1):
        total = 0
        for v in states:
            u = v
            for _ in range(n):
                u = image[u]
            total += int(u == v)
        fixed[str(n)] = total
    return {
        "state_count": len(states),
        "periodic_point_count": len(cycle_nodes),
        "max_preperiod_direct": max_tail,
        "cycle_histogram_direct": {str(k): cycle_hist[k] for k in sorted(cycle_hist)},
        "fixed_counts_direct": fixed,
    }


CASES = [
    ("nilpotent_index3_F2", "F2", 2, [[0, 0, 0, 1]]),
    ("identity_dimension3_F2", "F2", 2, [[1, 1], [1, 1], [1, 1]]),
    ("nilpotent_times_order3_F2", "F2", 2, [[0, 0, 1, 1, 1]]),
    ("inseparable_unipotent4_F2", "F2", 2, [[1, 0, 0, 0, 1]]),
    ("two_invariant_factors_F2", "F2", 2, [[1, 1], [1, 0, 0, 1]]),
    ("mixed_unipotent_semisimple_F3", "F3", 3, [[2, 1], [1, 2, 2, 1]]),
    ("nilpotent_times_order4_F5", "F5", 5, [[0, 0, 0, 3, 1]]),
    ("GF4_nonsemisimple_order6", "GF4", 4, [[3, 0, 1]]),
]


def build_case(label: str, field_name: str, q: int, factors: list[list[int]]) -> dict:
    F = Field(field_name, q)
    for f in factors:
        assert f[-1] == 1 and len(f) >= 2
    for f, g in zip(factors, factors[1:]):
        assert poly_divmod(g, f, F)[1] == [0], (label, f, g)
    M = block_diagonal([companion(f, F) for f in factors])
    graph = direct_graph(M, F)
    fixed_formula = {}
    gcd_degrees = {}
    for n in range(1, MAX_N + 1):
        degrees = [len(poly_gcd(f, x_pow_minus_one(n, F), F)) - 1 for f in factors]
        gcd_degrees[str(n)] = degrees
        fixed_formula[str(n)] = q ** sum(degrees)
    assert fixed_formula == graph["fixed_counts_direct"]
    exact_points, exact_cycles = {}, {}
    for n in range(1, MAX_N + 1):
        e = sum(mobius(n // d) * fixed_formula[str(d)] for d in divisors(n))
        assert e >= 0 and e % n == 0
        exact_points[str(n)] = e
        exact_cycles[str(n)] = e // n
    observed = {int(k): v for k, v in graph["cycle_histogram_direct"].items()}
    for n, c in observed.items():
        assert exact_cycles[str(n)] == c
    x_primary = [next((i for i, c in enumerate(f) if c != 0), len(f) - 1) for f in factors]
    periodic_dim = sum((len(f) - 1) - e for f, e in zip(factors, x_primary))
    max_preperiod = max(x_primary, default=0)
    assert graph["periodic_point_count"] == q ** periodic_dim
    assert graph["max_preperiod_direct"] == max_preperiod
    order = 1
    for n, c in observed.items():
        if c:
            order = lcm(order, n)
    koopman = {
        "zero_multiplicity": graph["state_count"] - graph["periodic_point_count"],
        "cycle_factor_exponents": {str(n): c for n, c in sorted(observed.items())},
        "factorization": "X^%d * %s" % (
            graph["state_count"] - graph["periodic_point_count"],
            " * ".join(f"(X^{n}-1)^{c}" for n, c in sorted(observed.items())) or "1",
        ),
    }
    return {
        "case_id": label,
        "field": {"name": field_name, "order": q, "encoding": "0,1,a,a+1" if field_name == "GF4" else "prime residues"},
        "invariant_factors_low_to_high": factors,
        "dimension": len(M),
        "matrix_rows": M,
        "gcd_degrees": gcd_degrees,
        "fixed_counts_formula": fixed_formula,
        "exact_periodic_points": exact_points,
        "exact_cycles": exact_cycles,
        "periodic_subspace_dimension": periodic_dim,
        "x_primary_exponents": x_primary,
        "max_preperiod": max_preperiod,
        "periodic_restriction_order": order,
        "artin_mazur_zeta_factors": {str(n): c for n, c in sorted(observed.items())},
        "full_function_koopman_characteristic_polynomial": koopman,
        "direct_enumeration": graph,
    }


def main() -> None:
    cases = [build_case(*spec) for spec in CASES]
    payload = {
        "schema": "hcs-c204-finite-linear-v1",
        "package_id": "HCS-C204",
        "generated_utc": "2026-08-27T00:00:00Z",
        "source_commit": "d108ef46fea7a8f62490a69071a83fcbda7c113b",
        "evaluator_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "scope_guard": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "theorem_contract": {
            "fixed_formula": "Fix(A^n)=q^(sum_i deg gcd(f_i,X^n-1))",
            "periodic_dimension": "sum_i(deg(f_i)-v_X(f_i))",
            "max_preperiod": "max_i v_X(f_i)",
            "exact_points": "P_n=sum_{d|n} mu(n/d) Fix(A^d)",
            "cycles": "C_n=P_n/n",
            "zeta": "product_n (1-z^n)^(-C_n)",
            "koopman_charpoly": "X^(nonperiodic states) product_n (X^n-1)^(C_n)",
        },
        "coverage": {
            "case_count": len(cases),
            "n_range": [1, MAX_N],
            "includes": ["inseparable X^n-1", "nilpotent", "nonsemisimple", "GF4 control", "multiple invariant factors"],
        },
        "cases": cases,
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "reason": "Exact finite functional-graph dynamics supplies no target local arithmetic, cohomological determinant, or Hilbert--Polya operator.",
        },
        "claim_flags": {
            "target_local_factors_computed": False,
            "target_root_numbers_computed": False,
            "automorphy_claimed": False,
            "hilbert_polya_operator_claimed": False,
            "literature_priority_claimed": False,
        },
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["semantic_payload_sha256"] = hashlib.sha256(raw).hexdigest()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")
    print(f"semantic_payload_sha256={payload['semantic_payload_sha256']}")
    print(f"cases={len(cases)} fixed_cells={len(cases)*MAX_N}")


if __name__ == "__main__":
    main()
