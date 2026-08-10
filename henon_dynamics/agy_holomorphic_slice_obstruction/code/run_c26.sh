#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python "$project_dir/code/c26_producer.py" --sentinel-max-length 20
python "$project_dir/code/c26_independent_check.py"
python -m unittest discover -s "$project_dir/code" -p 'test_c26.py' -v
python "$project_dir/code/c26_hash_manifest.py"
(cd "$project_dir" && sha256sum -c results/ARTIFACT_HASHES.sha256)
