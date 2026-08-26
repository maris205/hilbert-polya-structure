#!/usr/bin/env python3
"""Independent exact checker for the C173 Lyness evidence."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


EXPECTED_SOURCE = "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f"
EXPECTED_SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    return sha256(
        json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def parse_q(text: str) -> Fraction:
    return Fraction(text)


def rational_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def lyness(point: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    first, second = point
    return second, (1 + second) / first


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c173_lyness_evidence.json",
    )
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    assertions = 0

    def check(condition: bool, label: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(label)

    check(data["payload_sha256"] == canonical_hash(data), "canonical payload hash")
    check(data["schema"] == "hcs-c173-lyness-five-cycle-obstruction-v1", "schema")
    check(data["candidate_id"] == "HCS-C173", "candidate")
    check(data["evaluation_date"] == "2026-08-26", "date")
    check(data["source_commit"] == EXPECTED_SOURCE, "source commit")
    check(data["scope_literal"] == EXPECTED_SCOPE, "scope")

    lock = data["source_lock"]
    expected_lock = {
        "phase_space": "X=(0,infinity)^2",
        "map": "F(x,y)=(y,(1+y)/x)",
        "clock": "one application of F is one tick",
        "measure": "dmu=dx*dy/(x*y)",
        "koopman_convention": "(U f)(x,y)=f(F(x,y))",
        "determinant_convention": "classical Artin--Mazur series requires finite #Fix(F^n); ordinary operator Fredholm determinant requires trace class",
        "cutoffs": {"fixed_set_n_max": 50, "rational_grid_rows": 100},
        "precision": "exact rational and symbolic algebra only",
        "training_data": "none",
        "forbidden_data": "target zero or divisor tables, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, and Route B",
    }
    for key, value in expected_lock.items():
        check(lock[key] == value, f"source lock {key}")

    iteration = data["iterate_theorem"]
    expected_iterations = {
        "F0": ["x", "y"],
        "F1": ["y", "(1+y)/x"],
        "F2": ["(1+y)/x", "(1+x+y)/(x*y)"],
        "F3": ["(1+x+y)/(x*y)", "(1+x)/y"],
        "F4": ["(1+x)/y", "x"],
        "F5": ["x", "y"],
        "global_identity": "F^5=id_X",
        "proof_status": "PROVED_BY_DIRECT_RATIONAL_SIMPLIFICATION",
    }
    for key, value in expected_iterations.items():
        check(iteration[key] == value, f"iterate theorem {key}")

    periodic = data["periodic_structure"]
    periodic_expected = {
        "golden_ratio": "phi=(1+sqrt(5))/2",
        "fixed_point": ["phi", "phi"],
        "fixed_point_unique_in_X": True,
        "least_periods": [1, 5],
        "all_nonfixed_points_have_exact_period_five": True,
        "proof_basis": "period divides prime order 5, and the unique period-one point is removed",
        "fixed_sets": "Fix(F^n)={(phi,phi)} for 5 not dividing n and X for 5 dividing n",
    }
    for key, value in periodic_expected.items():
        check(periodic[key] == value, f"periodic structure {key}")

    zeta = data["zeta_obstruction"]
    zeta_expected = {
        "artin_mazur_definition": "zeta_AM(z)=exp(sum_(n>=1) #Fix(F^n)*z^n/n) when every fixed set is finite",
        "first_failed_coefficient": 5,
        "failed_fixed_set": "Fix(F^5)=X is uncountable",
        "classical_artin_mazur_zeta_defined": False,
        "finite_orbit_euler_product_defined": False,
        "regularized_or_lefschetz_substitute_claimed": False,
    }
    for key, value in zeta_expected.items():
        check(zeta[key] == value, f"zeta obstruction {key}")

    geometry = data["geometry"]
    geometry_expected = {
        "jacobian_determinant": "(1+y)/x^2",
        "target_coordinate_product": "y*(1+y)/x",
        "density_pullback_identity": "|det DF|/(F_1*F_2)=1/(x*y)",
        "measure_invariant": True,
        "measure_sigma_finite": True,
        "inverse": "F^(-1)(x,y)=((1+x)/y,x)",
        "reversor": "R(x,y)=(y,x)",
        "reversor_identity": "R*F*R=F^(-1)",
        "reversor_involutive": True,
    }
    for key, value in geometry_expected.items():
        check(geometry[key] == value, f"geometry {key}")

    koopman = data["koopman_theorem"]
    koopman_expected = {
        "hilbert_space": "H=L^2(X,dx*dy/(x*y))",
        "convention": "U f=f o F",
        "unitary": True,
        "finite_order": "U^5=I",
        "omega": "exp(2*pi*i/5)",
        "spectral_projection": "P_j=(1/5)*sum_(r=0)^4 omega^(-j*r)*U^r",
        "projection_range": "ker(U-omega^j*I)",
        "projection_index_set": [0, 1, 2, 3, 4],
        "orthogonal_resolution": "P_j*P_k=delta_(j,k)*P_j and sum_j P_j=I",
        "all_five_eigenspaces_infinite_dimensional": True,
        "infinite_multiplicity_proof": "countably many disjoint positive-measure orbit tubes and localized Fourier symmetrization",
        "compact": False,
        "finite_schatten_class": False,
        "trace_class": False,
        "ordinary_fredholm_determinant_available": False,
        "self_adjoint": False,
        "self_adjoint_obstruction": "a self-adjoint unitary with U^5=I would satisfy U=I, but F is nontrivial modulo measure",
        "antiunitary_reversal": "Theta=V_R*K satisfies Theta*U*Theta^(-1)=U^(-1)",
    }
    for key, value in koopman_expected.items():
        check(koopman[key] == value, f"Koopman theorem {key}")

    grid = data["finite_regression_sentinels"]["rational_grid"]
    check(len(grid) == 100, "rational grid length")
    for index, row in enumerate(grid):
        a = index // 10 + 1
        b = index % 10 + 1
        check(row["a"] == a and row["b"] == b, f"grid indices {index}")
        initial = (Fraction(a, 3), Fraction(b, 5))
        check(row["initial"] == [rational_text(v) for v in initial], f"grid initial {index}")
        states = []
        point = initial
        for _ in range(5):
            point = lyness(point)
            states.append(point)
        expected_states = [[rational_text(v) for v in state] for state in states]
        check(row["iterates_1_through_5"] == expected_states, f"grid iterates {index}")
        decoded = [tuple(parse_q(v) for v in state) for state in row["iterates_1_through_5"]]
        check(decoded[-1] == initial, f"grid fifth return {index}")
        check(row["returns_at_five"] is True, f"grid return flag {index}")
        check(row["fixed_at_one"] == (states[0] == initial), f"grid fixed flag {index}")

    fixed_rows = data["finite_regression_sentinels"]["fixed_set_ledger"]
    check(len(fixed_rows) == 50, "fixed-set ledger length")
    for n, row in enumerate(fixed_rows, 1):
        divisible = n % 5 == 0
        check(row["n"] == n, f"fixed row n {n}")
        check(row["five_divides_n"] == divisible, f"fixed row divisibility {n}")
        check(
            row["fixed_set"] == ("entire_positive_quadrant" if divisible else "singleton_phi"),
            f"fixed row set {n}",
        )
        check(row["finite_fixed_count"] == (None if divisible else 1), f"fixed row count {n}")
    check(data["finite_regression_sentinels"]["sentinels_are_proof"] is False, "sentinel boundary")

    route = data["route_a"]
    check(
        route["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
        "Route-A tuple",
    )
    check(route["overall"] == "ROUTE_A_REJECTED", "Route-A overall")
    check(route["route_b_invocation_allowed"] is False, "Route-B firewall")

    boundary = data["claim_boundary"]
    for key in (
        "source_side_fifth_iterate_identity",
        "source_side_period_classification",
        "source_side_invariant_measure",
        "natural_koopman_spectral_decomposition",
    ):
        check(boundary[key] is True, f"positive boundary {key}")
    for key in (
        "classical_artin_mazur_zeta",
        "ordinary_fredholm_determinant",
        "prime_like_correspondence",
        "target_divisor_matching",
        "target_functional_equation",
        "target_counting_law",
        "arithmetic_local_data",
        "euler_factors",
        "root_numbers",
        "automorphy",
        "hilbert_polya_operator",
    ):
        check(boundary[key] is False, f"negative boundary {key}")

    integrity = data["integrity"]
    check(integrity["hard_gate_status"] == "PASS_WITH_OBSTRUCTION", "hard gate")
    check(integrity["pivot_required"] is False, "pivot")
    check(integrity["model_rejected_as_primary_route_a_candidate"] is True, "model rejection")
    check(integrity["finite_ledgers_are_proof"] is False, "finite proof boundary")
    check(integrity["external_reviewer_simulated"] is False, "review boundary")
    check(integrity["citation_population"] == 0, "citation population")

    print(
        json.dumps(
            {
                "status": "C173_CHECKER_PASS",
                "assertions": assertions,
                "payload_sha256": data["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
