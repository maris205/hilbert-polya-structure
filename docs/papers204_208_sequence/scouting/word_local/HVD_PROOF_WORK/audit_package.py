#!/usr/bin/env python3
"""Read-only nonself-manifest, historical-pin, link and live-replay audit."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[4]


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def check_manifest(filename, root):
    names = []
    for line in (BASE / filename).read_text().splitlines():
        expected, name = line.split("  ", 1)
        assert re.fullmatch(r"[0-9a-f]{64}", expected), line
        path = root / name
        assert path.is_file(), str(path)
        assert digest(path.read_bytes()) == expected, ("pin_mismatch", name)
        names.append(name)
    assert len(names) == len(set(names)), ("duplicate_manifest_path", filename)
    return names


def main():
    inputs = check_manifest("INPUTS.sha256", ROOT)
    own = check_manifest("SHA256SUMS", BASE)
    actual = {str(path.relative_to(BASE)) for path in BASE.rglob("*")
              if path.is_file() and path.name != "SHA256SUMS"}
    assert set(own) == actual, ("manifest_coverage", sorted(actual - set(own)),
                                sorted(set(own) - actual))
    links = 0
    for source in sorted(BASE.glob("*.md")):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source.read_text()):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            assert (source.parent / target).resolve().exists(), (source.name, target)
            links += 1
    replays = []
    for script, canonical, replay in (
        ("verify_partial_theorems.py", "PARTIAL_CANONICAL.json", "PARTIAL_REPLAY.json"),
        ("probe_sentinels.py", "SENTINELS_CANONICAL.json", "SENTINELS_REPLAY.json"),
    ):
        expected = (BASE / canonical).read_bytes()
        assert expected == (BASE / replay).read_bytes(), ("archived_raw_pair", script)
        command = [sys.executable, "-B", str(BASE / script)]
        run = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
        assert run.returncode == 0, (script, run.returncode, run.stderr.decode())
        assert not run.stderr, (script, "unexpected_stderr", run.stderr.decode())
        assert run.stdout == expected, ("live_raw_compare", script)
        replays.append({"script": script, "exit_code": run.returncode,
                        "bytes": len(run.stdout), "sha256": digest(run.stdout),
                        "raw_byte_equal_to_canonical_and_replay": True,
                        "stderr_bytes": len(run.stderr)})
    print(json.dumps({"status": "PASS_AUTHOR_PACKAGE_AUDIT_ONLY",
                      "input_pins": len(inputs), "nonself_manifest_entries": len(own),
                      "local_markdown_links": links, "fresh_live_replays": replays,
                      "scope": "partial propositions; admission remains HOLD_PROOF"},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
