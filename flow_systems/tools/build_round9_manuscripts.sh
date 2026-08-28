#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

papers=(
  24-bianchi-holonomy-flow
  25-three-disk-scattering-flow
  26-level11-newform-time-change
  27-congruence-inverse-limit-no-go
  28-bolza-magnetic-flow
)

for paper in "${papers[@]}"; do
  paper_dir="$repo_root/papers/$paper/paper"
  printf '%s\n' "$paper"
  (
    cd "$paper_dir"
    lualatex -interaction=nonstopmode -halt-on-error -jobname=paper manuscript.tex
    bibtex paper
    lualatex -interaction=nonstopmode -halt-on-error -jobname=paper manuscript.tex
    lualatex -interaction=nonstopmode -halt-on-error -jobname=paper manuscript.tex
  )
done

python3 "$repo_root/tools/round9_manuscript_audit.py" --root "$repo_root" --pretty
