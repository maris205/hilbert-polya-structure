#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
canonical_dir="$project_dir/results/round2"
replica_dir="$project_dir/results/reproduction_run2"

python3 "$project_dir/code/round2_reduction_orders.py" generate --output-dir "$canonical_dir"
python3 "$project_dir/code/round2_reduction_orders.py" verify --output-dir "$canonical_dir"
python3 -m unittest discover -s "$project_dir/code" -p 'test_round2_reduction_orders.py' -v

python3 "$project_dir/code/round2_reduction_orders.py" generate --output-dir "$replica_dir"
python3 "$project_dir/code/round2_reduction_orders.py" verify --output-dir "$replica_dir"

for artifact in congruence_reduction_order_ledger.csv round2_metrics.json experiment_receipt.json manifest.json; do
  cmp "$canonical_dir/$artifact" "$replica_dir/$artifact"
done

sha256sum \
  "$canonical_dir/congruence_reduction_order_ledger.csv" \
  "$canonical_dir/round2_metrics.json" \
  "$canonical_dir/experiment_receipt.json" \
  "$canonical_dir/manifest.json"

echo "P27_ROUND2_REPRODUCIBILITY=PASS"
echo "P27_ROUND2_TWO_RUN_BYTE_IDENTITY=4/4"
