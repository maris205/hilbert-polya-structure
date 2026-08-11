#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
c31_temp_dir="$(mktemp -d)"
trap 'rm -rf -- "$c31_temp_dir"' EXIT
c31_python=(python3 -I -S -B -X "pycache_prefix=$c31_temp_dir/pycache")

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
    "${c31_python[@]}" "$project_dir/code/c31_hash_manifest.py"
fi

"${c31_python[@]}" "$project_dir/code/c31_producer.py" \
    --output "$c31_temp_dir/c31_certificate.json"
"${c31_python[@]}" "$project_dir/code/c31_independent_check.py" \
    --certificate "$c31_temp_dir/c31_certificate.json" \
    --output "$c31_temp_dir/c31_independent_check.json"
C31_TEST_CERTIFICATE="$c31_temp_dir/c31_certificate.json" \
    "${c31_python[@]}" -m unittest discover -s "$project_dir/code" -p 'test_c31.py' -v

if [[ $refresh_manifest == true ]]; then
    mv "$c31_temp_dir/c31_certificate.json" "$project_dir/results/c31_certificate.json"
    mv "$c31_temp_dir/c31_independent_check.json" "$project_dir/results/c31_independent_check.json"
    "${c31_python[@]}" "$project_dir/code/c31_hash_manifest.py" --write
else
    cmp "$c31_temp_dir/c31_certificate.json" "$project_dir/results/c31_certificate.json"
    cmp "$c31_temp_dir/c31_independent_check.json" "$project_dir/results/c31_independent_check.json"
fi
"${c31_python[@]}" "$project_dir/code/c31_hash_manifest.py"
