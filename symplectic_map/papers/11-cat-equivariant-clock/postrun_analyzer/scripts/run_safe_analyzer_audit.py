from __future__ import annotations

import json
from pathlib import Path

from equivariant_clock_postrun.audit import collect_analyzer_audit


if __name__ == "__main__":
    project_root = Path(__file__).absolute().parents[2]
    print(json.dumps(collect_analyzer_audit(project_root), indent=2, sort_keys=True))
