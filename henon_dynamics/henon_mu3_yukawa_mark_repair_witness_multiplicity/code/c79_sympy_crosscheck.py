#!/usr/bin/env python3
"""Small independent symbolic check for the C79 block polynomial."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from math import comb
from pathlib import Path
import json
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c79_repair_witness_multiplicity_evidence.json"


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["schema_id"] == "hcs-c79-repair-witness-multiplicity-prefreeze-v1"
    sizes = (1, 1, 2, 5)
    x, u, v = sp.symbols("x u v")
    symbolic = 0
    for state in product((0, 1), repeat=4):
        chosen = [i for i, full in enumerate(state) if full]
        term = x ** sum(sizes[i] for i in chosen)
        for i, full in enumerate(state):
            if not full:
                term *= (1 + x) ** sizes[i] - x ** sizes[i]
        rho = max(0, len(chosen) - 2)
        if len(chosen) <= 2:
            witness = 1
        elif len(chosen) == 3:
            witness = sum(sizes[i] for i in chosen)
        else:
            witness = sum(sizes[i] * sizes[j] for i, j in combinations(chosen, 2))
        symbolic += term * u ** rho * v ** witness
    symbolic = sp.expand((1 + x) ** 6 * (1 + x * u) * symbolic)
    actual = sp.expand(sum(
        int(value) * x ** int(k) * u ** int(rho) * v ** int(witness)
        for key, value in evidence["trivariate_generating_function"]["coefficient_table"].items()
        for k, rho, witness in [tuple(map(int, key.split(",")))]
    ))
    assert symbolic == actual
    assert sp.expand(symbolic.subs({u: 1, v: 1})) == sp.expand((1 + x) ** 16)
    assert sp.expand(symbolic.subs({x: 1, v: 1})) == 30400 + 32704 * u + 2368 * u ** 2 + 64 * u ** 3
    witness_marginal = {
        str(witness): int(value)
        for witness, value in evidence["witness_multiplicity_atlas"]["witness_value_counts"].items()
    }
    assert witness_marginal == {"1": 60800, "4": 3968, "7": 384, "8": 256, "25": 128}
    print(json.dumps({
        "status": "C79_SYMPY_CROSSCHECK_PASS",
        "trivariate_identity": True,
        "P_x_at_u1_v1": "(1+x)^16",
        "P_x1_at_v1": "30400+32704u+2368u^2+64u^3",
        "witness_values": [1, 4, 7, 8, 25],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
