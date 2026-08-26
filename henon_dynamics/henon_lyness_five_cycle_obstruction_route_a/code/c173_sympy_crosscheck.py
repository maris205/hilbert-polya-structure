#!/usr/bin/env python3
"""SymPy reconstruction of the C173 identities without importing the producer."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c173_lyness_evidence.json",
    )
    args = parser.parse_args()
    evidence = json.loads(args.input.read_text())
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    x, y = sp.symbols("x y", positive=True)

    def F(point: tuple[sp.Expr, sp.Expr]) -> tuple[sp.Expr, sp.Expr]:
        first, second = point
        return sp.cancel(second), sp.cancel((1 + second) / first)

    expected = [
        (x, y),
        (y, (1 + y) / x),
        ((1 + y) / x, (1 + x + y) / (x * y)),
        ((1 + x + y) / (x * y), (1 + x) / y),
        ((1 + x) / y, x),
        (x, y),
    ]
    point = (x, y)
    for index in range(6):
        check(sp.cancel(point[0] - expected[index][0]) == 0, f"iterate {index} coordinate 1")
        check(sp.cancel(point[1] - expected[index][1]) == 0, f"iterate {index} coordinate 2")
        if index < 5:
            point = F(point)

    first, second = F((x, y))
    jacobian = sp.factor(sp.Matrix([first, second]).jacobian([x, y]).det())
    check(jacobian == (1 + y) / x**2, "Jacobian determinant")
    check(sp.cancel(jacobian / (first * second) - 1 / (x * y)) == 0, "invariant density")

    def R(point: tuple[sp.Expr, sp.Expr]) -> tuple[sp.Expr, sp.Expr]:
        return point[1], point[0]

    rfr = R(F(R((x, y))))
    inverse = ((1 + x) / y, x)
    check(sp.cancel(rfr[0] - inverse[0]) == 0, "reversor coordinate 1")
    check(sp.cancel(rfr[1] - inverse[1]) == 0, "reversor coordinate 2")
    check(F(inverse) == (x, y), "right inverse")

    phi = (1 + sp.sqrt(5)) / 2
    psi = (1 - sp.sqrt(5)) / 2
    check(sp.simplify(phi**2 - phi - 1) == 0, "positive fixed root")
    check(sp.simplify(psi**2 - psi - 1) == 0, "negative algebraic root")
    check(phi.is_positive is True, "phi positive")
    check(psi.is_negative is True, "psi excluded from positive quadrant")
    fixed_image = F((phi, phi))
    check(sp.simplify(fixed_image[0] - phi) == 0, "fixed point coordinate 1")
    check(sp.simplify(fixed_image[1] - phi) == 0, "fixed point coordinate 2")

    # Exact group-algebra verification of the projection sign convention.
    w = sp.symbols("w")
    cyclotomic = w**4 + w**3 + w**2 + w + 1

    def reduce_w(expr: sp.Expr) -> sp.Expr:
        return sp.rem(sp.Poly(sp.expand(expr), w, domain=sp.QQ), sp.Poly(cyclotomic, w, domain=sp.QQ)).as_expr()

    projections: list[list[sp.Expr]] = []
    for j in range(5):
        projections.append([reduce_w(w ** ((-j * r) % 5) / 5) for r in range(5)])

    def convolution(left: list[sp.Expr], right: list[sp.Expr]) -> list[sp.Expr]:
        result = []
        for m in range(5):
            coefficient = sum(left[r] * right[(m - r) % 5] for r in range(5))
            result.append(reduce_w(coefficient))
        return result

    for j in range(5):
        for k in range(5):
            product = convolution(projections[j], projections[k])
            target = projections[j] if j == k else [sp.Integer(0)] * 5
            for m in range(5):
                check(reduce_w(product[m] - target[m]) == 0, f"P{j}P{k} coefficient {m}")

    total = [reduce_w(sum(projections[j][m] for j in range(5))) for m in range(5)]
    for m in range(5):
        check(total[m] == (1 if m == 0 else 0), f"projection resolution coefficient {m}")

    for j in range(5):
        shifted = [projections[j][(m - 1) % 5] for m in range(5)]
        for m in range(5):
            check(
                reduce_w(shifted[m] - w**j * projections[j][m]) == 0,
                f"U P{j}=omega^{j} P{j} coefficient {m}",
            )

    # Independently decode selected regression rows and apply the map five times.
    grid = evidence["finite_regression_sentinels"]["rational_grid"]
    for row in grid[:25]:
        start = tuple(sp.Rational(value) for value in row["initial"])
        current = start
        for _ in range(5):
            current = F(current)
        check(current == start, f"grid symbolic fifth return {row['a']},{row['b']}")

    check(evidence["iterate_theorem"]["global_identity"] == "F^5=id_X", "evidence iteration identity")
    check(evidence["geometry"]["measure_invariant"] is True, "evidence measure identity")
    check(evidence["koopman_theorem"]["projection_range"] == "ker(U-omega^j*I)", "projection range sign")
    check(evidence["zeta_obstruction"]["first_failed_coefficient"] == 5, "first zeta failure")

    print(json.dumps({"status": "C173_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
