#!/bin/bash
set -euo pipefail
umask 077
[[ "$#" == 2 && "$1" == "--execute-under-separate-root-grant" ]] || exit 78
case "$2" in terminal01) slot=1;; terminal02) slot=2;; *) exit 78;; esac
ROOT=/root/autodl-tmp/symbolic_dynamics
PREP=$ROOT/docs/papers211_215_sequence/qa/p214_terminal_preparation01
SRC=$ROOT/papers/214-nilpotent-bilinear-clock/frozen_round2
RUNTIME=$ROOT/docs/papers211_215_sequence/qa/p214_a_build_binding02/RUNTIME_INPUTS.sha256
OUT=$ROOT/docs/papers211_215_sequence/qa/p214_terminal_run0$slot
COLD=$OUT/source_only
[[ ! -e "$OUT" && ! -L "$OUT" ]]
mkdir -- "$OUT" "$OUT/raw" "$OUT/pass_artifacts" "$OUT/pages" "$COLD" "$COLD/sections"
exec 3>&1
set -C
exec > "$OUT/controller.stdout.raw" 2> "$OUT/controller.stderr.raw"
finish(){ rc=$?; trap - EXIT; printf '%s\n' "$rc" > "$OUT/controller.exit"; printf 'P214_TERMINAL_%s_EXIT=%s\n' "$slot" "$rc" >&3; exit "$rc"; }
trap finish EXIT
SOURCES=(main.tex math_commands.tex references.bib sections/0_abstract.tex sections/1_setup.tex sections/2_clock.tex sections/3_fibres.tex sections/4_controls.tex sections/5_scope.tex)
PRODUCTS=(main.aux main.bbl main.blg main.log main.fls main.out main.toc main.pdf)
cp --no-clobber -- "$PREP/SOURCE_EXPECTED.sha256" "$OUT/SOURCE_EXPECTED.sha256"
cp --no-clobber -- "$PREP/EVIDENCE_INPUTS.sha256" "$OUT/EVIDENCE_INPUTS.sha256"
cp --no-clobber -- "$RUNTIME" "$OUT/RUNTIME_EXPECTED.sha256"
sha256sum -- "$PREP/BUILD_REQUEST.sh" "$PREP/SOURCE_EXPECTED.sha256" "$PREP/EVIDENCE_INPUTS.sha256" "$RUNTIME" > "$OUT/REQUEST_AND_BINDING.sha256"
sha256sum -c --strict "$OUT/RUNTIME_EXPECTED.sha256" > "$OUT/runtime.before.stdout" 2> "$OUT/runtime.before.stderr"
(cd "$ROOT" && sha256sum -c --strict "$OUT/EVIDENCE_INPUTS.sha256") > "$OUT/evidence.before.stdout" 2> "$OUT/evidence.before.stderr"
(cd "$SRC" && sha256sum -c --strict "$OUT/SOURCE_EXPECTED.sha256") > "$OUT/source.before.stdout" 2> "$OUT/source.before.stderr"
for name in "${SOURCES[@]}"; do cp --no-clobber -- "$SRC/$name" "$COLD/$name"; cmp -- "$SRC/$name" "$COLD/$name"; done
cd "$COLD"
sha256sum -c --strict "$OUT/SOURCE_EXPECTED.sha256" > "$OUT/cold_source.initial.stdout" 2> "$OUT/cold_source.initial.stderr"
shopt -s dotglob nullglob; roots=(*); sections=(sections/*); shopt -u dotglob nullglob
[[ "$(pwd -P)" == "$COLD" && ${#roots[@]} == 4 && ${#sections[@]} == 6 ]]
printf 'physical_cwd=%s\nroot_members=%s\nsection_members=%s\n' "$(pwd -P)" "${#roots[@]}" "${#sections[@]}" > "$OUT/COLD_CWD.actual.txt"
for name in "${PRODUCTS[@]}"; do [[ ! -e "$name" && ! -L "$name" ]]; done
snapshot(){ dest=$OUT/pass_artifacts/$1; mkdir -- "$dest"; for name in "${PRODUCTS[@]}"; do if [[ -f "$name" && ! -L "$name" ]]; then cp --no-clobber -- "$name" "$dest/$name"; sha256sum -- "$name" >> "$dest/PRESENT.sha256"; else printf '%s\n' "$name" >> "$dest/ABSENT.txt"; fi; done; }
step=0
run(){ label=$1; seconds=$2; shift 2; printf 'cwd=%s\nargv=' "$COLD" > "$OUT/raw/$label.request.txt"; printf '%q ' /usr/bin/timeout --signal=TERM --kill-after=10s "${seconds}s" "$@" >> "$OUT/raw/$label.request.txt"; printf '\n' >> "$OUT/raw/$label.request.txt"; set +e; /usr/bin/timeout --signal=TERM --kill-after=10s "${seconds}s" "$@" < /dev/null > "$OUT/raw/$label.stdout.raw" 2> "$OUT/raw/$label.stderr.raw"; step=$?; set -e; printf '%s\n' "$step" > "$OUT/raw/$label.supervisor_exit"; }
buildpass(){ label=$1; shift; snapshot "$label.before"; run "$label" 600 "$@"; snapshot "$label.after"; sha256sum -c --strict "$OUT/SOURCE_EXPECTED.sha256" > "$OUT/raw/$label.sources.stdout" 2> "$OUT/raw/$label.sources.stderr"; [[ "$step" == 0 ]]; }
TEX=(/usr/bin/pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex)
buildpass pass1 "${TEX[@]}"
buildpass bibtex /usr/bin/bibtex main
buildpass pass2 "${TEX[@]}"
buildpass pass3 "${TEX[@]}"
[[ -s main.pdf ]]
run pdfinfo 180 /usr/bin/pdfinfo main.pdf; [[ "$step" == 0 ]]
run pdffonts 180 /usr/bin/pdffonts main.pdf; [[ "$step" == 0 ]]
run pdftotext 180 /usr/bin/pdftotext -layout main.pdf -; [[ "$step" == 0 ]]
run final_diagnostics 180 /usr/bin/awk '/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!/ {print FILENAME ":" FNR ":" $0}' main.log main.blg; [[ "$step" == 0 ]]
pages=$(/usr/bin/awk '/^Pages:[[:space:]]/ {print $2}' "$OUT/raw/pdfinfo.stdout.raw"); [[ "$pages" =~ ^[1-9][0-9]*$ ]]; printf '%s\n' "$pages" > "$OUT/PAGE_COUNT.txt"
for ((page=1;page<=pages;page++)); do printf -v label 'page-%04d' "$page"; run "$label" 180 /usr/bin/pdftoppm -f "$page" -l "$page" -singlefile -png -r 150 main.pdf "$OUT/pages/$label"; [[ "$step" == 0 && -s "$OUT/pages/$label.png" ]]; sha256sum -- "$OUT/pages/$label.png" >> "$OUT/PAGES.sha256"; done
sha256sum -c --strict "$OUT/RUNTIME_EXPECTED.sha256" > "$OUT/runtime.after.stdout" 2> "$OUT/runtime.after.stderr"
(cd "$ROOT" && sha256sum -c --strict "$OUT/EVIDENCE_INPUTS.sha256") > "$OUT/evidence.after.stdout" 2> "$OUT/evidence.after.stderr"
(cd "$SRC" && sha256sum -c --strict "$OUT/SOURCE_EXPECTED.sha256") > "$OUT/source.after.stdout" 2> "$OUT/source.after.stderr"
sha256sum -c --strict "$OUT/SOURCE_EXPECTED.sha256" > "$OUT/cold_source.final.stdout" 2> "$OUT/cold_source.final.stderr"
sha256sum -- main.pdf main.log main.fls main.aux main.bbl main.blg > "$OUT/FINAL_PRODUCTS.sha256"
printf '%s\n' CAPTURED_PENDING_ARTIFACT_AND_PAGE_RECEPTION > "$OUT/STATUS.txt"
