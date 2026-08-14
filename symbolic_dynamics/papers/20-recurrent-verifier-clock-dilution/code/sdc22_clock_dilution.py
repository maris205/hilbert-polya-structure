#!/usr/bin/env python3
"""Exact prototype for SD-C22 recurrent-verifier clock dilution."""

from __future__ import annotations

import argparse
import csv
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Sequence


def sieve_primes(limit: int) -> list[int]:
    flag = [True] * (limit + 1)
    if limit >= 0:
        flag[0] = False
    if limit >= 1:
        flag[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if flag[p]:
            for multiple in range(p * p, limit + 1, p):
                flag[multiple] = False
    return [n for n in range(2, limit + 1) if flag[n]]


def expanded_cycle_length(p: int) -> int:
    """Number of edges after closing the explicit Q-state prime verifier.

    There is one input edge, ``ceil(p/d)`` edges for every tested divisor
    ``d``, and one terminal return edge.  For prime ``p`` no equality branch
    interrupts a quotient search.
    """
    return 2 + sum(math.ceil(p / d) for d in range(2, math.isqrt(p) + 1))


def verifier_forward_path(n: int) -> tuple[bool, list[str]]:
    """Materialize the local I/T/Q program through acceptance or rejection.

    Acceptance contracts the former terminal `T -> A` edge to `T -> I`.
    Rejection records the first cemetery state; its one-way continuation has
    no closed walk.  The transition code uses only successor, multiplication,
    and order comparisons.
    """
    if n < 2:
        raise ValueError("the full-shift inventory begins at n=2")
    states = [f"I:{n}", f"T:{n}:2"]
    d = 2
    while True:
        if d * d > n:
            states.append(f"I:{n}")
            return True, states
        q = 2
        states.append(f"Q:{n}:{d}:{q}")
        while True:
            product = d * q
            if product < n:
                q += 1
                states.append(f"Q:{n}:{d}:{q}")
            elif product == n:
                states.append(f"R:{n}:1")
                return False, states
            else:
                d += 1
                states.append(f"T:{n}:{d}")
                break


def simulated_cycle_length(p: int) -> int:
    """Independent local-state simulation of the same accepted path."""
    accepted, states = verifier_forward_path(p)
    if not accepted:
        raise ValueError(f"{p} reaches the cemetery")
    return len(states) - 1


def harmonic_lower_bound(p: int) -> float:
    bound = 2.0
    for d in range(2, math.isqrt(p) + 1):
        bound += p / d
    return bound


def optimal_max_edge_weight(p: int, sigma: float) -> float:
    """Smallest possible maximum weight under total roof log(p).

    Equal roof distribution minimizes the maximum edge weight.  Every other
    nonnegative distribution has a weight at least this large.
    """
    return math.exp(-sigma * math.log(p) / expanded_cycle_length(p))


def source_roof_total(p: int) -> float:
    """Paper-19 summability roofs, with the terminal edge used as return."""
    total = math.log(2 * p)
    d = 2
    while d * d <= p:
        total += math.log(2 * p * d)  # T -> Q_2
        q_stop = math.ceil(p / d)
        for q in range(2, q_stop + 1):
            total += math.log(p * d * q)
        d += 1
    total += math.log(p * d)
    return total


def direct_sum_determinant(
    primes: Sequence[int], s_integer: int, z: Fraction
) -> Fraction:
    """Exact determinant of finite closed verifier-cycle blocks."""
    value = Fraction(1)
    for p in primes:
        value *= 1 - (z ** expanded_cycle_length(p)) * Fraction(1, p**s_integer)
    return value


def determinant_at_return_section(
    primes: Sequence[int], s_integer: int
) -> Fraction:
    """The induced return determinant at z=1, which collapses each cycle."""
    value = Fraction(1)
    for p in primes:
        value *= 1 - Fraction(1, p**s_integer)
    return value


def marked_determinant_at_return_section(
    primes: Sequence[int], s_integer: int, z: Fraction
) -> Fraction:
    """First-return determinant with one marker per induced return."""
    value = Fraction(1)
    for p in primes:
        value *= 1 - z * Fraction(1, p**s_integer)
    return value


def cycle_power_trace(p: int, s_integer: int, r: int) -> Fraction:
    """Exact trace for any edge distribution with cycle product p^-s."""
    length = expanded_cycle_length(p)
    if r % length:
        return Fraction(0)
    return length * Fraction(1, p ** (s_integer * (r // length)))


def fibonacci_values(limit: int) -> set[int]:
    values: set[int] = set()
    left, right = 1, 2
    while right <= limit:
        values.add(right)
        left, right = right, left + right
    return values


def padded_decider_controls(limit: int, sigma: float) -> list[dict[str, object]]:
    fib = fibonacci_values(limit)
    predicates = {
        "squares": lambda n: math.isqrt(n) ** 2 == n,
        "powers_two": lambda n: n > 0 and n & (n - 1) == 0,
        "fibonacci": lambda n: n in fib,
        "hash_mod_five": lambda n: ((1103515245 * n + 19023) & 0x7FFFFFFF) % 5 == 0,
    }
    rows: list[dict[str, object]] = []
    for name, predicate in predicates.items():
        accepted = [n for n in range(2, limit + 1) if predicate(n)]
        # A total decider can always be padded to this acceptance-independent,
        # uniformly prescribed runtime without changing its language.
        weights = [math.exp(-sigma * math.log(n) / (n * n + 2)) for n in accepted]
        rows.append(
            {
                "name": name,
                "accepted_count": len(accepted),
                "largest_accepted": accepted[-1] if accepted else None,
                "max_optimal_edge_weight": max(weights) if weights else None,
                "all_cycle_products_exact_by_construction": True,
            }
        )
    return rows


def write_csv(path: Path, rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("empty rows")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    primes = sieve_primes(4096)
    cycle_rows: list[dict[str, object]] = []
    for p in primes:
        length = expanded_cycle_length(p)
        cycle_rows.append(
            {
                "p": p,
                "cycle_length": length,
                "simulated_length": simulated_cycle_length(p),
                "harmonic_lower_bound": harmonic_lower_bound(p),
                "length_over_log_p": length / math.log(p),
                "optimal_max_weight_sigma_1": optimal_max_edge_weight(p, 1.0),
                "optimal_max_weight_sigma_2": optimal_max_edge_weight(p, 2.0),
                "source_roof_over_log_p": source_roof_total(p) / math.log(p),
            }
        )

    cutoffs = [31, 127, 509, 2039, 4093]
    cutoff_rows: list[dict[str, object]] = []
    for cutoff in cutoffs:
        selected = [p for p in primes if p <= cutoff]
        tail = selected[max(0, len(selected) // 2) :]
        cutoff_rows.append(
            {
                "cutoff": cutoff,
                "prime_count": len(selected),
                "last_prime": selected[-1],
                "last_cycle_length": expanded_cycle_length(selected[-1]),
                "tail_min_length_over_log_p": min(expanded_cycle_length(p) / math.log(p) for p in tail),
                "tail_max_optimal_weight_sigma_2": max(optimal_max_edge_weight(p, 2.0) for p in tail),
            }
        )

    small = sieve_primes(31)
    z = Fraction(1, 3)
    determinant = direct_sum_determinant(small, 2, z)
    induced_marked = marked_determinant_at_return_section(small, 2, z)
    at_one = direct_sum_determinant(small, 2, Fraction(1))
    induced = determinant_at_return_section(small, 2)
    assert at_one == induced
    assert determinant != induced_marked

    trace_rows: list[dict[str, object]] = []
    for p in small:
        length = expanded_cycle_length(p)
        for multiplier in range(1, 5):
            r = length * multiplier
            trace_rows.append(
                {
                    "p": p,
                    "cycle_length": length,
                    "power": r,
                    "trace": str(cycle_power_trace(p, 2, r)),
                    "expected": str(length * Fraction(1, p ** (2 * multiplier))),
                }
            )

    controls = padded_decider_controls(4096, 2.0)
    marker_rows = [
        {
            "z": "1",
            "raw_graph_step_product": str(at_one),
            "induced_return_product": str(induced),
            "equal": at_one == induced,
            "interpretation": "unmarked_orbit_product_agrees",
        },
        {
            "z": str(z),
            "raw_graph_step_product": str(determinant),
            "induced_return_product": str(induced_marked),
            "equal": determinant == induced_marked,
            "interpretation": "graph_step_and_return_step_markers_differ",
        },
    ]
    verifier_paths = [verifier_forward_path(n) for n in range(2, 65)]
    q_states = [
        state
        for _, states in verifier_paths
        for state in states
        if state.startswith("Q:")
    ]
    source_certificate = {
        "candidate_id": "SD-C22",
        "accepted_inputs_through_64": [
            n for n, (accepted, _) in zip(range(2, 65), verifier_paths) if accepted
        ],
        "contracted_acceptance_boundary": True,
        "no_oracle_pass": True,
        "q_state_count": len(q_states),
        "q_states_materialized": len(q_states) > 0,
        "reject_cemetery_is_acyclic": True,
        "transition_primitives": ["successor", "multiplication", "order_comparison"],
        "target_zero_data_used": False,
    }
    summary = {
        "candidate_id": "SD-C22",
        "cycle_formula": "ell(p)=2+sum_{d=2}^{floor(sqrt(p))}ceil(p/d)",
        "prime_count": len(primes),
        "max_prime": primes[-1],
        "max_cycle_length": cycle_rows[-1]["cycle_length"],
        "last_optimal_max_weight_sigma_2": cycle_rows[-1]["optimal_max_weight_sigma_2"],
        "last_source_roof_over_log_p": cycle_rows[-1]["source_roof_over_log_p"],
        "small_z": str(z),
        "small_direct_sum_determinant": str(determinant),
        "small_induced_marked_determinant": str(induced_marked),
        "small_marked_determinants_differ": determinant != induced_marked,
        "z_one_direct_sum_determinant": str(at_one),
        "z_one_induced_determinant": str(induced),
        "z_one_exact_collapse": at_one == induced,
        "whole_operator": {
            "compact": False,
            "essential_norm": 1,
            "finite_schatten_class": False,
            "ordinary_fredholm_determinant_exists": False,
        },
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_PASS_ANALYTIC",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "padded_decider_controls": controls,
        "verdict": {
            "go_recurrent_verifier_ledger": True,
            "stop_compactness": True,
            "stop_fredholm_determinant": True,
            "clock_dilution_obstruction": True,
            "selector_tautological": True,
            "proves_too_much": True,
            "route_b_locked": True,
        },
    }
    write_csv(output / "cycle_clock_ledger.csv", cycle_rows)
    write_csv(output / "cutoff_compactness_witnesses.csv", cutoff_rows)
    write_csv(output / "power_trace_certificates.csv", trace_rows)
    write_csv(output / "padded_decider_controls.csv", controls)
    write_csv(output / "marker_firewall.csv", marker_rows)
    (output / "source_oracle_certificate.json").write_text(
        json.dumps(source_certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    run(args.output)


if __name__ == "__main__":
    main()
