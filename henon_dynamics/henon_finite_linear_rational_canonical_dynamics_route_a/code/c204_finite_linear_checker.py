#!/usr/bin/env python3
"""Producer-independent checker for C204 (no producer imports)."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parents[1] / "results" / "c204_finite_linear_evidence.json"


def ops(name, q):
    def add(a, b): return a ^ b if name == "GF4" else (a + b) % q
    def mul(a, b):
        if name != "GF4": return a * b % q
        z = (a if b & 1 else 0) ^ ((a << 1) if b & 2 else 0)
        return z ^ 7 if z & 4 else z
    return add, mul


def mv(A, v, add, mul):
    return tuple(__import__("functools").reduce(add, (mul(a, b) for a, b in zip(row, v)), 0) for row in A)


def mm(A, B, add, mul):
    return [[__import__("functools").reduce(add, (mul(A[i][k], B[k][j]) for k in range(len(B))), 0)
             for j in range(len(B[0]))] for i in range(len(A))]


def mpow(A, n, add, mul):
    d = len(A); R = [[int(i == j) for j in range(d)] for i in range(d)]
    while n:
        if n & 1: R = mm(R, A, add, mul)
        A = mm(A, A, add, mul); n //= 2
    return R


def rank(A, name, q, add, mul):
    B = [row[:] for row in A]; r = 0
    def inv(x):
        return next(y for y in range(1, q) if mul(x, y) == 1)
    def neg(x): return x if name == "GF4" else (-x) % q
    for c in range(len(B[0]) if B else 0):
        pivot = next((i for i in range(r, len(B)) if B[i][c]), None)
        if pivot is None: continue
        B[r], B[pivot] = B[pivot], B[r]
        z = inv(B[r][c]); B[r] = [mul(z, x) for x in B[r]]
        for i in range(len(B)):
            if i != r and B[i][c]:
                z = neg(B[i][c]); B[i] = [add(x, mul(z, y)) for x, y in zip(B[i], B[r])]
        r += 1
    return r


def mobius(n):
    primes = 0; p = 2; m = n
    while p * p <= m:
        if m % p == 0:
            m //= p; primes += 1
            if m % p == 0: return 0
            while m % p == 0: m //= p
        p += 1
    if m > 1: primes += 1
    return -1 if primes % 2 else 1


def verify(data):
    clone = dict(data); claimed = clone.pop("semantic_payload_sha256")
    actual = hashlib.sha256(json.dumps(clone, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == actual
    assert data["package_id"] == "HCS-C204"
    assert data["source_commit"] == "d108ef46fea7a8f62490a69071a83fcbda7c113b"
    assert data["evaluator_sha256"] == "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
    assert data["scope_guard"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert not any(data["claim_flags"].values())
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    cells = 0
    saw_transient = saw_gf4 = False
    for case in data["cases"]:
        q = case["field"]["order"]; name = case["field"]["name"]; A = case["matrix_rows"]; d = len(A)
        add, mul = ops(name, q)
        if name == "GF4":
            saw_gf4 = True
            assert mul(2, 2) == 3 and add(2, 3) == 1 and mul(3, 3) == 2
        fixes = {}
        for n in range(1, 19):
            P = mpow(A, n, add, mul)
            K = [[add(P[i][j], (1 if name == "GF4" and i == j else ((-1) % q if i == j else 0)))
                  for j in range(d)] for i in range(d)]
            nullity = d - rank(K, name, q, add, mul)
            fixes[str(n)] = q ** nullity
            cells += 1
        assert fixes == case["fixed_counts_formula"] == case["direct_enumeration"]["fixed_counts_direct"]
        exact = {str(n): sum(mobius(n // e) * fixes[str(e)] for e in range(1, n + 1) if n % e == 0)
                 for n in range(1, 19)}
        assert exact == case["exact_periodic_points"]
        assert all(exact[str(n)] // n == case["exact_cycles"][str(n)] for n in range(1, 19))
        observed_cycles = {k: v for k, v in case["exact_cycles"].items() if v}
        assert observed_cycles == case["direct_enumeration"]["cycle_histogram_direct"]
        assert observed_cycles == case["artin_mazur_zeta_factors"]
        assert observed_cycles == case["full_function_koopman_characteristic_polynomial"]["cycle_factor_exponents"]
        states = list(itertools.product(range(q), repeat=d)); image = {v: mv(A, v, add, mul) for v in states}
        periodic = set()
        for v in states:
            u = v
            for n in range(1, len(states) + 1):
                u = image[u]
                if u == v:
                    periodic.add(v); break
        assert len(periodic) == case["direct_enumeration"]["periodic_point_count"]
        zero = len(states) - len(periodic)
        assert zero == case["full_function_koopman_characteristic_polynomial"]["zero_multiplicity"]
        saw_transient |= zero > 0 and case["max_preperiod"] > 1
        # Stabilization of ker(A^k) independently recovers periodic dimension and nilpotent height.
        previous = -1; stable_at = None
        for k in range(1, d + 2):
            null = d - rank(mpow(A, k, add, mul), name, q, add, mul)
            if k == 1 and null == 0: stable_at = 0
            if null == previous and stable_at is None: stable_at = k - 1
            previous = null
        assert d - previous == case["periodic_subspace_dimension"]
        assert (stable_at or 0) == case["max_preperiod"]
        assert case["direct_enumeration"]["max_preperiod_direct"] == case["max_preperiod"]
        order = 1
        for n in map(int, observed_cycles): order = math.lcm(order, n)
        assert order == case["periodic_restriction_order"]
    assert saw_transient and saw_gf4 and cells == 144


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EVIDENCE
    verify(json.loads(path.read_text()))
    print("C204 independent checker: PASS")
    print("144 kernel-rank/fixed-count cells; GF4 and transient-tree controls: PASS")


if __name__ == "__main__": main()
