#!/usr/bin/env python3
"""Produce the exact HCS-C183 random-transposition spectral certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from math import factorial
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c183_random_transposition_evidence.json"
SOURCE_COMMIT = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
N_MIN, N_MAX, MOMENT_MAX = 2, 11, 8


def partitions(n: int, ceiling: int | None = None):
    """Yield integer partitions in reverse lexicographic order."""
    if n == 0:
        yield ()
        return
    top = min(n, ceiling if ceiling is not None else n)
    for first in range(top, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def conjugate(shape: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row >= column for row in shape) for column in range(1, shape[0] + 1))


def hook_dimension(shape: tuple[int, ...]) -> int:
    n = sum(shape)
    hooks = 1
    for row, width in enumerate(shape):
        for column in range(width):
            below = sum(later > column for later in shape[row + 1 :])
            hooks *= (width - column) + below
    return factorial(n) // hooks


def content_numerator(shape: tuple[int, ...]) -> int:
    """n(n-1) times the character ratio at a transposition."""
    return sum(part * part - (2 * index - 1) * part for index, part in enumerate(shape, 1))


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    partition_rows = []
    moment_rows = []
    factor_rows = []
    summaries = []
    for n in range(N_MIN, N_MAX + 1):
        spectral = []
        for shape in partitions(n):
            dim = hook_dimension(shape)
            content = content_numerator(shape)
            ratio = Fraction(content, n * (n - 1))
            beta = Fraction(1, n) + Fraction(n - 1, n) * ratio
            multiplicity = dim * dim
            spectral.append((shape, dim, content, ratio, beta, multiplicity))
            partition_rows.append({
                "n": n,
                "partition": list(shape),
                "conjugate_partition": list(conjugate(shape)),
                "hook_dimension": dim,
                "content_numerator": content,
                "transposition_character_ratio": fraction_record(ratio),
                "lazy_eigenvalue": fraction_record(beta),
                "regular_multiplicity": multiplicity,
            })

        multiplicity_sum = sum(row[5] for row in spectral)
        assert multiplicity_sum == factorial(n)
        collected: dict[Fraction, int] = {}
        for *_, beta, multiplicity in spectral:
            collected[beta] = collected.get(beta, 0) + multiplicity
        for beta in sorted(collected):
            factor_rows.append({
                "n": n,
                "eigenvalue": fraction_record(beta),
                "multiplicity": collected[beta],
                "determinant_factor": f"(1-({beta})*z)^{collected[beta]}",
            })

        for step in range(MOMENT_MAX + 1):
            trace = sum(Fraction(mult) * beta**step for *_, beta, mult in spectral)
            return_probability = trace / factorial(n)
            word_count = return_probability * n ** (2 * step)
            assert word_count.denominator == 1
            l2_squared = sum(
                Fraction(mult) * beta ** (2 * step)
                for shape, _, _, _, beta, mult in spectral
                if shape != (n,)
            )
            moment_rows.append({
                "n": n,
                "step": step,
                "operator_trace": fraction_record(trace),
                "identity_return_probability": fraction_record(return_probability),
                "ordered_pair_word_return_count": word_count.numerator,
                "l2_density_distance_squared": fraction_record(l2_squared),
            })

        nontrivial = [beta for shape, _, _, _, beta, _ in spectral if shape != (n,)]
        summaries.append({
            "n": n,
            "state_count": factorial(n),
            "partition_count": len(spectral),
            "multiplicity_sum": multiplicity_sum,
            "distinct_eigenvalue_count": len(collected),
            "largest_nontrivial_eigenvalue": fraction_record(max(nontrivial)),
            "smallest_eigenvalue": fraction_record(min(beta for *_, beta, _ in spectral)),
            "spectral_gap": fraction_record(Fraction(2, n)),
            "ambient_dimension": sum(collected.values()),
            "nonzero_determinant_degree": sum(mult for beta, mult in collected.items() if beta),
        })

    data = {
        "schema": "HCS-C183-v1",
        "candidate_id": "HCS-C183",
        "date_utc": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        },
        "source_lock": {
            "object": "lazy random-transposition Markov chain on the symmetric group S_n",
            "family": "every integer n>=2",
            "clock": "one independent ordered-pair draw (i,j), followed by the transposition (i j), with (i i)=identity",
            "measure": "uniform probability on S_n",
            "operator": "central convolution P_n=(1/n^2) sum_(i,j) R_(i j) on L2(S_n)",
            "determinant_convention": "finite Markov determinant det(I-z P_n); on frozen S_n it is not an unweighted Artin--Mazur orbit determinant",
            "cutoff": "all-n proof; exact regression uses 2<=n<=11 and moments 0<=k<=8",
            "allowed_data": "partitions, hook lengths, exact characters at a transposition, and source-derived walk counts",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "spectral_theorem": {
            "irreducible_index": "partitions lambda of n",
            "dimension": "d_lambda=n!/product of hook lengths",
            "character_ratio": "chi_lambda(tau)/d_lambda=sum_i(lambda_i^2-(2i-1)lambda_i)/(n(n-1))",
            "eigenvalue": "beta_lambda=1/n+(n-1)/n*chi_lambda(tau)/d_lambda",
            "multiplicity": "d_lambda^2 in the regular representation",
            "determinant": "det(I-z P_n)=product_(lambda partition n)(1-z*beta_lambda)^(d_lambda^2)",
            "trace": "Tr(P_n^k)=sum_lambda d_lambda^2 beta_lambda^k=n!*Pr(X_k=e)",
            "gap": "largest nontrivial eigenvalue is 1-2/n and the spectral gap is 2/n",
            "bottom": "smallest eigenvalue is -1+2/n",
        },
        "mixing_and_operator_boundary": {
            "reversibility": "P_n is self-adjoint for uniform measure because the central step law is inversion-invariant",
            "l2_identity": "for a walk started at identity, squared L2 density distance equals sum_(lambda!=(n)) d_lambda^2 beta_lambda^(2k)",
            "classical_cutoff_boundary": "the total-variation cutoff at one-half n log n is attributed to Diaconis--Shahshahani and is not claimed as a new theorem here",
            "frozen_phase_space_boundary": "on frozen S_n, P_n is not induced by a single-valued deterministic map and is not a permutation Koopman operator",
            "frozen_determinant_boundary": "det(I-z P_n) is not the unweighted Artin--Mazur orbit determinant of a deterministic map on frozen S_n",
            "weighted_path_cycle_product": "after changing to the weighted directed-edge path space of P_n, det(I-z P_n)^(-1)=product_[primitive path cycles gamma](1-w(gamma) z^|gamma|)^(-1) as a formal power series",
            "owner_change_boundary": "the weighted path-space product is canonical for P_n but changes the phase space and dynamical object; it is not the frozen S_n owner",
            "a1_failure_boundary": "A1 remains FAIL because the frozen source has no primitive orbit carrying an A0 arithmetic payload; the failure is not an absolute denial of primitive factorizations after a lift",
        },
        "finite_replay": {
            "n_min": N_MIN,
            "n_max": N_MAX,
            "moment_max": MOMENT_MAX,
            "partition_rows": partition_rows,
            "moment_rows": moment_rows,
            "factor_rows": factor_rows,
            "summaries": summaries,
            "partition_row_count": len(partition_rows),
            "moment_row_count": len(moment_rows),
            "factor_row_count": len(factor_rows),
        },
        "progress_and_boundary": {
            "progress": "one all-size theorem joins the full partition-indexed spectrum, multiplicities, determinant, return traces, exact L2 distance, spectral gap, and the exact frozen-owner versus weighted-path-lift boundary",
            "prime_composite_control": "prime and composite deck sizes obey the same representation-theoretic formulas",
            "evidence_boundary": "finite rows regression-test exact formulas; all-size conclusions rest on written representation-theoretic proofs",
            "priority_boundary": "the spectrum and cutoff are classical; this package contributes a source-locked Route-A synthesis and obstruction certificate, not a priority claim",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "DECK_SIZE_AND_GROUP_REPRESENTATION_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
            "A1_qualification": "FROZEN_S_N_HAS_NO_PRIMITIVE_ORBIT_CARRYING_AN_A0_ARITHMETIC_PAYLOAD_AND_WEIGHTED_PATH_LIFT_CHANGES_THE_OBJECT",
            "A2_qualification": "FINITE_MARKOV_DETERMINANT_HAS_NO_TARGET_DIVISOR_MATCH",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_WEIL_COMPRESSION",
            "A4_qualification": "SELF_ADJOINT_MARKOV_CONTRACTION_AND_ABSTRACT_UNITARY_DILATION_ONLY",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_hilbert_polya": False,
            "route_b_invocation_allowed": False,
        },
        "source_registry": [{
            "key": "diaconis_shahshahani_1981_random_transpositions",
            "title": "Generating a random permutation with random transpositions",
            "authors": "Persi Diaconis and Mehrdad Shahshahani",
            "year": 1981,
            "doi": "10.1007/BF00535487",
            "role": "classical spectrum/mixing ownership and cutoff attribution",
        }],
        "nonclaims": [
            "novelty or priority for the random-transposition spectrum or cutoff",
            "identification of weighted path cycles with intrinsic deterministic orbits on frozen S_n",
            "absolute nonexistence of primitive-cycle factorizations after changing phase space",
            "prime semantics for the deck size n or partition labels",
            "a target divisor, functional equation, counting law, or continuation match",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
    }
    data["payload_sha256"] = sha256(canonical_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C183_PRODUCER_PASS",
        "partition_rows": data["finite_replay"]["partition_row_count"],
        "moment_rows": data["finite_replay"]["moment_row_count"],
        "factor_rows": data["finite_replay"]["factor_row_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
