#!/usr/bin/env bash
# One complete frozen-source build in one absent root; no retries or cleaning.
set -euo pipefail
project=/root/autodl-tmp/symplectic_map/papers/31-qpi-sharp-phase-mixing
source_root="$project/paper/v2"
manifest="$project/notes/SOURCE_V2_20260913.sha256"
case "${1-}" in
  r0|r1) build_root="$project/build/natural-20260913-$1" ;;
  *) echo 'Usage: bash scripts/build_natural_v1.sh r0|r1' >&2; exit 64 ;;
esac
if [[ -e "$build_root" ]]; then
  echo "Refusing existing build root: $build_root" >&2
  exit 73
fi
cd "$source_root"
sha256sum --strict -c "$manifest"
export SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C
export TEXINPUTS=.: BIBINPUTS=.: BSTINPUTS=.:
mkdir -p "$build_root/work" "$build_root/logs"
cp -a "$source_root/." "$build_root/work/"
cp "$manifest" "$build_root/source.sha256"
cd "$build_root/work"
sha256sum --strict -c ../source.sha256 > ../logs/copied-source-check.txt
printf '%s\n' 'SOURCE_DATE_EPOCH=0' 'FORCE_SOURCE_DATE=1' 'TZ=UTC' \
  'LC_ALL=C' 'TEXINPUTS=.:' 'BIBINPUTS=.:' 'BSTINPUTS=.:' > ../logs/environment.txt
run_pass() {
  local pass_name="$1" pass_status ext
  shift
  printf '%q ' "$@" > "../logs/$pass_name.command.txt"
  printf '\n' >> "../logs/$pass_name.command.txt"
  set +e
  "$@" > "../logs/$pass_name.stdout.txt" 2>&1
  pass_status=$?
  set -e
  printf '%s\n' "$pass_status" > "../logs/$pass_name.exit.txt"
  for ext in log aux out fls blg bbl pdf; do
    if [[ -f "main.$ext" ]]; then
      cp "main.$ext" "../logs/$pass_name.main.$ext"
    fi
  done
  if (( pass_status != 0 )); then
    echo "$pass_name failed with status $pass_status; all outputs retained." >&2
    exit "$pass_status"
  fi
}
tex_command=(/usr/bin/pdflatex
  -fmt=/var/lib/texmf/web2c/pdftex/pdflatex.fmt
  -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex)
run_pass 01-pdflatex "${tex_command[@]}"
run_pass 02-bibtex /usr/bin/bibtex main
run_pass 03-pdflatex "${tex_command[@]}"
run_pass 04-pdflatex "${tex_command[@]}"
sha256sum --strict -c ../source.sha256 > ../logs/final-source-check.txt
awk '/^INPUT \// { print substr($0,7) }' main.fls | sort -u > ../logs/absolute-inputs.txt
while IFS= read -r dependency; do
  sha256sum "$dependency"
done < ../logs/absolute-inputs.txt > ../logs/absolute-inputs.sha256
/usr/bin/pdfinfo main.pdf > ../logs/pdfinfo.txt
/usr/bin/pdffonts main.pdf > ../logs/pdffonts.txt
/usr/bin/pdftotext -layout main.pdf ../logs/main-layout.txt
sha256sum main.pdf > ../logs/pdf.sha256
echo 'Four-pass build finished. Page window, layout, determinism and acceptance remain unassessed.'
