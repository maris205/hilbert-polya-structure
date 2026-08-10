#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python "$project_dir/code/c25_producer.py"
python "$project_dir/code/c25_independent_check.py"
python -m unittest discover -s "$project_dir/code" -p 'test_c25.py' -v
python "$project_dir/code/c25_hash_manifest.py"
(cd "$project_dir" && sha256sum -c results/ARTIFACT_HASHES.sha256)
