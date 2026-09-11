#!/usr/bin/env python3
"""Read-only final artifact integrity; not a mathematical execution."""
import hashlib
import json
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
WORKSPACE = BASE.parents[3]


def check_pins(file, root):
    paths = []
    for line in file.read_text().splitlines():
        wanted, name = line.split("  ", 1)
        path = root/name
        assert path.is_file(), ("missing pin", name)
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        assert got == wanted, ("changed pin", name, wanted, got)
        paths.append(name)
    assert len(paths) == len(set(paths)), ("duplicate pins", file)
    return paths


def main():
    names = check_pins(BASE/"SHA256SUMS", BASE)
    actual = {str(p.relative_to(BASE)) for p in BASE.rglob("*")
              if p.is_file() and p.name != "SHA256SUMS"}
    assert actual == set(names), ("manifest coverage", actual-set(names), set(names)-actual)
    inputs = check_pins(BASE/"INPUTS.sha256", WORKSPACE)
    links = 0
    for file in BASE.rglob("*.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", file.read_text()):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].strip("<>")
            if not target:
                continue
            links += 1
            assert (file.parent/target).exists(), ("broken local link", str(file), target)
    print(json.dumps({"role": "read_only_final_artifact_integrity_not_mathematical_replay",
                      "manifest_entries": len(names), "context_input_pins": len(inputs),
                      "local_links_checked": links, "full_nonself_manifest": True,
                      "all_pins_pass": True, "status": "PASS"}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
