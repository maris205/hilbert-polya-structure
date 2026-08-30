#!/usr/bin/env python3
"""Producer-independent checker for the C245 event-network receipt."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c245_pulse_if_evidence.json"
SOURCE_COMMIT = "5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
EVALUATION_DATE = "2026-08-30"
R_VALUES = (F(1, 2), F(2, 3), F(3, 4))
EPS_VALUES = (F(1, 5), F(1, 4), F(1, 3))
N_VALUES = tuple(range(2, 9))
SEEDS = tuple(range(7))
EVENT_STEPS = 12

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}


def ftext(q: F | int) -> str:
    q = q if isinstance(q, F) else F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def groups(state: tuple[F, ...]) -> list[list[int]]:
    out: list[list[int]] = []
    used: set[int] = set()
    for i, value in enumerate(state):
        if i in used:
            continue
        g = [j for j, other in enumerate(state) if other == value]
        out.append(g)
        used.update(g)
    return out


def probe(r: F, n: int, seed: int) -> tuple[F, ...]:
    if seed == 0:
        return tuple(F(1) for _ in range(n))
    return tuple(r + (F(1) - r) * F((seed + 2 * i + i * i) % 8, 8) for i in range(n))


def step(state: tuple[F, ...], r: F, eps: F) -> tuple[tuple[F, ...], dict]:
    c = (F(1) - r) * eps
    m = min(state)
    scale = r / m
    scaled = tuple(u * scale for u in state)
    wave = sorted(i for i, u in enumerate(scaled) if u == r)
    after = list(scaled)
    fired: set[int] = set()
    generations: list[list[int]] = []
    while wave:
        generations.append(list(wave))
        for i in wave:
            fired.add(i)
            after[i] = F(1)
        fresh: list[int] = []
        for j in range(len(after)):
            if j in fired:
                continue
            after[j] -= c * len(wave)
            if after[j] <= r:
                after[j] = r
                fresh.append(j)
        wave = sorted(fresh)
    for i in fired:
        after[i] = F(1)
    result = tuple(after)
    gb, ga = groups(state), groups(result)
    block_receipts = []
    for old in gb:
        containers = [new for new in ga if set(old).issubset(new)]
        block_receipts.append({"old_block": old, "containing_new_block": containers[0] if len(containers) == 1 else None, "preserved": len(containers) == 1})
    no_split = all(x["preserved"] for x in block_receipts)
    return result, {"pre_state": [ftext(x) for x in state], "scaled_state": [ftext(x) for x in scaled], "scale": ftext(scale), "firing_indices": sorted(fired), "avalanche_generations": generations, "post_state": [ftext(x) for x in result], "clusters_before": gb, "clusters_after": ga, "cluster_count_before": len(gb), "cluster_count_after": len(ga), "old_block_receipts": block_receipts, "partition_no_split": no_split, "coarsens_or_equal": bool(no_split and len(ga) <= len(gb))}


def make_row(r: F, eps: F, n: int, seed: int) -> dict:
    state = probe(r, n, seed)
    initial = state
    history: list[dict] = []
    word: list[int] = []
    seen: dict[tuple[F, ...], int] = {}
    period = None
    for _ in range(EVENT_STEPS):
        if state in seen:
            period = len(history) - seen[state]
            break
        seen[state] = len(history)
        state, rec = step(state, r, eps)
        history.append(rec)
        word.append(len(rec["firing_indices"]))
    if period is None and state in seen:
        period = len(history) - seen[state]
    sync = initial == tuple(F(1) for _ in range(n))
    return {"r": ftext(r), "epsilon": ftext(eps), "n": n, "seed": seed, "initial_state": [ftext(x) for x in initial], "initial_clusters": groups(initial), "event_word": word, "history": history, "events_recorded": len(history), "cycle_period": period, "synchronous_initial": sync, "synchronous_absorbing": bool(sync and period == 1 and word == [n]), "primitive_event_cycle": bool(sync and period == 1 and word == [n]), "partition_nonincreasing": all(h["coarsens_or_equal"] for h in history), "max_cluster_count": max((h["cluster_count_before"] for h in history), default=len(groups(initial))), "final_state": [ftext(x) for x in state]}


def expected() -> tuple[list[dict], list[dict], list[dict]]:
    rows = [make_row(r, e, n, s) for r in R_VALUES for e in EPS_VALUES for n in N_VALUES for s in SEEDS]
    sync = [x for x in rows if x["synchronous_initial"]]
    coarse = []
    for x in rows:
        final = groups(tuple(F(v) for v in x["final_state"]))
        coarse.append({"r": x["r"], "epsilon": x["epsilon"], "n": x["n"], "seed": x["seed"], "cluster_counts": [h["cluster_count_before"] for h in x["history"]] + ([len(final)] if x["history"] else []), "pairwise_no_split": all(h["partition_no_split"] for h in x["history"]), "old_block_checks": sum(len(h["old_block_receipts"]) for h in x["history"]), "nonincreasing": x["partition_nonincreasing"]})
    return rows, sync, coarse


_CACHE = None


def validate(data: dict) -> int:
    global _CACHE
    checks = 0

    def check(ok: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            raise AssertionError(label)

    check(set(data) == TOP_KEYS, "top closure")
    check(data["schema"] == "hcs-c245-pulse-if-v1", "schema")
    check(data["candidate_id"] == "HCS-C245", "candidate")
    check(data["evaluation_date"] == EVALUATION_DATE and data["fixed_epoch"] == FIXED_EPOCH, "date/epoch")
    check(data["source_commit"] == SOURCE_COMMIT and data["scope_literal"] == SCOPE, "source/scope")
    check(data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict")
    check(set(data["scope_flags"]) == SCOPE_KEYS and all(v is False for v in data["scope_flags"].values()), "scope firewall")
    check("finite" in data["theorem"]["literature_scope"] and "not" in data["theorem"]["literature_scope"], "literature boundary")
    check(len(data["exact_identities"]) == 8, "identity count")
    check(data["regression"]["r_values"] == ["1/2", "2/3", "3/4"], "r grid")
    check(data["regression"]["epsilon_values"] == ["1/5", "1/4", "1/3"], "epsilon grid")
    check(data["regression"]["n_values"] == list(range(2, 9)) and data["regression"]["seed_values"] == list(range(7)), "probe grid")
    expected_ids = [
        {"name": "rise_inverse", "formula": "phi(y)=log(1-(1-r)y)/log(r)"},
        {"name": "free_flight", "formula": "u_i(t)=u_i(0)*exp(-a*t), next threshold scale=r/min(u)"},
        {"name": "pulse", "formula": "u' = max(r, u-(1-r)epsilon)"},
        {"name": "common_scaling", "formula": "u_i=u_j implies scaled_u_i=scaled_u_j"},
        {"name": "partition_order", "formula": "number_of_equal-coordinate_blocks_after <= before"},
        {"name": "synchronous_return", "formula": "(1,...,1) -> (1,...,1), event word [N]"},
        {"name": "primitive_word", "formula": "[N] is not a repetition of a shorter event word"},
        {"name": "parameter_domain", "formula": "0<r<1, 0<epsilon<1, N>=2"},
    ]
    check(data["exact_identities"] == expected_ids, "identity values")
    expected_citations = [
        {"key": "MirolloStrogatz1990", "claim": "strictly concave rise and all-to-all excitatory pulse coupling yield almost-everywhere synchronization for identical integrate-and-fire oscillators", "source": "https://doi.org/10.1137/0150098", "doi": "10.1137/0150098"},
        {"key": "Bottani1996", "claim": "globally coupled synchronization analysis beyond concavity/convexity restrictions", "source": "https://doi.org/10.1103/PhysRevE.54.2334", "doi": "10.1103/PhysRevE.54.2334"},
    ]
    check(data["citations"] == expected_citations, "citation closure")
    check(len(data["nonclaims"]) == 5, "nonclaim closure")
    if _CACHE is None:
        _CACHE = expected()
    rows, sync, coarse = _CACHE
    reg = data["regression"]
    check(reg["event_rows"] == rows, "event rows exact")
    check(reg["sync_rows"] == sync, "sync rows exact")
    check(reg["coarsening_rows"] == coarse, "coarsening rows exact")
    check(reg["event_row_count"] == len(rows) == 441, "event count")
    check(reg["sync_row_count"] == len(sync) == 63, "sync count")
    check(reg["coarsening_row_count"] == len(coarse) == 441, "coarsening count")
    check(reg["event_steps"] == EVENT_STEPS, "step cutoff")
    check(all(x["synchronous_absorbing"] and x["primitive_event_cycle"] for x in sync), "sync theorem rows")
    check(all(x["partition_nonincreasing"] for x in rows), "coarsening rows")
    check(all(x["pairwise_no_split"] and x["old_block_checks"] > 0 for x in coarse), "pairwise old-block containment")
    for row in rows:
        for value in row["initial_state"] + row["final_state"]:
            check(str(F(value)) == value, "fraction serialization")
    return checks


def quick_preflight(data: dict) -> None:
    assert set(data) == TOP_KEYS
    assert data["payload_sha256"] == payload_hash(data)
    assert data["candidate_id"] == "HCS-C245" and data["fixed_epoch"] == FIXED_EPOCH
    print("C245 quick hostile preflight: PASS")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    data = json.loads(args.evidence.read_text())
    if args.quick:
        quick_preflight(data)
    else:
        print(f"C245 independent checker: PASS ({validate(data)} assertions; independent Fraction event replay)")


if __name__ == "__main__":
    main()
