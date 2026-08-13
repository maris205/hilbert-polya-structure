import argparse
from pathlib import Path

from prime_multiplier.cli import run


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_full_cli_pipeline_writes_every_required_machine_artifact(tmp_path):
    output_root = tmp_path / "results"
    summary = run(
        argparse.Namespace(
            source_lock=PROJECT_ROOT / "experiments" / "source_lock.json",
            proof_package=PROJECT_ROOT / "notes" / "PROOF_PACKAGE.md",
            output_root=output_root,
            max_period=4,
        )
    )
    assert summary["status"] == "PASS"
    expected = {
        "source_lock_validation.json",
        "proof_audit.json",
        "control_audit.json",
        "parameter_preflight.json",
        "candidate_multiplier_audit.json",
        "conjugacy_audit.json",
        "symplectic_bridge_audit.json",
        "exact_polynomials.json",
        "negative_result_ledger.json",
        "command_environment_manifest.json",
        "run_summary.json",
    }
    assert expected <= {path.name for path in output_root.iterdir()}

