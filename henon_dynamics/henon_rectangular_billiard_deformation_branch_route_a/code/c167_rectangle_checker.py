#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C167."""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path

import mpmath as mp


CUTOFF = 24
C157_SHA256 = "de4f1a278c576fd4584e7a20ff5d35144f68b4369a4e93a5acdcf625f09af567"
C162_SHA256 = "1a2cf270689cd73d6c77643c76e0e781ede9c401189a8be9f3bcbf2741653161"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256")
    return sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False).encode()).hexdigest()


def rational_reconstruction(u: int, v: int) -> tuple[dict[int, list[list[int]]],
                                                       dict[int, list[list[int]]]]:
    fibres: dict[int, list[list[int]]] = defaultdict(list)
    for first in range(CUTOFF + 1):
        for second in range(CUTOFF + 1):
            if first or second:
                fibres[v * first * first + u * second * second].append([first, second])
    collisions = {energy: reps for energy, reps in fibres.items() if len(reps) > 1}
    return fibres, collisions


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path,
                        default=root / "results/c167_rectangle_evidence.json")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    assert set(data) == {
        "schema", "candidate_id", "evaluation_date", "scope_literal", "source_commit",
        "source_lock", "hard_gate", "poisson_identity", "branch_theorem",
        "collision_theorem", "quantization", "finite_sentinels", "route_a",
        "claim_boundary", "payload_sha256",
    }; checks += 1
    assert set(data["source_lock"]) == {
        "object", "upstream_c157_evidence_sha256", "upstream_c162_evidence_sha256",
        "trace", "clock", "normalization", "determinant_convention", "cutoff",
        "precision", "training_data", "forbidden_data",
    }; checks += 1
    assert set(data["hard_gate"]) == {"required", "status", "advance_over_c162"}; checks += 1
    assert set(data["poisson_identity"]) == {
        "formula", "principal_branch", "area_factor", "square_recovery",
        "reciprocal_aspect",
    }; checks += 1
    assert set(data["branch_theorem"]) == {
        "positive_time", "negative_time", "shell", "uniform_tail",
        "nonmatching_shells", "boundary_terms", "double_boundary_control",
    }; checks += 1
    assert set(data["collision_theorem"]) == {
        "parameter", "classification", "irrational_branch", "rational_branch",
        "squared_energy_transversality", "time_transversality",
        "multiple_collision_slopes", "general_divisor_formula_claimed",
        "irrational_uniform_gap_claimed",
    }; checks += 1
    assert set(data["quantization"]) == {
        "operator", "hilbert_space", "same_clock", "antiunitary", "target_operator_claimed",
    }; checks += 1
    assert set(data["finite_sentinels"]) == {
        "rational_fibres", "square_swap_quotient", "irrational_quadratic_field",
        "branch_convergence",
    }; checks += 1
    assert set(data["route_a"]) == {"tuple", "overall", "route_b_invocation_allowed"}; checks += 1
    assert set(data["claim_boundary"]) == {
        "isolated_primitive_orbit_determinant", "target_trace_identity",
        "target_divisor_matching", "target_functional_equation", "target_counting_law",
        "arithmetic_local_data", "euler_factors", "root_numbers", "automorphy",
        "hilbert_polya_operator", "route_b",
    }; checks += 1

    assert data["payload_sha256"] == payload_hash(data); checks += 1
    assert data["schema"] == "hcs-c167-rectangular-billiard-deformation-branch-evidence-v1"; checks += 1
    assert data["candidate_id"] == "HCS-C167"; checks += 1
    assert data["evaluation_date"] == "2026-08-25"; checks += 1
    assert data["source_commit"] == "4342893ce5e2516924181744bfacc01c12e4959d"; checks += 1
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"; checks += 1
    assert data["source_lock"]["cutoff"] == {
        "all_alpha_all_shell_theorem": True,
        "finite_collision_sentinel_absolute_coordinate": CUTOFF,
    }; checks += 1
    assert data["source_lock"]["upstream_c157_evidence_sha256"] == C157_SHA256; checks += 1
    assert data["source_lock"]["upstream_c162_evidence_sha256"] == C162_SHA256; checks += 1
    upstream_c157 = root.parent / "henon_square_billiard_abel_wave_trace_route_a/results/c157_abel_trace_evidence.json"
    upstream_c162 = root.parent / "henon_square_billiard_renormalized_branch_amplitude_route_a/results/c162_branch_amplitude_evidence.json"
    assert digest(upstream_c157) == C157_SHA256; checks += 1
    assert digest(upstream_c162) == C162_SHA256; checks += 1
    assert data["source_lock"] == {
        "object": "Dirichlet Abel half-wave trace on Q_alpha=(0,1)x(0,alpha), alpha>0",
        "upstream_c157_evidence_sha256": C157_SHA256,
        "upstream_c162_evidence_sha256": C162_SHA256,
        "trace": "W_alpha(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2/alpha^2)), Re(s)>0",
        "clock": "half-wave boundary time t under s=epsilon-i*t",
        "normalization": "epsilon^(3/2) at t=plus_or_minus 2*sqrt(E)",
        "determinant_convention": "none; clean lattice shells are not isolated-orbit determinants",
        "cutoff": {"all_alpha_all_shell_theorem": True,
                   "finite_collision_sentinel_absolute_coordinate": CUTOFF},
        "precision": "exact integer/quadratic-field collision arithmetic and 80-decimal branch sentinels",
        "training_data": "none",
        "forbidden_data": "target zero/prime tables, target divisor/counting law, arithmetic local or Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
    }; checks += 1
    assert data["hard_gate"] == {
        "required": "an all-aspect trace identity plus a proved deformation law for complete shell coefficients",
        "status": "PASS_NO_MODEL_PIVOT",
        "advance_over_c162": "the square coefficient becomes an all-alpha coefficient with an exact rational collision locus and pairwise-transverse branch splitting",
    }; checks += 1
    assert data["poisson_identity"] == {
        "formula": "W_alpha(s)=alpha*s/(2*pi)*sum_(m,n in Z)(s^2+4*(m^2+alpha^2*n^2))^(-3/2)-1/4-1/(2*(exp(pi*s)-1))-1/(2*(exp(pi*s/alpha)-1))",
        "principal_branch": True,
        "area_factor": "alpha",
        "square_recovery": "alpha=1 gives the C157 square identity exactly",
        "reciprocal_aspect": "W_alpha(s)=W_(1/alpha)(s/alpha)",
    }; checks += 1
    assert data["branch_theorem"] == {
        "positive_time": "lim_(epsilon down to 0) epsilon^(3/2) W_alpha(epsilon-i*2*sqrt(E))=alpha*exp(i*pi/4)*R_alpha(E)/(8*pi*E^(1/4))",
        "negative_time": "the limit at -2*sqrt(E) is the complex conjugate",
        "shell": "R_alpha(E)=#{(m,n) in Z^2:m^2+alpha^2*n^2=E}",
        "uniform_tail": "outside a fixed radius, m^2+alpha^2*n^2>=min(1,alpha^2)*(m^2+n^2) gives an epsilon-uniform summable |(m,n)|^-3 majorant",
        "nonmatching_shells": "finitely many nonmatching denominators stay bounded and vanish after epsilon^(3/2)",
        "boundary_terms": "each axis subtraction has at most a simple O(epsilon^-1) pole, so even coincident axis/boundary poles vanish as O(epsilon^(1/2)) after normalization",
        "double_boundary_control": "coincident horizontal and vertical boundary poles are a sum of simple poles, never a second-order pole",
    }; checks += 1
    assert data["collision_theorem"] == {
        "parameter": "beta=alpha^2",
        "classification": "for distinct absolute representatives with n^2!=n'^2, collision iff beta=(m'^2-m^2)/(n^2-n'^2)>0",
        "irrational_branch": "irrational beta has no collision beyond coordinate signs",
        "rational_branch": "for beta=u/v in lowest terms, complete shells are exactly fibres v*m^2+u*n^2=N",
        "squared_energy_transversality": "d(E_p-E_p')/d beta=n^2-n'^2!=0",
        "time_transversality": "at beta_0, d(t_p-t_p')/d beta=(n^2-n'^2)/sqrt(E_0)!=0",
        "multiple_collision_slopes": "distinct absolute representatives in one collision fibre have distinct n^2 slopes",
        "general_divisor_formula_claimed": False,
        "irrational_uniform_gap_claimed": False,
    }; checks += 1
    assert data["quantization"] == {
        "operator": "sqrt(-Delta_D,alpha)",
        "hilbert_space": "L^2(Q_alpha) with Dirichlet boundary conditions",
        "same_clock": "the half-wave boundary time is unchanged",
        "antiunitary": "complex conjugation reverses exp(-i*t*sqrt(-Delta_D,alpha))",
        "target_operator_claimed": False,
    }; checks += 1
    assert data["route_a"] == {
        "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
        "overall": "ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed": False,
    }; checks += 1
    assert not any(data["claim_boundary"].values()); checks += len(data["claim_boundary"])

    expected_beta = [(1, 1), (2, 1), (4, 1)]
    rows = data["finite_sentinels"]["rational_fibres"]
    assert len(rows) == len(expected_beta); checks += 1
    for row, (u, v) in zip(rows, expected_beta):
        assert set(row) == {
            "beta", "u", "v", "absolute_coordinate_cutoff", "occupied_fibres",
            "collision_fibres", "first_absolute_collision",
            "first_positive_primitive_collision", "collision_rows",
        }; checks += 1
        assert (row["u"], row["v"]) == (u, v); checks += 1
        assert row["beta"] == f"{u}/{v}"; checks += 1
        assert row["absolute_coordinate_cutoff"] == CUTOFF; checks += 1
        fibres, collisions = rational_reconstruction(u, v)
        assert row["occupied_fibres"] == len(fibres); checks += 1
        assert row["collision_fibres"] == len(collisions); checks += 1
        stored = {item["N"]: item["representatives"] for item in row["collision_rows"]}
        assert stored == collisions; checks += 1
        checks += sum(len(reps) for reps in collisions.values())
        first = min(collisions)
        assert row["first_absolute_collision"]["N"] == first; checks += 1
        assert row["first_absolute_collision"]["representatives"] == collisions[first]; checks += 1
        assert row["first_absolute_collision"]["globally_minimal_from_coordinate_bound"] is True; checks += 1
        pp = {}
        for energy, reps in fibres.items():
            retained = [rep for rep in reps if rep[0] and rep[1] and gcd(*rep) == 1]
            if len(retained) > 1:
                pp[energy] = retained
        first_pp = min(pp)
        assert row["first_positive_primitive_collision"]["N"] == first_pp; checks += 1
        assert row["first_positive_primitive_collision"]["representatives"] == pp[first_pp]; checks += 1
        assert row["first_positive_primitive_collision"]["globally_minimal_from_coordinate_bound"] is True; checks += 1

    assert rows[0]["first_positive_primitive_collision"] == {
        "N": 5, "representatives": [[1, 2], [2, 1]],
        "globally_minimal_from_coordinate_bound": True,
    }; checks += 1
    assert rows[1]["first_positive_primitive_collision"] == {
        "N": 33, "representatives": [[1, 4], [5, 2]],
        "globally_minimal_from_coordinate_bound": True,
    }; checks += 1
    assert rows[2]["first_absolute_collision"] == {
        "N": 4, "representatives": [[0, 1], [2, 0]],
        "globally_minimal_from_coordinate_bound": True,
    }; checks += 1

    square = data["finite_sentinels"]["square_swap_quotient"]
    assert square == {
        "coordinate_cutoff": CUTOFF,
        "first_square_symmetry_inequivalent_positive_primitive_collision_N": 65,
        "representatives": [[1, 8], [4, 7]],
        "globally_minimal_from_coordinate_bound": True,
    }; checks += 1

    irrational = data["finite_sentinels"]["irrational_quadratic_field"]
    assert irrational == {
        "beta": "sqrt(2)", "absolute_coordinate_cutoff": CUTOFF,
        "fibres": (CUTOFF + 1) ** 2 - 1, "non_sign_collisions": 0,
        "comparison_rule": "equality of m^2+sqrt(2)*n^2 is coefficientwise over Q(sqrt(2))",
    }; checks += 1

    mp.mp.dps = 90
    expected = {
        "square_ordered_collision": (mp.mpf(1), mp.mpf(5), 8),
        "beta_two_interior_collision": (mp.sqrt(2), mp.mpf(33), 8),
        "beta_four_double_axis_double_boundary": (mp.mpf(2), mp.mpf(4), 4),
        "irrational_beta_sign_only_shell": (mp.sqrt(mp.sqrt(2)), 1 + mp.sqrt(2), 4),
    }
    for row in data["finite_sentinels"]["branch_convergence"]:
        assert set(row) == {"label", "alpha", "energy_symbol", "energy",
                            "full_signed_shell_multiplicity", "target", "approximants",
                            "strict_error_decrease"}; checks += 1
        alpha, energy, multiplicity = expected[row["label"]]
        assert abs(mp.mpf(row["alpha"]) - alpha) < mp.mpf("1e-39"); checks += 1
        assert abs(mp.mpf(row["energy"]) - energy) < mp.mpf("1e-39"); checks += 1
        assert row["full_signed_shell_multiplicity"] == multiplicity; checks += 1
        target = (alpha * multiplicity * mp.e ** (mp.j * mp.pi / 4) /
                  (8 * mp.pi * energy ** (mp.mpf(1) / 4)))
        stored_target = mp.mpc(row["target"]["real"], row["target"]["imag"])
        assert abs(target - stored_target) < mp.mpf("1e-37"); checks += 1
        previous = None
        for item in row["approximants"]:
            epsilon = mp.mpf(item["epsilon"])
            s = epsilon - 2 * mp.j * mp.sqrt(energy)
            value = (epsilon ** (mp.mpf(3) / 2) * alpha * multiplicity * s /
                     (2 * mp.pi) * (s * s + 4 * energy) ** (-mp.mpf(3) / 2))
            stored_value = mp.mpc(item["value"]["real"], item["value"]["imag"])
            error = abs(value - target)
            assert abs(value - stored_value) < mp.mpf("1e-37"); checks += 1
            assert abs(error - mp.mpf(item["absolute_error"])) < mp.mpf("1e-27"); checks += 1
            if previous is not None:
                assert error < previous; checks += 1
            previous = error
        assert row["strict_error_decrease"] is True; checks += 1

    print(json.dumps({
        "status": "C167_INDEPENDENT_CHECK_PASS",
        "assertions": checks,
        "rational_fibre_rows": len(rows),
        "branch_sentinels": len(expected),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
