#!/usr/bin/env bash
set -euo pipefail

paper_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$paper_root/code/cohomological_owner_controls.py" \
  --output-dir "$paper_root/results" \
  --max-degree 24 \
  --max-power 24 >/dev/null
PYTHONPATH="$paper_root/code" python3 \
  "$paper_root/code/test_cohomological_owner_controls.py"
