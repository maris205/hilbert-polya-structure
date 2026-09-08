#!/usr/bin/env python3
"""One-shot artifact seal. No scientific computation or numerical PASS."""
import base64
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path("/root/autodl-tmp/symbolic_dynamics")
PACKAGE = pathlib.Path(__file__).resolve().parent
INPUTS = [
    ".agents/skills/symbolic-dynamics-research/SKILL.md",
    "docs/research_state/WORKFLOW.md",
    "SYMBOLIC_DYNAMICS_STATE.md",
    "docs/papers211_215_sequence/PIPELINE_STATE.md",
    "docs/papers211_215_sequence/PROBLEM_ANCHOR.md",
    "docs/papers197_201_sequence/PROBLEM_ANCHOR.md",
    "docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md",
    "docs/papers204_208_sequence/ARTIFACT_CONTRACT.md",
    "docs/papers162_166_sequence/scouting/geometry_group/SCOUT.md",
    "docs/papers204_208_sequence/scouting/set_partition_sixth/PROOF_BOUNDARIES.md",
    "docs/papers204_208_sequence/scouting/set_partition_sixth/SCOUT_REPORT.md",
    "papers/165-low-weight-support-shortening/PROOF_PACKAGE.md",
    "papers/106-synchronous-mis-polarity-dynamics/main.tex",
    "papers/97-sumset-squaring-dynamics/main.tex",
    "docs/papers211_215_sequence/scouting/graph_lane/PROOF_PACKAGE.md",
    "docs/papers187_191_sequence/scouting/graph_lane/CANDIDATES.md",
    "docs/papers187_191_sequence/scouting/graph_lane/replacement/CANDIDATES.md",
]
GENERATED = [
    "INPUT_PINS.sha256", "PAYLOAD_PINS.sha256",
    "ARTIFACT_NATIVE_RECORD.json", "MANIFEST.sha256",
]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def put_new(name, data):
    with (PACKAGE / name).open("xb") as handle:
        handle.write(data)

def native(command, cwd):
    begin = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(command, cwd=cwd, capture_output=True, check=False)
    return {
        "command": command,
        "cwd": str(cwd),
        "started_utc": begin,
        "ended_utc": datetime.now(timezone.utc).isoformat(),
        "exit_code": result.returncode,
        "stdout_utf8": result.stdout.decode("utf-8"),
        "stderr_utf8": result.stderr.decode("utf-8"),
        "stdout_base64": base64.b64encode(result.stdout).decode("ascii"),
        "stderr_base64": base64.b64encode(result.stderr).decode("ascii"),
        "stdout_bytes": len(result.stdout),
        "stderr_bytes": len(result.stderr),
        "stdout_sha256": hashlib.sha256(result.stdout).hexdigest(),
        "stderr_sha256": hashlib.sha256(result.stderr).hexdigest(),
    }

def main():
    assert PACKAGE == ROOT / "docs/papers211_215_sequence/scouting/set_code_lane"
    assert not any((PACKAGE / name).exists() for name in GENERATED), \
        "One-shot seal refuses existing outputs; preserve failures."
    lines = [f"{digest(ROOT / path)}  {path}\n" for path in INPUTS]
    put_new("INPUT_PINS.sha256", "".join(lines).encode("utf-8"))
    payload = sorted(path for path in PACKAGE.iterdir() if path.is_file())
    put_new("PAYLOAD_PINS.sha256", "".join(
        f"{digest(path)}  {path.name}\n" for path in payload
    ).encode("utf-8"))
    tool = shutil.which("sha256sum")
    assert tool is not None
    checks = [
        native([tool, "-c", str(PACKAGE / "INPUT_PINS.sha256")], ROOT),
        native([tool, "-c", str(PACKAGE / "PAYLOAD_PINS.sha256")], PACKAGE),
    ]
    record = {
        "kind": "CLOSED_DESK_ARTIFACT_ONLY_NOT_SCIENTIFIC_OR_TERMINAL",
        "scientific_runs": 0,
        "provenance_scope": "after-desk input snapshot and native current-byte checks",
        "python": {
            "executable": sys.executable,
            "version": sys.version,
            "resolved_sha256": digest(pathlib.Path(sys.executable).resolve()),
        },
        "native_tool": {
            "path": tool,
            "resolved_sha256": digest(pathlib.Path(tool).resolve()),
        },
        "input_pins": len(INPUTS),
        "payload_pins": len(payload),
        "commands": checks,
    }
    put_new("ARTIFACT_NATIVE_RECORD.json",
            (json.dumps(record, sort_keys=True, indent=2) + "\n").encode("utf-8"))
    all_pass = all(check["exit_code"] == 0 for check in checks)
    entries = sorted(path for path in PACKAGE.iterdir() if path.is_file())
    put_new("MANIFEST.sha256", "".join(
        f"{digest(path)}  {path.name}\n" for path in entries
    ).encode("utf-8"))
    print(json.dumps({
        "artifact_checks_pass": all_pass, "scientific_runs": 0,
        "input_pins": len(INPUTS), "payload_pins": len(payload),
        "manifest_entries": len(entries),
        "native_exit_codes": [check["exit_code"] for check in checks],
        "status": "NO_PROMOTION_HOLD_EXTERNAL",
    }, sort_keys=True))
    return 0 if all_pass else 1

if __name__ == "__main__":
    raise SystemExit(main())
