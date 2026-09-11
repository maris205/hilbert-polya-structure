#!/usr/bin/env python3
"""Read-only scoped artifact audit; no numerical replay is implied."""
from hashlib import sha256
import json
from pathlib import Path
import re


def main():
    directory = Path(__file__).resolve().parent
    workspace = directory.parents[3]
    manifest = directory / "SHA256SUMS"
    entries = {}
    for line in manifest.read_text().splitlines():
        digest, name = line.split("  ", 1)
        assert name not in entries and name != manifest.name
        assert Path(name).name == name
        entries[name] = digest
        assert sha256((directory / name).read_bytes()).hexdigest() == digest, name
    actual = {p.name for p in directory.iterdir() if p.is_file() and p != manifest}
    assert set(entries) == actual, (set(entries) - actual, actual - set(entries))
    historical = 0
    for line in (directory / "HISTORICAL_INPUTS.sha256").read_text().splitlines():
        digest, name = line.split("  ", 1)
        assert not Path(name).is_absolute()
        assert sha256((workspace / name).read_bytes()).hexdigest() == digest, name
        historical += 1
    local_links = 0
    for document in directory.glob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
            if target.startswith(("http://", "https://")):
                continue
            target = target.split("#", 1)[0]
            if target:
                assert (document.parent / target).resolve().exists(), (document.name, target)
                local_links += 1
    receipt = json.loads((directory / "REPLAY_PAIR.json").read_text())
    assert receipt["status"] == "PASS" and receipt["dependencies_unchanged"]
    assert receipt["dependencies_before"] == receipt["dependencies_after"]
    for name, digest in receipt["dependencies_before"].items():
        assert sha256((directory / name).read_bytes()).hexdigest() == digest, name
    assert len(receipt["runs"]) == 4
    for run in receipt["runs"]:
        raw = run["stdout"].encode()
        assert run["exit_code"] == run["raw_bytes_comparison_exit"] == 0
        assert run["stderr"] == "" and len(raw) == run["stdout_bytes"]
        assert sha256(raw).hexdigest() == run["stdout_sha256"]
        assert raw == (directory / run["canonical"]).read_bytes()
    census = json.loads((directory / "CANONICAL.json").read_text())
    deductions = json.loads((directory / "PROOF_CANONICAL.json").read_text())
    assert census["literal_maps"] == 6 and census["boxes"] == len(census["profiles"]) == 84
    assert sum(p["states"] for p in census["profiles"]) == census["states_across_boxes"] == 109867
    assert census["assertions"] == 447552 and deductions["assertions"] == 985626
    assert deductions["witnesses"]["MER_3x3_four_cycle"] == [41, 150, 296, 210, 41]
    print(json.dumps({"status": "PASS", "role": "artifact_consistency_not_fresh_numerical_replay",
                      "nonself_manifest_files": len(entries), "historical_pins": historical,
                      "local_markdown_links": local_links, "scientific_pair_pins": len(receipt["dependencies_before"]),
                      "embedded_raw_canonical_comparisons": len(receipt["runs"]),
                      "literal_maps": 6, "dispositions": "six NO_PROMOTION"}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
