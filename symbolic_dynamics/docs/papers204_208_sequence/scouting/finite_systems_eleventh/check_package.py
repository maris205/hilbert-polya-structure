#!/usr/bin/env python3
"""Read-only evidence audit; deliberately does not run the science pilot."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest(path, root):
    names = []
    for line in path.read_text().splitlines():
        h, name = line.split("  ", 1)
        assert re.fullmatch("[0-9a-f]{64}", h)
        target = root/name
        assert target.is_file(), name
        assert sha(target) == h, name
        names.append(name)
    assert len(names) == len(set(names))
    return names


def main():
    entries = manifest(BASE/"SHA256SUMS", BASE)
    actual = sorted(str(p.relative_to(BASE)) for p in BASE.rglob("*")
                    if p.is_file() and p != BASE/"SHA256SUMS")
    assert sorted(entries) == actual
    external = manifest(BASE/"CONTEXT_INPUTS.sha256", ROOT)
    records = []
    for name in ("execution_01", "execution_02"):
        folder = BASE/name
        record = json.loads((folder/"EXECUTION.json").read_text())
        before = json.loads((folder/"INPUTS_BEFORE.json").read_text())
        after = json.loads((folder/"INPUTS_AFTER.json").read_text())
        assert set(before) == {"INTAKE.md", "pilot.py", "record.py"}
        assert before == after and record["input_pins_unchanged"]
        for item, h in before.items():
            assert sha(folder/item) == h == sha(BASE/item)
        assert record["exit_code"] == 0 and record["stderr_bytes"] == 0
        assert (folder/"stderr.txt").read_bytes() == b""
        raw = (folder/"stdout.jsonl").read_bytes()
        assert len(raw) == record["stdout_bytes"] == 6667
        assert sha(folder/"stdout.jsonl") == record["stdout_sha256"]
        rows = [json.loads(line) for line in raw.splitlines()]
        assert rows[-1] == dict(assertions=340299, full_boxes=12,
                               literal_count=2, status="PASS")
        assert [r["label"] for r in rows[:-1]] == [f"WZS_d{d}" for d in range(5)] + [
            f"ACP_r{r}_p{p}" for r,p in ((2,3),(2,5),(2,7),(2,11),(3,5),(3,7),(4,5))]
        assert sum(row["states"] for row in rows[:-1]) == 67111
        for row in rows[:-1]:
            assert sum(count for _, count in row["target_fibre_histogram"]) == row["states"]
            assert sum(size*count for size, count in row["target_fibre_histogram"]) == row["states"]
            assert sum(count for _, count in row["height_census"]) == row["states"]
        records.append(record)
    assert records[0]["comparison"] is None
    oldcmp = records[1]["comparison"]
    assert oldcmp["exit_code"] == oldcmp["stdout_bytes"] == oldcmp["stderr_bytes"] == 0
    assert (BASE/"execution_02/cmp.stdout.txt").read_bytes() == b""
    assert (BASE/"execution_02/cmp.stderr.txt").read_bytes() == b""
    cmd = ["cmp", "--", str(BASE/"execution_01/stdout.jsonl"), str(BASE/"execution_02/stdout.jsonl")]
    current = subprocess.run(cmd, capture_output=True)
    assert current.returncode == 0 and current.stdout == current.stderr == b""
    links = []
    for file in BASE.glob("*.md"):
        for raw in re.findall(r"\]\(([^)]+)\)", file.read_text()):
            if "://" in raw or raw.startswith("#"):
                continue
            target = (file.parent/raw.split("#",1)[0]).resolve()
            assert target.exists(), (str(file), raw)
            links.append([str(file.relative_to(BASE)), raw])
    print(json.dumps(dict(status="PASS", kind="read_only_artifact_audit_not_science",
                          manifest_entries=len(entries), context_pins=len(external),
                          local_links=len(links), archived_executions=2,
                          states_per_execution=67111, assertions_per_execution=340299,
                          current_cmp=dict(command=cmd, exit_code=current.returncode,
                                           stdout_bytes=0, stderr_bytes=0)), sort_keys=True))


if __name__ == "__main__":
    main()
