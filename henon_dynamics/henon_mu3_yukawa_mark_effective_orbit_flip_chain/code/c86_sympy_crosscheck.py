#!/usr/bin/env python3
"""SymPy radial-cube and quotient-spectrum cross-check for C86."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c86_effective_orbit_flip_chain_evidence.json"


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["schema_id"] == "hcs-c86-effective-orbit-one-bit-flip-chain-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"

    radial = sp.zeros(17)
    for degree in range(17):
        if degree:
            radial[degree, degree - 1] = degree
        if degree < 16:
            radial[degree, degree + 1] = 16 - degree
    variable = sp.symbols("lambda")
    expected_radial = sp.prod(variable - (16 - 2 * degree) for degree in range(17))
    assert sp.expand(radial.charpoly(variable).as_expr() - expected_radial) == 0

    rows = evidence["invariant_walsh_spectrum"]["rows"]
    orbit_polynomial = sum(sp.Integer(row["multiplicity"]) * variable ** row["degree"] for row in rows)
    assert sp.expand(orbit_polynomial - variable ** 16 * orbit_polynomial.subs(variable, 1 / variable)) == 0
    assert orbit_polynomial.subs(variable, 1) == 3024
    assert sum(row["eigenvalue"] * row["multiplicity"] for row in rows) == 0
    assert sum(row["eigenvalue"] ** 2 * row["multiplicity"] for row in rows) == 77760

    flow = evidence["repair_flow"]["actual_directed_edge_count"]
    for left in range(4):
        for right in range(4):
            assert flow.get(f"{left},{right}", 0) == flow.get(f"{right},{left}", 0)
    assert sum(flow.values()) == 16 * 65536
    assert flow["0,0"] == 445696
    print(json.dumps({
        "status": "C86_SYMPY_CROSSCHECK_PASS",
        "radial_eigenvalue_count": 17,
        "invariant_dimension": 3024,
        "second_spectral_moment": 77760,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
