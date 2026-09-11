# P199 Round 0 build and replay

Environment: pdfLaTeX and BibTeX installed; latexmk is unavailable.
The explicit equivalent is run from the paper directory:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Only main.tex and references.bib are required as source inputs. The
round0_snapshot/cold_build_1 and cold_build_2 directories start with those
two files only; each invokes the above sequence and produces the identical
four-page PDF. Earlier qa_round0 builds are development checks, not the
final frozen source-only receipt.

PDF SHA-256: b6ba18a10e83281c1dd491b47cf5d8513ab9914933c659411c8d5c24b72478a0.
Source SHA-256: 33e5e27fe6c9cedef8490bc33628ce06dcef0416784ed4e2671c341cdbc80beb.
All info fields are empty, dates/trailer identifiers are suppressed, and
all fonts are embedded. Main build has zero undefined citations/references,
zero overfull boxes and no remaining TeX warnings. Visual QA covers four
pages; the last page contains the bibliography.

Run the bounded exact verifier with:

    python3 -B code/verify.py

Two fresh executions are preserved as code/RUN1.txt and RUN2.txt and equal
code/CANONICAL.txt byte-for-byte:
0b9a1f131984c427db95d8443470a280129b4863b4f92e817e484f99fc13c0ff.
Each checks 146,600 complete states, n=0,...,7, with 1,496,779 assertions.
No external imports are needed. This author reused their Stage-1 control;
the replay does not create a new independent review.

main_round0_original.pdf and round0_snapshot/ are immutable after the
Round 0 handoff. Later revisions must preserve these bytes.
