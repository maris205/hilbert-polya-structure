# P198 reproducible Round0 build

The recorded build used Python 3, pdfLaTeX, BibTeX, Latin Modern and the packages named in main.tex. No Python third-party package is required; latexmk was not available and was not used.

## Completed cold procedure

The author ran `python3 code/build_round0.py attempt1`. It started two fresh verifier subprocesses, compared stdout with code/CANONICAL.txt, then created two physically separate source-only build directories. Each received only main.tex and references.bib and ran pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX. Both PDFs were byte-identical. The environment set SOURCE_DATE_EPOCH=1704067200, TZ=UTC and PYTHONDONTWRITEBYTECODE=1. Dates, trailer IDs, producer metadata and author metadata are suppressed in the TeX preamble.

The actual [receipt](qa_round0/attempt1/RECEIPT.json), both stdout/stderr pairs, all eight build-pass stdout files and final logs are retained. This is executed evidence, not a suggested unrun workflow.

## Read-only replay

From this paper directory:

```sh
python3 code/verify.py
sha256sum main.pdf main_round0_original.pdf
cd round0_frozen
sha256sum -c SHA256SUMS
```

The verifier stdout must equal code/CANONICAL.txt byte for byte. An independent replay should use fresh subprocess capture; the retained verifier1.stdout and verifier2.stdout both already meet this check.

For an independent LaTeX rebuild, create a new temporary directory with mktemp -d, copy only frozen main.tex and references.bib into it, set the recorded environment, and run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Compare the resulting PDF against the frozen original. Do not reuse the existing build directory or auxiliary files when claiming a cold build.

The capture script intentionally refuses to overwrite any existing attempt or frozen original. Do not rerun it in place to replace Round0. Review-driven changes belong in later versions and must preserve main_round0_original.pdf and round0_frozen/.

## Artifact result

Four A4 pages; all fonts embedded. PDF SHA256:
`575d7382ed14715591a86e4f42599b3b5d131f859e498b68e564bc351acb14dd`.

This build and its canonical tests are author checks. They do not constitute Review A, Review B, human review or external owner clearance.

