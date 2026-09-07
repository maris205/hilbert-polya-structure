"""Seal completed candidate gate with actual archival checks, never science."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv, cwd):
    started = time.time()
    process = subprocess.run(argv, cwd=cwd, capture_output=True, check=False)
    result = {"argv": list(map(str, argv)), "cwd": str(cwd), "exit": process.returncode,
              "started_epoch": started, "finished_epoch": time.time(),
              "stdout": process.stdout.decode(), "stderr": process.stderr.decode()}
    if process.returncode:
        raise RuntimeError(result)
    return result


if (BASE / "SHA256SUMS").exists():
    raise RuntimeError("ALREADY_SEALED_NO_OVERWRITE")
initial = sorted(p for p in BASE.rglob("*") if p.is_file())
before = {str(p.relative_to(BASE)): sha(p) for p in initial}
(BASE / "VALIDATION_INPUTS.sha256").write_text("".join(d + "  " + p + "\n" for p, d in before.items()))
tools_before = {str(Path(p).resolve()): sha(Path(p).resolve()) for p in ["/usr/bin/sha256sum", "/usr/bin/cmp"]}
commands = []
for name, cwd in [("INPUT_PINS.sha256", ROOT), ("SUPPLEMENT_INPUTS.sha256", ROOT),
                  ("INPUT_PINS.sha256", BASE / "reviewed_input_snapshot"),
                  ("SUPPLEMENT_INPUTS.sha256", BASE / "supplementary_source_snapshot"),
                  ("VALIDATION_INPUTS.sha256", BASE)]:
    commands.append(run(["/usr/bin/sha256sum", "-c", str(BASE / name)], cwd))
for left, right in [("replay_01/producer.stdout", "replay_02/producer.stdout"),
                    ("CANONICAL.json", "replay_01/producer.stdout"),
                    ("CANONICAL.json", "replay_02/producer.stdout")]:
    commands.append(run(["/usr/bin/cmp", "--", str(BASE / left), str(BASE / right)], BASE))
links = []
for name in ["CANDIDATE_GATE.md", "SOURCE_AND_PROOF.md", "REPLAY_LOG.md", "PRE_AUTHOR_CODE_COMMITMENT.md"]:
    for destination in re.findall(r"\]\(([^)]+)\)", (BASE / name).read_text()):
        if "://" not in destination and not destination.startswith("#"):
            path = (BASE / destination.split("#")[0]).resolve()
            if not path.exists():
                raise RuntimeError(("MISSING_LOCAL_LINK", name, destination))
            links.append({"source": name, "destination": destination})
findings = json.loads((BASE / "FINDINGS.json").read_text())
for key in ["open_mathematical_findings", "open_evidence_findings", "open_in_scope_source_blockers", "new_reviewer_lemma_repairs", "new_paper_numbers"]:
    if findings[key] != 0:
        raise RuntimeError(("OPEN_FINDING_OR_SCOPE", key))
if findings["scientific_runs"] != 2:
    raise RuntimeError("RUN_CENSUS")
after = {str(p.relative_to(BASE)): sha(p) for p in initial}
tools_after = {p: sha(Path(p)) for p in tools_before}
if before != after or tools_before != tools_after:
    raise RuntimeError("VALIDATION_MUTATED_INPUTS_OR_TOOLS")
report = {"kind": "ARCHIVAL_PACKAGE_SEAL_ZERO_NEW_SCIENCE", "status": "PASS",
          "initial_payload_count": len(initial), "actual_commands": commands,
          "tools_before": tools_before, "tools_after": tools_after, "before_after_equal": True,
          "local_links": links, "canonical_sha256": sha(BASE / "CANONICAL.json"),
          "scope": "candidate gate only; no manuscript build/view or root admission"}
(BASE / "SEAL_VALIDATION.json").write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
files = sorted(p for p in BASE.rglob("*") if p.is_file() and p != BASE / "SHA256SUMS")
manifest = "".join(sha(p) + "  " + str(p.relative_to(BASE)) + "\n" for p in files)
(BASE / "SHA256SUMS").write_text(manifest)
actual = run(["/usr/bin/sha256sum", "-c", "SHA256SUMS"], BASE)
expected_paths = [line.split("  ", 1)[1] for line in manifest.splitlines()]
actual_paths = [str(p.relative_to(BASE)) for p in sorted(BASE.rglob("*")) if p.is_file() and p.name != "__UNUSED__" and p != BASE / "SHA256SUMS"]
if actual_paths != expected_paths:
    raise RuntimeError("MANIFEST_COVERAGE_FAILURE")
print(json.dumps({"status": "SEALED", "outer_payload_count": len(files),
                  "outer_actual_sha256_check_exit": actual["exit"],
                  "outer_actual_sha256_ok_lines": len(actual["stdout"].splitlines()),
                  "full_nonself_path_coverage": True,
                  "manifest_sha256": sha(BASE / "SHA256SUMS"),
                  "canonical_sha256": sha(BASE / "CANONICAL.json"),
                  "prior_validation_commands": len(commands)}, sort_keys=True))
