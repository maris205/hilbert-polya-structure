#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmp_dir="$(mktemp -d)"
trap 'rm -rf -- "$tmp_dir"' EXIT

python "$project_dir/code/c37_homogeneous_index_producer.py" \
  --output "$tmp_dir/c37_certificate.json"
cmp "$tmp_dir/c37_certificate.json" "$project_dir/results/c37_certificate.json"

python "$project_dir/code/c37_homogeneous_index_checker.py" \
  "$project_dir/results/c37_certificate.json" \
  --output "$tmp_dir/c37_independent_check.json"
cmp "$tmp_dir/c37_independent_check.json" \
  "$project_dir/results/c37_independent_check.json"

python -m unittest discover -s "$project_dir/code" -p 'test_c37.py' -v

if [[ "${1:-}" == "--refresh-manifest" ]]; then
  python "$project_dir/code/c37_hash_manifest.py" --write
elif [[ $# -ne 0 ]]; then
  echo "usage: $0 [--refresh-manifest]" >&2
  exit 2
fi
python "$project_dir/code/c37_hash_manifest.py"
