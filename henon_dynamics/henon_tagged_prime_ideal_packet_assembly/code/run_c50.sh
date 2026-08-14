#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
python -B "$here/code/c50_tagged_packets.py" --min-index 3 --max-index 20 --output "$here/results/c50_certificate.json"
python -B "$here/code/test_c50.py"
python -B "$here/code/generate_table.py"
python -B "$here/code/c50_tagged_packets.py" --check
