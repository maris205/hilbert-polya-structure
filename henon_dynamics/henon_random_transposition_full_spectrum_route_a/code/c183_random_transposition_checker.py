#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C183."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import factorial
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c183_random_transposition_evidence.json"
EXPECTED_COMMIT = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
EXPECTED_EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXPECTED_N_MIN, EXPECTED_N_MAX, EXPECTED_MOMENT_MAX = 2, 11, 8
EXPECTED_SOURCE_LOCK = {
    "object": "lazy random-transposition Markov chain on the symmetric group S_n",
    "family": "every integer n>=2",
    "clock": "one independent ordered-pair draw (i,j), followed by the transposition (i j), with (i i)=identity",
    "measure": "uniform probability on S_n",
    "operator": "central convolution P_n=(1/n^2) sum_(i,j) R_(i j) on L2(S_n)",
    "determinant_convention": "finite Markov determinant det(I-z P_n); on frozen S_n it is not an unweighted Artin--Mazur orbit determinant",
    "cutoff": "all-n proof; exact regression uses 2<=n<=11 and moments 0<=k<=8",
    "allowed_data": "partitions, hook lengths, exact characters at a transposition, and source-derived walk counts",
    "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
}
EXPECTED_BOUNDARY = {
    "reversibility": "P_n is self-adjoint for uniform measure because the central step law is inversion-invariant",
    "l2_identity": "for a walk started at identity, squared L2 density distance equals sum_(lambda!=(n)) d_lambda^2 beta_lambda^(2k)",
    "classical_cutoff_boundary": "the total-variation cutoff at one-half n log n is attributed to Diaconis--Shahshahani and is not claimed as a new theorem here",
    "frozen_phase_space_boundary": "on frozen S_n, P_n is not induced by a single-valued deterministic map and is not a permutation Koopman operator",
    "frozen_determinant_boundary": "det(I-z P_n) is not the unweighted Artin--Mazur orbit determinant of a deterministic map on frozen S_n",
    "weighted_path_cycle_product": "after changing to the weighted directed-edge path space of P_n, det(I-z P_n)^(-1)=product_[primitive path cycles gamma](1-w(gamma) z^|gamma|)^(-1) as a formal power series",
    "owner_change_boundary": "the weighted path-space product is canonical for P_n but changes the phase space and dynamical object; it is not the frozen S_n owner",
    "a1_failure_boundary": "A1 remains FAIL because the frozen source has no primitive orbit carrying an A0 arithmetic payload; the failure is not an absolute denial of primitive factorizations after a lift",
}
EXPECTED_ROUTE_A = {
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
    "overall": "ROUTE_A_REJECTED",
    "A0_qualification": "DECK_SIZE_AND_GROUP_REPRESENTATION_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
    "A1_qualification": "FROZEN_S_N_HAS_NO_PRIMITIVE_ORBIT_CARRYING_AN_A0_ARITHMETIC_PAYLOAD_AND_WEIGHTED_PATH_LIFT_CHANGES_THE_OBJECT",
    "A2_qualification": "FINITE_MARKOV_DETERMINANT_HAS_NO_TARGET_DIVISOR_MATCH",
    "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_WEIL_COMPRESSION",
    "A4_qualification": "SELF_ADJOINT_MARKOV_CONTRACTION_AND_ABSTRACT_UNITARY_DILATION_ONLY",
    "route_b_invocation_allowed": False,
}
EXPECTED_SCOPE_FLAGS = {
    "used_target_zero_table": False,
    "used_target_prime_table": False,
    "used_arithmetic_local_data": False,
    "claimed_target_divisor_match": False,
    "claimed_target_functional_equation": False,
    "claimed_hilbert_polya": False,
    "route_b_invocation_allowed": False,
}
EXPECTED_SOURCE_REGISTRY = [{
    "key": "diaconis_shahshahani_1981_random_transpositions",
    "title": "Generating a random permutation with random transpositions",
    "authors": "Persi Diaconis and Mehrdad Shahshahani",
    "year": 1981,
    "doi": "10.1007/BF00535487",
    "role": "classical spectrum/mixing ownership and cutoff attribution",
}]
EXPECTED_NONCLAIMS = [
    "novelty or priority for the random-transposition spectrum or cutoff",
    "identification of weighted path cycles with intrinsic deterministic orbits on frozen S_n",
    "absolute nonexistence of primitive-cycle factorizations after changing phase space",
    "prime semantics for the deck size n or partition labels",
    "a target divisor, functional equation, counting law, or continuation match",
    "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
]


