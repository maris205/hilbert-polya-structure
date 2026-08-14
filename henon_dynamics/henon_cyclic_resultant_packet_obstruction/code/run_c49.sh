#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
python -B "$here/code/c49_cyclic_packets.py" --max-index 12 --output "$here/results/c49_certificate.json"
python -B "$here/code/test_c49.py"
python -B "$here/code/generate_table.py"
python -B "$here/code/c49_cyclic_packets.py" --check
