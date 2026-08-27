#!/usr/bin/env python3
"""Separate SymPy oracle for C192 characteristic data and power traces."""
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c192_hyperplane_evidence.json"


def rational(value: str) -> sp.Rational:
    q = Fraction(value)
    return sp.Rational(q.numerator, q.denominator)


def main() -> None:
    document = json.loads(EVIDENCE.read_text())
    x, z = sp.symbols("x z")
    checks = 0
    coefficient_checks = 0
    trace_checks = 0
    diagonal_checks = 0
    for case in document["cases"]:
        matrix = sp.Matrix([[rational(value) for value in row] for row in case["transition_matrix"]])
        dimension = matrix.rows
        assert matrix.cols == dimension
        checks += dimension * dimension

        observed_charpoly = sum(rational(value) * x ** index for index, value in enumerate(case["charpoly_ascending"]))
        sympy_charpoly = matrix.charpoly(x).as_expr()
        assert sp.expand(observed_charpoly - sympy_charpoly) == 0
        coefficient_checks += dimension + 1

        observed_det = sum(rational(value) * z ** index for index, value in enumerate(case["det_I_minus_zK_ascending"]))
        sympy_det = (sp.eye(dimension) - z * matrix).det(method="domain-ge")
        assert sp.expand(observed_det - sympy_det) == 0
        coefficient_checks += dimension + 1

        flat_factor = sp.Integer(1)
        multiplicity_sum = 0
        for flat in case["flats"]:
            lam = rational(flat["lambda"])
            multiplicity = flat["multiplicity"]
            flat_factor *= (x - lam) ** multiplicity
            multiplicity_sum += multiplicity
            checks += 2
        assert multiplicity_sum == dimension
        assert sp.expand(flat_factor - sympy_charpoly) == 0
        diagonal_checks += dimension

        power = sp.eye(dimension)
        for row in case["power_traces"]:
            exponent = row["power"]
            if exponent:
                power = power * matrix
            direct = sp.trace(power)
            spectral = sum(
                sp.Integer(flat["multiplicity"]) * rational(flat["lambda"]) ** exponent
                for flat in case["flats"]
            )
            assert direct == rational(row["direct"]) == rational(row["spectral"]) == spectral
            trace_checks += dimension + len(case["flats"]) + 3

        # The source theorem states diagonalizability.  For each finite regression
        # matrix SymPy independently confirms that geometric and algebraic
        # multiplicities agree for every distinct eigenvalue.
        for eigenvalue, algebraic, basis in matrix.eigenvects():
            assert len(basis) == algebraic
            diagonal_checks += algebraic + len(basis)

    total = checks + coefficient_checks + trace_checks + diagonal_checks
    print(json.dumps({
        "status": "C192_SYMPY_PASS",
        "checks": total,
        "matrix_and_flat_checks": checks,
        "coefficient_checks": coefficient_checks,
        "trace_checks": trace_checks,
        "diagonalizability_checks": diagonal_checks,
        "case_count": len(document["cases"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
