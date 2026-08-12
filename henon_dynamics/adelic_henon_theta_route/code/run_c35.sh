#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
c35_temp_dir="$(mktemp -d)"
trap 'rm -rf -- "$c35_temp_dir"' EXIT
c35_python=(python3 -I -B -X "pycache_prefix=$c35_temp_dir/pycache")

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
    "${c35_python[@]}" "$project_dir/code/c35_hash_manifest.py"
fi

"${c35_python[@]}" "$project_dir/code/c35_adelic_theta_producer.py" \
    --output "$c35_temp_dir/c35_certificate.json"
"${c35_python[@]}" "$project_dir/code/c35_adelic_theta_checker.py" \
    "$c35_temp_dir/c35_certificate.json" \
    --output "$c35_temp_dir/c35_independent_check.json"

"${c35_python[@]}" -m unittest discover \
    -s "$project_dir/code" -p 'test_c35.py' -v

if [[ $refresh_manifest == true ]]; then
    mv "$c35_temp_dir/c35_certificate.json" \
        "$project_dir/results/c35_certificate.json"
    mv "$c35_temp_dir/c35_independent_check.json" \
        "$project_dir/results/c35_independent_check.json"
    "${c35_python[@]}" "$project_dir/code/c35_hash_manifest.py" --write
else
    cmp "$c35_temp_dir/c35_certificate.json" \
        "$project_dir/results/c35_certificate.json"
    cmp "$c35_temp_dir/c35_independent_check.json" \
        "$project_dir/results/c35_independent_check.json"
fi

"${c35_python[@]}" "$project_dir/code/c35_hash_manifest.py"
