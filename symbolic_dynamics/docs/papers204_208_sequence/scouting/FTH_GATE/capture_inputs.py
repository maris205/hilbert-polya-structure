"""Actual archival input snapshot and checksum validation; no science runs."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
root = base.parents[3]
author = base.parent / "finite_systems_nineteenth"
paths = set(p for p in author.rglob("*") if p.is_file())
for manifest in [author / "HISTORICAL_INPUTS.sha256", author / "HISTORICAL_SUPPLEMENT.sha256"]:
    paths |= {root / line.split("  ", 1)[1] for line in manifest.read_text().splitlines()}
paths |= {base.parent / "FTH_ROOT_LOCAL_OBSERVATIONS.md", base.parent / "NINETEENTH_ROOT_INSPECTION.md",
          root / "docs/papers204_208_sequence/qa/SCOUT19_ROOT_INSPECTION.actual.json",
          root / "docs/papers204_208_sequence/ARTIFACT_CONTRACT.md"}
paths |= {p for p in base.rglob("*") if p.is_file()}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


before = {str(p.relative_to(root)): sha(p) for p in sorted(paths)}
snapshot = base / "reviewed_input_snapshot"
snapshot.mkdir(exist_ok=False)
for rel in before:
    target = snapshot / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(root / rel, target)
after = {rel: sha(root / rel) for rel in before}
copies = {rel: sha(snapshot / rel) for rel in before}
(base / "INPUT_PINS.sha256").write_text("".join(digest + "  " + rel + "\n" for rel, digest in before.items()))
argv = ["/usr/bin/sha256sum", "-c", str(base / "INPUT_PINS.sha256")]
started = time.time()
process = subprocess.run(argv, cwd=root, capture_output=True, check=False)
(base / "input_pin_check.stdout").write_bytes(process.stdout)
(base / "input_pin_check.stderr").write_bytes(process.stderr)
receipt = {"kind": "ARCHIVAL_INPUT_SNAPSHOT_NOT_SCIENTIFIC_EXECUTION", "argv": argv, "cwd": str(root),
           "started_epoch": started, "finished_epoch": time.time(), "exit": process.returncode,
           "before": before, "after": after, "snapshot": copies,
           "all_equal": before == after == copies, "files": len(before), "invocation": sys.argv,
           "flags": str(sys.flags)}
(base / "INPUT_CAPTURE.json").write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
print(json.dumps({key: receipt[key] for key in ["kind", "exit", "all_equal", "files"]}, sort_keys=True))
if process.returncode or not receipt["all_equal"]:
    raise SystemExit(1)
