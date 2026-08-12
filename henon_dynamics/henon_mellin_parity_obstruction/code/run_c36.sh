#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
c36_temp_dir="$(mktemp -d)"
trap 'find "$c36_temp_dir" -type f -delete; find "$c36_temp_dir" -depth -type d -empty -delete' EXIT
c36_python=(python3 -I -B -X "pycache_prefix=$c36_temp_dir/pycache")

refresh_manifest=false
if [[ $# -gt 1 ]]; then
    echo "usage: $0 [--refresh-manifest]" >&2
    exit 2
fi
if [[ $# -eq 1 ]]; then
    if [[ $1 != "--refresh-manifest" ]]; then
        echo "usage: $0 [--refresh-manifest]" >&2
        exit 2
    fi
    refresh_manifest=true
fi

if [[ $refresh_manifest == false ]]; then
    "${c36_python[@]}" "$project_dir/code/c36_hash_manifest.py"
fi

"${c36_python[@]}" "$project_dir/code/c36_mellin_producer.py" \
    --output "$c36_temp_dir/c36_certificate.json"
"${c36_python[@]}" "$project_dir/code/c36_mellin_checker.py" \
    "$c36_temp_dir/c36_certificate.json" \
    --output "$c36_temp_dir/c36_independent_check.json"

"${c36_python[@]}" -m unittest discover \
    -s "$project_dir/code" -p 'test_c36.py' -v

if [[ $refresh_manifest == true ]]; then
    mv "$c36_temp_dir/c36_certificate.json" \
        "$project_dir/results/c36_certificate.json"
    mv "$c36_temp_dir/c36_independent_check.json" \
        "$project_dir/results/c36_independent_check.json"
    "${c36_python[@]}" "$project_dir/code/c36_hash_manifest.py" --write
else
    cmp "$c36_temp_dir/c36_certificate.json" \
        "$project_dir/results/c36_certificate.json"
    cmp "$c36_temp_dir/c36_independent_check.json" \
        "$project_dir/results/c36_independent_check.json"
fi

"${c36_python[@]}" "$project_dir/code/c36_hash_manifest.py"
