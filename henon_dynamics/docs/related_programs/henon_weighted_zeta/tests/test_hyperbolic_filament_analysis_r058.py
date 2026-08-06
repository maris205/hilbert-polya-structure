from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "scripts" / "analyze_hyperbolic_filament_r058.py"
OUTPUT = PROJECT_ROOT / "results" / "hyperbolic_filament_analysis_r058.json"
CHECKER = (
    PROJECT_ROOT
    / "results"
    / "hyperbolic_filament_independent_check_r058.json"
)
GRAPH = PROJECT_ROOT / "results" / "hyperbolic_filament_r058.json"
THEORY = PROJECT_ROOT / "results" / "hyperbolic_covering_r058.json"
DERIVATION = PROJECT_ROOT / "R058_COVERING_DERIVATION.md"
COVERING_PROOF = PROJECT_ROOT / "R058_COVERING_PROOF.md"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def test_r058_independent_checker_persisted_pass() -> None:
    payload = json.loads(CHECKER.read_text(encoding="utf-8"))
    assert payload["all_checks_pass"] is True
    assert (
        payload["fixed_source_checks"]["total_source_target_pair_count"]
        == 25_591_104
    )
    assert payload["refinement_checks"]["pass"] is True
    assert payload["lineage_checks"]["pass"] is True
    assert payload["symbolic_bridge_checks"]["pass"] is True
    assert payload["input_sha256"] == sha256_file(GRAPH)
    assert payload["theory_sha256"] == sha256_file(THEORY)
    assert all(
        not Path(pair["refinement_artifact"]).is_absolute()
        for pair in payload["refinement_checks"]["pairs"]
    )


def test_r058_analysis_outputs() -> None:
    subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(OUTPUT.read_text(encoding="utf-8"))
    assert payload["decisions"]["all_r058_gates_pass"] is True
    assert payload["input_checks"]["checker_graph_hash_alignment"] is True
    assert payload["input_checks"]["checker_theory_hash_alignment"] is True
    assert payload["proof_artifacts"]["derivation"]["sha256"] == sha256_file(
        DERIVATION
    )
    assert payload["proof_artifacts"]["covering_proof"][
        "sha256"
    ] == sha256_file(COVERING_PROOF)
    aggregate = payload["aggregate_metrics"]
    assert abs(aggregate["mean_size_exponent"] - 1.0385280336057081) < 1e-14
    assert 0.50 < aggregate["coverage_min"] < aggregate["coverage_max"] < 0.54
    assert aggregate["closed_identity_sidecar_pass_count"] == 9
