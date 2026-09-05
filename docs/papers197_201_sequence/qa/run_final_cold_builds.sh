#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/../../.." && pwd)"
papers=(
  "197-ternary-cyclic-sign-difference"
  "199-first-one-stirling-splice"
  "200-lex-first-alternating-switch"
)

# An explicit subset allows completed Round2 papers to close their own QA
# while replacement seats are still being searched. It is not batch PASS.
if (( $# )); then
  selected=()
  for requested in "$@"; do
    matched=false
    for paper in "${papers[@]}"; do
      if [[ "$requested" == "$paper" ]]; then
        selected+=("$paper")
        matched=true
        break
      fi
    done
    if [[ "$matched" != true ]]; then
      echo "Unknown admitted paper: $requested" >&2
      exit 2
    fi
  done
  papers=("${selected[@]}")
fi

export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
export LC_ALL=C
export FORCE_SOURCE_DATE=1

for paper in "${papers[@]}"; do
  paper_dir="$repo_root/papers/$paper"
  test -f "$paper_dir/main_round2.pdf"
  qa_dir="$paper_dir/qa_final"
  mkdir -p "$qa_dir"
  for run in 1 2; do
    build_dir="$qa_dir/cold_build_$run"
    if [[ -e "$build_dir" ]]; then
      echo "$paper cold_build_$run already exists; preserving"
      continue
    fi
    stage_dir="$(mktemp -d "$qa_dir/.cold_build_$run.XXXXXX")"
    cp "$paper_dir/main.tex" "$stage_dir/main.tex"
    cp "$paper_dir/references.bib" "$stage_dir/references.bib"
    (
      cd "$stage_dir"
      pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass1.stdout
      bibtex main > bibtex.stdout
      pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass2.stdout
      pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex > pass3.stdout
    )
    cmp -s "$stage_dir/main.pdf" "$paper_dir/main.pdf"
    mv "$stage_dir" "$build_dir"
    echo "$paper cold_build_$run PASS"
  done

  visual_dir="$qa_dir/visual"
  if [[ -e "$visual_dir" ]]; then
    echo "$paper visual directory already exists; preserving"
    continue
  fi
  visual_stage="$(mktemp -d "$qa_dir/.visual.XXXXXX")"
  (cd "$paper_dir" && sha256sum main.pdf) > "$visual_stage/SOURCE_PDF.sha256"
  pdftoppm -v > /dev/null 2> "$visual_stage/RENDERER.txt"
  pdftoppm -png -r 180 "$paper_dir/main.pdf" "$visual_stage/page" >/dev/null
  mv "$visual_stage" "$visual_dir"
done
