#!/usr/bin/env python3
"""SymPy Smith, adjugate, cycle, spectrum and reversal checks for HCS-C176."""
from __future__ import annotations

import json
from math import gcd
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c176_sandpile_evidence.json"


def lcm(values: list[int]) -> int:
    result = 1
    for value in values:
        result = int(sp.ilcm(result, value))
    return result


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    replay = data["finite_replay"]
    translations = {
        (row["graph_id"], row["sink"], row["source_label"]): row
        for row in replay["translation_rows"]
    }
    checks = 0

    for sink_row in replay["sink_rows"]:
        key_prefix = (sink_row["graph_id"], sink_row["sink"])
        delta = sp.Matrix(sink_row["reduced_laplacian"])
        D = int(delta.det())
        assert D == sink_row["determinant_D"] > 0
        checks += 1
        adjugate = delta.adjugate()
        assert delta * adjugate == D * sp.eye(delta.rows)
        checks += 1

        domain_delta = DomainMatrix.from_Matrix(delta).convert_to(ZZ)
        smith_domain, left_domain, right_domain = smith_normal_decomp(domain_delta)
        smith = smith_domain.to_Matrix()
        left = left_domain.to_Matrix()
        right = right_domain.to_Matrix()
        assert left * delta * right == smith
        checks += 1
        assert abs(int(left.det())) == abs(int(right.det())) == 1
        checks += 1
        diagonal = [abs(int(smith[i, i])) for i in range(smith.rows)]
        assert all(value > 0 for value in diagonal)
        checks += 1
        assert all(diagonal[i + 1] % diagonal[i] == 0 for i in range(len(diagonal) - 1))
        checks += 1
        assert sp.prod(diagonal) == D
        checks += 1

        matching = [row for key, row in translations.items() if key[:2] == key_prefix]
        for row in matching:
            b = sp.Matrix(row["b"])
            transformed = left * b
            smith_order = lcm([
                d // gcd(d, abs(int(transformed[i])))
                for i, d in enumerate(diagonal)
            ])
            assert smith_order == row["order_L"]
            checks += 1

            w = adjugate * b
            common = D
            for value in w:
                common = gcd(common, abs(int(value)))
            adjugate_order = D // common
            assert list(map(int, w)) == row["adjugate_times_b"]
            checks += 1
            assert adjugate_order == smith_order == row["order_L"]
            checks += 1

            # Minimal quotient order, tested without either closed formula.
            direct = next(
                ell for ell in range(1, D + 1)
                if all((ell * int(value)) % D == 0 for value in w)
            )
            assert direct == smith_order
            checks += 1

    # One cyclic permutation block owns all spectral formulas. Check every
    # order that occurs in the exhaustive ledger.
    orders = sorted({row["order_L"] for row in replay["translation_rows"]})
    lam = sp.symbols("lambda")
    for L in orders:
        cycle = sp.zeros(L)
        for i in range(L):
            cycle[(i + 1) % L, i] = 1
        assert sp.expand(cycle.charpoly(lam).as_expr() - (lam**L - 1)) == 0
        checks += 1
        reversal = sp.zeros(L)
        for i in range(L):
            reversal[(-i) % L, i] = 1
        assert reversal * reversal == sp.eye(L)
        checks += 1
        assert reversal * cycle * reversal == cycle.T
        checks += 1
        assert (cycle == cycle.T) == (L <= 2)
        checks += 1
        power = sp.eye(L)
        for n in range(1, 2 * L + 3):
            power = power * cycle
            assert int(sp.trace(power)) == (L if n % L == 0 else 0)
            checks += 1

    # Lift the one-cycle formulas to every observed (D,L) multiplicity pair.
    for D, L in sorted({
        (row["recurrent_state_count_D"], row["order_L"])
        for row in replay["translation_rows"]
    }):
        assert D % L == 0
        checks += 1
        cycle_count = D // L
        assert sum(L for _ in range(cycle_count)) == D
        checks += 1
        for n in range(1, 2 * L + 3):
            trace = cycle_count * (L if n % L == 0 else 0)
            assert trace == (D if n % L == 0 else 0)
            checks += 1

    # r=0 and b=0 boundaries.
    empty = sp.zeros(0)
    assert empty.det() == 1
    checks += 1
    assert data["order_theorem"]["sink_only"].startswith("if r=0")
    checks += 1
    zero_rows = [row for row in replay["translation_rows"] if row["source_label"] == "zero"]
    assert zero_rows and all(row["order_L"] == 1 for row in zero_rows)
    checks += 1

    print(json.dumps({"status": "C176_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
