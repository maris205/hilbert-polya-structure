#!/usr/bin/env python3
"""Independent SymPy reconstruction of the C154 orbit algebra."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c154_heteroclinic_evidence.json"


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EVIDENCE
    data = json.loads(path.read_text())
    z = sp.symbols("z")
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    rational = sp.cancel(1 / (1 - z ** 3))
    series = sp.series(rational, z, 0, 37).removeO().expand()
    for degree, value in enumerate(data["finite_replay"]["zeta_coefficients"]):
        ck(series.coeff(z, degree) == value, f"zeta coefficient {degree}")

    formal_log = sp.Add(*[
        sp.Integer(row["fixed_points"]) * z ** row["period_n"] / row["period_n"]
        for row in data["finite_replay"]["fixed_rows"][:36]
    ])
    expected_log = sp.Add(*[z ** (3 * q) / q for q in range(1, 13)])
    ck(sp.expand(formal_log - expected_log) == 0, "formal logarithm")

    for n, row in enumerate(data["finite_replay"]["fixed_rows"], 1):
        fixed = 3 if n % 3 == 0 else 0
        exact = sum(int(sp.mobius(n // d)) * (3 if d % 3 == 0 else 0) for d in sp.divisors(n))
        ck(row["fixed_points"] == fixed, f"fixed n={n}")
        ck(row["exact_period_points"] == exact, f"Mobius n={n}")
        ck(row["primitive_cycles"] == exact // n, f"cycles n={n}")

    substitution = sp.Matrix([[1, 1], [1, 1]])
    lam = sp.Symbol("lambda")
    ck(substitution.charpoly(lam).as_expr() == lam ** 2 - 2 * lam, "TM substitution matrix")
    permutation = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    ck(permutation ** 3 == sp.eye(3), "period-three permutation")
    ck(permutation.charpoly(lam).as_expr() == lam ** 3 - 1, "period-three characteristic polynomial")

    for receipt in data["frozen_configuration"]["tm_period_certificates"]:
        p = sp.Integer(receipt["putative_period"])
        k = receipt["odd_exponent_k"]
        d = p * (2 ** k - 1)
        ck(int(d) == receipt["multiple_d"], f"TM multiple p={p}")
        ck(int(d) % int(p) == 0, f"TM divisibility p={p}")

    for row in data["finite_replay"]["negative_shift_windows"]:
        word = row["central_word"]
        for index in range(len(word) - 3):
            ck(word[index] == word[index + 3], f"negative periodic {row['shift']}/{index}")

    print(json.dumps({"status": "C154_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
