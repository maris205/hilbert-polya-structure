#!/usr/bin/env python3
"""Separate SymPy cross-check of selected C195 exact identities."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

EVIDENCE = Path(__file__).resolve().parents[1] / "results/c195_burgers_evidence.json"
Z = sp.Symbol("Z", nonzero=True)


def rat(text: str) -> sp.Rational:
    numerator, denominator = text.split("/")
    return sp.Rational(int(numerator), int(denominator))


def complex_rat(value: list[str]) -> sp.Expr:
    return rat(value[0]) + sp.I * rat(value[1])


def expression(rows: list[dict]) -> sp.Expr:
    return sum(complex_rat(row["coefficient"]) * Z ** row["mode"] for row in rows)


def d(expr: sp.Expr) -> sp.Expr:
    return sp.expand(sp.I * Z * sp.diff(expr, Z))


def canon(expr: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.together(sp.expand(expr)))


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    checks = 0

    def require(condition: bool) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(f"SymPy check {checks} failed")

    require(data["schema"] == "hcs-c195-periodic-burgers-v1")
    selected = [0, 1, 4, 7, 10, 13, 17, 20, 23]
    for index in selected:
        row = data["regression_rows"][index]
        nu = rat(row["nu"])
        mean = rat(row["mean_m"])
        w = expression(row["initial_coefficients"])
        a = d(w)
        b = d(a)
        c = d(b)
        wt = nu * b - mean * a
        at = d(wt)
        residual = (
            -2 * nu * (at * w - a * wt) * w
            - 2 * nu * (mean * w - 2 * nu * a) * (b * w - a * a)
            + 2 * nu ** 2 * (c * w * w - 3 * a * b * w + 2 * a ** 3)
        )
        require(canon(residual) == 0)
        require(expression(row["generator_residual_coefficients"]) == 0)

        rho = rat(row["snapshot_parameters"]["rho"])
        rotation = complex_rat(row["snapshot_parameters"]["rotation"])
        expected_snapshot = sum(
            complex_rat(cell["coefficient"]) * rho ** (cell["mode"] ** 2) * rotation ** cell["mode"] * Z ** cell["mode"]
            for cell in row["initial_coefficients"]
        )
        require(canon(expression(row["snapshot_coefficients"]) - expected_snapshot) == 0)

        rho2 = rat(row["second_snapshot_parameters"]["rho"])
        rotation2 = complex_rat(row["second_snapshot_parameters"]["rotation"])
        expected_composed = sum(
            complex_rat(cell["coefficient"]) * (rho * rho2) ** (cell["mode"] ** 2)
            * (rotation * rotation2) ** cell["mode"] * Z ** cell["mode"]
            for cell in row["initial_coefficients"]
        )
        require(canon(expression(row["composed_snapshot_coefficients"]) - expected_composed) == 0)
        require(canon(expression(row["direct_composed_snapshot_coefficients"]) - expected_composed) == 0)
        require(expression(row["semigroup_composition_residual_coefficients"]) == 0)

        r = row["first_active_mode"]
        a0 = next(complex_rat(cell["coefficient"]) for cell in row["initial_coefficients"] if cell["mode"] == 0)
        expected_leading = 0
        for cell in row["initial_coefficients"]:
            if abs(cell["mode"]) == r:
                expected_leading += -2 * nu * sp.I * cell["mode"] * complex_rat(cell["coefficient"]) / a0 * Z ** cell["mode"]
        require(canon(expression(row["leading_u_minus_m_coefficients"]) - expected_leading) == 0)
        require(rat(row["exact_decay_exponent"]) == nu * r * r)
        require(rat(row["certified_remainder_exponent"]) > nu * r * r)

        spectrum = {cell["mode"]: complex_rat(cell["eigenvalue"]) for cell in row["linearized_spectrum"]}
        for mode in (-8, -3, 0, 2, 8):
            require(spectrum[mode] == -nu * mode * mode - sp.I * mean * mode)

    require(data["summary"]["finite_rows_role"] == "REGRESSION_ONLY_NOT_PROOF")
    require(data["route_a"]["route_b_invocation_allowed"] is False)
    print(json.dumps({"status": "C195_SYMPY_PASS", "checks": checks, "selected_cases": len(selected)}, sort_keys=True))


if __name__ == "__main__":
    main()
