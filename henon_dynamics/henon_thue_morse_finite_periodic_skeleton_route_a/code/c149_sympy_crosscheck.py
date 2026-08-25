#!/usr/bin/env python3
"""Independent SymPy reconstruction of the C149 orbit algebra."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c149_skeleton_evidence.json"


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

    lengths = tuple(data["finite_skeleton"]["cycle_lengths"])
    denominator = sp.prod(1 - z ** ell for ell in lengths)
    rational = sp.cancel(1 / denominator)
    series = sp.series(rational, z, 0, 31).removeO().expand()
    for degree, value in enumerate(data["finite_replay"]["zeta_coefficients"]):
        ck(series.coeff(z, degree) == value, f"zeta coefficient {degree}")

    formal_log = sp.Add(*[
        sp.Integer(row["fixed_points"]) * z ** row["period_n"] / row["period_n"]
        for row in data["finite_replay"]["rows"][:30]
    ])
    expected_log = sp.Add(*[
        sp.Add(*[z ** (ell * q) / q for q in range(1, 30 // ell + 1)])
        for ell in lengths
    ])
    ck(sp.expand(formal_log - expected_log) == 0, "formal logarithm through degree 30")

    for n in range(1, 61):
        fixed = sum(ell for ell in lengths if n % ell == 0)
        exact = sum(int(sp.mobius(n // d)) * sum(ell for ell in lengths if d % ell == 0) for d in sp.divisors(n))
        row = data["finite_replay"]["rows"][n - 1]
        ck(row["fixed_points"] == fixed, f"fixed n={n}")
        ck(row["exact_period_points"] == exact, f"Mobius n={n}")
        ck(exact % n == 0, f"cycle integrality n={n}")

    substitution = sp.Matrix([[1, 1], [1, 1]])
    lam = sp.Symbol("lambda")
    ck(substitution.charpoly(lam).as_expr() == lam ** 2 - 2 * lam, "TM substitution matrix")
    for receipt in data["thue_morse_component"]["period_certificates"]:
        p = sp.Integer(receipt["putative_period"])
        k = receipt["odd_exponent_k"]
        d = p * (2 ** k - 1)
        ck(int(d) == receipt["multiple_d"], f"TM multiple p={p}")
        ck(int(d) % int(p) == 0, f"TM divisibility p={p}")

    print(json.dumps({"status": "C149_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
