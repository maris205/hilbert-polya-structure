"""Write the safe-only preflight exactly once."""

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "code"))

from candidate_v1.bootstrap.canonical import write_json_exclusive
from candidate_v1.bootstrap.constants import PREFLIGHT_RELATIVE
from candidate_v1.bootstrap.preflight import collect_preflight


def main():
    if len(sys.argv) != 1:
        raise RuntimeError("safe preflight takes no arguments")
    record = collect_preflight(PROJECT_ROOT)
    write_json_exclusive(PROJECT_ROOT / PREFLIGHT_RELATIVE, record)


if __name__ == "__main__":
    main()

