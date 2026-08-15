from __future__ import annotations

from pathlib import Path

from equivariant_clock_postrun.manifest import write_manifest


if __name__ == "__main__":
    project_root = Path(__file__).absolute().parents[2]
    print(write_manifest(project_root))
