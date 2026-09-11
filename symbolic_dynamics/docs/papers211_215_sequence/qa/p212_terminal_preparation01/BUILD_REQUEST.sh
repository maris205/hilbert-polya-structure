#!/bin/bash
# ENABLED only by one exact separately recorded terminal grant.
set -euo pipefail
umask 077
[[ "$#" == 2 && "$1" == "--execute-under-separate-root-grant" ]] || exit 78
case "$2" in terminal01) p212_slot=1;; terminal02) p212_slot=2;; *) exit 78;; esac
P212_ROOT=/root/autodl-tmp/symbolic_dynamics
P212_PREP=$P212_ROOT/docs/papers211_215_sequence/qa/p212_terminal_preparation01
P212_SRC=$P212_ROOT/papers/212-closed-pointer-orbits/frozen_round2
P212_RUNTIME=$P212_ROOT/docs/papers211_215_sequence/qa/p212_b_build_binding01/RUNTIME_INPUTS.sha256
P212_PARENT=$P212_ROOT/papers/212-closed-pointer-orbits/qa_final
P212_OUT=$P212_PARENT/cold_build_$p212_slot
P212_COLD=$P212_OUT/source_only
[[ -f "$P212_PREP/BUILD_SOURCES.sha256" && ! -L "$P212_PREP/BUILD_SOURCES.sha256" ]]
[[ -f "$P212_RUNTIME" && ! -L "$P212_RUNTIME" ]]
if [[ "$p212_slot" == 1 ]]; then mkdir -- "$P212_PARENT"; else [[ -d "$P212_PARENT" && ! -L "$P212_PARENT" ]]; fi
mkdir -- "$P212_OUT" "$P212_OUT/raw" "$P212_OUT/pass_artifacts" "$P212_OUT/pages" "$P212_COLD" "$P212_COLD/sections"
exec 3>&1 4>&2
set -C
exec > "$P212_OUT/controller.stdout.raw" 2> "$P212_OUT/controller.stderr.raw"
p212_finish(){ local rc=$?; trap - EXIT; printf '%s\n' "$rc" > "$P212_OUT/controller.exit"; printf 'P212_TERMINAL_%s_EXIT=%s\n' "$p212_slot" "$rc" >&3; exit "$rc"; }
trap p212_finish EXIT
P212_SOURCES=(main.tex math_commands.tex references.bib sections/01_setup.tex sections/02_returns.tex sections/03_period_set.tex sections/04_census.tex sections/05_scope.tex)
P212_PRODUCTS=(main.aux main.bbl main.blg main.log main.fls main.out main.toc main.pdf)
cp --no-clobber -- "$P212_PREP/BUILD_SOURCES.sha256" "$P212_OUT/SOURCE_EXPECTED.sha256"
cp --no-clobber -- "$P212_RUNTIME" "$P212_OUT/RUNTIME_EXPECTED.sha256"
sha256sum -- "$P212_PREP/BUILD_REQUEST.sh" "$P212_PREP/BUILD_SOURCES.sha256" "$P212_RUNTIME" > "$P212_OUT/REQUEST_AND_BINDING.sha256"
sha256sum -c --strict "$P212_OUT/RUNTIME_EXPECTED.sha256" > "$P212_OUT/runtime.before.stdout" 2> "$P212_OUT/runtime.before.stderr"
(cd "$P212_SRC" && sha256sum -c --strict "$P212_OUT/SOURCE_EXPECTED.sha256") > "$P212_OUT/live_source.before.stdout" 2> "$P212_OUT/live_source.before.stderr"
for f in "${P212_SOURCES[@]}"; do [[ -f "$P212_SRC/$f" && ! -L "$P212_SRC/$f" ]]; cp --no-clobber -- "$P212_SRC/$f" "$P212_COLD/$f"; cmp -- "$P212_SRC/$f" "$P212_COLD/$f"; done
cd "$P212_COLD"
sha256sum -c --strict "$P212_OUT/SOURCE_EXPECTED.sha256" > "$P212_OUT/cold_source.initial.stdout" 2> "$P212_OUT/cold_source.initial.stderr"
[[ "$(pwd -P)" == "$P212_COLD" ]]
shopt -s dotglob nullglob; a=(*); b=(sections/*); shopt -u dotglob nullglob
[[ ${#a[@]} == 4 && ${#b[@]} == 5 && ! -e texmf && ! -L texmf && ! -e .texlive2021 && ! -L .texlive2021 ]]
printf 'physical_cwd=%s\nroot_members=%s\nsection_members=%s\n' "$(pwd -P)" "${#a[@]}" "${#b[@]}" > "$P212_OUT/COLD_CWD.actual.txt"
for f in "${P212_PRODUCTS[@]}"; do [[ ! -e "$f" && ! -L "$f" ]]; done
p212_snapshot(){ local d=$P212_OUT/pass_artifacts/$1; mkdir -- "$d"; for f in "${P212_PRODUCTS[@]}"; do if [[ -f "$f" && ! -L "$f" ]]; then cp --no-clobber -- "$f" "$d/$f"; sha256sum -- "$f" >> "$d/PRESENT.sha256"; else printf '%s\n' "$f" >> "$d/ABSENT.txt"; fi; done; }
P212_STEP=0
p212_run(){ local label=$1 seconds=$2; shift 2; printf 'cwd=%s\nargv=' "$P212_COLD" > "$P212_OUT/raw/$label.request.txt"; printf '%q ' /usr/bin/timeout --signal=TERM --kill-after=10s "${seconds}s" "$@" >> "$P212_OUT/raw/$label.request.txt"; printf '\n' >> "$P212_OUT/raw/$label.request.txt"; set +e; /usr/bin/timeout --signal=TERM --kill-after=10s "${seconds}s" "$@" < /dev/null > "$P212_OUT/raw/$label.stdout.raw" 2> "$P212_OUT/raw/$label.stderr.raw"; P212_STEP=$?; set -e; printf '%s\n' "$P212_STEP" > "$P212_OUT/raw/$label.supervisor_exit"; }
p212_pass(){ local label=$1; shift; p212_snapshot "$label.before"; p212_run "$label" 600 "$@"; p212_snapshot "$label.after"; sha256sum -c --strict "$P212_OUT/SOURCE_EXPECTED.sha256" > "$P212_OUT/raw/$label.sources.stdout" 2> "$P212_OUT/raw/$label.sources.stderr"; [[ "$P212_STEP" == 0 ]]; }
P212_TEX=(/usr/bin/pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex)
p212_pass pass1 "${P212_TEX[@]}"
p212_pass bibtex /usr/bin/bibtex main
p212_pass pass2 "${P212_TEX[@]}"
p212_pass pass3 "${P212_TEX[@]}"
[[ -s main.pdf ]]
p212_run pdfinfo 180 /usr/bin/pdfinfo main.pdf; [[ "$P212_STEP" == 0 ]]
p212_run pdffonts 180 /usr/bin/pdffonts main.pdf; [[ "$P212_STEP" == 0 ]]
p212_run pdftotext 180 /usr/bin/pdftotext -layout main.pdf -; [[ "$P212_STEP" == 0 ]]
p212_run final_diagnostics 180 /usr/bin/awk '/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!/ {print FILENAME ":" FNR ":" $0}' main.log main.blg; [[ "$P212_STEP" == 0 ]]
P212_PAGES=$(/usr/bin/awk '/^Pages:[[:space:]]/ {print $2}' "$P212_OUT/raw/pdfinfo.stdout.raw"); [[ "$P212_PAGES" =~ ^[1-9][0-9]*$ ]]; printf '%s\n' "$P212_PAGES" > "$P212_OUT/PAGE_COUNT.txt"
for ((i=1;i<=P212_PAGES;i++)); do printf -v label 'page-%04d' "$i"; p212_run "$label" 180 /usr/bin/pdftoppm -f "$i" -l "$i" -singlefile -png -r 150 main.pdf "$P212_OUT/pages/$label"; [[ "$P212_STEP" == 0 && -s "$P212_OUT/pages/$label.png" ]]; sha256sum -- "$P212_OUT/pages/$label.png" >> "$P212_OUT/PAGES.sha256"; done
sha256sum -c --strict "$P212_OUT/RUNTIME_EXPECTED.sha256" > "$P212_OUT/runtime.after.stdout" 2> "$P212_OUT/runtime.after.stderr"
(cd "$P212_SRC" && sha256sum -c --strict "$P212_OUT/SOURCE_EXPECTED.sha256") > "$P212_OUT/live_source.after.stdout" 2> "$P212_OUT/live_source.after.stderr"
sha256sum -c --strict "$P212_OUT/SOURCE_EXPECTED.sha256" > "$P212_OUT/cold_source.final.stdout" 2> "$P212_OUT/cold_source.final.stderr"
sha256sum -- main.pdf main.log main.fls main.aux main.bbl main.blg > "$P212_OUT/FINAL_PRODUCTS.sha256"
printf '%s\n' 'CAPTURED_PENDING_COMPLETE_ARTIFACT_AND_ACTUAL_PAGE_RECEPTION' > "$P212_OUT/STATUS.txt"
