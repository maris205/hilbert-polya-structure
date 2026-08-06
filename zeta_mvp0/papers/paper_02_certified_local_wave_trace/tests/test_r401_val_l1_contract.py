from __future__ import annotations

import json
import hashlib
import re
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results/r401_val_l1_branch"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"


def test_r401_val_l1_v2_archive_has_only_the_local_branch_status() -> None:
    summary = json.loads((RESULT / "summary.json").read_text(encoding="utf-8"))
    checker = json.loads(
        (RESULT / "independent_checker.json").read_text(encoding="utf-8")
    )
    assert summary["protocol_id"] == "R401-VAL-L1-V2"
    assert summary["milestone_status"] == "PASS_CONTIGUOUS_LOCAL_BRANCH"
    assert summary["final_status"] is None
    assert len(summary["records"]) == 202
    assert all(record["passed"] for record in summary["records"])
    assert {record["precision_bits"] for record in summary["records"]} == {
        128,
        256,
    }
    assert checker["checker_status"] == "PASS"
    assert checker["arithmetic_replay_count"] == 202
    assert checker["job_failures"] == []
    assert all(checker["global_gates"].values())
    assert checker["final_status"] is None


def test_r401_val_l1_v2_plan_uses_prefrozen_guarded_bridge_hulls() -> None:
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    padding = Fraction(plan["bridge_hull_padding"])
    assert padding == Fraction(1, 10**18)
    assert plan["slab_count"] == 51
    assert plan["bridge_count"] == 50
    assert plan["coverage"] == ["0", "0.101"]
    assert all(Fraction(bridge["hull_padding"]) == padding for bridge in plan["bridges"])

    for left, right, bridge in zip(
        plan["slabs"][:-1], plan["slabs"][1:], plan["bridges"], strict=True
    ):
        assert Fraction(bridge["epsilon_lower"]) == max(
            Fraction(left["epsilon_lower"]), Fraction(right["epsilon_lower"])
        )
        assert Fraction(bridge["epsilon_upper"]) == min(
            Fraction(left["epsilon_upper"]), Fraction(right["epsilon_upper"])
        )


def test_invalidated_predecessors_remain_explicitly_quarantined() -> None:
    invalid_directories = (
        ROOT / "results/r401_val_local_slab_smoke.attempt0-invalid-energy-jacobian",
        ROOT / "results/r401_val_l1_branch.attempt1-invalid-bridge-rounding",
    )
    for directory in invalid_directories:
        notice = directory / "INVALIDATED.md"
        assert notice.is_file()
        text = notice.read_text(encoding="utf-8").lower()
        assert "not" in text and "pass" in text
        status = json.loads(
            (directory / "AUTHORITATIVE_STATUS.json").read_text(encoding="utf-8")
        )
        assert status["authoritative_status"] == "INVALID"
        assert status["internal_pass_fields_superseded"] is True
        assert status["may_be_cited_as_proof"] is False


def test_release_provenance_binds_freeze_results_and_invalidation_registry() -> None:
    release = json.loads(
        (RESULT / "RELEASE_PROVENANCE.json").read_text(encoding="utf-8")
    )
    assert release["release_status"] == "PASS_CONTIGUOUS_LOCAL_BRANCH"
    assert release["final_status"] is None
    for relative, expected in release["files"].items():
        payload = (ROOT / relative).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == expected
    registry = json.loads(
        (ROOT / "results/R401_VAL_INVALIDATION_REGISTRY.json").read_text(
            encoding="utf-8"
        )
    )
    for record in registry["invalidated_archives"]:
        payload = (ROOT / record["authoritative_status_file"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == record[
            "authoritative_status_sha256"
        ]


def test_local_monodromy_gap_is_strict_but_not_the_final_identity_gate() -> None:
    result = ROOT / "results/r401_val_l1_monodromy_gap"
    summary = json.loads((result / "summary.json").read_text(encoding="utf-8"))
    checker = json.loads(
        (result / "independent_checker.json").read_text(encoding="utf-8")
    )
    assert summary["protocol_id"] == "R401-VAL-L1-MG-V2"
    assert summary["milestone_status"] == "PASS_LOCAL_MONODROMY_GAP"
    assert summary["final_status"] is None
    assert len(summary["records"]) == 202
    assert all(record["strictly_above_3"] for record in summary["records"])
    assert checker["checker_status"] == "PASS"
    assert checker["protocol_id"] == "R401-VAL-L1-MG-V2"
    assert checker["replay_count"] == 202
    assert checker["phase_slope_replay_count"] == 202
    assert checker["directed_decimal_payload_count"] == 815
    assert checker["failures"] == []
    assert all(checker["global_gates"].values())

    # The raw monodromy gap is strong enough for D>3, but its interval width
    # is intentionally far above the final protocol's 2^-30 identity gate.
    widths = [
        Fraction(summary["per_precision"][bits]["maximum_width"]["numerator"])
        / Fraction(summary["per_precision"][bits]["maximum_width"]["denominator"])
        for bits in ("128", "256")
    ]
    assert all(width > Fraction(1, 2**30) for width in widths)
    release = json.loads(
        (result / "RELEASE_PROVENANCE.json").read_text(encoding="utf-8")
    )
    assert release["protocol_id"] == "R401-VAL-L1-MG-V2"
    assert release["release_status"] == "PASS_LOCAL_MONODROMY_GAP"
    assert release["decimal_display_policy"] == {
        "decimal_places": 18,
        "lower_bounds": "directed floor",
        "upper_bounds": "directed ceil",
        "exact_numerator_denominator_retained": True,
        "binary_float_conversion": False,
    }
    for relative, expected in release["files"].items():
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == expected


def test_local_monodromy_gap_decimal_bounds_are_exactly_directed() -> None:
    result = ROOT / "results/r401_val_l1_monodromy_gap"
    summary = json.loads((result / "summary.json").read_text(encoding="utf-8"))
    report = (result / "R401_VAL_L1_MONODROMY_GAP_REPORT.md").read_text(
        encoding="utf-8"
    )
    fixed = re.compile(r"^-?\d+\.\d{18}$")
    grid = Fraction(1, 10**18)

    def check_payload(payload: dict[str, object]) -> Fraction:
        exact = Fraction(int(payload["numerator"]), int(payload["denominator"]))
        floor = Fraction(str(payload["decimal_floor"]))
        ceil = Fraction(str(payload["decimal_ceil"]))
        assert payload["decimal_places"] == 18
        assert fixed.fullmatch(str(payload["decimal_floor"]))
        assert fixed.fullmatch(str(payload["decimal_ceil"]))
        assert floor <= exact <= ceil
        assert 0 <= ceil - floor <= grid
        return exact

    payload_count = 0
    for record in summary["records"]:
        for name in (
            "d_m_lower",
            "d_m_upper",
            "phase_slope_lower",
            "phase_slope_upper",
        ):
            check_payload(record[name])
            payload_count += 1
    for bits in ("128", "256"):
        aggregates = summary["per_precision"][bits]
        for name in ("minimum_lower", "minimum_interval_upper", "maximum_width"):
            check_payload(aggregates[name])
            payload_count += 1
        assert f"`{aggregates['minimum_lower']['decimal_floor']}`" in report
        assert f"`{aggregates['maximum_width']['decimal_ceil']}`" in report
    phase = summary["phase_section_regularity"]["minimum_phase_slope_lower"]
    assert check_payload(phase) > 0
    payload_count += 1
    assert f"`{phase['decimal_floor']}`" in report
    assert payload_count == 815
    assert "decimal_18" not in json.dumps(summary)
    assert summary["phase_section_regularity_gate"] is True
