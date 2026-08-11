#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
c29_temp_dir="$(mktemp -d)"
trap 'rm -rf -- "$c29_temp_dir"' EXIT
c29_python=(python3 -I -S -B -X "pycache_prefix=$c29_temp_dir/pycache")

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
    "${c29_python[@]}" "$project_dir/code/c29_hash_manifest.py"
fi

"${c29_python[@]}" "$project_dir/code/c29_producer.py" \
    --output "$c29_temp_dir/c29_certificate.json"
"${c29_python[@]}" "$project_dir/code/c29_independent_check.py" \
    --certificate "$c29_temp_dir/c29_certificate.json" \
    --output "$c29_temp_dir/c29_independent_check.json"
"${c29_python[@]}" -m unittest discover -s "$project_dir/code" -p 'test_c29.py' -v

if [[ $refresh_manifest == true ]]; then
    mv "$c29_temp_dir/c29_certificate.json" "$project_dir/results/c29_certificate.json"
    mv "$c29_temp_dir/c29_independent_check.json" "$project_dir/results/c29_independent_check.json"
    "${c29_python[@]}" "$project_dir/code/c29_hash_manifest.py" --write
else
    cmp "$c29_temp_dir/c29_certificate.json" "$project_dir/results/c29_certificate.json"
    cmp "$c29_temp_dir/c29_independent_check.json" "$project_dir/results/c29_independent_check.json"
fi
"${c29_python[@]}" "$project_dir/code/c29_hash_manifest.py"
