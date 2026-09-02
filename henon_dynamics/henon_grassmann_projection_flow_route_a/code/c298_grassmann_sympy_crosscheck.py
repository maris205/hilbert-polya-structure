#!/usr/bin/env python3
"""Independent SymPy identities for the HCS-C298 Grassmann flow."""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def minor(matrix: sp.Matrix, rows: tuple[int, ...]) -> sp.Expr:
    return matrix.extract(rows, range(matrix.cols)).det()


def main() -> None:
    data = json.loads((ROOT / "results/c298_grassmann_evidence.json").read_text())
    checks = 0

    def check(value, label):
        nonlocal checks
        checks += 1
        if value is not True and value != sp.true:
            raise AssertionError(label)

    # Universal projector-vector-field algebra in a fixed rank-two chart.
    entries = sp.symbols("a00 a01 a02 a03 a11 a12 a13 a22 a23 a33")
    a00, a01, a02, a03, a11, a12, a13, a22, a23, a33 = entries
    A = sp.Matrix([
        [a00, a01, a02, a03], [a01, a11, a12, a13],
        [a02, a12, a22, a23], [a03, a13, a23, a33],
    ])
    P = sp.diag(1, 1, 0, 0)
    double = P * (P * A - A * P) - (P * A - A * P) * P
    riccati = A * P + P * A - 2 * P * A * P
    for i in range(4):
        for j in range(4):
            check(sp.expand(double[i, j] - riccati[i, j]) == 0, f"double bracket {i}:{j}")
    check(double.T == double, "tangent symmetry")
    check(P * double + double * P == double, "projector tangent identity")
    comm = P * A - A * P
    check(sp.expand(sp.trace(A * double) - sp.trace(comm.T * comm)) == 0, "Lyapunov identity")

    # A nontrivial exact all-time rank-one solution.
    t = sp.symbols("t", real=True)
    D2 = sp.diag(sp.exp(-t), sp.exp(2 * t))
    y = D2 * sp.Matrix([1, 2])
    exact = sp.simplify(y * y.T / (y.T * y)[0])
    A2 = sp.diag(-1, 2)
    rhs = exact * (exact * A2 - A2 * exact) - (exact * A2 - A2 * exact) * exact
    for i in range(2):
        for j in range(2):
            check(sp.simplify(sp.diff(exact[i, j], t) - rhs[i, j]) == 0, f"exact ODE {i}:{j}")
    check(sp.simplify(exact.det()) == 0, "rank one")
    check(sp.simplify(sp.trace(exact)) == 1, "trace one")
    check(sp.simplify(exact * exact - exact) == sp.zeros(2), "idempotence")

    # Exterior-power and maximal-minor scaling, including negative exponents.
    x = sp.symbols("x", positive=True)
    for case in data["enumeration"]["simple_cases"]:
        eigenvalues = case["eigenvalues_strictly_increasing"]
        frame = sp.Matrix(case["integer_frame"])
        scaled = sp.diag(*[x**value for value in eigenvalues]) * frame
        k = frame.cols
        support = {tuple(item["subset"]): item for item in case["plucker_support"]}
        for rows in itertools.combinations(range(frame.rows), k):
            base = minor(frame, rows)
            evolved = minor(scaled, rows)
            weight = sum(eigenvalues[i] for i in rows)
            check(sp.simplify(evolved - x**weight * base) == 0, f"minor scaling {case['case_id']}:{rows}")
            if base:
                recorded = support[tuple(i + 1 for i in rows)]
                check(recorded["minor"] == base and recorded["weight"] == weight, f"minor ledger {case['case_id']}:{rows}")
        weights = [item["weight"] for item in case["plucker_support"]]
        check(max(weights) == case["leading_weight"], f"leading {case['case_id']}")
        check(sorted(weights, reverse=True)[1] == case["second_nonzero_weight"], f"second {case['case_id']}")
        check(case["exact_rate_gap"] == case["leading_weight"] - case["second_nonzero_weight"] > 0, f"gap {case['case_id']}")

    tie_case = data["enumeration"]["simple_cases"][1]
    lambdas = tie_case["eigenvalues_strictly_increasing"]
    check(lambdas[0] + lambdas[3] == lambdas[1] + lambdas[2], "ambient subset-sum tie retained")
    check(tie_case["greedy_leading_subset"] == [3, 4], "tie-safe greedy leader")

    # Linearization at every recorded simple-spectrum coordinate plane.
    for case in data["enumeration"]["simple_cases"]:
        eigenvalues = case["eigenvalues_strictly_increasing"]
        n = len(eigenvalues)
        diagonal = sp.diag(*eigenvalues)
        selected = {i - 1 for i in case["greedy_leading_subset"]}
        equilibrium = sp.diag(*[int(i in selected) for i in range(n)])
        stable = unstable = 0
        for mode in case["linear_modes"]:
            i, j = mode["selected_i"] - 1, mode["unselected_j"] - 1
            H = sp.zeros(n)
            H[i, j] = H[j, i] = 1
            linear = equilibrium * (H * diagonal - diagonal * H) - (H * diagonal - diagonal * H) * equilibrium
            rate = eigenvalues[j] - eigenvalues[i]
            check(linear == rate * H, f"linear mode {case['case_id']}:{i}:{j}")
            check(mode["rate_lambda_j_minus_lambda_i"] == rate, f"recorded mode {case['case_id']}:{i}:{j}")
            stable += rate < 0
            unstable += rate > 0
        check(stable == case["stable_dimension"], f"stable count {case['case_id']}")
        check(unstable == case["unstable_dimension"], f"unstable count {case['case_id']}")

    # Exact rational projector and strict Lyapunov rows from both regimes.
    all_cases = data["enumeration"]["simple_cases"] + data["enumeration"]["repeated_cases"]
    for case in all_cases:
        eigenvalues = case.get("eigenvalues_strictly_increasing", case.get("eigenvalues_nondecreasing"))
        frame = sp.Matrix(case["integer_frame"])
        projector = frame * (frame.T * frame).inv() * frame.T
        recorded = sp.Matrix([[sp.Rational(value) for value in row] for row in case["rational_initial_data"]["initial_projection"]])
        check(projector == recorded, f"projector {case['case_id']}")
        check(projector.T == projector and projector * projector == projector, f"projector laws {case['case_id']}")
        diagonal = sp.diag(*eigenvalues)
        commutator = projector * diagonal - diagonal * projector
        derivative = sp.trace(commutator.T * commutator)
        check(derivative == sp.Rational(case["rational_initial_data"]["commutator_frobenius_square"]), f"Lyapunov row {case['case_id']}")
        check(derivative > 0, f"strict row {case['case_id']}")

    # Repeated-spectrum top weight and associated-graded occupancy identities.
    for case in data["enumeration"]["repeated_cases"]:
        blocks = case["eigenvalue_blocks"]
        occupancy = case["associated_graded_occupancies"]
        check(sum(occupancy) == case["k"], f"occupancy rank {case['case_id']}")
        check(all(0 <= value <= block["multiplicity"] for value, block in zip(occupancy, blocks)), f"occupancy bounds {case['case_id']}")
        expected_weight = sum(value * block["value"] for value, block in zip(occupancy, blocks))
        check(expected_weight == case["top_plucker_weight"], f"graded weight {case['case_id']}")
        top_rows = [row for row in case["plucker_support"] if row["weight"] == expected_weight]
        check(top_rows == case["top_weight_plucker_coordinates"], f"top weight vector {case['case_id']}")
        check(case["top_weight_coordinate_count"] == len(top_rows), f"top coordinate count {case['case_id']}")

    # Every product-Grassmann critical component closes its tangent/normal dimensions.
    for atlas in data["enumeration"]["morse_bott_atlases"]:
        m = atlas["multiplicities"]
        values = atlas["eigenvalue_values"]
        for component in atlas["components"]:
            occupancy = component["occupancy"]
            tangent = sum(occupancy[a] * (m[a] - occupancy[a]) for a in range(len(m)))
            stable = sum(occupancy[a] * (m[b] - occupancy[b]) for a in range(len(m)) for b in range(a))
            unstable = sum(occupancy[a] * (m[b] - occupancy[b]) for a in range(len(m)) for b in range(a + 1, len(m)))
            check(component["critical_manifold_dimension"] == tangent, f"Morse tangent {atlas['config_id']}:{occupancy}")
            check(component["stable_normal_dimension"] == stable, f"Morse stable {atlas['config_id']}:{occupancy}")
            check(component["unstable_normal_dimension"] == unstable, f"Morse unstable {atlas['config_id']}:{occupancy}")
            check(tangent + stable + unstable == atlas["grassmann_dimension"] == component["dimension_closure"], f"Morse closure {atlas['config_id']}:{occupancy}")
            check(component["critical_value_trace_A_P"] == sum(values[a] * occupancy[a] for a in range(len(values))), f"critical value {atlas['config_id']}:{occupancy}")

    print(f"C298 SymPy cross-check: PASS ({checks} symbolic checks; tied weights preserved)")


if __name__ == "__main__":
    main()
