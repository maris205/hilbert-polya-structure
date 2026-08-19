#!/usr/bin/env python3
"""SymPy/GAP cross-check for C73 blocker and reliability formulae."""

from __future__ import annotations

from collections import Counter
from itertools import product
import json
from pathlib import Path
import subprocess

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c73_generation_blocker_reliability_evidence.json"


def coefficient_map(poly: sp.Expr, variable: sp.Symbol) -> dict[str, int]:
    expanded = sp.Poly(sp.expand(poly), variable)
    return {str(power[0]): int(value) for power, value in expanded.terms()}


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    x, q = sp.symbols("x q")
    independent = 1 + ((1 + x) - 1) * 2 + ((1 + x) ** 2 - 1) + ((1 + x) ** 5 - 1)
    assert sp.expand(independent) == 1 + 9 * x + 11 * x ** 2 + 10 * x ** 3 + 5 * x ** 4 + x ** 5
    cover = sp.expand(x ** 9 * independent.subs(x, 1 / x))
    assert coefficient_map(cover, x) == {"4": 1, "5": 5, "6": 10,
                                           "7": 11, "8": 9, "9": 1}
    transversal = sp.expand(x * (1 + x) ** 15 + (1 + x) ** 6 * cover)
    spectrum = evidence["deletion_spectrum"]["rows"]
    assert coefficient_map(transversal, x) == {
        str(row["deleted_count"]): row["destructive_count"]
        for row in spectrum if row["destructive_count"]
    }
    assert int(transversal.subs(x, 1)) == 35136

    q0, q1, q2, q3, q9 = sp.symbols("q0 q1 q2 q3 q9")
    block_failures = (q0, q1, q2, q3)
    odd_success = 0
    successful_block_states = 0
    for failure_state in product((0, 1), repeat=4):
        if sum(failure_state) > 2:
            continue
        successful_block_states += 1
        state_probability = 1
        for failed, failure_probability in zip(failure_state, block_failures):
            state_probability *= failure_probability if failed else 1 - failure_probability
        odd_success += state_probability
    assert successful_block_states == 11
    heterogeneous = sp.expand((1 - q9) * odd_success)
    expected_heterogeneous = (1 - q9) * (
        1 - (q1 * q2 * q3 + q0 * q2 * q3 + q0 * q1 * q3 + q0 * q1 * q2)
        + 3 * q0 * q1 * q2 * q3
    )
    assert sp.expand(heterogeneous - expected_heterogeneous) == 0

    reliability = sp.expand(heterogeneous.subs({
        q0: q, q1: q, q2: q ** 2, q3: q ** 5, q9: q,
    }))
    expected_reliability = sp.expand(
        (1 - q) * (1 - q ** 4 - q ** 7 - 2 * q ** 8 + 3 * q ** 9)
    )
    assert reliability == expected_reliability
    assert coefficient_map(reliability, q) == evidence["exact_reliability"]["homogeneous_expanded_coefficients"]
    assert reliability.subs(q, 0) == 1 and reliability.subs(q, 1) == 0

    gap = subprocess.run(
        ["gap", "-q"],
        input=(
            'G:=DirectProduct(SymmetricGroup(6),SymmetricGroup(2),'
            'SymmetricGroup(2),SymmetricGroup(5));; Print(Size(G),"\\n"); QUIT;\n'
        ),
        capture_output=True, text=True, check=True,
    )
    assert int(gap.stdout.strip()) == evidence["hypergraph_symmetry"]["abstract_hypergraph_automorphism_order"] == 345600
    assert evidence["blocker_geometry"]["minimal_blocker_polynomial_coefficients"] == {
        "1": 1, "4": 1, "7": 1, "8": 2
    }
    print(json.dumps({
        "status": "POLYNOMIAL_CROSSCHECK_PASS",
        "transversal_count": 35136,
        "reliability_from_block_states": "verified",
        "successful_block_failure_states": successful_block_states,
        "gap_structural_direct_product_order": 345600,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
