from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEDULER = ROOT / "scripts/run_r401_val_l3_a1_all_slabs.py"
STATIC_CHECKER = ROOT / "scripts/check_r401_val_l3_a1_static_independent.py"
BRANCH_CHECKER = ROOT / "scripts/check_r401_val_l3_a1_branch_independent.py"
COMPOSITE_CHECKER = ROOT / "scripts/check_r401_val_l3_a1_composite_independent.py"
RELEASE_SOURCE = ROOT / "scripts/build_r401_val_l3_a1_release_provenance.py"
RELEASE_TEST_SOURCE = ROOT / "tests/test_r401_val_l3_a1_release_provenance.py"


def load(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


R = load(RELEASE_SOURCE, "l3_a1_e2e_release")
RT = load(RELEASE_TEST_SOURCE, "l3_a1_e2e_release_fixture")


def command(*arguments: str, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *arguments],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def test_complete_204_cell_mock_generation_to_68_role_release(tmp_path: Path) -> None:
    project = tmp_path / "project"
    result = project / R.RESULT_RELATIVE
    project.mkdir()

    static_run = command(
        str(SCHEDULER),
        "--mock-only",
        "--mock-static-cells", "102",
        "--output", str(result),
    )
    assert '"completed_cells": 102' in static_run.stdout
    command(str(STATIC_CHECKER), "--input-dir", str(result))
    command(str(STATIC_CHECKER), "--input-dir", str(result), "--postcheck")

    branch_run = command(
        str(SCHEDULER),
        "--mock-only",
        "--mock-branch-cells", "102",
        "--resume",
        "--output", str(result),
    )
    assert '"completed_cells": 102' in branch_run.stdout
    command(str(BRANCH_CHECKER), "--input-dir", str(result))
    command(str(BRANCH_CHECKER), "--input-dir", str(result), "--postcheck")

    composite_run = command(
        str(SCHEDULER),
        "--mock-only",
        "--finalize-mock-composite",
        "--resume",
        "--output", str(result),
    )
    assert "composite" in composite_run.stdout
    command(str(COMPOSITE_CHECKER), "--input-dir", str(result))
    command(str(COMPOSITE_CHECKER), "--input-dir", str(result), "--postcheck")

    checker = json.loads((result / "independent_checker.json").read_text(encoding="utf-8"))
    assert checker["checker_status"] == "PASS_MOCK_INDEPENDENT_REPLAY"
    assert checker["replay_counts"] == {
        "static_cells": 102,
        "branch_cells": 102,
        "component_chains": 2,
    }
    assert checker["scientific_licensing_enabled"] is False
    assert checker["milestone_status"] is None
    assert checker["theorem_status"] is None
    assert checker["final_status"] is None

    controls_before = {
        name: (result / name).read_bytes()
        for name in ("composite_summary.json", "composite_manifest.json")
    }
    resumed = command(
        str(SCHEDULER),
        "--mock-only",
        "--finalize-mock-composite",
        "--resume",
        "--output", str(result),
    )
    assert "RESUMED_COMMITTED" in resumed.stdout
    assert {
        name: (result / name).read_bytes() for name in controls_before
    } == controls_before

    RT.populate_inputs(project)
    report = (
        "Status: PASS_MOCK_PROVENANCE_REPLAY\n"
        "milestone_status = null\n"
        "theorem_status = null\n"
        "final_status = null\n"
        f"Claim boundary: {R.MOCK_CLAIM_BOUNDARY}\n"
    )
    (result / "R401_VAL_L3_A1_REPORT.md").write_text(report, encoding="utf-8")
    RT.publish_mock_freeze(project)

    released = R.build_release(project)
    assert released["release_status"] == "PASS_MOCK_PROVENANCE_REPLAY"
    assert len(released["roles"]) == 68
    assert released["scientific_licensing_enabled"] is False
    assert released["milestone_status"] is None
    assert released["theorem_status"] is None
    assert released["final_status"] is None
    assert R.verify_release(project) == released

    before = (result / "RELEASE_PROVENANCE.json").read_bytes()
    rejected = subprocess.run(
        [
            sys.executable,
            str(SCHEDULER),
            "--mock-only",
            "--finalize-mock-composite",
            "--resume",
            "--output", str(result),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
    )
    assert rejected.returncode == 1
    assert "namespace mismatch" in rejected.stderr
    assert (result / "RELEASE_PROVENANCE.json").read_bytes() == before
