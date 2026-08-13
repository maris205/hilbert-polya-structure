#!/usr/bin/env python3
"""Hash the frozen source and result artifacts after an official run."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from action_audit.manifest import collect_manifest_inputs, validate_required_artifacts


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    arguments = parser.parse_args()
    root = arguments.project_root.resolve()
    validation = validate_required_artifacts(root)
    if not validation["pass"]:
        raise RuntimeError(
            "required result artifacts are missing or semantically invalid: "
            + json.dumps(validation, sort_keys=True)
        )
    selected = collect_manifest_inputs(root)
    output = root / "results" / "final_result_manifest.json"
    payload = {
        "algorithm": "sha256",
        "required_artifact_validation": validation,
        "files": {
            str(path.relative_to(root)): sha256(path)
            for path in sorted(set(selected))
        },
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
