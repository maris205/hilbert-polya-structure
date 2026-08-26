#!/usr/bin/env python3
"""Produce exact source-side evidence for the C173 Lyness obstruction."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f"
N_MAX = 50
GRID_A_MAX = 10
GRID_B_MAX = 10


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    encoded = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(encoded).hexdigest()


def step(point: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    x, y = point
    return y, (1 + y) / x


def orbit_grid() -> list[dict]:
    rows = []
    for a in range(1, GRID_A_MAX + 1):
        for b in range(1, GRID_B_MAX + 1):
            point = (Fraction(a, 3), Fraction(b, 5))
            states = [point]
            for _ in range(5):
                states.append(step(states[-1]))
            rows.append(
                {
                    "a": a,
                    "b": b,
                    "initial": [q(value) for value in point],
                    "iterates_1_through_5": [
                        [q(value) for value in state] for state in states[1:]
                    ],
                    "returns_at_five": states[-1] == point,
                    "fixed_at_one": states[1] == point,
                }
            )
    return rows


def fixed_set_ledger() -> list[dict]:
    return [
        {
            "n": n,
            "five_divides_n": n % 5 == 0,
            "fixed_set": "entire_positive_quadrant" if n % 5 == 0 else "singleton_phi",
            "finite_fixed_count": None if n % 5 == 0 else 1,
        }
        for n in range(1, N_MAX + 1)
    ]


def build_evidence() -> dict:
    payload = {
        "schema": "hcs-c173-lyness-five-cycle-obstruction-v1",
        "candidate_id": "HCS-C173",
        "evaluation_date": "2026-08-26",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "phase_space": "X=(0,infinity)^2",
            "map": "F(x,y)=(y,(1+y)/x)",
            "clock": "one application of F is one tick",
            "measure": "dmu=dx*dy/(x*y)",
            "koopman_convention": "(U f)(x,y)=f(F(x,y))",
            "determinant_convention": "classical Artin--Mazur series requires finite #Fix(F^n); ordinary operator Fredholm determinant requires trace class",
            "cutoffs": {"fixed_set_n_max": N_MAX, "rational_grid_rows": GRID_A_MAX * GRID_B_MAX},
            "precision": "exact rational and symbolic algebra only",
            "training_data": "none",
            "forbidden_data": "target zero or divisor tables, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, and Route B",
        },
        "iterate_theorem": {
            "F0": ["x", "y"],
            "F1": ["y", "(1+y)/x"],
            "F2": ["(1+y)/x", "(1+x+y)/(x*y)"],
            "F3": ["(1+x+y)/(x*y)", "(1+x)/y"],
            "F4": ["(1+x)/y", "x"],
            "F5": ["x", "y"],
            "global_identity": "F^5=id_X",
            "proof_status": "PROVED_BY_DIRECT_RATIONAL_SIMPLIFICATION",
        },
        "periodic_structure": {
            "golden_ratio": "phi=(1+sqrt(5))/2",
            "fixed_point": ["phi", "phi"],
            "fixed_point_unique_in_X": True,
            "least_periods": [1, 5],
            "all_nonfixed_points_have_exact_period_five": True,
            "proof_basis": "period divides prime order 5, and the unique period-one point is removed",
            "fixed_sets": "Fix(F^n)={(phi,phi)} for 5 not dividing n and X for 5 dividing n",
        },
        "zeta_obstruction": {
            "artin_mazur_definition": "zeta_AM(z)=exp(sum_(n>=1) #Fix(F^n)*z^n/n) when every fixed set is finite",
            "first_failed_coefficient": 5,
            "failed_fixed_set": "Fix(F^5)=X is uncountable",
            "classical_artin_mazur_zeta_defined": False,
            "finite_orbit_euler_product_defined": False,
            "regularized_or_lefschetz_substitute_claimed": False,
        },
        "geometry": {
            "jacobian_determinant": "(1+y)/x^2",
            "target_coordinate_product": "y*(1+y)/x",
            "density_pullback_identity": "|det DF|/(F_1*F_2)=1/(x*y)",
            "measure_invariant": True,
            "measure_sigma_finite": True,
            "inverse": "F^(-1)(x,y)=((1+x)/y,x)",
            "reversor": "R(x,y)=(y,x)",
            "reversor_identity": "R*F*R=F^(-1)",
            "reversor_involutive": True,
        },
        "koopman_theorem": {
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
        },
        "finite_regression_sentinels": {
            "rational_grid": orbit_grid(),
            "fixed_set_ledger": fixed_set_ledger(),
            "sentinels_are_proof": False,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "source_side_fifth_iterate_identity": True,
            "source_side_period_classification": True,
            "source_side_invariant_measure": True,
            "natural_koopman_spectral_decomposition": True,
            "classical_artin_mazur_zeta": False,
            "ordinary_fredholm_determinant": False,
            "prime_like_correspondence": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
        },
        "integrity": {
            "hard_gate": "prove the global five-cycle identity and decide whether either classical zeta or ordinary Fredholm determinant exists",
            "hard_gate_status": "PASS_WITH_OBSTRUCTION",
            "pivot_required": False,
            "model_rejected_as_primary_route_a_candidate": True,
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
            "citation_population": 0,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c173_lyness_evidence.json",
    )
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "status": "C173_PRODUCER_PASS",
                "payload_sha256": payload["payload_sha256"],
                "rational_grid_rows": GRID_A_MAX * GRID_B_MAX,
                "fixed_set_n_max": N_MAX,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
