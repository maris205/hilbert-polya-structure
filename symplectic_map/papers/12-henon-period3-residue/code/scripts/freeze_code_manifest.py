"""Freeze the exact reviewed-code candidate manifest after clean JUnit/preflight."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 1:
        raise RuntimeError("manifest freeze accepts no arguments")
    sys.dont_write_bytecode = True
    project_root = Path(__file__).absolute().parents[2]
    sys.path.insert(0, str(project_root / "code/candidate_v1"))
    from bootstrap.manifest import build_code_manifest
    from bootstrap.protocol import write_json_exclusive

    manifest = build_code_manifest(project_root)
    write_json_exclusive(project_root / "preexecution/code_manifest.json", manifest)


if __name__ == "__main__":
    main()
