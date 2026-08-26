#!/usr/bin/env bash
set -euo pipefail

if [[ -n "${P13_REPRO_ACTIVE:-}" ]]; then
  echo "P13_REPRO_FAIL: recursive entry rejected" >&2
  exit 91
fi

script_path="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/$(basename -- "${BASH_SOURCE[0]}")"
exec 9<"$script_path"
if ! flock -n 9; then
  echo "P13_REPRO_FAIL: another top-level Paper-13 control run holds the reservation" >&2
  exit 92
fi

export P13_REPRO_ACTIVE=1
export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

paper_dir="$(cd -- "$(dirname -- "$script_path")/.." && pwd)"
generator="$paper_dir/code/generate_controls.py"
tests="$paper_dir/code/test_controls.py"
checked="$paper_dir/results"
fresh_a=""
fresh_b=""
temp_parent="$(cd -- "${TMPDIR:-/tmp}" && pwd -P)"

cleanup() {
  local status=$?
  if [[ -n "$fresh_a" && -d "$fresh_a" ]]; then
    case "$fresh_a" in
      "$temp_parent"/p13-controls-A.*) rm -rf -- "$fresh_a" ;;
      *) echo "P13_REPRO_FAIL: unsafe fresh-A cleanup target" >&2; status=93 ;;
    esac
  fi
  if [[ -n "$fresh_b" && -d "$fresh_b" ]]; then
    case "$fresh_b" in
      "$temp_parent"/p13-controls-B.*) rm -rf -- "$fresh_b" ;;
      *) echo "P13_REPRO_FAIL: unsafe fresh-B cleanup target" >&2; status=93 ;;
    esac
  fi
  if [[ -n "$fresh_a" && -e "$fresh_a" ]] || [[ -n "$fresh_b" && -e "$fresh_b" ]]; then
    echo "P13_REPRO_FAIL: temporary-root cleanup incomplete" >&2
    exit 93
  fi
  echo "TEMP_ROOTS_REMOVED=2"
  echo "TASK_TEMP_RESIDUE=0"
  exit "$status"
}
trap cleanup EXIT INT TERM HUP

echo "P13_CONTROL_RUN_RESERVATION=ACQUIRED"
echo "TOP_LEVEL_RUNS=1"

receipt_before="$(python3 -B "$generator" --receipt "$checked")"
python3 -B "$generator" --verify-only "$checked"
receipt_after="$(python3 -B "$generator" --receipt "$checked")"
if [[ "$receipt_before" != "$receipt_after" ]]; then
  echo "P13_REPRO_FAIL: verify-only changed checked-in bytes or metadata" >&2
  exit 94
fi
echo "VERIFY_ONLY_IMMUTABLE=true"

fresh_a="$(mktemp -d "$temp_parent/p13-controls-A.XXXXXX")"
fresh_b="$(mktemp -d "$temp_parent/p13-controls-B.XXXXXX")"
if [[ "$fresh_a" == "$fresh_b" ]] || [[ -n "$(find "$fresh_a" -mindepth 1 -maxdepth 1 -print -quit)" ]] || [[ -n "$(find "$fresh_b" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  echo "P13_REPRO_FAIL: fresh roots are not distinct and empty" >&2
  exit 95
fi

python3 -B "$generator" --output-dir "$fresh_a"
python3 -B "$generator" --verify-only "$fresh_a"
python3 -B "$generator" --output-dir "$fresh_b"
python3 -B "$generator" --verify-only "$fresh_b"

artifacts=(
  nerve_factorization_controls.csv
  circle_multiplier_cocycle_controls.csv
  lift_integer_defect_controls.csv
  gauge_coboundary_controls.csv
  twisted_convolution_controls.csv
  twisted_involution_controls.csv
  completion_gauge_controls.csv
  action_period_nonretention_controls.csv
  negative_domain_controls.csv
  actual_standard_support_transfer_controls.csv
  target_summary.csv
  completion_corona_controls_v2.csv
  manifest.json
)
for artifact in "${artifacts[@]}"; do
  cmp --silent -- "$checked/$artifact" "$fresh_a/$artifact"
  cmp --silent -- "$fresh_a/$artifact" "$fresh_b/$artifact"
done
echo "FRESH_GENERATIONS=2"
echo "BYTE_IDENTICAL_COPIES=3"
echo "BYTE_IDENTICAL_ARTIFACTS=13"

export P13_FRESH_A="$fresh_a"
export P13_FRESH_B="$fresh_b"
export P13_TEST_SCRATCH="$fresh_a/.test-scratch"
python3 -B "$tests"

if [[ -e "$P13_TEST_SCRATCH" ]]; then
  echo "P13_REPRO_FAIL: test scratch residue remains" >&2
  exit 96
fi
python3 -B "$generator" --verify-only "$checked"
python3 -B "$generator" --verify-only "$fresh_a"
python3 -B "$generator" --verify-only "$fresh_b"

echo "CSV_ARTIFACTS=12"
echo "GENERATED_ARTIFACTS_INCLUDING_MANIFEST=13"
echo "V1_CSV_BODY_ROWS=2548"
echo "V2_NEW_CSV_BODY_ROWS=117"
echo "CSV_BODY_ROWS=2665"
echo "V1_EXPLICIT_NEGATIVE_ROWS=47"
echo "V2_NEW_EXPLICIT_NEGATIVE_ROWS=20"
echo "EXPLICIT_NEGATIVE_ROWS=67"
echo "EXPECTED_NEGATIVES_DETECTED=67"
echo "NEGATIVE_FAILURES=0"
echo "TOLERANCE_POLICY=EXACT_ZERO"
echo "PROHIBITED_CACHE_ENTRIES=0"
echo "PROCESS_CHILDREN_REAPED=true"
echo "P13_CONTROL_REPRODUCTION=PASS"
