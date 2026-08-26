#!/usr/bin/env python3
"""Independent exact checker for C185; deliberately imports no producer code."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
import json
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c185_brockett_evidence.json"
EXPECTED_SOURCE = "908a6818caedb0c46195a591873a2ac9c685b55e"
EXPECTED_EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"

Matrix = list[list[Fraction]]


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    return sha256(
        json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def need(condition: bool, message: str, counter: list[int]) -> None:
    counter[0] += 1
    if not condition:
        raise AssertionError(message)


def exact_keys(mapping: dict, expected: set[str], label: str, counter: list[int]) -> None:
    need(set(mapping) == expected, f"{label} keys", counter)


def frac(text: str) -> Fraction:
    a, b = text.split("/")
    return Fraction(int(a), int(b))


def ident(n: int) -> Matrix:
    return [[Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]


def diag(values: list[int]) -> Matrix:
    return [[Fraction(values[i] if i == j else 0) for j in range(len(values))] for i in range(len(values))]


def trans(a: Matrix) -> Matrix:
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def product(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0)) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def difference(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def bracket(a: Matrix, b: Matrix) -> Matrix:
    return difference(product(a, b), product(b, a))


def tr(a: Matrix) -> Fraction:
    return sum((a[i][i] for i in range(len(a))), Fraction(0))


def norm2(a: Matrix) -> Fraction:
    return sum((entry * entry for row in a for entry in row), Fraction(0))


def digest_matrix(a: Matrix) -> str:
    text = "\n".join(
        ",".join(f"{x.numerator}/{x.denominator}" for x in row) for row in a
    ) + "\n"
    return sha256(text.encode()).hexdigest()


def orthogonal_sample(n: int) -> Matrix:
    q = ident(n)
    c, s = Fraction(3, 5), Fraction(4, 5)
    for k in range(n - 1):
        g = ident(n)
        g[k][k], g[k][k + 1] = c, -s
        g[k + 1][k], g[k + 1][k + 1] = s, c
        q = product(q, g)
    return q


def invs(p: tuple[int, ...]) -> int:
    total = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            total += int(p[i] > p[j])
    return total


def validate(payload: dict) -> int:
    checks = [0]
    top_keys = {
        "schema", "candidate_id", "evaluation_date", "scope_literal", "source_commit",
        "evaluator", "artifact_path_base", "source_lock", "theorem", "regression_cutoff",
        "permutation_rows", "size_summaries", "matrix_regressions", "boundary_controls",
        "counts", "source_registry", "attribution_boundary", "route_a_verdict",
        "arithmetic_controls", "scope_flags", "nonclaims", "integrity", "payload_sha256",
    }
    exact_keys(payload, top_keys, "top", checks)
    need(payload["payload_sha256"] == canonical_hash(payload), "payload hash", checks)
    need(payload["schema"] == "hcs-c185-brockett-double-bracket-v1", "schema", checks)
    need(payload["candidate_id"] == "HCS-C185", "candidate", checks)
    need(payload["evaluation_date"] == "2026-08-26", "date", checks)
    need(payload["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope", checks)
    need(payload["source_commit"] == EXPECTED_SOURCE, "source commit", checks)
    need(payload["artifact_path_base"] == "henon_dynamics/henon_brockett_double_bracket_sorting_flow_route_a", "artifact path", checks)
    need(payload["evaluator"] == {
        "skill_version": "0.2.0",
        "authority_path": "flow_systems/skills/route-a-evaluator.md",
        "authority_sha256": EXPECTED_EVALUATOR,
    }, "evaluator", checks)

    source_lock = payload["source_lock"]
    exact_keys(source_lock, {
        "family", "flow", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data",
    }, "source lock", checks)
    need(source_lock["family"] == "every n>=2, every real symmetric simple-spectrum orthogonal orbit, and every strictly increasing diagonal N", "family lock", checks)
    need(source_lock["flow"] == "dH/dt=[H,[H,N]]", "flow lock", checks)
    need(source_lock["arithmetic_origin"] == "absent; source and target spectra are arbitrary ordered real data", "arithmetic lock", checks)
    need(source_lock["clock"] == "autonomous continuous flow time t", "clock lock", checks)
    need(source_lock["normalization"] == "F(H)=Tr(HN) with the Frobenius norm identity dF/dt=||[H,N]||_F^2", "normalization lock", checks)
    need(source_lock["determinant_convention"] == "none; no dynamical zeta or Fredholm determinant is promoted", "determinant lock", checks)
    need(source_lock["cutoff"] == "all-n proof; exact permutation and pair-mode regression for 2<=n<=7", "cutoff lock", checks)
    need(source_lock["precision"] == "exact integer and rational matrix arithmetic with symbolic identities", "precision lock", checks)
    need("Euler factors" in source_lock["forbidden_data"] and "Route-B inputs" in source_lock["forbidden_data"], "forbidden lock", checks)

    theorem_expected = {
        "global_existence": "the compact orthogonal orbit is invariant, so the polynomial vector field has a global solution for every initial H",
        "isospectrality": "dH/dt=[H,K(H)] with K(H)=[H,N] skew-symmetric, hence H(t)=Q(t)H(0)Q(t)^T",
        "lyapunov_identity": "d Tr(HN)/dt=||[H,N]||_F^2, with equality zero exactly at equilibrium",
        "equilibria": "for simple source spectrum and strict diagonal N there are exactly n! diagonal permutation equilibria",
        "pair_linearization": "at D_pi, off-diagonal mode (i,j) has rate (lambda_pi(i)-lambda_pi(j))*(nu_j-nu_i)",
        "morse_index": "the Morse index of -Tr(HN) at D_pi equals inv(pi); stable and unstable dimensions for the ascent flow are C(n,2)-inv(pi) and inv(pi)",
        "generic_sorting": "every trajectory converges to one permutation equilibrium; outside the stable manifolds of the other equilibria it converges to the uniquely sorted diagonal",
        "no_recurrence": "strict Lyapunov monotonicity excludes every nonconstant recurrent or periodic orbit",
        "boundary": "repeated source spectra collapse permutation labels and can zero only ambient stabilizer pair rates, whereas repeated target spectra create genuine tangent zero modes and Morse--Bott equilibrium families; both lie outside the main theorem",
    }
    need(payload["theorem"] == theorem_expected, "theorem registry", checks)
    need(payload["regression_cutoff"] == {"n_min": 2, "n_max": 7, "source_spectrum": "1..n", "target_diagonal": "1^2..n^2"}, "cutoff metadata", checks)

    route_expected = {
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
    }
    need(payload["route_a_verdict"] == route_expected, "Route-A tuple", checks)
    scope_expected = {
        "claimed_automorphy", "claimed_euler_factor", "claimed_hilbert_polya",
        "claimed_root_number", "claimed_target_divisor_match",
        "claimed_target_functional_equation", "claimed_weil_compression",
        "route_b_invocation_allowed", "used_arithmetic_local_data",
        "used_target_prime_table", "used_target_zero_table",
    }
    exact_keys(payload["scope_flags"], scope_expected, "scope flags", checks)
    for key, value in payload["scope_flags"].items():
        need(value is False, f"scope flag {key}", checks)
    need(len(payload["arithmetic_controls"]) == 4, "arithmetic control count", checks)
    need(len(payload["nonclaims"]) == 6, "nonclaim count", checks)
    need(payload["nonclaims"][1] == "a full Bruhat or Schubert cell closure theorem", "Bruhat nonclaim", checks)
    need(payload["nonclaims"][2] == "a complete classification of the repeated-spectrum boundary or its target-degenerate Morse--Bott component", "boundary nonclaim", checks)

    source = payload["source_registry"]
    need(len(source) == 1, "source population", checks)
    need(source[0] == {
        "key": "brockett_1991_sorting",
        "authors": "R. W. Brockett",
        "title": "Dynamical systems that sort lists, diagonalize matrices, and solve linear programming problems",
        "journal": "Linear Algebra and its Applications",
        "volume": 146,
        "pages": "79--91",
        "year": 1991,
        "doi": "10.1016/0024-3795(91)90021-N",
        "role": "classical ownership of the double-bracket gradient sorting and diagonalization framework",
    }, "source registry", checks)
    need(payload["attribution_boundary"] == {
        "classical": "the double-bracket flow, its gradient interpretation, sorting role, and diagonalization application belong to Brockett",
        "package_synthesis": "the all-n proof ledger, finite exact regression, repeated-spectrum sentinel, and strict Route-A stop are an artifact-level synthesis; no mathematical priority is claimed",
    }, "attribution boundary", checks)

    rows = payload["permutation_rows"]
    expected_total = sum(factorial(n) for n in range(2, 8))
    need(len(rows) == expected_total == 5912, "permutation population", checks)
    cursor = 0
    expected_modes_total = 0
    summaries_by_n = {row["n"]: row for row in payload["size_summaries"]}
    need(set(summaries_by_n) == set(range(2, 8)), "summary sizes", checks)
    for n in range(2, 8):
        lam = list(range(1, n + 1))
        nu = [i * i for i in range(1, n + 1)]
        local_heights: list[int] = []
        inversion_hist = [0] * (n * (n - 1) // 2 + 1)
        for perm in permutations(lam):
            row = rows[cursor]
            cursor += 1
            inv = invs(perm)
            modes: list[list[int | str]] = []
            for i in range(n):
                for j in range(i + 1, n):
                    rate = (perm[i] - perm[j]) * (nu[j] - nu[i])
                    modes.append([i + 1, j + 1, rate, "unstable" if rate > 0 else "stable"])
            height = sum(perm[i] * nu[i] for i in range(n))
            digest = sha256(("\n".join(f"{i},{j},{rate},{sign}" for i, j, rate, sign in modes) + "\n").encode()).hexdigest()
            expected_header = {
                "n": n,
                "permutation": list(perm),
                "height_Tr_DN": height,
                "sorting_energy_minus_Tr_DN": -height,
                "inversions": inv,
                "morse_index_of_minus_height": inv,
                "stable_modes": len(modes) - inv,
                "unstable_modes": inv,
                "zero_modes": 0,
                "pair_mode_digest": digest,
            }
            for key, value in expected_header.items():
                need(row.get(key) == value, f"permutation n={n} p={perm} {key}", checks)
            need(len(row["pair_modes"]) == len(modes), f"mode length n={n} p={perm}", checks)
            for actual, expected in zip(row["pair_modes"], modes):
                need(actual == expected, f"mode n={n} p={perm} expected={expected}", checks)
            expected_modes_total += len(modes)
            local_heights.append(height)
            inversion_hist[inv] += 1
        summary = summaries_by_n[n]
        expected_summary = {
            "n": n,
            "source_spectrum": lam,
            "target_diagonal": nu,
            "permutation_count": factorial(n),
            "pair_mode_count": factorial(n) * n * (n - 1) // 2,
            "unique_height_maximizer": [lam],
            "unique_height_minimizer": [list(reversed(lam))],
            "height_max": max(local_heights),
            "height_min": min(local_heights),
            "inversion_generating_coefficients": inversion_hist,
        }
        need(summary == expected_summary, f"summary n={n}", checks)
    need(expected_modes_total == 118004, "mode population arithmetic", checks)

    regressions = payload["matrix_regressions"]
    need(len(regressions) == 6, "matrix regression count", checks)
    for n, row in zip(range(2, 8), regressions):
        lam = list(range(1, n + 1))
        nu = [i * i for i in range(1, n + 1)]
        q = orthogonal_sample(n)
        need(product(trans(q), q) == ident(n), f"orthogonality n={n}", checks)
        h = product(product(q, diag(lam)), trans(q))
        target = diag(nu)
        generator = bracket(h, target)
        velocity = bracket(h, generator)
        derivative = tr(product(velocity, target))
        squared_norm = norm2(generator)
        power = ident(n)
        traces: list[str] = []
        for k in range(1, n + 1):
            power = product(power, h)
            value = tr(power)
            need(value == sum(Fraction(x**k) for x in lam), f"trace invariant n={n} k={k}", checks)
            traces.append(f"{value.numerator}/{value.denominator}")
        expected_row = {
            "n": n,
            "source_spectrum": lam,
            "target_diagonal": nu,
            "givens_cosine": "3/5",
            "givens_sine": "4/5",
            "H_sha256": digest_matrix(h),
            "generator_sha256": digest_matrix(generator),
            "velocity_sha256": digest_matrix(velocity),
            "d_Tr_HN_dt": f"{derivative.numerator}/{derivative.denominator}",
            "commutator_frobenius_norm_sq": f"{squared_norm.numerator}/{squared_norm.denominator}",
            "trace_powers_1_through_n": traces,
            "H_symmetric": True,
            "generator_skew_symmetric": True,
            "velocity_symmetric": True,
            "strict_off_equilibrium": True,
        }
        need(row == expected_row, f"matrix row n={n}", checks)
        need(derivative == squared_norm and derivative > 0, f"Lyapunov n={n}", checks)
        need(trans(generator) == [[-x for x in r] for r in generator], f"skew n={n}", checks)
        need(trans(velocity) == velocity, f"velocity symmetric n={n}", checks)

    boundary = payload["boundary_controls"]
    need(boundary["status"] == "REPEATED_SPECTRUM_BOUNDARY_WITH_TARGET_MORSE_BOTT_SENTINEL", "boundary status", checks)
    need(boundary["nonclaim"] == "no full classification or Bruhat/Schubert closure theorem is asserted at repeated spectra", "boundary nonclaim", checks)
    source_boundary = boundary["repeated_source_spectrum"]
    need(source_boundary == {
        "lambda": [1, 1, 3], "nu": [1, 4, 9], "distinct_diagonal_equilibria": 3,
        "naive_factorial_count": 6, "representative_pair_rates": [0, -16, -10],
        "zero_ambient_pair_rates": 1,
        "zero_rate_interpretation": "stabilizer/non-tangent direction on the lower-dimensional repeated-source orbit",
    }, "repeated source sentinel", checks)
    target_boundary = boundary["repeated_target_spectrum"]
    rotation = [[Fraction(3, 5), Fraction(-4, 5), Fraction(0)], [Fraction(4, 5), Fraction(3, 5), Fraction(0)], [Fraction(0), Fraction(0), Fraction(1)]]
    rotated = product(product(rotation, diag([1, 2, 3])), trans(rotation))
    need(bracket(rotated, diag([1, 1, 4])) == [[Fraction(0) for _ in range(3)] for _ in range(3)], "target boundary commutator", checks)
    need(rotated[0][1] != 0, "target boundary non-diagonal", checks)
    need(target_boundary["lambda"] == [1, 2, 3] and target_boundary["nu"] == [1, 1, 4], "target boundary data", checks)
    need(target_boundary["rational_rotation"] == [[f"{x.numerator}/{x.denominator}" for x in row] for row in rotation], "target rotation", checks)
    need(target_boundary["non_diagonal_equilibrium_H"] == [[f"{x.numerator}/{x.denominator}" for x in row] for row in rotated], "target H", checks)
    need(target_boundary["commutator_is_zero"] is True, "target zero commutator flag", checks)
    need(target_boundary["representative_pair_rates"] == [0, -6, -3], "target rates", checks)
    need(target_boundary["zero_pair_modes"] == 1, "target zero modes", checks)
    need(target_boundary["continuous_equilibrium_family"] == "orthogonal rotations inside the repeated-N eigenspace", "target family", checks)

    counts = payload["counts"]
    need(counts == {
        "sizes": 6,
        "permutation_rows": 5912,
        "pair_mode_rows": 118004,
        "matrix_regression_rows": 6,
        "source_registry_population": 1,
        "reference_registry_population": 1,
        "all_n_theorem": True,
    }, "counts", checks)
    integrity = payload["integrity"]
    need(integrity == {
        "finite_regressions_are_proof": False,
        "all_n_argument_location": ["THEOREM_PACKAGE.md", "paper/main.tex"],
        "external_reviewer_simulated": False,
        "acceptance_score_reported": False,
        "citation_population": 1,
    }, "integrity", checks)
    return checks[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    payload = json.loads(args.evidence.read_text())
    assertions = validate(payload)
    print(json.dumps({"status": "C185_CHECKER_PASS", "assertions": assertions, "payload_sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
