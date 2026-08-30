#!/usr/bin/env python3
"""Deterministic exact receipt for a pulse-coupled integrate-and-fire network.

The event coordinates are ``u=exp(-a phi)``.  We freeze rational
``r=exp(-a)`` and rational pulse sizes, so every event operation is a
Fraction operation: free flight is a common rescaling, and a pulse subtracts
``c=(1-r)*epsilon`` with threshold clipping.  The receipt is deliberately a
finite N<=8 event atlas; it is not a census of all continuous state cells.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import os
from pathlib import Path

SOURCE_COMMIT = "5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
EVALUATION_DATE = "2026-08-30"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c245_pulse_if_evidence.json"
R_VALUES = (F(1, 2), F(2, 3), F(3, 4))
EPS_VALUES = (F(1, 5), F(1, 4), F(1, 3))
N_VALUES = tuple(range(2, 9))
SEEDS = tuple(range(7))
EVENT_STEPS = 12


def ftext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def canon_groups(state: tuple[F, ...]) -> list[list[int]]:
    """Equality clusters, ordered by first index (indices are labelled)."""
    groups: list[list[int]] = []
    seen: set[int] = set()
    for i, value in enumerate(state):
        if i in seen:
            continue
        group = [j for j, other in enumerate(state) if other == value]
        seen.update(group)
        groups.append(group)
    return groups


def initial_state(r: F, n: int, seed: int) -> tuple[F, ...]:
    """Rational, deterministic probes including sync and repeated clusters."""
    if seed == 0:
        return tuple(F(1) for _ in range(n))
    out: list[F] = []
    for i in range(n):
        # A small modular pattern gives both equal and unequal clusters while
        # staying strictly inside [r,1].
        q = ((seed + 2 * i + i * i) % 8)
        out.append(r + (F(1) - r) * F(q, 8))
    return tuple(out)


def event_step(state: tuple[F, ...], r: F, eps: F) -> tuple[tuple[F, ...], dict]:
    """Advance to the next threshold and close the all-to-all avalanche.

    In u-coordinates free flight multiplies all coordinates by r/min(u).
    Every firing oscillator emits one pulse; a receiver is clipped at r and
    joins the same avalanche.  Newly recruited firers emit the next
    simultaneous wave, sorted by index for canonical bytes.
    """
    c = (F(1) - r) * eps
    minimum = min(state)
    scale = r / minimum
    pre = tuple(u * scale for u in state)
    wave = sorted(i for i, u in enumerate(pre) if u == r)
    fired: set[int] = set()
    after = list(pre)
    generations: list[list[int]] = []
    while wave:
        generations.append(list(wave))
        for i in wave:
            fired.add(i)
            after[i] = F(1)
        new: list[int] = []
        for j in range(len(after)):
            if j in fired:
                continue
            after[j] -= c * len(wave)
            if after[j] <= r:
                after[j] = r
                new.append(j)
        wave = sorted(new)
    for i in fired:
        after[i] = F(1)
    result = tuple(after)
    groups_before = canon_groups(state)
    groups_after = canon_groups(result)
    block_receipts: list[dict] = []
    for old in groups_before:
        containers = [new for new in groups_after if set(old).issubset(new)]
        block_receipts.append({"old_block": old, "containing_new_block": containers[0] if len(containers) == 1 else None, "preserved": len(containers) == 1})
    no_split = all(x["preserved"] for x in block_receipts)
    record = {
        "pre_state": [ftext(x) for x in state],
        "scaled_state": [ftext(x) for x in pre],
        "scale": ftext(scale),
        "firing_indices": sorted(fired),
        "avalanche_generations": generations,
        "post_state": [ftext(x) for x in result],
        "clusters_before": groups_before,
        "clusters_after": groups_after,
        "cluster_count_before": len(groups_before),
        "cluster_count_after": len(groups_after),
        "old_block_receipts": block_receipts,
        "partition_no_split": no_split,
        "coarsens_or_equal": bool(no_split and len(groups_after) <= len(groups_before)),
    }
    return result, record


def event_row(r: F, eps: F, n: int, seed: int) -> dict:
    state = initial_state(r, n, seed)
    initial = state
    history: list[dict] = []
    event_word: list[int] = []
    seen: dict[tuple[F, ...], int] = {}
    cycle_period = None
    for step in range(EVENT_STEPS):
        if state in seen:
            cycle_period = step - seen[state]
            break
        seen[state] = step
        state, rec = event_step(state, r, eps)
        history.append(rec)
        event_word.append(len(rec["firing_indices"]))
    if cycle_period is None and state in seen:
        cycle_period = len(history) - seen[state]
    sync = initial == tuple(F(1) for _ in range(n))
    partition_nonincreasing = all(h["coarsens_or_equal"] for h in history)
    return {
        "r": ftext(r), "epsilon": ftext(eps), "n": n, "seed": seed,
        "initial_state": [ftext(x) for x in initial],
        "initial_clusters": canon_groups(initial),
        "event_word": event_word,
        "history": history,
        "events_recorded": len(history),
        "cycle_period": cycle_period,
        "synchronous_initial": sync,
        "synchronous_absorbing": bool(sync and cycle_period == 1 and event_word == [n]),
        "primitive_event_cycle": bool(sync and cycle_period == 1 and event_word == [n]),
        "partition_nonincreasing": partition_nonincreasing,
        "max_cluster_count": max((h["cluster_count_before"] for h in history), default=len(canon_groups(initial))),
        "final_state": [ftext(x) for x in state],
    }


def build() -> dict:
    rows: list[dict] = []
    for r in R_VALUES:
        for eps in EPS_VALUES:
            for n in N_VALUES:
                for seed in SEEDS:
                    rows.append(event_row(r, eps, n, seed))
    sync_rows = [row for row in rows if row["synchronous_initial"]]
    coarsening_rows = [
        {"r": row["r"], "epsilon": row["epsilon"], "n": row["n"], "seed": row["seed"],
         "cluster_counts": [h["cluster_count_before"] for h in row["history"]] + ([len(canon_groups(tuple(F(x) for x in row["final_state"])))] if row["history"] else []),
         "pairwise_no_split": all(h["partition_no_split"] for h in row["history"]),
         "old_block_checks": sum(len(h["old_block_receipts"]) for h in row["history"]),
         "nonincreasing": row["partition_nonincreasing"]}
        for row in rows
    ]
    data = {
        "schema": "hcs-c245-pulse-if-v1", "candidate_id": "HCS-C245",
        "evaluation_date": EVALUATION_DATE, "fixed_epoch": FIXED_EPOCH,
        "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "An exact rational event-map and cluster-coarsening receipt for an all-to-all excitatory integrate-and-fire network.",
        "frozen_object": {
            "network": "N identical oscillators with phase dot(phi)=1 on [0,1)",
            "rise": "U_a(phi)=(1-exp(-a*phi))/(1-exp(-a)), strictly concave for a>0",
            "transformed_coordinate": "u=exp(-a*phi), r=exp(-a); threshold u=r and reset u=1",
            "parameters": "r in {1/2,2/3,3/4}, epsilon in {1/5,1/4,1/3}, N in {2,...,8}",
            "pulse": "each firing sends epsilon in y=U coordinates; u decreases by c=(1-r)*epsilon and is clipped at r",
            "avalanche": "same-time closure in simultaneous recruitment waves; each newly recruited wave emits one further pulse and is index-sorted",
            "clock": "event count and exact rational transformed states; no arithmetic-prime clock",
            "atlas_cutoff": "seven deterministic rational initial seeds, twelve event steps, N<=8",
            "determinant_convention": "no determinant; event words are source-local labels only",
            "forbidden_data": "target primes/zeros, Euler factors, root numbers, automorphy, target divisors, Hilbert-Polya operators",
        },
        "theorem": {
            "event_map": "In u coordinates free flight is u_i -> r*u_i/min_j(u_j); a pulse is u_j -> max(r,u_j-(1-r)epsilon), with avalanche closure by repeated firer pulses.",
            "rationality": "For rational r, epsilon and rational event states, every event and avalanche state is Fraction-exact; firing tests use equality/inequality over Q.",
            "cluster_coarsening": "Identical coordinates remain identical under common rescaling and common pulses; an avalanche resets its recruited set together, so the equality partition cannot refine.",
            "synchrony_absorption": "The all-equal state u=(1,...,1) returns to itself after one all-N firing event and is an absorbing synchronized cluster.",
            "primitive_cycle": "The synchronized event word [N] has primitive period one; this is a source event cycle, not an arithmetic primitive orbit.",
            "literature_scope": "Mirollo-Strogatz almost-everywhere synchrony is cited under its hypotheses; the receipt separately certifies only the finite rational N<=8 probes and does not claim a complete continuous-state census.",
        },
        "regression": {
            "r_values": [ftext(x) for x in R_VALUES], "epsilon_values": [ftext(x) for x in EPS_VALUES],
            "n_values": list(N_VALUES), "seed_values": list(SEEDS), "event_rows": rows,
            "sync_rows": sync_rows, "coarsening_rows": coarsening_rows,
            "event_row_count": len(rows), "sync_row_count": len(sync_rows),
            "coarsening_row_count": len(coarsening_rows), "event_steps": EVENT_STEPS,
        },
        "exact_identities": [
            {"name": "rise_inverse", "formula": "phi(y)=log(1-(1-r)y)/log(r)"},
            {"name": "free_flight", "formula": "u_i(t)=u_i(0)*exp(-a*t), next threshold scale=r/min(u)"},
            {"name": "pulse", "formula": "u' = max(r, u-(1-r)epsilon)"},
            {"name": "common_scaling", "formula": "u_i=u_j implies scaled_u_i=scaled_u_j"},
            {"name": "partition_order", "formula": "number_of_equal-coordinate_blocks_after <= before"},
            {"name": "synchronous_return", "formula": "(1,...,1) -> (1,...,1), event word [N]"},
            {"name": "primitive_word", "formula": "[N] is not a repetition of a shorter event word"},
            {"name": "parameter_domain", "formula": "0<r<1, 0<epsilon<1, N>=2"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "exact rational event map, avalanche closure, partition coarsening and synchronized primitive event cycle",
            "strongest_failure": "no arithmetic carrier or target determinant; finite probes do not establish global synchrony beyond cited hypotheses",
        },
        "scope_flags": {
            "uses_target_zero_table": False, "uses_prime_table": False, "claims_arithmetic_local_data": False,
            "claims_euler_factors": False, "claims_root_numbers": False, "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False, "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"key": "MirolloStrogatz1990", "claim": "strictly concave rise and all-to-all excitatory pulse coupling yield almost-everywhere synchronization for identical integrate-and-fire oscillators", "source": "https://doi.org/10.1137/0150098", "doi": "10.1137/0150098"},
            {"key": "Bottani1996", "claim": "globally coupled synchronization analysis beyond concavity/convexity restrictions", "source": "https://doi.org/10.1103/PhysRevE.54.2334", "doi": "10.1103/PhysRevE.54.2334"},
        ],
        "nonclaims": [
            "The event receipt is a finite rational probe atlas for N<=8, seven seeds, and twelve events; it is not an exhaustive continuous-state cell census.",
            "Almost-everywhere synchrony is not re-proved by the finite receipt; the cited theorem is used only under its stated hypotheses.",
            "Tie hypersurfaces, epsilon=0, r->1, r->0, directed coupling and inhibitory pulses are boundary cases outside the frozen theorem.",
            "Event words and the one-cycle return are source-local labels, not arithmetic primitive orbits, Euler factors, or a target determinant.",
            "No arithmetic origin, automorphy, target functional equation, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    tmp = args.output.with_name(args.output.name + ".tmp")
    tmp.write_text(raw)
    os.replace(tmp, args.output)
    print(json.dumps({"status": "C245_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "evidence_sha256": sha256(raw.encode()).hexdigest(), "event_rows": len(data["regression"]["event_rows"]), "sync_rows": len(data["regression"]["sync_rows"])}, sort_keys=True))


if __name__ == "__main__":
    main()
