#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
project_root="$(dirname "$script_dir")"
workspace_root="$(dirname "$project_root")"
export PYTHONPATH="$script_dir"
export PYTHONHASHSEED=0
export SOURCE_DATE_EPOCH=1785888000
export FORCE_SOURCE_DATE=1
export TZ=UTC
cd "$workspace_root"

python "$script_dir/generate_catalog.py" --max-period 8 --parameter 6 --dps 80 --label development
python "$script_dir/generate_catalog.py" --max-period 12 --parameter 6 --dps 80 --label validation
python "$script_dir/generate_catalog.py" --max-period 16 --parameter 6 --dps 80 --label sealed_test
python "$script_dir/generate_catalog.py" --max-period 20 --parameter 6 --dps 80 --label robustness
python "$script_dir/generate_catalog.py" --max-period 16 --parameter 5.9 --dps 80 --label neighbor_a5p9
python "$script_dir/generate_catalog.py" --max-period 16 --parameter 6.1 --dps 80 --label neighbor_a6p1

python "$script_dir/analyze_roots.py" \
  --catalog "$project_root/results/catalog_development.json" \
  --label development --cutoffs 7 8
python "$script_dir/analyze_roots.py" \
  --catalog "$project_root/results/catalog_validation.json" \
  --label validation --cutoffs 7 8 10 12
python "$script_dir/analyze_roots.py" \
  --catalog "$project_root/results/catalog_sealed_test.json" \
  --label sealed_test --cutoffs 7 8 10 12 14 16
python "$script_dir/analyze_roots.py" \
  --catalog "$project_root/results/catalog_robustness.json" \
  --label robustness --cutoffs 7 8 10 12 14 16 18 20

python "$script_dir/run_controls.py" \
  --catalog "$project_root/results/catalog_robustness.json" \
  --root-results "$project_root/results/roots_robustness.json" \
  --neighbor-catalogs \
    "$project_root/results/catalog_neighbor_a5p9.json" \
    "$project_root/results/catalog_neighbor_a6p1.json"

python "$script_dir/summarize_results.py"
python "$script_dir/make_figure1.py"
python "$script_dir/check_results.py"
python "$script_dir/make_paper_includes.py"
pytest -q "$script_dir/tests"

cd "$project_root/paper"
if command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
else
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  bibtex main
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
fi

cd "$workspace_root"
python "$script_dir/build_manifest.py"
