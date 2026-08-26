#!/usr/bin/env python3
"""Produce exact C185 evidence for the all-size Brockett sorting flow."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
import json
from math import factorial
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
EVALUATOR_PATH = "flow_systems/skills/route-a-evaluator.md"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
N_MIN, N_MAX = 2, 7


Matrix = list[list[Fraction]]


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def qtext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def eye(n: int) -> Matrix:
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def diagonal(values: list[int]) -> Matrix:
    n = len(values)
    return [[Fraction(values[i]) if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in bt] for row in a]


def subtract(a: Matrix, b: Matrix) -> Matrix:
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return subtract(multiply(a, b), multiply(b, a))


def trace(a: Matrix) -> Fraction:
    return sum((a[i][i] for i in range(len(a))), Fraction(0))


def frobenius_sq(a: Matrix) -> Fraction:
    return sum((x * x for row in a for x in row), Fraction(0))


def matrix_digest(a: Matrix) -> str:
    rows = [",".join(qtext(x) for x in row) for row in a]
    return sha256(("\n".join(rows) + "\n").encode()).hexdigest()


def rational_orthogonal(n: int) -> Matrix:
    """A deterministic product of adjacent 3-4-5 Givens rotations."""
    q = eye(n)
    c, s = Fraction(3, 5), Fraction(4, 5)
    for k in range(n - 1):
        g = eye(n)
        g[k][k], g[k][k + 1] = c, -s
        g[k + 1][k], g[k + 1][k + 1] = s, c
        q = multiply(q, g)
    assert multiply(transpose(q), q) == eye(n)
    return q


def inversion_count(perm: tuple[int, ...]) -> int:
    return sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm)))


def permutation_rows() -> tuple[list[dict], list[dict]]:
    rows: list[dict] = []
    summaries: list[dict] = []
    for n in range(N_MIN, N_MAX + 1):
        lam = list(range(1, n + 1))
        nu = [i * i for i in range(1, n + 1)]
        local: list[dict] = []
        for perm in permutations(lam):
            inv = inversion_count(perm)
            modes: list[list[int | str]] = []
            for i in range(n):
                for j in range(i + 1, n):
                    rate = (perm[i] - perm[j]) * (nu[j] - nu[i])
                    sign = "unstable" if rate > 0 else "stable"
                    modes.append([i + 1, j + 1, rate, sign])
            energy = sum(perm[i] * nu[i] for i in range(n))
            mode_digest = sha256(
                ("\n".join(f"{i},{j},{rate},{sign}" for i, j, rate, sign in modes) + "\n").encode()
            ).hexdigest()
            row = {
                "n": n,
                "permutation": list(perm),
                "height_Tr_DN": energy,
                "sorting_energy_minus_Tr_DN": -energy,
                "inversions": inv,
                "morse_index_of_minus_height": inv,
                "stable_modes": len(modes) - inv,
                "unstable_modes": inv,
                "zero_modes": 0,
                "pair_modes": modes,
                "pair_mode_digest": mode_digest,
            }
            local.append(row)
            rows.append(row)
        heights = [row["height_Tr_DN"] for row in local]
        maximizers = [row["permutation"] for row in local if row["height_Tr_DN"] == max(heights)]
        minimizers = [row["permutation"] for row in local if row["height_Tr_DN"] == min(heights)]
        summaries.append(
            {
                "n": n,
                "source_spectrum": lam,
                "target_diagonal": nu,
                "permutation_count": len(local),
                "pair_mode_count": sum(len(row["pair_modes"]) for row in local),
                "unique_height_maximizer": maximizers,
                "unique_height_minimizer": minimizers,
                "height_max": max(heights),
                "height_min": min(heights),
                "inversion_generating_coefficients": [
                    sum(row["inversions"] == k for row in local) for k in range(n * (n - 1) // 2 + 1)
                ],
            }
        )
        assert len(local) == factorial(n)
        assert maximizers == [lam]
        assert minimizers == [list(reversed(lam))]
    return rows, summaries


def matrix_regressions() -> list[dict]:
    rows: list[dict] = []
    for n in range(N_MIN, N_MAX + 1):
        lam = list(range(1, n + 1))
        nu = [i * i for i in range(1, n + 1)]
        q = rational_orthogonal(n)
        h = multiply(multiply(q, diagonal(lam)), transpose(q))
        target = diagonal(nu)
        generator = commutator(h, target)
        velocity = commutator(h, generator)
        derivative = trace(multiply(velocity, target))
        norm = frobenius_sq(generator)
        traces: list[str] = []
        power = eye(n)
        for k in range(1, n + 1):
            power = multiply(power, h)
            actual = trace(power)
            expected = Fraction(sum(x**k for x in lam))
            assert actual == expected
            traces.append(qtext(actual))
        assert derivative == norm and derivative > 0
        assert transpose(generator) == [[-x for x in row] for row in generator]
        assert transpose(velocity) == velocity
        rows.append(
            {
                "n": n,
                "source_spectrum": lam,
                "target_diagonal": nu,
                "givens_cosine": "3/5",
                "givens_sine": "4/5",
                "H_sha256": matrix_digest(h),
                "generator_sha256": matrix_digest(generator),
                "velocity_sha256": matrix_digest(velocity),
                "d_Tr_HN_dt": qtext(derivative),
                "commutator_frobenius_norm_sq": qtext(norm),
                "trace_powers_1_through_n": traces,
                "H_symmetric": True,
                "generator_skew_symmetric": True,
                "velocity_symmetric": True,
                "strict_off_equilibrium": True,
            }
        )
    return rows


def boundary_controls() -> dict:
    source_lam = [1, 1, 3]
    target_nu = [1, 4, 9]
    source_rates = [
        (source_lam[i] - source_lam[j]) * (target_nu[j] - target_nu[i])
        for i in range(3)
        for j in range(i + 1, 3)
    ]

    repeated_target = diagonal([1, 1, 4])
    c, s = Fraction(3, 5), Fraction(4, 5)
    rotation = [[c, -s, Fraction(0)], [s, c, Fraction(0)], [Fraction(0), Fraction(0), Fraction(1)]]
    rotated_h = multiply(multiply(rotation, diagonal([1, 2, 3])), transpose(rotation))
    target_commutator = commutator(rotated_h, repeated_target)
    assert target_commutator == [[Fraction(0) for _ in range(3)] for _ in range(3)]
    assert rotated_h[0][1] != 0
    target_rates = [
        (i + 1 - (j + 1)) * ([1, 1, 4][j] - [1, 1, 4][i])
        for i in range(3)
        for j in range(i + 1, 3)
    ]
    return {
        "status": "REPEATED_SPECTRUM_BOUNDARY_WITH_TARGET_MORSE_BOTT_SENTINEL",
        "repeated_source_spectrum": {
            "lambda": source_lam,
            "nu": target_nu,
            "distinct_diagonal_equilibria": 3,
            "naive_factorial_count": 6,
            "representative_pair_rates": source_rates,
            "zero_ambient_pair_rates": source_rates.count(0),
            "zero_rate_interpretation": "stabilizer/non-tangent direction on the lower-dimensional repeated-source orbit",
        },
        "repeated_target_spectrum": {
            "lambda": [1, 2, 3],
            "nu": [1, 1, 4],
            "rational_rotation": [[qtext(x) for x in row] for row in rotation],
            "non_diagonal_equilibrium_H": [[qtext(x) for x in row] for row in rotated_h],
            "commutator_is_zero": True,
            "representative_pair_rates": target_rates,
            "zero_pair_modes": target_rates.count(0),
            "continuous_equilibrium_family": "orthogonal rotations inside the repeated-N eigenspace",
        },
        "nonclaim": "no full classification or Bruhat/Schubert closure theorem is asserted at repeated spectra",
    }


def build_evidence() -> dict:
    perms, summaries = permutation_rows()
    regressions = matrix_regressions()
    pair_modes = sum(len(row["pair_modes"]) for row in perms)
    payload = {
        "schema": "hcs-c185-brockett-double-bracket-v1",
        "candidate_id": "HCS-C185",
        "evaluation_date": "2026-08-26",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "evaluator": {
            "skill_version": "0.2.0",
            "authority_path": EVALUATOR_PATH,
            "authority_sha256": EVALUATOR_SHA256,
        },
        "artifact_path_base": "henon_dynamics/henon_brockett_double_bracket_sorting_flow_route_a",
        "source_lock": {
            "family": "every n>=2, every real symmetric simple-spectrum orthogonal orbit, and every strictly increasing diagonal N",
            "flow": "dH/dt=[H,[H,N]]",
            "arithmetic_origin": "absent; source and target spectra are arbitrary ordered real data",
            "clock": "autonomous continuous flow time t",
            "normalization": "F(H)=Tr(HN) with the Frobenius norm identity dF/dt=||[H,N]||_F^2",
            "determinant_convention": "none; no dynamical zeta or Fredholm determinant is promoted",
            "cutoff": "all-n proof; exact permutation and pair-mode regression for 2<=n<=7",
            "precision": "exact integer and rational matrix arithmetic with symbolic identities",
            "allowed_data": "ordered real spectra, symmetric matrices, orthogonal conjugacy, commutators, and finite permutation controls",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "theorem": {
            "global_existence": "the compact orthogonal orbit is invariant, so the polynomial vector field has a global solution for every initial H",
            "isospectrality": "dH/dt=[H,K(H)] with K(H)=[H,N] skew-symmetric, hence H(t)=Q(t)H(0)Q(t)^T",
            "lyapunov_identity": "d Tr(HN)/dt=||[H,N]||_F^2, with equality zero exactly at equilibrium",
            "equilibria": "for simple source spectrum and strict diagonal N there are exactly n! diagonal permutation equilibria",
            "pair_linearization": "at D_pi, off-diagonal mode (i,j) has rate (lambda_pi(i)-lambda_pi(j))*(nu_j-nu_i)",
            "morse_index": "the Morse index of -Tr(HN) at D_pi equals inv(pi); stable and unstable dimensions for the ascent flow are C(n,2)-inv(pi) and inv(pi)",
            "generic_sorting": "every trajectory converges to one permutation equilibrium; outside the stable manifolds of the other equilibria it converges to the uniquely sorted diagonal",
            "no_recurrence": "strict Lyapunov monotonicity excludes every nonconstant recurrent or periodic orbit",
            "boundary": "repeated source spectra collapse permutation labels and can zero only ambient stabilizer pair rates, whereas repeated target spectra create genuine tangent zero modes and Morse--Bott equilibrium families; both lie outside the main theorem",
        },
        "regression_cutoff": {"n_min": N_MIN, "n_max": N_MAX, "source_spectrum": "1..n", "target_diagonal": "1^2..n^2"},
        "permutation_rows": perms,
        "size_summaries": summaries,
        "matrix_regressions": regressions,
        "boundary_controls": boundary_controls(),
        "counts": {
            "sizes": N_MAX - N_MIN + 1,
            "permutation_rows": len(perms),
            "pair_mode_rows": pair_modes,
            "matrix_regression_rows": len(regressions),
            "source_registry_population": 1,
            "reference_registry_population": 1,
            "all_n_theorem": True,
        },
        "source_registry": [
            {
                "key": "brockett_1991_sorting",
                "authors": "R. W. Brockett",
                "title": "Dynamical systems that sort lists, diagonalize matrices, and solve linear programming problems",
                "journal": "Linear Algebra and its Applications",
                "volume": 146,
                "pages": "79--91",
                "year": 1991,
                "doi": "10.1016/0024-3795(91)90021-N",
                "role": "classical ownership of the double-bracket gradient sorting and diagonalization framework",
            }
        ],
        "attribution_boundary": {
            "classical": "the double-bracket flow, its gradient interpretation, sorting role, and diagonalization application belong to Brockett",
            "package_synthesis": "the all-n proof ledger, finite exact regression, repeated-spectrum sentinel, and strict Route-A stop are an artifact-level synthesis; no mathematical priority is claimed",
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "ARBITRARY_REAL_SPECTRA_HAVE_NO_INTRINSIC_RATIONAL_PRIME_OR_PRIME_POWER_ORIGIN",
            "A1": "A1_FAIL",
            "A1_qualification": "STRICT_LYAPUNOV_FLOW_HAS_NO_NONCONSTANT_PERIODIC_ORBITS_CARRYING_ARITHMETIC_PAYLOAD",
            "A2": "A2_FAIL",
            "A2_qualification": "NO_SOURCE_OWNED_DYNAMICAL_ZETA_OR_TARGET_DIVISOR_MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "STATE_DEPENDENT_SKEW_LAX_GENERATOR_IS_ONLY_A_FORMAL_ORTHOGONAL_LIFT_NOT_A_FIXED_QUANTUM_OPERATOR",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "arithmetic_controls": [
            "replace integer regression spectra by arbitrary irrational simple spectra without changing the theorem",
            "randomly relabel or reverse the ordered source spectrum; only the inversion index changes",
            "compare prime-sized and composite-sized matrices; the same all-n theorem applies",
            "erase every external arithmetic label; the vector field and proof remain unchanged",
        ],
        "scope_flags": {
            "claimed_automorphy": False,
            "claimed_euler_factor": False,
            "claimed_hilbert_polya": False,
            "claimed_root_number": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_weil_compression": False,
            "route_b_invocation_allowed": False,
            "used_arithmetic_local_data": False,
            "used_target_prime_table": False,
            "used_target_zero_table": False,
        },
        "nonclaims": [
            "novelty or priority for Brockett's double-bracket sorting flow",
            "a full Bruhat or Schubert cell closure theorem",
            "a complete classification of the repeated-spectrum boundary or its target-degenerate Morse--Bott component",
            "rational-prime, prime-power, logarithmic-prime-clock, or arithmetic-local semantics",
            "a dynamical zeta, target divisor, functional equation, counting law, continuation, or Weil compression",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
        "integrity": {
            "finite_regressions_are_proof": False,
            "all_n_argument_location": ["THEOREM_PACKAGE.md", "paper/main.tex"],
            "external_reviewer_simulated": False,
            "acceptance_score_reported": False,
            "citation_population": 1,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c185_brockett_evidence.json",
    )
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "status": "C185_PRODUCER_PASS",
                "permutation_rows": payload["counts"]["permutation_rows"],
                "pair_mode_rows": payload["counts"]["pair_mode_rows"],
                "matrix_rows": payload["counts"]["matrix_regression_rows"],
                "payload_sha256": payload["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
