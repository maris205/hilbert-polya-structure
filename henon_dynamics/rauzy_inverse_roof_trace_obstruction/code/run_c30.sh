#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
c30_temp_dir="$(mktemp -d)"
trap 'rm -rf -- "$c30_temp_dir"' EXIT
c30_python=(python3 -I -S -B -X "pycache_prefix=$c30_temp_dir/pycache")

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
    "${c30_python[@]}" "$project_dir/code/c30_hash_manifest.py"
fi

"${c30_python[@]}" "$project_dir/code/c30_producer.py" \
    --output "$c30_temp_dir/c30_certificate.json"
"${c30_python[@]}" "$project_dir/code/c30_independent_check.py" \
    --certificate "$c30_temp_dir/c30_certificate.json" \
    --output "$c30_temp_dir/c30_independent_check.json"
"${c30_python[@]}" -m unittest discover -s "$project_dir/code" -p 'test_c30.py' -v

if [[ $refresh_manifest == true ]]; then
    mv "$c30_temp_dir/c30_certificate.json" "$project_dir/results/c30_certificate.json"
    mv "$c30_temp_dir/c30_independent_check.json" "$project_dir/results/c30_independent_check.json"
    "${c30_python[@]}" "$project_dir/code/c30_hash_manifest.py" --write
else
    cmp "$c30_temp_dir/c30_certificate.json" "$project_dir/results/c30_certificate.json"
    cmp "$c30_temp_dir/c30_independent_check.json" "$project_dir/results/c30_independent_check.json"
fi
"${c30_python[@]}" "$project_dir/code/c30_hash_manifest.py"
