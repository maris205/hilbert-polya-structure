# COMPILATION REPORT — SD-C19

## Deliverable

- Title: *Genuine Fiber Symmetry after Relabeling Failure: Artin Character
  Factors of the Tensor-Atom Shift*
- Candidate: **SD-C19**
- Primary system family: **Symbolic Dynamics**
- PDF: **main.pdf**
- Page count: **19**
- Page geometry: **A4**, 595.276 × 841.89 pt, rotation 0
- File size: **439,969 bytes**
- PDF SHA-256:
  **1fdb100515cecdf2f776bd487933ba792091ad0f1ee53c29fe343290fce06e18**

## Toolchain

- pdfTeX 3.141592653-2.6-1.40.22
- TeX Live 2022/dev/Debian
- BibTeX 0.99d
- Bibliography style: plainnat

## Final build protocol

The bibliography database was rebuilt once, followed by four consecutive
final commands:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

All four passes exited successfully.  Every pass produced the same 19-page,
439,969-byte PDF.  The four final logs contain:

- zero LaTeX/package warnings;
- zero overfull or underfull boxes;
- zero undefined or multiply defined references;
- zero undefined citations;
- zero fatal errors.

The BibTeX log contains no warning or error.

## Citation and link audit

- Bibliography entries: **12**
- Distinct cited keys: **12**
- Cited-but-missing keys: **0**
- Uncited bibliography entries: **0**
- README relative links after report creation: **all targets present**
- Hyperref PDF-string warnings: **0**
- Unresolved internal references in extracted PDF text: **0**

The audit checked the Route-A tuple, Route-B lock, certificate counts, and the
base/lifted primitive distinction in extracted PDF text.  The PDF contains no
drafting marker, undefined-reference marker, or target-zero claim.

## Font and visual audit

pdffonts lists **24** font objects.  Every font is embedded and subset; all
listed fonts have Unicode maps.  The document uses Latin Modern and the
embedded AMS blackboard-bold font.

Pages 1, 6, and 13 were rasterized and inspected at 120 dpi.  This covers the
title/status box, the Artin factorization figure, displayed determinant
identities, the strict Route-A table, and the boxed route tuple.  No clipping,
collision, overflow, or illegible label was observed.

## Source hashes

- main.tex:
  **51cc2c2c3f0600b2984a352a3549e6dd954d1b72a4faabdb414afa52de680587**
- references.bib:
  **471479cacfafd9b6ad70abeda20cae55d4a1f66ac80f625a5561825a39481bd2**

## Cleanup

The final paper directory retains the manuscript sources, bibliography,
figure source, Markdown authority packages, and main.pdf.  LaTeX/BibTeX
intermediates (.aux, .bbl, .blg, .log, .out, .toc, .fls, .fdb_latexmk, and
.synctex.gz) were removed after verification.
