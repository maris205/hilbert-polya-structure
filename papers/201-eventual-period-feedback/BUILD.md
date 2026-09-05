# P201 reproducible Round0 build

Tools: Python 3 standard library, pdfLaTeX and BibTeX with the TeX packages listed in main.tex. No third-party Python dependency. latexmk was unavailable and not used.

## Executed capture

The author ran `python3 code/build_round0.py attempt1`. Two fresh verifier processes both matched code/CANONICAL.txt byte for byte with empty stderr. Two separate directories, each initially containing only main.tex and references.bib, each ran pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX. Their PDFs are identical bytes.

Environment: SOURCE_DATE_EPOCH=1704067200; TZ=UTC; PYTHONDONTWRITEBYTECODE=1. TeX suppresses date metadata, trailer IDs and identifying PDF fields. The complete [receipt](qa_round0/attempt1/RECEIPT.json), verifier stdout/stderr, per-pass build stdout and final logs are retained.

## Replay without overwriting originals

From the paper directory:

```sh
python3 code/verify.py
sha256sum main.pdf main_round0_original.pdf
cd round0_frozen
sha256sum -c SHA256SUMS
```

Verifier output must exactly equal code/CANONICAL.txt. The retained two fresh stdout files already do; independently replay using new subprocesses to certify a new review.

For a cold LaTeX replay, create a new mktemp directory, copy only round0_frozen/main.tex and round0_frozen/references.bib there, set the recorded environment, and execute:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Compare the new main.pdf to main_round0_original.pdf. No existing auxiliary files may be reused for a cold-build claim.

code/build_round0.py refuses existing attempts, originals and frozen directories. It is a preserved capture implementation, not a command to overwrite Round0 after review. Later changes require their own snapshots and receipts.

Result: five A4 pages, all fonts embedded. Frozen PDF SHA256:
`7711af8b9cf8b31f0c8a0514ad4b31d7709626a9faf77c1e2c633064c77d15a4`.

This is author build evidence only. Review A/B remain unrun at author handoff.

