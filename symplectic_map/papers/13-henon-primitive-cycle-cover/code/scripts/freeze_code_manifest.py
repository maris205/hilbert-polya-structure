"""Freeze the code/JUnit/preflight closure exactly once."""

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "code"))

from candidate_v1.bootstrap.canonical import write_json_exclusive
from candidate_v1.bootstrap.constants import CODE_MANIFEST_RELATIVE
from candidate_v1.bootstrap.manifest import build_code_manifest


def main():
    if len(sys.argv) != 1:
        raise RuntimeError("manifest freeze takes no arguments")
    manifest = build_code_manifest(PROJECT_ROOT)
    write_json_exclusive(PROJECT_ROOT / CODE_MANIFEST_RELATIVE, manifest)


if __name__ == "__main__":
    main()

