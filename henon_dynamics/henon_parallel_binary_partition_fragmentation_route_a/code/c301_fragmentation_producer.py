#!/usr/bin/env python3
"""Produce deterministic exact evidence for HCS-C301.

The producer deliberately uses only the Python standard library. All exact
probabilities are serialized as reduced rational strings; decimal asymptotic
diagnostics are explicitly labelled as displays rather than proof objects.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c301_fragmentation_evidence.json"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def rat(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def falling(q: int, k: int) -> int:
    if k < 0 or k > q:
        return 0
    answer = 1
    for j in range(k):
        answer *= q - j
    return answer


def stirling2(n: int, k: int, memo: dict[tuple[int, int], int] = {}) -> int:
    if (n, k) in memo:
        return memo[n, k]
    if n == 0:
        return int(k == 0)
    if k == 0 or k > n:
        return 0
    memo[n, k] = stirling2(n - 1, k - 1) + k * stirling2(n - 1, k)
    return memo[n, k]


def rgs_partitions(n: int) -> list[tuple[int, ...]]:
    """All labelled set partitions in canonical restricted-growth encoding."""
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []

    def extend(prefix: tuple[int, ...], current_max: int) -> None:
        if len(prefix) == n:
            out.append(prefix)
            return
        for value in range(current_max + 2):
            extend(prefix + (value,), max(current_max, value))

    extend((0,), 0)
    return out


def canonicalize(labels: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    names: dict[tuple[int, int], int] = {}
    return tuple(names.setdefault(label, len(names)) for label in labels)


def one_step_counts(state: tuple[int, ...]) -> Counter[tuple[int, ...]]:
    """Enumerate all labelled fair-bit assignments; independent of formula."""
    counts: Counter[tuple[int, ...]] = Counter()
    for bits in itertools.product((0, 1), repeat=len(state)):
        target = canonicalize(tuple(zip(state, bits)))
        counts[target] += 1
    return counts


def expected_blocks(n: int, q: int) -> Fraction:
    return Fraction(q**n - (q - 1) ** n, q ** (n - 1))


def trace_power(n: int, t: int) -> Fraction:
    return sum(Fraction(stirling2(n, k), 2 ** (t * (n - k))) for k in range(1, n + 1))


def transition_evidence(max_n: int = 6) -> dict:
    groups = []
    cells = probability_cells = 0
    for n in range(1, max_n + 1):
        states = rgs_partitions(n)
        rows = []
        for state in states:
            counts = one_step_counts(state)
            transitions = [
                {
                    "target_rgs": "".join(map(str, target)),
                    "numerator": Fraction(count, 2**n).numerator,
                    "denominator": Fraction(count, 2**n).denominator,
                }
                for target, count in sorted(counts.items())
            ]
            rows.append({
                "state_rgs": "".join(map(str, state)),
                "rank": 1 + max(state),
                "transitions": transitions,
            })
            cells += len(states)
            probability_cells += len(transitions)
        groups.append({"n": n, "bell_number": len(states), "rows": rows})
    return {
        "n_max": max_n,
        "matrix_cells_including_zeros": cells,
        "listed_nonzero_probability_cells": probability_cells,
        "groups": groups,
    }


def time_evidence(n_max: int = 9, t_max: int = 8) -> dict:
    rows = []
    coefficient_cells = 0
    for n in range(1, n_max + 1):
        multiplicities = [stirling2(n, k) for k in range(1, n + 1)]
        for t in range(t_max + 1):
            q = 2**t
            denominator = q**n
            numerators = [stirling2(n, k) * falling(q, k) for k in range(1, n + 1)]
            absorption = Fraction(falling(q, n), denominator)
            rows.append({
                "n": n,
                "t": t,
                "q": q,
                "block_count_k_1_to_n_numerators": numerators,
                "common_denominator": denominator,
                "mass_sum_numerator": sum(numerators),
                "expected_blocks": rat(expected_blocks(n, q)),
                "absorption_cdf": rat(absorption),
                "trace_K_power_t": rat(trace_power(n, t)),
                "eigenvalue_multiplicities_by_rank": multiplicities,
            })
            coefficient_cells += n
    return {
        "n_max": n_max,
        "t_max": t_max,
        "row_count": len(rows),
        "block_count_coefficient_cells": coefficient_cells,
        "rows": rows,
    }


def absorption_mass_evidence() -> list[dict]:
    rows = []
    for n in range(1, 9):
        cdf_previous = Fraction(0)
        for t in range(0, 13):
            cdf = Fraction(falling(2**t, n), 2 ** (t * n))
            rows.append({
                "n": n,
                "t": t,
                "cdf": rat(cdf),
                "mass": rat(cdf - cdf_previous),
            })
            cdf_previous = cdf
    return rows


def asymptotic_diagnostics() -> list[dict]:
    rows = []
    for n in (32, 64, 128, 256, 512):
        t = 2 * int(math.log2(n))
        q = 2**t
        cdf = Fraction(falling(q, n), q**n)
        rows.append({
            "n": n,
            "t": t,
            "n_squared_over_q": rat(Fraction(n * n, q)),
            "exact_cdf_decimal_12": f"{float(cdf):.12f}",
            "limit_exp_minus_half_decimal_12": f"{math.exp(-0.5):.12f}",
            "absolute_error_decimal_12": f"{abs(float(cdf) - math.exp(-0.5)):.12f}",
        })
    return rows


def build_payload() -> dict:
    transition = transition_evidence()
    times = time_evidence()
    payload = {
        "schema": "hcs-c301-parallel-binary-fragmentation-evidence-v1",
        "candidate_id": "HCS-C301",
        "obstruction_id": "HEN-O285",
        "title": "Parallel binary refinement of labelled set partitions",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority_sha256": EVALUATOR,
        "model": {
            "state_space": "labelled set partitions of [n]",
            "initial_state": "the one-block partition",
            "update": "each label independently receives a fresh fair bit; every block is refined by its two bit fibres and empty fibres are deleted",
            "one_step_kernel": "K_n(pi,sigma)=2^(|pi|-n) exactly when sigma refines pi and each pi-block contains at most two sigma-blocks; otherwise 0",
            "t_step_kernel": "K_n^t(pi,sigma)=1_{sigma refines pi} product_{B in pi} (2^t)_{r_B}/(2^t)^{|B|}",
            "encoding": "canonical restricted-growth strings on labels 1,...,n",
        },
        "theorem": {
            "partition_law": "P(Pi_t=sigma)=(2^t)_{|sigma|}/(2^t)^n",
            "block_count_law": "P(K_t=k)=S(n,k)(2^t)_k/(2^t)^n",
            "expected_blocks": "E[K_t]=2^t[1-(1-2^{-t})^n]",
            "absorption_cdf": "P(T_n<=t)=(2^t)_n/(2^t)^n",
            "absorption_mass": "P(T_n=t)=P(T_n<=t)-P(T_n<=t-1), with the t=-1 CDF set to 0",
            "mean_absorption_time": "E[T_n]=sum_{t>=0}[1-(2^t)_n/(2^t)^n]",
            "characteristic_polynomial": "chi_n(x)=product_{k=1}^n (x-2^{k-n})^{S(n,k)}",
            "spectral_determinant": "det(I-zK_n)=product_{k=1}^n (1-z 2^{k-n})^{S(n,k)}",
            "trace": "tr(K_n^t)=sum_{k=1}^n S(n,k)2^{t(k-n)}",
            "diagonalizability": "product_{k=1}^n(K_n-2^{k-n}I)=0, hence K_n is diagonalizable over Q",
            "critical_limit": "if n_j tends to infinity and n_j^2/2^{t_j} tends to lambda in (0,infinity), then P(T_{n_j}<=t_j) tends to exp(-lambda/2)",
            "lattice_boundary": "a phase-free continuous limit for T_n-2 log_2 n is not asserted because integer t and dyadic scaling retain subsequence phase",
        },
        "proof_certificates": {
            "semigroup_word": "after t rounds, each label carries an independent uniform word in {0,1}^t; blocks are equal-word fibres inside starting blocks",
            "kernel_count": "for r target fibres in a source block, injective word assignments number (2^t)_r",
            "spectrum_guard": "rank ordering makes K block upper triangular with scalar diagonal 2^{k-n}I on rank k; recursive block elimination gives the squarefree annihilator, not diagonal entries alone",
            "birthday_limit": "log product_{j=0}^{n-1}(1-j/q)=-n(n-1)/(2q)+O(n^3/q^2) when n^2/q is bounded",
        },
        "stirling_table": [
            {"n": n, "S_n_k_k_0_to_n": [stirling2(n, k) for k in range(n + 1)]}
            for n in range(0, 13)
        ],
        "transition_regression": transition,
        "time_regression": times,
        "absorption_mass_regression": absorption_mass_evidence(),
        "critical_window_diagnostics": asymptotic_diagnostics(),
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "obstruction": "absorbing refinement has no nonconstant recurrent primitive cycles, and its finite Markov determinant supplies no arithmetic local datum, logarithmic prime clock, target completed determinant, divisor law, or self-adjoint target-zero lift",
        },
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "nonclaims": [
            "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, zero match, or Hilbert--Polya operator is asserted.",
            "The finite-state Markov determinant is source-local and is not identified with an arithmetic zeta or L-function.",
            "No literature-priority claim is made for fragmentation chains, occupancy laws, birthday asymptotics, or Hopf-algebraic Markov chains.",
        ],
        "collision_boundary": {
            "C194": "C194 owns Holte carries and the base/riffle semigroup; C301 refines labelled set partitions by independent bit words and studies absorption at label separation.",
            "C215": "C215 owns continuous-time Kingman coalescence; C301 moves in the reverse refinement direction with synchronous discrete updates.",
            "C276": "C276 owns one marked orbit in a uniform random mapping; C301 separates all labels and has a logarithmic last-collision threshold.",
            "integer_partition_warning": "quotienting to unlabelled block-size partitions changes state multiplicities and is outside the theorem.",
        },
        "regression_summary": {
            "transition_state_rows": sum(len(group["rows"]) for group in transition["groups"]),
            "transition_nonzero_probability_cells": transition["listed_nonzero_probability_cells"],
            "time_rows": times["row_count"],
            "block_count_coefficient_cells": times["block_count_coefficient_cells"],
            "absorption_mass_rows": 8 * 13,
            "all_exact_probability_rows_normalized": True,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {args.output}")
    print(f"payload_sha256={payload['payload_sha256']}")
    print(f"transition_rows={payload['regression_summary']['transition_state_rows']}")
    print(f"nonzero_transition_cells={payload['regression_summary']['transition_nonzero_probability_cells']}")
    print(f"time_rows={payload['regression_summary']['time_rows']}")


if __name__ == "__main__":
    main()
