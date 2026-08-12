from __future__ import annotations

import hashlib
import importlib.util
import json
from decimal import Decimal
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "validated/capd_r401_phase_branch_tube_mp.cpp"
RUNNER = ROOT / "scripts/run_r401_val_l3_branch_tube_smoke.py"
CHECKER = ROOT / "scripts/check_r401_val_l3_branch_tube_smoke_independent.py"
RESULT = ROOT / "results/r401_val_l3_branch_tube_smoke"
PASS_STATUS = "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE"


def load_runner():
    spec = importlib.util.spec_from_file_location("branch_tube_runner", RUNNER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_checker():
    spec = importlib.util.spec_from_file_location("branch_tube_checker", CHECKER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def synthetic_transcript() -> str:
    lines = [
        "licensing=NON_LICENSING",
        "protocol_id=R401-VAL-L3-BT-S0",
        "milestone_status=null",
        "theorem_status=null",
        "final_status=null",
        "precision_bits=128",
        "taylor_order=24",
        "tolerance=1e-30",
        "phase_grid=64",
        "epsilon=[0 ,0.0021 ]",
        "root_box={[0 ,0 ],[0.149 ,0.150 ],[-0.00008 ,0.00008 ],[0.663 ,0.664 ]}",
        "tube_radius_sq=[0.0016 ,0.0016 ]",
        "omega_slow=[4.17 ,4.18 ]",
    ]
    state = "{[0 ,0 ],[0 ,0 ],[0 ,0 ],[0 ,0 ],[0 ,0 ],[0 ,0 ]}"
    for index in range(64):
        left = str(Decimal(index) / Decimal(64))
        right = str(Decimal(index + 1) / Decimal(64))
        stem = f"segment_{index:03d}"
        lines.extend(
            (
                f"{stem}_phase=[{left} ,{right} ]",
                f"{stem}_state={state}",
                f"{stem}_rslow_sq=[0 ,0.0001 ]",
                f"{stem}_margin_sq=[0.0015 ,0.0016 ]",
                f"{stem}_inside=1",
            )
        )
    lines.extend(
        (
            "solution_left_domain=0 ",
            "solution_right_domain=1.00000000000000000000000000000000000000000000 ",
            "solution_piece_count=21",
            f"terminal_state_box={state}",
            "maximum_rslow_sq_upper=[0.0001 ,0.0001 ]",
            "all_segments_inside=1",
            f"status={PASS_STATUS}",
        )
    )
    return "\n".join(lines) + "\n"


def test_cpp_uses_multiprecision_solution_curve_and_nonlicensing_gate() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    compact = " ".join(text.split())
    assert "MpC0Rect2Set flow_set(initial_box);" in compact
    assert "BranchTubeMpTimeMap::SolutionCurve solution" in compact
    assert "time_map(MpInterval(1), flow_set, solution)" in compact
    assert "const int phase_grid = 64;" in compact
    assert "MpInterval(1) / MpInterval(625)" in compact
    assert "sqr(omega_slow * state[0]) + sqr(state[2])" in compact
    assert "licensing=NON_LICENSING" in text
    for key in ("milestone_status=null", "theorem_status=null", "final_status=null"):
        assert key in text
    assert "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE" in text


def test_runner_accepts_actual_capd_space_format_and_scalar_domains() -> None:
    module = load_runner()
    replay = module.parse_transcript(synthetic_transcript())
    assert replay["precision_bits"] == 128
    assert replay["solution_piece_count"] == 21
    assert replay["maximum_rslow_sq_upper"] == "0.0001"
    assert replay["minimum_margin_sq_lower"] == "0.0015"
    assert replay["phase_cover_complete"] is True


@pytest.mark.parametrize(
    "old,new",
    (
        ("milestone_status=null", "milestone_status=PASS"),
        ("segment_010_phase=[0.15625 ,0.171875 ]", "segment_010_phase=[0.2 ,0.3 ]"),
        ("segment_020_margin_sq=[0.0015 ,0.0016 ]", "segment_020_margin_sq=[0 ,0.0016 ]"),
        ("solution_left_domain=0 ", "solution_left_domain=[0 ,0 ]"),
    ),
)
def test_runner_fails_closed_on_authority_grid_margin_or_domain_mutation(
    old: str, new: str
) -> None:
    module = load_runner()
    raw = synthetic_transcript()
    assert old in raw
    with pytest.raises(ValueError):
        module.parse_transcript(raw.replace(old, new, 1))


def test_runner_selects_exact_six_accepted_a412_primary_records() -> None:
    module = load_runner()
    summary = json.loads(module.L1_SUMMARY.read_text(encoding="utf-8"))
    selected = module.selected_records(summary)
    assert set(selected) == {
        (bits, slab)
        for bits in (128, 256)
        for slab in ("S000", "S025", "S050")
    }
    assert all(record["job_type"] == "primary" for record in selected.values())


def test_checker_is_separate_and_retains_null_scientific_authority() -> None:
    text = CHECKER.read_text(encoding="utf-8")
    assert "from run_r401_val_l3_branch_tube_smoke import" not in text
    assert "import run_r401_val_l3_branch_tube_smoke" not in text
    assert "Fraction(1, 625)" in text
    assert "raw_replay_count" in text
    assert '"milestone_status": None' in text
    assert '"theorem_status": None' in text
    assert '"final_status": None' in text
    assert "refusing to overwrite checker" in text


def test_independent_checker_recomputes_radius_and_rejects_forged_state() -> None:
    checker = load_checker()
    raw = synthetic_transcript()
    replay = checker.replay_transcript(raw)
    assert replay["maximum_rslow_sq_upper"] == 0
    forged_state = "{[1 ,1 ],[0 ,0 ],[0 ,0 ],[0 ,0 ],[0 ,0 ],[0 ,0 ]}"
    forged = raw.replace(
        "segment_000_state={[0 ,0 ],[0 ,0 ],[0 ,0 ],[0 ,0 ],[0 ,0 ],[0 ,0 ]}",
        f"segment_000_state={forged_state}",
        1,
    )
    assert forged != raw
    with pytest.raises(ValueError, match="independent rational tube gate"):
        checker.replay_transcript(forged)


def test_archived_six_job_smoke_and_independent_replay_are_consistent() -> None:
    summary = json.loads((RESULT / "summary.json").read_text(encoding="utf-8"))
    manifest = json.loads((RESULT / "manifest.json").read_text(encoding="utf-8"))
    checker = json.loads(
        (RESULT / "independent_checker.json").read_text(encoding="utf-8")
    )
    for payload in (summary, manifest, checker):
        assert payload["protocol_id"] == "R401-VAL-L3-BT-S0"
        assert payload["licensing"] == "NON_LICENSING"
        assert payload["milestone_status"] is None
        assert payload["theorem_status"] is None
        assert payload["final_status"] is None
    assert summary["prototype_status"] == PASS_STATUS
    assert len(summary["records"]) == 6
    assert all(record["passed"] for record in summary["records"])
    assert all(record["input_echo_gate"] for record in summary["records"])
    assert {record["precision_bits"] for record in summary["records"]} == {128, 256}
    assert {record["slab_id"] for record in summary["records"]} == {
        "S000",
        "S025",
        "S050",
    }
    assert max(
        Decimal(record["maximum_rslow_sq_upper"])
        for record in summary["records"]
    ) < Decimal("0.0016")
    assert min(
        Decimal(record["minimum_margin_sq_lower"])
        for record in summary["records"]
    ) > 0
    assert checker["checker_status"] == "PASS"
    assert checker["prototype_status"] == PASS_STATUS
    assert checker["raw_replay_count"] == 6
    assert checker["failures"] == []
    for name, expected in manifest["files"].items():
        assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == expected
