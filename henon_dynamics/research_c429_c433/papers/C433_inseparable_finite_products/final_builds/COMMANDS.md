# C433 final-build commands

This is a command record, not a new executable build driver.
All paths below are relative to the literal C433 paper directory
recorded in PREFLIGHT.md, unless a working directory is specified.

Fresh directories were created only after absence and ancestor checks:

    test ! -e final_builds && test ! -L final_builds && mkdir -- final_builds && mkdir -- final_builds/clean01 final_builds/clean01/source final_builds/clean01/source/sections final_builds/clean02 final_builds/clean02/source final_builds/clean02/source/sections

Exact inputs were copied with their layout:

    for build_copy in final_builds/clean01/source final_builds/clean02/source; do cp -p -- main.tex references.bib "$build_copy/" && cp -p -- sections/01_introduction.tex sections/02_statement.tex sections/03_cycles.tex sections/04_extractor.tex sections/05_transfer.tex sections/06_rank.tex sections/07_decision.tex sections/08_conclusion.tex "$build_copy/sections/" || exit 51; done

## Attempt clean01

Working directory: final_builds/clean01/source

    set -o pipefail
    env SOURCE_DATE_EPOCH=1788912000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex 2>&1 | tee ../console.log

## Attempt clean02

Working directory: final_builds/clean02/source

    set -o pipefail
    env SOURCE_DATE_EPOCH=1788912000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex 2>&1 | tee ../console.log

Each latexmk invocation is one authorized clean build attempt, including
its normal internal pdfLaTeX/BibTeX passes. Neither source directory
receives old auxiliary files, an old PDF, or a prior bibliography output.
Actual exits, byte comparisons and post-build commands are recorded
after execution in FINAL_BUILD_REPORT.md.
