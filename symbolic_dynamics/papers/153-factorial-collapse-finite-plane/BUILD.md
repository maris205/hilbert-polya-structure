# Build and Round-2 freeze record — P153

**Status: ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL.**

Requirements: a standard TeX Live installation with amsart, natbib, hyperref,
cleveref, microtype, and Latin Modern; Python 3 for the verifier.  Microtype
protrusion remains enabled, while font expansion is disabled explicitly to
avoid engine-order-dependent expansion initialization warnings.

From this directory run:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Exact replay:

    PYTHONDONTWRITEBYTECODE=1 python3 verify.py

The replay must match CANONICAL.txt byte for byte and end with
18,942,551 assertions and PASS_EXACT_REPLAY.

The TeX preamble removes timestamps, trailer IDs, and producer-side pTeX
metadata. Repeating the four-step build in the same environment produces the
same SHA-256 digest.

## Historical and current artifacts

| Stage | Artifact | Settled value |
|---|---|---|
| Round 0 | `main_round0_original.pdf` | 5 A4 pages, 393,462 bytes, SHA-256 `8940cc2979406cd788e9a1c2ed23cb76422c50ff92fe99723608d0cfcb8dfd77` |
| Round 1 | `main_round1.pdf` | 5 A4 pages, 394,720 bytes, SHA-256 `81e56c67a1029add2bc93aaf67add40cbc68016a82e8eb2a1b7025cad2d3bb7a` |
| Round 2 | `main.pdf`, `main_round2.pdf` | byte-identical; 5 A4 pages, 392,821 bytes, SHA-256 `ef8c82be2935ed23c406a7c688138400d9c76924d11f9d5c089893e8747049a5` |

Round-0 and Round-1 PDFs remain unchanged.  Two independent temporary
directories containing only `main.tex` and `references.bib` completed the
four-command sequence and reproduced the current/Round-2 PDF byte for byte.

The settled log has no build error, unresolved citation/reference, rerun
request, overfull/underfull box, or LaTeX/package warning.  Microtype
protrusion remains enabled and font expansion is explicitly disabled; the
former pdfTeX expansion-initialization warning is absent.  All 30 reported
font rows are embedded, subsetted, and Unicode mapped.  PDF metadata fields
for title, author, subject, and keywords are blank; the file is A4,
unencrypted, and contains no form or JavaScript.

Review A returned 0 Critical / 0 Major / 2 Minor and Review B returned
0 Critical / 0 Major / 2 Minor.  Every item is closed, leaving surviving
severity 0 / 0 / 0.  After these ledgers settle, the separately maintained
final `SHA256SUMS` covers all 25 other retained paper-local files.  No
external service is part of this record; scoped repository synchronization is
recorded at the batch level.
