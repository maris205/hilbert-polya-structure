from __future__ import annotations

from pathlib import Path

from equivariant_clock_postrun.protocol import analyzer_tree_sha256


if __name__ == "__main__":
    project_root = Path(__file__).absolute().parents[2]
    print(analyzer_tree_sha256(project_root))
