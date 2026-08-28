#!/usr/bin/env python3
"""Producer-independent exact checker for C212."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c212_bouncing_evidence.json"
SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 8
EXPECTED = [
    ("forced_half", F(1), F(1, 2), F(1), F(2)),
    ("forced_three_quarters", F(5, 2), F(3, 4), F(3, 2), F(1)),
    ("forced_one_step", F(9, 4), F(0), F(2), F(5, 2)),
    ("zeno_half", F(1), F(1, 2), F(0), F(3)),
    ("zeno_three_quarters", F(2), F(3, 4), F(0), F(1)),
    ("sticking_r_zero", F(3, 2), F(0), F(0), F(4, 3)),
    ("elastic_identity_unit", F(1), F(1), F(0), F(1)),
    ("elastic_identity_scaled", F(5, 2), F(1), F(0), F(7, 4)),
    ("accelerating_unit", F(1), F(1), F(1), F(1)),
    ("accelerating_scaled", F(2), F(1), F(3, 2), F(1, 2)),
    ("forced_two_thirds", F(7, 3), F(2, 3), F(1, 3), F(5, 4)),
    ("forced_one_third", F(11, 6), F(1, 3), F(2), F(1, 2)),
]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def q(value: F) -> str:
    return str(value)


def regime(r: F, impulse: F) -> str:
    if r == 1 and impulse == 0:
        return "elastic_identity"
    if r == 1:
        return "accelerating_translation"
    if r == 0 and impulse == 0:
        return "sticking_edge"
    if impulse == 0:
        return "zeno_contraction"
    if r == 0:
        return "forced_one_step"
    return "forced_contraction"


def zeta_expected(r: F, impulse: F) -> dict:
    if r < 1 and impulse > 0:
        return {"regular_section": "S_+=(0,infinity)", "physical_fixed_point": q(impulse / (1 - r)),
                "physical_event_map_series": "1/(1-z)", "closed_section": "S_closed=[0,infinity)",
                "closed_affine_series": "1/(1-z)", "interpretation": "one positive-duration forced cycle"}
    if r < 1:
        return {"regular_section": "S_+=(0,infinity)", "physical_fixed_point": None,
                "physical_event_map_series": "1", "closed_section": "S_closed=[0,infinity)",
                "closed_affine_series": "1/(1-z)", "interpretation": "closed-section fixed point u=0 is rest, not a flight"}
    if impulse == 0:
        return {"regular_section": "S_+=(0,infinity)", "physical_fixed_point": "continuum",
                "physical_event_map_series": "undefined_continuum", "closed_section": "S_closed=[0,infinity)",
                "closed_affine_series": "undefined_continuum", "interpretation": "elastic periods are a continuum; u=0 is rest"}
    return {"regular_section": "S_+=(0,infinity)", "physical_fixed_point": None,
            "physical_event_map_series": "1", "closed_section": "S_closed=[0,infinity)",
            "closed_affine_series": "1", "interpretation": "translation has no fixed point"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    top = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator",
           "headline", "frozen_object", "theorem", "cases", "boundary_ledger", "summary", "route_a",
           "scope_flags", "citations", "nonclaims", "payload_sha256"}
    check(set(data) == top, "top-level key closure")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c212-affine-impact-bouncing-ball-v1", "schema")
    check(data["candidate_id"] == "HCS-C212", "candidate")
    check(data["evaluation_date"] == "2026-08-28", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict")
    check(all(value is False for value in data["scope_flags"].values()), "scope firewall")
    check("0<r<1" in data["theorem"]["strict_zeno"], "strict Zeno wording")
    check("r=0,J=0" in data["theorem"]["r_zero_boundary"], "r=0 boundary wording")
    check("S_+" in data["theorem"]["series_domain"], "section domain wording")
    check(data["summary"] == {"case_count": 12, "event_time_cells": 96, "impact_sample_cells": 36,
                               "iterate_count": 8, "strict_zeno_cases": 2, "r_zero_sticking_cases": 1,
                               "forced_cycle_cases": 5, "elastic_cases": 2, "translation_cases": 2}, "summary")

    for index, (row, spec) in enumerate(zip(data["cases"], EXPECTED)):
        case_id, g, r, impulse, u0 = spec
        expected_keys = {"case_id", "g", "restitution", "impulse", "u0", "iterate_count", "regime",
                         "u_sequence_n0_to_n8", "cumulative_time_n0_to_n8", "flight_roof_n0_to_n7",
                         "fixed_speed", "forced_period", "event_multiplier", "positive_flight_count_in_ledger",
                         "zeno_accumulation_time", "impact_samples", "zeta"}
        check(set(row) == expected_keys, f"case {index} keys")
        check(row["case_id"] == case_id and row["g"] == q(g) and row["restitution"] == q(r)
              and row["impulse"] == q(impulse) and row["u0"] == q(u0), f"case {index} parameters")
        check(row["iterate_count"] == N and row["regime"] == regime(r, impulse), f"case {index} regime")
        speeds = [u0]
        for _ in range(N):
            speeds.append(r * speeds[-1] + impulse)
        times = [F(0)]
        for speed in speeds[:-1]:
            times.append(times[-1] + 2 * speed / g)
        check(row["u_sequence_n0_to_n8"] == [q(x) for x in speeds], f"case {index} iterates")
        check(row["cumulative_time_n0_to_n8"] == [q(x) for x in times], f"case {index} times")
        check(row["flight_roof_n0_to_n7"] == [q(2 * x / g) for x in speeds[:-1]], f"case {index} roofs")
        check(row["event_multiplier"] == q(r), f"case {index} multiplier")
        check(row["positive_flight_count_in_ledger"] == sum(x > 0 for x in speeds[:-1]), f"case {index} positive flights")
        if r < 1:
            check(row["fixed_speed"] == q(impulse / (1 - r)), f"case {index} fixed speed")
            check(row["forced_period"] == (q(2 * impulse / ((1 - r) * g)) if impulse > 0 else None), f"case {index} forced period")
        else:
            check(row["fixed_speed"] is None and row["forced_period"] is None, f"case {index} translation fixed")
        expected_zeno = q(2 * u0 / (g * (1 - r))) if impulse == 0 and 0 < r < 1 else None
        check(row["zeno_accumulation_time"] == expected_zeno, f"case {index} Zeno boundary")
        check(row["zeta"] == zeta_expected(r, impulse), f"case {index} zeta domain")

        seeds = [(F(4), F(1), F(3)), (F(3, 2), F(-1), F(2)), (F(1, 2), F(0), F(1))]
        check(len(row["impact_samples"]) == 3, f"case {index} impact sample count")
        for sample, (label, (scaled_q, velocity, speed)) in zip(row["impact_samples"], zip(("upward", "downward", "resting_start"), seeds)):
            check(set(sample) == {"label", "q0", "v0", "discriminant_speed", "first_impact_time", "outgoing_speed_after_reset"}, f"case {index} sample keys")
            q0 = scaled_q / g
            check(sample["label"] == label and sample["q0"] == q(q0) and sample["v0"] == q(velocity), f"case {index} sample initial")
            check(sample["discriminant_speed"] == q(speed), f"case {index} sample speed")
            check(sample["first_impact_time"] == q((velocity + speed) / g), f"case {index} sample time")
            check(sample["outgoing_speed_after_reset"] == q(r * speed + impulse), f"case {index} sample reset")
        check(all(x >= 0 for x in speeds), f"case {index} nonnegative speeds")
        if r == 0 and impulse == 0:
            check(row["regime"] == "sticking_edge" and row["zeno_accumulation_time"] is None, "r=0 is not Zeno")
        if r == 1 and impulse == 0:
            check(row["zeta"]["physical_event_map_series"] == "undefined_continuum", "elastic continuum")

    check(len(data["boundary_ledger"]) == 5, "boundary ledger count")
    labels = {row["label"] for row in data["boundary_ledger"]}
    check("r=0, J=0" in labels and "J=0, 0<r<1" in labels, "boundary labels")
    for citation in data["citations"]:
        check(set(citation) == {"key", "claim", "title", "authors", "venue", "year", "doi"}, "citation closure")
        check(citation["doi"].startswith("10."), "citation DOI")
    print(f"C212 independent checker: PASS ({checks} exact assertions; 96 event-time cells)")
    print("Zeno/r=0 boundary, regular-vs-closed section series, and scope firewall: PASS")


if __name__ == "__main__":
    main()
