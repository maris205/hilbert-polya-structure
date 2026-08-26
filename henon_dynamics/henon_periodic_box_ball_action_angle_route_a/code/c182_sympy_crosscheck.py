#!/usr/bin/env python3
"""SymPy reconstruction of the C182 lattice and cycle formulas."""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c182_periodic_bbs_evidence.json"


def smith_diagonal(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    form = smith_normal_form(sp.Matrix(matrix), domain=ZZ)
    return [abs(int(form[i, i])) for i in range(min(form.rows, form.cols)) if form[i, i]]


def lcm(values: list[int]) -> int:
    answer = 1
    for value in values:
        answer = answer * value // gcd(answer, value)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    finite = data["finite_regression_sentinels"]
    distinct_cycle_orders: set[int] = set()
    for level in finite["level_rows"]:
        L = level["L"]
        support = [entry["j"] for entry in level["content"]]
        vacancies = [entry["p_j"] for entry in level["content"]]
        for sector in level["sectors"]:
            matrix = sp.Matrix(sector["F_alpha"])
            if matrix.rows == 0:
                check(sector["det_F_alpha"] == 1, "vacuum determinant")
                check(sector["smith_invariants"] == [], "vacuum Smith")
            else:
                check(abs(int(matrix.det())) == sector["det_F_alpha"], "SymPy determinant")
                check(smith_diagonal(sector["F_alpha"]) == sector["smith_invariants"], "SymPy Smith F")
                alpha_product = sp.prod(sector["alpha"])
                predicted = sp.Integer(L) * sp.prod(vacancies[:-1]) / alpha_product
                check(sp.simplify(matrix.det() - predicted) == 0, "KTT determinant product")
            for translation in sector["translations"]:
                h = sp.Matrix(translation["h"])
                if matrix.rows:
                    solution = matrix.inv() * h
                    order = lcm([sp.denom(value) for value in solution])
                    augmented = [
                        sector["F_alpha"][i] + [translation["h"][i]]
                        for i in range(len(sector["F_alpha"]))
                    ]
                    check(order == translation["order"], "rational-denominator order")
                    check(smith_diagonal(augmented) == translation["augmented_smith_invariants"], "SymPy Smith augmented")
                    check(all(value.is_Integer for value in order * solution), "order kills translation")
                    for proper in sp.divisors(order):
                        if proper < order:
                            check(any(not value.is_Integer for value in proper * solution), "order minimality")
                else:
                    check(translation["order"] == 1, "vacuum translation order")

        for evolution in level["evolutions"]:
            spectrum = {row["order"]: row["points"] for row in evolution["cycle_spectrum"]}
            fixed = {row["n"]: row["fixed_points"] for row in evolution["fixed_point_prefix"]}
            distinct_cycle_orders.update(spectrum)
            for n in range(1, 13):
                primitive = sum(int(sp.mobius(n // d)) * fixed[d] for d in sp.divisors(n))
                check(primitive == spectrum.get(n, 0), "Mobius primitive points")
                check(primitive % n == 0, "primitive point/cycle divisibility")

    # A q-cycle permutation has characteristic polynomial x^q-1 and therefore
    # det(I-zP_q)=1-z^q.  Verify every small order occurring in the ledger.
    z, x = sp.symbols("z x")
    checked_orders = 0
    for order in sorted(distinct_cycle_orders):
        if order > 24:
            continue
        permutation = sp.zeros(order)
        for i in range(order):
            permutation[(i + 1) % order, i] = 1
        check(sp.expand(permutation.charpoly(x).as_expr() - (x**order - 1)) == 0, f"cycle charpoly {order}")
        check(sp.expand((sp.eye(order) - z * permutation).det() - (1 - z**order)) == 0, f"cycle determinant {order}")
        checked_orders += 1
    check(checked_orders > 0, "nonempty cycle determinant sample")

    # The exact sector multiplicity formula is reconstructed with SymPy's own
    # Mobius and binomial implementations.
    for level in finite["level_rows"]:
        content = level["content"]
        for sector in level["sectors"]:
            product_value = 1
            for position, entry in enumerate(content):
                m, p, alpha = entry["m_j"], entry["p_j"], sector["alpha"][position]
                total = 0
                for beta in sp.divisors(gcd(m, p)):
                    if beta % alpha == 0:
                        total += sp.mobius(beta // alpha) * sp.binomial((p + m) // beta - 1, m // beta - 1)
                check(int(total) == sector["lambda_exact_counts"][position], "SymPy Lambda Mobius")
                product_value *= int(total) // (m // alpha)
            check(product_value == sector["component_multiplicity"], "SymPy sector multiplicity")

    check(data["theorem"]["snf_order"].startswith("ord_alpha,l"), "evidence SNF theorem")
    check(data["theorem"]["zeta_koopman"].startswith("zeta_T(z)="), "evidence determinant theorem")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "evidence Route rejection")
    print(
        json.dumps(
            {
                "status": "C182_SYMPY_PASS",
                "checks": checks,
                "distinct_cycle_orders": len(distinct_cycle_orders),
                "small_cycle_determinants": checked_orders,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
