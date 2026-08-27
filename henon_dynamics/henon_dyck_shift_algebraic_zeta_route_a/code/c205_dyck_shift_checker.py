#!/usr/bin/env python3
"""Producer-independent formal-series and direct-word checker for C205."""
from __future__ import annotations

import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parents[1] / "results" / "c205_dyck_shift_evidence.json"
M = 24


def conv(a, b, m=M):
    out = [Fraction(0) for _ in range(m + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= m: out[i + j] += x * y
    return out


def divide(a, b, m=M):
    assert b[0]
    out = [Fraction(0) for _ in range(m + 1)]
    for n in range(m + 1):
        value = a[n] if n < len(a) else 0
        value -= sum(b[j] * out[n - j] for j in range(1, min(n, len(b) - 1) + 1))
        out[n] = value / b[0]
    return out


def fixed_from_zeta(N):
    # Independently expand s^2=1-4Nz^2, then z(d/dz)log zeta.
    s = [Fraction(0) for _ in range(M + 2)]; s[0] = 1
    for n in range(1, M + 2):
        target = -4 * N if n == 2 else 0
        s[n] = Fraction(target - sum(s[i] * s[n - i] for i in range(1, n)), 2)
    one_plus_s = s[:]; one_plus_s[0] += 1
    h = one_plus_s[:]; h[1] -= 2 * N
    ds = [Fraction((i + 1) * s[i + 1]) for i in range(M + 1)]
    dh = ds[:]; dh[0] -= 2 * N
    logder = [a - 2 * b for a, b in zip(divide(ds, one_plus_s), divide(dh, h))]
    fixed = {str(n): logder[n - 1] for n in range(1, M + 1)}
    assert all(v.denominator == 1 for v in fixed.values())
    return {k: int(v) for k, v in fixed.items()}


def mu(n):
    factors = 0; p = 2; m = n
    while p * p <= m:
        if m % p == 0:
            m //= p; factors += 1
            if m % p == 0: return 0
            while m % p == 0: m //= p
        p += 1
    if m > 1: factors += 1
    return (-1) ** factors


def nonzero(word):
    stack = []
    for kind, colour in word:
        if kind == 1 and stack and stack[-1][0] == 0:
            if stack[-1][1] != colour: return False
            stack.pop()
        else: stack.append((kind, colour))
    return True


def admissible(w):
    n = len(w); repeated = w * 3
    return all(nonzero(repeated[i:i + ell]) for i in range(n) for ell in range(1, 2 * n + 1))


def direct_count(N, n):
    alphabet = tuple((kind, i) for kind in (0, 1) for i in range(N))
    return sum(admissible(w) for w in itertools.product(alphabet, repeat=n))


def verify(data):
    clone = dict(data); claimed = clone.pop("semantic_payload_sha256")
    assert claimed == hashlib.sha256(json.dumps(clone, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert data["package_id"] == "HCS-C205"
    assert data["source_commit"] == "d108ef46fea7a8f62490a69071a83fcbda7c113b"
    assert data["evaluator_sha256"] == "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
    assert data["scope_guard"] == "NO_BAD_EULER_OR_ROOT_NUMBER" and not any(data["claim_flags"].values())
    assert data["source_records"][0]["title"] == "Zeta functions and topological entropy of the Markov-Dyck shifts"
    assert data["source_records"][0]["pages"] == "171-184" and data["source_records"][0]["arxiv"] == "0706.3262"
    assert "official Muenster volume PDF controls" in data["source_records"][0]["pagination_note"]
    assert data["source_records"][1]["pages"] == "75-83"
    assert data["source_records"][1]["doi"] == "10.1016/0097-3165(91)90023-A"
    assert data["coverage"] == {"N_range": [1, 6], "period_range": [1, 24], "formula_cells": 144, "direct_audit_cells": 33, "entropy_cells": 6}
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert data["theorem_contract"]["zeta"].startswith("zeta_N(z)=2*(1+sqrt")
    assert data["theorem_contract"]["circular_code_equation"] == "g_N(z)=N*z^2/(1-g_N(z))"
    assert "iff" in data["model_convention"]["finite_audit_rule"]
    assert "origin-marked" in data["model_convention"]["fixed_point_convention"]
    assert "divided by n only after Mobius" in data["model_convention"]["orbit_convention"]
    formula_cells = direct_cells = 0
    for rec in data["records"]:
        N = rec["N"]; fixed = fixed_from_zeta(N); formula_cells += len(fixed)
        assert rec["topological_entropy"] == f"log({N+1})"
        assert rec["periodic_point_exponential_growth"] == f"lim_(n->infinity) log(Fix_n)/n=log({N+1})"
        assert "Proposition 3.1" in rec["entropy_source_lock"]
        assert fixed == rec["fixed_points"]
        primitive = {str(n): sum(mu(n // d) * fixed[str(d)] for d in range(1, n + 1) if n % d == 0)
                     for n in range(1, M + 1)}
        assert primitive == rec["primitive_points"]
        assert all(primitive[str(n)] % n == 0 and primitive[str(n)] // n == rec["primitive_orbits"][str(n)]
                   for n in range(1, M + 1))
        for n, expected in rec["direct_periodic_word_audit"].items():
            assert direct_count(N, int(n)) == expected == fixed[n]
            direct_cells += 1
        singular = rec["singularity_and_asymptotic"]
        if N == 1:
            assert singular["pole_order"] == 1 and singular["branchpoints_cancel"]
            assert all(fixed[str(n)] == 2 ** n for n in range(1, M + 1))
        else:
            assert singular["dominant_pole"] == f"1/{N+1}"
            assert singular["pole_order"] == 2 and singular["nonrational"]
            assert (N + 1) ** 2 > 4 * N
    assert formula_cells == 144 and direct_cells == 33


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EVIDENCE
    verify(json.loads(path.read_text()))
    print("C205 independent checker: PASS")
    print("144 formal-log-derivative cells; 33 direct periodic-word audits: PASS")


if __name__ == "__main__": main()
