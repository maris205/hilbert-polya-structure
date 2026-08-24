#!/usr/bin/env python3
"""Fresh SymPy reconstruction of the C130 determinant and trace prefix."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results" / "c130_suspension_evidence.json"


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[k:] + word[:k] for k in range(len(word)))


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    checks = 0

    def ck(condition, label: str) -> None:
        nonlocal checks
        if not bool(condition):
            raise AssertionError(label)
        checks += 1

    body = dict(data)
    digest = body.pop("payload_sha256")
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ck(hashlib.sha256(raw).hexdigest() == digest, "payload hash")

    u, v, q, s = sp.symbols("u v q s")
    B = sp.Matrix([[1, 1], [1, 1]])
    M = B * sp.diag(u, v)
    ck(B.is_positive_definite is False, "positive matrix need not be positive definite")
    ck(all(entry == 1 for entry in B), "mixing positivity")
    ck(sp.expand((sp.eye(2) - M).det()) == 1 - u - v, "bivariate determinant")
    ck(M.rank() == 1, "rank one")
    charpoly = M.charpoly()
    lam = charpoly.gen
    ck(sp.expand(charpoly.as_expr() - (lam**2 - (u + v) * lam)) == 0, "characteristic polynomial")

    primitive_total = 0
    rooted_total = 0
    for n in range(1, 11):
        expected = sp.expand((u + v) ** n)
        ck(sp.expand(sp.trace(M**n) - expected) == 0, f"trace {n}")
        for k in range(n + 1):
            ck(sp.Poly(expected, u, v).coeff_monomial(u ** (n - k) * v**k) == math.comb(n, k), f"sector {n},{k}")
        reps = {
            least_rotation(word)
            for word in itertools.product(range(2), repeat=n)
            if primitive(word)
        }
        row = data["replay_prefix"]["rows"][n - 1]
        ck(len(reps) == row["primitive_cycles"], f"primitive {n}")
        ck(2**n == row["rooted_closed_words"], f"rooted {n}")
        primitive_total += len(reps)
        rooted_total += 2**n
    ck(primitive_total == 226, "primitive total")
    ck(rooted_total == 2046, "rooted total")

    ck(sp.expand((1 - u - v).subs({u: q, v: q**2})) == 1 - q - q**2, "rational specialization")
    t = 2 * sp.pi
    irrational_phase = complex(sp.N(sp.exp(-sp.I * sp.sqrt(2) * t), 40))
    ck(abs(irrational_phase - 1) > 0.1, "irrational roof defeats 2pi period")
    ck(sp.simplify(sp.exp(-sp.I * t)) == 1, "unit roof is 2pi periodic")
    ck(data["clock_sector_separation"]["same_sector_primitive_example_period_6"] == ["000111", "001011"], "same-sector caveat")
    ck(data["rational_roof_control"]["periodicity_recovered"] is True, "control periodicity")
    ck(data["route_a"]["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    ck(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    print(json.dumps({"status": "C130_SYMPY_CROSSCHECK_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
