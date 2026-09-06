#!/usr/bin/env python3
"""Artifact closure for this owned negative scout; no numerical reruns."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import subprocess


here = Path(__file__).resolve().parent
root = here.parents[3]
history = [
    "docs/papers204_208_sequence/scouting/algebra/SCOUT_REPORT.md",
    "docs/papers204_208_sequence/scouting/algebra_second/SCOUT_REPORT.md",
    "docs/papers204_208_sequence/scouting/algebra_third/PROOF_AND_ADAPTER_NOTES.md",
    "docs/papers204_208_sequence/scouting/graph_algebra_fifth/INTAKE.md",
    "docs/papers197_201_sequence/scouting/nonlinear_fifth_20260905/SCOUT_AND_DISPOSITION.md",
    "docs/papers132_136_sequence/scouting/algebraic/SCOUT.md",
    "docs/papers172_176_sequence/scouting/combinatorial_crossdomain/focused_nonextractive/IDEA_LEDGER.md",
    "docs/papers172_176_sequence/scouting/combinatorial_crossdomain/focused_nonextractive/breadth2.py",
    "docs/papers204_208_sequence/scouting/combinatorial/SCOUT_REPORT.md",
]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def put(path, data):
    with path.open("xb") as out:
        out.write(data)


def check(condition, text):
    if not condition:
        raise AssertionError(text)


commands = []


def run(command, cwd):
    result = subprocess.run(command, cwd=cwd, capture_output=True)
    commands.append({"command": command, "cwd": str(cwd), "returncode": result.returncode,
                     "stdout": result.stdout.decode(), "stderr": result.stderr.decode()})
    check(result.returncode == 0, str(command))


check(not (here / "SHA256SUMS").exists(), "top seal already exists")
check(not (here / "SEAL_CHECK.json").exists(), "receipt already exists")
put(here / "INPUTS.sha256", "".join(f"{digest(root/name)}  {name}\n" for name in history).encode())
run(["sha256sum", "-c", "--quiet", str(here / "INPUTS.sha256")], root)
run_details = []
for directory, canonical, expected_checks, checks_key in (
    ("execution_01", "CANONICAL.json", 116472, "assertions"),
    ("inverse_execution_01", "QEF_INVERSE_CANONICAL.json", 16893, "checks"),
):
    location = here / directory
    manifest_lines = (location / "SHA256SUMS").read_text().splitlines()
    names = [line.split("  ", 1)[1] for line in manifest_lines]
    actual = sorted(str(path.relative_to(location)) for path in location.rglob("*")
                    if path.is_file() and path.name != "SHA256SUMS")
    check(sorted(names) == actual and len(names) == len(set(names)), "nested exact closure")
    run(["sha256sum", "-c", "--quiet", "SHA256SUMS"], location)
    before = location / "INPUTS_BEFORE.sha256"
    after = location / "INPUTS_AFTER.sha256"
    check(before.read_bytes() == after.read_bytes(), "input lists unchanged")
    for path in (before, after):
        run(["sha256sum", "-c", "--quiet", str(path)], root)
    parsed = json.loads((here / canonical).read_text())
    check(parsed[checks_key] == expected_checks, "canonical assertion count")
    for i in range(3):
        receipt = json.loads((location / f"run{i}.receipt.json").read_text())
        comparison = json.loads((location / f"cmp{i}.receipt.json").read_text())
        check(receipt["returncode"] == comparison["returncode"] == 0, "actual exits")
        check((location / f"run{i}.stderr").read_bytes() == b"", "empty producer stderr")
        check((location / f"cmp{i}.stdout").read_bytes() == b"" and
              (location / f"cmp{i}.stderr").read_bytes() == b"", "empty cmp outputs")
        check(receipt["stdout_sha256"] == digest(location / f"run{i}.stdout"), "stdout receipt digest")
        run(["cmp", str(location / f"run{i}.stdout"), str(here / canonical)], here)
    run_details.append({"directory": directory, "manifest_entries": len(names),
                        "input_pins": len(before.read_text().splitlines()),
                        "canonical_sha256": digest(here/canonical),
                        "bytes": (here/canonical).stat().st_size,
                        "producer_checks_each": expected_checks})
links = []
for path in sorted(here.glob("*.md")):
    for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", path.read_text()):
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        check((path.parent/target).exists(), f"missing link {path.name}:{target}")
        links.append({"source": path.name, "target": target})
receipt = {"status": "PASS", "utc": datetime.now(timezone.utc).isoformat(),
           "new_numerical_runs": 0, "historical_input_pins": len(history),
           "packages": run_details, "commands": commands, "local_links": links,
           "caveat": "Initial old_LV label corrected in reports; original bytes preserved."}
put(here / "SEAL_CHECK.json", (json.dumps(receipt, sort_keys=True, indent=2)+"\n").encode())
paths = sorted(path for path in here.rglob("*") if path.is_file())
manifest = "".join(f"{digest(path)}  {path.relative_to(here)}\n" for path in paths)
put(here / "SHA256SUMS", manifest.encode())
print(json.dumps({"status": "PASS", "owned_manifest_entries": len(paths),
                  "manifest_sha256": digest(here/"SHA256SUMS"),
                  "historical_pins": len(history), "local_links": len(links),
                  "nested_manifest_entries": [r["manifest_entries"] for r in run_details]},
                 sort_keys=True))