def parts(total: int, cap: int | None = None):
    if total == 0:
        yield ()
    else:
        for x in range(min(total, cap or total), 0, -1):
            for rest in parts(total - x, x):
                yield (x,) + rest


def transpose(shape: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(x >= j for x in shape) for j in range(1, shape[0] + 1))


def degree(shape: tuple[int, ...]) -> int:
    hooks = []
    for i, width in enumerate(shape):
        for j in range(width):
            hooks.append(width - j + sum(row > j for row in shape[i + 1 :]))
    answer = factorial(sum(shape))
    for h in hooks:
        assert answer % h == 0
        answer //= h
    return answer


def kappa(shape: tuple[int, ...]) -> int:
    return 2 * sum(j - i for i, width in enumerate(shape) for j in range(width))


def frac(item: dict) -> Fraction:
    return Fraction(item["numerator"], item["denominator"])


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def swap(p: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    q = list(p)
    q[i], q[j] = q[j], q[i]
    return tuple(q)


def direct_return_words(n: int, max_step: int) -> list[int]:
    identity = tuple(range(n))
    counts = {identity: 1}
    returns = [1]
    for _ in range(max_step):
        nxt: dict[tuple[int, ...], int] = defaultdict(int)
        for permutation, count in counts.items():
            for i, j in product(range(n), repeat=2):
                nxt[swap(permutation, i, j)] += count
        counts = nxt
        returns.append(counts.get(identity, 0))
    return returns


def primitive_binary_cycles(max_length: int) -> dict[int, int]:
    """Count primitive cyclic words for the two-state weighted path lift."""
    counts = {}
    for length in range(1, max_length + 1):
        representatives = set()
        for word in product(range(2), repeat=length):
            rotations = [word[offset:] + word[:offset] for offset in range(length)]
            if word != min(rotations):
                continue
            if any(
                length % period == 0
                and word == word[:period] * (length // period)
                for period in range(1, length)
            ):
                continue
            representatives.add(word)
        counts[length] = len(representatives)
    return counts


def weighted_binary_euler_coefficients(max_degree: int) -> tuple[dict[int, int], list[Fraction]]:
    """Expand the primitive-cycle product for P_2 through max_degree."""
    cycle_counts = primitive_binary_cycles(max_degree)
    coefficients = [Fraction(0) for _ in range(max_degree + 1)]
    coefficients[0] = Fraction(1)
    for length, population in cycle_counts.items():
        weight = Fraction(1, 2) ** length
        for _ in range(population):
            updated = [Fraction(0) for _ in range(max_degree + 1)]
            for degree, coefficient in enumerate(coefficients):
                for repetitions in range((max_degree - degree) // length + 1):
                    updated[degree + repetitions * length] += coefficient * weight**repetitions
            coefficients = updated
    return cycle_counts, coefficients


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    checks = 0

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    check(data["schema"] == "HCS-C183-v1", "schema")
    check(data["candidate_id"] == "HCS-C183", "candidate")
    check(data["date_utc"] == "2026-08-26", "date")
    check(data["source_commit"] == EXPECTED_COMMIT, "commit")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["evaluator"] == {
        "path": "flow_systems/skills/route-a-evaluator.md",
        "version": "0.2.0",
        "sha256": EXPECTED_EVALUATOR,
    }, "evaluator lock")
    check(data["source_lock"] == EXPECTED_SOURCE_LOCK, "source lock")
    check(data["mixing_and_operator_boundary"] == EXPECTED_BOUNDARY, "operator-owner boundary")
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")
    check(data["route_a"] == EXPECTED_ROUTE_A, "Route-A exact ledger")
    check(data["scope_flags"] == EXPECTED_SCOPE_FLAGS, "scope flags exact")
    check(data["source_registry"] == EXPECTED_SOURCE_REGISTRY, "source registry exact")
    check(data["nonclaims"] == EXPECTED_NONCLAIMS, "nonclaims exact")

    replay = data["finite_replay"]
    check(replay["n_min"] == EXPECTED_N_MIN, "n_min metadata")
    check(replay["n_max"] == EXPECTED_N_MAX, "n_max metadata")
    check(replay["moment_max"] == EXPECTED_MOMENT_MAX, "moment_max metadata")
    rows = replay["partition_rows"]
    moments = replay["moment_rows"]
    factors = replay["factor_rows"]
    summaries = replay["summaries"]
    check(replay["partition_row_count"] == 193 == len(rows), "partition count")
    check(replay["moment_row_count"] == 90 == len(moments), "moment count")
    check(replay["factor_row_count"] == 163 == len(factors), "factor count")
    check(len(summaries) == 10, "summary count")

    expected_rows = {}
    spectra: dict[int, list[tuple[tuple[int, ...], int, Fraction]]] = {}
    for n in range(2, 12):
        spectra[n] = []
        for shape in parts(n):
            dim = degree(shape)
            kap = kappa(shape)
            ratio = Fraction(kap, n * (n - 1))
            beta = Fraction(1, n) + Fraction(n - 1, n) * ratio
            expected_rows[(n, shape)] = (dim, kap, ratio, beta)
            spectra[n].append((shape, dim, beta))

    check(len(rows) == len(expected_rows), "complete partition population")
    seen = set()
    for row in rows:
        n, shape = row["n"], tuple(row["partition"])
        check((n, shape) in expected_rows, "unexpected partition")
        check((n, shape) not in seen, "duplicate partition")
        seen.add((n, shape))
        dim, kap, ratio, beta = expected_rows[(n, shape)]
        check(tuple(row["conjugate_partition"]) == transpose(shape), "conjugate")
        check(row["hook_dimension"] == dim, "hook dimension")
        check(row["content_numerator"] == kap, "content numerator")
        check(frac(row["transposition_character_ratio"]) == ratio, "character ratio")
        check(frac(row["lazy_eigenvalue"]) == beta, "eigenvalue")
        check(row["regular_multiplicity"] == dim * dim, "multiplicity")
        conjugate_beta = Fraction(2, n) - beta
        check(expected_rows[(n, transpose(shape))][3] == conjugate_beta, "sign twist")

    moment_map = {(row["n"], row["step"]): row for row in moments}
    check(len(moment_map) == 10 * 9, "moment population")
    for n, spectral in spectra.items():
        check(sum(dim * dim for _, dim, _ in spectral) == factorial(n), "regular dimension")
        for step in range(9):
            trace = sum(Fraction(dim * dim) * beta**step for _, dim, beta in spectral)
            probability = trace / factorial(n)
            count = probability * n ** (2 * step)
            l2 = sum(Fraction(dim * dim) * beta ** (2 * step) for shape, dim, beta in spectral if shape != (n,))
            row = moment_map[(n, step)]
            check(frac(row["operator_trace"]) == trace, "trace")
            check(frac(row["identity_return_probability"]) == probability, "return probability")
            check(row["ordered_pair_word_return_count"] == count, "return word count")
            check(frac(row["l2_density_distance_squared"]) == l2, "L2 identity")

    summary_map = {row["n"]: row for row in summaries}
    for n, spectral in spectra.items():
        nontrivial = [beta for shape, _, beta in spectral if shape != (n,)]
        row = summary_map[n]
        check(row["state_count"] == factorial(n), "state count")
        check(row["partition_count"] == len(spectral), "partition count summary")
        check(row["multiplicity_sum"] == factorial(n), "multiplicity summary")
        check(frac(row["largest_nontrivial_eigenvalue"]) == Fraction(n - 2, n), "second eigenvalue")
        check(frac(row["smallest_eigenvalue"]) == Fraction(2 - n, n), "bottom eigenvalue")
        check(frac(row["spectral_gap"]) == Fraction(2, n), "gap")
        check(row["ambient_dimension"] == factorial(n), "ambient dimension")
        check(row["nonzero_determinant_degree"] == sum(dim * dim for _, dim, beta in spectral if beta), "determinant degree")

    factor_map = defaultdict(dict)
    for row in factors:
        beta = frac(row["eigenvalue"])
        check(beta not in factor_map[row["n"]], "duplicate factor")
        factor_map[row["n"]][beta] = row["multiplicity"]
        check(
            row["determinant_factor"] == f"(1-({beta})*z)^{row['multiplicity']}",
            "determinant factor string",
        )
    for n, spectral in spectra.items():
        expected = defaultdict(int)
        for _, dim, beta in spectral:
            expected[beta] += dim * dim
        check(dict(factor_map[n]) == dict(expected), "collected factors")

    for n in range(2, 8):
        direct = direct_return_words(n, 6)
        for step, count in enumerate(direct):
            check(moment_map[(n, step)]["ordered_pair_word_return_count"] == count, "direct word enumeration")

    cycle_counts, euler_coefficients = weighted_binary_euler_coefficients(8)
    check(cycle_counts == {1: 2, 2: 1, 3: 2, 4: 3, 5: 6, 6: 9, 7: 18, 8: 30}, "P2 primitive path-cycle population")
    for exponent, coefficient in enumerate(euler_coefficients):
        check(coefficient == 1, f"P2 weighted path Euler coefficient z^{exponent}")
    print(json.dumps({"status": "C183_CHECKER_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
