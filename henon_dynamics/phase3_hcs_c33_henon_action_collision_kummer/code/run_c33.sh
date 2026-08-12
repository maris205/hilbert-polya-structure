#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
c33_temp_dir="$(mktemp -d)"
trap 'rm -rf -- "$c33_temp_dir"' EXIT
c33_python=(python3 -I -B -X "pycache_prefix=$c33_temp_dir/pycache")

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
    "${c33_python[@]}" "$project_dir/code/c33_hash_manifest.py"
fi

"${c33_python[@]}" "$project_dir/code/c33_kummer_producer.py" \
    --output "$c33_temp_dir/c33_kummer_certificate.json"
"${c33_python[@]}" "$project_dir/code/c33_kummer_checker.py" \
    --certificate "$c33_temp_dir/c33_kummer_certificate.json" \
    --output "$c33_temp_dir/c33_kummer_independent_check.json"

C33_TEST_CERTIFICATE="$c33_temp_dir/c33_kummer_certificate.json" \
    "${c33_python[@]}" -m unittest discover \
    -s "$project_dir/code" -p 'test_c33.py' -v

if [[ $refresh_manifest == true ]]; then
    mv "$c33_temp_dir/c33_kummer_certificate.json" \
        "$project_dir/results/c33_kummer_certificate.json"
    mv "$c33_temp_dir/c33_kummer_independent_check.json" \
        "$project_dir/results/c33_kummer_independent_check.json"
    "${c33_python[@]}" "$project_dir/code/c33_hash_manifest.py" --write
else
    cmp "$c33_temp_dir/c33_kummer_certificate.json" \
        "$project_dir/results/c33_kummer_certificate.json"
    cmp "$c33_temp_dir/c33_kummer_independent_check.json" \
        "$project_dir/results/c33_kummer_independent_check.json"
fi

"${c33_python[@]}" "$project_dir/code/c33_hash_manifest.py"
