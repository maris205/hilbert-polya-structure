from datetime import datetime, timezone
from pathlib import Path

from action_audit.cli import _environment, build_parser


def test_cli_accepts_explicit_project_root():
    root = Path("/tmp/paper4-static-audit")
    arguments = build_parser().parse_args(["--project-root", str(root)])
    assert arguments.project_root == root


def test_runtime_environment_uses_actual_utc_clock():
    record = _environment(Path(__file__).resolve().parents[2], {})
    assert record["execution_date_utc"] == datetime.now(timezone.utc).date().isoformat()
    assert record["execution_timestamp_utc"].endswith("Z")
    assert "frozen document metadata" in record["document_lock_date_policy"]
